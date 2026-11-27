# Corrections, a general sufficient theorem, and the component-decomposition question

This report collects the results and corrections since the previous report, and asks for your view on the
overall direction of the program, in particular on \(q1\). Part I fixes the setting. Part II states the
results with their evidence level. Part III lists the questions.

## Part I. Setting

Given \(A\in\mathbb C^{n\times n}\), \(C\in\mathbb C^{p\times n}\), \(L_0\in\mathbb C^{r\times n}\), one seeks
\(R\in\mathbb C^{(q-r)\times n}\) with \(L=[L_0;R]\) full row rank and

\[
(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\quad\forall\lambda .
\]

Put \(K=\ker[C;CA]\), \(k=\dim K\), \(N=N_K\), \(M=AN_K\), \(H=LN\), \(H_A=LAN\), \(E=U_0=L_0N\),
\(F_0=V_0=L_0AN\), \(e=\dim E\). For a fixed rank \(\omega\), admissibility is
\(\operatorname{rank}H=\omega\) and \(\ker H\subseteq\ker H_A\); on it \(Z:W\to\mathbb C^q\),
\(W=\operatorname{im}H\), is defined by \(Z(Hx)=H_Ax\). Writing \(Z=(A;B)\) with the bottom \(\omega\) rows
forming \(B\), badness is
\[
\text{bad}\iff\exists\,0\ne y\in\ker B,\ Ay\in\mathbb C y .
\]

## Part II. Results

### II.1 The corrected projective theorem (v2)

For \(\sigma\in\mathbb P^{k-1}\), \(S=\ker\sigma\), choose a basis \(B\) of \(S\), and put
\[
P=B^\top Z_1,\qquad Q=B^\top Z_2,\qquad X_S=\{a:aP\in\operatorname{row}Q\}.
\]
The coordinate correction is
\[
\widetilde E_S=\{a\in\mathbb C^\omega:aB^\top\in E\},\qquad \dim\widetilde E_S=e,
\]
and the exact admissibility conditions are
\[
E+F_0\subseteq S,\qquad \widetilde E_S+X_S=\mathbb C^\omega
\ \Big(\iff e+\dim X_S-\dim(\widetilde E_S\cap X_S)=\omega\Big),\qquad m\ge\omega-e .
\]

The **lifted incidence space** includes \(R\) as a variable:
\[
\mathcal I=\{(\sigma,R):\ \operatorname{row}(L_0N)\subseteq S,\ \operatorname{row}(L_0AN)\subseteq S,\ 
\operatorname{row}(RN)\subseteq S,\ \operatorname{row}(RAN)\subseteq S,\ 
\operatorname{row}(L_0N;RN)=S,\ \operatorname{rank}[L_0;R]=q\}.
\]
It is locally closed (the last condition is open). It is stratified by
\[
\big(\operatorname{rank}Q,\ \operatorname{rank}[P;Q],\ \operatorname{rank}(\varphi_S|_{\widetilde E_S}),\ \operatorname{rank}H\big),
\]
where \(\varphi_S(a)=aP\bmod\operatorname{row}Q\). On every constant-rank stratum the bad set
\(\{(\sigma,R):\exists\lambda,\operatorname{rank}(\lambda H-H_A)<\omega\}\) is closed: homogenise \(\lambda\)
to \(\mathbb P^1\); at infinity the matrix is \(H\) of rank \(\omega\); the projection is proper. Hence on every
irreducible component either all points are bad, or the good points are Zariski-open dense; the generic
determinant divisor over \(\mathbb C(X)\) decides. Status: draft, M2.

### II.2 The lifting lemma

Let \(\mathcal R=\{R:RN=H_b,\ RM=H_{A,b}\}\), an affine subspace, and \(\pi:\mathbb C^n\to\mathbb C^n/\operatorname{row}L_0\).
Assume \(\operatorname{rank}L_0=r\) (otherwise no lift) and \(m\le n-r\). Then
\[
\operatorname{rank}[L_0;R]=q\iff\operatorname{rank}(\pi R)=m .
\]
A full-row-rank lift exists iff the symbolic matrix \(\pi R(t)\) has rank \(m\) over the function field of
the affine parameter space; then the full-row-rank lifts are Zariski-open dense. This is the general
affine-matrix lemma; the observer case is the quotient by \(\operatorname{row}L_0\). Status: proved.

### II.3 The \(k=3\) example table, and the retraction of a general linearity claim

We previously claimed that for \(k=3,e=0\) every rank stratum is a projective subspace or its complement,
hence irreducible. **This is false**, and we retract it. The counterexample is
\[
Z_1=\begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix},\qquad
Z_2=\begin{pmatrix}1&0\\0&2\\0&0\end{pmatrix}.
\]
Both images are \(U=\langle e_1,e_2\rangle\), so for every \(\sigma\in U\) the individual intersections
\(\dim(\operatorname{im}Z_i\cap\operatorname{span}\sigma)\) equal \(1\). But
\[
\operatorname{rank}\begin{bmatrix}P\\Q\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}Z_1\\Z_2\end{bmatrix}
-\dim\Big(\operatorname{im}\begin{bmatrix}Z_1\\Z_2\end{bmatrix}\cap(\operatorname{span}\sigma\oplus\operatorname{span}\sigma)\Big),
\]
and the common-preimage condition holds exactly at the two eigenvectors of \(\operatorname{diag}(1,2)\);
the rank-\((1,1)\) locus is two points, hence reducible. The correct general statement is only that the
rank-\(\operatorname{rank}Q\) strata are linear (via \(\operatorname{im}Z_2\)) while the stacked-rank strata are
determinantal, locally closed, and not necessarily irreducible.

The five-instance table (\(k=3\), \(d=1\) and \(d=2\)) remains as a collection of exact examples, not as a
general irreducibility theorem.

### II.4 The \(e>0\) data and the correction of the \(V_0Z_2\) criterion

For \(e=1\) (fixed top row \(U_0\ne0\)) we computed six instances at \(k=3,q=3,\omega=2\):

| seed | \(d\) | stratum \((r_Q,r_{PQ},\dim X_S,t)\) | good/bad | lift |
|---|---|---|---|---|
| 1163 | 1 | \((0,0,2,1)\) | good | yes |
| 1163 | 1 | \((1,1,2,1)\) | all bad | — |
| 753 | 2 | \((1,1,2,1)\) | all bad | — |
| 1081 | 2 | \((1,1,2,1)\) | good | yes |
| 1327 | 2 | \((1,1,2,1)\) | good | yes |
| 1491 | 2 | \((1,1,2,1)\) | good | yes |

Thus the \(d=1\) mixed phenomenon survives \(e=1\), while the \(d=2\) all-bad phenomenon fails when \(U_0\ne0\).

We then claimed that \(V_0Z_2=0\) implies all-bad. **That proof was wrong**: compatibility gives
\(y_iZ_2=-x_iZ_1\), which need not vanish, so \(y_i\) need not lie in \(\ker Z_2\). The correct object is
\[
Y=\{y\in\mathbb C^k:\ yZ_2\in\operatorname{row}Z_1\},\qquad
\dim Y=(k-\operatorname{rank}Z_2)+\dim(\operatorname{row}Z_1\cap\operatorname{row}Z_2).
\]
Since \(V_0Z_2=-U_0Z_1\in\operatorname{row}Z_1\) and \(y_iZ_2=-x_iZ_1\in\operatorname{row}Z_1\), all rows of
\(H_A\) lie in \(Y\). Hence:

> If \(\operatorname{row}Z_1\cap\operatorname{row}Z_2=0\), then \(\dim Y=k-2=\omega-1\) and every admissible
> compressed point is bad (at \(\lambda=0\)).

This holds for **every** \(k=\omega+1\) with \(d=2\) and \(\operatorname{rank}Z_2=2\). It is sufficient but not
necessary: instance 138 has nonzero intersection and is still all-bad, via another common root
\(\lambda_0=-1\).

### II.5 General theorem versus enumeration

The structural theorem of II.1 is independent of \(k\): only matrix sizes and the Grassmannian dimension
change. The \(k\)-specific part is the **component decomposition** of the determinantal strata, which is a
standard determinantal-variety problem (Bruns–Vetter; Fulton), not a \(k\)-by-\(k\) enumeration. We have
therefore made the following the main open problem.

### II.6 The main open problem: complexity of the component decomposition

For general \(k,\omega,q\), the decision reduces to:

1. decompose each rank stratum of the lifted incidence space into irreducible components;
2. compute the generic determinant divisor on each component;
3. decide the real-point question.

No polynomial algorithm is known; this is, in our present view, the concrete content of \(q1\). A first
bound: for \(k=\omega+1\), \(d=2\), the **base** rank stratification has at most \(16\) irreducible
components, independent of \(k\), because \(\operatorname{rank}Q\) is a linear condition on \(\sigma\) and
\(\operatorname{rank}[P;Q]\) is a quadratic (determinantal \(2\times2\)) condition. The **fibre** over each base
component, cut by \(\operatorname{rank}H=\omega\), is not bounded by this argument and remains the hard part.

## Part III. Questions

**Question 1.** Are the corrected theorem (II.1) and the lifting lemma (II.2) now correct? Is the lifted
incidence space with \(R\) the right object, and is the determinantal stratification the right general
statement? Is there any remaining coordinate or constructibility issue?

**Question 2.** Is the determinantal reformulation in II.3 the right way to present the \(k=3\) examples? Is
it worth keeping the five-instance table as exact examples, or should it be replaced entirely by the
general determinantal statement plus the restricted theorems?

**Question 3.** Is the \(e>0\) interpretation correct: \(d=1\) mixed is robust, \(d=2\) all-bad is a
\(U_0=0\) (or \(V_0Z_2=0\)) phenomenon? Is the sufficient condition
\(\operatorname{row}Z_1\cap\operatorname{row}Z_2=0\) sound, and is there a natural necessary condition?

**Question 4 (the main question).** What is your view on \(q1\) at this point? Is the
component-decomposition route the right one, or should the program aim at a hardness reduction, a
structural classification, or a different algebraic-geometric angle? Given the present state — a general
structural theorem, a correct lifting lemma, a restricted all-bad theorem, and a concrete open problem —
do you see a realistic route to either a polynomial algorithm or a hardness proof, and which one do you
consider more likely?

**Question 5.** Is the strategy of using concrete cases as examples (not as the theory) acceptable for a
paper, with the general determinantal theorem as the main result? Or should we first prove a general bound
on the number of components (or on the degrees) before writing anything?

**Question 6.** What would you do next: (a) bound the component count/degrees for general
\(k,\omega,q\), (b) attack the generic-gcd complexity over a component, (c) classify the
intersection-nonzero case at \(k>3\), (d) the real-point question, or (e) assemble the paper? We would
also welcome any suggestion or reference that would make the component-decomposition problem tractable.
