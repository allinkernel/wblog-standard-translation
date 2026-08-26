<!-- 英文原文镜像：https://pubs.opengroup.org/onlinepubs/9799919799/utilities/awk.html -->
<body bgcolor="white">

<a name="top" id="top"> <a name="awk" id="awk"> <a name="tag_20_06" id="tag_20_06"><!-- awk -->
<h4 class="mansect"><a name="tag_20_06_01" id="tag_20_06_01">NAME
<blockquote>awk — pattern scanning and processing language
<h4 class="mansect"><a name="tag_20_06_02" id="tag_20_06_02">SYNOPSIS
<blockquote class="synopsis">
<p><code><tt>awk <b>&#91;<tt>-F <i>sepstring<b>&#93; &#91;<tt>-v <i>assignment<b>&#93;<tt>&#46;&#46;&#46; <i>program
<b>&#91;<i>argument<tt>&#46;&#46;&#46;<b>&#93; <tt><br>
<br>
awk <b>&#91;<tt>-F <i>sepstring<b>&#93; <tt>-f <i>progfile <b>&#91;<tt>-f
<i>progfile<b>&#93;<tt>&#46;&#46;&#46; <b>&#91;<tt>-v <i>assignment<b>&#93;<tt>&#46;&#46;&#46;<br>
       <b>&#91;<i>argument<tt>&#46;&#46;&#46;<b>&#93; <tt><br>

<h4 class="mansect"><a name="tag_20_06_03" id="tag_20_06_03">DESCRIPTION
<blockquote>
<p>The <i>awk utility shall execute programs written in the <i>awk programming language, which is specialized for textual
data manipulation. An <i>awk program is a sequence of patterns and corresponding actions. When input is read that matches a
pattern, the action associated with that pattern is carried out.
<p>Input shall be interpreted as a sequence of records. By default, a record is a line, less its terminating &lt;newline&gt;, but
this can be changed by using the <b>RS built-in variable. Each record of input shall be matched in turn against each pattern in
the program. For each pattern matched, the associated action shall be executed.
<p>The <i>awk utility shall interpret each input record as a sequence of fields where, by default, a field is a string of
non-&lt;blank&gt; non-&lt;newline&gt; characters. This default &lt;blank&gt; and &lt;newline&gt; field delimiter can be changed by
using the <b>FS built-in variable or the <b>-F <i>sepstring option. The <i>awk utility shall denote the first field
in a record &#36;1, the second &#36;2, and so on. The symbol &#36;0 shall refer to the entire record; setting any other field causes the
re-evaluation of &#36;0. Assigning to &#36;0 shall reset the values of all other fields and the <b>NF built-in variable.

<h4 class="mansect"><a name="tag_20_06_04" id="tag_20_06_04">OPTIONS
<blockquote>
<p>The <i>awk utility shall conform to XBD <a href="../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax
Guidelines.
<p>The following options shall be supported:
<dl compact>
<dd>
<dt><b>-F <i>sepstring
<dd>Define the input field separator. This option shall be equivalent to:
<pre>
<tt>-v FS=<i>sepstring

<p>except that if <b>-F <i>sepstring and <b>-v <i><tt>FS=sepstring are both used, it is unspecified whether
the <b>FS assignment resulting from <b>-F <i>sepstring is processed in command line order or is processed after the
last <b>-v <i><tt>FS=sepstring. See the description of the <b>FS built-in variable, and how it is used, in the
EXTENDED DESCRIPTION section.

<dt><b>-f <i>progfile
<dd>Specify the pathname of the file <i>progfile containing an <i>awk program. A pathname of <tt>&#39;-&#39; shall denote the
standard input. If multiple instances of this option are specified, the concatenation of the files specified as <i>progfile in
the order specified shall be the <i>awk program. The <i>awk program can alternatively be specified in the command line as a
single argument.
<dt><b>-v <i>assignment
<dd>
The application shall ensure that the <i>assignment argument is in the same form as an <i>assignment operand. The specified
variable assignment shall occur prior to executing the <i>awk program, including the actions associated with <b>BEGIN
patterns (if any). Multiple occurrences of this option can be specified.

<h4 class="mansect"><a name="tag_20_06_05" id="tag_20_06_05">OPERANDS
<blockquote>
<p>The following operands shall be supported:
<dl compact>
<dd>
<dt><i>program
<dd>If no <b>-f option is specified, the first operand to <i>awk shall be the text of the <i>awk program. The
application shall supply the <i>program operand as a single argument to <i>awk. If the text does not end in a
&lt;newline&gt;, <i>awk shall interpret the text as if it did.
<dt><i>argument
<dd>Either of the following two types of <i>argument can be intermixed:
<dl compact>
<dd>
<dt><i>file
<dd>A pathname of a file that contains the input to be read, which is matched against the set of patterns in the program. If no
<i>file operands or their equivalents, achieved by modifying the <i>awk variables <b>ARGV and <b>ARGC, are
specified, or if a <i>file operand is <tt>&#39;-&#39;, the standard input shall be used.
<dt><i>assignment
<dd>An operand that begins with an &lt;underscore&gt; or alphabetic character from the portable character set (see the table in XBD
<a href="../basedefs/V1_chap06.html#tag_06_01"><i>6.1 Portable Character Set), followed by a sequence of underscores,
digits, and alphabetics from the portable character set, followed by the <tt>&#39;=&#39; character, shall specify a variable
assignment rather than a pathname. The characters before the <tt>&#39;=&#39; represent the name of an <i>awk variable; if that
name is an <i>awk reserved word (see <a href="#tag_20_06_13_16">Grammar) the behavior is undefined. The characters
following the &lt;equals-sign&gt; shall be interpreted as if they appeared in the <i>awk program preceded and followed by a
double-quote (<tt>&#39;&#34;&#39; ) character, as a <b>STRING token (see <a href="#tag_20_06_13_16">Grammar), except that if the
last character is an unescaped &lt;backslash&gt;, it shall be interpreted as a literal &lt;backslash&gt; rather than as the first
character of the sequence <tt>&#34;&#92;&#34;&#34;. The variable shall be assigned the value of that <b>STRING token and, if appropriate,
shall be considered a <i>numeric string (see <a href="#tag_20_06_13_02">Expressions in awk), the variable shall also be
assigned its numeric value. Each such variable assignment shall occur just prior to the processing of the following <i>file, if
any. Thus, an assignment before the first <i>file argument shall be executed after the <b>BEGIN actions (if any), while an
assignment after the last <i>file argument shall occur before the <b>END actions (if any). If there are no <i>file
arguments or their equivalents, achieved by modifying the <i>awk variables <b>ARGV and <b>ARGC, assignments shall be
executed before processing the standard input.

<h4 class="mansect"><a name="tag_20_06_06" id="tag_20_06_06">STDIN
<blockquote>
<p>The standard input shall be used only if no <i>file operands or their equivalents, achieved by modifying the <i>awk
variables <b>ARGV and <b>ARGC, are specified; or if a <i>file operand, or its equivalent, is <tt>&#39;-&#39;; or if a
<i>progfile option-argument is <tt>&#39;-&#39;; see the INPUT FILES section. If the <i>awk program contains no actions and no
patterns, but is otherwise a valid <i>awk program, standard input and any <i>file operands shall not be read and <i>awk
shall exit with a return status of zero.

<h4 class="mansect"><a name="tag_20_06_07" id="tag_20_06_07">INPUT FILES
<blockquote>
<p>Input files to the <i>awk program from any of the following sources shall be text files:
<ul>
<li>
<p>Any <i>file operands or their equivalents, achieved by modifying the <i>awk variables <b>ARGV and <b>ARGC

<li>
<p>Standard input in the absence of any <i>file operands, or their equivalents

<li>
<p>Arguments to the <b>getline function

<p>Whether the variable <b>RS is set to a value other than a &lt;newline&gt; or not, for these files, implementations shall
support records terminated with the specified separator up to {LINE&#95;MAX} bytes and may support longer records.
<p>If <b>-f <i>progfile is specified, the application shall ensure that the files named by each of the <i>progfile
option-arguments are text files and their concatenation, in the same order as they appear in the arguments, is an <i>awk
program.

<h4 class="mansect"><a name="tag_20_06_08" id="tag_20_06_08">ENVIRONMENT VARIABLES
<blockquote>
<p>The following environment variables shall affect the execution of <i>awk:
<dl compact>
<dd>
<dt><i>LANG
<dd>Provide a default value for the internationalization variables that are unset or null. (See XBD <a href=
"../basedefs/V1_chap08.html#tag_08_02"><i>8.2 Internationalization Variables for the precedence of internationalization
variables used to determine the values of locale categories.)
<dt><i>LC&#95;ALL
<dd>If set to a non-empty string value, override the values of all the other internationalization variables.
<dt><i>LC&#95;COLLATE
<dd>
Determine the locale for the behavior of ranges, equivalence classes, and multi-character collating elements within regular
expressions and in comparisons of string values.
<dt><i>LC&#95;CTYPE
<dd>Determine the locale for the interpretation of sequences of bytes of text data as characters (for example, single-byte as
opposed to multi-byte characters in arguments and input files), the behavior of character classes within regular expressions, the
identification of characters as letters, and the mapping of uppercase and lowercase characters for the <b>toupper and
<b>tolower functions.
<dt><i>LC&#95;MESSAGES
<dd>
Determine the locale that should be used to affect the format and contents of diagnostic messages written to standard error.
<dt><i>LC&#95;NUMERIC
<dd>
Determine the radix character used when interpreting numeric input, performing conversions between numeric and string values, and
formatting numeric output. Regardless of locale, the &lt;period&gt; character (the decimal-point character of the POSIX locale) is
the decimal-point character recognized in processing <i>awk programs (including assignments in command line arguments).
<dt><i>NLSPATH
<dd><sup>&#91;<a href="javascript:open_code('XSI')">XSI&#93; <img src=".pic/opt-start.gif" alt="[Option Start]" border="0">
Determine the location of messages objects and message catalogs. <img src=".pic/opt-end.gif" alt="[Option End]" border=
"0">
<dt><i>PATH
<dd>Determine the search path when looking for commands executed by <i>system(<i>expr), or input and output pipes; see XBD
<a href="../basedefs/V1_chap08.html#tag_08"><i>8. Environment Variables.

<p>In addition, all environment variables shall be visible via the <i>awk variable <b>ENVIRON.

<h4 class="mansect"><a name="tag_20_06_09" id="tag_20_06_09">ASYNCHRONOUS EVENTS
<blockquote>
<p>Default.

<h4 class="mansect"><a name="tag_20_06_10" id="tag_20_06_10">STDOUT
<blockquote>
<p>The nature of the output files depends on the <i>awk program.

<h4 class="mansect"><a name="tag_20_06_11" id="tag_20_06_11">STDERR
<blockquote>
<p>The standard error shall be used only for diagnostic messages.

<h4 class="mansect"><a name="tag_20_06_12" id="tag_20_06_12">OUTPUT FILES
<blockquote>
<p>The nature of the output files depends on the <i>awk program.<br>

<h4 class="mansect"><a name="tag_20_06_13" id="tag_20_06_13">EXTENDED DESCRIPTION
<blockquote>
<h5><a name="tag_20_06_13_01" id="tag_20_06_13_01">Overall Program Structure
<p>An <i>awk program is composed of pairs of the form:
<pre>
<i>pattern<tt> { <i>action<tt> }

<p>Either the pattern or the action (including the enclosing brace characters) can be omitted.
<p>A missing pattern shall match any record of input, and a missing action shall be equivalent to:
<pre>
<tt>{ print }

<p>Execution of the <i>awk program shall start by first executing the actions associated with all <b>BEGIN patterns in the
order they occur in the program. Then each <i>file operand (or standard input if no files were specified) shall be processed in
turn by reading data from the file until a record separator is seen (&lt;newline&gt; by default). Before the first reference to a
field in the record is evaluated, the record shall be split into fields, according to the rules in <a href=
"#tag_20_06_13_04">Regular Expressions, using the value of <b>FS that was current at the time the record was read. Each
pattern in the program then shall be evaluated in the order of occurrence, and the action associated with each pattern that matches
the current record executed. The action for a matching pattern shall be executed before evaluating subsequent patterns. Finally,
the actions associated with all <b>END patterns shall be executed in the order they occur in the program.
<h5><a name="tag_20_06_13_02" id="tag_20_06_13_02">Expressions in awk
<p>Expressions describe computations used in <i>patterns and <i>actions. In the following table, valid expression
operations are given in groups from highest precedence first to lowest precedence last, with equal-precedence operators grouped
between horizontal lines. In expression evaluation, where the grammar is formally ambiguous, higher precedence operators shall be
evaluated before lower precedence operators. In this table <i>expr, <i>expr1, <i>expr2, and <i>expr3 represent any
expression, while lvalue represents any entity that can be assigned to (that is, on the left side of an assignment operator). The
precise syntax of expressions is given in <a href="#tag_20_06_13_16">Grammar.
<p class="caption"><a name="tagtcjh_14" id="tagtcjh_14"> Table: Expressions in Decreasing Precedence in awk
<center>
<table border="1" cellpadding="3" align="center">
<tr valign="top">
<th align="center">
<p class="tent"><b>Syntax

<th align="center">
<p class="tent"><b>Name

<th align="center">
<p class="tent"><b>Type of Result

<th align="center">
<p class="tent"><b>Associativity

<tr valign="top">
<td align="left">
<p class="tent">(<i>expr)

<td align="left">
<p class="tent">Grouping

<td align="left">
<p class="tent">Type of <i>expr

<td align="left">
<p class="tent">N/A

<tr valign="top">
<td align="left">
<p class="tent">&#36;<i>expr

<td align="left">
<p class="tent">Field reference

<td align="left">
<p class="tent">Uninitialized or String

<td align="left">
<p class="tent">N/A

<tr valign="top">
<td align="left">
<p class="tent">lvalue ++
<p class="tent">lvalue &#45;&#45;

<td align="left">
<p class="tent">Post-increment
<p class="tent">Post-decrement

<td align="left">
<p class="tent">Numeric
<p class="tent">Numeric

<td align="left">
<p class="tent">N/A
<p class="tent">N/A

<tr valign="top">
<td align="left">
<p class="tent">++ lvalue
<p class="tent">&#45;&#45; lvalue

<td align="left">
<p class="tent">Pre-increment
<p class="tent">Pre-decrement

<td align="left">
<p class="tent">Numeric
<p class="tent">Numeric

<td align="left">
<p class="tent">N/A
<p class="tent">N/A

<tr valign="top">
<td align="left">
<p class="tent"><i>expr ^ <i>expr

<td align="left">
<p class="tent">Exponentiation

<td align="left">
<p class="tent">Numeric

<td align="left">
<p class="tent">Right

<tr valign="top">
<td align="left">
<p class="tent">! <i>expr
<p class="tent">+ <i>expr
<p class="tent">- <i>expr

<td align="left">
<p class="tent">Logical not
<p class="tent">Unary plus
<p class="tent">Unary minus

<td align="left">
<p class="tent">Numeric
<p class="tent">Numeric
<p class="tent">Numeric

<td align="left">
<p class="tent">N/A
<p class="tent">N/A
<p class="tent">N/A

<tr valign="top">
<td align="left">
<p class="tent"><i>expr &#42; <i>expr
<p class="tent"><i>expr / <i>expr
<p class="tent"><i>expr % <i>expr

<td align="left">
<p class="tent">Multiplication
<p class="tent">Division
<p class="tent">Modulus

<td align="left">
<p class="tent">Numeric
<p class="tent">Numeric
<p class="tent">Numeric

<td align="left">
<p class="tent">Left
<p class="tent">Left
<p class="tent">Left

<tr valign="top">
<td align="left">
<p class="tent"><i>expr + <i>expr
<p class="tent"><i>expr - <i>expr

<td align="left">
<p class="tent">Addition
<p class="tent">Subtraction

<td align="left">
<p class="tent">Numeric
<p class="tent">Numeric

<td align="left">
<p class="tent">Left
<p class="tent">Left

<tr valign="top">
<td align="left">
<p class="tent"><i>expr <i>expr

<td align="left">
<p class="tent">String concatenation

<td align="left">
<p class="tent">String

<td align="left">
<p class="tent">Left

<tr valign="top">
<td align="left">
<p class="tent"><i>expr &lt; <i>expr
<p class="tent"><i>expr &lt;= <i>expr
<p class="tent"><i>expr != <i>expr
<p class="tent"><i>expr == <i>expr
<p class="tent"><i>expr &gt; <i>expr
<p class="tent"><i>expr &gt;= <i>expr

<td align="left">
<p class="tent">Less than
<p class="tent">Less than or equal to
<p class="tent">Not equal to
<p class="tent">Equal to
<p class="tent">Greater than
<p class="tent">Greater than or equal to

<td align="left">
<p class="tent">Numeric
<p class="tent">Numeric
<p class="tent">Numeric
<p class="tent">Numeric
<p class="tent">Numeric
<p class="tent">Numeric

<td align="left">
<p class="tent">None
<p class="tent">None
<p class="tent">None
<p class="tent">None
<p class="tent">None
<p class="tent">None

<tr valign="top">
<td align="left">
<p class="tent"><i>expr ˜ <i>expr
<p class="tent"><i>expr !˜ <i>expr

<td align="left">
<p class="tent">ERE match
<p class="tent">ERE non-match

<td align="left">
<p class="tent">Numeric
<p class="tent">Numeric

<td align="left">
<p class="tent">None
<p class="tent">None

<tr valign="top">
<td align="left">
<p class="tent"><i>expr in array
<p class="tent">(<i>index) in <i>array

<td align="left">
<p class="tent">Array membership
<p class="tent">Multi-dimension array membership

<td align="left">
<p class="tent">Numeric
<p class="tent">Numeric

<td align="left">
<p class="tent">Left
<p class="tent">Left

<tr valign="top">
<td align="left">
<p class="tent"><i>expr &amp;&amp; <i>expr

<td align="left">
<p class="tent">Logical AND

<td align="left">
<p class="tent">Numeric

<td align="left">
<p class="tent">Left

<tr valign="top">
<td align="left">
<p class="tent"><i>expr || <i>expr

<td align="left">
<p class="tent">Logical OR

<td align="left">
<p class="tent">Numeric

<td align="left">
<p class="tent">Left

<tr valign="top">
<td align="left">
<p class="tent"><i>expr1 ? <i>expr2 : <i>expr3

<td align="left">
<p class="tent">Conditional expression

<td align="left">
<p class="tent">Type of selected<br><i>expr2 or <i>expr3

<td align="left">
<p class="tent">Right

<tr valign="top">
<td align="left">
<p class="tent">lvalue ^= <i>expr
<p class="tent">lvalue %= <i>expr
<p class="tent">lvalue &#42;= <i>expr
<p class="tent">lvalue /= <i>expr
<p class="tent">lvalue += <i>expr
<p class="tent">lvalue -= <i>expr
<p class="tent">lvalue = <i>expr

<td align="left">
<p class="tent">Exponentiation assignment
<p class="tent">Modulus assignment
<p class="tent">Multiplication assignment
<p class="tent">Division assignment
<p class="tent">Addition assignment
<p class="tent">Subtraction assignment
<p class="tent">Assignment

<td align="left">
<p class="tent">Numeric
<p class="tent">Numeric
<p class="tent">Numeric
<p class="tent">Numeric
<p class="tent">Numeric
<p class="tent">Numeric
<p class="tent">Type of <i>expr

<td align="left">
<p class="tent">Right
<p class="tent">Right
<p class="tent">Right
<p class="tent">Right
<p class="tent">Right
<p class="tent">Right
<p class="tent">Right

<p class="tent">Each expression shall have either a string value, a numeric value, or both. Except as stated for specific contexts,
the value of an expression shall be implicitly converted to the type needed for the context in which it is used. A string value
shall be converted to a numeric value either by the equivalent of the following calls to functions defined by the ISO C
standard:
<pre>
<tt>setlocale(LC&#95;NUMERIC, &#34;&#34;);
<i>numeric&#95;value<tt> = atof(<i>string&#95;value<tt>);

<p class="tent">or by converting the initial portion of the string to type <b>double representation as follows:
<blockquote>The input string is decomposed into two parts: an initial, possibly empty, sequence of white-space characters (as
specified by <a href="../functions/isspace.html"><i>isspace()) and a subject sequence interpreted as a floating-point
constant.
<p class="tent">The expected form of the subject sequence is an optional <tt>&#39;+&#39; or <tt>&#39;-&#39; sign, then a non-empty
sequence of digits optionally containing a radix character, then an optional exponent part. An exponent part consists of
<tt>&#39;e&#39; or <tt>&#39;E&#39;, followed by an optional sign, followed by one or more decimal digits.
<p class="tent">The sequence starting with the first digit or the radix character (whichever occurs first) is interpreted as a
floating constant of the C language, except that the radix character shall be used in place of a &lt;period&gt;, and if neither an
exponent part nor a radix character appears, a radix character is assumed to follow the last digit in the string. If the subject
sequence begins with a &lt;hyphen-minus&gt;, the value resulting from the conversion is negated.

<p class="tent">A numeric value that is exactly equal to the value of an integer (see <a href=
"../utilities/V3_chap01.html#tag_18_01_02"><i>1.1.2 Concepts Derived from the ISO C Standard) shall be converted to a
string by the equivalent of a call to the <b>sprintf function (see <a href="#tag_20_06_13_13">String Functions) with the
string <tt>&#34;%d&#34; as the <i>fmt argument and the numeric value being converted as the first and only <i>expr argument.
Any other numeric value shall be converted to a string by the equivalent of a call to the <b>sprintf function with the value of
the variable <b>CONVFMT as the <i>fmt argument and the numeric value being converted as the first and only <i>expr
argument. The result of the conversion is unspecified if the value of <b>CONVFMT is not a floating-point format specification.
This volume of POSIX.1-2024 specifies no explicit conversions between numbers and strings. An application can force an expression
to be treated as a number by adding zero to it, or can force it to be treated as a string by concatenating the null string
(<tt>&#34;&#34;) to it.
<p class="tent">A string value shall be considered a <i>numeric string if it comes from one of the following:
<ol>
<li class="tent">Field variables
<li class="tent">Input from the <i>getline() function
<li class="tent"><b>FILENAME
<li class="tent"><b>ARGV array elements
<li class="tent"><b>ENVIRON array elements
<li class="tent">Array elements created by the <i>split() function
<li class="tent">A command line variable assignment
<li class="tent">Variable assignment from another numeric string variable

<p class="tent">and an implementation-dependent condition corresponding to either case (a) or (b) below is met.
<ol type="a">
<li class="tent">After the equivalent of the following calls to functions defined by the ISO C standard,
<i>string&#95;value&#95;end would differ from <i>string&#95;value, and any characters before the terminating null character in
<i>string&#95;value&#95;end would be &lt;blank&gt; characters:
<pre>
<tt>char &#42;string&#95;value&#95;end;
setlocale(LC&#95;NUMERIC, &#34;&#34;);
numeric&#95;value = strtod (string&#95;value, &amp;string&#95;value&#95;end);

<li class="tent">After all the following conversions have been applied, the resulting string would lexically be recognized as a
<b>NUMBER token as described by the lexical conventions in <a href="#tag_20_06_13_16">Grammar:
<ul>
<li class="tent">All leading and trailing &lt;blank&gt; characters are discarded.
<li class="tent">If the first non-&lt;blank&gt; is <tt>&#39;+&#39; or <tt>&#39;-&#39;, it is discarded.
<li class="tent">Each occurrence of the radix character from the current locale is changed to a &lt;period&gt;.

In case (a) the numeric value of the <i>numeric string shall be the value that would be returned by the <a href=
"../functions/strtod.html"><i>strtod() call. In case (b) if the first non-&lt;blank&gt; is <tt>&#39;-&#39;, the numeric value
of the <i>numeric string shall be the negation of the numeric value of the recognized <b>NUMBER token; otherwise, the
numeric value of the <i>numeric string shall be the numeric value of the recognized <b>NUMBER token. Whether or not a
string is a <i>numeric string shall be relevant only in contexts where that term is used in this section.
<p class="tent">When an expression is used in a Boolean context, if it has a numeric value, a value of zero shall be treated as
false and any other value shall be treated as true. Otherwise, a string value of the null string shall be treated as false and any
other value shall be treated as true. A Boolean context shall be one of the following:
<ul>
<li class="tent">The first subexpression of a conditional expression
<li class="tent">An expression operated on by logical NOT, logical AND, or logical OR
<li class="tent">The second expression of a <b>for statement
<li class="tent">The expression of an <b>if statement
<li class="tent">The expression of the <b>while clause in either a <b>while or <b>do&#46;&#46;&#46;<b>while statement
<li class="tent">An expression used as a pattern (as in Overall Program Structure)

<p class="tent">All arithmetic shall follow the semantics of floating-point arithmetic as specified by the ISO C standard (see
<a href="../utilities/V3_chap01.html#tag_18_01_02"><i>1.1.2 Concepts Derived from the ISO C Standard).
<p class="tent">The value of the expression:
<pre>
<i>expr1<tt> ^ <i>expr2<tt>

<p class="tent">shall be equivalent to the value returned by the ISO C standard function call:
<pre>
<tt>pow(<i>expr1<tt>, <i>expr2<tt>)

<p class="tent">The expression:
<pre>
<tt>lvalue ^= <i>expr<tt>

<p class="tent">shall be equivalent to the ISO C standard expression:
<pre>
<tt>lvalue = pow(lvalue, <i>expr<tt>)

<p class="tent">except that lvalue shall be evaluated only once. The value of the expression:
<pre>
<i>expr1<tt> % <i>expr2<tt>

<p class="tent">shall be equivalent to the value returned by the ISO C standard function call:
<pre>
<tt>fmod(<i>expr1<tt>, <i>expr2<tt>)

<p class="tent">The expression:
<pre>
<tt>lvalue %= <i>expr<tt>

<p class="tent">shall be equivalent to the ISO C standard expression:
<pre>
<tt>lvalue = fmod(lvalue, <i>expr<tt>)

<p class="tent">except that lvalue shall be evaluated only once.
<p class="tent">Variables and fields shall be set by the assignment statement:
<pre>
<tt>lvalue = <i>expression<tt>

<p class="tent">and the type of <i>expression shall determine the resulting variable type. The assignment includes the
arithmetic assignments (<tt>&#34;+=&#34;, <tt>&#34;-=&#34;, <tt>&#34;&#42;=&#34;, <tt>&#34;/=&#34;, <tt>&#34;%=&#34;, <tt>&#34;^=&#34;, <tt>&#34;++&#34;,
<tt>&#34;&#45;&#45;&#34;) all of which shall produce a numeric result. The left-hand side of an assignment and the target of increment and
decrement operators can be one of a variable, an array with index, or a field selector.
<p class="tent">The <i>awk language supplies arrays that are used for storing numbers or strings. Arrays need not be declared.
They shall initially be empty, and their sizes shall change dynamically. The subscripts, or element identifiers, are strings,
providing a type of associative array capability. An array name followed by a subscript within square brackets can be used as an
lvalue and thus as an expression, as described in the grammar; see <a href="#tag_20_06_13_16">Grammar. Unsubscripted array
names can be used in only the following contexts:
<ul>
<li class="tent">A parameter in a function definition or function call
<li class="tent">The <b>NAME token following any use of the keyword <b>in as specified in the grammar (see <a href=
"#tag_20_06_13_16">Grammar); if the name used in this context is not an array name, the behavior is undefined
<li class="tent">The <b>NAME token following the keyword <b>Delete without a subscript as specified in the grammar (see
<a href="#tag_20_06_13_16">Grammar); if the name used in this context is not an array name, the behavior is undefined.

<p class="tent">A valid array <i>index shall consist of one or more &lt;comma&gt;-separated expressions, similar to the way in
which multi-dimensional arrays are indexed in some programming languages. Because <i>awk arrays are really one-dimensional,
such a &lt;comma&gt;-separated list shall be converted to a single string by concatenating the string values of the separate
expressions, each separated from the other by the value of the <b>SUBSEP variable. Thus, the following two index operations
shall be equivalent:
<pre>
<i>var<b>&#91;<i>expr1<tt>, <i>expr2<tt>, &#46;&#46;&#46; <i>exprn<b>&#93;
<br class="tent">
<i>var<b>&#91;<i>expr1<tt> SUBSEP <i>expr2<tt> SUBSEP &#46;&#46;&#46; SUBSEP <i>exprn<b>&#93;<tt>

<p class="tent">The application shall ensure that a multi-dimensioned <i>index used with the <b>in operator is
parenthesized. The <b>in operator, which tests for the existence of a particular array element, shall not cause that element to
exist. Any other reference to a nonexistent array element shall automatically create it.
<p class="tent">Comparisons (with the <tt>&#39;&lt;&#39;, <tt>&#34;&lt;=&#34;, <tt>&#34;!=&#34;, <tt>&#34;==&#34;, <tt>&#39;&gt;&#39;, and
<tt>&#34;&gt;=&#34; operators) shall be made numerically:
<ul>
<li class="tent">if both operands are numeric,
<li class="tent">if one is numeric and the other has a string value that is a numeric string,
<li class="tent">if both have string values that are numeric strings, or
<li class="tent">if one is numeric and the other has the uninitialized value.

<p class="tent">Otherwise, operands shall be converted to strings as required and a string comparison shall be made as follows:
<ul>
<li class="tent">For the <tt>&#34;!=&#34; and <tt>&#34;==&#34; operators, the strings shall be compared to check if they are identical
(not to check if they collate equally).
<li class="tent">For the other operators, the strings shall be compared using the locale-specific collation sequence.

<p class="tent">The value of the comparison expression shall be 1 if the relation is true, or 0 if the relation is false.
<h5><a name="tag_20_06_13_03" id="tag_20_06_13_03">Variables and Special Variables
<p class="tent">Variables can be used in an <i>awk program by referencing them. With the exception of function parameters (see
<a href="#tag_20_06_13_15">User-Defined Functions), they are not explicitly declared. Function parameter names shall be local
to the function; all other variable names shall be global. The same name shall not be used as both a function parameter name and as
the name of a function or a special <i>awk variable. The same name shall not be used both as a variable name with global scope
and as the name of a function. The same name shall not be used within the same scope both as a scalar variable and as an array.
Uninitialized variables, including scalar variables, array elements, and field variables, shall have an uninitialized value. An
uninitialized value shall have both a numeric value of zero and a string value of the empty string. Evaluation of variables with an
uninitialized value, to either string or numeric, shall be determined by the context in which they are used.
<p class="tent">Field variables shall be designated by a <tt>&#39;&#36;&#39; followed by a number or numerical expression. The effect of
the field number <i>expression evaluating to anything other than a non-negative integer is unspecified; uninitialized variables
or string values need not be converted to numeric values in this context. New field variables can be created by assigning a value
to them. References to nonexistent fields (that is, fields after &#36;<b>NF), shall evaluate to the uninitialized value. Such
references shall not create new fields. However, assigning to a nonexistent field (for example, &#36;(<b>NF+2)=5) shall increase
the value of <b>NF; create any intervening fields with the uninitialized value; and cause the value of &#36;0 to be recomputed,
with the fields being separated by the value of <b>OFS. Each field variable shall have a string value or an uninitialized value
when created. Field variables shall have the uninitialized value when created from &#36;0 using <b>FS and the variable does not
contain any characters. If appropriate, the field variable shall be considered a numeric string (see <a href=
"#tag_20_06_13_02">Expressions in awk).
<p class="tent">Implementations shall support the following other special variables that are set by <i>awk:
<dl compact>
<dd>
<dt><b>ARGC
<dd>A number determining when the iteration described for <b>ARGV stops. When an <i>awk program starts, <b>ARGC shall
be initialized to the number of elements in the <b>ARGV array. <b>ARGC can be updated by the <i>awk program and by
assignment operands. If <b>ARGC is set to a value less than 1, the behavior is unspecified. It is unspecified whether
alterations to <b>ARGC can be made using the <b>-v option.
<dt><b>ARGV
<dd>An array containing, initially, the command name (see <a href="../utilities/V3_chap02.html#tag_19_09_01"><i>2.9.1 Simple
Commands) used to invoke <i>awk in <tt>ARGV&#91;0&#93; and the command line arguments, if any, excluding options and the
<i>program operand, in <tt>ARGV&#91;1&#93; through <tt>ARGV&#91;ARGC-1&#93;. The elements in <b>ARGV can be assigned new values
or deleted, and new elements can be added. Note that alterations to <b>ARGV cannot be made using either the <i>assignment
operand or the <b>-v option, because an operand with a <tt>&#39;&#91;&#39; before <tt>&#39;=&#39; is treated as a <i>file operand,
not an <i>assignment operand, and applications are required to ensure that the <b>-v option-argument has the same form as
an <i>assignment operand. (See the OPTIONS and OPERANDS sections.)
<p class="tent">After processing the <b>BEGIN actions, if any, <i>awk begins interating over the elements of <b>ARGV,
processing them as if they were <i>argument operands. It shall behave as if the implementation maintains an internal counter
that is initialized to 1 and increments by 1 at the end of each iteration. For each iteration, the following shall occur:
<ul>
<li class="tent">If the internal counter is greater than or equal to the current value of <b>ARGC and no <i>file operands
have been processed, <i>awk shall set <b>FILENAME to <tt>&#39;-&#39; and process standard input as if it was given as a file
operand. The internal counter shall not be incremented at the end of this iteration.
<li class="tent">Otherwise, if the internal counter is greater than or equal to the current value of <b>ARGC, the iterations
shall stop and processing of the <b>END actions, if any, shall begin. Any <b>ARGV elements with index values greater than
or equal to <b>ARGC shall not be processed as <i>argument operands.
<li class="tent">Otherwise, if the element <tt>ARGV&#91; <i>internal counter value<tt>&#93; does not exist, it is unspecified
whether that element is created. No other action shall be taken.
<li class="tent">Otherwise, if <tt>ARGV&#91; <i>internal counter value<tt>&#93; is a null string, no action shall be
taken.
<li class="tent">Otherwise, if <tt>ARGV&#91; <i>internal counter value<tt>&#93; matches the format of an <i>assignment
operand (see OPERANDS), <i>awk shall process the assignment.
<li class="tent">Otherwise, <tt>ARGV&#91; <i>internal counter value<tt>&#93; shall be treated as a <i>file operand,
<b>FILENAME shall be set to that value, and the named file, or standard input if the value is <tt>&#39;-&#39;, shall be processed
as an input file.

<p class="tent">Since only non-null elements are processed, setting an element of <b>ARGV to the null string or deleting it
means that it shall not be treated as an <i>argument operand.

<dt><b>CONVFMT
<dd>The <b>printf format for converting numbers to strings (except for output statements, where <b>OFMT is used);
<tt>&#34;%.6g&#34; by default.
<dt><b>ENVIRON
<dd>An array representing the value of the environment, as described in the <i>exec functions defined in the System Interfaces
volume of POSIX.1-2024. The indices of the array shall be strings consisting of the names of the environment variables, and the
value of each array element shall be a string consisting of the value of that variable. If appropriate, the environment variable
shall be considered a <i>numeric string (see <a href="#tag_20_06_13_02">Expressions in awk); the array element shall also
have its numeric value.
<p class="tent">In all cases where the behavior of <i>awk is affected by environment variables (including the environment of
any commands that <i>awk executes via the <b>system function or via pipeline redirections with the <b>print statement,
the <b>printf statement, or the <b>getline function), the environment used shall be the environment at the time <i>awk
began executing; it is implementation-defined whether any modification of <b>ENVIRON affects this environment.

<dt><b>FILENAME
<dd>The pathname used to open the current input file, or <tt>&#39;-&#39; if the file is standard input. Inside a <b>BEGIN action
<b>FILENAME shall be unset. Inside an <b>END action the value shall be the name of the last input file processed. If an
application changes the value of <b>FILENAME, the results are unspecified.
<dt><b>FNR
<dd>The ordinal number of the current record in the current file. Inside a <b>BEGIN action the value shall be zero. Inside an
<b>END action the value shall be the number of the last record processed in the last file processed.
<dt><b>FS
<dd>Input field separator regular expression; a &lt;space&gt; by default.
<dt><b>NF
<dd>The number of fields in the current record. Inside a <b>BEGIN action, the use of <b>NF is undefined unless a
<b>getline function without a <i>var argument is executed previously. Inside an <b>END action, <b>NF shall retain
the value it had for the last record read, unless a subsequent, redirected, <b>getline function without a <i>var argument
is performed prior to entering the <b>END action.
<dt><b>NR
<dd>The ordinal number of the current record from the start of input. Inside a <b>BEGIN action the value shall be zero. Inside
an <b>END action the value shall be the number of the last record processed. Records skipped by the <b>nextfile statement
shall not be included.
<dt><b>OFMT
<dd>The <b>printf format for converting numbers to strings in output statements (see <a href="#tag_20_06_13_10">Output
Statements); <tt>&#34;%.6g&#34; by default. The result of the conversion is unspecified if the value of <b>OFMT is not a
floating-point format specification.
<dt><b>OFS
<dd>The <b>print statement output field separator; &lt;space&gt; by default.
<dt><b>ORS
<dd>The <b>print statement output record separator; a &lt;newline&gt; by default.
<dt><b>RLENGTH
<dd>The length of the string matched by the <b>match function.
<dt><b>RS
<dd>The first character of the string value of <b>RS shall be the input record separator; a &lt;newline&gt; by default. If
<b>RS contains more than one character, the results are unspecified. If <b>RS is null, then records are separated by
sequences consisting of a &lt;newline&gt; plus one or more blank lines, leading or trailing blank lines shall not result in empty
records at the beginning or end of the input, and a &lt;newline&gt; shall always be a field separator, no matter what the value of
<b>FS is.
<dt><b>RSTART
<dd>The starting position of the string matched by the <b>match function, numbering from 1. This shall always be equivalent to
the return value of the <b>match function.
<dt><b>SUBSEP
<dd>The subscript separator string for multi-dimensional arrays; the default value is implementation-defined.

<h5><a name="tag_20_06_13_04" id="tag_20_06_13_04">Regular Expressions
<p class="tent">The <i>awk utility shall make use of the extended regular expression notation (see XBD <a href=
"../basedefs/V1_chap09.html#tag_09_04"><i>9.4 Extended Regular Expressions) except that it shall allow the use of
C-language conventions for escaping special characters within the EREs, as specified in the table in XBD <a href=
"../basedefs/V1_chap05.html#tag_05"><i>5. File Format Notation for <tt>&#39;&#92;&#92;&#39;, <tt>&#39;&#92;a&#39;, <tt>&#39;&#92;b&#39;,
<tt>&#39;&#92;f&#39;, <tt>&#39;&#92;n&#39;, <tt>&#39;&#92;r&#39;, <tt>&#39;&#92;t&#39;, <tt>&#39;&#92;v&#39; and in the following table for other sequences; these
escape sequences shall be recognized both inside and outside bracket expressions. Note that records need not be separated by
&lt;newline&gt; characters and string constants can contain &lt;newline&gt; characters, so even the <tt>&#34;&#92;n&#34; sequence is valid
in <i>awk EREs. Using a &lt;slash&gt; character within the lexical token <b>ERE (except as one of the two delimiters)
requires the escaping shown in the following table.<br>
<p class="caption"><a name="tagtcjh_15" id="tagtcjh_15"> Table: Escape Sequences in awk
<center>
<table border="1" cellpadding="3" align="center">
<tr valign="top">
<th align="center">
<p class="tent"><b>Escape Sequence

<th align="center">
<p class="tent"><b>Description

<th align="center">
<p class="tent"><b>Meaning

<tr valign="top">
<td align="left">
<p class="tent">&#92;&#34;

<td align="left">
<p class="tent">&lt;backslash&gt; &lt;quotation-mark&gt;

<td align="left">
<p class="tent">In the lexical token <b>STRING, &lt;quotation-mark&gt; character. Otherwise undefined.

<tr valign="top">
<td align="left">
<p class="tent">&#92;/

<td align="left">
<p class="tent">&lt;backslash&gt; &lt;slash&gt;

<td align="left">
<p class="tent">In the lexical token <b>ERE, &lt;slash&gt; character. Otherwise undefined.

<tr valign="top">
<td align="left">
<p class="tent">&#92;ddd

<td align="left">
<p class="tent">A &lt;backslash&gt; character followed by the longest sequence of one, two, or three octal-digit characters
(01234567). If all of the digits are 0 (that is, representation of the NUL character), the behavior is undefined. If the digits
produce a value greater than octal 377, the behavior is undefined.

<td align="left">
<p class="tent">The character whose encoding is represented by the one, two, or three-digit octal integer. Multi-byte characters
require multiple, concatenated escape sequences of this type, including the leading &lt;backslash&gt; for each byte.

<tr valign="top">
<td align="left">
<p class="tent">&#92;., &#92;&#91;, &#92;(,&#92;&#42;, &#92;+, &#92;?, &#92;{, &#92;|, &#92;^, &#92;&#36;

<td align="left">
<p class="tent">A &lt;backslash&gt; character followed by a character that has a special meaning in EREs (see XBD <a href=
"../basedefs/V1_chap09.html#tag_09_04"><i>9.4 Extended Regular Expressions), other than &lt;backslash&gt;.

<td align="left">
<p class="tent">In the lexical token <b>ERE when not inside a bracket expression, the sequence shall represent itself.
Otherwise undefined.

<tr valign="top">
<td align="left">
<p class="tent">&#92;&#92;

<td align="left">
<p class="tent">Two &lt;backslash&gt; characters.

<td align="left">
<p class="tent">In the lexical token <b>ERE, the sequence shall represent itself. In the lexical token <b>STRING, it shall
represent a single &lt;backslash&gt;.

<tr valign="top">
<td align="left">
<p class="tent">&#92;c

<td align="left">
<p class="tent">A &lt;backslash&gt; character followed by any character not described in this table or in the table in XBD <a href=
"../basedefs/V1_chap05.html#tag_05"><i>5. File Format Notation (<tt>&#39;&#92;&#92;&#39;, <tt>&#39;&#92;a&#39;, <tt>&#39;&#92;b&#39;, <tt>&#39;&#92;f&#39;,
<tt>&#39;&#92;n&#39;, <tt>&#39;&#92;r&#39;, <tt>&#39;&#92;t&#39;, <tt>&#39;&#92;v&#39;).

<td align="left">
<p class="tent">Undefined

<p class="tent">A regular expression can be matched against a specific field or string by using one of the two regular expression
matching operators, <tt>&#39;~&#39; and <tt>&#34;!~&#34;. These operators shall interpret their right-hand operand as a regular
expression and their left-hand operand as a string. If the regular expression matches the string, the <tt>&#39;~&#39; expression shall
evaluate to a value of 1, and the <tt>&#34;!~&#34; expression shall evaluate to a value of 0. (The regular expression matching
operation is as defined by the term matched in XBD <a href="../basedefs/V1_chap09.html#tag_09_01"><i>9.1 Regular Expression
Definitions, where a match occurs on any part of the string unless the regular expression is limited with the
&lt;circumflex&gt; or &lt;dollar-sign&gt; special characters.) If the regular expression does not match the string, the
<tt>&#39;~&#39; expression shall evaluate to a value of 0, and the <tt>&#34;!~&#34; expression shall evaluate to a value of 1. If the
right-hand operand is any expression other than the lexical token <b>ERE, the string value of the expression shall be
interpreted as an extended regular expression, including the escape conventions described above. Note that these escape conventions
shall also be applied in determining the value of a string literal (the lexical token <b>STRING), and thus shall be applied a
second time when a string literal is used in this context.
<p class="tent">When an <b>ERE token appears as an expression in any context other than as the right-hand of the <tt>&#39;~&#39;
or <tt>&#34;!~&#34; operator or as one of the built-in function arguments described below, the value of the resulting expression shall
be the equivalent of:
<pre>
<tt>&#36;0 ~ /<i>ere<tt>/

<p class="tent">The <i>ere argument to the <b>gsub, <b>match, <b>sub functions, and the <i>fs argument to the
<b>split function (see <a href="#tag_20_06_13_13">String Functions) shall be interpreted as extended regular expressions.
These can be either <b>ERE tokens or arbitrary expressions, and shall be interpreted in the same manner as the right-hand side
of the <tt>&#39;~&#39; or <tt>&#34;!~&#34; operator.
<p class="tent">An extended regular expression can be used to separate fields by assigning a string containing the expression to
the built-in variable <b>FS, either directly or as a consequence of using the <b>-F <i>sepstring option. The default
value of the <b>FS variable shall be a single &lt;space&gt;. The following describes <b>FS behavior:
<ol>
<li class="tent">If <b>FS is a null string, the behavior is unspecified.
<li class="tent">If <b>FS is a single character:
<ol type="a">
<li class="tent">If <b>FS is &lt;space&gt;, skip leading and trailing &lt;blank&gt; and &lt;newline&gt; characters; fields
shall be delimited by sets of one or more &lt;blank&gt; or &lt;newline&gt; characters.
<li class="tent">Otherwise, if <b>FS is any other character <i>c, fields shall be delimited by each single occurrence of
<i>c.

<li class="tent">Otherwise, the string value of <b>FS shall be considered to be an extended regular expression. Each occurrence
of a sequence of one or more characters matching the extended regular expression shall delimit fields.

<p class="tent">When ERE matching is performed against input records; that is, the match is against &#36;0 and the current value of &#36;0
resulted from processing an input record, record separator characters (the first character of the value of the variable <b>RS,
&lt;newline&gt; by default) cannot be embedded in the expression, and no expression shall match the record separator character. If
the record separator is not &lt;newline&gt;, &lt;newline&gt; characters embedded in the expression can be matched. When ERE
matching is not performed against input records, it shall be based on text strings; any character (including &lt;newline&gt; and
the record separator) can be embedded in the pattern, and an appropriate pattern shall match any character. However, in all
<i>awk ERE matching, the use of one or more NUL characters in the pattern, input record, or text string produces undefined
results.
<h5><a name="tag_20_06_13_05" id="tag_20_06_13_05">Patterns
<p class="tent">A <i>pattern is any valid <i>expression, a range specified by two expressions separated by a comma, or one
of the two special patterns <b>BEGIN or <b>END.
<h5><a name="tag_20_06_13_06" id="tag_20_06_13_06">Special Patterns
<p class="tent">The <i>awk utility shall recognize two special patterns, <b>BEGIN and <b>END. Each <b>BEGIN pattern
shall be matched once and its associated action executed before the first record of input is read—except possibly by use of the
<b>getline function (see <a href="#tag_20_06_13_14">Input/Output and General Functions) in a prior <b>BEGIN action—and
before command line assignment is done. Each <b>END pattern shall be matched once and its associated action executed after the
last record of input has been read, or if there is no further input file to process following a <b>nextfile statement. These
two patterns shall have associated actions.
<p class="tent"><b>BEGIN and <b>END shall not combine with other patterns. Multiple <b>BEGIN and <b>END patterns
shall be allowed. The actions associated with the <b>BEGIN patterns shall be executed in the order specified in the program, as
are the <b>END actions. An <b>END pattern can precede a <b>BEGIN pattern in a program.
<p class="tent">If an <i>awk program consists of only actions with the pattern <b>BEGIN, and the <b>BEGIN action
contains no <b>getline function, <i>awk shall exit without reading its input when the last statement in the last
<b>BEGIN action is executed. If an <i>awk program consists of only actions with the pattern <b>END or only actions with
the patterns <b>BEGIN and <b>END, the input shall be read before the statements in the <b>END actions are executed.
<h5><a name="tag_20_06_13_07" id="tag_20_06_13_07">Expression Patterns
<p class="tent">An expression pattern shall be evaluated as if it were an expression in a Boolean context. If the result is true,
the pattern shall be considered to match, and the associated action (if any) shall be executed. If the result is false, the action
shall not be executed.
<h5><a name="tag_20_06_13_08" id="tag_20_06_13_08">Pattern Ranges
<p class="tent">A pattern range consists of two expressions separated by a comma; in this case, the action shall be performed for
all records between a match of the first expression and the following match of the second expression, inclusive. At this point, the
pattern range can be repeated starting at input records subsequent to the end of the matched range.
<h5><a name="tag_20_06_13_09" id="tag_20_06_13_09">Actions
<p class="tent">An action is a sequence of statements as shown in the grammar in <a href="#tag_20_06_13_16">Grammar. Any
single statement can be replaced by a statement list enclosed in curly braces. The application shall ensure that statements in a
statement list are separated by &lt;newline&gt; or &lt;semicolon&gt; characters. Statements in a statement list shall be executed
sequentially in the order that they appear.
<p class="tent">The <i>expression acting as the conditional in an <b>if statement shall be evaluated and if it is non-zero
or non-null, the following statement shall be executed; otherwise, if <b>else is present, the statement following the
<b>else shall be executed.
<p class="tent">The <b>if, <b>while, <b>do&#46;&#46;&#46;<b>while, <b>for, <b>break, and <b>continue statements are
based on the ISO C standard (see <a href="../utilities/V3_chap01.html#tag_18_01_02"><i>1.1.2 Concepts Derived from the ISO C
Standard), except that the Boolean expressions shall be treated as described in <a href="#tag_20_06_13_02">Expressions in
awk, and except in the case of:
<pre>
<tt>for (<i>variable<tt> in <i>array<tt>)

<p class="tent">which shall iterate, assigning each <i>index of <i>array to <i>variable in an unspecified order. The
results of adding new elements to <i>array within such a <b>for loop are undefined. If a <b>break or <b>continue
statement occurs outside of a loop, the behavior is undefined.
<p class="tent">The <b>delete statement shall remove either a specified individual array element or, if no element is
specified, all array elements. Thus, the following code:
<pre>
<tt>for (index in array)
    delete array&#91;index&#93;

<p class="tent">is equivalent to:
<pre>
<tt>delete array

<p class="tent">Both delete all elements of the array.
<p class="tent">The <b>next statement shall cause all further processing of the current input record to be abandoned. The
behavior is undefined if a <b>next statement appears or is invoked in a <b>BEGIN or <b>END action.
<p class="tent">The <b>nextfile statement shall cause all further processing of the current input file to be abandoned. The
behavior is undefined if a <b>nextfile statement appears or is invoked in a <b>BEGIN or <b>END action, or in a
user-defined function.
<p class="tent">The <b>exit statement shall invoke all <b>END actions in the order in which they occur in the program
source and then terminate the program without reading further input. An <b>exit statement inside an <b>END action shall
terminate the program without further execution of <b>END actions. If an expression is specified in an <b>exit statement,
its numeric value shall be the exit status of <i>awk, unless subsequent errors are encountered or a subsequent <b>exit
statement with an expression is executed.
<h5><a name="tag_20_06_13_10" id="tag_20_06_13_10">Output Statements
<p class="tent">Both <b>print and <b>printf statements shall write to standard output by default. The output shall be
written to the location specified by <i>output&#95;redirection if one is supplied, as follows:
<pre>
<tt>&gt; <i>expression<tt>
&gt;&gt; <i>expression<tt>
| <i>expression<tt>

<p class="tent">In all cases, the <i>expression shall be evaluated to produce a string that is used as a pathname into which to
write (for <tt>&#39;&gt;&#39; or <tt>&#34;&gt;&gt;&#34;) or as a command to be executed (for <tt>&#39;|&#39;). Using the first two forms, if
the file of that name is not currently open, it shall be opened, creating it if necessary and using the first form, truncating the
file. The output then shall be appended to the file. As long as the file remains open, subsequent calls in which <i>expression
evaluates to the same string value shall simply append output to the file. The file remains open until the <b>close function
(see <a href="#tag_20_06_13_14">Input/Output and General Functions) is called with an expression that evaluates to the same
string value.
<p class="tent">The third form shall write output onto a stream piped to the input of a command. The stream shall be created if no
stream is currently open with the value of <i>expression as its command name. The stream created shall be equivalent to one
created by a call to the <a href="../functions/popen.html"><i>popen() function defined in the System Interfaces volume of
POSIX.1-2024 with the value of <i>expression as the <i>command argument and a value of <i>w as the <i>mode
argument. As long as the stream remains open, subsequent calls in which <i>expression evaluates to the same string value shall
write output to the existing stream. The stream shall remain open until the <b>close function (see <a href=
"#tag_20_06_13_14">Input/Output and General Functions) is called with an expression that evaluates to the same string value.
At that time, the stream shall be closed as if by a call to the <a href="../functions/pclose.html"><i>pclose() function
defined in the System Interfaces volume of POSIX.1-2024.
<p class="tent">As described in detail by the grammar in <a href="#tag_20_06_13_16">Grammar, these output statements shall
take a &lt;comma&gt;-separated list of <i>expressions referred to in the grammar by the non-terminal symbols <b>expr&#95;list,
<b>print&#95;expr&#95;list, or <b>print&#95;expr&#95;list&#95;opt. This list is referred to here as the <i>expression list, and each member
is referred to as an <i>expression argument.
<p class="tent">The <b>print statement shall write the value of each expression argument onto the indicated output stream
separated by the current output field separator (see variable <b>OFS above), and terminated by the output record separator (see
variable <b>ORS above). All expression arguments shall be taken as strings, being converted if necessary; this conversion shall
be as described in <a href="#tag_20_06_13_02">Expressions in awk, with the exception that the <b>printf format in
<b>OFMT shall be used instead of the value in <b>CONVFMT. An empty expression list shall stand for the whole input record
(&#36;0).
<p class="tent">The <b>printf statement shall produce output based on a notation similar to the File Format Notation used to
describe file formats in this volume of POSIX.1-2024 (see XBD <a href="../basedefs/V1_chap05.html#tag_05"><i>5. File Format
Notation). Output shall be produced as specified with the first <i>expression argument as the string <i>format and
subsequent <i>expression arguments as the strings <i>arg1 to <i>argn, inclusive, with the following exceptions:
<ol>
<li class="tent">The <i>format shall be an actual character string rather than a graphical representation. Therefore, it cannot
contain empty character positions. The &lt;space&gt; in the <i>format string, in any context other than a <i>flag of a
conversion specification, shall be treated as an ordinary character that is copied to the output.
<li class="tent">If the character set contains a <tt>&#39;Δ&#39; character and that character appears in the <i>format string, it
shall be treated as an ordinary character that is copied to the output.
<li class="tent">The <i>escape sequences beginning with a &lt;backslash&gt; character shall be treated as sequences of ordinary
characters that are copied to the output. Note that these same sequences shall be interpreted lexically by <i>awk when they
appear in literal strings, but they shall not be treated specially by the <b>printf statement.
<li class="tent">A <i>field width or <i>precision can be specified as the <tt>&#39;&#42;&#39; character instead of a digit string.
In this case the next argument from the expression list shall be fetched and its numeric value taken as the field width or
precision.
<li class="tent">The implementation shall not precede or follow output from the <tt>d or <tt>u conversion specifier
characters with &lt;blank&gt; characters not specified by the <i>format string.
<li class="tent">The implementation shall not precede output from the <tt>o conversion specifier character with leading zeros
not specified by the <i>format string.
<li class="tent">For the <tt>c conversion specifier character: if the argument has a numeric value, the character whose
encoding is that value shall be output. If the value is zero or is not the encoding of any character in the character set, the
behavior is undefined. If the argument does not have a numeric value, the first character of the string value shall be output; if
the string does not contain any characters, the behavior is undefined.
<li class="tent">For each conversion specification that consumes an argument, the next expression argument shall be evaluated. With
the exception of the <tt>c conversion specifier character, the value shall be converted (according to the rules specified in
<a href="#tag_20_06_13_02">Expressions in awk) to the appropriate type for the conversion specification.
<li class="tent">If there are insufficient expression arguments to satisfy all the conversion specifications in the <i>format
string, the behavior is undefined.
<li class="tent">If any character sequence in the <i>format string begins with a <tt>&#39;%&#39; character, but does not form a
valid conversion specification, the behavior is unspecified.

<p class="tent">Both <b>print and <b>printf can output at least {LINE&#95;MAX} bytes.
<h5><a name="tag_20_06_13_11" id="tag_20_06_13_11">Functions
<p class="tent">The <i>awk language has a variety of built-in functions: arithmetic, string, input/output, and general.
<p class="tent">Function parameters, if present, can be either scalars or arrays; the behavior is undefined if an array name is
passed as a parameter that the function uses as a scalar, or if a scalar expression is passed as a parameter that the function uses
as an array. Function parameters shall be passed by value if scalar and by reference if array name.
<h5><a name="tag_20_06_13_12" id="tag_20_06_13_12">Arithmetic Functions
<p class="tent">The arithmetic functions, except for <b>int, shall be based on the ISO C standard (see <a href=
"../utilities/V3_chap01.html#tag_18_01_02"><i>1.1.2 Concepts Derived from the ISO C Standard). The behavior is undefined
in cases where the ISO C standard specifies that an error be returned or that the behavior is undefined. Although the grammar
(see <a href="#tag_20_06_13_16">Grammar) permits built-in functions to appear with no arguments or parentheses, unless the
argument or parentheses are indicated as optional in the following list (by displaying them within the <tt>&#34;&#91;&#93;&#34; brackets),
such use is undefined.
<dl compact>
<dd>
<dt><b>atan2(<i>y,<i>x)
<dd>Return arctangent of <i>y/<i>x in radians in the range &#91;-ℼ,ℼ&#93;.
<dt><b>cos(<i>x)
<dd>Return cosine of <i>x, where <i>x is in radians.
<dt><b>sin(<i>x)
<dd>Return sine of <i>x, where <i>x is in radians.
<dt><b>exp(<i>x)
<dd>Return the exponential function of <i>x.
<dt><b>log(<i>x)
<dd>Return the natural logarithm of <i>x.
<dt><b>sqrt(<i>x)
<dd>Return the square root of <i>x.
<dt><b>int(<i>x)
<dd>Return the argument truncated to an integer. Truncation shall be toward 0 when <i>x&gt;0.
<dt><b>rand()
<dd>Return a floating point pseudo-random number <i>n, such that 0&lt;=<i>n&lt;1.
<dt><b>srand(<b>&#91;<i>expr<b>&#93;)
<dd>Set the seed value for <b>rand to <i>expr or use the seconds since the Epoch if <i>expr is omitted. The previous
seed value shall be returned. The behavior is unspecified if <i>expr is not an integer expression or if the value of
<i>expr is not within the range 0 through 2<sup><small>31-1 (2147483647), inclusive. The initial seed value is
unspecified if <b>rand is called without calling <b>srand first. The <b>srand function uses the argument as a seed for
a new sequence of pseudo-random numbers to be returned by subsequent calls to <b>rand. If <b>srand is then called with the
same seed value, the sequence of pseudo-random numbers shall be repeated.

<h5><a name="tag_20_06_13_13" id="tag_20_06_13_13">String Functions
<p class="tent">The string functions in the following list shall be supported. Although the grammar (see <a href=
"#tag_20_06_13_16">Grammar) permits built-in functions to appear with no arguments or parentheses, unless the argument or
parentheses are indicated as optional in the following list (by displaying them within the <tt>&#34;&#91;&#93;&#34; brackets), such use is
undefined.
<dl compact>
<dd>
<dt><b>gsub(<i>ere, <i>repl<b>&#91;, <i>in<b>&#93;)
<dd>
Behave like <b>sub (see below), except that it shall replace all occurrences of the regular expression (like the <a href=
"../utilities/ed.html"><i>ed utility global substitute) in &#36;0 or in the <i>in argument, when specified.
<dt><b>index(<i>s, <i>t)
<dd>Return the position, in characters, numbering from 1, in string <i>s where string <i>t first occurs, or zero if it does
not occur at all.
<dt><b>length&#91;(<b>&#91;<i>arg<b>&#93;)<b>&#93;
<dd>
If <i>arg is an array, return the number of elements in the array; otherwise, return the length, in characters, of <i>arg
taken as a string, or of the whole record, &#36;0, if there is no argument.
<dt><b>match(<i>s, <i>ere)
<dd>Return the position, in characters, numbering from 1, in string <i>s where the extended regular expression <i>ere
occurs, or zero if it does not occur at all. RSTART shall be set to the starting position (which is the same as the returned
value), zero if no match is found; RLENGTH shall be set to the length of the matched string, -1 if no match is found.
<dt><b>split(<i>s, <i>a<b>&#91;, <i>fs <b>&#93;)
<dd>
Split the string <i>s into array elements <i>a&#91;1&#93;, <i>a&#91;2&#93;, &#46;&#46;&#46;, <i>a&#91;<i>n&#93;, and return <i>n. All elements
of the array shall be deleted before the split is performed. The separation shall be done with the ERE <i>fs or with the field
separator <b>FS if <i>fs is not given. Each array element shall have a string value when created and, if appropriate, the
array element shall be considered a numeric string (see <a href="#tag_20_06_13_02">Expressions in awk). The effect of a null
string as the value of <i>fs is unspecified.
<dt><b>sprintf(<i>fmt, <i>expr, <i>expr, &#46;&#46;&#46;)
<dd>
Format the expressions according to the <b>printf format given by <i>fmt and return the resulting string.
<dt><b>sub(<i>ere, <i>repl<b>&#91;, <i>in <b>&#93;)
<dd>
Substitute the string <i>repl in place of the first instance of the extended regular expression <i>ERE in string <i>in
and return the number of substitutions. An &lt;ampersand&gt; (<tt>&#39;&amp;&#39;) appearing in the string <i>repl shall be
replaced by the string from <i>in that matches the ERE. An &lt;ampersand&gt; preceded with a &lt;backslash&gt; shall be
interpreted as the literal &lt;ampersand&gt; character. An occurrence of two consecutive &lt;backslash&gt; characters shall be
interpreted as just a single literal &lt;backslash&gt; character. Any other occurrence of a &lt;backslash&gt; (for example,
preceding any other character) shall be treated as a literal &lt;backslash&gt; character. Note that if <i>repl is a string
literal (the lexical token <b>STRING; see <a href="#tag_20_06_13_16">Grammar), the handling of the &lt;ampersand&gt;
character occurs after any lexical processing, including any lexical &lt;backslash&gt;-escape sequence processing. If <i>in is
specified and it is not an lvalue (see <a href="#tag_20_06_13_02">Expressions in awk), the behavior is undefined. If <i>in
is omitted, <i>awk shall use the current record (&#36;0) in its place.
<dt><b>substr(<i>s, <i>m<b>&#91;, <i>n <b>&#93;)
<dd>
Return the at most <i>n-character substring of <i>s that begins at position <i>m, numbering from 1. If <i>n is
omitted, or if <i>n specifies more characters than are left in the string, the length of the substring shall be limited by the
length of the string <i>s.
<dt><b>tolower(<i>s)
<dd>Return a string based on the string <i>s. Each character in <i>s that is an uppercase letter specified to have a
<b>tolower mapping by the <i>LC&#95;CTYPE category of the current locale shall be replaced in the returned string by the
lowercase letter specified by the mapping. Other characters in <i>s shall be unchanged in the returned string.
<dt><b>toupper(<i>s)
<dd>Return a string based on the string <i>s. Each character in <i>s that is a lowercase letter specified to have a
<b>toupper mapping by the <i>LC&#95;CTYPE category of the current locale is replaced in the returned string by the uppercase
letter specified by the mapping. Other characters in <i>s are unchanged in the returned string.

<p class="tent">All of the preceding functions that take <i>ERE as a parameter expect a pattern or a string valued expression
that is a regular expression as defined in <a href="#tag_20_06_13_04">Regular Expressions.
<h5><a name="tag_20_06_13_14" id="tag_20_06_13_14">Input/Output and General Functions
<p class="tent">The input/output and general functions are:
<dl compact>
<dd>
<dt><b>close(<i>expression)
<dd>
Close the file or pipe opened by a <b>print or <b>printf statement or a call to <b>getline with the same string-valued
<i>expression. The limit on the number of open <i>expression arguments is implementation-defined. If the close was
successful, the function shall return zero; otherwise, it shall return non-zero.
<dt><b>fflush(<b>&#91;<i>expression<b>&#93;)
<dd>
Write any unwritten data to the file or piped stream opened by a <b>print or <b>printf statement with the same
string-valued <i>expression. If no argument, or if <i>expression evaluates to the null string, then write all such data for
all such open files and piped streams, and standard output.
<p class="tent">If <b>fflush is successful, it shall return 0; otherwise, it shall return non-zero.

<dt><i>expression | <b>getline &#91;<i>var<b>&#93;
<dd>
Read a record of input from a stream piped from the output of a command. The stream shall be created if no stream is currently open
with the value of <i>expression as its command name. The stream created shall be equivalent to one created by a call to the
<a href="../functions/popen.html"><i>popen() function with the value of <i>expression as the <i>command argument
and a value of <i>r as the <i>mode argument. As long as the stream remains open, subsequent calls in which
<i>expression evaluates to the same string value shall read subsequent records from the stream. The stream shall remain open
until the <b>close function is called with an expression that evaluates to the same string value. At that time, the stream
shall be closed as if by a call to the <a href="../functions/pclose.html"><i>pclose() function. If <i>var is omitted,
&#36;0 and <b>NF shall be set; otherwise, <i>var shall be set and, if appropriate, it shall be considered a numeric string (see
<a href="#tag_20_06_13_02">Expressions in awk).
<p class="tent">The <b>getline operator can form ambiguous constructs when there are unparenthesized operators (including
concatenate) to the left of the <tt>&#39;|&#39; (to the beginning of the expression containing <b>getline). In the context of the
<tt>&#39;&#36;&#39; operator, <tt>&#39;|&#39; shall behave as if it had a lower precedence than <tt>&#39;&#36;&#39;. The result of evaluating other
operators is unspecified, and conforming applications shall parenthesize properly all such usages.

<dt><b>getline
<dd>Set &#36;0 to the next input record from the current input file. This form of <b>getline shall set the <b>NF, <b>NR,
and <b>FNR variables.
<dt><b>getline <i>var
<dd>Set variable <i>var to the next input record from the current input file and, if appropriate, <i>var shall be
considered a numeric string (see <a href="#tag_20_06_13_02">Expressions in awk). This form of <b>getline shall set the
<b>FNR and <b>NR variables.
<dt><b>getline &#91;<i>var<b>&#93; &lt; <i>expression
<dd>
Read the next record of input from a named file. The <i>expression shall be evaluated to produce a string that is used as a
pathname. If the file of that name is not currently open, it shall be opened. As long as the stream remains open, subsequent calls
in which <i>expression evaluates to the same string value shall read subsequent records from the file. The file shall remain
open until the <b>close function is called with an expression that evaluates to the same string value. If <i>var is
omitted, &#36;0 and <b>NF shall be set; otherwise, <i>var shall be set and, if appropriate, it shall be considered a numeric
string (see <a href="#tag_20_06_13_02">Expressions in awk).
<p class="tent">The <b>getline operator can form ambiguous constructs when there are unparenthesized binary operators
(including concatenate) to the right of the <tt>&#39;&lt;&#39; (up to the end of the expression containing the <b>getline). The
result of evaluating such a construct is unspecified, and conforming applications shall parenthesize properly all such usages.

<dt><b>system(<i>expression)
<dd>
Execute the command given by <i>expression in a manner equivalent to the <a href="../functions/system.html"><i>system()
function defined in the System Interfaces volume of POSIX.1-2024 and return the exit status of the command.

<p class="tent">All forms of <b>getline shall return 1 for successful input, zero for end-of-file, and -1 for an error.
<p class="tent">Where strings are used as the name of a file or pipeline, the application shall ensure that the strings are
textually identical. The terminology &#34;same string value&#34; implies that &#34;equivalent strings&#34;, even those that differ only by
&lt;space&gt; characters, represent different files.
<h5><a name="tag_20_06_13_15" id="tag_20_06_13_15">User-Defined Functions
<p class="tent">The <i>awk language also provides user-defined functions. Such functions can be defined as:
<pre>
<tt>function <i>name<tt>(<b>&#91;<i>parameter<tt>, &#46;&#46;&#46;<b>&#93;<tt>) { <i>statements<tt> }

<p class="tent">A function can be referred to anywhere in an <i>awk program; in particular, its use can precede its definition.
The scope of a function is global.
<p class="tent">The number of parameters in the function definition need not match the number of parameters in the function call.
Excess formal parameters can be used as local variables. If fewer arguments are supplied in a function call than are in the
function definition, the extra parameters that are used in the function body as scalars shall evaluate to the uninitialized value
until they are otherwise initialized, and the extra parameters that are used in the function body as arrays shall be treated as
uninitialized arrays where each element evaluates to the uninitialized value until otherwise initialized.
<p class="tent">When invoking a function, no white space can be placed between the function name and the opening parenthesis.
Function calls can be nested and recursive calls can be made upon functions. Upon return from any nested or recursive function
call, the values of all of the calling function&#39;s parameters shall be unchanged, except for array parameters passed by reference.
The <b>return statement can be used to return a value. If a <b>return statement appears outside of a function definition,
the behavior is undefined.
<p class="tent">In the function definition, &lt;newline&gt; characters shall be optional before the opening brace and after the
closing brace. Function definitions can appear anywhere in the program where a <i>pattern-action pair is allowed.
<h5><a name="tag_20_06_13_16" id="tag_20_06_13_16">Grammar
<p class="tent">The grammar in this section and the lexical conventions in the following section shall together describe the syntax
for <i>awk programs. The general conventions for this style of grammar are described in <a href=
"../utilities/V3_chap01.html#tag_18_03"><i>1.3 Grammar Conventions. A valid program can be represented as the non-terminal
symbol <i>program in the grammar. This formal syntax shall take precedence over the preceding text syntax description.
<pre>
<tt>%token NAME NUMBER STRING ERE
%token FUNC&#95;NAME   /&#42; Name followed by &#39;(&#39; without white space. &#42;/
<br class="tent">
/&#42; Keywords &#42;/
%token       Begin   End
/&#42;          &#39;BEGIN&#39; &#39;END&#39;                                &#42;/
<br class="tent">
%token       Break   Continue   Delete   Do   Else
/&#42;          &#39;break&#39; &#39;continue&#39; &#39;delete&#39; &#39;do&#39; &#39;else&#39;      &#42;/
<br class="tent">
%token       Exit   For   Function   If   In   Next
/&#42;          &#39;exit&#39; &#39;for&#39; &#39;function&#39; &#39;if&#39; &#39;in&#39; &#39;next&#39;     &#42;/
<br class="tent">
%token       Nextfile   Print   Printf   Return   While
/&#42;          &#39;nextfile&#39; &#39;print&#39; &#39;printf&#39; &#39;return&#39; &#39;while&#39; &#42;/
<br class="tent">
/&#42; Reserved function names &#42;/
%token BUILTIN&#95;FUNC&#95;NAME
            /&#42; One token for the following:
             &#42; atan2 cos sin exp log sqrt int rand srand
             &#42; gsub index length match split sprintf sub
             &#42; substr tolower toupper close fflush system
             &#42;/
%token GETLINE
            /&#42; Syntactically different from other built-ins. &#42;/
<br class="tent">
/&#42; Two-character tokens. &#42;/
%token ADD&#95;ASSIGN SUB&#95;ASSIGN MUL&#95;ASSIGN DIV&#95;ASSIGN MOD&#95;ASSIGN POW&#95;ASSIGN
/&#42;     &#39;+=&#39;       &#39;-=&#39;       &#39;&#42;=&#39;       &#39;/=&#39;       &#39;%=&#39;       &#39;^=&#39; &#42;/
<br class="tent">
%token OR   AND  NO&#95;MATCH   EQ   LE   GE   NE   INCR  DECR  APPEND
/&#42;     &#39;||&#39; &#39;&amp;&amp;&#39; &#39;!~&#39; &#39;==&#39; &#39;&lt;=&#39; &#39;&gt;=&#39; &#39;!=&#39; &#39;++&#39;  &#39;&#45;&#45;&#39;  &#39;&gt;&gt;&#39;   &#42;/
<br class="tent">
/&#42; One-character tokens. &#42;/
%token &#39;{&#39; &#39;}&#39; &#39;(&#39; &#39;)&#39; &#39;&#91;&#39; &#39;&#93;&#39; &#39;,&#39; &#39;;&#39; NEWLINE
%token &#39;+&#39; &#39;-&#39; &#39;&#42;&#39; &#39;%&#39; &#39;^&#39; &#39;!&#39; &#39;&gt;&#39; &#39;&lt;&#39; &#39;|&#39; &#39;?&#39; &#39;:&#39; &#39;~&#39; &#39;&#36;&#39; &#39;=&#39;
<br class="tent">
%start program
%%
<br class="tent">
program          : item&#95;list
                 | item&#95;list item
                 ;
<br class="tent">
item&#95;list        : /&#42; empty &#42;/
                 | item&#95;list item terminator
                 ;
<br class="tent">
item             : action
                 | pattern action
                 | normal&#95;pattern
                 | Function NAME      &#39;(&#39; param&#95;list&#95;opt &#39;)&#39;
                       newline&#95;opt action
                 | Function FUNC&#95;NAME &#39;(&#39; param&#95;list&#95;opt &#39;)&#39;
                       newline&#95;opt action
                 ;
<br class="tent">
param&#95;list&#95;opt   : /&#42; empty &#42;/
                 | param&#95;list
                 ;
<br class="tent">
param&#95;list       : NAME
                 | param&#95;list &#39;,&#39; NAME
                 ;
<br class="tent">
pattern          : normal&#95;pattern
                 | special&#95;pattern
                 ;
<br class="tent">
normal&#95;pattern   : expr
                 | expr &#39;,&#39; newline&#95;opt expr
                 ;
<br class="tent">
special&#95;pattern  : Begin
                 | End
                 ;
<br class="tent">
action           : &#39;{&#39; newline&#95;opt                             &#39;}&#39;
                 | &#39;{&#39; newline&#95;opt terminated&#95;statement&#95;list   &#39;}&#39;
                 | &#39;{&#39; newline&#95;opt unterminated&#95;statement&#95;list &#39;}&#39;
                 ;
<br class="tent">
terminator       : terminator NEWLINE
                 |            &#39;;&#39;
                 |            NEWLINE
                 ;
<br class="tent">
terminated&#95;statement&#95;list : terminated&#95;statement
                 | terminated&#95;statement&#95;list terminated&#95;statement
                 ;
<br class="tent">
unterminated&#95;statement&#95;list : unterminated&#95;statement
                 | terminated&#95;statement&#95;list unterminated&#95;statement
                 ;
<br class="tent">
terminated&#95;statement : action newline&#95;opt
                 | If &#39;(&#39; expr &#39;)&#39; newline&#95;opt terminated&#95;statement
                 | If &#39;(&#39; expr &#39;)&#39; newline&#95;opt terminated&#95;statement
                       Else newline&#95;opt terminated&#95;statement
                 | While &#39;(&#39; expr &#39;)&#39; newline&#95;opt terminated&#95;statement
                 | For &#39;(&#39; simple&#95;statement&#95;opt &#39;;&#39;
                      expr&#95;opt &#39;;&#39; simple&#95;statement&#95;opt &#39;)&#39; newline&#95;opt
                      terminated&#95;statement
                 | For &#39;(&#39; NAME In NAME &#39;)&#39; newline&#95;opt
                      terminated&#95;statement
                 | &#39;;&#39; newline&#95;opt
                 | terminatable&#95;statement NEWLINE newline&#95;opt
                 | terminatable&#95;statement &#39;;&#39;     newline&#95;opt
                 ;
<br class="tent">
unterminated&#95;statement : terminatable&#95;statement
                 | If &#39;(&#39; expr &#39;)&#39; newline&#95;opt unterminated&#95;statement
                 | If &#39;(&#39; expr &#39;)&#39; newline&#95;opt terminated&#95;statement
                      Else newline&#95;opt unterminated&#95;statement
                 | While &#39;(&#39; expr &#39;)&#39; newline&#95;opt unterminated&#95;statement
                 | For &#39;(&#39; simple&#95;statement&#95;opt &#39;;&#39;
                  expr&#95;opt &#39;;&#39; simple&#95;statement&#95;opt &#39;)&#39; newline&#95;opt
                      unterminated&#95;statement
                 | For &#39;(&#39; NAME In NAME &#39;)&#39; newline&#95;opt
                      unterminated&#95;statement
                 ;
<br class="tent">
terminatable&#95;statement : simple&#95;statement
                 | Break
                 | Continue
                 | Next
                 | Nextfile
                 | Exit expr&#95;opt
                 | Return expr&#95;opt
                 | Do newline&#95;opt terminated&#95;statement While &#39;(&#39; expr &#39;)&#39;
                 ;
<br class="tent">
simple&#95;statement&#95;opt : /&#42; empty &#42;/
                 | simple&#95;statement
                 ;
<br class="tent">
simple&#95;statement : Delete NAME &#39;&#91;&#39; expr&#95;list &#39;&#93;&#39;
                 | Delete NAME
                 | expr
                 | print&#95;statement
                 ;
<br class="tent">
print&#95;statement  : simple&#95;print&#95;statement
                 | simple&#95;print&#95;statement output&#95;redirection
                 ;
<br class="tent">
simple&#95;print&#95;statement : Print  print&#95;expr&#95;list&#95;opt
                 | Print  &#39;(&#39; multiple&#95;expr&#95;list &#39;)&#39;
                 | Printf print&#95;expr&#95;list
                 | Printf &#39;(&#39; multiple&#95;expr&#95;list &#39;)&#39;
                 ;
<br class="tent">
output&#95;redirection : &#39;&gt;&#39;    expr
                 | APPEND expr
                 | &#39;|&#39;    expr
                 ;
<br class="tent">
expr&#95;list&#95;opt    : /&#42; empty &#42;/
                 | expr&#95;list
                 ;
<br class="tent">
expr&#95;list        : expr
                 | multiple&#95;expr&#95;list
                 ;
<br class="tent">
multiple&#95;expr&#95;list : expr &#39;,&#39; newline&#95;opt expr
                 | multiple&#95;expr&#95;list &#39;,&#39; newline&#95;opt expr
                 ;
<br class="tent">
expr&#95;opt         : /&#42; empty &#42;/
                 | expr
                 ;
<br class="tent">
expr             : unary&#95;expr
                 | non&#95;unary&#95;expr
                 ;
<br class="tent">
unary&#95;expr       : &#39;+&#39; expr
                 | &#39;-&#39; expr
                 | unary&#95;expr &#39;^&#39;      expr
                 | unary&#95;expr &#39;&#42;&#39;      expr
                 | unary&#95;expr &#39;/&#39;      expr
                 | unary&#95;expr &#39;%&#39;      expr
                 | unary&#95;expr &#39;+&#39;      expr
                 | unary&#95;expr &#39;-&#39;      expr
                 | unary&#95;expr          non&#95;unary&#95;expr
                 | unary&#95;expr &#39;&lt;&#39;      expr
                 | unary&#95;expr LE       expr
                 | unary&#95;expr NE       expr
                 | unary&#95;expr EQ       expr
                 | unary&#95;expr &#39;&gt;&#39;      expr
                 | unary&#95;expr GE       expr
                 | unary&#95;expr &#39;~&#39;      expr
                 | unary&#95;expr NO&#95;MATCH expr
                 | unary&#95;expr In NAME
                 | unary&#95;expr AND newline&#95;opt expr
                 | unary&#95;expr OR  newline&#95;opt expr
                 | unary&#95;expr &#39;?&#39; expr &#39;:&#39; expr
                 | unary&#95;input&#95;function
                 ;
<br class="tent">
non&#95;unary&#95;expr   : &#39;(&#39; expr &#39;)&#39;
                 | &#39;!&#39; expr
                 | non&#95;unary&#95;expr &#39;^&#39;      expr
                 | non&#95;unary&#95;expr &#39;&#42;&#39;      expr
                 | non&#95;unary&#95;expr &#39;/&#39;      expr
                 | non&#95;unary&#95;expr &#39;%&#39;      expr
                 | non&#95;unary&#95;expr &#39;+&#39;      expr
                 | non&#95;unary&#95;expr &#39;-&#39;      expr
                 | non&#95;unary&#95;expr          non&#95;unary&#95;expr
                 | non&#95;unary&#95;expr &#39;&lt;&#39;      expr
                 | non&#95;unary&#95;expr LE       expr
                 | non&#95;unary&#95;expr NE       expr
                 | non&#95;unary&#95;expr EQ       expr
                 | non&#95;unary&#95;expr &#39;&gt;&#39;      expr
                 | non&#95;unary&#95;expr GE       expr
                 | non&#95;unary&#95;expr &#39;~&#39;      expr
                 | non&#95;unary&#95;expr NO&#95;MATCH expr
                 | non&#95;unary&#95;expr In NAME
                 | &#39;(&#39; multiple&#95;expr&#95;list &#39;)&#39; In NAME
                 | non&#95;unary&#95;expr AND newline&#95;opt expr
                 | non&#95;unary&#95;expr OR  newline&#95;opt expr
                 | non&#95;unary&#95;expr &#39;?&#39; expr &#39;:&#39; expr
                 | NUMBER
                 | STRING
                 | lvalue
                 | ERE
                 | lvalue INCR
                 | lvalue DECR
                 | INCR lvalue
                 | DECR lvalue
                 | lvalue POW&#95;ASSIGN expr
                 | lvalue MOD&#95;ASSIGN expr
                 | lvalue MUL&#95;ASSIGN expr
                 | lvalue DIV&#95;ASSIGN expr
                 | lvalue ADD&#95;ASSIGN expr
                 | lvalue SUB&#95;ASSIGN expr
                 | lvalue &#39;=&#39; expr
                 | FUNC&#95;NAME &#39;(&#39; expr&#95;list&#95;opt &#39;)&#39;
                      /&#42; no white space allowed before &#39;(&#39; &#42;/
                 | BUILTIN&#95;FUNC&#95;NAME &#39;(&#39; expr&#95;list&#95;opt &#39;)&#39;
                 | BUILTIN&#95;FUNC&#95;NAME
                 | non&#95;unary&#95;input&#95;function
                 ;
<br class="tent">
print&#95;expr&#95;list&#95;opt : /&#42; empty &#42;/
                 | print&#95;expr&#95;list
                 ;
<br class="tent">
print&#95;expr&#95;list  : print&#95;expr
                 | print&#95;expr&#95;list &#39;,&#39; newline&#95;opt print&#95;expr
                 ;
<br class="tent">
print&#95;expr       : unary&#95;print&#95;expr
                 | non&#95;unary&#95;print&#95;expr
                 ;
<br class="tent">
unary&#95;print&#95;expr : &#39;+&#39; print&#95;expr
                 | &#39;-&#39; print&#95;expr
                 | unary&#95;print&#95;expr &#39;^&#39;      print&#95;expr
                 | unary&#95;print&#95;expr &#39;&#42;&#39;      print&#95;expr
                 | unary&#95;print&#95;expr &#39;/&#39;      print&#95;expr
                 | unary&#95;print&#95;expr &#39;%&#39;      print&#95;expr
                 | unary&#95;print&#95;expr &#39;+&#39;      print&#95;expr
                 | unary&#95;print&#95;expr &#39;-&#39;      print&#95;expr
                 | unary&#95;print&#95;expr          non&#95;unary&#95;print&#95;expr
                 | unary&#95;print&#95;expr &#39;~&#39;      print&#95;expr
                 | unary&#95;print&#95;expr NO&#95;MATCH print&#95;expr
                 | unary&#95;print&#95;expr In NAME
                 | unary&#95;print&#95;expr AND newline&#95;opt print&#95;expr
                 | unary&#95;print&#95;expr OR  newline&#95;opt print&#95;expr
                 | unary&#95;print&#95;expr &#39;?&#39; print&#95;expr &#39;:&#39; print&#95;expr
                 ;
<br class="tent">
non&#95;unary&#95;print&#95;expr : &#39;(&#39; expr &#39;)&#39;
                 | &#39;!&#39; print&#95;expr
                 | non&#95;unary&#95;print&#95;expr &#39;^&#39;      print&#95;expr
                 | non&#95;unary&#95;print&#95;expr &#39;&#42;&#39;      print&#95;expr
                 | non&#95;unary&#95;print&#95;expr &#39;/&#39;      print&#95;expr
                 | non&#95;unary&#95;print&#95;expr &#39;%&#39;      print&#95;expr
                 | non&#95;unary&#95;print&#95;expr &#39;+&#39;      print&#95;expr
                 | non&#95;unary&#95;print&#95;expr &#39;-&#39;      print&#95;expr
                 | non&#95;unary&#95;print&#95;expr          non&#95;unary&#95;print&#95;expr
                 | non&#95;unary&#95;print&#95;expr &#39;~&#39;      print&#95;expr
                 | non&#95;unary&#95;print&#95;expr NO&#95;MATCH print&#95;expr
                 | non&#95;unary&#95;print&#95;expr In NAME
                 | &#39;(&#39; multiple&#95;expr&#95;list &#39;)&#39; In NAME
                 | non&#95;unary&#95;print&#95;expr AND newline&#95;opt print&#95;expr
                 | non&#95;unary&#95;print&#95;expr OR  newline&#95;opt print&#95;expr
                 | non&#95;unary&#95;print&#95;expr &#39;?&#39; print&#95;expr &#39;:&#39; print&#95;expr
                 | NUMBER
                 | STRING
                 | lvalue
                 | ERE
                 | lvalue INCR
                 | lvalue DECR
                 | INCR lvalue
                 | DECR lvalue
                 | lvalue POW&#95;ASSIGN print&#95;expr
                 | lvalue MOD&#95;ASSIGN print&#95;expr
                 | lvalue MUL&#95;ASSIGN print&#95;expr
                 | lvalue DIV&#95;ASSIGN print&#95;expr
                 | lvalue ADD&#95;ASSIGN print&#95;expr
                 | lvalue SUB&#95;ASSIGN print&#95;expr
                 | lvalue &#39;=&#39; print&#95;expr
                 | FUNC&#95;NAME &#39;(&#39; expr&#95;list&#95;opt &#39;)&#39;
                     /&#42; no white space allowed before &#39;(&#39; &#42;/
                 | BUILTIN&#95;FUNC&#95;NAME &#39;(&#39; expr&#95;list&#95;opt &#39;)&#39;
                 | BUILTIN&#95;FUNC&#95;NAME
                 ;
<br class="tent">
lvalue           : NAME
                 | NAME &#39;&#91;&#39; expr&#95;list &#39;&#93;&#39;
                 | &#39;&#36;&#39; expr
                 ;
<br class="tent">
non&#95;unary&#95;input&#95;function : simple&#95;get
                 | simple&#95;get &#39;&lt;&#39; expr
                 | non&#95;unary&#95;expr &#39;|&#39; simple&#95;get
                 ;
<br class="tent">
unary&#95;input&#95;function : unary&#95;expr &#39;|&#39; simple&#95;get
                 ;
<br class="tent">
simple&#95;get       : GETLINE
                 | GETLINE lvalue
                 ;
<br class="tent">
newline&#95;opt      : /&#42; empty &#42;/
                 | newline&#95;opt NEWLINE
                 ;

<p class="tent">This grammar has several ambiguities that shall be resolved as follows:
<ul>
<li class="tent">Operator precedence and associativity shall be as described in <a href="#tagtcjh_14">Expressions in Decreasing
Precedence in awk.
<li class="tent">In case of ambiguity, an <b>else shall be associated with the most immediately preceding <b>if that would
satisfy the grammar.
<li class="tent">In some contexts, a &lt;slash&gt; (<tt>&#39;/&#39;) that is used to surround an ERE could also be the division
operator. This shall be resolved in such a way that wherever the division operator could appear, a &lt;slash&gt; is assumed to be
the division operator. (There is no unary division operator.)

<p class="tent">Each expression in an <i>awk program shall conform to the precedence and associativity rules, even when this is
not needed to resolve an ambiguity. For example, because <tt>&#39;&#36;&#39; has higher precedence than <tt>&#39;++&#39;, the string
<tt>&#34;&#36;x++&#45;&#45;&#34; is not a valid <i>awk expression, even though it is unambiguously parsed by the grammar as
<tt>&#34;&#36;(x++)&#45;&#45;&#34;.
<p class="tent">One convention that might not be obvious from the formal grammar is where &lt;newline&gt; characters are
acceptable. There are several obvious placements such as terminating a statement, and a &lt;backslash&gt; can be used to escape
&lt;newline&gt; characters between any lexical tokens. In addition, &lt;newline&gt; characters without &lt;backslash&gt; characters
can follow a comma, an open brace, logical AND operator (<tt>&#34;&amp;&amp;&#34;), logical OR operator (<tt>&#34;||&#34;), the <b>do
keyword, the <b>else keyword, and the closing parenthesis of an <b>if, <b>for, or <b>while statement. For
example:
<pre>
<tt>{ print  &#36;1,
         &#36;2 }

<h5><a name="tag_20_06_13_17" id="tag_20_06_13_17">Lexical Conventions
<p class="tent">The lexical conventions for <i>awk programs, with respect to the preceding grammar, shall be as follows:
<ol>
<li class="tent">Except as noted, <i>awk shall recognize the longest possible token or delimiter beginning at a given
point.
<li class="tent">A comment shall consist of any characters beginning with the &lt;number-sign&gt; character and terminated by, but
excluding the next occurrence of, a &lt;newline&gt;. Comments shall have no effect, except to delimit lexical tokens.
<li class="tent">The &lt;newline&gt; shall be recognized as the token <b>NEWLINE.
<li class="tent">A &lt;backslash&gt; character immediately followed by a &lt;newline&gt; shall have no effect.
<li class="tent">The token <b>STRING shall represent a string constant. A string constant shall begin with the character
<tt>&#39;&#34;&#39;. Within a string constant, a &lt;backslash&gt; character shall be considered to begin an escape sequence as specified
in the table in XBD <a href="../basedefs/V1_chap05.html#tag_05"><i>5. File Format Notation (<tt>&#39;&#92;&#92;&#39;, <tt>&#39;&#92;a&#39;,
<tt>&#39;&#92;b&#39;, <tt>&#39;&#92;f&#39;, <tt>&#39;&#92;n&#39;, <tt>&#39;&#92;r&#39;, <tt>&#39;&#92;t&#39;, <tt>&#39;&#92;v&#39;). In addition, the escape sequences in
<a href="#tagtcjh_15">Escape Sequences in awk shall be recognized. A &lt;newline&gt; shall not occur within a string constant.
A string constant shall be terminated by the first unescaped occurrence of the character <tt>&#39;&#34;&#39; after the one that begins the
string constant. The value of the string shall be the sequence of all unescaped characters and values of escape sequences between,
but not including, the two delimiting <tt>&#39;&#34;&#39; characters.
<li class="tent">The token <b>ERE represents an extended regular expression constant. An ERE constant shall begin with the
&lt;slash&gt; character. Within an ERE constant, a &lt;backslash&gt; character shall be considered to begin an escape sequence as
specified in the table in XBD <a href="../basedefs/V1_chap05.html#tag_05"><i>5. File Format Notation. In addition, the
escape sequences in <a href="#tagtcjh_15">Escape Sequences in awk shall be recognized. The application shall ensure that a
&lt;newline&gt; does not occur within an ERE constant. An ERE constant shall be terminated by the first unescaped occurrence of the
&lt;slash&gt; character after the one that begins the ERE constant. The extended regular expression represented by the ERE constant
shall be the sequence of all unescaped characters and values of escape sequences between, but not including, the two delimiting
&lt;slash&gt; characters.
<li class="tent">A &lt;blank&gt; shall have no effect, except to delimit lexical tokens or within <b>STRING or <b>ERE
tokens.
<li class="tent">The token <b>NUMBER shall represent a numeric constant. Its form and numeric value shall either be equivalent
to the <b>decimal-floating-constant token as specified by the ISO C standard, or it shall be a sequence of decimal digits
and shall be evaluated as an integer constant in decimal. In addition, implementations may accept numeric constants with the form
and numeric value equivalent to the <b>hexadecimal-constant and <b>hexadecimal-floating-constant tokens as specified by the
ISO C standard. Note that these forms do not use the radix character from the current locale; they always use a
&lt;period&gt;.
<p class="tent">If the value is too large or too small to be representable (see <a href=
"../utilities/V3_chap01.html#tag_18_01_02"><i>1.1.2 Concepts Derived from the ISO C Standard), the behavior is
undefined.

<li class="tent">A sequence of underscores, digits, and alphabetics from the portable character set (see XBD <a href=
"../basedefs/V1_chap06.html#tag_06_01"><i>6.1 Portable Character Set), beginning with an &lt;underscore&gt; or alphabetic
character, shall be considered a word.
<li class="tent">The following words are keywords that shall be recognized as individual tokens; the name of the token is the same
as the keyword:
<table cellpadding="3">
<tr valign="top">
<td align="left">
<p class="tent"><b><br>
BEGIN<br>
break<br>
continue<br>

<td align="left">
<p class="tent"><b><br>
delete<br>
do<br>
else<br>

<td align="left">
<p class="tent"><b><br>
END<br>
exit<br>
for<br>

<td align="left">
<p class="tent"><b><br>
function<br>
getline<br>
if<br>

<td align="left">
<p class="tent"><b><br>
in<br>
next<br>
nextfile<br>

<td align="left">
<p class="tent"><b><br>
print<br>
printf<br>
return<br>

<td align="left">
<p class="tent"><b><br>
while<br>

<li class="tent">The following words are names of built-in functions and shall be recognized as the token <b>BUILTIN&#95;FUNC&#95;NAME:
<table cellpadding="3">
<tr valign="top">
<td align="left">
<p class="tent"><b><br>
atan2<br>
close<br>
cos<br>
exp<br>

<td align="left">
<p class="tent"><b><br>
fflush<br>
gsub<br>
index<br>

<td align="left">
<p class="tent"><b><br>
int<br>
length<br>
log<br>

<td align="left">
<p class="tent"><b><br>
match<br>
rand<br>
sin<br>

<td align="left">
<p class="tent"><b><br>
split<br>
sprintf<br>
sqrt<br>

<td align="left">
<p class="tent"><b><br>
srand<br>
sub<br>
substr<br>

<td align="left">
<p class="tent"><b><br>
system<br>
tolower<br>
toupper<br>

<p class="tent">The above-listed keywords and names of built-in functions are considered reserved words.

<li class="tent">The token <b>NAME shall consist of a word that is not a keyword or a name of a built-in function and is not
followed immediately (without any delimiters) by the <tt>&#39;(&#39; character.
<li class="tent">The token <b>FUNC&#95;NAME shall consist of a word that is not a keyword or a name of a built-in function,
followed immediately (without any delimiters) by the <tt>&#39;(&#39; character. The <tt>&#39;(&#39; character shall not be included as
part of the token.
<li class="tent">The following two-character sequences shall be recognized as the named tokens:
<center>
<table border="1" cellpadding="3" align="center">
<tr valign="top">
<th align="center">
<p class="tent"><b>Token Name

<th align="center">
<p class="tent"><b>Sequence

<th align="center">
<p class="tent"><b>Token Name

<th align="center">
<p class="tent"><b>Sequence

<tr valign="top">
<td align="left">
<p class="tent"><b>ADD&#95;ASSIGN

<td align="center">
<p class="tent">+=

<td align="left">
<p class="tent"><b>NO&#95;MATCH

<td align="center">
<p class="tent">!~

<tr valign="top">
<td align="left">
<p class="tent"><b>SUB&#95;ASSIGN

<td align="center">
<p class="tent">-=

<td align="left">
<p class="tent"><b>EQ

<td align="center">
<p class="tent">==

<tr valign="top">
<td align="left">
<p class="tent"><b>MUL&#95;ASSIGN

<td align="center">
<p class="tent">&#42;=

<td align="left">
<p class="tent"><b>LE

<td align="center">
<p class="tent">&lt;=

<tr valign="top">
<td align="left">
<p class="tent"><b>DIV&#95;ASSIGN

<td align="center">
<p class="tent">/=

<td align="left">
<p class="tent"><b>GE

<td align="center">
<p class="tent">&gt;=

<tr valign="top">
<td align="left">
<p class="tent"><b>MOD&#95;ASSIGN

<td align="center">
<p class="tent">%=

<td align="left">
<p class="tent"><b>NE

<td align="center">
<p class="tent">!=

<tr valign="top">
<td align="left">
<p class="tent"><b>POW&#95;ASSIGN

<td align="center">
<p class="tent">^=

<td align="left">
<p class="tent"><b>INCR

<td align="center">
<p class="tent">++

<tr valign="top">
<td align="left">
<p class="tent"><b>OR

<td align="center">
<p class="tent">||

<td align="left">
<p class="tent"><b>DECR

<td align="center">
<p class="tent">&#45;&#45;

<tr valign="top">
<td align="left">
<p class="tent"><b>AND

<td align="center">
<p class="tent">&amp;&amp;

<td align="left">
<p class="tent"><b>APPEND

<td align="center">
<p class="tent">&gt;&gt;

<li class="tent">The following single characters shall be recognized as tokens whose names are the character:
<pre>
<tt>&lt;newline&gt; { } ( ) &#91; &#93; , ; + - &#42; % ^ ! &gt; &lt; | ? : ~ &#36; =

<p class="tent">There is a lexical ambiguity between the token <b>ERE and the tokens <tt>&#39;/&#39; and <b>DIV&#95;ASSIGN. When
an input sequence begins with a &lt;slash&gt; character in any syntactic context where the token <tt>&#39;/&#39; or <b>DIV&#95;ASSIGN
could appear as the next token in a valid program, the longer of those two tokens that can be recognized shall be recognized. In
any other syntactic context where the token <b>ERE could appear as the next token in a valid program, the token <b>ERE
shall be recognized.

<h4 class="mansect"><a name="tag_20_06_14" id="tag_20_06_14">EXIT STATUS
<blockquote>
<p>The following exit values shall be returned:
<dl compact>
<dd>
<dt> 0
<dd>All input files were processed successfully.
<dt>&gt;0
<dd>An error occurred.

<p class="tent">The exit status can be altered within the program by using an <b>exit expression.

<h4 class="mansect"><a name="tag_20_06_15" id="tag_20_06_15">CONSEQUENCES OF ERRORS
<blockquote>
<p>If any <i>file operand is specified and the named file cannot be accessed, <i>awk shall write a diagnostic message to
standard error and terminate without any further action.
<p class="tent">If the program specified by either the <i>program operand or a <i>progfile operand is not a valid
<i>awk program (as specified in the EXTENDED DESCRIPTION section), the behavior is undefined.

<hr>
<div class="box"><em>The following sections are informative.
<h4 class="mansect"><a name="tag_20_06_16" id="tag_20_06_16">APPLICATION USAGE
<blockquote>
<p>Since &lt;backslash&gt; has a special meaning both in the <i>assignment option-argument to the <b>-v option and in the
<i>assignment operand, applications that need to pass strings to <i>awk without special interpretation of &lt;backslash&gt;
should not use these methods but should instead make use of the <b>ARGV or <b>ENVIRON array.
<p class="tent">The <b>index, <b>length, <b>match, and <b>substr functions should not be confused with similar
functions in the ISO C standard; the <i>awk versions deal with characters, while the ISO C standard deals with
bytes.
<p class="tent">Because the concatenation operation is represented by adjacent expressions rather than an explicit operator, it is
often necessary to use parentheses to enforce the proper evaluation precedence.
<p class="tent">When using <i>awk to process pathnames, it is recommended that LC&#95;ALL, or at least LC&#95;CTYPE and LC&#95;COLLATE, are
set to POSIX or C in the environment, since pathnames can contain byte sequences that do not form valid characters in some locales,
in which case the utility&#39;s behavior would be undefined. In the POSIX locale each byte is a valid single-byte character, and
therefore this problem is avoided.
<p class="tent">Since the <tt>&#34;==&#34; operator checks if strings are identical, not whether they collate equally, applications
needing to check whether strings collate equally can use:
<pre>
<tt>a &lt;= b &amp;&amp; a &gt;= b

<p class="tent">To specify a <i>file operand naming a file with a name containing an &lt;equals-sign&gt;, users can use
<tt>&#34;./&#34; as the first two characters of a relative file pathname that starts with an &lt;underscore&gt; or an alphabetic
character to keep the <i>file operand from being interpreted as an <i>assignment operand. Similarly, <tt>&#34;./-&#34; can be
used to access a file named <tt>&#39;-&#39; in the current directory rather than use standard input.

<h4 class="mansect"><a name="tag_20_06_17" id="tag_20_06_17">EXAMPLES
<blockquote>
<p>The <i>awk program specified in the command line is most easily specified within single-quotes (for example,
&#39;<i>program&#39;) for applications using <a href="../utilities/sh.html"><i>sh, because <i>awk programs commonly contain
characters that are special to the shell, including double-quotes. In the cases where an <i>awk program contains single-quote
characters, it is usually easiest to specify most of the program as strings within single-quotes concatenated by the shell with
quoted single-quote characters. For example:
<pre>
<tt>awk &#39;/&#39;&#92;&#39;&#39;/ { print &#34;quote:&#34;, &#36;0 }&#39;

<p class="tent">prints all lines from the standard input containing a single-quote character, prefixed with <i>quote:.
<p class="tent">The following are examples of simple <i>awk programs:
<ol>
<li class="tent">Write to the standard output all input lines for which field 3 is greater than 5:
<pre>
<tt>&#36;3 &gt; 5

<li class="tent">Write every tenth line:
<pre>
<tt>(NR % 10) == 0

<li class="tent">Write any line with a substring matching the regular expression:
<pre>
<tt>/(G|D)(2&#91;0-9&#93;&#91;&#91;:alpha:&#93;&#93;&#42;)/

<li class="tent">Print any line with a substring containing a <tt>&#39;G&#39; or <tt>&#39;D&#39;, followed by a sequence of digits and
characters. This example uses character classes <b>digit and <b>alpha to match language-independent digit and alphabetic
characters respectively:
<pre>
<tt>/(G|D)(&#91;&#91;:digit:&#93;&#91;:alpha:&#93;&#93;&#42;)/

<li class="tent">Write any line in which the second field matches the regular expression and the fourth field does not:
<pre>
<tt>&#36;2 ~ /xyz/ &amp;&amp; &#36;4 !~ /xyz/

<li class="tent">Write any line in which the second field contains a &lt;backslash&gt;:
<pre>
<tt>&#36;2 ~ /&#92;&#92;/

<li class="tent">Write any line in which the second field contains a &lt;backslash&gt;. Note that &lt;backslash&gt;-escapes are
interpreted twice; once in lexical processing of the string and once in processing the regular expression:
<pre>
<tt>&#36;2 ~ &#34;&#92;&#92;&#92;&#92;&#34;

<li class="tent">Write the second to the last and the last field in each line. Separate the fields by a &lt;colon&gt;:
<pre>
<tt>{OFS=&#34;:&#34;;print &#36;(NF-1), &#36;NF}

<li class="tent">Write the line number and number of fields in each line. The three strings representing the line number, the
&lt;colon&gt;, and the number of fields are concatenated and that string is written to standard output:
<pre>
<tt>{print NR &#34;:&#34; NF}

<li class="tent">Write lines longer than 72 characters:
<pre>
<tt>length(&#36;0) &gt; 72

<li class="tent">Write the first two fields in opposite order separated by <b>OFS:
<pre>
<tt>{ print &#36;2, &#36;1 }

<li class="tent">Same, with input fields separated by a &lt;comma&gt; or &lt;space&gt; and &lt;tab&gt; characters, or both:
<pre>
<tt>BEGIN { FS = &#34;,&#91; &#92;t&#93;&#42;|&#91; &#92;t&#93;+&#34; }
      { print &#36;2, &#36;1 }

<li class="tent">Add up the first column, print sum, and average:
<pre>
<tt>      {s += &#36;1 }
END   {print &#34;sum is &#34;, s, &#34; average is&#34;, s/NR}

<li class="tent">Write fields in reverse order, one per line (many lines out for each line in):
<pre>
<tt>{ for (i = NF; i &gt; 0; &#45;&#45;i) print &#36;i }

<li class="tent">Write all lines between occurrences of the strings <b>start and <b>stop:
<pre>
<tt>/start/, /stop/

<li class="tent">Write all lines whose first field is different from the previous one:
<pre>
<tt>&#36;1 != prev { print; prev = &#36;1 }

<li class="tent">Simulate <a href="../utilities/echo.html"><i>echo:
<pre>
<tt>BEGIN  {
        for (i = 1; i &lt; ARGC; ++i)
        printf(&#34;%s%s&#34;, ARGV&#91;i&#93;, i==ARGC-1?&#34;&#92;n&#34;:&#34; &#34;)
}

<li class="tent">Write the path prefixes contained in the <i>PATH environment variable, one per line:
<pre>
<tt>BEGIN  {
        n = split (ENVIRON&#91;&#34;PATH&#34;&#93;, path, &#34;:&#34;)
        for (i = 1; i &lt;= n; ++i)
        print path&#91;i&#93;
}

<li class="tent">If there is a file named <b>input containing page headers of the form: Page #
<p class="tent">and a file named <b>program that contains:
<pre>
<tt>/Page/   { &#36;2 = n++; }
         { print }

then the command line:
<pre>
<tt>awk -f program n=5 input

<p class="tent">prints the file <b>input, filling in page numbers starting at 5.

<h4 class="mansect"><a name="tag_20_06_18" id="tag_20_06_18">RATIONALE
<blockquote>
<p>This description is based on the new <i>awk, &#34;nawk&#34;, (see the referenced <i>The AWK Programming Language), which
introduced a number of new features to the historical <i>awk:
<ol>
<li class="tent">New keywords: <b>delete, <b>do, <b>function, <b>return
<li class="tent">New built-in functions: <b>atan2, <b>close, <b>cos, <b>gsub, <b>match, <b>rand,
<b>sin, <b>srand, <b>sub, <b>system
<li class="tent">New predefined variables: <b>FNR, <b>ARGC, <b>ARGV, <b>RSTART, <b>RLENGTH, <b>SUBSEP
<li class="tent">New expression operators: <b>?, <b>:, <b>,, <b>^
<li class="tent">The <b>FS variable and the third argument to <b>split, now treated as extended regular expressions.
<li class="tent">The operator precedence, changed to more closely match the C language. Two examples of code that operate
differently are:
<pre>
<tt>while ( n /= 10 &gt; 1) &#46;&#46;&#46;
if (!&#34;wk&#34; ~ /bwk/) &#46;&#46;&#46;

<p class="tent">Several features have been added based on newer implementations of <i>awk:
<ul>
<li class="tent">Multiple instances of <b>-f <i>progfile are permitted.
<li class="tent">The new option <b>-v <i>assignment.
<li class="tent">The new predefined variable <b>ENVIRON.
<li class="tent">New built-in functions <b>toupper and <b>tolower.
<li class="tent">More formatting capabilities are added to <b>printf to match the ISO C standard.

<p class="tent">Earlier versions of this standard required implementations to support multiple adjacent &lt;semicolon&gt;s, lines
with one or more &lt;semicolon&gt; before a rule (<i>pattern-action pairs), and lines with only &lt;semicolon&gt;(s). These are
not required by this standard and are considered poor programming practice, but can be accepted by an implementation of <i>awk
as an extension.
<p class="tent">The overall <i>awk syntax has always been based on the C language, with a few features from the shell command
language and other sources. Because of this, it is not completely compatible with any other language, which has caused confusion
for some users. It is not the intent of the standard developers to address such issues. A few relatively minor changes toward
making the language more compatible with the ISO C standard were made; most of these changes are based on similar changes in
recent implementations, as described above. There remain several C-language conventions that are not in <i>awk. One of the
notable ones is the &lt;comma&gt; operator, which is commonly used to specify multiple expressions in the C language <b>for
statement. Also, there are various places where <i>awk is more restrictive than the C language regarding the type of expression
that can be used in a given context. These limitations are due to the different features that the <i>awk language does
provide.
<p class="tent">Regular expressions in <i>awk have been extended somewhat from historical implementations to make them a pure
superset of extended regular expressions, as defined by POSIX.1-2024 (see XBD <a href="../basedefs/V1_chap09.html#tag_09_04"><i>9.4
Extended Regular Expressions). The main extensions are internationalization features and interval expressions. Historical
implementations of <i>awk have long supported &lt;backslash&gt;-escape sequences as an extension to extended regular
expressions, and this extension has been retained despite inconsistency with other utilities. The number of escape sequences
recognized in both extended regular expressions and strings has varied (generally increasing with time) among implementations. The
set specified by POSIX.1-2024 includes most sequences known to be supported by popular implementations and by the ISO C
standard. One sequence that is not supported is hexadecimal value escapes beginning with <tt>&#39;&#92;x&#39;. This would allow values
expressed in more than 9 bits to be used within <i>awk as in the ISO C standard. However, because this syntax has a
non-deterministic length, it does not permit the subsequent character to be a hexadecimal digit. This limitation can be dealt with
in the C language by the use of lexical string concatenation. In the <i>awk language, concatenation could also be a solution
for strings, but not for extended regular expressions (either lexical ERE tokens or strings used dynamically as regular
expressions). Because of this limitation, the feature has not been added to POSIX.1-2024.
<p class="tent">When a string variable is used in a context where an extended regular expression normally appears (where the
lexical token ERE is used in the grammar) the string does not contain the literal &lt;slash&gt; characters.
<p class="tent">Some versions of <i>awk allow the form:
<pre>
<tt>func name(args, &#46;&#46;&#46; ) { statements }

<p class="tent">This has been deprecated by the authors of the language, who asked that it not be specified.
<p class="tent">Historical implementations of <i>awk produce an error if a <b>next statement is executed in a <b>BEGIN
action, and cause <i>awk to terminate if a <b>next statement is executed in an <b>END action. This behavior has not
been documented, and it was not believed that it was necessary to standardize it.
<p class="tent">The specification of conversions between string and numeric values is much more detailed than in the documentation
of historical implementations or in the referenced <i>The AWK Programming Language. Although most of the behavior is designed
to be intuitive, the details are necessary to ensure compatible behavior from different implementations. This is especially
important in relational expressions since the types of the operands determine whether a string or numeric comparison is performed.
From the perspective of an application developer, it is usually sufficient to expect intuitive behavior and to force conversions
(by adding zero or concatenating a null string) when the type of an expression does not obviously match what is needed. The intent
has been to specify historical practice in almost all cases. The one exception is that, in historical implementations, variables
and constants maintain both string and numeric values after their original value is converted by any use. This means that
referencing a variable or constant can have unexpected side-effects. For example, with historical implementations the following
program:
<pre>
<tt>{
    a = &#34;+2&#34;
    b = 2
    if (NR % 2)
        c = a + b
    if (a == b)
        print &#34;numeric comparison&#34;
    else
        print &#34;string comparison&#34;
}

<p class="tent">would perform a numeric comparison (and output numeric comparison) for each odd-numbered line, but perform a string
comparison (and output string comparison) for each even-numbered line. POSIX.1-2024 ensures that comparisons will be numeric if
necessary. With historical implementations, the following program:
<pre>
<tt>BEGIN {
    OFMT = &#34;%e&#34;
    print 3.14
    OFMT = &#34;%f&#34;
    print 3.14
}

<p class="tent">would output <tt>&#34;3.140000e+00&#34; twice, because in the second <b>print statement the constant
<tt>&#34;3.14&#34; would have a string value from the previous conversion. POSIX.1-2024 requires that the output of the second
<b>print statement be <tt>&#34;3.140000&#34;. The behavior of historical implementations was seen as too unintuitive and
unpredictable.
<p class="tent">It was pointed out that with the rules contained in early drafts, the following script would print nothing:
<pre>
<tt>BEGIN {
    y&#91;1.5&#93; = 1
    OFMT = &#34;%e&#34;
    print y&#91;1.5&#93;
}

<p class="tent">Therefore, a new variable, <b>CONVFMT, was introduced. The <b>OFMT variable is now restricted to affecting
output conversions of numbers to strings and <b>CONVFMT is used for internal conversions, such as comparisons or array
indexing. The default value is the same as that for <b>OFMT, so unless a program changes <b>CONVFMT (which no historical
program would do), it will receive the historical behavior associated with internal string conversions.
<p class="tent">The POSIX <i>awk lexical and syntactic conventions are specified more formally than in other sources. Again the
intent has been to specify historical practice. One convention that may not be obvious from the formal grammar as in other verbal
descriptions is where &lt;newline&gt; characters are acceptable. There are several obvious placements such as terminating a
statement, and a &lt;backslash&gt; can be used to escape &lt;newline&gt; characters between any lexical tokens. In addition,
&lt;newline&gt; characters without &lt;backslash&gt; characters can follow a comma, an open brace, a logical AND operator
(<tt>&#34;&amp;&amp;&#34;), a logical OR operator (<tt>&#34;||&#34;), the <b>do keyword, the <b>else keyword, and the closing
parenthesis of an <b>if, <b>for, or <b>while statement. For example:
<pre>
<tt>{ print &#36;1,
        &#36;2 }

<p class="tent">The requirement that <i>awk add a trailing &lt;newline&gt; to the program argument text is to simplify the
grammar, making it match a text file in form. There is no way for an application or test suite to determine whether a literal
&lt;newline&gt; is added or whether <i>awk simply acts as if it did.
<p class="tent">POSIX.1-2024 requires several changes from historical implementations in order to support internationalization.
Probably the most subtle of these is the use of the decimal-point character, defined by the <i>LC&#95;NUMERIC category of the
locale, in representations of floating-point numbers. This locale-specific character is used in recognizing numeric input, in
converting between strings and numeric values, and in formatting output. However, regardless of locale, the &lt;period&gt;
character (the decimal-point character of the POSIX locale) is the decimal-point character recognized in processing <i>awk
programs (including assignments in command line arguments). This is essentially the same convention as the one used in the
ISO C standard. The difference is that the C language includes the <a href=
"../functions/setlocale.html"><i>setlocale() function, which permits an application to modify its locale. Because of this
capability, a C application begins executing with its locale set to the C locale, and only executes in the environment-specified
locale after an explicit call to <a href="../functions/setlocale.html"><i>setlocale(). However, adding such an elaborate
new feature to the <i>awk language was seen as inappropriate for POSIX.1-2024. It is possible to execute an <i>awk program
explicitly in any desired locale by setting the environment in the shell.
<p class="tent">The undefined behavior resulting from NULs in extended regular expressions allows future extensions for the GNU
<i>gawk program to process binary data.
<p class="tent">The behavior in the case of invalid <i>awk programs (including lexical, syntactic, and semantic errors) is
undefined because it was considered overly limiting on implementations to specify. In most cases such errors can be expected to
produce a diagnostic and a non-zero exit status. However, some implementations may choose to extend the language in ways that make
use of certain invalid constructs. Other invalid constructs might be deemed worthy of a warning, but otherwise cause some
reasonable behavior. Still other constructs may be very difficult to detect in some implementations. Also, different
implementations might detect a given error during an initial parsing of the program (before reading any input files) while others
might detect it when executing the program after reading some input. Implementors should be aware that diagnosing errors as early
as possible and producing useful diagnostics can ease debugging of applications, and thus make an implementation more usable.
<p class="tent">The unspecified behavior from using multi-character <b>RS values is to allow possible future extensions based
on extended regular expressions used for record separators. Historical implementations take the first character of the string and
ignore the others.
<p class="tent">Unspecified behavior when <a href=
"../utilities/split.html"><i>split(<i>string,<i>array,&lt;null&gt;) is used is to allow a proposed future extension
that would split up a string into an array of individual characters.
<p class="tent">In the context of the <b>getline function, equally good arguments for different precedences of the <b>| and
<b>&lt; operators can be made. Historical practice has been that:
<pre>
<tt>getline &lt; &#34;a&#34; &#34;b&#34;

<p class="tent">is parsed as:
<pre>
<tt>( getline &lt; &#34;a&#34; ) &#34;b&#34;

<p class="tent">although many would argue that the intent was that the file <b>ab should be read. However:
<pre>
<tt>getline &lt; &#34;x&#34; + 1

<p class="tent">parses as:
<pre>
<tt>getline &lt; ( &#34;x&#34; + 1 )

<p class="tent">Similar problems occur with the <b>| version of <b>getline, particularly in combination with <b>&#36;. For
example:
<pre>
<tt>&#36;&#34;echo hi&#34; | getline

<p class="tent">(This situation is particularly problematic when used in a <b>print statement, where the <b>|getline part
might be a redirection of the <b>print.)
<p class="tent">Since in most cases such constructs are not (or at least should not) be used (because they have a natural ambiguity
for which there is no conventional parsing), the meaning of these constructs has been made explicitly unspecified. (The effect is
that a conforming application that runs into the problem must parenthesize to resolve the ambiguity.) There appeared to be few if
any actual uses of such constructs.
<p class="tent">Grammars can be written that would cause an error under these circumstances. Where backwards-compatibility is not a
large consideration, implementors may wish to use such grammars.
<p class="tent">Some historical implementations have allowed some built-in functions to be called without an argument list, the
result being a default argument list chosen in some &#34;reasonable&#34; way. Use of <b>length as a synonym for <b>length(&#36;0) is
the only one of these forms that is thought to be widely known or widely used; this particular form is documented in various places
(for example, most historical <i>awk reference pages, although not in the referenced <i>The AWK Programming Language) as
legitimate practice. With this exception, default argument lists have always been undocumented and vaguely defined, and it is not
at all clear how (or if) they should be generalized to user-defined functions. They add no useful functionality and preclude
possible future extensions that might need to name functions without calling them. Not standardizing them seems the simplest
course. The standard developers considered that <b>length merited special treatment, however, since it has been documented in
the past and sees possibly substantial use in historical programs. Accordingly, this usage has been made legitimate, but
Issue 5 removed the obsolescent marking for XSI-conforming implementations and many otherwise conforming applications depend
on this feature.
<p class="tent">In <b>sub and <b>gsub, if <i>repl is a string literal (the lexical token <b>STRING), then two
consecutive &lt;backslash&gt; characters should be used in the string to ensure a single &lt;backslash&gt; will precede the
&lt;ampersand&gt; when the resultant string is passed to the function. (For example, to specify one literal &lt;ampersand&gt; in
the replacement string, use <b>gsub(<b>ERE, <tt>&#34;&#92;&#92;&amp;&#34;).)
<p class="tent">Historically, the only special character in the <i>repl argument of <b>sub and <b>gsub string functions
was the &lt;ampersand&gt; (<tt>&#39;&amp;&#39;) character and preceding it with the &lt;backslash&gt; character was used to turn off
its special meaning.
<p class="tent">The description in the ISO POSIX-2:1993 standard introduced behavior such that the &lt;backslash&gt; character
was another special character and it was unspecified whether there were any other special characters. This description introduced
several portability problems, some of which are described below, and so it has been replaced with the more historical description.
Some of the problems include:
<ul>
<li class="tent">Historically, to create the replacement string, a script could use <b>gsub(<b>ERE, <tt>&#34;&#92;&#92;&amp;&#34;),
but with the ISO POSIX-2:1993 standard wording, it was necessary to use <b>gsub(<b>ERE, <tt>&#34;&#92;&#92;&#92;&#92;&amp;&#34;). The
&lt;backslash&gt; characters are doubled here because all string literals are subject to lexical analysis, which would reduce each
pair of &lt;backslash&gt; characters to a single &lt;backslash&gt; before being passed to <b>gsub.
<li class="tent">Since it was unspecified what the special characters were, for portable scripts to guarantee that characters are
printed literally, each character had to be preceded with a &lt;backslash&gt;. (For example, a portable script had to use
<b>gsub(<b>ERE, <tt>&#34;&#92;&#92;h&#92;&#92;i&#34;) to produce a replacement string of <tt>&#34;hi&#34;.)

<p class="tent">The description for comparisons in the ISO POSIX-2:1993 standard did not properly describe historical practice
because of the way numeric strings are compared as numbers. The current rules cause the following code:
<pre>
<tt>if (0 == &#34;000&#34;)
    print &#34;strange, but true&#34;
else
    print &#34;not true&#34;

<p class="tent">to do a numeric comparison, causing the <b>if to succeed. It should be intuitively obvious that this is
incorrect behavior, and indeed, no historical implementation of <i>awk actually behaves this way.
<p class="tent">To fix this problem, the definition of <i>numeric string was enhanced to include only those values obtained
from specific circumstances (mostly external sources) where it is not possible to determine unambiguously whether the value is
intended to be a string or a numeric.
<p class="tent">Variables that are assigned to a numeric string shall also be treated as a numeric string. (For example, the notion
of a numeric string can be propagated across assignments.) In comparisons, all variables having the uninitialized value are to be
treated as a numeric operand evaluating to the numeric value zero.
<p class="tent">Uninitialized variables include all types of variables including scalars, array elements, and fields. The
definition of an uninitialized value in <a href="#tag_20_06_13_03">Variables and Special Variables is necessary to describe the
value placed on uninitialized variables and on fields that are valid (for example, <b>&lt; <b>&#36;NF) but have no characters
in them and to describe how these variables are to be used in comparisons. A valid field, such as <b>&#36;1, that has no characters
in it can be obtained from an input line of <tt>&#34;&#92;t&#92;t&#34; when <b>FS=<tt>&#39;&#92;t&#39;. Historically, the comparison
(<b>&#36;1&lt;10) was done numerically after evaluating <b>&#36;1 to the value zero.
<p class="tent">The phrase &#34;&#46;&#46;&#46; also shall have the numeric value of the numeric string&#34; was removed from several sections of the
ISO POSIX-2:1993 standard because is specifies an unnecessary implementation detail. It is not necessary for POSIX.1-2024 to
specify that these objects be assigned two different values. It is only necessary to specify that these objects may evaluate to two
different values depending on context.
<p class="tent">Historical implementations of <i>awk did not parse hexadecimal integer or floating constants like
<tt>&#34;0xa&#34; and <tt>&#34;0xap0&#34;. Due to an oversight, the 2001 through 2004 editions of this standard required support for
hexadecimal floating constants. This was due to the reference to <a href="../functions/atof.html"><i>atof(). This version
of the standard allows but does not require implementations to use <a href="../functions/atof.html"><i>atof() and includes
a description of how floating-point numbers are recognized as an alternative to match historic behavior. The intent of this change
is to allow implementations to recognize floating-point constants according to either the ISO/IEC 9899:1990 standard or
ISO/IEC 9899:1999 standard, and to allow (but not require) implementations to recognize hexadecimal integer constants.
<p class="tent">Historical implementations of <i>awk did not support floating-point infinities and NaNs in <i>numeric
strings; e.g., <tt>&#34;-INF&#34; and <tt>&#34;NaN&#34;. However, implementations that use the <a href=
"../functions/atof.html"><i>atof() or <a href="../functions/strtod.html"><i>strtod() functions to do the conversion
picked up support for these values if they used a ISO/IEC 9899:1999 standard version of the function instead of a
ISO/IEC 9899:1990 standard version. Due to an oversight, the 2001 through 2004 editions of this standard did not allow support
for infinities and NaNs, but in this revision support is allowed (but not required). This is a silent change to the behavior of
<i>awk programs; for example, in the POSIX locale the expression:
<pre>
<tt>(&#34;-INF&#34; + 0 &lt; 0)

<p class="tent">formerly had the value 0 because <tt>&#34;-INF&#34; converted to 0, but now it may have the value 0 or 1.
<p class="tent">Deleting all elements of an array one element at a time, via:
<pre>
<tt>for (index in array)
    delete array&#91;index&#93;

<p class="tent">is usually not efficient. This standard requires <tt>delete array to have the same effects, and this was
supported in most implementations as a more efficient operation. It is also possible to use <tt>split(&#34;&#34;, array) to achieve
the same effect and efficiency.

<h4 class="mansect"><a name="tag_20_06_19" id="tag_20_06_19">FUTURE DIRECTIONS
<blockquote>
<p>If this utility is directed to create a new directory entry that contains any bytes that have the encoded value of a
&lt;newline&gt; character, implementations are encouraged to treat this as an error. A future version of this standard may require
implementations to treat this as an error.
<p class="tent">A future version of this standard may require <b>srand to accept any numeric value and calculate the seed by
taking the provided value, converting it to an integer, and calculating the integer value modulo
2<sup><small><i>n where <i>n is an implementation-defined value greater than or equal to 32.
<p class="tent">A future version of this standard may require the initial seed for the <b>rand function (the seed value used if
<b>srand is not called) to be an integer between 0 and 2<sup><small><i>n-1 inclusive where <i>n is an
implementation-defined value greater than or equal to 32. Additionally, the initial seed value may be required to be a
(pseudo-)random value such that two invocations of <i>awk are unlikely to emit the same sequence of random values (unless the
seed is explicitly set to the same value via <b>srand).
<p class="tent">A future version of this standard may define a new <b>posix&#95;srand function that enables application authors to
set the seed to a (pseudo-)random value generated by the system. Alternatively, the specification of the <b>srand function may
be altered to provide some means to set the default seed value to a (pseudo-)random value.

<h4 class="mansect"><a name="tag_20_06_20" id="tag_20_06_20">SEE ALSO
<blockquote>
<p><a href="../utilities/V3_chap01.html#tag_18_03"><i>1.3 Grammar Conventions, <a href=
"../utilities/grep.html#"><i>grep, <a href="../utilities/lex.html#"><i>lex, <a href=
"../utilities/sed.html#"><i>sed
<p class="tent">XBD <a href="../basedefs/V1_chap05.html#tag_05"><i>5. File Format Notation, <a href=
"../basedefs/V1_chap06.html#tag_06_01"><i>6.1 Portable Character Set, <a href="../basedefs/V1_chap08.html#tag_08"><i>8.
Environment Variables, <a href="../basedefs/V1_chap09.html#tag_09"><i>9. Regular Expressions, <a href=
"../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines
<p class="tent">XSH <a href="../functions/atof.html#"><i>atof(), <a href=
"../functions/exec.html#tag_17_129"><i>exec, <a href="../functions/isspace.html#"><i>isspace(), <a href=
"../functions/popen.html#"><i>popen(), <a href="../functions/setlocale.html#"><i>setlocale(), <a href=
"../functions/strtod.html#"><i>strtod()

<h4 class="mansect"><a name="tag_20_06_21" id="tag_20_06_21">CHANGE HISTORY
<blockquote>
<p>First released in Issue 2.

<h4 class="mansect"><a name="tag_20_06_22" id="tag_20_06_22">Issue 5
<blockquote>
<p>The FUTURE DIRECTIONS section is added.

<h4 class="mansect"><a name="tag_20_06_23" id="tag_20_06_23">Issue 6
<blockquote>
<p>The <i>awk utility is aligned with the IEEE P1003.2b draft standard.
<p class="tent">The normative text is reworded to avoid use of the term &#34;must&#34; for application requirements.<br>
<p class="tent">IEEE PASC Interpretation 1003.2 #211 is applied, adding the sentence &#34;An occurrence of two consecutive
&lt;backslash&gt; characters shall be interpreted as just a single literal &lt;backslash&gt; character.&#34; into the description of
the <b>sub string function.

<h4 class="mansect"><a name="tag_20_06_24" id="tag_20_06_24">Issue 7
<blockquote>
<p>PASC Interpretation 1003.2-1992 #107 (SD5-XCU-ERN-73) is applied, updating the description of the <b>OFS variable.
<p class="tent">Austin Group Interpretation 1003.1-2001 #189 is applied.
<p class="tent">Austin Group Interpretation 1003.1-2001 #201 is applied, permitting implementations to support infinities and
NaNs.
<p class="tent">SD5-XCU-ERN-79 is applied, restoring the horizontal lines to <a href="#tagtcjh_14">Expressions in Decreasing
Precedence in awk, and SD5-XCU-ERN-80 is applied, changing the order of some table entries.
<p class="tent">SD5-XCU-ERN-87 is applied, updating the descriptive text of the Grammar.
<p class="tent">SD5-XCU-ERN-97 is applied, updating the SYNOPSIS.
<p class="tent">The EXTENDED DESCRIPTION is changed to make the support of hexadecimal integer and floating constants optional.
<p class="tent">POSIX.1-2008, Technical Corrigendum 1, XCU/TC1-2008/0057 &#91;224&#93;, XCU/TC1-2008/0058 &#91;454&#93;, XCU/TC1-2008/0059 &#91;224&#93;,
XCU/TC1-2008/0060 &#91;224&#93;, XCU/TC1-2008/0061 &#91;254&#93;, XCU/TC1-2008/0062 &#91;254&#93;, XCU/TC1-2008/0063 &#91;224&#93;, and XCU/TC1-2008/0064 &#91;454&#93; are
applied.
<p class="tent">POSIX.1-2008, Technical Corrigendum 2, XCU/TC2-2008/0058 &#91;584&#93;, XCU/TC2-2008/0059 &#91;963&#93;, XCU/TC2-2008/0060 &#91;226&#93;,
XCU/TC2-2008/0061 &#91;663&#93;, XCU/TC2-2008/0062 &#91;963&#93;, XCU/TC2-2008/0063 &#91;226&#93;, and XCU/TC2-2008/0064 &#91;963&#93; are applied.

<h4 class="mansect"><a name="tag_20_06_25" id="tag_20_06_25">Issue 8
<blockquote>
<p>Austin Group Defect 251 is applied, encouraging implementations to disallow the creation of filenames containing any bytes that
have the encoded value of a &lt;newline&gt; character.
<p class="tent">Austin Group Defects 544 and 1136 are applied, requiring implementations to accept the <b>delete statement with
an unsubscripted array name.
<p class="tent">Austin Group Defect 607 is applied, adding the <b>nextfile statement.
<p class="tent">Austin Group Defect 634 is applied, adding the <b>fflush function.
<p class="tent">Austin Group Defects 974 and 1451 are applied, clarifying the <b>ARGC, <b>ARGV and <b>FILENAME
variables, and adding to APPLICATION USAGE.
<p class="tent">Austin Group Defect 983 is applied, changing the descriptions of the <b>rand and <b>srand functions and the
FUTURE DIRECTIONS section.
<p class="tent">Austin Group Defect 1070 is applied, requiring the <tt>&#34;!=&#34; and <tt>&#34;==&#34; operators to perform string
comparisons by checking if the strings are identical (and not by checking if they collate equally).
<p class="tent">Austin Group Defect 1105 is applied, clarifying the requirements for &lt;backslash&gt; escaping.
<p class="tent">Austin Group Defect 1122 is applied, changing the description of <i>NLSPATH .
<p class="tent">Austin Group Defect 1198 is applied, requiring comparisons to be performed numerically when both operands have
string values that are numeric strings.
<p class="tent">Austin Group Defect 1277 is applied, clarifying that using a &lt;slash&gt; character within an ERE requires
escaping only if it is within the lexical token <b>ERE.
<p class="tent">Austin Group Defect 1320 is applied, clarifying the condition under which ERE matching is against input
records.
<p class="tent">Austin Group Defect 1395 is applied, changing the requirements for string to number conversion.
<p class="tent">Austin Group Defect 1468 is applied, clarifying the behavior when <b>FS is an ERE that can match the null
string.
<p class="tent">Austin Group Defect 1566 is applied, specifying the behavior of the <b>length function when passed an array
argument.

<div class="box"><em>End of informative text.
<hr>

