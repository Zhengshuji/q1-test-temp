/-
Q1Paper/PaperII/GraphExtract.lean

Paper II, Proposition `prop:tight`, the converse direction — the setup.

A feasible subspace `W` with `dim W = dim (π₁ W) + 1` projects onto `U = π₁ W` with a
one-dimensional kernel; this file constructs the projection, shows it is onto, and
produces the kernel direction `b ≠ 0` that the graph extension `W(G, b)` needs.

Contents.
* `projW` — the first projection `W → E`.
* `projW_range` — its range is `π₁ W`.
* `projU` — the projection `W → π₁ W` (codomain restricted).
* `projU_surjective` — it is onto.
* `ker_finrank_eq_one` — `dim ker (π₁|_W) = 1` when `dim W = dim (π₁ W) + 1`.
* `exists_kernel_direction` — there is `x ∈ ker`, `x ≠ 0`.
* `exists_kernel_b` — hence `b = x₂ ≠ 0` in `π₁ W` (the paper's direction `b`).

Next step (not in this file): the section `sec` of `projU` and the induced
`G = π₂ ∘ sec`, giving `W = W(G, b)` (`PaperII/GraphExtension.lean` defines that
subspace and its pencil).

Reuses: `Q1Subspace.mem_pi1`, `Q1Subspace.mem_pi2`,
`LinearMap.finrank_range_add_finrank_ker`, `Submodule.exists_mem_ne_zero_of_ne_bot`.
-/

import Q1Paper.PaperII.GraphExtension

open Module Matrix

namespace Q1Paper.PaperII

variable {K : Type*} [Field K] {k : ℕ}

/-- The first projection `W → E`. -/
noncomputable def projW (W : Submodule K ((Fin k → K) × (Fin k → K))) :
    W →ₗ[K] (Fin k → K) :=
  (LinearMap.fst K (Fin k → K) (Fin k → K)).comp W.subtype

theorem projW_range (W : Submodule K ((Fin k → K) × (Fin k → K))) :
    (projW W).range = Q1Subspace.pi1 W := by
  rw [projW, LinearMap.range_comp, Submodule.range_subtype, Q1Subspace.pi1]

/-- The projection `W → π₁ W`. -/
noncomputable def projU (W : Submodule K ((Fin k → K) × (Fin k → K))) :
    W →ₗ[K] ↥(Q1Subspace.pi1 W) :=
  (projW W).codRestrict (Q1Subspace.pi1 W) (fun x => by
    rw [← projW_range]
    exact LinearMap.mem_range_self (projW W) x)

theorem projU_surjective (W : Submodule K ((Fin k → K) × (Fin k → K))) :
    Function.Surjective (projU W) := by
  intro u
  obtain ⟨y, hy⟩ := Q1Subspace.mem_pi1.mp u.2
  refine ⟨⟨(u.1, y), hy⟩, ?_⟩
  apply Subtype.ext
  rfl

/-- **The kernel of the projection is one-dimensional** under
`dim W = dim (π₁ W) + 1`. -/
theorem ker_finrank_eq_one (W : Submodule K ((Fin k → K) × (Fin k → K)))
    (hdim : finrank K ↥W = finrank K ↥(Q1Subspace.pi1 W) + 1) :
    finrank K ↥(LinearMap.ker (projU W)) = 1 := by
  have hrn := LinearMap.finrank_range_add_finrank_ker (projU W)
  have hrange : finrank K ↥(projU W).range = finrank K ↥(Q1Subspace.pi1 W) := by
    have htop : (projU W).range = ⊤ :=
      LinearMap.range_eq_top.mpr (projU_surjective W)
    rw [htop]
    simp
  rw [hrange, hdim] at hrn
  omega

/-- A nonzero element of the kernel exists. -/
theorem exists_kernel_direction (W : Submodule K ((Fin k → K) × (Fin k → K)))
    (hdim : finrank K ↥W = finrank K ↥(Q1Subspace.pi1 W) + 1) :
    ∃ x : W, x ∈ LinearMap.ker (projU W) ∧ x ≠ 0 := by
  have hdim1 : finrank K ↥(LinearMap.ker (projU W)) = 1 := ker_finrank_eq_one W hdim
  have hne : LinearMap.ker (projU W) ≠ ⊥ := by
    intro h
    rw [h, finrank_bot] at hdim1
    omega
  exact Submodule.exists_mem_ne_zero_of_ne_bot hne

/-- **The paper's direction `b`**: the second component of a nonzero kernel element
lies in `π₁ W` and is nonzero. -/
theorem exists_kernel_b (W : Submodule K ((Fin k → K) × (Fin k → K)))
    (hfeas : IsFeasible W)
    (hdim : finrank K ↥W = finrank K ↥(Q1Subspace.pi1 W) + 1) :
    ∃ b : ↥(Q1Subspace.pi1 W), b ≠ 0 := by
  obtain ⟨x, hxker, hxne⟩ := exists_kernel_direction W hdim
  have hx1 : ((x : W) : (Fin k → K) × (Fin k → K)).1 = 0 := by
    have h0 : projU W x = 0 := LinearMap.mem_ker.mp hxker
    have h1 := congrArg Subtype.val h0
    simpa [projU, projW] using h1
  have hx2 : ((x : W) : (Fin k → K) × (Fin k → K)).2 ≠ 0 := by
    intro h
    apply hxne
    apply Subtype.ext
    exact Prod.ext hx1 h
  refine ⟨⟨((x : W) : (Fin k → K) × (Fin k → K)).2, ?_⟩, ?_⟩
  · exact hfeas.1 (Q1Subspace.mem_pi2.mpr ⟨_, x.2⟩)
  · intro h
    exact hx2 (congrArg Subtype.val h)


/-- **Prop 3, the converse direction.**  A feasible `W` with
`dim W = dim (π₁ W) + 1` is the graph extension `W(G, b)` of its projection. -/
theorem exists_graph_representation
    (W : Submodule K ((Fin k → K) × (Fin k → K)))
    (hfeas : IsFeasible W)
    (hdim : finrank K ↥W = finrank K ↥(Q1Subspace.pi1 W) + 1) :
    ∃ (b : ↥(Q1Subspace.pi1 W)), b ≠ 0 ∧
      ∃ (G : ↥(Q1Subspace.pi1 W) →ₗ[K] ↥(Q1Subspace.pi1 W)),
        W = graphExt (Q1Subspace.pi1 W) G b := by
  classical
  obtain ⟨sec, hsec⟩ :=
    LinearMap.exists_rightInverse_of_surjective (projU W)
      (LinearMap.range_eq_top.mpr (projU_surjective W))
  have hsec' : ∀ u, projU W (sec u) = u := by
    intro u
    rw [← LinearMap.comp_apply, hsec]
    rfl
  obtain ⟨x, hxker, hxne⟩ := exists_kernel_direction W hdim
  have hx1 : ((x : W) : (Fin k → K) × (Fin k → K)).1 = 0 := by
    have h0 : projU W x = 0 := LinearMap.mem_ker.mp hxker
    have h1 := congrArg Subtype.val h0
    simpa [projU, projW] using h1
  have hx2 : ((x : W) : (Fin k → K) × (Fin k → K)).2 ≠ 0 := by
    intro h
    apply hxne
    apply Subtype.ext
    exact Prod.ext hx1 h
  let b : ↥(Q1Subspace.pi1 W) :=
    ⟨((x : W) : (Fin k → K) × (Fin k → K)).2, hfeas.1 (Q1Subspace.mem_pi2.mpr ⟨_, x.2⟩)⟩
  have hb : b ≠ 0 := fun h => hx2 (congrArg Subtype.val h)
  let G : ↥(Q1Subspace.pi1 W) →ₗ[K] ↥(Q1Subspace.pi1 W) :=
    ((LinearMap.snd K (Fin k → K) (Fin k → K)).comp ((W.subtype).comp (sec : _ →ₗ[K] W))).codRestrict
      (Q1Subspace.pi1 W)
      (fun u => hfeas.1 (Q1Subspace.mem_pi2.mpr ⟨((sec u : W) : (Fin k → K) × (Fin k → K)).1, (sec u).2⟩))
  refine ⟨b, hb, G, ?_⟩
  have hsec1 : ∀ u, ((sec u : W) : (Fin k → K) × (Fin k → K)).1 = (u : Fin k → K) :=
    fun u => congrArg Subtype.val (hsec' u)
  have hGval : ∀ u, ((G u : ↥(Q1Subspace.pi1 W)) : Fin k → K)
      = ((sec u : W) : (Fin k → K) × (Fin k → K)).2 := fun u => rfl
  have hbval : (b : Fin k → K) = ((x : W) : (Fin k → K) × (Fin k → K)).2 := rfl
  have hker_eq : LinearMap.ker (projU W) = Submodule.span K {x} := by
    have hle : Submodule.span K {x} ≤ LinearMap.ker (projU W) :=
      Submodule.span_le.mpr (Set.singleton_subset_iff.mpr hxker)
    have hd : finrank K ↥(Submodule.span K {x}) = finrank K ↥(LinearMap.ker (projU W)) := by
      rw [finrank_span_singleton (K := K) hxne, ker_finrank_eq_one W hdim]
    exact (Submodule.eq_of_le_of_finrank_eq hle hd).symm
  ext p
  constructor
  · intro hp
    set y : W := ⟨p, hp⟩ with hy
    have hq : y - sec (projU W y) ∈ LinearMap.ker (projU W) := by
      rw [LinearMap.mem_ker, map_sub, hsec' (projU W y), sub_self]
    rw [hker_eq, Submodule.mem_span_singleton] at hq
    obtain ⟨α, hα⟩ := hq
    have hy_decomp : ((y : W) : (Fin k → K) × (Fin k → K))
        = ((sec (projU W y) : W) : (Fin k → K) × (Fin k → K))
          + α • ((x : W) : (Fin k → K) × (Fin k → K)) := by
      have h := congrArg (fun z : W => (z : (Fin k → K) × (Fin k → K))) hα
      simp only [Submodule.coe_smul, Submodule.coe_sub] at h
      calc ((y : W) : (Fin k → K) × (Fin k → K))
          = (((y : W) : (Fin k → K) × (Fin k → K))
              - ((sec (projU W y) : W) : (Fin k → K) × (Fin k → K)))
            + ((sec (projU W y) : W) : (Fin k → K) × (Fin k → K)) :=
            (sub_add_cancel _ _).symm
        _ = α • ((x : W) : (Fin k → K) × (Fin k → K))
            + ((sec (projU W y) : W) : (Fin k → K) × (Fin k → K)) := by rw [h.symm]
        _ = ((sec (projU W y) : W) : (Fin k → K) × (Fin k → K))
            + α • ((x : W) : (Fin k → K) × (Fin k → K)) := add_comm _ _
    refine mem_graphExt.mpr ⟨projU W y, α, ?_, ?_⟩
    · calc p.1 = ((y : W) : (Fin k → K) × (Fin k → K)).1 := rfl
        _ = ((sec (projU W y) : W) : (Fin k → K) × (Fin k → K)).1 := by
            have h := congrArg Prod.fst hy_decomp
            rwa [Prod.fst_add, Prod.smul_fst, hx1, smul_zero, add_zero] at h
        _ = ((projU W y : ↥(Q1Subspace.pi1 W)) : Fin k → K) := hsec1 _
    · calc p.2 = ((y : W) : (Fin k → K) × (Fin k → K)).2 := rfl
        _ = ((sec (projU W y) : W) : (Fin k → K) × (Fin k → K)).2
              + α • ((x : W) : (Fin k → K) × (Fin k → K)).2 := by
            have h := congrArg Prod.snd hy_decomp
            rwa [Prod.snd_add, Prod.smul_snd] at h
        _ = ((G (projU W y) : ↥(Q1Subspace.pi1 W)) : Fin k → K) + α • (b : Fin k → K) := by
            rw [← hGval, ← hbval]
        _ = ((G (projU W y) + α • b : ↥(Q1Subspace.pi1 W)) : Fin k → K) := by
            rw [Submodule.coe_add, Submodule.coe_smul]
  · intro hp
    obtain ⟨u, α, h1, h2⟩ := mem_graphExt.mp hp
    have hmem : ((sec u : W) : (Fin k → K) × (Fin k → K))
        + α • ((x : W) : (Fin k → K) × (Fin k → K)) ∈ W :=
      W.add_mem (sec u).2 (W.smul_mem α x.2)
    have hpeq : ((sec u : W) : (Fin k → K) × (Fin k → K))
        + α • ((x : W) : (Fin k → K) × (Fin k → K)) = p := by
      apply Prod.ext
      · calc (((sec u : W) : (Fin k → K) × (Fin k → K))
              + α • ((x : W) : (Fin k → K) × (Fin k → K))).1
            = ((sec u : W) : (Fin k → K) × (Fin k → K)).1 := by
              rw [Prod.fst_add, Prod.smul_fst, hx1, smul_zero, add_zero]
          _ = (u : Fin k → K) := hsec1 u
          _ = p.1 := h1.symm
      · calc (((sec u : W) : (Fin k → K) × (Fin k → K))
              + α • ((x : W) : (Fin k → K) × (Fin k → K))).2
            = ((sec u : W) : (Fin k → K) × (Fin k → K)).2
              + α • ((x : W) : (Fin k → K) × (Fin k → K)).2 := by
              rw [Prod.snd_add, Prod.smul_snd]
          _ = ((G u : ↥(Q1Subspace.pi1 W)) : Fin k → K) + α • (b : Fin k → K) := by
              rw [hGval, hbval]
          _ = ((G u + α • b : ↥(Q1Subspace.pi1 W)) : Fin k → K) := by
              rw [Submodule.coe_add, Submodule.coe_smul]
          _ = p.2 := h2.symm
    rw [← hpeq]
    exact hmem

end Q1Paper.PaperII

