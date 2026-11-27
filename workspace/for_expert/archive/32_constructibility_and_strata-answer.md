# Mathematical review of `32_constructibility_and_strata.md`

This report makes meaningful progress on the algebraic-geometric side of the project. In particular, the incidence reformulation on \\(\mathbb P(W_K)\\) is well motivated, and the proposed constructibility argument has a sound core. However, I would not yet accept the constructibility claim exactly as stated, for two reasons:

1. the bounded-degree Bézout step needs an explicit lemma and proof;
2. the normal-rank stratum must be restricted to candidates satisfying (5a), or the report must independently establish that the normal rank of \\(Q\_{\mathcal L}\\) equals the stratum index.

The first issue is readily repairable. The second is a more important logical qualification: the determinantal divisor \\(\Delta_k\\) is the correct test for (5b) only when \\(k\\) is indeed the normal rank of the pencil.

My recommendations are:

- prove a Bézout degree bound of \\(D=k-1\\) for the \\(k\times k\\) minors;
- define the strata inside the (5a)-admissible locus;
- keep the real and complex augmentation problems separate;
- retain NP-hardness as a meaningful target, with \\(\exists\mathbb R\\)-hardness as a stronger target for real data and \\(\exists\mathbb C\\)-hardness for complex data;
- do not restrict the general complexity problem to constant-\\(k\\) strata merely because the present determinantal encoding becomes exponentially large in the middle regime.

I discuss the five questions below.

## 1. Is the constructibility argument correct?

### 1.1 The linear-system argument is correct once the degree bound is justified

Fix a candidate \\(R\\) and a stratum index \\(k\\). Let

\\[ p_1(\lambda;R),\ldots,p_N(\lambda;R) \\]

be the \\(k\times k\\) minors of \\(Q\_{\mathcal L}(\lambda)\\), where

\\[ N=\binom{m}{k}\binom{n}{k}. \\]

Each \\(p_i\\) has degree at most \\(k\\).

The condition

\\[ \gcd(p_1,\ldots,p_N)\in\mathbb C^\times \tag{1} \\]

is equivalent to the existence of polynomials \\(u_i\\) satisfying

\\[ \sum\_{i=1}^{N}u_i(\lambda)p_i(\lambda;R)=1. \tag{2} \\]

If we know that the \\(u_i\\) can be chosen with a uniform degree bound \\(D\\), write

\\[ u_i(\lambda)=\sum\_{j=0}^{D}u\_{ij}\lambda^j. \\]

Matching coefficients in (2) gives a finite linear system

\\[ M(R)u=b, \tag{3} \\]

where:

- the entries of \\(M(R)\\) are polynomial functions of the entries of \\(R\\);
- \\(u\\) is the vector of Bézout coefficients;
- \\(b\\) is the coefficient vector of the constant polynomial \\(1\\).

For each fixed \\(R\\), system (3) is solvable exactly when

\\[ \operatorname{rank}[M(R)\mid b] = \operatorname{rank}M(R). \tag{4} \\]

This part of the argument is correct. The rank equality describes a constructible subset: it is the finite union, over possible ranks \\(s\\), of the locally closed conditions

\\[ \operatorname{rank}M(R)=s,\qquad \operatorname{rank}[M(R)\mid b]=s. \\]

The missing point is exactly the one you identified: why may the \\(u_i\\) be truncated at a fixed degree without losing solutions?

### 1.2 A stronger bounded-degree lemma: \\(D=k-1\\) suffices

There is a useful elementary argument that gives a better bound than a repeated extended-Euclidean estimate.

Lemma (bounded-degree Bézout identity in one variable).\
Let \\(\mathbb F\\) be an infinite field, and let

\\[ p_1,\ldots,p_N\in\mathbb F[\lambda] \\]

be polynomials of degree at most \\(d\\). If

\\[ \gcd(p_1,\ldots,p_N)=1, \\]

then there exist \\(u_1,\ldots,u_N\in\mathbb F[\lambda]\\) such that

\\[ \sum\_{i=1}^N u_i p_i=1, \qquad \deg u_i\le d-1 \\]

for every \\(i\\), with the usual convention that zero coefficients are permitted.

For \\(d=0\\), the conclusion is immediate: at least one \\(p_i\\) is a nonzero constant.

Proof for \\(d\ge1\\).

Choose a nonzero polynomial among the \\(p_i\\), and relabel it as \\(p_1\\). If \\(p_1\\) is a nonzero constant, the result is immediate. Otherwise, let its distinct roots in an algebraic closure be

\\[ \alpha_1,\ldots,\alpha_s. \\]

Since the gcd of all the \\(p_i\\) is \\(1\\), for each root \\(\alpha_j\\), at least one of the remaining polynomials \\(p_2,\ldots,p_N\\) is nonzero at \\(\alpha_j\\).

Consider constant linear combinations

\\[ g=\sum\_{i=2}^{N}c_i p_i. \\]

For each \\(\alpha_j\\), the condition \\(g(\alpha_j)=0\\) defines a proper linear subspace of the coefficient space of the \\(c_i\\). There are only finitely many roots. Since \\(\mathbb F\\) is infinite, a finite union of proper linear subspaces cannot cover the whole coefficient space. We can therefore choose constants \\(c_i\\) such that

\\[ g(\alpha_j)\ne0 \qquad\text{for every }j. \\]

It follows that

\\[ \gcd(p_1,g)=1. \\]

By the ordinary extended Euclidean algorithm, there exist \\(a,b\in\mathbb F[\lambda]\\) such that

\\[ a p_1+b g=1, \\]

with

\\[ \deg a<\deg g,\qquad \deg b<\deg p_1. \\]

Both degrees are at most \\(d-1\\). Substituting the definition of \\(g\\),

\\[ a p_1+\sum\_{i=2}^{N}(bc_i)p_i=1. \\]

Every coefficient polynomial has degree at most \\(d-1\\), as required. \\(\square\\)

This proof is particularly convenient for your application because \\(\mathbb C\\) is infinite.

Application to the report. Take \\(d=k\\). For every fixed candidate \\(R\\) for which the gcd is a unit, there is a Bézout representation with

\\[ \boxed{\deg u_i\le k-1.} \tag{5} \\]

Thus the truncation is justified. You may use the slightly looser bound \\(D=k\\) if it makes the formalisation or indexing simpler, but \\(D=k-1\\) is available.

There is one qualification: if \\(k=0\\), handle the zero-rank case separately. With the conventional empty-minor convention, the \\(0\times0\\) minor is \\(1\\), so the determinantal condition is automatic. Alternatively, state the Bézout argument only for \\(k\ge1\\) and deal with \\(k=0\\) directly.

### 1.3 The resulting constructibility theorem

I would state the result as follows.

Theorem (constructibility of the unit-gcd locus).\
Let \\(p_1(\lambda;R),\ldots,p_N(\lambda;R)\\) be polynomials in \\(\lambda\\) of degree at most \\(d\\), whose coefficients are polynomial functions of a parameter \\(R\in\mathbb C^s\\). Then

\\[ \mathcal U= \left\\{R\in\mathbb C^s: \gcd(p_1(\lambda;R),\ldots,p_N(\lambda;R))\in\mathbb C^\times \right\\} \\]

is constructible.

Proof. By the lemma, membership is equivalent to the existence of \\(u_i\\) of degree at most \\(d-1\\) satisfying (2). Coefficient comparison gives a finite linear system in the coefficients of the \\(u_i\\). Its solvability is the rank equality (4), which is a constructible condition on \\(R\\). \\(\square\\)

This is stronger than merely proving the claim for matrix-pencil minors: it applies to any finite family of univariate polynomials with uniformly bounded degree and polynomially parameterised coefficients.

32_constructibility_and_strata.md

### 1.4 An important additional qualification: the stratum must be admissible

There is a separate issue in the current formulation.

You define

\\[ \mathcal S_k= \left\\{ R: \operatorname{rank} \begin{bmatrix} \mathcal L\\\CA\\\C \end{bmatrix} =k \right\\}. \\]

But (5b) uses the normal rank of

\\[ Q\_{\mathcal L}(\lambda) = \begin{bmatrix} \lambda\mathcal L-\mathcal LA\\\CA\\\C \end{bmatrix}. \\]

These two ranks are equal under (5a), not automatically for arbitrary \\(R\\).

Indeed, put

\\[ B=\begin{bmatrix}\mathcal L\\\CA\\\C\end{bmatrix}. \\]

Under (5a), the row space of \\(\mathcal LA\\) is contained in the row space of \\(B\\). Therefore, for every \\(\lambda\\),

\\[ \operatorname{row}Q\_{\mathcal L}(\lambda) \subseteq\operatorname{row}B. \\]

Conversely, for \\(\lambda\ne0\\),

\\[ \mathcal L = \lambda^{-1}\bigl((\lambda\mathcal L-\mathcal LA)+\mathcal LA\bigr), \\]

and the right-hand side belongs to the row space of \\(Q\_{\mathcal L}(\lambda)\\), since (5a) puts \\(\mathcal LA\\) in the row space of \\(B\\). Together with the \\(CA,C\\) blocks, this gives

\\[ \operatorname{row}B \subseteq\operatorname{row}Q\_{\mathcal L}(\lambda). \\]

Thus

\\[ \operatorname{rank}Q\_{\mathcal L}(\lambda) = \operatorname{rank}B=k \qquad(\lambda\ne0), \\]

and hence the normal rank is \\(k\\).

Without (5a), the normal rank of \\(Q\_{\mathcal L}\\) need not equal \\(k\\). Consequently, the \\(k\\)-minors need not be the maximal non-identically-zero minors of the pencil, and their gcd being a unit is not, in general, the criterion for (5b).

Correction I recommend: define the admissible rank stratum

\\[ \boxed{ \mathcal S_k^{(a)} = \left\\{ R: \operatorname{rank}B=k,\quad \operatorname{rank} \begin{bmatrix} \mathcal LA\\\B \end{bmatrix} =k \right\\}. } \tag{6} \\]

Then formulate the constructibility result on \\(\mathcal S_k^{(a)}\\). Equivalently, retain \\(\mathcal S_k\\) but explicitly intersect it with the (5a) locus.

This is not just a technical improvement: it makes the index of the determinantal divisor agree with the \\(h\\) in (5b).

## 2. Which field should the free block \\(R\\) range over?

This is a modelling decision, not something determined by the fact that the spectral parameter \\(\lambda\\) is complex.

There are two distinct formulations.

### 2.1 Real augmentation with complex spectral testing

If \\(A,C,L_0\\) are real matrices and the augmentation is intended to be a real matrix, then the natural problem is

\\[ R\in\mathbb R^{(q-r)\times n}, \qquad \lambda\in\mathbb C. \tag{7} \\]

This is the usual situation when the matrices represent a real system and complex eigenvalues are used to test its spectral properties.

In this formulation:

- the candidate variables are real;
- the pencil is evaluated over \\(\mathbb C\\);
- the rank and gcd conditions are interpreted over \\(\mathbb C\\);
- the decision problem is a real-algebraic feasibility problem.

The fact that \\(\lambda\\) ranges over \\(\mathbb C\\) does not force \\(R\\) to be complex.

If the entries of \\(A,C,L_0\\) are rational or real algebraic, the resulting polynomial constraints can be represented over the corresponding effective coefficient field. If the input contains arbitrary real constants without a finite representation, a conventional bit-complexity classification is not yet well-defined.

### 2.2 Complex augmentation

If instead

\\[ R\in\mathbb C^{(q-r)\times n}, \tag{8} \\]

then the parameter space is complex affine space, and the constructibility theorem applies directly over \\(\mathbb C\\).

The resulting feasibility question belongs naturally to the existential theory of algebraically closed fields, often denoted by \\(\exists\mathbb C\\) in complexity discussions.

This is a genuinely different optimisation problem. Allowing complex augmentation matrices may change the minimum order, so it should not be silently substituted for the real problem.

### 2.3 What if the data are complex but \\(R\\) is real?

Your report says the literature formulation uses complex matrix data, while the existence question has been stated in real terms.&#x20;

32_constructibility_and_strata.md



That case is also mathematically well-defined:

\\[ A,C,L_0\text{ fixed over }\mathbb C, \qquad R\in\mathbb R^{(q-r)\times n}. \tag{9} \\]

For real \\(R\\), the coefficients of the minors are complex-valued polynomials in real variables. A complex polynomial equality is equivalent to the simultaneous vanishing of its real and imaginary parts. A complex nonvanishing condition is equivalent to

\\[ (\operatorname{Re} f)^2+(\operatorname{Im} f)^2\ne0. \\]

Thus the resulting parameter locus can still be expressed by finitely many real polynomial equalities and inequations.

For complexity purposes, however, the coefficient representation matters. If the fixed complex data are rational or algebraic, their real and imaginary parts can be represented effectively. Arbitrary complex constants require a suitable computational model.

### 2.4 My recommendation

For the main paper, I would preserve the real augmentation problem if that is the intended observer-design problem:

\\[ \boxed{R\in\mathbb R^{(q-r)\times n},\quad \lambda\in\mathbb C.} \\]

Then state a separate complexification corollary:

\\[ R\in\mathbb C^{(q-r)\times n}. \\]

This prevents the paper from inadvertently proving a result for a larger class of admissible augmentations than the original problem permits.

## 3. What is the appropriate hardness target?

The answer depends on the coefficient field and the formulation of the decision problem.

### 3.1 For real augmentation, \\(\exists\mathbb R\\)-hardness is a meaningful stronger target

If the augmentation is real and the input data have an effective real-algebraic representation, the natural upper-bound framework is the existential theory of the reals.

Your constructibility result does not invalidate this target. It says that, for each fixed candidate \\(R\\), the admissibility condition can be described using polynomial equalities and inequations. It does not say that finding a real \\(R\\) satisfying those conditions is easy.

In particular, real polynomial feasibility is not restricted to equations alone. Nonvanishing conditions can encode strict inequalities with auxiliary variables. For example,

\\[ f(x)>0 \quad\Longleftrightarrow\quad \exists y:\ f(x)y^2=1 \\]

over \\(\mathbb R\\). Also,

\\[ f(x)\ge0 \quad\Longleftrightarrow\quad \exists z:\ f(x)=z^2. \\]

So a constructible description involving equations and inequations can still have substantial real-algebraic complexity.

This is why the statement

> “The feasibility set is constructible, therefore the decision problem is easier than \\(\exists\mathbb R\\)”

would be unjustified.

There is a distinction between:

- the geometric complexity of the set of admissible parameters;
- the computational complexity of deciding whether that set has a real point.

The first is what your current argument establishes. The second is the hardness question.

### 3.2 For complex augmentation, consider \\(\exists\mathbb C\\)-hardness

If \\(R\\) is complex, the relevant algebraic feasibility problem is over an algebraically closed field. The natural stronger hardness target is then \\(\exists\mathbb C\\)-hardness.

I would not describe this as simply a sharpening of \\(\exists\mathbb R\\)-hardness: the two problems have different underlying fields and different geometric semantics. The reduction direction must be stated explicitly.

### 3.3 NP-hardness remains a valid and useful target

For the real problem, I would retain NP-hardness as a primary target or at least a milestone.

A proof of \\(\exists\mathbb R\\)-hardness would imply NP-hardness under the standard polynomial-time many-one reductions, since Boolean satisfiability can be encoded as real polynomial feasibility using variables constrained to \\(0\\) or \\(1\\). But an NP-hardness reduction may be much easier to discover and prove.

My suggested hierarchy is:

1. Establish NP-hardness if a combinatorial reduction is available.
2. Investigate \\(\exists\mathbb R\\)-hardness if the geometry of the rank and spectral constraints supports a general real-algebraic encoding.
3. For the complex-augmentation variant, investigate \\(\exists\mathbb C\\)-hardness separately.

I would not change the target merely because the fixed-candidate feasibility locus is constructible.

### 3.4 One important distinction: decision versus optimisation

Your original question asks whether computing \\(q\_{\min}\\) is NP-hard.&#x20;

32_constructibility_and_strata.md



For precision, define the associated decision problem:

\\[ \mathrm{DEC}: \quad \text{Given }q,\text{ does there exist }R \text{ such that (5a), (5b) hold?} \tag{10} \\]

Then establish hardness for \\(\mathrm{DEC}\\). The optimisation problem of computing \\(q\_{\min}\\) is at least as hard as its threshold decision version, provided the reduction preserves the relevant input and threshold encoding.

I would make this decision problem the formal complexity object in the paper. The optimisation statement can then be derived as a corollary.

## 4. Should the complexity discussion be restricted to constant-\\(k\\) strata?

No—not for the general problem. There is also a correction needed in the report's size audit.

### 4.1 The stated polynomial-size criterion is not correct

The report states that the number

\\[ N=\binom{m}{h}\binom{n}{h} \tag{11} \\]

is polynomial exactly when

\\[ \min(h,n-h,m-h) \\]

is bounded.&#x20;

32_constructibility_and_strata.md



This criterion is insufficient.

For example, take

\\[ m=\lfloor n/2\rfloor,\qquad h=m-1. \\]

Then

\\[ m-h=1, \\]

so the minimum in the proposed criterion is bounded. But

\\[ \binom{m}{h}=m, \qquad \binom{n}{h}=\binom{n}{m-1}, \\]

and the second factor is exponentially large in \\(n\\).

The problem is that both binomial factors must be controlled independently.

For a family of instances with growing dimensions, the appropriate condition is:

\\[ \boxed{ \min(h,m-h)=O(1) \quad\text{and}\quad \min(h,n-h)=O(1). } \tag{12} \\]

Indeed, each binomial coefficient is polynomially bounded precisely when its lower index or its complementary index is bounded. Thus (12) is the correct criterion for the product to be polynomially bounded, assuming the bounds are uniform over the family.

Since \\(h\le\min(m,n)\\), this has two main boundary regimes:

- \\(h=O(1)\\);
- both \\(m-h=O(1)\\) and \\(n-h=O(1)\\).

There can also be polynomial-size behaviour when the relevant dimensions themselves are bounded, but that is already covered by treating the family parameters as fixed.

### 4.2 Consequences for the regimes in the report

The two regimes you identify are still meaningful:

- Small \\(q\\): if \\(m=q+2p\\) is bounded, then \\(h\le m\\) is bounded, so the number of minors is polynomial in \\(n\\).
- Near full column rank: if both \\(m-h\\) and \\(n-h\\) are bounded, then both binomial factors are polynomially bounded.

But “\\(q\\) near \\(n-p\\)” alone is not enough unless it implies the required two complementary dimensions are bounded. This should be checked from the exact relationship among \\(m,n,h,q,p\\), not asserted from the order description alone.

### 4.3 Do not restrict the general hardness question

The exponential number of minors in the middle regime means that this particular encoding may be exponentially large. It does not mean the underlying decision problem is necessarily hard, nor does it mean that the problem is easier in the boundary regimes.

There may be alternative encodings using:

- structured rank constraints;
- quotient-space formulations;
- a smaller set of polynomial invariants;
- a direct incidence or elimination formulation;
- problem-specific properties of the pencil that make many minors redundant.

Conversely, a hardness reduction may naturally use middle-rank instances. Restricting the complexity problem to constant \\(k\\) could exclude precisely the instances needed for a meaningful hardness theorem.

My recommendation is to present the complexity discussion in two layers:

1. General problem: retain all admissible \\(k\\), and state honestly that the current all-minors Bézout encoding can be exponential in the middle regime.
2. Boundary-stratum results: give polynomial-size encoding results under the explicit conditions (12).

That is a more accurate and useful result than restricting the main problem to constant \\(k\\).

## 5. What should be prioritised next?

Of the three proposed tasks, I recommend:



Next priority

&#x20;Complete the explicit Bézout degree bound and close the constructibility theorem.



Then proceed to the family version of the coverage criterion. Leave the comparison between the two pencils as a longer-term structural question.

This ordering is based on the current state of the project, rather than on the relative mathematical importance of the three topics.

### 5.1 Why the degree bound should come first

The Bézout lemma above resolves the principal gap in II.4. It is:

- elementary and self-contained;
- independent of the unresolved comparison between the two pencils;
- applicable to every fixed normal-rank stratum;
- directly useful for the algebraic formulation of the decision problem;
- suitable for a short Lean formalisation.

It also gives a more economical encoding than the one currently reported. For \\(k\ge1\\), one may use

\\[ D=k-1, \\]

so there are \\(kN\\) Bézout coefficient variables rather than \\((k+1)N\\), where

\\[ N=\binom{m}{k}\binom{n}{k}. \\]

The coefficient equations have degrees in \\(\lambda\\) at most \\(2k-1\\).

The next report could therefore contain a complete theorem with:

1. the bounded-degree Bézout lemma;
2. the finite coefficient-system construction;
3. the rank-solvability equivalence;
4. the constructibility theorem;
5. the correction restricting the rank strata to (5a)-admissible candidates;
6. the separate \\(k=0\\) convention.

That would close a specific mathematical gap rather than merely report another promising direction.

### 5.2 Why the family coverage criterion comes second

The incidence reformulation is already correct for a fixed candidate. Your report establishes that

\\[ \mathcal E_K = \\{[w]\in\mathbb P(W_K): \Phi_K(w)\wedge\iota_K(w)=0\\} \\]

is the natural projective obstruction locus, with the pullback to \\(\mathbb P(K)\setminus\mathbb P(D)\\) having fibre dimension \\(k-\omega\\).&#x20;

32_constructibility_and_strata.md



The next difficulty is not another fixed-candidate dimension calculation. It is the family problem: as \\(R\\) varies, the subspace

\\[ W_K(R)=\mathcal L(R)K \\]

can change dimension and position.

A rigorous family theorem should proceed by stratifying the parameter space according to

\\[ \operatorname{rank}(\mathcal L(R)|\_K)=\omega. \\]

On each constant-rank stratum, the images \\(W_K(R)\\) form a family of \\(\omega\\)-dimensional subspaces. One can then formulate the projective incidence construction relative to the corresponding Grassmannian or projective bundle.

I expect this to be a more involved argument than the Bézout lemma, but it is the natural next structural step after the constructibility theorem.

### 5.3 Why the pencil comparison should wait

The relation between

\\[ \overline N\_{\mathcal Z}(\lambda):V/S\to X/\mathcal Z \\]

and

\\[ P_K(\lambda):W_K\to\mathbb C^q \\]

is potentially the deepest structural question. But the current report does not provide enough information to establish the comparison, and the earlier counterexample already rules out one tempting identification.

I would not make this comparison a prerequisite for publishing the intrinsic partial-eigenvector theorem or the constructibility theorem. It should be pursued separately once the definitions of \\(X,\mathcal Z\\) and the coefficient pair of \\(\overline N\_{\mathcal Z}\\) are fully fixed.

## 6. Two additional observations worth preserving

### 6.1 The incidence formulation does not require a projective spectral parameter

This is a genuine simplification. The obstruction

\\[ \Phi_K(w)\in\mathbb Cw \\]

already means that \\(w\\) is an eigenvector of the induced map in the partial-eigenvector sense. The scalar eigenvalue is determined by \\(w\ne0\\), so there is no need to add a projective eigenvalue parameter.

The wedge formulation

\\[ \Phi_K(w)\wedge\iota_K(w)=0 \\]

gives homogeneous quadratic equations on \\(\mathbb P(W_K)\\). It is the correct fixed-candidate incidence formulation.&#x20;

32_constructibility_and_strata.md



I would retain this as a separate proposition in the structural paper, rather than burying it inside the coverage lemma.

### 6.2 Constructibility is not the same as a polynomial-time algorithm

This distinction deserves explicit emphasis in the manuscript.

Your result can establish that the admissible parameter locus is constructible. The Bézout encoding can establish that membership in that locus has a finite algebraic certificate. Neither statement implies that:

- the certificate has polynomial size in all regimes;
- the existential feasibility problem is polynomial-time decidable;
- the minimum \\(q\\) can be computed efficiently.

The middle-stratum growth of the minor count is a concrete warning. The correct size analysis should use (12), rather than the single-minimum criterion in the current report.

## 7. Proposed theorem package for the next revision

I would aim to close the next report with the following three statements.

Theorem 1 — Bounded-degree Bézout certificate.

For \\(N\\) univariate polynomials of degree at most \\(d\\) over an infinite field, their gcd is a unit if and only if there exist Bézout multipliers of degree at most \\(d-1\\) whose weighted sum is \\(1\\), with the degree-zero case treated separately.

Theorem 2 — Constructibility on admissible rank strata.

For each \\(k\\), the set

\\[ \left\\{ R: \operatorname{rank} \begin{bmatrix}\mathcal L\\\CA\\\C\end{bmatrix}=k,\quad (5a),\quad \Delta_k\in\mathbb C^\times \right\\} \\]

is constructible, with \\(\Delta_k\\) defined using all \\(k\times k\\) minors of \\(Q\_{\mathcal L}(\lambda)\\).

Theorem 3 — Finite stratified decision description.

The full feasibility locus is the finite union of the admissible rank-stratum loci:

\\[ \mathrm{FEAS} = \bigcup\_{k=0}^{\min(m,n)} \left\\{ R: \operatorname{rank}B=k,\ (5a),\ \Delta_k\in\mathbb C^\times \right\\}, \qquad B=\begin{bmatrix}\mathcal L\\\CA\\\C\end{bmatrix}, \\]

using the \\(k=0\\) convention separately.

This is the clean modular statement that I would want before proceeding to a complexity reduction.

## Final assessment

The report's central constructibility idea is correct after two repairs: supply the bounded-degree lemma, and ensure the rank strata are restricted to (5a)-admissible candidates. The first repair is now available with the explicit bound \\(D=k-1\\); the second should be incorporated into the formal statement immediately.

The field choice should follow the original modelling problem, not the complex spectral parameter. If the intended augmentation is real, retain real \\(R\\) and formulate the complexity problem over the reals. Constructibility does not remove the possibility of NP-hardness or \\(\exists\mathbb R\\)-hardness.

Finally, the size audit needs the corrected two-binomial criterion. Do not restrict the main complexity problem to constant-rank strata just to make the current encoding polynomial-sized.

My concrete request for the next research round: implement and verify the bounded-degree Bézout lemma, then give the corrected constructibility theorem on the (5a)-admissible rank strata. That is the most achievable result with the greatest immediate payoff for the project.