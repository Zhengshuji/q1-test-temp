# Research assessment of `33_q1_next_direction.md`

My overall recommendation is to pursue (c), the equivalence/barrier route, first—but make it a sharply defined structural investigation rather than a general search for an equivalent problem. In parallel, I would run one small computational experiment aimed at Question 3. I would not yet commit the project to an NP-hardness reduction, and I would not yet build a general Gröbner-basis algorithm.

The reason is specific to the structure established in Part II. The spectral obstruction has been reduced to a unit-gcd condition for a polynomial matrix whose coefficients depend affinely on the augmentation \\(R\\). That is a strong structural simplification. But it does not immediately yield either a standard hard problem or a polynomial-time algorithm. The most valuable next step is to identify exactly which established algebraic decision problem this special unit-gcd feasibility problem resembles—and, just as importantly, which features prevent a direct equivalence.

There is also one point in the report that I would check before building further arguments: the displayed definition of (5b) in line 19 contains

\\[ \lambda\mathcal L-\lambda\mathcal LA, \\]

whereas the earlier formulation in the project has been

\\[ \lambda\mathcal L-\mathcal LA. \\]

These are different pencils. The second is the usual pencil arising from \\(\lambda I-A\\); the first is \\(\lambda(\mathcal L-\mathcal LA)\\), which is a scalar multiple of a constant matrix and has a very different spectral condition. I will assume the intended condition is the established one,

\\[ Q\_{\mathcal L}(\lambda)= \begin{bmatrix} \lambda\mathcal L-\mathcal LA\\\ CA\\\ C \end{bmatrix}, \\]

but this must be corrected explicitly in the decision-problem definition. If the extra \\(\lambda\\) is intentional, the spectral and complexity analysis needs to be restarted for that different problem.

33_q1_next_direction.md

## 1. First audit: what the current results do and do not establish

The report's three principal structural results are valuable:

1. The spectral obstruction is controlled by the induced map on \\(W_K=\mathcal LK\\), not by an auxiliary eigenvalue parameter.
2. For a fixed admissible candidate, the spectral condition is equivalent to the gcd of the \\(\omega\times\omega\\) minors of \\(P_K(\lambda)\\) being a nonzero constant.
3. After stratifying by the rank \\(k\\) of \\(B(R)\\), the feasible parameter set is constructible.

These are meaningful reductions. In particular, the constructibility result is stronger and more precise than merely saying that the original condition is expressible by polynomial equations and inequations.

However, the following logical distinctions are essential for Question \\(q1\\).

### 1.1 Constructibility is not a complexity classification

The statement

\\[ \mathrm{FEAS}=\bigcup_k\mathcal C_k \\]

with each \\(\mathcal C_k\\) constructible establishes a geometric description of the feasible set. It does not establish that deciding whether this set is empty is polynomial-time solvable, NP-hard, or \\(\exists\mathbb R\\)-complete.

There are two separate complexity questions:

- Representation complexity: how many polynomial conditions and variables are needed to describe the feasible set?
- Decision complexity: how hard is it to determine whether at least one real \\(R\\) satisfies those conditions?

A compact representation can encode a difficult decision problem. Conversely, an exponentially large minor-based representation does not prove that the underlying problem is hard: it may be possible to exploit determinantal structure without enumerating all minors.

So I agree with the report's caution in Part II.5. I would make this distinction the guiding principle for the next phase.

### 1.2 The single-binomial minor count is an improvement, but not an algorithm

The report correctly improves the earlier count to

\\[ N\_{\mathrm{minor}}=\binom q\omega. \\]

This is a significant simplification compared with a product of two binomial coefficients. But the complexity of the full decision problem depends on more than this count:

- the number of real parameters in \\(R\\), namely \\((q-r)n\\);
- the degrees and coefficient bit-sizes of the minors as polynomials in \\(R\\) and \\(\lambda\\);
- the number of rank strata;
- the complexity of testing whether the corresponding constructible locus has a real point.

The observation that \\(\binom q\omega\\) is polynomially bounded when \\(\min(\omega,q-\omega)\\) is bounded is correct as an asymptotic statement with the other dimensions growing at most polynomially. But it does not by itself give a polynomial-time algorithm even in those regimes. One still needs a polynomial-size encoding and a polynomial-time method for the resulting real feasibility problem.

### 1.3 Be careful about the field and the quantifiers

The decision problem in the report has

\\[ R\in\mathbb R^{(q-r)\times n}, \qquad \lambda\in\mathbb C. \\]

This is a coherent mixed-field problem: the design variables are real, while the spectral condition excludes eigenvalues over the complex field.

It should be stated as a real decision problem with a universal complex spectral condition, or equivalently as a real-algebraic condition obtained by eliminating the spectral variable. The distinction matters when comparing it with complex constructibility and with \\(\exists\mathbb R\\).

For real \\(R\\), the condition that a real-coefficient polynomial in \\(\lambda\\) have no complex roots is not generally equivalent to a simple real-root exclusion. Nonreal roots occur in conjugate pairs. Any reduction or algorithm must preserve this complex spectral quantifier.

## 2. Question 1: which route should be pursued first?

### My ranking

| Route                   | Recommendation       | Reason                                                                                                                                        |
| ----------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| (c) Equivalence/barrier | First                | Cheapest way to determine whether the problem is a known algebraic decision problem in disguise; may identify the right complexity framework. |
| (a) Hardness            | Second, but targeted | There is a promising nearby NP-hard control problem, but no direct reduction is currently justified.                                          |
| (b) Algorithm           | Third, initially     | The polynomial-matrix viewpoint is useful, but the obvious Gröbner/resultant route risks merely repackaging elimination.                      |

I would not interpret “(c) first” as a reason to stop investigating hardness. Rather, the equivalence investigation should tell you what the correct source problem for a reduction might be.

### 2.1 Route (c): identify the exact algebraic problem

For a fixed candidate \\(R\\), the relevant polynomial matrix is

\\[ P_R(\lambda)=\lambda\iota\_{K,R}-\Phi\_{K,R}, \\]

where

\\[ \iota\_{K,R}:W\_{K,R}\hookrightarrow\mathbb C^q. \\]

The condition is that \\(P_R(\lambda)\\) have full column rank for every finite \\(\lambda\in\mathbb C\\).

Equivalently, the maximal minors of \\(P_R\\) have no common finite complex zero, or their gcd is a nonzero constant.

This has a natural interpretation in polynomial-matrix theory: the matrix is left-prime in the univariate sense relevant here, in that its maximal minors have no nonconstant common factor. Terminology varies between authors and conventions, so I would define the property explicitly rather than rely on the label alone.

The crucial point is that this is a zero-exclusion condition for a rectangular polynomial matrix, not ordinary eigenvalue placement for a square matrix.

That distinction should guide the equivalence search. I would investigate the following neighbouring problems, in this order.

1\. Full-column-rank polynomial matrix completion.\
Given a polynomial matrix with some free affine parameters, can one choose the parameters so that the matrix has full column rank at every finite complex value of \\(\lambda\\)? This is the closest formulation to the current problem.

2\. Polynomial-matrix left-prime completion.\
Given a partially specified or affine-parameterized polynomial matrix, can the free entries be chosen so that the maximal minors have gcd one? This is especially close to the Bézout formulation in the report.

3\. Zero exclusion for affine matrix pencils.\
Given \\(M_0+\sum_i x_iM_i+\lambda N\\), can the real parameters \\(x_i\\) be chosen so that the pencil has no finite rank drop over \\(\mathbb C\\)? This is a natural intermediate decision problem between the observer formulation and general polynomial-matrix completion.

4\. Structured rank completion and structured singularity.\
These may supply a source of hardness or a known algorithmic barrier, but the exact quantifiers and the permitted parameter structure must match.

I would not yet claim equivalence to any one of these. The present problem has additional structure: \\(K=\ker[C;CA]\\) is fixed by the plant, \\(W\_{K,R}=\mathcal L(R)K\\) varies with \\(R\\), and \\(\Phi\_{K,R}\\) is induced by the pair \\((\mathcal L(R),\mathcal L(R)A)\\). An arbitrary affine polynomial-matrix completion problem need not have that form.

The quotient dependence is not a superficial technicality. It is part of the structure that a valid reduction or equivalence theorem must preserve.

### 2.2 A useful algebraic reformulation

There is a potentially productive way to express the fixed-candidate condition without listing all maximal minors.

Let \\(P_R(\lambda)\\) be a \\(q\times\omega\\) polynomial matrix of full column normal rank. Its maximal minors are \\(p_1(\lambda),\ldots,p_N(\lambda)\\). The condition is

\\[ \exists u_1(\lambda),\ldots,u_N(\lambda): \qquad \sum\_{i=1}^N u_i(\lambda)p_i(\lambda)=1. \\]

This is a Bézout identity, and it says exactly that the ideal generated by the maximal minors in \\(\mathbb C[\lambda]\\) is the unit ideal.

But the family problem asks for

\\[ \exists R\in\mathbb R^{(q-r)\times n} \quad \text{such that}\quad \big(p_1(R,\lambda),\ldots,p_N(R,\lambda)\big) =\mathbb C[\lambda]. \\]

One must distinguish this from asking whether the ideal generated by the \\(p_i\\) in the multivariate ring \\(\mathbb C[R,\lambda]\\) is the unit ideal. These are not equivalent.

For example, the polynomial \\(p(R,\lambda)=R\lambda+1\\) has gcd one as a polynomial in \\(\lambda\\) at \\(R=0\\), since \\(p(0,\lambda)=1\\). But the ideal \\((R\lambda+1)\\) in \\(\mathbb C[R,\lambda]\\) is not the unit ideal. Conversely, a multivariate ideal may be the unit ideal for reasons that do not express the existence of a real parameter value satisfying the required univariate gcd condition in the way intended.

The correct algebraic object is a parameterized family of univariate ideals, evaluated at a real point \\(R\\). This distinction is important if you explore elimination or Gröbner bases.

### 2.3 Route (a): hardness candidates

The most plausible source is not arbitrary quadratic feasibility. It is a problem whose central condition already concerns the existence of a real parameter choice making an affine family of matrices or polynomial matrices satisfy a spectral or rank property.

I would investigate these candidates:

- affine matrix-pencil zero-exclusion;
- structured polynomial-matrix completion;
- structured rank completion with a parameter-dependent kernel;
- real feasibility of determinantal conditions with a spectral parameter eliminated.

The last candidate is particularly natural because the project already produces a constructible parameter locus defined by rank conditions.

I would be more cautious about the following candidates.

Arbitrary \\(\exists\mathbb R\\)-complete geometric problems. A generic reduction from point-line incidence, order-type realizability, or another geometric problem would need to encode many independent polynomial constraints into the special observer pencil. The fact that the spectral criterion contains quadratic equations in projective coordinates does not automatically give that encoding: those coordinates are not free independent design variables; they represent lines in \\(W_K\\), and the matrix defining the map is constrained by \\(A,C,L_0,R\\).

Generic rank-one feasibility. This may be useful if the induced map can be made to encode a rank-one condition, but it is not enough to observe that both problems involve rank constraints. A reduction must preserve the yes/no answer and have polynomial encoding size.

Ideal membership by itself. The unit-gcd test for a fixed candidate is an ideal-membership statement in \\(\mathbb C[\lambda]\\), but the hardness question is about choosing \\(R\\). Fixed-candidate gcd computation is not the same problem as existential parameter selection.

My advice is to begin with the simplest possible source problem: a parameterized rectangular pencil whose full-column-rank condition is required for all complex \\(\lambda\\). If that problem is already known to be hard, the next task is to embed it into the observer structure. If it is known to be tractable under the same affine restrictions, that would be equally informative.

## 3. Question 2: does static output-feedback NP-hardness transfer?

Not automatically. The gap is real, and a reduction must bridge it.

The report cites Löfberg's 2026 preprint, which proves NP-hardness of unrestricted static output-feedback stabilization by a reduction from Betweenness. Its construction concerns the existence of a real gain \\(K\\) such that

\\[ A+BKC \\]

is Hurwitz. The paper's abstract also describes a related NP-hard affine polynomial-family problem on a rational box.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arcxiv.org\&sz=32)

ArcXiv+1



This is a significant nearby result, but it is not a reduction to the present problem.

### 3.1 The spectral predicates are different

Static output-feedback stabilization asks for all eigenvalues of a square closed-loop matrix to lie in the open left half-plane:

\\[ \sigma(A+BKC)\subset\\{z:\operatorname{Re}z<0\\}. \\]

Your condition asks for a rectangular pencil to have full column rank at every finite complex \\(\lambda\\):

\\[ \operatorname{rank}P_R(\lambda)=\omega \qquad\forall\lambda\in\mathbb C. \\]

These are different spectral predicates.

- Stabilization permits eigenvalues, but requires them to lie in a specified region.
- Your condition excludes every finite value at which the pencil loses column rank.
- The stabilization problem is naturally expressed through a characteristic polynomial and Hurwitz inequalities.
- Your condition is naturally expressed through a common-zero exclusion condition for maximal minors.

A direct identification of the two would therefore be incorrect.

### 3.2 The rectangular structure matters

In the observer problem, the inclusion

\\[ \iota\_{K,R}:W\_{K,R}\hookrightarrow\mathbb C^q \\]

is part of the pencil. If \\(\omega=q\\), the pencil is square. In that case, the induced map \\(\Phi\_{K,R}:W\_{K,R}\to\mathbb C^q=W\_{K,R}\\) is an endomorphism of a nonzero complex vector space and necessarily has an eigenvector. Thus the spectral condition fails whenever \\(\omega=q>0\\).

This is already a useful structural restriction. In the nontrivial feasible case, one generally needs a genuinely rectangular pencil, with

\\[ \omega\<q. \\]

That is quite different from the ordinary square closed-loop matrix in static output feedback.

### 3.3 The quotient structure is probably the main obstacle

The dependence of \\(W\_{K,R}\\) on \\(R\\) is important, but I would describe the obstacle more precisely:

- In static output feedback, the gain appears in a prescribed affine closed-loop matrix \\(A+BKC\\).
- Here, \\(R\\) changes both the image subspace \\(W\_{K,R}\\) and the induced map \\(\Phi\_{K,R}\\) on that image.
- The spectral predicate is evaluated on the resulting rectangular pair \\((\iota\_{K,R},\Phi\_{K,R})\\), not on a fixed square matrix.

Thus, even if one could encode the entries of \\(A+BKC\\) into \\(\mathcal L(R)A\\), the target condition would still not be Hurwitz stability. One would need an additional construction that translates the source's stability inequalities into the target's rank-drop exclusion condition.

### 3.4 What a valid transfer would need to prove

I would look for a reduction in two stages:

1. Spectral-predicate translation: construct a rectangular pencil \\(P_K(\lambda)\\) whose full-column-rank-for-all-\\(\lambda\\) condition is equivalent to the source stability condition.
2. Observer-structure realization: show that this pencil can be represented as\
   \\[\
   P_K(\lambda)=\lambda\iota\_{K,R}-\Phi\_{K,R}\
   \\]\
   for some polynomial-size observer instance \\((A,C,L_0,q)\\), with the free parameters corresponding to the source gain.

Both stages must preserve real design variables, complex spectral quantification, and polynomial encoding size.

The first stage is already nontrivial. The second is a further structural embedding problem. I would not assume either one.

My assessment: the Löfberg result is a useful source of ideas about encoding sign constraints through spectral information, but it is not presently evidence that your decision problem is NP-hard. It should be treated as a candidate source construction, not as a nearly completed reduction.

## 4. Question 3: the smallest case \\(n=4,\ p=1,\ q=2,\ r=1\\)

This is potentially the most informative experiment in the report. It is small enough to analyse explicitly, and the geometry is unusually restrictive.

There is, however, a dimensional inconsistency in the question as written:

\\[ q-r=2-1=1, \\]

so the augmentation variable is

\\[ R\in\mathbb R^{1\times4}, \\]

not \\(\mathbb R^{2\times4}\\).

If the intended parameter space is \\(\mathbb R^{2\times4}\\), then either \\(q\\) or \\(r\\) must be different. I will analyse the stated values \\(n=4,p=1,q=2,r=1\\).

### 4.1 Generic dimension of the fixed subspace

Suppose the data are generic enough that

\\[ \operatorname{rank}\begin{bmatrix}C\\\CA\end{bmatrix}=2. \\]

Then

\\[ \dim K=4-2=2. \\]

For any candidate \\(\mathcal L\in\mathbb R^{2\times4}\\), the restricted map

\\[ \mathcal L|\_K:K\longrightarrow\mathbb R^2 \\]

has rank

\\[ \omega\in\\{0,1,2\\}. \\]

Since \\(q=2\\), the three cases can be completely separated.

### 4.2 The case \\(\omega=2\\): automatically spectrally infeasible

If \\(\omega=2\\), then

\\[ W_K=\mathbb R^2. \\]

The induced map

\\[ \Phi_K:W_K\longrightarrow\mathbb R^2=W_K \\]

is a square real linear map. Over \\(\mathbb C\\), every nonzero square matrix has an eigenvalue and an eigenvector.

Consequently, there is a nonzero \\(w\in W_K\otimes\_\mathbb R\mathbb C\\) and a \\(\lambda\in\mathbb C\\) such that

\\[ \Phi_K(w)=\lambda w. \\]

This is precisely the forbidden invariant-line condition.

Therefore,

\\[ \boxed{\omega=2\quad\Longrightarrow\quad (5b)\text{ fails}.} \\]

This conclusion is unconditional once the induced map is defined.

### 4.3 The case \\(\omega=1\\): a single scalar geometric obstruction

Now suppose

\\[ W_K=\operatorname{span}\\{w\\} \\]

for some nonzero \\(w\in\mathbb R^2\\).

The spectral condition fails exactly when

\\[ \Phi_K(w)\in\operatorname{span}\\{w\\}. \\]

In two dimensions, this is equivalent to

\\[ \det\begin{bmatrix}w&\Phi_K(w)\end{bmatrix}=0. \\]

Thus the condition for spectral feasibility becomes

\\[ \boxed{ \det\begin{bmatrix}w&\Phi_K(w)\end{bmatrix}\ne0. } \\]

Geometrically, the image \\(\Phi_K(w)\\) must not lie on the line \\(W_K\\).

This is a particularly simple and useful fact: when \\(\omega=1\\), the spectral condition is not a complicated collection of polynomial inequalities. It is one nonvanishing condition, once a representative \\(w\\) and the induced map have been expressed in coordinates.

### 4.4 The case \\(\omega=0\\): automatically spectrally feasible

If

\\[ W_K=\\{0\\}, \\]

then there is no nonzero vector \\(w\\) on which an invariant line could be formed. Equivalently, \\(P_K(\lambda)\\) has zero columns, so the full-column-rank condition is vacuous.

Therefore,

\\[ \boxed{\omega=0\quad\Longrightarrow\quad (5b)\text{ holds}.} \\]

This does not imply that (5a) holds. The algebraic condition must still be imposed.

### 4.5 A concrete algebraic consequence for the parameter space

Choose a basis of \\(K\\), and let

\\[ H(R)=\mathcal L(R)|\_K \\]

be the \\(2\times2\\) matrix representing the restriction. Then

\\[ \omega=\operatorname{rank}H(R). \\]

The preceding analysis gives the necessary condition

\\[ \operatorname{rank}H(R)\le1 \\]

for spectral feasibility. Hence

\\[ \det H(R)=0. \\]

Because

\\[ \mathcal L(R)= \begin{bmatrix} L_0\\\R \end{bmatrix}, \\]

the first row of \\(H(R)\\) is fixed, while the second row depends linearly on \\(R\\). Consequently, \\(\det H(R)\\) is an affine-linear polynomial in the four entries of \\(R\\).

If

\\[ L_0|\_K\ne0, \\]

then this affine-linear polynomial is not identically zero: because \\(K\\) is two-dimensional, one can choose the restriction of the second row \\(R\\) to be linearly independent of \\(L_0|\_K\\).

It follows that, under these generic hypotheses,

\\[ \boxed{ \mathrm{FEAS}\subseteq \\{R\in\mathbb R^4:\det H(R)=0\\}, } \\]

where the right-hand side is a proper affine hypersurface (in fact, a hyperplane in these coordinates).

This is a genuine geometric conclusion for the stated small case.

There are two qualifications:

1. If \\(L_0|\_K=0\\), the determinant may vanish identically, so the argument does not establish a proper hypersurface.
2. The hypersurface condition is only necessary. It does not by itself establish (5a), nor does it establish the \\(\omega=1\\) noninvariance condition.

### 4.6 What can be said about dimension and degree?

Under the generic assumptions just stated, the feasible set is contained in a hyperplane in \\(\mathbb R^4\\). Therefore its real dimension is at most three.

But I would not claim that its dimension is exactly three, or that its degree is one, without analysing the remaining conditions.

For example:

- the admissible locus (5a) may cut out a smaller subset;
- the \\(\omega=1\\) noninvariance condition removes the part where the induced map preserves \\(W_K\\);
- the \\(\omega=0\\) locus may have a different dimension;
- the union of the resulting strata need not itself be a variety.

In particular, the feasible set is generally constructible, not necessarily a variety. Its Zariski closure may have a different dimension from the feasible set itself.

I would therefore formulate the small-case problem as follows:

> For generic rational data \\(A,C,L_0\\) satisfying \\(\dim K=2\\) and \\(L_0|\_K\ne0\\), determine the constructible subset of \\(\mathbb R^4\\) satisfying (5a) and (5b), and compute the dimension and degree of the Zariski closure of each nonempty rank stratum.

This is a well-defined and manageable research task.

### 4.7 Suggested exact computation

I would use rational symbolic computation, not floating-point sampling.

1. Choose rational \\(A,C,L_0\\) with \\(\operatorname{rank}[C;CA]=2\\).
2. Compute an exact rational basis matrix \\(N_K\in\mathbb Q^{4\times2}\\) for \\(K\\).
3. Write\
   \\[\
   H(R)=\mathcal L(R)N_K.\
   \\]
4. Compute \\(\det H(R)\\) symbolically.
5. Restrict to \\(\det H(R)=0\\), and separate:\
   \\[\
   \operatorname{rank}H(R)=0,\qquad\
   \operatorname{rank}H(R)=1.\
   \\]
6. On the rank-one stratum, choose charts by specifying a nonzero entry of \\(H(R)\\). In each chart, derive the induced map \\(\Phi_K\\) exactly and impose\
   \\[\
   \det[w,\Phi_K(w)]\ne0.\
   \\]
7. Impose (5a) exactly, using polynomial rank conditions.
8. Compute the dimensions and degrees of the resulting algebraic pieces, then verify that their union gives the feasible set.

For the first experiment, I would choose data that make the induced map and rank-one chart particularly simple. A generic random rational example is useful as a check, but it is not a substitute for the symbolic description.

Why this experiment matters: it tests whether the special structure produces a low-dimensional feasible set, and whether the rank restriction alone captures most of the geometry. It may also reveal a simple parameterization that could be used in a reduction or an algorithm.

## 5. Question 4: which way would I bet?

My current bet is:



Tentative assessment

&#x20;The unrestricted decision problem is more likely to be computationally hard than to admit a general polynomial-time algorithm, but I would not yet bet specifically on NP-hardness without a reduction.



There are three reasons for this view.

First, the design variable \\(R\\) is free and enters the induced spectral structure nontrivially. The requirement that an affine family of rectangular pencils avoid all finite complex rank drops is a global condition, not a local rank test.

Second, the feasible set is constructible, but constructible-set nonemptiness over the reals can still be difficult. The rank-stratified description does not remove the existential search over \\(R\\).

Third, the nearby static output-feedback literature demonstrates that spectral design problems with affine parameter dependence can encode combinatorial difficulty. Löfberg's preprint provides a concrete NP-hardness construction for stabilization, although, as discussed above, it does not yet transfer to this problem.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arcxiv.org\&sz=32)

ArcXiv+1



I would distinguish three possible outcomes:

1. NP-hardness: a reduction from a combinatorial problem such as Betweenness or Subset Sum.
2. \\(\exists\mathbb R\\)-hardness: a reduction from a general real-algebraic feasibility problem.
3. A structural algorithm: an algorithm exploiting the special quotient and polynomial-matrix structure that avoids general real-algebraic elimination.

I consider the first two plausible, but neither is established. The third is also plausible in restricted regimes, particularly if the effective rank \\(\omega\\) or the number of free augmentation parameters is small.

### The cheapest computation that could falsify my bet

I would not start with a large random search for feasible or infeasible instances. Such a search is unlikely to distinguish between hardness and tractability.

Instead, I would compute the generic dimension and codimension of the feasible set for the smallest nontrivial parameter family, initially the \\(n=4,p=1,q=2,r=1\\) case.

More specifically:

- If the feasible set is generically empty, or confined to a very low-dimensional algebraic subset, that may reveal a strong structural obstruction and suggest a direct algebraic criterion.
- If it is generically a nonempty open subset of an admissible rank stratum, that would indicate a different geometry: feasibility may be robust once the algebraic rank condition is met.
- If the feasible set is a complicated union of components with varying dimensions, this would support the view that the existential search is genuinely nontrivial.

This experiment is cheap relative to a hardness reduction and gives concrete information about the geometry that any reduction or algorithm must respect.

I would also test whether the observed codimension persists as \\(n\\) increases while \\(q,p,r\\) are held fixed. A stable low-codimension pattern might suggest a parameterization; a rapidly growing number of components might suggest algebraic complexity.

## 6. A further issue I would address before pursuing any complexity theorem

There is an important distinction in the report between the fixed-candidate and family-level descriptions.

For a fixed candidate, the reduced pencil

\\[ P_K(\lambda):W_K\longrightarrow\mathbb C^q \\]

has \\(\binom q\omega\\) maximal minors.

But \\(W_K=\mathcal L(R)K\\) depends on \\(R\\). To obtain a single polynomial representation of the family problem, one must choose coordinates for \\(W_K\\), and those coordinates can only be chosen consistently on suitable rank charts.

The direct matrix

\\[ Q\_{\mathcal L}(\lambda)= \begin{bmatrix} \lambda\mathcal L-\mathcal LA\\\ CA\\\C \end{bmatrix} \\]

has fixed ambient dimensions, and its rank-stratified determinantal description is globally convenient. However, its \\(k\times k\\) minors are counted by

\\[ \binom{q+2p}{k}\binom nk, \\]

not by \\(\binom q\omega\\).

This does not invalidate the reduced-pencil approach. It means that the attractive single-binomial count in Part II.2 is, at present, a fixed-candidate or chartwise count, not automatically a global polynomial-size representation of the family problem.

I would make this distinction explicit in the next report.

A promising way forward is to stratify first by

\\[ \omega=\operatorname{rank}(\mathcal L(R)|\_K), \\]

then cover each rank stratum by finitely many coordinate charts. On each chart:

- choose a nonzero \\(\omega\times\omega\\) minor of the restriction matrix;
- construct a rational basis for \\(W_K\\);
- express \\(\Phi_K\\) in that basis;
- clear chart denominators in the maximal minors;
- impose the unit-gcd condition.

This would give a chartwise polynomial description of the reduced spectral condition. The main issue is whether the number and size of the charts remain polynomial in the input size.

I would investigate that before making any complexity claim based on the \\(\binom q\omega\\) count.

## 7. My broader view of the project

The project has reached a point where the main mathematical structure is substantially clearer than the complexity classification. I regard that as real progress, not as a detour.

### 7.1 What I consider genuinely strong

First, the reduction to \\(W_K\\) is the right conceptual level. It isolates the spectral obstruction in a subspace determined by the augmentation and gives a direct geometric criterion. This is more informative than relying solely on a Kronecker-form decomposition.

Second, the invariant-line formulation is especially valuable. It makes the spectral obstruction a projective incidence problem:

\\[ \mathcal E_K = \\{[w]\in\mathbb P(W_K): \Phi_K(w)\wedge\iota_K(w)=0\\}. \\]

This is a clean description that can be used in both theoretical and computational work.

Third, the constructibility result is a useful bridge to complexity theory. It establishes that the feasible locus is not an arbitrary analytic set: it is governed by finite algebraic rank conditions and a univariate unit-gcd test. That gives a precise algebraic object to study.

Fourth, the distinction between fixed-candidate and family-level complexity is becoming increasingly important. The project is now in a position to ask not merely whether a condition is algebraic, but how its representation changes when the subspace \\(W_K\\) itself varies.

### 7.2 What I would avoid

I would avoid three temptations.

1. Do not infer NP-hardness from static output feedback alone. The spectral predicates differ.
2. Do not infer tractability from constructibility. A finite algebraic description can still have difficult real-point existence.
3. Do not equate the number of reduced-pencil minors with the global family encoding size. The varying image subspace requires rank stratification and charts.

These are not minor technicalities. They are the points on which a correct complexity argument will turn.

### 7.3 A research plan I would actually follow

I recommend the following order.

Stage 1 — Close the formulation

Immediate

- Correct the (5b) formula in the report.
- State the input model: rational data, real \\(R\\), and binary encoding.
- State whether \\(q\\) is part of the input or fixed.
- Prove the chartwise family version of the reduced-pencil criterion.

  Stage 2 — Small-case geometry

  Immediate
- Work out \\(n=4,p=1,q=2,r=1\\) exactly.
- Determine the rank strata \\(\omega=0,1,2\\).
- Compute the feasible locus, its components, dimensions, and degrees for explicit rational data.

  Stage 3 — Equivalence search

  Next
- Compare with polynomial-matrix left-prime completion.
- Compare with affine rectangular-pencil zero exclusion.
- Determine whether the observer-induced family is a proper subclass of either problem.

  Stage 4 — Complexity

  After Stage 3
- Attempt a reduction from a problem with a matching spectral predicate.
- If no direct reduction emerges, establish an equivalence or a precise restricted-case algorithm.
- Separately analyse fixed-\\(\omega\\), fixed-\\(q\\), and fixed-\\(p\\) regimes.

### 7.4 One more important complexity-theoretic recommendation

The report defines \\(\mathrm{DEC}(q)\\) with \\(q\\) as an input. This is the right starting point, but I would explicitly define the input encoding.

For example:

- \\(A,C,L_0\\) have rational entries encoded in binary;
- \\(q\\) is encoded in binary or unary, as appropriate;
- \\(R\\) is existentially quantified over real matrices;
- the spectral condition is required for all \\(\lambda\in\mathbb C\\).

The binary-versus-unary convention for \\(q\\) can affect polynomial reductions if the matrix dimensions are allowed to grow. In a standard matrix-input encoding, the dimensions are already reflected in the input size, but it is better to state this than leave it implicit.

I would also distinguish:

\\[ \mathrm{DEC}\_{\mathrm{fixed}\ q} \quad\text{from}\quad \mathrm{DEC}\_{\mathrm{variable}\ q}. \\]

If \\(q\\) is fixed, the number of augmentation rows is fixed, and the problem may have a different complexity profile from the variable-order problem. Likewise, fixed \\(p\\) and fixed \\(q\\) are different parameter regimes.

Finally, if the goal is the optimisation problem \\(q\_{\min}\\), the threshold decision problem must include infeasibility conventions and a known finite upper bound on the search range. The report's assertion that an algorithm for \\(q\_{\min}\\) yields a decision algorithm is correct when the optimisation problem is well-defined and its output includes infeasibility, but the finite search domain and input encoding should be stated.

## 8. Final answers to the four questions

| Question                                              | My answer                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Q1. Which route first?                                | (c), equivalence/barrier. Then targeted (a). Defer a general (b) algorithm until the family representation is understood.                                                                                                                                                                                                                          |
| Q2. Does static output-feedback NP-hardness transfer? | No direct transfer is known from the cited result. Stabilization and rectangular-pencil zero exclusion are different spectral predicates. The quotient structure is an additional embedding obstacle.                                                                                                                                              |
| Q3. Smallest case?                                    | For \\(n=4,p=1,q=2,r=1\\), \\(R\in\mathbb R^{1\times4}\\), not \\(\mathbb R^{2\times4}\\). If \\(\dim K=2\\) and \\(L_0\|\_K\ne0\\), spectral feasibility forces \\(\det(\mathcal L\|\_K)=0\\), a proper affine hyperplane. Exact dimension and degree of the feasible locus still require imposing (5a) and the rank-one noninvariance condition. |
| Q4. Which way to bet?                                 | I lean toward computational hardness in the unrestricted setting, but NP-hardness remains unproved. The most informative inexpensive test is exact dimension and component analysis of the smallest nontrivial family.                                                                                                                             |

My strongest recommendation: make the next research milestone a complete chartwise description of the family-level reduced pencil, followed immediately by the exact \\(n=4,p=1,q=2,r=1\\) computation. Those two tasks will tell you whether the current structural simplification can be converted into a genuine complexity advantage—or whether the varying quotient \\(W_K\\) retains enough freedom to support a hardness reduction.

The project is now at a good point to make that distinction rigorously. The next step should be chosen to resolve it, rather than to accumulate another general reformulation.

### Sources consulted

- Fernando, A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions, arXiv:2609.33615.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

  arXiv

- Fernando, Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger, arXiv:2609.37992.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

  arXiv

- Löfberg, Static output-feedback stabilization is NP-hard, arXiv:2609.16886.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://arcxiv.org\&sz=32)

  ArcXiv

- Fu, Pole placement via static output feedback is NP-hard, IEEE Transactions on Automatic Control, 2004.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://dblp.dagstuhl.de\&sz=32)

  dblp
