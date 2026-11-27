"""Splice the new front matter (I Introduction, II Preliminaries) into v2 and
redistribute the old section III: the compression definitions and Lemma A stay in
the new Section III; the free-pair space joins Section IV."""

import io
import re

PATH = "paper/v2_test.tex"
FRONT = "paper/front_matter_v3.tex"

text = io.open(PATH, encoding="utf-8").read()
front = io.open(FRONT, encoding="utf-8").read().rstrip() + "\n"

# locate sections
def span(title):
    m = re.search(r"\\section\{%s\}.*?(?=\\section\{|\\begin\{thebibliography\})" % re.escape(title),
                  text, flags=re.S)
    return m

# old section III content
m3 = span("The problem and the compression")
old3 = m3.group(0)

# split old III into subsections
def subsections(block):
    parts = {}
    cur = None
    for line in block.split("\n"):
        mm = re.match(r"\\subsection\{(.+?)\}\\label\{([^}]*)\}", line)
        if mm:
            cur = mm.group(2)
            parts[cur] = [line]
        elif cur is not None:
            parts[cur].append(line)
    return {k: "\n".join(v).rstrip() for k, v in parts.items()}

sub3 = subsections(old3)
print("old III subsections:", list(sub3))

# old section IV content (without the header line)
m4 = span("The effective free-row dimension")
old4 = m4.group(0)
old4_body = old4.split("\n", 1)[1]

new_iii = ("\\section{The compressed pencil}\\label{sec:compressed}\n\n"
           + sub3["sec:compress"].replace("\\subsection{Observer compression}",
                                         "\\subsection{The common kernel and the compression}")
           + "\n\n" + sub3["sec:compression"] + "\n\n")

new_iv = ("\\section{The effective free-row dimension}\\label{sec:dimension}\n\n"
          + sub3["sec:free"].replace("\\subsection{The free-row space}",
                                     "\\subsection{The space of attainable row pairs}")
          + "\n" + old4_body + "\n\n")

# rebuild
tail = text[m4.end():]
text = text[:m3.start()] + new_iii + new_iv + tail.lstrip("\n")
# replace the old front matter (Introduction + Literature Review) by the new fragment
i_intro = text.index("\\section{Introduction}")
i_new3 = text.index("\\section{The compressed pencil}")
text = text[:i_intro] + front + "\n" + text[i_new3:]

# fix stale references
text = text.replace("\\ref{sec:problem}", "\\ref{sec:compression}")
text = text.replace("\\ref{sec:io}", "\\ref{sec:notation}")

io.open(PATH, "w", encoding="utf-8", newline="\n").write(text)
print("spliced; length", len(text))
