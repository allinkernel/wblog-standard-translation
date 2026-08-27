#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_blocks.py v2 —— HTML → 可翻译纯文本块（基于 tools/dom.py 轻量 DOM）
============================================================================

用法：
    python3 extract_blocks.py <index.html> <out_dir>
输出：
    out_dir/.chunks/NNNN.txt（块文本，每行 "[node_id] 文本"）
    out_dir/.chunks/manifest.json（节点：id/type/path/text/placeholders/context）

回填：tools/fill_blocks.py 按 path 原位替换，输出 xxx-translate/index.html。
规则对应 html_spec 3.1/3.2/3.4：块级最小单元、行内标签→占位符、表格带语义上下文、h2/h3 分块。
"""

import argparse
import html as html_mod
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dom import build, path_of, serialize

BLOCK_TAGS = {'p', 'h2', 'h3', 'h4', 'h5', 'li', 'td', 'th', 'dt', 'dd', 'blockquote', 'caption'}
INLINE_TRANSLATE = {'a', 'b', 'i', 'em', 'strong', 'sup', 'sub', 'span', 'font', 'u', 'small', 'big', 'q', 'abbr'}
INLINE_SKIP = {'code', 'tt'}
SKIP_TAGS = {'script', 'style', 'nav', 'noscript', 'head', 'iframe'}
VOID_KNOWN = {'br', 'img', 'hr'}


class Counter:
    def __init__(self):
        self.n = 0

    def next(self, prefix):
        self.n += 1
        return f"{prefix}{self.n}"


def collect_text(node, counter, ph_map, out_parts, skip_flag):
    """递归收集节点文本：行内可译标签→[X5]...[/X5]，code/tt/pre→整体占位符，br→换行。"""
    if node.is_text():
        out_parts.append(node.data)
        return
    if node.tag in SKIP_TAGS:
        return
    if node.tag in ('code', 'tt'):
        raw = serialize(node)
        ph = counter.next("CODE")
        ph_map[ph] = {"open": "", "close": "", "translate": False, "raw": raw}
        out_parts.append(f"[{ph}]")
        return
    if node.tag in ('img', 'hr'):
        raw = serialize(node)
        ph = counter.next("IMG")
        ph_map[ph] = {"open": "", "close": "", "translate": False, "raw": raw}
        out_parts.append(f"[{ph}]")
        return
    if node.tag == 'pre':
        raw = serialize(node)
        ph = counter.next("PRE")
        ph_map[ph] = {"open": "", "close": "", "translate": False, "raw": raw}
        out_parts.append(f"[{ph}]")
        return
    if node.tag == 'br':
        out_parts.append("\n")
        return
    if node.tag in INLINE_TRANSLATE:
        ph = counter.next(node.tag[0].upper())
        ph_map[ph] = {"open": serialize_open(node), "close": f"</{node.tag}>", "translate": True}
        out_parts.append(f"[{ph}]")
        for ch in node.children:
            collect_text(ch, counter, ph_map, out_parts, skip_flag)
        out_parts.append(f"[/{ph}]")
        return
    if node.tag in BLOCK_TAGS or node.tag in ('div', 'section', 'article', 'dl', 'ul', 'ol', 'tr', 'table', 'tbody', 'thead'):
        for ch in node.children:
            collect_text(ch, counter, ph_map, out_parts, skip_flag)
        return
    # 未知行内标签：取其文本
    for ch in node.children:
        collect_text(ch, counter, ph_map, out_parts, skip_flag)


def serialize_open(node):
    a = "".join(f' {k}="{html_mod.escape(v, quote=True)}"' for k, v in node.attrs.items())
    return f"<{node.tag}{a}>"


def is_block_leaf(node):
    """块级且无块级子节点（叶子块）→ 最小翻译单元。"""
    if node.tag not in BLOCK_TAGS:
        return False
    for ch in node.children:
        if not ch.is_text() and ch.tag in BLOCK_TAGS:
            return False
    return True


def is_chunk_boundary(node):
    return node.tag in ('h2', 'h3')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('html')
    ap.add_argument('out_dir')
    args = ap.parse_args()

    with open(args.html, encoding='utf-8') as f:
        src = f.read()

    # 去 NAVHEADER/NAVFOOTER/注释
    src = re.sub(r'<div class="NAVHEADER">.*?</div>', '', src, flags=re.S)
    src = re.sub(r'<div class="NAVFOOTER">.*?</div>', '', src, flags=re.S)
    src = re.sub(r'<!--.*?-->', '', src, flags=re.S)

    root = build(src)
    body = None
    for ch in root.children:
        if not ch.is_text() and ch.tag == 'body':
            body = ch
            break
    if body is None:
        body = root

    chunks_dir = os.path.join(args.out_dir, '.chunks')
    os.makedirs(chunks_dir, exist_ok=True)

    counter = Counter()
    manifest = {}
    chunk_no = 0
    chunk_nodes = []
    chunk_title = ""
    node_seq = 0

    def emit_node(node, ntype, text, placeholders, context=None):
        nonlocal node_seq
        node_seq += 1
        nid = f"{ntype}_{node_seq:05d}"
        return {"id": nid, "type": ntype, "path": path_of(node, root),
                "text": text.strip(), "placeholders": placeholders, "context": context}

    def sink():
        nonlocal chunk_no, chunk_title, chunk_nodes
        if not chunk_nodes:
            return
        chunk_no += 1
        cid = f"{chunk_no:04d}"
        lines = []
        for n in chunk_nodes:
            ctx = f" ctx={json.dumps(n['context'], ensure_ascii=False)}" if n.get("context") else ""
            # 节点文本单行化：内部换行（<br> 等）替换为空格，保证物理行数 == 节点数
            text = n['text'].replace('\n', ' ')
            lines.append(f"[{n['id']}]{ctx} {text}")
        with open(os.path.join(chunks_dir, f"{cid}.txt"), 'w', encoding='utf-8') as f:
            f.write("\n".join(lines))
        manifest[cid] = {"title": chunk_title, "nodes": chunk_nodes}
        chunk_nodes = []

    def walk(node):
        nonlocal chunk_title
        if node.is_text() or node.tag in SKIP_TAGS:
            return
        if is_chunk_boundary(node):
            sink()
            title = "".join(t.data for t in node._walk() if t.is_text()).strip()
            chunk_title = title
        if node.tag == 'table':
            # 表格：表头作上下文，单元格为节点
            emit_table(node)
            return
        if is_block_leaf(node):
            ph_map = {}
            parts = []
            collect_text(node, counter, ph_map, parts, False)
            text = "".join(parts).strip()
            if text:
                chunk_nodes.append(emit_node(node, node.tag, text, ph_map))
            return
        # 非叶子块：递归
        for ch in node.children:
            walk(ch)

    def emit_table(table_node):
        """表格单元格节点（带行头/列头上下文），跳过表头行本身。"""
        rows = []
        title = ""
        for ch in table_node.children:
            if not ch.is_text() and ch.tag == 'caption':
                title = "".join(t.data for t in ch._walk() if t.is_text()).strip()
            elif not ch.is_text() and ch.tag == 'tr':
                rows.append([td for td in ch.children if not td.is_text() and td.tag in ('td', 'th')])
        header = rows[0] if rows else []
        header_texts = ["".join(t.data for t in td._walk() if t.is_text()).strip() for td in header]
        for r, row in enumerate(rows):
            if r == 0:
                continue
            for c, td in enumerate(row):
                ph_map = {}
                parts = []
                collect_text(td, counter, ph_map, parts, False)
                text = "".join(parts).strip()
                if not text:
                    continue
                ctx_bits = []
                if title:
                    ctx_bits.append(f"表题: {title}")
                if c == 0:
                    ctx_bits.append(f"行 {r}: {text[:30]}")
                elif header_texts and c < len(header_texts) and header_texts[c]:
                    ctx_bits.append(f"列头: {header_texts[c]}")
                context = "；".join(ctx_bits) if ctx_bits else None
                chunk_nodes.append(emit_node(td, 'td', text, ph_map, context))

    walk(body)
    sink()

    with open(os.path.join(chunks_dir, 'manifest.json'), 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    total = sum(len(v['nodes']) for v in manifest.values())
    print(f"完成：{chunk_no} 块 / {total} 节点 → {chunks_dir}")


if __name__ == '__main__':
    main()
