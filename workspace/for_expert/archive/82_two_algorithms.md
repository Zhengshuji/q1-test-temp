# Two algorithmic routes for q1: fixed q polynomial time, fixed κ_obs FPT

This note reports two algorithmic proof skeletons, the exact checks behind them, and asks for an audit of their correctness and complexity.

## Part I. Setting

For fixed \(A,C,L_0\), find \(L=[L_0;R]\) with
\[
(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\ \forall\lambda.
\]
Let \(K_0=\ker[C;CA]\), \(N\) a basis, \(k=\dim K_0\), \(H=LN\), \(H_A=LAN\), \(\omega=\operatorname{rank}H\). Then
\[
(5a)\iff\operatorname{row}H_A\subseteq\operatorname{row}H,
\qquad
(5b)\iff\operatorname{rank}(\lambda H-H_A)=\omega\ \forall\lambda.
\]
The decision problem is \(q1\).

Labels: **P** paper, **E** exact finite computation, **S** sketch.

## Part II. Fixed \(q\): a polynomial algorithm

### II.1 Rank factorization

For \(\omega>0\), choose pivot columns \(J\subseteq[k]\), \(|J|=\omega\), such that
\[
X=H_{:,J}\in\mathbb R^{q\times\omega}
\]
has full column rank. Then there is \(B\in\mathbb R^{\omega\times k}\) with
\[
H=XB,\qquad B_{:,J}=I_\omega.
\]
Conversely, if \(X\) has full column rank and \(B_{:,J}=I_\omega\), then \(\operatorname{rank}(XB)=\omega\).

### II.2 \((5a)\) and \(F\)

From \((5a)\), choose \(F\in\mathbb R^{q\times q}\) with
\[
H_A=FH=FXB.
\]
The matrices \(F,X\) have \(q^2+q\omega\le2q^2\) entries.

### II.3 Linear system in \(B\)

Let
\[
\mathcal T=\operatorname{row}[N\ AN]\subseteq\mathbb R^{2k},
\]
and choose \(D\) with \(\ker D=\mathcal T\). Every free row pair satisfies
\[
D\begin{bmatrix}(X_iB)^{\mathsf T}\\ ((FX)_iB)^{\mathsf T}\end{bmatrix}=0,
\]
and every fixed row satisfies
\[
X_iB=h_i^0,\qquad (FX)_iB=g_i^0.
\]
After substituting \(B_{:,J}=I_\omega\), all these equations are linear in the remaining entries \(b\) of \(B\):
\[
M(F,X)b=c(F,X).
\]
The entries of \(M,c\) are polynomials of degree at most two in \(F,X\).

### II.4 Rank-consistency elimination

The system \(Mb=c\) is consistent iff
\[
\operatorname{rank}(MM^{\mathsf T})=\operatorname{rank}(MM^{\mathsf T}+cc^{\mathsf T}).
\]
Writing
\[
\Gamma=MM^{\mathsf T},\qquad \Gamma'=MM^{\mathsf T}+cc^{\mathsf T},
\]
this is the finite disjunction
\[
\bigvee_{t=0}^{d_1}\left[e_t(\Gamma)>0\wedge e_{t+1}(\Gamma)=0\wedge e_{t+1}(\Gamma')=0\right],
\]
where \(d_1=\min(\text{rows},\text{cols})\) of \(M\).

This eliminates \(b\) without quantifying it.

### II.5 Spectral condition

Since \(B\) has full row rank,
\[
P(\lambda)=(\lambda I-F)XB
\quad\Longrightarrow\quad
\operatorname{rank}P(\lambda)=\operatorname{rank}((\lambda I-F)X).
\]
Thus
\[
(5b)\iff\operatorname{rank}((\lambda I-F)X)=\omega\ \forall\lambda.
\]
Encode this by the \(2\omega\)-variable Gram–Bezout certificate for the maximal minors of \(Q(\lambda)=(\lambda I-F)X\), and impose
\[
e_\omega(X^{\mathsf T}X)>0.
\]

### II.6 Complexity

For each \(\omega\) and each pivot set \(J\), the quantified variables are
\[
q^2+q\omega+2\omega=O(q^2).
\]
The number of pivot sets is at most \(\binom{k}{\omega}\le k^q\), polynomial for fixed \(q\).
A fixed-variable real-feasibility algorithm gives a coarse bound
\[
\boxed{\mathcal L^{O(q^2)}}
\]
for fixed \(q\), where \(\mathcal L\) is the rational input bit length. This is XP in \(q\), not FPT.

### II.7 Exact checks

- `c311`: rank-consistency identity on 200 random systems.
- `c312`: on a \(3\times3\) rank-two instance, \(H=XB\), \(B_J=I\), \(H_A=FH\), and \(\operatorname{rank}P(\lambda)=\operatorname{rank}((\lambda I-F)X)\).

## Part III. Fixed \(\kappa_{\rm obs}\): FPT

### III.1 Compressed variables

Let
\[
d_0=\operatorname{rank}[N\ AN],\qquad \kappa_{\rm obs}=r d_0.
\]
Every free row pair lies in \(\mathcal T=\operatorname{row}[N\ AN]\), of dimension \(d_0\). Each row contributes \(d_0\) coordinates; all free rows contribute
\[
\kappa_{\rm obs}=r d_0
\]
real variables. Also
\[
k\le d_0\le\kappa_{\rm obs}.
\]
The number of fixed rows, hence \(q\), need not be bounded.

### III.2 \((5a)\) by Gram matrices

\[
G_H=H^{\mathsf T}H,\qquad G_S=H^{\mathsf T}H+H_A^{\mathsf T}H_A.
\]
Then
\[
(5a)\iff e_\omega(G_H)>0,\qquad e_{\omega+1}(G_S)=0
\]
on the rank-\(\omega\) stratum.

### III.3 \((5b)\) by a \(2\omega\)-dimensional certificate

Let \(f_1,\ldots,f_s\) be the \(\omega\times\omega\) minors of \(P(\lambda)=\lambda H-H_A\).
If they have no common complex root, there are real \(g_i\) with \(\deg g_i<\omega\) and
\[
\sum_i g_i f_i=1.
\]
Form \(B\) with rows indexed by \((i,j)\), \(0\le j<\omega\), and columns \(0\le t<2\omega\):
\[
B_{(i,j),t}=c_{i,t-j},
\]
where \(c_{i,a}\) is the coefficient of \(\lambda^a\) in \(f_i\). Then
\[
(5b)\iff e_0\in\operatorname{row}B
\iff\exists x\in\mathbb R^{2\omega}:\ B^{\mathsf T}Bx=e_0.
\]

### III.4 Cauchy–Binet compression

\[
K(\lambda,\mu)=\sum_{|J|=\omega}\det\left(P(\lambda)_{:,J}^{\mathsf T}P(\mu)_{:,J}\right)
=\sum_i f_i(\lambda)f_i(\mu).
\]
Let \(S_{a,b}\) be the coefficient of \(\lambda^a\mu^b\) in \(K\). Then
\[
(B^{\mathsf T}B)_{t,t'}=\sum_{j=0}^{\omega-1}S_{t-j,t'-j}.
\]
Only \(\binom{k}{\omega}\le2^{\kappa_{\rm obs}}\) terms occur; each is an \(\omega\times\omega\) determinant, so \(B^{\mathsf T}B\) is computable in
\[
f(\kappa_{\rm obs})\operatorname{poly}(q,\mathcal L)
\]
time.

### III.5 FPT conclusion

The quantified variables are
\[
\kappa_{\rm obs}+2\omega+1=f(\kappa_{\rm obs}),
\]
and all coefficients are computable in \(f(\kappa_{\rm obs})\operatorname{poly}(q,\mathcal L)\) time. Hence
\[
\boxed{\text{fixed }\kappa_{\rm obs}\Rightarrow q1\in\mathrm{FPT}.}
\]

### III.6 Exact checks

- `c313`: indexing formula \((B^{\mathsf T}B)_{t,t'}=\sum_j S_{t-j,t'-j}\) and \(e_0\in\operatorname{row}B\) on a \(3\times3\) pencil.
- `c278`: \(B^{\mathsf T}Bx=e_0\), Cauchy–Binet, \(e_2(G_H)=55>0\), \(e_3(G_S)=0\).

## Part IV. Soundness and hardness status

Only two sound q1 gadgets are currently known: the nonzero gadget and the input-controlled nonzero gadget. The multiplication construction is a full-observer realization but not sound: \(R=0\) gives a feasible instance with no condition on \(x,y,z\). Fixed-subspace port rigidity is only conditional; disjoint fixed subspaces can have moving intersections. No sound multiplication gadget and no hardness reduction are known.

## Part V. Questions

1. **Fixed \(q\) proof.** Is the factorization \(H=XB\), the normalization \(B_{:,J}=I_\omega\), the linear system \(M(F,X)b=c(F,X)\), and the rank-consistency formula a valid polynomial-time reduction for fixed \(q\)? Are there hidden cases (pivot enumeration, non-unique \(F\), degenerate \(B\)) that break it?

2. **Fixed \(q\) complexity.** Is \(\mathcal L^{O(q^2)}\) the right form of the bound, or does the number of pivot sets \(\binom{k}{\omega}\) force a worse exponent? Is the use of a fixed-variable real-feasibility algorithm legitimate here, given that the polynomial degrees grow with \(k\)?

3. **FPT proof.** Is the FPT argument correct with the corrected indexing \(B_{(i,j),t}=c_{i,t-j}\) and the Cauchy–Binet formula for \(B^{\mathsf T}B\)? Is the dependence on \(q\) really only polynomial in the coefficient computation?

4. **Bit complexity.** What is the justified bit-complexity statement for the FPT theorem, assuming rational input and exact linear algebra? Which standard real-feasibility bound should be cited?

5. **Combination.** Can the two results be combined into a two-parameter statement, e.g.
\[
\text{fixed }q:\ \mathrm{P};\qquad
\text{fixed }\kappa_{\rm obs}:\ \mathrm{FPT}?
\]
Which should be the main theorem of an algorithmic paper?

6. **Novelty.** Are these algorithmic statements already implied by known results on parametric linear systems, real algebraic geometry, or the Fernando 2026 characterization? If so, what is the correct citation/positioning?

7. **Hardness.** Given the soundness obstruction, should the gate programme be paused? Is there a known hardness source that naturally respects the global row-space condition \(\operatorname{row}H_A=\operatorname{row}H\) and the per-row space \(\mathcal T\), rather than local row-copy gates?

## Part VI. Bottom line

- Two algorithmic skeletons are written: fixed \(q\) polynomial (XP) and fixed \(\kappa_{\rm obs}\) FPT.
- Both rest on Gram/Bezout certificates and rank-consistency elimination; exact checks cover the algebraic identities, not the full complexity proofs.
- The hardness programme currently has no sound multiplication gate and no reduction.
- An audit of the two skeletons, especially the fixed-\(q\) reduction and the FPT bit complexity, is requested before turning them into a paper.
