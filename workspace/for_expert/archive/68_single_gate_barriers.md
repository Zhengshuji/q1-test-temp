# Single-gate realization: structural barriers, and a request for the next architecture

This report records the attempt to build the one-gate gadget requested in the previous programme. The uniform spectral part is solved; the obstruction is the realization with a fixed \(L_0\). We ask whether the fixed-\(L_0\) variable-kernel route is viable, and whether the arithmetic variables can instead enter the spectral map \(D(X)\) with a fixed kernel.

## Part I. Setting

With \(K_0=\ker[C;CA]\), \(N=N_K\), \(H=LN\), \(H_A=LAN\), \(\omega=\operatorname{rank}H\), \(c=k-\omega\), \(P(\lambda)=\lambda H-H_A\), and \((5a)(5b)\) as usual. The six-dimensional template
\[
Ae_1=e_5,\quad Ae_2=e_1,\quad Ae_5=e_6,\quad C=e_6^*,\quad L_0=e_1^*,\quad
L=[e_1^*;e_2^*;e_1^*+e_2^*+e_5^*]
\]
is feasible with \(H_A=DH\), \(D=\begin{bmatrix}0&1&0\\0&0&0\\1&1&0\end{bmatrix}\), and \(P\) of constant rank \(2\).

## Part II. Results

### II.1 Uniform spectral lemma (solved)

If \(H_A(X)=D(X)H(X)\), \(\operatorname{im}H(X)=W\) fixed, and \(D(X)\) preserves a filtration
\[
D(X)w_j=w_{j+1}+\sum_{i\le j}a_{ij}(X)w_i,\qquad
D(X)w_{\omega-1}=g+\sum_i a_{i,\omega-1}(X)w_i,
\]
then the submatrix of \((\lambda I-D)|_W\) on rows \((w_1,\dots,w_{\omega-1},g)\) and columns \((w_0,\dots,w_{\omega-1})\) is upper triangular with diagonal \(-1\). Hence \(\operatorname{rank}P_X(\lambda)=\omega\) for all \(X,\lambda\). This is a unit-minor certificate, independent of the coefficients \(a_{ij}(X)\).

### II.2 Fixed \(L_0\) forbids the naive graph chart

\(H\)'s first row is \(H_0=L_0N\), fixed by the input. The graph chart \(H(X)=[I\ -X]\) has a variable first row, so it cannot be used directly. The correct normal form with a fixed first row is
\[
H(X)=C_0\begin{bmatrix}h_0\\g(X)\end{bmatrix},
\]
with \(C_0\) fixed, \(h_0=L_0N\), and \(g(X)\) variable; then \(\operatorname{im}H=\operatorname{im}C_0\) is fixed.

### II.3 \(\omega=2\), \(q=3\) is impossible with a variable kernel

With \(q=3\), \(H\) has rows \(h_0,g,h_0+g\). \(H_A=DH\) forces \(h_{A,0}\in\operatorname{span}\{h_0,g(X)\}\) for all \(X\). If \(g(X)\) varies outside \(\operatorname{span}h_0\) (needed for a variable kernel), the intersection is \(\operatorname{span}h_0\), so \(h_{A,0}=\lambda_0h_0\), and \(P(\lambda_0)\) has a zero row. Hence a variable kernel needs \(q\ge4\) for \(\omega=2\), or \(\omega\ge3\).

### II.4 Two further obstructions

- Shift \(A\): \(h_A(v)\in R(X)\) forces \(v\) to lie in a fixed direction, so the kernel cannot vary.
- \(A(W)\subseteq S\): all \(h_A(v)\) lie in the fixed \(S^*\), so the \(D\)-column of the variable direction is zero (rank drop at \(\lambda=0\)); if instead \(h_A(v)\) has a \(v\)-component, that direction is an eigenvector of \(D\) (rank drop). A two-step variable chain is needed, suggesting \(\omega\ge4\).

### II.5 Experiments

- Perturbing the six-dimensional template (\(e_2^*\mapsto e_2^*+t e_3^*\)) is feasible only at \(t=0\); \(t=\pm1,2\) fail \((5b)\).
- On the feasible \(\dim W_L=3\) instance, the natural family \(V_t=\operatorname{span}\{e_4,e_5+t e_6\}\) is feasible only at \(t=0\) (exact and symbolic for that family).
- A systematic search of \(\operatorname{Gr}(2,3)\) on the \(\dim W_L=3\) instance (18 planes: 10 structured, 8 random; all row combinations with coefficients in \(\{-1,0,1\}\), exact checks) finds exactly one good plane, \(V_{45}=\operatorname{span}\{e_4,e_5\}\). The good kernel appears isolated, not open.


### II.6 A working fixed-kernel family (the bypass of Question 3)

On the feasible \(\dim W_L=3\) instance, take the fixed compressed rows
\[
H=[e_3;\ e_3+e_6;\ e_3+e_6]
\]
and the family
\[
L_3(s)=s e_2+e_3+e_6,\qquad L(s)=[e_3;\ e_3+e_6;\ L_3(s)].
\]
Since \(e_2N=0\) and \(e_2AN=e_3+e_6
e0\), the kernel is fixed while
\[
H_A(s)=[e_3;\ e_3+3e_6;\ (1+s)e_3+(3+s)e_6]
\]
varies. Exact checks give: for \(s=1,2,-1\), \((5a)\) and \((5b)\) hold and \(\operatorname{rank}[C;L]=4=p+q\); for \(s=0\) the pencil is still good but \(\operatorname{rank}[C;L]=3\), so it is excluded by the independence convention.

Thus the lift direction is a working variable channel: the variables need not enter the kernel, and the pencil is uniformly good along the family. However, feasibility along this family is the **open** condition \(s\ne0\), not an equation \(s=xy\); the lift parameter can absorb any value. Therefore the lift channel can adjust independence, but it **cannot force an arithmetic relation**. The arithmetic must enter through the kernel or through a determinantal zero-branch.

## Part III. Questions

**Question 1.** Is a variable-kernel family with fixed \(L_0\) possible at all? The obstructions above suggest that the fixed first row and the fixed \(h_{A,0}\) force either a parallel fixed direction (eigenvalue) or a fixed variable direction (no variation). Is there a general reason, or a construction we have missed?

**Question 2.** If a variable kernel is possible only for \(\omega\ge4\), what is the minimal architecture? We have in mind \(W=S\oplus V_2\) with \(\dim S=2\) fixed, and a two-step chain \(v_1\mapsto v_2\mapsto g_{\rm out}\) on the variable part; the fixed part must not be \(D\)-invariant, to avoid eigenvalues.

**Question 3 (the bypass, now tested).** The fixed-kernel lift family in II.6 works: the variables enter through \(g\in\operatorname{row}[C;CA]\) with \(gN=0\), \(gAN\ne0\), the kernel is fixed and the pencil is uniformly good. The remaining problem is that the lift parameter is **free**: feasibility is \(s\ne0\), so it cannot force \(s=xy\). The arithmetic must enter the kernel or a determinantal zero-branch. Do you see an architecture where a rank equality (not an open condition) forces the graph parameter to satisfy the multiplication relation?

**Question 4.** If the fixed-\(L_0\) variable-kernel route is impossible, is there a different hardness mechanism (e.g. varying the input rather than \(L\), or encoding in the lift/invisible directions)?

**Question 5.** Could you check the symbolic family in II.5 (all \(2\times2\) minors of the \(3\times4\) pencil, not just two rows) and confirm the isolation at \(t=0\)?
