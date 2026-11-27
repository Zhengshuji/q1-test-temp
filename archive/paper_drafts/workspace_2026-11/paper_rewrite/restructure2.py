"""Structural edits: equation numbering, drop the two prose tables, move
'What is not claimed' to the conclusions, rename Discussion -> Conclusions."""

import io
import re

PATH = "paper/v2_test.tex"
text = io.open(PATH, encoding="utf-8").read()

# 1. conditions get ordinary numbers; the historical names stay in the text
text = text.replace("\\tag{5a}\\label{eq:5a}", "\\label{eq:5a}")
text = text.replace("\\tag{5b}\\label{eq:5b}", "\\label{eq:5b}")
text = text.replace(
    "These are the Fernando--Trinh--Jennings conditions for a $q$-order functional observer\n"
    "\\cite{fer10}.",
    "These are the Fernando--Trinh--Jennings conditions for a $q$-order functional\n"
    "observer \\cite{fer10} (conditions (5a) and (5b) in the notation of that paper).")
text = text.replace(
    "These are the Fernando--Trinh--Jennings conditions for a $q$-order functional observer \\cite{fer10}.",
    "These are the Fernando--Trinh--Jennings conditions for a $q$-order functional\n"
    "observer \\cite{fer10} (conditions (5a) and (5b) in the notation of that paper).")

# 2. drop the two prose tables
def drop_table(m):
    return "" if ("what each controls" in m.group(0) or "Classical tools" in m.group(0)) else m.group(0)

text, k = re.subn(r"\\begin\{table\*\}.*?\\end\{table\*\}", drop_table, text, flags=re.S)
print("tables scanned:", k)

# 3. cut "What is not claimed" and keep its body
m = re.search(r"\\subsection\{What is not claimed\}\\label\{sec:notclaim\}\n(.*?)\n(?=\\section\{)",
              text, flags=re.S)
body = m.group(1).strip()
text = text[:m.start()] + text[m.end():]
print("not-claimed body chars:", len(body))

# 4. Discussion -> Conclusions, with the not-claimed paragraph appended
text = text.replace("\\section{Discussion}\\label{sec:discussion}",
                    "\\section{Conclusions}\\label{sec:conclusions}")
text = text.replace("\\subsection{Limitations}\\label{sec:limits}",
                    "\\subsection{Limitations and what is not claimed}\\label{sec:limits}")
# insert the body just after the Limitations heading
text = text.replace(
    "\\subsection{Limitations and what is not claimed}\\label{sec:limits}\n",
    "\\subsection{Limitations and what is not claimed}\\label{sec:limits}\n" + body + "\n")

io.open(PATH, "w", encoding="utf-8", newline="\n").write(text)
print("done")
