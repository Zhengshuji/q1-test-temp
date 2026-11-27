"""gen_lift.py -- emit PRecursionLift3.lean byte-exactly.

The Lean source contains U+29F8 (the quotient symbol) which the Windows text
pipeline intermittently replaces by U+2294 (sup).  This generator keeps the
Python source pure ASCII: every U+29F8 is written as the escape \\u29f8, so the
emitted .lean file is deterministic.
"""
import io
import os

Q = "\u29f8"  # the quotient symbol used by Lean's `V ⧸ M` notation

SRC = r'''import Mathlib

/-!
# PRecursionLift

Construction step of the `(≤)` half of the one-step recursion for
`P(A,B,S) = min { dim U | S ≤ U, A U ⊆ U + B }`.

Given `Φ : V →ₗ[K] V`, submodules `C, T`, with `M = T ⊔ C` and `π : V → V ⧸ M`:

* a linear section `s` of `π`,
* a feasible `U'` at level 1 (`T' ≤ U'`),
* a correction map `σ : U' → M` with `π (Φ (s u + σ u)) ∈ U'` for all `u ∈ U'`,

give a subspace `U = T ⊔ (s + σ) '' U'` that is admissible (`Φ U ≤ U ⊔ C`) and satisfies
`dim U = dim T + dim U'`.
-/
namespace PRec

open Submodule

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V] [FiniteDimensional K V]

/-- **Construction step of the `(≤)` half** (with `σ` given). -/
theorem lift_admissible (Φ : V →ₗ[K] V) (C T : Submodule K V)
    (s : V Q (T ⊔ C) →ₗ[K] V) (hs : (T ⊔ C).mkQ.comp s = LinearMap.id)
    (U' : Submodule K (V Q (T ⊔ C))) (σ : U' →ₗ[K] ↥(T ⊔ C))
    (hT' : Submodule.map (T ⊔ C).mkQ (Submodule.map Φ T) ≤ U')
    (hσ : ∀ u : U', (T ⊔ C).mkQ (Φ (s u + (σ u : V))) ∈ U') :
    ∃ U : Submodule K V,
      T ≤ U ∧ Submodule.map Φ U ≤ U ⊔ C ∧
        Module.finrank K ↥U = Module.finrank K ↥T + Module.finrank K ↥U' := by
  set F : U' →ₗ[K] V := s.comp U'.subtype + (Submodule.subtype (T ⊔ C)).comp σ with hF
  set E : Submodule K V := LinearMap.range F with hE
  have hπs : ∀ u : U', (T ⊔ C).mkQ (s u) = (u : V Q (T ⊔ C)) := by
    intro u
    rw [← LinearMap.comp_apply, hs, LinearMap.id_apply]
  have hπσ : ∀ u : U', (T ⊔ C).mkQ (σ u : V) = 0 := by
    intro u
    have hmem : (σ u : V) ∈ (T ⊔ C).mkQ.ker := by
      rw [Submodule.ker_mkQ]
      exact (σ u).2
    exact LinearMap.mem_ker.mp hmem
  have hπF : ∀ u : U', (T ⊔ C).mkQ (F u) = (u : V Q (T ⊔ C)) := by
    intro u
    simp only [hF, LinearMap.add_apply, LinearMap.comp_apply, Submodule.subtype_apply]
    rw [map_add, hπs u, hπσ u, add_zero]
  have hπE : Submodule.map (T ⊔ C).mkQ E = U' := by
    rw [hE]
    ext x
    constructor
    · intro hx
      rw [Submodule.mem_map] at hx
      obtain ⟨y, ⟨u, rfl⟩, rfl⟩ := hx
      rw [hπF u]
      exact u.2
    · intro hx
      exact Submodule.mem_map.mpr ⟨F ⟨x, hx⟩, ⟨⟨x, hx⟩, rfl⟩, hπF ⟨x, hx⟩⟩
  have hcomap : Submodule.comap (T ⊔ C).mkQ U' ≤ (T ⊔ E) ⊔ C := by
    rw [← hπE, Submodule.comap_map_eq, Submodule.ker_mkQ]
    refine sup_le ?_ ?_
    · exact le_sup_right.trans le_sup_left
    · refine sup_le ?_ ?_
      · exact le_sup_left.trans le_sup_left
      · exact le_sup_right
  refine ⟨T ⊔ E, le_sup_left, ?_, ?_⟩
  · have hTpart : Submodule.map Φ T ≤ (T ⊔ E) ⊔ C := by
      exact le_trans (Submodule.map_le_iff_le_comap.mp hT') hcomap
    have hEpart : Submodule.map Φ E ≤ (T ⊔ E) ⊔ C := by
      rw [Submodule.map_le_iff_le_comap]
      intro x hxE
      rw [hE, LinearMap.mem_range] at hxE
      obtain ⟨u, rfl⟩ := hxE
      rw [Submodule.mem_comap]
      have hx' : Φ (F u) ∈ Submodule.comap (T ⊔ C).mkQ U' := by
        rw [Submodule.mem_comap]
        exact hσ u
      exact hcomap hx'
    calc Submodule.map Φ (T ⊔ E)
        = Submodule.map Φ T ⊔ Submodule.map Φ E := Submodule.map_sup ..
      _ ≤ ((T ⊔ E) ⊔ C) ⊔ ((T ⊔ E) ⊔ C) := sup_le_sup hTpart hEpart
      _ = (T ⊔ E) ⊔ C := sup_idem _
  · have hinj : Function.Injective F := by
      intro a b hab
      have h := congrArg (T ⊔ C).mkQ hab
      rw [hπF a, hπF b] at h
      exact Subtype.ext h
    have hker : F.ker = ⊥ := LinearMap.ker_eq_bot.mpr hinj
    have hEfin : Module.finrank K ↥E = Module.finrank K ↥U' := by
      rw [hE]
      have h1 := LinearMap.finrank_range_add_finrank_ker F
      rw [hker, finrank_bot, add_zero] at h1
      exact h1
    have hEM : E ⊓ (T ⊔ C) = ⊥ := by
      rw [hE, eq_bot_iff]
      rintro x ⟨hx, hxM⟩
      rw [Submodule.mem_bot]
      obtain ⟨u, rfl⟩ := hx
      have h0 : (T ⊔ C).mkQ (F u) = 0 := by
        have : F u ∈ (T ⊔ C).mkQ.ker := by
          rw [Submodule.ker_mkQ]
          exact hxM
        exact LinearMap.mem_ker.mp this
      rw [hπF u] at h0
      have hu : (u : V Q (T ⊔ C)) = 0 := h0
      have : u = 0 := Subtype.ext hu
      rw [this]
      simp
    have hTE : T ⊓ E = ⊥ := by
      rw [eq_bot_iff]
      intro x hx
      rw [Submodule.mem_inf] at hx
      have hx' : x ∈ E ⊓ (T ⊔ C) := ⟨hx.2, (le_sup_left : T ≤ T ⊔ C) hx.1⟩
      rw [hEM] at hx'
      exact hx'
    have hdim := Submodule.finrank_sup_add_finrank_inf_eq T E
    rw [hTE, finrank_bot, hEfin, add_zero] at hdim
    linarith [hdim]

end PRec
'''


def main():
    out = SRC.replace(" Q ", " " + Q + " ").replace("Q (T", Q + " (T")
    path = os.path.join("tools", "lean", "PRecursionLift3.lean")
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(out)
    data = out.encode("utf-8")
    print("wrote", path, len(data), "bytes")
    print("U+29F8 count:", out.count(Q))
    print("U+2294 count:", out.count("\u2294"))


if __name__ == "__main__":
    main()
