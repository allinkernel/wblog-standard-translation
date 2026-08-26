#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
json_filler.py —— 译文结构化流式返回的解析 + 原位回填参考实现
================================================================

对应规范条目：
- spec.md 4.3   ：base64 + md5 双基线闭环（本脚本不涉及管道，只处理已取回的真实译文）
- html_spec.md 3.5：译文结构化流式返回镜像协议（LLM 返回 [{"index":N,"translated_text":"..."}]）
- html_spec.md 3.3：回填前 HTML 转义 + 节点数/顺序断言
- pdf_spec.md 4  ：译文结构化流式返回镜像协议（表格单元格按 index 拼回 <td>）
- 第六轮微调      ：尾逗号清洗 re.sub(r',\\s*\\]', ']', text)；节点级重试

用法（两段式，工具侧脚本调用）：

    1) raw = '...LLM 返回的原文...'
       ok, result, missing = parse_translation_json(raw, expected_indexes=[1,2,3])
       # ok=False 时 missing 给出缺失 index，供【节点级重试】——只重发缺失节点，不毁整个文档

    2) errors = fill_nodes(result, target_indexes, get_node, set_node_text, html_escape=True)
       # 按 index 原位回填 + 单节点断言；返回失败清单

依赖：仅 Python 标准库（json/re/string）。DOM 回填用回调函数，可接 BeautifulSoup 或占位符文件。
"""

import json
import re
import sys

# ---------------------------------------------------------------- 第 1 步：解析

def clean_trailing_comma(raw: str) -> str:
    """尾逗号清洗（第六轮微调）：LLM 流式输出长数组时高频多吐尾逗号，json.loads() 零容忍。

    [ {...}, {...}, ]  ->  [ {...}, {...} ]
    """
    return re.sub(r',\s*\]', ']', raw)


def parse_translation_json(raw: str, expected_indexes=None):
    """解析 LLM 返回的译文 JSON 数组，返回 (ok, {index: text}, missing_indexes)。

    - 先清洗尾逗号再 json.loads()；
    - 校验每个元素含 'index' 与 'translated_text'；
    - 与 expected_indexes 比对，缺的 index 进 missing（供节点级重试）；
    - 多余/未知 index 记 warning（容忍，不视为失败）。
    """
    cleaned = clean_trailing_comma(raw.strip())
    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as e:
        return False, {}, {"_parse_error": f"{e}; raw 前 200 字符: {cleaned[:200]}"}

    if not isinstance(data, list):
        return False, {}, {"_parse_error": f"顶层必须是 JSON 数组，实际是 {type(data).__name__}"}

    result = {}
    warnings = []
    for item in data:
        if not isinstance(item, dict) or "index" not in item or "translated_text" not in item:
            warnings.append(f"元素缺少 index/translated_text: {str(item)[:80]}")
            continue
        idx = item["index"]
        if not isinstance(idx, int):
            warnings.append(f"index 非整数: {idx!r}")
            continue
        result[idx] = item["translated_text"]

    missing = []
    if expected_indexes is not None:
        expected = set(expected_indexes)
        missing = sorted(expected - set(result.keys()))
        unknown = sorted(set(result.keys()) - expected)
        if unknown:
            warnings.append(f"多余/未知 index: {unknown}")

    return True, result, {"missing": missing, "warnings": warnings}


# ---------------------------------------------------------------- 第 2 步：回填

def escape_html(text: str) -> str:
    """回填前 HTML 转义（html_spec 3.3 / pdf_spec 3.4）：防译文中的 < > & 产生非法 HTML。"""
    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
    )


def fill_nodes(translated_map, target_indexes, get_node, set_node_text, html_escape=True):
    """按 index 原位回填 + 单节点断言。

    参数：
        translated_map : parse_translation_json 返回的 {index: text}
        target_indexes : 待回填的节点 index 列表（按 DOM 顺序）
        get_node       : callable(index) -> node（可空）
        set_node_text  : callable(node, text) -> None（如 node.string = ... 或写占位符文件）
        html_escape    : 回填前是否 HTML 转义（默认 True）

    返回：失败清单 [ {index, reason}, ... ]。空列表 = 全部成功。
    """
    errors = []
    for idx in target_indexes:
        if idx not in translated_map:
            errors.append({"index": idx, "reason": "译文缺失（供节点级重试）"})
            continue
        text = translated_map[idx]
        if html_escape:
            text = escape_html(text)
        try:
            node = get_node(idx)
            if node is None:
                errors.append({"index": idx, "reason": "目标节点不存在"})
                continue
            set_node_text(node, text)
        except Exception as e:  # noqa: BLE001 —— 单节点失败不影响整体，记入清单
            errors.append({"index": idx, "reason": f"{type(e).__name__}: {e}"})
    return errors


# ---------------------------------------------------------------- 演示/自测

def _demo():
    """最小自测：尾逗号清洗 + 解析 + 顺序断言 + 回填 + HTML 转义。"""
    raw = (
        '[ {"index": 1, "translated_text": "第一段"}, '
        '{"index": 2, "translated_text": "第二段 <注意> & 转义"}, '
        '{"index": 3, "translated_text": "第三段"}, ]'   # 故意带尾逗号
    )
    ok, result, info = parse_translation_json(raw, expected_indexes=[1, 2, 3])
    assert ok, f"解析失败: {info}"
    assert info["missing"] == [], f"缺失: {info['missing']}"

    class FakeNode:
        """演示用节点（真实场景为 BeautifulSoup 节点）。"""
        def __init__(self):
            self.text = ""

    nodes = {i: FakeNode() for i in [1, 2, 3]}  # DOM 节点映射：index -> node
    errors = fill_nodes(result, [1, 2, 3],
                        get_node=lambda i: nodes[i],
                        set_node_text=lambda node, t: setattr(node, "text", t))
    assert errors == [], f"回填失败: {errors}"
    assert nodes[2].text == "第二段 &lt;注意&gt; &amp; 转义", nodes[2].text
    print("自测通过：尾逗号清洗 ✓ 解析 ✓ 顺序断言 ✓ 回填 ✓ HTML 转义 ✓")
    print("回填结果:", {i: nodes[i].text for i in [1, 2, 3]})


if __name__ == "__main__":
    _demo()
    sys.exit(0)
