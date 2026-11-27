# Research assessment of Report 54: the general theorem, the \\(e>0\\) results, and the direction of \\(q1\\)

## Executive assessment

Report 54 is a substantial improvement over the previous version. It corrects the false general linearity claim, gives a sounder projective formulation, separates compressed compatibility from full-row-rank lifting, and identifies a more general sufficient condition for spectral failure. These are important advances.&#x20;

54_general_theorem_and_q1_direction(1).md

54_general_theorem_and_q1_direction(1).md



However, I would make one major change to the research direction.

The report currently treats the component decomposition of the lifted incidence space as the central unresolved difficulty. I think that is too pessimistic in the hyperplane case

\\[ k=\omega+1. \\]

There is a useful structural observation:

> Once the projective subspace is represented by its annihilator, the constraints on \\(R\\) are linear in \\(R\\). On every constant-rank base stratum, the admissible \\(R\\)'s form a vector bundle. The fibre therefore does not create an independent component-decomposition problem.

Moreover, for a hyperplane, the rank of the constraint map is simply the rank of two vectors \\(v\\) and \\(Av\\). Its rank-one locus is an eigenvector locus of \\(A\\), hence a union of projective linear subspaces.

This leads to a considerably sharper description than the proposed bound of 16 components for \\(k=\omega+1,\delta=2\\). Here I write

\\[ \delta:=\dim\ker T \\]

for the number of columns of \\(Z_1,Z_2\\), to avoid confusing it with the previously used \\(d=k-\omega\\).

My principal recommendations are:

1. Retain the corrected projective theorem and lifting lemma, with a few explicit qualifications.
2. Replace the proposed general component-decomposition strategy for \\(k=\omega+1\\) by a vector-bundle/eigenvector decomposition theorem.
3. Retain the five-instance and six-instance tables as exact examples, but do not promote them to universal classification results.
4. Replace the condition \\(\operatorname{row}Z_1\cap\operatorname{row}Z_2=0\\) by a more invariant kernel-dimension obstruction.
5. Separate the complexity of the synthesis decision problem from the complexity of enumerating every irreducible component.
6. For general \\(k-\omega>1\\), investigate Grassmannian degeneracy loci associated with \\(V\mapsto V+AV\\). This is the genuinely interesting remaining geometric problem.

I discuss the six questions in detail.

# 1. Question 1: Are the corrected projective theorem and lifting lemma now correct?

## 1.1 The projective theorem is correct, with an important scope condition

The report uses

\\[ S=\ker\sigma,\qquad [\sigma]\in\mathbb P^{k-1}. \\]

Consequently,

\\[ \dim S=k-1. \\]

Since the theorem requires \\(\dim S=\omega\\), it is specifically a hyperplane theorem, and it requires

\\[ \boxed{\omega=k-1.} \\]

This should be stated explicitly at the beginning of II.1. The report's broader discussion sometimes suggests that the same projective parametrisation applies for arbitrary \\(\omega\\), but it does not.

For arbitrary \\(\omega\\), the correct parameter space is

\\[ \operatorname{Gr}(\omega,k), \\]

not \\(\mathbb P^{k-1}\\).

The distinction is important for the generalisation in Question 4.

### The coordinate correction

Let \\(B_S\in\mathbb C^{k\times\omega}\\) be a basis matrix for \\(S\\). I recommend writing \\(B_S\\), rather than \\(B\\), to avoid confusion with the complementary block in the spectral decomposition.

Then

\\[ P=B_S^\top Z_1,\qquad Q=B_S^\top Z_2, \\]

and

\\[ X_S=\\{a\in\mathbb C^{1\times\omega}:aP\in\operatorname{row}Q\\}. \\]

The fixed top-row space must be represented in the same coordinates:

\\[ \widetilde E_S = \\{a\in\mathbb C^{1\times\omega}:aB_S^\top\in E\\}. \\]

The condition

\\[ \widetilde E_S+X_S=\mathbb C^{1\times\omega} \tag{1.1} \\]

is correct.

In particular, the dimension equality

\\[ e+\dim X_S-\dim(\widetilde E_S\cap X_S)=\omega \tag{1.2} \\]

is correct. The report has fixed the previous coordinate-space ambiguity.&#x20;

54_general_theorem_and_q1_direction(1).md



I would also include the useful rank formula

\\[ \boxed{ \dim X_S = \omega- \left( \rank\begin{bmatrix}P\\\Q\end{bmatrix} -\rank Q \right). } \tag{1.3} \\]

To see this, consider

\\[ \varphi_S:\mathbb C^{1\times\omega} \longrightarrow \mathbb C^{1\times\delta}/\operatorname{row}Q, \qquad a\longmapsto aP+\operatorname{row}Q. \\]

Then \\(X_S=\ker\varphi_S\\), and

\\[ \rank\varphi_S = \rank\begin{bmatrix}P\\\Q\end{bmatrix}-\rank Q. \\]

Likewise,

\\[ \dim(\widetilde E_S\cap X_S) = e-\rank(\varphi_S|\_{\widetilde E_S}). \tag{1.4} \\]

These two identities are useful both theoretically and computationally.

### The row-capacity condition

The condition

\\[ m=q-r\geq\omega-e \tag{1.5} \\]

is also necessary and sufficient for the bottom rows to have enough capacity to complete \\(E\\) to an \\(\omega\\)-dimensional space, once (1.1) holds.

The logic is:

- The fixed top rows already span an \\(e\\)-dimensional space.
- The bottom \\(m\\) rows must supply at least \\(\omega-e\\) additional independent directions.
- The compatible first-coordinate rows span \\(X_S\\).
- The equality \\(\widetilde E_S+X_S=\mathbb C^\omega\\) says that those compatible directions are sufficient.

Thus the three conditions in the report form the correct compressed admissibility criterion.

One qualification should remain explicit:

This theorem establishes the existence of compatible compressed row pairs. It does not, by itself, establish that those pairs have a full-row-rank lift \\(R\\).

The lifted incidence formulation is needed for that final step.

## 1.2 The lifted incidence space is the right object

I agree with the decision to include \\(R\\) directly:

\\[ \mathcal I = \\{(\sigma,R):\text{the incidence, compatibility and rank conditions hold}\\}. \\]

This avoids an unnecessary projection problem.

The conditions

\\[ \operatorname{row}(RN)\subseteq S,\qquad \operatorname{row}(RAN)\subseteq S \\]

express the restriction of (5a) to \\(K\\). Together with the corresponding top-row conditions, they give

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H. \\]

The equality

\\[ \operatorname{row}(L_0N;RN)=S \\]

then enforces \\(\rank H=\omega\\).

Finally,

\\[ \rank[L_0;R]=q \\]

is an open condition.

Therefore the lifted incidence space is locally closed, as claimed.&#x20;

54_general_theorem_and_q1_direction(1).md



There is no remaining fundamental constructibility issue here.

The distinction I would retain is:

- If one projects from a lifted space to compressed-pair space, the image is generally only guaranteed to be constructible by Chevalley's theorem.
- If one keeps \\(R\\) as a variable, full row rank is an open condition, and the incidence space itself is locally closed.

The second formulation is cleaner for the genericity argument.

## 1.3 The genericity theorem is correct

Let \\(X\\) be an irreducible locally closed component of the lifted incidence space, with

\\[ \rank H(x)=\omega\qquad\forall x\in X. \\]

Consider

\\[ \mathcal I\_{\mathrm{bad}} = \left\\{ (x,[\alpha:\beta])\in X\times\mathbb P^1: \rank(\alpha H(x)-\beta H_A(x))<\omega \right\\}. \\]

This is closed, since the condition is given by the vanishing of the \\(\omega\times\omega\\) minors.

At infinity,

\\[ [\alpha:\beta]=[1:0], \\]

the matrix is \\(H(x)\\), which has rank \\(\omega\\). Thus the bad incidence set avoids infinity.

The projection

\\[ X\times\mathbb P^1\longrightarrow X \\]

is proper, so the bad locus is closed in \\(X\\).

Since \\(X\\) is irreducible,

\\[ \boxed{ B_X=X \quad\text{or}\quad X\setminus B_X \text{ is nonempty, open and dense in }X. } \tag{1.6} \\]

The function-field determinant-divisor criterion is also correct:

\\[ \boxed{ \text{generic point of }X\text{ is bad} \iff \gcd(\omega\text{-minors of }\lambda H-H_A) \text{ is nonconstant in }\mathbb C(X)[\lambda]. } \tag{1.7} \\]

One should apply this component by component, not to a reducible union as if it had a single function field.

Verdict on Question 1: II.1 is correct under the explicit hyperplane hypothesis \\(\omega=k-1\\), and II.2 is correct. More importantly, I believe the component structure of the lifted incidence space can be analysed more directly than the report currently suggests. I develop that point in Section 3.

# 2. Question 2: Is the determinantal reformulation of the \\(k=3\\) examples correct?

Yes. The retraction in II.3 is mathematically appropriate.

The previous claim that every \\(k=3,e=0\\) rank stratum is a projective subspace or its complement was false. The counterexample in the report correctly shows that separate intersection dimensions do not determine the stacked rank.&#x20;

54_general_theorem_and_q1_direction(1).md



The right distinction is:

- The rank of \\(Q\\) is governed by a linear incidence condition.
- The rank of \\(\begin{bmatrix}P\\\Q\end{bmatrix}\\) is governed by a coupled condition involving a common preimage.
- The latter is determinantal and need not be linear or irreducible.

I would keep the counterexample. It is valuable because it identifies exactly why the earlier geometric shortcut failed.

## 2.1 A further structural identity

There is, however, a useful refinement that connects the projective ranks directly to the original operator \\(A\\).

Let

\\[ T:K\oplus K\longrightarrow\mathbb C^n, \qquad T(v,w)=v+Aw, \\]

and let

\\[ \ker T = \operatorname{im} \begin{bmatrix}Z_1\\\Z_2\end{bmatrix}, \qquad \delta=\dim\ker T. \\]

For a hyperplane \\(S=\ker\sigma\\), write

\\[ v=N\sigma^\top\in K\setminus\\{0\\}. \\]

Define

\\[ \rho(v)=\rank[v,\ Av]. \\]

Since \\(v\ne0\\),

\\[ \rho(v)\in\\{1,2\\}. \\]

Then the following identity holds:

\\[ \boxed{ \rank\begin{bmatrix}P\\\Q\end{bmatrix} = \delta-2+\rank[v,\ Av]. } \tag{2.1} \\]

### Proof

The kernel of the stacked quotient map is

\\[ \left\\{ u\in\mathbb C^\delta: Z_1u\in\operatorname{span}\\{\sigma^\top\\}, \quad Z_2u\in\operatorname{span}\\{\sigma^\top\\} \right\\}. \\]

For such a \\(u\\), there are unique scalars \\(a,b\\) with

\\[ Z_1u=a\sigma^\top,\qquad Z_2u=b\sigma^\top. \\]

Since

\\[ NZ_1+ANZ_2=0, \\]

we obtain

\\[ aN\sigma^\top+bAN\sigma^\top=0, \\]

or

\\[ av+bAv=0. \\]

Conversely, every pair \\((a,b)\\) satisfying this relation gives an element

\\[ (a\sigma^\top,b\sigma^\top)\in\ker T, \\]

and hence a unique \\(u\\).

Thus

\\[ \dim\ker\begin{bmatrix}P\\\Q\end{bmatrix} = \dim\ker[v,\ Av] = 2-\rho(v). \\]

Rank-nullity gives (2.1).

This is a useful identity because it replaces the coupled stacked-rank calculation by a simple rank-two matrix involving \\(A\\).

## 2.2 The rank-one locus is an eigenvector locus

We have

\\[ \rho(v)=1 \iff Av\in\mathbb Cv. \\]

Therefore

\\[ \rho(v)=1 \iff v\text{ is an eigenvector of }A. \tag{2.2} \\]

This gives a much more structural description of the projective rank stratification.

The \\(\rho=1\\) locus is a union of projectivised eigenspaces:

\\[ \bigcup\_{\lambda\in\operatorname{spec}(A)} \mathbb P\bigl(K_0\cap\ker(A-\lambda I)\bigr), \tag{2.3} \\]

where \\(K_0\\) is the linear subspace of \\(K\\) corresponding to the projective base condition \\(E+F_0\subseteq S\\).

The complement is the \\(\rho=2\\) locus.

This is a stronger structural description than merely saying that the stacked-rank locus is determinantal.

It also explains why the \\(k=3\\) examples can have exceptional projective points corresponding to eigenvectors.

# 3. A new component-decomposition theorem for the hyperplane case

This is the most important additional result I would pursue.

The report says that the base rank stratification has at most 16 components for \\(k=\omega+1,\delta=2\\), but that the fibre over each base component remains difficult.&#x20;

54_general_theorem_and_q1_direction(1).md



I believe the second part can be improved substantially.

## 3.1 The constraints on \\(R\\) are linear for fixed \\(S\\)

For a hyperplane \\(S=\ker\sigma\\), define

\\[ v=N\sigma^\top. \\]

The conditions

\\[ \operatorname{row}(RN)\subseteq S, \qquad \operatorname{row}(RAN)\subseteq S \\]

are equivalent to

\\[ \boxed{ Rv=0,\qquad RAv=0. } \tag{3.1} \\]

These are linear equations in the entries of \\(R\\).

For a single row \\(r\\) of \\(R\\), they say

\\[ rv=0,\qquad rAv=0. \\]

The rank of these two linear constraints is precisely

\\[ \rho(v)=\rank[v,\ Av]. \\]

Consequently, for fixed \\(v\\), the solution space for each row of \\(R\\) has dimension

\\[ n-\rho(v). \\]

For \\(m=q-r\\) rows, the full solution space has dimension

\\[ \boxed{m(n-\rho(v)).} \tag{3.2} \\]

On any constant-\\(\rho\\) base stratum, these kernels form a vector bundle.

This is the key point: the fibre is not an arbitrary nonlinear algebraic variety.

## 3.2 The base is a projective linear space

The fixed top-row conditions require

\\[ E+F_0\subseteq S=\ker\sigma. \\]

Equivalently,

\\[ \sigma e^\top=0,\qquad \sigma f^\top=0 \\]

for every \\(e\in E\\), \\(f\in F_0\\).

Under the isomorphism \\(N:\mathbb C^k\to K\\), these conditions define a linear subspace

\\[ K_0\subseteq K. \\]

The projective base is therefore

\\[ \boxed{\mathcal B=\mathbb P(K_0).} \tag{3.3} \\]

If \\(K_0=\\{0\\}\\), the base is empty and there is no candidate.

Otherwise, \\(\mathcal B\\) is irreducible.

## 3.3 Decomposition into eigenvector and non-eigenvector pieces

Define

\\[ \mathcal B_1 = \\{[v]\in\mathbb P(K_0):Av\in\mathbb Cv\\}. \\]

Then

\\[ \mathcal B_1 = \bigcup\_{\lambda\in\operatorname{spec}(A)} \mathbb P\bigl(K_0\cap\ker(A-\lambda I)\bigr). \tag{3.4} \\]

Each nonempty term is a projective linear subspace.

Moreover, eigenspaces corresponding to distinct eigenvalues have zero intersection. Their projectivisations are therefore disjoint.

Let

\\[ \mathcal B_2=\mathcal B\setminus\mathcal B_1. \\]

This is an open subset of the irreducible projective space \\(\mathcal B\\), so if nonempty it is irreducible.

Thus the base has at most

\\[ 1+\\#\\{\lambda: K_0\cap\ker(A-\lambda I)\ne0\\} \\]

irreducible pieces.

There is a sharper bound. Every eigenvector in \\(K_0\\) belongs to

\\[ D_A:=K\cap A^{-1}K. \\]

Write

\\[ \delta=\dim D_A=\dim\ker T. \\]

Eigenspaces corresponding to distinct eigenvalues are linearly independent. Since they all intersect \\(D_A\\), the number of nonempty projective eigenspace pieces is at most \\(\delta\\).

Therefore

\\[ \boxed{ \\#\\{\text{base components}\\}\leq\delta+1. } \tag{3.5} \\]

For \\(\delta=2\\), this gives at most three components, not 16.

## 3.4 The lifted incidence is a vector bundle over each piece

Let \\(X\\) be one of the irreducible base pieces on which \\(\rho(v)\\) is constant.

Define

\\[ \mathcal V_X = \\{(v,R)\in X\times\mathbb C^{m\times n}: Rv=0,\ RAv=0\\}. \\]

The linear map

\\[ \mathbb C^{1\times n} \longrightarrow\mathbb C^2, \qquad r\longmapsto(rv,rAv) \\]

has constant rank \\(\rho\\) on \\(X\\).

Its kernel therefore forms a vector bundle of rank \\(n-\rho\\). Taking \\(m\\) rows gives a vector bundle of rank

\\[ m(n-\rho). \\]

Now impose the two remaining conditions:

\\[ \rank H=\omega,\qquad \rank[L_0;R]=q. \\]

Both are open conditions on the total vector bundle:

- All rows of \\(H\\) already lie in the \\(\omega\\)-dimensional space \\(S\\), so \\(\rank H=\omega\\) is an open maximal-rank condition.
- Full row rank of \\([L_0;R]\\) is also an open maximal-rank condition.

Thus the actual lifted incidence over \\(X\\) is an open subset of an irreducible vector bundle.

A nonempty open subset of an irreducible variety is irreducible.

We obtain the following theorem.

Proposed structural theorem

Hyperplane lifted-incidence decomposition theorem

Assume \\(\omega=k-1\\). Let

\\[ K_0=\\{N\sigma^\top:\sigma E^\top=0,\ \sigma F_0^\top=0\\}\subseteq K. \\]

Let

\\[ D_A=K\cap A^{-1}K,\qquad \delta=\dim D_A. \\]

The lifted incidence space, including the full-row-rank and rank-\\(H\\) conditions, has at most

\\[ \boxed{\delta+1} \\]

nonempty irreducible components.

These components lie over:

- the non-eigenvector open subset of \\(\mathbb P(K_0)\\), if nonempty;
- the projectivised nonzero intersections \\(K_0\cap\ker(A-\lambda I)\\), for the distinct eigenvalues \\(\lambda\\) that occur.

Each nonempty lifted piece is an open subset of a vector bundle over its corresponding base piece.

The proof is exactly the rank-constant kernel-bundle argument above.

### Why this matters

This result directly addresses the main concern in II.6.

The fibre over a base component is not an independent source of arbitrary irreducible components. The fibre is linear; the full-rank conditions only remove closed subsets.

The difficult component geometry, in this hyperplane setting, is already present in the base eigenvector decomposition.

For \\(\delta=2\\), the base decomposition is particularly simple:

- at most two projective eigenspace components;
- one non-eigenvector open component.

The proposed bound of 16 can therefore be replaced by the sharper bound of 3 for the lifted incidence, under the stated hyperplane assumptions.

## 3.5 Refinement if one insists on retaining the rank-\\(Q\\) strata

There is a further useful identity.

The second-coordinate projection of \\(\ker T\\) is injective, so

\\[ \rank Z_2=\delta. \\]

Its image corresponds to

\\[ D_A=K\cap A^{-1}K. \\]

Therefore

\\[ \boxed{ \rank Q= \begin{cases} \delta-1,&v\in D_A,\\\ \delta,&v\notin D_A. \end{cases}} \tag{3.6} \\]

An eigenvector \\(v\\) automatically belongs to \\(D_A\\).

Consequently, if one refines the base decomposition by both \\(\rank Q\\) and \\(\rank[P;Q]\\), the natural pieces are:

1. Eigenvectors in \\(K_0\cap D_A\\);
2. Non-eigenvectors in \\(K_0\cap D_A\\);
3. Vectors in \\(K_0\setminus D_A\\).

The second and third pieces, when nonempty, are open subsets of projective linear spaces and are irreducible.

The first piece is a union of at most \\(\delta\\) disjoint projective linear spaces.

Thus the refined base stratification has at most

\\[ \boxed{\delta+2} \\]

nonempty irreducible pieces.

For \\(\delta=2\\), this gives at most four.

This is a useful refinement for the projective rank table, but it is not necessary for the lifted-incidence genericity theorem. The latter only needs the constant rank of \\([v,Av]\\).

# 4. Question 3: Is the \\(e>0\\) interpretation correct?

The report's empirical interpretation is reasonable, but it should be stated more cautiously.

The six examples establish the following facts:

- The mixed \\(d=1\\) phenomenon occurs in the displayed \\(e=1\\) data.
- The \\(d=2\\) all-bad phenomenon does not persist universally when \\(U_0\ne0\\).
- Some \\(d=2,e=1\\) instances are good and others are all bad.

These are valid conclusions about the six computed instances. They do not establish a general robustness theorem for \\(d=1\\), nor a universal \\(U_0=0\\) classification for \\(d=2\\).&#x20;

54_general_theorem_and_q1_direction(1).md



## 4.1 The correction of the \\(V_0Z_2\\) argument is right

The report correctly retracts the claim

\\[ V_0Z_2=0\implies\text{all bad}. \\]

The compatibility equation is

\\[ x_iZ_1+y_iZ_2=0. \\]

Thus

\\[ y_iZ_2=-x_iZ_1, \\]

which need not vanish.

The correct object is

\\[ Y=\\{y\in\mathbb C^k:yZ_2\in\operatorname{row}Z_1\\}. \\]

The dimension formula

\\[ \boxed{ \dim Y = k-\rank Z_2+ \dim(\operatorname{row}Z_1\cap\operatorname{row}Z_2) } \tag{4.1} \\]

is correct.

The proof is rank-nullity applied to

\\[ \psi:\mathbb C^{1\times k} \longrightarrow \mathbb C^{1\times\delta}/\operatorname{row}Z_1, \qquad y\longmapsto yZ_2+\operatorname{row}Z_1. \\]

Its rank is

\\[ \rank Z_2- \dim(\operatorname{row}Z_1\cap\operatorname{row}Z_2). \\]

Every row of \\(H_A\\) belongs to \\(Y\\):

- For a bottom row \\(y_i\\),\
  \\[\
  y_iZ_2=-x_iZ_1\in\operatorname{row}Z_1.\
  \\]
- For the top row \\(V_0\\),\
  \\[\
  V_0Z_2=-U_0Z_1\in\operatorname{row}Z_1.\
  \\]

Therefore

\\[ \operatorname{row}H_A\subseteq Y. \\]

If

\\[ \dim Y<\omega, \\]

then

\\[ \rank H_A<\omega, \\]

so the pencil is rank-deficient at \\(\lambda=0\\).

Thus the sufficient condition is sound.&#x20;

54_general_theorem_and_q1_direction(1).md



## 4.2 Simplify the stated condition

There is an additional simplification that should be included.

The projection of \\(\ker T\\) onto its second coordinate is injective. Therefore

\\[ \rank Z_2=\delta. \\]

Since \\(Z_2\\) has \\(\delta\\) columns, its row space is all of \\(\mathbb C^\delta\\):

\\[ \operatorname{row}Z_2=\mathbb C^\delta. \\]

Hence

\\[ \operatorname{row}Z_1\cap\operatorname{row}Z_2 = \operatorname{row}Z_1. \\]

The report's condition

\\[ \operatorname{row}Z_1\cap\operatorname{row}Z_2=0 \\]

is therefore equivalent to

\\[ \boxed{Z_1=0.} \tag{4.2} \\]

It is a valid sufficient condition, but it is quite restrictive. I would state it in the simpler form \\(Z_1=0\\).

There is also a more invariant interpretation. The kernel of \\(Z_1\\), under the second-coordinate projection, corresponds to

\\[ K\cap\ker A. \\]

Consequently,

\\[ \dim Y=k-\dim(K\cap\ker A). \tag{4.3} \\]

This gives a more transparent sufficient criterion:

\\[ \boxed{ \dim(K\cap\ker A)>k-\omega \quad\Longrightarrow\quad \text{every admissible point is bad at }\lambda=0. } \tag{4.4} \\]

In the hyperplane case \\(k=\omega+1\\), this becomes

\\[ \boxed{ \dim(K\cap\ker A)\geq2 \quad\Longrightarrow\quad \text{all admissible points are bad at }\lambda=0. } \tag{4.5} \\]

This is a useful structural obstruction, and it does not require \\(U_0=0\\).

### A direct proof of (4.4)

If \\(v\in K\cap\ker A\\), then

\\[ A v=0. \\]

Every row of \\(H_A=LAN\\) annihilates the coordinate vector of \\(v\\). Thus

\\[ \ker(A|\_K)\subseteq\ker H_A. \\]

Therefore

\\[ \rank H_A \leq k-\dim(K\cap\ker A). \\]

If the right-hand side is smaller than \\(\omega\\), then \\(\rank H_A<\omega\\), and the pencil is bad at zero.

This is perhaps the cleanest way to state the obstruction.

## 4.3 A more general necessary condition for good feasibility

The same argument works for every spectral parameter.

For any \\(\lambda\in\mathbb C\\), define

\\[ K\_\lambda=K\cap\ker(A-\lambda I). \\]

Since

\\[ H_A-\lambda H = L(A-\lambda I)N, \\]

every row of this matrix annihilates \\(K\_\lambda\\).

Therefore

\\[ \boxed{ \rank(H_A-\lambda H) \leq k-\dim K\_\lambda. } \tag{4.6} \\]

A necessary condition for any good candidate of rank \\(\omega\\) is thus

\\[ \boxed{ \dim\bigl(K\cap\ker(A-\lambda I)\bigr) \leq k-\omega \quad\forall\lambda\in\mathbb C. } \tag{4.7} \\]

This is not sufficient. Even if all these eigenspace dimensions satisfy the bound, the pencil may still have a common finite rank-loss root for other structural reasons.

But it is a natural invariant obstruction, and it should be added to the paper.

## 4.4 Is there a necessary and sufficient condition for all-bad behaviour?

For a fixed compressed pair, the exact condition remains the common-root condition:

\\[ \gcd(\omega\text{-minors of }\lambda H-H_A) \text{ is nonconstant}. \\]

For an irreducible incidence component, the exact generic condition is the corresponding function-field gcd.

I do not see a simple necessary and sufficient condition involving only

\\[ \dim(K\cap\ker(A-\lambda I)) \\]

or only the ranks of \\(Z_1,Z_2\\).

The example with a common root \\(\lambda_0=-1\\) illustrates why: failure can occur away from \\(\lambda=0\\), even when the zero-parameter obstruction is absent.

My recommendation: retain the \\(Y\\)-criterion as a general sufficient condition, add the invariant eigenspace obstruction (4.7), and do not claim a necessary and sufficient rank-only classification.

# 5. Question 4: What is the right direction for \\(q1\\)?

This is the most important research-strategy question.

My answer is that the component-decomposition route remains relevant, but it should be reformulated. It is not the entire fibre geometry that needs to be decomposed.

## 5.1 Separate three computational problems

The report currently groups the following tasks together:

1. Decompose the lifted incidence space into irreducible components.
2. Compute the generic determinant divisor on each component.
3. Decide real feasibility.

I would distinguish three different problems:

| Problem                   | Mathematical task                                         | Why it matters                                                  |
| ------------------------- | --------------------------------------------------------- | --------------------------------------------------------------- |
| A. Synthesis decision     | Does any good full-row-rank \\(R\\) exist?                | The actual yes/no observer-design question                      |
| B. Generic classification | Which irreducible components are generically good or bad? | Explains the geometry and exceptional cases                     |
| C. Component enumeration  | What are all irreducible components and their equations?  | Stronger structural information, but not always necessary for A |

The report's present \\(q1\\) is primarily Problem C. But the actual observer-synthesis decision, Problem A, does not necessarily require solving C.

This distinction is important for the research programme.

## 5.2 For \\(k=\omega+1\\), the component problem has a structural solution

The theorem in Section 3 gives at most \\(\delta+1\\) lifted-incidence components.

For \\(\delta=2\\), there are at most three:

- the non-eigenvector open component;
- the projectivised eigenspace component for one eigenvalue;
- the projectivised eigenspace component for a second eigenvalue.

There may be fewer.

Thus I would not treat component decomposition as an unresolved general algebraic-geometric problem in the hyperplane case.

The next task is to prove the vector-bundle theorem carefully and verify it against the existing examples.

## 5.3 For general codimension, the right base variety is a Grassmannian degeneracy locus

Now consider arbitrary

\\[ c=k-\omega. \\]

The variable subspace \\(S\\) has codimension \\(c\\). Instead of \\(S\\), use its annihilator \\(T\\), a \\(c\\)-dimensional subspace of the dual coordinate space. Under \\(N\\), identify it with a \\(c\\)-dimensional subspace

\\[ V\subseteq K. \\]

The fixed top-row conditions impose

\\[ V\subseteq K_0 \\]

for a suitable fixed linear subspace \\(K_0\subseteq K\\).

Thus the projective/Grassmannian base becomes

\\[ \operatorname{Gr}(c,K_0). \\]

For a fixed \\(V\\), the conditions on \\(R\\) are

\\[ RV=0,\qquad RAV=0. \\]

Equivalently, each row of \\(R\\) annihilates \\(V+AV\\).

Define

\\[ \rho(V)=\dim(V+AV). \\]

Then the solution space for \\(R\\), before imposing full-rank conditions, has dimension

\\[ \boxed{ m\bigl(n-\rho(V)\bigr). } \tag{5.1} \\]

On every constant-\\(\rho\\) stratum, these solution spaces form a vector bundle. The rank-\\(H\\) and full-row-rank conditions are open.

This gives the general formulation:

\\[ \boxed{ \mathcal D_s = \\{V\in\operatorname{Gr}(c,K_0): \dim(V+AV)\leq s\\}. } \tag{5.2} \\]

The component-decomposition problem is therefore reduced to a special family of Grassmannian degeneracy loci associated with \\(A\\).

This is a much more precise description of \\(q1\\).

### Why this is the right algebraic-geometric language

The map

\\[ \mathcal T\oplus\mathcal T \longrightarrow K\oplus\mathbb C^n, \qquad (v,w)\longmapsto v+Aw, \\]

where \\(\mathcal T\\) is the tautological bundle on the Grassmannian, is a morphism of vector bundles.

Its rank-drop loci are determinantal degeneracy loci.

Equivalently,

\\[ \dim(V+AV) = 2c-\dim(V\cap A^{-1}V). \tag{5.3} \\]

Thus the relevant geometry is the geometry of subspaces having a prescribed-dimensional intersection with their inverse image under \\(A\\).

For \\(c=1\\), this reduces to the eigenvector condition.

For \\(c>1\\), it is genuinely richer.

The most natural neighbouring subjects are:

- determinantal degeneracy loci;
- Grassmannian incidence varieties;
- varieties of invariant subspaces;
- quiver Grassmannians for the one-loop (Jordan) quiver.

The connection to invariant-subspace varieties is particularly direct at the lowest-rank stratum:

\\[ \dim(V+AV)=c \iff AV\subseteq V. \\]

That is precisely the condition that \\(V\\) be \\(A\\)-invariant.

For intermediate ranks, one studies subspaces \\(V\\) for which a large subspace of \\(V\\) is mapped back into \\(V\\).

This is a much more promising generalisation than attempting to enumerate arbitrary determinantal components without using the special structure of \\(A\\).

## 5.4 Is a polynomial algorithm realistic?

My assessment is now more optimistic for the hyperplane case, but more cautious for general codimension.

### Hyperplane case \\(c=1\\)

The base decomposition is controlled by eigenspaces. Its component count is at most \\(\delta+1\\).

For rational or algebraic input, a plausible exact algorithm is:

1. Compute \\(K\\) and \\(K_0\\).
2. Compute the relevant eigenspaces \\(K_0\cap\ker(A-\lambda I)\\).
3. Construct the non-eigenvector open component and the eigenspace components.
4. On each component, parameterise the vector-bundle fibre of \\(R\\).
5. Test generic rank of \\(H\\) and \\([L_0;R]\\).
6. Compute the generic determinant divisor of \\(\lambda H-H_A\\).
7. Accept if one component has a nonempty full-rank open set and generic gcd \\(1\\).

The crucial fact is that, on an irreducible component, the full-rank and good conditions are open. If both are nonempty, their intersection is nonempty.

This is a plausible route to an efficient algorithm for \\(c=1\\).

### General codimension \\(c>1\\)

Here the base variety

\\[ \mathcal D_s\subseteq\operatorname{Gr}(c,K_0) \\]

can have more complicated geometry.

I would not claim a polynomial algorithm yet.

However, I would also not begin a hardness reduction immediately. The structure

\\[ V\longmapsto V+AV \\]

is highly constrained: it is generated by a single linear operator, not by an arbitrary tuple of matrices.

A reduction from arbitrary polynomial feasibility would have to exploit this special form. It may be possible, but no hardness conclusion follows merely from the fact that general determinantal varieties can be complicated.

### My judgement

| Setting                       | Most promising direction                                                  |
| ----------------------------- | ------------------------------------------------------------------------- |
| \\(c=1\\)                     | Structural decomposition and generic algebra                              |
| \\(c=2\\), small \\(\delta\\) | Explicit Grassmannian incidence analysis                                  |
| Fixed \\(c\\)                 | Seek degree/component bounds and structured algorithms                    |
| Variable \\(c\\)              | Investigate both algorithmic structure and possible hardness              |
| General synthesis decision    | Use bounded polynomial certificates; do not require component enumeration |

I would put structural analysis ahead of hardness reductions at this stage.

## 5.5 The synthesis decision already has a separate \\(\exists\mathbb R\\) route

There is an additional point from the previous work that should influence the strategy.

The universal spectral condition can be replaced by a bounded-degree polynomial certificate.

On a rank-\\(\omega\\), (5a)-admissible stratum, factor

\\[ H=UV,\qquad H_A=GV, \\]

where \\(U\in\mathbb F^{q\times\omega}\\) has full column rank and \\(V\in\mathbb F^{\omega\times k}\\) has full row rank. Then

\\[ P(\lambda)=\lambda H-H_A=(\lambda U-G)V. \\]

The pointwise full-rank condition is equivalent to the existence of a polynomial generalized inverse

\\[ Y(\lambda)\in\mathbb F[\lambda]^{k\times q} \\]

satisfying

\\[ P(\lambda)Y(\lambda)P(\lambda)=P(\lambda). \tag{5.4} \\]

A bounded degree

\\[ \deg Y\leq 2\omega-2 \\]

suffices.

Thus the universal quantification over \\(\lambda\\) can be replaced by finitely many coefficient equations.

The factorisation of \\(H,H_A\\), full-rank witnesses, and the coefficient equations of (5.4) give a polynomial-size existential algebraic system. This provides an \\(\exists\mathbb R\\) upper bound for the real synthesis decision problem; it does not establish \\(\exists\mathbb R\\)-hardness.&#x20;

This is a separate and important research direction.

The key consequence is that irreducible-component enumeration is not a prerequisite for deciding whether a good observer exists. It is needed for the richer generic classification problem, not necessarily for the basic yes/no synthesis problem.

# 6. Question 5: Should the examples remain in the paper?

Yes. I would retain both tables.

The report is right to treat them as exact examples rather than as a general irreducibility theorem.&#x20;

54_general_theorem_and_q1_direction(1).md



The examples have three distinct roles:

1. They demonstrate that the compressed projective strata can have different spectral behaviour.
2. They show that the \\(d=1\\) mixed phenomenon persists in at least some \\(e>0\\) settings.
3. They show that the \\(d=2\\) all-bad behaviour is not universal once \\(U_0\ne0\\).

The third point is especially useful. It prevents the paper from making an overgeneralised statement based on the \\(U_0=0\\) theorem.

## 6.1 What must accompany the tables?

I would require the following for every example.

| Required item                                        | Reason                                      |
| ---------------------------------------------------- | ------------------------------------------- |
| Exact \\(A,C,L_0\\) or exact \\(N,Z_1,Z_2,U_0,V_0\\) | Reproducibility                             |
| Exact projective stratum equations                   | Makes the geometry independently checkable  |
| Exact ranks \\(r_Q,r\_{PQ}\\)                        | Verifies admissibility                      |
| Exact \\(\dim X_S\\) and \\(t\\)                     | Verifies the corrected projective criterion |
| Exact gcd of maximal minors                          | Certifies spectral good/bad behaviour       |
| Explicit \\(R\\) for every claimed good point        | Verifies actual lifting                     |
| Exact rank of \\([L_0;R]\\)                          | Verifies full-row-rank feasibility          |

A random seed alone is not sufficient for a mathematical paper. Include the exact matrices or a machine-readable supplementary file that reproduces them.

## 6.2 Keep the general theorem and examples logically separate

I would structure the exposition so that the reader can distinguish:

- theorem;
- proof;
- exact example;
- conjecture;
- computational observation.

The five-instance table should not be used to establish a component theorem. The six-instance \\(e=1\\) table should not be used to establish that the mixed phenomenon is universally robust.

Instead, use the tables to illustrate how the general incidence and spectral theorems behave in concrete cases.

This is entirely acceptable in a research paper.

You do not need to prove a complete arbitrary-dimensional component bound before writing the paper. The hyperplane vector-bundle theorem proposed above would, however, strengthen the paper considerably if you can verify and prove it cleanly.

# 7. Question 6: What should be done next?

I would change the priority order in the report.

## Priority 1 — Prove the hyperplane vector-bundle decomposition theorem

This is the most valuable immediate step.

Prove rigorously that, for \\(k=\omega+1\\):

1. The projective base is \\(\mathbb P(K_0)\\).
2. The rank of the linear constraint on each row of \\(R\\) is \\(\rank[v,Av]\\).
3. The rank-one locus is the union of the relevant projective eigenspaces.
4. The remaining base is irreducible and open.
5. The \\(R\\)-solution spaces form vector bundles on the constant-rank pieces.
6. The conditions \\(\rank H=\omega\\) and \\(\rank[L_0;R]=q\\) are open.
7. Every nonempty lifted piece is irreducible.

This would replace the report's proposed component-counting argument with a theorem tailored to the actual observer problem.

I would also verify the theorem against all eleven examples in the five-instance and six-instance tables.

## Priority 2 — Establish the generic spectral test on each vector-bundle component

For each irreducible component \\(X\\), the question is whether

\\[ \gcd(\omega\text{-minors of }\lambda H-H_A)=1 \\]

over \\(\mathbb C(X)[\lambda]\\).

The component theorem tells you which function fields to use.

The next step is to construct a bounded-degree polynomial certificate for the generic gcd condition and analyse its exact computational complexity.

I would compare two approaches:

- Bézout certificates based on maximal minors;
- polynomial generalized-inverse certificates of the form \\(PYP=P\\).

The second is especially attractive because it avoids explicitly enumerating all maximal minors.

## Priority 3 — Formalise the invariant eigenspace obstruction

Include the necessary condition

\\[ \dim(K\cap\ker(A-\lambda I))\leq k-\omega \qquad\forall\lambda. \\]

Also include the all-bad sufficient condition

\\[ \dim(K\cap\ker A)>k-\omega. \\]

These are simple, invariant, and independent of the choice of basis \\(N_K\\).

They should be proved before attempting more elaborate component classifications.

## Priority 4 — Extend to \\(c=k-\omega>1\\)

Use

\\[ \mathcal D_s = \\{V\in\operatorname{Gr}(c,K_0):\dim(V+AV)\leq s\\}. \\]

I would begin with \\(c=2\\), not arbitrary \\(c\\).

For \\(c=2\\), the rank of the map

\\[ V\oplus V\longrightarrow\mathbb C^n,\qquad (v,w)\longmapsto v+Aw \\]

ranges from 2 to 4. Its lowest-rank locus is the set of \\(A\\)-invariant two-dimensional subspaces. The intermediate loci correspond to one-dimensional intersections \\(V\cap A^{-1}V\\).

This is a tractable first Grassmannian case.

## Priority 5 — Real feasibility

Do not ignore the real-point issue, but do not let it block the complex theory.

For a real component that is a projective linear space or a vector bundle over one, the real points are Zariski dense whenever the component has a real point. Therefore a nonempty Zariski-open good locus intersects its real points.

For a non-real eigenvalue component, there may be no real points at all.

Thus, in the hyperplane case, the real-point question can be handled component by component:

- retain real-eigenvalue components;
- examine the real locus of the non-eigenvector component;
- use Zariski density of the real points on the corresponding real linear/vector-bundle component.

For general Grassmannian degeneracy loci, the real-point problem may be more complicated.

## Priority 6 — Assemble the paper

I would begin drafting after Priorities 1–3 are stable. Do not wait for the complete \\(c>1\\) classification.

# 8. Suggested paper structure

I would now organise the paper as follows.

### Section 1. Problem formulation and exact reduction

Define

\\[ K=\ker[C;CA],\qquad N=N_K, \\]

and derive the compressed matrices

\\[ H=LN,\qquad H_A=LAN. \\]

Establish the equivalence of (5a) with

\\[ \ker H\subseteq\ker H_A. \\]

Then introduce the induced map on \\(W=\operatorname{im}H\\) and the spectral eigenvector criterion.

One notation correction is essential here. The report writes \\(Z=(A;B)\\) and says the bottom \\(\omega\\) rows form \\(B\\). That is dimensionally incorrect in general.

The correct decomposition, after choosing

\\[ \mathbb C^q=W\oplus W', \\]

is

\\[ \boxed{ Z= \begin{bmatrix} A_W\\\B\_\perp \end{bmatrix}, \qquad A_W\in\mathbb C^{\omega\times\omega},\quad B\_\perp\in\mathbb C^{(q-\omega)\times\omega}. } \\]

Then

\\[ \boxed{ \text{bad} \iff \exists\\,0\ne y\in\ker B\_\perp,\quad A_Wy\in\mathbb Cy. } \tag{8.1} \\]

The report should avoid using \\(A\\) for both the original state matrix and the block of the induced map. Use, for example, \\(A_W\\) and \\(B\_\perp\\).

### Section 2. Projective compressed admissibility

Present the corrected criterion:

\\[ E+F_0\subseteq S, \\]

\\[ \widetilde E_S+X_S=\mathbb C^\omega, \\]

\\[ m\geq\omega-e. \\]

Explain explicitly that this is a compressed-pair criterion, not yet a full-row-rank lift theorem.

### Section 3. Full-row-rank lifting

State the affine lifting lemma in its general form.

The assumption

\\[ \rank L_0=r \\]

is necessary. If it fails, full row rank of \\([L_0;R]\\) is impossible.

### Section 4. Lifted incidence and genericity

Prove the projective properness argument and the generic determinant-divisor criterion.

### Section 5. Hyperplane vector-bundle decomposition

This is where I would put the new theorem:

\\[ \\#\\{\text{nonempty lifted components}\\}\leq\delta+1. \\]

It is potentially one of the most useful structural results in the paper.

### Section 6. All-bad obstructions and low-dimensional classifications

Include:

- the restricted \\(d=2,U_0=0\\) theorem;
- the \\(Y\\)-criterion;
- the invariant eigenspace obstruction;
- the exact \\(q=2\\) criterion.

### Section 7. Exact examples

Present the five-instance and six-instance tables with complete certificates.

### Section 8. General codimension and open problems

Introduce

\\[ \mathcal D_s = \\{V\in\operatorname{Gr}(c,K_0):\dim(V+AV)\leq s\\} \\]

as the general geometric problem.

State the real-point and complexity questions separately.

# 9. References and mathematical connections

The report's choice of determinantal geometry is correct, but I would add one more direction.

| Subject                              | Why it is relevant                                                                  | Suggested reference                                                      |
| ------------------------------------ | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Determinantal varieties              | Rank strata defined by minors                                                       | Bruns–Vetter, Determinantal Rings (1988)                                 |
| Degeneracy loci                      | Bundle-map formulation and rank conditions                                          | Fulton, Intersection Theory, 2nd ed. (1998), Chapter 14                  |
| Grassmannians and Schubert varieties | Incidence conditions involving variable subspaces                                   | Fulton, Young Tableaux (1997)                                            |
| Invariant-subspace varieties         | The lowest-rank locus \\(AV\subseteq V\\)                                           | Literature on Springer fibres and invariant subspaces                    |
| Quiver Grassmannians                 | Subspaces stable under a linear operator, viewed as modules over \\(\mathbb C[x]\\) | Caldero–Reineke, “On the quiver Grassmannian in the acyclic case” (2008) |
| Polynomial matrix normal forms       | Generic determinant-divisor and certificate computations                            | Kannan (1985); Storjohann–Labahn (1995)                                  |

I would not claim that the general loci \\(\mathcal D_s\\) are Schubert varieties. They are special determinantal degeneracy loci on a Grassmannian. The invariant-subspace case is closely related to quiver Grassmannians, but the intermediate-rank cases require their own analysis.

# 10. Final answers to the six questions

| Question                                      | My conclusion                                                                                                                                                                          |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Q1. Corrected theorem and lifting lemma?      | Yes, with \\(\omega=k-1\\) stated for the projective parametrisation. The lifted incidence is the right object.                                                                        |
| Q2. Determinantal reformulation and examples? | Correct. Keep the counterexample and exact tables; retract the general linearity claim.                                                                                                |
| Q3. \\(e>0\\), \\(d=1\\), \\(d=2\\)?          | The examples support the reported patterns but not universal claims. The \\(Y\\)-criterion is correct; simplify its sufficient condition and add the invariant eigenspace obstruction. |
| Q4. Main \\(q1\\) direction?                  | For hyperplanes, use the eigenvector/vector-bundle decomposition. For general codimension, study \\(\mathcal D_s\\) on Grassmannians. Do not begin with a hardness reduction.          |
| Q5. Keep the examples?                        | Yes. They are valuable exact examples, provided every claimed good point has an explicit full-row-rank lift and every spectral claim has an exact certificate.                         |
| Q6. What next?                                | Prove the hyperplane vector-bundle theorem, establish the generic spectral test, formalise the eigenspace obstruction, then study \\(c=2\\). Assemble the paper after these steps.     |

## Final verdict

The general framework is now coherent

The corrected projective theorem, affine lifting lemma, and properness-based genericity argument fit together. The \\(e>0\\) examples also show that the low-dimensional spectral behaviour is richer than the \\(U_0=0\\) special case.

A sharper hyperplane component theorem appears available

The key observation is

\\[ Rv=0,\qquad RAv=0, \\]

with \\(v=N\sigma^\top\\). The fibre in \\(R\\) is linear, and its dimension changes only when \\(v\\) is an eigenvector of \\(A\\). This yields the vector-bundle decomposition and the bound

\\[ \boxed{\\#\text{ lifted components}\leq\delta+1} \\]

for \\(k=\omega+1\\).

For \\(\delta=2\\), there are at most three such components.

General codimension remains open

For \\(k-\omega>1\\), the base geometry becomes

\\[ \\{V\in\operatorname{Gr}(k-\omega,K_0): \dim(V+AV)\leq s\\}. \\]

This is the correct general component-decomposition problem. Its geometry may be substantially more complicated, and neither a polynomial algorithm nor a hardness result has been established.

My strongest recommendation is to revise the main research question before proceeding. The hyperplane case should no longer be treated as an open-ended determinantal component-enumeration problem. It has a concrete eigenvector and vector-bundle structure. The genuine generalisation is the Grassmannian geometry of \\(V+AV\\), and that is where the next major theoretical effort should go.

I would prove that hyperplane theorem first, verify it against all existing examples, and then make \\(c=2\\) the next controlled generalisation. This offers a realistic route to a rigorous paper without prematurely claiming either polynomial-time solvability or \\(\exists\mathbb R\\)-hardness.