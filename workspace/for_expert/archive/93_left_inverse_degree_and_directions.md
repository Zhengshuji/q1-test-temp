# Minimum-order functional observers: three frontiers, two new observations, and a request for task planning

This note reports where the decision problem stands, two small results obtained since the last
exchange, and six questions. It is self-contained: Part I fixes the problem and the notation,
Part II states what is proved, what is machine-checked, and what is conjecture, and Part III asks
for specific judgements. Nothing here is claimed beyond the label attached to it.

---

## Part I. The problem and the notation

### I.1 Data and conditions

Fix rational matrices $A\in\mathbb Q^{n\times n}$, $C\in\mathbb Q^{p\times n}$ with
$\operatorname{rank}C=p$, and $L_0\in\mathbb Q^{r_0\times n}$. We look for $R$ such that
$\mathcal L=[L_0;R]\in\mathbb Q^{q\times n}$ satisfies

$$
(5a)\quad \operatorname{rank}\begin{bmatrix}\mathcal LA\\ \mathcal L\\ CA\\ C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}\mathcal L\\ CA\\ C\end{bmatrix},
\qquad
(5b)\quad \operatorname{rank}\begin{bmatrix}\lambda\mathcal L-\mathcal LA\\ CA\\ C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}\mathcal L\\ CA\\ C\end{bmatrix}
\quad \forall\lambda\in\mathbb C .
$$

Write $q_{\min}$ for the least admissible $q$ (possibly $+\infty$) and separate three problems:

$$
\mathrm{DEC}(q):\ \exists R?,\qquad
\mathrm{OPT}:\ q_{\min}=?,\qquad
\mathrm{FIND}:\ \text{output }R\text{ together with a minimality certificate.}
$$

$\mathrm{DEC}\equiv\mathrm{OPT}$ by scanning the $n-r_0+1$ candidate orders;
$\mathrm{FIND}$ additionally needs constructivity and an output field.

### I.2 The compression used throughout

Let
$$
K_0=\ker[C;CA],\qquad k=\dim K_0,\qquad N \text{ a basis of } K_0,
$$
$$
H=LN,\qquad H_A=LAN,\qquad \omega=\operatorname{rank}H,
$$
and
$$
\mathcal T=\operatorname{row}[N\ AN]\subseteq\mathbb Q^{2k},\qquad d_0=\dim\mathcal T,\qquad
r=q-r_0,\qquad \kappa_{\rm obs}=r\,d_0,\qquad \ell=\operatorname{rank}(AN).
$$
Then

$$
(5a)\iff\operatorname{row}H_A\subseteq\operatorname{row}H,
\qquad
(5b)\iff\operatorname{rank}(\lambda H-H_A)=\omega\quad\forall\lambda .
$$

Each free row pair lies in $\mathcal T$, and conversely every element of $\mathcal T$ is realised by a
state-space row; $\kappa_{\rm obs}$ is the dimension of the total compressed free-row space.

### I.3 What the literature settles, and what it does not

Fernando's two 2026 papers give an order-by-order characterisation (algebraic condition,
spectral condition, chart parameterisation $\exists\Theta$, maximal-minor gcd test), the order
spectrum, minimal order and a construction. What they do not give is the **decision complexity**
of the chart-times-semialgebraic feasibility problem. That is the only question we pursue.
Consequently we do not reprove any characterisation statement.

### I.4 Layer geometry (the notation used in Part II)

For a candidate row space $\mathcal V=\operatorname{row}\mathcal L$ put
$\rho=\dim\pi(\mathcal V)$ and $c=\dim(\mathcal V\cap\mathcal J)$, where
$\mathcal J=\operatorname{row}[C;CA]$ and $\pi$ is the quotient map; then $q=\rho+c$.
Separately, $\omega=\dim(\mathcal V\cap K_0)$, so $k-\omega=\operatorname{codim}_{K_0}(\mathcal V\cap K_0)$
measures the compression loss. The **hyperplane case** discussed in Part II is $k-\omega=1$: there the
base space is $\mathbb P(K_0)$, and the admissibility constraint reads $Rv=0$, $RAv=0$ for
$v=N\sigma^{\mathsf T}$.

---

## Part II. Status, and two observations from this round

### II.1 Three upper bounds and one exact test

1. **[Theorem, bit-level]** For every fixed order $q$, $\mathrm{DEC}(q)$ is decidable in
   $\mathcal L^{O(q^2)}$ bit operations, where $\mathcal L$ is the input bit length. The
   quantification is over a gauge-reduced pair plus a spectral certificate.
2. **[Theorem, bit-level]** For fixed $\ell=\operatorname{rank}(AN)$,
   $\mathrm{DEC}$ runs in $\exp(O(\ell^2\log(\ell+2)))\operatorname{poly}(\mathcal L)$,
   independently of the number $r$ of free rows. The certificate is a Gram–Bézout object whose
   size is governed by $\ell$, compressed by Cauchy–Binet so that no maximal minor is enumerated.
3. **[Theorem]** $q1\in\exists\mathbb R$, via a polynomial left inverse of degree $\le2\omega-2$.
4. **[Theorem, exact test]** $r=0$ reduces to a rational linear system with
   $(2\omega-1)q\omega$ unknowns and $2\omega^3$ equations, decided in deterministic polynomial
   time; no Kronecker/Smith algorithm is needed, and an explicit witness $S(\lambda)$ is returned.

All four are upper bounds. None of them decides unrestricted $q1$.

### II.2 Layer geometry

- **[Proved]** In the hyperplane case the lifted incidence space has at most $\delta+1$ irreducible
  components ($\delta=\dim\ker T$; at most three when $\delta=2$), each an open subset of a vector
  bundle, with the rank identities $\operatorname{rank}[P;Q]=\delta-2+\operatorname{rank}[v,Av]$.
- **[Algorithm, one-sided]** Per component, a random point plus a gcd test decides feasibility with
  false-negative probability $\le2^{-T}$. This is **not** a decision procedure: the set on which the
  gcd drops (the exceptional locus) is not completely enumerated, so the routine is allowed to
  answer only "feasible" or "unknown".
- **[Proved, $c=2$ partial]** Component bound $\binom{s}{2}+3s+2$; exact fibre
  $\operatorname{rank}(V\to K/V)=c-t$, an open Grassmannian; nonemptiness conditions per subtype.
- **[Conjecture]** Type control: for fixed $c$ the stratification by the Kronecker type of the
  restricted pair $(\iota|_W,A|_W):W\rightrightarrows W+A(W)$ has finitely many local-closed strata,
  with a bound $N(c)$ independent of $k$. (Jordan type is *not* the right invariant, since
  $A(W)\not\subseteq W$ in general.)

### II.3 Hardness side

Only two sound gadgets exist: the nonzero gadget $(5b)\iff f\ne0$, and the input-controlled
nonzero gadget $\exists R:(5a)\wedge(5b)\iff x\ne0$. The multiplication construction is a
full-observer realisation but **not sound**: $R=0$ gives a feasible instance that ignores the
intended variables. There is no reduction, so there is no hardness result. This is the standing
obstruction.

### II.4 Observation 1: the left-inverse degree bound looks loose by a factor of two

For a degree-one pencil $Q(\lambda)=\lambda X-G\in\mathbb Q[\lambda]^{q\times\omega}$ with $X$ of
full column rank and $Q$ of full column rank at every $\lambda$, define

$$
d_{\min}=\min\{\,d:\ \exists S(\lambda)=\textstyle\sum_{j\le d}S_j\lambda^j,\ S(\lambda)Q(\lambda)=I_\omega\,\}.
$$

The bound we use is $d_{\min}\le2\omega-2$, obtained by composing Bézout multipliers of degree
$<\omega$ with the adjugate of degree $\omega-1$. Both steps are lossy, and the data below suggest
that the composition is far from tight. Machine-checked, exactly, over rationals:

| $(q,\omega)$ | pencils scanned | feasible | histogram of $d_{\min}$ |
|---|---|---|---|
| $(3,2)$, exhaustive over $\{-1,0,1\}^6$ | 729 | 464 | $\{1:464\}$ |
| $(3,2)$, random entries in $[-2,2]$ | 1500 | 1267 | $\{1:1267\}$ |
| $(4,2)$, random | 1500 | 1453 | $\{0:1173,\ 1:280\}$ |
| $(5,2)$, random | 800 | 797 | $\{0:774,\ 1:23\}$ |
| $(4,3)$, random | 600 | 374 | $\{2:374\}$ |
| $(5,3)$, random | 300 | 270 | $\{1:236,\ 2:34\}$ |
| $(5,4)$, random | 60 | 46 | $\{3:46\}$ |
| $(6,4)$, random | 40 | 37 | $\{1:31,\ 2:4,\ 3:2\}$ |
| $(6,5)$, random | 20 | 16 | $\{4:16\}$ |

Three features:

1. $d_{\min}=2\omega-2$ was **never** attained ($\omega=2$: bound 2, observed $\le1$;
   $\omega=3$: bound 4, observed $\le2$; $\omega=4$: bound 6, observed $\le3$;
   $\omega=5$: bound 8, observed $\le4$).
2. The value $\omega-1$ **is** attained and is the observed maximum throughout; it appears also away
   from the minimal-height case (at $(6,4)$, where $q=\omega+2$, the values $1,2,3$ all occur).
3. For $q=\omega+1$ the histogram has a single bucket, exactly $\omega-1$ — in all four cases
   tested ($\omega=2,3,4,5$; 2167 feasible pencils).
   This has a one-line lower-bound explanation: with $X=[I_\omega;0]$, a constant left inverse
   forces $S_0=[0\mid C_0]$ of rank $\le q-\omega$, so $q-\omega\ge\omega$ is necessary for $d=0$;
   hence $q=\omega+1$, $\omega\ge2$ gives $d_{\min}\ge1$.

**Conjecture.** $d_{\min}\le\omega-1$ whenever $Q$ is pointwise of full column rank, with equality
observed for $q=\omega+1$.

If true, the $r=0$ linear system — which we currently run at $d=2\omega-2$ — shrinks from
$(2\omega-1)q\omega$ to $\omega^2q$ unknowns, and the $\exists\mathbb R$ left-inverse certificate
shrinks correspondingly. We have no proof.

Two side remarks that are proved: normalisation by invertible constant row/column operations
preserves $d_{\min}$ (so $X=[I;0]$ is a legitimate canonical form; 168/168 machine-checked
agreement), and the bound $d_{\min}\le2\omega-2$ is therefore not an artefact of coordinates.

### II.5 Observation 2: the fixed-order encoding cannot be shrunk to $O(q)$ variables

The fixed-$q$ encoding quantifies over $G=FX$, $X$ (each $q\times\omega$) and the spectral
certificate ($2\omega$ real variables), that is $2q\omega+2\omega$ variables. There is a free
$GL_\omega$ action $(X,G)\mapsto(XS,GS)$ with $B\mapsto S^{-1}B$, so the quotient has
$2q\omega-\omega^2$ variables; fixing the gauge by a chart (forcing $\omega$ rows of $X$ to the
identity) removes the action but not the variable count, at the price of $\binom{q}{\omega}$ charts.
Either way the quantifier-elimination instance has $\Theta(q^2)$ variables when $\omega=\Theta(q)$.

Consequently, **in this family of encodings** no $O(q)$-variable formulation exists, and the
exponent $O(q^2)$ of the fixed-order algorithm cannot be improved by bookkeeping. This matters for
the parameterised lower-bound programme: the chart cost $\binom{q}{\omega}$ is harmless for an XP
statement, but the variable count is exactly what blocks an FPT statement.

---

## Part III. Requests

**Q1 (hyperplane determinism).** In the case $c=1$ we have at most $\delta+1$ components, each an
open subset of a vector bundle, and a one-sided test whose only gap is the exceptional locus where
the maximal-minor gcd drops. The candidate enumeration of that locus is incomplete: a drop can also
be caused by the vanishing of a leading coefficient of a minor, not only by a common root. What is the
right formulation? Two options we can see are (i) a generic-gcd computation over the function field
of each component, followed by a recursion on the exceptional divisor, and (ii) a global statement
"the drop locus of the gcd of maximal minors of a linear pencil is a closed subscheme of degree
$\le D(\omega,q)$", which would give a finite exact test. Is either known, and which do you recommend?

**Q2 (type control).** Is the finite stratification by the Kronecker type of the restricted pair
$(\iota|_W,A|_W):W\rightrightarrows W+A(W)$ a theorem, with a bound $N(c)$ independent of $k$? What
is the cleanest invariant language for a subspace pair whose image is not invariant (quiver
Grassmannian? restricted pairs à la Berger–Trunk–Winkler?), and is there a reference that already
contains the $k$-independence we conjecture?

**Q3 (is FPT in $q$ plausible at all?).** Given II.5, an FPT$(q)$ theorem would have to avoid
quantifier elimination over $\Theta(q^2)$ variables. Do you regard that as plausible, or is XP$(q)$
the natural ceiling? If the ceiling is real, is W[1]-hardness in $q$ the right target, and is there a
source problem whose reduction respects both the row-wise constraint $(H_i,(H_A)_i)\in\mathcal T$
(with one common $\mathcal T$) and the identity $\operatorname{row}H_A=\operatorname{row}H$?

**Q4 (hardness route).** The recommended programme was a single translation lemma from affine rank
minimisation at fixed rank 3, using a fixed gauge block and a global row-space decoding, rather than
local multiplication gates. Before we invest in it: what do you expect the obstruction to be — the
per-row separability of $\mathcal T$, the pencil condition, or the fact that a rank-constrained global
object has no canonical basis once $\omega<q$? And would a no-go theorem for gate architectures be
worth writing, or is the global encoding the only sensible route?

**Q5 (the degree bound).** We use the elementary adjugate–Bézout bound $\deg S\le 2d\omega-d-1$, which is
$2\omega-2$ at $d=1$; degree bounds for polynomial-matrix left inverses are classical (Fabiano–Struppa,
Multidim. Syst. Signal Process. 1 (1990) 67–74), and we cite them as such without using their explicit
form. Does any of those bounds specialise, for degree-one pencils, to something linear in $\omega$ —
in particular to $\omega-1$? Our exact search says the elementary bound is not attained and that
$\omega-1$ is, so either the classical bounds are sharper than the adjugate route in this case, or the
conjecture needs a new argument. (We also tested the guess $\max(0,2\omega-q)$: it fails, e.g. at
$(5,3)$ where $2\omega-q=1$ but $34$ of $270$ pencils have $d_{\min}=2$.) If $\omega-1$ is known we
will cite it instead of conjecturing; if it is false we would like a counterexample, since our search
covered only $\omega\le5$ and $q\le\omega+2$.

**Q6 (task planning).** We have (i) a bit-level FPT theorem in $\ell$, (ii) a bit-level XP theorem in
$q$, (iii) no hardness reduction, (iv) a layer program that is the only visible route to a
polynomial algorithm, and (v) the two observations above. How would you order the following four, if
the goal is to move $q1$ rather than to publish:

- (a) make the hyperplane case deterministic (Q1), which would close the first non-trivial layer;
- (b) prove or refute type control (Q2), which would bound the number of components for all $c$;
- (c) the affine-rank-minimisation translation lemma (Q4);
- (d) W[1]-hardness in $q$ (Q3).

And a related question: is there a **known problem class** we should be testing membership against,
instead of building the layer program ourselves — for instance "rank-constrained feasibility over a
Grassmannian", "determinantal variety intersection", or "parametric linear system with a rank
condition"? If $q1$ is equivalent to a problem whose complexity is already classified, we would
rather learn that than continue.

### Reliability of what is asserted above

| Item | Label |
|---|---|
| fixed $q$: $\mathcal L^{O(q^2)}$ | proved, bit-level, audited |
| fixed $\ell$: FPT, $r$-independent | proved, bit-level, audited (one gap: FIND's bit model) |
| $q1\in\exists\mathbb R$ | proved (left-inverse certificate) |
| $r=0$ linear system | proved; machine-checked on 135 pencils plus negative controls |
| hyperplane components $\le\delta+1$ | proved |
| hyperplane algorithm | one-sided only; **not** a decision procedure |
| $c=2$ structure | proved partially; algorithm one-sided |
| type control | **conjecture** |
| $d_{\min}\le\omega-1$ | **conjecture**; evidence is exact but finite |
| no $O(q)$-variable encoding | proved for the encodings we use; not a general impossibility |
| sound multiplication, hardness | **not established** |

We would rather be told that one of these is wrong than have it pass unchallenged.
