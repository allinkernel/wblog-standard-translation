<!-- 英文原文镜像：https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html -->
<body bgcolor="white">

<a name="top" id="top">
<h2><a name="tag_19" id="tag_19">2. Shell Command Language
<p>This chapter contains the definition of the Shell Command Language.
<h3><a name="tag_19_01" id="tag_19_01">2.1 Shell Introduction
<p>The shell is a command language interpreter. This chapter describes the syntax of that command language as it is used by the
<a href="../utilities/sh.html"><i>sh utility and the <a href="../functions/system.html"><i>system() and <a href=
"../functions/popen.html"><i>popen() functions defined in the System Interfaces volume of POSIX.1-2024.
<p>The shell operates according to the following general overview of operations. The specific details are included in the cited
sections of this chapter.
<ol>
<li>
<p>The shell reads its input from a file (see <a href="../utilities/sh.html"><i>sh), from the <b>-c option or from the
<a href="../functions/system.html"><i>system() and <a href="../functions/popen.html"><i>popen() functions defined
in the System Interfaces volume of POSIX.1-2024. If the first line of a file of shell commands starts with the characters
<tt>&#34;#!&#34;, the results are unspecified.

<li>
<p>The shell breaks the input into tokens: words and operators; see <a href="#tag_19_03">2.3 Token Recognition.

<li>
<p>The shell parses the input into simple commands (see <a href="#tag_19_09_01">2.9.1 Simple Commands) and compound commands
(see <a href="#tag_19_09_04">2.9.4 Compound Commands).

<li>
<p>For each word within a command, the shell processes &lt;backslash&gt;-escape sequences inside dollar-single-quotes (see <a href=
"#tag_19_02_04">2.2.4 Dollar-Single-Quotes) and then performs various word expansions (see <a href="#tag_19_06">2.6 Word
Expansions). In the case of a simple command, the results usually include a list of pathnames and fields to be treated as a
command name and arguments; see <a href="#tag_19_09">2.9 Shell Commands.

<li>
<p>The shell performs redirection (see <a href="#tag_19_07">2.7 Redirection) and removes redirection operators and their
operands from the parameter list.

<li>
<p>The shell executes a function (see <a href="#tag_19_09_05">2.9.5 Function Definition Command), built-in (see <a href=
"#tag_19_15">2.15 Special Built-In Utilities), executable file, or script, giving the names of the arguments as positional
parameters numbered 1 to <i>n, and the name of the command (or in the case of a function within a script, the name of the
script) as special parameter 0 (see <a href="#tag_19_09_01_04">2.9.1.4 Command Search and Execution).

<li>
<p>The shell optionally waits for the command to complete and collects the exit status (see <a href="#tag_19_08_02">2.8.2 Exit
Status for Commands).

<h3><a name="tag_19_02" id="tag_19_02">2.2 Quoting
<p>Quoting is used to remove the special meaning of certain characters or words to the shell. Quoting can be used to preserve the
literal meaning of the special characters in the next paragraph, prevent reserved words from being recognized as such, and prevent
parameter expansion and command substitution within here-document processing (see <a href="#tag_19_07_04">2.7.4 Here-Document
).
<p>The application shall quote the following characters if they are to represent themselves:
<pre>
<tt>|  &amp;  ;  &lt;  &gt;  (  )  &#36;  &#96;  &#92;  &#34;  &#39;  &lt;space&gt;  &lt;tab&gt;  &lt;newline&gt;

<p>and the following might need to be quoted under certain circumstances. That is, these characters are sometimes special depending
on conditions described elsewhere in this volume of POSIX.1-2024:
<pre>
<tt>&#42;  ?  &#91;  &#93;  ^  -  !  #  ~  =  %  {  ,  }

<basefont size="2">
<dl>
<dt><b>Note:
<dd>A future version of this standard may extend the conditions under which these characters are special. Therefore applications
should quote them whenever they are intended to represent themselves. This does not apply to &lt;hyphen-minus&gt; (<tt>&#39;-&#39;)
since it is in the portable filename character set.

<basefont size="3">
<p>The various quoting mechanisms are the escape character, single-quotes, double-quotes, and dollar-single-quotes. The
here-document represents another form of quoting; see <a href="#tag_19_07_04">2.7.4 Here-Document.
<h4><a name="tag_19_02_01" id="tag_19_02_01">2.2.1 Escape Character (Backslash)
<p>A &lt;backslash&gt; that is not quoted shall preserve the literal value of the following character, with the exception of a
&lt;newline&gt;. If a &lt;newline&gt; immediately follows the &lt;backslash&gt;, the shell shall interpret this as line
continuation. The &lt;backslash&gt; and &lt;newline&gt; shall be removed before splitting the input into tokens. Since the escaped
&lt;newline&gt; is removed entirely from the input and is not replaced by any white space, it cannot serve as a token
separator.
<h4><a name="tag_19_02_02" id="tag_19_02_02">2.2.2 Single-Quotes
<p>Enclosing characters in single-quotes (<tt>&#39;&#39;) shall preserve the literal value of each character within the single-quotes.
A single-quote cannot occur within single-quotes.
<h4><a name="tag_19_02_03" id="tag_19_02_03">2.2.3 Double-Quotes
<p>Enclosing characters in double-quotes (<tt>&#34;&#34;) shall preserve the literal value of all characters within the double-quotes,
with the exception of the characters backquote, &lt;dollar-sign&gt;, and &lt;backslash&gt;, as follows:
<dl compact>
<dd>
<dt><tt>&#36;
<dd>The &lt;dollar-sign&gt; shall retain its special meaning introducing parameter expansion (see <a href="#tag_19_06_02">2.6.2
Parameter Expansion), a form of command substitution (see <a href="#tag_19_06_03">2.6.3 Command Substitution), and
arithmetic expansion (see <a href="#tag_19_06_04">2.6.4 Arithmetic Expansion), but shall not retain its special meaning
introducing the dollar-single-quotes form of quoting (see <a href="#tag_19_02_04">2.2.4 Dollar-Single-Quotes).
<p>The input characters within the quoted string that are also enclosed between <tt>&#34;&#36;(&#34; and the matching <tt>&#39;)&#39; shall
not be affected by the double-quotes, but rather shall define the command(s) whose output replaces the <tt>&#34;&#36;(&#46;&#46;&#46;)&#34; when the
word is expanded. The tokenizing rules in <a href="#tag_19_03">2.3 Token Recognition shall be applied recursively to find the
matching <tt>&#39;)&#39;.
<p>For the four varieties of parameter expansion that provide for substring processing (see <a href="#tag_19_06_02">2.6.2 Parameter
Expansion), within the string of characters from an enclosed <tt>&#34;&#36;{&#34; to the matching <tt>&#39;}&#39;, the double-quotes
within which the expansion occurs shall have no effect on the handling of any special characters.
<p>For parameter expansions other than the four varieties that provide for substring processing, within the string of characters
from an enclosed <tt>&#34;&#36;{&#34; to the matching <tt>&#39;}&#39;, the double-quotes within which the expansion occurs shall preserve the
literal value of all characters, with the exception of the characters double-quote, backquote, &lt;dollar-sign&gt;, and
&lt;backslash&gt;. If any unescaped double-quote characters occur within the string, other than in embedded command substitutions,
the behavior is unspecified. The backquote and &lt;dollar-sign&gt; characters shall follow the same rules as for characters in
double-quotes described in this section. The &lt;backslash&gt; character shall follow the same rules as for characters in
double-quotes described in this section except that it shall additionally retain its special meaning as an escape character when
followed by <tt>&#39;}&#39; and this shall prevent the escaped <tt>&#39;}&#39; from being considered when determining the matching
<tt>&#39;}&#39; (using the rule in <a href="#tag_19_06_02">2.6.2 Parameter Expansion).

<dt><tt>&#96;
<dd>The backquote shall retain its special meaning introducing the other form of command substitution (see <a href=
"#tag_19_06_03">2.6.3 Command Substitution). The portion of the quoted string from the initial backquote and the characters up
to the next backquote that is not preceded by a &lt;backslash&gt;, having escape characters removed, defines that command whose
output replaces <tt>&#34;&#96;&#46;&#46;&#46;&#96;&#34; when the word is expanded. Either of the following cases produces undefined results:
<ul>
<li>
<p>A quoted (single-quoted, double-quoted, or dollar-single-quoted) string that begins, but does not end, within the
<tt>&#34;&#96;&#46;&#46;&#46;&#96;&#34; sequence

<li>
<p>A <tt>&#34;&#96;&#46;&#46;&#46;&#96;&#34; sequence that begins, but does not end, within the same double-quoted string

<dt><tt>&#92;
<dd>Outside of <tt>&#34;&#36;(&#46;&#46;&#46;)&#34; and <tt>&#34;&#36;{&#46;&#46;&#46;}&#34; the &lt;backslash&gt; shall retain its special meaning as an escape
character (see <a href="#tag_19_02_01">2.2.1 Escape Character (Backslash)) only when immediately followed by one of the
following characters:
<pre>
<tt>&#36;   &#96;   &#92;   &lt;newline&gt;

<p>or by a double-quote character that would otherwise be considered special (see <a href="#tag_19_06_04">2.6.4 Arithmetic
Expansion and <a href="#tag_19_07_04">2.7.4 Here-Document).

<p>When double-quotes are used to quote a parameter expansion, command substitution, or arithmetic expansion, the literal value of
all characters within the result of the expansion shall be preserved.
<p>The application shall ensure that a double-quote that is not within <tt>&#34;&#36;(&#46;&#46;&#46;)&#34; nor within <tt>&#34;&#36;{&#46;&#46;&#46;}&#34; is
immediately preceded by a &lt;backslash&gt; in order to be included within double-quotes. The parameter <tt>&#39;@&#39; has special
meaning inside double-quotes and is described in <a href="#tag_19_05_02">2.5.2 Special Parameters.
<h4><a name="tag_19_02_04" id="tag_19_02_04">2.2.4 Dollar-Single-Quotes
<p>A sequence of characters starting with a &lt;dollar-sign&gt; immediately followed by a single-quote (<tt>&#36;&#39;) shall preserve
the literal value of all characters up to an unescaped terminating single-quote (<tt>&#39;), with the exception of certain
&lt;backslash&gt;-escape sequences, as follows:
<ul>
<li>
<p><tt>&#92;&#34; yields a &lt;quotation-mark&gt; (double-quote) character, but note that &lt;quotation-mark&gt; can be included
unescaped.

<li>
<p><tt>&#92;&#39; yields an &lt;apostrophe&gt; (single-quote) character.

<li>
<p><tt>&#92;&#92; yields a &lt;backslash&gt; character.

<li>
<p><tt>&#92;a yields an &lt;alert&gt; character.

<li>
<p><tt>&#92;b yields a &lt;backspace&gt; character.

<li>
<p><tt>&#92;e yields an &lt;ESC&gt; character.

<li>
<p><tt>&#92;f yields a &lt;form-feed&gt; character.

<li>
<p><tt>&#92;n yields a &lt;newline&gt; character.

<li>
<p><tt>&#92;r yields a &lt;carriage-return&gt; character.

<li>
<p><tt>&#92;t yields a &lt;tab&gt; character.

<li>
<p><tt>&#92;v yields a &lt;vertical-tab&gt; character.

<li>
<p><tt>&#92;c<i>X yields the control character listed in the <b>Value column of <a href=
"../utilities/stty.html#tagtcjh_23"><i>Values for cpio c&#95;mode Field in the OPERANDS section of the <a href=
"../utilities/stty.html"><i>stty utility when <i>X is one of the characters listed in the <b>^c column of the same
table, except that <tt>&#92;c&#92;&#92; yields the &lt;FS&gt; control character since the &lt;backslash&gt; character has to be
escaped.

<li>
<p><tt>&#92;x<i>XX yields the byte whose value is the hexadecimal value <i>XX (one or more hexadecimal digits). If more
than two hexadecimal digits follow <tt>&#92;x, the results are unspecified.

<li>
<p><tt>&#92;<i>ddd yields the byte whose value is the octal value <i>ddd (one to three octal digits).

<li>
<p>The behavior of an unescaped &lt;backslash&gt; immediately followed by any other character, including &lt;newline&gt;, is
unspecified.

<p>In cases where a variable number of characters can be used to specify an escape sequence (<tt>&#92;x<i>XX and
<tt>&#92;<i>ddd), the escape sequence shall be terminated by the first character that is not of the expected type or, for
<tt>&#92;<i>ddd sequences, when the maximum number of characters specified has been found, whichever occurs first.
<p>These &lt;backslash&gt;-escape sequences shall be processed (replaced with the bytes or characters they yield) immediately prior
to word expansion (see <a href="#tag_19_06">2.6 Word Expansions) of the word in which the dollar-single-quotes sequence
occurs.
<p>If a <tt>&#92;x<i>XX or <tt>&#92;<i>ddd escape sequence yields a byte whose value is 0, it is unspecified whether that
null byte is included in the result or if that byte and any following regular characters and escape sequences up to the terminating
unescaped single-quote are evaluated and discarded.
<p>If the octal value specified by <tt>&#92;<i>ddd will not fit in a byte, the results are unspecified.
<p>If a <tt>&#92;e or <tt>&#92;c<i>X escape sequence specifies a character that does not have an encoding in the locale in
effect when these &lt;backslash&gt;-escape sequences are processed, the result is implementation-defined. However, implementations
shall not replace an unsupported character with bytes that do not form valid characters in that locale&#39;s character set.
<p>If a &lt;backslash&gt;-escape sequence represents a single-quote character (for example <tt>&#92;&#39;), that sequence shall not
terminate the dollar-single-quote sequence.
<h3><a name="tag_19_03" id="tag_19_03">2.3 Token Recognition
<p>The shell shall read its input in terms of lines. (For details about how the shell reads its input, see the description of
<a href="../utilities/sh.html#"><i>sh.) The input lines can be of unlimited length. These lines shall be parsed using two
major modes: ordinary token recognition and processing of here-documents.
<p>When an <b>io&#95;here token has been recognized by the grammar (see <a href="#tag_19_10">2.10 Shell Grammar), one or more
of the subsequent lines immediately following the next <b>NEWLINE token form the body of a here-document and shall be parsed
according to the rules of <a href="#tag_19_07_04">2.7.4 Here-Document. Any non-<b>NEWLINE tokens (including more
<b>io&#95;here tokens) that are recognized while searching for the next <b>NEWLINE token shall be saved for processing after
the here-document has been parsed. If a saved token is an <b>io&#95;here token, the corresponding here-document shall start on the
line immediately following the line containing the trailing delimiter of the previous here-document. If any saved token includes a
&lt;newline&gt; character, the behavior is unspecified.
<p>When it is not processing an <b>io&#95;here, the shell shall break its input into tokens by applying the first applicable rule
below to each character in turn in its input. At the start of input or after a previous token has just been delimited, the first or
next token, respectively, shall start with the first character that has not already been included in a token and is not discarded
according to the rules below. Once a token has started, zero or more characters from the input shall be appended to the token until
the end of the token is delimited according to one of the rules below. When both the start and end of a token have been delimited,
the characters forming the token shall be exactly those in the input between the two delimiters, including any quoting characters.
If a rule below indicates that a token is delimited, and no characters have been included in the token, that empty token shall be
discarded.
<ol>
<li>
<p>If the end of input is recognized, the current token (if any) shall be delimited.

<li>
<p>If the previous character was used as part of an operator and the current character is not quoted and can be used with the
previous characters to form an operator, it shall be used as part of that (operator) token.

<li>
<p>If the previous character was used as part of an operator and the current character cannot be used with the previous characters
to form an operator, the operator containing the previous character shall be delimited.

<li>
<p>If the current character is an unquoted &lt;backslash&gt;, single-quote, or double-quote or is the first character of an
unquoted &lt;dollar-sign&gt; single-quote sequence, it shall affect quoting for subsequent characters up to the end of the quoted
text. The rules for quoting are as described in <a href="#tag_19_02">2.2 Quoting. During token recognition no substitutions
shall be actually performed, and the result token shall contain exactly the characters that appear in the input unmodified,
including any embedded or enclosing quotes or substitution operators, between the start and the end of the quoted text. The token
shall not be delimited by the end of the quoted field.

<li>
<p>If the current character is an unquoted <tt>&#39;&#36;&#39; or <tt>&#39;&#96;&#39;, the shell shall identify the start of any candidates for
parameter expansion ( <a href="#tag_19_06_02">2.6.2 Parameter Expansion), command substitution ( <a href="#tag_19_06_03">2.6.3
Command Substitution), or arithmetic expansion ( <a href="#tag_19_06_04">2.6.4 Arithmetic Expansion) from their
introductory unquoted character sequences: <tt>&#39;&#36;&#39; or <tt>&#34;&#36;{&#34;, <tt>&#34;&#36;(&#34; or <tt>&#39;&#96;&#39;, and <tt>&#34;&#36;((&#34;,
respectively. The shell shall read sufficient input to determine the end of the unit to be expanded (as explained in the cited
sections). While processing the characters, if instances of expansions or quoting are found nested within the substitution, the
shell shall recursively process them in the manner specified for the construct that is found. For <tt>&#34;&#36;(&#34; and <tt>&#39;&#96;&#39;
only, if instances of <b>io&#95;here tokens are found nested within the substitution, they shall be parsed according to the rules
of <a href="#tag_19_07_04">2.7.4 Here-Document; if the terminating <tt>&#39;)&#39; or <tt>&#39;&#96;&#39; of the substitution occurs
before the <b>NEWLINE token marking the start of the here-document, the behavior is unspecified. The characters found from the
beginning of the substitution to its end, allowing for any recursion necessary to recognize embedded constructs, shall be included
unmodified in the result token, including any embedded or enclosing substitution operators or quotes. The token shall not be
delimited by the end of the substitution.

<li>
<p>If the current character is not quoted and can be used as the first character of a new operator, the current token (if any)
shall be delimited. The current character shall be used as the beginning of the next (operator) token.

<li>
<p>If the current character is an unquoted &lt;blank&gt;, any token containing the previous character is delimited and the current
character shall be discarded.

<li>
<p>If the previous character was part of a word, the current character shall be appended to that word.

<li>
<p>If the current character is a <tt>&#39;#&#39;, it and all subsequent characters up to, but excluding, the next &lt;newline&gt;
shall be discarded as a comment. The &lt;newline&gt; that ends the line is not considered part of the comment.

<li>
<p>The current character is used as the start of a new word.

<p>Once a token is delimited, it is categorized as required by the grammar in <a href="#tag_19_10">2.10 Shell Grammar.
<p>In situations where the shell parses its input as a <i>program, once a <i>complete&#95;command has been recognized by the
grammar (see <a href="#tag_19_10">2.10 Shell Grammar), the <i>complete&#95;command shall be executed before the next
<i>complete&#95;command is tokenized and parsed.
<h4><a name="tag_19_03_01" id="tag_19_03_01">2.3.1 Alias Substitution
<p>After a token has been categorized as type <b>TOKEN (see <a href="#tag_19_10_01">2.10.1 Shell Grammar Lexical
Conventions), including (recursively) any token resulting from an alias substitution, the <b>TOKEN shall be subject to
alias substitution if all of the following conditions are true:
<ul>
<li>
<p>The <b>TOKEN does not contain any quoting characters.

<li>
<p>The <b>TOKEN is a valid alias name (see XBD <a href="../basedefs/V1_chap03.html#tag_03_10"><i>3.10 Alias Name).

<li>
<p>An alias with that name is in effect.

<li>
<p>The <b>TOKEN did not either fully or, optionally, partially result from an alias substitution of the same alias name at any
earlier recursion level.

<li>
<p>Either the <b>TOKEN is being considered for alias substitution because it follows an alias substitution whose replacement
value ended with a &lt;blank&gt; (see below) or the <b>TOKEN could be parsed as the command name word of a simple command (see
<a href="#tag_19_10">2.10 Shell Grammar), based on this <b>TOKEN and the tokens (if any) that preceded it, but ignoring
whether any subsequent characters would allow that.

except that if the <b>TOKEN meets the above conditions and would be recognized as a reserved word (see <a href="#tag_19_04">2.4
Reserved Words) if it occurred in an appropriate place in the input, it is unspecified whether the <b>TOKEN is subject to
alias substitution.
<p>When a <b>TOKEN is subject to alias substitution, the value of the alias shall be processed as if it had been read from the
input instead of the <b>TOKEN, with token recognition (see <a href="#tag_19_03">2.3 Token Recognition) resuming at the
start of the alias value. When the end of the alias value is reached, the shell may behave as if an additional &lt;space&gt;
character had been read from the input after the <b>TOKEN that was replaced. If it does not add this &lt;space&gt;, it is
unspecified whether the current token is delimited before token recognition is applied to the character (if any) that followed the
<b>TOKEN in the input. <basefont size="2">
<dl>
<dt><b>Note:
<dd>A future version of this standard may disallow adding this &lt;space&gt;.

<basefont size="3"> If the value of the alias replacing the <b>TOKEN ends in a &lt;blank&gt; that would be unquoted after
substitution, and optionally if it ends in a &lt;blank&gt; that would be quoted after substitution, the shell shall check the next
token in the input, if it is a <b>TOKEN, for alias substitution; this process shall continue until a <b>TOKEN is found that
is not a valid alias or an alias value does not end in such a &lt;blank&gt;.
<p>An implementation may defer the effect of a change to an alias but the change shall take effect no later than the completion of
the currently executing <i>complete&#95;command (see <a href="#tag_19_10">2.10 Shell Grammar). Changes to aliases shall not
take effect out of order. Implementations may provide predefined aliases that are in effect when the shell is invoked.
<p>When used as specified by this volume of POSIX.1-2024, alias definitions shall not be inherited by separate invocations of the
shell or by the utility execution environments invoked by the shell; see <a href="#tag_19_13">2.13 Shell Execution Environment
.
<h3><a name="tag_19_04" id="tag_19_04">2.4 Reserved Words
<p>Reserved words are words that have special meaning to the shell; see <a href="#tag_19_09">2.9 Shell Commands. The following
words shall be recognized as reserved words:
<table cellpadding="3">
<tr valign="top">
<td align="left">
<p class="tent"><b><br>
!<br>
{<br>
}<br>
case<br>

<td align="left">
<p class="tent"><b><br>
do<br>
done<br>
elif<br>
else<br>

<td align="left">
<p class="tent"><b><br>
esac<br>
fi<br>
for<br>
if<br>

<td align="left">
<p class="tent"><b><br>
in<br>
then<br>
until<br>
while<br>

<p class="tent">This recognition shall only occur when none of the characters is quoted and when the word is used as:
<ul>
<li class="tent">The first word of a command
<li class="tent">The first word following one of the reserved words other than <b>case, <b>for, or <b>in
<li class="tent">The third word in a <b>case command (only <b>in is valid in this case)
<li class="tent">The third word in a <b>for command (only <b>in and <b>do are valid in this case)

<p class="tent">See the grammar in <a href="#tag_19_10">2.10 Shell Grammar.
<p class="tent">When used in circumstances where reserved words are recognized (described above), the following words may be
recognized as reserved words, in which case the results are unspecified except as described below for <b>time:
<table cellpadding="3">
<tr valign="top">
<td align="left">
<p class="tent"><b>&#91;&#91;

<td align="left">
<p class="tent"><b>&#93;&#93;

<td align="left">
<p class="tent"><b>function

<td align="left">
<p class="tent"><b>namespace

<td align="left">
<p class="tent"><b>select

<td align="left">
<p class="tent"><b>time

<p class="tent">When the word <b>time is recognized as a reserved word in circumstances where it would, if it were not a
reserved word, be the command name (see <a href="#tag_19_09_01_01">2.9.1.1 Order of Processing) of a simple command that would
execute the <a href="../utilities/time.html"><i>time utility in a manner other than one for which <a href=
"../utilities/time.html#tag_20_122"><i>time states that the results are unspecified, the behavior shall be as specified for
the <a href="../utilities/time.html"><i>time utility.
<p class="tent">When used in circumstances where reserved words are recognized (described above), all words whose final character
is a &lt;colon&gt; (<tt>&#39;:&#39;) are reserved; their use in those circumstances produces unspecified results.
<h3><a name="tag_19_05" id="tag_19_05">2.5 Parameters and Variables
<p class="tent">A parameter can be denoted by a name, a number, or one of the special characters listed in <a href=
"#tag_19_05_02">2.5.2 Special Parameters. A variable is a parameter denoted by a name.
<p class="tent">A parameter is set if it has an assigned value (null is a valid value). Once a variable is set, it can only be
unset by using the <a href="#unset"><i>unset special built-in command.
<p class="tent">Parameters can contain arbitrary byte sequences, except for the null byte. The shell shall process their values as
characters only when performing operations that are described in this standard in terms of characters.
<h4><a name="tag_19_05_01" id="tag_19_05_01">2.5.1 Positional Parameters
<p class="tent">A positional parameter is a parameter denoted by a decimal representation of a positive integer. The digits
denoting the positional parameters shall always be interpreted as a decimal value, even if there is a leading zero. When a
positional parameter with more than one digit is specified, the application shall enclose the digits in braces (see <a href=
"#tag_19_06_02">2.6.2 Parameter Expansion).
<p class="tent">Examples:
<ul>
<li class="tent"><tt>&#34;&#36;8&#34;, <tt>&#34;&#36;{8}&#34;, <tt>&#34;&#36;{08}&#34;, <tt>&#34;&#36;{008}&#34;, etc. all expand to the value of the eighth
positional parameter.
<li class="tent"><tt>&#34;&#36;{10}&#34; expands to the value of the tenth positional parameter.
<li class="tent"><tt>&#34;&#36;10&#34; expands to the value of the first positional parameter followed by the character &#39;0&#39;.

<basefont size="2">
<dl>
<dt><b>Note:
<dd>0 is a special parameter, not a positional parameter, and therefore the results of expanding <tt>&#36;{00} are
unspecified.

<basefont size="3">
<p class="tent">Positional parameters are initially assigned when the shell is invoked (see <a href=
"../utilities/sh.html"><i>sh), temporarily replaced when a shell function is invoked (see <a href="#tag_19_09_05">2.9.5
Function Definition Command), and can be reassigned with the <a href="#set"><i>set special built-in command.
<h4><a name="tag_19_05_02" id="tag_19_05_02">2.5.2 Special Parameters
<p class="tent">Listed below are the special parameters and the values to which they shall expand. Only the values of the special
parameters are listed; see <a href="#tag_19_06">2.6 Word Expansions for a detailed summary of all the stages involved in
expanding words.
<dl compact>
<dd>
<dt><tt>@
<dd>Expands to the positional parameters, starting from one, initially producing one field for each positional parameter that is
set. When the expansion occurs in a context where field splitting will be performed, any empty fields may be discarded and each of
the non-empty fields shall be further split as described in <a href="#tag_19_06_05">2.6.5 Field Splitting. When the expansion
occurs within double-quotes, the behavior is unspecified unless one of the following is true:
<ul>
<li class="tent">Field splitting as described in <a href="#tag_19_06_05">2.6.5 Field Splitting would be performed if the
expansion were not within double-quotes (regardless of whether field splitting would have any effect; for example, if <i>IFS is
null).
<li class="tent">The double-quotes are within the <i>word of a &#36;{<i>parameter:-<i>word} or a
&#36;{<i>parameter:+<i>word} expansion (with or without the &lt;colon&gt;; see <a href="#tag_19_06_02">2.6.2 Parameter
Expansion) which would have been subject to field splitting if <i>parameter had been expanded instead of <i>word.

<p class="tent">If one of these conditions is true, the initial fields shall be retained as separate fields, except that if the
parameter being expanded was embedded within a word, the first field shall be joined with the beginning part of the original word
and the last field shall be joined with the end part of the original word. In all other contexts the results of the expansion are
unspecified. If there are no positional parameters, the expansion of <tt>&#39;@&#39; shall generate zero fields, even when
<tt>&#39;@&#39; is within double-quotes; however, if the expansion is embedded within a word which contains one or more other parts
that expand to a quoted null string, these null string(s) shall still produce an empty field, except that if the other parts are
all within the same double-quotes as the <tt>&#39;@&#39;, it is unspecified whether the result is zero fields or one empty field.

<dt><tt>&#42;
<dd>Expands to the positional parameters, starting from one, initially producing one field for each positional parameter that is
set. When the expansion occurs in a context where field splitting will be performed, any empty fields may be discarded and each of
the non-empty fields shall be further split as described in <a href="#tag_19_06_05">2.6.5 Field Splitting. When the expansion
occurs in a context where field splitting will not be performed, the initial fields shall be joined to form a single field with the
value of each parameter separated by the first character of the <i>IFS variable if <i>IFS contains at least one character,
or separated by a &lt;space&gt; if <i>IFS is unset, or with no separation if <i>IFS is set to a null string.
<dt><tt>#
<dd>Expands to the shortest representation of the decimal number of positional parameters. The command name (parameter 0) shall not
be counted in the number given by <tt>&#39;#&#39; because it is a special parameter, not a positional parameter.
<dt><tt>?
<dd>Expands to the shortest representation of the decimal exit status (see <a href="#tag_19_08_02">2.8.2 Exit Status for
Commands) of the pipeline (see <a href="#tag_19_09_02">2.9.2 Pipelines) executed from the current shell execution
environment (not a subshell environment) that most recently either terminated or, optionally but only if the shell is interactive
and job control is enabled, was stopped by a signal. If this pipeline terminated, the status value shall be its exit status;
otherwise, the status value shall be the same as the exit status that would have resulted if the pipeline had been terminated by a
signal with the same number as the signal that stopped it. The value of the special parameter <tt>&#39;?&#39; shall be set to 0 during
initialization of the shell. When a subshell environment is created, the value of the special parameter <tt>&#39;?&#39; from the
invoking shell environment shall be preserved in the subshell. <basefont size="2">
<dl>
<dt><b>Note:
<dd>In <tt>var=&#36;(some&#95;command); echo &#36;? the output is the exit status of <tt>some&#95;command, which is executed in a
subshell environment, but this is because its exit status becomes the exit status of the assignment command
<tt>var=&#36;(some&#95;command) (see <a href="#tag_19_09_01">2.9.1 Simple Commands) and this assignment command is the most
recently completed pipeline. Likewise for any pipeline consisting entirely of a simple command that has no command word, but
contains one or more command substitutions. (See <a href="#tag_19_09_01">2.9.1 Simple Commands.)

<basefont size="3">
<dt><tt>-
<dd>(Hyphen.) Expands to the current option flags (the single-letter option names concatenated into a string) as specified on
invocation, by the <a href="#set"><i>set special built-in command, or implicitly by the shell. It is unspecified whether
the <b>-c and <b>-s options are included in the expansion of <tt>&#34;&#36;-&#34;. The <b>-i option shall be included in
<tt>&#34;&#36;-&#34; if the shell is interactive, regardless of whether it was specified on invocation.
<dt><tt>&#36;
<dd>Expands to the shortest representation of the decimal process ID of the invoked shell. In a subshell (see <a href=
"#tag_19_13">2.13 Shell Execution Environment), <tt>&#39;&#36;&#39; shall expand to the same value as that of the current shell.
<dt><tt>!
<dd>Expands to the shortest representation of the decimal process ID associated with the most recent asynchronous AND-OR list (see
<a href="#tag_19_09_03_02">2.9.3.1 Asynchronous AND-OR Lists) executed from the current shell execution environment, or to the
shortest representation of the decimal process ID of the last command specified in the currently executing pipeline in the
job-control background job that most recently resumed execution through the use of <a href="../utilities/bg.html"><i>bg,
whichever is the most recent.
<dt>0
<dd>(Zero.) Expands to the name of the shell or shell script. See <a href="../utilities/sh.html#"><i>sh for a detailed
description of how this name is derived.

<p class="tent">See the description of the <i>IFS variable in <a href="#tag_19_05_03">2.5.3 Shell Variables.
<h4><a name="tag_19_05_03" id="tag_19_05_03">2.5.3 Shell Variables
<p class="tent">Variables shall be initialized from the environment (as defined by XBD <a href=
"../basedefs/V1_chap08.html#tag_08"><i>8. Environment Variables and the <i>exec function in the System Interfaces
volume of POSIX.1-2024) and can be given new values with variable assignment commands. Shell variables shall be initialized only
from environment variables that have valid names. If a variable is initialized from the environment, it shall be marked for export
immediately; see the <a href="#export"><i>export special built-in. New variables can be defined and initialized with
variable assignments, with the <a href="../utilities/read.html"><i>read or <a href=
"../utilities/getopts.html"><i>getopts utilities, with the <i>name parameter in a <b>for loop, with the
&#36;{<i>name=<i>word} expansion, or with other mechanisms provided as implementation extensions.<br>
<p class="tent">The following variables shall affect the execution of the shell:
<dl compact>
<dd>
<dt><i>ENV
<dd><sup>&#91;<a href="javascript:open_code('UP')">UP&#93; <img src=".pic/opt-start.gif" alt="[Option Start]" border="0">
The processing of the <i>ENV shell variable shall be supported if the system supports the User Portability Utilities option.
<img src=".pic/opt-end.gif" alt="[Option End]" border="0">
<p class="tent">This variable, when and only when an interactive shell is invoked, shall be subjected to parameter expansion (see
<a href="#tag_19_06_02">2.6.2 Parameter Expansion) by the shell and the resulting value shall be used as a pathname of a file.
Before any interactive commands are read, the shell shall tokenize (see <a href="#tag_19_03">2.3 Token Recognition) the
contents of the file, parse the tokens as a <i>program (see <a href="#tag_19_10">2.10 Shell Grammar), and execute the
resulting commands in the current environment. (In other words, the contents of the <i>ENV file are not parsed as a single
<i>compound&#95;list. This distinction matters because it influences when aliases take effect.) The file need not be executable. If
the expanded value of <i>ENV is not an absolute pathname, the results are unspecified. <i>ENV shall be ignored if the
user&#39;s real and effective user IDs or real and effective group IDs are different.

<dt><i>HOME
<dd>The pathname of the user&#39;s home directory. The contents of <i>HOME are used in tilde expansion (see <a href=
"#tag_19_06_01">2.6.1 Tilde Expansion).
<dt><i>IFS
<dd>A string treated as a list of characters that is used for field splitting, expansion of the <tt>&#39;&#42;&#39; special parameter, and
to split lines into fields with the <a href="../utilities/read.html"><i>read utility. If the value of <i>IFS includes
any bytes that do not form part of a valid character, the results of field splitting, expansion of <tt>&#39;&#42;&#39;, and use of the
<a href="../utilities/read.html"><i>read utility are unspecified.
<p class="tent">If <i>IFS is not set, it shall behave as normal for an unset variable, except that field splitting by the shell
and line splitting by the <a href="../utilities/read.html"><i>read utility shall be performed as if the value of <i>IFS
is &lt;space&gt;&lt;tab&gt;&lt;newline&gt;; see <a href="#tag_19_06_05">2.6.5 Field Splitting.
<p class="tent">The shell shall set <i>IFS to &lt;space&gt;&lt;tab&gt;&lt;newline&gt; when it is invoked.

<dt><i>LANG
<dd>Provide a default value for the internationalization variables that are unset or null. (See XBD <a href=
"../basedefs/V1_chap08.html#tag_08_02"><i>8.2 Internationalization Variables for the precedence of internationalization
variables used to determine the values of locale categories.)
<dt><i>LC&#95;ALL
<dd>The value of this variable overrides the <i>LC&#95;&#42; variables and <i>LANG , as described in XBD <a href=
"../basedefs/V1_chap08.html#tag_08"><i>8. Environment Variables.
<dt><i>LC&#95;COLLATE
<dd>Determine the behavior of range expressions, equivalence classes, and multi-character collating elements within pattern
matching.
<dt><i>LC&#95;CTYPE
<dd>Determine the interpretation of sequences of bytes of text data as characters (for example, single-byte as opposed to
multi-byte characters), which characters are defined as letters (character class <b>alpha) and &lt;blank&gt; characters
(character class <b>blank), and the behavior of character classes within pattern matching. Changing the value of
<i>LC&#95;CTYPE after the shell has started shall not affect the lexical processing of shell commands in the current shell
execution environment or its subshells. Invoking a shell script or performing <a href="#exec"><i>exec <a href=
"../utilities/sh.html"><i>sh subjects the new shell to the changes in <i>LC&#95;CTYPE .
<dt><i>LC&#95;MESSAGES
<dd>Determine the language in which messages should be written.
<dt><i>LINENO
<dd><sup>&#91;<a href="javascript:open_code('UP')">UP&#93; <img src=".pic/opt-start.gif" alt="[Option Start]" border="0">
The processing of the <i>LINENO shell variable shall be supported if the system supports the User Portability Utilities option.
<img src=".pic/opt-end.gif" alt="[Option End]" border="0">
<p class="tent">Set by the shell to a decimal number representing the current sequential line number (numbered starting with 1)
within a script or function before it executes each command. If the user unsets or resets <i>LINENO , the variable may lose its
special meaning for the life of the shell. If the shell is not currently executing a script or function, the value of <i>LINENO
is unspecified.

<dt><i>NLSPATH
<dd><sup>&#91;<a href="javascript:open_code('XSI')">XSI&#93; <img src=".pic/opt-start.gif" alt="[Option Start]" border="0">
Determine the location of message catalogs for the processing of <i>LC&#95;MESSAGES . <img src=".pic/opt-end.gif" alt=
"[Option End]" border="0">
<dt><i>PATH
<dd>A string formatted as described in XBD <a href="../basedefs/V1_chap08.html#tag_08"><i>8. Environment Variables, used
to effect command interpretation; see <a href="#tag_19_09_01_04">2.9.1.4 Command Search and Execution.
<dt><i>PPID
<dd>Set by the shell to the decimal value of its parent process ID during initialization of the shell. In a subshell (see <a href=
"#tag_19_13">2.13 Shell Execution Environment), <i>PPID shall be set to the same value as that of the parent of the
current shell. For example, <a href="../utilities/echo.html"><i>echo &#36;<i>PPID and (<a href=
"../utilities/echo.html"><i>echo &#36;<i>PPID ) would produce the same value.
<dt><i>PS1
<dd><sup>&#91;<a href="javascript:open_code('UP')">UP&#93; <img src=".pic/opt-start.gif" alt="[Option Start]" border="0">
The processing of the <i>PS1 shell variable shall be supported if the system supports the User Portability Utilities option.
<img src=".pic/opt-end.gif" alt="[Option End]" border="0">
<p class="tent">Each time an interactive shell is ready to read a command, the value of this variable shall be subjected to
parameter expansion (see <a href="#tag_19_06_02">2.6.2 Parameter Expansion) and exclamation-mark expansion (see below).
Whether the value is also subjected to command substitution (see <a href="#tag_19_06_03">2.6.3 Command Substitution) or
arithmetic expansion (see <a href="#tag_19_06_04">2.6.4 Arithmetic Expansion) or both is unspecified. After expansion, the
value shall be written to standard error.
<p class="tent">The expansions shall be performed in two passes, where the result of the first pass is input to the second pass.
One of the passes shall perform only the exclamation-mark expansion described below. The other pass shall perform the other
expansion(s) according to the rules in <a href="#tag_19_06">2.6 Word Expansions. Which of the two passes is performed first is
unspecified.
<p class="tent">The default value shall be <tt>&#34;&#36; &#34;. For users who have specific additional implementation-defined
privileges, the default may be another, implementation-defined value.
<p class="tent">Exclamation-mark expansion: The shell shall replace each instance of the &lt;exclamation-mark&gt; character
(<tt>&#39;!&#39;) with the history file number (see <a href="../utilities/sh.html#tag_20_110_13_01"><i>Command History List)
of the next command to be typed. An &lt;exclamation-mark&gt; character escaped by another &lt;exclamation-mark&gt; character (that
is, <tt>&#34;!!&#34;) shall expand to a single &lt;exclamation-mark&gt; character.

<dt><i>PS2
<dd><sup>&#91;<a href="javascript:open_code('UP')">UP&#93; <img src=".pic/opt-start.gif" alt="[Option Start]" border="0">
The processing of the <i>PS2 shell variable shall be supported if the system supports the User Portability Utilities option.
<img src=".pic/opt-end.gif" alt="[Option End]" border="0">
<p class="tent">Each time the user enters a &lt;newline&gt; prior to completing a command line in an interactive shell, the value
of this variable shall be subjected to parameter expansion (see <a href="#tag_19_06_02">2.6.2 Parameter Expansion). Whether
the value is also subjected to command substitution (see <a href="#tag_19_06_03">2.6.3 Command Substitution) or arithmetic
expansion (see <a href="#tag_19_06_04">2.6.4 Arithmetic Expansion) or both is unspecified. After expansion, the value shall be
written to standard error. The default value shall be <tt>&#34;&gt; &#34;.

<dt><i>PS4
<dd><sup>&#91;<a href="javascript:open_code('UP')">UP&#93; <img src=".pic/opt-start.gif" alt="[Option Start]" border="0">
The processing of the <i>PS4 shell variable shall be supported if the system supports the User Portability Utilities option.
<img src=".pic/opt-end.gif" alt="[Option End]" border="0">
<p class="tent">When an execution trace (<a href="#set"><i>set <b>-x) is being performed, before each line in the
execution trace, the value of this variable shall be subjected to parameter expansion (see <a href="#tag_19_06_02">2.6.2 Parameter
Expansion). Whether the value is also subjected to command substitution (see <a href="#tag_19_06_03">2.6.3 Command
Substitution) or arithmetic expansion (see <a href="#tag_19_06_04">2.6.4 Arithmetic Expansion) or both is unspecified.
After expansion, the value shall be written to standard error. The default value shall be <tt>&#34;+ &#34;.

<dt><i>PWD
<dd>Set by the shell and by the <a href="../utilities/cd.html"><i>cd utility. In the shell the value shall be initialized
from the environment as follows. If a value for <i>PWD is passed to the shell in the environment when it is executed, the value
is an absolute pathname of the current working directory that is no longer than {PATH&#95;MAX} bytes including the terminating null
byte, and the value does not contain any components that are dot or dot-dot, then the shell shall set <i>PWD to the value from
the environment. Otherwise, if a value for <i>PWD is passed to the shell in the environment when it is executed, the value is
an absolute pathname of the current working directory, and the value does not contain any components that are dot or dot-dot, then
it is unspecified whether the shell sets <i>PWD to the value from the environment or sets <i>PWD to the pathname that would
be output by <a href="../utilities/pwd.html"><i>pwd <b>-P. Otherwise, the <a href="../utilities/sh.html"><i>sh
utility sets <i>PWD to the pathname that would be output by <a href="../utilities/pwd.html"><i>pwd <b>-P. In cases
where <i>PWD is set to the value from the environment, the value can contain components that refer to files of type symbolic
link. In cases where <i>PWD is set to the pathname that would be output by <a href="../utilities/pwd.html"><i>pwd
<b>-P, if there is insufficient permission on the current working directory, or on any parent of that directory, to determine
what that pathname would be, the value of <i>PWD is unspecified. Assignments to this variable may be ignored. If an application
sets or unsets the value of <i>PWD , the behaviors of the <a href="../utilities/cd.html"><i>cd and <a href=
"../utilities/pwd.html"><i>pwd utilities are unspecified.

<h3><a name="tag_19_06" id="tag_19_06">2.6 Word Expansions
<p class="tent">This section describes the various expansions that are performed on words. Not all expansions are performed on
every word, as explained in the following sections and elsewhere in this chapter. The expansions that are performed for a given
word shall be performed in the following order:
<p class="tent">
<ol>
<li class="tent">Tilde expansion (see <a href="#tag_19_06_01">2.6.1 Tilde Expansion), parameter expansion (see <a href=
"#tag_19_06_02">2.6.2 Parameter Expansion), command substitution (see <a href="#tag_19_06_03">2.6.3 Command Substitution
), and arithmetic expansion (see <a href="#tag_19_06_04">2.6.4 Arithmetic Expansion) shall be performed, beginning to end. See
item 5 in <a href="#tag_19_03">2.3 Token Recognition.
<li class="tent">Field splitting (see <a href="#tag_19_06_05">2.6.5 Field Splitting) shall be performed on the portions of the
fields generated by step 1.
<li class="tent">Pathname expansion (see <a href="#tag_19_06_06">2.6.6 Pathname Expansion) shall be performed, unless <a href=
"#set"><i>set <b>-f is in effect.
<li class="tent">Quote removal (see <a href="#tag_19_06_07">2.6.7 Quote Removal), if performed, shall always be performed
last.

<p class="tent">Tilde expansions, parameter expansions, command substitutions, arithmetic expansions, and quote removals that occur
within a single word shall expand to a single field, except as described below. The shell shall create multiple fields or no fields
from a single word only as a result of field splitting, pathname expansion, or the following cases:
<ol>
<li class="tent">Parameter expansion of the special parameters <tt>&#39;@&#39; and <tt>&#39;&#42;&#39;, as described in <a href=
"#tag_19_05_02">2.5.2 Special Parameters, can create multiple fields or no fields from a single word.
<li class="tent">When the expansion occurs in a context where field splitting will be performed, a word that contains all of the
following somewhere within it, before any expansions are applied, in the order specified:
<ul>
<li class="tent">an unquoted &lt;left-curly-bracket&gt; (<tt>&#39;{&#39;) that is not immediately preceded by an unquoted
&lt;dollar-sign&gt; (<tt>&#39;&#36;&#39;)
<li class="tent">one or more unquoted &lt;comma&gt; (<tt>&#39;,&#39;) characters or a sequence that consists of two adjacent
&lt;period&gt; (<tt>&#39;.&#39;) characters surrounded by other characters (which can also be &lt;period&gt; characters)
<li class="tent">an unquoted &lt;right-curly-bracket&gt; (<tt>&#39;}&#39;)

<p class="tent">may be subject to an additional implementation-defined form of expansion that can create multiple fields from a
single word. This expansion, if supported, shall be applied before all the other word expansions are applied. The other expansions
shall then be applied to each field that results from this expansion.

<p class="tent">When the expansions in this section are performed other than in the context of preparing a command for execution,
they shall be carried out in the current shell execution environment.
<p class="tent">When expanding words for a command about to be executed, and the word will be the command name or an argument to
the command, the expansions shall be carried out in the current shell execution environment. (The environment for the command to be
executed is unknown until the command word is known.)
<p class="tent">When expanding the words in a command about to be executed that are used with variable assignments or redirections,
it is unspecified whether the expansions are carried out in the current execution environment or in the environment of the command
about to be executed.
<p class="tent">The <tt>&#39;&#36;&#39; character is used to introduce parameter expansion, command substitution, or arithmetic
evaluation. If a <tt>&#39;&#36;&#39; that is neither within single-quotes nor escaped by a &lt;backslash&gt; is immediately followed by a
character that is not a &lt;space&gt;, not a &lt;tab&gt;, not a &lt;newline&gt;, and is not one of the following:
<ul>
<li class="tent">A numeric character
<li class="tent">The name of one of the special parameters (see <a href="#tag_19_05_02">2.5.2 Special Parameters)
<li class="tent">A valid first character of a variable name
<li class="tent">A &lt;left-curly-bracket&gt; (<tt>&#39;{&#39;)
<li class="tent">A &lt;left-parenthesis&gt;
<li class="tent">A single-quote

<p class="tent">the result is unspecified. If a <tt>&#39;&#36;&#39; that is neither within single-quotes nor escaped by a
&lt;backslash&gt; is immediately followed by a &lt;space&gt;, &lt;tab&gt;, or a &lt;newline&gt;, or is not followed by any
character, the <tt>&#39;&#36;&#39; shall be treated as a literal character.
<h4><a name="tag_19_06_01" id="tag_19_06_01">2.6.1 Tilde Expansion
<p class="tent">A &#34;tilde-prefix&#34; consists of an unquoted &lt;tilde&gt; character at the beginning of a word, followed by all of
the characters preceding the first unquoted &lt;slash&gt; in the word, or all the characters in the word if there is no
&lt;slash&gt;. In an assignment (see XBD <a href="../basedefs/V1_chap04.html#tag_04_26"><i>4.26 Variable Assignment),
multiple tilde-prefixes can be used: one at the beginning of the word (that is, following the &lt;equals-sign&gt; of the
assignment), or one following any unquoted &lt;colon&gt;, or both. A tilde-prefix in an assignment is terminated by the first
unquoted &lt;colon&gt; or &lt;slash&gt;, or the end of the assignment word.
<p class="tent">If the tilde-prefix consists of only the &lt;tilde&gt; character, it shall be replaced by the value of the variable
<i>HOME . If <i>HOME is unset, the results are unspecified.
<p class="tent">Otherwise, the characters in the tilde-prefix following the &lt;tilde&gt; shall be treated as a possible login name
from the user database. If these characters do not form a portable login name (see the description of the <i>LOGNAME
environment variable in XBD <a href="../basedefs/V1_chap08.html#tag_08_03"><i>8.3 Other Environment Variables), the
results are unspecified.
<p class="tent"><basefont size="2">
<dl>
<dt><b>Note:
<dd>Since the tilde-prefix is not subject to further word expansions after the &lt;tilde&gt; is removed to obtain the login name,
none of the following has a portable login name following the &lt;tilde&gt;:
<pre>
<tt>~&#34;string&#34;
~&#39;string&#39;
~&#36;var
~&#92;/bin

<p class="tent">owing to the presence of <tt>&#39;&#34;&#39;, <tt>&#39;&#92;&#39;&#39;, <tt>&#39;&#36;&#39;, <tt>&#39;&#92;&#92;&#39;, and <tt>&#39;/&#39; characters in
the login name.

<basefont size="3">
<p class="tent">If the characters in the tilde-prefix following the &lt;tilde&gt; form a portable login name, the tilde-prefix
shall be replaced by a pathname of the initial working directory associated with the login name. The pathname shall be obtained as
if by using the <a href="../functions/getpwnam.html"><i>getpwnam() function as defined in the System Interfaces volume of
POSIX.1-2024. If the system does not recognize the login name, the results are unspecified.
<p class="tent">The pathname that replaces the tilde-prefix shall be treated as if quoted to prevent it being altered by field
splitting and pathname expansion; if a &lt;slash&gt; follows the tilde-prefix and the pathname ends with a &lt;slash&gt;, the
trailing &lt;slash&gt; from the pathname should be omitted from the replacement. If the word being expanded consists of only the
&lt;tilde&gt; character and <i>HOME is set to the null string, this produces an empty field (as opposed to zero fields) as the
expanded word. <basefont size="2">
<dl>
<dt><b>Note:
<dd>A future version of this standard may require that if a &lt;slash&gt; follows the tilde-prefix and the pathname ends with a
&lt;slash&gt;, the trailing &lt;slash&gt; from the pathname is omitted from the replacement.

<basefont size="3">
<h4><a name="tag_19_06_02" id="tag_19_06_02">2.6.2 Parameter Expansion
<p class="tent">The format for parameter expansion is as follows:
<pre>
<tt>&#36;{<i>expression<tt>}

<p class="tent">where <i>expression consists of all characters until the matching <tt>&#39;}&#39;. Any <tt>&#39;}&#39; escaped by a
&lt;backslash&gt; or within a quoted string, and characters in embedded arithmetic expansions, command substitutions, and variable
expansions, shall not be examined in determining the matching <tt>&#39;}&#39;.
<p class="tent">The simplest form for parameter expansion is:
<pre>
<tt>&#36;{<i>parameter<tt>}

<p class="tent">The value, if any, of <i>parameter shall be substituted.
<p class="tent">The parameter name or symbol can be enclosed in braces, which are optional except for positional parameters with
more than one digit or when <i>parameter is a name and is followed by a character that could be interpreted as part of the
name.
<p class="tent">For a parameter that is not enclosed in braces:
<ul>
<li class="tent">If the parameter is a name, the expansion shall use the longest valid name (see XBD <a href=
"../basedefs/V1_chap03.html#tag_03_216"><i>3.216 Name), whether or not the variable denoted by that name exists.
<li class="tent">Otherwise, the parameter is a single-character symbol, and behavior is unspecified if that character is neither a
digit nor one of the special parameters (see <a href="#tag_19_05_02">2.5.2 Special Parameters).

<p class="tent">In addition, a parameter expansion can be modified by using one of the following formats. In each case that a value
of <i>word is needed (based on the state of <i>parameter, as described below), <i>word shall be subjected to tilde
expansion, parameter expansion, command substitution, arithmetic expansion, and quote removal. If <i>word is not needed, it
shall not be expanded. The <tt>&#39;}&#39; character that delimits the following parameter expansion modifications shall be determined
as described previously in this section and in <a href="#tag_19_02_03">2.2.3 Double-Quotes. If <i>parameter is
<tt>&#39;&#42;&#39; or <tt>&#39;@&#39;, the result of the expansion is unspecified.
<dl compact>
<dd>
<dt>&#36;{<i>parameter:-<b>&#91;<i>word<b>&#93;}
<dd><b>Use Default Values. If <i>parameter is unset or null, the expansion of <i>word (or an empty string if
<i>word is omitted) shall be substituted; otherwise, the value of <i>parameter shall be substituted.
<dt>&#36;{<i>parameter:=<b>&#91;<i>word<b>&#93;}
<dd><b>Assign Default Values. If <i>parameter is unset or null, quote removal shall be performed on the expansion of
<i>word and the result (or an empty string if <i>word is omitted) shall be assigned to <i>parameter. In all cases, the
final value of <i>parameter shall be substituted. Only variables, not positional parameters or special parameters, can be
assigned in this way.
<dt>&#36;{<i>parameter:?<b>&#91;<i>word<b>&#93;}
<dd><b>Indicate Error if Null or Unset. If <i>parameter is unset or null, the expansion of <i>word (or a message
indicating it is unset if <i>word is omitted) shall be written to standard error and the shell exits with a non-zero exit
status. Otherwise, the value of <i>parameter shall be substituted. An interactive shell need not exit.
<dt>&#36;{<i>parameter:+<b>&#91;<i>word<b>&#93;}
<dd><b>Use Alternative Value. If <i>parameter is unset or null, null shall be substituted; otherwise, the expansion of
<i>word (or an empty string if <i>word is omitted) shall be substituted.

<p class="tent">In the parameter expansions shown previously, use of the &lt;colon&gt; in the format shall result in a test for a
parameter that is unset or null; omission of the &lt;colon&gt; shall result in a test for a parameter that is only unset. If
parameter is <tt>&#39;#&#39; and the colon is omitted, the application shall ensure that <i>word is specified (this is necessary
to avoid ambiguity with the string length expansion). The following table summarizes the effect of the &lt;colon&gt;:<br>
<center>
<table border="1" cellpadding="3" align="center">
<tr valign="top">
<th align="center">
<p class="tent"><b> 

<th align="center">
<p class="tent"><b><i>parameter Set and Not Null

<th align="center">
<p class="tent"><b><i>parameter Set But Null

<th align="center">
<p class="tent"><b><i>parameter Unset

<tr valign="top">
<td align="left">
<p class="tent"><b>&#36;{<i>parameter<b>:-<i>word<b>}

<td align="left">
<p class="tent">substitute <i>parameter

<td align="left">
<p class="tent">substitute <i>word

<td align="left">
<p class="tent">substitute <i>word

<tr valign="top">
<td align="left">
<p class="tent"><b>&#36;{<i>parameter<b>-<i>word<b>}

<td align="left">
<p class="tent">substitute <i>parameter

<td align="left">
<p class="tent">substitute null

<td align="left">
<p class="tent">substitute <i>word

<tr valign="top">
<td align="left">
<p class="tent"><b>&#36;{<i>parameter<b>:=<i>word<b>}

<td align="left">
<p class="tent">substitute <i>parameter

<td align="left">
<p class="tent">assign <i>word

<td align="left">
<p class="tent">assign <i>word

<tr valign="top">
<td align="left">
<p class="tent"><b>&#36;{<i>parameter<b>=<i>word<b>}

<td align="left">
<p class="tent">substitute <i>parameter

<td align="left">
<p class="tent">substitute null

<td align="left">
<p class="tent">assign <i>word

<tr valign="top">
<td align="left">
<p class="tent"><b>&#36;{<i>parameter<b>:?<i>word<b>}

<td align="left">
<p class="tent">substitute <i>parameter

<td align="left">
<p class="tent">error, exit

<td align="left">
<p class="tent">error, exit

<tr valign="top">
<td align="left">
<p class="tent"><b>&#36;{<i>parameter<b>?<i>word<b>}

<td align="left">
<p class="tent">substitute <i>parameter

<td align="left">
<p class="tent">substitute null

<td align="left">
<p class="tent">error, exit

<tr valign="top">
<td align="left">
<p class="tent"><b>&#36;{<i>parameter<b>:+<i>word<b>}

<td align="left">
<p class="tent">substitute <i>word

<td align="left">
<p class="tent">substitute null

<td align="left">
<p class="tent">substitute null

<tr valign="top">
<td align="left">
<p class="tent"><b>&#36;{<i>parameter<b>+<i>word<b>}

<td align="left">
<p class="tent">substitute <i>word

<td align="left">
<p class="tent">substitute <i>word

<td align="left">
<p class="tent">substitute null

<p class="tent">In all cases shown with &#34;substitute&#34;, the expression is replaced with the value shown. In all cases shown with
&#34;assign&#34;, <i>parameter is assigned that value, which also replaces the expression.
<dl compact>
<dd>
<dt>&#36;{#<i>parameter}
<dd><b>String Length. The shortest decimal representation of the length in characters of the value of <i>parameter shall be
substituted. If <i>parameter is <tt>&#39;&#42;&#39; or <tt>&#39;@&#39;, the result of the expansion is unspecified. If <i>parameter
is unset and <a href="#set"><i>set <b>-u is in effect, the expansion shall fail.

<p class="tent">The following four varieties of parameter expansion provide for character substring processing. In each case,
pattern matching notation (see <a href="#tag_19_14">2.14 Pattern Matching Notation), rather than regular expression notation,
shall be used to evaluate the patterns. If <i>parameter is <tt>&#39;#&#39;, <tt>&#39;&#42;&#39;, or <tt>&#39;@&#39;, the result of the
expansion is unspecified. If <i>parameter is unset and <a href="#set"><i>set <b>-u is in effect, the expansion
shall fail. Enclosing the full parameter expansion string in double-quotes shall not cause the following four varieties of pattern
characters to be quoted, whereas quoting characters within the braces shall have this effect. In each variety, if <i>word is
omitted, the empty pattern shall be used.
<dl compact>
<dd>
<dt>&#36;{<i>parameter%<b>&#91;<i>word<b>&#93;}
<dd><b>Remove Smallest Suffix Pattern. The <i>word shall be expanded to produce a pattern. The parameter expansion shall
then result in <i>parameter, with the smallest portion of the suffix matched by the <i>pattern deleted. If present,
<i>word shall not begin with an unquoted <tt>&#39;%&#39;.
<dt>&#36;{<i>parameter%%<b>&#91;<i>word<b>&#93;}
<dd><b>Remove Largest Suffix Pattern. The <i>word shall be expanded to produce a pattern. The parameter expansion shall
then result in <i>parameter, with the largest portion of the suffix matched by the <i>pattern deleted.
<dt>&#36;{<i>parameter#<b>&#91;<i>word<b>&#93;}
<dd><b>Remove Smallest Prefix Pattern. The <i>word shall be expanded to produce a pattern. The parameter expansion shall
then result in <i>parameter, with the smallest portion of the prefix matched by the <i>pattern deleted. If present,
<i>word shall not begin with an unquoted <tt>&#39;#&#39;.
<dt>&#36;{<i>parameter##<b>&#91;<i>word<b>&#93;}
<dd><b>Remove Largest Prefix Pattern. The <i>word shall be expanded to produce a pattern. The parameter expansion shall
then result in <i>parameter, with the largest portion of the prefix matched by the <i>pattern deleted.

<hr>
<div class="box"><em>The following sections are informative.
<h5><a name="tag_19_06_02_01" id="tag_19_06_02_01">Examples
<dl compact>
<dd>
<dt>&#36;{<i>parameter}
<dd><br>
In this example, the effects of omitting braces are demonstrated.
<pre>
<tt>a=1
set 2
echo &#36;{a}b-&#36;ab-&#36;{1}0-&#36;{10}-&#36;10
<b>1b&#45;&#45;20&#45;&#45;20<tt>

<dt>&#36;{<i>parameter-<i>word}
<dd><br>
This example demonstrates the difference between unset and set to the empty string, as well as the rules for finding the delimiting
close brace.
<blockquote>
<pre>
<tt>foo=asdf
echo &#36;{foo-bar}xyz}
<b>asdfxyz}<tt>
foo=
echo &#36;{foo-bar}xyz}
<b>xyz}<tt>
unset foo
echo &#36;{foo-bar}xyz}
<b>barxyz}<tt>

<dt>&#36;{<i>parameter:-<i>word}
<dd><br>
In this example, <a href="../utilities/ls.html"><i>ls is executed only if <i>x is null or unset. (The &#36;(<a href=
"../utilities/ls.html"><i>ls) command substitution notation is explained in <a href="#tag_19_06_03">2.6.3 Command
Substitution.)
<pre>
<tt>&#36;{x:-&#36;(ls)}

<dt>&#36;{<i>parameter:=<i>word}
<dd>
<pre>
<tt>unset X
echo &#36;{X:=abc}
<b>abc<tt>

<dt>&#36;{<i>parameter:?<i>word}
<dd>
<pre>
<tt>unset posix
echo &#36;{posix:?}
<b>sh: posix: parameter null or not set<tt>

<dt>&#36;{<i>parameter:+<i>word}
<dd>
<pre>
<tt>set a b c
echo &#36;{3:+posix}
<b>posix<tt>

<dt>&#36;{#<i>parameter}
<dd>
<pre>
<tt>HOME=/usr/posix
echo &#36;{#HOME}
<b>10<tt>

<dt>&#36;{<i>parameter%<i>word}
<dd>
<pre>
<tt>x=file.c
echo &#36;{x%.c}.o
<b>file.o<tt>

<dt>&#36;{<i>parameter%%<i>word}
<dd>
<pre>
<tt>x=posix/src/std
echo &#36;{x%%/&#42;}
<b>posix<tt>

<dt>&#36;{<i>parameter#<i>word}
<dd>
<pre>
<tt>x=&#36;HOME/src/cmd
echo &#36;{x#&#36;HOME}
<b>/src/cmd<tt>

<dt>&#36;{<i>parameter##<i>word}
<dd>
<pre>
<tt>x=/one/two/three
echo &#36;{x##&#42;/}
<b>three<tt>

<p class="tent">The double-quoting of patterns is different depending on where the double-quotes are placed:
<dl compact>
<dd>
<dt><tt>&#34;&#36;{x#&#42;}&#34;
<dd>The &lt;asterisk&gt; is a pattern character.
<dt><tt>&#36;{x#&#34;&#42;&#34;}
<dd>The literal &lt;asterisk&gt; is quoted and not special.

<div class="box"><em>End of informative text.
<hr>
<h4><a name="tag_19_06_03" id="tag_19_06_03">2.6.3 Command Substitution
<p class="tent">Command substitution allows the output of one or more commands to be substituted in place of the commands
themselves. Command substitution shall occur when command(s) are enclosed as follows:
<pre>
<tt>&#36;(<i>commands<tt>)

<p class="tent">or (backquoted version):
<pre>
<tt>&#96;<i>commands<tt>&#96;

<p class="tent">The shell shall expand the command substitution by executing <i>commands in a subshell environment (see
<a href="#tag_19_13">2.13 Shell Execution Environment) and replacing the command substitution (the text of the <i>commands
string plus the enclosing <tt>&#34;&#36;()&#34; or backquotes) with the standard output of the command(s); if the output ends with one or
more bytes that have the encoded value of a &lt;newline&gt; character, they shall not be included in the replacement. Any such
bytes that occur elsewhere shall be included in the replacement; however, they might be treated as field delimiters and eliminated
during field splitting, depending on the value of <i>IFS and quoting that is in effect. If the output contains any null bytes,
the behavior is unspecified.
<p class="tent">Within the backquoted style of command substitution, if the command substitution is not within double-quotes,
&lt;backslash&gt; shall retain its literal meaning, except when followed by: <tt>&#39;&#36;&#39;, <tt>&#39;&#96;&#39;, or &lt;backslash&gt;. See
<a href="#tag_19_02_03">2.2.3 Double-Quotes for the handling of &lt;backslash&gt; when the command substitution is within
double-quotes. The search for the matching backquote shall be satisfied by the first unquoted non-escaped backquote; during this
search, if a non-escaped backquote is encountered within a shell comment, a here-document, an embedded command substitution of the
&#36;(<i>commands) form, or a quoted string, undefined results occur. A quoted string that begins, but does not end, within the
<tt>&#34;&#96;&#46;&#46;&#46;&#96;&#34; sequence produces undefined results.
<p class="tent">With the &#36;(<i>commands) form, all characters following the open parenthesis to the matching closing parenthesis
constitute the <i>commands string.
<p class="tent">With both the backquoted and &#36;(<i>commands) forms, the <i>commands string shall be tokenized (see <a href=
"#tag_19_03">2.3 Token Recognition) and parsed (see <a href="#tag_19_10">2.10 Shell Grammar). It is unspecified whether
the <i>commands string is parsed and executed incrementally as a <i>program (as for a shell script), or is parsed as a
single <i>compound&#95;list that is executed after the string has been completely parsed. In addition, it is unspecified whether
the terminating <tt>&#39;)&#39; of the &#36;(<i>commands) form can result from alias substitution. With the &#36;(<i>commands) form
any syntactically correct <i>program can be used for <i>commands, except that:
<ul>
<li class="tent">If the <i>commands string consists solely of redirections, the results are unspecified.
<li class="tent">If the <i>commands string is parsed as a single <i>compound&#95;list, before any commands are executed,
<a href="../utilities/alias.html"><i>alias and <a href="../utilities/unalias.html"><i>unalias commands in
<i>commands have no effect during parsing (see <a href="#tag_19_03_01">2.3.1 Alias Substitution). Strictly conforming
applications shall ensure that the <i>commands string does not depend on alias changes taking effect incrementally as would be
the case if parsed and executed as a <i>program.
<li class="tent">The behavior is unspecified if the terminating <tt>&#39;)&#39; is not present in the token containing the command
substitution; that is, if the <tt>&#39;)&#39; is expected to result from alias substitution.

<p class="tent">The results of command substitution shall not be processed for further tilde expansion, parameter expansion,
command substitution, or arithmetic expansion.
<p class="tent">Command substitution can be nested. To specify nesting within the backquoted version, the application shall precede
the inner backquotes with &lt;backslash&gt; characters; for example:
<pre>
<tt>&#92;&#96;<i>commands<tt>&#92;&#96;

<p class="tent">The syntax of the shell command language has an ambiguity for expansions beginning with <tt>&#34;&#36;((&#34;, which can
introduce an arithmetic expansion or a command substitution that starts with a subshell. Arithmetic expansion has precedence; that
is, the shell shall first determine whether it can parse the expansion as an arithmetic expansion and shall only parse the
expansion as a command substitution if it determines that it cannot parse the expansion as an arithmetic expansion. The shell need
not evaluate nested expansions when performing this determination. If it encounters the end of input without already having
determined that it cannot parse the expansion as an arithmetic expansion, the shell shall treat the expansion as an incomplete
arithmetic expansion and report a syntax error. A conforming application shall ensure that it separates the <tt>&#34;&#36;(&#34; and
<tt>&#39;(&#39; into two tokens (that is, separate them with white space) in a command substitution that starts with a subshell. For
example, a command substitution containing a single subshell could be written as:
<pre>
<tt>&#36;( (<i>commands<tt>) )

<h4><a name="tag_19_06_04" id="tag_19_06_04">2.6.4 Arithmetic Expansion
<p class="tent">Arithmetic expansion provides a mechanism for evaluating an arithmetic expression and substituting its value. The
format for arithmetic expansion shall be as follows:
<pre>
<tt>&#36;((<i>expression<tt>))

<p class="tent">The expression shall be treated as if it were in double-quotes, except that a double-quote inside the expression is
not treated specially. The shell shall expand all tokens in the expression for parameter expansion, command substitution, and quote
removal.
<p class="tent">Next, the shell shall treat this as an arithmetic expression and substitute the value of the expression. The
arithmetic expression shall be processed according to the rules given in <a href=
"../utilities/V3_chap01.html#tag_18_01_02_01"><i>1.1.2.1 Arithmetic Precision and Operations, with the following
exceptions:
<ul>
<li class="tent">Only signed long integer arithmetic is required.
<li class="tent">Only the decimal-constant, octal-constant, and hexadecimal-constant constants specified in the ISO C
standard, Section 6.4.4.1 are required to be recognized as constants.
<li class="tent">The <i>sizeof() operator and the prefix and postfix <tt>&#34;++&#34; and <tt>&#34;&#45;&#45;&#34; operators are not
required.
<li class="tent">Selection, iteration, and jump statements are not supported.

<p class="tent">All changes to variables in an arithmetic expression shall be in effect after the arithmetic expansion, as in the
parameter expansion <tt>&#34;&#36;{x=value}&#34;.
<p class="tent">If the shell variable <i>x contains a value that forms a valid integer constant, optionally including a leading
&lt;plus-sign&gt; or &lt;hyphen-minus&gt;, then the arithmetic expansions <tt>&#34;&#36;((x))&#34; and <tt>&#34;&#36;((&#36;x))&#34; shall return the
same value.
<p class="tent">As an extension, the shell may recognize arithmetic expressions beyond those listed. The shell may use a signed
integer type with a rank larger than the rank of <b>signed long. The shell may use a real-floating type instead of <b>signed
long as long as it does not affect the results in cases where there is no overflow. If the expression is invalid, or the
contents of a shell variable used in the expression are not recognized by the shell, the expansion fails and the shell shall write
a diagnostic message to standard error indicating the failure.
<hr>
<div class="box"><em>The following sections are informative.
<h5><a name="tag_19_06_04_01" id="tag_19_06_04_01">Examples
<p class="tent">A simple example using arithmetic expansion:
<pre>
<tt># repeat a command 100 times
x=100
while &#91; &#36;x -gt 0 &#93;
do
    <i>command<tt>
    x=&#36;((&#36;x-1))
done

<div class="box"><em>End of informative text.
<hr>
<h4><a name="tag_19_06_05" id="tag_19_06_05">2.6.5 Field Splitting
<p class="tent">After parameter expansion ( <a href="#tag_19_06_02">2.6.2 Parameter Expansion), command substitution (
<a href="#tag_19_06_03">2.6.3 Command Substitution), and arithmetic expansion ( <a href="#tag_19_06_04">2.6.4 Arithmetic
Expansion), if the shell variable <i>IFS (see <a href="#tag_19_05_03">2.5.3 Shell Variables) is set and its value is
not empty, or if <i>IFS is unset, the shell shall scan each field containing results of expansions and substitutions that did
not occur in double-quotes for field splitting; zero, one or multiple fields can result.
<p class="tent">For the remainder of this section, any reference to the results of an expansion, or results of expansions, shall be
interpreted to mean the results from one or more unquoted variable or arithmetic expansions, or unquoted command substitutions.
<p class="tent">If the <i>IFS variable is set and has an empty string as its value, no field splitting shall occur. However, if
an input field which contained the results of an expansion is entirely empty, it shall be removed. Note that this occurs before
quote removal; any input field that contains any quoting characters can never be empty at this point. After the removal of any such
fields from the input, the possibly modified input field list shall become the output.
<p class="tent">Each input field shall be considered in sequence, first to last, with the results of the algorithm described in
this section causing output fields to be generated, which shall remain in the same order as the input fields from which they
originated.
<p class="tent">Fields which contain no results from expansions shall not be affected by field splitting, and shall remain
unaltered, simply moving from the list of input fields to be next in the list of output fields.
<p class="tent">In the remainder of this description, it is assumed that there is present in the field at least one expansion
result; this assumption will not be restated. Field splitting only ever alters those parts of the field.
<p class="tent">For the purposes of this section, the term &#34;<i>IFS white space&#34; is used to mean any of the white-space bytes
(see XBD <a href="../basedefs/V1_chap03.html#tag_03_413"><i>3.413 White Space, <a href=
"../basedefs/V1_chap03.html#tag_03_414"><i>3.414 White-Space Byte, and <a href=
"../basedefs/V1_chap03.html#tag_03_415"><i>3.415 White-Space Character) &lt;space&gt;, &lt;tab&gt;, or &lt;newline&gt;
from the portable character set (see XBD <a href="../basedefs/V1_chap06.html#tag_06_01"><i>6.1 Portable Character Set)
which are present in the value of the <i>IFS variable, and perhaps other white-space characters. It is implementation-defined
whether other white-space characters which appear in the value of <i>IFS are also considered as &#34;<i>IFS white space&#34;. The
three characters above specified as <i>IFS white-space bytes are always <i>IFS white space, when they occur in the value of
<i>IFS , regardless of whether they are white-space characters in any relevant locale. For other locale-specific white-space
characters allowed by the implementation it is unspecified whether the character is considered as <i>IFS white space if it is
white space at the time it is assigned to the <i>IFS variable, or if it is white space at the time field splitting occurs. (The
locale might have changed between those events.)
<p class="tent">If the <i>IFS variable is unset, then for the purposes of this section, but without altering the value of the
variable, its value shall be considered to contain the three single-byte characters &lt;space&gt;, &lt;tab&gt;, and &lt;newline&gt;
from the portable character set, all of which are <i>IFS white-space characters.
<p class="tent">The shell shall use the byte sequences that form the characters in the value of the <i>IFS variable as
delimiters. Each of the characters &lt;space&gt;, &lt;tab&gt;, and &lt;newline&gt; which appears in the value of <i>IFS shall
be a single-byte delimiter. The shell shall use these delimiters as field terminators to split the results of expansions, along
with other adjacent bytes, into separate fields, as described below. Note that these delimiters terminate a field; they do not, of
themselves, cause a new field to start—subsequent bytes that are not from the results of an expansion, or that do not form
<i>IFS white-space characters are required for a new field to begin.
<p class="tent">Note that the shell processes arbitrary bytes from the input fields; there is no requirement that those bytes form
valid characters.
<p class="tent">If the results of the algorithm are that no fields are delimited; that is, if the input field is wholly empty or
consists entirely of <i>IFS white space, the result shall be zero fields (rather than an empty field).
<p class="tent">For the purposes of this section, when a field is said to be delimited, then the candidate field, as generated
below shall become an output field. When the algorithm transforms a candidate into an output field it shall be appended to the
current list of output fields.
<p class="tent">Each field containing the results from an expansion shall be processed in order, intermixed with fields not
containing the results of expansions, processed as described above, as if by using the following algorithm, examining bytes in the
input field, from beginning to end:
<ul>
<li class="tent">Begin with an empty candidate field and the input as specified above.
<li class="tent">When instructed to start the next iteration of the loop, this is the start of the loop. While the input (as
modified by earlier iterations of this loop) is not empty:
<ul>
<li class="tent">Consider the leading remaining byte or byte sequence of the input. No such byte sequence shall contain data such
that some bytes in the sequence resulted from an expansion, and others did not, nor which contains bytes resulting from the results
of more than one expansion. If the byte or sequence of bytes is:
<ol>
<li class="tent">A byte (or sequence of bytes) in the input which did not result from an expansion:
<p class="tent">Append this byte (or sequence) to the candidate, and remove it from the input. Start the next iteration of the
loop.

<li class="tent">A byte sequence in the input which resulted from an expansion and which does not form a character in <i>IFS :
<p class="tent">Append the first byte of the sequence to the candidate, and remove that byte from the input. Start the next
iteration of the loop.

<li class="tent">A byte sequence in the input which resulted from an expansion and which forms an <i>IFS white space character:
<p class="tent">Remove that byte sequence from the input, consider the new leading input byte sequence, and repeat this step.

<li class="tent">A byte sequence in the input which resulted from an expansion and which forms an <i>IFS character that is not
<i>IFS white space:
<p class="tent">Remove that byte sequence from the input, but note it was observed.

<p class="tent">At this point, if the candidate is not empty, or if a sequence of bytes representing an <i>IFS character that
is not <i>IFS white space was seen at step 4, then a field is said to have been delimited, and the candidate shall become an
output field.

<li class="tent">Empty (clear) the candidate, and start the next iteration of the loop.

<li class="tent">Once the input is empty, the candidate shall become an output field if and only if it is not empty.

<p class="tent">The ordered list of output fields so produced, which might be empty, shall replace the list of input fields.
<h4><a name="tag_19_06_06" id="tag_19_06_06">2.6.6 Pathname Expansion
<p class="tent">After field splitting, if <a href="#set"><i>set <b>-f is not in effect, each field in the resulting
command line shall be expanded using the algorithm described in <a href="#tag_19_14">2.14 Pattern Matching Notation, qualified
by the rules in <a href="#tag_19_14_03">2.14.3 Patterns Used for Filename Expansion.
<h4><a name="tag_19_06_07" id="tag_19_06_07">2.6.7 Quote Removal
<p class="tent">The quote character sequence &lt;dollar-sign&gt; single-quote and the single-character quote characters
(&lt;backslash&gt;, single-quote, and double-quote) that were present in the original word shall be removed unless they have
themselves been quoted. Note that the single-quote character that terminates a &lt;dollar-sign&gt; single-quote sequence is itself
a single-character quote character. <basefont size="2">
<dl>
<dt><b>Note:
<dd>After quote removal the shell still remembers which characters were quoted. This is necessary for purposes such as matching
patterns in a <b>case conditional construct (see <a href="#tag_19_09_04_05">2.9.4.3 Case Conditional Construct and <a href=
"#tag_19_14">2.14 Pattern Matching Notation).

<basefont size="3">
<h3><a name="tag_19_07" id="tag_19_07">2.7 Redirection
<p class="tent">Redirection is used to open and close files for the current shell execution environment (see <a href=
"#tag_19_13">2.13 Shell Execution Environment) or for any command. Redirection operators can be used with numbers representing
file descriptors (see XBD <a href="../basedefs/V1_chap03.html#tag_03_141"><i>3.141 File Descriptor) as described
below.
<p class="tent">The overall format used for redirection is:
<pre>
<b>&#91;<i>n<b>&#93;<i>redir-op word<tt>

<p class="tent">The number <i>n is an optional one or more digit decimal number designating the file descriptor number; the
application shall ensure it is delimited from any preceding text and immediately precedes the redirection operator <i>redir-op
(with no intervening &lt;blank&gt; characters allowed). If <i>n is quoted, the number shall not be recognized as part of the
redirection expression. For example:
<pre>
<tt>echo &#92;2&gt;a

<p class="tent">writes the character 2 into file <b>a. If any part of <i>redir-op is quoted, no redirection expression is
recognized. For example:
<pre>
<tt>echo 2&#92;&gt;a

<p class="tent">writes the characters 2&gt;<i>a to standard output. The optional number, redirection operator, and <i>word
shall not appear in the arguments provided to the command to be executed (if any).
<p class="tent">The shell may support an additional format used for redirection:
<pre>
<b>{<i>location<b>}<i>redir-op word<tt>

<p class="tent">where <i>location is non-empty and indicates a location where an integer value can be stored, such as the name
of a shell variable. If this format is supported its behavior is implementation-defined.
<p class="tent">The largest file descriptor number supported in shell redirections is implementation-defined; however, all
implementations shall support at least 0 to 9, inclusive, for use by the application.
<p class="tent">If the redirection operator is <tt>&#34;&lt;&lt;&#34; or <tt>&#34;&lt;&lt;-&#34;, the word that follows the redirection
operator shall be subjected to quote removal; it is unspecified whether any of the other expansions occur. For the other
redirection operators, the word that follows the redirection operator shall be subjected to tilde expansion, parameter expansion,
command substitution, arithmetic expansion, and quote removal. Pathname expansion shall not be performed on the word by a
non-interactive shell; an interactive shell may perform it, but if the expansion would result in more than one word it is
unspecified whether the redirection proceeds without pathname expansion being performed or the redirection fails. <basefont size=
"2">
<dl>
<dt><b>Note:
<dd>A future version of this standard may require that the redirection fails in this case.

<basefont size="3">
<p class="tent">If more than one redirection operator is specified with a command, the order of evaluation is from beginning to
end.
<p class="tent">A failure to open or create a file shall cause a redirection to fail.
<h4><a name="tag_19_07_01" id="tag_19_07_01">2.7.1 Redirecting Input
<p class="tent">Input redirection shall cause the file whose name results from the expansion of <i>word to be opened for
reading on the designated file descriptor, or standard input if the file descriptor is not specified.
<p class="tent">The general format for redirecting input is:
<pre>
<b>&#91;<i>n<b>&#93;<tt>&lt;<i>word<tt>

<p class="tent">where the optional <i>n represents the file descriptor number. If the number is omitted, the redirection shall
refer to standard input (file descriptor 0).
<h4><a name="tag_19_07_02" id="tag_19_07_02">2.7.2 Redirecting Output
<p class="tent">The two general formats for redirecting output are:
<pre>
<b>&#91;<i>n<b>&#93;<tt>&gt;<i>word
<b>&#91;<i>n<b>&#93;<tt>&gt;|<i>word

<p class="tent">where the optional <i>n represents the file descriptor number. If the number is omitted, the redirection shall
refer to standard output (file descriptor 1).
<p class="tent">Output redirection using the <tt>&#39;&gt;&#39; format shall fail if the <i>noclobber option is set (see the
description of <a href="#set"><i>set <b>-C) and the file named by the expansion of <i>word exists and is either a
regular file or a symbolic link that resolves to a regular file; it may also fail if the file is a symbolic link that does not
resolve to an existing file. The check for existence, file creation, and open operations shall be performed atomically as is done
by the <a href="../functions/open.html"><i>open() function as defined in System Interfaces volume of POSIX.1-2024 when the
O&#95;CREAT and O&#95;EXCL flags are set, except that if the file exists and is a symbolic link, the open operation need not fail with
&#91;EEXIST&#93; unless the symbolic link resolves to an existing regular file. Performing these operations atomically ensures that the
creation of lock files and unique (often temporary) files is reliable, with important caveats detailed in <a href=
"../xrat/V4_xcu_chap01.html#tag_23_02_07_02"><i>C.2.7.2 Redirecting Output. The check for the type of the file need not be
performed atomically with the check for existence, file creation, and open operations. If not, there is a potential race condition
that may result in a misleading shell diagnostic message when redirection fails. See XRAT <a href=
"../xrat/V4_xcu_chap01.html#tag_23_02_07_02"><i>C.2.7.2 Redirecting Output for more details.
<p class="tent">In all other cases (<i>noclobber not set, redirection using <tt>&#39;&gt;&#39; does not fail for the reasons
stated above, or redirection using the <tt>&#34;&gt;|&#34; format), output redirection shall cause the file whose name results from
the expansion of <i>word to be opened for output on the designated file descriptor, or standard output if none is specified. If
the file does not exist, it shall be created as an empty file; otherwise, it shall be opened as if the <a href=
"../functions/open.html"><i>open() function was called with the O&#95;TRUNC flag set.
<h4><a name="tag_19_07_03" id="tag_19_07_03">2.7.3 Appending Redirected Output
<p class="tent">Appended output redirection shall cause the file whose name results from the expansion of word to be opened for
output on the designated file descriptor. The file shall be opened as if the <a href="../functions/open.html"><i>open()
function as defined in the System Interfaces volume of POSIX.1-2024 was called with the O&#95;APPEND flag set. If the file does not
exist, it shall be created.
<p class="tent">The general format for appending redirected output is as follows:
<pre>
<b>&#91;<i>n<b>&#93;<tt>&gt;&gt;<i>word<tt>

<p class="tent">where the optional <i>n represents the file descriptor number. If the number is omitted, the redirection refers
to standard output (file descriptor 1).
<h4><a name="tag_19_07_04" id="tag_19_07_04">2.7.4 Here-Document
<p class="tent">The redirection operators <tt>&#34;&lt;&lt;&#34; and <tt>&#34;&lt;&lt;-&#34; both allow redirection of subsequent lines
read by the shell to the input of a command. The redirected lines are known as a &#34;here-document&#34;.
<p class="tent">The here-document shall be treated as a single word that begins after the next <b>NEWLINE token and continues
until there is a line containing only the delimiter and a &lt;newline&gt;, with no &lt;blank&gt; characters in between. Then the
next here-document starts, if there is one. For the purposes of locating this terminating line, the end of a <i>command&#95;string
operand (see <a href="../utilities/sh.html#"><i>sh) shall be treated as a &lt;newline&gt; character, and the end of the
<i>commands string in <tt>&#36;(<i>commands) and <tt>&#96;<i>commands&#96; may be treated as a &lt;newline&gt;. If the
end of input is reached without finding the terminating line, the shell should, but need not, treat this as a redirection error.
The format is as follows:
<pre>
<b>&#91;<i>n<b>&#93;<tt>&lt;&lt;<i>word
    here-document
delimiter<tt>

<p class="tent">where the optional <i>n represents the file descriptor number. If the number is omitted, the here-document
refers to standard input (file descriptor 0). It is unspecified whether the file descriptor is opened as a regular file or some
other type of file. Portable applications cannot rely on the file descriptor being seekable (see XSH <a href=
"../functions/lseek.html#"><i>lseek()).
<p class="tent">If any part of <i>word is quoted, not counting double-quotes outside a command substitution if the
here-document is inside one, the delimiter shall be formed by performing quote removal on <i>word, and the here-document lines
shall not be expanded. Otherwise:
<ul>
<li class="tent">The delimiter shall be the <i>word itself.
<li class="tent">The removal of &lt;backslash&gt;&lt;newline&gt; for line continuation (see <a href="#tag_19_02_01">2.2.1 Escape
Character (Backslash)) shall be performed during the search for the trailing delimiter. (As a consequence, the trailing
delimiter is not recognized immediately after a &lt;newline&gt; that was removed by line continuation.) It is unspecified whether
the line containing the trailing delimiter is itself subject to this line continuation.
<li class="tent">All lines of the here-document shall be expanded, when the redirection operator is evaluated but after the
trailing delimiter for the here-document has been located, for parameter expansion, command substitution, and arithmetic expansion.
If the redirection operator is never evaluated (because the command it is part of is not executed), the here-document shall be read
without performing any expansions.
<li class="tent">Any &lt;backslash&gt; characters in the input shall behave as the &lt;backslash&gt; inside double-quotes (see
<a href="#tag_19_02_03">2.2.3 Double-Quotes). However, the double-quote character (<tt>&#39;&#34;&#39;) shall not be treated
specially within a here-document, except when the double-quote appears within <tt>&#34;&#36;()&#34;, <tt>&#34;&#96;&#96;&#34;, or
<tt>&#34;&#36;{}&#34;.

<p class="tent">If the redirection operator is <tt>&#34;&lt;&lt;-&#34;, all leading &lt;tab&gt; characters shall be stripped from
input lines after &lt;backslash&gt;&lt;newline&gt; line continuation (when it applies) has been performed, and from the line
containing the trailing delimiter. Stripping of leading &lt;tab&gt; characters shall occur as the here-document is read from the
shell input (and consequently does not affect any &lt;tab&gt; characters that result from expansions).
<p class="tent">If more than one <tt>&#34;&lt;&lt;&#34; or <tt>&#34;&lt;&lt;-&#34; operator is specified on a line, the here-document
associated with the first operator shall be supplied first by the application and shall be read first by the shell.
<p class="tent">When a here-document is read from a terminal device and the shell is interactive, it shall write the contents of
the variable <i>PS2, processed as described in <a href="#tag_19_05_03">2.5.3 Shell Variables, to standard error before
reading each line of input until the delimiter has been recognized.
<hr>
<div class="box"><em>The following sections are informative.
<h5><a name="tag_19_07_04_01" id="tag_19_07_04_01">Examples
<p class="tent">An example of a here-document follows:
<pre>
<tt>cat &lt;&lt;eof1; cat &lt;&lt;eof2
Hi,
eof1
Helene.
eof2

<div class="box"><em>End of informative text.
<hr>
<h4><a name="tag_19_07_05" id="tag_19_07_05">2.7.5 Duplicating an Input File Descriptor
<p class="tent">The redirection operator:
<pre>
<b>&#91;<i>n<b>&#93;<tt>&lt;&amp;<i>word<tt>

<p class="tent">shall duplicate one input file descriptor from another, or shall close one. If <i>word evaluates to one or more
digits, the file descriptor denoted by <i>n, or standard input if <i>n is not specified, shall be made to be a copy of the
file descriptor denoted by <i>word; if the digits in <i>word do not represent an already open file descriptor, a
redirection error shall result (see <a href="#tag_19_08_01">2.8.1 Consequences of Shell Errors); if the file descriptor
denoted by <i>word represents an open file descriptor that is not open for input, a redirection error may result. If
<i>word evaluates to <tt>&#39;-&#39;, file descriptor <i>n, or standard input if <i>n is not specified, shall be closed.
Attempts to close a file descriptor that is not open shall not constitute an error. If <i>word evaluates to something else, the
behavior is unspecified.
<h4><a name="tag_19_07_06" id="tag_19_07_06">2.7.6 Duplicating an Output File Descriptor
<p class="tent">The redirection operator:
<pre>
<b>&#91;<i>n<b>&#93;<tt>&gt;&amp;<i>word<tt>

<p class="tent">shall duplicate one output file descriptor from another, or shall close one. If <i>word evaluates to one or
more digits, the file descriptor denoted by <i>n, or standard output if <i>n is not specified, shall be made to be a copy
of the file descriptor denoted by <i>word; if the digits in <i>word do not represent an already open file descriptor, a
redirection error shall result (see <a href="#tag_19_08_01">2.8.1 Consequences of Shell Errors); if the file descriptor
denoted by <i>word represents an open file descriptor that is not open for output, a redirection error may result. If
<i>word evaluates to <tt>&#39;-&#39;, file descriptor <i>n, or standard output if <i>n is not specified, is closed.
Attempts to close a file descriptor that is not open shall not constitute an error. If <i>word evaluates to something else, the
behavior is unspecified.
<h4><a name="tag_19_07_07" id="tag_19_07_07">2.7.7 Open File Descriptors for Reading and Writing
<p class="tent">The redirection operator:
<pre>
<b>&#91;<i>n<b>&#93;<tt>&lt;&gt;<i>word<tt>

<p class="tent">shall cause the file whose name is the expansion of <i>word to be opened for both reading and writing on the
file descriptor denoted by <i>n, or standard input if <i>n is not specified. If the file does not exist, it shall be
created.
<h3><a name="tag_19_08" id="tag_19_08">2.8 Exit Status and Errors
<h4><a name="tag_19_08_01" id="tag_19_08_01">2.8.1 Consequences of Shell Errors
<p class="tent">Certain errors shall cause the shell to write a diagnostic message to standard error and exit as shown in the
following table:
<center>
<table border="1" cellpadding="3" align="center">
<tr valign="top">
<th align="center">
<p class="tent"><b>Error

<th align="center">
<p class="tent"><b>Non-Interactive<br>
Shell

<th align="center">
<p class="tent"><b>Interactive Shell

<th align="center">
<p class="tent"><b>Shell Diagnostic<br>
Message Required

<tr valign="top">
<td align="left">
<p class="tent">Shell language syntax error

<td align="left">
<p class="tent">shall exit

<td align="left">
<p class="tent">shall not exit

<td align="left">
<p class="tent">yes

<tr valign="top">
<td align="left">
<p class="tent">Special built-in utility error

<td align="left">
<p class="tent">shall exit<sup><small>1

<td align="left">
<p class="tent">shall not exit

<td align="left">
<p class="tent">no<sup><small>2

<tr valign="top">
<td align="left">
<p class="tent">Other utility (not a special<br>
built-in) error

<td align="left">
<p class="tent">shall not exit

<td align="left">
<p class="tent">shall not exit

<td align="left">
<p class="tent">no<sup><small>3

<tr valign="top">
<td align="left">
<p class="tent">Redirection error with<br>
special built-in utilities

<td align="left">
<p class="tent">shall exit

<td align="left">
<p class="tent">shall not exit

<td align="left">
<p class="tent">yes

<tr valign="top">
<td align="left">
<p class="tent">Redirection error with<br>
compound commands

<td align="left">
<p class="tent">shall not exit

<td align="left">
<p class="tent">shall not exit

<td align="left">
<p class="tent">yes

<tr valign="top">
<td align="left">
<p class="tent">Redirection error with<br>
function execution

<td align="left">
<p class="tent">shall not exit

<td align="left">
<p class="tent">shall not exit

<td align="left">
<p class="tent">yes

<tr valign="top">
<td align="left">
<p class="tent">Redirection error with other<br>
utilities (not special built-ins)

<td align="left">
<p class="tent">shall not exit

<td align="left">
<p class="tent">shall not exit

<td align="left">
<p class="tent">yes

<tr valign="top">
<td align="left">
<p class="tent">Variable assignment error

<td align="left">
<p class="tent">shall exit

<td align="left">
<p class="tent">shall not exit

<td align="left">
<p class="tent">yes

<tr valign="top">
<td align="left">
<p class="tent">Expansion error

<td align="left">
<p class="tent">shall exit

<td align="left">
<p class="tent">shall not exit

<td align="left">
<p class="tent">yes

<tr valign="top">
<td align="left">
<p class="tent">Command not found

<td align="left">
<p class="tent">may exit

<td align="left">
<p class="tent">shall not exit

<td align="left">
<p class="tent">yes

<tr valign="top">
<td align="left">
<p class="tent">Unrecoverable read error<br>
when reading commands

<td align="left">
<p class="tent">shall exit<sup><small>4

<td align="left">
<p class="tent">shall exit<sup><small>4

<td align="left">
<p class="tent">yes

Notes:
<ol>
<li class="tent">The shell shall exit only if the special built-in utility is executed directly. If it is executed via the <a href=
"../utilities/command.html"><i>command utility, the shell shall not exit.
<li class="tent">Although special built-ins are part of the shell, a diagnostic message written by a special built-in is not
considered to be a shell diagnostic message, and can be redirected like any other utility.
<li class="tent">The shell is not required to write a diagnostic message, but the utility itself shall write a diagnostic message
if required to do so.
<li class="tent">If an unrecoverable read error occurs when reading commands, other than from the <i>file operand of the
<a href="#dot"><i>dot special built-in, the shell shall execute no further commands (including any already successfully
read but not yet executed) other than any specified in a previously defined EXIT <a href="#trap"><i>trap action. An
unrecoverable read error while reading from the <i>file operand of the <a href="#dot"><i>dot special built-in shall be
treated as a special built-in utility error.

<p class="tent">An expansion error is one that occurs when the shell expansions defined in <a href="#tag_19_06">2.6 Word
Expansions are carried out (for example, <tt>&#34;&#36;{x!y}&#34;, because <tt>&#39;!&#39; is not a valid operator); an implementation
may treat these as syntax errors if it is able to detect them during tokenization, rather than during expansion.
<p class="tent">If any of the errors shown as &#34;shall exit&#34; or &#34;may exit&#34; occur in a subshell environment, the shell shall
(respectively, may) exit from the subshell environment with a non-zero status and continue in the environment from which that
subshell environment was invoked.
<p class="tent">In all of the cases shown in the table where an interactive shell is required not to exit and a non-interactive
shell is required to exit, an interactive shell shall not perform any further processing of the command in which the error
occurred.
<h4><a name="tag_19_08_02" id="tag_19_08_02">2.8.2 Exit Status for Commands
<p class="tent">Each command has an exit status that can influence the behavior of other shell commands. The exit status of
commands that are not utilities is documented in this section. The exit status of the standard utilities is documented in their
respective sections.
<p class="tent">The exit status of a command shall be determined as follows:
<ul>
<li class="tent">If the command is not found, the exit status shall be 127.
<li class="tent">Otherwise, if the command name is found, but it is not an executable utility, the exit status shall be 126.
<li class="tent">Otherwise, if the command terminated due to the receipt of a signal, the shell shall assign it an exit status
greater than 128. The exit status shall identify, in an implementation-defined manner, which signal terminated the command. Note
that shell implementations are permitted to assign an exit status greater than 255 if a command terminates due to a signal.
<li class="tent">Otherwise, the exit status shall be the value obtained by the equivalent of the WEXITSTATUS macro applied to the
status obtained by the <a href="../functions/wait.html"><i>wait() function (as defined in the System Interfaces volume of
POSIX.1-2024). Note that for C programs, this value is equal to the result of performing a modulo 256 operation on the value passed
to <a href="../functions/_Exit.html"><i>&#95;Exit(), <a href="../functions/_exit.html"><i>&#95;exit(), or <a href=
"../functions/exit.html"><i>exit() or returned from <i>main().

<h3><a name="tag_19_09" id="tag_19_09">2.9 Shell Commands
<p class="tent">This section describes the basic structure of shell commands. The following command descriptions each describe a
format of the command that is only used to aid the reader in recognizing the command type, and does not formally represent the
syntax. In particular, the representations include spacing between tokens in some places where &lt;blank&gt;s would not be
necessary (when one of the tokens is an operator). Each description discusses the semantics of the command; for a formal definition
of the command language, consult <a href="#tag_19_10">2.10 Shell Grammar.
<p class="tent">A <i>command is one of the following:
<ul>
<li class="tent">Simple command (see <a href="#tag_19_09_01">2.9.1 Simple Commands)
<li class="tent">Pipeline (see <a href="#tag_19_09_02">2.9.2 Pipelines)
<li class="tent">List compound-list (see <a href="#tag_19_09_03">2.9.3 Lists)
<li class="tent">Compound command (see <a href="#tag_19_09_04">2.9.4 Compound Commands)
<li class="tent">Function definition (see <a href="#tag_19_09_05">2.9.5 Function Definition Command)

<p class="tent">Unless otherwise stated, the exit status of a command shall be that of the last simple command executed by the
command. There shall be no limit on the size of any shell command other than that imposed by the underlying system (memory
constraints, {ARG&#95;MAX}, and so on).
<h4><a name="tag_19_09_01" id="tag_19_09_01">2.9.1 Simple Commands
<p class="tent">A &#34;simple command&#34; is a sequence of optional variable assignments and redirections, in any sequence, optionally
followed by words and redirections.
<h5 class="header4"><a name="tag_19_09_01_01" id="tag_19_09_01_01">2.9.1.1 Order of Processing
<p class="tent">When a given simple command is required to be executed (that is, when any conditional construct such as an AND-OR
list or a <b>case statement has not bypassed the simple command), the following expansions, assignments, and redirections shall
all be performed from the beginning of the command text to the end:
<ol>
<li class="tent">The words that are recognized as variable assignments or redirections according to <a href="#tag_19_10_02">2.10.2
Shell Grammar Rules are saved for processing in steps 3 and 4.
<li class="tent">The first word (if any) that is not a variable assignment or redirection shall be expanded. If any fields remain
following its expansion, the first field shall be considered the command name. If no fields remain, the next word (if any) shall be
expanded, and so on, until a command name is found or no words remain. If there is a command name and it is recognized as a
declaration utility, then any remaining words after the word that expanded to produce the command name, that would be recognized as
a variable assignment in isolation, shall be expanded as a variable assignment (tilde expansion after the first &lt;equals-sign&gt;
and after any unquoted &lt;colon&gt;, parameter expansion, command substitution, arithmetic expansion, and quote removal, but no
field splitting or pathname expansion); while remaining words that would not be a variable assignment in isolation shall be subject
to regular expansion (tilde expansion for only a leading &lt;tilde&gt;, parameter expansion, command substitution, arithmetic
expansion, field splitting, pathname expansion, and quote removal). For all other command names, words after the word that produced
the command name shall be subject only to regular expansion. All fields resulting from the expansion of the word that produced the
command name and the subsequent words, except for the field containing the command name, shall be the arguments for the
command.
<li class="tent">Redirections shall be performed as described in <a href="#tag_19_07">2.7 Redirection.
<li class="tent">Each variable assignment shall be expanded for tilde expansion, parameter expansion, command substitution,
arithmetic expansion, and quote removal prior to assigning the value.

<p class="tent">In the preceding list, the order of steps 3 and 4 may be reversed if no command name results from step 2 or if the
command name matches the name of a special built-in utility; see <a href="#tag_19_15">2.15 Special Built-In Utilities.
<p class="tent">When determining whether a command name is a declaration utility, an implementation may use only lexical analysis.
It is unspecified whether assignment context will be used if the command name would only become recognized as a declaration utility
after word expansions.
<h5 class="header4"><a name="tag_19_09_01_02" id="tag_19_09_01_02">2.9.1.2 Variable Assignments
<p class="tent">Variable assignments shall be performed as follows:
<ul>
<li class="tent">If no command name results, variable assignments shall affect the current execution environment.
<li class="tent">If the command name is not a special built-in utility or function, the variable assignments shall be exported for
the execution environment of the command and shall not affect the current execution environment except as a side-effect of the
expansions performed in step 4. In this case it is unspecified:
<ul>
<li class="tent">Whether or not the assignments are visible for subsequent expansions in step 4
<li class="tent">Whether variable assignments made as side-effects of these expansions are visible for subsequent expansions in
step 4, or in the current shell execution environment, or both

<li class="tent">If the command name is a standard utility implemented as a function (see XBD <a href=
"../basedefs/V1_chap04.html#tag_04_25"><i>4.25 Utility), the effect of variable assignments shall be as if the utility was
not implemented as a function.
<li class="tent">If the command name is a special built-in utility, variable assignments shall affect the current execution
environment before the utility is executed and remain in effect when the command completes; if an assigned variable is further
modified by the utility, the modifications made by the utility shall persist. Unless the <a href="#set"><i>set <b>-a
option is on (see <a href="#tag_19_26">set), it is unspecified:
<ul>
<li class="tent">Whether or not the variables gain the <i>export attribute during the execution of the special built-in
utility
<li class="tent">Whether or not <i>export attributes gained as a result of the variable assignments persist after the
completion of the special built-in utility

<li class="tent">If the command name is a function that is not a standard utility implemented as a function, variable assignments
shall affect the current execution environment during the execution of the function. It is unspecified:
<ul>
<li class="tent">Whether or not the variable assignments persist after the completion of the function
<li class="tent">Whether or not the variables gain the <i>export attribute during the execution of the function
<li class="tent">Whether or not <i>export attributes gained as a result of the variable assignments persist after the
completion of the function (if variable assignments persist after the completion of the function)

<p class="tent">If any of the variable assignments attempt to assign a value to a variable for which the <i>readonly attribute
is set in the current shell environment (regardless of whether the assignment is made in that environment), a variable assignment
error shall occur. See <a href="#tag_19_08_01">2.8.1 Consequences of Shell Errors for the consequences of these errors.
<h5 class="header4"><a name="tag_19_09_01_03" id="tag_19_09_01_03">2.9.1.3 Commands with no Command Name
<p class="tent">If a simple command has no command name after word expansion (see <a href="#tag_19_09_01_01">2.9.1.1 Order of
Processing), any redirections shall be performed in a subshell environment; it is unspecified whether this subshell
environment is the same one as that used for a command substitution within the command. (To affect the current execution
environment, see the <a href="#tag_19_21">exec special built-in.) If any of the redirections performed in the current shell
execution environment fail, the command shall immediately fail with an exit status greater than zero, and the shell shall write an
error message indicating the failure. See <a href="#tag_19_08_01">2.8.1 Consequences of Shell Errors for the consequences of
these failures on interactive and non-interactive shells.
<p class="tent">Additionally, if there is no command name but the command contains a command substitution, the command shall
complete with the exit status of the command substitution whose exit status was the last to be obtained. Otherwise, the command
shall complete with a zero exit status.
<h5 class="header4"><a name="tag_19_09_01_04" id="tag_19_09_01_04">2.9.1.4 Command Search and Execution
<p class="tent">If a simple command has a command name and an optional list of arguments after word expansion (see <a href=
"#tag_19_09_01_01">2.9.1.1 Order of Processing), the following actions shall be performed:
<ol>
<li class="tent">If the command name does not contain any &lt;slash&gt; characters, the first successful step in the following
sequence shall occur:
<ol type="a">
<li class="tent">If the command name matches the name of a special built-in utility, that special built-in utility shall be
invoked.
<li class="tent">If the command name matches the name of a utility listed in the following table, the results are unspecified.
<center>
<table cellpadding="3" align="center">
<tr valign="top">
<td align="left">
<p class="tent"><br>
<i>alloc<br>
<i>autoload<br>
<i>bind<br>
<i>bindkey<br>
<i>builtin<br>
<i>bye<br>
<i>caller<br>
<i>cap<br>
<i>chdir<br>
<i>clone<br>
<i>comparguments<br>
 

<td align="left">
<p class="tent"><br>
<i>compcall<br>
<i>compctl<br>
<i>compdescribe<br>
<i>compfiles<br>
<i>compgen<br>
<i>compgroups<br>
<i>complete<br>
<i>compound<br>
<i>compquote<br>
<i>comptags<br>
<i>comptry<br>
 

<td align="left">
<p class="tent"><br>
<i>compvalues<br>
<i>declare<br>
<i>dirs<br>
<i>disable<br>
<i>disown<br>
<i>dosh<br>
<i>echotc<br>
<i>echoti<br>
<i>enum<br>
<i>float<br>
<i>help<br>
 

<td align="left">
<p class="tent"><br>
<i>history<br>
<i>hist<br>
<i>integer<br>
<i>let<br>
<i>local<br>
<i>login<br>
<i>logout<br>
<i>map<br>
<i>mapfile<br>
<i>nameref<br>
<i>popd<br>
 

<td align="left">
<p class="tent"><br>
<i>print<br>
<i>pushd<br>
<i>readarray<br>
<i>repeat<br>
<i>savehistory<br>
<i>source<br>
<i>shopt<br>
<i>stop<br>
<i>suspend<br>
<i>typeset<br>
<i>whence<br>
 

<li class="tent">If the command name matches the name of a function known to this shell, the function shall be invoked as described
in <a href="#tag_19_09_05">2.9.5 Function Definition Command. If the implementation has provided a standard utility in the
form of a function, and that function definition still exists (i.e. has not been removed using <a href="#unset"><i>unset
<b>-f or replaced via another function definition with the same name), it shall not be recognized at this point. It shall be
invoked in conjunction with the path search in step 1e.
<li class="tent">If the command name matches the name of an intrinsic utility (see <a href=
"../utilities/V3_chap01.html#tag_18_07"><i>1.7 Intrinsic Utilities), that utility shall be invoked.
<li class="tent">Otherwise, the command shall be searched for using the <i>PATH environment variable as described in XBD
<a href="../basedefs/V1_chap08.html#tag_08"><i>8. Environment Variables:
<ol type="i">
<li class="tent">If the search is successful:
<ol type="a">
<li class="tent">If the system has implemented the utility as a built-in or as a shell function, and the built-in or function is
associated with the directory that was most recently tested during the successful <i>PATH search, that built-in or function
shall be invoked.
<li class="tent">Otherwise, the shell shall execute a non-built-in utility as described in <a href="#tag_19_09_01_06">2.9.1.6
Non-built-in Utility Execution.

<p class="tent">Once a utility has been searched for and found (either as a result of this specific search or as part of an
unspecified shell start-up activity), an implementation may remember its location and need not search for the utility again unless
the <i>PATH variable has been the subject of an assignment. If the remembered location fails for a subsequent invocation, the
shell shall repeat the search to find the new location for the utility, if any.

<li class="tent">If the search is unsuccessful, the command shall fail with an exit status of 127 and the shell shall write an
error message.

<li class="tent">If the command name contains at least one &lt;slash&gt;, the shell shall execute a non-built-in utility as
described in <a href="#tag_19_09_01_06">2.9.1.6 Non-built-in Utility Execution.

<h5 class="header4"><a name="tag_19_09_01_05" id="tag_19_09_01_05">2.9.1.5 Standard File Descriptors
<p class="tent">If the utility would be executed with file descriptor 0, 1, or 2 closed, implementations may execute the utility
with the file descriptor open to an unspecified file. If a standard utility or a conforming application is executed with file
descriptor 0 not open for reading or with file descriptor 1 or 2 not open for writing, the environment in which the utility or
application is executed shall be deemed non-conforming, and consequently the utility or application might not behave as described
in this standard.
<h5 class="header4"><a name="tag_19_09_01_06" id="tag_19_09_01_06">2.9.1.6 Non-built-in Utility Execution
When the shell executes a non-built-in utility, if the execution is not being made via the <a href="#exec"><i>exec special
built-in utility, the shell shall execute the utility in a separate utility environment (see <a href="#tag_19_13">2.13 Shell
Execution Environment).
<p class="tent">If the execution is being made via the <a href="#exec"><i>exec special built-in utility, the shell shall
not create a separate utility environment for this execution; the new process image shall replace the current shell execution
environment. If the current shell environment is a subshell environment, the new process image shall replace the subshell
environment and the shell shall continue in the environment from which that subshell environment was invoked.
<p class="tent">In either case, execution of the utility in the specified environment shall be performed as follows:
<ol>
<li class="tent">If the command name does not contain any &lt;slash&gt; characters, the command name shall be searched for using
the <i>PATH environment variable as described in XBD <a href="../basedefs/V1_chap08.html#tag_08"><i>8. Environment
Variables:
<ol type="a">
<li class="tent">If the search is successful, the shell shall execute the utility with actions equivalent to calling the <a href=
"../functions/execl.html"><i>execl() function as defined in the System Interfaces volume of POSIX.1-2024 with the
<i>path argument set to the pathname resulting from the search, <i>arg0 set to the command name, and the remaining <a href=
"../functions/execl.html"><i>execl() arguments set to the command arguments (if any) and the null terminator.
<p class="tent">If the <a href="../functions/execl.html"><i>execl() function fails due to an error equivalent to the
&#91;ENOEXEC&#93; error defined in the System Interfaces volume of POSIX.1-2024, the shell shall execute a command equivalent to having a
shell invoked with the pathname resulting from the search as its first operand, with any remaining arguments passed to the new
shell, except that the value of <tt>&#34;&#36;0&#34; in the new shell may be set to the command name. The shell may apply a heuristic
check to determine if the file to be executed could be a script and may bypass this command execution if it determines that the
file cannot be a script. In this case, it shall write an error message, and the command shall fail with an exit status of 126.
<basefont size="2">
<dl>
<dt><b>Note:
<dd>A common heuristic for rejecting files that cannot be a script is locating a NUL byte prior to a &lt;newline&gt; byte within a
fixed-length prefix of the file. Since <a href="../utilities/sh.html"><i>sh is required to accept input files with
unlimited line lengths, the heuristic check cannot be based on line length.

<basefont size="3">
<p class="tent">It is unspecified whether environment variables that were passed to the shell when it was invoked, but were not
used to initialize shell variables (see <a href="#tag_19_05_03">2.5.3 Shell Variables) because they had invalid names, are
included in the environment passed to <a href="../functions/execl.html"><i>execl() and (if <a href=
"../functions/execl.html"><i>execl() fails as described above) to the new shell.

<li class="tent">If the search is unsuccessful, the command shall fail with an exit status of 127 and the shell shall write an
error message.

<li class="tent">If the command name contains at least one &lt;slash&gt;:
<ol type="a">
<li class="tent">If the named utility exists, the shell shall execute the utility with actions equivalent to calling the <a href=
"../functions/execl.html"><i>execl() function defined in the System Interfaces volume of POSIX.1-2024 with the <i>path
and <i>arg0 arguments set to the command name, and the remaining <a href="../functions/execl.html"><i>execl() arguments
set to the command arguments (if any) and the null terminator.
<p class="tent">If the <a href="../functions/execl.html"><i>execl() function fails due to an error equivalent to the
&#91;ENOEXEC&#93; error, the shell shall execute a command equivalent to having a shell invoked with the command name as its first operand,
with any remaining arguments passed to the new shell. The shell may apply a heuristic check to determine if the file to be executed
could be a script and may bypass this command execution if it determines that the file cannot be a script. In this case, it shall
write an error message, and the command shall fail with an exit status of 126. <basefont size="2">
<dl>
<dt><b>Note:
<dd>A common heuristic for rejecting files that cannot be a script is locating a NUL byte prior to a &lt;newline&gt; byte within a
fixed-length prefix of the file. Since <a href="../utilities/sh.html"><i>sh is required to accept input files with
unlimited line lengths, the heuristic check cannot be based on line length.

<basefont size="3">
<p class="tent">It is unspecified whether environment variables that were passed to the shell when it was invoked, but were not
used to initialize shell variables (see <a href="#tag_19_05_03">2.5.3 Shell Variables) because they had invalid names, are
included in the environment passed to <a href="../functions/execl.html"><i>execl() and (if <a href=
"../functions/execl.html"><i>execl() fails as described above) to the new shell.

<li class="tent">If the named utility does not exist, the command shall fail with an exit status of 127 and the shell shall write
an error message.

<h4><a name="tag_19_09_02" id="tag_19_09_02">2.9.2 Pipelines
<p class="tent">A <i>pipeline is a sequence of one or more commands separated by the control operator <tt>&#39;|&#39;. For each
command but the last, the shell shall connect the standard output of the command to the standard input of the next command as if by
creating a pipe and passing the write end of the pipe as the standard output of the command and the read end of the pipe as the
standard input of the next command.
<p class="tent">The format for a pipeline is:
<pre>
<b>&#91;<tt>!<b>&#93; <i>command1 <b>&#91;<tt> | <i>command2<tt> &#46;&#46;&#46;<b>&#93;<tt>

<p class="tent">If the pipeline begins with the reserved word <b>! and <i>command1 is a subshell command, the application
shall ensure that the <b>( operator at the beginning of <i>command1 is separated from the <b>! by one or more
&lt;blank&gt; characters. The behavior of the reserved word <b>! immediately followed by the <b>( operator is
unspecified.
<p class="tent">The standard output of <i>command1 shall be connected to the standard input of <i>command2. The standard
input, standard output, or both of a command shall be considered to be assigned by the pipeline before any redirection specified by
redirection operators that are part of the command (see <a href="#tag_19_07">2.7 Redirection).
<p class="tent">If the pipeline is not in the background (see <a href="#tag_19_09_03_02">2.9.3.1 Asynchronous AND-OR Lists and
<a href="#tag_19_11">2.11 Job Control), the shell shall wait for the last command specified in the pipeline to complete, and
may also wait for all commands to complete.
<h5><a name="tag_19_09_02_01" id="tag_19_09_02_01">Exit Status
<p class="tent">The exit status of a pipeline shall depend on whether or not the <i>pipefail option (see <a href=
"#tag_19_26">set) is enabled and whether or not the pipeline begins with the <b>! reserved word, as described in the
following table. The <i>pipefail option determines which command in the pipeline the exit status is derived from; the <b>!
reserved word causes the exit status to be the logical NOT of the exit status of that command. The shell shall use the
<i>pipefail setting at the time it begins execution of the pipeline, not the setting at the time it sets the exit status of the
pipeline. (For example, in <tt>command1 | set -o pipefail the exit status of <tt>command1 has no effect on the exit
status of the pipeline, even if the shell executes <tt>set -o pipefail in the current shell environment.)
<center>
<table border="1" cellpadding="3" align="center">
<tr valign="top">
<th align="center">
<p class="tent"><b>pipefail Enabled

<th align="center">
<p class="tent"><b>Begins with !

<th align="center">
<p class="tent"><b>Exit Status

<tr valign="top">
<td align="left">
<p class="tent">no

<td align="left">
<p class="tent">no

<td align="left">
<p class="tent">The exit status of the last (rightmost) command specified in the pipeline.

<tr valign="top">
<td align="left">
<p class="tent">no

<td align="left">
<p class="tent">yes

<td align="left">
<p class="tent">Zero, if the last (rightmost) command in the pipeline returned a non-zero exit status; otherwise, 1.

<tr valign="top">
<td align="left">
<p class="tent">yes

<td align="left">
<p class="tent">no

<td align="left">
<p class="tent">Zero, if all commands in the pipeline returned an exit status of 0; otherwise, the exit status of the last
(rightmost) command specified in the pipeline that returned a non-zero exit status.

<tr valign="top">
<td align="left">
<p class="tent">yes

<td align="left">
<p class="tent">yes

<td align="left">
<p class="tent">Zero, if any command in the pipeline returned a non-zero exit status; otherwise, 1.

<h4><a name="tag_19_09_03" id="tag_19_09_03">2.9.3 Lists
<p class="tent">An <i>AND-OR list is a sequence of one or more pipelines separated by the operators <tt>&#34;&amp;&amp;&#34; and
<tt>&#34;||&#34;.
<p class="tent">A <i>list is a sequence of one or more AND-OR lists separated by the operators <tt>&#39;;&#39; and
<tt>&#39;&amp;&#39;.
<p class="tent">The operators <tt>&#34;&amp;&amp;&#34; and <tt>&#34;||&#34; shall have equal precedence and shall be evaluated with left
associativity. For example, both of the following commands write solely <b>bar to standard output:
<pre>
<tt>false &amp;&amp; echo foo || echo bar
true || echo foo &amp;&amp; echo bar

<p class="tent">A <tt>&#39;;&#39; separator or a <tt>&#39;;&#39; or &lt;newline&gt; terminator shall cause the preceding AND-OR list to
be executed sequentially; an <tt>&#39;&amp;&#39; separator or terminator shall cause asynchronous execution of the preceding AND-OR
list.
<p class="tent">The term &#34;compound-list&#34; is derived from the grammar in <a href="#tag_19_10">2.10 Shell Grammar; it is
equivalent to a sequence of <i>lists, separated by &lt;newline&gt; characters, that can be preceded or followed by an arbitrary
number of &lt;newline&gt; characters.
<hr>
<div class="box"><em>The following sections are informative.
<h5><a name="tag_19_09_03_01" id="tag_19_09_03_01">Examples
<p class="tent">The following is an example that illustrates &lt;newline&gt; characters in compound-lists:
<pre>
<tt>while
    # a couple of &lt;newline&gt;s
<br class="tent">
    # a list
    date &amp;&amp; who || ls; cat file
    # a couple of &lt;newline&gt;s
<br class="tent">
    # another list
    wc file &gt; output &amp; true
<br class="tent">
do
    # 2 lists
    ls
    cat file
done

<div class="box"><em>End of informative text.
<hr>
<h5 class="header4"><a name="tag_19_09_03_02" id="tag_19_09_03_02">2.9.3.1 Asynchronous AND-OR Lists
<p class="tent">If an AND-OR list is terminated by the control operator &lt;ampersand&gt; (<tt>&#39;&amp;&#39;), the shell shall
execute the AND-OR list asynchronously in a subshell environment. This subshell shall execute in the background; that is, the shell
shall not wait for the subshell to terminate before executing the next command (if any); if there are no further commands to
execute, the shell shall not wait for the subshell to terminate before exiting.
<p class="tent">If job control is enabled (see <a href="#tag_19_26">set, <b>-m), the AND-OR list shall become a
job-control background job and a job number shall be assigned to it. If job control is disabled, the AND-OR list may become a
non-job-control background job, in which case a job number shall be assigned to it; if no job number is assigned it shall become a
background command but not a background job.
<p class="tent">A job-control background job can be controlled as described in <a href="#tag_19_11">2.11 Job Control.
<p class="tent">The process ID associated with the asynchronous AND-OR list shall become known in the current shell execution
environment; see <a href="#tag_19_13">2.13 Shell Execution Environment. This process ID shall remain known until any one of
the following occurs (and, unless otherwise specified, may continue to remain known after it occurs).
<ul>
<li class="tent">The process terminates and the application waits for the process ID or the corresponding job ID (see <a href=
"../utilities/wait.html#tag_20_147"><i>wait).
<li class="tent">If the asynchronous AND-OR list did not become a background job: another asynchronous AND-OR list is invoked
before <tt>&#34;&#36;!&#34; (corresponding to the previous asynchronous AND-OR list) is expanded in the current shell execution
environment.
<li class="tent">If the asynchronous AND-OR list became a background job: the <a href="../utilities/jobs.html"><i>jobs
utility reports the termination status of that job.
<li class="tent">If the shell is interactive and the asynchronous AND-OR list became a background job: a message indicating
completion of the corresponding job is written to standard error. If <a href="#set"><i>set <b>-b is enabled, it is
unspecified whether the process ID is removed from the list of known process IDs when the message is written or immediately prior
to when the shell writes the next prompt for input.

<p class="tent">The implementation need not retain more than the {CHILD&#95;MAX} most recent entries in its list of known process IDs
in the current shell execution environment.
<p class="tent">If, and only if, job control is disabled, the standard input for the subshell in which an asynchronous AND-OR list
is executed shall initially be assigned to an open file description that behaves as if <b>/dev/null had been opened for reading
only. This initial assignment shall be overridden by any explicit redirection of standard input within the AND-OR list.
<p class="tent">If the shell is interactive and the asynchronous AND-OR list became a background job, the job number and the
process ID associated with the job shall be written to standard error using the format:
<pre>
<tt>&#34;&#91;%d&#93; %d&#92;n&#34;, &lt;<i>job-number<tt>&gt;, &lt;<i>process-id<tt>&gt;

<p class="tent">If the shell is interactive and the asynchronous AND-OR list did not become a background job, the process ID
associated with the asynchronous AND-OR list shall be written to standard error in an unspecified format.
<h5><a name="tag_19_09_03_03" id="tag_19_09_03_03">Exit Status
<p class="tent">The exit status of an asynchronous AND-OR list shall be zero.
<p class="tent">The exit status of the subshell in which the AND-OR list is asynchronously executed can be obtained using the
<a href="../utilities/wait.html"><i>wait utility.
<h5 class="header4"><a name="tag_19_09_03_04" id="tag_19_09_03_04">2.9.3.2 Sequential AND-OR Lists
<p class="tent">AND-OR lists that are separated by a &lt;semicolon&gt; (<tt>&#39;;&#39;) shall be executed sequentially. The format
for executing AND-OR lists sequentially shall be:
<pre>
<i>aolist1 <b>&#91;<tt>; <i>aolist2<b>&#93;<tt> &#46;&#46;&#46;

<p class="tent">Each AND-OR list shall be expanded and executed in the order specified.
<p class="tent">If job control is enabled, the AND-OR lists shall form all or part of a foreground job that can be controlled as
described in <a href="#tag_19_11">2.11 Job Control.
<h5><a name="tag_19_09_03_05" id="tag_19_09_03_05">Exit Status
<p class="tent">The exit status of a sequential AND-OR list shall be the exit status of the last pipeline in the AND-OR list that
is executed.
<h5 class="header4"><a name="tag_19_09_03_06" id="tag_19_09_03_06">2.9.3.3 AND Lists
<p class="tent">The control operator <tt>&#34;&amp;&amp;&#34; denotes an AND list. The format shall be:
<pre>
<i>command1 <b>&#91;<tt> &amp;&amp; <i>command2<b>&#93;<tt> &#46;&#46;&#46;

<p class="tent">First <i>command1 shall be executed. If its exit status is zero, <i>command2 shall be executed, and so on,
until a command has a non-zero exit status or there are no more commands left to execute. The commands are expanded only if they
are executed.
<h5><a name="tag_19_09_03_07" id="tag_19_09_03_07">Exit Status
<p class="tent">The exit status of an AND list shall be the exit status of the last command that is executed in the list.
<h5 class="header4"><a name="tag_19_09_03_08" id="tag_19_09_03_08">2.9.3.4 OR Lists
<p class="tent">The control operator <tt>&#34;||&#34; denotes an OR List. The format shall be:
<pre>
<i>command1 <b>&#91;<tt> || <i>command2<b>&#93;<tt> &#46;&#46;&#46;

<p class="tent">First, <i>command1 shall be executed. If its exit status is non-zero, <i>command2 shall be executed, and so
on, until a command has a zero exit status or there are no more commands left to execute.
<h5><a name="tag_19_09_03_09" id="tag_19_09_03_09">Exit Status
<p class="tent">The exit status of an OR list shall be the exit status of the last command that is executed in the list.
<h4><a name="tag_19_09_04" id="tag_19_09_04">2.9.4 Compound Commands
<p class="tent">The shell has several programming constructs that are &#34;compound commands&#34;, which provide control flow for
commands. Each of these compound commands has a reserved word or control operator at the beginning, and a corresponding terminator
reserved word or operator at the end. In addition, each can be followed by redirections on the same line as the terminator. Each
redirection shall apply to all the commands within the compound command that do not explicitly override that redirection.
<p class="tent">In the descriptions below, the exit status of some compound commands is stated in terms of the exit status of a
<i>compound-list. The exit status of a <i>compound-list shall be the value that the special parameter <tt>&#39;?&#39; (see
<a href="#tag_19_05_02">2.5.2 Special Parameters) would have immediately after execution of the <i>compound-list.
<h5 class="header4"><a name="tag_19_09_04_01" id="tag_19_09_04_01">2.9.4.1 Grouping Commands
<p class="tent">The format for grouping commands is as follows:
<dl compact>
<dd>
<dt>( <i>compound-list )
<dd>Execute <i>compound-list in a subshell environment; see <a href="#tag_19_13">2.13 Shell Execution Environment.
Variable assignments and built-in commands that affect the environment shall not remain in effect after the list finishes.
<p class="tent">If a character sequence beginning with <tt>&#34;((&#34; would be parsed by the shell as an arithmetic expansion if
preceded by a <tt>&#39;&#36;&#39;, shells which implement an extension whereby <tt>&#34;((<i>expression))&#34; is evaluated as an
arithmetic expression may treat the <tt>&#34;((&#34; as introducing as an arithmetic evaluation instead of a grouping command. A
conforming application shall ensure that it separates the two leading <tt>&#39;(&#39; characters with white space to prevent the shell
from performing an arithmetic evaluation.

<dt>{ <i>compound-list ; }
<dd>Execute <i>compound-list in the current process environment. The semicolon shown here is an example of a control operator
delimiting the <b>} reserved word. Other delimiters are possible, as shown in <a href="#tag_19_10">2.10 Shell Grammar; a
&lt;newline&gt; is frequently used.

<h5><a name="tag_19_09_04_02" id="tag_19_09_04_02">Exit Status
<p class="tent">The exit status of a grouping command shall be the exit status of <i>compound-list.
<h5 class="header4"><a name="tag_19_09_04_03" id="tag_19_09_04_03">2.9.4.2 The for Loop
<p class="tent">The <b>for loop shall execute a sequence of commands for each member in a list of <i>items. The <b>for
loop requires that the reserved words <b>do and <b>done be used to delimit the sequence of commands.
<p class="tent">The format for the <b>for loop is as follows:
<pre>
<tt>for <i>name<tt> <b>&#91;<tt> in <b>&#91;<i>word<tt> &#46;&#46;&#46; <b>&#93;&#93;<tt>
do
    <i>compound-list<tt>
done

<p class="tent">First, the list of words following <b>in shall be expanded to generate a list of items. Then, the variable
<i>name shall be set to each item, in turn, and the <i>compound-list executed each time. If no items result from the
expansion, the <i>compound-list shall not be executed. Omitting:
<pre>
<tt>in <i>word &#46;&#46;&#46;

<p class="tent">shall be equivalent to:
<pre>
<tt>in &#34;&#36;@&#34;

<h5><a name="tag_19_09_04_04" id="tag_19_09_04_04">Exit Status
<p class="tent">If there is at least one item in the list of items, the exit status of a <b>for command shall be the exit
status of the last <i>compound-list executed. If there are no items, the exit status shall be zero.
<h5 class="header4"><a name="tag_19_09_04_05" id="tag_19_09_04_05">2.9.4.3 Case Conditional Construct
<p class="tent">The conditional construct <b>case shall execute the <i>compound-list corresponding to the first
<i>pattern (see <a href="#tag_19_14">2.14 Pattern Matching Notation), if any are present, that is matched by the string
resulting from the tilde expansion, parameter expansion, command substitution, arithmetic expansion, and quote removal of the given
word. The reserved word <b>in shall denote the beginning of the patterns to be matched. Multiple patterns with the same
<i>compound-list shall be delimited by the <tt>&#39;|&#39; symbol. The control operator <tt>&#39;)&#39; terminates a list of patterns
corresponding to a given action. The terminated pattern list and the following <i>compound-list is called a <b>case
statement <i>clause. Each <b>case statement clause, with the possible exception of the last, shall be terminated with
either <tt>&#34;;;&#34; or <tt>&#34;;&amp;&#34;. The <b>case construct terminates with the reserved word <b>esac (<b>case
reversed).<br>
<p class="tent">The format for the <b>case construct is as follows:
<pre>
<tt>case <i>word<tt> in
    <b>&#91;&#91;<tt>(<b>&#93;<i> pattern<b>&#91; <tt>| <i>pattern<b>&#93;<tt> &#46;&#46;&#46; ) <i>compound-list terminator<b>&#93;<tt> &#46;&#46;&#46;
    <b>&#91;&#91;<tt>(<b>&#93;<i> pattern<b>&#91; <tt>| <i>pattern<b>&#93;<tt> &#46;&#46;&#46; ) <i>compound-list<b>&#93;<tt>
esac

<p class="tent">Where <i>terminator is either <tt>&#34;;;&#34; or <tt>&#34;;&amp;&#34; and is optional for the last
<i>compound-list.
<p class="tent">In order from the beginning to the end of the <b>case statement, each <i>pattern that labels a
<i>compound-list shall be subjected to tilde expansion, parameter expansion, command substitution, and arithmetic expansion,
and the result of these expansions shall be compared against the expansion of <i>word, according to the rules described in
<a href="#tag_19_14">2.14 Pattern Matching Notation (which also describes the effect of quoting parts of the pattern). After
the first match, no more patterns in the <b>case statement shall be expanded, and the <i>compound-list of the matching
clause shall be executed. If the <b>case statement clause is terminated by <tt>&#34;;;&#34;, no further clauses shall be examined.
If the <b>case statement clause is terminated by <tt>&#34;;&amp;&#34;, then the <i>compound-list (if any) of each subsequent
clause shall be executed, in order, until either a clause terminated by <tt>&#34;;;&#34; is reached and its <i>compound-list (if
any) executed or there are no further clauses in the <b>case statement. The order of expansion and comparison of multiple
<i>patterns that label a <i>compound-list statement is unspecified.
<h5><a name="tag_19_09_04_06" id="tag_19_09_04_06">Exit Status
<p class="tent">The exit status of <b>case shall be zero if no patterns are matched. Otherwise, the exit status shall be the
exit status of the <i>compound-list of the last clause to be executed.
<h5 class="header4"><a name="tag_19_09_04_07" id="tag_19_09_04_07">2.9.4.4 The if Conditional Construct
<p class="tent">The <b>if command shall execute a <i>compound-list and use its exit status to determine whether to execute
another <i>compound-list.
<p class="tent">The format for the <b>if construct is as follows:
<pre>
<tt>if <i>compound-list<tt>
then
    <i>compound-list<tt>
<b>&#91;<tt>elif <i>compound-list<tt>
then
    <i>compound-list<b>&#93;<tt> &#46;&#46;&#46;
<b>&#91;<tt>else
    <i>compound-list<b>&#93;<tt>
fi

<p class="tent">The <b>if <i>compound-list shall be executed; if its exit status is zero, the <b>then
<i>compound-list shall be executed and the command shall complete. Otherwise, each <b>elif <i>compound-list shall be
executed, in turn, and if its exit status is zero, the <b>then <i>compound-list shall be executed and the command shall
complete. Otherwise, the <b>else <i>compound-list shall be executed.
<h5><a name="tag_19_09_04_08" id="tag_19_09_04_08">Exit Status
<p class="tent">The exit status of the <b>if command shall be the exit status of the <b>then or <b>else
<i>compound-list that was executed, or zero, if none was executed. <basefont size="2">
<dl>
<dt><b>Note:
<dd>Although the exit status of the <b>if or <b>elif <i>compound-list is ignored when determining the exit status of
the <b>if command, it is available through the special parameter <tt>&#39;?&#39; (see <a href="#tag_19_05_02">2.5.2 Special
Parameters) during execution of the next <b>then, <b>elif, or <b>else <i>compound-list (if any is executed) in
the normal way.

<basefont size="3">
<h5 class="header4"><a name="tag_19_09_04_09" id="tag_19_09_04_09">2.9.4.5 The while Loop
<p class="tent">The <b>while loop shall continuously execute one <i>compound-list as long as another <i>compound-list
has a zero exit status.
<p class="tent">The format of the <b>while loop is as follows:
<pre>
<tt>while <i>compound-list-1<tt>
do
    <i>compound-list-2<tt>
done

<p class="tent">The <i>compound-list-1 shall be executed, and if it has a non-zero exit status, the <b>while command shall
complete. Otherwise, the <i>compound-list-2 shall be executed, and the process shall repeat.
<h5><a name="tag_19_09_04_10" id="tag_19_09_04_10">Exit Status
<p class="tent">The exit status of the <b>while loop shall be the exit status of the last <i>compound-list-2 executed, or
zero if none was executed. <basefont size="2">
<dl>
<dt><b>Note:
<dd>Since the exit status of <i>compound-list-1 is ignored when determining the exit status of the <b>while command, it is
not possible to obtain the status of the command that caused the loop to exit, other than via the special parameter <tt>&#39;?&#39;
(see <a href="#tag_19_05_02">2.5.2 Special Parameters) during execution of <i>compound-list-1, for example:
<pre>
<tt>while some&#95;command; st=&#36;?; false; do &#46;&#46;&#46;

<p class="tent">The exit status of <i>compound-list-1 is available through the special parameter <tt>&#39;?&#39; during execution
of <i>compound-list-2, but is known to be zero at that point anyway.

<basefont size="3">
<h5 class="header4"><a name="tag_19_09_04_11" id="tag_19_09_04_11">2.9.4.6 The until Loop
<p class="tent">The <b>until loop shall continuously execute one <i>compound-list as long as another <i>compound-list
has a non-zero exit status.
<p class="tent">The format of the <b>until loop is as follows:
<pre>
<tt>until <i>compound-list-1<tt>
do
    <i>compound-list-2<tt>
done

<p class="tent">The <i>compound-list-1 shall be executed, and if it has a zero exit status, the <b>until command completes.
Otherwise, the <i>compound-list-2 shall be executed, and the process repeats.
<h5><a name="tag_19_09_04_12" id="tag_19_09_04_12">Exit Status
<p class="tent">The exit status of the <b>until loop shall be the exit status of the last <i>compound-list-2 executed, or
zero if none was executed. <basefont size="2">
<dl>
<dt><b>Note:
<dd>Although the exit status of <i>compound-list-1 is ignored when determining the exit status of the <b>until command, it
is available through the special parameter <tt>&#39;?&#39; (see <a href="#tag_19_05_02">2.5.2 Special Parameters) during
execution of <i>compound-list-2 in the normal way.

<basefont size="3">
<h4><a name="tag_19_09_05" id="tag_19_09_05">2.9.5 Function Definition Command
<p class="tent">A function is a user-defined name that is used as a simple command to call a compound command with new positional
parameters. A function is defined with a &#34;function definition command&#34;.
<p class="tent">The format of a function definition command is as follows:
<pre>
<i>fname<tt> ( ) <i>compound-command <b>&#91;<i>io-redirect<tt> &#46;&#46;&#46;<b>&#93;<tt>

<p class="tent">The function is named <i>fname; the application shall ensure that it is a name (see XBD <a href=
"../basedefs/V1_chap03.html#tag_03_216"><i>3.216 Name) and that it is not the name of a special built-in utility. An
implementation may allow other characters in a function name as an extension. The implementation shall maintain separate name
spaces for functions and variables.
<p class="tent">The argument <i>compound-command represents a compound command, as described in <a href="#tag_19_09_04">2.9.4
Compound Commands.
<p class="tent">When the function is declared, none of the expansions in <a href="#tag_19_06">2.6 Word Expansions shall be
performed on the text in <i>compound-command or <i>io-redirect; all expansions shall be performed as normal each time the
function is called. Similarly, the optional <i>io-redirect redirections and any variable assignments within
<i>compound-command shall be performed during the execution of the function itself, not the function definition. See <a href=
"#tag_19_08_01">2.8.1 Consequences of Shell Errors for the consequences of failures of these operations on interactive and
non-interactive shells.
<p class="tent">When a function is executed, it shall have the syntax-error properties described for special built-in utilities in
the first item in the enumerated list at the beginning of <a href="#tag_19_15">2.15 Special Built-In Utilities.
<p class="tent">The <i>compound-command shall be executed whenever the function name is specified as the name of a simple
command (see <a href="#tag_19_09_01_04">2.9.1.4 Command Search and Execution). The operands to the command temporarily shall
become the positional parameters during the execution of the <i>compound-command; the special parameter <tt>&#39;#&#39; also shall
be changed to reflect the number of operands. The special parameter 0 shall be unchanged. When the function completes, the values
of the positional parameters and the special parameter <tt>&#39;#&#39; shall be restored to the values they had before the function
was executed. If the special built-in <a href="#return"><i>return (see <a href="#tag_19_25">return) is executed in the
<i>compound-command, the function completes and execution shall resume with the next command after the function call.
<h5><a name="tag_19_09_05_01" id="tag_19_09_05_01">Exit Status
<p class="tent">The exit status of a function definition shall be zero if the function was declared successfully; otherwise, it
shall be greater than zero. The exit status of a function invocation shall be the exit status of the last command executed by the
function.
<h3><a name="tag_19_10" id="tag_19_10">2.10 Shell Grammar
<p class="tent">The following grammar defines the Shell Command Language. This formal syntax shall take precedence over the
preceding text syntax description.
<h4><a name="tag_19_10_01" id="tag_19_10_01">2.10.1 Shell Grammar Lexical Conventions
<p class="tent">The input language to the shell shall be first recognized at the character level. The resulting tokens shall be
classified by their immediate context according to the following rules (applied in order). These rules shall be used to determine
what a &#34;token&#34; is that is subject to parsing at the token level. The rules for token recognition in <a href="#tag_19_03">2.3
Token Recognition shall apply.
<ol>
<li class="tent">If the token is an operator, the token identifier for that operator shall result.
<li class="tent">If the string consists solely of digits and the delimiter character is one of <tt>&#39;&lt;&#39; or <tt>&#39;&gt;&#39;,
the token identifier <b>IO&#95;NUMBER shall result.
<li class="tent">If the string contains at least three characters, begins with a &lt;left-curly-bracket&gt; (<tt>&#39;{&#39;) and ends
with a &lt;right-curly-bracket&gt; (<tt>&#39;}&#39;), and the delimiter character is one of <tt>&#39;&lt;&#39; or <tt>&#39;&gt;&#39;, the
token identifier <b>IO&#95;LOCATION may result; if the result is not <b>IO&#95;LOCATION, the token identifier <b>TOKEN shall
result.
<li class="tent">Otherwise, the token identifier <b>TOKEN shall result.

<p class="tent">Further distinction on <b>TOKEN is context-dependent. It may be that the same <b>TOKEN yields <b>WORD,
a <b>NAME, an <b>ASSIGNMENT&#95;WORD, or one of the reserved words below, dependent upon the context. Some of the productions
in the grammar below are annotated with a rule number from the following list. When a <b>TOKEN is seen where one of those
annotated productions could be used to reduce the symbol, the applicable rule shall be applied to convert the token identifier type
of the <b>TOKEN to:
<ul>
<li class="tent">The token identifier of the recognized reserved word, for rule 1
<li class="tent">A token identifier acceptable at that point in the grammar, for all other rules

<p class="tent">The reduction shall then proceed based upon the token identifier type yielded by the rule applied. When more than
one rule applies, the highest numbered rule shall apply (which in turn may refer to another rule). (Note that except in rule 7, the
presence of an <tt>&#39;=&#39; in the token has no effect.)
<p class="tent">The <b>WORD tokens shall have the word expansion rules applied to them immediately before the associated
command is executed, not at the time the command is parsed.
<h4><a name="tag_19_10_02" id="tag_19_10_02">2.10.2 Shell Grammar Rules
<ol>
<li class="tent">&#91;Command Name&#93;
<p class="tent">When the <b>TOKEN is exactly a reserved word, the token identifier for that reserved word shall result.
Otherwise, the token <b>WORD shall be returned. Also, if the parser is in any state where only a reserved word could be the
next correct token, proceed as above. <basefont size="2">
<dl>
<dt><b>Note:
<dd>Because at this point quoting characters (&lt;backslash&gt;, single-quote, &lt;quotation-mark&gt;, and the &lt;dollar-sign&gt;
single-quote sequence) are retained in the token, quoted strings cannot be recognized as reserved words. This rule also implies
that reserved words are not recognized except in certain positions in the input, such as after a &lt;newline&gt; or
&lt;semicolon&gt;; the grammar presumes that if the reserved word is intended, it is properly delimited by the user, and does not
attempt to reflect that requirement directly. Also note that line joining is done before tokenization, as described in <a href=
"#tag_19_02_01">2.2.1 Escape Character (Backslash), so escaped &lt;newline&gt; characters are already removed at this
point.

<basefont size="3">
<p class="tent">Rule 1 is not directly referenced in the grammar, but is referred to by other rules, or applies globally.

<li class="tent">&#91;Redirection to or from filename&#93;
<p class="tent">The expansions specified in <a href="#tag_19_07">2.7 Redirection shall occur. As specified there, exactly one
field can result (or the result is unspecified), and there are additional requirements on pathname expansion.

<li class="tent">&#91;Redirection from here-document&#93;
<p class="tent">Quote removal shall be applied to the word to determine the delimiter that is used to find the end of the
here-document that begins after the next &lt;newline&gt;.

<li class="tent">&#91;Case statement termination&#93;
<p class="tent">When the <b>TOKEN is exactly the reserved word <b>esac, the token identifier for <b>esac shall result.
Otherwise, the token <b>WORD shall be returned.

<li class="tent">&#91;<b>NAME in <b>for&#93;
<p class="tent">When the <b>TOKEN meets the requirements for a name (see XBD <a href=
"../basedefs/V1_chap03.html#tag_03_216"><i>3.216 Name), the token identifier <b>NAME shall result. Otherwise, the
token <b>WORD shall be returned.

<li class="tent">&#91;Third word of <b>for and <b>case&#93;
<ol type="a">
<li class="tent">&#91;<b>case only&#93;
<p class="tent">When the <b>TOKEN is exactly the reserved word <b>in, the token identifier for <b>in shall result.
Otherwise, the token <b>WORD shall be returned.

<li class="tent">&#91;<b>for only&#93;
<p class="tent">When the <b>TOKEN is exactly the reserved word <b>in or <b>do, the token identifier for <b>in or
<b>do shall result, respectively. Otherwise, the token <b>WORD shall be returned.

<p class="tent">(For a. and b.: As indicated in the grammar, a <i>linebreak precedes the tokens <b>in and <b>do. If
&lt;newline&gt; characters are present at the indicated location, it is the token after them that is treated in this fashion.)

<li class="tent">&#91;Assignment preceding command name&#93;
<ol type="a">
<li class="tent">&#91;When the first word&#93;
<p class="tent">If the <b>TOKEN is exactly a reserved word, the token identifier for that reserved word shall result.
Otherwise, 7b shall be applied.

<li class="tent">&#91;Not the first word&#93;
<p class="tent">If the <b>TOKEN contains an unquoted (as determined while applying rule 4 from <a href="#tag_19_03">2.3 Token
Recognition) &lt;equals-sign&gt; character that is not part of an embedded parameter expansion, command substitution, or
arithmetic expansion construct (as determined while applying rule 5 from <a href="#tag_19_03">2.3 Token Recognition):
<ul>
<li class="tent">If the <b>TOKEN begins with <tt>&#39;=&#39;, then the token <b>WORD shall be returned.
<li class="tent">If all the characters in the <b>TOKEN preceding the first such &lt;equals-sign&gt; form a valid name (see XBD
<a href="../basedefs/V1_chap03.html#tag_03_216"><i>3.216 Name), the token <b>ASSIGNMENT&#95;WORD shall be returned.
<li class="tent">Otherwise, it is implementation-defined whether the token <b>WORD or <b>ASSIGNMENT&#95;WORD is returned, or
the <b>TOKEN is processed in some other way.

<p class="tent">Otherwise, the token <b>WORD shall be returned.

<p class="tent">If a returned <b>ASSIGNMENT&#95;WORD token begins with a valid name, assignment of the value after the first
&lt;equals-sign&gt; to the name shall occur as specified in <a href="#tag_19_09_01">2.9.1 Simple Commands. If a returned
<b>ASSIGNMENT&#95;WORD token does not begin with a valid name, the way in which the token is processed is unspecified.

<li class="tent">&#91;<b>NAME in function&#93;
<p class="tent">When the <b>TOKEN is exactly a reserved word, the token identifier for that reserved word shall result.
Otherwise, when the <b>TOKEN meets the requirements for a name, the token identifier <b>NAME shall result. Otherwise, rule
7 applies.

<li class="tent">&#91;Body of function&#93;
<p class="tent">Word expansion and assignment shall never occur, even when required by the rules above, when this rule is being
parsed. Each <b>TOKEN that might either be expanded or have assignment applied to it shall instead be returned as a single
<b>WORD consisting only of characters that are exactly the token described in <a href="#tag_19_03">2.3 Token Recognition
.

<br>
<pre>
<tt>/&#42; &#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;-
   The grammar symbols
   &#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;- &#42;/
%token  WORD
%token  ASSIGNMENT&#95;WORD
%token  NAME
%token  NEWLINE
%token  IO&#95;NUMBER
%token  IO&#95;LOCATION
<br class="tent">

<tt>/&#42; The following are the operators (see XBD <a href="../basedefs/V1_chap03.html#tag_03_243"><i>3.243 Operator)
containing more than one character. &#42;/<br>
<pre><tt>
<br class="tent">
%token  AND&#95;IF    OR&#95;IF    DSEMI    SEMI&#95;AND
/&#42;      &#39;&amp;&amp;&#39;      &#39;||&#39;     &#39;;;&#39;     &#39;;&amp;&#39;   &#42;/
<br class="tent">
%token  DLESS  DGREAT  LESSAND  GREATAND  LESSGREAT  DLESSDASH
/&#42;      &#39;&lt;&lt;&#39;   &#39;&gt;&gt;&#39;    &#39;&lt;&amp;&#39;     &#39;&gt;&amp;&#39;      &#39;&lt;&gt;&#39;       &#39;&lt;&lt;-&#39;   &#42;/
<br class="tent">
%token  CLOBBER
/&#42;      &#39;&gt;|&#39;   &#42;/
<br class="tent">
/&#42; The following are the reserved words. &#42;/
<br class="tent">
%token  If    Then    Else    Elif    Fi    Do    Done
/&#42;      &#39;if&#39;  &#39;then&#39;  &#39;else&#39;  &#39;elif&#39;  &#39;fi&#39;  &#39;do&#39;  &#39;done&#39;   &#42;/
<br class="tent">
%token  Case    Esac    While    Until    For
/&#42;      &#39;case&#39;  &#39;esac&#39;  &#39;while&#39;  &#39;until&#39;  &#39;for&#39;   &#42;/
<br class="tent">
/&#42; These are reserved words, not operator tokens, and are
   recognized when reserved words are recognized. &#42;/
<br class="tent">
%token  Lbrace    Rbrace    Bang
/&#42;      &#39;{&#39;       &#39;}&#39;       &#39;!&#39;   &#42;/
<br class="tent">
%token  In
/&#42;      &#39;in&#39;   &#42;/
<br>
<br class="tent">
/&#42; &#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;-
   The Grammar
   &#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;- &#42;/
%start program
%%
program          : linebreak complete&#95;commands linebreak
                 | linebreak
                 ;
complete&#95;commands: complete&#95;commands newline&#95;list complete&#95;command
                 |                                complete&#95;command
                 ;
complete&#95;command : list separator&#95;op
                 | list
                 ;
list             : list separator&#95;op and&#95;or
                 |                   and&#95;or
                 ;
and&#95;or           :                         pipeline
                 | and&#95;or AND&#95;IF linebreak pipeline
                 | and&#95;or OR&#95;IF  linebreak pipeline
                 ;
pipeline         :      pipe&#95;sequence
                 | Bang pipe&#95;sequence
                 ;
pipe&#95;sequence    :                             command
                 | pipe&#95;sequence &#39;|&#39; linebreak command
                 ;
command          : simple&#95;command
                 | compound&#95;command
                 | compound&#95;command redirect&#95;list
                 | function&#95;definition
                 ;
compound&#95;command : brace&#95;group
                 | subshell
                 | for&#95;clause
                 | case&#95;clause
                 | if&#95;clause
                 | while&#95;clause
                 | until&#95;clause
                 ;
subshell         : &#39;(&#39; compound&#95;list &#39;)&#39;
                 ;
compound&#95;list    : linebreak term
                 | linebreak term separator
                 ;
term             : term separator and&#95;or
                 |                and&#95;or
                 ;
for&#95;clause       : For name                                      do&#95;group
                 | For name                       sequential&#95;sep do&#95;group
                 | For name linebreak in          sequential&#95;sep do&#95;group
                 | For name linebreak in wordlist sequential&#95;sep do&#95;group
                 ;
name             : NAME                     /&#42; Apply rule 5 &#42;/
                 ;
in               : In                       /&#42; Apply rule 6 &#42;/
                 ;
wordlist         : wordlist WORD
                 |          WORD
                 ;
case&#95;clause      : Case WORD linebreak in linebreak case&#95;list    Esac
                 | Case WORD linebreak in linebreak case&#95;list&#95;ns Esac
                 | Case WORD linebreak in linebreak              Esac
                 ;
case&#95;list&#95;ns     : case&#95;list case&#95;item&#95;ns
                 |           case&#95;item&#95;ns
                 ;
case&#95;list        : case&#95;list case&#95;item
                 |           case&#95;item
                 ;
case&#95;item&#95;ns     : pattern&#95;list &#39;)&#39; linebreak
                 | pattern&#95;list &#39;)&#39; compound&#95;list
                 ;
case&#95;item        : pattern&#95;list &#39;)&#39; linebreak     DSEMI linebreak
                 | pattern&#95;list &#39;)&#39; compound&#95;list DSEMI linebreak
                 | pattern&#95;list &#39;)&#39; linebreak     SEMI&#95;AND linebreak
                 | pattern&#95;list &#39;)&#39; compound&#95;list SEMI&#95;AND linebreak
                 ;
pattern&#95;list     :                  WORD    /&#42; Apply rule 4 &#42;/
                 |              &#39;(&#39; WORD    /&#42; Do not apply rule 4 &#42;/
                 | pattern&#95;list &#39;|&#39; WORD    /&#42; Do not apply rule 4 &#42;/
                 ;
if&#95;clause        : If compound&#95;list Then compound&#95;list else&#95;part Fi
                 | If compound&#95;list Then compound&#95;list           Fi
                 ;
else&#95;part        : Elif compound&#95;list Then compound&#95;list
                 | Elif compound&#95;list Then compound&#95;list else&#95;part
                 | Else compound&#95;list
                 ;
while&#95;clause     : While compound&#95;list do&#95;group
                 ;
until&#95;clause     : Until compound&#95;list do&#95;group
                 ;
function&#95;definition : fname &#39;(&#39; &#39;)&#39; linebreak function&#95;body
                 ;
function&#95;body    : compound&#95;command                /&#42; Apply rule 9 &#42;/
                 | compound&#95;command redirect&#95;list  /&#42; Apply rule 9 &#42;/
                 ;
fname            : NAME                            /&#42; Apply rule 8 &#42;/
                 ;
brace&#95;group      : Lbrace compound&#95;list Rbrace
                 ;
do&#95;group         : Do compound&#95;list Done           /&#42; Apply rule 6 &#42;/
                 ;
simple&#95;command   : cmd&#95;prefix cmd&#95;word cmd&#95;suffix
                 | cmd&#95;prefix cmd&#95;word
                 | cmd&#95;prefix
                 | cmd&#95;name cmd&#95;suffix
                 | cmd&#95;name
                 ;
cmd&#95;name         : WORD                   /&#42; Apply rule 7a &#42;/
                 ;
cmd&#95;word         : WORD                   /&#42; Apply rule 7b &#42;/
                 ;
cmd&#95;prefix       :            io&#95;redirect
                 | cmd&#95;prefix io&#95;redirect
                 |            ASSIGNMENT&#95;WORD
                 | cmd&#95;prefix ASSIGNMENT&#95;WORD
                 ;
cmd&#95;suffix       :            io&#95;redirect
                 | cmd&#95;suffix io&#95;redirect
                 |            WORD
                 | cmd&#95;suffix WORD
                 ;
redirect&#95;list    :               io&#95;redirect
                 | redirect&#95;list io&#95;redirect
                 ;
io&#95;redirect      :             io&#95;file
                 | IO&#95;NUMBER   io&#95;file
                 | IO&#95;LOCATION io&#95;file /&#42; Optionally supported &#42;/
                 |             io&#95;here
                 | IO&#95;NUMBER   io&#95;here
                 | IO&#95;LOCATION io&#95;here /&#42; Optionally supported &#42;/
                 ;
io&#95;file          : &#39;&lt;&#39;       filename
                 | LESSAND   filename
                 | &#39;&gt;&#39;       filename
                 | GREATAND  filename
                 | DGREAT    filename
                 | LESSGREAT filename
                 | CLOBBER   filename
                 ;
filename         : WORD                      /&#42; Apply rule 2 &#42;/
                 ;
io&#95;here          : DLESS     here&#95;end
                 | DLESSDASH here&#95;end
                 ;
here&#95;end         : WORD                      /&#42; Apply rule 3 &#42;/
                 ;
newline&#95;list     :              NEWLINE
                 | newline&#95;list NEWLINE
                 ;
linebreak        : newline&#95;list
                 | /&#42; empty &#42;/
                 ;
separator&#95;op     : &#39;&amp;&#39;
                 | &#39;;&#39;
                 ;
separator        : separator&#95;op linebreak
                 | newline&#95;list
                 ;
sequential&#95;sep   : &#39;;&#39; linebreak
                 | newline&#95;list
                 ;

<h3><a name="tag_19_11" id="tag_19_11">2.11 Job Control
<p class="tent">Job control is defined (see XBD <a href="../basedefs/V1_chap03.html#tag_03_181"><i>3.181 Job Control) as a
facility that allows users selectively to stop (suspend) the execution of processes and continue (resume) their execution at a
later point. It is jointly supplied by the terminal I/O driver and a command interpreter. The shell is one such command interpreter
and job control in the shell is enabled by <a href="#tag_19_26">set <b>-m (which is enabled by default in interactive
shells). The remainder of this section describes the job control facility provided by the shell. Requirements relating to
background jobs stated in this section only apply to job-control background jobs.
<p class="tent">If the shell has a controlling terminal and it is the controlling process for the terminal session, it shall
initially set the foreground process group ID associated with the terminal to its own process group ID. Otherwise, if it has a
controlling terminal, it shall initially perform the following steps if interactive and may perform them if non-interactive:
<ol>
<li class="tent">If its process group is the foreground process group associated with the terminal, the shell shall set its process
group ID to its process ID (if they are not already equal) and set the foreground process group ID associated with the terminal to
its process group ID.
<li class="tent">If its process group is not the foreground process group associated with the terminal (which would result from it
being started by a job-control shell as a background job), the shell shall either stop itself by sending itself a SIGTTIN signal
or, if interactive, attempt to read from standard input (which generates a SIGTTIN signal if standard input is the controlling
terminal). If it is stopped, then when it continues execution (after receiving a SIGCONT signal) it shall repeat these steps.

<p class="tent">Subsequently, the shell shall change the foreground process group associated with its controlling terminal when a
foreground job is running as noted in the description below.
<p class="tent">When job control is enabled, the shell shall create one or more jobs when it executes a list (see <a href=
"#tag_19_09_03">2.9.3 Lists) that has one of the following forms:
<ul>
<li class="tent">A single asynchronous AND-OR list
<li class="tent">One or more sequentially executed AND-OR lists followed by at most one asynchronous AND-OR list

<p class="tent">For the purposes of job control, a list that includes more than one asynchronous AND-OR list shall be treated as if
it were split into multiple separate lists, each ending with an asynchronous AND-OR list.
<p class="tent">When a job consisting of a single asynchronous AND-OR list is created, it shall form a <i>background job and
the associated process ID shall be that of a child process that is made a process group leader, with all other processes (if any)
that the shell creates to execute the AND-OR list initially having this process ID as their process group ID.
<p class="tent">For a list consisting of one or more sequentially executed AND-OR lists followed by at most one asynchronous AND-OR
list, the whole list shall form a single <i>foreground job up until the sequentially executed AND-OR lists have all completed
execution, at which point the asynchronous AND-OR list (if any) shall form a background job as described above.
<p class="tent">For each pipeline in a foreground job, if the pipeline is executed while the list is still a foreground job, the
set of processes comprising the pipeline, and any processes descended from it, shall all be in the same process group, unless the
shell executes some of the commands in the pipeline in the current shell execution environment and others in a subshell
environment; in this case the process group ID of the current shell need not change (or cannot change if it is the session leader),
and consequently the process group ID that the other processes all share may differ from the process group ID of the current shell
(which means that a SIGSTOP, SIGTSTP, SIGTTIN, or SIGTTOU signal sent to one of those process groups does not cause the whole
pipeline to stop).
<p class="tent">A background job that was created on execution of an asynchronous AND-OR list can be brought into the foreground by
means of the <a href="../utilities/fg.html"><i>fg utility (if supported); in this case the entire job shall become a single
foreground job. If a process that the shell subsequently waits for is part of this foreground job and is stopped by a signal, the
entire job shall become a suspended job and the behavior shall be as if the process had been stopped while the job was running in
the background.
<p class="tent">When a foreground job is created, or a background job is brought into the foreground by the <a href=
"../utilities/fg.html"><i>fg utility, if the shell has a controlling terminal it shall set the foreground process group ID
associated with the terminal as follows:
<ul>
<li class="tent">If the job was originally created as a background job, the foreground process group ID shall be set to the process
ID of the process that the shell made a process group leader when it executed the asynchronous AND-OR list.
<li class="tent">If the job was originally created as a foreground job, the foreground process group ID shall be set as follows
when each pipeline in the job is executed:
<ul>
<li class="tent">If the shell is not itself executing, in the current shell execution environment, all of the commands in the
pipeline, the foreground process group ID shall be set to the process group ID that is shared by the other processes executing the
pipeline (see above).
<li class="tent">If all of the commands in the pipeline are being executed by the shell itself in the current shell execution
environment, the foreground process group ID shall be set to the process group ID of the shell.

<p class="tent">When a foreground job terminates, or becomes a suspended job (see below), if the shell has a controlling terminal
it shall set the foreground process group ID associated with the terminal to the process group ID of the shell.
<p class="tent">Each background job (whether suspended or not) shall have associated with it a job number and a process ID that is
known in the current shell execution environment. When a background job is brought into the foreground by means of the <a href=
"../utilities/fg.html"><i>fg utility, the associated job number shall be removed from the shell&#39;s background jobs list and
the associated process ID shall be removed from the list of process IDs known in the current shell execution environment.
<p class="tent">If a process that the shell is waiting for is part of a foreground job that was started as a foreground job and is
stopped by a catchable signal (SIGTSTP, SIGTTIN, or SIGTTOU):
<ul>
<li class="tent">If the currently executing AND-OR list within the list comprising the foreground job consists of a single pipeline
in which all of the commands are simple commands, the shell shall either create a suspended job consisting of at least that AND-OR
list and the remaining (if any) AND-OR lists in the same list, or create a suspended job consisting of just that AND-OR list and
discard the remaining (if any) AND-OR lists in the same list.
<li class="tent">Otherwise, the shell shall create a suspended job consisting of a set of commands, from within the list comprising
the foreground job, that is unspecified except that the set shall include at least the pipeline to which the stopped process
belongs. Commands in the foreground job that have not already completed and are not included in the suspended job shall be
discarded.

<p class="tent"><basefont size="2">
<dl>
<dt><b>Note:
<dd>Although only a pipeline of simple commands is guaranteed to remain intact if started in the foreground and subsequently
suspended, it is possible to ensure that a complex AND-OR list will remain intact when suspended by starting it in the background
and immediately bringing it into the foreground. For example:
<pre>
<tt>command1 &amp;&amp; command2 | { command3 || command4; } &amp; fg

<basefont size="3">
<p class="tent">If a process that the shell is waiting for is part of a foreground job that was started as a foreground job and is
stopped by a SIGSTOP signal, the behavior shall be as described above for a catchable signal unless the shell was executing a
built-in utility in the current shell execution environment when the SIGSTOP was delivered, resulting in the shell itself being
stopped by the signal, in which case if the shell subsequently receives a SIGCONT signal and has one or more child processes that
remain stopped, the shell shall create a suspended job as if only those child processes had been stopped.
<p class="tent">When a suspended job is created as a result of a foreground job being stopped, it shall be assigned a job number,
and an interactive shell shall write, and a non-interactive shell may write, a message to standard error, formatted as described by
the <a href="../utilities/jobs.html"><i>jobs utility (without the <b>-l option) for a suspended job. The message may
indicate that the commands comprising the job include commands that have already completed; in this case the completed commands
shall not be repeated if execution of the job is subsequently continued. If the shell is interactive, it shall save the terminal
settings before changing them to the settings it needs to read further commands.
<p class="tent">When a process associated with a background job is stopped by a SIGSTOP, SIGTSTP, SIGTTIN, or SIGTTOU signal, the
shell shall convert the (non-suspended) background job into a suspended job and an interactive shell shall write a message to
standard error, formatted as described by the <a href="../utilities/jobs.html"><i>jobs utility (without the <b>-l
option) for a suspended job, at the following time:
<ul>
<li class="tent">If <a href="#set"><i>set <b>-b is enabled, the message shall be written either immediately after the
job became suspended or immediately prior to writing the next prompt for input.
<li class="tent">If <a href="#set"><i>set <b>-b is disabled, the message shall be written immediately prior to writing
the next prompt for input.

<p class="tent">Execution of a suspended job can be continued as a foreground job by means of the <a href=
"../utilities/fg.html"><i>fg utility (if supported), or as a (non-suspended) background job either by means of the <a href=
"../utilities/bg.html"><i>bg utility (if supported) or by sending the stopped processes a SIGCONT signal. The <a href=
"../utilities/fg.html"><i>fg and <a href="../utilities/bg.html"><i>bg utilities shall send a SIGCONT signal to the
process group of the process(es) whose stopped wait status caused the shell to suspend the job. If the shell has a controlling
terminal, the <a href="../utilities/fg.html"><i>fg utility shall send the SIGCONT signal after it has set the foreground
process group ID associated with the terminal (see above). If the <a href="../utilities/fg.html"><i>fg utility is used from
an interactive shell to bring into the foreground a suspended job that was created from a foreground job, before it sends the
SIGCONT signal the <a href="../utilities/fg.html"><i>fg utility shall restore the terminal settings to the ones that the
shell saved when the job was suspended.
<p class="tent">When a background job completes or is terminated by a signal, an interactive shell shall write a message to
standard error, formatted as described by the <a href="../utilities/jobs.html"><i>jobs utility (without the <b>-l
option) for a job that completed or was terminated by a signal, respectively, at the following time:
<ul>
<li class="tent">If <a href="#set"><i>set <b>-b is enabled, the message shall be written immediately after the job
completes or is terminated.
<li class="tent">If <a href="#set"><i>set <b>-b is disabled, the message shall be written immediately prior to writing
the next prompt for input.

<p class="tent">In each case above where an interactive shell writes a message immediately prior to writing the next prompt for
input, the same message may also be written by a non-interactive shell, at any of the following times:
<ul>
<li class="tent">After the next time a foreground job terminates or is suspended
<li class="tent">Before the shell parses further input
<li class="tent">Before the shell exits

<h3><a name="tag_19_12" id="tag_19_12">2.12 Signals and Error Handling
<p class="tent">If job control is disabled (see the description of <a href="#set"><i>set <b>-m) when the shell executes
an asynchronous AND-OR list, the commands in the list shall inherit from the shell a signal action of ignored (SIG&#95;IGN) for the
SIGINT and SIGQUIT signals. In all other cases, commands executed by the shell shall inherit the same signal actions as those
inherited by the shell from its parent unless a signal action is modified by the <a href="#trap"><i>trap special built-in
(see <a href="#tag_19_29">trap)
<p class="tent">When a signal for which a trap has been set is received while the shell is waiting for the completion of a utility
executing a foreground command, the trap associated with that signal shall not be executed until after the foreground command has
completed. When the shell is waiting, by means of the <a href="../utilities/wait.html"><i>wait utility, for asynchronous
commands to complete, the reception of a signal for which a trap has been set shall cause the <a href=
"../utilities/wait.html"><i>wait utility to return immediately with an exit status &gt;128, immediately after which the
trap associated with that signal shall be taken.
<p class="tent">If multiple signals are pending for the shell for which there are associated trap actions, the order of execution
of trap actions is unspecified.
<h3><a name="tag_19_13" id="tag_19_13">2.13 Shell Execution Environment
<p class="tent">A shell execution environment consists of the following:
<ul>
<li class="tent">Open files inherited upon invocation of the shell, plus open files controlled by <a href=
"#exec"><i>exec
<li class="tent">Working directory as set by <a href="../utilities/cd.html"><i>cd
<li class="tent">File creation mask set by <a href="../utilities/umask.html"><i>umask
<li class="tent">File size limit as set by <a href="../utilities/ulimit.html"><i>ulimit
<li class="tent">Current traps set by <a href="#trap"><i>trap
<li class="tent">Shell parameters that are set by variable assignment (see the <a href="#tag_19_26">set special built-in) or
from the System Interfaces volume of POSIX.1-2024 environment inherited by the shell when it begins (see the <a href=
"#tag_19_23">export special built-in)
<li class="tent">Shell functions; see <a href="#tag_19_09_05">2.9.5 Function Definition Command
<li class="tent">Options turned on at invocation or by <a href="#set"><i>set
<li class="tent">Background jobs and their associated process IDs, and process IDs of child processes created to execute
asynchronous AND-OR lists while job control is disabled; together these process IDs constitute the process IDs &#34;known to this
shell environment&#34;. If the implementation supports non-job-control background jobs, the list of known process IDs and the list of
background jobs may form a single list even though this standard describes them as being updated separately. See <a href=
"#tag_19_09_03_02">2.9.3.1 Asynchronous AND-OR Lists
<li class="tent">Shell aliases; see <a href="#tag_19_03_01">2.3.1 Alias Substitution

<p class="tent">Utilities other than the special built-ins (see <a href="#tag_19_15">2.15 Special Built-In Utilities) shall be
invoked in a separate environment that consists of the following. The initial value of these objects shall be the same as that for
the parent shell, except as noted below.
<ul>
<li class="tent">Open files inherited on invocation of the shell, open files controlled by the <a href="#exec"><i>exec
special built-in plus any modifications, and additions specified by any redirections to the utility
<li class="tent">Current working directory
<li class="tent">File creation mask
<li class="tent">If the utility is a shell script, traps caught by the shell shall be set to the default values and traps ignored
by the shell shall be set to be ignored by the utility; if the utility is not a shell script, the trap actions (default or ignore)
shall be mapped into the appropriate signal handling actions for the utility
<li class="tent">Variables with the <a href="#export"><i>export attribute, along with those explicitly exported for the
duration of the command, shall be passed to the utility environment variables
<li class="tent">It is unspecified whether environment variables that were passed to the invoking shell when it was invoked itself,
but were not used to initialize shell variables (see <a href="#tag_19_05_03">2.5.3 Shell Variables) because they had invalid
names, are included in the invoked utility&#39;s environment.

<p class="tent">The environment of the shell process shall not be changed by the utility unless explicitly specified by the utility
description (for example, <a href="../utilities/cd.html"><i>cd and <a href="../utilities/umask.html"><i>umask).
<p class="tent">A subshell environment shall be created as a duplicate of the shell environment, except that:
<ul>
<li class="tent">Unless specified otherwise (see <a href="#tag_19_29">trap), traps that are not being ignored shall be set to
the default action.
<li class="tent">If the shell is interactive, the subshell shall behave as a non-interactive shell in all respects except:
<ul>
<li class="tent">The expansion of the special parameter <tt>&#39;-&#39; may continue to indicate that it is interactive.
<li class="tent">The <a href="#set"><i>set <b>-n option may be ignored.

<p class="tent">Changes made to the subshell environment shall not affect the shell environment. Command substitution, commands
that are grouped with parentheses, and asynchronous AND-OR lists shall be executed in a subshell environment. Additionally, each
command of a multi-command pipeline is in a subshell environment; as an extension, however, any or all commands in a pipeline may
be executed in the current environment. Except where otherwise stated, all other commands shall be executed in the current shell
environment.
<h3><a name="tag_19_14" id="tag_19_14">2.14 Pattern Matching Notation
<p class="tent">The pattern matching notation described in this section is used to specify patterns for matching character strings
in the shell. This notation is also used by some other utilities (<a href="../utilities/find.html"><i>find, <a href=
"../utilities/pax.html"><i>pax, and optionally <a href="../utilities/make.html"><i>make) and by some system
interfaces (<a href="../functions/fnmatch.html"><i>fnmatch(), <a href="../functions/glob.html"><i>glob(), and
<a href="../functions/wordexp.html"><i>wordexp()). Historically, pattern matching notation is related to, but slightly
different from, the regular expression notation described in XBD <a href="../basedefs/V1_chap09.html#tag_09"><i>9. Regular
Expressions. For this reason, the description of the rules for this pattern matching notation are based on the description
of regular expression notation, modified to account for the differences.
<p class="tent">If an attempt is made to use pattern matching notation to match a string that contains one or more bytes that do
not form part of a valid character, the behavior is unspecified. Since pathnames can contain such bytes, portable applications need
to ensure that the current locale is the C or POSIX locale when performing pattern matching (or expansion) on arbitrary
pathnames.
<h4><a name="tag_19_14_01" id="tag_19_14_01">2.14.1 Patterns Matching a Single Character
<p class="tent">The following patterns shall match a single character: ordinary characters, special pattern characters, and pattern
bracket expressions. The pattern bracket expression also shall match a single collating element.
<p class="tent">In a pattern, or part of one, where a shell-quoting &lt;backslash&gt; can be used, a &lt;backslash&gt; character
shall escape the following character as described in <a href="#tag_19_02_01">2.2.1 Escape Character (Backslash), regardless of
whether or not the &lt;backslash&gt; is inside a bracket expression. (The sequence <tt>&#34;&#92;&#92;&#34; represents one literal
&lt;backslash&gt;.)
<p class="tent">In a pattern, or part of one, where a shell-quoting &lt;backslash&gt; cannot be used to preserve the literal value
of a character that would otherwise be treated as special:
<ul>
<li class="tent">A &lt;backslash&gt; character that is not inside a bracket expression shall preserve the literal value of the
following character, unless the following character is in a part of the pattern where shell quoting can be used and is a shell
quoting character, in which case the behavior is unspecified.
<li class="tent">For the shell only, it is unspecified whether or not a &lt;backslash&gt; character inside a bracket expression
preserves the literal value of the following character.

<p class="tent">All of the requirements and effects of quoting on ordinary, shell special, and special pattern characters shall
apply to escaping in this context, except where specified otherwise. (Situations where this applies include word expansions when a
pattern used in pathname expansion is not present in the original word but results from an earlier expansion, or the argument to
the <a href="../utilities/find.html"><i>find -<i>name or -<i>path primary as passed to <a href=
"../utilities/find.html"><i>find, or the <i>pattern argument to the <a href=
"../functions/fnmatch.html"><i>fnmatch() and <a href="../functions/glob.html"><i>glob() functions when FNM&#95;NOESCAPE
or GLOB&#95;NOESCAPE is not set in <i>flags, respectively.)
<p class="tent">If a pattern ends with an unescaped &lt;backslash&gt;, the behavior is unspecified.
<p class="tent">An ordinary character is a pattern that shall match itself. In a pattern, or part of one, where a shell-quoting
&lt;backslash&gt; can be used, an ordinary character can be any character in the supported character set except for NUL, those
special shell characters in <a href="#tag_19_02">2.2 Quoting that require quoting, and the three special pattern characters
described below. In a pattern, or part of one, where a shell-quoting &lt;backslash&gt; cannot be used to preserve the literal value
of a character that would otherwise be treated as special, an ordinary character can be any character in the supported character
set except for NUL and the three special pattern characters described below. Matching shall be based on the bit pattern used for
encoding the character, not on the graphic representation of the character. If any character (ordinary, shell special, or pattern
special) is quoted, or escaped with a &lt;backslash&gt;, that pattern shall match the character itself. The application shall
ensure that it quotes or escapes any character that would otherwise be treated as special, in order for it to be matched as an
ordinary character.
<p class="tent">When unquoted, unescaped, and not inside a bracket expression, the following three characters shall have special
meaning in the specification of patterns:
<dl compact>
<dd>
<dt><tt>?
<dd>A &lt;question-mark&gt; is a pattern that shall match any character.
<dt><tt>&#42;
<dd>An &lt;asterisk&gt; is a pattern that shall match multiple characters, as described in <a href="#tag_19_14_02">2.14.2 Patterns
Matching Multiple Characters.
<dt><tt>&#91;
<dd>A &lt;left-square-bracket&gt; shall introduce a bracket expression if the characters following it meet the requirements for
bracket expressions stated in XBD <a href="../basedefs/V1_chap09.html#tag_09_03_05"><i>9.3.5 RE Bracket Expression, except
that the &lt;exclamation-mark&gt; character (<tt>&#39;!&#39;) shall replace the &lt;circumflex&gt; character (<tt>&#39;^&#39;) in its
role in a non-matching list in the regular expression notation. A bracket expression starting with an unquoted &lt;circumflex&gt;
character produces unspecified results. A &lt;left-square-bracket&gt; that does not introduce a valid bracket expression shall
match the character itself.

<h4><a name="tag_19_14_02" id="tag_19_14_02">2.14.2 Patterns Matching Multiple Characters
<p class="tent">The following rules are used to construct patterns matching multiple characters from patterns matching a single
character:
<ol>
<li class="tent">The &lt;asterisk&gt; (<tt>&#39;&#42;&#39;) is a pattern that shall match any string, including the null string.
<li class="tent">The concatenation of patterns matching a single character is a valid pattern that shall match the concatenation of
the single characters or collating elements matched by each of the concatenated patterns.
<li class="tent">The concatenation of one or more patterns matching a single character with one or more &lt;asterisk&gt; characters
is a valid pattern. In such patterns, each &lt;asterisk&gt; shall match a string of zero or more characters, matching the greatest
possible number of characters that still allows the remainder of the pattern to match the string.

<h4><a name="tag_19_14_03" id="tag_19_14_03">2.14.3 Patterns Used for Filename Expansion
<p class="tent">The rules described so far in <a href="#tag_19_14_01">2.14.1 Patterns Matching a Single Character and <a href=
"#tag_19_14_02">2.14.2 Patterns Matching Multiple Characters are qualified by the following rules that apply when pattern
matching notation is used for filename expansion:
<ol>
<li class="tent">The &lt;slash&gt; character in a pathname shall be explicitly matched by using one or more &lt;slash&gt;
characters in the pattern; it shall neither be matched by the &lt;asterisk&gt; or &lt;question-mark&gt; special characters nor by a
bracket expression. &lt;slash&gt; characters in the pattern shall be identified before bracket expressions; thus, a &lt;slash&gt;
cannot be included in a pattern bracket expression used for filename expansion. If a &lt;slash&gt; character is found following an
unescaped &lt;left-square-bracket&gt; character before a corresponding &lt;right-square-bracket&gt; is found, the open bracket
shall be treated as an ordinary character. For example, the pattern <tt>&#34;a&#91;b/c&#93;d&#34; does not match such pathnames as <b>abd
or <b>a/d. It only matches a pathname of literally <b>a&#91;b/c&#93;d.
<li class="tent">If a filename begins with a &lt;period&gt; (<tt>&#39;.&#39;), the &lt;period&gt; shall be explicitly matched by using
a &lt;period&gt; as the first character of the pattern or immediately following a &lt;slash&gt; character. The leading
&lt;period&gt; shall not be matched by:
<ul>
<li class="tent">The &lt;asterisk&gt; or &lt;question-mark&gt; special characters
<li class="tent">A bracket expression containing a non-matching list, such as <tt>&#34;&#91;!a&#93;&#34;, a range expression, such as
<tt>&#34;&#91;%-0&#93;&#34;, or a character class expression, such as <tt>&#34;&#91;&#91;:punct:&#93;&#93;&#34;

<p class="tent">It is unspecified whether an explicit &lt;period&gt; in a bracket expression matching list, such as
<tt>&#34;&#91;.abc&#93;&#34;, can match a leading &lt;period&gt; in a filename.

<li class="tent">If a specified pattern contains any <tt>&#39;&#42;&#39;, <tt>&#39;?&#39; or <tt>&#39;&#91;&#39; characters that will be treated as
special (see <a href="#tag_19_14_01">2.14.1 Patterns Matching a Single Character), it shall be matched against existing
filenames and pathnames, as appropriate; if directory entries for dot and dot-dot exist, they may be ignored. Each component that
contains any such characters shall require read permission in the directory containing that component. Each component that contains
a &lt;backslash&gt; that will be treated as special may require read permission in the directory containing that component. Any
component, except the last, that does not contain any <tt>&#39;&#42;&#39;, <tt>&#39;?&#39; or <tt>&#39;&#91;&#39; characters that will be treated as
special shall require search permission. If these permissions are denied, or if an attempt to open or search a pathname as a
directory, or an attempt to read an opened directory, fails because of an error condition that is related to file system contents,
this shall not be considered an error and pathname expansion shall continue as if the pathname had named an existing directory
which had been successfully opened and read, or searched, and no matching directory entries had been found in it. For other error
conditions it is unspecified whether pathname expansion fails or they are treated the same as when permission is denied.
<p class="tent">For example, given the pattern:
<pre>
<tt>/foo/bar/x&#42;/bam

<p class="tent">search permission is needed for directories <b>/ and <b>foo, search and read permissions are needed for
directory <b>bar, and search permission is needed for each <b>x&#42; directory.
<p class="tent">If the pattern matches any existing filenames or pathnames, the pattern shall be replaced with those filenames and
pathnames, sorted according to the collating sequence in effect in the current locale. If this collating sequence does not have a
total ordering of all characters (see XBD <a href="../basedefs/V1_chap07.html#tag_07_03_02"><i>7.3.2 LC&#95;COLLATE), any
filenames or pathnames that collate equally shall be further compared byte-by-byte using the collating sequence for the POSIX
locale.
<p class="tent">If the pattern contains an open bracket (<tt>&#39;&#91;&#39;) that does not introduce a bracket expression as in XBD
<a href="../basedefs/V1_chap09.html#tag_09_03_05"><i>9.3.5 RE Bracket Expression, it is unspecified whether other unquoted
<tt>&#39;&#42;&#39;, <tt>&#39;?&#39;, <tt>&#39;&#91;&#39; or &lt;backslash&gt; characters within the same slash-delimited component of the pattern
retain their special meanings or are treated as ordinary characters. For example, the pattern <tt>&#34;a&#42;&#91;/b&#42;&#34; may match all
filenames beginning with <tt>&#39;b&#39; in the directory <tt>&#34;a&#42;&#91;&#34; or it may match all filenames beginning with <tt>&#39;b&#39; in
all directories with names beginning with <tt>&#39;a&#39; and ending with <tt>&#39;&#91;&#39;.
<p class="tent">If the pattern does not match any existing filenames or pathnames, the pattern string shall be left unchanged.
<basefont size="2">
<dl>
<dt><b>Note:
<dd>A future version of this standard may require that directory entries for dot and dot-dot are ignored (if they exist) when
matching patterns against existing filenames. For example, when expanding the pattern <tt>&#34;.&#42;&#34; the result would not include
dot and dot-dot.

<basefont size="3">
<li class="tent">If a specified pattern does not contain any <tt>&#39;&#42;&#39;, <tt>&#39;?&#39; or <tt>&#39;&#91;&#39; characters that will be
treated as special, the pattern string shall be left unchanged.

<h3><a name="tag_19_15" id="tag_19_15">2.15 Special Built-In Utilities
<p class="tent">The following &#34;special built-in&#34; utilities shall be supported in the shell command language. The output of each
command, if any, shall be written to standard output, subject to the normal redirection and piping possible with all commands.
<p class="tent">The term &#34;built-in&#34; implies that there is no need to execute a separate executable file because the utility is
implemented in the shell itself. An implementation may choose to make any utility a built-in; however, the special built-in
utilities described here differ from regular built-in utilities in two respects:
<ol>
<li class="tent">An error in a special built-in utility may cause a shell executing that utility to abort, while an error in a
regular built-in utility shall not cause a shell executing that utility to abort. (See <a href="#tag_19_08_01">2.8.1 Consequences
of Shell Errors for the consequences of errors on interactive and non-interactive shells.) If a special built-in utility
encountering an error does not abort the shell, its exit value shall be non-zero.
<li class="tent">As described in <a href="#tag_19_09_01">2.9.1 Simple Commands, variable assignments preceding the invocation
of a special built-in utility affect the current execution environment; this shall not be the case with a regular built-in or other
utility.

<p class="tent">The special built-in utilities in this section need not be provided in a manner accessible via the <i>exec
family of functions defined in the System Interfaces volume of POSIX.1-2024.
<p class="tent">Some of the special built-ins are described as conforming to XBD <a href=
"../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines. For those that are not, the requirement in
<a href="../utilities/V3_chap01.html#tag_18_04"><i>1.4 Utility Description Defaults that <tt>&#34;&#45;&#45;&#34; be recognized as a
first argument to be discarded does not apply and a conforming application shall not use that argument.

<a name="break" id="break"> <a name="tag_19_16" id="tag_19_16"><!-- break -->
<h4 class="mansect"><a name="tag_19_16_01" id="tag_19_16_01">NAME
<blockquote>break — exit from for, while, or until loop
<h4 class="mansect"><a name="tag_19_16_02" id="tag_19_16_02">SYNOPSIS
<blockquote class="synopsis">
<p><code><tt>break <b>&#91;<i>n<b>&#93;

<h4 class="mansect"><a name="tag_19_16_03" id="tag_19_16_03">DESCRIPTION
<blockquote>
<p>If <i>n is specified, the <a href="#break"><i>break utility shall exit from the <i>nth enclosing <b>for,
<b>while, or <b>until loop. If <i>n is not specified, <a href="#break"><i>break shall behave as if <i>n was
specified as 1. Execution shall continue with the command immediately following the exited loop. The application shall ensure that
the value of <i>n is a positive decimal integer. If <i>n is greater than the number of enclosing loops, the outermost
enclosing loop shall be exited. If there is no enclosing loop, the behavior is unspecified.
<p class="tent">A loop shall enclose a <i>break or <i>continue command if the loop lexically encloses the command. A loop
lexically encloses a <i>break or <i>continue command if the command is:
<ul>
<li class="tent">Executing in the same execution environment (see <a href="#tag_19_13">2.13 Shell Execution Environment) as
the compound-list of the loop&#39;s do-group (see <a href="#tag_19_10_02">2.10.2 Shell Grammar Rules), and
<li class="tent">Contained in a compound-list associated with the loop (either in the compound-list of the loop&#39;s do-group or, if
the loop is a <b>while or <b>until loop, in the compound-list following the <b>while or <b>until reserved word),
and
<li class="tent">Not in the body of a function whose function definition command (see <a href="#tag_19_09_05">2.9.5 Function
Definition Command) is contained in a compound-list associated with the loop.

<p class="tent">If <i>n is greater than the number of lexically enclosing loops and there is a non-lexically enclosing loop in
progress in the same execution environment as the <i>break or <i>continue command, it is unspecified whether that loop
encloses the command.

<h4 class="mansect"><a name="tag_19_16_04" id="tag_19_16_04">OPTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_16_05" id="tag_19_16_05">OPERANDS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_16_06" id="tag_19_16_06">STDIN
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_16_07" id="tag_19_16_07">INPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_16_08" id="tag_19_16_08">ENVIRONMENT VARIABLES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_16_09" id="tag_19_16_09">ASYNCHRONOUS EVENTS
<blockquote>
<p>Default.

<h4 class="mansect"><a name="tag_19_16_10" id="tag_19_16_10">STDOUT
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_16_11" id="tag_19_16_11">STDERR
<blockquote>
<p>The standard error shall be used only for diagnostic messages.

<h4 class="mansect"><a name="tag_19_16_12" id="tag_19_16_12">OUTPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_16_13" id="tag_19_16_13">EXTENDED DESCRIPTION
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_16_14" id="tag_19_16_14">EXIT STATUS
<blockquote>
<dl compact>
<dd>
<dt> 0
<dd>Successful completion.
<dt>&gt;0
<dd>The <i>n value was not an unsigned decimal integer greater than or equal to 1.

<h4 class="mansect"><a name="tag_19_16_15" id="tag_19_16_15">CONSEQUENCES OF ERRORS
<blockquote>
<p>Default.

<hr>
<div class="box"><em>The following sections are informative.
<h4 class="mansect"><a name="tag_19_16_16" id="tag_19_16_16">APPLICATION USAGE
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_16_17" id="tag_19_16_17">EXAMPLES
<blockquote>
<pre>
<tt>for i in &#42;
do
    if test -d &#34;&#36;i&#34;
    then break
    fi
done

<p class="tent">The results of running the following example are unspecified: there are two loops in progress when the <a href=
"#break"><i>break command is executed, and they are in the same execution environment, but neither loop is lexically
enclosing the <a href="#break"><i>break command. (There are no loops lexically enclosing the <a href=
"#continue"><i>continue commands, either.)
<pre>
<tt>foo() {
    for j in 1 2; do
        echo &#39;break 2&#39; &gt;/tmp/do&#95;break
        echo &#34;  sourcing /tmp/do&#95;break (&#36;j)&#46;&#46;&#46;&#34;
        # the behavior of the break from running the following command
        # results in unspecified behavior:
        . /tmp/do&#95;break
<br class="tent">
        do&#95;continue() { continue 2; }
        echo &#34;  running do&#95;continue (&#36;j)&#46;&#46;&#46;&#34;
        # the behavior of the continue in the following function call
        # results in unspecified behavior (if execution reaches this
        # point):
        do&#95;continue
<br class="tent">
        trap &#39;continue 2&#39; USR1
        echo &#34;  sending SIGUSR1 to self (&#36;j)&#46;&#46;&#46;&#34;
        # the behavior of the continue in the trap invoked from the
        # following signal results in unspecified behavior (if
        # execution reaches this point):
        kill -s USR1 &#36;&#36;
        sleep 1
    done
}
for i in 1 2; do
    echo &#34;running foo (&#36;i)&#46;&#46;&#46;&#34;
    foo
done

<h4 class="mansect"><a name="tag_19_16_18" id="tag_19_16_18">RATIONALE
<blockquote>
<p>In early proposals, consideration was given to expanding the syntax of <a href="#break"><i>break and <a href=
"#continue"><i>continue to refer to a label associated with the appropriate loop as a preferable alternative to the
<i>n method. However, this volume of POSIX.1-2024 does reserve the name space of command names ending with a &lt;colon&gt;. It
is anticipated that a future implementation could take advantage of this and provide something like:
<pre>
<tt>outofloop: for i in a b c d e
do
    for j in 0 1 2 3 4 5 6 7 8 9
    do
        if test -r &#34;&#36;{i}&#36;{j}&#34;
        then break outofloop
        fi
    done
done

<p class="tent">and that this might be standardized after implementation experience is achieved.

<h4 class="mansect"><a name="tag_19_16_19" id="tag_19_16_19">FUTURE DIRECTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_16_20" id="tag_19_16_20">SEE ALSO
<blockquote>
<p><a href="#tag_19_15">2.15 Special Built-In Utilities

<h4 class="mansect"><a name="tag_19_16_21" id="tag_19_16_21">CHANGE HISTORY
<h4 class="mansect"><a name="tag_19_16_22" id="tag_19_16_22">Issue 6
<blockquote>
<p>IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/5 is applied so that the reference page sections use terms as
described in the Utility Description Defaults ( <a href="../utilities/V3_chap01.html#tag_18_04"><i>1.4 Utility Description
Defaults). No change in behavior is intended.

<h4 class="mansect"><a name="tag_19_16_23" id="tag_19_16_23">Issue 7
<blockquote>
<p>POSIX.1-2008, Technical Corrigendum 2, XCU/TC2-2008/0046 &#91;842&#93; is applied.

<h4 class="mansect"><a name="tag_19_16_24" id="tag_19_16_24">Issue 8
<blockquote>
<p>Austin Group Defect 1058 is applied, clarifying that the requirement for <i>n to be a positive decimal integer is a
requirement on the application.

<div class="box"><em>End of informative text.
<hr>

 <a name="colon" id="colon"> <a name=
"tag_19_17" id="tag_19_17"><!-- colon -->
<h4 class="mansect"><a name="tag_19_17_01" id="tag_19_17_01">NAME
<blockquote>colon — null utility
<h4 class="mansect"><a name="tag_19_17_02" id="tag_19_17_02">SYNOPSIS
<blockquote class="synopsis">
<p><code><tt>: <b>&#91;<i>argument<tt>&#46;&#46;&#46;<b>&#93;

<h4 class="mansect"><a name="tag_19_17_03" id="tag_19_17_03">DESCRIPTION
<blockquote>
<p>This utility shall do nothing except return a 0 exit status. It is used when a command is needed, as in the <b>then
condition of an <b>if command, but nothing is to be done by the command.

<h4 class="mansect"><a name="tag_19_17_04" id="tag_19_17_04">OPTIONS
<blockquote>
<p>This utility shall not recognize the <tt>&#34;&#45;&#45;&#34; argument in the manner specified by Guideline 10 of XBD <a href=
"../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines.
<p class="tent">Implementations shall not support any options.

<h4 class="mansect"><a name="tag_19_17_05" id="tag_19_17_05">OPERANDS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_17_06" id="tag_19_17_06">STDIN
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_17_07" id="tag_19_17_07">INPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_17_08" id="tag_19_17_08">ENVIRONMENT VARIABLES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_17_09" id="tag_19_17_09">ASYNCHRONOUS EVENTS
<blockquote>
<p>Default.

<h4 class="mansect"><a name="tag_19_17_10" id="tag_19_17_10">STDOUT
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_17_11" id="tag_19_17_11">STDERR
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_17_12" id="tag_19_17_12">OUTPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_17_13" id="tag_19_17_13">EXTENDED DESCRIPTION
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_17_14" id="tag_19_17_14">EXIT STATUS
<blockquote>
<p>Zero.

<h4 class="mansect"><a name="tag_19_17_15" id="tag_19_17_15">CONSEQUENCES OF ERRORS
<blockquote>
<p>None.

<hr>
<div class="box"><em>The following sections are informative.
<h4 class="mansect"><a name="tag_19_17_16" id="tag_19_17_16">APPLICATION USAGE
<blockquote>
<p>See the APPLICATION USAGE for <a href="../utilities/true.html"><i>true.

<h4 class="mansect"><a name="tag_19_17_17" id="tag_19_17_17">EXAMPLES
<blockquote>
<pre>
<tt>: &#34;&#36;{X=abc}&#34;
if     false
then   :
else   printf &#39;%s&#92;n&#39; &#34;&#36;X&#34;
fi
<b>
abc<tt>

<p class="tent">As with any of the special built-ins, the null utility can also have variable assignments and redirections
associated with it, such as:
<pre>
<tt>x=y : &gt; z

<p class="tent">which sets variable <i>x to the value <i>y (so that it persists after the null utility completes) and
creates or truncates file <b>z; if the file cannot be created or truncated, a non-interactive shell exits (see <a href=
"#tag_19_08_01">2.8.1 Consequences of Shell Errors).

<h4 class="mansect"><a name="tag_19_17_18" id="tag_19_17_18">RATIONALE
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_17_19" id="tag_19_17_19">FUTURE DIRECTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_17_20" id="tag_19_17_20">SEE ALSO
<blockquote>
<p><a href="#tag_19_15">2.15 Special Built-In Utilities, <a href="../utilities/true.html#"><i>true

<h4 class="mansect"><a name="tag_19_17_21" id="tag_19_17_21">CHANGE HISTORY
<h4 class="mansect"><a name="tag_19_17_22" id="tag_19_17_22">Issue 6
<blockquote>
<p>IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/5 is applied so that the reference page sections use terms as
described in the Utility Description Defaults ( <a href="../utilities/V3_chap01.html#tag_18_04"><i>1.4 Utility Description
Defaults). No change in behavior is intended.

<h4 class="mansect"><a name="tag_19_17_23" id="tag_19_17_23">Issue 7
<blockquote>
<p>SD5-XCU-ERN-97 is applied, updating the SYNOPSIS.

<h4 class="mansect"><a name="tag_19_17_24" id="tag_19_17_24">Issue 8
<blockquote>
<p>Austin Group Defect 1272 is applied, clarifying that the null utility does not process its arguments, does not recognize the
<tt>&#34;&#45;&#45;&#34; end-of-options delimiter, does not support any options, and does not write to standard error.
<p class="tent">Austin Group Defect 1640 is applied, changing the APPLICATION USAGE section.

<div class="box"><em>End of informative text.
<hr>

 <a name="continue" id="continue"> <a name=
"tag_19_18" id="tag_19_18"><!-- continue -->
<h4 class="mansect"><a name="tag_19_18_01" id="tag_19_18_01">NAME
<blockquote>continue — continue for, while, or until loop
<h4 class="mansect"><a name="tag_19_18_02" id="tag_19_18_02">SYNOPSIS
<blockquote class="synopsis">
<p><code><tt>continue <b>&#91;<i>n<b>&#93;

<h4 class="mansect"><a name="tag_19_18_03" id="tag_19_18_03">DESCRIPTION
<blockquote>
<p>If <i>n is specified, the <a href="#continue"><i>continue utility shall return to the top of the <i>nth
enclosing <b>for, <b>while, or <b>until loop. If <i>n is not specified, <a href="#continue"><i>continue
shall behave as if <i>n was specified as 1. Returning to the top of the loop involves repeating the condition list of a
<b>while or <b>until loop or performing the next assignment of a <b>for loop, and re-executing the loop if
appropriate.
<p class="tent">The application shall ensure that the value of <i>n is a positive decimal integer. If <i>n is greater than
the number of enclosing loops, the outermost enclosing loop shall be used. If there is no enclosing loop, the behavior is
unspecified.
<p class="tent">The meaning of &#34;enclosing&#34; shall be as specified in the description of the <a href="#break"><i>break
utility.

<h4 class="mansect"><a name="tag_19_18_04" id="tag_19_18_04">OPTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_18_05" id="tag_19_18_05">OPERANDS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_18_06" id="tag_19_18_06">STDIN
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_18_07" id="tag_19_18_07">INPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_18_08" id="tag_19_18_08">ENVIRONMENT VARIABLES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_18_09" id="tag_19_18_09">ASYNCHRONOUS EVENTS
<blockquote>
<p>Default.

<h4 class="mansect"><a name="tag_19_18_10" id="tag_19_18_10">STDOUT
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_18_11" id="tag_19_18_11">STDERR
<blockquote>
<p>The standard error shall be used only for diagnostic messages.

<h4 class="mansect"><a name="tag_19_18_12" id="tag_19_18_12">OUTPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_18_13" id="tag_19_18_13">EXTENDED DESCRIPTION
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_18_14" id="tag_19_18_14">EXIT STATUS
<blockquote>
<dl compact>
<dd>
<dt> 0
<dd>Successful completion.
<dt>&gt;0
<dd>The <i>n value was not an unsigned decimal integer greater than or equal to 1.

<h4 class="mansect"><a name="tag_19_18_15" id="tag_19_18_15">CONSEQUENCES OF ERRORS
<blockquote>
<p>Default.

<hr>
<div class="box"><em>The following sections are informative.
<h4 class="mansect"><a name="tag_19_18_16" id="tag_19_18_16">APPLICATION USAGE
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_18_17" id="tag_19_18_17">EXAMPLES
<blockquote>
<pre>
<tt>for i in &#42;
do
    if test -d &#34;&#36;i&#34;
    then continue
    fi
    printf &#39;&#34;%s&#34; is not a directory.&#92;n&#39; &#34;&#36;i&#34;
done

<h4 class="mansect"><a name="tag_19_18_18" id="tag_19_18_18">RATIONALE
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_18_19" id="tag_19_18_19">FUTURE DIRECTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_18_20" id="tag_19_18_20">SEE ALSO
<blockquote>
<p><a href="#tag_19_15">2.15 Special Built-In Utilities

<h4 class="mansect"><a name="tag_19_18_21" id="tag_19_18_21">CHANGE HISTORY
<h4 class="mansect"><a name="tag_19_18_22" id="tag_19_18_22">Issue 6
<blockquote>
<p>IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/5 is applied so that the reference page sections use terms as
described in the Utility Description Defaults ( <a href="../utilities/V3_chap01.html#tag_18_04"><i>1.4 Utility Description
Defaults). No change in behavior is intended.

<h4 class="mansect"><a name="tag_19_18_23" id="tag_19_18_23">Issue 7
<blockquote>
<p>The example is changed to use the <a href="../utilities/printf.html"><i>printf utility rather than <a href=
"../utilities/echo.html"><i>echo.
<p class="tent">POSIX.1-2008, Technical Corrigendum 2, XCU/TC2-2008/0046 &#91;842&#93; is applied.

<h4 class="mansect"><a name="tag_19_18_24" id="tag_19_18_24">Issue 8
<blockquote>
<p>Austin Group Defect 1058 is applied, clarifying that the requirement for <i>n to be a positive decimal integer is a
requirement on the application.

<div class="box"><em>End of informative text.
<hr>

 <a name="dot" id="dot"> <a name=
"tag_19_19" id="tag_19_19"><!-- dot -->
<h4 class="mansect"><a name="tag_19_19_01" id="tag_19_19_01">NAME
<blockquote>dot — execute commands in the current environment
<h4 class="mansect"><a name="tag_19_19_02" id="tag_19_19_02">SYNOPSIS
<blockquote class="synopsis">
<p><code><tt>. <i>file

<h4 class="mansect"><a name="tag_19_19_03" id="tag_19_19_03">DESCRIPTION
<blockquote>
<p>The shell shall tokenize (see <a href="#tag_19_03">2.3 Token Recognition) the contents of the <i>file, parse the tokens
(see <a href="#tag_19_10">2.10 Shell Grammar), and execute the resulting commands in the current environment. It is
unspecified whether the commands are parsed and executed as a <i>program (as for a shell script) or are parsed as a single
<i>compound&#95;list that is executed after the entire file has been parsed.
<p class="tent">If <i>file does not contain a &lt;slash&gt;, the shell shall use the search path specified by <i>PATH to
find the directory containing <i>file. Unlike normal command search, however, the file searched for by the <a href=
"#dot"><i>dot utility need not be executable. If no readable file is found, a non-interactive shell shall abort; an
interactive shell shall write a diagnostic message to standard error.
<p class="tent">The <a href="#dot"><i>dot special built-in shall support XBD <a href=
"../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines, except for Guidelines 1 and 2.

<h4 class="mansect"><a name="tag_19_19_04" id="tag_19_19_04">OPTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_19_05" id="tag_19_19_05">OPERANDS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_19_06" id="tag_19_19_06">STDIN
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_19_07" id="tag_19_19_07">INPUT FILES
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_19_08" id="tag_19_19_08">ENVIRONMENT VARIABLES
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_19_09" id="tag_19_19_09">ASYNCHRONOUS EVENTS
<blockquote>
<p>Default.

<h4 class="mansect"><a name="tag_19_19_10" id="tag_19_19_10">STDOUT
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_19_11" id="tag_19_19_11">STDERR
<blockquote>
<p>The standard error shall be used only for diagnostic messages.

<h4 class="mansect"><a name="tag_19_19_12" id="tag_19_19_12">OUTPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_19_13" id="tag_19_19_13">EXTENDED DESCRIPTION
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_19_14" id="tag_19_19_14">EXIT STATUS
<blockquote>
<p>If no readable file was found or if the commands in the file could not be parsed, and the shell is interactive (and therefore
does not abort; see <a href="#tag_19_08_01">2.8.1 Consequences of Shell Errors), the exit status shall be non-zero. Otherwise,
return the value of the last command executed, or a zero exit status if no command is executed.

<h4 class="mansect"><a name="tag_19_19_15" id="tag_19_19_15">CONSEQUENCES OF ERRORS
<blockquote>
<p>Default.

<hr>
<div class="box"><em>The following sections are informative.
<h4 class="mansect"><a name="tag_19_19_16" id="tag_19_19_16">APPLICATION USAGE
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_19_17" id="tag_19_19_17">EXAMPLES
<blockquote>
<pre>
<tt>cat foobar
<b>
foo=hello bar=world<tt>

. ./foobar
echo &#36;foo &#36;bar
<b>
hello world<tt>

<h4 class="mansect"><a name="tag_19_19_18" id="tag_19_19_18">RATIONALE
<blockquote>
<p>Some older implementations searched the current directory for the <i>file, even if the value of <i>PATH disallowed it.
This behavior was omitted from this volume of POSIX.1-2024 due to concerns about introducing the susceptibility to trojan horses
that the user might be trying to avoid by leaving <b>dot out of <i>PATH .
<p class="tent">The KornShell version of <a href="#dot"><i>dot takes optional arguments that are set to the positional
parameters. This is a valid extension that allows a <a href="#dot"><i>dot script to behave identically to a function.

<h4 class="mansect"><a name="tag_19_19_19" id="tag_19_19_19">FUTURE DIRECTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_19_20" id="tag_19_19_20">SEE ALSO
<blockquote>
<p><a href="#tag_19_15">2.15 Special Built-In Utilities, <a href="#tag_19_25">return

<h4 class="mansect"><a name="tag_19_19_21" id="tag_19_19_21">CHANGE HISTORY
<h4 class="mansect"><a name="tag_19_19_22" id="tag_19_19_22">Issue 6
<blockquote>
<p>IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/5 is applied so that the reference page sections use terms as
described in the Utility Description Defaults ( <a href="../utilities/V3_chap01.html#tag_18_04"><i>1.4 Utility Description
Defaults). No change in behavior is intended.

<h4 class="mansect"><a name="tag_19_19_23" id="tag_19_19_23">Issue 7
<blockquote>
<p>SD5-XCU-ERN-164 is applied.
<p class="tent">POSIX.1-2008, Technical Corrigendum 1, XCU/TC1-2008/0038 &#91;114&#93; and XCU/TC1-2008/0039 &#91;214&#93; are applied.

<h4 class="mansect"><a name="tag_19_19_24" id="tag_19_19_24">Issue 8
<blockquote>
<p>Austin Group Defect 252 is applied, adding a requirement for <a href="#dot"><i>dot to support XBD <a href=
"../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines (except for Guidelines 1 and 2, since the
utility&#39;s name is <tt>&#39;.&#39;).
<p class="tent">Austin Group Defect 953 is applied, clarifying how the commands in the <i>file are parsed.
<p class="tent">Austin Group Defect 1265 is applied, updating the DESCRIPTION to align with the changes made to <a href=
"#tag_19_08_01">2.8.1 Consequences of Shell Errors between Issue 6 and Issue 7.

<div class="box"><em>End of informative text.
<hr>

 <a name="eval" id="eval"> <a name=
"tag_19_20" id="tag_19_20"><!-- eval -->
<h4 class="mansect"><a name="tag_19_20_01" id="tag_19_20_01">NAME
<blockquote>eval — construct command by concatenating arguments
<h4 class="mansect"><a name="tag_19_20_02" id="tag_19_20_02">SYNOPSIS
<blockquote class="synopsis">
<p><code><tt>eval <b>&#91;<i>argument<tt>&#46;&#46;&#46;<b>&#93;

<h4 class="mansect"><a name="tag_19_20_03" id="tag_19_20_03">DESCRIPTION
<blockquote>
<p>The <a href="#eval"><i>eval utility shall construct a command string by concatenating <i>arguments together,
separating each with a &lt;space&gt; character. The constructed command string shall be tokenized (see <a href="#tag_19_03">2.3
Token Recognition), parsed (see <a href="#tag_19_10">2.10 Shell Grammar), and executed by the shell in the current
environment. It is unspecified whether the commands are parsed and executed as a <i>program (as for a shell script) or are
parsed as a single <i>compound&#95;list that is executed after the entire constructed command string has been parsed.

<h4 class="mansect"><a name="tag_19_20_04" id="tag_19_20_04">OPTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_20_05" id="tag_19_20_05">OPERANDS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_20_06" id="tag_19_20_06">STDIN
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_20_07" id="tag_19_20_07">INPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_20_08" id="tag_19_20_08">ENVIRONMENT VARIABLES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_20_09" id="tag_19_20_09">ASYNCHRONOUS EVENTS
<blockquote>
<p>Default.

<h4 class="mansect"><a name="tag_19_20_10" id="tag_19_20_10">STDOUT
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_20_11" id="tag_19_20_11">STDERR
<blockquote>
<p>The standard error shall be used only for diagnostic messages.

<h4 class="mansect"><a name="tag_19_20_12" id="tag_19_20_12">OUTPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_20_13" id="tag_19_20_13">EXTENDED DESCRIPTION
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_20_14" id="tag_19_20_14">EXIT STATUS
<blockquote>
<p>If there are no <i>arguments, or only null <i>arguments, <a href="#eval"><i>eval shall return a zero exit
status; otherwise, it shall return the exit status of the command defined by the string of concatenated <i>arguments separated
by &lt;space&gt; characters, or a non-zero exit status if the concatenation could not be parsed as a command and the shell is
interactive (and therefore did not abort).

<h4 class="mansect"><a name="tag_19_20_15" id="tag_19_20_15">CONSEQUENCES OF ERRORS
<blockquote>
<p>Default.

<hr>
<div class="box"><em>The following sections are informative.
<h4 class="mansect"><a name="tag_19_20_16" id="tag_19_20_16">APPLICATION USAGE
<blockquote>
<p>Since <a href="#eval"><i>eval is not required to recognize the <tt>&#34;&#45;&#45;&#34; end of options delimiter, in cases where
the argument(s) to <a href="#eval"><i>eval might begin with <tt>&#39;-&#39; it is recommended that the first argument is
prefixed by a string that will not alter the commands to be executed, such as a &lt;space&gt; character:
<pre>
<tt>eval &#34; &#36;commands&#34;

<p class="tent">or:
<pre>
<tt>eval &#34; &#36;(some&#95;command)&#34;

<h4 class="mansect"><a name="tag_19_20_17" id="tag_19_20_17">EXAMPLES
<blockquote>
<pre>
<tt>foo=10 x=foo
y=&#39;&#36;&#39;&#36;x
echo &#36;y
<b>
&#36;foo<tt>

eval y=&#39;&#36;&#39;&#36;x
echo &#36;y
<b>
10<tt>

<h4 class="mansect"><a name="tag_19_20_18" id="tag_19_20_18">RATIONALE
<blockquote>
<p>This standard allows, but does not require, <a href="#eval"><i>eval to recognize <tt>&#34;&#45;&#45;&#34;. Although this means
applications cannot use <tt>&#34;&#45;&#45;&#34; to protect against options supported as an extension (or errors reported for unsupported
options), the nature of the <a href="#eval"><i>eval utility is such that other means can be used to provide this protection
(see APPLICATION USAGE above).

<h4 class="mansect"><a name="tag_19_20_19" id="tag_19_20_19">FUTURE DIRECTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_20_20" id="tag_19_20_20">SEE ALSO
<blockquote>
<p><a href="#tag_19_15">2.15 Special Built-In Utilities

<h4 class="mansect"><a name="tag_19_20_21" id="tag_19_20_21">CHANGE HISTORY
<h4 class="mansect"><a name="tag_19_20_22" id="tag_19_20_22">Issue 6
<blockquote>
<p>IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/5 is applied so that the reference page sections use terms as
described in the Utility Description Defaults ( <a href="../utilities/V3_chap01.html#tag_18_04"><i>1.4 Utility Description
Defaults). No change in behavior is intended.

<h4 class="mansect"><a name="tag_19_20_23" id="tag_19_20_23">Issue 7
<blockquote>
<p>SD5-XCU-ERN-97 is applied, updating the SYNOPSIS.
<p class="tent">POSIX.1-2008, Technical Corrigendum 1, XCU/TC1-2008/0040 &#91;114&#93;, XCU/TC1-2008/0041 &#91;163&#93;, and XCU/TC1-2008/0042
&#91;163&#93; are applied.

<h4 class="mansect"><a name="tag_19_20_24" id="tag_19_20_24">Issue 8
<blockquote>
<p>Austin Group Defect 953 is applied, clarifying how the commands in the constructed command string are parsed.

<div class="box"><em>End of informative text.
<hr>

 <a name="exec" id="exec"> <a name=
"tag_19_21" id="tag_19_21"><!-- exec -->
<h4 class="mansect"><a name="tag_19_21_01" id="tag_19_21_01">NAME
<blockquote>exec — perform redirections in the current shell or execute a utility
<h4 class="mansect"><a name="tag_19_21_02" id="tag_19_21_02">SYNOPSIS
<blockquote class="synopsis">
<p><code><tt>exec <b>&#91;<i>utility <b>&#91;<i>argument<tt>&#46;&#46;&#46;<b>&#93;&#93;

<h4 class="mansect"><a name="tag_19_21_03" id="tag_19_21_03">DESCRIPTION
<blockquote>
<p>If <a href="#exec"><i>exec is specified with no operands, any redirections associated with the <a href=
"#exec"><i>exec command shall be made in the current shell execution environment. If any file descriptors with numbers
greater than 2 are opened by those redirections, it is unspecified whether those file descriptors remain open when the shell
invokes another utility. Scripts concerned that child shells could misuse open file descriptors can always close them explicitly,
as shown in one of the following examples. If the result of the redirections would be that file descriptor 0, 1, or 2 is closed,
implementations may open the file descriptor to an unspecified file.
<p class="tent">If <a href="#exec"><i>exec is specified with a <i>utility operand, the shell shall execute a
non-built-in utility as described in <a href="#tag_19_09_01_06">2.9.1.6 Non-built-in Utility Execution with <i>utility as
the command name and the <i>argument operands (if any) as the command arguments.
<p class="tent">If the <a href="#exec"><i>exec command fails, a non-interactive shell shall exit from the current shell
execution environment; <sup>&#91;<a href="javascript:open_code('UP')">UP&#93; <img src=".pic/opt-start.gif" alt=
"[Option Start]" border="0">  an interactive shell may exit from a subshell environment but shall not exit if the current
shell environment is not a subshell environment.
<p class="tent">If the <a href="#exec"><i>exec command fails and the shell does not exit, any redirections associated with
the <a href="#exec"><i>exec command that were successfully made shall take effect in the current shell execution
environment. <img src=".pic/opt-end.gif" alt="[Option End]" border="0">
<p class="tent">The <a href="#exec"><i>exec special built-in shall support XBD <a href=
"../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines.

<h4 class="mansect"><a name="tag_19_21_04" id="tag_19_21_04">OPTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_21_05" id="tag_19_21_05">OPERANDS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_21_06" id="tag_19_21_06">STDIN
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_21_07" id="tag_19_21_07">INPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_21_08" id="tag_19_21_08">ENVIRONMENT VARIABLES
<blockquote>
<p>The following environment variable shall affect the execution of <a href="#exec"><i>exec:
<dl compact>
<dd>
<dt><i>PATH
<dd>Determine the search path when looking for the utility given as the <i>utility operand; see XBD <a href=
"../basedefs/V1_chap08.html#tag_08_03"><i>8.3 Other Environment Variables.

<h4 class="mansect"><a name="tag_19_21_09" id="tag_19_21_09">ASYNCHRONOUS EVENTS
<blockquote>
<p>Default.

<h4 class="mansect"><a name="tag_19_21_10" id="tag_19_21_10">STDOUT
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_21_11" id="tag_19_21_11">STDERR
<blockquote>
<p>The standard error shall be used only for diagnostic messages.

<h4 class="mansect"><a name="tag_19_21_12" id="tag_19_21_12">OUTPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_21_13" id="tag_19_21_13">EXTENDED DESCRIPTION
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_21_14" id="tag_19_21_14">EXIT STATUS
<blockquote>
<p>If <i>utility is specified and is executed, <a href="#exec"><i>exec shall not return to the shell; rather, the exit
status of the current shell execution environment shall be the exit status of <i>utility. If <i>utility is specified and an
attempt to execute it as a non-built-in utility fails, the exit status shall be as described in <a href="#tag_19_09_01_06">2.9.1.6
Non-built-in Utility Execution. If a redirection error occurs (see <a href="#tag_19_08_01">2.8.1 Consequences of Shell
Errors), the exit status shall be a value in the range 1-125. Otherwise, <a href="#exec"><i>exec shall return a zero
exit status.

<h4 class="mansect"><a name="tag_19_21_15" id="tag_19_21_15">CONSEQUENCES OF ERRORS
<blockquote>
<p>Default.

<hr>
<div class="box"><em>The following sections are informative.
<h4 class="mansect"><a name="tag_19_21_16" id="tag_19_21_16">APPLICATION USAGE
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_21_17" id="tag_19_21_17">EXAMPLES
<blockquote>
<p>Open <i>readfile as file descriptor 3 for reading:
<pre>
<tt>exec 3&lt; readfile

<p class="tent">Open <i>writefile as file descriptor 4 for writing:
<pre>
<tt>exec 4&gt; writefile

<p class="tent">Make file descriptor 5 a copy of file descriptor 0:
<pre>
<tt>exec 5&lt;&amp;0

<p class="tent">Close file descriptor 3:
<pre>
<tt>exec 3&lt;&amp;-

<p class="tent">Cat the file <b>maggie by replacing the current shell with the <a href="../utilities/cat.html"><i>cat
utility:
<pre>
<tt>exec cat maggie

<p class="tent">An application that is not concerned with strict conformance can make use of optional <tt>%g support known to
be present in the implementation&#39;s <a href="../utilities/printf.html"><i>printf utility by ensuring that any shell built-in
version is not executed instead, and using a subshell so that the shell continues afterwards:
<pre>
<tt>(exec printf &#39;%g&#92;n&#39; &#34;&#36;float&#95;value&#34;)

<h4 class="mansect"><a name="tag_19_21_18" id="tag_19_21_18">RATIONALE
<blockquote>
<p>Most historical implementations were not conformant in that:
<pre>
<tt>foo=bar exec cmd

<p class="tent">did not pass <b>foo to <b>cmd.

<h4 class="mansect"><a name="tag_19_21_19" id="tag_19_21_19">FUTURE DIRECTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_21_20" id="tag_19_21_20">SEE ALSO
<blockquote>
<p><a href="#tag_19_15">2.15 Special Built-In Utilities

<h4 class="mansect"><a name="tag_19_21_21" id="tag_19_21_21">CHANGE HISTORY
<h4 class="mansect"><a name="tag_19_21_22" id="tag_19_21_22">Issue 6
<blockquote>
<p>IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/5 is applied so that the reference page sections use terms as
described in the Utility Description Defaults ( <a href="../utilities/V3_chap01.html#tag_18_04"><i>1.4 Utility Description
Defaults). No change in behavior is intended.

<h4 class="mansect"><a name="tag_19_21_23" id="tag_19_21_23">Issue 7
<blockquote>
<p>SD5-XCU-ERN-97 is applied, updating the SYNOPSIS.

<h4 class="mansect"><a name="tag_19_21_24" id="tag_19_21_24">Issue 8
<blockquote>
<p>Austin Group Defect 252 is applied, adding a requirement for <a href="#exec"><i>exec to support XBD <a href=
"../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines.
<p class="tent">Austin Group Defect 1157 is applied, clarifying the execution of non-built-in utilities.
<p class="tent">Austin Group Defect 1587 is applied, changing the ENVIRONMENT VARIABLES section.

<div class="box"><em>End of informative text.
<hr>

 <a name="exit" id="exit"> <a name=
"tag_19_22" id="tag_19_22"><!-- exit -->
<h4 class="mansect"><a name="tag_19_22_01" id="tag_19_22_01">NAME
<blockquote>exit — cause the shell to exit
<h4 class="mansect"><a name="tag_19_22_02" id="tag_19_22_02">SYNOPSIS
<blockquote class="synopsis">
<p><code><tt>exit <b>&#91;<i>n<b>&#93;

<h4 class="mansect"><a name="tag_19_22_03" id="tag_19_22_03">DESCRIPTION
<blockquote>
<p>The <a href="#exit"><i>exit utility shall cause the shell to exit from its current execution environment. If the current
execution environment is a subshell environment, the shell shall exit from the subshell environment and continue in the environment
from which that subshell environment was invoked; otherwise, the shell utility shall terminate. The wait status of the shell or
subshell shall be determined by the unsigned decimal integer <i>n, if specified.
<p class="tent">If <i>n is specified and has a value between 0 and 255 inclusive, the wait status of the shell or subshell
shall indicate that it exited with exit status <i>n. If <i>n is specified and has a value greater than 256 that corresponds
to an exit status the shell assigns to commands terminated by a valid signal (see <a href="#tag_19_08_02">2.8.2 Exit Status for
Commands), the wait status of the shell or subshell shall indicate that it was terminated by that signal. No other actions
associated with the signal, such as execution of <a href="#trap"><i>trap actions or creation of a core image, shall be
performed by the shell.
<p class="tent">If <i>n is specified and is not an unsigned decimal integer, or has a value of 256, or has a value greater than
256 but not corresponding to an exit status the shell assigns to commands terminated by a valid signal, the wait status of the
shell or subshell is unspecified.
<p class="tent">If <i>n is not specified, the result shall be as if <i>n were specified with the current value of the
special parameter <tt>&#39;?&#39; (see <a href="#tag_19_05_02">2.5.2 Special Parameters), except that if the <a href=
"#exit"><i>exit command would cause the end of execution of a <a href="#trap"><i>trap action, the value for the
special parameter <tt>&#39;?&#39; that is considered &#34;current&#34; shall be the value it had immediately preceding the <a href=
"#trap"><i>trap action.
<p class="tent">A <a href="#trap"><i>trap action on <b>EXIT shall be executed before the shell terminates, except when
the <a href="#exit"><i>exit utility is invoked in that <a href="#trap"><i>trap action itself, in which case the
shell shall exit immediately. It is unspecified whether setting a new <a href="#trap"><i>trap action on <b>EXIT during
execution of a <a href="#trap"><i>trap action on <b>EXIT will cause the new <a href="#trap"><i>trap action to
be executed before the shell terminates.

<h4 class="mansect"><a name="tag_19_22_04" id="tag_19_22_04">OPTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_22_05" id="tag_19_22_05">OPERANDS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_22_06" id="tag_19_22_06">STDIN
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_22_07" id="tag_19_22_07">INPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_22_08" id="tag_19_22_08">ENVIRONMENT VARIABLES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_22_09" id="tag_19_22_09">ASYNCHRONOUS EVENTS
<blockquote>
<p>Default.

<h4 class="mansect"><a name="tag_19_22_10" id="tag_19_22_10">STDOUT
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_22_11" id="tag_19_22_11">STDERR
<blockquote>
<p>The standard error shall be used only for diagnostic messages.

<h4 class="mansect"><a name="tag_19_22_12" id="tag_19_22_12">OUTPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_22_13" id="tag_19_22_13">EXTENDED DESCRIPTION
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_22_14" id="tag_19_22_14">EXIT STATUS
<blockquote>
<p>The <a href="#exit"><i>exit utility causes the shell to exit from its current execution environment, and therefore does
not itself return an exit status.

<h4 class="mansect"><a name="tag_19_22_15" id="tag_19_22_15">CONSEQUENCES OF ERRORS
<blockquote>
<p>Default.

<hr>
<div class="box"><em>The following sections are informative.
<h4 class="mansect"><a name="tag_19_22_16" id="tag_19_22_16">APPLICATION USAGE
<blockquote>
<p>As explained in other sections, certain exit status values have been reserved for special uses and should be used by
applications only for those purposes:
<dl compact>
<dd>
<dt> 126
<dd>A file to be executed was found, but it was not an executable utility.
<dt> 127
<dd>A utility to be executed was not found.
<dt> 128
<dd>An unrecoverable read error was detected by the shell while reading commands, except from the <i>file operand of the
<a href="#dot"><i>dot special built-in.
<dt>&gt;128
<dd>A command was interrupted by a signal.

<h4 class="mansect"><a name="tag_19_22_17" id="tag_19_22_17">EXAMPLES
<blockquote>
<p>Exit with a <i>true value:
<pre>
<tt>exit 0

<p class="tent">Exit with a <i>false value:
<pre>
<tt>exit 1

<p class="tent">Propagate error handling from within a subshell:
<pre>
<tt>(
    command1 || exit 1
    command2 || exit 1
    exec command3
) &gt; outputfile || exit 1
echo &#34;outputfile created successfully&#34;

<h4 class="mansect"><a name="tag_19_22_18" id="tag_19_22_18">RATIONALE
<blockquote>
<p>The behavior of <a href="#exit"><i>exit when given an invalid argument or unknown option is unspecified, because of
differing practices in the various historical implementations. A value larger than 255 might be truncated by the shell, and be
unavailable even to a parent process that uses <a href="../functions/waitid.html"><i>waitid() to get the full exit value.
It is recommended that implementations that detect any usage error should cause a non-zero exit status (or, if the shell is
interactive and the error does not cause the shell to abort, store a non-zero value in <tt>&#34;&#36;?&#34;), but even this was not done
historically in all shells.
<p class="tent">See also <a href="../xrat/V4_xcu_chap01.html#tag_23_02_08_02"><i>C.2.8.2 Exit Status for Commands.

<h4 class="mansect"><a name="tag_19_22_19" id="tag_19_22_19">FUTURE DIRECTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_22_20" id="tag_19_22_20">SEE ALSO
<blockquote>
<p><a href="#tag_19_15">2.15 Special Built-In Utilities

<h4 class="mansect"><a name="tag_19_22_21" id="tag_19_22_21">CHANGE HISTORY
<h4 class="mansect"><a name="tag_19_22_22" id="tag_19_22_22">Issue 6
<blockquote>
<p>IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/5 is applied so that the reference page sections use terms as
described in the Utility Description Defaults ( <a href="../utilities/V3_chap01.html#tag_18_04"><i>1.4 Utility Description
Defaults). No change in behavior is intended.

<h4 class="mansect"><a name="tag_19_22_23" id="tag_19_22_23">Issue 7
<blockquote>
<p>POSIX.1-2008, Technical Corrigendum 2, XCU/TC2-2008/0047 &#91;717&#93;, XCU/TC2-2008/0048 &#91;960&#93;, XCU/TC2-2008/0049 &#91;717&#93;, and
XCU/TC2-2008/0050 &#91;960&#93; are applied.

<h4 class="mansect"><a name="tag_19_22_24" id="tag_19_22_24">Issue 8
<blockquote>
<p>Austin Group Defect 51 is applied, specifying the behavior when <i>n has a value greater than 256 that corresponds to an
exit status the shell assigns to commands terminated by a valid signal.
<p class="tent">Austin Group Defect 1029 is applied, changing &#34;<a href="#trap"><i>trap&#34; to &#34;<a href=
"#trap"><i>trap action&#34; in the DESCRIPTION section.
<p class="tent">Austin Group Defect 1309 is applied, changing the EXIT STATUS section.
<p class="tent">Austin Group Defect 1425 is applied, clarifying the requirements for a <a href="#trap"><i>trap action on
<b>EXIT.
<p class="tent">Austin Group Defect 1602 is applied, clarifying the behavior of <a href="#exit"><i>exit in a <a href=
"#trap"><i>trap action.
<p class="tent">Austin Group Defect 1629 is applied, adding exit status 128 to the APPLICATION USAGE section.

<div class="box"><em>End of informative text.
<hr>

 <a name="export" id="export"> <a name=
"tag_19_23" id="tag_19_23"><!-- export -->
<h4 class="mansect"><a name="tag_19_23_01" id="tag_19_23_01">NAME
<blockquote>export — set the export attribute for variables
<h4 class="mansect"><a name="tag_19_23_02" id="tag_19_23_02">SYNOPSIS
<blockquote class="synopsis">
<p><code><tt>export name<b>&#91;<tt>=<i>word<b>&#93;<tt>&#46;&#46;&#46;<br>
 <br>
export -p

<h4 class="mansect"><a name="tag_19_23_03" id="tag_19_23_03">DESCRIPTION
<blockquote>
<p>The shell shall give the <a href="#export"><i>export attribute to the variables corresponding to the specified
<i>names, which shall cause them to be in the environment of subsequently executed commands. If the name of a variable is
followed by =<i>word, then the value of that variable shall be set to <i>word.
<p class="tent">The <a href="#export"><i>export special built-in shall be a declaration utility. Therefore, if
<i>export is recognized as the command name of a simple command, then subsequent words of the form <i>name=<i>word
shall be expanded in an assignment context. See <a href="#tag_19_09_01_01">2.9.1.1 Order of Processing.
<p class="tent">The <a href="#export"><i>export special built-in shall support XBD <a href=
"../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines.
<p class="tent">When <b>-p is specified, <a href="#export"><i>export shall write to the standard output the names and
values of all exported variables, in the following format:
<pre>
<tt>&#34;export %s=%s&#92;n&#34;, &lt;<i>name<tt>&gt;, &lt;<i>value<tt>&gt;

<p class="tent">if <i>name is set, and:
<pre>
<tt>&#34;export %s&#92;n&#34;, &lt;<i>name<tt>&gt;

<p class="tent">if <i>name is unset.
<p class="tent">The shell shall format the output, including the proper use of quoting, so that it is suitable for reinput to the
shell as commands that achieve the same exporting results, except:
<ol>
<li class="tent">Read-only variables with values cannot be reset.
<li class="tent">Variables that were unset at the time they were output need not be reset to the unset state if a value is assigned
to the variable between the time the state was saved and the time at which the saved output is reinput to the shell.

<p class="tent">When no arguments are given, the results are unspecified.

<h4 class="mansect"><a name="tag_19_23_04" id="tag_19_23_04">OPTIONS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_23_05" id="tag_19_23_05">OPERANDS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_23_06" id="tag_19_23_06">STDIN
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_23_07" id="tag_19_23_07">INPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_23_08" id="tag_19_23_08">ENVIRONMENT VARIABLES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_23_09" id="tag_19_23_09">ASYNCHRONOUS EVENTS
<blockquote>
<p>Default.

<h4 class="mansect"><a name="tag_19_23_10" id="tag_19_23_10">STDOUT
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_23_11" id="tag_19_23_11">STDERR
<blockquote>
<p>The standard error shall be used only for diagnostic messages.

<h4 class="mansect"><a name="tag_19_23_12" id="tag_19_23_12">OUTPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_23_13" id="tag_19_23_13">EXTENDED DESCRIPTION
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_23_14" id="tag_19_23_14">EXIT STATUS
<blockquote>
<dl compact>
<dd>
<dt> 0
<dd>Successful completion.
<dt>&gt;0
<dd>At least one operand could not be processed as requested, such as a <i>name operand that could not be exported or an
attempt to modify a <i>readonly variable using a <i>name=<i>word operand, or the <b>-p option was specified and a
write error occurred.

<h4 class="mansect"><a name="tag_19_23_15" id="tag_19_23_15">CONSEQUENCES OF ERRORS
<blockquote>
<p>Default.

<hr>
<div class="box"><em>The following sections are informative.
<h4 class="mansect"><a name="tag_19_23_16" id="tag_19_23_16">APPLICATION USAGE
<blockquote>
<p>Note that, unless <i>X was previously marked readonly, the value of <tt>&#34;&#36;?&#34; after:
<pre>
<tt>export X=&#36;(false)

<p class="tent">will be 0 (because <a href="#export"><i>export successfully set <i>X to the empty string) and that
execution continues, even if <a href="#set"><i>set <b>-e is in effect. In order to detect command substitution
failures, a user must separate the assignment from the export, as in:
<pre>
<tt>X=&#36;(false)
export X

<p class="tent">In shells that support extended assignment syntax, for example to allow an array to be populated with a single
assignment, such extensions can typically only be used in assignments specified as arguments to <a href="#export"><i>export
if the command word is literally <i>export, and not if it is some other word that expands to <i>export. For example:
<pre>
<tt># Shells that support array assignment as an extension generally
# support this:
export x=(1 2 3); echo &#36;{x&#91;0&#93;}  # outputs 1
# But generally do not support this:
e=export; &#36;e x=(1 2 3); echo &#36;{x&#91;0&#93;}  # syntax error

<h4 class="mansect"><a name="tag_19_23_17" id="tag_19_23_17">EXAMPLES
<blockquote>
<p>Export <i>PWD and <i>HOME variables:
<pre>
<tt>export PWD HOME

<p class="tent">Set and export the <i>PATH variable:
<pre>
<tt>export PATH=&#34;/local/bin:&#36;PATH&#34;

<p class="tent">Save and restore all exported variables:
<pre>
<tt>export -p &gt; temp-file
unset <i>a lot of variables<tt>

&#46;&#46;&#46; <i>processing<tt>

. ./temp-file

<basefont size="2">
<dl>
<dt><b>Note:
<dd>If LANG, LC&#95;CTYPE or LC&#95;ALL are left altered or unset in the above example prior to sourcing <tt>temp-file, the results
may be undefined.

<basefont size="3">
<h4 class="mansect"><a name="tag_19_23_18" id="tag_19_23_18">RATIONALE
<blockquote>
<p>Some historical shells use the no-argument case as the functional equivalent of what is required here with <b>-p. This
feature was left unspecified because it is not historical practice in all shells, and some scripts may rely on the now-unspecified
results on their implementations. Attempts to specify the <b>-p output as the default case were unsuccessful in achieving
consensus. The <b>-p option was added to allow portable access to the values that can be saved and then later restored using;
for example, a <a href="#dot"><i>dot script.
<p class="tent">Some implementations extend the shell&#39;s assignment syntax, for example to allow an array to be populated with a
single assignment, and in order for such an extension to be usable in assignments specified as arguments to <a href=
"#export"><i>export these shells have <i>export as a separate token in their grammar. This standard only permits an
extension of this nature when the input to the shell would contain a syntax error according to the standard grammar. Note that
although <i>export can be a separate token in the shell&#39;s grammar, it cannot be a reserved word since <i>export is a
candidate for alias substitution whereas reserved words are not (see <a href="#tag_19_03_01">2.3.1 Alias Substitution).

<h4 class="mansect"><a name="tag_19_23_19" id="tag_19_23_19">FUTURE DIRECTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_23_20" id="tag_19_23_20">SEE ALSO
<blockquote>
<p><a href="#tag_19_09_01_01">2.9.1.1 Order of Processing, <a href="#tag_19_15">2.15 Special Built-In Utilities
<p class="tent">XBD <a href="../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines

<h4 class="mansect"><a name="tag_19_23_21" id="tag_19_23_21">CHANGE HISTORY
<h4 class="mansect"><a name="tag_19_23_22" id="tag_19_23_22">Issue 6
<blockquote>
<p>IEEE PASC Interpretation 1003.2 #203 is applied, clarifying the format when a variable is unset.
<p class="tent">IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/5 is applied so that the reference page sections
use terms as described in the Utility Description Defaults ( <a href="../utilities/V3_chap01.html#tag_18_04"><i>1.4 Utility
Description Defaults). No change in behavior is intended.
<p class="tent">IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/6 is applied, adding the following text to the end
of the first paragraph of the DESCRIPTION: &#34;If the name of a variable is followed by =<i>word, then the value of that variable
shall be set to <i>word.&#34;. The reason for this change is that the SYNOPSIS for <a href="#export"><i>export
includes:
<pre>
<tt>export name<b>&#91;<tt>=<i>word<b>&#93;<tt>&#46;&#46;&#46;

<p class="tent">but the meaning of the optional &#34;=<i>word&#34; is never explained in the text.

<h4 class="mansect"><a name="tag_19_23_23" id="tag_19_23_23">Issue 7
<blockquote>
<p>POSIX.1-2008, Technical Corrigendum 1, XCU/TC1-2008/0043 &#91;352&#93; is applied.
<p class="tent">POSIX.1-2008, Technical Corrigendum 2, XCU/TC2-2008/0051 &#91;654&#93; and XCU/TC2-2008/0052 &#91;960&#93; are applied.

<h4 class="mansect"><a name="tag_19_23_24" id="tag_19_23_24">Issue 8
<blockquote>
<p>Austin Group Defect 351 is applied, requiring <a href="#export"><i>export to be a declaration utility.
<p class="tent">Austin Group Defect 367 is applied, changing the EXIT STATUS section.
<p class="tent">Austin Group Defect 1258 is applied, changing the EXAMPLES section.
<p class="tent">Austin Group Defect 1393 is applied, changing the APPLICATION USAGE and RATIONALE sections.

<div class="box"><em>End of informative text.
<hr>

 <a name="readonly" id="readonly"> <a name=
"tag_19_24" id="tag_19_24"><!-- readonly -->
<h4 class="mansect"><a name="tag_19_24_01" id="tag_19_24_01">NAME
<blockquote>readonly — set the readonly attribute for variables
<h4 class="mansect"><a name="tag_19_24_02" id="tag_19_24_02">SYNOPSIS
<blockquote class="synopsis">
<p><code><tt>readonly name<b>&#91;<tt>=<i>word<b>&#93;<tt>&#46;&#46;&#46;<br>
 <br>
readonly -p

<h4 class="mansect"><a name="tag_19_24_03" id="tag_19_24_03">DESCRIPTION
<blockquote>
<p>The variables whose <i>names are specified shall be given the <a href="#readonly"><i>readonly attribute. The values
of variables with the <a href="#readonly"><i>readonly attribute cannot be changed by subsequent assignment or use of the
<a href="#export"><i>export, <a href="../utilities/getopts.html"><i>getopts, <a href=
"#readonly"><i>readonly, or <a href="../utilities/read.html"><i>read utilities, nor can those variables be unset by
the <a href="#unset"><i>unset utility. As described in XBD <a href="../basedefs/V1_chap08.html#tag_08_01"><i>8.1
Environment Variable Definition, conforming applications shall not request to mark a variable as <i>readonly if it is
documented as being manipulated by a shell built-in utility, as it may render those utilities unable to complete successfully. If
the name of a variable is followed by =<i>word, then the value of that variable shall be set to <i>word.
<p class="tent">The <a href="#readonly"><i>readonly special built-in shall be a declaration utility. Therefore, if
<i>readonly is recognized as the command name of a simple command, then subsequent words of the form <i>name=<i>word
shall be expanded in an assignment context. See <a href="#tag_19_09_01_01">2.9.1.1 Order of Processing.
<p class="tent">The <a href="#readonly"><i>readonly special built-in shall support XBD <a href=
"../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines.
<p class="tent">When <b>-p is specified, <a href="#readonly"><i>readonly writes to the standard output the names and
values of all read-only variables, in the following format:
<pre>
<tt>&#34;readonly %s=%s&#92;n&#34;, &lt;<i>name<tt>&gt;, &lt;<i>value<tt>&gt;

<p class="tent">if <i>name is set, and
<pre>
<tt>&#34;readonly %s&#92;n&#34;, &lt;<i>name<tt>&gt;

<p class="tent">if <i>name is unset.
<p class="tent">The shell shall format the output, including the proper use of quoting, so that it is suitable for reinput to the
shell as commands that achieve the same value and <i>readonly attribute-setting results in a shell execution environment in
which:
<ol>
<li class="tent">Variables with values at the time they were output do not have the <i>readonly attribute set.
<li class="tent">Variables that were unset at the time they were output do not have a value at the time at which the saved output
is reinput to the shell.

<p class="tent">When no arguments are given, the results are unspecified.

<h4 class="mansect"><a name="tag_19_24_04" id="tag_19_24_04">OPTIONS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_24_05" id="tag_19_24_05">OPERANDS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_24_06" id="tag_19_24_06">STDIN
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_24_07" id="tag_19_24_07">INPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_24_08" id="tag_19_24_08">ENVIRONMENT VARIABLES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_24_09" id="tag_19_24_09">ASYNCHRONOUS EVENTS
<blockquote>
<p>Default.

<h4 class="mansect"><a name="tag_19_24_10" id="tag_19_24_10">STDOUT
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_24_11" id="tag_19_24_11">STDERR
<blockquote>
<p>The standard error shall be used only for diagnostic messages.

<h4 class="mansect"><a name="tag_19_24_12" id="tag_19_24_12">OUTPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_24_13" id="tag_19_24_13">EXTENDED DESCRIPTION
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_24_14" id="tag_19_24_14">EXIT STATUS
<blockquote>
<dl compact>
<dd>
<dt> 0
<dd>Successful completion.
<dt>&gt;0
<dd>At least one operand could not be processed as requested, such as a <i>name operand that could not be marked
<i>readonly or an attempt to modify an already <i>readonly variable using a <i>name=<i>word operand, or the
<b>-p option was specified and a write error occurred.

<h4 class="mansect"><a name="tag_19_24_15" id="tag_19_24_15">CONSEQUENCES OF ERRORS
<blockquote>
<p>Default.

<hr>
<div class="box"><em>The following sections are informative.
<h4 class="mansect"><a name="tag_19_24_16" id="tag_19_24_16">APPLICATION USAGE
<blockquote>
<p>In shells that support extended assignment syntax, for example to allow an array to be populated with a single assignment, such
extensions can typically only be used in assignments specified as arguments to <a href="#readonly"><i>readonly if the
command word is literally <i>readonly, and not if it is some other word that expands to <i>readonly. For example:
<pre>
<tt># Shells that support array assignment as an extension generally
# support this:
readonly x=(1 2 3); echo &#36;{x&#91;0&#93;}  # outputs 1
# But generally do not support this:
r=readonly; &#36;r x=(1 2 3); echo &#36;{x&#91;0&#93;}  # syntax error

<h4 class="mansect"><a name="tag_19_24_17" id="tag_19_24_17">EXAMPLES
<blockquote>
<pre>
<tt>readonly HOME

<h4 class="mansect"><a name="tag_19_24_18" id="tag_19_24_18">RATIONALE
<blockquote>
<p>Some historical shells preserve the <i>readonly attribute across separate invocations. This volume of POSIX.1-2024 allows
this behavior, but does not require it.
<p class="tent">The <b>-p option allows portable access to the values that can be saved and then later restored using, for
example, a <a href="#dot"><i>dot script. Also see the RATIONALE for <a href="#tag_19_23">export for a description of
the no-argument and <b>-p output cases and a related example.
<p class="tent">Read-only functions were considered, but they were omitted as not being historical practice or particularly useful.
Furthermore, functions must not be read-only across invocations to preclude &#34;spoofing&#34; (spoofing is the term for the practice of
creating a program that acts like a well-known utility with the intent of subverting the real intent of the user) of administrative
or security-relevant (or security-conscious) shell scripts.
<p class="tent">Attempts to set the <i>readonly attribute on certain variables, such as <i>PWD , may have surprising
results. Either <a href="#readonly"><i>readonly will reject the attempt, or the attempt will succeed but the shell will
continue to alter the contents of <i>PWD during the <a href="../utilities/cd.html"><i>cd utility, or the attempt will
succeed and render the <a href="../utilities/cd.html"><i>cd utility inoperative (since it must not change directories if it
cannot also update <i>PWD ).
<p class="tent">Some implementations extend the shell&#39;s assignment syntax, for example to allow an array to be populated with a
single assignment, and in order for such an extension to be usable in assignments specified as arguments to <a href=
"#readonly"><i>readonly these shells have <i>readonly as a separate token in their grammar. This standard only permits
an extension of this nature when the input to the shell would contain a syntax error according to the standard grammar. Note that
although <i>readonly can be a separate token in the shell&#39;s grammar, it cannot be a reserved word since <i>readonly is a
candidate for alias substitution whereas reserved words are not (see <a href="#tag_19_03_01">2.3.1 Alias Substitution).

<h4 class="mansect"><a name="tag_19_24_19" id="tag_19_24_19">FUTURE DIRECTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_24_20" id="tag_19_24_20">SEE ALSO
<blockquote>
<p><a href="#tag_19_09_01_01">2.9.1.1 Order of Processing, <a href="#tag_19_15">2.15 Special Built-In Utilities
<p class="tent">XBD <a href="../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines

<h4 class="mansect"><a name="tag_19_24_21" id="tag_19_24_21">CHANGE HISTORY
<h4 class="mansect"><a name="tag_19_24_22" id="tag_19_24_22">Issue 6
<blockquote>
<p>IEEE PASC Interpretation 1003.2 #203 is applied, clarifying the format when a variable is unset.
<p class="tent">IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/5 is applied so that the reference page sections
use terms as described in the Utility Description Defaults ( <a href="../utilities/V3_chap01.html#tag_18_04"><i>1.4 Utility
Description Defaults). No change in behavior is intended.
<p class="tent">IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/7 is applied, adding the following text to the end
of the first paragraph of the DESCRIPTION: &#34;If the name of a variable is followed by =<i>word, then the value of that variable
shall be set to <i>word.&#34;. The reason for this change is that the SYNOPSIS for <a href="#readonly"><i>readonly
includes:<br>
<pre>
<tt>readonly name<b>&#91;<tt>=<i>word<b>&#93;<tt>&#46;&#46;&#46;

<p class="tent">but the meaning of the optional &#34;=<i>word&#34; is never explained in the text.

<h4 class="mansect"><a name="tag_19_24_23" id="tag_19_24_23">Issue 7
<blockquote>
<p>POSIX.1-2008, Technical Corrigendum 2, XCU/TC2-2008/0052 &#91;960&#93; is applied.

<h4 class="mansect"><a name="tag_19_24_24" id="tag_19_24_24">Issue 8
<blockquote>
<p>Austin Group Defect 351 is applied, requiring <a href="#readonly"><i>readonly to be a declaration utility.
<p class="tent">Austin Group Defect 367 is applied, clarifying that the values of <i>readonly variables cannot be changed by
subsequent use of the <a href="#export"><i>export, <a href="../utilities/getopts.html"><i>getopts, <a href=
"#readonly"><i>readonly, or <a href="../utilities/read.html"><i>read utilities, and changing the EXIT STATUS,
EXAMPLES and RATIONALE sections.
<p class="tent">Austin Group Defect 1393 is applied, changing the APPLICATION USAGE and RATIONALE sections.

<div class="box"><em>End of informative text.
<hr>

 <a name="return" id="return"> <a name=
"tag_19_25" id="tag_19_25"><!-- return -->
<h4 class="mansect"><a name="tag_19_25_01" id="tag_19_25_01">NAME
<blockquote>return — return from a function or dot script
<h4 class="mansect"><a name="tag_19_25_02" id="tag_19_25_02">SYNOPSIS
<blockquote class="synopsis">
<p><code><tt>return <b>&#91;<i>n<b>&#93;

<h4 class="mansect"><a name="tag_19_25_03" id="tag_19_25_03">DESCRIPTION
<blockquote>
<p>The <a href="#return"><i>return utility shall cause the shell to stop executing the current function or <a href=
"#dot"><i>dot script. If the shell is not currently executing a function or <a href="#dot"><i>dot script, the
results are unspecified.

<h4 class="mansect"><a name="tag_19_25_04" id="tag_19_25_04">OPTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_25_05" id="tag_19_25_05">OPERANDS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_25_06" id="tag_19_25_06">STDIN
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_25_07" id="tag_19_25_07">INPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_25_08" id="tag_19_25_08">ENVIRONMENT VARIABLES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_25_09" id="tag_19_25_09">ASYNCHRONOUS EVENTS
<blockquote>
<p>Default.

<h4 class="mansect"><a name="tag_19_25_10" id="tag_19_25_10">STDOUT
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_25_11" id="tag_19_25_11">STDERR
<blockquote>
<p>The standard error shall be used only for diagnostic messages.

<h4 class="mansect"><a name="tag_19_25_12" id="tag_19_25_12">OUTPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_25_13" id="tag_19_25_13">EXTENDED DESCRIPTION
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_25_14" id="tag_19_25_14">EXIT STATUS
<blockquote>
<p>The exit status shall be <i>n, if specified, except that the behavior is unspecified if <i>n is not an unsigned decimal
integer or is greater than 255. If <i>n is not specified, the result shall be as if <i>n were specified with the current
value of the special parameter <tt>&#39;?&#39; (see <a href="#tag_19_05_02">2.5.2 Special Parameters), except that if the
<a href="#return"><i>return command would cause the end of execution of a <a href="#trap"><i>trap action, the value
for the special parameter <tt>&#39;?&#39; that is considered &#34;current&#34; shall be the value it had immediately preceding the <a href=
"#trap"><i>trap action.

<h4 class="mansect"><a name="tag_19_25_15" id="tag_19_25_15">CONSEQUENCES OF ERRORS
<blockquote>
<p>Default.

<hr>
<div class="box"><em>The following sections are informative.
<h4 class="mansect"><a name="tag_19_25_16" id="tag_19_25_16">APPLICATION USAGE
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_25_17" id="tag_19_25_17">EXAMPLES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_25_18" id="tag_19_25_18">RATIONALE
<blockquote>
<p>The behavior of <a href="#return"><i>return when not in a function or <a href="#dot"><i>dot script differs
between the System V shell and the KornShell. In the System V shell this is an error, whereas in the KornShell, the effect is the
same as <a href="#exit"><i>exit.
<p class="tent">The results of returning a number greater than 255 are undefined because of differing practices in the various
historical implementations. Some shells AND out all but the low-order 8 bits; others allow larger values, but not of unlimited
size.
<p class="tent">See the discussion of appropriate exit status values under <a href="#tag_19_22">exit.

<h4 class="mansect"><a name="tag_19_25_19" id="tag_19_25_19">FUTURE DIRECTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_25_20" id="tag_19_25_20">SEE ALSO
<blockquote>
<p><a href="#tag_19_09_05">2.9.5 Function Definition Command, <a href="#tag_19_15">2.15 Special Built-In Utilities,
<a href="#tag_19_19">dot

<h4 class="mansect"><a name="tag_19_25_21" id="tag_19_25_21">CHANGE HISTORY
<h4 class="mansect"><a name="tag_19_25_22" id="tag_19_25_22">Issue 6
<blockquote>
<p>IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/5 is applied so that the reference page sections use terms as
described in the Utility Description Defaults ( <a href="../utilities/V3_chap01.html#tag_18_04"><i>1.4 Utility Description
Defaults). No change in behavior is intended.

<h4 class="mansect"><a name="tag_19_25_23" id="tag_19_25_23">Issue 7
<blockquote>
<p>POSIX.1-2008, Technical Corrigendum 1, XCU/TC1-2008/0044 &#91;214&#93; and XCU/TC1-2008/0045 &#91;214&#93; are applied.
<p class="tent">POSIX.1-2008, Technical Corrigendum 2, XCU/TC2-2008/0052 &#91;960&#93; is applied.

<h4 class="mansect"><a name="tag_19_25_24" id="tag_19_25_24">Issue 8
<blockquote>
<p>Austin Group Defect 1309 is applied, changing the EXIT STATUS section.
<p class="tent">Austin Group Defect 1602 is applied, clarifying the behavior of <a href="#return"><i>return in a <a href=
"#trap"><i>trap action.

<div class="box"><em>End of informative text.
<hr>

 <a name="set" id="set"> <a name=
"tag_19_26" id="tag_19_26"><!-- set -->
<h4 class="mansect"><a name="tag_19_26_01" id="tag_19_26_01">NAME
<blockquote>set — set or unset options and positional parameters
<h4 class="mansect"><a name="tag_19_26_02" id="tag_19_26_02">SYNOPSIS
<blockquote class="synopsis">
<p><code><tt>set <b>&#91;<tt>-abCefhmnuvx<b>&#93; &#91;<tt>-o <i>option<b>&#93; &#91;<i>argument<tt>&#46;&#46;&#46;<b>&#93;
<tt><br>
 <br>
set <b>&#91;<tt>+abCefhmnuvx<b>&#93; &#91;<tt>+o <i>option<b>&#93; &#91;<i>argument<tt>&#46;&#46;&#46;<b>&#93; <tt><br>
 <br>
set &#45;&#45; <b>&#91;<i>argument<tt>&#46;&#46;&#46;<b>&#93; <tt><br>
 <br>
set -o<br>
 <br>
set +o

<h4 class="mansect"><a name="tag_19_26_03" id="tag_19_26_03">DESCRIPTION
<blockquote>
<p>If no <i>options or <i>arguments are specified, <a href="#set"><i>set shall write the names and values of all
shell variables in the collation sequence of the current locale. Each <i>name shall start on a separate line, using the
format:
<pre>
<tt>&#34;%s=%s&#92;n&#34;, &lt;<i>name<tt>&gt;, &lt;<i>value<tt>&gt;

<p class="tent">The <i>value string shall be written with appropriate quoting; see the description of shell quoting in <a href=
"#tag_19_02">2.2 Quoting. The output shall be suitable for reinput to the shell, setting or resetting, as far as possible, the
variables that are currently set; read-only variables cannot be reset.
<p class="tent">When options are specified, they shall set or unset attributes of the shell, as described below. When
<i>arguments are specified, they cause positional parameters to be set or unset, as described below. Setting or unsetting
attributes and positional parameters are not necessarily related actions, but they can be combined in a single invocation of
<a href="#set"><i>set.
<p class="tent">The <a href="#set"><i>set special built-in shall support XBD <a href=
"../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines except that options can be specified with either a
leading &lt;hyphen-minus&gt; (meaning enable the option) or &lt;plus-sign&gt; (meaning disable it) unless otherwise specified.
<p class="tent">Implementations shall support the options in the following list in both their &lt;hyphen-minus&gt; and
&lt;plus-sign&gt; forms. These options can also be specified as options to <a href="../utilities/sh.html"><i>sh.
<dl compact>
<dd>
<dt><b>-a
<dd>Set the <i>export attribute for all variable assignments. When this option is on, whenever a value is assigned to a
variable in the current shell execution environment, the <i>export attribute shall be set for the variable. This applies to all
forms of assignment, including those made as a side-effect of variable expansions or arithmetic expansions, and those made as a
result of the operation of the <a href="../utilities/cd.html"><i>cd, <a href=
"../utilities/getopts.html"><i>getopts, or <a href="../utilities/read.html"><i>read utilities. <basefont size="2">
<dl>
<dt><b>Note:
<dd>As discussed in <a href="#tag_19_09_01">2.9.1 Simple Commands, not all variable assignments happen in the current
execution environment. When an assignment happens in a separate execution environment the <i>export attribute is still set for
the variable, but that does not affect the current execution environment.

<basefont size="3">
<dt><b>-b
<dd>This option shall be supported if the implementation supports the User Portability Utilities option. When job control and
<b>-b are both enabled, the shell shall write asynchronous notifications of background job completions (including termination
by a signal), and may write asynchronous notifications of background job suspensions. See <a href="#tag_19_11">2.11 Job Control
for details. When job control is disabled, the <b>-b option shall have no effect. Asynchronous notification shall not be
enabled by default.
<dt><b>-C
<dd>(Uppercase C.) Prevent existing regular files from being overwritten by the shell&#39;s <tt>&#39;&gt;&#39; redirection operator (see
<a href="#tag_19_07_02">2.7.2 Redirecting Output); the <tt>&#34;&gt;|&#34; redirection operator shall override this
<i>noclobber option for an individual file.
<dt><b>-e
<dd>When this option is on, when any command fails (for any of the reasons listed in <a href="#tag_19_08_01">2.8.1 Consequences of
Shell Errors or by returning an exit status greater than zero), the shell immediately shall exit, as if by executing the
<a href="#exit"><i>exit special built-in utility with no arguments, with the following exceptions:
<ol>
<li class="tent">The failure of any individual command in a multi-command pipeline, or of any subshell environments in which
command substitution was performed during word expansion, shall not cause the shell to exit. Only the failure of the pipeline
itself shall be considered.
<li class="tent">The <b>-e setting shall be ignored when executing the compound list following the <b>while, <b>until,
<b>if, or <b>elif reserved word, a pipeline beginning with the <b>! reserved word, or any command of an AND-OR list
other than the last.
<li class="tent">If the exit status of a compound command other than a subshell command was the result of a failure while <b>-e
was being ignored, then <b>-e shall not apply to this command.

<p class="tent">This requirement applies to the shell environment and each subshell environment separately. For example, in:
<pre>
<tt>set -e; (false; echo one) | cat; echo two

<p class="tent">the <a href="../utilities/false.html"><i>false command causes the subshell to exit without executing
<tt>echo one; however, <tt>echo two is executed because the exit status of the pipeline <tt>(false; echo one) | cat
is zero.
<p class="tent">In
<pre>
<tt>set -e; echo &#36;(false; echo one) two

<p class="tent">the <a href="../utilities/false.html"><i>false command causes the subshell in which the command
substitution is performed to exit without executing <tt>echo one; the exit status of the subshell is ignored and the shell
then executes the word-expanded command <tt>echo two.

<dt><b>-f
<dd>The shell shall disable pathname expansion.
<dt><b>-h
<dd><sup>&#91;<a href="javascript:open_code('OB')">OB&#93; <img src=".pic/opt-start.gif" alt="[Option Start]" border="0">
Setting this option may speed up <i>PATH searches (see XBD <a href="../basedefs/V1_chap08.html#tag_08"><i>8. Environment
Variables). This option may be enabled by default. <img src=".pic/opt-end.gif" alt="[Option End]" border="0">
<dt><b>-m
<dd>This option shall be supported if the implementation supports the User Portability Utilities option. When this option is
enabled, the shell shall perform job control actions as described in <a href="#tag_19_11">2.11 Job Control. This option shall
be enabled by default for interactive shells.
<dt><b>-n
<dd>The shell shall read commands but does not execute them; this can be used to check for shell script syntax errors. Interactive
shells and subshells of interactive shells, recursively, may ignore this option.
<dt><b>-o
<dd>Write the current settings of the options to standard output in an unspecified format.
<dt><b>+o
<dd>Write the current option settings to standard output in a format that is suitable for reinput to the shell as commands that
achieve the same options settings.
<dt><b>-o <i>option
<dd><br>
Set various options, many of which shall be equivalent to the single option letters. The following values of <i>option shall be
supported:
<dl compact>
<dd>
<dt><i>allexport
<dd>Equivalent to <b>-a.
<dt><i>errexit
<dd>Equivalent to <b>-e.
<dt><i>ignoreeof
<dd>Prevent an interactive shell from exiting on end-of-file. This setting prevents accidental logouts when &lt;control&gt;-D is
entered. A user shall explicitly <a href="#exit"><i>exit to leave the interactive shell. This option shall be supported if
the system supports the User Portability Utilities option.
<dt><i>monitor
<dd>Equivalent to <b>-m. This option shall be supported if the system supports the User Portability Utilities option.
<dt><i>noclobber
<dd>Equivalent to <b>-C (uppercase C).
<dt><i>noglob
<dd>Equivalent to <b>-f.
<dt><i>noexec
<dd>Equivalent to <b>-n.
<dt><i>nolog
<dd><sup>&#91;<a href="javascript:open_code('OB')">OB&#93; <img src=".pic/opt-start.gif" alt="[Option Start]" border="0">
Prevent the entry of function definitions into the command history; see <a href="../utilities/sh.html#tag_20_110_13_01"><i>Command
History List. This option may have no effect; it is kept for compatibility with previous versions of the standard. This
option shall be supported if the system supports the User Portability Utilities option. <img src=".pic/opt-end.gif" alt=
"[Option End]" border="0">
<dt><i>notify
<dd>Equivalent to <b>-b.
<dt><i>nounset
<dd>Equivalent to <b>-u.
<dt><i>pipefail
<dd>Derive the exit status of a pipeline from the exit statuses of all of the commands in the pipeline, not just the last
(rightmost) command, as described in <a href="#tag_19_09_02">2.9.2 Pipelines.
<dt><i>verbose
<dd>Equivalent to <b>-v.
<dt><i>vi
<dd>Allow shell command line editing using the built-in <a href="../utilities/vi.html"><i>vi editor. Enabling <a href=
"../utilities/vi.html"><i>vi mode shall disable any other command line editing mode provided as an implementation
extension. This option shall be supported if the system supports the User Portability Utilities option.
<p class="tent">It need not be possible to set <a href="../utilities/vi.html"><i>vi mode on for certain block-mode
terminals.

<dt><i>xtrace
<dd>Equivalent to <b>-x.

<dt><b>-u
<dd>When the shell tries to expand, in a parameter expansion or an arithmetic expansion, an unset parameter other than the
<tt>&#39;@&#39; and <tt>&#39;&#42;&#39; special parameters, it shall write a message to standard error and the expansion shall fail with the
consequences specified in <a href="#tag_19_08_01">2.8.1 Consequences of Shell Errors.
<dt><b>-v
<dd>The shell shall write its input to standard error as it is read.
<dt><b>-x
<dd>The shell shall write to standard error a trace for each command after it expands the command and before it executes it. It is
unspecified whether the command that turns tracing off is traced.

<p class="tent">The default for all these options shall be off (unset) unless stated otherwise in the description of the option or
unless the shell was invoked with them on; see <a href="../utilities/sh.html"><i>sh.
<p class="tent">The remaining arguments shall be assigned in order to the positional parameters. The special parameter <tt>&#39;#&#39;
shall be set to reflect the number of positional parameters. All positional parameters shall be unset before any new values are
assigned.
<p class="tent">If the first argument is <tt>&#39;-&#39;, the results are unspecified.
<p class="tent">The special argument <tt>&#34;&#45;&#45;&#34; immediately following the <a href="#set"><i>set command name can be used
to delimit the arguments if the first argument begins with <tt>&#39;+&#39; or <tt>&#39;-&#39;, or to prevent inadvertent listing of all
shell variables when there are no arguments. The command <a href="#set"><i>set <b>&#45;&#45; without <i>argument shall
unset all positional parameters and set the special parameter <tt>&#39;#&#39; to zero.

<h4 class="mansect"><a name="tag_19_26_04" id="tag_19_26_04">OPTIONS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_26_05" id="tag_19_26_05">OPERANDS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_26_06" id="tag_19_26_06">STDIN
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_26_07" id="tag_19_26_07">INPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_26_08" id="tag_19_26_08">ENVIRONMENT VARIABLES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_26_09" id="tag_19_26_09">ASYNCHRONOUS EVENTS
<blockquote>
<p>Default.

<h4 class="mansect"><a name="tag_19_26_10" id="tag_19_26_10">STDOUT
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_26_11" id="tag_19_26_11">STDERR
<blockquote>
<p>The standard error shall be used only for diagnostic messages.

<h4 class="mansect"><a name="tag_19_26_12" id="tag_19_26_12">OUTPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_26_13" id="tag_19_26_13">EXTENDED DESCRIPTION
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_26_14" id="tag_19_26_14">EXIT STATUS
<blockquote>
<dl compact>
<dd>
<dt> 0
<dd>Successful completion.
<dt>&gt;0
<dd>An invalid option was specified, or an error occurred.

<h4 class="mansect"><a name="tag_19_26_15" id="tag_19_26_15">CONSEQUENCES OF ERRORS
<blockquote>
<p>Default.

<hr>
<div class="box"><em>The following sections are informative.
<h4 class="mansect"><a name="tag_19_26_16" id="tag_19_26_16">APPLICATION USAGE
<blockquote>
<p>Application writers should avoid relying on <a href="#set"><i>set <b>-e within functions. For example, in the
following script:
<pre>
<tt>set -e
start() {
    some&#95;server
    echo some&#95;server started successfully
}
start || echo &gt;&amp;2 some&#95;server failed

<p class="tent">the <b>-e setting is ignored within the function body (because the function is a command in an AND-OR list
other than the last). Therefore, if <tt>some&#95;server fails, the function carries on to echo <tt>&#34;some&#95;server started
successfully&#34;, and the exit status of the function is zero (which means <tt>&#34;some&#95;server failed&#34; is not output).
<p class="tent">Use of <a href="#set"><i>set <b>-n causes the shell to parse the rest of the script without executing
any commands, meaning that <a href="#set"><i>set <b>+n cannot be used to undo the effect. Syntax checking is more
commonly done via <tt>sh <tt>-n <i>script&#95;name.

<h4 class="mansect"><a name="tag_19_26_17" id="tag_19_26_17">EXAMPLES
<blockquote>
<p>Write out all variables and their values:
<pre>
<tt>set

<p class="tent">Set &#36;1, &#36;2, and &#36;3 and set <tt>&#34;&#36;#&#34; to 3:
<pre>
<tt>set c a b

<p class="tent">Turn on the <b>-x and <b>-v options:
<pre>
<tt>set -xv

<p class="tent">Unset all positional parameters:
<pre>
<tt>set &#45;&#45;

<p class="tent">Set &#36;1 to the value of <i>x, even if it begins with <tt>&#39;-&#39; or <tt>&#39;+&#39;:
<pre>
<tt>set &#45;&#45; &#34;&#36;x&#34;

<p class="tent">Set the positional parameters to the expansion of <i>x, even if <i>x expands with a leading <tt>&#39;-&#39; or
<tt>&#39;+&#39;:
<pre>
<tt>set &#45;&#45; &#36;x

<h4 class="mansect"><a name="tag_19_26_18" id="tag_19_26_18">RATIONALE
<blockquote>
<p>The <a href="#set"><i>set &#45;&#45; form is listed specifically in the SYNOPSIS even though this usage is implied by the
Utility Syntax Guidelines. The explanation of this feature removes any ambiguity about whether the <a href="#set"><i>set &#45;&#45;
form might be misinterpreted as being equivalent to <a href="#set"><i>set without any options or arguments. The
functionality of this form has been adopted from the KornShell. In System V, <a href="#set"><i>set &#45;&#45; only unsets
parameters if there is at least one argument; the only way to unset all parameters is to use <a href="#shift"><i>shift.
Using the KornShell version should not affect System V scripts because there should be no reason to issue it without arguments
deliberately; if it were issued as, for example:
<pre>
<tt>set &#45;&#45; &#34;&#36;@&#34;

<p class="tent">and there were in fact no arguments resulting from <tt>&#34;&#36;@&#34;, unsetting the parameters would have no
result.
<p class="tent">The <a href="#set"><i>set + form in early proposals was omitted as being an unnecessary duplication of
<a href="#set"><i>set alone and not widespread historical practice.
<p class="tent">The <i>noclobber option was changed to allow <a href="#set"><i>set <b>-C as well as the <a href=
"#set"><i>set <b>-o <i>noclobber option. The single-letter version was added so that the historical <tt>&#34;&#36;-&#34;
paradigm would not be broken; see <a href="#tag_19_05_02">2.5.2 Special Parameters.
<p class="tent">The description of the <b>-e option is intended to match the behavior of the 1988 version of the KornShell.
<p class="tent">The <b>-h option is related to command name hashing. See <a href="../utilities/hash.html#"><i>hash.
The normative description is deliberately vague because the way this option works varies between shell implementations.
<p class="tent">Earlier versions of this standard specified <b>-h as a way to locate and remember utilities to be invoked by
functions as those functions are defined (the utilities are normally located when the function is executed). However, this did not
match existing practice in most shells.
<p class="tent">The following <a href="#set"><i>set options were omitted intentionally with the following rationale:
<dl compact>
<dd>
<dt><b>-k
<dd>The <b>-k option was originally added by the author of the Bourne shell to make it easier for users of pre-release versions
of the shell. In early versions of the Bourne shell the construct <a href="#set"><i>set <i>name=<i>value had to be
used to assign values to shell variables. The problem with <b>-k is that the behavior affects parsing, virtually precluding
writing any compilers. To explain the behavior of <b>-k, it is necessary to describe the parsing algorithm, which is
implementation-defined. For example:
<pre>
<tt>set -k; echo <i>name<tt>=<i>value<tt>

<p class="tent">and:
<pre>
<tt>set -k
echo <i>name<tt>=<i>value<tt>

<p class="tent">behave differently. The interaction with functions is even more complex. What is more, the <b>-k option is
never needed, since the command line could have been reordered.

<dt><b>-t
<dd>The <b>-t option is hard to specify and almost never used. The only known use could be done with here-documents. Moreover,
the behavior with <i>ksh and <a href="../utilities/sh.html"><i>sh differs. The reference page says that it exits after
reading and executing one command. What is one command? If the input is <i>date;<i>date, <a href=
"../utilities/sh.html"><i>sh executes both <a href="../utilities/date.html"><i>date commands while <i>ksh does
only the first.

<p class="tent">Consideration was given to rewriting <a href="#set"><i>set to simplify its confusing syntax. A specific
suggestion was that the <a href="#unset"><i>unset utility should be used to unset options instead of using the non-<a href=
"../functions/getopt.html"><i>getopt()-able +<i>option syntax. However, the conclusion was reached that the historical
practice of using +<i>option was satisfactory and that there was no compelling reason to modify such widespread historical
practice.
<p class="tent">The <b>-o option was adopted from the KornShell to address user needs. In addition to its generally friendly
interface, <b>-o is needed to provide the <a href="../utilities/vi.html"><i>vi command line editing mode, for which
historical practice yields no single-letter option name. (Although it might have been possible to invent such a letter, it was
recognized that other editing modes would be developed and <b>-o provides ample name space for describing such extensions.)
<p class="tent">Historical implementations are inconsistent in the format used for <b>-o option status reporting. The <b>+o
format without an option-argument was added to allow portable access to the options that can be saved and then later restored
using, for instance, a dot script.
<p class="tent">Historically, <a href="../utilities/sh.html"><i>sh did trace the command <a href="#set"><i>set
<b>+x, but <i>ksh did not.
<p class="tent">The <i>ignoreeof setting prevents accidental logouts when the end-of-file character (typically
&lt;control&gt;-D) is entered. A user shall explicitly <a href="#exit"><i>exit to leave the interactive shell.
<p class="tent">The <a href="#set"><i>set <b>-m option was added to apply only to the UPE because it applies primarily
to interactive use, not shell script applications.
<p class="tent">The ability to do asynchronous notification became available in the 1988 version of the KornShell. To have it
occur, the user had to issue the command:
<pre>
<tt>trap &#34;jobs -n&#34; CLD

<p class="tent">The C shell provides two different levels of an asynchronous notification capability. The environment variable
<i>notify is analogous to what is done in <a href="#set"><i>set <b>-b or <a href="#set"><i>set <b>-o
<i>notify. When set, it notifies the user immediately of background job completions. When unset, this capability is turned
off.
<p class="tent">The other notification ability comes through the built-in utility <i>notify. The syntax is:
<pre>
<tt>notify <b>&#91;<tt>%job &#46;&#46;&#46; <b>&#93;<tt>

<p class="tent">By issuing <i>notify with no operands, it causes the C shell to notify the user asynchronously when the state
of the current job changes. If given operands, <i>notify asynchronously informs the user of changes in the states of the
specified jobs.
<p class="tent">To add asynchronous notification to the POSIX shell, neither the KornShell extensions to <a href=
"#trap"><i>trap, nor the C shell <i>notify environment variable seemed appropriate (<i>notify is not a proper POSIX
environment variable name).
<p class="tent">The <a href="#set"><i>set <b>-b option was selected as a compromise.
<p class="tent">The <i>notify built-in was considered to have more functionality than was required for simple asynchronous
notification.
<p class="tent">Historically, some shells applied the <b>-u option to all parameters including <tt>&#36;@ and <tt>&#36;&#42;. The
standard developers felt that this was a misfeature since it is normal and common for <tt>&#36;@ and <tt>&#36;&#42; to be used in
shell scripts regardless of whether they were passed any arguments. Treating these uses as an error when no arguments are passed
reduces the value of <b>-u for its intended purpose of finding spelling mistakes in variable names and uses of unset positional
parameters.

<h4 class="mansect"><a name="tag_19_26_19" id="tag_19_26_19">FUTURE DIRECTIONS
<blockquote>
<p>A future version of this standard may remove the <b>-o <i>nolog option.

<h4 class="mansect"><a name="tag_19_26_20" id="tag_19_26_20">SEE ALSO
<blockquote>
<p><a href="#tag_19_15">2.15 Special Built-In Utilities, <a href="../utilities/hash.html#"><i>hash
<p class="tent">XBD <a href="../basedefs/V1_chap04.html#tag_04_26"><i>4.26 Variable Assignment, <a href=
"../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines

<h4 class="mansect"><a name="tag_19_26_21" id="tag_19_26_21">CHANGE HISTORY
<h4 class="mansect"><a name="tag_19_26_22" id="tag_19_26_22">Issue 6
<blockquote>
<p>The obsolescent <a href="#set"><i>set command name followed by <tt>&#39;-&#39; has been removed.
<p class="tent">The following new requirements on POSIX implementations derive from alignment with the Single UNIX
Specification:
<ul>
<li class="tent">The <i>nolog option is added to <a href="#set"><i>set <b>-o.

<p class="tent">IEEE PASC Interpretation 1003.2 #167 is applied, clarifying that the options default also takes into account the
description of the option.
<p class="tent">IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/5 is applied so that the reference page sections
use terms as described in the Utility Description Defaults ( <a href="../utilities/V3_chap01.html#tag_18_04"><i>1.4 Utility
Description Defaults). No change in behavior is intended.
<p class="tent">IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/8 is applied, changing the square brackets in the
example in RATIONALE to be in bold, which is the typeface used for optional items.

<h4 class="mansect"><a name="tag_19_26_23" id="tag_19_26_23">Issue 7
<blockquote>
<p>Austin Group Interpretation 1003.1-2001 #027 is applied, clarifying the behavior if the first argument is <tt>&#39;-&#39;.
<p class="tent">SD5-XCU-ERN-97 is applied, updating the SYNOPSIS.
<p class="tent">XSI shading is removed from the <b>-h functionality.
<p class="tent">POSIX.1-2008, Technical Corrigendum 1, XCU/TC1-2008/0046 &#91;52&#93;, XCU/TC1-2008/0047 &#91;155,280&#93;, XCU/TC1-2008/0048 &#91;52&#93;,
XCU/TC1-2008/0049 &#91;52&#93;, and XCU/TC1-2008/0050 &#91;155,430&#93; are applied.
<p class="tent">POSIX.1-2008, Technical Corrigendum 2, XCU/TC2-2008/0053 &#91;584&#93;, XCU/TC2-2008/0054 &#91;717&#93;, XCU/TC2-2008/0055 &#91;717&#93;,
and XCU/TC2-2008/0056 &#91;960&#93; are applied.

<h4 class="mansect"><a name="tag_19_26_24" id="tag_19_26_24">Issue 8
<blockquote>
<p>Austin Group Defect 559 is applied, changing the description of the <b>-u option.
<p class="tent">Austin Group Defect 789 is applied, adding <b>-o <i>pipefail.
<p class="tent">Austin Group Defect 981 is applied, changing the description of the <b>-o <i>nolog option and the FUTURE
DIRECTIONS section.
<p class="tent">Austin Group Defects 1009 and 1555 are applied, changing the description of the <b>-a option.
<p class="tent">Austin Group Defect 1016 is applied, changing the description of the <b>-C option.
<p class="tent">Austin Group Defect 1055 is applied, adding a paragraph about the <b>-n option to the APPLICATION USAGE
section.
<p class="tent">Austin Group Defect 1063 is applied, changing the description of the <b>-h option.
<p class="tent">Austin Group Defect 1150 is applied, changing the description of the <b>-e option.
<p class="tent">Austin Group Defect 1207 is applied, clarifying which option-arguments of the <b>-o option are related to the
User Portability Utilities option.
<p class="tent">Austin Group Defect 1254 is applied, changing the descriptions of the <b>-b and <b>-m options.
<p class="tent">Austin Group Defect 1384 is applied, allowing subshells of interactive shells to ignore the <b>-n option.

<div class="box"><em>End of informative text.
<hr>

 <a name="shift" id="shift"> <a name=
"tag_19_27" id="tag_19_27"><!-- shift -->
<h4 class="mansect"><a name="tag_19_27_01" id="tag_19_27_01">NAME
<blockquote>shift — shift positional parameters
<h4 class="mansect"><a name="tag_19_27_02" id="tag_19_27_02">SYNOPSIS
<blockquote class="synopsis">
<p><code><tt>shift <b>&#91;<i>n<b>&#93;

<h4 class="mansect"><a name="tag_19_27_03" id="tag_19_27_03">DESCRIPTION
<blockquote>
<p>The positional parameters shall be shifted. Positional parameter 1 shall be assigned the value of parameter (1+<i>n),
parameter 2 shall be assigned the value of parameter (2+<i>n), and so on. The parameters represented by the numbers
<tt>&#34;&#36;#&#34; down to <tt>&#34;&#36;#-n+1&#34; shall be unset, and the parameter <tt>&#39;#&#39; is updated to reflect the new number of
positional parameters.
<p class="tent">The value <i>n shall be an unsigned decimal integer less than or equal to the value of the special parameter
<tt>&#39;#&#39;. If <i>n is not given, it shall be assumed to be 1. If <i>n is 0, the positional and special parameters are
not changed.

<h4 class="mansect"><a name="tag_19_27_04" id="tag_19_27_04">OPTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_27_05" id="tag_19_27_05">OPERANDS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_27_06" id="tag_19_27_06">STDIN
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_27_07" id="tag_19_27_07">INPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_27_08" id="tag_19_27_08">ENVIRONMENT VARIABLES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_27_09" id="tag_19_27_09">ASYNCHRONOUS EVENTS
<blockquote>
<p>Default.

<h4 class="mansect"><a name="tag_19_27_10" id="tag_19_27_10">STDOUT
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_27_11" id="tag_19_27_11">STDERR
<blockquote>
<p>The standard error shall be used only for diagnostic messages and the warning message specified in EXIT STATUS.

<h4 class="mansect"><a name="tag_19_27_12" id="tag_19_27_12">OUTPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_27_13" id="tag_19_27_13">EXTENDED DESCRIPTION
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_27_14" id="tag_19_27_14">EXIT STATUS
<blockquote>
<p>If the <i>n operand is invalid or is greater than <tt>&#34;&#36;#&#34;, this may be treated as an error and a non-interactive shell
may exit; if the shell does not exit in this case, a non-zero exit status shall be returned and a warning message shall be written
to standard error. Otherwise, zero shall be returned.

<h4 class="mansect"><a name="tag_19_27_15" id="tag_19_27_15">CONSEQUENCES OF ERRORS
<blockquote>
<p>Default.

<hr>
<div class="box"><em>The following sections are informative.
<h4 class="mansect"><a name="tag_19_27_16" id="tag_19_27_16">APPLICATION USAGE
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_27_17" id="tag_19_27_17">EXAMPLES
<blockquote>
<pre>
<b>
&#36;<tt>
 set a b c d e
<b>
&#36;<tt>
 shift 2
<b>
&#36;<tt>
 echo &#36;&#42;
<b>
c d e<tt>

<h4 class="mansect"><a name="tag_19_27_18" id="tag_19_27_18">RATIONALE
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_27_19" id="tag_19_27_19">FUTURE DIRECTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_27_20" id="tag_19_27_20">SEE ALSO
<blockquote>
<p><a href="#tag_19_15">2.15 Special Built-In Utilities

<h4 class="mansect"><a name="tag_19_27_21" id="tag_19_27_21">CHANGE HISTORY
<h4 class="mansect"><a name="tag_19_27_22" id="tag_19_27_22">Issue 6
<blockquote>
<p>IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/5 is applied so that the reference page sections use terms as
described in the Utility Description Defaults ( <a href="../utilities/V3_chap01.html#tag_18_04"><i>1.4 Utility Description
Defaults). No change in behavior is intended.

<h4 class="mansect"><a name="tag_19_27_23" id="tag_19_27_23">Issue 7
<blockquote>
<p>POSIX.1-2008, Technical Corrigendum 1, XCU/TC1-2008/0051 &#91;459&#93; is applied.

<h4 class="mansect"><a name="tag_19_27_24" id="tag_19_27_24">Issue 8
<blockquote>
<p>Austin Group Defect 1265 is applied, updating the EXIT STATUS and STDERR sections to align with the changes made to <a href=
"#tag_19_08_01">2.8.1 Consequences of Shell Errors between Issue 6 and Issue 7.

<div class="box"><em>End of informative text.
<hr>

 <a name="times" id="times"> <a name=
"tag_19_28" id="tag_19_28"><!-- times -->
<h4 class="mansect"><a name="tag_19_28_01" id="tag_19_28_01">NAME
<blockquote>times — write process times
<h4 class="mansect"><a name="tag_19_28_02" id="tag_19_28_02">SYNOPSIS
<blockquote class="synopsis">
<p><code><tt>times

<h4 class="mansect"><a name="tag_19_28_03" id="tag_19_28_03">DESCRIPTION
<blockquote>
<p>The <a href="#times"><i>times utility shall write the accumulated user and system times for the shell and for all of its
child processes, in the following POSIX locale format:
<pre>
<tt>&#34;%dm%fs %dm%fs&#92;n%dm%fs %dm%fs&#92;n&#34;, &lt;<i>shell user minutes<tt>&gt;,
    &lt;<i>shell user seconds<tt>&gt;, &lt;<i>shell system minutes<tt>&gt;,
    &lt;<i>shell system seconds<tt>&gt;, &lt;<i>children user minutes<tt>&gt;,
    &lt;<i>children user seconds<tt>&gt;, &lt;<i>children system minutes<tt>&gt;,
    &lt;<i>children system seconds<tt>&gt;

<p class="tent">The four pairs of times shall correspond to the members of the <a href=
"../basedefs/sys_times.h.html"><i>&lt;sys/times.h&gt; <b>tms structure (defined in XBD <a href=
"../basedefs/V1_chap14.html#tag_14"><i>14. Headers) as returned by <a href="../functions/times.html"><i>times():
<i>tms&#95;utime, <i>tms&#95;stime, <i>tms&#95;cutime, and <i>tms&#95;cstime, respectively.

<h4 class="mansect"><a name="tag_19_28_04" id="tag_19_28_04">OPTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_28_05" id="tag_19_28_05">OPERANDS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_28_06" id="tag_19_28_06">STDIN
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_28_07" id="tag_19_28_07">INPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_28_08" id="tag_19_28_08">ENVIRONMENT VARIABLES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_28_09" id="tag_19_28_09">ASYNCHRONOUS EVENTS
<blockquote>
<p>Default.

<h4 class="mansect"><a name="tag_19_28_10" id="tag_19_28_10">STDOUT
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_28_11" id="tag_19_28_11">STDERR
<blockquote>
<p>The standard error shall be used only for diagnostic messages.

<h4 class="mansect"><a name="tag_19_28_12" id="tag_19_28_12">OUTPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_28_13" id="tag_19_28_13">EXTENDED DESCRIPTION
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_28_14" id="tag_19_28_14">EXIT STATUS
<blockquote>
<dl compact>
<dd>
<dt> 0
<dd>Successful completion.
<dt>&gt;0
<dd>An error occurred.

<h4 class="mansect"><a name="tag_19_28_15" id="tag_19_28_15">CONSEQUENCES OF ERRORS
<blockquote>
<p>Default.

<hr>
<div class="box"><em>The following sections are informative.
<h4 class="mansect"><a name="tag_19_28_16" id="tag_19_28_16">APPLICATION USAGE
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_28_17" id="tag_19_28_17">EXAMPLES
<blockquote>
<pre>
<b>
&#36;<tt>
 times
<b>
0m0.43s 0m1.11s
8m44.18s 1m43.23s<tt>

<h4 class="mansect"><a name="tag_19_28_18" id="tag_19_28_18">RATIONALE
<blockquote>
<p>The <a href="#times"><i>times special built-in from the Single UNIX Specification is now required for all conforming
shells.

<h4 class="mansect"><a name="tag_19_28_19" id="tag_19_28_19">FUTURE DIRECTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_28_20" id="tag_19_28_20">SEE ALSO
<blockquote>
<p><a href="#tag_19_15">2.15 Special Built-In Utilities
<p class="tent">XBD <a href="../basedefs/sys_times.h.html"><i>&lt;sys/times.h&gt;

<h4 class="mansect"><a name="tag_19_28_21" id="tag_19_28_21">CHANGE HISTORY
<h4 class="mansect"><a name="tag_19_28_22" id="tag_19_28_22">Issue 6
<blockquote>
<p>IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/9 is applied, changing text in the DESCRIPTION from: &#34;Write the
accumulated user and system times for the shell and for all of its child processes &#46;&#46;&#46;&#34; to: &#34;The <a href=
"#times"><i>times utility shall write the accumulated user and system times for the shell and for all of its child
processes &#46;&#46;&#46;&#34;.

<h4 class="mansect"><a name="tag_19_28_23" id="tag_19_28_23">Issue 7
<blockquote>
<p>POSIX.1-2008, Technical Corrigendum 2, XCU/TC2-2008/0056 &#91;960&#93; is applied.

<div class="box"><em>End of informative text.
<hr>

 <a name="trap" id="trap"> <a name=
"tag_19_29" id="tag_19_29"><!-- trap -->
<h4 class="mansect"><a name="tag_19_29_01" id="tag_19_29_01">NAME
<blockquote>trap — trap signals
<h4 class="mansect"><a name="tag_19_29_02" id="tag_19_29_02">SYNOPSIS
<blockquote class="synopsis">
<p><code><tt>trap <i>n <b>&#91;<i>condition<tt>&#46;&#46;&#46;<b>&#93; <tt><br>
 <br>
trap -p <b>&#91;<i>condition<tt>&#46;&#46;&#46;<b>&#93; <tt><br>
 <br>
trap <b>&#91;<i>action condition<tt>&#46;&#46;&#46;<b>&#93;

<h4 class="mansect"><a name="tag_19_29_03" id="tag_19_29_03">DESCRIPTION
<blockquote>
<p>If the <b>-p option is not specified and the first operand is an unsigned decimal integer, the shell shall treat all
operands as conditions, and shall reset each condition to the default value. Otherwise, if the <b>-p option is not specified
and there are operands, the first operand shall be treated as an action and the remaining as conditions.
<p class="tent">If <i>action is <tt>&#39;-&#39;, the shell shall reset each <i>condition to the default value. If
<i>action is null (<tt>&#34;&#34;), the shell shall ignore each specified <i>condition if it arises. Otherwise, the argument
<i>action shall be read and executed by the shell when one of the corresponding conditions arises. The action of <a href=
"#trap"><i>trap shall override a previous action (either default action or one explicitly set). The value of <tt>&#34;&#36;?&#34;
after the <a href="#trap"><i>trap action completes shall be the value it had before the <a href="#trap"><i>trap
action was executed.
<p class="tent">The condition can be EXIT, 0 (equivalent to EXIT), or a signal specified using a symbolic name, without the SIG
prefix, as listed in the tables of signal names in the <a href="../basedefs/signal.h.html"><i>&lt;signal.h&gt; header
defined in XBD <a href="../basedefs/V1_chap14.html#tag_14"><i>14. Headers; for example, HUP, INT, QUIT, TERM.
Implementations may permit names with the SIG prefix or ignore case in signal names as an extension. Setting a trap for SIGKILL or
SIGSTOP produces undefined results.
<p class="tent">The EXIT condition shall occur when the shell terminates normally (exits), and may occur when the shell terminates
abnormally as a result of delivery of a signal (other than SIGKILL) whose <a href="#trap"><i>trap action is the
default.
<p class="tent">The environment in which the shell executes a <a href="#trap"><i>trap action on EXIT shall be identical to
the environment immediately after the last command executed before the <a href="#trap"><i>trap action on EXIT was
executed.
<p class="tent">If <i>action is neither <tt>&#39;-&#39; nor the empty string, then each time a matching <i>condition arises,
the <i>action shall be executed in a manner equivalent to:
<pre>
<tt>eval <i>action<tt>

<p class="tent">Signals that were ignored on entry to a non-interactive shell cannot be trapped or reset, although no error need be
reported when attempting to do so. An interactive shell may reset or catch signals ignored on entry. Traps shall remain in place
for a given shell until explicitly changed with another <a href="#trap"><i>trap command.
<p class="tent">When a subshell is entered, traps that are not being ignored shall be set to the default actions, except in the
case of a command substitution containing only a single <a href="#trap"><i>trap command, when the traps need not be
altered. Implementations may check for this case using only lexical analysis; for example, if <tt>&#96;trap&#96; and <tt>&#36;( trap &#45;&#45;
) do not alter the traps in the subshell, cases such as assigning <tt>var=trap and then using <tt>&#36;(&#36;var) may still
alter them. This does not imply that the <a href="#trap"><i>trap command cannot be used within the subshell to set new
traps.
<p class="tent">The <a href="#trap"><i>trap command with no operands shall write to standard output a list of commands
associated with each of a set of conditions; if the <b>-p option is not specified, this set shall contain only the conditions
that are not in the default state (including signals that were ignored on entry to a non-interactive shell); if the <b>-p
option is specified, the set shall contain all conditions, except that it is unspecified whether conditions corresponding to the
SIGKILL and SIGSTOP signals are included in the set. If the command is executed in a subshell, the implementation does not perform
the optional check described above for a command substitution containing only a single <a href="#trap"><i>trap command, and
no <a href="#trap"><i>trap commands with operands have been executed since entry to the subshell, the list shall contain
the commands that were associated with each condition immediately before the subshell environment was entered. Otherwise, the list
shall contain the commands currently associated with each condition. The format shall be:
<pre>
<tt>&#34;trap &#45;&#45; %s %s &#46;&#46;&#46;&#92;n&#34;, &lt;<i>action<tt>&gt;, &lt;<i>condition<tt>&gt; &#46;&#46;&#46;

<p class="tent">The shell shall format the output, including the proper use of quoting, so that it is suitable for reinput to the
shell as commands that achieve the same trapping results for the set of conditions included in the output, except for signals that
were ignored on entry to the shell as described above. If this set includes conditions corresponding to the SIGKILL and SIGSTOP
signals, the shell shall accept them when the output is reinput to the shell (where accepting them means they do not cause a
non-zero exit status, a diagnostic message, or undefined behavior). For example:
<pre>
<tt>save&#95;traps=&#36;(trap -p)
<br class="tent">
&#46;&#46;&#46;
eval &#34;&#36;save&#95;traps&#34;

<p class="tent">or:
<pre>
<tt>save&#95;traps=&#36;(trap -p INT QUIT)
trap &#34;some command&#34; INT QUIT
<br class="tent">
&#46;&#46;&#46;
<br class="tent">
eval &#34;&#36;save&#95;traps&#34;

<p class="tent"><sup>&#91;<a href="javascript:open_code('XSI')">XSI&#93; <img src=".pic/opt-start.gif" alt="[Option Start]"
border="0"> XSI-conformant systems also allow numeric signal numbers for the conditions corresponding to the following signal
names:
<dl compact>
<dd>
<dt>1
<dd>SIGHUP
<dt>2
<dd>SIGINT
<dt>3
<dd>SIGQUIT
<dt>6
<dd>SIGABRT
<dt>9
<dd>SIGKILL
<dt>14
<dd>SIGALRM
<dt>15
<dd>SIGTERM

<img src=".pic/opt-end.gif" alt="[Option End]" border="0">
<p class="tent">If an invalid signal name <sup>&#91;<a href="javascript:open_code('XSI')">XSI&#93; <img src=".pic/opt-start.gif" alt="[Option Start]" border="0">  or number <img src=".pic/opt-end.gif" alt="[Option End]"
border="0"> is specified, the <a href="#trap"><i>trap utility shall write a warning message to standard error.
<p class="tent">The <a href="#trap"><i>trap special built-in shall conform to XBD <a href=
"../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines.

<h4 class="mansect"><a name="tag_19_29_04" id="tag_19_29_04">OPTIONS
<blockquote>
<p>The following option shall be supported:
<dl compact>
<dd>
<dt><b>-p
<dd>Write to standard output a list of commands associated with each <i>condition operand. The behavior when there are no
operands is specified in the DESCRIPTION section.
<p class="tent">The shell shall format the output, including the proper use of quoting, so that it is suitable for reinput to the
shell as commands that achieve the same trapping results for the specified set of conditions. If a <i>condition operand is a
condition corresponding to the SIGKILL or SIGSTOP signal, and <a href="#trap"><i>trap <b>-p without any operands would
not include it in the set of conditions for which it writes output, the behavior is undefined if the output is reinput to the
shell.

<h4 class="mansect"><a name="tag_19_29_05" id="tag_19_29_05">OPERANDS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_29_06" id="tag_19_29_06">STDIN
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_29_07" id="tag_19_29_07">INPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_29_08" id="tag_19_29_08">ENVIRONMENT VARIABLES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_29_09" id="tag_19_29_09">ASYNCHRONOUS EVENTS
<blockquote>
<p>Default.

<h4 class="mansect"><a name="tag_19_29_10" id="tag_19_29_10">STDOUT
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_29_11" id="tag_19_29_11">STDERR
<blockquote>
<p>The standard error shall be used only for diagnostic messages and warning messages about invalid signal names <sup>&#91;<a href=
"javascript:open_code('XSI')">XSI&#93; <img src=".pic/opt-start.gif" alt="[Option Start]" border="0">  or numbers.
<img src=".pic/opt-end.gif" alt="[Option End]" border="0">

<h4 class="mansect"><a name="tag_19_29_12" id="tag_19_29_12">OUTPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_29_13" id="tag_19_29_13">EXTENDED DESCRIPTION
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_29_14" id="tag_19_29_14">EXIT STATUS
<blockquote>
<p>If the trap name <sup>&#91;<a href="javascript:open_code('XSI')">XSI&#93; <img src=".pic/opt-start.gif" alt=
"[Option Start]" border="0">  or number <img src=".pic/opt-end.gif" alt="[Option End]" border="0"> is invalid, a non-zero
exit status shall be returned; otherwise, zero shall be returned. For both interactive and non-interactive shells, invalid signal
names <sup>&#91;<a href="javascript:open_code('XSI')">XSI&#93; <img src=".pic/opt-start.gif" alt="[Option Start]" border=
"0">  or numbers <img src=".pic/opt-end.gif" alt="[Option End]" border="0"> shall not be considered an error and shall
not cause the shell to abort.

<h4 class="mansect"><a name="tag_19_29_15" id="tag_19_29_15">CONSEQUENCES OF ERRORS
<blockquote>
<p>Default.

<hr>
<div class="box"><em>The following sections are informative.
<h4 class="mansect"><a name="tag_19_29_16" id="tag_19_29_16">APPLICATION USAGE
<blockquote>
<p>When the <b>-p option is not used, since <a href="#trap"><i>trap with no operands does not output commands to
restore traps that are currently set to default, these need to be restored separately. The RATIONALE section shows examples and
describes their drawbacks.

<h4 class="mansect"><a name="tag_19_29_17" id="tag_19_29_17">EXAMPLES
<blockquote>
<p>Write out a list of all traps and actions:
<pre>
<tt>trap

<p class="tent">Set a trap so the <i>logout utility in the directory referred to by the <i>HOME environment variable
executes when the shell terminates:
<pre>
<tt>trap &#39;&#34;&#36;HOME&#34;/logout&#39; EXIT

<p class="tent">or:
<pre>
<tt>trap &#39;&#34;&#36;HOME&#34;/logout&#39; 0

<p class="tent">Unset traps on INT, QUIT, TERM, and EXIT:
<pre>
<tt>trap - INT QUIT TERM EXIT

<h4 class="mansect"><a name="tag_19_29_18" id="tag_19_29_18">RATIONALE
<blockquote>
<p>Implementations may permit lowercase signal names as an extension. Implementations may also accept the names with the SIG
prefix; no known historical shell does so. The <a href="#trap"><i>trap and <a href="../utilities/kill.html"><i>kill
utilities in this volume of POSIX.1-2024 are now consistent in their omission of the SIG prefix for signal names. Some <a href=
"../utilities/kill.html"><i>kill implementations do not allow the prefix, and <a href=
"../utilities/kill.html"><i>kill <b>-l lists the signals without prefixes.
<p class="tent">Trapping SIGKILL or SIGSTOP is syntactically accepted by some historical implementations, but it has no effect.
Portable POSIX applications cannot attempt to trap these signals.
<p class="tent">The output format is not historical practice. Since the output of historical <a href="#trap"><i>trap
commands is not portable (because numeric signal values are not portable) and had to change to become so, an opportunity was taken
to format the output in a way that a shell script could use to save and then later reuse a trap if it wanted.
<p class="tent">The KornShell uses an <b>ERR trap that is triggered whenever <a href="#set"><i>set <b>-e would
cause an exit. This is allowable as an extension, but was not mandated, as other shells have not used it.
<p class="tent">The text about the environment for the EXIT trap invalidates the behavior of some historical versions of
interactive shells which, for example, close the standard input before executing a trap on 0. For example, in some historical
interactive shell sessions the following trap on 0 would always print <tt>&#34;&#45;&#45;&#34;:
<pre>
<tt>trap &#39;read foo; echo &#34;-&#36;foo-&#34;&#39; 0

<p class="tent">The command:
<pre>
<tt>trap &#39;eval &#34; &#36;cmd&#34;&#39; 0

<p class="tent">causes the contents of the shell variable <i>cmd to be executed as a command when the shell exits. Using:
<pre>
<tt>trap &#39;&#36;cmd&#39; 0

<p class="tent">does not work correctly if <i>cmd contains any special characters such as quoting or redirections. Using:
<pre>
<tt>trap &#34; &#36;cmd&#34; 0

<p class="tent">also works (the leading &lt;space&gt; character protects against unlikely cases where <i>cmd is a decimal
integer or begins with <tt>&#39;-&#39;), but it expands the <i>cmd variable when the <a href="#trap"><i>trap command is
executed, not when the exit action is executed.
<p class="tent">The <b>-p option was added because without it the method used to restore traps needs to include special
handling of traps that are set to default when <a href="#trap"><i>trap with no operands is used to save the current traps.
One example is:
<pre>
<tt>save&#95;traps=&#36;(trap)
trap &#34;some command&#34; INT QUIT
save&#95;traps=&#34;trap - INT QUIT; &#36;save&#95;traps&#34;
<br class="tent">
&#46;&#46;&#46;
<br class="tent">
eval &#34;&#36;save&#95;traps&#34;

<p class="tent">but this method relies on hard-coding the commands to reset the traps that are being set. It also has a race
condition if INT or QUIT was not set to default when saved, since it first sets them to default and then restores the saved traps.
A more general approach would be:
<pre>
<tt>save&#95;traps=&#36;(trap)
&#46;&#46;&#46;
for sig in EXIT &#36;( kill -l )
do
    case &#34;&#36;sig&#34; in
    SIGKILL | KILL | sigkill | kill | SIGSTOP | STOP | sigstop | stop)
    ;;
    &#42;) trap - &#36;sig
    ;;
    esac
done
eval &#34;&#36;save&#95;traps&#34;

<p class="tent">This has the same race condition since it first sets all traps (that can be set) to default and then restores those
that were not previously set to default.
<p class="tent">Historically, some shells behaved the same with and without <b>-p when there are no operands. This standard
requires that the set of conditions differs between the two cases: with <b>-p it is all conditions (except possibly SIGKILL and
SIGSTOP); without <b>-p it is only the conditions that are not in the default state.

<h4 class="mansect"><a name="tag_19_29_19" id="tag_19_29_19">FUTURE DIRECTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_29_20" id="tag_19_29_20">SEE ALSO
<blockquote>
<p><a href="#tag_19_15">2.15 Special Built-In Utilities
<p class="tent">XBD <a href="../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines, <a href=
"../basedefs/signal.h.html"><i>&lt;signal.h&gt;

<h4 class="mansect"><a name="tag_19_29_21" id="tag_19_29_21">CHANGE HISTORY
<h4 class="mansect"><a name="tag_19_29_22" id="tag_19_29_22">Issue 6
<blockquote>
<p>XSI-conforming implementations provide the mapping of signal names to numbers given above (previously this had been marked
obsolescent). Other implementations need not provide this optional mapping.
<p class="tent">IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/5 is applied so that the reference page sections
use terms as described in the Utility Description Defaults ( <a href="../utilities/V3_chap01.html#tag_18_04"><i>1.4 Utility
Description Defaults). No change in behavior is intended.

<h4 class="mansect"><a name="tag_19_29_23" id="tag_19_29_23">Issue 7
<blockquote>
<p>SD5-XCU-ERN-97 is applied, updating the SYNOPSIS.
<p class="tent">Austin Group Interpretation 1003.1-2001 #116 is applied.
<p class="tent">POSIX.1-2008, Technical Corrigendum 1, XCU/TC1-2008/0052 &#91;53,268,440&#93;, XCU/TC1-2008/0053 &#91;53,268,440&#93;,
XCU/TC1-2008/0054 &#91;163&#93;, XCU/TC1-2008/0055 &#91;163&#93;, and XCU/TC1-2008/0056 &#91;163&#93; are applied.

<h4 class="mansect"><a name="tag_19_29_24" id="tag_19_29_24">Issue 8
<blockquote>
<p>Austin Group Defect 621 is applied, clarifying when the EXIT condition occurs.
<p class="tent">Austin Group Defect 1029 is applied, clarifying the execution of <a href="#trap"><i>trap actions.
<p class="tent">Austin Group Defects 1211 and 1212 are applied, adding the <b>-p option and clarifying that, when <b>-p is
not specified, the output of <a href="#trap"><i>trap with no operands does not list conditions that are in the default
state.
<p class="tent">Austin Group Defect 1265 is applied, updating the DESCRIPTION, STDERR and EXIT STATUS sections to align with the
changes made to <a href="#tag_19_08_01">2.8.1 Consequences of Shell Errors between Issue 6 and Issue 7.
<p class="tent">Austin Group Defect 1285 is applied, inserting a blank line between the two SYNOPSIS lines.

<div class="box"><em>End of informative text.
<hr>

 <a name="unset" id="unset"> <a name=
"tag_19_30" id="tag_19_30"><!-- unset -->
<h4 class="mansect"><a name="tag_19_30_01" id="tag_19_30_01">NAME
<blockquote>unset — unset values and attributes of variables and functions
<h4 class="mansect"><a name="tag_19_30_02" id="tag_19_30_02">SYNOPSIS
<blockquote class="synopsis">
<p><code><tt>unset <b>&#91;<tt>-fv<b>&#93; <i>name<tt>&#46;&#46;&#46;

<h4 class="mansect"><a name="tag_19_30_03" id="tag_19_30_03">DESCRIPTION
<blockquote>
<p>The <a href="#unset"><i>unset utility shall unset each variable or function definition specified by <i>name that
does not have the <i>readonly attribute and remove any attributes other than <i>readonly that have been given to
<i>name (see <a href="#tag_19_15">2.15 Special Built-In Utilities <i>export and <i>readonly).
<p class="tent">If <b>-v is specified, <i>name refers to a variable name and the shell shall unset it and remove it from
the environment. Read-only variables cannot be unset.
<p class="tent">If <b>-f is specified, <i>name refers to a function and the shell shall unset the function definition.
<p class="tent">If neither <b>-f nor <b>-v is specified, <i>name refers to a variable; if a variable by that name does
not exist, it is unspecified whether a function by that name, if any, shall be unset.
<p class="tent">Unsetting a variable or function that was not previously set shall not be considered an error and does not cause
the shell to abort.
<p class="tent">The <a href="#unset"><i>unset special built-in shall support XBD <a href=
"../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines.
<p class="tent">Note that:
<pre>
<tt>VARIABLE=

<p class="tent">is not equivalent to an <a href="#unset"><i>unset of <b>VARIABLE; in the example, <b>VARIABLE is
set to <tt>&#34;&#34;. Also, the variables that can be <a href="#unset"><i>unset should not be misinterpreted to include the
special parameters (see <a href="#tag_19_05_02">2.5.2 Special Parameters).

<h4 class="mansect"><a name="tag_19_30_04" id="tag_19_30_04">OPTIONS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_30_05" id="tag_19_30_05">OPERANDS
<blockquote>
<p>See the DESCRIPTION.

<h4 class="mansect"><a name="tag_19_30_06" id="tag_19_30_06">STDIN
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_30_07" id="tag_19_30_07">INPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_30_08" id="tag_19_30_08">ENVIRONMENT VARIABLES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_30_09" id="tag_19_30_09">ASYNCHRONOUS EVENTS
<blockquote>
<p>Default.

<h4 class="mansect"><a name="tag_19_30_10" id="tag_19_30_10">STDOUT
<blockquote>
<p>Not used.

<h4 class="mansect"><a name="tag_19_30_11" id="tag_19_30_11">STDERR
<blockquote>
<p>The standard error shall be used only for diagnostic messages.

<h4 class="mansect"><a name="tag_19_30_12" id="tag_19_30_12">OUTPUT FILES
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_30_13" id="tag_19_30_13">EXTENDED DESCRIPTION
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_30_14" id="tag_19_30_14">EXIT STATUS
<blockquote>
<dl compact>
<dd>
<dt> 0
<dd>All <i>name operands were successfully unset.
<dt>&gt;0
<dd>At least one <i>name could not be unset.

<h4 class="mansect"><a name="tag_19_30_15" id="tag_19_30_15">CONSEQUENCES OF ERRORS
<blockquote>
<p>Default.

<hr>
<div class="box"><em>The following sections are informative.
<h4 class="mansect"><a name="tag_19_30_16" id="tag_19_30_16">APPLICATION USAGE
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_30_17" id="tag_19_30_17">EXAMPLES
<blockquote>
<p>Unset <i>VISUAL variable:
<pre>
<tt>unset -v VISUAL

<p class="tent">Unset the functions <b>foo and <b>bar:
<pre>
<tt>unset -f foo bar

<h4 class="mansect"><a name="tag_19_30_18" id="tag_19_30_18">RATIONALE
<blockquote>
<p>Consideration was given to omitting the <b>-f option in favor of an <i>unfunction utility, but the standard developers
decided to retain historical practice.
<p class="tent">The <b>-v option was introduced because System V historically used one name space for both variables and
functions. When <a href="#unset"><i>unset is used without options, System V historically unset either a function or a
variable, and there was no confusion about which one was intended. A portable POSIX application can use <a href=
"#unset"><i>unset without an option to unset a variable, but not a function; the <b>-f option must be used.

<h4 class="mansect"><a name="tag_19_30_19" id="tag_19_30_19">FUTURE DIRECTIONS
<blockquote>
<p>None.

<h4 class="mansect"><a name="tag_19_30_20" id="tag_19_30_20">SEE ALSO
<blockquote>
<p><a href="#tag_19_15">2.15 Special Built-In Utilities
<p class="tent">XBD <a href="../basedefs/V1_chap12.html#tag_12_02"><i>12.2 Utility Syntax Guidelines

<h4 class="mansect"><a name="tag_19_30_21" id="tag_19_30_21">CHANGE HISTORY
<h4 class="mansect"><a name="tag_19_30_22" id="tag_19_30_22">Issue 6
<blockquote>
<p>IEEE Std 1003.1-2001/Cor 1-2002, item XCU/TC1/D6/5 is applied so that the reference page sections use terms as
described in the Utility Description Defaults ( <a href="../utilities/V3_chap01.html#tag_18_04"><i>1.4 Utility Description
Defaults). No change in behavior is intended.

<h4 class="mansect"><a name="tag_19_30_23" id="tag_19_30_23">Issue 7
<blockquote>
<p>SD5-XCU-ERN-97 is applied, updating the SYNOPSIS.

<h4 class="mansect"><a name="tag_19_30_24" id="tag_19_30_24">Issue 8
<blockquote>
<p>Austin Group Defect 1075 is applied, clarifying that <a href="#unset"><i>unset removes attributes, other than
<i>readonly, from the variables it unsets.

<div class="box"><em>End of informative text.
<hr>

