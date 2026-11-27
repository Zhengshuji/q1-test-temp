/-
Q1Paper/PaperII/Audit.lean

The axiom footprint of every declaration of Paper II's Lean development.

Generated from the `PaperII/` sources (declaration names only).  Every audited
declaration must depend only on `propext`, `Classical.choice` and `Quot.sound`.
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

-- Converse.lean
#print axioms Q1Paper.PaperII.WRc
#print axioms Q1Paper.PaperII.WRc_eq_map
#print axioms Q1Paper.PaperII.map_symm_map
#print axioms Q1Paper.PaperII.feasible_to_DEC

-- GraphExtension.lean
#print axioms Q1Paper.PaperII.graphMap
#print axioms Q1Paper.PaperII.graphExt
#print axioms Q1Paper.PaperII.mem_graphExt
#print axioms Q1Paper.PaperII.graphExt_pi1
#print axioms Q1Paper.PaperII.graphExt_pi2_le
#print axioms Q1Paper.PaperII.graphExt_finrank
#print axioms Q1Paper.PaperII.graphPencil
#print axioms Q1Paper.PaperII.graphPencil_apply
#print axioms Q1Paper.PaperII.graphExt_piLam
#print axioms Q1Paper.PaperII.graphExt_feasible
#print axioms Q1Paper.PaperII.t_eq_of_graph

-- GraphExtract.lean
#print axioms Q1Paper.PaperII.projW
#print axioms Q1Paper.PaperII.projW_range
#print axioms Q1Paper.PaperII.projU
#print axioms Q1Paper.PaperII.projU_surjective
#print axioms Q1Paper.PaperII.ker_finrank_eq_one
#print axioms Q1Paper.PaperII.exists_kernel_direction
#print axioms Q1Paper.PaperII.exists_kernel_b
#print axioms Q1Paper.PaperII.exists_graph_representation

-- Interface.lean
#print axioms Q1Paper.PaperII.Mcol
#print axioms Q1Paper.PaperII.Φ
#print axioms Q1Paper.PaperII.Mcol_left
#print axioms Q1Paper.PaperII.Mcol_right
#print axioms Q1Paper.PaperII.Φ_apply
#print axioms Q1Paper.PaperII.Φ_vecMul
#print axioms Q1Paper.PaperII.map_rowSpace_Mcol
#print axioms Q1Paper.PaperII.t
#print axioms Q1Paper.PaperII.t_eq_finrank_sub
#print axioms Q1Paper.PaperII.t_le_iff
#print axioms Q1Paper.PaperII.DecOrder
#print axioms Q1Paper.PaperII.IsFeasible
#print axioms Q1Paper.PaperII.isFeasible_pairRowSpace_iff

-- LowerBound.lean
#print axioms Q1Paper.PaperII.finrank_sup_pi_le
#print axioms Q1Paper.PaperII.finrank_pi1_mono
#print axioms Q1Paper.PaperII.lowerBound_core
#print axioms Q1Paper.PaperII.lowerBound_sub
#print axioms Q1Paper.PaperII.t_eq_of_finrank

-- MinOrder.lean
#print axioms Q1Paper.PaperII.tMinSet
#print axioms Q1Paper.PaperII.tMin
#print axioms Q1Paper.PaperII.tMin_le_iff_dec
#print axioms Q1Paper.PaperII.ell
#print axioms Q1Paper.PaperII.omega_le_ell
#print axioms Q1Paper.PaperII.t_le_two_ell
#print axioms Q1Paper.PaperII.tMin_le_two_ell
#print axioms Q1Paper.PaperII.dec_sInf_tMinSet
#print axioms Q1Paper.PaperII.exists_least_of_monotone
#print axioms Q1Paper.PaperII.le_tMin_of_lowerBound
#print axioms Q1Paper.PaperII.le_tMin_of_lowerBound_max

-- Monotone.lean
#print axioms Q1Paper.PaperII.pairRowSpace_fromRows
#print axioms Q1Paper.PaperII.pairRowSpace_pad
#print axioms Q1Paper.PaperII.decC_mono_add
#print axioms Q1Paper.PaperII.decC_mono

-- Realification.lean
#print axioms Q1Paper.PaperII.pairRows
#print axioms Q1Paper.PaperII.Φ_pairRows
#print axioms Q1Paper.PaperII.pairRowSpace_eq_map_pairRows
#print axioms Q1Paper.PaperII.finrank_pairRowSpace_eq_rank
#print axioms Q1Paper.PaperII.pairRows_map
#print axioms Q1Paper.PaperII.mul_pairRows
#print axioms Q1Paper.PaperII.WR_eq_map_complex
#print axioms Q1Paper.PaperII.finrank_WR_eq
#print axioms Q1Paper.PaperII.finrank_W0_eq
#print axioms Q1Paper.PaperII.phi
#print axioms Q1Paper.PaperII.rowSpace_map_complex
#print axioms Q1Paper.PaperII.real_compress
#print axioms Q1Paper.PaperII.feasible_to_decC
#print axioms Q1Paper.PaperII.decC_to_feasible_design
#print axioms Q1Paper.PaperII.decC_saturates
#print axioms Q1Paper.PaperII.tMinCSet
#print axioms Q1Paper.PaperII.tMinC
#print axioms Q1Paper.PaperII.tMinC_le_iff_decC
#print axioms Q1Paper.PaperII.decC_sInf_tMinCSet
#print axioms Q1Paper.PaperII.tMinC_le_two_ell
#print axioms Q1Paper.PaperII.UC
#print axioms Q1Paper.PaperII.finrank_UC
#print axioms Q1Paper.PaperII.WR_le_TR
#print axioms Q1Paper.PaperII.tMin_le_tMinC
#print axioms Q1Paper.PaperII.le_tMinC_of_lowerBound

-- Sandwich.lean
#print axioms Q1Paper.PaperII.Ac
#print axioms Q1Paper.PaperII.L0c
#print axioms Q1Paper.PaperII.Rc
#print axioms Q1Paper.PaperII.Lc
#print axioms Q1Paper.PaperII.fromRows_Lc
#print axioms Q1Paper.PaperII.TR
#print axioms Q1Paper.PaperII.W0
#print axioms Q1Paper.PaperII.WR
#print axioms Q1Paper.PaperII.W0_eq_map
#print axioms Q1Paper.PaperII.TR_eq_map
#print axioms Q1Paper.PaperII.WR_eq_map
#print axioms Q1Paper.PaperII.decC_to_feasible

-- Saturate.lean
#print axioms Q1Paper.PaperII.DEC_to_feasible_c
#print axioms Q1Paper.PaperII.t_le_t_of_le
#print axioms Q1Paper.PaperII.dec_saturates
#print axioms Q1Paper.PaperII.dec_mono_complex

-- Tightness.lean
#print axioms Q1Paper.PaperII.omega_pos_of_nonzero
#print axioms Q1Paper.PaperII.W0_ne_bot_of_pos
#print axioms Q1Paper.PaperII.pi1_eq_sup_of_finrank
#print axioms Q1Paper.PaperII.tMin_eq_of_graph
#print axioms Q1Paper.PaperII.exists_graph_of_tMin_eq
#print axioms Q1Paper.PaperII.UV
#print axioms Q1Paper.PaperII.UV_eq
#print axioms Q1Paper.PaperII.mem_tMinSet
#print axioms Q1Paper.PaperII.tMin_le_of_feasible

