/-
Q1Paper/PaperII/Claims.lean

The paper interface of Paper II's formalisation: the paper's items in the paper's
order, each with the declarations that prove it.

This file is narration only — it declares nothing.  `ClaimsCheck.lean` machine-checks
that every name below resolves, so a rename breaks the build instead of silently
invalidating this table.

Scope.  Items marked "(Paper I)" are proved in the Paper I tree and reused here
through the column split `Φ` (`Interface.lean`).  Items concerning `DEC` are
stated for the field-generic predicate over `ℂ` (complex free blocks); the
real-design specification `DECℂ` has its forward direction and monotonicity
proved through the real-compression lemma `real_compress`, so both the forward and the
converse directions are available for `DECℂ` (the residual boundary is the single-`↔`
packaging of Proposition 3 and the real-design form of its tightness criterion).
-/

/-! ## §II Standing results (from Paper I, reused)

* **Claim 4, forward** (`lem:sandwich`): `row(L₀M) ⊆ row(LM) ⊆ row M` and
  `dim row(LM) ≤ dim row(L₀M) + r` — `Q1Paper.claim4_sandwich`.
* **Claim 4, converse** (`lem:sandwich`): every subspace of the sandwich with
  `dim W ≤ dim W₀ + r` is `row([L₀;R] M)` for some `R` with `r` rows —
  `Q1Paper.claim4_converse`.
* **Claim 5** (`lem:W-conditions`): (5a) and (5b) depend only on `W = row[H H_A]` —
  `Q1Paper.claim5_conditions_depend_on_W`.
* **Claim 6** (`lem:struct`): `ω + 1 ≤ dim W ≤ 2ω` for a feasible `W` with
  `ω > 0` — `Q1Paper.claim6_struct`.
-/

/-! ## §II Paper II's own interface

* **`t = dim (W/W₀)`**, with `t ≤ r ↔ dim W ≤ dim W₀ + r` (the hypothesis form of
  Claim 4) — `Q1Paper.PaperII.t`, `t_eq_finrank_sub`, `t_le_iff`.
* **The two encodings agree**: `row([L]·[N AN])` splits into the row pairs —
  `Q1Paper.PaperII.map_rowSpace_Mcol`.
* **Feasibility is the pair of compressed conditions** —
  `Q1Paper.PaperII.isFeasible_pairRowSpace_iff`.
-/

/-! ## §III The sandwich in Paper II's form

* **Forward, `DECℂ`**: a feasible real design of order `r₀ + r` gives a feasible
  `W` with `t ≤ r` — `Q1Paper.PaperII.decC_to_feasible`.
* **Forward, `DEC`** (complex designs) — `Q1Paper.PaperII.DEC_to_feasible_c`.
* **Converse** (complex designs): a feasible `W` with `W₀ ≤ W ≤ T` and `t ≤ r`
  gives `DEC r` — `Q1Paper.PaperII.feasible_to_DEC`.
-/

/-! ## §III Monotonicity and saturation

* **Claim 5, monotone, `DECℂ`**: `DECℂ r → DECℂ r'` for `r ≤ r'` —
  `Q1Paper.PaperII.decC_mono`.
* **Claim 5, monotone, `DEC`** — `Q1Paper.PaperII.dec_mono_complex`.
* **Claim 5, saturation**: `DEC r ↔ DEC m` for `m = dim (T/W₀) ≤ r` —
  `Q1Paper.PaperII.dec_saturates`.
-/

/-! ## §III Minimum order

* **Prop 1, minimum order**: `t_min ≤ r ↔ DEC (r₀ + r)`, i.e. `q_min = r₀ + t_min`
  (`t_min = ⊤` when infeasible) — `Q1Paper.PaperII.tMin_le_iff_dec`.
* **Prop 1, a priori bound**: `t_min ≤ 2ℓ`, `ℓ = rank(A N)` —
  `Q1Paper.PaperII.tMin_le_two_ell` (and `omega_le_ell`, `t_le_two_ell`).
* **Prop 1, the real-design bounds**: `t_min^ℝ ≤ 2ℓ` (`tMinC_le_two_ell`), the
  spectral lower bound `a + 1 − s₀ ≤ t_min^ℝ` (`le_tMinC_of_lowerBound`), and
  `t_min ≤ t_min^ℝ` (`tMin_le_tMinC`).
* **Prop 1, minimum order, real designs (`DECℂ`)**: `t_min^ℝ ≤ r ↔ DECℂ r`, where
  `t_min^ℝ = tMinC` is the least quotient dimension over feasible **real** designs
  (`Q1Paper.PaperII.tMinC_le_iff_decC`), and the least feasible real order is itself
  feasible (`decC_sInf_tMinCSet`).
* **Claim 5, saturation, real designs (`DECℂ`)**: `DECℂ r` at the saturation order
  `m = dim (T/W₀)`, via `real_compress` + `feasible_to_decC` + `decC_mono` —
  `Q1Paper.PaperII.decC_saturates` (and `decC_to_feasible_design`).
* **Real-design bridges** (for the `DECℂ` upgrade): the pair row space is the
  `Φ`-image of the encoded row space (`pairRows`, `pairRowSpace_eq_map_pairRows`), its
  dimension is the encoded matrix's rank (`finrank_pairRowSpace_eq_rank`), and the
  encoding commutes with complexification (`pairRows_map`, `Mcol_map`).
* **Prop 2 as a bound on the minimum order** (`eq:qmin-lb`): `a − s₀ + 1 ≤ t_min`
  whenever every feasible `W` has `ω > 0` — `Q1Paper.PaperII.le_tMin_of_lowerBound`.
* **Theorem 4, correctness half** (the interface): the least feasible order is itself
  feasible — `Q1Paper.PaperII.dec_sInf_tMinSet`; the ordering is
  `Q1Paper.PaperII.tMin_le_iff_dec`, and the abstract least-element statement is
  `Q1Paper.PaperII.exists_least_of_monotone`.  The `O(log(ℓ+2))` call count is not
  formalised.
-/

/-! ## §III The spectral lower bound

* **Prop 2**: `rank[U₀;V₀] + 1 ≤ s₀ + t` for a feasible `W` with `ω > 0`, hence
  `rank[U₀;V₀] − s₀ + 1 ≤ t` — `Q1Paper.PaperII.lowerBound_core`,
  `lowerBound_sub`.
* **Prop 3, numerical half**: if `dim W = rank[U₀;V₀] + 1` (and `s₀ ≤ rank[U₀;V₀]`),
  then `t = rank[U₀;V₀] − s₀ + 1`, i.e. the bound is attained —
  `Q1Paper.PaperII.t_eq_of_finrank`.
* **Prop 3, the `(G,b)` direction**: for `W(G,b) = {(h, Gh + αb)}` one has
  `π₁W = U`, `π₂W ≤ U`, `dim W = dim U + 1` (`graphExt`, `graphExt_pi1`,
  `graphExt_pi2_le`, `graphExt_finrank`), the pencil identity
  `πλ W(G,b) = (λI−G)U + span{b}` (`graphExt_piLam`), hence the paper's rank
  condition `rank[λI−G  b] = dim U` makes `W(G,b)` feasible (`graphExt_feasible`),
  and then `t = dim U + 1 − s₀` (`t_eq_of_graph`): the lower bound is attained.
* **Prop 3, the converse direction**: a feasible `W` with `dim W = dim (π₁W) + 1`
  is `W(G,b)` for some `b ≠ 0` and linear `G`
  (`Q1Paper.PaperII.exists_graph_representation`, via the section of `π₁|_W` and
  its one-dimensional kernel).
* **Prop 3, the composed criterion** (complex designs): the two directions are
  `tMin_eq_of_graph` (`(G,b)` ⇒ `t_min = a + 1 − s₀`) and `exists_graph_of_tMin_eq`
  (`t_min = a + 1 − s₀` ⇒ the data), with the identification `π₁W = U₀+V₀` at an
  attaining `W` in `pi1_eq_sup_of_finrank`.  (Packaging them into a single `↔` with
  `G` typed on `U₀+V₀` needs a transport along that identification; the two
  directions are what is proved.)
-/
