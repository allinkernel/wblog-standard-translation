# 2. Shell 命令语言 (Shell Command Language)

## 2.1 Shell 简介 (Shell Introduction)

Shell 是一个命令语言解释器（Command Language Interpreter），它执行来自终端、终端窗口、异步文件或来自 Shell 脚本文件的命令。

本章描述了 `sh` 实用程序（Utility）以及 POSIX.1-2024《系统接口》卷中定义的 `system()` 和 `popen()` C 语言 API 函数所使用的 Shell 命令语言的正式语法与语义。

### 2.1.1 Shell 的基本操作流程 (Shell Operation)

当 Shell 运行时，它会重复按顺序执行以下操作步骤：

1. **读取输入 (Read Input)**：
   - 从文件、`-c` 字符串选项输入、交互式终端，或通过 `system()` / `popen()` 函数读取命令输入。
   - **`#!` (Hash-Bang) 处理机制**：如果 Shell 脚本文件的第一行的前两个字节是 `#!`，其后续解释器的行为属于未指定行为（Unspecified）。系统可能将其作为可执行文件的路径并传递参数，但这超出了 POSIX 标准规范的约束范畴。
2. **标记识别与词法拆分 (Token Recognition)**：
   - 输入流被逐字符扫描，并根据 2.2 节（引用）和 2.3 节（Token 识别）的规则拆分为词法标记（Tokens）。Token 分为两类：**单词 (Words)** 与 **运算符 (Operators)**。
3. **语法解析 (Parsing)**：
   - 根据 2.10 节（Shell 语法）的 BNF 规则，将 Token 序列解析为简单命令（Simple Commands）与复合命令（Compound Commands），构建语法树。
4. **处理扩展 (Expansions)**：
   - 处理 `$''` 内的反斜杠转义序列。
   - 对各种语法成分按严格规定的顺序执行 2.6 节定义的 7 种**单词扩展 (Word Expansions)**。
5. **处理重定向 (Redirection)**：
   - 解析并执行 2.7 节定义的重定向操作。
   - 成功建立文件描述符映射后，将重定向运算符及其相关操作数从命令参数列表中移除。
6. **命令执行 (Command Execution)**：
   - 按照 2.9.1.4 节定义的搜索顺序，执行函数（Functions）、内置命令（Built-in Utilities）、内部脚本或外部可执行程序。
   - 向被执行的实体传递扩展后的位置参数（Positional Parameters）与环境变量。
7. **收集退出状态 (Exit Status Collection)**：
   - 可选地等待同步命令执行完成，收集其**退出状态码 (Exit Status)**；对于后台/异步命令，立刻返回并继续读取下一个输入。

## 2.2 引用 / 转义 (Quoting)

引用（Quoting）用于屏蔽字符或单词在 Shell 中原有的特殊语法含义（Special Meaning）。引用的核心作用包括：

1. 保留字符的字面含义（Literal Value）。
2. 防止单词被识别为保留字（Reserved Words）。
3. 阻止在 Here-Document（立即文档）处理过程中发生参数扩展、命令替换与算术扩展。

Shell 包含以下 4 种引用/转义机制：

### 2.2.1 转义字符：反斜杠 (Escape Character (Backslash))

未被引用的反斜杠 `\` 能够保留紧跟在其后的**单个字符**的字面值，但**换行符 (Newline)** 除外。

- **续行符规则 (Line Continuation)**：若反斜杠后紧跟一个换行符（`\<newline>`），该组合被视为“续行符”。Shell 在进行 Token 拆分之前，会将反斜杠和换行符**同时从输入流中彻底移除**。这允许一条超长命令跨越编写在多行中，而不会被分割为多条命令或注入换行 Token。
- **引用内行为**：如果反斜杠本身处于单引号内，它失去转义作用（作为普通字符）；如果处于双引号内，其行为遵循 2.2.3 节的特定限制。

### 2.2.2 单引号 (Single-Quotes)

将字符序列包围在一对单引号 `' '` 中，可以完全保留该序列内**所有字符**的字面值。

- **不可嵌套规则**：单引号内**绝对不能出现单引号本身**，无论是否使用了反斜杠转义（因为在单引号内部，反斜杠失去了任何转义功能，`\'` 会被直接解析为反斜杠和闭合单引号，导致语法报错或提前闭合）。

### 2.2.3 双引号 (Double-Quotes)

将字符序列包围在一对双引号 `" "` 中，可以保留该序列内绝大多数字符的字面值，**但以下 4 类特殊字符保持其特殊语法功能**：

1. **`$` (美元符号)**：
   - 保留其引入参数扩展（Parameter Expansion，如 `$var` 或 `${var}`）、命令替换（Command Substitution，如 `$(cmd)`）和算术扩展（Arithmetic Expansion，如 `$((expr))`）的语法功能。
   - **例外**：在双引号内部，`$` 不保留引入 `$''` 引用的语法功能（即 `"$''"` 中的 `$'` 不会被解析为美元单引号转义）。
2. **反引号**：
   - 保留其引入传统格式命令替换的语法功能。
3. **`\` (反斜杠)**：
   - 仅当反斜杠紧跟以下 5 个字符之一时，才保留其转义含义：
     - `$`
     - 反引号
     - `\` (反斜杠本身)
     - `"` (双引号)
     - `<newline>` (换行符，作为续行符移除)
   - 如果反斜杠紧跟任何其他字符，反斜杠将**失去转义含义**，作为普通字面字符传递给后续处理。
4. **`@` (特殊参数)**：
   - 当特殊参数 `@` 出现在双引号内（即 `"$@"`）时，它在 2.5.2 节定义的按独立单词扩展（Word Splitting Exemption）的特殊语义在双引号内**予以保留**。

### 2.2.4 美元单引号 (Dollar-Single-Quotes)

以 `$''`（一个美元符号紧跟一对单引号）开头的字符序列，保留其中字符的字面值，直到遇到未被转义的结尾单引号 `'`。但在该结构内部，**支持 ANSI C 风格的反斜杠转义序列**。

当按顺序扫描到以下转义序列时，它们会被直接替换为对应的单字符或字节：

- **标准转义字符**：
  - `\"`：双引号 (Double-quote)
  - `\'`：单引号 (Single-quote)
  - `\\`：反斜杠 (Backslash)
  - `\a`：响铃符 (Alert / Bell，ASCII 0x07)
  - `\b`：退格符 (Backspace，ASCII 0x08)
  - `\e` 或 `\E`：转义符 (Escape，ASCII 0x1B)
  - `\f`：换页符 (Form-feed，ASCII 0x0C)
  - `\n`：换行符 (Newline，ASCII 0x0A)
  - `\r`：回车符 (Carriage-return，ASCII 0x0D)
  - `\t`：水平制表符 (Horizontal-tab，ASCII 0x09)
  - `\v`：垂直制表符 (Vertical-tab，ASCII 0x0B)
- **控制字符 (Control Characters)**：
  - `\cX` 或 `\cx`：表示控制字符 Control-$X$。求值方式为：取 $X$ 的 ASCII 码与 `0x3F` 进行位与计算（或按约定转换为对应控制码，如 `\cA` 或 `\ca` 转换为 ASCII 0x01）。
- **数值转义字节 (Numeric Escapes)**：
  - `\xXX`：十六进制转义。由 1 个或 2 个十六进制数码（`0-9`, `a-f`, `A-F`）组成，代表对应的单字节值。
  - `\ddd` 或 `\dd` 或 `\d`：八进制转义。由 1 到 3 个八进制数码（`0-7`）组成，代表对应的单字节值。
- **未定义的转义**：
  - 若反斜杠后跟有未在上述列表中列出的字符，其行为是**保留反斜杠与后续字符**，或者剥离反斜杠（具体由系统实现决定，因此编写移植脚本时不可依赖）。

## 2.3 词法标记识别 (Token Recognition)

Shell 应当从输入流中逐字符读取输入，并将其处理为一系列 Token。输入行的长度限制必须是无限的（仅受系统内存限制）。

### 2.3.1 Token 识别规则 (Token Recognition Rules)

Shell 在处理输入流时，遵循以下 10 条严格优先级的词法识别算法：

1. **处理文件结束符 (EOF)**：如果遇到输入流结尾（EOF），当前的 Token 判定终止。
2. **结合新字符**：如果上一个字符是运算符（Operator）的一部分，且当前字符可以与上一个字符组合成一个新的运算符，则将当前字符并入该运算符中。
3. **运算符界定**：如果上一个字符是运算符的一部分，但当前字符**不能**与上一个字符组合成运算符，则上一个运算符的 Token 认定结束。
4. **处理引用状态**：如果当前字符处于被引用状态（在单引号、双引号、美元单引号内，或前有未引用的反斜杠），则将该字符追加到当前单词（Word）中。
5. **处理参数扩展/命令替换/算术扩展的起始**：如果当前字符未被引用，且是 `$` 或反引号：
   - Shell 应当扫描并找到匹配的闭合括号/反引号，在扫描匹配边界的过程中，内部的所有字符保持其原有的词法结构（例如嵌套的引用和重定向）。整个 `${...}`、`$(...)` 或 `$((...))` 结构将被整体作为当前 Word 的一部分。
6. **处理运算符起始**：如果当前字符未被引用，且能够开始一个新的运算符（如 `;`, `&`, `|`, `<`, `>`, `(`, `)`），则当前正在构建的 Word Token 结束，并开启一个新的运算符 Token。
7. **处理空白字符 (Blank Characters)**：如果当前字符未被引用，且是一个空白字符（空格或 Tab）：
   - 如果当前存在正在构建的 Word，则该 Word Token 宣告结束。
   - 连续的未引用空白字符将被丢弃，不产生 Token。
8. **处理普通字符**：如果当前字符是普通字符（非运算符、非空白、未被引用），则将其追加到当前 Word 的末尾。
9. **处理注释 (Comments)**：如果当前字符是未被引用的 `#`，且该 `#` 处于一条命令的开头，或者位于空白字符/运算符之后，则该 `#` 以及本行后续的所有字符将被作为注释**完全忽略**，直到遇到换行符为止。
10. **处理换行符 (Newline)**：未被引用的换行符被识别为特殊的控制运算符（Control Operator），标志着命令行的结束。

### 2.3.2 别名替换 (Alias Substitution)

在识别到一个 Token（单词）之后、且进行语法分析之前，Shell 会检查是否需要执行别名替换：

- **检查条件**：只有当这个 Word 处于“能够作为命令名称”的语法位置时，Shell 才会进行检查。这包括：
  1. 简单命令（Simple Command）的第一个单词。
  2. 紧跟在某些特定保留字之后的单词（如 `then`, `else`, `do`, `until` 等）。
  3. 紧跟在另一个已经被替换且**以空白字符结尾**的别名之后的单词。
- **替换机制**：
  - 若该 Word 匹配当前 Shell 别名数据库中的某个定义，则该 Word 被替换文本**直接替换**。
  - 替换后的文本会重置回词法分析器，重新进行 Token 识别。
  - **防止无限递归**：在对别名展开后的文本重新识别 Token 的过程中，如果再次遇到与正在展开的别名同名的 Word，则该 Word **不会被二次展开**，从而避免死循环。

## 2.4 保留字 (Reserved Words)

保留字（Reserved Words）是在 Shell 语言结构中具有特殊语法控制含义的单词。POSIX 规范定义的标准保留字如下：

Plaintext

```
!         if        then      else      elif
fi        case      esac      for       while
until     do        done      {         }
in
```

### 2.4.1 保留字的识别规则

一个 Word 只有在满足以下**所有条件**时，才会被识别为保留字：

1. 该 Word 中的所有字符都**未被任何方式引用**（例如 `if` 是保留字，但 `'if'` 或 `"if"` 或 `i\f` 只能被识别为普通单词）。
2. 该 Word 出现在命令的特定语法起始位置：
   - 命令行的第一个单词。
   - 紧跟在控制运算符 `;`, `&`, `|`, `&&`, `||`, `\n` 之后的第一个单词。
   - 紧跟在保留字 `then`, `else`, `elif`, `do`, `until`, `}` 之后的第一个单词。
   - 作为 `case` 结构的模式匹配词，或 `for` 循环中的 `in` 关键字。

## 2.5 参数与变量 (Parameters and Variables)

参数（Parameter）是 Shell 用于存储值的实体。可以通过名称、数字或特殊符号来引用参数。

- **变量 (Variable)**：由**名称 (Name)** 标识的参数。名称必须由字母、数字或下划线组成，且**不能以数字开头**。
- **位置参数 (Positional Parameter)**：由一个或多个数字标识的参数。
- **特殊参数 (Special Parameter)**：由单个特殊符号标识的参数。

### 2.5.1 位置参数 (Positional Parameters)

位置参数是由大于 0 的十进制数字标识的参数（`$1`, `$2`, `$3`, ... `${10}`, `${11}` ...）。

- **赋值与生命周期**：
  - 在 Shell 启动时，位置参数由传递给 Shell 脚本的命令行参数依次初始化（其中 `$1` 代表第一个实参）。
  - 在函数（Function）被调用时，位置参数被临时替换为传递给该函数的实参；函数执行完毕退出后，恢复为调用前的原位置参数。
  - 可以使用内置命令 `set` 重新对所有位置参数进行批量赋值。
  - 可以使用内置命令 `shift [n]` 将位置参数向左平移 $n$ 个位置（即原来的 `$((1+n))` 变为新的 `$1`），原有的前 $n$ 个参数被永久丢弃。
- **语法注意**：当位置参数的数字达到两位数或以上时，必须使用花括号（例如 `${10}`），否则 `$10` 会被解析为位置参数 `$1` 后紧跟字面字符 `0`。

### 2.5.2 特殊参数 (Special Parameters)

特殊参数的值由 Shell 动态维护，用户**不能**对其直接进行赋值（即不能编写 `* = value` 或 `? = 0`）。

1. **`\*` (Asterisk)**：
   - 扩展为从 $1$ 开始的所有位置参数（`$1 $2 $3 ...`）。
   - **双引号下的行为 (`"$*"`)**：当扩展处于双引号内部时，所有位置参数将被连接合并为一个**单一的单词 (Single Word)**。参数之间由 `IFS` 变量的**第一个字符**隔开。如果 `IFS` 未设置，默认使用空格分隔；如果 `IFS` 为 Null（即 `IFS=""`），则参数之间没有任何分隔符直接拼接到一起。
2. **`@` (At-sign)**：
   - 扩展为从 `$1` 开始的所有位置参数。
   - **双引号下的行为 (`"$@"`)**：当扩展处于双引号内部时，每个位置参数将被扩展为**独立的单词 (Separate Words)**。即 `"$@"` 严格等价于 `"$1" "$2" "$3"` ...。
   - **无参数时的行为**：当位置参数个数为 0 时，`"$@"` 不会产生任何单词（扩展结果为包含 0 个 Field 的空列表，而非包含一个空字符串的单词）。
3. **`#` (Pound-sign)**：
   - 扩展为当前位置参数的**总个数**（十进制无符号整数）。
4. **`?` (Question-mark)**：
   - 扩展为**最近一次在前台执行的命令的退出状态码 (Exit Status)**（十进制整数）。
5. **`-` (Hyphen)**：
   - 扩展为当前 Shell 在启动时传入或通过 `set` 命令激活的**单字符选项标志位 (Option Flags)** 拼接成的字符串。
6. **`$` (Dollar-sign)**：
   - 扩展为当前 Shell 进程的**进程 ID (PID)**。对于子 Shell（Subshell），该值保持为引发创建该环境的主 Shell 的 PID。
7. **`!` (Exclamation-mark)**：
   - 扩展为最近一个被启动的**后台/异步命令 (Asynchronous Command)** 的进程 ID (PID)。
8. **`0` (Zero)**：
   - 扩展为 Shell 或 Shell 脚本本身的名称。如果 Shell 是通过传入脚本文件调用的，则 `$0` 为该脚本的文件路径名；如果是通过 `-c` 选项调用的，则 `$0` 为第一个非选项参数或 Shell 名称。

### 2.5.3 Shell 变量 (Shell Variables)

当一个参数的名称由合法的标示符（字母/下划线开头）命名时，它就是一个 Shell 变量。

#### 变量赋值语法 (Variable Assignment)

变量赋值的语法格式为：

```
name=value
```

- `=` 左侧的 `name` 不能加 `$` 符号，且不能有引用。
- `=` 两侧**绝对不能出现未引用的空格**。
- 如果 `value` 为空，则该变量被赋值为 Null 字符串（例如 `var=`）。

#### 环境变量与导出 (Environment Variables)

- 默认情况下，Shell 内部创建的变量属于**局部 Shell 变量**，不会被子进程继承。
- 使用 `export name` 实用程序可以将变量提升为**环境变量 (Environment Variable)**，使其能够被该 Shell 派生的所有子进程（如外部可执行程序）继承。

#### POSIX 标准预定义的关键 Shell 变量

POSIX 定义了以下具有特殊控制功能的环境变量与内置变量：

| **变量名**                               | **全称与功能描述**                                           |
| ---------------------------------------- | ------------------------------------------------------------ |
| **`IFS`**                                | **Internal Field Separators（内部字段分隔符）**。用于在扩展后进行字段分割（Field Splitting），以及在使用 `read` 命令或 `"$*"` 扩展时作为分隔符。默认值为 `<space><tab><newline>`。 |
| **`PATH`**                               | **Executable Search Path（命令搜索路径）**。由冒号 `:` 分隔的目录路径列表。Shell 按照此顺序查找外部可执行命令。 |
| **`HOME`**                               | **User Home Directory（用户家目录）**。由 `cd` 命令无参数时默认进入，同时用于波浪号扩展（`~`）。 |
| **`PPID`**                               | **Parent Process ID（父进程 ID）**。当前 Shell 进程的父进程的 PID（只读）。 |
| **`PWD`**                                | **Present Working Directory（当前工作目录）**。存储当前绝对路径。 |
| **`OLDPWD`**                             | **Previous Working Directory（上一工作目录）**。存储上一次通过 `cd` 切换前的绝对路径（供 `cd -` 使用）。 |
| **`PS1`**                                | **Primary Prompt String（一级提示符）**。交互式 Shell 中的主命令行提示符（默认为 `"$ "`，非特权用户；或 `"#" `，特权用户）。 |
| **`PS2`**                                | **Secondary Prompt String（二级提示符）**。输入多行未完成命令时的续行提示符（默认为 `"> "`）。 |
| **`PS4`**                                | **Execution Trace Prompt（执行追踪提示符）**。开启 `set -x` 调试模式时，在输出每条执行命令前打印的前缀（默认为 `"+ "`）。 |
| **`LINENO`**                             | **Line Number（当前行号）**。扩展为当前正在执行的脚本或函数内的十进制行号。 |
| **`LC_ALL` / `LC_COLLATE` / `LC_CTYPE`** | **Locale Control（区域与字符集控制）**。控制字符分类、模式匹配大小写规则、正则表达式行为及排序顺序。 |

## 2.6 单词扩展 (Word Expansions)

在简单命令（Simple Commands）中，单词扩展（Word Expansions）发生在词法识别与语法解析完成之后、重定向处理与命令执行之前。

扩展共包含以下 7 种机制。当它们应用于同一个单词时，**严格按照以下顺序执行**：

1. **波浪号扩展 (Tilde Expansion)**
2. **参数扩展 (Parameter Expansion)**
3. **命令替换 (Command Substitution)**
4. **算术扩展 (Arithmetic Expansion)**
5. **字段分割 (Field Splitting)**
6. **路径名扩展 (Pathname Expansion)**
7. **引用消除 (Quote Removal)**

> **核心规则**：
>
> - 步骤 2、3、4（参数扩展、命令替换、算术扩展）具有**同等优先级**，它们在输入单词中从左到右扫描并按出现顺序依次进行处理。
> - 只有步骤 2、3、4 产生的未被引用的扩展结果，才会在后续进行步骤 5（字段分割）和步骤 6（路径名扩展）。
> - 如果一个单词包含在双引号内，则它绝对**不会**触发步骤 1（波浪号扩展）、步骤 5（字段分割）和步骤 6（路径名扩展）。

### 2.6.1 波浪号扩展 (Tilde Expansion)

如果一个单词以未引用的波浪号 `~` 开头，Shell 将扫描该波浪号，直到遇到未引用的斜杠 `/` 或单词结尾。波浪号与斜杠/结尾之间的字符被称为 **波浪号前缀 (Tilde-Prefix)**。

#### 扩展解析规则：

1. **未引用的单波浪号 (`~` 或 `~/...`)**：
   - 将波浪号前缀替换为环境变量 `HOME` 的值。若 `HOME` 未设置，其扩展结果是未指定的（Unspecified）。
2. **指定用户名 (`~user` 或 `~user/...`)**：
   - 波浪号后跟一个由合法名称字符构成的用户名。Shell 会在系统的用户数据库（如 `/etc/passwd`）中查找该 `user`，并将波浪号前缀替换为该用户的家目录绝对路径。如果找不到该用户，则保持波浪号前缀原样不变。
3. **变量赋值中的波浪号扩展**：
   - 在变量赋值（如 `var=~`）中，赋值符号 `=` 后紧跟的未引用波浪号会被识别并触发波浪号扩展。
   - 在变量赋值中，如果值里包含未引用的冒号 `:`（例如路径拼接 `PATH=~/bin:~user/bin`），每个冒号之后的波浪号也将各自触发波浪号扩展。

### 2.6.2 参数扩展 (Parameter Expansion)

参数扩展的形式为 `$parameter` 或 `${parameter}`。其基本含义是将参数替换为其存储的值。

#### 1. 基础扩展

- **`$parameter` 或 `${parameter}`**：
  - 扩展为 `parameter` 的值。
  - 如果 `parameter` 为位置参数或特殊参数，按 2.5 节规则求值。
  - 如果 `parameter` 未设置且未启用 `set -u` (nounset)，扩展结果为空（Null）。如果启用了 `set -u`，Shell 将向 stderr 输出错误信息并以非零状态码终止执行。

#### 2. 条件语法扩展 (Conditional Expansions)

在以下所有格式中，`word` 都会经历波浪号扩展、参数扩展、命令替换与算术扩展。只有在条件满足需要使用 `word` 时，`word` 才会真正被求值（即惰性求值/Lazy Evaluation）。

- **`${parameter:-word}` (使用默认值)**：
  - **规则**：若 `parameter` 未设置（Unset）或为 Null（空字符串），则整个表达式扩展为 `word` 的扩展结果；否则扩展为 `parameter` 的值。
  - **同类格式 `${parameter-word}`**：仅当 `parameter` 未设置时才扩展为 `word`（如果 `parameter` 为 Null，则依然扩展为 Null）。
- **`${parameter:=word}` (赋值默认值)**：
  - **规则**：若 `parameter` 未设置或为 Null，则将 `word` 的扩展结果**赋值给 `parameter`**，然后整个表达式扩展为 `parameter` 的新值。
  - **限制**：只有变量可以作为 `parameter`；位置参数和特殊参数不能使用此格式。
  - **同类格式 `${parameter=word}`**：仅当 `parameter` 未设置时才执行赋值与扩展。
- **`${parameter:?word}` (指示错误/检测未设置)**：
  - **规则**：若 `parameter` 未设置或为 Null，将 `word` 的扩展结果（若省略 `word` 则使用默认错误信息）输出到标准错误（stderr），且非交互式 Shell 将**立刻终止执行并返回非零退出码**。若 `parameter` 已设置且非 Null，扩展为 `parameter` 的值。
  - **同类格式 `${parameter?word}`**：仅当 `parameter` 未设置时才触发错误并终止。
- **`${parameter:+word}` (使用替代值)**：
  - **规则**：若 `parameter` 未设置或为 Null，整个表达式扩展为空（Null）；若 `parameter` 已设置且非 Null，整个表达式扩展为 `word` 的扩展结果（`parameter` 原有的值被忽略）。
  - **同类格式 `${parameter+word}`**：只要 `parameter` 已设置（即使为 Null），就扩展为 `word`。

#### 3. 字符串长度与模式匹配扩展

- **`${#parameter}` (获取字符串长度)**：
  - 扩展为 `parameter` 的值的字符长度（十进制无符号整数）。
  - 若 `parameter` 为 `*` 或 `@`，扩展结果为位置参数的总个数（等价于 `$#`）。
- **`${parameter#pattern}` (移除最短匹配前缀)**：
  - 将 `parameter` 的值从**开头**开始与 `pattern` 进行模式匹配。剥离匹配成功的最短（Shortest）前缀，扩展为剩余的后半部分字符串。
- **`${parameter##pattern}` (移除最长匹配前缀)**：
  - 将 `parameter` 的值从**开头**开始与 `pattern` 进行模式匹配。剥离匹配成功的最长（Longest）前缀，扩展为剩余的后半部分字符串。
- **`${parameter%pattern}` (移除最短匹配后缀)**：
  - 将 `parameter` 的值从**结尾**开始与 `pattern` 进行模式匹配。剥离匹配成功的最短（Shortest）后缀，扩展为剩余的前半部分字符串。
- **`${parameter%%pattern}` (移除最长匹配后缀)**：
  - 将 `parameter` 的值从**结尾**开始与 `pattern` 进行模式匹配。剥离匹配成功的最长（Longest）后缀，扩展为剩余的前半部分字符串。

#### 实例 (Examples)


```bash
# 示例 1: 变量默认值设置
# 若 PORT 未定义，使用默认值 8080
HTTP_PORT=${PORT:-8080}

# 示例 2: 剥离路径前缀与文件后缀
FILE="/var/log/syslog.tar.gz"

echo "${FILE#*/}"     # 输出: var/log/syslog.tar.gz (剥离最短前缀)
echo "${FILE##*/}"    # 输出: syslog.tar.gz (剥离最长前缀，相当于 basename)
echo "${FILE%.*}"     # 输出: /var/log/syslog.tar (剥离最短后缀)
echo "${FILE%%.*}"    # 输出: /var/log/syslog (剥离最长后缀)
```

### 2.6.3 命令替换 (Command Substitution)

命令替换允许一条命令的标准输出（stdout）替换命令本身的语法位置。

命令替换支持以下两种形式：

1. **POSIX 推荐形式**：`$(command)`
2. **传统反引号形式**：``command``

#### 执行与处理规则：

- Shell 会派生一个子 Shell（Subshell）环境来执行其中的 `command`。
- `command` 运行时的标准输出（stdout）会被 Shell 捕获。
- **末尾换行符剥离**：Shell 会将捕获到的输出结果末尾所包含的**所有换行符 (`\n`) 彻底剥离**。输出内容中间的换行符或非换行空白字符被完整保留。
- **嵌套解析规则**：
  - `$(command)` 内部支持无缝嵌套，例如 `$(cmd1 $(cmd2))`。
  - 反引号形式在嵌套时，内层的反引号和反斜杠必须使用反斜杠进行转义（如 ``cmd1 \`cmd2\` ``）。

### 2.6.4 算术扩展 (Arithmetic Expansion)

算术扩展用于对整数算术表达式求值并将其结果替换为十进制数字字符串。

- **语法格式**：`$((expression))`

#### 求值规则：

- 表达式 `expression` 作为双引号内的文本进行处理，内部支持变量展开（如 `$var` 或直接使用 `var` 变量名）。
- 所有运算均按照 **C 语言**的整数算术规则进行（通常为 ISO C 标准的 `signed long` 或 `intmax_t` 类型的宽整数运算）。
- 算术扩展支持的运算符及其优先级与 C 语言一致：
  - **括号**：`()`
  - **单目运算**：`+`, `-`, `~`, `!`
  - **乘除模**：`*`, `/`, `%`
  - **加减**：`+`, `-`
  - **移位**：`<<`, `>>`
  - **关系比较**：`<`, `<=`, `>`, `>=`
  - **相等比较**：`==`, `!=`
  - **按位与**：`&`
  - **按位异或**：`^`
  - **按位或**：`|`
  - **逻辑与**：`&&`
  - **逻辑或**：`||`
  - **三目条件**：`expr1 ? expr2 : expr3`
  - **赋值运算**：`=`, `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `^=`, `|=`
- **异常处理**：若发生除以零（Division by zero）或算术溢出，其行为是未定义的，Shell 会输出错误并返回非零状态。

#### 实例 (Examples)


```bash
# 示例 1: 简单算术计算与变量自增
count=5
total=$((count * 2 + 10))    # total 结果为 20

# 示例 2: 在循环中更新变量
index=0
index=$((index + 1))
```

### 2.6.5 字段分割 (Field Splitting)

在参数扩展、命令替换与算术扩展完成之后，如果它们**未处于双引号内部**，Shell 会检查它们产生的扩展结果，并根据环境变量 `IFS`（Internal Field Separator）的设定，将其分割为独立的字段（Fields / Words）。

#### 分割算法规则：

1. **`IFS` 包含默认空白字符（Space, Tab, Newline）**：
   - `IFS` 中的空白字符被称为 **IFS 空白符 (IFS Whitespace)**。
   - 扩展文本开头和结尾的所有 IFS 空白符都会被忽略/切除。
   - 文本内部连续的多个 IFS 空白符会被当作**单个分隔符**，将文本切分为字段。
   - 若文本内部包含非空白的 `IFS` 字符（如 `IFS=":"` 中的 `:`），则每个非空白字符都将被严格作为**字段终止符/分隔符**（两个连续的 `:` 会在中间产生一个空字段）。
2. **`IFS` 为空 (Null，即 `IFS=""`)**：
   - 完全禁用字段分割，扩展结果被原封不动地作为一个整体字段保留。
3. **`IFS` 未设置 (Unset)**：
   - 行为完全等同于 `IFS` 设置为 `<space><tab><newline>`。

### 2.6.6 路径名扩展 (Pathname Expansion)

除非显式设置了选项 `set -f` (或 `set -o noglob`) 禁用了路径名扩展，否则在字段分割之后，如果某个字段包含未引用的模式字符（`*`, `?`, `[...]`），该字段将被作为搜索模式（Pattern）。

- Shell 会在文件系统中匹配符合该模式的所有文件与目录。
- 匹配到的所有路径名将按照当前 Locale 的字典序（Collating Sequence）进行排序，并替换原有的模式字段。
- **匹配失败行为**：如果没有找到任何匹配的文件路径，该字段将**保持原样不变**传给后续处理。

*(关于匹配符号的具体规则，详见 2.14 节)*

### 2.6.7 引用消除 (Quote Removal)

在上述所有扩展（波浪号扩展、参数扩展、命令替换、算术扩展、字段分割、路径名扩展）彻底完成之后，Shell 将扫描最终的单词 Token。

- 所有在原始输入中用于引用的字符：
  - 未被引用的单引号 `'`
  - 未被引用的双引号 `"`
  - 未被引用的转义反斜杠 `\`
- 都将被 Shell **完全剥离/移除**，仅保留其保护的字面字符，形成最终传递给命令执行的字符串参数。

## 2.7 重定向 (Redirection)

重定向用于在命令执行前改变其标准输入（stdin, FD 0）、标准输出（stdout, FD 1）和标准错误（stderr, FD 2），或者关联其他的任意文件描述符（File Descriptors）。

重定向的语法格式为：`[n]operator word`

- `n` 是一个可选的十进制无符号整数，代表要操作的文件描述符。如果省略 `n`，根据运算符的不同，默认使用 0（输入）或 1（输出）。
- `word` 是重定向的目标，它会经历波浪号扩展、参数扩展、命令替换、算术扩展、路径名扩展和引用消除，但**绝对不会触发字段分割**（即扩展结果必须是单个唯一的路径名或 FD 数字）。

### 2.7.1 重定向输入 (Redirecting Input)

以只读方式打开指定文件，并将其绑定到文件描述符 `n`（默认为 0）。

- **语法**：`[n]< word`
- **行为**：若文件不存在，则打开失败并产生重定向错误。

### 2.7.2 重定向输出 (Redirecting Output)

打开指定文件进行写入，并将其绑定到文件描述符 `n`（默认为 1）。

- **语法**：`[n]> word`
- **行为**：
  - 若文件不存在，则创建该文件。
  - 若文件已存在，原文件内容将被**清空截断 (Truncated)** 到 0 字节。
  - **`noclobber` 保护机制**：如果 Shell 开启了 `set -C` (或 `set -o noclobber`) 选项，且重定向的目标是一个普通文件，则当文件已存在时重定向会**报错拒绝覆盖**。
  - **强制覆盖语法**：使用 `[n]>| word` 可以在开启 `noclobber` 的情况下强制截断并覆盖已有文件。

### 2.7.3 追加重定向输出 (Appending Redirected Output)

以追加模式打开文件并绑定到文件描述符 `n`（默认为 1）。

- **语法**：`[n]>> word`
- **行为**：
  - 若文件不存在，则创建该文件。
  - 若文件已存在，文件偏移量被定位到文件末尾（O_APPEND），所有新的写入数据将直接追加到文件原有内容的后面。

### 2.7.4 Here-Document (立即文档)

Here-Document 是一种特殊的输入重定向机制，它将脚本中紧跟在命令之后的多行文本块作为标准输入（或 FD `n`）传递给命令。

- **语法**：


  ```bash
  [n]<< delimiter
      body-lines
  delimiter
  ```

- **处理规则**：

  1. **定界符未被引用 (`<< delimiter`)**：
     - `body-lines` 中的文本会逐行经历参数扩展、命令替换与算术扩展。
     - 反斜杠 `\` 仅在紧跟 `$`, 反引号, `\` 或换行符时才起转义作用。
  2. **定界符包含引用 (`<< 'delimiter'` 或 `<< "delimiter"`)**：
     - `body-lines` 中的文本将被作为**绝对字面量**处理，完全禁止任何形式的参数扩展、命令替换或反斜杠转义。
  3. **制表符剥离语法 (`[n]<<- delimiter`)**：
     - 使用 `<<-` 时，每行输入文本 `body-lines` 以及结尾定界符 `delimiter` **行首的所有制表符 (`<tab>`) 都将被彻底剥离**。这允许在缩进的 Shell 脚本中优雅地编写 Here-Document。

#### 实例 (Examples)


```bash
# 示例 1: 带有变量展开与 Tab 剥离的 Here-Document
LOG_FILE="app.log"
cat <<- EOF > "$LOG_FILE"
	System Report Generated On: $(date)
	Target Host: $HOSTNAME
EOF

# 示例 2: 禁用变量展开的静态块
cat << 'END_TEXT'
The variable $USER will NOT be expanded here.
END_TEXT
```

### 2.7.5 复制输入文件描述符 (Duplicating an Input File Descriptor)

将文件描述符 `n` 复制为指定的输入文件描述符 `word`。

- **语法**：`[n]<&word`
- **规则**：
  - 若 `word` 展开为一个十进制数字，文件描述符 `n` 将被重定向为该数字所指代的文件描述符的副本（使用 `dup2()` 系统调用）。
  - 若 `word` 展开为 `-`，则文件描述符 `n` 将被**彻底关闭 (Closed)**。

### 2.7.6 复制输出文件描述符 (Duplicating an Output File Descriptor)

将文件描述符 `n` 复制为指定的输出文件描述符 `word`。

- **语法**：`[n]>&word`
- **规则**：
  - 若 `word` 展开为一个十进制数字，文件描述符 `n` 将被重定向为该数字所指代的输出文件描述符的副本。
  - 若 `word` 展开为 `-`，则文件描述符 `n` 将被关闭。
  - **典型用法**：` command > file 2>&1`（将标准输出重定向到 `file`，然后将标准错误 FD 2 复制为标准输出 FD 1 的副本，使得 stdout 与 stderr 同时落入 `file`）。

### 2.7.7 读写方式打开文件描述符 (Open File Descriptors for Reading and Writing)

以读写（Read-Write）双向模式打开指定文件并绑定到文件描述符 `n`（默认为 0）。

- **语法**：`[n]<> word`
- **规则**：若文件不存在且重定向未引发错误，则创建该文件；文件不会被清空截断。

## 2.8 退出状态与错误 (Exit Status and Errors)

### 2.8.1 Shell 错误后果 (Consequences of Shell Errors)

Shell 处理错误时，根据 Shell 是处于**交互式 (Interactive)** 还是**非交互式 (Non-Interactive)** 状态，以及错误的类型，采取不同的处理策略：

1. **严重错误（如语法解析错误、无效的重定向语法、特殊内置命令失败）**：
   - **非交互式脚本**：Shell 输出诊断信息，并**立即终止脚本的执行**，退出码为非零。
   - **交互式 Shell**：输出诊断信息，放弃当前命令行的执行，刷新提示符并等待用户下一条输入。
2. **普通错误（如外部命令未找到、常规内置命令失败、命令因无权限不可执行）**：
   - Shell 输出错误信息，将退出码变量 `$?` 设置为对应的非零数值，并**继续按顺序执行**后续命令。

### 2.8.2 命令退出状态 (Exit Status for Commands)

每个命令在执行完成后都会向 Shell 返回一个介于 0 到 255 之间的十进制整数作为其退出状态码（Exit Status）：

- **`0`**：代表命令**成功执行 (Success)**。
- **`1` 到 `125`**：代表命令执行失败，具体的数值由各个命令实用程序自定义（例如 `1` 通常代表常规通用错误，`2` 代表命令行参数语法错误）。
- **`126`**：找到了请求的命令文件，但该文件**不可执行**（例如没有可执行 `+x` 权限，或者不是合法的可执行二进制格式）。
- **`127`**：在 `PATH` 路径中**未找到指定的命令**（Command not found）。
- **`128`**：标准保留。
- **`> 128` (即 `128 + N`)**：命令因捕获到操作系统**信号 (Signal)** $N$ 而被强行终止执行。例如，如果命令被 `SIGKILL` (信号 9) 杀死，其退出码为 $128 + 9 = 137$；如果被 `SIGINT` (Ctrl+C，信号 2) 中断，其退出码为 $128 + 2 = 130$。

## 2.9 Shell 命令 (Shell Commands)

当词法分析与语法解析完成后，Shell 将识别出的语法结构划分为不同层级的命令形式，并按规定的语义依次执行。

### 2.9.1 简单命令 (Simple Commands)

简单命令是 Shell 中最基础的执行单元。它由一系列可选的**变量赋值 (Variable Assignments)**、**重定向 (Redirections)**，以及可选的**命令名称 (Command Name)** 与**命令参数 (Command Words)** 组成。

#### 2.9.1.1 处理顺序 (Order of Processing)

当 Shell 执行一条简单命令时，严格按照以下顺序依次处理：

1. **确定语法成分**：根据 Token 识别规则，分离出变量赋值、重定向指示以及命令单词（首个非变量赋值的单词作为命令名，后续单词作为参数）。
2. **执行扩展**：
   - 对变量赋值中的值表达式、重定向的操作数，以及命令名与参数单词进行波浪号扩展、参数扩展、命令替换、算术扩展、字段分割、路径名扩展与引用消除。
   - **注意**：命令名扩展后的结果必须是单个单词。若扩展后无单词产生，则视该命令无命令名。
3. **设置重定向**：在当前执行环境中按从左到右的顺序依次打开或复制重定向文件中指定的文件描述符。
4. **处理变量赋值**：
   - 若存在命令名：变量赋值将作为临时环境变量传入该命令的执行环境，**不影响**当前 Shell 本身的同名变量（除非调用的命令是特殊内置命令）。
   - 若不存在命令名：变量赋值将直接**修改当前 Shell 环境**中的变量。

#### 2.9.1.2 变量赋值 (Variable Assignments)

- 格式为 `NAME=VALUE`。
- 发生在命令名之前的变量赋值只在**该简单命令执行期间**有效。
- 若赋值过程中发生扩展错误（例如算术扩展除以零），则整条命令终止执行，退出码为非零。

#### 2.9.1.3 无命令名的命令 (Commands with no Command Name)

若简单命令扩展后不包含任何命令名（例如只有 `VAR=value` 或只有 `< input.txt > output.txt`）：

- 重定向将在当前 Shell 环境中依次建立并闭合。
- 变量赋值将直接在当前 Shell 环境中生效。
- 若重定向或扩展过程未发生错误，退出状态码为 **0**；若在此过程中打开文件失败，退出状态码为非零（1–125）。

#### 2.9.1.4 命令搜索与执行 (Command Search and Execution)

当简单命令包含命令名时，Shell 按照以下严格优先顺序查找并调用对应的实体：

1. **特殊内置命令 (Special Built-In Utilities)**：
   - 若命令名匹配 2.15 节列出的 15 个特殊内置命令之一，直接在当前 Shell 环境中执行它。
2. **Shell 函数 (Shell Functions)**：
   - 若命令名匹配当前 Shell 环境中已定义的函数名，则在当前 Shell 中跳转执行该函数体，位置参数临时被替换为传给函数的实参。
3. **常规内置命令 (Regular Built-In Utilities)**：
   - 若命令名匹配 Shell 内置实现的常规实用程序（如 `cd`, `echo`, `pwd` 等），直接在当前 Shell 中执行它。
4. **`PATH` 路径搜索与外部可执行文件**：
   - 若命令名包含斜杠 `/`，Shell 直接将该命令名作为文件路径加载。
   - 若命令名不含斜杠，Shell 逐个检索环境变量 `PATH` 中由冒号分隔的目录列表：
     - 若找到匹配的外部可执行文件（且具备可执行权限），派生子进程调用 `execve()` 执行。
     - 若找到的文件不具备可执行权限，搜索终止，命令返回退出状态码 **126**。
     - 若遍历 `PATH` 目录后仍未找到匹配的文件，命令返回退出状态码 **127**。
     - 若该文件属于非二进制的文本脚本但未包含 `#!`， Shell 会派生子 Shell 解释执行该脚本。

#### 2.9.1.5 标准文件描述符 (Standard File Descriptors)

在命令执行前，重定向将按顺序修饰标准文件描述符（FD 0 为 standard input，FD 1 为 standard output，FD 2 为 standard error）。执行实体继承重定向完成后的 FD 状态。

#### 2.9.1.6 非内置实用程序执行 (Non-built-in Utility Execution)

当找到外部可执行文件时，Shell 派生子进程并向其传递环境变量与位置参数。被调用的外部进程执行完毕后，向父 Shell 返回其退出状态码。

### 2.9.2 管道 (Pipelines)

管道是由一个或多个通过管道控制运算符 `|` 分隔的命令组成的序列。

- **语法格式**：`[!] command1 [ | command2 ... ]`
- **执行语义**：
  - 前一个命令 `command1` 的标准输出（FD 1）通过无名管道（Pipe）连接到后一个命令 `command2` 的标准输入（FD 0）。
  - 管道中的每个命令都在独立的**子 Shell (Subshell)** 环境中并行执行。
  - 若开头包含未引用的感叹号 `!`，则整个管道最终的退出状态码将被进行**逻辑非 (Logical NOT)** 取反操作（成功变失败，失败变成功）。

#### 退出状态 (Exit Status)

- 管道的退出状态码**默认为管道中最后一个命令的退出状态码**。
- 若管道开头带有 `!` 运算符：
  - 若最后一个命令的退出状态码为 0，整个管道的退出状态码为 **1**。
  - 若最后一个命令的退出状态码非 0，整个管道的退出状态码为 **0**。

### 2.9.3 命令列表 (Lists)

命令列表（List）是由一个或多个通过 `;`, `&`, `&&`, `||`, `\n` 分隔的管道或复合命令构成的序列。

#### 实例 (Examples)


```bash
# 示例 1: 逻辑与和逻辑或组合列表
make -j4 && make install || echo "Build failed"

# 示例 2: 顺序执行列表
cd /tmp ; ls -la
```

#### 2.9.3.1 异步 AND-OR 列表 (Asynchronous AND-OR Lists)

- **语法格式**：`list &`
- **语义**：Shell 在后台派生独立的子 Shell 异步执行 `list`。主 Shell 不需要等待该 `list` 执行结束，可立即读取并执行下一条命令。

##### 退出状态 (Exit Status)

主 Shell 在成功启动后台进程的瞬间，立刻返回退出状态码 **0**。特殊参数 `!` 被更新为该后台进程的 PID。

#### 2.9.3.2 顺序 AND-OR 列表 (Sequential AND-OR Lists)

- **语法格式**：`list1 ; list2` 或 `list1 <newline> list2`
- **语义**：Shell 先同步执行 `list1`，等待 `list1` 彻底执行完成后，再按顺序同步执行 `list2`。

##### 退出状态 (Exit Status)

顺序列表的退出状态码即为列表中最后一个被执行命令的退出状态码。

#### 2.9.3.3 AND 列表 (AND Lists)

- **语法格式**：`command1 && command2`
- **语义**：短路求值逻辑与。 Shell 首先执行 `command1`：
  - 若 `command1` 的退出状态码为 **0**（成功），则继续执行 `command2`。
  - 若 `command1` 的退出状态码**非零**（失败），短路跳过 `command2` 的执行。

##### 退出状态 (Exit Status)

退出状态码为该结构中最后一条实际被执行的命令的退出状态码。若 `command1` 失败而跳过 `command2`，则返回 `command1` 的退出状态码。

#### 2.9.3.4 OR 列表 (OR Lists)

- **语法格式**：`command1 || command2`
- **语义**：短路求值逻辑或。 Shell 首先执行 `command1`：
  - 若 `command1` 的退出状态码**非零**（失败），则继续执行 `command2`。
  - 若 `command1` 的退出状态码为 **0**（成功），短路跳过 `command2` 的执行。

##### 退出状态 (Exit Status)

退出状态码为该结构中最后一条实际被执行的命令的退出状态码。若 `command1` 成功而跳过 `command2`，则返回 `command1` 的退出状态码（即 0）。

### 2.9.4 复合命令 (Compound Commands)

复合命令是包含了其他命令列表的高级语法控制结构。

#### 2.9.4.1 组合命令 (Grouping Commands)

组合命令将一系列命令包裹在一起，作为一个整体进行重定向或控制流操作。

1. **子 Shell 形式**：`( compound-list )`
   - 命令列表 `compound-list` 在派生的**子 Shell 环境**中执行。内部发生的变量修改、工作目录变更（`cd`）或环境更改均**不会反哺影响**父 Shell。
2. **当前 Shell 形式**：`{ compound-list; }`
   - 命令列表在**当前 Shell 环境**中直接执行。
   - **注意**：`{` 和 `}` 是保留字，`{` 后必须有空白字符，`}` 前必须有分号 `;` 或换行符。

##### 退出状态 (Exit Status)

组合命令的退出状态码为 `compound-list` 中最后一条执行命令的退出状态码。

#### 2.9.4.2 for 循环 (The for Loop)

- **语法格式**：


  ```bash
  for name [ in [ word ... ] ]
  do
      compound-list
  done
  ```

- **语义**：

  - 将 `word` 列表依次进行单词扩展。
  - 对于扩展后的每一个结果，将其赋值给变量 `name`，并执行一次 `compound-list`。
  - 若省略 `in [ word ... ]` 部分，默认等价于 `in "$@"`（即遍历当前位置参数列表）。

##### 退出状态 (Exit Status)

循环体内最后一条实际执行命令的退出状态码。若 `word` 列表扩展为空导致循环体一次未执行，退出状态码为 **0**。

#### 2.9.4.3 case 条件分支 (Case Conditional Construct)

- **语法格式**：


  ```bash
  case word in
      [(] pattern1 [| pattern2] ... ) compound-list ;;
      [(] pattern3 ... ) compound-list ;;
  esac
  ```

- **语义**：

  - 对 `word` 进行扩展，并将其与模式 `pattern1`, `pattern2` ... 按照 2.14 节的模式匹配规则依次进行比较（管道符 `|` 代表“或”逻辑）。
  - 遇到第一个匹配成功的模式分支，执行其对应的 `compound-list`，执行完毕后遇到 `;;` 结束整个 `case` 结构的运行（不向下贯穿）。

##### 退出状态 (Exit Status)

被选中的匹配分支内最后一条命令的退出状态码。若无任何模式匹配成功，退出状态码为 **0**。

#### 2.9.4.4 if 条件分支 (The if Conditional Construct)

- **语法格式**：


  ```bash
  if compound-list1; then
      compound-list2;
  [elif compound-list3; then
      compound-list4;]
  ...
  [else
      compound-list5;]
  fi
  ```

- **语义**：

  - 执行 `compound-list1`，若其退出状态码为 **0**，则执行 `then` 后面的 `compound-list2`。
  - 若退出状态码非零，依次求值后续 `elif` 条件；若所有条件均不满足，执行 `else` 分支中的 `compound-list5`。

##### 退出状态 (Exit Status)

被选中的分支内最后一条命令的退出状态码。若无条件触发且无 `else` 分支，退出状态码为 **0**。

#### 2.9.4.5 while 循环 (The while Loop)

- **语法格式**：


  ```bash
  while compound-list1
  do
      compound-list2
  done
  ```

- **语义**：

  - 重复求值条件列表 `compound-list1`。只要其退出状态码为 **0**，就持续执行循环体 `compound-list2`。

##### 退出状态 (Exit Status)

循环体 `compound-list2` 内最后一条实际被执行命令的退出状态码。若首次条件判断即为非零而未进入循环体，退出状态码为 **0**。

#### 2.9.4.6 until 循环 (The until Loop)

- **语法格式**：


  ```bash
  until compound-list1
  do
      compound-list2
  done
  ```

- **语义**：

  - 重复求值条件列表 `compound-list1`。只要其退出状态码**非零**，就持续执行循环体 `compound-list2`（即条件为假时执行，条件为真时终止）。

##### 退出状态 (Exit Status)

循环体 `compound-list2` 内最后一条实际被执行命令的退出状态码。若首次条件判断即为 0 而未进入循环体，退出状态码为 **0**。

### 2.9.5 函数定义命令 (Function Definition Command)

- **语法格式**：


  ```bash
  fname() compound-command [ redirection ... ]
  ```

- **语义**：

  - 在当前 Shell 环境中注册一个名为 `fname` 的函数，其函数体为复合命令 `compound-command`（通常是 `{ compound-list; }`）。
  - 可以在函数定义的末尾附加重定向，该重定向将在每次调用该函数时生效。
  - 当函数被调用时，当前 Shell 环境的位置参数临时替换为传入的实参；当函数执行完毕或遇到内置命令 `return` 时，恢复原位置参数。

##### 退出状态 (Exit Status)

函数声明定义的退出状态码为 **0**（若定义过程发生语法错误则为非零）。当函数被调用执行时，其退出状态码为函数体内最后一条被执行命令的退出状态码，或 `return [n]` 命令显式指定的数值 `n`。

## 2.10 Shell 语法 (Shell Grammar)

Shell 语法通过正式的上下文无关文法（Context-Free Grammar）完整定义。

### 2.10.1 Shell 语法词法约定 (Shell Grammar Lexical Conventions)

词法分析器（Lexer）在将字符流转换为文法终结符（Terminal Symbols）时，遵循以下命名约定：

- **`WORD`**：普通单词 Token。
- **`NAME`**：合法的标示符名称（用于变量名或函数名）。
- **`ASSIGNMENT_WORD`**：形如 `NAME=VALUE` 的变量赋值 Token。
- **`IO_NUMBER`**：紧跟重定向运算符的无符号十进制数字字符串（如 `2>` 中的 `2`）。
- **运算符终结符**：
  - `AND_IF` : `&&`
  - `OR_IF` : `||`
  - `DSEMI` : `;;`
  - `DLESS` : `<<`
  - `DGREAT` : `>>`
  - `LESSAND` : `<&`
  - `GREATAND` : `>&`
  - `LESSGREAT` : `<>`
  - `DLESSDASH` : `<<-`
  - `CLOBBER` : `>|`

### 2.10.2 Shell 语法规则 (Shell Grammar Rules)

以下为 POSIX.1-2024 定义的标准巴科斯-诺尔范式（BNF）产生式方程（完整精确展开）：

BNF

```
%token  WORD
%token  ASSIGNMENT_WORD
%token  NAME
%token  NEWLINE
%token  IO_NUMBER

/* 运算符标记 */
%token  AND_IF    OR_IF    DSEMI
%token  DLESS     DGREAT   LESSAND  GREATAND  LESSGREAT  DLESSDASH
%token  CLOBBER

/* 保留字标记 */
%token  If        Then     Else     Elif     Fi
%token  Do        Done     Case     Esac     While    Until
%token  For       In
%token  Lbrace    Rbrace   Bang

%start  program
%%

program          : linebreak input_unit
                 | linebreak
                 ;

input_unit       : compound_list simple_list_terminator
                 | simple_list simple_list_terminator
                 ;

simple_list_terminator : NEWLINE
                 | ';'
                 ;

compound_list    : linebreak term
                 | linebreak term separator
                 ;

term             : term separator and_or
                 | and_or
                 ;

and_or           : pipeline
                 | and_or AND_IF linebreak pipeline
                 | and_or OR_IF  linebreak pipeline
                 ;

pipeline         : pipe_sequence
                 | Bang pipe_sequence
                 ;

pipe_sequence    : command
                 | pipe_sequence '|' linebreak command
                 ;

command          : simple_command
                 | compound_command
                 | compound_command redirect_list
                 | function_definition
                 ;

compound_command : brace_group
                 | subshell
                 | for_clause
                 | case_clause
                 | if_clause
                 | while_clause
                 | until_clause
                 ;

subshell         : '(' compound_list ')'
                 ;

brace_group      : Lbrace compound_list Rbrace
                 ;

for_clause       : For name linebreak do_group
                 | For name linebreak in word_list sequential_sep do_group
                 ;

name             : NAME
                 ;

word_list        : word_list WORD
                 | WORD
                 ;

case_clause      : Case WORD linebreak in linebreak case_list Esac
                 | Case WORD linebreak in linebreak case_list_ns Esac
                 | Case WORD linebreak in linebreak Esac
                 ;

case_list        : case_list case_item
                 | case_item
                 ;

case_list_ns     : case_list case_item_ns
                 | case_item_ns
                 ;

case_item        : pattern ')' compound_list DSEMI linebreak
                 | pattern ')' linebreak DSEMI linebreak
                 | '(' pattern ')' compound_list DSEMI linebreak
                 | '(' pattern ')' linebreak DSEMI linebreak
                 ;

case_item_ns     : pattern ')' compound_list
                 | pattern ')' linebreak
                 | '(' pattern ')' compound_list
                 | '(' pattern ')' linebreak
                 ;

pattern          : WORD
                 | pattern '|' WORD
                 ;

if_clause        : If compound_list Then compound_list else_part Fi
                 | If compound_list Then compound_list Fi
                 ;

else_part        : Elif compound_list Then compound_list else_part
                 | Elif compound_list Then compound_list
                 | Else compound_list
                 ;

while_clause     : While compound_list do_group
                 ;

until_clause     : Until compound_list do_group
                 ;

do_group         : Do compound_list Done
                 ;

function_definition : fname '(' ')' linebreak function_body
                 ;

fname            : NAME
                 ;

function_body    : compound_command
                 | compound_command redirect_list
                 ;

simple_command   : cmd_prefix cmd_word cmd_suffix
                 | cmd_prefix cmd_word
                 | cmd_prefix
                 | cmd_word cmd_suffix
                 | cmd_word
                 ;

cmd_prefix       : io_redirect
                 | cmd_prefix io_redirect
                 | ASSIGNMENT_WORD
                 | cmd_prefix ASSIGNMENT_WORD
                 ;

cmd_word         : WORD
                 ;

cmd_suffix       : io_redirect
                 | cmd_suffix io_redirect
                 | WORD
                 | cmd_suffix WORD
                 ;

redirect_list    : io_redirect
                 | redirect_list io_redirect
                 ;

io_redirect      : io_file
                 | IO_NUMBER io_file
                 | io_here
                 | IO_NUMBER io_here
                 ;

io_file          : '<'       filename
                 | LESSAND   filename
                 | '>'       filename
                 | GREATAND  filename
                 | DGREAT    filename
                 | LESSGREAT filename
                 | CLOBBER   filename
                 ;

filename         : WORD
                 ;

io_here          : DLESS     here_end
                 | DLESSDASH here_end
                 ;

here_end         : WORD
                 ;

newline_list     : NEWLINE
                 | newline_list NEWLINE
                 ;

linebreak        : newline_list
                 | /* empty */
                 ;

separator_op     : '&'
                 | ';'
                 ;

separator        : separator_op linebreak
                 | newline_list
                 ;

sequential_sep   : ';' linebreak
                 | newline_list
                 ;
```

## 2.11 作业控制 (Job Control)

作业控制（Job Control）是 Shell 允许单个终端会话管理与调度多个并发进程组（Process Groups / Jobs）的机制。

- **前台作业 (Foreground Job)**：当前独占终端输入/输出与信号响应的进程组。
- **后台作业 (Background Job)**：在后台并发运行的进程组，其 stdin 读取默认受到限制（若尝试读取终端输入会收到 `SIGTTIN` 信号而暂停）。
- **作业状态转换**：
  - 使用 `Ctrl+Z` 发送 `SIGTSTP` 信号可以**暂停 (Stop)** 当前前台作业。
  - 内置命令 `bg` 可将已暂停的作业转换为**后台继续运行**状态。
  - 内置命令 `fg` 可将后台运行或暂停的作业提拉回**前台执行**。
  - 使用 `%n`（作业标识符，如 `%1`, `%+`, `%-`）来指定具体的作业。

## 2.12 信号与错误处理 (Signals and Error Handling)

当操作系统向 Shell 进程发送异步信号时，Shell 遵循以下处理语义：

- **`SIGINT` (中断信号，如 Ctrl+C)**：
  - 在交互式 Shell 中：立即打断当前输入或正在前台运行的命令，清空命令行缓冲区，重新输出 `PS1` 提示符。
  - 在 Shell 脚本中：若未设置 `trap` 捕获，则直接终止当前脚本的执行。
- **`SIGQUIT` (退出信号，如 Ctrl+)**：
  - 交互式 Shell 默认**完全忽略**此信号。
- **`SIGHUP` (挂断信号)**：
  - 当终端连接断开时，Shell 退出前会向由其启动的所有作业发送 `SIGHUP` 信号，确保无残留孤儿进程。
- **`trap` 实用程序机制**：
  - 用户可以通过内置命令 `trap 'action' SIGNAL` 注册自定义捕获函数。
  - 当捕获到对应信号时，暂停当前命令流并执行 `action` 文本中的 Shell 命令。

## 2.13 Shell 执行环境 (Shell Execution Environment)

Shell 执行环境（Execution Environment）是维持命令求值与状态运行的全套上下文。它包含以下要素：

1. **文件描述符**：打开的文件映射表（FD 0, FD 1, FD 2 等）。
2. **当前工作目录 (PWD)**：由 `cd` 管理。
3. **文件创建掩码 (umask)**：控制新创建文件的默认权限。
4. **信号处理表 (trap)**：记录各个信号的忽略、默认或捕获状态。
5. **环境与 Shell 变量**：包含导出与未导出的变量值。
6. **Shell 函数与别名定义**：当前会话注册的函数和别名。
7. **选项标志 (Option Flags)**：通过启动选项或 `set` 命令激活的参数设置（如 `-e`, `-x`, `-f` 等）。
8. **位置参数 (`$1`, `$2` ...) 与特殊参数**。
9. **当前进程 PID (`$$`) 与父进程 PPID (`$PPID`)**。

#### 子 Shell 环境 (Subshell Execution Environment)

在管道、组合命令 `(...)` 或命令替换中创建的子 Shell 环境，将完整继承父 Shell 的上述绝大部分环境要素，但子 Shell 中对变量、工作目录、信号 trap 或 FD 进行的**任何修改，均无法反哺回父 Shell 环境**。

## 2.14 模式匹配符号 (Pattern Matching Notation)

模式匹配（Pattern Matching）用于路径名扩展（Globbing）、`case` 结构以及字符串裁切扩展。

### 2.14.1 单个字符匹配模式 (Patterns Matching a Single Character)

- **`?` (问号)**：匹配任何**单个字符**。
- **`[...]` (字符集/括号表达式)**：
  - 匹配方括号内包含的任意单个字符（如 `[abc]`）。
  - 支持连字符范围匹配（如 `[a-z]`，其行为取决于当前 Locale 的排序规则）。
  - 支持 POSIX 字符类，如 `[:alpha:]`, `[:digit:]`, `[:alnum:]`, `[:space:]` 等（例如 `[[:digit:]]` 匹配任意数字）。
  - **取反**：若括号内首字符为 `!` 或 `^`（如 `[!0-9]`），匹配**不在**该集合中的任意单个字符。

### 2.14.2 多个字符匹配模式 (Patterns Matching Multiple Characters)

- **`\*` (星号)**：匹配包含空字符串在内的任意**零个或多个字符**组成的序列。

### 2.14.3 用于文件名扩展的模式 (Patterns Used for Filename Expansion)

在路径名扩展（Pathname Expansion）中，模式匹配遵循以下两条特化限制：

1. **斜杠 `/` 的硬性约束**：
   - 路径分隔符 `/` **必须被显式匹配**。模式字符 `*`、`?` 以及括号表达式 `[...]` **绝对不能**跨越或匹配路径中的斜杠字符 `/`。
2. **隐藏点号 `.` (Leading Period) 的约束**：
   - 若文件名或路径节点以点号 `.` 开头（隐藏文件），则该开头的 `.` **必须被模式中的字面点号显式匹配**。模式字符 `*` 或 `?` 在路径节点开头时不能隐式匹配该点号（除非开启了特化扩展选项）。

## 2.15 特殊内置命令 (Special Built-In Utilities)

POSIX.1-2024 标准严格定义了以下 15 个特殊内置命令（Special Built-In Utilities）。

它们与常规 Built-in 或外部命令相比，具备以下 3 个特化核心语义：

1. **语法严重错误响应**：特殊内置命令发生语法错误或执行失败时，**会导致非交互式脚本直接终止退出**。
2. **变量赋值永久生效**：在特殊内置命令之前指定的变量赋值（如 `VAR=val exec ...`），将在该内置命令执行完成后**永久保留在当前 Shell 环境中**。
3. **命令查找优先级最高**：它们在命令查找顺序中处于第一优先级，且无法被用户定义的同名函数覆盖。

### 15 个特殊内置命令全清单：

1. **`.` (dot / source)**：在当前 Shell 环境中读取并执行指定文件中的命令。
2. **`:` (colon)**：空命令（Null command），不做任何操作，固定返回退出状态码 0。
3. **`break`**：跳出最近的 `for`, `while`, `until` 循环。
4. **`continue`**：跳过当前循环剩余部分，开始下一次 `for`, `while`, `until` 循环迭代。
5. **`eval`**：将其参数连接为一个字符串，并重新解析、执行该 Shell 命令行。
6. **`exec`**：用指定的命令直接**替换当前 Shell 进程**（不派生子进程）；若仅包含重定向，则永久修改当前 Shell 的文件描述符。
7. **`exit`**：终止当前 Shell 的运行，并向父进程返回指定的退出状态码。
8. **`export`**：将 Shell 变量提升导出为环境变量，传递给后续所有子进程。
9. **`readonly`**：将 Shell 变量或函数标记为只读（Read-Only），禁止对其进行重新赋值或取消定义。
10. **`return`**：从当前正在执行的 Shell 函数或被 `.`/`source` 引用的脚本文件中返回。
11. **`set`**：设置/重置 Shell 的选项标志位，或重新批量设置位置参数（`$1`, `$2` ...）。
12. **`shift`**：将位置参数向左平移指定个数。
13. **`times`**：累计并打印当前 Shell 及其已结束子进程所消耗的 CPU 用户时间与系统时间。
14. **`trap`**：为操作系统信号注册自定义捕获动作或恢复默认处理。
15. **`unset`**：取消定义并删除指定的变量或函数。

以下为您详细梳理 POSIX.1-2024 标准定义的 15 个特殊内置命令（Special Built-In Utilities）。

每个命令均包含**标准语法、核心功能描述、详细选项/参数解析、核心行为特性**以及**实际应用场景示例**。

### 1. `.` (dot) / `source`

在当前 Shell 执行环境中直接读取并执行指定文件中的命令（不派生子进程）。

#### 语法

Bash

```
. filename [argument...]
```

#### 选项与参数

- **`filename`**：包含 Shell 命令的文件路径。
  - 若路径中包含斜杠 `/`，Shell 直接按路径寻找文件。
  - 若路径不含斜杠 `/`，Shell 将在环境变量 `PATH` 所列出的目录中逐个检索该文件。
- **`argument...`**：可选参数。若指定了参数，它们将在执行该文件期间**临时替换**当前 Shell 的位置参数（`$1`, `$2` ...）。执行结束后恢复原位置参数。

#### 行为特性

- **环境变量共享**：被执行脚本中对变量的修改、`cd` 目录切换、`alias` 或函数定义，将**直接生效于当前父 Shell 环境**。
- **退出状态码**：为脚本中最后一条被执行命令的退出状态码；若文件为空，则为 0；若文件无法读取或找不到，返回非零状态码（脚本可能直接终止）。

#### 常见示例

Bash

```
# 加载环境变量配置文件
. ~/.bashrc

# 执行脚本并向其传递临时位置参数 $1 和 $2
. ./scripts/setup.sh --production --verbose
```

### 2. `:` (colon)

空命令（Null Command），对参数进行扩展但不执行任何具体操作。

#### 语法

Bash

```
: [argument...]
```

#### 选项与参数

- **`argument...`**：任何合法的单词或表达式。虽然命令本身什么都不做，但 Shell **依然会对这些参数进行完整的语法扩展**（如变量扩展、命令替换、算术扩展）。

#### 行为特性

- **固定返回值**：无论传入什么参数，退出状态码固定为 **0**。
- **副作用**：常用于通过参数扩展机制产生“副作用”（如对变量设置默认值），或者作为无限循环的条件占位符。

#### 常见示例

Bash

```
# 示例 1: 无限循环占位符
while : ; do
    echo "Running daemon..."
    sleep 5
done

# 示例 2: 利用参数扩展为未定义的变量提供默认值（若 VAR 未设置，则赋初值 "default"）
: "${VAR:=default}"

# 示例 3: 快速清空文件内容（不产生输出重定向至文件）
: > output.log
```

### 3. `break`

用于立即跳出最近的 `for`、`while` 或 `until` 循环体。

#### 语法

Bash

```
break [n]
```

#### 选项与参数

- **`n`**：一个大于等于 1 的正整数，指定要跳出的**循环嵌套层数**。默认为 `1`（即跳出当前所在的最内层循环）。若 `n` 大于当前的实际嵌套层数，Shell 将跳出最外层循环。

#### 行为特性

- 只能在循环体内部调用，在循环体外调用将被忽略或报语法错误。

#### 常见示例

Bash

```
# 跳出多层嵌套循环
for i in 1 2 3; do
    for j in a b c; do
        if [ "$i" -eq 2 ] && [ "$j" = "b" ]; then
            echo "Breaking 2 levels of loop at i=$i, j=$j"
            break 2  # 同时跳出内层与外层循环
        fi
        echo "$i - $j"
    done
done
```

### 4. `continue`

用于跳过当前循环体中剩余的语句，直接进入下一次循环迭代。

#### 语法

Bash

```
continue [n]
```

#### 选项与参数

- **`n`**：一个大于等于 1 的正整数，指定要执行下一次迭代的**循环嵌套层数**。默认为 `1`（即对当前最内层循环生效）。若 `n` 为 2，则代表跳过当前层并触发上一层外层循环的下一次迭代。

#### 行为特性

- 执行后，`for` 循环会直接取下一个元素；`while`/`until` 循环会直接跳回到条件测试部分。

#### 常见示例

Bash

```
# 跳过偶数，只打印奇数
for num in 1 2 3 4 5; do
    if [ $((num % 2)) -eq 0 ]; then
        continue
    fi
    echo "Odd number: $num"
done
```

### 5. `eval`

将传入的所有参数连接成一个字符串，并将其作为一条全新的 Shell 命令行重新进行解析与执行。

#### 语法

Bash

```
eval [argument...]
```

#### 选项与参数

- **`argument...`**：要拼装并重新求值的命令字符串。

#### 行为特性

- **二次解析机制**：Shell 在常规扫描解析完命令后，`eval` 会将其结果再次送入 Shell 的词法与语法分析器。这使得开发者可以实现**动态变量名引用**（如间接引用）或动态构建复杂的管道命令。

#### 常见示例

Bash

```
# 示例 1: 变量的间接引用
VAR_NAME="target"
target="Hello, World!"

# 重新解析后相当于执行: echo "$target"
eval "echo \$$VAR_NAME"  # 输出: Hello, World!

# 示例 2: 执行动态生成的复杂命令
CMD="ls -l | grep txt"
eval "$CMD"
```

### 6. `exec`

用指定的外部命令直接**替换当前 Shell 进程**；或者在不指定命令时，永久修改当前 Shell 环境的文件描述符重定向。

#### 语法

Bash

```
exec [command [argument...]] [redirection...]
```

#### 选项与参数

- **`command`**：要执行的外部可执行程序。
- **`redirection...`**：针对标准输入/输出或文件描述符（FD）的重定向表达式。

#### 行为特性

- **替换进程**：若指定了 `command`，内核将调用 `execve()` 载入新程序，**当前 Shell 进程被彻底覆盖，PID 保持不变**。新程序执行完毕后直接退出，**不会返回**到原脚本中。
- **修改 FD**：若**未指定** `command` 且包含重定向，重定向将在当前 Shell 生效，并**持续影响后续所有命令**。

#### 常见示例

Bash

```
# 示例 1: 在当前 Shell 中永久将 FD 3 重定向打开到指定日志文件，并重定向标准输出
exec 3> app.log
exec > output.log

echo "This output goes to output.log"
echo "This goes to app.log" >&3

# 示例 2: 在容器启动脚本末尾用主程序替换 Shell，确保主程序为 PID 1 并能正确接管 SIGTERM 信号
exec nginx -g 'daemon off;'
```

### 7. `exit`

终止当前 Shell 进程或脚本的运行，并向父进程返回指定的退出状态码。

#### 语法

Bash

```
exit [n]
```

#### 选项与参数

- **`n`**：一个无符号整数（有效范围通常为 `0–255`），代表返回给父进程的退出状态码（Exit Code）。
  - `0`：代表成功（Success）。
  - 非零 (`1–255`)：代表发生了不同类型的错误。
  - 若省略 `n`，默认使用**上一条被执行命令的退出状态码**。

#### 行为特性

- 在终端交互式 Shell 中调用会导致当前终端窗口/会话关闭。
- 在被 `.` 或 `source` 引用的脚本中调用，会直接退出**主 Shell** 而非仅终止子脚本。

#### 常见示例

Bash

```
# 参数校验失败时退出脚本并返回错误码 1
if [ -z "$1" ]; then
    echo "Error: Missing required argument." >&2
    exit 1
fi

echo "Processing..."
exit 0
```

### 8. `export`

将指定的 Shell 变量标记为导出状态，使其能够被当前 Shell 派生的所有子进程继承。

#### 语法

Bash

```
export [-p] [name[=value]...]
```

#### 选项与参数

- **`-p`**：以可重新输入的格式（如 `export name="value"`）列出当前 Shell 环境中已导出的所有环境变量。
- **`name[=value]`**：要导出的变量名及其可选的赋值表达式。

#### 行为特性

- **单向传递**：子进程继承环境变量后，子进程内对其进行的修改**无法反哺**回父 Shell。
- 不带任何参数的 `export` 等价于 `export -p`。

#### 常见示例

Bash

```
# 导出单个已有变量
PATH="/usr/local/bin:$PATH"
export PATH

# 导出并同时赋值
export NODE_ENV="production"

# 查看当前所有导出的环境变量
export -p
```

### 9. `readonly`

将 Shell 变量或函数标记为只读（Read-Only）。只读变量和函数无法被重新赋值、重新定义或被 `unset` 删除。

#### 语法

Bash

```
readonly [-p] [name[=value]...]
readonly -f [-p] [name...]
```

#### 选项与参数

- **`-f`**：指定作用对象为 **Shell 函数**。
- **`-p`**：以可重新输入的格式打印当前 Shell 中所有只读变量（或函数）的列表。

#### 行为特性

- 一旦变量或函数被标记为 `readonly`，在当前 Shell 进程生命周期内**没有任何命令可以撤销其只读状态**。

#### 常见示例

Bash

```
# 1. 声明只读变量
readonly MAX_CONNECTIONS=100
MAX_CONNECTIONS=200  # 报错: MAX_CONNECTIONS: is read only

# 2. 声明只读函数
my_func() {
    echo "Core function"
}
readonly -f my_func
```

### 10. `return`

从当前正在执行的 Shell 函数（Function）或由 `.` / `source` 引用的脚本文件中返回。

#### 语法

Bash

```
return [n]
```

#### 选项与参数

- **`n`**：函数的退出状态码（同样推荐为 `0–255` 的整数）。若省略 `n`，则默认返回函数内部最后一条实际被执行命令的退出状态码。

#### 行为特性

- 若在函数内部调用，立即中断函数体执行并返回主调环境。
- 若在通过 `.` 或 `source` 加载的脚本中调用，立即停止执行该脚本，将控制权还给父脚本（与 `exit` 不同，它**不会终止**父 Shell）。
- 在上述环境之外（即主脚本顶级作用域）直接调用 `return` 属于语法错误。

#### 常见示例

Bash

```
is_root() {
    if [ "$(id -u)" -eq 0 ]; then
        return 0  # 逻辑真
    else
        return 1  # 逻辑假
    fi
}

if is_root; then
    echo "Running as root."
fi
```

### 11. `set`

用于设置或重置当前 Shell 的控制选项标志位（Option Flags），以及重新批量覆盖设置位置参数（`$1`, `$2` ...）。

#### 语法

Bash

```
set [-abefhkmnptuvxBCEHPT] [-o option-name] [argument...]
set [+abefhkmnptuvxBCEHPT] [+o option-name] [argument...]
set -- [argument...]
```

#### 常用选项解析

- **`-`（连字符）激活选项，`+`（加号）关闭选项**。
- **`-e` (`-o errexit`)**：若任何命令返回非零退出状态码，立即终止 Shell 脚本执行。
- **`-x` (`-o xtrace`)**：在执行命令前，先在终端打印出扩展后的命令行（常用于调试）。
- **`-u` (`-o nounset`)**：遇到未定义的扩展变量时，将其视为错误并终止执行。
- **`-f` (`-o noglob`)**：禁用文件名路径扩展（Globbing，即禁用 `*` 和 `?`）。
- **`--`**：分隔符。防止后续的 `argument` 被误识别为选项。即使后续参数以 `-` 开头，也会被强行设置为位置参数 `$1`, `$2` 等。

#### 行为特性

- **无参数**：若不带任何选项与参数调用 `set`，将列出当前 Shell 中的所有变量与函数名。

#### 常见示例

Bash

```
# 示例 1: 现代化 Shell 脚本安全开局配置
set -euo pipefail  # 遇到错误即停、未定义变量报错、管道中任何一环报错即算整体失败

# 示例 2: 重新切割并覆盖位置参数
set -- "alpha" "beta" "gamma"
echo "$1"  # 输出: alpha
echo "$2"  # 输出: beta
```

### 12. `shift`

将位置参数从 `$1` 开始向左平移指定个数，原有的高位位置参数依次递补覆盖低位参数。

#### 语法

Bash

```
shift [n]
```

#### 选项与参数

- **`n`**：要向左平移的位置参数个数。必须为小于等于当前位置参数总数（`$#`）的非负整数。默认为 `1`。

#### 行为特性

- 若 `n` 为 1：原来的 `$2` 变成 `$1`，`$3` 变成 `$2`，以此类推。原来的 `$1` 被直接丢弃。
- 位置参数的总数 `$#` 会相应减少 `n`。
- 特殊参数 `$0`（脚本名）**不受影响**。

#### 常见示例

Bash

```
# 循环处理所有的命令行传入参数
while [ "$#" -gt 0 ]; do
    case "$1" in
        -v|--verbose)
            VERBOSE=1
            shift
            ;;
        -f|--file)
            FILE_PATH="$2"
            shift 2  # 一次性消耗选项及其对应的参数值
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done
```

### 13. `times`

统计并打印当前 Shell 进程及其已结束的所有子进程所消耗的累计 CPU 用户时间（User CPU Time）与系统时间（System CPU Time）。

#### 语法

Bash

```
times
```

#### 选项与参数

- 该命令不接受任何参数。

#### 输出格式与示例

输出包含两行内容：

- 第一行：当前 Shell 进程消耗的 `User Time` 与 `System Time`。
- 第二行：由该 Shell 衍生并已终止退出的所有子进程消耗的 `User Time` 与 `System Time` 的总和。

Bash

```
$ times
0m0.02s 0m0.01s
0m0.15s 0m0.08s
```

### 14. `trap`

为操作系统内核发送给当前 Shell 的异步信号（Signals）或内部事件注册自定义捕获动作（Handler）。

#### 语法

Bash

```
trap [action] condition...
trap -p [condition...]
```

#### 选项与参数

- **`action`**：捕获触发时要执行的命令字符串。
  - 若 `action` 为 `-`（连字符），重置该信号为操作系统默认处理方式。
  - 若 `action` 为空字符串 `""`，忽略该信号。
- **`condition`**：可以是信号名称（如 `INT`, `TERM`, `HUP`）、信号编号（如 `2`, `15`），或者是特殊的 Shell 虚拟事件：
  - **`EXIT` (或 0)**：在当前 Shell 退出（不论是正常结束还是因错误中断）前触发执行。
  - **`ERR`**：在任何命令返回非零状态码时触发。

#### 常见示例

Bash

```
# 示例 1: 创建临时文件，并保证脚本无论以何种方式退出，均能优雅清理资源
TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT

# 示例 2: 捕获 Ctrl+C (SIGINT) 信号，阻止直接中断并输出提示
trap 'echo " Standard Ctrl+C is disabled in this menu."' INT
```

### 15. `unset`

从当前 Shell 执行环境中删除已定义的变量或函数，释放对应内存空间。

#### 语法

Bash

```
unset [-v|-f] name...
```

#### 选项与参数

- **`-v`**：指定仅删除**变量**（此为默认选项）。
- **`-f`**：指定仅删除**函数**。
- **`name...`**：要取消定义的变量或函数标识符名称。

#### 行为特性

- **无法删除只读项**：若尝试 `unset` 一个声明为 `readonly` 的变量或函数，命令将报错且无法删除。
- 环境变量（`PATH`, `USER` 等）一旦被 `unset`，当前 Shell 及其后续子进程将不再感知该环境变量。

#### 常见示例

Bash

```
# 1. 取消变量定义
SECRET_KEY="123456"
# 使用完毕后抹除环境变量空间
unset -v SECRET_KEY

# 2. 删除之前定义的函数
custom_helper() {
    echo "helper"
}
unset -f custom_helper
```
