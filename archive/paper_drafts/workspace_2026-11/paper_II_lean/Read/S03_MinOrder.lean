import Q1Paper.PaperII.MainTheorems

/-!
Q1Paper/PaperII/Read/S03_MinOrder.lean

§III  The minimum order `q_min = r₀ + t_min` (complex designs).

This file contains **no proofs**: a reading entry in proof order, one `#check` per step.

## What it consumes

Monotonicity and saturation from `S02_Sandwich.lean`.

## What it proves

- `tMin` is the least `t` at which a feasible `W` exists; `t_min ≤ r` iff a design of `r`
  rows exists — `tMin_le_iff_dec`.
- The least feasible order is itself feasible (`dec_sInf_tMinSet`), and the abstract
  least-element statement for monotone predicates (`exists_least_of_monotone`).
- The a priori bound `t_min ≤ 2ℓ` (`tMin_le_two_ell`, via `omega_le_ell`/`t_le_two_ell`).

## The result

- `Q1Paper.PaperII.tMin_le_iff_dec`
- `Q1Paper.PaperII.dec_sInf_tMinSet`, `Q1Paper.PaperII.exists_least_of_monotone`
- `Q1Paper.PaperII.tMin_le_two_ell`, `Q1Paper.PaperII.omega_le_ell`, `Q1Paper.PaperII.t_le_two_ell`
-/

#check @Q1Paper.PaperII.tMin_le_iff_dec
#check @Q1Paper.PaperII.tMin_le_two_ell
#check @Q1Paper.PaperII.dec_sInf_tMinSet
#check @Q1Paper.PaperII.exists_least_of_monotone
#check @Q1Paper.PaperII.omega_le_ell
#check @Q1Paper.PaperII.t_le_two_ell
