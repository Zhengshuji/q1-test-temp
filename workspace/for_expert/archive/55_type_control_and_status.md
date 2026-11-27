# From the hyperplane theorem to a type-control conjecture: results, corrections, and the next step

This report collects the results and corrections since the previous report, classifies each result by
its evidence level, and asks for your judgement on the general framework, the low-codimension
classifications, the formalization priorities, and the paper plan.

## Part I. Setting

Given \(A\in\mathbb C^{n\times n}\), \(C\in\mathbb C^{p\times n}\), \(L_0\in\mathbb C^{r\times n}\), one seeks
\(R\in\mathbb C^{(q-r)\times n}\) with \(L=[L_0;R]\) full row rank and

\[
(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\quad\forall\lambda .
\]

Put \(K=\ker[C;CA]\), \(k=\dim K\), \(N=N_K\), \(H=LN\), \(H_A=LAN\), \(E=U_0=L_0N\),
\(F_0=V_0=L_0AN\), \(e=\dim E\). For a fixed rank \(\omega\), \(W=\operatorname{im}H\), and
\(Z:W\to\mathbb C^q\) is induced by \(H_A\). Writing \(Z=(A_W;B_\perp)\) with
\(A_W\in\mathbb C^{\omega\times\omega}\), \(B_\perp\in\mathbb C^{(q-\omega)\times\omega}\), badness is
\[
\text{bad}\iff\exists\,0\ne y\in\ker B_\perp,\ A_Wy\in\mathbb C y .
\]

Throughout, \(c=k-\omega\) is the codimension, \(\delta=\dim\ker T\) with \(T:K\oplus K\to\mathbb C^n\),
\(T(v,w)=v+Aw\), and \(V\in\operatorname{Gr}(c,K_0)\) is the annihilator variable, with
\[
K_0=\{v\in K:\ \sigma E^\top=0,\ \sigma F_0^\top=0\},\qquad
W=V\cap A^{-1}V,\qquad \rho(V)=\dim(V+AV)=2c-\dim W .
\]

## Part II. Results and corrections

### II.1 The hyperplane vector-bundle theorem

For \(c=1\), \(S=\ker\sigma\), \(v=N\sigma^\top\). The constraints on \(R\) are linear:
\[
Rv=0,\qquad RAv=0 .
\]
The rank of the two constraints is \(\rho(v)=\operatorname{rank}[v,Av]\in\{1,2\}\), and
\(\rho(v)=1\iff v\) is an eigenvector of \(A\). The base is \(\mathbb P(K_0)\); the rank-one locus is
\[
\mathcal B_1=\bigcup_{\lambda\in\operatorname{spec}(A)}\mathbb P\big(K_0\cap\ker(A-\lambda I)\big),
\]
and the non-eigenvector open set is irreducible. Over each constant-\(\rho\) piece the admissible \(R\)'s form
a vector bundle of rank \(m(n-\rho)\), and the conditions \(\operatorname{rank}H=\omega\),
\(\operatorname{rank}[L_0;R]=q\) are open. Hence the lifted incidence space has at most
\[
\delta+1
\]
nonempty irreducible components. Moreover
\[
\operatorname{rank}\begin{bmatrix}P\\Q\end{bmatrix}=\delta-2+\operatorname{rank}[v,Av],\qquad
\operatorname{rank}Q=\begin{cases}\delta-1,&v\in D_A=K\cap A^{-1}K,\\ \delta,&v\notin D_A.\end{cases}
\]
This replaces the earlier crude bound of 16 components. Evidence level: M2 write-up of your argument; not
Lean-formalizable at present (Grassmannians/bundles).

### II.2 The invariant eigenspace obstruction

If \(v\in K\cap\ker A\), then \(Av=0\), so every row of \(H_A\) annihilates \(v\), and
\(\operatorname{rank}H_A\le k-\dim(K\cap\ker A)\). Hence
\[
\dim(K\cap\ker A)>k-\omega\ \Longrightarrow\ \text{every admissible point is bad at }\lambda=0,
\]
and for \(k=\omega+1\) the sufficient condition is \(\dim(K\cap\ker A)\ge2\). More generally, for every
\(\lambda\),
\[
\dim\bigl(K\cap\ker(A-\lambda I)\bigr)\le k-\omega
\]
is necessary for a good candidate. The exact criterion remains the generic determinant divisor.
Evidence: M2, with your direct proof; the rank inequality has been compiled as a standalone Lean kernel
(axioms: `propext`, `Classical.choice`, `Quot.sound`); the remaining step is adding it to the project's
build graph.

### II.3 \(c=2\): classification, corrections, algorithm

Let \(V\in\operatorname{Gr}(2,K_0)\), \(W=V\cap A^{-1}V\), \(t=\dim W\).

* \(t=2\): \(V\) is \(A\)-invariant. By the Jordan type of \(A|_V\): two distinct eigenvalues give points;
  a scalar block gives \(\operatorname{Gr}(2,E_\lambda\cap K_0)\); a nontrivial Jordan block gives a bundle
  \(J_\lambda\to\mathbb P(E_\lambda\cap K_0)\) with affine fibre \(\mathbb A^{m_\lambda}\), \(m_\lambda=\dim E_\lambda\).
* \(t=1\): **two subtypes**.
  (a) \(AW=W\): an invariant line; \(V=L\oplus\langle w\rangle\), a bundle over the eigenline.
  (b) \(AW\ne W\): \(AL\) is another line in \(V\), so \(V=L+AL\) is **determined by \(L\)**;
  \(L\) ranges over \(\mathbb P(D)\setminus\bigcup_\lambda\mathbb P(E_\lambda\cap D)\),
  \(D=K_0\cap A^{-1}K_0\), and \(A(AL)\notin V\). This subtype is nonempty iff \(D\ne0\) and \(A|_D\)
  is not scalar.
* \(t=0\): open.

The component bound is
\[
\binom{s}{2}+3s+2,
\]
\(s\) the number of distinct eigenvalues, independent of \(k\). Nonemptiness conditions are linear-algebraic
in \(m_0=\dim K_0\), \(e_\lambda=\dim(E_\lambda\cap K_0)\), \(T_\lambda=(A-\lambda I)|_{K_0}\).

The corresponding algorithm enumerates the nonempty components, samples one generic \(V\) per component,
samples \(R\) in \((V+AV)^\perp\), checks the two open rank conditions, and computes the \(\omega\)-minor gcd.
It is one-sided: it never accepts a bad instance; on a good component a random point avoids the proper
closed bad set, so the false-negative probability is bounded by Schwartz–Zippel. Evidence: M2; the
algorithm is not Lean-related.

### II.4 \(c=3\): layers and the invariant/non-invariant correction

For \(V\in\operatorname{Gr}(3,K_0)\), \(t=\dim W\), \(\rho=6-t\):

* \(t=3\): \(A|_V\) has Jordan type \(1+1+1\), \(2+1\), or \(3\); the \(3\)-chain condition is an iterated
  preimage condition in \(K_0\).
* \(t=2\): **two subtypes**. (a) \(AW=W\): an invariant \(2\)-subspace, a bundle over the \(c=2\) \(\mathcal D_2\)
  pieces with a line in \(K/W\). (b) \(AW\ne W\): if \(A|_W\) is invertible, \(V=W+A(W)\) with
  \(\dim(W\cap A(W))=1\); if \(A|_W\) is singular, \(V=W\oplus\langle w\rangle\) with \(Aw\notin V\), or
  \(V=W+\langle A(W)\rangle\).
* \(t=1\): **two subtypes**. (a) \(AL=L\): \(V/L\) is a \(2\)-plane in \(K/L\) with no \(\bar A\)-invariant line
  (the \(c=2\) \(\mathcal D_4\) condition for \(\bar A\)). (b) \(AL\ne L\):
  \(V=L\oplus A(L)\oplus\langle w\rangle\), \(A(A(L))\notin V\).
* \(t=0\): open.

The earlier statement "\(\mathcal D_4\) consists of \(V\) containing an invariant \(2\)-subspace" only
covers subtype (a). The correction is the same as in II.3.

### II.5 A counterexample to the invariant-subspace picture, and the correct invariant

Take \(K=K_0=\mathbb C^4\), \(A=J_4(0)\), \(V=\langle e_2,e_3\rangle\). Then
\[
V\cap A^{-1}V=\langle e_3\rangle,\qquad t=1,
\]
but \(V\) contains no invariant line: \(Ae_2=e_1\notin V\), \(Ae_3=e_2\in V\) but \(e_2\notin\langle e_3\rangle\),
and no combination \(\alpha e_2+\beta e_3\) is an eigenvector. Thus \(V\in\mathcal D_3\) but has no invariant
line. The correct invariant is
\[
W=V\cap A^{-1}V,\qquad B=A(W)\subseteq V,
\]
not an invariant subspace.

### II.6 The type-control theorem

Define
\[
\tau(V)=\bigl(t,\ r=\operatorname{rank}(A|_W),\ s_0=\dim(W\cap A(W)),\ \text{Jordan type of }A|_W\bigr),
\]
and the \(W\)-stratum
\[
X_\tau=\{W\in\operatorname{Gr}(t,K_0):\ A(W)\subseteq K_0,\ \operatorname{rank}(A|_W)=r,\ 
\dim(W\cap A(W))=s_0,\ \text{Jordan type}=\tau\}.
\]
For \(W\in X_\tau\), \(B=A(W)\) has rank \(r\); \(V\) must contain \(W+B\), and \(V/(W+B)\) is a
\((c-t-(r-s_0))\)-plane in \(K/(W+B)\), subject to the open condition \(A(V)\cap V=B\). Hence the layer is
a Grassmannian bundle over \(X_\tau\) with open fibre, and its components correspond to those of \(X_\tau\).
For \(t<c\), \(X_\tau\) is the same problem at level \(t\), so this is an induction on \(c\); for \(t=c\)
one gets the invariant \(c\)-subspaces, classified by the Jordan type of \(A|_V\); the base \(c=1\) is II.1.
Consequently
\[
N(c)\le\sum_{\tau}N(t(\tau)),
\]
with finitely many types for fixed \(c\), so \(N(c)\) is finite and depends only on \(c\) and the Jordan
type of \(A|_{K_0}\), not on \(k\).

This is the main new general statement. It is a draft (M2): the per-type classification of \(X_\tau\) and
the nonemptiness conditions for general \(c\) are not yet written.

### II.7 Status of the results

| Result | Evidence | Lean |
|---|---|---|
| II.1 hyperplane theorem | M2 (your argument) | no (bundles) |
| II.2 eigenspace obstruction | M2 | yes: abstract rank inequality |
| II.3 \(c=2\) classification | M2 | partial (subspace lemmas) |
| II.3 \(c=2\) algorithm | M2 | no |
| II.4 \(c=3\) layers | M2 draft | no (bundles) |
| II.5 counterexample | M2, proved | yes: explicit \(4\times4\) matrix |
| II.6 type-control | M2 draft | no (induction/bundles) |

The main corrections since the previous report are: the \(k=3\) linearity retraction (already reported),
the \(V_0Z_2\) proof retraction (already reported), the invariant-subspace over-simplification in the
\(c=2\) and \(c=3\) classifications (corrected by the two-subtype analysis), and the replacement of the
16-component bound by \(\delta+1\).

## Part III. Questions

**Question 1.** Is the type-control theorem (II.6) the right general framework? Is the type
\((t,r,s_0,\text{Jordan type of }A|_W)\) the right invariant, or is there a better one? The pair
\((W,A(W))\) is a linear relation; should the classification be phrased in the language of linear relations
or descriptor systems, and is there a known normal form for such pairs?

**Question 2.** Are the two-subtype classifications for \(c=2\) (II.3) and \(c=3\) (II.4) correct and
complete? In particular, for \(A|_W\) singular with \(A(W)\subseteq W\), and for the position of \(A(A(W))\),
are there further subtypes we have not listed?

**Question 3.** Which propositions should be formalized in Lean first? We plan the rank inequality of II.2
(abstract finrank: if \(U\subseteq\ker f\) and \(\dim U>\dim K-\omega\), then
\(\operatorname{rank}f<\omega\)) as the first kernel, then the explicit counterexample of II.5. Is that the
right priority, or would you formalize the lifting rank formula or the block criterion first?

**Question 4.** Is the paper plan sound: (1) exact reduction and block criterion; (2) lifting; (3) the
hyperplane theorem and algorithm; (4) \(c=2\) classification and algorithm; (5) \(c=3\); (6) the
type-control theorem as a conjecture or draft theorem; (7) exact examples; (8) general \(c\) and open
problems? Should II.6 be presented as a theorem with the per-type proof deferred, or as a conjecture?

**Question 5.** For the general \(c\) type classification, is there a known classification of the pairs
\((W,A(W))\) — for instance by the Kronecker type of the pair of maps \(W\to K\), \(A|_W\) — that we should
use? We would welcome references on linear relations, descriptor systems, or determinantal strata of
subspace pairs.

**Question 6.** Does the type-control route change the complexity picture for \(q1\)? Is a polynomial
algorithm for fixed \(c\) plausible, or could the type classification hide a hardness result?

**Question 7.** What would you do next: the per-type classification of \(X_\tau\), the \(c=2\)/\(c=3\)
algorithms, or the paper? We would also welcome any other suggestion on the direction of the program.
