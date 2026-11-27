# Report 110: the layer program after the c = 1 paper — consolidated record, current state, and two new proofs

This report consolidates everything done on the layer program since the c = 1 paper was completed, so that
the whole arc is in one place. It is written so that the parts already reviewed (reports 107, 108, 109)
can be skimmed: the corrections they produced are collected in one ledger in Part III, and the two items
that are new since the last report are **A.1** (a general proof of the row-space identity, previously only
checked on a chart) and **A.2** (exact arithmetic and bit complexity for the fixed-c = 2 theorem). The
questions in Part IV concern those two.

Self-contained. Lengths are in terms of the ambient dimension n, the number p of output rows, k = dim K₀,
and the input bit size τ.

---

## Part I. Starting point and conventions

After the c = 1 paper, what was settled is: for the hyperplane layer (ker H of dimension one) the
admissible kernel directions are the real eigenvectors of the compression M = π_{K₀}A|_{K₀}, restricted by
the prescribed rows; the design family is a finite union of relative Grassmann bundles; and a single
function-field gcd per chart decides the whole chart, giving polynomial time for fixed q with a
geometrically simple real spectrum.

What was open at that point: (i) the definition of the layer index, which had been used in two
incompatible ways; (ii) whether the c = 2 layer is decidable and at what cost; (iii) whether anything can
be said about general c. The program below answers (i) and (ii) and reduces (iii) to three structural
questions.

Conventions used throughout. With ρ = rank H = dim π_{K₀}(V) and q the number of rows,

$$c:=k-\rho,\qquad t:=q-\rho,\qquad q=\rho+t,\qquad c-t=k-q,$$

D := ker H = K₀ ∩ V^⊥ has dimension c. Two problems are kept separate: the **unrestricted** layer (all
designs with dim ker H = c) and the **K₀-split** layer (those also satisfying dim(V ∩ K₀) = ρ, equivalently
V = (V ∩ K₀) ⊕ (V ∩ K₀^⊥)). Most structural results below are for the split problem; where a result is
split-only this is said explicitly.

---

## Part II. The chain of results

### II.1 Three quantities that coincide only when q = k, and why the dimension hypothesis is a hypothesis

With ρ = rank H = dim π_{K₀}(V) one has the identity ω = rank(LN) = ρ, so the layer index is c = k − ρ.
Two other quantities occur and must not be confused with it: dim(V ∩ K₀^⊥) = q − ρ (= t) and
dim(V ∩ K₀), which is a third, generally different, quantity. In the c = 1 setting q = k, so the three
coincide, which is why the confusion was invisible there.

The direction theorem (M(D) ⊆ D for split designs satisfying (5a)) requires dim(V ∩ K₀) = ρ. That
hypothesis is **not** a consequence of (5a): there are designs with c = 2, satisfying (5a) and with exact
kernel, whose ker H is not M-invariant. Hence the split condition is genuine structure, not a
normalisation — the reason the two problems are kept apart.

### II.2 The two fixed-direction fibres, and the prescribed-row condition

Unrestricted: F_D = {V ∈ Gr(q, U_D^⊥) : V₀ ⊆ V, K₀ ∩ V^⊥ = D} with U_D = D + AD, and exactness of the
kernel is equivalent to K₀ ∩ (D + AD) = D.

Split: V = D^{⊥_{K₀}} ⊕ W with W₀ ⊆ W ⊆ T_D := K₀^⊥ ∩ (A₂₁D)^⊥, and
F_D ≅ Gr(t − w₀, T_D/W₀), of dimension (t − w₀)((n − k) − r(D) − t), nonempty iff
w₀ ≤ t ≤ (n − k) − r(D), where r(D) = rank(A₂₁|_D).

The prescribed rows give **two** independent conditions, one on the base and one on the fibre:
P_{K₀}(V₀) ⊆ D^{⊥_{K₀}} (equivalently D ⊥ P_{K₀}(V₀)) and W₀ ⊆ W, with W₀ ⊆ T_D for the fibre to exist.
So the base must be restricted to B_pres = {D ∈ I_c(M) : P_{K₀}(V₀) ⊆ D^{⊥_{K₀}}}. Missing this was the
main correction of the previous round.

### II.3 The base

Write the real primary decomposition K₀ = ⊕ K_λ ⊕ ⊕ K_{μ,μ̄}. An M-invariant two-plane is: a two-plane
inside one real primary component; a sum of invariant lines from two distinct ones
(P(K_λ) × P(K_μ), dimension (d_λ−1)+(d_μ−1)); or a plane attached to an irreducible quadratic component,
the family being P_ℂ(E_μ) ≅ ℂP^{g_μ−1} of real dimension 2(g_μ−1), where g_μ is the **geometric**
multiplicity. For a single Jordan block only the first two vectors of a chain occur; with several Jordan
blocks the classification depends on the relative position of eigenvectors and generalised
eigenvectors.

For simple spectrum I₂(M) is finite, of binom(k_ℝ,2) + #{conjugate pairs} points. This is the case the
algorithm uses; the general (multiple-block, higher-degree factor) case is **not** covered by any rational
parametrisation — see the retraction in Part III.

### II.4 Decidability: a real generic-point criterion

Let X be an irreducible affine chart with coordinate ring A = F[x₁,…,x_d]_S (a localisation of a polynomial
ring, hence a UFD), defined over a real field F ⊂ ℝ; let m₁,…,m_s be the maximal minors of the cleared
pencil and d_gen their λ-gcd degree over F(X).

**Lemma A (the generic degree is a lower bound).** If x is *admissible*, i.e. some maximal minor keeps its
generic λ-degree at x (in the pencil setting: rank H(x) = ω), then
deg gcd(m_i(x,·)) ≥ d_gen.

*Proof.* Divide out contents. By Gauss's lemma the gcd over Frac(A)[λ] may be taken primitive,
G ∈ A[λ], and then G | m_i in A[λ]. With m_i = G q_i one has lc(m_i) = lc(G) lc(q_i) in A; so
lc(G)(x) = 0 would force lc(m_i)(x) = 0 for every i, contradicting admissibility. Hence G(x,·) has degree
d_gen and divides every m_i(x,·). ∎

The hypothesis cannot be dropped: for m₁ = xλ − 1, m₂ = (xλ − 1)(λ − 1) one has d_gen = 1 while at x = 0
the two specialisations are −1 and −(λ − 1) with gcd 1.

**Lemma B.** U = {x : deg gcd = d_gen and x admissible} is a nonempty Zariski open set: on a fixed-degree
locus {deg gcd ≥ d} is closed (subresultant conditions), and by Lemma A the admissible locus already
satisfies deg gcd ≥ d_gen.

**Theorem.** If moreover the real points of X are Zariski dense and every real point is admissible, then
d_gen = 0 iff X contains a real pencil-feasible point.

This replaces the earlier (invalid) inference from "nonempty Zariski open" to "there is a real point", and
it fixes the algorithm to three outcomes — feasible, infeasible, undecided — where "infeasible" requires a
positive-degree generic gcd on **every** real-admissible full-rank chart.

### II.5 The image reduction (the central structural result)

Fix a split design, D with M(D) ⊆ D, W₀ ⊆ T_D, V = D^{⊥_{K₀}} ⊕ W, W₀ ⊆ W ⊆ T_D, dim W = t. Define
φ_w(u) = ⟨w, A₂₁u⟩ for u ∈ K₀ and Φ(W) = {φ_w : w ∈ W}.

**Theorem (split-layer image reduction).** (i) Φ(W) ⊆ D°, hence dim Φ(W) ≤ c; (ii) for every λ,
row(λH − H_A) = row(λH_K − (H_A)_K) + Φ(W); (iii) consequently the pencil condition depends on W only
through Φ(W).

The proof is a two-step computation: the W-rows of H vanish (w ⊥ K₀) and the W-rows of H_A are the φ_w,
while the D-rows are independent of W; the row space of a stacked matrix is the sum of the row spaces of
its blocks. A full general proof is in A.1.

Since dim D° = c, the W-quantifier is replaced by a quantifier over subspaces of a c-dimensional space:
for c = 2 the effective parameter is a subset of {0} ∪ P(D°) ∪ {D°} — **at most one projective-line
component**, and which of the three occurs is determined by Φ₀ = φ(W₀) and the dimension inequalities.

**Exact realizability.** With φ̄ : T_D/W₀ → D°/Φ₀ induced, a prescribed Φ is realised by some W with
W₀ ⊆ W ⊆ T_D, dim W = t iff

$$\Phi_0\subseteq\Phi\subseteq\varphi(T_D),\qquad
\dim\Phi-\dim\Phi_0\ \le\ t-w_0\ \le\ \dim\ker\bar\varphi+\dim\Phi-\dim\Phi_0 .$$

**Reduced feasibility criterion.** Some admissible W makes (5b) hold iff some realisable Φ satisfies
dim(row P_D(λ) + Φ) = ω for all λ (P_D(λ) = λH_K − (H_A)_K), equivalently
dim Φ − dim(Φ ∩ row P_D(λ)) = ω − r_D(λ) for all λ.

**Machine-checked part.** The set/dimension assertions of II.2, the equivalence
V ⊥ (D + AD) ⟺ W ⊆ (A₂₁D)^⊥, and Φ(W) ⊆ D° are formalised and pass an axiom audit whose only axioms are
the three standard ones. The row-space identity itself is not formalised as a matrix statement; A.1 gives
it in general form.

### II.6 The c = 2 monotonicity counterexample

At one and the same order q = 3 — the only order at which both layers can occur, since c − t = k − q —
the c = 2 layer is feasible (an explicit rational design with ω = 2, satisfying (5a), exactness, and with
six coprime 2×2 maximal minors) while the c = 1 layer is infeasible: the invariant lines are the lines of
the two-dimensional eigenspace E₁ together with two isolated directions, and for the whole projective
family D = span{e₁ + s e₂} the gcd of the two nonzero maximal minors equals (λ−1)(λ−2)(λ−3),
**independent of s**; the missing point span{e₂} of the chart was checked separately and gives the same
gcd, so the projective line is covered completely. This rules out the tempting "only small layers matter"
strategy.

### II.7 Complexity at fixed c = 2, and the two boundaries

**Theorem.** Assume c = 2, M of simple spectrum, and the K₀-split condition. Then the three-valued layer
decision runs in poly(n,τ) bit operations, with arithmetic in number fields of degree at most k².

The ingredients, in the order in which they are used:

1. the base is finite, O(k²) points (II.3);
2. for each D the effective fibre has at most one projective-line component, so at most two charts (II.5);
3. each chart parameterises the **image line** Φ(s) = span(φ₀ + sφ₁), so only one row of the pencil
   varies with s; every maximal minor is multilinear in the rows, hence deg_s ≤ 1, and deg_λ ≤ ω;
4. all decisions (ranks, kernels, Φ₀, the dimension inequalities) are exact linear algebra over the field
   of definition of D;
5. the gcd is computed over L(s)[λ] with [L : ℚ] ≤ k² and heights poly(n,τ), so its cost is poly(n,τ).

Two boundaries are essential and not technicalities. Dropping the simplicity of the spectrum makes the base
positive-dimensional (a Grassmannian of dimension 2(d_λ − 2) = O(n)). Letting c vary makes the number of
components binom(k,c) exponential. Under both restrictions the present route cannot be uniform; the honest
general bound is n^{O(cn+c²)}.

### II.8 General c

Everything in II.2, II.3, II.5 generalises verbatim with 2 replaced by c; the only place where c = 2
entered was the numerical value of dim D°. The effective fibre becomes Gr(r, D°) with
max_r r(c−r) = ⌊c²/4⌋, the rank strata are r(D) ∈ {0,…,c}, and the base components have dimension
c(d_λ − c). Three questions remain, in the order recommended by the previous review: **Q-B** (can Φ be
eliminated for general c, i.e. can "some Φ makes the pencil full-fledged" be expressed as a rank or
separation condition on the induced maps on T_D/W₀ alone?), then **Q-A** (can the component enumeration of
I_c(M) be avoided?), then **Q-C** (is it better to index layers by dim U?).

---

## Part III. Corrections ledger

Every claim below was withdrawn or repaired during the programme; this table is meant to be the record.

| # | Earlier claim | Status | Replacement |
|---|---|---|---|
| 1 | ω = dim(V ∩ K₀) | false | ω = rank H = ρ, and c = k − ρ |
| 2 | dim(V ∩ K₀) = k − 1 follows from (5a) | false | it is the split hypothesis, kept as an assumption |
| 3 | the fixed-direction fibre is {V : V₀ + D ⊆ V ⊆ ...} | false (D ⊥ V) | the two formulae of II.2 |
| 4 | n^{O(c²)} complexity | unjustified | n^{O(cn+c²)}; poly only at fixed c with simple spectrum |
| 5 | rational primary decomposition gives charts for the general invariant-plane family | **false** | geometry via ℚ-defined equations; algorithm by real Jordan type; the simple-spectrum finite classification suffices for the theorem |
| 6 | the prescribed rows are handled by W₀ ⊆ W alone | incomplete | also P_{K₀}(V₀) ⊆ D^{⊥_{K₀}}, i.e. restrict the base |
| 7 | conjugate pairs contribute one isolated plane | too broad | family ℂP^{g_μ−1}, real dimension 2(g_μ−1), geometric multiplicity |
| 8 | the c = 1 side of the counterexample covers the projective family | incomplete | the missing point span{e₂} was checked; same gcd |
| 9 | a nonempty Zariski-open set of good points implies feasibility | invalid | needs real-point density; Lemma A/B and the theorem of II.4 |
| 10 | dim T_D = ρ − r(D) with ρ = rank H | notational error | dim T_D = (n−k) − r(D) |
| 11 | deg_s ≤ 1 on any fibre chart | too broad | holds for the **image-line** parameterisation only (one varying row) |
| 12 | realizability of Φ is "linear plus dimension bookkeeping" | incomplete | the two explicit inequalities |

---

## Part IV. What is new since the last report, and questions

**A.1 The row-space identity in general form.** Writing h_v(x) = ⟨v, Nx⟩ and h^A_v(x) = ⟨v, ANx⟩ for the
rows viewed as elements of K₀^*, and Ψ_λ = λ h_· − h^A_·, with A = M + A₂₁ the decomposition of A along
E = K₀ ⊥ K₀^⊥:

- Lemma 1: for w ∈ W ≤ K₀^⊥, h_w = 0 and h^A_w = φ_w;
- Lemma 2: for any linear Ψ and V = P ⊕ W, Ψ(V) = Ψ(P) + Ψ(W);
- Theorem: Ψ_λ(V) = Ψ_λ(P) + Φ(W) for every λ, and Ψ_λ restricted to W equals −φ_· independently of λ.

So the identity no longer rests on a chart computation. The only "coordinate" choice is the identification
K₀^* ≃ ℝ^k via the basis N, which is where the row convention enters.

**A.2 Exact arithmetic for the fixed-c = 2 theorem.** For simple spectrum every invariant plane is a sum of
two eigenlines; each eigenline comes from an irreducible factor f_i of the minimal polynomial of M over ℚ
and a real root α, and the plane is defined over L = ℚ(α, β) with [L : ℚ] ≤ d_i d_j ≤ k². Heights of M, N,
A₂₁, the f_i, the α, the bases of D, D^⊥, T_D, and of φ, Φ₀ are poly(n,τ). All the decisions of II.7 (4)
are exact linear algebra over L, and the gcd of II.7 (5) costs poly(ω, deg_s, [L : ℚ], heights) = poly(n,τ).
Finally, only **real embeddings** are used, so no general real algebraic geometry is needed: the number of
charts is O(k²) and each carries one real parameter.

**Questions.**

**Q1 (A.1).** Is the general proof in A.1 correct as stated, in particular (a) the identification of the
rows with the functionals h_v, h^A_v (including the sign −φ_w), and (b) the claim that only the
identification K₀^* ≃ ℝ^k is needed?

**Q2 (A.2).** Are the field-degree and height claims right? In particular: is it legitimate to represent
each D by a basis over L = ℚ(α,β) when α and β come from two different irreducible factors, and is the
field degree bound d_i d_j (rather than larger) correct? Is anything lost by restricting to real embeddings?

**Q3 (algorithm contract).** Is the three-valued semantics (feasible / infeasible / undecided) acceptable as
the contract of the paper's algorithm, given that "infeasible" is certified only chartwise?

**Q4 (next step).** Given that Priority 1 and 2 of the previous review are now addressed, is Q-B still the
right next move, or should the c = 2 package first be written up as a paper?

### Reliability

| Item | Status |
|---|---|
| II.1 identity ω = ρ, the counterexample to the dimension hypothesis | identity proved; counterexample exact arithmetic |
| II.2 both fibres; prescribed-row base | set/dimension part and the (5a) equivalence machine-checked; the rest paper |
| II.3 base description | paper (classical), multiplicity qualified; general case explicitly not parametrised |
| II.4 Lemmas A, B, Theorem | paper (Gauss, subresultants, density) |
| II.5 image reduction, realizability, reduced criterion | (i),(iii) and the (5a) equivalence machine-checked; (ii) general proof in A.1; realizability and reduced criterion paper, complete |
| II.6 counterexample | exact arithmetic on both sides, projective line covered |
| II.7 complexity theorem | paper; deg_s bound checked on one chart, the rest by the structural argument of A.2 |
| II.8 | structural remarks, no proofs |
