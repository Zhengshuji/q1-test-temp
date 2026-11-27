/-
Q1Paper/PaperII/Tightness.lean

Paper II, Proposition `prop:tight`, the composed criterion (complex designs):
`t_min = a − s₀ + 1` if and only if the prescribed subspace admits a one-dimensional
extension `W(G,b)` inside `T` whose pencil has the paper's rank.

Contents.
* `pi1_eq_sup_of_finrank` — at an attaining `W` (feasible, `W₀ ≤ W`,
  `dim W = a + 1`), the projection `π₁W` is exactly `U₀+V₀` (and `ω > 0` is derived,
  not assumed).
* `omega_pos_of_nonzero` — `ω > 0` for every feasible `W ≥ W₀` when `W₀ ≠ 0`.
* `W0_ne_bot_of_pos` — `W₀ ≠ 0` when the paper's data has positive dimension.
* `tMin_eq_of_graph` — the `(⇐)` direction (no non-degeneracy hypothesis).
* `exists_graph_of_tMin_eq` — the `(⇒)` direction.
-/

import Q1Paper.PaperII.MinOrder
import Q1Paper.PaperII.GraphExtension
import Q1Paper.PaperII.GraphExtract

set_option maxHeartbeats 800000

open Module Matrix

namespace Q1Paper.PaperII

variable {p r0 n k : ℕ}

/-- **`ω > 0` for every feasible `W ≥ W₀`** when `W₀ ≠ 0`: such a `W` is nonzero, and
`dim W ≤ 2ω`. -/
theorem omega_pos_of_nonzero
    (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ)
    (hW0ne : W0 A N L0 ≠ ⊥) :
    ∀ V : Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ)),
      W0 A N L0 ≤ V → V ≤ TR A N → IsFeasible V → 0 < finrank ℂ ↥(Q1Subspace.pi1 V) := by
  intro V hV _ hfeas
  have h1 := Q1Subspace.finrank_le_pi1_add_pi2 (K := ℂ) V
  have h2 : finrank ℂ ↥(Q1Subspace.pi2 V) ≤ finrank ℂ ↥(Q1Subspace.pi1 V) :=
    Submodule.finrank_mono hfeas.1
  have hne : V ≠ ⊥ := fun h => hW0ne (le_bot_iff.mp (h ▸ hV))
  have hpos : 0 < finrank ℂ ↥V := by
    by_contra h
    exact hne ((Submodule.finrank_eq_zero).mp (by omega))
  omega

/-- `W₀ ≠ ⊥` when the paper's data has positive dimension. -/
theorem W0_ne_bot_of_pos
    (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ)
    (hpos : 0 < finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0))) :
    W0 A N L0 ≠ ⊥ := by
  intro h
  have hbot : Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0) = ⊥ := by
    rw [h]
    simp only [Q1Subspace.pi1, Q1Subspace.pi2, Submodule.map_bot, sup_bot_eq]
  rw [hbot] at hpos
  simp at hpos

/-- **At an attaining `W`, `π₁W = U₀+V₀`.**  `W₀ ≤ W` gives `U₀+V₀ ≤ π₁W`, the
structural bound gives `ω ≤ a` from `dim W = a+1`, and `a ≤ ω` is monotonicity.
The positivity `ω > 0` needed by the structural bound is derived from
`dim W ≤ 2ω` and `dim W = a + 1 > 0`. -/
theorem pi1_eq_sup_of_finrank
    (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ)
    {W : Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ))}
    (hW0 : W0 A N L0 ≤ W) (hfeas : IsFeasible W)
    (hdim : finrank ℂ ↥W
      = finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) + 1) :
    Q1Subspace.pi1 W = Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0) := by
  have hω : 0 < finrank ℂ ↥(Q1Subspace.pi1 W) := by
    have h1 := Q1Subspace.finrank_le_pi1_add_pi2 (K := ℂ) W
    have h2 : finrank ℂ ↥(Q1Subspace.pi2 W) ≤ finrank ℂ ↥(Q1Subspace.pi1 W) :=
      Submodule.finrank_mono hfeas.1
    omega
  have hle : Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)
      ≤ Q1Subspace.pi1 W := by
    refine sup_le ?_ ?_
    · exact Submodule.map_mono (f := LinearMap.fst ℂ (Fin k → ℂ) (Fin k → ℂ)) hW0
    · exact (Submodule.map_mono (f := LinearMap.snd ℂ (Fin k → ℂ) (Fin k → ℂ)) hW0).trans hfeas.1
  have hωa : finrank ℂ ↥(Q1Subspace.pi1 W)
      ≤ finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) := by
    have hb := (Q1Paper.claim6_struct hfeas.1 hω hfeas.2).1
    omega
  have haω : finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0))
      ≤ finrank ℂ ↥(Q1Subspace.pi1 W) := Submodule.finrank_mono hle
  exact Q1Subspace.eq_of_le_of_finrank_eq hle (by omega)

/-- **Prop 3, the `(⇐)` direction.**  If there are `b ≠ 0` and `G : U₀+V₀ → U₀+V₀`
with `W₀ ⊆ W(G,b) ⊆ T` and the paper's pencil rank condition, then the minimum order
saturates: `t_min = dim (U₀+V₀) + 1 − s₀`.  No non-degeneracy hypothesis: `ω > 0`
for every feasible `W ≥ W₀` follows from `b ≠ 0`. -/
theorem tMin_eq_of_graph
    (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ)
    {b : ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0))}
    {G : ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) →ₗ[ℂ]
         ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0))}
    (hb : b ≠ 0)
    (hW0le : W0 A N L0
      ≤ graphExt (Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) G b)
    (hWTle : graphExt (Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) G b
      ≤ TR A N)
    (hrank : ∀ lam : ℂ,
      finrank ℂ ↥(Submodule.map
          (graphPencil (Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) G lam) ⊤
        ⊔ Submodule.span ℂ
            {((b : ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0))) : Fin k → ℂ)})
        = finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0))) :
    tMin A N L0 = ↑((finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)))
      + 1 - finrank ℂ ↥(W0 A N L0)) := by
  have hW0ne : W0 A N L0 ≠ ⊥ := by
    intro h
    have hbot : Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0) = ⊥ := by
      rw [h]
      simp only [Q1Subspace.pi1, Q1Subspace.pi2, Submodule.map_bot, sup_bot_eq]
    haveI : Subsingleton ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) := by
      rw [hbot]
      infer_instance
    exact hb (Subsingleton.elim b 0)
  have hω := omega_pos_of_nonzero A N L0 hW0ne
  have hfeas : IsFeasible
      (graphExt (Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) G b) :=
    graphExt_feasible _ G b hrank
  have hmem : t (W0 A N L0)
      (graphExt (Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) G b)
      ∈ tMinSet A N L0 :=
    ⟨_, hW0le, hWTle, hfeas, rfl⟩
  have hne : (tMinSet A N L0).Nonempty := ⟨_, hmem⟩
  have ht : t (W0 A N L0)
      (graphExt (Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) G b)
      = finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0))
        + 1 - finrank ℂ ↥(W0 A N L0) :=
    t_eq_of_graph A N L0 hb hW0le
  have hub : tMin A N L0
      ≤ ↑((finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)))
        + 1 - finrank ℂ ↥(W0 A N L0)) := by
    rw [tMin, dif_pos hne]
    exact WithTop.coe_le_coe.mpr (by rw [← ht]; exact Nat.sInf_le hmem)
  exact le_antisymm hub (le_tMin_of_lowerBound_max A N L0 hω)

/-- **Prop 3, the `(⇒)` direction.**  If the minimum order saturates,
`t_min = a + 1 − s₀` (with `s₀ ≤ a`), then some feasible `W` with `W₀ ≤ W ≤ T` and
`dim W = a + 1` is a graph extension `W(G, b)`, and its projection is exactly
`U₀+V₀` — the paper's data for the tightness criterion. -/
theorem exists_graph_of_tMin_eq
    (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ)
    (hsa : finrank ℂ ↥(W0 A N L0)
      ≤ finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)))
    (heq : tMin A N L0
      = ↑(finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0))
        + 1 - finrank ℂ ↥(W0 A N L0))) :
    ∃ (V : Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ)))
      (G : ↥(Q1Subspace.pi1 V) →ₗ[ℂ] ↥(Q1Subspace.pi1 V))
      (b : ↥(Q1Subspace.pi1 V)),
      W0 A N L0 ≤ V ∧ V ≤ TR A N ∧ IsFeasible V ∧ b ≠ 0 ∧
        V = graphExt (Q1Subspace.pi1 V) G b ∧
        Q1Subspace.pi1 V
          = Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0) ∧
        (∀ lam : ℂ,
          finrank ℂ ↥(Submodule.map (graphPencil (Q1Subspace.pi1 V) G lam) ⊤
            ⊔ Submodule.span ℂ {((b : ↥(Q1Subspace.pi1 V)) : Fin k → ℂ)})
            = finrank ℂ ↥(Q1Subspace.pi1 V)) := by
  classical
  have hne : (tMinSet A N L0).Nonempty := by
    by_contra h
    rw [tMin, dif_neg h] at heq
    exact WithTop.not_top_le_coe _ (le_of_eq heq)
  obtain ⟨V, hV0, hVT, hVf, hVt⟩ := Nat.sInf_mem hne
  have hsInf : sInf (tMinSet A N L0)
      = finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0))
        + 1 - finrank ℂ ↥(W0 A N L0) := by
    rw [tMin, dif_pos hne] at heq
    exact WithTop.coe_inj.mp heq
  have ht : t (W0 A N L0) V
      = finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0))
        + 1 - finrank ℂ ↥(W0 A N L0) := by
    rw [hVt, hsInf]
  have hdimV : finrank ℂ ↥V
      = finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) + 1 := by
    have hsub := t_eq_finrank_sub (K := ℂ) hV0
    have hmono := Submodule.finrank_mono hV0
    omega
  have hpi := pi1_eq_sup_of_finrank A N L0 hV0 hVf hdimV
  have hdimV' : finrank ℂ ↥V = finrank ℂ ↥(Q1Subspace.pi1 V) + 1 := by
    rw [hpi]
    exact hdimV
  obtain ⟨b, hb, G, hWV⟩ := exists_graph_representation V hVf hdimV'
  refine ⟨V, G, b, hV0, hVT, hVf, hb, hWV, hpi, ?_⟩
  intro lam
  have hpen := graphExt_piLam (Q1Subspace.pi1 V) G b lam
  have hspec := hVf.2 lam
  rw [hWV] at hspec
  rw [hpen] at hspec
  rw [graphExt_pi1] at hspec
  exact hspec


/-- `U₀ + V₀`, the projection of the prescribed subspace (a short name keeps the
statements below small). -/
noncomputable def UV (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) : Submodule ℂ (Fin k → ℂ) :=
  Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)

theorem UV_eq (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ) :
    UV A N L0 = Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0) := rfl

/-- Membership in `tMinSet`, stated with an abstract `V`. -/
theorem mem_tMinSet
    (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ)
    {V : Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ))}
    (hV0 : W0 A N L0 ≤ V) (hVT : V ≤ TR A N) (hVf : IsFeasible V) :
    t (W0 A N L0) V ∈ tMinSet A N L0 :=
  ⟨V, hV0, hVT, hVf, rfl⟩

/-- `t_min` is below the quotient dimension of any feasible `W ≥ W₀`. -/
theorem tMin_le_of_feasible
    (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ)
    {V : Submodule ℂ ((Fin k → ℂ) × (Fin k → ℂ))}
    (hV0 : W0 A N L0 ≤ V) (hVT : V ≤ TR A N) (hVf : IsFeasible V) :
    tMin A N L0 ≤ ((t (W0 A N L0) V : ℕ) : WithTop ℕ) := by
  have hmem := mem_tMinSet A N L0 hV0 hVT hVf
  by_cases hne : (tMinSet A N L0).Nonempty
  · rw [tMin, dif_pos hne]
    exact WithTop.coe_le_coe.mpr (Nat.sInf_le hmem)
  · exact absurd ⟨_, hmem⟩ hne

end Q1Paper.PaperII

