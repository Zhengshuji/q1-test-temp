# Recent results, experiments, and questions

This report collects the results of the last few rounds, the experimental methods and outputs, and the
conjectures we would like you to assess. Part I fixes the setting. Part II states the results with their
evidence level. Part III lists the questions.

## Part I. Setting

Given $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$, one seeks
$R\in\mathbb C^{(q-r)\times n}$ with $L=[L_0;R]$ (full row rank, $q$ rows) satisfying

$$(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\quad\forall\lambda .$$

Put $K=\ker[C;CA]$, $k=\dim K$, $N_K$ a basis, $H=LN_K$, $H_A=LAN_K$, $h=\operatorname{rank}[L;CA;C]$. For a fixed
rank $\omega$, the admissible locus is $\operatorname{rank}H=\omega$ and $\ker H\subseteq\ker H_A$; on it
$Z:W\to\mathbb C^q$, $W=\operatorname{im}H$, is defined by $Z(Hx)=H_Ax$. Writing $Z=(A;B)$ with the bottom
$\omega$ rows forming $B$, the bad condition is

$$\text{bad}\iff\exists\,0\ne y\in\ker B,\ Ay\in\mathbb C y .$$

For $q=\omega+1$, $B$ is the last row and $\ker B=\mathbb C w$; for $\omega=2$,
$\text{good}\iff B\ne0$ and $\det[w,Aw]\ne0$. The free case is $\ker T=0$ for $T(v,w)=v+Aw$.

## Part II. Results

### II.1 A one-parameter family at $d=1$: mixed stratum (proved)

Data: $k=3$, $q=3$, $\omega=2$, $d=\dim\ker T=1$,
$$E=L_0N_K=0,\qquad V_0=L_0AN_K=(0,a,b)\ne(0,0),\qquad Z_1=0,\qquad Z_2=e_1 .$$

Then the compatible pairs satisfy $y_1=0$, and the admissible locus is
$$\{\sigma:\sigma\cdot V_0=0\}\cong\mathbb P^1,\qquad S=\ker\sigma .$$

*Open stratum* ($\sigma\ne(1,0,0)$, i.e. $S\ne\{y_1=0\}$): $S\cap\{y_1=0\}$ is a line; since $V_0\in S$ and
$(V_0)_1=0$, that line is $\langle V_0\rangle$; every compatible $y_i$ is a multiple of $V_0$. At $\lambda_0=0$
the three rows of $\lambda H-H_A$ are $-V_0,-y_1,-y_2$, all in $\langle V_0\rangle$, so the rank is
$\le1<2$. Hence the whole open stratum is bad.

*Exceptional point* ($\sigma=(1,0,0)$): $S=\langle e_2,e_3\rangle$, $V_0=(a,b)$ in these coordinates. A good
point exists in two cases:

- if $ab\ne0$: take $x_1=e_2$, $x_2=e_2+e_3$, $y_1=y_2=e_2$; the three $2$-minors are
  $$b(\lambda-1),\qquad (b-a)\lambda-b,\qquad \lambda(\lambda-1),$$
  with gcd $1$;
- if $a=0$ or $b=0$: take $x_1=e_2$, $x_2=e_3$, $y_1=e_3$, $y_2=e_2$; the minors are
  $$a+b\lambda,\qquad -a\lambda-b,\qquad \lambda^2-1,$$
  with gcd $1$ (a nonzero constant divisor kills the gcd).

Hence the $q=3,\omega=2$ stratum is **mixed**: the open stratum is entirely bad, one point is good. The proof
is paper-level; three instances were checked by enumeration (see II.4).

### II.2 A $d=2$ example: two points, entirely bad (proved)

Data: $n=7$, $p=2$, $r=1$, $k=3$, $d=2$,
$$U_0=0,\quad V_0=(-1,0,0),\quad
Z_1=\begin{pmatrix}0&0\\0&0\\0&1\end{pmatrix},\quad
Z_2=\begin{pmatrix}0&0\\1&0\\0&1\end{pmatrix}.$$

The admissible locus is $\{\sigma_1=0\}$; for $\sigma=(0,1,t)$ with $t\ne0$ one has $\dim X_S=1$, so
$E+X_S\ne S$ and the point is not admissible. The admissible points are exactly
$$\sigma=(0,1,0)\quad\text{and}\quad\sigma=(0,0,1).$$

At $\sigma=(0,1,0)$: $S=\langle e_1,e_3\rangle$, $V_0=-e_1$, $P=Q=\binom{0\ 0}{0\ 1}$; compatibility gives
$b_2=-a_2$, so $x=a_1e_1+a_2e_3$, $y=b_1e_1-a_2e_3$. At $\lambda=-1$,
$$-V_0=e_1,\qquad -x_i-y_i=-(a_{i1}+b_{i1})e_1,$$
all rows in $\langle e_1\rangle$; rank $\le1$. At $\sigma=(0,0,1)$: $S=\langle e_1,e_2\rangle$, $P=0$,
$Q=\binom{0\ 0}{1\ 0}$; compatibility gives $b_2=0$, so $x=a_1e_1+a_2e_2$, $y=b_1e_1$. All $2$-minors of
$\lambda H-H_A$ carry a factor $\lambda$:
$$\det(e_1,\lambda x_i-y_i)=\lambda a_{i2},\qquad
\det(\lambda x_i-y_i,\lambda x_j-y_j)=\lambda^2(a_{i1}a_{j2}-a_{i2}a_{j1}),$$
so $\lambda=0$ is a common root. Hence both admissible points are entirely bad.

A scan of further $d=2$ instances gave: one with ten admissible points, all bad (sampled); one with no
admissible point at this layer. This suggests the conjecture below.

### II.3 $q_{\min}$ versus the stratum: all four instances have $q_{\min}=2$ (exact)

For four instances (three of the family in II.1, one of II.2), $q=1$ fails exactly (the $(5a)$ check fails),
and $q=2$ has an explicit witness passing all seven checks:

| instance | $q=2$ witness $R$ (one row) |
|---|---|
| 1 | $(0,0,13/5,-6/5,0,-1,0)$ |
| 2 | $(0,0,0,-1,-1/2,-1/2,0)$ |
| 3 | $(-1,-1,0,1,-2,-1,-1)$ |
| 4 | $L=[e_7;-e_2]$ |

Thus $q_{\min}=2$ for all four, although the $q=3,\omega=2$ stratum is mixed in the first family and
entirely bad in the $d=2$ example. So the stratum behaviour does not determine the order.

There is a discrepancy we could not resolve. For $q=2$, $\omega=1$ with $U_0=0$, we argued that
admissibility forces $V_0\parallel h=R N_K$ and $g_2=RAN_K\parallel V_0$, and that the block criterion then
predicts good iff the coefficient of $g_2$ is nonzero. The witness for instance 2 has that coefficient
equal to zero by our computation, yet it passes $(5b)$. Either our identification of the blocks $A,B$, or our
well-definedness condition, is wrong. This is Question 3 below.

### II.4 The projective constrained theorem (draft)

For $k=\omega+1$, $\sigma\in\mathbb P^{k-1}$, $B$ a basis of $S=\ker\sigma$, put
$$P=B^\top Z_1,\qquad Q=B^\top Z_2,\qquad X_S=\{a\in\mathbb C^\omega:aP\in\operatorname{row}Q\}.$$
We stratify the incidence space by
$$\big(\operatorname{rank}Q,\ \operatorname{rank}[P;Q],\ [X_S\subseteq E],\ \dim(E\cap X_S)\big).$$
On each stratum the ranks are constant, and we proved
$$\dim X_S=\omega-\big(\operatorname{rank}[P;Q]-\operatorname{rank}Q\big)$$
by rank-nullity applied to $a\mapsto aP\bmod\operatorname{row}Q$; the image is
$(\operatorname{row}P+\operatorname{row}Q)/\operatorname{row}Q$. For $E+X_S$, the condition is the complement
of the closed condition $X_S\subseteq E$; on that open part $\dim(E+X_S)=e+\dim X_S-\dim(E\cap X_S)$, and
further refinement by $\dim(E\cap X_S)$ makes it constant.

On each constant-rank stratum $Z$, homogenize $\lambda$ to $\mathbb P^1$; the set where all $\omega$-minors
vanish is closed, and on the fibre at infinity $\lambda_0H-\lambda_1H_A=\lambda_0H$ has rank
$\operatorname{rank}H=\omega$, so the bad set avoids infinity. The projection from $Z\times\mathbb P^1$ is
closed, so the bad set is closed in $Z$; if $Z$ is irreducible, either it is all bad or the good set is
Zariski-open dense. The generic determinant divisor over $\mathbb C(Z)$ decides which case occurs.

For $k=3,\omega=2,q=3$ the strata are explicit ($q\ne0$; $q=0,p\ne0$; $q=0,p=0$), and the family of II.1
realizes the first and the last. The open gaps are the enumeration of irreducible components for general
$k$, the general $k>\omega+1$ induction, and the real-point question.

### II.5 Rectangular determinantal divisor: a bridge lemma (proved)

Let $P\in\mathbb Q[\lambda]^{q\times k}$ have full column normal rank $k$, and let
$UP=\binom{D}{0}$ with $U$ unimodular and $D$ a $k\times k$ triangular block. Then
$$\Delta_k(P)=\gcd\{\text{all }k\text{-minors}\}=\det D$$
up to a nonzero constant. Proof: Cauchy–Binet shows that the ideals generated by the $k$-minors of $P$ and
$UP$ agree up to units; the only nonzero $k$-minor of $\binom{D}{0}$ is $\det D$.

For the rectangular Hermite form we now use the Las Vegas algorithm of Storjohann–Labahn (ISSAC 1995): a
rectangular $m\times n$ matrix ($m>n$) is reduced to an $(n+1)\times n$ Hermite form, with the main cost
comparable to fraction-free Gaussian elimination. Since RP absorbs Las Vegas, this closes the determinantal
divisor step without invoking the square nonsingular Smith theorem. The remaining detail is the explicit
bit-length bound for $D$.

### II.6 The RP bound (status)

With the repaired two-combination lemma (choose one nonzero $f$ first and only its finitely many irreducible
factors) and the bridge lemma of II.5, the argument for $k=\omega$ gives
$\mathrm{DEC}_{k=\omega}(q)\in\mathbf{RP}$ (not ZPP); the fixed-$(q,\omega)$ polynomial statement is retained.
The remaining technical detail is the bit-length accounting.

## Part III. Questions

**Question 1.** Is the family theorem of II.1 correct? In particular, is the two-case construction at the
exceptional point sound, and is the open-stratum argument ($S\cap\{y_1=0\}=\langle V_0\rangle$) complete?
Is there any hidden issue caused by the jump of the fibre dimension at $\sigma=(1,0,0)$?

**Question 2.** The $d=1$ family is mixed, while the $d=2$ examples are entirely bad or empty. Is this a
general phenomenon? What invariant distinguishes the two cases: the dimension $d=\dim\ker T$, the rank of
the compatibility map, or the fibre dimension at the exceptional point? Is a general $d=2$ theorem (all bad)
worth proving, or is the behaviour instance-dependent?

**Question 3.** The discrepancy in II.3: for $q=2$, $\omega=1$, $U_0=0$, we predicted good iff a certain
coefficient is nonzero, yet a witness with that coefficient zero passes $(5b)$. What is the correct
criterion for $q=2$, $\omega=1$? More generally, is $q_{\min}$ always decided by the lowest feasible
$\omega$-layer, and can the block criterion be used directly to decide it?

**Question 4.** Is the incidence-space stratification of II.4 the right formulation? Is the layer-constancy
formula $\dim X_S=\omega-(\operatorname{rank}[P;Q]-\operatorname{rank}Q)$ correct and complete, and is the
closedness/dichotomy argument acceptable? What is the main missing piece for a general $k=\omega+1$ theorem:
component enumeration, the generic-gcd computation, or the stratification of $E\cap X_S$ for $r>1$?

**Question 5.** Is the bridge lemma of II.5 correct, and is the Las Vegas rectangular Hermite form of
Storjohann–Labahn sufficient for the RP argument? Is there a deterministic rectangular alternative that
would avoid the Las Vegas step? Which bit-length bound for $D$ should be stated?

**Question 6.** Which next step would you prioritise: (a) a general $q=2$ criterion, (b) a general $d=2$
theorem, (c) the general $k=\omega+1$ projective theorem, (d) a Lean formalisation of the $d=1$ family, or
(e) assembling the paper package? We would also welcome any suggestion for a single computation or small
theorem that would most cheaply discriminate between the algorithmic and the hardness scenarios.
