# A complete reassessment of the dimension question, the admissible locus, and the complexity strategy

The central issue in `44_dimension_question.md` is correctly identified: the proposed codimension estimate was made in the ambient reachable space, whereas feasibility is tested only on the subset satisfying (5a). The distinction is decisive. The twelve examples demonstrate that the admissibility constraint can force the entire admissible family into the spectral bad locus.

My main conclusions are:

1. The admissible locus is generally not a finite union of affine-linear pieces. It is naturally a locally closed determinantal variety. It has a useful Grassmannian-fiber description: after fixing the row space of \\(H(R)\\), the constraints become affine-linear in \\(R\\), but the row space itself varies over a Grassmannian.
2. The correct replacement for the failed dimension argument is componentwise incidence geometry. One must estimate the spectral bad locus inside each irreducible component of the admissible locus, not in the whole reachable space.
3. I would not yet abandon the hardness programme, but I would change its order. First investigate the structure of the admissible components and the spectral obstruction on them. Stage 3 should be attempted only after identifying a nontrivial family in which the spectral condition genuinely retains enough freedom to encode variable algebraic constraints.
4. The twelve-instance phenomenon is a genuine obstruction mechanism, but there is no basis for believing it is the only one. Spectral obstructions can persist even when the admissible locus is large and well behaved. The conjecture that feasibility is decidable by rank computations remains a plausible research direction, not an established conclusion.

I will develop these points in detail and then give a revised research plan.

## 1. The mathematical setting and the precise object to study

Let

\\[ K=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \qquad k=\dim K, \\]

and let \\(N_K\\) be a basis matrix of \\(K\\). Write

\\[ H(R)=\mathcal L(R)N_K,\qquad H_A(R)=\mathcal L(R)A N_K, \\]

where

\\[ \mathcal L(R)= \begin{bmatrix} L_0\\\R \end{bmatrix}, \qquad m=q-r. \\]

The report denotes by \\(\mathscr R\\) the reachable linear space of lower-block pairs \\((H,H_A)\\). Its dimension is

\\[ \dim\mathscr R =m\bigl(2k-\dim\ker T\bigr), \\]

where

\\[ T:K\oplus K\longrightarrow\mathbb C^n, \qquad T(v,w)=v+Aw. \\]

The kernel is naturally isomorphic to

\\[ \ker T\cong\\{w\in K:Aw\in K\\}. \\]

The relevant admissible locus, at a fixed rank \\(\omega\\), is

\\[ \boxed{ \mathcal X\_\omega = \left\\{ R: \operatorname{rank}H(R)=\omega,\quad \operatorname{rank} \begin{bmatrix} H(R)\\\H_A(R) \end{bmatrix} =\omega \right\\}. } \\]

This is the right object because, once \\(\operatorname{rank}H=\omega\\), condition (5a) is equivalent to

\\[ \operatorname{row}H_A(R) \subseteq \operatorname{row}H(R). \\]

The spectral bad locus is

\\[ \boxed{ \mathcal B\_\omega = \left\\{ R\in\mathcal X\_\omega: \exists\lambda\in\mathbb C,\  \operatorname{rank}\bigl(\lambda H(R)-H_A(R)\bigr)<\omega \right\\}. } \\]

The feasibility question at rank \\(\omega\\) is exactly

\\[ \mathcal X\_\omega\setminus\mathcal B\_\omega\ne\varnothing. \\]

The important point is that the dimension comparison must be

\\[ \dim\mathcal B\_\omega \quad\text{versus}\quad \dim\mathcal X\_\omega, \\]

or, more precisely, the corresponding comparison on irreducible components. A comparison with \\(\dim\mathscr R\\) is not sufficient.

# 2. Question 1: Is the admissible locus a finite union of affine-linear pieces?

## 2.1 The short answer

In general, no.

There is a useful decomposition into affine-linear fibers indexed by a Grassmannian, but that does not give a finite union of fixed affine-linear pieces.

The natural algebraic description is a locally closed determinantal set:

\\[ \mathcal X\_\omega = \left\\{ R: \operatorname{rank}H(R)=\omega \right\\} \cap \left\\{ R: \operatorname{rank} \begin{bmatrix}H(R)\\\H_A(R)\end{bmatrix} \le\omega \right\\}. \\]

The first condition is locally closed:

\\[ \operatorname{rank}H=\omega \iff \operatorname{rank}H\le\omega \quad\text{and}\quad \operatorname{rank}H\ge\omega. \\]

The second condition is determinantal, defined by the \\((\omega+1)\\)-minors of the stacked matrix.

Consequently, \\(\mathcal X\_\omega\\) is locally closed in the parameter space. It is constructible and has finitely many irreducible components, but its components need not be affine-linear.

That distinction matters: a finite decomposition into algebraic or locally closed pieces is not the same as a finite decomposition into affine-linear pieces.

## 2.2 A simple determinantal example showing why affine-linearity fails

Consider the special situation

\\[ q=k=2,\qquad \omega=1, \\]

and suppose the attainable pair has the form

\\[ H(R)=R,\qquad H_A(R)=0, \\]

where \\(R\\) ranges over all \\(2\times2\\) complex matrices.

This is compatible with the structural possibility that \\(A\\) vanishes on \\(K\\), so \\(A N_K=0\\), while the lower block can generate arbitrary \\(H\\).

Condition (5a) is automatic because \\(H_A=0\\). The rank condition is simply

\\[ \operatorname{rank}R=1. \\]

Thus the admissible locus is

\\[ \mathcal X_1 = \left\\{ R\in\mathbb C^{2\times2}: \operatorname{rank}R=1 \right\\}. \\]

Writing

\\[ R=\begin{pmatrix}a&b\\\c&d\end{pmatrix}, \\]

we obtain

\\[ \mathcal X_1 = \left\\{ (a,b,c,d): ad-bc=0,\quad R\ne0 \right\\}. \\]

Its Zariski closure is the rank-at-most-one determinantal variety

\\[ \overline{\mathcal X_1} = V(ad-bc). \\]

This is an irreducible quadratic hypersurface in \\(\mathbb C^4\\). It is not an affine-linear subspace.

More strongly, it cannot be a finite union of proper affine-linear subsets. Indeed, suppose that it were contained in a finite union

\\[ \overline{\mathcal X_1} \subseteq L_1\cup\cdots\cup L_s, \\]

where each \\(L_i\\) is affine-linear and lies in the determinantal hypersurface. Since \\(\overline{\mathcal X_1}\\) is irreducible, it would have to be contained in one \\(L_i\\). But that would force the irreducible three-dimensional quadric hypersurface to lie in an affine-linear subspace of dimension at least three, which would make that subspace equal to the hypersurface. This is impossible.

The example shows that even when (5a) is automatic, the rank-exact admissible locus can be genuinely nonlinear.

So the hoped-for finite affine-linear decomposition is not available in general.

## 2.3 The useful replacement: fix the row space first

Although the admissible locus is not generally a finite union of affine-linear pieces, it has a much more informative description.

For \\(R\in\mathcal X\_\omega\\), define

\\[ S=\operatorname{row}H(R)\in\operatorname{Gr}(\omega,k). \\]

Then (5a) is equivalent to

\\[ \operatorname{row}H_A(R)\subseteq S. \\]

For each fixed \\(S\in\operatorname{Gr}(\omega,k)\\), define

\\[ \mathcal X\_{\omega,S} = \left\\{ R: \operatorname{row}H(R)=S,\quad \operatorname{row}H_A(R)\subseteq S \right\\}. \\]

Then

\\[ \boxed{ \mathcal X\_\omega = \bigcup\_{S\in\operatorname{Gr}(\omega,k)} \mathcal X\_{\omega,S}. } \\]

This is the right decomposition.

For a fixed subspace \\(S\\), the conditions

\\[ \operatorname{row}H(R)\subseteq S, \qquad \operatorname{row}H_A(R)\subseteq S \\]

are linear conditions on the entries of \\(H(R)\\) and \\(H_A(R)\\). Since \\(H\\) and \\(H_A\\) depend affinely on \\(R\\), these are affine-linear conditions on \\(R\\).

The equality

\\[ \operatorname{row}H(R)=S \\]

adds the open condition \\(\operatorname{rank}H(R)=\omega\\).

Therefore:

> Fixed-row-space fiber principle. For each fixed \\(S\in\operatorname{Gr}(\omega,k)\\), the corresponding admissible fiber is a relatively open subset of an affine-linear subspace of the \\(R\\)-parameter space.

This is a strong structural statement. It is not, however, a finite affine-linear decomposition of the entire admissible locus, because \\(S\\) varies continuously.

## 2.4 Why finite Grassmannian charts do not solve the problem

One might object that the Grassmannian has a finite standard affine-chart cover. Could this make the admissible locus a finite union of affine-linear pieces after all?

No. It gives a finite cover by coordinate charts, but the equations in those charts generally remain polynomial rather than affine-linear.

For example, on a standard chart of \\(\operatorname{Gr}(\omega,k)\\), write a subspace \\(S\\) as the row space of

\\[ \begin{bmatrix}I\_\omega&T\end{bmatrix}, \\]

where \\(T\\) is an \\(\omega\times(k-\omega)\\) matrix.

A row vector \\(x=(x_1,x_2)\\), with the coordinates partitioned according to this chart, lies in \\(S\\) precisely when

\\[ x_2=x_1T. \\]

Applying this to every row of \\(H\\) and \\(H_A\\) gives equations involving products of the chart variable \\(T\\) and the entries of \\(H,H_A\\). Since the latter depend on \\(R\\), the joint equations in \\((R,T)\\) are generally bilinear.

Thus the finite chart cover produces a finite family of algebraic parameterizations, not a finite union of affine-linear subsets in \\(R\\).

This distinction is important for the dimension argument. The correct geometric object is a family of affine-linear fibers over a Grassmannian, and the base variation contributes dimension and can create nonlinear behavior.

## 2.5 A more precise incidence-space formulation

It is useful to make the Grassmannian description algebraic.

Let

\\[ \mathfrak I\_\omega = \left\\{ (R,S)\in\mathbb C^{\dim R}\times \operatorname{Gr}(\omega,k): \operatorname{row}H(R)\subseteq S,\ \operatorname{row}H_A(R)\subseteq S \right\\}. \\]

Inside this incidence variety, impose the open condition

\\[ \operatorname{rank}H(R)=\omega. \\]

The projection

\\[ \pi:\mathfrak I\_\omega\longrightarrow \mathbb C^{\dim R}, \qquad (R,S)\longmapsto R \\]

then has image exactly \\(\mathcal X\_\omega\\), and on the rank-\\(\omega\\) locus the subspace \\(S\\) is uniquely determined by \\(R\\):

\\[ S=\operatorname{row}H(R). \\]

This incidence-space construction is useful for at least three reasons:

1. It gives a geometric model of the admissible locus that separates the row-space variable from the augmentation variable.
2. It allows one to study dimensions through fibers of a projection.
3. It gives a natural setting for analyzing how the spectral obstruction varies with \\(S\\).

Recommendation: make \\(\mathfrak I\_\omega\\) the principal geometric object for the next stage of the project. It is more informative than trying to force \\(\mathcal X\_\omega\\) into a finite affine-linear decomposition.

# 3. The failed codimension argument: exactly where it breaks

The report considers the determinantal variety

\\[ Z\_\omega = \left\\{ M\in\mathbb C^{q\times k}: \operatorname{rank}M<\omega \right\\}. \\]

Its codimension in the full matrix space is

\\[ \boxed{ \operatorname{codim}Z\_\omega = (q-\omega+1)(k-\omega+1). } \\]

This formula is correct, assuming \\(1\le\omega\le\min(q,k)\\).

The problem is the next inference:

\\[ \operatorname{codim}\phi^{-1}(Z\_\omega) \ge \operatorname{codim}Z\_\omega. \\]

This is false for a general linear or affine-linear map \\(\phi\\).

## 3.1 A counterexample to the pullback-codimension claim

Let

\\[ \phi:\mathbb C\longrightarrow\mathbb C^2, \qquad \phi(t)=(t,0), \\]

and let

\\[ Z=\\{(0,0)\\}. \\]

Then

\\[ \operatorname{codim}\_{\mathbb C^2}Z=2, \\]

but

\\[ \phi^{-1}(Z)=\\{0\\} \\]

has codimension one in \\(\mathbb C\\).

Thus

\\[ \operatorname{codim}\phi^{-1}(Z) < \operatorname{codim}Z. \\]

The issue is that the image of \\(\phi\\) is only a one-dimensional subspace of the two-dimensional target. The pullback sees the intersection of \\(Z\\) with that image, not the full ambient codimension of \\(Z\\).

## 3.2 The correct formula for a linear pullback

Let

\\[ \phi:X\longrightarrow Y \\]

be an affine-linear map of affine spaces, with image \\(L=\phi(X)\\). Let \\(Z\subseteq Y\\) be an algebraic set.

Because all nonempty fibers of \\(\phi:X\to L\\) have dimension \\(\dim\ker\phi\\),

\\[ \dim\phi^{-1}(Z) = \dim\ker\phi+\dim(Z\cap L), \\]

provided \\(Z\cap L\ne\varnothing\\).

Since

\\[ \dim X=\dim\ker\phi+\dim L, \\]

we obtain

\\[ \boxed{ \operatorname{codim}\_X\phi^{-1}(Z) = \operatorname{codim}\_L(Z\cap L). } \\]

This is the correct statement.

The codimension in the ambient target \\(Y\\) is relevant only when the image \\(L\\) has sufficiently general position relative to \\(Z\\), or when \\(\phi\\) is surjective. In the surjective case,

\\[ \operatorname{codim}\_X\phi^{-1}(Z) = \operatorname{codim}\_Y Z. \\]

But there is no such surjectivity assumption in the report's setting.

## 3.3 The additional problem: the admissible locus is smaller still

For a fixed \\(\lambda\\), define

\\[ \phi\_\lambda(R) = \lambda H(R)-H_A(R). \\]

The bad condition at that \\(\lambda\\) is

\\[ \operatorname{rank}\phi\_\lambda(R)<\omega. \\]

Even if one had a useful codimension estimate for

\\[ \phi\_\lambda^{-1}(Z\_\omega) \\]

inside the whole \\(R\\)-space, the desired set is

\\[ \mathcal X\_\omega \cap \phi\_\lambda^{-1}(Z\_\omega). \\]

Its codimension must be measured inside \\(\mathcal X\_\omega\\), not inside the whole parameter space.

The twelve-instance batch is a concrete demonstration of this problem. There, the rank-one admissibility constraint forces one parameter to vanish. On the resulting admissible locus, the spectral non-invariance determinant vanishes identically. Thus the bad set fills the admissible locus even though the ambient reachable space has a much larger dimension.

The report's diagnosis of the failed argument is therefore correct.&#x20;

44_dimension_question.md



# 4. The correct replacement: componentwise incidence geometry

The spectral bad locus is not simply a fixed-\\(\lambda\\) determinantal pullback. It is a union over all spectral parameters.

The right object is the incidence variety.

## 4.1 Homogenize the spectral parameter

For \\(R\in\mathcal X\_\omega\\), consider

\\[ P_R(\alpha,\beta) = \alpha H(R)-\beta H_A(R), \qquad [\alpha:\beta]\in\mathbb P^1. \\]

Define

\\[ \mathfrak B\_\omega = \left\\{ (R,[\alpha:\beta]): R\in\mathcal X\_\omega,\  \operatorname{rank} \bigl(\alpha H(R)-\beta H_A(R)\bigr)<\omega \right\\}. \\]

This is a determinantal incidence variety in

\\[ \mathcal X\_\omega\times\mathbb P^1. \\]

The projection to the first factor has image equal to the bad locus:

\\[ \operatorname{pr}\_1(\mathfrak B\_\omega)=\mathcal B\_\omega. \\]

At the point \\([1:0]\\),

\\[ P_R(1,0)=H(R), \\]

which has rank \\(\omega\\) throughout \\(\mathcal X\_\omega\\). Therefore the incidence variety has no point over \\([1:0]\\).

Because \\(\mathbb P^1\\) is projective, the projection

\\[ \mathcal X\_\omega\times\mathbb P^1 \longrightarrow\mathcal X\_\omega \\]

is proper. Hence the image of the closed incidence variety is closed relative to \\(\mathcal X\_\omega\\).

Thus:

> Closedness theorem. The spectral bad locus \\(\mathcal B\_\omega\\) is Zariski-closed relative to the admissible locus \\(\mathcal X\_\omega\\).

This is important because it makes the generic-feasibility question precise.

## 4.2 The irreducible-component dichotomy

Suppose

\\[ \mathcal X\_\omega=\bigcup\_{i=1}^s X_i \\]

is the decomposition into irreducible components.

Since \\(\mathcal B\_\omega\\) is relatively closed, each intersection

\\[ \mathcal B\_\omega\cap X_i \\]

is closed in \\(X_i\\).

There are two possibilities for each component:

- Entirely bad:\
  \\[\
  X_i\subseteq\mathcal B\_\omega.\
  \\]
- Generically good:\
  \\[\
  X_i\not\subseteq\mathcal B\_\omega.\
  \\]\
  In this case, \\(\mathcal B\_\omega\cap X_i\\) is a proper closed subset, and\
  \\[\
  X_i\setminus\mathcal B\_\omega\
  \\]\
  is a nonempty Zariski-open dense subset of \\(X_i\\).

Therefore the admissible locus has a componentwise dichotomy:

\\[ \boxed{ \text{Each irreducible component is either entirely bad or generically good.} } \\]

This is stronger and more useful than a global dimension comparison.

A subtlety is worth emphasizing. If \\(\mathcal X\_\omega\\) is reducible, it is not enough to show that the bad locus is proper in the union. It may contain some entire components and miss others. Feasibility requires at least one component to contain a good point; generic feasibility on every component requires that no component be entirely bad.

## 4.3 A dimension criterion that actually works

Let \\(X_i\\) be an irreducible component of \\(\mathcal X\_\omega\\), with

\\[ \dim X_i=d_i. \\]

Suppose we can prove that for every \\([\alpha:\beta]\in\mathbb P^1\\), the fixed-parameter rank-drop locus

\\[ D\_{[\alpha:\beta]} = \left\\{ R\in X_i: \operatorname{rank} \bigl(\alpha H(R)-\beta H_A(R)\bigr)<\omega \right\\} \\]

has codimension at least \\(c_i\\) in \\(X_i\\), uniformly in \\([\alpha:\beta]\\).

Then

\\[ \dim D\_{[\alpha:\beta]}\le d_i-c_i. \\]

The incidence variety has a one-dimensional parameter space, so

\\[ \dim\bigl(\mathfrak B\_\omega|\_{X_i}\bigr) \le d_i-c_i+1. \\]

Consequently, if

\\[ \boxed{c_i\ge2,} \\]

then

\\[ \dim\bigl(\mathfrak B\_\omega|\_{X_i}\bigr) \le d_i-1. \\]

Its projection cannot fill \\(X_i\\). Therefore \\(X_i\\) contains a nonempty Zariski-open set of spectrally feasible points.

This gives a correct version of the dimension argument:

> Componentwise codimension criterion. If every fixed-spectral-parameter rank-drop locus has codimension at least two inside an irreducible admissible component, uniformly in the spectral parameter, then the bad spectral locus is a proper closed subset of that component.

This is the most direct replacement for the failed argument in the report.

It also explains the critical role of codimension one. A one-parameter family of codimension-one bad loci can sweep out an entire component. A one-parameter family of codimension-two bad loci cannot.

## 4.4 Why the ambient determinantal codimension is not enough

The ambient codimension

\\[ (q-\omega+1)(k-\omega+1) \\]

is only a starting point.

To use it, one would need a theorem showing that the relevant linear or affine-linear slices meet the determinantal variety with a controlled codimension inside the admissible component.

For example, a sufficient but generally strong hypothesis would be that, for every \\([\alpha:\beta]\\), the induced map from \\(X_i\\) to the matrix space is sufficiently transverse to the rank-drop variety.

There is no reason to expect this automatically. In the twelve-instance example, the admissible component is already contained in the bad locus, so the fixed-parameter codimension is zero.

The next research task is therefore not to improve the ambient codimension estimate. It is to understand the geometry of the attainable spectral slices after imposing (5a).

# 5. A second route: generic spectral analysis over function fields

The incidence method gives a geometric criterion. There is also an algebraic method that is especially suitable for computation.

Let \\(X_i\\) be an irreducible component of the complex admissible locus, and let

\\[ F_i=\mathbb C(X_i) \\]

be its function field.

Regard

\\[ P_i(\lambda)=\lambda H-H_A \\]

as a polynomial matrix over \\(F_i[\lambda]\\).

Let

\\[ \Delta_i(\lambda) = \gcd\\{\text{all }\omega\times\omega\text{ minors of }P_i(\lambda)\\} \\]

in \\(F_i[\lambda]\\), defined up to multiplication by a nonzero element of \\(F_i\\).

Then:

- If\
  \\[\
  \deg\Delta_i>0,\
  \\]\
  the maximal minors have a common nonconstant factor over the function field. The generic point of \\(X_i\\) is spectrally bad. In fact, the entire component is bad.
- If\
  \\[\
  \deg\Delta_i=0,\
  \\]\
  the maximal minors are coprime over the function field. The generic point is good, and the bad locus is a proper closed subset of \\(X_i\\). Hence the good points form a nonempty Zariski-open dense subset.

The reason is that the common-factor condition is algebraic in the coefficients. If a common root exists over an algebraic closure of the function field, the incidence projection dominates the component. Conversely, if the generic point is not in the closed bad locus, that locus is proper.

Thus:

\\[ \boxed{ X_i\text{ is entirely bad} \iff \deg\Delta_i>0. } \\]

And

\\[ \boxed{ X_i\text{ is generically good} \iff \deg\Delta_i=0. } \\]

This is a particularly attractive criterion because it reduces the geometric dichotomy to a polynomial gcd computation over a function field.

There are, however, two important qualifications.

### Qualification 1: It is not yet a rank-only criterion

Computing a gcd of polynomial minors over a function field is an algebraic computation. It is not generally equivalent to checking the ranks of a fixed finite list of constant matrices.

It may eventually admit a finite rank characterization under additional structure, but that is precisely something to prove.

### Qualification 2: Complex generic feasibility does not automatically imply real feasibility

The original synthesis problem is over real matrices \\(R\\). A complex irreducible component may have no real points, or its real points may fail to be Zariski dense.

Therefore:

\\[ \text{complex generic good} \not\Rightarrow \text{real feasible} \\]

without a real-point hypothesis.

A useful sufficient condition is that the relevant irreducible component is defined over \\(\mathbb R\\) and has a nonsingular real point. Under suitable irreducibility assumptions, its real points are then Zariski dense, and a nonempty complex Zariski-open good subset must meet the real locus.

For the paper, I recommend keeping the complex-geometric genericity theorem and the real-existence statement separate.

# 6. Question 2: Should Stage 3 begin, or should the negative evidence become a conjecture?

The report asks whether, after three unsuccessful attempts to identify a minimal hard subfamily, the project should proceed to encoding quadratic constraints or consolidate the negative evidence into a conjecture.

My recommendation is:

Do not begin a broad Stage 3 reduction yet. But do not abandon the hardness programme either. First complete a targeted structural investigation of the admissible locus and the spectral obstruction.

The reason is methodological. A polynomial many-one reduction requires a subfamily with enough algebraic freedom to encode the source problem. At present, the experiments suggest that some apparently promising regimes collapse under (5a). That is a warning that the chosen subfamilies may not preserve the degrees of freedom required for hardness.

However, three negative probes are not evidence of a general polynomial-time theorem.

## 6.1 Why the three negative probes are informative but inconclusive

The report records:

- the free regime is trivially feasible;
- the smallest constrained regime is rigid and comparatively easy;
- the reachable space is not thin;
- three attempts to find a minimal hard subfamily have not succeeded.

These observations are useful. They suggest that a naive reduction strategy based on a small number of freely assignable quadratic coefficients may not work.

But there are several reasons not to infer tractability.

### First: a large reachable space does not imply easy feasibility

The dimension formula

\\[ \dim\mathscr R = m\bigl(2k-\dim\ker T\bigr) \\]

measures the dimension of the attainable pair space. It does not describe the complexity of the subset satisfying (5a), nor the geometry of the spectral bad locus within that subset.

A large ambient parameter space can contain a highly constrained admissible locus.

### Second: hardness need not arise from rare feasible points

The report suggests that the difficulty of \\(q1\\) may not be of the “rare feasible set” kind exploited by NP-hard reductions.

That is too strong as a complexity-theoretic inference.

A decision problem can be hard even if its yes-instances occupy a large or dense subset of some natural parameter space. Conversely, a problem can have a very sparse feasible set and still be easy to decide.

Dimension and measure heuristics can help identify promising reductions, but they do not establish or exclude computational hardness.

### Third: three failed subfamilies do not constrain all possible reductions

A reduction may require:

- a larger rank \\(\omega\\);
- more than one independent spectral direction;
- a nontrivial interaction between the fixed top block and the variable lower block;
- a family in which the admissible row space itself carries the encoded variables;
- or a construction in which the spectral bad locus has codimension one and its projection encodes a polynomial constraint.

The current negative probes do not rule out these possibilities.

## 6.2 What should be done before Stage 3?

I recommend three focused tasks.

### Task A: classify the admissible locus by row-space fibers

For each \\(\omega\\), use

\\[ \mathcal X\_\omega = \bigcup\_{S\in\operatorname{Gr}(\omega,k)} \mathcal X\_{\omega,S}. \\]

Study the fixed-\\(S\\) fibers first.

Questions to answer:

1. For which \\(S\\) is \\(\mathcal X\_{\omega,S}\\) nonempty?
2. What is its dimension?
3. Is it an affine-linear space with an open rank condition, or can the fixed-\\(S\\) constraints themselves have further nonlinear features due to the parameterization of \\(H,H_A\\)?
4. How does the spectral pencil vary over that fiber?
5. Can the set of \\(S\\) for which a good pencil exists be characterized by a finite set of rank conditions?

This task should clarify whether the difficulty is primarily in choosing the row space \\(S\\), or in choosing a spectrally good pencil once \\(S\\) is fixed.

### Task B: compute the generic spectral obstruction on each component

For each irreducible component \\(X_i\\), calculate

\\[ \Delta_i(\lambda) = \gcd\\{\omega\text{-minors of }\lambda H-H_A\\} \\]

over \\(\mathbb C(X_i)\\).

This gives an exact classification:

- positive degree: the component is entirely bad;
- degree zero: the component is generically good.

For small examples, one can use symbolic computation to identify the pattern. The eventual theoretical objective is to express the degree of \\(\Delta_i\\) through structural data of \\((A,C,L_0)\\).

This is a much more focused target than immediately trying to encode arbitrary quadratic systems.

### Task C: identify a nontrivial flexible family

A useful hardness candidate should satisfy all of the following:

1. The admissible locus has positive dimension.
2. It is not forced into the bad locus by an immediate rank collapse.
3. The spectral condition depends nontrivially on the free parameters.
4. The parameter dependence is rich enough to encode a source problem.
5. The attainable-pair constraints can be described explicitly.

Only after finding such a family should Stage 3 begin.

## 6.3 How to formulate the rank-decidability conjecture

The report proposes a conjecture along the lines of:

> Feasibility is decidable by rank computations on the admissible locus.

I think this is worth investigating, but it should be formulated more carefully.

As written, “rank computations on the admissible locus” is ambiguous. The admissible locus is generally a positive-dimensional algebraic set, and deciding whether a spectral condition holds somewhere on it is not automatically a finite rank problem.

I suggest distinguishing two conjectures.

Conjecture A — structural rank criterion.

For every fixed input \\((A,C,L_0)\\) and target order, the existence of a spectrally feasible admissible augmentation is equivalent to a finite collection of rank conditions on explicitly constructed matrices determined by \\((A,C,L_0)\\).

This is a strong conjecture. It would imply a substantial simplification of the synthesis problem, but it needs a precise specification of the matrices and their construction.

Conjecture B — componentwise spectral criterion.

For every irreducible component \\(X_i\\) of the admissible locus, the degree of the generic determinantal divisor

\\[ \deg\Delta_i \\]

is determined by a finite collection of structural rank invariants of the original data.

This is more directly connected to the established geometry. It also leaves open the possibility that the relevant invariants are more elaborate than ordinary ranks of a few constant matrices.

I recommend beginning with Conjecture B. If it is proved, it may lead to Conjecture A.

## 6.4 A caution about the phrase “decidable by ranks”

There are several distinct levels of a rank-based result:

| Claim                          | Mathematical content                                              | What it would establish |
| ------------------------------ | ----------------------------------------------------------------- | ----------------------- |
| Rank test for a fixed \\(R\\)  | Check (5a), then test the pencil                                  | Candidate verification  |
| Rank test for fixed \\(S\\)    | Decide whether a good extension exists in a fixed row-space fiber | Fiberwise synthesis     |
| Rank test across all \\(S\\)   | Decide whether some admissible row space supports a good pencil   | Full synthesis          |
| Polynomial-time rank algorithm | Bound the number and size of rank computations polynomially       | Complexity result       |

These statements are not equivalent.

In particular, a characterization by finitely many ranks is not automatically a polynomial-time algorithm unless the matrices have polynomial size and can be constructed in polynomial time.

# 7. Question 3: Is admissibility collapse the general mechanism behind infeasibility?

The answer is no, not on the evidence currently available.

The twelve-instance batch demonstrates one important mechanism:

\\[ \text{(5a) restricts the parameter family} \quad\Longrightarrow\quad \text{the admissible family lies inside the bad locus}. \\]

But there are other mechanisms.

## 7.1 Mechanism I: admissibility collapse

This is the mechanism observed in the twelve examples.

The ambient reachable space \\(\mathscr R\\) has a certain dimension, but the admissibility condition imposes additional constraints. In the example, on the rank-one chart, (5a) forces one parameter to vanish. The remaining admissible family is then entirely spectrally bad.

Geometrically,

\\[ \mathcal X\_\omega\subseteq\mathcal B\_\omega. \\]

This is a genuine and important phenomenon.

But it is not the only way to have

\\[ \mathcal X\_\omega\subseteq\mathcal B\_\omega. \\]

The entire admissible locus could be bad because the spectral pencil is structurally constrained, even if the admissible locus itself is large.

## 7.2 Mechanism II: an intrinsic spectral obstruction

Recall the factorization on an admissible rank-\\(\omega\\) chart:

\\[ H=UV,\qquad H_A=GV, \\]

where

\\[ U\in\mathbb C^{q\times\omega} \quad\text{has full column rank}, \\]

and

\\[ V\in\mathbb C^{\omega\times k} \quad\text{has full row rank}. \\]

Then

\\[ \lambda H-H_A = (\lambda U-G)V. \\]

Since \\(V\\) has full row rank,

\\[ \operatorname{rank}(\lambda H-H_A) = \operatorname{rank}(\lambda U-G). \\]

Thus the spectral problem is equivalent to asking whether

\\[ \lambda U-G \\]

has full column rank for every \\(\lambda\in\mathbb C\\).

This can fail because of the structure of \\(U,G\\), independently of any severe collapse of the admissible locus.

### Example: the square reduced-pencil obstruction

If

\\[ q=\omega, \\]

then \\(U\\) is square and invertible. Consequently,

\\[ \det(\lambda U-G) \\]

is a polynomial of degree \\(\omega\\) with leading coefficient \\(\det U\ne0\\).

Since \\(\mathbb C\\) is algebraically closed and \\(\omega\ge1\\), this polynomial has a root. At that root,

\\[ \operatorname{rank}(\lambda U-G)<\omega. \\]

Therefore:

\\[ \boxed{ q=\omega,\ \omega\ge1 \quad\Longrightarrow\quad \text{spectral infeasibility}. } \\]

This obstruction is not an admissibility-collapse phenomenon. It applies to every admissible candidate of that reduced size.

It also confirms that

\\[ q>\omega \\]

is necessary for spectral feasibility, although it is not sufficient.

### Example: a rectangular pencil can be feasible even when \\([U\ G]\\) has deficient rank

For \\(q=3,\omega=2\\), consider

\\[ U= \begin{pmatrix} 1&0\\\ 0&1\\\ 0&0 \end{pmatrix}, \qquad G= \begin{pmatrix} 0&0\\\ 1&0\\\ 0&1 \end{pmatrix}. \\]

Then

\\[ \lambda U-G = \begin{pmatrix} \lambda&0\\\ -1&\lambda\\\ 0&-1 \end{pmatrix}. \\]

Its \\(2\times2\\) minors are

\\[ \lambda^2,\qquad -\lambda,\qquad 1. \\]

They have gcd \\(1\\). Therefore the pencil has full column rank for every \\(\lambda\in\mathbb C\\).

Yet

\\[ \operatorname{rank}[U\ G]=3<4=2\omega. \\]

So the condition

\\[ \operatorname{rank}[U\ G]=2\omega \\]

is sufficient for some constructions but not necessary.

This example is a reduced-pencil example. It does not by itself prove that the pair is realizable from a given observer triple \\((A,C,L_0)\\). That realization question must be handled separately.

## 7.3 Mechanism III: every attainable row space may be spectrally bad

There is another possibility.

For each fixed \\(S\\), the admissible fiber may contain spectrally good pencils. Nevertheless, the original observer structure may allow only row spaces \\(S\\) in a subset

\\[ \Sigma\_{\mathrm{att}}\subseteq\operatorname{Gr}(\omega,k) \\]

that is entirely contained in the bad-row-space locus.

In that case, the obstruction is not a collapse of each individual fiber. It is a restriction on the base family of row spaces.

This is precisely why the Grassmannian incidence model is useful.

One can separate the problem into:

- fiberwise spectral feasibility: for a given \\(S\\), does there exist a good pencil in \\(\mathcal X\_{\omega,S}\\)?
- base-family feasibility: does at least one such \\(S\\) occur among the attainable row spaces?

The overall problem is the conjunction of these two questions.

This is a third mechanism, distinct from both admissibility collapse and the square-pencil obstruction.

## 7.4 A useful taxonomy of infeasibility

I recommend using the following classification in the research report.

| Mechanism                           | Geometric description                                                     | Diagnostic                                                 |
| ----------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------- |
| A. Admissibility collapse           | (5a) restricts the family until it lies in the bad locus                  | Dimension and equations of \\(\mathcal X\_\omega\\)        |
| B. Intrinsic pencil obstruction     | Every admissible reduced pencil has a spectral rank drop                  | Generic determinantal divisor or structural pencil theorem |
| C. Attainable-row-space obstruction | Good pencils exist in some fibers, but no attainable \\(S\\) supports one | Geometry of the attainable subset of the Grassmannian      |
| D. Mixed obstruction                | Several of the above occur simultaneously                                 | Incidence analysis over the admissible family              |

The twelve examples establish Mechanism A in one small regime. They do not establish that A is universal.

# 8. The special cases \\(\omega=0\\) and \\(\omega=1\\)

These cases should be treated separately in both the theoretical presentation and the computational implementation.

## 8.1 The case \\(\omega=0\\)

If

\\[ \operatorname{rank}H=0, \\]

then

\\[ H=0. \\]

Under the admissibility condition,

\\[ \operatorname{rank} \begin{bmatrix}H\\\H_A\end{bmatrix}=0 \\]

forces

\\[ H_A=0. \\]

The spectral pencil is identically zero:

\\[ \lambda H-H_A=0. \\]

But the required rank is also zero. Thus the condition

\\[ \operatorname{rank}(\lambda H-H_A)=\omega \\]

holds for every \\(\lambda\\).

So the spectral condition is automatic when \\(\omega=0\\).

This is not a generic-pencil problem and should be handled separately in the decision procedure.

## 8.2 The case \\(\omega=1\\)

Suppose

\\[ H=uv,\qquad H_A=gv, \\]

where \\(u,g\in\mathbb C^q\\) and \\(v\in\mathbb C^{1\times k}\\) is nonzero.

Then

\\[ \lambda H-H_A = (\lambda u-g)v. \\]

Since \\(v\ne0\\), this matrix has rank one precisely when

\\[ \lambda u-g\ne0. \\]

There exists \\(\lambda\in\mathbb C\\) with

\\[ \lambda u-g=0 \\]

if and only if \\(u\\) and \\(g\\) are linearly dependent.

Therefore

\\[ \boxed{ (5b) \iff \operatorname{rank}[u\ g]=2. } \\]

Since

\\[ [H\ H_A] = [u\ g] \begin{bmatrix} v&0\\\0&v \end{bmatrix} \\]

in the appropriate block interpretation, the equivalent condition is

\\[ \boxed{ (5b) \iff \operatorname{rank}[H\ H_A]=2. } \\]

In particular:

- if \\(q=1\\), spectral feasibility is impossible for \\(\omega=1\\);
- if \\(q\ge2\\), feasibility requires that the two column directions \\(u,g\\) be independent;
- if the admissibility constraints force \\(g\in\operatorname{span}\\{u\\}\\), the entire admissible fiber is bad.

This gives a particularly clean explanation of the twelve-instance behavior if the rank-one reduction indeed forces the two directions to coincide.

It also suggests a useful experimental diagnostic: in every \\(\omega=1\\) instance, record

\\[ \operatorname{rank}[H\ H_A]. \\]

This rank immediately decides the spectral condition.

# 9. What the current evidence does and does not establish

It is important to keep the logical status of the conclusions explicit.

| Statement                                                                         | Status                                                      |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| The ambient pullback-codimension argument is invalid in general                   | Proved                                                      |
| The admissible locus is locally closed determinantal                              | Proved                                                      |
| The admissible locus is generally not a finite union of affine-linear pieces      | Proved by a determinantal example                           |
| Fixed-row-space fibers have affine-linear constraints plus an open rank condition | Proved                                                      |
| The bad spectral locus is closed relative to the admissible locus                 | Proved                                                      |
| Each irreducible component is either entirely bad or generically good             | Proved                                                      |
| The function-field gcd detects whether a component is generically bad             | Proved                                                      |
| The twelve-instance infeasibility is caused by admissibility collapse             | Supported by the reported calculation                       |
| Admissibility collapse is the only possible infeasibility mechanism               | Not established; generally false as a universal explanation |
| Feasibility is decidable by ordinary rank computations                            | Conjectural                                                 |
| The problem is polynomial-time decidable                                          | Not established                                             |
| The problem is \\(\exists\mathbb R\\)-hard                                        | Not established                                             |
| The failure of three proposed hard subfamilies implies tractability               | Not established                                             |

The distinction between “not found” and “impossible” is especially important here. Stage 2 has not produced a hard subfamily, but that does not establish that none exists.

# 10. Revised research plan

I would revise the project into the following sequence.

## Stage 1 — Complete the admissible-locus geometry

Core structure identified

Use the Grassmannian incidence variety

\\[ \mathfrak I\_\omega = \left\\{ (R,S): \operatorname{row}H(R)\subseteq S,\ \operatorname{row}H_A(R)\subseteq S \right\\} \\]

with the open condition \\(\operatorname{rank}H=\omega\\).

For each standard Grassmannian chart:

1. Write the row-space variable \\(S\\) explicitly.
2. Derive the equations in \\(R\\) and the chart variables.
3. Determine the dimension of the fixed-\\(S\\) fiber.
4. Determine the attainable subset of the Grassmannian.
5. Identify which components arise from different row-space strata.

The main goal is a theorem describing the dimension and irreducible components of \\(\mathcal X\_\omega\\) in terms of the map \\(T\\) and the fixed top block \\(L_0\\).

## Stage 2 — Classify the spectral obstruction componentwise

A rigorous criterion is available

For every irreducible component \\(X_i\\), compute

\\[ \Delta_i(\lambda) = \gcd\\{\text{maximal minors of }\lambda H-H_A\\} \\]

over \\(\mathbb C(X_i)\\).

Then classify:

- \\(\deg\Delta_i>0\\): entire component bad;
- \\(\deg\Delta_i=0\\): generic feasibility on the component.

For small dimensions, use exact symbolic computations to discover structural patterns.

The key question is whether \\(\deg\Delta_i\\) can be expressed in terms of simpler invariants of \\((A,C,L_0)\\).

## Stage 3 — Investigate the rank-only conjecture

Do not yet state the conjecture as a theorem. Test it against the componentwise criterion.

In particular, ask whether the generic determinantal divisor is controlled by:

- ranks of \\(L_0N_K\\) and \\(L_0AN_K\\);
- ranks of natural stacked matrices;
- dimensions of \\(K\cap AK\\);
- dimensions of the attainable row-space family;
- ranks of induced maps on the quotient spaces determined by \\(K\\).

A successful criterion should explain both the twelve-instance collapse and the intrinsically bad pencil cases.

## Stage 4 — Resume the hardness search selectively

Only after Stages 1–3 identify a genuinely flexible family should you return to quadratic encoding.

A useful target family should have:

- a positive-dimensional admissible locus;
- nontrivial variation of the reduced pencil;
- no automatic rank-one or square-pencil obstruction;
- a spectral condition whose coefficients can encode independent variables;
- an explicit realization by the original observer data.

If such a family is found, then Stage 3 (quadratic encoding) and Stage 4 (polynomial many-one reduction) become appropriate.

If every tested family collapses to rank conditions, that is evidence for a structural theorem, but it is still not a proof of tractability.

## Stage 5 — Formalization and paper preparation

The remaining tasks in the report should be ordered as follows:

1. Formalize the reduced spectral criterion and its equivalence to the original rank condition.
2. Formalize the fixed-row-space fiber description.
3. Formalize the projective incidence argument for closedness.
4. Formalize the componentwise genericity statement where the required algebraic-geometric infrastructure is available.
5. Prepare the seven-column comparison table for the paper after the mathematical classification has stabilized.

I would not prioritize the comparison table ahead of the structural theorem. The paper's central contribution should be the exact characterization of the admissible and spectrally feasible loci, not merely a catalog of computational regimes.

# 11. Suggested replacement text for the report's conclusions

The following is a more defensible formulation of the current research position.

> Current structural conclusion. The admissible locus at fixed rank \\(\omega\\) is a locally closed determinantal variety, not generally a finite union of affine-linear pieces. It admits a Grassmannian-fiber description: after fixing the row space \\(S=\operatorname{row}H\\), the admissibility constraints become affine-linear in the augmentation variables, together with an open rank condition. The variation of \\(S\\), however, introduces a genuinely algebraic family of fibers.
>
> The spectral bad locus is closed relative to the admissible locus. Consequently, on each irreducible component, either every admissible point is spectrally bad or the spectrally feasible points form a nonempty Zariski-open dense subset. This dichotomy can be tested generically by computing the determinantal divisor of the reduced pencil over the function field of the component.
>
> The twelve-instance batch illustrates one mechanism of infeasibility: the admissibility constraints collapse the candidate family into the spectral bad locus. This mechanism is not known to be universal. Other obstructions arise from the reduced pencil itself or from restrictions on the attainable row spaces.
>
> The current negative results from three proposed hard subfamilies do not establish polynomial-time decidability and do not rule out \\(\exists\mathbb R\\)-hardness. They do suggest that a broad hardness search is premature. The next step should be a componentwise study of the admissible locus and its generic spectral obstruction. A rank-based criterion is a reasonable conjectural direction, but it should be stated as a conjecture until the generic determinantal divisor has been related rigorously to finite structural invariants of the original data.

# 12. Final assessment

The report has made a valuable conceptual correction. The central problem is no longer “Can the ambient determinantal codimension prove feasibility?” It is:

\\[ \boxed{ \text{How does the spectral bad locus intersect the admissible determinantal family?} } \\]

The best way to answer that question is to separate the problem into two layers:

\\[ \underbrace{ \text{Which row spaces }S\text{ are attainable?} }\_{\text{Grassmannian/base-family problem}} \qquad+\qquad \underbrace{ \text{Which attainable fibers contain a good pencil?} }\_{\text{fixed-}S\text{ spectral problem}}. \\]

This separation is the most promising direction emerging from the current work.

My concrete recommendation is to pause broad hardness construction, prove the Grassmannian incidence description carefully, and then compute the generic determinantal divisor on each admissible component. That gives a rigorous structural foundation for either outcome:

- If the componentwise divisor is controlled by finitely many structural ranks, the rank-decidability conjecture may become a theorem.
- If one finds a flexible component on which the divisor varies with independent algebraic parameters, that component may provide the right starting point for a hardness reduction.

At present, neither outcome has been established. But the next mathematical question is now much sharper, and the report's correction of the dimension argument is an important step toward resolving it.