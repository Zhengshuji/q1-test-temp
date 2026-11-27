/-
Q1Paper/PaperII/Monotone.lean

Paper II, Claim `lem:monotone`, the monotone half: a feasible real design can be
padded with zero rows, so `DECℂ r → DECℂ (r + c)`.

Contents.
* `pairRowSpace_fromRows` — the pair row space splits over a row stacking.
* `pairRowSpace_pad` — adjoining zero rows to the free block leaves `W` unchanged.
* `decC_mono_add` — `DECℂ r → DECℂ (r + c)`.
* `decC_mono` — `DECℂ r → DECℂ r'` for `r ≤ r'`.

Reuses: `Q1Paper.pairRowSpace`, `Matrix.fromRows_mul`,
`isFeasible_pairRowSpace_iff` (`PaperII/Interface.lean`),
`PaperI.DEC_complex_iff_compressed` (`PaperI/S01_Compression/CompressionMatrix.lean`).
-/

import Q1Paper.PaperII.Sandwich

open Module Matrix

namespace Q1Paper.PaperII

/-- **The pair row space splits over a row stacking.** -/
theorem pairRowSpace_fromRows {K : Type*} [Field K] {q1 q2 k : Type*}
    [Fintype q1] [Fintype q2] [Fintype k]
    (H1 : Matrix q1 k K) (H2 : Matrix q2 k K)
    (HA1 : Matrix q1 k K) (HA2 : Matrix q2 k K) :
    Q1Paper.pairRowSpace (Matrix.fromRows H1 H2) (Matrix.fromRows HA1 HA2)
      = Q1Paper.pairRowSpace H1 HA1 ⊔ Q1Paper.pairRowSpace H2 HA2 := by
  have hset : Set.range (fun i : q1 ⊕ q2 =>
        (Matrix.fromRows H1 H2 i, Matrix.fromRows HA1 HA2 i)) =
      Set.range (fun i : q1 => (H1 i, HA1 i)) ∪
        Set.range (fun j : q2 => (H2 j, HA2 j)) := by
    ext p
    constructor
    · rintro ⟨i, rfl⟩
      cases i with
      | inl i => exact Or.inl ⟨i, rfl⟩
      | inr j => exact Or.inr ⟨j, rfl⟩
    · rintro (⟨i, rfl⟩ | ⟨j, rfl⟩)
      · exact ⟨Sum.inl i, rfl⟩
      · exact ⟨Sum.inr j, rfl⟩
  rw [Q1Paper.pairRowSpace, Q1Paper.pairRowSpace, Q1Paper.pairRowSpace, hset,
    Submodule.span_union]

/-- **Adjoining zero rows leaves the pair row space unchanged.** -/
theorem pairRowSpace_pad {K : Type*} [Field K] {r c n k : ℕ}
    (N : Matrix (Fin n) (Fin k) K) (HA : Matrix (Fin n) (Fin k) K)
    (R : Matrix (Fin r) (Fin n) K) (R' : Matrix (Fin (r + c)) (Fin n) K)
    (hpad : ∀ i : Fin (r + c), ∀ h : (i : ℕ) < r, R' i = R ⟨i, h⟩)
    (hzero : ∀ i : Fin (r + c), ¬ (i : ℕ) < r → R' i = 0) :
    Q1Paper.pairRowSpace (R' * N) (R' * HA)
      = Q1Paper.pairRowSpace (R * N) (R * HA) := by
  apply le_antisymm
  · rw [Q1Paper.pairRowSpace, Submodule.span_le]
    rintro _ ⟨i, rfl⟩
    change ((R' * N) i, (R' * HA) i) ∈ Q1Paper.pairRowSpace (R * N) (R * HA)
    by_cases h : (i : ℕ) < r
    · have hi : R' i = R ⟨i, h⟩ := hpad i h
      have hrow1 : (R' * N) i = (R * N) ⟨i, h⟩ := by
        funext j
        simp only [Matrix.mul_apply, hi]
      have hrow2 : (R' * HA) i = (R * HA) ⟨i, h⟩ := by
        funext j
        simp only [Matrix.mul_apply, hi]
      rw [hrow1, hrow2]
      exact Submodule.subset_span ⟨⟨i, h⟩, rfl⟩
    · have hi : R' i = 0 := hzero i h
      have hrow1 : (R' * N) i = 0 := by
        funext j
        simp only [Matrix.mul_apply, hi, Pi.zero_apply, zero_mul, Finset.sum_const_zero]
      have hrow2 : (R' * HA) i = 0 := by
        funext j
        simp only [Matrix.mul_apply, hi, Pi.zero_apply, zero_mul, Finset.sum_const_zero]
      rw [hrow1, hrow2]
      exact Submodule.zero_mem _
  · rw [Q1Paper.pairRowSpace, Submodule.span_le]
    rintro _ ⟨j, rfl⟩
    change ((R * N) j, (R * HA) j) ∈ Q1Paper.pairRowSpace (R' * N) (R' * HA)
    have hlt : (j : ℕ) < r + c := Nat.lt_add_right c j.isLt
    have hi : R' ⟨j, hlt⟩ = R j := hpad ⟨j, hlt⟩ j.isLt
    have hrow1 : (R * N) j = (R' * N) ⟨j, hlt⟩ := by
      funext l
      simp only [Matrix.mul_apply, hi]
    have hrow2 : (R * HA) j = (R' * HA) ⟨j, hlt⟩ := by
      funext l
      simp only [Matrix.mul_apply, hi]
    rw [hrow1, hrow2]
    exact Submodule.subset_span ⟨⟨j, hlt⟩, rfl⟩

variable {p r0 n k : ℕ}

/-- **Monotonicity, with `c` zero rows.**  `DECℂ r → DECℂ (r + c)`. -/
theorem decC_mono_add
    (C : Matrix (Fin p) (Fin n) ℝ) (A : Matrix (Fin n) (Fin n) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (hN : N.mulVecLin.range = (Matrix.fromRows ((C.map (algebraMap ℝ ℂ)) *
      (A.map (algebraMap ℝ ℂ))) (C.map (algebraMap ℝ ℂ))).mulVecLin.ker)
    {r : ℕ} (c : ℕ) (h : DecOrder C A L0 r) :
    DecOrder C A L0 (r + c) := by
  classical
  obtain ⟨R, h1, h2⟩ := (PaperI.DEC_complex_iff_compressed C A L0 r N hN).mp h
  -- the compressed conditions in the pair-space shape used below
  have h1' : IsFeasible (Q1Paper.pairRowSpace (Lc L0 R * N) (Lc L0 R * (Ac A * N))) := by
    refine (isFeasible_pairRowSpace_iff (Lc L0 R * N) (Lc L0 R * (Ac A * N))).mpr ⟨?_, ?_⟩
    · rw [← Matrix.mul_assoc]; exact h1
    · rw [← Matrix.mul_assoc]; exact h2
  -- the padded real design
  set R' : Matrix (Fin (r + c)) (Fin n) ℝ :=
    fun i j => if h : (i : ℕ) < r then R ⟨i, h⟩ j else 0 with hR'def
  have hpad : ∀ i : Fin (r + c), ∀ h : (i : ℕ) < r, R' i = R ⟨i, h⟩ := by
    intro i h
    funext j
    simp only [hR'def, dif_pos h]
  have hzero : ∀ i : Fin (r + c), ¬ (i : ℕ) < r → R' i = 0 := by
    intro i h
    funext j
    simp only [hR'def, dif_neg h, Pi.zero_apply]
  -- its complexification, padded
  set Rc' : Matrix (Fin (r + c)) (Fin n) ℂ := fun i j => algebraMap ℝ ℂ (R' i j) with hRc'def
  have hpadC : ∀ i : Fin (r + c), ∀ h : (i : ℕ) < r, Rc' i = Rc R ⟨i, h⟩ := by
    intro i h
    ext j
    simp only [hRc'def, Rc, Matrix.map_apply, hpad i h]
  have hzeroC : ∀ i : Fin (r + c), ¬ (i : ℕ) < r → Rc' i = 0 := by
    intro i h
    ext j
    simp only [hRc'def, hzero i h, Pi.zero_apply, map_zero]
  have hpadRow : Q1Paper.pairRowSpace (Rc' * N) (Rc' * (Ac A * N))
      = Q1Paper.pairRowSpace (Rc R * N) (Rc R * (Ac A * N)) :=
    pairRowSpace_pad N (Ac A * N) (Rc R) Rc' hpadC hzeroC
  -- the two designs have the same W
  have hW : Q1Paper.pairRowSpace (Lc L0 R' * N) (Lc L0 R' * (Ac A * N))
      = Q1Paper.pairRowSpace (Lc L0 R * N) (Lc L0 R * (Ac A * N)) := by
    have hL' : Lc L0 R' = Matrix.fromRows (L0c L0) Rc' := by
      ext i j; cases i <;> rfl
    have hL : Lc L0 R = Matrix.fromRows (L0c L0) (Rc R) := by
      ext i j; cases i <;> rfl
    rw [hL', hL, Matrix.fromRows_mul, Matrix.fromRows_mul, Matrix.fromRows_mul,
      Matrix.fromRows_mul, pairRowSpace_fromRows, pairRowSpace_fromRows, hpadRow]
  have hfeas' : IsFeasible (Q1Paper.pairRowSpace (Lc L0 R' * N) (Lc L0 R' * (Ac A * N))) := by
    rw [hW]
    exact h1'
  refine (PaperI.DEC_complex_iff_compressed C A L0 (r + c) N hN).mpr ⟨R', ?_, ?_⟩
  · have := (isFeasible_pairRowSpace_iff (Lc L0 R' * N) (Lc L0 R' * (Ac A * N))).mp hfeas'
    rw [Matrix.mul_assoc]
    exact this.1
  · have := (isFeasible_pairRowSpace_iff (Lc L0 R' * N) (Lc L0 R' * (Ac A * N))).mp hfeas'
    rw [Matrix.mul_assoc]
    exact this.2

/-- **Monotonicity**: `DECℂ r → DECℂ r'` for `r ≤ r'`. -/
theorem decC_mono
    (C : Matrix (Fin p) (Fin n) ℝ) (A : Matrix (Fin n) (Fin n) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (hN : N.mulVecLin.range = (Matrix.fromRows ((C.map (algebraMap ℝ ℂ)) *
      (A.map (algebraMap ℝ ℂ))) (C.map (algebraMap ℝ ℂ))).mulVecLin.ker)
    {r r' : ℕ} (hrr : r ≤ r') (h : DecOrder C A L0 r) :
    DecOrder C A L0 r' := by
  have h' : r' = r + (r' - r) := (Nat.add_sub_cancel' hrr).symm
  rw [h']
  exact decC_mono_add C A L0 N hN (r' - r) h

end Q1Paper.PaperII
