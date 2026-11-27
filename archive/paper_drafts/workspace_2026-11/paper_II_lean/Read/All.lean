import Q1Paper.PaperII.Read.S01_Standing
import Q1Paper.PaperII.Read.S02_Sandwich
import Q1Paper.PaperII.Read.S03_MinOrder
import Q1Paper.PaperII.Read.S04_LowerBound
import Q1Paper.PaperII.Read.S05_Tightness
import Q1Paper.PaperII.Read.S06_RealDesigns

/-!
Q1Paper/PaperII/Read/All.lean

Reading entry for Paper II, in the paper's order: the standing results and the interface
(`S01`), the sandwich with monotonicity and saturation (`S02`), the minimum order (`S03`), the
spectral lower bound (`S04`), tightness (`S05`), and the real-design specification (`S06`).

Each section file contains **no proofs**: it lists that section's steps in proof order, each
with a `#check` of the declaration that carries it, so that a rename breaks the build instead of
silently rotting the map.  The claim table is `Q1Paper/PaperII/Claims.lean` (narrative) and
`ClaimsCheck.lean` (machine-checked); the axiom footprint is `Audit.lean`; the module index is
`Q1Paper/PaperII/MODULES.md`; the reader-facing claim table is `Q1Paper/PaperII/CLAIMS.md`.
-/
