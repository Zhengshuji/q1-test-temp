import Q1Paper.PaperII.MainTheorems

/-!
Q1Paper/PaperII/Read/S01_Standing.lean

§II  Standing results and Paper II's interface.

This file contains **no proofs**: it is a reading entry that lists the steps in proof order,
each with the declaration that carries it.  Every step is a `#check`, so a rename breaks the
build instead of silently rotting the map.

## What it sets up

Paper II works on the pair encoding `W = row[H  H_A]`.  The column split `Φ` reads a pair
space as row pairs, and `t = dim(W/W₀)` is the quotient dimension that the order counts.

The structural statements of the companion paper enter through this split: the sandwich
`W₀ ⊆ W ⊆ T`, its converse (every subspace of the sandwich of the right dimension is realised
by a free block), the fact that (5a)/(5b) depend only on `W`, and the bound
`ω + 1 ≤ dim W ≤ 2ω`.

## The result

- `Q1Paper.claim4_sandwich`, `Q1Paper.claim4_converse`
- `Q1Paper.claim5_conditions_depend_on_W`, `Q1Paper.claim6_struct`
- `Q1Paper.PaperII.t`, `Q1Paper.PaperII.t_eq_finrank_sub`, `Q1Paper.PaperII.t_le_iff`
- `Q1Paper.PaperII.map_rowSpace_Mcol`, `Q1Paper.PaperII.isFeasible_pairRowSpace_iff`
-/

#check @Q1Paper.claim4_sandwich
#check @Q1Paper.claim4_converse
#check @Q1Paper.claim5_conditions_depend_on_W
#check @Q1Paper.claim6_struct

#check @Q1Paper.PaperII.t
#check @Q1Paper.PaperII.t_eq_finrank_sub
#check @Q1Paper.PaperII.t_le_iff
#check @Q1Paper.PaperII.map_rowSpace_Mcol
#check @Q1Paper.PaperII.isFeasible_pairRowSpace_iff
