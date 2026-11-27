/-
Q1Paper/PaperII/Interface.lean

Paper II's interface layer: the quotient dimension `t = dim (W/W₀)` and the two
encodings of the compressed data — the row(`[N  A N]`) encoding used by Paper I's
Claim 4, and the pair encoding `pairRowSpace` used by Claims 5–6.

Paper II's spectral condition lives over `ℂ` (real design, complex ranks); the
column-split lemmas below are field-generic and are used at `K = ℂ`.

Contents.
* `Mcol N A` — the compressed matrix `[N  A N]`, with columns split into the two
  halves by `Fin.addCases`.
* `Φ` — the column split `(Fin (k+k) → K) ≃ₗ (Fin k → K) × (Fin k → K)`.
* `Φ_vecMul` — `Φ (u * [N AN]) = (u * N, u * (A N))`, row by row.
* `map_rowSpace_Mcol` — the two encodings agree:
  `Φ '' rowSpace (L * [N AN]) = pairRowSpace (L * N) (L * (A * N))`.
* `t W₀ W` — the paper's `t = dim (W/W₀)`.
* `t_eq_finrank_sub` — `t = dim W − dim W₀` for `W₀ ≤ W`.
* `t_le_iff` — `t ≤ r ↔ dim W ≤ dim W₀ + r`, the hypothesis form of Claim 4.
* `DecOrder` — Paper II's decision predicate, read through `PaperI.DECℂ`.

Reuses: `Q1Subspace.rowSpace` (`RowSpaceAlgebraic.lean`), `Q1Paper.pairRowSpace`
(`PaperI/S02_Subspace/Claims38.lean`), `Q1Paper.PaperI.DECℂ`
(`PaperI/S00_Interface/Interface.lean`), `LinearEquiv.sumArrowLequivProdArrow`,
`finSumFinEquiv`, `Fin.addCases`.
-/

import Q1Paper.PaperI.S00_Interface.MainTheorems

open Module Matrix

namespace Q1Paper.PaperII

variable {K : Type*} [Field K]

/-! ### 1. The two encodings of the compressed data -/

/-- The compressed matrix `[N  A N]`, with columns indexed by `Fin (k + k)` and
split into the two halves by `Fin.addCases`. -/
def Mcol {n k : ℕ} (N : Matrix (Fin n) (Fin k) K) (A : Matrix (Fin n) (Fin n) K) :
    Matrix (Fin n) (Fin (k + k)) K :=
  fun i => Fin.addCases (fun j => N i j) (fun j => (A * N) i j)

/-- The column split `(Fin (k+k) → K) ≃ₗ (Fin k → K) × (Fin k → K)`, i.e. reading a
row of `[N  A N]` as a row pair. -/
noncomputable def Φ {k : ℕ} : ((Fin (k + k)) → K) ≃ₗ[K] ((Fin k → K) × (Fin k → K)) :=
  (LinearEquiv.funCongrLeft K K (finSumFinEquiv : Fin k ⊕ Fin k ≃ Fin (k + k))).trans
    (LinearEquiv.sumArrowLequivProdArrow (Fin k) (Fin k) K K)

/-- The left half of `Mcol`. -/
theorem Mcol_left {n k : ℕ} (N : Matrix (Fin n) (Fin k) K) (A : Matrix (Fin n) (Fin n) K)
    (i : Fin n) (j : Fin k) : Mcol N A i (Fin.castAdd k j) = N i j :=
  Fin.addCases_left j

/-- The right half of `Mcol`. -/
theorem Mcol_right {n k : ℕ} (N : Matrix (Fin n) (Fin k) K) (A : Matrix (Fin n) (Fin n) K)
    (i : Fin n) (j : Fin k) : Mcol N A i (Fin.natAdd k j) = (A * N) i j :=
  Fin.addCases_right j

/-- The value of `Φ` on a row. -/
theorem Φ_apply {k : ℕ} (g : Fin (k + k) → K) :
    Φ (K := K) g = ((fun j : Fin k => g (finSumFinEquiv (Sum.inl j))),
      (fun j : Fin k => g (finSumFinEquiv (Sum.inr j)))) := by
  apply Prod.ext <;> funext j <;> rfl

/-- **Row by row, the column split is the row pair.**  For a row vector `u`,
`Φ (u * Mcol N A) = (u * N, u * (A N))`. -/
theorem Φ_vecMul {n k : ℕ} (N : Matrix (Fin n) (Fin k) K) (A : Matrix (Fin n) (Fin n) K)
    (u : Fin n → K) :
    Φ (K := K) (u ᵥ* Mcol N A) = (u ᵥ* N, u ᵥ* (A * N)) := by
  rw [Φ_apply]
  apply Prod.ext
  · funext j
    show (u ᵥ* Mcol N A) (finSumFinEquiv (Sum.inl j)) = (u ᵥ* N) j
    simp only [Matrix.vecMul]
    rw [finSumFinEquiv_apply_left]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    show u i * Mcol N A i (Fin.castAdd k j) = u i * N i j
    rw [Mcol_left]
  · funext j
    show (u ᵥ* Mcol N A) (finSumFinEquiv (Sum.inr j)) = (u ᵥ* (A * N)) j
    simp only [Matrix.vecMul]
    rw [finSumFinEquiv_apply_right]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    show u i * Mcol N A i (Fin.natAdd k j) = u i * (A * N) i j
    rw [Mcol_right]

/-- **The two encodings agree.**  The row space of `L * [N  A N]`, read through the
column split, is the pair row space `row[L N  L A N]`. -/
theorem map_rowSpace_Mcol {n k : ℕ} (N : Matrix (Fin n) (Fin k) K)
    (A : Matrix (Fin n) (Fin n) K) (q : Type*) [Fintype q]
    (L : Matrix q (Fin n) K) :
    Submodule.map (Φ (K := K)).toLinearMap (Q1Subspace.rowSpace (L * Mcol N A))
      = Q1Paper.pairRowSpace (L * N) (L * (A * N)) := by
  have hrow : ∀ i : q, Φ (K := K) ((L * Mcol N A) i) = ((L * N) i, (L * (A * N)) i) := by
    intro i
    show Φ (K := K) ((L i) ᵥ* Mcol N A) = ((L * N) i, (L * (A * N)) i)
    rw [Φ_vecMul]
    rfl
  rw [Q1Subspace.rowSpace, Submodule.map_span]
  have himg : (fun x : (Fin (k + k) → K) => (Φ (K := K)).toLinearMap x) ''
      Set.range (fun i : q => (L * Mcol N A) i)
      = Set.range (fun i : q => ((L * N) i, (L * (A * N)) i)) := by
    ext x
    constructor
    · rintro ⟨y, ⟨i, rfl⟩, rfl⟩
      exact ⟨i, (hrow i).symm⟩
    · rintro ⟨i, rfl⟩
      exact ⟨(L * Mcol N A) i, ⟨i, rfl⟩, hrow i⟩
  rw [himg]
  rfl

/-! ### 2. The quotient dimension `t = dim (W/W₀)` -/

section Quotient

variable {E : Type*} [AddCommGroup E] [Module K E] [FiniteDimensional K E]

/-- **The paper's `t = dim (W/W₀)`**, the quotient dimension of the sandwich. -/
noncomputable def t (W₀ W : Submodule K E) : ℕ :=
  finrank K (↥W ⧸ W₀.comap W.subtype)

/-- **`t = dim W − dim W₀`** for `W₀ ≤ W`. -/
theorem t_eq_finrank_sub {W₀ W : Submodule K E} (h : W₀ ≤ W) :
    t W₀ W = finrank K ↥W - finrank K ↥W₀ := by
  have hq := Submodule.finrank_quotient_add_finrank (R := K) (M := ↥W)
    (W₀.comap W.subtype)
  have hdim : finrank K ↥(W₀.comap W.subtype) = finrank K ↥W₀ :=
    LinearEquiv.finrank_eq (Submodule.comapSubtypeEquivOfLe h)
  rw [t]
  omega

/-- **`t ≤ r` is the dimension bound of Claim 4**: for `W₀ ≤ W`,
`t W₀ W ≤ r ↔ dim W ≤ dim W₀ + r`. -/
theorem t_le_iff {W₀ W : Submodule K E} (h : W₀ ≤ W) {r : ℕ} :
    t W₀ W ≤ r ↔ finrank K ↥W ≤ finrank K ↥W₀ + r := by
  rw [t_eq_finrank_sub h]
  have hmono : finrank K ↥W₀ ≤ finrank K ↥W := Submodule.finrank_mono h
  omega

end Quotient

/-! ### 3. Paper II's decision predicate -/

/-- **Paper II's decision predicate**: a real observer block, ranks over `ℂ`.  This
is `PaperI.DECℂ`, given a Paper II-local name so that the claims table can refer to
it without ambiguity with Paper I's `DEC` (which quantifies over the real field). -/
abbrev DecOrder {p r0 n : ℕ} (C : Matrix (Fin p) (Fin n) ℝ) (A : Matrix (Fin n) (Fin n) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (r : ℕ) : Prop :=
  Q1Paper.PaperI.DECℂ C A L0 r

/-! ### 4. Feasibility of a subspace -/

section Feasible

variable {F : Type*} [AddCommGroup F] [Module K F]

/-- **Paper II's feasibility predicate on `W`**: the algebraic condition
`π₂ W ≤ π₁ W` and the spectral condition `dim (π_λ W) = dim (π₁ W)` for every `λ`.
For `W = pairRowSpace H H_A` this is exactly the pair of compressed conditions
(`isFeasible_pairRowSpace_iff`). -/
def IsFeasible (W : Submodule K (F × F)) : Prop :=
  Q1Subspace.pi2 W ≤ Q1Subspace.pi1 W ∧
    ∀ lam : K, finrank K ↥(Q1Subspace.piLam lam W) = finrank K ↥(Q1Subspace.pi1 W)

/-- **Feasibility is the pair of compressed conditions** (Claim 5). -/
theorem isFeasible_pairRowSpace_iff {q k : Type*} [Fintype q] [Fintype k]
    (H HA : Matrix q k K) :
    IsFeasible (Q1Paper.pairRowSpace H HA) ↔
      PaperI.compressedAlgebraic H HA ∧ PaperI.compressedSpectral H HA := by
  have h := Q1Paper.claim5_conditions_depend_on_W (K := K) H HA
  constructor
  · rintro ⟨h1, h2⟩
    exact ⟨h.1.mpr h1, h.2.mpr h2⟩
  · rintro ⟨h1, h2⟩
    exact ⟨h.1.mp h1, h.2.mp h2⟩

end Feasible

end Q1Paper.PaperII
