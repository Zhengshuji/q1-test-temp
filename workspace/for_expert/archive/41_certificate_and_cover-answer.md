# Mathematical review of `41_certificate_and_cover.md`

The new report makes an important advance. I agree with its left-inverse theorem, its polynomial-degree calculation, and its identification of the remaining chart issue. However, I think there is a stronger answer to the central question than the factorisation proposed in Part IV.

The chart cover can be removed from the existential spectral-feasibility formulation altogether. The most direct route is not the proposed factorisation

\\[ P=P_1R, \\]

but a polynomial generalized-inverse identity

\\[ \boxed{P(\lambda)Y(\lambda)P(\lambda)=P(\lambda).} \\]

Here \\(P(\lambda)=\lambda H-H_A\\), and \\(Y\\) is an auxiliary polynomial matrix. Under the correct normal-rank hypothesis, this identity is equivalent to the absence of every finite rank drop. Moreover, in your degree-one pencil setting, \\(Y\\) admits an explicit degree bound:

\\[ \boxed{\deg Y\leq 2\omega-2.} \\]

This gives a chart-free, polynomial-size algebraic certificate directly for the original rectangular pencil. It avoids selecting a column chart and avoids enumerating maximal minors.

There are, however, several important distinctions:

1. Your proposed \\(P_1R\\) formulation is not sufficient as written: it needs a right-inverse condition on \\(R\\).
2. The generalized-inverse formulation repairs this problem without introducing separate left and right factors.
3. Removing charts from the existential encoding does not automatically remove them from the geometric analysis of generic feasibility, irreducible components, or real-point density.
4. The report's statement about the degree of the bad locus needs qualification: a bound on the degree of a polynomial certificate is not automatically a bound on the geometric degree of the bad locus.

I will establish these points carefully.

## 1. The left-inverse theorem: correct, with an important scope distinction

The report states that for a polynomial matrix

\\[ P(\lambda)\in F[\lambda]^{q\times\omega} \\]

of full column normal rank,

\\[ \gcd\\{\text{all }\omega\times\omega\text{ minors of }P\\}\in F^\times \\]

if and only if there exists

\\[ X(\lambda)\in F[\lambda]^{\omega\times q} \\]

such that

\\[ X(\lambda)P(\lambda)=I\_\omega. \\]

This is correct. The constructive formula and degree estimate in Part II are also correct.&#x20;

41_certificate_and_cover.md



The theorem is an instance of a general fact about matrices over a polynomial ring: a full-column-rank matrix has a polynomial left inverse precisely when its maximal minors generate the unit ideal.

### 1.1 Why the forward implication holds

Suppose

\\[ X(\lambda)P(\lambda)=I\_\omega. \\]

For every row subset \\(I\\) of size \\(\omega\\), let \\(E_I\\) select the rows in \\(I\\). By the Cauchy–Binet formula, every \\(\omega\times\omega\\) minor of \\(XP\\), and hence every entry of \\(I\_\omega\\), is a polynomial combination of the \\(\omega\\)-minors of \\(P\\).

In particular, the determinant of \\(I\_\omega\\) is one of those combinations. Therefore

\\[ 1\in \left\langle \text{all }\omega\times\omega\text{ minors of }P \right\rangle. \\]

Equivalently, their gcd is a unit.

### 1.2 Why the converse holds

Let

\\[ P_I=E_IP \\]

denote the square submatrix formed by selecting \\(\omega\\) rows.

If the maximal minors have gcd one, there exist polynomials \\(u_I\\) such that

\\[ \sum_I u_I(\lambda)\det(P_I(\lambda))=1. \\]

The adjugate identity gives

\\[ \operatorname{adj}(P_I)E_IP = \det(P_I)I\_\omega. \\]

Multiplying by \\(u_I\\) and summing,

\\[ \left(\sum_Iu_I\operatorname{adj}(P_I)E_I\right)P =I\_\omega. \\]

Thus one can take

\\[ X=\sum_Iu_I\operatorname{adj}(P_I)E_I. \\]

For your reduced pencil

\\[ P(\lambda)=\lambda U-G, \\]

every maximal minor has degree at most \\(\omega\\). The bounded-degree Bézout result gives

\\[ \deg u_I\leq\omega-1. \\]

Since

\\[ \deg\operatorname{adj}(P_I)\leq\omega-1, \\]

we obtain

\\[ \boxed{\deg X\leq2\omega-2.} \\]

This proof is sound.

### 1.3 A qualification about the field

The theorem is valid over any field \\(F\\), provided the gcd and polynomial identities are interpreted in \\(F[\lambda]\\).

For real system data, taking \\(F=\mathbb R\\) is appropriate. A collection of real polynomials has a common root in \\(\mathbb C\\) if and only if its gcd in \\(\mathbb R[\lambda]\\) is nonconstant. Thus the real polynomial certificate captures the requirement that the pencil have full rank at every complex finite spectral parameter.

## 2. The coefficient equations are correct

For

\\[ X(\lambda)=\sum\_{j=0}^{2\omega-2}X_j\lambda^j, \\]

the identity

\\[ X(\lambda)(\lambda U-G)=I\_\omega \\]

gives

\\[ -X_0G=I\_\omega, \\]

\\[ X\_{j-1}U-X_jG=0, \qquad 1\leq j\leq2\omega-2, \\]

and

\\[ X\_{2\omega-2}U=0. \\]

There are \\(2\omega\\) coefficient equations, counting the constant coefficient and the coefficients through degree \\(2\omega-1\\). The report has this right.&#x20;

41_certificate_and_cover.md



The caution in lines 38–40 is also correct.&#x20;

41_certificate_and_cover.md



Indeed,

\\[ X\_{2\omega-2}U=0 \\]

does not imply \\(X\_{2\omega-2}=0\\) unless \\(U\\) is square and invertible. In the rectangular case, it only says that \\(X\_{2\omega-2}\\) vanishes on \\(\operatorname{im}U\\).

This is not a technical nuisance: the certificate is genuinely rectangular.

### One point I would correct in the comparison table

The report describes the left-inverse certificate as having “linear” dependence on \\(R\\).&#x20;

41_certificate_and_cover.md



That needs more precise wording.

The entries of \\(U\\) and \\(G\\) are affine-linear in the original augmentation parameters \\(R\\). But the coefficient equations contain products such as

\\[ X_jU,\qquad X_jG. \\]

If \\(X_j\\) is also an existential unknown, these are bilinear expressions in the joint variables \\((R,X_j)\\).

The accurate comparison is:

- the pencil coefficients depend affinely on \\(R\\);
- the certificate equations have degree at most two in the joint variables \\((R,X)\\);
- the certificate has polynomially many variables and equations.

This is still a substantial improvement over the explicit-minor Bézout system. But it is not a linear system in the joint unknowns.

Likewise, a polynomial degree bound in \\(\lambda\\) should not be called a bound on the geometric degree of the bad locus without an additional argument. I return to this in Section 7.

# 3. Question 1: the proposed factorisation is insufficient as stated

The report proposes

\\[ P(\lambda)=P_1(\lambda)R(\lambda), \\]

where

\\[ P_1\in\mathbb C[\lambda]^{q\times\omega}, \qquad R\in\mathbb C[\lambda]^{\omega\times k}, \\]

and requires \\(P_1\\) to have full column rank everywhere and a polynomial left inverse

\\[ XP_1=I\_\omega. \\]

The intended idea is reasonable: isolate a rank-\\(\omega\\) polynomial basis for the image of \\(P\\), then represent the original pencil in that basis.

However, the proposed conditions do not guarantee that \\(P\\) has rank \\(\omega\\) at every finite \\(\lambda\\).

The missing condition is that \\(R(\lambda)\\) must have full row rank everywhere.

### 3.1 A one-dimensional counterexample

Take

\\[ P(\lambda)=\lambda. \\]

Let

\\[ P_1(\lambda)=1,\qquad R(\lambda)=\lambda,\qquad X(\lambda)=1. \\]

Then

\\[ P=P_1R,\qquad XP_1=1. \\]

The proposed conditions are satisfied, but

\\[ \operatorname{rank}P(0)=0<1. \\]

The rank drop occurs entirely in the factor \\(R\\).

Thus the left-invertibility of \\(P_1\\) alone is insufficient.

### 3.2 The corrected factorisation formulation

The appropriate formulation is

\\[ P=P_1R, \\]

together with

\\[ XP_1=I\_\omega, \qquad RZ=I\_\omega, \\]

for polynomial matrices

\\[ X\in F[\lambda]^{\omega\times q}, \qquad Z\in F[\lambda]^{k\times\omega}. \\]

The two inverse identities have different purposes:

- \\(XP_1=I\_\omega\\) ensures that \\(P_1(\lambda)\\) has full column rank at every finite \\(\lambda\\).
- \\(RZ=I\_\omega\\) ensures that \\(R(\lambda)\\) has full row rank at every finite \\(\lambda\\).

Then

\\[ \operatorname{rank}P(\lambda)=\omega \\]

for every finite \\(\lambda\\), since

\\[ P(\lambda)=P_1(\lambda)R(\lambda) \\]

is a product of a full-column-rank matrix and a full-row-rank matrix of inner dimension \\(\omega\\).

Conversely, if \\(P\\) has constant rank \\(\omega\\) at every finite \\(\lambda\\), such a factorisation exists over \\(F[\lambda]\\).

The reason is that \\(F[\lambda]\\) is a principal ideal domain. The column module of \\(P\\) is a free submodule of \\(F[\lambda]^q\\). The unit-gcd condition on the maximal minors means that this submodule is saturated, so the quotient is torsion-free. Over a PID, a finitely generated torsion-free module is free. The resulting short exact sequence splits, giving a polynomial basis \\(P_1\\) of the image with a polynomial left inverse. The coordinates of the columns of \\(P\\) in that basis form \\(R\\). Constant rank also gives a polynomial right inverse for \\(R\\).

This is a valid factorisation theorem.

But it is not the formulation I would recommend for your project, because it introduces two polynomial inverse certificates and a factorisation, whereas there is a more economical single identity.

# 4. The stronger chart-free theorem: polynomial generalized inverse

This is the main new result I recommend adding to the research chain.

Let

\\[ P(\lambda)\in F[\lambda]^{q\times k} \\]

have normal rank \\(\omega\\), meaning

\\[ \operatorname{rank}\_{F(\lambda)}P(\lambda)=\omega. \\]

Then the following are equivalent:

1. \\(P(\lambda)\\) has rank \\(\omega\\) at every finite point of the algebraic closure of \\(F\\).
2. The gcd of all \\(\omega\times\omega\\) minors of \\(P\\) is a nonzero constant.
3. There exists a polynomial matrix\
   \\[\
   Y(\lambda)\in F[\lambda]^{k\times q}\
   \\]\
   such that\
   \\[\
   \boxed{\
   P(\lambda)Y(\lambda)P(\lambda)=P(\lambda).\
   }\
   \\]

The third condition is the chart-free certificate.

I will give both directions of the proof.

## 4.1 The Smith normal form proof

Since \\(F[\lambda]\\) is a PID, \\(P\\) has a Smith normal form. Thus there exist unimodular polynomial matrices

\\[ S(\lambda)\in GL_q(F[\lambda]), \qquad T(\lambda)\in GL_k(F[\lambda]) \\]

such that

\\[ S(\lambda)P(\lambda)T(\lambda) = D(\lambda), \\]

where

\\[ D(\lambda)= \begin{bmatrix} d_1(\lambda)&&&0\\\ &\ddots&&\\\ &&d\_\omega(\lambda)&\\\ 0&&&0 \end{bmatrix}, \\]

with

\\[ d_1\mid d_2\mid\cdots\mid d\_\omega, \qquad d_i\ne0. \\]

The gcd of all \\(\omega\\)-minors is, up to a nonzero constant, the product

\\[ d_1d_2\cdots d\_\omega. \\]

Therefore the maximal minors have gcd one precisely when every \\(d_i\\) is a unit.

Now suppose

\\[ PYP=P. \\]

Set

\\[ Y'=T^{-1}YS^{-1}. \\]

Multiplying the identity on the left by \\(S\\) and on the right by \\(T\\) gives

\\[ DY'D=D. \\]

Consider the \\(i\\)-th diagonal entry for \\(1\leq i\leq\omega\\). We obtain

\\[ d_i^2Y'\_{ii}=d_i. \\]

Since \\(d_i\ne0\\) and \\(F[\lambda]\\) is an integral domain,

\\[ d_iY'\_{ii}=1. \\]

Thus \\(d_i\\) is a unit.

It follows that every Smith invariant factor is a unit, so

\\[ \gcd\\{\omega\text{-minors of }P\\}\in F^\times. \\]

Conversely, if every Smith invariant factor is a unit, then \\(D\\) is equivalent over \\(F[\lambda]\\) to the constant rank-\\(\omega\\) matrix

\\[ \begin{bmatrix} I\_\omega&0\\\ 0&0 \end{bmatrix}. \\]

That matrix has a polynomial generalized inverse, and transporting it through \\(S,T\\) gives a polynomial \\(Y\\) satisfying

\\[ PYP=P. \\]

This proves the equivalence.

## 4.2 A direct constructive proof and the degree bound

The Smith normal form proves existence, but for complexity we also need a degree bound.

Assume now that

\\[ \deg P\leq1, \qquad \operatorname{nrank}P=\omega. \\]

For row and column subsets \\(I\subseteq\\{1,\ldots,q\\}\\) and \\(J\subseteq\\{1,\ldots,k\\}\\), both of size \\(\omega\\), define

\\[ P\_{I,J}=P[I,J]. \\]

Let \\(E_J\in F^{k\times\omega}\\) be the column-selection matrix and \\(E_I\in F^{\omega\times q}\\) the row-selection matrix. Then

\\[ P\_{I,J}=E_IPE_J. \\]

Because the gcd of the maximal minors is one, the bounded-degree Bézout lemma gives polynomials \\(u\_{I,J}\\) satisfying

\\[ \sum\_{I,J}u\_{I,J}(\lambda)\det(P\_{I,J}(\lambda))=1, \\]

with

\\[ \deg u\_{I,J}\leq\omega-1. \\]

Define

\\[ \boxed{ Y(\lambda) = \sum\_{I,J} u\_{I,J}(\lambda) E_J\operatorname{adj}(P\_{I,J}(\lambda))E_I. } \\]

The dimensions are correct:

\\[ E_J\operatorname{adj}(P\_{I,J})E_I \in F[\lambda]^{k\times q}. \\]

Now use the fact that \\(P\\) has normal rank \\(\omega\\). Over the rational-function field \\(F(\lambda)\\), whenever \\(P\_{I,J}\\) is nonsingular,

\\[ P E_J\operatorname{adj}(P\_{I,J})E_I P = \det(P\_{I,J})P. \\]

To see this, note that

\\[ P = PE_J(P\_{I,J})^{-1}E_IP \\]

over \\(F(\lambda)\\): both sides have columns in the same \\(\omega\\)-dimensional column space, and their restrictions to the selected rows \\(I\\) agree. Multiplying by \\(\det(P\_{I,J})\\) gives the adjugate identity.

Consequently,

\\[ \begin{aligned} PYP &= \sum\_{I,J} u\_{I,J} PE_J\operatorname{adj}(P\_{I,J})E_IP\\\ &= \sum\_{I,J} u\_{I,J}\det(P\_{I,J})P\\\ &=P. \end{aligned} \\]

Finally,

\\[ \deg\operatorname{adj}(P\_{I,J})\leq\omega-1, \\]

so

\\[ \deg Y \leq (\omega-1)+(\omega-1). \\]

Therefore

\\[ \boxed{\deg Y\leq2\omega-2.} \\]

This is the crucial point: the degree bound is obtained without choosing a chart. The construction uses all minors in the proof of existence, but the resulting certificate is one polynomial matrix \\(Y\\), not a separate family of Bézout multipliers.

# 5. Applying the generalized-inverse theorem to your pencil

Return to the original matrices

\\[ H=\mathcal L N_K,\qquad H_A=\mathcal L A N_K, \\]

and define

\\[ P(\lambda)=\lambda H-H_A. \\]

On the rank-\\(\omega\\) stratum, suppose

\\[ \operatorname{rank}H=\omega \\]

and

\\[ \ker H\subseteq\ker H_A. \\]

The latter is exactly condition (5a).

## 5.1 The normal rank is automatically \\(\omega\\)

This is important: we do not need to impose normal rank separately.

Since

\\[ \ker H\subseteq\ker H_A, \\]

there exists a linear map \\(G\\) on \\(\operatorname{im}H\\) such that

\\[ H_A=GH. \\]

Choose a rank factorisation

\\[ H=UV, \\]

where

\\[ U\in F^{q\times\omega} \quad\text{has full column rank},\qquad V\in F^{\omega\times k} \quad\text{has full row rank}. \\]

Then

\\[ H_A=GV \\]

for a suitable \\(G\in F^{q\times\omega}\\).

Thus

\\[ P(\lambda) = (\lambda U-G)V. \\]

The matrix \\(\lambda U-G\\) has full column normal rank \\(\omega\\), because its leading coefficient \\(U\\) has full column rank. Since \\(V\\) has full row rank,

\\[ \boxed{ \operatorname{nrank}P=\omega. } \\]

This is exactly the normal-rank hypothesis needed in the generalized-inverse theorem.

## 5.2 The chart-free spectral criterion

It follows that, under (5a) and \\(\operatorname{rank}H=\omega\\),

\\[ \boxed{ (5b) \iff \exists Y(\lambda)\in F[\lambda]^{k\times q}: P(\lambda)Y(\lambda)P(\lambda)=P(\lambda). } \\]

Moreover, for the degree-one pencil,

\\[ \boxed{\deg Y\leq2\omega-2} \\]

is sufficient.

This is a direct formulation in terms of the original \\(q\times k\\) pencil. No column chart \\(S\\) is needed.

For \\(\omega=0\\), handle the case separately. Under (5a), \\(H=H_A=0\\), so \\(P=0\\), and the spectral condition is automatic.

# 6. The resulting polynomial-size encoding

This is the strongest practical consequence of the new theorem.

Write

\\[ Y(\lambda)=\sum\_{j=0}^{2\omega-2}Y_j\lambda^j, \qquad Y_j\in F^{k\times q}. \\]

Impose

\\[ \boxed{ (\lambda H-H_A)Y(\lambda)(\lambda H-H_A) = \lambda H-H_A. } \\]

Since the pencil has degree one and \\(Y\\) has degree at most \\(2\omega-2\\), the left-hand side has degree at most

\\[ 2+(2\omega-2)=2\omega. \\]

Thus the polynomial identity is equivalent to \\(2\omega+1\\) matrix coefficient equations, for degrees

\\[ 0,1,\ldots,2\omega. \\]

The number of scalar certificate variables is

\\[ \boxed{(2\omega-1)kq.} \\]

The coefficient equations are polynomial in the entries of \\(H,H_A,Y_0,\ldots,Y\_{2\omega-2}\\). Since \\(H,H_A\\) are affine in \\(R\\), the total algebraic degree in the joint unknowns is at most three.

This is polynomial-size in the explicit matrix dimensions.

### 6.1 Comparison with the reduced left-inverse certificate

| Feature                  | Reduced left inverse           | Original-pencil generalized inverse |
| ------------------------ | ------------------------------ | ----------------------------------- |
| Matrix being certified   | \\(q\times\omega\\)            | \\(q\times k\\)                     |
| Requires a column chart  | Yes                            | No                                  |
| Certificate              | \\(XP=I\_\omega\\)             | \\(PYP=P\\)                         |
| Certificate variables    | \\((2\omega-1)\omega q\\)      | \\((2\omega-1)kq\\)                 |
| Degree in \\(\lambda\\)  | \\(\deg X\leq2\omega-2\\)      | \\(\deg Y\leq2\omega-2\\)           |
| Coefficient equations    | \\(2\omega\\) matrix equations | \\(2\omega+1\\) matrix equations    |
| Degree in joint unknowns | At most two                    | At most three                       |

The original-pencil certificate has more variables and a higher algebraic degree, but it removes the need to select \\(S\\).

For your purpose, that is a favourable trade-off.

### 6.2 Can the degree three be reduced?

Possibly, but I would not make that the immediate priority.

The factorisation approach with

\\[ P=P_1R,\qquad XP_1=I,\qquad RZ=I \\]

uses bilinear equations rather than the cubic equation \\(PYP=P\\). However, it introduces several polynomial matrices and requires degree bounds for all of them.

The generalized-inverse certificate has a direct and explicit degree bound. It is therefore the safer theorem to establish first.

# 7. Question 2: can a polynomial number of charts suffice?

My answer is:

There is no need for a polynomial chart bound in the existential feasibility formulation. But the question remains meaningful for the geometric analysis of generic feasibility.

These are different issues.

## 7.1 Why charts are unnecessary for the decision problem

The rank-\\(\omega\\) condition on \\(H\\) can itself be encoded without choosing a nonzero minor.

Introduce

\\[ U\in F^{q\times\omega}, \qquad V\in F^{\omega\times k}, \\]

and impose

\\[ H=UV. \\]

Then introduce left and right inverses

\\[ J\in F^{\omega\times q}, \qquad Z\in F^{k\times\omega} \\]

satisfying

\\[ JU=I\_\omega,\qquad VZ=I\_\omega. \\]

These equations ensure

\\[ \operatorname{rank}U=\omega,\qquad \operatorname{rank}V=\omega, \\]

and therefore

\\[ \operatorname{rank}H=\omega. \\]

Similarly, impose

\\[ H_A=GV. \\]

Together,

\\[ H=UV,\qquad H_A=GV \\]

encode condition (5a) on the rank-\\(\omega\\) stratum.

The spectral condition is then encoded by the generalized-inverse identity

\\[ (\lambda H-H_A)Y(\lambda)(\lambda H-H_A) = \lambda H-H_A. \\]

This is one polynomial system for the entire rank-\\(\omega\\) stratum. It does not require a choice of \\(S\\).

The factorisation variables \\(U,V,G,J,Z\\) are auxiliary existential variables. They are not fixed charts; they range over all possible rank factorizations.

Thus the number of coordinate charts

\\[ \binom{k}{\omega} \\]

does not enter the size of the existential formulation.

## 7.2 What this does not prove

It does not prove that the rank-\\(\omega\\) stratum is irreducible.

It does not prove that a generic point of one chart represents all irreducible components.

It does not prove a polynomial bound on the number of irreducible components.

It does not establish a polynomial-time procedure for deciding generic feasibility.

The distinction is important. The factorisation

\\[ H=UV \\]

is a global parametrisation with auxiliary variables, but the set of \\(R\\)'s for which \\(\operatorname{rank}H(R)=\omega\\) may still be reducible.

For example, the intersection of a determinantal variety with an affine-linear family need not be irreducible. The observer-induced parameter family is special, but no irreducibility theorem for it has yet been established in the research chain.

### 7.3 What about a generic pivot chart?

A chart selected at one generic point covers a nonempty Zariski-open subset of the irreducible component on which its pivot minor is not identically zero.

It need not cover other irreducible components.

For an irreducible component on which that particular minor vanishes identically, another chart is necessary.

Therefore the proposed strategy of using “the pivots of a single generic point, plus a polynomial number of exceptional ones” requires a separate structural theorem. It does not follow from the rank factorisation or the open-or-empty dichotomy.

I would not make such a claim at present.

### Recommendation on Question 2

Do not pursue a polynomial chart-cover bound as a prerequisite for the complexity formulation. Replace the chart-based encoding by the generalized-inverse certificate.

Retain the chart and component analysis only for questions about:

- generic feasibility;
- the geometry of the bad locus;
- irreducible components;
- real-point density.

That is a much cleaner division of labour.

# 8. Question 3: the chart-free split by \\((\omega+1)\\)-minors and \\(\omega\\)-minors

The proposed split is mathematically correct:

\\[ \begin{aligned} &\text{all }(\omega+1)\text{-minors vanish identically}\\\ &\qquad\wedge\\\ &\text{the }\omega\text{-minors have no common finite complex root}. \end{aligned} \\]

The first condition ensures

\\[ \operatorname{nrank}P\leq\omega. \\]

The second ensures

\\[ \operatorname{rank}P(\lambda)\geq\omega \\]

at every finite \\(\lambda\\).

Together, they give

\\[ \operatorname{rank}P(\lambda)=\omega \quad\text{for all finite }\lambda. \\]

However, in your problem, the first condition is redundant once (5a) and \\(\operatorname{rank}H=\omega\\) have been imposed.

## 8.1 Why the first condition is automatic

Under (5a),

\\[ \ker H\subseteq\ker H_A. \\]

As shown above, this gives

\\[ P(\lambda)=(\lambda U-G)V \\]

with inner dimension \\(\omega\\).

Therefore

\\[ \operatorname{rank}P(\lambda)\leq\omega \\]

for every \\(\lambda\\), and in particular every \\((\omega+1)\\)-minor vanishes identically.

Thus, on the admissible rank-\\(\omega\\) stratum,

\\[ \boxed{ (5b) \iff \text{the }\omega\text{-minors of }P \text{ have no common finite root}. } \\]

The generalized-inverse certificate expresses this second condition without selecting a chart or enumerating minors.

## 8.2 A caution if the compatibility condition is removed

If one works with arbitrary polynomial matrices \\(P\\), then the first condition is not redundant.

For example, \\(P\\) may have normal rank strictly less than \\(\omega\\), in which case all \\(\omega\\)-minors vanish identically. A statement about the gcd of those minors must be interpreted carefully: the gcd of the zero family is zero, not a unit.

The clean general formulation is:

- require \\(\operatorname{nrank}P=\omega\\);
- require \\(PYP=P\\).

Or equivalently:

- require all \\((\omega+1)\\)-minors to vanish identically;
- require at least one \\(\omega\\)-minor not to vanish identically;
- require \\(PYP=P\\).

In the observer problem, the first two rank requirements are already guaranteed by the rank-\\(\omega\\) condition on \\(H\\) and (5a).

### Recommendation on Question 3

Yes, the split is a good conceptual presentation. But for the actual complexity encoding, I would replace the second conjunct by the generalized-inverse identity. Then the chart-free condition is simply

\\[ \boxed{ \operatorname{nrank}P=\omega \quad\wedge\quad PYP=P. } \\]

In your setting, the normal-rank condition follows from the other constraints, so only the generalized-inverse identity needs to be added.

# 9. Real and complex spectral parameters

One subtlety deserves explicit treatment in the next report.

Your system matrices are naturally real, but (5b) quantifies over

\\[ \lambda\in\mathbb C. \\]

The generalized-inverse formulation works directly over \\(\mathbb R[\lambda]\\):

\\[ Y(\lambda)\in\mathbb R[\lambda]^{k\times q}. \\]

This is not a weaker condition.

For a real polynomial matrix \\(P\\), the following are equivalent:

1. \\(P(\lambda)\\) has rank \\(\omega\\) for every \\(\lambda\in\mathbb C\\).
2. The maximal minors have no common complex root.
3. Their gcd in \\(\mathbb R[\lambda]\\) is a nonzero constant.
4. There exists \\(Y\in\mathbb R[\lambda]^{k\times q}\\) with \\(PYP=P\\).

The equivalence of 2 and 3 follows because a nonconstant real polynomial has a complex root. If the common root is nonreal, its conjugate is also a common root, so the corresponding real irreducible quadratic factor divides all the minors.

Thus the real existential synthesis problem can use real coefficients throughout, even though the spectral parameter ranges over the complex plane.

This is important for the \\(\exists\mathbb R\\) upper-bound discussion.

# 10. The revised fixed-order existential formulation

I recommend making the following the central theorem of the next research stage.

Fix a candidate order \\(q\\) and a rank \\(\omega\\). Let

\\[ H(R)=\mathcal L(R)N_K,\qquad H_A(R)=\mathcal L(R)AN_K. \\]

Introduce existential matrices

\\[ U,V,G,J,Z \\]

with dimensions

\\[ \begin{aligned} &U\in\mathbb R^{q\times\omega}, &&V\in\mathbb R^{\omega\times k},\\\ &G\in\mathbb R^{q\times\omega}, &&J\in\mathbb R^{\omega\times q},\\\ &Z\in\mathbb R^{k\times\omega}. \end{aligned} \\]

Impose

\\[ \boxed{ \begin{aligned} H(R)&=UV,\\\ H_A(R)&=GV,\\\ JU&=I\_\omega,\\\ VZ&=I\_\omega. \end{aligned} } \tag{A} \\]

These equations encode

\\[ \operatorname{rank}H(R)=\omega, \qquad \ker H(R)\subseteq\ker H_A(R). \\]

Now introduce

\\[ Y(\lambda)=\sum\_{j=0}^{2\omega-2}Y_j\lambda^j, \qquad Y_j\in\mathbb R^{k\times q}, \\]

and impose

\\[ \boxed{ (\lambda H(R)-H_A(R)) Y(\lambda) (\lambda H(R)-H_A(R)) = \lambda H(R)-H_A(R). } \tag{B} \\]

Coefficient comparison turns (B) into finitely many polynomial equations.

Then:

Theorem. For \\(\omega>0\\), a real augmentation \\(R\\) exists satisfying (5a), (5b), and

\\[ \operatorname{rank}H(R)=\omega \\]

if and only if the finite polynomial system (A)–(B) has a real solution.

For \\(\omega=0\\), use the separate equations

\\[ H(R)=0,\qquad H_A(R)=0, \\]

with no spectral certificate variables.

The full fixed-order problem is the finite disjunction over

\\[ 0\leq\omega\leq\min(q,k). \\]

This theorem would give a direct polynomial-size existential-real encoding of the fixed-order synthesis problem, without a chart cover and without a list of maximal minors.

A caveat about terminology: the auxiliary matrices \\(U,V,G,J,Z\\) are existential witnesses. The equivalence is an existence equivalence, not a one-to-one parametrisation of \\(R\\). That is perfectly sufficient for a decision-problem reduction.

# 11. What this means for the complexity question

The generalized-inverse certificate gives a clean upper-bound route.

Under the following model:

- rational \\(A,C,L_0\\), encoded in binary;
- \\(q\\) explicitly encoded, preferably in unary unless a polynomial bound is proved;
- \\(R\\) existentially quantified over \\(\mathbb R^{(q-r)\times n}\\);
- spectral condition required for every \\(\lambda\in\mathbb C\\);

the fixed-order problem has a polynomial-size existential real-algebraic formulation.

Therefore:

\\[ \boxed{ \mathrm{FEAS}(q)\in\exists\mathbb R. } \\]

This is an upper bound. It is not a hardness theorem and does not establish \\(\exists\mathbb R\\)-completeness.

The result is stronger than the previous minor-based encoding in one important sense: the polynomial size no longer depends on whether

\\[ \binom q\omega \\]

is polynomially bounded.

It also avoids the need to enumerate the \\(\binom{k}{\omega}\\) column charts.

### What remains open

The following questions are still genuine research problems:

1. Is the observer-induced fixed-order problem \\(\exists\mathbb R\\)-hard?
2. Can one prove a lower-complexity algorithm for \\(\omega=0\\) or \\(\omega=1\\) under a meaningful input model?
3. Can the special structure\
   \\[\
   H=\mathcal L N_K,\qquad H_A=\mathcal L A N_K\
   \\]\
   yield stronger complexity bounds than arbitrary affine pencils?
4. Can the observer-induced rank strata be shown to have additional irreducibility or component-count properties?
5. Can the generic feasibility problem be decided efficiently through a function-field polynomial-matrix computation without enumerating components?

The new certificate settles none of these by itself, but it puts the existential problem on a much firmer footing.

# 12. Revised answers to the three questions

| Question                                     | Answer                                                                                              | Recommendation                                                |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Can the chart cover be removed?              | Yes, for existential spectral feasibility.                                                          | Use \\(PYP=P\\) with a bounded-degree polynomial \\(Y\\).     |
| Is a polynomial chart-cover bound available? | No such bound follows from the present results; it is unnecessary for the existential encoding.     | Retain charts only for generic geometric analysis.            |
| Is the minor split preferable?               | It is conceptually correct, but the first conjunct is automatic under (5a) and rank \\(H=\omega\\). | Replace the gcd conjunct by the generalized-inverse identity. |

# 13. Recommended changes to `41_certificate_and_cover.md`

I would make the next revision in the following order.

First: retain Part II, but clarify the algebraic degree.

The reduced left-inverse certificate is valid and useful. Replace the phrase “dependence on \\(R\\) is linear” with “the pencil coefficients are affine-linear in \\(R\\); the joint certificate equations are bilinear.”

Do not identify the \\(\lambda\\)-degree of the certificate with the geometric degree of the bad locus.

Second: add the generalized-inverse theorem.

State

\\[ \operatorname{nrank}P=\omega \quad\Longrightarrow\quad \left[ \operatorname{rank}P(\lambda)=\omega\ \forall\lambda\in\mathbb C \iff \exists Y\in F[\lambda]^{k\times q}:PYP=P \right]. \\]

Then prove the Smith normal form equivalence and the degree bound

\\[ \deg Y\leq2\omega-2 \\]

for degree-one pencils.

Third: replace the chart-based complexity encoding.

Use the global rank factorisation

\\[ H=UV,\qquad H_A=GV \\]

with

\\[ JU=I\_\omega,\qquad VZ=I\_\omega, \\]

and append the generalized-inverse identity.

Fourth: preserve the chart discussion as a separate geometric workstream.

The chart-free existential formulation does not answer the real-density or irreducible-component questions. Those remain relevant to generic feasibility, but they no longer block the complexity upper bound.

## Final assessment

Left-inverse certificate validated

The left-inverse theorem and its degree bound are correct. The coefficient equations and the rectangular-matrix caution are also correct.

Proposed factorisation needs a repair

The condition \\(XP_1=I\\) alone is insufficient. A right-inverse condition \\(RZ=I\\) is necessary to rule out rank drops in the second factor.

Stronger chart-free certificate available

The identity

\\[ \boxed{ P(\lambda)Y(\lambda)P(\lambda)=P(\lambda) } \\]

is equivalent to the unit-gcd condition for the maximal minors of a polynomial matrix of normal rank \\(\omega\\). For your degree-one pencil, it has a certificate with

\\[ \deg Y\leq2\omega-2. \\]

This is the main result I would pursue next.

My overall recommendation: stop trying to bound the number of column charts for the fixed-order existential problem. The generalized-inverse certificate removes that obstruction at the formulation level. The next substantial theorem should be the chart-free, polynomial-size existential-real encoding of the full fixed-order spectral-feasibility problem. Keep the chart/component problem as a separate question about generic geometry, rather than allowing it to hold up the complexity analysis.