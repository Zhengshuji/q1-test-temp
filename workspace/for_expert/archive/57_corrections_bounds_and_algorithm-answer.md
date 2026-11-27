# Overall assessment

This report identifies a genuine bottleneck, but it also brings the project to a point where I would change the order of attack.

The central issue is that the compressed subspace \\(V=\ker H\\) is not, by itself, a complete parametrisation of the original matrices \\(L\\). It records the restriction of the rows of \\(L\\) to \\(K_0\\), but it does not record their components in the annihilator of \\(K_0\\). Those components are precisely where the additional independence condition involving \\(C\\) can be achieved—or can fail.

There is a useful way to formulate the problem that makes this distinction explicit:

- first, solve the compressed problem and determine which \\(V\\)'s are admissible;
- second, describe the affine space of all lifts of the compressed row map;
- third, impose the full-row-rank and independence conditions on that affine space;
- finally, impose the spectral good-locus condition.

This is not an argument against the compressed approach. It is an argument for treating the lift as a separate, structured matrix-completion problem rather than assuming that a right inverse of \\(N\\) will automatically preserve the required ranks.

I also see two substantive issues in the new component-count claims:

1. the \\(c=3\\) report says “eight layers” but enumerates eleven cases if the invariant \\(t=3\\) types are counted as written;
2. the claimed general invariant-part bound \\(p(c)n^c\\) is not justified merely by counting Jordan types. Varieties of invariant subspaces can themselves be reducible.

I would resolve these before using the component bounds as the basis of a general theorem.

The most promising immediate direction is therefore not to abandon \\(c=2\\), and not to move prematurely to \\(c=3\\). It is to solve the lift problem exactly, beginning with a linear-algebraic characterisation of the rank condition \\(\operatorname{rank}[C;L]=p+q\\). That may turn the current obstruction into a clean necessary-and-sufficient lifting criterion.

# 1. Question 1: The blocked lifting algorithm

I believe there is a standard construction here, and it is more explicit than solving the entire problem in the original \\(L\\)-variables from scratch.

The key is to use the exact sequence induced by restriction of row functionals to \\(K_0\\). It gives a necessary-and-sufficient criterion for completing the compressed rows to rows that are independent modulo \\(C\\).

This is the most important new observation I would suggest investigating.

## 1.1 First clarify the rank requirement

The original conditions stated in Part I require \\(L\\) to have full row rank. They do not, as written, require

\\[ \operatorname{rank}\begin{bmatrix}C\\\L\end{bmatrix}=p+q. \\]

The latter is strictly stronger. It says that the rows of \\(L\\) are linearly independent modulo the row space of \\(C\\).

If this is an additional requirement of the intended synthesis problem, it should be stated explicitly. If it is not, the two failed constructions may be rejecting valid solutions to the original problem.

For the rest of this section, I assume that the intended requirement really is

\\[ \operatorname{rank}\begin{bmatrix}C\\\L\end{bmatrix}=p+q. \tag{R} \\]

I also initially assume that \\(C\\) has full row rank \\(p\\). If not, replace \\(p\\) by \\(\operatorname{rank}C\\) throughout.

Notice that (R) automatically implies

\\[ \operatorname{rank}L=q. \\]

Thus, under (R), there is no need to impose the latter as a separate condition.

## 1.2 The restriction exact sequence

Write

\\[ D_C=\begin{bmatrix}C\\\CA\end{bmatrix}, \qquad K_0=\ker D_C. \\]

Let \\(\mathcal X=\mathbb C^n\\), and use row vectors for linear functionals. Consider the restriction map

\\[ \rho:\mathcal X^\*/\operatorname{row}C \longrightarrow K_0^\*, \qquad [\ell]\longmapsto \ell|\_{K_0}. \\]

Its kernel consists of the row functionals that vanish on \\(K_0\\), modulo those already in \\(\operatorname{row}C\\). Since

\\[ K_0^\perp=\operatorname{row}\begin{bmatrix}C\\\CA\end{bmatrix}, \\]

we obtain the exact sequence

\\[ 0\longrightarrow \frac{\operatorname{row}[C;CA]}{\operatorname{row}C} \longrightarrow \frac{\mathcal X^\*}{\operatorname{row}C} \overset{\rho}{\longrightarrow} K_0^\* \longrightarrow0. \tag{1} \\]

Define

\\[ E_C=\frac{\operatorname{row}[C;CA]}{\operatorname{row}C}, \qquad d_C=\dim E_C =\operatorname{rank}[C;CA]-\operatorname{rank}C. \\]

The interpretation is important:

- \\(K_0^\*\\) records the compressed row of \\(L\\);
- \\(E_C\\) records the freedom in lifting that row without changing its restriction to \\(K_0\\);
- this freedom is exactly the part that is invisible to \\(H=LN\\), but can be used to make \\([C;L]\\) have full row rank.

This is the missing piece in the attempted construction using \\(N_K^+\\).

## 1.3 Exact lifting criterion

Suppose \\(H=LN\\) is prescribed, with

\\[ H=\begin{bmatrix}H_0\\\H_1\end{bmatrix}, \qquad H_0=L_0N, \\]

where \\(H_1\\) is the prescribed compressed bottom block.

Let

\\[ \bar H:\mathbb C^q\longrightarrow K_0^\* \\]

denote the linear map whose rows are the prescribed compressed rows. Its rank is \\(\omega\\).

Let

\\[ \mathcal N_H=\ker \bar H^{\\,\*} \\]

be the space of linear dependencies among the \\(q\\) compressed rows. In coordinates, this is simply the left nullspace of \\(H\\), and

\\[ \dim\mathcal N_H=q-\omega. \\]

Let

\\[ \mathcal N_0 = \\{(a,0)\in\mathbb C^r\oplus\mathbb C^{q-r}: a^{\mathsf T}H_0=0\\}. \\]

Because \\(L_0\\) is fixed, the lift of a dependency in \\(\mathcal N_0\\) is already determined.

Here is the useful criterion.

Proposition (completion criterion modulo \\(C\\)). Suppose

\\[ \operatorname{rank}\begin{bmatrix}C\\\L_0\end{bmatrix}=p+r. \tag{2} \\]

Then there exist bottom rows \\(R\\) with prescribed compression \\(RN=H_1\\) such that

\\[ \operatorname{rank}\begin{bmatrix}C\\\L_0\\\R\end{bmatrix}=p+q \\]

if and only if

\\[ \boxed{q-\omega\le d_C.} \tag{3} \\]

Here the bottom rows are allowed to vary by arbitrary elements of\
\\(\operatorname{row}[C;CA]\\) without changing their prescribed restrictions to \\(K_0\\).

Proof.

Take any lifts of the \\(q\\) prescribed compressed rows to

\\[ \mathcal X^\*/\operatorname{row}C. \\]

They define a linear map

\\[ \widetilde H:\mathbb C^q \longrightarrow \mathcal X^\*/\operatorname{row}C. \\]

The row classes are independent modulo \\(C\\) precisely when \\(\widetilde H\\) is injective.

If \\(a\in\ker\bar H^\*\\), then the corresponding linear combination of lifted rows restricts to zero on \\(K_0\\), so it lies in \\(E_C\\). Consequently,

\\[ \ker\bar H^\* \longrightarrow E_C,\qquad a\longmapsto \widetilde H(a) \tag{4} \\]

is well-defined.

Since any linear dependence among the lifted rows must first be a dependence among their restrictions to \\(K_0\\), the lifted rows are independent if and only if (4) is injective.

On \\(\mathcal N_0\\), the map (4) is fixed by \\(L_0\\). Assumption (2) implies that this fixed restriction is injective: a nonzero combination of the top rows cannot vanish modulo \\(C\\).

The bottom rows can be adjusted independently by arbitrary elements of \\(E_C\\). Thus we can extend the already injective map on \\(\mathcal N_0\\) to an injective map on all of \\(\mathcal N_H\\) if and only if

\\[ \dim\mathcal N_H\le\dim E_C. \\]

This is exactly (3). \\(\square\\)

This proposition gives a precise explanation of why a Moore–Penrose or arbitrary right-inverse lift can fail: it chooses one particular representative of each compressed row, whereas full row independence requires a suitable choice of the components in \\(E_C\\).

## 1.4 Consequence for \\(q=\omega+1\\)

In your target case,

\\[ q=\omega+1, \\]

so

\\[ q-\omega=1. \\]

The completion criterion reduces to

\\[ \boxed{ \operatorname{rank}[C;L_0]=p+r, \qquad \operatorname{rank}[C;CA]-\operatorname{rank}C\ge1. } \tag{5} \\]

Under these two conditions, every prescribed compressed bottom block can be lifted so that \\([C;L]\\) has full row rank, provided the top block \\(L_0\\) is kept fixed.

This is a particularly useful result. It says that, in the \\(q=\omega+1\\) case, the rank completion itself does not require enumerating different \\(V\\)'s or solving the spectral problem. It is a simple dimension test.

There is one important qualification: the proposition assumes that the bottom rows can be varied freely in the kernel of restriction, namely by arbitrary rows in \\(\operatorname{row}[C;CA]\\). This is exactly the freedom available when only the compressed pair is fixed. If your lifting equations impose additional restrictions on those components beyond (5a), those restrictions must be included separately.

## 1.5 Why (5a) does not obstruct this completion

The rank condition (5a) is equivalent to

\\[ \ker[L;CA;C]\subseteq\ker LA. \\]

Since

\\[ K_0=\ker[C;CA], \\]

this becomes

\\[ v\in K_0,\ Lv=0 \quad\Longrightarrow\quad LAv=0. \\]

In compressed coordinates this is precisely

\\[ \boxed{\ker H\subseteq\ker H_A.} \tag{6} \\]

Thus (5a) depends only on the compressed pair \\((H,H_A)\\), not on which representatives of the rows are chosen in the exact sequence (1).

This is the decisive point: once (6) holds, adding arbitrary rows from \\(\operatorname{row}[C;CA]\\) to the bottom block preserves (5a). It does not change \\(H\\) or \\(H_A\\).

Consequently, if the completion criterion above applies, one can first construct a compressed pair satisfying (5a), then choose the invisible lift components to enforce (R), and finally test (5b).

## 1.6 What I recommend implementing

For a fixed admissible compressed pair, do not use \\(N_K^+\\) as the final lift. Instead:

1. Compute a particular lift \\(L^{(0)}\\) satisfying\
   \\[\
   L^{(0)}N=H.\
   \\]
2. Compute a basis \\(G\\) of\
   \\[\
   E_C=\operatorname{row}[C;CA]/\operatorname{row}C.\
   \\]
3. Add arbitrary linear combinations of these basis rows to the bottom block:\
   \\[\
   L=\
   L^{(0)}+\
   \begin{bmatrix}0\XG\end{bmatrix}.\
   \\]\
   Here the top block is unchanged.
4. Choose \\(X\\) so that the induced map (4) is injective.
5. Verify \\([C;L]\\) has rank \\(p+q\\), and then test the spectral condition.

For \\(q=\omega+1\\), the kernel in (4) is one-dimensional. The construction reduces to choosing the single remaining dependency direction so that its lift is nonzero in \\(E_C\\).

This is a much simpler problem than a general matrix completion.

My answer to Question 1: I would not abandon the compressed approach. I would add this exact lifting layer. Directly solving for \\(L\\) is a valid alternative, but it obscures the useful separation between the compressed spectral problem and the rank-completion problem.

# 2. Question 2: The good-locus criterion and the two-branch system

There is a logical issue in the report's current formulation that I would resolve before formalising anything.

## 2.1 The pencil descends for every admissible \\(V\\), not only for \\(t=2\\)

You state that

\\[ V=\ker H \\]

and that (5a) implies

\\[ \ker H\subseteq\ker H_A. \\]

Therefore, for every \\(v\in V\\),

\\[ Hv=0,\qquad H_Av=0. \\]

It follows immediately that

\\[ P(\lambda)v=(\lambda H-H_A)v=0 \qquad\forall\lambda. \\]

Thus \\(P(\lambda)\\) vanishes on \\(V\\), and hence factors through the quotient:

\\[ \boxed{ \overline P(\lambda): K_0/V\longrightarrow\mathbb C^q. } \\]

This is true for every \\(t=\dim(V\cap A^{-1}V)\\), not just \\(t=2\\).

Since

\\[ \dim(K_0/V)=k-c=\omega \\]

and \\(\operatorname{rank}H=\omega\\), the induced map \\(\overline H\\) is injective. Choose a basis of \\(K_0/V\\) and a suitable basis of \\(\mathbb C^q\\) so that

\\[ \overline H= \begin{bmatrix} I\_\omega\\\ 0 \end{bmatrix}. \\]

Write the corresponding matrix for \\(\overline H_A\\) as

\\[ \overline H_A= \begin{bmatrix} A\_\*\\\ B\_\* \end{bmatrix}, \\]

where

\\[ A\_\*\in\mathbb C^{\omega\times\omega}, \qquad B\_\*\in\mathbb C^{(q-\omega)\times\omega}. \\]

Then the transformed pencil is

\\[ \boxed{ \overline P(\lambda)= \begin{bmatrix} \lambda I\_\omega-A\_\*\\\ -B\_\* \end{bmatrix}. } \tag{7} \\]

Consequently,

\\[ \operatorname{rank}P(\lambda)<\omega \\]

if and only if

\\[ \exists\\,0\ne y\in\mathbb C^\omega: \quad A\_\*y=\lambda y,\qquad B\_\*y=0. \tag{8} \\]

This is exactly the block criterion you already have.

The value of \\(t\\) is irrelevant to this descent. The descent follows from (5a), not from the equality \\(W=V\\).

For \\(q=\omega+1\\), \\(B\_\*\\) is a single row. The pencil is good precisely when that row is nonzero on every eigenspace of \\(A\_\*\\).

This should hold for all admissible \\(V\\), including \\(t=0\\) and \\(t=1\\).

## 2.2 The two-branch equations need to be reinterpreted

You report the system

\\[ x^{\mathsf T}(\lambda H_0-A\_{11})=\alpha B_1, \qquad x^{\mathsf T}A\_{12}=-\alpha B_2, \tag{9} \\]

with branches \\(\alpha=0\\) and \\(\alpha\ne0\\).

I cannot verify (9) as an equivalent formulation without the exact definitions of the block matrices \\(H_0,A\_{11},A\_{12},B_1,B_2\\), the dimensions of \\(x\\), and the transformation that produces these blocks.

However, under the hypotheses stated in this report, there is no need for a separate two-branch formulation to test the spectral goodness of \\(P\\). Equation (7) already gives the exact criterion.

If (9) arises from a different elimination problem—perhaps one that includes additional restrictions on the lift \\(L\\)—then it may be useful, but it should not be described as the general spectral criterion for \\(P\\) without a proof of equivalence to (8).

There is also a conceptual point about the branches:

- \\(\alpha=0\\) is a homogeneous constrained eigenvector condition;
- \\(\alpha\ne0\\) can be normalised to \\(\alpha=1\\), producing an affine system.

That is a legitimate algebraic decomposition. But the nonzero-\\(\alpha\\) branch is not guaranteed to be nonempty. It is nonempty exactly when the corresponding affine equations have a solution. No general conclusion follows from \\(c=2\\) alone.

## 2.3 Is “affine eigenvalue obstruction” standard terminology?

I would not introduce “affine eigenvalue obstruction” as a standard term without a specific reference.

Depending on the exact block structure, more established language may be appropriate:

- constrained eigenvalue problem, if one seeks an eigenpair satisfying linear side constraints;
- generalised eigenvalue problem, if the equations have the form \\((\lambda E-A)x=0\\);
- Rosenbrock system matrix pencil or transmission-zero condition, if the block matrix arises from a state-space system with input/output constraints.

The last terminology is particularly relevant if the blocks in (9) have the form of a system matrix pencil. It would be premature to identify your system with a Rosenbrock pencil until the precise block correspondence has been established.

### Recommendation

Before formalising (9), perform a statement-fidelity check:

1. Write the exact matrix pencil whose rank drop is being tested.
2. Give the invertible row and column transformations leading to (9).
3. Check that the transformations preserve the rank condition for every \\(\lambda\\).
4. Prove that the union of the \\(\alpha=0\\) and \\(\alpha\ne0\\) branches is exactly the rank-drop locus.
5. Verify that \\(\alpha\ne0\\) can be normalised to \\(1\\) without changing the equations.

Until this is done, I would use (7)–(8) for the spectral part.

# 3. Question 3: General \\(c\\), invariant-part bounds, and determinantal strata

There are two separate issues here.

## 3.1 The invariant-part bound \\(p(c)n^c\\)

I would not yet accept this as a proved component bound.

The reason is that a Jordan-type classification of the restriction

\\[ A|\_V:V\to V \\]

classifies the possible similarity types of the restricted operator. It does not, by itself, prove that the set of \\(A\\)-invariant \\(c\\)-planes of a given type is irreducible.

The relevant varieties are varieties of invariant subspaces, equivalently certain quiver Grassmannians for the representation of \\(\mathbb C[x]\\) defined by \\(A\\).

Such varieties can have nontrivial component structure. Springer fibres are a central family of examples of varieties parametrising flags compatible with a nilpotent operator, and their irreducible components are a substantial subject in their own right. See Im, Lai, and Wilbert, A study of irreducible components of Springer fibers using quiver varieties (2022).&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车



This does not prove that your particular fixed-\\(c\\) invariant-subspace strata are reducible for \\(c=2\\) or \\(c=3\\). It does show that irreducibility cannot be inferred merely from the Jordan type.

There is a useful distinction:

- the set of possible Jordan types of \\(A|\_V\\) is finite;
- the locus of \\(V\\)'s realising a fixed type may have several irreducible components.

For \\(c=2\\), your explicit parameterisations may establish irreducibility case by case. For general \\(c\\), a separate argument is required.

I would therefore revise the invariant-part claim to:

> There are at most \\(p(c)n^c\\) possible coarse eigenvalue/Jordan-type labels for invariant \\(c\\)-planes, but this is not yet a bound on the number of irreducible components.

That statement is defensible. A component bound requires control of the geometry within each type.

## 3.2 Are the determinantal strata \\(S\_{t,u}\\) irreducible?

In general, no such conclusion follows from the fact that they are determinantal strata.

Let

\\[ D=K_0\cap A^{-1}K_0,\qquad A_0=A|\_D:D\to K_0, \\]

and consider

\\[ S\_{t,u} = \left\\{ W\in\operatorname{Gr}(t,D): \dim(W+A_0(W))=u \right\\}. \\]

On the Grassmannian, this is a rank-exact locus for the bundle map

\\[ \mathcal S\oplus\mathcal S \longrightarrow K_0\otimes\mathcal O, \qquad (w_1,w_2)\longmapsto w_1+A_0w_2. \\]

It is locally closed, because it is defined by vanishing of minors of size \\(u+1\\) and nonvanishing of at least one minor of size \\(u\\).

But a rank-exact locus of a matrix of linear forms is not automatically irreducible. It may be reducible, even when the ambient Grassmannian is irreducible.

This is the central obstacle in the general component-bound conjecture.

### What can be proved unconditionally

The following two statements are sound.

Theorem A — finite determinantal stratification.

For fixed \\(c\\), the base incidence space admits a finite locally closed stratification indexed by

\\[ 0\le t\le c,\qquad t\le u\le2t. \\]

Theorem B — relative Grassmannian fibre theorem.

Over each \\(S\_{t,u}\\), the extension spaces form a relative Grassmannian

\\[ \operatorname{Gr}(c-u,K_0/U), \\]

and exactness is an open rank condition.

Thus the total incidence space over each base stratum is an open subvariety of a relative Grassmannian.

If the base stratum is irreducible and the relevant open subset is nonempty, the corresponding total space is irreducible.

These theorems are valuable, but they do not imply a general component bound.

## 3.3 Recommended references

For the algebraic geometry of determinantal loci and relative Grassmannians, I would start with the following standard references:

- Harris, Algebraic Geometry: A First Course. Useful for Grassmannians, determinantal varieties, incidence varieties, and dimension arguments.
- Bruns and Vetter, Determinantal Rings. A more algebraic treatment of determinantal ideals and rank loci.
- Hartshorne, Algebraic Geometry, Chapter II. Useful for vector bundles, projective bundles, and relative constructions.
- Weyman, Cohomology of Vector Bundles and Syzygies. More advanced, particularly relevant if you pursue determinantal geometry and resolutions.

For the quiver viewpoint:

- Caldero and Reineke, “On the quiver Grassmannian in the acyclic case,” Journal of Pure and Applied Algebra 212 (2008), 2369–2380. This is a natural starting point, but do not interpret its existence as an irreducibility theorem for arbitrary quiver Grassmannians.
- Im, Lai, and Wilbert, “A study of irreducible components of Springer fibers using quiver varieties,” Journal of Algebra 591 (2022), 217–248. This is useful precisely because it illustrates the nontrivial component geometry that can arise in closely related invariant-subspace problems.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

  科学直通车



My recommendation is to use the quiver-Grassmannian language to identify the base varieties, but to avoid claiming that the general theory automatically gives irreducibility.

# 4. Question 4: References for the four requested topics

## 4.1 Polynomial generalised inverses and degree bounds

Your minor–Bézout construction is sufficiently elementary that it can be presented as a self-contained theorem. It is not necessary to rely on a specialised reference for the exact bound \\(2\omega-2\\).

Nevertheless, two useful references are:

1. A. Fabiano and V. Marino, “Bounds for the degree of the entries of generalized inverses of polynomial matrices,” Rendiconti dell’Istituto di Matematica dell’Università di Trieste 22 (1990), 126–135. This is directly concerned with degree bounds for polynomial generalised inverses.&#x20;

   [image](https://www.google.com/s2/favicons?domain=https://www.openstarts.units.it\&sz=32)

   openstarts.units.it

2. “Computing generalized inverse of polynomial matrices by interpolation,” Applied Mathematics and Computation. This is useful for computational constructions and degree estimates, although it is not the source of your particular minor–Bézout argument.&#x20;

   [image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

   科学直通车



I would keep your proof self-contained:

- maximal minors have degree at most \\(\omega\\);
- their gcd is constant;
- the Bézout coefficients can be chosen with degree below the degree of one selected nonzero minor;
- the embedded-adjugate identity gives \\(PYP=P\\);
- the degree bound follows.

That is clearer than citing a general polynomial-matrix inverse theorem and then adapting it.

## 4.2 Irreducibility of incidence varieties

The references above—Harris, Bruns–Vetter, Hartshorne, and Weyman—are appropriate for the determinantal and relative-Grassmannian portions.

For quiver Grassmannians, Caldero–Reineke is a useful entry point. The Springer-fibre literature is also important because it warns against assuming irreducibility.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车



I would not expect a single standard theorem to imply irreducibility of all your \\(S\_{t,u}\\). The matrices involved depend on the fixed pair \\((\iota,A_0)\\), and the rank-exact strata retain information about that pair.

## 4.3 Real analogue of the fibre theorem

The algebraic statement works over \\(\mathbb R\\) with no difficulty.

Let all vector spaces and maps be real, and define

\\[ \Phi_V:V\to\mathcal X/V. \\]

Then

\\[ \ker\Phi_V=V\cap A^{-1}V \\]

and

\\[ \operatorname{rank}\Phi_V=c-t \\]

are valid over \\(\mathbb R\\). The corresponding fibre is an open subset of the real Grassmannian

\\[ \operatorname{Gr}\_{\mathbb R}(c-u,K_0/U). \\]

The important issue is nonemptiness.

For a fixed real \\(W\\), if the exactness condition defines a nonempty Zariski-open subset of the real Grassmannian, that open subset has real points. The real points of a real Grassmannian are Zariski dense in its complexification.

But the existence of a complex base point \\(W\\) does not imply the existence of a real base point. Therefore the real feasibility question is:

1. Does the base stratum contain a real \\(W\\)?
2. For some such real \\(W\\), is the open fibre nonempty?

This is the correct real analogue. It separates the real-point problem on the base from the open-fibre problem.

A useful general reference for real algebraic geometry is:

\- Bochnak, Coste, and Roy, Real Algebraic Geometry.

It is the standard reference for real loci, semialgebraic sets, and real algebraic feasibility.

## 4.4 Complexity of \\(\exists\mathbb R\\) and related matrix problems

The most useful general reference is:

\- Schaefer, Cardinal, and Miltzow, “The Existential Theory of the Reals as a Complexity Class: A Compendium.”

It gives a systematic account of \\(\exists\mathbb R\\), membership, hardness reductions, and a large collection of algebraic and geometric problems.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://research-portal.uu.nl\&sz=32)

Utrecht University



The compendium discusses, among other things, the \\(\exists\mathbb R\\)-completeness of minimum and maximum matrix-rank problems and of minimum rank of a linear combination of matrices.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencestack.ai\&sz=32)

sciencestack.ai



This is relevant background, but it does not imply that your fixed-\\(c\\) augmentation problem is \\(\exists\mathbb R\\)-hard.

For your problem, the bounded-degree polynomial certificate gives a natural route to membership. The remaining question is whether the admissibility and lifting constraints can encode a known \\(\exists\mathbb R\\)-hard problem.

A useful methodological warning: an arbitrary matrix-rank feasibility problem can be hard even when the rank threshold is small, but your matrices have special structure induced by \\(A,C,L_0\\), the compressed pencil, and the fixed number of added rows. A hardness reduction must preserve those structural restrictions.

# 5. Question 5: What should be the next step?

My recommendation is:



Recommended direction

&#x20;Resolve the exact lifting problem first, then finish the \\(c=2\\) feasibility algorithm.



I would rank the options as follows.

| Direction                                      | Recommendation        | Reason                                                                                                  |
| ---------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------- |
| \\(c=2\\) feasibility                          | First                 | Close to a complete structural description; the lift obstruction may now have a simple exact criterion. |
| \\(c=3\\) feasibility                          | Second                | Valuable, but more complicated incidence strata and more opportunities for reducibility.                |
| Complexity and \\(\exists\mathbb R\\)-hardness | Parallel, exploratory | Worth investigating, but a hardness reduction may be much more difficult than completing \\(c=2\\).     |
| General component bounds                       | Later                 | The general determinantal strata are not known to be irreducible.                                       |

## 5.1 Why \\(c=2\\) is still the best target

You have already developed:

- six admissible layers;
- exact conditions for each layer;
- the good-locus criterion;
- formalised rank and kernel identities;
- a bounded-degree polynomial certificate.

The missing part was the compatibility of the compressed rows with the original rank conditions.

The exact sequence (1) gives a direct way to address that issue. In the target case \\(q=\omega+1\\), the additional independence requirement reduces to a one-dimensional completion problem.

This is a much more promising bottleneck than the earlier approach of constructing \\(R\\) by a pseudoinverse.

## 5.2 Do not yet make \\(\exists\mathbb R\\)-hardness the main project

It is reasonable to ask whether the \\(c=2\\) problem is already \\(\exists\mathbb R\\)-complete. But the fact that other rank-constrained matrix problems are \\(\exists\mathbb R\\)-complete is not sufficient evidence.

The first question should be whether the \\(c=2\\) problem has a polynomial-time exact algorithm under a suitable rational input model.

If it does, that would be a strong and useful result. If the problem remains difficult despite the explicit low-dimensional layer classification, then a hardness investigation becomes more compelling.

The complexity programme should proceed in this order:

1. define the input encoding;
2. prove membership in \\(\exists\mathbb R\\);
3. identify the remaining nonlinear constraints after the lifting criterion;
4. investigate whether those constraints can encode a known hard problem;
5. only then attempt a reduction.

For the current project, I would not claim that \\(c=2\\) is likely \\(\exists\mathbb R\\)-complete. There is not enough evidence either way.

# 6. Question 6: Should the \\(t=2\\) block criterion be formalised?

I would formalise the general block criterion, but I would not formalise it as a special \\(t=2\\) theorem.

The key observation in Section 2 is that the pencil descends through \\(K_0/V\\) for every admissible \\(V\\), because (5a) gives

\\[ \ker H\subseteq\ker H_A. \\]

Thus the block criterion is independent of \\(t\\).

I would recommend the following formal theorem:

Compressed pencil criterion. Suppose

\\[ H:\mathbb C^k\to\mathbb C^q \\]

has rank \\(\omega\\), and

\\[ \ker H\subseteq\ker H_A. \\]

Then \\(H_A\\) induces a map on \\(\mathbb C^k/\ker H\\), and there exist bases in which the induced pencil is

\\[ \begin{bmatrix} \lambda I\_\omega-A\_\*\\\ -B\_\* \end{bmatrix}. \\]

For each \\(\lambda\\),

\\[ \operatorname{rank}P(\lambda)<\omega \iff \exists y\ne0: \quad A\_\*y=\lambda y,\quad B\_\*y=0. \\]

This is a stable theorem with a clean mathematical statement. It is a worthwhile formalisation target.

I would not formalise the two-branch system (9) until the transformations and equivalence proof are written down. The risk is not primarily a difficult theorem; it is a statement-fidelity error. It may be describing a different pencil or a different elimination problem.

The most important check is whether the two-branch equations are meant to test:

- the spectral condition (5b) for the compressed pencil; or
- an additional condition arising from the lift.

Those are different problems. The first is already solved by the block criterion above. The second may genuinely require a separate affine branch.

# 7. Question 7: The robust rank identity

I would retain the robust identity as the primary statement:

\\[ \boxed{ \operatorname{rank} \begin{bmatrix}P\\\Q\end{bmatrix} + \bigl(2-\operatorname{rank}[v,Av]\bigr) =\delta. } \tag{10} \\]

It is the right formal statement and avoids truncated natural subtraction.

For the paper, I would present it in the following form.

Theorem. Under the hypotheses of the hyperplane construction,

\\[ \operatorname{rank} \begin{bmatrix}P\\\Q\end{bmatrix} + 2-\operatorname{rank}[v,Av] =\delta. \\]

Since \\(v\ne0\\),

\\[ \operatorname{rank}[v,Av]\in\\{1,2\\}. \\]

Therefore

\\[ \operatorname{rank} \begin{bmatrix}P\\\Q\end{bmatrix} = \begin{cases} \delta-1,&Av\in\mathbb Cv,\\\\[1mm] \delta,&Av\notin\mathbb Cv. \end{cases} \\]

The second display is valid whenever the corresponding case is possible; the first case requires \\(\delta\ge1\\), and the second requires \\(\delta\ge2\\). The robust identity automatically handles the boundary cases.

This is more informative than simply writing the subtraction formula with a nonnegativity hypothesis.

# 8. A correction to the new component-count report

There are two issues I would resolve before accepting II.4.

## 8.1 The \\(c=3\\) layer count is inconsistent

The report says there are eight layers, but its enumeration gives:

- six invariant \\(t=3\\) types;
- two \\(t=2\\) types;
- two \\(t=1\\) types;
- one \\(t=0\\) type.

That is eleven cases, not eight.

The six invariant types should be listed carefully as:

1. three distinct eigenvalues;
2. one eigenvalue with semisimple multiplicity three;
3. one eigenvalue with Jordan type \\(2+1\\);
4. one eigenvalue with Jordan type \\(3\\);
5. two eigenvalues, with a semisimple double eigenvalue and a distinct simple eigenvalue;
6. two eigenvalues, with a Jordan block of size two and a distinct simple eigenvalue.

This list is exhaustive for a three-dimensional complex operator, but the parameter spaces associated with those types must still be analysed.

## 8.2 Irreducibility of a parameter space must be proved, not inferred from its label

For \\(c=2\\), the six-layer argument is plausible and can be justified case by case:

- distinct-eigenvalue planes are parametrised by products of projective eigenspaces;
- scalar planes are parametrised by Grassmannians;
- Jordan planes are parametrised by a projective linear base with affine fibres;
- invariant-line extensions are open subsets of relative Grassmannians;
- non-invariant-line planes are images of open subsets of projective spaces;
- the \\(t=0\\) stratum is open in a Grassmannian.

Each of these constructions can give an irreducible parameter space when nonempty. One must still check that the map from the parameter space to the actual layer has irreducible image, and that the stated layer is exactly that image.

For \\(c=3\\), however, I would not accept the same conclusion without a separate proof for each invariant type and for the \\(t=2,\dim U=3\\) stratum.

In particular, the locus

\\[ \left\\{ W\in\operatorname{Gr}(2,D): \dim(W+A_0(W))=3 \right\\} \\]

is a rank-exact determinantal locus. It is not automatically irreducible.

Similarly, invariant-subspace varieties can have multiple components. The quiver-Grassmannian and Springer-fibre literature makes this a genuine concern, not merely a technicality.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车



I would therefore provisionally accept the \\(c=2\\) component bound after a written irreducibility proof, but I would suspend the \\(c=3\\) bound until the eleven strata have been checked individually.

# 9. Recommended work plan

I would now organise the project around the following six tasks.

1. Establish the exact lift-completion theorem.

   Prove the exact sequence (1), the dependency-map criterion (4), and the necessary-and-sufficient condition (3). Verify that the top block satisfies \\(\operatorname{rank}[C;L_0]=p+r\\).
2. Clarify the intended rank requirement.

   Decide whether \\(\operatorname{rank}[C;L]=p+q\\) is part of the original problem or an additional design constraint. Do not mix it with the weaker requirement that \\(L\\) have full row rank.
3. Use the universal compressed block criterion.

   Replace the \\(t=2\\)-specific goodness test with the quotient-pencil construction (7)–(8), valid for all \\(t\\), assuming (5a).
4. Complete the \\(c=2\\) algorithm.

   Combine the six admissible layers, the lift-completion theorem, and the polynomial gcd test. Give an exact algorithm with a precise coefficient-field model.
5. Audit the \\(c=3\\) component bound.

   Correct the layer count, then prove irreducibility of every stratum or replace the claimed bound by a bound on the number of explicitly described parameter families.
6. Return to general \\(c\\).

   Prove the finite determinantal stratification and relative-Grassmannian theorem, while keeping the general component-count assertion conjectural.

# 10. Final verdict

| Question                   | Assessment                                                                                                                                                                                                                                                                                                 |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Blocked lift            | There is a natural exact-sequence construction. Under the stated assumptions, completion modulo \\(C\\) is possible precisely when \\(q-\omega\le \operatorname{rank}[C;CA]-\operatorname{rank}C\\), provided the fixed top block is already independent modulo \\(C\\).                                   |
| 2. Good locus              | The compressed pencil descends through \\(K_0/V\\) for every admissible \\(V\\), not only for \\(t=2\\). The two-branch equations need a separate derivation and may describe a different problem.                                                                                                         |
| 3. General component bound | \\(p(c)n^c\\) currently bounds possible coarse Jordan-type labels, not irreducible components. General determinantal strata need not be irreducible.                                                                                                                                                       |
| 4. References              | Fabiano–Marino for polynomial inverse degree bounds; Harris, Bruns–Vetter, Hartshorne, and Weyman for determinantal geometry; Caldero–Reineke and Springer-fibre literature for quiver Grassmannians; Bochnak–Coste–Roy for real algebraic geometry; Schaefer–Cardinal–Miltzow for \\(\exists\mathbb R\\). |
| 5. Next step               | Continue with \\(c=2\\), but first solve the lift-completion problem. Do not move to \\(c=3\\) or general hardness prematurely.                                                                                                                                                                            |
| 6. Formalisation           | Formalise the general quotient-pencil block criterion. Do not formalise the two-branch equations until their equivalence is established.                                                                                                                                                                   |
| 7. Rank identity           | Retain the robust additive identity as the primary theorem; use the subtraction form only as a corollary under explicit dimension conditions.                                                                                                                                                              |

## My strongest recommendation

The immediate breakthrough to pursue is the exact sequence

\\[ 0\longrightarrow \frac{\operatorname{row}[C;CA]}{\operatorname{row}C} \longrightarrow \frac{\mathcal X^\*}{\operatorname{row}C} \longrightarrow K_0^\* \longrightarrow0. \\]

It explains exactly what the compressed representation forgets and exactly where the missing lifting freedom resides.

For \\(q=\omega+1\\), this freedom is especially simple: there is only one compressed row dependency to lift, and the additional independence condition reduces to making its lifted representative nonzero in the kernel of restriction.

If the proposition in Section 1.3 is incorporated successfully, the project may be able to close the \\(c=2\\) feasibility algorithm without solving the general type-control conjecture.

That is the direction I would pursue next.