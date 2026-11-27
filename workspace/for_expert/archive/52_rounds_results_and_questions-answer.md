# Comprehensive mathematical audit of Report 52

The new report contains several important advances. In particular, the \\(d=1\\) example is a convincing illustration of how a jump in compatibility-fibre dimension can create mixed spectral behaviour, and the \\(d=2\\) example points toward a stronger structural theorem under an additional hypothesis.

There is, however, one significant mathematical error in the draft projective theorem, and one important ambiguity in the interpretation of the \\(q=2,\omega=1\\) block criterion. The latter can be resolved exactly. The former needs to be corrected before the projective theorem is used as a foundation for further work.

My main conclusions are:

1. Question 1: The \\(d=1\\) mixed-stratum construction is correct at the compressed compatibility level. The exceptional point is precisely where the rank of the compatibility map drops. The fibre-dimension jump is real and must be retained in the theorem.
2. Question 2: The distinction is not determined by \\(d\\) alone. There is a useful restricted theorem: for \\(k=3,\omega=2,q=3,d=2\\) and \\(U_0=0\\), every admissible point is bad. This is stronger than the individual example.
3. Question 3: The \\(q=2,\omega=1\\) discrepancy is a block-identification error. The transverse block is determined by the coefficient of \\(V_0\\), not the coefficient of \\(g_2\\).
4. Question 4: The formula for \\(\dim X_S\\) is correct. But the claimed equivalence between admissibility and \\(X_S\nsubseteq E\\) is false when \\(\dim E<\omega-1\\). The correct condition is a full spanning-rank equality.
5. Question 5: The rectangular determinantal-divisor bridge lemma is correct. The Storjohann–Labahn rectangular Hermite algorithm is suitable, but a deterministic route is also available through square embedding and Kannan's polynomial-time Hermite-form algorithm.
6. Question 6: Resolve the \\(q=2\\) criterion first, prove the restricted \\(d=2\\) theorem second, repair the projective theorem third, and assemble the paper only after those steps.

52_rounds_results_and_questions.md

## 1. Question 1: the \\(d=1\\) mixed-stratum theorem

Compressed-fibre argument is correct

I agree with the central conclusion of II.1, subject to one qualification concerning the lifting back to a full-row-rank observer matrix.

The data are

\\[ k=3,\qquad q=3,\qquad \omega=2,\qquad d=1, \\]

and

\\[ E=U_0=0,\qquad V_0=(0,a,b)\ne0,\qquad Z_1=0,\qquad Z_2=e_1. \\]

The compatibility condition is

\\[ xZ_1+yZ_2=0. \\]

Since \\(Z_1=0\\) and \\(Z_2=e_1\\), it becomes

\\[ y_1=0. \\]

The candidate row space is

\\[ S=\ker\sigma,\qquad [\sigma]\in\mathbb P^2,\qquad \sigma V_0=0. \\]

The projective condition \\(\sigma V_0=0\\) indeed defines a projective line:

\\[ \mathcal B=\\{[\sigma]\in\mathbb P^2:\sigma V_0=0\\} \cong\mathbb P^1. \\]

### 1.1 The open stratum is entirely bad

Suppose

\\[ [\sigma]\ne[1:0:0]. \\]

Then

\\[ S\ne\\{y_1=0\\}. \\]

Both \\(S\\) and \\(\\{y_1=0\\}\\) are two-dimensional subspaces of \\(\mathbb C^3\\). Since they are distinct,

\\[ \dim\left(S\cap\\{y_1=0\\}\right)=1. \\]

Moreover, \\(V_0\\) belongs to both subspaces:

\\[ V_0\in S,\qquad (V_0)\_1=0. \\]

As \\(V_0\ne0\\), it follows that

\\[ S\cap\\{y_1=0\\}=\operatorname{span}\\{V_0\\}. \\]

Every compatible \\(y_i\\) must belong to this intersection. Consequently,

\\[ y_i\in\operatorname{span}\\{V_0\\}. \\]

At \\(\lambda=0\\), the rows of the pencil are

\\[ -V_0,\qquad -y_1,\qquad -y_2. \\]

They all belong to the same one-dimensional space. Therefore

\\[ \rank(-H_A)\le1<2. \\]

This proves that the entire open stratum is bad.

There is no missing case here. The only hyperplane \\(S\\) equal to \\(\\{y_1=0\\}\\) is represented by the projective point \\([1:0:0]\\). Every other point of the projective line belongs to the open stratum just considered.

### 1.2 The exceptional-point constructions are sound

At

\\[ [\sigma]=[1:0:0], \\]

we have

\\[ S=\operatorname{span}\\{e_2,e_3\\}. \\]

The compatibility condition \\(y_1=0\\) now imposes no additional restriction on \\(y\in S\\). Thus the compatible \\(y\\)-space jumps from dimension one to dimension two.

Use the ordered coordinates \\((e_2,e_3)\\).

#### Case A: \\(ab\ne0\\)

Choose

\\[ x_1=e_2,\quad x_2=e_2+e_3,\qquad y_1=y_2=e_2. \\]

The pencil rows are

\\[ (-a,-b),\quad (\lambda-1,0),\quad (\lambda-1,\lambda). \\]

Their three \\(2\times2\\) minors are

\\[ m\_{12}=b(\lambda-1), \\]

\\[ m\_{13}=(b-a)\lambda-b, \\]

\\[ m\_{23}=\lambda(\lambda-1). \\]

The first and third have gcd \\(\lambda-1\\), up to a nonzero constant. But

\\[ m\_{13}(1)=-a\ne0. \\]

Therefore

\\[ \gcd(m\_{12},m\_{13},m\_{23})=1. \\]

The pencil has full column rank for every finite \\(\lambda\\).

#### Case B: \\(a=0\\) or \\(b=0\\)

Because \\(V_0\ne0\\), these cases do not include \\(a=b=0\\).

Choose

\\[ x_1=e_2,\quad x_2=e_3,\qquad y_1=e_3,\quad y_2=e_2. \\]

The minors are

\\[ m\_{12}=a+b\lambda, \\]

\\[ m\_{13}=-a\lambda-b, \\]

\\[ m\_{23}=\lambda^2-1. \\]

If \\(a=0\\), then

\\[ m\_{13}=-b \\]

is a nonzero constant.

If \\(b=0\\), then

\\[ m\_{12}=a \\]

is a nonzero constant.

In either case the gcd is a unit.

Thus the exceptional point contains a good compatible choice.

### 1.3 The fibre-dimension jump is not a defect; it explains the mixed behaviour

This is the most interesting part of the example.

For a generic \\(S\\), the compatible \\(y\\)-space is

\\[ S\cap\ker(e_1^{\mathsf T}) =\operatorname{span}\\{V_0\\}. \\]

At the exceptional point,

\\[ S=\ker(e_1^{\mathsf T}), \\]

so the compatible \\(y\\)-space becomes all of \\(S\\).

In terms of the projective theorem's matrices,

\\[ Q=B^{\mathsf T}Z_2, \\]

the generic stratum has

\\[ \rank Q=1, \\]

whereas the exceptional point has

\\[ Q=0,\qquad \rank Q=0. \\]

So the projective line is not one constant-rank compatibility stratum. It is the union of:

- an open rank-one stratum, entirely bad;
- an exceptional rank-zero stratum, containing good points.

This explains why the mixed behaviour does not contradict the generic bad/good dichotomy on irreducible constant-rank strata.

The distinction is important. If one applied the genericity theorem to the entire projective line as though it were one constant-rank admissible family, one would overlook the fibre jump. The correct genericity argument applies after stratification.

### 1.4 One remaining qualification: lifting to the original \\(R\\)-space

The calculations prove the compressed statement about compatible pairs \\((x_i,y_i)\\). To establish the original observer synthesis theorem, one must also verify that the chosen compatible pairs lift to an \\(R\\) for which

\\[ L=\begin{bmatrix}L_0\\\R\end{bmatrix} \\]

has full row rank.

Compatibility guarantees that the prescribed restrictions to \\(K\\) and \\(AK\\) are consistent. It does not, by itself, prove full row rank of the resulting \\(L\\).

I recommend adding a separate lifting lemma:

> Full-row-rank lifting lemma. Given a compatible collection of prescribed pairs \\((RN_K,RAN_K)\\), characterize when the affine space of all \\(R\\) realizing these pairs contains a matrix for which \\([L_0;R]\\) has full row rank.

For the particular example, the authors should verify this condition explicitly. If it has already been checked in the original data, report it as an additional exact verification.

Verdict on Q1: the mixed-stratum proof is sound at the compressed level. The dimension jump is the mechanism, not an obstacle. The full-row-rank lifting should be recorded separately.

## 2. Question 2: what distinguishes \\(d=1\\) from \\(d=2\\)?

The answer is not simply the numerical value of

\\[ d=\dim\ker T. \\]

The more informative quantities are the ranks of the compatibility maps after restricting to \\(S\\), particularly

\\[ \rank Q=\rank(B^{\mathsf T}Z_2), \\]

and the dimension of the corresponding compatible first-coordinate space \\(X_S\\).

There is, however, a useful theorem for the special \\(d=2\\) regime represented by II.2.

### 2.1 A restricted \\(d=2\\) all-bad theorem

The following is a stronger statement than the particular \\(n=7\\) example.

Proposition. Suppose

\\[ k=3,\qquad \omega=2,\qquad q=3,\qquad d=2, \\]

and

\\[ U_0=L_0N_K=0. \\]

Then every admissible compressed point is spectrally bad.

Here admissibility means

\\[ \rank H=2,\qquad \ker H\subseteq\ker H_A. \\]

The proposition concerns the spectral property of every admissible point; it does not assert that an admissible point necessarily exists.

#### Proof

First, the projection of \\(\ker T\\) onto its second coordinate is injective. Indeed, if

\\[ (v,0)\in\ker T, \\]

then

\\[ v+A0=0, \\]

so \\(v=0\\).

Since \\(d=2\\), it follows that

\\[ \rank Z_2=2. \\]

Thus the left kernel of \\(Z_2\\) is one-dimensional. Choose a nonzero row vector \\(\ell\\) such that

\\[ \ell Z_2=0. \\]

The defining relation for the basis of \\(\ker T\\) is

\\[ N_KZ_1+AN_KZ_2=0. \\]

Consequently,

\\[ \begin{aligned} V_0Z_2 &=L_0AN_KZ_2\\\ &=-L_0N_KZ_1\\\ &=-U_0Z_1\\\ &=0. \end{aligned} \\]

Therefore

\\[ V_0\in\ker(\\,\cdot\\, Z_2) =\operatorname{span}\\{\ell\\}. \tag{2.1} \\]

There are two cases.

Case 1: \\(V_0=0\\).

Because \\(U_0=0\\), the compressed matrices have the form

\\[ H=\begin{bmatrix}0\\\X\end{bmatrix}, \qquad H_A=\begin{bmatrix}0\\\Y\end{bmatrix}, \\]

where \\(X\\) is a \\(2\times3\\) matrix of rank two.

Choose coordinates on the row space \\(S\\). In those coordinates, the two nonzero rows of the pencil form a square \\(2\times2\\) pencil

\\[ \lambda X_S-Y_S, \\]

with \\(X_S\\) invertible.

Its determinant has degree two, because its leading coefficient is

\\[ \det X_S\ne0. \\]

Over \\(\mathbb C\\), this determinant has a root. At that root, the pencil has rank at most one. The first row is identically zero, so the original \\(3\times3\\) pencil is bad.

Case 2: \\(V_0\ne0\\).

By (2.1), \\(V_0\\) is a nonzero multiple of \\(\ell\\). Every admissible row space \\(S\\) contains \\(V_0\\), hence

\\[ \ell\in S. \\]

Choose a \\(3\times3\\) matrix \\(\bar A\\) satisfying

\\[ \bar A Z_2=-Z_1. \\]

Such a matrix exists because the columns of \\(Z_2\\) are linearly independent.

For \\(x,y\in S\\), compatibility is equivalent to

\\[ xZ_1+yZ_2=0 \iff (y-x\bar A)Z_2=0 \iff y-x\bar A\in\operatorname{span}\\{\ell\\}. \tag{2.2} \\]

Since \\(\ell\in S\\), the existence of a compatible \\(y\in S\\) for a given \\(x\in S\\) is equivalent to

\\[ x\bar A\in S. \\]

Admissibility requires \\(X_S=S\\). Hence

\\[ S\bar A\subseteq S. \\]

The induced operator on

\\[ S/\operatorname{span}\\{\ell\\} \\]

is an endomorphism of a one-dimensional complex vector space. It is therefore multiplication by some scalar \\(\mu\\).

Thus, for every \\(x\in S\\),

\\[ \mu x-x\bar A\in\operatorname{span}\\{\ell\\}. \tag{2.3} \\]

For every compatible pair \\((x_i,y_i)\\), equation (2.2) gives

\\[ y_i-x_i\bar A\in\operatorname{span}\\{\ell\\}. \\]

Combining with (2.3),

\\[ \mu x_i-y_i\in\operatorname{span}\\{\ell\\}. \\]

The top row of \\(\mu H-H_A\\) is

\\[ -V_0\in\operatorname{span}\\{\ell\\}. \\]

All three rows therefore lie in the same one-dimensional space:

\\[ \rank(\mu H-H_A)\le1<2. \\]

This proves the proposition. \\(\square\\)

### 2.2 What this theorem says about the reported \\(d=2\\) example

The II.2 example has \\(U_0=0\\). The all-bad conclusion therefore follows from the proposition without needing to enumerate the two admissible Grassmannian points.

The explicit two-point computation remains valuable as a transparent illustration, but the proposition explains the structural reason for the phenomenon.

It also explains why the \\(d=1\\) family can behave differently.

### 2.3 The key distinction is the left kernel of \\(Z_2\\)

For \\(k=3\\):

- if \\(d=1\\), then \\(\rank Z_2=1\\), so the left kernel of \\(Z_2\\) has dimension two;
- if \\(d=2\\), then \\(\rank Z_2=2\\), so the left kernel has dimension one.

In the \\(d=1\\) family, there is a two-dimensional compatibility subspace. A candidate \\(S\\) can coincide with it, causing \\(\rank Q\\) to drop from one to zero. This exceptional rank drop permits the good construction.

In the \\(d=2,\ U_0=0\\) case, \\(V_0\\) is forced into the one-dimensional left kernel of \\(Z_2\\). Every admissible \\(S\\) must contain that line. The induced operator on the one-dimensional quotient then necessarily has an eigenvalue, which gives a common rank-drop value for the entire compatible pencil.

This is the genuine mechanism.

Recommendation: prove the restricted theorem above. Do not claim that all \\(d=2\\) strata are bad without the \\(U_0=0\\) hypothesis. When \\(U_0\ne0\\), the identity \\(V_0Z_2=0\\) need not hold, and the argument can fail.

## 3. Question 3: the exact \\(q=2,\omega=1\\) criterion

Discrepancy resolved

This is a straightforward but important block-identification error.

The cleanest way to state the answer is invariantly.

Let

\\[ q=2,\qquad \omega=1. \\]

Then \\(W=\operatorname{im}H\\) is a line in \\(\mathbb C^2\\), and

\\[ Z:W\longrightarrow\mathbb C^2 \\]

is the induced map.

The bad condition is

\\[ \exists\\,0\ne w\in W,\qquad Z(w)\in\mathbb Cw. \\]

Since \\(W\\) is one-dimensional, every nonzero \\(w\in W\\) spans it. Therefore

\\[ \boxed{ \text{good} \iff Z(W)\not\subseteq W. } \\]

Equivalently, the induced quotient map

\\[ \overline Z:W\longrightarrow\mathbb C^2/W \\]

must be nonzero.

If \\(w\\) spans \\(W\\), this is

\\[ \boxed{ \text{good} \iff \det[w,Z(w)]\ne0. } \tag{3.1} \\]

This is the simplest exact \\(q=2,\omega=1\\) criterion.

### 3.1 Applying it when \\(U_0=0\\)

Write

\\[ H=\begin{pmatrix}0\\\h\end{pmatrix}, \qquad H_A=\begin{pmatrix}V_0\\\g_2\end{pmatrix}, \\]

where \\(h\ne0\\).

The well-definedness condition

\\[ \ker H\subseteq\ker H_A \\]

implies that both \\(V_0\\) and \\(g_2\\) are multiples of \\(h\\). Write

\\[ V_0=\alpha h,\qquad g_2=\beta h. \\]

Then

\\[ W=\operatorname{span}\\{e_2\\}. \\]

For \\(w=(0,t)\in W\\), the induced map is

\\[ Z(0,t)=(\alpha t,\beta t). \\]

Use the ordered target decomposition

\\[ \mathbb C^2 = \underbrace{\operatorname{span}\\{e_2\\}}\_{W} \oplus \underbrace{\operatorname{span}\\{e_1\\}}\_{W'}. \\]

In this order,

\\[ Z(w)=\beta t\\,e_2+\alpha t\\,e_1. \\]

Thus the block decomposition is

\\[ A=\beta,\qquad B=\alpha. \\]

The block criterion says

\\[ \text{good}\iff B\ne0. \\]

Therefore

\\[ \boxed{ \text{good}\iff \alpha\ne0, } \\]

not \\(\beta\ne0\\).

The coefficient of \\(g_2\\) is the coefficient in the \\(W\\)-direction. It contributes to the \\(A\\)-block. The coefficient of \\(V_0\\) is the component transverse to \\(W\\), and that is the \\(B\\)-block.

Consequently, the reported witness with \\(\beta=0\\) can indeed pass (5b), provided \\(\alpha\ne0\\). There is no contradiction with the block criterion.

### 3.2 General \\(q=2\\) classification by \\(\omega\\)

Over \\(\mathbb C\\), the three possible compressed ranks have a simple description:

| \\(\omega\\) | Spectral criterion                           |
| ------------ | -------------------------------------------- |
| \\(0\\)      | Automatically good, subject to admissibility |
| \\(1\\)      | Good iff \\(Z(W)\not\subseteq W\\)           |
| \\(2\\)      | Always bad                                   |

For \\(\omega=2\\), \\(q=\omega\\), so the induced map is a square \\(2\times2\\) complex matrix. Every such matrix has an eigenvector. Hence every point is bad.

This yields an exact order-two feasibility statement:

\\[ \boxed{ q=2\text{ is feasible} \iff \begin{cases} \text{an admissible full-row-rank point with }\omega=0\text{ exists},\\\ \text{or}\\\ \text{an admissible full-row-rank point with }\omega=1 \text{ and }\overline Z\ne0\text{ exists}. \end{cases} } \\]

The \\(\omega=2\\) stratum cannot contribute.

### 3.3 Is \\(q\_{\min}\\) always determined by the lowest feasible \\(\omega\\)?

No such conclusion follows from the current results.

The order \\(q\\) is fixed first, and the feasible set is a union over possible values of \\(\omega\\). The block criterion decides the spectral property within each rank stratum. It does not establish a monotonicity theorem relating different \\(\omega\\)-strata.

For a fixed \\(q\\), a lower \\(\omega\\)-stratum might be empty while a higher one is nonempty, or vice versa. Even if a particular \\(\omega\\) is feasible, this does not prove that all lower values are feasible.

The correct order-minimisation procedure is therefore:

1. Fix \\(q\\).
2. Enumerate the possible compressed ranks \\(\omega\\).
3. Test admissibility and full-row-rank lifting in each stratum.
4. Apply the corresponding spectral criterion.
5. Declare \\(q\\) feasible if at least one stratum contributes a good point.

The four examples demonstrate precisely why one cannot infer order infeasibility from the behaviour of the \\(q=3,\omega=2\\) stratum.&#x20;

52_rounds_results_and_questions.md



## 4. Question 4: audit of the projective constrained theorem

This section contains the most important correction to Report 52.

### 4.1 The formula for \\(\dim X_S\\) is correct

Let \\(B\in\mathbb C^{k\times\omega}\\) have columns forming a basis of \\(S\\). A row vector in \\(S\\) has the form

\\[ x=aB^{\mathsf T},\qquad a\in\mathbb C^{1\times\omega}. \\]

Define

\\[ P=B^{\mathsf T}Z_1,\qquad Q=B^{\mathsf T}Z_2. \\]

Compatibility requires

\\[ aP+bQ=0 \\]

for some \\(b\in\mathbb C^{1\times\omega}\\). Thus

\\[ X_S=\\{a:aP\in\operatorname{row}Q\\}. \\]

Consider the linear map

\\[ \phi_S: \mathbb C^{1\times\omega} \longrightarrow \mathbb C^{1\times d}/\operatorname{row}Q, \qquad a\longmapsto aP+\operatorname{row}Q. \\]

Its kernel is \\(X_S\\). Its image has dimension

\\[ \dim\frac{\operatorname{row}P+\operatorname{row}Q} {\operatorname{row}Q}. \\]

This dimension equals

\\[ \rank\begin{bmatrix}P\\\Q\end{bmatrix}-\rank Q. \\]

By rank-nullity,

\\[ \boxed{ \dim X_S = \omega- \left( \rank\begin{bmatrix}P\\\Q\end{bmatrix} -\rank Q \right). } \tag{4.1} \\]

This is correct.

On a Grassmannian chart where \\(B\\) varies algebraically, constant-rank conditions on \\(Q\\) and the stacked matrix \\([P;Q]\\) make the kernel spaces \\(X_S\\) vary as vector subbundles. This is the right foundation for a constant-rank stratification.

### 4.2 The admissibility condition in II.4 is not correct as stated

The report says that

\\[ E+X_S=S \\]

is the complement of the closed condition

\\[ X_S\subseteq E. \\]

That is false in general.

The exact identity is

\\[ \dim(E+X_S) = \dim E+\dim X_S-\dim(E\cap X_S). \\]

Writing \\(e=\dim E\\), the correct admissibility condition is

\\[ \boxed{ e+\dim X_S-\dim(E\cap X_S)=\omega. } \tag{4.2} \\]

The condition

\\[ X_S\nsubseteq E \\]

only says that \\(E+X_S\\) is strictly larger than \\(E\\). It does not say that it equals \\(S\\).

For example, take

\\[ S=\mathbb C^3,\qquad E=\operatorname{span}\\{e_1\\},\qquad X_S=\operatorname{span}\\{e_2\\}. \\]

Then

\\[ X_S\nsubseteq E, \\]

but

\\[ E+X_S=\operatorname{span}\\{e_1,e_2\\} \ne S. \\]

The complement-of-\\(X_S\subseteq E\\) formulation is valid only when

\\[ \dim E=\omega-1, \\]

so that any strict enlargement of \\(E\\) inside \\(S\\) must equal \\(S\\).

This is precisely why the report's concern about \\(r>1\\) matters.

### 4.3 The correct stratification repairs the issue

On a constant-rank stratum, both

\\[ \dim X_S \quad\text{and}\quad \dim E \\]

are fixed.

Further stratify by

\\[ t=\dim(E\cap X_S). \\]

Then (4.2) becomes the numerical equality

\\[ \boxed{ e+\dim X_S-t=\omega. } \tag{4.3} \\]

This gives an exact algebraic criterion on the stratum.

The locus where

\\[ \dim(E\cap X_S)\le t \\]

is a determinantal rank condition, so the corresponding exact-dimension loci are constructible (locally closed after the usual rank stratification). The spanning condition is therefore an algebraic rank condition, not merely the complement of \\(X_S\subseteq E\\).

I recommend replacing the current paragraph in II.4 with (4.2)–(4.3).

### 4.4 A second missing condition: the number of bottom rows

There are \\(m=q-r\\) bottom rows available to span \\(S/E\\).

Since

\\[ \dim(S/E)=\omega-e, \\]

a necessary condition is

\\[ \boxed{ m\ge\omega-e. } \tag{4.4} \\]

Together, the conditions are:

\\[ E+F_0\subseteq S, \\]

\\[ E+X_S=S, \\]

\\[ \omega-e\le m. \\]

These are the Grassmannian-level nonemptiness conditions from the earlier criterion. They should appear explicitly in the projective theorem.

### 4.5 The projective base must incorporate the fixed rows

For

\\[ S=\ker\sigma,\qquad [\sigma]\in\mathbb P^{k-1}, \\]

the fixed-row inclusion

\\[ E+F_0\subseteq S \\]

means

\\[ \sigma|\_{E+F_0}=0. \\]

Thus the relevant projective parameter space is

\\[ \mathbb P\big((E+F_0)^\perp\big), \\]

not necessarily the entire \\(\mathbb P^{k-1}\\).

This is a simple but important reduction of the search space.

### 4.6 A third issue: distinguish the Grassmannian base from the total incidence space

The spectral pencil is not determined by \\(S\\) alone. It also depends on the actual compatible bottom-row pairs

\\[ (x_i,y_i). \\]

Therefore the relevant parameter space for the spectral genericity theorem must include these choices. More precisely, define a total incidence space containing:

- the candidate \\(S\\);
- compatible bottom-row pairs;
- the spanning condition that makes \\(\operatorname{row}H=S\\);
- the full-row-rank condition on \\(L\\), if the theorem concerns the original observer problem.

Then stratify this total incidence space using the compatibility ranks.

The distinction matters because the \\(d=1\\) example has a projective base \\(\mathbb P^1\\) but a jump in the compatible-pair fibre dimension. A generic-gcd computation over the function field of the base alone cannot decide whether the total fibre contains a good member.

The correct procedure is:

1. Stratify the projective base by the ranks of the compatibility maps.
2. Construct the compatible-pair incidence space over each stratum.
3. Impose the spanning and full-row-rank conditions.
4. Decompose the resulting total incidence space into irreducible components.
5. Apply the spectral genericity theorem to each component.

This is the precise formulation needed to avoid conflating the base geometry with the full synthesis parameter space.

### 4.7 Is the closedness/dichotomy argument valid?

Yes, with that clarification.

Let \\(X\\) be an irreducible locally closed component of the total admissible incidence space, with

\\[ \rank H=\omega \\]

everywhere.

Homogenise the pencil:

\\[ P(x;\alpha,\beta)=\alpha H(x)-\beta H_A(x), \qquad [\alpha:\beta]\in\mathbb P^1. \\]

The rank-drop condition is defined by the vanishing of all \\(\omega\times\omega\\) minors. It is closed in

\\[ X\times\mathbb P^1. \\]

At the point at infinity \\([1:0]\\),

\\[ P(x;1,0)=H(x), \\]

which has rank \\(\omega\\). Hence the bad incidence set has no point at infinity.

The projection

\\[ X\times\mathbb P^1\longrightarrow X \\]

is proper, so the bad locus is closed in \\(X\\).

Consequently, if \\(X\\) is irreducible, exactly one of the following holds:

- every point of \\(X\\) is bad;
- the good points form a nonempty Zariski-open dense subset of \\(X\\).

The generic determinantal divisor over \\(\mathbb C(X)\\) decides which case occurs.

This is sound. The main missing work is not the projective closedness argument; it is constructing the correct total incidence space, including the spanning and full-row-rank conditions, and identifying its irreducible components.

### 4.8 Real-point issue

The report correctly identifies this as an open issue.

A complex Zariski-open subset of a complex irreducible variety need not contain a real point. Thus a complex generic-good theorem does not automatically imply real feasibility for real input data.

For the real synthesis problem, one must either:

- prove that the relevant real points are Zariski dense in the component;
- identify a nonsingular real point and use local real geometry;
- or directly decide real-point feasibility using real algebraic geometry.

This should be kept distinct from the complex generic-gcd theorem.

Verdict on Q4: the dimension formula is correct, and the closedness/dichotomy argument is correct on the appropriate total incidence components. But the current admissibility discussion has a genuine error: \\(X_S\nsubseteq E\\) is not sufficient. Replace it by the full spanning-rank condition.

## 5. Question 5: rectangular determinantal divisor and Hermite form

Bridge lemma is correct

### 5.1 The algebraic bridge lemma

Suppose

\\[ P\in\mathbb Q[\lambda]^{q\times k} \\]

has full column normal rank \\(k\\).

If its rectangular row Hermite form is

\\[ UP= \begin{pmatrix} D\\\0 \end{pmatrix}, \\]

where \\(U\\) is unimodular and \\(D\\) is a \\(k\times k\\) triangular matrix, then

\\[ \boxed{ \Delta_k(P)=\det D } \\]

up to a nonzero constant.

The proof is correct.

By Cauchy–Binet, every maximal minor of \\(UP\\) is a polynomial combination of the maximal minors of \\(P\\). Conversely, applying the same argument to \\(U^{-1}\\) gives the reverse ideal inclusion. Thus the two collections generate the same ideal in \\(\mathbb Q[\lambda]\\).

But

\\[ \begin{pmatrix}D\\\0\end{pmatrix} \\]

has exactly one potentially nonzero \\(k\times k\\) minor, namely \\(\det D\\).

Therefore the ideals generated by the maximal minors of \\(P\\) and by \\(\det D\\) agree. Since \\(\mathbb Q[\lambda]\\) is a PID, their gcds agree up to a unit.

This proves the bridge lemma.

### 5.2 The Storjohann–Labahn rectangular algorithm is appropriate

The report cites:

Arne Storjohann and George Labahn, “Preconditioning of Rectangular Polynomial Matrices for Efficient Hermite Normal Form Computation,” ISSAC 1995, pp. 119–125.

This is indeed a rectangular full-column-rank Hermite-form result. It presents a Las Vegas preconditioning algorithm reducing an \\(m\times n\\) rectangular polynomial matrix to an \\((n+1)\times n\\) matrix with entries of comparable coefficient size and degree.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://cs.uwaterloo.ca\&sz=32)

cs.uwaterloo.ca+1



The algorithm detects unsuccessful preconditioning and returns `FAIL`, rather than returning an incorrect Hermite form. The paper gives the success-probability analysis using a Schwartz–Zippel bound.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://cs.uwaterloo.ca\&sz=32)

cs.uwaterloo.ca



This is suitable for the determinantal-divisor computation. It directly addresses the rectangular problem, unlike the square-only Smith-form theorem in Storjohann–Labahn 1997.

For the special dimensions:

- \\(q=k\\): use a square Hermite form;
- \\(q=k+1\\): the rectangular input is already in the reduced-size regime;
- \\(q>k+1\\): use the rectangular preconditioning.

### 5.3 The remaining bit-length bound can be made explicit

The 1995 paper states a bound for the lengths of the numerators and denominators of the rational coefficients appearing in the rectangular Hermite form:

\\[ \widetilde O(k^2\delta\log\\|P\\|), \\]

where \\(\delta\\) is the maximum degree of the input entries and \\(k\\) is the number of columns. It also gives bounds for the coefficient growth in the preconditioning stage.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://cs.uwaterloo.ca\&sz=32)

cs.uwaterloo.ca+1



To avoid collision with your use of \\(d=\dim\ker T\\), write \\(\delta\\) for the polynomial degree bound.

For your degree-one case, \\(\delta=1\\).

Suppose the rational input coefficients have total binary encoding length \\(L\\). Clear denominators by multiplying \\(P\\) by a common denominator \\(\eta\\). The bit length of \\(\eta\\) is at most polynomial in \\(L\\), and the resulting integer coefficients have bit length

\\[ \tau'=O(L). \\]

The rectangular Hermite-form coefficient bound then gives

\\[ \boxed{ \operatorname{bitsize}(D) = \widetilde O\big(k^2(\tau'+\log q)\big) = \widetilde O(k^2L) } \\]

for degree-one input, with the logarithmic factors suppressed.

The common denominator scaling changes the determinantal divisor by

\\[ \Delta_k(\eta P)=\eta^k\Delta_k(P), \\]

which is harmless when the gcd is normalised to be monic.

This is enough to establish polynomial output size and polynomial bit complexity.

### 5.4 There is also a deterministic rectangular route

This is worth adding to the report.

The Storjohann–Labahn 1995 paper explicitly describes a reduction of a rectangular Hermite-form computation to a square nonsingular one. After permuting the rows, write

\\[ P= \begin{pmatrix} P_1\\\P_2 \end{pmatrix}, \\]

where \\(P_1\\) is a nonsingular \\(k\times k\\) row submatrix.

Construct

\\[ \widehat P= \begin{pmatrix} P_1&0\\\ P_2&I\_{q-k} \end{pmatrix}. \\]

This is a square nonsingular \\(q\times q\\) polynomial matrix. Its first \\(k\\) columns are the permuted rectangular input \\(P\\). Computing the square Hermite form of \\(\widehat P\\) and taking its first \\(k\\) columns gives the rectangular Hermite form of \\(P\\).

The reduction is described explicitly in the rectangular-HNF paper.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://cs.uwaterloo.ca\&sz=32)

cs.uwaterloo.ca



Kannan's 1985 paper establishes a deterministic polynomial-time Hermite-form algorithm over \\(\mathbb Q[\lambda]\\) for square nonsingular polynomial matrices.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车



Therefore the square embedding gives a deterministic polynomial-time route for the rectangular determinantal divisor as well. It may be less efficient than the direct rectangular Las Vegas method, but it avoids the randomized preconditioning.

My recommendation: state both routes:

- the rectangular Las Vegas algorithm as the efficient direct method;
- the deterministic square-embedding reduction as the clean deterministic complexity justification.

### 5.5 Does “RP absorbs Las Vegas” need further explanation?

Yes. The conclusion is reasonable, but the paper should make the complexity-class step explicit.

A Las Vegas subroutine has no incorrect outputs but may have random running time. Expected polynomial time alone is not the same as the worst-case polynomial running-time requirement in the standard definition of RP.

To obtain an RP algorithm:

1. Use the explicit expected-polynomial running-time bound of the Las Vegas subroutine.
2. Choose a polynomial cutoff at least twice that expected bound.
3. If the subroutine has not completed by the cutoff, reject.
4. Since the subroutine never returns an incorrect result, this truncation introduces only an additional false-negative probability.

Combined with the outer one-sided randomized test, this gives an RP algorithm, provided the yes/no convention is chosen so that timeouts only reject yes-instances.

Alternatively, use the deterministic square-embedding method and avoid this additional discussion altogether.

The overall DEC result remains RP rather than ZPP because the outer randomized two-combination and parameter-sampling steps are still present. Making the determinantal-divisor subroutine deterministic does not remove those sources of randomness.

Verdict on Q5: the bridge lemma is correct. The Storjohann–Labahn rectangular algorithm is sufficient. The bit-length bound can be stated as \\(\widetilde O(k^2L)\\) for degree-one rational input, and a deterministic rectangular alternative follows from square embedding.

## 6. Question 6: what should be done next?

I would choose a combination of (a) and (c), with a short restricted theorem from (b) inserted between them.

### Priority 1: finish the general \\(q=2\\) criterion

This is the cheapest correction and gives an exact theorem.

State:

\\[ q=2,\ \omega=1 \quad\Longrightarrow\quad \text{good}\iff Z(W)\not\subseteq W. \\]

Then give the \\(U_0=0\\) coordinate form:

\\[ V_0=\alpha h,\qquad g_2=\beta h \quad\Longrightarrow\quad \text{good}\iff\alpha\ne0. \\]

Recompute the four \\(q=2\\) witnesses using this criterion. This will eliminate the discrepancy and give a reliable low-order result.

### Priority 2: prove the restricted \\(d=2,\ U_0=0\\) all-bad theorem

The proposition in Section 2 is short and conceptually clean.

It explains the observed examples and identifies the structural role of the left kernel of \\(Z_2\\). It is more valuable than trying to prove a universal \\(d=2\\) statement without the necessary hypotheses.

### Priority 3: repair and complete the \\(k=\omega+1\\) projective theorem

The next main theorem should use the exact admissibility condition

\\[ e+\dim X_S-\dim(E\cap X_S)=\omega, \\]

together with

\\[ E+F_0\subseteq S,\qquad \omega-e\le m. \\]

It should then construct the total compatible-pair incidence space and stratify it by the ranks of \\(Q\\), \\([P;Q]\\), and the intersection with \\(E\\).

Only after the total incidence components are identified should the generic determinantal-divisor theorem be applied.

### Priority 4: assemble the paper package

Once the three items above are stable, assemble:

- the structural reduction to the induced map on \\(W=\mathcal LK\\);
- the free-fibre theorem;
- the \\(d=1\\) mixed example;
- the restricted \\(d=2\\) all-bad theorem;
- the corrected \\(q=2\\) criterion;
- the projective constrained-fibre theorem;
- the RP result and determinantal-divisor algorithm;
- the Lean-checked linear-algebra kernel.

The Lean formalisation of the \\(d=1\\) family should follow the exact theorem, not precede it. It should include the compatibility equations and the exceptional-point calculation if the aim is to formalise the entire mixed-stratum statement.

## 7. A single computation that would be especially informative

I recommend a targeted exact computation, not another broad random scan.

Test: rank-stratum decomposition and spectral behaviour for \\(k=3,\omega=2,q=3\\)

Fix exact rational data with \\(d=1\\) and \\(d=2\\), and compute:

1. The projective candidate locus \\(E+F_0\subseteq S\\).
2. The ranks of \\(Q=B^{\mathsf T}Z_2\\) and \\([P;Q]\\).
3. The dimension of \\(X_S\\).
4. The dimension of \\(E\cap X_S\\).
5. The exact admissibility equality \\(E+X_S=S\\).
6. The compatible-pair fibre over every resulting stratum.
7. The generic gcd of the maximal minors on each irreducible component of the total incidence space.
8. The existence of a full-row-rank lift to \\(L=[L_0;R]\\).

The key output: a table with one row per irreducible incidence component, recording its dimension, compatibility rank, admissibility status, generic determinantal divisor, and whether it contains a full-row-rank lift.

This would distinguish the algorithmic and hardness scenarios more effectively than simply collecting more examples.

In particular, it would test whether the number of irreducible components and the degrees of the rank-stratum equations remain controlled as \\(k\\) increases. That is the issue most likely to determine whether the constrained geometry is algorithmically manageable.

## 8. Final research status

| Result                                     | Assessment                                        | Action                                                          |
| ------------------------------------------ | ------------------------------------------------- | --------------------------------------------------------------- |
| \\(d=1\\) mixed family                     | Correct at compressed-fibre level                 | Add full-row-rank lifting verification                          |
| Exceptional-point constructions            | Correct                                           | Retain both gcd computations                                    |
| \\(d=1\\) fibre jump                       | Essential structural phenomenon                   | Encode through compatibility-rank strata                        |
| \\(d=2\\) example                          | Correct                                           | Replace enumeration as main explanation with restricted theorem |
| \\(d=2\\), \\(U_0=0\\) all-bad proposition | Strong and provable                               | Prove and include                                               |
| \\(q=2,\omega=1\\) criterion               | Exact; discrepancy resolved                       | Correct block identification                                    |
| \\(q\_{\min}\\) from one rank stratum      | Not justified                                     | Test all admissible \\(\omega\\)-layers                         |
| Formula for \\(\dim X_S\\)                 | Correct                                           | Retain                                                          |
| \\(X_S\nsubseteq E\\) as admissibility     | Incorrect generally                               | Replace by (4.2)                                                |
| Projective genericity argument             | Correct on irreducible total-incidence components | Clarify parameter space                                         |
| Rectangular bridge lemma                   | Correct                                           | Retain                                                          |
| Storjohann–Labahn rectangular HNF          | Suitable Las Vegas method                         | State bit bound and truncation                                  |
| Deterministic rectangular alternative      | Available                                         | Include square-embedding reduction                              |
| RP theorem                                 | Promising                                         | Complete bit-complexity and one-sided-error argument            |

## 9. Overall recommendation

The most important new conceptual point is that the \\(d=1\\) mixed example and the \\(d=2\\) all-bad example are not merely different outcomes of random experiments. They illustrate two different compatibility geometries.

For \\(d=1\\), the compatibility rank drops at an exceptional hyperplane, and the enlarged fibre admits a good pencil.

For \\(d=2\\) with \\(U_0=0\\), the relation

\\[ V_0Z_2=0 \\]

forces every admissible hyperplane to contain the left kernel of \\(Z_2\\). The induced operator on the one-dimensional quotient then has an eigenvalue, forcing rank loss.

This is a genuine structural distinction. It suggests that the projective theory should be built around the rank of the restricted compatibility map, rather than around \\(d\\) alone.

My recommended next milestone is therefore:

\\[ \boxed{ \text{Exact }q=2\text{ criterion} \\;\longrightarrow\\; \text{restricted }d=2\text{ theorem} \\;\longrightarrow\\; \text{corrected }k=\omega+1\text{ projective theorem}. } \\]

That sequence resolves an existing inconsistency, extracts a new theorem from the \\(d=2\\) experiments, and repairs the central geometric framework. It is the most economical route to a coherent and publishable paper.

The immediate mathematical task I would tackle is the corrected incidence-space theorem, with (4.2) as its exact admissibility condition and with the full-row-rank lifting condition treated explicitly.