# Mathematical assessment of Report 60

This report makes substantial progress: it supplies a useful forced-plane feasibility criterion, repairs the invariant-subspace argument using cyclic vectors, gives an explicit \\(c=3\\) classification, and reduces the remaining general-\\(c\\) geometry to the rank strata

\\[ B\_{u,v} = \left\\{ U\in\operatorname{Gr}(u,K_0): \dim(U\cap A^{-1}U)=v \right\\}. \\]

My overall verdict is that the cyclic-vector idea is sound after one important correction; the proposed \\(c=3\\) list is not yet correct as written; and the general rank strata are not always irreducible, but they admit a uniform, if crude, algebraic-geometric component bound.

The most useful new result I can give is a direct coordinate description of \\(B\_{u,v}\\) as an exact-rank locus of a matrix whose entries are quadratic polynomials. This both answers the irreducibility question negatively and provides a general component bound independent of \\(c\\).

Here is the detailed adjudication.

## 1. The forced-plane \\(c=2,\ q=3\\) criterion

### 1.1 The row-space criterion

The report assumes that the two-dimensional annihilator of the forced plane is

\\[ \operatorname{Ann}(V)=\langle h_0,u_1\rangle, \qquad h_0=L_0N_K, \\]

and writes each bottom row of \\(H\\) as

\\[ h_i=a_i h_0+b_i u_1. \\]

The condition \\(b_i=0\\) is a linear condition on the parameter vector

\\[ x_i=(a_i,b_i,c_i)^{\mathsf T}, \\]

where \\(c_i\\) denotes any additional free parameter entering the corresponding row of \\(H_A\\).

Suppose the admissibility equations are homogeneous:

\\[ \mathrm{Des}\_i x_i=0. \\]

Then the solution space is

\\[ \ker(\mathrm{Des}\_i). \\]

Let \\(e_b^{\mathsf T}\\) denote the coordinate functional extracting \\(b_i\\). The assertion that \\(b_i\\) is forced to zero means

\\[ e_b^{\mathsf T}x=0 \qquad\forall x\in\ker(\mathrm{Des}\_i). \\]

By the fundamental theorem of linear algebra,

\\[ (\ker \mathrm{Des}\_i)^\perp = \operatorname{rowspace}(\mathrm{Des}\_i). \\]

Consequently,

\\[ \boxed{ b_i\text{ is forced to }0 \iff e_b^{\mathsf T}\in\operatorname{rowspace}(\mathrm{Des}\_i). } \\]

So the report's criterion is exactly right for homogeneous admissibility equations.

There is one qualification worth making explicit. If the equations are instead affine,

\\[ \mathrm{Des}\_i x_i=d_i, \\]

then row-space membership only says that \\(b_i\\) is constant over the solution set. It does not say that the constant is zero. In that case, assuming the system is consistent, the exact criterion is

\\[ e_b^{\mathsf T}\in\operatorname{rowspace}(\mathrm{Des}\_i) \quad\text{and}\quad e_b^{\mathsf T}x_i^{(0)}=0 \\]

for one particular solution \\(x_i^{(0)}\\).

The report should state explicitly that the Des equations are homogeneous, or include this affine correction.

### 1.2 Why two forced bottom rows imply infeasibility

If both bottom rows satisfy \\(b_i=0\\), then

\\[ h_i=a_i h_0. \\]

Thus all three rows of \\(H\\) are multiples of \\(h_0\\):

\\[ H= \begin{bmatrix} h_0\\\ a_1h_0\\\ a_2h_0 \end{bmatrix}. \\]

Therefore

\\[ \operatorname{rank}H\leq1. \\]

But the target is

\\[ \omega=2. \\]

This is a contradiction. Hence, under the stated homogeneous-equation interpretation,

\\[ \boxed{ \text{if both bottom rows force }b_i=0,\text{ the }q=3,\omega=2 \text{ layer is infeasible.} } \\]

This is a genuine structural obstruction. It is stronger than the observation that 600 random choices failed.

### 1.3 Assessment of instances 10, 16, and 21

The conclusions in the report are logically consistent:

- Instance 10 has a displayed witness and is reported to satisfy the original conditions.
- Instances 16 and 21 are infeasible in this \\(q=3\\) layer if both bottom-row \\(b_i\\)'s are forced to zero.

However, I cannot independently verify the numerical instance classifications from this report alone: the matrices defining \\(\mathrm{Des}\_i\\), the original input data for instances 10/16/21, and the precise admissibility equations are not displayed.

Recommendation: make the row-space test part of the algorithm, and have the program output a certificate. For each bottom row, it should report either:

- a row-space representation\
  \\[\
  e_b^{\mathsf T}=\alpha^{\mathsf T}\mathrm{Des}\_i,\
  \\]\
  proving \\(b_i=0\\) for every admissible solution; or
- a vector\
  \\[\
  x_i\in\ker(\mathrm{Des}\_i),\qquad b_i\ne0,\
  \\]\
  proving that \\(b_i\\) is not forced to zero.

This gives a short exact certificate in either direction.

60_deliverables_and_rank_strata.md

## 2. The cyclic-vector repair: essentially correct, but the parameter space needs one more constraint

This is a real improvement over the earlier chain-lifting argument. It avoids taking a quotient by choices of Jordan-chain bases and uses a morphism from a parameter space directly to the Grassmannian.

There is, however, a significant issue in the stated definition of \\(U\_\lambda\\).

### 2.1 The issue: \\(K_0\\) need not be \\(A\\)-invariant

The report defines

\\[ T=A-\lambda I \\]

and

\\[ U\_\lambda = \\{x\in K_0:T^cx=0,\ T^{c-1}x\ne0\\}. \\]

It then maps

\\[ x\longmapsto \operatorname{span}\\{x,Tx,\ldots,T^{c-1}x\\} \\]

into \\(\operatorname{Gr}(c,K_0)\\).

But the condition \\(x\in K_0\\) does not imply

\\[ Tx,T^2x,\ldots,T^{c-1}x\in K_0. \\]

In the project, \\(K_0=\ker[C;CA]\\) is not assumed to be \\(A\\)-invariant. Thus the displayed map need not even take values in \\(\operatorname{Gr}(c,K_0)\\).

This is the one essential correction to the cyclic-vector proof.

### 2.2 Corrected cyclic-vector parameter space

For a Jordan block of length \\(m\\) and eigenvalue \\(\lambda\\), define

\\[ T\_\lambda=A-\lambda I. \\]

The appropriate linear subspace is

\\[ \mathcal K\_{\lambda,m} = \left\\{ x\in\mathbb C^n: T\_\lambda^m x=0,\quad T\_\lambda^j x\in K_0\quad(0\leq j\leq m-1) \right\\}. \\]

This is a linear subspace: all the displayed conditions are linear in \\(x\\).

Now define

\\[ \boxed{ \mathcal U\_{\lambda,m} = \mathcal K\_{\lambda,m} \setminus \ker T\_\lambda^{m-1}. } \\]

Equivalently,

\\[ \mathcal U\_{\lambda,m} = \left\\{ x: T\_\lambda^m x=0,\  T\_\lambda^j x\in K_0\ (0\leq j\<m),\ T\_\lambda^{m-1}x\ne0 \right\\}. \\]

This is a Zariski-open subset of the linear space \\(\mathcal K\_{\lambda,m}\\), and hence is irreducible whenever nonempty.

The corrected map is

\\[ \Phi\_{\lambda,m}: \mathcal U\_{\lambda,m}\longrightarrow \operatorname{Gr}(m,K_0), \\]

\\[ x\longmapsto \operatorname{span}\\{x,T\_\lambda x,\ldots,T\_\lambda^{m-1}x\\}. \\]

It is a morphism because the Plücker coordinates of the chain span are polynomial in \\(x\\).

### 2.3 Why the image is exactly the single-block stratum

The report's independence argument is correct.

If

\\[ T\_\lambda^m x=0,\qquad T\_\lambda^{m-1}x\ne0, \\]

then the vectors

\\[ x,T\_\lambda x,\ldots,T\_\lambda^{m-1}x \\]

are linearly independent.

Indeed, suppose

\\[ a_0x+a_1T\_\lambda x+\cdots+a\_{m-1}T\_\lambda^{m-1}x=0. \\]

Let \\(j\\) be the smallest index with \\(a_j\ne0\\). Apply \\(T\_\lambda^{m-1-j}\\). All terms of index greater than \\(j\\) vanish, and the result is

\\[ a_jT\_\lambda^{m-1}x=0, \\]

a contradiction.

Since all chain vectors lie in \\(K_0\\), their span is an \\(m\\)-dimensional subspace of \\(K_0\\). It is invariant under \\(A\\), and the restriction of \\(A\\) has one Jordan block of size \\(m\\) with eigenvalue \\(\lambda\\).

Conversely, if \\(V\subseteq K_0\\) is invariant and its restriction \\(A|\_V\\) consists of one Jordan block of size \\(m\\), a cyclic generator \\(x\in V\\) satisfies exactly these conditions.

Thus the image is precisely the single-block stratum.

Since the image of an irreducible variety under a morphism is irreducible (as a topological subspace), the single-block stratum is irreducible or empty.

### 2.4 Multiple blocks: the argument also works after the correction

Suppose a fixed eigenvalue-labelled Jordan type is

\\[ \tau=\\{(\lambda_i,m_i)\\}\_{i=1}^{\ell}, \qquad \sum_i m_i=c. \\]

Use the corrected product parameter space

\\[ \Omega\_\tau= \left\\{ (x_1,\ldots,x\_\ell)\in \prod\_{i=1}^{\ell}\mathcal U\_{\lambda_i,m_i}: \operatorname{rank} \big[ T\_{\lambda_1}^jx_1\ \cdots\ T\_{\lambda\_\ell}^jx\_\ell \big]=c \right\\}. \\]

The rank-\\(c\\) condition is open. Thus \\(\Omega\_\tau\\) is an open subset of an irreducible product, and is irreducible or empty.

The map sending the tuple to the sum of the chain spans is a morphism. Every invariant subspace of Jordan type \\(\tau\\) admits a Jordan basis and therefore has a preimage under this map.

Consequently, the fixed-type invariant stratum is irreducible or empty.

The important point is that the cyclic-vector method really does eliminate the need to control the quotient from chain bases to subspaces. The map need not be injective. Surjectivity onto the fixed-type stratum and irreducibility of the source are sufficient.

### 2.5 Component bound

Let \\(s\\) be the number of distinct eigenvalues of \\(A\\). Every invariant \\(c\\)-plane has a Jordan type obtained by:

- choosing a partition of \\(c\\);
- assigning eigenvalues to its blocks.

Therefore, once the corrected parameter spaces are used, the number of irreducible invariant strata is bounded by the number of such labels:

\\[ \boxed{ N\_{\mathrm{inv}}(c) \leq \sum\_{\lambda\vdash c}s^{b(\lambda)} \leq p(c)s^c. } \\]

Here \\(b(\lambda)\\) is the number of parts of the partition, and \\(p(c)\\) is the partition number.

This is a valid upper bound, although it may overcount because different block assignments or parameter descriptions can yield the same stratum.



Correct after repair

&#x20;The cyclic-vector argument proves the invariant-part component bound once the requirement that every chain vector lie in \\(K_0\\) is added.



60_deliverables_and_rank_strata.md

## 3. The \\(c=3\\) classification: the six invariant types are right, but several defining conditions are missing

The proposed classification by

\\[ t=\dim(V\cap A^{-1}V) \\]

is a good organizing principle. The range

\\[ t\in\\{0,1,2,3\\} \\]

is exhaustive, and the six Jordan types for \\(t=3\\) are the correct six possibilities for a three-dimensional invariant space.

However, I would not certify the eleven strata exactly as written. Some conditions need to be added, and the irreducibility argument for the non-invariant strata is incomplete.

### 3.1 The dimension bound \\(u\leq3\\) is correct

For every admissible \\(V\\),

\\[ W=V\cap A^{-1}V \\]

satisfies

\\[ W\subseteq V,\qquad A(W)\subseteq V. \\]

Therefore

\\[ U=W+A(W)\subseteq V. \\]

Since \\(\dim V=3\\),

\\[ \boxed{u=\dim U\leq3.} \\]

Also, since \\(\dim W=t\\),

\\[ u=\dim(W+A(W))\leq2t. \\]

Thus the general range is

\\[ \boxed{t\leq u\leq\min(2t,3).} \\]

There is no \\(u=4\\) case in the actual \\(c=3\\) problem. This is a direct consequence of the definition of \\(W\\), not an additional spectral assumption.

### 3.2 The invariant \\(t=3\\) cases: correct after adding the nilpotence equations

The six Jordan types are:

| Type  | Jordan structure                                   |
| ----- | -------------------------------------------------- |
| (3a)  | Three distinct eigenvalues, all blocks of size one |
| (3b)  | One eigenvalue, partition \\(1+1+1\\)              |
| (3b′) | Two eigenvalues, partitions \\(1+1\\) and \\(1\\)  |
| (3c)  | One eigenvalue, partition \\(2+1\\)                |
| (3c′) | Two eigenvalues, partitions \\(2\\) and \\(1\\)    |
| (3d)  | One eigenvalue, partition \\(3\\)                  |

These are exhaustive.

But the chain descriptions in the report must include the vanishing conditions that specify the exact block lengths.

For \\(T\_\lambda=A-\lambda I\\):

- A block of size two requires\
  \\[\
  T\_\lambda^2x=0,\qquad T\_\lambda x\ne0.\
  \\]
- A block of size three requires\
  \\[\
  T\_\lambda^3x=0,\qquad T\_\lambda^2x\ne0.\
  \\]

Thus rows (3c) and (3c′) need \\(T\_\lambda^2u=0\\), while row (3d) needs \\(T\_\lambda^3u=0\\).

For (3c), the eigenline \\(\ell\_\lambda\\) must also be independent of the two-dimensional chain span. For (3c′), the eigenline at \\(\mu\ne\lambda\\) must be independent of the chain span at \\(\lambda\\).

With these conditions, the invariant classification is correct and its fixed-type irreducibility follows from the corrected cyclic-vector argument in Section 2.

### 3.3 The \\(t=2\\) cases

There are two possibilities.

Case (2a): \\(t=2,u=3\\).

Here

\\[ U=W+A(W) \\]

has dimension three. Since \\(U\subseteq V\\) and \\(\dim V=3\\), necessarily

\\[ V=U. \\]

But the condition \\(V=U\\) alone does not guarantee that

\\[ W=V\cap A^{-1}V \\]

has dimension exactly two. The exact condition is

\\[ \dim(U\cap A^{-1}U)=2. \\]

Equivalently, the map

\\[ A|\_U:U\longrightarrow\mathbb C^n/U \\]

must have rank one.

This is an important condition to include in the stratum definition.

A convenient parameterization is to begin with

\\[ U\in B\_{3,2}. \\]

Then \\(W=U\cap A^{-1}U\\) is uniquely determined. To ensure that \\(U=W+A(W)\\), impose

\\[ A(W)\not\subseteq W. \\]

This is an open condition within the appropriate incidence locus.

Case (2b): \\(t=2,u=2\\).

Here

\\[ U=W,\qquad A(W)\subseteq W. \\]

The candidate is

\\[ V=W\oplus\langle x\rangle. \\]

The exact condition for \\(t=2\\) is

\\[ \boxed{Ax\notin V.} \\]

Indeed, \\(A(W)\subseteq W\\), so every vector of \\(W\\) belongs to \\(V\cap A^{-1}V\\). If \\(Ax\notin V\\), no vector with a nonzero \\(x\\)-component can belong to this intersection. Thus

\\[ V\cap A^{-1}V=W. \\]

This part of the report is correct.

### 3.4 The \\(t=1\\) cases

Again there are two possibilities.

Case (1a): \\(AL\subseteq L\\).

Here \\(W=L\\) is an invariant line and

\\[ U=L. \\]

Write

\\[ V=L\oplus U', \\]

where \\(U'\\) is two-dimensional in the quotient \\(K_0/L\\).

Since \\(L\\) is invariant, \\(A\\) induces an operator \\(\bar A\\) on the ambient quotient \\(\mathbb C^n/L\\).

The exact condition is

\\[ \boxed{ U'\cap\bar A^{-1}U'=\\{0\\}. } \\]

This is correct. It ensures that no additional vector outside \\(L\\) belongs to \\(V\cap A^{-1}V\\).

The notation must make clear that \\(\bar A^{-1}U'\\) is taken in the ambient quotient \\(\mathbb C^n/L\\), not automatically in \\(K_0/L\\). The latter need not be invariant under the induced operator.

Case (1b): \\(AL\not\subseteq L\\).

Now

\\[ U=L+AL,\qquad \dim U=2. \\]

Since \\(U\subseteq V\\) and \\(\dim V=3\\), write

\\[ V=U\oplus\langle x\rangle. \\]

The report requires \\(Ax\\) and \\(A^2L\\) to be independent modulo \\(V\\). This is correct and, importantly, is not an unnecessary strengthening.

To see why, choose a nonzero \\(l\in L\\). The vectors

\\[ l,\quad Al,\quad x \\]

span \\(V\\).

For a general vector

\\[ v=a l+b Al+c x, \\]

we have

\\[ Av=aAl+bA^2l+cAx. \\]

The term \\(aAl\\) already belongs to \\(V\\). Therefore, modulo \\(V\\), the image is

\\[ b(A^2l+V)+c(Ax+V). \\]

Consequently,

\\[ V\cap A^{-1}V=L \\]

if and only if the two vectors

\\[ A^2l+V,\qquad Ax+V \\]

are linearly independent in \\(\mathbb C^n/V\\).

This is precisely the condition in the report.

It also explains why the non-invariant \\(t=1\\) case requires more than \\(Ax\notin V\\): the vector \\(Al\\) is itself in \\(V\\), and its image \\(A^2l\\) must also be controlled.

### 3.5 The \\(t=0\\) case

The condition is simply

\\[ V\cap A^{-1}V=\\{0\\}. \\]

This is an open rank condition on the Grassmannian \\(\operatorname{Gr}(3,K_0)\\). Its locus is irreducible if nonempty.

### 3.6 Verdict on the eleven strata

Correct the definitions before claiming the theorem

The eleven-way organization is exhaustive at the level of the possible values of \\(t,u\\) and the Jordan types of invariant three-planes. But I recommend revising the table as follows:

| Strata            | Verdict              | Required adjustment                                                   |
| ----------------- | -------------------- | --------------------------------------------------------------------- |
| (3a), (3b), (3b′) | Correct              | State the direct-sum and independence conditions explicitly           |
| (3c), (3c′)       | Correct after repair | Add \\(T\_\lambda^2u=0\\), \\(T\_\lambda u\ne0\\)                     |
| (3d)              | Correct after repair | Add \\(T\_\lambda^3u=0\\), \\(T\_\lambda^2u\ne0\\)                    |
| (2a)              | Incomplete           | Require \\(\dim(U\cap A^{-1}U)=2\\), equivalently rank one on \\(U\\) |
| (2b)              | Correct              | Retain \\(Ax\notin V\\)                                               |
| (1a)              | Correct              | Specify the ambient quotient for \\(\bar A\\)                         |
| (1b)              | Correct              | Retain independence of \\(A^2L\\) and \\(Ax\\) modulo \\(V\\)         |
| (0)               | Correct              | State the open rank condition                                         |

The main remaining issue is irreducibility. The invariant strata are covered by the cyclic-vector theorem. The other strata should be analyzed through the \\(B\_{u,v}\\) reduction below. In particular, (2a) is not automatically irreducible merely because it is an open subset of some Grassmannian.

60_deliverables_and_rank_strata.md

## 4. The general rank strata \\(B\_{u,v}\\): they are not always irreducible

This is the central general-\\(c\\) question in Report 60.

The answer to the first question is unequivocal:

\\[ \boxed{B\_{u,v}\text{ is not always irreducible.}} \\]

But there is a useful general structure and a uniform component bound.

### 4.1 Reinterpretation as a vector-bundle rank locus

Let

\\[ \mathcal X=\mathbb C^n,\qquad K=K_0,\qquad \dim K=k. \\]

On

\\[ G=\operatorname{Gr}(u,K), \\]

let \\(\mathcal S\\) denote the tautological rank-\\(u\\) subbundle.

The ambient operator \\(A\\) induces a bundle morphism

\\[ \varphi:\mathcal S\longrightarrow (\mathcal X\otimes\mathcal O_G)/\mathcal S, \\]

whose fibre at \\(U\in G\\) is

\\[ \varphi_U:U\longrightarrow\mathcal X/U, \qquad x\longmapsto Ax+U. \\]

Its kernel is

\\[ \ker\varphi_U = \\{x\in U:Ax\in U\\} = U\cap A^{-1}U. \\]

Therefore

\\[ \dim\ker\varphi_U=v \iff \operatorname{rank}\varphi_U=u-v. \\]

Hence

\\[ \boxed{ B\_{u,v} = \\{U\in G:\operatorname{rank}\varphi_U=u-v\\}. } \\]

This is the cleanest geometric formulation.

Define the closed degeneracy loci

\\[ D_r= \\{U\in G:\operatorname{rank}\varphi_U\leq r\\}. \\]

Then

\\[ \boxed{ B\_{u,v}=D\_{u-v}\setminus D\_{u-v-1}. } \\]

Thus \\(B\_{u,v}\\) is locally closed. It is an exact-rank stratum of a vector-bundle morphism.

This places the problem in the standard theory of degeneracy loci and determinantal varieties. Fulton’s treatment of degeneracy loci is directly relevant to this formulation; the Thom–Porteous theory describes their cycle classes under suitable hypotheses, although it does not by itself establish irreducibility.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://ideas.repec.org\&sz=32)

RePEc+1



### 4.2 A simple counterexample to universal irreducibility

Take

\\[ K=\mathcal X=\mathbb C^2, \qquad A= \begin{bmatrix} 0&0\\\ 0&1 \end{bmatrix}, \qquad u=1,\quad v=1. \\]

Then \\(B\_{1,1}\\) consists of the one-dimensional subspaces \\(U\\) satisfying

\\[ AU\subseteq U. \\]

These are exactly the two eigenspaces:

\\[ U=\langle e_1\rangle \quad\text{or}\quad U=\langle e_2\rangle. \\]

Therefore

\\[ \boxed{ B\_{1,1} = \\{[e_1],[e_2]\\}\subseteq\mathbb P^1. } \\]

It is the disjoint union of two points, hence reducible.

More generally, for \\(u=1,v=1\\), the stratum is the union of the projectivized eigenspaces of \\(A\\) that lie in \\(K_0\\). If there are multiple distinct eigenvalues with nonzero eigenspaces in \\(K_0\\), this union is reducible.

So a theorem asserting that all \\(B\_{u,v}\\) are irreducible is false even in the simplest case.

### 4.3 A direct coordinate description

We can go further and obtain a uniform bound on the number of components.

Choose a vector-space complement

\\[ \mathcal X=K\oplus K'. \\]

Consider a standard affine chart of \\(\operatorname{Gr}(u,K)\\). Choose a splitting

\\[ K=E\oplus F, \qquad \dim E=u,\quad \dim F=k-u. \\]

Every subspace in this chart is the graph of a matrix

\\[ X:E\longrightarrow F. \\]

In coordinates, a basis matrix for \\(U\\) is

\\[ G(X)= \begin{bmatrix} I\\\X\\\0 \end{bmatrix}, \\]

where the last block corresponds to \\(K'\\).

Write \\(A\\) in blocks relative to

\\[ \mathcal X=E\oplus F\oplus K'. \\]

Then

\\[ AG(X)= \begin{bmatrix} A\_{11}+A\_{12}X\\\ A\_{21}+A\_{22}X\\\ A\_{31}+A\_{32}X \end{bmatrix}. \\]

The quotient \\(\mathcal X/U\\) can be represented using the coordinates

\\[ (y_F-Xy_E,\ y\_{K'}). \\]

Consequently, the matrix representing

\\[ \varphi_U:U\to\mathcal X/U \\]

is

\\[ \boxed{ F_A(X)= \begin{bmatrix} A\_{21}+A\_{22}X-XA\_{11}-XA\_{12}X\\\ A\_{31}+A\_{32}X \end{bmatrix}. } \\]

This is an \\((n-u)\times u\\) matrix whose entries are polynomials of degree at most two in the \\(u(k-u)\\) chart coordinates.

The key identity is

\\[ \boxed{ \operatorname{rank}F_A(X)=u-\dim(U\cap A^{-1}U). } \\]

Therefore, on this chart, \\(B\_{u,v}\\) is exactly the locus

\\[ \operatorname{rank}F_A(X)=u-v. \\]

In particular, its closed rank-at-most part is defined by the \\((u-v+1)\\)-minors of a matrix of quadratic polynomials.

This is a direct algebraic description of the remaining general-\\(c\\) geometry.

### 4.4 A uniform component bound

Put

\\[ r=u-v,\qquad m=u(k-u). \\]

If

\\[ 0\leq r<\min(u,n-u), \\]

the closed locus

\\[ D_r=\\{U:\operatorname{rank}\varphi_U\leq r\\} \\]

is, on each standard affine chart, defined by polynomials of degree at most

\\[ d=2(r+1). \\]

A standard affine Bézout bound gives at most \\(d^m\\) irreducible components for such a common zero set in an \\(m\\)-dimensional affine space.

There are

\\[ \binom{k}{u} \\]

standard Grassmannian charts. Every global irreducible component meets at least one of these charts, and the number of global components is bounded by the sum of the chartwise bounds.

Since \\(B\_{u,v}\\) is an open subset of \\(D_r\\), it cannot have more irreducible components than \\(D_r\\).

Thus the following crude bound is available:

\\[ \boxed{ \\#\operatorname{Irr}(B\_{u,v}) \leq \binom{k}{u} \left(2(u-v+1)\right)^{u(k-u)}. } \\]

Here \\(\\#\operatorname{Irr}\\) denotes the number of irreducible components.

If \\(r=\min(u,n-u)\\), then \\(B\_{u,v}\\) is the full-rank locus of the bundle map, which is open in the irreducible Grassmannian. It is therefore irreducible or empty. If \\(r>\min(u,n-u)\\), it is empty.

The bound is deliberately crude. Its advantages are that it:

- is uniform;
- depends only on \\(n,k,u,v\\);
- does not require classifying the Jordan structure of \\(A\\);
- does not require enumerating \\(c\\);
- gives a finite component bound for every rank stratum.

It is not necessarily a practical numerical bound, and it is unlikely to be sharp. But it provides a rigorous route to a general-\\(c\\) component theorem.

## 5. How the \\(B\_{u,v}\\) bound enters the general-\\(c\\) theorem

The report's reduction to \\(B\_{u,v}\\) is the right idea. I would make the incidence construction slightly more explicit.

Fix \\(t,u\\). Consider pairs

\\[ (W,U) \\]

such that

\\[ W\subseteq U,\qquad A(W)\subseteq U, \\]

with

\\[ \dim W=t,\qquad\dim U=u. \\]

The exact condition

\\[ U=W+A(W) \\]

is an open rank condition within this incidence space: it says that the span of \\(W\\) and \\(A(W)\\) has dimension \\(u\\).

For a fixed \\(U\\), the possible \\(W\\)'s lie in

\\[ U\cap A^{-1}U. \\]

If

\\[ v=\dim(U\cap A^{-1}U), \\]

then the space of \\(t\\)-planes \\(W\\) contained in this intersection is

\\[ \operatorname{Gr}(t,v). \\]

On \\(B\_{u,v}\\), the kernel of the constant-rank bundle map \\(\varphi\\) is a rank-\\(v\\) vector bundle. Thus these Grassmannians form a relative Grassmannian over \\(B\_{u,v}\\).

The additional condition

\\[ U=W+A(W) \\]

cuts out an open subset of this relative Grassmannian.

Over each irreducible component of \\(B\_{u,v}\\), the relative Grassmannian is irreducible, and its nonempty open subset remains irreducible.

Finally, the \\(c\\)-dimensional spaces \\(V\\) containing \\(U\\) are parameterized by a relative Grassmannian

\\[ \operatorname{Gr}(c-u,K_0/U). \\]

The condition

\\[ V\cap A^{-1}V=W \\]

is again an open rank condition within this family.

Therefore, under the stated incidence construction, each irreducible component of \\(B\_{u,v}\\) contributes at most one irreducible component to the corresponding exact \\((t,u,v)\\) incidence stratum. Taking images cannot increase the number of irreducible components.

This justifies the bound

\\[ \boxed{ N(c)\leq N\_{\mathrm{inv}}(c) + \sum\_{t=0}^{c-1} \sum\_{u=t}^{\min(2t,c)} \sum\_{v=t}^{u} b\_{u,v}, } \\]

where

\\[ b\_{u,v}=\\#\operatorname{Irr}(B\_{u,v}), \\]

and only nonempty, dimensionally admissible strata are counted.

The sum over \\(u\\) must be explicit; it is implicit or missing in the report's displayed formula.

Combining this with the cyclic-vector bound gives

\\[ \boxed{ \begin{aligned} N(c)\leq{}& \sum\_{\lambda\vdash c}s^{b(\lambda)} \\\ &+ \sum\_{t=0}^{c-1} \sum\_{u=t}^{\min(2t,c)} \sum\_{v=t}^{u} b\_{u,v}. \end{aligned} } \\]

This is the correct general shape of the bound.

Substituting the crude affine Bézout estimate yields an entirely explicit, though large, upper bound:

\\[ \boxed{ \begin{aligned} N(c)\leq{}& \sum\_{\lambda\vdash c}s^{b(\lambda)} \\\ &+ \sum\_{t=0}^{c-1} \sum\_{u=t}^{\min(2t,c)} \sum\_{v=t}^{u} \binom{k}{u} \left(2(u-v+1)\right)^{u(k-u)}, \end{aligned} } \\]

with the full-rank and empty cases treated separately as above.

This is a legitimate general-\\(c\\) theorem candidate. It should be stated as a bound on the relevant compressed incidence strata only after the relative-Grassmannian and open-fibre construction is formalized. It does not yet count the actual observer lifts; the pair-preserving lift constraints must still be imposed.

60_deliverables_and_rank_strata.md

## 6. References and the right mathematical framework

The report asks for references on the rank strata of

\\[ U\longmapsto U\cap A^{-1}U. \\]

I would organize the literature review around three related subjects rather than search for a single theorem that exactly matches this map.

### 6.1 Determinantal varieties and degeneracy loci

The bundle morphism

\\[ \varphi:\mathcal S\to(\mathcal X\otimes\mathcal O)/\mathcal S \\]

makes \\(D_r\\) a degeneracy locus.

The most directly relevant standard references are:

- William Fulton, Intersection Theory, Chapter 14, “Degeneracy Loci and Grassmannians.” This develops degeneracy loci of vector-bundle morphisms and the Thom–Porteous formula. It is the natural reference for the geometric formulation of \\(D_r\\).&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://ideas.repec.org\&sz=32)

  RePEc+1

- Winfried Bruns and Udo Vetter, Determinantal Rings, Lecture Notes in Mathematics 1327, Springer, 1988. This is a standard reference for determinantal ideals and their algebraic properties.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://link.springer.com\&sz=32)

  Springer+1



These works provide the algebraic framework for the closed rank-at-most loci. They do not imply that the particular loci arising from a fixed operator \\(A\\) are irreducible.

### 6.2 Quiver Grassmannians and invariant-subspace varieties

The invariant part of the problem is naturally related to submodules of a module over \\(\mathbb C[t]\\), with \\(t\\) acting as \\(A\\).

Useful references include:

- Philippe Caldero and Markus Reineke, “On the quiver Grassmannian in the acyclic case,” Journal of Pure and Applied Algebra 212 (2008), 2369–2380. This studies Grassmannians of submodules of a quiver representation and their geometric properties.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://documat.unirioja.es\&sz=32)

  Documat

- Claus Michael Ringel and Markus Schmidmeier, “Invariant subspaces of nilpotent linear operators, I,” Journal für die reine und angewandte Mathematik 614 (2008), 1–52. This is particularly relevant to the geometry and classification of invariant subspaces of nilpotent operators.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://www.degruyterbrill.com\&sz=32)

  De Gruyter Brill+1



One caution: the one-loop quiver corresponding to a single arbitrary operator is not acyclic. Therefore, results specifically proved for acyclic quivers cannot simply be imported without checking their hypotheses. The Ringel–Schmidmeier work is more directly relevant to the nilpotent invariant-subspace aspect.

### 6.3 What the literature should be used for

I would not expect a general theorem saying that every \\(B\_{u,v}\\) is irreducible. The elementary counterexample above rules that out.

Instead, use these references for:

1. determinantal equations and scheme structure of \\(D_r\\);
2. dimension and codimension estimates;
3. singular loci and rank-drop behaviour;
4. component bounds for specific operator classes;
5. invariant-subspace geometry when \\(A\\) has a particularly simple Jordan form.

The new quadratic-chart description is especially useful because it makes the project's rank strata concrete, without requiring a full classification of quiver Grassmannians.

## 7. What this means for the \\(c=3\\) component count

The eleven strata should not be assigned a single irreducibility conclusion without distinguishing their bases.

The situation is:

| Stratum           | Natural base                                                                 | Component status                                           |
| ----------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------- |
| (3a), (3b), (3b′) | Products of eigenspace projective spaces or a Grassmannian                   | Irreducible when nonempty                                  |
| (3c), (3c′), (3d) | Fixed Jordan-type invariant-subspace varieties                               | Irreducible after the cyclic-vector correction             |
| (2a)              | An open sublocus of \\(B\_{3,2}\\)                                           | Not automatically irreducible                              |
| (2b)              | Invariant two-planes, followed by an open extension family                   | Finite union of irreducible fixed-type pieces              |
| (1a)              | Invariant lines, followed by an open extension family                        | Finite union of irreducible eigenvalue-labelled pieces     |
| (1b)              | A rank stratum based on \\(B\_{2,1}\\), followed by an open extension family | Not automatically irreducible without decomposing the base |
| (0)               | Open subset of \\(\operatorname{Gr}(3,K_0)\\)                                | Irreducible when nonempty                                  |

This is a useful refinement of the original eleven-stratum report.

In particular, the earlier claim that all of (2a), (2b), (1a), (1b), and (0) are open subsets of irreducible bases is too broad. The bases in (2a) and (1b) are rank-exact loci and can be reducible.

The \\(B\_{u,v}\\) framework gives a way to bound those components without having to classify them individually.

## 8. Recommended next steps

I would now change the project's priorities slightly.

## Priority 1 — Complete the general rank-strata theorem

Prove formally that

\\[ B\_{u,v}=D\_{u-v}\setminus D\_{u-v-1} \\]

for the tautological bundle morphism, then establish the quadratic chart formula and the affine Bézout component bound.

This is the most important general-\\(c\\) advance in Report 60.

## Priority 2 — Correct and certify the \\(c=3\\) table

Add the missing nilpotence conditions to the invariant cases, retain the exact-rank conditions in (2a), and write each non-invariant stratum as a precise incidence locus.

Then prove the component bounds using the invariant-type result and the \\(B\_{u,v}\\) bounds.

## Priority 3 — Formalize the forced-plane certificate

State whether the Des systems are homogeneous. If they are, prove the row-space equivalence and have the implementation output exact row-space certificates for instances 10, 16, and 21.

## Priority 4 — Integrate the lift theorem

The component bound for compressed pairs is not automatically a component bound for actual \\(L\\)'s. The pair-preserving lift map and its compatibility conditions must be incorporated.

### Suggested formalization order

I would formalize these results in Lean or another proof assistant in the following order:

1. The equivalence\
   \\[\
   \ker\varphi_U=U\cap A^{-1}U.\
   \\]
2.

# The rank identity \\[ \operatorname{rank}\varphi_U

u-\dim(U\cap A^{-1}U).\
\\]

1. The chart expression for \\(F_A(X)\\).
2. The fact that its entries have degree at most two.
3. The determinantal description of \\(D_r\\).
4. The corrected cyclic-vector parameterization.
5. The incidence-space component comparison.
6. The \\(c=3\\) exact-stratum classification.
7. The pair-preserving lift theorem.

The affine Bézout component bound may be more naturally cited as an established algebraic-geometric theorem than reproved from scratch in Lean, unless formalizing degree theory is itself a project goal.

## 9. Final answers to the five questions in the report

| Report question                                              | Adjudication                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Q1. Is the cyclic-vector argument acceptable?                | Yes, after requiring every chain vector \\(T\_\lambda^jx\\) to lie in \\(K_0\\). The fixed-type image argument is sound, and it gives the invariant-part component bound.                                                                                               |
| Q2. Is the \\(c=3\\) list exhaustive and mutually exclusive? | The eleven-way organization is exhaustive by \\(t,u\\) and Jordan type; \\(u=4\\) is impossible. But the invariant rows need missing nilpotence equations, and the exact condition in (2a) must be added.                                                               |
| Q3. Are all \\(B\_{u,v}\\) irreducible?                      | No. \\(B\_{1,1}\\) for a diagonal \\(2\times2\\) matrix with distinct eigenvalues is already reducible. A uniform, crude component bound follows from the quadratic chart representation and affine Bézout.                                                             |
| Q4. Is the forced-plane row-space criterion correct?         | Yes for homogeneous Des equations. For affine equations, add the condition that the coordinate functional vanishes at one particular solution. The stated infeasibility conclusion for 16/21 follows if both equations are homogeneous and both rows force \\(b_i=0\\). |
| Q5. Is the proposed general-\\(c\\) bound the right shape?   | Yes in structure, but the sum over \\(u\\) must be explicit, and the incidence-to-\\(V\\) fibre argument must be proved. The resulting bound is a bound for the compressed geometric strata; the actual observer lift still needs its own analysis.                     |

## 10. Overall conclusion

Report 60 is a substantial improvement over the previous stage. The cyclic-vector repair gives a clean route to the invariant component bound, and the forced-plane criterion turns the \\(c=2\\) obstruction into an exact linear-algebra certificate.

The most important unresolved issue is now much more sharply defined:

\\[ \boxed{ \text{Control the irreducible components of } B\_{u,v} = \\{U:\dim(U\cap A^{-1}U)=v\\}. } \\]

There is no universal irreducibility theorem: even the simplest example is reducible. But the rank-strata formulation gives a general determinantal description, and the quadratic chart calculation gives a uniform component bound.

That is enough to make real progress on the general-\\(c\\) problem without solving every invariant-subspace variety explicitly.

My strongest recommendation: turn the quadratic-chart representation and the resulting component bound for \\(B\_{u,v}\\) into the next formal theorem. In parallel, correct the \\(c=3\\) table and use the \\(B\_{u,v}\\) framework to repair its non-invariant component claims. This would convert the present classification programme into a coherent general-\\(c\\) geometric bound, while keeping the separate observer-lift problem visible rather than silently absorbing it into the compressed geometry.