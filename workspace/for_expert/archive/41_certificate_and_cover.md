# The left-inverse certificate, and the one remaining structural question: can the chart cover be removed?

This report records the consequence of the left-inverse certificate for the encoding, states precisely what is
now settled, and reduces the remaining difficulty to a single structural question about charts.

---

# Part I. Setting

$H=\mathcal L(R)N_K$, $H_A=\mathcal LA(R)N_K$ are $q\times k$ and affine in $R$; $\omega=\operatorname{rank}H$;
$(5a)$ is equivalent to $\ker H\subseteq\ker H_A$; the reduced criterion says $(5b)$ holds iff
$\operatorname{rank}(\lambda H-H_A)=\omega$ for every $\lambda\in\mathbb C$.

---

# Part II. The certificate and its size

**Left-inverse theorem.** Let $P\in F[\lambda]^{q\times\omega}$ have full column normal rank. Then
$$\gcd\{\text{all }\omega\times\omega\text{ minors of }P\}\in F^\times
\iff\exists X\in F[\lambda]^{\omega\times q}:\ X(\lambda)P(\lambda)=I_\omega .$$
The converse direction is constructive: with $\sum_I u_Ip_I=1$ and $\deg u_I\le\omega-1$,
$$X=\sum_I u_I\operatorname{adj}(P_I)E_I,\qquad \deg X\le2\omega-2 .$$

**Encoding.** Writing $X=\sum_{j=0}^{2\omega-2}X_j\lambda^j$ and matching coefficients in
$X(\lambda)(\lambda U-G)=I_\omega$ gives $2\omega$ matrix equations, namely
$$-X_0G=I_\omega,\qquad X_{j-1}U-X_jG=0,\qquad X_{2\omega-2}U=0 .$$

| Quantity | minors plus Bézout | left-inverse certificate |
|---|---|---|
| unknowns | $\binom{q}{\omega}\omega$ | $(2\omega-1)\omega q$ |
| dependence on $R$ | degree $\omega$ | **linear** |
| degree bound for the bad locus | $2\omega^2$ | $2\omega$ |

So the certificate simultaneously makes the encoding polynomial-size and lowers the degree. The earlier
discussion of $\binom{m}{h}\binom{n}{h}$ as an obstruction applies only to the minor-based encoding and should be
replaced.

**A caution we recorded.** One must not argue that $X_{2\omega-2}U=0$ with $U$ of full column rank forces
$X_{2\omega-2}=0$: it only forces vanishing on $\operatorname{im}U$, and $U$ is not square. The example
$P=\binom{\lambda}{-1}$ with the constant $X=(0,-1)$ satisfies the certificate while $XU=0$.

---

# Part III. What is settled, and what is not

## III.1 Settled

1. The reduced criterion, including $\omega=0$.
2. Closedness of the bad locus on a chart of constant rank, and the resulting dichotomy: on an irreducible
   component the feasible set is either empty or Zariski open dense.
3. The reduced Bézout system with $2\omega$ equations and the rank-stratified description of the bad locus.
4. The exact image of the fixed-row map, $\operatorname{im}\Theta=\{(B_1,B_2):\ker T\subseteq\ker B\}$, with
   $\ker T\cong K\cap A^{-1}K$; in particular the observation data give an explicit **linear** compatibility
   space $\mathscr C$.
5. The decision problem equals the rank-stratified target, with $\omega=0$ included.
6. The encoding of the spectral condition is polynomial-size and of degree $2\omega$.

## III.2 Not settled

1. **The cover.** A chart is a choice of column set $S$ with $|S|=\omega$ and $H_{[:,S]}$ of full column rank;
   there are $\binom{k}{\omega}$ candidates, and the rank-$\omega$ locus may be reducible. Nothing we have shows
   that a polynomial number of charts and components suffices.
2. **The real points.** The complex dichotomy does not imply real feasibility without a density hypothesis.
3. **Complexity.** With a polynomial-size encoding and a linear compatibility space, a one-sided test is
   plausible, but it cannot be stated as a theorem about the decision problem until (1) is resolved.

---

# Part IV. The question

**Question 1.** Can the cover be removed altogether? We have in mind a chart-free encoding of
"$\operatorname{rank}(\lambda H-H_A)=\omega$ for all $\lambda$" along the following lines: if the pencil has
constant rank $\omega$ on $\mathbb C$, then in one variable it factors as
$$\lambda H-H_A=P_1(\lambda)\,R(\lambda),\qquad P_1\in\mathbb C[\lambda]^{q\times\omega},\quad
R\in\mathbb C[\lambda]^{\omega\times k},$$
with $P_1$ of full column rank everywhere, and $P_1$ admits a polynomial left inverse $X$ with $XP_1=I_\omega$.
Is the corresponding existentially quantified system — unknowns $P_1$, $R$, $X$, with the bilinear relation
$\lambda H-H_A=P_1R$ and $XP_1=I_\omega$ — a legitimate chart-free formulation? If so, the cover disappears from
the statement of the problem.

**Question 2.** If the cover cannot be removed, is there a polynomial bound on the number of charts needed for a
fixed stratum? Concretely: for a fixed $\omega$, is it enough to consider the charts corresponding to the
pivots of a single generic point, plus a polynomial number of exceptional ones?

**Question 3.** Is the formulation
$$\text{"all }(\omega+1)\text{-minors of }\lambda H-H_A\text{ vanish identically"}\ \wedge\
\text{"the }\omega\text{-minors have no common root"}$$
preferable to the chart-based formulation? The first conjunct is a family of polynomial identities in $R$ and is
chart-free; only the second involves the gcd. Would this split make the covering issue disappear from the
complexity statement, leaving it only in the gcd condition?

We would rather ask these three questions than build another layer on top of the chart formulation.
