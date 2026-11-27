# Same-Grassmannian mixed spectral behaviour, and a decision procedure for q = ω+1, ω = 2

This report has three parts. Part I fixes the setting and the notation. Part II records two results obtained
after the previous exchange: a same-Grassmannian example with opposite spectral verdicts, and a decision
procedure for the case q = ω+1, ω = 2. It also states the corrected complexity wording for k = ω. Part III
asks four specific questions.

## Part I. Setting

Given A ∈ C^{n×n}, C ∈ C^{p×n}, L_0 ∈ C^{r×n}, one seeks R ∈ C^{(q−r)×n} such that
L = [L_0; R] (q rows, full row rank) satisfies

(5a) rank[LA; L; CA; C] = rank[L; CA; C],
(5b) rank[λL − LA; CA; C] = rank[L; CA; C] for all λ ∈ C.

Put K = ker[C; CA] (dim k), choose a basis matrix N_K, and define

H = L N_K (q×k), H_A = L A N_K (q×k).

For a fixed rank ω, the admissible locus is the set of R with rank H = ω and ker H ⊆ ker H_A. On it the
induced map Z: W → C^q, W = im H, is defined by Z(Hx) = H_A x, and the pencil is λH − H_A = (λI − Z)H.
Choose a complement C^q = W ⊕ W′ and write Z = (A; B) in the corresponding blocks; then

bad ⟺ there is 0 ≠ y ∈ ker B with Ay ∈ C y.

For q = ω+1, B is a single row, ker B is a hyperplane in W, and for ω = 2 the hyperplane is a line
ker B = C w, so that

good ⟺ det[w, Aw] ≠ 0.

This is the case treated below. The pointwise statement is intrinsic: the vanishing of det[w, Aw] does not
depend on the chosen complement, because Aw = Zw for w ∈ ker B, and “Zw ∈ C w” is intrinsic. The matrix A
itself does depend on the complement, and should not be presented as canonical.

## Part II. Results

### II.1 The k = ω complexity statement

The previous report said that k = ω is settled “with a polynomial algorithm”. I accept the qualification:
the written argument enumerates the binom(q, ω) maximal minors, which can grow exponentially, and the
fixed-(q, ω) resultant bound does not give a uniform bound in the dimensions. I have replaced the statement by

> k = ω admits an exact generic-pencil reduction. For fixed (q, ω) the resulting test has a polynomial-time
> implementation using bounded-degree algebraic computations. A uniform polynomial-time bound for variable
> (q, ω) requires further analysis.

I would like to ask whether the following randomised route is legitimate (Question 1 below). By the
componentwise theorem, one generic point decides the answer: if the generic gcd has degree zero, the bad
locus is a proper closed subset and a random point avoids it; if the generic degree is positive, every point
is bad. At a rational point R_0, the gcd of the maximal minors of λH(R_0) − H_A(R_0) is the ω-th
determinantal divisor, which can be computed by a Smith form over Q[λ] without enumerating the minors. This
would give a one-sided (RP) test, provided the degree and bit-size bookkeeping is supplied.

### II.2 The same-Grassmannian example (Experiment B)

The question was whether two compatible choices over the same S can give one good and one bad pencil.
The answer is yes; the example is in the free region.

Data: n = 9, p = 3, q = 3, r = 1. C = [I_3 0]; the columns 4,5,6 of A are e_1, e_2, e_3 and the columns
7,8,9 are e_4, e_5, e_6; L_0 = e_7^T. Then K = ⟨e_7, e_8, e_9⟩, k = 3, K ∩ AK = 0, and the map
T(v, w) = v + Aw has trivial kernel, so every pair (x, y) ∈ S × S is compatible.

Take S = ⟨e_1, e_2⟩ in K-coordinates and fix

H = [[1,0,0], [0,1,0], [0,1,0]]  (rows E, w, w;  w = e_2).

Two choices of H_A:

good: H_A = [[0,0,0], [1,1,0], [1,0,0]]   (rows 0, e_1 + w, e_1),
bad : H_A = [[0,0,0], [0,1,0], [0,0,0]]   (rows 0, w, 0).

Both have rank H = 2 and ker H ⊆ ker H_A. Recovering R from R N_K = H_{2:3} and R A N_K = (H_A)_{2:3} gives

L_good = [e_7; e_4 + e_5 + e_8; e_4 + e_8],
L_bad  = [e_7; e_5 + e_8; e_8],

both of rank 3. The good candidate satisfies (5b); the bad one fails at λ = 0 (the maximal minors are
λ(λ−1), λ^2, and 0, whose gcd is λ). Both pass the seven consistency checks: ranks, null-space dimension,
CZ = LZ = 0, (5a) against the null-space rank criterion, h = 8 equal to the generic rank, and the gcd test
against the Toeplitz criterion.

Since H is the same, S = row(H) is the same and the rank-ω stratum is the same; only H_A (equivalently the
compatible y's) changes. Hence spectral behaviour is not a function of S, and not even a function of H.

### II.3 A decision procedure at q = ω+1, ω = 2

For fixed data, the admissible pairs are obtained from the Grassmannian points S with E + F_0 ⊆ S and
E + X_S = S, where E = row(L_0 N_K), F_0 = row(L_0 A N_K), and

C_S = {(x, y) ∈ S × S : xZ_1 + yZ_2 = 0}

is the compatible fibre. Writing the bottom rows as x_1, x_2 and y_1, y_2 gives H = [U_0; x_1; x_2] and
H_A = [V_0; y_1; y_2]. The exact procedure is:

1. enumerate the Grassmannian points S satisfying the criterion;
2. solve the linear system defining C_S;
3. build (H, H_A) and test the gcd of the 2-minors of λH − H_A (equivalently, det[w, Aw] at one point of
   each irreducible component of the fibre);
4. declare the instance feasible at q = ω+1 iff one component is generically good.

Two mechanisms occur:

- free case, ker T = 0: C_S = S × S and the fibre is large; the same S can carry both verdicts (II.2);
- constrained case, 0 < dim ker T ≤ k: the fibre is cut by linear conditions, and it can be entirely bad.

For the constrained example n = 5, p = 1, q = 3, r = 1 with C = e_1^T, A having first row e_5^T and columns
2,3,4 equal to e_3, e_2, e_5, and L_0 = e_4^T, one has K = ⟨e_2,e_3,e_4⟩ and dim ker T = 2. The Grassmannian
criterion gives the two points σ = (1, ±1, 0); on both, all 200 admissible parameter points tested have
positive-degree gcd (the family is entirely bad).

The classification obtained is therefore a classification of mechanisms together with an exact decision
procedure, not a closed-form criterion for every instance: free ⇒ the fibre can be mixed; constrained ⇒ the
fibre can be entirely bad; in both cases the same determinant decides.

## Part III. Requests

**Question 1.** Is the randomised route of II.1 legitimate? Specifically: (i) does one generic rational point
suffice to read off the generic degree, given that the coefficients of the gcd are rational functions whose
denominators may vanish on a proper closed set; (ii) is the Smith form of λH(R_0) − H_A(R_0) over Q[λ]
polynomial in the input size and in the degrees, so that the bit-size bookkeeping closes? If yes, may we state
k = ω ∈ RP (or ZPP), or would you prefer to keep the weaker wording?

**Question 2.** Is the example of II.2 the decisive answer to Experiment B? It shows that the spectral
verdict is not determined by S, nor by H, but only by the induced map. Does this settle the question in your
view, or would you still want an example where the two verdicts occur on different irreducible components of
the same fibre?

**Question 3.** For q = ω+1, ω = 2, is the free/constrained dichotomy of II.3 the right level of
classification? The alternative would be to push for a closed form on the free case (a criterion on the top
blocks U_0, V_0 deciding whether the fibre is generically good). We can attempt either; which would you
prioritise?

**Question 4.** Is the corrected wording of II.1 acceptable for a paper, or should the k = ω statement be
weakened further (for instance, stated only for fixed (q, ω)) until the Smith-form argument is written out?
