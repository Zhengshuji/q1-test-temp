# Block criterion, the $q=\omega+1$ case, and a closing summary

This report records four results proved since the last exchange, one correction, and the present state of the
problem. It closes with a short account of what we think remains.

---

# Part I. Setting

$K=\ker[C;CA]$, $k=\dim K$, $N_K$ a basis; $H(R)=\mathcal L(R)N_K$, $H_A(R)=\mathcal LA(R)N_K$; $\omega$ fixed;
admissible locus $\mathcal X_\omega=\{\operatorname{rank}H=\omega,\ \ker H\subseteq\ker H_A\}$;
$\mathcal B$ the spectral bad locus (some finite $\lambda$ with a rank drop). The reduced criterion is that
$\gcd$ of the $\omega$-minors of $\lambda H-H_A$ is a nonzero constant.

Three formulations are now separated: $\mathrm{DEC}(q)$, $\mathrm{OPT}$ (the value $q_{\min}$), and $\mathrm{FIND}$
(the design itself). Since a full-row-rank $\mathcal L$ has $q\le n$, the candidate orders are finite, and
$\mathrm{FIND}\ge\mathrm{OPT}\equiv\mathrm{DEC}$ by scanning; we do **not** claim binary search, because monotonicity
of feasibility in $q$ is not proved. $\mathrm{FIND}$ carries an extra burden: the output field and bit length.

---

# Part II. Results

## II.1 Theorem A: the componentwise dichotomy

Let $X$ be an irreducible locally closed subset contained in the rank-$\omega$ admissible locus. Then either
$X\subseteq\mathcal B$, or $X\setminus\mathcal B$ is a nonempty Zariski-open dense subset of $X$; and the two cases
are distinguished by the gcd of the $\omega$-minors over $\mathbb C(X)$.

*Proof.* $\mathcal B$ is closed in $X$ by the closedness theorem. If $\mathcal B\ne X$, then $X\setminus\mathcal B$ is a
nonempty open subset of the irreducible $X$, hence dense. If $\mathcal B=X$, every point is bad. The test: $\mathcal B=X$
iff the generic point lies in $\mathcal B$ iff the minors have a common root over the algebraic closure of $\mathbb C(X)$
iff that gcd is nonconstant. $\square$

This is the statement you called Workstream A. Its consequence for the project: the **closedness** and the
**spectral test** are both available; what is missing for an algorithm is a description of the irreducible
components of the admissible locus.

## II.2 The block criterion

Suppose $(5a)$ holds on the stratum, so that $H_A=ZH$ for some $Z$ defined on $W=\operatorname{im}H$. Choose a
complement $W'$ and write $Z=\binom{A}{B}$ with $A\in\mathbb C^{\omega\times\omega}$, $B\in\mathbb C^{(q-\omega)\times\omega}$.
Then
$$\text{bad}\iff \exists\,0\ne y\in\ker B\ \text{with}\ Ay\in\operatorname{span}\{y\}.$$
*Proof.* A rank drop at $\lambda$ means $Zy=\lambda y$ for some $0\ne y\in W$. In blocks this is exactly $Ay=\lambda y$
and $By=0$. $\square$

Three consequences:

* $q=\omega$: then $W'=0$, so $B=0$ and $\ker B=W$; the condition becomes "the $\omega\times\omega$ complex matrix $A$
  has an eigenvector", which always holds. This reproves from this side that the square case is never feasible.
* $q\ge2\omega$: if $\ker B=0$ then badness is impossible. This requires $q-\omega\ge\omega$. So
  $$\ker B=0\ \Longrightarrow\ \text{feasible},$$
  provided a reachable pair with $\ker B=0$ exists; that proviso is exactly the difficulty, since $\ker B=0$ is an
  open condition and admissibility is closed.
* $\omega=1$: $B$ is a row vector and the condition reduces to $g\parallel u$, consistent with the rank criterion
  $\operatorname{rank}[H\ H_A]=2$.

## II.3 The $q=\omega+1$ case, made explicit

Here $B$ is a single row, so $\ker B$ is a hyperplane in $W$, and
$$\text{bad}\iff \text{some one-dimensional eigenspace of }A\text{ is contained in }\ker B.$$
If an eigenspace has dimension at least two, it meets the hyperplane nontrivially and the case is bad. For
$\omega=2$, $q=3$ the hyperplane is a line $\operatorname{span}\{w\}$, and
$$\boxed{\text{good}\iff\det[w,\ Aw]\ne0,}$$
that is, $w$ is not an eigenvector of $A$. Note that $A=\mu I$ gives $Aw=\mu w$ and is correctly classified as bad.

So the whole question at $q=\omega+1$ has become a single determinant in the blocks $(A,B)$ of $Z$, and the remaining
problem is whether a reachable pair can make that determinant nonzero.

## II.4 A complete obstruction instance, and a general obstruction

For the instance with
$$C=e_1^{\mathsf T},\quad L_0=e_3^{\mathsf T},\quad
A=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&1&0&0\\0&0&0&0\end{pmatrix},$$
$v_\pm=e_2\pm e_3$ are eigenvectors with $Cv_\pm=CAv_\pm=0$. If $Av=\lambda v$ with $Cv=CAv=0$, then for any $\mathcal L$
the left-hand matrix of $(5b)$ annihilates $v$; when $q=n$ and $\mathcal L$ is invertible the right-hand rank is $n$,
so $(5b)$ fails at that $\lambda$. Together with the failures at $q\le3$ this gives $q_{\min}=+\infty$: no feasible
augmentation at any order. The general statement — a $C$- and $CA$-invisible eigenvector obstructs every invertible
augmentation — is a reusable obstruction.

---

# Part III. One correction

We earlier reported a rank-one feasible stratum for one instance and concluded $q_{\min}=2$ for it. That was wrong on
two counts: the construction violated $(5a)$ (the fixed top row of $H_A$ did not lie in the row space of $H$), and we
confused the horizontal concatenation $\operatorname{rank}[H\ H_A]$ with the vertical one
$\operatorname{rank}\binom{H}{H_A}$. The Grassmannian criterion independently rules that stratum out, since
$\dim(E+F_0)=2>1=\omega$. The conclusion $q_{\min}=2$ is withdrawn; that instance is in fact infeasible at $q=2$ and
$q=3$.

We record this because it happened twice in the same form (a rank condition taken horizontal instead of vertical), and
because it shows the value of the Grassmannian criterion as an independent check.

---

# Part IV. Where the problem stands

Easy or settled: fixed $R$ (univariate gcd); $\omega=0$; $\omega=1$ (rank criterion); $k=\omega$ (the theorem of the
previous exchange, with a polynomial algorithm); $q=\omega$ (infeasible).

Open, in the order we intend to attack:

1. **Components of the admissible locus** when $k>\omega$. Theorem A then converts into an algorithm. The
   Grassmannian description is available; the compatible fibre
   $\mathcal C_S=\{(x,y)\in S\times S:\ xZ_1+yZ_2=0\}$ is where the remaining geometry lives. We would start with
   $k-\omega=1$, where $\dim\operatorname{Gr}(\omega,k)=\omega$ grows only linearly.
2. **Whether a reachable pair can make $\det[w,Aw]\ne0$** at $q=\omega+1$.
3. Only after (1) or (2) produces a component that is neither empty nor uniformly bad would we attempt a hardness
   reduction, and it would have to respect the shared $R$-dependence.

A caveat on our own numerical work: four times in this exchange a sampling experiment was inconclusive because the
target stratum had positive codimension. We now regard sampling as a witness-finder only, and construct points
instead. Every "all bad" conclusion we accept is accompanied by a matrix identity or by the Grassmannian criterion,
not by a sample.
