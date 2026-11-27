# Lean 4 formalization of the functional-observer feasibility chain: current state and the six places it gets stuck

This note is for an expert in Lean 4 / Mathlib. It has three parts: the mathematical
statements (Part I), what already compiles (Part II), and the six concrete places where
the formalization stops, with the exact failing goals and error messages (Part III).

The request at the end of each item in Part III is the same in kind: **a compiling
proof** (tactic script or term) for the displayed statement, in the environment fixed in
§0.2, or a pointer to the Mathlib lemma that makes it short.

---

## 0. Environment

### 0.1 Convention

Throughout: `K` is a field, `K[X]` is `Polynomial K`, matrices are `Matrix (Fin m) (Fin n) K`,
`rank` means rank over `K`, and for a matrix `A`, `row A` is the span of its rows.

### 0.2 Toolchain

```
lean-toolchain: leanprover/lean4:v4.35.0
Mathlib:        commit 56a005855ea17e0b0958f73ec801ae140b0a1679 (tag v4.35.0)
```

The whole development builds with `lake build` (9074 jobs, 0 errors) and every declaration
listed in Part II passes `#print axioms` with only `propext`, `Classical.choice`,
`Quot.sound`.

---

## Part I. The mathematical statements

Let $(A,C)$ be the system, $C\in K^{p\times n}$, and let $L=[L_0;R]$ be the observer rows
($L_0$ fixed, $R$ the $r$ free rows, $q=r_0+r$). Put

$$K_0=\ker\begin{bmatrix}C\\CA\end{bmatrix},\quad N \text{ a basis matrix of } K_0,\quad
H=LN,\quad H_A=LAN,\quad \omega=\operatorname{rank}H .$$

The two feasibility conditions are

$$(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\ \ \forall\lambda\in\mathbb C .$$

The paper proves, in order:

- **L1 (rank identity).** For $P\in K^{m\times n}$, $N_P$ a basis matrix of $\ker P$, and
  any $M\in K^{p\times n}$: $\operatorname{rank}[P;M]=\operatorname{rank}P+\operatorname{rank}(MN_P)$.
- **L2 (compression).** $(5a)\iff \operatorname{row}H_A\subseteq\operatorname{row}H$;
  under $(5a)$, $(5b)\iff\operatorname{rank}(\lambda H-H_A)=\omega$ for all $\lambda$.
- **L3 (attainable row pairs).** A free row $r_i$ is determined by
  $(H_i,(H_A)_i)=r_i[N\ AN]$, so the free rows live in
  $\mathcal T=\operatorname{row}[N\ AN]\subseteq K^{2k}$ of dimension
  $d_0=\operatorname{rank}[N\ AN]$, and are parametrized by $\kappa_{\rm obs}=r\,d_0$
  real coordinates.
- **L4 (rank consistency).** For real $M,c$: $\exists b,\ Mb=c$ iff
  $\operatorname{rank}(MM^{\mathsf T})=\operatorname{rank}(MM^{\mathsf T}+cc^{\mathsf T})$.
- **L5 (Bézout with degree bound).** For $f_1,\dots,f_s\in K[\lambda]$ of degree $\le\omega$
  with no common root ($\omega\ge1$), there are $g_1,\dots,g_s$ with
  $\sum_i g_if_i=1$ and $\deg g_i<\omega$.
- **L6 (pencil test).** For $Q(\lambda)=\lambda X-G$ with $q\ge\omega\ge1$, the following
  are equivalent: (i) $\operatorname{rank}Q(\lambda)=\omega$ for all $\lambda$; (ii) the
  maximal minors have no common complex root; (iii) their gcd is a nonzero constant;
  (iv) there is $S(\lambda)\in K[\lambda]^{\omega\times q}$ with $S(\lambda)Q(\lambda)=I_\omega$
  and $\deg S\le2\omega-2$; (v) there are $S_0,\dots,S_{2\omega-2}$ solving
  $$-S_0G=I_\omega,\qquad S_{j-1}X-S_jG=0\ (1\le j\le 2\omega-2),\qquad S_{2\omega-2}X=0.\tag{R0}$$
- **Prop 1 ($r=0$ test).** With $r=0$: compute $H$, $H_A$, rank-factor $H=XB$, and run L6
  on $(X,G)$ with $G=FX$, $H_A=FH$; the answer is feasibility of $(5a)\wedge(5b)$.
- **Thm 1/2 (bounds).** DEC at fixed $q$ costs $\mathcal L^{O(q^2)}$ bit operations; DEC is
  FPT in $\kappa_{\rm obs}$ with bound $f(\kappa_{\rm obs})\operatorname{poly}(\mathcal L)$.
- **Thm 3 ($\exists\mathbb R$).** $\mathrm{DEC}(q)\in\exists\mathbb R$.

---

## Part II. What compiles today

All in namespace `Q1Paper`, over `{K : Type*} [Field K]`, `q ω : ℕ`, `Fin`-indexed matrices.

### II.1 Compression and the row-pair space (abstract, linear-map level)

```lean
theorem ker_pairMap (f g : E →ₗ[K] F) :
    LinearMap.ker (pairMap f g) = LinearMap.ker f ⊓ LinearMap.ker g

theorem finrank_range_prod [FiniteDimensional K E]
    (f : E →ₗ[K] F) (g : E →ₗ[K] G) :
    finrank K ↥(LinearMap.range (f.prod g)) =
      finrank K ↥(LinearMap.range f) +
        finrank K ↥(Submodule.map g (LinearMap.ker f))

theorem finrank_range_pairMap ...
theorem finrank_range_pairMap_common ...
theorem ker_compressed_iff ...                -- (5a) ⟺ ker inclusion, abstract form
theorem G_form_iff ...                        -- H_A = FH ⟺ row inclusion, abstract form
theorem kappaObs_eq_mul_freePairSpace ...     -- κ_obs = r · d_0, abstract form
theorem freePairDim_le_kappaObs ...
theorem kappaObs_zero ...
```

`finrank_range_prod` is the abstract form of L1: with `f` the map `x ↦ xN` and `g` the map
`x ↦ xAN`, the second summand is `finrank (range (g|ker f))`, i.e.
`rank(MN_P)` in the paper's notation.

### II.2 Rank consistency (abstract, range/ker level)

```lean
theorem exists_solution_iff_mem_range ...
theorem exists_solution_iff_span_le_range ...
theorem exists_solution_iff_range_eq_sup_span ...
```

### II.3 Bézout (L5) — complete

```lean
theorem exists_forall_apply_ne_zero (s : Finset ι) (ℓ : ι → V →ₗ[K] K)
    (h : ∀ i ∈ s, ℓ i ≠ 0) : ∃ x, ∀ i ∈ s, ℓ i x ≠ 0

theorem exists_ne_zero_linearCombination (f : ι → K[X])
    (h : ∀ x : K, ∃ i, (f i).eval x ≠ 0) :
    ∃ a : ι → K, (∑ i, C (a i) * f i) ≠ 0

theorem exists_ne_zero_with_finite_roots (f : ι → K[X])
    (h : ∀ x : K, ∃ i, (f i).eval x ≠ 0) :
    ∃ F : K[X], F ≠ 0 ∧ Set.Finite {x : K | IsRoot F x}

theorem isCoprime_of_no_common_root [IsAlgClosed K] {F G : K[X]} (hF : F ≠ 0)
    (h : ∀ x : K, ¬ (F.IsRoot x ∧ G.IsRoot x)) : IsCoprime F G

theorem exists_bezout_deg_lt {ω : ℕ} {F G : K[X]} (hF : F ≠ 0) (hG : G ≠ 0)
    (hω : 1 ≤ ω) (hFd : F.natDegree ≤ ω) (hGd : G.natDegree ≤ ω)
    (h : IsCoprime F G) :
    ∃ u v : K[X], u * F + v * G = 1 ∧ u.natDegree < ω ∧ v.natDegree < ω

theorem exists_bezout_family {ω : ℕ} {f : ι → K[X]} [Fintype ι]
    (hω : 1 ≤ ω) (hdeg : ∀ i, (f i).natDegree ≤ ω)
    (hroot : ∀ x : K, ∃ i, (f i).eval x ≠ 0) :
    ∃ g : ι → K[X], (∑ i, g i * f i) = 1 ∧ ∀ i, (g i).natDegree < ω
```

(The last one is L5 verbatim; the proof goes: nonzero combination $F$, finitely many roots,
a second combination $G$ avoiding them by hyperplane avoidance, coprimality, and the
degree-bounded two-polynomial Bézout obtained by reducing $u_0$ modulo $G$.)

### II.4 The rectangular left inverse from the adjugate, and the coefficient system

```lean
def rowSel (e : Fin ω → Fin q) : Matrix (Fin ω) (Fin q) K        -- the row-selection matrix E_I
def adjRowInverse (e : Fin ω → Fin q) (Q : Matrix (Fin q) (Fin ω) K) : Matrix (Fin ω) (Fin q) K
theorem adjRowInverse_mul (e : Fin ω → Fin q) (Q : Matrix (Fin q) (Fin ω) R) :
    adjRowInverse (R := R) e Q * Q =
      Matrix.det (Q.submatrix e id) • (1 : Matrix (Fin ω) (Fin ω) R)   -- R any CommRing

def minors (Q : Matrix (Fin q) (Fin ω) K) (e : Fin ω ↪ Fin q) : K[X]
theorem leftInverse_of_bezout ... :
    (∑ e, g e • adjRowInverse e Q) * Q = 1
theorem exists_leftInverse ... : ∃ S, S * Q = 1                     -- with hdeg as hypothesis

-- degree estimates
theorem natDegree_det_le_sum (d : Fin n → ℕ) (h : ∀ i j, (M i j).natDegree ≤ d i) :
    (Matrix.det M).natDegree ≤ ∑ i, d i
theorem natDegree_det_le (h : ∀ i j, (M i j).natDegree ≤ d) :
    (Matrix.det M).natDegree ≤ n * d
theorem natDegree_adjugate_le (h : ∀ i j, (M i j).natDegree ≤ 1) (i j : Fin n) :
    (Matrix.adjugate M i j).natDegree ≤ n - 1
theorem natDegree_adjRowInverse_le ... : (adjRowInverse e Q i j).natDegree ≤ ω - 1
theorem exists_leftInverse_linear (hlin : ∀ i j, (Q i j).natDegree ≤ 1)
    (hminor : ∀ α : K, ∃ e : Fin ω ↪ Fin q, (minors Q e).eval α ≠ 0) :
    ∃ S : Matrix (Fin ω) (Fin q) K[X], S * Q = 1 ∧ ∀ i j, (S i j).natDegree ≤ 2 * ω - 2

-- the coefficient system (v) ⇒ (iv) of L6
def pencil (Xm Gm : Matrix (Fin q) (Fin ω) K) : Matrix (Fin q) (Fin ω) K[X]
def spoly {d : ℕ} (S : Fin (d + 1) → Matrix (Fin ω) (Fin q) K) : Matrix (Fin ω) (Fin q) K[X]
theorem spoly_mul_pencil ... :   -- product expansion of S(λ)Q(λ)
theorem spoly_mul_pencil_zero ...      -- d = 0 (ω = 1) case
theorem spoly_mul_pencil_eq_one {d : ℕ} (S : Fin (d + 1) → Matrix (Fin ω) (Fin q) K)
    (h0 : S 0 * Gm = -1)
    (hj : ∀ j : Fin d, S (Fin.castSucc j) * Xm - S (Fin.succ j) * Gm = 0)
    (hd : S (Fin.last d) * Xm = 0) :
    spoly S * pencil Xm Gm = 1

-- one algebraic fact used by the Gram certificate
theorem sum_sq_eq_zero_iff {ι : Type*} [Fintype ι] (v : ι → ℝ) :
    (∑ i, v i * v i = 0) ↔ v = 0
```

---

## Part III. The six places it stops

For each item: the statement wanted, the exact error, the attempts, and the request.

### Item 1. Matrix-level rank identity (L1) — the biggest gap

**Wanted.**

```lean
variable {K : Type*} [Field K] {m n p r : ℕ}

theorem rank_vstack_add_rank_mul
    (P : Matrix (Fin m) (Fin n) K) (M : Matrix (Fin p) (Fin n) K)
    (N : Matrix (Fin n) (Fin r) K)
    (hN : ∀ v : Fin n → K, P.mulVec v = 0 ↔ ∃ w, N.mulVec w = v)
    (hNr : ∀ w : Fin r → K, N.mulVec w = 0 → w = 0) :
    (Matrix.fromRows P M).rank = P.rank + (M * N).rank
```

**What exists.** Only the abstract version: I proved the same statement for
`f : E →ₗ[K] E'`, `g : E →ₗ[K] E''` and a complement/quotient argument, ending in
`Module.finrank` equalities. Nothing is stated with `Matrix.rank`.

**Where it stops.** I do not know the idiomatic Mathlib route from a linear-map statement
about `LinearMap.ker`/`range` to a statement about `Matrix.rank`, in a way that stays
short. The pieces I could find are `Matrix.rank` (defined for matrices over a field via
`toLin'`), `LinearMap.finrank_range_add_finrank_ker`, `Submodule.finrank_add_finrank_orthogonal`.
A direct `calc` through `Matrix.rank_eq_finrank_row` (if that is the right name) plus
`Submodule.finrank_sup` looks plausible but I could not make it elaborate within a
reasonable heartbeat budget.

**Request.** A compiling proof of `rank_vstack_add_rank_mul` (or of the same statement with
`N` replaced by `LinearMap.ker P` and `Matrix.rank` replaced by `Module.finrank` of row
spaces), plus, if possible, the one-line explanation of which Mathlib lemma is the intended
bridge. This single statement is the matrix form of L1 and is what Lemmas 2 and 4 are
currently missing.

**Knock-on.** With Item 1 in hand, L2 and L4 become mechanical: both are two applications of
the rank identity to specific block matrices, exactly as in the paper.

### Item 2. Matrix-level rank-consistency criterion (L4)

**Wanted.**

```lean
theorem exists_mulVec_eq_iff_rank_gram
    (M : Matrix (Fin m) (Fin n) ℝ) (c : Fin m → ℝ) :
    (∃ b : Fin n → ℝ, M.mulVec b = c) ↔
      (M * Mᵀ).rank = (M * Mᵀ + Matrix.vecMulVec c c).rank
```

**What exists.**

```lean
theorem exists_solution_iff_mem_range (T : E →ₗ[K] F) (c : F) :
    (∃ b : E, T b = c) ↔ c ∈ LinearMap.range T

theorem exists_solution_iff_span_le_range ...
theorem exists_solution_iff_range_eq_sup_span ...
```
The last two express the same solvability condition by span inclusion and by a sup of
ranges. None of them mentions the Gram matrix, so the two-rank criterion is not covered.

**Where it stops.** Same bridge problem as Item 1, plus one genuinely missing lemma:
$$\operatorname{rank}(MM^{\mathsf T})=\operatorname{rank}(M)\quad\text{and}\quad
\operatorname{range}(MM^{\mathsf T})=\operatorname{range}(M)$$
for real matrices (equivalently $\ker(MM^{\mathsf T})=\ker M^{\mathsf T}$; note the
domains differ, $MM^{\mathsf T}$ lives on $\mathbb R^m$ while $M$ acts on $\mathbb R^n$, so the
correct statement is $\ker(MM^{\mathsf T})=\ker M^{\mathsf T}$, not $\ker M$).

Verified by `#check` in the pinned environment:

* exist: `Matrix.rank`, `Matrix.rank_transpose`, `Matrix.vecMulVec`;
* **do not exist**: `Matrix.rank_mul_transpose`, `Matrix.rank_eq_finrank_row`,
  `Matrix.rank_eq_finrank_col`.

Correction (see the reply archived next to this note): `rank(MM^{\mathsf T}) = rank M` **is**
available, as `Matrix.rank_self_mul_transpose`; the transpose orientation matters, and
`Matrix.rank_transpose_mul_self` is the one for $M^{\mathsf T}M$.

So the rank of the Gram matrix is nowhere related to that of $M$ in the Mathlib version I
have, and without that step the equivalence between "$c\in\operatorname{range}M$" and the
two-rank test cannot be closed.

**Request.** A compiling proof of the statement above, or of the two ingredients separately:
(i) `(M * Mᵀ).rank = M.rank` over `ℝ`; (ii) `M.mulVec b = c` solvable iff
`range M = range (M * Mᵀ + vecMulVec c c)`.

### Item 3. Cauchy–Binet for rectangular matrices (needed by the certificate)

**Wanted.**

```lean
theorem cauchy_binet {m n p : ℕ} (A : Matrix (Fin m) (Fin n) R) (B : Matrix (Fin n) (Fin p) R)
    (I : Finset (Fin m)) (J : Finset (Fin p)) (hI : I.card = J.card) :
    (A * B).submatrix (↑) (↑) I J).det =
      ∑ K ∈ (Finset.univ.powersetCard I.card), (A.submatrix id (↑) K).det * (B.submatrix (↑) id K).det
```
(up to the exact `Finset`/`OrderEmbedding` encoding of the index sets).

**What exists.** Nothing; the paper uses Cauchy–Binet at the level of the compressed
certificate $Z^{\mathsf T}Z$ and the kernel $K(\lambda,\mu)$.

**Where it stops.** Mathlib does not have Cauchy–Binet (any form) as of the pinned commit.
I am aware of an external Lean 4 formalization (`ClassicalGaps.cauchy_binet_det`, written
against Lean 4.30) but have not ported it, and I do not know whether the statement shape
there matches what the paper needs (minors indexed by arbitrary `Finset`s on both sides).

**Request.** Either a pointer to a Mathlib-compatible version, or a proof of the statement
above in the pinned environment.

### Item 4. Coefficient extraction: $(\mathrm{iv})\Rightarrow(\mathrm{v})$ of L6

**Wanted.**

```lean
theorem coeff_mul_apply {n p : ℕ} (A : Matrix (Fin ω) (Fin n) K[X])
    (B : Matrix (Fin n) (Fin p) K[X]) (i : Fin ω) (j : Fin p) (k : ℕ) :
    ((A * B) i j).coeff k
      = ∑ a : Fin n, ∑ x ∈ Finset.antidiagonal k,
          (A i a).coeff x.1 * (B a j).coeff x.2
```

**What exists.** The reverse direction $(v)\Rightarrow(iv)$ is complete
(`spoly_mul_pencil_eq_one`). The forward direction needs this coefficient lemma.

**Where it stops.** Four attempts, four different failures:

1. `rw [Matrix.mul_apply, Polynomial.coeff_sum]`
   → ``Tactic `rewrite` failed: Did not find an occurrence of the pattern (sum ?m ?f).coeff ?n``
   (the goal's sum is `∑ a, A i a * B a j`, but the rewrite does not fire after
   `Matrix.mul_apply`; error tail: ``function expected A i``).
2. `simp only [Matrix.mul_apply, Polynomial.coeff_sum]` then
   `refine Finset.sum_congr rfl (fun a _ => ?_)`
   → `typeclass instance problem is stuck: AddCommMonoid ?m.46`.
3. Adding type annotations and using
   `Polynomial.natDegree_sum_le`-style lemmas instead
   → `(deterministic) timeout at whnf, maximum number of heartbeats (200000)`.
4. `simp only [Matrix.mul_apply, Polynomial.coeff_sum, Polynomial.coeff_mul]`
   → leaves an unsolved goal (the `coeff_mul` form uses `Finset.antidiagonal`, and `simp`
   does not re-index the outer `Finset.univ` sum).

**Request.** A compiling proof of `coeff_mul_apply`. This is the one place where I believe
a 10-line solution exists and I simply cannot find the right tactic sequence.

### Item 5. The window / Gram certificate at matrix level (Proposition 7)

**Wanted.** (Shape only; the paper's statement is the equivalence between the spectral
condition on $P(\lambda)=\lambda H-H_A$ and the solvability of
$Z^{\mathsf T}Z\,x=e_0$, $x\in\mathbb R^{2\omega}$, where $Z$ is the matrix of coefficients
of the $2\omega$ forms built from the maximal minors.)

**What exists.** Only the one-line algebraic fact
`sum_sq_eq_zero_iff : (∑ i, v i * v i = 0) ↔ v = 0` over `ℝ`, which is the last step of
$K(\alpha,\bar\alpha)=\sum_{I,J}|f_{I,J}(\alpha)|^2$. Nothing about the coefficient matrix
$Z$ is formalized.

**Where it stops.** The statement itself has not been pinned down in Lean form: it involves
(i) the coefficient matrix of the forms $\alpha\mapsto f_I(\alpha)$ for $|I|=\omega$,
(ii) the identity $K(\alpha,\bar\alpha)=\sum_{I,J}|f_{I,J}(\alpha)|^2$ from Cauchy–Binet,
(iii) the equivalence "no common complex root iff $Z^{\mathsf T}Zx=e_0$ solvable".
Each of (i)–(iii) is a small formalization, but (ii) depends on Item 3.

**Request.** Advice on the minimal *statement* to formalize so that the paper's Proposition 7
is covered by one Lean theorem, and a skeleton of that statement. I would rather get the
statement right than guess at it.

### Item 6. Small API gaps that cost a full iteration each

These are not mathematical blockers; they are places where the name I expected does not
exist in the pinned Mathlib. Listing them so the answer to Items 1–5 does not repeat them.

| I expected | Reality in v4.35.0 | Workaround used |
|---|---|---|
| `Polynomial.monic_gcd` | absent | prove gcd is a *unit* via `IsAlgClosed.exists_root`, then multiply a Bézout relation by its inverse |
| `EuclideanDomain.gcd_eq_one_iff_coprime` | absent | same |
| `Polynomial.gcd_eq_normalize` | absent | same |
| `Finset.sum_univ_one` | absent; it is `Fin.sum_univ_one` | use `Fin.sum_univ_one` |
| `Int.cast_eq_C` | absent | `push_cast; rfl` |
| `map_intCast C c` | `RingHomClass` synthesis fails | `push_cast; rfl` |
| `Matrix.updateRow_apply` applied to `M i` | statement is pointwise: `M.updateRow i b i' j = if i' = i then b j else M i' j` | rewrite pointwise, then `split_ifs` |
| `Pi.single i 1` inside a hypothesis about `M.updateRow` | takes the type family from context only if the matrix is passed as an explicit argument | state a helper with the matrix as an explicit parameter |
| `mul_smul` for `A * (c • B)` | `mul_smul` is the *scalar* law `(a*b) • x`; the matrix law is `Matrix.mul_smul` | use `Matrix.mul_smul` |
| `Matrix.map_sub` | carries a side condition `∀ a b, f (a - b) = f a - f b` | avoid it: take the equality from `sub_eq_zero.mp` before mapping |
| `Finset.sum_mul` for matrices | matrix version is `Matrix.sum_mul` | use `Matrix.sum_mul` |
| `pow_succ'` for `λ^j * λ` | `pow_succ'` is `a^(n+1) = a * a^n`; for `a^n * a` use `pow_succ` | use `pow_succ` |
| `linarith` over an arbitrary field | `linarith` needs an ordered ring; a general `K` is not ordered | `field_simp` / `eq_neg_iff_add_eq_zero` / `ring` / `abel` |
| `Polynomial.natDegree_sum_le_of_forall_le s` | the `Fintype`/`Semiring` arguments stay metavariables | annotate the `Finset` explicitly, or use `natDegree_sum_le` + `Finset.sup_le` |
| `Matrix.det_apply` + `natDegree` | the permutation sum blows the heartbeat budget | expand along the first row (`Matrix.det_succ_row_zero`) and induct on `n` |

---

## Part IV. What would close the gap

In decreasing order of value per unit of work:

1. **Item 1** (matrix rank identity): closes the matrix-level gap for L1, L2, L4 at once.
2. **Item 2** (rank-consistency criterion): makes L4 literally what the paper states.
3. **Item 4** (`coeff_mul_apply`): makes L6 (iv)⇒(v) — currently paper-level — a Lean step.
4. **Item 3** (Cauchy–Binet): prerequisite for Proposition 7 and for the compressed certificate.
5. **Item 5** (window statement): needs a decision on the statement before any proof attempt.

Items 1–3 and 5 are each, I believe, one focused session for someone who knows the Mathlib
API; Item 4 is a tactic question; Item 3 is the only one where I suspect genuine work is
needed.
