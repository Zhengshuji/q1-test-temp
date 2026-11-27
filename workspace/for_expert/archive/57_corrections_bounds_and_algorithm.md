# From the corrected fibre theorem to a general component bound: results, a blocked algorithm, and requests

This report collects the work since the previous report, states the one point where we are blocked, and asks for references, corrections, and direction.

## Part I. Setting

Given \(A\in\mathbb C^{n\times n}\), \(C\in\mathbb C^{p\times n}\), \(L_0\in\mathbb C^{r\times n}\), one seeks
\(R\in\mathbb C^{(q-r)\times n}\) with \(L=[L_0;R]\) of full row rank and

\[
(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\quad\forall\lambda .
\]

Put \(K_0=\ker[C;CA]\), \(k=\dim K_0\), \(N=N_K\), \(H=LN\), \(H_A=LAN\), \(c=k-\omega\) with
\(\omega=\operatorname{rank}[H;H_A]\), and \(P(\lambda)=\lambda H-H_A\). We work with the compressed problem:
\(V=\ker H\in\operatorname{Gr}(c,K_0)\) is the admissible \(c\)-plane, \(W=V\cap A^{-1}V\), \(t=\dim W\),
\(U=W+A(W)\), and the companion map
\[
\Phi_V:V\longrightarrow\mathcal X/V,\qquad v\longmapsto Av+V,
\]
with \(\ker\Phi_V=V\cap A^{-1}V=W\) and \(\operatorname{rank}\Phi_V=c-t\).

The structural facts we rely on are the spectral criterion (constant \(\gcd\) of the \(\omega\)-minors of
\(P(\lambda)\)), the block criterion (at a fixed \(\lambda\), \(\operatorname{rank}P(\lambda)<\omega\) iff
there is \(0\ne y\in\ker B\) with \(Ay=\lambda y\) for the block form \(Z=(A;B)\)), and the fibre theorem
below.

## Part II. Results and corrections

### II.1 The corrected fibre theorem

As you recommended, the quotient is the ambient state space:
\[
\mathcal F_W=\{V\in\operatorname{Gr}(c,K_0):\ U\subseteq V,\ \operatorname{rank}\Phi_V=c-t\},
\]
an open subset of \(\operatorname{Gr}(c-\dim U,K_0/U)\). The proof is the identify
\(\ker\Phi_V=V\cap A^{-1}V\); no \(A\)-invariance of \(K_0\) is used. All statements in the \(c=2\) and \(c=3\)
sections have been rewritten with \(\mathcal X/V\).

### II.2 The \(c=2\) admissible layers

Six mutually disjoint layers, with exact parameter spaces:

* \(t=2\), distinct eigenvalues: \(\big(\mathbb P(E_\lambda\cap K_0)\times\mathbb P(E_\mu\cap K_0)\big)/S_2\);
* \(t=2\), scalar: \(\operatorname{Gr}(2,E_\lambda\cap K_0)\);
* \(t=2\), Jordan block: an eigenline \(\ell\subseteq E_\lambda\cap K_0\) that also satisfies the chain-lifting
  condition \(\ell\subseteq(A-\lambda I)(K_0)\), and an affine fibre of dimension \(\dim(E_\lambda\cap K_0)-1\);
* \(t=1\), \(A(L)\subseteq L\): \(V=L\oplus\langle x\rangle\) with \(Ax\notin L+\langle x\rangle\);
* \(t=1\), \(A(L)\not\subseteq L\): \(V=L+AL\), with the exact condition \(\operatorname{rank}[v,Av,A^2v]=3\);
* \(t=0\): the open set \(\{V:V\cap A^{-1}V=0\}\).

The layers are exhaustive and disjoint. This is the admissible part only; the feasibility of \(q=\omega+1\)
requires in addition that \(V\) be good.

### II.3 The \(c=3\) admissible layers

Eight layers: for \(t=3\), the Jordan types of \(A|_V\) (distinct eigenvalues; \(1+1+1\); \(1+1\) plus a
distinct eigenvalue; \(2+1\); \(2\) plus a distinct eigenvalue; \(3\), with the two chain-lifting conditions
\(\mathbb C T^2u\subseteq(A-\lambda I)(K_0)\) and \(\mathbb C Tu\subseteq(A-\lambda I)^2(K_0)\)); for \(t=2\),
\(\dim U=3\) (with \(Ab\notin V\)) and \(\dim U=2\) (with \(Ax\notin W+\langle x\rangle\)); for \(t=1\),
\(A(L)\subseteq L\) (with \(U'\cap\bar A^{-1}U'=0\)) and \(A(L)\not\subseteq L\) (with \(Ax+V\) and \(A^2L+V\)
independent in \(\mathcal X/V\)); for \(t=0\), the open condition \(\operatorname{rank}\Phi_V=3\).

### II.4 Component bounds

Using the irreducibility of the above parameter spaces (Grassmannians, projective spaces, projective linear
subspaces, affine fibres, finite quotients), we obtain for \(s=\#\{\text{distinct eigenvalues of }A\}\le n\):
\[
c=2:\ \#\{\text{components}\}\le\binom{s}{2}+3s+2,\qquad
c=3:\ \#\{\text{components}\}\le\binom{s}{3}+3s^2+6s+1.
\]
The same bounds hold for the good locus, which is an open subset of each irreducible layer. This turns the
component-count part of the type-control conjecture into a theorem in these two cases. In the general case we
can prove unconditionally only the invariant part (\(t=c\)): the Jordan type of \(A|_V\) gives at most
\(p(c)\,n^c\) components, where \(p(c)\) is the number of partitions of \(c\). The remaining part (\(t<c\))
reduces to the irreducibility of the determinantal strata
\(S_{t,u}=\{W\in\operatorname{Gr}(t,D):\dim(W+A(W))=u\}\), which is the open point for \(c\ge4\).

### II.5 General incidence theorems

For fixed \((t,u)\) with \(t\le u\le2t\), the condition \(\dim(W+A_0(W))=u\) is a locally closed determinantal
stratum in \(\operatorname{Gr}(t,D)\); over it, the admissible \(V\)'s form an open subvariety of the relative
Grassmannian \(\operatorname{Gr}(c-u,K_0/U)\). If a base stratum is irreducible and the open fibre is nonempty,
the total incidence space is irreducible. This gives a genuine finite stratification, but not a component bound.

### II.6 Polynomial certificate

For \(P(\lambda)\) of rank \(\omega\) for every \(\lambda\), there is \(Y(\lambda)\) with \(\deg Y\le2\omega-2\)
and \(PYP=P\). The construction uses the maximal minors \(p_I\), the Bézout coefficients \(b_I\) with
\(\sum b_Ip_I=1\), \(\deg b_I<d\le\omega\) (the elementary lemma you indicated), and
\[
Y=\sum_I b_I\,\operatorname{adj}(\widehat{P_I}),
\]
with \(\deg\operatorname{adj}\le\omega-1\); hence \(\deg Y\le2\omega-2\). The constant-matrix identity
\(P(V_rU_l)P=P\) for \(P=UV\) is formalised.

### II.7 Formalisation

Standalone Lean kernels, compiled without `sorry`, `#print axioms` equal to
\([\text{propext},\text{Classical.choice},\text{Quot.sound}]\): the rank inequality, the lifting rank formula,
the explicit \(J_3(0)\) counterexample, the block criterion in rank and kernel form together with the pencil
splitting, the \(\operatorname{rank}Q\) formula, the kernel equivalence
\(\ker[P;Q]\cong\ker[v,Av]\) with the rank identity
\(\operatorname{rank}[P;Q]+(2-\operatorname{rank}[v,Av])=\delta\), and the constant-matrix certificate
identity. The paper form \(\operatorname{rank}[P;Q]=\delta-2+\operatorname{rank}[v,Av]\) needs \(\delta\ge2\);
for \(\delta<2\) the natural-number subtraction wraps, so we state the robust form.

### II.8 The blocked algorithm

For the \(c=2\) feasibility of \(q=\omega+1\), the plan is: enumerate the admissible \(V\), solve the lifting
system for \(L\), and test goodness. Two constructions failed:

1. choosing \(R\) from \(RN_K\) equal to the annihilator of \(V\) and \(R=MN_K^{+}\) gives the right kernel
   \(V=\ker H\) but violates \(\operatorname{rank}[C;L]=p+q\);
2. adding the homogeneous part of the lifting system restores neither \(\operatorname{rank}[C;L]=p+q\) nor,
   in general, \(\operatorname{rank}[L_0;R]=q\);
3. the existing mod-\(J\) candidate generator produces \((5a)\)-feasible \(L\)'s but its \(q\) is not the fixed
   \(q=\omega+1\).

We can parametrise the admissible layers and we have a good criterion, but we do not have a correct construction
of \(L\) from \((V,\text{lift})\) that satisfies all rank conditions simultaneously. This is the one point where
we need help.

## Part III. Questions

**Question 1 (the blocked algorithm).** Is there a standard construction of the lift \(L\), given the compressed
pair \((H,H_A)\), that satisfies \(\operatorname{rank}[L_0;R]=q\) *and* \(\operatorname{rank}[C;L]=p+q\)
simultaneously? We know the lifting lemma for \(\operatorname{rank}[L_0;R]\) (an affine symbolic-rank
condition), but the second condition involves \(C\) and is not part of that lemma. Is the right algorithm
instead to solve for \(L\) directly (for example, by eliminating \(R\) from the block conditions and then
checking \((5b)\) by a gcd), rather than to pass through \(V\)? A reference or a counterexample to this
decomposition would be very helpful.

**Question 2 (the good-locus criteria).** For \(t=2\) we use the block criterion: bad iff there is
\(0\ne y\in\ker B\) with \(Ay=\lambda y\), where the pencil descends to a \(q\times\omega\) block because
\(P\) vanishes on \(V\). For \(t<2\) the pencil does not descend, and we obtain a two-branch system
\[
x^{\mathsf T}(\lambda H_0-A_{11})=\alpha B_1,\qquad x^{\mathsf T}A_{12}=-\alpha B_2,
\]
with an eigenvector branch \(\alpha=0\) and an affine branch \(\alpha\ne0\). Is this the correct general form,
and is the affine branch really nonempty in \(c=2\)? Is there a standard name or reference for this "affine
eigenvalue" obstruction?

**Question 3 (general \(c\)).** Is the invariant-part bound \(p(c)n^c\) acceptable, and is the irreducibility of
the determinantal strata \(S_{t,u}\) known for general \(c\)? We would welcome references on determinantal
varieties, relative Grassmannians, and quiver Grassmannians (we have Caldero–Reineke in mind) that could
settle the \(t<c\) part.

**Question 4 (references).** We would be grateful for references on: (a) polynomial generalised inverses with
degree bounds (the Bézout/minor construction); (b) irreducibility of incidence varieties of the above type;
(c) the real analogue of the fibre theorem (open Grassmannian over \(\mathbb R\), nonemptiness criteria);
(d) the complexity of the \(\exists\Theta\) problem, or of closely related semialgebraic decision problems.

**Question 5 (next step).** Given the blocked \(c=2\) algorithm, should we (i) keep pushing the \(c=2\)
feasibility, (ii) move to \(c=3\) feasibility with the same decomposition, (iii) concentrate on the complexity
side (is \(c=2\) already hard, for example \(\exists\mathbb R\)-complete?), or (iv) something else? Which of
these is most likely to produce a substantial result?

**Question 6 (verification).** We now have the kernel equivalence and the rank identity formalised, and the
constant-matrix certificate identity. Would you recommend formalising the \(t=2\) block criterion for the
good locus, or is the paper proof sufficient at this stage? Do you see any statement-fidelity risk in the
two-branch formulation of Question 2 that we should check before formalising it?

**Question 7 (the rank identity).** Is the robust form
\(\operatorname{rank}[P;Q]+(2-\operatorname{rank}[v,Av])=\delta\) the right statement for the paper, or would
you present it differently (for instance with an explicit nonnegativity hypothesis and the paper form)?
