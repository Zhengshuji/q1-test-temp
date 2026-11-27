# Corrected projective theorem, lifting, and the k=3 component table

This report has three parts. Part I fixes the setting. Part II states the results since the last report: the
corrected projective theorem, a lifting lemma for the full-row-rank condition, and the component
decomposition for $k=3$ with the resulting table. Part III asks whether the present concrete-case focus is
sound and what you would suggest next.

## Part I. Setting

Given $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$, one seeks
$R\in\mathbb C^{(q-r)\times n}$ with $L=[L_0;R]$ full row rank and

$$(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\quad\forall\lambda .$$

Put $K=\ker[C;CA]$, $k=\dim K$, $N_K$ a basis, $H=LN_K$, $H_A=LAN_K$. For a fixed rank $\omega$,
admissibility is $\operatorname{rank}H=\omega$ and $\ker H\subseteq\ker H_A$; on it $Z:W\to\mathbb C^q$,
$W=\operatorname{im}H$, is defined by $Z(Hx)=H_Ax$. Writing $Z=(A;B)$ with the bottom $\omega$ rows forming
$B$, badness is
$$\text{bad}\iff\exists\,0\ne y\in\ker B,\ Ay\in\mathbb C y .$$

Throughout, $q=\omega+1$, $k=\omega+1$, $m=q-r$, $E=U_0=L_0N_K$, $F_0=V_0=L_0AN_K$, $e=\dim E$.

## Part II. Results

### II.1 The corrected projective theorem

For $\sigma\in\mathbb P^{k-1}$, $S=\ker\sigma$, choose a basis $B$ of $S$ and put
$$P=B^\top Z_1,\qquad Q=B^\top Z_2,\qquad X_S=\{a\in\mathbb C^\omega:aP\in\operatorname{row}Q\}.$$

The base is not the whole $\mathbb P^{k-1}$ but
$$\mathcal B=\mathbb P\big((E+F_0)^\perp\big)=\{[\sigma]:\sigma|_{E+F_0}=0\}.$$

The exact admissibility conditions are
$$E+F_0\subseteq S,\qquad e+\dim X_S-\dim(E\cap X_S)=\omega,\qquad m\ge\omega-e,$$
together with $\operatorname{rank}H=\omega$, $\ker H\subseteq\ker H_A$, and the existence of a full-row-rank
lift. The first two replace the incorrect condition “$X_S\not\subseteq E$” of the previous report; the last one
is treated in II.2.

The **total incidence space** consists of $(\sigma,(x_i,y_i)_{i=1}^m)$ satisfying the above, with
$x_i,y_i\in S$ and $x_iZ_1+y_iZ_2=0$. It is stratified by
$$\big(\operatorname{rank}Q,\ \operatorname{rank}[P;Q],\ t=\dim(E\cap X_S),\ \operatorname{rank}H\big).$$
On each constant-rank stratum, the bad set is closed: homogenise $\lambda$ to $\mathbb P^1$; at infinity
$\lambda_0H-\lambda_1H_A=\lambda_0H$ has rank $\operatorname{rank}H=\omega$, so the bad incidence set avoids
infinity; the projection from $X\times\mathbb P^1$ is proper. Hence on each irreducible component either all
points are bad, or the good points are Zariski-open dense; the generic determinant divisor over $\mathbb C(X)$
decides. The component decomposition itself is the remaining algorithmic input; for $k=3$ it is given in II.3.

### II.2 A lifting lemma for the full-row-rank condition

Let $N=N_K$, $M=AN_K$, and let $(H_b,H_{A,b})$ be a compatible compressed pair. The set
$$\mathcal R=\{R\in\mathbb C^{m\times n}:RN=H_b,\ RM=H_{A,b}\}$$
is an affine subspace. Let $\pi:\mathbb C^n\to\mathbb C^n/\operatorname{row}L_0$ be the quotient.

> **Lemma.** (i) $\operatorname{rank}[L_0;R]=q\iff\operatorname{rank}(\pi R)=m$.
> (ii) $\mathcal R$ contains a full-row-rank lift iff the symbolic matrix
> $\pi R(t)=\pi R_0+\sum_j t_j\,\pi R_j$ has rank $m$ over $\mathbb C(t)$, where $R_0$ is a particular
> solution and $R_j$ a basis of the homogeneous space.
> (iii) If so, the full-row-rank lifts are Zariski-open dense in $\mathcal R$.

The proof is three lines: the rank formula, the fact that the $m\times m$ minors are polynomials in $t$, and
the complement of a nonzero minor. This makes the lifting condition a symbolic rank test rather than a
geometric condition. For the $k=3$ examples, the good compressed points have been lifted explicitly and pass
all seven checks.

### II.3 The $k=3$ component decomposition

For $k=3$, $S$ is a hyperplane and $\ker B^\top=\operatorname{span}\{\sigma\}$. Hence
$$\operatorname{rank}Q=\operatorname{rank}Z_2-\dim(\operatorname{im}Z_2\cap\operatorname{span}\{\sigma\}).$$
The right-hand side depends only on whether $\sigma$ lies in the fixed subspace $\operatorname{im}Z_2$; this is
a linear condition. Similarly $\operatorname{rank}[P;Q]$ depends only on the dimensions of
$\operatorname{im}Z_1\cap\operatorname{span}\{\sigma\}$ and $\operatorname{im}Z_2\cap\operatorname{span}\{\sigma\}$,
again linear conditions. Therefore, for $k=3$ and $e=0$, every rank stratum is a projective subspace (a point
or a line) or its complement, hence irreducible; the strata of the table are the irreducible components.

For the five instances the components are:

| instance | $d$ | component | rank data | generic behaviour |
|---|---|---|---|---|
| 1–3 | 1 | open $\mathbb P^1\setminus\{pt\}$ | $\operatorname{rank}Q=1$ | all bad, gcd $\lambda t$ |
| 1–3 | 1 | the point $\sigma=(1,0,0)$ | $\operatorname{rank}Q=0$ | good, gcd $1$, lift verified |
| 4 | 2 | open part of the base | $\operatorname{rank}Q=1$, $\operatorname{rank}[P;Q]=1$ | all bad |
| 4 | 2 | the excluded points | $\operatorname{rank}Q=1$, $\operatorname{rank}[P;Q]=2$ | not admissible |
| 5 | 2 | line $\mathbb P(\operatorname{im}Z_2)$ | $\operatorname{rank}Q=1$ | all bad |
| 5 | 2 | complement of that line | $\operatorname{rank}Q=2$ | all bad |

The table is exact for these instances; the $d=1$ open stratum has a symbolic gcd certificate, the other rows
are sampled. The $d=2$ rows are consistent with the restricted theorem of the previous report
($k=3,\omega=2,q=3,d=2,U_0=0$: every admissible compressed point is bad).

### II.4 The corrected $q=2$ criterion and the restricted $d=2$ theorem

For $q=2$, $\omega=1$, the exact criterion is
$$\text{good}\iff Z(W)\not\subseteq W,$$
equivalently $\det[w,Z(w)]\ne0$. When $U_0=0$, writing $H=[0;h]$, $H_A=[V_0;g_2]$ with $V_0=\alpha h$ and
$g_2=\beta h$, the block identification gives $A=\beta$, $B=\alpha$, hence good $\iff\alpha\ne0$ (the
coefficient of $V_0$, not of $g_2$). The $q=2$ classification is: $\omega=0$ good, $\omega=1$ good iff
$Z(W)\not\subseteq W$, $\omega=2$ always bad. Four instances have $q_{\min}=2$ with explicit witnesses, while
their $q=3,\omega=2$ strata are mixed or entirely bad — a concrete instance of “the stratum does not determine
the order”.

The restricted $d=2$ theorem is as before: for $k=3$, $\omega=2$, $q=3$, $d=2$, $U_0=0$, every admissible
compressed point is bad. The proof uses $V_0Z_2=-U_0Z_1=0$, hence $V_0\in\ker(\cdot Z_2)=\operatorname{span}\{\ell\}$,
and the induced operator on $S/\operatorname{span}\{\ell\}$ has an eigenvalue.

## Part III. Questions

**Question 1.** Is the corrected projective theorem now correct? Are the three admissibility conditions
complete (together with rank $H=\omega$, $\ker H\subseteq\ker H_A$ and the lift), and is the total incidence
space the right object for the genericity theorem? Is there any remaining subtlety in the closedness or
dichotomy argument?

**Question 2.** Is the $k=3$ component argument correct? In particular, is it true that for $k=3$, $e=0$ every
rank stratum is irreducible because the rank conditions are linear in $\sigma$? What changes for $e>0$, where
$t=\dim(E\cap X_S)$ enters? And is the linearity special to $k=3$ (hyperplane sections), or is there a general
theory of rank strata of hyperplane sections that we should cite?

**Question 3.** Is the lifting lemma correct and sufficient as stated? Is the symbolic rank over $\mathbb C(t)$
the right criterion, and is the Zariski-open density statement the strongest one can make? Should the lemma be
stated for affine subspaces of matrices rather than for this particular system?

**Question 4.** The present work is concentrated on concrete cases: $k=3$, $q=3$, $\omega=2$, $d=1$ or $2$,
$e=0$. Is this a problem for the long-term programme? Are we at risk of overfitting the general theory to the
smallest case, or is the concrete case the right place to discover the mechanisms (fibre-dimension jump,
left kernel of $Z_2$, rank strata) before generalising? Which generalisation is most valuable: $e>0$, $k>3$,
$q>3$, or the real-point question?

**Question 5.** Is there a general theory that would make the $k=3$ component decomposition a special case —
for example, the rank strata of hyperplane sections of determinantal varieties, Schubert varieties of the
Grassmannian, or rank-metric codes? We would be grateful for references; the formula
$\operatorname{rank}Q=\operatorname{rank}Z_2-\dim(\operatorname{im}Z_2\cap\operatorname{span}\{\sigma\})$ looks
like a standard restriction formula, but we have not located a citable statement.

**Question 6.** What would you suggest next? Is the concrete-case package (the corrected projective theorem,
the restricted $d=2$ theorem, the $q=2$ criterion, the $k=3$ component table and the lifting lemma)
publishable as it stands, or should the general theorem precede the paper? Do you have other suggestions —
for the choice of generalisation, for the Lean formalisation, or for a computation that would most cheaply
test whether the $k=3$ phenomena persist?
