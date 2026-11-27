# Review of `43_standard_form_and_literature.md`

The report makes a useful attempt to move from the algebraic certificate to a geometric decision problem. However, the proposed reduction of the bad set to a one-parameter family of affine subspaces is not valid for the observer problem as currently formulated. This is a fundamental issue, not a minor technical gap.

There are two independent obstructions:

1. The maximal minors of \\(\lambda H(R)-H_A(R)\\) are generally polynomial of degree up to \\(\omega\\) in \\(R\\), not affine-linear in \\(R\\). Thus their common-zero sets in \\(R\\) are generally algebraic varieties, not affine subspaces.
2. The spectral parameter ranges over \\(\mathbb C\\), whereas the design variable \\(R\\) is real. Treating \\(\lambda\in\mathbb C\\) as a one-dimensional real parameter is incorrect. The complex parameter has two real coordinates, and the real locus of the resulting incidence projection needs separate treatment.

Consequently, the dimension estimate in Part II does not establish the claimed polynomial-time tests, and the proposed “critical case” is not yet a valid description of the remaining difficulty.

The standard decision formulation in Part I, by contrast, is sound when interpreted using the reduced-pencil certificate from the previous report. It gives a legitimate \\(\exists\mathbb R\\) upper bound. I would retain that as the main complexity formulation and treat the affine-covering question as a separate possible research direction, not as a reduction already obtained from the observer problem.

I will examine the claims in order, then discuss the literature and the most promising research strategy.

## 1. Part I: the standard formulation

The decision problems

\\[ \mathrm{REAL\text{-}AUG}(q),\qquad \mathrm{REAL\text{-}AUG}\_{\omega}(q) \\]

are appropriate.

For fixed \\(\omega\geq1\\), the system

\\[ H(R)=UV,\quad H_A(R)=GV,\quad JU=I\_\omega,\quad VZ=I\_\omega, \\]

\\[ X(\lambda)(\lambda U-G)=I\_\omega,\qquad \deg X\leq 2\omega-2 \\]

is indeed an equivalent real polynomial feasibility formulation, assuming the central theorem's hypotheses and the established reduced-pencil criterion.

A terminology refinement: the equations are not all bilinear in the strict sense that every monomial is a product of one variable from each of two disjoint blocks. They are polynomial equations of total degree at most two, with affine and bilinear terms. For example, \\(H(R)=UV\\) has an affine-linear left-hand side and a bilinear right-hand side. This distinction is small but worth keeping in a formal complexity statement.

The variable count in the report,

\\[ (2\omega-1)\omega q+O(\omega^2+qr), \\]

is not a complete count: it suppresses the dimensions of \\(R,U,V,G,J,Z\\), and the term \\(qr\\) does not in general account for all of them. A more transparent count, using the dimensions from the previous report, is

\\[ (q-r)n+3q\omega+2k\omega+(2\omega-1)\omega q. \\]

This is polynomial in the explicit input dimensions.

There is also a small but important encoding qualification. If \\(q\\) is part of the input in binary and the input does not explicitly contain matrices of dimension \\(q\\), one must specify how the output dimension is encoded. In the usual explicit-matrix model, dimensions are already reflected in the input length. If \\(q\\) is an independent parameter, unary encoding or an explicit polynomial bound on \\(q\\) avoids a succinct-dimension ambiguity.

The statement

\\[ \mathrm{REAL\text{-}AUG}(q) \iff \bigvee\_{\omega=0}^{\min(q,k)} \mathrm{REAL\text{-}AUG}\_{\omega}(q) \\]

is correct. The zero-rank branch must be handled separately, as the report says.

Assessment: Part I is the right standard formulation. The \\(\exists\mathbb R\\) membership conclusion is justified by the quadratic certificate, not by the geometry in Part II.&#x20;

43_standard_form_and_literature.md



## 2. Part II: the claimed affine-subspace structure

### 2.1 The decisive error: the minors are not affine in \\(R\\)

The report says:

> “The \\(\omega\\)-minors \\(p_i(R,\lambda)\\) are affine in \\(R\\) and of degree at most \\(\omega\\) in \\(\lambda\\).”

The second assertion is correct: because the pencil is degree one in \\(\lambda\\), its \\(\omega\\)-minors have degree at most \\(\omega\\) in \\(\lambda\\).

The first assertion is generally false.

The entries of

\\[ P(R,\lambda)=\lambda H(R)-H_A(R) \\]

are affine-linear in \\(R\\). But an \\(\omega\times\omega\\) determinant is a sum of products of \\(\omega\\) entries. Consequently, its degree in \\(R\\) is generally at most \\(\omega\\), not one.

For example, take a \\(2\times2\\) pencil with entries affine in two scalar design variables \\(x,y\\):

\\[ P(x,y,\lambda)= \begin{pmatrix} \lambda x&y\\\ 1&\lambda \end{pmatrix}. \\]

Its determinant is

\\[ p(x,y,\lambda)=\lambda^2x-y. \\]

This particular example happens to be affine in \\(x,y\\), but that is due to its sparse structure. In general, the determinant

\\[ \det\begin{pmatrix} x&y\\\ z&w \end{pmatrix}=xw-yz \\]

is quadratic in the design variables.

Thus, for general \\(\omega\\),

\\[ p_i(R,\lambda)=0 \\]

defines an algebraic set in \\(R\\), not an affine hyperplane or affine subspace.

It follows that the claimed representation

\\[ L(\lambda)R=b(\lambda) \\]

has not been derived. The bad set cannot currently be written as

\\[ \mathcal B=\bigcup\_{\lambda\in\mathbb C}A(\lambda) \\]

with \\(A(\lambda)\\) affine subspaces.

This is the first point that must be corrected before any of the subsequent dimension arguments can be used.

### 2.2 A second issue: the complex spectral parameter

Even if an affine representation were available, the dimension argument needs a careful choice of base field and ambient space.

The augmentation variable is real:

\\[ R\in\mathbb R^N. \\]

But a spectral rank drop can occur at a nonreal \\(\lambda\\). The bad set is therefore described by

\\[ \exists\\,\lambda\in\mathbb C: \operatorname{rank}P(R,\lambda)<\omega. \\]

Writing \\(\lambda=a+ib\\), the condition involves two real parameters \\(a,b\\), with the real and imaginary parts of the polynomial equations imposed simultaneously.

For a real parameter \\(\lambda\\), a one-parameter real dimension estimate might be relevant. For a complex parameter, the parameter space has real dimension two. More fundamentally, the correct algebraic treatment is usually to work over \\(\mathbb C\\), form the incidence variety in

\\[ \mathbb C^N\times\mathbb P^1(\mathbb C), \\]

and then study its real points in the \\(R\\)-coordinates.

One cannot simply use a one-dimensional real-parameter estimate and conclude that the real bad set has the asserted dimension.

### 2.3 The dimension bound itself needs hypotheses

The estimate

\\[ \dim\bigcup\_\lambda A(\lambda) \leq \max\_\lambda\dim A(\lambda)+1 \\]

is reasonable for a suitably algebraic family of affine subspaces over a one-dimensional algebraic parameter space, with dimension interpreted over the appropriate field. But it is not an automatic statement for an arbitrary set-theoretic union. One needs a constructible or algebraic incidence family and a dimension theorem for its projection.

Even after correcting the base field, this bound would give information about the dimension of the bad locus, not automatically a polynomial-time decision procedure. One would still need to compute the relevant fibre dimensions uniformly in \\(\lambda\\), handle exceptional parameter values, and account for the real-point question.

### 2.4 What remains valid from Part II?

The following general idea is sound:

- For a fixed candidate \\(R\\), one can compute the relevant univariate determinantal gcd and verify the spectral condition exactly.
- For variable \\(R\\), one can form an incidence set recording pairs \\((R,\lambda)\\) at which the pencil drops rank.
- The bad augmentation set is the projection of this incidence set to the \\(R\\)-space.
- Projective compactification in \\(\lambda\\) is useful, provided the point at infinity is handled correctly.

But the incidence equations are generally polynomial in \\(R\\), not linear. So the appropriate geometry is a parameterised determinantal variety and its projection, rather than a union of affine subspaces.

## 3. Questions 1 and 2: the affine-covering problem

There is a meaningful general problem here, but it needs to be separated from the observer-specific claim.

### 3.1 General polynomial family of affine subspaces

Suppose

\\[ A(t)=\\{x\in\mathbb R^N:L(t)x=b(t)\\}, \\]

where \\(L(t)\\) and \\(b(t)\\) have polynomial entries in a real parameter \\(t\\).

The covering question is

\\[ \boxed{\mathbb R^N=\bigcup\_{t\in\mathbb R}A(t)?} \\]

Equivalently,

\\[ \forall x\in\mathbb R^N\ \exists t\in\mathbb R: L(t)x=b(t). \\]

This is a first-order sentence over the real numbers. It is therefore decidable by quantifier elimination over real closed fields. But this does not imply a simple resultant criterion or a polynomial-time algorithm. In general, the quantifier structure is universal-existential:

\\[ \forall x\ \exists t. \\]

That is substantially different from checking whether one univariate polynomial has a root or whether a fixed matrix pencil has constant rank.

For the complex version,

\\[ \mathbb C^N=\bigcup\_{t\in\mathbb C}A(t), \\]

one can instead use algebraic geometry. If the incidence set is defined over a projective parameter space, its projection is closed. In that setting, surjectivity onto \\(\mathbb C^N\\) can be tested by elimination: the image is all of \\(\mathbb C^N\\) precisely when its vanishing ideal is zero. This is a finite, computable algebraic condition, for example through elimination ideals or Gröbner-basis methods.

There are two qualifications:

- If the parameter is affine rather than projective, projection need not be closed. Dominance of the projection need not imply that every point is attained.
- A complex-algebraic surjectivity test does not decide whether every real \\(x\\) is covered by some complex parameter \\(t\\). That is a mixed real-complex quantifier problem and must be encoded with real and imaginary parts.

Thus, the answer to Question 1 is:

A finite decision procedure exists in general through real quantifier elimination (or algebraic elimination in the purely complex projective setting), but no general single-resultant or constant-rank criterion follows from the stated hypotheses.

A resultant can be useful in special cases—for example, when the family reduces to a pair of univariate polynomials with a common-root condition—but it is not a universal solution to the covering problem.

### 3.2 Why the dimension heuristic does not settle coverage

Even for a valid family of affine hyperplanes, dimension alone does not settle the critical case. A one-parameter family of hyperplanes can have a union of full ambient dimension without covering the ambient space.

For instance, in \\(\mathbb R^2\\), consider

\\[ A(t)=\\{(x,y):y=tx+t^2\\}. \\]

For a fixed \\((x,y)\\), membership means

\\[ t^2+xt-y=0. \\]

There is a real \\(t\\) precisely when

\\[ x^2+4y\geq0. \\]

Therefore the union is

\\[ \bigcup\_{t\in\mathbb R}A(t) =\\{(x,y):x^2+4y\geq0\\}, \\]

which has nonempty interior and full dimension, but is not all of \\(\mathbb R^2\\).

This example illustrates why a dimension estimate cannot distinguish coverage from noncoverage in the borderline case. It also shows that even a very simple polynomially parameterised family can lead to a nontrivial real inequality.

### 3.3 The observer-specific version is not currently an affine-covering problem

For the observer problem, the bad locus on a rank-\\(\omega\\), (5a)-admissible stratum is described by

\\[ \exists\lambda\in\mathbb C: \operatorname{rank}(\lambda H(R)-H_A(R))<\omega. \\]

Equivalently, all \\(\omega\\)-minors vanish at a common \\(\lambda\\).

The entries of the pencil are affine in \\(R\\), but its \\(\omega\\)-minors are generally degree-\\(\omega\\) polynomials in \\(R\\). The incidence set is therefore a determinantal algebraic set:

\\[ \mathcal I\_\omega = \left\\{(R,\lambda): \text{all }\omega\text{-minors of } \lambda H(R)-H_A(R)\text{ vanish} \right\\}. \\]

The bad set is its projection onto the \\(R\\)-coordinates. That is the correct geometric object.

This suggests the following replacement for the report's proposed covering question:

> Observer-specific projection problem. Given the affine matrix pencils \\(H(R),H_A(R)\\) arising from a fixed \\((A,C,L_0)\\), determine whether the projection of the rank-drop incidence variety covers the real points of a prescribed admissible rank stratum.

This formulation retains the useful geometric intuition while avoiding the unsupported affine-subspace assertion.

### 3.4 Is the observer-specific geometry more rigid?

Yes, it is more structured than an arbitrary polynomial family, but the relevant rigidity has not yet been converted into a decision theorem.

The key structural constraints are

\\[ H(R)=\mathcal L(R)N_K,\qquad H_A(R)=\mathcal L(R)AN_K, \\]

so the two coefficient matrices are not independent. In addition, (5a) imposes

\\[ \ker H(R)\subseteq\ker H_A(R). \\]

On a rank-\\(\omega\\) admissible stratum this gives

\\[ H=UV,\qquad H_A=GV, \\]

and reduces the spectral question to

\\[ S(\lambda)=\lambda U-G. \\]

That is real structure: the same full-row-rank factor \\(V\\) occurs in both coefficients, and the reduced pencil has only \\(\omega\\) columns. However, \\(U,G,V\\) are themselves existentially coupled to \\(R\\). This factorisation does not make the original bad locus affine-linear in \\(R\\).

My recommendation is to exploit this factorisation algebraically, as in the quadratic certificate, rather than to assume that it produces an affine-subspace covering problem.

## 4. Question 3: literature on the neighbouring problems

I would divide the literature into four groups. The distinctions matter: some results establish hardness for inequalities, some address polynomial-matrix rank, and some concern observer existence. They are related to REAL-AUG, but none of the results found so far proves hardness or tractability for your particular structured equality problem.

### 4.1 Bilinear matrix inequalities and control design

Toker and Özbay (1995) is correctly identified and is an important reference:

- O. Toker and H. Özbay, “On the NP-hardness of solving bilinear matrix inequalities and simultaneous stabilization with static output feedback,” Proceedings of the 1995 American Control Conference, vol. 4, pp. 2525–2526.
- DOI: [10.1109/ACC.1995.532300](https://doi.org/10.1109/ACC.1995.532300?utm_source=chatgpt.com).

The paper establishes NP-hardness for BMI feasibility and simultaneous stabilization by static output feedback.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://research.tue.nl\&sz=32)

埃因霍温科技大学研究门户+1



But there is an important distinction for your project:

\\[ \text{bilinear matrix inequality feasibility} \quad\ne\quad \text{bilinear matrix equality feasibility}. \\]

The Toker–Özbay result is strong evidence that nonconvex bilinear control design can be difficult. It is not a reduction to REAL-AUG. In particular, one cannot infer that REAL-AUG is NP-hard simply because its certificate contains bilinear equations.

For your problem, a more relevant observation is that general bilinear equation feasibility is already expressive enough to encode general quadratic feasibility. To see the basic mechanism, introduce two copies \\(x,y\\) of the original variables, impose the linear equalities \\(x=y\\), and represent each quadratic monomial \\(x_ix_j\\) as the bilinear monomial \\(x_i y_j\\). Linear and constant terms can be represented by including a homogenising coordinate fixed to one. Thus general bilinear equation feasibility is \\(\exists\mathbb R\\)-complete whenever general quadratic equation feasibility is used as the source problem.

The important unresolved question is not whether general bilinear equations are hard. It is whether that hardness survives the special shared-factor structure

\\[ H=UV,\qquad H_A=GV,\qquad X(\lambda)(\lambda U-G)=I\_\omega \\]

and the fact that \\(H,H_A\\) are generated by the same augmentation matrix \\(R\\).

That is the reduction challenge.

### 4.2 Existential theory of the reals and quadratic systems

The report's reference is appropriate:

\- M. Schaefer, J. Cardinal, and T. Miltzow, The Existential Theory of the Reals as a Complexity Class: A Compendium, arXiv:2407.18006 (2024).

It provides a broad account of \\(\exists\mathbb R\\), its relationship to real algebraic geometry, and known hard and complete problems.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



For the present project, I would use it to support three precise statements:

1. The quadratic certificate gives\
   \\[\
   \mathrm{REAL\text{-}AUG}(q)\in\exists\mathbb R.\
   \\]
2. General quadratic equation feasibility is an appropriate \\(\exists\mathbb R\\)-complete source problem for a possible hardness reduction.
3. No hardness conclusion follows until a polynomial-time many-one reduction into the observer-constrained system has actually been constructed.

I would also distinguish the standard discrete Turing model, with rational coefficients encoded in binary, from the Blum–Shub–Smale model over \\(\mathbb R\\). The phrase “polynomial time” can mean different things in those models. For the paper, the standard \\(\exists\mathbb R\\) formulation with rational input is the clearest choice.

### 4.3 Polynomial matrices, determinantal divisors, and rank-drop loci

This is a literature direction I would strengthen in the report.

The fixed-candidate spectral test is fundamentally a polynomial-matrix problem. For a polynomial matrix \\(S(\lambda)\\) of normal column rank \\(\omega\\), the gcd of its \\(\omega\\)-minors is its top determinantal divisor. Its Smith form describes the invariant factors and the finite rank-drop structure.

The classical reference to consult is:

\- T. Kailath, Linear Systems, Prentice-Hall, 1980 — polynomial matrices, Smith forms, invariant factors, and matrix pencils.

The relevant conceptual distinction is between:

- a univariate polynomial matrix with fixed coefficients, where Smith-form and gcd methods are available; and
- a parameterised polynomial matrix, whose entries also depend on design variables, where one must solve a multivariate algebraic feasibility problem.

The latter is much closer to REAL-AUG. Smith form solves the first problem for a fixed \\(R\\); it does not by itself solve the existential problem over \\(R\\).

For further background on polynomial matrices and polynomial right inverses, the literature on zero-left-prime (ZLP) matrices and unimodular completion is relevant. For example, the Quillen–Suslin theorem and its algorithmic developments concern polynomial matrices over multivariate polynomial rings and the existence of polynomial completions or right inverses under suitable hypotheses.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://onlinelibrary.wiley.com\&sz=32)

Wiley Online Library+1



I would not make Quillen–Suslin a central tool yet: your spectral parameter is univariate, and the central theorem already gives a bounded-degree certificate. But the polynomial-matrix viewpoint is useful for understanding why the certificate works and what changes when parameters are introduced.

### 4.4 Functional-observer literature: several important additions

The observer bibliography should be expanded. In addition to the papers already identified in the report, the following are particularly relevant.

Fernando, Trinh, and Jennings (2010)

“Functional Observability and the Design of Minimum Order Linear Functional Observers,” IEEE Transactions on Automatic Control, 55(5), 1268–1273.

DOI: [10.1109/TAC.2010.2042761](https://doi.org/10.1109/TAC.2010.2042761?utm_source=chatgpt.com).

This is a foundational minimum-order functional-observer paper. It introduces functional observability/detectability and establishes a minimum-order design framework.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

数字对象标识符+1



Fernando and Trinh (2013)

“A Procedure for Designing Linear Functional Observers,” Applied Mathematics Letters, 26(2), 240–243.

DOI: [10.1016/j.aml.2012.09.002](https://doi.org/10.1016/j.aml.2012.09.002?utm_source=chatgpt.com).

Relevant for low-order existence conditions and constructive design.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车



Fernando and Trinh (2014)

“A System Decomposition Approach to the Design of Functional Observers,” International Journal of Control, 87(9), 1846–1860.

DOI: [10.1080/00207179.2014.891293](https://doi.org/10.1080/00207179.2014.891293?utm_source=chatgpt.com).

Especially relevant to minimum-order structure and functional observability indices.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

数字对象标识符+1



Darouach and Fernando (2020)

“On the Existence and Design of Functional Observers,” IEEE Transactions on Automatic Control, 65(6), 2751–2759.

DOI: [10.1109/TAC.2019.2944904](https://doi.org/10.1109/TAC.2019.2944904?utm_source=chatgpt.com).

This paper revisits existence conditions, addresses controllability and stabilizability in the proof, and gives a general design algorithm and parametrisation of observers.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

数字对象标识符+1



Darouach and Fernando (2023)

“Functional Detectability and Asymptotic Functional Observer Design.”

This is relevant if the project later distinguishes arbitrary spectral feasibility from asymptotic or prescribed-region pole placement. It connects functional detectability, observer existence, and Sylvester-equation methods.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://research-repository.uwa.edu.au\&sz=32)

the UWA Profiles and Research Repository



Darouach and Fernando (2025)

“On Functional Observability and Functional Observer Design,” Automatica, 173, article 112115.

DOI: [10.1016/j.automatica.2025.112115](https://doi.org/10.1016/j.automatica.2025.112115?utm_source=chatgpt.com).

This is a recent treatment of functional observability and observer design. Its discussion explicitly recognises the possibility that a higher-dimensional observer may exist when a lower-dimensional one does not. That is particularly close to the order-by-order existence question in your project.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车



Fernando (2026), two recent preprints

- “A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions,” arXiv:2609.33615.
- “Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger,” arXiv:2609.37992.

These are particularly important to check against your current setup. They address intermediate observer orders, functional observability indices, and order-by-order algebraic and spectral feasibility.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



The 2026 preprints are especially relevant because they appear to address the order spectrum rather than only the classical minimum-order construction. I would compare definitions and theorem statements carefully before claiming novelty for the order-by-order framework. I would not, however, assume that they settle the computational complexity of existential augmentation: that is a separate question.

My literature conclusion: the observer theory is much richer than the report's current bibliography suggests, but the gap between necessary-and-sufficient observer existence conditions and the complexity of synthesising an augmentation of prescribed order remains a legitimate research direction. The existence conditions in these papers do not automatically imply a complexity classification for REAL-AUG.

## 5. Question 4: attack the critical case, or attempt a hardness reduction?

My recommendation is to stop treating the critical case in Part II.4 as the central bottleneck. The reason is not that the critical case is uninteresting; it is that it was derived from an invalid affine-subspace representation.

I would instead make the following the main research direction:

> Investigate whether REAL-AUG is \\(\exists\mathbb R\\)-hard by reducing a standard quadratic feasibility problem to the structured observer synthesis system.

But I would not start by attempting a direct reduction from arbitrary BMI feasibility. The Toker–Özbay result concerns inequalities, and the structure of your equations is more restrictive.

### 5.1 Why a direct reduction is the more promising direction

The current formulation has three useful properties:

1. It is already a polynomial-size quadratic feasibility problem.
2. Its variables and equations have a clear algebraic interpretation.
3. The spectral condition is encoded by a bounded-degree polynomial identity, rather than an infinite family of pointwise conditions.

These properties make a reduction from a standard \\(\exists\mathbb R\\)-complete problem a natural target.

The central obstacle is the observer-specific coupling:

\\[ H(R)=\mathcal L(R)N_K,\qquad H_A(R)=\mathcal L(R)AN_K. \\]

The two matrices are not independent. A reduction must respect the fact that both arise from one \\(R\\).

I would approach the reduction in stages:

Stage 1 — Understand the attainable coefficient pairs.

Characterise exactly which pairs

\\[ (H,H_A) \\]

can arise from a common \\(R\\). This is the most important structural preliminary. Treating \\(H\\) and \\(H_A\\) as independent matrices would make a reduction much easier, but would not prove anything about REAL-AUG.

Stage 2 — Identify a minimal hard subfamily.

Try to restrict the observer problem to small values of \\(\omega\\), simple \\(K\\), or carefully chosen \\(A,C,L_0\\). The aim is to determine whether even a restricted observer family can encode a known hard feasibility problem.

Stage 3 — Encode quadratic constraints.

Use the factorisation variables \\(U,V,G\\) and the polynomial left-inverse identity to represent the source problem. The hard part will be forcing the required algebraic relations through the shared \\(R\\)-dependence, not merely reproducing generic bilinear equations.

Stage 4 — Prove a polynomial-time many-one reduction.

The proof must explicitly show that:

- every source instance produces rational observer data of polynomial encoding size;
- every source solution produces a real admissible augmentation;
- every admissible augmentation produces a source solution;
- all auxiliary dimensions and coefficient bit lengths remain polynomially bounded.

Only then can you claim \\(\exists\mathbb R\\)-hardness.

### 5.2 Keep a smaller structural-geometry workstream

I would not discard the geometric approach altogether. Instead, reframe it around the determinantal incidence variety:

\\[ \mathcal I\_\omega = \left\\{(R,[\alpha:\beta]): \rank(\alpha H(R)-\beta H_A(R))<\omega \right\\}. \\]

The homogeneous parameter \\([\alpha:\beta]\in\mathbb P^1\\) is useful for compactification. The point \\([1:0]\\) corresponds to the leading coefficient \\(H(R)\\). On a rank-\\(\omega\\) stratum, this leading coefficient has full column rank, so no rank drop occurs at infinity.

This gives a projective incidence problem with a closed projection. It is a much better foundation for studying generic feasibility and exceptional parameter values than the affine-subspace cover in Part II.

However, I would keep this as a secondary project focused on:

- generic feasibility on irreducible components;
- exceptional parameter strata;
- real points of the projected bad locus;
- efficient elimination for the observer-induced determinantal family.

It is not yet a polynomial-time algorithm.

## 6. Question 5: additional recommendations for the observer problem

I would organise the bibliography around three themes rather than simply adding more observer papers.

### Theme A — Minimum-order functional observer theory

The most important references to compare directly against your work are:

1. Fernando, Trinh, and Jennings (2010).
2. Fernando and Trinh (2013, 2014).
3. Darouach and Fernando (2020, 2023, 2025).
4. Fernando (2026), the two recent preprints listed above.

These papers are important for the observer-existence and minimum-order background. In particular, the 2026 work should be checked carefully because it addresses order-by-order characterisation and intermediate observer dimensions.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+2



For your eventual paper, I would prepare a comparison table with columns for:

| Topic               | What to compare                                              |
| ------------------- | ------------------------------------------------------------ |
| Observer class      | Darouach, Luenberger, augmented/intermediate                 |
| Order parameter     | Fixed order or minimum order                                 |
| Algebraic condition | Rank condition and nullspace characterisation                |
| Spectral condition  | Matrix pencil and finite rank-drop condition                 |
| Augmentation        | Fixed, parametrised, or existentially synthesised            |
| Computation         | Constructive procedure, exact decision, or existence theorem |
| Complexity          | Any formal computational complexity result                   |

The last two columns are especially important. A paper can give necessary-and-sufficient existence conditions without addressing the complexity of deciding whether a suitable augmentation exists.

### Theme B — Algebraic geometry and real algebraic decision

For the geometry and complexity side, I recommend concentrating on:

- Real quantifier elimination and the existential theory of the reals;
- Determinantal varieties and incidence varieties;
- Elimination ideals and projective projection;
- Real points of complex algebraic varieties;
- Polynomial-matrix Smith forms and determinantal divisors.

The Schaefer–Cardinal–Miltzow compendium is a useful entry point for the complexity vocabulary and known reductions.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



For the observer problem, the most important distinction is between the complex-algebraic bad locus and its real points. Even if the complex projection is proper, that alone does not decide whether it contains every real augmentation in the relevant real stratum.

### Theme C — Nonconvex control synthesis

Toker–Özbay and the static-output-feedback literature should be used as motivation, not as a hardness proof.

The survey literature on static output feedback is useful for understanding why bilinear design conditions arise and why general BMI problems are difficult.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车+1



But your problem is not a standard static-output-feedback BMI. It is a structured polynomial equality feasibility problem with a special matrix-pencil certificate. The distinction should be explicit in any literature review.

## 7. Recommended revised research plan

I would revise the next phase of the project as follows.

1. Correct the standard formulation

   Retain REAL-AUG and REAL-AUG\\(\_\omega\\). Make the reduced-pencil identity

   \\[ X(\lambda)(\lambda U-G)=I\_\omega \\]

   the official quadratic certificate.
2. Withdraw the affine-covering claim in Part II

   Replace the proposed family of affine subspaces by the determinantal incidence variety. Keep the affine-covering question only as an independent abstract problem.
3. Establish exact candidate-verification complexity

   Specify rational or algebraic input representations and use polynomial-matrix algorithms rather than enumerating all maximal minors. State the bit-complexity model.
4. Study restricted observer families

   Start with small \\(\omega\\), restricted augmentation dimensions, and special choices of \\(A,C,L_0\\). Determine whether these cases admit structural algorithms or already exhibit difficult synthesis behaviour.
5. Attempt an \\(\exists\mathbb R\\)-hardness reduction

   Use general quadratic equation feasibility as the source problem. The main task is to encode its constraints through the attainable pairs \\((H,H_A)\\).
6. Complete the literature comparison

   Compare the current order-by-order theory with the 2026 Fernando preprints and the earlier functional-observer existence literature. Be precise about what is already known and what is new in the computational formulation.

## 8. Overall assessment

There are two very different levels of progress in this report.

Part I is a genuine advance. It establishes a standard decision problem and gives a polynomial-size quadratic certificate for each rank branch. The resulting \\(\exists\mathbb R\\) membership statement is well motivated and mathematically meaningful.

Part II is not yet a valid complexity argument. The maximal minors are not generally affine in \\(R\\), the spectral parameter is complex, and the dimension estimate does not yield the proposed polynomial-time tests. I would remove the claimed critical-case dichotomy from the current conclusions until a correct incidence formulation is developed.

My strongest recommendation is therefore:

Make REAL-AUG the central object, use the quadratic reduced-pencil system as its standard formulation, and investigate \\(\exists\mathbb R\\)-hardness through the observer-specific coupling constraints.

The geometric approach remains useful, but it should support that programme rather than determine it.

The next document I would prepare is a focused reduction-design report: first characterise the attainable pairs \\((H,H_A)\\), then identify the simplest observer instances capable of encoding nontrivial bilinear constraints. That is the most direct route from the current theorem to a substantive complexity result.