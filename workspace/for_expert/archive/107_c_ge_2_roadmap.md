# Report 107: the next layer — from c = 1 to c ≥ 2, and what has to be settled first

This report has two purposes: to report the state of the layer program after the hyperplane-layer
paper, and to ask for guidance on the route into layers c ≥ 2. It also asks for a check of the c ≥ 2
material below, in particular of the two counterexamples, because they change how the layer index
should be defined.

Self-contained; the two companion papers are referred to as Paper I and Paper II.

---

## Part I. Setting

$K_0=\ker[C;CA]$, $k=\dim K_0$, $N$ a basis, $H=LN$, $H_A=LAN$ for a $q$-row design
$\mathcal L=[L_0;R]$ with row space $V$, $\omega=\rank H$, and

$$(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \rank(\lambda H-H_A)=\omega\ \ \forall\lambda .$$

The layer index of the paper is $c:=k-\omega$; the paper treats $c=1$, where $\ker H$ is a line and
the whole design family is governed by it. Its results: the kernel line is a real eigenvector of the
compression $M=\pi_{K_0}A|_{K_0}$ (restricted by the prescribed rows); the design family is a finite
union of relative Grassmann bundles over projective eigenspaces; a single gcd over a chart's function
field decides the whole chart, via a full-rank leading-coefficient lemma; and for fixed $p$ with
geometrically simple real spectrum the decision is polynomial in the bit size.

---

## Part II. What has happened since the previous report

### II.1 The c = 1 paper, and its formalization

The paper is written and compiles (IEEEtran, 14 pages). Three Lean modules accompany it and are
axiom-audited (only `propext`, `Classical.choice`, `Quot.sound`): the direction theorem in both
directions plus its invariant form, the two prescribed-row lemmas, and the numerical part of the
fibre lemma (`finrank D_v + 1 = finrank K`, i.e. $k-1$). The relative-Grassmann parameterization, the
full-rank lemma and the bit-complexity theorem are deliberately left at paper level.

### II.2 Three quantities that coincide at c = 1 but not in general

While starting c ≥ 2 we found that three quantities are conflated in the c = 1 write-up because
there $q=k$. With $\rho:=\dim\pi_{K_0}(V)$:

$$\boxed{\ \omega=\rank(LN)=\dim(LK_0)=\rho,\qquad
c_{\text{new}}:=k-\rho=\dim(K_0\cap V^\perp),\qquad
c_{\text{old}}:=q-\rho=\dim(V\cap K_0^\perp).\ }$$

Exact arithmetic on one instance ($n=8$, $k=4$, $\rho=4$; full-rank random designs):

| $q$ | $\rank H$ | $c_{\text{new}}=k-\rho$ | $\rho$ | $c_{\text{old}}=q-\rho$ | $\dim(V\cap K_0)$ |
|---|---|---|---|---|---|
| 3 | 3 | 1 | 3 | 0 | 0 |
| 4 | 4 | 0 | 4 | 0 | 0 |
| 5 | 4 | 0 | 4 | 1 | **2** |
| 6 | 4 | 0 | 4 | 2 | 2 |

So $\omega=\rho$ identically; $c_{\text{new}}$ and $c_{\text{old}}$ differ by $q-k$; and
$\dim(V\cap K_0)$ is a *third* quantity, not equal to either (the $q=5$ row shows
$\omega=4$ against $\dim(V\cap K_0)=2$).

**Consequence for the paper.** The c = 1 paper states $\omega=\dim(V\cap K_0)$ and, in the same
spirit, treats $\dim(V\cap K_0)=k-1$ as a consequence of $(5a)$. The first is corrected to
$\omega=\rank H=k-\dim(K_0\cap V^\perp)$; the second is not a consequence at all (see II.3).
I record this here because the layer index of the c ≥ 2 program has to be one of
$c_{\text{new}}$ or $c_{\text{old}}$, and the choice is not free.

### II.3 The dimension hypothesis, and why it cannot be dropped

Write $D:=\ker H=K_0\cap V^\perp$ (so $\dim D=c_{\text{new}}$). Then $(5a)$ says exactly
$AD\perp V$. The natural generalization of the c = 1 direction theorem is:

> **Claim.** If $\dim(V\cap K_0)=k-\dim D$, then $M(D)\subseteq D$.

*Proof.* For $d\in D$ the functional $\varphi_{Ad}:u\mapsto\langle u,Ad\rangle$ on $K_0$ vanishes on
$V\cap K_0$ (as $V\perp AD$); the annihilator of $V\cap K_0$ in $K_0^*$ has dimension
$k-(k-\dim D)=\dim D$, and the $\varphi_d$ with $d\in D$ are $\dim D$ independent elements of it;
hence $\varphi_{Ad}$ is a combination of them and $\pi_{K_0}(Ad)\in D$. $\square$

The hypothesis is **not** automatic. With $M=\operatorname{diag}(1,1,2,3)$,
$K_0=\operatorname{span}\{e_5,\dots,e_8\}$, and the natural construction $D\le K_0$,
$U=D+AD$, $V=U^\perp$:

| $D$ | $c_{\text{new}}$ | $\dim(V\cap K_0)$ | $k-c$ | $(5a)$ | $M(D)\subseteq D$ |
|---|---|---|---|---|---|
| $\operatorname{span}\{e_1,e_2\}$ (invariant) | 2 | 2 | 2 | yes | **yes** |
| $\operatorname{span}\{e_1,e_4\}$ (invariant) | 2 | 2 | 2 | yes | yes |
| $\operatorname{span}\{e_1{+}e_2,\,e_3{+}e_4\}$ (not invariant) | 2 | **1** | 2 | yes | **no** |

So there are designs with $c=2$, satisfying $(5a)$, whose $\ker H$ is *not* $M$-invariant: the claim
is false without the dimension hypothesis. In the c = 1 paper the hypothesis held by construction
($q=k$ and the row space contains $D_v$), which is why the issue did not surface.

### II.4 The layer program as it stands

What the project already contains for c > 1, in its own (ambient) language:

1. the decomposition $q=\rho+c$, with the $\rho$-side completely solved (an $(A,B)$-invariant
   subspace computation, polynomial);
2. a description of the design family over $\operatorname{Gr}(c,K_0)$ as the **degeneracy locus**
   $\mathcal D_s=\{D:\dim(D+AD)\le s\}$, whose lowest stratum is "$AD\subseteq D$" (an
   $A$-invariant $c$-subspace) — note this is stronger than the $M$-invariance of II.3;
3. an exact fibre over a fixed direction $D$ (an open subset of a Grassmannian);
4. a criterion for a *fixed* direction: the container is unique when a certain invariant equals
   $\rho-1$, and then the layer test is a dimension comparison (hence linear);
5. a Kronecker-type description of the constrained pair $(\iota,D)\rightrightarrows D+AD$, used as a
   candidate classification invariant (the type-control statement is a conjecture, not a theorem).

Open, per the project's own notes: components and degrees of $\mathcal D_s$, complexity, real points.
The advice recorded there was "do c = 2 first, not hardness".

---

## Part III. Questions

**Q1 (definitions).** Should the layer index for c ≥ 2 be $c_{\text{new}}=k-\rank H$ (the dimension of
$\ker H$, which is the dimension of the direction space) or $c_{\text{old}}=q-\rho$ (the ambient
"wasted rows")? They differ by $q-k$, and the two literatures in play use different ones. My
inclination is $c_{\text{new}}$, because the design family is stratified by $D=\ker H$ and its fibres;
but the decomposition $q=\rho+c$ of Paper I/II uses $c_{\text{old}}$.

**Q2 (is the direction theorem the right entry?).** Is the claim of II.3 — with the dimension
hypothesis kept as part of the layer definition — the right generalization, or would you rather drop
the hypothesis and work with the larger family of designs (where $\ker H$ need not be
$M$-invariant)? Dropping it seems to cost the whole "direction first" structure, so I am inclined to
keep it and to state the layer as "$c=\dim\ker H$ **and** $\dim(V\cap K_0)=\dim\pi_{K_0}(V)$".

**Q3 (parameter space for c = 2).** Is the base — the variety of $M$-invariant 2-subspaces of $K_0$,
stratified by $\dim(D+AD)\in\{2,3,4\}$ — the right parameter space? For $c=1$ it degenerates to the
finite union of projective eigenspaces used in the paper, which is a consistency check; for $c=2$ the
base is positive-dimensional, and I do not know its components or their degrees.

**Q4 (fibre).** Over a fixed invariant $D$, the admissible row spaces are
$\{V: V_0+D\subseteq V\subseteq(D+AD)^\perp,\ \dim V=q\}$, which is a Grassmannian; imposing the
dimension hypothesis $\dim(V\cap K_0)=\rho$ cuts out an open subset of it. Is that the correct fibre,
and is the resulting total space — a Grassmann bundle over the invariant-subspace variety — still
irreducible on each stratum?

**Q5 (known results).** For $c=2$, are the components and degrees of $\{D\in\operatorname{Gr}(2,K_0):
\dim(D+AD)\le s\}$ known (degeneracy loci, determinantal varieties)? Note that on the invariant
stratum $D+AD=D+A_{21}D$, so the stratification is driven by the nilpotent-like part $A_{21}$, not by
$M$ alone. And is anything known about the
*complexity* of deciding whether the family is nonempty — in particular, is a hardness result known
for the c ≥ 2 layer, or is the problem expected to stay polynomial?

**Q6 (check).** I would ask for a check of II.3 and II.4: in particular, (i) whether the
dimension hypothesis is the natural one, (ii) whether the proof of the claim is complete (the
annihilator argument assumes the inner product is nondegenerate on $K_0$, which holds here), and
(iii) whether "the lowest stratum is $AD\subseteq D$" is really the correct reading of the degeneracy
locus in the compressed language, since $M$-invariance is weaker.

### Reliability

| Item | Status |
|---|---|
| $\omega=\rho$ identity | proved (rank of a composition) and checked exactly |
| $c_{\text{new}}$ vs $c_{\text{old}}$ table | exact arithmetic, one instance |
| Claim of II.3 | proved, conditional on dimension hypothesis |
| Counterexample of II.3 | exact arithmetic |
| c ≥ 2 program (II.4) | inherited from the project's earlier layer work; the Kronecker-type control is a conjecture |
