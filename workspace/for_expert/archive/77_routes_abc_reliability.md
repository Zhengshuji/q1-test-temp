# Routes A, B, C: current claims, verification levels, and a request for a reliability audit

This note summarizes the three current routes to \(q1\), states exactly what is proved, computed, or only sketched, and asks for both a mathematical check and a reliability audit.

## Part I. Setting and conventions

For fixed \(A,C,L_0\), find \(L=[L_0;R]\) with
\[
(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\ \forall\lambda.
\]
Let \(K_0=\ker[C;CA]\), \(N\) a basis, \(k=\dim K_0\), \(H=LN\), \(H_A=LAN\), \(\omega=\operatorname{rank}H\), and
\[
(5a)\iff\ker H\subseteq\ker H_A\iff \operatorname{row}(H_A)\subseteq\operatorname{row}H.
\]
The complexity of \(\exists L\) is \(q1\).

**Verification labels used below**:
- **P**: paper proof, not machine-checked;
- **E**: exact computation/script, for the stated finite instance or identity only;
- **S**: sketch/route, with a named missing step.

I mark every claim with one of these.

## Part II. Route A: fixed rows / incidence

### II.1 The decomposition (P)

Take \(q=4\), \(r_0=2\) fixed rows \(L_0\), \(r=2\) free rows \(R\), \(L=[L_0;R]\). Choose a left inverse \(N^+\) of \(N\) and write
\[
AN=NM+E,\qquad M=N^+AN,\qquad E=(I-NN^+)AN.
\]
With \(Y=RN\),
\[
H=\begin{bmatrix}H_0\\Y\end{bmatrix},\qquad
H_A=\begin{bmatrix}H_{A,0}\\YM+RE\end{bmatrix},
\]
and
\[
(5a)\iff H_{A,0}\in\operatorname{row}H\ \text{and}\ RE\in\operatorname{row}H.
\]
This is paper-level (P). The decomposition is algebraic; the only choice is \(N^+\).

### II.2 The incidence form (P)

For general \(E\),
\[
RE\in\operatorname{row}H\iff W_R:=\operatorname{row}(RE)\subseteq\operatorname{row}H.
\]
Since \(\dim W_R\le r=2\), this is a Grassmannian incidence condition:
\(\operatorname{row}H\) contains a fixed (for fixed \(R\)) subspace \(W_R\).
It is linear in Plücker coordinates of \(\operatorname{row}H\), but its zero locus is a determinantal variety, not an arbitrary affine hyperplane in the entries of \(H\).

**This does not by itself rule out Route A**: incidence systems can be universal. It only rules out identifying each affine equation with one incidence. (The expert has already confirmed this reading.)

### II.3 Rank-one section gate, compressed level (E)

Set \(q=4\), \(r_0=2\), \(k=4\), \(H_0=[e_1;e_2]\), \(S_0=\operatorname{row}H_0\), \(\pi:\mathbb C^4\to\mathbb C^4/S_0\), and
\[
Y=\begin{bmatrix}0&0&r_{11}&r_{12}\\0&0&r_{21}&r_{22}\end{bmatrix}.
\]
Then
\[
\operatorname{rank}H=3\iff \det\pi(Y)=0\iff r_{11}r_{22}-r_{12}r_{21}=0.
\]
On the chart \(r_{11}=1\), this is \(r_{22}=r_{12}r_{21}\), a multiplication relation.

This determinant identity is verified by an exact script (E) at the compressed level. **No full \(A,C,L_0\) instance has been constructed**, so this is not yet an observer gate.

### II.4 Missing pieces for Route A (S)

1. A full rational \(A,C,L_0\) realizing the compressed \(H_0,Y,\pi\) and the desired \(E\);
2. the role of \(E=0\): if \(E=0\), then \((5a)\) is automatic on the free rows, but the global rigidity theorem (\(A(K_0)\subseteq K_0\), \(\omega>0\) implies infeasibility) may rule it out;
3. the spectral guard: \((5b)\) is stronger than \(\operatorname{rank}H=3\); it requires \(\operatorname{rank}P(\lambda)=3\) for all \(\lambda\);
4. the chart boundary \(r_{11}=0\), which is a spurious branch unless excluded.

## Part III. Route B: \((5a)\) equalities + \((5b)\) nonvanishing

### III.1 Polarity (E)

- \((5a)\) is a rank equality, hence polynomial **equations** (maximal minors zero).
- \((5b)\) is \(\gcd\{\text{maximal minors of }P\}=1\), a **nonvanishing** condition.

This polarity matches the usual \(\exists\mathbb R\) format (equations plus nonvanishing). An exact script verifies the polarity on tested instances (E).

### III.2 Compressed nonzero gadget (E)

For \(q=3,\omega=2\), an explicit \(P(\lambda)\) has
\[
\gcd\{\text{all }2\times2\text{ minors of }P\}=f,
\]
so that \((5b)\iff f\ne0\). An exact script verifies this compressed identity (E).

**This is only a compressed-layer gadget**: it does not construct \(L\) with \(H=LN\), \(H_A=LAN\).

### III.3 The shared-\(f\) obstruction (P)

To make the gcd exactly \(f\), every free row of \(H\) must be an \(f\)-multiple of a fixed vector. Repeating rows does not repair this. A row-space invariant version conflicts with the linearity of \(H\) in \(L\): if \(f\) is a nonlinear invariant of the row space, it cannot be a common factor of all maximal minors without breaking \(H=LN\).

The claim “a single Plücker coordinate divides all maximal minors” is not proved. (P)

## Part IV. Route C: tractability

### IV.1 Fixed \(\kappa_{\rm obs}\): FPT (P, modulo standard QE)

Define
\[
\kappa_{\rm obs}=r\operatorname{rank}[N,AN].
\]
Since \(N\) has full column rank,
\[
\operatorname{rank}[N,AN]\ge k\quad\Rightarrow\quad \kappa_{\rm obs}\ge rk,
\]
so for \(r\ge1\), \(k,r,q\le f(\kappa_{\rm obs})\).

Then:
- \((5a)\) is encoded by all \((\omega+1)\)-minors of \([H_A;H]\) vanishing plus one nonzero \(\omega\)-minor;
- \((5b)\) is encoded by a Bezout identity \(\sum g_i f_i=1\) over the maximal minors \(f_i\) of \(P\);
- a constructive Bezout bound gives \(\deg g_i\le(s-1)\omega\), where \(s=\binom{k}{\omega}\), so all degrees and variable counts are \(f(\kappa_{\rm obs})\);
- real quantifier elimination in fixed dimension then gives
\[
\text{fixed }\kappa_{\rm obs}\ \Rightarrow\ q1\in\mathrm{FPT}
\]
modulo the standard real-QE bound.

This is paper-level (P). The only external ingredients are the Bezout degree bound and the standard fixed-dimension real-QE complexity. No machine verification of the full theorem exists; the rank-nullity core is Lean-checked separately.

### IV.2 Fixed \(q\): polynomial route (S)

A sketch: fix \(q\), quantify over \(Z\in\mathbb C^{q\times q}\) and \(U=\operatorname{im}H\in\operatorname{Gr}(\omega,q)\); then \(H=LN\), \(H_A=LAN\), \(H_A=ZH\), \(\operatorname{im}H=U\) are linear/rank conditions in \(L\), which can be eliminated by linear algebra. Since \(Z,U\) have dimension depending only on \(q\), this suggests a polynomial algorithm for fixed \(q\).

**The linear-elimination rank criterion is not written**, and no machine check exists. This is a sketch (S), not an established theorem.

## Part V. Questions

**Question 1 (reliability audit).** Please check the following claims and mark each as correct, requiring an extra hypothesis, or wrong:
1. the decomposition \(AN=NM+E\) and \((5a)\iff H_{A,0}\in\operatorname{row}H\) and \(RE\in\operatorname{row}H\);
2. the incidence form \(RE\in\operatorname{row}H\iff W_R\subseteq\operatorname{row}H\);
3. the compressed determinant identity \(\operatorname{rank}H=3\iff r_{11}r_{22}-r_{12}r_{21}=0\) for the displayed \(H_0,Y\);
4. the polarity “\((5a)\) equations, \((5b)\) nonvanishing”;
5. the shared-\(f\) necessity;
6. the fixed-\(\kappa_{\rm obs}\) FPT argument, especially the Bezout degree bound \((s-1)\omega\);
7. the fixed-\(q\) polynomial sketch: is the linear elimination legitimate, and does it really avoid exponential dependence on \(n\)?

**Question 2 (Route A completion).** Can the compressed rank-one gate be realized by a full \(A,C,L_0\)? Is \(E=0\) fatal by the rigidity theorem, and if so, how should \(E\) be chosen to keep \((5a)\) nontrivial while preserving \((5b)\)? How should the chart \(r_{11}=0\) be excluded?

**Question 3 (Route B).** Is there a mechanism to force every free row to share the same factor \(f\) without breaking \(H=LN\)? Or is the compressed nonzero gadget fundamentally non-liftable?

**Question 4 (Route C).** Is the fixed-\(q\) polynomial route correct? If yes, what is the missing rank criterion? If not, where does the exponential dependence on \(n\) enter?

**Question 5 (priority).** Given the reliability audit, which route should be pursued: complete the rank-one gate (A), force the shared factor (B), or finish the fixed-parameter algorithms (C)?
