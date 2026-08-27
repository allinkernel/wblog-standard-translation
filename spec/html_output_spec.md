# 三兄弟 HTML 输出规范（html_output_spec.md）——完全适配 template.html

> **版本**：v1.0（2026-08-27）
> **适用**：三兄弟的**全部** `index.html` 产物——英文原文镜像（老大）、中文直译（老二）、AI 导读（老三）——在嵌入博客前必须满足本规范，**完全适配 `template/template.html` 的渲染模板**（大纲、代码块、表格工具栏、主题、阅读设置全部生效）。
> **上游规范**：`template/template对输入的html的要求.md` 是模板侧的总规范（289 行，**以它为准**）；本文只规定「官方 HTML → 三兄弟产物」的**转换规则**与**与官方标签的映射**。
> **配套**：`spec/html_spec.md`（DOM 抽取→翻译→回填）产出的是"官方结构的中文 HTML"；本规范是**最终适配层**——回填产物与本规范冲突时，按本规范转换（只改结构表达，**不改文本内容**）。
> **执行区隔**：标有 **[Agent 执行]** 或"必须/禁止/一律/铁律"的条目是硬性约束。

---

## 1. 核心原则

**内容不变、结构适配**：转换只改变 HTML 的结构表达（标签、属性、容器），**绝不改变文本内容**（原文内容正确 > 原文排版正确 > 译文正确 > 译文排版）。官方 HTML 的样式（官方 CSS）在模板中不生效——模板主题接管视觉，转换的目标是让模板的渲染机制（大纲/代码/表格/图片）全部工作。

**生成即合规**：转换后的 `index.html` 必须**直接满足** template 规范，不得依赖构建脚本兜底。

---

## 2. 统一输出形态

- 文件名：`index.html`，UTF-8。
- 双形态：完整 HTML 文档（可独立拖入浏览器）或 body 片段（模板剥壳后渲染）均可；**模板渲染时剥壳**，因此 `<head>` 中的渲染 CSS 仅用于独立打开（可选，不加也行）。
- **`<body>` 内第一个节点必须且只能是 `<h1>`**（文章标题），`<h1>` 之前禁止任何标签/文本/注释。
  - 老大（原文镜像）：`<h1>` = 官方章节标题的完整形式（如 `System Interfaces — 2. General Information`，或官方 `<title>` 文本）；
  - 老二（直译）：`<h1>` = 章标题直译（如 `2. 通用信息 (General Information)`）；
  - 老三（导读）：`<h1>` = 导读标题（如 `导读：2. 通用信息 (General Information)`）。
- `<h1>` 之后可紧跟 `<blockquote>` 说明来源（官方 URL、生成方式等）。

---

## 3. 转换规则（官方 HTML / 回填产物 → template 适配）

### 3.1 标题

| 官方/回填形态 | 转换后 | 说明 |
| --- | --- | --- |
| `<h2><a name="tag_15" id="tag_15"></a>2. General Information</h2>` | `<a id="tag_15" name="tag_15"></a><h2>2. 通用信息 (General Information)</h2>` | **锚点移到标题外**（template 禁标题内嵌 `<a>`）；锚点元素保留 `id`/`name` 供站内 `#tag_xx` 跳转 |
| 标题内嵌 `<code>` | 保留 `<code>` | template 允许标题内行内代码 |
| 标题内其它标签（`<i>`、`<b>` 等） | 剥成纯文本 | 标题内仅纯文本 + `<code>` |
| 标题跳级（h2→h4） | 逐级补齐/调整 | 官方一般逐级；若出现跳级，补一级空标题不可行时降级为段落加粗（**原则上避免**，转换器应检测并报告） |

**[Agent 执行] 锚点铁律**：官方 `id="tag_xx"` / `name="tag_xx"` 锚点**必须保留**（正文交叉引用 `href="#tag_xx"` 依赖它），但**必须放在标题元素之外**（`<a id="tag_xx"></a>` 独立元素，紧邻标题前）。禁止删除锚点。模板自动生成的大纲锚点（`toc-anchor-N`）与官方锚点不冲突（自动跳过已有 id 的标题——注意：**标题自身不要写 id**，官方锚点 id 放在独立 `<a>` 上）。

### 3.2 文本与空白

- 裸 `<` `>` `&` 必须转义（`&lt;` / `&gt;` / `&amp;`）——回填产物已做（fill_blocks 的 escape_text），转换器复核。
- **[Agent 执行] `&nbsp;` 铁律**：官方正文的 `&nbsp;`（不间断空格）**全部转换为普通空格**（ASCII 32）——template 禁止不可见控制字符（`\u00A0`）与连续 `&nbsp;` 调间距。注意：**只转换实体形式** `&nbsp;` 与 `&#160;`；已渲染为 `\u00A0` 的（若有）一并替换。
- 段落用 `<p>`；禁止用 `<br>` 制造段落间距（官方正文 `<br>` 罕见，表格单元格内 `<br>` 数据分行允许）。
- 正文文本必须在容器内（`<p>/<li>/<td>/<blockquote>`），禁止 body/div 下裸文本。

### 3.3 代码块

- 官方 `<pre>代码</pre>` → `<pre><code class="language-plaintext">代码</code></pre>`。
- **[Agent 执行] 紧贴与转义**：`<pre>` 与 `<code>` 之间、`<code>` 内容首尾**不得有空白/换行**；代码内部 `<` `>` `&` 必须**且仅一次**转义（官方 HTML 中已是 `&lt;` 等实体，保持原样，**不得二次转义**）。
- `language-` 类名：无明确语言时一律 `language-plaintext`；可启发识别 shell（`language-sh`）、C（`language-c`）、make（`language-make`）、JSON（`language-json`）等，但**拿不准就用 plaintext**。
- 代码内部**纯文本**：官方 `<pre>` 内若有嵌套标签（罕见），剥成纯文本（保留换行）。
- 行内 `<tt>` → `<code>`（template 禁 `<tt>`）；行内 `<code>` 内部同样严格转义。

### 3.4 表格（最复杂，转换器核心）

官方表格（无 `<thead>/<tbody>`、带 `colspan/rowspan`、`border` 等属性、单元格内可能含块级）→ template 兼容表格：

1. **结构**：`<table>` → `<table><thead><tr><th>…</th></tr></thead><tbody>…</tbody></table>`。官方表格首行若语义上是表头（全 `<th>` 或首行加粗）→ 转 `<thead>`；否则第一行作为表头行（template 表格必须带 thead 一行）。
2. **[Agent 执行] colspan/rowspan 展开**：template 列宽拖拽不支持合并单元格 → **展开为重复单元格**：`colspan=N` → 该单元格复制 N 份；`rowspan=N` → 后续 N-1 行对应位置插入相同内容。展开后**每行 `<td>` 数必须严格相等**。
3. **空单元格**：`<td></td>` → `<td>-</td>`（建议连字符）。
4. **去表现属性**：删除 `border`、`cellpadding`、`cellspacing`、`width`、`bgcolor`、`align`、`style` 等（模板 CSS 接管）；`class` 如非必要也删。
5. **[Agent 执行] 单元格白名单**：`<td>/<th>` 内仅允许文本、`<code>`、`<strong>/<em>/<i>`、`<a>`、`<br>`。官方单元格内的 `<p>`（去标签留文本）、`<pre>`（转 `<code>` 行内，多行拆 `<br>` 或移出表格）、嵌套 `<table>`（**拆出**为独立表格）、`<ul>/<ol>`（转文本，用 `<br>` 分行）——一律按此转换。
6. 表格后跟的官方"脚注"文本（表格下方的 `<p>` 说明）保留为普通段落。

> **保真权衡**：colspan/rowspan 展开后视觉网格与官方一致（内容逐格对应），列宽由模板自适应。转换后**逐格核对**：行数、列数、每个单元格文本与官方一致。

### 3.5 图片

- `<img src=".pic/opt-start.gif" alt="Option Start">` 保留（alt 已有）。**alt 必填**：官方 alt 为空 → 补描述（如 `alt="Option Start 标记"`）；alt 内禁裸双引号。
- `src` 相对路径（`.pic/`）或完整 URL；文件名英文小写/数字/下划线（官方 `opt-start.gif` 合规）。

### 3.6 链接

| 官方链接形态 | 转换后 | 说明 |
| --- | --- | --- |
| `<a href="#tag_19_03">2.3 Token Recognition</a>`（站内锚点） | **保留**（`href="#tag_xx"` 不变，目标锚点已外移保留） | 正文交叉引用必须保留 |
| `<a href="../basedefs/V1_chap01.html">XBD</a>`（跨页官方链接） | **剥成纯文本**（`XBD`） | template 禁 `../xxx.html` 官方文档相对链接（构建后 404）；译文里可改为文字引用（如 `XBD（见 Base Definitions 卷）`） |
| `<a href="https://…">`（外部完整 URL） | 保留 | URL 中 `&` 写 `&amp;` |
| 站内文章链接 | 相对路径省略 `.html`（如 `./2.general-information/index`） | 三兄弟互链时用 |

### 3.7 引用块（blockquote）

- 官方 `<blockquote>` 内容必须是 `<p>/<ul>/<ol>` + 行内元素；**禁内嵌 `<pre>`/`<table>`**。官方 blockquote 内若含代码/表格 → 拆出为块级（引用块只留文本，代码/表格移到引用块外）。

### 3.8 列表

- `<ul>/<ol>` 直接子元素必须是 `<li>`；嵌套列表完全包在父 `<li>` 内；`<li>` 内文本先于子列表/代码块。
- 官方 `<dl>`（定义列表）→ **转 `<ul><li><strong>term</strong>：definition</li></ul>`**（template 无 dl 样式；term 用 `<strong>`，dt/dd 合并进同一 `<li>`）。

### 3.9 禁用标签/属性映射（官方 → template）

| 官方标签/属性 | 转换 |
| --- | --- |
| `<tt>` | `<code>` |
| `<font>`、`<center>` | 去标签留文本 |
| `<hr>` | 删除（正文禁 `<hr>`） |
| `<sup>/<sub>` | 保留（数学/化学符号） |
| `<kbd>/<samp>` | 保留（模板有样式） |
| `<mark>` | `<strong>` |
| `<script>/<style>/<iframe>/<form>/<svg>/<details>/<summary>` | 删除（正文禁）——官方正文不含，若 NAVHEADER 清理不彻底则删 |
| `bgcolor`、`border="…"`、`width="…%"`、`style="…"`、`align` | 删除 |
| 文档导航（Previous/Home/Next）、版权横幅 | 删除（`html_spec` 的 clean 已做，转换器复核） |
| `&nbsp;`、`&#160;` | 普通空格 |

---

## 4. 转换流程（[Agent 执行]）

```
回填产物 / 官方 HTML（html_spec 流程输出）
        │
        ▼
python 转换器（tools/adapt_template.py，基于 tools/dom.py）
  ├─ 加 <h1>（文章标题，参数化）
  ├─ 标题锚点外移（保留 id/name）
  ├─ &nbsp; → 空格；文本实体复核
  ├─ <pre> → <pre><code class="language-xxx">
  ├─ 表格：thead/tbody + colspan/rowspan 展开 + 白名单 + 去属性
  ├─ <tt>/<font>/<center>/<hr> 映射
  ├─ 跨页链接剥文本；站内锚点保留
  └─ 图片 alt 复核
        │
        ▼
验证（见 5）→ 输出 index.html
```

转换器**只改结构不改文本**：转换前后做"文本内容一致性断言"（剥离全部标签后文本应逐字一致，除 `&nbsp;`→空格、跨页链接剥文本等已声明变更）。

---

## 5. 验证清单（每篇必跑）

1. **h1 铁律**：`<body>` 第一个节点是 `<h1>`，h1 前无内容；
2. **标题**：逐级递减、无跳级；标题内仅文本+`<code>`；官方 `id/name="tag_xx"` 锚点全部保留（数量与官方一致）且在标题外；
3. **实体**：无未转义裸 `<`（除标签）、无 `&nbsp;`/`\u00A0`/其它不可见字符；无二次转义（`&amp;lt;` 残留 0）；
4. **代码块**：全部 `<pre>` 已包 `<code class="language-*">`；pre/code 紧贴；代码内实体单次转义；
5. **表格**：全部 `<table>` 含 `<thead>+<tbody>`；每行 `<td>` 数 == `<th>` 数；无 colspan/rowspan；单元格无块级嵌套；行数列数与官方逐格一致（转换器断言）；
6. **禁用项**：无 `<tt>/<font>/<center>/<hr>/<mark>/<script>/<style>/<details>`；无 `bgcolor/border/width%/style` 属性；无 NAVHEADER/版权横幅；
7. **链接**：无 `../xxx.html` 官方相对链接；站内 `#tag_xx` 锚点目标存在；
8. **文本一致性**：剥标签后文本与转换前一致（除声明变更）；
9. **渲染冒烟**：`template.html` 环境下打开（或 `article.innerHTML` 注入）无布局崩坏——大纲标题、代码块行号、表格工具栏可见。

---

## 6. 与既有规范的关系

- `html_spec.md`：定义「官方 HTML → 中文 HTML」的抽取/翻译/回填；其产物是**官方结构的 HTML**。
- 本规范（`html_output_spec.md`）：定义「三兄弟 HTML → template 适配 HTML」的**最终转换**；两阶段衔接：
  `官方 HTML →(html_spec) 回填 HTML →(本规范) template 适配 index.html`。
- 英文原文镜像（老大）也走本规范的转换（官方 HTML → 适配），保留全部文本与锚点，仅改结构。
- `spec.md` 总入口第 9 节示例与 `md_spec.md` 的 pandoc 编译说明：产物若为 HTML 直出，不再依赖 pandoc，直接走本规范；若仍用 pandoc 编译 markdown，pandoc 输出本身满足大部分 template 规范（fragment），再按本规范复核。
