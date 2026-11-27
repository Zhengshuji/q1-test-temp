# Paper proofs for review: the propositions that are not machine-checked

This note has one purpose: to put the **paper proofs** in front of you for checking, for the parts of the project
that could not be formalised. Part II states each proposition and its full proof. Part III reports progress,
difficulties and specific questions.

For orientation on the verification levels used below: **L1** = paper proof written out and self-checked;
**L2** = exact rational/integer arithmetic on finite instances (a filter, never a confirmation);
**L3** = machine-checked (Lean 4 + Mathlib, `lake env lean` exit code 0, declaration names given).

---

# Part I. Setting and what is already machine-checked

## I.1 The problem

$A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$ with
$\operatorname{rank}[C;L_0]=p+r$. A candidate $\mathcal L\in\mathbb C^{q\times n}$ satisfies
$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$ and $\operatorname{rank}[C;\mathcal L]=p+q$ (so
$\operatorname{rank}\mathcal L=q$). The two conditions are

$$(5a)\ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=h\ \ \forall\lambda\in\mathbb C,$$

with $h:=\operatorname{rank}[\mathcal L;CA;C]$ the normal rank of the pencil
$Q_{\mathcal L}(\lambda)=[\lambda\mathcal L-\mathcal LA;CA;C]$ (an $(q+2p)\times n$ pencil). $q_{\min}$ is the least
$q$ for which both hold.

## I.2 Notation

* $\mathcal J:=\operatorname{row}[C;CA]$, $r_1:=\dim\mathcal J=\operatorname{rank}[C;CA]$, $W:=\mathcal J$;
* $\mathcal Z:=\ker[C;\mathcal L]$ (dimension $d=n-p-q$), so $\mathcal Z^\perp=\operatorname{row}[C;\mathcal L]$;
* $\eta_j$ = right minimal indices of $Q_{\mathcal L}$, $\varepsilon_i$ = left minimal indices,
  $d_{\rm fin}$ = total degree of the finite elementary divisors, $d_\infty$ = total degree of the infinite ones;
* **Type I** = $h\ge q+r_1$ (counting obstruction); **Type III** = $h<q+r_1$ but $d_{\rm fin}>0$ (spectral
  obstruction). There is no third case (see II.4).

## I.3 What is Lean-checked, and what this note is about

The following are already **L3**, so they do not need review here (declaration names are given so the statements
can be inspected without reading code):

| Proposition | Lean declarations |
|---|---|
| pencil reformulation $(5b)\iff\operatorname{rank}Q_{\mathcal V}(\lambda)=\rho\ \forall\lambda$ | `PencilEquivalence.pencil_rank_eq`, `pencil_rank_forall` |
| B.2 (top layer $\rho=d$: observability of $(D_W,T_W)$) | `B2Block.block_on_J`, `block_on_W`, `block_on_W_compression` |
| B.3 ($\rho=0$ layer) | `Rho0Layer.rho_zero_iff`, `five_a_of_le`, `five_b_auto` |
| B.4 ($V=\mathbb C^n$ criterion) | `B4FullSpace.b4_iff_no_eigenvector` |
| B.5 (cyclic-vector criterion) | `CyclicVector.isCyclic_iff`, `cyclic_iff_no_left_eigen`, `not_cyclic_of_left_eigen`, `exists_left_eigen_of_not_cyclic`; `CyclicStructural.b5_converse` |
| B.9b (counting case "Type II" is empty) | `TypeII.typeII_rank_mono`, `typeII_vacuous`, `typeII_vacuous_geometric` |
| B.11 ($h=\dim(\mathcal Z^\perp+W)$) | `TypeIGeom.B11_dim` |
| B.11b ($h=q+r_1-\dim(\pi R\cap\pi W)$) | `TypeIGeom.mkQ_map_inf_eq`, `typeI_dim`, `typeI_geometric` |
| A.0, first step ($(5a)\iff\operatorname{row}\mathcal LA\subseteq\operatorname{row}[\mathcal L;CA;C]$) | `A0Row.five_a_row_iff`, `rank_eq_of_rowSpace_le` |
| row-space bridge used above | `RowSpace.rowSpace_from_rows`, `rank_le_rank_fromRows` |

What remains **L1 + L2 only**, and is the subject of Part II, is the left-index/Kronecker chain (B.6–B.9), the
spectral confinement B.10, the dimension obstruction with its uniformity statement, the whole-family counterexample,
and the quotient form of $(5a)$. Each needs local Smith/Kronecker theory or polynomial-matrix ranks, which the
library does not provide; that is why they are here.

---

# Part II. The paper proofs

## II.1 B.6 — the right minimal indices of $Q_{\mathcal L}$ are all zero

**Proposition.** If $(5a)$ holds then the right null module of $Q_{\mathcal L}$ has a constant basis; equivalently
$\sum_j\eta_j=0$. Only $(5a)$ is used.

**Proof.** From $(5a)$, $\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}[\mathcal L;CA;C]$, so there are
matrices $X,Y_1,Y_2$ with
$$(\ast)\qquad \mathcal LA=X\mathcal L+Y_1CA+Y_2C .$$
Let $v(\lambda)=\sum_{k=0}^{d}\lambda^kv_k\ne0$ be a polynomial vector with $Q_{\mathcal L}(\lambda)v(\lambda)=0$;
equivalently
$$(\lambda\mathcal L-\mathcal LA)v(\lambda)=0,\qquad CA\,v(\lambda)=0,\qquad C\,v(\lambda)=0 .$$
Reading the coefficients from the top: the $\lambda^{d+1}$ coefficient of the first identity is
$\mathcal L v_d=0$; the $\lambda^d$ coefficient gives $\mathcal Lv_{d-1}-\mathcal LAv_d=0$, and the $\lambda^d$
coefficients of the other two give $CAv_d=Cv_d=0$. Hence $v_d\in\ker\mathcal L\cap\ker C\cap\ker CA$; feeding this
into $(\ast)$ gives $\mathcal LAv_d=X\mathcal Lv_d+Y_1CAv_d+Y_2Cv_d=0$. So $v_d$ lies in the constant space
$N:=\ker\mathcal L\cap\ker LA\cap\ker C\cap\ker CA$, and $\lambda^dv_d$ is itself a polynomial null vector. Subtract
it and repeat: $d$ decreases, so induction terminates with a null vector of degree $0$. Hence the right null module
is generated by constant vectors, i.e. it is free and all right minimal indices vanish. $\square$

**Status.** L1 + L2 (150/150 pencils at $n=6,7,8$). The Lean kernel covers exactly the coefficient induction
(`KronCoeff.kron_coeff_chain_strong`, `kron_coeff_mem_N`); the translation "polynomial vector ↔ coefficient
sequence" and the step "constant basis ⟹ Kronecker indices zero" are paper. **Please check:** the induction and the
use of $(\ast)$; in particular that $\mathcal LAv_d=0$ follows from $v_d\in\ker\mathcal L\cap\ker C\cap\ker CA$ and
$(\ast)$ alone (I believe yes, but this is the one place where the row-space argument is used).

**Remark.** This is not a general fact about constant-rank pencils: $[\lambda\ \ 1]$ has constant rank 1 and a
right index 1. The block structure of $Q_{\mathcal L}$ together with $(5a)$ is what makes it work.

## II.2 B.7 — the infinite elementary divisors are all of degree one

**Proposition.** If $(5a)$ holds and $h=\operatorname{rank}[\mathcal L;CA;C]$, then all infinite elementary divisors
of $Q_{\mathcal L}$ have degree one; hence $d_\infty=h-\operatorname{rank}\mathcal L$. Only $(5a)$ is used.

**Proof.** Use $(\ast)$ to write
$$\lambda\mathcal L-\mathcal LA=(\lambda I-X)\mathcal L-Y_1CA-Y_2C,$$
so $Q_{\mathcal L}(\lambda)=D(\lambda)H$ with
$$D(\lambda)=\begin{pmatrix}\lambda I-X&-Y_1&-Y_2\\0&I&0\\0&0&I\end{pmatrix},\qquad
H=\begin{pmatrix}\mathcal L\\CA\\C\end{pmatrix}.$$
The infinite elementary divisors of a pencil are those of its reversed pencil at $\mu=0$. In the reversed variable,
$D$ becomes block triangular with diagonal blocks $I-\mu X$, $\mu I$, $\mu I$; the only possible contribution at
$\mu=0$ comes from the first block, whose value at $\mu=0$ is the identity, i.e. it contributes no divisor. Hence
$Q_{\mathcal L}$ and $H$ have the same infinite elementary divisors, and those of $H$ — a constant matrix of rank
$h$ — are $h-\operatorname{rank}\mathcal L$ copies of $\mu$ (locally $H$ is equivalent to
$[\,\operatorname{diag}(I_{\operatorname{rank}\mathcal L},0)\,;\,\mu\cdot(\dots)\,]$, whose determinant divisors are
$\Delta_k=\mu^{\,k-\operatorname{rank}\mathcal L}$ for $k>\operatorname{rank}\mathcal L$). Summing degrees gives
$d_\infty=h-\operatorname{rank}\mathcal L$. $\square$

**Status.** L1 + L2 (151/151 at $n=6,\dots,10$, including 43 infeasible). Lean covers the factorisation identity
`KronFactor.kron_block_factor`; the local Smith computation at $\mu=0$ is paper. **Please check:** the claim that
the first block of the reversed $D$ contributes nothing at $\mu=0$ — equivalently, that multiplying by $D(\lambda)$
does not change the infinite divisors even though $\det D(\lambda)=\det(\lambda I-X)$ is not constant. My argument
is that $D$ has no infinite elementary divisors itself; if there is a standard reference for this step I would
rather cite it.

## II.3 B.8 — the discrete form of the spectral condition

**Proposition.** Under $(5a)$,
$$(5b)\iff d_{\rm fin}=0\iff\sum_i\varepsilon_i=\operatorname{rank}\mathcal L .$$

**Proof.** $(5b)$ says the rank of $Q_{\mathcal L}(\lambda)$ is constant in $\lambda$, which is the same as saying
there are no finite elementary divisors with a $\lambda$-dependence, i.e. $d_{\rm fin}=0$. For the second
equivalence use the standard index identity for an $(q+2p)\times n$ pencil of normal rank $h$,
$$\sum_j\eta_j+\sum_i\varepsilon_i+d_{\rm fin}+d_\infty=h,$$
together with $\sum_j\eta_j=0$ (B.6) and $d_\infty=h-\operatorname{rank}\mathcal L$ (B.7): this gives
$\sum_i\varepsilon_i=\operatorname{rank}\mathcal L-d_{\rm fin}$, so $d_{\rm fin}=0$ iff
$\sum_i\varepsilon_i=\operatorname{rank}\mathcal L$. $\square$

**Status.** L1, with both sides of the equivalence checked exactly in the verification script. **Please check:** the
index identity as I use it (degrees counted on both sides, left indices on the row side); it is standard, but the
conventions differ between sources and everything downstream depends on this one.

## II.4 B.9 — the counting obstruction: $(5b)$ forces $h<q+r_1$

**Proposition.** Under $(5a)$, if $(5b)$ holds then $h<q+r_1$. Equivalently: the number of nonzero left minimal
indices of $Q_{\mathcal L}$ is $q+r_1-h$, so $h\ge q+r_1$ leaves none.

**Proof.** $Q_{\mathcal L}$ has $q+2p$ rows. A **constant** left null vector $\varphi=(\varphi_1,\varphi_2,\varphi_3)$
satisfies $\varphi_1\mathcal L=0$ and $\varphi_1\mathcal LA=\varphi_2CA+\varphi_3C$. Since $\mathcal L$ has full row
rank, $\varphi_1=0$; then $(\varphi_2,\varphi_3)\in\ker_{\rm left}[CA;C]$, whose dimension is
$2p-\operatorname{rank}[CA;C]=2p-r_1$. These constant vectors are exactly the zero left indices, so there are
$2p-r_1$ of them.

The total number of left indices equals $q+2p-h$: the left null module is the kernel of the map
$\mathbb C[\lambda]^{q+2p}\to\mathbb C[\lambda]^{n}$ given by $Q_{\mathcal L}$, hence is free of rank
$q+2p-h$ (it is a kernel over a PID, and its rank is rows minus the normal rank), and a free left null module of
rank $k$ has exactly $k$ left indices. Therefore the number of **nonzero** left indices is
$$(q+2p-h)-(2p-r_1)=q+r_1-h .$$
If $h\ge q+r_1$ this number is $\le0$, so all left indices are zero, $\sum_i\varepsilon_i=0$, and by B.8
$d_{\rm fin}=\operatorname{rank}\mathcal L=q>0$, i.e. $(5b)$ fails. $\square$

**Status.** L1 + L2 (56/56 and 698/698 in two independent scripts). **Please check:** the identification of the
constant left null vectors with the zero left indices, and the count $q+2p-h$ of *all* left indices (I use only that
the left null module is a kernel over a PID, hence free of that rank — B.6 is needed for B.8, not for this count).
This proposition is the basis of the whole "counting versus spectral" separation, so an error here would propagate.

## II.5 B.10 — the spectral obstruction is confined to $\operatorname{spec}\Lambda$

**Proposition.** Write $(\ast)$ as $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ (with $\Lambda:=X$,
$G_0:=Y_2$, $G_1:=Y_1$). Then for $\lambda\notin\operatorname{spec}\Lambda$ we have
$\operatorname{rank}Q_{\mathcal L}(\lambda)=h$; consequently $(5b)$ need only be checked at the eigenvalues of
$\Lambda$.

**Proof.** With $H=[\mathcal L;CA;C]$ and
$D(\lambda)=\begin{pmatrix}\lambda I-\Lambda&-G_1&-G_0\\0&I&0\\0&0&I\end{pmatrix}$ we have
$Q_{\mathcal L}(\lambda)=D(\lambda)H$. If $\lambda\notin\operatorname{spec}\Lambda$ then $\lambda I-\Lambda$ is
invertible, so $D(\lambda)$ is invertible (block triangular with invertible diagonal blocks), hence
$\operatorname{rank}Q_{\mathcal L}(\lambda)=\operatorname{rank}H=h$. $\square$

**Status.** L1 + L2 (3/3, and the bad eigenvalue of one candidate is a **complex** root, so scanning rational
$\lambda$ misses it). **Please check:** that $(\ast)$ really is available with $\Lambda$ of size $q$ and that no
extra hypothesis (e.g. $\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$) is needed for it.

## II.6 The dimension obstruction and its uniformity statement

**Proposition (dimension formula).** $h=\dim(\mathcal Z^\perp+W)$. Moreover, with
$\delta:=\dim(\mathcal Z^\perp\cap W)-p\ (\ge0$, because $\operatorname{row}C\subseteq\mathcal Z^\perp\cap W)$,
$$h=q+r_1-\delta .$$
Hence Type I ($h\ge q+r_1$) holds exactly when $\delta=0$, i.e. exactly when
$\mathcal Z^\perp\cap W=\operatorname{row}C$.

**Proof.** $\operatorname{row}\mathcal L+W=\mathcal Z^\perp+W$, because $\operatorname{row}\mathcal L\subseteq
\mathcal Z^\perp$ and $\mathcal Z^\perp=\operatorname{row}C+\operatorname{row}\mathcal L\subseteq W+
\operatorname{row}\mathcal L$. Then $h=\dim(\operatorname{row}\mathcal L+W)=q+r_1-\dim(\operatorname{row}
\mathcal L\cap W)$ and, by the modular formula applied to $\operatorname{row}C\subseteq W$,
$\dim(\mathcal Z^\perp\cap W)=\dim(\operatorname{row}\mathcal L\cap W)+p$. $\square$

**Proposition (uniformity, conditional).** Let $S:=\operatorname{row}[C;L_0]+W$, $s_0:=\dim S$. Suppose the
augmentation satisfies $V'\cap S=0$ for the "new" part $V'$ of the chart, equivalently $\dim\pi(V')=q-r$. Then
$$h\ge q+r_1\iff s_0\ge r_1+r,$$
an inequality that **does not involve $\mathcal L$**. Hence on such a chart the whole augmentation family is of the
same type: either all Type I or all not.

**Proof.** Under the hypothesis $h=s_0+q-r$ (this is the uniformity identity; it is where the hypothesis is used),
so $h\ge q+r_1\iff s_0+q-r\ge q+r_1\iff s_0\ge r_1+r$. $\square$

**Status.** L1 + L2 (240/240 for the dimension formula; 495/495 for the uniformity with its hypothesis; 117/117 for
"$h=n$ implies $(5a)$ automatic"). **Please check, and this is my main reason for putting it here:** the uniformity
identity $h=s_0+q-r$ is used with a hypothesis ($V'\cap S=0$) that I have not been able to relate to the rest of the
notation in a way I fully trust, and the notation $V'$ itself is defined operationally in our notes rather than
intrinsically. If you can tell me the invariant form of this hypothesis — or a counterexample showing that the
identity can fail on a whole chart — that would settle a question we keep circling.

**Two consequences we do use** (both L1, the first also 18/18 with no false positive in an exact scan):

* $\dim(\operatorname{row}L_0\cap W)\le p\Longrightarrow$ every $(5a)$-admissible augmentation at $q_0$ is Type I
  $\Longrightarrow q_{\min}>q_0$;
* if $V'\cap S=0$ and $s_0\ge r_1+r$ then the *entire* family at that order is infeasible.

## II.7 The whole-family counterexample at $q_0$

**Proposition.** There is an instance with $n=6$, $p=r=2$, $q_0=3$, $r_1=4$, $s_0=5$, $t=1$, such that **every**
$(5a)$-admissible augmentation at $q_0$ fails $(5b)$; its $q_{\min}$ is $4$.

The instance: $A$ is the direct sum of three Jordan blocks of size 2 (eigenvalues $1,2,1$),
$$A=\begin{pmatrix}1&1&&&&\\&1&&&&\\&&2&1&&\\&&&2&&\\&&&&1&1\\&&&&&1\end{pmatrix},\qquad
C=\begin{pmatrix}0&0&1&1&1&1\\1&0&0&0&0&0\end{pmatrix},\qquad
L_0=\begin{pmatrix}0&0&8&20&1&4\\1&3&0&0&0&0\end{pmatrix}.$$

**Proof, step 1 ($(5a)$ is automatic).** Here $s_0=5$ and $t=q_0-r=1$, so by the dimension formula
$h=s_0+t=6=n$; hence $\mathcal Z^\perp+W=\mathbb C^6$ and $(5a)$ holds for **every** $\mathcal Z$. (Consequently the
whole Grassmannian of admissible $\mathcal Z$'s has to be excluded by the spectral condition alone.)

**Proof, step 2 (every $\mathcal Z$ has a rank-dropping $\lambda$).** Let $V=\ker[C;CA]$ ($\dim V=2$). For $x\in V$
with $L_0x\ne0$ define $\lambda(x):=L_0Ax/L_0x$ and $z(x):=(\lambda(x)I-A)x$. Then $Cz(x)=0$ and
$L_0z(x)=L_0Ax-\lambda(x)L_0x=0$, so $z(x)\in\ker[C;L_0]$. Taking $\mathcal Z=\operatorname{span}z(x)$ gives
$(\lambda(x)I-A)x=z(x)\in\mathcal Z\subseteq\ker\mathcal L$, hence
$$[\lambda(x)\mathcal L-\mathcal LA;CA;C]\,x=0,\qquad x\ne0,$$
so $\operatorname{rank}Q_{\mathcal L}(\lambda(x))<h$.

It remains to see that **every** $\mathcal Z$ arises this way. The map $\Phi:\mathbb P(V)\to\mathbb P(\ker[C;L_0])$,
$x\mapsto\operatorname{span}z(x)$, is a morphism of projective lines; it is not constant (two distinct images occur),
hence it is surjective, so every one-dimensional $\mathcal Z\subseteq\ker[C;L_0]$, and therefore every admissible
$\mathcal Z$ of dimension $d=1$, is hit. $\square$

**Status.** L1 + L2, and there are **three further independent proofs**: (i) a per-chart symbolic gcd computation
over $\mathbb Q(\theta)[\lambda]$, where both charts have generic degree $2$ and the only exceptional parameters
($\theta=5/4$, $\theta=4/5$, the zeros of the denominators) give degree $1$ — never $0$, so the "drop locus" is
empty; (ii) a Bézout coefficient-matrix computation whose left null space yields two polynomials in $\theta$ that
generate the unit ideal; (iii) a $\theta$-only determinantal elimination of the joint system $(5a)+(5b)$, whose
Gröbner basis is $[1]$ on both charts. **Please check:** step 2's surjectivity argument — a morphism of projective
lines that is not constant is surjective, which needs the image to be closed; I think this is fine because
$\mathbb P^1$ is complete and the map is a morphism (not merely a rational map) on the chart where $L_0x\ne0$, but
this is precisely the kind of step where we have erred before.

## II.8 The quotient form of $(5a)$ — the step that is not machine-checked

**Proposition.** Let $\pi$ be the quotient map modulo $\mathcal J$. Then
$$(5a)\iff\pi(\mathcal VA)\subseteq\pi(\mathcal V)\quad\text{(equivalently }\pi(\mathcal LA)\subseteq
\pi(\operatorname{row}\mathcal L)) .$$

**Proof.** $(5a)\iff\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}\mathcal L+\mathcal J$ (the first
step is machine-checked); taking $\pi$ gives the claim. $\square$

**Status.** The first step is L3 (`A0Row.five_a_row_iff`); the quotient step is L1. **Please check:** we also rely on
the *negative* statement recorded earlier in our correspondence, namely that the implication
"$\overline T(\overline U)\subseteq\overline U\Rightarrow(5a)$" fails, where $\overline T$ is induced by $A$ on
$X/B$ with $B=\pi(\mathcal J A)$ and $\overline U=(U+B)/B$ with $U=\pi(\mathcal V)$. I would like this negative
statement either confirmed with your counterexample or dropped from our notes.

---

# Part III. Progress, difficulties, questions

## III.1 Where the project stands

* **The classification collapsed from three cases to two.** The counting case "Type II"
  ($k:=q+r_1-h>\operatorname{rank}\mathcal L$) is **empty**: $h\ge r_1$ (row stacking) and
  $\operatorname{rank}\mathcal L=q$ give $k\le q$. This is machine-checked. So $(5b)$ fails for exactly two
  reasons: counting (Type I) and spectral (Type III).
* **Type I has a geometric form** that is machine-checked: with $R=\operatorname{row}\mathcal L$ and
  $\pi=\pi_{\operatorname{row}C}$, $h=q+r_1-\dim(\pi R\cap\pi W)$, so Type I $\iff\pi R\cap\pi W=0$, i.e. "$R$
  avoids $W$ modulo $\operatorname{row}C$". A consequence we can state without any spectral theory: if
  $q+\dim\pi W>n-p$ then **no** $R$ avoids $W$, so Type I cannot occur at that order; and if
  $q+\dim\pi W\le n-p$ then avoidance is the generic situation, so the interesting case is exactly the one where
  $(5a)$ forces $R$ into the incidence variety.
* **The counterexample now has four independent proofs** (one geometric, three algebraic), and the family is
  excluded for *every* parameter, not just for a sample.
* **A per-order decision procedure** exists and is certificate-based: each order is reported as feasible (with an
  explicit $\mathcal L$ and seven consistency checks), or infeasible with an integer, an algebraic-emptiness, or a
  gcd certificate; otherwise unknown. On 26 instances at $q_0$ it decides 24 with certificates in about 20 seconds.
* **The encoding size of the natural algebraic formulation is exponential**: the number of maximal minors of
  $P_{\mathcal Z}(\lambda)$ is $\binom{1.5n-3}{n}$ in the controlled regime, and the number of charts is
  $\binom{n-2}{\lfloor n/2\rfloor-1}$. So the subdeterminant/Bézout route does **not** give a polynomial-size
  $\exists\mathbb R$ instance, and no polynomial algorithm can proceed by enumerating charts and minors.
* **Empirical regularity, unproved.** At $q_0$: 55 of 74 instances with witnesses have $q_{\min}=q_0$; the gap
  concentrates on $r=1$; and the sufficient condition
  $\dim(\operatorname{row}L_0\cap W)\le p\Rightarrow q_{\min}>q_0$ had 18 hits and no false positive.

## III.2 Difficulties

1. **The rank-drop locus.** $\operatorname{rank}[V\,|\,Z(\theta)]$ drops at special parameters, which changes the
   size of the maximal minors; this invalidated an earlier version of our decision procedure. Stratifying by the
   rank works for charts with one parameter but the double stratification (rank of the pencil, rank of
   $[\mathcal Z^\perp|W]$) is beyond reach: the Gröbner computations with the saturation variables do not terminate
   in twenty minutes on an $n=7$ instance.
2. **Generic versus universal.** For a long time we conflated "the generic gcd has positive degree" with "the chart
   is uniformly bad". The correct statement is per irreducible component of the admissible family, and the feasible
   set is only constructible, not open and not closed.
3. **No machine-check for the Kronecker chain.** B.6–B.9 and B.10 need local Smith theory and polynomial-matrix
   ranks, which the library lacks; that is the content of Part II.
4. **Type III has exactly one whole-family theorem.** Everything else we know about Type III is either a
   single-point decision or an observation.

## III.3 Questions

**Q1.** Are the countings in II.4 correct as stated — in particular "constant left null vectors $=$ zero left
indices", and "$q+2p-h$ left indices" via the freeness from B.6? If a convention differs, which one?

**Q2.** In II.2, is the argument that the factor $D(\lambda)$ (determinant $\det(\lambda I-\Lambda)$, not constant)
does not alter the **infinite** elementary divisors correct as I phrase it? A citable reference would be better than
my own argument.

**Q3.** In II.6, is the uniformity identity $h=s_0+q-r$ (under $V'\cap S=0$) a known statement, and is the
hypothesis $V'\cap S=0$ equivalent to something intrinsic (for instance an intersection number on the chart)? This
hypothesis is the weakest link in our "arithmetic criterion for $q_{\min}>q_0$".

**Q4.** In II.7, is the surjectivity of $\Phi$ legitimate as used (image closed because the source is $\mathbb P^1$
and the map is a morphism where $L_0x\ne0$)? If not, is there a counterexample where the family escapes?

**Q5.** Given III.1's exponential encoding, is it your view that the subdeterminant/Bézout formulation is closed as
a route to complexity, and if so, which of the four compact representations you listed should be attempted first?

**Q6.** Type III currently means "$h<q+r_1$ and $d_{\rm fin}>0$". Is there an invariant that separates the two
cases *uniformly over a chart* — the analogue, on the spectral side, of what $\dim(\operatorname{row}L_0\cap W)$
does for the counting side? We can compute the answer instance by instance but cannot yet state it.
