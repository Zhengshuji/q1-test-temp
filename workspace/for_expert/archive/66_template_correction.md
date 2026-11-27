# Correction of the six-dimensional template, and the strengthened rigidity

This note records that the six-dimensional feasible template in the previous answer does not match its own data, and asks for the intended matrices. The corrections to the local rigidity are accepted.

## Part I. Accepted corrections

- The local leakage-rigidity theorem is retracted: \(A(V)\subseteq K_0\) and \(\omega>0\) imply \(A(V)\subseteq V\), but not pencil failure.
- The global rigidity is strengthened to: if \(A(K_0)\subseteq K_0\) and \(\omega>0\), no feasible observer exists (the case \(c=0\) included; only \(\omega=0\) is excluded).
- For \(A(V)\subseteq V\): \(H_A=DH\), \(\Delta:W=\operatorname{im}H\to\mathbb C^q\), the pencil is good iff \(\ker(\Delta-\lambda I)\cap W=\{0\}\) for all \(\lambda\), and \(q>\omega\) is necessary.

## Part II. The template and the discrepancy

The template in the previous answer is
\[
n=6,\quad C=e_6^*,\quad K_0=\operatorname{span}\{e_1,\dots,e_4\},
\]
\[
Ae_1=e_5,\quad Ae_2=e_1,\quad Ae_3=Ae_4=0,\quad Ae_5=e_6,\quad Ae_6=0,
\]
\[
L_0=e_1^*,\qquad L=\begin{bmatrix}e_1^*\\e_2^*\\e_1^*+e_2^*+e_5^*\end{bmatrix},
\]
with the displayed pencil
\[
P(\lambda)=\begin{bmatrix}\lambda&-1&0&0\\0&\lambda&0&0\\ \lambda-1&\lambda-1&0&0\end{bmatrix}.
\]

With \(N=[e_1,e_2,e_3,e_4]\), direct exact computation gives
\[
H=LN=\begin{bmatrix}1&0&0&0\\0&1&0&0\\1&1&0&0\end{bmatrix},
\]
which agrees with the answer, but
\[
H_A=LAN=\begin{bmatrix}0&0&0&0\\1&0&0&0\\1&0&0&0\end{bmatrix},
\]
whereas the answer states
\[
H_A=\begin{bmatrix}0&1&0&0\\0&0&0&0\\1&1&0&0\end{bmatrix}.
\]
Consequently the actual pencil is
\[
\lambda H-H_A=\begin{bmatrix}\lambda&0&0&0\\-1&\lambda&0&0\\ \lambda-1&\lambda&0&0\end{bmatrix},
\]
whose first two columns have minors \(\lambda^2,\lambda^2,-\lambda^2\); the gcd is \(\lambda^2\), so the rank drops at \(\lambda=0\). The exact check returns \((5a)\) true but \((5b)\) false.

Two natural corrections were tried:
- chain \(e_1\mapsto e_2\mapsto e_5\mapsto e_6\) (\(Ae_1=e_2\), \(Ae_2=e_5\), \(Ae_5=e_6\)): \(H_A\) rows \(e_2,0,e_2\), gcd \(\lambda^2\);
- the stated chain \(e_2\mapsto e_1\mapsto e_5\): \(H_A\) rows \(0,e_1,e_1\), gcd \(\lambda^2\).

Both fail. The displayed \(P(\lambda)\) is good (its minors \(\lambda^2,\lambda^2-1,-\lambda(\lambda-1)\) have gcd one), but we could not find \(A,L\) satisfying the stated actions, \(K_0=\ker[C;CA]\), \((5a)\), and producing that \(P\).

## Part III. Questions

**Question 1.** Is there a typo in the actions or in the rows of \(L\)? The \(H_A\) that matches the displayed \(P\) is \((e_2,0,e_1+e_2)\), which would require \(e_1A=e_2\), \(e_2A=0\), \(e_5A=e_1\) (on \(K_0\)); but then \(A(K_0)\subseteq K_0\) (no leakage), since \(Ae_5=e_1\in K_0\).

**Question 2.** Could you give the explicit \(A,L\) (or the corrected actions) that yield the displayed \(P\) together with \(K_0=\operatorname{span}\{e_1,\dots,e_4\}\) and \((5a)\)? We would like to use the template as the base for the arithmetic gadget.

**Question 3.** Is the discrepancy perhaps due to a different convention for \(H_A\) (e.g., \(AN\) versus \(NA\), or \(L\) acting from the left)? Our computation uses \(H=LN\) and \(H_A=LAN\) with row vectors.
