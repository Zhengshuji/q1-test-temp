# From the lift-completion theorem to general-c rank strata: results, corrections, and a request for direct help

This report collects the work since the previous report, states the current blockage precisely, and asks whether the route is right and whether you can help complete one concrete piece.

## Part I. Setting and notation

Given \(A\in\mathbb C^{n\times n}\), \(C\in\mathbb C^{p\times n}\), \(L_0\in\mathbb C^{r\times n}\), one seeks
\(R\) with \(L=[L_0;R]\) of full row rank and

\[
(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\quad\forall\lambda .
\]

Put \(K_0=\ker[C;CA]\), \(k=\dim K_0\), \(N=N_K\), \(H=LN\), \(H_A=LAN\), \(\omega=\operatorname{rank}H\),
\(c=k-\omega\), and \(P(\lambda)=\lambda H-H_A\). For a candidate \(V=\ker H\in\operatorname{Gr}(c,K_0)\),
let \(W=V\cap A^{-1}V\), \(t=\dim W\), \(U=W+A(W)\).

## Part II. Results and corrections since the last report

### II.1 Lift completion with fixed \(L_0\)

The exact sequence
\[
0\longrightarrow E_C=\frac{\operatorname{row}[C;CA]}{\operatorname{row}C}\longrightarrow
\frac{\mathcal X^*}{\operatorname{row}C}\longrightarrow K_0^*\longrightarrow0
\]
gives the completion problem. With \(d_C=\operatorname{rank}[C;CA]-\operatorname{rank}C\), the rank
completion \(q-\omega\le d_C\) is possible given \(\operatorname{rank}[C;L_0]=p+r\). But adding a row
\(g=aC+bCA\) changes \(H_A\) by \(gAN=b\,CA^2N\), which need not vanish; the freedom that **preserves the
compressed pair** is
\[
E'_C=\{g\in\operatorname{row}[C;CA]:\ gAN=0\}/\operatorname{row}C,\qquad
d'_C=d_C-\operatorname{rank}(g\mapsto gAN).
\]
On the tested instances \(d_C=3\), \(\operatorname{rank}(g\mapsto gAN)=1\), \(d'_C=2\). The pair-preserving
completion criterion is \(q-\omega\le d'_C\); the restricted version (only compatibility on \(V\)) uses
\(d'_C(V)=\dim\ker\mathcal T_V\), \(\mathcal T_V(G)=GAN|_V\), and \(d'_C(V)\ge d'_C\).

### II.2 The \(W_L\) constraint and its consequence

Because the top \(r\) rows of \(H\) and \(H_A\) are fixed (\(L_0N\), \(L_0AN\)), and \(V=\ker H\subseteq\ker H_A\),
\[
\boxed{V\subseteq W_L:=\ker[L_0N_K;\ L_0AN_K].}
\]
Thus \(V\) is not free in \(\operatorname{Gr}(c,K_0)\) but in \(\operatorname{Gr}(c,W_L)\). On the tested
instances \(k=4\), \(\omega=2\), \(c=2\), and \(\operatorname{rank}[L_0N;L_0AN]=2\), so \(\dim W_L=2\):
**\(V\) is forced**. The six-layer classification then classifies the type of this single \(V\), not a
family of admissible planes.

### II.3 The \(c=2\) algorithm: correct spec and a full witness

The correct row-wise relation is
\[
H_{A,i}=l_i^{(0)}AN+g_iAN,
\]
where \(l_i^{(0)}\) is a particular solution of \(l_iN=h_i\), and \(g_i\in\operatorname{row}[C;CA]\) is the
per-row invisible correction (the earlier formula \(H_{A,i}=h_iAN+\Gamma(g_i)\) was dimensionally wrong).
The algorithm: take \(V=W_L\), \(H\)'s rows from \(\operatorname{ann}(V)\), solve the linear admissibility
equations \(H_{A,i}|_V=0\) for \((a,b,g_i)\), then require the \(3\times k\) pencil
\(\lambda h_i-H_{A,i}\) to have constant rank \(\omega\) (gcd of \(2\times2\) minors constant).

On instance 10 (\(n=7,p=2,r=1,k=4,\omega=2,q=3\)) this gives a full witness
\[
L=\begin{bmatrix}0&0&-1&1&0&0&-3\\0&-1&0&0&-1&0&0\\2&-1&2&0&-1&0&0\end{bmatrix},
\]
which passes all seven consistency checks ((5a), (5b), ranks, field). On instances 16 and 21 the linear
admissibility system is also consistent, but no good pencil appears in 600 random samples of the free
parameters; we do not know whether they are infeasible or the good locus is rare.

### II.4 \(c=3\): the suspicious stratum is not \(S_{2,3}\)

For \(t=2\), \(u=3\):
\[
S_{2,3}=\{W\in\operatorname{Gr}(2,D):\ \dim(W+A_0(W))=3\}=\{W:\ A_0(W)\not\subseteq W\},
\]
the complement of the closed condition \(A_0(W)\subseteq W\); it is **open**, hence irreducible. The
reducible strata are the invariant ones (\(t=3\) Jordan types, \(t=2\) with \(A(W)\subseteq W\), \(t=1\) with
\(A(L)\subseteq L\)). Counting the invariant blocks and the open layers gives
\[
N_3\le\binom{s}{3}+\binom{s}{2}+2s^2+4s+3,
\]
where \(s\) is the number of distinct eigenvalues. Each invariant block is a projective linear subspace
(base) times an affine chain fibre, hence empty or irreducible; chain-lifting failures only make blocks empty,
so no piecewise correction is needed.

### II.5 General \(c\)

The invariant part (\(t=c\)) has
\[
N_{\rm inv}(c)\le\sum_{\lambda\vdash c}s^{b(\lambda)}\le p(c)\,s^{c},
\]
where \(b(\lambda)\) is the number of blocks; each block is a product of projective/Grassmannian and affine
chain spaces, so this is a component bound, not merely a label count.

For the non-invariant part, \(S_{t,u}\) is the image of the incidence
\[
\mathcal I_{t,u}=\{(W,U):\ W\subseteq U,\ A(W)\subseteq U,\ U\in\operatorname{Gr}(u,K_0)\},
\]
whose fibre over \(U\) is \(\operatorname{Gr}(t,U\cap A^{-1}U)\). Stratifying by
\(v=\dim(U\cap A^{-1}U)\) gives
\[
\#\{\text{components of }S_{t,u}\}\le\sum_{v=t}^{u}\#\{\text{components of }B_{u,v}\},
\qquad
B_{u,v}=\{U\in\operatorname{Gr}(u,K_0):\ \dim(U\cap A^{-1}U)=v\}.
\]
The point is that \(B_{u,v}\) depends only on \((A,u,v)\), not on \(c\); the problem is reduced to the
component count of the rank strata \(B_{u,v}\) of the fixed map \(U\mapsto U\cap A^{-1}U\).

### II.6 The \(\exists\mathbb R\) audit

The existing encoding of \(\mathrm{DEC}(q)\) in the existential theory of the reals satisfies six of the eight
encoding checks (rational input, polynomial number of variables, polynomial bit size, \(\omega=0\), no
disjunctions, fixed \(L_0\)). Two items need only a sentence each in the write-up: the uniform treatment of
\(\omega\) (covered by the \(s\)-branches) and the full-row-rank condition (handled by the lifting lemma).

## Part III. Questions and requests

**Question 1 (the \(W_L\) constraint).** Is \(V\subseteq W_L\) the correct constraint? If so, the six-layer
classification is a classification of the type of a single \(V\) whenever \(\dim W_L=c\). Is that the intended
reading, or is the classification meant for the free \(V\in\operatorname{Gr}(c,K_0)\) with the \(W_L\)
constraint imposed afterwards?

**Question 2 (the \(c=2\) algorithm).** Is the row-wise pipeline
\[
h_i\ \longrightarrow\ l_i^{(0)}\ \longrightarrow\ H_{A,i}=l_i^{(0)}AN+g_iAN
\]
with the linear admissibility equations and the \(3\times k\) pencil gcd the right algorithm? Can you see a
criterion for instances 16/21 (consistent admissibility, no good pencil in random samples)? A direct
construction or a counterexample would settle whether they are infeasible.

**Question 3 (direct help).** Could you complete the \(c=2\) case directly — for example, give the exact
condition for the good locus of the \(3\times k\) pencil to be nonempty, or a worked example of an infeasible
instance with a proof? This is the one place where a short direct argument from you would close the algorithm.

**Question 4 (general \(c\)).** Is the reduction to \(B_{u,v}\) sound, and is \(\#\{\text{components of
}B_{u,v}\}\) known for the rank strata of \(U\mapsto U\cap A^{-1}U\)? References on determinantal rank
strata / quiver Grassmannians would help. Is the invariant bound \(\sum_{\lambda\vdash c}s^{b(\lambda)}\)
acceptable as a component bound?

**Question 5 (\(c=3\) count).** Is the count \(\binom{s}{3}+\binom{s}{2}+2s^2+4s+3\) correct, or are we
missing strata (for example, degenerate chain-lifting cases that split a block into several components)?

**Question 6 (\(\exists\mathbb R\)).** Are the two phrasing items (uniform \(\omega\), full-row-rank) the only
gaps in the membership proof, or is there a mathematical gap we have not seen?

**Question 7 (route).** Given the above, is the right order (i) close the \(c=2\) algorithm, (ii) work out
\(B_{u,v}\) for \(u=3,4\) and then in general, (iii) something else? We would especially value your view on
whether the \(B_{u,v}\) reduction is the right generalisation, or whether the component-count programme should
be replaced by a different invariant.
