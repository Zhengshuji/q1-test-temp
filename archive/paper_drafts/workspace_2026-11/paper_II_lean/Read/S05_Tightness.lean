import Q1Paper.PaperII.MainTheorems

/-!
Q1Paper/PaperII/Read/S05_Tightness.lean

§III  When the bound is attained (Proposition 3, complex designs).

This file contains **no proofs**: a reading entry in proof order, one `#check` per step.

## What it consumes

The lower bound and the numerical half from `S04_LowerBound.lean`.

## What it proves

1. **The graph extension `W(G,b)`** and its projections: `π₁W(G,b) = U`,
   `π₂W(G,b) ≤ U`, `dim W(G,b) = dim U + 1` — `graphExt`, `graphExt_pi1`, `graphExt_pi2_le`,
   `graphExt_finrank`.
2. **Its pencil and feasibility**: `π_λ W(G,b) = (λI − G)U + span{b}` — `graphExt_piLam`;
   the rank condition `rank[λI − G  b] = dim U` makes it feasible — `graphExt_feasible`; and then
   `t = dim U + 1 − s₀` — `t_eq_of_graph`.
3. **The converse**: a feasible `W` with `dim W = dim π₁W + 1` is such a `W(G,b)` —
   `exists_graph_representation`.
4. **The composition**: at an attaining `W`, `π₁W = U₀+V₀` — `pi1_eq_sup_of_finrank`; hence
   a `(G,b)` pair forces `t_min = a + 1 − s₀` — `tMin_eq_of_graph`; and conversely a saturating
   `t_min` produces the data — `exists_graph_of_tMin_eq`.

The two directions are stated separately; a single `↔` packaging is deliberately not provided
(it only adds interface convenience and trips elaboration).

## The result

- `Q1Paper.PaperII.graphExt`, `graphPencil`, `graphExt_pi1`, `graphExt_pi2_le`,
  `graphExt_finrank`, `graphExt_piLam`, `graphExt_feasible`, `t_eq_of_graph`
- `Q1Paper.PaperII.exists_graph_representation`
- `Q1Paper.PaperII.pi1_eq_sup_of_finrank`, `tMin_eq_of_graph`, `exists_graph_of_tMin_eq`
-/

#check @Q1Paper.PaperII.graphExt
#check @Q1Paper.PaperII.graphExt_pi1
#check @Q1Paper.PaperII.graphExt_pi2_le
#check @Q1Paper.PaperII.graphExt_finrank
#check @Q1Paper.PaperII.graphPencil
#check @Q1Paper.PaperII.graphExt_piLam
#check @Q1Paper.PaperII.graphExt_feasible
#check @Q1Paper.PaperII.t_eq_of_graph
#check @Q1Paper.PaperII.exists_graph_representation
#check @Q1Paper.PaperII.pi1_eq_sup_of_finrank
#check @Q1Paper.PaperII.tMin_eq_of_graph
#check @Q1Paper.PaperII.exists_graph_of_tMin_eq
