# Report 101: The hyperplane layer — structure, a two-way decision procedure, and complexity

The two papers settle the characterization, the order spectrum, the minimum order and the construction.
This report is about the remaining question: the **complexity** of deciding, for given data, whether a
design of a given order exists. I restrict to the simplest nontrivial slice of that question — the
**hyperplane layer** — and report what is proved, what is computed, and what is still open.

Everything below is self-contained: the layers, the structure and the procedure are not in the papers.

---

## Part I. Setting

### I.1 Notation

I use the papers' symbols: $K_0=\ker[C;CA]$, $k=\dim K_0$, $N$ a basis of $K_0$,
$H=LN$, $H_A=LAN$, $\omega=\operatorname{rank}H$, $P(\lambda)=\lambda H-H_A$,
$S=\operatorname{row}(AN)$, $\ell=\operatorname{rank}(AN)=\dim(AK_0)$.
The data are rational; the spectral condition is quantified over $\lambda\in\mathbb C$.

The two conditions:
$$
(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \operatorname{rank}P(\lambda)=\omega\ \ \forall\lambda\in\mathbb C .
$$

$\mathcal L=[L_0;R]$ has $q$ rows; $V=\operatorname{row}\mathcal L$; and
$$\omega=\dim(V\cap K_0).$$

### I.2 The layer program

Write $c=k-\omega$ ("codimension"). The design problem decomposes as
$$\text{feasible}\iff\bigvee_{c}\ \bigl(\text{the }c\text{-th layer is nonempty}\bigr),$$
so a decision procedure can work layer by layer. **This report is about $c=1$** ($\omega=k-1$), the
first nontrivial layer. Two facts make it tractable:

* $\ker H$ is a **line**; write it as $\mathbb C v$ with $v\in K_0$. Every row of the free block
  annihilates $v$, so rows lie in $v^\perp$.
* Write $U=\operatorname{span}(v,Av)$. Then the admissible row spaces satisfy
  $V\subseteq U^\perp$ and $\dim(V\cap K_0)=k-1$.

Call $v$ **eigen** if $\dim U=1$ and **non-eigen** if $\dim U=2$.

---

## Part II. Results

### II.1 A local criterion, and the fact that components are not needed

**Theorem A.** Let $X$ be a piece of the parameter space on which $\operatorname{rank}H\equiv\omega$ and
$H,H_A$ are polynomial. Then the bad locus
$$\mathcal B=\{x\in X:\exists\lambda,\ \operatorname{rank}P_x(\lambda)<\omega\}$$
is closed in $X$; and if $X$ is irreducible,
$$X\text{ contains a feasible point}\iff \gcd_I m_I=1\ \text{ in }\ \overline{\mathbb Q(X)}[\lambda],$$
where $m_I$ are the $\omega\times\omega$ maximal minors.

*Proof.* Homogenise: $\det((sH-tH_A)_I)$ is homogeneous of degree $\omega$ and regular, so
$\mathcal D=\{(x,[s:t]):\text{all minors vanish}\}\subseteq X\times\mathbb P^1$ is closed. At $t=0$ the
matrix is $H$ with $\operatorname{rank}\omega$, so $\mathcal D$ misses $t=0$ and equals the affine
incidence. The projection $X\times\mathbb P^1\to X$ is proper (base change of $\mathbb P^1\to\mathrm{pt}$),
so $\mathcal B$ is closed. On irreducible $X$, $\mathcal B$ is proper or everything; the generic point
decides, and "no common root in the function field" is exactly $\gcd=1$. $\square$

**A refinement that matters for the algorithm.** The proof uses only (i) a **cover** of the parameter
space by pieces and (ii) irreducibility plus closedness **on each piece** — never maximality. So the
procedure does not need the decomposition into irreducible components (which is delicate for
Grassmannian strata); a finite cover by Grassmann charts suffices, each piece being a determinantal
(hence irreducible) subset of an affine chart. This observation removed a real gap in an earlier draft
of mine, where "components" were claimed.

### II.2 The non-eigen stratum for $p=1$

**Theorem B.** Let $p=1$, $q=n-2$, $r_0=0$. Then every admissible point of the hyperplane layer whose
kernel direction is non-eigen violates $(5b)$.

*Proof.* $r=\operatorname{rank}[C;CA]\le 2=p+1$, hence $n-2-p\le k-1=n-r-1$. Two cases.

(i) If $n-2-p<k-1$: each row of $C$ lies in $U^\perp$ and kills $K_0$ and $AK_0$, so the compressed
pencil $Q(\lambda I-A)N$ has $p$ identically zero rows and $\operatorname{rank}\widetilde M\le n-2-p<k-1$
for all $\lambda$.

(ii) If $n-2-p=k-1$: take a basis of $U^\perp$ whose first row is a row of $C$, and the basis
$[N_1\ v]$ of $K_0$. Then the first row and the last column of $Q(\lambda I-A)N$ vanish identically,
and the effective pencil is $\lambda X'-G'$ with $X'$ of full column rank (here $q=n-2$ forces
$V=U^\perp$, hence $\operatorname{rank}(QN)=k-1$). It is square, so $\det(\lambda X'-G')$ has degree
exactly $k-1\ge1$ and a complex root; there the rank drops. $\square$

The hypothesis $q=n-2$ is essential: it is what forces $V=U^\perp$ and hence puts the rows of $C$
inside the row space. (An earlier version of mine omitted it; the correction is due to the audit of
Report 97.)

### II.3 A zero-frequency identity

**Proposition C.** For any admissible row space $V$,
$$\boxed{\operatorname{rank}H_A=\dim(AK_0)-\dim(AK_0\cap V^\perp).}$$
Consequently:

1. $(5b)$ at $\lambda=0$ requires $\operatorname{rank}H_A=\omega$;
2. if $v\in AK_0$ then $\operatorname{rank}H_A\le\dim(AK_0)-1$, so feasibility requires
   $\dim(AK_0)\ge\omega+1$;
3. if $v$ is an eigenvector with eigenvalue $\lambda_0\ne0$, then $v=A(v/\lambda_0)\in AK_0$, so
   $$\dim(AK_0)\ge\omega+1=k.$$

*Proof.* $\operatorname{im}(AN)=AK_0$, so $\operatorname{rank}(LAN)=\dim L(AK_0)$; rank–nullity for
$L|_{AK_0}$ with $\ker L=V^\perp$ gives the identity. Each row of $\mathcal L$ annihilates $v$, so
$v\in V^\perp$; if also $v\in AK_0$ the intersection is nonzero. $\square$

In the papers' notation the last item is "$\ell\ge k$", which is a *necessary* condition for a
non-eigen-feasible design with nonzero eigenvalue — computable by one rank.

### II.4 The eigenvector criterion is not sufficient (a counterexample)

It is tempting to conjecture "the layer is feasible iff $K_0$ contains an eigenvector". That is false.

**Proposition D.** For $n=5$, $p=1$, $C=e_5^{\mathsf T}$ and
$$A=\begin{pmatrix}2&2&-1&0&0\\0&-2&1&0&1\\0&1&-2&0&-1\\0&0&0&0&2\\0&-1&2&0&-1\end{pmatrix},$$
$e_1$ is an eigenvector in $K_0$, yet the whole eigen fibre fails $(5b)$ at $\lambda=0$.

*Proof.* $K_0=\operatorname{span}\{e_1,w,e_4\}$ with $w=(0,2,1,0,0)$, and
$AK_0=\operatorname{span}\{(2,0,0,0,0),(3,-3,0,0,0)\}$, so $\dim(AK_0)=2=\omega$ and $e_1\in AK_0$.
Every admissible $V$ satisfies $V\subseteq e_1^\perp$, so $e_1\in V^\perp$; by Proposition C
$\operatorname{rank}H_A\le1<\omega$ at every point of the fibre. $\square$

### II.5 The admissible directions are finite (and algebraic)

**Proposition E.** Let $v\in K_0$ be non-eigen and admissible (i.e. some $V\subseteq v^\perp$ has
$\dim(V\cap K_0)=k-1$). Then
$$\operatorname{proj}_{K_0}(Av)\in\operatorname{span}(v),$$
i.e. $v$ is an eigenvector of the compression $M=(\pi|_{K_0})\circ A|_{K_0}$.

*Proof.* $V\cap K_0\subseteq K_0\cap U^\perp=\{u\in K_0:u\cdot v=u\cdot Av=0\}$, whose dimension is
$k-\operatorname{rank}\{\varphi_v,\varphi_{Av}\}$. This must be $\ge k-1$, so the two functionals are
dependent; as $\varphi_v\ne0$ and the form is nondegenerate on $K_0$, this means
$\operatorname{proj}_{K_0}(Av)\parallel v$. $\square$

**Consequence.** The layer is a **finite** union of fibres: one for each eigenvalue of the compression
(and each fibre is $\mathbb P^{r}$ with $r=\dim U^\perp-\omega$). The kernel direction is an *algebraic*
number in general, not rational — a point that my earlier sampling-based experiments systematically
missed, and which caused two retracted claims (see Part II.9).

### II.6 Left-factor form: badness as an incidence

**Proposition F.** Under $(5a)$ there is $S$ with $H_A=SH$, hence
$$P(\lambda)=(\lambda I-S)H,\qquad
\operatorname{rank}P(\lambda)=\omega-\dim\bigl(\operatorname{im}H\cap E_\lambda(S)\bigr),$$
where $E_\lambda(S)=\ker(\lambda I-S)$. Therefore
$$\text{bad}\iff \operatorname{im}H\ \text{meets an eigenline of } S .$$

*Proof.* $(5a)$ says each row of $H_A$ is a combination of rows of $H$, i.e. $H_A=SH$; then
$P(\lambda)=(\lambda I-S)H$ and rank–nullity on the restriction of $\lambda I-S$ to $\operatorname{im}H$
gives the formula. $\square$

This turns badness into an incidence condition between a fixed $(\omega)$-dimensional subspace and
finitely many lines — the same shape as the closedness argument of Theorem A.

### II.7 A two-way decision procedure, and three instances

Since the layer is a finite union of fibres (II.5), and each fibre is irreducible with the bad locus
closed, Theorem A gives:

$$\text{the layer is feasible}\iff \text{some fibre has } \gcd_I m_I=1
\text{ in } \overline{\mathbb Q(x)}[\lambda],$$

where $x$ runs over the fibre parameters ($r$ of them).

I implemented this — exact rational arithmetic only, no computer algebra system:

1. compute $K_0$, the compression $M$ and its characteristic polynomial;
2. factor it over $\mathbb Q$; for each irreducible factor build the number field
   $\mathbb Q[\mu]/(f)$;
3. compute an eigenvector $v$ over that field, and the fibre over $v$;
4. compute the $\omega\times\omega$ minors as polynomials in $\lambda$ with coefficients in the
   rational function field $K(x)$;
5. take the gcd over $K(x)[\lambda]$: degree $0$ means the fibre is generically good, positive degree
   means the fibre is **entirely** bad.

Instances ($n=8$, $p=2$, $q=4$, $\omega=3$, so $n-2-p=4>\omega$):

| instance | compression characteristic polynomial | result |
|---|---|---|
| 1 | $(x-1)(x^3+2x^2+4x+6)$ | **feasible** (both fibres good) |
| 2 | $x(x-1)(x^2-8)$ | **feasible** (the $x^2-8$ fibre is good) |
| 3 | $(x-1)(x^3+4x^2+2x-5)$ | **infeasible** (both fibres entirely bad) |

Instance 1 was independently certified by an explicit Bézout identity $\sum_i g_i f_i=1$ for the
maximal minors (an exact certificate, in the spirit of Paper I's Gram criterion), and instance 2 by a
direct computation in $\mathbb Q(\sqrt2)$.

**Instance 3 is, as far as I can tell, the first instance in the excess regime
($n-2-p>\omega$) that is proved infeasible.** In particular, "excess dimension implies feasibility"
is false; the structured family can lie entirely inside the bad locus even though the unrestricted
tall-pencil count says otherwise.

### II.8 Complexity

**Proposition G.** For fixed $p$, the decision of the hyperplane layer is polynomial time in $n$ and
in the input length.

*Sketch.* The fibre parameter count is
$$r=\dim\frac{U^\perp}{K_0\cap U^\perp}=(n-\dim U)-\omega ,$$
which equals $\rho-1$ for non-eigen $v$ and $\rho$ for eigen $v$, where $\rho=\operatorname{rank}[C;CA]$.
Since $\rho\le2p$, $r\le2p$ is **independent of $n$**. Each step of the procedure is polynomial
(linear algebra over $\mathbb Q$, factoring an integer polynomial, arithmetic in a number field of
degree $\le k$), and the last step — a gcd in $K(x)[\lambda]$ — is polynomial for a **fixed number of
variables**, which is what $r\le2p$ gives. $\square$

So the c=1 layer is decidable in polynomial time for fixed $p$; the difficulty of $q1$ is pushed to
the regime where $p$ grows with $n$ (then $r$ grows too, and the multivariate gcd becomes exponential).

### II.9 Corrections (my own, in order)

This material went through several retractions; I list them because they mark where the arguments are
delicate.

1. An earlier draft claimed the parameter space decomposes into irreducible **components** with a
   proof by fibre-dimension comparison. That argument is invalid (the fibre of a closure is not the
   closure of the fibres). The correct statement, sufficient for the criterion, is the finite
   irreducible **cover** of II.1.
2. The rank bound and Theorem B are valid only in the full-row-space pattern $q=n-2$
   (the rows of $C$ must lie in the row space).
3. "Excess dimension implies feasibility" was claimed, then refuted, then re-claimed with a bug, and
   only settled by instance 3 above. In between, two implementation bugs produced a false positive
   (zero coefficients left in a polynomial dictionary; and a rational $p/q$ converted to the field
   element $p+q\mu$ instead of $p/q$). Both were caught by cross-checking symbolic results against
   point evaluations.
4. The eigen direction ($v$ also an eigenvector of $A$) is not a slice: its fibre has $r=\rho$, one
   more parameter than the non-eigen case. The implementation now handles both.

### II.10 Formal verification

The following were checked in Lean 4 (Mathlib, `lake env lean`, exit code 0):

| statement | Lean name |
|---|---|
| $\operatorname{finrank}(\operatorname{range}g)=\operatorname{finrank}(\operatorname{range}(f\circ g))+\operatorname{finrank}(\operatorname{range}g\sqcap\ker f)$ | `propC_rank_identity` |
| nonzero intersection $\Rightarrow$ rank drops by at least one | `propC_consequence` |
| $v\ne0$ in both $\operatorname{range}g$ and $\ker f$ $\Rightarrow$ rank drops | `rank_drop_of_mem_common` |
| every element of an algebraically closed field is a square | `exists_sq_eq_of_isAlgClosed` |
| $a\ne0\Rightarrow\exists x,\ ax^2+bx+c=0$ over an algebraically closed field | `quadratic_has_root` |

The abstract rank identity is a generalization of an existing lemma of mine for endomorphisms; the
second and third are the algebraic core of Proposition C, the last two of Theorem B's root step.
The matrix bookkeeping ($\det(\lambda X-G)$ is such a quadratic) and the concrete instances are not
formalized.

---

## Part III. Questions

**Q1.** The two-way procedure rests on Proposition E: the admissible directions are the eigenvectors of
the compression. Is there a standard name or a known obstruction theory for this "compression eigenvector"
condition? It looks like the natural invariant for this layer, and I would like to know whether it is a
special case of something in the literature.

**Q2.** For instance 3 the bad locus covers the whole layer, and the mechanism is a fixed common factor
of the maximal minors (of $\lambda$-degree 3). Is there a structural description of when such a fixed
factor can occur — something like a "resonance" between $A$ and the compression?

**Q3.** My complexity statement (Proposition G) is polynomial for fixed $p$ and says nothing when $p$
grows. Is that the right boundary to report, or is there a formulation in the papers' language
(e.g. in terms of $\ell=\operatorname{rank}(AN)$ and $q_0$) under which the layer decision is
polynomial without fixing $p$?

**Q4.** Proposition F writes the pencil as $(\lambda I-S)H$ with $H_A=SH$. Is the resulting
"$\operatorname{im}H$ meets an eigenline of $S$" picture the same as the observability formulation
used in Paper I, or is it a genuinely different decomposition that might be easier to work with?

**Q5.** The counterexample of II.4 kills the eigenvector criterion. Is there a natural repair — e.g.
adding the zero-frequency rank condition of Proposition C as a hypothesis — that would make a clean
"sufficient" criterion for the layer? My computations suggest yes for the instances I have, but I have
no proof.

### Reliability

| Statement | Status |
|---|---|
| Theorem A (closedness, criterion, finite cover) | proved |
| Theorem B ($p=1$, $q=n-2$) | proved |
| Proposition C (rank identity) | proved, and the abstract form is Lean-checked |
| Proposition D (counterexample) | proved, and checked by exact computation |
| Proposition E (admissible directions) | proved |
| Proposition F (left-factor form) | proved, checked by exact computation |
| Decision procedure, instances 1–3 | exact computation; the underlying criterion is Theorem A |
| Proposition G (complexity) | proved modulo standard facts (polynomial factorization, multivariate gcd for fixed variable count) |
