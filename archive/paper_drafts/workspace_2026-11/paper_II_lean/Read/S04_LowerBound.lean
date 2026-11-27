import Q1Paper.PaperII.MainTheorems

/-!
Q1Paper/PaperII/Read/S04_LowerBound.lean

§III  The spectral lower bound.

This file contains **no proofs**: a reading entry in proof order, one `#check` per step.

## What it proves

- **Proposition 2** (a computable lower bound): for a feasible `W` with `t = dim(W/W₀)` and
  `ω = dim π₁W > 0`, one has `rank[U₀;V₀] ≤ ω ≤ s₀ + t − 1` — `lowerBound_core`, and in the
  subtraction form `lowerBound_sub`.
- **The a priori bound in the paper's `max` form**: `a + 1 − s₀ ≤ t_min`, without a side
  condition on `s₀ ≤ a` — `le_tMin_of_lowerBound_max` (the version with the side condition is
  `le_tMin_of_lowerBound`).
- **The numerical half of Proposition 3**: `dim W = dim π₁W + 1` forces
  `t = a − s₀ + 1` — `t_eq_of_finrank`.

## The result

- `Q1Paper.PaperII.lowerBound_core`, `Q1Paper.PaperII.lowerBound_sub`
- `Q1Paper.PaperII.le_tMin_of_lowerBound`, `Q1Paper.PaperII.le_tMin_of_lowerBound_max`
- `Q1Paper.PaperII.t_eq_of_finrank`
-/

#check @Q1Paper.PaperII.lowerBound_core
#check @Q1Paper.PaperII.lowerBound_sub
#check @Q1Paper.PaperII.le_tMin_of_lowerBound
#check @Q1Paper.PaperII.le_tMin_of_lowerBound_max
#check @Q1Paper.PaperII.t_eq_of_finrank
