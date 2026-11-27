# Problem, established results, and open requests

This document is self-contained: it states the problem, reports what has been established, and lists
the points on which assistance is requested. No external references are needed to read it.

---

# Part I. The problem and its standard forms

## I.1 The decision problem

Let $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$ be given.
For an integer $q\ge r$ and a matrix $\mathcal L\in\mathbb C^{q\times n}$ with
$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$, consider the two conditions

$$(5a)\quad \operatorname{rank}[\mathcal LA;\;\mathcal L;\;CA;\;C]=\operatorname{rank}[\mathcal L;\;CA;\;C],$$

$$(5b)\quad \operatorname{rank}[\lambda\mathcal L-\mathcal LA;\;CA;\;C]=\operatorname{rank}[\mathcal L;\;CA;\;C]\quad\text{for every }\lambda\in\mathbb C .$$

Problem **MIN**: determine $q_{\min}(A,C,L_0)=\min\{q:\ \exists\,\mathcal L\ (q\times n)\ \text{satisfying }(5a)\text{ and }(5b)\}$.
Problem **q1**: is the computation of $q_{\min}$ polynomial-time, or is the decision version NP-hard?

Equivalently, with $q$ fixed: **DEC($q$)**: does there exist $\mathcal L$ ($q$ rows, containing $L_0$) satisfying both conditions?

## I.2 What is already known in the literature

Two 2026 papers by Fernando give a complete *characterisation* (not a complexity result).
Restated in the notation above:

* the admissible orders form a spectrum $\Sigma\subseteq[q_0,\,n_0-p]$ with
  $q_0=\sum_{j=1}^{r}\eta_j$, where $\eta_j$ are the functional observability indices of $(A,C,L_0)$;
* for each order the existence problem is equivalent to the existence of a subspace $Z$ (or, in chart
  form, of a chart $I$ and a parameter $\Theta$) satisfying an algebraic condition and a spectral
  condition;
* the algebraic condition is exactly $(5a)$; it has an explicit construction of a minimum-order
  augmentation and a complete description, up to row equivalence, of all augmentations attaining $q_0$;
* therefore $\min\Sigma$ equals $q_0$ precisely when some member of that complete family satisfies $(5b)$.

Consequently the only part not settled by the literature is the **complexity** of the fixed-order
feasibility problem, i.e. of deciding whether some member of the family satisfies $(5b)$.

## I.3 Equivalent forms of $(5b)$ used below

For a fixed $\mathcal L$ the following are equivalent; all are stated here in self-contained form.

1. **Constant rank.** The pencil $Q_{\mathcal L}(\lambda)=[\lambda\mathcal L-\mathcal LA;\;CA;\;C]$ has rank
   $h:=\operatorname{rank}[\mathcal L;CA;C]$ for every $\lambda$; equivalently $Q_{\mathcal L}$ has no
   finite elementary divisor, i.e. its rank never drops below its normal rank $h$.
2. **Determinantal divisor.** Every maximal minor of $Q_{\mathcal L}(\lambda)$ being a polynomial in
   $\lambda$, $(5b)$ holds if and only if the gcd of all $h\times h$ minors of $Q_{\mathcal L}$ is a
   nonzero constant (equivalently, the determinant divisor $\Delta_h$ has degree $0$).
3. **Smith form.** Equivalently, all invariant factors of $Q_{\mathcal L}(\lambda)$ over $\mathbb C[\lambda]$
   are units.
4. **Factorisation.** If $(5a)$ holds, there are constant matrices $\Lambda,G_0,G_1$ with
   $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$; hence
   $Q_{\mathcal L}(\lambda)=(\lambda I-\Lambda)H$ with $H=[\mathcal L;CA;C]$, and
   $\operatorname{rank}Q_{\mathcal L}(\lambda)\le\operatorname{rank}H$ holds automatically. Condition
   $(5b)$ is the reverse inequality.

Since a Smith form of a degree-one polynomial matrix is computable in polynomial time, **for fixed
$\mathcal L$ condition $(5b)$ is decidable in polynomial time**. The difficulty, if any, lies in the
existential quantifier over $\mathcal L$ (equivalently over the chart parameter $\Theta$).

---

# Part II. Results established in this project

All statements below are either proved on paper or verified on finitely many instances by exact rational
arithmetic; the distinction is marked. "Verified $N/N$" means an exact check on $N$ instances, which is
not a proof.

## II.1 Deciding $(5b)$ at fixed $\mathcal L$

* $(5b)$ $\iff$ the gcd of all $h\times h$ minors is a nonzero constant $\iff$ all invariant factors are
  units (Part I.3). (Proved; implemented with exact rational arithmetic.)
* Equivalently, with $H=[\mathcal L;CA;C]$ and $\Lambda$ the matrix characterised by $(5a)$, one has
  $Q_{\mathcal L}=(\lambda I-\Lambda)H$ and $(5b)$ is the statement that $\det(\lambda I-\Lambda)$ does not
  cause a rank drop, i.e. that the finite spectrum of $Q_{\mathcal L}$ is empty. (Proved.)
* Conclusion: the quantifier over $\lambda$ is eliminated; the remaining content of DEC($q$) is
  existential over a continuous parameter.

## II.2 Regions in which the decision is settled

| region | criterion (proved) |
|---|---|
| $\rho=\dim\pi(\mathcal V)=0$ | $(5b)$ holds automatically |
| $\rho=d$ (top layer) | $(5b)$ $\iff$ the pair $(D_W^{\mathsf T},T_W)$ is observable (PBH test) |
| $\mathcal V=\mathbb C^n$ | $(5b)$ $\iff$ $A^{\mathsf T}$ has no eigenvector in $\ker[C;CA]$ |
| $c_0=1$, $\rho=d$ | $(5b)$ $\iff$ $v_W$ is a cyclic vector of $T_W$ |
| $(\rho,c)=(2,1)$ | the pencil has three $2\times2$ minors; the auxiliary parameter $\tau$ is eliminated by linear algebra; the criterion is that their gcd be constant |
| $(\rho,c)=(3,1)$, single cell | whether the cell admits a feasible member is decided by $\mu=\dim(B\cap\mathcal U)$ |

In these regions the decision is polynomial. The intermediate layers $0<\rho<d$ in general are open at the
layer level.

## II.3 Structural obstacles

1. **Rank barrier.** If a layer $(\rho,c)$ is feasible then
   $\rho\le r(\lambda):=\dim\pi(\mathbb C^n(\lambda I-A))$ for every $\lambda$; consequently
   $\min_\lambda r(\lambda)<\rho_{ci}$ implies that no solution exists. (Proved; 1484 exact checks.)
2. **Complementary obstruction.** If $\ker C=\mathcal V\oplus Z$ with $\dim V\ge1$, then $(5b)$ fails for
   every $Z$ satisfying $(5a)$. This requires the two conditions "number of columns equals $h$" and
   "$h=n-p$" simultaneously; the earlier unconditional version of this statement is false (a counterexample
   with a wide pencil exists).
3. **Non-monotonicity.** Feasibility at order $q$ does not imply feasibility at order $q+1$; the set of
   admissible orders is not an interval. Hence binary search is unavailable and the continuous parameters
   cannot be replaced by integer conditions.

## II.4 Complexity

* **Upper bound (proved).** DEC($q$) belongs to the existential theory of the reals $\exists\mathbb R$,
  via a chart-free encoding with $O(n^3)$ variables and equations and degree $\le n$, with no disjunction
  over charts.
* **Lower bound.** Unknown: neither $\exists\mathbb R$-hardness nor NP-hardness is established.
* **Encoding size.** Three items required for a completeness statement are not established: the number of
  constraints, the bit size of the coefficients, and the polynomial representation of the rank condition.

## II.5 Structure of the pencil for arbitrary $\mathcal L$ satisfying $(5a)$

The following four statements are proved under $(5a)$ alone; none of them uses $(5b)$. They describe the
Kronecker invariants of $Q_{\mathcal L}$ (normal rank $h$, left minimal indices $\varepsilon_j$, right
minimal indices $\eta_i$, total degree of infinite elementary divisors $d_\infty$, total degree of finite
elementary divisors $d_{\rm fin}$).

1. **Right indices.** Every right minimal index of $Q_{\mathcal L}$ is $0$; the polynomial right null
   module of $Q_{\mathcal L}$ equals $N\otimes\mathbb C[\lambda]$ with
   $N=\ker\mathcal L\cap\ker\mathcal LA\cap\ker C\cap\ker CA$.
   *Proof.* Expand a polynomial null vector $v(\lambda)=\sum_{k\le d}\lambda^kv_k$. The coefficients satisfy
   $\mathcal LA v_0=0$, $\mathcal L v_k=\mathcal LA v_{k+1}$ for $k<d$, $\mathcal L v_d=0$ and
   $Cv_k=CAv_k=0$. From $(5a)$ written as $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ one gets
   $\mathcal LA v_d=0$; so $v_d\in N$. Subtracting $\lambda^dv_d$ and inducting on $d$ finishes the proof.
   (Proved; exact verification on 150 instances; a Lean kernel covers the coefficient induction.)
2. **Infinite divisors.** Every infinite elementary divisor of $Q_{\mathcal L}$ has degree one and
   $d_\infty=h-\operatorname{rank}\mathcal L$.
   *Proof.* By $(5a)$, $Q_{\mathcal L}$ is strictly equivalent (constant invertible row operations) to
   $M(\lambda)=[(\lambda I-\Lambda)\mathcal L;CA;C]$. The infinite elementary divisors of $M$ are the
   elementary divisors at $\mu=0$ of the reversed pencil
   $[(I-\mu\Lambda)\mathcal L;\mu CA;\mu C]$; since $I-\mu\Lambda$ is invertible over the local ring
   $\mathbb C[\mu]_{(\mu)}$, this pencil is locally equivalent to $[\mathcal L;\mu CA;\mu C]$. Its
   determinantal divisors satisfy $\Delta_k=c_k$ for $k\le\operatorname{rank}\mathcal L$ and
   $\Delta_k=c_k\mu^{k-\operatorname{rank}\mathcal L}$ for $\operatorname{rank}\mathcal L<k\le h$ with
   $c_k\ne0$; hence the invariant factors are $\operatorname{rank}\mathcal L$ units followed by
   $h-\operatorname{rank}\mathcal L$ copies of $\mu$. (Proved; exact verification on 151 instances,
   43 of which fail $(5b)$; a Lean kernel covers the factorisation step.)
3. **Left indices and $(5b)$.** With the global identity
   $\sum_i\eta_i+\sum_j\varepsilon_j+d_{\rm fin}+d_\infty=h$ and the two statements above,
   $$\sum_j\varepsilon_j=\operatorname{rank}\mathcal L-d_{\rm fin}.$$
   In particular
   $$(5b)\iff d_{\rm fin}=0\iff \sum_j\varepsilon_j=\operatorname{rank}\mathcal L .$$
   This replaces the quantifier over $\lambda$ by a single equality between Kronecker invariants.
   (Proved as a corollary.)
4. **Descriptor form of the left indices.** Let $J$ be a full-row-rank matrix with
   $\ker J=\ker H^{\mathsf T}$, and let $\Lambda$ be as above. Then
   $$R(\lambda)=J\,\operatorname{diag}(\lambda I-\Lambda,I,I)^{\mathsf T}=[\lambda E-E\Lambda^{\mathsf T}\ \,B]$$
   with $E=J_1$, $B=[J_2\ J_3]$ (block partition $J=[J_1\ J_2\ J_3]$) satisfies
   $\operatorname{rank}E=\operatorname{rank}\mathcal L$, and
   $$\{\text{right minimal indices of }R\}=\{\text{left minimal indices of }Q_{\mathcal L}\}.$$
   *Proof.* $R(\lambda)y=0\iff JD(\lambda)^{\mathsf T}y=0\iff D(\lambda)^{\mathsf T}y\in\ker J=\ker H^{\mathsf T}
   \iff H^{\mathsf T}D(\lambda)^{\mathsf T}y=0\iff Q'(\lambda)^{\mathsf T}y=0$ with $Q'=D(\lambda)H$, which is
   strictly equivalent to $Q_{\mathcal L}$. (Proved; exact verification on 66 instances.)
   In the terminology of descriptor systems, the right Kronecker indices of $[\lambda E-F\ \,B]$ are the
   controllability indices of the system $(\lambda E-F,B)$; hence the left minimal indices of
   $Q_{\mathcal L}$ are the controllability indices of the descriptor system
   $(-E,-E\Lambda^{\mathsf T},B)$.

**A family with $(5b)$ for every member.** For $L_k=[C;CA;\dots;CA^{k-1}]$ the condition $(5b)$ holds for
every $k$ and every $(A,C)$: the rows of $\lambda L_k-L_kA$ span the same space as those of
$[C;\dots;CA^k]$ for $\lambda\ne0$, and the same space at $\lambda=0$. The condition $(5a)$ for this family
holds exactly when $CA^k\in\operatorname{row}[C;\dots;CA^{k-1}]$ (for $k\ge2$). (Proved.)

## II.6 Corrections made

Six statements previously asserted in this project were found false and are retracted; they are listed
here because they determine which formulations should not be used:

1. "$h=n-p$ implies $(5b)$ fails" — false; counterexample with a wide pencil.
2. The order-spectrum is an interval — false; feasibility is not monotone in $q$.
3. Constant rank implies all right minimal indices vanish — false; the pencil $[\lambda\ \ 1]$ has constant
   rank $1$ and right index $1$.
4. $d_\infty=h-\operatorname{rank}\mathcal L$ is equivalent to $\ker\mathcal L=N$ — false; the correct
   statement is $d_\infty=\dim(\ker\mathcal L/N)$.
5. $d_\infty$ is the sum of the polynomial degrees of the reversed pencil's invariant factors — false; it is
   the sum of their $\mu$-adic valuations.
6. $(5a)$ alone gives $\sum_j\varepsilon_j=\operatorname{rank}\mathcal L$ — false; the correct statement is
   $\sum_j\varepsilon_j=\operatorname{rank}\mathcal L-d_{\rm fin}$.

## II.7 Method

All computations are exact (rational arithmetic); no floating point is used in any statement above.
Kronecker data are computed by degree-truncated linear algebra (the dimension of the space of polynomial
null vectors of degree $\le d$), Smith forms by exact polynomial row/column reduction, and each
numercial statement is cross-checked by an independent route (determinant degrees for regular square
pencils, sampled ranks otherwise). The two algebraic steps of II.5.1 and II.5.2 are additionally checked
by a Lean 4 formalisation of their kernels. Instances are generated from small integer matrices and from
the known feasible configurations described in II.2.

---

# Part III. Requests

The project's remaining gaps, in the order in which they block progress.

## III.1 Complexity of the fixed-order decision

**Gap G-1.** No lower bound is known for DEC($q$): neither $\exists\mathbb R$-hardness nor NP-hardness.
An algorithm is also unknown. Any indication of which of the two directions is plausible, or of a
technique that applies, would be useful.

## III.2 Size of the encoding

**Gap G-2.** For a completeness statement one needs the number of constraints, the bit size of the
coefficients, and a polynomial representation of the rank condition. Only the first two constants of the
chart-free encoding ($O(n^3)$ variables and equations, degree $\le n$) are established; the bit size is not.

## III.3 The remaining structural freedom

**Gap G-3.** By II.5.3, $(5b)$ is equivalent to $\sum_j\varepsilon_j=\operatorname{rank}\mathcal L$. The left
minimal indices form a non-increasing sequence of length $q+2p-h$ summing to $\operatorname{rank}\mathcal L$.
Whether every such sequence is realisable is open. In 140 feasible pencils spanning 35 different aggregate
data $(q,p,h,\operatorname{rank}\mathcal L)$ no two different sequences occurred for the same data, which is
consistent with, but does not establish, the determinacy of the sequence by the aggregate data.

## III.4 Engineering gap

**Gap G-4.** Evaluating $\sum_j\varepsilon_j$ over the complete family of minimum-order augmentations
(II.2) has not been implemented; only individual members have been examined.

## III.5 Questions

1. Is the problem "decide whether a member of the complete augmentation family has a prescribed
   controllability-index sum" a known problem, and is a complexity result available for
   controllability-index assignment problems for descriptor systems?
2. Are the attainable left-minimal-index sequences of pencils of the form
   $[\lambda E-E\Lambda^{\mathsf T}\ B]$ with $[E\ B]$ of full row rank and $\operatorname{rank}E=\operatorname{rank}\mathcal L$
   characterised anywhere in the literature?
3. Is there a standard method to bound the coefficient bit size of a chart-free $\exists\mathbb R$
   encoding of a "constant rank for all $\lambda$" condition?
4. Given that II.5.2 rests on Smith forms over $\mathbb C[\mu]$, is a paper proof with exact verification on
   151 instances an acceptable permanent status, or is a formalisation of the determinantal-divisor
   argument expected?

## III.6 What is not being asked

The characterisation of existence (order spectrum, $q_0$, construction, complete family) is taken from the
literature and is not part of the project's aims. The project does not claim any of the
above results as complete without the stated verification; the only exception is the classical material
of Part I.2.
