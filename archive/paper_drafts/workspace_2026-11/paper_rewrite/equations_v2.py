"""Give the named equations real tags and labels, and turn hand-typed
references into \\eqref (applied to the v2 candidate)."""

import io
import re

PATH = "paper/v2_test.tex"
text = io.open(PATH, encoding="utf-8").read()
n0 = text.count("\\tag{")

# 1. (5a)/(5b): literal text inside \[...\]  ->  equation with \tag and \label
def cond(m):
    tag, body = m.group(1), m.group(2)
    body = body.replace("\\quad ", "", 1)
    return ("\\begin{equation}\n\\tag{%s}\\label{eq:%s}\n%s\n\\end{equation}"
            % (tag, tag, body.strip()))

text, k1 = re.subn(
    r"\\\[\n\((5a|5b)\)\\quad (.*?)\n\\\]",
    cond, text, flags=re.S)
print("condition displays converted:", k1)

# 2. equation* with \tag{R0} / (B.1) / (B.2): make them numbered equations with labels
def tagged(m):
    body = m.group(1)
    tag = re.search(r"\\tag\{([^}]*)\}", body).group(1)
    key = {"R0": "eq:R0", "B.1": "eq:B1", "B.2": "eq:B2"}[tag]
    body = body.replace("\\tag{%s}" % tag, "\\tag{%s}\\label{%s}" % (tag, key))
    return "\\begin{equation}\n" + body.strip() + "\n\\end{equation}"

text, k2 = re.subn(
    r"\\begin\{equation\*\}\n(.*?)\n\\end\{equation\*\}",
    tagged, text, flags=re.S)
print("tagged equations converted:", k2)

# 3. hand-typed references -> \eqref
text = text.replace("$(5a)(5b)$", "\\eqref{eq:5a} and \\eqref{eq:5b}")
text = text.replace("\\((5b)_\\lambda\\)", "\\eqref{eq:5b}$_\\lambda$")
for old, new in [("(5a)", "\\eqref{eq:5a}"), ("(5b)", "\\eqref{eq:5b}"),
                 ("(B.1)", "\\eqref{eq:B1}"), ("(B.2)", "\\eqref{eq:B2}"),
                 ("(R0)", "\\eqref{eq:R0}")]:
    text = text.replace(old, new)

io.open(PATH, "w", encoding="utf-8", newline="\n").write(text)
print("tags before:", n0, "| eqref occurrences:", text.count("\\eqref{"))
