/-
Q1Paper/PaperII/GraphExtension.lean

Paper II, Proposition `prop:tight`, the `(G, b)` construction: the graph-like subspace

  `W(G, b) = { (h, G h + α b) : h ∈ U, α ∈ K }`

of `E × E`, `E = Fin k → K`.

Contents.
* `graphMap`, `graphExt` — the map `(h, α) ↦ (h, G h + α b)` and its range.
* `mem_graphExt` — membership.
* `graphExt_pi1` — `π₁ W(G,b) = U`.
* `graphExt_pi2_le` — `π₂ W(G,b) ≤ U`.
* `graphExt_finrank` — `dim W(G,b) = dim U + 1` when `b ≠ 0`.
* `graphPencil`, `graphPencil_apply` — the pencil map `h ↦ λ h − G h`.
* `graphExt_piLam` — `πλ W(G,b) = (λI − G)U + span {b}`, so the paper's rank
  condition `rank[λI − G  b] = dim U` is `dim πλ W = dim U`.
* `graphExt_feasible` — the rank condition makes `W(G,b)` feasible.

Reuses: `Q1Subspace.pi1`, `pi2`, `piLam`, `mem_piLam`, `mem_pi2`,
`LinearMap.finrank_range_add_finrank_ker`, `Submodule.mem_sup`.
-/

import Q1Paper.PaperII.LowerBound

open Module Matrix

namespace Q1Paper.PaperII

variable {K : Type*} [Field K] {k : ℕ}

/-- The linear map `(h, α) ↦ (h, G h + α b)`. -/
noncomputable def graphMap (U : Submodule K (Fin k → K)) (G : U →ₗ[K] U) (b : U) :
    (U × K) →ₗ[K] ((Fin k → K) × (Fin k → K)) where
  toFun p := ((p.1 : Fin k → K), ((G p.1 + p.2 • b : U) : Fin k → K))
  map_add' p q := by
    apply Prod.ext
    · rfl
    · show (((G (p.1 + q.1) + (p.2 + q.2) • b : U)) : Fin k → K)
        = ((G p.1 + p.2 • b : U) : Fin k → K) + ((G q.1 + q.2 • b : U) : Fin k → K)
      simp only [map_add, add_smul, Submodule.coe_add]
      abel
  map_smul' c p := by
    apply Prod.ext
    · rfl
    · show (((G (c • p.1) + (c * p.2) • b : U)) : Fin k → K)
        = c • ((G p.1 + p.2 • b : U) : Fin k → K)
      simp only [map_smul, smul_add, smul_smul, Submodule.coe_add, Submodule.coe_smul, mul_comm]

/-- **The graph-like subspace** `W(G,b) = {(h, G h + α b)}`. -/
noncomputable def graphExt (U : Submodule K (Fin k → K)) (G : U →ₗ[K] U) (b : U) :
    Submodule K ((Fin k → K) × (Fin k → K)) :=
  (graphMap U G b).range

theorem mem_graphExt {U : Submodule K (Fin k → K)} {G : U →ₗ[K] U} {b : U}
    {x y : Fin k → K} :
    (x, y) ∈ graphExt U G b ↔
      ∃ (h : U) (α : K), x = (h : Fin k → K) ∧ y = ((G h + α • b : U) : Fin k → K) := by
  rw [graphExt, LinearMap.mem_range]
  constructor
  · rintro ⟨p, hp⟩
    exact ⟨p.1, p.2, (congrArg Prod.fst hp).symm, (congrArg Prod.snd hp).symm⟩
  · rintro ⟨h, α, rfl, rfl⟩
    exact ⟨(h, α), rfl⟩

theorem graphExt_pi1 (U : Submodule K (Fin k → K)) (G : U →ₗ[K] U) (b : U) :
    Q1Subspace.pi1 (graphExt U G b) = U := by
  have hmap : LinearMap.fst K (Fin k → K) (Fin k → K) ∘ₗ graphMap U G b
      = (Submodule.subtype U) ∘ₗ LinearMap.fst K U K := by
    apply LinearMap.ext
    intro p
    rfl
  rw [graphExt, Q1Subspace.pi1, ← LinearMap.range_comp, hmap, LinearMap.range_comp,
    show (LinearMap.fst K U K).range = ⊤ from
      LinearMap.range_eq_top.mpr (fun u => ⟨(u, 0), rfl⟩),
    Submodule.map_top, Submodule.range_subtype]

theorem graphExt_pi2_le (U : Submodule K (Fin k → K)) (G : U →ₗ[K] U) (b : U) :
    Q1Subspace.pi2 (graphExt U G b) ≤ U := by
  intro y hy
  rw [Q1Subspace.mem_pi2] at hy
  obtain ⟨x, hxy⟩ := hy
  rw [mem_graphExt] at hxy
  obtain ⟨h, α, -, rfl⟩ := hxy
  exact Submodule.coe_mem _

theorem graphExt_finrank (U : Submodule K (Fin k → K)) (G : U →ₗ[K] U) (b : U)
    (hb : b ≠ 0) :
    finrank K ↥(graphExt U G b) = finrank K ↥U + 1 := by
  have hrn := LinearMap.finrank_range_add_finrank_ker (graphMap U G b)
  have hker : LinearMap.ker (graphMap U G b) = ⊥ := by
    rw [LinearMap.ker_eq_bot']
    rintro ⟨h, α⟩ hp
    have h1 : (h : Fin k → K) = 0 := congrArg Prod.fst hp
    have h2 : ((G h + α • b : U) : Fin k → K) = 0 := congrArg Prod.snd hp
    have hh : h = 0 := Subtype.ext h1
    rw [hh, map_zero, zero_add] at h2
    have hsb : α • b = 0 := Subtype.ext h2
    have hα : α = 0 := by
      rcases smul_eq_zero.mp hsb with h | h
      · exact h
      · exact absurd h hb
    exact Prod.ext hh hα
  rw [hker, finrank_bot, add_zero] at hrn
  have hdim : finrank K (U × K) = finrank K ↥U + 1 := by
    rw [Module.finrank_prod, Module.finrank_self]
  rw [hdim] at hrn
  exact hrn

/-! ### The pencil of the graph extension -/

/-- The pencil map `h ↦ λ h − G h`. -/
noncomputable def graphPencil (U : Submodule K (Fin k → K)) (G : U →ₗ[K] U) (lam : K) :
    U →ₗ[K] (Fin k → K) :=
  (Submodule.subtype U) ∘ₗ (lam • LinearMap.id - G)

theorem graphPencil_apply (U : Submodule K (Fin k → K)) (G : U →ₗ[K] U) (lam : K) (h : U) :
    graphPencil U G lam h = lam • (h : Fin k → K) - ((G h : U) : Fin k → K) := by
  simp [graphPencil]

/-- **The pencil of `W(G,b)`**: `πλ W(G,b) = (λI − G)U + span {b}`. -/
theorem graphExt_piLam (U : Submodule K (Fin k → K)) (G : U →ₗ[K] U) (b : U) (lam : K) :
    Q1Subspace.piLam lam (graphExt U G b)
      = Submodule.map (graphPencil U G lam) ⊤
        ⊔ Submodule.span K {((b : U) : Fin k → K)} := by
  ext x
  rw [Q1Subspace.mem_piLam]
  constructor
  · rintro ⟨p, hp, hpx⟩
    obtain ⟨h, α, h1, h2⟩ := mem_graphExt.mp hp
    rw [h1, h2] at hpx
    have hdeep : lam • (h : Fin k → K) - ((G h + α • b : U) : Fin k → K)
        = graphPencil U G lam h + ((-α) • ((b : U) : Fin k → K)) := by
      rw [graphPencil_apply, Submodule.coe_add, Submodule.coe_smul]
      module
    rw [← hpx, hdeep]
    refine Submodule.add_mem _ ?_ ?_
    · exact Submodule.mem_sup_left (Submodule.mem_map.mpr ⟨h, Submodule.mem_top, rfl⟩)
    · exact Submodule.mem_sup_right (Submodule.smul_mem _ _ (Submodule.subset_span rfl))
  · intro hx
    rw [Submodule.mem_sup] at hx
    obtain ⟨y, hy, z, hz, rfl⟩ := hx
    rw [Submodule.mem_map] at hy
    obtain ⟨h, -, rfl⟩ := hy
    rw [Submodule.mem_span_singleton] at hz
    obtain ⟨β, rfl⟩ := hz
    refine ⟨((h : Fin k → K), ((G h + (-β) • b : U) : Fin k → K)), ?_, ?_⟩
    · exact mem_graphExt.mpr ⟨h, -β, rfl, rfl⟩
    · show lam • (h : Fin k → K) - ((G h + (-β) • b : U) : Fin k → K)
        = graphPencil U G lam h + β • ((b : U) : Fin k → K)
      rw [graphPencil_apply, Submodule.coe_add, Submodule.coe_smul]
      module

theorem graphExt_feasible (U : Submodule K (Fin k → K)) (G : U →ₗ[K] U) (b : U)
    (hrank : ∀ lam : K,
      finrank K ↥(Submodule.map (graphPencil U G lam) ⊤
        ⊔ Submodule.span K {((b : U) : Fin k → K)}) = finrank K ↥U) :
    IsFeasible (graphExt U G b) := by
  constructor
  · rw [graphExt_pi1]
    exact graphExt_pi2_le U G b
  · intro lam
    rw [graphExt_piLam, graphExt_pi1]
    exact hrank lam

/-! ### Prop 3, the `(G,b)` direction -/

/-- **Prop 3, the `(G,b)` direction** (complex design layer).  Take
`U = π₁W₀ ⊔ π₂W₀` and let `W₀ ⊆ W(G,b)`.  Then the quotient dimension of `W(G,b)` is
`dim U + 1 − s₀`, i.e. the lower bound `a − s₀ + 1` is attained (with `a = dim U`),
provided `b ≠ 0`.  Feasibility of `W(G,b)` is `graphExt_feasible`, and `W₀ ⊆ W(G,b) ⊆ T`
is supplied by the caller. -/
theorem t_eq_of_graph
    (A : Matrix (Fin n) (Fin n) ℝ) (N : Matrix (Fin n) (Fin k) ℂ)
    (L0 : Matrix (Fin r0) (Fin n) ℝ)
    {b : ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0))}
    {G : ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) →ₗ[ℂ]
         ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0))}
    (hb : b ≠ 0)
    (hW0 : W0 A N L0
      ≤ graphExt (Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) G b) :
    t (W0 A N L0) (graphExt (Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) G b)
      = finrank ℂ ↥(Q1Subspace.pi1 (W0 A N L0) ⊔ Q1Subspace.pi2 (W0 A N L0)) + 1
        - finrank ℂ ↥(W0 A N L0) := by
  rw [t_eq_finrank_sub hW0, graphExt_finrank _ G b hb]

end Q1Paper.PaperII

