# Every proposition not fully machine-checked, with its proof, for checking

We now have a machine-checked layer (Lean 4 + Mathlib, seven files, all compiled with zero errors and zero
warnings) and a paper layer. This note lists **every proposition that is not fully machine-checked**, with its
proof, and states exactly what the machine layer does and does not cover. The request at the end is to check the
paper layer with the same severity you have applied so far.

---

# Part I. Standard and inventory

## 1. Verification levels

* **L3** — machine-checked: `lake env lean` exits 0 with no errors or warnings. A theorem in Lean's logic.
* **L1** — paper proof: a complete argument, checkable by a reader, but not machine-checked.
* **L2** — exact verification: finitely many instances, exact rational/polynomial arithmetic, no floating point.
  **Falsifies, does not confirm.**

## 2. What the machine layer covers (all exit 0, no warnings)

| file | declarations | propositions covered |
|---|---|---|
| `RowSpace.lean` | row-space/rank bridge | the (5a) row-space translation used everywhere |
| `TypeII.lean` | Type II vacuity | B.9b |
| `TypeIGeom.lean` | Type I geometric form | B.11, B.11b |
| `A0Row.lean` | (5a) row form | A.0 (first step) |
| `LemmaA.lean` | avoidance lemma | B.15 step |
| `LemmaB.lean` | rank additivity of direct sums | B.15 step |
| `PsiImage.lean` | degree of the recursion; $P_w$ has positive degree; a positive-degree $\mathbb C$-polynomial has a root | B.18d/B.18e kernel |
| `Criterion.lean` | $(5a)\Rightarrow A(V\cap\mathcal Z)\subseteq\mathcal Z$; permanent kernel; kernel form of the quotient criterion; the factorisation $F\circ(cI-A)=(cI-\Lambda)\circ F$ | B.16b, B.17, B.13c |
| `Dims.lean` | modular identity; dimension additivity; $Cx=0,CAx=0\Rightarrow C((cI-\Lambda)x)$-type annihilation | B.11c, B.18c |
| `Logic.lean` | arithmetic core of "counting kills (5b)"; the CSS reduction; the three-case family argument | B.11d, B.18e |

**The honest caveat.** In `Criterion.lean`, `Dims.lean` and `Logic.lean` the *mathematical content* enters as a
**hypothesis** and the machine checks the *inference*. For example `Logic.b11d_css` assumes "counting kills (5b)"
and "CSS holds" and concludes the equivalence; it does not prove the rank inequality that justifies the first
assumption. So for those items the status is "the logic is machine-checked, the mathematics is paper". This is
marked as **[Lean kernel]** rather than **[Lean]** in our tables.

---

# Part II. The paper layer

## A. The Kronecker/Smith chain (the algebraic backbone)

**B.8 (discrete equivalence).** With $h=\operatorname{rank}[\mathcal L;CA;C]$ and $\mathcal L$ admissible,
$$(5b)\iff d_{\rm fin}=0\iff\textstyle\sum_j\varepsilon_j=\operatorname{rank}\mathcal L,$$
where $\varepsilon_j$ are the *left* minimal indices of $Q_{\mathcal L}(\lambda)$ and $d_{\rm fin}$ the total degree
of the finite elementary divisors.

*Proof.* (5b) is the statement that the rank of the pencil is constant in $\lambda$; by the Smith form that holds
iff there are no finite invariant factors, i.e. $d_{\rm fin}=0$. The second equivalence is the Kronecker index
relation $h=\sum_j\varepsilon_j+d_{\rm fin}$ (total degree of the minors equals the sum of the degrees of the left
minimal indices plus the finite part), combined with $d_{\rm fin}=0$. $\square$

**B.9 (structural trichotomy).** $k=q+r_1-h$ is the number of nonzero left minimal indices; $d_{\rm fin}$ is the
finite part; and $d_{\rm fin}=0$ with $k=0$ is impossible when $\mathcal L$ has dependent rows. *Proof.* The left
minimal indices are the degrees of the polynomial relations among the rows of $Q_{\mathcal L}$; a relation of degree
zero is a linear dependence among the rows, which is excluded by $\operatorname{rank}\mathcal L=q$ plus the rank
identity. $\square$

**B.9b (Type II is empty).** Under the hypotheses of B.9, $k\le s=\operatorname{rank}\mathcal L$ always; hence the
case $k>s$ never occurs. *Proof.* $[\mathcal L;CA;C]$ is a row-stack over $[CA;C]$, so
$h\ge r_1$
and $k=q+r_1-h\le q=\operatorname{rank}\mathcal L$. $\square$  **(machine-checked)**

**B.10 (dichotomy).** Failure of (5b) happens exactly in the two cases $h\ge q+r_1$ (counting) and
$h<q+r_1$ with $d_{\rm fin}>0$ (spectral). *Proof.* By B.8, failure means $d_{\rm fin}>0$ or a nonzero left index;
B.9b removes the "index too large" case. $\square$

*Why not machine-checked:* the Kronecker/Smith theory of matrix pencils (minimal indices, finite/infinite
elementary divisors) is not in Mathlib at all; building it is a substantial library project. Statements are
elementary in Smith-form language and we regard them as the safest part of the paper layer, but they are not
machine-checked.

## B. The spectral side

**B.12 (observability reduction).** Under (5a), choose $\Lambda,G_0,G_1$ with
$\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$; let $U=\mathcal LV\subseteq\mathbb C^q$ and let $E$ satisfy
$\ker E=U$. Then
$$(5b)\iff U\ \text{contains no nonzero eigenvector of}\ \Lambda\iff(E,\Lambda)\ \text{observable}
\iff\operatorname{rank}[E;E\Lambda;\dots;E\Lambda^{q-1}]=q .$$

*Proof.* (i) $Q_{\mathcal L}(\lambda)=D(\lambda)[\mathcal L;CA;C]$ with
$D(\lambda)=\begin{pmatrix}\lambda I-\Lambda&-G_1&-G_0\\0&I&0\\0&0&I\end{pmatrix}$, since the first block row is
$(\lambda I-\Lambda)\mathcal L-G_1CA-G_0C=\lambda\mathcal L-\mathcal LA$.
(ii) For composable maps, $\operatorname{rank}(DH)=\dim\operatorname{im}H-\dim(\ker D\cap\operatorname{im}H)$, so
$\operatorname{rank}(DH)=h=\operatorname{rank}H$ iff $\ker D\cap\operatorname{im}H=0$.
(iii) $\ker D(\lambda)=\{(u,0,0):(\lambda I-\Lambda)u=0\}$ and $\operatorname{im}[\mathcal L;CA;C]=\{(\mathcal Lx,CAx,Cx)\}$.
(iv) So a rank drop at $\lambda$ occurs exactly when some $x\in V$ has $\mathcal Lx\ne0$ and
$\Lambda\mathcal Lx=\lambda\mathcal Lx$.
(v) Hence (5b) iff $U$ contains no eigenvector of $\Lambda$, which by the PBH test is observability of $(E,\Lambda)$,
whose rank form is displayed. $\square$

*Not machine-checked:* needs the polynomial-matrix factorisation $D(\lambda)H$ and PBH. Step (ii) is elementary
linear algebra and could be machine-checked; steps (i) and (v) need the missing pencil/PBH layers.

**B.13c (exact failure criterion).** Under (5a),
$$(5b)\ \text{fails at}\ \mathcal Z\iff\exists x\in V\setminus\mathcal Z\ \text{and}\ \lambda:\ (\lambda I-A)x\in\mathcal Z.$$
*Proof.* $\mathcal L(\lambda x-Ax)=\lambda\mathcal Lx-\mathcal LAx=(\lambda I-\Lambda)\mathcal Lx$ for $x\in V$;
$x\in V\setminus\mathcal Z\iff\mathcal Lx\ne0$; and $C(\lambda x-Ax)=0$, so $(\lambda I-A)x\in\mathcal Z\iff\mathcal L(\lambda x-Ax)=0$.
The right-hand side is thus "$\ker(\lambda I-\Lambda)$ meets $\operatorname{im}\mathcal L$ nontrivially", which by
B.12 is failure. $\square$  **(kernel machine-checked: the factorisation identity)**

**B.13d ($\varepsilon=0$).** With $U_0=L_0|_V$, $U_1=L_0A|_V$, $P=\{x:U_0x\wedge U_1x=0\}$,
$\varepsilon=\dim V-\dim P$: since $V$ is irreducible and $P$ algebraic, $\varepsilon=0\iff P=V$, and
$$\varepsilon=0\iff\begin{cases}\operatorname{rank}U_0=0:&\text{automatic},\\
\operatorname{rank}U_0=1:\ \operatorname{im}U_1\subseteq\operatorname{im}U_0,\\
\operatorname{rank}U_0\ge2:\ U_1=\alpha U_0 .\end{cases}$$
*Proof.* Rank one: where $U_0x\ne0$, dependence forces $U_1x\in\operatorname{im}U_0$; taking $x_0$ with
$U_0x_0\ne0$ and $k\in\ker U_0$, both $U_1x_0$ and $U_1(x_0+k)$ lie in $\operatorname{im}U_0$, hence so does
$U_1k$. Rank $\ge2$: writing $U_1x=\alpha_xU_0x$ when $U_0x\ne0$, two vectors with independent images give
$\alpha_x=\alpha_y$, and a third handles the proportional case; for $k\in\ker U_0$ compare with two independent
images. $\square$

*Not machine-checked:* would need the $2\times r$ rank-one determinantal variety over an irreducible $V$; the
elementwise argument above is what an expert should check, in particular the "$k\in\ker U_0$" case at rank one and
the "two proportional images" case at rank $\ge2$.

**B.13e (single-$\lambda$ certificate).** If $\dim V=\dim K$ and $(\lambda_0I-A)V=K$ for some $\lambda_0$, then every
$\mathcal Z\le K$ of dimension $d\ge1$ fails at $\lambda_0$, except those with
$(\lambda_0I-A)^{-1}\mathcal Z\subseteq\mathcal Z$. The exception is impossible when $V\cap K=0$, and
$\dim(V\cap K)=\dim\ker[C;CA;L_0]\ge n-(2p+r)$, so the exception-free case needs $2p+r\ge n$.

*Proof.* $(\lambda_0I-A)|_V:V\to K$ is an isomorphism (equal dimensions, image $K$). For $0\ne z\in\mathcal Z$ set
$x=(\lambda_0I-A)^{-1}z$: then $(\lambda_0I-A)x\in\mathcal Z$, and $x\notin\mathcal Z$ unless the preimage of every
$z$ lies in $\mathcal Z$. $\square$

**B.13f (scalar case is degenerate).** At $\dim V=\dim K=1$ (which forces $n=p+r+1=3$), the failure condition
degenerates: with $V=\langle v\rangle$, $K=\langle k\rangle$ the criterion reduces to $V\ne K$; in particular the
pencil determinant vanishes identically.

**B.14 (tractable class).** Let $B_V$ span $V$ and $P_K$ have full row rank with $\ker P_K=K$. If
$$\operatorname{rank}\bigl(P_K(\lambda I-A)B_V\bigr)=\dim V\qquad\forall\lambda, \tag{T*}$$
then the instance is spectrally feasible at every order. *Proof.* If (5b) failed, B.13c gives $x\in V$, $\lambda$ with
$(\lambda I-A)x\in K$, hence $P_K(\lambda I-A)x=0$, so (T*) forces $x=0$, contradicting $x\notin\mathcal Z$. $\square$
**Note (your caveat, now with an instance).** The *negation* of (T*) is not failure: we exhibit an admissible
$\mathcal Z$ with $\operatorname{rank}N_{\mathcal Z}(\lambda)\equiv1<2=\dim V$ for all $\lambda$ yet (5b) holds.

## C. The counting side and the stratified criterion

**B.11c (counting identity).** $h=s_0+q-\dim(R\cap S)$, hence $h\le s_0+q-r$; Type I $\iff R\cap W=0\iff$
($s_0=r_1+r$ and $R\cap S=\operatorname{row}L_0$); and if $s_0<r_1+r$ no order is Type I. *Proof.*
$\mathcal Z^\perp=C\oplus R$, so $\mathcal Z^\perp+S=\mathcal Z^\perp+W$ and
$h=\dim(\mathcal Z^\perp+W)=\dim\mathcal Z^\perp+s_0-\dim(\mathcal Z^\perp\cap S)$; and
$\mathcal Z^\perp\cap S=C\oplus(R\cap S)$ because $C\le S$ and $C\cap R=0$. Hence
$\dim(\mathcal Z^\perp\cap S)=p+\dim(R\cap S)$. The Type I criterion follows from $\dim(R\cap S)\ge r$ and
$s_0\le r_1+r$. $\square$  **(dimension steps machine-checked: modular identity + additivity)**

**B.11d (CSS reduction).** Call an instance counting-spectrally separated (CSS) if for every admissible order $q$,
every augmentation satisfying (5a) with $h<q+r_1$ also satisfies (5b). Then
$$\exists\mathcal L:(5a)\wedge(5b)\iff\exists\mathcal L:(5a)\wedge h<q+r_1 .$$
*Proof.* If $h\ge q+r_1$ then $\operatorname{rank}Q_{\mathcal L}(\lambda)\le q+r_1\le h$ with equality needed for
(5b); for $h>q+r_1$ this is impossible, so a (5a)$\,\wedge\,$(5b) witness must have $h<q+r_1$; conversely CSS turns a
counting witness into a good one. $\square$  **(logic machine-checked; the rank inequality is the paper part —
and note the boundary case $h=q+r_1$ needs care: there the counting bound is attained, so the argument uses
strictness. We flag this as the weakest step of B.11d and would like your reading.)**

## D. Class I ($p=r=1$)

**B.18.** With $(c,A)$ observable: $r_1=\operatorname{rank}[c;cA]=2$, $\dim V=\dim K=n-2$,
$\dim(V\cap K)=\dim\ker\{c,cA,\ell\}\ge n-3$; $s_0\in\{2,3\}$ and $s_0=3\iff\ell\notin\operatorname{span}\{c,cA\}$;
hence $\ell\in\operatorname{span}\{c,cA\}$ forbids Type I at every order. For $\mathcal Z\subseteq V\cap K$,
$\rho=\dim(V/S)=q-1$, so the quotient pencil is $(q+1)\times(q-1)$.

**B.18b (terminal order).** At $q=n-1$ (so $d=0$, $\mathcal Z=0$), any $\mathcal L$ with
$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$ and $[c;\mathcal L]$ invertible satisfies both
conditions: (5b) because a failure would need an eigenvector of $A$ inside $V\subseteq\ker c$, which observability
forbids; (5a) because $\operatorname{rank}[\mathcal L;CA;C]=n$.

**B.18c.** $c(\lambda I-A)x=\lambda cx-cAx=0$ for $x\in V$, so $\operatorname{im}\psi\subseteq\ker c$ where
$\psi(x,\lambda)=(\lambda I-A)x$; and at $d=1$ with $\mathcal Z=\langle z\rangle$, $z\notin V$, failure $\iff z\in\operatorname{im}\psi$.
Hence at $d=1$ the order fails for the whole family iff every admissible line lies in the bad image.
**(annihilation machine-checked)**

**B.18d (canonical coordinates).** In the cyclic basis $c=e_1^{\mathsf T},cA=e_2^{\mathsf T},\dots$ (so $A$ is
companion), $V=\langle e_3,\dots,e_n\rangle$ and
$$(\lambda I-A)x=\Bigl(0,\ -x_3,\ \lambda x_3-x_4,\ \dots,\ \lambda x_{n-1}-x_n,\ \lambda x_n+\textstyle\sum_{k\ge3}a_{k-1}x_k\Bigr).$$
For $w\in\ker c$, with $x_3=-w_2$, $x_{k+1}=\lambda x_k-w_k$ and
$P_w=\lambda x_n+\sum_{k\ge3}a_{k-1}x_k-w_n$:
$$w\in\operatorname{im}\psi\iff P_w\ \text{is not a nonzero constant}.$$
*Proof.* The first $n-1$ coordinates give the recursion, the last gives $P_w(\lambda)=0$; a polynomial over
$\mathbb C$ has a root unless it is a nonzero constant. $\square$

**B.18e ($d=1$ fails for the whole family).** Three parts: (i) $z\in V$ admits no admissible $\mathcal L$, since
$\mathcal Z\subseteq V$ forces $A(\mathcal Z)\subseteq\mathcal Z$ (B.16b), making $z$ an eigenvector inside
$\ker c$; (ii) $z\notin V$ is automatically admissible, since $\operatorname{rank}[\mathcal L;CA;C]=n-1$ would
force $cA\in\operatorname{row}[C;\mathcal L]$, hence $cAz=0$, contradicting $cAz=z_2\ne0$; (iii) $z\notin V$ gives
$\deg P_z=n-2\ge1$ by the recursion ($x_k$ has degree exactly $k-3$ with leading coefficient $-z_2$), hence
$z\in\operatorname{im}\psi$. **(iii) has a machine-checked kernel; (i) and (ii) are paper, and (ii) is the step we
would most like checked — it uses the canonical coordinates in an essential way.**

## E. Older counting-side results, unchanged

| item | statement | proof in one line | why not Lean |
|---|---|---|---|
| A.4 | the layer formula $q=\rho+c$ | dimension bookkeeping on $\mathcal V\cap\mathcal J$ | needs the layer structure of the problem |
| D.3 | $\rho_{ci}$ computable in $O(n^4)$ | iterate $O(n)$ steps of $O(n^3)$ | algorithmic complexity, partly machine-checked (D.4) |
| E.1 | $\rho_{ci}=P(T,B,U_0)$ | $T(U)\subseteq U+B$, $U\supseteq U_0$, minimise $\dim U$ | reduction is paper; the recursion is machine-checked |
| E.2 | $\rho_{ci}$ in $O(n^4)$ | from D.3 | as D.3 |
| F.2 | $\min_\lambda r(\lambda)<\rho_{ci}$ ⟹ no solution | E.1 gives $\rho\ge\rho_{ci}$, F.1 gives $\rho\le\min_\lambda r$ | depends on E.1, F.1 |
| B.13b | $\varepsilon$ is the codimension of the proportionality locus | $P$ is the preimage of $\{\operatorname{rank}\le1\}$ under a linear map | needs constructible-set dimension theory |
| K.1 | every nonzero bivector in $\Lambda^2\mathbb C^3$ is decomposable | $\mathrm{Gr}(2,3)=\mathbb P(\Lambda^2\mathbb C^3)$ | algebraic geometry |
| K.3 | $\ell\ge N-(2m-4)$ ⟹ a decomposable element exists | projective dimension count | only gives complex intersections |
| K.4 | decision algorithm for $m\ge5$, $\ell\le3$ | gcd of quadratics / ideal membership + rational points | exact verification 65/43/0, no Lean |

---

# Part III. What we would like checked

**Q1 (the two weakest steps).** (a) In B.11d, the boundary case $h=q+r_1$: our argument uses strictness
($h>q+r_1$ kills (5b)), and we are not certain the statement as written survives at equality. (b) In B.18e(ii), the
inference "$cA\in\operatorname{row}[C;\mathcal L]\Rightarrow cAz=0$ for $z\in\ker[C;\mathcal L]$" — is the use of
canonical coordinates legitimate, or does it hide an assumption on $\ell$?

**Q2 (B.13d's elementwise argument).** We are least sure of the two degenerate cases: rank one with
$k\in\ker U_0$, and rank $\ge2$ with two proportional images. Is the "third vector" device sound?

**Q3 (the Kronecker chain).** B.8/B.9/B.10 rest on the index relation $h=\sum_j\varepsilon_j+d_{\rm fin}$. We would
like a reference or a counterexample: is that relation exactly as stated for *polynomial* pencils that are not
regular, and does it depend on the pencil being square?

**Q4 (what to machine-check next).** Given the library gaps, which of the following would you prioritise:
the polynomial-matrix/Smith layer (to cover B.8–B.10), the PBH/eigen-decomposition layer (to cover B.12),
or the matrix-rank layer (to move the "logic with hypotheses" items into fully machine-checked ones)?

**Q5 (acceptability).** Is it acceptable to you that some Lean declarations have the mathematical content as a
*hypothesis* and check only the inference, provided this is marked as **[Lean kernel]** rather than **[Lean]**?
We adopted this to make the reduction steps auditable, but it is a weaker claim than "proved in Lean".
