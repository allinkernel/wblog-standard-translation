<!-- 英文原文镜像：https://pubs.opengroup.org/onlinepubs/9799919799/utilities/sed.html -->
<body bgcolor="white">

<a name="top" id="top"> <a name="sed" id="sed"> <a name="tag_20_109" id="tag_20_109"><!-- sed -->
<h4 class="mansect"><a name="tag_20_109_01" id="tag_20_109_01">NAME
<blockquote>sed — stream editor
<h4 class="mansect"><a name="tag_20_109_02" id="tag_20_109_02">SYNOPSIS
<blockquote class="synopsis">
<p><code><tt>sed <b>&#91;<tt>-En<b>&#93; <i>script <b>&#91;<i>file<tt>&#46;&#46;&#46;<b>&#93; <tt><br>
<br>
sed <b>&#91;<tt>-En<b>&#93; <tt>-e <i>script <b>&#91;<tt>-e <i>script<b>&#93;<tt>&#46;&#46;&#46;
<b>&#91;<tt>-f <i>script&#95;file<b>&#93;<tt>&#46;&#46;&#46; <b>&#91;<i>file<tt>&#46;&#46;&#46;<b>&#93; <tt><br>
<br>
sed <b>&#91;<tt>-En<b>&#93; &#91;<tt>-e <i>script<b>&#93;<tt>&#46;&#46;&#46; -f <i>script&#95;file <b>&#91;<tt>-f
<i>script&#95;file<b>&#93;<tt>&#46;&#46;&#46; <b>&#91;<i>file<tt>&#46;&#46;&#46;<b>&#93; <tt><br>

<h4 class="mansect"><a name="tag_20_109_03" id="tag_20_109_03">DESCRIPTION
<blockquote>
<p>The <i>sed utility is a stream editor that shall read one or more text files, make editing changes according to a script of
editing commands, and write the results to standard output. The script shall be obtained from either the <i>script operand
string or a combination of the option-arguments from the <b>-e <i>script and <b>-f <i>script&#95;file options.

<h4 class="mansect"><a name="tag_20_109_04" id="tag_20_109_04">OPTIONS
<blockquote>
<p>The <i>sed utility shall conform to XBD <a href="../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax
Guidelines, except that the order of presentation of the <b>-e and <b>-f options is significant.
<p>The following options shall be supported:
<dl compact>
<dd>
<dt><b>-E
<dd>Match using extended regular expressions. Treat each pattern specified as an ERE, as described in XBD <a href=
"../basedefs/V1_chap09.html#tag_09_04"><i>9.4 Extended Regular Expressions.
<dt><b>-e <i>script
<dd>Add the editing commands specified by the <i>script option-argument to the end of the script of editing commands.
<dt><b>-f <i>script&#95;file
<dd>Add the editing commands in the file <i>script&#95;file to the end of the script of editing commands.
<dt><b>-n
<dd>Suppress the default output (in which each line, after it is examined for editing, is written to standard output). Only lines
explicitly selected for output are written.

<p>If any <b>-e or <b>-f options are specified, the script of editing commands shall initially be empty. The commands
specified by each <b>-e or <b>-f option shall be added to the script in the order specified. When each addition is made, if
the previous addition (if any) was from a <b>-e option, a &lt;newline&gt; shall be inserted before the new addition. The
resulting script shall have the same properties as the <i>script operand, described in the OPERANDS section.

<h4 class="mansect"><a name="tag_20_109_05" id="tag_20_109_05">OPERANDS
<blockquote>
<p>The following operands shall be supported:
<dl compact>
<dd>
<dt><i>file
<dd>A pathname of a file whose contents are read and edited. If multiple <i>file operands are specified, the named files shall
be read in the order specified and the concatenation shall be edited. If no <i>file operands are specified, the standard input
shall be used.
<dt><i>script
<dd>A string to be used as the script of editing commands. The application shall not present a <i>script that violates the
restrictions of a text file except that the final character need not be a &lt;newline&gt;.

<h4 class="mansect"><a name="tag_20_109_06" id="tag_20_109_06">STDIN
<blockquote>
<p>The standard input shall be used if no <i>file operands are specified, and shall be used if a <i>file operand is
<tt>&#39;-&#39; and the implementation treats the <tt>&#39;-&#39; as meaning standard input. Otherwise, the standard input shall not be
used. See the INPUT FILES section.

<h4 class="mansect"><a name="tag_20_109_07" id="tag_20_109_07">INPUT FILES
<blockquote>
<p>The input files shall be text files. The <i>script&#95;files named by the <b>-f option shall consist of editing
commands.

<h4 class="mansect"><a name="tag_20_109_08" id="tag_20_109_08">ENVIRONMENT VARIABLES
<blockquote>
<p>The following environment variables shall affect the execution of <i>sed:
<dl compact>
<dd>
<dt><i>LANG
<dd>Provide a default value for the internationalization variables that are unset or null. (See XBD <a href=
"../basedefs/V1_chap08.html#tag_08_02"><i>8.2 Internationalization Variables for the precedence of internationalization
variables used to determine the values of locale categories.)
<dt><i>LC&#95;ALL
<dd>If set to a non-empty string value, override the values of all the other internationalization variables.
<dt><i>LC&#95;COLLATE
<dd><br>
Determine the locale for the behavior of ranges, equivalence classes, and multi-character collating elements within regular
expressions.
<dt><i>LC&#95;CTYPE
<dd>Determine the locale for the interpretation of sequences of bytes of text data as characters (for example, single-byte as
opposed to multi-byte characters in arguments and input files), and the behavior of character classes within regular
expressions.
<dt><i>LC&#95;MESSAGES
<dd><br>
Determine the locale that should be used to affect the format and contents of diagnostic messages written to standard error.
<dt><i>NLSPATH
<dd><sup>&#91;<a href="javascript:open_code('XSI')">XSI&#93; <img src=".pic/opt-start.gif" alt="[Option Start]" border="0">
Determine the location of messages objects and message catalogs. <img src=".pic/opt-end.gif" alt="[Option End]" border=
"0">

<h4 class="mansect"><a name="tag_20_109_09" id="tag_20_109_09">ASYNCHRONOUS EVENTS
<blockquote>
<p>Default.

<h4 class="mansect"><a name="tag_20_109_10" id="tag_20_109_10">STDOUT
<blockquote>
<p>The input files shall be written to standard output, with the editing commands specified in the script applied. If the <b>-n
option is specified, only those input lines selected by the script shall be written to standard output.

<h4 class="mansect"><a name="tag_20_109_11" id="tag_20_109_11">STDERR
<blockquote>
<p>The standard error shall be used only for diagnostic and warning messages.

<h4 class="mansect"><a name="tag_20_109_12" id="tag_20_109_12">OUTPUT FILES
<blockquote>
<p>The output files shall be text files whose formats are dependent on the editing commands given.

<h4 class="mansect"><a name="tag_20_109_13" id="tag_20_109_13">EXTENDED DESCRIPTION
<blockquote>
<p>The <i>script shall consist of editing commands of the following form:
<pre>
<b>&#91;<i>address<b>&#91;<tt>,<i>address<b>&#93;&#93;<i>function<tt>

<p>where <i>function represents a single-character command verb from the list in <a href="#tag_20_109_13_03">Editing Commands
in sed, followed by any applicable arguments.
<p>The command can be preceded by &lt;blank&gt; characters and/or &lt;semicolon&gt; characters. The function can be preceded by
&lt;blank&gt; characters. These optional characters shall have no effect.
<p>In default operation, <i>sed cyclically shall append a line of input, less its terminating &lt;newline&gt; character, into
the pattern space. Reading from input shall be skipped if a &lt;newline&gt; was in the pattern space prior to a <b>D command
ending the previous cycle. The <i>sed utility shall then apply in sequence all commands whose addresses select that pattern
space, until a command starts the next cycle or quits. If no commands explicitly started a new cycle, then at the end of the script
the pattern space shall be copied to standard output (except when <b>-n is specified) and the pattern space shall be deleted.
Whenever the pattern space is written to standard output or a named file, <i>sed shall immediately follow it with a
&lt;newline&gt;.
<p>Some of the editing commands use a hold space to save all or part of the pattern space for subsequent retrieval. The pattern and
hold spaces shall each be able to hold at least 8192 bytes.
<h5><a name="tag_20_109_13_01" id="tag_20_109_13_01">Addresses in sed
<p>An address is either a decimal number that counts input lines cumulatively across files, a <tt>&#39;&#36;&#39; character that addresses
the last line of input, or a context address. A context address has either the form <tt>&#34;/RE/&#34; or
<tt>&#34;&#92;<i>cRE<i>c&#34;, where RE is a regular expression as described in <a href="#tag_20_109_13_02">Regular Expressions in
sed, and <i>c is any character other than &lt;backslash&gt; or &lt;newline&gt;. In a <i>sed context address, the BRE
and ERE syntax shall be extended to support escaping occurrences of the &lt;slash&gt; or <i>c delimiter within the RE by means
of an escape sequence (see XBD <a href="../basedefs/V1_chap09.html#tag_09_01"><i>9.1 Regular Expression Definitions). For
the <tt>&#34;&#92;<i>cRE<i>c&#34; form, if the character designated by <i>c is not listed as a special BRE character (if the
<b>-E option is not specified) or a special ERE character (if <b>-E is specified) in XBD <a href=
"../basedefs/V1_chap09.html#tag_09_03_03"><i>9.3.3 BRE Special Characters or XBD <a href=
"../basedefs/V1_chap09.html#tag_09_04_03"><i>9.4.3 ERE Special Characters, respectively, the escape sequence
&lt;backslash&gt;<i>c shall be treated as that literal character; otherwise, it is unspecified whether the escape sequence
&lt;backslash&gt;<i>c is treated as the literal character or the special character. In either case, the escape sequence
&lt;backslash&gt;<i>c shall not terminate the RE. For example, in the context address <tt>&#34;/abc&#92;/def/&#34;, the second
&lt;slash&gt; stands for itself, so that the RE is <tt>&#34;abc/def&#34;, and in <tt>&#34;&#92;xabc&#92;xdefx&#34;, the second <tt>&#39;x&#39;
stands for itself, so that the RE is <tt>&#34;abcxdef&#34;.
<p>An editing command with no addresses shall select every pattern space.
<p>An editing command with one address shall select each pattern space that matches the address.
<p>An editing command with two addresses shall select the inclusive range from the first pattern space that matches the first
address through the next pattern space that matches the second. (If the second address is a number less than or equal to the line
number first selected, only one line shall be selected.) Starting at the first line following the selected range, <i>sed shall
look again for the first address. Thereafter, the process shall be repeated. Omitting either or both of the address components in
the following form produces undefined results:
<pre>
<b>&#91;<i>address<b>&#91;<tt>,<i>address<b>&#93;&#93;<tt>

<h5><a name="tag_20_109_13_02" id="tag_20_109_13_02">Regular Expressions in sed
<p>The <i>sed utility shall support the REs described in XBD <a href="../basedefs/V1_chap09.html#tag_09"><i>9. Regular
Expressions; by default it shall use BREs as described in XBD <a href="../basedefs/V1_chap09.html#tag_09_03"><i>9.3 Basic
Regular Expressions, but if the <b>-E option is used, it shall use EREs as described in XBD <a href=
"../basedefs/V1_chap09.html#tag_09_04"><i>9.4 Extended Regular Expressions. In <i>sed, the BRE and ERE syntax shall be
extended as follows:
<ul>
<li>
<p>The delimiter character that precedes and follows the RE shall not terminate the RE when it appears within a bracket expression,
and shall have its normal meaning in the bracket expression. For example, the context address <tt>&#34;&#92;%&#91;%&#93;%&#34; is equivalent to
<tt>&#34;/&#91;%&#93;/&#34;, and the command <tt>&#34;s-&#91;0-9&#93;&#45;&#45;g&#34; is equivalent to <tt>&#34;s/&#91;0-9&#93;//g&#34;.

<li>
<p>The escape sequence <tt>&#39;&#92;n&#39; shall match a &lt;newline&gt; embedded in the pattern space. A literal &lt;newline&gt; shall
not be used in the RE of a context address or in the substitute function.

<li>
<p>If an RE is empty (that is, no pattern is specified) <i>sed shall behave as if the last RE used in the last command applied
(either as an address or as part of a substitute command) was specified.

<h5><a name="tag_20_109_13_03" id="tag_20_109_13_03">Editing Commands in sed
<p>In the following list of editing commands, the maximum number of permissible addresses for each function is indicated by
&#91;<i>0addr&#93;, &#91;<i>1addr&#93;, or &#91;<i>2addr&#93;, representing zero, one, or two addresses.
<p>The argument <i>text shall consist of one or more lines. A &lt;backslash&gt; in the text can be escaped with another
&lt;backslash&gt;. The application shall ensure that each embedded &lt;newline&gt; (that is, those other than the terminating
&lt;newline&gt; of the last line) in the text is preceded by an unescaped &lt;backslash&gt;. The behavior is unspecified if an
unescaped &lt;backslash&gt; is immediately followed by any character other than &lt;backslash&gt; or &lt;newline&gt;, or by the end
of a <i>script.
<p>The <b>r and <b>w command verbs, and the <i>w flag to the <b>s command, take an <i>rfile (or <i>wfile)
parameter, separated from the command verb letter or flag by one or more &lt;blank&gt; characters; implementations may allow zero
separation as an extension.
<p>The argument <i>rfile or the argument <i>wfile shall terminate the editing command. Each <i>wfile shall be created
before processing begins. Implementations shall support at least ten <i>wfile arguments in the script; the actual number
(greater than or equal to 10) that is supported by the implementation is unspecified. The use of the <i>wfile parameter shall
cause that file to be initially created, if it does not exist, or shall replace the contents of an existing file.
<p>The <b>b, <b>r, <b>s, <b>t, <b>w, <b>y, and <b>: command verbs shall accept additional arguments.
The following synopses indicate which arguments shall be separated from the command verbs by a single &lt;space&gt;.
<p>The <b>a and <b>r commands schedule text for later output. The text specified for the <b>a command, and the contents
of the file specified for the <b>r command, shall be written to standard output just before the next attempt to fetch a line of
input when executing the <b>c, <b>D, <b>d, <b>N, or <b>n commands, just before executing the <b>q command,
or when reaching the end of the script. If written when reaching the end of the script, and the <b>-n option was not specified,
the text shall be written after copying the pattern space to standard output. The contents of the file specified for the <b>r
command shall be as of the time the output is written, not the time the <b>r command is applied. The text shall be output in
the order in which the <b>a and <b>r commands were applied to the input.
<p>Editing commands other than <b>a, <b>b, <b>c, <b>i, <b>r, <b>t, <b>w, <b>:, and <b># can be
followed by a &lt;semicolon&gt;, optional &lt;blank&gt; characters, and another editing command. However, when an <b>s editing
command is used with the <i>w flag, following it with another command in this manner produces undefined results.
<p>A function can be preceded by a <tt>&#39;!&#39; character, in which case the function shall be applied if the addresses do not
select the pattern space. Zero or more &lt;blank&gt; characters shall be accepted before the <tt>&#39;!&#39; character. It is
unspecified whether &lt;blank&gt; characters can follow the <tt>&#39;!&#39; character, and conforming applications shall not follow
the <tt>&#39;!&#39; character with &lt;blank&gt; characters.
<p>If a <i>label argument (to a <b>b, <b>t, or <b>: command) contains characters outside of the portable filename
character set, or if a <i>label is longer than 8 bytes, the behavior is unspecified. The implementation shall support
<i>label arguments recognized as unique up to at least 8 bytes; the actual length (greater than or equal to 8) supported by the
implementation is unspecified. It is unspecified whether exceeding the maximum supported label length causes an error or a silent
truncation.
<dl compact>
<dd>
<dt><b>&#91;<i>2addr<b>&#93; {<i>editing command
<dd>
<dt><i>editing command
<dd>
<dt>&#46;&#46;&#46;
<dd>
<dt><b>}
<dd>Execute a list of <i>sed editing commands only when the pattern space is selected. The list of <i>sed editing commands
shall be surrounded by braces. The braces can be preceded or followed by &lt;blank&gt; characters. The &lt;right-brace&gt; shall be
preceded by a &lt;newline&gt; or &lt;semicolon&gt; (before any optional &lt;blank&gt; characters preceding the
&lt;right-brace&gt;).
<p>Each command in the list of commands shall be terminated by a &lt;newline&gt; character, or by a &lt;semicolon&gt; character if
permitted when the command is used outside the braces. The editing commands can be preceded by &lt;blank&gt; characters, but shall
not be followed by &lt;blank&gt; characters.

<dt><b>&#91;<i>1addr<b>&#93;a&#92;
<dd>
<dt><i>text
<dd>Write text to standard output as described previously.
<dt><b>&#91;<i>2addr<b>&#93;b &#91;<i>label<b>&#93;
<dd><br>
Branch to the <b>: command verb bearing the <i>label argument. If <i>label is not specified, branch to the end of the
script.
<dt><b>&#91;<i>2addr<b>&#93;c&#92;
<dd>
<dt><i>text
<dd>Delete the pattern space. With a 0 or 1 address or at the end of a 2-address range, place <i>text on the output. Start the
next cycle.
<dt><b>&#91;<i>2addr<b>&#93;d
<dd>Delete the pattern space and start the next cycle.
<dt><b>&#91;<i>2addr<b>&#93;D
<dd>If the pattern space contains no &lt;newline&gt;, delete the pattern space and start a normal new cycle as if the <b>d
command was issued. Otherwise, delete the initial segment of the pattern space through the first &lt;newline&gt;, and start the
next cycle with the resultant pattern space and without reading any new input.
<dt><b>&#91;<i>2addr<b>&#93;g
<dd>Replace the contents of the pattern space by the contents of the hold space.
<dt><b>&#91;<i>2addr<b>&#93;G
<dd>Append to the pattern space a &lt;newline&gt; followed by the contents of the hold space.
<dt><b>&#91;<i>2addr<b>&#93;h
<dd>Replace the contents of the hold space with the contents of the pattern space.
<dt><b>&#91;<i>2addr<b>&#93;H
<dd>Append to the hold space a &lt;newline&gt; followed by the contents of the pattern space.
<dt><b>&#91;<i>1addr<b>&#93;i&#92;
<dd>
<dt><i>text
<dd>Write <i>text to standard output.
<dt><b>&#91;<i>2addr<b>&#93;l
<dd>(The letter ell.) Write the pattern space to standard output in a visually unambiguous form. The characters listed in XBD
<a href="../basedefs/V1_chap05.html#tagtcjh_2"><i>Escape Sequences and Associated Actions (<tt>&#39;&#92;&#92;&#39;, <tt>&#39;&#92;a&#39;,
<tt>&#39;&#92;b&#39;, <tt>&#39;&#92;f&#39;, <tt>&#39;&#92;r&#39;, <tt>&#39;&#92;t&#39;, <tt>&#39;&#92;v&#39;) shall be written as the corresponding escape sequence;
the <tt>&#39;&#92;n&#39; in that table is not applicable. Non-printable characters not in that table shall be written as one three-digit
octal number (with a preceding &lt;backslash&gt;) for each byte in the character (most significant byte first).
<p>Long lines shall be folded, with the point of folding indicated by writing a &lt;backslash&gt; followed by a &lt;newline&gt;;
the length at which folding occurs is unspecified, but should be appropriate for the output device. The end of each line shall be
marked with a <tt>&#39;&#36;&#39;.

<dt><b>&#91;<i>2addr<b>&#93;n
<dd>Write the pattern space to standard output if the default output has not been suppressed, and replace the pattern space with
the next line of input, less its terminating &lt;newline&gt;.
<p>If no next line of input is available, the <b>n command verb shall branch to the end of the script and quit without starting
a new cycle.

<dt><b>&#91;<i>2addr<b>&#93;N
<dd>Append the next line of input, less its terminating &lt;newline&gt;, to the pattern space, using an embedded &lt;newline&gt; to
separate the appended material from the original material. Note that the current line number changes.
<p>If no next line of input is available, the <b>N command verb shall branch to the end of the script and quit without starting
a new cycle or copying the pattern space to standard output.

<dt><b>&#91;<i>2addr<b>&#93;p
<dd>Write the pattern space to standard output.
<dt><b>&#91;<i>2addr<b>&#93;P
<dd>Write the pattern space, up to the first &lt;newline&gt;, to standard output.
<dt><b>&#91;<i>1addr<b>&#93;q
<dd>Branch to the end of the script and quit without starting a new cycle.
<dt><b>&#91;<i>1addr<b>&#93;r <i>rfile
<dd>Copy the contents of <i>rfile to standard output as described previously. If <i>rfile does not exist or cannot be read,
it shall be treated as if it were an empty file, causing no error condition.
<dt><b>&#91;<i>2addr<b>&#93;s/<i>RE<b>/<i>replacement<b>/<i>flags
<dd><br>
Substitute the replacement string for instances of the RE in the pattern space. Any character other than &lt;backslash&gt; or
&lt;newline&gt; can be used instead of a &lt;slash&gt; to delimit the RE and the replacement. Within the RE (as a <i>sed
extension to the BRE and ERE syntax) and the replacement, the delimiter shall not terminate the RE or replacement if it is the
second character of an escape sequence (see XBD <a href="../basedefs/V1_chap09.html#tag_09_01"><i>9.1 Regular Expression
Definitions). If the delimiter character is not listed as a special BRE character (if the <b>-E option is not
specified) or a special ERE character (if <b>-E is specified) in XBD <a href="../basedefs/V1_chap09.html#tag_09_03_03"><i>9.3.3
BRE Special Characters or XBD <a href="../basedefs/V1_chap09.html#tag_09_04_03"><i>9.4.3 ERE Special Characters,
respectively, the escaped delimiter shall be treated as that literal character in the RE; otherwise, it is unspecified whether the
escaped delimiter is treated as the literal character or the special character. Likewise, if the delimiter character is not
&lt;ampersand&gt; (<tt>&#39;&amp;&#39;), the escaped delimiter shall be treated as that literal character in the replacement; if it is
&lt;ampersand&gt;, it is unspecified whether the escaped delimiter is treated as the literal character or the special character
(see below).
<p>The replacement string shall be scanned from beginning to end. An &lt;ampersand&gt; (<tt>&#39;&amp;&#39;) appearing in the
replacement shall be replaced by the string matching the RE. The special meaning of <tt>&#39;&amp;&#39; in this context can be
suppressed by preceding it by a &lt;backslash&gt;. The characters <tt>&#34;&#92;<i>n&#34;, where <i>n is a digit, shall be
replaced by the text matched by the corresponding back-reference expression. If the corresponding back-reference expression does
not match, then the characters <tt>&#34;&#92;<i>n&#34; shall be replaced by the empty string. The special meaning of
<tt>&#34;&#92;<i>n&#34; where <i>n is a digit in this context, can be suppressed by preceding it by a &lt;backslash&gt;. For each
other &lt;backslash&gt; encountered, the following character shall lose its special meaning (if any).
<p>A line can be split by substituting a &lt;newline&gt; into it. The application shall escape the &lt;newline&gt; in the
replacement by preceding it by a &lt;backslash&gt;.
<p>The meaning of an unescaped &lt;backslash&gt; immediately followed by any character other than <tt>&#39;&amp;&#39;,
&lt;backslash&gt;, a digit, &lt;newline&gt;, or the delimiter character used for this command, is unspecified.
<p>Any &lt;backslash&gt; used to alter the default meaning of a subsequent character shall be discarded from the resulting
replacement string. A substitution shall be considered to have been performed even if the resulting replacement string is identical
to the string that it replaces.
<p>The value of <i>flags shall be zero or more of:
<dl compact>
<dd>
<dt><i>n
<dd>Substitute for the <i>nth occurrence only of the RE found within the pattern space.
<dt><b>g
<dd>Globally substitute for all non-overlapping instances of the RE rather than just the first one. If both <b>g and <i>n
are specified, the results are unspecified.
<dt><b>i
<dd>Match the regular expression in a case-insensitive way.
<dt><b>p
<dd>Write the pattern space to standard output if a replacement was made.
<dt><b>w <i>wfile
<dd>Write. Append the pattern space to <i>wfile if a replacement was made. A conforming application shall precede the
<i>wfile argument with one or more &lt;blank&gt; characters. If the <b>w flag is not the last flag value given in a
concatenation of multiple flag values, the results are undefined.

<dt><b>&#91;<i>2addr<b>&#93;t &#91;<i>label<b>&#93;
<dd><br>
Test. Branch to the <b>: command verb bearing the <i>label if any substitutions have been made since the most recent
reading of an input line or execution of a <b>t. If <i>label is not specified, branch to the end of the script.
<dt><b>&#91;<i>2addr<b>&#93;w <i>wfile
<dd><br>
Append (write) the pattern space to <i>wfile.
<dt><b>&#91;<i>2addr<b>&#93;x
<dd>Exchange the contents of the pattern and hold spaces.
<dt><b>&#91;<i>2addr<b>&#93;y/<i>string1<b>/<i>string2<b>/
<dd><br>
Replace all occurrences of characters in <i>string1 with the corresponding characters in <i>string2. If a &lt;backslash&gt;
followed by an <tt>&#39;n&#39; appear in <i>string1 or <i>string2, the two characters shall be handled as a single
&lt;newline&gt;. If (after resolving any escape sequences) the numbers of characters in <i>string1 and <i>string2 are not
equal, or if any of the characters in <i>string1 appear more than once, the results are undefined. Any character other than
&lt;backslash&gt; or &lt;newline&gt; can be used instead of &lt;slash&gt; to delimit the strings. If the delimiter is not
<tt>&#39;n&#39;, within <i>string1 and <i>string2, the delimiter itself can be used as a literal character if it is preceded
by an unescaped &lt;backslash&gt;. If a &lt;backslash&gt; character is escaped by an immediately preceding unescaped
&lt;backslash&gt; character in <i>string1 or <i>string2, the two &lt;backslash&gt; characters shall be treated as a single
literal &lt;backslash&gt; character. The meaning of an unescaped &lt;backslash&gt; followed by any character that is not
<tt>&#39;n&#39;, a &lt;backslash&gt;, or the delimiter character is undefined.
<dt><b>&#91;<i>0addr<b>&#93;:<i>label
<dd>Do nothing. This command bears a <i>label to which the <b>b and <b>t commands branch.
<dt><b>&#91;<i>1addr<b>&#93;=
<dd>Write the following to standard output:
<pre>
<tt>&#34;%d&#92;n&#34;, &lt;<i>current line number<tt>&gt;

<dt><b>&#91;<i>0addr<b>&#93;
<dd>Ignore this empty command.
<dt><b>&#91;<i>0addr<b>&#93;#
<dd>Ignore the <tt>&#39;#&#39; and the remainder of the line (treat them as a comment), with the single exception that if the first
two characters in the script are <tt>&#34;#n&#34;, the default output shall be suppressed; this shall be the equivalent of specifying
<b>-n on the command line.

<h4 class="mansect"><a name="tag_20_109_14" id="tag_20_109_14">EXIT STATUS
<blockquote>
<p>The following exit values shall be returned:
<dl compact>
<dd>
<dt> 0
<dd>Successful completion.
<dt>&gt;0
<dd>An error occurred.

<h4 class="mansect"><a name="tag_20_109_15" id="tag_20_109_15">CONSEQUENCES OF ERRORS
<blockquote>
<p>Default.

<hr>
<div class="box"><em>The following sections are informative.
<h4 class="mansect"><a name="tag_20_109_16" id="tag_20_109_16">APPLICATION USAGE
<blockquote>
<p>Regular expressions match entire strings, not just individual lines, but a &lt;newline&gt; is matched by <tt>&#39;&#92;n&#39; in a
<i>sed RE; a &lt;newline&gt; is not allowed by the general definition of regular expression in POSIX.1-2024. Also note that
<tt>&#39;&#92;n&#39; cannot be used to match a &lt;newline&gt; at the end of an arbitrary input line; &lt;newline&gt; characters appear in
the pattern space as a result of the <b>N editing command.
<p>Applications that use a special RE character as a delimiter (for example, <tt>&#39;.&#39; or <tt>&#39;&#42;&#39;) and need to use the
delimiter as a literal character in the RE should put it inside a bracket expression, as implementations differ regarding whether
escaping it with a &lt;backslash&gt; removes its special meaning. For example, for the context address <tt>&#34;/&#92;.&#91;0-9&#93;/&#34; to be
written with <tt>&#39;.&#39; as delimiter, the form <tt>&#34;&#92;.&#91;.&#93;&#91;0-9&#93;.&#34; needs to be used; <tt>&#34;&#92;.&#92;.&#91;0-9&#93;.&#34; cannot be used
portably for this purpose, as it is unspecified whether this would be equivalent to <tt>&#34;/&#92;.&#91;0-9&#93;/&#34; or <tt>&#34;/.&#91;0-9&#93;/&#34;.
Portable applications cannot use a special RE character as a delimiter if that character needs to have its special meaning in the
RE, as escaping it may remove its special meaning.
<p>When using <i>sed to process pathnames, it is recommended that LC&#95;ALL, or at least LC&#95;CTYPE and LC&#95;COLLATE, are set to POSIX
or C in the environment, since pathnames can contain byte sequences that do not form valid characters in some locales, in which
case the utility&#39;s behavior would be undefined. In the POSIX locale each byte is a valid single-byte character, and therefore this
problem is avoided.
<p>Note that some implementations of <i>sed also support an <b>I flag for the <b>s command as an alias for the lower
case <b>i flag.
<p>Some implementations of <i>sed, when executed in a non-conforming environment, handle &lt;backslash&gt; escapes in regular
expressions in a similar way to how <a href="../utilities/awk.html"><i>awk handles them in the lexical token <b>ERE
(processing <tt>&#34;&#92;t&#34; as a tab character, etc.). This is a compatible extension except that it conflicts with the requirements
of this standard when &lt;backslash&gt; appears inside a bracket expression. A future version of this standard may allow this
behavior, and therefore applications should use two &lt;backslash&gt; characters in bracket expressions instead of one in order to
ensure future portability. On implementations conforming to the current standard, the second &lt;backslash&gt; is redundant. In the
future (and in current non-conforming environments) the first &lt;backslash&gt; may escape the second.

<h4 class="mansect"><a name="tag_20_109_17" id="tag_20_109_17">EXAMPLES
<blockquote>
<p>This <i>sed script simulates the BSD <a href="../utilities/cat.html"><i>cat <b>-s command, squeezing excess
empty lines from standard input.
<pre>
<tt>sed -n &#39;
# Write non-empty lines.
/./ {
    p
    d
    }
# Write a single empty line, then look for more empty lines.
/^&#36;/    p
# Get next line, discard the held &lt;newline&gt; (empty line),
# and look for more empty lines.
:Empty
/^&#36;/    {
    N
    s/.//
    b Empty
    }
# Write the non-empty line before going back to search
# for the first in a set of empty lines.
    p
&#39;

<p>The following <i>sed command is a much simpler method of squeezing empty lines, although it is not quite the same as
<a href="../utilities/cat.html"><i>cat <b>-s since it removes any initial empty lines:
<pre>
<tt>sed -n &#39;/./,/^&#36;/p&#39;

<h4 class="mansect"><a name="tag_20_109_18" id="tag_20_109_18">RATIONALE
<blockquote>
<p>This volume of POSIX.1-2024 requires implementations to support at least ten distinct <i>wfiles, matching historical
practice on many implementations. Implementations are encouraged to support more, but conforming applications should not exceed
this limit.
<p>The exit status codes specified here are different from those in System V. System V returns 2 for garbled <i>sed commands,
but returns zero with its usage message or if the input file could not be opened. The standard developers considered this to be a
bug.
<p>The manner in which the <b>l command writes non-printable characters was changed to avoid the historical
backspace-overstrike method, and other requirements to achieve unambiguous output were added. See the RATIONALE for <a href=
"../utilities/ed.html#"><i>ed for details of the format chosen, which is the same as that chosen for <i>sed.
<p>This volume of POSIX.1-2024 requires implementations to provide pattern and hold spaces of at least 8192 bytes, larger than the
4000 bytes spaces used by some historical implementations, but less than the 20480 bytes limit used in an early proposal.
Implementations are encouraged to allocate dynamically larger pattern and hold spaces as needed.
<p>The requirements for acceptance of &lt;blank&gt; and &lt;space&gt; characters in command lines has been made more explicit than
in early proposals to describe clearly the historical practice and to remove confusion about the phrase &#34;protect initial blanks
&#91;<i>sic&#93; and tabs from the stripping that is done on every script line&#34; that appears in much of the historical documentation
of the <i>sed utility description of text. (Not all implementations are known to have stripped &lt;blank&gt; characters from
text lines, although they all have allowed leading &lt;blank&gt; characters preceding the address on a command line.)
<p>The treatment of <tt>&#39;#&#39; comments differs from the SVID which only allows a comment as the first line of the script, but
matches BSD-derived implementations. The comment character is treated as a command, and it has the same properties in terms of
being accepted with leading &lt;blank&gt; characters; the BSD implementation has historically supported this.
<p>Early proposals required that a <i>script&#95;file have at least one non-comment line. Some historical implementations have
behaved in unexpected ways if this were not the case. The standard developers considered that this was incorrect behavior and that
application developers should not have to avoid this feature. A correct implementation of this volume of POSIX.1-2024 shall permit
<i>script&#95;files that consist only of comment lines.
<p>Early proposals indicated that if <b>-e and <b>-f options were intermixed, all <b>-e options were processed before
any <b>-f options. This has been changed to process them in the order presented because it matches historical practice and is
more intuitive.
<p>The characters &lt;backslash&gt; and &lt;newline&gt; cannot be used as RE delimiter characters, as they can never be recognized
as the ending delimiter:
<ul>
<li>
<p>&lt;backslash&gt; does not work, because if it appears unescaped later in the RE, it either escapes the following character,
which can then never be the ending delimiter, or it is part of a bracket expression, inside which the ending delimiter for the RE
cannot be located.

<li>
<p>&lt;newline&gt; does not work, because if not escaped, it terminates the command, meaning it cannot be the ending delimiter.

<p>Some historical <i>sed implementations did not support escaping <tt>&#39;(&#39;, <tt>&#39;)&#39;, <tt>&#39;{&#39;, and <tt>&#39;}&#39;
when used as a BRE delimiter, as the sequences <tt>&#34;&#92;(&#34; and so on were still treated as special, usually resulting in an
error. This standard requires that these sequences are treated as the literal character. This is for consistency with extensions.
For example, some implementations treat <tt>&#34;&#92;s&#34; in a BRE as matching white-space characters, as an extension. This cannot
have its special meaning when <tt>&#39;s&#39; is used as a BRE delimiter in order to ensure portability of <i>sed commands that
have <tt>&#39;s&#39; as a delimiter and escape it. If <tt>&#34;&#92;s&#34; were allowed to keep its special meaning, then the potential for
further extensions would mean portable applications would not be able to escape any delimiter character other than
&lt;slash&gt;.
<p>The treatment of the <b>p flag to the <b>s command differs between System V and BSD-based systems when the default
output is suppressed. In the two examples:
<pre>
<tt>echo a | sed    &#39;s/a/A/p&#39;
echo a | sed -n &#39;s/a/A/p&#39;

<p>this volume of POSIX.1-2024, BSD, System V documentation, and the SVID indicate that the first example should write two lines
with <b>A, whereas the second should write one. Some System V systems write the <b>A only once in both examples because the
<b>p flag is ignored if the <b>-n option is not specified.
<p>This is a case of a diametrical difference between systems that could not be reconciled through the compromise of declaring the
behavior to be unspecified. The SVID/BSD/System V documentation behavior was adopted for this volume of POSIX.1-2024 because:
<ul>
<li>
<p>No known documentation for any historic system describes the interaction between the <b>p flag and the <b>-n option.

<li>
<p>The selected behavior is more correct as there is no technical justification for any interaction between the <b>p flag and
the <b>-n option. A relationship between <b>-n and the <b>p flag might imply that they are only used together, but this
ignores valid scripts that interrupt the cyclical nature of the processing through the use of the <b>D, <b>d, <b>q, or
branching commands. Such scripts rely on the <b>p suffix to write the pattern space because they do not make use of the default
output at the &#34;bottom&#34; of the script.

<li>
<p>Because the <b>-n option makes the <b>p flag unnecessary, any interaction would only be useful if <i>sed scripts
were written to run both with and without the <b>-n option. This is believed to be unlikely. It is even more unlikely that
programmers have coded the <b>p flag expecting it to be unnecessary. Because the interaction was not documented, the likelihood
of a programmer discovering the interaction and depending on it is further decreased.

<li>
<p>Finally, scripts that break under the specified behavior produce too much output instead of too little, which is easier to
diagnose and correct.

<p>The form of the substitute command that uses the <b>n suffix was limited to the first 512 matches in an early proposal. This
limit has been removed because there is no reason an editor processing lines of {LINE&#95;MAX} length should have this restriction. The
command <b>s/a/A/2047 should be able to substitute the 2047th occurrence of <b>a on a line.
<p>The <b>b, <b>t, and <b>: commands are documented to ignore leading white space, but no mention is made of trailing
white space. Historical implementations of <i>sed assigned different locations to the labels <tt>&#39;x&#39; and
<tt>&#34;x &#34;. This is not useful, and leads to subtle programming errors, but it is historical practice, and changing it
could theoretically break working scripts. Implementors are encouraged to provide warning messages about labels that are never
referenced by a <b>b or <b>t command, jumps to labels that do not exist, and label arguments that are subject to
truncation.
<p>Earlier versions of this standard allowed for implementations with bytes other than eight bits, but this has been modified in
this version.

<h4 class="mansect"><a name="tag_20_109_19" id="tag_20_109_19">FUTURE DIRECTIONS
<blockquote>
<p>A future version of this standard may allow <i>sed to handle &lt;backslash&gt; escapes in regular expressions in a similar
way to how <a href="../utilities/awk.html"><i>awk handles them in the lexical token <b>ERE. (&#34;Similar&#34; rather than
&#34;the same&#34; because <i>sed can use BREs or EREs whereas <a href="../utilities/awk.html"><i>awk uses only EREs.)

<h4 class="mansect"><a name="tag_20_109_20" id="tag_20_109_20">SEE ALSO
<blockquote>
<p><a href="../utilities/awk.html#"><i>awk, <a href="../utilities/ed.html#"><i>ed, <a href=
"../utilities/grep.html#"><i>grep
<p>XBD <a href="../basedefs/V1_chap05.html#tagtcjh_2"><i>Escape Sequences and Associated Actions, <a href=
"../basedefs/V1_chap08.html#tag_08"><i>8. Environment Variables, <a href="../basedefs/V1_chap09.html#tag_09_03"><i>9.3
Basic Regular Expressions, <a href="../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines

<h4 class="mansect"><a name="tag_20_109_21" id="tag_20_109_21">CHANGE HISTORY
<blockquote>
<p>First released in Issue 2.

<h4 class="mansect"><a name="tag_20_109_22" id="tag_20_109_22">Issue 5
<blockquote>
<p>The FUTURE DIRECTIONS section is added.

<h4 class="mansect"><a name="tag_20_109_23" id="tag_20_109_23">Issue 6
<blockquote>
<p>The following new requirements on POSIX implementations derive from alignment with the Single UNIX Specification:
<ul>
<li>
<p>Implementations are required to support at least ten <i>wfile arguments in an editing command.

<p>The EXTENDED DESCRIPTION is changed to align with the IEEE P1003.2b draft standard.
<p>IEEE PASC Interpretation 1003.2 #190 is applied.
<p>IEEE PASC Interpretation 1003.2 #203 is applied, clarifying the meaning of the &lt;backslash&gt;-escape sequences in a
replacement string for a BRE.
<p>IEEE Std 1003.1-2001/Cor 2-2004, item XCU/TC2/D6/28 is applied, removing text describing behavior on systems with
bytes consisting of more than eight bits.
<p>IEEE Std 1003.1-2001/Cor 2-2004, item XCU/TC2/D6/29 is applied, making an editorial correction within the Editing
Commands in <i>sed section.

<h4 class="mansect"><a name="tag_20_109_24" id="tag_20_109_24">Issue 7
<blockquote>
<p>Austin Group Interpretations 1003.1-2001 #006, #036, and #092 are applied.
<p>SD5-XCU-ERN-97 and SD5-XCU-ERN-123 are applied, updating the SYNOPSIS.
<p>A second example is added.
<p>POSIX.1-2008, Technical Corrigendum 1, XCU/TC1-2008/0133 &#91;262&#93;, XCU/TC1-2008/0134 &#91;282,431&#93;, XCU/TC1-2008/0135 &#91;269&#93;, and
XCU/TC1-2008/0136 &#91;282,431&#93; are applied.
<p>POSIX.1-2008, Technical Corrigendum 2, XCU/TC2-2008/0166 &#91;945&#93;, XCU/TC2-2008/0167 &#91;944&#93;, XCU/TC2-2008/0168 &#91;945&#93;,
XCU/TC2-2008/0169 &#91;944&#93;, XCU/TC2-2008/0170 &#91;945&#93;, XCU/TC2-2008/0171 &#91;533&#93;, XCU/TC2-2008/0172 &#91;663&#93;, XCU/TC2-2008/0173 &#91;945&#93;, and
XCU/TC2-2008/0174 &#91;944&#93; are applied.

<h4 class="mansect"><a name="tag_20_109_25" id="tag_20_109_25">Issue 8
<blockquote>
<p>Austin Group Defect 528 is applied, adding support for selecting the use of EREs instead of BREs, by specifying the <b>-E
option.
<p>Austin Group Defect 779 is applied, adding the <b>i flag to the <b>s command.
<p>Austin Group Defect 961 is applied, requiring that <b>{&#46;&#46;&#46;} can be followed by a &lt;semicolon&gt;, optional &lt;blank&gt;
characters, and another editing command.
<p>Austin Group Defect 1122 is applied, changing the description of <i>NLSPATH .
<p>Austin Group Defect 1231 is applied, clarifying the handling of &lt;backslash&gt; in <i>text arguments.
<p>Austin Group Defect 1233 is applied, changing the APPLICATION USAGE and FUTURE DIRECTIONS sections.
<p>Austin Group Defect 1319 is applied, changing when the text specified for the <b>a command and the contents of the file
specified for the <b>r command are written.
<p>Austin Group Defect 1550 is applied, clarifying requirements relating to delimiters in context addresses and in <b>s and
<b>y commands.
<p>Austin Group Defect 1578 is applied, clarifying the description of the <b>y command.
<p>Austin Group Defect 1767 is applied, clarifying that a <b>c command starts the next cycle on every line that its address
range matches.

<div class="box"><em>End of informative text.
<hr>

