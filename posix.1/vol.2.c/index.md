# System Interfaces (XSH) 卷大纲

> - [大纲](https://pubs.opengroup.org/onlinepubs/9799919799/functions/contents.html)
> - [1. Introduction](https://pubs.opengroup.org/onlinepubs/9799919799/functions/V2_chap01.html) → [英文原文](1.introduction/index.html) / [中文直译](1.introduction-translate/index.html) / [导读](1.introduction-AI-guide/index.html)
> - [2. General Information](https://pubs.opengroup.org/onlinepubs/9799919799/functions/V2_chap02.html) → [英文原文](2.general-information/index.html) / [中文直译](2.general-information-translate/index.html) / [导读](2.general-information-AI-guide/index.html)
> - [3. System Interfaces（函数参考页）](https://pubs.opengroup.org/onlinepubs/9799919799/functions/contents.html) → [函数清单](3.functions/index.html)

POSIX Standard（IEEE Std 1003.1-2024 / Issue 8）的《System Interfaces》卷（Vol. 2，C 语言接口）——**三章主体全部推进**：前 2 章完整三兄弟；第 3 章函数参考页（官方共 699 个函数页）已建立 **713 个函数总清单**，并完成 **78 个核心函数的原文/直译/导读三兄弟**。

> **三兄弟结构说明**：每章维护三份文档——`英文原文`（官方 HTML 经 template 适配转换，保留全部文本与锚点）、`中文直译`（结构镜像原文，段对段/条对条/层对层，便于中英对照）、`AI 导读`（同编号的结构化讲解，机制层 + 延伸阅读）。三份 HTML 均完全适配 `template.html` 渲染。

### 1. Introduction（引言）→ [1.introduction/index.html](1.introduction/index.html)

* **1.1 Relationship to Other Formal Standards**：本卷与 ISO C（C17）、IEEE 754 等标准的关系。
* **1.2 Format of Entries**：函数条目（reference page）的格式说明（SYNOPSIS / DESCRIPTION / RETURN VALUE / ERRORS 等小节）。

### 2. General Information（通用信息）→ [2.general-information/index.html](2.general-information/index.html)

* **2.1 Use and Implementation of Interfaces**：函数与宏的使用与实现规则（未定义行为、宏的抑制、数据竞争限制）。
* **2.2 The Compilation Environment**：编译环境——POSIX.1 符号、名字空间、功能测试宏（`_POSIX_C_SOURCE`、`_XOPEN_SOURCE`）。
* **2.3 Error Numbers**：错误编号体系与全部 errno 宏（`E2BIG` … `EXDEV`）的语义。
* **2.4 Signal Concepts**：信号概念——产生与递送、实时信号、信号动作（`SIG_DFL`/`SIG_IGN`/函数指针）、信号对其他函数的影响。
* **2.5 Standard I/O Streams**：标准 I/O 流——文件描述符交互、流方向性与编码规则。
* **2.6 File Descriptor Allocation**：文件描述符分配规则。
* **2.7 XSI Interprocess Communication**：XSI 进程间通信（消息队列、信号量、共享内存）总述。
* **2.8 Realtime**：实时扩展——异步 I/O、内存管理、进程调度（`SCHED_FIFO` 等策略）、时钟与定时器。
* **2.9 Threads**：线程——线程安全、互斥量、调度、取消、读写锁、与应用管理线程栈。
* **2.10 Sockets**：套接字——地址族、寻址、协议、套接字类型、选项（`SO_*`）、本地 UNIX / IPv4 / IPv6。
* **2.11 Data Types**：数据类型——已定义类型（`size_t`、`off_t` 等）与 char 类型。
* **2.12 Status Information**：状态信息——`wait()`/`waitid()`/`waitpid()` 返回的进程状态语义。

### 3. System Interfaces（系统接口函数参考页）→ [函数清单](3.functions/index.html)

第一层为 [函数总清单](3.functions/index.html)：713 个函数（官方 TOC 699 + 补充 14 个共用页主名，如 `stat`/`printf`/`execve`），含序号、头文件、中文简介，已翻译的 78 个核心函数链接本地，其余链接官方页面。第二层为 78 个核心函数的三兄弟（每函数 `<fn>/index.html` 原文、`<fn>-translate/index.html` 直译、`<fn>-AI-guide/index.html` 导读）：

* **文件描述符与文件 I/O**：`open` `read` `write` `close` `lseek` `pread` `pwrite` `fcntl` `dup` `dup2` `stat` `fstat` `lstat` `ftruncate` `fsync`
* **进程与程序执行**：`fork` `execve` `exit` `_exit` `abort` `atexit` `system` `getpid` `kill`
* **信号与定时**：`signal` `sigaction` `sigprocmask` `raise` `alarm` `sleep` `nanosleep`
* **线程**：`pthread_create` `pthread_join` `pthread_exit` `pthread_self` `pthread_once` `pthread_key_create` `pthread_mutex_lock` `pthread_mutex_unlock` `pthread_cond_wait` `pthread_cond_signal` `pthread_cancel`
* **套接字**：`socket` `bind` `listen` `accept` `connect` `send` `recv` `getsockopt` `setsockopt`
* **内存与格式化**：`malloc` `free` `realloc` `calloc` `mmap` `munmap` `printf` `fprintf` `sprintf` `snprintf`
* **标准 I/O 与字符串**：`fopen` `fclose` `fread` `fwrite` `fgets` `fputs` `fflush` `strtok` `strtol` `getenv`
* **环境与目录**：`setenv` `chdir` `getcwd` `unlink` `rename` `mkdir` `rmdir`

---

**进度**：第 1 章（34 节点）与第 2 章（1477 节点）三兄弟全部完成（2026-08-27），HTML 经 `tools/adapt_template.py` 适配 `template.html`。第 3 章已完成函数总清单（713 个）与 78 个核心函数三兄弟（2026-08-27）；其余 621 个函数页待后续分批翻译。
