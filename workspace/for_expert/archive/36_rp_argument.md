# The decision problem appears to lie in RP: a claim to be checked, plus an audit of what is verified

Two things are in this report. First, a verification audit: which of the recent statements are machine-checked,
and which are paper-only and therefore need your scrutiny. Second, the RP argument for the decision problem,
with the degree bound that was missing in the previous report, stated in full so that it can be checked point
by point.

---

# Part I. Setting

Given $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$, $q\ge r$, let
$\mathcal L=\begin{bmatrix}L_0\\R\end{bmatrix}$ and require

$$(5a)\ \operatorname{rank}\begin{bmatrix}\mathcal LA\\ \mathcal L\\ CA\\ C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}\mathcal L\\ CA\\ C\end{bmatrix},
\qquad
(5b)\ \operatorname{rank}\bigl[\lambda\mathcal L-\mathcal LA;\ CA;\ C\bigr]=h\ \ \forall\lambda\in\mathbb C .$$

$K=\ker[C;CA]$, $k=\dim K$, $N_K$ a basis of $K$ (columns), $H(R)=\mathcal L(R)N_K$, $H_A(R)=\mathcal LA(R)N_K$,
$\omega=\operatorname{rank}H(R)$. $\mathrm{DEC}(q)$: does there exist $R$ with $(5a)$ and $(5b)$?

---

# Part II. Verification audit

## II.1 Machine-checked (Lean, `lake env lean`, exit 0)

| Statement | Declaration |
|---|---|
| $(5a)\iff\exists\Lambda,G_0,G_1:\ \mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ | `QProofFactor.Decomp.decomp_iff_ker` |
| $\Phi_K$ well defined (quotient form) | `B37Domain.l2_factor` |
| $\Phi_K$ independent of the extension | `B37Domain.l3_unique` |
| $\dim(\mathcal LK)=\dim K-\dim\ker(\mathcal L|_K)$ | `B37Domain.l6_finrank` |
| $\ker Q_{\mathcal L}(\lambda)\cap K=K\cap L^{-1}\ker(\Phi-\lambda)$ (set level of the kernel identity) | `B24L4.l4_ker_fiber`, `l4_finrank` |
| $K\cap\ker L\le\ker T\iff\ker(L|_K)\le\ker(T|_K)$ — the identity $(5a)\iff\ker H\subseteq\ker H_A$ | `B36FiveA.ker_inf_le_iff_restrict` |
| $H$ of full column rank $\Rightarrow$ $(5a)$ automatic | `B36FiveA.ker_inf_le_of_injective` |

## II.2 Paper-only, listed for review

1. **(12) with the dimension addition**: $\dim\ker Q_{\mathcal L}(\lambda)=\dim D+\dim\ker P_K(\lambda)$.
   The set-level identity is machine-checked; the addition of $\dim D$ is rank–nullity on $v\mapsto Lv$.
2. **L7**: $(5b)\iff\gcd\{\omega\text{-minors of }\lambda H-H_A\}\in\mathbb C^\times$.
3. **Closedness of the bad locus** (homogenise to $\mathbb P^1$; no root at infinity because the leading
   coefficient has full column rank; projection from $U\times\mathbb P^1$ is proper).
4. **Elimination-ideal trichotomy** and the correction that feasibility is "$E\ne(0)$", not "$E$ proper".
5. **Generic-gcd criterion** over the function field of an irreducible chart.
6. **Realizability lemma**: if $K\cap AK=0$ then $\Psi:M\mapsto(MN_K,MAN_K)$ is onto, and $n-p\ge 2k$ is the
   compatibility condition. (The explicit borderline construction was checked numerically, not in Lean.)
7. **Rank-stratified target RAZE** and $\mathrm{DEC}\iff\mathrm{RAZE}$.
8. **Per-layer analysis**: $\omega=0$ and $\omega=1$ are polynomial-time; $\omega\ge2$ reduces to a
   non-emptiness/identity test.
9. **Degree bound** (Part III below).

---

# Part III. The RP argument

## III.1 The three ingredients

(i) *Closedness.* On each admissible chart the bad locus $\mathcal B$ is Zariski closed, hence on an
irreducible component either $\mathcal B=U$ (infeasible) or $\mathcal B\subsetneq U$ (feasible, open dense).

(ii) *Explicit low-degree equations for $\mathcal B$.* By the bounded-degree Bézout lemma, $\gcd$ is a unit iff
there are multipliers $u_i$ of degree $\le\omega-1$ with $\sum_i u_i p_i=1$. Matching the coefficients of
$\lambda^0,\dots,\lambda^{2\omega-2}$ gives a linear system
$$M(R)\,u=b,$$
with $N\omega$ unknowns, $2\omega-1$ equations, $M(R)$ **linear** in $R$ and $b$ constant. Then
$$\mathcal B=\bigl\{R:\ \operatorname{rank}[M(R)\mid b]>\operatorname{rank}M(R)\bigr\}
=\bigl\{R:\ \text{all }(2\omega-1)\text{-minors of }[M(R)\mid b]\text{ vanish}\bigr\},$$
so $\mathcal B$ is cut by polynomials of degree $\le 2\omega-1$ in $R$. In the rank parameterisation
$H=UV^{\mathsf T}$, $M$ is of degree $\omega$ in each of $U,V$, giving total degree $\le 2\omega(2\omega-1)$.

(iii) *Sampling inside the chart.* Draw $U,V$ at random, form the target pair, and solve the linear system
$H(R)=UV^{\mathsf T}$, $H_A(R)=\text{(the corresponding target)}$ for $R$; in the region $K\cap AK=0$ the
system is solvable for every target pair (realizability lemma), so each draw yields a point of the chart.

## III.2 The consequence

If $\mathcal B\subsetneq U$ then a random draw is feasible with probability at least $1-2\omega(2\omega-1)/|S|$,
by Schwartz–Zippel; if $\mathcal B=U$ no draw is feasible. Hence the decision problem for a fixed chart has a
one-sided error test with polynomially many draws when $\omega$ is bounded, and
$$\mathrm{DEC}(q)\in\mathrm{RP}\qquad(\text{complex version})$$
provided the chart sampling and the component decomposition are as described. Consequently
$$q1\text{ is NP-hard}\ \Longrightarrow\ \mathrm{NP}\subseteq\mathrm{RP}.$$

## III.3 What this does not give

* It does not give a deterministic algorithm, nor a bound on $q_{\min}$ itself.
* The real version requires the real points of the charts to be Zariski dense; otherwise the complex feasible
  open set may miss the real locus.
* The probability bound requires $|S|$ to exceed the degree; over $\mathbb Q$ this means working over a large
  prime field and then verifying candidates exactly.
* $\omega$ is not bounded in general, so the "polynomially many draws" statement is per chart; the number of
  charts is $\sum_\omega\binom{k}{\omega}$, which is not polynomial when $k$ grows.

---

# Part IV. Questions

**Question 1.** Is ingredient (ii) correct as an identity of sets? In particular, is
$\mathcal B=\{R:\operatorname{rank}[M(R)\mid b]>\operatorname{rank}M(R)\}$ exactly, rather than up to closure,
given that $\mathcal B$ is already known closed?

**Question 2.** Is the degree bound $2\omega(2\omega-1)$ in the parameterisation $(U,V)$ correct, and is
Schwartz–Zippel applicable in the form used (the sampled distribution must be over the chart, not over the
ambient space of $R$)?

**Question 3.** Is the conclusion "$\mathrm{DEC}\in\mathrm{RP}$" the right way to state this, or is the honest
statement weaker (for instance: a one-sided test per chart, with the number of charts unbounded)? We would
rather state the weakest true claim.

**Question 4.** If the RP statement is correct, what is the appropriate way to phrase the answer to $q1$?
Our reading is: $q1$ is false unless $\mathrm{NP}\subseteq\mathrm{RP}$; but the problem as originally posed asks
about computing $q_{\min}$, and the threshold versions are what we can address.

**Question 5.** Among the paper-only items listed in II.2, which ones would you check first? We are willing to
formalise any of them that is amenable to Lean, but we cannot tell which ones carry the most risk.
