## 名称 (NAME)

> *awk* — 模式扫描与处理语言（pattern scanning and processing language）

## 概要 (SYNOPSIS)

```
awk [-F sepstring] [-v assignment]... program [argument...]

awk [-F sepstring] -f progfile [-f progfile]... [-v assignment]...
     [argument...]
```

## 描述 (DESCRIPTION)

*awk* 实用程序应执行用 *awk* 编程语言编写的程序，该语言专门用于文本数据操作。一个 *awk* 程序是一系列模式（pattern）及与之对应的动作（action）。当读入的输入与某个模式匹配时，与该模式关联的动作即被执行。

输入应被解释为一系列记录（record）。默认情况下，一条记录就是一行，减去其结尾的 \<newline\>（换行符），但可以通过使用 `RS` 内置变量来改变这一点。输入的每条记录应依次与程序中的每个模式进行匹配。对于每个匹配的模式，应执行其关联的动作。

*awk* 实用程序应将每条输入记录解释为一系列字段（field），默认情况下，字段是由非 \<blank\>（空白）、非 \<newline\>（换行）字符组成的字符串。这个默认的 \<blank\> 与 \<newline\> 字段分隔符可以通过使用 `FS` 内置变量或 `-F sepstring` 选项来改变。*awk* 实用程序应以 `$1` 表示记录中的第一个字段，`$2` 表示第二个字段，依此类推。符号 `$0` 应指整个记录；对任何其他字段的赋值都会导致对 `$0` 的重新求值。对 `$0` 赋值应重置所有其他字段以及 `NF` 内置变量的值。

## 选项 (OPTIONS)

*awk* 实用程序应符合 XBD [*12.2 实用程序语法准则*](../basedefs/V1_chap12.html#tag_12_02)（Utility Syntax Guidelines）。

应支持以下选项：

`-F sepstring`

:   定义输入字段分隔符。此选项应等价于：

    ```
    -v FS=sepstring
    ```

    但如果同时使用了 `-F sepstring` 与 `-v FS=sepstring`，则由 `-F sepstring` 产生的 `FS` 赋值是按命令行顺序处理，还是在最后一个 `-v FS=sepstring` 之后处理，是未指定的（unspecified）。参见“扩展描述 (EXTENDED DESCRIPTION)”一节中对 `FS` 内置变量及其用法的描述。

`-f progfile`

:   指定包含 *awk* 程序的文件 *progfile* 的路径名。路径名 `'-'` 应表示标准输入。如果指定了该选项的多个实例，则按指定顺序将这些 *progfile* 文件的内容连接起来，作为 *awk* 程序。*awk* 程序也可以作为单个参数在命令行中指定。

`-v assignment`

:   应用（application）应确保 *assignment* 参数与 *assignment* 操作数具有相同的形式。指定的变量赋值应在执行 *awk* 程序之前发生，包括与 `BEGIN` 模式关联的动作（如果有的话）。可以多次指定此选项。

## 操作数 (OPERANDS)

应支持以下操作数：

`program`

:   如果未指定 `-f` 选项，则 *awk* 的第一个操作数应为 *awk* 程序的文本。应用应将 *program* 操作数作为单个参数提供给 *awk*。如果文本不以 \<newline\>（换行符）结尾，*awk* 应如同文本以换行符结尾一样解释该文本。

`argument`

:   以下两种类型的 *argument* 可以混合出现：

    `file`

    :   包含要读取的输入的文件路径名，该输入将与程序中的模式集合进行匹配。如果未指定 *file* 操作数或其等价物（通过修改 *awk* 变量 `ARGV` 和 `ARGC` 实现），或者某个 *file* 操作数为 `'-'`，则应使用标准输入。

    `assignment`

    :   以便携字符集（见 XBD [*6.1 便携字符集*](../basedefs/V1_chap06.html#tag_06_01)）中的 \<underscore\>（下划线）或字母字符开头，后跟便携字符集中的一串下划线、数字和字母，再后跟 `'='` 字符的操作数，应指定一个变量赋值而不是路径名。`'='` 之前的字符表示一个 *awk* 变量的名称；如果该名称是 *awk* 保留字（见“语法 (Grammar)”一节），则行为是未定义的（undefined）。`'='` 之后的字符应被解释为仿佛它们出现在 *awk* 程序中、并且前后各有一个双引号（`'"'`）字符，作为一个 `STRING` token（见“语法 (Grammar)”一节），但如果最后一个字符是未转义的 \<backslash\>（反斜杠），则应将其解释为字面的 \<backslash\>，而不是序列 `"\""` 的第一个字符。该变量应被赋予该 `STRING` token 的值，并且如果适当，应被视为数值字符串（numeric string）（见“awk 中的表达式 (Expressions in awk)”一节），该变量还应同时被赋予其数值。每个这样的变量赋值应恰好在处理下一个 *file*（如果有的话）之前发生。因此，在第一个 *file* 参数之前的赋值应在 `BEGIN` 动作（如果有的话）之后执行，而在最后一个 *file* 参数之后的赋值应在 `END` 动作（如果有的话）之前发生。如果没有 *file* 参数或其等价物（通过修改 *awk* 变量 `ARGV` 和 `ARGC` 实现），赋值应在处理标准输入之前执行。

## 标准输入 (STDIN)

仅当未指定 *file* 操作数或其等价物（通过修改 *awk* 变量 `ARGV` 和 `ARGC` 实现）时，或者某个 *file* 操作数或其等价物为 `'-'` 时，或者某个 *progfile* 选项参数为 `'-'` 时，才应使用标准输入；见“输入文件 (INPUT FILES)”一节。如果 *awk* 程序不包含动作也不包含模式，但除此之外是有效的 *awk* 程序，则不应读取标准输入和任何 *file* 操作数，且 *awk* 应以返回状态零退出。

## 输入文件 (INPUT FILES)

来自以下任何来源的、供 *awk* 程序使用的输入文件应为文本文件：

- 任何 *file* 操作数或其等价物（通过修改 *awk* 变量 `ARGV` 和 `ARGC` 实现）
- 在没有 *file* 操作数或其等价物时的标准输入
- 传给 `getline` 函数的参数

无论变量 `RS` 是否被设置为 \<newline\>（换行符）以外的值，对于这些文件，实现（implementation）应支持以指定分隔符终止、长度不超过 {LINE_MAX} 字节的记录，并且可以支持更长的记录。

如果指定了 `-f progfile`，应用应确保每个 *progfile* 选项参数所命名的文件都是文本文件，并且它们按在参数中出现的相同顺序连接起来后是一个 *awk* 程序。

## 环境变量 (ENVIRONMENT VARIABLES)

以下环境变量应影响 *awk* 的执行：

`LANG`

:   为未设置或为空的国际化变量提供默认值。（见 XBD [*8.2 国际化变量*](../basedefs/V1_chap08.html#tag_08_02)，了解用于确定 locale 类别值的国际化变量的优先级。）

`LC_ALL`

:   如果设置为非空字符串值，则覆盖所有其他国际化变量的值。

`LC_COLLATE`

:   确定正则表达式内部以及字符串值比较中范围（range）、等价类（equivalence class）和多字符整理元素（multi-character collating element）行为的 locale。

`LC_CTYPE`

:   确定将文本数据的字节序列解释为字符的 locale（例如，参数和输入文件中的单字节字符与多字节字符）、正则表达式内字符类的行为、字符作为字母的识别，以及 `toupper` 和 `tolower` 函数的大小写字符映射。

`LC_MESSAGES`

:   确定应用于影响写入标准错误的诊断消息的格式和内容的 locale。

`LC_NUMERIC`

:   确定在解释数字输入、在数值与字符串值之间执行转换以及格式化数字输出时所使用的小数点字符（radix character）。无论 locale 如何，\<period\>（句点）字符（POSIX locale 的小数点字符）都是处理 *awk* 程序（包括命令行参数中的赋值）时所识别的小数点字符。

`NLSPATH`

:   <sup>[XSI]</sup> ![][opt-start] 确定消息对象和消息目录的位置。 ![][opt-end]

`PATH`

:   确定查找由 *system*(*expr*) 执行的命令、或输入/输出管道时的搜索路径；见 XBD [*8. 环境变量*](../basedefs/V1_chap08.html#tag_08)。

此外，所有环境变量都应通过 *awk* 变量 `ENVIRON` 可见。

## 异步事件 (ASYNCHRONOUS EVENTS)

默认（Default）。

## 标准输出 (STDOUT)

输出文件的性质取决于 *awk* 程序。

## 标准错误 (STDERR)

标准错误应仅用于诊断消息。

## 输出文件 (OUTPUT FILES)

输出文件的性质取决于 *awk* 程序。
## 扩展描述 (EXTENDED DESCRIPTION)

### 总体程序结构 (Overall Program Structure)

一个 *awk* 程序由如下形式的（模式-动作）对组成：

```
pattern { action }
```

模式或动作（包括包围的花括号字符）都可以省略。

缺失的模式应匹配任何输入记录，缺失的动作应等价于：

```
{ print }
```

*awk* 程序的执行应从首先执行与所有 `BEGIN` 模式关联的动作开始，按它们在程序中出现的顺序执行。然后逐个处理每个 *file* 操作数（如果未指定文件则为标准输入），从文件中读取数据，直到看到记录分隔符（默认为 \<newline\>）。在对记录中的字段进行第一次引用之前，应根据“正则表达式 (Regular Expressions)”一节中的规则，使用读取该记录时 `FS` 的当前值将记录拆分为字段。然后按出现顺序对程序中的每个模式求值，并对每个匹配当前记录的模式执行其关联的动作。匹配模式的动响应在求值后续模式之前执行。最后，按在程序中出现的顺序执行与所有 `END` 模式关联的动作。

### awk 中的表达式 (Expressions in awk)

表达式描述用于 *模式* 和 *动作* 的计算。在下表中，有效的表达式运算按从最高优先级到最低优先级的顺序分组给出，同等优先级的运算符用水平线分组。在表达式求值中，当文法存在形式上的歧义时，较高优先级的运算符应先于较低优先级的运算符求值。在本表中，*expr*、*expr1*、*expr2* 和 *expr3* 表示任何表达式，而 lvalue 表示任何可以被赋值的实体（即在赋值运算符左侧的实体）。表达式的精确语法见“语法 (Grammar)”一节。

**表：awk 中按优先级递减的表达式 (Expressions in Decreasing Precedence in awk)**

<table border="1" cellpadding="3" align="center">
<tr valign="top">
<th align="center"><p><b>语法 (Syntax)</b></p></th>
<th align="center"><p><b>名称 (Name)</b></p></th>
<th align="center"><p><b>结果类型 (Type of Result)</b></p></th>
<th align="center"><p><b>结合性 (Associativity)</b></p></th>
</tr>
<tr valign="top">
<td align="left"><p>(<i>expr</i>)</p></td>
<td align="left"><p>分组 (Grouping)</p></td>
<td align="left"><p><i>expr</i> 的类型</p></td>
<td align="left"><p>N/A</p></td>
</tr>
<tr valign="top">
<td align="left"><p><code>&#36;</code><i>expr</i></p></td>
<td align="left"><p>字段引用 (Field reference)</p></td>
<td align="left"><p>未初始化的或字符串</p></td>
<td align="left"><p>N/A</p></td>
</tr>
<tr valign="top">
<td align="left"><p>lvalue <code>++</code>&lt;br&gt;lvalue <code>--</code></p></td>
<td align="left"><p>后置自增 (Post-increment)&lt;br&gt;后置自减 (Post-decrement)</p></td>
<td align="left"><p>数值&lt;br&gt;数值</p></td>
<td align="left"><p>N/A&lt;br&gt;N/A</p></td>
</tr>
<tr valign="top">
<td align="left"><p><code>++</code> lvalue&lt;br&gt;<code>--</code> lvalue</p></td>
<td align="left"><p>前置自增 (Pre-increment)&lt;br&gt;前置自减 (Pre-decrement)</p></td>
<td align="left"><p>数值&lt;br&gt;数值</p></td>
<td align="left"><p>N/A&lt;br&gt;N/A</p></td>
</tr>
<tr valign="top">
<td align="left"><p><i>expr</i> <code>^</code> <i>expr</i></p></td>
<td align="left"><p>幂运算 (Exponentiation)</p></td>
<td align="left"><p>数值</p></td>
<td align="left"><p>右 (Right)</p></td>
</tr>
<tr valign="top">
<td align="left"><p><code>!</code> <i>expr</i>&lt;br&gt;<code>+</code> <i>expr</i>&lt;br&gt;<code>-</code> <i>expr</i></p></td>
<td align="left"><p>逻辑非 (Logical not)&lt;br&gt;一元加 (Unary plus)&lt;br&gt;一元减 (Unary minus)</p></td>
<td align="left"><p>数值&lt;br&gt;数值&lt;br&gt;数值</p></td>
<td align="left"><p>N/A&lt;br&gt;N/A&lt;br&gt;N/A</p></td>
</tr>
<tr valign="top">
<td align="left"><p><i>expr</i> <code><i></code> </i>expr<i>&lt;br&gt;</i>expr<i> <code>/</code> </i>expr<i>&lt;br&gt;</i>expr<i> <code>%</code> </i>expr&#42;</p></td>
<td align="left"><p>乘法 (Multiplication)&lt;br&gt;除法 (Division)&lt;br&gt;取模 (Modulus)</p></td>
<td align="left"><p>数值&lt;br&gt;数值&lt;br&gt;数值</p></td>
<td align="left"><p>左 (Left)&lt;br&gt;左 (Left)&lt;br&gt;左 (Left)</p></td>
</tr>
<tr valign="top">
<td align="left"><p><i>expr</i> <code>+</code> <i>expr</i>&lt;br&gt;<i>expr</i> <code>-</code> <i>expr</i></p></td>
<td align="left"><p>加法 (Addition)&lt;br&gt;减法 (Subtraction)</p></td>
<td align="left"><p>数值&lt;br&gt;数值</p></td>
<td align="left"><p>左 (Left)&lt;br&gt;左 (Left)</p></td>
</tr>
<tr valign="top">
<td align="left"><p><i>expr</i> <i>expr</i></p></td>
<td align="left"><p>字符串连接 (String concatenation)</p></td>
<td align="left"><p>字符串</p></td>
<td align="left"><p>左 (Left)</p></td>
</tr>
<tr valign="top">
<td align="left"><p><i>expr</i> <code>&lt;</code> <i>expr</i>&lt;br&gt;<i>expr</i> <code>&lt;=</code> <i>expr</i>&lt;br&gt;<i>expr</i> <code>!=</code> <i>expr</i>&lt;br&gt;<i>expr</i> <code>==</code> <i>expr</i>&lt;br&gt;<i>expr</i> <code>&gt;</code> <i>expr</i>&lt;br&gt;<i>expr</i> <code>&gt;=</code> <i>expr</i></p></td>
<td align="left"><p>小于 (Less than)&lt;br&gt;小于或等于 (Less than or equal to)&lt;br&gt;不等于 (Not equal to)&lt;br&gt;等于 (Equal to)&lt;br&gt;大于 (Greater than)&lt;br&gt;大于或等于 (Greater than or equal to)</p></td>
<td align="left"><p>数值&lt;br&gt;数值&lt;br&gt;数值&lt;br&gt;数值&lt;br&gt;数值&lt;br&gt;数值</p></td>
<td align="left"><p>无 (None)&lt;br&gt;无 (None)&lt;br&gt;无 (None)&lt;br&gt;无 (None)&lt;br&gt;无 (None)&lt;br&gt;无 (None)</p></td>
</tr>
<tr valign="top">
<td align="left"><p><i>expr</i> <code>~</code> <i>expr</i>&lt;br&gt;<i>expr</i> <code>!~</code> <i>expr</i></p></td>
<td align="left"><p>ERE 匹配 (ERE match)&lt;br&gt;ERE 不匹配 (ERE non-match)</p></td>
<td align="left"><p>数值&lt;br&gt;数值</p></td>
<td align="left"><p>无 (None)&lt;br&gt;无 (None)</p></td>
</tr>
<tr valign="top">
<td align="left"><p><i>expr</i> <code>in</code> array&lt;br&gt;(<i>index</i>) <code>in</code> <i>array</i></p></td>
<td align="left"><p>数组成员关系 (Array membership)&lt;br&gt;多维数组成员关系 (Multi-dimension array membership)</p></td>
<td align="left"><p>数值&lt;br&gt;数值</p></td>
<td align="left"><p>左 (Left)&lt;br&gt;左 (Left)</p></td>
</tr>
<tr valign="top">
<td align="left"><p><i>expr</i> <code>&amp;&amp;</code> <i>expr</i></p></td>
<td align="left"><p>逻辑与 (Logical AND)</p></td>
<td align="left"><p>数值</p></td>
<td align="left"><p>左 (Left)</p></td>
</tr>
<tr valign="top">
<td align="left"><p><i>expr</i> <code>||</code> <i>expr</i></p></td>
<td align="left"><p>逻辑或 (Logical OR)</p></td>
<td align="left"><p>数值</p></td>
<td align="left"><p>左 (Left)</p></td>
</tr>
<tr valign="top">
<td align="left"><p><i>expr1</i> <code>?</code> <i>expr2</i> <code>:</code> <i>expr3</i></p></td>
<td align="left"><p>条件表达式 (Conditional expression)</p></td>
<td align="left"><p>所选 <i>expr2</i> 或 <i>expr3</i> 的类型</p></td>
<td align="left"><p>右 (Right)</p></td>
</tr>
<tr valign="top">
<td align="left"><p>lvalue <code>^=</code> <i>expr</i>&lt;br&gt;lvalue <code>%=</code> <i>expr</i>&lt;br&gt;lvalue <code><i>=</code> </i>expr<i>&lt;br&gt;lvalue <code>/=</code> </i>expr<i>&lt;br&gt;lvalue <code>+=</code> </i>expr<i>&lt;br&gt;lvalue <code>-=</code> </i>expr<i>&lt;br&gt;lvalue <code>=</code> </i>expr&#42;</p></td>
<td align="left"><p>幂赋值 (Exponentiation assignment)&lt;br&gt;取模赋值 (Modulus assignment)&lt;br&gt;乘法赋值 (Multiplication assignment)&lt;br&gt;除法赋值 (Division assignment)&lt;br&gt;加法赋值 (Addition assignment)&lt;br&gt;减法赋值 (Subtraction assignment)&lt;br&gt;赋值 (Assignment)</p></td>
<td align="left"><p>数值&lt;br&gt;数值&lt;br&gt;数值&lt;br&gt;数值&lt;br&gt;数值&lt;br&gt;数值&lt;br&gt;<i>expr</i> 的类型</p></td>
<td align="left"><p>右 (Right)&lt;br&gt;右 (Right)&lt;br&gt;右 (Right)&lt;br&gt;右 (Right)&lt;br&gt;右 (Right)&lt;br&gt;右 (Right)&lt;br&gt;右 (Right)</p></td>
</tr>
</table>

每个表达式应具有字符串值、数值值，或两者兼具。除针对特定上下文所作说明外，表达式的值应被隐式转换为使用它的上下文所需的类型。字符串值应通过等价于以下对 ISO C 标准所定义函数的调用来转换为数值值：

```
setlocale(LC_NUMERIC, "");
numeric_value = atof(string_value);
```

或者通过如下方式将字符串的初始部分转换为 `double` 类型表示：

> 输入字符串被分解为两部分：一个初始的、可能为空的空白字符（由 [*isspace*()](../functions/isspace.html) 指定）序列，以及一个被解释为浮点常量的主体序列（subject sequence）。

> 主体序列的预期形式是：一个可选的 `'+'` 或 `'-'` 符号，然后是一个非空的数字序列（可选地包含小数点字符），然后是一个可选的指数部分。指数部分由 `'e'` 或 `'E'` 组成，后跟一个可选的符号，再后跟一个或多个十进制数字。

> 从第一个数字或小数点字符（以先出现者为准）开始的序列被解释为 C 语言的浮点常量，但应使用小数点字符代替 \<period\>（句点），并且如果既没有指数部分也没有小数点字符出现，则假定小数点字符位于字符串中最后一个数字之后。如果主体序列以 \<hyphen-minus\>（连字符-减号）开头，则转换所得的值取反。

恰好等于某个整数值（见 [*1.1.2 源自 ISO C 标准的概念*](../utilities/V3_chap01.html#tag_18_01_02)）的数值应通过等价于调用 `sprintf` 函数（见“字符串函数 (String Functions)”一节）的方式转换为字符串，以字符串 `"%d"` 作为 *fmt* 参数，被转换的数值作为第一个也是唯一的 *expr* 参数。任何其他数值应通过等价于调用 `sprintf` 函数的方式转换为字符串，以变量 `CONVFMT` 的值作为 *fmt* 参数，被转换的数值作为第一个也是唯一的 *expr* 参数。如果 `CONVFMT` 的值不是浮点格式说明（floating-point format specification），则转换结果是未指定的（unspecified）。本卷 POSIX.1-2024 未规定数字与字符串之间的显式转换。应用可以通过给表达式加零来强制将其视为数字，也可以通过将空字符串（`""`）连接到表达式来强制将其视为字符串。

如果字符串值来自以下来源之一，则应被视为*数值字符串*（numeric string）：

1. 字段变量
2. 来自 *getline*() 函数的输入
3. `FILENAME`
4. `ARGV` 数组元素
5. `ENVIRON` 数组元素
6. 由 *split*() 函数创建的数组元素
7. 命令行变量赋值
8. 来自另一个数值字符串变量的变量赋值

并且满足与下述情况 (a) 或 (b) 之一对应的、依赖实现（implementation-dependent）的条件：

a. 在等价于以下对 ISO C 标准所定义函数的调用之后，*string_value_end* 将不同于 *string_value*，并且 *string_value_end* 中终止空字符之前的任何字符都将是 \<blank\>（空白）字符：

   ```
   char *string_value_end;
   setlocale(LC_NUMERIC, "");
   numeric_value = strtod (string_value, &string_value_end);
   ```

b. 在应用了以下所有转换之后，所得字符串在词法上将被识别为 *词法约定 (Lexical Conventions)* 一节所描述的 `NUMBER` token：

   - 丢弃所有前导和尾随的 \<blank\>（空白）字符。
   - 如果第一个非 \<blank\> 字符是 `'+'` 或 `'-'`，则丢弃它。
   - 将当前 locale 的小数点字符的每次出现改为 \<period\>（句点）。

在情况 (a) 中，*数值字符串*的数值应是对 [*strtod*()](../functions/strtod.html) 调用将返回的值。在情况 (b) 中，如果第一个非 \<blank\> 字符是 `'-'`，则*数值字符串*的数值应是所识别的 `NUMBER` token 数值的相反数；否则，*数值字符串*的数值应是所识别的 `NUMBER` token 的数值。一个字符串是否是*数值字符串*，只在本节中使用该术语的上下文中才有意义。

当表达式在布尔上下文中使用时，如果它具有数值，则零值应被视为假，任何其他值应被视为真。否则，空字符串的字符串值应被视为假，任何其他值应被视为真。布尔上下文应是以下之一：

- 条件表达式的第一个子表达式
- 由逻辑非、逻辑与或逻辑或运算的表达式
- `for` 语句的第二个表达式
- `if` 语句的表达式
- `while` 或 `do...while` 语句中 `while` 子句的表达式
- 用作模式（如“总体程序结构 (Overall Program Structure)”中所述）的表达式

所有算术都应遵循 ISO C 标准（见 [*1.1.2 源自 ISO C 标准的概念*](../utilities/V3_chap01.html#tag_18_01_02)）所规定的浮点算术语义。

表达式：

```
expr1 ^ expr2
```

的值应等价于 ISO C 标准函数调用：

```
pow(expr1, expr2)
```

所返回的值。

表达式：

```
lvalue ^= expr
```

应等价于 ISO C 标准表达式：

```
lvalue = pow(lvalue, expr)
```

但 lvalue 应只被求值一次。表达式：

```
expr1 % expr2
```

的值应等价于 ISO C 标准函数调用：

```
fmod(expr1, expr2)
```

所返回的值。

表达式：

```
lvalue %= expr
```

应等价于 ISO C 标准表达式：

```
lvalue = fmod(lvalue, expr)
```

但 lvalue 应只被求值一次。

变量和字段应由赋值语句：

```
lvalue = expression
```

设置，且 *expression* 的类型应决定结果变量的类型。赋值包括算术赋值（`"+="`、`"-="`、`"*="`、`"/="`、`"%="`、`"^="`、`"++"`、`"--"`），所有这些赋值都应产生数值结果。赋值的左侧以及自增和自减运算符的目标可以是变量、带下标的数组或字段选择器之一。

*awk* 语言提供用于存储数字或字符串的数组。数组无需声明。它们最初应为空，其大小应动态变化。下标（subcripts）或元素标识符是字符串，提供了一种关联数组（associative array）能力。数组名后跟方括号内的下标可以用作 lvalue，从而作为表达式使用，如文法所述；见“语法 (Grammar)”一节。不带下标的数组名只能在以下上下文中使用：

- 函数定义或函数调用中的参数
- 按文法（见“语法 (Grammar)”一节）规定，在任何使用关键字 `in` 之后紧跟的 `NAME` token；如果在此上下文中使用的名称不是数组名，则行为是未定义的（undefined）
- 按文法（见“语法 (Grammar)”一节）规定，在关键字 `delete` 之后、不带下标地紧跟的 `NAME` token；如果在此上下文中使用的名称不是数组名，则行为是未定义的（undefined）

有效的数组*下标*应由一个或多个以 \<comma\>（逗号）分隔的表达式组成，类似于某些编程语言中多维数组的索引方式。由于 *awk* 数组实际上是一维的，这样的 \<comma\> 分隔列表应通过连接各个表达式的字符串值转换为单个字符串，每个表达式之间用 `SUBSEP` 变量的值分隔。因此，以下两个下标操作应是等价的：

```
var[expr1, expr2, ... exprn]
var[expr1 SUBSEP expr2 SUBSEP ... SUBSEP exprn]
```

应用应确保与 `in` 运算符一起使用的多维*下标*要加括号。`in` 运算符测试特定数组元素是否存在，不应导致该元素存在。对不存在的数组元素的任何其他引用都应自动创建它。

比较（使用 `'<'`、`"<="`、`"!="`、`"=="`、`'>'` 和 `">="` 运算符）应按数值进行：

- 如果两个操作数都是数值，
- 如果一个是数值，另一个具有作为数值字符串的字符串值，
- 如果两者都具有作为数值字符串的字符串值，或
- 如果一个是数值，另一个具有未初始化的值。

否则，操作数应按需要转换为字符串，并按如下方式进行字符串比较：

- 对于 `"!="` 和 `"=="` 运算符，应比较字符串以检查它们是否相同（而不是检查它们是否整理相等）。
- 对于其他运算符，应使用 locale 特定的整理序列（collation sequence）比较字符串。

比较表达式的值在关系为真时应为 1，关系为假时应为 0。

### 变量与特殊变量 (Variables and Special Variables)

可以通过引用变量来在 *awk* 程序中使用变量。除函数参数（见“用户定义函数 (User-Defined Functions)”一节）外，变量不显式声明。函数参数名应是函数的局部变量；所有其他变量名应是全局的。同一名称不应既用作函数参数名，又用作函数名或特殊的 *awk* 变量名。同一名称不应既用作具有全局作用域的变量名，又用作函数名。同一名称不应在同一作用域内既用作标量变量又用作数组。未初始化的变量（包括标量变量、数组元素和字段变量）应具有未初始化的值。未初始化的值应同时具有零的数值和空字符串的字符串值。对具有未初始化值的变量求值为字符串或数值，应由使用它们的上下文决定。

字段变量应由 `'$'` 后跟一个数字或数值表达式来指定。字段编号*表达式*求值为非负整数以外的任何值的效果是未指定的（unspecified）；在此上下文中，未初始化的变量或字符串值不必转换为数值。可以通过给新字段变量赋值来创建它们。对不存在的字段（即 `$NF` 之后的字段）的引用应求值为未初始化的值。此类引用不应创建新字段。但是，对不存在的字段赋值（例如 `$(NF+2)=5`）应增大 `NF` 的值；创建任何介于中间的字段，其值为未初始化的值；并导致重新计算 `$0` 的值，字段之间用 `OFS` 的值分隔。每个字段变量在创建时应具有字符串值或未初始化的值。当使用 `FS` 从 `$0` 创建字段且变量不包含任何字符时，字段变量应具有未初始化的值。如果适当，字段变量应被视为数值字符串（见“awk 中的表达式 (Expressions in awk)”一节）。

实现应支持以下由 *awk* 设置的其他特殊变量：

`ARGC`

:   确定为 `ARGV` 所描述的迭代何时停止的数字。当 *awk* 程序启动时，`ARGC` 应被初始化为 `ARGV` 数组中元素的个数。`ARGC` 可以由 *awk* 程序和赋值操作数更新。如果 `ARGC` 被设置为小于 1 的值，行为是未指定的（unspecified）。是否可以使用 `-v` 选项修改 `ARGC` 是未指定的。

`ARGV`

:   一个数组，最初在 `ARGV[0]` 中包含用于调用 *awk* 的命令名（见 [*2.9.1 简单命令*](../utilities/V3_chap02.html#tag_19_09_01)），在 `ARGV[1]` 到 `ARGV[ARGC-1]` 中包含命令行参数（如果有的话），不包括选项和 *program* 操作数。`ARGV` 中的元素可以被赋予新值或删除，也可以添加新元素。注意，不能使用 *assignment* 操作数或 `-v` 选项修改 `ARGV`，因为在 `'='` 之前带有 `'['` 的操作数被视为 *file* 操作数而不是 *assignment* 操作数，并且要求应用确保 `-v` 选项参数与 *assignment* 操作数具有相同的形式。（见“选项 (OPTIONS)”和“操作数 (OPERANDS)”一节。）

    在处理完 `BEGIN` 动作（如果有的话）之后，*awk* 开始遍历 `ARGV` 的元素，将它们当作 *argument* 操作数处理。其行为应如同实现维护一个内部计数器，该计数器初始化为 1，并在每次迭代结束时递增 1。对于每次迭代，应发生以下情况：

    - 如果内部计数器大于或等于 `ARGC` 的当前值，且尚未处理任何 *file* 操作数，则 *awk* 应将 `FILENAME` 设置为 `'-'`，并像处理 file 操作数一样处理标准输入。内部计数器不应在此次迭代结束时递增。
    - 否则，如果内部计数器大于或等于 `ARGC` 的当前值，迭代应停止，并开始处理 `END` 动作（如果有的话）。索引值大于或等于 `ARGC` 的任何 `ARGV` 元素不应作为 *argument* 操作数处理。
    - 否则，如果元素 `ARGV[内部计数器值]` 不存在，则该元素是否被创建是未指定的。不应采取其他操作。
    - 否则，如果 `ARGV[内部计数器值]` 是空字符串，则不应采取任何操作。
    - 否则，如果 `ARGV[内部计数器值]` 符合 *assignment* 操作数的格式（见“操作数 (OPERANDS)”一节），*awk* 应处理该赋值。
    - 否则，`ARGV[内部计数器值]` 应被视为 *file* 操作数，`FILENAME` 应被设置为该值，并应处理命名的文件（如果该值为 `'-'` 则为标准输入）作为输入文件。

    由于只处理非空元素，将 `ARGV` 的某个元素设置为空字符串或删除它，意味着它不应被视为 *argument* 操作数。

`CONVFMT`

:   用于将数字转换为字符串的 `printf` 格式（输出语句除外，输出语句使用 `OFMT`）；默认为 `"%.6g"`。

`ENVIRON`

:   表示环境值的数组，如 POSIX.1-2024《系统接口》卷中定义的 *exec* 函数所述。数组的下标应是由环境变量名称组成的字符串，每个数组元素的值应是由该变量的值组成的字符串。如果适当，环境变量应被视为数值字符串（见“awk 中的表达式 (Expressions in awk)”一节）；该数组元素还应具有其数值。

    在所有 *awk* 的行为受环境变量影响的场合（包括 *awk* 通过 `system` 函数或通过 `print` 语句、`printf` 语句或 `getline` 函数的管道重定向执行的任何命令的环境），所使用的环境应是 *awk* 开始执行时的环境；对 `ENVIRON` 的任何修改是否影响此环境是实现定义的（implementation-defined）。

`FILENAME`

:   用于打开当前输入文件的路径名，如果文件是标准输入则为 `'-'`。在 `BEGIN` 动作内部，`FILENAME` 应是未设置的。在 `END` 动作内部，其值应是最后处理的输入文件的名称。如果应用更改 `FILENAME` 的值，结果是未指定的（unspecified）。

`FNR`

:   当前记录在当前文件中的序号。在 `BEGIN` 动作内部，其值应为零。在 `END` 动作内部，其值应是在最后处理的文件中处理的最后一条记录的编号。

`FS`

:   输入字段分隔符正则表达式；默认为 \<space\>（空格）。

`NF`

:   当前记录中的字段数。在 `BEGIN` 动作内部，除非先前执行了不带 *var* 参数的 `getline` 函数，否则 `NF` 的使用是未定义的（undefined）。在 `END` 动作内部，除非在进入 `END` 动作之前执行了后续的、带重定向的不带 *var* 参数的 `getline` 函数，否则 `NF` 应保留读取的最后一条记录所具有的值。

`NR`

:   从输入开始算起的当前记录的序号。在 `BEGIN` 动作内部，其值应为零。在 `END` 动作内部，其值应是最后处理的记录的编号。被 `nextfile` 语句跳过的记录不应包括在内。

`OFMT`

:   在输出语句（见“输出语句 (Output Statements)”一节）中用于将数字转换为字符串的 `printf` 格式；默认为 `"%.6g"`。如果 `OFMT` 的值不是浮点格式说明，转换结果是未指定的（unspecified）。

`OFS`

:   `print` 语句的输出字段分隔符；默认为 \<space\>（空格）。

`ORS`

:   `print` 语句的输出记录分隔符；默认为 \<newline\>（换行符）。

`RLENGTH`

:   由 `match` 函数匹配的字符串的长度。

`RS`

:   `RS` 字符串值的第一个字符应是输入记录分隔符；默认为 \<newline\>（换行符）。如果 `RS` 包含多个字符，结果是未指定的（unspecified）。如果 `RS` 为空，则记录由 \<newline\> 加一个或多个空行组成的序列分隔，前导或尾随的空行不应在输入的开头或结尾产生空记录，并且无论 `FS` 的值是什么，\<newline\> 应始终是字段分隔符。

`RSTART`

:   由 `match` 函数匹配的字符串的起始位置，从 1 开始编号。这应始终等价于 `match` 函数的返回值。

`SUBSEP`

:   多维数组的下标分隔符字符串；默认值是实现定义的（implementation-defined）。
### 正则表达式 (Regular Expressions)

*awk* 实用程序应使用扩展正则表达式记号（见 XBD [*9.4 扩展正则表达式*](../basedefs/V1_chap09.html#tag_09_04)），但它应允许在 ERE 中使用 C 语言约定来转义特殊字符，如 XBD [*5. 文件格式记号*](../basedefs/V1_chap05.html#tag_05) 中的表针对 `'\\'`、`'\a'`、`'\b'`、`'\f'`、`'\n'`、`'\r'`、`'\t'`、`'\v'` 所规定，以及下表中针对其他序列所规定；这些转义序列应在括号表达式（bracket expression）内外都被识别。注意，记录不需要由 \<newline\>（换行符）字符分隔，字符串常量可以包含 \<newline\> 字符，因此即使是 `"\n"` 序列在 *awk* ERE 中也是有效的。在词法 token `ERE` 内使用 \<slash\>（斜杠）字符（除作为两个分隔符之一外）<table border="1" cellpadding="3" align="center">
<tr valign="top">
<th align="center"><p><b>转义序列 (Escape Sequence)</b></p></th>
<th align="center"><p><b>描述 (Description)</b></p></th>
<th align="center"><p><b>含义 (Meaning)</b></p></th>
</tr>
<tr valign="top"><td align="left"><p>&amp;#92;&amp;#34;</p></td><td align="left"><p>&amp;#92;&amp;lt;backslash&amp;#92;&amp;gt; &amp;#92;&amp;lt;quotation-mark&amp;#92;&amp;gt;（反斜杠 双引号）</p></td><td align="left"><p>在词法 token &amp;#96;STRING&amp;#96; 中为 &amp;#92;&amp;lt;quotation-mark&amp;#92;&amp;gt;（双引号）字符。否则未定义。</p></td></tr>
<tr valign="top"><td align="left"><p>&amp;#92;/</p></td><td align="left"><p>&amp;#92;&amp;lt;backslash&amp;#92;&amp;gt; &amp;#92;&amp;lt;slash&amp;#92;&amp;gt;（反斜杠 斜杠）</p></td><td align="left"><p>在词法 token &amp;#96;ERE&amp;#96; 中为 &amp;#92;&amp;lt;slash&amp;#92;&amp;gt;（斜杠）字符。否则未定义。</p></td></tr>
<tr valign="top"><td align="left"><p>&amp;#92;ddd</p></td><td align="left"><p>一个 &amp;#92;&amp;lt;backslash&amp;#92;&amp;gt; 字符后跟一到三个八进制数字</p></td><td align="left"><p>编码为该八进制值的字符。</p></td></tr>
<tr valign="top"><td align="left"><p>&amp;#92;., &amp;#92;&amp;#91;, &amp;#92;(, &amp;#92;&amp;#42;, &amp;#92;+, &amp;#92;?, &amp;#92;{, &amp;#92;|, &amp;#92;^, &amp;#92;&amp;#36;</p></td><td align="left"><p>一个 &amp;#92;&amp;lt;backslash&amp;#92;&amp;gt; 字符后跟一个在 ERE 中具有特殊含义的字符（见 XBD 9.4 扩展正则表达式），&amp;#92;&amp;lt;backslash&amp;#92;&amp;gt; 本身除外。</p></td><td align="left"><p>在词法 token &amp;#96;ERE&amp;#96; 中、不在括号表达式内部时，该序列应表示其自身。否则未定义。</p></td></tr>
<tr valign="top"><td align="left"><p>&amp;#92;&amp;#92;</p></td><td align="left"><p>两个 &amp;#92;&amp;lt;backslash&amp;#92;&amp;gt; 字符。</p></td><td align="left"><p>在词法 token &amp;#96;ERE&amp;#96; 中，该序列应表示其自身。在词法 token &amp;#96;STRING&amp;#96; 中，它应表示单个 &amp;#92;&amp;lt;backslash&amp;#92;&amp;gt;。</p></td></tr>
<tr valign="top"><td align="left"><p>&amp;#92;c</p></td><td align="left"><p>一个 &amp;#92;&amp;lt;backslash&amp;#92;&amp;gt; 字符后跟任意其他字符。</p></td><td align="left"><p>未定义（undefined）。</p></td></tr>
</table>

可以使用两个正则表达式匹配运算符 `'~'` 和 `"!~"` 之一，将正则表达式与特定字段或字符串进行匹配。这些运算符应将其右操作数解释为正则表达式，将其左操作数解释为字符串。如果正则表达式匹配该字符串，`'~'` 表达式应求值为 1，`"!~"` 表达式应求值为 0。（正则表达式匹配操作如 XBD [*9.1 正则表达式定义*](../basedefs/V1_chap09.html#tag_09_01) 中术语 matched 所定义，除非用 \<circumflex\>（脱字符）或 \<dollar-sign\>（美元符号）特殊字符限定正则表达式，否则匹配发生在字符串的任何部分。）如果正则表达式不匹配该字符串，`'~'` 表达式应求值为 0，`"!~"` 表达式应求值为 1。如果右操作数是词法 token `ERE` 以外的任何表达式，则表达式的字符串值应被解释为扩展正则表达式，包括上述转义约定。注意，这些转义约定在确定字符串字面量（词法 token `STRING`）的值时也应被应用，因此当字符串字面量在此上下文中使用时，应被第二次应用。

当 `ERE` token 作为表达式出现在除 `'~'` 或 `"!~"` 运算符右侧或下述内置函数参数以外的任何上下文中时，所得表达式的值应等价于：

```
$0 ~ /ere/
```

传给 `gsub`、`match`、`sub` 函数的 *ere* 参数，以及传给 `split` 函数的 *fs* 参数（见“字符串函数 (String Functions)”一节）应被解释为扩展正则表达式。这些可以是 `ERE` token 或任意表达式，并且应以与 `'~'` 或 `"!~"` 运算符右侧相同的方式解释。

可以通过将包含该表达式的字符串赋给内置变量 `FS`（直接或作为使用 `-F sepstring` 选项的结果）来使用扩展正则表达式分隔字段。`FS` 变量的默认值应是单个 \<space\>（空格）。以下描述 `FS` 的行为：

1. 如果 `FS` 是空字符串，行为是未指定的（unspecified）。
2. 如果 `FS` 是单个字符：
   a. 如果 `FS` 是 \<space\>（空格），跳过前导和尾随的 \<blank\>（空白）和 \<newline\>（换行）字符；字段应由一个或多个 \<blank\> 或 \<newline\> 字符组成的集合分隔。
   b. 否则，如果 `FS` 是任何其他字符 *c*，字段应由 *c* 的每次单独出现分隔。
3. 否则，`FS` 的字符串值应被视为扩展正则表达式。匹配该扩展正则表达式的一个或多个字符序列的每次出现都应分隔字段。

当对输入记录执行 ERE 匹配时；即，匹配针对 `$0`，且 `$0` 的当前值来自处理输入记录，则记录分隔符字符（变量 `RS` 值的第一个字符，默认为 \<newline\>（换行符））不能嵌入表达式中，并且任何表达式都不应匹配记录分隔符字符。如果记录分隔符不是 \<newline\>，则嵌入表达式中的 \<newline\> 字符可以被匹配。当 ERE 匹配不是针对输入记录执行时，它应基于文本字符串；任何字符（包括 \<newline\> 和记录分隔符）都可以嵌入模式中，适当的模式应匹配任何字符。但是，在所有 *awk* ERE 匹配中，在模式、输入记录或文本字符串中使用一个或多个 NUL 字符会产生未定义（undefined）的结果。

### 模式 (Patterns)

*模式*是任何有效的*表达式*、由逗号分隔的两个表达式指定的范围，或者是两个特殊模式 `BEGIN` 或 `END` 之一。

### 特殊模式 (Special Patterns)

*awk* 实用程序应识别两个特殊模式 `BEGIN` 和 `END`。每个 `BEGIN` 模式应被匹配一次，其关联的动作应在读取第一条输入记录之前执行——除非可能通过在先前的 `BEGIN` 动作中使用 `getline` 函数（见“输入/输出与通用函数 (Input/Output and General Functions)”一节）——并且应在命令行赋值完成之前执行。每个 `END` 模式应被匹配一次，其关联的动作应在读取最后一条输入记录之后执行，或者在没有进一步输入文件可在 `nextfile` 语句之后处理时执行。这两个模式应具有关联的动作。

`BEGIN` 和 `END` 不应与其他模式组合。允许多个 `BEGIN` 和 `END` 模式。与 `BEGIN` 模式关联的动作应按程序中指定的顺序执行，`END` 动作也是如此。`END` 模式可以出现在程序中的 `BEGIN` 模式之前。

如果 *awk* 程序只由模式为 `BEGIN` 的动作组成，且 `BEGIN` 动作不包含 `getline` 函数，则 *awk* 应在执行最后一个 `BEGIN` 动作中的最后一条语句时退出，而不读取其输入。如果 *awk* 程序只由模式为 `END` 的动作组成，或只由模式为 `BEGIN` 和 `END` 的动作组成，则应在执行 `END` 动作中的语句之前读取输入。

### 表达式模式 (Expression Patterns)

表达式模式应被求值，如同它是布尔上下文中的表达式。如果结果为真，则该模式应被视为匹配，并应执行关联的动作（如果有的话）。如果结果为假，则不应执行该动作。

### 模式范围 (Pattern Ranges)

模式范围由逗号分隔的两个表达式组成；在这种情况下，应对第一个表达式匹配与第二个表达式随后匹配之间的所有记录（含两端）执行该动作。此时，模式范围可以从匹配范围结束之后的后续输入记录开始重复。

### 动作 (Actions)

动作是如“语法 (Grammar)”一节中文法所示的一系列语句。任何单个语句都可以替换为用花括号括起来的语句列表。应用应确保语句列表中的语句用 \<newline\>（换行）或 \<semicolon\>（分号）字符分隔。语句列表中的语句应按出现顺序依次执行。

作为 `if` 语句中条件的*表达式*应被求值，如果它非零或非空，则应执行其后的语句；否则，如果存在 `else`，则应执行 `else` 之后的语句。

`if`、`while`、`do...while`、`for`、`break` 和 `continue` 语句基于 ISO C 标准（见 [*1.1.2 源自 ISO C 标准的概念*](../utilities/V3_chap01.html#tag_18_01_02)），但布尔表达式应按“awk 中的表达式 (Expressions in awk)”一节所述处理，并且以下情况除外：

```
for (variable in array)
```

它应以未指定的（unspecified）顺序迭代，将 *array* 的每个*下标*赋给 *variable*。在此类 `for` 循环内向 *array* 添加新元素的结果是未定义的（undefined）。如果 `break` 或 `continue` 语句出现在循环之外，行为是未定义的。

`delete` 语句应删除指定的单个数组元素，或者，如果未指定元素，则删除所有数组元素。因此，以下代码：

```
for (index in array)
    delete array[index]
```

等价于：

```
delete array
```

两者都删除数组的所有元素。

`next` 语句应导致放弃对当前输入记录的所有进一步处理。如果 `next` 语句出现在 `BEGIN` 或 `END` 动作中或被其调用，行为是未定义的（undefined）。

`nextfile` 语句应导致放弃对当前输入文件的所有进一步处理。如果 `nextfile` 语句出现在 `BEGIN` 或 `END` 动作中、或在用户定义函数中被调用，行为是未定义的（undefined）。

`exit` 语句应按在程序源中出现的顺序调用所有 `END` 动作，然后终止程序，而不读取更多输入。`END` 动作内部的 `exit` 语句应终止程序，而不进一步执行 `END` 动作。如果在 `exit` 语句中指定了表达式，其数值应为 *awk* 的退出状态，除非随后遇到错误或执行了带表达式的后续 `exit` 语句。

### 输出语句 (Output Statements)

`print` 和 `printf` 语句默认都应写入标准输出。如果提供了 *output_redirection*，输出应写入其指定的位置，如下所示：

```
> expression
>> expression
| expression
```

在所有情况下，*expression* 应被求值以产生一个字符串，该字符串用作要写入的路径名（对于 `'>'` 或 `">>"`）或要执行的命令（对于 `'|'`）。使用前两种形式时，如果该名称的文件当前未打开，则应将其打开，必要时创建它，并且使用第一种形式时截断该文件。然后输出应被追加到该文件。只要文件保持打开，后续调用中 *expression* 求值为相同字符串值的，应简单地将输出追加到该文件。文件保持打开，直到调用 `close` 函数（见“输入/输出与通用函数 (Input/Output and General Functions)”一节），且其表达式求值为相同的字符串值。

第三种形式应将输出写入管道到命令输入的流。如果当前没有以 *expression* 的值作为其命令名打开的流，则应创建该流。所创建的流应等价于调用 POSIX.1-2024《系统接口》卷中定义的 [*popen*()](../functions/popen.html) 函数所创建的流，以 *expression* 的值作为 *command* 参数，以值 *w* 作为 *mode* 参数。只要流保持打开，后续调用中 *expression* 求值为相同字符串值的，应写入现有流。流应保持打开，直到调用 `close` 函数（见“输入/输出与通用函数 (Input/Output and General Functions)”一节），且其表达式求值为相同的字符串值。此时，流应如同调用 POSIX.1-2024《系统接口》卷中定义的 [*pclose*()](../functions/pclose.html) 函数一样关闭。

如“语法 (Grammar)”一节中的文法详细所述，这些输出语句应接受以 \<comma\>（逗号）分隔的*表达式*列表，文法中以非终结符号 `expr_list`、`print_expr_list` 或 `print_expr_list_opt` 引用。此列表在此称为*表达式列表*，每个成员称为一个*表达式参数*。

`print` 语句应将其每个表达式参数的值写入指定的输出流，用当前的输出字段分隔符（见上面的变量 `OFS`）分隔，并以输出记录分隔符（见上面的变量 `ORS`）终止。所有表达式参数应作为字符串处理，必要时进行转换；此转换应按“awk 中的表达式 (Expressions in awk)”一节所述进行，但应使用 `OFMT` 中的 `printf` 格式而不是 `CONVFMT` 中的值。空的表达式列表应代表整个输入记录（`$0`）。

`printf` 语句应基于与本卷 POSIX.1-2024 中用于描述文件格式的文件格式记号（File Format Notation）相似的记号产生输出（见 XBD [*5. 文件格式记号*](../basedefs/V1_chap05.html#tag_05)）。输出应按以下规定产生：第一个*表达式参数*作为字符串*格式*，后续*表达式参数*作为字符串 *arg1* 到 *argn*（含），但有以下例外：

1. *格式*应是实际的字符串，而不是图形表示。因此，它不能包含空的字符位置。*格式*字符串中的 \<space\>（空格），在转换说明的*标志*（flag）以外的任何上下文中，应被视为复制到输出的普通字符。
2. 如果字符集包含 `'Δ'` 字符且该字符出现在*格式*字符串中，它应被视为复制到输出的普通字符。
3. 以 \<backslash\>（反斜杠）字符开头的*转义序列*应被视为复制到输出的普通字符序列。注意，当这些序列出现在字面字符串中时，*awk* 应对其进行词法解释，但 `printf` 语句不应特殊处理它们。
4. 字段宽度（field width）或精度（precision）可以指定为 `'*'` 字符而不是数字字符串。在这种情况下，应获取表达式列表中的下一个参数，并将其数值作为字段宽度或精度。
5. 实现不应在来自 `d` 或 `u` 转换说明符字符的输出前后加上*格式*字符串未指定的 \<blank\>（空白）字符。
6. 实现不应在来自 `o` 转换说明符字符的输出前面加上*格式*字符串未指定的前导零。
7. 对于 `c` 转换说明符字符：如果参数具有数值，应输出编码为该值的字符。如果该值为零或不是字符集中任何字符的编码，行为是未定义的（undefined）。如果参数没有数值，应输出字符串值的第一个字符；如果字符串不包含任何字符，行为是未定义的。
8. 对于每个消耗参数的转换说明，应求值下一个表达式参数。除 `c` 转换说明符字符外，该值应按“awk 中的表达式 (Expressions in awk)”一节规定的规则转换为转换说明所需的适当类型。
9. 如果表达式参数不足以满足*格式*字符串中的所有转换说明，行为是未定义的。
10. 如果*格式*字符串中的任何字符序列以 `'%'` 字符开头，但不构成有效的转换说明，行为是未指定的（unspecified）。

`print` 和 `printf` 都可以输出至少 {LINE_MAX} 字节。

### 函数 (Functions)

*awk* 语言具有各种内置函数：算术、字符串、输入/输出和通用函数。

函数参数（如果有的话）可以是标量或数组；如果数组名作为函数用作标量的参数传递，或者标量表达式作为函数用作数组的参数传递，行为是未定义的（undefined）。函数参数如果是标量应按值传递，如果是数组名应按引用传递。

### 算术函数 (Arithmetic Functions)

除 `int` 外，算术函数应基于 ISO C 标准（见 [*1.1.2 源自 ISO C 标准的概念*](../utilities/V3_chap01.html#tag_18_01_02)）。在 ISO C 标准规定应返回错误或行为未定义（undefined）的情况下，行为是未定义的。虽然文法（见“语法 (Grammar)”一节）允许内置函数不带参数或括号出现，但除非在下列列表中将参数或括号指示为可选的（通过将其显示在 `"[]"` 括号内），否则此类使用是未定义的。

`atan2(y, x)`

:   返回 *y*/*x* 的反正切，以弧度为单位，范围为 [-ℼ,ℼ]。

`cos(x)`

:   返回 *x* 的余弦，其中 *x* 以弧度为单位。

`sin(x)`

:   返回 *x* 的正弦，其中 *x* 以弧度为单位。

`exp(x)`

:   返回 *x* 的指数函数值。

`log(x)`

:   返回 *x* 的自然对数。

`sqrt(x)`

:   返回 *x* 的平方根。

`int(x)`

:   返回截断为整数的参数。当 *x*>0 时截断应向 0 进行。

`rand()`

:   返回浮点伪随机数 *n*，使得 0<=*n*<1。

`srand([expr])`

:   将 `rand` 的种子值设置为 *expr*，如果省略 *expr* 则使用自 Epoch 以来的秒数。应返回先前的种子值。如果 *expr* 不是整数表达式，或者 *expr* 的值不在 0 到 2^31-1 (2147483647)（含）范围内，行为是未指定的（unspecified）。如果在未先调用 `srand` 的情况下调用 `rand`，初始种子值是未指定的。`srand` 函数使用该参数作为新伪随机数序列的种子，该序列由后续对 `rand` 的调用返回。如果随后使用相同的种子值调用 `srand`，伪随机数序列应重复。

### 字符串函数 (String Functions)

应支持下列列表中的字符串函数。虽然文法（见“语法 (Grammar)”一节）允许内置函数不带参数或括号出现，但除非在下列列表中将参数或括号指示为可选的（通过将其显示在 `"[]"` 括号内），否则此类使用是未定义的。

`gsub(ere, repl [, in])`

:   行为类似于 `sub`（见下文），但它应替换 `$0` 中或（当指定时）*in* 参数中正则表达式的所有出现（类似于 [*ed*](../utilities/ed.html) 实用程序的全局替换）。

`index(s, t)`

:   返回字符串 *t* 在字符串 *s* 中首次出现的位置（以字符计，从 1 开始编号），如果根本不出现则返回零。

`length[( [arg] )]`

:   如果 *arg* 是数组，返回数组中元素的个数；否则，返回将 *arg* 作为字符串的长度（以字符计），如果没有参数则返回整个记录 `$0` 的长度。

`match(s, ere)`

:   返回扩展正则表达式 *ere* 在字符串 *s* 中出现的位置（以字符计，从 1 开始编号），如果根本不出现则返回零。`RSTART` 应被设置为起始位置（与返回值相同），如果未找到匹配则为零；`RLENGTH` 应被设置为匹配字符串的长度，如果未找到匹配则为 -1。

`split(s, a [, fs ])`

:   将字符串 *s* 拆分为数组元素 `a[1]`、`a[2]`、...、`a[n]`，并返回 *n*。在执行拆分之前，应删除数组的所有元素。应使用 ERE *fs* 进行分隔，如果未给出 *fs* 则使用字段分隔符 `FS`。每个数组元素在创建时应具有字符串值，并且如果适当，该数组元素应被视为数值字符串（见“awk 中的表达式 (Expressions in awk)”一节）。空字符串作为 *fs* 的值的效应是未指定的（unspecified）。

`sprintf(fmt, expr, expr, ...)`

:   根据 *fmt* 给出的 `printf` 格式格式化这些表达式，并返回结果字符串。

`sub(ere, repl [, in ])`

:   用字符串 *repl* 替换字符串 *in* 中扩展正则表达式 `ERE` 的第一个实例，并返回替换次数。出现在字符串 *repl* 中的 \<ampersand\>（& 符号）（`'&'`）应被替换为 *in* 中匹配该 ERE 的字符串。前面带 \<backslash\>（反斜杠）的 \<ampersand\> 应被解释为字面的 \<ampersand\> 字符。两个连续 \<backslash\> 字符的出现应被解释为单个字面 \<backslash\> 字符。任何其他 \<backslash\> 的出现（例如，在任何其他字符之前）应被视为字面 \<backslash\> 字符。注意，如果 *repl* 是字符串字面量（词法 token `STRING`；见“语法 (Grammar)”一节），则任何 \<ampersand\> 字符的处理都发生在任何词法处理（包括任何词法 \<backslash\>-转义序列处理）之后。如果指定了 *in* 且它不是 lvalue（见“awk 中的表达式 (Expressions in awk)”一节），行为是未定义的（undefined）。如果省略 *in*，*awk* 应使用当前记录（`$0`）代替。

`substr(s, m [, n ])`

:   返回 *s* 中从位置 *m* 开始（从 1 编号）的至多 *n* 个字符的子串。如果省略 *n*，或者 *n* 指定的字符数多于字符串中剩余的字符数，子串的长度应受字符串 *s* 长度的限制。

`tolower(s)`

:   返回基于字符串 *s* 的字符串。*s* 中每个由当前 locale 的 `LC_CTYPE` 类别指定具有 `tolower` 映射的大写字母字符，都应在返回的字符串中被映射指定的相应小写字母替换。*s* 中的其他字符在返回的字符串中应保持不变。

`toupper(s)`

:   返回基于字符串 *s* 的字符串。*s* 中每个由当前 locale 的 `LC_CTYPE` 类别指定具有 `toupper` 映射的小写字母字符，都应在返回的字符串中被映射指定的相应大写字母替换。*s* 中的其他字符在返回的字符串中保持不变。

所有上述将 `ERE` 作为参数的函数，都期望一个模式或字符串值的表达式，该表达式是“正则表达式 (Regular Expressions)”一节所定义的正则表达式。

### 输入/输出与通用函数 (Input/Output and General Functions)

输入/输出和通用函数是：

`close(expression)`

:   关闭由 `print` 或 `printf` 语句、或具有相同字符串值 *expression* 的 `getline` 调用打开的文件或管道。打开的 *expression* 参数数量的限制是实现定义的（implementation-defined）。如果关闭成功，函数应返回零；否则，应返回非零。

`fflush([expression])`

:   将任何未写入的数据写入由 `print` 或 `printf` 语句以相同字符串值 *expression* 打开的文件或管道流。如果没有参数，或者 *expression* 求值为空字符串，则写入所有此类打开的文件和管道流以及标准输出的所有此类数据。

    如果 `fflush` 成功，应返回 0；否则，应返回非零。

`expression | getline [var]`

:   从命令输出管道来的流中读取一条输入记录。如果当前没有以 *expression* 的值作为其命令名打开的流，则应创建该流。所创建的流应等价于调用 [*popen*()](../functions/popen.html) 函数所创建的流，以 *expression* 的值作为 *command* 参数，以值 *r* 作为 *mode* 参数。只要流保持打开，后续调用中 *expression* 求值为相同字符串值的，应读取流中的后续记录。流应保持打开，直到调用 `close` 函数且其表达式求值为相同的字符串值。此时，流应如同调用 [*pclose*()](../functions/pclose.html) 函数一样关闭。如果省略 *var*，应设置 `$0` 和 `NF`；否则，应设置 *var*，并且如果适当，它应被视为数值字符串（见“awk 中的表达式 (Expressions in awk)”一节）。

    `getline` 运算符在 `'|'` 左侧（直到包含 `getline` 的表达式的开头）存在未加括号的运算符（包括连接）时，会形成歧义结构。在 `'$'` 运算符的上下文中，`'|'` 应表现得如同它的优先级低于 `'$'`。其他运算符的求值结果是未指定的（unspecified），符合标准的应用应适当地将所有此类用法加括号。

`getline`

:   将 `$0` 设置为当前输入文件中的下一条输入记录。此形式的 `getline` 应设置 `NF`、`NR` 和 `FNR` 变量。

`getline var`

:   将变量 *var* 设置为当前输入文件中的下一条输入记录，并且如果适当，*var* 应被视为数值字符串（见“awk 中的表达式 (Expressions in awk)”一节）。此形式的 `getline` 应设置 `FNR` 和 `NR` 变量。

`getline [var] < expression`

:   从命名文件读取下一条输入记录。*expression* 应被求值以产生用作路径名的字符串。如果该名称的文件当前未打开，则应将其打开。只要流保持打开，后续调用中 *expression* 求值为相同字符串值的，应读取文件中的后续记录。文件应保持打开，直到调用 `close` 函数且其表达式求值为相同的字符串值。如果省略 *var*，应设置 `$0` 和 `NF`；否则，应设置 *var*，并且如果适当，它应被视为数值字符串（见“awk 中的表达式 (Expressions in awk)”一节）。

    `getline` 运算符在 `'<'` 右侧（直到包含 `getline` 的表达式的结尾）存在未加括号的二元运算符（包括连接）时，会形成歧义结构。此类结构的求值结果是未指定的（unspecified），符合标准的应用应适当地将所有此类用法加括号。

`system(expression)`

:   以与 POSIX.1-2024《系统接口》卷中定义的 [*system*()](../functions/system.html) 函数等价的方式执行 *expression* 给出的命令，并返回该命令的退出状态。

所有形式的 `getline` 应在成功输入时返回 1，文件结尾时返回零，出错时返回 -1。

在字符串用作文件或管道的名称时，应用应确保这些字符串在文本上完全相同。“相同字符串值”这一术语意味着“等价的字符串”，即使那些仅相差 \<space\>（空格）字符的字符串，也表示不同的文件。

### 用户定义函数 (User-Defined Functions)

*awk* 语言还提供用户定义函数。此类函数可以定义为：

```
function name([parameter, ...]) { statements }
```

函数可以在 *awk* 程序中的任何位置被引用；特别是，它的使用可以先于它的定义。函数的作用域是全局的。

函数定义中的参数个数不必与函数调用中的参数个数匹配。多余的形式参数可以用作局部变量。如果函数调用中提供的参数少于函数定义中的参数，则函数体中用作标量的多余参数在另行初始化之前应求值为未初始化的值，而函数体中用作数组的多余参数应被视为未初始化的数组，其中每个元素在另行初始化之前求值为未初始化的值。

调用函数时，函数名与左括号之间不能放置空白。函数调用可以嵌套，也可以对函数进行递归调用。从任何嵌套或递归函数调用返回时，调用函数的所有参数的值都应保持不变，按引用传递的数组参数除外。`return` 语句可用于返回值。如果 `return` 语句出现在函数定义之外，行为是未定义的（undefined）。

在函数定义中，左花括号之前和右花括号之后的 \<newline\>（换行）字符应是可选的。函数定义可以出现在程序中允许模式-动作对的任何位置。
### 语法 (Grammar)

本节中的文法与下一节中的词法约定应共同描述 *awk* 程序的语法。此类文法的通用约定在 [*1.3 文法约定*](../utilities/V3_chap01.html#tag_18_03) 中描述。有效程序可以用文法中的非终结符号 *program* 表示。此形式语法应优先于前面的文本语法描述。

```
%token NAME NUMBER STRING ERE
%token FUNC_NAME   /* Name followed by '(' without white space. */

/* Keywords */
%token       Begin   End
/*          'BEGIN' 'END'                                */

%token       Break   Continue   Delete   Do   Else
/*          'break' 'continue' 'delete' 'do' 'else'      */

%token       Exit   For   Function   If   In   Next
/*          'exit' 'for' 'function' 'if' 'in' 'next'     */

%token       Nextfile   Print   Printf   Return   While
/*          'nextfile' 'print' 'printf' 'return' 'while' */

/* Reserved function names */
%token BUILTIN_FUNC_NAME
            /* One token for the following:
             * atan2 cos sin exp log sqrt int rand srand
             * gsub index length match split sprintf sub
             * substr tolower toupper close fflush system
             */
%token GETLINE
            /* Syntactically different from other built-ins. */

/* Two-character tokens. */
%token ADD_ASSIGN SUB_ASSIGN MUL_ASSIGN DIV_ASSIGN MOD_ASSIGN POW_ASSIGN
/*     '+='       '-='       '*='       '/='       '%='       '^=' */

%token OR   AND  NO_MATCH   EQ   LE   GE   NE   INCR  DECR  APPEND
/*     '||' '&&' '!~' '==' '<=' '>=' '!=' '++'  '--'  '>>'   */

/* One-character tokens. */
%token '{' '}' '(' ')' '[' ']' ',' ';' NEWLINE
%token '+' '-' '*' '%' '^' '!' '>' '<' '|' '?' ':' '~' '$' '='

%start program
%%

program          : item_list
                 | item_list item
                 ;

item_list        : /* empty */
                 | item_list item terminator
                 ;

item             : action
                 | pattern action
                 | normal_pattern
                 | Function NAME      '(' param_list_opt ')'
                       newline_opt action
                 | Function FUNC_NAME '(' param_list_opt ')'
                       newline_opt action
                 ;

param_list_opt   : /* empty */
                 | param_list
                 ;

param_list       : NAME
                 | param_list ',' NAME
                 ;

pattern          : normal_pattern
                 | special_pattern
                 ;

normal_pattern   : expr
                 | expr ',' newline_opt expr
                 ;

special_pattern  : Begin
                 | End
                 ;

action           : '{' newline_opt                             '}'
                 | '{' newline_opt terminated_statement_list   '}'
                 | '{' newline_opt unterminated_statement_list '}'
                 ;

terminator       : terminator NEWLINE
                 |            ';'
                 |            NEWLINE
                 ;

terminated_statement_list : terminated_statement
                 | terminated_statement_list terminated_statement
                 ;

unterminated_statement_list : unterminated_statement
                 | terminated_statement_list unterminated_statement
                 ;

terminated_statement : action newline_opt
                 | If '(' expr ')' newline_opt terminated_statement
                 | If '(' expr ')' newline_opt terminated_statement
                       Else newline_opt terminated_statement
                 | While '(' expr ')' newline_opt terminated_statement
                 | For '(' simple_statement_opt ';'
                      expr_opt ';' simple_statement_opt ')' newline_opt
                      terminated_statement
                 | For '(' NAME In NAME ')' newline_opt
                      terminated_statement
                 | ';' newline_opt
                 | terminatable_statement NEWLINE newline_opt
                 | terminatable_statement ';'     newline_opt
                 ;

unterminated_statement : terminatable_statement
                 | If '(' expr ')' newline_opt unterminated_statement
                 | If '(' expr ')' newline_opt terminated_statement
                      Else newline_opt unterminated_statement
                 | While '(' expr ')' newline_opt unterminated_statement
                 | For '(' simple_statement_opt ';'
                  expr_opt ';' simple_statement_opt ')' newline_opt
                      unterminated_statement
                 | For '(' NAME In NAME ')' newline_opt
                      unterminated_statement
                 ;

terminatable_statement : simple_statement
                 | Break
                 | Continue
                 | Next
                 | Nextfile
                 | Exit expr_opt
                 | Return expr_opt
                 | Do newline_opt terminated_statement While '(' expr ')'
                 ;

simple_statement_opt : /* empty */
                 | simple_statement
                 ;

simple_statement : Delete NAME '[' expr_list ']'
                 | Delete NAME
                 | expr
                 | print_statement
                 ;

print_statement  : simple_print_statement
                 | simple_print_statement output_redirection
                 ;

simple_print_statement : Print  print_expr_list_opt
                 | Print  '(' multiple_expr_list ')'
                 | Printf print_expr_list
                 | Printf '(' multiple_expr_list ')'
                 ;

output_redirection : '>'    expr
                 | APPEND expr
                 | '|'    expr
                 ;

expr_list_opt    : /* empty */
                 | expr_list
                 ;

expr_list        : expr
                 | multiple_expr_list
                 ;

multiple_expr_list : expr ',' newline_opt expr
                 | multiple_expr_list ',' newline_opt expr
                 ;

expr_opt         : /* empty */
                 | expr
                 ;

expr             : unary_expr
                 | non_unary_expr
                 ;

unary_expr       : '+' expr
                 | '-' expr
                 | unary_expr '^'      expr
                 | unary_expr '*'      expr
                 | unary_expr '/'      expr
                 | unary_expr '%'      expr
                 | unary_expr '+'      expr
                 | unary_expr '-'      expr
                 | unary_expr          non_unary_expr
                 | unary_expr '<'      expr
                 | unary_expr LE       expr
                 | unary_expr NE       expr
                 | unary_expr EQ       expr
                 | unary_expr '>'      expr
                 | unary_expr GE       expr
                 | unary_expr '~'      expr
                 | unary_expr NO_MATCH expr
                 | unary_expr In NAME
                 | unary_expr AND newline_opt expr
                 | unary_expr OR  newline_opt expr
                 | unary_expr '?' expr ':' expr
                 | unary_input_function
                 ;

non_unary_expr   : '(' expr ')'
                 | '!' expr
                 | non_unary_expr '^'      expr
                 | non_unary_expr '*'      expr
                 | non_unary_expr '/'      expr
                 | non_unary_expr '%'      expr
                 | non_unary_expr '+'      expr
                 | non_unary_expr '-'      expr
                 | non_unary_expr          non_unary_expr
                 | non_unary_expr '<'      expr
                 | non_unary_expr LE       expr
                 | non_unary_expr NE       expr
                 | non_unary_expr EQ       expr
                 | non_unary_expr '>'      expr
                 | non_unary_expr GE       expr
                 | non_unary_expr '~'      expr
                 | non_unary_expr NO_MATCH expr
                 | non_unary_expr In NAME
                 | '(' multiple_expr_list ')' In NAME
                 | non_unary_expr AND newline_opt expr
                 | non_unary_expr OR  newline_opt expr
                 | non_unary_expr '?' expr ':' expr
                 | NUMBER
                 | STRING
                 | lvalue
                 | ERE
                 | lvalue INCR
                 | lvalue DECR
                 | INCR lvalue
                 | DECR lvalue
                 | lvalue POW_ASSIGN expr
                 | lvalue MOD_ASSIGN expr
                 | lvalue MUL_ASSIGN expr
                 | lvalue DIV_ASSIGN expr
                 | lvalue ADD_ASSIGN expr
                 | lvalue SUB_ASSIGN expr
                 | lvalue '=' expr
                 | FUNC_NAME '(' expr_list_opt ')'
                      /* no white space allowed before '(' */
                 | BUILTIN_FUNC_NAME '(' expr_list_opt ')'
                 | BUILTIN_FUNC_NAME
                 | non_unary_input_function
                 ;

print_expr_list_opt : /* empty */
                 | print_expr_list
                 ;

print_expr_list  : print_expr
                 | print_expr_list ',' newline_opt print_expr
                 ;

print_expr       : unary_print_expr
                 | non_unary_print_expr
                 ;

unary_print_expr : '+' print_expr
                 | '-' print_expr
                 | unary_print_expr '^'      print_expr
                 | unary_print_expr '*'      print_expr
                 | unary_print_expr '/'      print_expr
                 | unary_print_expr '%'      print_expr
                 | unary_print_expr '+'      print_expr
                 | unary_print_expr '-'      print_expr
                 | unary_print_expr          non_unary_print_expr
                 | unary_print_expr '~'      print_expr
                 | unary_print_expr NO_MATCH print_expr
                 | unary_print_expr In NAME
                 | unary_print_expr AND newline_opt print_expr
                 | unary_print_expr OR  newline_opt print_expr
                 | unary_print_expr '?' print_expr ':' print_expr
                 ;

non_unary_print_expr : '(' expr ')'
                 | '!' print_expr
                 | non_unary_print_expr '^'      print_expr
                 | non_unary_print_expr '*'      print_expr
                 | non_unary_print_expr '/'      print_expr
                 | non_unary_print_expr '%'      print_expr
                 | non_unary_print_expr '+'      print_expr
                 | non_unary_print_expr '-'      print_expr
                 | non_unary_print_expr          non_unary_print_expr
                 | non_unary_print_expr '~'      print_expr
                 | non_unary_print_expr NO_MATCH print_expr
                 | non_unary_print_expr In NAME
                 | '(' multiple_expr_list ')' In NAME
                 | non_unary_print_expr AND newline_opt print_expr
                 | non_unary_print_expr OR  newline_opt print_expr
                 | non_unary_print_expr '?' print_expr ':' print_expr
                 | NUMBER
                 | STRING
                 | lvalue
                 | ERE
                 | lvalue INCR
                 | lvalue DECR
                 | INCR lvalue
                 | DECR lvalue
                 | lvalue POW_ASSIGN print_expr
                 | lvalue MOD_ASSIGN print_expr
                 | lvalue MUL_ASSIGN print_expr
                 | lvalue DIV_ASSIGN print_expr
                 | lvalue ADD_ASSIGN print_expr
                 | lvalue SUB_ASSIGN print_expr
                 | lvalue '=' print_expr
                 | FUNC_NAME '(' expr_list_opt ')'
                     /* no white space allowed before '(' */
                 | BUILTIN_FUNC_NAME '(' expr_list_opt ')'
                 | BUILTIN_FUNC_NAME
                 ;

lvalue           : NAME
                 | NAME '[' expr_list ']'
                 | '$' expr
                 ;

non_unary_input_function : simple_get
                 | simple_get '<' expr
                 | non_unary_expr '|' simple_get
                 ;

unary_input_function : unary_expr '|' simple_get
                 ;

simple_get       : GETLINE
                 | GETLINE lvalue
                 ;

newline_opt      : /* empty */
                 | newline_opt NEWLINE
                 ;
```

此文法有几个歧义，应按如下方式解决：

- 运算符优先级和结合性应如“awk 中按优先级递减的表达式 (Expressions in Decreasing Precedence in awk)”所述。
- 在有歧义的情况下，`else` 应与最接近的、能满足文法的前面的 `if` 关联。
- 在某些上下文中，用于包围 ERE 的 \<slash\>（斜杠）（`'/'`）也可能是除法运算符。这应以这样的方式解决：在除法运算符可能出现的任何地方，都假定 \<slash\> 是除法运算符。（没有一元除法运算符。）

*awk* 程序中的每个表达式都应符合优先级和结合性规则，即使这不是解决歧义所必需的。例如，由于 `'$'` 的优先级高于 `'++'`，字符串 `"$x++--"` 不是有效的 *awk* 表达式，尽管文法明确地将其解析为 `"$(x++)--"`。

形式文法中可能不明显的一个约定是 \<newline\>（换行）字符在何处可接受。有几个明显的位置，例如终止语句，并且 \<backslash\> 可用于转义任何词法 token 之间的 \<newline\> 字符。此外，不带 \<backslash\> 字符的 \<newline\> 字符可以跟在逗号、左花括号、逻辑与运算符（`"&&"`）、逻辑或运算符（`"||"`）、`do` 关键字、`else` 关键字以及 `if`、`for` 或 `while` 语句的右括号之后。例如：

```
{ print  $1,
         $2 }
```

### 词法约定 (Lexical Conventions)

关于前述文法，*awk* 程序的词法约定应如下：

1. 除注明者外，*awk* 应识别在给定点开始的最长可能 token 或分隔符。
2. 注释应由以 \<number-sign\>（数字符号）字符开头、以（但不包括）下一次出现的 \<newline\>（换行符）终止的任何字符组成。注释除了分隔词法 token 外没有其他作用。
3. \<newline\>（换行符）应被识别为 token `NEWLINE`。
4. 紧跟 \<newline\>（换行符）的 \<backslash\>（反斜杠）字符应没有作用。
5. token `STRING` 应表示字符串常量。字符串常量应以 `'"'` 字符开头。在字符串常量内部，\<backslash\>（反斜杠）字符应被视为开始 XBD [*5. 文件格式记号*](../basedefs/V1_chap05.html#tag_05) 中的表所规定的转义序列（`'\\'`、`'\a'`、`'\b'`、`'\f'`、`'\n'`、`'\r'`、`'\t'`、`'\v'`）。此外，还应识别“awk 中的转义序列 (Escape Sequences in awk)”中的转义序列。字符串常量内不应出现 \<newline\>（换行符）。字符串常量应由开始字符串常量的 `'"'` 字符之后第一个未转义的 `'"'` 字符的出现终止。字符串的值应是在两个定界 `'"'` 字符之间（但不包括它们）的所有未转义字符和转义序列的值序列。
6. token `ERE` 表示扩展正则表达式常量。ERE 常量应以 \<slash\>（斜杠）字符开头。在 ERE 常量内部，\<backslash\>（反斜杠）字符应被视为开始 XBD [*5. 文件格式记号*](../basedefs/V1_chap05.html#tag_05) 中的表所规定的转义序列。此外，还应识别“awk 中的转义序列 (Escape Sequences in awk)”中的转义序列。应用应确保 \<newline\>（换行符）不发生在 ERE 常量内。ERE 常量应由开始 ERE 常量的 \<slash\> 字符之后第一个未转义的 \<slash\> 字符的出现终止。ERE 常量所表示的扩展正则表达式应是在两个定界 \<slash\> 字符之间（但不包括它们）的所有未转义字符和转义序列的值序列。
7. \<blank\>（空白）除了分隔词法 token 或在 `STRING` 或 `ERE` token 内部外，没有其他作用。
8. token `NUMBER` 应表示数值常量。其形式和数值应等价于 ISO C 标准规定的 `decimal-floating-constant` token，或者应是十进制数字序列并按十进制整数常量求值。此外，实现可以接受形式和数值等价于 ISO C 标准规定的 `hexadecimal-constant` 和 `hexadecimal-floating-constant` token 的数值常量。注意，这些形式不使用当前 locale 的小数点字符；它们总是使用 \<period\>（句点）。
   如果该值太大或太小而无法表示（见 [*1.1.2 源自 ISO C 标准的概念*](../utilities/V3_chap01.html#tag_18_01_02)），行为是未定义的（undefined）。
9. 便携字符集（见 XBD [*6.1 便携字符集*](../basedefs/V1_chap06.html#tag_06_01)）中的一串下划线、数字和字母，以 \<underscore\>（下划线）或字母字符开头，应被视为一个单词（word）。
10. 以下单词是应被识别为单独 token 的关键字；token 的名称与关键字相同：

<table cellpadding="3" align="center">
<tr valign="top">
<td align="left"><p><br><code>BEGIN</code><br><code>break</code><br><code>continue</code><br></p></td>
<td align="left"><p><br><code>delete</code><br><code>do</code><br><code>else</code><br></p></td>
<td align="left"><p><br><code>END</code><br><code>exit</code><br><code>for</code><br></p></td>
<td align="left"><p><br><code>function</code><br><code>getline</code><br><code>if</code><br></p></td>
<td align="left"><p><br><code>in</code><br><code>next</code><br><code>nextfile</code><br></p></td>
<td align="left"><p><br><code>print</code><br><code>printf</code><br><code>return</code><br></p></td>
<td align="left"><p><br><code>while</code><br></p></td>
</tr>
</table>

11. 以下单词是内置函数的名称，应被识别为 token `BUILTIN_FUNC_NAME`：

<table cellpadding="3" align="center">
<tr valign="top">
<td align="left"><p><br><code>atan2</code><br><code>close</code><br><code>cos</code><br><code>exp</code><br></p></td>
<td align="left"><p><br><code>fflush</code><br><code>gsub</code><br><code>index</code><br></p></td>
<td align="left"><p><br><code>int</code><br><code>length</code><br><code>log</code><br></p></td>
<td align="left"><p><br><code>match</code><br><code>rand</code><br><code>sin</code><br></p></td>
<td align="left"><p><br><code>split</code><br><code>sprintf</code><br><code>sqrt</code><br></p></td>
<td align="left"><p><br><code>srand</code><br><code>sub</code><br><code>substr</code><br></p></td>
<td align="left"><p><br><code>system</code><br><code>tolower</code><br><code>toupper</code><br></p></td>
</tr>
</table>

    上面列出的关键字和内置函数名称被视为保留字（reserved word）。

12. token `NAME` 应由一个单词组成，该单词不是关键字或内置函数名称，并且不紧跟（没有任何分隔符）`'('` 字符。
13. token `FUNC_NAME` 应由一个单词组成，该单词不是关键字或内置函数名称，紧跟（没有任何分隔符）`'('` 字符。`'('` 字符不应作为 token 的一部分包含在内。
14. 以下两字符序列应被识别为指定的 token：

<table border="1" cellpadding="3" align="center">
<tr valign="top">
<th align="center"><p><b>Token 名称 (Token Name)</b></p></th>
<th align="center"><p><b>序列 (Sequence)</b></p></th>
<th align="center"><p><b>Token 名称 (Token Name)</b></p></th>
<th align="center"><p><b>序列 (Sequence)</b></p></th>
</tr>
<tr valign="top"><td align="left"><p><code>ADD_ASSIGN</code></p></td><td align="center"><p>+=</p></td><td align="left"><p><code>NO_MATCH</code></p></td><td align="center"><p>!~</p></td></tr>
<tr valign="top"><td align="left"><p><code>SUB_ASSIGN</code></p></td><td align="center"><p>-=</p></td><td align="left"><p><code>EQ</code></p></td><td align="center"><p>==</p></td></tr>
<tr valign="top"><td align="left"><p><code>MUL_ASSIGN</code></p></td><td align="center"><p>&#42;=</p></td><td align="left"><p><code>LE</code></p></td><td align="center"><p>&lt;=</p></td></tr>
<tr valign="top"><td align="left"><p><code>DIV_ASSIGN</code></p></td><td align="center"><p>/=</p></td><td align="left"><p><code>GE</code></p></td><td align="center"><p>&gt;=</p></td></tr>
<tr valign="top"><td align="left"><p><code>MOD_ASSIGN</code></p></td><td align="center"><p>%=</p></td><td align="left"><p><code>NE</code></p></td><td align="center"><p>!=</p></td></tr>
<tr valign="top"><td align="left"><p><code>POW_ASSIGN</code></p></td><td align="center"><p>^=</p></td><td align="left"><p><code>INCR</code></p></td><td align="center"><p>++</p></td></tr>
<tr valign="top"><td align="left"><p><code>OR</code></p></td><td align="center"><p>||</p></td><td align="left"><p><code>DECR</code></p></td><td align="center"><p>--</p></td></tr>
<tr valign="top"><td align="left"><p><code>AND</code></p></td><td align="center"><p>&amp;&amp;</p></td><td align="left"><p><code>APPEND</code></p></td><td align="center"><p>&gt;&gt;</p></td></tr>
</table>

15. 以下单个字符应被识别为名称即该字符本身的 token：

    ```
    <newline> { } ( ) [ ] , ; + - * % ^ ! > < | ? : ~ $ =
    ```

token `ERE` 与 token `'/'` 和 `DIV_ASSIGN` 之间存在词法歧义。当输入序列以 \<slash\>（斜杠）字符开头、处于 token `'/'` 或 `DIV_ASSIGN` 可以作为有效程序中的下一个 token 出现的任何语法上下文时，应识别这两个可识别的 token 中较长者。在 token `ERE` 可以作为有效程序中的下一个 token 出现的任何其他语法上下文中，应识别 token `ERE`。

## 退出状态 (EXIT STATUS)

应返回以下退出值：

`0`

:   所有输入文件都成功处理。

`>0`

:   发生错误。

可以使用 `exit` 表达式在程序内部更改退出状态。

## 错误后果 (CONSEQUENCES OF ERRORS)

如果指定了任何 *file* 操作数且无法访问所命名的文件，*awk* 应向标准错误写入诊断消息并终止，而不采取任何进一步操作。

如果由 *program* 操作数或 *progfile* 操作数指定的程序不是有效的 *awk* 程序（如“扩展描述 (EXTENDED DESCRIPTION)”一节所规定），行为是未定义的（undefined）。

---

*以下各节是提供信息的（informative）。*

## 应用程序用法 (APPLICATION USAGE)

由于 \<backslash\>（反斜杠）在 `-v` 选项的 *assignment* 选项参数和 *assignment* 操作数中都有特殊含义，需要将字符串传递给 *awk* 而不对 \<backslash\> 进行特殊解释的应用不应使用这些方法，而应利用 `ARGV` 或 `ENVIRON` 数组。

`index`、`length`、`match` 和 `substr` 函数不应与 ISO C 标准中的类似函数混淆；*awk* 版本处理字符，而 ISO C 标准处理字节。

由于连接操作由相邻表达式表示，而不是显式运算符，因此通常有必要使用括号来强制执行正确的求值优先级。

使用 *awk* 处理路径名时，建议在环境中将 LC_ALL 或至少 LC_CTYPE 和 LC_COLLATE 设置为 POSIX 或 C，因为路径名可以包含在某些 locale 中不构成有效字符的字节序列，在这种情况下实用程序的行为将是未定义的（undefined）。在 POSIX locale 中，每个字节都是有效的单字节字符，因此避免了此问题。

由于 `"=="` 运算符检查字符串是否相同，而不是它们是否整理相等，需要检查字符串是否整理相等的应用可以使用：

```
a <= b && a >= b
```

要指定命名包含 \<equals-sign\>（等号）的文件名的 *file* 操作数，用户可以使用 `"./"` 作为以 \<underscore\>（下划线）或字母字符开头的相对文件路径名的前两个字符，以防止该 *file* 操作数被解释为 *assignment* 操作数。类似地，`"./-"` 可用于访问当前目录中名为 `'-'` 的文件，而不是使用标准输入。

## 示例 (EXAMPLES)

在命令行中指定的 *awk* 程序最容易放在单引号内（例如，`'program'`）供使用 [*sh*](../utilities/sh.html) 的应用使用，因为 *awk* 程序通常包含对 shell 特殊的字符，包括双引号。在 *awk* 程序包含单引号字符的情况下，通常最容易将程序的大部分指定为单引号内的字符串，并由 shell 用加引号的单引号字符连接起来。例如：

```
awk '/'/ { print "quote:", $0 }'
```

打印标准输入中包含单引号字符的所有行，前缀为 *quote:*。

以下是简单 *awk* 程序的示例：

1. 向标准输出写入字段 3 大于 5 的所有输入行：

   ```
   $3 > 5
   ```

2. 写出每第十行：

   ```
   (NR % 10) == 0
   ```

3. 写出任何包含匹配正则表达式的子串的行：

   ```
   /(G|D)(2[0-9][[:alpha:]]*)/
   ```

4. 打印任何包含 `'G'` 或 `'D'` 后跟数字和字符序列的子串的行。此示例使用字符类 `digit` 和 `alpha` 分别匹配与语言无关的数字和字母字符：

   ```
   /(G|D)([[:digit:][:alpha:]]*)/
   ```

5. 写出第二个字段匹配正则表达式而第四个字段不匹配的任何行：

   ```
   $2 ~ /xyz/ && $4 !~ /xyz/
   ```

6. 写出第二个字段包含 \<backslash\>（反斜杠）的任何行：

   ```
   $2 ~ /\\/
   ```

7. 写出第二个字段包含 \<backslash\>（反斜杠）的任何行。注意 \<backslash\>-转义被解释两次；一次在字符串的词法处理中，一次在正则表达式的处理中：

   ```
   $2 ~ "\\\\"
   ```

8. 写出每行的倒数第二个和最后一个字段。用 \<colon\>（冒号）分隔字段：

   ```
   {OFS=":";print $(NF-1), $NF}
   ```

9. 写出每行的行号和字段数。表示行号、\<colon\>（冒号）和字段数的三个字符串被连接起来，该字符串被写入标准输出：

   ```
   {print NR ":" NF}
   ```

10. 写出长度超过 72 个字符的行：

    ```
    length($0) > 72
    ```

11. 写出前两个字段，按相反顺序，用 `OFS` 分隔：

    ```
    { print $2, $1 }
    ```

12. 同上，但输入字段由 \<comma\>（逗号）或 \<space\>（空格）和 \<tab\>（制表）字符或两者分隔：

    ```
    BEGIN { FS = ", [ \t]*|[ \t]+" }
          { print $2, $1 }
    ```

13. 累加第一列，打印总和和平均值：

    ```
          {s += $1 }
    END   {print "sum is ", s, " average is", s/NR}
    ```

14. 按相反顺序写出字段，每行一个（每一行输入产生多行输出）：

    ```
    { for (i = NF; i > 0; --i) print $i }
    ```

15. 写出字符串 `start` 和 `stop` 出现之间的所有行：

    ```
    /start/, /stop/
    ```

16. 写出第一个字段与前一行的第一个字段不同的所有行：

    ```
    $1 != prev { print; prev = $1 }
    ```

17. 模拟 [*echo*](../utilities/echo.html)：

    ```
    BEGIN  {
            for (i = 1; i < ARGC; ++i)
            printf("%s%s", ARGV[i], i==ARGC-1?"\n":" ")
    }
    ```

18. 写出 *PATH* 环境变量中包含的路径前缀，每行一个：

    ```
    BEGIN  {
            n = split (ENVIRON["PATH"], path, ":")
            for (i = 1; i <= n; ++i)
            print path[i]
    }
    ```

19. 如果有一个名为 `input` 的文件包含如下形式的页眉：Page #（Page 页号）

    并且有一个名为 `program` 的文件包含：

    ```
    /Page/   { $2 = n++; }
             { print }
    ```

    那么命令行：

    ```
    awk -f program n=5 input
    ```

    打印文件 `input`，填入从 5 开始的页码。
## 原理 (RATIONALE)

此描述基于新的 *awk*（“nawk”）（见所引用的 *The AWK Programming Language*），它为历史 *awk* 引入了许多新特性：

1. 新关键字：`delete`、`do`、`function`、`return`
2. 新内置函数：`atan2`、`close`、`cos`、`gsub`、`match`、`rand`、`sin`、`srand`、`sub`、`system`
3. 新的预定义变量：`FNR`、`ARGC`、`ARGV`、`RSTART`、`RLENGTH`、`SUBSEP`
4. 新的表达式运算符：`?`、`:`、`,`、`^`
5. `FS` 变量和 `split` 的第三个参数，现在被视为扩展正则表达式。
6. 运算符优先级，改为更接近 C 语言。两个行为不同的代码示例是：

   ```
   while ( n /= 10 > 1) ...
   if (!"wk" ~ /bwk/) ...
   ```

基于较新的 *awk* 实现添加了几个特性：

- 允许多个 `-f progfile` 实例。
- 新选项 `-v assignment`。
- 新的预定义变量 `ENVIRON`。
- 新的内置函数 `toupper` 和 `tolower`。
- `printf` 增加了更多格式化能力以匹配 ISO C 标准。

本标准的早期版本要求实现支持多个相邻 \<semicolon\>（分号）、规则（模式-动作对）前有一个或多个 \<semicolon\> 的行，以及只有 \<semicolon\>（s）的行。本标准不要求这些，并认为它们是不良编程实践，但 *awk* 的实现可以将其作为扩展接受。

*awk* 的整体语法一直基于 C 语言，并带有一些来自 shell 命令语言和其他来源的特性。因此，它与任何其他语言都不完全兼容，这给一些用户造成了困惑。标准开发者无意解决此类问题。为使语言与 ISO C 标准更兼容，进行了一些相对较小的更改；这些更改大多基于近期实现中的类似更改，如上所述。*awk* 中仍然没有几种 C 语言约定。其中一个值得注意的是 \<comma\>（逗号）运算符，它在 C 语言中常用于在 `for` 语句中指定多个表达式。此外，在给定上下文中可以使用哪种类型的表达式方面，*awk* 比 C 语言更受限制的地方有各种各样。这些限制是由于 *awk* 语言确实提供的不同特性。

*awk* 中的正则表达式已从历史实现进行了某种程度的扩展，使它们成为扩展正则表达式的纯超集，如 POSIX.1-2024 所定义（见 XBD [*9.4 扩展正则表达式*](../basedefs/V1_chap09.html#tag_09_04)）。主要扩展是国际化特性和区间表达式（interval expression）。历史 *awk* 实现长期支持 \<backslash\>-转义序列作为扩展正则表达式的扩展，尽管与其他实用程序不一致，此扩展仍被保留。在扩展正则表达式和字符串中识别的转义序列数量在各实现中有所不同（通常随时间增加）。POSIX.1-2024 规定的集合包括已知被流行实现和 ISO C 标准支持的大多数序列。一个不支持的序列是以 `'\x'` 开头的十六进制值转义。这将允许在 *awk* 中使用超过 9 位表示的值，如同在 ISO C 标准中一样。但是，由于此语法具有非确定性长度，它不允许后续字符是十六进制数字。在 C 语言中，可以通过使用词法字符串连接来处理此限制。在 *awk* 语言中，连接也可以是字符串的解决方案，但不适用于扩展正则表达式（无论是词法 ERE token 还是动态用作正则表达式的字符串）。由于此限制，该特性尚未添加到 POSIX.1-2024 中。

当字符串变量在通常出现扩展正则表达式的上下文（文法中使用词法 token ERE 的地方）中使用时，该字符串不包含字面的 \<slash\>（斜杠）字符。

某些版本的 *awk* 允许以下形式：

```
func name(args, ... ) { statements }
```

这已被语言作者弃用，他们要求不要将其标准化。

历史 *awk* 实现如果在 `BEGIN` 动作中执行 `next` 语句会产生错误，如果在 `END` 动作中执行 `next` 语句会导致 *awk* 终止。此行为未被记录，并且认为没有必要将其标准化。

字符串与数值之间转换的规定比历史实现的文档或所引用的 *The AWK Programming Language* 中的规定详细得多。虽然大部分行为旨在直观，但细节对于确保不同实现的行为兼容是必要的。这在关系表达式中尤其重要，因为操作数的类型决定了执行字符串比较还是数值比较。从应用程序开发者的角度来看，通常期望直观的行为，并在表达式的类型与所需类型不明显匹配时强制转换（通过加零或连接空字符串）就足够了。意图几乎在所有情况下都规定历史实践。唯一的例外是，在历史实现中，变量和常量在其原始值被任何使用转换后仍保持字符串和数值两种值。这意味着引用变量或常量可能产生意外的副作用。例如，使用历史实现，以下程序：

```
{
    a = "+2"
    b = 2
    if (NR % 2)
        c = a + b
    if (a == b)
        print "numeric comparison"
    else
        print "string comparison"
}
```

将对每个奇数行执行数值比较（并输出 numeric comparison），但对每个偶数行执行字符串比较（并输出 string comparison）。POSIX.1-2024 确保在必要时比较将是数值的。使用历史实现，以下程序：

```
BEGIN {
    OFMT = "%e"
    print 3.14
    OFMT = "%f"
    print 3.14
}
```

将输出 `"3.140000e+00"` 两次，因为在第二个 `print` 语句中，常量 `"3.14"` 将具有先前转换的字符串值。POSIX.1-2024 要求第二个 `print` 语句的输出为 `"3.140000"`。历史实现的行为被认为过于不直观和不可预测。

有人指出，根据早期草案中的规则，以下脚本将不打印任何内容：

```
BEGIN {
    y[1.5] = 1
    OFMT = "%e"
    print y[1.5]
}
```

因此，引入了一个新变量 `CONVFMT`。`OFMT` 变量现在仅限于影响数字到字符串的输出转换，而 `CONVFMT` 用于内部转换，例如比较或数组索引。默认值与 `OFMT` 相同，因此除非程序更改 `CONVFMT`（历史程序不会这样做），否则它将获得与内部字符串转换相关的历史行为。

POSIX *awk* 的词法和句法约定比其他来源规定得更正式。同样，意图是规定历史实践。一个从形式文法中可能不明显的约定（如其他口头描述中所述）是 \<newline\>（换行）字符在何处可接受。有几个明显的位置，例如终止语句，并且 \<backslash\> 可用于转义任何词法 token 之间的 \<newline\> 字符。此外，不带 \<backslash\> 字符的 \<newline\> 字符可以跟在逗号、左花括号、逻辑与运算符（`"&&"`）、逻辑或运算符（`"||"`）、`do` 关键字、`else` 关键字以及 `if`、`for` 或 `while` 语句的右括号之后。例如：

```
{ print $1,
        $2 }
```

要求 *awk* 向程序参数文本添加尾随 \<newline\>（换行符）是为了简化文法，使其在形式上与文本文件匹配。应用或测试套件无法确定是添加了字面的 \<newline\>，还是 *awk* 只是表现得如同添加了一样。

POSIX.1-2024 要求对历史实现进行几处更改以支持国际化。其中可能最微妙的是在浮点数表示中使用由 locale 的 `LC_NUMERIC` 类别定义的小数点字符。此 locale 特定字符用于识别数字输入、在字符串和数值之间转换以及格式化输出。但是，无论 locale 如何，\<period\>（句点）字符（POSIX locale 的小数点字符）都是处理 *awk* 程序（包括命令行参数中的赋值）时所识别的小数点字符。这基本上与 ISO C 标准中使用的约定相同。区别在于 C 语言包含 [*setlocale*()](../functions/setlocale.html) 函数，该函数允许应用修改其 locale。由于此能力，C 应用开始执行时其 locale 设置为 C locale，并且仅在显式调用 [*setlocale*()](../functions/setlocale.html) 之后才在环境指定的 locale 中执行。但是，在 *awk* 语言中添加如此复杂的新特性被认为不适合 POSIX.1-2024。可以通过在 shell 中设置环境来在任何所需 locale 中显式执行 *awk* 程序。

扩展正则表达式中 NUL 产生的未定义（undefined）行为允许 GNU *gawk* 程序的未来扩展处理二进制数据。

无效 *awk* 程序（包括词法、句法和语义错误）情况下的行为是未定义的，因为认为对此进行规定对实现限制过多。在大多数情况下，此类错误可以预期产生诊断和非零退出状态。但是，某些实现可能选择以利用某些无效结构的方式扩展语言。其他无效结构可能被认为值得警告，但除此之外会导致某些合理的行为。还有某些结构在某些实现中可能很难检测。此外，不同的实现可能在程序初始解析期间（在读取任何输入文件之前）检测给定错误，而其他实现可能在读取一些输入后执行程序时检测到它。实现者应意识到，尽早诊断错误并产生有用的诊断可以简化应用的调试，从而使实现更可用。

使用多字符 `RS` 值的未指定（unspecified）行为是为了允许基于用于记录分隔符的扩展正则表达式的可能未来扩展。历史实现取字符串的第一个字符并忽略其他字符。

当使用 [*split*](../utilities/split.html)(*string*,*array*,`<null>`) 时的未指定行为是为了允许一个提议的未来扩展，该扩展将字符串拆分为单个字符的数组。

在 `getline` 函数的上下文中，可以为 `|` 和 `<` 运算符的不同优先级提出同样好的论据。历史实践是：

```
getline < "a" "b"
```

被解析为：

```
( getline < "a" ) "b"
```

尽管许多人会争辩说意图是应读取文件 `ab`。但是：

```
getline < "x" + 1
```

解析为：

```
getline < ( "x" + 1 )
```

`getline` 的 `|` 版本也会出现类似问题，特别是与 `$` 结合使用时。例如：

```
$"echo hi" | getline
```

（此情况在 `print` 语句中使用时尤其成问题，其中 `|getline` 部分可能是 `print` 的重定向。）

由于在大多数情况下此类结构不应（或至少不应）被使用（因为它们具有没有常规解析的自然歧义），这些结构的含义已被明确地规定为未指定的（unspecified）。（效果是遇到该问题的符合标准的应用必须加括号来解决歧义。）此类结构的实际使用似乎很少（如果有的话）。

可以编写在这些情况下会导致错误的文法。在向后兼容性不是主要考虑因素的地方，实现者可能希望使用此类文法。

一些历史实现允许一些内置函数在没有参数列表的情况下被调用，结果是以某种“合理”方式选择的默认参数列表。将 `length` 用作 `length($0)` 的同义词是这些形式中唯一被认为被广泛知晓或广泛使用的；此特定形式在各种地方被记录（例如，大多数历史 *awk* 参考页，尽管不在所引用的 *The AWK Programming Language* 中）为合法实践。除这个例外，默认参数列表一直未被记录且定义模糊，并且完全不清楚它们应如何（或是否应）推广到用户定义函数。它们没有添加有用的功能，并排除可能的未来扩展（这些扩展可能需要在不调用的情况下命名函数）。不将它们标准化似乎是最简单的做法。标准开发者认为 `length` 值得特殊对待，因为它过去已被记录，并且在历史程序中可能有相当大的使用量。因此，此用法已被合法化，但 Issue 5 移除了对 XSI 一致性实现的过时标记，并且许多其他方面符合标准的应用依赖于此特性。

在 `sub` 和 `gsub` 中，如果 *repl* 是字符串字面量（词法 token `STRING`），则应在字符串中使用两个连续的 \<backslash\>（反斜杠）字符，以确保当结果字符串传递给函数时，单个 \<backslash\> 将位于 \<ampersand\>（& 符号）之前。（例如，要在替换字符串中指定一个字面 \<ampersand\>，请使用 `gsub(ERE, "\\&")`。）

历史上，`sub` 和 `gsub` 字符串函数的 *repl* 参数中唯一的特殊字符是 \<ampersand\>（`'&'`）字符，在其前面加上 \<backslash\>（反斜杠）字符用于关闭其特殊含义。

ISO POSIX-2:1993 标准中的描述引入了这样的行为：\<backslash\>（反斜杠）字符是另一个特殊字符，并且是否有任何其他特殊字符是未指定的（unspecified）。此描述引入了几个可移植性问题，其中一些在下面描述，因此已被更符合历史的描述取代。其中一些问题包括：

- 历史上，要创建替换字符串，脚本可以使用 `gsub(ERE, "\\&")`，但根据 ISO POSIX-2:1993 标准的措辞，有必要使用 `gsub(ERE, "\\\\&")`。这里的 \<backslash\> 字符被加倍，因为所有字符串字面量都受词法分析的影响，这将在传递给 `gsub` 之前将每对 \<backslash\> 字符减少为单个 \<backslash\>。
- 由于特殊字符是什么是未指定的，为了可移植脚本保证字符被字面打印，每个字符都必须在其前面加上 \<backslash\>。（例如，可移植脚本必须使用 `gsub(ERE, "\\h\\i")` 来产生替换字符串 `"hi"`。）

ISO POSIX-2:1993 标准中比较的描述没有正确描述历史实践，因为数值字符串被作为数字比较的方式。当前规则导致以下代码：

```
if (0 == "000")
    print "strange, but true"
else
    print "not true"
```

进行数值比较，导致 `if` 成功。凭直觉应该很明显这是不正确的行为，事实上，没有历史 *awk* 实现真正这样表现。

为了修复此问题，*数值字符串*的定义被增强为仅包括那些从特定情况（主要是外部来源）获得的值，在这些情况下无法明确确定该值旨在是字符串还是数值。

被赋予数值字符串的变量也应被视为数值字符串。（例如，数值字符串的概念可以跨赋值传播。）在比较中，所有具有未初始化值的变量都应被视为求值为数值零的数值操作数。

未初始化的变量包括所有类型的变量，包括标量、数组元素和字段。在“变量与特殊变量 (Variables and Special Variables)”一节中未初始化值的定义是必要的，以描述放在未初始化变量和有效（例如，`$NF` 之前的字段）但其中没有字符的字段上的值，并描述这些变量在比较中应如何使用。有效字段（如 `$1`）中没有任何字符，可以从 `"\t\t"` 的输入行获得，当 `FS='\t'` 时。历史上，比较（`$1<10`）在将 `$1` 求值为零后按数值进行。

“... 也应具有数值字符串的数值”这一短语已从 ISO POSIX-2:1993 标准的几个部分中删除，因为它指定了不必要的实现细节。POSIX.1-2024 不必规定这些对象被赋予两个不同的值。只需规定这些对象可以根据上下文求值为两个不同的值。

历史 *awk* 实现不解析十六进制整数或浮点常量，如 `"0xa"` 和 `"0xap0"`。由于疏忽，本标准的 2001 到 2004 版本要求支持十六进制浮点常量。这是由于引用了 [*atof*()](../functions/atof.html)。本版本的标准允许但不要求实现使用 [*atof*()](../functions/atof.html)，并包含如何识别浮点数的描述作为匹配历史行为的替代方案。此更改的意图是允许实现根据 ISO/IEC 9899:1990 标准或 ISO/IEC 9899:1999 标准识别浮点常量，并允许（但不要求）实现识别十六进制整数常量。

历史 *awk* 实现不支持*数值字符串*中的浮点无穷大和 NaN；例如，`"-INF"` 和 `"NaN"`。但是，使用 [*atof*()](../functions/atof.html) 或 [*strtod*()](../functions/strtod.html) 函数进行转换的实现，如果它们使用 ISO/IEC 9899:1999 标准版本的函数而不是 ISO/IEC 9899:1990 标准版本，则获得了对这些值的支持。由于疏忽，本标准的 2001 到 2004 版本不允许支持无穷大和 NaN，但在本修订版中允许（但不要求）支持。这是 *awk* 程序行为的静默更改；例如，在 POSIX locale 中，表达式：

```
("-INF" + 0 < 0)
```

以前具有值 0，因为 `"-INF"` 转换为 0，但现在可能具有值 0 或 1。

一次一个地删除数组的所有元素，通过：

```
for (index in array)
    delete array[index]
```

通常效率不高。本标准要求 `delete array` 具有相同的效果，这在大多数实现中被支持为更高效的操作。也可以使用 `split("", array)` 来实现相同的效果和效率。

## 未来方向 (FUTURE DIRECTIONS)

如果此实用程序被指示创建包含任何具有 \<newline\>（换行符）字符编码值的字节的新目录项，鼓励实现将此视为错误。本标准的未来版本可能要求实现将此视为错误。

本标准的未来版本可能要求 `srand` 接受任何数值，并通过取提供的值、将其转换为整数并计算该整数值对 2^n 取模来计算种子，其中 *n* 是大于或等于 32 的实现定义（implementation-defined）值。

本标准的未来版本可能要求 `rand` 函数的初始种子（如果未调用 `srand` 则使用的种子值）是 0 到 2^n-1（含）之间的整数，其中 *n* 是大于或等于 32 的实现定义值。此外，初始种子值可能被要求是（伪）随机值，使得两次 *awk* 调用不太可能发出相同的随机值序列（除非通过 `srand` 将种子显式设置为相同的值）。

本标准的未来版本可能定义一个新的 `posix_srand` 函数，使应用程序作者能够将种子设置为系统生成的（伪）随机值。或者，`srand` 函数的规范可能被更改，以提供某种方式将默认种子值设置为（伪）随机值。

## 参见 (SEE ALSO)

[*1.3 文法约定*](../utilities/V3_chap01.html#tag_18_03)、[*grep*](../utilities/grep.html)、[*lex*](../utilities/lex.html)、[*sed*](../utilities/sed.html)

XBD [*5. 文件格式记号*](../basedefs/V1_chap05.html#tag_05)、[*6.1 便携字符集*](../basedefs/V1_chap06.html#tag_06_01)、[*8. 环境变量*](../basedefs/V1_chap08.html#tag_08)、[*9. 正则表达式*](../basedefs/V1_chap09.html#tag_09)、[*12.2 实用程序语法准则*](../basedefs/V1_chap12.html#tag_12_02)

XSH [*atof*()](../functions/atof.html)、[*exec*](../functions/exec.html)、[*isspace*()](../functions/isspace.html)、[*popen*()](../functions/popen.html)、[*setlocale*()](../functions/setlocale.html)、[*strtod*()](../functions/strtod.html)

## 变更历史 (CHANGE HISTORY)

首次发布于 Issue 2。

### Issue 5

添加了“未来方向 (FUTURE DIRECTIONS)”一节。

### Issue 6

*awk* 实用程序与 IEEE P1003.2b 草案标准保持一致。

规范文本被改写，以避免对应用要求使用“must”一词。

应用了 IEEE PASC 解释 1003.2 #211，在 `sub` 字符串函数的描述中添加了句子“两个连续 \<backslash\>（反斜杠）字符的出现应被解释为单个字面 \<backslash\> 字符。”

### Issue 7

应用了 PASC 解释 1003.2-1992 #107 (SD5-XCU-ERN-73)，更新了 `OFS` 变量的描述。

应用了 Austin Group 解释 1003.1-2001 #189。

应用了 Austin Group 解释 1003.1-2001 #201，允许实现支持无穷大和 NaN。

应用了 SD5-XCU-ERN-79，恢复了“awk 中按优先级递减的表达式 (Expressions in Decreasing Precedence in awk)”中的水平线，并应用了 SD5-XCU-ERN-80，更改了一些表项的顺序。

应用了 SD5-XCU-ERN-87，更新了“语法 (Grammar)”的描述文本。

应用了 SD5-XCU-ERN-97，更新了“概要 (SYNOPSIS)”。

“扩展描述 (EXTENDED DESCRIPTION)”被更改，使十六进制整数和浮点常量的支持变为可选的。

应用了 POSIX.1-2008 技术勘误 1：XCU/TC1-2008/0057 [224]、XCU/TC1-2008/0058 [454]、XCU/TC1-2008/0059 [224]、XCU/TC1-2008/0060 [224]、XCU/TC1-2008/0061 [254]、XCU/TC1-2008/0062 [254]、XCU/TC1-2008/0063 [224] 和 XCU/TC1-2008/0064 [454]。

应用了 POSIX.1-2008 技术勘误 2：XCU/TC2-2008/0058 [584]、XCU/TC2-2008/0059 [963]、XCU/TC2-2008/0060 [226]、XCU/TC2-2008/0061 [663]、XCU/TC2-2008/0062 [963]、XCU/TC2-2008/0063 [226] 和 XCU/TC2-2008/0064 [963]。

### Issue 8

应用了 Austin Group Defect 251，鼓励实现禁止创建包含任何具有 \<newline\>（换行符）字符编码值的字节的文件名。

应用了 Austin Group Defects 544 和 1136，要求实现接受不带下标数组名的 `delete` 语句。

应用了 Austin Group Defect 607，添加了 `nextfile` 语句。

应用了 Austin Group Defect 634，添加了 `fflush` 函数。

应用了 Austin Group Defects 974 和 1451，澄清了 `ARGC`、`ARGV` 和 `FILENAME` 变量，并添加到“应用程序用法 (APPLICATION USAGE)”。

应用了 Austin Group Defect 983，更改了 `rand` 和 `srand` 函数以及“未来方向 (FUTURE DIRECTIONS)”一节的描述。

应用了 Austin Group Defect 1070，要求 `"!="` 和 `"=="` 运算符通过检查字符串是否相同（而不是检查它们是否整理相等）来执行字符串比较。

应用了 Austin Group Defect 1105，澄清了 \<backslash\>（反斜杠）转义的要求。

应用了 Austin Group Defect 1122，更改了 *NLSPATH* 的描述。

应用了 Austin Group Defect 1198，要求当两个操作数都具有作为数值字符串的字符串值时按数值进行比较。

应用了 Austin Group Defect 1277，澄清了在 ERE 中使用 \<slash\>（斜杠）字符仅当它在词法 token `ERE` 内时才需要转义。

应用了 Austin Group Defect 1320，澄清了 ERE 匹配针对输入记录的条件。

应用了 Austin Group Defect 1395，更改了字符串到数字转换的要求。

应用了 Austin Group Defect 1468，澄清了当 `FS` 是能够匹配空字符串的 ERE 时的行为。

应用了 Austin Group Defect 1566，规定了 `length` 函数在传入数组参数时的行为。

---

*提供信息文本结束。*

[opt-start]: ../6.awk/.pic/opt-start.gif
[opt-end]: ../6.awk/.pic/opt-end.gif
