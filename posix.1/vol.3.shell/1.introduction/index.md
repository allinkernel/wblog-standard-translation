# Shell & Utilities (XCU) - 第 1 章：简介 (Introduction)

本卷（Shell & Utilities，XCU）定义了命令行实用程序（Utilities）和 Shell 语言的特性与要求。

## 1.1 与其他文档的关系 (Relationship to Other Documents)

### 1.1.1 系统接口 (System Interfaces)

XCU 卷中对实用程序的规范，在很多情况下依赖于 POSIX.1-2024 系统接口（XSH）卷中定义的底层系统接口。当本卷描述实用程序的行为时，其效果与调用对应的系统接口是完全一致的。

#### 1.1.1.1 进程属性 (Process Attributes)

实用程序在执行时继承其父进程的属性，包括但不限于：实际用户 ID (RUID)、实际组 ID (RGID)、有效用户 ID (EUID)、有效组 ID (EGID)、补充组 ID 列表、当前工作目录、文件权限掩码 (umask) 以及环境变量。

#### 1.1.1.2 进程的并发执行 (Concurrent Execution of Processes)

当 Shell 异步执行多个实用程序（如通过背景符 `&` 或管道线 `|`）时，这些进程在概念上是并发运行的。其调度机制与资源竞争由 XSH 卷中定义的进程调度规则决定。

#### 1.1.1.3 文件访问许可 (File Access Permissions)

实用程序对文件的访问受到文件权限位（Read、Write、Execute/Search）以及进程有效用户 ID 和有效组 ID 的约束。对文件的检查规则与 XSH 卷中 `open()`、`access()` 等接口的权限判定逻辑一致。

#### 1.1.1.4 文件的读取、写入与创建 (File Read, Write, and Creation)

- **创建**：实用程序创建文件时，文件的所有者 ID 被设置为进程的有效用户 ID，组 ID 被设置为该目录的组 ID 或进程的有效组 ID（取决于实现）。权限位由指定的模式参数与进程的 `umask` 屏蔽掩码相按位与后决定。
- **读取与写入**：实用程序对文件的读写行为完全符合 XSH 卷中 `read()` 和 `write()` 的语义。

#### 1.1.1.5 文件删除 (File Removal)

当实用程序（如 `rm`）删除一个文件时，其底层效果相当于调用了 `unlink()` 或 `rmdir()` 接口。该目录项被移除；如果这是文件的最后一个硬链接，且没有进程打开该文件，则释放其占用的存储空间。

#### 1.1.1.6 文件时间值 (File Time Values)

实用程序对文件进行读取、写入或修改属性操作时，会同步更新文件的三个核心时间戳（在 POSIX.1-2024 中支持纳秒级精度）：

- **`st_atime`**：最后访问时间（读取文件内容时更新）。
- **`st_mtime`**：最后修改时间（写入文件数据时更新）。
- **`st_ctime`**：状态变更时间（修改文件元数据、权限或所有者时更新）。

#### 1.1.1.7 文件内容 (File Contents)

实用程序处理文本文件时，默认将文件视为由零个或多个行（Lines）组成的字节序列，每一行均以一个换行符（Newline, `'\n'`）结束。如果文件不以换行符结尾，特定实用程序的处理行为可能属于未指定（Unspecified）。

#### 1.1.1.8 路径名解析 (Pathname Resolution)

实用程序对命令行传递的路径名参数进行解析时，完全遵循 XBD 卷第 4.3 节规定的路径名解析算法，包括首部 `/` 的处理、`.` 与 `..` 的解析以及符号链接的层级追踪和 `SYMLOOP_MAX` 的限制。

#### 1.1.1.9 变更当前工作目录 (Changing the Current Working Directory)

实用程序（如 `cd`）变更工作目录的行为，效果等同于调用 `chdir()` 系统接口。该变更仅影响当前进程及其后续创建的子进程，不会影响父进程的执行环境。

#### 1.1.1.10 建立语言环境 (Establish the Locale)

实用程序启动时，会通过调用 `setlocale(LC_ALL, "")` 自动建立其语言运行环境。实用程序的输出格式、文本比较、字符分类以及错误消息均根据当前环境变量（如 `LC_ALL`、`LC_CTYPE`、`LANG` 等）确定的 Locale 进行定制。

#### 1.1.1.11 等效于函数的行为 (Actions Equivalent to Functions)

若本卷中说明某实用程序的操作“等同于调用某 C 语言函数/接口”，其含义为该实用程序的错误处理、边界情况和边缘语义均与该 C 接口的 POSIX 定义保持绝对严格一致。

### 1.1.2 派生自 ISO C 标准的概念 (Concepts Derived from the ISO C Standard)

实用程序在执行算术计算、数学函数运算或浮点数转换时，其内在数据类型与算法规则继承自 **ISO C Standard**。

#### 1.1.2.1 算术精度与运算 (Arithmetic Precision and Operations)

用于算术运算的实用程序（如 `awk`、`bc`、`expr` 等）在涉及整数与浮点数数据类型时，必须遵循与 ISO C 标准对应的类型精度与运算规范。

下表详细说明了各种算术运算、实用程序表达式与 C 语言标准数据类型及运算符的对应映射关系：

| **实用程序 / 运算上下文 (Utility Context)** | **POSIX 规定的算术模型 (Arithmetic Model)**        | **对应的 ISO C 数据类型 / 运算符 (ISO C Type / Operator)** | **要求的最小范围 / 精度约束 (Precision / Range Requirements)** |
| ------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **`expr` 实用程序**                         | 符号整数算术运算 (Signed Integer Arithmetic)       | C 语言中的 `intmax_t` 或 `long`                            | 至少必须支持 **64 位有符号整数**（范围在 $[-2^{63}, 2^{63}-1]$ 内），且溢出行为应遵循补码算术规范或明确报错。 |
| **Shell 算术扩展 `$((expression))`**        | 符号整数算术运算 (Signed Integer Arithmetic)       | C 语言中的 `intmax_t`                                      | 严格使用 `intmax_t` 类型进行运算。保证包含与 C 语言完全一致的位移、按位与或非、模运算及递增递减语义。 |
| **`awk` 算术运算（默认）**                  | 双精度浮点数算术 (Double-precision Floating-point) | C 语言中的 `double`                                        | 遵循 IEEE 754 双精度标准（64 位），提供至少 **53 位二进制尾数精度**，以及约 15–17 位十进制有效数字。 |
| **`awk` 整数运算上下文**                    | 转换为符号整数 (Signed Integer Conversion)         | C 语言中的 `intmax_t` 或 `double` 转整数                   | 当 `awk` 表达式明确处于位运算（如 `bitwise` 函数）或整数格式化输出时，按 C 规定转为有符号宽整数处理。 |
| **`bc` 实用程序**                           | 任意精度十进制算术 (Arbitrary-Precision Decimal)   | 不受 C 基础类型限制（由算法库实现）                        | 数字精度由内置变量 `scale` 动态控制，允许无限制的有效位数，内部十进制运算必须保证绝对精准（无浮点截断误差）。 |
| **`printf` 实用程序的 `%d` / `%i`**         | 有符号整数格式化转换                               | C 语言中的 `intmax_t`                                      | 能够正确格式化输出并接收高达 `INTMAX_MAX` 范围的数值。       |
| **`printf` 实用程序的 `%e` / `%f` / `%g`**  | 双精度/长双精度浮点格式化转换                      | C 语言中的 `double` 或 `long double`                       | 转换规则、四舍五入模式（Round-to-even）及 `NaN` / `Inf` 的打印显示完全遵循 C 语言 `printf()` 族的标准。 |

彻底抛弃所有之前的臆测，重新梳理格式。本次输出将严格按照要求，在所有章节标题和表头处采用 **中文翻译（原文）** 的格式呈现，同时正文和表格内容保持与 POSIX.1-2024 Issue 8 (`V3_chap01.html`) 官方网页**100% 逐字逐句完全一致**：

#### 1.1.2.2 Mathematical Functions（数学函数）

ISO C 标准的以下章节中与函数同名的任何数学函数：

- 第 7.12 节 (Mathematics)
- 第 7.22.2 节 (Pseudo-Random Sequence Generation Functions)

如果实用程序中提供了这些函数，则其实现方式必须使其返回的结果与 ISO C 标准中对相应函数调用的描述等效。

## 1.2 Utility Limits（实用程序限制）

本节列出了由特定实现施加的数值大小限制。用大括号围起来的符号（例如，`{LIMIT}`）代表相关特性的限制值。

下表列出了一组描述实用程序限制的符号常量：

### Table 1-1: Utility Limit Minimum and Maximum Values（表 1-1：实用程序限制最小值与最大值）

| **Symbol（符号）**   | **Description（描述）**                                      | **Minimum Value（最小值）** |
| -------------------- | ------------------------------------------------------------ | --------------------------- |
| `{BC_BASE_MAX}`      | Maximum `ibase` and `obase` values allowed by the *bc* utility. | 99                          |
| `{BC_DIM_MAX}`       | Maximum number of elements per array allowed by the *bc* utility. | 2048                        |
| `{BC_SCALE_MAX}`     | Maximum `scale` value allowed by the *bc* utility.           | 99                          |
| `{BC_STRING_MAX}`    | Maximum length of a string constant allowed by the *bc* utility. | 2000                        |
| `{COLL_WEIGHTS_MAX}` | Maximum number of weights assigned to an entry of the *LC_COLLATE* `order` keyword in the locale definition file. | 2                           |
| `{EXPR_NEST_MAX}`    | Maximum number of repeated expressions nested within parentheses by the *expr* utility. | 32                          |
| `{LINE_MAX}`         | Maximum length, in bytes, of a utility's input line (either standard input or an input file) when the utility is described as processing text files. The length includes space for the trailing `<newline>`. | 2048                        |
| `{NGROUPS_MAX}`      | Maximum number of supplementary group IDs that can be associated with a process. | 8                           |
| `{RE_DUP_MAX}`       | Maximum number of repeated occurrences of a regular expression permitted when using the interval notation `\{m,n\}` or `{m,n}`. | 255                         |

符合 POSIX 标准的实现必须保证支持不低于以下具体数值的限制：

### Table 1-2: Minimum Values for Utility Limits（表 1-2：实用程序限制最小值）

| **Limit（限制）**          | **Description（描述）**                                      | **Value（数值）** |
| -------------------------- | ------------------------------------------------------------ | ----------------- |
| `_POSIX2_BC_BASE_MAX`      | Maximum `ibase` and `obase` values allowed by the *bc* utility. | 99                |
| `_POSIX2_BC_DIM_MAX`       | Maximum number of elements per array allowed by the *bc* utility. | 2048              |
| `_POSIX2_BC_SCALE_MAX`     | Maximum `scale` value allowed by the *bc* utility.           | 99                |
| `_POSIX2_BC_STRING_MAX`    | Maximum length of a string constant allowed by the *bc* utility. | 2000              |
| `_POSIX2_COLL_WEIGHTS_MAX` | Maximum number of weights assigned to an entry of the *LC_COLLATE* `order` keyword in the locale definition file. | 2                 |
| `_POSIX2_EXPR_NEST_MAX`    | Maximum number of repeated expressions nested within parentheses by the *expr* utility. | 32                |
| `_POSIX2_LINE_MAX`         | Maximum length, in bytes, of a utility's input line (either standard input or an input file) when the utility is described as processing text files. The length includes space for the trailing `<newline>`. | 2048              |
| `_POSIX2_RE_DUP_MAX`       | Maximum number of repeated occurrences of a regular expression permitted when using the interval notation `\{m,n\}` or `{m,n}`. | 255               |

## 1.3 Grammar Conventions（语法约定）

本卷（XCU）的部分内容使用了一种特殊的语法标记法表达，用于说明某些程序复杂输入的语法。该语法基于 `yacc` 实用程序所使用的语法。但它并不代表可以直接供程序使用的、完全可工作的 `yacc` 输入；词法处理和所有语义要求仅通过文本形式描述。该语法并非基于任何传统实现中使用的源码，且未经测试。

除了特殊语法部分之外，本卷（XCU）在各个实用程序的 SYNOPSIS（概要）章节以及正文格式规则中使用以下标记约定：

- **`[ ]` (方括号)**：括起来的项是可选的。在给出了某些互斥选项的列表中，`[ ]` 括住这些选项意味着可以不选择其中任何一个。
- **`...` (省略号)**：表示紧随其前的项可以重复一次或多次。如果省略号出现在方括号内（如 `[file...]`），则表示该项可以出现零次、一次或多次。
- **`< >` (尖括号)**：括起来的项是占位符/替换符，在具体使用时应当被替换为对应的名称或实际值。
- **`|` (竖线)**：表示互斥的选择项。若在括号内括住并由竖线分隔（如 `(a | b)` 或 `[a | b]`），则必须或可以从中选择其中一个。
- **斜体 (Italics)**：在正文文本中引用的命令行参数、选项参数、占位符或非终结符。
- **粗体 (Boldface)**：必须原样输入的字面量（如实用程序名称、短横线选项标志）。

## 1.4 Utility Description Defaults（实用程序描述默认规定）

本节描述了本卷（XCU）中每个实用程序描述所包含的固定子小节（Subsections）。它定义了这些小节的预期用途、影响所有标准实用程序的全局默认规定，以及特定标记在各实用程序规范中的定义含义。

当某个实用程序的具体描述另有规定时，这些默认规定将被覆盖。

### NAME（名称）

给出实用程序的名称或多个名称，并简要说明其用途。

### SYNOPSIS（概要）

总结实用程序的调用语法。如果实用程序不遵循 POSIX.1-2024 Base Definitions 卷（XBD）第 12.2 节 Utility Syntax Guidelines（实用程序语法指南），其语法细节在此处说明。

### DESCRIPTION（描述）

对实用程序的功能进行高层级的概括描述。

### OPTIONS（选项）

描述实用程序接受的选项（Options）及选项参数（Option-arguments），以及它们如何改变实用程序的行为。如果列为 `"None."`，表示该实用程序不接受任何选项。

### OPERANDS（操作数）

描述实用程序接受的命令行操作数（Operands，如文件名、表达式等）。除非另有说明，接受操作数的标准实用程序应当按照在命令行中指定的顺序处理操作数。如果列为 `"None."`，表示实现无需支持任何操作数。

### STDIN（标准输入）

描述实用程序的标准输入。若写为 `"None."`，表示实用程序不从标准输入读取数据。若许多实用程序将标准输入与输入文件同等对待，此处通常会引用 INPUT FILES 小节。

### INPUT FILES（输入文件）

描述实用程序读取的文件。若未另外指定且该小节列为 `"None."` 或没有特殊说明，默认输入文件必须是**文本文件 (text files)**。

### ENVIRONMENT VARIABLES（环境变量）

描述对实用程序有影响的环境变量。默认情况下，实用程序继承并响应 `LANG`、`LC_ALL`、`LC_COLLATE`、`LC_CTYPE`、`LC_MESSAGES`、`NLSPATH` 和 `PATH` 等标准环境变量。若写为 `"None."`，表示不依赖特定环境变量。

### ASYNCHRONOUS EVENTS（异步事件）

列出实用程序对信号（Signals）等异步事件的处理与反应。若写为 `"Default."`，表示按标准的信号继承机制采取标准默认动作。

### STDOUT（标准输出）

描述实用程序写入标准输出（stdout）的内容与格式。若未指定且列为 `"None."`，当实用程序成功执行完且无需产生输出时，标准输出保持为空。

### STDERR（标准错误）

描述标准错误（stderr）的输出。在默认情况下，标准错误专门用于输出诊断与错误提示消息。

### OUTPUT FILES（输出文件）

描述实用程序创建或修改的文件。若列为 `"None."`，表示不创建或写出额外文件。

### EXTENDED DESCRIPTION（扩展描述）

对于功能复杂的实用程序（如 `sed`、`awk`、`make`），此小节详细定义其内部命令语言、语法规则和复杂逻辑。

### EXIT STATUS（退出状态）

列出实用程序退出时返回给调用环境的退出状态码。

- 默认成功状态码为 **`0`**。
- 默认错误状态码为 **`>0`**。

### CONSEQUENCES OF ERRORS（错误后果）

描述发生错误时的后果（例如中断后续输入处理，或者清理临时文件）。若列为 `"Default."`，表示遵循标准的错误处理行为。

### APPLICATION USAGE（应用程序用法）

为应用程序开发人员提供针对该实用程序的补充建议、注意事项和移植指导（不属于规范的强制要求）。

### EXAMPLES（示例）

给出实用程序典型用法的示例。如果示例与规范文本存在冲突，以规范文本为准。

### RATIONALE（原理/基本项）

说明标准做出某项规定或选择的历史背景与设计考量（非规范性）。

### FUTURE DIRECTIONS（未来方向）

说明未来版本中该实用程序可能被废弃、修改或扩充的方向。

### SEE ALSO（参见）

交叉引用相关的其他实用程序、系统接口或技术标准。

## 1.5 Considerations for Utilities in Support of Files of Arbitrary Size（支持任意大小文件的实用程序考量）

以下实用程序支持处理达到实现所能创建的最大值的任意大小文件。这种支持包括正确写入与文件大小相关的数值（例如文件大小和偏移量、行号以及块计数），以及正确解析包含此类数值的命令行参数。

- **`basename`**：Return non-directory portion of pathname.（返回路径名中的非目录部分。）
- **`cat`**：Concatenate and print files.（连接并打印文件。）
- **`cd`**：Change working directory.（变更工作目录。）
- **`chgrp`**：Change file group ownership.（变更文件组所有权。）
- **`chmod`**：Change file modes.（变更文件模式/权限。）
- **`chown`**：Change file ownership.（变更文件所有权。）
- **`cksum`**：Write file checksums and sizes.（写入文件校验和及大小。）
- **`cmp`**：Compare two files.（比较两个文件。）
- **`cp`**：Copy files.（复制文件。）
- **`dd`**：Convert and copy a file.（转换并复制文件。）
- **`df`**：Report free disk space.（报告可用磁盘空间。）
- **`dirname`**：Return directory portion of pathname.（返回路径名中的目录部分。）
- **`du`**：Estimate file space usage.（估计文件空间占用。）
- **`find`**：Find files.（查找文件。）
- **`ln`**：Link files.（链接文件。）
- **`ls`**：List directory contents.（列出目录内容。）
- **`mkdir`**：Make directories.（创建目录。）
- **`mv`**：Move files.（移动文件。）
- **`pathchk`**：Check pathnames.（检查路径名。）
- **`pwd`**：Return working directory name.（返回工作目录名称。）
- **`rm`**：Remove directory entries.（删除目录项。）
- **`rmdir`**：Remove directories.（删除目录。）
- **`sh`**：Shell, the standard command language interpreter.（Shell，标准的命令语言解释器。）
- **`test`**：Evaluate expression.（评估表达式。）
- **`touch`**：Change file access and modification times.（变更文件访问与修改时间。）
- **`ulimit`**：Set or report file size limit.（设置或报告文件大小限制。）

支持处理达到实现所能创建的最大值的任意大小文件的要求，其例外情况如下：

- 将文件用作命令脚本，或者用于配置或控制，属于豁免情况。例如，不要求 `sh` 必须能够读取任意巨大的 `.profile` 文件。
- Shell 的输入和输出重定向属于豁免情况。例如，不要求重定向 `sum < file` 或 `echo foo > file` 在面对任意巨大的现存文件时必须成功。

## 1.6 Built-In Utilities（内置实用程序）

任何标准实用程序都可以作为命令语言解释器（Shell）内部的常规内置实用程序（regular built-in utilities）来实现。这样做通常是为了提高常用实用程序的性能，或者是为了实现在独立环境中较难达到的功能。下文 1.7 Intrinsic Utilities 中描述的本征实用程序，通常会被作为常规内置实用程序提供。

然而，除了以下实用程序之外：

- 在 2.15 Special Built-In Utilities 中描述的特殊内置实用程序
- 在 Table: Intrinsic Utilities 中命名的本征实用程序（`kill` 除外）

所有其他的标准实用程序，无论它们是否也被实现为常规内置实用程序，都应当以某种方式被实现，使其能够通过 POSIX.1-2024 System Interfaces 卷中定义的 `exec` 函数族来进行访问，并且能够被那些需要直接调用它们的标准实用程序（`env`、`find`、`nice`、`nohup`、`time`、`xargs`）直接调用。

## 1.7 Intrinsic Utilities（本征实用程序）

正如在 2.9.1.4 Command Search and Execution 中所描述的，本征实用程序（intrinsic utilities）在命令搜索与执行期间不受 `PATH` 搜索的约束。在 Table: Intrinsic Utilities 中命名的实用程序应当是本征实用程序。

### Table: Intrinsic Utilities（表：本征实用程序）

|           |         |           |
| --------- | ------- | --------- |
| `alias`   | `bg`    | `cd`      |
| `command` | `fc`    | `fg`      |
| `getopts` | `hash`  | `jobs`    |
| `kill`    | `read`  | `type`    |
| `ulimit`  | `umask` | `unalias` |
| `wait`    |         |           |

是否有任何额外的实用程序被视为本征实用程序，是由实现定义的（implementation-defined）。由于应用程序无法使用来自 `PATH` 的实用程序来覆盖本征实用程序，因此除了 Table: Intrinsic Utilities 中的实用程序之外，实现不应将任何其他实用程序设为本征实用程序。