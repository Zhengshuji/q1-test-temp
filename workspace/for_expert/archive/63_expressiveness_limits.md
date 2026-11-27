# Expressiveness limits for the hardness reduction: row-space, quadratic, and Sylvester constraints

This report records three attempts to encode affine constraints (as in affine rank minimisation) into the observer data, and the structural limits found. It asks whether these limits rule out a direct reduction, and what gadget to try next.

## Part I. Setting

With \(K_0=\ker[C;CA]\), \(N=N_K\), \(H=LN\), \(H_A=LAN\), \(\omega=\operatorname{rank}H\), \(c=k-\omega\). The compressed form of \((5a)\) is
\[
\ker H\subseteq\ker H_A\iff \operatorname{row}H\subseteq\operatorname{Ann}(V),\qquad V=\ker H\in\operatorname{Gr}(c,K_0).
\]
For \(V=\operatorname{graph}(X)\) in a chart of \(\operatorname{Gr}(c,K_0)\), \(A\) is partitioned accordingly.

## Part II. Three expressiveness results

### II.1 The constraints on \(H\) are row-space type

The bottom rows \(h_i=l_iN\) are free in \(K_0^*\) (since \(N\) has full column rank). The only equality constraints on \(H\) come from the kernel condition: every row lies in \(\operatorname{Ann}(V)\), for a single \(V\) determined by the data. Inside \(\operatorname{Ann}(V)\) the rows are free, subject only to the rank (open) and pencil conditions. Hence the observer does not impose arbitrary affine equations \(\langle A_i,H\rangle=b_i\); it imposes a **subspace inclusion** \(\operatorname{row}H\subseteq\operatorname{Ann}(V)\) plus the fixed top rows. In particular, identifying a source matrix \(X\) with \(H\) does not give a reduction.

### II.2 The chart constraints on \(V\) are quadratic

For \(V=\operatorname{graph}(X)\), the invariance condition \(A(V)\subseteq V\) is
\[
A_{21}+A_{22}X=X(A_{11}+A_{12}X),
\]
which contains the quadratic term \(XA_{12}X\). Hence the natural condition on the chart coordinates is quadratic, not affine. For invariant \(V\) the admissibility condition is automatic and the pencil is generically good; for non-invariant \(V\) the admissibility is a linear condition on the lifts. Neither produces linear equations in \(X\).

### II.3 A linearisation exists only in a structured (Sylvester) case

If \(A_{12}=0\), the invariance condition becomes the linear Sylvester equation
\[
A_{21}+A_{22}X-XA_{11}=0.
\]
With \(A_{11}=\operatorname{diag}(\lambda_i)\), \(A_{22}=\operatorname{diag}(\mu_j)\), this is entrywise
\[
(\mu_j-\lambda_i)X_{ij}=-(A_{21})_{ij}.
\]
Thus one can fix entries or impose relations with a **difference-matrix** coefficient structure, but not arbitrary linear functionals of \(X\). A single source constraint \(\sum_{ij}(A_1)_{ij}X_{ij}=b_1\) with arbitrary coefficients is not directly representable.

## Part III. Questions

**Question 1.** Do the three results above suffice to rule out a **direct** reduction from affine rank minimisation (or from ETR) that identifies the source matrix with \(H\) or with the chart matrix \(X\)? Or is there a standard encoding trick that circumvents the row-space/quadratic/Sylvester structure?

**Question 2.** Is there a known way to use the quadratic term \(XA_{12}X\) of the chart map as a **multiplication gadget**, in the spirit of the arithmetic-circuit encodings used for affine rank minimisation? If so, which variables should represent the source, and how are the affine constraints implemented?

**Question 3.** Could **block-diagonal gadgets** (several invariant blocks with different eigenvalues, plus several \(A_{21}\) blocks) generate enough difference-matrix equations to encode arbitrary affine constraints by combining them, or is the difference structure a genuine obstruction?

**Question 4.** If the answer to Question 1 is negative for affine rank minimisation, is **ETR in arithmetic-circuit form** the better source? What would be the smallest meaningful gadget to attempt first: one multiplication gate, one addition gate, or a rank-forcing gadget?

**Question 5.** Are there structural theorems in the observer literature (e.g. on the set of achievable compressed pairs \((LN,LAN)\)) that already describe the expressiveness limits we are encountering, so that we do not reprove them?

**Question 6.** Given these limits, should the hardness workstream continue with gadget construction, or would it be more valuable to first prove a **rigidity theorem** (a structural restriction on the set of feasible observer data) and only then look for a reduction?
