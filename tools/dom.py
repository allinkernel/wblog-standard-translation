#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dom.py —— 标准库轻量 DOM 树（html.parser 构建，供 extract_blocks/fill_blocks 共用）
====================================================================================

无 bs4/lxml 环境下的最小 DOM：
    Node(tag, attrs, parent)  节点；children 列表；text 由文本子节点承载
    build(html) -> root       构建树
    serialize(root) -> str    序列化回 HTML
    find_path(root, path)     按子索引路径定位节点
    文本节点：tag == None，attrs={}，text 存 data

保留原始属性（含锚点 name/id），序列化时原样输出；void 元素按 HTML 规则自闭合。
"""

import re
from html.parser import HTMLParser

VOID_TAGS = {'br', 'img', 'hr', 'meta', 'link', 'input', 'area', 'base', 'col',
             'embed', 'source', 'track', 'wbr'}


class Node:
    __slots__ = ('tag', 'attrs', 'children', 'parent', 'data')

    def __init__(self, tag, attrs=None, parent=None, data=None):
        self.tag = tag            # None = 文本节点
        self.attrs = attrs if attrs is not None else {}
        self.children = []
        self.parent = parent
        self.data = data          # 文本节点内容

    def is_text(self):
        return self.tag is None

    def iter_block(self):
        """深度优先遍历（含自身），只产出块级/行内可见节点，跳过 script/style。"""
        for ch in self.children:
            yield from ch._walk()

    def _walk(self):
        yield self
        for ch in self.children:
            yield from ch._walk()


class DOMBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)  # 保留实体，序列化原样
        self.root = Node('__root__')
        self._stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, dict(attrs), parent=self._stack[-1])
        self._stack[-1].children.append(node)
        if tag not in VOID_TAGS:
            self._stack.append(node)

    def handle_startendtag(self, tag, attrs):
        node = Node(tag, dict(attrs), parent=self._stack[-1])
        self._stack[-1].children.append(node)

    def handle_endtag(self, tag):
        for i in range(len(self._stack) - 1, 0, -1):
            if self._stack[i].tag == tag:
                del self._stack[i:]
                break

    def handle_data(self, data):
        if not data:
            return
        self._stack[-1].children.append(Node(None, parent=self._stack[-1], data=data))

    def handle_entityref(self, name):
        self.handle_data(f'&{name};')

    def handle_charref(self, name):
        self.handle_data(f'&#{name};')


def build(html_text):
    b = DOMBuilder()
    b.feed(html_text)
    b.close()
    return b.root


def serialize(node, out=None):
    """序列化子树为 HTML 字符串（保留原始属性顺序与实体）。"""
    if out is None:
        out = []
    if node.is_text():
        out.append(node.data)
        return ''.join(out)
    if node.tag == '__root__':
        for ch in node.children:
            serialize(ch, out)
        return ''.join(out)
    attrs = ''.join(f' {k}="{v}"' for k, v in node.attrs.items())
    if node.tag in VOID_TAGS:
        out.append(f'<{node.tag}{attrs}>')
        return ''.join(out)
    out.append(f'<{node.tag}{attrs}>')
    for ch in node.children:
        serialize(ch, out)
    out.append(f'</{node.tag}>')
    return ''.join(out)


def find_path(node, path):
    """path = [i0, i1, ...] 子索引链，定位节点；越界返回 None。"""
    cur = node
    for i in path:
        if cur is None or i >= len(cur.children):
            return None
        cur = cur.children[i]
    return cur


def path_of(target, root):
    """从 root 到 target 的子索引路径（用于抽取时记录、回填时定位）。"""
    path = []
    cur = target
    while cur is not root and cur.parent is not None:
        p = cur.parent
        try:
            path.append(p.children.index(cur))
        except ValueError:
            return None
        cur = p
    path.reverse()
    return path


def text_content(node):
    """节点纯文本（去标签，实体保留原样）。"""
    parts = []
    for n in node._walk():
        if n.is_text():
            parts.append(n.data)
    return ''.join(parts)


if __name__ == '__main__':
    import sys
    src = open(sys.argv[1], encoding='utf-8').read()
    root = build(src)
    print(serialize(root)[:500])
