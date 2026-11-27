# An RP bound for k = ω, a free-fibre criterion at q = ω+1, and an all-bad constrained stratum

This report has three parts. Part I fixes the setting. Part II records three results obtained after the previous
exchange: an RP bound for the case k = ω, a necessary-and-sufficient criterion for the free fibre at
q = ω+1, ω = 2, and a proof that a constrained stratum is entirely bad. Part III asks three questions.

## Part I. Setting

Given $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$, one seeks
$R\in\mathbb C^{(q-r)\times n}$ such that $L=[L_0;R]$ (q rows, full row rank) satisfies

$$(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\quad\forall\lambda\in\mathbb C .$$

Put $K=\ker[C;CA]$ (dim k), choose a basis $N_K$, and define $H=LN_K$, $H_A=LAN_K$. For a fixed rank $\omega$,
the admissible locus is the set of $R$ with $\operatorname{rank}H=\omega$ and $\ker H\subseteq\ker H_A$; on it
the induced map $Z:W\to\mathbb C^q$, $W=\operatorname{im}H$, is defined by $Z(Hx)=H_Ax$. Choosing a complement
$\mathbb C^q=W\oplus W'$ and writing $Z=(A;B)$ gives

$$\text{bad}\iff\exists\,0\ne y\in\ker B,\ Ay\in\mathbb C y .$$

For $q=\omega+1$, $B$ is a single row and $\ker B$ is a hyperplane; for $\omega=2$ it is a line
$\ker B=\mathbb C w$, and

$$\text{good}\iff B\ne0\ \text{and}\ \det[w,Aw]\ne0 .$$

The case $B=0$ is automatically bad (then $\ker B=W$ and every complex $2\times2$ matrix has an eigenvector).

The free case is $\ker T=0$ for $T(v,w)=v+Aw$ (equivalently $K\cap A^{-1}K=0$); then the bottom rows of $H$
and $H_A$ are unconstrained, and the problem is a matrix completion. In the constrained case the compatible
pairs satisfy $xZ_1+yZ_2=0$.

## Part II. Results

### II.1 The case $k=\omega$ is in RP

**Theorem.** For rational input ($A,C,L_0$ binary rationals, $q$ unary), the decision problem
$\mathrm{DEC}_{k=\omega}(q)$ belongs to RP. It is not claimed to be in ZPP. The fixed-$(q,\omega)$
polynomial-time statement is retained and is not weakened.

*Proof.* On the rank-$k$ stratum, $\operatorname{rank}H=k$ implies $\ker H=0$, so $(5a)$ is automatic. The
domain $D=\{R:\operatorname{rank}H=k,\ \operatorname{rank}L=q\}$ is open in the affine parameter space (both
conditions say that some minor is nonzero), hence irreducible when nonempty. The bad locus $\mathcal B$ is
closed in $D$ (the closedness theorem of the previous exchange), so either $D\subseteq\mathcal B$ or
$D\setminus\mathcal B$ is a nonempty open dense subset. Thus a generic point decides the existence question.

The algorithm samples a rational point $R_0$, verifies the two rank conditions, computes the $k$-th
determinantal divisor $\Delta$ of $\lambda H(R_0)-H_A(R_0)$ over $\mathbb Q[\lambda]$, and accepts iff
$\deg\Delta=0$. It never accepts on a no-instance: if $D=\varnothing$ the rank test fails, and if
$D\subseteq\mathcal B$ every admissible sample has positive-degree gcd.

For the one-sided error bound we need a nonzero polynomial vanishing on the exceptional set. Let
$m_1,\dots,m_N$ be the $k$-minors of $\lambda H-H_A$. Each has degree at most $k$ in $\lambda$ and in $R$.
Over the function field $\mathbb Q(R)$ their gcd is $1$ on a yes-instance. We use the following lemma.

**Lemma.** Let $V_0=\operatorname{span}_{\mathbb Q}\{m_i\}$. If the gcd of all $m_i$ is $1$, then there exist
constant rational combinations $f=\sum a_i m_i$, $g=\sum b_i m_i$ with $\gcd(f,g)=1$ in $\mathbb Q(R)[\lambda]$.

*Proof.* For an irreducible $p\in\mathbb Q(R)[\lambda]$, let $V_p=\{f\in V_0:p\mid f\}$. Since some $m_i$ is
not divisible by $p$, $V_p$ is a proper $\mathbb Q$-subspace. If $\gcd(f,g)\ne1$, then some $p$ divides both,
i.e. $(f,g)\in V_p\times V_p$. A finite union of proper subspaces cannot cover $V_0\times V_0$ over the
infinite field $\mathbb Q$; choose $(f,g)$ outside. $\square$

Then $\operatorname{Res}_\lambda(f,g)$ is a nonzero polynomial in $R$. If $R_0\in\mathcal B$, then
$f(R_0,\cdot)$ and $g(R_0,\cdot)$ have a common root, so the resultant vanishes. Its total degree is at most
$2k^2$: the Sylvester matrix has size at most $2k$ and entries of degree at most $k$ in $R$.

The rank conditions are witnessed by a nonzero $k\times k$ minor $h$ of $H$ (degree $\le k$) and a nonzero
$q\times q$ minor $\ell$ of $L$ (degree $\le q$). Hence the exceptional set is contained in the zero set of
$P=\operatorname{Res}\cdot h\cdot\ell$, of degree at most $2k^2+k+q$. Sampling every entry of $R$ from a grid
of size $N=2(2k^2+k+q)$ and using Schwartz–Zippel gives a false-negative probability at most $1/2$;
repetition makes it $2^{-T}$.

The determinantal divisor is the gcd of the $k$-minors; it is computed by a Smith form over $\mathbb Q[\lambda]$.
The pencil has $q\times k$ entries of degree at most one; polynomial-matrix normal-form algorithms give
polynomial bit complexity in the dimensions, the degree and the coefficient bit size (Kaltofen–Krishnamoorthy–
Saunders 1987; Storjohann–Labahn 1997). This citation is the one step not proved here. $\square$

Two remarks. First, the test is one-sided: a generically good instance can look bad at an exceptional sample,
never the converse. Second, rational sampling loses nothing: if the good locus is nonempty over $\mathbb C$ it
is a nonempty $\mathbb Q$-Zariski-open set, hence has rational points.

### II.2 A necessary-and-sufficient criterion for the free fibre at $q=3$, $\omega=2$

Assume $\ker T=0$. Let $E=\operatorname{row}(U_0)$ with $U_0=L_0N_K$, $F_0=\operatorname{row}(V_0)$ with
$V_0=L_0AN_K$, $m=q-r=3-r$, and let $\rho$ be the normal rank over $\mathbb C(\lambda)$ of the fixed pencil
$A(\lambda)=\lambda U_0-V_0$.

**Theorem.** The instance is feasible at $q=3$, $\omega=2$ if and only if

1. $\dim(E+F_0)\le2$;
2. $m\ge2-\dim E$;
3. and one of:
   (a) $\rho=2$, $V_0\ne\lambda U_0$ for every $\lambda$, and either the fixed pencil is good (constant gcd)
       or $m\ge1$;
   (b) $\rho=2$, $V_0=\lambda_0U_0$ for some $\lambda_0$, and $m\ge2$;
   (c) $\rho=1$ and $m\ge2$;
   (d) $\rho=0$ and $m=3$.

*Necessity.* Condition 1: every admissible row space $S$ contains both $E$ and $F_0$ and has dimension two.
Condition 2: $\operatorname{rank}H\le\dim E+m$. In (a), a bad fixed pencil with $m=0$ leaves no free row.
In (b), at $\lambda_0$ all fixed rows vanish and one free row gives rank at most one. In (c), the fixed rows
span a line $L(\lambda)$ for every $\lambda$; rank two requires the free row $b(\lambda)=\lambda x-y$ to lie
outside $L(\lambda)$. Since $x$ must lie outside $\operatorname{row}(U_0)$ for rank $H=2$, the determinant
$\det(a(\lambda),b(\lambda))$ is a nonconstant polynomial of degree at most two, hence has a root; there the
rank is at most one. In (d), $m=2$ gives a square free $2\times2$ pencil whose determinant has a root, and
$m<2$ is excluded by condition 2.

*Sufficiency.* (a) If the fixed pencil is good, the fixed rows themselves span $S$ for every $\lambda$. If it
is bad, its drops have rank one; for each drop $\lambda_i$ the condition $b(\lambda_i)\notin L_i$ is a proper
linear condition on $y$, and finitely many lines cannot cover $\mathbb C^2$. (b) Choose two free rows
independent at $\lambda_0$; for $\lambda\ne\lambda_0$ the fixed rows already span $S$. (c) With two free rows,
at every $\lambda$ at least one of them is outside $L(\lambda)$, and at the points where the fixed rows vanish
the two are chosen independent; again finitely many proper conditions. (d) An explicit witness is
$$H=\begin{pmatrix}1&1\\-1&2\\-1&-1\end{pmatrix},\qquad
H_A=\begin{pmatrix}-1&-1\\-2&0\\1&2\end{pmatrix},$$
whose three $2$-minors are $3\lambda^2+\lambda-2$, $-\lambda-1$, $3\lambda^2+2\lambda-4$, with gcd $1$; for
$k>2$ embed this in a two-plane. $\square$

A correction is worth recording. A first version of the criterion used only $\dim(E+F_0)$. It fails for
$$U_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad V_0=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad m=1:$$
here $\dim(E+F_0)=2$ but the fixed pencil $\binom{\lambda\ -1}{0\ 0}$ has normal rank one, and one free row
cannot complete it. The correct invariant is the normal rank $\rho$, not the dimension of $E+F_0$.

The criterion was checked on 1200 random instances ($k=2,3$; $r=0,1,2$; 200 each): all predictions were
confirmed, with explicit good completions for the feasible cases.

### II.3 A constrained stratum that is entirely bad

Consider $n=5$, $p=1$, $q=3$, $r=1$, with $C=e_1^{\mathsf T}$, $A$ having first row $e_5^{\mathsf T}$ and
columns $2,3,4$ equal to $e_3,e_2,e_5$, and $L_0=e_4^{\mathsf T}$. Then
$K=\langle e_2,e_3,e_4\rangle$, and the two Grassmannian points are $\sigma=(1,\pm1,0)$. With $K$-coordinates
denoted $E_1,E_2,E_3$ and $E=(0,0,1)$, the compatible pairs are

$$S_1:\ x=(a,-a,b),\ y=(-a,a,d);\qquad S_2:\ x=(a,a,b),\ y=(a,a,d).$$

For two compatible pairs $(x,y)$, $(x',y')$ put $H=[E;x;x']$, $H_A=[0;y;y']$.

**Theorem.** Over $S_1$ every admissible point drops rank at $\lambda=-1$; over $S_2$ every admissible point
drops rank at $\lambda=+1$. Hence the whole stratum $q=3$, $\omega=2$ is bad.

*Proof.* Over $S_1$ the rows of $\lambda H-H_A$ are
$$(0,0,\lambda),\qquad (\lambda+1)a\,(1,-1,0)+(0,0,\lambda b-d),\qquad
(\lambda+1)a'\,(1,-1,0)+(0,0,\lambda b'-d').$$
At $\lambda=-1$ all three lie in $\operatorname{span}\{E_3\}$, so the rank is at most one. Over $S_2$ the same
computation with $(\lambda-1)$ and $\lambda=+1$ applies. $\square$

Consequently $q_{\min}\ge4$. On the other hand $p=1$, $r_1=\operatorname{rank}[CA;C]=2$, so
$\rho=r_1-p=1\le1$; $(C,A)$ is observable and $\operatorname{rank}[C;L_0]=2$, so the terminal-region result
of the previous exchanges gives $q_{\min}=n-p=4$. Thus $q_{\min}=4$, and the stratum-level mechanism and the
numerical value agree.

The mechanism is worth isolating: if some $\lambda_0$ makes all rows of $\lambda_0H-H_A$, uniformly over a
fibre, lie in a fixed line, then that fibre is entirely bad. This is a reusable sufficient condition, and it
generalises the scaling argument of the earlier $k=2$ example.

## Part III. Questions

**Question 1.** Is the citation of Kaltofen–Krishnamoorthy–Saunders and Storjohann–Labahn sufficient for the
determinantal-divisor step, or should the exact algorithmic statement (input model, degree and bit-size
bounds, whether the full Smith form or only the determinantal divisor is computed) be spelled out separately?
With that step supplied, may the RP statement be made unconditional in a paper?

**Question 2.** Is the free-fibre criterion of II.2 complete in the form stated? The sufficiency uses only the
standard fact that finitely many proper algebraic conditions cannot cover $\mathbb C^2$. Is that acceptable,
or would you prefer an explicit construction for each of (a)–(d)? And is the normal-rank form the right one,
or should the criterion also be stated for general $k$?

**Question 3.** For the constrained case, is "there exists a common $\lambda_0$ at which the whole fibre
collapses to a line" the right general sufficient condition, and is there a natural necessary condition? More
generally, is the next target the general constrained criterion at $q=\omega+1$, or should the free-case
criterion and the RP bound be written up first?
