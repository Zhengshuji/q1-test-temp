# Research assessment of `29_status_and_requests.md`

## 1. Overall assessment

The project has reached a significant change in mathematical maturity. The central issue is no longer simply how to characterize the rank condition (5b), nor how to compute the minimum dimension imposed by the invariant-subspace condition (5a). Those aspects have acquired a substantial structural theory.

The remaining problem is considerably more specific:

> Given the algebraically admissible augmentations satisfying (5a), determine whether one can choose an augmentation for which the associated pencil has no finite rank-drop point, and determine the minimum order at which this is possible.

I regard this as a constrained spectral-avoidance problem, rather than a conventional matrix-rank minimization problem.

My main conclusions are:

1\. The intrinsic spectral characterization B.23–B.24 is potentially the most important conceptual advance in the current work. It identifies the obstruction as a partial eigenvector phenomenon, rather than merely a condition on the dimensions of several subspaces.

2\. B.17 and B.23–B.24 are complementary, not competing, descriptions. B.17 explains the kernel structure and its permanent component. B.23–B.24 gives a more explicit spectral interpretation of the finite rank-drop obstruction. Together they provide a strong foundation for a unified theorem.

3\. Approach B is the better immediate research direction, but there is an important mathematical distinction: eliminating the enumeration of Grassmannian charts does not automatically produce a polynomial-time algorithm. One must still solve the partial eigenvector existence problem over the relevant family of admissible augmentations.

4\. Approach A is viable in principle, but neither F.1 nor B.13c currently provides a sufficiently flexible reduction interface. In particular, B.13c is a useful geometric sufficient condition, but its base-locus hypothesis is exceptionally restrictive.

5\. The paper should distinguish three different contributions: the fixed-candidate spectral criterion, the structural characterization of admissible layers, and the unresolved complexity of selecting an admissible layer. These should not be presented as if they were all consequences already established in the cited characterization papers.

6\. The complexity question is genuinely open on the evidence supplied. An upper bound in \\(\exists\mathbb R\\) is important, but it does not establish \\(\exists\mathbb R\\)-hardness, NP-hardness, or a polynomial algorithm.

I will address the five questions in turn, but first I want to clarify the logical structure of the problem because it determines which reductions and algorithms are mathematically appropriate.

# 2. The correct complexity-theoretic formulation

## 2.1 Three problems that must remain distinct

There are three closely related computational problems.

Problem A: Fixed-order feasibility

Given \\(A,C,L_0\\), and an integer \\(q\\), decide whether there exists a free block \\(R\\) such that

\\[ \mathcal L=\begin{bmatrix}L_0\\\R\end{bmatrix} \\]

satisfies (5a) and (5b).

Call this problem DEC\\((q)\\).

Problem B: Minimum-order computation

Compute

\\[ q\_{\min}= \min\\{q:\operatorname{DEC}(q)\text{ is feasible}\\}. \\]

This is the optimization problem in the original formulation.

Problem C: Fixed-candidate verification

Given a particular matrix \\(\mathcal L\\), determine whether (5a) and (5b) hold.

These are not equivalent complexity problems.

The third problem is substantially easier because the unknown augmentation has disappeared. The fixed-candidate spectral condition can be checked using polynomial-time linear algebra and polynomial arithmetic.

In particular, the Smith/gcd criterion B.8 provides an exact algebraic test:

\\[ \operatorname{rank}Q\_{\mathcal L}(\lambda)=h \quad\forall\lambda\in\mathbb C \\]

if and only if the gcd of all maximal minors is a nonzero constant.

Thus, the difficulty is not testing a proposed augmentation. It is finding one.

This distinction should be emphasized throughout the paper.

## 2.2 Relationship between DEC\\((q)\\) and \\(q\_{\min}\\)

Because the admissible order range is finite, a polynomial-time algorithm for DEC\\((q)\\) would yield a polynomial-time algorithm for \\(q\_{\min}\\), provided the relevant input representation and arithmetic model are fixed.

Indeed, one can test the admissible orders sequentially:

\\[ q=q_0,q_0+1,\ldots,n_0-p. \\]

The number of tests is at most linear in the dimension.

Conversely, an algorithm computing \\(q\_{\min}\\) immediately decides whether an admissible order exists at or below any given threshold \\(k\\):

\\[ q\_{\min}\le k. \\]

Therefore, the optimization and threshold-decision formulations are polynomially equivalent, subject to the usual conventions for infeasible instances.

There is, however, an important logical qualification concerning the statement in the uploaded note:

> If DEC-\\(\Theta\\) is polynomial, then the NP-hardness question is false.

That is too strong as a statement of unconditional complexity theory.

The correct statement is:

\\[ \boxed{ \text{DEC-\\(\Theta\\)}\in\mathbf P \Longrightarrow q\_{\min}\in\mathbf P. } \\]

If \\(q\_{\min}\\) were also NP-hard under polynomial-time reductions, this would imply

\\[ \mathbf P=\mathbf{NP}. \\]

Thus, polynomial solvability would rule out NP-hardness under the standard assumption \\(\mathbf P\ne\mathbf{NP}\\), not as an unconditional mathematical fact.

On the other hand,

\\[ \boxed{ \text{DEC-\\(\Theta\\) is }\exists\mathbb R\text{-hard} \Longrightarrow \text{DEC-\\(\Theta\\) is NP-hard}, } \\]

under the standard polynomial-time many-one reductions, because

\\[ \mathbf{NP}\subseteq\exists\mathbb R. \\]

This is the right relationship to use in the paper.

## 2.3 A further distinction: the arithmetic model

The current discussion moves between

\\[ A,C\in\mathbb C^{\cdot\times\cdot} \\]

and real semialgebraic charts.

That needs to be made precise before making a complexity classification.

For a standard \\(\exists\mathbb R\\) formulation, the natural input model is rational matrices encoded in binary, with real variables describing the unknown augmentation.

One must then specify:

- Whether the input matrices are rational or algebraic.
- Whether the unknown augmentation is real or complex.
- Whether complex variables are represented by pairs of real variables.
- Whether the problem is feasibility over \\(\mathbb R\\) or over \\(\mathbb C\\).
- How strict inequalities and nonvanishing conditions are encoded.
- Whether the dimensions and the target order are part of the input.

This is not merely a technicality. A complexity result over rational real inputs is not automatically the same result as one over arbitrary complex inputs.

For the remainder of this assessment, I will interpret DEC-\\(\Theta\\) as a rational-input real-algebraic decision problem, with complex rank conditions represented by their real and imaginary parts where necessary.

# 3. Question 1 — Where does DEC-\\(\Theta\\) sit in the existing complexity literature?

## 3.1 Static output feedback is relevant, but not a ready-made reduction

The closest control-theoretic comparison is static output-feedback design.

A typical static output-feedback problem asks whether there exists a matrix \\(K\\) such that

\\[ A+BKC \\]

satisfies a prescribed spectral property, for example Hurwitz stability.

There is a genuine structural similarity:

| Static output feedback              | Present problem                                   |
| ----------------------------------- | ------------------------------------------------- |
| Unknown feedback matrix \\(K\\)     | Unknown augmentation \\(R\\)                      |
| Affine dependence on \\(K\\)        | Structured dependence on \\(R\\)                  |
| Spectral constraint                 | Constant-rank pencil constraint                   |
| Existence of a stabilizing feedback | Existence of a spectrally admissible augmentation |
| Nonlinear algebraic feasibility     | Nonlinear algebraic feasibility                   |

However, the two problems are not equivalent.

The static output-feedback problem generally allows the feedback matrix to vary in a prescribed affine family. Here the unknown augmentation must simultaneously satisfy:

\\[ (5a)\qquad \pi(\mathcal VA)\subseteq\pi(\mathcal V) \\]

and

\\[ (5b)\qquad \operatorname{rank}Q\_{\mathcal V}(\lambda)=\rho \quad\forall\lambda\in\mathbb C. \\]

The first condition restricts the admissible family before the spectral condition is considered.

Consequently, an NP-hardness result for static output feedback does not automatically transfer to DEC-\\(\Theta\\).

There is, nevertheless, a particularly interesting recent result worth incorporating into the literature discussion.

The September 2026 preprint by Johan Löfberg, Static output-feedback stabilization is NP-hard, proves NP-hardness of unrestricted static output-feedback stabilization by a reduction from Betweenness. The construction already works in a single-input, multiple-output setting. It also establishes NP-hardness for deciding whether an affinely parameterized rational polynomial family contains a Hurwitz member on a rational box.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



This is relevant for two reasons.

First, it provides a relatively recent and explicit hardness construction involving spectral constraints and continuously varying parameters.

Second, it suggests a potentially useful intermediate problem:

\\[ \exists \theta\in\mathbb R^m: \quad p\_\theta(\lambda) \text{ has a prescribed spectral property}. \\]

But there is an important difference between Hurwitz stability and the present condition.

Hurwitz stability requires every root to lie in the open left half-plane. Your condition requires the absence of finite rank-drop points over the entire complex plane.

For a regular square pencil, the latter is particularly restrictive: every nonconstant characteristic determinant has a complex root. Thus, the condition is fundamentally a nonsingularity/regular-subpencil avoidance condition, not a stability-region condition.

My recommendation: use the static-output-feedback literature as motivation and as a possible source of reductions, but do not claim that the existing NP-hardness theorem proves anything about \\(q\_{\min}\\).

## 3.2 Regular subpencils and matrix-pencil completion

A second relevant literature is the theory of matrix-pencil completion and prescribed Kronecker structure.

For example, Dodig's work on matrix-pencil completion gives necessary and sufficient conditions for the existence of pencils with prescribed Kronecker invariants and regular subpencils.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

ScienceDirect



Roca and Silva study pencils with prescribed constant subpencils and characterize when a pencil is strictly equivalent to one containing a given constant subpencil.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

ScienceDirect



These works are conceptually close to B.6, B.8, B.22, and B.23.

But there is a critical distinction:

- Classical pencil completion asks whether a pencil with specified structural invariants or subblocks exists.
- Your problem asks whether a pencil can be obtained from a particular augmentation family constrained by a fixed pair \\((A,C)\\), a fixed \\(L_0\\), and the invariant-subspace condition (5a).

The second problem is a constrained realization problem.

The fact that an arbitrary pencil with the desired Kronecker structure exists does not imply that it can be realized through your particular \\(\mathcal L\\).

This is precisely why the unconstrained matrix-pencil literature cannot by itself settle the complexity question.

## 3.3 Is there an established \\(\exists\mathbb R\\)-hardness result that applies?

I would not currently classify DEC-\\(\Theta\\) as a known \\(\exists\mathbb R\\)-hard problem.

The natural ambient complexity class is \\(\exists\mathbb R\\), and the general theory is well developed. The 2024 compendium by Schaefer, Cardinal, and Miltzow, subsequently published as a 2026 book chapter, is a useful reference for identifying appropriate source problems and understanding what makes a continuous feasibility problem a plausible candidate for \\(\exists\mathbb R\\)-hardness.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

Springer Nature Link+1



However, a problem's expressibility using polynomial equations and inequalities is only an upper-bound argument.

To establish \\(\exists\mathbb R\\)-hardness, one must encode arbitrary instances of a suitable \\(\exists\mathbb R\\)-complete problem into the constrained augmentation problem.

In particular, one needs to preserve:

1. The fixed input matrices \\(A,C,L_0\\).
2. The invariant-subspace condition (5a).
3. The prescribed augmentation structure.
4. The spectral avoidance condition (5b).
5. Polynomial growth of dimensions and coefficient bit lengths.

The fourth requirement is especially important. A reduction that encodes arbitrary polynomial equations into the entries of a matrix is not sufficient unless the resulting matrix family is actually realizable as the pencil generated by the permitted augmentations.

### My classification recommendation

At present, I would describe the problem as follows:

DEC-\\(\Theta\\): a structured real-algebraic spectral-avoidance problem

Upper bound

In \\(\exists\mathbb R\\), subject to encoding assumptions

NP-hardness

Open

\\(\exists\mathbb R\\)-hardness

Open

Polynomial algorithm

Open

This is a more defensible classification than associating the problem directly with static output-feedback NP-hardness.

# 4. Question 2 — Approach A: which hard problem should be used, and which interface is better?

My recommendation is to investigate two source problems, but to prioritize a different use of B.13 than the one suggested in the current note.

## 4.1 The first candidate: existential real feasibility

The canonical source problem is the existential theory of the reals:

\\[ \exists x_1,\ldots,x_m\in\mathbb R: \quad f_1(x)=\cdots=f_s(x)=0, \\]

possibly with additional inequalities.

A reduction should construct matrices \\(A,C,L_0\\) such that

\\[ \exists x\text{ satisfying the source system} \\]

if and only if

\\[ \exists R: \quad (5a),(5b)\text{ hold}. \\]

The key challenge is not representing polynomial equations by matrix entries. That can often be done through multiplication blocks, companion constructions, and determinantal identities.

The challenge is making the equivalence exact.

In particular, the construction must prevent unintended augmentations \\(R\\) from satisfying (5a) and (5b) even when the original polynomial system is infeasible.

This is the central obstacle in most naive reductions.

I would therefore not start with a general matrix-pencil realization theorem. I would start with a source problem whose variables and constraints naturally correspond to the eigenvector equations appearing in B.24.

## 4.2 A more natural source: polynomial eigenvalue incidence

Consider the condition

\\[ \Phi(w)=\lambda w, \qquad 0\ne w\in W. \\]

This is already a system of polynomial equations involving:

- the coordinates of \\(w\\);
- the scalar \\(\lambda\\);
- the parameters determining \\(\Phi\\);
- the parameters determining the admissible subspace \\(W\\).

The difficulty is that \\(\Phi\\) is a partial map:

\\[ \Phi:W\longrightarrow\mathbb C^q, \\]

not an endomorphism of \\(W\\).

This distinction is useful rather than inconvenient.

It means that the eigenvector condition is equivalent to the vanishing of a collection of bilinear expressions:

\\[ \Phi(w)\wedge w=0. \\]

In coordinates, this becomes

\\[ \Phi_i(w)w_j-\Phi_j(w)w_i=0, \qquad 1\le i\<j\le q. \\]

Thus, the obstruction set is a projective algebraic variety:

\\[ \mathcal E\_\Phi = \left\\{ [w]\in\mathbb P(W): \Phi(w)\wedge w=0 \right\\}. \\]

Your feasibility condition becomes

\\[ \boxed{ \mathcal E\_\Phi=\varnothing. } \\]

This is an attractive reduction interface because the target condition is already expressed as a projective incidence problem.

A promising strategy would be to encode a known hard projective incidence problem into the family of partial maps \\(\Phi\\) generated by the admissible augmentations.

The issue is whether the family is sufficiently expressive.

That is the realization problem that must be solved.

## 4.3 Comparing F.1 and B.13c

The two available interfaces have quite different characteristics.

| Feature             | F.1 rank barrier                       | B.13c coverage                     |
| ------------------- | -------------------------------------- | ---------------------------------- |
| Type                | Necessary infeasibility condition      | Sufficient infeasibility condition |
| Mechanism           | Dimension obstruction                  | Projective incidence               |
| Main object         | Quotient rank                          | Incidence variety                  |
| Reduction potential | Good for dimension-gated constructions | Good for geometric encoding        |
| Main limitation     | Does not characterize feasibility      | Base locus must be empty           |

### F.1: the rank barrier

The result says

\\[ (5b)\Longrightarrow \rho\le r(\lambda_0) \\]

for every \\(\lambda_0\\).

Hence,

\\[ \rho>\min\_\lambda r(\lambda) \\]

implies infeasibility.

This is useful for excluding layers.

However, there is a fundamental limitation: F.1 is only a necessary condition.

Suppose a source problem is encoded into the inequality

\\[ \rho>\min\_\lambda r(\lambda). \\]

Then the reduction can establish infeasibility in the corresponding cases, but the converse is not automatic.

When the inequality does not hold, the instance may still be infeasible for entirely different spectral reasons.

For a valid many-one reduction, this false-positive possibility must be eliminated.

My assessment: F.1 is best suited to controlling the order spectrum and creating structural gadgets. It is not yet a strong standalone hardness interface.

### B.13c: the coverage criterion

This is geometrically more promising.

You construct

\\[ \mathfrak I = \left\\{ ([x],[z],[\alpha:\beta]): z\wedge(\alpha x-\beta Ax)=0 \right\\} \\]

and project onto \\(\mathbb P(K)\\).

If

\\[ \dim\mathfrak I\<k-1, \\]

the projection cannot cover \\(\mathbb P(K)\\). Therefore some \\([z]\\) avoids all incidence conditions.

This is exactly the kind of mechanism that can turn an algebraic-geometric existence question into a dimension problem.

However, your B.13c hypothesis

\\[ \mathcal B=\varnothing \\]

is restrictive.

The reason is particularly important:

If there exists even one base point

\\[ ([x],[\alpha:\beta])\in\mathcal B, \\]

then

\\[ \alpha x-\beta Ax=0. \\]

Consequently,

\\[ z\wedge(\alpha x-\beta Ax)=0 \\]

for every \\(z\in K\\).

Thus the projection of the incidence variety covers all of \\(\mathbb P(K)\\).

In other words, a single base point destroys the avoidance property.

This is not a weakness in your proof. It is an intrinsic feature of the chosen incidence relation.

### A necessary refinement

I would not attempt to weaken the condition \\(\mathcal B=\varnothing\\) while retaining exactly the same incidence variety and the same universal avoidance conclusion.

That cannot work: any nonempty base locus immediately produces full coverage.

Instead, I suggest changing the incidence relation.

For example, introduce an auxiliary projective condition that distinguishes the part of \\(K\\) relevant to the augmentation from the entire space \\(K\\).

The current construction treats every \\(z\in K\\) as an equally valid candidate. But in the original problem, the admissible augmentation may only generate a restricted subset

\\[ \mathcal Z\_{\mathrm{adm}}\subseteq\mathbb P(K). \\]

Then the relevant question becomes whether

\\[ \operatorname{pr}\_K(\mathfrak I) \\]

covers \\(\mathcal Z\_{\mathrm{adm}}\\), rather than whether it covers all of \\(\mathbb P(K)\\).

This suggests the following replacement:

\\[ \boxed{ \operatorname{pr}\_K(\mathfrak I) \cap\mathcal Z\_{\mathrm{adm}} \ne\mathcal Z\_{\mathrm{adm}}. } \\]

A dimension estimate for the intersection with the admissible parameter locus may succeed even when the unrestricted base locus is nonempty.

There is one important qualification: this is a proposed direction, not yet a theorem. The admissible locus must itself be defined algebraically and its dimension and irreducible components must be controlled.

## 4.4 A more concrete reduction architecture

I would organize Approach A into four stages.

## Proposed hardness-reduction architecture

Source problem

\\(\exists x:f_i(x)=0,\ g_j(x)\ge0\\)

Algebraic encoding

Construct a family of partial maps \\(\Phi\_\theta\\)

Incidence encoding

\\(\Phi\_\theta(w)\wedge w=0\\)

Realizability theorem

The constructed \\(\Phi\_\theta\\) arises from an admissible augmentation satisfying (5a).

Target equivalence

Source feasibility iff DEC-\\(\Theta\\) feasibility

The fourth stage is the decisive one.

Without it, the construction proves hardness for an abstract partial-eigenvector problem, not for your original problem.

Recommendation for Approach A: use the partial-eigenvector incidence formulation as the primary interface, and use F.1 to enforce order and dimension restrictions. Retain B.13c as a geometric auxiliary theorem, but do not make its current base-locus-free condition the central reduction mechanism.

# 5. Question 3 — Approach B: can the partial eigenvector condition be tested in polynomial time?

This is, in my opinion, the most important mathematical question in the present project.

The answer requires separating two problems:

1. Testing the partial eigenvector condition for a fixed \\(\Phi\\).
2. Deciding whether there exists an admissible augmentation producing a \\(\Phi\\) for which the condition is avoided.

The first problem has a polynomial-time algebraic solution. The second is still open.

This distinction gives a much more precise understanding of where the actual computational difficulty lies.

## 5.1 The fixed partial-map problem

Let

\\[ V\subseteq\mathbb C^q,\qquad \dim V=\rho, \\]

and let

\\[ \Phi:V\longrightarrow\mathbb C^q \\]

be linear.

Let

\\[ \iota:V\hookrightarrow\mathbb C^q \\]

denote the inclusion.

The obstruction is

\\[ \exists\\,0\ne w\in V,\quad \exists\lambda\in\mathbb C: \quad \Phi(w)=\lambda\iota(w). \\]

Equivalently,

\\[ \exists\lambda\in\mathbb C: \quad \ker(\Phi-\lambda\iota)\ne\\{0\\}. \\]

Therefore,

\\[ \boxed{ (5b)\iff \operatorname{rank}(\lambda\iota-\Phi)=\rho \quad\forall\lambda\in\mathbb C. } \\]

This is a rectangular pencil:

\\[ P(\lambda)=\lambda\iota-\Phi \in\mathbb C^{q\times\rho}. \\]

The crucial point is that the pencil has only one scalar parameter.

That makes the fixed-candidate problem substantially easier than general multivariate polynomial feasibility.

## 5.2 An exact polynomial-time test using maximal minors

Choose bases of \\(V\\) and \\(\mathbb C^q\\). Write

\\[ P(\lambda)=\lambda E-F, \\]

where

\\[ E\in\mathbb C^{q\times\rho}, \qquad F\in\mathbb C^{q\times\rho}, \qquad \operatorname{rank}E=\rho. \\]

Let \\(p_I(\lambda)\\) denote the \\(\rho\times\rho\\) minor corresponding to a row subset

\\[ I\subseteq\\{1,\ldots,q\\}, \qquad |I|=\rho. \\]

Then

\\[ \operatorname{rank}P(\lambda)=\rho \\]

if and only if at least one \\(p_I(\lambda)\ne0\\).

Consequently,

\\[ \exists\lambda: \operatorname{rank}P(\lambda)<\rho \\]

if and only if all maximal minors vanish simultaneously at some \\(\lambda\\).

By the gcd criterion,

\\[ \boxed{ \text{No partial eigenvector exists} \iff \gcd_I p_I(\lambda)\in\mathbb C^\times. } \\]

This is precisely the one-variable polynomial principle already developed in B.8.

The computation consists of:

1. Constructing the maximal minors.
2. Computing their polynomial gcd.
3. Checking whether that gcd has positive degree.

Thus, the fixed partial-map problem does not require enumeration of eigenvectors or numerical searches over \\(\lambda\\).

It is an exact algebraic test.

For rational input coefficients, polynomial gcd computations can be performed using standard exact polynomial arithmetic. A formal bit-complexity claim should still account for coefficient growth and the representation of the minors.

## 5.3 Why the minimal polynomial proposal needs correction

The current note suggests deciding the condition through the minimal polynomial of \\(\Phi\\) restricted to \\(W\\).

There is a subtle problem.

You explicitly establish in B.24 that

\\[ \Phi:W\longrightarrow\mathbb C^q \\]

does not necessarily map \\(W\\) into itself.

Therefore, in general,

\\[ \Phi|\_W \\]

is not an endomorphism of \\(W\\).

The ordinary minimal polynomial is not defined for this partial map.

One could introduce a projection

\\[ P_W:\mathbb C^q\longrightarrow W \\]

and consider

\\[ P_W\Phi:W\longrightarrow W. \\]

But this does not solve the original problem.

Indeed,

\\[ P_W\Phi(w)=\lambda w \\]

only implies that the component of \\(\Phi(w)\\) inside \\(W\\) equals \\(\lambda w\\). It does not imply that the component outside \\(W\\) vanishes.

The actual condition requires

\\[ \Phi(w)-\lambda w=0 \\]

in the entire ambient space.

Therefore, the minimal polynomial of a projected operator can introduce spurious eigenvectors.

I would remove the minimal-polynomial suggestion from the main theorem unless an additional invariance hypothesis is established.

## 5.4 The more appropriate intrinsic object: a rectangular pencil

The natural object is

\\[ P\_\Phi(\lambda)=\lambda\iota-\Phi. \\]

Its Kronecker structure contains the relevant information.

For the fixed partial map, the condition is exactly the absence of finite eigenvalues of this pencil in the column-rank-loss sense.

This is closely related to the finite elementary divisors and maximal-minor gcd in B.8.

There is a useful conceptual reformulation:

\\[ \boxed{ \mathcal E\_\Phi=\varnothing \iff P\_\Phi(\lambda) \text{ has full column rank for every finite }\lambda. } \\]

This gives an intrinsic description without referring to any extension of \\(\Phi\\).

It also suggests a computational route based on the polynomial matrix rather than an ordinary matrix operator.

## 5.5 Why this does not yet solve DEC-\\(\Theta\\)

Now comes the central difficulty.

In the original problem, \\(\Phi\\) is not fixed.

It depends on the unknown augmentation:

\\[ \Phi=\Phi_R. \\]

Furthermore, the admissible \\(R\\)'s must satisfy (5a).

Thus the actual decision problem is

\\[ \exists R: \quad (5a) \quad\land\quad \gcd_I p\_{I,R}(\lambda)\in\mathbb C^\times. \\]

The individual gcd computation is easy.

The difficulty is finding \\(R\\) such that the gcd becomes constant.

This is a parametric polynomial problem.

For example, suppose

\\[ p\_{I,R}(\lambda) = a\_{I,0}(R)+a\_{I,1}(R)\lambda+\cdots+ a\_{I,\rho}(R)\lambda^\rho. \\]

The condition that all these polynomials have no common complex root is equivalent to their gcd being constant.

Using Bézout's identity, this can be expressed through polynomial multipliers:

\\[ \sum_I u_I(\lambda)p\_{I,R}(\lambda)=1. \\]

With appropriate degree bounds, this becomes a finite algebraic system in:

- the entries of \\(R\\);
- the coefficients of the multipliers \\(u_I\\);
- any auxiliary variables used to impose (5a).

This is a natural route to an \\(\exists\mathbb R\\) upper bound.

But it does not establish polynomial-time solvability.

The degrees and number of multipliers, the number of minors, and the dependence of their coefficients on \\(R\\) all matter.

More importantly, one must exploit additional structure beyond generic polynomial feasibility to obtain a polynomial algorithm.

## 5.6 A potentially important improvement: avoid enumerating maximal minors

The gcd criterion is mathematically elegant, but directly generating all

\\[ \binom q\rho \\]

maximal minors can be expensive.

A more promising implementation is to use polynomial-matrix algorithms that compute the determinantal divisor or an appropriate normal-rank certificate without explicitly enumerating every maximal minor.

The relevant algebraic object is the top determinantal divisor of

\\[ \lambda\iota-\Phi. \\]

For a fixed candidate, one should investigate whether the special form of the leading coefficient \\(\iota\\), which has full column rank, allows a more efficient computation than a generic maximal-minor construction.

This would improve the fixed-candidate verification algorithm, although it would not by itself resolve the family-existence problem.

## 5.7 My conclusion on Approach B

There are two possible outcomes.

Outcome 1: an intrinsic polynomial criterion for the family.

If one can derive a finite collection of linear-algebraic conditions on the admissible augmentation that is equivalent to

\\[ \mathcal E\_{\Phi_R}=\varnothing, \\]

then a polynomial algorithm may follow.

Outcome 2: the family-existence problem remains genuinely algebraic.

Even if every fixed candidate is efficiently testable, selecting a candidate may encode a hard real-algebraic feasibility problem.

This is not unusual in optimization: efficiently checking a proposed solution does not imply that finding a solution is easy.

My recommendation is therefore:

> Do not make the immediate objective finding a polynomial-time algorithm. First prove a parameterized structural theorem describing how the determinantal divisor changes over the admissible family.

That is a mathematically meaningful intermediate result regardless of the eventual complexity classification.

# 6. Question 4 — Do B.17 and B.23–B.24 form a unified description?

My answer is yes, with one qualification: they should be combined into a theorem with clearly separated structural, spectral, and computational conclusions.

The results are complementary.

## 6.1 What B.17 contributes

B.17 works with

\\[ \overline N\_{\mathcal Z}(\lambda): V/S\longrightarrow X/\mathcal Z. \\]

Its most important conclusions are:

- A permanent kernel component determined by \\(S\\).
- An exact failure criterion.
- A description of the right null space.
- A stratification according to the rank of the restricted map.

The main mathematical insight is that the right null space is not arbitrary.

It is controlled by the fixed subspace \\(S\\).

In particular,

\\[ \ker Q\_{\mathcal V}(\lambda) \\]

has a structural component that is independent of \\(\lambda\\).

This is valuable because it separates the unavoidable kernel from the genuinely spectral kernel.

The distinction is essential in singular-pencil problems.

## 6.2 What B.23 contributes

B.23 gives the factorization

\\[ Q\_{\mathcal L}(\lambda)=P(\lambda)H_0, \\]

with

\\[ P(\lambda)= \begin{pmatrix} \lambda I_q-K_1&-K_2\\\ 0&I\_{r_1} \end{pmatrix}. \\]

The important point is that the pencil has been reduced to a block-triangular form.

The spectral dependence is concentrated in

\\[ \lambda I_q-K_1. \\]

This is an enormous simplification.

Instead of dealing with the entire original matrix pencil, one can study the interaction between a fixed finite-dimensional map and the image of the augmentation.

However, the block factorization alone is not yet the full conceptual explanation.

It is the bridge to the partial eigenvector condition.

## 6.3 What B.24 contributes

B.24 identifies the obstruction as

\\[ \exists\\,0\ne w\in W: \quad \Phi(w)\in\mathbb Cw. \\]

This is the most informative interpretation of the finite rank-drop condition.

It tells us exactly what must happen for the pencil to fail.

The obstruction is not simply that a certain square matrix has an eigenvalue.

It is that the image of a nonzero vector under a partially defined map becomes collinear with the original vector.

That distinction matters because

\\[ \Phi(W)\not\subseteq W \\]

in general.

## 6.4 The unified theorem I would recommend

I suggest organizing the unified result around the following statement.

Unified structural-spectral theorem (proposed formulation).

Let \\(\mathcal L\\) satisfy (5a), and let the associated spaces \\(V,S,W\\) and maps be defined as in the project.

Then:

1\. The quotient-pencil representation reduces the rank condition to a pencil acting on the effective quotient \\(V/S\\).

2\. The kernel of the quotient map contains a permanent component determined by \\(S\\).

3\. After removing that permanent component, failure of (5b) is equivalent to the existence of a nonzero partial eigenvector.

4\. The partial eigenvector condition is equivalent to the existence of a finite parameter \\(\lambda\\) for which the rectangular pencil

\\[ \lambda\iota-\Phi \\]

&#x20;  loses full column rank.

5\. For a fixed augmentation, this is equivalent to the nonconstant gcd of its maximal minors.

The logical architecture is therefore

Layer 1 — Quotient structure

B.17: remove the permanent kernel \\(S\\).

Layer 2 — Block structure

B.23: isolate the spectral block.

Layer 3 — Geometric obstruction

B.24: identify partial eigenvectors.

Layer 4 — Algebraic decision criterion

B.8: use the determinantal divisor.

This is a coherent and useful mathematical narrative.

## 6.5 One additional result that I would try to prove

There is a potentially important missing bridge between the structural and computational formulations.

Let

\\[ P_R(\lambda)=\lambda\iota_R-\Phi_R. \\]

Define its top determinantal divisor by

\\[ \Delta_R(\lambda) = \gcd\\{\text{maximal minors of }P_R(\lambda)\\}. \\]

Then

\\[ (5b)\iff\Delta_R(\lambda)\in\mathbb C^\times. \\]

The natural next question is:

Can the determinantal divisor be characterized directly in terms of the Kronecker invariants of the quotient pencil in B.17?

This would connect:

- the permanent kernel;
- the right minimal indices;
- the finite elementary divisors;
- the partial eigenvector variety;
- the maximal-minor gcd.

Your B.6 already provides an important part of this connection.

Under (5a), the right minimal indices are zero and the infinite elementary divisors have degree one.

Consequently, the finite elementary divisors contain precisely the remaining spectral obstruction.

This is consistent with the earlier project result:

\\[ (5b) \iff d\_{\mathrm{fin}}=0 \iff \sum_j\varepsilon_j = \operatorname{rank}\mathcal L. \\]

The latter is a particularly useful fixed-candidate criterion.

I would include this connection in the unified theorem, provided the equality between the relevant quotient-pencil invariants and the original pencil invariants is proved carefully.

It would make the theorem substantially more complete.

# 7. Question 5 — Which results deserve to be claimed as new?

This question requires particular care because the two September 2026 papers already establish a substantial characterization of the functional-observer order problem.

The relevant references are:

- Tyrone Fernando, A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions, arXiv:2609.33615.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://papers.cool\&sz=32)

  Cool Papers - Immersive Paper Discovery

- Tyrone Fernando, Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger, arXiv:2609.37992.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://papers.cool\&sz=32)

  Cool Papers - Immersive Paper Discovery



Based on the descriptions available, the papers establish:

1. The algebraically admissible minimum order.
2. Functional observability indices.
3. The order spectrum.
4. Necessary and sufficient conditions at each prescribed order.
5. An existence criterion involving an auxiliary subspace \\(Z\\).
6. A chart representation \\(Z_I(\Theta)\\).
7. An explicit construction of admissible observers.

This is already a substantial theory.

The new paper should therefore not claim to have established the general order-by-order characterization from scratch.

Instead, I would organize the contributions according to how much additional mathematical information they provide beyond the existing characterization.

## 7.1 Classification of the current results

The following classification is my assessment based on the uploaded report and the descriptions of the two papers. It is not a substitute for a line-by-line comparison with their full proofs.

| Result                                     | Assessment                                                              | Recommended treatment                          |
| ------------------------------------------ | ----------------------------------------------------------------------- | ---------------------------------------------- |
| A.1: \\(q=\rho+c\\)                        | Structural decomposition                                                | State as a useful preliminary identity         |
| A.1: lower bounds                          | Potentially additional                                                  | State with precise hypotheses and proof        |
| B.1: quotient pencil                       | Likely reformulation of the existing spectral criterion                 | Use as the starting reduction                  |
| B.2: PBH criterion                         | Standard control-theoretic result in the top layer                      | Present as a corollary                         |
| B.3: \\(\rho=0\\)                          | Elementary special case                                                 | Corollary                                      |
| B.4: right-eigenvector criterion           | Potentially new and important                                           | Develop as a main theorem                      |
| F.1: rank barrier                          | Potentially new necessary condition                                     | Main structural theorem                        |
| B.9: equality boundary                     | Potentially new refinement                                              | Include with proof                             |
| B.22: equality obstruction                 | Important additional spectral obstruction                               | Main theorem                                   |
| B.6: minimal indices and infinite divisors | Potentially new pencil-structure result                                 | Main theorem                                   |
| B.8: gcd criterion                         | Standard polynomial-matrix principle                                    | State as a tool or preliminary lemma           |
| B.31–B.32                                  | Additional feasibility obstruction and terminal-order result            | Main theorem, after checking assumptions       |
| B.17: unified quotient-kernel theorem      | Potentially substantial new refinement                                  | Main theorem                                   |
| B.23–B.24                                  | Intrinsic partial-eigenvector characterization                          | Main theorem                                   |
| B.13a–c                                    | Standard incidence/dimension method with a problem-specific application | State the application and its precise scope    |
| D.1: polynomial-time \\(P\\) problem       | Potentially independent algorithmic contribution                        | Separate algorithmic theorem                   |
| G.1: \\(\exists\mathbb R\\) upper bound    | Potentially independent complexity contribution                         | Separate complexity theorem                    |
| H.1: Theorem Q                             | Potentially a useful reformulation                                      | Compare against the existing \\(Z\\)-criterion |
| C.1                                        | Special-family result                                                   | Supplementary proposition                      |

The most promising new results are B.17, B.22, B.24, F.1, B.31, and G.1.

However, each needs a careful novelty check.

## 7.2 The most important distinction: characterization versus intrinsic spectral structure

Suppose the existing paper proves

\\[ \exists Z:\quad \mathcal C(Z) \\]

if and only if a prescribed order is feasible.

Suppose your work proves

\\[ (5b) \iff \mathcal E\_\Phi=\varnothing. \\]

These are not automatically the same contribution.

The first is an existence characterization.

The second is a structural characterization of the spectral obstruction.

Even if both are logically equivalent when combined with the algebraic constraints, the second may reveal information not explicit in the first.

In particular, B.24 identifies a concrete geometric obstruction: the existence of a partial eigenvector.

That is more informative than merely knowing that a certain auxiliary subspace exists.

Likewise, B.6 describes the Kronecker structure of the pencil, while B.17 identifies its permanent kernel component.

These results can legitimately constitute additional contributions even if they are derived from an already-known order characterization.

The paper should explain exactly what new information they provide.

## 7.3 My recommended paper architecture

I would not make the complexity question the only contribution.

A paper containing several proved structural theorems and an open complexity problem can be mathematically valuable.

I would organize it as follows.

### Part I. Algebraic admissibility and quotient reduction

Recall the existing order characterization and establish the quotient notation.

Clearly distinguish previously known results from new reductions.

### Part II. Spectral structure of the quotient pencil

Present B.17, B.6, B.22, and the relation to the finite elementary divisors.

This should be the main structural part of the paper.

### Part III. Intrinsic partial-eigenvector characterization

Present B.23 and B.24.

Explain why the obstruction is a partial eigenvector rather than an ordinary eigenvector.

Connect this theorem to the maximal-minor gcd criterion.

### Part IV. Additional infeasibility criteria

Present F.1, B.9, B.31, B.32, and the incidence-variety results.

These results give explicit ways to exclude entire layers or ranges of orders.

### Part V. Computational complexity

Present the chart-free \\(\exists\mathbb R\\) encoding.

Then state explicitly that the classification between polynomial-time solvability and hardness remains unresolved.

This organization has a natural progression:

\\[ \text{known existence characterization} \longrightarrow \text{new pencil structure} \longrightarrow \text{intrinsic spectral obstruction} \longrightarrow \text{infeasibility criteria} \longrightarrow \text{complexity}. \\]

It also avoids presenting the new results as competing with the existing papers.

# 8. Additional mathematical audit: points I would resolve before submission

The uploaded report is well organized, and the verification status is unusually useful. Nevertheless, I would resolve the following issues before treating it as a definitive research-status document.

These are not all objections to the results. Some are questions of formulation and theorem scope.

## 8.1 Coefficient-field consistency in B.8

The report states

\\[ \Delta_h(\lambda)\in\mathbb Q^\times. \\]

But the original problem allows

\\[ A,C\in\mathbb C^{\cdot\times\cdot}. \\]

For arbitrary complex input coefficients, the appropriate conclusion is

\\[ \Delta_h(\lambda)\in\mathbb C^\times. \\]

The rational-field statement is correct when the input polynomial matrix has rational coefficients.

I recommend stating the theorem over an arbitrary field \\(F\\), with the algebraic-closure assumption used explicitly when asserting that every nonconstant polynomial has a root.

For the original problem over \\(\mathbb C\\), use \\(\mathbb C[\lambda]\\).

## 8.2 The distinction between B.22 and B.24 must remain explicit

B.22 uses the equality case

\\[ h=q+r_1. \\]

Under this hypothesis, the stacked matrix \\(H_0\\) has full row rank, and the block factorization gives a direct determinant argument.

B.24 is more general.

It does not require the same full-row-rank argument. It uses the partial map and the intersection of the image with the relevant eigendirections.

Do not accidentally use

\\[ \det(\lambda I_q-K_1) \\]

as a universal criterion for failure of (5b).

The determinant argument is directly justified in the full-row-rank equality situation. In the general situation, the correct criterion is the partial-eigenvector condition.

This distinction is important and should be emphasized in the proof of the unified theorem.

## 8.3 Make the permanent-kernel statement in B.17 completely precise

The phrase

> the \\(\lambda\\)-independent part of the kernel equals \\(S\\)

is conceptually understandable but mathematically ambiguous.

I would replace it with an exact statement.

For example, if the intended meaning is the common kernel, write

\\[ \bigcap\_{\lambda\in\mathbb C} \ker\overline N\_{\mathcal Z}(\lambda)=S. \\]

If the intended meaning is a polynomial null-module statement, formulate that separately:

\\[ \ker\_{\mathbb C[\lambda]} \overline N\_{\mathcal Z}(\lambda) = S\otimes\_{\mathbb C}\mathbb C[\lambda]. \\]

These are different assertions and should not be conflated.

The exact formulation will make B.17 much easier to verify and cite.

## 8.4 Check the terminal-order notation in B.32

The report uses the upper endpoint

\\[ n_0-p \\]

in Part I, but B.32 states

\\[ q\_{\min}=n-p. \\]

These expressions coincide if \\(n_0=n\\), for example under an appropriate complete-observability assumption.

If B.32 is intended to hold without that assumption, the difference needs to be resolved.

I would specifically verify:

- The definition of \\(n_0\\).
- Whether \\(n_0=n\\) follows from \\(r_1\le p+1\\).
- Whether terminal-order feasibility is established at \\(n-p\\) or \\(n_0-p\\).
- Whether the theorem assumes complete observability or only functional observability.

This is a potentially substantive issue, not merely a typographical one.

## 8.5 Clarify the exact meaning of the complexity upper bound

G.1 is potentially important, but its statement should specify:

\\[ \text{Input encoding} + \text{number of variables} + \text{number of equations} + \text{maximum degree} + \text{coefficient bit size}. \\]

In particular, a bound of \\(O(n^3)\\) variables and degree at most \\(n\\) is not by itself a complete polynomial-time reduction proof.

You also need polynomial bounds on coefficient encoding and a proof that all existential constraints are equivalent to the original feasibility condition.

The report's mention of the kernel identity

\\[ \ker(CAZ)=Z\cap\mathcal V \\]

and the left-inverse implication is encouraging, but the complete encoding needs to be audited.

## 8.6 Separate formal verification from mathematical novelty

The Lean verification status is a substantial strength of the project.

However, the paper should distinguish:

- A theorem whose complete statement is formalized.
- A theorem whose central algebraic lemma is formalized.
- A theorem whose proof is complete on paper but not formalized.
- A computational conjecture supported by experiments.

I particularly appreciate that the report already distinguishes the 8 literal formalizations from the 14 formalizations of nontrivial cores.

Continue using this distinction.

It prevents formal verification from being overstated while still making its contribution visible.

# 9. Recommended research programme

I would not pursue Approaches A and B with equal priority at this stage.

The results already obtained suggest a more efficient research strategy.

## 9.1 Priority ranking

Priority 1 — Complete the unified theorem

Highest

Prove the exact equivalence between B.17, B.23–B.24, and the finite elementary-divisor criterion.

Deliverable: A single theorem identifying the permanent kernel, the partial-eigenvector obstruction, and the fixed-candidate algebraic test.

Priority 2 — Develop the parameterized pencil

Highest

Study the family

\\[ P_R(\lambda)=\lambda\iota_R-\Phi_R. \\]

Determine how its determinantal divisor changes over the admissible augmentation family.

Deliverable: A structural theorem for the parameterized spectral obstruction.

Priority 3 — Strengthen the incidence method

High

Replace unrestricted coverage of \\(\mathbb P(K)\\) with coverage relative to the admissible augmentation locus.

Deliverable: A more flexible geometric infeasibility criterion.

Priority 4 — Investigate hardness

High

Attempt to realize polynomial incidence systems through the partial maps generated by the augmentation constraints.

Deliverable: Either a valid reduction or a realization theorem identifying restrictions that obstruct such reductions.

Priority 5 — Investigate polynomial solvability

Longer-term

Investigate whether the admissible family has special structure allowing the spectral condition to be decided without general real-algebraic feasibility.

Deliverable: A polynomial algorithm or a precise obstruction to the proposed algorithmic approach.

## 9.2 Five concrete mathematical tasks

I would turn the programme into the following five questions.

Task 1. Prove the determinantal-divisor equivalence at the quotient level.

Starting with B.17, construct the rectangular pencil

\\[ P(\lambda)=\lambda\iota-\Phi. \\]

Prove that its maximal-minor gcd is exactly the relevant finite spectral obstruction.

This should establish a direct relationship between the quotient construction and B.8.

Task 2. Investigate whether the admissible family has a simpler parametrization.

The chart representation \\(Z_I(\Theta)\\) may be useful for proving existence, but it may obscure the geometry of the family.

Try to identify an intrinsic parameter space for admissible partial maps.

The objective is not necessarily to eliminate all coordinates. It is to expose the algebraic restrictions on \\(\Phi\\).

Task 3. Determine whether the family of partial maps is universal enough for hardness.

Given a general rectangular pencil

\\[ \lambda E-F, \qquad \operatorname{rank}E=\rho, \\]

ask whether it can be realized, up to the appropriate equivalence, as

\\[ \lambda\iota_R-\Phi_R \\]

for some admissible augmentation.

If the answer is yes for a sufficiently broad class of pencils, hardness becomes much more plausible.

If the answer is no, characterize the obstruction.

This is arguably the most important question for Approach A.

Task 4. Strengthen B.13.

Study the incidence projection relative to the admissible parameter locus.

The objective is to replace

\\[ \operatorname{pr}\_K(\mathfrak I) \ne\mathbb P(K) \\]

with a condition that remains useful when the unrestricted incidence projection is surjective.

Task 5. Separate the fixed-candidate and family-existence algorithms.

Establish the best possible exact algorithm for a fixed partial pencil.

Then investigate whether the additional constraints defining the admissible family permit a more efficient search.

Do not assume that a polynomial fixed-candidate test implies a polynomial family-existence test.

# 10. What I would put in the paper now

There is a useful distinction between what the project has proved and what it hopes to prove.

I would make the following claims.

### Claims that are suitable for the current manuscript

1. A quotient-space representation of the spectral condition.
2. A precise description of the permanent kernel.
3. A structural characterization of the finite spectral obstruction.
4. The partial-eigenvector characterization.
5. The fixed-candidate maximal-minor gcd criterion.
6. The right-minimal-index and infinite-elementary-divisor structure.
7. The equality obstruction.
8. The rank barrier and incidence-based sufficient infeasibility criteria.
9. The chart-free \\(\exists\mathbb R\\) upper bound, provided its encoding is fully audited.

### Claims that should remain open problems

1. NP-hardness of \\(q\_{\min}\\).
2. \\(\exists\mathbb R\\)-hardness of DEC-\\(\Theta\\).
3. A polynomial-time algorithm for DEC-\\(\Theta\\).
4. A complete intrinsic classification of all feasible orders.
5. A polynomial test for the existence of an admissible augmentation.

There is no need to force a complexity result into the current paper.

A rigorous structural paper with a clearly identified open complexity problem is preferable to a paper that makes an insufficiently justified hardness claim.

# 11. Proposed central theorem and paper contribution

I would make the partial-eigenvector characterization the conceptual centre of the manuscript.

The following is the theorem statement I would aim to publish, subject to checking the equivalences and hypotheses in the complete proofs.

Proposed central theorem

# Intrinsic characterization of spectral feasibility

Let \\(\mathcal L\\) satisfy the algebraic condition (5a), and let \\(V,S,W,\Phi\\) be the associated quotient spaces and partial linear map.

Define

\\[ P\_\Phi(\lambda)=\lambda\iota-\Phi, \\]

where \\(\iota:W\hookrightarrow\mathbb C^q\\) is the inclusion in the corresponding coordinates.

Then the following conditions are equivalent:

1. The original spectral condition (5b) holds.
2. The quotient pencil has full column rank for every finite \\(\lambda\\).
3. There is no nonzero partial eigenvector:

   \\[\
   \nexists,0\ne w\in W,\quad\
   \Phi(w)\in\mathbb Cw.\
   \\]
4. The maximal minors of \\(P\_\Phi(\lambda)\\) have constant nonzero gcd.

In addition, the quotient-kernel structure is governed by the permanent subspace \\(S\\), as specified in B.17.

The important feature of this theorem is that it gives four different perspectives on the same phenomenon:

- Original rank formulation.
- Quotient-pencil formulation.
- Geometric partial-eigenvector formulation.
- Polynomial determinantal formulation.

That is a strong and coherent mathematical result.

It also creates a natural transition to the complexity question: fixed-candidate feasibility is algebraically decidable, but the existence of a suitable candidate remains unresolved.

# 12. Final assessment

I want to emphasize one point about the direction of the research.

The original problem looked like a dimension-minimization problem:

\\[ q\_{\min} = \min\\{q:\exists R,\ (5a),(5b)\\}. \\]

The project has progressively revealed that the dimension constraint is only part of the story.

The algebraic condition (5a) determines a family of admissible augmentations. The spectral condition (5b) then asks whether one can choose a member of that family avoiding every finite partial eigenvalue.

This leads to a much more revealing formulation:

\\[ \boxed{ \begin{aligned} &\text{Find an admissible }R\\\ &\text{such that } \mathcal E\_{\Phi_R}=\varnothing. \end{aligned} } \\]

I believe this is the right formulation around which to organize the next stage of the research.

The main strategic point is:

First understand the geometry and algebra of the family of partial pencils. Then decide whether the family is sufficiently restricted to permit a polynomial algorithm, or sufficiently expressive to encode a hard real-algebraic problem.

That approach keeps both possibilities open without prematurely committing to either.

My preferred immediate direction is to complete the B.17–B.23–B.24–B.8 synthesis and establish the exact relation to B.6. Once this is done, the project will have a substantially stronger mathematical foundation for both the hardness programme and the algorithmic programme.

The current results already justify a serious research manuscript, provided the novelty comparison with Fernando's two papers is completed and the technical points identified above are resolved.

## References and source basis

The mathematical assessment above is based primarily on your uploaded research-status report.&#x20;

29_status_and_requests.md



Additional literature consulted:

1. Fernando, A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions, arXiv:2609.33615 (2026).&#x20;

   [image](https://www.google.com/s2/favicons?domain=https://papers.cool\&sz=32)

   Cool Papers - Immersive Paper Discovery

2. Fernando, Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger, arXiv:2609.37992 (2026).&#x20;

   [image](https://www.google.com/s2/favicons?domain=https://papers.cool\&sz=32)

   Cool Papers - Immersive Paper Discovery

3. Löfberg, Static output-feedback stabilization is NP-hard, arXiv:2609.16886 (2026).&#x20;

   [image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

   arXiv

4. Schaefer, Cardinal, and Miltzow, The Existential Theory of the Reals as a Complexity Class: A Compendium (2026).&#x20;

   [image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

   Springer Nature Link

5. Dodig, Matrix pencils completion problems II, Linear Algebra and its Applications (2008).&#x20;

   [image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

   ScienceDirect

6. Roca and Silva, Pencils with prescribed constant subpencils over arbitrary fields, Linear Algebra and its Applications (2014).&#x20;

   [image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

   ScienceDirect



One final recommendation: Before starting a hardness reduction, I would make the exact realization problem for \\(\lambda\iota-\Phi\\) the next technical milestone. It is the point where the project's strongest new structural insight meets its most important unresolved computational question.