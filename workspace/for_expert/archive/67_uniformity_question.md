# Acknowledgement of the template verification, and the uniformity question

You are right: the six-dimensional template is correct, and my computation of \(H_A=LAN\) was wrong because I confused the column action \(Ae_i\) with the row action \(e_i^*A\). With the matrix
\[
A=\begin{bmatrix}
0&1&0&0&0&0\\
0&0&0&0&0&0\\
0&0&0&0&0&0\\
0&0&0&0&0&0\\
1&0&0&0&0&0\\
0&0&0&0&1&0
\end{bmatrix}
\]
and the stated \(C=e_6^*\), \(L_0=e_1^*\), \(L=[e_1^*;e_2^*;e_1^*+e_2^*+e_5^*]\), \(N=[e_1,e_2,e_3,e_4]\), the exact checks give
\[
H=\begin{bmatrix}1&0&0&0\\0&1&0&0\\1&1&0&0\end{bmatrix},\qquad
H_A=\begin{bmatrix}0&1&0&0\\0&0&0&0\\1&1&0&0\end{bmatrix},
\]
and
\[
P(\lambda)=\begin{bmatrix}\lambda&-1&0&0\\0&\lambda&0&0\\ \lambda-1&\lambda-1&0&0\end{bmatrix},
\]
with minors \(\lambda^2,\lambda^2-1,-\lambda(\lambda-1)\), \(\gcd=1\). All seven checks pass: \((5a)\) and \((5b)\) hold, \(\operatorname{rank}[C;L]=4=p+q\), \(A(K_0)\not\subseteq K_0\), \(A(V)=0\subseteq V\), \(\omega=2\), \(q=3>\omega\). The record has been corrected.

## The next question: uniformity

This is a verified spectral base case at one fixed configuration. The arithmetic-gadget programme needs a family of configurations, parametrised by the arithmetic variables, with the following property:

> for every parameter value satisfying the encoded arithmetic relation, the pencil has constant rank \(\omega\); and for every value violating it, some other condition (or the pencil itself) fails.

The template gives no uniformity: the gcd certificate is for one \(A\).

**Question 1.** Is there a general method to make the spectral condition **uniform** under a variable-dependent perturbation of \(A\) and \(L\)? For example, can the shift chain \(e_1\mapsto e_2\mapsto e_5\mapsto e_6\) be kept fixed while the arithmetic variables enter only through rows that are provably independent of the pencil minors (e.g. through coordinates in the kernel of every minor)?

**Question 2.** If the arithmetic relation is encoded in the graph chart \(V=\operatorname{graph}(X)\), the invariance equation \(F_A(X)=0\) changes \(L\) and \(H_A\) with \(X\). Is there a known way to keep \(P(\lambda)\)'s minors coprime for all \(X\) (e.g. by a block-triangular arrangement where the spectral block is independent of the arithmetic block)?

**Question 3.** Would it be more promising to use this template as a **padding** (a fixed spectral-good block added to any arithmetic construction), rather than trying to make the arithmetic block itself spectrally good? If so, what is the minimal padding that survives the addition of an arbitrary arithmetic block?

**Question 4.** Given the negative expressiveness results for affine constraints on \(H\), and the positive spectral template here, do you see a concrete route to an arithmetic gadget, or should the hardness workstream first establish a general "padding lemma" (fixed good spectral block + arbitrary arithmetic block \(\Rightarrow\) good pencil)?
