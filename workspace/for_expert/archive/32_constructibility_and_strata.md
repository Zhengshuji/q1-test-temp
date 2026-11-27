# Progress report: incidence on $W_K$, size audit, stratification, and a constructibility claim

This note reports four results obtained since the previous report and asks whether the third of them
— the claim that stratum feasibility is a rank condition — is correct as stated.
All notation is repeated; nothing is assumed from earlier files.

---

# Part I. Setting

## I.1 Problem

Given $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$ and a row block $L_0\in\mathbb C^{r\times n}$,
let $\mathcal L=\begin{bmatrix}L_0\\R\end{bmatrix}\in\mathbb C^{q\times n}$, and require

$$(5a)\ \operatorname{rank}\begin{bmatrix}\mathcal LA\\ \mathcal L\\ CA\\ C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}\mathcal L\\ CA\\ C\end{bmatrix},
\qquad
(5b)\ \operatorname{rank}\bigl[\lambda\mathcal L-\mathcal LA;\ CA;\ C\bigr]=h\ \ \forall\lambda\in\mathbb C,$$

with $h=\operatorname{rank}\begin{bmatrix}\mathcal L\\CA\\C\end{bmatrix}$. Question $q1$: is computing
$q_{\min}=\min\{q:\exists R\}$ NP-hard?

## I.2 Notation (column convention)

$K=\ker[C;CA]$, $k=\dim K$; $W_K=\mathcal LK$, $\omega=\dim W_K$; $D=K\cap\ker\mathcal L$, $d=\dim D=k-\omega$;
$\Phi_K(\mathcal Lv)=\mathcal LAv$ for $v\in K$; $P_K(\lambda)=\lambda\iota_K-\Phi_K$ with
$\iota_K:W_K\hookrightarrow\mathbb C^q$; $Q_{\mathcal L}(\lambda)=\begin{bmatrix}\lambda\mathcal L-\mathcal LA\\CA\\C\end{bmatrix}$
of size $m\times n$ with $m=q+2p$.

Standing fact (Theorem A, previously established): $(5b)$ fails iff $\mathcal E_K\neq\varnothing$, where
$$\mathcal E_K=\{[w]\in\mathbb P(W_K):\ \Phi_K(w)\in\mathbb Cw\}.$$

---

# Part II. Four results

## II.1 Incidence lives on $\mathbb P(W_K)$ and needs no $\mathbb P^1$

Since $\Phi_K(w)\in\mathbb Cw$ determines the scalar uniquely when $w\ne0$, the spectral obstruction is a
subset of $\mathbb P(W_K)$ alone:
$$\mathcal E_K=\{[w]\in\mathbb P(W_K):\ \Phi_K(w)\wedge\iota_K(w)=0\},$$
cut out by $\binom{q}{2}$ quadratic equations in $\omega$ variables. No parameter $[\alpha:\beta]$ is required.

The map $\pi:\mathbb P(K)\setminus\mathbb P(D)\to\mathbb P(W_K)$, $[v]\mapsto[\mathcal Lv]$, has constant fibre
dimension $d=k-\omega$ (since $\dim\mathcal L_K^{-1}(\mathbb Cw)=d+1$). Hence, for
$\widetilde{\mathcal E}_K=\pi^{-1}(\mathcal E_K)$,
$$\dim\widetilde{\mathcal E}_K=\dim\mathcal E_K+(k-\omega).$$
This is the exact relation between the old estimate in $\mathbb P(K)$ and the corrected one in $\mathbb P(W_K)$;
in particular one may not simply replace $k$ by $\omega$ in the old coverage bound.

## II.2 Size audit of the Bézout encoding

For $m=q+2p$, $n$, normal rank $h$, the Bézout encoding has
$$\text{variables}=(q-r)n+(h+1)\binom{m}{h}\binom{n}{h}.$$
Computed values:

| regime | $h$ | $\binom{m}{h}\binom{n}{h}$ for $n=6,8,10,12$ |
|---|---|---|
| $h=n-1$ | $n-1$ | 336, 960, 2 200, 4 368 |
| $h=n/2$ | $n/2$ | 1 120, 14 700, 199 584, 2 774 772 |
| $h=q+2p$ with $q$ small | small | 20–252 |
| $q$ near $n-p$ | $n$ | 1–11 |

So the count is polynomial exactly when $\min(h,\,n-h,\,m-h)$ is bounded, and exponential in the middle
regime. The two regimes relevant here ($q$ small, and $q$ near the terminal order) are both polynomial-size;
the middle regime is the only obstruction to a polynomial-size formula.

## II.3 Stratification by the normal rank

$h$ depends on $R$, so the index of $\Delta_h$ does. Stratify:

* $\mathcal S_k=\{\mathcal L:\operatorname{rank}[\mathcal L;CA;C]=k\}$ is **constructible**
  ($\{\operatorname{rank}\le k\}$ is closed, so the difference of two closed sets);
* $h$ takes at most $\min(m,n)+1\le n+1$ values;
* on $\mathcal S_k$ the criterion is a fixed determinantal condition with $\binom{m}{k}\binom{n}{k}$ minors of
  degree $\le k$.

Hence
$$\mathrm{DEC}(q)\iff\bigvee_{k=0}^{\min(m,n)}\Bigl[\mathcal L\in\mathcal S_k\ \wedge\ \Delta_k\text{ is a nonzero constant}\Bigr],$$
a disjunction of at most $n+1$ strata. This removes the "$h$ varies with $R$" obstruction, and it recovers the
$\exists\mathbb R$ upper bound by a modular route (each stratum is a finite statement). It does not improve the
bound and does not by itself give an algorithm.

## II.4 The constructibility claim

**Claim.** Fix a stratum $\mathcal S_k$. Then
$$\{R\in\mathcal S_k:\ \Delta_k\text{ is a nonzero constant}\}$$
is a **constructible** subset of $\mathcal S_k$.

**Argument.** Fix $R$. Write the $k\times k$ minors as $p_1(\lambda;R),\dots,p_N(\lambda;R)$, $N=\binom{m}{k}\binom{n}{k}$,
of degree at most $k$. Over the principal ideal domain $\mathbb C[\lambda]$,
$$\gcd(p_1,\dots,p_N)\ \text{is a unit}\iff\exists u_1,\dots,u_N\in\mathbb C[\lambda]:\ \sum_i u_ip_i=1 .$$
Truncate the multipliers at degree $D$ (a finite Bézout bound). Matching the coefficients of $\lambda^j$ on both
sides turns the identity into a **linear system whose unknowns are the coefficients of the $u_i$** and whose data
are polynomial functions of $R$. Solvability of that system is the rank condition
$$\operatorname{rank}\bigl[M(R)\mid b(R)\bigr]=\operatorname{rank}M(R).$$
Hence the set of $R$ for which $\Delta_k$ is a nonzero constant is defined by finitely many rank conditions,
i.e. it is constructible. $\square$

**Consequences, if the claim holds.**

1. The feasibility set is a constructible set, not an arbitrary semialgebraic set.
2. If the free block $R$ ranges over $\mathbb C^{(q-r)\times n}$, then the decision problem lies in the
   existential theory of algebraically closed fields rather than in the existential theory of the reals;
   the upper bound $\mathrm{DEC}\in\exists\mathbb R$ could then be sharpened.
3. If $R$ must range over $\mathbb R$, the intersection of a constructible set with the real points is still a
   real constructible set, which is a much smaller class than arbitrary semialgebraic sets.

**Caveats we are aware of.**

* The Bézout criterion itself requires no algebraic closedness, but the truncation at degree $D$ requires a
  valid finite bound; the explicit bound and its proof are not yet written out.
* Equivalence of the truncated system with the original condition rests on that bound.
* The size of $M(R)$ is of order $N(D+1)$, which is exponential in the middle stratum; the claim is structural,
  not algorithmic.
* Whether $R$ ranges over $\mathbb C$ or over $\mathbb R$ is, in our reading, not yet fixed by the project's
  complexity formulation.

---

# Part III. Questions

**Question 1.** Is the constructibility argument in II.4 correct as stated? In particular, is the truncated
Bézout system's solvability exactly the rank condition above, or does truncation require an additional argument
(for instance that a solution of degree $\le D$ exists whenever any solution exists)? If the latter is needed,
we would be grateful for the precise statement of the bounded-degree lemma.

**Question 2.** Which domain is appropriate for the free block: $R\in\mathbb C^{(q-r)\times n}$ or
$R\in\mathbb R^{(q-r)\times n}$? The literature formulation we follow uses complex matrix data and a complex
spectral parameter, but the existence question for the augmentation has been stated in real terms. This choice
decides whether the upper bound should be stated over the algebraically closed fields theory or over the reals.

**Question 3.** If the feasibility set is constructible, is the appropriate hardness target still
$\exists\mathbb R$-hardness, or does one now aim at NP-hardness of a constructible-set emptiness problem?
We would like your view on which target is both plausible and meaningful for the paper.

**Question 4.** Since only the middle strata have exponentially many minors, would you restrict the
complexity discussion to strata of constant $k$ (or to the two regimes $q$ small and $q$ near the terminal order),
and treat the general statement as a structural remark?

**Question 5.** Given the four results above, what would you prioritise next: the explicit Bézout degree bound
(needed to close II.4), the family version of the coverage criterion (needed to make II.1 usable for a family),
or the comparison between the two pencils?

We would rather report an attempt at one of these than a survey of all three.
