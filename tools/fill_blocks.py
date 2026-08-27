#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fill_blocks.py —— 译文 JSON → 原位回填 DOM → 输出 translate/index.html
========================================================================

对应 html_spec 3.3/3.5：
    - LLM 译文 JSON 数组 [{"index":N,"translated_text":"..."}]，index 对应块内节点顺序
    - 尾逗号清洗（re.sub）+ json.loads 容错
    - 回填前 HTML 转义；占位符还原为真实标签；节点级重试信息（缺失 index 列表）

用法：
    python3 fill_blocks.py <index.html> <manifest.json> <translated_dir> <out.html>
    translated_dir 下放子 Agent 译文：NNNN.json（块号与 manifest 一致）
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dom import build, find_path, serialize

PH_RE = re.compile(r'\[([A-Za-z]+)(\d+)\]|\[/([A-Za-z]+)(\d+)\]')


def clean_src(html_text):
    s = re.sub(r'<div class="NAVHEADER">.*?</div>', '', html_text, flags=re.S)
    s = re.sub(r'<div class="NAVFOOTER">.*?</div>', '', s, flags=re.S)
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    return s


def clean_trailing_comma(raw):
    return re.sub(r',\s*\]', ']', raw)


def escape_text(s):
    """回填前 HTML 转义（html_spec 3.3 / pdf_spec 3.4）。
    注意：只转义【裸】& < >——原文已是实体的形式（&lt; &amp; &nbsp; &quot; 等）必须原样保留，
    否则 & 被二次转义成 &amp;lt;，浏览器显示字面 &lt;（双重转义 bug）。
    """
    s = re.sub(r'&(?![a-zA-Z0-9#]+;)', '&amp;', s)  # 非实体 & -> &amp;
    return s.replace('<', '&lt;').replace('>', '&gt;')


def restore_placeholders(translated, ph_map):
    """译文 → HTML 片段：占位符先换特殊标记，文本转义，再还原真实标签。

    返回 (fragment_html, missing_ph)
    """
    # 1) 占位符 → \x00 标记（先于转义保护）
    def repl_open(m):
        ph = f"{m.group(1)}{m.group(2)}"
        info = ph_map.get(ph)
        if not info:
            return m.group(0)
        return f"\x00O{ph}\x00"

    def repl_close(m):
        ph = f"{m.group(3)}{m.group(4)}"
        info = ph_map.get(ph)
        if not info:
            return m.group(0)
        return f"\x00C{ph}\x00"

    s = PH_RE.sub(lambda m: repl_open(m) if m.group(1) else repl_close(m), translated)
    # 2) 文本转义
    s = escape_text(s)
    # 3) \x00 标记 → 真实标签（整体占位符直接还原 raw；成对占位符还原开闭标签）
    for ph, info in ph_map.items():
        if not info.get('translate', True):
            s = s.replace(f"\x00O{ph}\x00", info.get('raw', ''))
            s = s.replace(f"\x00C{ph}\x00", "")
            continue
        s = s.replace(f"\x00O{ph}\x00", info.get('open', ''))
        s = s.replace(f"\x00C{ph}\x00", info.get('close', ''))
    return s


def parse_translation(raw):
    """尾逗号清洗 + 解析，返回 {index: text}。"""
    cleaned = clean_trailing_comma(raw.strip())
    data = json.loads(cleaned)
    if not isinstance(data, list):
        raise ValueError("顶层必须是 JSON 数组")
    out = {}
    for item in data:
        if not isinstance(item, dict) or 'index' not in item or 'translated_text' not in item:
            continue
        out[int(item['index'])] = item['translated_text']
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('html')            # 官方 index.html（工作版，src 已本地化）
    ap.add_argument('manifest')        # .chunks/manifest.json
    ap.add_argument('translated_dir')  # .translated/（NNNN.json）
    ap.add_argument('out')             # translate/index.html
    args = ap.parse_args()

    with open(args.html, encoding='utf-8') as f:
        src = f.read()
    src = clean_src(src)
    root = build(src)

    with open(args.manifest, encoding='utf-8') as f:
        manifest = json.load(f)

    total_missing = []
    import glob
    for cid in sorted(manifest.keys()):
        info = manifest[cid]
        # 支持子块：.translated/{cid}.json 或 {cid}_1.json / {cid}_2.json ...（index 全局对齐）
        files = sorted(glob.glob(os.path.join(args.translated_dir, f"{cid}*.json")))
        if not files:
            total_missing.append(f"{cid}: 译文文件缺失")
            continue
        trans = {}
        parse_errors = []
        for tpath in files:
            with open(tpath, encoding='utf-8') as f:
                try:
                    trans.update(parse_translation(f.read()))
                except (json.JSONDecodeError, ValueError) as e:
                    parse_errors.append(f"{os.path.basename(tpath)}: {e}")
        if parse_errors:
            total_missing.extend(f"{cid}: {pe}" for pe in parse_errors)
            continue
        nodes = info['nodes']
        # index 仅用于保序：按 index 排序后依序对应节点（兼容 agent 输出全局/局部 index 的差异）
        if len(trans) != len(nodes):
            total_missing.append(f"{cid}: 译文 {len(trans)} 条 != 节点 {len(nodes)} 个（缺 {len(nodes)-len(trans)}）")
        ordered = [trans[k] for k in sorted(trans.keys())]
        for node, text in zip(nodes, ordered):
            frag = restore_placeholders(text, node.get('placeholders') or {})
            # 定位 DOM 节点
            target = find_path(root, node['path'])
            if target is None:
                total_missing.append(f"{cid} 节点 {node['id']}: 路径定位失败")
                continue
            # 替换 children 为片段解析出的节点
            frag_root = build(frag)
            target.children = frag_root.children
            for ch in target.children:
                ch.parent = target

    if total_missing:
        print("回填告警（缺译/解析问题）：")
        for m in total_missing:
            print("  -", m)

    with open(args.out, 'w', encoding='utf-8') as f:
        f.write(serialize(root))
    print(f"回填完成 → {args.out}（{len(total_missing)} 条告警）")


if __name__ == '__main__':
    main()
