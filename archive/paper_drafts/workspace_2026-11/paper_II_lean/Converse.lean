/-
Q1Paper/PaperII/Converse.lean

Paper II's sandwich, converse direction, for the complex-design predicate
`PaperI.DEC` over `ℂ` (Paper I's field-generic predicate).

**Scope.**  Paper II's paper works with real observers (`DECℂ`).  The converse for
`DECℂ` needs a *real compression* lemma: a feasible `W` coming from a real design
must be re-realized by a real design with `t = dim (W/W₀)` rows.  That argument is
not in this file; here the free block is allowed to be complex, so that Paper I's
`claim4_converse` applies directly through the column split `Φ`.  The real-design
refinement is tracked in `workspace/paper_split/PAPER_II_LEAN_PLAN.md` §8.5.

Contents.
* `WRc` — the pair row space `row[L N  L A N]` for a complex free block.
* `WRc_eq_map` — it is the `Φ`-image of `row([L₀;R] [N AN])`.
* `map_symm_map` — `Φ` and `Φ.symm` cancel on submodules.
* `feasible_to_DEC` — a feasible `W` with `W₀ ≤ W ≤ T` and `t ≤ r` gives `DEC r`
  (complex designs).

Reuses: `Q1Paper.claim4_converse` (`PaperI/S02_Subspace/Claim4Converse.lean`),
`PaperI.DEC_iff_compressed`, `map_rowSpace_Mcol`, `W0_eq_map`, `TR_eq_map`,
`isFeasible_pairRowSpace_iff`, `t_le_iff`.
-/

import Q1Paper.PaperII.Sandwich

open Module Matrix

namespace Q1Paper.PaperII

variable {p r0 n k : ℕ}

/-! ### 1. The pair row space of a complex design -/

/-- `W = row[L N  L A N]` for a complex free block `R`. -/
noncomputable def WRc (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (R : Matrix (Fin r) (Fin n) ℂ) :
    Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ)) :=
  Q1Paper.pairRowSpace (Matrix.fromRows (L0c L0) R * N)
    (Matrix.fromRows (L0c L0) R * (Ac A * N))

/-- `W` is the `Φ`-image of `row([L₀;R] [N AN])`. -/
theorem WRc_eq_map (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (R : Matrix (Fin r) (Fin n) ℂ) :
    WRc A N L0 R = Submodule.map (Φ (K := ℂ)).toLinearMap
      (Q1Subspace.rowSpace (Matrix.fromRows (L0c L0) R * Mcol N (Ac A))) := by
  rw [WRc, map_rowSpace_Mcol (K := ℂ) N (Ac A) (Fin r0 ⊕ Fin r)
    (Matrix.fromRows (L0c L0) R)]

/-! ### 2. `Φ` and `Φ.symm` cancel on submodules -/

/-- `Φ` after `Φ.symm` is the identity on submodules. -/
theorem map_symm_map (p : Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ))) :
    Submodule.map (Φ (K := ℂ) (k := k)).toLinearMap
      (Submodule.map (Φ (K := ℂ) (k := k)).symm.toLinearMap p) = p := by
  apply le_antisymm
  · rintro y ⟨x, hx, rfl⟩
    obtain ⟨z, hz, rfl⟩ := Submodule.mem_map.mp hx
    simpa using hz
  · intro y hy
    refine Submodule.mem_map.mpr ⟨(Φ (K := ℂ) (k := k)).symm y, ?_, ?_⟩
    · exact Submodule.mem_map.mpr ⟨y, hy, rfl⟩
    · exact LinearEquiv.apply_symm_apply _ _

/-! ### 3. The converse -/

/-- **Sandwich, converse (complex designs).**  A feasible `W` with `W₀ ≤ W ≤ T` and
`t = dim (W/W₀) ≤ r` is realized by a free block `R` of `r` rows: `DEC r` holds
for the field-generic predicate over `ℂ`. -/
theorem feasible_to_DEC
    (C : Matrix (Fin p) (Fin n) ℂ) (A : Matrix (Fin n) (Fin n) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (hN : N.mulVecLin.range = (Matrix.fromRows (C * Ac A) C).mulVecLin.ker)
    {r : ℕ} {W : Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ))}
    (hW0 : W0 A N L0 ≤ W) (hWT : W ≤ TR A N) (hfeas : IsFeasible W)
    (ht : t (W0 A N L0) W ≤ r) :
    PaperI.DEC C (Ac A) (L0c L0) r := by
  classical
  -- the preimage of `W` under the column split
  set V : Submodule ℂ ((Fin (k + k)) → ℂ) :=
    Submodule.map (Φ (K := ℂ)).symm.toLinearMap W with hV
  have hVmap : Submodule.map (Φ (K := ℂ)).toLinearMap V = W := by
    rw [hV]
    exact map_symm_map W
  -- the sandwich inequalities, transported
  have hV0 : Q1Subspace.rowSpace (L0c L0 * Mcol N (Ac A)) ≤ V := by
    intro x hx
    rw [hV]
    refine Submodule.mem_map.mpr ⟨Φ (K := ℂ) x, ?_, ?_⟩
    · have hx' : Φ (K := ℂ) x ∈ W0 A N L0 := by
        rw [W0_eq_map]
        exact Submodule.mem_map.mpr ⟨x, hx, rfl⟩
      exact hW0 hx'
    · simp
  have hVT : V ≤ Q1Subspace.rowSpace (Mcol N (Ac A)) := by
    intro x hx
    rw [hV] at hx
    obtain ⟨y, hyW, rfl⟩ := Submodule.mem_map.mp hx
    have hyT : y ∈ TR A N := hWT hyW
    rw [TR_eq_map] at hyT
    obtain ⟨z, hz, hzy⟩ := Submodule.mem_map.mp hyT
    rw [← hzy]
    simpa using hz
  have hdim : finrank ℂ ↥V
      ≤ finrank ℂ ↥(Q1Subspace.rowSpace (L0c L0 * Mcol N (Ac A))) + r := by
    have hdimW : finrank ℂ ↥W ≤ finrank ℂ ↥(W0 A N L0) + r :=
      (t_le_iff hW0).mp ht
    have hVW : finrank ℂ ↥V = finrank ℂ ↥W := by
      rw [hV]
      exact LinearEquiv.finrank_map_eq _ _
    have hW0r : finrank ℂ ↥(W0 A N L0)
        = finrank ℂ ↥(Q1Subspace.rowSpace (L0c L0 * Mcol N (Ac A))) := by
      rw [W0_eq_map]
      exact LinearEquiv.finrank_map_eq _ _
    omega
  -- Claim 4's converse, over ℂ
  obtain ⟨R, hRV⟩ := Q1Paper.claim4_converse (K := ℂ) (L0c L0) (Mcol N (Ac A)) V hV0 hVT hdim
  -- the two descriptions of `W` agree
  have hW_eq : WRc A N L0 R = W := by
    rw [WRc_eq_map, hRV, hVmap]
  -- feasibility, transferred
  have hfeas' : IsFeasible (Q1Paper.pairRowSpace
      (Matrix.fromRows (L0c L0) R * N) (Matrix.fromRows (L0c L0) R * (Ac A * N))) := by
    rw [show Q1Paper.pairRowSpace (Matrix.fromRows (L0c L0) R * N)
          (Matrix.fromRows (L0c L0) R * (Ac A * N)) = WRc A N L0 R from rfl, hW_eq]
    exact hfeas
  refine (PaperI.DEC_iff_compressed C (Ac A) (L0c L0) r N hN).mpr ⟨R, ?_, ?_⟩
  · have := (isFeasible_pairRowSpace_iff
      (Matrix.fromRows (L0c L0) R * N) (Matrix.fromRows (L0c L0) R * (Ac A * N))).mp hfeas'
    rw [Matrix.mul_assoc]
    exact this.1
  · have := (isFeasible_pairRowSpace_iff
      (Matrix.fromRows (L0c L0) R * N) (Matrix.fromRows (L0c L0) R * (Ac A * N))).mp hfeas'
    rw [Matrix.mul_assoc]
    exact this.2

end Q1Paper.PaperII
