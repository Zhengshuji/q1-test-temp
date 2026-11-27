Research assessment: from the hyperplane theorem to the type-control conjecture
Overall assessment
The report makes a significant conceptual advance: it identifies
\[
W=V\cap A^{-1}V,\qquad A(W)\subseteq V
\]

as the natural intermediate object and recognises that the geometry of \(V\) is controlled by the interaction between a subspace and its image under \(A\).

I agree with this direction. In particular, the passage from the hyperplane case to the Grassmannian problem
\[
V\longmapsto V+AV
\]

is the right general framework.

However, I would not yet state II.6 as a theorem. There are several mathematical gaps, one of which is a genuine error in the proposed fibre description. There is also a more fundamental problem with the proposed type: the Jordan type of \(A|_W\) is generally undefined, because \(A(W)\) need not be contained in \(W\).

These are not merely presentational issues. They affect the induction and the claimed component bound.

My main conclusions are:
1. II.1 remains sound, subject to the hypotheses and qualifications already discussed. The hyperplane vector-bundle theorem is a useful structural result.
2. II.2 is correct, and the invariant-eigenspace obstruction should be retained as a general preliminary test.
3. II.3 and II.4 contain useful geometric decompositions, but their completeness and some of their nonemptiness claims need further verification. The distinction between invariant and non-invariant \(W\) is essential, but it is not the only distinction needed.
4. II.6 has a correct starting point but an incomplete fibre condition. The condition \(A(V)\cap V=A(W)\) does not, by itself, guarantee that \(W=V\cap A^{-1}V\).
5. The proposed induction is not yet established. The varieties \(X_\tau\) are not automatically instances of the same problem at a smaller level.
6. For general \(c\), the natural algebraic language is that of matrix pencils and representations of the Kronecker quiver, but the Kronecker type of a restricted pair does not by itself classify the ambient Grassmannian incidence problem.
7. I would formalise the elementary linear-algebra lemmas first, then the hyperplane theorem and exact examples. I would postpone formalising the unproved \(c=2,c=3\) component classifications.
The most productive next step is to repair II.6 at the level of the exact incidence condition, then determine which data of \(W\) control the components of its base.

1. First correction: the exact fibre condition in II.6
This is the most important mathematical correction.

Let
\[
V\in\operatorname{Gr}(c,K_0),\qquad
W=V\cap A^{-1}V.
\]

By definition,
\[
W=\{v\in V:Av\in V\}.
\]

Put
\[
B=A(W).
\]

Then
\[
W+B\subseteq V.
\]

The report proposes to reconstruct \(V\), for a fixed \(W\), by requiring
\[
W+B\subseteq V,\qquad A(V)\cap V=B.
\tag{1.1}
\]

The second condition is necessary, but it is not sufficient.
1.1 Why equality of the image intersection is insufficient
Suppose \(v\in V\) satisfies
\[
Av\in B=A(W).
\]

Then there exists \(w\in W\) such that
\[
Av=Aw.
\]

It follows that
\[
A(v-w)=0.
\]

But this only gives
\[
v-w\in\ker A.
\]

It does not imply \(v=w\), unless \(A\) is injective on the relevant part of \(V\).

Thus it is possible to have
\[
A(V)\cap V=A(W)
\]

while
\[
V\cap A^{-1}V
\supsetneq W.
\]

The additional vectors are precisely the problem: they are vectors in \(V\) whose images lie in \(B\), but which are not already in \(W\).
1.2 The correct condition
The exact condition is
\[
\boxed{V\cap A^{-1}V=W.}
\tag{1.2}
\]

There is a convenient equivalent formulation. Consider the induced map
\[
\overline A_V:V\longrightarrow K/V,\qquad
v\longmapsto Av+V.
\]

Its kernel is exactly
\[
\ker\overline A_V=V\cap A^{-1}V.
\]

Since \(W\subseteq\ker\overline A_V\), the condition is
\[
\boxed{\rank\overline A_V=c-t.}
\tag{1.3}
\]

This is the cleanest formulation for the fibre.

It says that the induced map on the quotient
\[
V/W\longrightarrow K/V
\]

is injective.

This is equivalent to
\[
\ker\overline A_V=W.
\]

The important advantage is that (1.3) is a maximal-rank open condition on the Grassmannian of \(V\)'s containing \(W+B\).
1.3 Corrected fibre theorem
For fixed \(W\), define
\[
B=A(W),\qquad U=W+B.
\]

Necessarily,
\[
U\subseteq K_0
\]

and \(V\) must contain \(U\).

The ambient family of possible \(V\)'s is
\[
\operatorname{Gr}\bigl(c-\dim U,\ K_0/U\bigr).
\]

On this Grassmannian, impose
\[
\rank\bigl(\overline A_V:V\to K/V\bigr)=c-t.
\]

Consequently, the exact fibre is
\[
\boxed{
\mathcal F_W=
\left\{
V\in\operatorname{Gr}(c,K_0):
U\subseteq V,\ 
\rank(V\to K/V)=c-t
\right\}.
}
\tag{1.4}
\]

Here the map \(V\to K/V\) is induced by \(A\).

Thus the fibre is an open subset of the Grassmannian
\[
\operatorname{Gr}\bigl(c-\dim(W+A(W)),K_0/(W+A(W))\bigr).
\]

It may be empty, but if it is nonempty, it is irreducible.

This gives a corrected and stronger version of the geometric statement in II.6:
For fixed \(W\), the fibre of the map \(V\mapsto V\cap A^{-1}V\) is an open subset of a Grassmannian, defined by a maximal-rank condition.

The fibre is therefore not an arbitrary determinantal variety. Its geometry is relatively simple once \(W\) is fixed.

Important qualification: this does not yet imply that the total layer has one irreducible component for each component of the base. That conclusion requires analysing the variation of the fibre and, in particular, the image of the projection from the total incidence space to the base. I return to this below.

2. Second correction: the proposed type contains an undefined invariant
The report defines
\[
\tau(V)=
\bigl(t,r,s_0,\text{Jordan type of }A|_W\bigr),
\]

where
\[
W=V\cap A^{-1}V,\qquad
r=\rank(A|_W),\qquad
s_0=\dim(W\cap A(W)).
\]

The first three entries are well-defined. The last entry is not well-defined in general.

Indeed,
\[
A(W)\subseteq V
\]

but not necessarily
\[
A(W)\subseteq W.
\]

A Jordan type is defined for an endomorphism of a vector space. In the general case,
\[
A|_W:W\longrightarrow A(W)
\]

is a map between two spaces that need not be equal.
2.1 The right replacement
I would initially replace the proposed type by
\[
\boxed{
\tau_0(W)=
\bigl(
t,\ r,\ s_0,\ \dim(W\cap\ker A),\
\text{relative position of }W\text{ and }A(W)
\bigr).
}
\tag{2.1}
\]

The relative position can be encoded by the pair
\[
(W,B),\qquad B=A(W),
\]

together with the map
\[
A|_W:W\to B.
\]

The dimensions
\[
\dim W=t,\qquad
\dim B=r,\qquad
\dim(W\cap B)=s_0
\]

are the first coarse invariants, but they do not necessarily determine the isomorphism type of the pair.

The map \(A|_W\) has kernel
\[
W\cap\ker A
\]

and image \(B\). Its rank is \(r\). Once the domain and codomain are fixed, the map itself is equivalent under independent changes of basis to a standard rank-\(r\) matrix. But the embedding of \(W\) and \(B\) into the ambient \(K_0\), and their interaction with the ambient operator \(A\), contain additional information.

For this reason, the type should not be thought of as merely a Jordan partition.
2.2 When Jordan type is legitimate
There are two important special cases.

Case A: \(W=V\), so \(t=c\).

Then
\[
A(W)\subseteq V=W.
\]

Thus \(A|_W\) is an endomorphism, and its Jordan type is meaningful.

Case B: \(A(W)=W\).

Again \(A|_W\) is an endomorphism, and it is invertible.

These are precisely the invariant cases that appear in the \(c=2\) and \(c=3\) classifications.

For the non-invariant cases, Jordan type must be replaced by data for a map between distinct subspaces or by the associated matrix pencil.
2.3 A useful distinction
The report should distinguish:
- Invariant restriction: \(A(W)\subseteq W\), where Jordan type applies.
- Image-contained restriction: \(A(W)\subseteq V\), where \(A|_W:W\to B\subseteq V\) is a map into a larger space.
- General restriction: \(A|_W:W\to K\), where only the rank and kernel are intrinsically defined without additional ambient data.
The middle case is the one relevant to the general type-control construction.

3. Question 1: Is the type-control theorem the right general framework?
3.1 The basic reduction is excellent
The most useful identity in the report is
\[
W=V\cap A^{-1}V,\qquad B=A(W)\subseteq V.
\]

It separates the problem into two stages:
1. Choose the subspace \(W\) of vectors in \(V\) whose images remain in \(V\).
2. Extend \(W+B\) to a \(c\)-dimensional subspace \(V\), while ensuring that no additional vector enters \(V\cap A^{-1}V\).
This is a much better starting point than trying to classify \(V\) directly by its Jordan structure.

The corrected fibre description from Section 1 gives a useful formulation:
\[
\mathcal F_W
=
\left\{
V\in\operatorname{Gr}(c,K_0):
W+A(W)\subseteq V,\
\rank(V\to K/V)=c-\dim W
\right\}.
\tag{3.1}
\]

For each fixed \(W\), this is an open subset of a Grassmannian.

The remaining difficulty is therefore the geometry of the base of possible \(W\)'s.
3.2 A better base space: the pair of maps \((\iota,A_0)\)
Define
\[
D:=K_0\cap A^{-1}K_0
\]

and
\[
A_0:=A|_D:D\longrightarrow K_0.
\]

Let
\[
\iota:D\hookrightarrow K_0
\]

be the inclusion.

Every possible \(W\) satisfies
\[
W\subseteq D.
\]

The pair
\[
\boxed{(\iota,A_0):D\rightrightarrows K_0}
\tag{3.2}
\]

is the natural algebraic object.

Indeed, the image space
\[
U_W=W+A_0(W)
\]

is determined by the two arrows. The first coarse invariants are
\[
t=\dim W,\qquad
r=\dim A_0(W),\qquad
s_0=\dim(W\cap A_0(W)).
\]

They give
\[
\dim U_W=t+r-s_0.
\tag{3.3}
\]

This is the quantity controlling the dimension of the Grassmannian fibre.

The key improvement over the report's type is that \((\iota,A_0)\) is well-defined even when \(A(W)\not\subseteq W\).
3.3 The Kronecker pencil is the natural normal-form object
The pair of maps (3.2) defines the rectangular matrix pencil
\[
\boxed{
P(\lambda)=\lambda\iota-A_0:D\longrightarrow K_0.
}
\tag{3.4}
\]

This is a representation of the Kronecker quiver: two parallel arrows from the space \(D\) to the space \(K_0\).

Under independent changes of basis in \(D\) and \(K_0\), the pair of arrows is transformed by strict equivalence. The Kronecker canonical form classifies such pairs of maps. It records:
- finite elementary divisors;
- infinite elementary divisors;
- right minimal indices;
- left minimal indices.
The standard matrix-pencil theory is therefore directly relevant. In particular, Berger, Trunk and Winkler explain the relation between linear relations and the Kronecker canonical form, while Berger and Trenn develop the quasi-Kronecker form and its relation to descriptor systems and Wong sequences. 

科学直通车+2

There is a useful simplification here. Since \(\iota\) is injective, the pencil has full column normal rank: for generic \(\lambda\), the leading term \(\lambda\iota\) has full column rank. Consequently, there are no right minimal-index blocks. The relevant singular structure is on the left, together with the regular finite and infinite elementary divisors.

This is a more appropriate invariant than the Jordan type of \(A|_{K_0}\), which may not even be defined.
3.4 But the Kronecker form does not solve the Grassmannian problem by itself
There is an important limitation.

The Kronecker form classifies the ambient pair of arrows. It does not automatically classify the varieties of subspaces \(W\subseteq D\) with prescribed values of
\[
\dim W,\quad
\dim A_0(W),\quad
\dim(W\cap A_0(W)).
\]

Those are subspace-incidence conditions. Their geometry can be nontrivial even when the ambient representation has a known canonical form.

A natural formulation is through quiver Grassmannians.

For fixed dimensions \(t,u\), consider pairs of subspaces
\[
W\subseteq D,\qquad U\subseteq K_0,\qquad
\dim W=t,\quad\dim U=u,
\]

satisfying
\[
\iota(W)\subseteq U,\qquad A_0(W)\subseteq U.
\tag{3.5}
\]

These are subrepresentations of the Kronecker representation \((D,K_0;\iota,A_0)\). The additional condition
\[
U=W+A_0(W)
\tag{3.6}
\]

selects the minimal possible target space.

The resulting incidence variety is closely related to a quiver Grassmannian, with the exact-image condition imposing an additional rank stratum.

This suggests a good division of labour:
- Use the Kronecker form to describe the ambient pair.
- Use quiver Grassmannians or determinantal incidence varieties to describe its subspaces.
- Use the exact fibre condition (3.1) to reconstruct \(V\).
Caldero and Reineke's work on quiver Grassmannians is a useful entry point, although their paper's principal setting is acyclic quivers; the two-arrow Kronecker quiver itself is also a standard object in representation theory. 

documat.unirioja.es+1

3.5 What should replace \(\tau\)?
I would use a two-level type rather than one tuple.

First, define the coarse numerical type
\[
\boxed{
\tau_{\mathrm{num}}(W)
=
\bigl(t,r,s_0,\kappa\bigr),
\qquad
\kappa=\dim(W\cap\ker A).
}
\tag{3.7}
\]

This is sufficient to determine the dimensions of \(W+A(W)\), the kernel of \(A|_W\), and the dimension of the Grassmannian containing the fibre.

It is not sufficient to determine the irreducible component.

For the finer type, retain the isomorphism class of the restricted two-arrow representation
\[
\boxed{
\bigl(W,\ W+A(W);\ \iota|_W,\ A|_W\bigr).
}
\tag{3.8}
\]

Here the target is \(W+A(W)\), and the two maps are
\[
w\longmapsto w,\qquad w\longmapsto Aw.
\]

This is a well-defined finite-dimensional representation of the Kronecker quiver. Its Kronecker data are meaningful whether or not \(A(W)\subseteq W\).

However, I would not assume that the restricted Kronecker type alone controls the component. The embedding
\[
W+A(W)\subseteq K_0
\]

and the extension of \(A\) to the rest of \(K_0\) can affect the geometry of the possible extensions \(V\).

A good provisional definition is therefore
\[
\boxed{
\tau(W)=
\left(
\text{Kronecker type of }(\iota|_W,A|_W),\
\text{ambient incidence data in }K_0
\right).
}
\tag{3.9}
\]

The second entry needs to be made precise in a later theorem. It is not yet a finite list of numerical invariants.

Answer to Question 1: Yes, the type-control direction is right. But the correct framework is a Kronecker representation together with a Grassmannian incidence problem, not the Jordan type of \(A|_W\). The fibre is an open Grassmannian, and the central unresolved problem is the geometry of the base incidence strata.

4. Question 2: Are the \(c=2\) and \(c=3\) classifications correct and complete?
My assessment is that the proposed stratifications are useful, but neither classification should yet be described as complete. There are several missing cases and missing maximal-rank conditions.

The simplest way to audit both is to use the universal identity
\[
\boxed{
W=V\cap A^{-1}V
\iff
\rank\bigl(\overline A_V:V\to K/V\bigr)=c-\dim W.
}
\tag{4.1}
\]

This condition should be used in every subtype. It is more reliable than checking only whether one particular image vector lies outside \(V\).
4.1 First correction: invariant means \(A(W)\subseteq W\), not \(A(W)=W\)
The report repeatedly uses conditions such as
\[
AW=W,\qquad AL=L.
\]

These are too restrictive when \(A|_W\) is singular.

The correct definition of an invariant subspace is
\[
\boxed{A(W)\subseteq W.}
\tag{4.2}
\]

For a line \(L\), this includes both
\[
A(L)=L
\]

and
\[
A(L)=0.
\]

In particular, a line in \(\ker A\) is invariant. It must not be placed in the non-invariant subtype merely because \(A(L)\ne L\).

This correction affects the \(c=2,t=1\) and \(c=3,t=1\) classifications.
4.2 The \(c=2\) classification
Let
\[
V\in\operatorname{Gr}(2,K_0),\qquad
W=V\cap A^{-1}V.
\]

There are three possible values:
\[
t=\dim W\in\{0,1,2\}.
\]

Case \(t=2\): invariant two-planes
Here \(W=V\), so
\[
A(V)\subseteq V.
\]

Over \(\mathbb C\), the Jordan type of \(A|_V\) is meaningful. There are two possibilities:
1. Two distinct eigenvalues.
2. A single eigenvalue, with either scalar or nontrivial Jordan structure.
But the report's parameterisation of the first case as isolated points is incorrect in general.

For distinct eigenvalues \(\lambda\ne\mu\), the two-plane is
\[
V=L_\lambda\oplus L_\mu,
\]

where
\[
L_\lambda\in\mathbb P(E_\lambda\cap K_0),\qquad
L_\mu\in\mathbb P(E_\mu\cap K_0).
\]

Thus the parameter space is
\[
\boxed{
\mathbb P(E_\lambda\cap K_0)
\times
\mathbb P(E_\mu\cap K_0),
}
\tag{4.3}
\]

not necessarily a point.

It is a point only when both eigenspace intersections are one-dimensional.

For the scalar type at eigenvalue \(\lambda\),
\[
V\in\operatorname{Gr}(2,E_\lambda\cap K_0).
\tag{4.4}
\]

For a nontrivial Jordan block of size two, write
\[
T_\lambda=A-\lambda I.
\]

A chain plane has the form
\[
V=\operatorname{span}\{u,T_\lambda u\},
\]

with
\[
T_\lambda u\ne0,\qquad
T_\lambda^2u=0,\qquad
u,T_\lambda u\in K_0.
\tag{4.5}
\]

It is more accurate to parameterise these planes by Jordan chains than to assert a bundle with affine fibre dimension \(\dim E_\lambda\).

Indeed, for a fixed eigenline \(L\subseteq E_\lambda\cap K_0\), the choices of \(u\in K_0\) satisfying
\[
T_\lambda u\in L\setminus\{0\}
\]

must be considered modulo adding vectors in \(L\). When the condition is solvable, the corresponding affine freedom has dimension
\[
\dim(E_\lambda\cap K_0)-1,
\]

not \(\dim(E_\lambda\cap K_0)\).

There may also be restrictions on the eigenlines \(L\) for which a chain vector \(u\in K_0\) exists.

Thus the invariant \(t=2\) case is classifiable, but the bundle dimensions and base need correction.
Case \(t=1\): two genuinely different cases
Let
\[
W=L=\mathbb Cv.
\]

Subtype A: \(A(L)\subseteq L\).

This includes \(Av=0\), as well as \(Av=\lambda v\) with \(\lambda\ne0\).

Choose a second line in \(K_0/L\) to form \(V\). The exact condition is that
\[
\overline A_V:V/L\longrightarrow K_0/V
\]

be injective.

Since \(V/L\) is one-dimensional, this is equivalent to saying that a representative \(x\in V\setminus L\) satisfies
\[
Ax\notin V.
\tag{4.6}
\]

Thus the family is an open subset of the projective bundle of lines in \(K_0/L\).

Subtype B: \(A(L)\not\subseteq L\).

Now \(Av\) is independent of \(v\), and because \(Av\in V\),
\[
V=\operatorname{span}\{v,Av\}.
\]

The exact condition is
\[
A^2v\notin\operatorname{span}\{v,Av\}.
\tag{4.7}
\]

Equivalently,
\[
\boxed{
\rank[v,Av,A^2v]=3.
}
\tag{4.8}
\]

The report's nonemptiness condition
\[
D\ne0,\qquad A|_D\text{ not scalar}
\]

is not sufficient.

For example, take a nilpotent Jordan block of size two on \(D=\operatorname{span}\{e_1,e_2\}\):
\[
Ae_1=0,\qquad Ae_2=e_1.
\]

The restriction is not scalar, but
\[
A^2v=0
\]

for every \(v\in D\). No line in the non-invariant subtype satisfies (4.7).

The correct nonemptiness criterion is the existence of
\[
v\in D=K_0\cap A^{-1}K_0
\]

such that
\[
\boxed{
\rank[v,Av,A^2v]=3.
}
\tag{4.9}
\]

This is a concrete, exact test.
Case \(t=0\): the open stratum
Here
\[
V\cap A^{-1}V=0.
\]

Equivalently,
\[
\overline A_V:V\to K_0/V
\]

is injective, so it has rank two.

This is an open condition on \(\operatorname{Gr}(2,K_0)\).

It may be empty, depending on \(A\) and \(K_0\).
4.3 The \(c=3\) classification
The same maximal-rank criterion is even more important here.

For \(t=2\), the map
\[
\overline A_V:V/W\to K_0/V
\]

must have rank one.

Put
\[
B=A(W),\qquad U=W+B.
\]

There are two possible dimensions for \(U\) if the fibre is nonempty:
\[
\dim U=2\quad\text{or}\quad 3.
\]

Case \(\dim U=3\).

Then
\[
V=U=W+B
\]

is determined. But it is admissible only if
\[
\rank(\overline A_V)=1.
\]

For example, if \(B\) is a line outside \(W\), choose \(b\) spanning \(B\). Since \(A(W)\subseteq B\), the condition reduces to
\[
Ab\notin V.
\tag{4.10}
\]

The report's description of the unique plane \(V=W+A(W)\) omits this essential condition.

Case \(\dim U=2\).

Here \(B\subseteq W\), so
\[
A(W)\subseteq W.
\]

This includes singular invariant two-planes. Choose a line in \(K_0/W\) to obtain \(V\). The exact condition is that the induced map
\[
V/W\to K_0/V
\]

be injective, or equivalently that a generator \(w\) of the added line satisfy
\[
Aw\notin V.
\tag{4.11}
\]

This is an open condition in the projective space of possible extensions.

Thus the natural division is by
\[
A(W)\subseteq W
\quad\text{versus}\quad
A(W)\not\subseteq W,
\]

not by equality \(A(W)=W\).

For \(t=1\), let \(W=L=\mathbb Cv\).

Subtype A: \(A(L)\subseteq L\).

The quotient operator
\[
\bar A:K_0/L\longrightarrow K_0/L
\]

is well-defined.

The quotient plane \(U=V/L\) must satisfy
\[
\boxed{
U\cap\bar A^{-1}U=0.
}
\tag{4.12}
\]

Equivalently, the map
\[
\bar A_U:U\to(K_0/L)/U
\]

must have rank two.

The report's condition that \(U\) contain no \(\bar A\)-invariant line is too weak.

A two-plane can contain a nonzero vector \(u\) with \(\bar A u\in U\), without containing an invariant line. Such a vector would enlarge \(W\), so it must be excluded.

Subtype B: \(A(L)\not\subseteq L\).

Then
\[
U=W+A(W)=L+A(L)
\]

is two-dimensional, and \(V\) is obtained by adjoining a third line.

The condition
\[
A^2v\notin V
\]

is necessary, but not sufficient.

If \(w\) represents the added line, the induced map on \(V/L\) must have rank two. Thus
\[
\boxed{
A^2v+V,\quad Aw+V
\text{ must be linearly independent in }K_0/V.
}
\tag{4.13}
\]

This is the correct condition. It simultaneously excludes both the possibility that \(A^2v\in V\) and the possibility that the image of \(w\) is dependent on the image of \(Av\).

For \(t=0\), the exact condition is
\[
\boxed{
\dim(V\cap A^{-1}V)=0,
}
\tag{4.14}
\]

or equivalently
\[
\rank(\overline A_V)=3.
\]

4.4 The \(c=3\) invariant three-plane case
For \(t=3\), \(V\) is an invariant three-dimensional subspace:
\[
A(V)\subseteq V.
\]

The Jordan types \(1+1+1\), \(2+1\), and \(3\) are the possible Jordan block-size patterns for a single eigenvalue. But one must also allow decompositions involving distinct eigenvalues, such as
\[
1_\lambda+1_\mu+1_\nu,\qquad
2_\lambda+1_\mu,\qquad
1_\lambda+2_\lambda,
\]

where the subscripts distinguish eigenvalues and the notation is interpreted accordingly.

A complete classification should therefore be indexed by the elementary divisors of the restriction, not just by the partition of three.

Moreover, the parameter spaces of such invariant subspaces need not be points or single affine bundles. They are varieties of submodules of the \(\mathbb C[x]\)-module defined by \(A\).
4.5 Overall verdict on Questions 2 and 4
The two-subtype insight is valuable, but the classification needs a systematic rewrite.

I recommend replacing the case-by-case prose with a single rule:
For each proposed \(W\), first compute \(U=W+A(W)\). Then parameterise \(V\supseteq U\) by a Grassmannian. Finally impose the open maximal-rank condition \(\rank(V\to K_0/V)=c-t\).

This rule automatically handles singular restrictions, non-invariant images, and the position of \(A(A(W))\). The \(c=2\) and \(c=3\) lists then become explicit expansions of the same theorem.

5. Question 3: Which propositions should be formalised in Lean first?
Your proposed order is reasonable, but I would slightly change it.

The aim should be to build a small, reusable formal linear-algebra library for the project before attempting algebraic-geometric results.
5.1 Recommended formalisation order
Priority	Proposition	Reason
1	Rank inequality from a large subspace of the kernel	Foundational; short; reusable
2	Exact lifting rank formula	Directly supports the synthesis problem
3	Explicit \(4\times4\) counterexample	Concrete end-to-end verification
4	Block spectral criterion	Central reduction from pencil rank to an eigenvector condition
5	Hyperplane identities involving \(Z_1,Z_2\)	Connects the abstract geometry to the actual matrices
6	Polynomial certificate equivalence	Supports the finite algebraic encoding
7	\(c=2\) exact subspace lemmas	Only after the corrected classification is stable

I would not formalise the full \(c=2\) or \(c=3\) component classification yet.
5.2 The kernel-rank inequality
The statement is:

Let \(f:K\to Y\) be linear and \(U\subseteq\ker f\). Then
\[
\rank f
\leq \dim K-\dim U.
\]

Hence, if
\[
\dim U>\dim K-\omega,
\]

then
\[
\rank f<\omega.
\]

This is an excellent first Lean theorem.

It is independent of the observer-specific construction and will be reusable in several later proofs.

The axioms you list,
\[
\texttt{propext},\quad\texttt{Classical.choice},\quad\texttt{Quot.sound},
\]

are standard Lean axioms. Their presence is not, by itself, a concern. The relevant issue is whether any additional project-specific axioms or sorry placeholders occur in the dependency chain.

I would verify the complete dependency closure, not just the standalone theorem.
5.3 The lifting rank formula should be second
Suppose \(L_0\) has full row rank \(r\), and let
\[
\pi:\mathbb C^n\to\mathbb C^n/\operatorname{row}L_0.
\]

Then
\[
\boxed{
\rank\begin{bmatrix}L_0\\R\end{bmatrix}
=
r+\rank(\pi R).
}
\tag{5.1}
\]

This is a very clean theorem and central to the actual problem.

It should be formalised early because it separates the full-row-rank condition into an ordinary quotient-space rank condition.

The affine lifting corollary is also useful:

For an affine family \(R(t)\), a full-row-rank lift exists precisely when the induced quotient matrix \(\pi R(t)\) has full row rank for at least one parameter value.

This can be expressed using the nonvanishing of at least one maximal minor.
5.4 The explicit counterexample is a good third target
The counterexample is valuable because it verifies a genuinely nontrivial mathematical phenomenon in a completely concrete setting.

I would formalise:
1. The exact matrix \(A\).
2. The exact subspace \(V\).
3. The computation of \(A(V)\).
4. The computation of \(V\cap A^{-1}V\).
5. The absence of an invariant line in \(V\).
The final item should be proved directly by solving the eigenvector equations, rather than relying on a numerical computation.

This gives a robust example that can be cited in the paper and used as a regression test for later formalisation.
5.5 The block criterion is more important than the \(c=2\) classification
The spectral criterion
\[
\text{bad}
\iff
\exists\,0\ne y\in\ker B_\perp,\quad
A_Wy\in\mathbb Cy
\]

is central to the conceptual reduction.

It is also comparatively elementary.

I would formalise it before the \(c=2\) classification.

In Lean, it is useful to express it in terms of:
- the induced map on the image of \(H\);
- the decomposition of the codomain into \(W\oplus W'\);
- nonzero vectors in the kernel of the complementary block;
- eigenvector membership for the \(W\)-block.
This will make later spectral arguments much easier to reuse.
5.6 Do not formalise the M2 geometry prematurely
The M2 work is useful evidence and a valuable discovery tool, but it does not replace proof of:
- local triviality of the relevant vector bundles;
- irreducibility of the total incidence;
- nonemptiness of the open fibres;
- component correspondence under projection.
Lean formalisation of these results is likely to be expensive. It should follow a stable mathematical theorem, not be used to determine what the theorem ought to say.

Answer to Question 3: Your first kernel theorem is a good first target. I would put the lifting rank formula second, the explicit counterexample third, and the block criterion fourth. I would postpone the component classification formalisation.

6. Question 4: Is the proposed paper plan sound?
The overall plan is sensible, but I would change the order and the status of II.6.
6.1 Do not state II.6 as a theorem yet
The type-control theorem currently has three unproved steps:
1. A valid type invariant for non-invariant \(W\).
2. A correct fibre reconstruction condition.
3. A proof that the base strata are controlled recursively by smaller-dimensional instances.
The first two can be repaired as above. The third remains open.

In particular, the assertion
\[
N(c)\leq\sum_\tau N(t(\tau))
\tag{6.1}
\]

does not follow merely from the fact that the fibres are Grassmannian bundles.

To justify it, one must prove that:
- the base is partitioned into finitely many locally closed strata;
- the relevant fibre construction is algebraic over each stratum;
- the total space over each irreducible base component has the asserted component behaviour;
- the number of irreducible components of the base strata admits the claimed bound.
The recursion itself also needs a precise definition. The variety
\[
X_\tau=
\{W\in\operatorname{Gr}(t,K_0):A(W)\subseteq K_0,\ \ldots\}
\]

is not automatically the same problem at level \(t\). It is a subspace-incidence problem for the pair \((\iota,A_0)\), and its component structure needs to be established independently.

I would therefore label II.6:
Conjectural framework
Type-control conjecture. For fixed codimension \(c\), the incidence variety of pairs
\[
(W,V),\qquad
W=V\cap A^{-1}V,\qquad
\dim V=c,
\]

admits a finite stratification by locally closed varieties whose geometry is controlled by a finite set of Kronecker-type invariants of the restricted pair \((\iota|_W,A|_W)\) and its ambient embedding.

This is a defensible conjectural formulation. It does not yet assert a uniform component bound.
6.2 Suggested revised paper structure
I recommend the following order.

Section 1. Exact observer reduction
- Definition of \(K\).
- Restriction of (5a) to \(K\).
- The induced map on \(W=\operatorname{im}H\).
- The exact spectral eigenvector criterion.
Section 2. Block criterion and polynomial certificates
- The \(W\oplus W'\) block decomposition.
- The bad-eigenvector condition.
- The bounded-degree polynomial generalized-inverse certificate.
Section 3. Full-row-rank lifting
- Quotient-space lifting formula.
- Affine lift families.
- Exact full-row-rank existence criterion.
Section 4. Hyperplane theorem
- Projective parametrisation.
- Eigenvector base decomposition.
- Vector-bundle structure.
- Component bound \(\delta+1\).
- Generic determinant-divisor test.
Section 5. General Grassmannian formulation
- \(V\in\operatorname{Gr}(c,K_0)\).
- \(W=V\cap A^{-1}V\).
- \(B=A(W)\).
- The exact open fibre condition.
- The pair-of-arrows formulation.
This section is the natural transition from the hyperplane theorem to the general conjecture.

Section 6. Low-codimension classifications
- Corrected \(c=2\) classification.
- Corrected \(c=3\) classification.
- Explicit nonemptiness tests.
- Exact rank conditions.
Section 7. Exact examples and formal verification
- All exact matrices.
- Exact ranks.
- Exact gcds.
- Explicit lifts.
- Lean-verified elementary lemmas.
Section 8. Type-control conjecture and open problems
- Kronecker representation.
- Quiver Grassmannian incidence.
- Component bounds.
- Complexity.
- Real-field extension.
This is preferable to putting the \(c=2\) and \(c=3\) classifications before the general fibre theorem. The general fibre theorem explains the logic behind the low-dimensional cases.

7. Question 5: Is there a known classification of the pairs \((W,A(W))\)?
Yes, but there are two different levels of classification, and they should not be confused.
7.1 The pair of maps is classified by Kronecker canonical form
For
\[
\iota_W:W\to W+A(W),\qquad
A_W:W\to W+A(W),
\]

we have a pair of maps with the same domain and codomain.

The associated pencil is
\[
\lambda\iota_W-A_W.
\]

Its Kronecker canonical form is the appropriate normal form under independent changes of basis in the domain and codomain.

It includes both regular and singular structure. For rectangular pencils, one must retain left and right minimal indices as well as finite and infinite elementary divisors. Omitting the minimal indices would lose information about the pair. 

Springer+2

For the restricted pair, \(\iota_W\) is injective. Thus the pencil has full column normal rank and no right minimal-index blocks.

This is a useful simplification.
7.2 The ambient pair is more useful than the restricted pair
For the entire problem, I would start with
\[
\iota:D\hookrightarrow K_0,\qquad A_0:D\to K_0,
\]

and its pencil
\[
\lambda\iota-A_0.
\]

This captures all possible \(W\subseteq D\) simultaneously.

The restricted pair is then obtained by restricting both arrows to \(W\), with codomain reduced to \(W+A(W)\).

This is preferable to independently classifying each \(A|_W\), because it preserves the relation between the different candidate subspaces.
7.3 Linear relations and descriptor systems
The language of linear relations is relevant because a pair of maps or a rectangular pencil can encode a partially defined, multivalued, or constrained linear operator.

Berger, Trunk and Winkler give a direct connection between linear relations and Kronecker canonical form. Their interpretation is particularly appropriate when the ordinary Jordan form is unavailable. 

科学直通车

Descriptor-system theory is also relevant. The pencil
\[
\lambda\iota-A_0
\]

has the same structural features that appear in differential-algebraic equations:
- finite eigenvalues;
- infinite eigenvalues;
- singular chains;
- minimal indices.
Berger and Trenn's quasi-Kronecker form uses Wong sequences to separate underdetermined, regular and overdetermined parts of a pencil, and is useful for understanding its solution structure. 

应用数学学会+1

7.4 Suggested references
I would begin with the following.
Reference	Relevance
Berger, Trunk and Winkler, “Linear relations and the Kronecker canonical form,” Linear Algebra and its Applications 488 (2016), 13–44.	Direct connection between linear relations and Kronecker form.  科学直通车
Berger and Trenn, “The quasi-Kronecker form for matrix pencils,” SIAM Journal on Matrix Analysis and Applications 33 (2012), 336–368.	Wong sequences, descriptor systems, and singular pencil structure.  格罗宁根大学研究门户
Caldero and Reineke, “On the quiver Grassmannian in the acyclic case,” Journal of Pure and Applied Algebra 212 (2008), 2369–2380.	Geometry of subrepresentations and quiver Grassmannians.  Documat
Gantmacher, The Theory of Matrices, Vol. II, Chapter XII.	Classical Kronecker theory for matrix pencils.  School of Mathematics

The important warning is that Kronecker canonical form classifies the ambient pair of maps, not automatically every quiver Grassmannian or every component of the subspace incidence variety.

8. Question 6: Does the type-control route change the complexity picture?
It changes the mathematical structure of the problem, but it does not yet establish a new complexity classification.

I would distinguish three issues.
8.1 The fixed-codimension problem may be more tractable
For fixed \(c\), the variable \(V\) belongs to
\[
\operatorname{Gr}(c,K_0).
\]

Its dimension is
\[
c(\dim K_0-c),
\]

which grows linearly with \(\dim K_0\) for fixed \(c\).

The incidence conditions involve only the restriction of \(A\) to subspaces of dimension at most \(c\).

This makes a fixed-\(c\) algorithm plausible.

The corrected fibre theorem is encouraging: once \(W\) is fixed, the possible \(V\)'s are an open subset of a Grassmannian, not an arbitrary high-degree variety.

The remaining challenge is the base variety of \(W\)'s.
8.2 The Kronecker form does not automatically give a polynomial algorithm
The canonical form of the ambient pencil can be computed, but the component geometry of the relevant subspace varieties may still be complicated.

A polynomial-time algorithm would need to do more than compute the Kronecker invariants. It would need to:
1. Enumerate the relevant base strata.
2. Determine which are nonempty.
3. Determine which have real points when working over \(\mathbb R\).
4. Test the generic spectral determinant divisor on each relevant component.
5. Construct an actual \(R\) when a good component exists.
The Kronecker form is a structural tool, not an automatic solution of all five tasks.
8.3 The claimed independence from \(k\) needs qualification
The report states that \(N(c)\) depends only on \(c\) and the Jordan type of \(A|_{K_0}\), not on \(k\).

There are two problems:
- \(A|_{K_0}\) need not be an endomorphism of \(K_0\), so its Jordan type may not exist.
- Even after replacing it with the Kronecker type of \((\iota,A_0)\), that Kronecker data includes dimensions and block multiplicities. Those data can grow with \(k\).
Thus the statement is not yet a dimension-independent component bound.

A more realistic conjecture would be:
For fixed \(c\), the number and complexity of the relevant incidence strata admit bounds in terms of \(c\) and suitable structural invariants of the pencil \(\lambda\iota-A_0\).

Whether such bounds can be made polynomial in the input size is a separate question.
8.4 Could there still be hardness?
Yes. The type-control route does not rule it out.

There are two plausible possibilities:
- The special one-operator structure makes fixed-\(c\) incidence varieties sufficiently simple to admit polynomial algorithms.
- The geometry of the subspace strata retains enough complexity to encode difficult algebraic feasibility problems, even at small fixed codimension.
At present, neither conclusion is justified.

I would not attempt a hardness reduction until the \(c=2\) and \(c=3\) strata have been classified correctly and the general Kronecker formulation has been made precise.

Answer to Question 6: A polynomial algorithm for fixed \(c\) is plausible, but not proved. The type-control route gives a more structured attack on the problem; it does not settle complexity or exclude hardness.

9. Question 7: What should be done next?
I would not begin with the full per-type classification of \(X_\tau\). The current type is not yet correct, and a large classification built on it would risk another round of retractions.

I recommend the following sequence.
Step 1 — Repair the general fibre theorem
Write and prove the following exact proposition:
Exact Grassmannian fibre proposition

Let \(W\subseteq D=K_0\cap A^{-1}K_0\) have dimension \(t\), and put
\[
U=W+A(W).
\]

The fibre over \(W\) of the map
\[
V\longmapsto V\cap A^{-1}V
\]

is
\[
\left\{
V\in\operatorname{Gr}(c,K_0):
U\subseteq V,\ 
\rank(V\to K_0/V)=c-t
\right\}.
\]

It is an open subset of
\[
\operatorname{Gr}(c-\dim U,K_0/U).
\]


This is the correct foundation for the general theory.
Step 2 — Rewrite the \(c=2\) classification using the exact fibre condition
For each of \(t=0,1,2\):
- determine the possible \(W\);
- determine \(U=W+A(W)\);
- describe the Grassmannian fibre;
- impose the exact rank condition;
- give exact nonemptiness criteria.
In particular, replace the false condition
\[
D\ne0,\quad A|_D\text{ not scalar}
\]

by the cyclic-vector condition
\[
\exists v\in D:\rank[v,Av,A^2v]=3.
\]

Also correct the two-distinct-eigenvalue parameter space and the Jordan-chain fibre dimension.

This is the most useful next mathematical task because it is small enough to finish and will reveal exactly what the general type should record.
Step 3 — Rewrite the \(c=3\) classification
Use the same procedure. In particular:
- replace “no invariant line” by the exact injectivity condition;
- require rank two for the induced map in the non-invariant \(t=1\) case;
- impose the missing condition \(A(A(W))\not\subseteq V\) in the relevant \(t=2\) case;
- include singular invariant lines and singular invariant planes.
This should be done before claiming a complete \(c=3\) algorithm.
Step 4 — Introduce the Kronecker representation formally
Define
\[
D=K_0\cap A^{-1}K_0,\qquad
\iota:D\hookrightarrow K_0,\qquad
A_0=A|_D.
\]

Then state the general incidence variety as a variety of subrepresentations of
\[
(D,K_0;\iota,A_0)
\]

with the additional maximality condition
\[
W=V\cap A^{-1}V.
\]

This is the correct bridge to representation theory.
Step 5 — Prove the type-control statement only after the base is understood
The right question is no longer simply whether there are finitely many Jordan types.

It is:
Can the subspace-incidence variety associated with \((\iota,A_0)\), for fixed \(c\), be stratified into a controlled number of irreducible locally closed pieces, with each fibre an open Grassmannian?

If yes, then a component bound may follow.

This is the genuinely important theorem to seek.
Step 6 — Continue Lean formalisation in parallel
The recommended order is:
1. Kernel-rank inequality.
2. Quotient lifting rank formula.
3. Exact counterexample.
4. Block spectral criterion.
5. Hyperplane rank identities.
6. Polynomial certificate.
Do not let formalisation of the unproved component theorem delay the mathematical work.
Step 7 — Start the paper now, but present the general theorem as a conjecture
The hyperplane theorem and exact spectral reduction are already a coherent paper core.

You do not need a complete classification for every \(c\) to write a strong paper.

I would write the main paper around the exact reduction, hyperplane theorem, lifting theorem, and generic determinant-divisor criterion. Then present \(c=2,c=3\) as low-codimension extensions, with the general type-control framework clearly labelled as a conjectural direction.

10. Consolidated status of the report
Result	Assessment	Recommended status
II.1 Hyperplane vector-bundle theorem	Structurally sound under the stated hypotheses	Theorem, after full proof
II.1 Bound \(\delta+1\)	Plausible and supported by the eigenvector decomposition	Theorem, after proving the incidence-stratum argument
II.2 Eigenspace obstruction	Correct	Theorem
II.3 \(c=2,t=2\)	Correct general direction; parameter spaces need refinement	Partial classification
II.3 \(c=2,t=1\)	Two-subtype idea correct; invariant zero-image lines omitted; nonemptiness criterion false	Revise
II.3 \(c=2,t=0\)	Correct open maximal-rank condition	Theorem
II.4 \(c=3,t=2\)	Correct dimension-layer idea; missing exact rank test in some subtypes	Revise
II.4 \(c=3,t=1\)	Current condition too weak; missing rank-two condition	Revise
II.4 \(c=3,t=0\)	Correct open maximal-rank formulation	Theorem
II.5 Counterexample	Valuable and correct in principle	Exact example
II.6 Type-control theorem	Correct conceptual direction, but induction and type definition are incomplete	Conjecture
II.7 Lean plan	Good, with minor priority adjustment	Proceed


11. Final answers to the seven questions
Question	Conclusion
Q1. Is type-control the right framework?	Yes, but use the Kronecker representation \((\iota,A_0)\), not Jordan type of \(A|_W\).
Q2. Are \(c=2,c=3\) classifications complete?	Not yet. The invariant-line distinction, cyclic-vector criterion, and maximal-rank fibre conditions need correction.
Q3. What should be formalised first?	Kernel-rank inequality, lifting formula, exact counterexample, block criterion, then polynomial certificates.
Q4. Should II.6 be a theorem?	No. Present it as a conjectural framework until the base-stratum induction is proved.
Q5. Which normal form is appropriate?	Kronecker canonical form of the rectangular pencil \(\lambda\iota-A_0\), together with quiver-Grassmannian incidence.
Q6. Does this settle complexity?	No. It makes fixed-\(c\) tractability plausible, but neither a polynomial algorithm nor hardness has been established.
Q7. What next?	Prove the exact fibre theorem, complete \(c=2\), repair \(c=3\), formulate the Kronecker incidence, then write the paper.

Final judgement
The report has identified a genuinely promising general structure. The central object is not the restriction \(A|_W\) considered as though it were always an endomorphism. It is the pair
\[
\boxed{
W\overset{\iota}{\longrightarrow}W+A(W),
\qquad
W\overset{A}{\longrightarrow}W+A(W),
}
\]

together with its embedding in \(K_0\).

The central fibre condition is not merely
\[
A(V)\cap V=A(W),
\]

but the exact equality
\[
\boxed{V\cap A^{-1}V=W,}
\]

equivalently
\[
\boxed{\rank(V\to K_0/V)=c-\dim W.}
\]

This is the correction on which I would rebuild the general theory.

The resulting research programme has a coherent hierarchy:
- Hyperplane case: eigenvectors and vector bundles.
- Codimension two and three: explicit Grassmannian strata and exact rank conditions.
- General codimension: Kronecker representations and quiver-Grassmannian incidence.
- Spectral feasibility: generic determinant divisors on irreducible components.
- Complexity: determine whether the fixed-codimension incidence structure admits efficient exact algorithms.
My strongest recommendation is to prove the exact fibre theorem and rewrite the \(c=2\) classification before expanding the type-control conjecture. The \(c=2\) case is the right test of whether the proposed representation-theoretic invariant is sufficiently strong. If it works there, the \(c=3\) case will provide a serious test of the induction. If it fails, the failure will identify precisely which additional ambient data the type must retain.

That is a more reliable route than attempting to prove the general type-control theorem in its current form.