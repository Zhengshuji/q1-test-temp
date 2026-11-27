# Research assessment: The new no-go theorem changes the direction of the project

I have treated your new report, The single-row multiplication gate is closed for \\(q=2\\); four 2026 hardness papers and the next route, as the primary basis for this assessment.

My main conclusion is that the project should now move away from the single-row determinant-gate architecture and toward two parallel directions: coupled-row hardness constructions and fixed-parameter tractability.

This is a meaningful change from my previous recommendation.

Your new result is stronger than merely finding that one particular rank-4 construction fails. According to the report, you have established that:

1. For \\(q=2\\), the \\(u\neq0\\) case is linear.
2. The \\(u=0\\) case produces a genuine rank-4, signature-\\((2,2)\\) determinant gate when \\(n=7\\).
3. Nevertheless, that gate necessarily fails (5b) when \\(\omega=2\\).
4. The cases \\(\omega\leq1\\) are trivial.
5. Increasing to \\(q=3\\) can restore spectral admissibility, but the additional free row absorbs the intended multiplication constraint.

Thus, the obstruction is not simply that you have not found the right quadratic form. You have found the right quadratic form, but the observer's spectral condition destroys the construction.

This is a much more informative negative result.

74_gate_no_go_and_literature.md

## 1. What the new result tells us

I would distinguish three conclusions.

First: abandon the isolated single-row gate as the main hardness strategy.

The \\(q=2\\) no-go result rules out the architecture in which one free row independently generates the multiplication relation.

Second: do not abandon determinant-based constructions altogether.

The \\(q=3\\) example suggests that additional rows can restore spectral feasibility. The remaining difficulty is controlling the interaction between rows.

This points toward a different architecture: multiplication should be encoded through a coupling between rows, rather than through an isolated quadratic equation.

Third: the most promising alternative may be to encode arithmetic in the pencil's characteristic or invariant-factor structure.

This is where the Liu paper becomes especially relevant.

# 2. Detailed assessment of the four papers

I checked the four arXiv papers, including their mathematical constructions and not just their abstracts. They are all relevant, but their usefulness is quite different.

## Priority ranking for this project

1\. Liu — 2610.00390

Highest priority

Effective gain dimension, \\(\exists\mathbb R\\)-completeness, fixed-dimensional exact algorithms.

2\. Löfberg — 2609.16886

High priority

Anchor variables, boundedness, exclusion of spurious witnesses, frequency separation.

3\. Barkai–Shames — 2609.38728

Methodological value

Bounded-gain construction, robust margins, local root-count arguments.

4\. Ahmadi–Chaudhry–Narang–Tang — 2609.20636

Supporting reference

Strong NP-hardness and representation-size obstructions.

## 2.1 Liu: Computational complexity of static output feedback stabilization

[arXiv:2610.00390 — Zhaobo Liu (2026)](https://arxiv.org/html/2610.00390?utm_source=chatgpt.com).

This is the most important of the four papers for your project.

I would recommend studying it in its entirety, particularly Sections 2.3, 3.1, 4.1, and 5.1.

### A. The effective gain dimension

Liu considers the static output feedback problem

\\[ A\_{\mathrm{cl}}=A+BKC \\]

and observes that the number of entries in \\(K\\) can substantially overestimate the number of parameters that actually affect the characteristic polynomial.

He defines

\\[ p_K(s)=\det(sI-A-BKC) \\]

and introduces

\\[ \mathcal N\_{\mathrm{pole}} = \\{D:p\_{K+tD}(s)=p_K(s) \text{ for all }K,t\\}. \\]

This is the subspace of gain directions that never affect the characteristic polynomial.

The effective gain dimension is

\\[ \boxed{ \kappa=mp-\dim\mathcal N\_{\mathrm{pole}}. } \\]

The significance is that the original gain matrix can be replaced by only \\(\kappa\\) independent parameters without changing the attainable characteristic polynomials.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



Liu then establishes:

\\[ T\_{\mathrm{alg}} \leq (\mathcal L+1)^c(n+1)^{c(\kappa+1)} \\]

for an absolute constant \\(c\\).

For fixed \\(\kappa\\), exact decision and rational synthesis are polynomial-time.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



This is a particularly important observation for your project.

### B. The observer analogue of effective gain dimension

I think we can develop a precise analogue using your existing quotient-space formulation.

Recall

\\[ K_0=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \\]

and let \\(N\\) be a basis matrix for \\(K_0\\).

Define the compressed matrices

\\[ H=LN,\qquad H_A=LAN. \\]

For fixed \\(L_0\\), the variable part \\(R\\) influences the observer feasibility conditions through

\\[ RN,\qquad RAN. \\]

This suggests the following definition.

Definition (effective observer parameter dimension).

Let \\(r\\) denote the number of free rows in \\(R\\). Define

\\[ \mathcal T:\mathbb F^{r\times n} \longrightarrow \mathbb F^{r\times 2\omega} \\]

by

\\[ \mathcal T(\Delta R) = \left(\Delta RN,\Delta RAN\right), \\]

where \\(\omega=\dim K_0\\) and \\(\mathbb F\\) is the relevant coefficient field.

Define the redundant observer directions by

\\[ \boxed{ \mathcal N\_{\mathrm{obs}} = \\{\Delta R:\Delta RN=0,\ \Delta RAN=0\\}. } \\]

Then define

\\[ \boxed{ \kappa\_{\mathrm{obs}} = \operatorname{codim}\mathcal N\_{\mathrm{obs}}. } \\]

Because the map is row-wise linear, this has the explicit formula

\\[ \boxed{ \kappa\_{\mathrm{obs}} = r\\,\operatorname{rank}[N,\ AN]. } \tag{1} \\]

This is an exact dimension count for the compressed pair \\((H,H_A)\\).

The important point is that the observer rank conditions can be expressed using this pair:

\\[ (5a) \iff \operatorname{rank} \begin{bmatrix} H_A\\\H \end{bmatrix} = \operatorname{rank}H, \\]

and

\\[ (5b) \iff \operatorname{rank}(\lambda H-H_A) = \operatorname{rank}H \quad\forall\lambda\in\mathbb C. \\]

The fixed rows of \\(L\\) contribute fixed parts of \\(H,H_A\\); the free rows contribute only through \\(\mathcal T(R)\\).

Consequently, two matrices \\(R_1,R_2\\) satisfying

\\[ R_1N=R_2N,\qquad R_1AN=R_2AN \\]

are indistinguishable to these two feasibility tests.

This gives us a concrete analogue of Liu's pole-invariant gain directions.

An important qualification: \\(\kappa\_{\mathrm{obs}}\\) is the dimension of the compressed data, not necessarily the smallest possible dimension after exploiting further symmetries of the rank predicates. It is a rigorous starting parameter, not necessarily the final optimal one.

### C. Why this is potentially a major result

Consider the following possible theorem.

Proposed Theorem 1 — Effective observer dimension reduction

For rational input data, the decision problem \\(q1\\) admits an exact reduction to a real algebraic feasibility problem involving at most \\(\kappa\_{\mathrm{obs}}\\) independent real parameters, with polynomially bounded input encoding and a polynomial-size description of the resulting constraints.

If the algebraic description can be made sufficiently explicit, fixed \\(\kappa\_{\mathrm{obs}}\\) may imply polynomial-time decision.

The natural route is:

1. Compute a rational basis \\(N\\) of \\(K_0\\).
2. Compute a basis of the image of \\(\mathcal T\\).
3. Parameterize \\(H,H_A\\) using \\(\kappa\_{\mathrm{obs}}\\) variables.
4. Express (5a) through determinantal equations.
5. Express (5b) through a polynomial gcd or Bezout certificate.
6. Apply fixed-dimensional real algebraic algorithms.

There is an important complexity-theoretic nuance.

Liu's bound is of the form

\\[ \mathcal L^{O(1)}n^{O(\kappa+1)}. \\]

This is polynomial for each fixed \\(\kappa\\), but as a parameterized bound it is an XP-type bound, not automatically an FPT bound of the form

\\[ f(\kappa)\mathcal L^{O(1)}. \\]

I would preserve this distinction in your paper.

### D. A new issue: fixed \\(c\\) versus fixed \\(\kappa\_{\mathrm{obs}}\\)

This deserves particular attention.

Even if your structural parameter \\(c\\) is fixed, it does not automatically follow that

\\[ \kappa\_{\mathrm{obs}} = r\operatorname{rank}[N,AN] \\]

is fixed.

One factor may remain large.

Therefore, I would investigate the relationship

\\[ c \longrightarrow r,\quad \operatorname{rank}[N,AN], \quad \kappa\_{\mathrm{obs}}. \\]

Possible outcomes:

- Fixed \\(c\\) bounds \\(\kappa\_{\mathrm{obs}}\\): a strong algorithmic consequence.
- Fixed \\(c\\) does not bound it, but some additional invariant does: a refined parameterized theory.
- Fixed \\(c\\) and fixed \\(\kappa\_{\mathrm{obs}}\\) are independent: two separate tractability regimes.

This is a much more precise research question than simply asking whether fixed \\(c\\) is tractable.

### E. The coefficient-encoding construction

There is another important contribution in Liu's paper.

The paper uses the identity

\\[ \det \begin{pmatrix} s^q+a&b\\\ -1&s^q-a \end{pmatrix} = s^{2q}+b-a^2 \\]

to encode polynomial residuals into characteristic-polynomial coefficients.

For affine forms \\(\ell_j,h_j\\), the construction creates expressions of the form

\\[ \ell_j(v)^2-h_j(v). \\]

These residuals are placed into distinct polynomial coefficients, and auxiliary variables cancel cross terms.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



This is relevant to your project because it provides a different philosophy of encoding.

Instead of trying to make one determinant equal \\(xy-z\\), you could try to encode a collection of polynomial residuals in the coefficients of the observer pencil's determinantal minors.

However, there is a significant obstacle.

Your spectral condition is not a Hurwitz condition. It is

\\[ \gcd\\{\text{maximal minors of }P(\lambda)\\}=1. \\]

That is, it requires the maximal minors to have no common complex root.

The condition is therefore about coprimality, not about the signs of polynomial coefficients or the location of roots in the left half-plane.

The Liu identity is not directly transferable.

Nevertheless, I regard coefficient encoding into a structured polynomial pencil as a promising new route.

My recommendation is to study Liu's Section 4.1 and ask:

> Can polynomial equation residuals be encoded into the maximal minors of \\(\lambda H-H_A\\), so that (5a) enforces the source equations and (5b) supplies a nondegeneracy condition?

This is more promising than copying the characteristic-polynomial construction literally.

## 2.2 Löfberg: Static output-feedback stabilization is NP-hard

[arXiv:2609.16886 — Johan Löfberg (2026)](https://arxiv.org/html/2609.16886?utm_source=chatgpt.com).

This paper is particularly useful for understanding how to eliminate spurious solutions.

Its reduction is from Betweenness.

The central polynomial is

\\[ q(s;u,v) = s^3+(N+u)s^2+N(N+v)s +N^2(N+u+v)+1. \\]

Its nontrivial Routh determinant is

\\[ \Delta=Nuv-1. \\]

Choosing

\\[ u=x_b-x_a,\qquad v=x_c-x_b \\]

makes Hurwitz stability enforce the betweenness condition.

The clever part is the use of anchor values.

By fixing two anchor coordinates at \\(0,N\\), the construction forces all gain variables to lie in a bounded interval:

\\[ 0\<x_i\<N. \\]

This prevents arbitrary large gains from creating spurious stabilizing solutions.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



### What transfers to the observer problem?

I see three potentially useful techniques.

1\. Anchor-based normalization

The projective boundary problem in your earlier determinant construction was a major obstacle.

Löfberg's approach suggests a general strategy: do not assume the desired normalization. Construct constraints that force it.

For the observer problem, one could seek a fixed-row structure that forces a selected coordinate of a variable row or Plücker vector to be nonzero.

However, this must be implemented through (5a) and (5b), not by adding an external constraint.

2\. Excluding unbounded witnesses

A reduction must prevent arbitrary large observer rows from producing unintended feasible solutions.

Löfberg's anchor mechanism is a useful model.

3\. Aggregating many conditions

Löfberg uses frequency separation to combine multiple source conditions into one polynomial while preserving the necessary root information.

This is a possible inspiration for constructing a large observer pencil from multiple local gadgets.

### What does not transfer directly?

The target is Hurwitz stability.

Your target is constant rank of a polynomial matrix for every complex \\(\lambda\\).

The two conditions have fundamentally different geometry.

A Hurwitz condition partitions the complex plane into left and right half-planes.

Your condition excludes common zeros of a family of minors, irrespective of where those zeros are located.

Therefore, Routh–Hurwitz determinants cannot simply replace the gcd criterion.

My judgement: This paper is valuable for reduction architecture, normalization, and soundness, but not as a direct hardness reduction.

## 2.3 Barkai–Shames: Unconstrained static output feedback

[arXiv:2609.38728 — Barkai and Shames (2026)](https://arxiv.org/html/2609.38728?utm_source=chatgpt.com).

This paper reduces Subset Sum to unrestricted static output feedback stabilization.

Its main technical innovation is the construction of scalar blocks whose stabilizing gains lie in two narrow intervals around 1 and 2.

The weighted sum

\\[ W=\sum_i a_i k_i \\]

is then constrained through a shared summing block.

The construction uses frequency separation and Rouché's theorem to transfer root counts from decoupled scalar systems to the coupled plant.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+2



### What is useful for your project?

I would extract three techniques.

1. Approximate discrete choices: Two narrow feasible intervals can encode Boolean decisions.
2. A shared coupling mechanism: Many individual variables can be coupled through one aggregate constraint.
3. Quantitative soundness: Explicit margins and bounds prevent small perturbations from invalidating the reduction.

The shared coupling block is especially interesting.

Your \\(q=3\\) example demonstrates that simply adding another free row can destroy the intended gate by allowing one row to absorb the image of another.

The Barkai–Shames construction suggests the opposite strategy: deliberately couple several variables through a shared structure.

For your observer problem, this could mean designing \\(A\\) so that the images

\\[ l_1A,\ldots,l_rA \\]

are constrained through a common quotient-space block.

The challenge is to make the coupling unavoidable rather than allowing the free rows to absorb one another.

### What should not be copied?

Their Rouché argument is tailored to roots in selected regions of the right half-plane.

It does not directly establish that the maximal minors of an observer pencil have gcd 1.

I would borrow the quantitative bounding ideas, not the root-counting argument itself.

## 2.4 Ahmadi–Chaudhry–Narang–Tang: Complexity of output feedback stabilization

[arXiv:2609.20636 — Ahmadi et al. (2026)](https://arxiv.org/html/2609.20636?utm_source=chatgpt.com).

This paper proves strong NP-hardness for output feedback stabilization in both continuous and discrete time.

It also establishes an interesting representation obstruction: even for stabilizable systems, a polynomial-time algorithm cannot always output a stabilizing feedback gain in its standard representation.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



### Why is this relevant?

I see two lessons.

First: do not assume that decision and synthesis have the same complexity.

For your project, separate:

\\[ \mathrm{DEC}: \exists L\text{ satisfying (5a),(5b)} \\]

from

\\[ \mathrm{SYNTH}: \text{construct such an }L. \\]

A rational-witness theorem would be valuable, but it should not be assumed.

Second: distinguish representation size from algebraic existence.

An observer might exist but require a complicated algebraic representation.

This is particularly important if you want to establish membership in NP or develop an exact synthesis algorithm.

The representation obstruction in the output-feedback paper does not prove that your observer problem has the same obstruction. It is a warning against assuming polynomial-size rational witnesses without proof.

### My assessment

This paper is useful as complexity-theoretic background, but it is not my preferred source of a direct reduction to your problem.

The mismatch between Hurwitz stabilization and pencil-rank admissibility remains substantial.

# 3. The most important new direction: understand the spectral condition through invariant subspaces

I think there is a deeper structural observation behind your \\(q=2\\) no-go theorem that deserves to become a central lemma in the next stage.

It also explains why the \\(q=3\\) example behaves differently.

## 3.1 An eigenvector interpretation

Suppose (5a) holds. In the compressed representation, there exists a matrix \\(F\\) such that

\\[ H_A=FH. \\]

Consequently,

\\[ P(\lambda)=\lambda H-H_A =(\lambda I-F)H. \\]

Let

\\[ h=\operatorname{rank}H. \\]

Since \\(F\\) is a square matrix, it has at least one complex eigenvalue, say \\(\lambda_0\\).

At that eigenvalue,

\\[ \operatorname{rank}(\lambda_0 I-F)\leq q-1. \\]

Therefore,

\\[ \operatorname{rank}P(\lambda_0) \leq q-1. \\]

A necessary condition for (5b) is consequently

\\[ \boxed{h\leq q-1.} \tag{2} \\]

This immediately explains the \\(q=2\\) obstruction when \\(h=2\\).

There is a stronger characterization.

Let \\(U=\operatorname{im}H\subseteq\mathbb C^q\\). Then

\\[ \operatorname{rank}((\lambda I-F)H) = \operatorname{rank}H \\]

if and only if

\\[ U\cap\ker(\lambda I-F)=\\{0\\}. \\]

Thus (5b) is equivalent to requiring

\\[ \boxed{ U\cap E\_\lambda(F)=\\{0\\} \quad \text{for every eigenvalue }\lambda\text{ of }F, } \tag{3} \\]

where \\(E\_\lambda(F)=\ker(\lambda I-F)\\).

This is a useful way to understand the spectral condition: the image of \\(H\\) must avoid all eigenspaces of the induced row-action matrix.

### Why this matters for the next reduction

For \\(q=2\\), if \\(h=2\\), then \\(U=\mathbb C^2\\), so it necessarily intersects every nonzero eigenspace.

For \\(q=3\\), however, \\(h=2\\) allows \\(U\\) to be a plane in \\(\mathbb C^3\\) avoiding finitely many eigenvector directions.

This is exactly the additional freedom that makes the \\(q=3\\) construction possible.

I would investigate (3) as a central structural tool.

It potentially turns the hardness problem into one of constructing a suitable invariant subspace together with an eigenvector-avoidance condition.

## 3.2 The next gate should be a coupled-plane gate

I would now abandon the objective of realizing multiplication in one row.

Instead, work with a two-dimensional subspace

\\[ U=\operatorname{span}\\{x_1,x_2\\} \\]

and study the induced action of \\(A\\) on it.

The goal is to make the two rows satisfy coupled relations:

\\[ \begin{aligned} v_1&=a\_{11}x_1+a\_{12}x_2,\\\ v_2&=a\_{21}x_1+a\_{22}x_2. \end{aligned} \tag{4} \\]

The coefficients \\(a\_{ij}\\) are not necessarily independent variables. They arise from the same induced linear action.

The crucial requirement is that the second row cannot be freely chosen to absorb the first row's image.

Your \\(q=3\\) example fails precisely because such absorption is possible.

A valid construction must force a relation between \\(x_1\\) and \\(x_2\\) before the spectral condition is applied.

### A possible construction method

I would use the following approach.

1. Choose a fixed quotient-space decomposition.
2. Prescribe a structured induced action of \\(A\\).
3. Require the variable two-plane to be invariant under that action.
4. Encode multiplication in the Plücker coordinates of that plane.
5. Choose the remaining spectral degrees of freedom so that the plane avoids all eigenspaces of \\(F\\).

The Plücker embedding is particularly natural because a two-plane in a four-dimensional space is represented by coordinates

\\[ p\_{12},p\_{13},p\_{14},p\_{23},p\_{24},p\_{34} \\]

satisfying

\\[ p\_{12}p\_{34} -p\_{13}p\_{24} +p\_{14}p\_{23}=0. \\]

This is a quadratic relation.

It is not automatically the desired multiplication gate, but it gives a richer geometric object than the single-row determinant.

A concrete target: Construct a valid \\(q=3\\) observer instance in which the feasible two-plane has a nontrivial algebraic relation between its Plücker coordinates, and demonstrate that neither row can be independently altered without violating (5a) or (5b).

I would make this the next hardness experiment.

# 4. The ARM(3) paper: a fifth reference that may be even closer geometrically

Although you asked specifically about four papers, I would not leave out Majumdar's work.

[Affine Rank Minimization is ER Complete, arXiv:2602.14037](https://arxiv.org/abs/2602.14037?utm_source=chatgpt.com).

It proves \\(\exists\mathbb R\\)-completeness of affine rank minimization even for a fixed rank bound of 3.

Its construction uses:

- Arithmetic circuit compilation.
- Rank-forcing gadgets.
- A fixed-rank gauge block.
- A composition lemma.
- Exact control of unintended interactions.

This is extremely relevant because your observer problem is also governed by structured rank constraints.

There is one particularly important connection.

In the ARM construction, the gauge block removes ambiguity in the matrix factorization.

In your observer construction, the analogous problem is that free rows can absorb one another or create unintended feasible row spaces.

I would therefore investigate whether an observer analogue of the ARM gauge block can be constructed.

For example, can fixed rows of \\(L_0\\), together with carefully designed rows of \\(CA\\) and \\(C\\), force a canonical representation of the variable observer subspace?

If yes, the ARM composition strategy may become much more transferable.

The central theorem to seek is:

Proposed Theorem 2 — Observer gadget composition

Given a collection of local observer gadgets satisfying suitable independence and rank conditions, construct a single observer instance whose feasible compressed row spaces correspond exactly to compatible solutions of the individual gadgets.

This would be much more valuable than finding another isolated multiplication example.

# 5. Answering the five questions in your new report

## Question 1. Is the single-row determinant architecture genuinely dead?

My answer is:

Yes, for the \\(q=2\\) architecture described in the report. No, for determinant-based hardness in general.

The complete \\(q=2\\) result is sufficiently strong to close this particular route.

I would state the result carefully in the research paper:

> Under the stated observer formulation, no \\(q=2\\) instance realizes a nontrivial single-row multiplication gate satisfying both (5a) and (5b).

I would not generalize this to all determinant-based constructions.

The coupled-plane approach remains open.

## Question 2. Which route should come next?

My ranking is:

| Route                                         | Priority | Reason                                                    |
| --------------------------------------------- | -------- | --------------------------------------------------------- |
| (d) Fixed-\\(c\\) theory and structural paper | 1        | Independent results can be obtained immediately           |
| (c) Liu-style coefficient encoding            | 2        | Best new route to \\(\exists\mathbb R\\)-hardness         |
| (a) \\(q\geq3\\) coupling gate                | 3        | Natural continuation of the new structural result         |
| (b) ARM gauge/rank forcing                    | 4        | Potentially powerful, but requires a nontrivial embedding |

I would actually combine (c) and (b).

The objective should be to encode arithmetic residuals into structured pencil minors, with an observer-specific gauge mechanism preventing unwanted row-space solutions.

The \\(q\geq3\\) coupling construction can be developed alongside this work.

## Question 3. Can Liu's effective gain dimension be adapted?

Yes. I think this is the most immediately actionable question in the report.

My proposed parameter is

\\[ \boxed{ \kappa\_{\mathrm{obs}} = r\\,\operatorname{rank}[N,AN]. } \\]

It measures the dimension of the free observer data after compression to \\(K_0\\).

The next step is to prove an exact algorithmic theorem.

The most promising formulation is:

Proposed Theorem 3 — Fixed effective observer dimension

For rational observer data, if \\(\kappa\_{\mathrm{obs}}\\) is fixed, the feasibility problem admits a polynomial-time exact decision algorithm and, where possible, exact observer synthesis.

The proof needs to establish a polynomial-size algebraic formulation of the spectral gcd condition.

I would investigate a Bezout certificate.

Suppose the maximal minors of \\(P(\lambda)\\) are

\\[ f_1(\lambda),\ldots,f_s(\lambda). \\]

Then (5b) is equivalent to

\\[ \gcd(f_1,\ldots,f_s)=1. \\]

By the polynomial Bezout identity, this is equivalent to the existence of polynomials \\(g_i\\) such that

\\[ \boxed{ \sum\_{i=1}^s g_i(\lambda)f_i(\lambda)=1. } \tag{5} \\]

The degree of the \\(g_i\\) can be bounded in terms of the degrees of the minors.

Equating coefficients gives finitely many polynomial equations in the compressed observer parameters and the coefficients of the \\(g_i\\).

This could eliminate the universal quantifier over \\(\lambda\\) in a particularly clean way.

There is an important implementation issue: the number of maximal minors can grow combinatorially. A polynomial-time theorem must avoid an exponentially large explicit enumeration when the relevant matrix dimensions vary.

I would investigate structured determinantal algorithms or a bounded-size generating family of minors.

## Question 4. Do bounded-gain and root-counting techniques help?

Yes, but I would separate the two techniques.

| Technique                  | Potential usefulness    |
| -------------------------- | ----------------------- |
| Anchors and gain bounds    | High                    |
| Robust margins             | High                    |
| Frequency separation       | Moderate                |
| Rouché root counting       | Indirect                |
| Routh–Hurwitz determinants | Low for direct transfer |

The reason is that the observer problem has a different spectral geometry.

For your problem, the important object is not the location of roots but the common-root structure of maximal minors.

I would investigate the following substitutes:

- Polynomial root separation bounds.
- Subresultant sequences.
- Resultant certificates.
- Bezout identities.
- Projective compactification.
- Quantitative bounds on the coefficients of common factors.

These are more naturally adapted to the observer pencil.

## Question 5. Should the structural paper be written now?

Yes. I would begin the paper now rather than waiting for a hardness result.

The new no-go theorem substantially strengthens the structural contribution.

In particular, it establishes that a mathematically valid rank-4 gate for (5a) is insufficient for observer feasibility.

That is a valuable result because it identifies an obstruction arising specifically from the interaction between the invariance condition and the spectral condition.

The paper should emphasize this interaction rather than present the negative result as a failed hardness attempt.

# 6. How I would reorganize the structural paper

The new report suggests a stronger paper than the one I proposed previously.

I would make the interaction between algebraic invariance and spectral admissibility the central theme.

### Suggested title

Algebraic Structure and Complexity of Minimum-Order Functional Observer Synthesis

Alternative:

Invariant Subspaces, Matrix Pencils, and the Computational Complexity of Functional Observer Design

### Proposed organization

| Section                                    | Main content                                                          |
| ------------------------------------------ | --------------------------------------------------------------------- |
| 1. Introduction                            | Problem formulation and complexity motivation                         |
| 2. Algebraic preliminaries                 | Rank conditions, quotient spaces, compressed matrices                 |
| 3. General observer characterization       | (5a), (5b), spectral gcd formulation                                  |
| 4. Low-codimension classification          | \\(c=0,1,2\\), including the \\(q=2\\) dichotomy                      |
| 5. Spectral obstructions                   | The \\(\omega=2\\) obstruction and complete \\(q=2\\) no-go theorem   |
| 6. Higher-row phenomena                    | \\(q=3\\) feasible example and row absorption                         |
| 7. Rigidity and invariant-subspace results | Global rigidity and precise local limitations                         |
| 8. Algebraic complexity                    | \\(\exists\mathbb R\\) upper bound and effective observer dimension   |
| 9. Exact algorithms                        | Spectral gcd, Bezout certificates, four-layer solver                  |
| 10. Open problems                          | Coupled-row hardness, fixed-parameter algorithms, real versus complex |

I would include the rank-4 construction even though it fails (5b).

It demonstrates an important distinction:

\\[ \boxed{ \text{Algebraic expressiveness of (5a)} \neq \text{expressiveness of the complete observer problem}. } \\]

That is a meaningful structural finding.

I would also include the new eigenvector-avoidance interpretation if you can prove it in the generality required by the paper.

# 7. The three experiments I would conduct next

Rather than launch several unrelated searches, I would prioritize these three experiments.

## Experiment A — Effective observer dimension

Highest immediate priority

Establish the compressed parameter space rigorously.

Starting with

\\[ \mathcal T(\Delta R)=(\Delta RN,\Delta RAN), \\]

calculate \\(\kappa\_{\mathrm{obs}}\\) for your existing test instances.

Investigate whether fixed \\(c\\), fixed \\(\omega\\), or fixed \\(\operatorname{rank}[N,AN]\\) implies a tractable subclass.

Success criterion: An exact reduction theorem and a fixed-parameter algorithmic result.

## Experiment B — Coupled-row multiplication gate

Highest hardness priority

Work with \\(q=3\\), rank \\(H=2\\), and a two-dimensional variable row space.

Search for an induced action \\(F\\) that forces a nontrivial relation between both rows, while ensuring

\\[ \operatorname{im}H\cap E\_\lambda(F)=\\{0\\} \\]

for every eigenvalue.

Success criterion: A genuine multiplication relation that survives both (5a) and (5b), with no row-absorption solutions.

## Experiment C — Pencil coefficient encoding

Alternative hardness priority

Study the polynomial minors of

\\[ P(\lambda)=\lambda H-H_A. \\]

Try to encode polynomial residuals into their coefficients and construct a composition mechanism analogous to Liu's coefficient encoding or Majumdar's rank-forcing gadgets.

Success criterion: A polynomial-time reduction from a known \\(\exists\mathbb R\\)-complete problem, with both directions of correctness proved.

These experiments are complementary.

Experiment A can lead to an independent algorithmic paper. Experiments B and C address unrestricted hardness.

# 8. My final judgement on the four papers

| Paper                     | What I would actually use                                                                     |
| ------------------------- | --------------------------------------------------------------------------------------------- |
| Liu, 2610.00390           | Effective observer dimension; coefficient encoding; fixed-dimensional exact synthesis         |
| Löfberg, 2609.16886       | Anchor mechanism; boundedness; soundness against unbounded witnesses                          |
| Barkai–Shames, 2609.38728 | Shared coupling architecture; robust margins; quantitative estimates                          |
| Ahmadi et al., 2609.20636 | Complexity background; distinction between decision and synthesis; representation obstruction |

My strongest recommendation is to study Liu's paper first.

It offers something your project currently needs: a way to turn the apparent number of free observer parameters into a smaller, structurally meaningful quantity.

I would then study Majumdar's ARM(3) paper alongside Liu, because the two papers suggest complementary ideas:

- Liu: eliminate redundant continuous parameters.
- Majumdar: use rank constraints to encode multiplication.
- Your project: exploit invariant row spaces and spectral pencils to combine these two mechanisms.

That combination is potentially more fruitful than attempting to imitate any one of the four output-feedback reductions.

## 9. A final strategic point

I would change the central research question slightly.

Instead of asking only:

> Is minimum-order functional observer synthesis \\(\exists\mathbb R\\)-complete?

I would ask:

> What is the effective algebraic dimension of functional observer synthesis, and how does this dimension govern both its computational complexity and the expressive power of its invariant matrix pencils?

This gives you a coherent research program with three connected objectives:

1. Structural: Understand the geometry of admissible invariant row spaces.
2. Algorithmic: Identify effective parameters that permit exact polynomial-time synthesis.
3. Complexity-theoretic: Determine whether the unrestricted pencil constraints can encode arbitrary real algebraic feasibility.

The new \\(q=2\\) no-go theorem is an important step toward answering the third question. The \\(q=3\\) example suggests where to look next, and Liu's effective gain dimension provides a concrete starting point for the second.

My recommendation is to make Experiment A the next theorem you prove, Experiment B the main new hardness construction you investigate, and start writing the structural paper immediately. This is a better-balanced strategy than continuing to search for isolated determinant gates.

### Primary references

1. [Liu (2026), Computational complexity of static output feedback stabilization](https://arxiv.org/html/2610.00390?utm_source=chatgpt.com).
2. [Löfberg (2026), Static output-feedback stabilization is NP-hard](https://arxiv.org/html/2609.16886?utm_source=chatgpt.com).
3. [Barkai and Shames (2026), On the NP-Hardness of Unconstrained Static Output Feedback Stabilization](https://arxiv.org/html/2609.38728?utm_source=chatgpt.com).
4. [Ahmadi, Chaudhry, Narang and Tang (2026), Complexity of Output Feedback Stabilization](https://arxiv.org/html/2609.20636?utm_source=chatgpt.com).
5. [Majumdar (2026), Affine Rank Minimization is ER Complete](https://arxiv.org/abs/2602.14037?utm_source=chatgpt.com).

All four requested papers are arXiv preprints; the assessments above concern their stated mathematical results and constructions, not an independent verification of every proof.