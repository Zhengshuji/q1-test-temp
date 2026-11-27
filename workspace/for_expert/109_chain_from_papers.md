# From the three papers to the middle layer: what stands, what was withdrawn, what is open

This report re-organises a line of work that had become hard to follow. It starts from the three companion
papers, states exactly which of their results are used, then gives the layer-side work in **logical** order
rather than chronological order, and separates three things that were repeatedly confused in earlier drafts:
(i) statements with proof, (ii) statements verified only on instances, (iii) statements that turned out to be
false and are now withdrawn. Every withdrawal is listed with the counterexample that killed it.

---

## Part I. Problem, notation, and the anchors borrowed from the three papers

### I.1 The decision problem

\(A\in\mathbb Q^{n\times n}\), \(C\in\mathbb Q^{p\times n}\), \(L_0\in\mathbb Q^{r_0\times n}\) are given. One seeks
\(R\in\mathbb F^{m\times n}\) (with \(\mathcal L=[L_0;R]\)) such that

\[
(5a)\ \operatorname{rank}\begin{bmatrix}\mathcal LA\\\mathcal L\\CA\\C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}\mathcal L\\CA\\C\end{bmatrix},
\qquad
(5b)\ \operatorname{rank}\begin{bmatrix}\lambda\mathcal L-\mathcal LA\\CA\\C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}\mathcal L\\CA\\C\end{bmatrix}\ \ \forall\lambda\in\mathbb C .
\]

The question of interest is the computational complexity of deciding, for given \((A,C,L_0,q)\), whether such an
\(R\) with \(q=r_0+m\) rows exists — including the minimum-order form. Throughout, \(\mathbb F=\mathbb Q\) for the
instances and \(\mathbb F=\mathbb R\) for the decision problem as posed in the first paper.

### I.2 The compressed form (first paper)

\[
K_0=\ker[C;CA],\quad k=\dim K_0,\quad N:\mathbb Q^{k}\to K_0\ \text{a basis},\quad
H=LN,\quad H_A=LAN,\quad \omega=\operatorname{rank}H .
\]

Both conditions become brackets on the compressed rows:
\[
(5a)'\ \operatorname{row}H_A\subseteq\operatorname{row}H,
\qquad
(5b)'\ \operatorname{rank}(\lambda H-H_A)=\omega\ \ \forall\lambda\in\mathbb C .
\]
Because the two conditions involve the same free rows, the decision splits over the layer number:
\(\text{decision}=\bigvee_{\omega=0}^{k}(\text{layer }\omega\text{ feasible})\).

### I.3 The subspace form and two structural bounds (first paper; second paper)

Let \(V=\mathbb Q^{1\times k}\) be the space of compressed rows, and let
\[
\mathcal S=\operatorname{row}[N\ AN]\subseteq V\oplus V
\]
be the space of compressed row pairs \((rN,rAN)\). A design determines a subspace
\(\mathcal W\subseteq\mathcal S\) of realised pairs; the conditions become a row-space inclusion together with a
constant-rank condition on the pencil. The two bounds used below are
\[
\omega+1\le\dim\mathcal W\le 2\omega,\qquad \dim\mathcal W\le 2\ell,\quad \ell=\operatorname{rank}(AN).
\]
The second bound is the reason the decision is fixed-parameter tractable in \(\ell\) and, in particular, why the
search is not over \(n\)-dimensional data. The first paper also proves that the case of no free rows is decidable
in polynomial time, gives a finite algebraic certificate for the spectral condition (compressed by Cauchy–Binet
to a Gram matrix governed by \(\ell\)), and places the decision problem in the existential theory of the reals.

### I.4 The optimisation layer (second paper)

The minimum order is \(q_{\min}=r_0+t_{\min}\) where \(t_{\min}\) is the smallest quotient dimension of a feasible
subspace; feasible orders are monotone and saturate, so the threshold problem is a single decision instance; and
the spectral condition yields a lower bound that is independent of, and on an instance strictly stronger than, the
purely algebraic bound. Given a decision procedure the minimum is found in \(O(\log(\ell+2))\) calls, and a
minimum-order observer is recovered by lifting a basis.

### I.5 The hyperplane layer (third paper)

For the layer in which the compressed pencil has a one-dimensional kernel, the admissible kernel directions are
exactly the real eigenvectors of the orthogonal compression of the state matrix to the unobservable subspace,
restricted by the prescribed rows. The design family is a finite union of relative Grassmann bundles over strata of
projective eigenspaces, and a **full-rank leading-coefficient lemma** makes a single computation per chart decide
the whole chart rather than a generic point. A certified repeated-eigenvalue example shows that feasibility need not
be constant on a projective eigenspace.

### I.6 What is *not* taken from the papers

No hardness statement is taken from any of the three papers: the decision problem is only known to lie in
\(\exists\mathbb R\) and to be fixed-parameter tractable in \(\ell\). The complexity classification is open in all
three.

---

## Part II. The layer-side work

The purpose of this line is narrow: to understand, layer by layer, whether the decision problem has structure that
would either (a) put it in P, or (b) provide a foothold for a reduction. It has produced a criterion, a
parametrisation of the admissible row-pair spaces, and a list of failures. It has **not** produced a complexity
statement.

### II.1 Setting and the two maps

For \(\omega\)-dimensional \(W\subseteq V\) put
\[
\mathcal T_W=\mathcal S\cap(W\oplus W),\qquad
\pi_1,\pi_2:\mathcal T_W\to W,\qquad
E_\lambda(x,y)=\lambda x-y .
\]
Fixed rows give \(V_0=\operatorname{span}\{(L_0)_iN\}\), and the compatible loci are
\(\{W:U\subseteq W\}\cong\operatorname{Gr}(\omega-d,k-d)\) with
\(U=\operatorname{span}\{(L_0)_iN,(L_0)_iAN\}\), \(d=\dim U\).

Two standing facts. First, the **kernel lemma**, in its correct form: it is \((5a)'\) **together with** \((5b)'\) that forces
\(\ker H=\ker H_A\). Row inclusion alone gives only \(\ker H\subseteq\ker H_A\) (take \(H=(1\ 0)\), \(H_A=(0\ 0)\));
the missing step is \(\lambda=0\) in \((5b)'\), which gives \(\operatorname{rank}H_A=\omega=\operatorname{rank}H\) and hence equal row spaces. Second, **fibrewise
rigidity**: in a fibre the feasible set is Zariski open, so no polynomial condition beyond the fibre can be imposed
on the free rows. (The correct phrasing, after a correction: fixing \(W\), the allowed free pairs form
\(\mathcal T_W\), the choices meeting the rank requirement form an open subset, and when \(m\ge\dim\mathcal T_W\)
the existence of such a choice is equivalent to the two conditions below.)

### II.2 Criterion for a fixed row space

> **Proposition (fixed \(W\); \(m\ge\dim\mathcal T_W\)).** Layer \(\omega\) is feasible on the fibre of \(W\) if and
> only if
> \[
> \textbf{(R)}\ \operatorname{span}\bigl(V_0\cup\pi_1(\mathcal T_W)\bigr)=W,
> \qquad
> \textbf{(E)}\ E_\lambda(\mathcal T_W)=W\ \ \forall\lambda\in\mathbb C .
> \]

Necessity: \(\operatorname{rank}H=\omega\) forces the first components of the fixed and free rows to span \(W\),
which is (R); the rows of the pencil are the evaluations of pairs in \(\mathcal T_W\), so rank \(\omega\) for all
\(\lambda\) forces (E). Sufficiency: take a basis of \(\mathcal T_W\) as the free rows; (R) gives
\(\operatorname{rank}H=\omega\), (E) gives rank \(\omega\) for the pencil at every \(\lambda\). This requires
\(m\ge\dim\mathcal T_W\); the version valid for an arbitrary row budget is stated in II.2b.

Two remarks that were learned the hard way and that the report is meant to make explicit.

1. (E) **cannot** be weakened to a projection condition. An earlier draft of this line claimed
   \((E)\iff\pi_2(\mathcal T_W)=W\) through the identity \(E_\lambda=\lambda\pi_1+\pi_2\). That identity is false:
   \(E_\lambda\) is a single linear map and its image is
   \(\{(\lambda x-y):(x,y)\in\mathcal T_W\}\), while the Minkowski sum of the two projections would require
   \((x,0)\) and \((0,y)\) to be present separately. The two coordinates are coupled by the common \(r\). The error is
   visible at once on the hyperplane layer: for the graph \(\mathcal T_W=\{(r,Ar):r\in W\}\) one has
   \(\pi_\lambda(\mathcal T_W)=(\lambda I-A)W\), which drops rank exactly at the eigenvalues of \(A|_W\). A scan on a
   concrete instance confirms the drop.
2. (E) **cannot** be dropped in favour of (R). The case \(\mathcal T_W=\{0\}\oplus W\) satisfies a projection-type
   condition while \(\pi_1=0\), so rank completion fails.

### II.2b Row budget: the criterion for arbitrary \(m\)

With \(\mathcal W_0=\operatorname{row}[L_0N\ L_0AN]\), the hypothesis-free form is

> **Theorem.** For fixed \(W\) and a budget of \(m\) free rows, the layer is feasible if and only if there is a subspace
> \(\mathcal U\) with
> \[ \mathcal W_0\subseteq\mathcal U\subseteq\mathcal T_W,\qquad \dim(\mathcal U/\mathcal W_0)\le m,\qquad
> \operatorname{span}(V_0\cup\pi_1(\mathcal U))=W,\qquad \pi_\lambda(\mathcal U)=W\ \ \forall\lambda . \]

Necessity: take \(\mathcal U\) to be the span of all row pairs of the design. Sufficiency: take a basis of
\(\mathcal U\) adapted to \(\mathcal W_0\), realise the \(\dim(\mathcal U/\mathcal W_0)\) basis elements outside
\(\mathcal W_0\) as free rows (every element of \(\mathcal S\) is \((rN,rAN)\) for some row \(r\)), and pad with zero
rows; the row space of \(H\) is then \(\operatorname{span}\pi_1(\mathcal U)\) and the pencil's row space is
\(\pi_\lambda(\mathcal U)\). Row-count exactness: the construction needs exactly
\(\dim(\mathcal U/\mathcal W_0)\) free rows, so
\[ q_{\min}=r_0+\min\{\dim(\mathcal U/\mathcal W_0)\}. \]
The criterion of II.2 is the case \(m\ge\dim(\mathcal T_W/\mathcal W_0)\) with \(\mathcal U=\mathcal T_W\).

### II.3 Parametrising the admissible row-pair spaces (the \(D_I\) construction)

Let \(\bar V=V/U\), \(b=k-d\), \(a=\omega-d\), \(\bar\pi:V\to\bar V\), and \(\bar{\mathcal S}=(\bar\pi\oplus\bar\pi)(\mathcal S)\)
with a rational basis \(B_0\). On the standard chart \(W_X/U=\operatorname{row}[I_a\ X]\), \(X\in\mathbb A^{a(b-a)}\),
put
\[
C(X)=\begin{pmatrix}-X&I_{b-a}&0&0\\0&0&-X&I_{b-a}\end{pmatrix},\qquad D_I(X)=C(X)\,B_0 .
\]
Equivalently, column \(j\) of \(D_I(X)\) is \(\bigl(E_X(x_j),E_X(Ax_j)\bigr)\) with \(E_X(v)=v^{(J)}-Xv^{(I)}\).

> **Proposition.** There is an exact sequence
> \[
> 0\longrightarrow \mathcal S\cap(U\oplus U)\longrightarrow \mathcal T_{W_X}\longrightarrow\ker D_I(X)\longrightarrow 0,
> \]
> hence \(\dim\mathcal T_{W_X}=\dim\ker D_I(X)+\dim\bigl(\mathcal S\cap(U\oplus U)\bigr)\), and the rank strata of
> \(\mathcal T_{W_X}\) over the chart are the strata of \(\operatorname{rank}D_I(X)\), i.e. the zero loci of its minors.

The fixed part \(\mathcal S\cap(U\oplus U)\) is the only piece not captured by \(D_I\); on the smallest model it is
zero and the formula is checked by hand.

### II.4 Three levels that must be kept apart

| object | parameter space | why it matters |
|---|---|---|
| a standard Grassmann chart \(W_X/U=\operatorname{row}[I_a\ X]\) | a **rational affine space** | rational and real points are Zariski dense, so a generic-rank test is legitimate here |
| the generic rank stratum of \(D_I\) | a non-empty **Zariski open** subset of the chart | generic-rank test legitimate, and it is open |
| a special (lower) rank stratum | a **locally closed** set, possibly reducible | density of real points is **not** automatic; this is where the difficulty sits |

Two crisp warnings, both learned from counterexamples.

* Generic-rank reasoning does **not** cover all strata. On the smallest model \(k=2,\omega=1,U=0\) with
  \(N=I_2\), \(A=\operatorname{diag}(1,2)\), the chart gives
  \(D_I(X)=\begin{pmatrix}-X&1\\-X&2\end{pmatrix}\), \(\det D_I=-X\). At \(X=0\) the kernel is one-dimensional and the
  layer is feasible; at \(X\ne0\) the kernel vanishes and it is not. So feasibility sits on the special stratum, and a
  single generic test would report "infeasible".
* Determinantal real-density does **not** pass to linear preimages: \(\Phi(x,y)=\begin{pmatrix}x&-y\\y&x\end{pmatrix}\)
  is linear, \(\det\Phi=x^2+y^2\), and \(\Phi^{-1}(\{\operatorname{rank}\le1\})=V(x^2+y^2)\) has just one real point.
  Hence "the rank strata are linear preimages of determinantal varieties, and those are real-dense" is not an
  argument.

The correct statement is therefore conditional: on any irreducible parameter stratum whose real (or rational) points
are Zariski dense, the generic-rank test decides the stratum; on the remaining strata one must either prove density
or do real algebraic feasibility directly. Which of the two applies is open for the specific \(D_I\).

### II.5 Direction admissibility is not feasibility

On the hyperplane layer one gets a clean statement: with \(M(\ell)=\begin{pmatrix}\ell\\ \ell A\end{pmatrix}\),
\[
\operatorname{rank}M(\ell)\le 1\iff \ell A=\mu\ell\ \text{for some }\mu\iff \ell\ \text{is a left eigenvector of }A,
\]
and then \(W=\ker\ell\) is automatically \(A\)-invariant. This is exactly the direction-admissibility statement of
the third paper, and it is **not** the feasibility statement: the spectral condition of II.2 is an additional,
independent requirement. A first attempt to read a real/complex mismatch off the eigenvector condition alone failed
precisely here — the candidate complex direction failed the pencil rank condition at \(\lambda=i\), and the real
direction failed it as well.

Two things are worth keeping from that attempt: the eigenvector characterisation of admissible directions (a
restatement of the third paper's principle in the language of II.2), and the observation that a real-versus-complex
gap would have to be produced inside the spectral condition, not before it.

### II.6 What has been withdrawn

| withdrawn statement | counterexample |
|---|---|
| "every middle layer is infeasible" | a rational instance on the hyperplane layer is feasible, so the claim is false |
| "the criterion is \(\mathcal T_W=W\oplus W\), i.e. \(\dim=2\omega\)" | a subspace of dimension \(2\omega-1\) can satisfy the spectral condition: \(\mathcal T=\ker(\alpha+\beta)\) with \(\alpha\notin\operatorname{span}\beta\) |
| "the feasible set is open, so one generic point decides" | feasible points can lie on coordinate charts that a fixed generic point does not represent |
| "\(\operatorname{rank}M(q)=2\) for every \(q\ne0\), so rank stratification is vacuous" | \(N=I_2\), \(A=I_2\) gives rank one everywhere |
| "\(\mathbb Q\)-irreducibility implies rational points are Zariski dense" | \(V(x^2+y^2)\) is \(\mathbb Q\)-irreducible with a single rational point |
| "determinantal real-density passes to linear preimages" | the rotation map above |
| "\((E)\iff\pi_2(\mathcal T_W)=W\)" | the pencil rank drops at the eigenvalues of \(A|_W\), as in II.2 |
| "the layer is complex-feasible and real-infeasible, therefore A2 is unavoidable" | the same instance fails the spectral condition on both sides |

The pattern behind most of these: treating a coupled object as if it were a product. The image of \(E_\lambda\) is not
a sum of two projections; the rank of \(D_I\) is not constant; a linear preimage does not preserve density; a
\(\mathbb Q\)-irreducible set need not have dense rational points.

### II.7 Where the two open items stand

**(A) Real feasibility on special strata.** The generic-rank test is available on charts and on open strata. On
special strata it is not, unless density is proved for the specific \(D_I\). Nothing in the present line proves
density, and one instance in which it fails is exhibited in the literature (the rotation map). This item is open.

**(B) Complexity.** The number of charts is \(\binom{b}{a}\) with \(a=\omega-d\), \(b=k-d\), and by the second
bound of I.3 this is bounded by \(n^{O(\ell)}\) — a **counting** estimate. To obtain an end-to-end complexity
statement one must add: the number of strata and of \(\mathbb Q\)-branches, the cost of the kernel parametrisation on
each stratum, the real feasibility step of (A), and the bit-length growth of the rational functions. None of this is
done. In particular the chartwise route does not, at present, improve on the fixed-parameter bound of the first
paper, and the two should not be confused.

---

## Part III. Questions

**Q1.** On each fixed rank stratum, what is the correct way to carry the spectral condition of II.2 into the
parametrised form? Writing \(Z_{Q,P}(X)=\begin{pmatrix}-D_{Q,P}(X)^{-1}D_{Q,P^{c}}(X)\\ I\end{pmatrix}\) for a basis
of \(\ker D_I(X)\) on the subchart where the minor \(\Delta=\det D_{Q,P}\neq0\), condition (R) becomes a rank
condition on a block of \(Z_{Q,P}\). The spectral condition is a maximal-minor gcd condition on
\(\pi_\lambda|_{\ker D_I(X)}\), which is a pencil in \((\lambda,X)\); is the right move to compute that gcd over
\(\mathbb Q(X)[\lambda]\), and does the leading-coefficient obstruction (the one handled by the third paper's lemma)
reappear here?

**Q2.** Is the real-feasibility step (A) avoidable for this specific \(D_I\), given that its two rows are the same
functional \(\ell\) applied to \(N\) and to \(AN\)? The \(2\times2\) minors are then quadratic forms in \(\ell\) of
the form \(\ell^{\mathsf T}\bigl(N_i(AN_j)^{\mathsf T}-N_j(AN_i)^{\mathsf T}\bigr)\ell\), i.e. Plücker coordinates
of the row space, whose relations hold identically and therefore do not by themselves exclude a definite form. What
extra structure of \(A,N\) would have to be used?

**Q3.** Is a real-versus-complex mismatch possible at the **decision** level, i.e. an instance where some complex
design satisfies both conditions for some layer while no real design does for any layer? If this is known to be
impossible for this class, the real-feasibility step would collapse; if it is possible, an example would settle the
question that II.7(A) leaves open.

**Q4.** For the reduction side: the two conditions are (i) a span equality and (ii) a pencil rank condition that
must hold for all \(\lambda\). Is there a known hard problem of the form "does there exist a subspace \(U\) of
prescribed dimension such that a given pencil restricted to \(U\) has constant rank"? We are aware that 0–1 linear
feasibility is the wrong target (it is NP-hard rather than a natural \(\exists\mathbb R\)-hard problem), and that a
constraint on subspace configurations looks closer to the shape here, but we have not found a reduction.

**Q5.** Is any step of Part II silently assuming something? In particular: the exact sequence of II.3 uses the
quotient by \(U\); the criterion of II.2 uses \(m\ge\dim\mathcal T_W\); and the three-level picture of II.4 uses the
rationality of the chart. We would rather have these checked than add further instances.

### Status of the statements in this report

| statement | status |
|---|---|
| kernel lemma; fibrewise rigidity; compatibility loci | proved |
| bounds \(\omega+1\le\dim\mathcal W\le2\omega\), \(\dim\mathcal W\le2\ell\); FPT in \(\ell\); \(\exists\mathbb R\) | from the three papers |
| criterion of II.2 — (R) together with the full spectral condition | proved (and corrected; see II.2) |
| exact sequence of II.3 and the dimension formula | proved, with the fixed part explicitly present; checked on the smallest model |
| three-level picture of II.4 | straightforward, but the two warnings are essential to it |
| eigenvector characterisation in II.5 | proved; it is direction admissibility, not feasibility |
| real feasibility on special strata (II.7 A) | **open** |
| end-to-end complexity (II.7 B) | **open**; only a chart-count estimate exists |
| hardness of the decision problem | **open**; no reduction |
