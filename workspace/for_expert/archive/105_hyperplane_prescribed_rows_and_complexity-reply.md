# **Review of Report 105: prescribed-row parameterization and fixed-**\\(p\\)**&#x20;complexity**

## **1. Overall assessment**

Report 105 is a substantial improvement over Report 103. It addresses the most important structural omission identified in the previous audit: the fixed rows \\(L_0\\) are now incorporated into the direction space itself, rather than being treated as an afterthought. The corrected fibre description is mathematically natural, and the use of relative Grassmann bundles is the right geometric formulation.

My assessment is:

- **The prescribed-row lemmas A and B are correct**, under the stated Euclidean identification of row vectors with vectors in \\(\mathbb R^n\\).
- **Theorem&#x20;**\\(1'\\)**&#x20;has the right structure and dimension formulas.** Its irreducibility assertion is also justified for each nonempty stratum, provided the relative bundles are understood as algebraic bundles over the indicated locally closed bases.
- **Lemma C is correct**, but its proof should explicitly explain why enlarging the row space cannot destroy the pencil-rank condition.
- **The chartwise gcd criterion needs one important lemma in the paper.** In this particular hyperplane layer, the assertion that a positive-degree generic gcd makes the whole chart bad can be justified by the invariant full-row-rank property of \\(H\\). It is not a general property of gcd specialization.
- **The fixed-**\\(p\\)**&#x20;polynomial-bit-complexity claim is plausible and can likely be proved**, but the report does not yet contain the bounds needed to state it as a theorem.
- The repeated-eigenvalue example is promising, but the report still needs to display the actual matrices and certificates. The table alone is not a reproducible certificate.

The most important point is that Report 105 has moved beyond merely repairing the geometry. It now has a potentially coherent route to an exact decision procedure on the geometrically simple subclass. The remaining work is to turn the computational description into a rigorous algorithmic theorem.

## **2. Audit of Lemmas A, B, C, and Theorem&#x20;**\\(1'\\)

### **2.1 Lemma A: prescribed-row compatibility**

The lemma is correct.

For \\(v\in E\_\mu^0\\), the definition gives

\\[ L_0v=0,\qquad L_0Av=0. \\]

Thus every row \\(\ell\in V_0\\) satisfies

\\[ \ell v=0,\qquad \ell Av=0. \\]

Consequently,

\\[ V_0\subseteq U_v^\perp, \qquad U_v=\operatorname{span}(v,Av). \\]

Since

\\[ D_v=K_0\cap U_v^\perp, \\]

we obtain

\\[ \begin{aligned} V_0\cap D_v &=V_0\cap K_0\cap U_v^\perp\\\ &=V_0\cap K_0, \end{aligned} \\]

where the second equality follows from \\(V_0\subseteq U_v^\perp\\).

Therefore

\\[ \dim\frac{V_0+D_v}{D_v} =\dim V_0-\dim(V_0\cap D_v) =\dim V_0-\dim(V_0\cap K_0) =\delta. \\]

This proves both the compatibility assertion and the independence of \\(\delta\\) from \\(v\\).

There is one presentational improvement worth making. State explicitly that \\(E\_\mu^0\\) is the space of directions compatible with the prescribed rows:

\\[ E\_\mu^0 = \\{v\in E\_\mu:L_0v=0,\ L_0Av=0\\}. \\]

This makes the logic transparent: the prescribed rows impose two linear conditions on the direction, and once those conditions are satisfied, compatibility with every subsequent row-space construction is automatic.

### **2.2 Lemma B: the prescribed-row fibre**

The fibre formula is correct.

Fix \\([v]\in\mathbb P(E\_\mu^0)\\). Every admissible row space satisfies

\\[ D_v\subseteq V\subseteq U_v^\perp, \qquad V_0\subseteq V, \qquad \dim V=q. \\]

Pass to the quotient

\\[ \mathcal Q_v=U_v^\perp/D_v. \\]

Then \\(V/D_v\\) is an \\(s\\)-dimensional subspace of \\(\mathcal Q_v\\), where

\\[ s=q-\dim D_v=q-k+1. \\]

It must contain

\\[ \overline V\_{0,v}=(V_0+D_v)/D_v, \qquad \dim\overline V\_{0,v}=\delta. \\]

Subspaces of dimension \\(s\\) containing a fixed \\(\delta\\)-dimensional subspace correspond bijectively to \\((s-\delta)\\)-dimensional subspaces of the quotient by that fixed subspace. Hence the fibre is

\\[ \boxed{ \operatorname{Gr}\left( s-\delta,\\, \mathcal Q_v/\overline V\_{0,v} \right). } \\]

The dimension calculation is also correct. If

\\[ r(v)=\dim\mathcal Q_v, \\]

then

\\[ \dim\left(\mathcal Q_v/\overline V\_{0,v}\right) =r(v)-\delta. \\]

Thus

\\[ \begin{aligned} \dim\operatorname{Gr} &=(s-\delta)\big((r(v)-\delta)-(s-\delta)\big)\\\ &=\boxed{(s-\delta)(r(v)-s)}. \end{aligned} \\]

The nonemptiness condition is

\\[ \boxed{\delta\le s\le r(v).} \\]

The two possible values of \\(r(v)\\) follow from the dimension of \\(U_v\\).

If \\(A\_{21}v=0\\), then \\(Av=\mu v\\), so \\(\dim U_v=1\\). Therefore

\\[ \dim U_v^\perp=n-1,\qquad \dim D_v=k-1, \\]

and

\\[ r(v)=n-1-(k-1)=\rho. \\]

If \\(A\_{21}v\ne0\\), then \\(v\\) and \\(Av\\) are linearly independent, so \\(\dim U_v=2\\). Hence

\\[ r(v)=n-2-(k-1)=\rho-1. \\]

Thus the stated formula is correct.

**A useful improvement:** explicitly record the two necessary feasibility inequalities:

\\[ \begin{array}{ll} \delta\le s\le \rho, &\text{on the eigen-direction stratum},\\\\[2mm] \delta\le s\le \rho-1, &\text{on the non-eigen stratum}. \end{array} \\]

These give immediate structural infeasibility tests before any pencil calculation.

### **2.3 Lemma C: full row rank**

The conclusion is correct, but the proof should be expanded.

Suppose a feasible design has row space \\(V\\) with

\\[ \dim V=t\<q. \\]

Because \\(V\subseteq U_v^\perp\\) and \\(q\le\dim U_v^\perp\\), we can choose a \\(q\\)-dimensional subspace

\\[ V'\quad\text{such that}\quad V\subseteq V'\subseteq U_v^\perp. \\]

This extension retains \\(V_0\\) and \\(D_v\\).

The key point is that the extension preserves the structural pencil conditions. Every row \\(x\in V'\\) annihilates \\(v\\) and \\(Av\\). If \\(v=Na\\), then

\\[ xNa=0,\qquad xANa=0. \\]

Thus both \\(xN\\) and \\(xAN\\) belong to the annihilator \\(a^\circ\subseteq\mathbb R^k\\).

Moreover, \\(D_v\subseteq V'\\) already supplies the entire \\((k-1)\\)-dimensional space \\(a^\circ\\) through restriction to \\(K_0\\). Therefore

\\[ \operatorname{row}H=a^\circ, \qquad \operatorname{row}H_A\subseteq a^\circ=\operatorname{row}H. \\]

In particular,

\\[ \operatorname{rank}H=k-1=\omega. \\]

The new pencil is obtained by adding rows to the old pencil. Adding rows cannot decrease rank. On the other hand, the structural containment above bounds the pencil rank by \\(\omega\\). Hence

\\[ \operatorname{rank}P'(\lambda)=\omega \\]

for every \\(\lambda\\) whenever the original pencil had this property.

This supplies the missing argument.

I recommend making Lemma C a separate normalization lemma, since it is useful beyond the immediate parameterization: it justifies working with \\(q\\)-dimensional row spaces even when the original design matrix is allowed to have dependent rows.

### **2.4 Theorem&#x20;**\\(1'\\)**: geometry and dimensions**

Theorem \\(1'\\) is essentially correct.

The bases are

\\[ B\_\mu^{\mathrm{eig}} = \mathbb P(E\_\mu^0\cap\ker A\_{21}), \\]

and

\\[ B\_\mu^{\mathrm{non}} = \mathbb P(E\_\mu^0) \setminus \mathbb P(E\_\mu^0\cap\ker A\_{21}). \\]

The first is projective space of dimension

\\[ h\_\mu^0-1, \\]

when nonempty. The second is a nonempty Zariski-open subset of\
\\(\mathbb P(E\_\mu^0)\\), so it has dimension

\\[ d\_\mu^0-1. \\]

The relative Grassmann fibres have dimensions

\\[ (s-\delta)(\rho-s) \\]

and

\\[ (s-\delta)(\rho-1-s), \\]

respectively. Therefore the total dimensions are

\\[ \boxed{ h\_\mu^0-1+(s-\delta)(\rho-s) } \\]

and

\\[ \boxed{ d\_\mu^0-1+(s-\delta)(\rho-1-s). } \\]

The irreducibility claim is also justified: each nonempty base is irreducible, and a Grassmann bundle with fixed fibre dimension over an irreducible base is irreducible.

There are three refinements I would make.

1\. **Specify the category.** Say that the bundles are algebraic relative Grassmann bundles over the relevant locally closed real algebraic bases. This avoids ambiguity about whether “defined over \\(\mathbb R\\)” means the equations, the geometric points, or the existence of real points.

2\. **Separate empty strata explicitly.** If \\(h\_\mu^0=0\\), the eigen-direction component is empty. If \\(d\_\mu^0=0\\), both components are empty. Do not use dimension \\(-1\\) without explaining the convention.

3\. **State the partition at the level of directions first.** The eigen and non-eigen bases are disjoint and cover \\(\mathbb P(E\_\mu^0)\\). Their relative Grassmann bundles are consequently disjoint as parameter spaces. This makes the “disjoint union” statement unambiguous.

With those refinements, I would accept Theorem \\(1'\\).

## **3. Audit of the chartwise gcd decision**

This is the most delicate part of Report 105. The report's conclusion can be correct, but it needs a structural lemma that is currently implicit.

### **3.1 Why a generic gcd usually does not settle every specialization**

For arbitrary polynomial families, the following inference is invalid:

\\[ \deg\_\lambda\gcd_I m_I(X,\lambda)>0 \quad\Longrightarrow\quad \text{every specialization }X=X_0\text{ has a common factor}. \\]

A common factor over the function field can specialize to a nonzero constant. For example, the factor \\(X\lambda+1\\) has positive \\(\lambda\\)-degree for generic \\(X\\), but specializes to \\(1\\) at \\(X=0\\). Thus a generic gcd computation alone does not generally justify a claim about every point of a parameter chart.

However, your hyperplane-layer construction has an additional invariant that changes the situation.

### **3.2 The full-rank leading-coefficient lemma**

On every admissible point of a fixed-direction Grassmann chart, the construction gives

\\[ \operatorname{rank}H=\omega. \\]

The maximal minors of

\\[ P(X,\lambda)=\lambda H(X)-H_A(X) \\]

are polynomials in \\(\lambda\\) of degree at most \\(\omega\\). Their coefficients of \\(\lambda^\omega\\) are precisely the corresponding maximal minors of \\(H(X)\\).

Since \\(\operatorname{rank}H(X)=\omega\\) at every chart point, we have

\\[ \boxed{ \text{For every }X_0,\text{ at least one maximal minor has degree }\omega. } \tag{3.1} \\]

This uniform full-degree property is the missing ingredient.

**Lemma (specialization of the common factor).**\
Let \\(K\\) be a field, let \\(X=(X_1,\ldots,X_d)\\), and let

\\[ m_1,\ldots,m_t\in K[X,\lambda] \\]

have \\(\lambda\\)-degree at most \\(\omega\\). Assume that for every admissible specialization \\(X=X_0\\), at least one \\(m_i(X_0,\lambda)\\) has degree exactly \\(\omega\\). If

\\[ \deg\_\lambda\gcd(m_1,\ldots,m_t) \\]

over \\(K(X)[\lambda]\\) is positive, then every admissible specialization has a nonconstant common factor.

**Proof.** By Gauss's lemma, a nonconstant common divisor over \\(K(X)[\lambda]\\) can be represented, after removing its content, by a polynomial

\\[ g(X,\lambda)\in K[X,\lambda] \\]

of positive \\(\lambda\\)-degree which divides every \\(m_i\\) in \\(K[X,\lambda]\\). Write

\\[ m_i=g h_i. \\]

At a specialization \\(X_0\\), \\(g(X_0,\lambda)\\) cannot be the zero polynomial: if it were, all the specialized maximal minors would vanish identically, contradicting the full-rank property (3.1).

Suppose instead that \\(g(X_0,\lambda)\\) were a nonzero constant. Since the degree of \\(h_i\\) in \\(\lambda\\) is at most \\(\omega-\deg\_\lambda g\\), every specialized \\(m_i(X_0,\lambda)\\) would have degree strictly less than \\(\omega\\). This again contradicts (3.1). Therefore \\(g(X_0,\lambda)\\) is nonconstant and divides every specialized minor. \\(\square\\)

This is exactly the specialization argument needed for your setting.

**Consequently, the two chart tests have the following interpretation:**

- If the function-field gcd has degree zero, the chart has a good point. Indeed, the nonzero resultant or the corresponding nonzero subresultant condition can be realized at some parameter point over an infinite field.
- If the function-field gcd has positive degree, the full-rank leading-coefficient lemma implies that every point of that chart is bad.

Thus the report's chartwise decision principle is defensible, but the reason is not a generic property of gcds. It is the invariant condition \\(\operatorname{rank}H=\omega\\) throughout the chart.

I strongly recommend adding this lemma immediately before the two bullet points in II.2. It is important enough to be stated and proved explicitly.

### **3.3 What the resultant test does and does not establish**

The statement

\\[ \operatorname{Res}\_\lambda(m_I,m_J)\not\equiv0 \\]

is a valid sufficient test for generic goodness: it proves that this pair has no common factor over the function field, and hence the gcd of the entire family is \\(1\\).

It is not a necessary test. It is possible that every pair of minors has a nonconstant gcd while the gcd of the whole family is \\(1\\). For example, consider

\\[ f_1=\lambda(\lambda-1),\quad f_2=\lambda(\lambda-2),\quad f_3=(\lambda-1)(\lambda-2). \\]

Every pair has a nonconstant gcd, but

\\[ \gcd(f_1,f_2,f_3)=1. \\]

Therefore:

- a nonzero pairwise resultant is a convenient positive certificate;
- failure to find such a pair is not a negative certificate;
- the exact decision procedure must compute the gcd of the full family, or use an equivalent simultaneous common-root test.

This distinction should be made explicit in II.2.

### **3.4 The chart cover must include the direction base**

There is one further scope issue.

The Grassmann charts parameterize the fibre over a fixed direction. For a geometrically simple eigenspace, this is enough: each eigenspace contributes at most one projective direction, so only the fibre charts need to be enumerated.

For a repeated eigenspace, however, the base

\\[ \mathbb P(E\_\mu^0) \\]

also has parameters. A complete chartwise analysis of that component must include:

1. affine charts for the projective direction base;
2. local trivializations of the quotient vector bundles;
3. Grassmann charts for the fibre over those base charts.

The coefficients of the pencil then depend on both direction parameters and Grassmann parameters. The full-rank leading-coefficient lemma can still be applied, provided the local trivialization is chosen on a chart where its denominators do not vanish and the structural rank condition holds throughout that chart.

This distinction matters for the claims about repeated eigenvalues. A fixed-direction fibre computation is not, by itself, a decision procedure for an entire repeated eigenspace.

## **4. Q1: How to establish polynomial bit complexity for fixed&#x20;**\\(p\\)

I agree with the report's decision not to claim polynomial bit complexity yet. Nevertheless, I think the desired theorem is achievable. The right approach is to give a sequence of explicit polynomial bounds, rather than attempting to bound the size of every intermediate expression generated by a naive Euclidean algorithm.

Let \\(\tau\\) denote the maximum input coefficient bit length, and let \\(n\\) be the state dimension. Assume \\(p\\) is fixed.

### **4.1 First establish polynomial height bounds for the compression**

The compression is

\\[ M=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN. \\]

The main issue is to avoid treating \\(N\\) as an arbitrary rational basis. You should specify how it is computed and normalized.

A suitable procedure is:

1. Clear denominators in the matrix defining \\(K_0\\).
2. Compute a rational nullspace basis using fraction-free Gaussian elimination.
3. Clear denominators in that basis and, if convenient, make its columns primitive integer vectors.
4. Form \\(N^{\mathsf T}N\\), \\(N^{\mathsf T}AN\\), and their rational inverse/product using fraction-free determinant or elimination algorithms.

The entries of \\(N\\) can be bounded using minors of the integerized matrix defining \\(K_0\\). Hadamard's inequality gives a bound of the form

\\[ \log \max\_{i,j}|N\_{ij}| \le \operatorname{poly}(n,\tau). \\]

The exact polynomial is not important for the fixed-\\(p\\) theorem, but it should be stated or cited.

The entries of \\(N^{\mathsf T}N\\) and \\(N^{\mathsf T}AN\\) then have polynomial bit length. The same is true of the entries of \\(M\\), because determinant and fraction-free elimination bounds control the inverse of \\(N^{\mathsf T}N\\).

You should therefore state a lemma of the following form:

> **Compression height lemma.** Given rational input matrices with maximum coefficient bit length \\(\tau\\), a rational basis \\(N\\) of \\(\ker[C;CA]\\) and the compressed matrix \\(M\\) can be computed in polynomial bit complexity. The bit lengths of all entries of \\(N\\) and \\(M\\) are bounded by a polynomial in \\(n\\) and \\(\tau\\).

This is a standard exact-linear-algebra result, but it is worth including in the paper because all later algebraic-number bounds depend on it.

### **4.2 Characteristic polynomial and eigenvalue heights**

Once the entries of \\(M\\) have polynomial bit length, the characteristic polynomial

\\[ \chi_M(t)=\det(tI-M) \\]

has integer coefficients of polynomial bit length after clearing denominators and taking a primitive part.

This follows from determinant bounds: each coefficient is a sum of principal minors, and the bit length of each minor is bounded by a polynomial in \\(n\\) and the entry bit lengths.

Every eigenvalue \\(\mu\\) is a root of \\(\chi_M\\). Consequently:

- its algebraic degree is at most \\(k\le n\\);
- its logarithmic height is bounded polynomially in \\(n\\) and \\(\tau\\);
- its real embeddings can be isolated using exact real-algebraic-number algorithms in polynomial bit complexity.

You do not need a bespoke height theorem. Cite a standard root-height bound for roots of integer polynomials, together with the standard bit-complexity results for real-root isolation and arithmetic in algebraic number fields.

A useful conservative formulation is

\\[ [\mathbb Q(\mu):\mathbb Q]\le n, \qquad h(\mu)\le \operatorname{poly}(n,\tau). \\]

For the paper, the important point is the polynomial bound, not the sharpest possible constant.

### **4.3 Eigenvectors and quotient-bundle bases**

On the geometrically simple subclass,

\\[ \dim\ker(M-\mu I)=1 \\]

for each real eigenvalue \\(\mu\\). Therefore the projective direction is uniquely determined.

A basis vector \\(a\\) for this eigenspace can be computed over

\\[ K=\mathbb Q(\mu) \\]

using exact Gaussian elimination. Cramer's rule or fraction-free elimination gives polynomial height bounds for its coordinates in terms of the entries of \\(M\\) and the height of \\(\mu\\).

The same argument applies to the bases needed for:

- \\(E\_\mu^0\\);
- \\(D_v\\);
- \\(U_v^\perp\\);
- \\(\mathcal Q_v/\overline V\_{0,v}\\).

Since all these spaces are obtained by kernels, images, sums, and quotients of matrices of dimension at most \\(n\\), their bases can be computed over \\(K\\) with polynomial bit complexity.

The report should make one point explicit: the quotient-bundle trivialization must be computed over the same algebraic number field as the eigenvector. It is not generally a rational-coordinate calculation when \\(\mu\notin\mathbb Q\\).

### **4.4 Number of chart parameters**

The number of free parameters in a fibre chart is

\\[ d\_{\mathrm{chart}} =(s-\delta)\big((r(v)-\delta)-(s-\delta)\big) =(s-\delta)(r(v)-s). \\]

Since

\\[ r(v)\le \rho\le 2p, \\]

we have

\\[ \boxed{d\_{\mathrm{chart}}\le p^2} \\]

(up to an inessential sharper constant).

Thus, for fixed \\(p\\), the number of variables in each chart is constant.

The number of Grassmann charts is

\\[ \binom{r(v)-\delta}{s-\delta}, \\]

which is bounded by a constant depending only on \\(p\\).

This is the key geometric reason a fixed-\\(p\\) algorithm is plausible.

### **4.5 Degrees and number of maximal minors**

The pencil entries are affine-linear in the chart variables and in \\(\lambda\\). A maximal minor of order \\(\omega=k-1\\) therefore has:

- degree at most \\(\omega\le n\\) in \\(\lambda\\);
- degree at most \\(\omega\le n\\) in the chart variables.

The number of maximal minors is

\\[ \binom{q}{k-1}\binom{k}{k-1} = k\binom{q}{q-k+1}. \\]

Because

\\[ s=q-k+1\le \rho\le 2p, \\]

this number is at most

\\[ n^{O(p)} \\]

for fixed \\(p\\).

The same is true of the total size of the list of minors, including their coefficient representations, once the polynomial bit bounds from the previous steps have been established.

### **4.6 Fraction-free subresultants are the right approach**

Your instinct in II.1 is correct: do not base a polynomial-bit-complexity proof on an unqualified rational-function Euclidean algorithm.

A naive Euclidean algorithm in

\\[ K(X_1,\ldots,X_d)[\lambda] \\]

can cause substantial numerator and denominator growth. Instead, use subresultant or fraction-free polynomial remainder sequences.

The relevant facts are:

- the degree in \\(\lambda\\) is at most \\(\omega\le n\\);
- the number of chart variables \\(d\\) is bounded in terms of fixed \\(p\\);
- the coefficient degrees in the chart variables are polynomially bounded in \\(n\\);
- the coefficient heights are polynomially bounded after the compression and algebraic-field computations.

Subresultant coefficients are determinants of matrices whose dimensions are controlled by the \\(\lambda\\)-degree. Consequently, their degrees in \\(X\\) and their coefficient bit lengths can be bounded by polynomial expressions in \\(n\\) and \\(\tau\\), for fixed \\(p\\).

There is an additional issue: the gcd is taken over a family of

\\[ n^{O(p)} \\]

maximal minors. The paper should state an explicit multi-polynomial gcd algorithm and bound its running time in terms of the number of input polynomials, their degrees, and their coefficient heights. It is not enough to discuss only the cost of one pairwise resultant.

An alternative is to formulate the common-root condition as a rank condition on a suitable Sylvester/Macaulay-type matrix. This can make the bit-complexity argument cleaner, but the matrix size must still be bounded explicitly. I would start with subresultants because the degree in \\(\lambda\\) is the naturally small parameter.

### **4.7 Irrational eigenvalues must be included consistently**

There is a mismatch in II.2:

> “Two-way decisions are available for rational eigenvalues; for irrational ones the direction screen is implemented over the number field … and the chart computation is still on rational eigenvalues only.”

This is not sufficient for a theorem covering the full geometrically simple subclass.

If \\(\mu\\) is irrational, then the fibre basis and pencil coefficients generally lie in \\(\mathbb Q(\mu)\\), not \\(\mathbb Q\\). The chart gcd must therefore be computed over

\\[ \mathbb Q(\mu)(X)[\lambda]. \\]

That is entirely compatible with the complexity strategy above. The algebraic degree is at most \\(n\\), and the height is polynomially bounded. But the implementation and theorem must actually include it.

If the current implementation only completes chart computations for rational eigenvalues, then the honest theorem is restricted to the subclass in which every relevant real eigenvalue is rational. That is a much narrower claim than geometric simplicity.

### **4.8 A suitable theorem statement**

I recommend aiming for this formulation:

> **Proposed fixed-**\\(p\\)**&#x20;theorem.** Fix \\(p\\). Given rational input data \\((A,C,L_0,q)\\), the hyperplane-layer feasibility problem can be decided in deterministic polynomial bit complexity on the subclass for which every real eigenvalue of the compression \\(M\\) has a one-dimensional eigenspace, provided the algorithm performs the chartwise gcd computation over the corresponding exact real algebraic number fields.

The proof should list the bounds in this order:

1. polynomial-size rational compression;
2. polynomial degree and height of the characteristic polynomial;
3. polynomial-size algebraic eigenvalue representations;
4. polynomial-size eigenvectors and quotient bases;
5. at most \\(p^2\\) chart variables;
6. \\(n^{O(p)}\\) maximal minors and a number of Grassmann charts depending only on \\(p\\);
7. polynomial bit complexity of the fraction-free gcd/subresultant computation.

I would not yet claim this theorem in the manuscript, but I think this is the right target.

## **5. Q2 and Q3: repeated eigenvalues and the right invariant**

### **5.1 The rank stratification of&#x20;**\\(A\_{21}|\_{E\_\mu^0}\\)

Let

\\[ B\_\mu=A\_{21}|\_{E\_\mu^0}, \qquad d\_\mu^0=\dim E\_\mu^0, \qquad b\_\mu=\operatorname{rank}B\_\mu. \\]

Then

\\[ \dim\ker B\_\mu=d\_\mu^0-b\_\mu. \\]

This gives three useful structural cases.

| Rank of \\(B\_\mu\\)      | Eigen-direction stratum          | Non-eigen stratum                           |
| ------------------------- | -------------------------------- | ------------------------------------------- |
| \\(b\_\mu=0\\)            | All of \\(\mathbb P(E\_\mu^0)\\) | Empty                                       |
| \\(0\<b\_\mu\<d\_\mu^0\\) | \\(\mathbb P(\ker B\_\mu)\\)     | Its complement in \\(\mathbb P(E\_\mu^0)\\) |
| \\(b\_\mu=d\_\mu^0\\)     | Empty                            | All of \\(\mathbb P(E\_\mu^0)\\)            |

This stratification is worth retaining. It determines which fibre dimension applies and gives a first classification of the possible geometry.

But it does **not** determine spectral feasibility. The counterexample in II.3 is already evidence of this: a special direction in \\(\ker B\_\mu\\) can behave differently from directions outside it, and the gcd depends on the full induced pencil, not merely on the rank of \\(B\_\mu\\).

I would therefore use the rank stratification as the first layer of a classification, not as the final invariant.

### **5.2 Define the bad set using the incidence variety**

For a fixed direction and a fixed Grassmann chart, let

\\[ m_I(X,\lambda) \\]

be the maximal minors of the pencil.

The natural bad locus is

\\[ \mathcal B = \left\\{ X:\exists\lambda\in\mathbb C \text{ such that }m_I(X,\lambda)=0 \text{ for every }I \right\\}. \\]

Equivalently, define the incidence set

\\[ \mathcal I = \left\\{(X,\lambda): m_I(X,\lambda)=0\text{ for every }I \right\\}. \\]

Then

\\[ \mathcal B=\operatorname{pr}\_X(\mathcal I). \\]

This formulation is more informative than saying simply that the bad set is “the set where the gcd has positive degree.” It makes the quantifiers explicit and separates:

- a fixed row-space being bad;
- every row-space in a fibre being bad;
- at least one row-space in a fibre being bad;
- every direction in an eigenspace being bad.

These are different questions.

For the fixed-\\(p\\) simple-eigenspace algorithm, the chartwise function-field gcd decides whether the entire fibre chart is good or bad, using the full-rank specialization lemma from Section 3. For repeated eigenspaces, one must also account for the direction parameters.

### **5.3 What should be classified?**

I recommend the following hierarchy.

**Level 1: structural direction geometry.**

Classify

\\[ E\_\mu^0,\qquad \ker(A\_{21}|\_{E\_\mu^0}), \\]

and the resulting eigen/non-eigen strata.

**Level 2: fibre geometry.**

For each direction stratum, classify the relative Grassmann fibre, including its dimension and prescribed-row constraints.

**Level 3: spectral incidence.**

On each local chart, study the simultaneous common-root incidence of all maximal minors.

**Level 4: existential feasibility.**

Determine whether the spectral-good locus is nonempty in the total parameter space.

This hierarchy is much cleaner than trying to force the entire repeated-eigenvalue problem into a single rank invariant.

A particularly useful algebraic object is the ideal generated by the maximal minors:

\\[ \mathfrak I_v = \langle m_I(X,\lambda): I\rangle \subseteq K[X,\lambda]. \\]

The question whether a chart is spectrally bad is whether the fibre over a parameter point has a common finite \\(\lambda\\)-root. For the entire chart, the common-factor calculation over \\(K(X)\\), together with the full-rank specialization lemma, gives the desired uniform conclusion.

For a repeated eigenspace, the corresponding ideal should be constructed over the combined direction and fibre parameters, after choosing local trivializations. Its algebraic structure, rather than the rank of \\(A\_{21}\\) alone, is the natural object for a more general classification.

## **6. Q4: the Paper II duality should be a theorem**

Yes. I think this should become a standalone proposition or theorem, because it is a genuine bridge between the ambient row-space geometry and Paper II's compressed description.

Let

\\[ \mathsf M=[N\ \ AN]. \\]

Define the linear map

\\[ \Phi:\mathbb R^n\longrightarrow \mathbb R^k\oplus\mathbb R^k, \qquad x\longmapsto (xN,xAN), \\]

where row vectors are being used.

For a row space \\(V\\), define

\\[ W=\Phi(V)=\operatorname{row}(V\mathsf M). \\]

Suppose \\(v=Na\\) is the hyperplane direction. Since

\\[ V\subseteq U_v^\perp, \\]

every \\(x\in V\\) satisfies

\\[ xNa=0,\qquad xANa=xAv=0. \\]

Thus

\\[ W\subseteq a^\circ\times a^\circ. \\]

If the Paper II hypotheses give

\\[ \pi_1(W)=\pi_2(W)=U, \qquad \dim U=k-1, \\]

then

\\[ U\subseteq a^\circ. \\]

Both spaces have dimension \\(k-1\\), so

\\[ \boxed{U=a^\circ.} \\]

Therefore

\\[ \boxed{ [a]=\mathbb P(\operatorname{Ann}(U)), \qquad v=Na. } \\]

This establishes the direction dictionary.

### **6.1 The cleanest statement**

I would formulate it as follows.

> **Hyperplane-layer duality proposition.**\
> Let \\(V\\) be an admissible ambient row space in the hyperplane layer, and let\
> \\[\
> W=\operatorname(V[N\ \ AN]).\
> \\]\
> If the two coordinate projections of \\(W\\) coincide and have dimension \\(k-1\\), then there is a unique projective direction \\([a]\in\mathbb P^{k-1}\\) such that\
> \\[\
> \pi_1(W)=\pi_2(W)=a^\circ.\
> \\]\
> The corresponding ambient direction is \\(v=Na\\), and every row of \\(V\\) annihilates both \\(v\\) and \\(Av\\).

The reverse direction should be stated with the appropriate qualification: a compressed subspace \\(W\\) satisfying the Paper II conditions determines the direction \\(a\\), but one still needs an ambient lift \\(V\\) satisfying the prescribed-row and dimension conditions.

### **6.2 The fibres of&#x20;**\\(V\mapsto W\\)

The map \\(\Phi\\) is generally not injective. Its kernel is

\\[ \ker\Phi = \\{x:xN=0,\ xAN=0\\}. \\]

Equivalently, under the Euclidean identification,

\\[ \ker\Phi=(K_0+AK_0)^\perp. \\]

For a fixed compressed subspace \\(W\\), put

\\[ T_W=\Phi^{-1}(W). \\]

Any ambient row space mapping onto \\(W\\) must satisfy

\\[ V\subseteq T_W,\qquad \Phi(V)=W. \\]

For the prescribed-row problem, also put

\\[ S=V_0+D_v. \\]

For a compatible lift, \\(S\subseteq T_W\\). Passing to the quotient gives an induced map

\\[ \overline\Phi:T_W/S\longrightarrow W/\Phi(S). \\]

The ambient lifts are exactly the subspaces

\\[ \overline V=V/S\subseteq T_W/S \\]

of dimension

\\[ q-\dim S \\]

such that

\\[ \boxed{ \overline\Phi(\overline V)=W/\Phi(S). } \\]

Thus the fibre is a surjectivity locus inside a Grassmannian, rather than generally an entire Grassmannian.

This is a useful and precise answer to the question about fibres. It also explains why Paper II's compressed representation can be more economical than Report 105's ambient parameterization: the map \\(V\mapsto W\\) forgets directions in \\(\ker\Phi\\), while the ambient formulation retains the degrees of freedom needed to enforce \\(L_0\\) and the prescribed row count.

I would not claim that every Paper II compressed \\(W\\) has an admissible ambient lift. The lift conditions are part of the dictionary and must be retained.

## **7. Q5: negative certificates**

The report's direction-screen certificate is valid:

\\[ E\_\mu^0=0 \quad\text{for every real eigenvalue }\mu \\]

implies that no structural direction exists in the hyperplane layer. This is a particularly clean negative certificate because it requires only exact linear algebra over the relevant real eigenvalue fields.

There are stronger certificates, but they should be distinguished by their logical strength.

### **7.1 Fibre-dimension certificates**

For each admissible direction, the fibre must be nonempty. Thus if

\\[ \delta>s \\]

or

\\[ s>\rho \\]

on every eigen-direction stratum, and

\\[ \delta>s \\]

or

\\[ s>\rho-1 \\]

on every non-eigen stratum, then no candidate row space exists.

This is a structural negative certificate, still requiring no pencil gcd computations.

In particular, if all admissible directions are non-eigen and

\\[ s>\rho-1, \\]

the layer is infeasible.

### **7.2 Universal spectral-obstruction certificates**

A stronger certificate is to exhibit, for every admissible candidate row space, a fixed nonzero vector in the kernel of the pencil at some finite \\(\lambda\\).

For example, for a given direction \\(v\\), if there exist

\\[ z\in K_0\setminus\\{0\\},\qquad \lambda_0\in\mathbb C \\]

such that

\\[ \lambda_0 z-Az\in U_v, \\]

then every row \\(x\in V\subseteq U_v^\perp\\) satisfies

\\[ x(\lambda_0 z-Az)=0. \\]

Consequently,

\\[ P(\lambda_0)z=0, \\]

and the candidate is spectrally infeasible.

This is a valid certificate for that direction. To certify the entire layer, one needs a condition that covers every admissible direction, possibly with \\(z\\) and \\(\lambda_0\\) depending on \\(v\\).

A particularly simple special case is

\\[ Az=\lambda_0z \\]

for some nonzero \\(z\in K_0\\) that is annihilated by every admissible row space. Then \\(\lambda_0\\) is a universal pencil obstruction.

Such certificates may be useful in special instances, but I would not expect them to characterize all infeasible cases.

### **7.3 Exact algebraic negative certificates**

The most general route is to prove that every chart has positive-degree generic gcd. By the full-rank specialization lemma, this proves that every point in every chart is bad.

For a geometrically simple eigenspace, this is a finite list of exact computations. A negative certificate can consist of:

1. the complete list of eigenvalues and directions;
2. the finite Grassmann chart cover;
3. for each chart, a nonconstant common divisor of all maximal minors over the appropriate function field;
4. exact divisibility identities.

This is a valid exact certificate, although it may be large.

For repeated eigenspaces, the certificate must cover the direction parameters as well. A calculation on only a few selected directions cannot certify the whole eigenspace.

## **8. An additional issue: the number of prescribed rows versus their rank**

There is one important point that is not addressed in Report 105 and that I would resolve before accepting Lemma C.

The original observer has the form

\\[ L=\begin{bmatrix}L_0\\\R\end{bmatrix}, \qquad L_0\in\mathbb Q^{r_0\times n}, \qquad R\in\mathbb R^{(q-r_0)\times n}. \\]

Write

\\[ t_0=\operatorname{rank}L_0=\dim V_0. \\]

Then every such observer necessarily satisfies

\\[ \boxed{ \dim V\le t_0+(q-r_0). } \tag{8.1} \\]

Therefore, unless

\\[ \operatorname{rank}L_0=r_0, \\]

the row space of an observer with \\(q\\) rows cannot in general have dimension \\(q\\).

This matters because Lemma C claims that a feasible design can be replaced by one with

\\[ \dim V=q. \\]

That conclusion does not follow merely from \\(q\le\dim U_v^\perp\\). It also requires that the prescribed block have full row rank.

For example, if \\(q=r_0\\) and \\(L_0\\) has dependent rows, there are no free rows at all. The only possible row space is \\(V_0\\), whose dimension is strictly less than \\(q\\). It cannot be enlarged while retaining the prescribed block and the same number of rows.

### **How to repair this**

There are two possible routes.

**Route A: make full row rank of&#x20;**\\(L_0\\)**&#x20;an explicit standing assumption.**

If the intended problem assumes

\\[ \operatorname{rank}L_0=r_0, \\]

then Lemma C is valid with its present target dimension \\(q\\). The assumption should be stated in Part I and traced to the original problem formulation. It should not be left implicit.

**Route B: retain possibly dependent prescribed rows.**

Then define

\\[ q\_{\mathrm{eff}}=t_0+q-r_0. \\]

This is the maximum possible dimension of the row space of an observer with the prescribed block \\(L_0\\) and exactly \\(q-r_0\\) free rows.

The normalization lemma should target \\(q\_{\mathrm{eff}}\\), not \\(q\\):

\\[ \boxed{ \dim V=q\_{\mathrm{eff}} } \\]

whenever a feasible design can be extended to that dimension and

\\[ q\_{\mathrm{eff}}\le \dim U_v^\perp. \\]

The corresponding fibre parameter becomes

\\[ s\_{\mathrm{eff}} =q\_{\mathrm{eff}}-(k-1) =t_0+q-r_0-k+1, \\]

rather than \\(s=q-k+1\\).

The prescribed-row quotient dimension remains

\\[ \delta=t_0-\dim(V_0\cap K_0), \\]

so the fibre would be

\\[ \operatorname{Gr}\left( s\_{\mathrm{eff}}-\delta,\\, \mathcal Q_v/\overline V\_{0,v} \right), \\]

with dimension

\\[ (s\_{\mathrm{eff}}-\delta)(r(v)-s\_{\mathrm{eff}}). \\]

This is not a cosmetic change: it changes the dimension of the parameter space and the exact number of free chart variables.

**My recommendation:** check whether full row rank of \\(L_0\\) is an explicit assumption in the original problem. If it is, add it prominently to Report 105. If it is not, use Route B and revise Lemma C, Theorem \\(1'\\), and the chart parameter count accordingly.

## **9. The repeated-spectrum example: useful, but not yet a complete certificate**

The example in II.3 is conceptually important. It is intended to show that feasibility can vary within one repeated eigenspace:

\\[ E_1=\operatorname{span}(e_1,e_2). \\]

The direction \\((1,1)\\) is reported to be good, while several other directions are reported to be bad.

If verified with complete data, this is a strong demonstration that one cannot simply choose an arbitrary representative eigenvector for each distinct eigenvalue.

However, the report still does not provide enough information to independently reproduce the example.

### **9.1 The full matrix&#x20;**\\(A\\)**&#x20;is missing**

The statement

> “arrange the compression to be \\(M=\operatorname{diag}(1,1,2,3)\\) (by choosing the action of \\(A\\) on \\(K_0\\))”

does not specify the complete input.

In particular, \\(K_0\\) is defined by

\\[ K_0=\ker\begin{bmatrix}C\\\CA\end{bmatrix}. \\]

Thus specifying the compression of \\(A\\) on \\(K_0\\) is not sufficient to specify \\(K_0\\): the rows of \\(CA\\) also depend on the action of \\(A\\) outside \\(K_0\\).

The report needs to give:

- the full rational \\(8\times8\\) matrix \\(A\\);
- the full matrix \\(C\\);
- a basis \\(N\\) of the resulting \\(K_0\\);
- the resulting compression \\(M\\);
- the matrix \\(A\_{21}\\), or enough information to calculate it;
- the value of \\(q\\).

The last item is also missing from II.3, although \\(q\\) determines the Grassmann fibre and hence the maximal minors being tested.

### **9.2 The certificates need to cover every chart**

For a good direction, one rational point of one fibre chart with gcd \\(1\\) is enough to establish feasibility.

For a bad direction, however, the certificate must cover the entire fibre. It is not enough to report a positive-degree gcd on just one chart. The report should state:

1. how many Grassmann charts cover the fibre;
2. the generic gcd on each chart;
3. the nonconstant common divisor on each chart;
4. the exact divisibility identities.

The full-rank specialization lemma in Section 3 then turns those function-field gcd computations into certificates for every point of the corresponding charts.

This is a manageable requirement because the fibre dimension is bounded by a function of \\(p\\), and in this example \\(p=2\\).

### **9.3 The example should distinguish two claims**

The report currently says that the example confirms feasibility is not constant on a repeated eigenspace. More precisely, the intended conclusion is:

\\[ \begin{array}{ll} \text{direction }[1:1]:& \text{there exists an admissible row space with a good pencil},\\\ \text{other listed directions}:& \text{every admissible row space has a bad pencil}. \end{array} \\]

The second statement is stronger than saying that a generic row space is bad. Your certificates should explicitly establish the stronger statement.

Once the complete data and all chart certificates are included, this will be a persuasive counterexample to any proposed reduction that tests only one arbitrary eigenvector per distinct eigenvalue.

## **10. Suggested revisions to Report 105**

I would make the following changes, in this order.

1\. **Resolve the rank-**\\(L_0\\)**&#x20;issue.** Either impose \\(\operatorname{rank}L_0=r_0\\) or replace \\(q\\) by the effective maximum row-space dimension \\(q\_{\mathrm{eff}}\\) in the normalization and fibre formulas.

2\. **Expand Lemma C.** Include the argument that extending \\(V\\) inside \\(U_v^\perp\\) preserves both the row-space inclusion and the constant pencil rank.

3\. **Add the full-rank leading-coefficient lemma.** This is what makes the positive-degree function-field gcd a certificate that the entire chart is bad.

4\. **Clarify the resultant test.** It is sufficient, not necessary, for the gcd of the full family to be \\(1\\).

5\. **Specify the domain of the chart algorithm.** Distinguish fixed-direction fibre charts from charts that also parameterize a repeated eigenspace.

6\. **Complete the algebraic-number implementation.** If the fixed-\\(p\\) theorem includes irrational eigenvalues, the gcd computation must be carried out over the corresponding number fields.

7\. **Publish the complete repeated-spectrum instance.** Include \\(A,C,N,q,A\_{21}\\), all chart gcds, and exact divisibility or coprimality certificates.

8\. **State the bit-complexity theorem only after the bounds are written down.** In particular, bound the multi-polynomial gcd computation, not merely one resultant.

## **11. Final verdict**

Substantial mathematical progress

Report 105 is significantly stronger than Report 103. Its main geometric correction—the incorporation of prescribed rows through \\(E\_\mu^0\\), followed by the relative Grassmann-bundle parameterization—is sound. The dimension formulas are correct, and the Paper II duality offers a promising way to connect the ambient and compressed formulations.

I would classify the current results as follows:

| Component                    | Assessment                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------ |
| Lemma A                      | Correct                                                                                          |
| Lemma B                      | Correct                                                                                          |
| Lemma C                      | Correct if \\(L_0\\) has full row rank; otherwise its target dimension must be changed           |
| Theorem \\(1'\\)             | Correct after resolving the row-rank issue and stating the bundle hypotheses precisely           |
| Chartwise gcd criterion      | Correct with the full-rank leading-coefficient lemma made explicit                               |
| Resultant test               | Correct as a sufficient test, not a necessary one                                                |
| Repeated-spectrum example    | Promising, but the data and complete chart certificates are missing                              |
| Paper II duality             | Correct direction correspondence; ambient lifting fibres need the more precise description above |
| Fixed-\\(p\\) bit complexity | Plausible, but not yet proved                                                                    |

### **The central research conclusion**

I think the most valuable result emerging from Report 105 is not simply the hyperplane parameterization. It is the combination of three ideas:

\\[ \boxed{ \text{prescribed-row-compatible directions} \\;\longrightarrow\\; \text{relative Grassmann fibres} \\;\longrightarrow\\; \text{exact chartwise pencil certificates}. } \\]

This gives a principled route from the original observer problem to finite algebraic computations. The geometrically simple subclass is particularly promising because each real eigenvalue contributes at most one projective direction, leaving only a bounded-dimensional Grassmann fibre when \\(p\\) is fixed.

The repeated-spectrum case is more complicated, but Report 105 has identified the right structural objects: the admissible eigenspaces \\(E\_\mu^0\\), the rank stratification of \\(A\_{21}|\_{E\_\mu^0}\\), and the common-root incidence of the maximal minors.

### **What I would do next**

I would not expand the repeated-eigenvalue classification immediately. First, settle the prescribed-row rank assumption and prove the full-rank specialization lemma in the manuscript. Then complete the fixed-\\(p\\) bit-complexity proof for geometrically simple eigenspaces, including irrational eigenvalues. This would turn the strongest algorithmic claim into a defensible theorem.

After that, I would use the fully specified repeated-spectrum example to motivate a separate investigation of the general repeated-eigenspace case.

**Bottom line:** Report 105 has a sound and potentially publishable mathematical core. The prescribed-row correction is successful, but the rank-\\(L_0\\) issue is a genuine point to settle, and the complexity claim still needs a formal bit-model proof. I would regard the report as a strong research-stage result, not yet a finished theorem package.