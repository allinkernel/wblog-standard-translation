#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
adapt_template.py —— 三兄弟 HTML → template.html 适配转换器
================================================================

对应规范：spec/html_output_spec.md（三兄弟 HTML 输出规范，完全适配 template.html）
    - 加 <h1>（body 第一个节点）
    - 标题锚点外移（保留 id/name="tag_xx"，供 #tag_xx 站内跳转）
    - &nbsp;/&#160; → 普通空格（template 禁不可见控制字符）
    - <pre> → <pre><code class="language-plaintext">（紧贴、strip 首尾换行）
    - 表格：thead/tbody + colspan/rowspan 展开 + 首行转 th + 去表现属性 + 空单元格 "-"
    - <tt> → <code>；<font>/<center> 去标签；<hr> 删除
    - 跨页官方相对链接（../xxx.html）剥成纯文本；站内 #tag_xx 与 http(s) 链接保留
    - 删表现属性（bgcolor/border/cellpadding/width%/style/align 等）
    - 文本一致性断言（转换前后剥标签文本对比，忽略已声明变更）

用法：
    python3 adapt_template.py <input.html> <title> <out.html>
    title = 文章 <h1> 文本（如 "2. 通用信息 (General Information)"）
"""

import argparse
import re
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dom import Node, build, serialize

SKIP_TAGS = {'script', 'style', 'iframe', 'form', 'svg', 'details', 'summary', 'nav', 'noscript'}
VOID_KEEP = {'img', 'br', 'hr'}
HEADING_TAGS = {'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}


def clean_input(html_text):
    """剥壳：去 head/NAVHEADER/NAVFOOTER/版权/注释，取 body 内容。"""
    s = re.sub(r'<div class="NAVHEADER">.*?</div>', '', html_text, flags=re.S)
    s = re.sub(r'<div class="NAVFOOTER">.*?</div>', '', html_text, flags=re.S)
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    # 版权块（<center><font size="2">The Open Group Base Specifications...</font></center>）
    s = re.sub(r'<center><font[^>]*>.*?</font></center>', '', s, flags=re.S)
    s = re.sub(r'<head>.*?</head>', '', s, flags=re.S)
    m = re.search(r'<body[^>]*>(.*)</body>', s, flags=re.S)
    if m:
        s = m.group(1)
    else:
        s = re.sub(r'</?(?:html|body)[^>]*>', '', s)
    return s


def text_of(node):
    parts = []
    for n in node._walk():
        if n.is_text():
            parts.append(n.data)
        elif n.tag == 'br':
            parts.append(' ')
    return ''.join(parts)


def set_text_content(node, text):
    """把节点内容替换为纯文本节点。"""
    node.children = [Node(None, parent=node, data=text)]


def fix_entities_in_text(text):
    return text.replace('&nbsp;', ' ').replace('&#160;', ' ')


def move_heading_anchors(root):
    """标题内嵌的空锚点 <a name="tag_x" id="tag_x"></a> 外移到标题前。"""
    for h in root._walk():
        if h.is_text() or h.tag not in HEADING_TAGS:
            continue
        new_children = []
        moved = []
        for ch in h.children:
            if not ch.is_text() and ch.tag == 'a' and not text_of(ch).strip() and ('name' in ch.attrs or 'id' in ch.attrs):
                moved.append(ch)  # 空锚点
            else:
                new_children.append(ch)
        if moved:
            parent = h.parent
            idx = parent.children.index(h)
            parent.children = parent.children[:idx] + moved + parent.children[idx:]
            h.children = new_children


def pre_to_code(root, lang='language-plaintext'):
    """<pre> → <pre><code class="language-plaintext">，内容 strip 首尾空白，子标签剥文本。
    若 <pre> 已直接含 <code> 子节点（导读手写），跳过不二次包裹。"""
    for pre in list(root._walk()):
        if pre.is_text() or pre.tag != 'pre':
            continue
        # 已包裹 <code>：跳过
        if len(pre.children) == 1 and not pre.children[0].is_text() and pre.children[0].tag == 'code':
            continue
        content = text_of(pre).strip('\n\r\t ')
        code = Node('code', {'class': lang}, parent=pre)
        set_text_content(code, content)
        pre.children = [code]
        pre.attrs = {}


def strip_crosspage_links(root):
    """跨页官方相对链接（href 非 #/http 开头）→ 剥成纯文本；站内/外链保留；纯锚点元素（无 href）保留。"""
    for a in list(root._walk()):
        if a.is_text() or a.tag != 'a':
            continue
        href = a.attrs.get('href', '')
        # 保留：纯锚点 / 站内 # / 外链 http / 站内相对 ./ ；只剥官方跨页相对链接（../xxx.html）
        if not href or href.startswith('#') or href.startswith('http') or href.startswith('./'):
            continue
        # 剥成纯文本（防御：节点可能已被其它步骤替换/移除）
        parent = a.parent
        if parent is None:
            continue
        try:
            idx = parent.children.index(a)
        except ValueError:
            continue
        txt = Node(None, parent=parent, data=text_of(a))
        parent.children[idx] = txt


def map_tags(root):
    """<tt>→<code>；<font>/<center> 去标签留文本；<hr> 删除。"""
    for n in list(root._walk()):
        if n.is_text():
            continue
        if n.tag == 'tt':
            n.tag = 'code'
            n.attrs = {}
        elif n.tag in ('font', 'center', 'basefont'):
            # 去表现标签，保留子节点（表格等块级内容不能被吞）
            parent = n.parent
            if parent is None:
                continue
            try:
                idx = parent.children.index(n)
            except ValueError:
                continue
            parent.children[idx:idx + 1] = n.children
            for ch in n.children:
                ch.parent = parent
        elif n.tag == 'hr':
            parent = n.parent
            if parent is not None:
                parent.children.remove(n)
        elif n.tag in SKIP_TAGS:
            parent = n.parent
            if parent is not None:
                parent.children.remove(n)


def strip_presentational_attrs(root):
    BAD = {'bgcolor', 'border', 'cellpadding', 'cellspacing', 'width', 'height',
           'align', 'valign', 'style', 'face', 'color', 'size', 'bgcolor'}
    for n in root._walk():
        if n.is_text():
            continue
        for k in list(n.attrs.keys()):
            if k in BAD:
                del n.attrs[k]
            # class 仅保留在 <code> 上（language-* 是模板硬性要求），其余元素删除
            elif k == 'class' and n.tag != 'code':
                del n.attrs[k]
        if n.tag == 'img':
            n.attrs.setdefault('alt', '图片')


def expand_table(table_node):
    """colspan/rowspan 展开为重复单元格；返回二维文本网格。"""
    rows = []
    for tr in table_node.children:
        if tr.is_text() or tr.tag != 'tr':
            continue
        cells = []
        for td in tr.children:
            if td.is_text() or td.tag not in ('td', 'th'):
                continue
            cs = int(td.attrs.get('colspan', 1) or 1)
            rs = int(td.attrs.get('rowspan', 1) or 1)
            cells.append((text_of(td).strip(), cs, rs))
        rows.append(cells)

    expanded = []
    pending = {}  # col -> text（rowspan 单列继承）
    for row in rows:
        out_row = []
        col = 0
        # 先填继承
        while col in pending and pending[col] is not None:
            out_row.append(pending.pop(col))
            col += 1
        for (text, cs, rs) in row:
            while col in pending and pending[col] is not None:
                out_row.append(pending.pop(col))
                col += 1
            for _ in range(cs):
                out_row.append(text)
                if rs > 1:
                    pending[col] = text
                col += 1
        # 行尾剩余 pending 不填（下一行处理）；但确保本行不空
        expanded.append(out_row)
    # 补尾部 pending
    if expanded and pending:
        for k in sorted(pending.keys()):
            if k < len(expanded[-1]):
                continue
    # 统一列数（按最大）
    maxc = max((len(r) for r in expanded), default=0)
    for r in expanded:
        while len(r) < maxc:
            r.append('-')
        for i in range(len(r)):
            if not r[i].strip():
                r[i] = '-'
    return expanded


def rebuild_table(table_node, grid):
    table_node.attrs = {}
    thead = Node('thead', parent=table_node)
    tbody = Node('tbody', parent=table_node)
    table_node.children = [thead, tbody]
    if grid:
        tr = Node('tr', parent=thead)
        for cell in grid[0]:
            th = Node('th', parent=tr)
            set_text_content(th, cell)
        thead.children = [tr]
    for row in grid[1:]:
        tr = Node('tr', parent=tbody)
        for cell in row:
            td = Node('td', parent=tr)
            set_text_content(td, cell)
        tbody.children.append(tr)


def convert_tables(root):
    for t in list(root._walk()):
        if t.is_text() or t.tag != 'table':
            continue
        # 已合规（含 <thead>）不重复转换，防止二次处理丢内容
        if any(not c.is_text() and c.tag == 'thead' for c in t.children):
            continue
        grid = expand_table(t)
        rebuild_table(t, grid)


def strip_inner_block(root):
    """去块级包裹：<p>/<div>/<dl> 等在正文中保留，但去掉裸文本风险——本函数仅清理 div 包裹。"""
    for n in list(root._walk()):
        if n.is_text() or n.tag not in ('div', 'section', 'article'):
            continue
        # div 去标签（保留子节点）
        parent = n.parent
        idx = parent.children.index(n)
        parent.children[idx:idx + 1] = n.children
        for ch in n.children:
            ch.parent = parent


def add_h1(root, title):
    h1 = Node('h1', parent=root)
    set_text_content(h1, title)
    root.children.insert(0, h1)


def collect_text_snapshot(root):
    """剥标签后全文（归一化空白）——用于一致性断言。"""
    t = text_of(root)
    t = fix_entities_in_text(t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input')
    ap.add_argument('title')
    ap.add_argument('out')
    args = ap.parse_args()

    with open(args.input, encoding='utf-8') as f:
        src = f.read()
    body = clean_input(src)
    before = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', body)).strip()

    root = build(body)

    # 转换序列（顺序敏感：先锚点外移，再剥跨页链接，再标签映射，再表格，最后 h1）
    move_heading_anchors(root)
    strip_crosspage_links(root)
    map_tags(root)
    convert_tables(root)
    strip_inner_block(root)
    pre_to_code(root)
    strip_presentational_attrs(root)
    # &nbsp; 处理（文本节点 data 中）
    for n in root._walk():
        if n.is_text() and ('&nbsp;' in n.data or '&#160;' in n.data):
            n.data = fix_entities_in_text(n.data)
    add_h1(root, args.title)

    after = collect_text_snapshot(root)
    # 一致性断言：比较【去全部空白】后的子串关系（标签数差异会产生空格差，去空白后不受影响）
    # h1 为新增（开头），故 after_flat 应以 title 开头并包含 before_flat
    before_flat = re.sub(r'\s+', '', before)
    after_flat = re.sub(r'\s+', '', after)
    if before_flat not in after_flat:
        print("警告：文本一致性断言未通过（before 去空白后不在 after 中）")
        print("  before 去空白长度:", len(before_flat), " after 去空白长度:", len(after_flat))
        # 找出首个差异
        i = 0
        while i < min(len(before_flat), len(after_flat)) and before_flat[i] == after_flat[i]:
            i += 1
        print("  首个差异 @", i, repr(before_flat[max(0, i-40):i+40]), "VS", repr(after_flat[max(0, i-40):i+40]))

    html = serialize(root)
    with open(args.out, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"完成 → {args.out}（{len(html)} 字节）")


if __name__ == '__main__':
    main()
