# Mathematical assessment of `06_state_corrections_and_assessment.md`

I have examined the complete report, including the corrected \\(n=7\\) example, the integer obstruction, the whole-family occlusion theorem, and all eight questions.

My overall assessment is that the project has reached a more mathematically coherent stage. The most important development is the separation of two fundamentally different mechanisms:

- A dimension obstruction, determined by the relative positions of subspaces.
- A spectral obstruction, determined by finite elementary divisors of a matrix pencil.

This distinction should become the organizing principle of the next theoretical development.

There is also an important opportunity that I think has not yet been fully exploited: the whole-family occlusion argument can be reformulated for arbitrary \\(r\\) and arbitrary \\(h\\), without requiring the special rational map \\(\Phi\\) used in II.E.

I will address the eight questions individually, then give a proposed theorem and a revised research plan.

# 1. Q1 — A formulation of the spectral obstruction depending only on \\(\mathcal Z\\)

Important: an exact general formulation is available

This is the question I would prioritize. In fact, the formulation can be obtained directly from the factorization already established in your work.

## 1.1 The fundamental observation

Fix an augmentation \\(\mathcal L\\) satisfying (5a). Then

\\[ \mathcal LA=\Lambda\mathcal L+G_0C+G_1CA. \\]

Consequently, for every \\(x\in V=\ker[C;CA]\\),

\\[ \mathcal LAx=\Lambda\mathcal Lx. \\]

Let

\\[ \mathcal Z=\ker[C;\mathcal L]. \\]

Since \\(x\in V\\), we have \\(Cx=CAx=0\\). Therefore,

\\[ \begin{aligned} x\notin\mathcal Z &\iff \mathcal Lx\ne0,\\\ (\lambda I-A)x\in\mathcal Z &\iff \mathcal L(\lambda I-A)x=0. \end{aligned} \\]

The second equivalence uses the fact that

\\[ C(\lambda I-A)x=0. \\]

Combining these identities gives

\\[ \mathcal L(\lambda I-A)x =(\lambda I-\Lambda)\mathcal Lx. \\]

Thus the exact spectral failure condition is

\\[ \boxed{ \exists x\in V,\ \exists\lambda\in\mathbb C: \quad x\notin\mathcal Z,\qquad (\lambda I-A)x\in\mathcal Z. } \tag{Q1.1} \\]

This is not merely a sufficient condition. It is necessary and sufficient.

In particular, it remains valid when \\(h\<n\\).

That is important because the original occlusion argument used \\(h=n\\) to convert a nonzero kernel vector into a rank drop. The formulation above does not need that conversion: it describes the rank drop itself.

## 1.2 Quotient-space formulation

Let

\\[ X=\mathbb C^n, \qquad J\_{\mathcal Z}:V\longrightarrow X/\mathcal Z, \\]

be the natural quotient map

\\[ J\_{\mathcal Z}x=x+\mathcal Z. \\]

Define another linear map

\\[ T\_{\mathcal Z}:V\longrightarrow X/\mathcal Z, \qquad T\_{\mathcal Z}x=Ax+\mathcal Z. \\]

Then (Q1.1) becomes

\\[ \boxed{ \exists x\in V: \quad J\_{\mathcal Z}x\ne0,\qquad T\_{\mathcal Z}x=\lambda J\_{\mathcal Z}x \quad\text{for some }\lambda\in\mathbb C. } \tag{Q1.2} \\]

Therefore,

\\[ \boxed{ (5b) \iff \text{the pencil }T\_{\mathcal Z}-\lambda J\_{\mathcal Z} \text{ has no nonzero finite generalized eigenvector} } \\]

where the phrase nonzero generalized eigenvector must specifically mean a vector \\(x\\) with \\(J\_{\mathcal Z}x\ne0\\).

There is a subtle point worth emphasizing.

This is generally a rectangular pencil:

\\[ T\_{\mathcal Z},J\_{\mathcal Z}:V\to X/\mathcal Z. \\]

It is not necessarily an ordinary endomorphism pencil on a single vector space. In particular, one cannot assume that it has an eigenvalue merely because its domain is nonzero.

That distinction is essential.

## 1.3 The bad-subspace locus

Define

\\[ \mathcal B= \left\\{ \mathcal Z\in\operatorname{Gr}(d,K): \exists x\in V,\ \exists\lambda\in\mathbb C,\ \begin{array}{l} x\notin\mathcal Z,\\\ (\lambda I-A)x\in\mathcal Z \end{array} \right\\}. \\]

Then

\\[ \boxed{ \text{An admissible }\mathcal Z\text{ satisfies (5b)} \iff \mathcal Z\notin\mathcal B. } \\]

This gives exactly the subspace-only formulation requested in Q1.

More importantly, it identifies the problem as a Grassmannian avoidance problem for a source–image incidence relation.

The incidence relation is

\\[ x\in V\setminus\mathcal Z, \qquad (\lambda I-A)x\in\mathcal Z. \\]

The two conditions must be retained together. Replacing them by the condition that \\(\mathcal Z\\) intersects a fixed set of vectors would generally lose information.

## 1.4 An alternative formulation through linear maps

Choose a matrix \\(P\_{\mathcal Z}\\) whose kernel is \\(\mathcal Z\\). Then the condition is

\\[ P\_{\mathcal Z}x\ne0, \qquad P\_{\mathcal Z}(\lambda I-A)x=0, \qquad x\in V. \\]

If \\(B_V\\) is a basis matrix for \\(V\\), write \\(x=B_Vu\\). The problem becomes

\\[ \exists u,\lambda: \quad P\_{\mathcal Z}B_Vu\ne0, \qquad P\_{\mathcal Z}(\lambda I-A)B_Vu=0. \tag{Q1.3} \\]

This is particularly useful computationally.

For a fixed \\(\mathcal Z\\), one can investigate the polynomial matrix

\\[ R\_{\mathcal Z}(\lambda) = P\_{\mathcal Z}(\lambda I-A)B_V. \\]

However, one must not simply test whether this matrix has full column rank. The nonzero condition is imposed on \\(P\_{\mathcal Z}B_Vu\\), not on \\(u\\) alone. A kernel vector belonging to \\(\ker(P\_{\mathcal Z}B_V)\\) is not a spectral obstruction.

That distinction should be explicitly preserved in the implementation.

Conclusion on Q1: I consider the quotient formulation a substantial theoretical improvement. It removes the special requirement \\(h=n\\) and works for \\(r\ge2\\), without constructing a scalar \\(\lambda(x)\\) from \\(L_0x\\).

# 2. Q2 — Is the integer obstruction known under another name?

My assessment is that the underlying mathematics is familiar, but your particular uniformity statement deserves separate treatment.

Recall

\\[ h=s_0+\dim\pi(V'), \\]

and the integer obstruction

\\[ h\ge q+r_1. \\]

Equivalently,

\\[ \boxed{ \dim\pi(V')\ge q+r_1-s_0. } \tag{Q2.1} \\]

This is fundamentally a dimension inequality arising from a quotient-space decomposition.

## 2.1 Relation to familiar concepts

The relevant mathematical ingredients are:

- Grassmannian dimension counting;
- quotient-space dimension formulas;
- rank inequalities;
- subspace transversality;
- intersection dimensions.

In observer theory, the surrounding language is usually that of functional observability, invariant subspaces, and observer-order bounds.

For example, Fernando and Trinh's work on functional observers introduced functional observability indices and a decomposition-based construction of minimum-order observers.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.tandfonline.com\&sz=32)

Get Access+1



The 2026 characterization also explicitly organizes admissible observer orders between the functional-observability lower bound and the reduced-order Luenberger upper bound.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arxiv.org+1



I would not claim that your threshold is a new general dimension theorem. It is an application of standard linear algebra to the particular geometry of the augmentation problem.

But there is a potentially useful contribution in the following consequence.

## 2.2 The order-uniformity theorem

Suppose

\\[ V'\cap S=\\{0\\}. \\]

Then

\\[ \dim\pi(V')=\dim V'=q-r. \\]

Therefore,

\\[ h=s_0+q-r. \\]

The integer obstruction becomes

\\[ s_0+q-r\ge q+r_1, \\]

or

\\[ \boxed{s_0\ge r+r_1.} \tag{Q2.2} \\]

Notice that the candidate augmentation has disappeared completely.

Thus, at an order for which every admissible \\(V'\\) satisfies \\(V'\cap S=0\\), the integer obstruction is uniform across the entire family.

This is the strongest form of the result that I would present.

There is one qualification: the condition \\(V'\cap S=0\\) must be established for the entire admissible family, not merely for sampled candidates.

## 2.3 Recommended terminology

I suggest using:

- dimension obstruction for \\(h\ge q+r_1\\);
- spectral obstruction for \\(d\_{\rm fin}>0\\) when the dimension obstruction does not apply.

These names are clearer than integer obstruction.

A useful refinement is to call

\\[ s_0\ge r+r_1 \\]

the uniform dimension criterion on transverse orders.

Conclusion on Q2: the threshold itself is elementary; the uniformity consequence is the more interesting result. I would make the latter the emphasis of the paper.

# 3. Q3 — Is the minimum-order problem computationally hard?

This is the question where I would be most conservative.

There are related hardness results in control theory, but none of the results I located establishes hardness of your exact continuous augmentation problem.

## 3.1 What is already known nearby?

A useful example is the 2025 work on structural functional observability and optimal sensor placement.

It establishes NP-hardness of selecting a minimum set of sensors to achieve functional observability under structural constraints.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://ieeexplore.ieee.org\&sz=32)

IEEE Xplore+1



However, that problem is different from yours.

| Sensor-placement problem             | Your augmentation problem              |
| ------------------------------------ | -------------------------------------- |
| Select a subset of available sensors | Choose continuous matrix entries       |
| Primarily combinatorial              | Algebraic and spectral                 |
| Discrete design variables            | Grassmannian/subspace design variables |
| Structural observability             | Constant-rank matrix-pencil condition  |

Consequently, the sensor-placement result cannot be directly used to claim NP-hardness of DEC(\\(q\\)).

It might be possible to encode a discrete selection problem through coordinate-subspace restrictions on \\(\mathcal L\\), but this would require a genuine reduction.

## 3.2 The three restricted cases

I would distinguish the following possibilities.

Case A: fixed \\(p,r\\), variable \\(n\\).

This is a legitimate hardness target.

Although the number of output and target rows is fixed, the number of state variables and augmentation parameters grows with \\(n\\).

A reduction could potentially encode a growing combinatorial instance in the state-space structure of \\(A\\).

I would prioritize this case.

Case B: \\(A\\) in companion form.

This is also interesting, but I would not assume it is easy.

Companion structure restricts the representation of the dynamics, but the augmentation subspace may still have substantial freedom.

A reduction could exploit polynomial multiplication, invariant factors, or structured matrix-pencil rank conditions.

One possibility is to investigate whether the quotient pencil can encode polynomial divisibility constraints.

Case C: \\(\mathcal L\\) restricted to coordinate subspaces.

This is the most natural route toward a discrete reduction.

If the candidate subspace is required to be coordinate-aligned, the design becomes a selection problem.

However, a coordinate restriction may make the problem substantially easier than the unrestricted problem. A hardness result in this restricted class would be valuable, but it would not automatically establish hardness for arbitrary complex augmentations.

## 3.3 The correct complexity formulation

I recommend fixing the following problem definitions:

\\[ \operatorname{DEC}(q): \quad \exists\mathcal L\in\mathbb C^{q\times n} \quad\text{satisfying (5a) and (5b)}. \\]

And separately,

\\[ \operatorname{MIN}: \quad \text{compute }q\_{\min}. \\]

For rational input matrices, an existential-real encoding is a reasonable upper-bound route, provided the complex variables are split into real and imaginary parts and the spectral condition is represented by a finite polynomial certificate.

But the hardness question must distinguish real and complex design variables.

A reduction from real quadratic feasibility cannot simply use complex variables and assume that real infeasibility is preserved.

### My recommendation

Do not claim NP-hardness, \\(\exists\mathbb R\\)-hardness, or completeness at this stage.

Instead, investigate:

\\[ \boxed{ \text{Is DEC}(q)\text{ hard when }p,r\text{ are fixed and }n\text{ varies?} } \\]

This is a sufficiently strong and mathematically meaningful target.

# 4. Q4 — Is \\(n_0-p\\) always the correct upper endpoint?

Yes, under the stated functional-observability assumption

I agree with the report's use of the interval

\\[ [q_0,n_0-p]. \\]

Here is the reasoning.

Let

\\[ \mathscr O=\operatorname{row}\mathcal O_C, \qquad \dim\mathscr O=n_0. \\]

Because

\\[ \operatorname{rank}[C;L_0]=p+r, \\]

the matrix \\(C\\) has full row rank \\(p\\), and

\\[ \operatorname{row}C\cap\operatorname{row}L_0=\\{0\\}. \\]

Functional observability gives

\\[ \operatorname{row}L_0\subseteq\mathscr O. \\]

Choose a basis of \\(\mathscr O/\operatorname{row}C\\), and choose representatives so that the rows of \\(L_0\\) are included in the resulting basis.

Let \\(\mathcal L\\) consist of these representatives. Then

\\[ \operatorname{rank}\mathcal L=n_0-p, \\]

and

\\[ \operatorname{row}[C;\mathcal L]=\mathscr O. \\]

Since the observability row space is \\(A\\)-invariant,

\\[ \mathscr O A\subseteq\mathscr O. \\]

Therefore,

\\[ \operatorname{row}(\mathcal LA) \subseteq\operatorname{row}[C;\mathcal L], \\]

which gives (5a).

For the spectral condition, use the standard reduced-order Luenberger observer construction on the observable subsystem. The resulting observer has order \\(n_0-p\\), contains the prescribed functional rows, and its observer dynamics can be assigned without introducing a finite elementary divisor in the corresponding pencil.

Thus,

\\[ \boxed{ q\_{\min}\le n_0-p. } \\]

The upper endpoint is not \\(n-p\\) unless the entire system is observable.

This distinction is important for systems containing an unobservable state subspace.

It is also consistent with Fernando's 2026 characterization, which identifies \\(n_0-p\\) as the upper endpoint and recovers the classical Luenberger order \\(n-p\\) under complete observability.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arxiv.org+1



### One recommendation

Add a regression test that constructs the upper-endpoint augmentation directly from a basis of the observable row space.

Then verify:

\\[ \operatorname{rank}[C;\mathcal L]=n_0, \\]

\\[ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=n_0, \\]

and

\\[ \gcd(\text{maximal minors of }Q\_{\mathcal L})=1. \\]

This should become a permanent consistency check in your implementation.

# 5. Q5 — Terminology

I recommend the following terminology throughout the paper.

| Mathematical condition                   | Recommended name               |
| ---------------------------------------- | ------------------------------ |
| \\(h\ge q+r_1\\)                         | Dimension obstruction          |
| \\(h\<q+r_1\\), but \\(d\_{\rm fin}>0\\) | Spectral obstruction           |
| \\(s_0\ge r+r_1\\) under transversality  | Uniform dimension criterion    |
| \\(\dim Y\ge q-r\\) with \\(h=n\\)       | Projective occlusion criterion |
| \\(d\_{\rm fin}=0\\)                     | Spectral feasibility           |

There are two reasons for preferring this terminology.

First, it distinguishes the source of the obstruction rather than merely describing its numerical form.

Second, it makes the logical relationship clearer:

\\[ \text{Failure} = \text{dimension obstruction} \quad\text{or}\quad \text{spectral obstruction}. \\]

The two mechanisms are not mutually exclusive as properties of an individual candidate: a candidate with \\(h\ge q+r_1\\) may also have a spectral rank drop. But for the purpose of excluding candidates, the dimension obstruction is already decisive.

I would explicitly state that the spectral obstruction is the remaining obstruction after the dimension test has passed.

# 6. Q6 — What is sufficient for a short mathematical note?

My recommendation is to write a focused note around three results, not five.

## 6.1 What I would definitely include

Result 1. The dimension obstruction theorem.

This is the cleanest standalone theorem.

State

\\[ h=s_0+\dim\pi(V') \\]

and derive

\\[ h\ge q+r_1 \iff \dim\pi(V')\ge q+r_1-s_0. \\]

Then prove the uniformity statement under \\(V'\cap S=0\\).

This result is short, exact, and useful.

Result 2. The published two-order-gap example.

This is an excellent illustration because the two failures have a common dimension-based explanation.

The advantage is that it connects the abstract criterion to an existing example rather than relying entirely on newly constructed instances.

Result 3. The \\(n=6\\) whole-family counterexample.

I would include this.

In fact, I think it is more mathematically interesting than the isolated \\(n=7\\) example.

Its importance is not that it establishes a general theorem about all \\(r\ge2\\). It demonstrates that passing the dimension obstruction does not guarantee spectral feasibility.

The projective occlusion proof provides a genuine mechanism for excluding an entire admissible family.

It should be presented explicitly as a sufficient condition with narrow hypotheses.

## 6.2 What I would include only after strengthening

The \\(n=7\\) order-three solution is a useful correction and a good exact certificate.

I would include it as a short supplementary example or a remark about the necessity of complete Grassmannian parametrization.

However, I would not make its sampled enumeration the basis of a general claim.

There is an important issue here:

> A finite rational grid on the three affine charts of \\(\operatorname{Gr}(2,3)\\) is not, by itself, a complete scan of the complex Grassmannian.

If the admissibility conditions reduce the possible nullspaces to a finite algebraic set, then a complete enumeration is possible. But this requires solving the defining polynomial equations and establishing completeness, not merely checking a rational grid.

I would ask your team to produce one of the following:

- An exact algebraic parametrization of all admissible nullspaces.
- A proof that the admissible set is finite, followed by exact root isolation or symbolic elimination.
- A theorem showing that every admissible nullspace is represented by one of the enumerated points.

Until then, the statement should be phrased as an extensive exact-arithmetic search, not a complete classification.

The same warning applies to the 486/486 enumeration.

## 6.3 What I would leave out

I would leave out the following as main results:

- The conjecture that dimension obstruction is the only generic obstruction.
- Claims about the codimension of the spectral failure locus.
- General conclusions about \\(r\ge2\\) based on the scalar-ratio construction.
- Complexity claims without a reduction.

These belong in a discussion section as open questions.

## 6.4 Suggested note structure

I would organize the note as follows:

1. Problem formulation and spectral-pencil characterization.
2. The dimension obstruction theorem.
3. Uniformity over transverse admissible families.
4. The published two-order-gap example.
5. The \\(n=6\\) whole-family spectral counterexample.
6. Projective occlusion as a sufficient criterion.
7. Limitations and the general \\(r\ge2,\ h\<n\\) problem.

This would make a coherent short note with a clear mathematical contribution.

# 7. Q7 — Should the Toeplitz criterion be included in the paper?

My recommendation is yes, but as an exact computational theorem supporting the spectral characterization, rather than replacing the matrix-pencil characterization.

You currently have two independent methods.

### Method A: maximal-minor gcd

For

\\[ Q\_{\mathcal L}(\lambda) = [\lambda\mathcal L-\mathcal LA;\ CA;\ C], \\]

let

\\[ h=\operatorname{normalrank}Q\_{\mathcal L}(\lambda). \\]

Then

\\[ (5b) \iff \gcd\\{\text{all }h\times h\text{ minors of }Q\_{\mathcal L}(\lambda)\\} \\]

is a nonzero constant.

This is mathematically transparent and directly identifies the finite spectral obstruction.

### Method B: the Toeplitz criterion

Your report establishes

\\[ \nu_d=\sum_j\max\\{0,d-\varepsilon_j+1\\}, \\]

and

\\[ \\#\\{j:\varepsilon_j=d\\} = \nu_d-2\nu\_{d-1}+\nu\_{d-2}. \\]

Consequently,

\\[ \boxed{ (5b)\iff \nu_s=(s+1)m-s, } \\]

where

\\[ s=\operatorname{rank}\mathcal L,\qquad m=q+2p-h. \\]

The computational advantage is significant: one constant Toeplitz matrix replaces symbolic manipulation of polynomial minors.

### My suggested presentation

Use the following hierarchy:

1. State the finite-elementary-divisor characterization as the mathematical definition of spectral feasibility.
2. Present the Toeplitz identity as an equivalent exact finite-dimensional criterion.
3. Present the maximal-minor gcd as an independent verification method.

I would not bury the Toeplitz criterion in an implementation appendix.

It is a genuine mathematical result: it converts a polynomial matrix-pencil property into a nullity computation for a constant matrix.

However, the paper should explain why the chosen truncation degree \\(s\\) is sufficient. The identity is only as useful as its proof of completeness.

I would also state the conventions for zero-dimensional or degenerate cases explicitly, even if the standing assumptions exclude most of them.



Recommendation

&#x20;Include the Toeplitz theorem in the main text, with the gcd method as an independent certificate.



# 8. Q8 — Where are the checks most likely to be systematically wrong?

This is an important question. Based on the corrected history, I see five risks, of which two are particularly serious.

## 8.1 Risk 1: incomplete parametrization of the Grassmannian

Highest priority

The history of the \\(n=7\\) example demonstrates that incomplete enumeration can produce a false nonexistence conclusion.

This is not simply a programming bug. It is a mathematical issue concerning the coverage of the parameter space.

For

\\[ \mathcal Z\in\operatorname{Gr}(d,K), \\]

an affine chart does not cover the entire Grassmannian.

If you use several charts, you must prove that their union covers every admissible subspace.

For numerical or rational-grid searches, there is a further issue: sampling a chart does not establish the absence of solutions between sampled points.

I recommend that every enumeration report contain:

- The dimension of the Grassmannian.
- The number of affine charts.
- The exact parametrization in each chart.
- The algebraic constraints defining admissibility.
- Whether the search is exhaustive or sampled.
- A proof that the resulting list is complete, if completeness is claimed.

This should become a mandatory verification protocol.

## 8.2 Risk 2: confusing normal rank with pointwise rank

For a polynomial matrix \\(Q(\lambda)\\), distinguish

\\[ h=\operatorname{normalrank}Q(\lambda) \\]

from

\\[ \operatorname{rank}Q(\lambda) \\]

at a particular value of \\(\lambda\\).

The condition (5b) is

\\[ \operatorname{rank}Q(\lambda)=h \quad\forall\lambda\in\mathbb C. \\]

The gcd criterion requires the maximal minors of size \\(h\\), not an arbitrarily chosen minor and not necessarily the largest square submatrix available.

The correct procedure is:

1. Compute the normal rank \\(h\\).
2. Generate all \\(h\times h\\) minors, or a mathematically justified generating subset.
3. Compute their gcd over the exact coefficient field.
4. Check whether the gcd is constant.

If the normal rank is smaller than expected, using the wrong minor size can produce an entirely incorrect conclusion.

This is particularly important when \\(h\<n\\).

## 8.3 Risk 3: \\(\lambda=0\\) and singular \\(A\\)

I do not think singularity of \\(A\\) is itself a fundamental difficulty.

The pencil is

\\[ Q(\lambda)=[\lambda\mathcal L-\mathcal LA;\ CA;\ C]. \\]

The value \\(\lambda=0\\) gives

\\[ Q(0)=[-\mathcal LA;\ CA;\ C]. \\]

There is no reason to exclude it.

In fact, if \\(A\\) is singular, zero may be an eigenvalue of the relevant reduced dynamics, so excluding it could hide a genuine spectral obstruction.

The gcd criterion automatically includes zero as a possible root.

The real danger is an implementation that tests only nonzero eigenvalues or divides by \\(\lambda\\).

Recommendation: explicitly include singular-\\(A\\) regression examples and verify the pencil at \\(\lambda=0\\).

## 8.4 Risk 4: the scalar-ratio construction for \\(r\ge2\\)

This is a subtle conceptual issue.

For \\(r=1\\),

\\[ \lambda(x)=\frac{L_0Ax}{L_0x} \\]

is well-defined whenever \\(L_0x\ne0\\).

For \\(r\ge2\\), however, \\(L_0x\\) and \\(L_0Ax\\) are vectors.

A scalar \\(\lambda(x)\\) exists only if

\\[ L_0Ax=\lambda(x)L_0x. \\]

The correct domain is therefore

\\[ \mathcal D= \left\\{ [x]\in\mathbb P(V): L_0x\ne0,\quad L_0Ax\in\operatorname{span}(L_0x) \right\\}. \\]

This is an algebraic proportionality condition.

The projective occlusion argument can be extended to \\(r\ge2\\) by studying the image of this restricted domain, but its dimension may be much smaller than \\(\dim\mathbb P(V)\\), or the domain may even be empty.

I would make this explicit in the next version of the report.

The quotient-pencil formulation in Q1 is more general and avoids this difficulty entirely.

## 8.5 Risk 5: exact arithmetic versus floating-point rank

All critical claims should be established over the exact field.

For rational input matrices, use rational arithmetic whenever possible.

For polynomial pencils, use exact polynomial arithmetic.

For algebraic coefficients, use a suitable exact algebraic-number representation.

Avoid relying on floating-point singular values to distinguish

\\[ \operatorname{rank}Q(\lambda)=h \\]

from

\\[ \operatorname{rank}Q(\lambda)=h-1. \\]

A small nonzero singular value is not evidence of exact rank.

# 9. A new theorem I recommend pursuing

The quotient formulation in Q1 suggests a stronger way to organize the whole-family problem.

Let

\\[ \mathscr G=\operatorname{Gr}(d,K) \\]

be the admissible Grassmannian, with any additional algebraic admissibility restrictions imposed.

Define the incidence variety

\\[ \mathscr I= \left\\{ (\mathcal Z,[x],\lambda): \begin{array}{l} \mathcal Z\in\mathscr G,\\\ [x]\in\mathbb P(V),\\\ x\notin\mathcal Z,\\\ (\lambda I-A)x\in\mathcal Z \end{array} \right\\}. \\]

Let

\\[ \mathscr B=\operatorname{pr}\_{\mathscr G}(\mathscr I). \\]

Then

\\[ \mathscr B = \\{\text{spectrally infeasible admissible subspaces}\\}. \\]

The whole-family problem is exactly

\\[ \boxed{\mathscr G\subseteq\mathscr B.} \\]

This gives three different mathematical tasks:

1. Determine whether \\(\mathscr B\\) is empty.
2. Determine whether \\(\mathscr B=\mathscr G\\).
3. Determine whether \\(\mathscr G\setminus\mathscr B\\) is nonempty.

These correspond to different questions in your project:

- Existence of a feasible augmentation.
- Whole-family spectral infeasibility.
- Existence of at least one feasible augmentation at a prescribed order.

By Chevalley's theorem, \\(\mathscr B\\) is constructible. It need not be closed, so a projective closure argument must be handled carefully.

This formulation is particularly useful because it separates the general spectral problem from the special projective occlusion construction.

## A potentially stronger approach: stratification by rank

Instead of treating all admissible \\(\mathcal Z\\) simultaneously, stratify the Grassmannian according to

\\[ \operatorname{rank} \left( J\_{\mathcal Z}|\_V \right), \\]

where

\\[ J\_{\mathcal Z}:V\to X/\mathcal Z. \\]

The rank is the dimension of the image of \\(V\\) in the quotient.

On each fixed-rank stratum, the quotient-pencil representation has a more stable dimension.

This suggests the following research programme:

- First classify the possible ranks of \\(J\_{\mathcal Z}|\_V\\).
- Then characterize the spectral obstruction on each stratum.
- Finally, determine whether any stratum can be excluded by a dimension argument.

This is a more systematic route than attempting to construct one universal bad-point map.

I would regard this as the most promising new theoretical direction in the report.

# 10. Revised research priorities

I would now revise the order of work as follows.

Priority 1 — Prove the general quotient-pencil theorem

Immediate

Establish the equivalence between spectral failure and the source–image incidence condition for arbitrary \\(h\\) and \\(r\\).

Deliverable: a theorem with a short proof using \\(Q\_{\mathcal L}(\lambda)=D(\lambda)H\\).

Priority 2 — Strengthen the dimension obstruction

Immediate

Determine when \\(V'\cap S=0\\) holds for the entire admissible family.

Deliverable: a verifiable condition on \\((A,C,L_0,q)\\) that makes the dimension obstruction uniform.

Priority 3 — Generalize projective occlusion

Replace the scalar-ratio map by the proportionality locus \\(\mathcal D\\) for \\(r\ge2\\).

Deliverable: a projective sufficient condition with explicitly stated domain and hypotheses.

Priority 4 — Stratify the Grassmannian

Classify admissible subspaces according to the rank of the quotient map.

Deliverable: a finite collection of algebraic strata and corresponding spectral criteria.

Priority 5 — Investigate complexity

After the geometric structure is clearer, investigate DEC(\\(q\\)) for fixed \\(p,r\\) and variable \\(n\\).

Deliverable: either a reduction or a polynomial-time algorithm for a meaningful restricted class.

# 11. Final assessment

I would make three decisions now.

First: the dimension obstruction should become the principal theorem of the short note. It has a clean proof and explains the published two-order-gap example.

Second: the \\(n=6\\) example should definitely be retained. Its whole-family infeasibility proof is a genuine contribution, even though its hypotheses are restrictive.

Third: the quotient-pencil formulation should become the central object of the next research phase. It resolves the main conceptual limitation of the existing occlusion argument: the need for \\(h=n\\) and a scalar-valued map constructed from \\(L_0\\).

My strongest recommendation is to prove the following statement carefully and use it as the foundation of the next report:

\\[ \boxed{ \begin{aligned} (5a)\Longrightarrow\quad (5b)\text{ fails} \iff \exists x\in V,\ \exists\lambda\in\mathbb C:\\\ x\notin\mathcal Z,\qquad (\lambda I-A)x\in\mathcal Z. \end{aligned} } \\]

It is exact, applies beyond the special examples, and directly links the original matrix-pencil condition to the geometry of admissible nullspaces.

Once this theorem is established, the research question becomes much sharper:

\\[ \boxed{ \text{Can one characterize when every admissible } \mathcal Z\in\operatorname{Gr}(d,K) \text{ belongs to the bad incidence locus?} } \\]

That, in my view, is the central unresolved mathematical problem in the current project.

The complexity question should follow from this structural understanding rather than precede it.

06_state_corrections_and_assessment.md