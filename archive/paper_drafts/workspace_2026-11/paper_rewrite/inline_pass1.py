"""Convert safe single-line displays to inline math (first pass).

Rule (deliberately conservative): a display of the form
    <prev line not ending in '.'>
    \\[
    <one short line ending in '.' or ','>
    \\]
is folded into the previous line as $...$ with the punctuation outside.

Displays containing matrices, sums, \\left, \\begin, tags or line breaks are left
alone. Reports what it changed.
"""

import io
import re

PATH = "paper/v2_test.tex"
lines = io.open(PATH, encoding="utf-8").read().split("\n")

SKIP_TOKENS = ("\\begin", "\\left", "\\sum", "\\tag", "\\\\", "\\det", "\\prod",
               "\\int", "\\binom", "matrix", "aligned", "cases")

out = []
i = 0
converted = []
while i < len(lines):
    line = lines[i]
    if (line.strip() == "\\[" and i + 2 < len(lines) and lines[i + 2].strip() == "\\]"
            and lines[i + 1].strip() and not any(t in lines[i + 1] for t in SKIP_TOKENS)):
        content = lines[i + 1].strip()
        if content[-1] in ".," and len(content) < 90 and not content.startswith("\\eqref"):
            punct = content[-1]
            body = content[:-1].rstrip()
            body = body.replace("\\qquad", ",\\ ").replace("\\quad ", "\\ ")
            body = body.replace(", ,", ",").replace(" ,", ",")
            j = len(out) - 1
            while j >= 0 and not out[j].strip():
                j -= 1
            prev = out[j] if j >= 0 else ""
            ok = (prev and not prev.rstrip().endswith(".")
                  and not prev.strip().startswith("\\item")
                  and not prev.strip().startswith("\\paragraph")
                  and not prev.strip().startswith("\\subsection")
                  and not prev.strip().startswith("\\section"))
            if ok:
                out[j] = prev.rstrip() + " $" + body + "$" + punct
                converted.append((i + 1, body[:50]))
                i += 3
                continue
    out.append(line)
    i += 1

io.open(PATH, "w", encoding="utf-8", newline="\n").write("\n".join(out))
print("converted", len(converted), "displays")
for ln, prev in converted:
    print("  line", ln, ":", prev)
