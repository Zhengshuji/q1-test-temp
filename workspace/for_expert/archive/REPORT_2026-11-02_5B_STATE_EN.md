# The state of $(5b)$ — inventory and gaps

**Date:** 2026-11-02 (evening, after the fourth review)
**Purpose:** a complete inventory of what the project has established about the spectral condition $(5b)$,
and an honest list of the remaining gaps. Written after a self-audit in which we found that several
recent "discoveries" were re-derivations of material from 2026-10-21 (see §7).

**Notation.** $(5a)$: $\operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C]$.
$(5b)$: $\operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=\operatorname{rank}[\mathcal L;CA;C]$ for all $\lambda$.
$Q_{\mathcal V}(\lambda)=\lambda\pi(\mathcal L)-\pi(\mathcal LA)$ is the quotient pencil (B.1);
$P(\lambda)=[(\lambda I-A)V\mid Z]$ is the chart pencil of P2;
$h=\operatorname{rank}H$ with $H=[\mathcal L;CA;C]$.

---

## 1. Equivalences: $(5b)$ as a finite computable object

| form | statement | grade | where |
|---|---|---|---|
| quotient pencil | $(5b)\iff\operatorname{rank}Q_{\mathcal V}(\lambda)=\dim\pi(\mathcal V)\ \forall\lambda$ | proved + Lean | `proof/pencil_equivalence` (B.1) |
| factorization | $P(\lambda)=(\lambda I-\Lambda)H$; hence $\operatorname{rank}P\le\operatorname{rank}H$ **free from $(5a)$** | proved + Lean | `proof/5b_upper_bound` |
| Theorem Q | the $\mathcal L(\lambda I-A)$ version: $(5b)$ as a **constant-rank** condition on $[U\mid P(\lambda)]$; matrix is $w_m\times(r+t)$, square $\iff q=t$ | proved | `proof/quotient_equivalence` (H.1, H.2) |
| $d=0$ boundary | $d=0$: $(A)$ automatic; $(S)\iff V\cap\ker(\lambda I-A)=0\ \forall\lambda$ | proved | `proof/d0_boundary` (H.3) |
| **fixed $U$** | $(5b)\iff$ the determinant divisor $\Delta_b$ of $[U\mid P(\lambda)]$ is a **nonzero constant** (Smith form) | proved + tool | docs/02 **J**; `tools/verification/poly_smith.py` |
| all maximal minors | equivalently: $\gcd$ of all $k\times k$ minors is a constant | proved + tool | docs/02 B.1; `tools/verification/spectral_gcd.py` |

**Consequence.** At a **fixed** $\mathcal L$, $(5b)$ is decidable in polynomial time (Smith form of a
polynomial matrix of degree $\le1$). The hardness, if any, is in the **choice** of $\mathcal L$.

---

## 2. Layers and regions where $(5b)$ is settled

| region | criterion | grade |
|---|---|---|
| $\rho=0$ | $\mathcal V\subseteq\mathcal J$; $(5b)$ automatic | proved |
| $\rho=d$ (top layer) | $(5b)\iff(D_W^{\mathsf T},T_W)$ observable (PBH) | proved + Lean kernel |
| $\mathcal V=\mathbb C^n$ | $(5b)\iff A^{\mathsf T}$ has no eigenvector in $\ker[C;CA]$ | proved |
| $c_0=1,\rho=d$ | $(5b)\iff v_W$ cyclic for $T_W$: $\operatorname{rank}[v_W;v_WT_W;\dots]=d$ | proved + Lean kernel |
| $(2,1)$ layer | the pencil has three $2\times2$ minors; the $\tau$-quantifier is eliminated by linear algebra; criterion is their $\gcd$ | proved / exact verification |
| $(3,1)$ layer, **single cell** | "is the cell covered" is decided by $\mu=\dim(B\cap\mathcal U)$ (C.1–C.5) | proved |
| $c=1$ branch | composed into a program with one named gap | see `proof/layer_program` |

**Not settled:** the layer-level decision for $0<\rho<d$ in general (this is the open part of the
"layer program"), and the complexity of the whole.

---

## 3. Structural obstacles (why integer conditions are not enough)

1. **Rank barrier** (F.1/F.2): a feasible layer forces $\rho\le r(\lambda):=\dim\pi(\mathbb C^n(\lambda I-A))$
   for **every** $\lambda$; hence $\min_\lambda r<\rho_{ci}\Rightarrow$ no solution. Verified on 1484 checks.
   — This is a genuine wall that no amount of combinatorics removes.
2. **Complementary obstruction** (`proof/h_bound`): if $\ker C=\mathcal V\oplus Z$ and $\dim V\ge1$, then
   $(S)$ fails for every $Z$ satisfying $(A)$. This requires **both** $N_c=h$ and $h=n-p$; the earlier
   unconditional version ("$h=n-p\Rightarrow$ fails") was wrong (R13, wide matrices).
3. **Non-monotonicity**: the order spectrum is **not** an interval; $\mathrm{DEC}(q)\not\Rightarrow\mathrm{DEC}(q+1)$
   (R17). Hence no binary search, and no reduction to pure combinatorics: the continuous parameters
   ($\mathcal V$, hence $\Theta$) genuinely matter.

---

## 4. Complexity

| result | content | grade |
|---|---|---|
| **upper bound** | $\mathrm{DEC}(q)\in\exists\mathbb R$; **chart-free** encoding: $O(n^3)$ variables/equations, degree $\le n$, no disjunction over charts | proved (paper) + partial Lean |
| older route | Smith-certificate version (`proof/spectral_locus`), superseded; its Lemma 1 ("no spurious failure at $\lambda=\infty$") must be stated **under $(A)$** | proved |
| **lower bound** | none. $\exists\mathbb R$-hardness / NP-hardness **unknown** | — |
| **encoding size (G.1)** | the three items required for "$\exists\mathbb R$-complete" — number of constraints, coefficient bit size, polynomial representation — **not proved** | — |

**So the state of the art is exactly: $\mathrm{DEC}(q)\in\exists\mathbb R$, nothing more.**

---

## 5. New results since 2026-11-01 (this week)

| result | statement | grade |
|---|---|---|
| **B.6** | $(5a)\Rightarrow$ every right minimal index of $Q_L$ is $0$ | proved + Lean kernel + 150/150 |
| **B.7** | $(5a)\Rightarrow$ every infinite elementary divisor has degree $1$, and $d_\infty=h-\operatorname{rank}L$ | proved + Lean kernel + 151/151 |
| **B.8** | $(5b)\iff d_{\rm fin}=0\iff\sum_j\varepsilon_j=\operatorname{rank}L$ (left minimal indices) | proved (corollary of B.6+B.7) |
| descriptor reduction | left indices of $Q_L$ = right indices of $R(\lambda)=[\lambda E-EX^{\mathsf T}\,B]$ = **controllability indices** of the descriptor system $(-E,-EX^{\mathsf T},B)$ | proved + 66/66 |
| observability chain | $L_k=[C;CA;\dots;CA^{k-1}]$ always satisfies $(5b)$; $(5a)$ needs chain closure | proved |

**What these do:** they describe the Kronecker data of the pencil for **any** $\mathcal L$ satisfying
$(5a)$, and they turn $(5b)$ into a **discrete equality** $\sum\varepsilon_j=\operatorname{rank}L$
(no quantifier over $\lambda$).

**What they do not do:** they do not decide $\mathrm{DEC}(q)$. The equality is a condition on a
Kronecker invariant; deciding whether *some* member of the admissible family satisfies it is still an
$\exists$ over continuous parameters.

---

## 6. Gaps (complete list)

| id | gap | status |
|---|---|---|
| **G-1** | complexity of $\mathrm{DEC}(q)$: lower bound ($\exists\mathbb R$-hard? NP-hard?) or polynomial algorithm | open; only $\in\exists\mathbb R$ known |
| **G-2** | the three encoding-size items of G.1 | open |
| **G-3** | the **left-index partition**: which sequences $(\varepsilon_1\ge\dots\ge\varepsilon_{q+2p-h})$ with $\sum\varepsilon_j=\operatorname{rank}L$ are realisable? In 140 feasible pencils spanning 35 aggregate groups $(q,p,h,\operatorname{rank}L)$ we found **no** two different partitions in one group — consistent with (but not proof of) "determined by the aggregate data" | open |
| **G-4** | evaluating $\sum\varepsilon$ over Fernando's **complete family** of minimum-$(A)$ augmentations (P1 Thm 3) is not implemented | engineering |

---

## 7. Corrections and process (for transparency)

* Retracted in this line: **R13** ($h=n-p\Rightarrow$ fail), **R17** (order-spectrum conjecture),
  **R18** (constant rank $\Rightarrow$ zero right indices), **R19** ($d_\infty=h-\operatorname{rank}L\iff\ker L=N$),
  **R20** ($d_\infty$ measured by polynomial degree instead of $\mu$-adic valuation),
  **R21** ($(5a)\Rightarrow\sum\varepsilon=\operatorname{rank}L$ — needs $-\,d_{\rm fin}$).
* Our own process failure: we re-derived $(5a)$-side facts (the decomposition
  $LA=\Lambda L+G_0C+G_1CA$, its Lean proof, and $P=(\lambda I-\Lambda)H$) that had existed since
  2026-10-21. We now maintain a machine-generated **claim index** (152 entries) and a rule to search by
  the *shape* of the claim before starting new work.

---

## 8. Questions

**Q1.** Given $(5b)\iff\sum_j\varepsilon_j=\operatorname{rank}L$ (B.8) and that the left indices are the
controllability indices of the descriptor system $(-E,-EX^{\mathsf T},B)$, is the right target
"decide whether Fernando's complete augmentation family contains a member with a prescribed index sum"?
Do you know of a complexity result for controllability-**index assignment** problems for descriptor
systems (or for "which index sequences are attainable")?

**Q2.** For G-3: are the possible left-index partitions for pencils of the form
$[\lambda E-EX^{\mathsf T}\ B]$ (with $[E\ B]$ of full row rank $h$ and $\operatorname{rank}E=\operatorname{rank}L$)
known? We suspect they are not determined by $(q,p,h,\operatorname{rank}L)$ alone, but our samples show no
counterexample.

**Q3.** For G-2 (encoding size): is there a standard way to bound the number of constraints and the
coefficient bit size for a chart-free $\exists\mathbb R$ encoding of a "$\forall\lambda$ rank" condition
that is already known in the literature (e.g. in the ∃R-completeness proofs for static output feedback)?

**Q4.** Given that B.7 depends on Smith forms over $\mathbb C[\mu]$, would you accept
"[proved on paper] + [exact verification 151/151]" as the permanent status, or is a Lean formalisation of
the determinantal-divisor lemma worth the cost?

---

## 9. Pointers

| path | content |
|---|---|
| `workspace/inventory/5b_map.md` | Chinese map of the same inventory (with per-item pointers) |
| `workspace/inventory/claims.tsv` | machine-generated claim index (152 entries) |
| `proof/README.md` | claim dependency table |
| `proof/dec_q_existsR/` | the $\exists\mathbb R$ upper bound |
| `proof/5a_archive/`, `proof/5b_upper_bound/` | the 2026-10-21 material (decomposition, pencil factorization, Lean) |
| `proof/h_bound/`, `proof/rank_barrier/` | structural obstacles |
| `proof/rho1_layer/`, `proof/layer_31_theorems/`, `proof/layer_program/` | layer criteria |
| `proof/kron_null_module/`, `proof/t4b_infinite_divisors/`, `proof/descriptor_reduction/` | this week's Kronecker results (B.6–B.8) |
