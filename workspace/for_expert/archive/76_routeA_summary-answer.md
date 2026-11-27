# Route A: the incidence obstruction is real, but it is not a general impossibility theorem

My assessment is that the decomposition in Part II.2 is correct, provided the matrices have the stated dimensions and \\(N^+\\) is a genuine left inverse. The main strategic conclusion, however, needs to be more nuanced:

- A single incidence condition is not an arbitrary affine equation in the entries of \\(H\\).
- A family of incidence conditions can nevertheless encode arithmetic, because incidence geometry has its own universality phenomena.
- For this observer architecture, the hard question is whether the available incidences are sufficiently expressive after accounting for the dependence of \\(RE\\) on the same free matrix \\(R\\).

So I would not declare Route A closed. I would stop trying to identify each ARM affine equation with one incidence, and instead investigate whether a small collection of observer incidences can implement a projective-arithmetic gadget system.

There is also a useful distinction between two possible targets: encoding ARM(3) literally, and reducing from an incidence-realization problem that is already \\(\exists\mathbb R\\)-hard. The latter is likely the cleaner route.

## 1. Check of the decomposition

Let \\(N\in\mathbb R^{n\times k}\\) have full column rank, and let \\(N^+\in\mathbb R^{k\times n}\\) satisfy

\\[ N^+N=I_k. \\]

Define

\\[ M=N^+AN,\qquad E=(I-NN^+)AN. \\]

Then indeed

\\[ AN=NM+E, \\]

because

\\[ NM+E =NN^+AN+(I-NN^+)AN =AN. \\]

Also,

\\[ N^+E=0. \\]

Thus \\(E\\) is the component of \\(AN\\) transverse to \\(\operatorname{im}N\\), relative to the chosen projection \\(NN^+\\).

With \\(Y=RN\\), the compressed matrices are

\\[ H= \begin{bmatrix} L_0N\\\ Y \end{bmatrix} = \begin{bmatrix} H_0\\\Y \end{bmatrix}, \\]

and

\\[ H_A=LAN = \begin{bmatrix} L_0AN\\\ RAN \end{bmatrix} = \begin{bmatrix} H\_{A,0}\\\ RNM+RE \end{bmatrix} = \begin{bmatrix} H\_{A,0}\\\ YM+RE \end{bmatrix}. \\]

Since every row of \\(YM\\) is a linear combination of rows of \\(Y\\), and \\(Y\\) is a block of \\(H\\),

\\[ \operatorname{row}(YM)\subseteq\operatorname{row}(H). \\]

Using the given equivalence

\\[ (5a)\iff \operatorname{row}(H_A)\subseteq\operatorname{row}(H), \\]

we obtain

\\[ \boxed{ (5a)\iff \operatorname{row}(H\_{A,0})\subseteq\operatorname{row}(H) \quad\text{and}\quad \operatorname{row}(RE)\subseteq\operatorname{row}(H). } \\]

So the boxed equivalence in the report is correct, with one notational refinement: \\(H\_{A,0}\in\operatorname{row}H\\) should mean that every row of \\(H\_{A,0}\\) belongs to \\(\operatorname{row}H\\), not that the whole matrix is a single row vector.

### Is the choice of left inverse legitimate?

Yes. Any left inverse gives a valid decomposition. But \\(M\\) and \\(E\\) individually depend on the choice of \\(N^+\\).

The invariant object is the quotient map

\\[ \overline A:\operatorname{im}N\longrightarrow \mathbb R^n/\operatorname{im}N, \qquad Nz\longmapsto ANz+\operatorname{im}N. \\]

The matrix \\(E\\) is a representative of this quotient action in the chosen complement. Changing the left inverse changes the representative, but not the quotient class of \\(AN\\) modulo \\(\operatorname{im}N\\).

This matters for the research programme: a proposed gadget should ideally be formulated in terms of the quotient map, or be shown invariant under a change of complement. Otherwise, the construction may depend on an arbitrary coordinate choice.

## 2. The rank-one \\(E\\) case: distinguish rank one from one nonzero column

The report's special-case calculation is correct if \\(E\\) has exactly one nonzero column. But there are two different assumptions:

1. \\(E\\) has rank one;
2. \\(E\\) has only one nonzero column.

If the only nonzero column is column \\(j\\), with value \\(e_a\\), then \\(RE\\) has only one possibly nonzero column, equal to \\(Re_a\\). Hence

\\[ \operatorname{row}(RE)= \begin{cases} \\{0\\},&Re_a=0,\\\ \operatorname{span}\\{e_j^\top\\},&Re_a\ne0. \end{cases} \\]

Thus

\\[ \boxed{ \operatorname{row}(RE)\subseteq\operatorname{row}(H) \iff Re_a=0 \quad\text{or}\quad e_j^\top\in\operatorname{row}(H). } \\]

That is right.

If \\(E\\) merely has rank one, write

\\[ E=ab^\top. \\]

Then

\\[ RE=(Ra)b^\top, \\]

and the corresponding condition is

\\[ \boxed{ Ra=0 \quad\text{or}\quad b^\top\in\operatorname{row}(H). } \\]

So a rank-one \\(E\\) still gives at most one projective direction, but that direction need not be a coordinate vector.

For general \\(E\\), it is not correct to think of each column as giving an independent incidence condition. The rows of \\(RE\\) are linear combinations of the rows of \\(E\\), and the entire row space of \\(RE\\) must be contained in \\(\operatorname{row}(H)\\). The columns interact through the same two rows of \\(R\\).

## 3. The actual geometry of Route A when \\(\omega=3\\)

There is a useful structural simplification specific to your proposed dimensions.

You have \\(q=4\\), two fixed rows and two free rows. Write

\\[ H= \begin{bmatrix} H_0\\\Y \end{bmatrix}, \qquad H_0\in\mathbb R^{2\times k}, \quad Y\in\mathbb R^{2\times k}. \\]

Suppose

\\[ \operatorname{rank}H_0=2, \qquad \operatorname{rank}H=3. \\]

Set

\\[ S_0=\operatorname{row}(H_0), \qquad U=\operatorname{row}(H). \\]

Then \\(U\\) is a three-dimensional subspace containing the fixed two-dimensional subspace \\(S_0\\). Therefore \\(U/S_0\\) is a line in the quotient space

\\[ V=\mathbb R^k/S_0. \\]

Let \\(\pi:\mathbb R^k\to V\\) be the quotient map. The row-space conditions become

\\[ \pi(y_1),\ \pi(y_2),\ \pi(z_1),\ \pi(z_2) \quad\text{all lie in one common line of }V, \\]

where \\(z_1,z_2\\) are the rows of \\(RE\\).

Equivalently,

\\[ \boxed{ \operatorname{rank} \begin{bmatrix} \pi(y_1)\\\ \pi(y_2)\\\ \pi(z_1)\\\ \pi(z_2) \end{bmatrix} \le1. } \\]

This is a rank-one determinantal condition on a matrix whose entries are linear in \\(R\\).

That is more informative than viewing the problem as an arbitrary collection of incidences. It says that the architecture has a very particular form: the two variable rows and their two transverse images must all determine the same projective direction after quotienting out the fixed rows.

### 3.1 A useful dichotomy from the fixed rows

The other part of (5a) requires

\\[ \operatorname{row}(H\_{A,0})\subseteq U. \\]

Define

\\[ T=\operatorname{span}\big( \operatorname{row}(H_0), \operatorname{row}(H\_{A,0}) \big). \\]

There are two cases.

Case I: \\(\dim T=3\\).

Then \\(U=T\\) is already determined by the fixed data. All the conditions on \\(Y\\) and \\(RE\\) are ordinary linear containment conditions in a fixed subspace. This case is unlikely to carry the desired nonlinear hardness.

Case II: \\(\dim T=2\\).

Then \\(U\\) is a variable three-plane containing \\(T\\). Equivalently, \\(U/T\\) is a projective point in \\(\mathbb P(V)\\). The four projected rows above must all lie on that same projective point.

This is the only interesting case for Route A in the proposed \\((q,r_0,r)=(4,2,2)\\), \\(\omega=3\\) architecture.

It is not obviously too weak: rank-one matrix varieties can encode multiplication through their \\(2\times2\\) minors. But it is also not automatically expressive enough: the entries of the rank-one matrix are not independent variables; they are linked through the common \\(R\\), \\(N\\), and \\(E\\).

My recommendation is to make Case II the precise object of study. It is a much smaller problem than the original observer synthesis problem and exposes exactly where the available degrees of freedom lie.

## 4. Question 1: is incidence-versus-affine mismatch decisive?

No. It is decisive only against the naive, one-equation-per-incidence approach.

There are two different notions of expressiveness here.

### 4.1 A single incidence is not a general affine hyperplane

Suppose \\(U\\) is a three-plane in \\(\mathbb R^k\\), represented on a coordinate chart as the row space of

\\[ [I_3\mid X], \qquad X\in\mathbb R^{3\times(k-3)}. \\]

A fixed vector \\(w=(a,b)\\), with \\(a\in\mathbb R^3\\) and \\(b\in\mathbb R^{k-3}\\), belongs to \\(U\\) exactly when

\\[ b=a^\top X. \\]

This gives \\(k-3\\) linear equations in the entries of \\(X\\), but their coefficients have a special structure: for each column \\(j\\) of \\(X\\), the equation is

\\[ b_j=\sum\_{i=1}^3 a_iX\_{ij}. \\]

One fixed vector does not give an arbitrary affine functional involving unrelated coefficients across all entries of \\(X\\).

That is the genuine local mismatch.

### 4.2 But projective incidence systems can encode arithmetic

The important counterpoint is the universality of projective and matroid realization spaces.

Mnëv's universality theorem shows, roughly, that realization spaces of rank-three oriented matroids can represent arbitrary primary semialgebraic sets up to stable equivalence. More directly relevant to complexity, Kim, de Mesmay and Miltzow prove that real matroid realizability is \\(\exists\mathbb R\\)-complete already for rank-three matroids.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://dmtcs.episciences.org\&sz=32)

dmtcs.episciences.org+1



A rank-three matroid realization can be described using vectors in \\(\mathbb R^3\\), with conditions on which triples are linearly dependent and independent. In projective language, these are collinearity and non-collinearity conditions.

This is exactly the sort of setting in which a collection of incidence conditions can simulate arithmetic. Classical projective constructions implement addition and multiplication through configurations of points and lines; universality results show that this is not merely an isolated trick.

But there is a caveat important to your problem:

- Matroid realization uses many separately specified incidences and non-incidences.
- Your observer condition does not give arbitrary point-line incidence constraints.
- In Route A, the incidences are all tied to the same \\(U\\), and the vectors being tested include \\(RE\\), which depends on the same free rows that define \\(H\\).

Thus matroid universality shows that incidence constraints are not inherently too weak. It does not show that this particular observer incidence architecture can implement a universal incidence system.

### 4.3 The mechanism that turns incidences into equations

There are two mechanisms worth investigating.

Mechanism A: projective arithmetic gadgets.

Represent a scalar by a point on a projective line. Use fixed incidence configurations to construct points representing sums and products. Then enforce the incidence relations defining the arithmetic circuit.

This is the route suggested by Mnëv universality. It would be natural if the observer variables could represent many projective points and the fixed data could represent the corresponding projective lines.

Mechanism B: rank-one matrix completion.

A rank-one matrix

\\[ Z=uv^\top \\]

satisfies

\\[ Z\_{ij}Z\_{ab}-Z\_{ib}Z\_{aj}=0. \\]

For example,

\\[ \det \begin{bmatrix} x&z\\\ 1&y \end{bmatrix}=0 \quad\Longleftrightarrow\quad z=xy. \\]

This is a direct multiplication relation. A sufficiently flexible affine matrix-completion problem can use shared entries and fixed constants to compose such relations.

The Case II geometry above naturally produces a rank-one matrix condition. So I would investigate whether its entries can be arranged into a partially specified matrix with the sharing pattern needed for an arithmetic circuit.

The crucial issue is variable sharing. A rank-one condition alone does not give a reduction: the same source variable must appear consistently in several gate locations. You need a construction showing how the same entry of the observer variables participates in multiple constraints without introducing unwanted degrees of freedom.

## 5. Question 2: which \\(\exists\mathbb R\\)-complete incidence problem should replace ARM(3)?

My first candidate is:

Real rank-three matroid realizability, or equivalently a suitably formulated rank-three projective configuration realization problem.

It is a much better conceptual match than ARM(3), because the source constraints are already rank and incidence constraints rather than arbitrary affine equations. Its \\(\exists\mathbb R\\)-completeness at rank three is established by Kim, de Mesmay and Miltzow.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://dmtcs.episciences.org\&sz=32)

dmtcs.episciences.org+1



A useful source formulation is:

- variables: vectors \\(v_1,\ldots,v_m\in\mathbb R^3\\);
- prescribed dependent triples:\
  \\[\
  \det(v_i,v_j,v\_\ell)=0;\
  \\]
- prescribed independent triples:\
  \\[\
  \det(v_i,v_j,v\_\ell)\ne0.\
  \\]

The zero determinants give incidence conditions. The nonzero determinants enforce that points do not accidentally become collinear or coincide in forbidden ways.

### 5.1 The match to the observer problem

Your observer conditions have a potentially useful division of labour:

- (5a) gives closed algebraic rank/inclusion constraints;
- (5b) gives an all-\\(\lambda\\) nondegeneracy condition.

This suggests the following high-level strategy:

| Source condition         | Possible observer role                                     |
| ------------------------ | ---------------------------------------------------------- |
| Prescribed incidence     | A row-space containment from (5a)                          |
| Prescribed non-incidence | A nondegeneracy condition, potentially involving (5b)      |
| Projective normalization | Fixed rows and affine lift constraints                     |
| Shared point or line     | Reuse of a common coordinate or common row-space direction |

However, the last column is a research proposal, not an established translation. In particular, (5b) does not give arbitrary independent nonvanishing constraints: it requires the pencil to retain full rank at every complex \\(\lambda\\). You cannot simply assume it can enforce each desired matroid non-incidence.

### 5.2 An important warning about the source problem

The usual matroid realizability input specifies both dependent and independent sets. If you use only the dependent triples, you obtain a weaker realization problem: extra dependencies may appear.

Those extra dependencies can create spurious solutions. A reduction must either:

1. enforce the required nonzero determinants; or
2. use a source problem whose completeness is already established using only the allowed positive incidence constraints.

Do not silently replace matroid realizability by its incidence-only fragment.

### 5.3 A more tailored intermediate problem

Before reducing full matroid realizability, define an intermediate problem that matches Route A exactly:

> Common-line realization problem. Given a collection of affine-linear maps \\(T_1,\ldots,T_s\\) of a common variable matrix \\(R\\), determine whether the images \\(T_i(R)\\) lie in a common one-dimensional subspace of a specified quotient vector space, subject to prescribed fixed incidences.

Your Case II construction is a special instance with the maps induced by \\(N\\) and \\(E\\).

Study this problem first. It may be possible to prove \\(\exists\mathbb R\\)-hardness for a sufficiently expressive family of maps, or it may reveal a structural limitation of the two-free-row architecture.

## 6. Question 3: can several blocks or gadgets save Route A?

The dimension count \\(q=4,r=2\\) does not, by itself, forbid a reduction. But it imposes a strong bottleneck.

In the interesting Case II, all the projected rows must lie on one common line. Adding more blocks \\(E_1,\ldots,E_t\\) gives

\\[ R E_1,\ldots,R E_t, \\]

and the condition becomes

\\[ \operatorname{row} \begin{bmatrix} Y\\\RE_1\\\ \vdots\\\RE_t \end{bmatrix} \subseteq U. \\]

After quotienting by the fixed two-plane, this still says that all projected rows lie on the same one-dimensional subspace.

Thus adding blocks does not automatically create independent gates. It creates more vectors that must share the same projective direction.

That may be useful for a projective construction, but it is not the same as giving each affine equation its own independent incidence.

### 6.1 When a block composition lemma could work

A meaningful composition theorem would need to show how a collection of local constraints can be represented by different coordinate regions while preserving the same source variables.

For example, suppose the source circuit has gates

\\[ z_i=x_iy_i. \\]

For each gate, one would like a \\(2\times2\\) minor equation

\\[ Z\_{i,11}Z\_{i,22}-Z\_{i,12}Z\_{i,21}=0. \\]

The construction must then identify entries across gates whenever the same variable appears more than once.

In Route A, all these entries would have to arise as linear functions of the same two rows of \\(R\\), and all resulting vectors would have to lie in the same \\(U\\). That is a very restrictive coupling.

I would not try to build a large block construction immediately. First test whether even two independent multiplication gates can be represented with the required variable sharing.

### 6.2 A dimension-based test that may quickly reject the architecture

Let

\\[ \mathcal W(R)= \begin{bmatrix} \pi(RN)\\\ \pi(RE) \end{bmatrix} \\]

denote the matrix of projected rows in Case II. Its rank must be at most one.

Compute the dimension of the linear image

\\[ \mathcal V= \left\\{ \begin{bmatrix} \pi(RN)\\\ \pi(RE) \end{bmatrix} :R\in\mathbb R^{2\times n} \right\\}. \\]

Then study the intersection

\\[ \mathcal V\cap \\{Z:\operatorname{rank}Z\le1\\}. \\]

If this intersection has a simple parameterization or decomposes into a small number of linear families for all possible \\(N,E\\) allowed by the observer construction, then Route A may have a genuine structural obstruction.

If, on the other hand, it can realize sufficiently general linear sections of a rank-one determinantal variety, there may be room for hardness.

This is a concrete algebraic-geometric problem. It is much more decisive than informal counting of the number of observer rows.

## 7. Question 4: Route B or Route C?

I would rank them as follows.

### Route B: spectral branch encoding

This is plausible as a branch-selection or nondegeneracy mechanism, but I would not make it the primary source of arithmetic equations.

Recall

\\[ (5b)\iff \operatorname{im}H\cap E\_\lambda(F)=\\{0\\} \quad\text{for all }\lambda\in\sigma(F). \\]

This is an avoidance condition. It is naturally suited to excluding unwanted components, preventing rank collapse, and enforcing genericity.

It is not naturally suited to imposing equations such as \\(z=xy\\).

For Route A, I would therefore use (5b) as a guard:

- rule out a degenerate projective chart;
- exclude a pure eigenspace branch;
- force a required compressed rank;
- prevent a solution from collapsing to a lower-dimensional component.

The report's earlier spectral analysis is especially relevant here: the condition is about avoiding eigenspaces, not about Hurwitz stability or about a polynomial coefficient vanishing.

### Route C: remove the fixed-\\(\kappa\_{\rm obs}\\) restriction and seek a polynomial algorithm

This is a much larger ambition. I would not prioritize a general polynomial-time algorithm without evidence that the effective dimension can be eliminated.

There is an important distinction:

- fixed \\((q,c)\\) gives bounded \\(k\\), and hence a constant-dimensional real-algebraic problem;
- fixed \\(\kappa\_{\rm obs}\\) gives a bounded number of effective compressed variables;
- neither statement implies polynomial time when the relevant parameter is allowed to grow.

The special pencil structure

\\[ P(\lambda)=\lambda H-H_A \\]

could yield more efficient algorithms than generic Smith-form computation, but that is a separate algorithm-design project. The fact that \\(P\\) is a linear pencil is helpful, but it does not by itself remove the combinatorial dependence on \\(k\\).

My choice: prioritize Route B as a supporting tool for a hardness reduction, while continuing the fixed-parameter algorithmic theory independently. Do not make a general polynomial algorithm the fallback goal yet.

## 8. Question 5: is \\(E\\) the only possible encoder?

No. \\(E\\) is the only transverse contribution from the free rows in this particular decomposition, but it is not the only place where the fixed input can encode information.

The decomposition separates the lower block as

\\[ RAN=RNM+RE. \\]

The \\(RNM\\) part is automatically in \\(\operatorname{row}(H)\\). The remaining lower-block contribution is \\(RE\\). But the upper block contributes

\\[ H\_{A,0}=L_0AN, \\]

which can impose fixed incidences on \\(U=\operatorname{row}(H)\\).

In addition, the input affects:

1. The quotient space \\(K_0\\): through \\(C\\) and \\(CA\\).
2. The quotient action of \\(A\\): through the induced map \\(\overline A\\).
3. The fixed row data: through \\(L_0N\\) and \\(L_0AN\\).
4. The transverse action: through the quotient class of \\(AN\\) modulo \\(\operatorname{im}N\\).
5. The spectral guard: through the induced \\(F\\) satisfying \\(H_A=FH\\).

So I would phrase the conclusion more precisely:

> Once \\(N\\) is fixed, the only contribution of the free rows to the failure of automatic row-space inclusion in the lower block is the transverse term \\(RE\\). The fixed block \\(H\_{A,0}\\) supplies additional fixed incidence constraints. The input matrices \\(A,C,L_0\\) can encode information through the quotient space, its induced action, the fixed incidences, and the spectral guard.

This distinction is important. It prevents the research programme from overlooking constructions in which the hard information is carried primarily by the fixed quotient geometry rather than by \\(E\\).

## 9. My recommended next steps

I would not abandon Route A today, but I would stop trying to force a direct ARM(3) embedding. Here is the order I recommend.

Step 1 — Classify the common-line variety

Fix the proposed dimensions and reduce to

\\[ \mathcal V\cap\\{Z:\operatorname{rank}Z\le1\\}. \\]

Classify the possible linear spaces \\(\mathcal V\\) arising from \\((N,E)\\). Determine whether their rank-one intersections can realize general arithmetic circuits.

Do first

Step 2 — Test a two-gate composition

Try to realize two multiplication relations with one shared source variable. If variable sharing cannot be implemented, the two-free-row architecture is probably too restrictive for a universal reduction.

Step 3 — Study rank-three matroid realization

Use it as the candidate source problem, not ARM(3). Its constraints are naturally incidence and non-incidence conditions, and its real realizability problem is \\(\exists\mathbb R\\)-complete.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://dmtcs.episciences.org\&sz=32)

dmtcs.episciences.org+1



Step 4 — Use (5b) only as a guard initially

Try to use it to eliminate degenerate branches and enforce the chosen chart. Do not ask it to encode multiplication directly.

Step 5 — Keep the algorithmic paper moving

The fixed-\\((q,c)\\) result is independent of the success of Route A. It is a solid positive result and should not be delayed by the hardness search.

## 10. Bottom line

My conclusion is:

- The algebraic decomposition is correct.
- The use of \\(N^+\\) is legitimate, though \\(E\\) itself depends on the chosen complement.
- The rank-one special case is correct, but distinguish rank-one \\(E\\) from a matrix with only one nonzero column.
- The incidence-versus-affine mismatch rules out a naive direct translation, not a general reduction.
- Rank-three matroid realizability is a much better source problem than ARM(3) for an incidence-based route.
- In your specific \\(q=4,r=2,\omega=3\\) architecture, the central object is the rank-one variety\
  \\[\
  \mathcal V\cap{Z:\operatorname{rank}Z\le1},\
  \\]\
  where \\(\mathcal V\\) is the linear image of the two free observer rows.

My recommendation is to give Route A one more tightly bounded attempt: classify that linear-section-of-rank-one-variety problem and test two-gate composition. If it fails, abandon this particular \\(q=4,r=2\\) architecture—not the broader incidence approach. The next architecture should allow several independently selectable projective directions or several coupled subspaces, rather than forcing every variable image onto one common line.