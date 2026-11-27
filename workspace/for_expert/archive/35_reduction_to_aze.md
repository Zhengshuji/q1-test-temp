# $q1$: a reduction to affine pencil zero exclusion, and a request for references

This report continues the $q1$ programme only. It has one new mathematical content — a reduction of the
observer decision problem to a standard problem about affine matrix pencils — and one request: references on
the complexity of that standard problem.

---

# Part I. Setting

Given $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$, $q\ge r$,
let $\mathcal L=\begin{bmatrix}L_0\\R\end{bmatrix}$ and require

$$(5a)\ \operatorname{rank}\begin{bmatrix}\mathcal LA\\ \mathcal L\\ CA\\ C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}\mathcal L\\ CA\\ C\end{bmatrix},
\qquad
(5b)\ \operatorname{rank}\bigl[\lambda\mathcal L-\mathcal LA;\ CA;\ C\bigr]=h\ \ \forall\lambda\in\mathbb C .$$

$K=\ker[C;CA]$, $k=\dim K$; $N_K$ a basis of $K$ as columns; $H(R)=\mathcal L(R)N_K$, $H_A(R)=\mathcal LA(R)N_K$.
The reduced criterion (established earlier) is
$$(5b)\iff\gcd\{\text{all }\omega\times\omega\text{ minors of }\lambda H(R)-H_A(R)\}\in\mathbb C^\times,
\qquad \omega=\operatorname{rank}H(R).$$
$\mathrm{DEC}(q)$: does there exist $R$ with $(5a)$ and $(5b)$? $q1$: is computing $q_{\min}$ NP-hard?

---

# Part II. New content

## II.1 The quantified set is a linear section

Both $H(R)=M(R)N_K$ and $H_A(R)=M(R)AN_K$ are determined by $M(R)=\begin{bmatrix}L_0\\R\end{bmatrix}$ and are
**linear (affine)** in $R$. Hence the family of pencil pairs we quantify over is an affine linear section of
the space of pairs $(H,H_A)\in\mathbb C^{q\times k}\times\mathbb C^{q\times k}$.

Dimension count: the parameter space has $(q-r)n$ dimensions, the pair space has $2qk$.

## II.2 Realizability lemma

**Lemma.** Assume $K\cap AK=0$. Then for **every** pair $(H,H_A)\in\mathbb C^{q\times k}\times\mathbb C^{q\times k}$
there exists $M$ with $MN_K=H$ and $MAN_K=H_A$.

*Proof.* $M|_K$ is determined by $H$ (as $N_K$ has full column rank), $M|_{AK}$ is determined by $H_A$ (as
$AN_K$ has full column rank, which is exactly $K\cap AK=0$), and the two determinations do not interfere
because $K\cap AK=0$. Extend $M$ arbitrarily off $K\oplus AK$. $\square$

So in the region where this applies, our family is not a thin section: it is the whole space of pencil pairs
with the first $r$ rows fixed by $L_0$.

## II.3 When is $K\cap AK=0$ compatible with $K=\ker[C;CA]$?

Necessarily $K\subseteq\ker C$ and $AK\subseteq\ker C$ and $K\cap AK=0$, hence
$$\dim\ker C\ \ge\ 2k,\qquad\text{i.e.}\qquad n-p\ \ge\ 2k .$$

**Explicit construction at the borderline $n-p=2k$** ($n=6$, $p=2$, $k=2$): take $K=\langle e_1,e_2\rangle$,
$$C=\begin{pmatrix}0&0&1&0&0&0\\0&0&0&1&0&0\end{pmatrix},\qquad
A:\ e_1\mapsto e_5,\quad e_2\mapsto e_6,\quad e_5\mapsto e_3,\quad e_6\mapsto e_4,\quad e_3,e_4\mapsto 0 .$$
Then $\ker C=\langle e_1,e_2,e_5,e_6\rangle$, $AK=\langle e_5,e_6\rangle\subseteq\ker C$, $K\cap AK=0$, and
$\operatorname{rank}[C;CA]=4=n-k$, so indeed $K=\ker[C;CA]$.

Computed check (exact rational arithmetic): $\operatorname{rank}[C;CA]=4$; $\dim K=2$; $\dim(K\cap AK)=0$;
and for twenty random target pairs $(H,H_A)\in(\mathbb Q^{3\times2})^2$ the system $MN_K=H$, $MAN_K=H_A$ was
solvable in all twenty cases.

## II.4 Consequence: a conditional reduction

Let AZE be the problem: given an affine linear family of pencils $\lambda H-H_A$ (with $H$ of full column
normal rank), does there exist a member with no finite complex rank drop?

Then, in the region $n-p\ge 2k$,
$$\text{AZE is hard}\ \Longrightarrow\ \mathrm{DEC}(q)\text{ is hard},$$
because every AZE instance whose first $r$ rows are fixed can be realized by observer data as above. In the
complementary region $n-p<2k$, $K\cap AK\neq 0$ is forced, so the pair must satisfy linear relations and the
family is a thin section; hardness of AZE does not transfer there.

This does not yet say anything about $q1$'s truth, but it changes the status of the difficulty: it is no longer
a private property of the observer pencil.

## II.5 Two corrections recorded

1. A first attempt used $A$ defined by rows instead of columns, which produced $A e_1=e_3\notin\ker C$; the
   computed check gave $K\cap AK$ of dimension $2$ and zero solvable target pairs. The construction and its
   condition were corrected to the version above.
2. The naive condition $k\le n/2$ is not the right one; the correct necessary condition is $n-p\ge 2k$. In
   particular the small instance used in earlier reports ($n=4$, $p=1$, $k=2$) does **not** satisfy it and
   therefore lies outside the reducible region.

---

# Part III. Questions

**Question 1.** Is the realizability lemma and its consequence used correctly? In particular: is it legitimate
to fix the first $r$ rows (by $L_0$) and still claim that "all" AZE instances are realized, or must the
reduction also produce the fixed row as part of the construction? We believe the fixed row can be absorbed
into the AZE instance, but we would like this checked.

**Question 2.** Does the reduction need to control all strata and charts, in the sense you warned about
earlier? Our reduction produces a *single* instance, not a family of charts; but the observer instance has
several rank strata, and a feasible candidate might exist in a stratum that the AZE instance does not exclude.
If so, the reduction as stated is incomplete, and we would like to know the minimal extra condition needed.

**Question 3.** Subject to Questions 1–2: what is known about the complexity of AZE — existence of a member of
an affine family of matrix pencils with no finite complex rank drop (equivalently, with constant maximal
determinantal divisor)? We are interested in

* NP-hardness or $\exists\mathbb R$-hardness results;
* polynomial-time algorithms for structured families (e.g. when the number of parameters is fixed, or when the
  pencil is square);
* any survey that states the problem in this form.

We have not been able to locate a complexity statement for this problem; the literature we found treats
Kronecker/Popov forms structurally rather than decision-theoretically. If the problem is known to be open, that
is itself useful information for us.
