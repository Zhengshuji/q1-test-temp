/-
Q1Paper/PaperII/Realification.lean

Real-design bridges: the real-compression lemma `real_compress` (upgrade of the
complex-design results to the paper's real-design specification `DECℂ`), the
real-design minimum order `tMinC` with its saturation and bounds, and the
complexification of real subspaces (`UC`, `finrank_UC`).

The pair row space `row[H  H_A]` is encoded in `K^{k+k}` by stacking the two blocks
of each row (`pairRows`); the column split `Φ` reads that encoding as row pairs.
Complexifying a real matrix commutes with this encoding, and the dimension of the
pair row space is the rank of the encoded matrix, so `rank_map_ofReal` gives
`dim_ℂ W = dim_ℝ V` for a real design — the identity the compression needs.

Contents.
* `pairRows` — the encoded matrix `row ↦ (row of H, row of H_A)`.
* `Φ_pairRows` — `Φ` reads it as the row pair.
* `pairRowSpace_eq_map_pairRows` — `row[H H_A]` is the `Φ`-image of its row space.
* `finrank_pairRowSpace_eq_rank` — its dimension is the rank of the encoded matrix.
* `pairRows_map` — encoding commutes with complexification.

Next step: the compression itself — a real design of `r` rows re-realised with
`t = dim (W/W₀)` rows by applying Paper I's `claim4_converse` over `ℝ` to the real
row space and complexifying.
-/

import Q1Paper.PaperII.Saturate
import Q1Paper.PaperII.MinOrder
import Q1Paper.PaperII.Tightness
import Q1Paper.PaperII.Monotone
import Q1Paper.PaperI.S08_ChartEquivalence.DecComplex

set_option maxHeartbeats 1000000

open Module Matrix

namespace Q1Paper.PaperII

variable {K : Type*} [Field K] {k : ℕ}

/-- The encoded matrix whose rows are the pairs `(H i, H_A i)`. -/
def pairRows {q : Type*} {k : ℕ} (H : Matrix q (Fin k) K) (HA : Matrix q (Fin k) K) :
    Matrix q (Fin (k + k)) K :=
  fun i => Fin.addCases (fun j => H i j) (fun j => HA i j)

/-- `Φ` reads an encoded row as the row pair. -/
theorem Φ_pairRows {q : Type*} {k : ℕ} (H : Matrix q (Fin k) K) (HA : Matrix q (Fin k) K)
    (i : q) : Φ (K := K) (pairRows H HA i) = (H i, HA i) := by
  rw [Φ_apply]
  apply Prod.ext <;> funext j
  · show pairRows H HA i (finSumFinEquiv (Sum.inl j)) = H i j
    rw [finSumFinEquiv_apply_left]
    exact Fin.addCases_left j
  · show pairRows H HA i (finSumFinEquiv (Sum.inr j)) = HA i j
    rw [finSumFinEquiv_apply_right]
    exact Fin.addCases_right j

/-- **The pair row space is the `Φ`-image of the encoded row space.** -/
theorem pairRowSpace_eq_map_pairRows {q : Type*} [Fintype q] {k : ℕ}
    (H : Matrix q (Fin k) K) (HA : Matrix q (Fin k) K) :
    Q1Paper.pairRowSpace H HA
      = Submodule.map (Φ (K := K)).toLinearMap
        (Q1Subspace.rowSpace (pairRows H HA)) := by
  rw [Q1Paper.pairRowSpace, Q1Subspace.rowSpace, Submodule.map_span]
  congr 1
  ext p
  constructor
  · rintro ⟨i, rfl⟩
    exact ⟨pairRows H HA i, ⟨i, rfl⟩, Φ_pairRows H HA i⟩
  · rintro ⟨x, ⟨i, rfl⟩, rfl⟩
    exact ⟨i, (Φ_pairRows H HA i).symm⟩

/-- **The dimension of a pair row space is the rank of the encoded matrix.** -/
theorem finrank_pairRowSpace_eq_rank {q : Type*} [Fintype q] {k : ℕ}
    (H : Matrix q (Fin k) K) (HA : Matrix q (Fin k) K) :
    finrank K ↥(Q1Paper.pairRowSpace H HA) = Matrix.rank (pairRows H HA) := by
  rw [pairRowSpace_eq_map_pairRows]
  rw [LinearEquiv.finrank_map_eq (Φ (K := K)) (Q1Subspace.rowSpace (pairRows H HA))]
  exact (Q1Subspace.rank_eq_finrank_rowSpace (pairRows H HA)).symm

/-- **Encoding commutes with complexification.** -/
theorem pairRows_map {q : Type*} {k : ℕ}
    (H : Matrix q (Fin k) ℝ) (HA : Matrix q (Fin k) ℝ) :
    pairRows (H.map (algebraMap ℝ ℂ)) (HA.map (algebraMap ℝ ℂ))
      = (pairRows H HA).map (algebraMap ℝ ℂ) := by
  ext i t
  refine Fin.addCases (motive := fun t =>
    pairRows (H.map (algebraMap ℝ ℂ)) (HA.map (algebraMap ℝ ℂ)) i t
      = (pairRows H HA).map (algebraMap ℝ ℂ) i t) ?_ ?_ t
  · intro j
    show Fin.addCases (fun j => (H.map (algebraMap ℝ ℂ)) i j)
        (fun j => (HA.map (algebraMap ℝ ℂ)) i j) (Fin.castAdd k j)
      = (algebraMap ℝ ℂ) (Fin.addCases (fun j => H i j) (fun j => HA i j) (Fin.castAdd k j))
    rw [Fin.addCases_left, Fin.addCases_left]
    rfl
  · intro j
    show Fin.addCases (fun j => (H.map (algebraMap ℝ ℂ)) i j)
        (fun j => (HA.map (algebraMap ℝ ℂ)) i j) (Fin.natAdd k j)
      = (algebraMap ℝ ℂ) (Fin.addCases (fun j => H i j) (fun j => HA i j) (Fin.natAdd k j))
    rw [Fin.addCases_right, Fin.addCases_right]
    rfl


/-- Multiplication commutes with the row encoding. -/
theorem mul_pairRows {q : Type*} [Fintype q] {n k : ℕ}
    (X : Matrix q (Fin n) K) (H : Matrix (Fin n) (Fin k) K) (HA : Matrix (Fin n) (Fin k) K) :
    X * pairRows H HA = pairRows (X * H) (X * HA) := by
  ext i t
  refine Fin.addCases (motive := fun t =>
    (X * pairRows H HA) i t = pairRows (X * H) (X * HA) i t) ?_ ?_ t
  · intro j
    rw [Matrix.mul_apply]
    rw [show pairRows (X * H) (X * HA) i (Fin.castAdd k j) = (X * H) i j from
      Fin.addCases_left j]
    rw [Matrix.mul_apply]
    refine Finset.sum_congr rfl (fun l _ => ?_)
    rw [show pairRows H HA l (Fin.castAdd k j) = H l j from Fin.addCases_left j]
  · intro j
    rw [Matrix.mul_apply]
    rw [show pairRows (X * H) (X * HA) i (Fin.natAdd k j) = (X * HA) i j from
      Fin.addCases_right j]
    rw [Matrix.mul_apply]
    refine Finset.sum_congr rfl (fun l _ => ?_)
    rw [show pairRows H HA l (Fin.natAdd k j) = HA l j from Fin.addCases_right j]


/-- **`W` is the `Φ`-image of the complexified real row space.** -/
theorem WR_eq_map_complex {r0 n k r : ℕ}
    (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (R : Matrix (Fin r) (Fin n) ℝ) :
    WR A (N.map (algebraMap ℝ ℂ)) L0 R
      = Submodule.map (Φ (K := ℂ)).toLinearMap
        (Q1Subspace.rowSpace
          ((Matrix.fromRows L0 R * pairRows N (A * N)).map (algebraMap ℝ ℂ))) := by
  have hL : Lc L0 R = (Matrix.fromRows L0 R).map (algebraMap ℝ ℂ) := by
    rw [← fromRows_Lc]
    exact Q1Paper.Thm5.fromRows_map_ofReal L0 R
  have hN : (N.map (algebraMap ℝ ℂ)) = (N.map (algebraMap ℝ ℂ)) := rfl
  have hA : Ac A * N.map (algebraMap ℝ ℂ) = (A * N).map (algebraMap ℝ ℂ) := by
    rw [Ac, Matrix.map_mul]
  have h1 : Lc L0 R * N.map (algebraMap ℝ ℂ)
      = ((Matrix.fromRows L0 R) * N).map (algebraMap ℝ ℂ) := by
    rw [hL]
    exact Matrix.map_mul.symm
  have h2 : Lc L0 R * (Ac A * N.map (algebraMap ℝ ℂ))
      = ((Matrix.fromRows L0 R) * (A * N)).map (algebraMap ℝ ℂ) := by
    rw [hA, hL]
    exact Matrix.map_mul.symm
  calc WR A (N.map (algebraMap ℝ ℂ)) L0 R
      = Submodule.map (Φ (K := ℂ)).toLinearMap
          (Q1Subspace.rowSpace (pairRows (Lc L0 R * N.map (algebraMap ℝ ℂ))
            (Lc L0 R * (Ac A * N.map (algebraMap ℝ ℂ))))) := by
        rw [WR, pairRowSpace_eq_map_pairRows]
    _ = Submodule.map (Φ (K := ℂ)).toLinearMap
          (Q1Subspace.rowSpace (pairRows (((Matrix.fromRows L0 R) * N).map (algebraMap ℝ ℂ))
            (((Matrix.fromRows L0 R) * (A * N)).map (algebraMap ℝ ℂ)))) := by
        rw [h1, h2]
    _ = Submodule.map (Φ (K := ℂ)).toLinearMap
          (Q1Subspace.rowSpace ((pairRows ((Matrix.fromRows L0 R) * N)
            ((Matrix.fromRows L0 R) * (A * N))).map (algebraMap ℝ ℂ))) := by
        rw [pairRows_map]
    _ = Submodule.map (Φ (K := ℂ)).toLinearMap
          (Q1Subspace.rowSpace
            ((Matrix.fromRows L0 R * pairRows N (A * N)).map (algebraMap ℝ ℂ))) := by
        rw [mul_pairRows]

/-- **The dimension identity for a real design**: `dim W = dim V`, `V` the real row
space. -/
theorem finrank_WR_eq {r0 n k r : ℕ}
    (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (R : Matrix (Fin r) (Fin n) ℝ) :
    finrank ℂ ↥(WR A (N.map (algebraMap ℝ ℂ)) L0 R)
      = finrank ℝ ↥(Q1Subspace.rowSpace (Matrix.fromRows L0 R * pairRows N (A * N))) := by
  rw [WR_eq_map_complex]
  rw [LinearEquiv.finrank_map_eq (Φ (K := ℂ) (k := k))
    (Q1Subspace.rowSpace ((Matrix.fromRows L0 R * pairRows N (A * N)).map (algebraMap ℝ ℂ)))]
  have h1 : finrank ℂ ↥(Q1Subspace.rowSpace
        ((Matrix.fromRows L0 R * pairRows N (A * N)).map (algebraMap ℝ ℂ)))
      = ((Matrix.fromRows L0 R * pairRows N (A * N)).map (algebraMap ℝ ℂ)).rank :=
    (Q1Subspace.rank_eq_finrank_rowSpace _).symm
  rw [h1]
  have h2 : ((Matrix.fromRows L0 R * pairRows N (A * N)).map (algebraMap ℝ ℂ)).rank
      = (Matrix.fromRows L0 R * pairRows N (A * N)).rank :=
    Q1Paper.PaperI.DecComplex.rank_map_ofReal_any _
  rw [h2]
  have h3 : (Matrix.fromRows L0 R * pairRows N (A * N)).rank
      = finrank ℝ ↥(Q1Subspace.rowSpace (Matrix.fromRows L0 R * pairRows N (A * N))) :=
    Q1Subspace.rank_eq_finrank_rowSpace _
  rw [h3]


/-- **The dimension identity for `W₀`.** -/
theorem finrank_W0_eq {r0 n k : ℕ}
    (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) :
    finrank ℂ ↥(W0 A (N.map (algebraMap ℝ ℂ)) L0)
      = finrank ℝ ↥(Q1Subspace.rowSpace (L0 * pairRows N (A * N))) := by
  have hL0c : L0c L0 = L0.map (algebraMap ℝ ℂ) := rfl
  have hA : Ac A * N.map (algebraMap ℝ ℂ) = (A * N).map (algebraMap ℝ ℂ) := by
    rw [Ac]
    exact Matrix.map_mul.symm
  have h1 : L0c L0 * N.map (algebraMap ℝ ℂ) = (L0 * N).map (algebraMap ℝ ℂ) := by
    rw [hL0c]
    exact Matrix.map_mul.symm
  have h2 : L0c L0 * (Ac A * N.map (algebraMap ℝ ℂ)) = (L0 * (A * N)).map (algebraMap ℝ ℂ) := by
    rw [hA, hL0c]
    exact Matrix.map_mul.symm
  rw [W0, pairRowSpace_eq_map_pairRows, h1, h2, pairRows_map]
  rw [← mul_pairRows]
  rw [LinearEquiv.finrank_map_eq (Φ (K := ℂ) (k := k)) _]
  have ha : finrank ℂ ↥(Q1Subspace.rowSpace
        ((L0 * pairRows N (A * N)).map (algebraMap ℝ ℂ)))
      = ((L0 * pairRows N (A * N)).map (algebraMap ℝ ℂ)).rank :=
    (Q1Subspace.rank_eq_finrank_rowSpace _).symm
  rw [ha]
  have hb : ((L0 * pairRows N (A * N)).map (algebraMap ℝ ℂ)).rank
      = (L0 * pairRows N (A * N)).rank :=
    Q1Paper.PaperI.DecComplex.rank_map_ofReal_any _
  rw [hb]
  exact Q1Subspace.rank_eq_finrank_rowSpace _



/-- The complexification map on function spaces. -/
noncomputable def phi (ι : Type*) : (ι → ℝ) →ₗ[ℝ] (ι → ℂ) where
  toFun f i := algebraMap ℝ ℂ (f i)
  map_add' f g := by ext i; simp
  map_smul' c f := by ext i; simp

/-- **Complexification of a row space.**  The row space of `M.map f` is the
`ℂ`-span of the complexified rows of `M`. -/
theorem rowSpace_map_complex {q : Type*} [Fintype q] {k : ℕ} (M : Matrix q (Fin k) ℝ) :
    Q1Subspace.rowSpace (M.map (algebraMap ℝ ℂ))
      = Submodule.span ℂ ((phi (Fin k)) '' (Q1Subspace.rowSpace M)) := by
  have hrange : Set.range (M.map (algebraMap ℝ ℂ))
      = (phi (Fin k)) '' (Set.range (fun i => M i)) := by
    ext x
    constructor
    · rintro ⟨i, rfl⟩
      exact ⟨M i, ⟨i, rfl⟩, rfl⟩
    · rintro ⟨y, ⟨i, rfl⟩, rfl⟩
      exact ⟨i, rfl⟩
  have hcomap : Q1Subspace.rowSpace M
      ≤ Submodule.comap (phi (Fin k))
        ((Submodule.span ℂ ((phi (Fin k)) '' (Set.range (fun i => M i)))).restrictScalars ℝ) := by
    rw [Q1Subspace.rowSpace, Submodule.span_le]
    intro s hs
    exact Submodule.mem_comap.mpr (Submodule.subset_span ⟨s, hs, rfl⟩)
  rw [Q1Subspace.rowSpace, Q1Subspace.rowSpace, hrange]
  apply le_antisymm
  · exact Submodule.span_mono (Set.image_mono (Submodule.subset_span))
  · rw [Submodule.span_le]
    intro x hx
    obtain ⟨y, hy, rfl⟩ := hx
    exact hcomap hy


/-- **The real-compression lemma.**  A feasible real design `R` whose pair row space
contains `W₀` can be re-realised by a real design `R'` with `t = dim (W/W₀)` rows,
giving the *same* `W`. -/
theorem real_compress {r0 n k r : ℕ}
    (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (R : Matrix (Fin r) (Fin n) ℝ)
    (hW0 : W0 A (N.map (algebraMap ℝ ℂ)) L0 ≤ WR A (N.map (algebraMap ℝ ℂ)) L0 R)
    (hfeas : IsFeasible (WR A (N.map (algebraMap ℝ ℂ)) L0 R)) :
    ∃ R' : Matrix (Fin (t (W0 A (N.map (algebraMap ℝ ℂ)) L0)
        (WR A (N.map (algebraMap ℝ ℂ)) L0 R))) (Fin n) ℝ,
      WR A (N.map (algebraMap ℝ ℂ)) L0 R' = WR A (N.map (algebraMap ℝ ℂ)) L0 R := by
  classical
  have hs := Q1Paper.claim4_sandwich (K := ℝ) L0 R (pairRows N (A * N))
  have hV0le : finrank ℝ ↥(Q1Subspace.rowSpace (L0 * pairRows N (A * N)))
      ≤ finrank ℝ ↥(Q1Subspace.rowSpace (Matrix.fromRows L0 R * pairRows N (A * N))) :=
    Submodule.finrank_mono hs.1
  have hdim : finrank ℝ ↥(Q1Subspace.rowSpace (Matrix.fromRows L0 R * pairRows N (A * N)))
      ≤ finrank ℝ ↥(Q1Subspace.rowSpace (L0 * pairRows N (A * N)))
        + t (W0 A (N.map (algebraMap ℝ ℂ)) L0) (WR A (N.map (algebraMap ℝ ℂ)) L0 R) := by
    have ht := t_eq_finrank_sub (K := ℂ) hW0
    rw [ht, finrank_WR_eq A N L0 R, finrank_W0_eq A N L0]
    omega
  obtain ⟨R', hR'⟩ := Q1Paper.claim4_converse (K := ℝ) L0 (pairRows N (A * N))
    (Q1Subspace.rowSpace (Matrix.fromRows L0 R * pairRows N (A * N))) hs.1 hs.2.1 hdim
  refine ⟨R', ?_⟩
  have e1 : WR A (N.map (algebraMap ℝ ℂ)) L0 R'
      = Submodule.map (Φ (K := ℂ)).toLinearMap
        (Q1Subspace.rowSpace
          ((Matrix.fromRows L0 R' * pairRows N (A * N)).map (algebraMap ℝ ℂ))) :=
    WR_eq_map_complex A N L0 R'
  have e2 : WR A (N.map (algebraMap ℝ ℂ)) L0 R
      = Submodule.map (Φ (K := ℂ)).toLinearMap
        (Q1Subspace.rowSpace
          ((Matrix.fromRows L0 R * pairRows N (A * N)).map (algebraMap ℝ ℂ))) :=
    WR_eq_map_complex A N L0 R
  have hm : Q1Subspace.rowSpace
        ((Matrix.fromRows L0 R' * pairRows N (A * N)).map (algebraMap ℝ ℂ))
      = Q1Subspace.rowSpace
        ((Matrix.fromRows L0 R * pairRows N (A * N)).map (algebraMap ℝ ℂ)) := by
    rw [rowSpace_map_complex, rowSpace_map_complex, hR']
  calc WR A (N.map (algebraMap ℝ ℂ)) L0 R'
      = Submodule.map (Φ (K := ℂ)).toLinearMap
          (Q1Subspace.rowSpace
            ((Matrix.fromRows L0 R' * pairRows N (A * N)).map (algebraMap ℝ ℂ))) := e1
    _ = Submodule.map (Φ (K := ℂ)).toLinearMap
          (Q1Subspace.rowSpace
            ((Matrix.fromRows L0 R * pairRows N (A * N)).map (algebraMap ℝ ℂ))) := by
        rw [hm]
    _ = WR A (N.map (algebraMap ℝ ℂ)) L0 R := e2.symm


/-- **The converse sandwich for real designs (`DECℂ`).**  A feasible real design `R`
with `W₀ ≤ W` gives `DECℂ` at order `t = dim (W/W₀)`: compress to `t` rows and
convert the compressed conditions into the raw ones of `DECℂ`. -/
theorem feasible_to_decC {p r0 n k : ℕ}
    (C : Matrix (Fin p) (Fin n) ℝ) (A : Matrix (Fin n) (Fin n) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℝ)
    (hN : (N.map (algebraMap ℝ ℂ)).mulVecLin.range
      = (Matrix.fromRows ((C.map (algebraMap ℝ ℂ)) * (A.map (algebraMap ℝ ℂ)))
          (C.map (algebraMap ℝ ℂ))).mulVecLin.ker)
    {r : ℕ} {R : Matrix (Fin r) (Fin n) ℝ}
    (hW0 : W0 A (N.map (algebraMap ℝ ℂ)) L0 ≤ WR A (N.map (algebraMap ℝ ℂ)) L0 R)
    (hfeas : IsFeasible (WR A (N.map (algebraMap ℝ ℂ)) L0 R)) :
    DecOrder C A L0 (t (W0 A (N.map (algebraMap ℝ ℂ)) L0)
      (WR A (N.map (algebraMap ℝ ℂ)) L0 R)) := by
  classical
  obtain ⟨R', hR'⟩ := real_compress A N L0 R hW0 hfeas
  have hfeas' : IsFeasible (WR A (N.map (algebraMap ℝ ℂ)) L0 R') := by
    rw [hR']
    exact hfeas
  have hpair : IsFeasible (Q1Paper.pairRowSpace
      (Lc L0 R' * (N.map (algebraMap ℝ ℂ)))
      (Lc L0 R' * (Ac A * N.map (algebraMap ℝ ℂ)))) := hfeas'
  have hcomp := (isFeasible_pairRowSpace_iff
    (Lc L0 R' * (N.map (algebraMap ℝ ℂ)))
    (Lc L0 R' * (Ac A * N.map (algebraMap ℝ ℂ)))).mp hpair
  have hLc : Lc L0 R' = (Matrix.fromRows L0 R').map (algebraMap ℝ ℂ) := by
    rw [← fromRows_Lc]
    exact Q1Paper.Thm5.fromRows_map_ofReal L0 R'
  refine ⟨R', ?_, ?_⟩
  · refine (PaperI.rawAlgebraic_iff_compressed (C.map (algebraMap ℝ ℂ))
      ((C.map (algebraMap ℝ ℂ)) * (A.map (algebraMap ℝ ℂ)))
      ((Matrix.fromRows L0 R').map (algebraMap ℝ ℂ))
      (((Matrix.fromRows L0 R').map (algebraMap ℝ ℂ)) * (A.map (algebraMap ℝ ℂ)))
      (N.map (algebraMap ℝ ℂ)) hN).mpr ?_
    have h := hcomp.1
    rw [hLc] at h
    rw [Matrix.mul_assoc]
    exact h
  · refine (PaperI.rawSpectral_iff_compressed (C.map (algebraMap ℝ ℂ))
      ((C.map (algebraMap ℝ ℂ)) * (A.map (algebraMap ℝ ℂ)))
      ((Matrix.fromRows L0 R').map (algebraMap ℝ ℂ))
      (((Matrix.fromRows L0 R').map (algebraMap ℝ ℂ)) * (A.map (algebraMap ℝ ℂ)))
      (N.map (algebraMap ℝ ℂ)) hN).mpr ?_
    have h := hcomp.2
    rw [hLc] at h
    rw [Matrix.mul_assoc]
    exact h


/-- **The forward sandwich, exposing the design.**  `DECℂ r` gives a real `R` whose
pair row space is feasible, sits between `W₀` and `T`, and has `t ≤ r`. -/
theorem decC_to_feasible_design {p r0 n k : ℕ}
    (C : Matrix (Fin p) (Fin n) ℝ) (A : Matrix (Fin n) (Fin n) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (hN : N.mulVecLin.range
      = (Matrix.fromRows ((C.map (algebraMap ℝ ℂ)) * (A.map (algebraMap ℝ ℂ)))
          (C.map (algebraMap ℝ ℂ))).mulVecLin.ker)
    {r : ℕ} (h : DecOrder C A L0 r) :
    ∃ R : Matrix (Fin r) (Fin n) ℝ,
      W0 A N L0 ≤ WR A N L0 R ∧ WR A N L0 R ≤ TR A N ∧
        IsFeasible (WR A N L0 R) ∧ t (W0 A N L0) (WR A N L0 R) ≤ r := by
  obtain ⟨R, h1, h2⟩ := (PaperI.DEC_complex_iff_compressed C A L0 r N hN).mp h
  have hs := Q1Paper.claim4_sandwich (K := ℂ) (L0c L0) (Rc R) (Mcol N (Ac A))
  have hW0W : W0 A N L0 ≤ WR A N L0 R := by
    rw [W0_eq_map, WR_eq_map]
    exact Submodule.map_mono hs.1
  have hWT : WR A N L0 R ≤ TR A N := by
    rw [WR_eq_map, TR_eq_map]
    exact Submodule.map_mono hs.2.1
  have hdim : finrank ℂ ↥(WR A N L0 R) ≤ finrank ℂ ↥(W0 A N L0) + r := by
    have h' := hs.2.2.1
    rw [Fintype.card_fin] at h'
    rw [WR_eq_map, W0_eq_map,
      LinearEquiv.finrank_map_eq (Φ (K := ℂ))
        (Q1Subspace.rowSpace (Matrix.fromRows (L0c L0) (Rc R) * Mcol N (Ac A))),
      LinearEquiv.finrank_map_eq (Φ (K := ℂ))
        (Q1Subspace.rowSpace (L0c L0 * Mcol N (Ac A)))]
    exact h'
  refine ⟨R, hW0W, hWT, ?_, ?_⟩
  · have h1' : PaperI.compressedAlgebraic (Lc L0 R * N) (Lc L0 R * (Ac A * N)) :=
      (Matrix.mul_assoc (Lc L0 R) (Ac A) N) ▸ h1
    have h2' : PaperI.compressedSpectral (Lc L0 R * N) (Lc L0 R * (Ac A * N)) :=
      (Matrix.mul_assoc (Lc L0 R) (Ac A) N) ▸ h2
    exact (isFeasible_pairRowSpace_iff (Lc L0 R * N) (Lc L0 R * (Ac A * N))).mpr
      ⟨h1', h2'⟩
  · rw [t_le_iff hW0W]
    exact hdim

/-- **Claim 5, saturation, real designs.**  `DECℂ r` is equivalent to `DECℂ` at the
saturation order `m = dim (T/W₀)`: every feasible real design compresses to `m` rows,
and `m ≤ r`. -/
theorem decC_saturates {p r0 n k : ℕ}
    (C : Matrix (Fin p) (Fin n) ℝ) (A : Matrix (Fin n) (Fin n) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℝ)
    (hN : (N.map (algebraMap ℝ ℂ)).mulVecLin.range
      = (Matrix.fromRows ((C.map (algebraMap ℝ ℂ)) * (A.map (algebraMap ℝ ℂ)))
          (C.map (algebraMap ℝ ℂ))).mulVecLin.ker)
    {r : ℕ} (h : t (W0 A (N.map (algebraMap ℝ ℂ)) L0) (TR A (N.map (algebraMap ℝ ℂ))) ≤ r)
    (hr : DecOrder C A L0 r) :
    DecOrder C A L0 (t (W0 A (N.map (algebraMap ℝ ℂ)) L0) (TR A (N.map (algebraMap ℝ ℂ)))) := by
  obtain ⟨R, hW0, hWT, hf, _ht⟩ :=
    decC_to_feasible_design C A L0 (N.map (algebraMap ℝ ℂ)) hN hr
  have hmono : t (W0 A (N.map (algebraMap ℝ ℂ)) L0) (WR A (N.map (algebraMap ℝ ℂ)) L0 R)
      ≤ t (W0 A (N.map (algebraMap ℝ ℂ)) L0) (TR A (N.map (algebraMap ℝ ℂ))) :=
    t_le_t_of_le hW0 hWT
  refine decC_mono (C := C) (A := A) (L0 := L0) (N := N.map (algebraMap ℝ ℂ)) (r := t (W0 A (N.map (algebraMap ℝ ℂ)) L0) (WR A (N.map (algebraMap ℝ ℂ)) L0 R)) (r' := t (W0 A (N.map (algebraMap ℝ ℂ)) L0) (TR A (N.map (algebraMap ℝ ℂ)))) hN hmono ?_
  exact feasible_to_decC (C := C) (A := A) (L0 := L0) (N := N) (R := R) hN hW0 hf


/-! ### The minimum order for real designs -/

/-- The possible quotient dimensions of feasible **real** designs. -/
def tMinCSet (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) : Set ℕ :=
  {m | ∃ (r : ℕ) (R : Matrix (Fin r) (Fin n) ℝ),
      W0 A (N.map (algebraMap ℝ ℂ)) L0 ≤ WR A (N.map (algebraMap ℝ ℂ)) L0 R ∧
      IsFeasible (WR A (N.map (algebraMap ℝ ℂ)) L0 R) ∧
      t (W0 A (N.map (algebraMap ℝ ℂ)) L0) (WR A (N.map (algebraMap ℝ ℂ)) L0 R) = m}

/-- The minimum quotient dimension over real designs (`⊤` when there is none). -/
noncomputable def tMinC (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) : WithTop ℕ := by
  classical
  exact if h : (tMinCSet A N L0).Nonempty then ↑(sInf (tMinCSet A N L0)) else ⊤

/-- **The minimum order for real designs**: `t_min ≤ r ↔ DECℂ r`. -/
theorem tMinC_le_iff_decC {p r0 n k : ℕ}
    (C : Matrix (Fin p) (Fin n) ℝ) (A : Matrix (Fin n) (Fin n) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℝ)
    (hN : (N.map (algebraMap ℝ ℂ)).mulVecLin.range
      = (Matrix.fromRows ((C.map (algebraMap ℝ ℂ)) * (A.map (algebraMap ℝ ℂ)))
          (C.map (algebraMap ℝ ℂ))).mulVecLin.ker)
    (r : ℕ) :
    tMinC A N L0 ≤ (r : WithTop ℕ) ↔ DecOrder C A L0 r := by
  classical
  constructor
  · intro hle
    by_cases hne : (tMinCSet A N L0).Nonempty
    · rw [tMinC, dif_pos hne] at hle
      have hle' : sInf (tMinCSet A N L0) ≤ r := WithTop.coe_le_coe.mp hle
      obtain ⟨rr, R, hW0, hf, ht⟩ := Nat.sInf_mem hne
      have htle : t (W0 A (N.map (algebraMap ℝ ℂ)) L0)
          (WR A (N.map (algebraMap ℝ ℂ)) L0 R) ≤ r := by
        rw [ht]
        exact hle'
      refine decC_mono (C := C) (A := A) (L0 := L0) (N := N.map (algebraMap ℝ ℂ))
        (r := t (W0 A (N.map (algebraMap ℝ ℂ)) L0)
          (WR A (N.map (algebraMap ℝ ℂ)) L0 R)) (r' := r) hN htle ?_
      exact feasible_to_decC (C := C) (A := A) (L0 := L0) (N := N) (R := R) hN hW0 hf
    · rw [tMinC, dif_neg hne] at hle
      exact absurd hle (WithTop.not_top_le_coe r)
  · intro hr
    obtain ⟨R, hW0, _hWT, hf, ht⟩ :=
      decC_to_feasible_design C A L0 (N.map (algebraMap ℝ ℂ)) hN hr
    have hmem : t (W0 A (N.map (algebraMap ℝ ℂ)) L0)
        (WR A (N.map (algebraMap ℝ ℂ)) L0 R) ∈ tMinCSet A N L0 :=
      ⟨_, R, hW0, hf, rfl⟩
    have hne : (tMinCSet A N L0).Nonempty := ⟨_, hmem⟩
    have hle : sInf (tMinCSet A N L0)
        ≤ t (W0 A (N.map (algebraMap ℝ ℂ)) L0) (WR A (N.map (algebraMap ℝ ℂ)) L0 R) :=
      Nat.sInf_le hmem
    rw [tMinC, dif_pos hne]
    exact WithTop.coe_le_coe.mpr (le_trans hle ht)


/-- **The least feasible real order is itself feasible.** -/
theorem decC_sInf_tMinCSet {p r0 n k : ℕ}
    (C : Matrix (Fin p) (Fin n) ℝ) (A : Matrix (Fin n) (Fin n) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℝ)
    (hN : (N.map (algebraMap ℝ ℂ)).mulVecLin.range
      = (Matrix.fromRows ((C.map (algebraMap ℝ ℂ)) * (A.map (algebraMap ℝ ℂ)))
          (C.map (algebraMap ℝ ℂ))).mulVecLin.ker)
    (hne : (tMinCSet A N L0).Nonempty) :
    DecOrder C A L0 (sInf (tMinCSet A N L0)) := by
  refine (tMinC_le_iff_decC C A L0 N hN (sInf (tMinCSet A N L0))).mp ?_
  rw [tMinC, dif_pos hne]


/-- **`t_min ≤ 2ℓ` for real designs.**  Every feasible real design has `W ≤ T` and
quotient dimension `≤ 2ℓ`, so the minimum over real designs obeys the bound. -/
theorem tMinC_le_two_ell
    (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ)
    (hne : (tMinCSet A N L0).Nonempty) :
    tMinC A N L0 ≤ ((2 * ell A (N.map (algebraMap ℝ ℂ)) : ℕ) : WithTop ℕ) := by
  rw [tMinC, dif_pos hne]
  refine WithTop.coe_le_coe.mpr ?_
  have hmem : sInf (tMinCSet A N L0) ∈ tMinCSet A N L0 := Nat.sInf_mem hne
  obtain ⟨r, R, hW0, hf, ht⟩ := hmem
  rw [← ht]
  have hWT : WR A (N.map (algebraMap ℝ ℂ)) L0 R ≤ TR A (N.map (algebraMap ℝ ℂ)) := by
    rw [WR_eq_map, TR_eq_map]
    exact Submodule.map_mono
      (Q1Paper.rowSpace_mul_le (Matrix.fromRows (L0c L0) (Rc R)) (Mcol (N.map (algebraMap ℝ ℂ)) (Ac A)))
  exact t_le_two_ell A (N.map (algebraMap ℝ ℂ)) L0 hW0 hWT hf


/-- **The complexification of a real subspace** of `Fin k → ℝ`. -/
noncomputable def UC {k : ℕ} (U : Submodule ℝ (Fin k → ℝ)) : Submodule ℂ (Fin k → ℂ) :=
  Submodule.span ℂ ((phi (Fin k)) '' (U : Set (Fin k → ℝ)))

/-- **Complexification preserves the dimension.**  Every submodule of `Fin k → ℝ` is the
row space of a matrix, so this reduces to `rowSpace_map_complex` and
`rank_map_ofReal`. -/
theorem finrank_UC {k : ℕ} (U : Submodule ℝ (Fin k → ℝ)) :
    finrank ℂ ↥(UC U) = finrank ℝ ↥U := by
  classical
  let d := finrank ℝ ↥U
  let B : Basis (Fin d) ℝ ↥U := Module.finBasis ℝ ↥U
  let M : Matrix (Fin d) (Fin k) ℝ := fun i => (B i : Fin k → ℝ)
  have hM : Q1Subspace.rowSpace M = U := by
    apply le_antisymm
    · rw [Q1Subspace.rowSpace, Submodule.span_le]
      rintro _ ⟨i, rfl⟩
      exact (B i).2
    · intro x hx
      have hrepr := B.sum_repr (⟨x, hx⟩ : ↥U)
      have hco := congrArg (fun y : ↥U => (y : Fin k → ℝ)) hrepr
      simp only [Submodule.coe_sum, Submodule.coe_smul, Finset.sum_apply,
        Pi.smul_apply, smul_eq_mul] at hco
      rw [show x = ∑ i, (B.repr ⟨x, hx⟩) i • (B i : Fin k → ℝ) from hco.symm]
      refine Submodule.sum_mem _ (fun i _ => ?_)
      exact Submodule.smul_mem _ _ (Submodule.subset_span ⟨i, rfl⟩)
  have hUC : UC U = Q1Subspace.rowSpace (M.map (algebraMap ℝ ℂ)) := by
    have h := rowSpace_map_complex M
    rw [hM] at h
    exact h.symm
  rw [hUC]
  rw [← Q1Subspace.rank_eq_finrank_rowSpace (M.map (algebraMap ℝ ℂ))]
  rw [Q1Paper.PaperI.DecComplex.rank_map_ofReal_any M]
  rw [Q1Subspace.rank_eq_finrank_rowSpace M, hM]


/-- `WR` of any real design lies in `TR` (so the real designs are a subset of the
feasible complex `W`). -/
theorem WR_le_TR (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (r : ℕ) (R : Matrix (Fin r) (Fin n) ℝ) :
    WR A (N.map (algebraMap ℝ ℂ)) L0 R ≤ TR A (N.map (algebraMap ℝ ℂ)) := by
  rw [WR_eq_map, TR_eq_map]
  exact Submodule.map_mono
    (Q1Paper.rowSpace_mul_le (Matrix.fromRows (L0c L0) (Rc R)) (Mcol (N.map (algebraMap ℝ ℂ)) (Ac A)))

/-- **The complex-domain minimum is the smaller one**: real designs are among the
feasible complex `W`, so `t_min ≤ t_min^ℝ`. -/
theorem tMin_le_tMinC (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) :
    tMin A (N.map (algebraMap ℝ ℂ)) L0 ≤ tMinC A N L0 := by
  classical
  by_cases hne : (tMinCSet A N L0).Nonempty
  · rw [tMinC, dif_pos hne]
    obtain ⟨r, R, hW0, hf, ht⟩ := Nat.sInf_mem hne
    have hWT := WR_le_TR A N L0 r R
    have hle : tMin A (N.map (algebraMap ℝ ℂ)) L0
        ≤ ((t (W0 A (N.map (algebraMap ℝ ℂ)) L0)
            (WR A (N.map (algebraMap ℝ ℂ)) L0 R) : ℕ) : WithTop ℕ) :=
      tMin_le_of_feasible A (N.map (algebraMap ℝ ℂ)) L0 hW0 hWT hf
    rw [← ht]
    exact hle
  · rw [tMinC, dif_neg hne]
    exact le_top

/-- **Prop 1's `qmin-lb` for real designs**: `a + 1 − s₀ ≤ t_min^ℝ`. -/
theorem le_tMinC_of_lowerBound
    (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ)
    (hω : ∀ V : Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ)),
      W0 A (N.map (algebraMap ℝ ℂ)) L0 ≤ V → V ≤ TR A (N.map (algebraMap ℝ ℂ))
        → IsFeasible V → 0 < finrank ℂ ↥(Q1Subspace.pi1 V)) :
    ((finrank ℂ ↥(Q1Subspace.pi1 (W0 A (N.map (algebraMap ℝ ℂ)) L0)
        ⊔ Q1Subspace.pi2 (W0 A (N.map (algebraMap ℝ ℂ)) L0)) + 1
        - finrank ℂ ↥(W0 A (N.map (algebraMap ℝ ℂ)) L0) : ℕ) : WithTop ℕ)
      ≤ tMinC A N L0 :=
  le_trans (le_tMin_of_lowerBound_max A (N.map (algebraMap ℝ ℂ)) L0 hω)
    (tMin_le_tMinC A N L0)

end Q1Paper.PaperII









