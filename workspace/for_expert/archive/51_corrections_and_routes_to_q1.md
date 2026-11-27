# Corrections, a Lean-checked stratum theorem, and a request for routes to q1

This report has three parts. Part I fixes the setting. Part II records the corrections requested in the last
audit and one new result: a Lean-checked kernel for the constrained stratum. Part III asks for help with the
next step: which technical routes are most likely to move q1, and whether the candidate routes below are
sensible.

## Part I. Setting

Given $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$, one seeks
$R\in\mathbb C^{(q-r)\times n}$ such that $L=[L_0;R]$ (q rows, full row rank) satisfies

$$(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\quad\forall\lambda\in\mathbb C .$$

Put $K=\ker[C;CA]$, $k=\dim K$, choose a basis $N_K$, and let $H=LN_K$, $H_A=LAN_K$. For a fixed rank
$\omega$, the admissible locus is the set of $R$ with $\operatorname{rank}H=\omega$ and
$\ker H\subseteq\ker H_A$; on it the induced map $Z:W\to\mathbb C^q$, $W=\operatorname{im}H$, is defined by
$Z(Hx)=H_Ax$. Choosing a complement and writing $Z=(A;B)$ gives

$$\text{bad}\iff\exists\,0\ne y\in\ker B,\ Ay\in\mathbb C y .$$

For $q=\omega+1$, $B$ is a single row; for $\omega=2$ it is a line $\ker B=\mathbb Cw$ and
$\text{good}\iff B\ne0$ and $\det[w,Aw]\ne0$. The free case is $\ker T=0$ for $T(v,w)=v+Aw$; then the bottom
rows are unconstrained. In the constrained case the compatible pairs satisfy $xZ_1+yZ_2=0$.

## Part II. Corrections and results

### II.1 The case $k=\omega$: a corrected RP route

The two-combination lemma is now proved by the sequential argument: choose a nonzero $f$ in
$V_0=\operatorname{span}_{\mathbb Q}\{m_i\}$; if $f$ has finitely many irreducible factors $p_1,\dots,p_s$,
each $V_{p_j}=\{h\in V_0:p_j\mid h\}$ is a proper $\mathbb Q$-subspace, and a finite union of proper
subspaces cannot cover $V_0$; choose $g$ outside. Then $\gcd(f,g)=1$. The resultant $\operatorname{Res}_\lambda(f,g)$
is nonzero of total degree at most $2k^2$ in $R$; together with the rank witnesses this gives an exceptional
set of degree at most $2k^2+k+q$, and the grid $N=2(2k^2+k+q)$ gives false-negative probability at most
$1/2$.

For the determinantal-divisor step, I will state the following as a separate lemma rather than cite author
names alone:

> Given $P(\lambda)\in\mathbb Q[\lambda]^{q\times k}$ of degree at most one and full column normal rank $k$,
> the gcd of its $k\times k$ minors can be computed in deterministic polynomial bit complexity in $q,k$ and
> the coefficient bit size.

This is intended to follow from a rectangular Smith/Hermite form; if the cited theorem is only for square
nonsingular input, a reduction is included. The Kaltofen–Krishnamoorthy–Saunders reference is the
deterministic route; the Storjohann–Labahn algorithm is a faster Las Vegas alternative for square nonsingular
input and is not used as the primary citation.

With these two items the RP statement is unconditional in the paper; the fixed-$(q,\omega)$ polynomial
statement is retained. ZPP is not claimed.

### II.2 The free-fibre criterion at $q=3$, $\omega=2$ (final form)

Assume $\ker T=0$ and $\operatorname{rank}L_0=r$. Let $E=\operatorname{row}(U_0)$,
$F_0=\operatorname{row}(V_0)$, $m=3-r$, and let $\rho$ be the normal rank of $\lambda U_0-V_0$ over
$\mathbb C(\lambda)$. The criterion is:

1. $\dim(E+F_0)\le2$;
2. $m\ge2-\dim E$;
3. one of
   (a) $\rho=2$, $V_0\ne\lambda U_0$ for every $\lambda$, and either the fixed pencil is good or $m\ge1$;
   (b) $\rho=2$, $V_0=\lambda_0U_0$ for some $\lambda_0$, and $m\ge2$;
   (c) $\rho=1$ and $m\ge2$;
   (d) $\rho=0$ and $m=3$.

Case (c) now has the incidence-dimension proof: at a fixed $\lambda$ with $a(\lambda)\ne0$, the condition
$b_1(\lambda),b_2(\lambda)\in L(\lambda)$ has codimension two in the eight-dimensional parameter space, and
varying $\lambda$ adds one dimension, so the incidence variety has dimension at most seven and its projection
cannot fill the parameter space; at the finitely many $\lambda_0$ with $a(\lambda_0)=0$ one imposes
independence separately. The full-row-rank condition is handled once: the image of the top rows in
$S\times S$ has dimension at most $r$, so the quotient has dimension at least $4-r=m+1$, and $m$ bottom pairs
can be chosen independent modulo the top rows. The theorem is stated for every $k\ge2$; the 1200 random
instances are corroboration only, not part of the proof.

### II.3 The constrained stratum: an all-bad theorem, a Lean kernel, and the $q_{\min}$ correction

For the $n=5$ instance ($C=e_1^{\mathsf T}$, $A$'s first row $e_5^{\mathsf T}$, columns $2,3,4$ equal to
$e_3,e_2,e_5$, $L_0=e_4^{\mathsf T}$), the two admissible Grassmannian points are $\sigma=(1,\pm1,0)$. Over
$S_1$ the compatible pairs are $x=(a,-a,b)$, $y=(-a,a,d)$; over $S_2$, $x=(a,a,b)$, $y=(a,a,d)$. At
$\lambda=-1$ (over $S_1$) all three rows of $\lambda H-H_A$ lie in $\operatorname{span}\{E_3\}$; over $S_2$
the same happens at $\lambda=+1$. Hence the whole $q=3,\omega=2$ stratum is bad.

The algebraic core is now machine-checked. A Lean file proves: a $3\times3$ matrix over a field whose rows
all have zero first and second coordinates has rank at most one (via the row space contained in the span of
$E_3$), and the same for the special row form with only the third column possibly nonzero. The file is in the
build graph; the whole build exits with code zero and the project's rule check passes. This is a kernel
(F2), not the literal statement: the derivation of the row form from the compatibility equations and the
parametrisation remains paper plus exact verification.

Finally, the correction: the claim $q_{\min}=4$ was wrong. The data admit
$L=\binom{e_4^{\mathsf T}}{e_5^{\mathsf T}}$, of order $q=2$, which passes all consistency checks
($\operatorname{rank}[C;L]=3$, $(5a)$, $h=3$, $(5b)$), while $q=1$ fails at $\lambda=0$. Hence
$q_{\min}=2$. Two independent reasons made the old inference invalid: a bad stratum does not make the order
infeasible (the $\omega=1$ layer at $q=2$ is feasible), and $(C,A)$ is not observable
($\langle e_1,e_4,e_5\rangle$ is $A$-invariant, so the observability matrix has rank at most three), so the
terminal-region result cannot be applied.

## Part III. Questions

**Question 1 — routes to q1.** Given the state above, which of the following routes would you prioritise, and
why?

(a) a general constrained-fibre criterion at $q=\omega+1$, starting with $k-\omega=1$
($\operatorname{Gr}(\omega,\omega+1)=\mathbb P^\omega$);
(b) a description of the irreducible components of the admissible locus for general $k>\omega$;
(c) a hardness reduction (from which source problem, and how to preserve the shared $R$-dependence);
(d) an equivalence or barrier result identifying DEC with a known problem (AZE, regular subpencil
completion, min-rank completion), then importing known complexity.

**Question 2 — candidate ideas; are they sensible?**

(i) *Induction on $k-\omega$.* For $k-\omega=1$ the Grassmannian is a projective space; perhaps the
compatible fibre is a $\mathbb P^1$-bundle and the spectral condition reduces to one univariate polynomial
whose roots can be analysed. Then add one dimension at a time. Is such a peeling argument plausible, or is
there a known obstruction?

(ii) *Hardness in the free case.* When $\ker T=0$, the bottom-row map is surjective, so the problem becomes a
matrix completion: given the top blocks and $m$ free rows, does an affine family of $q\times\omega$ pencils
contain a good member? At general $(q,\omega)$ this looks like an affine-space full-rank problem. Is a
hardness reduction from a known problem (AZE, or quadratic feasibility) available there, or does the rank
condition make the free case tractable?

(iii) *Stratify by the normal rank of the fixed pencil.* The free-fibre criterion suggests that the relevant
invariant is the normal rank $\rho$ (and the proportionality type), not the dimension of $E+F_0$. Could the
constrained case be decided by a finite stratification according to $\rho$ and the rank of the compatibility
map, with a generic gcd computed on each stratum? Is that the right algorithmic template?

(iv) *A direct reduction from quadratic feasibility.* The block criterion is bilinear in the entries of $Z$,
and $Z$ depends affinely on $R$. Could a free regime encode a quadratic feasibility problem (QES /
$\exists\mathbb R$) directly? What is the main obstruction you would expect?

**Question 3 — next deliverable.** Would you make the next deliverable (i) the general constrained criterion,
(ii) a paper package consisting of the corrected RP theorem, the free-fibre theorem and the constrained
collapse lemma (with the Lean kernel), or (iii) a first hardness attempt? What would you consider a
publishable package in the present state?

**Question 4 — references and support.** Could you point us to (i) the complexity of affine-space full-rank
or AZE-type problems, (ii) rank-metric / min-rank completion results that might serve as reduction sources,
and (iii) the precise rectangular Smith-form complexity statement? If a draft of the paper package would be
useful, we would be glad to prepare one for your review.

We would also welcome any concrete suggestion for a single computation or small theorem that would most
cheaply discriminate between the algorithmic and the hardness scenarios.
