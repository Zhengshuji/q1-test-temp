# Lean coverage and gap inventory for the three papers

Scope and method. Statements were taken from the theorem-like environments of
`paper/current/paper_I_dec.tex`, `paper/current/paper_II_minorder.tex` and
`paper/current/paper_III_hyperplane.tex` (counted as numbered environments; definitions and
the algorithm environment are not counted as statements). Each statement's status was checked
against the declaration that actually states it, read in the artifact tree
`q1-functional-observer/Q1Paper/` (32 modules), and cross-checked with `paper/LEAN_MAP.md`.
Status vocabulary is the one used by the papers' own evidence tables (all three labelled
`tab:evidence`): *literal* = the Lean statement is the paper's statement; *abstract core* =
linear-map/submodule version, matrix translation paper-level; *ingredient* = one step of a
proof; *none* = no Lean support. Where the papers' tables grade a statement higher than the
declarations warrant, the gap column says so and section 6 lists the corrections.

## 1. Summary

Paper I has **20** numbered statements, **11** with Lean support (4 literal, 4 abstract core,
3 ingredient) and **9** paper-level. Paper II has **11** statements, **6** with Lean support
(1 literal, 4 abstract core, 1 ingredient) and **5** paper-level. Paper III has **24**
statements, **3** with Lean support (2 abstract core, 1 ingredient) and **21** paper-level.
Across the three papers: **55** statements, **20** Lean-backed, **35** paper-level; of the 20,
only **3** are literal without qualification (Paper I `lem:rankid`, `lem:struct`,
`lem:rankcons`-in-rank-form), because two further "literal" grades are conditional
(Paper I `lem:struct` is stated with the projection equality as a hypothesis) or hold over the
wrong base field (Paper I `lem:bezout` is proved only over an algebraically closed field, so it
gives complex multipliers while the paper insists on real ones). The Lean library is strongest
exactly where the papers' structural layer is (rank identities, projections, the sandwich, the
structural bound, the direction theorem of Paper III) and silent wherever the papers' own text
says the content is algorithmic: bit-complexity, real algebraic decisions, Grassmannian
bundles, gcd/subresultant cost, and the existential-real encodings. No module contains `sorry`,
`admit` or a new `axiom`; no module mentions Cauchy–Binet, resultants, Grassmannians,
subresultants, Bareiss, Hadamard, Renegar or controllability, which is why the gaps below are
gaps of infrastructure and not of effort alone.

## 2. Paper I — `paper/current/paper_I_dec.tex`

Counted statements: 20 (13 claims, 2 propositions, 3 theorems, 2 corollaries). Rows: 21,
because `lem:struct` is split into its two halves. Labels are those of the file.

| Paper statement (label/number) | Status | Lean declaration(s) | If none: what is missing | Effort | Question for the expert |
|---|---|---|---|---|---|
| `lem:rankid` Rank identity, eq:rankid | literal | `Q1Paper.rank_vstack_add_rank_mul` (via `rank_fromRows_add_map`, `mulVecLin_range_eq_ker`) | — | — | — |
| `lem:compression` (i)–(iv) Compression and pencil criterion | abstract core | `Q1Paper.ker_compressed_iff`; `Q1Paper.G_form_iff`; `Q1Subspace.rank_of_spectralCondition` | (iii): the equivalence to the maximal minors of the pencil having no common complex root, and to their gcd in R[λ] being a constant — no declaration in the tree uses polynomial gcd at all. (i) is stated in kernel form, not as rank[H_A;H] = rank H, though that bridge exists separately (`Q1Subspace.rank_fromRows_eq_rank_iff`) and is not linked to it | medium | Q4 |
| `lem:attainable` Attainable row pairs, eq:kappa | abstract core | `Q1Paper.freePairSpace`, `finrank_freePairSpace_add_ker`, `finrank_domain_le_freePairSpace`, `FPT.freePairDim_le_kappaObs`, `kappaObs_eq_mul_freePairSpace` | the identification of the matrix row r_i[N AN] with a point of the pair map, and the reading of kappa = r d_0 as a coordinate count (needs the `Matrix.fromRows`/`fromCols` block API); the two halves of k ≤ d_0 ≤ r d_0 exist as separate declarations but are not assembled | small | — |
| `lem:sandwich` Sandwich and realizability | abstract core | `Q1Subspace.rowSpan_fromRows_left`, `Q1Subspace.mem_rowSpan_iff_exists_vecMul` | the converse half — every W with W_0 ⊆ W ⊆ T is realized by a free block of exactly t = dim(W/W_0) rows — and the bound dim(W/W_0) ≤ r. Needs the quotient dimension (`Submodule.finrank_quotient_add_finrank` exists) plus the block bookkeeping. The paper's table calls the row literal; only two of its four clauses are formalized | medium | — |
| `lem:W-conditions` Conditions depend only on W | abstract core | `Q1Subspace.rank_fromRows_eq_rank_iff`, `Q1Subspace.SpectralCondition`, `Q1Step3.spectralCondition_zero` | the π1/π2 formulation of (5a) and the quantification of λ over C for a real pencil: `SpectralCondition H H_A` quantifies over the base field K only, so the real-to-complex passage (rank invariance under scalar extension) must be supplied | medium | Q5 |
| `lem:struct` upper half, dim W ≤ 2ω | literal, conditional | `Q1Subspace.finrank_le_two_mul_of_pi1_eq_pi2` | the equality π1 W = π2 W is a hypothesis; deriving it from (5a) plus (5b) at λ = 0 is available only in given-hypothesis form (`Q1Subspace.pi1_eq_pi2_of_le_of_finrank_eq`), and the rank equality at λ = 0 is not linked to it | small | — |
| `lem:struct` lower half, ω + 1 ≤ dim W | literal | `Q1Subspace.finrank_add_one_le_of_spectral` (`BoundLower.lean`) | — (the eigenvalue step uses `Module.End.exists_eigenvalue` under `IsAlgClosed`). Caveat: `Audit.lean` does not import this module, so the declaration has no `#print axioms` entry | small | — |
| `lem:monotone` Monotonicity, DEC(q) ⇒ DEC(q+1) | ingredient | `Q1Paper.rank_fromRows_zero`, `Q1Paper.rowSpan_fromRows_zero` | carrying H = LN and H_A = LAN through the passage L ↦ [L_0;R], i.e. a `Matrix.fromRows`-multiplication lemma and the double block stacking | small | — |
| `lem:rankcons` Rank consistency | literal (rank form) | `Q1Paper.exists_mulVec_eq_iff_rank_gram`, `Q1Paper.rank_augment_eq_iff`, `Q1Paper.augment_mul_transpose` | the second, disjunctive form via the elementary symmetric functions e_t of the eigenvalues of the PSD matrices Gamma, Gamma': needs eigenvalues of real symmetric matrices and e_j > 0 iff rank ≥ j | medium | — |
| `lem:bezout` Bézout with degree bound | literal only over an algebraically closed field | `Q1Paper.exists_bezout_family`, `Q1Paper.isCoprime_of_no_common_root`, `Q1Paper.exists_bezout_deg_lt` | the paper's point is that the multipliers are **real**, and every one of these three declarations carries `[IsAlgClosed K]`; instantiating at C yields complex multipliers. Missing: coprimality in R[X] from "no common complex root" (a nonconstant real gcd has a complex root), then re-running the assembly over R | medium | Q2 |
| `lem:window` Degree-windowed relations | none | — | the row-space identity row Z = {coef(sum_i g_i f_i) : deg g_i < ω}: a coefficient-vector/linear-map statement with the index set (i,j) and 2ω columns. No declaration mentions the window matrix | medium | — |
| `prop:gram` Gram certificate | ingredient | `Q1Paper.sum_sq_eq_zero_iff` | e_0 in row Z iff there is x with Z^T Z x = e_0 (needs `lem:window` and `lem:bezout`), plus the Cauchy–Binet compression of the K(λ,μ) kernel and the identity (Z^T Z)_{t,t'} = sum_j S_{t-j,t'-j} | large | Q1 |
| `thm:fixedq` Fixed q, polynomial time | none | — | the existential-real formula Phi_{ω,J}, its satisfiability equivalence, and Renegar's Part II bound; no decision procedure and no cost model in the tree | large | Q6 |
| `thm:fpt` FPT in ell | none | — | the Grassmannian charts of V/W_0 with m' ≤ 2ℓ − s_0, the chart count 2^{m'}, and the Renegar count with ℓ as parameter | large | Q3, Q6 |
| `cor:arith` Arithmetic operations | none | — | the arithmetic-operation count; follows from `thm:fpt` once counted | small | — |
| `lem:rationalbasis` Rational bases and annihilators | none | — | fraction-free (Bareiss) elimination and the Hadamard bound on minor bit length, hence the bound tau_M | large | Q6 |
| `lem:coeff` Coefficient sizes | none | — | bit lengths of the minors of λH − H_A and of Z^T Z; Hadamard again, plus Laplace expansion over the λ-columns | large | Q6 |
| `lem:zero` Pencil (i)–(v) | ingredient | `Q1Paper.spoly_mul_pencil_eq_one` ((v) ⇒ (iv)); `Q1Paper.leftInverse_of_bezout`; `Q1Paper.exists_leftInverse_linear` ((ii) ⇒ (iv), algebraically closed) | (iii): gcd in Q[λ] a nonzero constant iff no common complex root; (iv) ⇒ (i): evaluating the polynomial identity at λ and reading off the rank; and again the coefficient field (the paper's (iv) wants S over Q, the Lean implication is over an algebraically closed field) | medium | Q2 |
| `prop:zero` The r = 0 test | none | — | the algorithm: rank factorization H = XB, G = FX, then the `lem:zero` test, with its polynomial cost. Note the paper's table attributes this row to `exists_leftInverse_linear`, which proves existence of a left inverse, not the polynomial-time test | medium | — |
| `thm:existsr` DEC(q) in existential reals | none | — | correctness of the encoding with the blocks X, B, G, X_L, B_R, S_0..S_{2ω−2} and its polynomial size; needs a semantics for real-closed formulas | large | Q6 |
| `cor:time` Time bound | none | — | the minimum of the two bounds; follows from the two theorems | small | — |

## 3. Paper II — `paper/current/paper_II_minorder.tex`

Counted statements: 11 (5 claims, 3 propositions, 1 theorem, 2 corollaries). Labels are those of
the file; the evidence table is the one labelled `tab:evidence` in section VII.

| Paper statement (label/number) | Status | Lean declaration(s) | If none: what is missing | Effort | Question for the expert |
|---|---|---|---|---|---|
| `claim:compress` Compression and pencil form | abstract core | `Q1Paper.ker_compressed_iff`, `Q1Subspace.rank_fromRows_eq_rank_iff`, `Q1Step3.spectralCondition_zero` | the pencil criterion (eq:pencil) as such: rank(λH − H_A) = ω for all complex λ, and the gcd reading. Same gap as Paper I `lem:compression` (iii) | medium | Q4 |
| `claim:rows` Attainable row pairs | abstract core | `Q1Paper.freePairSpace`, `Q1Paper.finrank_freePairSpace_add_ker`, `Q1Paper.kappaObs_eq_mul_freePairSpace` | the matrix realization of r_i[N AN] and the parameter count kappa_obs = r d_0; the row is not listed in this paper's table (statements not listed are called paper-level), but the declarations behind it exist | small | — |
| `claim:sandwich` Sandwich and the subspace reading | abstract core | `Q1Subspace.rowSpan_fromRows_left`, `Q1Subspace.mem_rowSpan_iff_exists_vecMul` | the realization half (free block with exactly t = dim(W/W_0) rows) and hence "DEC(q) iff some such W exists"; quotient bookkeeping again. The paper's table calls the row literal | medium | — |
| `claim:struct` Structural bound | literal, conditional | `Q1Subspace.finrank_le_two_mul_of_pi1_eq_pi2`, `Q1Subspace.finrank_add_one_le_of_spectral` | the projection equality π1 W = π2 W = row H_A, given here as a hypothesis; and the derivation of the spectral hypothesis from (5b) (see Paper I row `lem:W-conditions`) | small | — |
| `lem:monotone` Monotonicity and saturation | ingredient | `Q1Paper.rank_fromRows_zero` | DEC(q) ⇒ DEC(q+1) through the blocks H, H_A, and the saturation argument dim(W/W_0) ≤ dim(T/W_0) = m with the realization half of `claim:sandwich` | small | — |
| `prop:minorder` q_min = r_0 + t_min, t_min ≤ 2ℓ | none | — | the assembly: feasibility as existence of a feasible W of quotient dimension ≤ r, minimality of t_min, and ω ≤ ℓ from row H_A ⊆ S. No declaration states q_min at all | medium | — |
| `prop:lowerbound` A computable lower bound | abstract core | `Q1Subspace.finrank_sup_pi_le`, `Q1Subspace.finrank_pi1_mono` | the first inequality rank[U_0;V_0] ≤ ω is there; missing are the second inequality ω ≤ s_0 + t − 1 (a substitution into the structural bound) and the assembly into eq:lb and eq:qmin-lb | small | — |
| `prop:tight` When the bound is attained | none | — | the pair (G,b) criterion. Its spectral half, rank[λI − G b] = a for all λ, is exactly controllability of the single-input pair (G,b); the tree contains no controllability theory (the paper says so itself) | medium | — |
| `thm:interface` Interface | none | — | the binary search over the window and the solution of t rational systems of size n × 2k; depends on `prop:minorder` and `claim:sandwich` | small | — |
| `cor:opt` OPT | none | — | bit accounting with the companion's f(ℓ) decision cost | small | Q6 |
| `cor:find` FIND, arithmetic model | none | — | the construction step (lifting a basis of W/W_0 to rows); needs the realization half of `claim:sandwich` | medium | — |

## 4. Paper III — `paper/current/paper_III_hyperplane.tex`

Counted statements: 24 (17 claims, 2 propositions, 4 theorems, 1 corollary; the claim with the
three labels `sec4:thm:closed`, `sec4:thm:generic`, `sec4:prop:cover` is one statement with
parts (a)–(c)). The algorithm environment `sec4:algo:decide` is listed for completeness but not
counted. Labels are those of the file; evidence table is the one labelled `tab:evidence`.

| Paper statement (label/number) | Status | Lean declaration(s) | If none: what is missing | Effort | Question for the expert |
|---|---|---|---|---|---|
| `sec4:thm:closed`, `sec4:thm:generic`, `sec4:prop:cover` Standard tools (a)–(c) | none | — | (a) closedness of the bad locus as the projection of an incidence subvariety of the chart times P^1 (an elimination statement); (b) "a piece has a good point iff deg_λ gcd_I m_I = 0 over the function field"; (c) finite-cover bookkeeping | large | Q4 |
| `prop:rankprecheck` rank L_0 < r_0 forces infeasibility | none | — | the rank inequality q = rank L ≤ rank L_0 + (q − r_0); Mathlib's stacked-rank lemmas are enough | small | — |
| `sec3:lem:direction` Structure of the layer (i)–(iv) | ingredient | `Q1Paper.mem_orthogonal_span_pair_iff`, `Q1Paper.Dv_eq_ker`, `Q1Paper.finrank_Dv`, `Q1Paper.le_orthogonal_span_pair` | (i) ker(L restricted to K_0) = K_0 ∩ V^perp = R v and the uniqueness of v; (iv) dim(V ∩ K_0) ≤ ω with equality iff D_v ⊆ V; and the rank{phi_v, phi_Av} form of (iii) | medium | — |
| `sec3:thm:direction` Direction theorem | abstract core | `Q1Paper.compression_eq_of_proportional`, `Q1Paper.proportional_of_compression`, `Q1Paper.direction_iff` | both implications are proved for a given split A v = w + z. Missing: existence of a q-dimensional V with S1–S2, and the consequence that the admissible directions are the union of the projective eigenspaces P(E_mu) (needs eigenvalues of the compression over R plus projective bookkeeping) | medium | Q5 |
| `sec3:lem:prescribed` Prescribed rows (i)–(iii) | abstract core | `Q1Paper.le_orthogonal_span_pair`, `Q1Paper.inf_inf_orthogonal_eq` | (ii) "if every E_mu^0 = 0 the layer is empty", (iii) rank L_0 = r_0 is forced; and the quotient V0bar = (V_0 + D_v)/D_v with delta a quotient dimension | medium | — |
| `sec3:prop:strata` Eigen and non-eigen directions | none | — | dim span{v, Av} is 1 or 2 and dim U_v^perp is n−1 or n−2; the stratum decomposition by rank(A_21 restricted to E_mu^0) and its nonemptiness cases | small | — |
| `sec3:lem:constantrank` Constant rank and the fibre | none | — | the vector bundle v ↦ D_v of constant rank k−1; the quotient bundle U_v^perp/D_v of rank rho or rho−1 per stratum; the fibre as Gr(s−delta, Q_v/V0bar) with dimension (s−delta)(r(v)−s) | large | Q3 |
| `sec3:thm:param` Complete parameterization | none | — | relative Grassmann bundles over a locally closed real algebraic base, irreducibility of each stratum, Zariski density of its real points, and the dimension bookkeeping h_mu^0 − 1 + (s−delta)(rho−s) | large | Q3 |
| `sec3:prop:duality` Direction duality and the fibres of V ↦ W | none | — | W ⊆ a° × a°, [a] = P(Ann U), ker Phi = (K_0 + A K_0)^perp, and the lifts of W as a surjectivity locus inside a Grassmannian | medium | — |
| `sec4:lem:cover` The total charts cover, and are finitely many | none | — | the cover by direction charts times trivializations times Grassmann charts, and the rationality of the resulting entries | medium | — |
| `sec4:lem:minorcount` Size of a chart | none | — | deg_X m_I ≤ ω, deg_λ m_I ≤ ω and the count k C(q,s); the degree half could reuse `Q1Paper.natDegree_det_le` | small | — |
| `sec4:lem:fullrank` Full-rank leading coefficient; dichotomy | none | — | the paper's main new lemma: a positive λ-degree gcd over K(X)[λ], taken primitive by Gauss's lemma, forces a nonconstant common factor at every specialization, using rank H ≡ ω. Needs gcd over a rational function field and specialization of a primitive polynomial | medium | Q4 |
| `sec4:prop:realpoints` Real designs and certificates (a)–(e) | none | — | Zariski density of the real points of a rational chart (a nonzero polynomial has a nonvanishing real point), and the certificate alternatives (Bézout identity versus division identities) | medium | — |
| `sec4:algo:decide` Exact decision for the entire layer | none | — | the procedure itself (not a statement); its correctness is `sec4:prop:correct` and its cost `sec5:thm:poly` | — | — |
| `sec4:prop:correct` Correctness | none | — | the case analysis over the three algorithm exits; depends on `sec4:thm:generic`, `sec4:lem:cover`, `sec4:lem:fullrank`, `sec4:prop:realpoints` | medium | — |
| `sec5:lem:height` Heights of the data, of the roots and of the field | none | — | Bareiss elimination, Hadamard bounds, the primitive normalization, the factor-height (Mignotte) bound, and eigenvector heights over a number field | large | Q6 |
| `sec5:lem:chart` Size of the charts | none | — | at most 2^{2p} charts per fibre, n^{O(p)} maximal minors, degrees ≤ ω ≤ n | large | Q6 |
| `sec5:lem:subres` Cost of the gcd | none | — | the subresultant chain computing the primitive part of the gcd over the fraction field, with Sylvester-minor bit bounds; nothing in the tree computes a polynomial gcd | large | Q6 |
| `sec5:thm:poly` Fixed p, geometrically simple spectrum | none | — | the assembly of the three rows above with factorization (S1), real root isolation (S2) and number-field arithmetic (S3) | large | Q6 |
| `appBC:lem:norm` explicit form of `sec5:lem:height`(a) | none | — | bit lengths of N, N^T N, N^T A N and M | large | Q6 |
| `appBC:lem:charpoly` explicit form of `sec5:lem:height`(b)–(d) | none | — | heights of the characteristic polynomial, of the roots, of the eigenvector bases | large | Q6 |
| `appBC:lem:chart` explicit form of `sec5:lem:chart` | none | — | the explicit chart count and minor count | large | Q6 |
| `appBC:prop:iter` iteration and cost | none | — | the summation of per-chart costs, and the pairwise gcd remark | large | Q6 |
| `sec6:prop:nonconstant` counterexample (n = 8, p = 2, q = 4) | none | — | a finite rational certificate: the two-dimensional real eigenspace E_1, the feasible design over [1:1], the infeasibility over five non-eigen directions. In principle a `decide`/`norm_num` computation over Q; no declaration mentions these matrices | medium | — |
| `sec6:cor:reduction` failure of the representative-direction reduction | none | — | the one-line consequence of `sec6:prop:nonconstant` plus the definition of the reduction | small | — |

## 5. What to formalise next, ranked by value / effort

1. **Paper II: monotonicity and saturation through the blocks (`lem:monotone`, small).** The only
   missing step is a `Matrix.fromRows`-multiplication lemma carrying H = LN and H_A = LAN through
   L ↦ [L_0;R]. Value: it is the load-bearing step of Paper II's main theorem and of its binary
   search, and the rank half is already proved (`rank_fromRows_zero`).
2. **Paper I: real-coefficient Bézout (`lem:bezout`, medium).** Replace `[IsAlgClosed K]` by R:
   prove coprimality in R[X] from absence of a common complex root (a nonconstant real gcd has a
   complex root), then re-run `exists_bezout_family` over R. Value: the certificate chain of
   Paper I and the r = 0 branch both need real multipliers; without this the "literal" grade is
   wrong and `lem:zero` (iii) stays open.
3. **Paper III: eigen versus non-eigen directions (`sec3:prop:strata`, small).** Dimension of
   span{v, Av} and of U_v^perp on the two strata, and the rank criterion for nonemptiness. Value:
   small proof, and every later Paper III statement (fibre, charts, decision) is stratified by it.
4. **Paper II: minimum order (`prop:minorder`, medium).** After 1 and the realization half of
   `claim:sandwich`, the assembly is quotient bookkeeping (`Submodule.finrank_quotient_add_finrank`
   is in Mathlib) plus ω ≤ ℓ. Value: this is Paper II's headline statement.
5. **Paper III: full-rank leading coefficient (`sec4:lem:fullrank`, medium).** Gauss lemma,
   primitive part, specialization of the gcd over K(X)[λ]. Value: Paper III calls it its main new
   result; it is what turns a generic test into a decision on the whole chart.
6. **Paper I: degree-windowed relations (`lem:window`, medium).** A coefficient-vector identity,
   but it requires setting up the (i,j)-indexed window matrix and the 2ω-column truncation
   convention. Value: it is the only bridge between the Bézout bound and the Gram certificate.
7. **Paper I: Gram certificate plus Cauchy–Binet compression (`prop:gram`, large).** Depends on 6
   and on Cauchy–Binet. Value: the only route from "no common root" to a polynomial-size test, but
   gated by infrastructure (see section 6).
8. **Paper III: the counterexample (`sec6:prop:nonconstant`, `sec6:cor:reduction`, medium).** A
   finite rational certificate that can be discharged by computation. Value: it is a published
   claim of error against one reduction, so machine-checking it has independent weight.

Not blocked but not ranked: the quotient-dimension bookkeeping behind `lem:sandwich` and
`claim:sandwich` (needed by items 1 and 4), `prop:rankprecheck` of Paper III (small), and the
e_1..e_j form of Paper I `lem:rankcons` (medium; needs eigenvalues of real symmetric matrices).

## 6. Blocked on infrastructure

| Statement(s) | What Mathlib lacks | How it might be obtained |
|---|---|---|
| Paper I `prop:gram`, the Cauchy–Binet compression of K(λ,μ) | Cauchy–Binet for rectangular matrices: no declaration in the 32 modules mentions it, and `paper/LEAN_MAP.md` section C records that Mathlib has none | Port the external Lean 4.30 proof already under discussion (LEAN_MAP section C, Ask 1), or derive only the 2-by-2 Gram identity from `Matrix.det_mul` and a Schur-complement block matrix |
| Paper II `prop:tight` (the pair (G,b)) | controllability / Popov–Belevitch–Hautus theory; the tree has no controllability development (the paper says so in its reproducibility subsection) | The single-input case is elementary: rank[λI − G b] = a for all λ iff no eigenvector of G is annihilated by b. Build it from `Module.End.exists_eigenvalue` and eigenspace lemmas instead of porting PBH |
| Paper III `sec5:lem:subres`, and the gcd step of `sec4:thm:generic` | subresultant chains and any cost bound for polynomial gcd; no module computes a polynomial gcd, and the tree has no size model | Build the primitive-part gcd from `Polynomial.gcd`/`EuclideanDomain` for correctness only; the Sylvester-minor size bounds need a bit-length development, otherwise leave paper-level |
| Paper I `thm:fixedq`, `thm:fpt`, `cor:arith`; Paper III `sec5:thm:poly` | real algebraic decision procedures: Renegar's bound, BPR root isolation and sampling, quantifier elimination; nothing in the tree mentions Renegar | Formalize only the reduction (the formula Phi_{ω,J} and its size) and cite the decision bound, or treat the bound as a hypothesis in the statement |
| Paper I `lem:rationalbasis`, `lem:coeff`; Paper III `sec5:lem:height`, `appBC:lem:norm`, `appBC:lem:charpoly` | a bit-complexity library: Hadamard's inequality, Bareiss growth, coefficient heights, the Mignotte factor bound. Mathlib has `Nat.size`/`Nat.log2` but no matrix or polynomial height bounds | Build from `Matrix.det` plus `Nat.log2` primitives, which is a research-sized project; recommended to leave paper-level |
| Paper III `sec4:thm:closed` (bad locus closed) | elimination theory: the projection of an incidence subvariety of X times P^1, and projective closedness; no module mentions resultants or projective space | Recast the paper's own proof as "the bad locus is the zero set of the maximal minors' resultants"; needs a resultants API, otherwise paper-level |
| Paper III `sec3:lem:constantrank`, `sec3:thm:param`, `sec4:prop:realpoints` | relative Grassmann bundles, vector bundles over a projective base, irreducibility and Zariski-dense real points; no module mentions Grassmannians | Only the dimension count of Gr(m,N) is library-shaped; the bundle and density layer needs an algebraic-geometry development, so keep it paper-level |
| Paper I `lem:W-conditions` (quantified form), `lem:zero` (i)–(iii) | the real-to-complex passage for a real pencil: rank invariance under scalar extension R → C. Eigenvalues over C themselves are available (`Module.End.exists_eigenvalue` is used in `BoundLower.lean`) | Port `LinearMap.extendScalars`/`Matrix.rank_map` style rank invariance (a small port), then state the pencil condition over C |

## 7. Where the papers' own tables overstate the Lean coverage

1. **Paper I, `lem:bezout` graded literal.** `exists_bezout_family`,
   `isCoprime_of_no_common_root` and `exists_bezout_deg_lt` all require `[IsAlgClosed K]`; the
   real coefficients that the paper calls "not a cosmetic refinement" are not covered.
2. **Paper I, row "Rectangular left inverse (Proposition prop:zero) — literal —
   `exists_leftInverse_linear`".** That declaration is `lem:zero` (ii) ⇒ (iv) (existence of a
   degree-bounded left inverse); `prop:zero` is the polynomial-time test, which the same table's
   last row calls paper-level. The two rows contradict each other.
3. **Paper I and Paper II, "Sandwich and realizability — literal".** Only the inclusion
   (`rowSpan_fromRows_left`) and the preimage statement (`mem_rowSpan_iff_exists_vecMul`) are
   formalized; the converse realization with exactly t = dim(W/W_0) rows and the bound
   dim(W/W_0) ≤ r are paper-level.
4. **Axiom-audit coverage.** `Audit.lean` imports neither `Q1Paper.BoundLower` nor
   `Q1Paper.TightDim`, and has no `#print axioms` line for `finrank_add_one_le_of_spectral`,
   `finrank_sup_pi_le`, `finrank_pi1_mono`, or for `exists_mulVec_eq_iff_rank_gram` (only its
   helper `augment_mul_transpose` is listed). The declarations build, and no module contains
   `sorry`/`admit`/`axiom`, but the "every declaration is checked against only propext,
   Classical.choice, Quot.sound" sentence is currently stronger than what `Audit.lean` prints.

## 8. Questions for the expert

Q1 (Paper I `prop:gram`). Is there a usable Mathlib proof of Cauchy–Binet for rectangular
matrices, and is it cheaper to port an existing Lean 4 formalization or to derive
det(A^T B) from `Matrix.det_mul` via a Schur-complement block matrix?

Q2 (Paper I `lem:bezout`, `lem:zero` (iii)). For f_1..f_s in R[λ] of degree at most ω with no
common complex root, is the cleanest route to real multipliers g_i with deg g_i < ω (a) gcd in
R[X] plus the fact that a nonconstant real gcd has a complex root, or (b) a real linear-algebra
argument on the coefficient system? Which is better supported by Mathlib's `Polynomial.gcd` API?

Q3 (Paper III `sec3:lem:constantrank`, `sec3:thm:param`). Does Mathlib's Grassmannian API suffice
to state "the s-dimensional subspaces containing a fixed delta-dimensional one are
Gr(s−delta, Q/V_0)" and to compute its dimension, and would you state the bundle structure as a
map of varieties or only as a dimension count?

Q4 (Paper III `sec4:lem:fullrank`, Paper I `lem:compression` (iii)). Is Mathlib's
`Polynomial.IsPrimitive`/Gauss-lemma API strong enough to prove "a λ-gcd of positive degree over
K(X) forces a nonconstant common factor at every specialization", or is the resultant-based route
necessary?

Q5 (Paper I `lem:W-conditions`, Paper III `sec3:thm:direction`). Is formalizing "a real matrix has
the same rank over R and over C" via `LinearMap.extendScalars` or `Matrix.rank_map` currently
feasible in Mathlib, and is `Module.End.exists_eigenvalue` under `IsAlgClosed` the right tool for
the eigenvalue arguments instead of building a complexification?

Q6 (Paper I `thm:fpt`, `lem:rationalbasis`; Paper III `sec5`). Is there any Mathlib development of
coefficient-height or bit-length bounds for `Matrix.det` or `Polynomial.gcd` that could be reused
for Hadamard/Bareiss/subresultant estimates, or should all such cost claims stay paper-level?

## 9. Provenance of the declarations quoted

All declaration names above were read in the artifact tree `q1-functional-observer/Q1Paper/`
(32 modules, root module `Q1Paper.lean` importing 31 of them). The mapping from paper items to
declarations agrees with `paper/LEAN_MAP.md` sections A–C except for the four points in
section 7. No Lean source and no paper was modified for this document.
