# Mathematical and complexity audit of the two algorithmic routes

My overall assessment is positive: both algorithmic skeletons are mathematically viable, and the fixed-\\(\kappa\_{\rm obs}\\) route appears capable of yielding a genuine FPT theorem. The fixed-\\(q\\) route also appears correct, but I recommend simplifying its factorization before writing the proof.

There are several refinements worth making:

1. In the fixed-\\(q\\) construction, the matrix \\(F\\) is unnecessarily large and nonunique. Replace it by \\(G=FX\\). This reduces the number of variables and makes the linear system simpler.
2. The rank-consistency formula is correct, including rectangular and rank-deficient cases.
3. The pivot enumeration does not spoil polynomial time for fixed \\(q\\). The important detail is to process each pivot chart separately.
4. The FPT Gram–Cauchy–Binet certificate is correct with the stated shifted-index formula. Its coefficient computation genuinely avoids dependence exponential in \\(q\\).
5. The parameter-zero case \\(r=0\\) must be handled separately in the FPT theorem. Otherwise, \\(\kappa\_{\rm obs}=0\\) while the spectral pencil can still have arbitrarily large dimensions.
6. Fernando's 2026 characterization is important related work, but it is not itself a complexity theorem for q1.

I would develop both algorithmic results, with the fixed-\\(\kappa\_{\rm obs}\\) FPT theorem as the principal result and fixed-\\(q\\) polynomial time as a complementary theorem.

# Part I. Fixed \\(q\\): audit and simplification

## 1. Rank factorization and pivot normalization

The factorization in II.1 is correct.

Fix a feasible candidate of rank \\(\omega>0\\). There is a set of columns \\(J\subseteq[k]\\), \\(|J|=\omega\\), such that

\\[ X=H\_{:,J} \\]

has full column rank. Define

\\[ B=X^\dagger H, \\]

where \\(X^\dagger\\) is any left inverse of \\(X\\). Then

\\[ H=XB,\qquad B\_{:,J}=I\_\omega. \\]

Conversely, if \\(X\\) has full column rank and \\(B\_{:,J}=I\_\omega\\), then

\\[ \operatorname{rank}(XB)=\omega. \\]

The pivot normalization is particularly useful because it avoids a separate rank constraint on \\(B\\). It also makes the rank factorization valid over the real numbers without introducing rationality assumptions about the unknown solution.

There are only

\\[ \binom{k}{\omega}\le k^\omega\le k^q \\]

possible pivot sets. For fixed \\(q\\), this is polynomial in the input dimension.

No hidden degenerate-\\(B\\) problem exists: the identity block \\(B\_{:,J}=I\_\omega\\) guarantees full row rank.

## 2. Eliminate the nonunique matrix \\(F\\)

This is the first improvement I would make to the report.

The report introduces \\(F\in\mathbb R^{q\times q}\\) satisfying

\\[ H_A=FH. \\]

Since \\(H=XB\\), this gives

\\[ H_A=FXB. \\]

Define instead

\\[ \boxed{G:=FX\in\mathbb R^{q\times\omega}.} \\]

Then

\\[ \boxed{H_A=GB.} \tag{1} \\]

The key fact is that \\(G\\) can be treated as an unconstrained existential matrix. There is no need to quantify over \\(F\\).

To prove this equivalence:

- If (5a) holds, there exists \\(F\\) with \\(H_A=FH\\). Setting \\(G=FX\\) gives (1).
- Conversely, suppose (1) holds. Since \\(X\\) has full column rank, it has a left inverse \\(X_L\\) satisfying \\(X_LX=I\_\omega\\). Set\
  \\[\
  F=GX_L.\
  \\]\
  Then \\(FX=G\\), and\
  \\[\
  FH=FXB=GB=H_A.\
  \\]\
  Thus (5a) holds.

So we can replace the pair \\((F,X)\\) with \\((G,X)\\) without changing the feasible set.

This also resolves the nonuniqueness of \\(F\\) completely. Different matrices \\(F\\) may induce the same \\(G=FX\\), but the pencil only depends on \\(FX\\):

\\[ \lambda H-H_A=(\lambda X-G)B. \\]

The new variable count is

\\[ 2q\omega \\]

instead of \\(q^2+q\omega\\). Both are \\(O(q^2)\\), but the new formulation is cleaner and its equations have lower degree.

## 3. The parametric linear system remains exact

Choose a rational matrix \\(D\\) such that

\\[ \ker D=\mathcal T,\qquad \mathcal T=\operatorname{row}[N\ AN]. \\]

Write the fixed row pairs as

\\[ h_i^0=(L_0N)\_i,\qquad g_i^0=(L_0AN)\_i. \\]

For fixed rows \\(i\le r_0\\), the requirements are

\\[ X\_{i,:}B=h_i^0,\qquad G\_{i,:}B=g_i^0. \tag{2} \\]

For free rows \\(i>r_0\\), the requirement is

\\[ \boxed{ D \begin{bmatrix} (X\_{i,:}B)^{\mathsf T}\\\ (G\_{i,:}B)^{\mathsf T} \end{bmatrix}=0. } \tag{3} \\]

These conditions are necessary and sufficient:

- The fixed rows must have their prescribed compressed pairs.
- Every free row pair must belong to \\(\mathcal T\\).
- Membership in \\(\mathcal T\\) is exactly the condition that the row pair can be produced by an actual state-space row of \\(R\\).

After substituting \\(B\_{:,J}=I\_\omega\\), all remaining entries of \\(B\\) are unknowns \\(b\\). Equations (2)–(3) form a system

\\[ \boxed{M(X,G)b=c(X,G).} \tag{4} \\]

With the \\(G\\)-formulation, \\(M\\) and \\(c\\) have entries of degree at most one in \\(X,G\\), rather than degree at most two as in the original \\(F,X\\)-formulation.

This is a useful strengthening, not just a notational change.

### Why (4) is an exact reduction

Suppose q1 is feasible. Choose a rank-\\(\omega\\) pivot set, factor \\(H=XB\\), and use (5a) to obtain \\(G\\). The actual free rows belong to \\(\mathcal T\\), so (2)–(4) hold.

Conversely, suppose there are \\(X,G\\) and a solution \\(B\\) of (4), with \\(X\\) full column rank and \\(B\_{:,J}=I\\). Set

\\[ H=XB,\qquad H_A=GB. \\]

The fixed rows are correct, and every free compressed row pair belongs to \\(\mathcal T\\). Hence each free row has a state-space preimage, so there is an actual \\(R\\). Equation (1) and the left-inverse argument imply (5a).

Thus the only remaining condition to impose is (5b).

## 4. Rank-consistency elimination: correct

The identity

\\[ Mb=c \iff \operatorname{rank}M=\operatorname{rank}[M\ c] \\]

is standard.

Let

\\[ \Gamma=MM^{\mathsf T},\qquad \Gamma'=MM^{\mathsf T}+cc^{\mathsf T}. \\]

Since

\\[ [M\ c][M\ c]^{\mathsf T}=\Gamma', \\]

we have

\\[ \operatorname{rank}\Gamma=\operatorname{rank}M, \qquad \operatorname{rank}\Gamma'=\operatorname{rank}[M\ c]. \\]

Both matrices are positive semidefinite. For a positive-semidefinite matrix \\(G\\),

\\[ e_t(G)>0\iff \operatorname{rank}G\ge t, \\]

where \\(e_t\\) is the \\(t\\)-th elementary symmetric polynomial of its eigenvalues, equivalently the sum of its \\(t\times t\\) principal minors.

Therefore consistency is equivalent to

\\[ \boxed{ \bigvee\_{t=0}^{d_1} \left[ e_t(\Gamma)>0 \ \wedge\ e\_{t+1}(\Gamma)=0 \ \wedge\ e\_{t+1}(\Gamma')=0 \right], } \tag{5} \\]

where

\\[ d_1=\min\\{\operatorname{rows}(M),\operatorname{cols}(M)\\}. \\]

The logic of (5) is:

- The first two conditions force \\(\operatorname{rank}M=t\\).
- The last forces \\(\operatorname{rank}[M\ c]\le t\\).
- Since \\(\operatorname{rank}[M\ c]\ge\operatorname{rank}M=t\\), equality follows.

### Rectangular and degenerate cases

The use of \\(d_1\\), rather than just the row count of \\(M\\), is appropriate.

If \\(M\\) has more rows than columns, adding \\(c\\) could increase the rank from \\(d_1\\) to \\(d_1+1\\). The term \\(e\_{d_1+1}(\Gamma')=0\\) detects precisely that obstruction.

If \\(M\\) has no columns, \\(d_1=0\\). The only branch is \\(t=0\\), which says \\(c=0\\). That is exactly consistency of the system with no unknowns.

If \\(M\\) has full row rank, the augmented matrix cannot have larger rank than the row count, and the convention \\(e_j=0\\) beyond the matrix size handles the endpoint correctly.

Verdict: the formula is correct for all rectangular ranks and does not require a nondegeneracy assumption.

One practical improvement: construct the \\(e_t\\)'s as coefficients of the characteristic polynomial

\\[ \det(sI+\Gamma) \quad\text{and}\quad \det(sI+\Gamma'). \\]

This avoids explicitly expanding all principal minors.

## 5. Spectral condition: correct

From

\\[ H=XB,\qquad H_A=GB, \\]

we have

\\[ P(\lambda)=\lambda H-H_A=(\lambda X-G)B. \\]

Since \\(B\\) has full row rank, its image as a linear map onto \\(\mathbb C^\omega\\) is all of \\(\mathbb C^\omega\\). Consequently,

\\[ \operatorname{im}((\lambda X-G)B) =\operatorname{im}(\lambda X-G), \\]

and

\\[ \boxed{ \operatorname{rank}P(\lambda) =\operatorname{rank}(\lambda X-G). } \\]

Therefore

\\[ (5b)\iff \operatorname{rank}(\lambda X-G)=\omega \quad\forall\lambda\in\mathbb C. \tag{6} \\]

Impose

\\[ e\_\omega(X^{\mathsf T}X)>0 \\]

to guarantee full column rank of \\(X\\).

The maximal minors of the \\(q\times\omega\\) pencil

\\[ Q(\lambda)=\lambda X-G \\]

have no common complex zero exactly when (6) holds. The bounded-degree Bezout certificate from the FPT construction applies directly. Because \\(q\\) is fixed, the number of maximal minors is already bounded by \\(\binom q\omega\\).

Thus the spectral part introduces only \\(2\omega\\) auxiliary variables.

## 6. Fixed-\\(q\\) complexity: the claimed exponent is plausible

With the improved \\(G\\)-formulation, the number of real variables is

\\[ 2q\omega+2\omega \le 2q^2+2q =O(q^2). \tag{7} \\]

The first term counts \\(X,G\\); the second counts the spectral certificate. If strict positivity is converted into a polynomial equation rather than retained as an inequality, add one variable.

Let us count the other dimensions.

There are \\(r_0\le q\\) fixed rows and \\(r\le q\\) free rows. Each fixed row gives \\(2k\\) linear equations in \\(B\\), and each free row gives at most \\(2k-d_0\\) equations. Thus the number of rows in (4) is

\\[ O(qk). \\]

The number of unknown entries in \\(b\\) is

\\[ \omega(k-\omega)\le qk. \\]

Hence

\\[ d_1=O(qk). \\]

For each pivot chart:

- the number of rank-consistency polynomials in (5) is \\(O(qk)\\);
- their degrees are \\(O(qk)\\);
- the number of variables is \\(O(q^2)\\);
- the spectral certificate has \\(O(q)\\) equations of degree \\(O(q)\\).

The dependence on \\(k\\) in the consistency formula is polynomial. In particular, the large dimension of \\(B\\) does not generate additional quantified variables.

### 6.1 Why the pivot enumeration does not spoil the bound

For every \\(1\le\omega\le q\\), enumerate the sets \\(J\\) of \\(\omega\\) columns. The number of charts is at most

\\[ \sum\_{\omega=1}^q\binom{k}{\omega} \le(q+1)k^q. \\]

Run the real-feasibility algorithm separately on each chart. For each chart, the variable count is \\(O(q^2)\\); its number of polynomials and degrees are polynomial in \\(k\\).

A singly exponential existential-real algorithm with \\(m\\) variables, \\(s\\) polynomials of maximum degree \\(D\\), and coefficient bit length \\(\tau\\) has a representative bit-complexity bound of the form

\\[ \widetilde O\\!\left( \tau(sD)^{O(m)} \right), \tag{8} \\]

up to encoding-dependent logarithmic and polynomial factors. Renegar's decision and quantifier-elimination work is a standard source for these bounds.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车+1



Here, on each chart,

\\[ m=O(q^2),\qquad s,D=\operatorname{poly}(k,q). \\]

Thus a chart costs

\\[ \mathcal L^{O(q^2)} \\]

for fixed \\(q\\). Multiplication by \\(k^q\\) charts preserves that form:

\\[ \boxed{ T\_{\text{fixed }q}(\mathcal L) =\mathcal L^{O(q^2)}. } \tag{9} \\]

This is a legitimate XP-style parameterized bound in \\(q\\).

### 6.2 A point about symbolic polynomial construction

The rank-consistency polynomials have degree growing with \\(k\\), so it is not enough to say “there are \\(O(q^2)\\) variables” and invoke fixed-variable quantifier elimination without accounting for degrees.

For fixed \\(q\\), the number of monomials of degree at most \\(D=O(k)\\) in \\(O(q^2)\\) variables is

\\[ \binom{D+O(q^2)}{O(q^2)} =k^{O(q^2)}. \\]

This is polynomial in the input size for fixed \\(q\\). The coefficients can be computed using polynomial-matrix determinant algorithms, or characteristic-polynomial algorithms, over the fixed-dimensional polynomial ring.

This is why the fixed-\\(q\\) claim works. The degree grows, but only polynomially, and the number of variables is fixed.

Verdict: I accept the fixed-\\(q\\) proof skeleton, with the \\(G=FX\\) simplification and the explicit complexity accounting above. The proposed \\(\mathcal L^{O(q^2)}\\) bound is defensible.

# Part II. Fixed \\(\kappa\_{\rm obs}\\): the FPT proof

I regard this route as the stronger contribution. The key is that it does not merely reduce the number of variables: it also compresses the spectral certificate so that its construction does not enumerate the exponentially many row subsets.

## 7. Compressing the free rows

Set

\\[ d_0=\operatorname{rank}[N\ AN],\qquad \kappa\_{\rm obs}=r d_0. \\]

For each free row \\(r_i\\), the compressed pair is

\\[ (H_i,(H_A)\_i)=r_i[N\ AN]. \\]

The set of all possible pairs is exactly

\\[ \mathcal T=\operatorname{row}[N\ AN], \\]

which has dimension \\(d_0\\).

Choose a rational row basis \\(T_0\in\mathbb Q^{d_0\times 2k}\\) of \\(\mathcal T\\). Each free row pair can be written uniquely as

\\[ (H_i,(H_A)\_i)=\alpha_iT_0, \qquad \alpha_i\in\mathbb R^{1\times d_0}. \\]

Because the rows of \\(R\\) are independent variables, the \\(\alpha_i\\)'s are independent.

Therefore the total number of free real coordinates is exactly

\\[ \boxed{\kappa\_{\rm obs}=r d_0.} \\]

This part of the report is correct.

Also, because \\(N\\) has full column rank,

\\[ d_0=\operatorname{rank}[N\ AN]\ge\operatorname{rank}N=k. \\]

Thus, if \\(r\ge1\\),

\\[ \boxed{k\le d_0\le\kappa\_{\rm obs}, \qquad r\le\kappa\_{\rm obs}.} \tag{10} \\]

This is what allows the spectral certificate to have parameter-bounded dimension even when \\(q\\) is large.

### An important edge case: \\(r=0\\)

When \\(r=0\\), the parameter \\(\kappa\_{\rm obs}\\) is zero, but \\(q\\), \\(k\\), and \\(\omega\\) need not be bounded. The Gram–Cauchy–Binet FPT construction below cannot simply be applied with \\(\omega\\) treated as bounded.

This case must be handled separately.

Fortunately, it has a direct polynomial-time solution. Here \\(H,H_A\\) are fixed matrices. Test (5a) by rational linear algebra. If it holds, factor

\\[ H=XB,\qquad H_A=GB, \\]

using a pivot set, with \\(B\\) full row rank. Then

\\[ (5b)\iff Q(\lambda):=\lambda X-G \\]

has full column rank at every complex \\(\lambda\\).

For a fixed rational polynomial matrix \\(Q(\lambda)\\), this is equivalent to the existence of a polynomial left inverse

\\[ S(\lambda)Q(\lambda)=I\_\omega. \tag{11} \\]

Indeed, full column rank everywhere is equivalent to the maximal minors having gcd \\(1\\). The Bezout identity for those minors, combined with the adjugate formula, constructs a left inverse. Since the minors have degree at most \\(\omega\\), the multipliers can have degree less than \\(\omega\\), and an \\(S\\) of degree at most \\(2\omega-2\\) suffices.

One need not explicitly enumerate all maximal minors to test (11). Introduce the coefficients of a general \\(\omega\times q\\) polynomial matrix \\(S\\) of degree at most \\(2\omega-2\\) and solve

\\[ S(\lambda)Q(\lambda)=I\_\omega \\]

coefficient by coefficient. This is a rational linear system with polynomially many unknowns and equations. Thus the \\(r=0\\) branch can be decided in deterministic polynomial time.

If \\(\omega=0\\), it is simpler: test directly whether the fixed compressed matrices are both zero. If \\(k=0\\), the compressed conditions are vacuous.

This closes the \\(\kappa\_{\rm obs}=0\\) edge case without invoking an unbounded-dimensional real-algebraic computation.

## 8. Rank condition (5a) by Gram matrices

This part is fully correct.

Let

\\[ G_H=H^{\mathsf T}H,\qquad G_S=H^{\mathsf T}H+H_A^{\mathsf T}H_A. \\]

Then

\\[ \operatorname{rank}G_H=\operatorname{rank}H, \\]

and

\\[ \operatorname{rank}G_S =\operatorname{rank}\begin{bmatrix}H\\\H_A\end{bmatrix}. \\]

Because both matrices are positive semidefinite,

\\[ e_j(G)>0\iff\operatorname{rank}G\ge j. \\]

On the rank-\\(\omega\\) stratum,

\\[ \boxed{ (5a)\iff e\_\omega(G_H)>0,\qquad e\_{\omega+1}(G_S)=0. } \tag{12} \\]

For completeness, the logic is:

\\[ \operatorname{rank}H\ge\omega, \qquad \operatorname{rank}\begin{bmatrix}H\\\H_A\end{bmatrix}\le\omega. \\]

But stacking cannot reduce rank, so both ranks equal \\(\omega\\).

There is no need to impose a separate upper bound on \\(\operatorname{rank}H\\).

For \\(\omega=0\\), use \\(e_0=1\\); the condition \\(e_1(G_S)=0\\) forces \\(H=H_A=0\\).

For \\(\omega=k\\), \\(e\_{k+1}(G_S)=0\\) is automatic because \\(G_S\\) is \\(k\times k\\). This is correct: if \\(H\\) has full column rank, its row space is all of \\(\mathbb R^k\\), so (5a) holds automatically.

## 9. The bounded-degree Bezout lemma

This is the central algebraic lemma behind the compact spectral certificate. It deserves to be stated and proved explicitly in the paper.

Let

\\[ f_1,\ldots,f_s\in\mathbb R[\lambda], \qquad \deg f_i\le\omega, \qquad \omega>0. \\]

Suppose they have no common complex root. Then there exist real polynomials \\(g_i\\) of degree strictly less than \\(\omega\\) such that

\\[ \boxed{ \sum\_{i=1}^s g_i(\lambda)f_i(\lambda)=1. } \tag{13} \\]

### Proof

Choose a nonzero real linear combination

\\[ g=\sum_i a_i f_i. \\]

If some \\(f_i\\) is a nonzero constant, the conclusion is immediate. Otherwise \\(g\\) has finitely many complex roots.

At each root \\(\alpha\\) of \\(g\\), not all \\(f_i(\alpha)\\) can vanish, by the no-common-root assumption. Thus the real coefficient vectors \\(b=(b_1,\ldots,b_s)\\) satisfying

\\[ \sum_i b_i f_i(\alpha)=0 \\]

form a proper real linear subspace of \\(\mathbb R^s\\). Avoiding the finite union of these proper subspaces gives a real vector \\(b\\) such that

\\[ h=\sum_i b_i f_i \\]

does not vanish at any root of \\(g\\).

Hence \\(g,h\\) are coprime over \\(\mathbb C[\lambda]\\), and therefore over \\(\mathbb R[\lambda]\\). The ordinary two-polynomial Bezout theorem gives

\\[ u g+v h=1, \\]

where

\\[ \deg u<\deg h\le\omega,\qquad \deg v<\deg g\le\omega. \\]

Expanding \\(g,h\\) into the original \\(f_i\\)'s gives (13), with each multiplier having degree less than \\(\omega\\). \\(\square\\)

This proves the degree bound without an iterative Euclidean algorithm involving an increasing number of polynomials.

## 10. The \\(2\omega\\)-dimensional Gram certificate

Let \\(f_i\\) be all \\(\omega\times\omega\\) minors of \\(P(\lambda)\\), and write

\\[ f_i(\lambda)=\sum\_{a=0}^{\omega}c\_{i,a}\lambda^a, \\]

with out-of-range coefficients interpreted as zero.

Form \\(B\\) with rows indexed by \\((i,j)\\), \\(0\le j<\omega\\), and columns indexed by \\(0\le t<2\omega\\):

\\[ B\_{(i,j),t}=c\_{i,t-j}. \tag{14} \\]

Thus each row is the coefficient vector of \\(\lambda^j f_i(\lambda)\\).

By the Bezout lemma,

\\[ (5b)\iff e_0\in\operatorname{row}B. \\]

For real matrices,

\\[ \operatorname{row}B=\operatorname{im}(B^{\mathsf T}B), \\]

because

\\[ \ker(B^{\mathsf T}B)=\ker B. \\]

Therefore

\\[ \boxed{ (5b)\iff \exists x\in\mathbb R^{2\omega}: B^{\mathsf T}Bx=e_0. } \tag{15} \\]

This is correct.

A minor but important point for exposition: the entries of \\(B\\) are polynomials in the free-row coordinates, so the equation in (15) is a polynomial equation in those coordinates and the new auxiliary variable \\(x\\). We do not need to quantify over the entries of the enormous matrix \\(B\\) itself.

## 11. Cauchy–Binet compression: correct, and essential

This is the most important computational step.

The matrix \\(B\\) has one group of rows for every maximal minor of \\(P\\). There are

\\[ \binom q\omega\binom k\omega \\]

such minors. Explicitly constructing \\(B\\) would therefore introduce a dependence exponential in \\(q\\), which is unacceptable for the proposed FPT parameter.

Define

\\[ K(\lambda,\mu)=\sum_i f_i(\lambda)f_i(\mu). \\]

For each column subset \\(J\subseteq[k]\\), \\(|J|=\omega\\), let \\(P_J(\lambda)\\) denote the \\(q\times\omega\\) submatrix of \\(P(\lambda)\\) formed by columns in \\(J\\). Then Cauchy–Binet gives

\\[ \begin{aligned} K(\lambda,\mu) &=\sum\_{\substack{|I|=\omega\\\\|J|=\omega}} \det(P\_{I,J}(\lambda)) \det(P\_{I,J}(\mu))\\\ &=\boxed{ \sum\_{\substack{J\subseteq[k]\\\\|J|=\omega}} \det\\!\left(P_J(\lambda)^{\mathsf T}P_J(\mu)\right). } \end{aligned} \tag{16} \\]

The order of the two factors is important: the first matrix is transposed and the product is an \\(\omega\times\omega\\) matrix. The identity follows by applying Cauchy–Binet to

\\[ P_J(\lambda)^{\mathsf T}P_J(\mu). \\]

Write

\\[ K(\lambda,\mu)=\sum\_{a,b}S\_{a,b}\lambda^a\mu^b. \\]

Then

\\[ S\_{a,b}=\sum_i c\_{i,a}c\_{i,b}. \\]

Using (14),

\\[ \boxed{ (B^{\mathsf T}B)\_{t,t'} = \sum\_{j=0}^{\omega-1}S\_{t-j,t'-j}. } \tag{17} \\]

The sum over the shift index \\(j\\) is necessary. The report has it in the correct form.

### Why the \\(q\\)-dependence is polynomial

The compressed expression (16) has only

\\[ \binom{k}{\omega}\le2^k\le2^{\kappa\_{\rm obs}} \\]

terms when \\(r\ge1\\).

Each term is an \\(\omega\times\omega\\) determinant. Its entries are dot products over the \\(q\\) rows, so computing them costs polynomial time in \\(q\\). Since \\(\omega\le k\le\kappa\_{\rm obs}\\), the determinant dimension is parameter-bounded.

This is precisely the desired separation:

\\[ \boxed{ \text{parameter-dependent number of determinant terms} \times \text{polynomial dependence on }q. } \\]

No enumeration of the \\(\binom q\omega\\) row subsets occurs.

Verdict: the Cauchy–Binet compression and the corrected coefficient indexing are mathematically sound. I see no remaining dependence on \\(\binom q\omega\\).

## 12. Bit complexity of the FPT construction

This is where the report should become more explicit. The mathematical certificate is not sufficient by itself: one must bound the coefficient sizes after exact rational preprocessing and polynomial construction.

Assume throughout that the input \\(A,C,L_0\\) is rational and given in binary. Let \\(\mathcal L\\) denote its total bit length.

### 12.1 Rational preprocessing

Compute:

1. A rational basis \\(N\\) of \\(\ker[C;CA]\\).
2. A rational basis of \\(\mathcal T=\operatorname{row}[N\ AN]\\).
3. The fixed compressed row pairs.
4. The affine-linear representation of every free compressed pair in its \\(d_0\\) basis coordinates.

All these operations can be carried out by exact rational Gaussian elimination or fraction-free elimination.

The sizes of the numerators and denominators of the resulting basis vectors are polynomially bounded in \\(\mathcal L\\). One way to see the relevant bound is through determinant estimates for the rational submatrices used in elimination: after clearing denominators, the determinants have bit length polynomial in the dimensions and the original coefficient bit length.

Thus the preprocessing takes polynomial bit time and supplies a rational compressed parametrization whose coefficients have polynomial bit length.

### 12.2 Constructing the Gram polynomials

Each free compressed row is affine-linear—in fact linear—in its \\(d_0\\) coordinates. Hence \\(H,H_A\\), and \\(P(\lambda)\\) have entries of degree at most one in the \\(\kappa\_{\rm obs}\\) variables.

For (12), the Gram entries are sums over \\(q\\) rows of products of affine-linear forms. The elementary symmetric polynomials have degrees bounded by

\\[ 2\omega,\qquad 2(\omega+1), \\]

respectively.

For (16), every entry of

\\[ P_J(\lambda)^{\mathsf T}P_J(\mu) \\]

is a sum of \\(q\\) products of affine-linear forms. Its degree in the free coordinates is at most two. The determinant has size \\(\omega\\), so its degree is at most \\(2\omega\\). Thus

\\[ \deg\_{\text{free}} K\le2\omega. \\]

The same bound applies to the entries of \\(B^{\mathsf T}B\\).

Because \\(\omega\le\kappa\_{\rm obs}\\), the degrees of all final polynomials are bounded by a function of \\(\kappa\_{\rm obs}\\).

### 12.3 Coefficient bit lengths and construction time

The number of column subsets \\(J\\) in (16) is at most \\(2^{\kappa\_{\rm obs}}\\). Each determinant has dimension at most \\(\kappa\_{\rm obs}\\), with coefficients obtained from sums over \\(q\\) rows.

There are only a parameter-bounded number of products in each determinant, and only polynomially many input-row contributions. Exact rational additions and multiplications therefore produce coefficient bit lengths bounded by

\\[ f_1(\kappa\_{\rm obs})\operatorname{poly}(\mathcal L) \\]

for some computable \\(f_1\\).

The number of monomials in \\(\kappa\_{\rm obs}\\) variables of degree at most \\(2\kappa\_{\rm obs}+2\\) is also a function only of \\(\kappa\_{\rm obs}\\). Hence the complete polynomial system can be constructed in

\\[ \boxed{ f_2(\kappa\_{\rm obs})\operatorname{poly}(\mathcal L) } \\]

bit operations.

This is the part that converts the algebraic certificate into an actual parameterized algorithm.

### 12.4 Real-feasibility decision

The resulting formula has:

- at most \\(\kappa\_{\rm obs}\\) compressed free variables;
- \\(2\omega\\) Gram-certificate variables;
- one optional auxiliary variable if strict positivity is encoded using an equation rather than a strict inequality.

Thus

\\[ m\le\kappa\_{\rm obs}+2\omega+1 \le3\kappa\_{\rm obs}+1. \\]

If strict inequalities are allowed directly, the \\(+1\\) is unnecessary.

The number of polynomials and their degrees are bounded by functions of \\(\kappa\_{\rm obs}\\). Applying a singly exponential existential-real decision algorithm gives a running time of the form

\\[ \boxed{ f(\kappa\_{\rm obs})\operatorname{poly}(\mathcal L). } \tag{18} \\]

Renegar's real-algebraic decision bounds are an appropriate citation for this last step; the \\(\widetilde O(\tau(sD)^{O(m)})\\) form is a convenient schematic statement in terms of coefficient bit length \\(\tau\\), number \\(s\\) of polynomials, maximum degree \\(D\\), and number \\(m\\) of variables.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车+1



The fixed-\\(\kappa\_{\rm obs}\\) theorem should therefore be stated as follows.

> Theorem candidate — fixed effective free-row dimension.
>
> For rational input \\(A,C,L_0\\), q1 is decidable in
>
> \\[ f(\kappa\_{\rm obs})\mathcal L^{O(1)} \\]
>
> bit operations, where
>
> \\[ \kappa\_{\rm obs} =(q-r_0)\operatorname{rank}[N\ AN]. \\]
>
> The case \\(r=0\\) is handled by a polynomial-time polynomial-matrix left-inverse test; the case \\(k=0\\) is trivial.

I regard this as a strong theorem candidate, not just a numerical or symbolic identity. Its remaining work is formalizing all coefficient-size bounds and giving a complete implementation-level proof of (16)–(17).

# Part III. Combining the two algorithms

The two results are genuinely complementary, not redundant.

Recall

\\[ q=r_0+r,\qquad \kappa\_{\rm obs}=r\operatorname{rank}[N\ AN]. \\]

There is no general bound on \\(q\\) in terms of \\(\kappa\_{\rm obs}\\), because \\(r_0\\) can increase independently of the free-row count and the rank of the row-pair map.

Thus:

- Fixed \\(q\\) gives polynomial time with an exponent depending on \\(q\\).
- Fixed \\(\kappa\_{\rm obs}\\) gives an FPT algorithm even when \\(q\\) is unbounded.

Under the rational-input assumptions and the separate \\(r=0\\) treatment, both can be stated together as

\\[ \boxed{ T(\mathcal I) \le \min\left\\{ \mathcal L^{O(q^2)}, \ f(\kappa\_{\rm obs})\mathcal L^{O(1)} \right\\}. } \tag{19} \\]

The first bound is an XP result with parameter \\(q\\); it is not an FPT result in \\(q\\). The second is genuinely FPT in \\(\kappa\_{\rm obs}\\).

A particularly useful feature is that the parameter \\(\kappa\_{\rm obs}\\) measures something structural: the total dimension of the compressed freedom available to all free rows. It is not simply the observer order or the state dimension.

## Which should be the main theorem?

I recommend this order.

Main theorem: fixed-\\(\kappa\_{\rm obs}\\) FPT.

It is the more distinctive algorithmic result. The crucial new ingredient is the combination of:

- effective free-row compression;
- a bounded-degree Bezout identity;
- a \\(2\omega\\)-dimensional Gram certificate;
- Cauchy–Binet elimination of the exponentially many row subsets.

Second theorem: fixed-\\(q\\) polynomial time.

This is an independent and useful result. Its factorization and rank-consistency elimination are also conceptually valuable. It shows that fixed observer order has a polynomial-time decision procedure even when the effective free-row dimension is not bounded.

I would not present the fixed-\\(q\\) result merely as a corollary of FPT. It is not one: for fixed \\(q\\), \\(d_0\\) may grow with the state dimension, so \\(\kappa\_{\rm obs}\\) may still be unbounded.

# Part IV. Novelty and relationship to existing work

There are three relevant bodies of literature, and they should be positioned differently.

## 13. Fernando's 2026 characterization

The closest direct antecedent I found is Tyrone Fernando's 2026 preprint, Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger, arXiv:2609.37992.

This work explicitly formulates the algebraic and spectral observer conditions as the two rank equalities

\\[ \operatorname{rank} \begin{bmatrix} \mathcal LA\\\\\mathcal L\\\CA\\\C \end{bmatrix} = \operatorname{rank} \begin{bmatrix} \mathcal L\\\CA\\\C \end{bmatrix} \\]

and

\\[ \operatorname{rank} \begin{bmatrix} \lambda\mathcal L-\mathcal LA\\\CA\\\C \end{bmatrix} = \operatorname{rank} \begin{bmatrix} \mathcal L\\\CA\\\C \end{bmatrix}. \\]

It also uses the nullspace of \\([C;CA]\\), as in your reduction.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



More specifically, the paper:

- characterizes the algebraically admissible observer orders;
- gives a nullspace-basis parameterization of fixed-order algebraically admissible realizations;
- gives a matrix-pencil characterization of the spectral condition;
- characterizes fixed-order observer existence through those conditions.

Its fixed-order existence theorem uses a full-column-rank matrix \\(Z\\), together with algebraic and spectral rank tests.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



This is important related work. Your paper should cite it prominently and should not present the rank and pencil formulations themselves as new.

### But does Fernando's result imply your algorithms?

Not from the results I inspected.

There are two distinctions.

First, the synthesis architecture differs. In Fernando's formulation, a prescribed functional is required to be recoverable from an augmented functional matrix and the measured output. Your q1 formulation fixes a literal block

\\[ L=[L_0;R] \\]

and asks whether the remaining rows \\(R\\) can be chosen to complete it. Recoverability of a target functional from an augmented observer matrix is not the same restriction as requiring the target rows to occur unchanged as a fixed submatrix. If your q1 instance is intended to be a special case of his observer problem, the exact correspondence should be written down, including any reducedness or row-independence assumptions.

Second, the paper is a structural characterization, not a bit-complexity theorem. Its nullspace parameterization and finite matrix charts do not, by themselves, show that the feasibility problem can be decided in polynomial time for fixed \\(q\\), or in FPT time for your \\(\kappa\_{\rm obs}\\). The dimension of the nullspace parameterization can still grow with the state dimension.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



The safest positioning is:

> Fernando provides the closely related fixed-order algebraic and spectral characterization of functional-observer existence. We study the exact bit complexity of a more constrained synthesis problem with prescribed rows, deriving fixed-order and effective-free-dimension algorithms through compressed polynomial certificates.

I would also cite Fernando's related preprint A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions, arXiv:2609.33615, where the minimum algebraically admissible order and its associated spectral feasibility question are developed.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



## 14. Parametric linear systems literature

The relevant paper here is Corless, Giesbrecht, Rafiee Sevyeri, and Saunders, On Parametric Linear System Solving, arXiv:2508.21629 (2025).

It studies systems

\\[ M(z)b=c(z) \\]

that are linear in the unknowns \\(b\\), with polynomial dependence on parameters \\(z\\). It develops algorithms for describing parameter regimes and explicitly obtains polynomial-time results for up to three parameters.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



This is closely related to your fixed-\\(q\\) elimination step, but it does not make that step redundant.

Your system has \\(O(q^2)\\) parameters after factorization. For \\(q\ge2\\), that can exceed the three-parameter setting treated by their specialized result. Moreover, your objective is not to produce a comprehensive solution description for \\(b\\) across every parameter regime; it is to decide the existence of at least one \\(b\\) for a given parameter value.

The rank-consistency formula

\\[ \operatorname{rank}(MM^{\mathsf T}) = \operatorname{rank}(MM^{\mathsf T}+cc^{\mathsf T}) \\]

gives a direct semialgebraic description of consistency for any number of parameters. It is a particularly natural tool for your problem.

I would cite Corless et al. as related parametric-linear-system work, but not claim that their theorem implies your fixed-\\(q\\) result.

## 15. Real algebraic geometry and the correct complexity citation

The appropriate algorithmic foundation is existential real feasibility, rather than general quantifier elimination with arbitrary alternations.

For a formula with \\(m\\) real variables, \\(s\\) polynomials, maximum degree \\(D\\), and coefficient bit length \\(\tau\\), a standard singly exponential existential-feasibility bound has schematic form

\\[ \widetilde O\left(\tau(sD)^{O(m)}\right). \\]

This is the kind of bound needed in both proofs.

The primary references I recommend are:

1\. James Renegar, On the Computational Complexity and Geometry of the First-Order Theory of the Reals, Parts I–III, Journal of Symbolic Computation 13 (1992), pp. 255–352. The three parts develop decision and quantifier-elimination methods with bit-complexity analysis.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车+2



2\. Saugata Basu, Richard Pollack, and Marie-Françoise Roy, Algorithms in Real Algebraic Geometry, Springer, 2006. This is a standard source for exact real algebraic algorithms, existential feasibility, and effective semialgebraic geometry.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://link.springer.com\&sz=32)

Springer Link+1



3\. Marcus Schaefer, Jean Cardinal, and Tillmann Miltzow, The Existential Theory of the Reals as a Complexity Class: A Compendium, arXiv:2407.18006 (2024). This is useful for positioning the result within the \\(\exists\mathbb R\\) complexity landscape.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



I would cite Renegar for the quantitative decision bound and Basu–Pollack–Roy for the underlying algorithmic real algebraic geometry.

### A useful distinction about the \\(+1\\) variable

The report counts

\\[ \kappa\_{\rm obs}+2\omega+1 \\]

variables. The last variable is only needed if one insists on expressing

\\[ e\_\omega(G_H)>0 \\]

using equations alone, for example through

\\[ s^2e\_\omega(G_H)-1=0. \\]

If strict inequalities are allowed in the existential formula, the variable is unnecessary. Either convention yields the same FPT conclusion.

# Part V. Hardness: pause local gates, not the whole programme

My recommendation is to pause the current multiplication-gate and row-copy programme as the principal research line.

That recommendation is not based on a proof that sound multiplication is impossible. It is based on the difference between the current status of the two routes:

- The algorithmic route has explicit certificates, bounded variable counts, and a plausible bit-complexity proof.
- The hardness route has locally correct compressed constructions, but no sound multiplication gadget under unrestricted \\(R\\), and no reduction.

It is a question of research risk and proof maturity.

## 16. Is there a better hardness source?

I would investigate global subspace-realization problems rather than another isolated arithmetic gate.

The natural object is the pair

\\[ \mathcal T=\operatorname{row}[N\ AN], \qquad W=\operatorname{row}H. \\]

A feasible solution must have

\\[ \operatorname{row}H_A=W, \\]

and every free row pair must lie in \\(\mathcal T\\).

This is a constrained subspace-realization problem with an additional polynomial-pencil condition.

Three possible source directions are worth considering.

### 16.1 Matroid and subspace representation problems

Matroid representability and related subspace-arrangement realization problems naturally encode global incidence relations. Their advantage over local multiplication gates is that they are already formulated in terms of shared linear dependencies.

This matches the global condition

\\[ \operatorname{row}H_A=\operatorname{row}H \\]

better than independent gate blocks do.

But there is a substantial missing step: a matroid representation typically constrains which collections of vectors are dependent. It does not automatically impose the per-row pair-space restriction \\(\mathcal T\\), nor the condition that the pencil \\(\lambda H-H_A\\) has full rank at every complex \\(\lambda\\).

So this is a plausible source, not a known reduction.

### 16.2 Structured matrix completion

The compressed problem can be viewed as choosing free rows from a fixed linear space \\(\mathcal T\\), with the completed matrices required to have equal row spaces and a regularity property for their pencil.

This suggests looking at complexity results for structured matrix completion, rank-constrained completion, and subspace realization.

A useful reduction would need to preserve the following three features simultaneously:

\\[ \begin{aligned} & (H_i,(H_A)\_i)\in\mathcal T     &&\text{for every free row},\\\ & \operatorname{row}H_A=\operatorname{row}H,     &&\\\ & \operatorname{rank}(\lambda H-H_A)=\operatorname{rank}H     &&\forall\lambda\in\mathbb C. \end{aligned} \\]

I do not know of a standard hardness theorem that directly gives this combination.

### 16.3 Polynomial-matrix completion and unimodularity

There is also a possible route through polynomial matrices. The spectral requirement says that the pencil has a polynomial left inverse after compression:

\\[ G(\lambda)Q(\lambda)=I. \\]

This is a unimodularity or left-primeness condition.

Structured polynomial-matrix completion and unimodularity problems may be useful sources because they naturally combine coefficient constraints with a global polynomial certificate.

However, a hardness result for general polynomial-matrix completion is not enough. The polynomial matrix here has the special form

\\[ Q(\lambda)=\lambda X-G, \\]

and its coefficients are tied to the same row-pair space \\(\mathcal T\\). That structural restriction must be respected in any reduction.

### My recommendation

Explore these directions conceptually, but do not yet invest in a full reduction. The key question is whether a known hard realization problem can be represented directly through \\(\mathcal T\\) and the global pencil, without requiring row labels or artificial zero rows.

I would not claim that matroid realization or structured matrix completion gives q1-hardness until such a reduction is written and checked in both directions.

# Part VI. Reliability assessment of the report

Here is how I would label the claims after this audit.

| Claim                                                  | Assessment                                                                             |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| Rank factorization \\(H=XB,\ B\_{:,J}=I\\)             | P                                                                                      |
| Existential representation \\(H_A=FH\\)                | P                                                                                      |
| Replacement \\(G=FX\\), \\(H_A=GB\\)                   | P, and improves the formulation                                                        |
| Free-row constraints via \\(\mathcal T\\)              | P, exact                                                                               |
| Parametric system \\(Mb=c\\)                           | P, exact                                                                               |
| Gram rank-consistency formula                          | P, including rectangular and degenerate cases                                          |
| Spectral reduction to \\(\lambda X-G\\)                | P                                                                                      |
| Fixed-\\(q\\) polynomial-time conclusion               | Strong proof route, with the coefficient-construction analysis to be formalized        |
| Bounded-degree Bezout lemma                            | P                                                                                      |
| \\(2\omega\\)-dimensional Gram certificate             | P                                                                                      |
| Cauchy–Binet compression                               | P                                                                                      |
| Correct shifted-index formula for \\(B^{\mathsf T}B\\) | P                                                                                      |
| Fixed-\\(\kappa\_{\rm obs}\\) FPT conclusion           | Strong proof route, with bit-growth and the \\(r=0\\) branch to be included explicitly |
| c311, c312, c313, c278 checks                          | E as reported, but not independently reproduced here                                   |
| Multiplication hardness gadget                         | Not established                                                                        |
| Unrestricted q1 \\(\exists\mathbb R\\)-hardness        | Open in this programme                                                                 |

One point about the exact checks: the algebraic identities in c311–c313 are independently justified by the arguments above. The labels themselves describe computations that I have not rerun, because the scripts and their input/output records were not supplied. They should remain evidence for the displayed instances rather than substitutes for the general proofs.

# Part VII. How I would write the algorithmic paper

I suggest organizing the paper around two theorems and one central compression lemma.

## 17. Main theorem statements

Theorem A — Fixed observer order.

For every fixed \\(q\\), q1 can be decided in deterministic polynomial time over rational input. More quantitatively, the proposed algorithm has a bound of the form

\\[ T_A(\mathcal I)\le \mathcal L^{O(q^2)}. \\]

The proof should use:

1. Rank factorization with pivot charts.
2. The reduced variables \\(X,G\\), rather than \\(F,X\\).
3. Parametric linear consistency.
4. Gram rank-consistency elimination.
5. The bounded-dimensional spectral Bezout certificate.
6. Exact real-feasibility decision.

Theorem B — Fixed effective free-row dimension.

For rational input, q1 is decidable in

\\[ T_B(\mathcal I) \le f(\kappa\_{\rm obs})\mathcal L^{O(1)}, \\]

where

\\[ \kappa\_{\rm obs} =(q-r_0)\operatorname{rank}[N\ AN]. \\]

The proof should use:

1. The \\(d_0\\)-dimensional row-pair parametrization.
2. Gram encoding of (5a).
3. The univariate bounded-degree Bezout lemma.
4. The \\(2\omega\\)-dimensional certificate.
5. Cauchy–Binet computation of its Gram matrix.
6. The separate \\(r=0\\) and \\(k=0\\) cases.
7. Exact coefficient-height analysis and Renegar's decision bound.

These two statements together give an interesting algorithmic picture: the problem is tractable both when the observer order is fixed and when the effective dimension of the free-row map is fixed, even though neither parameter controls the other.

## 18. A central lemma worth highlighting

I would present the Cauchy–Binet identity as a named lemma, since it is arguably the most technically interesting part of the FPT result.

> Compressed determinantal Gram lemma.\
> Let \\(P(\lambda)\in\mathbb Q[\mathbf x,\lambda]^{q\times k}\\), and let \\(f_i\\) range over all maximal \\(\omega\times\omega\\) minors. The Gram polynomial\
> \\[\
> \sum_i f_i(\lambda)f_i(\mu)\
> \\]\
> can be computed as\
> \\[\
> \sum\_}\
> \det\left(P_J(\lambda)^P_J(\mu)\right).\
> \\]\
> Consequently, the \\(2\omega\times2\omega\\) Bezout Gram matrix can be constructed using at most \\(\binom{k}{\omega}\\) determinants of order \\(\omega\\), with polynomial dependence on the number \\(q\\) of rows.

The significance is that the ordinary Bezout certificate appears to have exponentially many generators, but the specific Gram matrix required by the certificate has a compact Cauchy–Binet representation.

That is a much more precise contribution than simply saying that a large family of minors can be handled symbolically.

## 19. What still needs to be completed before submission?

I would regard the following as the final proof checklist.

- State the input encoding explicitly: rational \\(A,C,L_0\\), binary representation.
- Fix the dimensions and row/column conventions for \\(N\\), \\(\mathcal T\\), and \\(D\\).
- Replace \\(F\\) with \\(G=FX\\) in the fixed-\\(q\\) proof.
- Give a formal proof that the system \\(Mb=c\\) is equivalent to the existence of the missing columns of \\(B\\).
- State the rectangular rank-consistency lemma with the \\(e_0\\) and endpoint conventions.
- Prove the real bounded-degree Bezout lemma.
- Derive the Cauchy–Binet identity with indices explicitly.
- Show that the coefficients of \\(B^{\mathsf T}B\\) are exactly the shifted sums in (17).
- Give explicit bounds on the number of polynomial variables, equations, degrees, and coefficient bit lengths.
- Handle \\(\omega=0\\), \\(k=0\\), and \\(r=0\\) explicitly.
- State exactly which version of the Renegar bit-complexity bound is being applied.
- Separate exact symbolic identities from script-based finite checks.
- Compare the scope of q1 carefully with Fernando's 2026 fixed-order observer characterization.

In particular, I would not leave the \\(r=0\\) branch implicit. It is easy to handle by a polynomial left-inverse test, and explicitly including it makes the FPT theorem valid even when the parameter is zero.

# Final verdict

## Recommended research direction

Fixed-\\(\kappa\_{\rm obs}\\) FPT

Prioritize

The Gram–Bezout–Cauchy–Binet construction is mathematically sound and has a credible exact bit-complexity proof.

Fixed-\\(q\\) polynomial time

Develop in parallel

The factorization and rank-consistency route works. Use \\(G=FX\\) to simplify it and make the \\(O(q^2)\\) variable bound transparent.

Hardness programme

Pause local gates

Do not abandon hardness, but stop treating the current multiplication realization as a sound gadget. Investigate global constrained-subspace and polynomial-matrix formulations instead.

The strongest potential paper is not a claim that q1 is \\(\exists\mathbb R\\)-hard. It is a carefully proved algorithmic classification result:

\\[ \boxed{ \begin{aligned} &\text{For every fixed }q,\quad q1\in\mathrm P,\\\\[2mm] &\text{parameterized by }\kappa\_{\rm obs},\quad q1\in\mathrm{FPT}. \end{aligned} } \\]

The first is an XP-style fixed-order result; the second is a genuine FPT result under a different structural parameter. Their combination is stronger and more informative than either alone.

The immediate next step should be a formal write-up of the Cauchy–Binet Gram-certificate lemma and the full coefficient bit-complexity proof. Once those are complete, the FPT theorem should be the centrepiece of the algorithmic paper.