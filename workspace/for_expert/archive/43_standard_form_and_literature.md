# The standard complexity formulation, the literature we found, and one sharp covering question

This report does three things: it states the complexity problem in the form we now regard as standard, it records
the literature we located by shape, and it reduces the remaining difficulty to one question about a
one-parameter family of affine subspaces.

---

# Part I. The standard formulation

## I.1 Decision problems

For rational data $A,C,L_0$ and a given $q$:
$$\mathrm{REAL\text{-}AUG}(q):\quad\exists R\in\mathbb R^{(q-r)\times n}\ \text{with }(5a),(5b);$$
$$\mathrm{REAL\text{-}AUG}_\omega(q):\quad \text{the same, together with }\operatorname{rank}H(R)=\omega .$$
Then
$$\mathrm{REAL\text{-}AUG}(q)\iff\bigvee_{\omega=0}^{\min(q,k)}\mathrm{REAL\text{-}AUG}_\omega(q),$$
with the $\omega=0$ branch handled separately.

## I.2 Algebraic form of each branch

For fixed $\omega\ge1$, by the central theorem the branch is equivalent to the real solvability of
$$H(R)=UV,\qquad H_A(R)=GV,\qquad JU=I_\omega,\qquad VZ=I_\omega,\qquad X(\lambda)(\lambda U-G)=I_\omega,$$
with $\deg X\le2\omega-2$, all unknowns real. The system has $(2\omega-1)\omega q+O(\omega^2+qr)$ unknowns and
**every equation is bilinear** in the joint unknowns.

## I.3 Where the problem sits

| Problem | shape | known complexity |
|---|---|---|
| linear feasibility | linear | in $\mathrm{P}$ |
| **REAL-AUG** | bilinear **equalities** | unknown; in $\exists\mathbb R$ |
| bilinear matrix inequality feasibility | bilinear inequalities | **NP-hard** (Toker–Özbay, ACC 1995) |
| quadratic equation systems (QES) | general quadratic | $\exists\mathbb R$-complete (Blum–Shub–Smale; compendium arXiv:2407.18006) |

So the problem lies between linear feasibility and BMI feasibility. Our family is more constrained than a
general BMI (the two factors share $\mathcal L(R)$, $U$ is forced to have full column rank, and $X$ has a
staircase structure), which is why we have not assumed hardness.

---

# Part II. What we can decide, and the gap

## II.1 For a fixed $R$: polynomial time

The spectral condition is a univariate gcd test; everything is elementary.

## II.2 The bad set as a family of affine subspaces

The $\omega$-minors $p_i(R,\lambda)$ are affine in $R$ and of degree at most $\omega$ in $\lambda$. Hence the
condition "all $p_i(R,\lambda)=0$" is a **linear** system in $R$,
$$L(\lambda)R=b(\lambda),$$
and
$$\mathcal B=\bigcup_{\lambda\in\mathbb C}A(\lambda),\qquad A(\lambda)=\{R:L(\lambda)R=b(\lambda)\},$$
a one-parameter family of affine subspaces of $\mathbb R^N$, $N=(q-r)n$.

## II.3 What this decides

Since $\dim\bigcup_\lambda A(\lambda)\le\max_\lambda\dim A(\lambda)+1$:

* if $\max_\lambda\dim A(\lambda)\le N-2$, then $\mathcal B\ne\mathbb R^N$ and a feasible $R$ exists (indeed the
  feasible set is open dense);
* if $\max_\lambda\dim A(\lambda)=N$, then $\mathcal B=\mathbb R^N$ and no feasible $R$ exists.

Both tests reduce to comparing ranks along $\lambda$, i.e. to univariate gcd computations, hence are in
polynomial time.

## II.4 The gap

$$\boxed{\max_{\lambda}\dim A(\lambda)=N-1}$$

In this critical case $\mathcal B$ is a union of affine hyperplanes (or of affine subspaces of codimension one)
indexed by $\lambda$, and it may or may not cover $\mathbb R^N$. Everything we cannot decide lies here.

**Question 1.** Is there a known criterion for whether a one-parameter family of affine hyperplanes
$A(\lambda)=\{R:L(\lambda)R=b(\lambda)\}$, with $L,b$ polynomial in $\lambda$, covers the whole ambient space? We
can decide the "generic" cases by ranks; we do not know how to decide the critical one. In particular, is the
covering property equivalent to some finite, computable condition (for instance, to the vanishing of a resultant
of the family, or to a statement about the pencil $L(\lambda)$ being a "constant-rank" family)?

**Question 2.** If the answer to Question 1 is negative in general, is it known for the special shape arising
here — namely $L(\lambda)$ built from the $\omega$-minors of a pencil $\lambda H-H_A$ whose coefficients are
affine in $R$? We expect this shape to be much more rigid than a general family.

---

# Part III. Literature located, and a request

## III.1 What we found by shape

* **Toker & Özbay, ACC 1995**: solving bilinear matrix inequalities and simultaneous stabilization with static
  output feedback is NP-hard. This is the closest hardness result we know for a bilinear feasibility problem in
  control.
* **Blum–Shub–Smale (1998)**: the existential theory of the reals, containing quadratic feasibility.
* **Schaefer–Cardinal–Miltzow compendium (arXiv:2407.18006)**: records the $\exists\mathbb R$-completeness of
  quadratic equation systems, which is the natural upper bound for us.
* Earlier, from the control side: Löfberg (arXiv:2609.16886) on static output feedback, and the two Fernando
  papers on minimum-order functional observers.

## III.2 What we would like to know

**Question 3.** Are there papers on the following, which we have not been able to locate?

* deciding whether a **parametric family** of linear systems $L(\lambda)R=b(\lambda)$ is solvable for some
  parameter value (not for all values) — i.e. the existential, rather than the universal, parametric linear
  problem;
* the complexity of **bilinear matrix equalities** (rather than inequalities), which is our shape;
* "parametric determinantal" or "parametric rank" decision problems where the parameter is one-dimensional and
  the matrix entries are affine in the design variables;
* any control-theoretic literature on **minimum-order observer existence as a decision problem**, as opposed to
  constructive algorithms.

**Question 4.** Given the formulation in Part I, would you recommend attacking the critical case in II.4
directly, or instead attempting a reduction from a bilinear-equality problem to REAL-AUG? Our own reading is that
the second is more likely to succeed, because the first has resisted two attempts (charts, and the dimension
bound above).

**Question 5.** Is there any additional literature you would recommend for the observer problem itself —
something we may have missed because we searched by shape rather than by name?
