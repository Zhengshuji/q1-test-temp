# Class I ($p=r=1$): the quotient pencil, terminal feasibility, and one remaining lemma

This note reports the outcome of the programme you proposed for the smallest case ($p=r=1$, $n$ growing):
the quotient-pencil formulation, the structure of the case, a proof that the terminal order is always feasible, a
reduction of the next order to a containment of a "bad image", and the one lemma that remains open.

Levels: **L1** paper proof; **L2** exact arithmetic; **L3** Lean.

---

# Part I. Setting

$A:X\to X$ ($X=\mathbb C^n$), $C=c^{\mathsf T}$ ($p=1$), $L_0=\ell^{\mathsf T}$ ($r=1$), with
$\operatorname{rank}[C;L_0]=2$ and both pairs observable. A candidate $\mathcal L$ ($q$ rows) satisfies
$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$, $\operatorname{rank}[C;\mathcal L]=1+q$;
$h=\operatorname{rank}[\mathcal L;CA;C]$; conditions $(5a)$, $(5b)$ as usual.
$V=\ker[c;cA]$, $K=\ker[c;\ell]$, $\mathcal Z=\ker[C;\mathcal L]$, $d=n-1-q$.
For an admissible $\mathcal Z$: $S=V\cap\mathcal Z$, $J_{\mathcal Z}x=x+\mathcal Z$,
$T_{\mathcal Z}x=Ax+\mathcal Z$, $N_{\mathcal Z}(\lambda)=T_{\mathcal Z}-\lambda J_{\mathcal Z}$.

---

# Part II. Results

## 1. The quotient pencil (your correction, now proved; L1; L2 1513/1513)

**(5a) forces $A(S)\subseteq\mathcal Z$.** Hence $S\subseteq\ker N_{\mathcal Z}(\lambda)$ for **every** $\lambda$:
so on strata with $S\ne0$ the pencil $N_{\mathcal Z}$ is never of full column rank, and the full-column-rank
criterion is invalid. The correct object is the induced pencil
$$\overline N_{\mathcal Z}(\lambda):V/S\longrightarrow X/\mathcal Z,$$
and
$$(5b)\ \text{holds}\iff\ker N_{\mathcal Z}(\lambda)=S\ \ \forall\lambda
\iff\overline N_{\mathcal Z}(\lambda)\ \text{injective for every}\ \lambda .$$
Computational form: with $V'$ a complement of $S$ in $V$ and $P_{\mathcal Z}$ annihilating $\mathcal Z$,
the matrix $P_{\mathcal Z}(A-\lambda I)V'$ has full column rank for all $\lambda$ iff the gcd of its maximal minors
is a nonzero constant; if $\dim(V/S)=0$ the condition is vacuous. Note the distinction you insisted on: **full
normal rank is not pointwise full rank**.

## 2. Structure of Class I (L1; L2)

With $(c,A)$ observable:
$r_1=\operatorname{rank}[c;cA]=2$; $\dim V=\dim K=n-2$; $\dim(V\cap K)=\dim\ker\{c,cA,\ell\}\ge n-3$;
$s_0=\dim(\operatorname{row}[c;\ell]+W)\in\{2,3\}$ with $s_0=3\iff\ell\notin\operatorname{span}\{c,cA\}$.
Since $r_1+r=3$, **if $\ell\in\operatorname{span}\{c,cA\}$ then no order can fail for counting reasons**; the
interesting class is $\ell\notin\operatorname{span}\{c,cA\}$, where the counting obstruction is possible at every
order.

## 3. The terminal order is always feasible (L1; L2 589/589)

At $q=n-1$, i.e. $d=0$ and $\mathcal Z=0$, **any** $\mathcal L$ with $\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$
and $[c;\mathcal L]$ invertible satisfies $(5a)$ and $(5b)$:
$(5b)$ because failure would need an eigenvector of $A$ inside $V\subseteq\ker c$, and observability forbids that;
$(5a)$ because $\operatorname{rank}[\mathcal L;CA;C]=n$. This is the claim $q_{\min}\le n-1$ proved in this case.

## 4. The next order reduces to a containment (L1; L2 229/229)

Put $\psi:V\times\mathbb C\to\mathbb C^n$, $(x,\lambda)\mapsto(\lambda I-A)x$, and
$\operatorname{im}\psi=\bigcup_\lambda(\lambda I-A)V$.

* $c(\lambda I-A)x=\lambda cx-cAx$, so **$\operatorname{im}\psi\subseteq\ker c$** — the whole bad image lies in the
  hyperplane $\ker c$ (dimension $n-1$).
* For $d=1$, $\mathcal Z=\langle z\rangle$ with $z\in K\setminus0$ and $z\notin V$:
  $$(5b)\ \text{fails at}\ \mathcal Z\iff z\in\operatorname{im}\psi .$$
* Hence at $d=1$: whole-family failure $\iff K\setminus\{0\}\subseteq\operatorname{im}\psi$. Since $\dim K=n-2$
  and $\dim\operatorname{im}\psi\le n-2$, this is dimension-matched: it says the hyperplane $K$ is an irreducible
  component of the bad image.

**Numerics.** With the exact membership test (gcd of the maximal minors of the augmented pencil
$[\lambda B_V-AB_V\mid z]$; *not* sampling rational $\lambda$, which gives false negatives because the relevant
$\lambda$ can be algebraic): the equivalence above holds in 229/229 sampled $(z,\mathcal Z)$ pairs; and over 240
random $z\in K$ the contingency table is

| admissible and in im ψ | not admissible and in im ψ | **admissible and not in im ψ** |
|---|---|---|
| 239 | 1 | **0** |

so at $d=1$ there were no feasible candidates. Combined with item 3: $q_{\min}=n-1$ in every scanned instance
(881 instances over $n=4,\dots,7$, with the orders $q\le n-2$ tested).

## 5. The remaining lemma (open; strong numerical support)

**Claim.** $\operatorname{im}\psi=\ker c$, i.e. every $w$ with $cw=0$ has a representation $w=(\lambda I-A)x$ with
$x\in\ker[c;cA]$.

Evidence: 534/534 random $w\in\ker c$ (over $n=4,5,6$) are members.

*Reduction.* Write $x=(\lambda I-A)^{-1}w$ for $\lambda\notin\operatorname{spec}A$ and let
$f(\lambda)=c(\lambda I-A)^{-1}w$. Since $A(\lambda I-A)^{-1}=\lambda(\lambda I-A)^{-1}-I$,
$$cA(\lambda I-A)^{-1}w=\lambda f(\lambda)-cw=\lambda f(\lambda),$$
so both requirements $cx=0$ and $cAx=0$ collapse to the single equation $f(\lambda)=0$. Thus membership would follow
from "for every $w\in\ker c$ the rational function $f$ has a zero outside $\operatorname{spec}A$".
That is not obvious: $f$ is strictly proper (since $cw=0$, $f=O(\lambda^{-2})$ at infinity), so writing
$f=p/\chi$ with $\chi$ the characteristic polynomial gives $\deg p\le n-2$, and $p$ could in principle be a nonzero
constant. The pencil formulation also allows $\lambda\in\operatorname{spec}A$, where the resolvent argument does not
apply, and we have not settled that case.

---

# Part III. Questions

**Q1 (the remaining lemma).** Do you see a proof — or a counterexample — for $\operatorname{im}\psi=\ker c$?
Our attempts reduce it to "the transfer function $c(\lambda I-A)^{-1}w$ has a zero off the spectrum", which fails for
strictly proper functions in general; the pencil formulation might rescue it at eigenvalues of $A$. If the claim is
false in general, is there a weaker statement (e.g. $K\subseteq\operatorname{im}\psi$ without $K\subseteq\ker c$
playing a role) that would still give $q_{\min}=n-1$?

**Q2 (is Class I worth completing?).** Proving $K\subseteq\operatorname{im}\psi$ would give $d=1$ infeasibility; the
orders with $d\ge2$ would still need separate treatment (there $\mathcal Z$ is higher-dimensional and the "image"
test becomes a statement about subspaces, not lines). Would you carry the case to a complete classification, or stop
at "$d\le1$ plus the terminal order" and treat the rest as out of scope?

**Q3 (the two paths).** With the quotient-pencil formulation now definitive, which do you consider more promising for
the general problem: proving a polynomial algorithm for the constrained pointwise-injective problem, or a hardness
reduction from a subspace-selection problem? Our structural results suggest that infeasibility is thin, which is
awkward for reductions (a gadget must encode the thinness), but we have no strong argument either way.

**Q4 (terminology).** We have adopted your naming (dimension obstruction / spectral obstruction / quotient pencil /
permanent kernel). The "permanent kernel" proposition is now written up as a separate item; would you place it before
or after the dimension-obstruction theorem in a write-up?
