# The central theorem: real augmentation exists iff the chart-free algebraic system has a real solution

This report states and proves the theorem proposed in the last audit, and lists the points we would like checked.

---

# Part I. Setting

$A,C,L_0$ real; $R\in\mathbb R^{(q-r)\times n}$; $\mathcal L(R)=\begin{bmatrix}L_0\\R\end{bmatrix}$;
$K=\ker[C;CA]$, $k=\dim K$, $N_K$ a real basis of $K$; $H(R)=\mathcal L(R)N_K$, $H_A(R)=\mathcal LA(R)N_K$,
both $q\times k$ and affine in $R$; $P(R,\lambda)=\lambda H(R)-H_A(R)$. Fix $\omega\in\{1,\dots,\min(q,k)\}$.

---

# Part II. The system

Unknowns: $R$, and
$$U\in\mathbb R^{q\times\omega},\quad V\in\mathbb R^{\omega\times k},\quad G\in\mathbb R^{q\times\omega},\quad
J\in\mathbb R^{\omega\times q},\quad Z\in\mathbb R^{k\times\omega},$$
and polynomials $Y(\lambda)=\sum_{j=0}^{2\omega-2}Y_j\lambda^j$ with $Y_j\in\mathbb R^{k\times q}$.

$$(\mathrm{A})\quad H(R)=UV,\qquad H_A(R)=GV,\qquad JU=I_\omega,\qquad VZ=I_\omega;$$
$$(\mathrm{B})\quad P(R,\lambda)\,Y(\lambda)\,P(R,\lambda)=P(R,\lambda),\qquad \deg Y\le 2\omega-2 .$$

**Theorem.** For $\omega\ge1$,
$$\exists\,R\in\mathbb R^{(q-r)\times n}\ \text{with }(5a),\ (5b)\ \text{and}\ \operatorname{rank}H(R)=\omega
\quad\Longleftrightarrow\quad (\mathrm{A})+(\mathrm{B})\ \text{has a real solution}.$$

## II.1 Proof, forward direction

Take such an $R$. Since $(5a)$ is equivalent to $\ker H\subseteq\ker H_A$, the map $H_A$ vanishes on $\ker H$ and
factorises as $H_A=G_0H$. Since $\operatorname{rank}H=\omega$, choose $H=UV$ with $U$ of full column rank and $V$
of full row rank (for instance with $V_{[:,S]}=I_\omega$ for a chart $S$). Then $H_A=GV$ with $G=G_0U$. The two
full-rank conditions give $J$ with $JU=I_\omega$ and $Z$ with $VZ=I_\omega$. By the reduced criterion, the
$\omega$-minors of $P$ have a gcd which is a nonzero **real** constant (a real polynomial with a complex root has
a real irreducible factor dividing it, so a nonconstant complex gcd forces a nonconstant real gcd). The
constructive generalized-inverse formula
$$Y=\sum_I u_I(\lambda)\operatorname{adj}(P_I(\lambda))\,E_I$$
with $\deg u_I\le\omega-1$ then gives $PYP=P$ with $\deg Y\le2\omega-2$. All entries are real.

## II.2 Proof, reverse direction

Take a real solution of (A)+(B).

1. *Rank.* $JU=I_\omega$ makes $U$ injective, $VZ=I_\omega$ makes $V$ surjective, and
   $UVZ=U$ gives $\operatorname{rank}(UV)\ge\operatorname{rank}U=\omega$; hence
   $\operatorname{rank}H(R)=\omega$.
2. *Condition $(5a)$.* If $Hx=0$ then $UVx=0$, so $Vx\in\ker U=0$ and $H_Ax=GVx=0$; hence
   $\ker H\subseteq\ker H_A$, which is $(5a)$.
3. *Normal rank.* $P=(\lambda U-G)V$ and $V$ is surjective, so $\operatorname{rank}P(\lambda)\le\omega$ for all
   $\lambda$; choosing $\lambda$ with $\lambda U-G$ of full column rank (a nonempty open condition over $\mathbb R$)
   gives $\operatorname{nrank}P=\omega$.
4. *No finite rank drop.* The polynomial identity $PYP=P$, together with $\operatorname{nrank}P=\omega$, says that
   the maximal $\omega$-minors generate the unit ideal; by the reduced criterion this is $(5b)$.

---

# Part III. What the theorem removes

* The $(5a)$ condition and the rank condition come from the two full-rank equations in (A), so no chart is
  selected and no maximal minors are enumerated.
* The spectral condition is the single identity (B).
* All unknowns and coefficients are **real**, and by (3) above the normal-rank hypothesis is automatic, so the
  real-point-density question of the earlier geometric stage does not arise: the system is itself a real system.
* The number of strata is $k+1$, which is polynomial; what used to be exponential was the chart count, and it
  has disappeared.

## III.1 What remains

Only one thing: the **decision complexity** of the real system (A)+(B). Its equations have degree at most two in
the joint variables, its size is $(2\omega-1)\omega q+O(\omega^2+qr)$, and it contains a bilinear block
$H(R)=UV$.

---

# Part IV. Questions

**Question 1.** Is the forward direction correct in taking $H_A=G_0H$ and $G=G_0U$? We rely on the factorisation
$H_A=ZH$ (valid since $\ker H\subseteq\ker H_A$) and then restrict.

**Question 2.** Is step 3 of the reverse direction correct? We assert that $\operatorname{nrank}P=\omega$ follows
from (A) plus the existence of some $\lambda$ with $\lambda U-G$ of full column rank. We believe this is implied
by (B) but we have not separated the two uses.

**Question 3.** Is the real-gcd step in the forward direction correct as stated — namely that a nonconstant gcd
over $\mathbb C[\lambda]$ of real polynomials forces a nonconstant gcd over $\mathbb R[\lambda]$? We argue via
conjugate pairs and real irreducible quadratic factors, but this is the kind of step that has failed before in
this project.

**Question 4.** Given that (A)+(B) is a real polynomial system of degree two and polynomial size, what is the
right way to state the complexity question for it? We would prefer to state the problem once, in this form, and
then ask about it, rather than to keep both the geometric and the algebraic formulations in play.
