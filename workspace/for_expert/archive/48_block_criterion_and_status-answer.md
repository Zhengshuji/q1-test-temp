# Mathematical review of `48_block_criterion_and_status.md`

The new report is a significant improvement in the organization of the research. In particular, it moves beyond the previous Grassmannian and generic-gcd formulations and identifies a useful finite-dimensional operator that directly controls spectral failure.

My overall assessment is positive: Theorem A and the block criterion are mathematically sound under the stated assumptions, and the \\(q=\omega+1\\) analysis gives a particularly useful reduction. The report also correctly withdraws the erroneous rank-one construction from the previous round.

There are, however, several points that should be sharpened before the results are presented as a complete theory:

1. The componentwise dichotomy is correct, but its algorithmic consequence depends critically on computing the irreducible components and their function fields.
2. The block criterion needs a more explicit statement of the coordinate decomposition and the induced operator.
3. The discussion of \\(\omega=1\\) should distinguish a column vector from a row vector and make clear why the horizontal rank condition is appropriate there.
4. The \\(q=\omega+1\\) case can be stated more generally in terms of geometric eigenspaces, not merely the \\(\omega=2\\) determinant.
5. The claim that \\(k=\omega\\) is settled “with a polynomial algorithm” needs a complexity qualification. The earlier fixed-\\((q,\omega)\\) resultant argument does not, by itself, establish a uniform polynomial-time algorithm when the dimensions vary.
6. The remaining problem is now more precisely identifiable: it is the geometry of the reachable compatible fibres and the spectral behavior of their induced operators.

I will first verify the new mathematics, then discuss the qualifications and propose a concrete next-stage research plan.

# 1. The mathematical setting and the three problem formulations

The report fixes

\\[ K=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \qquad k=\dim K, \\]

and a basis matrix \\(N_K\\) of \\(K\\). It defines

\\[ H(R)=\mathcal L(R)N_K,\qquad H_A(R)=\mathcal L(R)AN_K. \\]

For a fixed rank \\(\omega\\), the admissible locus is

\\[ \mathcal X\_\omega = \left\\{ R: \rank H(R)=\omega,\quad \ker H(R)\subseteq\ker H_A(R) \right\\}. \\]

The spectral bad locus is

\\[ \mathcal B = \left\\{ R\in\mathcal X\_\omega: \exists\lambda\in\mathbb C,\  \rank(\lambda H(R)-H_A(R))<\omega \right\\}. \\]

The report uses the equivalent criterion

\\[ R\notin\mathcal B \iff \gcd\\{\text{all }\omega\text{-minors of } \lambda H(R)-H_A(R)\\} \in\mathbb C^\times. \tag{1.1} \\]

This is the correct starting point.

Indeed, since

\\[ \ker H\subseteq\ker H_A, \\]

the two maps \\(H,H_A:\mathbb C^k\to\mathbb C^q\\) induce a well-defined linear map

\\[ Z:W\longrightarrow\mathbb C^q, \qquad W=\operatorname{im}H, \\]

defined by

\\[ Z(Hx)=H_Ax. \tag{1.2} \\]

The reduced pencil is therefore

\\[ \lambda H-H_A=(\lambda I-Z)H, \tag{1.3} \\]

where \\(I\\) in this expression denotes the inclusion of \\(W\\) into \\(\mathbb C^q\\).

Because \\(H\\) has rank \\(\omega\\), it is surjective onto \\(W\\). Thus

\\[ \rank(\lambda H-H_A)<\omega \\]

if and only if

\\[ \ker(\lambda I-Z)\ne\\{0\\}. \\]

Consequently,

\\[ \boxed{ R\in\mathcal B \iff Z:W\to\mathbb C^q \text{ has a nonzero eigenvector in }W. } \tag{1.4} \\]

This is the fundamental observation behind the new block criterion.

The separation into DEC, OPT, and FIND is also now correctly formulated. In particular, the report explicitly avoids claiming monotonicity in \\(q\\). This is important: finite scanning gives

\\[ \mathrm{OPT}\ \leq\_{\mathrm{T}}\ \mathrm{DEC}, \\]

in the sense that an optimization algorithm can be obtained by testing the finitely many permitted orders. But binary search would require a separate monotonicity theorem.

The output-field and output-size distinction for FIND should also remain in the formal statement.&#x20;

48_block_criterion_and_status.md



# 2. Theorem A: the componentwise dichotomy is correct

The report's first theorem is:

> Let \\(X\\) be an irreducible locally closed subset contained in the rank-\\(\omega\\) admissible locus. Then either \\(X\subseteq\mathcal B\\), or \\(X\setminus\mathcal B\\) is a nonempty Zariski-open dense subset of \\(X\\). The two cases are distinguished by the gcd of the \\(\omega\\)-minors over \\(\mathbb C(X)\\).

I agree with this theorem.

## 2.1 Why the bad locus is closed

The relevant projective pencil is

\\[ P^h(R;\alpha,\beta) = \alpha H(R)-\beta H_A(R), \qquad [\alpha:\beta]\in\mathbb P^1. \\]

Consider the incidence set

\\[ \mathcal I = \left\\{ (R,[\alpha:\beta])\in X\times\mathbb P^1: \rank P^h(R;\alpha,\beta)<\omega \right\\}. \tag{2.1} \\]

It is closed because rank deficiency is expressed by the vanishing of all \\(\omega\\)-minors.

The projection

\\[ \pi:X\times\mathbb P^1\longrightarrow X \\]

is proper, since \\(\mathbb P^1\\) is projective. Hence the image

\\[ \pi(\mathcal I) \\]

is closed in \\(X\\).

We must check that this projective image is exactly the finite spectral bad locus, rather than containing additional points corresponding to \\(\lambda=\infty\\).

At the projective point \\([1:0]\\),

\\[ P^h(R;1,0)=H(R). \\]

But \\(\rank H(R)=\omega\\) throughout \\(X\\). Therefore the incidence set has no point over \\([1:0]\\).

Every point in the projected bad locus consequently has \\(\beta\ne0\\), and we may normalize \\(\beta=1\\). Writing \\(\lambda=\alpha/\beta\\), we obtain precisely

\\[ \mathcal B = \left\\{ R\in X: \exists\lambda\in\mathbb C,\ \rank(\lambda H(R)-H_A(R))<\omega \right\\}. \\]

Thus

\\[ \boxed{\mathcal B\text{ is closed in }X.} \tag{2.2} \\]

This is the correct projective argument. It also explains why it is essential to stratify by the constant rank of \\(H\\): the full-rank leading coefficient eliminates the spurious projective point at infinity.

## 2.2 Why irreducibility gives the dichotomy

Since \\(\mathcal B\\) is closed in \\(X\\), its complement is open.

If

\\[ \mathcal B=X, \\]

then every point is bad.

Otherwise,

\\[ X\setminus\mathcal B\ne\varnothing. \\]

Since \\(X\\) is irreducible, every nonempty open subset is dense. Therefore

\\[ \boxed{ X\subseteq\mathcal B \quad\text{or}\quad X\setminus\mathcal B \text{ is nonempty, open, and dense in }X. } \tag{2.3} \\]

This is a strong and useful result.

It says that on an irreducible admissible component, the spectral behavior cannot be divided into two unrelated dense regions. There is a generic behavior:

- either the entire component is bad;
- or a generic point is good.

There can still be exceptional bad points inside a generically good component, but those form a proper closed subset.

## 2.3 Why the function-field gcd is the correct test

Let

\\[ F=\mathbb C(X) \\]

be the function field of \\(X\\). The entries of \\(H\\) and \\(H_A\\), and hence the maximal minors of

\\[ P(\lambda)=\lambda H-H_A, \\]

are elements of \\(F[\lambda]\\).

The generic point of \\(X\\) is bad if and only if there exists a finite spectral value over an algebraic closure \\(\overline F\\) at which the generic pencil loses rank.

Equivalently, all \\(\omega\\)-minors have a common root in \\(\overline F\\).

Since \\(F\\) is a field, this is equivalent to

\\[ \gcd\_{F[\lambda]}\\{\omega\text{-minors of }P(\lambda)\\} \\]

being nonconstant.

Therefore

\\[ \boxed{ X\subseteq\mathcal B \iff \deg\_\lambda \gcd\_{F[\lambda]}\\{\omega\text{-minors}\\}>0. } \tag{2.4} \\]

The converse is worth emphasizing. If the gcd is constant, the generic point is good. Since the bad locus is closed, it cannot contain any nonempty open subset of \\(X\\). Thus the good points form a nonempty open dense subset.

The theorem is therefore not merely a qualitative genericity statement. It gives an exact algebraic invariant for the generic behavior of each irreducible component.

## 2.4 The limitation: Theorem A is not yet a complete algorithm

The report correctly identifies the remaining issue: the irreducible components of \\(\mathcal X\_\omega\\) must be described.

Theorem A gives the following conditional algorithm:

1. Compute the irreducible components \\(X_1,\ldots,X_s\\) of \\(\mathcal X\_\omega\\).
2. Compute the generic pencil on each component.
3. Compute the gcd of its maximal minors over \\(\mathbb C(X_i)\\).
4. Declare the component generically good if and only if that gcd is constant.
5. Decide complex feasibility by checking whether at least one component is generically good.

This is mathematically correct.

But the complexity of component decomposition and function-field arithmetic has not been settled. The theorem is therefore an exact structural reduction, not yet a polynomial-time algorithm.

That distinction should be preserved in any paper.

# 3. The block criterion: correct and potentially the most important new result

The block criterion is the most promising development in this report.

Let

\\[ W=\operatorname{im}H\subseteq\mathbb C^q, \qquad \dim W=\omega. \\]

The induced map

\\[ Z:W\to\mathbb C^q \\]

is defined by \\(Z(Hx)=H_Ax\\).

Choose a complementary subspace \\(W'\\) such that

\\[ \mathbb C^q=W\oplus W'. \\]

Then

\\[ \dim W'=q-\omega. \\]

Choose bases of \\(W\\) and \\(W'\\), and write the matrix of \\(Z\\) in block form:

\\[ Z= \begin{pmatrix} A\\\ B \end{pmatrix}, \tag{3.1} \\]

where

\\[ A\in\mathbb C^{\omega\times\omega}, \qquad B\in\mathbb C^{(q-\omega)\times\omega}. \\]

Strictly speaking, \\(A\\) is the \\(W\\)-component of \\(Z\\), while \\(B\\) is its \\(W'\\)-component. This is a coordinate representation of the map \\(Z\\), not an arbitrary partition of the original matrix \\(H_A\\).

## 3.1 Proof of the block criterion

A spectral rank drop occurs if and only if there exists \\(0\ne w\in W\\) such that

\\[ Z(w)=\lambda w \\]

for some \\(\lambda\in\mathbb C\\).

Represent \\(w\\) by its coordinate vector \\(y\in\mathbb C^\omega\\). Then

\\[ Z(w)= \begin{pmatrix} Ay\\\ By \end{pmatrix}, \qquad \lambda w= \begin{pmatrix} \lambda y\\\ 0 \end{pmatrix}. \\]

Thus the eigenvector equation is equivalent to

\\[ Ay=\lambda y, \qquad By=0. \tag{3.2} \\]

Equivalently,

\\[ 0\ne y\in\ker B, \qquad Ay\in\operatorname{span}\\{y\\}. \\]

Therefore

\\[ \boxed{ \text{bad} \iff \exists\\,0\ne y\in\ker B \text{ such that }Ay\in\mathbb Cy. } \tag{3.3} \\]

The report's theorem is correct.

The advantage is substantial: the original spectral question involved a parameter \\(\lambda\\), but the block criterion eliminates it. We now need only determine whether the hyperplane or subspace \\(\ker B\\) intersects an eigenspace of \\(A\\).

## 3.2 Coordinate invariance

The matrices \\(A\\) and \\(B\\) depend on the choice of complement \\(W'\\) and on the chosen bases. However, the criterion itself does not.

The intrinsic statement is:

\\[ \boxed{ \text{bad} \iff \exists\\,0\ne w\in W: Z(w)\in\mathbb Cw. } \\]

The block criterion is simply a convenient coordinate representation.

This should be stated explicitly in the paper, so that readers do not mistake \\(A,B\\) for canonical matrices independent of the complement.

I would also consider renaming the induced map \\(Z\\) as \\(\Phi\\), because the project has already used \\(Z_1,Z_2\\) for the compatibility-kernel blocks. The notation

\\[ \Phi:W\to\mathbb C^q, \qquad \Phi= \begin{pmatrix}A\\\B\end{pmatrix} \\]

would reduce ambiguity.

# 4. Consequences of the block criterion

The three consequences in the report are mostly correct. They can be stated more sharply.

## 4.1 The square case \\(q=\omega\\)

If \\(q=\omega\\), then

\\[ W=\mathbb C^q, \qquad W'=\\{0\\}. \\]

Therefore \\(B\\) has zero rows, so

\\[ \ker B=\mathbb C^\omega. \\]

The badness condition becomes

\\[ \exists\\,0\ne y\in\mathbb C^\omega: Ay=\lambda y. \\]

Every complex square matrix has an eigenvalue and a nonzero eigenvector. Hence every admissible point is bad.

Thus

\\[ \boxed{q=\omega\implies\text{spectral infeasibility}.} \tag{4.1} \\]

This is a clean alternative proof of the square-pencil obstruction.

The use of \\(\mathbb C\\) matters: every complex square matrix has an eigenvalue. Over \\(\mathbb R\\), the corresponding statement about real eigenvectors would be false.

## 4.2 The regime \\(q\ge2\omega\\)

Here

\\[ B\in\mathbb C^{(q-\omega)\times\omega}, \qquad q-\omega\ge\omega. \\]

If

\\[ \ker B=\\{0\\}, \\]

then the badness condition is impossible. Therefore

\\[ \boxed{ \ker B=\\{0\\} \implies \text{good}. } \tag{4.2} \\]

This is correct.

There is, however, a subtle geometric issue in the report's explanation.

The condition

\\[ \ker B=\\{0\\} \\]

is open in the space of \\(B\\)-matrices: it is the nonvanishing of at least one \\(\omega\times\omega\\) minor.

But the admissible locus is not globally closed in the original parameter space, because the condition

\\[ \rank H=\omega \\]

is locally closed.

More precisely:

- \\(\rank H\le\omega\\) is closed;
- \\(\rank H\ge\omega\\) is open;
- their intersection \\(\rank H=\omega\\) is locally closed;
- on this fixed-rank locus, the condition \\(\ker H\subseteq\ker H_A\\) is closed relative to the rank stratum.

Indeed, on \\(\rank H=\omega\\),

\\[ \ker H\subseteq\ker H_A \iff \rank\begin{bmatrix}H\\\H_A\end{bmatrix}=\omega. \\]

Thus the question is not whether an open condition intersects a globally closed admissible set. The relevant question is whether the reachable admissible family contains a point with \\(B\\) of full column rank.

That is the actual remaining synthesis problem.

I would formulate it as:

> For which fixed data \\((A,C,L_0,q,\omega)\\) does the reachable family of induced maps \\(\Phi:W\to\mathbb C^q\\) contain a member whose projection onto \\(W'\\) is injective?

If such a point exists, the corresponding design is automatically good.

This is a useful sufficient condition, although it is not necessary when \\(q<2\omega\\).

## 4.3 The case \\(\omega=1\\)

For \\(\omega=1\\), \\(A\\) is a scalar and \\(B\\) has size

\\[ (q-1)\times1. \\]

The badness condition is

\\[ \exists\\,0\ne y\in\ker B. \\]

Since the domain of \\(B\\) is one-dimensional, this is equivalent to

\\[ B=0. \\]

Thus

\\[ \boxed{ \omega=1: \quad \text{good}\iff B\ne0. } \tag{4.3} \\]

Equivalently,

\\[ \text{good} \iff \operatorname{rank}[H\ H_A]=2. \tag{4.4} \\]

Here the horizontal concatenation is appropriate: both \\(H\\) and \\(H_A\\) have one column, and the condition says that their column vectors are linearly independent.

This is not the vertical rank condition in (5a). The two conditions have different roles:

\\[ (5a)\quad \rank\begin{bmatrix}H\\\H_A\end{bmatrix} =\rank H, \\]

whereas the \\(\omega=1\\) spectral criterion is

\\[ \rank[H\ H_A]=2. \\]

The report's use of the horizontal rank condition here is correct. It should simply explain why this condition is spectral rather than admissibility-related.

# 5. The \\(q=\omega+1\\) case: a particularly useful classification

This section is correct and deserves further development.

When

\\[ q=\omega+1, \\]

the matrix \\(B\\) is a single row:

\\[ B\in\mathbb C^{1\times\omega}. \\]

If \\(B\ne0\\), then

\\[ \dim\ker B=\omega-1. \\]

Thus \\(\ker B\\) is a hyperplane in \\(W\\).

The badness criterion becomes

\\[ \text{bad} \iff \ker B \text{ contains a nonzero eigenvector of }A. \tag{5.1} \\]

## 5.1 General eigenspace formulation

For each eigenvalue \\(\mu\\) of \\(A\\), let

\\[ E\_\mu=\ker(A-\mu I) \\]

be its eigenspace.

Then

\\[ \boxed{ \text{bad} \iff \exists\mu\in\sigma(A): E\_\mu\cap\ker B\ne\\{0\\}. } \tag{5.2} \\]

Since \\(B\\) is a linear functional,

\\[ E\_\mu\cap\ker B = \ker(B|\_{E\_\mu}). \\]

Therefore

\\[ \boxed{ \text{good} \iff B|\_{E\_\mu}\text{ is injective for every }\mu\in\sigma(A). } \tag{5.3} \\]

But a linear functional on a vector space of dimension at least two cannot be injective. Hence a necessary condition for goodness is

\\[ \dim E\_\mu=1 \quad\text{for every eigenvalue }\mu. \tag{5.4} \\]

If every eigenspace is one-dimensional, then goodness is equivalent to \\(B\\) being nonzero on every eigenline.

This yields a useful general theorem.

Theorem: block criterion for \\(q=\omega+1\\)

Let \\(A\in\mathbb C^{\omega\times\omega}\\) and \\(B\in\mathbb C^{1\times\omega}\\). Then the block pencil associated with \\(\binom AB\\) is good if and only if:

1. every eigenspace of \\(A\\) is one-dimensional; and
2. \\(Bv\ne0\\) for every nonzero eigenvector \\(v\\) of \\(A\\).

Equivalently, \\(A\\) has geometric multiplicity one at every eigenvalue, and its eigenlines are all transverse to \\(\ker B\\).

Notice that this condition concerns geometric multiplicity, not algebraic multiplicity. A matrix can have a repeated eigenvalue but a one-dimensional eigenspace. Such a matrix is not automatically excluded.

## 5.2 The special case \\(\omega=2,\ q=3\\)

If \\(\omega=2\\) and \\(B\ne0\\), then \\(\ker B\\) is a line:

\\[ \ker B=\operatorname{span}\\{w\\}. \\]

The pencil is bad if and only if \\(w\\) is an eigenvector of \\(A\\), which is equivalent to

\\[ Aw\in\operatorname{span}\\{w\\}. \\]

Therefore

\\[ \boxed{ \text{good} \iff \det[w,\ Aw]\ne0. } \tag{5.5} \\]

This is correct.

It is worth emphasizing that the determinant is independent of the choice of nonzero representative of the line. If \\(w\\) is replaced by \\(cw\\), then

\\[ \det[cw,A(cw)] = c^2\det[w,Aw]. \\]

Its vanishing is therefore a well-defined projective condition on \\([w]\in\mathbb P^1\\).

The special case \\(A=\mu I\\) is necessarily bad because

\\[ Aw=\mu w \\]

for every \\(w\\).

## 5.3 A stronger conclusion: the exceptional bad directions are finite

There is another useful observation in the \\(q=3,\omega=2\\) case.

For a fixed \\(2\times2\\) matrix \\(A\\), the bad directions are exactly its eigenlines.

There are two possibilities:

- If \\(A\\) is scalar, every line is an eigenline, so every nonzero \\(B\\) is bad.
- If \\(A\\) is nonscalar, it has at most two eigenlines over \\(\mathbb C\\), so only finitely many projective directions \\([w]\in\mathbb P^1\\) are bad.

Thus, for a fixed nonscalar \\(A\\), a generic nonzero row \\(B\\) gives a good pencil.

This is potentially important for the synthesis problem. If the reachable family allows \\(B\\) to vary freely enough while keeping \\(A\\) fixed, then goodness should be generic.

However, the shared dependence of \\(A\\) and \\(B\\) on \\(R\\) may prevent that variation. That is exactly where the observer-specific geometry enters.

# 6. The general obstruction instance is correctly strengthened

The report considers

\\[ C=e_1^{\mathsf T}, \qquad L_0=e_3^{\mathsf T}, \\]

and

\\[ A= \begin{pmatrix} 0&0&0&1\\\ 0&0&1&0\\\ 0&1&0&0\\\ 0&0&0&0 \end{pmatrix}. \\]

We have

\\[ Ae_2=e_3,\qquad Ae_3=e_2. \\]

Therefore

\\[ v\_+=e_2+e_3,\qquad v\_-=e_2-e_3 \\]

satisfy

\\[ Av\_+=v\_+,\qquad Av\_-=-v\_-. \\]

Furthermore,

\\[ Cv\_+=Cv\_-=0. \\]

Since \\(CA=e_4^{\mathsf T}\\),

\\[ CAv\_+=CAv\_-=0. \\]

Thus

\\[ v\_\pm\in\ker C\cap\ker CA. \\]

For any augmentation \\(\mathcal L\\), at the corresponding eigenvalue \\(\lambda\\),

\\[ (\lambda\mathcal L-\mathcal LA)v = \mathcal L(\lambda I-A)v =0. \\]

Together with

\\[ CAv=Cv=0, \\]

this gives

\\[ \begin{bmatrix} \lambda\mathcal L-\mathcal LA\\\ CA\\\ C \end{bmatrix}v=0. \tag{6.1} \\]

If \\(q=n=4\\) and \\(\mathcal L\\) has full row rank, then \\(\mathcal L\\) is invertible, so

\\[ \rank\begin{bmatrix}\mathcal L\\\CA\\\C\end{bmatrix}=4. \\]

But the matrix in (6.1) has a nonzero null vector, so its rank is at most three. Hence (5b) fails.

This proves infeasibility at \\(q=4\\), independently of the particular choice of \\(R\\).

Combined with the report's structural arguments for \\(q\le3\\), it gives

\\[ \boxed{ \text{No feasible augmentation exists at any permitted order.} } \\]

This is a complete obstruction theorem for that example.

## 6.1 A general version

The useful general statement is:

Proposition. Suppose there exists \\(0\ne v\in\mathbb C^n\\) and \\(\lambda\in\mathbb C\\) such that

\\[ Av=\lambda v,\qquad Cv=0,\qquad CAv=0. \\]

Then every invertible augmentation \\(\mathcal L\in\mathbb C^{n\times n}\\) violates (5b).

The proof is exactly the argument above.

This proposition is a valid reusable obstruction, but it does not establish that every noninvertible augmentation fails. In the non-square case, the right-hand rank

\\[ \rank\begin{bmatrix}\mathcal L\\\CA\\\C\end{bmatrix} \\]

may also be deficient. The obstruction then needs additional information about the rank of the right-hand side.

I recommend presenting the proposition in this precise form rather than implying it rules out all possible augmentation orders by itself.

# 7. The correction in Part III is appropriate and should remain explicit

The report correctly withdraws the earlier claimed rank-one feasible stratum.

The essential issue was the distinction between

\\[ \rank\begin{bmatrix}H\\\H_A\end{bmatrix} \\]

and

\\[ \rank[H\ H_A]. \\]

The first is the vertical rank condition inherited from (5a). The second is a horizontal concatenation and measures something different.

For the previously discussed instance, the fixed top rows satisfy

\\[ E=\operatorname{span}\\{(0,1,0)\\}, \qquad F_0=\operatorname{span}\\{(1,0,0)\\}. \\]

Every admissible row space \\(S\\) must contain \\(E+F_0\\). Therefore

\\[ \dim S\ge2. \\]

Consequently, the \\(\omega=1\\) stratum is empty.

The correction is not merely a programming fix. It is a useful methodological lesson: every constructed \\(R\\) should be verified against the original vertical rank condition, not just against a reduced or horizontal rank calculation.

The exact Grassmannian criterion provides an independent check and should remain part of the verification protocol.

# 8. The status of the main problem: what is genuinely settled?

The report's final status is broadly correct, but I would refine the terminology and the complexity claims.

## 8.1 Fixed-\\(R\\) spectral verification

This is settled.

Given a particular admissible \\(R\\), one computes the \\(\omega\\)-minors of

\\[ \lambda H-H_A \\]

and their gcd. The condition is exact.

The number of minors can be large, but this is a verification problem, not an existence problem.

## 8.2 The cases \\(\omega=0\\) and \\(\omega=1\\)

These are structurally simple.

For \\(\omega=0\\), the spectral condition is automatic once the admissibility requirements are met, because the relevant rank is zero.

For \\(\omega=1\\), the block criterion reduces spectral feasibility to

\\[ B\ne0, \\]

or equivalently

\\[ \rank[H\ H_A]=2. \\]

The remaining task is then to determine whether the reachable admissible family contains a point satisfying this rank condition.

## 8.3 The case \\(q=\omega\\)

This is settled: every admissible point is bad over \\(\mathbb C\\).

## 8.4 The case \\(k=\omega\\)

The structural simplification is correct.

When \\(k=\omega\\),

\\[ \rank H=k, \\]

so \\(H\\) has trivial kernel. Hence

\\[ \ker H\subseteq\ker H_A \\]

holds automatically.

Thus (5a) imposes no additional compatibility condition on the restricted maps \\(H,H_A\\), and the reachable pair family is affine-linear in \\(R\\).

The earlier generic-pencil theorem then applies: if the rank-full affine domain is nonempty, a good member exists if and only if the generic pencil over the parameter function field is good.

This is a significant result.

### Important qualification: the polynomial-time claim

The report says that \\(k=\omega\\) is settled “with a polynomial algorithm.”

I would qualify this claim.

The earlier fixed-\\((q,\omega)\\) resultant method establishes polynomial complexity when \\(q,\omega\\) are fixed, because the number of maximal minors and their degrees are then bounded independently of the input dimension.

But for variable \\(q,\omega\\), the number of maximal minors is

\\[ \binom q\omega, \\]

which can be exponential in the dimensions.

There may be more efficient ways to compute the determinantal divisor without explicitly expanding every maximal minor, for example by exploiting polynomial-matrix normal forms over the rational function field. But that requires a separate complexity analysis, especially when the coefficients themselves are rational functions in many design parameters.

Therefore I recommend replacing the current statement with:

> The case \\(k=\omega\\) admits an exact generic-pencil reduction. For fixed \\(q,\omega\\), the resulting test has a polynomial-time implementation using bounded-degree algebraic computations. A uniform polynomial-time bound for variable \\(q,\omega\\) requires further analysis.

This is more precise and avoids claiming a complexity result that has not yet been fully established.

# 9. The main open problem has now become much more specific

The report identifies two central open directions:

1. describe the irreducible components of the admissible locus when \\(k>\omega\\);
2. determine whether the reachable family can produce a good block pair in the \\(q=\omega+1\\) regime.

I agree with this prioritization, but I would organize them under one common framework.

## 9.1 The compatible fibre over a Grassmannian point

Recall the fixed-row setup.

Let

\\[ U_0=L_0N_K,\qquad V_0=L_0AN_K, \\]

and write

\\[ E=\operatorname{row}(U_0), \qquad F_0=\operatorname{row}(V_0). \\]

Let

\\[ T:K\oplus K\longrightarrow\mathbb C^n, \qquad T(v,w)=v+Aw, \\]

and let \\(Z_1,Z_2\\) describe a basis of \\(\ker T\\).

For a fixed \\(S\in\operatorname{Gr}(\omega,k)\\), the compatible row pairs are

\\[ \mathcal C_S = \left\\{ (x,y)\in S\times S: xZ_1+yZ_2=0 \right\\}. \tag{9.1} \\]

The first-coordinate projection is

\\[ X_S = \left\\{ x\in S: \exists y\in S,\ xZ_1+yZ_2=0 \right\\}. \\]

The Grassmannian criterion says that a rank-\\(\omega\\) admissible design exists over \\(S\\) if and only if

\\[ E+F_0\subseteq S, \qquad E+X_S=S, \qquad \omega-\dim E\le m. \tag{9.2} \\]

This describes the base points \\(S\\) over which the admissible fibre is nonempty.

But for spectral feasibility, we need more than the existence of some compatible row pairs. We need to understand the family of all possible pairs \\((B_1,B_2)\\) and the resulting block matrices \\(A,B\\).

That suggests studying the map

\\[ \Psi_S:\mathfrak F_S \longrightarrow \\{(A,B)\\}, \tag{9.3} \\]

where \\(\mathfrak F_S\\) is the set of compatible bottom-row choices that span the required quotient \\(S/E\\).

The central question becomes:

\\[ \boxed{ \text{Does }\Psi_S(\mathfrak F_S) \text{ contain a block pair }(A,B) \text{ satisfying the spectral criterion?} } \tag{9.4} \\]

This formulation combines the Grassmannian and block approaches rather than treating them as separate stages.

## 9.2 Why this is better than searching for a universal identity

The previous examples had a rigid relation

\\[ H_A=-HZ_1. \\]

That relation forced the spectrum and made the entire stratum bad.

But the block criterion shows that a general stratum need not have such a fixed relation. It may instead contain a family of induced maps

\\[ \Phi_S= \begin{pmatrix} A\\\B \end{pmatrix} \\]

whose spectral behavior changes as the compatible rows vary.

The appropriate general question is not whether \\(H_A=-HZ\\) holds for a fixed matrix \\(Z\\), but whether the image of the reachable family intersects the good-block locus.

For \\(q=\omega+1\\), this good-block locus is especially simple:

\\[ \mathcal G = \left\\{ (A,B): B|\_{E\_\mu(A)}\text{ is injective for every eigenvalue }\mu \right\\}. \\]

For \\(\omega=2\\), it is described by the single determinant

\\[ \det[w,Aw]\ne0, \qquad \ker B=\mathbb Cw. \\]

This is the natural algebraic target for the next round.

# 10. A concrete next theorem: the \\(q=\omega+1\\) reachable-block criterion

I recommend developing the following theorem.

Let \\(\mathscr R\_\omega\\) denote the family of all induced block pairs \\((A,B)\\) obtainable from admissible augmentations at fixed \\(q=\omega+1\\) and fixed rank \\(\omega\\).

Then:

\\[ \boxed{ \text{A feasible augmentation exists} \iff \mathscr R\_\omega\cap\mathcal G\ne\varnothing, } \tag{10.1} \\]

where

\\[ \mathcal G = \left\\{ (A,B): \forall\mu\in\sigma(A),\ B|\_{\ker(A-\mu I)} \text{ is injective} \right\\}. \tag{10.2} \\]

This is essentially a reformulation of the block criterion, but it provides a much clearer research target.

The next step is to derive an explicit algebraic description of \\(\mathcal G\\).

## 10.1 An alternative polynomial formulation

For \\(B\in\mathbb C^{1\times\omega}\\), the badness condition is

\\[ \exists y\ne0: By=0,\quad Ay=\lambda y. \\]

This can be written as

\\[ \operatorname{rank} \begin{pmatrix} A-\lambda I\\\ B \end{pmatrix} <\omega \\]

for some \\(\lambda\in\mathbb C\\).

Equivalently, all \\(\omega\times\omega\\) minors of this \\((\omega+1)\times\omega\\) matrix vanish simultaneously for some \\(\lambda\\).

Thus the good-block condition is again a univariate gcd condition, but now the special structure of \\(B\\) may permit a simpler description.

When \\(\omega=2\\), it reduces to the determinant criterion.

When \\(\omega\\) is general, the eigenspace formulation may be more useful than direct expansion of all minors.

## 10.2 The simple-spectrum case

Suppose \\(A\\) has \\(\omega\\) distinct eigenvalues. Let

\\[ v_1,\ldots,v\_\omega \\]

be corresponding eigenvectors.

Then

\\[ \boxed{ \text{good} \iff Bv_i\ne0 \quad\text{for every }i. } \tag{10.3} \\]

For a fixed \\(A\\) with simple spectrum, the bad \\(B\\)'s form the union of the \\(\omega\\) hyperplanes

\\[ \\{B:Bv_i=0\\}. \\]

Hence the good set is a nonempty Zariski-open subset of the space of row vectors \\(B\\).

This is a strong indication that the \\(q=\omega+1\\) problem should be tractable whenever the reachable family allows sufficiently independent variation in \\(B\\).

The difficult part is proving that the observer-induced family actually has this freedom.

## 10.3 Repeated eigenspaces

If \\(A\\) has an eigenspace of dimension at least two, no row \\(B\\) can be injective on that eigenspace. Hence the whole block pair is bad.

Therefore a necessary condition for any good block pair in this regime is

\\[ \dim\ker(A-\mu I)=1 \quad\text{for every }\mu\in\sigma(A). \tag{10.4} \\]

This is a useful structural obstruction that can be checked before any search over \\(B\\).

It also suggests a natural two-stage algorithm for a fixed reachable family:

1. determine whether a reachable \\(A\\) has all eigenspaces one-dimensional;
2. determine whether a compatible reachable \\(B\\) is nonzero on every eigenline.

The second step must preserve the shared dependence of \\(A,B\\) on \\(R\\).

# 11. Recommended computational experiments

The report is right to treat sampling only as a witness-finder. I would now design experiments around the new block criterion rather than continue random sampling in \\(R\\)-space.

## Experiment A: verify the block criterion independently

For each constructed admissible \\(R\\):

1. compute \\(H,H_A\\) exactly;
2. compute \\(W=\operatorname{im}H\\);
3. choose a complement \\(W'\\);
4. construct \\(A,B\\);
5. compute the gcd of the maximal minors of \\(\lambda H-H_A\\);
6. independently test whether \\(A\\) has an eigenvector in \\(\ker B\\).

The two tests must agree.

For rational matrices, eigenvalues may be algebraic, so the final check should use exact polynomial arithmetic rather than floating-point eigenvectors.

A convenient exact test is

\\[ \gcd\\{\text{maximal minors of } \begin{pmatrix} A-\lambda I\\\B \end{pmatrix}\\}=1. \\]

This provides an independent verification of the block theorem.

## Experiment B: search for a same-\\(S\\), different-spectral-behavior example

This is the most informative next experiment.

Fix a Grassmannian point \\(S\\) for which the compatible fibre \\(\mathfrak F_S\\) has positive dimension.

Construct two compatible choices

\\[ (B_1^{(1)},B_2^{(1)}), \qquad (B_1^{(2)},B_2^{(2)}) \\]

that give the same \\(S\\), but different induced block pairs.

Try to obtain:

- one good pair;
- one bad pair.

If successful, this would decisively show that spectral behavior is not determined by the Grassmannian point alone.

It would also demonstrate why the fibre geometry must be studied, not just the set of admissible \\(S\\).

If no such example is found in small dimensions, that is not proof of rigidity, but it may suggest a stronger structural theorem worth investigating.

## Experiment C: investigate the \\(q=\omega+1,\omega=2\\) case

For each admissible \\(S\\), calculate the reachable line

\\[ \ker B=\mathbb Cw. \\]

Then test

\\[ \det[w,Aw]. \\]

This should be the primary exact test for the \\(3\times2\\) reduced pencil.

The important question is whether the compatible family can vary \\(w\\) away from the eigenlines of \\(A\\).

In particular, distinguish:

1. \\(A\\) is fixed and \\(w\\) varies;
2. \\(w\\) is fixed and \\(A\\) varies;
3. \\(A,w\\) vary together under a shared parameter;
4. the fibre forces \\(w\\) to be an eigenvector identically.

These four situations have very different implications for feasibility.

## Experiment D: search for nontrivial bad components without a fixed matrix identity

This is the most important test of the new theory.

Construct an admissible irreducible family \\(X\\) and compute the generic gcd over \\(\mathbb C(X)\\).

Try to find a family for which

\\[ \deg\gcd>0 \\]

but for which there is no simple constant matrix \\(Z_0\\) satisfying

\\[ H_A=-HZ_0 \\]

throughout the family.

Such an example would show that the componentwise generic-gcd theorem genuinely extends beyond the scaling and fixed-identity mechanisms found so far.

# 12. Revised research plan

I recommend the following order.

Phase 1 — Formalize the block theorem

Ready to write

- State the induced map \\(\Phi:W\to\mathbb C^q\\).
- Prove the coordinate-independent badness criterion.
- State the block form relative to a complement.
- Derive the \\(q=\omega\\), \\(q\ge2\omega\\), and \\(\omega=1\\) consequences.
- Include the eigenspace theorem for \\(q=\omega+1\\).

Phase 2 — Complete the \\(q=\omega+1,\omega=2\\) classification

Best next mathematical target

- Parameterize the reachable \\(\ker B\\) directions.
- Derive the determinant \\(\det[w,Aw]\\) in the original Grassmannian variables.
- Determine when this determinant is identically zero.
- Determine when it is nonzero at some reachable point.

Phase 3 — Study compatible fibres

- Fix \\(S\in\operatorname{Gr}(\omega,k)\\).
- Determine the affine structure and dimension of \\(\mathfrak F_S\\).
- Determine the induced map from \\(\mathfrak F_S\\) to block pairs \\((A,B)\\).
- Identify when \\(A\\) and \\(B\\) can vary independently.

Phase 4 — Establish componentwise algorithms

- Describe irreducible components of the admissible locus.
- Compute generic gcds over their function fields.
- Separate complex feasibility from real feasibility.
- Establish complexity bounds under explicit dimension restrictions.

Phase 5 — Reassess hardness

- If the compatible fibres are structurally restricted, pursue a classification or algorithm.
- If they can realize sufficiently general algebraic families of block pairs, investigate hardness.
- Any reduction must preserve the common \\(R\\)-dependence of the two restricted maps.

I would not prioritize a general hardness reduction yet. The block criterion has revealed a potentially much more tractable structure, particularly when \\(q-\omega\\) is small.

# 13. Final assessment of the report

| Result                                | Assessment          | Qualification                                                  |
| ------------------------------------- | ------------------- | -------------------------------------------------------------- |
| DEC / OPT / FIND separation           | Correct             | Keep binary search excluded until monotonicity is proved       |
| Theorem A                             | Correct             | Component decomposition remains the algorithmic bottleneck     |
| Function-field gcd test               | Correct             | Must be computed over the actual component function field      |
| Block criterion                       | Correct             | Define the induced map and complement carefully                |
| \\(q=\omega\\) obstruction            | Correct             | Uses algebraic closedness of \\(\mathbb C\\)                   |
| \\(q\ge2\omega\\), injective \\(B\\)  | Correct             | Sufficient, not necessary                                      |
| \\(\omega=1\\) criterion              | Correct             | Clarify horizontal versus vertical rank                        |
| \\(q=\omega+1\\) eigenspace criterion | Correct             | Can be generalized as in Section 5                             |
| \\(q=3,\omega=2\\) determinant        | Correct             | Projectively well-defined                                      |
| Complete obstruction example          | Correct             | The all-orders conclusion uses the separate \\(q\le3\\) proofs |
| Withdrawal of rank-one construction   | Correct             | Should remain explicitly documented                            |
| \\(k=\omega\\) polynomial algorithm   | Needs qualification | Fixed dimensions versus variable dimensions                    |

## Final recommendation

The report represents a real advance. The project now has two complementary structural tools:

- the Grassmannian criterion, which describes where admissible designs can exist;
- the block criterion, which describes exactly when an admissible design is spectrally bad.

The first controls the geometry of the reachable row spaces. The second controls the spectrum of the induced map on those row spaces.

The most promising next step is to combine them.

In particular, I recommend making the next deliverable a complete theorem for

\\[ \boxed{q=\omega+1,\qquad \omega=2.} \\]

In this case, the spectral condition is the single projective determinant

\\[ \boxed{\det[w,Aw]\ne0.} \\]

The remaining task is to express the reachable pair \\((A,w)\\) in terms of the compatible Grassmannian fibre and determine whether this determinant can be nonzero.

This is a sharply defined problem. It is small enough to permit a complete classification, but rich enough to reveal whether the shared \\(R\\)-dependence creates genuine algebraic obstructions.

If that case yields a tractable theorem, it provides a concrete foundation for the general \\(q=\omega+1\\) problem. If it yields a counterexample to the suspected rigidity, it provides a precise starting point for a more general componentwise analysis.

My conclusion is that the research should now move from general structural reduction to an explicit reachable-block classification. The main mathematical framework is sufficiently developed to support that transition.