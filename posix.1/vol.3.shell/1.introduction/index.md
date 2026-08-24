POSIX Standard (IEEE Std 1003.1-2024 / Issue 8) 的《Shell and Utilities》卷（Vol. 3）全卷分为 4 个主要章节（Chapters）：

### 1. Introduction (引言)

* **1.1 Relationship to Other Documents**：说明与 C Standard、Base Definitions、System Interfaces 等其他 POSIX 卷的关系。
* **1.2 Conformance**：定义符合 POSIX 标准的具体要求。
* **1.3 Utility Limits**：规定实用程序处理的最大限制（如路径长度、命令行参数长度等）。
* **1.4 Utility Description Defaults**：统一规定后文各个 Command/Utility 文档小节的标准格式及默认行为（包括 `NAME`, `SYNOPSIS`, `DESCRIPTION`, `OPTIONS`, `OPERANDS`, `STDIN`, `INPUT FILES`, `ENVIRONMENT VARIABLES`, `ASYNCHRONOUS EVENTS`, `STDOUT`, `STDERR`, `OUTPUT FILES`, `EXTENDED DESCRIPTION`, `EXIT STATUS`, `CONSEQUENCES OF ERRORS`, `APPLICATION USAGE`, `EXAMPLES`, `RATIONALE`, `FUTURE DIRECTIONS`, `CHANGE HISTORY`）。
* **1.5 Considerations for Utilities in Support of Files of Arbitrary Size**：对于支持任意大小文件的工具的规范要求。
* **1.6 Built-In Utilities**：定义内置工具（Built-In Utilities）的分类、查找规则与行为规范。
* **1.7 Intrinsic Utilities**：定义固有工具（Intrinsic Utilities，如 `cd`, `read`, `alias`, `kill` 等）的清单与执行要求。

### 2. Shell Command Language (Shell 命令语言)

* **2.1 Shell Introduction**：Shell 解析和执行命令的总流程。
* **2.2 Quoting**：转义与引用机制（反斜杠 `\`、单引号 `'`、双引号 `"`、ANSI-C 引用 `$'...'`）。
* **2.3 Token Recognition**：词法分析与 Token 识别规则（包括别名替换 `Alias Substitution`）。
* **2.4 Reserved Words**：保留字列表及识别逻辑（`if`, `then`, `else`, `while`, `for`, `case` 等）。
* **2.5 Parameters and Variables**：参数与变量（位置参数、特殊参数如 `$@`, `$*`, `$#`, `$?` 以及环境变量）。
* **2.6 Word Expansions**：扩展机制（波浪号扩展 `Tilde Expansion`、参数扩展 `Parameter Expansion`、命令替换 `Command Substitution`、算术扩展 `Arithmetic Expansion`、字段分割 `Field Splitting`、路径名扩展 `Pathname Expansion`、引用消除 `Quote Removal`）。
* **2.7 Redirection**：重定向机制（`Input/Output Redirection`, `Here-Documents`, `Here-Strings` 等）。
* **2.8 Exit Status and Errors**：退出状态码与错误处理（如 126, 127 等状态码语义）。
* **2.9 Shell Commands**：命令分类（简单命令 `Simple Commands`、管道 `Pipelines`、命令列表 `Lists`、复合命令 `Compound Commands` 如 `if`, `while`, `case`, `{}`、函数定义 `Function Definition Command`）。
* **2.10 Shell Grammar**：Shell 语言的完整 Lexer / Yacc 形式化文法（Formal Grammar）。
* **2.11 Signals and Error Handling**：信号捕捉与错误恢复（如 `trap` 的响应机制）。
* **2.12 Shell Execution Environment**：Shell 执行环境的继承、子 Shell（Subshell）与环境隔离逻辑。
* **2.13 Special Built-In Utilities**：特殊内置命令（如 `break`, `colon`, `continue`, `dot`, `eval`, `exec`, `exit`, `export`, `readonly`, `return`, `set`, `shift`, `times`, `trap`, `unset`）。

### 3. Utilities (实用程序手册)

按字母顺序（A-Z）详细定义系统需提供的标准命令行工具/实用程序（例如 `awk`, `cat`, `cd`, `find`, `grep`, `ls`, `sed`, `sh` 等）。每个工具的规范均遵循 Chapter 1.4 定义的 20 个字段小节结构。

### 4. Extended Description (扩展说明 / 各工具附录)

某些大型实用程序（如 `awk`, `ed`, `lex`, `make`, `sed`, `sh`, `yacc` 等）的复杂交互语法、内置宏或详细语法解析说明，被拆分或收录在此章节作为其 `EXTENDED DESCRIPTION` 的规范延伸。
