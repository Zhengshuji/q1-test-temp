# Mathematical review of `34_open_or_empty_dichotomy.md`

The new report contains a genuinely important idea: on a fixed rank stratum and a suitable column chart, the bad spectral locus is not merely constructible; under the correct hypotheses, it is Zariski closed relative to that chart. The reason is that the spectral parameter can be compactified to \\(\mathbb P^1\\), and the full-column-rank leading coefficient prevents a common zero from escaping to infinity.

I think this is a stronger and more useful result than the earlier constructibility statement. It changes the way I would approach the complexity question.

However, there is a significant correction needed in the report's interpretation of elimination ideals. In particular,

> “deciding feasibility of a chart is deciding whether the elimination ideal is proper”

is not correct if “proper ideal” is used in its standard algebraic meaning. The relevant question is whether the elimination ideal is nonzero in the coordinate ring of the chart, not whether it is a proper ideal. Those are different tests, and confusing them reverses the interpretation of the principal cases.

There are also two qualifications to the open-or-empty dichotomy:

1. The dichotomy applies to an irreducible stratum-chart, not automatically to a reducible chart.
2. The elimination ideal must be understood relative to the chart and rank-stratum constraints. A naive contraction in the ambient polynomial ring can encode the wrong closure if the chart's nonvanishing conditions have not been incorporated.

Subject to these corrections, I regard the central geometric result as sound and potentially the most important advance in the recent sequence of reports.

I will address the three questions in order, then give a revised formulation and a concrete research plan.

34_open_or_empty_dichotomy.md

## 1. Preliminary audit: the corrected rectangular-pencil formulation

The report now uses

\\[ K=\ker\begin{bmatrix}C\\\CA\end{bmatrix},\qquad N_K\in\mathbb C^{n\times k},\qquad H(R)=\mathcal L(R)N_K,\qquad H_A(R)=\mathcal L(R)AN_K. \\]

Both \\(H\\) and \\(H_A\\) are \\(q\times k\\) matrices, and the spectral pencil before quotienting is

\\[ \lambda H(R)-H_A(R). \\]

Let

\\[ \omega=\operatorname{rank}H(R). \\]

Under (5a), the induced map

\\[ \Phi_K:W_K\longrightarrow\mathbb C^q,\qquad \Phi_K(\mathcal Lv)=\mathcal LAv,\quad v\in K, \\]

is well-defined, where

\\[ W_K=\operatorname{im}H(R). \\]

Choose a subset of column indices

\\[ S=\\{s_1,\ldots,s\_\omega\\}\subseteq\\{1,\ldots,k\\} \\]

such that the columns \\(H\_{[:,S]}\\) are linearly independent. Write

\\[ H_S=H\_{[:,S]},\qquad H\_{A,S}=(H_A)\_{[:,S]}. \\]

The vectors \\(N_Ke\_{s_j}\\) give a basis of the quotient image \\(W_K\\), represented by the columns of \\(H_S\\). Therefore the reduced pencil is

\\[ P_S(R,\lambda)=\lambda H_S(R)-H\_{A,S}(R), \\]

a \\(q\times\omega\\) pencil with full-column-rank leading coefficient:

\\[ \operatorname{rank}H_S(R)=\omega. \\]

The spectral condition is

\\[ (5b)\iff \operatorname{rank}P_S(R,\lambda)=\omega \quad\text{for every }\lambda\in\mathbb C. \\]

Equivalently,

\\[ (5b)\iff \gcd\\{\text{all }\omega\times\omega \text{ minors of }P_S(R,\lambda)\\}\in\mathbb C^\times. \\]

This is the correct rectangular criterion. It is important that the minors are the \\(\binom q\omega\\) maximal minors of the reduced \\(q\times\omega\\) pencil—not the minors of the unreduced \\(q\times k\\) matrix. The column chart is what makes the reduced pencil explicit.

### 1.1 The two corrections in the report are right

I agree with both repairs:

- The charts must be chosen by columns of \\(H\\), because \\(W_K=\operatorname{im}H\\).
- In a rectangular pencil, the criterion involves all maximal minors, not one determinant.

The retraction in II.2 is also correct. If \\(k\<q\\) and \\(\omega=k\\), then the reduced pencil is \\(q\times k\\) with full column rank in its leading coefficient. It need not lose column rank at any finite \\(\lambda\\). A single maximal minor can vanish without the entire collection of maximal minors vanishing.

The square case remains special. If \\(\omega=q>0\\), the reduced pencil is square and its determinant has degree \\(q\\), with nonzero leading coefficient. Over \\(\mathbb C\\), it has a finite root. Thus

\\[ \boxed{\omega=q>0\implies (5b)\text{ fails}.} \\]

This is a useful necessary restriction on feasible rank strata.

## 2. Question 1: is the bad locus closed, or only constructible?

### 2.1 General elimination theory alone gives only the closure

Let \\(U\\) be a parameter space and suppose

\\[ p_1(R,\lambda),\ldots,p_N(R,\lambda) \\]

are polynomials in \\(R\\) and \\(\lambda\\). Define the bad set

\\[ \mathcal B= \left\\{R\in U: \exists\lambda\in\mathbb C,\  p_1(R,\lambda)=\cdots=p_N(R,\lambda)=0 \right\\}. \\]

Let

\\[ I=\langle p_1,\ldots,p_N\rangle \subseteq\mathbb C[R,\lambda]. \\]

The elimination ideal

\\[ I\cap\mathbb C[R] \\]

defines the Zariski closure of the projection of \\(V(I)\\) onto parameter space. In general,

\\[ V(I\cap\mathbb C[R]) = \overline{\mathcal B}^{\\,Z}, \\]

and this need not equal \\(\mathcal B\\).

A standard example is

\\[ I=\langle R\lambda-1\rangle \subseteq\mathbb C[R,\lambda]. \\]

Its projection onto the \\(R\\)-line is

\\[ \mathcal B=\mathbb C\setminus\\{0\\}, \\]

which is not closed. But

\\[ I\cap\mathbb C[R]=(0), \\]

so its elimination variety is all of \\(\mathbb C\\).

Thus the report is right to ask whether the particular pencil structure prevents this phenomenon. It does.

### 2.2 The decisive extra property: the leading coefficient has full column rank

Fix a rank stratum and a column chart \\(S\\), so that

\\[ P_S(R,\lambda)=\lambda H_S(R)-H\_{A,S}(R), \qquad \operatorname{rank}H_S(R)=\omega \\]

for every \\(R\in U\\).

Let

\\[ p_1(R,\lambda),\ldots,p_N(R,\lambda), \qquad N=\binom q\omega, \\]

be all the \\(\omega\times\omega\\) minors of \\(P_S\\).

Each \\(p_i\\) has degree at most \\(\omega\\) in \\(\lambda\\). Homogenise it:

\\[ p_i^{\mathrm h}(R;\alpha,\beta) = \beta^\omega p_i\\!\left(R,\frac{\alpha}{\beta}\right). \\]

Because \\(P_S\\) is linear in \\(\lambda\\), this is simply the corresponding maximal minor of

\\[ \alpha H_S(R)-\beta H\_{A,S}(R). \\]

Consider the incidence variety

\\[ \mathcal X= \left\\{ (R,[\alpha:\beta])\in U\times\mathbb P^1: p_i^{\mathrm h}(R;\alpha,\beta)=0 \text{ for every }i \right\\}. \\]

It is closed in \\(U\times\mathbb P^1\\), because it is defined by homogeneous polynomial equations in \\([\alpha:\beta]\\) with coefficients polynomial in \\(R\\).

Now examine the point at infinity:

\\[ [\alpha:\beta]=[1:0]. \\]

At that point,

\\[ \alpha H_S-\beta H\_{A,S}=H_S. \\]

Since \\(H_S\\) has full column rank \\(\omega\\), at least one of its maximal minors is nonzero. Therefore the homogeneous maximal minors cannot all vanish at infinity.

Consequently, every point of \\(\mathcal X\\) has \\(\beta\ne0\\). In other words, the projective incidence condition is exactly the original finite-\\(\lambda\\) common-root condition; compactification has introduced no spurious root at infinity.

Finally, the projection

\\[ \operatorname{pr}:U\times\mathbb P^1\longrightarrow U \\]

is a proper morphism, because \\(\mathbb P^1\\) is projective. Proper morphisms are closed. Hence

\\[ \mathcal B=\operatorname{pr}(\mathcal X) \\]

is closed in \\(U\\).

This proves the key assertion:

Established, subject to the chart hypotheses

\\[ \boxed{ \mathcal B_S = \\{R\in U: \text{the maximal minors of }P_S(R,\lambda) \text{ have a common finite complex root}\\} \text{ is Zariski closed in }U. } \\]

The complementary feasible set

\\[ \mathcal F_S=U\setminus\mathcal B_S \\]

is therefore Zariski open in \\(U\\).

This is the proof I would put in the next report. It is short, conceptual, and directly explains why the general counterexample to closedness does not apply here.

### 2.3 An alternative proof using projective eigenvectors

There is a second proof, closely tied to the invariant-line interpretation.

For each \\(R\in U\\), the leading coefficient \\(H_S(R)\\) identifies the \\(\omega\\)-dimensional space \\(W_K\\) with \\(\mathbb C^\omega\\). A rank drop occurs exactly when there are

\\[ [x]\in\mathbb P^{\omega-1} \quad\text{and}\quad \lambda\in\mathbb C \\]

such that

\\[ (\lambda H_S-H\_{A,S})x=0. \\]

Equivalently,

\\[ H\_{A,S}x=\lambda H_Sx. \\]

Because \\(H_S\\) is injective, \\(H_Sx\ne0\\) for \\(x\ne0\\). Thus the bad condition says that the induced map sends some nonzero vector into the line represented by that vector.

This can be expressed without \\(\lambda\\):

\\[ H\_{A,S}x\wedge H_Sx=0. \\]

These are homogeneous quadratic equations in the projective coordinates \\(x\\). The incidence set in

\\[ U\times\mathbb P^{\omega-1} \\]

is closed, and its projection to \\(U\\) is closed because projective space is proper.

This proof makes the geometry especially transparent: the bad set is the parameter locus for which the induced map has an invariant line.

I slightly prefer the \\(\mathbb P^1\\) proof for the elimination discussion, and the projective-eigenvector proof for the conceptual geometry.

### 2.4 The irreducible open-or-empty dichotomy

Now let \\(U\\) be irreducible. Since \\(\mathcal B_S\\) is closed in \\(U\\), exactly one of the following holds:

1. \\(\mathcal B_S=U\\), so every candidate in the chart is spectrally bad and\
   \\[\
   \mathcal F_S=\varnothing;\
   \\]
2. \\(\mathcal B_S\subsetneq U\\), so \\(\mathcal F_S\\) is a nonempty Zariski-open dense subset of \\(U\\).

Thus the report's dichotomy is correct on an irreducible chart:

\\[ \boxed{ \mathcal F_S=\varnothing \quad\text{or}\quad \mathcal F_S\text{ is Zariski-open dense in }U. } \\]

There is no third possibility on an irreducible base.

But the irreducibility qualification is essential.

If \\(U\\) is reducible, one component may be entirely bad while another has a nonempty open feasible subset. For example,

\\[ U=U_1\cup U_2,\qquad \mathcal B=U_1. \\]

Then

\\[ \mathcal F=U_2. \\]

The feasible set is neither empty nor dense in all of \\(U\\), although it is open in \\(U\\).

Therefore, the correct general statement is:

> On each irreducible component of each rank stratum and column chart, the feasible locus is either empty or open dense in that component.

This is the version I recommend using throughout the project.

### 2.5 A necessary qualification: the chart must include the admissibility conditions

The reduced pencil represents the original spectral condition only when (5a) holds, because (5a) is what makes \\(\Phi_K\\) well-defined on \\(W_K\\).

Thus the base of the projective incidence construction should be the admissible part of the rank stratum, not merely

\\[ \\{R:\operatorname{rank}H(R)=\omega\\}. \\]

A suitable base is

\\[ U\_{\omega,S} = \left\\{ R: \begin{array}{l} \operatorname{rank}H(R)=\omega,\\\ \operatorname{rank}\begin{bmatrix}\mathcal LA(R)\\\B(R)\end{bmatrix} =\operatorname{rank}B(R),\\\ H\_{[:,S]}(R)\text{ has full column rank} \end{array} \right\\}, \\]

where

\\[ B(R)=\begin{bmatrix}\mathcal L(R)\\\CA\\\C\end{bmatrix}. \\]

This is a locally closed algebraic set, or a finite union of such sets if one has not yet separated its irreducible components.

There is a second chart-level detail. Selecting the column set \\(S\\) specifies which columns form a basis, but the condition that these columns are independent is itself a union of principal open sets:

\\[ \bigcup\_{\substack{T\subseteq\\{1,\ldots,q\\}\\\\|T|=\omega}} \left\\{\det H\_{T,S}\ne0\right\\}. \\]

For a geometric proof, this union is perfectly acceptable as one column chart. For a literal affine-coordinate-ring calculation, it is cleaner to refine it further by choosing both \\(S\\) and a row set \\(T\\), and localising at

\\[ g\_{S,T}(R)=\det H\_{T,S}(R). \\]

This distinction does not invalidate the report's column-chart approach. It simply makes the algebraic implementation precise.

## 3. The elimination-ideal correction: the crucial distinction

This is the most important correction I would make to Part II.4 and II.5.

Let \\(U\\) be an irreducible affine chart with coordinate ring \\(A\\), which is an integral domain. Let

\\[ J=\langle p_1,\ldots,p_N\rangle\subseteq A[\lambda] \\]

be generated by the maximal minors of the reduced pencil, and put

\\[ E=J\cap A. \\]

By the closed-projection result,

\\[ \mathcal B=V_U(E). \\]

Now there are three possibilities:

| Elimination ideal \\(E\\) in \\(A\\) | Bad set \\(\mathcal B\\)      | Feasible set \\(U\setminus\mathcal B\\) |
| ------------------------------------ | ----------------------------- | --------------------------------------- |
| \\(E=(0)\\)                          | \\(\mathcal B=U\\)            | Empty                                   |
| \\(0\ne E\ne A\\)                    | Proper nonempty closed subset | Nonempty open dense                     |
| \\(E=A\\)                            | \\(\mathcal B=\varnothing\\)  | All of \\(U\\)                          |

This table is the correct algebraic form of the dichotomy.

### 3.1 Why “proper ideal” is not the feasibility test

In standard commutative-algebra terminology, an ideal \\(E\\) is proper if \\(E\ne A\\).

But both

\\[ E=(0) \\]

and

\\[ 0\ne E\ne A \\]

are proper ideals in an integral domain. They correspond to opposite answers:

- \\(E=(0)\\): every candidate is bad; no feasible candidate exists.
- \\(0\ne E\ne A\\): the bad set is a proper closed subset; generic candidates are feasible.

So the condition

\\[ E\text{ is a proper ideal} \\]

does not decide feasibility.

The relevant condition is

\\[ \boxed{E\ne(0).} \\]

On an irreducible chart, this is equivalent to the bad set being a proper subset, hence to the existence of feasible candidates over the algebraically closed field.

There is also the special case \\(E=A\\), in which every candidate is feasible.

### 3.2 The geometric meaning is dominance

Let

\\[ \mathcal X= \left\\{ (R,[\alpha:\beta])\in U\times\mathbb P^1: p_i^{\mathrm h}(R;\alpha,\beta)=0\ \forall i \right\\}. \\]

The projection

\\[ \pi:\mathcal X\to U \\]

has image \\(\mathcal B\\).

Since \\(\pi\\) is projective, its image is closed. If \\(U\\) is irreducible, then:

- \\(E=(0)\\) precisely when \\(\mathcal B=U\\), i.e. when \\(\pi\\) is surjective;
- \\(E\ne(0)\\) precisely when \\(\mathcal B\ne U\\), i.e. when \\(\pi\\) is not dominant;
- \\(E=A\\) precisely when \\(\mathcal B=\varnothing\\).

Thus the right geometric problem is:

> Determine whether the projective incidence projection \\(\pi:\mathcal X\to U\\) is dominant.

This is much more precise than saying “decide whether the elimination ideal is proper.”

### 3.3 The elimination contraction does describe the actual bad set here

The report's concern about whether elimination gives only the closure is resolved by the projective argument.

In general,

\\[ V(J\cap A) \\]

is the closure of the projection of \\(V(J)\\). Here, however, the projection is closed because of the projective compactification and the full-column-rank leading coefficient. Consequently,

\\[ \boxed{ \mathcal B=V_U(J\cap A) } \\]

set-theoretically.

Strictly speaking, the contraction need not be radical, so the equality is an equality of algebraic sets, not necessarily of ideals. If the goal is to identify the reduced defining ideal of the bad locus, one should use

\\[ \sqrt{J\cap A}. \\]

For a chart described by nonvanishing conditions, the contraction should be computed in its localised coordinate ring. If the chart is represented in the ambient polynomial ring by \\(g\ne0\\), one must account for that localisation—for example, by saturation with respect to \\(g\\)—rather than silently treating the chart as the whole affine space.

This is a real repair to the report, but it strengthens rather than weakens its main result.

## 4. Question 2: what known type of problem is this, and what does that imply for complexity?

The corrected formulation places the problem in a recognisable area of computational algebraic geometry:

\\[ \boxed{\text{dominance testing for a projective incidence projection}} \\]

or, equivalently in the present setting,

\\[ \boxed{\text{generic rank-drop testing for a parameterised polynomial matrix}.} \\]

The object is not merely a generic elimination ideal. It is an elimination problem with a special geometric guarantee: the projection is closed.

This opens up a more focused algorithmic direction.

### 4.1 The relevant computational task

For each irreducible chart \\(U\\), the problem is to decide whether

\\[ \pi:\mathcal X\to U \\]

is surjective.

Equivalently, determine whether

\\[ E=J\cap A \\]

is the zero ideal or not.

If \\(U\\) is affine and irreducible, this can also be phrased as a dimension test:

\\[ \mathcal B=U \quad\Longleftrightarrow\quad \dim\mathcal B=\dim U, \\]

because \\(\mathcal B\\) is closed in \\(U\\). Therefore

\\[ \boxed{ \text{there is a feasible point over }\mathbb C \quad\Longleftrightarrow\quad \dim\mathcal B<\dim U. } \\]

This includes the empty bad locus, with the convention \\(\dim\varnothing=-\infty\\).

That is potentially useful because one may be able to compute the dimension of the image without computing a full Gröbner basis for the entire elimination ideal.

### 4.2 What standard algebraic algorithms can offer

There are several possible approaches:

(i) Gröbner-basis elimination.\
Compute a Gröbner basis of \\(J\\) in an elimination order and extract \\(J\cap A\\). This is conceptually direct. Its worst-case complexity can be very high, and the number of variables and polynomial degrees may grow substantially with the matrix dimensions.

(ii) Dimension and dominance algorithms.\
Rather than compute the entire elimination ideal, test whether the projection has image of full dimension. This is exactly the question of dominance. Dimension computations, transcendence-degree calculations, and elimination can sometimes be more efficient than constructing all equations of the image.

(iii) Generic-fibre methods.\
The projection is surjective if and only if its fibre is nonempty over every point of \\(U\\). Because the projection is projective and \\(U\\) is irreducible, surjectivity is equivalent to the generic fibre being nonempty. This suggests studying the fibre over the function field \\(\mathbb C(U)\\). In suitable formulations, the question becomes whether the maximal minors have a common root over an algebraic closure of \\(\mathbb C(U)\\).

This is an especially promising viewpoint. It replaces the universal parameter statement by a single computation over a rational-function field.

There is a subtlety: the generic fibre must be interpreted after passing to the correct function field of the irreducible chart, and the projective incidence equations must include the chart's rank and admissibility conditions.

### 4.3 A useful generic-fibre reformulation

Let

\\[ F=\mathbb C(U) \\]

be the function field of an irreducible chart. Consider the polynomial matrix

\\[ P_S(\lambda)=\lambda H_S-H\_{A,S} \\]

over \\(F[\lambda]\\).

Then the bad projection is dominant if and only if the maximal minors of this generic pencil have a common root over an algebraic closure \\(\overline F\\).

Equivalently,

\\[ \gcd\_{F[\lambda]} \\{\text{maximal minors of }P_S(\lambda)\\} \\]

is nonconstant.

Why is this equivalence useful? Because a finite collection of univariate polynomials over a field has a common root over the algebraic closure exactly when its gcd has positive degree. Thus the generic badness question can be reduced to a univariate gcd computation over the function field.

This is a much more focused algorithmic problem than eliminating \\(\lambda\\) from a large collection of multivariate polynomials.

There is one important caveat: the pencil is defined on the chart, and the entries of \\(H_S,H\_{A,S}\\) may be rational functions when one passes to a coordinate representation of the chart. This is not a problem in the function field, but the denominators and the defining equations of the chart must be handled correctly.

### 4.4 What this says—and does not say—about NP-hardness

This reformulation does not establish polynomial-time solvability.

Computing a gcd of univariate polynomials over a field is efficient in the degree and coefficient representation of those polynomials. But here the coefficient field is a rational-function field in many parameters, and the input includes the algebraic variety defining the chart. Symbolic coefficient growth and representation size can dominate the computation.

Nor does it establish NP-hardness. The relevant hardness question becomes whether deciding generic common-root existence for this specially structured affine pencil is hard.

I would therefore not state that the complexity of the new problem is known. The report has identified a standard geometric decision task—dominance of a projective incidence projection—but it has not yet identified a matching complexity classification for the special matrix family.

This is an important distinction: recognising the geometric problem is progress even if the complexity of the general problem is not settled.

### 4.5 A particularly promising algorithmic route: compute the generic gcd

The generic-fibre interpretation suggests a concrete next experiment.

Let \\(U\\) be an irreducible chart and \\(F=\mathbb C(U)\\) its function field. Form the reduced pencil over \\(F\\):

\\[ P_S(\lambda)=\lambda H_S-H\_{A,S}\in F[\lambda]^{q\times\omega}. \\]

Compute

\\[ g_S(\lambda)= \gcd\_{F[\lambda]} \\{\text{all }\omega\times\omega\text{ minors of }P_S(\lambda)\\}. \\]

Then, for \\(\omega>0\\),

\\[ \boxed{ \begin{aligned} \deg g_S>0 &\iff \text{the bad locus is all of }U,\\\ \deg g_S=0 &\iff \text{the bad locus is a proper closed subset of }U. \end{aligned} } \\]

The second line includes the case in which the bad locus is empty.

This is an exact generic test, not a numerical heuristic. It is also a direct way to exploit the special feature that the spectral variable is univariate.

I would prioritise this computation over a full multivariate Gröbner elimination experiment. It may reveal that the family-level question is easier than a generic elimination problem, at least on individual irreducible charts.

There are still real algorithmic issues:

- computing the irreducible components of the rank-stratum chart;
- representing the function field of each component;
- computing the gcd over that function field;
- controlling coefficient growth and the number of maximal minors;
- handling the real-point condition.

But the mathematical decision criterion itself is clean.

## 5. An important distinction: the complex geometric dichotomy does not automatically solve the real decision problem

The report defines

\\[ R\in\mathbb R^{(q-r)\times n}, \\]

while its algebraic-geometric discussion is over \\(\mathbb C\\). That is appropriate for the spectral variable, but it requires care when drawing conclusions about \\(\mathrm{DEC}(q)\\).

The closedness theorem proves a statement about the complexification of a chart:

\\[ \mathcal F\_{\mathbb C}=U\_{\mathbb C}\setminus\mathcal B\_{\mathbb C}. \\]

The actual decision problem asks whether

\\[ \mathcal F\_{\mathbb R} = \mathcal F\_{\mathbb C}\cap U(\mathbb R) \\]

is nonempty.

If \\(\mathcal B\_{\mathbb C}\subsetneq U\_{\mathbb C}\\), then \\(\mathcal F\_{\mathbb C}\\) is nonempty and Zariski open dense. But this alone does not guarantee that it contains a real point.

### 5.1 Why the implication can fail

Consider a real algebraic set whose complexification has positive dimension but whose real locus is very small. For instance,

\\[ U\_{\mathbb C}=\\{(x,y)\in\mathbb C^2:x^2+y^2=0\\}. \\]

Its real locus is just

\\[ U(\mathbb R)=\\{(0,0)\\}. \\]

Let the bad set be the origin. It is a proper closed subset of \\(U\_{\mathbb C}\\), so the complex feasible complement is nonempty and open dense. Yet

\\[ U(\mathbb R)\setminus\mathcal B(\mathbb R)=\varnothing. \\]

Thus complex generic feasibility does not imply real feasibility in complete generality.

This example is not being offered as a counterexample within the specific observer family. It illustrates the logical issue that must be addressed before using the complex dichotomy to decide the real problem.

### 5.2 When the implication does hold

A useful sufficient condition is that the real points of the irreducible chart be Zariski dense in its complexification.

For example, if an irreducible component defined over \\(\mathbb R\\) has a nonsingular real point, its real points are locally a real manifold of the expected dimension and are Zariski dense in that component.

Under this density hypothesis,

\\[ \mathcal B\_{\mathbb C}\subsetneq U\_{\mathbb C} \quad\Longrightarrow\quad U(\mathbb R)\setminus\mathcal B(\mathbb R)\ne\varnothing. \\]

Therefore, on such a component, the complex generic-gcd test decides the existence of a real feasible augmentation.

This is a promising situation, but the density condition should be proved or checked—not assumed.

### 5.3 What remains true without real-density assumptions

There is still a useful one-way statement:

\\[ \boxed{ \exists R\in U(\mathbb R)\text{ feasible} \quad\Longrightarrow\quad \mathcal B\_{\mathbb C}\ne U\_{\mathbb C}. } \\]

A real feasible point is also a complex feasible point, so the complex bad set cannot be the entire complex chart.

The converse requires the real-density condition or a separate real-point argument.

This has two consequences for the project:

1. The complex geometric analysis can eliminate many impossible charts.
2. A final algorithm for \\(\mathrm{DEC}(q)\\) must also determine whether the open complex feasible locus contains a real point.

The second step may be much easier than arbitrary semialgebraic feasibility on charts with dense real loci. But it is not automatically absent.

### 5.4 A correction to the random-search interpretation

The report says that a single random feasible \\(R\\) certifies feasibility, while failure to find one proves nothing. I agree with the first statement, subject to exact verification of (5a) and (5b).

The second statement is also correct, but there is a practical qualification: random sampling must be performed within the relevant rank stratum and chart.

If the feasible set is contained in a lower-dimensional stratum such as

\\[ \\{r_3=0\\}\setminus\\{r_4=0\\}\subset\mathbb R^4, \\]

then a continuously sampled point in the ambient \\(\mathbb R^4\\) hits that hyperplane with probability zero. The fact that the feasible set is open dense inside the hyperplane does not make it likely to be found by sampling the ambient parameter space.

A sound experimental protocol is therefore:

- first identify the relevant rank stratum;
- parameterise or sample that stratum;
- sample within the chosen column chart;
- verify the resulting candidate exactly over the rationals or an appropriate algebraic number field.

A numerically small singular value is not an exact feasibility certificate.

## 6. Question 3: should the next attack be chart-level, stratum-level, or global?

My answer is: use all three, but give them different roles.

### 6.1 The chart is the right unit for local computation

The chart is where the reduced pencil has a fixed basis:

\\[ P_S(R,\lambda)=\lambda H_S(R)-H\_{A,S}(R). \\]

This is the right place to:

- write down the maximal minors;
- homogenise the spectral variable;
- compute the generic gcd over the function field;
- test dominance of the incidence projection;
- produce an explicit feasible witness when one exists.

So I would formulate the local theorem at the chart level.

### 6.2 The irreducible component is the right unit for the dichotomy

A chart need not be irreducible. The open-or-empty conclusion applies componentwise.

Therefore, for each \\((\omega,S)\\), decompose the admissible chart into irreducible components

\\[ U\_{\omega,S}=\bigcup\_{\nu}U\_{\omega,S,\nu}. \\]

On each component,

\\[ \mathcal F\_{\omega,S,\nu} = \varnothing \quad\text{or}\quad \mathcal F\_{\omega,S,\nu} \text{ is open dense}. \\]

For real feasibility, also determine whether the component has a sufficiently large real locus, or directly test whether its real points meet the feasible open set.

This is the correct unit for statements involving genericity and function fields.

### 6.3 The stratum is the right unit for structural theorems

A rank stratum fixes \\(\omega\\), and hence fixes:

- the dimension of the quotient image;
- the size of the reduced pencil;
- the degree bound in \\(\lambda\\);
- the number \\(\binom q\omega\\) of maximal minors;
- the projective dimension of the invariant-line incidence.

Structural statements about all candidates with a given \\(\omega\\) should therefore be made at the stratum level.

For example, the square-stratum obstruction

\\[ \omega=q>0\implies\text{infeasible} \\]

is a stratum-level theorem, not a chart-specific observation.

### 6.4 The whole decision problem is the right unit for complexity

The global decision problem is a finite disjunction:

\\[ \mathrm{DEC}(q) \iff \bigvee\_{\omega,S,\nu} \left[ \text{the corresponding real feasible locus is nonempty} \right]. \\]

The chart-level computations are the local subroutines. The stratum-level structure controls which subroutines are relevant. But NP-hardness, polynomial-time solvability, and \\(\exists\mathbb R\\)-membership are properties of the whole input-to-answer problem.

I would not try to establish hardness for an isolated chart unless the reduction can guarantee that all other charts and strata behave in a controlled way. Otherwise, a source instance might be accepted through an unintended chart.

### 6.5 How I would revise the proposed \\(q\_{\min}\\) formula

The report writes

\\[ q\_{\min} = \min\left\\{ q: \exists\\,\omega<\min(q,k),\ \exists S: \mathcal B_S^{(q)}\subsetneq U_S^{(q)} \right\\}. \\]

As a complex-geometric statement, this is a useful summary, provided the chart is replaced by its irreducible components and (5a) is included in the base.

For the actual real decision problem, I would state instead:

\\[ \boxed{ q\_{\min} = \min\left\\{ q: \exists\\,\omega,\ S,\ \nu: \left(U\_{\omega,S,\nu}\setminus \mathcal B\_{\omega,S,\nu}\right)(\mathbb R) \ne\varnothing \right\\}. } \\]

Here:

- \\(U\_{\omega,S,\nu}\\) is an irreducible component of the admissible rank-\\(\omega\\) column chart;
- \\(\mathcal B\_{\omega,S,\nu}\\) is its relative closed bad locus;
- the real-point condition is explicit.

If real points are Zariski dense in every relevant component, the last condition simplifies to

\\[ \mathcal B\_{\omega,S,\nu}\subsetneq U\_{\omega,S,\nu}. \\]

That is the simplification I would aim to prove for the specific determinantal varieties arising in the project.

## 7. A more precise answer to Question 3: what would count as an algorithm or a hardness result?

The report asks whether it is sensible to prove that an elimination ideal is proper for all plant data of a certain type, or unit for all plant data of another type.

I would reformulate this question using the three cases in the elimination-ideal table.

For an irreducible chart with coordinate ring \\(A\\), the three cases are:

\\[ \begin{array}{c|c} E=(0) & \text{all candidates are bad}\\\ 0\ne E\ne A & \text{generic candidates are feasible}\\\ E=A & \text{all candidates are feasible}. \end{array} \\]

### 7.1 What a useful universal algorithm theorem would look like

A meaningful positive theorem would be something like:

> For every plant in a specified class, there exists an order \\(q\\), a rank stratum \\(\omega\\), and an admissible real chart component \\(U\\) such that the generic reduced pencil has constant maximal determinantal divisor.

In the notation above, this says

\\[ \deg\gcd\_{F[\lambda]} \\{\text{maximal minors of }P_S(\lambda)\\}=0. \\]

Under an appropriate real-density condition, it would imply the existence of a real feasible augmentation on that component.

This would be much more useful than merely proving that the elimination ideal is proper in the usual sense. It would give a structural existence theorem and potentially a constructive route to an augmentation.

There is a further distinction between:

- proving that some feasible augmentation exists;
- giving a polynomial-time algorithm to find one;
- giving a polynomial-time algorithm to find the minimum feasible order.

These are different results. The open-or-empty theorem helps with the first, and perhaps the second, but does not by itself settle the third.

### 7.2 What a useful hardness construction would look like

For a reduction from a source decision problem \\(L\\), the construction should map an input instance \\(x\\) to rational plant data such that

\\[ x\in L \quad\Longleftrightarrow\quad \mathrm{DEC}(q)\text{ is feasible}. \\]

At the chart level, one possible design would be to arrange that:

- in a YES instance, at least one admissible real chart component has \\(E\ne(0)\\);
- in a NO instance, every admissible real chart component has \\(E=(0)\\), or has no real feasible points for another explicitly controlled reason.

But the reduction must control all charts and rank strata. It is not sufficient to encode the source instance into one selected chart if another chart can yield a feasible augmentation regardless of the source answer.

Also, \\(E=A\\) is not the natural condition for a NO instance. It means the bad locus is empty, so every candidate on that chart is feasible. A hardness reduction may use any of the three cases, but it must state exactly how the source answer corresponds to them.

### 7.3 Why I would not try to prove a universal “all data” theorem immediately

A universal result across all plant data is attractive, but the data may change:

- \\(\dim K\\);
- the rank profile of \\(\mathcal L|\_K\\);
- the number of admissible rank strata;
- the number of nonempty chart components;
- the existence and density of real points on those components.

These variations are precisely where the complexity may reside.

I would first classify a few natural structural classes, such as:

1. \\(k\\) fixed;
2. \\(q\\) fixed;
3. \\(q-r\\) fixed;
4. \\(\omega\\) fixed;
5. \\(\dim K\\) fixed with \\(n\\) growing.

The objective is not merely to find a tractable subcase. It is to identify which dimensions actually control the algebraic computation.

## 8. Further suggestions: exploit polynomial-matrix algorithms before enumerating all minors

There is one algorithmic direction I would add to the report.

The gcd of all maximal minors of a polynomial matrix is its maximal determinantal divisor. It is a standard invariant in polynomial-matrix theory.

For

\\[ P_S(\lambda)\in F[\lambda]^{q\times\omega}, \qquad q\ge\omega, \\]

with full column normal rank, let

\\[ d\_\omega(\lambda) = \gcd\\{\text{all }\omega\times\omega\text{ minors of }P_S(\lambda)\\}. \\]

The spectral condition is

\\[ d\_\omega(\lambda)\in F^\times \\]

when the coefficient field is \\(F\\), and the generic-badness test is

\\[ \deg d\_\omega>0. \\]

The Smith normal form of a polynomial matrix over the Euclidean domain \\(F[\lambda]\\) provides a way to compute this invariant without explicitly expanding and listing every maximal minor. In terms of the invariant factors \\(s_1,\ldots,s\_\omega\\),

\\[ d\_\omega(\lambda) \sim \prod\_{i=1}^{\omega}s_i(\lambda), \\]

where \\(\sim\\) means equality up to a nonzero constant in \\(F\\).

This suggests a potentially important improvement:

> Instead of computing \\(\binom q\omega\\) maximal minors and then taking their gcd, compute the maximal determinantal divisor directly using polynomial-matrix normal-form algorithms.

### 8.1 Why this matters

The number of maximal minors can be enormous. A polynomial-matrix normal-form algorithm may avoid that combinatorial expansion.

At the level of arithmetic operations in the coefficient field, this is a plausible route to an efficient generic-badness test.

However, there is a serious qualification: the coefficient field is

\\[ F=\mathbb C(U), \\]

the function field of an algebraic chart. Its elements are rational functions modulo the defining equations of that component. Arithmetic in \\(F\\) may itself be expensive.

Therefore, one must distinguish:

- polynomial complexity in matrix dimensions and degree, measured in field operations over \\(F\\);
- bit complexity when the original data are rational and encoded in binary.

The first may be achievable using polynomial-matrix algorithms. The second requires controlling the representation and coefficient growth of elements of the function field.

Still, I consider this a promising algorithmic experiment. It directly exploits the univariate nature of the spectral parameter and may avoid the worst feature of the original Bézout encoding.

### 8.2 A concrete experiment

For each irreducible chart component:

1. Construct its function field \\(F\\).
2. Express \\(H_S\\) and \\(H\_{A,S}\\) over \\(F\\).
3. Form \\(P_S(\lambda)=\lambda H_S-H\_{A,S}\\).
4. Compute its Smith form or maximal determinantal divisor.
5. Record \\(\deg d\_\omega\\).

This produces an exact answer to the complex generic question on that component.

I would compare three methods:

- direct maximal-minor gcd;
- Smith/Popov form;
- subresultant-based gcd computation.

The comparison should record not only runtime but also coefficient growth, degrees of intermediate expressions, and the representation size of function-field elements.

## 9. What I would preserve, correct, and add in the next report

### Preserve

I would preserve the following as established mathematical results:

1. The retraction of the false claim for \\(k\<q\\).
2. The correct rectangular maximal-minor criterion.
3. The use of column charts for \\(W_K=\operatorname{im}H\\).
4. The projective closedness argument for the bad locus.
5. The open-or-empty dichotomy on irreducible components.

These are not merely corrections to earlier mistakes. Together they establish a useful geometric structure.

### Correct

I would make the following changes:

1. Replace “the elimination ideal is proper” with “the elimination ideal is nonzero” when the intended conclusion is that the bad locus is a proper subset of an irreducible chart.
2. Explicitly distinguish the cases \\(E=(0)\\), \\(0\ne E\ne A\\), and \\(E=A\\).
3. State that the dichotomy is componentwise.
4. Form the base chart inside the (5a)-admissible locus.
5. Use the coordinate ring of the locally closed chart, with localisation or saturation where necessary.
6. Separate complex generic feasibility from real feasibility.
7. Correct the \\(q\_{\min}\\) formula to include real points and irreducible components.

### Add

I would add three propositions.

Proposition A — Closedness of the bad locus.\
On every admissible column chart of fixed rank \\(\omega>0\\), the set of parameters for which the reduced pencil loses column rank at some finite complex \\(\lambda\\) is Zariski closed relative to the chart.

Proposition B — Componentwise dichotomy.\
On each irreducible component of an admissible chart, the feasible locus is either empty or Zariski open dense.

Proposition C — Generic-gcd criterion.\
Let \\(F\\) be the function field of an irreducible chart component. The bad locus equals the entire component if and only if the maximal determinantal divisor of the generic reduced pencil has positive degree in \\(\lambda\\).

Proposition C is the bridge to the algorithmic programme.

## 10. My overall assessment and recommended direction

I regard this report as a substantial advance. The important change is that the project has moved from the statement

> “the feasible set is constructible”

to the much stronger statement

> “on each irreducible admissible chart, the bad spectral locus is closed, and the feasible locus is either empty or open dense.”

That is a meaningful geometric dichotomy. It is not a complexity classification, but it gives the complexity question a much more precise form.

My revised recommendation is:

Priority 1 — Prove the projective closedness theorem

Do next

Use the \\(\mathbb P^1\\) compactification of the spectral parameter. Emphasise that the full-column-rank leading coefficient excludes infinity. State the result relative to the admissible chart.

Priority 2 — Derive the generic-gcd test

Do next

Pass to the function field of each irreducible chart component and compute the maximal determinantal divisor. This is the most direct way to test whether the bad projection is dominant.

Priority 3 — Resolve the real-point issue

Essential

Determine whether the real loci of the relevant rank-stratum components are Zariski dense. Without this, complex generic feasibility is not yet a solution to the real decision problem.

Priority 4 — Complexity reduction

After the above

Study hardness for generic rank-drop of affine rectangular pencils, then investigate whether that problem embeds into the observer-induced family.

### My view on the eventual complexity

The new result makes me somewhat more optimistic about finding an algorithm for fixed structural regimes than I was after the previous report. The generic-gcd reduction is a much more focused computational object than unrestricted real-algebraic feasibility.

But I would not infer that the unrestricted problem is easy. The difficult parts may simply have moved into:

- decomposition of the rank strata;
- computation of their function fields;
- the real-point problem;
- the number of candidate orders, ranks, and charts;
- the arithmetic complexity of polynomial-matrix normal forms over function fields.

I would therefore maintain the hypothesis that the unrestricted problem may be hard, but revise the immediate research strategy: first determine whether the generic-gcd problem admits an efficient symbolic solution on the observer-induced charts. That is a much more targeted experiment than attempting an NP-hardness reduction now.

The most valuable next deliverable would be a rigorous theorem with the following conclusion:

\\[ \boxed{ \begin{gathered} \text{For every irreducible admissible chart }U,\text{ the generic reduced pencil}\\\ P_S(\lambda)\text{ has a nonconstant maximal determinantal divisor}\\\ \Longleftrightarrow \text{every complex candidate in }U\text{ is spectrally bad}. \end{gathered} } \\]

Then add the real-density condition under which the converse generic-feasibility conclusion gives a real augmentation.

That theorem would put the project on a much firmer foundation. It would also clarify whether \\(q1\\) is fundamentally a problem of polynomial-matrix computation, real algebraic geometry, or the combinatorics of choosing a rank stratum and chart.

In short: I agree with the central open-or-empty insight, but I would correct the elimination-ideal terminology, make the result componentwise, and separate complex genericity from real feasibility. Once those points are settled, the function-field gcd and polynomial-matrix normal-form route is, in my view, the best next direction.