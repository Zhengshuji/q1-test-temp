# Paper proofs for checking, and a request to judge the research direction

This note collects the results of the last phase with their full paper proofs, so that the ones **without**
machine verification can be checked directly, and then states the judgments we are acting on so that you can tell us
whether they are right and whether the overall direction is sound.

Verification levels: **L1** = paper proof (written out below); **L2** = exact rational/polynomial arithmetic on
instances; **L3** = machine-checked (Lean 4 + Mathlib, 0 errors, 0 warnings, declaration names given).

What is **L3**: the vacuity of Type II, the geometric form of Type I, the dimension formula for $h$, the row-space
form of $(5a)$, and two abstract kernels added last — an *avoidance lemma* ("if $V\cap K=0$, $Z\le K$ is nonzero and
$\varphi:V\to K$ is onto, then some $x\in V$ maps into $Z$ but is not in $Z$") and *rank additivity of a direct sum*
("$\dim\operatorname{range}(f\oplus g)=\dim\operatorname{range}f+\dim\operatorname{range}g$").

What is **L1 only** (and therefore needs your eye): items 1–6 below.

---

# Part I. Setting

$A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$,
$\operatorname{rank}[C;L_0]=p+r$; $L_0$ and $(C,A)$ observable. $\mathcal L\in\mathbb C^{q\times n}$ with
$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$ and $\operatorname{rank}[C;\mathcal L]=p+q$;
$h=\operatorname{rank}[\mathcal L;CA;C]$; conditions $(5a)$, $(5b)$ as usual.
$V=\ker[C;CA]$, $K=\ker[C;L_0]$, $R=\operatorname{row}\mathcal L$, $\mathcal Z=\ker[C;\mathcal L]$,
$W=\operatorname{row}[C;CA]$ ($r_1=\dim W$), $S=\operatorname{row}[C;L_0]+W$ ($s_0=\dim S$), $d=n-p-q$.
Type I $:=$ $h\ge q+r_1$; Type III $:=$ $h<q+r_1$ with a finite elementary divisor of positive degree.

---

# Part II. Statements and proofs

## 1. Counting identity (L1; L2 35/35, 54/54)

**Claim.** $h=s_0+q-\dim(R\cap S)$, hence $h\le s_0+q-r$; and
$$\text{Type I}\iff R\cap W=0\iff\bigl(s_0=r_1+r\ \text{and}\ R\cap S=\operatorname{row}L_0\bigr).$$
If $s_0<r_1+r$, no admissible order of the instance is Type I.

*Proof.* $\mathcal Z^\perp=C\oplus R$ since $\operatorname{rank}[C;\mathcal L]=p+q$. As
$\operatorname{row}L_0\subseteq R\subseteq\mathcal Z^\perp$ we get $\mathcal Z^\perp+S=\mathcal Z^\perp+W$, so
$$h=\dim(\mathcal Z^\perp+W)=\dim(\mathcal Z^\perp+S)=(p+q)+s_0-\dim(\mathcal Z^\perp\cap S).$$
Because $C\subseteq S$ and $C\cap R=0$, $(C\oplus R)\cap S=C\oplus(R\cap S)$: one inclusion is clear, and for
$c+u\in S$ with $c\in C$, $u\in R$ we get $u=(c+u)-c\in S$, hence $u\in R\cap S$. Therefore
$\dim(\mathcal Z^\perp\cap S)=p+\dim(R\cap S)$ and $h=q+s_0-\dim(R\cap S)$. Since
$\operatorname{row}L_0\subseteq R\cap S$ we have $\dim(R\cap S)\ge r$, hence $h\le s_0+q-r$.

For Type I: $h\ge q+r_1\iff\dim(R\cap S)\le s_0-r_1$. Now
$s_0=\dim(\operatorname{row}[C;L_0]+W)=(p+r)+r_1-\dim(\operatorname{row}[C;L_0]\cap W)$ and
$\operatorname{row}C\subseteq\operatorname{row}[C;L_0]\cap W$, so $s_0\le r_1+r$; combined with
$\dim(R\cap S)\ge r$ this forces $\dim(R\cap S)=r$ and $s_0=r_1+r$, i.e. $R\cap S=\operatorname{row}L_0$. Since
$C\subseteq W$ and $C\cap R=0$, $R\cap W=0$ is equivalent to the same statement. $\square$

## 2. Observability reduction (L1; L2 44/44 against the Toeplitz criterion)

**Claim.** Under $(5a)$, choose $\Lambda,G_0,G_1$ with $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$, let
$U=\mathcal LV\subseteq\mathbb C^q$ and let $E$ satisfy $\ker E=U$. Then
$$(5b)\iff U\ \text{contains no nonzero eigenvector of}\ \Lambda\iff(E,\Lambda)\ \text{observable}
\iff\operatorname{rank}[E;E\Lambda;\dots;E\Lambda^{q-1}]=q .$$

*Proof.* (i) $Q_{\mathcal L}(\lambda)=D(\lambda)H$ where $H=[\mathcal L;CA;C]$ and
$D(\lambda)=\begin{pmatrix}\lambda I-\Lambda&-G_1&-G_0\\0&I&0\\0&0&I\end{pmatrix}$, because the first block row is
$(\lambda I-\Lambda)\mathcal L-G_1CA-G_0C=\lambda\mathcal L-\mathcal LA$.
(ii) For any two maps, $\operatorname{rank}(DH)=\dim\operatorname{im}H-\dim(\ker D\cap\operatorname{im}H)$, so
$\operatorname{rank}(DH)=h=\operatorname{rank}H\iff\ker D\cap\operatorname{im}H=0$.
(iii) $\ker D(\lambda)=\{(u,0,0):(\lambda I-\Lambda)u=0\}$ and
$\operatorname{im}H=\{(\mathcal Lx,CAx,Cx)\}$.
(iv) Hence a rank drop at $\lambda$ occurs iff there is $x\in V$ with $\mathcal Lx\ne0$ and
$\Lambda\mathcal Lx=\lambda\mathcal Lx$.
(v) Therefore $(5b)$ holds iff $U$ contains no eigenvector of $\Lambda$; by PBH the latter is equivalent to
observability of $(E,\Lambda)$, whose rank form is the displayed matrix. $\square$

*Remark.* The factorization is not canonical, but step (iv) holds for any admissible one, so the truth value does
not depend on the choice.

## 3. Exact failure criterion (L1; L2 — six explicit $(x,\lambda_0)$ certificates, with irrational or complex
$\lambda_0$)

**Claim.** Under $(5a)$, $(5b)$ fails at $\mathcal Z$ iff there are $x\in V\setminus\mathcal Z$ and $\lambda$ with
$(\lambda I-A)x\in\mathcal Z$.

*Proof.* For $x\in V$ we have $Cx=CAx=0$, hence $\mathcal L(\lambda x-Ax)=(\lambda I-\Lambda)\mathcal Lx$. Also
$x\in V\setminus\mathcal Z\iff\mathcal Lx\ne0$: if $\mathcal Lx=0$ and $Cx=0$ then $x\in\ker[C;\mathcal L]=\mathcal Z$.
Finally $C(\lambda x-Ax)=0$, so $(\lambda I-A)x\in\mathcal Z\iff\mathcal L(\lambda x-Ax)=0$. Combining, the two
sides are both equivalent to "$\ker(\lambda I-\Lambda)$ meets $\operatorname{im}\mathcal L$ in a nonzero vector",
which by item 2 is exactly failure of $(5b)$. $\square$

This is a restatement of the cited nullspace-pencil criterion; what is new in our use is only that the condition
$x\notin\mathcal Z$ is made explicit, and that it bridges to the observability form.

## 4. Proportionality invariant $\varepsilon=0$ (L1; L2 5983/5983 over all three cases)

**Claim.** Let $U_0=L_0|_V$, $U_1=L_0A|_V:V\to\mathbb C^r$, $P=\{x\in V:U_0x\wedge U_1x=0\}$ and
$\varepsilon=\dim V-\dim P$. Since $V$ is irreducible and $P$ algebraic, $\varepsilon=0\iff P=V$; and
$$\varepsilon=0\iff\begin{cases}\operatorname{rank}U_0=0:&\text{automatic};\\
\operatorname{rank}U_0=1:&\operatorname{im}U_1\subseteq\operatorname{im}U_0;\\
\operatorname{rank}U_0\ge2:&U_1=\alpha U_0\ \text{for some}\ \alpha .\end{cases}$$

*Proof.* (rank one) Whenever $U_0x\ne0$, dependence forces $U_1x\in\operatorname{im}U_0$. For $k\in\ker U_0$ and
$x_0$ with $U_0x_0\ne0$, both $U_1x_0$ and $U_1(x_0+k)$ lie in $\operatorname{im}U_0$, so $U_1k$ does. The converse
is immediate.
(rank $\ge2$) Write $U_1x=\alpha_xU_0x$ whenever $U_0x\ne0$. If $U_0x,U_0y$ are independent then applying
dependence to $x+y$ gives $\alpha_x=\alpha_y$, and a third vector with independent image handles the case of two
proportional nonzero images; hence all $\alpha_x$ agree. If $k\in\ker U_0$, comparison with two vectors whose
images are independent gives $U_1k=0$. The converse is immediate. $\square$

## 5. Single-$\lambda$ certificate and the design constraint (L1; L2 — the certificate holds exactly at the one
infeasible parameter value of a one-parameter family, and for $k=1,2,3$ copies)

**Claim.** If $\dim V=\dim K$ and there is $\lambda_0$ with $(\lambda_0I-A)V=K$, then every $\mathcal Z\subseteq K$
of dimension $d\ge1$ fails at $\lambda_0$, **except** those with $(\lambda_0I-A)^{-1}\mathcal Z\subseteq\mathcal Z$.
The exception is absent whenever $V\cap K=0$, and
$$\dim(V\cap K)=\dim\ker[C;CA;L_0]\ \ge\ n-(2p+r),$$
so the exception-free case requires $2p+r\ge n$.

*Proof.* $(\lambda_0I-A)|_V:V\to K$ is an isomorphism since the spaces have equal dimension and the image is $K$.
Given $Z\ni z\ne0$, let $x=(\lambda_0I-A)^{-1}z$; then $(\lambda_0I-A)x\in\mathcal Z$. If $x\notin\mathcal Z$ we are
done by item 3; if $x\in\mathcal Z$ for every choice of $z$ then
$(\lambda_0I-A)^{-1}\mathcal Z\subseteq\mathcal Z$. The exception is impossible when $x\in V$ and
$\mathcal Z\subseteq K$ are disjoint, i.e. when $V\cap K=0$. The dimension formula is immediate from
$V\cap K=\ker[C;CA;L_0]$. $\square$

## 6. A tractable class (L1; L2 — 56 of 595 random observable instances, all 56 with an explicit feasible witness)

**Claim.** Let $B_V$ span $V$ and let $P_K$ have full row rank with $\ker P_K=K$. If
$$\operatorname{rank}\bigl(P_K(\lambda I-A)B_V\bigr)=\dim V\qquad\forall\lambda, \tag{T*}$$
then the instance is spectrally feasible at **every** order.

*Proof.* Suppose $(5b)$ failed at some $\mathcal Z\subseteq K$. By item 3 there are $x\in V$ and $\lambda$ with
$(\lambda I-A)x\in\mathcal Z\subseteq K$, hence $P_K(\lambda I-A)x=0$; by (T*) this forces $x=0$, contradicting
$x\in V\setminus\mathcal Z$. $\square$

(T*) is checkable by taking the gcd of the maximal minors of the pencil $P_K(\lambda I-A)B_V$ and testing whether it
is a nonzero constant. It is stronger than necessary, and it is disjoint from the certificate of item 5: (T*) implies
$(\lambda I-A)V\cap K=0$ for all $\lambda$, so the single-$\lambda$ certificate cannot hold simultaneously.

## 7. Unbounded order gap (L1; the two abstract steps are L3; L2 for $k=1,2,3$)

**Claim.** Let a single copy satisfy $V_1\cap K_1=0$ and $(\lambda_0I-A_1)V_1=K_1$ with $\dim V_1=\dim K_1$, and let
it have a feasible augmentation $\mathcal L_1$ of order $q_1$ with $d_1=n_1-p_1-q_1=0$. Then for the $k$-fold direct
sum $(A,C,L_0)=(A_1,C_1,L_{0,1})^{\oplus k}$:
$$q_{\min}=k\,q_{\min}(\text{copy}),\qquad\text{so the gap scales by }k.$$

*Proof.* For a direct sum, $V=V_1^{\oplus k}$, $K=K_1^{\oplus k}$, $V\cap K=0$, and
$(\lambda_0I-A)V=K$ **with the same $\lambda_0$** since the blocks are identical. By item 5 every order with
$d=n-p-q\ge1$ is infeasible for the whole family. At $d=0$, i.e. $q=kq_1$, the block-diagonal augmentation
$\mathcal L=\mathcal L_1^{\oplus k}$ satisfies $(5a)$ and $(5b)$ because $Q_{\mathcal L}$ and
$[\mathcal L;CA;C]$ are block diagonal and ranks add — this is the abstract step verified in Lean
(`finrank_range_prodMap`), and the avoidance step is Lean-verified as well (`exists_witness_not_mem`); what remains
paper is only the matrix bookkeeping that "block diagonal $\Rightarrow$ ranks add". $\square$

Consequently $k$ copies of the gap-2 example give gap $2k$: the difference between $q_{\min}$ and the algebraic
minimum order can grow linearly with the instance.

## 8. What is conditional, and one retraction

The covering criterion (if the image of the bad-line map has dimension at least $q-r$ then the order is infeasible
for the whole family) is **conditional**: the image is only constructible, so projective dimension theory does not
apply as stated, and the two excluded loci cannot be discarded from the dimension count. It is not used in any
statement above. Separately, the guess "Type III implies $\varepsilon=0$" is **false** — our own $n=7$ and $n=8$
instances have isolated Type III candidates with $\varepsilon\ge1$; it is withdrawn.

---

# Part III. The judgments we are acting on — please check them

**J1 (where the hardness can live).** The counting side is arithmetic and decidable by rank computations; the
per-candidate spectral condition is a $(5b)$-test that is polynomial in the candidate. Therefore any hardness must
come from the *existence* question over the Grassmannian, and — since the unconstrained version of the resulting
"regular subpencil" problem is classical and polynomial — hardness, if it exists, must come from the two
constraints that $V=\ker[C;CA]$ and $K=\ker[C;L_0]$ impose.

**J2 (the object to study).** The clean form of the existence question is: does there exist $\mathcal Z\le K$ of
dimension $d$ such that the compression $\Pi_{\mathcal Z}(\lambda I-A)B_V$ has full column rank over $\mathbb C[\lambda]$
(equivalently: no finite zero)? We call this AVOID. It has three equivalent forms (the failure criterion of item 3,
the observability form of item 2, and a gcd condition).

**J3 (the feasible side is the hard side).** Whole-family infeasibility is thin in the data: along a one-parameter
deformation of our gap-2 example only one value is infeasible. So a reduction cannot leave a parameter free; it has
to *encode* the thin condition. Conversely, a hardness proof for the feasible side would have to encode a hard
algebraic feasibility problem into "AVOID holds".

**J4 (the structural picture is stable).** The distinction counting/spectral is exact (item 1 versus items 2–3);
Type II is empty; the gap is unbounded (item 7); and the tractable class (T*) is genuinely complementary to the
certificate (item 5). We believe these four facts are the reliable part of the picture and that the complexity
question is separate from them.

**J5 (method).** We do not see how to settle the complexity without a gadget, and we do not have one. The next
concrete experiment we plan is a control experiment for J1: replace $V$ and $K$ by *random* subspaces of the same
dimensions (so that they no longer come from $A$, $C$, $L_0$) and measure how the feasibility rate changes. If the
unconstrained problem is generically feasible while the constrained one is not, that supports J1 and tells us where
the gadget has to bite.

## Questions

**Q1.** Are J1–J4 right? In particular, do you agree that hardness must come from the constraints on $V$ and $K$,
rather than from the pencil structure itself?

**Q2.** Is the control experiment of J5 worth running, or would you replace it by something sharper?

**Q3.** Among items 1–7, is any proof wrong or under-stated? We are most doubtful about item 7, where the matrix
bookkeeping (block diagonal implies ranks add) is the only unverified part, and about item 6, whose condition (T*)
is strong enough that we do not know whether the covered 9.4% of instances is representative.

**Q4.** Given J3, would you advise attacking the *infeasibility* side (which is where our two examples live and
where the thin algebraic conditions sit) rather than the feasibility side? The two directions are equivalent as
decision problems only if one can decide both, but they suggest different reductions.

**Q5.** Is the overall strategy — structural characterisation first, complexity second — the right one, or would you
push us to fix a target problem class now (for instance, the constrained subpencil problem with $(p,r)$ fixed and
$n$ growing, as you suggested) and try to show hardness only there?
