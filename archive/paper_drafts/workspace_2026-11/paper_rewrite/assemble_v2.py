"""Assemble the restructured paper (v2) from the current .tex + the new section.

Reads  paper/q1_parametric_algorithms.tex   (the source of record, untouched)
       paper/lit_review_draft.tex           (new Section II)
Writes paper/v2_test.tex                    (candidate; not the source)

Restructuring:
  I   Introduction                    = old 1, minus subsection 1.4
  II  Literature Review               = lit_review_draft
  III The problem and the compression = old 2 + old 3
  IV  The effective free-row dimension= old 4
  V   Rank factorization, consistency, and the certificate = old 5 + old 6
  VI  The fixed-order algorithm       = old 7
  VII The fixed-parameter algorithm   = old 8
  VIII Membership in exists-R         = old 9
  IX  Discussion                      = old 10
  Appendix A  (old Appendix B)
References moved to the end; old Appendix A and C dropped.
"""

import io
import os
import re

SRC = os.path.join("paper", "q1_parametric_algorithms.tex")
LIT = os.path.join("paper", "lit_review_draft.tex")
OUT = os.path.join("paper", "v2_test.tex")

text = io.open(SRC, encoding="utf-8").read()
lines = text.split("\n")

# ---- split: preamble / front matter / body / bib / end ----------------
i_begin = lines.index("\\begin{document}")
i_end = lines.index("\\end{document}")
preamble = lines[:i_begin]
inside = lines[i_begin + 1:i_end]

i_bib = next(i for i, l in enumerate(inside) if l.startswith("\\begin{thebibliography}"))
front = inside[:i_bib]
bib = inside[i_bib:]
body = front

# body starts after \maketitle + abstract + keywords
i_first_section = next(i for i, l in enumerate(body) if l.startswith("\\section{"))
head = body[:i_first_section]
body = body[i_first_section:]

# ---- split body into top-level sections -------------------------------
chunks = []
cur = None
for line in body:
    if line.startswith("\\section{"):
        if cur is not None:
            chunks.append(cur)
        cur = [line]
    else:
        if cur is None:
            cur = [line]
        else:
            cur.append(line)
if cur is not None:
    chunks.append(cur)


def title(chunk):
    return re.match(r"\\section\{(.+?)\}", chunk[0]).group(1)


by_title = {}
for c in chunks:
    by_title[title(c)] = c

print("sections found:", list(by_title))

# ---- I. Introduction: drop subsection 1.4 ----------------------------
intro = by_title["Introduction"]
i_rel = next(i for i, l in enumerate(intro) if l.startswith("\\subsection{Relation to the characterization"))
intro_new = intro[:i_rel]
# strip trailing blank lines
while intro_new and not intro_new[-1].strip():
    intro_new.pop()
intro_new.append("")

# ---- II. Literature Review -------------------------------------------
lit = io.open(LIT, encoding="utf-8").read().split("\n")
# new bibliography entries live in the commented block at the end of the draft
i_mark = next(i for i, l in enumerate(lit) if "NEW BIB ENTRIES" in l)
extra_bib = []
for l in lit[i_mark:]:
    if l.startswith("% \\bibitem"):
        extra_bib.append(l[2:])
    elif l.startswith("%   ") and extra_bib:
        extra_bib.append(l[2:])
# keep from \section to the end of the last subsection (before the commented block)
lit_body = [l for l in lit[:i_mark] if not l.startswith("%")]
while lit_body and not lit_body[-1].strip():
    lit_body.pop()

# ---- old Appendix A ("Proof details"): split by A.n and redistribute --
app_old = by_title["Proof details"]
parts = {}
cur = None
for line in app_old[1:]:
    m = re.match(r"\\subsection\*\{A\.(\d)\s*(.*)\}", line)
    if m:
        cur = m.group(1)
        parts[cur] = []
        continue
    if cur is not None:
        parts[cur].append(re.sub(r"^\\subsubsection\*\{", r"\\paragraph{", line))

# ---- III. old 2 + old 3 (+ A.1) --------------------------------------
s2 = by_title["Setting and notation"]
s3 = by_title["Lemma A: compression and pencil criterion"]
s3_body = s3[1:]                      # drop old \section line
s3_body = [l.replace("\\subsection*{", "\\subsection{") for l in s3_body]
sec3 = (["\\section{The problem and the compression}\\label{sec:formulation}"] + s2[1:]
        + ["", "\\subsection{The compression and the pencil criterion}\\label{sec:compression}"]
        + s3_body + [""] + parts.get("1", []))

# ---- IV. old 4 (+ A.2) -----------------------------------------------
sec4 = ["\\section{The effective free-row dimension}\\label{sec:dimension}"] + by_title["Lemma B: free-row parametrization"][1:] + [""] + parts.get("2", [])

# ---- V. old 5 + old 6 (+ A.3, A.4) -----------------------------------
s5 = by_title["Lemma C: rank factorization and consistency"]
s6 = by_title["Lemma D: spectral certificate"]
s5_body = [re.sub(r"^\\subsection\{", r"\\paragraph{", l) for l in s5[1:]]
s6_body = [re.sub(r"^\\subsection\{", r"\\paragraph{", l) for l in s6[1:]]
sec5 = (["\\section{Rank factorization, consistency, and the finite certificate}"
         "\\label{sec:certificate}",
         "\\subsection{Rank factorization and consistency}\\label{sec:consistency}"]
        + s5_body + [""] + parts.get("3", [])
        + ["", "\\subsection{The spectral certificate}\\label{sec:spectrum}"]
        + s6_body + [""] + parts.get("4", []))

# ---- VI, VII, VIII, IX ----------------------------------------------
sec6 = ["\\section{The fixed-order algorithm}\\label{sec:fixedq}"] + by_title["Theorem 1: fixed observer order"][1:]
sec7 = ["\\section{The fixed-parameter algorithm}\\label{sec:fpt}"] + by_title["Theorem 2: fixed effective dimension"][1:]
sec8 = ["\\section{Membership in the existential theory of the reals}\\label{sec:existsr}"] + by_title["Theorem 3 and the combined bound"][1:]
sec9 = ["\\section{Discussion}\\label{sec:discussion}"] + by_title["Discussion and open problems"][1:]

# A.5 (complexity estimates) goes into the FPT section
sec7 = sec7 + [""] + parts.get("5", [])

# ---- Appendix A (old Appendix B) ------------------------------------
app_b = by_title["Real-algebraic certificate"]
app_a = ["\\appendices", "\\section{The existential-real encoding}\\label{app:encoding}"] + app_b[1:]

# ---- assemble: references last --------------------------------------
new_body = (head + intro_new + lit_body + [""] + sec3 + [""] + sec4 + [""] + sec5
            + [""] + sec6 + [""] + sec7 + [""] + sec8 + [""] + sec9 + [""]
            + app_a + [""] + bib)

# append the new bibliography entries just before \end{thebibliography}
i_endbib = next(i for i, l in enumerate(new_body) if l.startswith("\\end{thebibliography}"))
new_body = new_body[:i_endbib] + extra_bib + new_body[i_endbib:]

out_lines = preamble + ["\\begin{document}"] + new_body + ["\\end{document}"]
text = "\n".join(out_lines)

# ---- cross-reference fixups after the appendix merge -----------------
text = text.replace("Appendix A.1", "Section~\\ref{sec:compression}")
text = text.replace("Appendix A.5", "Section~\\ref{sec:fpt}")
text = text.replace("Appendix B", "Appendix~\\ref{app:encoding}")
text = text.replace("Appendix C", "the artifact repository")

io.open(OUT, "w", encoding="utf-8", newline="\n").write(text)
print("wrote", OUT, "lines:", text.count("\n") + 1)
