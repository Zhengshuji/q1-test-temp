import Q1Paper.PaperII.MainTheorems

/-!
Q1Paper/PaperII/Read/S02_Sandwich.lean

§III  The sandwich, monotonicity and saturation.

This file contains **no proofs**: it is a reading entry, in proof order, with one `#check`
per step.

## What it consumes

The split `Φ` and the quotient dimension `t` from `S01_Standing.lean`.

## What it proves

1. **The sandwich, forward.**  A design of `r` rows produces a `W` with `W₀ ⊆ W ⊆ T` and
   `t ≤ r` — `decC_to_feasible`.
2. **The sandwich, converse (complex designs).**  Every feasible `W` of the sandwich with
   `t = dim(W/W₀)` is realised by a design at that order — `feasible_to_DEC`.
3. **Monotonicity.**  `DECℂ r → DECℂ r'` for `r ≤ r'` — `decC_mono`.
4. **Saturation.**  From `DECℂ r` one gets `DECℂ m` with `m = dim(T/W₀)` — the largest order
   that can ever be needed — `dec_saturates` (complex designs) and later `decC_saturates`
   (real designs, `S06_RealDesigns.lean`).

## The result

- `Q1Paper.PaperII.decC_to_feasible`, `Q1Paper.PaperII.feasible_to_DEC`
- `Q1Paper.PaperII.decC_mono`, `Q1Paper.PaperII.dec_mono_complex`
- `Q1Paper.PaperII.dec_saturates`
-/

#check @Q1Paper.PaperII.decC_to_feasible
#check @Q1Paper.PaperII.DEC_to_feasible_c
#check @Q1Paper.PaperII.feasible_to_DEC

#check @Q1Paper.PaperII.decC_mono
#check @Q1Paper.PaperII.dec_mono_complex
#check @Q1Paper.PaperII.dec_saturates
