# Reliability audit of Routes A, B and C

The report is unusually helpful because it distinguishes proved statements, exact finite computations, and sketches. I would preserve that discipline. My audit finds:

1. Route A: the decomposition and incidence formulation are correct. The compressed determinant identity needs a rank qualification. The full observer realization remains open.
2. Route B: the equations/nonvanishing distinction is correct, but the proposed “shared-\\(f\\)” necessity is not established and appears too strong as stated.
3. Route C: the fixed-\\(\kappa\_{\rm obs}\\) result has a promising route to a rigorous FPT theorem, but the stated Bezout certificate needs a more careful treatment of the number of minors and certificate variables. There is a potentially useful way to compress that certificate. The fixed-\\(q\\) polynomial claim remains a sketch; linearity in \\(L\\) does not by itself eliminate the existential quantifier over \\(L\\).

I will use these labels:

-

  Correct

  &#x20;follows from the stated hypotheses.


-

  Needs qualification

  &#x20;is valid with an additional condition or a more precise formulation.


-

  Not established / incorrect

  &#x20;should not be stated as a theorem in its current form.



## 1. Question 1: claim-by-claim audit

### 1.1 Decomposition \\(AN=NM+E\\) and the resulting (5a) equivalence

Correct, with a notation refinement

Since \\(N\\) has full column rank, a left inverse \\(N^+\\) exists:

\\[ N^+N=I_k. \\]

Define

\\[ M=N^+AN,\qquad E=(I-NN^+)AN. \\]

Then

\\[ AN=NN^+AN+(I-NN^+)AN=NM+E. \\]

Also \\(N^+E=0\\). With \\(Y=RN\\),

\\[ H=\begin{bmatrix}H_0\\\Y\end{bmatrix}, \qquad H_A= \begin{bmatrix} H\_{A,0}\\\YM+RE \end{bmatrix}. \\]

The rows of \\(YM\\) are linear combinations of rows of \\(Y\\), and hence belong to \\(\operatorname{row}H\\). Therefore

\\[ \operatorname{row}(H_A)\subseteq\operatorname{row}(H) \\]

is equivalent to

\\[ \boxed{ \operatorname{row}(H\_{A,0})\subseteq\operatorname{row}(H), \qquad \operatorname{row}(RE)\subseteq\operatorname{row}(H). } \\]

The only notation refinement is that \\(H\_{A,0}\in\operatorname{row}H\\) must mean that each row of \\(H\_{A,0}\\) belongs to \\(\operatorname{row}H\\).

The choice of \\(N^+\\) is legitimate, but \\(M\\) and \\(E\\) depend on that choice. The invariant object is the induced map

\\[ K_0\longrightarrow \mathbb R^n/K_0, \qquad x\longmapsto Ax+K_0, \\]

where \\(K_0=\operatorname{im}N\\). The matrix \\(E\\) represents this transverse action in a chosen complement. A theorem about the construction should ideally be phrased in terms of this quotient map, not a particular \\(E\\).

### 1.2 Incidence form

Correct

For every \\(R\\),

\\[ RE\in\operatorname{row}(H) \\]

means that every row of \\(RE\\) belongs to \\(\operatorname{row}(H)\\). Equivalently,

\\[ W_R:=\operatorname{row}(RE) \subseteq\operatorname{row}(H). \\]

This is a Grassmannian incidence condition. The important qualification is that \\(W_R\\) is not fixed independently of the unknowns: it depends on \\(R\\). It is therefore a coupled incidence condition, not simply a fixed-subspace incidence problem.

The report's conclusion is appropriately restrained: this mismatch prevents a naive identification of each ARM affine equation with one incidence, but does not prove that a family of such incidences cannot encode an affine system.

### 1.3 Compressed determinant identity

Correct on the stated chart; incorrect as an unrestricted equivalence

Here

\\[ H= \begin{bmatrix} 1&0&0&0\\\ 0&1&0&0\\\ 0&0&r\_{11}&r\_{12}\\\ 0&0&r\_{21}&r\_{22} \end{bmatrix}. \\]

Consequently,

\\[ \operatorname{rank}H = 2+ \operatorname{rank} \begin{bmatrix} r\_{11}&r\_{12}\\\ r\_{21}&r\_{22} \end{bmatrix}. \\]

Thus

\\[ \operatorname{rank}H=3 \iff \begin{cases} r\_{11}r\_{22}-r\_{12}r\_{21}=0,\\\ (r\_{11},r\_{12},r\_{21},r\_{22})\ne(0,0,0,0). \end{cases} \\]

The determinant equation alone is equivalent to

\\[ \operatorname{rank}H\le3, \\]

not to rank exactly three.

On the chart \\(r\_{11}=1\\), the nonzero condition is automatic and the gate becomes

\\[ r\_{22}=r\_{12}r\_{21}. \\]

So the compressed multiplication identity is valid. But it is not yet an observer gate: no \\(A,C,L_0\\) have been shown to realize the specified compressed data, and the chart restriction must be implemented in the actual reduction.

### 1.4 Polarity of (5a) and (5b)

Correct, with the usual rank-stratum qualification

For fixed rank \\(\omega\\), (5a) is equivalent to

\\[ \operatorname{rank} \begin{bmatrix}H_A\\\H\end{bmatrix} = \operatorname{rank}H =\omega. \\]

It can be expressed using polynomial equalities (vanishing of all \\((\omega+1)\\)-minors) and a nonvanishing condition ensuring rank at least \\(\omega\\).

For (5b), let \\(f_I(\lambda)\\) range over the \\(\omega\times\omega\\) minors of \\(P(\lambda)\\), assuming \\(\operatorname{rank}H=\omega\\). Then

\\[ (5b) \iff \text{the polynomials }f_I\text{ have no common complex root} \iff \gcd_I f_I=1 \\]

up to multiplication by a nonzero constant.

This is a nonvanishing/unit-ideal condition, not an equation requiring a coefficient to vanish.

One caution: if \\(\omega\\) is not fixed, the whole formula is a finite disjunction over possible ranks. That is harmless for fixed parameters, but should be made explicit in a complexity proof.

### 1.5 The shared-\\(f\\) necessity

Not established; too strong as stated

The assertion

> To make the gcd exactly \\(f\\), every free row of \\(H\\) must be an \\(f\\)-multiple of a fixed vector

does not follow from the gcd condition alone.

A common factor of maximal minors is a statement about the determinantal ideal of the pencil. It does not generally imply a common factor in each row of \\(H\\).

For example, consider the compressed algebraic data

\\[ H= \begin{bmatrix} 1&0\\\ 0&1\\\ 0&0 \end{bmatrix}, \qquad F= \begin{bmatrix} a&0&0\\\ 0&a&0\\\ 0&0&b \end{bmatrix}, \qquad H_A=FH. \\]

Then

\\[ P(\lambda)=(\lambda I-F)H = \begin{bmatrix} \lambda-a&0\\\ 0&\lambda-a\\\ 0&0 \end{bmatrix}. \\]

Its \\(2\times2\\) minors have gcd \\((\lambda-a)^2\\), although the nonzero rows of \\(H\\) are constant, not multiples of this polynomial.

This example illustrates the general point: common factors can arise from the action on the column space of \\(H\\), not only from rowwise divisibility.

It does not establish a full observer realization, nor does it directly refute a more specialized statement about a scalar factor \\(f\\) depending on the free variables. It does show that the stated necessity needs a much more specific hypothesis and proof.

I would replace it with:

> The proposed compressed gadget has not yet been shown to lift. A common scalar factor in all maximal minors imposes a determinantal degeneracy condition, but no general rowwise divisibility characterization has been proved.

That is accurate and leaves the route open.

## 2. Route A completion: what the compressed gate still needs

There is a useful distinction between the compressed gate and the observer realization.

The compressed gate asks for

\\[ H_0= \begin{bmatrix}e_1^\top\\\e_2^\top\end{bmatrix}, \qquad Y= \begin{bmatrix} 0&0&r\_{11}&r\_{12}\\\ 0&0&r\_{21}&r\_{22} \end{bmatrix}. \\]

But in an actual instance,

\\[ H_0=L_0N,\qquad Y=RN, \\]

and the same \\(A\\) must also determine \\(H_A=LAN\\). Thus \\(N\\), \\(H_0\\), \\(E\\), and \\(H_A\\) cannot be chosen independently.

### 2.1 Is \\(E=0\\) fatal?

Fatal under (5a) and positive rank, as in the stated rigidity claim

If \\(E=0\\), then

\\[ AN=NM, \\]

so

\\[ H_A=HM. \\]

Now (5a) says

\\[ \operatorname{row}(HM)\subseteq\operatorname{row}H. \\]

Thus \\(\operatorname{row}H\\) is an invariant subspace for right multiplication by \\(M\\). If \\(\omega>0\\), the restriction of that linear map to this nonzero finite-dimensional invariant subspace has a complex eigenvalue \\(\lambda\\). Therefore there is a nonzero row vector \\(u\in\operatorname{row}H\\) such that

\\[ uM=\lambda u. \\]

It follows that

\\[ u(\lambda I-M)=0. \\]

Since \\(u\\) is a linear combination of rows of \\(H\\), this implies

\\[ \operatorname{rank}\big(H(\lambda I-M)\big)<\operatorname{rank}H. \\]

But

\\[ P(\lambda)=\lambda H-H_A=H(\lambda I-M), \\]

contradicting (5b).

So, under these hypotheses,

\\[ \boxed{E=0,\quad (5a),\quad\omega>0 \quad\Longrightarrow\quad \text{(5b) fails}.} \\]

This confirms why a nontrivial transverse component is necessary for Route A.

### 2.2 What should \\(E\\) do?

It should not merely be nonzero. It must make the lower-block condition

\\[ \operatorname{row}(RE)\subseteq\operatorname{row}(H) \\]

nontrivial while permitting a pencil whose rank remains \\(\omega\\) at every complex \\(\lambda\\).

A sensible first target is a very small exact construction with:

- \\(q=4\\), \\(r_0=r=2\\);
- \\(k=4\\);
- the specified \\(H_0\\);
- the specified \\(Y\\);
- \\(\operatorname{rank}H=3\\) on the intended chart;
- an \\(E\\) for which \\(RE\in\operatorname{row}H\\) is compatible with the determinant equation;
- a verified \\(\gcd\\) of the \\(3\times3\\) minors equal to \\(1\\).

The last condition is essential. It is not enough to construct an \\(E\\) that preserves the multiplication equation in (5a).

### 2.3 How to exclude the chart boundary

On the compressed chart, \\(r\_{11}=1\\) makes the determinant equation a multiplication gate. A reduction must prevent solutions with \\(r\_{11}=0\\) from creating false positives.

Possible approaches, in descending order of attractiveness:

1. Gauge normalization: use the invariance of the observer conditions under invertible rescaling of a free row, provided the coordinate being normalized is nonzero. This normalizes a nonzero \\(r\_{11}\\), but does not prove it is nonzero.
2. A fixed affine incidence: design the fixed data so that the desired rank stratum forces a specified coordinate to be nonzero.
3. Spectral branch selection: use (5b) to rule out the boundary component, if an exact construction supports this.
4. Multiple charts: cover the intended projective locus by finitely many charts and reduce separately, or use a source normalization that guarantees the chosen chart.

I would not rely on “genericity” here. The reduction needs a proof that every feasible observer corresponds to a valid source solution.

## 3. Route C: fixed-\\(\kappa\_{\rm obs}\\) FPT

Promising, but the stated proof needs repair

There are two separate issues:

1. the parameter bounds;
2. the size of the algebraic certificate.

### 3.1 The parameter bounds: \\(q\\) is not bounded by \\(\kappa\_{\rm obs}\\)

You have

\\[ \kappa\_{\rm obs}=r\\,\operatorname{rank}[N,AN]. \\]

Since \\(N\\) has full column rank \\(k\\),

\\[ \operatorname{rank}[N,AN]\ge k. \\]

For \\(r\ge1\\) and \\(k\ge1\\),

\\[ k\le\kappa\_{\rm obs}, \qquad r\le\kappa\_{\rm obs}. \\]

But the assertion

\\[ q\le f(\kappa\_{\rm obs}) \\]

does not follow: \\(q=r_0+r\\), and the number \\(r_0\\) of fixed rows may grow independently of \\(r\\).

This does not necessarily destroy FPT. It means the proof must allow \\(q\\) to grow with the input and show that the dependence on \\(q\\) is polynomial, with an exponent independent of \\(\kappa\_{\rm obs}\\).

The exceptional cases should be separated:

- \\(r=0\\): there are no free observer rows; directly test the fixed candidate.
- \\(k=0\\): the compressed problem is trivial, since \\(K_0=\\{0\\}\\) and the fixed rows \\(CA,C\\) already have full column rank.
- \\(r,k\ge1\\): \\(r,k\le\kappa\_{\rm obs}\\).

### 3.2 The proposed Bezout degree bound

The proposed bound

\\[ \deg g_i\le(s-1)\omega \\]

is a safe-looking iterative bound, but the proof should be supplied. More importantly, using it directly introduces up to \\(s\omega\\) auxiliary coefficients, where

\\[ s=\binom q\omega\binom k\omega. \\]

Since \\(q\\) is not bounded by \\(\kappa\_{\rm obs}\\), that is not a bounded-variable certificate.

There is a sharper univariate observation that can potentially repair this.

Let \\(f_1,\ldots,f_s\in\mathbb R[\lambda]\\) have degree at most \\(\omega\\), and suppose

\\[ \gcd(f_1,\ldots,f_s)=1 \quad\text{in }\mathbb C[\lambda]. \\]

Then there exist two real linear combinations

\\[ g=\sum_i a_i f_i,\qquad h=\sum_i b_i f_i \\]

such that

\\[ \gcd(g,h)=1. \\]

Why? Choose a nonzero \\(g\\) in the real span of the \\(f_i\\). It has finitely many complex roots. Since the original family has no common root, at each root of \\(g\\) the condition \\(h(\alpha)=0\\) excludes a proper real linear subspace of choices of \\(b\\). A finite union of proper real linear subspaces cannot cover the coefficient space. Thus one can choose \\(h\\) avoiding every root of \\(g\\).

The ordinary two-polynomial Euclidean algorithm then gives

\\[ u(\lambda)g(\lambda)+v(\lambda)h(\lambda)=1, \qquad \deg u,\deg v<\omega. \\]

Expanding \\(g,h\\) gives

\\[ \boxed{ \sum\_{i=1}^s g_i(\lambda)f_i(\lambda)=1, \qquad \deg g_i<\omega. } \\]

This is stronger than the proposed \\((s-1)\omega\\) bound.

But it still does not immediately give an FPT certificate if one introduces all \\(s\omega\\) coefficients \\(g_i\\) as variables. We need to avoid that.

### 3.3 A compact Gram-matrix certificate for (5b)

There is a way to remove those \\(s\omega\\) auxiliary variables.

For each \\(f_i\\), form the coefficient vectors of

\\[ f_i,\lambda f_i,\ldots,\lambda^{\omega-1}f_i. \\]

Each such polynomial has degree at most \\(2\omega-1\\). Put all these coefficient vectors into a matrix \\(B\\) with \\(2\omega\\) columns.

The Bezout identity with \\(\deg g_i<\omega\\) exists exactly when the coefficient vector of the constant polynomial \\(1\\),

\\[ e_0=(1,0,\ldots,0)^\top\in\mathbb R^{2\omega}, \\]

belongs to the row space of \\(B\\).

Since \\(B\\) is real,

\\[ \operatorname{row}(B)=\operatorname{im}(B^\top B). \\]

Therefore

\\[ \boxed{ (5b)\iff \exists x\in\mathbb R^{2\omega}: B^\top Bx=e_0. } \\]

This certificate has only \\(2\omega\\) auxiliary variables, regardless of the number \\(s\\) of maximal minors.

There is a second compression: we need not construct \\(B\\) by enumerating all the minors.

Write the \\(\omega\\)-minors as

\\[ f\_{I,J}(\lambda) =\det P(\lambda)\_{I,J}, \\]

where \\(|I|=|J|=\omega\\). Define

\\[ K(\lambda,\mu) = \sum\_{\substack{I\subseteq[q],\\,J\subseteq[k]\\\ |I|=|J|=\omega}} f\_{I,J}(\lambda)f\_{I,J}(\mu). \\]

For each fixed \\(J\\), Cauchy–Binet gives

\\[ \sum\_{|I|=\omega} f\_{I,J}(\lambda)f\_{I,J}(\mu) = \det\\!\left( P(\lambda)\_{:,J}^{\mathsf T} P(\mu)\_{:,J} \right). \\]

Hence

\\[ \boxed{ K(\lambda,\mu) = \sum\_{\substack{J\subseteq[k]\\\\|J|=\omega}} \det\\!\left( P(\lambda)\_{:,J}^{\mathsf T} P(\mu)\_{:,J} \right). } \\]

This sum has only \\(\binom{k}{\omega}\\) terms. Since \\(k\le\kappa\_{\rm obs}\\), it can be computed in

\\[ f(\kappa\_{\rm obs})\operatorname{poly}(q,\mathcal L) \\]

arithmetic operations, where \\(\mathcal L\\) denotes the input size.

The entries of \\(B^\top B\\) are coefficient pairings of the \\(f\_{I,J}\\), so they can be read off from the coefficients of \\(K(\lambda,\mu)\\). The matrix \\(B^\top B\\) has size \\(2\omega\times2\omega\\).

This gives a genuinely promising route to an FPT certificate:

- the compressed free data have dimension \\(\kappa\_{\rm obs}\\);
- the rank condition (5a) can be encoded using small Gram matrices;
- the spectral condition (5b) can be encoded using a \\(2\omega\\)-dimensional Gram certificate;
- \\(q\\) appears in polynomial-time sums, not in the number of quantified variables.

There are still details to prove, especially the exact treatment of the \\(\omega=0\\) case and the bit complexity of constructing the coefficient Gram matrix. But this is substantially better than introducing one Bezout polynomial for every maximal minor.

### 3.4 Encoding (5a) without enumerating its minors

There is a similarly useful Gram-matrix formulation.

Let

\\[ G_H=H^\mathsf TH, \qquad G_S=H^\mathsf TH+H_A^\mathsf TH_A. \\]

These are \\(k\times k\\) positive semidefinite matrices. Over the reals,

\\[ \operatorname{rank}G_H=\operatorname{rank}H, \\]

and

\\[ \operatorname{rank}G_S = \operatorname{rank} \begin{bmatrix}H\\\H_A\end{bmatrix}. \\]

For a positive semidefinite matrix \\(G\\), let \\(e_j(G)\\) be its \\(j\\)-th elementary symmetric polynomial in the eigenvalues. Then

\\[ e_j(G)>0\iff\operatorname{rank}G\ge j, \\]

and

\\[ e\_{j}(G)=0\quad\text{for }j>\operatorname{rank}G. \\]

Thus, on the rank-\\(\omega\\) stratum, (5a) is equivalent to

\\[ \boxed{ e\_\omega(G_H)>0, \qquad e\_{\omega+1}(G_S)=0. } \\]

Indeed, the first condition gives \\(\operatorname{rank}H\ge\omega\\), and the second gives

\\[ \operatorname{rank} \begin{bmatrix}H\\\H_A\end{bmatrix} \le\omega. \\]

Since the stacked matrix contains \\(H\\), both ranks must equal \\(\omega\\).

These are polynomials in \\(k\times k\\) matrices. Their number and degrees depend on \\(k\\), not on \\(q\\), and their entries are computable by summing over the \\(q\\) rows.

### 3.5 What this means for FPT

The preceding two Gram constructions suggest a stronger theorem than the current report states.

For \\(r,k\ge1\\), one can hope to reduce the problem to real-algebraic feasibility in

\\[ \kappa\_{\rm obs}+2\omega \\]

variables, with a number and degree of defining polynomials bounded by a function of \\(\kappa\_{\rm obs}\\). The coefficients can be computed in polynomial time in the original input size, even if the number of fixed rows \\(q-r\\) grows.

If the coefficient-size and arithmetic-complexity details work out, standard fixed-dimensional real-algebraic algorithms then give

\\[ \boxed{ \text{fixed }\kappa\_{\rm obs} \quad\Longrightarrow\quad q1\in\mathrm{FPT}. } \\]

This is a promising proof programme, not yet a theorem. In particular, the FPT claim should be based on the compressed Gram certificate, not on the original \\(s\\)-polynomial Bezout expansion.

## 4. Route C, fixed \\(q\\): what is valid and what is missing?

The fixed-\\(q\\) sketch is plausible, but not yet a polynomial-time theorem

There is a valuable reduction of the spectral condition to fixed-dimensional data. It does not, by itself, eliminate the free observer rows.

### 4.1 The useful \\(Z,U\\) reformulation

For any feasible \\(H,H_A\\), (5a) gives a matrix \\(Z\in\mathbb R^{q\times q}\\) such that

\\[ H_A=ZH. \\]

Let

\\[ U=\operatorname{im}H\subseteq\mathbb R^q, \qquad \dim U=\omega. \\]

Then

\\[ P(\lambda)=(\lambda I-Z)H. \\]

Because \\(H:\mathbb C^k\to U\_\mathbb C\\) is surjective,

\\[ \operatorname{rank}P(\lambda) = \operatorname{rank}\left((\lambda I-Z)|\_{U\_\mathbb C}\right). \\]

Consequently,

\\[ \boxed{ (5b)\iff U\_\mathbb C\cap\ker(\lambda I-Z)=\\{0\\} \quad\forall\lambda\in\sigma(Z). } \\]

Equivalently, \\(U\_\mathbb C\\) contains no eigenvector of \\(Z\\).

This is important: once \\(Z\\) and \\(U\\) are known, (5b) no longer depends on the individual columns of \\(H\\).

If \\(q\\) is fixed, one can represent \\(U\\) by a \\(q\times\omega\\) basis matrix \\(B\\), and the spectral condition becomes a fixed-size pencil condition on

\\[ (\lambda I-Z)B. \\]

Its maximal minors have degree at most \\(\omega\\), and there are only \\(\binom q\omega\\) of them. A bounded-size Bezout certificate can express their gcd being one. Thus the spectral part really can be expressed using a number of variables depending only on \\(q\\).

### 4.2 The missing part: eliminating \\(R\\) while retaining full rank

For fixed \\(Z\\) and \\(U\\), choose a matrix \\(D\\) with

\\[ \ker D=U. \\]

The constraints on the unknown \\(R\\) include

\\[ D LN=0, \qquad LAN=ZLN. \\]

Together with the fixed-row constraints, these are linear equations in the entries of \\(R\\).

So far, so good.

But we also need

\\[ \operatorname{rank}(LN)=\omega. \\]

The first equation only ensures

\\[ \operatorname{im}(LN)\subseteq U, \\]

which gives rank at most \\(\omega\\). We need to ensure that the map actually spans all of \\(U\\).

For a fixed \\(Z,U\\), the linear equations define an affine space

\\[ R=R_0+\sum\_{j=1}^{d}t_jV_j. \\]

The rank condition is equivalent to saying that at least one \\(\omega\times\omega\\) minor of \\(LN\\), viewed as a polynomial in \\(t_1,\ldots,t_d\\), is not identically zero.

Since \\(\omega\le q-1\\) is fixed, each such polynomial has bounded degree. There are polynomially many candidate minors when \\(q\\) is fixed. For fixed \\(Z,U\\), this can be checked by expanding the bounded-degree polynomials in the affine parameters.

The unresolved issue is that \\(Z,U\\) themselves are existentially quantified. The affine solution space for \\(R\\) depends on them. A direct Gaussian elimination performed after choosing \\(Z,U\\) does not automatically produce a polynomial-size quantifier-free condition in \\(Z,U\\).

In particular, the rank of the coefficient matrix of the linear system for \\(R\\) may change on special algebraic subsets of the \\((Z,U)\\)-space. A complete proof must handle those exceptional parameter strata, not just the generic one.

### 4.3 The missing lemma

I would formulate the exact missing result this way.

> Parametric linear-elimination lemma needed for fixed \\(q\\).\
> Given a linear system\
> \\[\
> M(z)y=b(z)\
> \\]\
> whose coefficients are polynomial in a fixed number of real parameters \\(z\\), and a bounded-degree polynomial rank condition on an affine-linear image of \\(y\\), construct in polynomial time a real-algebraic formula in \\(z\\), of size polynomial in the original input, that is equivalent to the existence of \\(y\\) satisfying both conditions.

Here the number of parameters \\(z\\) would depend only on \\(q\\), but the dimension of \\(y\\) grows with the input.

If this lemma holds with the needed bit-complexity bounds, the fixed-\\(q\\) polynomial route may work. But ordinary linear elimination does not prove it automatically.

### 4.4 Where an exponential dependence could enter

There are three possible sources:

1. Rank strata of \\(M(z)\\). A naive approach enumerates pivot minors, and the number of choices can be exponential in the matrix dimensions.
2. The rank-\\(\omega\\) condition. Although each minor has bounded degree, the affine solution space depends on \\(z\\). One must express non-identical vanishing uniformly across all parameter strata.
3. Elimination complexity. A general quantifier-elimination procedure on all entries of \\(R\\) has a number of variables growing with \\(n\\), so its complexity is not polynomial merely because \\(q\\) is fixed.

The Gram-matrix idea from the fixed-\\(\kappa\_{\rm obs}\\) discussion may help with the rank condition, but it does not automatically solve the parametric linear-elimination problem.

My verdict: keep fixed \\(q\\) as an interesting conjectural algorithmic direction, but do not state it as a polynomial-time theorem until the parametric elimination lemma is proved.

## 5. Route B: can the shared factor be forced?

Open; the current obstruction is not a no-go theorem

The strongest conceptual point is that (5b) is a condition on the entire pencil, not on each row separately.

Given

\\[ H_A=ZH, \\]

we have

\\[ P(\lambda)=(\lambda I-Z)H. \\]

The maximal minors are therefore controlled jointly by:

- the eigenspace structure of \\(Z\\);
- the position of \\(U=\operatorname{im}H\\);
- the way \\(H\\) parametrizes \\(U\\).

A common scalar factor in the minors need not arise by making every free row a multiple of that factor.

### 5.1 A better way to think about the scalar factor

Suppose a proposed gadget wants (5b) to hold exactly when a scalar residual \\(f(x)\\) is nonzero.

The target is

\\[ \gcd_I f_I(\lambda;x)=f(x), \\]

where \\(f_I\\) are the \\(\omega\\)-minors of \\(P\\), and \\(f(x)\\) is independent of \\(\lambda\\).

For fixed \\(x\\), this means:

- if \\(f(x)\ne0\\), the gcd is a nonzero constant and (5b) holds;
- if \\(f(x)=0\\), all maximal minors vanish identically in \\(\lambda\\), so (5b) fails.

Thus the gadget must arrange

\\[ f(x)=0 \quad\Longrightarrow\quad \operatorname{rank}P(\lambda;x)<\omega \quad\text{for every }\lambda. \\]

That is a uniform rank-collapse condition over the entire pencil. It is stronger than arranging a rank drop at one selected eigenvalue.

The rowwise common-factor idea is one way to force such a collapse, but it is not necessary in general.

### 5.2 A more promising construction principle

Try to make the residual control the rank of a fixed-dimensional map:

\\[ T(x):U\longrightarrow \mathbb C^q/E \\]

for an appropriate eigenspace or invariant subspace \\(E\\). Arrange that

\\[ \operatorname{rank}T(x)=\omega \iff f(x)\ne0. \\]

Then (5b) could potentially reduce to this rank condition.

This is conceptually more natural than asking every row of \\(H\\) to carry a common scalar factor.

However, one must still ensure that the same \\(A,C,L_0\\) produce the required \\(H,H_A\\). This is where compressed examples often fail to lift.

### 5.3 The exact liftability test

For a proposed compressed pair \\((H,H_A)\\), each free row \\(r_i\\) must satisfy

\\[ (r_iN,\ r_iAN) \\]

equal to the corresponding pair of rows of \\((H,H_A)\\).

Thus, for each free row, the concatenated pair must belong to

\\[ \operatorname{row}[N\ \ AN]. \\]

This is a necessary and sufficient condition for that row pair to have a preimage \\(r_i\\), once \\(N\\) and \\(AN\\) are fixed.

It is the right test to apply to the Route B compressed gadget before trying to construct \\(A,C,L_0\\). A compressed pair may satisfy all the desired determinant and gcd identities but fail this linear liftability condition.

The input-design problem is then to choose \\(N,AN,C,A\\) so that:

1. the desired compressed row pairs lie in \\(\operatorname{row}[N\ AN]\\);
2. \\(N\\) is a basis of \\(\ker[C;CA]\\);
3. the transverse action is nontrivial;
4. the resulting spectral guard has the intended behavior.

That is the full observer realization problem.

## 6. Revised priority recommendation

I would not spend the next major effort trying to force the shared factor in Route B. Nor would I yet claim the fixed-\\(q\\) polynomial algorithm.

My priority order is:

1\. Finish the fixed-\\(\kappa\_{\rm obs}\\) theorem

Highest priority

The Gram compression of (5a) and the \\(2\omega\\)-dimensional Gram certificate for (5b) offer a concrete route to a rigorous FPT theorem even when the number of fixed rows grows. This is the most promising positive result.

2\. Complete one full Route A observer instance

Keep the compressed determinant gate, but insist on a rational \\(A,C,L_0\\) realization and verify all of (5a), (5b), the rank stratum, and the chart restriction exactly. Do not generalize to a reduction before that instance exists.

3\. Keep Route B as a secondary algebraic experiment

Replace the unproved shared-row-factor necessity by the uniform rank-collapse formulation. Search for a residual-controlled map on \\(U\\), and test liftability through \\(\operatorname{row}[N\ AN]\\).

4\. Investigate fixed \\(q\\) only after formalizing parametric elimination

The \\(Z,U\\) reduction is valid and useful. The polynomial-time conclusion needs a separate lemma about parameter-dependent linear systems and rank attainment.

## 7. Suggested revised status table

| Claim                                                        | Reliability verdict                                          | Recommended status |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------ |
| \\(AN=NM+E\\) decomposition                                  | Correct                                                      | P                  |
| (5a) splits into fixed and transverse row incidences         | Correct                                                      | P                  |
| Incidence is not an arbitrary affine hyperplane              | Correct                                                      | P                  |
| Compressed determinant equation                              | Correct only on a nonzero chart for rank exactly 3           | E, qualified       |
| Compressed gate is an observer gate                          | Not yet shown                                                | S                  |
| \\(E=0\\) is incompatible with (5a), (5b) and \\(\omega>0\\) | Correct under the stated invariant-subspace hypotheses       | P                  |
| (5a) equations and (5b) unit-ideal condition                 | Correct                                                      | P                  |
| Every free row must share factor \\(f\\)                     | Not established; too strong generally                        | Remove as theorem  |
| Bezout degree \\((s-1)\omega\\)                              | Needs explicit proof; not enough for FPT as directly encoded | P, incomplete      |
| Fixed-\\(\kappa\_{\rm obs}\\) FPT                            | Promising; Gram compression may complete it                  | S pending proof    |
| Fixed-\\(q\\) polynomial time                                | Not established                                              | S                  |

## 8. Final assessment

The most important correction to the report is that the fixed-\\(\kappa\_{\rm obs}\\) algorithmic route may be stronger than the current Bezout argument suggests. You can potentially compress the entire family of maximal minors into a small Gram matrix using Cauchy–Binet, avoiding both the enumeration of all minors and a separate Bezout polynomial for each one.

The most important correction to the hardness discussion is that the shared-\\(f\\) obstruction should not be treated as a no-go theorem. The right object is the uniform rank-collapse behavior of the pencil, together with the liftability condition imposed by \\([N\ AN]\\).

My recommendation is therefore:

Make Route C the main theorem-development effort, and give Route A one bounded construction attempt in parallel. Route B should remain a targeted exploratory direction, not the main project, until it yields a compressed gadget with a demonstrable lift.

One especially useful next deliverable would be a formal lemma proving the \\(2\omega\\)-dimensional Gram certificate for (5b), including its Cauchy–Binet construction and bit-complexity bound. That would turn the most promising part of Route C from a plausible argument into a theorem candidate.