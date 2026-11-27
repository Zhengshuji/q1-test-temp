/-
Q1Paper/PaperII/Saturate.lean

Paper II, Claim `lem:monotone`, the saturation half: `DEC r` and `DEC m` are
equivalent for `m = dim (T/W₀) ≤ r`, for the field-generic predicate `PaperI.DEC`
over `ℂ` (complex designs; see `Converse.lean` for the scope note on `DECℂ`).

Both directions go through the sandwich:
* forward: `DEC r` gives a feasible `W` with `t(W) ≤ r`; since `t` is monotone in
  `W` and `W ≤ T`, `t(W) ≤ t(T) = m`, so the converse (`feasible_to_DEC`) gives
  `DEC m`;
* backward: `DEC m` gives `W` with `t(W) ≤ m ≤ r`, so the converse gives `DEC r`.

Contents.
* `DEC_to_feasible_c` — the forward sandwich for the complex-design predicate.
* `t_le_t_of_le` — `t` is monotone in the subspace.
* `dec_saturates` — `DEC r ↔ DEC m` for `m ≤ r`.
* `dec_mono_complex` — `DEC r → DEC r'` for `r ≤ r'` (via saturation and
  `claim7_DEC_succ`).

Reuses: `PaperI.claim4_sandwich`, `PaperI.DEC_iff_compressed`,
`PaperI.claim7_DEC_succ`, `feasible_to_DEC`, `t_eq_finrank_sub`, `t_le_iff`.
-/

import Q1Paper.PaperII.Converse

open Module Matrix

namespace Q1Paper.PaperII

variable {p r0 n k : ℕ}

/-! ### 1. The forward sandwich for complex designs -/

/-- **Sandwich, forward (complex designs).**  `DEC r` gives a feasible `W` with
`W₀ ≤ W ≤ T` and `t ≤ r`. -/
theorem DEC_to_feasible_c
    (C : Matrix (Fin p) (Fin n) ℂ) (A : Matrix (Fin n) (Fin n) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (hN : N.mulVecLin.range = (Matrix.fromRows (C * Ac A) C).mulVecLin.ker)
    {r : ℕ} (h : PaperI.DEC C (Ac A) (L0c L0) r) :
    ∃ W : Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ)),
      W0 A N L0 ≤ W ∧ W ≤ TR A N ∧ IsFeasible W ∧ t (W0 A N L0) W ≤ r := by
  obtain ⟨R, h1, h2⟩ := (PaperI.DEC_iff_compressed C (Ac A) (L0c L0) r N hN).mp h
  have hs := Q1Paper.claim4_sandwich (K := ℂ) (L0c L0) R (Mcol N (Ac A))
  have hW0W : W0 A N L0 ≤ WRc A N L0 R := by
    rw [W0_eq_map, WRc_eq_map]
    exact Submodule.map_mono hs.1
  have hWT : WRc A N L0 R ≤ TR A N := by
    rw [WRc_eq_map, TR_eq_map]
    exact Submodule.map_mono hs.2.1
  have hdim : finrank ℂ ↥(WRc A N L0 R) ≤ finrank ℂ ↥(W0 A N L0) + r := by
    have h := hs.2.2.1
    rw [Fintype.card_fin] at h
    rw [WRc_eq_map, W0_eq_map,
      LinearEquiv.finrank_map_eq (Φ (K := ℂ))
        (Q1Subspace.rowSpace (Matrix.fromRows (L0c L0) R * Mcol N (Ac A))),
      LinearEquiv.finrank_map_eq (Φ (K := ℂ))
        (Q1Subspace.rowSpace (L0c L0 * Mcol N (Ac A)))]
    exact h
  refine ⟨WRc A N L0 R, hW0W, hWT, ?_, ?_⟩
  · have h1' : IsFeasible (Q1Paper.pairRowSpace
        (Matrix.fromRows (L0c L0) R * N) (Matrix.fromRows (L0c L0) R * (Ac A * N))) := by
      refine (isFeasible_pairRowSpace_iff _ _).mpr ⟨?_, ?_⟩
      · rw [← Matrix.mul_assoc]; exact h1
      · rw [← Matrix.mul_assoc]; exact h2
    exact h1'
  · rw [t_le_iff hW0W]
    exact hdim

/-! ### 2. Monotonicity of `t` -/

/-- **`t` is monotone in the subspace**: `W₀ ≤ V ≤ T` gives `t(V) ≤ t(T)`. -/
theorem t_le_t_of_le {K : Type*} [Field K] {E : Type*} [AddCommGroup E] [Module K E]
    [FiniteDimensional K E] {W₀ V T : Submodule K E} (hW0 : W₀ ≤ V) (hVT : V ≤ T) :
    t W₀ V ≤ t W₀ T := by
  rw [t_eq_finrank_sub hW0, t_eq_finrank_sub (hW0.trans hVT)]
  have hmono : finrank K ↥V ≤ finrank K ↥T := Submodule.finrank_mono hVT
  have hmono0 : finrank K ↥W₀ ≤ finrank K ↥V := Submodule.finrank_mono hW0
  omega

/-! ### 3. Saturation -/

/-- **Saturation.**  With `m = dim (T/W₀)`, `DEC r` and `DEC m` are equivalent
whenever `m ≤ r`: every feasible design can be compressed to `m` rows, and `m` rows
suffice for any order at least `m` above `r₀`. -/
theorem dec_saturates
    (C : Matrix (Fin p) (Fin n) ℂ) (A : Matrix (Fin n) (Fin n) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (hN : N.mulVecLin.range = (Matrix.fromRows (C * Ac A) C).mulVecLin.ker)
    {r : ℕ} (h : t (W0 A N L0) (TR A N) ≤ r) :
    PaperI.DEC C (Ac A) (L0c L0) r ↔
      PaperI.DEC C (Ac A) (L0c L0) (t (W0 A N L0) (TR A N)) := by
  constructor
  · intro hr
    obtain ⟨W, hW0, hWT, hWf, hWt⟩ := DEC_to_feasible_c C A L0 N hN hr
    have hmono : t (W0 A N L0) W ≤ t (W0 A N L0) (TR A N) := t_le_t_of_le hW0 hWT
    exact feasible_to_DEC C A L0 N hN hW0 hWT hWf hmono
  · intro hm
    obtain ⟨W, hW0, hWT, hWf, hWt⟩ := DEC_to_feasible_c C A L0 N hN hm
    exact feasible_to_DEC C A L0 N hN hW0 hWT hWf (le_trans hWt h)

/-! ### 4. Monotonicity in the order -/

/-- **Monotonicity**: `DEC r → DEC r'` for `r ≤ r'`, by saturation and Paper I's
`claim7_DEC_succ`. -/
theorem dec_mono_complex
    (C : Matrix (Fin p) (Fin n) ℂ) (A : Matrix (Fin n) (Fin n) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (hN : N.mulVecLin.range = (Matrix.fromRows (C * Ac A) C).mulVecLin.ker)
    {r r' : ℕ} (hrr : r ≤ r') (h : PaperI.DEC C (Ac A) (L0c L0) r) :
    PaperI.DEC C (Ac A) (L0c L0) r' := by
  -- pad one row at a time from `r` to `r'`
  have hstep : ∀ d : ℕ, PaperI.DEC C (Ac A) (L0c L0) (r + d) := by
    intro d
    induction d with
    | zero => simpa using h
    | succ d ih =>
        have := Q1Paper.claim7_DEC_succ (K := ℂ) C (Ac A) (L0c L0) (r + d) ih
        simpa [Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using this
  have h' : r' = r + (r' - r) := (Nat.add_sub_cancel' hrr).symm
  rw [h']
  exact hstep (r' - r)

end Q1Paper.PaperII
