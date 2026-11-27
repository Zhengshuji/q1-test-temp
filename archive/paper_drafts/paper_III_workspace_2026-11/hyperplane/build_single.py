"""把分节 tex 合并成单一 hyperplane_layer.tex（覆盖旧的重定向式主文件）。"""
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "src")

PREAMBLE = r"""\documentclass[journal]{IEEEtran}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{amsthm}
\usepackage{booktabs,array}
\usepackage{enumitem}
\usepackage{microtype}
\usepackage[hidelinks]{hyperref}
\newtheoremstyle{plainn}{}{}{\itshape}{}{\bfseries}{.}{.5em}%
  {\thmname{#1}\thmnumber{ #2}\thmnote{ (#3)}}
\theoremstyle{plainn}
\newtheorem{thm}{Theorem}
\newtheorem{lem}[thm]{Lemma}
\newtheorem{prop}[thm]{Proposition}
\newtheorem{cor}[thm]{Corollary}
\newtheorem{defn}[thm]{Definition}
\newtheorem{exmp}[thm]{Example}
\newtheorem{algo}[thm]{Algorithm}
\theoremstyle{remark}
\newtheorem{remark}{Remark}
\renewcommand{\qedsymbol}{QED}
\newcommand{\row}{\operatorname{row}}
\newcommand{\rank}{\operatorname{rank}}
\newcommand{\Ann}{\operatorname{Ann}}
\newcommand{\Gr}{\operatorname{Gr}}
\newcommand{\Prob}{\operatorname{Prob}}
\newcommand{\poly}{\operatorname{poly}}

\begin{document}

\title{Functional-Observer Feasibility in the Hyperplane Layer}
\author{}
\maketitle
"""

ABSTRACT = r"""
\begin{abstract}
The companion papers decide whether a functional observer of a prescribed order exists and compute the
minimum order; neither describes the admissible designs. This paper does, for the smallest layer in
which the kernel of the compressed pencil is one-dimensional. The admissible kernel directions are
exactly the real eigenvectors of the orthogonal compression of the state matrix to the unobservable
subspace, further restricted by the prescribed rows. The design family is therefore a finite union of
relative Grassmann bundles over locally closed algebraic strata of projective eigenspaces, with
explicit fibre dimensions and nonemptiness conditions. Feasibility in the layer is decided exactly by
algebraic computation on these bundles, and a full-rank leading-coefficient lemma lets a single
computation per chart settle every point of it rather than a generic one. For fixed output dimension
and geometrically simple real spectrum the decision is polynomial in the input bit size. A certified
repeated-eigenspace example shows that feasibility need not be constant on a projective eigenspace, so
one eigenvector per eigenvalue is not a valid reduction; no hardness statement is claimed. A duality
identifies the projective direction with the annihilator of the common projection of the compressed
formulation.
\end{abstract}

\begin{IEEEkeywords}
Functional observers, feasibility, compressed pencil, Grassmannian, exact algorithms,
parameterized complexity.
\end{IEEEkeywords}
"""

BIB = r"""
\begin{thebibliography}{99}
\bibitem{fer26a} J. A. Fernando. A minimum-order functional observer beyond the Darouach and Luenberger constructions. arXiv:2609.33615, 2026 (preprint).
\bibitem{fer26b} J. A. Fernando. Complete characterization of minimum-order functional observers from Darouach to Luenberger. arXiv:2609.37992, 2026 (preprint).
\bibitem{fer10} J. A. Fernando, H. Trinh, L. Jennings. Functional observability and the design of minimum order linear functional observers. \emph{IEEE Trans. Automat. Control} 55(5):1268--1273, 2010.
\bibitem{dar25} M. Darouach, J. A. Fernando. On functional observability and functional observer design. \emph{Automatica}, vol. 173, Art. no. 112115, 2025.
\bibitem{hj13} R. A. Horn, C. R. Johnson. \emph{Matrix Analysis}. 2nd ed. Cambridge University Press, 2013.
\bibitem{bpr06} S. Basu, R. Pollack, M.-F. Roy. \emph{Algorithms in Real Algebraic Geometry}, 2nd ed. Berlin, Germany: Springer, 2006, Algorithms and Computation in Mathematics, vol. 10.
\bibitem{lan02} S. Lang. \emph{Algebra}. Revised 3rd ed. Graduate Texts in Mathematics 211, Springer, 2002.
\bibitem{vzgg03} J. von zur Gathen, J. Gerhard. \emph{Modern Computer Algebra}. 2nd ed. Cambridge University Press, 2003.
\bibitem{companion1} Deciding functional observer feasibility: compression, certificates, and parameterized algorithms. Companion manuscript, 2026.
\bibitem{companion2} Minimum order and minimum-order construction for functional observers. Companion manuscript, 2026.
\end{thebibliography}

\end{document}
"""

ORDER = [
    "sec1s.tex",
    "sec2.tex",
    "sec3w.tex",
    "sec4w.tex",
    "sec5w.tex",
    "sec6t.tex",
    "appAs.tex",
    "appBCw.tex",
]


def main() -> None:
    parts = [PREAMBLE, ABSTRACT]
    for name in ORDER:
        path = os.path.join(SRC, name)
        with io.open(path, encoding="utf-8") as fh:
            body = fh.read()
        if "appA" in name or "appBC" in name:
            if "\\appendices" not in "".join(parts):
                parts.append("\n\\appendices\n")
        parts.append(body)
        parts.append("\n")
    parts.append(BIB)
    text = "".join(parts)
    out = os.path.join(HERE, "hyperplane_layer.tex")
    with io.open(out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print("wrote", out, len(text.splitlines()), "lines")


if __name__ == "__main__":
    main()
