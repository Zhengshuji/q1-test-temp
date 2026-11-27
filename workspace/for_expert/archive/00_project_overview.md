# The MIN-ROWS / q1 project: problem, reduction chain, results, and open problems

This report is a self-contained overview of the project for a reader who has not seen the earlier
correspondence. It states the problem, the three reductions that organise the work, the results that are
established (with their verification status), the point where we are currently blocked, and a list of
questions.

## Part I. The problem and the standard form

### I.1 The problem

Given \(A\in\mathbb C^{n\times n}\), \(C\in\mathbb C^{p\times n}\) and \(L_0\in\mathbb C^{r\times n}\), one seeks
the smallest \(q\) and a matrix \(R\in\mathbb C^{(q-r)\times n}\) such that \(L=[L_0;R]\) has full row rank and

\[
(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\quad\forall\lambda .
\]

The question \(q1\) is whether computing the minimal \(q\) (and deciding whether a given \(q\) is feasible) is
NP-hard. The problem is equivalent to the order problem for minimal functional observers of Fernando, Trinh
and Jennings (IEEE TAC 2010).

### I.2 What the literature already settles

The characterisation is solved. Fernando (arXiv:2609.33615 and arXiv:2609.37992, 2026) gives the complete
order spectrum, necessary and sufficient conditions for each order, the equality "minimal order = minimal
spectrally feasible order", and a construction; the quantity \(q_0\) is polynomial-time computable. In the
notation of that work, the open target is the complexity of the existential problem \(\exists\Theta\)
(chart times semialgebraic condition). The present project does not attempt to reprove the characterisation;
it studies the structure and the complexity of this existential problem.

### I.3 Notation

\[
K_0=\ker[C;CA],\quad k=\dim K_0,\quad N_K\ \text{a basis},\quad
H=LN_K,\quad H_A=LAN_K,
\]
\[
\omega=\operatorname{rank}[H;H_A],\quad c=k-\omega,\quad P(\lambda)=\lambda H-H_A .
\]
For a candidate \(V=\ker H\in\operatorname{Gr}(c,K_0)\), put
\[
W=V\cap A^{-1}V,\qquad t=\dim W,\qquad U=W+A(W),
\]
and
\[
\Phi_V:V\longrightarrow\mathcal X/V,\qquad v\longmapsto Av+V,
\]
where \(\mathcal X=\mathbb C^n\) is the ambient space. Then \(\ker\Phi_V=W\) and \(\operatorname{rank}\Phi_V=c-t\).
The spectral condition is that the \(\omega\)-minors of \(P(\lambda)\) have constant gcd, or equivalently that
\(\operatorname{rank}P(\lambda)=\omega\) for every \(\lambda\).

## Part II. The reduction chain and the results

### II.1 From closed forms to layers

The project began by looking for a closed formula for \(q_{\min}\). Four such formulas were proposed and all
were refuted by explicit small counterexamples. The structural conclusion was that \(q_{\min}\) is not a
function of a few invariants, and that the feasible set must be treated as a union over the layer
\(\omega=\operatorname{rank}H\). This turned the strategy from "find a formula" into "fix a layer and study its
geometry". A crucial warning came from a concrete example: a layer can be entirely bad while the instance is
still feasible at a lower layer, so "bad layer" does not imply "infeasible order".

### II.2 First compression: \(R\mapsto(H,H_A)\)

Fixing \(\omega\), the rows of \(R\) are compressed into the two \(q\times k\) matrices \(H\) and \(H_A\). Then:

* \((5a)\) is equivalent to \(\ker H\subseteq\ker H_A\). Geometrically, \((5a)\) is a condition on the domain;
* \((5b)\) is the condition that \(\lambda H-H_A\) has rank \(\omega\) for all \(\lambda\).

The kernel inclusion lets one define the block map
\[
Z:W=\operatorname{im}H\longrightarrow\mathbb C^q,\qquad Z(Hx)=H_Ax,
\]
and, after splitting \(\mathbb C^q=W\oplus W'\), write \(Z=(A_W;B_\perp)\). The **block criterion** is
\[
\boxed{\operatorname{rank}P(\lambda)<\omega\iff\exists\,0\ne y\in\ker B_\perp\ \text{with}\ A_Wy=\lambda y.}
\]
In words: \((5a)\) is the domain condition, and \((5b)\) says that \(Z\) has no partial eigenvector on \(W\).

### II.3 Second compression: \((H,H_A)\mapsto Z\), closedness and gcd

On a fixed rank layer, the bad set is Zariski closed. The proof homogenises \(\lambda\) to \(\mathbb P^1\); at
infinity the matrix is \(H\), of rank exactly \(\omega\), so the projection from \(\mathbb P^1\) is proper. It
follows that on every irreducible component, either all points are bad or the good points are Zariski dense.
This reduces the pointwise search to a single gcd computation over the function field of the component.

### II.4 Third compression: the incidence space

The constrained case shows that the fibre dimension can jump: in a \(\mathbb P^1\) example, the open stratum is
entirely bad while an exceptional point is good. Hence one must work with the **lifted incidence space** that
contains the row space \(S\), the compatible pairs, the spanning conditions and the full-row-rank condition
together. Over a fixed layer this is a locally closed determinantal variety, stratified by finitely many rank
conditions. This is the current geometric framework. It is important that the strata are determinantal, not
linear: an earlier claim that the \(k=3\) rank layers are linear/irreducible was refuted by an explicit
example.

### II.5 The hyperplane case \(c=1\)

For \(k=\omega+1\), the base is \(\mathbb P(K_0)\); for \(v=N\sigma\), the constraints on \(R\) are linear,
\(Rv=0\) and \(RAv=0\). The rank \(\rho(v)=\operatorname{rank}[v,Av]\) is \(1\) exactly at eigenvectors of
\(A\), and the eigenvector locus is the union of the projective eigenspaces
\(\mathbb P(K_0\cap\ker(A-\lambda I))\). On the constant-\(\rho\) pieces the solution space of \(R\) is a vector
bundle, and the full-row-rank condition is open. Consequently the number of lifted components is at most
\(\delta+1\), where \(\delta=\dim\ker T\) with \(T(v,w)=v+Aw\); for \(\delta=2\) this gives at most three
components. Moreover
\[
\operatorname{rank}\begin{bmatrix}P\\Q\end{bmatrix}+(2-\operatorname{rank}[v,Av])=\delta,
\]
which is the robust form; the paper form \(\delta-2+\operatorname{rank}[v,Av]\) requires \(\delta\ge2\).
The rank of \(Q\) is \(\delta-1\) on \(v\in D_A=K_0\cap A^{-1}K_0\) and \(\delta\) otherwise.

### II.6 The exact fibre theorem

For \(V\in\operatorname{Gr}(c,K_0)\) and \(W=V\cap A^{-1}V\),
\[
\mathcal F_W=\{V\in\operatorname{Gr}(c,K_0):\ U\subseteq V,\ \operatorname{rank}\Phi_V=c-t\},
\]
and this is an open subset of \(\operatorname{Gr}(c-\dim U,K_0/U)\). The quotient is the ambient
\(\mathcal X/V\), not \(K_0/V\); the latter is valid only if \(A(K_0)\subseteq K_0\), which is not part of the
hypotheses. The proof is the identify \(\ker\Phi_V=V\cap A^{-1}V\).

### II.7 The admissible layers for \(c=2\) and \(c=3\)

For \(c=2\), the admissible locus has six mutually disjoint layers with exact parameter spaces:

1. \(t=2\), two distinct eigenvalues: pairs of eigenlines, modulo the swap;
2. \(t=2\), scalar: \(\operatorname{Gr}(2,E_\lambda\cap K_0)\);
3. \(t=2\), Jordan block: an eigenline satisfying the chain-lifting condition
   \(\ell\subseteq(A-\lambda I)(K_0)\), with an affine fibre of dimension \(\dim(E_\lambda\cap K_0)-1\);
4. \(t=1\), \(A(L)\subseteq L\): \(V=L\oplus\langle x\rangle\) with \(Ax\notin L+\langle x\rangle\);
5. \(t=1\), \(A(L)\not\subseteq L\): \(V=L+AL\), with the exact condition
   \(\operatorname{rank}[v,Av,A^2v]=3\);
6. \(t=0\): the open set \(V\cap A^{-1}V=0\).

For \(c=3\) there are eleven layers: six invariant types (three distinct eigenvalues; \(1+1+1\); \(1+1\) plus a
distinct eigenvalue; \(2+1\); \(2\) plus a distinct eigenvalue; \(3\), with two chain-lifting conditions), two
\(t=2\) types (\(\dim U=3\) with \(Ab\notin V\), and \(\dim U=2\) with \(Ax\notin W+\langle x\rangle\)), two
\(t=1\) types (\(A(L)\subseteq L\) with \(U'\cap\bar A^{-1}U'=0\), and \(A(L)\not\subseteq L\) with \(Ax+V\)
and \(A^2L+V\) independent), and the \(t=0\) open stratum.

### II.8 Component bounds

For \(c=2\), the layers above are irreducible parameter spaces (Grassmannians, projective spaces, projective
linear subspaces, affine fibres, finite quotients), which gives
\[
\#\{\text{components}\}\le\binom{s}{2}+3s+2,
\]
where \(s\) is the number of distinct eigenvalues of \(A\). The good locus is an open subset of each layer, so
it obeys the same bound. This turns the component-count part of the type-control conjecture into a theorem
for \(c=2\) (subject to a written irreducibility proof having been accepted).

For \(c=3\), the analogous count would be \(\binom{s}{3}+3s^2+6s+1\), but we have been advised that the
irreducibility of every one of the eleven strata must be checked separately; the \(c=3\) bound is therefore
currently suspended. The general invariant-part count \(p(c)n^c\) (where \(p(c)\) is the number of partitions
of \(c\)) bounds the number of possible Jordan-type labels, not the number of irreducible components; varieties
of invariant subspaces can be reducible (Springer fibres are the standard warning).

### II.9 General incidence theorems

For fixed \((t,u)\) with \(t\le u\le2t\), the condition \(\dim(W+A_0(W))=u\) defines a locally closed
determinantal stratum in \(\operatorname{Gr}(t,D)\), \(D=K_0\cap A^{-1}K_0\). Over such a stratum the admissible
\(V\)'s form an open subvariety of the relative Grassmannian \(\operatorname{Gr}(c-u,K_0/U)\). If the base is
irreducible and the open fibre is nonempty, the total space is irreducible. This gives a genuine finite
stratification but not a general component bound.

### II.10 The polynomial certificate

If \(P(\lambda)\) has rank \(\omega\) for every \(\lambda\), then there is a polynomial \(Y(\lambda)\) with
\(\deg Y\le2\omega-2\) and \(PYP=P\). The construction uses the maximal minors \(p_I\), their Bézout
coefficients \(b_I\) with \(\sum b_Ip_I=1\) and \(\deg b_I<d\le\omega\) (the elementary lemma: in
\(\mathbb C[\lambda]/(p_1)\), the other minors generate the unit ideal, so the coefficients can be chosen of
degree below \(\deg p_1\)), and the embedded adjugates:
\[
Y=\sum_I b_I\,\operatorname{adj}(\widehat{P_I}),
\qquad \deg Y\le(\omega-1)+(\omega-1)=2\omega-2.
\]
The identity \(P\,\operatorname{adj}(\widehat{P_I})\,P=\det(P_I)P\) is first checked over the rational
function field and then extended as a polynomial identity. This certificate is the basis of a membership
argument in \(\exists\mathbb R\); no hardness reduction is known.

### II.11 Formalisation

The following are standalone Lean kernels, compiled without `sorry`, with `#print axioms` equal to
\([\text{propext},\text{Classical.choice},\text{Quot.sound}]\):

* the rank inequality \(\dim U>\dim K-\omega\Rightarrow\operatorname{rank}f<\omega\);
* the lifting rank formula \(\operatorname{rank}[L_0;R]=r+\operatorname{rank}(\pi R)\);
* the explicit counterexample \(J_3(0)\), \(V=\langle e_1,e_2\rangle\);
* the block criterion in rank and kernel form, the pencil factorisation and the splitting
  \(\operatorname{rank}(\lambda U-G)=\operatorname{rank}(\lambda I-A_W,-B)\);
* the \(\operatorname{rank}Q\) formula;
* the kernel equivalence \(\ker[P;Q]\cong\ker[v,Av]\) with the robust rank identity;
* the constant-matrix certificate identity \(P(V_rU_l)P=P\) for \(P=UV\).

The paper form of the rank identity is kept as a corollary under \(\delta\ge2\). The Lean development is
evidence that the algebraic identities are stated correctly; it does not replace checking that the formal
statement is the intended mathematical statement.

## Part III. The current frontier, the blockage, and the questions

### III.1 The lift-completion problem

The compressed plane \(V=\ker H\) records the restriction of the rows of \(L\) to \(K_0\), but not their
components in the annihilator of \(K_0\). Those components are exactly where the independence condition
\(\operatorname{rank}[C;L]=p+q\) can be achieved or can fail. The exact sequence
\[
0\longrightarrow E_C=\frac{\operatorname{row}[C;CA]}{\operatorname{row}C}
\longrightarrow\frac{\mathcal X^*}{\operatorname{row}C}
\overset{\rho}{\longrightarrow}K_0^*\longrightarrow0
\]
makes the missing freedom explicit, with \(d_C=\operatorname{rank}[C;CA]-\operatorname{rank}C\). The
completion criterion is: if \(\operatorname{rank}[C;L_0]=p+r\), then the prescribed compressed rows can be
completed to rows satisfying \(\operatorname{rank}[C;L]=p+q\) if and only if \(q-\omega\le d_C\). For
\(q=\omega+1\) this reduces to \(d_C\ge1\).

We have found, however, that adding a row \(g\in\operatorname{row}[C;CA]\) to the bottom block changes
\(H_A\) unless \(gAN=0\): writing \(g=aC+bCA\) and using \(CAN=0\) (the columns of \(N\) lie in
\(K_0=\ker[C;CA]\)), one gets
\[
gAN=b\,CA^2N,
\]
which is not zero in general. Numerically, on the instances we tested, \(d_C=3\) and the map
\(g\mapsto gAN\) has rank \(1\) on the invisible space, so the dimension of the freedom that preserves the
compressed pair is
\[
d'_C=d_C-\operatorname{rank}(g\mapsto gAN)=2.
\]
Thus there are two different criteria: \(q-\omega\le d_C\) for the rank completion alone (after which
\((5b)\) must be rechecked), and \(q-\omega\le d'_C\) for a completion that preserves the compressed pair and
therefore the spectral problem. For \(q=\omega+1\), \(q-\omega=1\le d'_C=2\), so completion preserving the
pair is still possible; but the construction must use a basis of
\[
E'_C=\{g\in\operatorname{row}[C;CA]:\ gN=0,\ gAN=0\}/\operatorname{row}C,
\]
not of the full \(E_C\).

With this correction in hand, the \(c=2\) feasibility algorithm would be: enumerate the six admissible layers,
construct a compressed pair, complete the lift using \(E'_C\), and test \((5b)\) by the gcd criterion. We have
not yet succeeded in making this pipeline produce a feasible witness on our test instances; the immediate
diagnosis is that the \(V\)'s we tried are not \(A\)-invariant, so the admissibility condition
\(\ker H\subseteq\ker H_A\) is not automatic, and for \(t<2\) it must be imposed as a linear condition on the
off-\(K_0\) part of the lift.

### III.2 The universal block criterion

Because \((5a)\) is equivalent to \(\ker H\subseteq\ker H_A\), the pencil \(P(\lambda)\) vanishes on
\(V=\ker H\) for every admissible \(V\), not only for \(t=2\). Hence it descends to
\(\overline P(\lambda):K_0/V\to\mathbb C^q\), and in suitable bases
\[
\overline P(\lambda)=\begin{bmatrix}\lambda I_\omega-A_*\\-B_*\end{bmatrix},
\qquad
\operatorname{rank}P(\lambda)<\omega\iff\exists\,0\ne y:\ A_*y=\lambda y,\ B_*y=0.
\]
This is the block criterion in its general form. An earlier two-branch system (with an eigenvector branch
\(\alpha=0\) and an affine branch \(\alpha\ne0\)) was derived from a different elimination; we have withdrawn
it as a statement about the spectral condition, and it should only be reused if its equivalence to the
quotient-pencil criterion is proved.

### III.3 Questions for the readers

**Question 1 (framework).** Is the three-compression framework — \(R\mapsto(H,H_A)\mapsto Z\mapsto\) incidence
space — sound as the organising structure of the problem? Are there hidden assumptions (for instance on the
rank of \(C\), on \(\operatorname{rank}[C;L_0]\), or on the coefficient field) that should be stated at the
outset?

**Question 2 (lift completion).** Is the exact-sequence criterion the standard way to treat the completion
modulo \(C\)? Is our observation that \(gAN=b\,CA^2N\) (so that invisible directions can change \(H_A\))
correct, and is \(d'_C=d_C-\operatorname{rank}(g\mapsto gAN)\) the right dimension for the completion that
preserves the compressed pair? Is there a reference for this matrix-completion problem?

**Question 3 (the \(c=2\) algorithm).** With \(d'_C\ge1\), should the completion that preserves the compressed
pair always be possible for \(q=\omega+1\), and can the remaining parameters always be chosen to make the good
locus nonempty? Is the pipeline "enumerate the six layers, complete the lift, test the gcd" correct, or is
there a better algorithm (for example one that avoids enumerating \(V\) altogether)?

**Question 4 (the \(c=3\) strata).** Are the eleven \(c=3\) strata irreducible? The \(t=2,\dim U=3\) stratum
\(\{W\in\operatorname{Gr}(2,D):\dim(W+A_0(W))=3\}\) is a rank-exact determinantal locus, which is not
automatically irreducible. Which of the eleven need a separate argument, and are there known examples of
reducibility in this range?

**Question 5 (general \(c\)).** Is there a route to a general component bound, or is the honest statement only
the finite stratification plus the label count \(p(c)n^c\)? Would the quiver-Grassmannian language give
additional structure (for instance for the base strata \(S_{t,u}\))?

**Question 6 (complexity).** Does the bounded-degree certificate give a complete membership argument in
\(\exists\mathbb R\) under a suitable rational input model? Is there any evidence that the fixed-\(c=2\)
problem is already hard, or should one first look for a polynomial-time exact algorithm for \(c=2\)?

**Question 7 (references).** We would welcome references on: (a) degree bounds for polynomial generalised
inverses; (b) irreducibility of determinantal and incidence varieties; (c) real points of Grassmannians and
real algebraic feasibility; (d) the complexity of rank-constrained matrix problems in \(\exists\mathbb R\).

**Question 8 (next step).** Given the current state, is the best next step (i) the \(c=2\) feasibility
algorithm, (ii) the \(c=3\) stratum audit, (iii) the complexity side, or (iv) a consolidation of the
\(c=1\)/\(c=2\) structure theorems into a single statement? What would make the strongest contribution?

**Question 9 (verification).** Which of the paper statements would you consider most in need of independent
checking, and which would you advise not to formalise at this stage?
