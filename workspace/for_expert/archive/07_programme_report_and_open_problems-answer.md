# Review of `07_programme_report_and_open_problems.md`

The report marks a substantial advance. In particular, the programme has moved beyond numerical exploration: you now have exact nullspace-pencil tests, chart-wise algebraic calculations, explicit consistency checks, and a second algebraic proof of the \\(n=6\\) counterexample. That is a meaningful improvement in the reliability of the project.

My overall assessment is:

1. The main technical bottleneck is now correctly identified: deciding whether the specialized maximal minors have gcd \\(1\\) at some parameter value.
2. There is a standard algebraic-geometric route to Q1. It is not necessary to infer exceptional parameter values from the generic gcd alone. One can formulate the existence of a good specialization directly by a bounded-degree Bézout identity, or by a resultant after a finite stratification by degrees.
3. The observation at \\(q_0\\) is plausible and potentially important, but its current formulation is stronger than the evidence supports. The six-instance observation should be presented as an empirical pattern until the precise algebraic hypotheses and a proof are supplied.
4. The proposed short note is worth writing, but I would make the dimension obstruction and the exact \\(n=6\\) counterexample the two principal results. Include the drop-locus phenomenon as a carefully qualified computational observation, not as a theorem.
5. The existence of a polynomial-system formulation does not, by itself, make a hardness reduction more promising. It identifies a natural complexity framework, but a valid reduction still has to encode the unrestricted problem rather than a restricted family of solutions.

I will address Q1–Q4 in detail, then give a revised technical and writing plan.

## 1. Assessment of the progress reported

### 1.1 The nullspace-pencil criterion is now the right primary test

Your implementation uses

\\[ P\_{\mathcal Z}(\lambda) = \big[(\lambda I-A)V\mid Z\big], \\]

where the columns of \\(V\\) and \\(Z\\) span

\\[ \ker[C;CA],\qquad \ker[C;\mathcal L], \\]

respectively.

This is the right object to use as the primary spectral test. It removes the need to work directly with the larger pencil \\(Q\_{\mathcal L}(\lambda)\\), and it makes the dependence on the chosen augmentation transparent: the spectral condition is expressed in terms of the nullspace \\(\mathcal Z\\).

The report's six-pencil comparison is useful evidence that the two implementations agree on the tested examples. The failed sampled-\\(\lambda\\) test is also a valuable diagnostic: a finite sample cannot certify a rank identity for every complex \\(\lambda\\). A rank drop can occur at an unsampled algebraic number, including a non-rational one.

One qualification is important. A gcd computation over \\(\mathbb Q(\theta)[\lambda]\\) is a computation over the generic parameter point. It does not, on its own, decide the existence of a special parameter point with a different gcd. Your report has correctly discovered this limitation; Q1 is precisely about replacing that incomplete inference with an exact specialization test.

### 1.2 The dimension obstruction and its uniformity result

The report says that the identity

\\[ h=s_0+q-r \\]

is used only under the explicit hypothesis

\\[ V'\cap S=0. \\]

That qualification must remain attached to every statement using the identity. In particular, it would be unsafe to describe the formula as a general expression for \\(h\\), or to infer it from the dimensions alone.

The 495 augmentation checks and 360 identity checks are useful regression evidence. They do not replace a proof, but they are exactly the kind of evidence that helps detect implementation errors in a project with several interacting nullspace and rank calculations.

For the paper, I suggest separating three levels:

- the unconditional dimension identity or inequality;
- the additional hypothesis under which equality \\(h=s_0+q-r\\) follows;
- the resulting uniform obstruction on the class of augmentations satisfying that hypothesis.

This will make the theorem easier to state and harder to misapply.

### 1.3 The algebraic feasibility formulation is a real step forward

The formulation

\\[ \sum_i u_i(\lambda)m_i(\lambda;\Theta)=1 \\]

is conceptually appropriate. For a fixed specialization \\(\Theta=\theta\\), it expresses that the maximal minors have no common complex root, equivalently that they generate the unit ideal in the univariate polynomial ring.

However, the degree bound on the \\(u_i\\) needs to be stated and justified carefully. It is not enough to say that the coefficients are polynomially bounded in number. One needs a uniform bound that is valid even when some specialized minors become zero or drop in degree.

I give a clean way to formulate this below.

### 1.4 The chart computations are much stronger than a rational grid

The use of Gröbner bases and saturation for the algebraic \\((5a)\\)-layer is the correct direction. In particular, the Rabinowitsch equation

\\[ zf-1=0 \\]

is a standard way to impose \\(f\ne0\\) algebraically.

There are still two distinctions to preserve in the report:

- A Gröbner basis equal to \\([1]\\) certifies emptiness of the algebraic set over the field in which the computation is performed, provided the ideal and saturation have been set up correctly.
- A computation over \\(\mathbb Q\\) or its algebraic closure is not automatically a statement about real points. For a real-parameter existence question, real algebraic geometry is the appropriate framework.

The transpose correction in your implementation is also important. The condition involves row vectors \\(xA\\), so in column coordinates the corresponding operation is \\(A^{\mathsf T}x^{\mathsf T}\\). It is good that this was caught and that the previous claim about a defect in the nullspace generator was withdrawn.

### 1.5 The generic-gcd correction is mathematically essential

The report explicitly withdraws the statement

> a chart with generic gcd degree \\(\ge1\\) is uniformly bad.

That withdrawal is correct and necessary.

A generic gcd of positive degree says that the generic parameter point is spectrally bad. It does not imply that every specialization is bad. At exceptional parameter values, the gcd can drop in degree, possibly all the way to a nonzero constant.

This is not a minor technicality. It changes the logical status of the chart analysis:

- generic gcd degree \\(0\\) gives a generic good point, subject to the usual nonvanishing and admissibility checks;
- generic gcd degree \\(>0\\) gives generic failure;
- generic gcd degree \\(>0\\) does not decide whether exceptional good points exist.

Your new `UNKNOWN` status is therefore the correct one whenever the exceptional locus has not been exhaustively analyzed.

### 1.6 The \\(n=6\\) counterexample is now considerably stronger

The two improvements are significant:

1. The proportionality condition\
   \\[\
   L_0Ax\parallel L_0x,\qquad x\in V,\
   \\]\
   is now proved by showing that the relevant \\(2\times2\\) determinant vanishes on a basis and on pairwise sums, hence vanishes identically as a quadratic form.
2. The chart-wise gcd calculation gives a second algebraic route to the conclusion that no parameter value is feasible.

The second proof is particularly useful because it is independent of the earlier projective-surjectivity argument. But I would still inspect the actual chart equations and denominator handling before describing it as a complete certificate. The report gives the conclusion and the exceptional parameter values, but not the underlying polynomials or the exact specialization argument. Those should be included in the technical appendix or computational supplement.

## 2. Q1 — An exact way to decide whether the gcd can drop to degree zero

This is the most important question in the report.

Let

\\[ m_1(\theta,\lambda),\ldots,m_N(\theta,\lambda) \\]

be the maximal minors of \\(P\_{\mathcal Z}(\theta,\lambda)\\), after expressing the chart coordinates by \\(\theta\\).

For a fixed parameter value \\(\theta=\theta_0\\), the spectral condition is

\\[ \gcd\_{\mathbb C[\lambda]} \big(m_1(\theta_0,\lambda),\ldots,m_N(\theta_0,\lambda)\big)=1. \\]

Equivalently, the specialized polynomials have no common complex root.

There are two useful exact formulations.

### 2.1 The bounded-degree Bézout formulation

For a fixed \\(\theta_0\\), the polynomials \\(m_i(\theta_0,\lambda)\\) generate the unit ideal in \\(\mathbb C[\lambda]\\) if and only if there exist polynomials \\(u_i(\lambda)\\) such that

\\[ \boxed{ \sum\_{i=1}^N u_i(\lambda)m_i(\theta_0,\lambda)=1. } \\]

This is the univariate Bézout identity.

Suppose every \\(m_i\\) has degree at most \\(D\\) in \\(\lambda\\). There is a uniform finite degree bound on the Bézout coefficients. A conservative bound that is sufficient for an algorithmic formulation is obtained by iterating the two-polynomial Euclidean algorithm: one may use a bound depending only on \\(N\\) and \\(D\\), for example a bound of order \\(ND\\). The precise sharp bound is not important for decidability, but it must be stated and proved before it is used in a certificate-size claim.

Write

\\[ u_i(\lambda)=\sum\_{k=0}^{B}u\_{ik}\lambda^k \\]

for a justified uniform bound \\(B\\). Comparing coefficients in

\\[ \sum_i u_i(\lambda)m_i(\theta,\lambda)=1 \\]

then gives finitely many polynomial equations in

\\[ \theta,\quad u\_{10},\ldots,u\_{NB}. \\]

Consequently, the existence question can be written as a finite algebraic feasibility problem:

\\[ \boxed{ \exists\theta,\\{u\_{ik}\\}: \quad \sum_i u_i(\lambda)m_i(\theta,\lambda)\equiv1. } \\]

This is the cleanest way to repair the logical gap in the current report.

There are two qualifications.

First, handle denominators. If the chart parametrization or the minors have rational-function coefficients in \\(\theta\\), clear denominators only on a chart domain where the denominators are nonzero. Those nonzero conditions must remain in the system. Multiplying by denominators without retaining their nonvanishing conditions can introduce spurious specializations.

Second, handle zero specializations. A polynomial that is identically zero after specialization is allowed among the \\(m_i(\theta_0,\lambda)\\). The Bézout identity handles this naturally: its coefficient \\(u_i\\) can be zero, and the other minors must still generate the unit ideal.

This gives a direct exact test for the existence of a good specialization. It does not require guessing the exceptional values from the leading coefficients of the generic gcd.

### 2.2 A resultant formulation using a generic linear combination

There is also a more compact alternative.

Fix a specialization \\(\theta_0\\), and suppose at least one specialized minor, say \\(m_j(\theta_0,\lambda)\\), is nonzero. Consider a linear combination of the other minors:

\\[ g_c(\theta_0,\lambda) = \sum\_{i\ne j}c_i\\,m_i(\theta_0,\lambda). \\]

Over an infinite field, if

\\[ \gcd(m_1,\ldots,m_N)=1, \\]

then for a suitable choice of constants \\(c_i\\),

\\[ \gcd(m_j,g_c)=1. \\]

The reason is simple. The nonconstant irreducible factors of \\(m_j\\) are finite in number. For each such factor, the combinations \\(g_c\\) divisible by that factor form a proper linear subspace of the coefficient space, provided that factor does not divide every \\(m_i\\). Since the total gcd is \\(1\\), no factor of \\(m_j\\) divides all the other minors. A finite union of proper linear subspaces cannot cover the whole coefficient space over an infinite field.

Thus, for a fixed specialization,

\\[ \gcd(m_1,\ldots,m_N)=1 \\]

is equivalent to the existence of a coefficient vector \\(c\\) for which

\\[ \operatorname{Res}\_\lambda(m_j,g_c)\ne0, \\]

with the usual degree and zero-polynomial cases handled separately.

This leads to a finite existential formulation:

\\[ \boxed{ \exists\theta,\ c: \quad \operatorname{Res}\_\lambda \left(m_j(\theta,\lambda),\\, \sum\_{i\ne j}c_i m_i(\theta,\lambda)\right)\ne0. } \\]

One must take a finite disjunction over the possible choices of \\(j\\) and the possible specialized degrees of \\(m_j\\). This is necessary because the degree can drop at special parameter values. If \\(m_j\\) specializes to a nonzero constant, the gcd is already \\(1\\); if all minors specialize to zero, the gcd is not \\(1\\).

This resultant approach is attractive because it turns the question into polynomial equations and one polynomial nonvanishing condition, without introducing a large collection of Bézout coefficient variables.

### 2.3 What about the Bézout matrix?

The Bézout matrix is useful for two polynomials. For a pair \\(f,g\\) of fixed degrees, its determinant is closely related to the resultant, and its rank detects common factors.

For a family of many minors, I would not start by constructing a single “Bézout matrix of the family” unless you define precisely which generalized construction you mean. There is no unique canonical matrix with all the desired properties merely from the phrase “the Bézout matrix of the family.”

A safer construction is:

1. choose one nonzero specialized minor \\(m_j\\);
2. form a generic linear combination \\(g_c\\) of the other minors;
3. use the ordinary two-polynomial resultant or Bézout matrix of \\(m_j\\) and \\(g_c\\);
4. stratify by the degree of \\(m_j\\), and enforce all chart-denominator conditions.

That is standard, explicit, and easy to verify.

### 2.4 Real parameters versus rational parameters

This distinction is crucial for your programme.

If the question is whether there exists a real parameter vector \\(\theta\\) satisfying the chart constraints and the Bézout identity, then the resulting problem is a semialgebraic feasibility problem over the reals. In principle, it is decidable by real quantifier elimination, for example cylindrical algebraic decomposition. It may be expensive, but it is an exact decision procedure.

If the question is whether there exists a rational parameter vector \\(\theta\in\mathbb Q^k\\), that is a different arithmetic problem. Real quantifier elimination does not decide rational-point existence in general.

Your report currently says that candidate matrices are rational, hence real. That is a valid statement about the candidates you have found. It does not establish that every real feasible chart point can be replaced by a rational one.

There is one useful special case: if a good point lies in a nonempty relatively open subset of a rational chart, rational points are dense, so a rational good point exists. But an exceptional drop locus may be lower-dimensional or even zero-dimensional. In that case, rational density of the ambient chart says nothing about whether the exceptional locus contains a rational point.

My recommendation for Q1: formulate the primary theorem as a real-parameter existential problem, unless the mathematical problem explicitly requires rational augmentations. Use the Bézout identity as the most direct formulation and the resultant as a more compact computational alternative. Do not use generic-gcd degree or leading-coefficient roots as a complete decision method.

## 3. Q2 — Does the “thin feasible locus at \\(q_0\\)” already appear in the 2026 preprint?

Not in the precise form stated in your report. The preprint supplies important structural ingredients, but I did not find it asserting the generic-gcd-drop phenomenon or proving that the spectral-feasible subset of the minimum-order algebraic family is a proper subvariety.

The distinction matters.

### 3.1 What the preprint does establish

The 2026 preprint establishes that:

- \\(q_0\\) is the minimum order at which the algebraic condition is feasible;
- the complete family of order-\\(q_0\\) algebraically admissible augmentations can be characterized;
- at a prescribed order, the algebraic and spectral conditions admit nullspace-based characterizations;
- Grassmann charts provide a finite parameterization of the candidate nullspaces;
- the spectral condition is a matrix-pencil rank condition on each such candidate.

These are directly relevant to your computations. In particular, Theorem 4 gives the nullspace-pencil condition, and the paper's fixed-order characterization provides the geometric setting in which chart-wise analysis is performed.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



The illustrative example also proves that the spectral condition can exclude the entire algebraically admissible family at \\(q_0\\), and even at \\(q_0+1\\), while allowing a solution at \\(q_0+2\\). It does so by examining the full Grassmann-chart families, not by relying on a finite rational grid.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



### 3.2 What the preprint does not appear to establish

I did not find a result in the preprint of the following form:

> On the algebraically admissible variety at \\(q_0\\), the generic parameter point is spectrally infeasible, and the spectrally feasible points are exactly the points at which the generic gcd drops to degree zero.

Nor did I find a general theorem saying that the spectral-feasible subset at \\(q_0\\) is a proper algebraic subvariety of the algebraically admissible family.

The preprint's characterization makes such a study possible, but it does not settle it.

Thus your six-instance observation is not merely a restatement of the preprint's main theorem. It is a potentially distinct observation about the geometry of the spectral-feasible locus inside the algebraically admissible family. Its novelty, however, depends on whether you can turn it into a mathematically precise statement and establish it beyond the six examples.

### 3.3 An important correction to the geometric interpretation in II.12

I would not yet call the feasible set a “finite determinantal set rather than an open one.”

There are two issues.

First, the condition

\\[ \gcd\_\lambda(m_1(\theta,\lambda),\ldots,m_N(\theta,\lambda))=1 \\]

is naturally a constructible condition in the parameters. It can be described using a finite collection of polynomial equalities and inequalities, for example through Bézout coefficients or a degree-stratified resultant construction. It need not be a closed algebraic condition.

Second, the phrase “generic gcd degree” needs to refer to the correct parameter space. There are at least two possible generic points:

- the generic point of the entire Grassmann chart;
- the generic point of the algebraically admissible locus inside that chart.

These are not interchangeable. If the \\((5a)\\)-condition cuts out a proper subvariety of the chart, the generic gcd on the ambient chart need not describe the generic gcd along the admissible locus.

For the paper, define the algebraically admissible parameter set on a chart by

\\[ X=\\{\theta:\text{the chart is defined and (5a) holds}\\}. \\]

Then study the spectral-feasible subset

\\[ X\_{\mathrm{sp}} = \left\\{\theta\in X: \gcd\_\lambda(m_1(\theta,\lambda),\ldots,m_N(\theta,\lambda))=1 \right\\}. \\]

The correct questions are:

1. Is \\(X\\) irreducible, or does it have several irreducible components?
2. What is the generic gcd degree on each component of \\(X\\)?
3. Is \\(X\_{\mathrm{sp}}\\) empty, dense in a component, relatively open in a component, or contained in a lower-dimensional subset?
4. Does \\(X\_{\mathrm{sp}}\\) have rational points, real points, or only complex points?

These are more precise than asking whether the feasible set is “thin.”

### 3.4 Why a generic positive-degree gcd can coexist with good exceptional points

The phenomenon you report is algebraically possible because specialization can reduce the degree of a polynomial.

For example, consider the simple family

\\[ f(\theta,\lambda)=\theta\lambda+1,\qquad g(\theta,\lambda)=2\theta\lambda+2. \\]

Over the rational-function field \\(\mathbb Q(\theta)\\),

\\[ \gcd(f,g)=\theta\lambda+1, \\]

up to a nonzero scalar, so the generic gcd has degree one. But at \\(\theta=0\\),

\\[ f(0,\lambda)=1,\qquad g(0,\lambda)=2, \\]

and the specialized gcd is \\(1\\).

The common factor has effectively disappeared because its degree dropped at the specialization.

This example also illustrates why one must distinguish the generic polynomial identity from the specialized polynomial identity. It does not prove that your six instances have the same mechanism; it only demonstrates that the mechanism is mathematically consistent.

In your actual problem, the exceptional set may involve:

- vanishing leading coefficients of the generic gcd;
- vanishing denominators in a rational-function representation;
- specializations at which the generic gcd itself specializes to the zero polynomial;
- degree drops in individual minors that alter the effective gcd calculation.

That is why your present list of candidate exceptional parameters is incomplete, as the report correctly acknowledges. 【turn6file0】

### 3.5 A better formulation of the observation

I suggest replacing the current statement by the following provisional formulation:

> Observed minimum-order specialization phenomenon. In the six tested instances, on every examined chart of the order-\\(q_0\\) algebraically admissible family, the generic spectral pencil is infeasible. Every spectrally feasible point found by exact or rational specialization occurs at a parameter value where the specialized maximal-minor gcd has degree zero. In the tested \\(n=6\\) counterexample, no such specialization exists.

This is accurate, useful, and does not overstate what the data prove.

A stronger theorem might eventually be:

> On each irreducible component of the order-\\(q_0\\) algebraically admissible locus, either the spectral condition holds generically, or its feasible locus is contained in a proper constructible subset characterized by explicit subresultant rank conditions.

That statement is a reasonable research target. It is not established by the current report, and it is not automatic merely from the preprint's chart parameterization.

## 4. Q3 — Should the drop-locus observation appear in the short note?

Yes, but as a clearly labelled computational observation or conjecture, not as one of the two main theorems.

The proposed short note has a coherent mathematical centre:

1. a dimension obstruction, including the uniformity result under its stated hypothesis;
2. an exact \\(n=6\\) example in which the dimension obstruction does not detect the failure, but the spectral condition excludes the entire admissible family.

The drop-locus observation can strengthen the motivation for the second result and explain why naive sampling is unreliable. But it should not displace the two results that you can currently support rigorously.

### 4.1 Suggested structure

I would organize the note as follows.

1\. Introduction and problem formulation

State the observer augmentation problem, the algebraic and spectral conditions, and the order interval

\\[ q_0\le q\le n_0-p. \\]

Briefly explain why algebraic feasibility and spectral feasibility must be distinguished.

2\. A dimension obstruction

State the relevant dimension identity with all hypotheses, derive the obstruction, and state the uniformity corollary. Be explicit about which class of augmentations is covered.

3\. A spectral counterexample beyond the dimension obstruction

Give the \\(n=6\\) example. The proof should contain:

- the exact matrices \\(A,C,L_0\\);
- the value of \\(q_0\\), \\(r_1\\), and \\(h\\);
- verification of \\((5a)\\);
- the full parameterization of all admissible nullspaces at that order;
- the proportionality identity used in the projective argument;
- the exact pencil or maximal-minor gcd calculation;
- the conclusion that no admissible parameter point satisfies \\((5b)\\).

The two independent proofs are an asset. I would present the algebraic chart proof as the principal exhaustive certificate and the projective proof as an independent geometric explanation, or reverse their order if the projective proof is substantially shorter.

4\. Computational observation: spectral feasibility and specialization

Present the six-instance observation in a short subsection or remark. State exactly what was tested, what was computed symbolically, and what remains unproved.

5\. Discussion and open problems

Identify the specialization-decision problem as the main open computational question. Avoid a broad complexity claim at this stage.

### 4.2 What evidence should accompany the observation?

For each of the six instances, I would record:

| Item                   | What should be reported                                       |
| ---------------------- | ------------------------------------------------------------- |
| Algebraic locus        | Equations and chart or branch parameterization for \\((5a)\\) |
| Components             | Whether the locus is irreducible or decomposed                |
| Generic pencil         | Generic gcd degree on each component                          |
| Exceptional parameters | Exact algebraic equations, not just grid points               |
| Specialized gcd        | Exact gcd at each candidate point                             |
| Feasibility            | Explicit witness or an exhaustive infeasibility certificate   |

The most important distinction is between a finite list of candidate points and an exhaustive description of the exceptional locus. The former is exploration; the latter is a theorem or certificate.

### 4.3 What should not be claimed yet?

Avoid the following claims until they are proved:

- that all minimum-order feasible sets are lower-dimensional;
- that the feasible points always arise from a degree drop of the generic gcd;
- that the feasible set is always finite;
- that a generic positive-degree gcd implies uniform infeasibility;
- that the observed phenomenon holds for all \\(r\\), all \\(n\\), or all chart components.

The first three are especially tempting but are not justified by six examples. The report itself has already shown why the fourth is false.

My recommendation is therefore: include the observation, but give it a modest title and a precise scope. It may later become the starting point of a separate paper on the algebraic geometry of minimum-order functional-observer families.

## 5. Q4 — Does the determinantal nature of feasibility make a hardness reduction more attractive?

It makes the problem more naturally expressible in algebraic complexity terms, but it does not yet make a hardness reduction substantially easier.

There are three separate questions.

### 5.1 Polynomial-system formulation is not the same as hardness

A problem being expressible as

\\[ \exists x_1,\ldots,x_k:\quad f_1(x)=\cdots=f_m(x)=0,\quad g_1(x)\ne0,\ldots,g_s(x)\ne0 \\]

places it naturally in the setting of existential real algebraic feasibility, provided the encoding has polynomial size.

But this only gives a route to an upper-bound classification. It does not imply that the problem is \\(\exists\mathbb R\\)-hard.

A hardness proof must construct, from an arbitrary instance of a known hard problem, a polynomial-size observer instance whose feasible augmentations correspond exactly to the solutions of the original instance.

The structured form of your matrices is the main difficulty. The coefficients in the polynomial system cannot be chosen arbitrarily: they arise from a single state matrix \\(A\\), measurement matrix \\(C\\), prescribed functional \\(L_0\\), Grassmann coordinates, and the special pencil

\\[ [(\lambda I-A)V\mid Z]. \\]

Encoding arbitrary polynomial constraints into that structure is a nontrivial problem.

### 5.2 There is a complexity caveat in the current \\(\exists\mathbb R\\) claim

The report says that the number of variables and degrees is polynomial, and therefore the formulation is consistent with \\(\exists\mathbb R\\). 【turn6file0】

I would not yet state this as a formal complexity-membership result without checking the number of maximal minors.

If the pencil has dimensions growing with the input, the number of its maximal minors can be combinatorial:

\\[ \binom{a}{h}\binom{b}{h} \\]

for an \\(a\times b\\) matrix of normal rank \\(h\\), in the generic rectangular case. This may be exponential in the matrix dimensions.

A Bézout identity with one coefficient polynomial \\(u_i\\) for each maximal minor then has potentially exponentially many coefficient variables. A polynomial degree bound on each \\(u_i\\) does not by itself establish a polynomial-size existential formula.

This does not invalidate the algebraic feasibility formulation. It means that the encoding-size argument needs another step.

Possible ways forward include:

- exploiting the special structure of \\(P\_{\mathcal Z}(\lambda)\\) to use a polynomial-size set of generators for the maximal-minor ideal;
- finding a polynomial-size rank or polynomial-matrix certificate that avoids enumerating all maximal minors;
- proving a complexity result for a restricted family where the number of relevant minors is polynomially bounded;
- treating the problem as an algebraic feasibility problem with an explicit, possibly exponential, representation until a compact encoding is found.

This is an important point to settle before claiming membership in \\(\exists\mathbb R\\).

### 5.3 The failed coordinate-row reduction is a valuable warning

Your report correctly identifies the logical issue with the earlier coordinate-row restriction.

Restricting \\(\mathcal L\\) to coordinate rows restricts the set of allowed solutions for a given instance. A hardness result for that restricted solution problem does not automatically imply hardness of the unrestricted observer problem.

For a valid reduction, the construction must ensure both directions:

- every solution of the source problem gives an admissible observer augmentation;
- every admissible observer augmentation for the constructed instance yields a solution of the source problem.

The second direction is where an unrestricted solution space can invalidate a reduction based only on coordinate-row candidates.

I would retain this correction in your internal research notes. It is exactly the sort of issue that can invalidate an otherwise convincing graph-theoretic reduction.

### 5.4 My recommendation on hardness

I would not abandon the hardness direction, but I would postpone a serious reduction attempt until the following are done:

1. Complete the exact specialization criterion in Q1.
2. Establish a polynomial-size algebraic formulation, or explicitly identify the representation size if the formulation is exponential.
3. Determine whether the hardness target is real feasibility, rational feasibility, or complex algebraic feasibility.
4. Identify a restricted observer family whose structure is rich enough to encode polynomial constraints, while retaining a proof that unrestricted augmentations cannot create spurious solutions.

The \\(r=1\\) investigation is useful. The failure of the \\((5a)\\)-locus to be affine means that one particular linear-degeneration route is unavailable; it does not rule out polynomial-time algorithms or hardness reductions by other means.

The companion-form investigation could be a sensible later step, but only after the general algebraic formulation is made exact. I agree with the report's decision not to begin there prematurely.

## 6. A particularly useful refinement: turn Q1 into a single coefficient-matrix rank test

There is a formulation that I would actually recommend implementing before either the resultant or the full quantifier-elimination approach. It handles degree drops directly and gives a precise answer to the concern about zeros of individual minors' leading coefficients.

Let

\\[ D=\max_i\deg\_\lambda m_i(\theta,\lambda) \\]

be a uniform upper bound, independent of \\(\theta\\). In your application, one can take

\\[ D\leq \dim V. \\]

For a fixed specialization \\(\theta=\theta_0\\), define the linear map

\\[ \Phi\_{\theta_0}: \bigoplus\_{i=1}^N\mathbb R[\lambda]\_{\leq D-1} \longrightarrow \mathbb R[\lambda]\_{\leq 2D-1} \\]

by

\\[ \Phi\_{\theta_0}(u_1,\ldots,u_N) = \sum\_{i=1}^N u_i(\lambda)m_i(\theta_0,\lambda). \\]

Here \\(\mathbb R[\lambda]\_{\leq k}\\) denotes the vector space of polynomials of degree at most \\(k\\).

For \\(D\geq1\\), the univariate Bézout identity implies

\\[ \boxed{ \gcd(m_1(\theta_0,\lambda),\ldots,m_N(\theta_0,\lambda))=1 \iff 1\in\operatorname{im}\Phi\_{\theta_0}. } \\]

The important point is that the bound \\(\deg u_i\leq D-1\\) is sufficient. To see this, choose a nonzero \\(m_j\\). If it is a nonzero constant, the conclusion is immediate. Otherwise, since the gcd of all the minors is \\(1\\), an appropriate constant linear combination \\(g\\) of the other minors can be chosen so that

\\[ \gcd(m_j,g)=1. \\]

The ordinary two-polynomial Bézout identity then gives

\\[ a(\lambda)m_j(\lambda)+b(\lambda)g(\lambda)=1, \\]

where

\\[ \deg a<\deg g\leq D,\qquad \deg b<\deg m_j\leq D. \\]

Expanding \\(g\\) into the original minors gives the required coefficients \\(u_i\\).

Now express \\(\Phi\_{\theta}\\) in monomial bases. Let

\\[ M(\theta)\in\mathbb R[\theta]^{2D\times ND} \\]

be its coefficient matrix, whose columns are the coefficient vectors of

\\[ m_i(\theta,\lambda),\quad \lambda m_i(\theta,\lambda),\quad\ldots,\quad \lambda^{D-1}m_i(\theta,\lambda). \\]

Let \\(e_0=(1,0,\ldots,0)^{\mathsf T}\\) denote the coefficient vector of the constant polynomial \\(1\\).

Then the entire spectral condition at a parameter point is equivalent to

\\[ \boxed{ \operatorname{rank}M(\theta) = \operatorname{rank}[M(\theta)\mid e_0]. } \tag{\*} \\]

This is a finite rank condition on a polynomial matrix in the chart parameters.

Recommended Q1 implementation

This formulation has several advantages:

1. It treats all maximal minors simultaneously.
2. It handles zero specializations without special conventions.
3. It does not assume that specialized degrees remain equal to generic degrees.
4. It does not require guessing exceptional parameter values.
5. It gives an exact determinantal description of the good-specialization locus.

The \\(D=0\\) case is separate and trivial: all the minors are constant in \\(\lambda\\), and the gcd is \\(1\\) exactly when at least one specialized minor is nonzero.

### 6.1 What this means for the current open problem

Your question III.1(a) can therefore be replaced by the following finite algebraic problem:

> # Given the polynomial coefficient matrix \\(M(\theta)\\), determine whether there exists an admissible parameter point \\(\theta\\) such that \\[ \operatornameM(\theta)
>
> \operatorname[M(\theta)\mid e_0].\
> \\]

The admissibility equations for \\((5a)\\), chart denominators, and full-rank requirements are simply added to the parameter constraints.

This is more robust than trying to list zeros of the leading coefficient of the generic gcd. In particular, it incorporates the degree drops of individual minors automatically.

It also gives a direct way to study the geometry of the spectral-feasible locus: partition parameter space according to the rank of \\(M(\theta)\\), and impose the rank equality in \\((\*)\\).

There is a caveat for computational complexity: the matrix \\(M(\theta)\\) has \\(ND\\) columns, where \\(N\\) is the number of maximal minors. If \\(N\\) is exponentially large in the input dimensions, this is an exact finite formulation but not yet a polynomial-size complexity certificate. That issue is separate from the correctness of the formulation.

## 7. Revised recommendations for the next phase

I would now prioritize the work as follows.

Priority 1 — Complete the specialization criterion

Do next

Implement the coefficient-matrix condition \\((\*)\\). Test it against the current gcd computation on every existing example, including the two deliberately failing pencils and the \\(n=6\\) example.

Priority 2 — Reanalyse the six \\(q_0\\) examples

Do next

Compute the algebraically admissible locus first, identify its components, and then determine the spectral-feasible subset on each component. This will tell you whether the reported generic-gcd phenomenon is genuinely a property of the admissible family.

Priority 3 — Write the short note

Proceed

Do not wait for the complete complexity analysis. The dimension obstruction and the \\(n=6\\) counterexample already provide a coherent mathematical narrative. Include the drop-locus observation as a qualified computational remark.

Priority 4 — Investigate complexity

Defer

First determine whether the determinantal/Bézout formulation has polynomial encoding size. Then consider a hardness reduction. Do not infer hardness merely from the existence of a polynomial-system formulation.

### 7.1 Specific computational checks I would add

For every chart or admissible branch, record:

- the number of maximal minors \\(N\\) and the uniform degree bound \\(D\\);
- the coefficient matrix \\(M(\theta)\\);
- the generic ranks of \\(M(\theta)\\) and \\([M(\theta)\mid e_0]\\);
- the equations defining the \\((5a)\\)-locus;
- the equations and inequations defining the spectral-feasible locus;
- the real and rational feasibility status, separately.

For the \\(n=6\\) counterexample, this should give a particularly useful independent certificate: the system consisting of the \\((5a)\\)-constraints and the rank equality \\((\*)\\) should have no real solution on any of the relevant charts.

That would be a direct algebraic-geometry certificate of whole-family spectral infeasibility, without relying on the generic gcd or on a projective image argument.

## 8. Final assessment

The project has reached a point where the main mathematical results and the main computational bottleneck are reasonably well separated.

| Topic                        | My assessment                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------------- |
| Nullspace-pencil criterion   | Correct primary spectral test; consistent with the 2026 preprint                      |
| Dimension obstruction        | Worth retaining as a principal result, with hypotheses explicit                       |
| \\(n=6\\) counterexample     | Stronger now; suitable as a principal result if all chart certificates are documented |
| Generic-gcd-drop observation | Interesting, but currently empirical                                                  |
| Q1 specialization problem    | Has a direct solution through a bounded-degree Bézout coefficient matrix              |
| Algebraic complexity         | Natural direction, but polynomial-size encoding still needs justification             |
| Hardness reduction           | Premature, but not ruled out                                                          |
| Short note                   | Ready to draft, provided the computational certificates are made reproducible         |

The most important conceptual point is this:

The generic gcd is not the decision object. The specialized Bézout identity is.

Your earlier approach asked whether the generic gcd could be used to predict every specialization. The report has correctly exposed why that is unreliable. The coefficient-matrix formulation changes the question into an exact rank-feasibility problem that treats exceptional points on the same footing as generic ones.

I would make that the immediate next technical step. It is likely to resolve the current open problem III.1(a), or at least reduce it to a well-defined real algebraic feasibility problem with a precise certificate structure.

Finally, the literature comparison should be stated carefully in the note: the 2026 preprint already supplies the all-order nullspace and Grassmann-chart framework, including the order interval and the fact that spectral feasibility need not be monotone. Your strongest potential contribution is therefore not the chart framework itself, but the additional dimension obstruction, the exact \\(n=6\\) whole-family counterexample, and possibly a new analysis of the specialization geometry of the spectral-feasible locus.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+2



The report's corrections are a positive sign: it is now distinguishing generic calculations, exact certificates, finite sampling, and conjectural patterns instead of treating them as interchangeable. That discipline will matter more than adding another large batch of numerical examples.