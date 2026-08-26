# Shell & Utilities (XCU) 卷大纲

> - [大纲](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/contents.html)
> - [1. Introduction](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap01.html) → [英文原文](1.introduction/index.html) / [中文直译](1.introduction-translate/index.html) / [导读](1.introduction-AI-guide/index.html)
> - [2. Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html) → [英文原文](2.shell/index.html) / [中文直译](2.shell-translate/index.html) / [导读](2.shell-AI-guide/index.html)
> - [3. Utilities](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap03.html) → [工具清单](3.utilities/index.html)

POSIX Standard（IEEE Std 1003.1-2024 / Issue 8）的《Shell and Utilities》卷（Vol. 3）共 **3 个主要章节**（Chapters）。「Extended Description」并非独立章节，而是各复杂工具（如 `awk`、`sed`、`sh`、`make`）规范内部的一个标准小节。

> **三兄弟结构说明**：每章维护三份文档——`英文原文`（官方 HTML 镜像，保留原始标签）、`中文直译`（结构镜像原文，段对段/条对条/层对层，便于中英对照）、`AI 导读`（同编号的结构化讲解，机制层 + 延伸阅读）。

### 1. Introduction（引言）→ [1.introduction/index.md](1.introduction/index.md)

* **1.1 Relationship to Other Documents**：说明与 C Standard、Base Definitions、System Interfaces 等其他 POSIX 卷的关系。
* **1.2 Utility Limits**：规定实用程序处理的最大限制（如路径长度、命令行参数长度等）。
* **1.3 Grammar Conventions**：本卷使用语法标记法的约定（`[ ]`、`...`、`< >`、`|`、斜体、粗体）。
* **1.4 Utility Description Defaults**：统一规定后文各个 Utility 文档小节的标准格式及默认行为（`NAME`、`SYNOPSIS`、`DESCRIPTION`、`OPTIONS`、`OPERANDS`、`STDIN`、`INPUT FILES`、`ENVIRONMENT VARIABLES`、`ASYNCHRONOUS EVENTS`、`STDOUT`、`STDERR`、`OUTPUT FILES`、`EXTENDED DESCRIPTION`、`EXIT STATUS`、`CONSEQUENCES OF ERRORS`、`APPLICATION USAGE`、`EXAMPLES`、`RATIONALE`、`FUTURE DIRECTIONS`、`SEE ALSO`）。
* **1.5 Considerations for Utilities in Support of Files of Arbitrary Size**：支持任意大小文件的工具的规范要求。
* **1.6 Built-In Utilities**：定义内置工具（Built-In Utilities）的分类、查找规则与行为规范。
* **1.7 Intrinsic Utilities**：定义固有工具（Intrinsic Utilities，如 `cd`、`read`、`alias`、`kill` 等）的清单与执行要求。

### 2. Shell Command Language（Shell 命令语言）→ [2.shell/index.md](2.shell/index.md)

* **2.1 Shell Introduction**：Shell 解析和执行命令的总流程。
* **2.2 Quoting**：转义与引用机制（反斜杠 `\`、单引号 `'`、双引号 `"`、ANSI-C 引用 `$'...'`）。
* **2.3 Token Recognition**：词法分析与 Token 识别规则（包括别名替换 Alias Substitution）。
* **2.4 Reserved Words**：保留字列表及识别逻辑（`if`、`then`、`else`、`while`、`for`、`case` 等）。
* **2.5 Parameters and Variables**：参数与变量（位置参数、特殊参数如 `$@`、`$*`、`$#`、`$?` 以及环境变量）。
* **2.6 Word Expansions**：扩展机制（波浪号扩展、参数扩展、命令替换、算术扩展、字段分割、路径名扩展、引用消除）。
* **2.7 Redirection**：重定向机制（Input/Output Redirection、Here-Document 等）。
* **2.8 Exit Status and Errors**：退出状态码与错误处理（如 126、127 等状态码语义）。
* **2.9 Shell Commands**：命令分类（简单命令、管道、命令列表、复合命令如 `if`/`while`/`case`/`{}`、函数定义）。
* **2.10 Shell Grammar**：Shell 语言的完整 Lexer / Yacc 形式化文法（Formal Grammar）。
* **2.11 Job Control**：作业控制（`bg`/`fg`/`jobs` 的作业模型）。
* **2.12 Signals and Error Handling**：信号捕捉与错误恢复（如 `trap` 的响应机制）。
* **2.13 Shell Execution Environment**：Shell 执行环境的继承、子 Shell（Subshell）与环境隔离逻辑。
* **2.14 Pattern Matching Notation**：文件名/模式匹配符号（`*`、`?`、`[...]` 等）。
* **2.15 Special Built-In Utilities**：特殊内置命令（`break`、`colon`、`continue`、`dot`、`eval`、`exec`、`exit`、`export`、`readonly`、`return`、`set`、`shift`、`times`、`trap`、`unset`，官方编号 2.16–2.30）。

### 3. Utilities（实用程序手册）→ [3.utilities/index.md](3.utilities/index.md)

按字母顺序定义系统需提供的 **155 个**标准命令行工具，每个工具遵循 Chapter 1.4 定义的固定小节结构（SYNOPSIS / DESCRIPTION / OPTIONS / ... / EXIT STATUS / RATIONALE / CHANGE HISTORY）：

```
admin alias ar asa at awk basename batch bc bg c17 cal cat cd cflow chgrp
chmod chown cksum cmp comm command compress cp crontab csplit ctags cut
cxref date dd delta df diff dirname du echo ed env ex expand expr false fc
fg file find fold fuser gencat get getconf getopts gettext grep hash head
iconv id ipcrm ipcs jobs join kill lex link ln locale localedef logger
logname lp ls m4 mailx make man mesg mkdir mkfifo more msgfmt mv newgrp
ngettext nice nl nm nohup od paste patch pathchk pax pr printf prs ps pwd
read readlink realpath renice rm rmdel rmdir sact sccs sed sh sleep sort
split strings strip stty tabs tail talk tee test time timeout touch tput
tr true tsort tty type ulimit umask unalias uname uncompress unexpand
unget uniq unlink uucp uudecode uuencode uustat uux val vi wait wc what
who write xargs xgettext yacc zcat
```

> 附录中还保留了 13 个已在 POSIX.1-2024 中移除的旧工具条目（`c99`、`fort77` 及 NQS 批处理 `q*` 系列），仅作历史参考。

### 翻译说明

* 源文档：<https://pubs.opengroup.org/onlinepubs/9799919799/utilities/toc.html>
* 翻译风格：基于对 POSIX 的理解重新组织并突出重点，**不逐字直译**；`WORD`、`NAME`、`SID`、`dot-po` 等具有特殊语义的术语保留原文。
* 术语约定：unspecified=未指定、undefined=未定义、implementation-defined=实现定义，三者严格区分。
