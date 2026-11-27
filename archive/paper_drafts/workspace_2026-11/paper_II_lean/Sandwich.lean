/-
Q1Paper/PaperII/Sandwich.lean

Paper II's sandwich in the pair encoding: the forward direction, from a feasible
design to a feasible subspace `W`, together with the dimension bound `t ≤ r`.

The proof goes through Paper I's Claim 4 (`claim4_sandwich`), which lives in the
row(`[N  A N]`) encoding, and the column split `Φ` of `Interface.lean` that turns
that encoding into the pair encoding where Paper II's conditions (Claim 5) live.

Contents.
* `Ac`, `L0c`, `Rc`, `Lc` — complexifications of the system matrix, the prescribed
  block, the free block, and the design.
* `W0`, `TR`, `WR` — the paper's `W₀`, `T` and `W = row[L N  L A N]`.
* `fromRows_Lc` — `[L₀c; Rc] = (L₀;R)c`.
* `W0_eq_map`, `TR_eq_map`, `WR_eq_map` — the three subspaces are the `Φ`-images
  of the corresponding claim4 subspaces.
* `decC_to_feasible` — a feasible design of order `r` gives `W` with
  `W₀ ≤ W ≤ T`, `W` feasible, and `t = dim (W/W₀) ≤ r`.

Reuses: `Q1Paper.claim4_sandwich` (`PaperI/S02_Subspace/Claims38.lean`),
`Q1Paper.pairRowSpace`, `Q1Subspace.rowSpace`, `map_rowSpace_Mcol`,
`isFeasible_pairRowSpace_iff`, `t_le_iff` (`PaperII/Interface.lean`).

The converse (`feasible_to_decC`) and saturation are in `PaperII/Converse.lean`.
-/

import Q1Paper.PaperII.Interface

open Module Matrix

namespace Q1Paper.PaperII

variable {p r0 n k : ℕ}

/-! ### 1. Complexifications -/

/-- Complexification of the system matrix. -/
noncomputable def Ac (A : Matrix (Fin n) (Fin n) ℝ) : Matrix (Fin n) (Fin n) ℂ :=
  A.map (algebraMap ℝ ℂ)

/-- Complexification of the prescribed block. -/
noncomputable def L0c (L0 : Matrix (Fin r0) (Fin n) ℝ) : Matrix (Fin r0) (Fin n) ℂ :=
  L0.map (algebraMap ℝ ℂ)

/-- Complexification of a real free block. -/
noncomputable def Rc (R : Matrix (Fin r) (Fin n) ℝ) : Matrix (Fin r) (Fin n) ℂ :=
  R.map (algebraMap ℝ ℂ)

/-- Complexification of the design `[L₀; R]`. -/
noncomputable def Lc (L0 : Matrix (Fin r0) (Fin n) ℝ) (R : Matrix (Fin r) (Fin n) ℝ) :
    Matrix (Fin r0 ⊕ Fin r) (Fin n) ℂ :=
  (Matrix.fromRows L0 R).map (algebraMap ℝ ℂ)

/-- `[L₀c; Rc]` is the complexification of `[L₀;R]`. -/
theorem fromRows_Lc (L0 : Matrix (Fin r0) (Fin n) ℝ) (R : Matrix (Fin r) (Fin n) ℝ) :
    Matrix.fromRows (L0c L0) (Rc R) = Lc L0 R := by
  ext i j
  cases i <;> rfl

/-! ### 2. The three subspaces -/

/-- The paper's `T = row[N  A N]`, over `ℂ`. -/
noncomputable def TR (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ) :
    Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ)) :=
  Q1Paper.pairRowSpace N (Ac A * N)

/-- The paper's `W₀ = row[L₀N  L₀ A N]`, over `ℂ`. -/
noncomputable def W0 (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) : Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ)) :=
  Q1Paper.pairRowSpace (L0c L0 * N) (L0c L0 * (Ac A * N))

/-- The paper's `W = row[L N  L A N]` for the design `L = [L₀;R]`, over `ℂ`. -/
noncomputable def WR (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (R : Matrix (Fin r) (Fin n) ℝ) :
    Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ)) :=
  Q1Paper.pairRowSpace (Lc L0 R * N) (Lc L0 R * (Ac A * N))

/-! ### 3. The three subspaces as `Φ`-images -/

/-- `W₀` is the `Φ`-image of `row(L₀ [N AN])`. -/
theorem W0_eq_map (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) :
    W0 A N L0 = Submodule.map (Φ (K := ℂ)).toLinearMap
      (Q1Subspace.rowSpace (L0c L0 * Mcol N (Ac A))) := by
  rw [W0, map_rowSpace_Mcol (K := ℂ) N (Ac A) (Fin r0) (L0c L0)]

/-- `T` is the `Φ`-image of `row[N AN]`. -/
theorem TR_eq_map (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ) :
    TR A N = Submodule.map (Φ (K := ℂ)).toLinearMap
      (Q1Subspace.rowSpace (Mcol N (Ac A))) := by
  have h := map_rowSpace_Mcol (K := ℂ) N (Ac A) (Fin n) (1 : Matrix (Fin n) (Fin n) ℂ)
  simp only [Matrix.one_mul] at h
  rw [TR]
  exact h.symm

/-- `W` is the `Φ`-image of `row([L₀;R] [N AN])`. -/
theorem WR_eq_map (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (R : Matrix (Fin r) (Fin n) ℝ) :
    WR A N L0 R = Submodule.map (Φ (K := ℂ)).toLinearMap
      (Q1Subspace.rowSpace (Matrix.fromRows (L0c L0) (Rc R) * Mcol N (Ac A))) := by
  rw [WR, map_rowSpace_Mcol (K := ℂ) N (Ac A) (Fin r0 ⊕ Fin r)
    (Matrix.fromRows (L0c L0) (Rc R)), fromRows_Lc]

/-! ### 4. The forward direction of the sandwich -/

/-- **Sandwich, forward.**  A feasible design of order `r₀ + r` produces a subspace
`W` with `W₀ ≤ W ≤ T`, feasible, and of quotient dimension `t ≤ r`.

All three inequalities are Paper I's `claim4_sandwich`, transported from the
row(`[N AN]`) encoding to the pair encoding by the column split `Φ`. -/
theorem decC_to_feasible
    (C : Matrix (Fin p) (Fin n) ℝ) (A : Matrix (Fin n) (Fin n) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (hN : N.mulVecLin.range = (Matrix.fromRows ((C.map (algebraMap ℝ ℂ)) *
      (A.map (algebraMap ℝ ℂ))) (C.map (algebraMap ℝ ℂ))).mulVecLin.ker)
    {r : ℕ} (h : DecOrder C A L0 r) :
    ∃ W : Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ)),
      W0 A N L0 ≤ W ∧ W ≤ TR A N ∧ IsFeasible W ∧ t (W0 A N L0) W ≤ r := by
  obtain ⟨R, h1, h2⟩ := (PaperI.DEC_complex_iff_compressed C A L0 r N hN).mp h
  have hs := Q1Paper.claim4_sandwich (K := ℂ) (L0c L0) (Rc R) (Mcol N (Ac A))
  have hW0W : W0 A N L0 ≤ WR A N L0 R := by
    rw [W0_eq_map, WR_eq_map]
    exact Submodule.map_mono hs.1
  have hWT : WR A N L0 R ≤ TR A N := by
    rw [WR_eq_map, TR_eq_map]
    exact Submodule.map_mono hs.2.1
  have hdim : finrank ℂ ↥(WR A N L0 R) ≤ finrank ℂ ↥(W0 A N L0) + r := by
    have h := hs.2.2.1
    rw [Fintype.card_fin] at h
    rw [WR_eq_map, W0_eq_map,
      LinearEquiv.finrank_map_eq (Φ (K := ℂ))
        (Q1Subspace.rowSpace (Matrix.fromRows (L0c L0) (Rc R) * Mcol N (Ac A))),
      LinearEquiv.finrank_map_eq (Φ (K := ℂ))
        (Q1Subspace.rowSpace (L0c L0 * Mcol N (Ac A)))]
    exact h
  refine ⟨WR A N L0 R, hW0W, hWT, ?_, ?_⟩
  · have h1' : PaperI.compressedAlgebraic (Lc L0 R * N) (Lc L0 R * (Ac A * N)) :=
      (Matrix.mul_assoc (Lc L0 R) (Ac A) N) ▸ h1
    have h2' : PaperI.compressedSpectral (Lc L0 R * N) (Lc L0 R * (Ac A * N)) :=
      (Matrix.mul_assoc (Lc L0 R) (Ac A) N) ▸ h2
    exact (isFeasible_pairRowSpace_iff (Lc L0 R * N) (Lc L0 R * (Ac A * N))).mpr
      ⟨h1', h2'⟩
  · rw [t_le_iff hW0W]
    exact hdim

end Q1Paper.PaperII
