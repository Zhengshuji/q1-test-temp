# Three formulations, four new results, and a request for a plan

This report has three parts. Part I fixes the formulation: the original question is to **produce the design**, not
only the optimal order. Part II records four results obtained since the last report. Part III asks what it would
take to finish the problem, and what general plan you would advise for the project as a whole.

---

# Part I. Formulations

Given $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$, one seeks a matrix
$R\in\mathbb C^{(q-r)\times n}$ such that $\mathcal L=\binom{L_0}{R}$ ($q$ rows, full row rank) satisfies
$$(5a)\ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\ \forall\lambda .$$

Three formulations must be distinguished:

$$\begin{aligned}
\mathrm{DEC}(q):\quad&\text{given }(A,C,L_0)\text{ and }q,\ \text{decide whether such an }R\text{ exists};\\
\mathrm{OPT}:\quad&\text{compute }q_{\min}=\min\{q:\mathrm{DEC}(q)\};\\
\mathrm{FIND}:\quad&\text{output an actual }R\text{ at the minimal order, with a certificate of minimality}.
\end{aligned}$$

Since a full-row-rank $\mathcal L$ has $q\le n$, the candidate set is finite of size $n-r+1$, and
$$\mathrm{FIND}\ \ge\ \mathrm{OPT}\ \equiv\ \mathrm{DEC}$$
by binary search. The step $\mathrm{OPT}\Rightarrow\mathrm{FIND}$ requires the decision procedure to be
**constructive**: it must return the stratum or the subspace that witnesses existence. The Grassmannian criterion
stated in the previous round is constructive, so inside its range of applicability
$$\mathrm{FIND}\equiv\mathrm{DEC}.$$

Two burdens are specific to $\mathrm{FIND}$:

1. **Output representation.** $\mathrm{DEC}$ answers yes or no; $\mathrm{FIND}$ must emit a matrix, so the output
   field and the bit length must be declared. Moreover a real witness does not imply a rational one: for
   $A=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ there is a complex but not a rational invariant subspace. So the
   answer to $\mathrm{FIND}$ can depend on the declared output field, whereas $\mathrm{DEC}$ over $\mathbb C$ does
   not face this.
2. **Constructivity.** A non-constructive decision algorithm gives no witness.

We have therefore restated the problem in three lines and will state any hardness claim against
$\mathrm{DEC}$; our previous statements named only $\mathrm{OPT}$.

---

# Part II. Four results since the last report

## II.1 The Grassmannian criterion, implemented

The criterion was implemented exactly (rational arithmetic, no computer-algebra system). For an instance with
$n=5$, $p=1$, $q=3$, $r=1$, $K=\langle e_2,e_3\rangle$, $L_0=e_4^{\mathsf T}$:
$$E=\operatorname{row}(0,1),\qquad F_0=\operatorname{row}(1,0),\qquad
Z_1=\begin{pmatrix}0&-1\\-1&0\end{pmatrix},\qquad Z_2=I_2 .$$
Of the projective candidates for $S$, exactly two satisfy the criterion, $\sigma=(1,1,0)$ and $\sigma=(1,-1,0)$.
So the rank-two admissible stratum is nonempty but consists of two one-parameter families only. This explains why
six earlier attempts to find admissible points by sampling in the $R$-space returned nothing: the stratum
corresponds to two discrete points of the Grassmannian.

Recovering $R$ from $S$ then failed at first, because of three convention errors on our side (the columns rather
than the rows of $N_K$ are the basis; the top row $L_0AN_K=0$ is still a row; the minors must range over all
pairs of columns). After these were fixed, the recovery succeeded, which independently confirms the exact
fixed-row image theorem.

## II.2 A stratum can be entirely bad, and this can be proved by a scaling argument

For the same instance, each admissible $S$ carries a free scalar $t$, and the recovered solution satisfies
$R(t)=tR(1)$. The top blocks are independent of $t$, so every $\omega$-minor of $P(t,\lambda)=\lambda H(t)-H_A(t)$
equals $t^{s}$ times the corresponding minor at $t=1$. Since $t$ is a unit in $\mathbb Q(t)$,
$$\deg_\lambda\gcd_{\mathbb Q(t)[\lambda]}\{\text{minors}\}=\deg_\lambda\gcd\text{ at }t=1=2>0,$$
so the whole family is bad. This is a short and reusable argument: **a stratum that degenerates to a scaling ray is
uniformly bad**.

## II.3 Correction: a bad stratum does not make the instance infeasible

We had treated II.2 as a hardness target. It is not. For the same instance the rank-one stratum is feasible: take
$B_1$ and $B_2$ with rows in the span of $(0,0,1)$, which is admissible and satisfies the rank criterion
$\operatorname{rank}[H\ H_A]=2$; a direct computation gives $q_{\min}=2$ for that instance.

$$\boxed{\text{"some stratum is admissible but entirely bad" does \textbf{not} imply infeasibility}}$$

Feasibility may be supplied by a lower stratum. Hardness would require **every** stratum to be infeasible
(empty or entirely bad), which is exactly what the definition of $q_{\min}$ demands. This is a genuine weakening
of the previous round's conclusion and we record it as such.

## II.4 A first provable lower bound: $q_{\min}\ge4$ for a concrete instance

Take $n=4$, $p=1$, $r=1$, $C=e_1^{\mathsf T}$,
$$A=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&1&0&0\\0&0&0&0\end{pmatrix},\qquad L_0=e_3^{\mathsf T},$$
so $K=\langle e_2,e_3\rangle$, $k=2$. Then:

* $q=2$. The stratum $\omega=0$ is empty since $E\ne0$; the stratum $\omega=1$ is empty because
  $\dim(E+F_0)=2>1=\omega$ (necessary condition N1); the stratum $\omega=2=q$ is a square pencil and therefore
  fails. So $q=2$ is infeasible, by structural conditions rather than by enumeration.
* $q=3$. The strata $\omega=0,1$ are empty as above. For $\omega=2$ the Grassmannian criterion is satisfied, so
  the stratum is nonempty; but $F_0=-EZ_1$ and the compatibility relation gives $B_2=-B_1Z_1$, hence
  $$H_A=\begin{bmatrix}F_0\\B_2\end{bmatrix}=-HZ_1\qquad\text{identically on the stratum},$$
  and therefore $P(\lambda)=H(\lambda I+Z_1)$. Since $Z_1$ has eigenvalue $-1$, the factor $I+Z_1$ is singular and
  $\operatorname{rank}P(1)<\omega$. **Every admissible point of that stratum is bad**, so $q=3$ is infeasible.

$$\boxed{q_{\min}\ge4\ \text{for this instance}}$$

The mechanism deserves emphasis: the badness is not generic-looking, it follows from a **matrix identity**
($H_A\equiv-HZ_1$) that holds because the compatibility relation is linear and the top block happens to satisfy
$F_0=-EZ_1$. The singularity then reduces to a spectral property of the fixed matrix $Z_1$.

---

# Part III. Questions

**Question 1.** Is the three-way formulation in Part I the right one to state, or would you formulate
$\mathrm{FIND}$ differently? In particular, for $\mathrm{FIND}$ we are unsure how to state the output field: if the
answer requires algebraic numbers of large height, that alone may separate $\mathrm{FIND}$ from $\mathrm{DEC}$ in
complexity terms, and we would like your view on whether that separation is worth tracking.

**Question 2.** Results II.2 and II.4 suggest a pattern: **stratum by stratum, a stratum is either empty (decided by
N1/N2 and the Grassmannian criterion) or its badness follows from an identity of the form $H_A\equiv-HZ$**. If that
pattern is general, then feasibility is decidable by (i) enumerating strata, (ii) solving the Grassmannian
condition, and (iii) testing a spectral property of a fixed matrix. Is such a general statement plausible in your
view, or do you expect strata whose badness is not of this rigid form? This is the single question that decides
whether the project should aim at an algorithm or at a hardness reduction.

**Question 3.** What would it take to finish the problem? Concretely, if the answer is "polynomial time", we would
need (a) a polynomial bound on the number of strata to examine, (b) an algorithm for the Grassmannian condition in
general $k,\omega$, and (c) a decision procedure for the spectral property; if the answer is "hard", we would need
a reduction from a known hard problem that respects the shared $R$-dependence. Which of these three components
would you attack first, and is there any of them that you consider hopeless in its current form?

**Question 4.** Finally, a question about the project as a whole. We have spent a long sequence of rounds on
structural results, and each one has narrowed the problem without settling it. Would you advise continuing this
layer-by-layer route, or would you advise a change of strategy — for instance proving a conditional result
("if the spectrum of $Z$ can be prescribed freely, then ..."), or isolating a small case (fixed $n$, or $k-\omega$
bounded) where the answer can be settled completely? We would value a plan that produces a definite statement,
even a conditional one, rather than further narrowing.
