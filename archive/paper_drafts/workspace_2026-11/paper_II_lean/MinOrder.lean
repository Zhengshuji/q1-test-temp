/-
Q1Paper/PaperII/MinOrder.lean

Paper II, Proposition `prop:minorder` (minimum order): `q_min = r₀ + t_min`, with
`t_min = min { dim (W/W₀) : W feasible }`, and the a priori bound `t_min ≤ 2ℓ`,
`ℓ = rank(A N)`.

The paper's `q_min = r₀ + t_min` is formalised as the equivalence
`t_min ≤ r ↔ DEC (r₀ + r)`: the minimum number of free rows is the minimum
quotient dimension.  `t_min` is `WithTop ℕ`, with `⊤` meaning "no feasible design"
(the paper's `+∞`).

Scope: the `DEC` here is the field-generic predicate over `ℂ` (complex free
blocks), matching `Saturate.lean`; the real-design specification `DECℂ` needs the
real-compression lemma (see `Converse.lean` and the plan §8.5).

Contents.
* `tMinSet` — `{ dim (W/W₀) : W feasible, W₀ ≤ W ≤ T }`.
* `tMin` — its infimum in `WithTop ℕ`.
* `tMin_le_iff_dec` — `t_min ≤ r ↔ DEC (r₀ + r)`.
* `ell` — the paper's `ℓ = dim row(A N)`.
* `omega_le_ell` — for a feasible `W`, `ω = dim π₁ W ≤ ℓ`.
* `t_le_two_ell` — every feasible `W` has `t ≤ 2ℓ` (Prop 1's bound).
* `tMin_le_two_ell` — `t_min ≤ 2ℓ` when a feasible `W` exists.

Reuses: `DEC_to_feasible_c`, `feasible_to_DEC` (`Saturate.lean`, `Converse.lean`),
`Q1Subspace.finrank_le_pi1_add_pi2`, `pi1_eq_pi2_of_spectral`,
`pi2_pairRowSpace`, `rowSpace_mul_le`, `Nat.sInf_mem`, `Nat.sInf_le`.
-/

import Q1Paper.PaperII.Saturate
import Q1Paper.PaperII.LowerBound

open Module Matrix

namespace Q1Paper.PaperII

variable {p r0 n k : ℕ}

/-! ### 1. The set of quotient dimensions and its infimum -/

/-- **`{ dim (W/W₀) : W feasible, W₀ ≤ W ≤ T }`**, the set whose minimum is the
paper's `t_min`. -/
def tMinSet (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) : Set ℕ :=
  {m | ∃ V : Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ)),
    W0 A N L0 ≤ V ∧ V ≤ TR A N ∧ IsFeasible V ∧ t (W0 A N L0) V = m}

/-- **The paper's `t_min`**, as `WithTop ℕ`: the infimum of the quotient dimensions,
and `⊤` when no feasible subspace exists (the paper's `+∞`). -/
noncomputable def tMin (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) : WithTop ℕ := by
  classical
  exact if h : (tMinSet A N L0).Nonempty then ↑(sInf (tMinSet A N L0)) else ⊤

/-! ### 2. `q_min = r₀ + t_min` -/

/-- **Minimum order: `t_min ≤ r ↔ DEC (r₀ + r)`.**  The least number of free rows
equals the least quotient dimension of a feasible subspace. -/
theorem tMin_le_iff_dec
    (C : Matrix (Fin p) (Fin n) ℂ) (A : Matrix (Fin n) (Fin n) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (hN : N.mulVecLin.range = (Matrix.fromRows (C * Ac A) C).mulVecLin.ker)
    (r : ℕ) :
    tMin A N L0 ≤ (r : WithTop ℕ) ↔ PaperI.DEC C (Ac A) (L0c L0) r := by
  constructor
  · intro hle
    by_cases h : (tMinSet A N L0).Nonempty
    · rw [tMin, dif_pos h] at hle
      have hle' : sInf (tMinSet A N L0) ≤ r := WithTop.coe_le_coe.mp hle
      obtain ⟨V, hV0, hVT, hVf, hVt⟩ := Nat.sInf_mem h
      exact feasible_to_DEC C A L0 N hN hV0 hVT hVf (by rw [hVt]; exact hle')
    · rw [tMin, dif_neg h] at hle
      exact absurd hle (WithTop.not_top_le_coe r)
  · intro hdec
    obtain ⟨V, hV0, hVT, hVf, hVt⟩ := DEC_to_feasible_c C A L0 N hN hdec
    have hne : (tMinSet A N L0).Nonempty := ⟨_, V, hV0, hVT, hVf, rfl⟩
    have hle : sInf (tMinSet A N L0) ≤ r :=
      le_trans (Nat.sInf_le ⟨V, hV0, hVT, hVf, rfl⟩) hVt
    rw [tMin, dif_pos hne]
    exact WithTop.coe_le_coe.mpr hle

/-! ### 3. The bound `t_min ≤ 2ℓ` -/

/-- **`ℓ = rank(A N)`**, the paper's parameter (`ℓ ≤ k`). -/
noncomputable def ell (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ) : ℕ :=
  finrank ℂ ↥(Q1Subspace.rowSpace (Ac A * N))

/-- For a feasible `W`, `ω = dim π₁ W ≤ ℓ`.  `W ≤ T` forces `π₂ W ≤ row(A N)`, and
feasibility forces `π₁ W = π₂ W`. -/
theorem omega_le_ell (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    {V : Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ))}
    (hVT : V ≤ TR A N) (hVf : IsFeasible V) :
    finrank ℂ ↥(Q1Subspace.pi1 V) ≤ ell A N := by
  have hpi2map : Submodule.map (LinearMap.snd ℂ (Fin k → ℂ) (Fin k → ℂ)) (TR A N)
      = Q1Subspace.rowSpace (Ac A * N) := by
    rw [show TR A N = Q1Paper.pairRowSpace N (Ac A * N) from rfl]
    exact Q1Paper.pi2_pairRowSpace N (Ac A * N)
  have hpi2 : Q1Subspace.pi2 V ≤ Q1Subspace.rowSpace (Ac A * N) := by
    have h := Submodule.map_mono (f := LinearMap.snd ℂ (Fin k → ℂ) (Fin k → ℂ)) hVT
    rw [hpi2map] at h
    exact h
  have heq : Q1Subspace.pi1 V = Q1Subspace.pi2 V :=
    Q1Subspace.pi1_eq_pi2_of_spectral hVf.1 (hVf.2 0)
  rw [heq, ell]
  exact Submodule.finrank_mono hpi2

/-- **`t ≤ 2ℓ`** for every feasible `W`: `dim W ≤ 2ω ≤ 2ℓ` (the unconditional half
of the structural bound) and `t ≤ dim W`. -/
theorem t_le_two_ell (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ)
    {V : Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ))}
    (hV0 : W0 A N L0 ≤ V) (hVT : V ≤ TR A N) (hVf : IsFeasible V) :
    t (W0 A N L0) V ≤ 2 * ell A N := by
  have hω : finrank ℂ ↥(Q1Subspace.pi1 V) ≤ ell A N := omega_le_ell A N hVT hVf
  have hstruct : finrank ℂ ↥V ≤ 2 * finrank ℂ ↥(Q1Subspace.pi1 V) := by
    have h1 := Q1Subspace.finrank_le_pi1_add_pi2 V
    have h2 : finrank ℂ ↥(Q1Subspace.pi2 V) ≤ finrank ℂ ↥(Q1Subspace.pi1 V) :=
      Submodule.finrank_mono hVf.1
    omega
  have ht : t (W0 A N L0) V = finrank ℂ ↥V - finrank ℂ ↥(W0 A N L0) :=
    t_eq_finrank_sub hV0
  have hmono : finrank ℂ ↥(W0 A N L0) ≤ finrank ℂ ↥V := Submodule.finrank_mono hV0
  omega

/-- **`t_min ≤ 2ℓ`** (Prop 1's a priori bound), when a feasible subspace exists. -/
theorem tMin_le_two_ell (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (hne : (tMinSet A N L0).Nonempty) :
    tMin A N L0 ≤ ((2 * ell A N : ℕ) : WithTop ℕ) := by
  obtain ⟨V, hV0, hVT, hVf, hVt⟩ := Nat.sInf_mem hne
  have h1 : sInf (tMinSet A N L0) ≤ t (W0 A N L0) V :=
    Nat.sInf_le ⟨V, hV0, hVT, hVf, rfl⟩
  have h2 : t (W0 A N L0) V ≤ 2 * ell A N := t_le_two_ell A N L0 hV0 hVT hVf
  rw [tMin, dif_pos hne]
  exact WithTop.coe_le_coe.mpr (le_trans h1 h2)

/-! ### 4. The minimum order is attained -/

/-- **The least feasible order is itself feasible.**  When a feasible subspace exists,
`sInf (tMinSet A N L0)` is the quotient dimension of some feasible `W`, hence it is a
feasible order: this is the correctness half of the interface theorem (Theorem 4 of
the paper) — the ordering itself is decided by `tMin_le_iff_dec`. -/
theorem dec_sInf_tMinSet
    (C : Matrix (Fin p) (Fin n) ℂ) (A : Matrix (Fin n) (Fin n) ℝ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (hN : N.mulVecLin.range = (Matrix.fromRows (C * Ac A) C).mulVecLin.ker)
    (hne : (tMinSet A N L0).Nonempty) :
    PaperI.DEC C (Ac A) (L0c L0) (sInf (tMinSet A N L0)) := by
  refine (tMin_le_iff_dec C A L0 N hN (sInf (tMinSet A N L0))).mp ?_
  rw [tMin, dif_pos hne]

/-- **The abstract minimum-order problem.**  For a monotone predicate `P` on the
number of free rows with a feasible order, the least feasible order is `sInf {r | P r}`;
this is the ordering that a binary search over `tMin_le_iff_dec` computes.  (The
`O(log (ℓ+2))` count is not formalised.) -/
theorem exists_least_of_monotone (P : ℕ → Prop) (h : ∃ r, P r) :
    P (sInf {r | P r}) ∧ ∀ s, P s → sInf {r | P r} ≤ s := by
  exact ⟨Nat.sInf_mem h, fun s hs => Nat.sInf_le hs⟩

/-! ### 5. The lower bound on the minimum order -/

/-- **`a − s₀ + 1 ≤ t_min`** (the paper's `eq:qmin-lb`), provided every feasible `W`
has `ω > 0` and `s₀ ≤ a = rank[U₀;V₀]`: it is Proposition 2 applied to the
minimising `W`. -/
theorem le_tMin_of_lowerBound
    (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ)
    (hω : ∀ V : Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ)),
      W0 A N L0 ≤ V → V ≤ TR A N → IsFeasible V → 0 < finrank ℂ ↥(Q1Subspace.pi1 V))
    (hs₀ : finrank ℂ ↥(W0 A N L0)
      ≤ finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0))) :
    ((finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0))
        - finrank ℂ ↥(W0 A N L0) + 1 : ℕ) : WithTop ℕ) ≤ tMin A N L0 := by
  by_cases hne : (tMinSet A N L0).Nonempty
  · rw [tMin, dif_pos hne]
    refine WithTop.coe_le_coe.mpr ?_
    obtain ⟨V₀, hV0, hVT, hVf, hVt⟩ := Nat.sInf_mem hne
    rw [← hVt]
    exact lowerBound_sub hV0 hVf (hω V₀ hV0 hVT hVf) hs₀
  · rw [tMin, dif_neg hne]
    exact le_top


/-- **`eq:qmin-lb` in the paper's unconditional form**: `a + 1 − s₀ ≤ t_min`, i.e.
`max 0 (a − s₀ + 1) ≤ t_min` (natural-number subtraction), with no side condition on
`s₀ ≤ a`.  The only hypothesis is `ω > 0` for every feasible `W`, which the paper's
structural bound also uses. -/
theorem le_tMin_of_lowerBound_max
    (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ)
    (hω : ∀ V : Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ)),
      W0 A N L0 ≤ V → V ≤ TR A N → IsFeasible V → 0 < finrank ℂ ↥(Q1Subspace.pi1 V)) :
    ((finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) + 1
        - finrank ℂ ↥(W0 A N L0) : ℕ) : WithTop ℕ) ≤ tMin A N L0 := by
  by_cases hsa : finrank ℂ ↥(W0 A N L0)
      ≤ finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0))
  · have h := le_tMin_of_lowerBound A N L0 hω hsa
    have hfin : finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) + 1
        - finrank ℂ ↥(W0 A N L0)
        = finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0))
          - finrank ℂ ↥(W0 A N L0) + 1 := by omega
    rw [hfin]
    exact h
  · have h0 : finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) + 1
        - finrank ℂ ↥(W0 A N L0) = 0 := by omega
    rw [h0]
    exact zero_le

end Q1Paper.PaperII


