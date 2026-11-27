# Route A: fixed rows as affine constants, free rows as variables, and the incidence obstruction

This note summarizes the attempt to reduce ARM(3) to the observer problem using fixed rows, states the structural obstruction reached, and asks whether the route can be repaired or should be abandoned.

## Part I. Setting

For fixed \(A,C,L_0\), find \(L=[L_0;R]\) with
\[
(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\ \forall\lambda.
\]
Let \(K_0=\ker[C;CA]\), \(N\) a basis, \(k=\dim K_0\), \(H=LN\), \(H_A=LAN\).
It is standard in this framework that
\[
(5a)\iff \ker H\subseteq\ker H_A\iff \operatorname{row}(H_A)\subseteq\operatorname{row}H.
\]
The open problem is the complexity of \(\exists L\), i.e. \(q1\).

ARM(3): given affine constraints \(\langle A_\ell,X\rangle=b_\ell\) on \(X\in\mathbb R^{m\times n}\), decide whether some feasible \(X\) has \(\operatorname{rank}X\le3\). It is \(\exists\mathbb R\)-complete (Majumdar 2026), already for rank 3.

## Part II. Route A

### II.1 The architecture

Take \(q=4\) observer rows, \(r_0=2\) fixed rows \(L_0\), \(r=2\) free rows \(R\), so \(L=[L_0;R]\).
Then \(H\) is \(4\times k\). If \(\omega=\operatorname{rank}H=3\), then \(X=H\) is a \(4\times k\) matrix of rank 3 — the shape of ARM(3).
The intended roles:
- fixed rows \(L_0\) supply constants;
- free rows \(R\) supply variables;
- \((5b)\) enforces \(\operatorname{rank}H=3\);
- \((5a)\) encodes the affine constraints.

### II.2 Decomposition of \((5a)\)

Choose a left inverse \(N^+\) of \(N\) and write
\[
AN=NM+E,\qquad M=N^+AN,\qquad E=(I-NN^+)AN.
\]
With \(Y=RN\),
\[
H=\begin{bmatrix}H_0\\Y\end{bmatrix},\qquad
H_A=\begin{bmatrix}H_{A,0}\\YM+RE\end{bmatrix}.
\]
Since \(YM\in\operatorname{row}Y\subseteq\operatorname{row}H\),
\[
\boxed{(5a)\iff H_{A,0}\in\operatorname{row}H\ \text{and}\ RE\in\operatorname{row}H.}
\]
The second condition is the only place where \(E\) can encode something beyond the fixed-row incidence.

### II.3 Rank-one \(E\)

If \(E\) has a single nonzero column \(e_a\), then \(RE\) has a single nonzero column \(R e_a\), and
\[
RE\in\operatorname{row}H
\iff
R e_a=0\ \text{or}\ e_j\in\operatorname{row}H
\]
(where \(e_j\) is the corresponding standard basis vector of \(\mathbb C^k\)).
If \(k=3\) and \(\operatorname{rank}H=3\), this is automatic; non-triviality requires \(k>\omega\).
Thus each column of \(E\) gives at most one linear row-space condition.

### II.4 General \(E\): the incidence obstruction

For general \(E\),
\[
RE\in\operatorname{row}H
\iff
W_R:=\operatorname{row}(RE)\subseteq\operatorname{row}H.
\]
Since \(W_R\subseteq\operatorname{row}E\) and \(\dim W_R\le r=2\), this is a Grassmannian incidence condition:
\[
\{\Lambda\in\operatorname{Gr}(3,k):\ W_R\subseteq\Lambda\}.
\]
In Plücker coordinates it is linear in \(\Lambda\), but it is not an arbitrary linear functional on the entries of \(H\); its zero locus is a determinantal variety of degree \(\omega\), not a hyperplane.

By contrast, the ARM constraints are
\[
\langle A_\ell,H\rangle=b_\ell,
\]
i.e. affine hyperplanes in the entries of \(H\). The two types do not match: an incidence condition is a rank/determinant condition, while an ARM constraint is a linear equation.

With several fixed rows, \((5a)\) gives several incidences \(H_{A,i}\in\operatorname{row}H\); requiring \(\operatorname{row}H\) to contain many fixed points is again a rank condition on those points (their span must have dimension at most 3), not an arbitrary affine system.

## Part III. Questions

**Question 1 (obstruction).** Is the incidence-versus-affine mismatch decisive, or can a finite family of incidences encode an arbitrary affine system on \(H\)? If the latter, what is the mechanism that turns a hyperplane condition into a subspace-containment condition?

**Question 2 (ARM variant).** Is there a variant of ARM(3) or of an \(\exists\mathbb R\)-complete problem whose constraints are themselves incidence/rank conditions (so that Route A's natural output matches the input)? For example, a rank-constrained matrix completion with prescribed subspace incidences rather than entrywise affine equations.

**Question 3 (saving Route A).** Could one use several blocks/gadgets so that each affine equation is represented by a separate incidence, with a composition lemma? Or does the dimension count \(q=4\), \(r=2\) forbid this?

**Question 4 (fallback).** If Route A is closed, which is more promising:
- Route B: encode residuals into the spectral branch \((5b)\iff\operatorname{im}H\cap E_\lambda(F)=\{0\}\), or
- Route C: remove the fixed-\(\kappa_{\rm obs}\) restriction from the FPT theorem and look for a polynomial algorithm?

**Question 5 (check).** Please check the decomposition \(AN=NM+E\) and the equivalence \((5a)\iff H_{A,0}\in\operatorname{row}H\) and \(RE\in\operatorname{row}H\). In particular, is the use of a left inverse \(N^+\) legitimate for the observer's row-space conditions, and is \(E\) the only possible encoder?
