# A comprehensive mathematical audit of the MIN-ROWS / q1 project

## 1. Overall assessment

The project has developed into a substantial investigation of the algebraic geometry, polynomial-matrix structure, and computational complexity of minimal-order functional observer feasibility.

My assessment is positive, but I would make an important distinction between three levels of achievement:

1. Established algebraic structure: reductions, kernel identities, pencil factorizations, polynomial certificates, and exact fibre descriptions.
2. Established geometric structure under stated hypotheses: finite stratifications, relative Grassmannian descriptions, and low-codimension classifications.
3. Unresolved feasibility theory: whether the compressed geometric configurations admit compatible lifts satisfying the original independence and spectral requirements.

The third level is the decisive obstacle.

The main risk is not that the individual algebraic reductions are fundamentally incorrect. It is that a result proved for the compressed variables may be presented as a result for the original observer variables without a sufficiently strong lifting theorem.

There is also an opportunity to improve the complexity argument: the bounded-degree polynomial generalized-inverse certificate can be applied directly to the original pencil, avoiding the need to construct a basis of \\(K_0\\) for the purpose of proving existential-real membership.

I recommend making the following changes to the research strategy:

- Establish an exact affine lifting theorem, including the fixed \\(L_0\\) rows.
- Separate the geometry of compressed subspaces from the geometry of actual observer matrices.
- Complete the \\(c=2\\) classification and its irreducibility proof before making a component-bound claim.
- Establish the \\(\exists\mathbb R\\) upper bound using a fully specified rational-input model.
- Treat \\(c=3\\) as an independent geometric investigation.
- Do not claim NP-hardness or a general component bound without a new proof.

I will examine the mathematical foundations in detail.

# Part I. The original problem and its logical structure

## 2. First establish the exact problem being studied

We are given

\\[ A\in\mathbb C^{n\times n},\qquad C\in\mathbb C^{p\times n},\qquad L_0\in\mathbb C^{r\times n}. \\]

We seek

\\[ L=\begin{bmatrix}L_0\\\R\end{bmatrix} \in\mathbb C^{q\times n}, \qquad q\ge r, \\]

with full row rank, satisfying

\\[ \tag{5a} \operatorname{rank} \begin{bmatrix} LA\\\L\\\CA\\\C \end{bmatrix} = \operatorname{rank} \begin{bmatrix} L\\\CA\\\C \end{bmatrix}, \\]

and

\\[ \tag{5b} \operatorname{rank} \begin{bmatrix} \lambda L-LA\\\CA\\\C \end{bmatrix} = \operatorname{rank} \begin{bmatrix} L\\\CA\\\C \end{bmatrix} \quad\forall\lambda\in\mathbb C. \\]

There is an important preliminary issue.

The report sometimes uses the condition

\\[ \operatorname{rank}[C;L]=p+q. \\]

This is stronger than merely requiring \\(L\\) to have full row rank.

In fact,

\\[ \operatorname{rank}[C;L]=p+q \\]

requires both

\\[ \operatorname{rank}C=p \\]

and

\\[ \operatorname{row}C\cap\operatorname{row}L=\\{0\\}. \\]

These assumptions should be stated explicitly whenever this stronger independence condition is used.

If \\(C\\) is not full row rank, the expression \\(p+q\\) is not the correct target rank.

A more general formulation is

\\[ \operatorname{rank}[C;L] = \operatorname{rank}C+q, \\]

assuming \\(L\\) itself has \\(q\\) independent rows.

Likewise, the fixed-row condition

\\[ \operatorname{rank}[C;L_0] = \operatorname{rank}C+r \\]

should be distinguished from the weaker condition that \\(L_0\\) has full row rank.

These distinctions are not cosmetic. They affect the lifting theorem, the admissible range of \\(q\\), and the complexity formulation.

### Recommendation 2.1

Use the following notation throughout the paper:

\\[ s_C=\operatorname{rank}C, \\]

and state whether the standing assumptions are

\\[ \operatorname{rank}L_0=r, \qquad \operatorname{rank}[C;L_0]=s_C+r. \\]

If the original observer problem requires full independence from \\(C\\), impose these assumptions at the outset.

Under this stronger requirement,

\\[ q\le n-s_C. \\]

Without it, the only universal upper bound from full row rank of \\(L\\) is

\\[ q\le n. \\]

## 3. The first compression is mathematically sound

Let

\\[ K_0=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \qquad k=\dim K_0, \\]

and let

\\[ N\in\mathbb C^{n\times k} \\]

have columns forming a basis of \\(K_0\\).

Define

\\[ H=LN,\qquad H_A=LAN. \\]

The key observation is that restricting a row space to \\(K_0\\) eliminates the rows of \\(C\\) and \\(CA\\).

Indeed, for any row matrix \\(X\\),

\\[ \operatorname{rank} \begin{bmatrix} X\\\CA\\\C \end{bmatrix} = \operatorname{rank} \begin{bmatrix} CA\\\C \end{bmatrix} + \operatorname{rank}(XN). \\]

This identity follows because the kernel of the restriction map

\\[ \mathbb C^{1\times n} \longrightarrow \mathbb C^{1\times k}, \qquad x\longmapsto xN \\]

is exactly

\\[ \operatorname{row}[C;CA]. \\]

Consequently,

\\[ \boxed{(5a)\iff\ker H\subseteq\ker H_A.} \\]

Similarly, if

\\[ \omega=\operatorname{rank}H, \\]

then (5b) becomes

\\[ \boxed{ \operatorname{rank}(\lambda H-H_A)=\omega \quad\forall\lambda\in\mathbb C. } \\]

This is an exact reduction, not merely a necessary condition.

It is one of the strongest foundations of the project.

### 3.1 A useful dimension identity

Let

\\[ V=\ker H. \\]

Then

\\[ \dim V=k-\omega. \\]

Writing

\\[ c=k-\omega, \\]

we have

\\[ \dim V=c. \\]

The kernel inclusion implies

\\[ V\subseteq\ker H_A. \\]

Thus the pencil

\\[ P(\lambda)=\lambda H-H_A \\]

annihilates \\(V\\) for every \\(\lambda\\).

Therefore it descends to a map

\\[ \overline P(\lambda): K_0/V\longrightarrow\mathbb C^q. \\]

Since

\\[ \dim(K_0/V)=\omega, \\]

the descended pencil has at most \\(\omega\\) columns and the required rank is \\(\omega\\).

This is the correct geometric interpretation of the compression.

# Part II. The operator-theoretic reduction

## 4. The universal block criterion is correct

Since

\\[ \ker H\subseteq\ker H_A, \\]

there exists a unique linear map

\\[ Z:\operatorname{im}H\longrightarrow\mathbb C^q \\]

satisfying

\\[ H_A=ZH. \\]

Let

\\[ W=\operatorname{im}H. \\]

Then

\\[ \dim W=\omega. \\]

Choose a complementary subspace

\\[ \mathbb C^q=W\oplus W'. \\]

Relative to this decomposition,

\\[ Z= \begin{bmatrix} A\_\*\\\B\_\* \end{bmatrix}, \\]

where

\\[ A\_\*:W\to W, \qquad B\_\*:W\to W'. \\]

We obtain

\\[ P(\lambda) = (\lambda I-Z)H = \begin{bmatrix} \lambda I-A\_\*\\\ -B\_\* \end{bmatrix}H. \\]

Since \\(H\\) maps onto \\(W\\),

\\[ \operatorname{rank}P(\lambda)<\omega \\]

if and only if there exists \\(0\ne y\in W\\) such that

\\[ (\lambda I-A\_\*)y=0, \qquad B\_\*y=0. \\]

Hence

\\[ \boxed{ \operatorname{rank}P(\lambda)<\omega \iff \exists\\,0\ne y\in\ker B\_\*: A\_\*y=\lambda y. } \\]

This is a correct and useful characterization.

It shows that the spectral condition is not simply an eigenvalue-avoidance condition for \\(A\_\*\\).

It is an eigenvalue-avoidance condition for the restriction of \\(A\_\*\\) to the subspace \\(\ker B\_\*\\), in the sense that no nonzero vector in that subspace may be an eigenvector of \\(A\_\*\\).

One must be slightly careful with the phrase "restriction to \\(\ker B\_\*\\)": the subspace need not be invariant under \\(A\_\*\\). The precise condition is the displayed simultaneous kernel equation.

### 4.1 An important consequence

The spectral condition can be written as

\\[ \ker(\lambda I-A\_\*)\cap\ker B\_\*=\\{0\\} \qquad\forall\lambda\in\mathbb C. \\]

This form is especially convenient for theoretical analysis.

It also provides a direct connection to observability-type rank conditions.

I recommend retaining this formulation prominently in the paper.

## 5. The three-compression framework: a necessary refinement

The proposed chain is

\\[ R\longrightarrow(H,H_A)\longrightarrow Z \longrightarrow\text{incidence space}. \\]

This is conceptually correct, but the first arrow is not a bijective reduction.

Different original matrices can have the same compressed pair.

More importantly, the compressed pair does not retain all the information required for the full-row-rank condition.

I would therefore use the following diagram:

Original observer matrix \\(L\\)

Fixed rows \\(L_0\\), adjustable rows, independence constraints

Compressed pair \\((H,H_A)\\)

Exact restriction to \\(K_0\\); affine lifting fibre retained

Compatible operator \\(Z\\)

Domain compatibility and partial-eigenvector criterion

Lifted incidence variety

Actual observer variables, determinantal conditions, spectral-good locus

The affine lifting fibre must not be discarded.

This observation leads directly to the most important theorem that should be developed next.

# Part III. The lift-completion problem: the central unresolved issue

## 6. The exact sequence is correct, but it should be used more systematically

Let

\\[ \mathcal X^\*=\mathbb C^{1\times n}, \\]

and define

\\[ S_C=\operatorname{row}C, \qquad T_C=\operatorname{row}[C;CA]. \\]

By definition,

\\[ K_0=\ker[C;CA]. \\]

The restriction map

\\[ \rho:\mathcal X^\*\longrightarrow K_0^\*, \qquad \rho(g)=gN \\]

has kernel

\\[ \ker\rho=T_C. \\]

It is surjective: every linear functional on \\(K_0\\) extends to a linear functional on \\(\mathbb C^n\\).

Therefore there is an exact sequence

\\[ \boxed{ 0\longrightarrow T_C/S_C \longrightarrow \mathcal X^\*/S_C \overset{\rho}{\longrightarrow} K_0^\* \longrightarrow0. } \\]

Set

\\[ E_C=T_C/S_C. \\]

Then

\\[ d_C=\dim E_C = \operatorname{rank}[C;CA]-\operatorname{rank}C. \\]

This part of the report is correct.

### 6.1 The second compression must also be included in the exact sequence

The compressed pair of a row \\(g\in\mathcal X^\*\\) is

\\[ \Psi(g+S_C) = (gN,gAN). \\]

This is well-defined because

\\[ CN=0,\qquad CAN=0. \\]

Thus we have a linear map

\\[ \boxed{ \Psi: \mathcal X^\*/S_C \longrightarrow K_0^\*\oplus K_0^\*. } \\]

Its kernel is

\\[ \ker\Psi = \left\\{ g+S_C: gN=0,\quad gAN=0 \right\\}. \\]

Since \\(gN=0\\) implies \\(g\in T_C\\), this kernel is precisely

\\[ E'\_C= \frac{ \\{g\in T_C:gAN=0\\} }{S_C}. \\]

Consequently,

\\[ \boxed{ \dim E'\_C = d_C-\operatorname{rank}\Gamma, } \\]

where

\\[ \Gamma:E_C\longrightarrow K_0^\*, \qquad \Gamma(g+S_C)=gAN. \\]

This proves the dimension formula

\\[ d'\_C=d_C-\operatorname{rank}\Gamma. \\]

The formula is correct.

There is, however, a subtle point about the interpretation of \\(d'\_C\\).

It is the dimension of the kernel of the map that records both compressed coordinates. It is not, by itself, a statement that every arbitrary compressed pair can be lifted.

The image of \\(\Psi\\) may be a proper subspace of

\\[ K_0^\*\oplus K_0^\*. \\]

This distinction should be built into the theorem.

## 7. The calculation \\(gAN=bCA^2N\\) is correct

Suppose

\\[ g=aC+bCA. \\]

Since the columns of \\(N\\) belong to \\(K_0\\),

\\[ CAN=0. \\]

Then

\\[ \begin{aligned} gAN &=aCAN+bCA^2N\\\ &=bCA^2N. \end{aligned} \\]

Thus the invisible directions for the first compression need not be invisible for the second compression.

This is an important correction to the original lift argument.

It also identifies exactly where the second-order dynamics enter:

\\[ CA^2N. \\]

I recommend defining

\\[ G_C=CA^2N \\]

as a named matrix.

If \\(C\\) has full row rank, the map \\(\Gamma\\) can be represented, after choosing a basis of the quotient \\(E_C\\), by the action of the coefficients of \\(CA\\) through \\(G_C\\).

The rank of this map is an intrinsic quantity; it should not be confused with the rank of the particular matrix \\(CA^2N\\) before quotienting by dependencies in the rows of \\(C\\).

## 8. A more precise lift-completion theorem

I recommend replacing the informal dimension-counting argument by the following theorem.

It makes the role of the fixed rows \\(L_0\\) explicit and clarifies why the quantity \\(d'\_C\\) is relevant.

### Theorem 8.1. Pair-preserving lift completion

Let

\\[ S_C=\operatorname{row}C, \\]

and suppose

\\[ \operatorname{rank}[C;L_0] = \operatorname{rank}C+r. \\]

Define

\\[ \mathcal Q=\mathcal X^\*/S_C, \\]

and the linear map

\\[ \Psi:\mathcal Q\to K_0^\*\oplus K_0^\*, \qquad \Psi(\bar g)=(gN,gAN). \\]

Let

\\[ E'=\ker\Psi, \qquad d'=\dim E'. \\]

Suppose the prescribed compressed rows are

\\[ z_1,\ldots,z_q\in\operatorname{im}\Psi, \\]

where the first \\(r\\) rows are those determined by \\(L_0\\).

Define

\\[ Z:\mathbb C^q\longrightarrow K_0^\*\oplus K_0^\*, \qquad Z(\alpha)=\sum\_{i=1}^q\alpha_i z_i. \\]

Then there exist lifts

\\[ \bar\ell_1,\ldots,\bar\ell_q\in\mathcal Q \\]

satisfying

\\[ \Psi(\bar\ell_i)=z_i, \\]

with

\\[ \bar\ell_1,\ldots,\bar\ell_r \\]

equal to the prescribed classes of the rows of \\(L_0\\), and with all \\(q\\) classes linearly independent, if and only if

\\[ \boxed{ d'\ge\dim\ker Z. } \\]

Here the fixed rows are assumed to be linearly independent modulo \\(S_C\\), as guaranteed by the displayed rank hypothesis.

### Proof

Let

\\[ \ell:\mathbb C^q\longrightarrow\mathcal Q \\]

be the linear map whose columns are the desired lifted rows.

We need

\\[ \Psi\circ\ell=Z \\]

and

\\[ \ell\text{ injective}. \\]

For every

\\[ \alpha\in\ker Z, \\]

we have

\\[ \Psi(\ell(\alpha))=0. \\]

Thus

\\[ \ell(\ker Z)\subseteq E'. \\]

If \\(\ell\\) is injective, its restriction to \\(\ker Z\\) is injective. Therefore

\\[ \dim E'\ge\dim\ker Z. \\]

This proves necessity.

For sufficiency, let

\\[ K=\ker Z. \\]

The prescribed \\(L_0\\) rows determine \\(\ell\\) on the subspace

\\[ K_0^{\mathrm{fix}} = K\cap\mathbb C^r, \\]

where \\(\mathbb C^r\\) denotes the coefficient subspace supported on the first \\(r\\) coordinates.

Because the rows of \\(L_0\\) are independent modulo \\(S_C\\), this prescribed restriction is injective.

Its image lies in \\(E'\\), because every vector in \\(K\\) produces zero compressed pair.

By the dimension assumption, this injection extends to an injection

\\[ \ell_K:K\longrightarrow E'. \\]

Choose a complementary subspace

\\[ \mathbb C^q=K\oplus K^\perp \\]

and define \\(\ell\\) on \\(K\\) using \\(\ell_K\\).

On \\(K^\perp\\), choose arbitrary lifts of the prescribed values under \\(\Psi\\).

Then

\\[ \Psi\ell=Z. \\]

If

\\[ \ell(\alpha)=0, \\]

then

\\[ Z(\alpha)=\Psi(\ell(\alpha))=0, \\]

so \\(\alpha\in K\\).

But \\(\ell_K\\) is injective, so \\(\alpha=0\\).

Thus \\(\ell\\) is injective.

This completes the proof.

### 8.1 Consequence under (5a)

Under the kernel inclusion

\\[ \ker H\subseteq\ker H_A, \\]

we have

\\[ \operatorname{rank} \begin{bmatrix} H\\\H_A \end{bmatrix} = \operatorname{rank}H = \omega. \\]

Therefore

\\[ \operatorname{rank}Z=\omega \\]

and

\\[ \dim\ker Z=q-\omega. \\]

The theorem gives

\\[ \boxed{ q-\omega\le d'\_C. } \\]

Thus the pair-preserving completion criterion stated in the report is correct, provided that:

1. Every prescribed compressed pair belongs to \\(\operatorname{im}\Psi\\).
2. The fixed rows satisfy the required independence assumption.
3. The compressed pair includes the fixed rows \\(L_0\\), not merely the adjustable rows.
4. The rank condition being completed is independence modulo \\(S_C\\).

This is a more rigorous formulation than a simple argument that counts available invisible directions.

### 8.2 Why this resolves a subtle concern about \\(L_0\\)

It is tempting to argue that the intersection

\\[ E'\_C\cap \frac{\operatorname{row}[C;L_0]}{\operatorname{row}C} \\]

must be subtracted from \\(d'\_C\\).

That subtraction is not generally correct as an independent correction to the theorem.

The fixed invisible combinations of \\(L_0\\) already occupy part of the coefficient kernel \\(\ker Z\\).

The correct dimension condition is

\\[ \dim E'\_C\ge\dim\ker Z. \\]

It automatically accounts for the directions already determined by the fixed rows.

This is precisely why the theorem should be formulated through the map \\(Z\\), rather than through a bare count of additional rows.

### 8.3 What the theorem does not establish

The theorem is a completion result for prescribed compressed pairs.

It does not prove that a suitable compressed pair exists.

It does not prove that a pair satisfying the spectral condition exists.

It does not prove that the six \\(c=2\\) strata contain a good point.

These are separate questions.

This distinction should be explicit in the paper.

## 9. The most useful improvement: formulate the lift problem as one linear map

The preceding theorem suggests a cleaner computational formulation.

Choose a basis of

\\[ \mathcal Q=\mathcal X^\*/S_C. \\]

Construct the matrix representing

\\[ \Psi(\bar g)=(gN,gAN). \\]

Then compute:

\\[ \operatorname{im}\Psi, \qquad \ker\Psi, \qquad d'=\dim\ker\Psi. \\]

For a candidate compressed pair \\((H,H_A)\\):

1. Check that each row pair belongs to \\(\operatorname{im}\Psi\\).
2. Check that the first \\(r\\) rows agree with the prescribed \\(L_0\\).
3. Compute the rank of the combined pair map \\(Z\\).
4. Check

\\[ \dim\ker Z\le d'. \\]

5. Construct an injective extension on \\(\ker Z\\).
6. Recover actual row vectors representing the lifted classes.

All these operations are finite-dimensional linear algebra.

In particular, once a compressed pair is fixed, the pair-preserving completion problem is polynomial-time solvable over exact rational or algebraic input, with the usual bit-complexity qualifications.

This is an important practical result.

It means that the lift problem, conditional on a prescribed compressed pair, is not itself the difficult nonlinear part of the project.

The difficulty lies in finding a compressed pair whose spectral pencil is good.

# Part IV. The Grassmannian and incidence geometry

## 10. The exact fibre theorem

The report's fibre theorem is one of its strongest geometric statements.

Let

\\[ V\in\operatorname{Gr}(c,K_0), \\]

and define

\\[ W=V\cap A^{-1}V. \\]

Write

\\[ t=\dim W, \qquad U=W+A(W), \qquad u=\dim U. \\]

Define

\\[ \Phi_V:V\longrightarrow\mathcal X/V, \qquad v\longmapsto Av+V. \\]

Then

\\[ \ker\Phi_V=W. \\]

Consequently,

\\[ \operatorname{rank}\Phi_V=c-t. \\]

For a fixed subspace \\(W\\), define

\\[ \mathcal F_W= \left\\{ V\in\operatorname{Gr}(c,K_0): U\subseteq V,\  \operatorname{rank}\Phi_V=c-t \right\\}. \\]

Then

\\[ \boxed{ \mathcal F_W \text{ is open in } \operatorname{Gr}(c-u,K_0/U). } \\]

### Proof

If \\(W\subseteq V\\) and \\(A(W)\subseteq V\\), then

\\[ U=W+A(W)\subseteq V. \\]

Conversely, \\(U\subseteq V\\) implies

\\[ W\subseteq V\cap A^{-1}V. \\]

Thus

\\[ W\subseteq\ker\Phi_V. \\]

The condition

\\[ \operatorname{rank}\Phi_V=c-t \\]

is equivalent to

\\[ \dim\ker\Phi_V=t. \\]

Since \\(W\\) already has dimension \\(t\\), this gives

\\[ \ker\Phi_V=W. \\]

The rank equality is an open condition in the family of maps under consideration.

All \\(V\\) containing \\(U\\) are parametrised by

\\[ \operatorname{Gr}(c-u,K_0/U). \\]

Therefore the result follows.

### 10.1 An essential quotient-space correction

The ambient target of \\(\Phi_V\\) is

\\[ \mathcal X/V, \\]

not

\\[ K_0/V. \\]

This distinction is fundamental.

Replacing the ambient space by \\(K_0\\) would require

\\[ A(K_0)\subseteq K_0, \\]

which is not among the original assumptions.

The theorem should retain the ambient quotient throughout.

### 10.2 A useful additional observation

The fibre is nonempty only if

\\[ u\le c \\]

and

\\[ c-u\le k-u, \\]

the latter being automatic when \\(c\le k\\).

But the open rank condition may still make the fibre empty.

Thus the relative Grassmannian description is not equivalent to saying that every base point has a nonempty fibre.

The nonemptiness condition must be checked.

## 11. The general \\((t,u)\\)-stratification is sound but conditional

Define

\\[ D=K_0\cap A^{-1}K_0. \\]

Since

\\[ W\subseteq K_0 \\]

and

\\[ A(W)\subseteq K_0, \\]

we necessarily have

\\[ W\subseteq D. \\]

The dimension of \\(W+A(W)\\) satisfies

\\[ t\le u\le2t. \\]

The base strata are

\\[ S\_{t,u} = \left\\{ W\in\operatorname{Gr}(t,D): \dim(W+A(W))=u \right\\}. \\]

These are locally closed determinantal strata.

To see this, consider the bundle map

\\[ \mathcal W\longrightarrow K_0/W, \qquad w\longmapsto Aw+W, \\]

where \\(\mathcal W\\) is the tautological bundle over \\(\operatorname{Gr}(t,D)\\).

The rank of this map is

\\[ u-t. \\]

Thus the condition defining \\(S\_{t,u}\\) is an exact-rank condition.

Exact-rank loci are locally closed.

Over \\(S\_{t,u}\\), the fibre is an open subset of the corresponding relative Grassmannian.

This gives a finite stratification.

### 11.1 What follows about irreducibility?

Suppose \\(S\_{t,u}\\) is irreducible.

Suppose the relative Grassmannian is defined over \\(S\_{t,u}\\).

Suppose the open fibre is nonempty over every point of the base.

Then the total space is irreducible.

However, the last hypothesis matters.

An open subset of a relative Grassmannian can be empty over some base points, and the locus over which it is nonempty must itself be understood.

A clean formulation is to define

\\[ S\_{t,u}^{\mathrm{adm}} = \\{W\in S\_{t,u}:\mathcal F_W\ne\varnothing\\}. \\]

Then the lifted space over this admissible base should be analysed.

This is a useful refinement for the general theorem.

## 12. The \\(c=2\\) classification: a promising theorem, but the component argument needs a precise scope

The six proposed cases are mathematically natural.

For

\\[ c=2, \qquad \dim V=2, \\]

we have

\\[ t=\dim(V\cap A^{-1}V)\in\\{0,1,2\\}. \\]

These three possibilities give the basic decomposition.

### 12.1 Case \\(t=2\\): invariant planes

Here

\\[ V\subseteq A^{-1}V, \\]

so

\\[ A(V)\subseteq V. \\]

The restriction \\(A|\_V\\) is a two-dimensional complex linear operator.

There are three possibilities.

Type I: two distinct eigenvalues.

Then

\\[ V=\ell_1\oplus\ell_2, \\]

where

\\[ A\ell_i=\lambda_i\ell_i, \qquad \lambda_1\ne\lambda_2. \\]

Both eigenlines must lie in \\(K_0\\).

For each unordered pair of distinct eigenvalues, the parameter space is a product of projective eigenspaces, modulo interchange of the two factors.

If the eigenspaces intersect \\(K_0\\) nontrivially, the resulting parameter space is irreducible whenever nonempty.

Type II: scalar restriction.

Here

\\[ A|\_V=\lambda I. \\]

Thus

\\[ V\in\operatorname{Gr} \left(2,E\_\lambda\cap K_0\right), \\]

where

\\[ E\_\lambda=\ker(A-\lambda I). \\]

This is an irreducible Grassmannian whenever nonempty.

Type III: one Jordan block of size two.

There exist linearly independent \\(v,x\in K_0\\) satisfying

\\[ (A-\lambda I)v=0, \qquad (A-\lambda I)x=v. \\]

The eigenline

\\[ \ell=\langle v\rangle \\]

must satisfy

\\[ \ell\subseteq E\_\lambda\cap(A-\lambda I)(K_0). \\]

The set of possible eigenlines is a projective linear subspace.

Over each such line, the generalized eigenvector has an affine family of choices, modulo the eigenline.

This is the correct geometric source of the affine-fibre description.

The irreducibility argument should explicitly establish that this affine family is a vector bundle or affine bundle over the relevant projective linear base.

### 12.2 Case \\(t=1\\): one-dimensional intersection

Let

\\[ W=L=\langle v\rangle. \\]

Then

\\[ Av\in V. \\]

There are two cases.

Type IV: \\(L\\) is \\(A\\)-invariant.

Then

\\[ Av=\lambda v. \\]

The plane can be written

\\[ V=L\oplus\langle x\rangle, \\]

where

\\[ x\notin L, \qquad Ax\notin V. \\]

The last condition guarantees that

\\[ V\cap A^{-1}V=L \\]

rather than all of \\(V\\).

The base is a projective eigenspace, and the admissible choices of \\(x\\) form an open subset of a suitable projective quotient.

Type V: \\(L\\) is not \\(A\\)-invariant.

Then \\(v,Av\\) are linearly independent.

Since \\(Av\in V\\), necessarily

\\[ V=\langle v,Av\rangle. \\]

The exact condition that \\(t=1\\) is

\\[ A^2v\notin\langle v,Av\rangle. \\]

Equivalently,

\\[ \boxed{ \operatorname{rank}[v,Av,A^2v]=3. } \\]

This gives an open rank-exact condition on the corresponding projective parameter space.

### 12.3 Case \\(t=0\\): transverse planes

Here

\\[ V\cap A^{-1}V=\\{0\\}. \\]

This is an open condition in

\\[ \operatorname{Gr}(2,K_0). \\]

Consequently, if nonempty, this stratum is irreducible.

## 13. Is the \\(c=2\\) component bound valid?

The proposed bound is

\\[ \boxed{ \\#\\{\text{components}\\} \le \binom{s}{2}+3s+2, } \\]

where \\(s\\) is the number of distinct eigenvalues of \\(A\\).

The counting argument is understandable:

| Geometric type                              | Maximum number of irreducible parameter families |
| ------------------------------------------- | ------------------------------------------------ |
| Two distinct eigenvalues                    | \\(\binom{s}{2}\\)                               |
| Scalar restriction                          | \\(s\\)                                          |
| Jordan block of size two                    | \\(s\\)                                          |
| Invariant line plus complementary direction | \\(s\\)                                          |
| Non-invariant line                          | \\(1\\)                                          |
| Transverse planes                           | \\(1\\)                                          |

Summing gives the claimed expression.

I regard this as a plausible and potentially strong theorem.

However, there is a distinction that must be enforced in the final paper.

### 13.1 Three different component counts

The project contains at least three varieties:

1. The admissible Grassmannian base of \\(V\\)'s.
2. The compressed incidence space of pairs \\((H,H_A)\\).
3. The lifted incidence space of actual observer matrices \\(L\\).

The bound obtained by counting the six \\(V\\)-strata directly applies first to the base geometry.

It does not automatically apply to the other two spaces.

To transfer the bound, one must prove that the relevant maps have irreducible fibres and that the admissibility and independence conditions cut out nonempty open subsets over the appropriate base components.

The pair-preserving lifting theorem from Section 8 is a useful ingredient.

For instance, if over an irreducible base component the compressed pair parameters form an irreducible bundle, and the compatible lift is a nonempty affine bundle followed by an open independence condition, then the lifted space is irreducible.

But this must be demonstrated for the actual family.

### 13.2 The spectral-good locus

Suppose the lifted incidence component \\(X_i\\) is irreducible.

Let

\\[ B_i\subseteq X_i \\]

be the spectral-bad locus.

If the projective closedness theorem applies, then \\(B_i\\) is closed.

Thus either

\\[ B_i=X_i \\]

or

\\[ X_i\setminus B_i \\]

is a dense open subset.

This is an excellent reduction.

But it requires that the projective pencil family be defined on the entire component, with the correct constant-rank layer and the correct treatment at infinity.

It is not enough to establish closedness on the compressed base while ignoring the lift variables.

### 13.3 My verdict on the \\(c=2\\) bound

I recommend retaining

\\[ \binom{s}{2}+3s+2 \\]

as a theorem for the \\(V\\)-parameter geometry once all six irreducibility proofs are complete.

For the lifted observer incidence variety, state a separate theorem with explicit hypotheses on the lift fibres.

Do not silently identify the two component counts.

This distinction will make the paper substantially more rigorous.

## 14. The \\(c=3\\) classification: an audit is necessary before counting

The report lists eleven strata.

I would not yet endorse the statement that these are eleven irreducible varieties.

There are two independent issues:

1. Whether the eleven cases are exhaustive and mutually exclusive.
2. Whether each individual case is irreducible.

These should be checked separately.

### 14.1 First audit the classification itself

For

\\[ \dim V=3, \\]

we have

\\[ t\in\\{0,1,2,3\\}. \\]

The invariant case \\(t=3\\) involves three-dimensional invariant subspaces.

The possible Jordan module structures of a three-dimensional restriction include:

- three distinct eigenvalues;
- one repeated eigenvalue with a two-dimensional eigenspace and another eigenvalue;
- a scalar operator;
- one Jordan block of size two together with a distinct eigenvalue;
- one Jordan block of size two together with a one-dimensional block at the same eigenvalue;
- one Jordan block of size three.

The report's shorthand should be replaced by explicit Jordan data.

For example, the notation \\(1+1+1\\) is ambiguous unless it specifies whether the three blocks belong to the same eigenvalue or to distinct eigenvalues.

I recommend describing each invariant type by:

\\[ \\{(\lambda_i,\pi_i)\\}\_i, \\]

where \\(\lambda_i\\) is an eigenvalue and \\(\pi_i\\) is a partition describing the Jordan block sizes for that eigenvalue.

This eliminates possible overlaps.

### 14.2 The highest-priority non-invariant case

The report identifies

\\[ S\_{2,3} = \left\\{ W\in\operatorname{Gr}(2,D): \dim(W+A_0(W))=3 \right\\} \\]

as a potentially difficult stratum.

This concern is justified.

Let

\\[ f:D\longrightarrow K_0 \\]

be the map induced by \\(A\\), followed by the relevant quotient or projection.

The condition

\\[ \dim(W+A(W))=3 \\]

is equivalent to

\\[ \operatorname{rank}(f|\_W)=1 \\]

when \\(W\\) has dimension two and the intersection \\(W\cap A(W)\\) has dimension one.

Equivalently, it is a rank-exact condition on a bundle map over the Grassmannian.

Rank-at-most-one loci are determinantal, but exact-rank loci need not be irreducible in general.

The special form of \\(f\\) may impose additional structure, but that structure must be used in the proof.

### 14.3 Recommended method for the \\(c=3\\) audit

For each of the eleven strata:

1. Write its defining subspace conditions.
2. Express the conditions as ranks of explicitly defined bundle maps.
3. Identify the base parameter space.
4. Determine whether the base is a Grassmannian, projective bundle, affine bundle, or determinantal variety.
5. If determinantal, calculate its irreducible decomposition or prove irreducibility from the special operator structure.
6. Establish the nonemptiness of the open fibre.
7. Only then count components.

For computational exploration, use small dimensions and several Jordan types.

In particular, test

\\[ \dim K_0=4,5,6. \\]

Use exact rational or algebraic arithmetic.

A numerical failure to find reducibility is not an irreducibility proof.

### 14.4 What I would publish now

I would publish the eleven-stratum description only if its exhaustiveness and mutual exclusivity have been independently established.

I would state the component-count result conditionally until the irreducibility audit is complete.

The proposed expression

\\[ \binom{s}{3}+3s^2+6s+1 \\]

should not yet be presented as a theorem.

# Part V. General \\(c\\) and representation-theoretic structure

## 15. Why the general component problem is substantially harder

The general base strata are

\\[ S\_{t,u} = \left\\{ W\in\operatorname{Gr}(t,D): \dim(W+A(W))=u \right\\}. \\]

The integer pair \\((t,u)\\) gives a finite stratification, but it does not control the number of irreducible components.

The number

\\[ p(c)n^c \\]

is a bound on a crude count of possible combinatorial Jordan-type labels under the relevant finite-dimensional setting.

It is not a bound on irreducible components.

The reason is that a single Jordan-type label can correspond to a reducible family of invariant subspaces.

The geometry of invariant-subspace varieties can be much more complicated than the Jordan classification of individual restrictions.

### 15.1 The quiver-Grassmannian viewpoint

There is a natural representation-theoretic formulation.

A linear operator \\(A\\) on a vector space \\(X\\) is a representation of the one-loop quiver.

An \\(A\\)-invariant subspace is a subrepresentation.

The variety of invariant subspaces of fixed dimension is therefore a quiver Grassmannian.

This perspective is useful because it connects the project to:

- representation varieties;
- submodule varieties;
- orbit closures;
- degenerations of modules;
- extension spaces;
- decomposition into indecomposable modules.

However, the condition

\\[ W\subseteq D, \qquad \dim(W+A(W))=u \\]

is more general than simply requiring \\(W\\) to be invariant.

It is better viewed as a constrained incidence condition involving a representation and its image.

I would therefore use quiver-Grassmannian language as an organising framework, not as an automatic irreducibility theorem.

### 15.2 A realistic general theorem

The strongest currently defensible general statement is conditional.

Suppose each base stratum \\(S\_{t,u}\\) has at most \\(B\_{t,u}\\) irreducible components.

Suppose the admissible relative Grassmannian fibres are nonempty over the corresponding components.

Suppose the compressed-pair and lift families have irreducible nonempty fibres.

Then the number of irreducible components of the resulting lifted incidence variety is bounded by

\\[ \boxed{ \sum\_{t=0}^{c} \sum\_{u=t}^{\min(2t,c)} B\_{t,u}. } \\]

This statement needs the usual qualification that one counts only nonempty admissible strata and that the relevant fibre maps have the stated irreducibility properties.

It is a useful theorem because it separates:

- the difficult invariant-subspace geometry;
- the comparatively manageable lifting geometry.

I would include it in the general theory.

# Part VI. Polynomial matrices and the \\(\exists\mathbb R\\) upper bound

## 16. The polynomial generalized-inverse theorem

This is one of the most promising independent contributions of the project.

Let

\\[ P(\lambda)\in\mathbb C[\lambda]^{m\times n} \\]

have normal rank \\(\omega\\).

Suppose

\\[ \operatorname{rank}P(\lambda)=\omega \qquad\forall\lambda\in\mathbb C. \\]

Then the project claims that there exists

\\[ Y(\lambda)\in\mathbb C[\lambda]^{n\times m} \\]

such that

\\[ \boxed{ P(\lambda)Y(\lambda)P(\lambda)=P(\lambda) } \\]

and

\\[ \boxed{ \deg Y\le2\omega-2. } \\]

For \\(\omega\ge1\\), the proposed proof is correct.

I would present it as a standalone theorem.

## 17. Detailed verification of the Bézout-adjugate construction

Let

\\[ p\_{I,J}(\lambda) = \det P\_{I,J}(\lambda) \\]

denote the nonzero \\(\omega\times\omega\\) minors.

Since the rank is \\(\omega\\) at every finite complex point,

\\[ \gcd\_{I,J}p\_{I,J}=1. \\]

Choose one nonzero minor

\\[ p_1 \\]

with degree

\\[ d=\deg p_1\le\omega. \\]

Since the gcd is one, the other minors generate the unit ideal modulo \\(p_1\\):

\\[ \sum\_{(I,J)\ne1}b\_{I,J}p\_{I,J} \equiv1\pmod{p_1}. \\]

Because

\\[ \mathbb C[\lambda]/(p_1) \\]

is finite-dimensional and every residue class has a representative of degree less than \\(d\\), the coefficients can be chosen with

\\[ \deg b\_{I,J}\<d. \\]

There is therefore a polynomial \\(b_1\\) satisfying

\\[ 1=\sum\_{I,J}b\_{I,J}p\_{I,J}. \\]

We must also bound the degree of \\(b_1\\).

For the terms other than \\(p_1\\),

\\[ \deg(b\_{I,J}p\_{I,J}) \le(d-1)+\omega. \\]

Thus the numerator

\\[ 1-\sum\_{(I,J)\ne1}b\_{I,J}p\_{I,J} \\]

has degree at most

\\[ d+\omega-1. \\]

Dividing by \\(p_1\\), we obtain

\\[ \deg b_1\le\omega-1. \\]

Hence

\\[ \boxed{ \deg b\_{I,J}\le\omega-1. } \\]

### 17.1 The embedded-adjugate identity

For each minor \\(P\_{I,J}\\), define the matrix

\\[ E\_{I,J}\in\mathbb C[\lambda]^{n\times m} \\]

by placing

\\[ \operatorname{adj}(P\_{I,J}) \\]

in the rows indexed by \\(J\\) and columns indexed by \\(I\\), with all other entries zero.

Then

\\[ \boxed{ P E\_{I,J}P = p\_{I,J}P. } \\]

To verify this, work first over the rational-function field \\(\mathbb C(\lambda)\\), where the selected minor is invertible.

Because the normal rank is \\(\omega\\),

\\[ P=P\_{:,J}P\_{I,J}^{-1}P\_{I,:}. \\]

Consequently,

\\[ \begin{aligned} PE\_{I,J}P &= P\_{:,J}\operatorname{adj}(P\_{I,J})P\_{I,:}\\\ &= \det(P\_{I,J}) P\_{:,J}P\_{I,J}^{-1}P\_{I,:}\\\ &= p\_{I,J}P. \end{aligned} \\]

Both sides have polynomial entries, so the identity holds in the polynomial ring.

Now set

\\[ Y(\lambda) = \sum\_{I,J}b\_{I,J}(\lambda)E\_{I,J}(\lambda). \\]

We obtain

\\[ \begin{aligned} PYP &= \sum\_{I,J}b\_{I,J}PE\_{I,J}P\\\ &= \sum\_{I,J}b\_{I,J}p\_{I,J}P\\\ &= P. \end{aligned} \\]

Since

\\[ \deg E\_{I,J}\le\omega-1 \\]

and

\\[ \deg b\_{I,J}\le\omega-1, \\]

we conclude

\\[ \boxed{ \deg Y\le2\omega-2. } \\]

This proof is rigorous.

### 17.2 The zero-rank case

When

\\[ \omega=0, \\]

the matrix polynomial is identically zero.

Set

\\[ Y=0. \\]

The degree-bound formula should not be applied in this case.

## 18. An important improvement: a direct certificate for the original pencil

There is a useful way to strengthen the complexity part.

The project has developed the certificate for the compressed pencil

\\[ P(\lambda)=\lambda H-H_A. \\]

But the same theorem can be applied directly to the original pencil

\\[ \boxed{ Q(\lambda)= \begin{bmatrix} \lambda L-LA\\\ CA\\\ C \end{bmatrix}. } \\]

This may simplify the proof of \\(\exists\mathbb R\\) membership considerably.

Define

\\[ s=\operatorname{rank} \begin{bmatrix} L\\\CA\\\C \end{bmatrix}. \\]

Under (5a), every row of \\(LA\\) belongs to the row space of

\\[ \begin{bmatrix}L\\\CA\\\C\end{bmatrix}. \\]

Therefore every row of \\(\lambda L-LA\\) belongs to that same row space.

It follows that

\\[ \operatorname{rank}Q(\lambda)\le s \qquad\forall\lambda. \\]

Condition (5b) is exactly

\\[ \operatorname{rank}Q(\lambda)=s \qquad\forall\lambda\in\mathbb C. \\]

Thus, under (5a), (5b) is equivalent to the assertion that \\(Q\\) has constant rank \\(s\\) at every finite complex point.

The polynomial generalized-inverse theorem gives a polynomial matrix

\\[ Y(\lambda)\in\mathbb C[\lambda]^{n\times(q+2p)} \\]

with

\\[ \boxed{ Q(\lambda)Y(\lambda)Q(\lambda)=Q(\lambda) } \\]

and

\\[ \boxed{ \deg Y\le2s-2. } \\]

This is an alternative certificate.

### 18.1 Why a normal-rank condition must be included

There is a subtle but important logical point.

The identity

\\[ QYQ=Q \\]

alone does not imply that \\(Q\\) has the required rank.

For example, a constant matrix of rank smaller than \\(s\\) always has a generalized inverse satisfying this identity.

The correct equivalence is:

- \\(\operatorname{rank}Q(\lambda)\le s\\) for all \\(\lambda\\);
- the normal rank of \\(Q\\) is \\(s\\);
- there exists a polynomial \\(Y\\) satisfying \\(QYQ=Q\\).

The normal-rank condition can be expressed by requiring that at least one \\(s\times s\\) minor of \\(Q\\) is not the zero polynomial.

Equivalently, there exist a complex number \\(\lambda_0\\) and an \\(s\times s\\) minor such that

\\[ \det Q\_{I,J}(\lambda_0)\ne0. \\]

Then

\\[ \operatorname{rank}Q(\lambda_0)=s \\]

because the upper bound is already known.

This extra condition is essential.

### 18.2 Why the certificate implies constant rank

Suppose \\(Q\\) has normal rank \\(s\\) and

\\[ QYQ=Q \\]

with polynomial \\(Y\\).

Fix any \\(\lambda_0\in\mathbb C\\).

Over the local ring

\\[ \mathbb C[\lambda]\_{(\lambda-\lambda_0)}, \\]

put \\(Q\\) into Smith form:

\\[ UQV= \begin{bmatrix} d_1&&&0\\\ &d_2&&0\\\ &&\ddots&0\\\ 0&&&d_s \end{bmatrix}, \\]

with the remaining rows and columns zero.

The matrices \\(U,V\\) are invertible over the local ring.

Transforming the generalized-inverse identity gives

\\[ D\widetilde YD=D. \\]

In particular,

\\[ d_i^2\widetilde y\_{ii}=d_i. \\]

Since \\(d_i\ne0\\) in the domain, cancellation gives

\\[ d_i\widetilde y\_{ii}=1. \\]

Therefore \\(d_i\\) is a unit in the local ring.

Hence none of the invariant factors vanishes at \\(\lambda_0\\).

It follows that

\\[ \operatorname{rank}Q(\lambda_0)=s. \\]

Since \\(\lambda_0\\) was arbitrary,

\\[ \operatorname{rank}Q(\lambda)=s \qquad\forall\lambda\in\mathbb C. \\]

This establishes the converse.

### 18.3 Why this direct certificate is useful

It avoids the need to introduce:

- a basis \\(N\\) of \\(K_0\\);
- the compressed pair \\((H,H_A)\\);
- the compressed rank \\(\omega\\);
- the separate polynomial pencil \\(P\\).

For the geometric theory, the compressed formulation remains superior.

For the complexity upper bound, the original pencil may be simpler.

I would prove both versions and use whichever gives the cleanest theorem.

## 19. A second proof through Smith normal form

The project can also give a conceptual proof of polynomial generalized-inverse existence.

Over the PID

\\[ \mathbb C[\lambda], \\]

there exist unimodular polynomial matrices \\(U,V\\) such that

\\[ UPV= \operatorname{diag}(d_1,\ldots,d\_\omega,0,\ldots,0), \\]

where

\\[ d_1\mid d_2\mid\cdots\mid d\_\omega. \\]

The determinantal divisors are products of the invariant factors.

The condition that the maximal minors have gcd one implies

\\[ d_1\cdots d\_\omega \\]

is a unit.

Thus every \\(d_i\\) is a unit.

After rescaling,

\\[ UPV= \begin{bmatrix} I\_\omega&0\\\ 0&0 \end{bmatrix}. \\]

This immediately gives a polynomial generalized inverse.

The two proofs serve different purposes:

| Proof                | Main advantage                                            |
| -------------------- | --------------------------------------------------------- |
| Smith normal form    | Conceptual explanation of why a polynomial inverse exists |
| Bézout and adjugates | Explicit degree bound and constructive certificate        |

The second is the appropriate proof for the complexity theorem.

# Part VII. Computational complexity

## 20. Does the certificate prove membership in \\(\exists\mathbb R\\)?

My conclusion is yes, under a rational-input model.

However, I would formulate the proof carefully.

### 20.1 Input model

Assume the entries of

\\[ A,\ C,\ L_0 \\]

belong to

\\[ \mathbb Q(i)=\\{a+ib:a,b\in\mathbb Q\\}. \\]

Each complex unknown is represented by two real variables.

All matrix equations over \\(\mathbb C\\) are replaced by their real and imaginary parts.

A complex polynomial equality is therefore equivalent to two real polynomial equalities.

The resulting system is an existential formula over the real numbers.

### 20.2 Encoding rank

For a matrix \\(M\\) with rational or polynomial entries,

\\[ \operatorname{rank}M\le d \\]

is equivalent to the vanishing of all \\((d+1)\times(d+1)\\) minors.

The condition

\\[ \operatorname{rank}M=d \\]

additionally requires at least one \\(d\times d\\) minor to be nonzero.

Over complex variables, a complex determinant \\(z=x+iy\\) is nonzero exactly when

\\[ x^2+y^2>0. \\]

Thus exact rank can be expressed by polynomial equations and strict polynomial inequalities.

The number of minors is polynomial in the matrix dimensions.

### 20.3 Encoding (5a)

Let

\\[ D_0= \begin{bmatrix} L\\\CA\\\C \end{bmatrix}. \\]

The first condition is

\\[ \operatorname{rank} \begin{bmatrix} LA\\\D_0 \end{bmatrix} = \operatorname{rank}D_0. \\]

Introduce an integer rank parameter \\(s\\), with

\\[ 0\le s\le\min(n,q+2p). \\]

Impose

\\[ \operatorname{rank}D_0=s \\]

and

\\[ \operatorname{rank} \begin{bmatrix} LA\\\D_0 \end{bmatrix} =s. \\]

This gives a finite existential rank encoding.

### 20.4 Encoding (5b) using the direct certificate

Define

\\[ Q(\lambda)= \begin{bmatrix} \lambda L-LA\\\CA\\\C \end{bmatrix}. \\]

Introduce the unknown polynomial matrix

\\[ Y(\lambda) = Y_0+Y_1\lambda+\cdots+Y_D\lambda^D, \\]

where

\\[ D=2s-2 \\]

for \\(s\ge1\\).

Impose

\\[ Q(\lambda)Y(\lambda)Q(\lambda)=Q(\lambda). \\]

Equating coefficients of \\(\lambda\\) gives finitely many polynomial equations.

The degree of the left-hand side is at most

\\[ 2D+2=4s-2, \\]

because \\(Q\\) has degree at most one.

The normal-rank condition is encoded by introducing \\(\lambda_0\\) and requiring at least one \\(s\times s\\) minor of \\(Q(\lambda_0)\\) to be nonzero.

Under (5a), the rank of \\(Q(\lambda)\\) is at most \\(s\\) for all \\(\lambda\\).

The certificate then implies that its rank is exactly \\(s\\) everywhere.

Thus the existential system is equivalent to (5b).

For \\(s=0\\), handle the zero pencil separately.

### 20.5 Encoding the full-row-rank condition

If the required condition is

\\[ \operatorname{rank}L=q, \\]

add the corresponding exact-rank constraints.

If the stronger requirement is

\\[ \operatorname{rank}[C;L] = \operatorname{rank}C+q, \\]

encode that rank instead.

The fixed rows \\(L_0\\) are imposed by equality constraints on the appropriate rows of \\(L\\).

### 20.6 Polynomial size

The number of coefficients in \\(Y\\) is bounded by

\\[ O(smn), \\]

where \\(m=q+2p\\) is the number of rows of \\(Q\\), up to the usual indexing convention.

Since

\\[ s\le\min(n,q+2p), \\]

this is polynomial in the matrix dimensions.

The coefficient equations have bounded polynomial degree.

Their rational coefficients have bit lengths controlled by the input bit lengths and the arithmetic operations used in the construction.

Therefore the resulting existential formula has polynomial encoding size.

We obtain

\\[ \boxed{ \mathrm{DEC}(q)\in\exists\mathbb R. } \\]

Here \\(\mathrm{DEC}(q)\\) denotes feasibility for a specified \\(q\\).

### 20.7 The minimum-order decision problem

Define

\\[ \mathrm{MIN}(k): \quad \exists q\le k \text{ such that }\mathrm{DEC}(q)\text{ holds}. \\]

Since \\(q\ge r\\) and \\(q\le n\\), this is a finite disjunction:

\\[ \mathrm{MIN}(k) = \bigvee\_{q=r}^{\min(k,n)} \mathrm{DEC}(q). \\]

Under the stronger independence requirement, the upper limit becomes

\\[ \min(k,n-\operatorname{rank}C). \\]

The number of alternatives is polynomial in the input dimensions.

Therefore

\\[ \boxed{ \mathrm{MIN}(k)\in\exists\mathbb R. } \\]

One important point: feasibility need not be monotone in \\(q\\).

The finite disjunction is valid without assuming monotonicity.

## 21. What the \\(\exists\mathbb R\\) result does and does not establish

The result establishes an upper bound.

It does not establish:

\\[ \mathrm{MIN\text{-}ROWS} \text{ is }\exists\mathbb R\text{-hard}. \\]

It does not establish NP-hardness.

It does not establish that a polynomial-time algorithm exists.

The appropriate complexity classification at present is:

\\[ \boxed{ \mathrm{MIN\text{-}ROWS}\in\exists\mathbb R, \qquad \text{hardness unresolved}. } \\]

I would make this a separate theorem in the paper.

It has independent value even if no hardness reduction is eventually found.

# Part VIII. Algorithmic implications and the \\(c=2\\) feasibility problem

## 22. The proposed \\(c=2\\) algorithm: what is established and what is missing?

The proposed algorithm is

\\[ \begin{aligned} &\text{enumerate six admissible strata}\\\ &\longrightarrow\text{construct compressed pairs}\\\ &\longrightarrow\text{complete the lift}\\\ &\longrightarrow\text{test the spectral pencil}. \end{aligned} \\]

This is the right conceptual decomposition.

But it is not yet a complete decision algorithm.

I would refine it into seven steps.

### Step 1. Enumerate the possible kernels

For

\\[ c=2, \\]

enumerate the six geometric types described above.

Each type should be represented by explicit parameters and exact algebraic constraints.

### Step 2. Construct the compressed map

For each candidate \\(V\\), construct

\\[ H:K_0\to\mathbb C^q \\]

with

\\[ \ker H=V, \qquad \operatorname{rank}H=\omega. \\]

A basis-free implementation should preferably use a matrix \\(X\\) whose columns span \\(V\\), together with

\\[ HX=0, \qquad \operatorname{rank}H=\omega. \\]

### Step 3. Impose (5a)

Require

\\[ H_AX=0. \\]

Equivalently,

\\[ \ker H\subseteq\ker H_A. \\]

This must be imposed explicitly.

It is not automatic for a non-invariant \\(V\\).

### Step 4. Parameterise the compatible operator

Construct

\\[ Z:\operatorname{im}H\to\mathbb C^q \\]

such that

\\[ H_A=ZH. \\]

The block decomposition then gives

\\[ Z= \begin{bmatrix} A\_\*\\\B\_\* \end{bmatrix}. \\]

### Step 5. Impose the spectral condition

Require

\\[ \ker(\lambda I-A\_\*)\cap\ker B\_\*=\\{0\\} \qquad\forall\lambda. \\]

Alternatively, compute the gcd of the maximal minors of

\\[ P(\lambda)=\lambda H-H_A. \\]

The gcd method is an exact algebraic test.

### Step 6. Complete the lift

Use the map

\\[ \Psi(\bar g)=(gN,gAN). \\]

Check that the compressed rows are in its image.

Then verify

\\[ d'\_C\ge q-\omega. \\]

Construct the lift using the injective extension on the kernel of the prescribed compressed-pair map.

### Step 7. Verify the original conditions

Finally, construct \\(L\\) and calculate

\\[ \operatorname{rank} \begin{bmatrix} LA\\\L\\\CA\\\C \end{bmatrix}, \\]

\\[ \operatorname{rank} \begin{bmatrix} L\\\CA\\\C \end{bmatrix}, \\]

and the polynomial gcd of the maximal minors of the original pencil.

This final verification is indispensable.

## 23. Can the \\(c=2\\) algorithm be made polynomial-time?

This is an important question.

I would not yet claim polynomial-time solvability, but I believe it is a worthwhile target.

The finite classification of six strata is promising.

However, finite stratification alone does not imply polynomial-time feasibility.

There are three distinct sources of complexity:

1. The parameter spaces of the strata.
2. The affine compatibility constraints.
3. The spectral-good-locus condition.

The second is linear once the compressed pair is fixed.

The first is manageable in low dimension.

The third is where the algebraic difficulty remains.

### 23.1 Generic-point testing

Suppose a lifted component \\(X\\) is irreducible and the spectral-bad locus is closed.

Then either:

\\[ X\_{\mathrm{bad}}=X, \\]

or

\\[ X\_{\mathrm{good}}=X\setminus X\_{\mathrm{bad}} \\]

is dense and open.

This suggests testing a generic point of \\(X\\).

Over an algebraically closed field, this can be expressed by calculating the gcd of maximal minors over the function field

\\[ \mathbb C(X). \\]

If the gcd is one, the generic point is good.

If the gcd is nonconstant, the generic point is bad.

But there is a distinction between generic feasibility and feasibility at a special point.

If a component is entirely bad at generic points, a lower-dimensional exceptional subset could still contain good points only if the bad locus were not closed.

Since the bad locus is closed, that cannot happen: if a dense open subset is bad, the whole irreducible component is bad.

This is precisely why the closedness theorem is valuable.

### 23.2 What must be computed

For each irreducible lifted component:

1. Obtain a rational parameterisation or a function-field representation.
2. Express the pencil entries in that function field.
3. Compute all maximal minors.
4. Calculate their gcd in the univariate polynomial ring over the function field.
5. Test whether the gcd is a unit.

This is a finite exact computation.

The challenge is controlling the size of the rational functions and the complexity of the parameterisation.

### 23.3 My recommendation

Develop two algorithms in parallel.

Geometric algorithm

Uses the six strata, the irreducibility results, and generic-point tests.

Direct algebraic algorithm

Uses a matrix \\(X\\) representing \\(V\\), the linear lift map \\(\Psi\\), and the polynomial certificate.

Compare them experimentally.

The geometric algorithm is likely to give the strongest mathematical theorem.

The direct algebraic algorithm is likely to be easier to implement as a complete baseline.

## 24. An important distinction: fixed-candidate testing versus existential feasibility

The report has made considerable progress on the spectral test for a given pencil.

These are two different problems.

Fixed-candidate problem:

Given \\(L\\), decide whether (5a) and (5b) hold.

This is polynomial-time solvable over exact rational input:

- calculate the relevant ranks;
- calculate the maximal minors;
- compute their polynomial gcd.

Existential problem:

Given \\(A,C,L_0,q\\), decide whether there exists \\(L\\) satisfying the conditions.

This is the actual MIN-ROWS decision problem.

The fact that fixed-candidate testing is easy does not imply that existential feasibility is easy.

This distinction should be emphasised in the introduction and conclusion of the paper.

# Part IX. Complexity and hardness research

## 25. Is fixed \\(c=2\\) likely to be hard?

There is currently insufficient evidence.

I would not infer hardness from general rank-constrained matrix problems.

A reduction must preserve the specific structure

\\[ P(\lambda)=\lambda H-H_A, \\]

together with

\\[ \ker H\subseteq\ker H_A \\]

and the relationship between \\(H,H_A\\) and the original matrices \\(A,C,L_0\\).

An arbitrary affine matrix pencil does not necessarily arise from this construction.

Likewise, an arbitrary determinantal feasibility problem does not automatically embed into the \\(c=2\\) observer problem.

### 25.1 Why \\(c=2\\) may be easier

For fixed \\(c=2\\), the kernel geometry is controlled by a small number of subspace configurations.

The number of geometric types is bounded independently of \\(n\\), apart from the dependence on the number of eigenvalues.

This suggests the possibility of an exact polynomial-time algorithm.

However, the complexity of the spectral condition over the parameter space may still be substantial.

A small number of strata does not mean that the corresponding polynomial feasibility problems are easy.

### 25.2 A useful research strategy

I recommend first proving the following conditional statement:

> For each \\(c=2\\) stratum, the lifted incidence variety admits an effective rational parameterisation, and the spectral-good-locus test can be performed in polynomial time.

If this is true, it gives a polynomial-time algorithm.

If it fails, the proof should identify precisely where the complexity enters.

That would be more informative than searching immediately for a general hardness reduction.

# Part X. Independent references and literature

## 26. Literature that should guide the project

I would divide the bibliography into five groups.

### 26.1 Polynomial matrices and matrix pencils

The central references should be:

- Thomas Kailath — Linear Systems.
- Gohberg, Lancaster and Rodman — Matrix Polynomials.
- Peter Lancaster and Miron Tismenetsky — The Theory of Matrices.

Topics to extract:

1. Smith normal form.
2. Determinantal divisors.
3. Polynomial unimodular transformations.
4. Kronecker canonical form.
5. Minimal indices.
6. Generalised inverses of polynomial matrices.

The project should connect its Bézout certificate explicitly to determinantal divisors.

### 26.2 Invariant-subspace varieties

I recommend studying:

- Murray Gerstenhaber's work on invariant subspaces and commuting matrices.
- Ringel and Schmidmeier's work on invariant subspaces of nilpotent operators.
- The literature on Springer fibres and their irreducible components.
- The theory of quiver Grassmannians.

The purpose is not merely to collect examples of reducible varieties.

It is to identify which special properties of the induced operator on \\(D\\) might guarantee irreducibility for the particular strata appearing in MIN-ROWS.

### 26.3 Algebraic geometry of determinantal varieties

The following concepts are especially relevant:

- determinantal ideals;
- Fitting ideals;
- degeneracy loci;
- Thom–Porteous formulas;
- relative Grassmannians;
- incidence correspondences;
- projective morphisms and properness;
- constructibility and generic fibres.

The distinction between rank-at-most and rank-exact loci is essential.

### 26.4 Existential-real complexity

Study:

- the existential theory of the reals;
- polynomial-time reductions between real algebraic feasibility problems;
- affine rank minimisation;
- structured matrix completion;
- determinantal feasibility.

The recent work on affine rank minimisation and ETR-hardness may offer reduction techniques, but it should be treated as methodological background, not as evidence of MIN-ROWS hardness.

### 26.5 Functional observers

The two preprints identified in the report are important to the problem's formulation:

- Fernando, A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions.
- Fernando, Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger.

The paper should make clear which results are taken from the observer literature and which are new contributions of the MIN-ROWS project.

The distinction is important for establishing novelty.

I would also independently verify the precise correspondence between the problem's notation and the original observer-order formulation, particularly the treatment of prescribed rows \\(L_0\\).

# Part XI. Lean formalisation and computational verification

## 27. Assessment of the existing Lean development

The formalisation is a valuable part of the project.

The reported kernel results include:

- rank inequalities;
- lifting rank formulas;
- explicit counterexamples;
- block-pencil identities;
- the rank formula for \\(Q\\);
- kernel equivalences;
- the constant-matrix generalized-inverse identity.

The reported axiom list is

\\[ [\text{propext},\text{Classical.choice},\text{Quot.sound}]. \\]

This is consistent with ordinary Lean mathematical formalisation without additional unproved axioms.

Nevertheless, the paper should distinguish two kinds of verification.

### 27.1 Formal proof correctness

Does Lean prove the proposition encoded in the theorem?

### 27.2 Mathematical statement correctness

Does that proposition faithfully express the intended mathematical claim?

These are different questions.

For example, a theorem about matrices of a particular fixed dimension may compile perfectly but fail to express the dimension-independent statement needed in the paper.

Similarly, a proof that uses an assumption such as

\\[ A(K_0)\subseteq K_0 \\]

must not be cited as a proof of a theorem that does not assume this invariance.

### 27.3 My recommendation

I would organise the formalisation into five modules.

| Module              | Contents                                   | Priority              |
| ------------------- | ------------------------------------------ | --------------------- |
| Linear algebra      | Kernel, image, rank, quotient identities   | Essential             |
| Pencil theory       | Block criterion and rank equivalences      | Essential             |
| Lifting             | Exact sequences and completion theorem     | Highest next priority |
| Geometry            | Grassmannian and incidence statements      | Later                 |
| Polynomial matrices | Bézout certificate and generalized inverse | High priority         |

The lift-completion theorem from Section 8 is an excellent candidate for the next substantial Lean development.

It is a finite-dimensional linear algebra theorem and does not require formalising the full algebraic geometry.

I would also formalise the direct original-pencil certificate, because it provides an independent verification route for the complexity argument.

## 28. Computational experiments: the methodology should become exact and adversarial

The project has already benefited from large-scale random testing.

However, random testing alone is not adequate for the next stage.

The central unresolved issues concern exceptional configurations, which are often rare under generic random sampling.

### 28.1 Exact rational arithmetic

Use matrices over

\\[ \mathbb Q \\]

whenever possible.

For spectral computations, use exact polynomial arithmetic over \\(\mathbb Q[\lambda]\\).

For eigenvalue structures, use exact algebraic extensions where necessary.

Avoid floating-point rank decisions in the verification pipeline.

A numerical matrix that appears to have rank three may have exact rank two.

Such errors are particularly dangerous when testing exact-rank strata.

### 28.2 Build an adversarial test suite

I recommend systematically generating the following families.

Family A: diagonal operators

\\[ A=\operatorname{diag}(\lambda_1,\ldots,\lambda_n). \\]

Test:

- all distinct eigenvalues;
- repeated eigenvalues;
- high-dimensional eigenspaces;
- eigenspaces with different intersections with \\(K_0\\).

Family B: Jordan operators

Use blocks of sizes

\\[ 2,\quad 3,\quad 2+2,\quad 3+2. \\]

These test chain-lifting conditions.

Family C: invariant and non-invariant \\(K_0\\)

Test both

\\[ A(K_0)\subseteq K_0 \\]

and

\\[ A(K_0)\not\subseteq K_0. \\]

This is especially important because the second case is the general one.

Family D: lift obstructions

Construct examples with:

\\[ d'\_C=0, \\]

\\[ d'\_C>0, \\]

and cases where

\\[ q-\omega=d'\_C \\]

or

\\[ q-\omega>d'\_C. \\]

Also test prescribed compressed pairs outside \\(\operatorname{im}\Psi\\).

Family E: spectral obstructions

Construct cases where:

- a compressed pair is compatible but spectrally bad;
- the generic point is good;
- the generic point is bad;
- the good locus is nonempty only after moving to another component.

These are much more informative than generic random instances.

### 28.3 Use independent verification

For every constructed witness \\(L\\), verify:

\\[ \operatorname{rank}L=q, \\]

and, if required,

\\[ \operatorname{rank}[C;L]=\operatorname{rank}C+q. \\]

Then check (5a) directly.

For (5b), calculate the maximal minors of the original pencil

\\[ Q(\lambda) = \begin{bmatrix} \lambda L-LA\\\CA\\\C \end{bmatrix} \\]

and compute their gcd.

Do not verify (5b) solely through the same compressed calculation that generated the candidate.

Independent verification reduces the risk of a shared implementation error.

### 28.4 Preserve all counterexamples

Maintain a permanent registry of:

1. Refuted closed-form formulas.
2. Non-monotonicity examples.
3. Reducible-stratum examples.
4. Invalid lift-completion constructions.
5. Spectral obstructions.
6. Incorrect quotient-space substitutions.
7. Rank identities that require additional hypotheses.

Every new theorem should be tested against this registry.

# Part XII. The strongest research direction

## 29. Three possible publication directions

I see three coherent papers.

### Paper A. Low-codimension geometry

Low-Codimension Incidence Geometry in Minimal-Order Functional Observer Problems

The central results would be:

1. Exact compression to \\((H,H_A)\\).
2. Universal block criterion.
3. Exact Grassmannian fibre theorem.
4. Complete \\(c=1\\) classification.
5. Complete \\(c=2\\) classification.
6. Irreducibility and component bounds.
7. Exact lift-completion theorem.

This is the most natural first paper if the \\(c=2\\) lifting and component arguments are completed.

### Paper B. Polynomial certificates and complexity

Polynomial Generalized-Inverse Certificates for Functional Observer Feasibility

The central results would be:

1. Constant-rank characterization through maximal minors.
2. Explicit Bézout-adjugate construction.
3. Degree bound \\(2s-2\\).
4. Direct original-pencil certificate.
5. Existential-real formulation.
6. Exact fixed-candidate spectral testing.

This paper has a particularly clear independent mathematical contribution.

It does not depend on the irreducibility of the \\(c=2\\) strata.

### Paper C. General incidence geometry

Invariant-Subspace Incidence Varieties and Component Bounds in Functional Observer Design

The central results would be:

1. General \\((t,u)\\)-stratification.
2. Quiver-Grassmannian interpretation.
3. Reducibility criteria.
4. Component bounds in selected dimensions.
5. Degeneration and orbit-closure analysis.

This is the most ambitious direction and should probably come later.

### 29.1 Which combination is best?

My preference is to complete Papers A and B as independent but complementary contributions.

If their results fit together naturally, they can be combined.

However, I would not force them into one manuscript if doing so obscures the main theorem.

The geometric contribution and the complexity contribution are logically independent.

A successful paper should have one central theorem, not several partially completed research programmes.

## 30. Recommended research priorities

Here is the order I would follow.

1\. Prove the exact lift theorem

Highest priority

Establish the image condition, the fixed-row compatibility, the kernel dimension criterion, and a constructive lifting algorithm.

2\. Complete the \\(c=2\\) classification

High priority

Verify exhaustiveness, mutual exclusivity, irreducibility, and nonempty fibres.

3\. Transfer the component bound to lifted spaces

High priority

Prove the relevant affine-bundle and open-fibre properties. Do not infer this from the base count alone.

4\. Finish the \\(\exists\mathbb R\\) theorem

Independent result

Use the direct original-pencil certificate and provide the complete rational-input encoding.

5\. Audit the eleven \\(c=3\\) strata

Exploratory

Begin with \\(S\_{2,3}\\), then proceed through the other strata.

6\. Investigate general component bounds

Long-term

Use representation theory and quiver-Grassmannian methods.

7\. Search for hardness reductions

Long-term

First understand the fixed-\\(c=2\\) problem; do not assume general rank hardness transfers.

# Part XIII. Final answers to the nine questions

## 31. Question 1 — Is the three-compression framework sound?

Yes. It is the correct organising structure, provided the affine lift fibre is retained.

The precise formulation should be

\\[ \boxed{ L \longrightarrow (H,H_A;\text{lift fibre}) \longrightarrow Z \longrightarrow \text{lifted incidence variety}. } \\]

The first compression is exact for the rank conditions but is not injective.

The assumptions on \\(C,L_0\\), full row rank, and independence modulo \\(\operatorname{row}C\\) must be stated explicitly.

The coefficient field should be \\(\mathbb C\\) for the algebraic-geometric results and a specified rational subfield for the complexity results.

## 32. Question 2 — Is the exact-sequence lift criterion correct?

Yes, with a stronger formulation.

The exact sequence

\\[ 0\longrightarrow E_C \longrightarrow \mathcal X^\*/\operatorname{row}C \longrightarrow K_0^\* \longrightarrow0 \\]

is correct.

The calculation

\\[ gAN=bCA^2N \\]

is correct.

The dimension formula

\\[ d'\_C=d_C-\operatorname{rank}\Gamma \\]

is correct.

Most importantly, the exact pair-preserving completion criterion is

\\[ \boxed{ d'\_C\ge \dim\ker Z\_{\mathrm{pair}}, } \\]

where \\(Z\_{\mathrm{pair}}\\) maps the coefficient space of all \\(q\\) prescribed rows into the space of compressed pairs.

Under (5a),

\\[ \operatorname{rank}Z\_{\mathrm{pair}}=\omega, \\]

so this becomes

\\[ \boxed{q-\omega\le d'\_C.} \\]

This is a constructive necessary-and-sufficient theorem for completion, assuming the prescribed pairs are in the image of the pair map and the fixed rows satisfy the independence hypotheses.

I regard this as an important theorem to develop and formalise immediately.

## 33. Question 3 — Is the \\(c=2\\) algorithm correct?

The mathematical architecture is correct, but the complete algorithm has not yet been proved.

The six strata provide the geometric enumeration.

The affine lift theorem provides the completion step.

The gcd or polynomial generalized-inverse test provides the spectral step.

What remains is to prove that the resulting lifted families have the required nonempty fibres and that the spectral-good locus is correctly tested on every irreducible component.

I recommend developing the algorithm using both geometric and direct algebraic formulations.

## 34. Question 4 — Are the eleven \\(c=3\\) strata irreducible?

This remains open.

The eleven-stratum classification should first be written in unambiguous Jordan-type notation.

Then each stratum should receive its own irreducibility proof.

The highest-priority test is

\\[ S\_{2,3}. \\]

The proposed component bound should remain suspended until all eleven cases have been checked.

## 35. Question 5 — Is there a general component bound?

Not yet.

The general finite \\((t,u)\\)-stratification is established at the structural level.

The relative Grassmannian description is also established under its stated hypotheses.

The label count

\\[ p(c)n^c \\]

is not a component bound.

Quiver-Grassmannian theory is a promising direction, but the honest current result is a conditional component theorem in terms of the component counts of the base strata.

## 36. Question 6 — Does the polynomial certificate prove \\(\exists\mathbb R\\) membership?

Yes, under a rational-input model.

The bounded-degree certificate provides a finite existential formulation.

I recommend proving the result using the original pencil

\\[ Q(\lambda)= \begin{bmatrix} \lambda L-LA\\\CA\\\C \end{bmatrix} \\]

as well as the compressed pencil.

The original-pencil approach can avoid computing \\(N\\) and the quotient \\(K_0\\) in the complexity proof.

The resulting theorem is

\\[ \boxed{\mathrm{DEC}(q)\in\exists\mathbb R.} \\]

The minimum-order decision problem also belongs to \\(\exists\mathbb R\\).

Hardness remains open.

## 37. Question 7 — Which references are most useful?

The highest-priority subjects are:

1. Smith normal forms and polynomial matrix theory.
2. Kronecker canonical forms and minimal indices.
3. Determinantal varieties and degeneracy loci.
4. Invariant-subspace varieties and Springer fibres.
5. Quiver Grassmannians and representation varieties.
6. Existential-real complexity and structured rank feasibility.
7. Minimal-order functional observer theory.

I would avoid adding references merely to make the bibliography extensive. Every reference should support a specific theorem, method, or comparison with previous work.

## 38. Question 8 — What should be the next step?

My recommendation is:

\\[ \boxed{ \text{Lift theorem} \\;\longrightarrow\\; c=2\text{ feasibility} \\;\longrightarrow\\; \text{component theorem}. } \\]

Develop the \\(\exists\mathbb R\\) result in parallel.

Only after these results should the project invest heavily in \\(c=3\\) and general component bounds.

## 39. Question 9 — What should be formalised?

Formalise now:

- the exact-sequence construction;
- the pair-map kernel;
- the lift-completion theorem;
- the universal block criterion;
- the fibre theorem;
- the Bézout-adjugate identity;
- the original-pencil polynomial certificate.

Postpone:

- general component bounds;
- \\(c=3\\) irreducibility;
- polynomial-time solvability;
- hardness reductions;
- generic-feasibility assertions that depend on unproved irreducibility.

# Part XIV. The decisive next mathematical task

## 40. A concrete theorem that should become the next research deliverable

I would formulate the next research task as follows.

Recommended next theorem

## Exact lifted feasibility theorem

Given \\(A,C,L_0\\) and a prescribed compressed pair \\((H,H_A)\\), establish necessary and sufficient conditions for the existence of an actual matrix \\(L\\) satisfying:

1. The prescribed rows \\(L_0\\) are unchanged.
2. \\(LN=H\\).
3. \\(LAN=H_A\\).
4. The required full-row-rank and independence conditions hold.
5. Conditions (5a) and (5b) hold.

The theorem should give a constructive procedure for recovering \\(L\\).

I would split it into three propositions.

### Proposition A. Pair realizability

Define

\\[ \Psi: \mathcal X^\*/\operatorname{row}C \longrightarrow K_0^\*\oplus K_0^\* \\]

by

\\[ \Psi(\bar g)=(gN,gAN). \\]

The prescribed compressed pair must belong row by row to

\\[ \operatorname{im}\Psi. \\]

This is an exact linear compatibility condition.

### Proposition B. Independence completion

Assume the fixed rows are independent modulo \\(\operatorname{row}C\\).

Let \\(Z\_{\mathrm{pair}}\\) be the prescribed compressed-pair map on the coefficient space of all \\(q\\) rows.

Then the prescribed pair has an independent lift if and only if

\\[ \boxed{ \dim\ker\Psi\ge\dim\ker Z\_{\mathrm{pair}}. } \\]

Under (5a), this reduces to

\\[ \boxed{d'\_C\ge q-\omega.} \\]

### Proposition C. Spectral feasibility

Once an independent lift has been constructed, impose

\\[ \operatorname{rank} \begin{bmatrix} \lambda L-LA\\\CA\\\C \end{bmatrix} = \operatorname{rank} \begin{bmatrix} L\\\CA\\\C \end{bmatrix} \qquad\forall\lambda. \\]

Equivalently, use the polynomial generalized-inverse certificate with the appropriate normal-rank condition.

These propositions would connect the original observer problem, the compressed geometry, and the complexity certificate in a mathematically complete manner.

# Part XV. Final verdict

# Research assessment

The project is mathematically substantial and has a viable publication direction.

The strongest established contributions are:

1. Exact reduction to the compressed pencil.
2. Universal block criterion.
3. Exact Grassmannian fibre theorem.
4. General finite incidence stratification.
5. Low-codimension classification framework.
6. Polynomial generalized-inverse certificate.
7. Formal verification of several fundamental algebraic identities.

The most important unfinished contribution is the complete connection between compressed feasibility and actual observer feasibility.

I would make three final observations.

First: the lifting issue is now much more structured than it initially appeared.

The exact pair map

\\[ \Psi(\bar g)=(gN,gAN) \\]

provides the correct language. The completion theorem can be expressed as an injective extension problem on the kernel of the prescribed compressed-pair map. This is a meaningful advance over an informal count of invisible directions.

Second: the complexity result should not wait for the geometric classification.

The original-pencil certificate offers a direct route to an \\(\exists\mathbb R\\) upper bound. This result can be completed independently of the \\(c=2\\) and \\(c=3\\) irreducibility questions.

Third: the project should distinguish three kinds of results in every future report.

- Theorems proved completely.
- Theorems proved under additional hypotheses.
- Conjectures and computationally supported observations.

This discipline is especially important because the project has already discovered several counterexamples to attractive but overly general claims.

My final recommendation is to concentrate the next research phase on two deliverables:

1. A rigorous, constructive pair-preserving lift-completion theorem with fixed \\(L_0\\).
2. A complete \\(c=2\\) lifted feasibility and component theorem.

In parallel, finish the direct-pencil \\(\exists\mathbb R\\) membership proof.

These three results would provide a coherent mathematical contribution even if the ultimate NP-hardness question remains unresolved.

The project should not be judged solely by whether it eventually proves NP-hardness. A rigorous geometric classification, an exact lifting theorem, and a polynomial-size existential certificate would already constitute a substantial contribution to the mathematical theory and computational study of minimal-order functional observers.