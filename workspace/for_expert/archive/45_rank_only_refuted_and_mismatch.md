# The rank-only conjecture fails at $\omega\ge2$: where the difficulty can live, and one mismatch to exploit

This report records one refutation, one structural observation, and one mismatch that we believe is the right thing
to attack.

---

# Part I. Setting

$K=\ker[C;CA]$, $k=\dim K$, $N_K$ a basis; $H(R)=\mathcal L(R)N_K$, $H_A(R)=\mathcal LA(R)N_K$; $\omega$ fixed;
$\mathcal X_\omega$ the admissible locus $\{\operatorname{rank}H=\omega,\ \operatorname{rank}[H;H_A]=\omega\}$;
$\mathcal B_\omega$ the spectral bad locus inside it; feasibility at rank $\omega$ is
$\mathcal X_\omega\setminus\mathcal B_\omega\ne\varnothing$. The reachable pairs form a linear space, and
$\ker H\subseteq\ker H_A$ is equivalent to $\operatorname{row}H_A\subseteq\operatorname{row}H$.

---

# Part II. Three items

## II.1 The rank-only conjecture, refuted at $\omega\ge2$

At $\omega=1$ the criterion is $\operatorname{rank}[H\ H_A]=2$ (as established previously), so feasibility is a
rank condition. We tested $\omega=2$: take $q=3$, $k=2$, $U=\begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix}$ fixed, and
enumerate $G\in\{-1,0,1\}^{3\times2}$, grouping by the rank invariants
$$\bigl(\operatorname{rank}U,\ \operatorname{rank}G,\ \operatorname{rank}[U\ G],\
\operatorname{rank}[U;G]\bigr).$$
Within the single group $(2,2,3,2)$ there are **464 feasible and 112 infeasible** choices. A minimal pair differing
in one entry:
$$G_a=\begin{pmatrix}-1&-1\\-1&-1\\-1&0\end{pmatrix}\ \text{gives}\ \gcd=1\ (\text{feasible}),\qquad
G_b=\begin{pmatrix}-1&-1\\-1&-1\\-1&1\end{pmatrix}\ \text{gives}\ \gcd=\lambda+2\ (\text{infeasible}).$$
So feasibility at $\omega=2$ is **not** a rank condition. The conjecture that feasibility is decidable by rank
computations therefore fails at $\omega\ge2$; it survives only at $\omega\le1$.

## II.2 The shape of the spectral condition at $\omega=2$

The $\omega$-minors of $P=\lambda U-G$ come in two kinds: those using only the "active" rows of $U$ have degree
$\omega$ in $\lambda$, while those using an inactive row have lower degree. At $\omega=2$, $q=3$ this gives
$$1\ \text{quadratic in }\lambda\ +\ (q-2)\ \text{linear in }\lambda.$$
The bad condition is that these share a common root: a determinantal condition for the linear part, together with
the vanishing of the quadratic there.

Because $G$'s entries are affine in $R$, the coefficients of these minors contain **products** $g_{ij}g_{kl}$, i.e.
they are quadratic in $R$. This is exactly why ranks do not suffice: the bad condition involves products of design
variables.

## II.3 The mismatch we intend to attack

$$\boxed{\text{the reachable set of }G\ \text{is \textbf{linear},\qquad the bad condition is \textbf{quadratic}.}}$$
The reachable set is defined by the linear compatibility relations $B_1Z_1+B_2Z_2=0$ (established earlier); the bad
condition is defined by polynomial equations of degree two in $R$.

So the decision problem at $\omega=2$ has the following clean shape:

> **Given a linear subspace $\Lambda$ of pencils $\lambda U-G$ (of the special form induced by the observer data),
> is $\Lambda$ contained in the set of pencils that drop rank at some finite $\lambda$?**

We can decide the question for a *single* pencil (univariate gcd), and we can decide it when the codimension
argument applies. The hard part is the interaction of a linear $\Lambda$ with a quadratic condition.

---

# Part III. Questions

**Question 1.** Is the decision problem just displayed a known one? We would state it as: given a linear subspace
of matrix pencils, does every member fail to be regular? Or, contrapositively, does the subspace contain a regular
pencil? We have not found a complexity statement for this in the literature; if it is known, or known to be open,
that would settle which way to aim.

**Question 2.** If it is open, which side would you attack at $\omega=2$? Two concrete sub-questions:

* *Algorithm side.* Since $q=3$ gives one quadratic and $(q-2)$ linears, the bad condition is the vanishing of a
  resultant of a quadratic and a linear, subject to the linear compatibility constraints. Is there a normal form
  for "linear subspace of pencils" that makes rank-drops decidable by linear algebra alone, for instance a
  Kronecker-form stratification of the subspace rather than of a single pencil?
* *Hardness side.* Would you try to encode a two-variable quadratic feasibility problem into the pair
  (linear compatibility constraints, quadratic bad condition)? If so, would you start from the minimal case
  $\omega=2$, $q=3$, $k=2$, where explicit computations are still possible, or from a family with more parameters?

**Question 3.** Given the refutation in II.1, does the balance of evidence now favour hardness rather than
tractability? Our own reading has changed twice in the last few exchanges, and we would like an outside view on
which way the evidence points, with the caveat that no reduction exists yet.

**Question 4.** Of the five stages in your last plan, we have begun stage 2 (componentwise classification) and
finished the rank-only test of stage 3 (refuted). Would you now prioritize the componentwise symbolic computations
(stage 2) or the encoding attempt at $\omega=2$ (stage 4)?
