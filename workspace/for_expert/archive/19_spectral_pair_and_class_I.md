# The spectral side as one matrix pair, and the state of Class I at $d\ge2$

This note reports the steps taken after your referee report: the spectral condition has been rewritten as a
statement about **one explicit pair** (a $q\times q$ matrix and a subspace), the equality theorem now appears as a
special case of that, and Class I has been pushed from $d\le1$ (proved) to $d\ge2$ (open, with evidence). The
proofs are written out so that you can check them; the last part asks how to attack the remaining coupling.

Levels: **L1** paper proof; **L2** exact verification on finitely many instances; **L3** machine-checked. We use your
labels: `[Lean-verified]`, `[Lean-conditional]`, `[Paper proof]`, `[Exact verification]`.

---

# Part I. Where we are

Since the last report: the equality case is closed by your theorem B.22 (now in our numbered sequence, with the
stronger conclusion $d_{\rm fin}=q$, $d_\infty=r_1$), B.8b has been corrected to
$h=\sum_i\varepsilon_i+d_{\rm fin}+d_\infty$ (all right minimal indices are degree zero), B.19 now uses the short
proof via $s=n-h$, and B.11d is unconditional under CSS. Internally: five Lean files compiled with zero errors and
zero warnings, an axiom audit shows the thirteen central declarations depend only on `propext`,
`Classical.choice`, `Quot.sound`, and all hygiene gates are clean.

The two new results below are the ones we would like checked.

---

# Part II. The two new results

## B.23 (the pencil factors through one square matrix)

Let $\mathcal L$ satisfy (5a), $\operatorname{rank}\mathcal L=q$. Choose $B\in\mathbb C^{r_1\times n}$ of full row
rank with $\operatorname{row}B=\operatorname{row}[CA;C]$, put $H_0=[\mathcal L;B]$. By (5a),
$\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}H_0$, so $\mathcal LA=KH_0$ for some
$K=[K_1\ K_2]$ with $K_1\in\mathbb C^{q\times q}$, $K_2\in\mathbb C^{q\times r_1}$. Then
$$Q_{\mathcal L}(\lambda)=\begin{bmatrix}\lambda\mathcal L-\mathcal LA\\ B\end{bmatrix}
=P(\lambda)H_0,\qquad P(\lambda)=\begin{bmatrix}\lambda I_q-K_1&-K_2\\ 0&I_{r_1}\end{bmatrix},$$
and for every $\lambda$,
$$\operatorname{rank}Q_{\mathcal L}(\lambda)=\operatorname{rank}H_0-\dim(\ker P(\lambda)\cap\operatorname{im}H_0),
\qquad \det P(\lambda)=\det(\lambda I_q-K_1).$$
Consequently
$$(5b)\ \text{fails}\iff\exists\lambda:\ \ker P(\lambda)\cap\operatorname{im}H_0\ne0,$$
and any such $\lambda$ is an **eigenvalue of $K_1$**.

*Proof.* Block multiplication gives the factorization; $\operatorname{rank}(PH)=\operatorname{rank}H-\dim(\ker P\cap\operatorname{im}H)$
is the standard rank formula for composable maps; the determinant of a block-triangular matrix with unit block is
$\det(\lambda I_q-K_1)$. $\square$

**Exact verification.** 2032 admissible $(q,\mathcal Z)$ samples × 4 values of $\lambda$: the factorization, the
rank equality and the determinant identity all hold (8128/8128 checks).

**Consequence (your B.22 as a corollary).** At $h=q+r_1$ we have $\operatorname{rank}H_0=q+r_1$, so
$\operatorname{im}H_0=\mathbb C^{q+r_1}$; then every eigenvalue of $K_1$ produces a drop, and $K_1$ has $q\ge1$
eigenvalues. This reproduces the equality theorem, and it also shows *why*: at equality there is no subspace left to
hide in.

## B.24 (what the condition actually says)

In the notation of B.23, $\ker P(\lambda)=\{(u,0):(\lambda I_q-K_1)u=0\}=\ker(\lambda I_q-K_1)\oplus\{0\}$, while
$\operatorname{im}H_0=\{(\mathcal Lx,Bx):x\in\mathbb C^n\}$ and $\ker B=(\operatorname{row}B)^\perp
=(\operatorname{row}[CA;C])^\perp=\ker[C;CA]=V$. Hence
$$\ker P(\lambda)\cap\operatorname{im}H_0\ne0\iff\exists x\in V,\ \lambda:\ \mathcal Lx\ne0,\ K_1\mathcal Lx=\lambda\mathcal Lx,$$
i.e.
$$\boxed{(5b)\ \text{fails}\iff\mathcal LV\ \text{contains a nonzero eigenvector of}\ K_1.}$$
This is the observability form of your earlier reduction, with $\Lambda$ replaced by the **explicit, computable**
$K_1$. Since $\dim(\mathcal LV)=\dim V-s=h-2$ (we have $s=n-h$), the spectral condition becomes:

> *there is an $(h-2)$-dimensional subspace — necessarily of the form $\mathcal LV$ for an admissible $\mathcal L$ —
> that avoids every eigenvector of the $q\times q$ matrix $K_1$.*

*Proof.* Direct computation of $\ker P$ plus $\ker B=V$. $\square$

## Class I ($p=r=1$): the state at $d\ge2$

With $h\le q+r_1=q+2$ and $r_1=2$:

* $d=0$ ($q=n-1$): always feasible (terminal order).
* $d=1$ ($q=n-2$): every admissible candidate fails (proved earlier).
* $d\ge2$: **open**. An exhaustive scan (all charts, $\theta\in\{-2,\dots,2\}$ plus random $\theta$; $n=5,6$)
  found 29 instances with admissible candidates at $d=2$ and 1 at $d=3$; in total **47 admissible candidates, none
  feasible**.

The dimension count does **not** forbid feasibility at $d\ge2$: when $h\le q+1$ the space $\mathcal LV$ is a proper
subspace of $\mathbb C^q$, and a generic proper subspace avoids finitely many eigenvector directions. So whatever
forces failure must come from the coupling between $(5a)$ and $K_1$ — precisely the coupling that, at $d=1$, we
handled with the canonical-coordinate recursion ($\deg P_z=n-2\ge1$).

---

# Part III. Questions

**Q1 (the coupling).** At $d\ge2$ we must show: for admissible $\mathcal L$, $\mathcal LV$ contains an eigenvector of
$K_1$. Do you see a route? At $d=1$ the proof came from writing everything in the cyclic basis of $(c,A)$ and
counting degrees in the recursion $x_{k+1}=\lambda x_k-w_k$. Is there an analogous normal form for
$(K_1,\mathcal LV)$ at higher $d$, or would you go through the incidence variety
$\{(\mathcal Z,[x],\lambda):x\in V\setminus\mathcal Z,\ (\lambda I-A)x\in\mathcal Z\}$ instead?

**Q2 (is there a structural reason we are missing?).** The evidence says $d\ge2$ always fails, yet no dimension
argument forces it. Is there an obstruction of a different kind — for instance, that admissibility makes $\mathcal L$
"too small" to hide an eigenvector, or that $\mathcal LV$ must contain the range of some projection determined by
$K_1$?

**Q3 (what to formalize).** B.23/B.24 live in the matrix-rank layer (the identity $\operatorname{rank}(PH)=\operatorname{rank}H-\dim(\ker P\cap\operatorname{im}H)$ and the block determinant). Would you prioritize formalizing this layer, or is the paper proof enough for now, with the effort better spent on $d\ge2$?

**Q4 (how to state Class I in the paper).** We can prove $d\le1$ and have strong evidence for $d\ge2$. Should
$q_{\min}=n-1$ for Class I be stated as a conjecture with the $d\le1$ theorem as partial evidence, or would you
state only the $d\le1$ result and leave the minimum-order question out of the paper?

**Q5 (the paper layer).** With B.22 in place, the dichotomy
$h\ge q+r_1\Rightarrow(5b)$ fails is unconditional. Do you now consider the counting/spectral framework ready to be
written up as a theorem sequence, with B.8b's $d_\infty$ bookkeeping and Class I's $d\ge2$ as the only open items?
