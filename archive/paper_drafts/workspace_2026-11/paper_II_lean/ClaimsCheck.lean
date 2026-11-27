/-
Q1Paper/PaperII/ClaimsCheck.lean

Machine-checked index: one `#check` per item of `Claims.lean`.  A rename breaks
this build instead of silently invalidating the claims table.
-/

import Q1Paper.PaperII.MainTheorems

-- §II  Standing results (from Paper I, reused)
#check @Q1Paper.claim3_attainable
#check @Q1Paper.PaperI.DEC_iff_compressed
#check @Q1Paper.claim4_sandwich
#check @Q1Paper.claim4_converse
#check @Q1Paper.claim5_conditions_depend_on_W
#check @Q1Paper.claim6_struct

-- §II  Paper II's own interface
#check @Q1Paper.PaperII.t
#check @Q1Paper.PaperII.t_eq_finrank_sub
#check @Q1Paper.PaperII.t_le_iff
#check @Q1Paper.PaperII.map_rowSpace_Mcol
#check @Q1Paper.PaperII.isFeasible_pairRowSpace_iff

-- §III  The sandwich in Paper II's form
#check @Q1Paper.PaperII.decC_to_feasible
#check @Q1Paper.PaperII.DEC_to_feasible_c
#check @Q1Paper.PaperII.feasible_to_DEC

-- §III  Monotonicity and saturation
#check @Q1Paper.PaperII.decC_mono
#check @Q1Paper.PaperII.dec_mono_complex
#check @Q1Paper.PaperII.dec_saturates

-- §III  Minimum order
#check @Q1Paper.PaperII.tMin_le_iff_dec
#check @Q1Paper.PaperII.tMin_le_two_ell
#check @Q1Paper.PaperII.le_tMin_of_lowerBound
#check @Q1Paper.PaperII.le_tMin_of_lowerBound_max
#check @Q1Paper.PaperII.pairRows
#check @Q1Paper.PaperII.pairRowSpace_eq_map_pairRows
#check @Q1Paper.PaperII.finrank_pairRowSpace_eq_rank
#check @Q1Paper.PaperII.pairRows_map
#check @Q1Paper.PaperII.mul_pairRows
#check @Q1Paper.PaperII.WR_eq_map_complex
#check @Q1Paper.PaperII.finrank_WR_eq
#check @Q1Paper.PaperII.real_compress
#check @Q1Paper.PaperII.feasible_to_decC
#check @Q1Paper.PaperII.decC_saturates
#check @Q1Paper.PaperII.tMinC
#check @Q1Paper.PaperII.tMinC_le_iff_decC
#check @Q1Paper.PaperII.decC_sInf_tMinCSet
#check @Q1Paper.PaperII.tMinC_le_two_ell
#check @Q1Paper.PaperII.WR_le_TR
#check @Q1Paper.PaperII.tMin_le_tMinC
#check @Q1Paper.PaperII.le_tMinC_of_lowerBound
#check @Q1Paper.PaperII.UC
#check @Q1Paper.PaperII.finrank_UC
#check @Q1Paper.PaperII.dec_sInf_tMinSet
#check @Q1Paper.PaperII.exists_least_of_monotone
#check @Q1Paper.PaperII.omega_le_ell
#check @Q1Paper.PaperII.t_le_two_ell

-- §III  The spectral lower bound
#check @Q1Paper.PaperII.lowerBound_core
#check @Q1Paper.PaperII.lowerBound_sub
#check @Q1Paper.PaperII.t_eq_of_finrank
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
