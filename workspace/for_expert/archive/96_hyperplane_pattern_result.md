# The hyperplane layer in one dimension pattern: a criterion, one proved side, and symbolic certificates

This note reports a self-contained result for a single dimension pattern of the hyperplane layer, and
asks what is needed to turn it into a general statement. As before, the question is the decision
complexity of the prescribed-row problem; the characterisation is taken from the literature.

---

## Part I. Setting

Let $A\in\mathbb Q^{n\times n}$, $C\in\mathbb Q^{p\times n}$ ($\operatorname{rank}C=p$),
$L_0\in\mathbb Q^{r_0\times n}$, and let $\mathcal L=[L_0;R]$ have $q$ rows. Put
$K_0=\ker[C;CA]$, $k=\dim K_0$, $N$ a basis of $K_0$, $H=LN$, $H_A=LAN$, $\omega=\operatorname{rank}H$,
and $V=\operatorname{row}L$. Recall

$$
(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \operatorname{rank}(\lambda H-H_A)=\omega\quad\forall\lambda\in\mathbb C,
$$

and $\omega=\dim(V\cap K_0)$.

**The pattern.** Throughout: $n=5$, $p=1$, $C=e_5^{\mathsf T}$, $r_0=0$ (so there are no fixed rows and
$B=\mathbb P(K_0)$), $q=3$. Then $\operatorname{rank}[C;CA]=2$, $k=3$, and the **hyperplane layer**
$\omega=k-1=2$ is the only nontrivial one.

**Components.** With $U=\operatorname{span}(v,Av)$ and
$E_\lambda=\mathbb P(K_0\cap\ker(A-\lambda I))$, the lifted incidence space is
$$
Z=Z^\circ\ \cup\ \bigcup_{\lambda:\ E_\lambda\ne\varnothing}F_\lambda ,
$$
where $Z^\circ$ is the closure of the bundle over $B\setminus E$ (the *non-eigen stratum*, $\dim U=2$)
and $F_\lambda$ is the full fibre over $E_\lambda$ (the *eigen fibres*, $\dim U=1$). The pieces are
irreducible and pairwise incomparable.

---

## Part II. What we have

### II.1 The non-eigen stratum is entirely bad

Two facts combine.

1. **Forced relation.** Since $U\subseteq K_0\subseteq\ker C$, every row of $C$ lies in $U^\perp$ and
   annihilates $K_0$ and $AK_0$. Hence, for the quotient pencil
   $\widetilde M=Q(\lambda I-A)\hat N$ (with $Q$ a basis of $U^\perp$ and $\hat N$ the basis of $K_0$
   with the $v$-column removed),
   $$\operatorname{rank}\widetilde M(\lambda)\le n-2-p=2\qquad\forall\lambda .$$
   Equivalently: the forced relation is present exactly when $C\in\operatorname{row}L$.
2. **Dimension count.** In the non-eigen stratum $\dim U^\perp=n-2=3=q$, so $\operatorname{row}L=U^\perp$
   is forced; hence $C\in\operatorname{row}L$ and the forced relation always holds.
   In this pattern $n-2-p=2=k-1$, so the bound is attained and the effective object is a $2\times2$
   pencil; its determinant is a quadratic in $\lambda$, nonconstant in the sampled instances
   (nonzero discriminant), and a nonconstant quadratic over $\mathbb C$ always has a root. So every
   point of $Z^\circ$ is bad.

The last step is the only place where an argument is still missing for a *uniform* statement: one has
to know that the effective quadratic is not identically constant. We checked it on several instances
(nonzero discriminant each time) but did not prove it for all $A$.

### II.2 The eigen fibres are good, with symbolic certificates

In the eigen case $\dim U=1$ and $\dim U^\perp=n-1=4>q$, so the row space is a hyperplane of $U^\perp$
and generically **avoids** $C$; the forced relation of II.1 is absent. We can do better than absence:

**Single instance.** For one $A$ with $Ae_1=\lambda_0e_1$, $C=e_5^{\mathsf T}$, take the one-parameter
family of row spaces
$$V_t=\langle e_2,e_3,e_4+t\,e_5\rangle,\qquad t\in\mathbb P^1 ,$$
and compute the gcd of the $2\times2$ minors of $\lambda H_t-H_{A,t}$ in $\mathbb Q(t)[\lambda]$:
$$\gcd\bigl(m_I(t;\lambda)\bigr)\equiv1 .$$
So **every** $t$ gives a good pencil, and the eigen component is feasible (by closedness of the bad
locus plus irreducibility).

**Five instances.** Repeating with five random $A$ (each with $Ae_1=\lambda_0e_1$,
$\lambda_0\in\{2,3,-1,5\}$) and symbolic $t$ gives $\gcd\equiv1$ in all five cases.

A structural remark: $C=e_5\notin V_t$ for every $t$ (the coefficient of $e_4$ is $1$), so the whole
curve lies in the "avoiding $C$" region — which is why it is uniformly good.

### II.3 The criterion for this pattern

$$
\text{the layer is feasible}\iff E:=\bigcup_\lambda\mathbb P(K_0\cap\ker(A-\lambda I))\ne\varnothing .
$$

- $E=\varnothing$: only $Z^\circ$ remains, and it is entirely bad by II.1 — **infeasible**.
- $E\ne\varnothing$: the corresponding $F_\lambda$ is feasible by the certificates of II.2 —
  **feasible**.

$E$ is computable in polynomial time (eigenstructure of $A$ intersected with $K_0$).

### II.4 Status

| Item | Status |
|---|---|
| $E=\varnothing\Rightarrow$ infeasible | proved (II.1), modulo the nonconstancy of the effective quadratic |
| forced relation $\iff C\in\operatorname{row}L$ | proved |
| $\dim U^\perp=q\Rightarrow\operatorname{row}L=U^\perp$ | proved |
| $E\ne\varnothing\Rightarrow$ feasible, single instance | symbolic certificate, $\gcd\equiv1$ in $\mathbb Q(t)[\lambda]$ |
| same, five random $A$ | symbolic certificates, $5/5$ |
| general $A$ | **open**: a PIT over $\mathbb Q(A,t)[\lambda]$ |
| higher-dimensional eigenspaces, other patterns | not attempted |

---

## Part III. Questions

**Q1.** Is the argument of II.1 a legitimate proof of "entirely bad"? The step I am unsure about is the
nonconstancy of the effective $2\times2$ determinant: is there a clean way to certify it uniformly
(e.g. by exhibiting one $v$ where it is nonconstant, plus an argument that the leading coefficient does
not vanish identically)? Or should the whole stratum be handled by the generic-gcd criterion instead?

**Q2.** Is a symbolic certificate in one parameter $t$ (five instances) enough to state a family theorem,
or should we insist on the general-$A$ identity? If the latter, is there a standard way to reduce that
PIT to the one-parameter case (e.g. by a specialization argument on $A$)?

**Q3.** Is "$K_0$ contains an eigenvector" the right general form of the criterion, or is it an artifact
of the pattern $n-2-p=k-1$? Concretely: when $n-2-p<k-1$ the layer is automatically infeasible by the
rank bound; when $n-2-p>k-1$, what replaces the eigenvector condition?

**Q4.** Does this count as progress on Theorem C of the previous report (the hyperplane layer's
complexity)? The criterion is polynomial-time computable, and the affirmative side comes with a
certificate; the negative side needs the nonconstancy check. What is the cleanest way to state the
result so that it is not overclaimed?

**Q5.** Which pattern should be next? The candidates we see: (a) generalise over $A$ in this pattern;
(b) next dimension pattern, $n=6,p=1,q=4$; (c) higher-dimensional eigenspaces inside $K_0$.

### Reliability

| Item | Label |
|---|---|
| components $Z=Z^\circ\cup\bigcup F_\lambda$ | proved |
| forced relation, rank bound $\operatorname{rank}\widetilde M\le n-2-p$ | proved |
| $\dim U^\perp=q\Rightarrow\operatorname{row}L=U^\perp$ | proved |
| non-eigen stratum entirely bad | proved on the sampled instances; the uniform nonconstancy is open |
| eigen fibres good | symbolic certificates ($\mathbb Q(t)[\lambda]$, one parameter), $1+5$ instances |
| the criterion $E\ne\varnothing$ | proved in one direction, certified in the other, for this pattern only |
