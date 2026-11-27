/-
Q1Paper/PaperII/MainTheorems.lean

Entry point of Paper II's Lean development: the interface layer, the sandwich in
both directions (complex designs), monotonicity, saturation, the spectral lower
bound, the minimum-order theorem, and the graph-extension part of tightness.

Scope note: the statements concerning `PaperI.DEC` over `ℂ` (complex free blocks)
are the field-generic counterpart of the paper's real-design specification
`DECℂ`.  For `DECℂ` the forward direction (`decC_to_feasible`) and monotonicity
(`decC_mono`) are proved; the converse needs the real-compression lemma, tracked
in `workspace/paper_split/PAPER_II_LEAN_PLAN.md` §8.5.
-/

import Q1Paper.PaperII.Interface
import Q1Paper.PaperII.Sandwich
import Q1Paper.PaperII.Monotone
import Q1Paper.PaperII.LowerBound
import Q1Paper.PaperII.Converse
import Q1Paper.PaperII.Saturate
import Q1Paper.PaperII.MinOrder
import Q1Paper.PaperII.GraphExtension
import Q1Paper.PaperII.GraphExtract
import Q1Paper.PaperII.Realification
import Q1Paper.PaperII.Tightness
