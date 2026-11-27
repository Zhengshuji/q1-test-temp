/-
Q1Paper/PaperII/LowerBound.lean

Paper II, Proposition `prop:lowerbound`, the spectral lower bound:
`a + 1 ≤ s₀ + t`, where `a = rank[U₀;V₀] = dim (π₁ W₀ ⊔ π₂ W₀)`, `s₀ = dim W₀` and
`t = dim (W/W₀)`.

Two independent inputs:
* `a ≤ ω` — the algebraic side (`finrank_sup_pi_le`: both projections of `W₀` land
  in `π₁ W`, hence the span of the two has dimension at most `ω = dim π₁ W`);
* `ω + 1 ≤ dim W` — the spectral side (`claim6_struct`, from `BoundLower`),
  available over an algebraically closed field and for `ω > 0`.

Paper's `ω ≤ s₀ + t − 1` presumes `ω ≥ 1` (at `ω = 0` feasibility forces `W = 0`),
so the hypothesis `0 < ω` is carried explicitly; the natural-number statement is
`a + 1 ≤ s₀ + t`, and the subtraction form `a − s₀ + 1 ≤ t` is derived under
`s₀ ≤ a`, where it is literally the paper's inequality.

Contents.
* `finrank_sup_pi_le` — `rank[U₀;V₀] ≤ ω`.
* `finrank_pi1_mono` — `dim U₀ ≤ ω`.
* `lowerBound_core` — `a + 1 ≤ s₀ + t`.
* `lowerBound_sub` — `a − s₀ + 1 ≤ t` for `s₀ ≤ a`.

Reuses: `Q1Subspace.pi1/pi2`, `Q1Paper.claim6_struct`,
`Q1Subspace.finrank_add_one_le_of_spectral` (`BoundLower.lean`), `t_eq_finrank_sub`
(`PaperII/Interface.lean`).
-/

import Q1Paper.PaperII.Sandwich

open Module Matrix

namespace Q1Paper.PaperII

variable {K : Type*} [Field K] {F : Type*} [AddCommGroup F] [Module K F]

/-- **`rank[U₀;V₀] ≤ ω`.**  Both projections of `W₀` land in `π₁ W`, so the span of
the two has dimension at most `dim π₁ W`. -/
theorem finrank_sup_pi_le [FiniteDimensional K F] {W₀ W : Submodule K (F × F)}
    (h : W₀ ≤ W) (hle : Q1Subspace.pi2 W ≤ Q1Subspace.pi1 W) :
    finrank K ↥(Q1Subspace.pi1 W₀ ⊔ Q1Subspace.pi2 W₀)
      ≤ finrank K ↥(Q1Subspace.pi1 W) := by
  have h₁ : Q1Subspace.pi1 W₀ ≤ Q1Subspace.pi1 W := Submodule.map_mono h
  have h₂ : Q1Subspace.pi2 W₀ ≤ Q1Subspace.pi1 W :=
    (Submodule.map_mono h).trans hle
  exact Submodule.finrank_mono (sup_le h₁ h₂)

/-- **`dim U₀ ≤ ω`**: monotonicity of the first projection. -/
theorem finrank_pi1_mono [FiniteDimensional K F] {W₀ W : Submodule K (F × F)}
    (h : W₀ ≤ W) :
    finrank K ↥(Q1Subspace.pi1 W₀) ≤ finrank K ↥(Q1Subspace.pi1 W) :=
  Submodule.finrank_mono (Submodule.map_mono h)

/-- **Paper II, Proposition 2 (the dimension chain).**  For a feasible `W` with
`W₀ ≤ W` and `ω = dim (π₁ W) > 0`, `a + 1 ≤ s₀ + t`. -/
theorem lowerBound_core [FiniteDimensional K F] [IsAlgClosed K]
    {W₀ W : Submodule K (F × F)} (hW₀ : W₀ ≤ W)
    (hfeas : IsFeasible W) (hω : 0 < finrank K ↥(Q1Subspace.pi1 W)) :
    finrank K ↥(Q1Subspace.pi1 W₀ ⊔ Q1Subspace.pi2 W₀) + 1
      ≤ finrank K ↥W₀ + t W₀ W := by
  have hle : Q1Subspace.pi2 W ≤ Q1Subspace.pi1 W := hfeas.1
  have hspec : ∀ lam : K,
      finrank K ↥(Q1Subspace.piLam lam W) = finrank K ↥(Q1Subspace.pi1 W) := hfeas.2
  have ha : finrank K ↥(Q1Subspace.pi1 W₀ ⊔ Q1Subspace.pi2 W₀)
      ≤ finrank K ↥(Q1Subspace.pi1 W) := finrank_sup_pi_le hW₀ hle
  have hb : finrank K ↥(Q1Subspace.pi1 W) + 1 ≤ finrank K ↥W :=
    (Q1Paper.claim6_struct hle hω hspec).1
  have ht : t W₀ W = finrank K ↥W - finrank K ↥W₀ := t_eq_finrank_sub hW₀
  have hmono : finrank K ↥W₀ ≤ finrank K ↥W := Submodule.finrank_mono hW₀
  rw [ht]
  omega

/-- **Paper II, Proposition 2, subtraction form**: when `s₀ ≤ a`, the paper's
`a − s₀ + 1 ≤ t`. -/
theorem lowerBound_sub [FiniteDimensional K F] [IsAlgClosed K]
    {W₀ W : Submodule K (F × F)} (hW₀ : W₀ ≤ W)
    (hfeas : IsFeasible W) (hω : 0 < finrank K ↥(Q1Subspace.pi1 W))
    (hs₀ : finrank K ↥W₀ ≤ finrank K ↥(Q1Subspace.pi1 W₀ ⊔ Q1Subspace.pi2 W₀)) :
    finrank K ↥(Q1Subspace.pi1 W₀ ⊔ Q1Subspace.pi2 W₀) - finrank K ↥W₀ + 1
      ≤ t W₀ W := by
  have h := lowerBound_core hW₀ hfeas hω
  omega

/-! ### 4. The numerical half of tightness (Prop 3) -/

/-- **Prop 3, numerical half.**  Let `a = rank[U₀;V₀] = dim (π₁W₀ ⊔ π₂W₀)` and
`s₀ = dim W₀`.  If a feasible `W` has `dim W = a + 1` then its quotient dimension is
`a − s₀ + 1`: the spectral lower bound is attained.

The other half of Prop 3 — producing such a `W` from a pair `(G, b)` with
`W₀ ⊆ W(G,b) ⊆ T` — is not formalised. -/
theorem t_eq_of_finrank (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ)
    {W : Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ))} (hW0 : W0 A N L0 ≤ W)
    (ha : finrank ℂ ↥(W0 A N L0)
      ≤ finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)))
    (hdim : finrank ℂ ↥W
      = finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) + 1) :
    t (W0 A N L0) W
      = finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0))
        - finrank ℂ ↥(W0 A N L0) + 1 := by
  rw [t_eq_finrank_sub hW0]
  have hmono : finrank ℂ ↥(W0 A N L0) ≤ finrank ℂ ↥W := Submodule.finrank_mono hW0
  omega

end Q1Paper.PaperII
