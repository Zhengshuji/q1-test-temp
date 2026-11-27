# Research assessment of the rank-only refutation and the proposed \\(\omega=2\\) route

I have treated `45_rank_only_refuted_and_mismatch.md` as the primary document for this review. Its central observation is important: the reachable family is linear in the design variables, whereas the spectral rank-drop condition is nonlinear. The examples also decisively refute the proposed rank-only criterion at \\(\omega=2\\), within the fixed-\\(U\\) pencil family considered in the report.

My overall recommendation, however, is more qualified than “the evidence now favours hardness.” The refutation establishes that certain ordinary rank invariants do not decide the problem. It does not establish that the problem is hard, nor that the relevant nonlinear condition has enough freedom to encode arbitrary quadratic feasibility. The next step should be to derive the exact algebraic description of the bad locus on the actual observer-induced family, and then test whether its special structure admits a tractable decision procedure or a genuine reduction.

There are also two technical points that deserve correction or sharpening:

1. At \\(q=3,\omega=2\\), the three maximal minors consist of one quadratic and one linear polynomial in \\(\lambda\\), as the report states. But a resultant must be handled carefully when the degree of the linear polynomial drops: a homogeneous resultant can detect a common root at infinity, which is not a finite spectral rank drop.
2. The phrase “a linear subspace of pencils contains a regular pencil” is potentially misleading. For a rectangular pencil, the relevant property is full column rank at every finite \\(\lambda\\), not regularity in the usual square-pencil sense. I recommend defining the problem explicitly rather than relying on “regular.”

I develop these points below, then answer the four questions and give a revised work plan.

## 1. First, correct the algebra in the report

This is the most important technical correction. The report's description of the maximal minors in the \\(q=3,\omega=2\\) case is not correct as written.

Let

\\[ U= \begin{pmatrix} 1&0\\\ 0&1\\\ 0&0 \end{pmatrix}, \qquad G= \begin{pmatrix} a_1&b_1\\\ a_2&b_2\\\ a_3&b_3 \end{pmatrix}, \qquad P(\lambda)=\lambda U-G. \\]

Then

\\[ P(\lambda)= \begin{pmatrix} \lambda-a_1&-b_1\\\ -a_2&\lambda-b_2\\\ -a_3&-b_3 \end{pmatrix}. \\]

There are three \\(2\times2\\) maximal minors, not two:

\\[ \begin{aligned} m\_{12}(\lambda) &=(\lambda-a_1)(\lambda-b_2)-a_2b_1\\\ &=\lambda^2-(a_1+b_2)\lambda+a_1b_2-a_2b_1,\\\\[2mm] m\_{13}(\lambda) &=-b_3\lambda+a_1b_3-b_1a_3,\\\\[2mm] m\_{23}(\lambda) &=a_3\lambda+a_2b_3-a_3b_2. \end{aligned} \\]

Thus the correct description for \\(q=3,\omega=2\\) is

\\[ \boxed{\text{one quadratic minor and two linear minors}.} \\]

More generally, for \\(U=[I_2;0]\in\mathbb C^{q\times2}\\), the maximal minors have the following distribution:

| Rows used                    | Number of minors     | Degree in \\(\lambda\\) |
| ---------------------------- | -------------------- | ----------------------- |
| Both active rows             | \\(1\\)              | \\(2\\)                 |
| One active, one inactive row | \\(2(q-2)\\)         | At most \\(1\\)         |
| Two inactive rows            | \\(\binom{q-2}{2}\\) | \\(0\\)                 |

Consequently, the expression

\\[ 1\text{ quadratic}+(q-2)\text{ linears} \\]

in the report should be replaced by

\\[ \boxed{ 1\text{ quadratic} +2(q-2)\text{ linears} +\binom{q-2}{2}\text{ constants}. } \\]

For \\(q=3\\), this gives exactly one quadratic and two linears.

This is not merely a counting correction. It affects the proposed resultant argument: the bad condition is that all three minors have a common finite root. It is not, in general, just the vanishing of the resultant of one quadratic and one linear polynomial.

### 1.1 The numerical counterexample remains valid

The two matrices in the report are

\\[ G_a= \begin{pmatrix} -1&-1\\\ -1&-1\\\ -1&0 \end{pmatrix}, \qquad G_b= \begin{pmatrix} -1&-1\\\ -1&-1\\\ -1&1 \end{pmatrix}. \\]

For \\(G_a\\),

\\[ m\_{12}=\lambda^2+2\lambda,\qquad m\_{13}=-1,\qquad m\_{23}=-(\lambda+1). \\]

Therefore

\\[ \gcd(m\_{12},m\_{13},m\_{23})=1. \\]

For \\(G_b\\),

\\[ m\_{12}=\lambda^2+2\lambda,\qquad m\_{13}=-(\lambda+2),\qquad m\_{23}=-(\lambda+2), \\]

and hence

\\[ \gcd(m\_{12},m\_{13},m\_{23})=\lambda+2. \\]

So the example correctly demonstrates

\\[ \begin{aligned} &\operatorname{rank}U=2,\quad \operatorname{rank}G_a=\operatorname{rank}G_b=2,\\\ &\operatorname{rank}[U\ G_a] =\operatorname{rank}[U\ G_b]=3, \end{aligned} \\]

while one pencil is feasible and the other is infeasible.

There is a small redundancy in the four-invariant tuple in the report: since \\(U\\) already has full column rank,

\\[ \operatorname{rank}\begin{bmatrix}U\\\G\end{bmatrix}=2 \\]

holds automatically. The meaningful comparison is therefore between the three remaining rank quantities.

Conclusion: the example refutes the sufficiency of these ordinary rank invariants for deciding the spectral property of an individual pencil. It does not refute every possible rank-based or algebraic criterion, and it does not by itself establish that the two examples belong to the same observer-induced reachable family. That last point would need to be checked if the example is to support a theorem specifically about REAL-AUG.

## 2. The right formulation of the spectral property

For a full-column-normal-rank polynomial matrix

\\[ P(\lambda)\in\mathbb C[\lambda]^{q\times\omega}, \qquad q\geq\omega, \\]

the following conditions are equivalent:

1. \\(\operatorname{rank}P(\lambda)=\omega\\) for every \\(\lambda\in\mathbb C\\).
2. The \\(\omega\times\omega\\) maximal minors of \\(P\\) have no common finite root.
3. The gcd of all maximal minors is a nonzero constant.

This property is commonly described as right primeness for a tall polynomial matrix. In particular, it is not the same as regularity of a square pencil. The right-prime terminology and its characterization by maximal minors are standard in the polynomial-matrix literature.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车+1



For the observer problem, this means that the reduced spectral requirement is a right-prime condition on the reduced polynomial matrix.

I recommend using the following terminology consistently:

> A pencil \\(P(\lambda)=\lambda U-G\\), with \\(U\\) of full column rank, is called spectrally feasible if it has full column rank for every finite \\(\lambda\in\mathbb C\\), equivalently if it is right prime.

This avoids the ambiguity of calling a rectangular pencil “regular.”

### 2.1 A more reliable resultant construction

For the \\(q=3,\omega=2\\) case, write the three maximal minors as

\\[ m_1(t,\lambda),\quad m_2(t,\lambda),\quad m_3(t,\lambda), \\]

where \\(t=(t_1,\ldots,t_s)\\) denotes affine parameters for the family.

Introduce two independent sets of auxiliary indeterminates

\\[ a=(a_1,a_2,a_3),\qquad b=(b_1,b_2,b_3), \\]

and define

\\[ f_a(t,\lambda)=\sum\_{i=1}^3a_i m_i(t,\lambda), \qquad f_b(t,\lambda)=\sum\_{i=1}^3b_i m_i(t,\lambda). \\]

Then form

\\[ \mathcal R(t,a,b) = \operatorname{Res}\_{\lambda}(f_a,f_b). \\]

Over the rational function field in the parameters and auxiliary variables, generic linear combinations of a finite family of univariate polynomials have the same gcd as the entire family. Thus, provided the leading-rank condition on \\(U\\) is retained,

\\[ \boxed{ \mathcal R\not\equiv0 \quad\Longleftrightarrow\quad \gcd(m_1,m_2,m_3)=1 \text{ over }\mathbb C(t)[\lambda]. } \\]

The reason is straightforward:

- If the three minors have a nonconstant common factor, every linear combination has that factor, so every pair of combinations has a common root.
- If their gcd is \\(1\\), generic combinations are coprime, so their resultant is nonzero.

This is preferable to trying to formulate a single resultant using one selected quadratic and one selected linear minor. The latter approach needs a separate treatment of cases in which the selected linear polynomial vanishes or drops degree.

There is also a useful degree estimate. Each maximal minor is quadratic in the affine parameters \\(t\\). Therefore each coefficient of \\(f_a\\) and \\(f_b\\) has degree at most \\(2\\) in \\(t\\). The Sylvester resultant of two polynomials of degree at most \\(2\\) is a \\(4\times4\\) determinant, so

\\[ \boxed{\deg_t\mathcal R\leq 8.} \\]

The bound is a total-degree bound; cancellations can make the actual degree smaller.

A caveat is necessary: a homogeneous resultant can detect a common root at infinity. In the present setup, \\(U\\) has full column rank, so at least one maximal minor of the leading coefficient matrix is nonzero. Generic combinations avoid a common root at infinity. Nevertheless, an implementation should use the homogeneous formulation with this leading-rank condition explicitly checked, or use subresultants/gcd computations that directly test finite common roots.

## 3. Question 1: Is the outer linear-space problem already known?

The problem in the report can be formulated more precisely as follows.

Affine pencil-family right-prime existence problem

Input: an affine-linear family

\\[ P_t(\lambda)=\lambda U(t)-G(t), \qquad t\in\mathbb F^s, \\]

where \\(U(t),G(t)\\) depend affinely on \\(t\\), and \\(U(t)\\) has full column rank on the parameter domain \\(D\\).

Question:

\\[ \exists t\in D:\quad \operatorname{rank}P_t(\lambda)=\omega \quad\text{for every }\lambda\in\overline{\mathbb F}? \\]

Equivalently: does the affine family contain a right-prime pencil?

I did not find an exact standard name or a directly applicable general complexity classification for this outer-family problem in the literature searched. There are, however, several nearby problems that should be distinguished carefully.

### 3.1 Relation to Edmonds' problem and symbolic determinant identity testing

Edmonds' problem, also called symbolic determinant identity testing in this context, asks whether a linear space of square matrices contains a nonsingular matrix. Its rectangular analogue asks for the maximum rank attained by a matrix in a linear matrix space.

This is structurally relevant because both problems concern the intersection of a linear space with a determinantal rank-deficiency locus. The literature contains randomized algorithms and deterministic algorithms for important special classes of matrix spaces. For example, Ivanyos, Karpinski, Qiao, and Santha study symbolic matrix rank and symbolic determinant identity testing, with deterministic algorithms for special classes such as spaces spanned by rank-one matrices or triangularizable matrices.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://eccc.weizmann.ac.il\&sz=32)

eccc.weizmann.ac.il+1



But there is an important difference:

- Edmonds asks whether one matrix in a linear space is nonsingular.
- Your problem asks whether one pencil in a linear family is full column rank at every value of a second variable \\(\lambda\\).

The latter is a polynomial-matrix primeness condition, not an ordinary matrix nonsingularity condition.

Thus Edmonds' problem is a useful point of comparison, but it is not an exact identification.

### 3.2 Relation to rectangular matrix-pencil eigenvalue problems

The multiparameter matrix-pencil problem studied by Gungah, Alsubaie, and Jaimoukha asks for parameter values at which a given rectangular pencil loses column rank, together with corresponding eigenvectors. This is a problem about the rank-drop parameters of a fixed pencil, not the existence of a right-prime member in an outer family of pencils.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://epubs.siam.org\&sz=32)

工业与应用数学学会+1



The distinction is:

\\[ \begin{array}{ll} \text{Inner problem:} & \text{Given }P(\lambda),\text{ find }\lambda\text{ where rank drops};\\\\[1mm] \text{Your outer problem:} & \text{Given a family }P_t(\lambda),\text{ decide whether some }t \text{ has no finite rank drop}. \end{array} \\]

The inner problem is well studied. The outer problem has a different quantifier structure.

### 3.3 A useful working name

For papers and internal reports, I would use:

Linear-space avoidance of the right-nonprime pencil locus.

This describes the geometry accurately without claiming that the problem has a standard complexity name.

Let

\\[ \mathcal N\_{\omega} = \\{(U,G):\exists\lambda\in\mathbb C,\  \operatorname{rank}(\lambda U-G)<\omega\\} \\]

on the open set where \\(U\\) has full column rank. The outer problem is whether the affine family \\(\Lambda\\) is contained in \\(\mathcal N\_\omega\\).

That formulation leads directly to the main structural result.

## 4. The crucial point: the affine-family problem is generically decidable

This is the most important reason I would not begin a hardness reduction at \\(k=\omega=2\\).

Let \\(t\in\mathbb C^s\\) parameterize an affine family

\\[ P_t(\lambda)=\lambda U(t)-G(t), \\]

and suppose the domain

\\[ D=\\{t:\operatorname{rank}U(t)=\omega\\} \\]

is nonempty.

Define the bad set

\\[ \mathcal B= \\{t\in D:\exists\lambda\in\mathbb C,\ \operatorname{rank}P_t(\lambda)<\omega\\}. \\]

### Theorem: genericity of spectral feasibility on an affine family

The set \\(\mathcal B\\) is closed relative to \\(D\\). Since \\(D\\) is a nonempty Zariski-open subset of an affine space, it is irreducible. Consequently, exactly one of the following holds:

1. \\(\mathcal B=D\\): every member is spectrally bad.
2. \\(D\setminus\mathcal B\\) is nonempty and Zariski open dense in \\(D\\): a generic member is spectrally feasible.

In particular,

\\[ \boxed{ \exists t\in D:\ P_t\text{ is spectrally feasible} \iff \text{the generic member is spectrally feasible}. } \\]

Proof. Homogenize the pencil:

\\[ P_t^h(\alpha,\beta)=\alpha U(t)-\beta G(t). \\]

The condition that this matrix have rank less than \\(\omega\\) is defined by the vanishing of all its \\(\omega\times\omega\\) minors. Hence the incidence set

\\[ \mathcal I= \left\\{(t,[\alpha:\beta])\in D\times\mathbb P^1: \operatorname{rank}P_t^h(\alpha,\beta)<\omega \right\\} \\]

is closed.

Projection from \\(D\times\mathbb P^1\\) to \\(D\\) is proper because \\(\mathbb P^1\\) is projective. Therefore its image \\(\mathcal B\\) is closed.

At \\([1:0]\\), the homogenized pencil equals \\(U(t)\\), which has full column rank throughout \\(D\\). Thus every rank drop in the projective parameter occurs at a finite \\(\lambda\\). This proves that the projection describes exactly the bad set in question.

Finally, a closed subset of an irreducible space is either the whole space or a proper closed subset. In the latter case its complement is nonempty open dense. \\(\square\\)

### 4.1 Generic gcd criterion

Let \\(F=\mathbb C(t_1,\ldots,t_s)\\) be the rational function field of the affine parameter space. The preceding theorem gives the equivalent criterion

\\[ \boxed{ \exists t\in D\text{ with }P_t\text{ right prime} \iff \gcd\\{\omega\text{-minors of }P_t(\lambda)\\}=1 \text{ in }F[\lambda]. } \\]

This changes the nature of the outer problem. Instead of searching for one exceptional parameter value \\(t\\), one tests the generic pencil over the function field.

For \\(q=3,\omega=2\\), the generic resultant construction above gives a concrete exact test.

### 4.2 Complexity consequence at \\(\omega=2\\)

For a fixed \\(\omega=2\\), the number of maximal minors is

\\[ M=\binom q2=O(q^2). \\]

The resultant of two generic linear combinations has degree at most \\(2\\) in each of the two sets of combination coefficients, and degree at most \\(8\\) in the original affine parameters.

Consequently, its coefficient expansion has polynomial size in the number of affine parameters and in \\(q\\), when \\(\omega=2\\) is fixed. With rational input and exact arithmetic, this gives a deterministic polynomial-time route for this affine-family subproblem.

More generally, for each fixed \\(\omega\\), the analogous generic-combination resultant has degree at most \\(2\omega^2\\) in the affine parameters. Its expansion is polynomial-size when \\(\omega\\) is fixed, although the polynomial exponent grows with \\(\omega\\).

This is a meaningful positive algorithmic result. It does not establish polynomial-time solvability when \\(\omega\\) is part of the input and grows with the instance.

### 4.3 Why this matters specifically for \\(k=\omega=2\\)

When

\\[ k=\omega=2, \\]

the matrix \\(H(R)\\) has two columns and is required to have rank \\(2\\). Therefore

\\[ \ker H(R)=\\{0\\}. \\]

The condition

\\[ \ker H(R)\subseteq\ker H_A(R) \\]

is automatic. In other words, condition (5a) imposes no further restriction on this rank stratum.

Moreover, \\(H(R)\\) and \\(H_A(R)\\) depend affinely on \\(R\\). Thus the rank-two domain is simply the open full-column-rank locus of an affine family.

It follows that the genericity theorem applies directly to this case. In particular, the specific minimal case

\\[ q=3,\qquad k=\omega=2 \\]

is not a promising place to search for a general hardness reduction. The spectral feasibility question there can be attacked by the generic gcd/resultant test.

This is a stronger conclusion than merely saying that the numerical examples are small. It says that the outer existence question has a generic algebraic characterization in this regime.

## 5. Question 2: Which direction should be pursued at \\(\omega=2\\)?

My recommendation is to separate two cases.

### Case A: \\(k=\omega=2\\)

Prioritize the algorithmic approach.

The fixed-\\(U\\) example is useful for refuting rank-only criteria, but it should not be treated as a promising hardness model. The reason is that the admissible domain is an open subset of an affine space and the bad locus is closed. Hence feasibility is generic.

For this case, I would do the following:

1. Derive the exact generic gcd criterion for the affine pencil family.
2. Implement the generic resultant construction.
3. Verify the degree-\\(8\\) bound and test it against exhaustive small examples.
4. Compare the resultant test against the direct gcd test at randomly selected rational parameter values.
5. Prove that the actual observer-induced map \\((H,H_A)\\) is represented by the affine parameterization used in the implementation.

The last point is important. The generic resultant argument is only as good as the parameterization to which it is applied.

### Case B: \\(k>\omega\\)

This is where the difficult part of REAL-AUG can remain.

For fixed \\(\omega\\), the admissible locus is

\\[ \mathcal X\_\omega = \left\\{ R: \operatorname{rank}H(R)=\omega,\quad \operatorname{rank} \begin{bmatrix} H(R)\\\H_A(R) \end{bmatrix} =\omega \right\\}. \\]

Equivalently,

\\[ \operatorname{rank}H(R)=\omega, \qquad \ker H(R)\subseteq\ker H_A(R). \\]

The reachable pairs \\((H,H_A)\\) form an affine-linear family, but the second condition is not generally affine-linear in \\((H,H_A)\\). It is a determinantal condition. In particular,

\\[ \operatorname{rank} \begin{bmatrix}H\\\H_A\end{bmatrix} \leq\omega \\]

is imposed by the vanishing of all \\((\omega+1)\\)-minors.

Thus the admissible locus is generally locally closed and determinantal, not an affine-linear space.

This is where the proposed hardness route has a plausible target. The key issue is no longer simply the interaction of a linear family with a quadratic spectral condition. It is the interaction of:

1. an affine-linear reachable-pair space;
2. a determinantal admissibility constraint;
3. an open spectral-feasibility condition inside the admissible locus.

The algebraic geometry of this intersection is potentially much richer than that of the affine family considered in Case A.

### 5.1 Why the admissible locus is not generally a finite union of affine-linear pieces

A rank condition such as

\\[ \operatorname{rank}M(t)\leq\omega \\]

defines a determinantal variety. Such varieties are generally nonlinear and irreducible, rather than finite unions of affine-linear subspaces.

The observer-induced linear structure may impose special simplifications, so one should not claim that every instance has a complicated determinantal variety. But there is no general reason to expect the admissible locus to split into finitely many affine-linear pieces.

A more natural replacement is:

- use pivot charts to cover the fixed-rank locus;
- describe the admissibility constraints algebraically on each chart;
- decompose the resulting algebraic set into irreducible components, at least in the small cases under investigation;
- test the generic spectral gcd on each component.

This preserves the useful genericity principle without making the unjustified assumption that the admissible set is affine-linear.

### 5.2 Componentwise genericity

Let \\(X_i\\) be an irreducible component of the complex admissible locus, and let

\\[ F_i=\mathbb C(X_i) \\]

be its function field.

On a suitable pivot chart, form the reduced pencil

\\[ P_i(\lambda). \\]

Then the generic spectral condition on that component is

\\[ \gcd\\{\omega\text{-minors of }P_i(\lambda)\\}=1 \quad\text{in }F_i[\lambda]. \\]

There are two possibilities:

- If the generic gcd is nonconstant, the entire component is spectrally bad.
- If the generic gcd is constant, the spectrally good locus is a nonempty Zariski-open dense subset of that component.

Thus the original feasibility question can be reduced, over an algebraically closed field, to identifying whether at least one admissible irreducible component is generically good.

For real feasibility, there is an additional issue: a complex component may have no real points, or its real points may fail to be Zariski dense. Therefore, a complex generic-gcd calculation is not by itself a complete real-feasibility proof. One must also establish the existence and appropriate density of real points on a component.

This is precisely why I recommend componentwise analysis rather than treating the whole admissible locus as one affine family.

## 6. Is a Kronecker-form classification of the pencil space likely to help?

I would not make that the principal algorithmic direction.

The Kronecker canonical form is a classification tool for an individual matrix pencil under strict equivalence. It records the finite and infinite elementary divisors and the left and right minimal indices.

Your problem is different: the object to be classified is an entire linear or affine space of pencils. A transformation that puts one member into Kronecker form need not preserve the affine-linear structure of the family of all members. In particular, choosing parameter-dependent equivalence transformations can turn a linear family into a nonlinear one.

There are still useful ways to employ Kronecker theory:

- classify generic members of the family;
- identify the possible rank-drop structures;
- study special parameter loci where the Kronecker structure changes;
- use minimal indices to derive structural restrictions on possible right-prime members.

But a “Kronecker form of the whole subspace” is not an obvious substitute for the generic gcd/resultant approach. It risks replacing a relatively concrete polynomial-identity question with a much harder classification problem for matrix spaces.

For \\(\omega=2\\), I would first use the explicit maximal-minor formulas. They contain the relevant information directly and are easier to manipulate symbolically.

## 7. Question 3: Does the evidence now favour hardness?

No. The evidence does not yet favour hardness over tractability.

It favours the conclusion that ordinary rank invariants are insufficient. That is a different statement.

Let us separate the evidence carefully.

### Evidence against a simple rank-only criterion

The pair \\(G_a,G_b\\) is a valid counterexample to the assertion that the listed rank invariants determine spectral feasibility. It is a useful and clean counterexample.

It does not show that the problem is \\(\exists\mathbb R\\)-hard, NP-hard, or even computationally difficult for fixed \\(\omega\\).

### Evidence for tractability in the affine regime

The genericity theorem gives a structural reason for tractability whenever the admissible parameter domain is a nonempty open subset of an affine space. The \\(k=\omega=2\\) regime falls into this category.

For fixed \\(\omega\\), the generic resultant construction gives a finite exact computation whose algebraic degree is bounded independently of the number of affine parameters.

This is substantive positive evidence for tractability in that regime.

### Evidence that the general observer problem may be harder

When \\(k>\omega\\), the admissibility constraint

\\[ \ker H\subseteq\ker H_A \\]

is an additional determinantal restriction. The feasible set is no longer simply the complement of a closed bad locus in an affine space. It is the complement of the bad locus inside a nonlinear admissible set.

That is a plausible source of complexity. However, it is only a plausible source until a reduction is constructed or a structural algorithm is proved.

### My assessment

| Claim                                                                           | Assessment                                        |
| ------------------------------------------------------------------------------- | ------------------------------------------------- |
| Ordinary rank invariants determine feasibility at \\(\omega=2\\)                | Refuted                                           |
| Fixed-pencil spectral feasibility is difficult                                  | No; it is a univariate gcd test                   |
| Affine-family feasibility is difficult at \\(k=\omega=2\\)                      | Evidence points to tractability                   |
| General \\(k>\omega\\) observer synthesis is tractable                          | Open                                              |
| General \\(k>\omega\\) observer synthesis is \\(\exists\mathbb R\\)-hard        | Not established                                   |
| The admissible determinantal locus is the likely source of remaining complexity | Strong structural hypothesis, worth investigating |

I would therefore describe the current state as:

> The rank-only conjecture is false, but the evidence does not support a hardness conjecture yet. The affine spectral subproblem has a generic algebraic test. Any genuine complexity barrier is more likely to arise from the nonlinear admissibility locus imposed by (5a), especially when \\(k>\omega\\).

This is a more defensible conclusion than saying that the balance has shifted toward hardness.

## 8. Question 4: Should Stage 2 or Stage 4 be prioritized?

I recommend Stage 2, with a focused generic-resultant computation inserted before expanding the hardness work.

The reason is that the current results have identified a structural separation:

- the spectral condition behaves generically on affine families;
- the admissibility condition can make the relevant domain nonlinear.

A hardness reduction attempted before understanding this separation could accidentally encode difficulty into a subproblem that is already tractable.

### Revised priority order

Priority 1 — Correct and consolidate the \\(\omega=2\\) algebra

Immediate

- Correct the maximal-minor count.
- Verify the three explicit minors.
- Retain the rank counterexample, with its precise scope.
- Implement the generic resultant and degree-\\(8\\) bound.

Priority 2 — Continue componentwise classification

Main research direction

- Work on \\(k>\omega\\).
- Describe the admissible locus on pivot charts.
- Determine its irreducible components in the smallest nontrivial examples.
- Compute the generic gcd on each component.

Priority 3 — Identify the actual nonlinear bottleneck

After Stage 2

Determine whether the hard part is:

- existence of real points on the admissible locus;
- component selection;
- generic spectral feasibility on a component;
- or interaction among these conditions.

Priority 4 — Attempt a hardness reduction

Conditional

Target the nonlinear admissibility geometry, not merely the \\(\omega=2\\) common-root condition on an affine family. Start with \\(k>\omega\\).

I would not abandon hardness research. I would postpone it until the componentwise structure is clearer.

## 9. A concrete research programme for the next round

I suggest the following experiments and proofs, in this order.

### Experiment A: Verify the affine genericity theorem computationally

For small rational affine families

\\[ P_t(\lambda)=\lambda U(t)-G(t), \\]

with \\(U(t)\\) full column rank on a nonempty domain:

1. Compute the gcd of the maximal minors over \\(\mathbb Q(t)[\lambda]\\).
2. Compute the generic-combination resultant.
3. Sample rational \\(t\\) values in the full-rank domain.
4. Verify that a nonzero generic resultant corresponds to a nonempty open set of good samples.
5. Verify that an identically zero generic resultant corresponds to every sample being bad.

This is a useful independent audit of the theorem and its implementation.

### Experiment B: Compare \\(k=\omega\\) and \\(k>\omega\\)

Fix small observer dimensions and compare:

\\[ \begin{array}{c|c|c} \text{Regime}&\text{Admissibility condition}&\text{Expected analysis}\\\ \hline k=\omega&\text{Automatic on }\rank H=\omega& \text{Affine genericity}\\\ k>\omega&\ker H\subseteq\ker H_A& \text{Determinantal component analysis} \end{array} \\]

The comparison should be performed with the same \\(A,C,L_0\\) wherever possible, so that changes in behaviour can be attributed to the rank stratum rather than unrelated changes in the system.

### Experiment C: Search for a nontrivial bad admissible component

The most valuable new example would be an observer instance with:

- \\(k>\omega\\);
- a nonempty admissible locus;
- at least one irreducible component on which the generic gcd is nonconstant;
- another component, or another instance, on which the generic gcd is constant.

Such an example would demonstrate that componentwise generic behaviour is genuinely relevant and not merely a formal possibility.

If all small examples are generically good, that would support a tractability conjecture, but would not prove one. If a component is generically bad, it would identify a more precise target for a hardness reduction.

### Experiment D: Only then attempt quadratic-feasibility encoding

A reduction should specify:

1. the source problem and its input encoding;
2. how source variables are represented by observer augmentation variables;
3. how the source equations are enforced by the admissibility constraints;
4. why every source solution yields a spectrally feasible augmentation;
5. why every spectrally feasible augmentation yields a source solution;
6. why the construction has polynomial bit complexity.

The last two implications are particularly important. It is easy to arrange that a source solution produces one feasible augmentation. It is much harder to prove that there are no unintended feasible augmentations.

I would avoid claiming \\(\exists\mathbb R\\)-hardness until all six points are established.

## 10. Recommended corrections to the report itself

I would make the following changes before treating `45_rank_only_refuted_and_mismatch.md` as a stable research record.

| Current statement                                                                       | Recommended revision                                                                                                                                                                              |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| “The conjecture fails at \\(\omega\ge2\\)”                                              | “The tested ordinary-rank characterization fails at \\(\omega=2\\).”                                                                                                                              |
| “One quadratic and \\(q-2\\) linears”                                                   | “One quadratic, \\(2(q-2)\\) linears, and \\(\binom{q-2}{2}\\) constants.”                                                                                                                        |
| “The bad condition is quadratic in \\(R\\)”                                             | “At fixed \\(\lambda\\), the maximal-minor equations are quadratic in \\(R\\); eliminating \\(\lambda\\) generally produces higher-degree equations.”                                             |
| “Does \\(\Lambda\\) contain a regular pencil?”                                          | “Does \\(\Lambda\\) contain a right-prime pencil, i.e. one with full column rank at every finite \\(\lambda\\)?”                                                                                  |
| “The hard part is the interaction of a linear \\(\Lambda\\) with a quadratic condition” | “In the affine regime, the bad locus is closed and feasibility is generic. The unresolved difficulty lies in the interaction of the spectral-open condition with the nonlinear admissible locus.” |
| “Would you start with \\(k=\omega=2\\) for hardness?”                                   | “Use \\(k=\omega=2\\) as an algorithmic test case; investigate \\(k>\omega\\) for possible hardness.”                                                                                             |

One further point should be added explicitly: the counterexample proves that the four listed rank invariants are insufficient. It does not establish that all rank-based invariants are insufficient, nor does it automatically establish a counterexample within every observer-induced reachable family.

## 11. Final assessment

The report contains a real mathematical advance: it has isolated a mismatch between linear reachability and nonlinear spectral rank-drop conditions, and it has produced a concrete counterexample to a natural rank-only conjecture.

But the most important next insight is that the mismatch needs to be analyzed at the correct level.

For \\(k=\omega\\), the admissibility condition is automatic on the full-rank domain. The problem is then an affine-family right-prime existence problem, and the generic gcd/resultant method provides a strong algorithmic route. In particular, \\(q=3,k=\omega=2\\) is better viewed as a tractable laboratory than as a likely hardness core.

For \\(k>\omega\\), the admissible set is generally determinantal rather than affine-linear. This is where componentwise algebraic geometry becomes essential, and where a genuine complexity barrier might reside.

My recommendation is therefore:

\\[ \boxed{ \text{Correct the minor analysis} \\;\longrightarrow\\; \text{establish the affine generic test} \\;\longrightarrow\\; \text{classify admissible components for }k>\omega \\;\longrightarrow\\; \text{attempt hardness only if the geometry warrants it}. } \\]

This sequence is mathematically safer, more likely to produce a publishable structural theorem, and less likely to spend substantial effort trying to prove hardness in a regime where genericity already gives an exact decision method.