# Status report and request for direction

This note consolidates the current state of the project after the revisions you requested, lists what is proved and
how it is checked, records the corrections we had to make, and ends with six questions on how to proceed.

Verification levels used: **L1** = paper proof written out; **L2** = exact rational/integer arithmetic on finite
instances (a filter, never a confirmation); **L3** = machine-checked (Lean 4 + Mathlib, exit code 0, declaration
names given).

---

# Part I. Setting

$A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$ with
$\operatorname{rank}[C;L_0]=p+r$. A candidate $\mathcal L\in\mathbb C^{q\times n}$ has
$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$ and $\operatorname{rank}[C;\mathcal L]=p+q$ (whence
$\operatorname{rank}\mathcal L=q$). With $h=\operatorname{rank}[\mathcal L;CA;C]$ the normal rank of
$Q_{\mathcal L}(\lambda)=[\lambda\mathcal L-\mathcal LA;CA;C]$:

$$(5a)\ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\ \operatorname{rank}Q_{\mathcal L}(\lambda)=h\ \ \forall\lambda .$$

Notation fixed once and for all: $R=\operatorname{row}\mathcal L$, $C=\operatorname{row}C$,
$W=\operatorname{row}[C;CA]$ ($\dim W=r_1$), $S=\operatorname{row}[C;L_0]+W$ ($\dim S=s_0$),
$\mathcal Z=\ker[C;\mathcal L]$, $\mathcal Z^\perp=\operatorname{row}[C;\mathcal L]$, $\pi$ = quotient map modulo
$\operatorname{row}C$; $\varepsilon_j$ = left minimal indices of $Q_{\mathcal L}$, $d_{\rm fin}$/$d_\infty$ = total
degree of finite/infinite elementary divisors.

**Type I** means $h\ge q+r_1$; **Type III** means $h<q+r_1$ but $d_{\rm fin}>0$.

---

# Part II. What is established, and how it is checked

## II.1 The classification has two cases, not three

$k:=q+r_1-h$ (the number of nonzero left indices) satisfies $k\le\operatorname{rank}\mathcal L$ always, because
$h\ge r_1$ (row stacking) and $\operatorname{rank}\mathcal L=q$; hence the "counting-deficiency" case $k>\operatorname{rank}\mathcal L$
is empty and $(5b)$ fails for exactly two reasons: **counting** ($h\ge q+r_1$) and **spectral**
($h<q+r_1$ with $d_{\rm fin}>0$). *Checked*: L1 + **L3** (`TypeII.typeII_vacuous`) + L2 (93/93).

## II.2 The counting side is arithmetic — unconditional form

Replacing the earlier conditional "uniformity" statement (which used an object $V'$ that I could not define
intrinsically — you were right to insist), we now have an unconditional identity:

$$h=s_0+q-\dim(R\cap S).$$

*Proof.* $\mathcal Z^\perp=C\oplus R$; since $\operatorname{row}L_0\subseteq R\subseteq\mathcal Z^\perp$ we get
$\mathcal Z^\perp+S=\mathcal Z^\perp+W$, so $h=\dim(\mathcal Z^\perp+S)=(p+q)+s_0-\dim(\mathcal Z^\perp\cap S)$;
and $(C\oplus R)\cap S=C\oplus(R\cap S)$ because $C\subseteq S$ and $C\cap R=0$. $\square$

Consequences, all with the same proof:

* $h\le s_0+q-r$ (since $\dim(R\cap S)\ge\dim\operatorname{row}L_0=r$);
* $\text{Type I}\iff R\cap W=0$;
* $s_0\le r_1+r$; hence **Type I is possible only when $s_0=r_1+r$**, and then
  $\text{Type I}\iff R\cap S=\operatorname{row}L_0$;
* **if $s_0<r_1+r$ then no augmentation at that order is Type I** — an unconditional exclusion, independent of
  $\mathcal L$.

*Checked*: L1; L2: identity 35/35, inequality and equality criterion 54/54, `Type I ⟺ R∩W=0` 56/56,
$s_0<r_1+r$ samples 39 with **0** Type I.

An equivalent geometric form, already machine-checked: $h=q+r_1-\dim(\pi R\cap\pi W)$, so
$\text{Type I}\iff\pi R\cap\pi W=0$. Its generic consequence: if $q+\dim\pi W>n-p$ then no $R$ avoids $\pi W$ and
Type I cannot occur at that order; if $q+\dim\pi W\le n-p$ then avoidance is the generic situation, and the
interesting case is exactly the one where $(5a)$ forces $R$ into the incidence locus.
*Checked*: L1 + **L3** (`TypeIGeom.mkQ_map_inf_eq`, `typeI_dim`, `typeI_geometric`, `B11_dim`).

## II.3 The Kronecker chain (B.6–B.10), revised per your review

* **B.6.** $(5a)$ forces the right null module of $Q_{\mathcal L}$ to be generated over $\mathbb C[\lambda]$ by its
  constant vectors; a vector-space basis of the constant nullspace is then a module basis, so all right minimal
  indices vanish. L1 + L3 kernel + 150/150.
* **B.7 (proof replaced as you suggested).** Reverse the pencil: at $\mu=0$ the reversed pencil has rank $q$;
  choose $h$ rows containing all $q$ rows of $\mathcal L$ and $h$ columns with a nonzero minor; that minor is
  $\mu^{h-q}(c+O(\mu))$ with $c\ne0$, while every $h\times h$ minor is divisible by $\mu^{h-q}$; hence the $h$-th
  determinantal divisor has valuation exactly $h-q$, the first $q$ invariant factors are units and the remaining
  $h-q$ have total valuation $h-q$, so each has valuation one and $d_\infty=h-q$. L1 + L3 kernel + 151/151.
  (The earlier argument, which you identified as invalid, is gone.)
* **B.8.** $(5b)\iff d_{\rm fin}=0\iff\sum\varepsilon=\operatorname{rank}\mathcal L$. Following your advice we no
  longer cite the identity as a black box: from the Kronecker form of a **rectangular** pencil (existence:
  Gantmacher II Ch. XII; Kailath §6.5) the normal rank is the sum of the block ranks, giving
  $h=\sum\eta+\sum\varepsilon+d_{\rm fin}+d_\infty$ block by block.
* **B.9.** Nonzero left indices $=q+r_1-h$; the bridge from "constant left null vectors" to "zero left indices" now
  goes through a reduced minimal basis and its predictable-degree property, as you asked; plus the consistency
  checks $h\ge r_1$ and $h\le q+r_1$.
* **B.10.** $Q_{\mathcal L}=D(\lambda)H$ with $D$ block triangular, invertible off $\operatorname{spec}\Lambda$;
  so $(5b)$ need only be tested there. Bad eigenvalues can be non-real.
* **B.10b (new).** On a chart and a locally closed stratum $\Sigma=\{\operatorname{rank}[V|Z]=\rho,\ h=h_0,\
  (5a)\}$, the coefficients $\Lambda$ can be chosen rationally in the parameters (Cramer), so the spectral-failure
  locus is the projection of a closed subset of $\Sigma\times\mathbb P^1$; by properness of $\mathbb P^1$ that
  projection is closed. Hence **on each stratum the failure locus is closed and the feasible locus open**; across
  strata one only gets constructible. This resolves the tension you pointed out in your §10.2.

## II.4 The whole-family counterexample

$n=6$, $p=r=2$, $q_0=3$, $r_1=4$, $s_0=5$: every $(5a)$-admissible augmentation at $q_0$ fails $(5b)$, and
$q_{\min}=4$. Three **algebraic** proofs cover all parameters: a per-chart gcd over $\mathbb Q(\theta)[\lambda]$
(generic degree $2$, the only exceptional parameters giving degree $1$, never $0$ — so the "drop locus" is empty);
a Bézout left-null-space computation whose two polynomials in $\theta$ generate the unit ideal; and a
$\theta$-only determinantal elimination of the joint system $(5a)+(5b)$ with Gröbner basis $[1]$. The geometric proof
(generic-degree map $\mathbb P(V)\to\mathbb P(\ker[C;L_0])$ that is nonconstant, hence surjective) is **demoted to
conditional**: the proportionality needed to define $\lambda(x)$ is proved separately (the $2\times2$ determinant
vanishes on a basis and on a sum of basis vectors, hence by polarization identically — re-checked exactly), but
$L_0|_V$ has rank $1$, so the formula is undefined at one point of $\mathbb P(V)$ and properness cannot be invoked
on an open subset. One target line may be missed; that is the remaining gap.

## II.5 Per-order decision: what is certified, and how much

Three tools, all certificate-based (a verdict is `FEASIBLE` only with an explicit augmentation passing seven
independent checks; `INFEASIBLE` only with an integer, an algebraic-emptiness, or a gcd certificate):

* integer screening: Type I decides many orders outright (§II.2);
* per-chart symbolic gcd (degree $0$ $\Rightarrow$ feasible; $\ge1$ $\Rightarrow$ generic failure with an explicit
  common factor);
* $\theta$-only determinantal elimination of $(5a)$ together with the Bézout rank condition.

Coverage measured: at $q_0$, 26 instances gave 15 `FEASIBLE` (with witnesses), 9 `INFEASIBLE` (constant charts,
complete) and 2 `UNKNOWN`, in about 20 seconds. A witness-only scan over 89 instances ($n=5,6,7$, $p,r\in\{1,2\}$)
took 48 seconds and produced 74 upper bounds for $q_{\min}$; the observed gaps were 0 in 55 cases, 1 in 18, 2 in 1.
The sufficient condition $s_0\ge r_1+r$ predicted a positive gap in 18 cases with **no false positive** and one
miss. Every `INFEASIBLE` on a non-constant chart, however, is only "typical stratum" — the rank-drop strata are not
covered, and that is where the remaining incompleteness is.

## II.6 The two empirical phenomena, correctly stated

1. **Generic degree dichotomy.** For a chart, let $g$ be the generic degree of the gcd of the maximal minors of
   $P_{\mathcal Z}(\lambda)$. Then $g=0$ means the generic parameter is spectrally feasible, $g>0$ means the generic
   parameter fails. Specializations can lower $g$ — that is the "drop locus" — and feasible parameters, when they
   exist in the $g>0$ case, lie there. For the counterexample the drop locus is empty.
2. **Shape of the feasible set.** Per stratum it is open (II.3, B.10b); across strata only constructible. My earlier
   flat statement "the feasible set is not open" was wrong in that form.

## II.7 Encoding: the $\exists\mathbb R$ upper bound is intact

This point needs a correction of something I wrote in an earlier note. We once argued that the encoding is
exponential, because the unstructured Bézout identity $\sum u_im_i=1$ needs all maximal minors and their number is
$\binom{n}{\rho}\binom{\rho+d}{\rho}$; in a controlled regime we measured $\log_2 N/n\to1.09$. **That measurement
concerns the unstructured variant only and does not apply to the encoding actually used**, which is structured:

* the spectral condition is the matrix identity $X(\lambda)P(\lambda)=I_t$ with $\deg X\le t-1$ (linear in the
  coefficients of $X$, $t^2q=O(n^3)$ unknowns, degree bound from the pencil right-inverse criterion you identified —
  Noferini–Van Dooren Lemma 5.2 — with the conditions checked one by one);
* the degenerate case $Z\cap\mathcal V\ne0$ is handled by an $O(n)$ disjunction on $s=\dim(Z\cap\mathcal V)$ together
  with working modulo $S$, so no generalized inverse and no Smith-form degree control is needed;
* the coefficient bit length is $O(n^2(B+\log n))$ (Hadamard + Cramer), and every constraint can be written with
  division-free arithmetic circuits.

So $\mathrm{DEC}(q)\in\exists\mathbb R$ with a polynomial-size encoding stands, and what remains open is hardness and
polynomial algorithms, not membership. (This also means my earlier "the $\exists\mathbb R$ route is void" remark was
wrong; it has been retracted in our notes.)

## II.8 What is machine-checked

37 propositions are registered; 25 have Lean content, 159 declarations across 59 files, with every declaration
mapped to the proposition it supports and to its "difference" (0 audit issues). The Lean part covers, among others,
the pencil equivalence, the top/$\rho=0$/full-space cases, the cyclic-vector criterion, the counting case's vacuity
(B.9b), the geometric form of Type I (B.11b), the dimension formula (B.11), the row-space form of $(5a)$ (A.0), and
a matrix row-space bridge. Not Lean-checkable at present: B.8–B.10 (Kronecker/Smith theory), the quotient step of
A.0, and the algorithmic statements.

## II.9 Corrections we made (all recorded, none deleted)

| Earlier claim | Status |
|---|---|
| Type II ("counting deficiency") as a separate case | empty; proved and machine-checked |
| "$\dim(\operatorname{row}L_0\cap W)\le p\ \Rightarrow$ Type I everywhere" | **wrong** (55 false positives in 89 instances); correct form is $\operatorname{row}L_0\cap W\subseteq\operatorname{row}C$, equivalently $s_0=r_1+r$ (0 false positives) |
| "uniformity under $V'\cap S=0$" | $V'$ had no intrinsic definition; replaced by the unconditional identity of II.2 |
| "the $\exists\mathbb R$ route is void because the encoding is exponential" | retracted; see II.7 |
| "the feasible set is not open" | corrected: open on each stratum, constructible across strata |
| B.7's old proof | invalid (you identified the reversed factor as singular at $\mu=0$); replaced |
| the geometric proof of the counterexample | demoted to conditional; two gaps, one now proved separately, one open |
| the "$(5a)\iff\overline T$-invariance" negative statement | withdrawn from the proof chain pending reproduction of a counterexample |

---

# Part III. Questions

**Q1 (target).** With the counting side reduced to arithmetic and the spectral side being the only hard part, which
of the following would you attack first: (a) an $\exists\mathbb R$-hardness reduction for the spectral part;
(b) a polynomial algorithm for the counting side plus a *complete* compact decision for the spectral side;
(c) a structural classification of when Type III occurs at all (see Q2)?

**Q2 (a boundary phenomenon).** In all instances we have found, Type III at $q_0$ occurs only when
$r_1=p+r$ (four out of four, including the counterexample, whose three Jordan blocks make $r_1$ maximal). Is this
boundary phenomenon familiar — e.g. is "$r_1=p+r$" the only stratum where the incidence map can be surjective? If
it is a theorem, the search space for Type III would collapse to that boundary.

**Q3 (which hardness).** If one attempts hardness, is $\exists\mathbb R$-hardness the right target rather than
NP-hardness, given that the feasibility problem is an $\exists\mathbb R$ statement of polynomial size whose
counting part is decidable in polynomial time? Which known $\exists\mathbb R$-complete problem would you reduce
from — quadratic feasibility, or something closer to a determinantal condition?

**Q4 (the decision procedure).** Our per-order procedure is exact but incomplete on the rank-drop strata; making it
complete requires a subresultant description of the "drop locus". Is that the right technical investment, given that
a complete decision procedure does not by itself give a complexity bound? Or would you rather see the effort go into
the compact encoding of the *whole* order spectrum?

**Q5 (structure of the pencil).** The pencil has a very special shape: $[({\lambda}I-A)V\,|\,Z]$ with the first block
linear in $\lambda$ and $V,Z$ constant. Do you see a route to a polynomial algorithm that exploits this — for
instance through the fact that all bad eigenvalues lie in $\operatorname{spec}\Lambda$ with
$\deg\det(\lambda I-\Lambda)=q$, so the test could be run on a degree-$q$ polynomial rather than over all
$\lambda$?

**Q6 (priority).** Should we now write up the two results (the counting structure of II.2, and the counterexample of
II.4) as the paper, with the decision procedure as an appendix, or keep pushing on Type III while the machinery is
warm? We have no preference; we would follow your judgement.
