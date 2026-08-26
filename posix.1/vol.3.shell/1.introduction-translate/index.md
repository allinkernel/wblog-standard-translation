## 1. 引言 (Introduction)

> POSIX.1-2024《Shell 与实用程序》卷（XCU，Shell and Utilities）描述了 POSIX 一致（POSIX-conformant）系统提供给应用程序的命令（commands）与实用程序（utilities）。
>
> 翻译说明：本译文为**中文直译**，与英文原文（`1.introduction/index.md`）**逐段、逐条、逐层对应**，结构（标题层级、表格、列表、定义列表、代码块）完全镜像原文，便于中英对照阅读。

### 1.1 与其他文档的关系 (Relationship to Other Documents)

#### 1.1.1 系统接口 (System Interfaces)

本小节描述了 POSIX.1-2024《系统接口》卷所提供的、被假定为在符合本卷 POSIX.1-2024 的所有系统上**全局可用**的部分特性。本小节并不试图详述《系统接口》卷中定义的全部、为本卷所定义的各个实用程序所需的特性；实用程序与函数描述会指出提供各自所需特性时需要的附加功能。

以下各小节描述了经常使用的概念。其中许多概念在 POSIX.1-2024《基础定义》卷中有描述。在适当时，实用程序和函数描述的陈述覆盖（override）这些默认值。

##### 1.1.1.1 进程属性 (Process Attributes)

以下进程属性，如《系统接口》卷所述，被假定为在本卷 POSIX.1-2024 中对所有进程都受支持：

<table cellpadding="3">
<tr valign="top">
<td align="left">
<p><br>控制终端（Controlling Terminal）<br>当前工作目录（Current Working Directory）<br>有效组 ID（Effective Group ID）<br>有效用户 ID（Effective User ID）<br>文件描述符（File Descriptors）<br>文件模式创建掩码（File Mode Creation Mask）<br>进程组 ID（Process Group ID）<br>进程 ID（Process ID）<br></p>
</td>
<td align="left">
<p><br>真实组 ID（Real Group ID）<br>真实用户 ID（Real User ID）<br>根目录（Root Directory）<br>保存的设置组 ID（Saved Set-Group-ID）<br>保存的设置用户 ID（Saved Set-User-ID）<br>会话成员资格（Session Membership）<br>补充组 ID（Supplementary Group IDs）<br></p>
</td>
</tr>
</table>

一致实现（conforming implementation）可包含额外的进程属性。

##### 1.1.1.2 进程的并发执行 (Concurrent Execution of Processes)

在《系统接口》卷中定义的 [*fork*()](../functions/fork.html) 函数的以下功能，应在符合本卷 POSIX.1-2024 的所有系统上可用：

1.  独立进程应能够在互不终止对方的情况下独立执行。
2.  进程应能够创建一个新进程，该新进程具有 [1.1.1.1 进程属性](#tag_18_01_01_01) 中所引用的全部属性，其确定方式依据《系统接口》卷中定义的 [*fork*()](../functions/fork.html) 函数调用、继之以子进程中调用《系统接口》卷中定义的某个 *exec* 函数的语义。

##### 1.1.1.3 文件访问权限 (File Access Permissions)

XBD [*4.7 文件访问权限*](../basedefs/V1_chap04.html#tag_04_07) 所描述的文件访问控制机制应适用于符合本卷 POSIX.1-2024 的实现上的所有文件。

##### 1.1.1.4 文件的读、写与创建 (File Read, Write, and Creation)

如果要写入一个不存在的文件，除非实用程序描述另有说明，否则应按下文所述创建该文件。

当创建一个不存在的文件时，除非实用程序或函数描述另有说明，否则《系统接口》卷中定义的以下特性应适用：

1.  文件的用户 ID 应设置为调用进程的有效用户 ID。
2.  文件的组 ID 应设置为调用进程的有效组 ID，或创建该文件的目录的组 ID。
3.  如果该文件是普通文件（regular file），文件的权限位应设置为：S_IROTH | S_IWOTH | S_IRGRP | S_IWGRP | S_IRUSR | S_IWUSR（参见 XBD [*14. 头文件*](../basedefs/V1_chap14.html#tag_14)、[*\<sys/stat.h\>*](../basedefs/sys_stat.h.html) 中"文件模式（File Modes）"的描述），但进程的文件模式创建掩码所指定的位应被清除。如果该文件是目录，权限位应设置为：S_IRWXU | S_IRWXG | S_IRWXO，但进程的文件模式创建掩码所指定的位应被清除。
4.  文件的最后数据访问、最后数据修改和最后文件状态更改时间戳，应按 XBD [*4.12 文件时间更新*](../basedefs/V1_chap04.html#tag_04_12) 的规定更新。
5.  如果该文件是目录，它应为空目录；否则，该文件的长度应为零。
6.  如果该文件是符号链接（symbolic link），除非符号链接将被创建的目录中 `{POSIX2_SYMLINKS}` 变量生效，否则其效果是未定义的（undefined）。
7.  除非另有规定，创建的文件应为普通文件。

当试图创建一个已经存在的文件时，除非实用程序描述另有说明，否则实用程序应采取 [创建已存在文件时的动作](#tagtcjh_9) 中对应于该实用程序试图创建的文件的类型以及现有文件的类型的动作。

**表：创建已存在文件时的动作 (Actions when Creating a File that Already Exists)**

<table border="1" cellpadding="3" align="center">
<tr valign="top">
<th colspan="2" align="center"><p><b>&nbsp;</b></p></th>
<th colspan="11" align="center"><p><b>新建类型（New Type）</b></p></th>
<th align="center"><p><b>&nbsp;</b></p></th>
</tr>
<tr valign="top">
<th colspan="2" align="center"><p><b>现有类型（Existing Type）</b></p></th>
<th align="center"><p><b>B</b></p></th>
<th align="center"><p><b>C</b></p></th>
<th align="center"><p><b>D</b></p></th>
<th align="center"><p><b>F</b></p></th>
<th align="center"><p><b>L</b></p></th>
<th align="center"><p><b>M</b></p></th>
<th align="center"><p><b>P</b></p></th>
<th align="center"><p><b>Q</b></p></th>
<th align="center"><p><b>R</b></p></th>
<th align="center"><p><b>S</b></p></th>
<th align="center"><p><b>T</b></p></th>
<th align="center"><p><b>创建新文件的函数（Function Creating New）</b></p></th>
</tr>
<tr valign="top">
<td align="left"><p>B</p></td>
<td align="left"><p>块特殊（Block Special）</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>U</p></td>
<td align="center"><p>U</p></td>
<td align="center"><p>U</p></td>
<td align="center"><p>OF</p></td>
<td align="center"><p>U</p></td>
<td align="center"><p>U</p></td>
<td align="left"><p><i>mknod</i>()**</p></td>
</tr>
<tr valign="top">
<td align="left"><p>C</p></td>
<td align="left"><p>字符特殊（Character Special）</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>U</p></td>
<td align="center"><p>U</p></td>
<td align="center"><p>U</p></td>
<td align="center"><p>OF</p></td>
<td align="center"><p>U</p></td>
<td align="center"><p>U</p></td>
<td align="left"><p><i>mknod</i>()**</p></td>
</tr>
<tr valign="top">
<td align="left"><p>D</p></td>
<td align="left"><p>目录（Directory）</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>U</p></td>
<td align="left"><p><i>mkdir</i>()</p></td>
</tr>
<tr valign="top">
<td align="left"><p>F</p></td>
<td align="left"><p>FIFO 特殊文件（FIFO Special File）</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>O</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>U</p></td>
<td align="left"><p><i>mkfifo</i>()</p></td>
</tr>
<tr valign="top">
<td align="left"><p>L</p></td>
<td align="left"><p>符号链接（Symbolic Link）</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>FL</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>U</p></td>
<td align="left"><p><i>symlink</i>()</p></td>
</tr>
<tr valign="top">
<td align="left"><p>M</p></td>
<td align="left"><p>共享内存（Shared Memory）</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>U</p></td>
<td align="left"><p><i>shm_open</i>()</p></td>
</tr>
<tr valign="top">
<td align="left"><p>P</p></td>
<td align="left"><p>信号量（Semaphore）</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>U</p></td>
<td align="left"><p><i>sem_open</i>()</p></td>
</tr>
<tr valign="top">
<td align="left"><p>Q</p></td>
<td align="left"><p>消息队列（Message Queue）</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>U</p></td>
<td align="left"><p><i>mq_open</i>()</p></td>
</tr>
<tr valign="top">
<td align="left"><p>R</p></td>
<td align="left"><p>普通文件（Regular File）</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>RF</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>U</p></td>
<td align="left"><p><i>open</i>()</p></td>
</tr>
<tr valign="top">
<td align="left"><p>S</p></td>
<td align="left"><p>套接字（Socket）</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>—</p></td>
<td align="center"><p>U</p></td>
<td align="left"><p><i>bind</i>()</p></td>
</tr>
<tr valign="top">
<td align="left"><p>T</p></td>
<td align="left"><p>类型化内存（Typed Memory）</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>F</p></td>
<td align="center"><p>U</p></td>
<td align="center"><p>U</p></td>
<td align="center"><p>U</p></td>
<td align="center"><p>U</p></td>
<td align="center"><p>U</p></td>
<td align="center"><p>U</p></td>
<td align="left"><p>&#42;</p></td>
</tr>
</table>

[*创建已存在文件时的动作*](#tagtcjh_9) 中使用了以下代码：

`F`

:   失败（Fail）。创建新文件的尝试应失败，且实用程序应根据其描述，或者继续其操作，或者以指示发生错误的退出状态立即退出。

`FL`

:   跟随链接（Follow link）。除非另有规定，应按路径名解析（pathname resolution）的规定跟随符号链接，所执行的操作应如同该符号链接的目标（在所有解析之后）被直接命名一样。如果符号链接的目标不存在，则应如同直接命名了那个不存在的目标一样。

`O`

:   打开 FIFO（Open FIFO）。当试图创建普通文件而现有文件是 FIFO 特殊文件时：
    1.  如果 FIFO 尚未为读而打开，该尝试应阻塞，直到 FIFO 为读而打开。
    2.  一旦 FIFO 为读而打开，实用程序应为写而打开该 FIFO 并继续其操作。

`OF`

:   命名的文件应按照为该文件类型定义的后果被打开。

`RF`

:   普通文件（Regular file）。当试图创建普通文件而现有文件是普通文件时：
    1.  文件的用户 ID、组 ID 和权限位不应被更改。
    2.  文件应被截断为零长度。
    3.  最后数据修改和最后文件状态更改时间戳应标记为更新。

`—`

:   除非实用程序描述指定，否则其效果是实现定义的（implementation-defined）。

`U`

:   除非实用程序描述指定，否则其效果是未指定的（unspecified）。

`*`

:   不存在可移植的方式创建此类型的文件。

`**`

:   不可移植（Not portable）。

当要追加（append）文件时，文件应以一种等价于在《系统接口》卷中定义的 [*open*()](../functions/open.html) 函数中使用 O_APPEND 标志、而不使用 O_TRUNC 标志的方式打开。

当要读或写文件时，文件应以对应于要执行操作（operation）的访问模式打开。如果文件访问权限拒绝访问，请求的操作应失败。

##### 1.1.1.5 文件移除 (File Removal)

当移除任何进程的根目录或当前工作目录时，其效果是实现定义的（implementation-defined）。如果文件访问权限拒绝访问，请求的操作应失败。否则，当移除一个文件时：

1.  文件的目录项应从文件系统中移除。
2.  文件的链接计数（link count）应递减。
3.  如果该文件是空目录（参见 XBD [*3.119 空目录*](../basedefs/V1_chap03.html#tag_03_119)）：
    a.  如果没有进程打开该目录，该目录占用的空间应被释放，且该目录不再可访问。
    b.  如果一个或多个进程打开了该目录，该目录的内容应被保留，直到对该文件的所有引用都被关闭。
4.  如果该文件是非空目录，最后文件状态更改时间戳应标记为更新。
5.  如果该文件不是目录：
    a.  如果链接计数变为零：
        i.  如果没有进程打开该文件，该文件占用的空间应被释放，且该文件不再可访问。
        ii. 如果一个或多个进程打开了该文件，该文件的内容应被保留，直到对该文件的所有引用都被关闭。
    b.  如果链接计数未减为零，最后文件状态更改时间戳应标记为更新。
6.  包含该文件的目录的最后数据修改和最后文件状态更改时间戳应标记为更新。

##### 1.1.1.6 文件时间值 (File Time Values)

所有文件应具有 XBD [*4.12 文件时间更新*](../basedefs/V1_chap04.html#tag_04_12) 所描述的三个时间值。

##### 1.1.1.7 文件内容 (File Contents)

当引用文件的内容（*pathname*）时，这意指执行《系统接口》卷中定义的以下操作中的 [*read*()](../functions/read.html) 函数调用时，放入 *buf* 所指向空间中的所有数据的等价物：

```
while (read (fildes, buf, nbytes) > 0)
    ;
```

如果文件由路径名 *pathname* 指示，文件描述符应通过《系统接口》卷中定义的以下操作的等价物来确定：

```
fildes = open (pathname, O_RDONLY);
```

上述序列中 *nbytes* 的值是未指定的（unspecified）；如果文件的类型使得 [*read*()](../functions/read.html) 返回的数据会因不同的值而变化，则该值应是导致返回最多数据的那种值。

如果 [*read*()](../functions/read.html) 函数调用会返回错误，则文件内容是否被认为包含文件中错误返回位置之后偏移处的任何数据，是未指定的。

##### 1.1.1.8 路径名解析 (Pathname Resolution)

XBD [*4.16 路径名解析*](../basedefs/V1_chap04.html#tag_04_16) 所描述的路径名解析算法应被符合本卷 POSIX.1-2024 的实现所使用；另见 XBD [*4.8 文件层级*](../basedefs/V1_chap04.html#tag_04_08)。

##### 1.1.1.9 更改当前工作目录 (Changing the Current Working Directory)

当要更改当前工作目录（参见 XBD [*3.94 当前工作目录*](../basedefs/V1_chap03.html#tag_03_94)）时，除非实用程序或函数描述另有说明，否则该操作应成功，除非以新工作目录路径名作为参数调用《系统接口》卷中定义的 [*chdir*()](../functions/chdir.html) 函数会失败。

##### 1.1.1.10 建立区域设置 (Establish the Locale)

《系统接口》卷中定义的 [*setlocale*()](../functions/setlocale.html) 函数的功能应在符合本卷 POSIX.1-2024 的所有系统上可用；也就是说，需要建立国际操作环境（international operating environment）能力的实用程序应被允许设置国际环境的指定类别（category）。

##### 1.1.1.11 与函数等价的动作 (Actions Equivalent to Functions)

某些实用程序描述规定，实用程序执行与《系统接口》卷中定义的函数等价的动作。此类规定只要求**外部效果**（external effects）等价，而不要求实用程序内部、且仅对实用程序可见的任何效果等价。

#### 1.1.2 源自 ISO C 标准的概念 (Concepts Derived from the ISO C Standard)

某些标准实用程序使用它们自己的过程语言（procedure language）和算术语言（arithmetic language）执行复杂的数据操作，如其 EXTENDED DESCRIPTION 或 OPERANDS 部分所定义。除非另有说明，算术与语义概念（精度、类型转换、控制流等）应等价于 ISO C 标准中定义的、如下各节所描述的概念。注意：本标准不要求标准实用程序用任何特定编程语言实现。

##### 1.1.2.1 算术精度与运算 (Arithmetic Precision and Operations)

本卷 POSIX.1-2024 所列标准实用程序使用的整数变量与常量（包括操作数和选项参数的值）应实现为等价于 ISO C 标准的 **signed long**（有符号长整型）数据类型；浮点应实现为等价于 ISO C 标准的 **double**（双精度）类型。类型之间的转换应按 ISO C 标准的描述进行。所有变量，如果未被应用程序的输入另行赋值，应初始化为零。

算术运算符和控制流关键字应实现为等价于所引用的 ISO C 标准节中的运算符与关键字，如[选定的 ISO C 标准运算符与控制流关键字](#tagtcjh_10)所列。

**注意：**

:   逗号运算符（ISO C 标准第 6.5.17 节）有意不包含在表中。实现不需要支持它。

<table border="1" cellpadding="3" align="center">
<tr valign="top">
<th align="center"><p><b>运算 (Operation)</b></p></th>
<th align="center"><p><b>ISO C 标准等价引用 (ISO C Standard Equivalent Reference)</b></p></th>
</tr>
<tr valign="top">
<td align="left"><p>()</p></td>
<td align="left"><p>第 6.5.1 节，主表达式（Primary Expressions）</p></td>
</tr>
<tr valign="top">
<td align="left"><p>后缀 <code>++</code><br>后缀 <code>--</code></p></td>
<td align="left"><p>第 6.5.2 节，后缀运算符（Postfix Operators）</p></td>
</tr>
<tr valign="top">
<td align="left"><p>一元 <code>+</code><br>一元 <code>-</code><br>前缀 <code>++</code><br>前缀 <code>--</code><br><code>~</code><br><code>!</code><br><i>sizeof</i>()</p></td>
<td align="left"><p>第 6.5.3 节，一元运算符（Unary Operators）</p></td>
</tr>
<tr valign="top">
<td align="left"><p><code>&#42;</code><br><code>/</code><br><code>%</code></p></td>
<td align="left"><p>第 6.5.5 节，乘法运算符（Multiplicative Operators）</p></td>
</tr>
<tr valign="top">
<td align="left"><p><code>+</code><br><code>-</code></p></td>
<td align="left"><p>第 6.5.6 节，加法运算符（Additive Operators）</p></td>
</tr>
<tr valign="top">
<td align="left"><p><code>&lt;&lt;</code><br><code>&gt;&gt;</code></p></td>
<td align="left"><p>第 6.5.7 节，按位移位运算符（Bitwise Shift Operators）</p></td>
</tr>
<tr valign="top">
<td align="left"><p><code>&lt;</code>, <code>&lt;=</code><br><code>&gt;</code>, <code>&gt;=</code></p></td>
<td align="left"><p>第 6.5.8 节，关系运算符（Relational Operators）</p></td>
</tr>
<tr valign="top">
<td align="left"><p><code>==</code><br><code>!=</code></p></td>
<td align="left"><p>第 6.5.9 节，相等性运算符（Equality Operators）</p></td>
</tr>
<tr valign="top">
<td align="left"><p><code>&amp;</code></p></td>
<td align="left"><p>第 6.5.10 节，按位与运算符（Bitwise AND Operator）</p></td>
</tr>
<tr valign="top">
<td align="left"><p><code>^</code></p></td>
<td align="left"><p>第 6.5.11 节，按位异或运算符（Bitwise Exclusive OR Operator）</p></td>
</tr>
<tr valign="top">
<td align="left"><p><code>|</code></p></td>
<td align="left"><p>第 6.5.12 节，按位或运算符（Bitwise Inclusive OR Operator）</p></td>
</tr>
<tr valign="top">
<td align="left"><p><code>&amp;&amp;</code></p></td>
<td align="left"><p>第 6.5.13 节，逻辑与运算符（Logical AND Operator）</p></td>
</tr>
<tr valign="top">
<td align="left"><p><code>||</code></p></td>
<td align="left"><p>第 6.5.14 节，逻辑或运算符（Logical OR Operator）</p></td>
</tr>
<tr valign="top">
<td align="left"><p><i>expr</i>?<i>expr</i>:<i>expr</i></p></td>
<td align="left"><p>第 6.5.15 节，条件运算符（Conditional Operator）</p></td>
</tr>
<tr valign="top">
<td align="left"><p><code>=</code>, <code>&#42;=</code>, <code>/=</code>, <code>%=</code>, <code>+=</code>, <code>-=</code><br><code>&lt;&lt;=</code>, <code>&gt;&gt;=</code>, <code>&amp;=</code>, <code>^=</code>, <code>|=</code></p></td>
<td align="left"><p>第 6.5.16 节，赋值运算符（Assignment Operators）</p></td>
</tr>
<tr valign="top">
<td align="left"><p><b>if</b> ()<br><b>if</b> () ... <b>else</b><br><b>switch</b> ()</p></td>
<td align="left"><p>第 6.8.4 节，选择语句（Selection Statements）</p></td>
</tr>
<tr valign="top">
<td align="left"><p><b>while</b> ()<br><b>do</b> ... <b>while</b> ()<br><b>for</b> ()</p></td>
<td align="left"><p>第 6.8.5 节，迭代语句（Iteration Statements）</p></td>
</tr>
<tr valign="top">
<td align="left"><p><b>goto</b><br><b>continue</b><br><b>break</b><br><b>return</b></p></td>
<td align="left"><p>第 6.8.6 节，跳转语句（Jump Statements）</p></td>
</tr>
</table>

算术表达式的求值应等价于 ISO C 标准第 6.5 节"表达式（Expressions）"中所描述的求值。

##### 1.1.2.2 数学函数 (Mathematical Functions)

任何与 ISO C 标准以下各节中的函数同名的数学函数：

-   第 7.12 节，数学，`<math.h>`
-   第 7.22.2 节，伪随机序列生成函数（Pseudo-Random Sequence Generation Functions）

应实现为返回与调用 ISO C 标准中描述的相应函数所返回的结果等价的结果。

### 1.2 实用程序限制 (Utility Limits)

本节列出特定实现所施加的规模限制（magnitude limitations）。本卷 POSIX.1-2024 使用花括号记法（braces notation）{LIMIT} 来指示这些值，但花括号不是名称的一部分。

<table border="1" cellpadding="3" align="center">
<tr valign="top">
<th align="center"><p><b>名称 (Name)</b></p></th>
<th align="center"><p><b>描述 (Description)</b></p></th>
<th align="center"><p><b>值 (Value)</b></p></th>
</tr>
<tr valign="top"><td align="left"><p><code>{POSIX2&#95;BC&#95;BASE&#95;MAX}</code></p></td><td align="left"><p>&lt;a href=&#34;../utilities/bc.html&#34;&gt;<i>bc</i></a> 实用程序允许的最大 <i>obase</i> 值。</p></td><td align="center"><p>99</p></td></tr>
<tr valign="top"><td align="left"><p><code>{POSIX2&#95;BC&#95;DIM&#95;MAX}</code></p></td><td align="left"><p>&lt;a href=&#34;../utilities/bc.html&#34;&gt;<i>bc</i></a> 实用程序允许的数组中元素的最大数量。</p></td><td align="center"><p>2048</p></td></tr>
<tr valign="top"><td align="left"><p><code>{POSIX2&#95;BC&#95;SCALE&#95;MAX}</code></p></td><td align="left"><p>&lt;a href=&#34;../utilities/bc.html&#34;&gt;<i>bc</i></a> 实用程序允许的最大 <i>scale</i> 值。</p></td><td align="center"><p>99</p></td></tr>
<tr valign="top"><td align="left"><p><code>{POSIX2&#95;BC&#95;STRING&#95;MAX}</code></p></td><td align="left"><p>&lt;a href=&#34;../utilities/bc.html&#34;&gt;<i>bc</i></a> 实用程序接受的字符串常量的最大长度。</p></td><td align="center"><p>1000</p></td></tr>
<tr valign="top"><td align="left"><p><code>{POSIX2&#95;COLL&#95;WEIGHTS&#95;MAX}</code></p></td><td align="left"><p>区域设置定义文件中 <code>LC&#95;COLLATE</code> 的 <b>order</b> 关键字的条目可被赋予的权值（weights）的最大数量；参见 XBD &lt;a href=&#34;../basedefs/V1&#95;chap07.html#tag&#95;07&#95;03&#95;02&#34;&gt;<i>7.3.2 LC&#95;COLLATE</i></a> 中的 <b>order&#95;start</b> 关键字。</p></td><td align="center"><p>2</p></td></tr>
<tr valign="top"><td align="left"><p><code>{POSIX2&#95;EXPR&#95;NEST&#95;MAX}</code></p></td><td align="left"><p>&lt;a href=&#34;../utilities/expr.html&#34;&gt;<i>expr</i></a> 实用程序允许的括号内嵌套表达式的最大数量。</p></td><td align="center"><p>32</p></td></tr>
<tr valign="top"><td align="left"><p><code>{POSIX2&#95;LINE&#95;MAX}</code></p></td><td align="left"><p>除非另有说明，当实用程序被描述为处理文本文件时，实用程序输入行（标准输入或其他文件）的最大长度（以字节计）。该长度包含结尾的 &#92;&lt;newline&#92;&gt; 的空间。</p></td><td align="center"><p>2048</p></td></tr>
<tr valign="top"><td align="left"><p><code>{POSIX&#95;RE&#95;DUP&#95;MAX}</code></p></td><td align="left"><p>BRE 或 ERE 区间表达式（interval expression）的最大重复次数；参见 XBD &lt;a href=&#34;../basedefs/V1&#95;chap09.html#tag&#95;09&#95;03&#95;06&#34;&gt;<i>9.3.6 匹配多个字符的 BRE</i></a> 和 &lt;a href=&#34;../basedefs/V1&#95;chap09.html#tag&#95;09&#95;04&#95;06&#34;&gt;<i>9.4.6 匹配多个字符的 ERE</i></a>。</p></td><td align="center"><p>255</p></td></tr>
</table>

<table border="1" cellpadding="3" align="center">
<tr valign="top">
<th align="center"><p><b>名称 (Name)</b></p></th>
<th align="center"><p><b>描述 (Description)</b></p></th>
<th align="center"><p><b>最小值 (Minimum Value)</b></p></th>
</tr>
<tr valign="top"><td align="left"><p><code>{BC&#95;BASE&#95;MAX}</code></p></td><td align="left"><p>&lt;a href=&#34;../utilities/bc.html&#34;&gt;<i>bc</i></a> 实用程序允许的最大 <i>obase</i> 值。</p></td><td align="center"><p><code>{POSIX2&#95;BC&#95;BASE&#95;MAX}</code></p></td></tr>
<tr valign="top"><td align="left"><p><code>{BC&#95;DIM&#95;MAX}</code></p></td><td align="left"><p>&lt;a href=&#34;../utilities/bc.html&#34;&gt;<i>bc</i></a> 实用程序允许的数组中元素的最大数量。</p></td><td align="center"><p><code>{POSIX2&#95;BC&#95;DIM&#95;MAX}</code></p></td></tr>
<tr valign="top"><td align="left"><p><code>{BC&#95;SCALE&#95;MAX}</code></p></td><td align="left"><p>&lt;a href=&#34;../utilities/bc.html&#34;&gt;<i>bc</i></a> 实用程序允许的最大 <i>scale</i> 值。</p></td><td align="center"><p><code>{POSIX2&#95;BC&#95;SCALE&#95;MAX}</code></p></td></tr>
<tr valign="top"><td align="left"><p><code>{BC&#95;STRING&#95;MAX}</code></p></td><td align="left"><p>&lt;a href=&#34;../utilities/bc.html&#34;&gt;<i>bc</i></a> 实用程序接受的字符串常量的最大长度。</p></td><td align="center"><p><code>{POSIX2&#95;BC&#95;STRING&#95;MAX}</code></p></td></tr>
<tr valign="top"><td align="left"><p><code>{COLL&#95;WEIGHTS&#95;MAX}</code></p></td><td align="left"><p>区域设置定义文件中 <code>LC&#95;COLLATE</code> 的 <b>order</b> 关键字的条目可被赋予的权值的最大数量；参见 XBD &lt;a href=&#34;../basedefs/V1&#95;chap07.html#tag&#95;07&#95;03&#95;02&#34;&gt;<i>7.3.2 LC&#95;COLLATE</i></a> 中的 <b>order&#95;start</b> 关键字。</p></td><td align="center"><p><code>{POSIX2&#95;COLL&#95;WEIGHTS&#95;MAX}</code></p></td></tr>
<tr valign="top"><td align="left"><p><code>{EXPR&#95;NEST&#95;MAX}</code></p></td><td align="left"><p>&lt;a href=&#34;../utilities/expr.html&#34;&gt;<i>expr</i></a> 实用程序允许的括号内嵌套表达式的最大数量。</p></td><td align="center"><p><code>{POSIX2&#95;EXPR&#95;NEST&#95;MAX}</code></p></td></tr>
<tr valign="top"><td align="left"><p><code>{LINE&#95;MAX}</code></p></td><td align="left"><p>除非另有说明，当实用程序被描述为处理文本文件时，实用程序输入行（标准输入或其他文件）的最大长度（以字节计）。该长度包含结尾的 &#92;&lt;newline&#92;&gt; 的空间。</p></td><td align="center"><p><code>{POSIX2&#95;LINE&#95;MAX}</code></p></td></tr>
<tr valign="top"><td align="left"><p><code>{RE&#95;DUP&#95;MAX}</code></p></td><td align="left"><p>BRE 或 ERE 区间表达式的最大重复次数；参见 XBD &lt;a href=&#34;../basedefs/V1&#95;chap09.html#tag&#95;09&#95;03&#95;06&#34;&gt;<i>9.3.6 匹配多个字符的 BRE</i></a> 和 &lt;a href=&#34;../basedefs/V1&#95;chap09.html#tag&#95;09&#95;04&#95;06&#34;&gt;<i>9.4.6 匹配多个字符的 ERE</i></a>。</p></td><td align="center"><p><code>{POSIX&#95;RE&#95;DUP&#95;MAX}</code></p></td></tr>
</table>

以下值在实现内可能是常量，也可能随路径名不同而变化。

`{POSIX2_SYMLINKS}`

:   当涉及目录时，系统支持在该目录内创建符号链接；对于非目录文件，`{POSIX2_SYMLINKS}` 的含义是未定义的（undefined）。

### 1.3 文法约定 (Grammar Conventions)

本卷 POSIX.1-2024 的部分内容以特殊的文法（grammar）记法表达。它用于描绘某些程序输入的复杂语法。该文法基于 [*yacc*](../utilities/yacc.html) 实用程序所使用的语法。然而，它并不代表完全可用的、适合程序使用的 [*yacc*](../utilities/yacc.html) 输入；词法处理（lexical processing）和所有语义要求仅以文本形式描述。该文法并非基于任何传统实现所使用的源，也未用通常需要伴随它的语义代码进行过测试。此外，这并不意味着所呈现的部分 [*yacc*](../utilities/yacc.html) 代码代表了支持实用程序内复杂语法的最有效或唯一的手段。实现可以使用其他编程语言或算法，只要所支持的语法与文法所表示的语法相同。

文法中使用了以下排版约定；它们除了帮助阅读外没有其他意义。

-   语言保留字（reserved words）的标识符以大写字母开头。（这些是文法中的终结符（terminals）；例如 **While**、**Case**。）
-   文法中终结符的标识符全部以大写字母和下划线命名；例如 **NEWLINE**、**ASSIGN_OP**、**NAME**。
-   非终结符（non-terminals）的标识符全部小写。

### 1.4 实用程序描述默认值 (Utility Description Defaults)

本节描述实用程序描述中使用的所有小节，包括：

-   该小节的预期用途（intended usage）
-   影响所有标准实用程序的全局默认值（global defaults）
-   本卷 POSIX.1-2024 中特定于个别实用程序小节的记法（notations）的含义

**NAME**

:   本小节给出实用程序的名称，并简要说明其用途。

**SYNOPSIS**

:   SYNOPSIS 小节总结了实用程序调用序列（calling sequence）的语法，包括选项、选项参数和操作数。实用程序命名标准在 XBD [*12.2 实用程序语法指南*](../basedefs/V1_chap12.html#tag_12_02) 中描述；实用程序参数的描述见 XBD [*12.1 实用程序参数语法*](../basedefs/V1_chap12.html#tag_12_01)。

**DESCRIPTION**

:   DESCRIPTION 小节描述实用程序的动作。如果实用程序有非常复杂的子命令集或自己的过程语言，还会提供 EXTENDED DESCRIPTION 小节。可选功能的大多数解释在此处省略，因为它们通常在 OPTIONS 小节中解释。

    如 [1.1.1.11 与函数等价的动作](#tag_18_01_01_11) 所述，某些函数以等价功能来描述。当引用了特定函数时，实现应提供等价的功能，包括与函数成功执行相关的副作用（side-effects）。本卷 POSIX.1-2024 通常不规定所引用的各别函数对错误和中间结果的处理。参见实用程序的 EXIT STATUS 和 CONSEQUENCES OF ERRORS 小节，以了解与实用程序遇到的错误相关的所有动作。

    除非在本小节中明确说明，标准实用程序不应被视为声明实用程序（declaration utility）。

**OPTIONS**

:   OPTIONS 小节描述实用程序选项和选项参数，以及它们如何修改实用程序的动作。带选项的标准实用程序要么完全符合 XBD [*12.2 实用程序语法指南*](../basedefs/V1_chap12.html#tag_12_02)，要么描述所有偏差。OPTIONS 与 DESCRIPTION（或 EXTENDED DESCRIPTION）小节中功能描述之间的明显分歧，总是以 OPTIONS 小节为准。

    每个使用短语“The ... utility shall conform to the Utility Syntax Guidelines ...”（...实用程序应符合实用程序语法指南...）的 OPTIONS 小节，仅指按本卷 POSIX.1-2024 规定使用该实用程序；实现扩展也应符合该指南，但可允许历史实践上的例外。

    除非实用程序描述中另有说明，当给定实现无法识别的选项，或未提供必需的选项参数时，标准实用程序应向标准错误发出诊断消息，并以指示发生错误的退出状态退出。

    本卷 POSIX.1-2024 中的所有实用程序应能够使用八位透明（eight-bit transparency）处理参数。

    **默认行为：** 当本小节列为“None.”（无）时，表示实现不需要支持任何选项。不接受选项但接受操作数的标准实用程序，应将 `"--"` 识别为要丢弃的第一个参数。

    要求识别 `"--"` 是因为一致应用程序需要一种方式，使其操作数免受实现可能作为扩展提供的任意选项的影响。例如，如果标准实用程序 *foo* 被列为不接受选项，而应用程序需要给它一个前导 \<hyphen-minus\> 的路径名，则可以安全地这样做：

    ```
    foo -- -myfile
    ```

    从而避免 **-m** 被用作扩展时带来的任何问题。

**OPERANDS**

:   OPERANDS 小节描述实用程序操作数，以及它们如何影响实用程序的动作。OPERANDS 与 DESCRIPTION（或 EXTENDED DESCRIPTION）小节中功能描述之间的明显分歧，应以 OPERANDS 小节为准。

    如果命名文件的操作数可以指定为 `'-'`（表示使用标准输入而不是命名文件），则在本小节中明确说明。除非另有说明，在单个命令中多次使用 `'-'` 表示标准输入会产生未指定的结果。

    除非另有说明，接受操作数的标准实用程序应按命令行中规定的顺序处理这些操作数。

    **默认行为：** 当本小节列为“None.”（无）时，表示实现不需要支持任何操作数。

**STDIN**

:   STDIN 小节描述实用程序的标准输入。本小节经常只是对以下小节的引用，因为许多实用程序以相同方式对待标准输入和输入文件。除非另有说明，INPUT FILES 小节中描述的所有限制也应适用于本小节。

    将终端用于标准输入，会使任何读取标准输入的标准实用程序在后台使用时停止。因此，应用程序不应在要置于后台的脚本中使用交互式功能。

    标准实用程序的指定标准输入格式，不应依赖于本卷 POSIX.1-2024 中定义的环境变量的存在或值，除非本卷 POSIX.1-2024 另有规定。

    **默认行为：** 当本小节列为“Not used.”（不使用）时，表示当按本卷 POSIX.1-2024 描述使用实用程序时，不应读取标准输入。

**INPUT FILES**

:   INPUT FILES 小节描述除标准输入外、实用程序用作输入的文件。它包括作为操作数和选项参数命名的文件，以及被引用的其他文件，如启动和初始化文件、数据库等。常用文件通常在一处描述，并由其他实用程序交叉引用。

    本卷 POSIX.1-2024 中的所有实用程序应能够使用八位透明处理输入文件。

    当标准实用程序读取可查找（seekable）的输入文件并在到达文件结尾之前无错误地终止时，实用程序应确保打开文件描述（open file description）中的文件偏移量正确定位在实用程序处理的最后字节之后。对于不可查找的文件，该文件的打开文件描述中文件偏移量的状态是未指定的。一致应用程序不应假定以下三个命令是等价的：

    ```
    tail -n +2 file
    (sed -n 1q; cat) < file
    cat file | (sed -n 1q; cat)
    ```

    第二个命令仅当文件可查找时才与第一个等价。第三个命令使打开文件描述中的文件偏移量处于未指定状态。其他实用程序，如 [*head*](../utilities/head.html)、[*read*](../utilities/read.html) 和 [*sh*](../utilities/sh.html)，具有类似属性。

    某些标准实用程序（如过滤器）一次一行或一块地处理输入文件，对最大输入文件大小没有限制。某些实用程序可能有不如文件空间或内存限制明显的尺寸限制。此类限制应反映某种资源限制，而不是实现者设定的任意限制。实现应记录那些受文件系统空间、可用内存和本卷 POSIX.1-2024 特别引用的其他限制之外的约束限制的实用程序，并说明约束是什么，以及指示估计何时将达到约束的方法。类似地，某些实用程序会（递归地）下潜目录树（directory tree）。实现还应记录其在目录树下潜中可能存在的、超出本卷 POSIX.1-2024 所引用限制的任何限制。

    当输入文件被描述为“文本文件”时，如果给定的输入不是来自文本文件，除非另有说明，实用程序产生未定义的结果。某些实用程序（例如 [*make*](../utilities/make.html)、[*read*](../utilities/read.html)、[*sh*](../utilities/sh.html)）允许使用转义的 \<newline\> 约定续行；除非另有说明，实用程序无需能够从一组多个连续续行中累积超过 {LINE_MAX} 字节。因此，对于一致应用程序，一组中所有续行的总和不能超过 {LINE_MAX}。如果使用转义 \<newline\> 约定的实用程序在转义的 \<newline\> 之后立即检测到文件结尾条件，结果是未指定的。

    记录格式以类似于 C 语言函数 [*printf*()](../functions/printf.html) 使用的记法描述。参见 XBD [*5. 文件格式记法*](../basedefs/V1_chap05.html#tag_05)。格式描述旨在足够严谨，使其他应用程序能够生成这些输入文件。然而，由于 \<blank\> 可以合法地包含在标准实用程序描述的某些字段中（特别是在 POSIX locale 之外的区域设置中），这一意图并不总能实现。

    **默认行为：** 当本小节列为“None.”（无）时，表示当按本卷 POSIX.1-2024 描述使用实用程序时，不需要提供输入文件。

**ENVIRONMENT VARIABLES**

:   ENVIRONMENT VARIABLES 小节列出哪些变量影响实用程序的执行。

    本卷 POSIX.1-2024 中描述的环境变量影响每个实用程序行为的全部方式，在该实用程序的 ENVIRONMENT VARIABLES 小节中描述，并结合 XBD [*8. 环境变量*](../basedefs/V1_chap08.html#tag_08) 中描述的 *LANG*、*LC_ALL* 和 `[XSI]` *NLSPATH* 环境变量的全局影响。[译者注：原文中 “[XSI]” 之后以 opt-start.gif 与 opt-end.gif 两个小图标标示 XSI 选项内容的起止，此处以文字表示。] 本卷 POSIX.1-2024 中描述的环境变量的存在或值，不应以其他方式影响标准实用程序的指定行为。本卷 POSIX.1-2024 未描述的环境变量的存在或值对标准实用程序的任何影响，是未指定的。

    对于那些使用环境变量作为选择要执行的实用程序的手段的标准实用程序（如 [*make*](../utilities/make.html) 中的 *CC*），提供给实用程序的字符串应经受 XBD [*8. 环境变量*](../basedefs/V1_chap08.html#tag_08) 中为 *PATH* 描述的路径搜索。

    本卷 POSIX.1-2024 中的所有实用程序应能够使用八位透明处理环境变量名称和值。

    **默认行为：** 当本小节列为“None.”（无）时，表示当按本卷 POSIX.1-2024 描述使用实用程序时，实用程序的行为不受本卷 POSIX.1-2024 所描述环境变量的直接影响。

**ASYNCHRONOUS EVENTS**

:   ASYNCHRONOUS EVENTS 小节列出实用程序如何对信号等事件作出反应，以及捕获哪些信号。

    **默认行为：** 当本小节列为“Default.”（默认），或对任何信号引用“标准动作”时，表示因信号而采取的动作应如下：

    -   如果根据《系统接口》卷中定义的信号动作继承规则，从调用进程继承的动作是忽略该信号，则实用程序应忽略该信号。
    -   如果根据《系统接口》卷中定义的信号动作继承规则，从调用进程继承的动作是默认信号动作，则实用程序执行的结果应如同采取了默认信号动作一样。

    当要求的动作是让信号终止实用程序时，实用程序可捕获该信号、执行一些附加处理（如删除临时文件）、恢复默认信号动作，并重新向自身发信号。

**STDOUT**

:   STDOUT 小节完整描述实用程序的标准输出。本小节经常只是对以下小节 OUTPUT FILES 的引用，因为许多实用程序以相同方式对待标准输出和输出文件。

    将终端用于标准输出，会使任何写入标准输出的标准实用程序在后台使用时停止。因此，应用程序不应在要置于后台的脚本中使用交互式功能。

    记录格式以类似于 C 语言函数 [*printf*()](../functions/printf.html) 使用的记法描述。参见 XBD [*5. 文件格式记法*](../basedefs/V1_chap05.html#tag_05)。

    标准实用程序的指定标准输出，不应依赖于本卷 POSIX.1-2024 中定义的环境变量的存在或值，除非本卷 POSIX.1-2024 另有规定。

    某些标准实用程序使用动词 *display*（显示）描述其输出，该词在 XBD [*3.107 显示*](../basedefs/V1_chap03.html#tag_03_107) 中定义。此类实用程序 STDOUT 小节中描述的输出可使用标准输出以外的手段产生。当标准输出指向终端时，所描述的输出应直接写入终端。否则，结果是未定义的。

    **默认行为：** 当本小节列为“Not used.”（不使用）时，表示当按本卷 POSIX.1-2024 描述使用实用程序时，不应写入标准输出。

**STDERR**

:   STDERR 小节描述实用程序的标准错误输出。只描述实用程序有意发送的那些消息。

    将终端用于标准错误，会使任何写入标准错误输出的标准实用程序在后台使用时停止。因此，应用程序不应在要置于后台的脚本中使用交互式功能。

    大多数实用程序的诊断消息格式是未指定的，但本卷 POSIX.1-2024 未指定格式的诊断和信息性消息的语言与文化惯例，应受 *LC_MESSAGES* 和 `[XSI]` *NLSPATH* 设置的影响。[译者注：原文 “[XSI]” 处以 opt-start.gif/opt-end.gif 图标标示 XSI 选项内容的起止，此处以文字表示。]

    标准实用程序的指定标准错误输出，不应依赖于本卷 POSIX.1-2024 中定义的环境变量的存在或值，除非本卷 POSIX.1-2024 另有规定。

    **默认行为：** 当本小节列为“The standard error shall be used only for diagnostic messages.”（标准错误应仅用于诊断消息）时，表示除非另有说明，仅当退出状态指示发生错误且按本卷 POSIX.1-2024 描述使用实用程序时，诊断消息才应发送到标准错误。

    当本小节列为“Not used.”（不使用）时，表示当按本卷 POSIX.1-2024 描述使用实用程序时，不应使用标准错误。

**OUTPUT FILES**

:   OUTPUT FILES 小节完整描述实用程序创建或修改的文件。为本实用程序或实现的其他部分内部使用而创建的临时或系统文件（例如 spool、log 和 audit 文件）不在本小节或任何小节中描述。创建此类文件的实用程序以及此类文件的名称是未指定的。如果应用程序要使用临时或中间文件，应使用 *TMPDIR* 环境变量（如果它被设置并代表一个可访问的目录）来选择临时文件的位置。

    实现应确保标准实用程序使用的临时文件的命名，使不同的实用程序或同一实用程序的多个实例能够同时操作，而不必考虑其工作目录或除进程 ID 之外的任何其他进程特性。此规则有两个例外：

    1.  临时文件的名称空间之外的资源（例如磁盘空间、可用的目录项或允许的进程数）不保证。
    2.  某些标准实用程序生成的输出文件旨在作为其他实用程序的输入（例如 [*lex*](../utilities/lex.html) 生成 **lex.yy.c**），这些不能有唯一名称。这些情况在各实用程序的描述中被明确标识。

    实现创建的任何临时文件，应由实现在该实用程序成功退出、因错误退出、或被任何 SIGHUP、SIGINT 或 SIGTERM 信号终止之前移除，除非实用程序描述另有规定。

    收到 SIGQUIT 信号通常应导致终止（除非在某些调试模式下），这将绕过任何尝试的恢复动作。

    记录格式以类似于 C 语言函数 [*printf*()](../functions/printf.html) 使用的记法描述；参见 XBD [*5. 文件格式记法*](../basedefs/V1_chap05.html#tag_05)。

    **默认行为：** 当本小节列为“None.”（无）时，表示当按本卷 POSIX.1-2024 描述使用实用程序时，不会因实用程序的直接动作而创建或修改任何文件。然而，实用程序可以创建或修改实用程序正常执行环境之外的系统文件，如日志文件。

**EXTENDED DESCRIPTION**

:   EXTENDED DESCRIPTION 小节为描述非常复杂的实用程序（如文本编辑器或语言处理器，它们通常有精心设计的命令语言）的动作提供了一个位置。

    **默认行为：** 当本小节列为“None.”（无）时，无需进一步描述。

**EXIT STATUS**

:   EXIT STATUS 小节描述实用程序应返回给调用程序或 shell 的值，以及导致返回这些值的条件。通常，实用程序成功完成时返回零，各种错误条件下返回大于零的值。如果本小节列出了特定数值，系统应对所描述的错误使用这些值。在某些情况下，状态值的列出较宽松，如 >0。严格一致（strictly conforming）应用程序不应依赖所示范围内的任何特定值，并应准备好接收该范围内的任何值。

    例如，实用程序可将零列为成功返回，1 列为特定原因的失败，>1 列为“发生了错误”。在这种情况下，未指定的条件可能导致返回 2 或 3 或其他值。一致应用程序的编写应测试成功的退出状态值（此处为零），而不是依赖本卷 POSIX.1-2024 中列出的单个特定错误值。这样，即使在带扩展的实现上，它也具有最大可移植性。

    未指定的错误条件可由本卷 POSIX.1-2024 未列出的特定值表示。

    **默认行为：** 当退出状态 0 的描述是“Successful completion”（成功完成）时，表示退出状态 0 应指示实用程序被要求执行的所有动作都成功完成。

**CONSEQUENCES OF ERRORS**

:   CONSEQUENCES OF ERRORS 小节描述发生错误条件时对环境、文件系统、进程状态等的影响。它不描述产生的错误消息或使用的退出状态值。

    实用程序失败的许多原因通常不由实用程序描述规定。实用程序可能因以下情况过早终止：选项、参数或环境变量的无效使用；EXTENDED DESCRIPTION 小节中表达的复杂语法的无效使用；资源耗尽；访问、创建、读取或写入文件的困难；或与进程权限相关的困难。

    除非另有说明，以下内容应适用于每个实用程序：

    -   如果请求的动作无法对代表文件、目录、用户、进程等的操作数执行，实用程序应向标准错误发出诊断消息并继续处理下一个操作数，但最终退出状态应是指示发生错误的退出状态。

        对于递归遍历文件层级的实用程序（如 [*find*](../utilities/find.html) 或 [*chown*](../utilities/chown.html) **-R**），如果请求的动作无法对层级中遇到的某个文件或目录执行，实用程序应向标准错误发出诊断消息并继续处理层级中剩余的文件，但最终退出状态应是指示发生错误的退出状态。

        **注意：** 如果请求的动作是以 \<newline\> 作为终止符或分隔符的格式写入一个或多个路径名，而要写入的路径名包含任何字节值为 \<newline\> 字符的编码，则应将其视为无法执行的动作。本标准未来版本可能要求实用程序将此视为错误。

    -   如果以选项或选项参数为特征的动作无法执行，实用程序应向标准错误发出诊断消息，返回的退出状态应是指示发生错误的退出状态。
    -   当遇到不可恢复的错误条件时，实用程序应以指示发生错误的退出状态退出。
    -   每当发生错误条件时，应向标准错误写入诊断消息。

    当实用程序遇到错误条件时，根据错误的严重性和实用程序的状态，可能有几种动作。各种实用程序可能采取的动作包括：删除临时或中间工作文件；删除不完整的文件；对文件系统或目录进行有效性检查。

    **默认行为：** 当本小节列为“Default.”（默认）时，表示对环境、文件系统、进程状态等的任何更改都是未指定的。

**APPLICATION USAGE**

:   本小节是提供信息的（informative）。

    APPLICATION USAGE 小节就实用程序的使用方式向应用程序程序员或用户提供建议。

**EXAMPLES**

:   本小节是提供信息的（informative）。

    EXAMPLES 小节在适当时给出一个或多个用法示例。如果示例与规范的规定性部分冲突，以规范性材料为准。

    在所有示例中，都使用了引号（quoting），展示示例命令（实用程序名称与参数组合）如何能正确地传递给 shell（参见 [*sh*](../utilities/sh.html)）或作为字符串传递给《系统接口》卷中定义的 [*system*()](../functions/system.html) 函数。如果实用程序使用《系统接口》卷中定义的某个 *exec* 函数调用，则不会使用此类引号。

**RATIONALE**

:   本小节是提供信息的（informative）。

    本小节包含有关本卷 POSIX.1-2024 内容的史料，以及标准开发者为何包含或舍弃某些特性的原因。

**FUTURE DIRECTIONS**

:   本小节是提供信息的（informative）。

    FUTURE DIRECTIONS 小节应作为当前思路的指南；并不一定要承诺全部实现所有这些未来方向。

**SEE ALSO**

:   本小节是提供信息的（informative）。

    SEE ALSO 小节列出相关条目。

**CHANGE HISTORY**

:   本小节是提供信息的（informative）。

    本小节显示条目的来源以及对其所做的任何重大更改。

某些标准实用程序描述了它们如何调用其他实用程序或应用程序，例如向命令解释器传递命令字符串。此类被调用实用程序的外部影响（STDIN、ENVIRONMENT VARIABLES 等）和外部效果（STDOUT、CONSEQUENCES OF ERRORS 等），不在调用它们的标准实用程序的小节中描述。

### 1.5 支持任意大小文件的实用程序的注意事项 (Considerations for Utilities in Support of Files of Arbitrary Size)

以下实用程序支持大到实现可创建的最大值的任意大小的文件。此支持包括正确写入与文件大小相关的值（如文件大小和偏移量、行号和块计数），以及正确解释包含此类值的命令行参数。

*basename*

:   返回路径名的非目录部分。

*cat*

:   连接并打印文件。

*cd*

:   更改工作目录。

*chgrp*

:   更改文件组属主。

*chmod*

:   更改文件模式。

*chown*

:   更改文件属主。

*cksum*

:   写入文件校验和与大小。

*cmp*

:   比较两个文件。

*cp*

:   复制文件。

*dd*

:   转换并复制文件。

*df*

:   报告可用磁盘空间。

*dirname*

:   返回路径名的目录部分。

*du*

:   估算文件空间使用。

*find*

:   查找文件。

*ln*

:   链接文件。

*ls*

:   列出目录内容。

*mkdir*

:   创建目录。

*mv*

:   移动文件。

*pathchk*

:   检查路径名。

*pwd*

:   返回工作目录名。

*rm*

:   移除目录项。

*rmdir*

:   移除目录。

*sh*

:   shell，标准命令语言解释器。

*test*

:   求值表达式。

*touch*

:   更改文件访问和修改时间。

*ulimit*

:   设置或报告文件大小限制。

对“实用程序支持大到最大值的任意大小文件”这一要求的例外如下：

1.  将文件用作命令脚本，或用于配置或控制，是豁免的。例如，不要求 [*sh*](../utilities/sh.html) 能够读取任意大的 **.profile**。
2.  Shell 输入和输出重定向是豁免的。例如，不要求重定向 *sum* \< *file* 或 *echo foo* \> *file* 对任意大的现有文件都成功。

### 1.6 内置实用程序 (Built-In Utilities)

任何标准实用程序都可以在命令语言解释器内实现为常规内置实用程序（regular built-in utilities）。这样做通常是为了提高常用实用程序的性能，或实现单独环境中更难实现的功能。下面 [1.7 内在实用程序](#tag_18_07) 中描述的内在实用程序经常作为常规内置提供。

然而，除以下之外的所有标准实用程序：

-   [2.15 特殊内置实用程序](../utilities/V3_chap02.html#tag_19_15) 中描述的特殊内置
-   [内在实用程序](#tagtcjh_13) 中命名的内在实用程序，[*kill*](../utilities/kill.html) 除外

无论它们是否也作为常规内置实现，都应以一种可通过《系统接口》卷中定义的 *exec* 函数族访问的方式实现，并且能够被需要它的标准实用程序（[*env*](../utilities/env.html)、[*find*](../utilities/find.html)、[*nice*](../utilities/nice.html)、[*nohup*](../utilities/nohup.html)、[*time*](../utilities/time.html)、[*xargs*](../utilities/xargs.html)）直接调用。

### 1.7 内在实用程序 (Intrinsic Utilities)

如 [2.9.1.4 命令搜索与执行](../utilities/V3_chap02.html#tag_19_09_01_04) 所述，内在实用程序在命令搜索与执行期间不受 *PATH* 搜索的约束。[内在实用程序](#tagtcjh_13) 中命名的实用程序应为内在实用程序。

<table cellpadding="3" align="center">
<tr valign="top">
<td align="left"><p><br>&nbsp;<br><a href="../utilities/*alias*.html"><i>*alias*</i></a><br><a href="../utilities/*bg*.html"><i>*bg*</i></a><br><a href="../utilities/*cd*.html"><i>*cd*</i></a><br></p></td>
<td align="left"><p><br>&nbsp;<br><a href="../utilities/*command*.html"><i>*command*</i></a><br><a href="../utilities/*fc*.html"><i>*fc*</i></a><br><a href="../utilities/*fg*.html"><i>*fg*</i></a><br></p></td>
<td align="left"><p><br>&nbsp;<br><a href="../utilities/*getopts*.html"><i>*getopts*</i></a><br><a href="../utilities/*hash*.html"><i>*hash*</i></a><br><a href="../utilities/*jobs*.html"><i>*jobs*</i></a><br></p></td>
<td align="left"><p><br>&nbsp;<br><a href="../utilities/*kill*.html"><i>*kill*</i></a><br><a href="../utilities/*read*.html"><i>*read*</i></a><br><a href="../utilities/*type*.html"><i>*type*</i></a><br></p></td>
<td align="left"><p><br>&nbsp;<br><a href="../utilities/*ulimit*.html"><i>*ulimit*</i></a><br><a href="../utilities/*umask*.html"><i>*umask*</i></a><br><a href="../utilities/*unalias*.html"><i>*unalias*</i></a><br></p></td>
<td align="left"><p><br>&nbsp;<br><a href="../utilities/*wait*.html"><i>*wait*</i></a><br>&nbsp;<br>&nbsp;<br></p></td>
</tr>
</table>

是否将任何附加实用程序视为内在实用程序是实现定义的（implementation-defined）。由于应用程序无法用 *PATH* 中的实用程序覆盖内在实用程序，实现不应将[内在实用程序](#tagtcjh_13) 之外的任何实用程序设为内在实用程序。
