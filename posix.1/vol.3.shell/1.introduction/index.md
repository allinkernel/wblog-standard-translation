<!-- 英文原文镜像：https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap01.html -->
<body bgcolor="white">

<a name="top" id="top">
<h2><a name="tag_18" id="tag_18">1. Introduction
<p>The Shell and Utilities volume of POSIX.1-2024 describes the commands and utilities offered to application programs by
POSIX-conformant systems.
<h3><a name="tag_18_01" id="tag_18_01">1.1 Relationship to Other Documents
<h4><a name="tag_18_01_01" id="tag_18_01_01">1.1.1 System Interfaces
<p>This subsection describes some of the features provided by the System Interfaces volume of POSIX.1-2024 that are assumed to be
globally available on all systems conforming to this volume of POSIX.1-2024. This subsection does not attempt to detail all of the
features defined in the System Interfaces volume of POSIX.1-2024 that are required by all of the utilities defined in this volume
of POSIX.1-2024; the utility and function descriptions point out additional functionality required to provide the corresponding
specific features needed by each.
<p>The following subsections describe frequently used concepts. Many of these concepts are described in the Base Definitions volume
of POSIX.1-2024. Utility and function description statements override these defaults when appropriate.
<h5 class="header4"><a name="tag_18_01_01_01" id="tag_18_01_01_01">1.1.1.1 Process Attributes
<p>The following process attributes, as described in the System Interfaces volume of POSIX.1-2024, are assumed to be supported for
all processes in this volume of POSIX.1-2024:
<table cellpadding="3">
<tr valign="top">
<td align="left">
<p class="tent"><br>
Controlling Terminal<br>
Current Working Directory<br>
Effective Group ID<br>
Effective User ID<br>
File Descriptors<br>
File Mode Creation Mask<br>
Process Group ID<br>
Process ID<br>

<td align="left">
<p class="tent"><br>
Real Group ID<br>
Real User ID<br>
Root Directory<br>
Saved Set-Group-ID<br>
Saved Set-User-ID<br>
Session Membership<br>
Supplementary Group IDs<br>

<p class="tent">A conforming implementation may include additional process attributes.
<h5 class="header4"><a name="tag_18_01_01_02" id="tag_18_01_01_02">1.1.1.2 Concurrent Execution of Processes
<p class="tent">The following functionality of the <a href="../functions/fork.html"><i>fork() function defined in the
System Interfaces volume of POSIX.1-2024 shall be available on all systems conforming to this volume of POSIX.1-2024:
<ol>
<li class="tent">Independent processes shall be capable of executing independently without either process terminating.
<li class="tent">A process shall be able to create a new process with all of the attributes referenced in <a href=
"#tag_18_01_01_01">1.1.1.1 Process Attributes, determined according to the semantics of a call to the <a href=
"../functions/fork.html"><i>fork() function defined in the System Interfaces volume of POSIX.1-2024 followed by a call in
the child process to one of the <i>exec functions defined in the System Interfaces volume of POSIX.1-2024.

<h5 class="header4"><a name="tag_18_01_01_03" id="tag_18_01_01_03">1.1.1.3 File Access Permissions
<p class="tent">The file access control mechanism described by XBD <a href="../basedefs/V1_chap04.html#tag_04_07"><i>4.7 File
Access Permissions shall apply to all files on an implementation conforming to this volume of POSIX.1-2024.
<h5 class="header4"><a name="tag_18_01_01_04" id="tag_18_01_01_04">1.1.1.4 File Read, Write, and Creation
<p class="tent">If a file that does not exist is to be written, it shall be created as described below, unless the utility
description states otherwise.
<p class="tent">When a file that does not exist is created, the following features defined in the System Interfaces volume of
POSIX.1-2024 shall apply unless the utility or function description states otherwise:
<ol>
<li class="tent">The user ID of the file shall be set to the effective user ID of the calling process.
<li class="tent">The group ID of the file shall be set to the effective group ID of the calling process or the group ID of the
directory in which the file is being created.
<li class="tent">If the file is a regular file, the permission bits of the file shall be set to: S&#95;IROTH | S&#95;IWOTH | S&#95;IRGRP |
S&#95;IWGRP | S&#95;IRUSR | S&#95;IWUSR
<p class="tent">(see the description of <i>File Modes in XBD <a href="../basedefs/V1_chap14.html#tag_14"><i>14. Headers
, <a href="../basedefs/sys_stat.h.html"><i>&lt;sys/stat.h&gt;) except that the bits specified by the file mode creation
mask of the process shall be cleared. If the file is a directory, the permission bits shall be set to: S&#95;IRWXU | S&#95;IRWXG |
S&#95;IRWXO
<p class="tent">except that the bits specified by the file mode creation mask of the process shall be cleared.

<li class="tent">The last data access, last data modification, and last file status change timestamps of the file shall be updated
as specified in XBD <a href="../basedefs/V1_chap04.html#tag_04_12"><i>4.12 File Times Update.
<li class="tent">If the file is a directory, it shall be an empty directory; otherwise, the file shall have length zero.
<li class="tent">If the file is a symbolic link, the effect shall be undefined unless the {POSIX2&#95;SYMLINKS} variable is in effect
for the directory in which the symbolic link would be created.
<li class="tent">Unless otherwise specified, the file created shall be a regular file.

<p class="tent">When an attempt is made to create a file that already exists, the utility shall take the action indicated in
<a href="#tagtcjh_9">Actions when Creating a File that Already Exists corresponding to the type of the file the utility is
trying to create and the type of the existing file, unless the utility description states otherwise.
<p class="caption"><a name="tagtcjh_9" id="tagtcjh_9"> Table: Actions when Creating a File that Already Exists
<center>
<table border="1" cellpadding="3" align="center">
<tr valign="top">
<th colspan="2" align="center">
<p class="tent"><b> 

<th colspan="11" align="center">
<p class="tent"><b>New Type

<th align="center">
<p class="tent"><b> 

<tr valign="top">
<th colspan="2" align="center">
<p class="tent"><b>Existing Type

<th align="center">
<p class="tent"><b>B

<th align="center">
<p class="tent"><b>C

<th align="center">
<p class="tent"><b>D

<th align="center">
<p class="tent"><b>F

<th align="center">
<p class="tent"><b>L

<th align="center">
<p class="tent"><b>M

<th align="center">
<p class="tent"><b>P

<th align="center">
<p class="tent"><b>Q

<th align="center">
<p class="tent"><b>R

<th align="center">
<p class="tent"><b>S

<th align="center">
<p class="tent"><b>T

<th align="center">
<p class="tent"><b>Function Creating New

<tr valign="top">
<td align="left">
<p class="tent">B

<td align="left">
<p class="tent">Block Special

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">U

<td align="center">
<p class="tent">U

<td align="center">
<p class="tent">U

<td align="center">
<p class="tent">OF

<td align="center">
<p class="tent">U

<td align="center">
<p class="tent">U

<td align="left">
<p class="tent"><i>mknod()&#42;&#42;

<tr valign="top">
<td align="left">
<p class="tent">C

<td align="left">
<p class="tent">Character Special

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">U

<td align="center">
<p class="tent">U

<td align="center">
<p class="tent">U

<td align="center">
<p class="tent">OF

<td align="center">
<p class="tent">U

<td align="center">
<p class="tent">U

<td align="left">
<p class="tent"><i>mknod()&#42;&#42;

<tr valign="top">
<td align="left">
<p class="tent">D

<td align="left">
<p class="tent">Directory

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">U

<td align="left">
<p class="tent"><i>mkdir()

<tr valign="top">
<td align="left">
<p class="tent">F

<td align="left">
<p class="tent">FIFO Special File

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">O

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">U

<td align="left">
<p class="tent"><i>mkfifo()

<tr valign="top">
<td align="left">
<p class="tent">L

<td align="left">
<p class="tent">Symbolic Link

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">FL

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">U

<td align="left">
<p class="tent"><i>symlink()

<tr valign="top">
<td align="left">
<p class="tent">M

<td align="left">
<p class="tent">Shared Memory

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">U

<td align="left">
<p class="tent"><i>shm&#95;open()

<tr valign="top">
<td align="left">
<p class="tent">P

<td align="left">
<p class="tent">Semaphore

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">U

<td align="left">
<p class="tent"><i>sem&#95;open()

<tr valign="top">
<td align="left">
<p class="tent">Q

<td align="left">
<p class="tent">Message Queue

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">U

<td align="left">
<p class="tent"><i>mq&#95;open()

<tr valign="top">
<td align="left">
<p class="tent">R

<td align="left">
<p class="tent">Regular File

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">RF

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">U

<td align="left">
<p class="tent"><i>open()

<tr valign="top">
<td align="left">
<p class="tent">S

<td align="left">
<p class="tent">Socket

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">—

<td align="center">
<p class="tent">U

<td align="left">
<p class="tent"><i>bind()

<tr valign="top">
<td align="left">
<p class="tent">T

<td align="left">
<p class="tent">Typed Memory

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">F

<td align="center">
<p class="tent">U

<td align="center">
<p class="tent">U

<td align="center">
<p class="tent">U

<td align="center">
<p class="tent">U

<td align="center">
<p class="tent">U

<td align="center">
<p class="tent">U

<td align="left">
<p class="tent">&#42;

<p class="tent">The following codes are used in <a href="#tagtcjh_9">Actions when Creating a File that Already Exists:
<dl compact>
<dd>
<dt>F
<dd>Fail. The attempt to create the new file shall fail and the utility shall either continue with its operation or exit
immediately with an exit status that indicates an error occurred, depending on the description of the utility.
<dt>FL
<dd>Follow link. Unless otherwise specified, the symbolic link shall be followed as specified for pathname resolution, and the
operation performed shall be as if the target of the symbolic link (after all resolution) had been named. If the target of the
symbolic link does not exist, it shall be as if that nonexistent target had been named directly.
<dt>O
<dd>Open FIFO. When attempting to create a regular file, and the existing file is a FIFO special file:
<ol>
<li class="tent">If the FIFO is not already open for reading, the attempt shall block until the FIFO is opened for reading.
<li class="tent">Once the FIFO is open for reading, the utility shall open the FIFO for writing and continue with its
operation.

<dt>OF
<dd>The named file shall be opened with the consequences defined for that file type.
<dt>RF
<dd>Regular file. When attempting to create a regular file, and the existing file is a regular file:
<ol>
<li class="tent">The user ID, group ID, and permission bits of the file shall not be changed.
<li class="tent">The file shall be truncated to zero length.
<li class="tent">The last data modification and last file status change timestamps shall be marked for update.

<dt>—
<dd>The effect is implementation-defined unless specified by the utility description.
<dt>U
<dd>The effect is unspecified unless specified by the utility description.
<dt>&#42;
<dd>There is no portable way to create a file of this type.
<dt>&#42;&#42;
<dd>Not portable.

<p class="tent">When a file is to be appended, the file shall be opened in a manner equivalent to using the O&#95;APPEND flag, without
the O&#95;TRUNC flag, in the <a href="../functions/open.html"><i>open() function defined in the System Interfaces volume of
POSIX.1-2024.
<p class="tent">When a file is to be read or written, the file shall be opened with an access mode corresponding to the operation
to be performed. If file access permissions deny access, the requested operation shall fail.
<h5 class="header4"><a name="tag_18_01_01_05" id="tag_18_01_01_05">1.1.1.5 File Removal
<p class="tent">When a directory that is the root directory or current working directory of any process is removed, the effect is
implementation-defined. If file access permissions deny access, the requested operation shall fail. Otherwise, when a file is
removed:
<ol>
<li class="tent">Its directory entry shall be removed from the file system.
<li class="tent">The link count of the file shall be decremented.
<li class="tent">If the file is an empty directory (see XBD <a href="../basedefs/V1_chap03.html#tag_03_119"><i>3.119 Empty
Directory):
<ol type="a">
<li class="tent">If no process has the directory open, the space occupied by the directory shall be freed and the directory shall
no longer be accessible.
<li class="tent">If one or more processes have the directory open, the directory contents shall be preserved until all references
to the file have been closed.

<li class="tent">If the file is a directory that is not empty, the last file status change timestamp shall be marked for
update.
<li class="tent">If the file is not a directory:
<ol type="a">
<li class="tent">If the link count becomes zero:
<ol type="i">
<li class="tent">If no process has the file open, the space occupied by the file shall be freed and the file shall no longer be
accessible.
<li class="tent">If one or more processes have the file open, the file contents shall be preserved until all references to the file
have been closed.

<li class="tent">If the link count is not reduced to zero, the last file status change timestamp shall be marked for update.

<li class="tent">The last data modification and last file status change timestamps of the containing directory shall be marked for
update.

<h5 class="header4"><a name="tag_18_01_01_06" id="tag_18_01_01_06">1.1.1.6 File Time Values
<p class="tent">All files shall have the three time values described by XBD <a href="../basedefs/V1_chap04.html#tag_04_12"><i>4.12
File Times Update.
<h5 class="header4"><a name="tag_18_01_01_07" id="tag_18_01_01_07">1.1.1.7 File Contents
<p class="tent">When a reference is made to the contents of a file, <i>pathname, this means the equivalent of all of the data
placed in the space pointed to by <i>buf when performing the <a href="../functions/read.html"><i>read() function calls
in the following operations defined in the System Interfaces volume of POSIX.1-2024:
<pre>
<tt>while (read (fildes, buf, nbytes) &gt; 0)
    ;

<p class="tent">If the file is indicated by a pathname <i>pathname, the file descriptor shall be determined by the equivalent
of the following operation defined in the System Interfaces volume of POSIX.1-2024:
<pre>
<tt>fildes = open (pathname, O&#95;RDONLY);

<p class="tent">The value of <i>nbytes in the above sequence is unspecified; if the file is of a type where the data returned
by <a href="../functions/read.html"><i>read() would vary with different values, the value shall be one that results in the
most data being returned.
<p class="tent">If the <a href="../functions/read.html"><i>read() function calls would return an error, it is unspecified
whether the contents of the file are considered to include any data from offsets in the file beyond where the error would be
returned.
<h5 class="header4"><a name="tag_18_01_01_08" id="tag_18_01_01_08">1.1.1.8 Pathname Resolution
<p class="tent">The pathname resolution algorithm, described by XBD <a href="../basedefs/V1_chap04.html#tag_04_16"><i>4.16 Pathname
Resolution, shall be used by implementations conforming to this volume of POSIX.1-2024; see also XBD <a href=
"../basedefs/V1_chap04.html#tag_04_08"><i>4.8 File Hierarchy.
<h5 class="header4"><a name="tag_18_01_01_09" id="tag_18_01_01_09">1.1.1.9 Changing the Current Working Directory
<p class="tent">When the current working directory (see XBD <a href="../basedefs/V1_chap03.html#tag_03_94"><i>3.94 Current Working
Directory) is to be changed, unless the utility or function description states otherwise, the operation shall succeed
unless a call to the <a href="../functions/chdir.html"><i>chdir() function defined in the System Interfaces volume of
POSIX.1-2024 would fail when invoked with the new working directory pathname as its argument.
<h5 class="header4"><a name="tag_18_01_01_10" id="tag_18_01_01_10">1.1.1.10 Establish the Locale
<p class="tent">The functionality of the <a href="../functions/setlocale.html"><i>setlocale() function defined in the
System Interfaces volume of POSIX.1-2024 shall be available on all systems conforming to this volume of POSIX.1-2024; that is,
utilities that require the capability of establishing an international operating environment shall be permitted to set the
specified category of the international environment.
<h5 class="header4"><a name="tag_18_01_01_11" id="tag_18_01_01_11">1.1.1.11 Actions Equivalent to Functions
<p class="tent">Some utility descriptions specify that a utility performs actions equivalent to a function defined in the System
Interfaces volume of POSIX.1-2024. Such specifications require only that the external effects be equivalent, not that any effect
within the utility and visible only to the utility be equivalent.
<h4><a name="tag_18_01_02" id="tag_18_01_02">1.1.2 Concepts Derived from the ISO C Standard
<p class="tent">Some of the standard utilities perform complex data manipulation using their own procedure and arithmetic
languages, as defined in their EXTENDED DESCRIPTION or OPERANDS sections. Unless otherwise noted, the arithmetic and semantic
concepts (precision, type conversion, control flow, and so on) shall be equivalent to those defined in the ISO C standard, as
described in the following sections. Note that there is no requirement that the standard utilities be implemented in any particular
programming language.
<h5 class="header4"><a name="tag_18_01_02_01" id="tag_18_01_02_01">1.1.2.1 Arithmetic Precision and Operations
<p class="tent">Integer variables and constants, including the values of operands and option-arguments, used by the standard
utilities listed in this volume of POSIX.1-2024 shall be implemented as equivalent to the ISO C standard <b>signed long
data type; floating point shall be implemented as equivalent to the ISO C standard <b>double type. Conversions between
types shall be as described in the ISO C standard. All variables shall be initialized to zero if they are not otherwise
assigned by the input to the application.
<p class="tent">Arithmetic operators and control flow keywords shall be implemented as equivalent to those in the cited ISO C
standard section, as listed in <a href="#tagtcjh_10">Selected ISO C Standard Operators and Control Flow Keywords.
<basefont size="2">
<dl>
<dt><b>Note:
<dd>The comma operator (section 6.5.17 of the ISO C standard) is intentionally not included in the table. It need not be
supported by implementations.

<basefont size="3">
<p class="caption"><a name="tagtcjh_10" id="tagtcjh_10"> Table: Selected ISO C Standard Operators and Control Flow Keywords
<center>
<table border="1" cellpadding="3" align="center">
<tr valign="top">
<th align="center">
<p class="tent"><b>Operation

<th align="center">
<p class="tent"><b>ISO C Standard Equivalent Reference

<tr valign="top">
<td align="left">
<p class="tent">()

<td align="left">
<p class="tent">Section 6.5.1, Primary Expressions

<tr valign="top">
<td align="left">
<p class="tent">postfix ++<br>
postfix &#45;&#45;

<td align="left">
<p class="tent">Section 6.5.2, Postfix Operators

<tr valign="top">
<td align="left">
<p class="tent">unary +<br>
unary -<br>
prefix ++<br>
prefix &#45;&#45;<br>
~<br>
!<br>
<i>sizeof()

<td align="left">
<p class="tent">Section 6.5.3, Unary Operators

<tr valign="top">
<td align="left">
<p class="tent">&#42;<br>
/<br>
%

<td align="left">
<p class="tent">Section 6.5.5, Multiplicative Operators

<tr valign="top">
<td align="left">
<p class="tent">+<br>
-

<td align="left">
<p class="tent">Section 6.5.6, Additive Operators

<tr valign="top">
<td align="left">
<p class="tent">&lt;&lt;<br>
&gt;&gt;

<td align="left">
<p class="tent">Section 6.5.7, Bitwise Shift Operators

<tr valign="top">
<td align="left">
<p class="tent">&lt;, &lt;=<br>
&gt;, &gt;=

<td align="left">
<p class="tent">Section 6.5.8, Relational Operators

<tr valign="top">
<td align="left">
<p class="tent">==<br>
!=

<td align="left">
<p class="tent">Section 6.5.9, Equality Operators

<tr valign="top">
<td align="left">
<p class="tent">&amp;

<td align="left">
<p class="tent">Section 6.5.10, Bitwise AND Operator

<tr valign="top">
<td align="left">
<p class="tent">^

<td align="left">
<p class="tent">Section 6.5.11, Bitwise Exclusive OR Operator

<tr valign="top">
<td align="left">
<p class="tent">|

<td align="left">
<p class="tent">Section 6.5.12, Bitwise Inclusive OR Operator

<tr valign="top">
<td align="left">
<p class="tent">&amp;&amp;

<td align="left">
<p class="tent">Section 6.5.13, Logical AND Operator

<tr valign="top">
<td align="left">
<p class="tent">||

<td align="left">
<p class="tent">Section 6.5.14, Logical OR Operator

<tr valign="top">
<td align="left">
<p class="tent"><i>expr?<i>expr:<i>expr

<td align="left">
<p class="tent">Section 6.5.15, Conditional Operator

<tr valign="top">
<td align="left">
<p class="tent">=, &#42;=, /=, %=, +=, -=<br>
&lt;&lt;=, &gt;&gt;=, &amp;=, ^=, |=

<td align="left">
<p class="tent">Section 6.5.16, Assignment Operators

<tr valign="top">
<td align="left">
<p class="tent"><b>if ()<br>
<b>if () &#46;&#46;&#46; <b>else<br>
<b>switch ()

<td align="left">
<p class="tent">Section 6.8.4, Selection Statements

<tr valign="top">
<td align="left">
<p class="tent"><b>while ()<br>
<b>do &#46;&#46;&#46; <b>while ()<br>
<b>for ()

<td align="left">
<p class="tent">Section 6.8.5, Iteration Statements

<tr valign="top">
<td align="left">
<p class="tent"><b>goto<br>
<b>continue<br>
<b>break<br>
<b>return

<td align="left">
<p class="tent">Section 6.8.6, Jump Statements

<br>
<p class="tent">The evaluation of arithmetic expressions shall be equivalent to that described in Section 6.5, Expressions, of the
ISO C standard.
<h5 class="header4"><a name="tag_18_01_02_02" id="tag_18_01_02_02">1.1.2.2 Mathematical Functions
<p class="tent">Any mathematical functions with the same names as those in the following sections of the ISO C standard:
<ul>
<li class="tent">Section 7.12, Mathematics, <tt>&lt;math.h&gt;
<li class="tent">Section 7.22.2, Pseudo-Random Sequence Generation Functions

<p class="tent">shall be implemented to return the results equivalent to those returned from a call to the corresponding function
described in the ISO C standard.
<h3><a name="tag_18_02" id="tag_18_02">1.2 Utility Limits
<p class="tent">This section lists magnitude limitations imposed by a specific implementation. The braces notation, {LIMIT}, is
used in this volume of POSIX.1-2024 to indicate these values, but the braces are not part of the name.<br>
<p class="caption"><a name="tagtcjh_11" id="tagtcjh_11"> Table: Utility Limit Minimum Values
<center>
<table border="1" cellpadding="3" align="center">
<tr valign="top">
<th align="center">
<p class="tent"><b>Name

<th align="center">
<p class="tent"><b>Description

<th align="center">
<p class="tent"><b>Value

<tr valign="top">
<td align="left">
<p class="tent">{POSIX2&#95;BC&#95;BASE&#95;MAX}

<td align="left">
<p class="tent">The maximum <i>obase value allowed by the <a href="../utilities/bc.html"><i>bc utility.

<td align="left">
<p class="tent">99

<tr valign="top">
<td align="left">
<p class="tent">{POSIX2&#95;BC&#95;DIM&#95;MAX}

<td align="left">
<p class="tent">The maximum number of elements permitted in an array by the <a href="../utilities/bc.html"><i>bc
utility.

<td align="left">
<p class="tent">2048

<tr valign="top">
<td align="left">
<p class="tent">{POSIX2&#95;BC&#95;SCALE&#95;MAX}

<td align="left">
<p class="tent">The maximum <i>scale value allowed by the <a href="../utilities/bc.html"><i>bc utility.

<td align="left">
<p class="tent">99

<tr valign="top">
<td align="left">
<p class="tent">{POSIX2&#95;BC&#95;STRING&#95;MAX}

<td align="left">
<p class="tent">The maximum length of a string constant accepted by the <a href="../utilities/bc.html"><i>bc utility.

<td align="left">
<p class="tent">1000

<tr valign="top">
<td align="left">
<p class="tent">{POSIX2&#95;COLL&#95;WEIGHTS&#95;MAX}

<td align="left">
<p class="tent">The maximum number of weights that can be assigned to an entry of the <i>LC&#95;COLLATE <b>order keyword in the
locale definition file; see the <b>border&#95;start keyword in XBD <a href="../basedefs/V1_chap07.html#tag_07_03_02"><i>7.3.2
LC&#95;COLLATE.

<td align="left">
<p class="tent">2

<tr valign="top">
<td align="left">
<p class="tent">{POSIX2&#95;EXPR&#95;NEST&#95;MAX}

<td align="left">
<p class="tent">The maximum number of expressions that can be nested within parentheses by the <a href=
"../utilities/expr.html"><i>expr utility.

<td align="left">
<p class="tent">32

<tr valign="top">
<td align="left">
<p class="tent">{POSIX2&#95;LINE&#95;MAX}

<td align="left">
<p class="tent">Unless otherwise noted, the maximum length, in bytes, of the input line of a utility (either standard input or
another file), when the utility is described as processing text files. The length includes room for the trailing
&lt;newline&gt;.

<td align="left">
<p class="tent">2048

<tr valign="top">
<td align="left">
<p class="tent">{POSIX&#95;RE&#95;DUP&#95;MAX}

<td align="left">
<p class="tent">Maximum number of repeated occurrences of a BRE or ERE interval expression; see XBD <a href=
"../basedefs/V1_chap09.html#tag_09_03_06"><i>9.3.6 BREs Matching Multiple Characters and <a href=
"../basedefs/V1_chap09.html#tag_09_04_06"><i>9.4.6 EREs Matching Multiple Characters.

<td align="left">
<p class="tent">255

<p class="tent">The values specified in <a href="#tagtcjh_11">Utility Limit Minimum Values represent the lowest values
conforming implementations shall provide and, consequently, the largest values on which an application can rely without further
enquiries, as described below. These values shall be accessible to applications via the <a href=
"../utilities/getconf.html"><i>getconf utility (see <a href="../utilities/getconf.html#"><i>getconf).
<p class="tent">Implementations may provide more liberal, or less restrictive, values than shown in <a href="#tagtcjh_11">Utility
Limit Minimum Values. These possibly more liberal values are accessible using the symbols in <a href="#tagtcjh_12">Symbolic
Utility Limits.
<p class="tent">The <a href="../functions/sysconf.html"><i>sysconf() function defined in the System Interfaces volume of
POSIX.1-2024 or the <a href="../utilities/getconf.html"><i>getconf utility return the value of each symbol on each specific
implementation. The value so retrieved is the largest, or most liberal, value that is available throughout the session lifetime, as
determined at session creation. The literal names shown in the table apply only to the <a href=
"../utilities/getconf.html"><i>getconf utility; the high-level language binding describes the exact form of each name to be
used by the interfaces in that binding.
<p class="tent">All numeric limits defined by the System Interfaces volume of POSIX.1-2024, such as {PATH&#95;MAX}, shall also apply to
this volume of POSIX.1-2024. All the utilities defined by this volume of POSIX.1-2024 are implicitly limited by these values,
unless otherwise noted in the utility descriptions.
<p class="tent">It is not guaranteed that the application can actually reach the specified limit of an implementation in any given
case, or at all, as a lack of virtual memory or other resources may prevent this. The limit value indicates only that the
implementation does not specifically impose any arbitrary, more restrictive limit.<br>
<p class="caption"><a name="tagtcjh_12" id="tagtcjh_12"> Table: Symbolic Utility Limits
<center>
<table border="1" cellpadding="3" align="center">
<tr valign="top">
<th align="center">
<p class="tent"><b>Name

<th align="center">
<p class="tent"><b>Description

<th align="center">
<p class="tent"><b>Minimum Value

<tr valign="top">
<td align="left">
<p class="tent">{BC&#95;BASE&#95;MAX}

<td align="left">
<p class="tent">The maximum <i>obase value allowed by the <a href="../utilities/bc.html"><i>bc utility.

<td align="left">
<p class="tent">{POSIX2&#95;BC&#95;BASE&#95;MAX}

<tr valign="top">
<td align="left">
<p class="tent">{BC&#95;DIM&#95;MAX}

<td align="left">
<p class="tent">The maximum number of elements permitted in an array by the <a href="../utilities/bc.html"><i>bc
utility.

<td align="left">
<p class="tent">{POSIX2&#95;BC&#95;DIM&#95;MAX}

<tr valign="top">
<td align="left">
<p class="tent">{BC&#95;SCALE&#95;MAX}

<td align="left">
<p class="tent">The maximum <i>scale value allowed by the <a href="../utilities/bc.html"><i>bc utility.

<td align="left">
<p class="tent">{POSIX2&#95;BC&#95;SCALE&#95;MAX}

<tr valign="top">
<td align="left">
<p class="tent">{BC&#95;STRING&#95;MAX}

<td align="left">
<p class="tent">The maximum length of a string constant accepted by the <a href="../utilities/bc.html"><i>bc utility.

<td align="left">
<p class="tent">{POSIX2&#95;BC&#95;STRING&#95;MAX}

<tr valign="top">
<td align="left">
<p class="tent">{COLL&#95;WEIGHTS&#95;MAX}

<td align="left">
<p class="tent">The maximum number of weights that can be assigned to an entry of the <i>LC&#95;COLLATE <b>order keyword in the
locale definition file; see the <b>order&#95;start keyword in XBD <a href="../basedefs/V1_chap07.html#tag_07_03_02"><i>7.3.2
LC&#95;COLLATE.

<td align="left">
<p class="tent">{POSIX2&#95;COLL&#95;WEIGHTS&#95;MAX}

<tr valign="top">
<td align="left">
<p class="tent">{EXPR&#95;NEST&#95;MAX}

<td align="left">
<p class="tent">The maximum number of expressions that can be nested within parentheses by the <a href=
"../utilities/expr.html"><i>expr utility.

<td align="left">
<p class="tent">{POSIX2&#95;EXPR&#95;NEST&#95;MAX}

<tr valign="top">
<td align="left">
<p class="tent">{LINE&#95;MAX}

<td align="left">
<p class="tent">Unless otherwise noted, the maximum length, in bytes, of the input line of a utility (either standard input or
another file), when the utility is described as processing text files. The length includes room for the trailing
&lt;newline&gt;.

<td align="left">
<p class="tent">{POSIX2&#95;LINE&#95;MAX}

<tr valign="top">
<td align="left">
<p class="tent">{RE&#95;DUP&#95;MAX}

<td align="left">
<p class="tent">Maximum number of repeated occurrences of a BRE or ERE interval expression; see XBD <a href=
"../basedefs/V1_chap09.html#tag_09_03_06"><i>9.3.6 BREs Matching Multiple Characters and <a href=
"../basedefs/V1_chap09.html#tag_09_04_06"><i>9.4.6 EREs Matching Multiple Characters.

<td align="left">
<p class="tent">{POSIX&#95;RE&#95;DUP&#95;MAX}

<p class="tent">The following value may be a constant within an implementation or may vary from one pathname to another.
<dl compact>
<dd>
<dt>{POSIX2&#95;SYMLINKS}
<dd><br>
When referring to a directory, the system supports the creation of symbolic links within that directory; for non-directory files,
the meaning of {POSIX2&#95;SYMLINKS} is undefined.

<h3><a name="tag_18_03" id="tag_18_03">1.3 Grammar Conventions
<p class="tent">Portions of this volume of POSIX.1-2024 are expressed in terms of a special grammar notation. It is used to portray
the complex syntax of certain program input. The grammar is based on the syntax used by the <a href=
"../utilities/yacc.html"><i>yacc utility. However, it does not represent fully functional <a href=
"../utilities/yacc.html"><i>yacc input, suitable for program use; the lexical processing and all semantic requirements are
described only in textual form. The grammar is not based on source used in any traditional implementation and has not been tested
with the semantic code that would normally be required to accompany it. Furthermore, there is no implication that the partial
<a href="../utilities/yacc.html"><i>yacc code presented represents the most efficient, or only, means of supporting the
complex syntax within the utility. Implementations may use other programming languages or algorithms, as long as the syntax
supported is the same as that represented by the grammar.
<p class="tent">The following typographical conventions are used in the grammar; they have no significance except to aid in
reading.
<ul>
<li class="tent">The identifiers for the reserved words of the language are shown with a leading capital letter. (These are
terminals in the grammar; for example, <b>While, <b>Case.)
<li class="tent">The identifiers for terminals in the grammar are all named with uppercase letters and underscores; for example,
<b>NEWLINE, <b>ASSIGN&#95;OP, <b>NAME.
<li class="tent">The identifiers for non-terminals are all lowercase.

<h3><a name="tag_18_04" id="tag_18_04">1.4 Utility Description Defaults
<p class="tent">This section describes all of the subsections used within the utility descriptions, including:
<ul>
<li class="tent">Intended usage of the section
<li class="tent">Global defaults that affect all the standard utilities
<li class="tent">The meanings of notations used in this volume of POSIX.1-2024 that are specific to individual utility
sections

<dl compact>
<dd>
<dt><b>NAME
<dd><br>
This section gives the name or names of the utility and briefly states its purpose.
<dt><b>SYNOPSIS
<dd><br>
The SYNOPSIS section summarizes the syntax of the calling sequence for the utility, including options, option-arguments, and
operands. Standards for utility naming are described in XBD <a href="../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax
Guidelines; for describing the utility&#39;s arguments in XBD <a href="../basedefs/V1_chap12.html#tag_12_01"><i>12.1 Utility
Argument Syntax.
<dt><b>DESCRIPTION
<dd><br>
The DESCRIPTION section describes the actions of the utility. If the utility has a very complex set of subcommands or its own
procedural language, an EXTENDED DESCRIPTION section is also provided. Most explanations of optional functionality are omitted
here, as they are usually explained in the OPTIONS section.
<p class="tent">As stated in <a href="#tag_18_01_01_11">1.1.1.11 Actions Equivalent to Functions, some functions are described
in terms of equivalent functionality. When specific functions are cited, the implementation shall provide equivalent functionality
including side-effects associated with successful execution of the function. The treatment of errors and intermediate results from
the individual functions cited is generally not specified by this volume of POSIX.1-2024. See the utility&#39;s EXIT STATUS and
CONSEQUENCES OF ERRORS sections for all actions associated with errors encountered by the utility.
<p class="tent">A standard utility shall not be treated as a declaration utility unless explicitly stated in this section.

<dt><b>OPTIONS
<dd><br>
The OPTIONS section describes the utility options and option-arguments, and how they modify the actions of the utility. Standard
utilities that have options either fully comply with XBD <a href="../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax
Guidelines or describe all deviations. Apparent disagreements between functionality descriptions in the OPTIONS and
DESCRIPTION (or EXTENDED DESCRIPTION) sections are always resolved in favor of the OPTIONS section.
<p class="tent">Each OPTIONS section that uses the phrase &#34;The &#46;&#46;&#46; utility shall conform to the Utility Syntax Guidelines &#46;&#46;&#46;&#34;
refers only to the use of the utility as specified by this volume of POSIX.1-2024; implementation extensions should also conform to
the guidelines, but may allow exceptions for historical practice.
<p class="tent">Unless otherwise stated in the utility description, when given an option unrecognized by the implementation, or
when a required option-argument is not provided, standard utilities shall issue a diagnostic message to standard error and exit
with an exit status that indicates an error occurred.
<p class="tent">All utilities in this volume of POSIX.1-2024 shall be capable of processing arguments using eight-bit
transparency.
<p class="tent"><b>Default Behavior: When this section is listed as &#34;None.&#34;, it means that the implementation need not
support any options. Standard utilities that do not accept options, but that do accept operands, shall recognize <tt>&#34;&#45;&#45;&#34; as a
first argument to be discarded.
<p class="tent">The requirement for recognizing <tt>&#34;&#45;&#45;&#34; is because conforming applications need a way to shield their
operands from any arbitrary options that the implementation may provide as an extension. For example, if the standard utility
<i>foo is listed as taking no options, and the application needed to give it a pathname with a leading &lt;hyphen-minus&gt;, it
could safely do it as:
<pre>
<tt>foo &#45;&#45; -myfile

<p class="tent">and avoid any problems with <b>-m used as an extension.

<dt><b>OPERANDS
<dd><br>
The OPERANDS section describes the utility operands, and how they affect the actions of the utility. Apparent disagreements between
functionality descriptions in the OPERANDS and DESCRIPTION (or EXTENDED DESCRIPTION) sections shall be resolved in favor of the
OPERANDS section.
<p class="tent">If an operand naming a file can be specified as <tt>&#39;-&#39;, which means to use the standard input instead of a
named file, this is explicitly stated in this section. Unless otherwise stated, the use of multiple instances of <tt>&#39;-&#39; to
mean standard input in a single command produces unspecified results.
<p class="tent">Unless otherwise stated, the standard utilities that accept operands shall process those operands in the order
specified in the command line.
<p class="tent"><b>Default Behavior: When this section is listed as &#34;None.&#34;, it means that the implementation need not
support any operands.

<dt><b>STDIN
<dd><br>
The STDIN section describes the standard input of the utility. This section is frequently merely a reference to the following
section, as many utilities treat standard input and input files in the same manner. Unless otherwise stated, all restrictions
described in the INPUT FILES section shall apply to this section as well.
<p class="tent">Use of a terminal for standard input can cause any of the standard utilities that read standard input to stop when
used in the background. For this reason, applications should not use interactive features in scripts to be placed in the
background.
<p class="tent">The specified standard input format of the standard utilities shall not depend on the existence or value of the
environment variables defined in this volume of POSIX.1-2024, except as provided by this volume of POSIX.1-2024.
<p class="tent"><b>Default Behavior: When this section is listed as &#34;Not used.&#34;, it means that the standard input shall not
be read when the utility is used as described by this volume of POSIX.1-2024.

<dt><b>INPUT FILES
<dd><br>
The INPUT FILES section describes the files, other than the standard input, used as input by the utility. It includes files named
as operands and option-arguments as well as other files that are referred to, such as start-up and initialization files, databases,
and so on. Commonly-used files are generally described in one place and cross-referenced by other utilities.
<p class="tent">All utilities in this volume of POSIX.1-2024 shall be capable of processing input files using eight-bit
transparency.
<p class="tent">When a standard utility reads a seekable input file and terminates without an error before it reaches end-of-file,
the utility shall ensure that the file offset in the open file description is properly positioned just past the last byte processed
by the utility. For files that are not seekable, the state of the file offset in the open file description for that file is
unspecified. A conforming application shall not assume that the following three commands are equivalent:
<pre>
<tt>tail -n +2 file
(sed -n 1q; cat) &lt; file
cat file | (sed -n 1q; cat)

<p class="tent">The second command is equivalent to the first only when the file is seekable. The third command leaves the file
offset in the open file description in an unspecified state. Other utilities, such as <a href=
"../utilities/head.html"><i>head, <a href="../utilities/read.html"><i>read, and <a href=
"../utilities/sh.html"><i>sh, have similar properties.
<p class="tent">Some of the standard utilities, such as filters, process input files a line or a block at a time and have no
restrictions on the maximum input file size. Some utilities may have size limitations that are not as obvious as file space or
memory limitations. Such limitations should reflect resource limitations of some sort, not arbitrary limits set by implementors.
Implementations shall document those utilities that are limited by constraints other than file system space, available memory, and
other limits specifically cited by this volume of POSIX.1-2024, and identify what the constraint is and indicate a way of
estimating when the constraint would be reached. Similarly, some utilities descend the directory tree (recursively).
Implementations shall also document any limits that they may have in descending the directory tree that are beyond limits cited by
this volume of POSIX.1-2024.
<p class="tent">When an input file is described as a &#34;text file&#34;, the utility produces undefined results if given input that is
not from a text file, unless otherwise stated. Some utilities (for example, <a href="../utilities/make.html"><i>make,
<a href="../utilities/read.html"><i>read, <a href="../utilities/sh.html"><i>sh) allow for continued input lines
using an escaped &lt;newline&gt; convention; unless otherwise stated, the utility need not be able to accumulate more than
{LINE&#95;MAX} bytes from a set of multiple, continued input lines. Thus, for a conforming application the total of all the continued
lines in a set cannot exceed {LINE&#95;MAX}. If a utility using the escaped &lt;newline&gt; convention detects an end-of-file condition
immediately after an escaped &lt;newline&gt;, the results are unspecified.
<p class="tent">Record formats are described in a notation similar to that used by the C-language function, <a href=
"../functions/printf.html"><i>printf(). See XBD <a href="../basedefs/V1_chap05.html#tag_05"><i>5. File Format
Notation for a description of this notation. The format description is intended to be sufficiently rigorous to allow other
applications to generate these input files. However, since &lt;blank&gt;s can legitimately be included in some of the fields
described by the standard utilities, particularly in locales other than the POSIX locale, this intent is not always realized.
<p class="tent"><b>Default Behavior: When this section is listed as &#34;None.&#34;, it means that no input files are required to be
supplied when the utility is used as described by this volume of POSIX.1-2024.

<dt><b>ENVIRONMENT VARIABLES
<dd><br>
The ENVIRONMENT VARIABLES section lists what variables affect the utility&#39;s execution.
<p class="tent">The entire manner in which environment variables described in this volume of POSIX.1-2024 affect the behavior of
each utility is described in the ENVIRONMENT VARIABLES section for that utility, in conjunction with the global effects of the
<i>LANG , <i>LC&#95;ALL , and <sup>&#91;<a href="javascript:open_code('XSI')">XSI&#93; <img src=".pic/opt-start.gif"
alt="[Option Start]" border="0"> <i>NLSPATH <img src=".pic/opt-end.gif" alt="[Option End]" border="0"> environment
variables described in XBD <a href="../basedefs/V1_chap08.html#tag_08"><i>8. Environment Variables. The existence or value
of environment variables described in this volume of POSIX.1-2024 shall not otherwise affect the specified behavior of the standard
utilities. Any effects of the existence or value of environment variables not described by this volume of POSIX.1-2024 upon the
standard utilities are unspecified.
<p class="tent">For those standard utilities that use environment variables as a means for selecting a utility to execute (such as
<i>CC in <a href="../utilities/make.html"><i>make), the string provided to the utility is subjected to the path search
described for <i>PATH in XBD <a href="../basedefs/V1_chap08.html#tag_08"><i>8. Environment Variables.
<p class="tent">All utilities in this volume of POSIX.1-2024 shall be capable of processing environment variable names and values
using eight-bit transparency.
<p class="tent"><b>Default Behavior: When this section is listed as &#34;None.&#34;, it means that the behavior of the utility is not
directly affected by environment variables described by this volume of POSIX.1-2024 when the utility is used as described by this
volume of POSIX.1-2024.

<dt><b>ASYNCHRONOUS EVENTS
<dd><br>
The ASYNCHRONOUS EVENTS section lists how the utility reacts to such events as signals and what signals are caught.
<p class="tent"><b>Default Behavior: When this section is listed as &#34;Default.&#34;, or it refers to &#34;the standard action&#34; for
any signal, it means that the action taken as a result of the signal shall be as follows:
<ul>
<li class="tent">If the action inherited from the invoking process, according to the rules of inheritance of signal actions defined
in the System Interfaces volume of POSIX.1-2024, is for the signal to be ignored, the utility shall ignore the signal.
<li class="tent">If the action inherited from the invoking process, according to the rules of inheritance of signal actions defined
in System Interfaces volume of POSIX.1-2024, is the default signal action, the result of the utility&#39;s execution shall be as if the
default signal action had been taken.

<p class="tent">When the required action is for the signal to terminate the utility, the utility may catch the signal, perform some
additional processing (such as deleting temporary files), restore the default signal action, and resignal itself.

<dt><b>STDOUT
<dd><br>
The STDOUT section completely describes the standard output of the utility. This section is frequently merely a reference to the
following section, OUTPUT FILES, because many utilities treat standard output and output files in the same manner.
<p class="tent">Use of a terminal for standard output may cause any of the standard utilities that write standard output to stop
when used in the background. For this reason, applications should not use interactive features in scripts to be placed in the
background.
<p class="tent">Record formats are described in a notation similar to that used by the C-language function, <a href=
"../functions/printf.html"><i>printf(). See XBD <a href="../basedefs/V1_chap05.html#tag_05"><i>5. File Format
Notation for a description of this notation.
<p class="tent">The specified standard output of the standard utilities shall not depend on the existence or value of the
environment variables defined in this volume of POSIX.1-2024, except as provided by this volume of POSIX.1-2024.
<p class="tent">Some of the standard utilities describe their output using the verb <i>display, defined in XBD <a href=
"../basedefs/V1_chap03.html#tag_03_107"><i>3.107 Display. Output described in the STDOUT sections of such utilities may be
produced using means other than standard output. When standard output is directed to a terminal, the output described shall be
written directly to the terminal. Otherwise, the results are undefined.
<p class="tent"><b>Default Behavior: When this section is listed as &#34;Not used.&#34;, it means that the standard output shall not
be written when the utility is used as described by this volume of POSIX.1-2024.

<dt><b>STDERR
<dd><br>
The STDERR section describes the standard error output of the utility. Only those messages that are purposely sent by the utility
are described.
<p class="tent">Use of a terminal for standard error may cause any of the standard utilities that write standard error output to
stop when used in the background. For this reason, applications should not use interactive features in scripts to be placed in the
background.
<p class="tent">The format of diagnostic messages for most utilities is unspecified, but the language and cultural conventions of
diagnostic and informative messages whose format is unspecified by this volume of POSIX.1-2024 should be affected by the setting of
<i>LC&#95;MESSAGES and <sup>&#91;<a href="javascript:open_code('XSI')">XSI&#93; <img src=".pic/opt-start.gif" alt=
"[Option Start]" border="0"> <i>NLSPATH . <img src=".pic/opt-end.gif" alt="[Option End]" border="0">
<p class="tent">The specified standard error output of standard utilities shall not depend on the existence or value of the
environment variables defined in this volume of POSIX.1-2024, except as provided by this volume of POSIX.1-2024.
<p class="tent"><b>Default Behavior: When this section is listed as &#34;The standard error shall be used only for diagnostic
messages.&#34;, it means that, unless otherwise stated, the diagnostic messages shall be sent to the standard error only when the exit
status indicates that an error occurred and the utility is used as described by this volume of POSIX.1-2024.
<p class="tent">When this section is listed as &#34;Not used.&#34;, it means that the standard error shall not be used when the utility
is used as described in this volume of POSIX.1-2024.

<dt><b>OUTPUT FILES
<dd><br>
The OUTPUT FILES section completely describes the files created or modified by the utility. Temporary or system files that are
created for internal usage by this utility or other parts of the implementation (for example, spool, log, and audit files) are not
described in this, or any, section. The utilities creating such files and the names of such files are unspecified. If applications
are written to use temporary or intermediate files, they should use the <i>TMPDIR environment variable, if it is set and
represents an accessible directory, to select the location of temporary files.
<p class="tent">Implementations shall ensure that temporary files, when used by the standard utilities, are named so that different
utilities or multiple instances of the same utility can operate simultaneously without regard to their working directories, or any
other process characteristic other than process ID. There are two exceptions to this rule:
<ol>
<li class="tent">Resources for temporary files other than the name space (for example, disk space, available directory entries, or
number of processes allowed) are not guaranteed.
<li class="tent">Certain standard utilities generate output files that are intended as input for other utilities (for example,
<a href="../utilities/lex.html"><i>lex generates <b>lex.yy.c), and these cannot have unique names. These cases are
explicitly identified in the descriptions of the respective utilities.

<p class="tent">Any temporary file created by the implementation shall be removed by the implementation upon a utility&#39;s successful
exit, exit because of errors, or before termination by any of the SIGHUP, SIGINT, or SIGTERM signals, unless specified otherwise by
the utility description.
<p class="tent">Receipt of the SIGQUIT signal should generally cause termination (unless in some debugging mode) that would bypass
any attempted recovery actions.
<p class="tent">Record formats are described in a notation similar to that used by the C-language function, <a href=
"../functions/printf.html"><i>printf(); see XBD <a href="../basedefs/V1_chap05.html#tag_05"><i>5. File Format
Notation for a description of this notation.
<p class="tent"><b>Default Behavior: When this section is listed as &#34;None.&#34;, it means that no files are created or modified
as a consequence of direct action on the part of the utility when the utility is used as described by this volume of POSIX.1-2024.
However, the utility may create or modify system files, such as log files, that are outside the utility&#39;s normal execution
environment.

<dt><b>EXTENDED DESCRIPTION
<dd><br>
The EXTENDED DESCRIPTION section provides a place for describing the actions of very complicated utilities, such as text editors or
language processors, which typically have elaborate command languages.
<p class="tent"><b>Default Behavior: When this section is listed as &#34;None.&#34;, no further description is necessary.

<dt><b>EXIT STATUS
<dd><br>
The EXIT STATUS section describes the values the utility shall return to the calling program, or shell, and the conditions that
cause these values to be returned. Usually, utilities return zero for successful completion and values greater than zero for
various error conditions. If specific numeric values are listed in this section, the system shall use those values for the errors
described. In some cases, status values are listed more loosely, such as &gt;0. A strictly conforming application shall not rely on
any specific value in the range shown and shall be prepared to receive any value in the range.
<p class="tent">For example, a utility may list zero as a successful return, 1 as a failure for a specific reason, and &gt;1 as
&#34;an error occurred&#34;. In this case, unspecified conditions may cause a 2 or 3, or other value, to be returned. A conforming
application should be written so that it tests for successful exit status values (zero in this case), rather than relying upon the
single specific error value listed in this volume of POSIX.1-2024. In that way, it has maximum portability, even on implementations
with extensions.
<p class="tent">Unspecified error conditions may be represented by specific values not listed in this volume of POSIX.1-2024.
<p class="tent"><b>Default Behavior: When the description of exit status 0 is &#34;Successful completion&#34;, it means that exit
status 0 shall indicate that all of the actions the utility is required to perform were completed successfully.

<dt><b>CONSEQUENCES OF ERRORS
<dd><br>
The CONSEQUENCES OF ERRORS section describes the effects on the environment, file systems, process state, and so on, when error
conditions occur. It does not describe error messages produced or exit status values used.
<p class="tent">The many reasons for failure of a utility are generally not specified by the utility descriptions. Utilities may
terminate prematurely if they encounter: invalid usage of options, arguments, or environment variables; invalid usage of the
complex syntaxes expressed in EXTENDED DESCRIPTION sections; resource exhaustion; difficulties accessing, creating, reading, or
writing files; or difficulties associated with the privileges of the process.
<p class="tent">The following shall apply to each utility, unless otherwise stated:
<ul>
<li class="tent">If the requested action cannot be performed on an operand representing a file, directory, user, process, and so
on, the utility shall issue a diagnostic message to standard error and continue processing the next operand in sequence, but the
final exit status shall be one that indicates an error occurred.
<p class="tent">For a utility that recursively traverses a file hierarchy (such as <a href="../utilities/find.html"><i>find
or <a href="../utilities/chown.html"><i>chown <b>-R), if the requested action cannot be performed on a file or
directory encountered in the hierarchy, the utility shall issue a diagnostic message to standard error and continue processing the
remaining files in the hierarchy, but the final exit status shall be one that indicates an error occurred. <basefont size="2">
<dl>
<dt><b>Note:
<dd>If the requested action is to write one or more pathnames in a format that has &lt;newline&gt; as a terminator or separator,
and a pathname to be written contains any bytes that have the encoded value of a &lt;newline&gt; character, this should be treated
as an action that cannot be performed. A future version of this standard may require that utilities treat this as an error.

<basefont size="3">
<li class="tent">If the requested action characterized by an option or option-argument cannot be performed, the utility shall issue
a diagnostic message to standard error and the exit status returned shall be one that indicates an error occurred.
<li class="tent">When an unrecoverable error condition is encountered, the utility shall exit with an exit status that indicates an
error occurred.
<li class="tent">A diagnostic message shall be written to standard error whenever an error condition occurs.

<p class="tent">When a utility encounters an error condition several actions are possible, depending on the severity of the error
and the state of the utility. Included in the possible actions of various utilities are: deletion of temporary or intermediate work
files; deletion of incomplete files; validity checking of the file system or directory.
<p class="tent"><b>Default Behavior: When this section is listed as &#34;Default.&#34;, it means that any changes to the environment,
file systems, process state, and so on are unspecified.

<dt><b>APPLICATION USAGE
<dd><br>
This section is informative.
<p class="tent">The APPLICATION USAGE section gives advice to the application programmer or user about the way the utility should
be used.

<dt><b>EXAMPLES
<dd><br>
This section is informative.
<p class="tent">The EXAMPLES section gives one or more examples of usage, where appropriate. In the event of conflict between an
example and a normative part of the specification, the normative material is to be taken as correct.
<p class="tent">In all examples, quoting has been used, showing how sample commands (utility names combined with arguments) could
be passed correctly to a shell (see <a href="../utilities/sh.html"><i>sh) or as a string to the <a href=
"../functions/system.html"><i>system() function defined in the System Interfaces volume of POSIX.1-2024. Such quoting would
not be used if the utility is invoked using one of the <i>exec functions defined in the System Interfaces volume of
POSIX.1-2024.

<dt><b>RATIONALE
<dd><br>
This section is informative.
<p class="tent">This section contains historical information concerning the contents of this volume of POSIX.1-2024 and why
features were included or discarded by the standard developers.

<dt><b>FUTURE DIRECTIONS
<dd><br>
This section is informative.
<p class="tent">The FUTURE DIRECTIONS section should be used as a guide to current thinking; there is not necessarily a commitment
to implement all of these future directions in their entirety.

<dt><b>SEE ALSO
<dd><br>
This section is informative.
<p class="tent">The SEE ALSO section lists related entries.

<dt><b>CHANGE HISTORY
<dd><br>
This section is informative.
<p class="tent">This section shows the derivation of the entry and any significant changes that have been made to it.

<p class="tent">Certain of the standard utilities describe how they can invoke other utilities or applications, such as by passing
a command string to the command interpreter. The external influences (STDIN, ENVIRONMENT VARIABLES, and so on) and external effects
(STDOUT, CONSEQUENCES OF ERRORS, and so on) of such invoked utilities are not described in the section concerning the standard
utility that invokes them.
<h3><a name="tag_18_05" id="tag_18_05">1.5 Considerations for Utilities in Support of Files of Arbitrary Size
<p class="tent">The following utilities support files of any size up to the maximum that can be created by the implementation. This
support includes correct writing of file size-related values (such as file sizes and offsets, line numbers, and block counts) and
correct interpretation of command line arguments that contain such values.
<dl compact>
<dd>
<dt><i>basename
<dd>Return non-directory portion of pathname.
<dt><i>cat
<dd>Concatenate and print files.
<dt><i>cd
<dd>Change working directory.
<dt><i>chgrp
<dd>Change file group ownership.
<dt><i>chmod
<dd>Change file modes.
<dt><i>chown
<dd>Change file ownership.
<dt><i>cksum
<dd>Write file checksums and sizes.
<dt><i>cmp
<dd>Compare two files.
<dt><i>cp
<dd>Copy files.
<dt><i>dd
<dd>Convert and copy a file.
<dt><i>df
<dd>Report free disk space.
<dt><i>dirname
<dd>Return directory portion of pathname.
<dt><i>du
<dd>Estimate file space usage.
<dt><i>find
<dd>Find files.
<dt><i>ln
<dd>Link files.
<dt><i>ls
<dd>List directory contents.
<dt><i>mkdir
<dd>Make directories.
<dt><i>mv
<dd>Move files.
<dt><i>pathchk
<dd>Check pathnames.
<dt><i>pwd
<dd>Return working directory name.
<dt><i>rm
<dd>Remove directory entries.
<dt><i>rmdir
<dd>Remove directories.
<dt><i>sh
<dd>Shell, the standard command language interpreter.
<dt><i>test
<dd>Evaluate expression.
<dt><i>touch
<dd>Change file access and modification times.
<dt><i>ulimit
<dd>Set or report file size limit.

<br>
<p class="tent">Exceptions to the requirement that utilities support files of any size up to the maximum are as follows:
<ol>
<li class="tent">Uses of files as command scripts, or for configuration or control, are exempt. For example, it is not required
that <a href="../utilities/sh.html"><i>sh be able to read an arbitrarily large <b>.profile.
<li class="tent">Shell input and output redirection are exempt. For example, it is not required that the redirections <i>sum
&lt; <i>file or <i>echo foo &gt; <i>file succeed for an arbitrarily large existing file.

<h3><a name="tag_18_06" id="tag_18_06">1.6 Built-In Utilities
<p class="tent">Any of the standard utilities may be implemented as regular built-in utilities within the command language
interpreter. This is usually done to increase the performance of frequently used utilities or to achieve functionality that would
be more difficult in a separate environment. The intrinsic utilities described in <a href="#tag_18_07">1.7 Intrinsic Utilities
below are frequently provided as regular built-ins.
<p class="tent">However, all of the standard utilities other than:
<ul>
<li class="tent">The special built-ins described in <a href="../utilities/V3_chap02.html#tag_19_15"><i>2.15 Special Built-In
Utilities
<li class="tent">The intrinsic utilities named in <a href="#tagtcjh_13">Intrinsic Utilities, except for <a href=
"../utilities/kill.html"><i>kill

<p class="tent">shall be implemented, regardless of whether they are also implemented as regular built-ins, in a manner so that
they can be accessed via the <i>exec family of functions as defined in the System Interfaces volume of POSIX.1-2024 and can be
invoked directly by those standard utilities that require it (<a href="../utilities/env.html"><i>env, <a href=
"../utilities/find.html"><i>find, <a href="../utilities/nice.html"><i>nice, <a href=
"../utilities/nohup.html"><i>nohup, <a href="../utilities/time.html"><i>time, <a href=
"../utilities/xargs.html"><i>xargs).
<h3><a name="tag_18_07" id="tag_18_07">1.7 Intrinsic Utilities
<p class="tent">As described in <a href="../utilities/V3_chap02.html#tag_19_09_01_04"><i>2.9.1.4 Command Search and
Execution, intrinsic utilities are not subject to a <i>PATH search during command search and execution. The utilities
named in <a href="#tagtcjh_13">Intrinsic Utilities shall be intrinsic utilities.<br>
<p class="caption"><a name="tagtcjh_13" id="tagtcjh_13"> Table: Intrinsic Utilities
<center>
<table cellpadding="3" align="center">
<tr valign="top">
<td align="left">
<p class="tent"><br>
<a href="../utilities/alias.html"><i>alias<br>
<a href="../utilities/bg.html"><i>bg<br>
<a href="../utilities/cd.html"><i>cd<br>
 

<td align="left">
<p class="tent"><br>
<a href="../utilities/command.html"><i>command<br>
<a href="../utilities/fc.html"><i>fc<br>
<a href="../utilities/fg.html"><i>fg<br>
 

<td align="left">
<p class="tent"><br>
<a href="../utilities/getopts.html"><i>getopts<br>
<a href="../utilities/hash.html"><i>hash<br>
<a href="../utilities/jobs.html"><i>jobs<br>
 

<td align="left">
<p class="tent"><br>
<a href="../utilities/kill.html"><i>kill<br>
<a href="../utilities/read.html"><i>read<br>
<a href="../utilities/type.html"><i>type<br>
 

<td align="left">
<p class="tent"><br>
<a href="../utilities/ulimit.html"><i>ulimit<br>
<a href="../utilities/umask.html"><i>umask<br>
<a href="../utilities/unalias.html"><i>unalias<br>
 

<td align="left">
<p class="tent"><br>
<a href="../utilities/wait.html"><i>wait<br>
 

<p class="tent">Whether any additional utility is considered an intrinsic utility is implementation-defined. Because applications
are unable to override an intrinsic utility with a utility from <i>PATH , implementations should not make any utility an
intrinsic utility beyond the utilities in <a href="#tagtcjh_13">Intrinsic Utilities.

