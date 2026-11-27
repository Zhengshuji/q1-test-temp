# Referee report: Parameterized algorithms for functional observer feasibility

Overall assessment: Major revision required. There is a potentially valuable algorithmic contribution, but the current manuscript contains a fundamental issue in the reduction from the original rank conditions to the polynomial pencil. This issue must be resolved before either main theorem can be accepted.

I have examined both the manuscript, including Appendices A–C, and `REVIEW_NOTES.md`.

I will distinguish four things throughout this review:

1. Mathematical correctness: whether the statements and proofs follow from the definitions.
2. Algorithmic correctness: whether the proposed algorithms actually decide the original problem.
3. Complexity correctness: whether the claimed bit-complexity bounds follow from the constructions.
4. Research novelty: whether the results constitute new contributions relative to existing literature.

The distinction is important. A reduction can be mathematically elegant and computationally efficient while still failing to encode the original problem. Likewise, a correct theorem can be insufficiently novel for a strong journal.

My main conclusion is that the paper has a promising central idea: compressing the observer constraints to a low-dimensional space and exploiting the free-row geometry to obtain parameterized algorithms. However, the connection between the original conditions (5a)–(5b) and the proposed full-column-rank pencil condition needs a fundamental audit. There are also several independent issues in the fixed-order encoding and complexity accounting.

I would not recommend submitting the present version as a completed theorem paper. I would recommend continuing the project, beginning with the foundational audit below.

# Part I. The most important mathematical issue

## 1. Lemma A: the claimed equivalence for (5b)

This is the first point I would ask the authors to resolve.

The paper starts with

\\[ (5a)\quad \operatorname{rank} \begin{bmatrix} LA\\\L\\\CA\\\C \end{bmatrix} = \operatorname{rank} \begin{bmatrix} L\\\CA\\\C \end{bmatrix}, \\]

and

\\[ (5b)\quad \operatorname{rank} \begin{bmatrix} \lambda L-LA\\\CA\\\C \end{bmatrix} = \operatorname{rank} \begin{bmatrix} L\\\CA\\\C \end{bmatrix} \qquad \forall\lambda\in\mathbb C. \\]

Let

\\[ K_0=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \\]

and let \\(N\\) be a basis matrix for \\(K_0\\). Define

\\[ H=LN,\qquad H_A=LAN. \\]

The paper correctly establishes the following equivalence for (5a):

\\[ (5a) \iff \operatorname{row}H_A\subseteq\operatorname{row}H. \\]

Consequently, there exists \\(F\\) such that

\\[ H_A=FH. \\]

So far, the argument is sound.

However, consider (5b).

Equality of the two ranks in (5b) is equivalent to

\\[ \operatorname{row}(\lambda L-LA) \subseteq \operatorname{row}[L;CA;C]. \\]

Right multiplication by \\(N\\) gives the necessary condition

\\[ \operatorname{row}(\lambda H-H_A) \subseteq \operatorname{row}H. \\]

In fact, it gives an equivalence, by the same kernel argument used for (5a):

\\[ \boxed{ (5b)\_\lambda \iff \operatorname{row}(\lambda H-H_A) \subseteq\operatorname{row}H. } \\]

But if (5a) holds, then

\\[ H_A=FH, \\]

and therefore

\\[ \lambda H-H_A = (\lambda I-F)H. \\]

It follows immediately that

\\[ \operatorname{row}(\lambda H-H_A) \subseteq\operatorname{row}H \\]

for every complex \\(\lambda\\).

Thus, with (5a) and (5b) written exactly as they appear in the manuscript, (5b) is automatic once (5a) holds.

This is incompatible with the subsequent assertion

\\[ (5b) \iff \operatorname{rank}(\lambda H-H_A)=\omega \qquad\forall\lambda\in\mathbb C, \\]

where

\\[ \omega=\operatorname{rank}H. \\]

The latter is a much stronger condition.

### A simple counterexample

Take

\\[ H=\begin{bmatrix}1\\\0\end{bmatrix}, \qquad H_A=\begin{bmatrix}0\\\0\end{bmatrix}. \\]

Then

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H. \\]

For every \\(\lambda\\),

\\[ \lambda H-H_A = \begin{bmatrix}\lambda\\\0\end{bmatrix}. \\]

At \\(\lambda=0\\),

\\[ \operatorname{rank}(\lambda H-H_A)=0, \\]

whereas

\\[ \operatorname{rank}H=1. \\]

Nevertheless, the row-space inclusion required by (5b) holds for every \\(\lambda\\).

Therefore, the two conditions are not equivalent.

### Why this matters

This issue affects almost the entire manuscript:

- Lemma A(iii);
- Lemma A(iv);
- Lemmas D1–D2 as applied to observer feasibility;
- Theorem 1;
- Theorem 2;
- Proposition 3c;
- Theorem 3's pencil certificate;
- the combined complexity bound.

The polynomial-pencil machinery may be correct for the stronger condition, but that does not establish the original problem unless the stronger condition is actually equivalent to the original observer definition.

My recommendation: Before doing any further complexity optimization, verify the exact statement of (5b) against the original Fernando–Trinh–Jennings definition and the characterization papers cited in the manuscript.

There are two possibilities:

1. The manuscript has transcribed (5b) incorrectly. In that case, correct the definition and redo the compression proof.
2. The definition is correct as printed. In that case, the current spectral reduction does not characterize the stated problem.

This is a blocking issue, not a minor technical correction.

## 2. Correction after checking the original characterization

There is an important qualification to the preceding objection.

I checked Fernando's 2026 paper, Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger, including its original formulation and Theorem 4. The manuscript's two rank conditions are indeed the conditions used there.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



The missing step in my initial objection is the rank equality, not merely row-space inclusion.

To see this, put

\\[ B_0=\begin{bmatrix}CA\\\C\end{bmatrix}. \\]

For every matrix \\(M\\),

\\[ \operatorname{rank}\begin{bmatrix}M\\\B_0\end{bmatrix} = \operatorname{rank}B_0+ \operatorname{rank}(MN), \\]

where \\(N\\) is a basis of \\(\ker B_0\\).

Consequently, (5b) is equivalent to

\\[ \operatorname{rank}(\lambda H-H_A) = \operatorname{rank}H. \\]

Thus Lemma A(iii) is correct, and the maximal-minor criterion is appropriate.

My initial objection confused the inclusion implied by (5a) with the additional rank equality required by (5b). I withdraw that objection.

This is also an important confirmation of the paper's starting point: the spectral condition really does become a constant-rank pencil condition after compression.

The remaining issue is different: whether the subsequent algorithms encode this condition correctly in every detail. That is what I examine below.

# Part II. Independent audit of the main mathematical results

## 3. Lemmas A–D

My assessment is that most of the underlying algebra is sound, subject to the corrections identified later.

| Result                                      | Assessment | Required action                            |
| ------------------------------------------- | ---------- | ------------------------------------------ |
| Lemma A: compression                        | Correct    | Make the rank-quotient argument explicit   |
| Lemma B: free-row parametrization           | Correct    | Clarify the coordinate map                 |
| Lemma C: rank consistency                   | Correct    | Improve notation and complexity discussion |
| Lemma D1: Bézout degree bound               | Correct    | Give a slightly more formal proof          |
| Lemma D2: coefficient-vector representation | Correct    | No substantive change                      |
| Cauchy–Binet aggregation                    | Correct    | Strengthen the novelty discussion          |

### 3.1 Lemma A: compression

The key identity deserves to be stated explicitly.

For any matrix \\(M\\), with \\(N\\) a basis of \\(\ker B_0\\),

\\[ \operatorname{rank} \begin{bmatrix} M\\\B_0 \end{bmatrix} = \operatorname{rank}B_0+\operatorname{rank}(MN). \\]

This follows by considering the linear map induced by \\(M\\) on the quotient by \\(\ker B_0\\), or equivalently by choosing a basis adapted to \\(\ker B_0\\).

Applying it to the two rank conditions gives

\\[ (5a)\iff \operatorname{rank}\begin{bmatrix}H_A\\\H\end{bmatrix} =\operatorname{rank}H, \\]

and

\\[ (5b)\_\lambda\iff \operatorname{rank}(\lambda H-H_A) =\operatorname{rank}H. \\]

The second identity is particularly important: it explains why the spectral condition is a full-rank pencil condition rather than merely a row-space inclusion.

I recommend adding both identities directly to Appendix A.1. They make the entire compression argument much easier to verify.

There is also a useful conceptual observation:

\\[ (5a)\implies H_A=FH. \\]

Thus

\\[ \lambda H-H_A=(\lambda I-F)H. \\]

The spectral condition becomes

\\[ \boxed{ \operatorname{rank}((\lambda I-F)H)=\operatorname{rank}H \quad\forall\lambda\in\mathbb C. } \\]

This is a more transparent interpretation of the pencil condition: the induced dynamics must not destroy any direction in the compressed row space at any finite complex spectral value.

The manuscript should exploit this interpretation in its introduction.

### 3.2 Lemma B: free-row parametrization

This is one of the strongest structural parts of the paper.

Define

\\[ \Phi:\mathbb R^{1\times n}\longrightarrow \mathbb R^{2k}, \qquad \Phi(v)=(vN,vAN). \\]

Then

\\[ \operatorname{im}\Phi=\mathcal T =\operatorname{row}[N\ AN]. \\]

By rank-nullity,

\\[ \dim\mathcal T=d_0 =\operatorname{rank}[N\ AN]. \\]

Every free observer row therefore contributes exactly \\(d_0\\) independent real coordinates.

For \\(r=q-r_0\\) free rows, the total number is

\\[ \kappa\_{\rm obs}=rd_0. \\]

This is not merely a convenient upper bound on the number of variables. It is the exact dimension of the image of the free-row parametrization before imposing the observer constraints.

That is a genuine structural advantage.

I would make one improvement: introduce \\(\Phi\\) explicitly and formulate the result as a statement about the image of a linear map. This avoids making the argument appear dependent on a particular basis \\(N\\).

It also makes basis invariance immediate. Replacing \\(N\\) by \\(NQ\\), for nonsingular \\(Q\\), changes coordinates but not \\(d_0\\).

### 3.3 Lemma C: rank consistency

The identity

\\[ \exists b:\ Mb=c \iff \operatorname{rank}(MM^{\mathsf T}) = \operatorname{rank}(MM^{\mathsf T}+cc^{\mathsf T}) \\]

is correct over the reals.

Indeed,

\\[ \operatorname{im}(MM^{\mathsf T}) =\operatorname{im}M \\]

and

\\[ \operatorname{im}(MM^{\mathsf T}+cc^{\mathsf T}) =\operatorname{im}[M\ c]. \\]

Consequently, the two ranks agree exactly when \\(c\in\operatorname{im}M\\).

The elementary-symmetric-polynomial formulation is also correct.

For a positive semidefinite matrix \\(\Gamma\\),

\\[ e_t(\Gamma)>0,\qquad e\_{t+1}(\Gamma)=0 \\]

characterizes rank exactly \\(t\\).

The condition

\\[ e\_{t+1}(\Gamma')=0 \\]

then ensures that the augmented matrix has rank at most \\(t\\). Since \\(\Gamma'\succeq\Gamma\\), its rank cannot be smaller.

There is no mathematical objection here.

One improvement: distinguish carefully between the number of polynomial constraints and the cost of constructing their coefficients. The latter needs more explanation in the complexity section.

### 3.4 Lemma D1: rectangular Bézout degree bound

I independently checked the argument in Appendix A.4 and A.5.1.

The claimed bound

\\[ \deg g_i<\omega \\]

for

\\[ \sum_i g_i f_i=1 \\]

is valid when the \\(f_i\\) have degree at most \\(\omega\\) and no common complex root.

The reduction to two polynomial combinations is legitimate.

Choose

\\[ g=\sum_i a_i f_i \\]

nonzero. At every complex root \\(\alpha\\) of \\(g\\), not all \\(f_i(\alpha)\\) vanish. Thus

\\[ \sum_i b_i f_i(\alpha)=0 \\]

defines a proper real linear subspace of the possible coefficient vectors \\(b\\).

There are only finitely many roots of \\(g\\). A finite union of proper real linear subspaces cannot cover the entire real coefficient space.

We can therefore choose

\\[ h=\sum_i b_i f_i \\]

with no common root with \\(g\\).

Now

\\[ \gcd(g,h)=1. \\]

The ordinary Euclidean algorithm gives

\\[ ug+vh=1, \\]

where

\\[ \deg u<\deg h\le\omega, \qquad \deg v<\deg g\le\omega. \\]

Substitution yields

\\[ 1=\sum_i(ua_i+vb_i)f_i. \\]

Since \\(a_i,b_i\\) are constants,

\\[ \deg(ua_i+vb_i)<\omega. \\]

This proves the desired bound.

Mathematically sound

This is an important result because it works for a family of polynomials, not just a pair.

The manuscript should explicitly mention the zero-polynomial and constant-polynomial cases, although they do not invalidate the proof.

### 3.5 Lemma D2: coefficient-vector representation

This lemma is correct.

The coefficient vector of \\(\lambda^j f_i\\) is precisely the row indexed by \\((i,j)\\).

Therefore,

\\[ \operatorname{row}B = \left\\{ \operatorname{coeff}\left( \sum_i g_i f_i \right): \deg g_i<\omega \right\\}. \\]

Consequently,

\\[ (5b) \iff e_0\in\operatorname{row}B. \\]

For a real matrix,

\\[ \operatorname{row}B = \operatorname{im}(B^{\mathsf T}B). \\]

Hence

\\[ \boxed{ (5b)\iff \exists x:\ B^{\mathsf T}Bx=e_0. } \\]

This is a useful conversion of a universal spectral condition into a finite linear-algebraic certificate.

It is also worth emphasizing that the vector \\(x\\) need not be interpreted as the Bézout coefficients themselves. It is a certificate that the constant coefficient vector belongs to the row space. The actual Bézout coefficients can subsequently be recovered by solving a linear system.

## 4. The Cauchy–Binet aggregation: correct, but what is new?

This is the second major question in the accompanying note.

I checked the identities in §6.3 and Appendix A.4.

Let

\\[ P(\lambda)\in\mathbb R[\lambda]^{q\times k} \\]

and let \\(f\_{I,J}(\lambda)\\) denote its maximal minors.

The proposed kernel is

\\[ K(\lambda,\mu) = \sum\_{|J|=\omega} \det\left( P(\lambda)\_{:,J}^{\mathsf T} P(\mu)\_{:,J} \right). \\]

By Cauchy–Binet,

\\[ \det\left( P(\lambda)\_{:,J}^{\mathsf T} P(\mu)\_{:,J} \right) = \sum\_{|I|=\omega} f\_{I,J}(\lambda)f\_{I,J}(\mu). \\]

Summing over \\(J\\),

\\[ \boxed{ K(\lambda,\mu) = \sum\_{I,J} f\_{I,J}(\lambda)f\_{I,J}(\mu). } \\]

This is exactly the Gram kernel of all maximal minors.

There is no missing combinatorial factor, and the transpose placement is correct.

The coefficient identity

\\[ (B^{\mathsf T}B)\_{t,t'} = \sum\_{j=0}^{\omega-1} S\_{t-j,t'-j} \\]

also follows directly from the indexing convention.

### 4.1 What the construction achieves

Direct enumeration would require

\\[ \binom q\omega\binom k\omega \\]

maximal minors.

The proposed method uses only

\\[ \binom k\omega \\]

determinants of order \\(\omega\\).

Since

\\[ k\le d_0\le\kappa\_{\rm obs} \\]

for \\(r\ge1\\), the number of determinants is bounded by

\\[ 2^{\kappa\_{\rm obs}}. \\]

This is a genuine computational improvement.

In particular, it removes the dependence on enumerating the row subsets of a potentially large \\(q\times k\\) matrix.

### 4.2 Is this a new mathematical identity?

I would be cautious about claiming that it is.

The underlying identity is a direct application of classical Cauchy–Binet and the induced Gram structure on exterior powers.

There is a substantial literature on:

- compound matrices;
- Gram determinants;
- Bézout matrices;
- polynomial-matrix inversion;
- maximal minors and polynomial matrix coprimeness.

For background, the survey by Emiris and Mourrain, Matrices in Elimination Theory (1999), is relevant to the broader Bézoutian and elimination framework.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直接+2



I did not find, in the literature retrieved for this review, an exact statement of the particular aggregation used in §6.3 with the same complexity objective. That is not sufficient evidence that the construction is new.

My recommendation is:

Do not present Cauchy–Binet aggregation as an independently new algebraic theorem. Present it as an algorithmic compression tailored to the observer-feasibility problem.

The novelty claim should be about the combination:

1. the compressed observer formulation;
2. the Bézout Gram certificate;
3. the Cauchy–Binet aggregation;
4. the resulting parameterized reduction.

That combination is more defensible than claiming a new form of Cauchy–Binet.

### 4.3 A useful improvement to the paper

The manuscript currently proves the coefficient identity but does not sufficiently explain how the coefficients are actually computed.

I recommend adding an algorithm:

1\.&#x20;

# For each \\(J\subseteq[k]\\), form \\[ K_J(\lambda,\mu)

\det(P(\lambda){:,J}^{\mathsf T}\
P(\mu){:,J}).\
\\]

2\. Compute its coefficients using polynomial-matrix determinant algorithms.

3\. Sum the coefficients over \\(J\\).

4\. Recover \\(B^{\mathsf T}B\\) using the shifted coefficient identity.

This makes the computational contribution explicit.

It also avoids any impression that the algorithm merely replaces one exponential enumeration by another hidden enumeration.

## 5. A definite error in the Kronecker-form discussion

There is a separate, easily identifiable error in §8.1.

The paper states that both

\\[ Q(\lambda)=1 \\]

and

\\[ Q(\lambda)= \operatorname{diag}(1,1+\lambda) \\]

satisfy full column rank at every finite complex \\(\lambda\\).

The second example is false.

Indeed,

\\[ Q(-1)= \begin{bmatrix} 1&0\\\ 0&0 \end{bmatrix}, \\]

so

\\[ \operatorname{rank}Q(-1)=1<2. \\]

Its determinant is

\\[ \det Q(\lambda)=1+\lambda, \\]

which has the finite root \\(-1\\).

This is an actual mathematical error, although it does not invalidate Lemma 8.1 or the R0 algorithm.

The correct general statement is:

- right singular Kronecker blocks are forbidden;
- finite regular elementary-divisor blocks are forbidden;
- left singular blocks are permitted;
- infinite regular elementary-divisor blocks are permitted.

The first two restrictions are necessary to prevent a loss of full column rank at finite spectral values.

For an example of an infinite regular block, the scalar pencil

\\[ Q(\lambda)=1 \\]

is sufficient.

A valid two-dimensional example is

\\[ Q(\lambda)=I_2. \\]

Alternatively, one can use a nonconstant pencil with constant nonzero determinant, such as

\\[ Q(\lambda)= \begin{bmatrix} 1&\lambda\\\ 0&1 \end{bmatrix}. \\]

Both have full rank for every finite \\(\lambda\\).

Required correction: Replace the erroneous diagonal example and explicitly distinguish finite and infinite elementary divisors.

# Part III. Audit of the three main complexity claims

## 6. Theorem 1: fixed observer order

Main idea is valid; formula needs correction

The fixed-order approach is conceptually reasonable.

The central strategy is:

1. Fix the rank \\(\omega\\).
2. Enumerate a pivot set \\(J\\).
3. Write\
   \\[\
   H=XB,\qquad B\_{:,J}=I\_\omega.\
   \\]
4. Replace \\(H_A=FH\\) by\
   \\[\
   H_A=GB.\
   \\]
5. Eliminate the remaining entries of \\(B\\) using rank consistency.
6. Apply the spectral certificate to \\(\lambda X-G\\).

For fixed \\(q\\), the number of real variables is bounded independently of \\(n\\).

This is the reason the Renegar bound gives polynomial time for each fixed observer order.

### 6.1 A concrete error in the displayed formula

There is a dimension error in item 5 of the algorithm in §7.

The paper writes

\\[ D\begin{bmatrix} (X_iB)^{\mathsf T}\\\ ((GU)\_iB)^{\mathsf T} \end{bmatrix}=0. \\]

But the dimensions are

\\[ G\in\mathbb R^{q\times\omega}, \qquad U\in\mathbb R^{\omega\times q}, \\]

so

\\[ GU\in\mathbb R^{q\times q}. \\]

Its \\(i\\)-th row has \\(q\\) entries, whereas \\(B\\) has \\(\omega\\) rows.

Thus

\\[ (GU)\_iB \\]

is not defined in general.

The intended expression is almost certainly

\\[ \boxed{ D\begin{bmatrix} (X_iB)^{\mathsf T}\\\ (G_iB)^{\mathsf T} \end{bmatrix}=0. } \\]

This is exactly the free-row membership condition in Appendix B.

Alternatively, if the authors want to express everything through the matrix \\(F=GU\\), the second component should be

\\[ (GUX)\_iB, \\]

because \\(UX=I\_\omega\\) implies

\\[ GUXB=GB. \\]

I strongly recommend the first correction.

### 6.2 A second issue: the variable count

Theorem 1 states that the number of quantified variables is

\\[ N=2q\omega+2\omega. \\]

This counts \\(X,G,x\\), but not \\(U\\).

Yet the displayed formula invokes \\(U\\).

There are two possible repairs.

Repair A (preferable):

Use

\\[ e\_\omega(X^{\mathsf T}X)>0 \\]

and formulate the free-row condition using \\(G_iB\\). Do not introduce \\(U\\) as a quantified variable.

A left inverse \\(U\\) can be selected afterward in the correctness proof.

Then the stated variable count is valid.

Repair B:

Explicitly introduce \\(U\\) satisfying

\\[ UX=I\_\omega. \\]

In that case the number of variables becomes

\\[ N=3q\omega+2\omega. \\]

This is still

\\[ O(q^2), \\]

so the asymptotic exponent remains of the claimed form, but the exact count in the manuscript must change.

### 6.3 Is the complexity estimate correct?

The claimed bound is

\\[ \mathcal L^{O(q^2)}. \\]

I believe this is recoverable after the formula correction.

The important point is that the number of variables is bounded by

\\[ O(q^2), \\]

while the number and degrees of the polynomial constraints grow polynomially with the input dimensions.

For fixed \\(q\\), the pivot enumeration costs at most

\\[ (q+1)k^q, \\]

which is polynomial in the input size.

The rank-consistency test involves a matrix \\(M\\) whose dimensions are \\(O(qk)\\). Therefore its possible ranks range over \\(O(qk)\\) values.

For fixed \\(q\\), this is \\(O(k)\\).

The elementary symmetric polynomials have degree at most \\(O(qk)\\), hence \\(O(k)\\) when \\(q\\) is fixed.

Thus the structural count

\\[ N=O(q^2),\qquad s=\operatorname{poly}(k),\qquad D=O(k) \\]

is consistent with

\\[ (sD)^{O(N)} = \mathcal L^{O(q^2)}. \\]

However, the manuscript should explain how the polynomial constraints are constructed and represented.

In particular, elementary symmetric polynomials of \\(MM^{\mathsf T}\\) should be computed as coefficients of

\\[ \det(zI+MM^{\mathsf T}), \\]

using polynomial-matrix determinant algorithms, rather than relying on an implicit exponential determinant expansion.

For fixed \\(q\\), the number of variables is constant, and the dense polynomial representation has polynomial size in \\(k\\). This makes the complexity argument rigorous.

### 6.4 The question about the disjunction over \\(t\\)

The note asks whether the disjunction over \\(t\\) should be folded into \\(D\\) rather than \\(s\\).

My answer is no.

The rank-consistency condition is

\\[ \bigvee\_{t=0}^{d_1} \left[ e_t(\Gamma)>0,\quad e\_{t+1}(\Gamma)=0,\quad e\_{t+1}(\Gamma')=0 \right]. \\]

The disjunction is a Boolean combination of polynomial sign conditions.

It does not increase the degree of any individual polynomial.

There are two clean ways to handle it:

- include all branches in the Boolean formula and count their polynomial constraints;
- solve each branch separately and add the running times.

The second method is especially transparent.

There are \\(O(d_1)\\) branches, so the additional factor is polynomial in \\(k\\) for fixed \\(q\\).

It should therefore be counted in the formula size or as an external multiplicative factor, not incorporated into the polynomial degree \\(D\\).

Verdict on Theorem 1: The mathematical strategy is sound, and the claimed asymptotic result appears recoverable. The displayed encoding is not correct as currently written because of the \\(GU\\) dimension error and the missing variable \\(U\\). These are fixable, but the proof must be rewritten to match the corrected formula.

## 7. Theorem 2: fixed effective dimension

Strongest potential contribution

This is the theorem I consider most interesting.

The central advantage is that it avoids the pivot-chart enumeration and works directly with the free-row coordinates.

For \\(r\ge1\\),

\\[ k\le d_0\le\kappa\_{\rm obs}. \\]

Consequently, the matrices

\\[ H,\ H_A \\]

have only \\(\kappa\_{\rm obs}\\)-bounded column dimension.

The algorithm uses the Gram matrices

\\[ G_H=H^{\mathsf T}H, \\]

and

\\[ G_S=H^{\mathsf T}H+H_A^{\mathsf T}H_A. \\]

The conditions

\\[ e\_\omega(G_H)>0, \\]

and

\\[ e\_{\omega+1}(G_S)=0 \\]

are equivalent to

\\[ \operatorname{rank}H=\omega, \\]

and

\\[ \operatorname{rank} \begin{bmatrix} H\\\H_A \end{bmatrix} =\omega. \\]

Thus they encode (5a).

This is correct.

The spectral certificate, after Cauchy–Binet compression, encodes (5b).

The number of variables is

\\[ N=\kappa\_{\rm obs}+2\omega \le3\kappa\_{\rm obs}. \\]

The polynomial degrees are bounded by a function of \\(\kappa\_{\rm obs}\\), and the coefficient bit lengths have the required parameterized bound.

Therefore, the real-feasibility step yields

\\[ \boxed{ T=f(\kappa\_{\rm obs})\operatorname{poly}(\mathcal L). } \\]

I find this argument substantially stronger than the fixed-order result.

### 7.1 One missing presentation detail: \\(\omega=0\\)

Lemma D is stated for \\(\omega\ge1\\).

However, §8 says that the spectral certificate is imposed for every

\\[ \omega=0,\ldots,q. \\]

The zero-rank branch should be separated explicitly.

For \\(\omega=0\\), the conditions are simply

\\[ H=0,\qquad H_A=0. \\]

Indeed, when \\(H=0\\), condition (5b) requires

\\[ \operatorname{rank}(-H_A)=0. \\]

Therefore,

\\[ H_A=0. \\]

This branch is easy to decide and is already handled elsewhere in the manuscript, but §8 should explicitly refer to it instead of applying Lemma D at \\(\omega=0\\).

### 7.2 The real strength of Theorem 2

I would emphasize the following distinction.

A naive observation that there are \\(\kappa\_{\rm obs}\\) free real coordinates would only show that the problem can be expressed as a \\(\kappa\_{\rm obs}\\)-variable real-algebraic problem.

That observation alone is not particularly interesting.

The actual contribution is that the authors avoid constructing an exponentially large collection of maximal minors.

They compute the spectral certificate through

\\[ \binom{k}{\omega} \\]

determinants rather than

\\[ \binom q\omega\binom k\omega \\]

minors.

This is what makes the preprocessing compatible with an FPT bound in \\(\kappa\_{\rm obs}\\).

I would make this the central theorem of the paper and give its proof more space than Theorem 1.

### 7.3 Does the parameterized bit-complexity argument work?

Broadly, yes.

The key requirements are:

\\[ N=f(\kappa\_{\rm obs}), \\]

\\[ s=f(\kappa\_{\rm obs}), \\]

\\[ D=f(\kappa\_{\rm obs}), \\]

and

\\[ B=f(\kappa\_{\rm obs})\operatorname{poly}(\mathcal L), \\]

where \\(B\\) denotes coefficient bit length.

Substitution into Renegar's real-feasibility bound yields an FPT running time.

The manuscript's coefficient-size argument is plausible:

- kernel bases are computed by rational elimination;
- the resulting rational entries have polynomial bit length;
- maximal minors have parameterized coefficient growth;
- the Cauchy–Binet aggregation uses only parameter-boundedly many determinants;
- elementary symmetric polynomials involve matrices of parameter-bounded dimension.

I would nevertheless expand the coefficient-size proof, particularly the passage from determinant coefficients to the coefficients of the final polynomial system.

The proof should distinguish:

1. the size of an individual rational coefficient;
2. the number of coefficients;
3. the cost of constructing the coefficients.

The current version mostly addresses the first.

## 8. Proposition 3c: the zero-free-row case

Mathematically sound

This part is stronger than the note suggests.

The important result is not merely that a rectangular pencil can have a polynomial left inverse. It is that the degree of the left inverse can be bounded independently of the number of maximal minors.

For

\\[ Q(\lambda)=\lambda X-G \in\mathbb Q[\lambda]^{q\times\omega}, \\]

full column rank at every finite complex value is equivalent to

\\[ \exists S(\lambda)\in \mathbb Q[\lambda]^{\omega\times q} \\]

such that

\\[ S(\lambda)Q(\lambda)=I\_\omega \\]

with

\\[ \deg S\le2\omega-2. \\]

The proof is valid for rectangular pencils.

For every \\(\omega\\)-element row subset \\(I\\), define

\\[ Q_I=E_IQ, \qquad f_I=\det Q_I. \\]

Then

\\[ \operatorname{adj}(Q_I)E_IQ = f_I I\_\omega. \\]

The Bézout identity

\\[ \sum_I g_I f_I=1 \\]

gives

\\[ S(\lambda)= \sum_I g_I(\lambda) \operatorname{adj}(Q_I(\lambda))E_I. \\]

Since

\\[ \deg g_I<\omega \\]

and

\\[ \deg\operatorname{adj}(Q_I)\le\omega-1, \\]

we obtain

\\[ \deg S\le2\omega-2. \\]

This is a complete proof.

### 8.1 The important algorithmic distinction

The adjugate construction is not itself an efficient algorithm because it may involve

\\[ \binom q\omega \\]

row subsets.

But the algorithm does not construct this sum.

It solves the coefficient equations directly:

\\[ -S_0G=I\_\omega, \\]

\\[ S\_{j-1}X-S_jG=0, \\]

\\[ S\_{2\omega-2}X=0. \\]

These equations are linear in the unknown coefficients of \\(S\\).

The unknown count is

\\[ (2\omega-1)q\omega \\]

and the equation count is

\\[ 2\omega^3. \\]

Both are polynomial in \\(q,\omega\\).

This is a particularly good piece of algorithmic reasoning: use a potentially large construction to establish a bounded certificate, then search for the certificate through a small linear system.

I would retain this section almost unchanged, apart from the Kronecker example and a more explicit treatment of rational bit complexity.

### 8.2 An additional opportunity

The polynomial left inverse provides more than a decision procedure.

It provides a verifiable certificate.

Given the solution of (R0), one can output

\\[ S_0,\ldots,S\_{2\omega-2} \\]

and verify

\\[ S(\lambda)(\lambda X-G)=I\_\omega \\]

by polynomial multiplication.

This is a useful constructive feature and should be highlighted in the abstract and conclusion.

## 9. Theorem 3: membership in \\(\exists\mathbb R\\)

The encoding in Appendix B is substantially better than a naive encoding through all maximal minors.

The main ingredients are:

\\[ H=XB, \qquad H_A=GB, \\]

\\[ UX=I\_\omega, \qquad BV=I\_\omega, \\]

and

\\[ S(\lambda)(\lambda X-G)=I\_\omega. \\]

The first two equations encode the factorization.

The next two guarantee the appropriate full-rank properties.

The last one encodes the spectral condition.

The additional data constraints

\\[ X_iB=h_i^0,\qquad G_iB=g_i^0 \\]

for fixed rows, and

\\[ D\begin{bmatrix} (X_iB)^{\mathsf T}\\\ (G_iB)^{\mathsf T} \end{bmatrix}=0 \\]

for free rows, are essential.

I checked both directions of the encoding.

### 9.1 From an encoding solution to an observer

Given a solution:

1. The fixed-row equations identify the rows corresponding to \\(L_0\\).
2. The free-row equations place each free pair in \\(\mathcal T\\).
3. Membership in \\(\mathcal T\\) guarantees a preimage row in the original state coordinates.
4. These preimages construct \\(R\\).
5. The equations \\(UX=I\_\omega\\) and \\(H_A=GB\\) imply\
   \\[\
   H_A=GUH.\
   \\]
6. The polynomial left inverse guarantees the spectral condition.

This direction is correct.

### 9.2 From an observer to an encoding solution

Given a feasible observer:

1. Choose a pivot factorization \\(H=XB\\).
2. Obtain \\(H_A=FH\\) from (5a).
3. Set \\(G=FX\\).
4. Choose left and right inverses of \\(X\\) and \\(B\\).
5. Use the rectangular Bézout construction to obtain \\(S\\).
6. Verify the fixed-row and free-row constraints.

This direction is also correct.

### 9.3 My assessment

The encoding is mathematically credible.

The main weakness is not its correctness but its exposition and formal status.

The manuscript should explicitly distinguish:

- the existence of the polynomial certificate;
- the finite polynomial system expressing that certificate;
- the proof that every solution corresponds to a feasible observer;
- the polynomial bound on the encoding size.

These are four separate statements.

I would also make clear that the \\(\omega=0\\) branch does not introduce a polynomial \\(S\\) of negative degree. It is a separate algebraic branch.

### 9.4 An important terminology correction

There is a conceptual issue in the paper's use of \\(q1\\).

The manuscript defines:

- \\(\mathrm{DEC}(q)\\): feasibility at a prescribed order;
- \\(\mathrm{OPT}\\): finding the minimum feasible order;
- \\(\mathrm{FIND}\\): constructing an optimal observer.

It then states

\\[ q1\in\exists\mathbb R. \\]

But Appendix B directly establishes an existential-real encoding of \\(\mathrm{DEC}(q)\\).

Membership of the optimization problem \\(\mathrm{OPT}\\) in \\(\exists\mathbb R\\) is not formally the same statement: optimization problems are generally function problems, not decision languages.

There is an easy repair.

Define the decision problem

\\[ \mathrm{MINDEC}(Q): \quad \text{Does there exist a feasible observer of order at most }Q? \\]

This can be encoded by a finite disjunction over

\\[ q=r_0,\ldots,Q. \\]

Then

\\[ \mathrm{MINDEC}\in\exists\mathbb R. \\]

Alternatively, explicitly state that \\(q1\\) refers to the decision version rather than the optimization function.

This terminology should be corrected throughout the abstract, introduction, and theorem statements.

# Part IV. Detailed responses to REVIEW_NOTES.md

I now address the six residual-risk questions directly.

## 10. Question 1: Is \\(\kappa\_{\rm obs}\\) the natural parameter?

My answer is:

Yes, it is a mathematically natural parameter for the present reduction. No, there is not yet evidence that it is an optimal or minimal parameter for the problem.

These are different claims.

### 10.1 Why it is natural

Recall the linear map

\\[ \Phi(v)=(vN,vAN). \\]

Its image has dimension

\\[ d_0=\operatorname{rank}[N\ AN]. \\]

The free-row choices are independent, so the combined map is

\\[ \Phi^{(r)}: (\mathbb R^{1\times n})^r \longrightarrow \mathcal T^r. \\]

Its image has dimension

\\[ \dim\mathcal T^r=rd_0. \\]

Thus

\\[ \kappa\_{\rm obs}=rd_0 \\]

is exactly the dimension of the free observer data after the first compression.

This is a strong justification for the parameter.

It is not an arbitrary product introduced to make an FPT theorem work.

### 10.2 Can we quotient further?

Potentially, yes.

There are at least three different levels of reduction worth investigating.

Level 1: the existing kernel quotient.

The map

\\[ v\mapsto(vN,vAN) \\]

already identifies rows that produce exactly the same compressed pair.

Its kernel is

\\[ \ker\Phi = \\{v:vN=0,\ vAN=0\\}. \\]

The dimension \\(d_0\\) is therefore minimal for representing the pair itself.

No further reduction is possible if the objective is to represent all pairs \\((vN,vAN)\\) without loss.

Level 2: quotient by observer-coordinate transformations.

The rank conditions depend on the row spaces of the observer matrices.

In particular, they are invariant under invertible transformations of the rows of \\(L\\).

Because the first \\(r_0\\) rows must remain equal to \\(L_0\\), the relevant transformations have a block lower-triangular structure:

\\[ T= \begin{bmatrix} I\_{r_0}&0\\\ U&S \end{bmatrix}, \qquad \det S\ne0. \\]

They preserve the fixed rows while changing the free rows by combinations of fixed and free rows.

This suggests that the space of free-row coordinates may contain redundant representations of the same observer subspace.

A quotient by this symmetry could potentially reduce the parameter.

However, this is not automatic.

One must preserve the fixed-row constraints and account for possible stabilizers and changes of rank.

Level 3: quotient by spectral invisibility.

This is the most interesting possibility.

The free rows enter through

\\[ H,\qquad H_A, \\]

and the spectral condition depends on

\\[ \lambda H-H_A. \\]

It may be possible to identify directions in the free-row space that affect neither the algebraic rank condition nor the spectral feasibility condition.

But the quotient must preserve the interaction between \\(H\\) and \\(H_A\\), not merely preserve the rank of \\(H\\).

A quotient that preserves the algebraic condition but changes the finite spectrum would be invalid.

### 10.3 My proposed research direction

I would formulate the next problem as follows.

Let \\(\mathcal P\\) be the affine space of admissible free-row pairs after imposing the fixed-row constraints.

Define an equivalence relation on \\(\mathcal P\\) by

\\[ (H,H_A)\sim(\widetilde H,\widetilde H_A) \\]

if the two pairs induce equivalent observer feasibility conditions.

The challenge is to find a finite-dimensional algebraic quotient

\\[ \mathcal P/\sim \\]

whose dimension is strictly smaller than \\(rd_0\\) on a nontrivial class of inputs.

There are two possible outcomes:

- a smaller parameter gives a stronger FPT theorem;
- the existing parameter is optimal within a natural class of linear or algebraic reductions.

The second outcome would also be a useful theoretical result.

### 10.4 A more immediate improvement

Before proving parameter optimality, investigate the effective rank of the free-row map after the fixed-row constraints.

The present parameter is

\\[ rd_0. \\]

But some free-row directions may already be constrained by \\(L_0\\).

A refined affine-dimension calculation could yield a smaller parameter without needing a complicated spectral quotient.

This should be investigated first.

## 11. Question 2: Is the Cauchy–Binet aggregation known?

My answer is nuanced.

The identity itself is classical. The particular use of it in this algorithm may be new.

The key equation is

\\[ \sum\_{|J|=\omega} \det\left( P(\lambda)\_{:,J}^{\mathsf T} P(\mu)\_{:,J} \right) = \sum\_{I,J} f\_{I,J}(\lambda)f\_{I,J}(\mu). \\]

This is an exterior-power Gram identity.

It is an immediate consequence of Cauchy–Binet.

Therefore, I would not claim the identity itself as a new theorem.

However, there is a potentially interesting algorithmic contribution:

- the spectral certificate is initially defined through all maximal minors;
- the coefficient Gram matrix would naively require their explicit enumeration;
- the Cauchy–Binet representation computes the same object without enumerating the row subsets.

That is the contribution.

### What I recommend

Add a short subsection titled:

Algorithmic aggregation of the maximal-minor Bézout Gram matrix.

State explicitly:

1. The algebraic identity follows from Cauchy–Binet.
2. The contribution is the resulting complexity reduction.
3. The reduction is especially useful when \\(q\\) is large but \\(k\\) is parameter-bounded.

Also add a literature comparison table.

| Existing mathematical tool      | Role in the paper                                      |
| ------------------------------- | ------------------------------------------------------ |
| Cauchy–Binet                    | Produces the Gram-kernel identity                      |
| Compound matrices               | Explain the maximal-minor structure                    |
| Bézout identities               | Convert spectral feasibility into a finite certificate |
| Polynomial-matrix left inverses | Justify the certificate                                |
| Renegar's algorithm             | Provides the bit-complexity bound                      |

This would make the novelty claim much more credible.

I would not spend months trying to establish that the bare identity has never appeared before. The stronger research opportunity is to establish that this particular aggregation gives an effective FPT reduction.

## 12. Question 3: Is the fixed-order count acceptable?

My answer:

The asymptotic conclusion is plausible, but the complexity accounting needs to be made more explicit.

The note correctly identifies the two points that require attention:

\\[ N\le2q^2+2q, \\]

and

\\[ s=O(k^2),\qquad D=O(k). \\]

The first bound is correct if the unnecessary auxiliary \\(U\\) is removed from the existential formula.

If \\(U\\) is retained, the variable count must include it, although the asymptotic order remains \\(O(q^2)\\).

For the second bound, I recommend writing out the dimensions of the consistency matrix.

Suppose

\\[ M\in\mathbb R^{m\times h}. \\]

Then the rank parameter \\(t\\) ranges over

\\[ 0\le t\le\min(m,h). \\]

In the construction, both dimensions are \\(O(qk)\\), so the number of possible rank branches is \\(O(qk)\\).

For fixed \\(q\\), this is \\(O(k)\\).

Each branch uses only a constant number of elementary symmetric polynomial conditions.

Thus the number of polynomial sign conditions grows polynomially with \\(k\\).

The degree of the largest elementary symmetric polynomial is at most \\(O(qk)\\), hence \\(O(k)\\) for fixed \\(q\\).

### How I would rewrite the complexity proof

I would introduce the following table:

| Quantity                  | Bound                                           |
| ------------------------- | ----------------------------------------------- |
| Real variables            | \\(O(q^2)\\)                                    |
| Pivot charts              | \\(O(k^q)\\)                                    |
| Rank-consistency branches | \\(O(qk)\\)                                     |
| Polynomial degree         | \\(O(qk)\\)                                     |
| Coefficient bit length    | \\(\operatorname{poly}(\mathcal L)\\)           |
| Total construction size   | \\(k^{O(q^2)}\operatorname{poly}(\mathcal L)\\) |

For fixed \\(q\\), this gives the desired polynomial bound.

The key improvement is to state the total construction cost, rather than only the number of variables and maximum degree.

### Should \\(t\\) be folded into \\(D\\)?

No.

The rank index \\(t\\) is a discrete branch index, not a polynomial degree.

It should be counted as an additional number of branches or sign conditions.

This is a standard distinction in real-algebraic complexity.

I would therefore retain the current conceptual organization, but make the polynomial-system construction explicit.

## 13. Question 4: Is the rectangular-pencil degree bound correct?

Yes.

I consider this one of the most solid parts of the manuscript.

The proof is independent of the square-pencil assumption.

For a rectangular matrix

\\[ Q(\lambda)\in \mathbb Q[\lambda]^{q\times\omega}, \qquad q\ge\omega, \\]

every maximal minor is the determinant of an \\(\omega\times\omega\\) submatrix.

If the pencil has full column rank for every finite complex \\(\lambda\\), these maximal minors have no common complex root.

Since \\(\mathbb Q[\lambda]\\) is a principal ideal domain, their greatest common divisor is a nonzero constant.

The Bézout argument gives coefficients of degree less than \\(\omega\\).

The adjugate then adds at most \\(\omega-1\\) degrees.

Hence

\\[ \boxed{\deg S\le2\omega-2.} \\]

There is no hidden square assumption.

### A useful generalization

The argument actually proves a slightly more general statement.

Suppose

\\[ Q(\lambda)\in\mathbb F[\lambda]^{q\times\omega} \\]

has entries of degree at most \\(d\\), where \\(\mathbb F\\) is a field.

Every maximal minor has degree at most

\\[ d\omega. \\]

The same two-polynomial Bézout argument yields multipliers of degree less than \\(d\omega\\).

The adjugate contributes at most

\\[ d(\omega-1). \\]

Thus one obtains the general bound

\\[ \boxed{ \deg S\le 2d\omega-d-1. } \\]

For \\(d=1\\), this becomes

\\[ 2\omega-2. \\]

This generalization may be worth including as a separate lemma.

It could become useful if the observer model is extended to higher-degree matrix pencils or polynomial system dynamics.

### My recommendation

Keep the current degree-bound proof.

Add the general degree-\\(d\\) version as a remark or corollary.

This makes the result more reusable without significantly lengthening the paper.

## 14. Question 5: Is the \\(\exists\mathbb R\\) encoding complete?

My assessment:

Yes, the encoding in Appendix B is mathematically convincing for the fixed-order decision problem.

The important correction from the earlier draft has been made: the data constraints are now present.

I would explicitly identify the roles of the two groups of constraints.

For the fixed rows:

\\[ X_iB=h_i^0,\qquad G_iB=g_i^0. \\]

These force the compressed observer to agree with the prescribed \\(L_0\\).

For the free rows:

\\[ D\begin{bmatrix} (X_iB)^{\mathsf T}\\\ (G_iB)^{\mathsf T} \end{bmatrix}=0. \\]

Since

\\[ \ker D=\mathcal T, \\]

these constraints guarantee that each free compressed pair has a preimage in the original state space.

This is exactly the necessary condition.

The witness construction is straightforward once these facts are stated.

### One subtle point worth emphasizing

The matrix \\(B\\) is not merely a factorization variable.

The condition

\\[ BV=I\_\omega \\]

is essential because it guarantees that \\(B\\) has full row rank.

Without it, the equivalence

\\[ \operatorname{rank}((\lambda X-G)B) = \operatorname{rank}(\lambda X-G) \\]

would not necessarily hold.

Similarly,

\\[ UX=I\_\omega \\]

is needed to establish the factorization

\\[ H_A=FH. \\]

These are not redundant technical constraints.

They are essential parts of the encoding.

### What remains to improve

I recommend writing the correctness proof as two separate propositions:

- Soundness: every real solution of the encoding gives a feasible observer.
- Completeness: every feasible observer produces a real solution of the encoding.

Then prove the two propositions independently.

This would make the formal structure considerably clearer.

Also, use the phrase

\\[ \mathrm{DEC}(q)\in\exists\mathbb R \\]

rather than \\(q1\in\exists\mathbb R\\) until the decision-versus-optimization terminology is resolved.

## 15. Question 6: Is the Renegar step justified?

The underlying use of Renegar's real-feasibility bounds is standard and appropriate.

However, the paper should make three things explicit.

### 15.1 Strict inequalities

The fixed-order and FPT formulas contain conditions such as

\\[ e\_\omega(G_H)>0. \\]

These are legitimate real-algebraic sign conditions.

They should not be silently treated as polynomial equations.

One can either use a real-feasibility model that directly supports strict inequalities or replace

\\[ f>0 \\]

by

\\[ \exists u:\ fu^2-1=0. \\]

The latter is equivalent over the reals.

The conversion adds a bounded number of variables per inequality and preserves the required parameter dependence.

### 15.2 Boolean disjunctions

The rank-consistency formula contains a finite disjunction.

The paper should specify whether the real-feasibility algorithm is applied to:

- the full Boolean formula; or
- each branch independently.

Both are acceptable, but the complexity accounting should reflect the chosen implementation.

### 15.3 Coefficient growth

This is the part that deserves the most careful treatment.

The paper should establish explicit bounds for:

\\[ \operatorname{bits}(N), \\]

\\[ \operatorname{bits}(D), \\]

\\[ \operatorname{bits}(H), \\]

\\[ \operatorname{bits}(H_A), \\]

and the coefficients of the final Gram and determinant polynomials.

The current Hadamard argument is reasonable, but it should be expanded into a sequence of lemmas.

In particular, it should explain how the common denominator is cleared and how the resulting integer coefficients are bounded.

### My conclusion on the six questions

Parameter \\(\kappa\_{\rm obs}\\)

Natural

Exact dimension of the free-pair coordinate space; optimality remains open.

Cauchy–Binet aggregation

Novelty unestablished

Correct and computationally useful; the identity itself is classical.

Fixed-order counting

Needs clarification

The exponent is plausible; repair the formula and document construction costs.

Rectangular degree bound

Correct

The adjugate–Bézout proof is valid for rectangular pencils.

Existential-real encoding

Correct for DEC(q)

Both directions work with the data constraints; clarify the decision language.

Renegar complexity

Needs fuller accounting

The approach is appropriate; explicitly handle sign conditions, disjunctions and bit growth.

# Part V. Originality and research significance

## 16. Is the paper's current contribution original?

This is probably the most important question from a publication perspective.

My assessment is:



Potentially original

&#x20;The combination of the structural reduction and the FPT algorithm is the strongest candidate for an original contribution.



However, I would not yet claim that every component is new.

I distinguish five contributions.

| Contribution                                  | Originality assessment                                            |
| --------------------------------------------- | ----------------------------------------------------------------- |
| Observer compression to \\(H,H_A\\)           | Primarily a reformulation of existing structural characterization |
| Fixed-order real-algebraic algorithm          | Potentially new algorithmic consequence                           |
| Free-row effective dimension                  | Strong candidate for original contribution                        |
| Cauchy–Binet Gram aggregation                 | Specific application may be new; underlying identity is classical |
| Rectangular polynomial left-inverse algorithm | Useful constructive algorithm; its ingredients are classical      |

### 16.1 Relationship with Fernando's characterization papers

The manuscript correctly acknowledges that it does not establish a new observer-order characterization.

The two relevant preprints are:

- [A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions](https://arxiv.org/abs/2609.33615?utm_source=chatgpt.com).
- [Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger](https://arxiv.org/abs/2609.37992?utm_source=chatgpt.com).

The second paper already establishes an order-by-order characterization and a matrix-pencil formulation of the spectral condition.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



In particular, its Theorem 4 gives a nullspace-based pencil characterization, and its Theorem 5 gives a fixed-order existence condition.

This means the present manuscript must not suggest that the reduction to a spectral pencil is itself its principal new theorem.

The computational question is different.

The characterization papers establish when an observer exists. The present paper asks how efficiently the corresponding existence problem can be decided.

That is a legitimate and potentially important research direction.

### 16.2 The most promising original result

I would identify Theorem 2 as the main contribution:

\\[ \boxed{ \mathrm{DEC}(q) \in \mathrm{FPT}(\kappa\_{\rm obs}), \qquad \kappa\_{\rm obs} = (q-r_0)\operatorname{rank}[N\ AN]. } \\]

The reason is that the theorem exploits a problem-specific geometric parameter rather than merely applying general real-algebraic elimination to the original observer variables.

Its strength comes from the combination of:

1. the free-row image-space parametrization;
2. the low-dimensional Gram representation;
3. the maximal-minor Bézout certificate;
4. the Cauchy–Binet aggregation;
5. the parameterized real-feasibility algorithm.

This is a coherent algorithmic contribution.

The novelty claim becomes considerably stronger if the authors can demonstrate that existing polynomial-matrix algorithms do not already yield the same parameterized reduction.

### 16.3 What I would not claim

I would avoid the following statements:

- A new characterization of minimum-order functional observers.
- A new general Bézout theorem.
- A new Cauchy–Binet identity.
- A polynomial-time algorithm for unrestricted \\(q1\\).
- An \\(\exists\mathbb R\\)-completeness result.

The manuscript already avoids most of these overclaims. That restraint is good.

### 16.4 What would make the originality claim substantially stronger?

I would add a comparison with the existing literature using the following distinction:

| Question                                                                 | Existing characterization work                        | Present work             |
| ------------------------------------------------------------------------ | ----------------------------------------------------- | ------------------------ |
| Which observer orders are feasible?                                      | Yes                                                   | Uses existing results    |
| What are the algebraic conditions?                                       | Yes                                                   | Uses existing conditions |
| What is the spectral pencil condition?                                   | Yes                                                   | Uses existing condition  |
| Can fixed-order feasibility be decided in polynomial time?               | Not established by the cited characterization results | Proposed                 |
| Is there an FPT algorithm in a problem-specific parameter?               | Not established by the cited characterization results | Proposed                 |
| Can the zero-free-row case be solved by a finite rational linear system? | Not established by the cited characterization results | Proposed                 |

The comparison must be phrased as a statement about the cited works, not as an exhaustive claim about every paper in the literature.

# Part VI. What I would change before submission

## 17. A prioritized correction list

I would divide the revisions into three levels.

## Priority 1 — Mathematical and logical corrections

Required before submission

1. Correct the dimensionally invalid free-row constraint in Theorem 1.
2. Correct the quantified-variable count or eliminate the auxiliary \\(U\\).
3. Correct the Kronecker-form example in §8.1.
4. Separate \\(\mathrm{DEC}(q)\\), \\(\mathrm{MINDEC}(Q)\\), and the optimization problem \\(\mathrm{OPT}\\).
5. Explicitly handle the \\(\omega=0\\) branch in Theorem 2.
6. Add the rank-quotient identity directly to Appendix A.1.
   ## Priority 2 — Proof and complexity improvements
   Strongly recommended
7. Expand the polynomial construction and coefficient-size accounting.
8. Explain the representation of elementary symmetric polynomials.
9. State how strict inequalities are handled.
10. State how the rank-consistency disjunction is processed.
11. Separate the existence proof of the Bézout certificate from its algorithmic construction.
12. Clarify that the FPT theorem concerns the prescribed-order decision problem unless an optimization parameter is explicitly defined.
    ## Priority 3 — Novelty and presentation
    Recommended for a stronger paper
13. Strengthen the comparison with Fernando's 2026 characterization work.
14. Reframe Cauchy–Binet as an algorithmic compression.
15. Make Theorem 2 the central contribution.
16. Add a precise discussion of parameter invariance and possible quotient reductions.
17. Include a constructive example illustrating the FPT reduction.
18. Expand the discussion of practical limitations and the size of \\(f(\kappa\_{\rm obs})\\).

## 18. A particularly important conceptual improvement: distinguish the two algorithms

At present, the paper gives roughly equal structural attention to Theorems 1 and 2.

I would change that.

Theorem 1 is an XP-type result:

\\[ T_1= \mathcal L^{O(q^2)}. \\]

Theorem 2 is an FPT result:

\\[ T_2= f(\kappa\_{\rm obs})\operatorname{poly}(\mathcal L). \\]

They answer different questions.

The first says that the complexity is controlled when the observer order is fixed.

The second says that the complexity is controlled when the effective dimension of the free-row space is fixed.

The second is the more interesting result.

I would organize the paper around this hierarchy:

1. Establish the compression.
2. Establish the finite spectral certificate.
3. Derive the FPT algorithm.
4. Present fixed-order tractability as a complementary consequence.
5. Present the zero-free-row algorithm as a boundary-case result.
6. Establish existential-real membership.

This gives the paper a clearer central message.

# Part VII. A research roadmap toward a substantially stronger paper

The current results are promising, but I would not stop at the existing two algorithms.

There are several directions that could lead to a stronger contribution.

## 19. Research direction A: improve the parameter

Highest priority for theoretical advancement

The existing parameter is

\\[ \kappa\_{\rm obs}=rd_0. \\]

The immediate question is whether the factor \\(r\\) can be reduced.

Consider the affine space of all free-row pairs after fixing \\(L_0\\).

The observer feasibility conditions are invariant under certain changes of row coordinates. This suggests that the actual number of degrees of freedom may be smaller than \\(rd_0\\).

I would investigate:

\\[ \kappa\_{\rm eff} = \dim(\text{free-row parameter space}/\text{observer equivalence}). \\]

The main technical challenge is to characterize the equivalence relation algebraically.

A useful first target is not a complete quotient theory. It is a provable reduction in a restricted setting.

For example:

- one free row;
- a fixed number of fixed rows;
- a prescribed rank of \\(H\\);
- a family with special invariant-subspace structure.

If a smaller parameter can be established even for one nontrivial class, it would strengthen the research.

## 20. Research direction B: seek a direct algorithm avoiding general real algebraic geometry

Theorem 2 currently relies on Renegar's algorithm.

This gives a theoretically clean FPT result, but the function \\(f\\) may be enormous.

The spectral condition is a univariate polynomial-matrix condition.

That structure may permit more efficient algorithms.

Possible approaches include:

1. polynomial-matrix gcd algorithms;
2. subresultant sequences;
3. structured Bézout matrices;
4. rank-profile algorithms;
5. generalized eigenvalue and Kronecker methods;
6. determinantal representations of the coefficient Gram matrix.

The key is to exploit the special dependence of the pencil on the free-row variables.

A general real-algebraic solver treats the problem as an arbitrary polynomial system. A specialized algorithm could potentially exploit its matrix-pencil structure.

I would consider this the most promising route toward a practically useful algorithm.

## 21. Research direction C: investigate whether the problem is actually in P

The present results do not resolve unrestricted complexity.

There are three possibilities:

\\[ q1\in\mathrm P, \\]

\\[ q1\text{ is }\exists\mathbb R\text{-complete}, \\]

or an intermediate classification.

The current paper does not distinguish them.

A useful intermediate target would be to investigate whether the special pencil structure restricts the existential-real encoding sufficiently to admit a polynomial algorithm.

The relevant distinction is that the paper's polynomial constraints are not arbitrary.

They originate from:

\\[ H=LN,\qquad H_A=LAN, \\]

and the spectral pencil

\\[ \lambda H-H_A. \\]

The two matrices are coupled by the same observer rows.

This coupling may impose additional algebraic structure not present in general existential-real problems.

One possibility is that the spectral condition can be represented through a smaller collection of structured rank conditions.

Another is that the algebraic constraints force the relevant pencil into a class with efficient coprimeness testing.

Neither possibility has been established. Both deserve investigation.

## 22. Research direction D: hardness

I would not attempt an arbitrary \\(\exists\mathbb R\\)-hardness reduction immediately.

A better approach is to study simpler restrictions.

For example:

- one free row;
- fixed rank \\(\omega=1\\);
- a prescribed kernel dimension \\(k\\);
- sparse \\(A\\);
- special forms of \\(C\\);
- diagonal or nilpotent \\(A\\).

The objective would be to identify the first setting where the feasibility problem becomes nontrivial.

If a restricted case is polynomial, that may reveal additional structure.

If a restricted case is already hard, it may suggest a route to a general hardness reduction.

The important point is to preserve the special form

\\[ H=LN,\qquad H_A=LAN. \\]

An arbitrary polynomial-pencil hardness construction is not automatically an observer-feasibility hardness construction.

## 23. Research direction E: a more general polynomial-matrix result

The rectangular-pencil argument suggests a possible independent theorem.

For

\\[ Q(\lambda)=Q_0+\lambda Q_1+\cdots+\lambda^d Q_d \\]

with \\(q\ge\omega\\), determine the smallest uniform degree bound for a polynomial left inverse under the condition

\\[ \operatorname{rank}Q(\lambda)=\omega \qquad\forall\lambda\in\mathbb C. \\]

The current argument gives

\\[ \deg S\le2d\omega-d-1. \\]

It may be possible to improve this bound by exploiting dependencies among the maximal minors.

If a better bound is obtained, the resulting finite linear certificate could improve the complexity of the zero-free-row branch and potentially the general algorithm.

# Part VIII. References and literature improvements

## 24. References I recommend retaining or adding

The existing references are relevant, but I would broaden the algebraic and algorithmic background.

| Reference                           | Why it matters                                           |
| ----------------------------------- | -------------------------------------------------------- |
| Fernando, Trinh and Jennings (2010) | Original functional-observer rank conditions             |
| Fernando (2026a, 2026b)             | Recent minimum-order and order-spectrum characterization |
| Darouach and Fernando (2025)        | More recent functional-observer formulation              |
| Renegar (1992)                      | Real-algebraic decision complexity                       |
| Beelen and Van Dooren (1988)        | Kronecker form and singular pencils                      |
| Fabiano and Struppa (1990)          | Degree bounds for polynomial matrix left inverses        |
| Emiris and Mourrain (1999)          | Bézoutian and elimination matrix background              |
| Noferini and Van Dooren (2023)      | Polynomial eigenvalue and pencil background              |

The 2010 functional-observer paper is the foundational reference.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

数字对象标识符+1



The 2025 Automatica paper by Darouach and Fernando is also worth discussing because it develops a newer functional-observability and observer-design framework.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直接+1



For the rectangular-pencil argument, Fabiano and Struppa's work on degree bounds for polynomial matrix left inverses is particularly relevant.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://portal.mardi4nfdi.de\&sz=32)

MaRDI portal+1



One caution: the 2026 Fernando papers are arXiv preprints in the versions cited here. The manuscript should identify them as preprints unless their publication status has subsequently changed.

I would also add a paragraph explaining why the present complexity results are not already implied by the characterization papers.

That comparison is more important than simply adding more references.

# Part IX. Final referee assessment

## 25. Overall evaluation

Here is my assessment of the current manuscript.

| Criterion                       | Assessment                                    |
| ------------------------------- | --------------------------------------------- |
| Research question               | Important and well motivated                  |
| Structural compression          | Correct                                       |
| Free-row parametrization        | Strong                                        |
| Fixed-order algorithm           | Promising, requires formula correction        |
| FPT algorithm                   | Strongest potential contribution              |
| Bézout certificate              | Correct and useful                            |
| Cauchy–Binet aggregation        | Correct, novelty needs qualification          |
| Zero-free-row algorithm         | Strong mathematical component                 |
| \\(\exists\mathbb R\\) encoding | Correct for prescribed-order decision         |
| Complexity analysis             | Plausible, needs fuller accounting            |
| Originality                     | Promising but requires literature positioning |
| Presentation                    | Needs substantial revision                    |

## 26. What I believe the paper has actually established

After the audit, I would summarize the mathematical achievements as follows.

Result 1 — Structural reduction.

The observer feasibility conditions can be compressed to

\\[ H=LN,\qquad H_A=LAN, \\]

with

\\[ (5a)\iff \operatorname{row}H_A\subseteq\operatorname{row}H \\]

and

\\[ (5b)\iff \operatorname{rank}(\lambda H-H_A) =\operatorname{rank}H \quad\forall\lambda\in\mathbb C. \\]

Result 2 — Fixed-order tractability.

For prescribed \\(q\\), the problem admits a finite real-algebraic formulation with \\(O(q^2)\\) real variables.

After correcting the fixed-order formula, this supports

\\[ T_1=\mathcal L^{O(q^2)}. \\]

Result 3 — Effective-dimension FPT.

The free rows can be represented using exactly

\\[ \kappa\_{\rm obs} = r\operatorname{rank}[N\ AN] \\]

coordinates.

The Cauchy–Binet aggregation permits construction of the spectral certificate without enumerating all maximal minors.

This supports

\\[ T_2= f(\kappa\_{\rm obs})\operatorname{poly}(\mathcal L). \\]

Result 4 — Zero-free-row polynomial algorithm.

The rectangular pencil condition has a polynomial left inverse of degree at most

\\[ 2\omega-2. \\]

The coefficients can be found by solving a finite rational linear system.

Result 5 — Existential-real membership.

The prescribed-order decision problem admits a polynomial-size existential-real encoding.

These are meaningful results, provided the corrections and complexity details are incorporated.

## 27. My recommendation

# Major revision

The paper has a credible algorithmic research contribution, particularly in Theorem 2, but the current version is not yet ready for external submission.

The most important revision is to repair the fixed-order encoding and the decision-versus-optimization terminology.

The remaining work is largely proof clarification, complexity bookkeeping, and novelty positioning rather than abandoning the mathematical approach.

I would not abandon this project because of the issues identified here. Most are repairable, and the FPT construction has a coherent mathematical foundation.

However, I would not advertise the current draft as fully audited.

## 28. The single most important strategic recommendation

If I were directing this research project, I would make the next version of the paper revolve around the following theorem:

\\[ \boxed{ \begin{gathered} \text{Functional observer feasibility}\\\ \Downarrow\\\ \text{Low-dimensional free-pair parametrization}\\\ \Downarrow\\\ \text{Polynomial-pencil coprimeness}\\\ \Downarrow\\\ \text{Compressed Bézout Gram certificate}\\\ \Downarrow\\\ \text{FPT real-algebraic decision algorithm}. \end{gathered} } \\]

This is the paper's strongest narrative.

The fixed-order result, zero-free-row algorithm, and \\(\exists\mathbb R\\) encoding should support that central argument.

Most importantly, I would pursue one additional theoretical result before submission:

Determine whether the parameter \\(\kappa\_{\rm obs}\\) can be strictly reduced by quotienting out the observer-coordinate symmetries.

A successful result here could turn a sound parameterized-algorithm paper into a substantially more interesting contribution to the computational theory of functional observers.

My final judgment is that the project is worth continuing. The FPT theorem is the part I would invest the most effort in strengthening.