# Report 108: the layer c = 2 — fibre, base, decidability, a non-monotonicity counterexample, and the Lean-checked core

This report continues the layer program from c = 1 to c = 2. It states the results, marks what is
verified and how, records two corrections, and asks for a check of the c = 2 package.

Self-contained. The c = 1 paper is referred to as the hyperplane paper; the compressed-pair
formulation as the pair formulation.

---

## Part I. Setting

$K_0=\ker[C;CA]$, $k=\dim K_0$, $N$ a basis, $H=LN$, $H_A=LAN$ for a $q$-row design $\mathcal L$
with row space $V$ of dimension $q$, and

$$(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \rank(\lambda H-H_A)=\omega:=\rank H\ \ \forall\lambda .$$

Two layer parameters, kept distinct throughout:

$$\boxed{\ c:=k-\rho\ \ (\rho=\rank H=\dim\pi_{K_0}(V)),\qquad t:=q-\rho\ }$$

so $q=\rho+t$ and $t=q-k+c$. The direction space is $D:=\ker H=K_0\cap V^\perp$ of dimension $c$.

The hypothesis used below is the dimension condition $\dim(V\cap K_0)=\rho$, equivalently $V$ split
with respect to $X=K_0\oplus K_0^\perp$; call such a design **$K_0$-split**. It is not a consequence
of $(5a)$, and the counterexample in II.1 shows this.

---

## Part II. Results

### II.1 The fibre at a fixed direction (both problems)

**(a) Unrestricted problem.** With $U_D:=D+AD$,

$$\mathcal F_D=\big\{V\in\operatorname{Gr}(q,U_D^\perp):\ V_0\subseteq V,\ K_0\cap V^\perp=D\big\}.$$

The containment $V\subseteq U_D^\perp$ gives only $D\subseteq K_0\cap V^\perp$; *exactness*
$K_0\cap V^\perp=D$ holds iff

$$\boxed{K_0\cap(D+AD)=D},$$

which is necessary by $(5a)$ (as $D+AD\subseteq V^\perp$) and sufficient together with $V_0\subseteq U_D^\perp$
and $\dim(D+AD)\le n-q$.

**(b) $K_0$-split problem.** If $V$ is $K_0$-split and $M(D)\subseteq D$ with $A_{21}=\pi_{K_0^\perp}A|_{K_0}$,
then

$$V\cap K_0=D^{\perp_{K_0}},\qquad V=D^{\perp_{K_0}}\oplus W,\qquad W\subseteq T_D:=K_0^\perp\cap(A_{21}D)^\perp,$$

$$\boxed{\ \mathcal F_D^{\rm split}\cong\operatorname{Gr}\bigl(t-w_0,\ T_D/W_0\bigr)\ },\qquad
\dim T_D=(n-k)-r(D),\quad r(D)=\rank(A_{21}|_D),$$

with $w_0=\dim W_0$, $W_0=P_{K_0^\perp}(V_0)$; the fibre is nonempty iff $w_0\le t\le(n-k)-r(D)$ and its
dimension is $(t-w_0)\bigl((n-k)-r(D)-t\bigr)$.

*Proof of (b).* (i) $V\cap K_0=(V^\perp\cap K_0)^\perp$ inside $K_0$ equals $D^{\perp_{K_0}}$.
(ii) for $d\in D$: $\langle d,V\rangle=\langle d,D^{\perp_{K_0}}\rangle+\langle d,W\rangle=0$ as both are
orthogonal to $D$; and $\langle Ad,V\rangle=\langle Md,V\rangle+\langle A_{21}d,V\rangle=\langle A_{21}d,W\rangle$
since $Md\in D$; so $V\perp AD\iff W\subseteq(A_{21}D)^\perp$.
(iii) $V_0\subseteq V$ splits into $P_{K_0}(V_0)\subseteq D^{\perp_{K_0}}$ and $W_0\subseteq W$.
(iv) dimension: $\dim T_D=(n-k)-r(D)$ and $\operatorname{Gr}(t-w_0,(n-k)-r-w_0)$ has dimension
$(t-w_0)\bigl((n-k)-r(D)-t\bigr)$. $\square$

**Verified in Lean.** The two set/dimension assertions of (b) — namely $V\cap K_0=K_0\cap D^\perp$ for
$V=(K_0\cap D^\perp)\sqcup W$ with $W\le K_0^\perp$, and $\dim V=\dim(K_0\cap D^\perp)+\dim W$ — are
formalized (three lemmas) and pass an axiom audit whose only axioms are `propext`, `Classical.choice`,
`Quot.sound`. The implication in (ii) and the exactness condition in (a) are not formalized.

### II.2 The base: invariant two-planes

Let $\mathcal I_2(M)=\{D\in\operatorname{Gr}(2,K_0):M(D)\subseteq D\}$. Writing the real
primary/Jordan decomposition $K_0=\bigoplus_\lambda K_\lambda\oplus\bigoplus_{\{\mu,\bar\mu\}}K_\mu$, the
$M$-invariant two-planes are:

1. inside one primary block: for a semisimple block with $\dim K_\lambda=d_\lambda\ge3$, the whole
   $\operatorname{Gr}(2,K_\lambda)$ (dimension $2(d_\lambda-2)$); for a Jordan block only the first two
   vectors of a chain (isolated);
2. between two blocks: $\mathbb P(K_\lambda)\times\mathbb P(K_\mu)$, dimension $(d_\lambda-1)+(d_\mu-1)$;
3. a conjugate pair: **one** isolated real two-plane, provided its complex eigenspace is one-dimensional;
   if the irreducible quadratic has multiplicity $>1$ the corresponding real two-planes form a
   positive-dimensional family.

So the base is positive-dimensional exactly in the repeated-eigenvalue (or repeated-irreducible) case;
Jordan blocks and simple conjugate pairs contribute isolated points only.

**Consequence.** If all eigenvalues of $M$ are simple (over $\mathbb C$), $\mathcal I_2(M)$ is a finite
set of $\binom{k_{\mathbb R}}{2}+\#\{\text{conjugate pairs}\}$ points, and the $K_0$-split $c=2$ decision
reduces to finitely many Grassmannian fibres, each decided by one function-field gcd test; no base
charts are needed.

### II.3 Total charts and the algorithm (c = 2, $K_0$-split)

Let $\mathcal C$ be a component of $\mathcal I_2(M)$ on which $r(D)\equiv r$. Then:

1. the admissible designs over $\mathcal C$ form a relative Grassmann bundle with fibre
   $\operatorname{Gr}(t-w_0,T_D/W_0)$;
2. it is covered by finitely many affine charts, each a product of a chart of $\mathcal C$, a chart
   trivializing $D\mapsto(D^{\perp_{K_0}},T_D)$ (pivot minors), and a Grassmann chart of the fibre;
3. on each chart the rows of $L$ are rational in the chart coordinates and, after clearing denominators,
   the pencil is polynomial;
4. refining to a chart where a fixed $\omega$-minor of $H$ is nonzero gives $\rank H\equiv\omega$, so the
   full-rank leading-coefficient lemma applies and one gcd decides the whole chart.

The algorithm enumerates $c$, the components of $\mathcal I_c(M)$, the rank strata of $A_{21}|_D$, and
the charts; it answers *feasible* on the first chart whose gcd is constant, answers *infeasible* only
when every chart of every layer piece is positive-degree, and otherwise reports *undecided*.

**A methodological remark.** Within one rank stratum the gcd **degree** is not constant (values 1 and 2
both occur in the experiments below), but its **positivity** was; the method only needs positivity, since
the full-rank lemma converts "positive degree at the generic point of the chart" into "every point of the
chart is bad". Requiring a constant degree would be a needless extra condition.

### II.4 A counterexample to monotonicity in the layer index

On one instance ($n=8$, $p=2$, $k=4$, $M=\operatorname{diag}(1,1,2,3)$) at **one and the same order**
$q=3$ — the only order at which both $c=1$ and $c=2$ can occur, since $c-t=k-q$ —

- **the $c=2$ layer is feasible**: with $D=\operatorname{span}\{e_1+e_2,e_3\}$ and
  $W=(0,0,1,1,0,0,0,0)\subseteq K_0^\perp$, the design $V=D^{\perp_{K_0}}\oplus W$ has $\dim V=3$,
  $\omega=2$, satisfies $(5a)$ and the exactness condition, and has all six $2\times2$ maximal minors of
  $\lambda H-H_A$ coprime (gcd of degree 0);
- **the $c=1$ layer is infeasible**: the invariant lines are the lines of the eigenspace $E_1$ (dimension
  2) together with $e_3$ and $e_4$; parametrizing the first family by $D=\operatorname{span}\{e_1+s e_2\}$,
  one has
  $$H=\begin{pmatrix}-s&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
  \operatorname{rank}H=3,$$
  and the gcd of the two nonzero $3\times3$ maximal minors of $\lambda H-H_A$ equals
  $(\lambda-1)(\lambda-2)(\lambda-3)$, **independent of $s$**; the two points $e_3,e_4$ are bad as well.

So feasible designs need not exist at the smaller layer index: the layer index is **not monotone** at
fixed order, and in the direction "larger $c$ is easier".

### II.5 One uniform statement, and why charts cannot decide it at once

$K_0$-split $c$-layer feasibility is the single formula

$$\exists D\in\mathcal I_c(M)\ \exists W\subseteq T_D\ (\dim W=t,\ W_0\subseteq W):\
\rank(\lambda H-H_A)=\omega\ \ \forall\lambda,$$

i.e. $\exists c\,\exists D\,\exists W\,\forall\lambda$ — a specialization of the chart-times-semialgebraic
formulation of the literature. Enumerating $c$ and the components of $\mathcal I_c(M)$ is polynomial, but
the per-chart cost is exponential in the number of chart variables,
$c(d_\lambda-c)+(t-w_0)((n-k)-r-t)=\Theta(n^2)$ in the worst case; hence the chart route gives
$n^{O(c^2)}$, polynomial for fixed $c$ but not uniformly.

### II.6 Dictionary with the compressed-pair formulation

With $W=\operatorname{row}(V\mathsf M)$ and $\pi_1,\pi_2$ the two $k$-parts of $\mathsf M=[N\ AN]$:

$$U:=\pi_1(W)=\operatorname{row}(VN),\qquad D=\ker H=U^{\perp_{K_0}},\qquad c=k-\dim U,$$

and $(5a)$ is exactly $\pi_2(W)\subseteq\pi_1(W)$, while $M(D)\subseteq D$ is $M^*$-invariance of $U$.
Thus the layer index is the codimension of the common projection, and the layer decomposition is a
partition of one and the same family by $\dim U$; the parameters do not disappear by changing language.

---

## Part III. Corrections recorded

1. **A notational overloading.** The dimension of $T_D$ must be written with $n-k$, not with
   $\rank H$: these coincide only when $n-k=\rank H$. Formulae stated earlier with "$\rho-r(D)$" were
   re-derived as "$\rho_{\rm amb}-r(D)$" with $\rho_{\rm amb}=n-k$ and checked numerically on two
   instances. This is a notation accident, not a change of mathematics.
2. **The conjugate-pair count.** "One isolated real two-plane per conjugate pair" needs the complex
   eigenspace to be one-dimensional; repeated irreducible quadratics give a positive-dimensional family.
   The earlier statement was too broad and is now qualified.
3. **An earlier error, already corrected.** In the previous report the fixed-direction fibre was written
   with $D\subseteq V$, which contradicts $D\perp V$. The corrected formulae are II.1(a) and II.1(b); the
   present report restates them so that the record is self-contained.

---

## Part IV. Requests

**Q1 (fibre).** Is II.1 correct as stated, in particular (i) the exactness condition
$K_0\cap(D+AD)=D$ for the unrestricted problem and (ii) the decomposition (b) with
$V\cap K_0=D^{\perp_{K_0}}$ and $W\subseteq T_D$? The set/dimension part of (b) is Lean-checked; the
equivalence in II.1(b)(ii) and the exactness in II.1(a) are paper only.

**Q2 (base).** Is the base description of II.2 correct and complete, in particular the treatment of
Jordan blocks (isolated only) and the multiplicity caveat for conjugate pairs? Is there a standard
reference for the dimension of the variety of real invariant two-planes in the repeated case?

**Q3 (the counterexample).** II.4 claims non-monotonicity in the layer index at fixed order. On the
$c=1$ side the argument uses the dimension hypothesis ($K_0$-split) and the direction theorem, then a
symbolic gcd over the whole projective family; on the $c=2$ side it exhibits one admissible design. Does
this establish the claim, or is some part of the $c=1$ layer left uncovered by the parametrization?

**Q4 (degrees versus positivity).** Is the remark of II.3 sound — that a chartwise decision needs only the
positivity of the gcd degree, never its value? Is there a structural reason why the degree varies (1 and
2) inside a single rank stratum with fixed direction?

**Q5 (direction).** Given II.4, the "only small layers matter" route to the complexity question is closed.
Of the remaining two — a uniform-in-$c$ algorithm, or a hardness reduction — which would you pursue
first, and is there an intermediate target (for example, a structural criterion eliminating
$\exists W$ at fixed $D$) that would be worth settling before either?

### Reliability

| Item | Status |
|---|---|
| II.1(b) set/dimension part | Lean, axiom-audited (three lemmas) |
| II.1(a) exactness, II.1(b)(ii) equivalence | paper proof, no machine check |
| II.2 base description | paper proof (classical), multiplicity caveat qualified |
| II.3 charts and algorithm | paper construction, no machine check |
| II.4 both sides | exact arithmetic: $c=2$ side explicit rational design; $c=1$ side symbolic gcd over the family |
| II.5 obstruction | dimension count |
| II.6 dictionary | exact arithmetic, three instances |
