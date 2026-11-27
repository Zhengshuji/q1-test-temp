# Research assessment of Report 67: Uniform spectral control and the route to an arithmetic gadget

## 1. Overall assessment

Report 67 identifies the correct next obstacle. The six-dimensional construction is now a verified example of a feasible rectangular pencil with an invariant kernel and genuine leakage from \\(K_0\\). However, its spectral certificate is currently a certificate at one fixed configuration. The hardness programme requires something substantially stronger: a construction in which the arithmetic variables can vary while the pencil remains spectrally admissible throughout the intended parameter space.

My main conclusion is:

The most promising direction is to develop a uniform rectangular-pencil lemma, not to seek a direct-sum padding lemma for an arbitrary arithmetic pencil.

There is a particularly useful general mechanism:

- let \\(H(X)\\) have a parameter-dependent kernel \\(V(X)\\), but a fixed image \\(W\\);
- arrange that\
  \\[\
  H_A(X)=D(X)H(X);\
  \\]
- require the restriction \\(D(X)|\_W:W\to\mathbb C^q\\) to have no eigenvectors, uniformly in \\(X\\).

Then

\\[ P_X(\lambda) =(\lambda I-D(X))H(X) \\]

has rank \\(\omega\\) for every finite \\(\lambda\\), independently of the arithmetic parameters.

The six-dimensional template is an instance of precisely this mechanism.

There is also a stronger possibility: the map \\(D(X)|\_W\\) need not be constant. A fixed filtration and a fixed leakage pivot can guarantee the absence of eigenvectors even when many entries of \\(D(X)\\) depend on the arithmetic variables.

That is the route I would investigate first.

There is, however, an important distinction between an abstract pencil construction and its realization by matrices \\(A,C,L_0,L\\). A uniform pencil lemma alone does not establish an observer-problem reduction. The pair-lift constraints must be satisfied simultaneously.

I will address the four questions in turn, then formulate a concrete research programme.

# Part I. The algebraic structure of uniform spectral control

## 2. Reformulating the spectral condition

Recall the compressed matrices

\\[ H(X)=L(X)N,\qquad H_A(X)=L(X)AN, \\]

where \\(N\\) is a basis matrix for

\\[ K_0=\ker[C;CA]. \\]

Suppose

\\[ \operatorname{rank}H(X)=\omega \\]

and

\\[ \ker H(X)\subseteq\ker H_A(X). \\]

The compressed pencil is

\\[ P_X(\lambda)=\lambda H(X)-H_A(X). \\]

The spectral condition is

\\[ \operatorname{rank}P_X(\lambda)=\omega \qquad\forall\lambda\in\mathbb C. \\]

For a fixed \\(X\\), this is equivalent to saying that all \\(\omega\times\omega\\) minors of \\(P_X(\lambda)\\) have no common complex zero.

For a family \\(X\in S\\), where \\(S\\) is the parameter set defined by the arithmetic constraints, the desired condition is

\\[ \boxed{ \forall X\in S,\ \forall\lambda\in\mathbb C: \quad \operatorname{rank}P_X(\lambda)=\omega. } \\]

This is a genuinely stronger requirement than checking the pencil at a sample of parameter values.

A finite collection of numerical experiments cannot establish it. Nor is it enough to prove that the pencil has full rank for generic \\(X\\): the reduction needs the property at every intended solution, including special or degenerate arithmetic solutions.

The right object to study is therefore not merely the gcd of the minors at one point, but a uniform certificate that their common zero set is empty over the entire parameter space.

## 3. The uniform Bézout-certificate viewpoint

Let

\\[ \Delta_I(X,\lambda) \\]

denote the \\(\omega\times\omega\\) minors of \\(P_X(\lambda)\\).

A sufficient condition for uniform spectral admissibility is the existence of polynomial coefficients \\(a_I(X,\lambda)\\) and a polynomial \\(s(X)\\) such that

\\[ \boxed{ \sum_I a_I(X,\lambda)\Delta_I(X,\lambda) = s(X), } \\]

where

\\[ s(X)\ne0\qquad\forall X\in S. \\]

If \\(s(X)=1\\), this is a particularly strong certificate.

More generally, if \\(S\\) is defined by polynomial equations

\\[ f_1(X)=\cdots=f_m(X)=0, \\]

one can seek an identity

\\[ \sum_I a_I(X,\lambda)\Delta_I(X,\lambda) + \sum\_{j=1}^m b_j(X,\lambda)f_j(X) =1. \\]

On \\(S\\), the second sum vanishes, leaving

\\[ \sum_I a_I(X,\lambda)\Delta_I(X,\lambda)=1. \\]

Thus the minors cannot vanish simultaneously.

This is the algebraic-geometric form of the uniformity question. It is more useful than simply saying that the gcd is one, because the gcd computation in the original template concerns one fixed numerical pencil, whereas the identity above is valid on an entire algebraic family.

There is a simple special case worth emphasizing.

If two minors satisfy

\\[ \Delta_1(X,\lambda)-\Delta_2(X,\lambda)=1 \\]

for every \\(X,\lambda\\), then the spectral condition is immediate.

In the six-dimensional example, the minors

\\[ \lambda^2,\qquad \lambda^2-1 \\]

differ by a constant. The original certificate is therefore already of the strongest possible elementary type.

Recommendation: whenever a new parameter-dependent pencil is constructed, first look for two minors differing by a fixed nonzero constant, or more generally for a low-degree uniform Bézout identity. This is often much simpler than computing a general resultant or eliminating \\(\lambda\\).

# Part II. Question 1: Can the spectral condition be made uniform under perturbations?

## 4. The basic uniform rectangular-pencil lemma

The most direct method is to factor the pencil through a fixed image space.

Let \\(X\\) vary in some parameter set \\(S\\). Suppose

\\[ H(X)\in\mathbb C^{q\times k} \\]

satisfies

\\[ \operatorname{rank}H(X)=\omega \qquad\forall X\in S, \\]

and suppose

\\[ \operatorname{im}H(X)=W \\]

is independent of \\(X\\).

Assume that there exists

\\[ D(X)\in\mathbb C^{q\times q} \\]

such that

\\[ \boxed{H_A(X)=D(X)H(X).} \\]

Then

\\[ P_X(\lambda) = \lambda H(X)-H_A(X) = (\lambda I_q-D(X))H(X). \\]

Since \\(H(X)\\) maps onto \\(W\\), we have

\\[ \operatorname{rank}P_X(\lambda) = \operatorname{rank} \left((\lambda I_q-D(X))|\_W\right). \\]

Consequently,

\\[ \operatorname{rank}P_X(\lambda)=\omega \\]

if and only if

\\[ \ker\left((\lambda I_q-D(X))|\_W\right)=\\{0\\}. \\]

Equivalently,

\\[ \boxed{ Dw=\lambda w,\quad w\in W \quad\Longrightarrow\quad w=0. } \\]

The important point is that this is a rectangular eigenvector problem.

The map

\\[ D(X)|\_W:W\longrightarrow\mathbb C^q \\]

does not necessarily map \\(W\\) into itself. It can send a vector in \\(W\\) partly outside \\(W\\). Therefore it need not possess an eigenvector, even over \\(\mathbb C\\).

This is the precise mechanism behind the six-dimensional construction.

### Why this is useful

The arithmetic parameters can enter \\(H(X)\\) through its kernel while leaving its image fixed. They can also enter \\(D(X)\\), provided the latter remains eigenvector-free on \\(W\\).

Thus there are two distinct sources of parameter dependence:

1. the quotient map \\(H(X)\\), whose kernel represents the candidate subspace \\(V(X)\\);
2. the rectangular map \\(D(X)|\_W\\), whose spectral properties must be controlled uniformly.

This separation is the main structural opportunity.

## 5. A particularly strong sufficient condition: a fixed shift chain

Let

\\[ W=\operatorname{span}\\{w_0,\ldots,w\_{\omega-1}\\} \\]

and extend it by one vector \\(g\\), so that

\\[ \mathbb C^q=W\oplus\mathbb Cg, \qquad q=\omega+1. \\]

Define a map \\(D:W\to\mathbb C^q\\) by

\\[ \begin{aligned} Dw_0&=w_1,\\\ Dw_1&=w_2,\\\ &\ \vdots\\\ Dw\_{\omega-2}&=w\_{\omega-1},\\\ Dw\_{\omega-1}&=g. \end{aligned} \\]

Then \\(D|\_W\\) has no eigenvector.

Indeed, suppose

\\[ Dw=\lambda w, \\]

where

\\[ w=\sum\_{j=0}^{\omega-1}a_jw_j. \\]

Comparing the coefficient of \\(g\\), we obtain

\\[ a\_{\omega-1}=0. \\]

Comparing the coefficient of \\(w\_{\omega-1}\\), we then obtain

\\[ a\_{\omega-2}=0. \\]

Continuing recursively gives

\\[ a\_{\omega-3}=\cdots=a_0=0. \\]

Hence \\(w=0\\).

Therefore

\\[ \operatorname{rank}((\lambda I-D)|\_W)=\omega \qquad\forall\lambda\in\mathbb C. \\]

This gives a uniform spectral certificate that does not require computing any minors.

### The six-dimensional example in this language

For the six-dimensional example, take

\\[ W=\operatorname{span}\\{f_1,f_2\\}\subset\mathbb C^3, \\]

where \\(f_1,f_2,f_3\\) are the standard output-coordinate vectors.

The matrices are

\\[ H= \begin{bmatrix} 1&0&0&0\\\ 0&1&0&0\\\ 1&1&0&0 \end{bmatrix}, \\]

and

\\[ H_A= \begin{bmatrix} 0&1&0&0\\\ 0&0&0&0\\\ 1&1&0&0 \end{bmatrix}. \\]

There is a map \\(D\\) satisfying

\\[ H_A=DH. \\]

One possible choice is

\\[ D= \begin{bmatrix} 0&1&0\\\ 0&0&0\\\ 1&1&0 \end{bmatrix}. \\]

Indeed,

\\[ Df_1=f_3,\qquad Df_2=f_1+f_3. \\]

The image of \\(H\\) is

\\[ W=\operatorname{span}\\{f_1,f_2\\}. \\]

For a vector

\\[ w=af_1+bf_2, \\]

we have

\\[ Dw=bf_1+(a+b)f_3. \\]

If \\(Dw=\lambda w\\), the \\(f_3\\)-coordinate gives \\(a+b=0\\), while the \\(f_2\\)-coordinate gives \\(\lambda b=0\\). The \\(f_1\\)-coordinate then forces \\(b=0\\), and hence \\(a=0\\).

Thus the map is eigenvector-free on \\(W\\).

This is a slightly different coordinate presentation from the pure shift chain, but it exhibits the same mechanism: a component outside \\(W\\) prevents an eigenvector.

## 6. Can the shift chain survive variable-dependent perturbations?

Yes, provided the perturbations respect an appropriate filtration.

This is more flexible than insisting that \\(D(X)\\) remain exactly equal to a fixed shift.

Let

\\[ W=\operatorname{span}\\{w_0,\ldots,w\_{\omega-1}\\}, \\]

and suppose

\\[ D(X)w_j \in \operatorname{span}\\{w_0,\ldots,w\_{j+1}\\} \qquad (0\le j<\omega-1), \\]

while

\\[ D(X)w\_{\omega-1} \in W+\mathbb Cg, \\]

with the coefficient of \\(g\\) in the last expression equal to \\(1\\).

Also require that the coefficient of \\(w\_{j+1}\\) in \\(D(X)w_j\\) is exactly \\(1\\).

All other coefficients may depend on \\(X\\), as long as the stated support restrictions are maintained.

Then the same descending-coordinate argument proves that

\\[ D(X)w=\lambda w,\quad w\in W \quad\Longrightarrow\quad w=0 \\]

for every \\(X\\).

To see why, write

\\[ D(X)w=\lambda w,\qquad w=\sum\_{j=0}^{\omega-1}a_jw_j. \\]

The coefficient of \\(g\\) is \\(a\_{\omega-1}\\), so

\\[ a\_{\omega-1}=0. \\]

Now examine the coefficient of \\(w\_{\omega-1}\\). By the support restrictions, the only contribution that can survive after setting \\(a\_{\omega-1}=0\\) is the fixed coefficient \\(a\_{\omega-2}\\). Hence

\\[ a\_{\omega-2}=0. \\]

Continue recursively.

The result is

\\[ a_0=\cdots=a\_{\omega-1}=0. \\]

This gives the following useful principle.

Uniform filtration principle

If a family of rectangular maps \\(D(X)|\_W\\) has a fixed nonzero shift coefficient on every successive level of a filtration, and the final level leaks with a fixed nonzero coefficient outside \\(W\\), then the entire family is eigenvector-free on \\(W\\).

This is a genuine answer to Question 1. The perturbation need not be zero; it must preserve the filtration and its pivot coefficients.

It is also a natural way to allow arithmetic variables into the spectral block without allowing them to destroy the spectral certificate.

# Part III. The role of rows invisible to the pencil

## 7. What happens if arithmetic variables enter through rows in the common kernel of the compressed-pair map?

The report suggests using rows whose coordinates lie in the kernel of every pencil minor.

There is a useful interpretation, but it is important to distinguish two cases.

Recall the pair map

\\[ \Psi: (\mathbb C^n)^\*/\operatorname{row}C \longrightarrow K_0^\*\oplus K_0^\*, \\]

\\[ \bar g\longmapsto(gN,gAN). \\]

If

\\[ gN=0,\qquad gAN=0, \\]

then adding \\(g\\) to a row of \\(L\\) changes neither \\(H\\) nor \\(H_A\\).

Thus

\\[ \ker\Psi \\]

consists of directions that are completely invisible to the compressed pencil.

They can be used to adjust row independence, and they can be valuable in the pair-lift construction. They do not, however, alter the spectral condition.

There are two consequences.

### 7.1 What these rows can accomplish

Suppose a row \\(l_i\\) already gives the desired compressed pair

\\[ (l_iN,l_iAN). \\]

Replacing it by

\\[ l_i+g_i,\qquad g_i\in\ker\Psi, \\]

does not change that pair.

Such directions can therefore be used to complete rows independently modulo \\(\operatorname{row}C\\), subject to the dimension condition from the pair-lift theorem.

This is useful for satisfying \\(\mathsf P\_{\mathrm{ind}}\\) without disturbing the pencil.

### 7.2 What these rows cannot accomplish

If all arithmetic variables enter only through \\(\ker\Psi\\), then

\\[ H(X)=H,\qquad H_A(X)=H_A. \\]

Consequently,

\\[ V(X)=\ker H(X)=\ker H \\]

is fixed.

The compressed invariance structure is also unchanged.

Thus these invisible rows cannot, by themselves, encode an arithmetic relation through a variable graph

\\[ V(X)=\operatorname{graph}(X). \\]

They are an auxiliary device for row completion, not a substitute for the arithmetic gadget.

My recommendation: reserve \\(\ker\Psi\\) for the independence problem. Do not make it the primary location of the arithmetic variables.

# Part IV. Question 2: Can a graph-chart arithmetic construction be separated from the spectral block?

## 8. The ideal graph-chart factorization

Suppose

\\[ K_0=U\oplus Z \\]

and the candidate kernel is parameterized by

\\[ V(X)=\operatorname{graph}(X) = \\{(Xz,z):z\in Z\\}, \\]

where

\\[ X:Z\to U. \\]

A natural quotient map is

\\[ H(X)= \begin{bmatrix} I_U&-X \end{bmatrix}. \\]

Its kernel is exactly

\\[ \ker H(X)=V(X). \\]

Its image is the fixed space \\(U\\), independently of \\(X\\).

This is precisely the kind of representation needed for uniform spectral control.

If one could arrange

\\[ H_A(X)=D(X)H(X), \\]

where

\\[ D(X):U\to U\oplus\mathbb Cg \\]

is uniformly eigenvector-free, then

\\[ P_X(\lambda) = (\lambda I-D(X))H(X) \\]

would have rank \\(\dim U\\) for every \\(\lambda\\).

The graph \\(X\\) would control the kernel, while the filtration structure of \\(D(X)\\) would control the spectrum.

This is the cleanest abstract formulation of the proposed separation.

## 9. A critical limitation: a fixed \\(D\\) may destroy the arithmetic expressiveness

There is an important issue that should not be overlooked.

If \\(D\\) is fixed, then

\\[ H_A(X)=DH(X) \\]

is a linear relation between \\(H(X)\\) and \\(H_A(X)\\).

Since

\\[ H(X)=L(X)N,\qquad H_A(X)=L(X)AN, \\]

the equation

\\[ L(X)AN=DL(X)N \\]

is linear in the entries of \\(L(X)\\).

If \\(D\\) is fixed and all other constraints are linear, this construction may reduce the arithmetic problem to an affine-linear feasibility problem. It would then be too restrictive to encode general multiplication constraints such as

\\[ z=xy. \\]

Therefore, I would not recommend insisting on a constant \\(D\\) as the final arithmetic construction.

The better target is

\\[ \boxed{ H_A(X)=D(X)H(X), } \\]

where \\(D(X)\\) is allowed to depend on the arithmetic variables, but belongs to a class of rectangular maps satisfying the uniform filtration condition.

This permits nonlinear dependence in the relation between \\(H\\) and \\(H_A\\), while the spectral proof remains independent of the numerical values of the variables.

For example, some entries of \\(D(X)\\) could contain \\(x\\), \\(y\\), or \\(z\\), with the multiplication relation encoded through the compatibility equations for the lifted rows.

The spectral proof would not need to use

\\[ z=xy. \\]

It would use only the structural support and fixed-pivot conditions on \\(D(X)\\).

That separation is highly desirable.

## 10. The difficulty of realizing \\(D(X)\\) with a fixed \\(A\\)

The preceding construction is an abstract pencil construction. The actual observer problem requires

\\[ H(X)=L(X)N,\qquad H_A(X)=L(X)AN \\]

for the same fixed matrices \\(A,C,N\\).

Thus it is not enough to prescribe arbitrary matrices \\(H(X)\\) and \\(H_A(X)\\).

For each row \\(i\\), the pair

\\[ (h_i(X),h\_{A,i}(X)) \\]

must lie in the image of the pair map \\(\Psi\\).

In particular, the target relation

\\[ h\_{A,i}(X)=d_i(X)H(X) \\]

must be compatible with the geometry of \\(K_0\\) and \\(A(K_0)\\).

There is a useful way to see this compatibility.

A row functional \\(l\\) determines two restrictions:

\\[ h=l|\_{K_0},\qquad g=l\circ A|\_{K_0}. \\]

These restrictions are not arbitrary if \\(A(K_0)\\) intersects \\(K_0\\).

For every \\(v\in K_0\\) with \\(Av\in K_0\\), one must have

\\[ \boxed{ g(v)=h(Av). } \\]

This is an unavoidable compatibility relation.

If \\(A(K_0)\cap K_0=\\{0\\}\\), then the two restrictions can be prescribed independently and extended to an ambient functional. But in many useful constructions, including shift-chain constructions, the intersection is nontrivial.

Thus a successful gadget must respect these relations rather than treating \\(H\\) and \\(H_A\\) as independent variables.

### The exact realization problem

The key question is therefore:

Can one construct a fixed \\(A,C,N\\) and a parameterized family \\(L(X)\\) such that

\\[ L(X)N=H(X), \\]

\\[ L(X)AN=D(X)H(X), \\]

where:

1. \\(\ker H(X)=V(X)\\) is the desired graph;
2. \\(\operatorname{im}H(X)=W\\) is fixed;
3. \\(D(X)|\_W\\) satisfies a uniform filtration condition;
4. the first row of \\(L(X)\\) is the prescribed fixed row \\(L_0\\);
5. the required row-independence condition holds?

This is the central constructive problem. It is considerably more precise than the original uniformity question.

## 11. A useful refinement: preserve the image, vary the kernel

I would formulate the arithmetic gadget around the following architecture:

\\[ \begin{array}{ccccc} K_0&\xrightarrow{\ H(X)\ }&W\\\ &&\downarrow D(X)\\\ &&\mathbb C^q. \end{array} \\]

The desired properties are:

\\[ \ker H(X)=V(X), \\]

\\[ \operatorname{im}H(X)=W, \\]

\\[ H_A(X)=D(X)H(X). \\]

Then:

- the arithmetic variables are represented by the kernel \\(V(X)\\);
- the image \\(W\\) remains fixed;
- the spectral condition is guaranteed by \\(D(X)|\_W\\);
- the invariance condition (5a) follows automatically from the factorization.

This is a much better decomposition of responsibilities than asking the arithmetic block itself to generate a favorable spectrum.

There is one subtle point: although (5a) follows from the factorization, the relation \\(H_A(X)=D(X)H(X)\\) is stronger than (5a). It is a particular way of enforcing it. If the resulting family is too restrictive, one should weaken the factorization to a filtration-compatible relation rather than abandon the uniformity principle.

# Part V. Question 3: Should the six-dimensional template be used as padding?

## 12. Why direct-sum padding is insufficient in general

Suppose an arithmetic construction gives a pencil

\\[ P\_{\mathrm{arith}}(X,\lambda). \\]

Suppose we add the fixed spectral-good template as a block:

\\[ P\_{\mathrm{total}}(X,\lambda) = \begin{bmatrix} P\_{\mathrm{pad}}(\lambda)&0\\\ 0&P\_{\mathrm{arith}}(X,\lambda) \end{bmatrix}. \\]

Then

\\[ \operatorname{rank}P\_{\mathrm{total}}(X,\lambda) = \operatorname{rank}P\_{\mathrm{pad}}(\lambda) + \operatorname{rank}P\_{\mathrm{arith}}(X,\lambda). \\]

If the padding block has rank \\(\omega\_{\mathrm{pad}}\\) at every \\(\lambda\\), then

\\[ \operatorname{rank}P\_{\mathrm{total}} = \omega\_{\mathrm{pad}} + \operatorname{rank}P\_{\mathrm{arith}}. \\]

Therefore, if the arithmetic block drops rank at some \\(\lambda\\), the total pencil also drops rank.

A fixed direct-sum block cannot compensate for a rank defect in another independent block.

This is a simple but decisive obstruction.

Consequently, the following proposed lemma is false without additional assumptions:

> A fixed spectral-good block added by direct sum to an arbitrary arithmetic block makes the total pencil spectrally good.

The rank of a block-diagonal matrix is additive. There is no cancellation mechanism.

## 13. When direct-sum padding does work

Direct-sum padding is valid under the stronger assumption that the arithmetic block is already spectrally admissible.

Suppose

\\[ \operatorname{rank}P\_{\mathrm{arith}}(X,\lambda) =\omega\_{\mathrm{arith}} \\]

for every intended arithmetic solution \\(X\\) and every \\(\lambda\\).

Then

\\[ \operatorname{rank}P\_{\mathrm{total}} = \omega\_{\mathrm{pad}}+\omega\_{\mathrm{arith}} \\]

for every such \\(X,\lambda\\).

In that case, the padding block can supply a fixed leakage mechanism and an extra row without interfering with the arithmetic block.

But it does not solve the difficult part: the arithmetic block must still be spectrally good.

## 14. A more promising interpretation of padding: a rectangular guard

There is a stronger idea than direct-sum padding.

Instead of adding a good block on disjoint columns, one can try to add rows that act on the same quotient coordinates as the arithmetic construction.

The aim would be to produce a pencil of the form

\\[ P\_{\mathrm{total}}(X,\lambda) = \begin{bmatrix} P\_{\mathrm{arith}}(X,\lambda)\\\ P\_{\mathrm{guard}}(X,\lambda) \end{bmatrix}, \\]

where the guard is sufficient to guarantee full column rank independently of the arithmetic block.

For example, if the guard itself satisfies

\\[ \operatorname{rank}P\_{\mathrm{guard}}(X,\lambda)=\omega \qquad\forall X,\lambda, \\]

then automatically

\\[ \operatorname{rank}P\_{\mathrm{total}}(X,\lambda)=\omega, \\]

provided the total pencil has only \\(\omega\\) relevant independent columns.

This can indeed make the spectral condition independent of the arithmetic block.

However, there is a major issue: if the guard makes the pencil full rank for every possible arithmetic configuration, then the pencil no longer detects whether the arithmetic relation holds.

That is not necessarily a problem. The arithmetic relation may be encoded in (5a), in the graph-invariance equations, or in the lift constraints. But it means that the spectral condition becomes a structural side condition rather than the mechanism enforcing the arithmetic relation.

The guard must therefore be designed so that it does not trivialize the entire feasibility problem.

### The key distinction

There are two different objectives:

1. Spectral protection: ensure the pencil is good for every intended solution.
2. Arithmetic discrimination: ensure the observer feasibility conditions hold exactly when the encoded arithmetic system is feasible.

A guard can accomplish the first while making the pencil irrelevant to the second.

The arithmetic gadget must still be independently sound and complete.

## 15. What is the minimum padding?

There are two different answers, depending on the meaning of padding.

### 15.1 Minimal output-dimension padding for the invariant-kernel mechanism

Suppose

\\[ A(V)\subseteq V \\]

and

\\[ \operatorname{rank}H=\omega>0. \\]

The local kernel-invariance lemma gives

\\[ H_A=DH \\]

for some \\(D\\) on the output space.

If \\(q=\omega\\), then

\\[ W=\operatorname{im}H=\mathbb C^q. \\]

In that case, \\(D|\_W\\) is a square endomorphism of a nonzero complex vector space. It necessarily has an eigenvector. Hence the pencil cannot have full column rank for every finite complex \\(\lambda\\).

Thus

\\[ \boxed{q>\omega} \\]

is necessary for this invariant-\\(V\\) mechanism.

The shift-chain construction shows that

\\[ \boxed{q=\omega+1} \\]

is sufficient.

Therefore:

Sharp within this mechanism

One extra output dimension is both necessary and sufficient for the invariant-kernel rectangular spectral construction.

This is a strong and useful result.

### 15.2 Minimal padding for an arbitrary arithmetic block

There is no corresponding universal one-row theorem for an arbitrary arithmetic pencil.

The reason is that an arbitrary pencil may have rank defects that are unrelated to the fixed shift chain. A direct-sum padding block cannot repair them, and a rectangular guard must be designed to act on the same quotient coordinates.

The minimum padding dimension depends on:

- the number of independent quotient coordinates;
- the structure of the arithmetic pencil;
- the allowable dependence of the guard on the arithmetic variables;
- the realization constraints imposed by \\(A,C\\);
- the prescribed first row \\(L_0\\);
- the row-independence convention.

So the correct conclusion is:

\\[ \boxed{ \text{One extra row is sharp for the shift-chain spectral mechanism,} } \\]

but

\\[ \boxed{ \text{one extra row is not a universal padding theorem for arbitrary pencils.} } \\]

# Part VI. Question 4: A concrete route to an arithmetic gadget

## 16. My recommendation: establish a uniform padding lemma first, but not the naive one

I agree with the report's suggestion that the hardness workstream should first establish a general padding lemma.

However, I would change the formulation.

Do not aim for:

> A fixed good spectral block plus an arbitrary arithmetic block always gives a good pencil.

That statement is false for block-diagonal pencils.

Instead, aim for:

> A parameterized rectangular quotient map \\(H(X)\\) with prescribed graph kernel, together with a filtration-compatible leakage map \\(D(X)\\), yields a pencil with uniformly constant rank.

This formulation is both mathematically correct and sufficiently flexible to support arithmetic variables.

The proposed route is as follows.

## 17. Stage A: Construct the graph kernel with a fixed image

Let

\\[ K_0=U\oplus Z, \\]

and let

\\[ V(X)=\operatorname{graph}(X) = \\{(Xz,z):z\in Z\\}. \\]

Set

\\[ H(X)= \begin{bmatrix} I_U&-X \end{bmatrix}. \\]

Then

\\[ \ker H(X)=V(X), \\]

and

\\[ \operatorname{im}H(X)=U. \\]

This gives the desired parameterized kernel without changing the image.

The dimensions are

\\[ \dim K_0=\dim U+\dim Z, \\]

\\[ \omega=\dim U,\qquad c=\dim Z. \\]

The rank of \\(H(X)\\) is automatically \\(\omega\\), regardless of \\(X\\).

This is an excellent starting point.

## 18. Stage B: Introduce a variable-dependent leakage map

Choose an additional coordinate \\(g\\), and let

\\[ q=\omega+1. \\]

Define

\\[ D(X):U\longrightarrow U\oplus\mathbb Cg \\]

with the filtration structure described earlier.

For example, in a basis \\(w_0,\ldots,w\_{\omega-1}\\), require

\\[ D(X)w_j = w\_{j+1} + \sum\_{i=0}^{j}a\_{ij}(X)w_i \qquad (j<\omega-1), \\]

and

\\[ D(X)w\_{\omega-1} = g+\sum\_{i=0}^{\omega-1}a\_{i,\omega-1}(X)w_i. \\]

The coefficients \\(a\_{ij}(X)\\) may depend on the arithmetic variables.

The fixed superdiagonal coefficients and the fixed leakage coefficient \\(1\\) provide the spectral certificate.

Then define

\\[ H_A(X)=D(X)H(X). \\]

It follows that

\\[ P_X(\lambda) = (\lambda I-D(X))H(X). \\]

The uniform filtration argument gives

\\[ \boxed{ \operatorname{rank}P_X(\lambda)=\omega \quad\forall X,\lambda. } \\]

This is the desired uniform spectral property.

### Why this construction is better than a constant shift

A constant shift would make the spectral proof easy but may make the arithmetic system too rigid.

A variable-dependent \\(D(X)\\) allows arithmetic information to enter the pencil while preserving the spectral argument.

The key is that the arithmetic variables may alter the lower-order coefficients but cannot change the pivot pattern.

This is analogous to a triangular matrix argument: the numerical values of the off-diagonal entries do not affect the determinant if the diagonal pivots remain fixed. Here the analogous structure is rectangular and is governed by a filtration rather than a square determinant.

## 19. Stage C: Realize the pair through fixed \\(A,C\\)

This is the most important stage.

We need to solve

\\[ L(X)N=H(X), \\]

\\[ L(X)AN=D(X)H(X). \\]

These equations are not merely a matter of choosing \\(L(X)\\) arbitrarily. Each row pair must be realizable under the fixed linear map

\\[ \Psi: (\mathbb C^n)^\*/\operatorname{row}C \to K_0^\*\oplus K_0^\*. \\]

For each row \\(i\\), we need

\\[ (h_i(X),h\_{A,i}(X))\in\operatorname{im}\Psi. \\]

The correct approach is to design the ambient leakage geometry so that the required pairs are realizable.

A useful sufficient condition for unrestricted pair realization is

\\[ K_0\cap A(K_0)=\\{0\\}. \\]

Under this condition, a functional on \\(K_0\\) and a functional on \\(A(K_0)\\) can be specified independently and extended to the ambient space.

This condition may be too strong for the desired shift-chain construction, but it gives a clean starting point for a small gadget.

If the intersection is nonzero, then the pair data must satisfy the compatibility relations

\\[ h_A(v)=h(Av) \\]

whenever \\(v\in K_0\\) and \\(Av\in K_0\\).

I would explicitly include these compatibility equations in the gadget design rather than trying to avoid them through numerical experimentation.

## 20. Stage D: Encode one multiplication gate

The first serious test should be a single gate:

\\[ z=xy. \\]

Do not begin with a full arithmetic circuit.

There are two possible locations for the variables:

1. the graph matrix \\(X\\);
2. the coefficients \\(a\_{ij}(X)\\) in \\(D(X)\\).

I recommend beginning with a mixed design.

For example, let \\(x,y,z\\) occur as entries of \\(X\\), while a separate coefficient of \\(D(X)\\) is constrained to equal a linear expression involving those entries.

The equation

\\[ H_A(X)=D(X)H(X) \\]

then generates bilinear expressions through the product of the variable-dependent factors.

One must be careful here: simply declaring a coefficient of \\(D(X)\\) to be \\(xy\\) does not encode multiplication. It only introduces another variable unless the matrix equations force the product relation.

The actual target is to obtain a system in which the compatibility equations contain

\\[ z-xy=0 \\]

and no unintended solutions.

The filtration constraints should be chosen so that this equation can appear in a lower-order coefficient without altering the fixed shift pivots.

### The one-gate success criterion

A successful one-gate gadget should establish all of the following:

1. Every solution of \\(z=xy\\) gives a valid \\(L(X)\\).
2. Every valid \\(L(X)\\) in the intended chart yields \\(z=xy\\).
3. The compressed matrix \\(H(X)\\) has the intended graph kernel.
4. The image of \\(H(X)\\) is fixed.
5. \\(H_A(X)=D(X)H(X)\\).
6. \\(D(X)|\_W\\) satisfies the filtration condition.
7. The prescribed first row \\(L_0\\) remains fixed.
8. The rows of \\(L\\) satisfy the required independence convention.
9. All matrices \\(A,C,L_0\\) are fixed as part of the reduction instance; only the unknown \\(L\\) varies.

The last point is essential. A reduction cannot encode the arithmetic variables by allowing the input matrix \\(A\\) itself to depend on those variables.

## 21. Stage E: Use the pair-lift theorem as a formal obstruction test

The pair-lift results from the earlier reports should be used before attempting a large construction.

For each proposed pair

\\[ (H(X),H_A(X)), \\]

check:

- whether its rows belong to \\(\operatorname{im}\Psi\\);
- whether the prescribed first row has a compatible lift;
- whether the bottom rows can be completed independently modulo \\(\operatorname{row}C\\);
- whether the lift-direction dimension is sufficient.

For the case in which the compressed pairs are prescribed, the criterion involving

\\[ d'\_C=\dim\ker\Psi \\]

and the kernel of the prescribed row-pair matrix remains relevant.

For the more general affine lift formulation, use the common lift direction

\\[ \mathcal G_V = \mathcal R\cap(A\widehat V)^\perp \\]

and the affine independent-representative condition.

These are alternative parameterizations of the lift problem. They should not be applied cumulatively.

This is particularly important because a perfectly good abstract pencil may fail to be realizable by any admissible \\(L\\).

# Part VII. What I would not do

## 22. Avoid a generic perturbation argument

A tempting approach is to start with the six-dimensional template and add arbitrary small perturbations depending on \\(X\\).

This is not sufficient.

The property

\\[ \operatorname{rank}P_X(\lambda)=\omega \qquad\forall\lambda\in\mathbb C \\]

is not an open property in the naive sense of arbitrary perturbations of the coefficients.

A small perturbation may move a common zero of the maximal minors, create a finite eigenvalue, or introduce a rank drop at a special value of \\(\lambda\\).

The problem is especially serious because the spectral condition quantifies over all complex \\(\lambda\\).

One should use a structural invariant—such as the filtration pivots or a uniform Bézout identity—not continuity or genericity.

## 23. Avoid direct-sum padding as the primary hardness mechanism

As discussed, a block-diagonal padding construction cannot repair an arbitrary rank defect in the arithmetic block.

It is useful only if the arithmetic block is already spectrally admissible.

The right construction should be a coupled rectangular extension, or preferably a factorization

\\[ P_X(\lambda)=(\lambda I-D(X))H(X) \\]

whose rank is controlled by a uniform eigenvector-free property.

## 24. Avoid putting all arithmetic variables in \\(\ker\Psi\\)

This solves only the row-completion issue.

It leaves \\(H,H_A\\), and therefore \\(V\\), unchanged.

The arithmetic relation must influence the compressed geometry or the compatibility equations, not merely the invisible lift directions.

## 25. Avoid fixing the entire spectral map if doing so makes the system linear

A fixed \\(D\\) is excellent for proving uniform spectral admissibility. But the equation

\\[ H_A=DH \\]

is linear in \\(L\\) when \\(A,D\\) are fixed.

It may therefore destroy the expressive power needed for \\(\exists\mathbb R\\)-hardness.

The variable-dependent filtration-preserving \\(D(X)\\) is a better target.

# Part VIII. A more precise padding lemma to prove

I suggest making the next mathematical deliverable the following theorem.

Proposed theorem

Uniform rectangular spectral lemma

Let \\(S\\) be a parameter set and let

\\[ H(X)\in\mathbb C^{q\times k}, \qquad X\in S, \\]

satisfy

\\[ \operatorname{rank}H(X)=\omega \\]

and

\\[ \operatorname{im}H(X)=W \\]

for a fixed \\(\omega\\)-dimensional subspace \\(W\subseteq\mathbb C^q\\).

Suppose there is a family of linear maps

\\[ D(X):W\to\mathbb C^q \\]

such that:

1. \\(H_A(X)=D(X)H(X)\\);
2. \\(D(X)|\_W\\) is injective after subtraction of every scalar multiple of the inclusion \\(W\hookrightarrow\mathbb C^q\\), i.e.\
   \\[\
   D(X)w=\lambda w\
   \Longrightarrow w=0\
   \\]\
   for every \\(X\in S,\lambda\in\mathbb C\\).

Then

\\[ \operatorname{rank}(\lambda H(X)-H_A(X))=\omega \\]

for every \\(X\in S\\) and every finite \\(\lambda\in\mathbb C\\).

Moreover, condition 2 is guaranteed by the fixed shift-chain filtration with a nonzero leakage pivot.

The proof is immediate:

\\[ \begin{aligned} \lambda H(X)-H_A(X) &=(\lambda I-D(X))H(X),\\\ \operatorname{rank}P_X(\lambda) &=\operatorname{rank}\left((\lambda I-D(X))|\_W\right)\\\ &=\omega. \end{aligned} \\]

The important work is not proving this theorem. It is proving a realizability theorem that places the required family \\(H(X),H_A(X)\\) inside the image of the fixed pair map induced by \\(A,C\\).

That is the next genuine mathematical obstacle.

# Part IX. The distinction between spectral uniformity and arithmetic expressiveness

## 26. A necessary warning about the proposed factorization

There is a subtle but important logical issue.

Suppose we succeed in constructing

\\[ H_A(X)=D(X)H(X) \\]

with \\(D(X)|\_W\\) uniformly eigenvector-free.

Then the pencil condition is automatically satisfied for every \\(X\\) in the parameter space.

This means the pencil no longer distinguishes satisfying arithmetic assignments from nonsatisfying ones.

That is acceptable only if the arithmetic relation is encoded elsewhere in the feasibility problem.

In the proposed construction, the natural place is the realizability condition

\\[ (H(X),D(X)H(X))\in\operatorname{im}\Psi \\]

row by row, together with the fixed-row and row-independence requirements.

But this must be demonstrated, not assumed.

The reduction must have the form

\\[ \text{arithmetic system feasible} \iff \text{there exists a lift }L(X) \text{ satisfying all observer conditions}. \\]

It is not enough to prove

\\[ \text{arithmetic system feasible} \Longrightarrow \text{there exists a spectrally good pencil}. \\]

The reverse implication is equally important.

## 27. A useful conceptual separation

I would explicitly divide the construction into three layers:

| Layer         | Mathematical role                               | Desired behaviour                  |
| ------------- | ----------------------------------------------- | ---------------------------------- |
| Graph layer   | Encodes arithmetic variables through \\(V(X)\\) | Nonlinear and expressive           |
| Leakage layer | Guarantees uniform spectral admissibility       | Structurally rigid                 |
| Lift layer    | Realizes the prescribed pairs by ambient rows   | Exact linear-algebraic feasibility |

This is a more effective architecture than attempting to encode all three tasks in one large matrix.

The graph layer should carry the nonlinear information.

The leakage layer should carry a fixed filtration and a fixed nonzero pivot.

The lift layer should guarantee that the abstract pair data come from actual rows of \\(L\\), with the required independence.

This separation also makes failures much easier to diagnose.

# Part X. Concrete research plan

## 28. Priority 1: Prove the uniform filtration lemma in its most useful form

I would first formalize the following statement.

Let

\\[ W=W_0\supset W_1\supset\cdots\supset W\_\omega=\\{0\\} \\]

be a complete flag in \\(W\\).

Suppose the induced map \\(D(X):W\to W\oplus\mathbb Cg\\) satisfies:

- the quotient map from the final filtration level has a fixed nonzero leakage coefficient;
- each successive quotient map\
  \\[\
  W_j/W\_{j+1}\longrightarrow W\_{j+1}/W\_{j+2}\
  \\]\
  has a fixed nonzero pivot;
- all variable-dependent terms respect the filtration.

Then prove that \\(D(X)|\_W\\) has no eigenvectors.

This generalization will be more useful than the single shift-chain example because it allows multiple variable-dependent coefficients and more complicated block structures.

## 29. Priority 2: Solve the one-gate realizability problem

Choose the smallest nontrivial graph chart and attempt to encode

\\[ z=xy. \\]

The objective is not to optimize dimensions initially. It is to obtain an exact construction with:

- fixed \\(A,C,L_0\\);
- variable \\(L\\);
- graph kernel \\(V(X)\\);
- fixed image \\(W\\);
- filtration-compatible \\(D(X)\\);
- exact pair-lift feasibility;
- exact row independence.

Use symbolic calculations to verify all matrix identities and derive the polynomial equations defining the feasible parameter set.

A successful one-gate example would be a major advance. It would show that the spectral condition is no longer the bottleneck.

## 30. Priority 3: Prove soundness and completeness

For the one-gate construction, prove both directions.

Completeness: Given \\(x,y,z\\) satisfying \\(z=xy\\), construct \\(L\\) and verify every condition.

Soundness: Given any admissible \\(L\\), recover \\(x,y,z\\) and prove \\(z=xy\\).

The soundness direction must account for all possible lifts, including the directions in \\(\ker\Psi\\). Otherwise, extra lift freedom may create unintended feasible solutions.

This is where the exact pair-lift theorem is particularly important.

## 31. Priority 4: Extend to a circuit only after the one-gate proof

Once the multiplication gadget works, variable sharing and circuit composition can be addressed.

At that stage, one must ensure that:

- shared variables correspond to the same graph coordinates;
- each multiplication gate imposes exactly one intended polynomial relation;
- no unintended solutions arise from the lift kernel;
- the filtration pivots remain fixed;
- the fixed first row remains compatible;
- the dimensions and row-independence constraints scale polynomially.

There is no reason to attempt a full \\(\exists\mathbb R\\)-reduction before these issues are settled for a single gate.

# Part XI. Final answers to the four questions

## Question 1

Is there a general method to make the spectral condition uniform under variable-dependent perturbations?

Yes.

The most promising method is to arrange

\\[ H_A(X)=D(X)H(X), \\]

with

\\[ \operatorname{im}H(X)=W \\]

fixed, and to ensure that \\(D(X)|\_W\\) is uniformly eigenvector-free.

A fixed shift chain with a leakage coordinate provides a uniform certificate. More generally, variable-dependent lower-order terms can be allowed if they preserve a fixed filtration and its nonzero pivots.

Rows in \\(\ker\Psi\\) can be used to adjust independence without changing the pencil, but they cannot encode the graph variables by themselves.

## Question 2

Can the graph-chart construction be separated from the spectral block?

At the abstract pencil level, yes.

The natural graph quotient map is

\\[ H(X)=\begin{bmatrix}I&-X\end{bmatrix}, \\]

whose kernel is \\(V(X)\\) and whose image is fixed.

If one can realize

\\[ H_A(X)=D(X)H(X) \\]

with a filtration-compatible \\(D(X)\\), then the pencil has constant rank uniformly in \\(X\\).

However, a fixed \\(D\\) may make the construction too linear to encode arithmetic. A variable-dependent but filtration-preserving \\(D(X)\\) is preferable.

The main unresolved issue is realizing this pair through fixed \\(A,C\\) and variable \\(L(X)\\), subject to the pair-map compatibility conditions.

## Question 3

Is it more promising to use the template as padding? What is the minimal padding?

It is more promising to use the template as a structural spectral mechanism than as an independent direct-sum block.

A direct-sum block cannot repair arbitrary rank defects in another pencil.

For the invariant-kernel rectangular mechanism, one extra output dimension is sharp:

\\[ q=\omega+1. \\]

But this is not a universal padding theorem for arbitrary arithmetic pencils.

The best formulation is a coupled rectangular guard whose image is fixed and whose kernel carries the arithmetic variables.

## Question 4

Should the hardness workstream first establish a general padding lemma?

Yes, but the lemma should be the uniform rectangular-pencil/filtration lemma, not the naive direct-sum padding lemma.

The concrete route is:

1. parameterize \\(V(X)\\) by a graph chart;
2. construct \\(H(X)\\) with fixed image and kernel \\(V(X)\\);
3. introduce a variable-dependent filtration-compatible leakage map \\(D(X)\\);
4. require \\(H_A(X)=D(X)H(X)\\);
5. solve the exact pair-lift problem for fixed \\(A,C,L_0\\);
6. encode one multiplication gate;
7. prove soundness and completeness;
8. only then extend to an arithmetic circuit.

# Final research judgement

Recommended direction

The uniform rectangular-pencil approach is the strongest route currently available.

The six-dimensional example has established that an invariant candidate kernel does not itself force spectral failure when \\(A(K_0)\not\subseteq K_0\\). The next step is to turn that phenomenon into a parameterized construction.

I would not spend the next round trying to perturb the six-dimensional example numerically. Nor would I start with a direct-sum arithmetic block.

Instead, I would work on the following exact target:

\\[ \boxed{ \begin{gathered} \ker H(X)=V(X)=\operatorname{graph}(X),\\\ \operatorname{im}H(X)=W\quad\text{fixed},\\\ H_A(X)=D(X)H(X),\\\ D(X)|\_W\text{ uniformly eigenvector-free},\\\ (H(X),H_A(X))\text{ realizable by fixed }A,C. \end{gathered} } \\]

The first four lines solve the uniform spectral problem. The fifth line is the genuine observer-realization problem.

There is one further strategic point: do not require the spectral condition to encode the arithmetic relation. It is perfectly legitimate—and probably preferable—to make spectral admissibility automatic on the entire parameterized family, provided the graph and lift constraints encode the arithmetic system exactly.

The remaining challenge is then sharply localized: construct a fixed ambient pair \\((A,C)\\) whose row-pair map realizes a sufficiently expressive family of graph-dependent compressed pairs while preserving the filtration pivots.

That is where the next mathematical effort should go.

In my assessment, Report 67 points toward a substantially better research architecture. It does not yet provide an arithmetic gadget or a hardness proof, but it identifies a concrete intermediate theorem that is both plausible and independently valuable. The next decisive milestone should be a one-multiplication-gate realization theorem, not another collection of isolated spectral examples.&#x20;

67_uniformity_question(1).md
