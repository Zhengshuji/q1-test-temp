# Audit request: the hyperplane layer, ten claims with proofs

This note asks for two things: a check of the arguments below, and, where they stop, a proof.
Every claim is stated with its proof so that the proof itself can be audited; the labels say what I
believe each claim's status to be. Reports 94–96 are assumed; the new material is the regime analysis
(Claims 5–8) and the two counterexamples (Claims 9–10).

---

## Part I. Setting

$A\in\mathbb Q^{n\times n}$, $C\in\mathbb Q^{p\times n}$ with $\operatorname{rank}C=p$,
$L_0\in\mathbb Q^{r_0\times n}$, $\mathcal L=[L_0;R]$ with $q$ rows,
$K_0=\ker[C;CA]$, $k=\dim K_0$, $N$ a basis of $K_0$, $H=LN$, $H_A=LAN$,
$\omega=\operatorname{rank}H$, $V=\operatorname{row}L$, and
$$
(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \operatorname{rank}(\lambda H-H_A)=\omega\ \ \forall\lambda\in\mathbb C .
$$
Recall $\omega=\dim(V\cap K_0)$.

**The hyperplane layer** is $\omega=k-1$. Then $\ker H$ is a line; write it as $\mathbb C\,v$ with
$v\in K_0$. Put $U=\operatorname{span}(v,Av)$ and $B=\{v\in K_0:\ L_0v=L_0Av=0\}$
(empty $L_0$ means $B=\mathbb P(K_0)$). Each row of $L$ satisfies $rv=rAv=0$, i.e.
$\operatorname{row}L\subseteq U^\perp$.

$v$ is called **eigen** if $\dim U=1$; otherwise **non-eigen** ($\dim U=2$).

For a pencil $P(\lambda)=\lambda H-H_A$ write $m_I$ for its $\omega\times\omega$ maximal minors and
$\mathcal B=\{y:\exists\lambda,\ m_I(y;\lambda)=0\ \forall I\}$ for the bad locus.

---

## Part II. Ten claims

### Claim 1 — components
With $E_\lambda=\mathbb P(K_0\cap\ker(A-\lambda I))\cap B$, $E=\bigcup_\lambda E_\lambda$, and
$B^\circ=B\setminus E$:
$$
Z=Z^\circ\ \cup\bigcup_{\lambda:\,E_\lambda\ne\varnothing}F_\lambda,\qquad
Z^\circ=\overline{\{(\sigma,\text{rows}):\ \sigma\in B^\circ,\ \text{rows}\subseteq U(\sigma)^\perp\}},\quad
F_\lambda=\{\sigma\in E_\lambda,\ \text{rows}\subseteq U(\sigma)^\perp\}.
$$
Each piece is an irreducible component (empty ones aside), and their number is $\le1+\delta$ with
$\delta=\dim(K_0\cap A^{-1}K_0)$.

*Proof.* Coverage: a point lies over $B^\circ$ or over some $E_\lambda$. $Z^\circ$ is the closure of a
vector bundle over the irreducible $B^\circ$; $F_\lambda$ is a vector bundle over the irreducible
$E_\lambda$. Incomparability: $Z^\circ$ projects onto $B^\circ$ while $F_\lambda$ projects to $E_\lambda$;
and over $\sigma\in E_\lambda$ the fibre of $Z^\circ$ is a Grassmannian limit of $(d_0-2)$-dimensional
spaces while $F_\lambda$'s fibre has dimension $d_0-1$. Count: the eigenspaces are independent and
sum into $K_0\cap A^{-1}K_0$. $\square$

**Ask: is the incomparability step (the Grassmannian limit) enough, in particular when $E_\lambda$ is
positive-dimensional?**

### Claim 2 — the bad locus is closed
*Proof.* Homogenise: $M_I(y;s,t)=\det((sH-tH_A)_I)$ is homogeneous of degree $\omega$ and regular in
$(y,s,t)$; $\mathcal D=\{(y,[s:t]):M_I=0\ \forall I\}\subseteq Y\times\mathbb P^1$ is closed. At $t=0$,
$M_I(y;1,0)=\det H_I(y)$, and $\operatorname{rank}H=\omega$ makes some of them nonzero; so $\mathcal D$
avoids $t=0$ and equals the affine incidence. The projection $Y\times\mathbb P^1\to Y$ is proper.
$\square$

**Ask: is the properness step (base change of $\mathbb P^1\to\mathrm{pt}$) acceptable for an *open*
$Y$? I believe yes, but I want it confirmed.**

### Claim 3 — generic-gcd criterion
On an irreducible component $Y$: $Y$ contains a feasible point $\iff$
$\gcd_I m_I=1$ in $\overline{\mathbb Q(Y)}[\lambda]$.

*Proof.* By Claim 2, $\mathcal B$ is closed; $Y$ irreducible. So either $\mathcal B=Y$ or $Y\setminus
\mathcal B$ is a nonempty open dense subset; the generic point decides. $\square$

### Claim 4 — quotient pencil (this is your argument, restated)
Put $C$'s rows first in $Q$ (possible since $U\subseteq K_0\subseteq\ker C$), and take the $K_0$-basis
$[N_1\ v]$. Then $M(\lambda)=Q(\lambda I-A)N$ has first row and last column identically zero, and after
deleting them
$$
B(\lambda)=(\lambda X-G),\qquad X=\begin{bmatrix}Q_1N_1\\Q_2N_1\end{bmatrix}\in\mathbb Q^{2\times2},
\qquad \operatorname{rank}X=2 .
$$
Hence $\deg_\lambda\det B=2$ and $\det B$ has a complex root; so every non-eigen point is bad.

**Ask: no question here — only that Claims 5–8 below build on it.**

### Claim 5 — the rank bound
For any non-eigen point, $\operatorname{rank}\widetilde M(\lambda)\le n-2-p$ for all $\lambda$,
where $\widetilde M$ is the reduced pencil (before deleting the forced kernel column).

*Proof.* Each row $c$ of $C$ lies in $U^\perp$ and satisfies $cN=cAN=0$; hence $c(\lambda I-A)N=0$. So
$M=Q(\lambda I-A)N$ has $p$ identically zero rows among its $n-2$ rows. $\square$

**Ask: correct? In particular, is "the $p$ rows of $C$ are independent as rows of $Q$" automatic
(rank $C=p$)?**

### Claim 6 — for $p=1$ the non-eigen stratum is always bad
Let $r=\operatorname{rank}[C;CA]$, so $k=n-r$. Then
$$
n-2-p\ \gtrless\ k-1\iff r\gtrless p+1 .
$$
For $p=1$, $r\le2=p+1$, so only two cases arise:
- $n-3<k-1$: Claim 5 gives $\operatorname{rank}\widetilde M\le n-3<k-1=\omega$ for all $\lambda$;
- $n-3=k-1$ (i.e. $r=2$): deleting the $p=1$ zero row leaves a square $(k-1)\times(k-1)$ pencil
  $\lambda X'-G'$ with $X'$ invertible (rank $X=k-1$), so $\det$ has degree exactly $k-1\ge1$ and a
  complex root.

Hence for $p=1$ every non-eigen point fails $(5b)$.

**Ask: is this correct as stated? Two places worry me: (i) the case split assumes $r\le2$ for $p=1$,
i.e. that $[C;CA]$ is $2\times n$; (ii) in the critical case I need $X'$ invertible rather than just
$\operatorname{rank}X=k-1$.**

### Claim 7 — the $\lambda=0$ obstruction
If $v\in A K_0$ then $\operatorname{rank}H_A\le\dim(AK_0)-1$.

*Proof.* $\operatorname{rank}H_A=\dim(AK_0)-\dim(AK_0\cap\ker L)=\dim(AK_0)-\dim(AK_0\cap V^\perp)$,
and $V\subseteq v^\perp$ gives $V^\perp\supseteq\operatorname{span}(v)$; if $v\in AK_0$ the intersection
is nonzero. $\square$

**Ask: is the identity $\operatorname{rank}(LAN)=\dim(AK_0)-\dim(AK_0\cap V^\perp)$ correct? I derived
it from $\operatorname{rank}L(Au)=\dim L(AK_0)$, but the bookkeeping is where I have made mistakes.**

### Claim 8 — corollary
If $v$ is an eigenvector with eigenvalue $\lambda_0\ne0$, then $v=A(v/\lambda_0)\in AK_0$, so
feasibility requires $\dim(AK_0)\ge\omega+1=k$. In particular $\operatorname{rank}(A|_{K_0})<k$ makes
the layer infeasible.

**Ask: right? And what is the correct necessary condition when $v\notin AK_0$?**

### Claim 9 — the eigen-fibre sufficiency conjecture is false
Pattern $n=5$, $p=1$, $C=e_5^{\mathsf T}$, and
$$
A=\begin{pmatrix}2&2&-1&0&0\\0&-2&1&0&1\\0&1&-2&0&-1\\0&0&0&0&2\\0&-1&2&0&-1\end{pmatrix}.
$$
Here $v=e_1$ satisfies $Ae_1=2e_1$ and $Ce_1=CAe_1=0$, so $e_1$ is an eigenvector in $K_0$. But
$K_0=\operatorname{span}\{e_1,(0,2,1,0,0),e_4\}$,
$AK_0=\operatorname{span}\{(2,0,0,0,0),(3,-3,0,0,0)\}$, so $\dim(AK_0)=2=\omega$ and $e_1\in AK_0$;
by Claim 7, $\operatorname{rank}H_A\le1<\omega$ at every point of the fibre, so the whole eigen fibre
fails $(5b)$. (Exact check: 20 random layer points, all with $\operatorname{rank}H_A\le1$.)

**Ask: does this refute the conjecture correctly? I want to be sure the fibre really is exactly the
set of admissible row spaces over $E_2$, and that no point of it escapes the argument.**

### Claim 10 — fixed roots are not the only mechanism, and fixed-root checking is not a criterion
Two observations:
(a) In one instance ($n=5$, $p=1$, $r_0=0$, $B=\mathbb P^2$), ten choices of $v$ give eight distinct
monic quadratics whose roots all differ, and all ten points are bad; so all-bad can occur with a
**moving** root and no fixed $\lambda_0$;
(b) in another family, six instances out of sixty have no good point in 24 samples, and the inspected
one has $\operatorname{rank}H_A=2$ (so $\lambda=0$ is fine) but $\gcd\equiv\lambda+2$ — a fixed root
at $\lambda=-2$.

**Ask: (a) is evidence, and I would like your view on whether the "moving root" phenomenon can be
turned into a real obstruction statement; (b) likewise.**

### Claim 11 — in the excess regime the non-eigen stratum can be good
When $r>p+1$ (needs $p\ge2$), the reduced pencil is tall and a good point can exist. Concretely, with
$n=8$, $p=2$, $C=[e_1;e_2]$, $A$'s first two rows $e_3,e_4$ (so $K_0=\operatorname{span}\{e_5,\dots,e_8\}$,
$r=4$, $k=4$, $\omega=3$, reduced pencil $4\times3$), and the $K_0$-part of $A$ having a prescribed
eigenvector: 27 admissible layer points, **18 good, 9 bad**. The bad ones come from the degenerate
choice $AK_0\subseteq K_0$, where the $k-1$ rows in $K_0$ force the pencil to carry the factor
$(\lambda I-B)$ with $B=A|_{K_0}$ (all 23 points of that family were bad).

**Ask: can you prove that for $r>p+1$ the non-eigen stratum is generically good? This seems to be the
one positive piece still missing, and the tall pencil / observability picture suggests it should be
true.**

---

## Part III. Questions, in priority order

1. **Are Claims 2, 5, 6, 7 correct as proved?** These are the load-bearing ones. If any proof has a
   gap, everything downstream (the regime map and the corollary) needs revision.
2. **Claim 6**: is the "$p=1$ ⟹ non-eigen always bad" theorem right, and is the case split complete?
3. **Claim 8**: is the corollary right, and what replaces it when $v\notin AK_0$?
4. **Claim 9**: does the counterexample really settle the sufficiency question?
5. **Claim 11**: a proof of "excess ⟹ generically good" — what is the cleanest route?
6. **The remaining gap**: an actual criterion for the eigen fibres. After Claims 6 and 11, the layer's
   feasibility rests entirely on them, and I have only certificates (a symbolic identity in one
   parameter, and explicit points), no criterion.

### Reliability

| Claim | Label |
|---|---|
| 1, 2, 3 | proved here (subject to this audit) |
| 4 | your argument (Report 96) |
| 5, 6, 7, 8 | proved here (subject to this audit) |
| 9 | proved (structural) + exact check |
| 10 | exact computation; evidence only |
| 11 | exact computation; evidence only |
