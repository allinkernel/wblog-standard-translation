
POSIX 标准定义的完整 Utilities 约有 160 个。我们将采用与上一期相同结构：**语法、核心功能描述、常用选项/参数解析、核心行为特性** 以及 **实际应用场景示例**。

### 1. `admin` (SCCS 源代码控制系统)

创建与管理 SCCS（Source Code Control System）历史记录文件。

#### 语法

```sh
admin [-n] [-i[name]] [-rrel] [-t[name]] [-f flag[value]] [-d flag] file...

```

#### 选项与参数

* **`-n`**：创建一个新的 SCCS 文件。
* **`-i[name]`**：从指定文件 `name` 读取初始文本内容。若省略 `name`，则从标准输入读取。
* **`-rrel`**：指定初始版本号（Release），默认为 `1`。
* **`-fflag[value]`**：设置 SCCS 文件标志位（如 `-fb` 允许建立分支）。
* **`-dflag`**：删除指定的 SCCS 标志位。

#### 行为特性

* SCCS 文件默认以 `s.` 开头（如 `s.main.c`）。`admin` 是经典的 UNIX 版本控制工具，现代开发中多被 Git 替代，但仍作为 POSIX 遗留（XSI Option）标准保留。

#### 常见示例

```sh
# 基于 main.c 初始化创建一个新的 SCCS 控制文件 s.main.c
admin -imain.c s.main.c

```

---

### 2. `alias`

在当前 Shell 会话中定义或查看别名（Command Alias）。

#### 语法

```sh
alias [alias-name[=string]...]

```

#### 选项与参数

* **`alias-name`**：要定义的别名名称。
* **`string`**：别名代表的实际命令行字符串。
* 无参数时：打印当前 Shell 环境中定义的所有别名。

#### 行为特性

* 别名只对交互式 Shell 的**第一个语法单词**生效。
* 别名替换发生在语法解析阶段的最早期，**不能**被子 Shell 继承（除非写在 `~/.bashrc` 或配置文件中）。

#### 常见示例

```sh
# 示例 1: 为常用命令配置默认参数
alias ll='ls -l'
alias rm='rm -i'

# 示例 2: 查看当前定义的所有别名
alias

```

---

### 3. `ar`

创建、修改库文件（Archive），或从 `.a` 静态库中提取目标文件（`.o`）。

#### 语法

```sh
ar -d [-v] archive file...
ar -r [-cvu] archive file...
ar -t [-v] archive [file...]
ar -x [-v] archive [file...]

```

#### 选项与参数

* **`-r`**：将文件插入或替换（Replace）到归档文件中。
* **`-c`**：创建归档文件时抑制提示信息。
* **`-t`**：列出（Table）归档文件内部包含的所有文件名。
* **`-x`**：提取（Extract）归档文件内部的目标文件。
* **`-d`**：从归档文件中删除指定文件。

#### 行为特性

* 用于 ANSI C / C++ 开发中的静态链接库（`.a` 文件）管理。

#### 常见示例

```sh
# 示例 1: 将两个目标文件打包为一个静态库 libmath.a
ar -rc libmath.a add.o sub.o

# 示例 2: 列出静态库中的内容
ar -t libmath.a

```

---

### 4. `asa`

将含有 Fortran 换行控制字符（Carriage Control Characters）的文本转换为标准打印格式。

#### 语法

```sh
asa [file...]

```

#### 选项与参数

* **`file`**：待转换的文本文件。若未指定，从标准输入读取。

#### 行为特性

* 解析行首的传统 Fortran 格式控制符：
* `' '`（空格）：正常换行。
* `'0'`：输出两个换行（空一行）。
* `'1'`：换页（Page eject / Form feed）。
* `'+'`：不换行（实现重叠打印/加粗效果）。



#### 常见示例

```sh
# 转换 Fortran 程序输出的文本文件格式
asa fortran_output.txt > formatted_output.txt

```

---

### 5. `at`

提交一次性定时任务，在未来指定的时间点由 `atd` 守护进程执行。

#### 语法

```sh
at [-m] [-f file] [-q queue] time
at -r job_id...
at -l [job_id...]

```

#### 选项与参数

* **`time`**：指定运行时间（如 `10:30`、`now + 30 minutes`、`4pm tomorrow`）。
* **`-f file`**：从文件读取要执行的命令列表，而非交互式输入。
* **`-m`**：任务执行完成后给用户发送邮件。
* **`-l`**：列出当前队列中待执行的任务（等价于 `atq`）。
* **`-r job_id`**：删除指定的作业（等价于 `atrm`）。

#### 行为特性

* 任务执行时的环境变量和当前工作目录将被完整保留。任务的标准输出和标准错误默认通过系统邮件发给提交者。

#### 常见示例

```sh
# 示例 1: 提交在晚上 11:30 执行的任务
at 23:30 << 'EOF'
/home/user/scripts/backup.sh
EOF

# 示例 2: 查看待执行队列
at -l

```

---

### 6. `awk`

模式扫描与文本处理语言。按行读取输入，以分隔符切分成字段，匹配模式后执行指定动作。

#### 语法

```sh
awk [-F ERE] [-v assignment] 'program' [argument...]
awk [-F ERE] -f scriptfile [-v assignment] [argument...]

```

#### 选项与参数

* **`-F ERE`**：指定输入字段的分隔符（Extended Regular Expression），默认为连续空白符。
* **`-v var=value`**：向 awk 内部变量赋值。
* **`-f scriptfile`**：从文件加载 awk 脚本逻辑。

#### 核心内置变量

* **`$0`**：整行文本。
* **`$1, $2...`**：切割后的第 1、第 2 个字段。
* **`NF`**：当前行的字段总数（Number of Fields）。
* **`NR`**：当前已处理的行号记录数（Number of Records）。

#### 常见示例

```sh
# 示例 1: 打印 /etc/passwd 中 UID >= 1000 的用户名及 Shell（以 : 分隔）
awk -F: '$3 >= 1000 { print $1, $7 }' /etc/passwd

# 示例 2: 统计文本总行数与最后一列之和
awk '{ sum += $NF } END { print "Total lines:", NR, "Sum:", sum }' data.txt

```


### 7. `basename`

从包含路径的文件名字符串中剥离目录部分，仅保留最终的文件名（或可选剥离后缀）。

#### 语法

```sh
basename string [suffix]

```

#### 选项与参数

* **`string`**：完整的路径字符串（如 `/usr/local/bin/python3`）。
* **`suffix`**：可选的后缀名（如 `.c`）。若文件名以此后缀结尾，该后缀也会被同时裁切掉。

#### 核心行为特性

* 不检查文件系统中的实际文件是否存在，仅对输入的字符串进行文本规则切分。

#### 常见示例

```sh
# 示例 1: 提取文件名
basename /usr/include/stdio.h
# 输出: stdio.h

# 示例 2: 提取文件名并去掉指定后缀
basename /home/user/main.c .c
# 输出: main

```

---

### 8. `batch`

将任务放入系统后台列队中，等待系统负载（Load Average）降到指定阈值以下时再延迟执行。

#### 语法

```sh
batch

```

#### 核心行为特性

* 语法与 `at` 类似，但不需要显式指定绝对时间，由系统负载调度器决定何时启动。命令从标准输入读取。

#### 常见示例

```sh
# 提交一个对 CPU 消耗较大的编译或分析任务
batch << 'EOF'
gcc -O3 heavy_computation.c -o heavy_app
./heavy_app
EOF

```

---

### 9. `bc`

任意精度算术运算语言与交互式计算器（支持大整数、浮点数及基本数学函数）。

#### 语法

```sh
bc [-l] [file...]

```

#### 选项与参数

* **`-l`**：加载标准数学库（Math Library），此时默认保留 20 位小数精度（`scale=20`），并引入 `s(x)` 正弦、`c(x)` 余弦、`a(x)` 反切、`l(x)` 对数、`e(x)` 指数等函数。

#### 核心行为特性

* 默认的 `scale`（小数位数）为 0，即默认进行整数运算。可以通过在代码中显式设置 `scale=N` 改变精度。

#### 常见示例

```sh
# 示例 1: 在命令行管道中计算浮点数除法（保留 4 位小数）
echo "scale=4; 22 / 7" | bc
# 输出: 3.1428

# 示例 2: 使用数学库计算圆周率 pi (4 * arctan(1))
echo "scale=10; 4*a(1)" | bc -l

```

---

### 10. `bg`

作业控制命令：将当前暂停（Stopped）的前台任务放到后台继续运行。

#### 语法

```sh
bg [job_id...]

```

#### 选项与参数

* **`job_id`**：作业标识符（如 `%1`, `%+`, `%-`）。若省略，默认作用于当前最近被暂停的作业（`%+`）。

#### 常见示例

```sh
# 假设按 Ctrl+Z 暂停了前台任务 [1]+ Stopped vim app.log
bg %1
# 任务 [1] 转入后台继续运行

```

---

### 11. `c99` (C 语言编译器)

POSIX 标准中定义的 C99 规范 ANSI/ISO C 编译器前端（如 `gcc` 或 `clang` 的 POSIX 抽象）。

#### 语法

```sh
c99 [-c] [-g] [-s] [-O optlevel] [-o outfile] [-D name[=def]]... [-U name]...
    [-I dir]... [-L dir]... file... [-l library]...

```

#### 选项与参数

* **`-c`**：仅编译生成目标文件（`.o`），不进行链接。
* **`-g`**：生成用于调试器（如 gdb）的调试符号信息。
* **`-O optlevel`**：指定优化级别（如 `-O1`, `-O2`）。
* **`-o outfile`**：指定编译输出的可执行文件名。
* **`-D name[=def]`**：定义预处理器宏。
* **`-I dir`**：添加头文件搜索目录。
* **`-L dir`**：添加库文件搜索目录。
* **`-l library`**：链接指定的静态或动态库（如 `-lm` 代表数学库）。

#### 常见示例

```sh
c99 -O2 -I/usr/local/include -o myapp main.c utils.c -L/usr/local/lib -lm

```

---

### 12. `cal`

在终端打印简易的公历日历。

#### 语法

```sh
cal [[month] year]

```

#### 选项与参数

* 无参数：打印当前月份的日历。
* **`month year`**：指定月份（1–12）与年份（1–9999）。

#### 常见示例

```sh
# 打印 2026 年 8 月的日历
cal 8 2026

```

---

### 13. `cat`

连接（Concatenate）一个或多个文件并输出到标准输出（Standard Output）。

#### 语法

```sh
cat [-u] [file...]

```

#### 选项与参数

* **`-u`**：取消输出缓冲（Unbuffered IO），对字节流进行无缓冲地实时写入。
* **`file`**：待读取的文件列表。若为 `-` 或未指定，则从标准输入读取。

#### 常见示例

```sh
# 示例 1: 合并多个文本文件
cat part1.txt part2.txt > full.txt

# 示例 2: 从标准输入读取并追加重定向
cat - >> notes.txt

```

---

### 14. `cd`

改变当前 Shell 的工作目录（Change Directory）。

#### 语法

```sh
cd [-L|-P] [directory]
cd -

```

#### 选项与参数

* **`-L`**：（默认）逻辑路径视角。跟随符号链接（Symlink），不解析物理父目录。
* **`-P`**：物理路径视角。强制解析所有符号链接，进入真实的物理文件目录路径。
* **`directory`**：目标目录。若省略，默认进入环境变量 `$HOME` 所在的目录。
* **`cd -`**：快速返回上一次的工作目录（即进入 `$OLDPWD`）。

#### 常见示例

```sh
# 进入符号链接的真实物理目录
cd -P /var/mail

```

---

### 15. `cflow`

生成 C 语言源文件的代码调用流程图（Call Graph）。

#### 语法

```sh
cflow [-r] [-d depth] [-i incl] [-U name]... [-D name[=def]]... [-I dir]... file...

```

#### 选项与参数

* **`-r`**：生成反向调用图（即查看某个函数被哪些上层函数所调用）。
* **`-d depth`**：限制调用的最大嵌套深度数字。

#### 常见示例

```sh
# 分析 main.c 的代码调用关系
cflow main.c

```

---

### 16. `chgrp`

变更文件或目录的所属组（Group Ownership）。

#### 语法

```sh
chgrp [-h] [-R [-H|-L|-P]] group file...

```

#### 选项与参数

* **`-R`**：递归（Recursive）修改目录及其下所有文件/子目录的组。
* **`-h`**：若目标是符号链接，直接修改符号链接本身的组，而非其指向的目标文件。
* **`-H / -L / -P`**：在 `-R` 递归时对符号链接的遍历策略（`-P` 为不跟随任何符号链接，默认）。

#### 常见示例

```sh
chgrp -R developers /srv/www/project

```

---

### 17. `chmod`

变更文件或目录的访问权限位（Mode Bits / Access Permissions）。

#### 语法

```sh
chmod [-R [-H|-L|-P]] mode file...

```

#### 选项与参数

* **`mode`**：可以使用**八进制数字模式**（如 `755`、`644`），也可以使用**符号模式**（格式为 `[ugoa][+-=][rwx]`）。
* **`-R`**：递归修改目录下所有文件的权限。

#### 常见示例

```sh
# 示例 1: 符号模式 - 为属主与属组添加可执行权限
chmod ug+x deploy.sh

# 示例 2: 数字模式 - 设置目录权限（rwxr-xr-x）
chmod 755 /var/www/html

```

---

### 18. `chown`

变更文件或目录的所有者（Owner）与所属组（Group）。

#### 语法

```sh
chown [-h] [-R [-H|-L|-P]] owner[:group] file...

```

#### 选项与参数

* **`owner[:group]`**：新所有者用户名/UID，以及可选的用冒号分隔的新组名/GID。

#### 常见示例

```sh
# 同时修改所有者为 www-data，组为 www-data
chown -R www-data:www-data /var/www/html

```

---

### 19. `cksum`

计算并打印文件的 POSIX 循环冗余校验码（CRC-32 Checksum）以及字节数。

#### 语法

```sh
cksum [file...]

```

#### 行为特性

* 输出三列信息：`CRC校验码` `文件字节大小` `文件名`。常用于在传输后验证数据完整性。

#### 常见示例

```sh
cksum ubuntu-24.04-desktop-amd64.iso

```

---

### 20. `cmp`

按字节逐位比较两个任意类型的文件（包括二进制文件），并找出首个不匹配的字节位置。

#### 语法

```sh
cmp [-l|-s] file1 file2

```

#### 选项与参数

* **`-s`**：静默模式（Silent）。不输出任何文本信息，仅通过退出状态码告知结果：
* `0`：两文件完全相同。
* `1`：两文件不同。
* `>1`：发生了读取错误。


* **`-l`**：列出（List）所有不相同字节的十进制偏移量及对应的八进制字节值。

#### 常见示例

```sh
# 在脚本中静默判断二进制文件是否发生变动
if cmp -s bin1.exec bin2.exec; then
    echo "Binaries are identical."
fi

```

---

### 21. `comm`

逐行比较两个已经排序好（Sorted）的文本文件，并以三列格式输出结果。

#### 语法

```sh
comm [-123] file1 file2

```

#### 选项与参数

* **`-1`**：抑制第一列输出（即隐藏“仅在 file1 中出现的行”）。
* **`-2`**：抑制第二列输出（即隐藏“仅在 file2 中出现的行”）。
* **`-3`**：抑制第三列输出（即隐藏“两文件共有的行”）。

#### 常见示例

```sh
# 仅打印 file1.txt 与 file2.txt 两者共有的行
comm -12 file1_sorted.txt file2_sorted.txt

```

---

### 22. `command`

直接调用系统实用程序，强制**绕过 Shell 函数与别名的查找**。

#### 语法

```sh
command [-p] command_name [argument...]
command [-v|-V] command_name

```

#### 选项与参数

* **`-p`**：使用 POSIX 标准默认的 `PATH` 路径搜索该命令，确保调用的是系统标准工具。
* **`-v`**：打印命令的寻找路径（类似于 `which`）。
* **`-V`**：详细描述该命令在 Shell 中会如何被解析执行（函数、内置命令还是外部文件）。

#### 常见示例

```sh
# 即使定义了 alias ls='ls --color=auto'，依然调用原始的 ls 命令
command ls

```

---

### 23. `compress`

使用自适应 Lempel-Ziv 编码算法（LZW）压缩文件（生成 `.Z` 结尾的文件）。

#### 语法

```sh
compress [-cfv] [-b bits] [file...]

```

#### 选项与参数

* **`-c`**：将压缩数据写入标准输出，保持原文件不变。
* **`-f`**：强制压缩（即使文件没有变小或目标文件已存在）。
* **`-v`**：打印压缩比率详情。

#### 常见示例

```sh
compress -v archive.tar
# 生成 archive.tar.Z 并替换原文件

```

---

### 24. `cp`

复制文件或目录（Copy）。

#### 语法

```sh
cp [-fip] source_file target_file
cp [-fip] source_file... target_directory
cp -R|-r [-fip] source_directory... target_directory

```

#### 选项与参数

* **`-R / -r`**：递归复制目录及其子树。
* **`-i`**：交互式确认（Interactive），在覆盖已存在文件前弹出提示。
* **`-f`**：强制（Force）覆盖目标文件。
* **`-p`**：保留（Preserve）原文件的修改时间、访问时间、权限位及 UID/GID。

#### 常见示例

```sh
cp -Rp /src/project /backup/project_bak

```

---

### 25. `crontab`

提交、编辑、列出或删除用户的后台周期性定时任务表（Cron Job）。

#### 语法

```sh
crontab [file]
crontab -e|-l|-r

```

#### 选项与参数

* **`-e`**：使用默认文本编辑器打开并编辑当前用户的 crontab 配置文件。
* **`-l`**：列出当前用户已注册的所有定时任务。
* **`-r`**：移除（Remove）当前用户所有的定时任务。

#### 常见示例

```sh
# 1. 查看已有任务
crontab -l

# 2. crontab 中的时间语法规范：分 时 日 月 星期 命令
# 示例: 每天凌晨 2 点执行清理
# 0 2 * * * /home/user/clean.sh

```

---

### 26. `csplit`

根据文本中的上下文模式（Context Pattern）或行号，将一个大文本文件切分为多个小块文件。

#### 语法

```sh
csplit [-s] [-f prefix] [-n number] file arg1 ...argN

```

#### 选项与参数

* **`-f prefix`**：切分后生成的文件名前缀，默认是 `xx`（如 `xx00`, `xx01`）。
* **`-n number`**：指定文件名序号的数字位数，默认是 `2`。
* **`arg`**：可以是行号（如 `100`），或者是正则表达式（如 `/SECTION/`）。

#### 常见示例

```sh
# 在匹配到包含 "CHAPTER" 字符串的地方切分文件
csplit -f chapter_ book.txt /CHAPTER/ {*}

```

---

### 27. `ctags`

为 C/C++ 等源代码文件提取函数、变量、宏的定义索引，生成 `tags` 文件（供 Vim/Emacs 跳转）。

#### 语法

```sh
ctags [-a] [-x] [-f tagsfile] file...

```

#### 选项与参数

* **`-f tagsfile`**：指定生成的索引文件名，默认为 `tags`。
* **`-a`**：追加模式，将新索引追加到现有 `tags` 文件末尾。
* **`-x`**：不在文件里生成 tag，而是直接将符号列表和对应的行号、文件名输出到屏幕。

#### 常见示例

```sh
ctags -f src_tags src/*.c src/*.h

```

---

### 28. `cut`

从文本文件的每一行中裁切并提取指定的**字节、字符或字段（Columns）**。

#### 语法

```sh
cut -b list [-n] [file...]
cut -c list [file...]
cut -f list [-d delim] [-s] [file...]

```

#### 选项与参数

* **`-d delim`**：指定字段分隔符，默认为制表符（Tab）。
* **`-f list`**：提取指定的字段列表（如 `-f 1,3` 或 `-f 2-5`）。
* **`-c list`**：按字符位置提取（如 `-c 1-10`）。
* **`-s`**：不打印不包含分隔符的行。

#### 常见示例

```sh
# 提取 /etc/passwd 中每行的用户名（第 1 字段）和 Shell（第 7 字段）
cut -d: -f1,7 /etc/passwd

```

---

### 29. `cxref`

生成 C 语言程序源文件的交叉引用表（Cross-Reference Table），列出所有符号出现在哪些文件的第几行。

#### 语法

```sh
cxref [-c] [-w num] [-o file] [-D name[=def]]... [-I dir]... file...

```

#### 常见示例

```sh
cxref -o ref.txt main.c utils.c

```

### 30. `date`

打印或设置系统的日期与时间。

#### 语法

```sh
date [-u] [+format]
date [-u] mmddhhmm[[cc]yy]

```

#### 选项与参数

* **`-u`**：使用协调世界时（UTC），而非本地时区。
* **`+format`**：以指定的格式化字符串输出日期/时间。常用占位符：
* `%Y`：四位数年份，`%m`：月份 (01–12)，`%d`：日 (01–31)
* `%H`：24小时制小时，`%M`：分钟，`%S`：秒
* `%s`：自 Unix 纪元起计的秒数（Timestamp）
* `%F`：等价于 `%Y-%m-%d`，`%T`：等价于 `%H:%M:%S`



#### 常见示例

```sh
# 示例 1: 输出标准 ISO 8601 格式的当前时间
date "+%Y-%m-%d %H:%M:%S"

# 示例 2: 获取当前 UTC 时间戳
date -u "+%s"

```

---

### 31. `dd`

转换并复制文件（Data Duplicator），支持按指定的块大小（Block Size）直接进行底层数据块复制与格式转换。

#### 语法

```sh
dd [operand=value...]

```

#### 常用操作数 (Operands)

* **`if=file`**：输入文件路径（Input File），默认为标准输入。
* **`of=file`**：输出文件路径（Output File），默认为标准输出。
* **`bs=expr`**：同时设置读/写块大小（如 `bs=1M`）。
* **`count=n`**：仅复制 `n` 个输入块。
* **`seek=n`**：写入时跳过输出文件开头的 `n` 个块。
* **`skip=n`**：读取时跳过输入文件开头的 `n` 个块。
* **`conv=value`**：数据转换标志（如 `conv=ucase` 转大写，`conv=notrunc` 不截断输出文件）。

#### 常见示例

```sh
# 示例 1: 创建一个 100MB 的空文件
dd if=/dev/zero of=sparse.img bs=1M count=100

# 示例 2: 备份磁盘 MBR 主引导记录（前 512 字节）
dd if=/dev/sda of=mbr.bak bs=512 count=1

```

---

### 32. `delta` (SCCS 源代码控制系统)

在 SCCS 文件中应用改动，创建一个新的版本差分记录（Delta）。

#### 语法

```sh
delta [-r gfile] [-s] [-y[comment]] s.filename

```

#### 选项与参数

* **`-y[comment]`**：指定该版本的提交日志注释。
* **`-r gfile`**：显式指定被修改过的源文件。

#### 常见示例

```sh
delta -y"Fix memory leak in parser" s.main.c

```

---

### 33. `df`

显示文件系统的磁盘空间使用率（Disk Free）。

#### 语法

```sh
df [-k] [-P] [file|file_system...]

```

#### 选项与参数

* **`-P`**：使用 POSIX 标准输出格式，确保在不同 Unix 系统上字段对齐一致，方便脚本解析。
* **`-k`**：以 1024 字节（1 KiB）为单位显示数据块大小（默认单位可能是 512 字节）。

#### 常见示例

```sh
# 脚本安全的标准磁盘查询
df -P -k /

```

---

### 34. `diff`

逐行比较两个文本文件的差异，并输出补丁（Patch）指令。

#### 语法

```sh
diff [-c|-u] [-r] file1 file2

```

#### 选项与参数

* **`-u`**：输出统一格式补丁（Unified Context Format，即 `---`/`+++`/`@@` 格式，现代工具最通用）。
* **`-c`**：输出上下文格式补丁（Context Format）。
* **`-r`**：递归比较两个目录下的所有同名文件。

#### 常见示例

```sh
# 生成补丁文件
diff -u main.c.orig main.c > main.patch

```

---

### 35. `dirname`

从包含路径的字符串中剥离文件名，仅保留其上级目录路径。

#### 语法

```sh
dirname string

```

#### 常见示例

```sh
# 示例 1: 提取父目录
dirname /usr/local/bin/python3
# 输出: /usr/local/bin

# 示例 2: 在 Shell 脚本中获取当前脚本所在的绝对目录
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

```

---

### 36. `du`

递归汇总文件及目录占用的磁盘空间大小（Disk Usage）。

#### 语法

```sh
du [-a|-s] [-k] [-H|-L] [file...]

```

#### 选项与参数

* **`-s`**：汇总模式（Summary），仅打印每个输入参数的总体大小，不展开列出其子目录。
* **`-a`**：同时列出每个具体文件的大小，而不只是目录。
* **`-k`**：以 1024 字节（1 KiB）为单位计数。

#### 常见示例

```sh
# 查看 /var/log 目录的总占用空间（单位 KiB）
du -sk /var/log

```

---

### 37. `echo`

将参数字符串输出到标准输出。

#### 语法

```sh
echo [string...]

```

#### 行为特性

* **注意**：POSIX 标准规定 `echo` 的移植性较差。不同 Unix 实现对 `-n`（不换行）或 `\n`（转义字符）的处理存在分歧。若需要严格跨平台的格式化打印，**强烈建议优先使用 `printf**`。

#### 常见示例

```sh
echo "Build complete successfully."

```

---

### 38. `ed`

POSIX 标准定义的最基础的行编辑器（Line Editor）。

#### 语法

```sh
ed [-p string] [-s] [file]

```

#### 选项与参数

* **`-s`**：静默模式（Silent），关闭字节计数提示信息，适合在非交互脚本中使用。
* **`-p string`**：指定交互提示符。

#### 常见示例

```sh
# 使用 ed 在非交互脚本中修改文件首行
ed -s config.txt << 'EOF'
1s/old_value/new_value/
w
q
EOF

```

---

### 39. `env`

在修改后的环境中运行命令；若不带参数，则打印当前进程的所有环境变量。

#### 语法

```sh
env [-i] [name=value]... [utility [argument...]]

```

#### 选项与参数

* **`-i`**：清空环境（Ignore Environment），仅使用随后在命令行显式指定的 `name=value` 运行命令。
* **`name=value`**：临时添加或覆写环境变量。

#### 常见示例

```sh
# 示例 1: 在绝大多数脚本首行中用作 Shebang，动态定位解释器路径
#!/usr/bin/env sh

# 示例 2: 切换语言环境运行特定命令
env LC_ALL=C date

```

---

### 40. `ex`

Vim/Vi 的文本行编辑模式组件，提供面向行操作的文本批处理功能。

#### 语法

```sh
ex [-s] [-v] [file...]

```

#### 选项与参数

* **`-s`**：无提示静默脚本模式。
* **`-v`**：启动全屏幕可视模式（即直接启动 `vi`）。

#### 常见示例

```sh
ex -s -c '%s/LOG_DEBUG/LOG_INFO/g|x' app.c

```

---

### 41. `expr`

将参数作为算术或字符串求值表达式进行计算，并打印结果。

#### 语法

```sh
expr expression

```

#### 运算符与逻辑

* **算术**：`+`, `-`, `*`, `/`, `%`（乘号 `\*` 在 Shell 中需要转义）。
* **比较**：`=`, `!=`, `>`, `>=`, `<`, `<=`
* **字符串**：`string : regex`（匹配正则表达式并返回长度或提取组）。

#### 常见示例

```sh
# 示例 1: 算术计算（已被 Shell $(( )) 语法广泛替代，但仍作为独立命令存在）
expr 10 + 20

# 示例 2: 提取正则表达式匹配字符数
expr "hello.c" : '.*\.c'

```

---

### 42. `false`

空操作命令，除了**返回退出状态码 1** 之外不做任何事情。

#### 语法

```sh
false

```

#### 常见示例

```sh
# 用于测试条件判断或强行使管道中断
false || echo "Triggered on error"

```

---

### 43. `fc` (Fix Commands)

Shell 历史命令编辑器。可以从 Shell 历史记录中检索、修改并重新执行命令。

#### 语法

```sh
fc [-r] [-e editor] [first [last]]
fc -l [-nr] [first [last]]
fc -s [old=new] [first]

```

#### 选项与参数

* **`-l`**：列出（List）历史命令而非调用编辑器。
* **`-e editor`**：指定用于编辑历史命令的文本编辑器（如 `vim`）。
* **`-s`**：直接重新执行（Re-execute）指定的命令，可进行简单的字符串替换。

#### 常见示例

```sh
# 重新执行上一条包含 "make" 的历史命令，并将 "debug" 替换为 "release"
fc -s debug=release make

```

---

### 44. `fg`

作业控制命令：将后台运行或已暂停的任务拉回前台（Foreground）继续运行。

#### 语法

```sh
fg [job_id]

```

#### 常见示例

```sh
# 将作业号为 2 的后台任务切回前台
fg %2

```

---

### 45. `file`

通过检查文件的魔数（Magic Number）与文件头特征，检测并判定文件的真实类型。

#### 语法

```sh
file [-h] [file...]

```

#### 选项与参数

* **`-h`**：不跟随符号链接，直接检测符号链接文件本身。

#### 常见示例

```sh
file /bin/ls
# 输出类似: /bin/ls: ELF 64-bit LSB executable, x86-64, version 1 (SYSV)...

```

---

### 46. `find`

在目录树中递归搜索符合条件的文件，并对搜索到的文件执行动作。

#### 语法

```sh
find [-H|-L] path... [operand_expression...]

```

#### 常用谓词表达式 (Predicates)

* **`-name pattern`**：按文件名通配符匹配（如 `-name "*.c"`）。
* **`-type t`**：按文件类型筛选（`f` 普通文件，`d` 目录，`l` 符号链接）。
* **`-mtime n`**：按修改时间筛选（单位为天）。
* **`-exec utility {} +` / `-exec utility {} \;**`：对找到的每个文件执行指定命令。

#### 常见示例

```sh
# 找到 /var/log 下所有 7 天前修改且以 .log 结尾的文件并删除
find /var/var/log -type f -name "*.log" -mtime +7 -exec rm -f {} +

```

---

### 47. `fold`

将输入的长文本行按照指定的列宽进行硬折行（Wrap）处理。

#### 语法

```sh
fold [-b] [-s] [-w width] [file...]

```

#### 选项与参数

* **`-w width`**：指定折行列数宽度，默认为 `80`。
* **`-s`**：尽力在空格处折断（Break at spaces），避免截断单词。
* **`-b`**：以字节数（Bytes）而非字符数（Column Positions）计算宽度。

#### 常见示例

```sh
fold -w 40 -s long_text.txt

```

### 48. `fort77` (Fortran 编译器)

POSIX 标准中定义的 FORTRAN 77 语言编译器抽象接口。

#### 语法

```sh
fort77 [-c] [-g] [-O optlevel] [-s] [-o outfile] [-L dir]... file... [-l library]...

```

#### 选项与参数

* **`-c`**：仅编译生成目标文件（`.o`），不进行链接。
* **`-o outfile`**：指定最终可执行文件名。
* **`-O optlevel`**：开启优化。

#### 常见示例

```sh
fort77 -O2 -o calc math_sub.f main.f

```

---

### 49. `fuser`

列出正在使用指定文件、套接字或文件系统的进程 PID。

#### 语法

```sh
fuser [-cfu] file...

```

#### 选项与参数

* **`-c`**：将 `file` 作为挂载点，列出该文件系统上打开的所有文件对应的进程。
* **`-f`**：仅检查指定的具体文件。
* **`-u`**：在 PID 旁附加显示占用该文件的用户名。

#### 常见示例

```sh
# 查看谁占用了 /mnt/data 导致无法 umount
fuser -cu /mnt/data

```

---

### 50. `gencat`

生成格式化的消息目录文件（Message Catalog），用于国际化（i18n）多语言本地化支持。

#### 语法

```sh
gencat catfile msgfile...

```

#### 常见示例

```sh
gencat en_US.cat en_US.msg

```

---

### 51. `get` (SCCS 源代码控制系统)

从 SCCS 文件中提取指定版本的文本用于查看或编辑。

#### 语法

```sh
get [-e] [-r SID] s.filename

```

#### 选项与参数

* **`-e`**：以只写编辑模式提取，准备进行后续修改与 `delta` 提交。
* **`-r SID`**：提取指定的 Revision ID 版本。

#### 常见示例

```sh
get -e -r 1.2 s.main.c

```

---

### 52. `getconf`

查询 POSIX 系统配置参数或路径变量值（如最大文件名长度、页面大小等）。

#### 语法

```sh
getconf system_var
getconf path_var path

```

#### 常见示例

```sh
# 示例 1: 获取系统的内存页面字节大小
getconf PAGE_SIZE

# 示例 2: 查询特定路径下的最大文件路径名长度
getconf PATH_MAX /var/log

```

---

### 53. `getopts`

Shell 内置/实用程序，用于解析命令行传入的短选项（如 `-a -b val`）。

#### 语法

```sh
getopts optstring name [arg...]

```

#### 选项与参数

* **`optstring`**：合法选项字符列（若字符后接 `:`，代表该选项必须带参数）。
* **`name`**：存储当前解析到的选项字符的变量名。

#### 常见示例

```sh
while getopts "f:v" opt; do
    case "$opt" in
        f) FILE_PATH="$OPTARG" ;;
        v) VERBOSE=1 ;;
        ?) echo "Invalid option" ; exit 1 ;;
    esac
done

```

---

### 54. `grep`

使用基本或扩展正则表达式匹配文本并输出符合条件的数据行。

#### 语法

```sh
grep [-E|-F] [-i] [-l|-q] [-n] [-v] pattern [file...]

```

#### 选项与参数

* **`-E`**：使用扩展正则表达式（Extended Regular Expressions，等价于 `egrep`）。
* **`-F`**：匹配固定字符串，不按正则表达式解析（Fixed Strings，等价于 `fgrep`，速度最快）。
* **`-i`**：忽略大小写。
* **`-v`**：反向匹配（打印不匹配的行）。
* **`-q`**：静默模式（Quiet），不输出结果，通过 Exit Code 判断是否找到匹配项。
* **`-l`**：仅打印匹配到的文件名。

#### 常见示例

```sh
# 示例 1: 使用扩展正则查找错误日志
grep -E "ERROR|CRITICAL" /var/log/syslog

# 示例 2: 脚本中静默检查
if grep -q "SUCCESS" deploy.log; then
    echo "Deployment passed."
fi

```

---

### 55. `hash`

在 Shell 中查找、刷新或列出缓存的外部命令路径哈希表（避免重复搜索 `PATH`）。

#### 语法

```sh
hash [utility...]
hash -r

```

#### 选项与参数

* **`-r`**：清空当前 Shell 缓存的所有命令路径。

#### 常见示例

```sh
# 重置路径缓存（例如在安装了新版本的可执行程序后）
hash -r

```

---

### 56. `head`

输出文本文件的前 N 行（默认为前 10 行）。

#### 语法

```sh
head [-n number] [file...]

```

#### 选项与参数

* **`-n number`**：指定输出的行数。

#### 常见示例

```sh
head -n 20 access.log

```

---

### 57. `iconv`

在不同的字符编码格式之间进行文本转换（如 UTF-8 与 GBK 或 ISO-8859-1 的互转）。

#### 语法

```sh
iconv -f fromcode -t tocode [file...]

```

#### 选项与参数

* **`-f fromcode`**：源字符编码。
* **`-t tocode`**：目标字符编码。

#### 常见示例

```sh
iconv -f GBK -t UTF-8 legacy_doc.txt > utf8_doc.txt

```

---

### 58. `id`

打印当前或指定用户的真实与有效用户 ID（UID）和组 ID（GID）。

#### 语法

```sh
id [-u|-g|-G] [-n] [user]

```

#### 选项与参数

* **`-u`**：仅打印 UID。
* **`-g`**：仅打印有效 GID。
* **`-G`**：打印用户所属的所有附加组 GID。
* **`-n`**：与 `-u`/`-g`/`-G` 配合，输出名称而非数字 ID。

#### 常见示例

```sh
# 获取当前用户的有效用户名
id -un

```

---

### 59. `ipcrm`

删除指定的 System V 进程间通信（IPC）资源（消息队列、共享内存段或信号量集）。

#### 语法

```sh
ipcrm [-q msgid] [-m shmid] [-s semid] [-Q msgkey] [-M shmkey] [-S semkey]

```

#### 常见示例

```sh
# 清理 ID 为 32768 的共享内存段
ipcrm -m 32768

```

---

### 60. `ipcs`

列出当前系统中所有的 System V IPC 资源状态与使用统计。

#### 语法

```sh
ipcs [-a|-b|-c|-m|-q|-s]

```

#### 常见示例

```sh
ipcs -m  # 查看所有共享内存段

```

---

### 61. `jobs`

列出当前 Shell 会话中在后台运行或暂停的作业状态。

#### 语法

```sh
jobs [-l|-p] [job_id...]

```

#### 选项与参数

* **`-l`**：列出作业的同时，显示对应的进程 PID。
* **`-p`**：仅打印作业组长进程的 PID。

#### 常见示例

```sh
jobs -l

```

---

### 62. `join`

根据共享的关键字段（Key Field）将两个**已排序**的文本文件进行关联合并（类似 SQL 中的 JOIN）。

#### 语法

```sh
join [-a filenum] [-j field] [-1 field] [-2 field] [-t char] file1 file2

```

#### 选项与参数

* **`-t char`**：指定分隔符。
* **`-1 field`**：指定 file1 用于关联的列。
* **`-2 field`**：指定 file2 用于关联的列。

#### 常见示例

```sh
join -t: -1 1 -2 1 user_list.txt user_details.txt

```

---

### 63. `kill`

向指定的进程或作业发送操作系统信号（Signal）。

#### 语法

```sh
kill -s signal_name pid...
kill -signal_number pid...
kill -l [exit_status]

```

#### 选项与参数

* **`-l`**：列出系统支持的所有信号名称。
* **`-s signal_name`**：指定信号名称（如 `TERM`, `KILL`, `HUP`, `INT`）。

#### 常见示例

```sh
# 示例 1: 优雅请求 PID 1234 退出 (SIGTERM)
kill -s TERM 1234

# 示例 2: 强制杀死进程 (SIGKILL)
kill -9 1234

```

---

### 64. `lex` / `flex`

生成词法分析器（Lexical Analyzer）程序代码的工具（根据规则转为 C 语言代码）。

#### 语法

```sh
lex [-t] [-v] [file]

```

#### 常见示例

```sh
lex scanner.l   # 生成 lex.yy.c

```

---

### 65. `link`

创建执行现有文件的硬链接（Hard Link），底层的 `link()` 系统调用抽象。

#### 语法

```sh
link file1 file2

```

#### 常见示例

```sh
link original.txt hardlink.txt

```

---

### 66. `ln`

创建文件的硬链接（Hard Link）或符号链接（Symbolic Link）。

#### 语法

```sh
ln [-f|-i] [-s] source_file target_file
ln [-f|-i] [-s] source_file... target_dir

```

#### 选项与参数

* **`-s`**：创建软链接/符号链接（Symbolic Link），而非硬链接。
* **`-f`**：强制覆盖已存在的目标文件。

#### 常见示例

```sh
ln -s /usr/local/bin/python3 /usr/bin/python

```

---

### 67. `locale`

获取或打印当前系统的 Locale（语言、字符集、货币、时间等本地化）环境配置。

#### 语法

```sh
locale [-a|-m]

```

#### 选项与参数

* **`-a`**：列出当前系统支持的所有可用 Locale。

#### 常见示例

```sh
locale

```

---

### 68. `localedef`

根据定义的字符映射和语言包规则文件，编译生成新的二进制 Locale 数据库。

#### 语法

```sh
localedef [-c] [-f charmap] [-i inputfile] localename

```

#### 常见示例

```sh
localedef -i en_US -f UTF-8 en_US.UTF-8

```

---

### 69. `logger`

将自定义信息发送到系统日志接口（Syslog）。

#### 语法

```sh
logger [-p priority] [-t tag] message...

```

#### 选项与参数

* **`-t tag`**：为每行日志添加指定的标记/模块名。
* **`-p priority`**：指定日志级别（如 `user.notice` 或 `local0.err`）。

#### 常见示例

```sh
logger -t "backup_script" -p local0.err "Backup failed: Disk full"

```

---

### 70. `logname`

打印当前用户登录系统时使用的初始登录名。

#### 语法

```sh
logname

```

#### 常见示例

```sh
logname

```

---

### 71. `lp`

将文件发送到打印机进行打印排队。

#### 语法

```sh
lp [-c] [-d destination] [-n number] [file...]

```

#### 常见示例

```sh
lp -d office_printer document.pdf

```

---

### 72. `ls`

列出目录内容及文件的属性信息。

#### 语法

```sh
ls [-a] [-A] [-C] [-d] [-F] [-g] [-i] [-l] [-n] [-o] [-p] [-r] [-R] [-s] [-t] [-u] [file...]

```

#### 常用选项

* **`-a`**：显示所有文件（包含 `.` 和 `..` 隐藏文件）。
* **`-l`**：以长格式（Long Listing）显示详细属性（权限、链接数、所有者、组、大小、修改时间）。
* **`-d`**：仅列出目录本身的信息，而非展开其内部文件。
* **`-t`**：按修改时间排序。
* **`-R`**：递归列出所有子目录。

#### 常见示例

```sh
ls -la /var/log

```

---

### 73. `m4`

宏处理器（Macro Processor），常用于构建系统、编译配置中的模板文本替换。

#### 语法

```sh
m4 [-D name[=val]]... [-U name]... [file...]

```

#### 常见示例

```sh
m4 -DVERSION=2.0 config.m4 > config.h

```

---

### 74. `mailx`

处理和发送电子邮件的标准文本交互实用程序。

#### 语法

```sh
mailx [-s subject] mailaddr...

```

#### 常见示例

```sh
echo "Job Complete" | mailx -s "Status Report" admin@example.com

```

---

### 75. `make`

根据 `Makefile` 中的依赖关系树，自动化编译与构建项目的工程管理工具。

#### 语法

```sh
make [-f makefile] [-k] [-n] [-s] [macro=value...] [target...]

```

#### 选项与参数

* **`-f makefile`**：显式指定 Makefile 文件。
* **`-n`**：干排调试（Dry Run），只打印要执行的命令而不真正执行。
* **`-k`**：遇到错误时不停止，尽可能继续构建其余无关目标。
* **`-s`**：静默执行，不打印被调用的构建命令。

#### 常见示例

```sh
make -f Build.mk -n all

```

---

### 76. `man`

查看系统命令、函数与配置文件的手册页（Manual Page）。

#### 语法

```sh
man [-k] [section] title

```

#### 选项与参数

* **`-k`**：关键字搜索（等价于 `apropos`）。
* **`section`**：指定手册章节（1 为用户命令，2 为系统调用，3 为 C 库函数，5 为配置文件等）。

#### 常见示例

```sh
man 3 printf

```

---

### 77. `mesg`

控制其他用户是否可以通过 `write` 或 `talk` 命令向当前终端写入消息。

#### 语法

```sh
mesg [y|n]

```

#### 常见示例

```sh
mesg n  # 关闭终端接受外界写入

```

---

### 78. `mkdir`

创建新目录。

#### 语法

```sh
mkdir [-p] [-m mode] dir...

```

#### 选项与参数

* **`-p`**：递归创建多级父目录；若目录已存在也不报错。
* **`-m mode`**：指定新目录的八进制权限。

#### 常见示例

```sh
mkdir -p -m 755 /tmp/app/logs/2026

```

---

### 79. `mkfifo`

创建命名管道（FIFO 特殊文件）。

#### 语法

```sh
mkfifo [-m mode] path...

```

#### 常见示例

```sh
mkfifo /tmp/my_pipe

```

---

### 80. `more`

简易的文本分页阅读器。

#### 语法

```sh
more [-e|-c] [-n lines] [file...]

```

#### 常见示例

```sh
more big_log.log

```

---

### 81. `mv`

移动或重命名文件与目录。

#### 语法

```sh
mv [-f|-i] source_file target_file
mv [-f|-i] source_file... target_dir

```

#### 选项与参数

* **`-i`**：覆盖已存在文件前弹出交互提示。
* **`-f`**：强制覆盖。

#### 常见示例

```sh
mv -f app.tmp /srv/app/bin/app

```


### 82. `newgrp`

更改当前 Shell 会话的有效组 ID（GID）。

#### 语法

```sh
newgrp [-l] [group]

```

#### 选项与参数

* **`-l`**：重新模拟登录过程，初始化环境。

#### 常见示例

```sh
newgrp developers

```

---

### 83. `nice`

以更改后的进程调度优先级（Nice Value）运行指定的命令。

#### 语法

```sh
nice [-n increment] utility [argument...]

```

#### 选项与参数

* **`-n increment`**：优先级增量值（正值降低优先级，负值提高优先级）。

#### 常见示例

```sh
# 以低优先级运行后台计算密集型任务
nice -n 10 make -j8

```

---

### 84. `nl`

为文本文件添加行号并输出。

#### 语法

```sh
nl [-b type] [-d delim] [-f type] [-h type] [-i incr] [-l num] [-n format] [-s sep] [-v startnum] [-w width] [file]

```

#### 选项与参数

* **`-b type`**：指定正文行号样式（`a` 所有行，`t` 仅非空行）。
* **`-w width`**：行号字段的输出宽度。

#### 常见示例

```sh
nl -ba -w4 main.c

```

---

### 85. `nm`

打印目标文件（Object File）、共享库或可执行二进制文件中的符号表信息。

#### 语法

```sh
nm [-A] [-g|-u] [-P] [file...]

```

#### 选项与参数

* **`-g`**：仅显示全局（外部）符号。
* **`-u`**：仅显示未定义（External/Undefined）的符号。
* **`-P`**：使用 POSIX 可移植输出格式。

#### 常见示例

```sh
nm -gP libtest.a

```

---

### 86. `nohup`

运行命令并忽略挂起信号（SIGHUP），使命令在终端断开后仍能在后台持续运行。

#### 语法

```sh
nohup utility [argument...]

```

#### 常见示例

```sh
nohup ./long_running_task.sh > task.log 2>&1 &

```

---

### 87. `od`

按八进制（Octal）或其他多种指定格式（十六进制、ASCII、双字等）转储文件内容，常用于分析二进制文件。

#### 语法

```sh
od [-A address_base] [-j skip] [-N length] [-t type_string]... [file...]

```

#### 选项与参数

* **`-t type_string`**：指定输出格式（如 `x1` 单字节十六进制，`c` ASCII 转义字符）。
* **`-A address_base`**：偏移地址基数（`x` 十六进制，`d` 十进制，`n` 不显示地址）。

#### 常见示例

```sh
# 查看二进制文件的头部前 16 字节十六进制
od -t x1 -N 16 binary.bin

```

---

### 88. `paste`

按列对齐合并多个文本文件的对应行（以制表符或指定分隔符拼接）。

#### 语法

```sh
paste [-s] [-d list] file...

```

#### 选项与参数

* **`-d list`**：指定列间分隔符。
* **`-s`**：将单个文件中的多行合并为单行。

#### 常见示例

```sh
paste -d ',' col1.txt col2.txt

```

---

### 89. `patch`

将 `diff` 生成的补丁文件应用到原始文件上。

#### 语法

```sh
patch [-p num] [-R] [-i patchfile] [file]

```

#### 选项与参数

* **`-p num`**：从补丁中的文件路径剥离 `num` 层前缀目录。
* **`-R`**：反向应用补丁（撤销更改）。
* **`-i patchfile`**：指定补丁文件路径。

#### 常见示例

```sh
patch -p1 < bugfix.patch

```

---

### 90. `pathchk`

检查文件名或路径名在当前系统或标准 POSIX 规范下的合法性与可移植性。

#### 语法

```sh
pathchk [-p|-P] pathname...

```

#### 选项与参数

* **`-p`**：根据 POSIX 最小可移植文件名字符集检查路径合规性。

#### 常见示例

```sh
pathchk -p "my_file_name.txt"

```

---

### 91. `pax`

POSIX 标准可移植归档工具（用于取代传统的 `tar` 与 `cpio`）。

#### 语法

```sh
pax [-w] [-x format] [-f archive] [file...]
pax -r [-f archive] [pattern...]

```

#### 选项与参数

* **`-w`**：写模式（创建归档）。
* **`-r`**：读模式（解包归档）。
* **`-x format`**：指定归档格式（如 `pax` 或 `cpio`）。

#### 常见示例

```sh
# 创建 pax 归档文件
pax -w -f backup.pax ./src

```

---

### 92. `prs` (linux上不支持)

---

### 93. `printf`

格式化并打印数据，提供比 `echo` 更可靠、跨平台一致的输出能力。

#### 语法

```sh
printf format [argument...]

```

#### 常见说明

* 格式控制字符包括 `%s`（字符串）、`%d`（十进制整数）、`%x`（十六进制）、`%f`（浮点数）。

#### 常见示例

```sh
printf "Name: %-10s | ID: %04d\n" "Alice" 42

```

---

### 94. `ps`

获取当前系统中运行进程的状态快照（Process Status）。

#### 语法

```sh
ps [-a|-A|-e] [-f] [-o format] [-p plist] [-u ulist]

```

#### 选项与参数

* **`-A` / `-e**`：显示系统中的所有进程。
* **`-o format`**：自定义输出列（如 `pid,user,args`）。
* **`-f`**：完整格式显示。

#### 常见示例

```sh
ps -eo pid,user,pcpu,comm

```

---

### 95. `pwd`

打印当前工作目录的绝对路径（Print Working Directory）。

#### 语法

```sh
pwd [-L|-P]

```

#### 选项与参数

* **`-P`**：解析物理路径（避免符号链接）。
* **`-L`**：使用逻辑路径（保留符号链接路径）。

#### 常见示例

```sh
pwd -P

```

---

### 96. `qalter` (linux上不支持)

---

### 97. `qdel` (linux上不支持)

---

### 98. `qhold` (linux上不支持)

---

### 99. `qmove` (linux上不支持)

---

### 100. `qmsg` (linux上不支持)

---

### 101. `qrerun` (linux上不支持)

---

### 102. `qrls` (linux上不支持)

---

### 103. `qselect` (linux上不支持)

---

### 104. `qsig` (linux上不支持)

---

### 105. `qstat` (linux上不支持)

---

### 106. `qsub` (linux上不支持)

---

### 107. `read`

从标准输入读取一行文本并赋值给 Shell 变量。

#### 语法

```sh
read [-r] var...

```

#### 选项与参数

* **`-r`**：禁止反斜杠转义（原始输入模式，避免反斜杠被吃掉）。

#### 常见示例

```sh
read -r USER_INPUT

```

---

### 108. `renice`

修改已在运行中的进程的调度优先级（Nice Value）。

#### 语法

```sh
renice [-n increment] [-g|-p|-u] ID...

```

#### 选项与参数

* **`-n increment`**：指定优先级的调整增量值。
* **`-p`**：指定进程 PID（默认）。

#### 常见示例

```sh
renice -n 5 -p 1234

```

---

### 109. `rm`

删除文件或目录。

#### 语法

```sh
rm [-f|-i] [-r|-R] file...

```

#### 选项与参数

* **`-r` / `-R**`：递归删除目录及其内容。
* **`-f`**：强制删除（忽略不存在的文件，不弹出提示）。
* **`-i`**：逐一交互确认删除。

#### 常见示例

```sh
rm -rf /tmp/build_cache

```

---

### 110. `rmdel` (linux上不支持)

---

### 111. `rmdir`

删除空目录。

#### 语法

```sh
rmdir [-p] dir...

```

#### 选项与参数

* **`-p`**：递归删除上层空目录。

#### 常见示例

```sh
rmdir -p a/b/c

```


### 112. `sact` (linux上不支持)

---

### 113. `sccs` (linux上不支持)

---

### 114. `sed`

流编辑器（Stream Editor），用于对输入文本进行过滤和转换。

#### 语法

```sh
sed [-n] [-e script]... [-f script_file]... [file...]

```

#### 选项与参数

* **`-n`**：取消默认打印输出，仅输出被 `p` 命令显式指定的行。
* **`-e script`**：指定编辑指令脚本。
* **`-f script_file`**：从文件中读取编辑指令。

#### 常见示例

```sh
# 示例 1: 将文件中的 foo 全局替换为 bar
sed 's/foo/bar/g' input.txt

# 示例 2: 仅打印第 10 到第 20 行
sed -n '10,20p' access.log

```

---

### 115. `sh`

POSIX 标准 Shell 命令解释器。

#### 语法

```sh
sh [-abCefhimnuvx] [-o option] [file [argument...]]
sh -c command_string [command_name [argument...]]

```

#### 选项与参数

* **`-c`**：从字符串中读取并执行 Shell 命令。
* **`-e`**：若命令返回非零状态码，则立即退出脚本。
* **`-x`**：在执行每条命令前先将其打印出来（调试模式）。

#### 常见示例

```sh
sh -c 'echo "Current shell PID: $$"'

```

---

### 116. `sleep`

暂停执行指定的秒数。

#### 语法

```sh
sleep time

```

#### 常见示例

```sh
# 轮询时等待 5 秒
sleep 5

```

---

### 117. `sort`

对文本文件的行进行排序、合并或去重。

#### 语法

```sh
sort [-c|-C] [-m] [-u] [-o output] [-k keydef]... [-t char] [file...]

```

#### 选项与参数

* **`-k keydef`**：按指定的列/字段排序（如 `-k2,2` 代表按第二列排序）。
* **`-t char`**：指定列分隔符。
* **`-u`**：排序并去除重复行（Unique）。
* **`-n`**：按数值大小而非字典序排序。
* **`-r`**：逆序排序。

#### 常见示例

```sh
# 按第三列以数字逆序对 /etc/passwd 排序
sort -t: -k3,3 -nr /etc/passwd

```

---

### 118. `split`

将一个大文件拆分为多个较小的片段文件。

#### 语法

```sh
split [-a length] [-b bytes|-l line_count] [file [prefix]]

```

#### 选项与参数

* **`-b bytes`**：按指定的字节大小切割（如 `10m` 或 `100k`）。
* **`-l line_count`**：按指定行数切割。
* **`-a length`**：后缀文件名序号的长度（默认 2 位，如 `xaa`, `xab`）。

#### 常见示例

```sh
# 将大日志按每 50,000 行切割为一个新文件
split -l 50000 large_app.log log_part_

```

---

### 119. `strings`

从二进制文件中提取并打印可打印的 ANSI/ASCII 字符序列。

#### 语法

```sh
strings [-a] [-n number] [-t format] [file...]

```

#### 选项与参数

* **`-n number`**：限定最小连续字符长度（默认 4 个字符）。
* **`-t format`**：显示字符串在文件中的字节偏移地址（`d` 十进制，`x` 十六进制）。

#### 常见示例

```sh
# 在编译好的二进制文件中查找版本标识
strings -n 6 libnet.so | grep -i "version"

```

---

### 120. `strip`

从可执行二进制文件或目标文件中移除符号表（Symbol Table）与调试信息，以减小体积。

#### 语法

```sh
strip file...

```

#### 常见示例

```sh
strip --strip-unneeded main_binary

```

---

### 121. `stty`

设置或打印当前终端行接口（Terminal Line）的控制属性。

#### 语法

```sh
stty [-a|-g]
stty [operand...]

```

#### 选项与参数

* **`-a`**：以人可读的格式输出当前终端的所有详细设置。
* **`-g`**：以可作为参数重新传入 `stty` 的格式输出设置。

#### 常见示例

```sh
# 隐藏键盘输入（通常用于输入密码）
stty -echo
read -r PASSWORD
stty echo

```

---

### 122. `tabs`

设置终端标签页止位（Tab Stops）。

#### 语法

```sh
tabs [-n|-a|-c|-f|-p|-r|-u] [+m[n]] [-T type]

```

#### 常见示例

```sh
# 设置制表符间隔为 4 个空格
tabs -4

```

---

### 123. `tail`

输出文本文件末尾的部分内容（默认最后 10 行）。

#### 语法

```sh
tail [-f] [-c number|-n number] [file]

```

#### 选项与参数

* **`-f`**：持续监视文件（Follow），在文件有新增长时实时打印（常用于日志分析）。
* **`-n number`**：指定输出末尾的行数。

#### 常见示例

```sh
tail -f -n 50 /var/log/syslog

```

---

### 124. `talk`

在多个终端用户之间建立实时双向文本对话。

#### 语法

```sh
talk user_name [tty_name]

```

#### 常见示例

```sh
talk alice tty1

```

---

### 125. `tee`

从标准输入读取数据，并将内容同时写入到标准输出和指定的一个或多个文件中。

#### 语法

```sh
tee [-a] [file...]

```

#### 选项与参数

* **`-a`**：追加模式（Append），不覆盖目标文件原有内容。

#### 常见示例

```sh
make | tee -a build.log

```

---

### 126. `test`

评估条件表达式（Condition Evaluation），返回退出码 0（真）或 1（假）。Shell 中 `[` 为其等价形式。

#### 语法

```sh
test expression
[ expression ]

```

#### 常见操作符

* **文件判断**：`-f`（普通文件），`-d`（目录），`-e`（存在），`-r`（可读）。
* **数值比较**：`-eq`, `-ne`, `-gt`, `-ge`, `-lt`, `-le`。
* **字符串判断**：`-z`（字符串为空），`-n`（非空），`=`（相等）。

#### 常见示例

```sh
test -f /etc/config.json && echo "Config found."

```

---

### 127. `time`

测量并打印运行指定命令所耗费的系统 CPU 时间、用户 CPU 时间和墙上时钟时间（Wall-clock time）。

#### 语法

```sh
time [-p] utility [argument...]

```

#### 选项与参数

* **`-p`**：使用 POSIX 规定的标准三行格式输出（`real`, `user`, `sys`，单位秒）。

#### 常见示例

```sh
time -p ./bench_test

```

---

### 128. `timeout`

在给定的超时限制时间内运行指定的命令，超时后自动向其发送中止信号。

#### 语法

```sh
timeout [-s signal] time utility [argument...]

```

#### 选项与参数

* **`-s signal`**：指定超时时发送的信号（默认 `SIGTERM`）。

#### 常见示例

```sh
# 允许脚本运行最多 10 秒，超时直接杀死
timeout 10 ./network_fetch.sh

```

---

### 129. `touch`

更新文件的访问（Atime）和修改（Mtime）时间戳；若文件不存在，则自动创建一个空文件。

#### 语法

```sh
touch [-a] [-m] [-c] [-r ref_file|-t time] file...

```

#### 选项与参数

* **`-c`**：若文件不存在，则不创建新文件。
* **`-t time`**：指定具体的时间戳，格式为 `[[CC]YY]MMDDhhmm[.ss]`。
* **`-r ref_file`**：将时间戳复制并更新为参考文件 `ref_file` 的时间。

#### 常见示例

```sh
touch -t 202601010000 file.txt

```

---

### 130. `tput`

查询并设置终端的能力库（Terminfo），如移动光标、清屏或改变颜色。

#### 语法

```sh
tput [-T type] capname [parm...]

```

#### 常见示例

```sh
# 示例 1: 清空终端屏幕
tput clear

# 示例 2: 打印加粗文本
tput bold; echo "Important"; tput sgr0

```

---

### 131. `tr`

按字符转换（Translate）或删除标准输入中的指定字符集。

#### 语法

```sh
tr [-c|-C] [-d] [-s] string1 [string2]

```

#### 选项与参数

* **`-d`**：删除匹配 `string1` 的字符。
* **`-s`**：挤压（Squeeze）连续重复的匹配字符为单个字符。
* **`-c`**：对 `string1` 取补集。

#### 常见示例

```sh
# 示例 1: 将小写转换为大写
echo "hello" | tr 'a-z' 'A-Z'

# 示例 2: 删除 Windows 回车符 \r
cat script.sh | tr -d '\r'

```

---

### 132. `true`

空操作命令，除了**返回退出状态码 0** 之外不做任何事情。

#### 语法

```sh
true

```

#### 常见示例

```sh
# 在 Shell 中创建无限循环
while true; do
    ./ping.sh
    sleep 1
done

```

---

### 133. `tsort`

对输入的有向图节点进行拓扑排序（Topological Sort），常用于依赖关系决议。

#### 语法

```sh
tsort [file]

```

#### 常见示例

```sh
# 输入节点依赖对：A 依赖 B, B 依赖 C
cat << 'EOF' | tsort
A B
B C
EOF
# 输出拓扑顺序: C B A

```

---

### 134. `tty`

打印当前标准输入所连接的终端设备节点路径（Terminal Name）。

#### 语法

```sh
tty [-s]

```

#### 选项与参数

* **`-s`**：静默模式（Silent），仅通过退出码判断标准输入是否为终端。

#### 常见示例

```sh
tty
# 输出如: /dev/pts/0

```

---

### 135. `type`

确定传入的名称是 Shell 内置命令、外部可执行文件、别名（Alias）还是 Shell 函数。

#### 语法

```sh
type name...

```

#### 常见示例

```sh
type cd ls grep

```

### 136. `ulimit`

显示或设置当前 Shell 及其子进程能够使用的系统资源限制（如最大打开文件数、栈大小、进程数等）。

#### 语法

```sh
ulimit [-f] [n]

```

#### 选项与参数

* **`-f`**：设置或显示可以创建的最大文件块数（单位为 512 字节）。
* *(注：POSIX 仅明确规定了 `-f` 选项，现代 Shell 实现如 bash/zsh 扩展了 `-n`、`-u` 等选项)*

#### 常见示例

```sh
# 查询可创建文件的最大块数限制
ulimit -f

```

---

### 137. `umask`

设置或显示文件创建掩码（File Mode Creation Mask），决定新创建文件与目录的默认权限。

#### 语法

```sh
umask [-S] [mask]

```

#### 选项与参数

* **`-S`**：以符号（Symbolic）形式打印或设置掩码，方便阅读。
* **`mask`**：八进制数字或符号表达式（如 `022` 或 `u=rwx,g=rx,o=rx`）。

#### 常见示例

```sh
# 设置掩码为 022（新文件默认 644，新目录默认 755）
umask 022

```

---

### 138. `unalias`

移除由 `alias` 定义的 Shell 别名。

#### 语法

```sh
unalias alias_name...
unalias -a

```

#### 选项与参数

* **`-a`**：移除当前 Shell 会话中的所有别名。

#### 常见示例

```sh
unalias ls

```

---

### 139. `uname`

打印当前运行系统的名称及硬件平台属性（System Information）。

#### 语法

```sh
uname [-a|-m|-n|-r|-s|-v]

```

#### 选项与参数

* **`-a`**：打印所有可用的系统属性信息。
* **`-s`**：内核/操作系统名称（系统默认行为）。
* **`-m`**：硬件架构类型（如 `x86_64` 或 `aarch64`）。
* **`-r`**：操作系统内核版本发布号（Release）。

#### 常见示例

```sh
uname -smr

```

---

### 140. `uncompress`

解压由 `compress` 压缩的 `.Z` 格式归档文件。

#### 语法

```sh
uncompress [-c] [-f] [file...]

```

#### 选项与参数

* **`-c`**：将解压后的文本数据直接发送到标准输出，不改变原文件。

#### 常见示例

```sh
uncompress archive.tar.Z

```

---

### 141. `unget` (linux上不支持)

---

### 142. `unexpand`

将文本文件中的连续空格字符转换为制表符（Tab）。

#### 语法

```sh
unexpand [-a|-t tablist] [file...]

```

#### 选项与参数

* **`-a`**：将所有连续的空格序列转换为制表符（默认仅处理每行开头的空格）。
* **`-t tablist`**：指定制表符所代表的列宽。

#### 常见示例

```sh
unexpand -a input.txt > formatted.txt

```

---

### 143. `uniq`

检测并过滤文本文件中的相邻重复行（通常配合 `sort` 使用）。

#### 语法

```sh
uniq [-c|-d|-u] [-f fields] [-s chars] [input_file [output_file]]

```

#### 选项与参数

* **`-c`**：在每行开头前缀打印该行连续出现的次数。
* **`-d`**：仅输出存在重复的行。
* **`-u`**：仅输出完全没有重复的唯一行（Unique）。

#### 常见示例

```sh
# 统计文本中不同词条的出现频率
sort keywords.txt | uniq -c | sort -nr

```

---

### 144. `unlink`

直接调用底层的 `unlink()` 系统调用，删除指定的文件系统入口点。

#### 语法

```sh
unlink file

```

#### 常见示例

```sh
unlink unused_link.tmp

```

---

### 145. `uucp` (linux上不支持)

---

### 146. `uudecode`

将通过 `uuencode` 生成的包含 ASCII 可打印字符的二进制编码文本还原为原始二进制文件。

#### 语法

```sh
uudecode [-o outfile] [file]

```

#### 选项与参数

* **`-o outfile`**：重定向输出到指定的目标二进制文件。

#### 常见示例

```sh
uudecode -o image.png encoded_image.txt

```

---

### 147. `uuencode`

将二进制文件编码为仅包含可打印 ASCII 字符的文本文件，以便在不支持二进制传输的传统介质中传输。

#### 语法

```sh
uuencode [-m] [file] decode_pathname

```

#### 选项与参数

* **`-m`**：使用 Base64 算法进行编码（默认使用传统的 uuencode 编解码算法）。

#### 常见示例

```sh
uuencode -m payload.bin payload.bin > encoded.txt

```

---

### 148. `uustat` (linux上不支持)

---

### 149. `uux` (linux上不支持)

---

### 150. `val` (linux上不支持)

---

### 151. `vi`

POSIX 标准定义的可视化全屏幕文本编辑器（Visual Display Editor）。

#### 语法

```sh
vi [-rR] [-c command] [-t tagstring] [file...]

```

#### 选项与参数

* **`-R`**：只读模式（Read-only）。
* **`-r`**：恢复崩溃前保存的编辑会话缓冲区。
* **`-c command`**：打开文件后立即执行给定的 `ex` 编辑指令。

#### 常见示例

```sh
vi +100 main.c  # 打开 main.c 并定位到第 100 行

```

---

### 152. `wait`

挂起当前 Shell 进程，直到指定的后台进程 PID 或作业运行结束，并返回其退出状态码。

#### 语法

```sh
wait [pid|job_id...]

```

#### 常见示例

```sh
# 在后台启动任务并在 Shell 脚本中等待其结束
./async_build.sh &
BUILD_PID=$!
wait $BUILD_PID
echo "Build finished with exit code $?"

```

---

### 153. `wc`

统计文本文件或标准输入中的行数（Line）、词数（Word）以及字节数/字符数（Byte/Character）。

#### 语法

```sh
wc [-c|-m] [-l] [-w] [file...]

```

#### 选项与参数

* **`-l`**：仅统计换行符出现的行数。
* **`-w`**：仅统计单词数（以空白分隔的字符序列）。
* **`-c`**：仅统计字节数（Bytes）。
* **`-m`**：仅统计多字节字符数（Characters）。

#### 常见示例

```sh
# 统计源代码文件的总行数
wc -l src/*.c

```

---

### 154. `what` (linux上不支持)

---

### 155. `who`

显示当前已登录系统的用户列表及其连接终端信息。

#### 语法

```sh
who [-a|-b|-d|-H|-l|-m|-p|-q|-r|-s|-t|-u] [file]
who am i

```

#### 选项与参数

* **`-H`**：打印输出列表的表头。
* **`am i` / `am I**`：仅输出当前终端会话的用户登录信息。

#### 常见示例

```sh
who -H

```

---

### 156. `write`

向指定已登录用户的终端屏幕实时发送短消息。

#### 语法

```sh
write user_name [tty_name]

```

#### 常见示例

```sh
write alice pts/1

```

---

### 157. `xargs`

从标准输入读取以空白或换行分隔的字符串列表，并将它们作为参数构造并循环调用指定的实用程序。

#### 语法

```sh
xargs [-E eofstr] [-I replstr|-L number|-n number] [-p|-t] [-s size] [utility [argument...]]

```

#### 选项与参数

* **`-n number`**：限制每次调用命令时传入的最大参数个数。
* **`-I replstr`**：将参数替换到指定位置的占位符字符串中。
* **`-t`**：在执行构造出的命令之前，先打印命令本身到标准错误。

#### 常见示例

```sh
# 将找到的所有 .tmp 文件传递给 rm 批量删除
find . -name "*.tmp" | xargs rm -f

```

---

### 158. `yacc` (Yet Another Compiler-Compiler)

根据给定的上下文无关文法（Grammar）产生式规则，自动生成 C 语言语法分析器（Parser）代码。

#### 语法

```sh
yacc [-b prefix] [-d] [-t] [-v] grammar

```

#### 选项与参数

* **`-d`**：额外生成包含 `token` 码定义的头文件（默认文件名为 `y.tab.h`）。
* **`-b prefix`**：更改生成文件的前缀（默认为 `y.`）。

#### 常见示例

```sh
yacc -d parser.y

```

---

### 159. `zcat`

解压并直接输出 `.Z`（或现代 Linux 扩展的 `.gz`）压缩文件的内容到标准输出，而不修改原始压缩包。

#### 语法

```sh
zcat [file...]

```

#### 常见示例

```sh
zcat sys_log.gz | grep "FATAL"

```

