# Follow-up: the two remaining formalization gaps after Items 1, 2 and 4

This note reports what has been closed since the previous request and asks for two
specific things. Everything claimed as formalized below compiles in the pinned
environment (`leanprover/lean4:v4.35.0`, Mathlib `56a0058`) and passes `#print axioms`
with only `propext`, `Classical.choice`, `Quot.sound`.

## Part I. Closed since the previous note

### Item 1 — matrix-level rank identity (was the largest gap)

```lean
theorem rank_vstack_add_rank_mul {m n p r : ℕ}
    (P : Matrix (Fin m) (Fin n) K) (M : Matrix (Fin p) (Fin n) K)
    (N : Matrix (Fin n) (Fin r) K)
    (hN : ∀ v : Fin n → K, P.mulVec v = 0 ↔ ∃ w, N.mulVec w = v) :
    (Matrix.fromRows P M).rank = P.rank + (M * N).rank
```

Obtained through

```lean
noncomputable def sumArrowEquivProd (α β : Type*) :
    ((α ⊕ β) → K) ≃ₗ[K] ((α → K) × (β → K))

theorem rank_fromRows_add_map (P M) :
    (Matrix.fromRows P M).rank
      = P.rank + Module.finrank K ↥(Submodule.map M.mulVecLin P.mulVecLin.ker)
```

using `Matrix.rank` $=$ `Module.finrank` of the range of `mulVecLin` definitionally, plus
`finrank_range_prod` from the previous development. The remark in your reply that `hNr`
is redundant is confirmed: it is not used.

### Item 2 — rank-consistency criterion (now literally the paper's statement)

```lean
theorem exists_mulVec_eq_iff_rank_gram {m n : ℕ} (M : Matrix (Fin m) (Fin n) ℝ)
    (c : Fin m → ℝ) :
    (∃ b : Fin n → ℝ, M.mulVec b = c) ↔
      (M * Mᵀ).rank = (M * Mᵀ + Matrix.vecMulVec c c).rank
```

The augmented-matrix route worked as you predicted, with

```lean
def colMatrix (c : Fin m → ℝ) : Matrix (Fin m) (Fin 1) ℝ
def augment (M) (c) : Matrix (Fin m) (Fin n ⊕ Fin 1) ℝ := M.fromCols (colMatrix c)

theorem augment_mul_transpose (M) (c) :
    augment M c * (augment M c)ᵀ = M * Mᵀ + Matrix.vecMulVec c c

theorem rank_augment_eq_iff (M) (c) :
    (augment M c).rank = M.rank ↔ c ∈ LinearMap.range M.mulVecLin
```

Two things cost time and are worth recording:

* `Matrix.rank_self_mul_transpose` is the one for $MM^{\mathsf T}$ (as you said);
  `Matrix.rank_transpose_mul_self` is the one for $M^{\mathsf T}M$.
* The proof that $c$ lies in the range of the augmented matrix is easiest with
  `Pi.single (Sum.inr 0) 1` as the witness and `Matrix.mulVec_single_one`
  ($M\,e_j = \operatorname{col}_j M$); every attempt to obtain it from a
  `Sum.elim 0 1` witness ran into a `Pi.zero_apply`/`map_zero` mismatch inside
  `Matrix.mulVecLin`.

### Item 4 — coefficient extraction

```lean
theorem coeff_sum_finset {α} (s : Finset α) (f : α → K[X]) (k : ℕ) :
    (∑ a ∈ s, f a).coeff k = ∑ a ∈ s, (f a).coeff k

theorem coeff_mul_apply {ω n p} (A : Matrix (Fin ω) (Fin n) K[X])
    (B : Matrix (Fin n) (Fin p) K[X]) (i j) (k : ℕ) :
    ((A * B) i j).coeff k
      = ∑ a : Fin n, ∑ x ∈ Finset.antidiagonal k,
          (A i a).coeff x.1 * (B a j).coeff x.2
```

Your diagnosis was exactly right: `Polynomial.coeff_sum` is the wrong lemma for a general
`Finset.sum`; the Finset induction plus `Polynomial.coeff_mul` closes it in two lines.

---

## Part II. Two remaining asks

### Ask 1 (Item 3): the Cauchy–Binet step the certificate needs

What the paper uses is not the general rectangular formula, but the Gram special case:
for $Q(\lambda)$ of size $q\times\omega$,
$$\det\bigl(Q(\lambda)^{\mathsf T}Q(\lambda)\bigr)=\sum_{|I|=\omega}\det\bigl(Q_I(\lambda)\bigr)^2 .$$

**Question.** Given that `ClassicalGaps.cauchy_binet_det` is stated for Lean 4.30 /
Mathlib `c5ea003`, would you recommend

* (a) porting it verbatim to our pinned toolchain and then deriving the Gram case, or
* (b) proving only the Gram case directly (which may avoid the `Finset.powersetCard`
  reindexing entirely)?

If (b), what is the shortest route you would take in the pinned Mathlib — is there a
`det_mul`/`det_transpose`-based argument for $q\times\omega$ matrices, or is
`Matrix.det_apply` plus the Leibniz formula unavoidable?

### Ask 2 (Item 5): fixing the statement of the window certificate

Our difficulty is not the proof but the **statement**: the paper's Proposition 7 says the
spectral condition is equivalent to the solvability of $Z^{\mathsf T}Zx=e_0$ with
$x\in\mathbb R^{2\omega}$, where $Z$ is the matrix of coefficients of the $2\omega$ forms
built from the maximal minors. Before formalizing, we must fix $Z$ exactly.

**Question.** Which of the following would you formalize, and with which definition?

1. $Z:\mathbb R^{?}\to$ coefficients of the forms $f_I(\lambda)$ (degree $\le\omega$), one
   row per form or one column per form;
2. the identity $K(\alpha,\bar\alpha)=\sum_{I,J}|f_{I,J}(\alpha)|^2$ where $K$ is the
   Cauchy–Binet kernel of $Z^{\mathsf T}Z$;
3. the equivalence "the maximal minors have no common complex root $\iff$
   $Z^{\mathsf T}Zx=e_0$ is solvable".

We would rather receive the exact statement of a single theorem covering (1)–(3) than
guess at it; the proof can follow afterwards, and we are willing to leave it paper-level
if the statement itself cannot be made canonical.

---

## Part III. What stays paper-level regardless

The complexity bounds (Theorems 1 and 2, Corollaries 1 and 2), the coefficient-size
estimates, and the existential-real encoding (Theorem 3 and the appendix) are not planned
for formalization: Mathlib has no bit-complexity or $\exists\mathbb R$ infrastructure, and
the paper states them at the level of bit operations and formula size.


### Ask 3 (a Lean interface question that now blocks several matrix proofs)

After Items 1, 2 and 4 were closed, the next natural step is the matrix form of Lemma 2(i):
with $P_0=[C;CA]$, $M=[LA;L]$, $N$ a basis matrix of $\ker P_0$, one would like

```lean
theorem compression_rank_identity {p q n k : ℕ}
    (A : Matrix (Fin n) (Fin n) K) (C : Matrix (Fin p) (Fin n) K)
    (L : Matrix (Fin q) (Fin n) K) (N : Matrix (Fin n) (Fin k) K)
    (hN : ∀ v : Fin n → K,
      (Matrix.fromRows C (C * A)).mulVec v = 0 ↔ ∃ w, N.mulVec w = v) :
    (Matrix.fromRows (Matrix.fromRows C (C * A)) (Matrix.fromRows (L * A) L)).rank
      = (Matrix.fromRows C (C * A)).rank
        + (Matrix.fromRows (L * A * N) (L * N)).rank
```

which is `rank_vstack_add_rank_mul` applied to `P := Matrix.fromRows C (C * A)` and
`M := Matrix.fromRows (L * A) L`, followed by `Matrix.fromRows_mul`.

**It does not elaborate.** The error is

```
Application type mismatch: The argument hN has type
  ∀ v, C.fromRows (C * A) *ᵥ v = 0 ↔ ∃ w, N *ᵥ w = v
but is expected to have type
  ∀ v, ?m.105 *ᵥ v = 0 ↔ ∃ w, N *ᵥ w = v
```

i.e. the implicit row index `m` of `rank_vstack_add_rank_mul` stays a metavariable,
because `Matrix.fromRows C (C * A)` has row type `Fin p ⊕ Fin p` while the lemma's signature
is indexed by `Fin m`. We tried passing `P` explicitly, and `exact`/`have` forms, with the
same result.

The obvious fix is to state the rank identity for arbitrary finite index types,

```lean
theorem rank_fromRows_add_rank_mul' {m n p r : Type*} [Fintype m] [Fintype p] [Fintype n]
    [Fintype r] (P : Matrix m n K) (M : Matrix p n K) (N : Matrix n r K)
    (hN : ∀ v : n → K, P.mulVec v = 0 ↔ ∃ w, N.mulVec w = v) :
    (Matrix.fromRows P M).rank = P.rank + (M * N).rank
```

but then the whole chain has to be re-stated at that level: `rank_fromRows_add_map` is
`Fin`-indexed, and `finrank_range_prod` is already general.

**Question.** Which do you recommend:

* (a) generalise `rank_fromRows_add_map` (and hence `rank_vstack_add_rank_mul`) to arbitrary
  `[Fintype]` index types, so that `⊕`-indexed matrices are handled without casting, or
* (b) keep the `Fin` version and use `finSumFinEquiv : Fin m ⊕ Fin n ≃ Fin (m + n)` to
  reindex at each use site (`Matrix.reindex`), accepting the extra bookkeeping?

We suspect (a) is cleaner and would make Lemma 2(i) a two-line corollary, but we did not
want to restate the lemma chain without your view.
