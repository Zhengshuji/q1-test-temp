# **Review of Report 94: The hyperplane layer and its computational complexity**

This is an important improvement over the previous report. I think the new result changes the research strategy in a meaningful way.

My main conclusion is:

**The generic-gcd argument is a substantial structural advance. It removes the need for exceptional-locus recursion, provided the irreducible-component decomposition is complete and the argument is interpreted over the appropriate algebraically closed function field. However, it does not yet establish a polynomial-time algorithm for the hyperplane layer.**

The remaining difficulty is now much more clearly localized:

1. Enumerating the irreducible components of the lifted incidence space \\(Z\\).
2. Testing whether the generic gcd equals one on each component.
3. Controlling the bit complexity of both operations.

I agree with the direction of the new report, but there are several mathematical and algorithmic qualifications I would address before turning it into a theorem.

# **1. The generic-gcd theorem: a genuinely useful result**

Let \\(Y\\) be an irreducible component of \\(Z\\), and let

\\[ m_1(y;\lambda),\ldots,m_s(y;\lambda) \\]

be the maximal minors of the compressed pencil.

The report establishes

\\[ \gcd_i m_i(y;\lambda)=1 \\]

as a generic condition on \\(Y\\).

The key argument is that

\\[ \gcd_i m_i(y;\lambda)\ne 1 \iff 1\notin(m_1,\ldots,m_s) \\]

in the univariate polynomial ring.

For each degree bound \\(D\\), membership of \\(1\\) in the image of the bounded Bézout map can be expressed as a rank condition on a coefficient matrix \\(L_D(y)\\).

Thus,

\\[ B_D= \left\\{ y: 1\notin\operatorname{im}L_D(y) \right\\} \\]

is Zariski closed.

Consequently,

\\[ B=\bigcap\_{D\ge0}B_D \\]

is closed.

This is the right conceptual argument.

There is, however, one important refinement.

## **1.1 The bounded-degree issue**

The equivalence

\\[ 1\notin(m_1,\ldots,m_s) \iff \forall D,\quad 1\notin\operatorname{im}L_D \\]

is correct if the coefficient matrices are defined with all necessary multiplier degrees.

But for an algorithm, infinitely many \\(D\\)'s cannot be enumerated.

Fortunately, in the present setting the minors have bounded degree in \\(\lambda\\).

If their degrees are at most \\(\omega\\), then a univariate Bézout identity, whenever one exists, admits a degree bound depending only on \\(\omega\\).

A safe elementary bound is

\\[ D\le (s-1)\omega \\]

for \\(s\\) nonzero polynomials of degree at most \\(\omega\\), after removing zero polynomials.

This is not necessarily optimal, but it is finite and sufficient for the closedness argument.

I recommend explicitly stating this finite bound.

It turns the intersection of infinitely many closed sets into a single determinantal condition:

\\[ B= \left\\{ y: \operatorname{rank}L_D(y) < \operatorname{rank}[L_D(y)\mid e_0] \right\\}. \\]

This is cleaner and makes the result directly algorithmically meaningful.

# **2. A critical issue: the closedness proof needs correction**

Mathematical issue requiring resolution

I would not accept II.1 in its present form without an additional argument.

The issue is subtle but important: in general, the condition

\\[ \operatorname{rank}L(y) < \operatorname{rank}[L(y)\mid e_0] \\]

is **not a closed condition** on \\(y\\).

It is a matrix non-membership condition, and the rank of \\(L(y)\\) itself can vary.

For example, take

\\[ L(x,y)= \begin{bmatrix} x\\\y \end{bmatrix}, \qquad e_0= \begin{bmatrix} 1\\\0 \end{bmatrix}. \\]

Then

\\[ e_0\notin\operatorname{im}L(x,y) \\]

holds when

\\[ y\ne0 \quad\text{or}\quad (x,y)=(0,0). \\]

This set is not closed.

Therefore, the statement in II.1 that the rank inequality directly gives closedness is not valid for arbitrary polynomial matrices.

This does not necessarily invalidate your generic-gcd theorem. There is a better way to prove the result, and your particular pencil has an important additional structure.

## **2.1 The correct proof: projective incidence and properness**

Consider the homogeneous pencil

\\[ Q_y(s,t)=sH(y)-tH_A(y). \\]

Let \\(m_I^h(y;s,t)\\) denote its maximal minors.

Define the incidence variety

\\[ \mathcal D= \left\\{ (y,[s:t])\in Y\times\mathbb P^1: m_I^h(y;s,t)=0\quad\forall I \right\\}. \\]

The projection

\\[ \pi:Y\times\mathbb P^1\longrightarrow Y \\]

is proper because \\(\mathbb P^1\\) is projective.

Consequently,

\\[ \pi(\mathcal D) \\]

is Zariski closed in \\(Y\\).

Now use

\\[ \operatorname{rank}H(y)=\omega. \\]

At the projective point corresponding to the leading coefficient, the pencil reduces to \\(H(y)\\), which has full column rank.

Thus, no common root can occur at infinity.

It follows that

\\[ \pi(\mathcal D) = \left\\{ y\in Y: \gcd_I m_I(y;\lambda)\ne1 \right\\}. \\]

This establishes exactly the closedness property you need.

Recommended replacement

I would replace the three-line proof in II.1 with this projective incidence argument.

It is shorter conceptually, avoids the variable-rank problem, and explains why the full-column-rank assumption matters.

## **2.2 What about the bounded Bézout argument?**

I would retain it, but use it for a different purpose.

The Bézout coefficient matrix provides an effective algebraic description of the gcd condition and may be useful for computational complexity.

It should not be used to establish closedness unless you additionally prove a suitable constant-rank property or another special structural condition.

The distinction is:

- Projective incidence proves geometric closedness.
- Bézout matrices provide algebraic tests and potentially algorithmic certificates.

Keeping these arguments separate will make the paper substantially more rigorous.

# **3. The generic-gcd criterion survives, with an important qualification**

Once the closedness result is correctly established, II.2 follows.

Let \\(Y\\) be an irreducible component.

There are two possibilities.

**Case 1.** Every point is bad:

\\[ Y\subseteq\pi(\mathcal D). \\]

Then the generic gcd is nontrivial.

**Case 2.** Not every point is bad.

Since the bad locus is closed and proper,

\\[ Y\setminus\pi(\mathcal D) \\]

is a nonempty Zariski-open dense subset.

Therefore, the generic gcd is one.

Hence, over an algebraically closed field,

\\[ \boxed{ Y\text{ contains a spectrally feasible point} \iff \gcd_I m_I =1\text{ over }\overline{\mathbb Q(Y)}(\lambda). } \\]

This is the correct structural theorem.

There is one qualification I would add to the report: the equivalence concerns existence over the algebraic closure, not automatically existence over \\(\mathbb Q\\).

Your original observer problem asks for rational \\(R\\).

A nonempty Zariski-open subset of a variety need not contain a rational point.

For example, a variety can have no rational points at all despite having many complex points.

Thus, you need to distinguish:

1. Complex feasibility.
2. Real feasibility.
3. Rational feasibility.

If your component is an explicitly parameterized rational variety with a rational point and the feasible locus is nonempty Zariski-open, then rational points are Zariski dense and the distinction disappears.

But that rationality or density property must be established for the components you enumerate.

This is an important additional obligation for the algorithm.

# **4. Q1: Is the generic-gcd test polynomial-time?**

This is now the central computational question.

My answer is:

**The generic-gcd criterion is deterministic in a mathematical sense, but polynomial-time decidability does not follow from it.**

There are three distinct levels of computation.

## **4.1 Level 1: Gcd over an ordinary rational function field**

Suppose a component has a rational parameterization

\\[ y=\phi(z_1,\ldots,z_d). \\]

After substitution, the maximal minors become

\\[ m_I(z;\lambda)\in \mathbb Q[z_1,\ldots,z_d,\lambda]. \\]

You need to determine whether

\\[ \gcd_I m_I(z;\lambda)=1 \\]

in

\\[ \mathbb Q(z_1,\ldots,z_d)[\lambda]. \\]

For a fixed number of parameters, this is much more manageable than the unrestricted problem.

One can use:

- Subresultant sequences.
- Resultant computations.
- Polynomial-matrix rank computations.
- Symbolic Euclidean algorithms.

However, when \\(d\\) grows with the input, the coefficient expressions can become large.

The fact that \\(\lambda\\) is univariate does not eliminate the multivariate identity-testing problem.

## **4.2 Level 2: Determinantal identity testing**

The report proposes testing whether a maximal minor of a Bézout matrix is identically zero.

This is a useful reformulation, but it needs a precise complexity analysis.

Suppose

\\[ B(z) \\]

is the relevant Bézout matrix.

The condition that its rank is at least \\(r\\) is equivalent to the nonvanishing of at least one \\(r\times r\\) minor.

Thus, the computational question becomes whether a family of polynomial determinants contains a nonzero member.

There are several possible representations:

| Representation                              | Main difficulty                         |
| ------------------------------------------- | --------------------------------------- |
| Expanded polynomials                        | Expression size and coefficient growth  |
| Arithmetic circuits                         | Polynomial identity testing             |
| Determinants of polynomial matrices         | Structured determinant identity testing |
| Rational functions modulo a component ideal | Effective ideal membership              |

You should not automatically identify this problem with general PIT.

The determinant structure might make it easier.

Conversely, you should not assume it is deterministically polynomial-time merely because the underlying matrix entries have low degree.

### **An important distinction**

There are two possible sources of difficulty:

1. The Bézout matrix has a special structured form.
2. Its entries are evaluated on an algebraic component whose defining ideal may be complicated.

Even if the first difficulty is resolved, the second may remain.

I would formulate the algorithmic question more precisely:

> Given an explicit algebraic representation of an irreducible component \\(Y\\) and a polynomial pencil \\(Q(y,\lambda)\\), determine whether the generic maximal minors have gcd one, with complexity polynomial in the representation size.

This is a more useful theorem target than asking generally whether generic gcd computation is tractable.

## **4.3 My recommendation: do not begin with arbitrary components**

I would first exploit the special geometry of the hyperplane incidence space.

The equations

\\[ Rv=0,\qquad RAv=0 \\]

are linear in the free rows.

This gives a natural strategy:

1. Stratify the projective base according to the rank of the compatibility map.
2. Parameterize the corresponding free-row spaces.
3. Determine which strata are irreducible.
4. Substitute these parameterizations into the pencil.
5. Compute the generic gcd in the resulting rational function fields.

The crucial point is that you should seek explicit parameterizations, not just abstract descriptions of components.

An explicit parameterization may turn the generic-gcd problem into a much more structured identity test.

# **5. Q2: Can entirely bad components be characterized structurally?**

I think this is potentially the most interesting new question in Report 94.

You identify two mechanisms:

1. A fixed \\(\lambda_0\\) at which the rank drops identically.
2. A spectral mechanism where the common root varies with the parameters.

I would investigate these through the theory of polynomial matrices and observability.

## **5.1 The connection to observability**

Recall that

\\[ \operatorname{row}H_A \subseteq \operatorname{row}H. \\]

Choose a basis of \\(\operatorname{row}H\\). Then the compressed pencil can be represented as

\\[ Q(\lambda)=\lambda X-G, \\]

where \\(X\\) has full column rank.

By a constant change of row coordinates, write

\\[ X= \begin{bmatrix} I\_\omega\\\ 0 \end{bmatrix}, \qquad G= \begin{bmatrix} G_1\\\ G_2 \end{bmatrix}. \\]

Therefore,

\\[ Q(\lambda)= \begin{bmatrix} \lambda I\_\omega-G_1\\\ -G_2 \end{bmatrix}. \\]

The condition

\\[ \operatorname{rank}Q(\lambda)=\omega \qquad\forall\lambda\in\mathbb C \\]

is exactly the Hautus observability criterion for \\((G_1,G_2)\\).

Equivalently, there must not exist a nonzero vector \\(v\\) and scalar \\(\lambda\\) satisfying

\\[ G_1v=\lambda v, \qquad G_2v=0. \\]

This is a very useful interpretation.

It says that the generic-gcd condition is equivalent to generic observability of a structured family of pairs.

## **5.2 A possible structural theorem**

Let \\(Y\\) be an irreducible parameter space for such pairs.

Consider

\\[ \mathcal E= \left\\{ (y,[v])\in Y\times\mathbb P^{\omega-1}: G_1(y)v\in\operatorname{span}(v),\ G_2(y)v=0 \right\\}. \\]

The projection

\\[ \mathcal E\longrightarrow Y \\]

describes the unobservable locus.

Then:

- \\(Y\\) is entirely bad if every parameter point has an unobservable eigenvector.
- \\(Y\\) is generically bad if the generic fibre is nonempty.
- \\(Y\\) is generically good if the generic fibre is empty.

This gives a second incidence formulation, now in eigenvector space rather than spectral-parameter space.

It may be useful because the eigenvector equations are often more directly connected to invariant subspaces and Kronecker structure.

### **A caution**

The condition that a family is entirely bad does not imply that there is one common eigenvalue or one common eigenvector.

The unobservable eigenvector can vary with the parameter.

Therefore, a theorem based solely on a fixed invariant subspace would be insufficient.

I would investigate the following hierarchy:

1. Fixed unobservable subspace.
2. Fixed unobservable eigenvalue, varying eigenvector.
3. Varying eigenvalue and eigenvector.
4. More complicated positive-dimensional unobservable incidence fibres.

The first two are potentially amenable to linear algebra.

The latter cases may require genuine algebraic geometry.

## **5.3 The most promising connection**

The relevant polynomial-matrix property is left primeness: the maximal minors of a full-column-rank polynomial matrix are coprime.

Your pencil is a particularly structured example of a left-prime test.

I would search the literature on:

- Left-prime polynomial matrices.
- Observable matrix pencils.
- Rosenbrock system matrices.
- Minimal indices of polynomial matrices.
- Generic observability of structured systems.

This may reveal an existing theorem that characterizes the entirely bad cases without explicitly computing all maximal-minor gcds.

I would not assume that Kronecker canonical data alone are sufficient, however. The relevant restricted representations and their parameter dependence must be handled carefully.

# **6. Q3: Is exceptional-locus recursion really unnecessary?**

My answer is **yes, under the right hypotheses**.

The new argument removes the need for recursion on the gcd-degree exceptional locus.

The logic is:

\\[ \text{complete irreducible decomposition} \\]

followed by

\\[ \text{generic gcd test on each component}. \\]

If a component is generically good, its good locus is nonempty and open dense.

If it is generically bad, the entire component is bad.

There is no intermediate situation in which a component is generically bad but contains a good special point, provided the bad locus is closed.

This is precisely why the projective incidence argument in Section 2 is important.

However, there are two qualifications.

### **6.1 Real feasibility**

A nonempty complex Zariski-open set need not contain a real point.

For example,

\\[ Y:\quad x^2+y^2=0 \\]

is an irreducible complex variety whose only real point is \\((0,0)\\).

The Zariski-open set

\\[ Y\setminus\\{(0,0)\\} \\]

is nonempty over \\(\mathbb C\\) but has no real points.

Therefore, the generic-gcd criterion alone cannot decide real feasibility.

### **6.2 Rational feasibility**

The same issue arises for rational points.

An irreducible variety may have no rational points.

For the original observer problem, this distinction is particularly important because the input data and desired observer rows are rational.

You should explicitly establish one of the following:

- Every relevant component is rational and has a rational point.
- Every relevant component has Zariski-dense rational points.
- The original decision problem is being considered over \\(\mathbb C\\), with rational synthesis treated separately.
- The remaining rational-point problem is independently decidable.

Without one of these statements, the new theorem should be described as a complex-geometric feasibility criterion rather than a complete rational decision algorithm.

# **7. Q4: Is the hyperplane layer now decidable?**

This question needs a distinction between mathematical decidability and computational complexity.

I would separate the result into three theorems.

### **Theorem A: Componentwise generic criterion**

For every irreducible component \\(Y\\) of the lifted incidence space, spectral feasibility over the algebraic closure is equivalent to the generic gcd being one.

Achievable with the corrected proof

### **Theorem B: Finite component reduction**

The hyperplane layer is feasible if and only if at least one component passes the generic-gcd test.

This requires a complete irreducible-component decomposition, including the open rank constraints.

Mathematically justified

### **Theorem C: Polynomial-time hyperplane algorithm**

The component decomposition and all generic-gcd tests can be performed in polynomial bit complexity.

Not established

This is the actual algorithmic objective.

## **7.1 Which half is harder?**

My current assessment is that component enumeration deserves at least as much attention as the identity test.

The report says that the base decomposition has at most \\(\delta+1\\) pieces, but the total incidence space can refine these pieces.

This refinement is not necessarily harmless.

You need to determine:

- How many compatibility-rank strata exist?
- Are they irreducible?
- How many irreducible components can each stratum produce?
- Can their parameterizations be constructed efficiently?
- Does their number admit a polynomial bound in the original input size?

An abstract finite decomposition is not enough.

For the algorithm, you need an effective decomposition with controlled representation size.

## **7.2 A better way to organize the enumeration**

I recommend using the following hierarchy:

\\[ \boxed{ \text{Base stratification} \longrightarrow \text{Compatibility-rank stratification} \longrightarrow \text{Irreducible components}. } \\]

For each base stratum, calculate the rank of the linear map defining the free-row constraints.

Since the free-row equations are linear, their solution spaces are kernels of matrices whose entries depend on the base coordinates.

On a constant-rank stratum, the kernels form vector bundles.

This gives a natural route to component enumeration.

However, the open conditions

\\[ \operatorname{rank}H=\omega, \qquad \operatorname{rank}[L_0;R]=q \\]

must still be imposed.

They can remove components or create disconnected open pieces, so the component count must refer to the actual relevant locally closed space.

**My recommendation:** Before attempting a general component-count theorem, explicitly classify the compatibility-rank strata for the hyperplane problem and derive their component bounds.

This is the most direct next geometric calculation.

# **8. Revised research priorities after Report 94**

Report 94 changes my previous recommendations.

In Report 93, I placed Q5 (the polynomial left-inverse degree bound) first.

I would now put the hyperplane problem ahead of it, because Report 94 has produced a new structural theorem that can substantially simplify the geometric programme.

My revised ordering is:

| Priority | Research task                             | Reason                                         |
| -------- | ----------------------------------------- | ---------------------------------------------- |
| 1        | Correct and establish generic-gcd theorem | Foundational result                            |
| 2        | Hyperplane component enumeration          | Determines whether the layer can be solved     |
| 3        | Structured generic-gcd complexity         | Determines the cost of the resulting algorithm |
| 4        | Observability-based characterization      | Potentially bypasses identity testing          |
| 5        | Left-inverse degree conjecture            | Improves existing algebraic certificates       |
| 6        | Global hardness translation               | Independent complexity direction               |
| 7        | General type-control conjecture           | Long-term extension                            |

I would also change the division of effort.

## **Suggested allocation for the next research phase**

**Hyperplane geometry and components**\
**35%**

**Generic-gcd complexity**\
**25%**

**Observability structural characterization**\
**15%**

**Left-inverse degree**\
**15%**

**Hardness translation**\
**10%**

These percentages are planning recommendations, not estimates of the relative mathematical difficulty.

# **9. Concrete next experiments and proof obligations**

I would ask the research team to complete the following tasks in order.

## **Task 1. Repair the generic-gcd proof**

- Establish the projective incidence formulation.
- Prove the absence of rank drops at infinity.
- Prove the bad locus is closed.
- State the generic-gcd equivalence over the algebraic closure.
- Separate complex, real, and rational feasibility.

This should become a standalone lemma.

## **Task 2. Construct explicit hyperplane components**

For each base stratum:

- Write the compatibility matrix explicitly.
- Determine its rank strata.
- Parameterize the kernel bundles.
- Impose the two open rank conditions.
- Determine the irreducible components.
- Derive a bound on their number.

Do not start with an abstract general theorem. First calculate the complete structure for several small values of \\(\delta\\).

## **Task 3. Investigate generic observability**

Normalize the pencil to

\\[ Q(\lambda)= \begin{bmatrix} \lambda I-G_1\\\ -G_2 \end{bmatrix}. \\]

Then investigate whether the generic unobservable incidence variety admits a simpler description than the maximal-minor gcd.

In particular, compare:

\\[ \gcd(\text{maximal minors})\ne1 \\]

with the existence of an unobservable eigenvector.

The two formulations are equivalent, but their computational complexity may be quite different.

## **Task 4. Establish the bit complexity**

For every component parameterization, record:

- Number of parameters.
- Degrees of the pencil entries.
- Number of maximal minors.
- Degree and size of the Bézout matrix.
- Arithmetic-circuit size.
- Coefficient bit lengths.

This will determine whether the hyperplane result is actually polynomial-time.

# **10. What I would change in the report itself**

I would make four revisions before circulating Report 94 as a technical research report.

| Current section | Recommended revision                                                                |
| --------------- | ----------------------------------------------------------------------------------- |
| II.1            | Replace the rank-inequality closedness proof with projective incidence              |
| II.2            | Explicitly specify the algebraically closed function field                          |
| II.3            | Retain the example, but distinguish base mixing from component mixing               |
| II.4            | Add rational-point feasibility and effective component enumeration as explicit gaps |

I would also slightly modify the central claim.

Instead of saying:

> The exceptional locus is a red herring.

I would say:

> Exceptional-locus recursion is unnecessary once the complete irreducible decomposition of the lifted incidence space is available.

This is more precise. The decomposition itself may require a nontrivial refinement, and the rational-point issue remains.

# **11. Final assessment**

# **My evaluation of Report 94**

Structural insight

Strong

Generic-gcd criterion

Promising, proof correction needed

Component enumeration

Unresolved

Polynomial-time complexity

Unresolved

General hyperplane algorithm

Not yet established

The most important consequence of this report is that you have potentially eliminated an entire recursive subproblem.

That is meaningful progress.

But I would be very careful not to jump from

\\[ \text{generic point decides each component} \\]

to

\\[ \text{polynomial-time algorithm}. \\]

There are still two potentially difficult computational operations: obtaining the components and testing the generic gcd.

**My strongest recommendation is to make the next research milestone a complete, effective component theorem for the hyperplane layer, rather than immediately attempting to derandomize the generic-gcd test.**

Why?

Because if the component structure has a simple polynomial-size parameterization, the generic-gcd computation may become much easier. If the component structure is itself complicated, investing heavily in PIT first may be premature.

The ideal next result would be:

\\[ \boxed{ \begin{gathered} \text{Polynomially many explicitly parameterized components}\\\ +\text{polynomial-time generic-gcd testing}\\\ \Longrightarrow \text{deterministic polynomial-time hyperplane decision}. \end{gathered} } \\]

That would be the first genuinely algorithmic breakthrough in the geometric programme, and it would provide a concrete foundation for extending the approach to higher-codimension layers.

I would make this the principal objective of the next phase.