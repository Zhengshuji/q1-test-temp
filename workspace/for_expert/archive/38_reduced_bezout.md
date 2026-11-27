# The reduced-pencil Bézout theorem, stated explicitly

This report does exactly one thing requested in the last audit: it states the Bézout theorem for the **reduced**
$q\times\omega$ pencil, with the selected columns fixed, the factorisation proved, the number of minors
identified, the $2\omega$-equation coefficient matrix displayed, the rank-stratified description derived, and
the degree bound stated under the affine-entry hypothesis. It also records the three clarifications the audit
asked for in Theorems 1 and 2.

---

# Part I. Setting and notation

Let $K=\ker[C;CA]$, $N_K\in\mathbb C^{n\times k}$ a matrix whose columns span $K$, and
$$H(R)=\mathcal L(R)N_K,\qquad H_A(R)=\mathcal LA(R)N_K,$$
both $q\times k$, with entries **affine-linear** in the observer variables $R$. Put
$\omega=\operatorname{rank}H(R)$, assumed constant on the chart under consideration, and assume $(5a)$ in the
form $\ker H\subseteq\ker H_A$.

**Rectangular factorisation.** Choose a factorisation
$$H=UV^{\mathsf T},\qquad U\in\mathbb C^{q\times\omega},\quad V\in\mathbb C^{k\times\omega},$$
with both factors of full column rank. Then
$$\ker H\subseteq\ker H_A\iff\exists G\in\mathbb C^{q\times\omega}:\ H_A=G\,V^{\mathsf T},$$
and in that case
$$P(\lambda)=\lambda H-H_A=(\lambda U-G)V^{\mathsf T}.$$
We use the rectangular factor $G$ rather than the square extension $Z$ of the previous report; the two are
related by $G=ZU$, and only the rectangular one is intrinsic.

**Selected columns.** Fix a column set $J\subseteq\{1,\dots,\omega\}$ with $|J|=\omega$ — in the reduced
setting all $\omega$ columns are used, so the chart is specified by the factorisation itself; if one works with
the unreduced pencil one fixes instead an invertible $\omega\times\omega$ submatrix of $H$, and the count of
minors changes as noted in Part III.

---

# Part II. The theorem

**Theorem (reduced-pencil Bézout).** Let
$$P_{\mathrm{red}}(\lambda):=\lambda U-G\ \in\ \mathbb C[\lambda]^{q\times\omega},$$
with $U$ of full column rank $\omega\ge1$, and let $p_1,\dots,p_N$ be its maximal ($\omega\times\omega$)
minors, where
$$N=\binom{q}{\omega}.$$
Assume the entries of $U$ and $G$ are affine-linear in $R$. Then the following are equivalent:

1. $\operatorname{rank}P_{\mathrm{red}}(\lambda_0)=\omega$ for every $\lambda_0\in\mathbb C$;
2. $\gcd(p_1,\dots,p_N)\in\mathbb C^\times$;
3. there exist $u_1,\dots,u_N\in\mathbb C[\lambda]$ with $\deg u_i\le\omega-1$ and
   $\sum_i u_i p_i=1$;
4. the linear system
   $$M_\omega(R)\,u=b_\omega,\qquad M_\omega(R)\in\mathbb C^{2\omega\times N\omega},\quad
   b_\omega=(1,0,\dots,0)^{\mathsf T},$$
   is solvable, where the $2\omega$ rows are the coefficients of $\lambda^0,\dots,\lambda^{2\omega-1}$.

*Proof.* (1)$\iff$(2): for fixed $\lambda_0$, $\operatorname{rank}P_{\mathrm{red}}(\lambda_0)=\omega$ iff some
maximal minor is nonzero; the minors vanish simultaneously at $\lambda_0$ iff $\lambda_0$ is a common root; over
$\mathbb C$ a family of univariate polynomials has a common root iff its gcd is nonconstant.
(2)$\iff$(3): the bounded-degree Bézout lemma, applicable because each $p_i$ has degree at most $\omega$.
(3)$\iff$(4): with $\deg u_i\le\omega-1$ and $\deg p_i\le\omega$, the left side has degree at most
$2\omega-1$, so the identity is equivalent to matching $2\omega$ coefficients; each matching equation is linear
in the unknown coefficients of the $u_i$, with coefficients read off from the $p_i$. $\square$

**Corollary (exact inconsistency identity).** On the chart,
$$\mathcal B_\omega=\{R:\operatorname{rank}[M_\omega(R)\mid b_\omega]>\operatorname{rank}M_\omega(R)\},$$
an equality of sets, and consequently
$$\mathcal B_\omega=\bigcup_{s=0}^{2\omega-1}\{R:\operatorname{rank}M_\omega(R)=s,\
\operatorname{rank}[M_\omega(R)\mid b_\omega]\ge s+1\},$$
a finite union of constructible sets. The set where all maximal minors of $[M_\omega\mid b_\omega]$ vanish is
**not** $\mathcal B_\omega$: when $\operatorname{rank}M=m-1$ and $\operatorname{rank}[M\mid b]=m$ the system is
inconsistent although the augmented matrix has a nonzero maximal minor.

**Degree bound.** The entries of $M_\omega$ are linear functions of $R$; a size-$s$ minor has degree at most
$s\cdot\omega$ in the minors' coefficients, and $M_\omega$ has $2\omega$ rows, so the rank-stratified equations
have degree at most
$$2\omega^2\quad\text{in }R .$$
In the factor variables $(U,V,G)$ a maximal minor of $P_{\mathrm{red}}$ has degree at most $\omega$ in $U$ and
$G$ and is independent of $V$; the factorisation $P=(\lambda U-G)V^{\mathsf T}$ shows that the pullback of a
size-$s$ rank condition has degree at most $2\omega\cdot\omega=2\omega^2$ in $(U,G)$, and the $V$-dependence of
the unreduced minors is the factor $\det(V_{J,:}^{\mathsf T})$, of degree at most $\omega$ per factor, giving
the total bound $4\omega^2$ in $(U,V,G)$.

---

# Part III. Clarifications requested by the audit

## III.1 Theorem 1 (the square extension)

The extension $Z\in\mathbb C^{q\times q}$ with $H_A=ZH$ exists but is **not unique**, and only its restriction
$\operatorname{im}H\to\mathbb C^q$ is determined. In general $\operatorname{im}H$ is **not** $Z$-invariant.
Accordingly the obstruction is
$$\exists\,0\ne w\in\operatorname{im}H,\ \lambda\in\mathbb C:\ Zw=\lambda w,$$
i.e. the invariant-**line** condition on the map $\operatorname{im}H\to\mathbb C^q$, not an eigenvalue condition
for an endomorphism of $\operatorname{im}H$. The criterion is intrinsic because any two extensions agree on
$\operatorname{im}H$.

## III.2 Theorem 2 (closedness)

State explicitly that $H,H_A$ depend **algebraically** on $R$, so that the incidence equations are algebraic.
For the elimination corollary, state that $U$ is affine irreducible with coordinate ring $A=\mathbb C[U]$; for
locally closed rank charts, localise in the coordinate ring (or saturate) rather than silently treating the
chart as affine space.

## III.3 The minor count

The count $N=\binom{q}{\omega}$ is correct for the **reduced** $q\times\omega$ pencil used in Part II. For the
**unreduced** $q\times k$ pencil the count is
$$N=\binom{q}{\omega}\binom{k}{\omega},$$
and the coefficient system keeps $N\omega$ unknowns but with this larger $N$. We adopt the reduced formulation
as the main statement, since it removes redundant minors and matches the intrinsic $W_K$-based reduction.

---

# Part IV. Question

Is the reduced-pencil formulation in Part II now correct in all six respects the audit listed (selected columns;
factorisation; count $\binom{q}{\omega}$; displayed $2\omega$-equation matrix; rank-stratified description;
degree bound under the affine hypothesis)? In particular, is the $4\omega^2$ bound in $(U,V,G)$ the right one,
or does the factor $\det(V_{J,:}^{\mathsf T})$ contribute differently once one restricts to a chart with a fixed
$J$?
