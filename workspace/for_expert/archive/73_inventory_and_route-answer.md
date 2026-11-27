# Research strategy and recommendations for the minimum functional observer project

My overall recommendation is to pursue Route (a) and Route (c) in parallel, while preparing Route (d) as a publishable structural contribution.

More specifically, I would organize the project around the following central question:

> What is the computational complexity of deciding whether a minimum-order functional observer exists, and what structural properties of the observer equations determine the boundary between tractability and hardness?

I would not make the rank-4 determinant construction the sole objective of the project. It is a promising route to an \\(\exists\mathbb R\\)-hardness proof, but there are several substantial obstacles between finding a quadratic determinant and obtaining a valid complexity reduction.

There is also an opportunity that I think deserves more attention: the observer problem may admit a useful hierarchy of complexity results indexed by the codimension \\(c\\), the quotient dimension, and the structure of the pair \\((A,C)\\). This could produce meaningful theorems even if the unrestricted complexity question remains unresolved.

I will distinguish three types of conclusions below:

- Established project results: facts explicitly stated in your inventory.
- Mathematical deductions: consequences or plausible extensions of those results.
- Research proposals: conjectures and experiments that still need proof.

I will use your notation and regard the retracted results as unavailable.

## 1. First, reorganize the mathematical problem

The problem is to determine whether there exists a matrix

\\[ L=\begin{bmatrix}L_0\\\R\end{bmatrix} \\]

satisfying

\\[ \operatorname{rank} \begin{bmatrix} LA\\\L\\\CA\\\C \end{bmatrix} = \operatorname{rank} \begin{bmatrix} L\\\CA\\\C \end{bmatrix}, \tag{5a} \\]

and

\\[ \operatorname{rank} \begin{bmatrix} \lambda L-LA\\\CA\\\C \end{bmatrix} = \operatorname{rank} \begin{bmatrix} L\\\CA\\\C \end{bmatrix}, \qquad \forall\lambda\in\mathbb C. \tag{5b} \\]

According to your inventory, the characterization, existence, order spectrum, per-order conditions, and minimum order have already been settled in the Fernando (2026) literature. The remaining issue is the complexity of the existential condition, denoted by \\(q1\\).

This distinction is important. The project should not attempt to re-establish the observer characterization. It should investigate the algebraic and geometric complexity of the remaining feasibility problem.

### 1.1 Separate the three sources of complexity

I suggest distinguishing three layers.

Layer I: Geometric feasibility

Can one find a row space satisfying the linear and invariant-subspace constraints imposed by (5a)?

Layer II: Spectral feasibility

Can that row space simultaneously satisfy (5b), which requires the associated pencil to have the appropriate rank for every complex \\(\lambda\\)?

Layer III: Realizability and dimension

Can the geometric and spectral conditions be realized by an actual matrix \\(L=[L_0;R]\\) with the required order and fixed rows?

This decomposition is particularly useful because the three layers may have very different computational properties.

For example, a geometric condition might reduce to a Grassmannian incidence problem, while the spectral condition might reduce to a polynomial gcd condition.

A successful hardness proof must show that the difficult algebraic computation survives all three layers.

A successful tractability proof might instead exploit a structural interaction between them.

### 1.2 Use the quotient-space formulation as the primary language

For the \\(q=2\\) case, your inventory defines

\\[ S=\operatorname{row}[L_0;CA;C], \qquad Q=(\mathbb C^n)^\*/S, \\]

and

\\[ u=[L_0A],\qquad x=[l],\qquad v=[lA]. \\]

The condition reduces to

\\[ u,v\in\operatorname{span}\\{x\\}. \\]

This is an exceptionally useful reduction.

It tells us that the complexity does not necessarily come from the number of entries of \\(L\\). It may come from the interaction between the induced action of \\(A\\) on the quotient and the geometry of the admissible subspaces.

I would therefore make quotient-space coordinates central to the next stage of the project.

In particular, I would seek a general formulation in which:

1. The fixed data determine a quotient space.
2. The variable rows determine a point on a Grassmannian.
3. The invariance constraints define an algebraic incidence variety.
4. The spectral constraints remove certain components of that variety.
5. The minimum-order question becomes a question about the smallest admissible Grassmannian stratum.

This formulation could lead to both complexity results and structural classification theorems.

## 2. My assessment of the four proposed routes

| Route                                   | Potential | Main obstacle                                        | Recommendation          |
| --------------------------------------- | --------- | ---------------------------------------------------- | ----------------------- |
| (a) Rank-4 gate and circuit composition | Very high | Constructing a sound, composable reduction           | Pursue selectively      |
| (b) Reduction from another hard problem | Very high | Preserving the observer constraints                  | Investigate in parallel |
| (c) Fixed-\\(c\\) tractability          | High      | Exploiting structure beyond naive dimension counting | Make a major priority   |
| (d) Structural paper                    | High      | Organizing results into a coherent contribution      | Begin now               |

The important point is that these routes are not mutually exclusive.

I would not wait for a complete answer to \\(q1\\) before publishing the structural results, provided the results are independently substantial and the open complexity question is stated accurately.

## 3. Route (a): Is the rank-4 determinant gate a good direction?

My assessment is that this is mathematically interesting and worth pursuing, but the project should first establish a stronger result than merely finding a rank-4 quadratic form.

The real target is:

> Construct a family of observer instances in which feasible observers correspond exactly to solutions of an arithmetic multiplication constraint, with no additional feasible observers arising from degenerate cases or normalization boundaries.

This is a much more demanding requirement.

### 3.1 Why the rank-4 condition is natural

Your current \\(q=2\\) analysis gives

\\[ u=0 \quad\Longrightarrow\quad D(l)=\det[S;l;lA]=0. \\]

You have already found an instance where \\(D\\) has rank 3.

The next step is to understand the geometry of rank-4 quadratic forms.

Consider the homogeneous quadratic polynomial

\\[ Q(x,y,z,w)=xy-zw. \\]

Its symmetric matrix has rank 4. On the affine chart \\(w=1\\), we obtain

\\[ Q(x,y,z,1)=xy-z. \\]

Consequently,

\\[ Q(x,y,z,1)=0 \quad\Longleftrightarrow\quad z=xy. \\]

This is exactly the multiplication relation needed for an arithmetic circuit.

The underlying idea is sound.

However, there are four important issues.

### 3.2 Obstacle I: Rank alone is not the complete condition over \\(\mathbb R\\)

Over \\(\mathbb C\\), nondegenerate quadratic forms of the same dimension are equivalent under an invertible linear transformation.

Over \\(\mathbb R\\), this is no longer true.

The real signature matters.

For example, the quadratic form

\\[ x_1^2+x_2^2+x_3^2+x_4^2 \\]

has rank 4, but it cannot be transformed into \\(xy-zw\\) by a real invertible linear transformation.

The latter has signature \\((2,2)\\).

Therefore, if you pursue a real-variable hardness reduction, the correct target is not merely

\\[ \operatorname{rank}D=4, \\]

but rather

\\[ \operatorname{rank}D=4, \qquad \operatorname{signature}(D)=(2,2). \\]

If the problem is genuinely formulated over complex observer matrices, rank 4 is sufficient for equivalence of nondegenerate quadratic forms, but the real-versus-complex witness issue must still be resolved separately.

Recommendation: Search directly for a rank-4 quadratic form with the required real signature, rather than first constructing an arbitrary rank-4 form.

### 3.3 Obstacle II: The normalization boundary

The most serious issue is the affine chart.

Suppose the homogeneous determinant equation is

\\[ xy-zw=0. \\]

You want to normalize \\(w=1\\), obtaining \\(z=xy\\).

But the original observer problem does not automatically impose

\\[ w\neq0. \\]

When \\(w=0\\), the equation becomes

\\[ xy=0, \\]

which admits additional solutions.

These additional solutions may correspond to feasible observers that have nothing to do with the intended arithmetic circuit.

This is not a minor technicality. It is a potential source of false positives in the reduction.

I suggest treating the projective and affine formulations separately.

Projective formulation

Study the full homogeneous variety

\\[ \mathcal V=\\{[x:y:z:w]\in\mathbb P^3:xy-zw=0\\}. \\]

Affine formulation

Study the open subset

\\[ \mathcal V\_{\mathrm{aff}} = \mathcal V\cap\\{w\neq0\\}. \\]

The reduction must show that the observer constraints either:

1. Exclude the boundary \\(w=0\\); or
2. Ensure that every boundary solution can be transformed into a valid affine solution; or
3. Make every boundary solution correspond to a legitimate source-instance solution.

The third possibility is often overlooked and may be easier than directly excluding the boundary.

There is also an important algebraic-geometric distinction here: equations defining rank conditions naturally give closed algebraic sets, whereas \\(w\neq0\\) defines an open condition. You need to understand exactly which part of (5b) can supply the necessary nonvanishing condition.

One possible mechanism is to use an auxiliary variable \\(t\\) and impose

\\[ wt=1. \\]

But you must prove that this relation itself can be represented within the observer constraints. It cannot simply be added as an independent polynomial constraint.

### 3.4 Obstacle III: The fixed row \\(L_0A\\)

This is the most important issue revealed by your retractions.

The previous determinant construction failed because it omitted the row \\(L_0A\\).

Therefore, any new construction should start from the complete condition (5a), not from a reduced determinant that happens to resemble the desired multiplication gate.

I recommend a strict construction protocol.

For each proposed instance:

1. Specify the complete matrices \\(A,C,L_0\\).
2. Compute \\(S=\operatorname{row}[L_0;CA;C]\\).
3. Verify \\(u=[L_0A]=0\\) exactly.
4. Derive the determinant polynomial \\(D(l)\\) from the full row configuration.
5. Compute its rank and signature.
6. Independently verify the equivalence with (5a).
7. Only then investigate (5b).

This ordering avoids spending time on a beautiful quadratic form that does not correspond to a valid observer instance.

### 3.5 Obstacle IV: A single multiplication gate is not an arithmetic circuit reduction

Even if you obtain

\\[ z=xy, \\]

you still need to encode arbitrary polynomial feasibility.

A standard approach is to convert an existential real formula into an arithmetic circuit with constraints

\\[ g_i=0,\qquad g_i=x_j+x_k,\quad g_i=x_jx_k,\quad g_i=c, \\]

together with the necessary inequality gadgets.

Then every multiplication gate must be implemented by an observer construction.

This raises a new issue: can multiple gates be composed without interfering with each other?

For the rank-4 construction, I would formulate a gate composition theorem.

A suitable theorem would look like this:

Suppose observer gadgets \\(G_1,\ldots,G_m\\) encode independent arithmetic constraints. There exists a polynomial-time construction of a combined observer instance such that its feasible observers correspond exactly to compatible solutions of all the individual gadgets.

This theorem must explicitly control:

- The common fixed rows.
- The induced quotient-space action.
- The interaction between variable rows.
- The spectral condition.
- Degenerate projective solutions.
- The growth of the matrix dimensions and coefficient bit-length.

Without such a composition theorem, a local multiplication gadget does not establish \\(\exists\mathbb R\\)-hardness.

### 3.6 A more efficient experimental program for the rank-4 gate

I would not search blindly over random matrices.

Instead, use the structure of the determinant to design a constrained search.

Let the quotient dimension be \\(d\\). Represent the induced action of \\(A\\) on the quotient by a matrix \\(T\\). Then, after choosing a basis for the relevant row space, the determinant polynomial has the schematic form

\\[ D(x)=\det \begin{bmatrix} B_0\\\ x\\\ xT \end{bmatrix}, \\]

where \\(B_0\\) represents the fixed quotient constraints.

Your task is to find \\(B_0,T\\) for which this polynomial has rank 4 and the desired signature.

I recommend the following sequence.

Experiment A: Dimension lower bounds

Determine the smallest possible quotient dimension \\(d\\) for which a rank-4 determinant polynomial can exist.

Do this theoretically first, then verify computationally.

Experiment B: Structural parametrization

Instead of choosing arbitrary \\(T\\), classify the possible quadratic forms generated by the map

\\[ x\longmapsto (x,xT). \\]

This may reveal a rank restriction that rules out the gate entirely in certain dimensions.

Experiment C: Exact symbolic search

Use rational matrices and symbolic determinant calculations.

For each candidate, calculate:

\\[ \operatorname{rank}D,\qquad \operatorname{signature}D,\qquad \operatorname{rank}S,\qquad u. \\]

Do not use floating-point rank calculations as proof.

Experiment D: Boundary analysis

For each successful candidate, explicitly solve the boundary equations associated with the proposed affine chart.

The desired output is not merely one example. It is a theorem identifying a class of matrices for which the gate is valid.



Recommendation

&#x20;Keep the rank-4 direction, but give it a limited research milestone: first prove existence or impossibility of a valid rank-4, signature-\\((2,2)\\) gate satisfying the full observer equations. Do not begin a large circuit reduction before this is settled.



## 4. Route (b): Reduction from existing \\(\exists\mathbb R\\)-complete problems

I think this route has the greatest potential to shorten the proof.

There are two particularly relevant developments in the 2026 literature.

### 4.1 Affine rank minimization

Majumdar's 2026 preprint, Affine Rank Minimization is ER Complete, proves that affine constraints combined with a fixed rank bound can encode arbitrary existential real computations. In particular, the result establishes \\(\exists\mathbb R\\)-completeness even for rank at most 3.

The construction uses:

- Arithmetic circuits.
- Matrix-entry variables representing circuit values.
- Affine equations for addition and other linear operations.
- Rank-forcing gadgets for multiplication.
- A fixed-rank gauge block to remove factorization ambiguity.
- A composition lemma to combine the gadgets.

See [Affine Rank Minimization is ER Complete](https://arxiv.org/abs/2602.14037?utm_source=chatgpt.com).&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



This is highly relevant to your project.

Your observer problem is also governed by structured rank constraints. However, the important question is whether its special matrix pattern can simulate the affine rank minimization construction.

I would investigate the following possible reduction:

\\[ \mathrm{ARM}(3) \longrightarrow q1. \\]

The objective would be to construct an observer instance from an affine rank minimization instance.

The central difficulty is that your variable matrix is not arbitrary. It must have the form

\\[ L=\begin{bmatrix}L_0\\\R\end{bmatrix}, \\]

and the matrices appearing in the rank conditions are coupled through multiplication by the same fixed \\(A\\).

Therefore, an arbitrary rank constraint cannot simply be substituted into (5a).

Nevertheless, the ARM paper suggests an important alternative to the rank-4 determinant route.

Instead of encoding multiplication in one determinant polynomial, encode multiplication through the interaction of several observer rows.

For example, suppose the variable rows represent vectors

\\[ r_1,\ldots,r_k. \\]

The action of \\(A\\) produces

\\[ r_1A,\ldots,r_kA. \\]

The invariance condition requires these transformed rows to belong to the appropriate span.

This creates algebraic relations between the original rows and their images.

It is conceivable that a carefully designed block structure could encode the same type of multiplication constraints as the ARM construction.

This is a research hypothesis, not an established reduction.

### 4.2 Static output feedback stabilization

An even more interesting connection is the 2026 preprint by Zhaobo Liu:

Computational complexity of static output feedback stabilization.

It proves \\(\exists\mathbb R\\)-completeness for static output feedback stabilization with rational input data, even for controllable and observable integer plants with two inputs. It also identifies an effective gain dimension and proves polynomial-time exact synthesis when that dimension is fixed.

See [Computational complexity of static output feedback stabilization](https://arxiv.org/abs/2610.00390?utm_source=chatgpt.com).&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



Why is this important?

Both problems involve finding a matrix of free parameters subject to structural constraints induced by a linear system.

However, there is a crucial distinction:

- Static output feedback asks for a gain making a closed-loop matrix stable.
- Your problem asks for an observer matrix satisfying invariance and a pencil-rank condition.

The two feasibility problems are not automatically equivalent.

I would investigate whether one can construct a transformation

\\[ (A\_{\mathrm{SOF}},B,C,K) \longmapsto (A\_{\mathrm{obs}},C\_{\mathrm{obs}},L_0,R) \\]

such that

\\[ \exists K:\ A\_{\mathrm{SOF}}+BKC \text{ is Hurwitz} \\]

if and only if

\\[ \exists L:\ (5a),(5b)\text{ hold}. \\]

There are two possible directions:

1. Encode the characteristic-polynomial constraints of static output feedback in the observer pencil.
2. Encode the observer pencil's eigenvector-exclusion condition in a closed-loop stability problem.

I would start with the first.

The observer pencil already has a parameter-dependent spectral structure, so it may be possible to represent polynomial conditions on the gain through its invariant factors or minors.

But one must preserve the exact quantifiers and the requirement that all spectral values satisfy (5b).

### 4.3 Which external problem should you try first?

My ranking is:

| Candidate                              | Relevance | Reason                                      |
| -------------------------------------- | --------- | ------------------------------------------- |
| Affine rank minimization               | Very high | Closest algebraic structure                 |
| Static output feedback                 | High      | Closest control-theoretic structure         |
| General arithmetic circuit feasibility | High      | Most flexible source problem                |
| Oriented matroid realization           | Medium    | Potential universality route                |
| Polynomial matrix completion           | Medium    | Possible connection through structured rank |

I would start with affine rank minimization because it provides an explicit circuit-encoding framework.

However, I would not assume that the existing ARM rank-3 gadget transfers directly.

The real contribution would be a theorem showing that the observer's constrained rank geometry is expressive enough to simulate the ARM gadget.

## 5. Route (c): Fixed-\\(c\\) tractability may be the most promising independent result

This is the direction I would give more attention than the current inventory seems to suggest.

The reason is the \\(q=2\\) result.

When \\(u\neq0\\), your problem becomes linear:

\\[ u,v\in\operatorname{span}\\{x\\} \quad\Longrightarrow\quad x\propto u. \\]

When \\(u=0\\), the problem becomes quadratic:

\\[ D(l)=\det[S;l;lA]=0. \\]

This is a striking dichotomy.

It suggests that the algebraic complexity may depend strongly on the number of free observer rows and on the geometry of the fixed-row quotient.

### 5.1 A possible complexity hierarchy

I propose investigating the following conjectural hierarchy.

| Regime           | Possible complexity                           | Current evidence                    |
| ---------------- | --------------------------------------------- | ----------------------------------- |
| \\(c=0\\)        | Immediate infeasibility                       | Established                         |
| \\(c=1\\)        | Structural classification                     | Partial classification established  |
| \\(c=2\\)        | Algebraic feasibility of low-degree varieties | Full structural reduction available |
| Fixed \\(c\\)    | Potentially polynomial or FPT                 | Open research direction             |
| Variable \\(c\\) | Potentially \\(\exists\mathbb R\\)-hard       | Not established                     |

Here, \\(c\\) should be defined exactly as in your existing framework, rather than silently identified with the number of free rows if those conventions differ.

The central question is:

\\[ \text{Is }q1\text{ fixed-parameter tractable in }c? \\]

A positive result might take the form

\\[ f(c)\operatorname{poly}(n,\ell), \\]

where \\(\ell\\) is the input bit-length.

A weaker but still meaningful result might be

\\[ n^{O(c)}\operatorname{poly}(\ell). \\]

The distinction matters:

- The latter is an XP algorithm.
- The former is an FPT algorithm.

### 5.2 Why a fixed number of rows could help

The free variables in \\(L\\) are row vectors.

If there are only a few such rows, the feasible row spaces may be represented using a relatively small number of Grassmannian coordinates.

For example, a one-dimensional variable row space is represented by projective coordinates.

A two-dimensional row space can be represented using Plücker coordinates subject to quadratic Grassmannian relations.

In general, a \\(k\\)-dimensional row space in a \\(d\\)-dimensional quotient is represented by

\\[ \operatorname{Gr}(k,d), \\]

with Plücker embedding into projective space.

This gives a natural algebraic-geometric formulation of the problem.

The crucial point is that the number of variables and the degree of the defining equations may be controlled by \\(c\\), even though the original matrix dimension is large.

This does not automatically yield polynomial time, but it creates an avenue for parameterized algorithms.

### 5.3 A concrete algorithmic proposal

Develop a Grassmannian-based algorithm with four stages.

Stage 1: Construct the quotient

Compute

\\[ S=\operatorname{row}[L_0;CA;C] \\]

and a basis of

\\[ Q=(\mathbb C^n)^\*/S. \\]

Stage 2: Parameterize the candidate subspaces

Represent the free row space using Plücker coordinates.

Impose the necessary Grassmannian relations.

Stage 3: Impose invariance

Translate (5a) into polynomial equations in the Plücker coordinates.

Use the induced action of \\(A\\) on the quotient rather than working with the full matrix \\(A\\) throughout.

Stage 4: Impose the spectral condition

Use your existing spectral lemma and gcd criterion to translate (5b) into algebraic conditions.

This is where the project has a particularly useful advantage: you already have a four-layer exact solver, including a spectral gcd stage.

The algorithmic work should build on that implementation rather than develop a completely separate feasibility framework.

### 5.4 A particularly interesting special case: \\(c=2\\)

I would prioritize \\(c=2\\).

You already have:

- The forced-plane row-wise criterion.
- Two test instances that are infeasible for all \\(q\\) under \\(\mathsf P\_{\mathrm{ind}}\\).
- The complete \\(q=2\\) structure.
- The distinction between the linear \\(u\neq0\\) case and the quadratic \\(u=0\\) case.

The next theorem to seek is:

Proposed Theorem A — Fixed-\\(c=2\\) algebraic classification

For every fixed instance with \\(c=2\\), the observer feasibility problem can be reduced to a finite collection of explicitly described polynomial feasibility problems of bounded degree, with the number of variables and equations controlled by the quotient dimension.

The stronger objective is to determine whether those special polynomial systems admit a polynomial-time algorithm.

I would not claim that bounded degree implies polynomial-time solvability. It does not.

The key is whether the polynomial systems have additional structure, such as:

- Bounded rank.
- Few independent quadratic forms.
- A common invariant subspace.
- A low-dimensional singular locus.
- A restricted signature or factorization pattern.

These properties may be enough to give a tractability theorem.

## 6. An overlooked direction: use algebraic geometry to classify the feasible set

This may be the most productive conceptual change.

Instead of asking only whether a feasible observer exists, investigate the geometry of the entire feasible set.

Define

\\[ \mathcal F= \\{R:(5a),(5b)\text{ hold for }L=[L_0;R]\\}. \\]

The geometry of \\(\mathcal F\\) could reveal much more than a yes/no decision.

I suggest studying five properties.

### 6.1 Dimension

Determine the dimension of the algebraic family of feasible observers.

Your 10-dimensional family already demonstrates why dimension arguments must be handled carefully.

A useful theorem would bound the dimension of \\(\mathcal F\\) in terms of the quotient dimension and the invariant-subspace structure.

### 6.2 Irreducible components

Is the feasible set irreducible?

Can it have multiple components corresponding to different invariant subspaces?

Can the components be classified by the spectral structure of \\(A\\)?

This could explain why naive determinant gates fail: the intended multiplication component might coexist with unintended components.

### 6.3 Singular locus

The singular locus is particularly important.

For a quadratic determinant gate, the singular points often correspond to degenerate configurations or chart-boundary phenomena.

A theorem describing the singular locus could help establish when the normalization is legitimate.

### 6.4 Generic versus exceptional instances

Your closedness/generic-gcd machinery suggests studying the generic behavior of the bad spectral locus.

A possible theorem is:

For a Zariski-open set of fixed data satisfying a specified structural condition, the spectral admissibility condition has a generic algebraic characterization.

This would be valuable even without a complete complexity classification.

### 6.5 Universality and realization spaces

There is a more ambitious possibility.

The existential theory of the reals is deeply connected with universality phenomena in algebraic geometry and combinatorial geometry.

For example, the survey by Schaefer, Cardinal, and Miltzow discusses the connection between \\(\exists\mathbb R\\), oriented matroid realization spaces, and algebraic feasibility.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://link.springer.com\&sz=32)

Springer Nature Link



Could the feasible observer spaces realize sufficiently general algebraic varieties?

If so, a universality theorem might establish hardness without explicitly constructing a separate multiplication gate for every arithmetic operation.

This would be a major result, but it is considerably more ambitious than the current project.

## 7. Descriptive complexity: what can be said beyond \\(\exists\mathbb R\\)?

This is another direction worth pursuing.

Your inventory establishes the upper bound

\\[ \mathrm{DEC}(q)\in\exists\mathbb R. \\]

But membership is only the first step.

I would investigate the following possibilities.

### 7.1 Is the problem in NP?

One should be careful here.

The fact that the observer matrices are finite-dimensional does not mean that a feasible observer has a polynomial-size rational representation.

A real algebraic system can have solutions that require algebraic numbers of large degree or large bit complexity.

Therefore, a rational-witness theorem would be extremely useful.

One possible result would be:

Proposed Theorem B — Rational witness property

For every feasible rational observer instance, there exists a feasible observer whose free entries are rational numbers with polynomially bounded encoding length.

If true, this would establish membership in NP.

However, I consider this conjecture uncertain and potentially false.

A more realistic target might be a bounded algebraic-degree witness theorem.

For example, prove that the degree of the required algebraic extension is bounded by a function of \\(c\\).

This could yield a more refined complexity upper bound.

### 7.2 Could the problem be complete for a smaller class?

I would not assume that the full \\(\exists\mathbb R\\) complexity is necessary.

The observer conditions have strong algebraic restrictions:

- The matrix \\(A\\) is fixed.
- The variable matrix appears linearly.
- The invariance condition is a row-space inclusion.
- The spectral condition comes from a structured pencil.
- The spectral variable is universally quantified but can be eliminated through a finite algebraic criterion.

This structure may place the problem in a smaller subclass of real algebraic feasibility.

Possible directions include:

- Special cases of rank-constrained feasibility.
- Restricted determinantal varieties.
- Polynomial feasibility with bounded degree and low-dimensional variable spaces.
- Real algebraic problems with a restricted incidence structure.

I would avoid claiming membership in \\(\mathrm{NP}\cap\exists\mathbb R\\) without an explicit certificate argument.

### 7.3 A useful distinction: decision versus synthesis

Separate the following problems:

\\[ \mathrm{DEC}: \quad \exists L\text{ satisfying (5a),(5b)}? \\]

\\[ \mathrm{SYNTH}: \quad \text{Construct such an }L\text{ if one exists.} \\]

These need not have the same computational complexity.

A polynomial-time decision algorithm might exist even when producing an explicit observer is harder.

Conversely, a rational-witness theorem could make synthesis easier in special cases.

This distinction is particularly important when comparing the project with the static output feedback literature.

## 8. Real versus complex: an issue that should be settled early

Your inventory explicitly formulates the spectral condition for all \\(\lambda\in\mathbb C\\). But that does not, by itself, specify whether the unknown observer matrix \\(L\\) is real or complex.

This distinction matters for the complexity classification.

There are at least three different decision problems:

\\[ \begin{aligned} P\_{\mathbb R}:&\quad \exists L\in\mathbb R^{p\times n} \text{ satisfying (5a),(5b)},\\\ P\_{\mathbb C}:&\quad \exists L\in\mathbb C^{p\times n} \text{ satisfying (5a),(5b)},\\\ P\_{\mathbb R,\mathbb C}:&\quad \exists L\in\mathbb R^{p\times n}, \quad\forall\lambda\in\mathbb C:\ (5b). \end{aligned} \\]

The third formulation is often the natural one for real-valued dynamical systems.

It should not be confused with complex-valued observer synthesis.

### 8.1 Why the distinction matters

Consider the elementary equation

\\[ x^2+1=0. \\]

It has no real solution but has complex solutions.

Thus, a reduction that works over complex variables does not automatically establish hardness for the real problem.

Conversely, if the unknown observer entries are real and the spectral parameter is complex, the spectral condition can still be expressed through real polynomial constraints.

For a polynomial pencil, rank failure can be described by vanishing minors. A complex minor vanishes precisely when both its real and imaginary parts vanish.

The nonvanishing condition can be represented by

\\[ (\operatorname{Re}f)^2+ (\operatorname{Im}f)^2>0. \\]

This gives a route to an existential real formulation, once the spectral quantifier has been eliminated correctly.

### 8.2 My proposed research question

Determine whether the two problems have identical feasibility:

\\[ P\_{\mathbb R}=P\_{\mathbb C} \\]

under any natural assumptions on \\(A,C,L_0\\).

I would not expect this to hold in complete generality.

But perhaps it holds under conditions such as:

- Real controllability or observability assumptions.
- A suitable conjugation-invariant construction.
- A real structure on the quotient-space action.
- Additional restrictions on the invariant subspaces.

A theorem establishing equality in an important subclass would be useful.

Even a counterexample would be informative because it would identify exactly which complexity problem should be studied.

Recommendation: Fix the computational model in the paper before attempting any hardness reduction. Specify the input field, coefficient encoding, unknown field, and interpretation of \\(\lambda\\).

## 9. The \\(\mathsf P\_{\mathrm{ind}}\\) versus \\(\mathsf P\_{\mathrm{full}}\\) distinction

I would elevate this from a technical convention to an explicit research question.

Your inventory indicates that two test instances are infeasible for all \\(q\\) under \\(\mathsf P\_{\mathrm{ind}}\\).

However, the project should establish exactly what changes under \\(\mathsf P\_{\mathrm{full}}\\).

I suggest constructing a comparison theorem.

Proposed Theorem C — Independence versus full admissibility

Identify necessary and sufficient conditions under which feasibility under \\(\mathsf P\_{\mathrm{ind}}\\) implies feasibility under \\(\mathsf P\_{\mathrm{full}}\\).

The proof should investigate:

1. Whether independent row choices can always be completed to a full admissible row space.
2. Whether spectral admissibility is preserved under such completion.
3. Whether the completion can introduce new invariant subspaces.
4. Whether the two conventions have different minimum feasible orders.

A useful experiment would be to generate small rational instances and compute both feasibility notions exactly.

If they differ, determine the smallest dimensions in which the difference occurs.

This might expose an entirely new structural obstruction.

## 10. Numerical and symbolic experimentation: how I would organize the computational work

Your four-layer exact solver is a valuable asset. I would turn it into a research instrument rather than treating it merely as a verification program.

I suggest creating a systematic experiment database.

### 10.1 What to record for each instance

| Quantity                                | Purpose                         |
| --------------------------------------- | ------------------------------- |
| \\(n\\)                                 | Original state dimension        |
| \\(c\\)                                 | Structural parameter            |
| \\(\dim Q\\)                            | Quotient dimension              |
| \\(\operatorname{rank}S\\)              | Fixed-row geometry              |
| \\(\operatorname{rank}D\\)              | Quadratic determinant structure |
| Signature of \\(D\\)                    | Real gate feasibility           |
| \\(\dim\mathcal F\\)                    | Feasible-set geometry           |
| Number of components                    | Possible unwanted branches      |
| Spectral gcd degree                     | Pencil obstruction              |
| Minimum feasible \\(q\\)                | Order behavior                  |
| \\(\mathsf P\_{\mathrm{ind}}\\) status  | Convention comparison           |
| \\(\mathsf P\_{\mathrm{full}}\\) status | Convention comparison           |

This allows you to search for structural patterns rather than isolated counterexamples.

### 10.2 Three kinds of experiments

Experiment 1: Exhaustive low-dimensional classification

Enumerate small integer matrices \\(A,C,L_0\\), modulo obvious equivalences where possible.

Classify all feasible cases for small \\(n\\) and \\(c\\).

The goal is to identify patterns that suggest theorems.

Experiment 2: Adversarial construction

Do not merely search for examples supporting your conjectures.

Try systematically to break them.

In particular:

- Search for feasible observers violating proposed rigidity extensions.
- Search for boundary witnesses of proposed determinant gates.
- Search for instances where generic spectral admissibility differs from exact admissibility.
- Search for counterexamples to no-drop conjectures.

Your seed 10 experience shows why this is important.

Experiment 3: Symbolic verification

For every claimed example, generate an exact certificate.

For a candidate \\(L\\), this should include:

- Exact rank verification for (5a).
- A symbolic polynomial or invariant-factor certificate for (5b).
- Exact values of the relevant determinants.
- Verification of the quotient-space conditions.

A numerical solver can discover examples, but the final mathematical evidence should be exact.

### 10.3 A particularly valuable experiment

I would run a targeted search for the smallest instance satisfying all of:

\\[ u=0, \\]

\\[ \operatorname{rank}D=4, \\]

\\[ \operatorname{signature}D=(2,2), \\]

and a nontrivial spectral condition.

Then classify every projective solution of the determinant equation into:

1. Intended affine solutions.
2. Boundary solutions.
3. Degenerate solutions.
4. Spectrally inadmissible solutions.

If no such instance exists up to a carefully chosen dimension, try to prove a structural impossibility theorem instead of continuing random searches.

That would be an efficient way to decide whether Route (a) deserves further investment.

## 11. My recommendation on the paper

I would start preparing a structural paper now.

I would not wait for the \\(\exists\mathbb R\\)-hardness question to be settled.

The reason is that the current project already contains several different types of mathematical contributions:

1. Low-\\(c\\) structural classification.
2. Rigidity and infeasibility results.
3. A direct \\(\exists\mathbb R\\) upper bound.
4. A uniform spectral lemma.
5. Exact quotient-space characterizations.
6. Counterexamples correcting earlier conjectures.
7. An exact computational framework.

These results can form a coherent paper if the central theme is chosen correctly.

### 11.1 Suggested paper title

Algebraic Structure and Computational Complexity of Minimum-Order Functional Observer Synthesis

An alternative, more conservative title:

Structural Characterization and Algebraic Feasibility of Functional Observer Design

I prefer the first if the complexity upper bound is one of the main contributions.

### 11.2 Proposed paper organization

Section 1. Introduction

Explain the functional observer synthesis problem and distinguish the already-solved characterization problem from the remaining complexity question.

State the precise decision problem.

Section 2. Preliminaries and problem formulation

Introduce:

- The fixed data \\(A,C,L_0\\).
- The variable observer matrix.
- The rank conditions.
- The order parameter.
- The relevant quotient-space notation.
- The real or complex computational model.

Section 3. Algebraic characterization

Present the row-space inclusion and the spectral pencil characterization.

Explain the relationship between the two conditions.

Section 4. Low-codimension classification

Present the \\(c=0,1,2\\) results.

This should be one of the central mathematical sections.

Section 5. Rigidity and structural obstructions

Include:

- The global rigidity result.
- The precise local rigidity result.
- The counterexample to the stronger local claim.
- The no-drop conjecture, clearly labeled as open.

Section 6. Spectral structure

Present the shift-filtration lemma, constant minor, and spectral gcd machinery.

Section 7. Computational complexity

Give the \\(\exists\mathbb R\\) upper bound.

Then explain the remaining hardness question and why the obvious determinant constructions do not yet prove it.

Section 8. Exact computational methods

Describe the four-layer solver and its verification methodology.

Section 9. Open problems

Include:

- \\(\exists\mathbb R\\)-hardness.
- Fixed-\\(c\\) tractability.
- The rank-4 gate.
- Real versus complex feasibility.
- The two admissibility conventions.

### 11.3 What I would not include

I would avoid presenting retracted constructions as partial results.

In particular:

- Do not use the old \\(\omega=2,q=3\\) impossibility statement.
- Do not use the reduced determinant gate.
- Do not use the old boundary witness.
- Do not claim that the no-drop obstruction has been disproved.

The paper should contain a short, precise discussion of these corrections only if they are necessary to clarify the current mathematical status.

A clean paper is more convincing than a paper that attempts to preserve every historical development.

# 12. A concrete research roadmap

Here is how I would allocate the next research period.

## Research roadmap

Suggested sequence: 12 weeks, with parallel work where possible

1. Weeks 1–2: Formalize the problem
   - Fix the real/complex model.
   - Formalize \\(q1\\) and its input encoding.
   - Prove or verify the direct \\(\exists\mathbb R\\) upper-bound formulation.
   - Clarify \\(\mathsf P\_{\mathrm{ind}}\\) versus \\(\mathsf P\_{\mathrm{full}}\\).
   Deliverable: A rigorous problem statement and a reusable algebraic formulation.
2. Weeks 3–4: Investigate the rank-4 gate
   - Derive the general quadratic-form representation.
   - Find the minimum possible quotient dimension.
   - Search for rank-4 forms with the required signature.
   - Analyze all projective boundary cases.
   Deliverable: A rank-4 existence theorem or an impossibility theorem.
3. Weeks 5–6: Study alternative hardness reductions
   - Analyze the ARM(3) reduction.
   - Identify the observer analogue of its gauge block.
   - Investigate whether the fixed \\(A\\) action can encode multiplication.
   - Examine the static output feedback construction.
   Deliverable: A concrete candidate reduction or a rigorous obstruction.
4. Weeks 7–8: Fixed-\\(c\\) classification
   - Develop the Grassmannian formulation.
   - Analyze \\(c=2\\) in detail.
   - Determine whether the spectral condition admits a bounded-variable representation.
   - Search for FPT or XP algorithms.
   Deliverable: A new structural theorem or algorithmic result.
5. Weeks 9–10: Exact experiments and counterexamples
   - Expand the instance database.
   - Verify all conjectures against adversarial examples.
   - Investigate feasible-set dimensions and components.
   - Compare the two admissibility conventions.
   Deliverable: A collection of exact certificates and refined conjectures.
6. Weeks 11–12: Consolidate the paper
   - Write the structural results.
   - Include the \\(\exists\mathbb R\\) upper bound.
   - State the hardness question precisely.
   - Present the strongest new result from the preceding investigations.
   Deliverable: A complete structural manuscript.

I would not insist on completing every task in this order. If a promising reduction emerges during weeks 3–4, it should receive priority. The roadmap is intended to prevent the entire project from becoming dependent on a single difficult construction.

# 13. References and literature worth incorporating

I would divide the bibliography into four groups. The first two are especially important for the complexity question.

## 13.1 Existential theory of the reals

1\. Schaefer, M., Cardinal, J., and Miltzow, T. (2026).

The Existential Theory of the Reals as a Complexity Class: A Compendium.

Springer, Bolyai Society Mathematical Studies, pp. 167–313.

[Publisher's reference and abstract](https://link.springer.com/chapter/10.1007/978-3-032-10503-5_5?utm_source=chatgpt.com).

Why read it:

- Understand the relationship between NP and \\(\exists\mathbb R\\).
- Study universality-based hardness reductions.
- Identify relevant algebraic and geometric feasibility problems.
- Learn how to formulate rigorous polynomial-time reductions.

2\. Canny, J. (1988).

Some Algebraic and Geometric Computations in PSPACE.

University of California, Berkeley.

[Technical report](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1988/6041.html?utm_source=chatgpt.com).

Relevant to the general complexity of real algebraic feasibility.

## 13.2 Rank minimization and arithmetic circuit reductions

3\. Majumdar, A. (2026).

Affine Rank Minimization is ER Complete.

arXiv:2602.14037.

[Read the paper](https://arxiv.org/abs/2602.14037?utm_source=chatgpt.com).

Highest priority

I would study this paper carefully, especially its:

- Arithmetic circuit normal form.
- Rank-forcing multiplication gadgets.
- Gauge-fixing construction.
- Gadget composition theorem.
- Exact soundness and completeness arguments.

It is probably the closest existing complexity-theoretic framework to your observer problem.

4\. Minimum Rank 3 of Graphs is Complete for the Existential Theory of the Reals.

Related research and technical background:

[Berkeley technical report](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2023/EECS-2023-265.pdf?utm_source=chatgpt.com).

Useful for understanding how low-rank geometry can encode real algebraic feasibility.

## 13.3 Computational complexity in control theory

5\. Liu, Z. (2026).

Computational Complexity of Static Output Feedback Stabilization.

arXiv:2610.00390.

[Read the paper](https://arxiv.org/abs/2610.00390?utm_source=chatgpt.com).

Highest priority

Pay particular attention to the effective gain dimension and its fixed-parameter consequences.

The effective gain dimension in this paper is an especially interesting analogue for your proposed fixed-\\(c\\) research.

6\. Ahmadi, A. A., Chaudhry, A., Narang, I., and Tang, Y. (2026).

Complexity of Output Feedback Stabilization.

arXiv:2609.20636.

[Read the paper](https://arxiv.org/abs/2609.20636?utm_source=chatgpt.com).

This work establishes NP-hardness of output feedback stabilization under its specified problem formulation.

It is worth studying as an alternative source of control-theoretic hardness constructions.

7\. Löfberg, J. (2026).

Static Output-Feedback Stabilization is NP-hard.

[Search for the preprint](https://arxiv.org/abs/2609.18844?utm_source=chatgpt.com).

The connection is relevant, but distinguish unrestricted output feedback stabilization from the particular static gain formulation in Liu's paper.

Bibliographic caution: These 2026 complexity results are recent preprints or research reports. Their proofs, assumptions, and publication status should be checked before relying on them as established peer-reviewed results.

## 13.4 Your existing observer literature

The two Fernando (2026) papers identified in your research materials should remain the starting point for the observer-specific theory.

- [Fernando (2026), first paper](https://arxiv.org/abs/2609.33615?utm_source=chatgpt.com).
- [Fernando (2026), second paper](https://arxiv.org/abs/2609.37992?utm_source=chatgpt.com).

These should be cited for the characterization, existence, order spectrum, per-order conditions, and minimum-order results, rather than attempting to reproduce those contributions as new results.

# 14. My current judgement: What is the most likely answer to \\(q1\\)?

This is necessarily a research conjecture, not a theorem.

I would rank the possibilities as follows.

My working hypothesis

# Intermediate / parameterized

I consider it plausible that the problem has a nontrivial complexity hierarchy, with substantially better algorithms for fixed structural parameters and potentially high complexity when those parameters grow.

Why I favor this hypothesis

1. The \\(q=2\\) analysis exhibits a strong linear-versus-quadratic dichotomy.
2. The fixed-row constraints restrict the possible algebraic varieties.
3. The spectral condition introduces additional structure not present in arbitrary polynomial feasibility.
4. The existing rigidity results indicate that certain large families of instances are structurally impossible.
5. The existence of a direct \\(\exists\mathbb R\\) encoding does not establish that the upper bound is tight.

However, I would not rule out \\(\exists\mathbb R\\)-completeness.

In fact, the ARM(3) result makes hardness more plausible than it might initially appear: very restricted rank geometry can already encode arbitrary real algebraic computations.

The decisive issue is whether your particular observer-induced rank geometry is sufficiently expressive.

There are three scenarios worth distinguishing.

### Scenario A: \\(\exists\mathbb R\\)-complete

A successful multiplication gadget and composition theorem establish hardness.

This would give the cleanest unrestricted complexity classification:

\\[ q1\in\exists\mathbb R \quad\text{and}\quad q1\text{ is }\exists\mathbb R\text{-hard}. \\]

### Scenario B: Fixed-parameter tractable, but hard in general

One obtains an algorithm

\\[ f(c)\operatorname{poly}(N) \\]

for fixed structural parameter \\(c\\), while the unrestricted problem is NP-hard or \\(\exists\mathbb R\\)-hard.

This is, in my opinion, the most interesting possible outcome from the perspective of combining control theory and parameterized complexity.

### Scenario C: A smaller algebraic complexity class

The special structure of the observer equations might permit polynomial-time feasibility testing, or an algorithm substantially better than general real quantifier elimination.

This possibility should not be dismissed simply because the direct formulation belongs to \\(\exists\mathbb R\\).

# 15. The single experiment that I think is most valuable

If I could choose only one experiment for the next stage, it would be:

Determine the expressive power of the \\(u=0\\) quadratic determinant family under the full observer constraints.

More concretely, investigate the family

\\[ \mathcal D= \left\\{ D(x)=\det[S;x;xA]: \begin{array}{l} \text{valid rational }A,S,\\\ [L_0A]\in S,\\\ \text{all full observer constraints respected} \end{array} \right\\}. \\]

Determine whether \\(\mathcal D\\) can contain a quadratic form equivalent to

\\[ xy-zw. \\]

But do not stop there.

For every successful form, determine the complete set of feasible observers, including the projective boundary and the spectral admissibility condition.

There are two possible outcomes.

Outcome 1: A valid rank-4 gate exists.

Then proceed immediately to the arithmetic circuit composition problem.

Outcome 2: A structural theorem rules out the gate.

Then you have eliminated an entire family of hardness constructions and can redirect effort toward affine rank minimization, Grassmannian geometry, and fixed-\\(c\\) algorithms.

This is much more valuable than accumulating additional numerical examples.

# 16. Five concrete mathematical conjectures I would add to the project

I would maintain a separate conjecture list and assign each conjecture a status: open, supported experimentally, disproved, or proved.

| No. | Conjecture                                                                                                  | Importance               |
| --- | ----------------------------------------------------------------------------------------------------------- | ------------------------ |
| C1  | A valid rank-4 signature-\\((2,2)\\) determinant gate exists under the full observer constraints.           | Hardness                 |
| C2  | For fixed \\(c\\), the feasible observer geometry admits a bounded-complexity algebraic description.        | Parameterized complexity |
| C3  | The no-drop obstruction holds under explicitly stated additional hypotheses.                                | Structural theory        |
| C4  | The spectral admissibility condition can be expressed through a finite family of quotient-space invariants. | Algorithms               |
| C5  | There are structural conditions under which real and complex observer feasibility coincide.                 | Complexity model         |

One important refinement: C2 should not be confused with FPT. A bounded-degree algebraic description does not automatically imply an efficient decision algorithm. The actual goal is to identify a tractable algebraic subclass.

I would also retain the distinction between global rigidity and the weaker local statement. Your inventory correctly identifies that the local version only yields \\(A(V)\subseteq V\\), and seed 10 prevents extending it to the stronger claim without additional assumptions.&#x20;

73_inventory_and_route.md



# 17. Final recommendations: Where I would invest research effort

Here is my preferred allocation.

## Research priority allocation

Fixed-c structural theory and algorithms

30%

Independent theorem potential and a natural route to a complexity hierarchy.

Rank-4 gate and its impossibility theory

25%

A decisive test of the most direct hardness strategy.

Affine rank minimization reduction

20%

The closest known source of real-algebraic hardness.

Exact algebraic experiments

15%

Find counterexamples, discover invariants, and certify conjectures.

Structural paper preparation

10%

Preserve and consolidate the results already established.

Suggested allocation of research effort, not measured probabilities of success.

My strongest recommendation is to stop treating the rank-4 gate as the only possible route to hardness.

The project has reached a stage where there are at least three potentially independent contributions:

1. A structural theory of minimum functional observer feasibility.
2. An algorithmic theory for fixed structural parameters.
3. A computational complexity classification for unrestricted observer synthesis.

These should reinforce each other, but none should be held hostage by the success of another.

If I were directing this research project, my immediate next objective would be the following theorem:

> Characterize the quadratic forms realizable as \\(D(l)=\det[S;l;lA]\\) under \\(u=0\\) and the complete observer constraints, including their possible ranks, signatures, and projective boundary structure.

This is the most direct bridge between your existing mathematical results and the unresolved complexity question.

It also has an attractive feature: either outcome is publishable mathematics if the characterization is sufficiently strong.

A positive result gives a route to arithmetic circuit reductions. A negative result identifies a genuine structural limitation of functional observer synthesis and tells us which hardness approaches cannot work.

I would pursue this theorem first, while simultaneously preparing the structural manuscript. That gives the project a concrete mathematical target without sacrificing the results already obtained.

The overarching research goal should be to discover whether functional observer synthesis is merely an instance of general real algebraic feasibility, or whether the special geometry of invariant row spaces and spectral pencils creates a fundamentally different computational theory.

That is a more interesting question than simply proving another upper or lower complexity bound.