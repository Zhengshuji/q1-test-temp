# Mathematical and complexity audit of the manuscript

“Complete paper-level proof: DEC, OPT and FIND are fixed-parameter tractable in the rank of AN”

My overall assessment is that this is a substantial improvement in the mathematical architecture of the project. The manuscript now has a coherent route from the original rank constraints to a finite-dimensional semialgebraic decision problem, followed by optimization and exact witness construction.

However, I would distinguish three conclusions:

1. The structural reduction is essentially correct. In particular, the compression identity, the characterization in terms of \\(W\\), the structural bound, and the reduction from \\(k\\) to \\(\ell=\operatorname{rank}(AN)\\) have a sound mathematical foundation.
2. The semialgebraic encoding is promising but needs a more explicit proof. The Bézout certificate is the right idea, and the use of \\(B^{\mathsf T}B\\) is mathematically legitimate. Nevertheless, several dimensional, degree, and coefficient-height details should be made explicit before the complexity theorem is regarded as complete.
3. The bit-complexity and formalisation claims need further qualification. In particular, the real-algebraic sample-point theorem must be connected carefully to the representation and bit length of the output witness. The Lean formalisation should not be presented as formal verification of the complete FPT theorem.

My recommendation is major revision, with a realistic path to a strong theoretical-computer-science or computational-mathematics paper. I would not yet recommend describing every result in the title as a fully established, end-to-end bit-complexity theorem without resolving the points below.

I will examine the arguments in the manuscript in their existing order, then answer the six questions individually.

## 1. The compression reduction: mathematically sound

The first important achievement is that the original feasibility conditions are converted into conditions on a single row space.

Let

\\[ K_0=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \\]

and let \\(N\\) have columns forming a basis of \\(K_0\\). Write

\\[ M=[N\ AN]. \\]

For any matrix \\(Q\\) with \\(n\\) columns, the identity

\\[ \operatorname{rank} \begin{bmatrix} CA\\\C\\\Q \end{bmatrix} = \operatorname{rank} \begin{bmatrix} CA\\\C \end{bmatrix} + \operatorname{rank}(QN) \\]

is correct.

The reason is that restricting the linear map represented by \\(Q\\) to the kernel of the map represented by \\([CA;C]\\) measures exactly the additional rank contributed by adjoining \\(Q\\).

Set

\\[ J=\begin{bmatrix}CA\\\C\end{bmatrix}, \qquad B=LM=[H\ H_A]. \\]

Then the first original equality becomes

\\[ \operatorname{rank}\begin{bmatrix}H_A\\\H\end{bmatrix} =\operatorname{rank}H. \\]

Equivalently,

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H. \tag{1} \\]

The second equality becomes

\\[ \operatorname{rank}(\lambda H-H_A) =\operatorname{rank}H \qquad(\forall\lambda\in\mathbb C). \tag{2} \\]

These are exactly the two conditions needed for the subsequent structural argument.

### 1.1 One improvement to the presentation

I recommend explicitly stating the underlying rank-compression lemma.

Lemma. Let \\(J\\) be a matrix with \\(n\\) columns, and let \\(N\\) be a basis matrix for \\(\ker J\\). Then, for every \\(Q\\) with \\(n\\) columns,

\\[ \operatorname{rank} \begin{bmatrix}J\\\Q\end{bmatrix} = \operatorname{rank}J+\operatorname{rank}(QN). \\]

The proof should be given using the induced map

\\[ \ker J\longrightarrow \operatorname{im}Q, \qquad x\longmapsto Qx. \\]

Its image is precisely the additional rank.

This formulation makes the reduction independent of matrix-coordinate calculations and is also particularly suitable for Lean.

### 1.2 Characterization in terms of \\(W\\)

Let

\\[ W=\operatorname{row}[H\ H_A]. \\]

Define

\\[ \pi_1(h,g)=h,\qquad \pi_2(h,g)=g. \\]

Then (1) says

\\[ \pi_2(W)\subseteq\pi_1(W). \\]

Equation (2) says

\\[ \dim\pi\_\lambda(W)=\dim\pi_1(W) \\]

for every complex \\(\lambda\\), where

\\[ \pi\_\lambda(h,g)=\lambda h-g. \\]

This equivalence is correct.

There is one small but important presentational issue: \\(W\\) is initially a real subspace, whereas the spectral condition quantifies over complex \\(\lambda\\).

The cleanest approach is to introduce the complexification

\\[ W\_{\mathbb C}=W\otimes\_{\mathbb R}\mathbb C \\]

when discussing eigenvalues and complex ranks.

Since a real matrix has the same rank over \\(\mathbb R\\) and \\(\mathbb C\\), this introduces no change in the rank conditions.

Recommendation: explicitly distinguish real row spaces from their complexifications. This will eliminate an avoidable ambiguity later.

## 2. The structural bound: correct, and central to the paper

This is one of the strongest parts of the manuscript.

Let

\\[ \omega=\dim\pi_1(W). \\]

For a feasible \\(W\\), the first condition gives

\\[ \pi_2(W)\subseteq\pi_1(W). \\]

Taking \\(\lambda=0\\) in the second condition gives

\\[ \dim\pi_2(W)=\dim\pi_1(W)=\omega. \\]

Consequently,

\\[ \pi_1(W)=\pi_2(W)=U \\]

for some \\(\omega\\)-dimensional subspace \\(U\\).

Therefore,

\\[ W\subseteq U\times U, \\]

and hence

\\[ \boxed{\dim W\le 2\omega.} \tag{3} \\]

The lower bound is also correct.

Suppose that

\\[ \dim W=\omega>0. \\]

Both coordinate projections

\\[ \pi_1|\_W:W\to U, \qquad \pi_2|\_W:W\to U \\]

are surjective maps between vector spaces of equal dimension. They are therefore isomorphisms.

It follows that \\(W\\) is the graph of an endomorphism

\\[ F:U\to U. \\]

More explicitly,

\\[ W=\\{(u,Fu):u\in U\\}. \\]

Since \\(U\_{\mathbb C}\\) is a nonzero finite-dimensional complex vector space, \\(F\_{\mathbb C}\\) has an eigenvalue \\(\lambda_0\\).

For an associated nonzero eigenvector \\(u\\),

\\[ F\_{\mathbb C}u=\lambda_0u. \\]

Consequently,

\\[ \pi\_{\lambda_0}(u,F\_{\mathbb C}u) = \lambda_0u-F\_{\mathbb C}u=0. \\]

Thus

\\[ \dim\pi\_{\lambda_0}(W\_{\mathbb C})<\omega, \\]

contradicting feasibility.

Therefore,

\\[ \boxed{\omega+1\le\dim W\le2\omega} \qquad(\omega>0). \tag{4} \\]

This argument is valid.

### 2.1 An important improvement: state the structural theorem independently

I would promote this result to a standalone theorem.

Structural Theorem. Let \\(W\subseteq V\times V\\) be a finite-dimensional real subspace satisfying

\\[ \pi_2(W)\subseteq\pi_1(W) \\]

and

\\[ \dim\pi\_\lambda(W)=\dim\pi_1(W) \qquad\text{for every }\lambda\in\mathbb C. \\]

Then either \\(W=\\{0\\}\\), or

\\[ \dim\pi_1(W)+1 \le\dim W \le2\dim\pi_1(W). \\]

This theorem is independent of the original matrices \\(A,C,L_0\\).

That independence is valuable: it makes clear that the dimension bound is a geometric obstruction, not an accidental property of the particular compression.

### 2.2 The zero case

The manuscript correctly identifies the exceptional case:

\\[ \omega=0\implies W=0. \\]

Since

\\[ W_0\subseteq W, \\]

feasibility in this case requires

\\[ W_0=0. \\]

I recommend keeping this case explicit throughout the algorithm. In particular, do not allow formulas involving \\(e\_{\omega+1}\\), \\(\binom{\ell}{\omega}\\), or a positive-dimensional eigenvalue argument to silently assume that \\(\omega=0\\) is covered.

## 3. Reduction from \\(k\\) to \\(\ell=\operatorname{rank}(AN)\\)

This is an important parameter reduction, and I agree with the manuscript's choice of \\(\ell\\) as the principal parameter.

Recall

\\[ S=\operatorname{row}(AN)\subseteq\mathbb R^k, \qquad \dim S=\ell. \\]

For every feasible \\(W\\), we have

\\[ \pi_1(W)=\pi_2(W)=U\subseteq S. \\]

Thus

\\[ W\subseteq S\times S. \\]

Since \\(W_0\subseteq W\\), necessarily

\\[ W_0\subseteq S\times S. \tag{5} \\]

This proves the claimed infeasibility test.

### 3.1 Is the infeasibility test sufficient?

Yes. The argument is particularly simple:

If \\(W\\) is feasible, then

\\[ W_0\subseteq W\subseteq S\times S. \\]

Therefore,

\\[ W_0\subseteq S\times S. \\]

The contrapositive gives

\\[ \boxed{ W_0\not\subseteq S\times S \implies \text{infeasibility at every order}. } \\]

There is no hidden assumption about the number of free rows in this argument.

This is an exact obstruction, not merely a necessary condition for a particular order.

### 3.2 Coordinate reduction

Choose a rational basis of \\(S\\), and extend it to a rational basis of \\(\mathbb Q^k\\).

There is an invertible rational coordinate transformation \\(P\\) such that

\\[ SP=\mathbb Q^\ell\times\\{0\\}^{k-\ell}. \\]

After applying this transformation to both blocks, every feasible pair has the form

\\[ [H\ G] \\]

where \\(H,G\\) have only \\(\ell\\) potentially nonzero columns.

This is mathematically valid.

There is, however, a wording correction that I consider necessary.

The manuscript says:

> row spaces are unchanged by right multiplication by an invertible matrix.

This statement is literally false if row spaces are regarded as subsets of a fixed coordinate space.

In general,

\\[ \operatorname{row}(XP)\ne\operatorname{row}(X). \\]

What is true is

\\[ \operatorname{rank}(XP)=\operatorname{rank}(X), \\]

and, for two matrices \\(X,Y\\) with the same number of columns,

\\[ \operatorname{row}(X)\subseteq\operatorname{row}(Y) \iff \operatorname{row}(XP)\subseteq\operatorname{row}(YP). \\]

Likewise, equality of row spaces is preserved.

Suggested replacement:

"Right multiplication by the same invertible coordinate transformation preserves all ranks, row-space inclusions, row-space equalities, and the pencil rank conditions. In the resulting coordinates, every feasible row is supported on the first \\(\ell\\) coordinates."

This is precise.

### 3.3 The parameter should be \\(\ell\\), not \\(k\\)

I agree with the main conclusion.

The structural argument shows that the relevant projection space is contained in \\(S\\), whose dimension is \\(\ell\\). Therefore, the Grassmannian dimensions and polynomial-system variable counts should be governed by \\(\ell\\).

The parameter \\(k\\) measures the dimension of the original compressed state space, but it can contain directions that no feasible row space can use.

The distinction is important:

\\[ k=\dim K_0, \qquad \ell=\operatorname{rank}(AN)\le k. \\]

The algorithm should first perform the exact coordinate compression and only then construct the polynomial system.

One qualification: the complexity analysis must consistently use the reduced \\(\ell\\)-column matrices. It is not enough to establish the dimension reduction in the mathematical discussion and then reintroduce \\(k\\) into the implementation or coefficient computation.

I discuss an inconsistency of exactly this kind in Section 5.

## 4. The encoding: the right idea, but the proof needs tightening

This is the most technically delicate part of the paper.

The encoding is designed to express two properties:

1. The projection \\(H\\) has rank exactly \\(\omega\\), and the second projection is contained in its row space.
2. The pencil \\(\lambda H-G\\) has rank \\(\omega\\) for every complex \\(\lambda\\).

The first property is encoded using Gram matrices. The second uses a Bézout certificate.

I believe this is the right general strategy.

### 4.1 The Grassmannian parameterization

Let

\\[ V=T\cap(S\times S). \\]

Assuming the necessary preliminary test \\(W_0\subseteq V\\), define

\\[ m'=\dim V-s_0. \\]

Every admissible candidate \\(W\\) has

\\[ W_0\subseteq W\subseteq V. \\]

Therefore \\(W/W_0\\) is a \\(t\\)-dimensional subspace of \\(V/W_0\\), where

\\[ t=\dim(W/W_0). \\]

The parameter space is consequently

\\[ \operatorname{Gr}(t,m'). \\]

The standard Grassmannian charts are indexed by the choices of \\(t\\) pivot coordinates. Their number is

\\[ \binom{m'}{t}. \\]

Summing over all \\(t\\),

\\[ \sum\_{t=0}^{m'}\binom{m'}t=2^{m'}\le 4^\ell. \\]

This is correct.

The chart coordinates have dimension

\\[ t(m'-t). \\]

Thus

\\[ N\_{\mathrm{var}} =t(m'-t)+2\omega \le \ell^2+2\ell. \\]

This bound is also correct.

One detail to make explicit: the chosen chart must parameterize subspaces in the quotient \\(V/W_0\\), not arbitrary \\(t\\)-dimensional subspaces of \\(V\\). The latter would incorrectly allow candidates that do not contain \\(W_0\\).

The affine basis construction should be described as follows:

- Fix a rational basis of \\(W_0\\).
- Fix a rational complement of \\(W_0\\) in \\(V\\).
- Use a Grassmannian chart in the quotient coordinates.
- Lift the chart basis back to \\(V\\).
- Adjoin the fixed basis of \\(W_0\\).

Then the resulting matrix \\(Z(Y)\\) has

\\[ \nu=s_0+t \\]

rows, and its entries are affine polynomials in \\(Y\\).

### 4.2 The Gram-matrix conditions

The proposed conditions are

\\[ e\_\omega(HH^{\mathsf T})>0 \\]

and

\\[ e\_{\omega+1} \left( \begin{bmatrix}H\\\G\end{bmatrix} \begin{bmatrix}H\\\G\end{bmatrix}^{\mathsf T} \right)=0. \\]

Here \\(e_j(X)\\) must be defined explicitly as the \\(j\\)-th elementary symmetric polynomial of the eigenvalues of the real symmetric matrix \\(X\\), equivalently the sum of its principal minors of order \\(j\\).

For a positive semidefinite Gram matrix,

\\[ e_j(XX^{\mathsf T})>0 \iff \operatorname{rank}X\ge j. \\]

Similarly,

\\[ e_j(XX^{\mathsf T})=0 \iff \operatorname{rank}X\<j. \\]

Consequently, the first condition gives

\\[ \operatorname{rank}H\ge\omega, \\]

and the second gives

\\[ \operatorname{rank} \begin{bmatrix}H\\\G\end{bmatrix} \le\omega. \\]

Combining these with the fact that \\(H\\) is a block of the stacked matrix gives

\\[ \operatorname{rank}H = \operatorname{rank} \begin{bmatrix}H\\\G\end{bmatrix} =\omega. \\]

Thus

\\[ \operatorname{row}G\subseteq\operatorname{row}H. \\]

The encoding is correct.

I recommend adding a short lemma explaining the Gram-matrix characterization rather than assuming readers will immediately recognize the role of \\(e_j\\).

Also, define the convention for \\(e_j\\) when \\(j\\) exceeds the matrix dimension. This matters in boundary cases.

### 4.3 The Bézout certificate

Let

\\[ P_Y(\lambda)=\lambda H(Y)-G(Y). \\]

The matrix has \\(\nu\\) rows and \\(\ell\\) columns.

Since the desired rank is \\(\omega\\), consider all maximal minors

\\[ f\_{I,J}(\lambda;Y) = \det P_Y(\lambda)\_{I,J}, \\]

where

\\[ |I|=|J|=\omega. \\]

The condition

\\[ \operatorname{rank}P_Y(\lambda)=\omega \qquad\forall\lambda\in\mathbb C \\]

is equivalent to saying that these polynomials have no common complex zero.

For a finite family of univariate polynomials over \\(\mathbb C\\), this is equivalent to their greatest common divisor being constant.

Since the polynomials have real coefficients, the equivalent Bézout identity can also be taken over \\(\mathbb R[\lambda]\\).

Thus the desired condition is equivalent to the existence of polynomials \\(g\_{I,J}\\) such that

\\[ \sum\_{I,J}g\_{I,J}(\lambda)f\_{I,J}(\lambda;Y)=1. \tag{6} \\]

The degree bound on the multipliers is the next issue.

Every \\(f\_{I,J}\\) has degree at most \\(\omega\\). Because

\\[ \operatorname{rank}H=\omega, \\]

at least one maximal minor has degree exactly \\(\omega\\).

The univariate effective Bézout bound permits a representation with

\\[ \deg g\_{I,J}<\omega. \\]

Therefore write

\\[ g\_{I,J}(\lambda) = \sum\_{j=0}^{\omega-1}x\_{I,J,j}\lambda^j. \\]

Equation (6) becomes a linear combination of the coefficient vectors of

\\[ f\_{I,J},\lambda f\_{I,J},\ldots, \lambda^{\omega-1}f\_{I,J}. \\]

Each such polynomial has degree at most

\\[ 2\omega-1. \\]

Its coefficient vector therefore has exactly \\(2\omega\\) coordinates.

This verifies the central degree bookkeeping.

### 4.4 The \\(B^{\mathsf T}B\\) trick

The manuscript's construction of \\(B\\) is mathematically sound, provided its orientation is specified.

Let \\(B\\) be the matrix whose rows are the coefficient vectors of all the polynomials

\\[ \lambda^j f\_{I,J}, \qquad 0\le j<\omega. \\]

Then

\\[ B\in\mathbb R^{s\times 2\omega}, \\]

where

\\[ s=\omega\binom{\nu}{\omega}\binom{\ell}{\omega}. \\]

The Bézout condition is

\\[ e_0\in\operatorname{row}(B), \\]

where now \\(e_0=(1,0,\ldots,0)^{\mathsf T}\in\mathbb R^{2\omega}\\).

For a real matrix,

\\[ \operatorname{range}(B^{\mathsf T}B) = \operatorname{range}(B^{\mathsf T}). \\]

Hence

\\[ e_0\in\operatorname{row}(B) \iff \exists x\in\mathbb R^{2\omega}: B^{\mathsf T}Bx=e_0. \\]

This is correct.

Encoding principle validated

The auxiliary variable \\(x\\) really does have dimension \\(2\omega\\), independently of the number of maximal minors.

This is a valuable compression of the certificate.

There is one notational problem: the manuscript uses \\(e\_\omega\\) for elementary symmetric polynomials and \\(e_0\\) for a coordinate vector. These are different mathematical objects. I would use distinct notation, for example

\\[ \sigma_j(X) \\]

for the Gram-matrix elementary symmetric polynomial and

\\[ \mathbf e_1 \\]

for the first standard basis vector.

That small change will make the encoding much easier to read.

## 5. An important complexity inconsistency: \\(k\\) versus \\(\ell\\)

This is the correction I would prioritize before submitting the manuscript.

The paper correctly reduces the matrices to \\(\ell\\) columns, but the Cauchy–Binet discussion then states

\\[ \binom{k}{\omega}\le 2^k. \\]

After the coordinate reduction, the corresponding number of column subsets should be

\\[ \boxed{\binom{\ell}{\omega}\le2^\ell.} \\]

The distinction is essential.

The Cauchy–Binet identity gives

\\[ \sum\_{\substack{J\subseteq[\ell]\\\\|J|=\omega}} \det\left( P\_{:,J}(\lambda)^{\mathsf T} P\_{:,J}(\mu) \right) = \sum\_{\substack{I\subseteq[\nu]\\\\|I|=\omega}} \sum\_{\substack{J\subseteq[\ell]\\\\|J|=\omega}} f\_{I,J}(\lambda)f\_{I,J}(\mu). \tag{7} \\]

This is precisely the Gram kernel needed to construct \\(B^{\mathsf T}B\\).

The important point is that the sum over row subsets \\(I\\) is eliminated through Cauchy–Binet, while the remaining sum is over column subsets of the reduced matrix.

Thus the relevant combinatorial factor is

\\[ \binom{\ell}{\omega}, \\]

not \\(\binom{k}{\omega}\\).

If the implementation actually constructs the reduced matrices, the corrected estimate is

\\[ 2^\ell\operatorname{poly}(\omega,\ell) \\]

rather than \\(2^k\operatorname{poly}(\omega,\ell)\\).

This is compatible with the advertised parameter.

### 5.1 Why this correction matters

Suppose \\(k\\) is very large but

\\[ \ell=\operatorname{rank}(AN) \\]

is small.

An algorithm with a \\(2^k\\) factor is not an FPT algorithm in \\(\ell\\), even though the polynomial-system dimension is bounded in terms of \\(\ell\\).

The fact that the original input explicitly contains \\(n\times k\\) matrices does not make \\(2^k\\) polynomial in the input size.

Therefore, the proof must consistently eliminate \\(k\\) from all exponential factors.

My recommendation is to rewrite the paragraph containing equations (97)–(100) and explicitly state:

- The coordinate-reduced pencil has \\(\ell\\) columns.
- Cauchy–Binet sums over \\(\binom{\ell}{\omega}\\) column subsets.
- No enumeration of the \\(\binom{\nu}{\omega}\\) row subsets is required.
- The remaining construction is singly exponential in \\(\ell\\), not in \\(k\\).

This is a repair of the presentation and potentially of the implementation, not a failure of the underlying mathematical idea.

### 5.2 Polynomial coefficient height

The proposed estimate

\\[ \tau\_{\mathrm{cert}} \le \operatorname{poly}(\mathcal L) + O(\omega\log(\omega+2)) \\]

is plausible, but the manuscript does not yet establish it sufficiently.

There are several contributions:

1. The rational basis of \\(S\\).
2. The rational basis of \\(V/W_0\\).
3. The affine chart matrices.
4. The coefficients of the maximal minors.
5. The sums and products arising in \\(B^{\mathsf T}B\\).

The first three involve rational linear algebra. Their bit heights should be bounded polynomially in the original input length, provided the bases are computed using exact rational elimination with controlled normalization.

The maximal minors involve determinants of order \\(\omega\\). Standard determinant height estimates introduce a contribution of order

\\[ O(\omega(\tau+\log\omega)) \\]

when the entries have height bounded by \\(\tau\\).

The Cauchy–Binet summation introduces a logarithmic dependence on the number of summands, which is at most \\(O(\ell)\\).

However, the coefficient height of \\(B^{\mathsf T}B\\) must be estimated directly. It is not enough to estimate one minor and then assert the same bound for the entire Gram matrix.

I suggest stating an intermediate lemma:

Coefficient-height lemma. After rational preprocessing and coordinate compression, every coefficient of every polynomial defining the semialgebraic system has bit height bounded by

\\[ \operatorname{poly}(\mathcal L) + \operatorname{poly}(\ell,\omega), \\]

with an explicit bound obtained from rational determinant and summation estimates.

Then derive the particular bound needed by the real-algebraic algorithm.

I would not retain the exact \\(O(\omega\log\omega)\\) term until this derivation has been written out. It may be correct under a suitable normalization, but it is not established by the current text.

## 6. Decision complexity: the FPT calculation

Assuming the corrected encoding and coefficient-height estimates, the main parameter calculation is good.

The number of variables satisfies

\\[ N\_{\mathrm{var}}\le\ell^2+2\ell. \\]

The number of polynomials is

\\[ S\_{\mathrm{poly}}=2+2\omega, \\]

and their degrees are bounded by

\\[ D\le2\omega+2. \\]

Since \\(\omega\le\ell\\),

\\[ S\_{\mathrm{poly}}D=O((\ell+1)^2). \\]

The real-algebraic decision bound therefore contributes

\\[ (S\_{\mathrm{poly}}D)^{O(N\_{\mathrm{var}})} = \exp\bigl(O(\ell^2\log(\ell+2))\bigr). \\]

The cited Basu–Pollack–Roy work is relevant: it establishes a sign-condition sample-point algorithm with arithmetic complexity \\(s^{k'+1}d^{O(k)}\\) in its general formulation, with the full-dimensional case giving the familiar \\(s^{k+1}d^{O(k)}\\) bound.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车+1



In the present setting, the number of charts contributes

\\[ 2^{m'}\le4^\ell. \\]

The number of pairs \\((t,\omega)\\) is polynomial in \\(\ell\\).

Thus, provided that the coefficient sizes and formula construction are controlled as claimed,

\\[ \boxed{ T\_{\mathrm{DEC}} = \exp\bigl(O(\ell^2\log(\ell+2))\bigr) \operatorname{poly}(\mathcal L). } \tag{8} \\]

I agree with this final asymptotic form.

### 6.1 An important distinction about formula length

The manuscript correctly distinguishes

\\[ \tau\_{\mathrm{cert}} \\]

from

\\[ L\_{\mathrm{formula}}. \\]

This distinction should remain.

The coefficient height controls the bit complexity of arithmetic involving the input coefficients. The expanded formula length controls the cost of actually constructing and representing the polynomial system.

A concise polynomial-system description does not automatically imply that its expanded representation can be generated in polynomial time.

The Cauchy–Binet representation is useful precisely because it provides a compact way to compute the relevant Gram coefficients without enumerating all row minors.

I would strengthen the proof by giving an explicit preprocessing lemma:

Preprocessing Lemma. Given a rational instance, the reduced coordinates, Grassmannian chart equations, and the polynomial coefficient data needed by the decision algorithm can be constructed within

\\[ \exp(O(\ell\log(\ell+2))) \operatorname{poly}(\mathcal L) \\]

bit operations.

The precise exponent can be adjusted to the actual implementation.

This would make the transition from mathematical encoding to algorithmic complexity much more convincing.

## 7. OPT: the minimum-order argument

This part is correct under the stated row-slot model.

Let

\\[ t=\dim(W/W_0). \\]

A space \\(W\\) with this value of \\(t\\) can be realized using exactly \\(t\\) additional rows.

If fewer than \\(t\\) rows are available, it cannot be realized.

If at least \\(t\\) rows are available, append zero rows.

Therefore,

\\[ \mathrm{DEC}(r_0+t) \\]

is monotone nondecreasing in \\(t\\).

Furthermore, every feasible \\(W\\) satisfies

\\[ \dim W\le2\omega\le2\ell. \\]

Since

\\[ \dim(W/W_0)=\dim W-s_0, \\]

we obtain

\\[ t\le2\ell. \\]

Consequently,

\\[ \boxed{ q\_{\min}=r_0+t\_{\min}, \qquad 0\le t\_{\min}\le2\ell. } \\]

Binary search is therefore valid.

If DEC at \\(r_0+2\ell\\) is infeasible, saturation implies that no feasible \\(W\\) exists at any order.

### 7.1 One improvement: use saturation explicitly

Define

\\[ d=\dim T, \qquad m=d-s_0. \\]

The actual saturation threshold is \\(m\\), not necessarily \\(2\ell\\).

Indeed,

\\[ m\le \dim(S\times S)\le2\ell. \\]

The stronger statement is

\\[ \mathrm{DEC}(r_0+t) = \mathrm{DEC}(r_0+m) \qquad(t\ge m). \\]

Then use \\(2\ell\\) only as a uniform parameter-dependent upper bound.

This gives a cleaner explanation:

- \\(m\\) is the instance-specific saturation threshold.
- \\(2\ell\\) is the uniform upper bound needed for the FPT algorithm.

### 7.2 Binary-search complexity

The number of decision calls is

\\[ O(\log(\ell+2)). \\]

Therefore,

\\[ T\_{\mathrm{OPT}} = \exp\bigl(O(\ell^2\log(\ell+2))\bigr) \operatorname{poly}(\mathcal L). \\]

This conclusion follows directly from DEC.

I see no mathematical gap in this part.

## 8. FIND: witness construction and the algebraic output

The construction argument is conceptually correct.

Suppose the semialgebraic feasibility system has a real solution

\\[ (Y^\*,x^\*). \\]

The resulting chart basis determines \\(W\\).

Since

\\[ W_0\subseteq W\subseteq T, \\]

choose a rational linear section

\\[ \sigma:T\to\mathbb Q^{1\times n} \\]

satisfying

\\[ \sigma(w)M=w. \\]

Take a basis

\\[ w_1,\ldots,w_t \\]

of a complement of \\(W_0\\) in \\(W\\).

Set

\\[ R= \begin{bmatrix} \sigma(w_1)\\\ \vdots\\\ \sigma(w_t) \end{bmatrix}. \\]

Then

\\[ \operatorname{row}(L_0M;RM)=W. \\]

Thus the resulting matrix \\(L=[L_0;R]\\) is feasible.

The construction of a rational section is justified because the linear map

\\[ \mathbb Q^{1\times n}\longrightarrow T, \qquad u\longmapsto uM \\]

is surjective.

A right inverse can be computed by rational Gaussian elimination.

### 8.1 Is the witness necessarily rational?

No.

The semialgebraic system can have real solutions without having rational solutions.

Therefore the appropriate output guarantee is an exact real-algebraic witness, not necessarily a rational one.

This distinction is important and the manuscript correctly acknowledges it.

### 8.2 The bit-complexity claim needs a more careful theorem citation

The manuscript currently gives

\\[ L\_{\mathrm{out}} \le (\tau\_{\mathrm{cert}}+\log S\_{\mathrm{poly}}) D^{O(N)}. \tag{9} \\]

This is the right general shape of a real-algebraic output-size estimate, but I would not cite it as an automatic consequence of the arithmetic-operation bound alone.

There are three distinct statements:

1. The algorithm performs a bounded number of arithmetic operations.
2. The algebraic sample points have bounded algebraic degree.
3. Their exact representations have bounded coefficient bit lengths.

These are related, but they are not interchangeable.

In particular, an arithmetic-complexity theorem over a real closed field does not, by itself, provide the precise Turing bit complexity of the output.

I recommend introducing a separate output-representation lemma.

For example, use a standard univariate representation of the algebraic sample point:

\\[ P(\theta)=0, \qquad Y_i=\frac{Q_i(\theta)}{Q_0(\theta)}. \\]

Then establish:

- A bound on \\(\deg P\\).
- A bound on the coefficient heights of \\(P,Q_i\\).
- A bound on the number of bits needed to encode the representation.
- A bound on the cost of recovering the witness rows.

The exact representation theorem should be cited separately from the arithmetic sign-condition theorem.

The relevant BPR reference is:

S. Basu, R. Pollack and M.-F. Roy, On Computing a Set of Points Meeting Every Cell Defined by a Family of Polynomials on a Variety, Journal of Complexity 13 (1997), 28–37.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车+1



It supports the sample-point algorithm and its arithmetic complexity. It should not be used as the sole justification for every bit-size assertion in (9).

### 8.3 A safer presentation of FIND

I recommend stating two separate results.

Arithmetic construction theorem

The witness can be constructed using

\\[ \exp(O(\ell^2\log(\ell+2))) \\]

arithmetic operations in the relevant exact coefficient model.

Bit-complexity construction theorem

Under the specified rational input encoding and a specified algebraic-number representation, the output witness has a bounded representation length and can be computed within

\\[ \exp(O(\ell^2\log(\ell+2))) \operatorname{poly}(\mathcal L) + \operatorname{poly}(L\_{\mathrm{out}}). \\]

Only state this second theorem after establishing the representation-size lemma.

This separation will make the result much harder to challenge during peer review.

## 9. Row-slot model versus reduced order

My answer to Question 2 is straightforward:

Yes. The manuscript can legitimately establish an FPT theorem for the row-slot problem without proving the reduced-order problem.

There is no general mathematical requirement that every paper solve every related formulation.

However, the scope must be stated prominently, not hidden in a technical remark.

The distinction is substantial.

Your model defines the order through the number of rows of \\(L\\):

\\[ q=\text{number of rows of }L. \\]

It allows:

- Redundant rows.
- Zero rows.
- Rows that do not increase the rank of \\([C;L]\\).

The reduced-order model instead measures

\\[ \operatorname{rank} \begin{bmatrix}C\\\L\end{bmatrix} - \operatorname{rank}C. \\]

These are not equivalent.

### 9.1 Why the distinction matters

In the row-slot model, if a feasible witness uses \\(t\\) additional rows, it remains feasible with \\(t+1\\) rows by appending a zero row.

Thus feasibility is monotone in the row count.

This is what makes the minimum-order binary search immediate.

In the reduced-order model, adding zero rows does not increase the order at all. The same monotonicity argument does not establish the same optimization statement.

Likewise, the formula

\\[ q\_{\min}=r_0+t\_{\min} \\]

is specifically a row-slot statement.

### 9.2 Publication recommendation

I would retain the current scope but make it explicit in three places:

1. The abstract.
2. The problem-definition section.
3. The discussion of limitations.

I would also add a short paragraph explaining why the row-slot model is independently meaningful.

For example, it may be relevant when the number of available measurement channels or design slots is itself a resource, irrespective of whether some channels are redundant.

Do not suggest that the result automatically resolves the reduced-order formulation.

A paper with a precisely bounded theorem is stronger than a paper with a broader but ambiguous claim.

## 10. Which parameter should the paper advertise?

You have three candidates:

\\[ k=\dim K_0, \\]

\\[ \ell=\operatorname{rank}(AN), \\]

and the iterated common-projection core \\(S\_\*\\).

My recommendation is:



Primary parameter

\\(\ell=\operatorname{rank}(AN)\\)





Possible refinement

\\(\dim S\_\*\\)



Do not advertise \\(k\\) as the main parameter unless you have a specific reason to retain the unreduced formulation.

### 10.1 Why \\(\ell\\) is the correct headline

The entire geometric argument takes place in

\\[ S\times S, \qquad \dim S=\ell. \\]

In particular:

\\[ \dim W\le2\ell, \\]

\\[ m'\le2\ell, \\]

\\[ N\_{\mathrm{var}}\le\ell^2+2\ell, \\]

and the number of charts is bounded by

\\[ 4^\ell. \\]

Thus \\(\ell\\) controls every principal exponential factor in the algorithm.

This is a strong reason to use it as the parameter.

### 10.2 What about \\(S\_\*\\)?

The iterated construction is potentially interesting:

\\[ T_j=T\cap(S_j\times S_j), \\]

\\[ S\_{j+1}=\pi_1(T_j)\cap\pi_2(T_j). \\]

It is worth investigating because it may reveal additional structure in the admissible row spaces.

However, I would distinguish two possible claims.

Claim A: Structural refinement.

The feasible space \\(W\\) is contained in

\\[ S\_\*\times S\_\*. \\]

If this follows from the iteration and the relevant inclusions, it gives a legitimate refined dimension bound.

Claim B: Algorithmic improvement.

The entire algorithm can be reformulated using \\(\dim S\_\*\\) instead of \\(\ell\\), including:

- The preliminary containment test.
- The Grassmannian parameterization.
- The polynomial certificate.
- The coefficient-height bounds.
- The witness reconstruction.

Claim A does not automatically imply Claim B.

In particular, the fact that random experiments do not show significant shrinking does not establish that the refinement is useless. Nor does it establish that the refined parameter is theoretically superior.

### 10.3 My recommendation

Keep the main theorem in terms of \\(\ell\\).

Include \\(S\_\*\\) in a discussion of possible refinements only after proving its containment property and showing how the actual encoding changes.

I would not complicate the present main theorem with an unproved refinement.

A clean theorem of the form

\\[ \boxed{ \mathrm{DEC},\mathrm{OPT},\mathrm{FIND} \text{ are FPT parameterized by } \operatorname{rank}(AN) } \\]

is already a substantial result.

## 11. The two Lean formalisation obstructions

The two obstacles you identify are manageable. Neither requires a fundamentally new mathematical development.

### 11.1 Obstruction (a): dimension of a product of submodules

You need

\\[ \dim(U_1\times U_2) = \dim U_1+\dim U_2. \\]

I would not start by trying to prove a specialized theorem about submodules.

Instead, use the existing finite-dimensional product theorem.

Mathlib has a theorem for the finrank of a product of finite-dimensional modules; the older documentation exposes it as `finite_dimensional.finrank_prod`. The current Mathlib documentation also provides the general finite-dimensional framework.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://leanprover-community.github.io\&sz=32)

mathlib3 docs+1



The mathematical proof is immediate from a linear equivalence:

\\[ \Phi: U_1\times U_2 \longrightarrow U_1\times U_2, \\]

where the left-hand side is regarded as a product of submodules and the right-hand side as the product of their underlying types.

More concretely, if the ambient spaces are \\(V_1,V_2\\), construct

\\[ \Phi: \\{(x,y)\in V_1\times V_2: x\in U_1,\ y\in U_2\\} \simeq U_1\times U_2 \\]

by

\\[ (x,y)\longmapsto (\langle x,h_x\rangle,\langle y,h_y\rangle). \\]

The inverse simply forgets the subtype proofs.

Then apply the product finrank theorem.

My preferred Lean strategy:

1. Define the product submodule.
2. Establish the equivalence with the product of the two underlying submodules.
3. Apply `Module.finrank` preservation under linear equivalence.
4. Use the existing product finrank theorem.

This is cleaner than a bespoke dimension argument.

One caution: theorem names and namespaces differ between Mathlib versions. The linked documentation establishes that the mathematical result exists, but you should inspect the exact API in the Mathlib revision used by your 9116-job build.

### 11.2 Obstruction (b): the graph/eigenvalue argument

This is also manageable, and I would formalize it in three independent lemmas.

Lemma 1: Both projections are isomorphisms.

Suppose

\\[ W\subseteq U\times U \\]

and

\\[ \dim W=\dim U. \\]

If both coordinate projections are surjective, then they are isomorphisms.

In Lean, use the finite-dimensional linear-map rank theorem, or derive injectivity from equality of dimensions.

Lemma 2: Construct the graph representation.

Let

\\[ \pi_1|\_W:W\simeq U \\]

be the first projection.

Define

\\[ F= \pi_2|\_W\circ(\pi_1|\_W)^{-1}. \\]

Then

\\[ W=\\{(u,F(u)):u\in U\\}. \\]

I would construct this explicitly rather than search for a specialized graph-submodule theorem.

The graph is simply the range of the linear map

\\[ u\longmapsto(u,F(u)). \\]

This map is injective because its first coordinate is \\(u\\).

Lemma 3: An endomorphism of a nonzero finite-dimensional complex vector space has an eigenvalue.

The mathematical proof is the usual characteristic-polynomial argument:

\\[ \chi_F(\lambda)=\det(\lambda I-F). \\]

Since the space has positive dimension, \\(\chi_F\\) is nonconstant.

Because \\(\mathbb C\\) is algebraically closed, it has a root \\(\lambda_0\\).

Therefore,

\\[ \ker(\lambda_0 I-F)\ne\\{0\\}. \\]

This is exactly the contradiction required.

Mathlib already has an eigenvalue and eigenspace development. In particular, the current documentation contains `LinearAlgebra.Eigenspace.Basic` and results concerning `HasEigenvalue`.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub+1



I would investigate the existing characteristic-polynomial and eigenvalue-existence lemmas before implementing anything new.

The exact theorem name for existence of an eigenvalue should be checked against your pinned Mathlib version; I would not hard-code an API name based only on documentation from another revision.

### 11.3 A better formalisation strategy

I strongly recommend separating the abstract mathematical result from the matrix-specific application.

Formalize:

\\[ \text{Abstract spectral projection theorem} \\]

over a finite-dimensional complex vector space.

Then instantiate it with the complexification of the real row space.

This gives a reusable theorem:

> A subspace of \\(U\times U\\) whose two coordinate projections are surjective and whose pencil projections have constant dimension cannot have dimension equal to \\(\dim U\\), provided \\(U\ne0\\).

The benefit is that the Lean development no longer needs to know anything about \\(A,C,N,M\\) or the original compression.

That is a much better formalisation boundary.

## 12. Assessment of the Lean formalisation status

The reported 9116-job successful build is encouraging.

The formalised components are also well chosen:

- Abstract compression identity.
- Rank additivity and subspace inclusion.
- Row-space/rank correspondence.
- Matrix row-space bridge.
- Pencil interface.
- The zero-spectral-parameter rank condition.

These are foundational lemmas, not merely implementation details.

However, the paper must be precise about what has and has not been formally verified.

The following results remain unformalised:

1. The upper structural bound.
2. The strict lower structural bound.
3. The minimum-order theorem.
4. The semialgebraic encoding.
5. The Bézout certificate.
6. The decision-complexity theorem.
7. The algebraic witness construction and bit-complexity estimates.

Therefore, I would describe the formalisation as:

A substantial Lean formalisation of the algebraic and linear-algebraic reduction, with the central structural dimension theorem and algorithmic complexity analysis remaining outside the formalised development.

That is a meaningful achievement.

I would not describe the entire FPT result as Lean-verified.

### 12.1 What should be formalised next?

My suggested order is:

| Priority | Result                     | Reason                                         |
| -------- | -------------------------- | ---------------------------------------------- |
| 1        | Product dimension lemma    | Removes an immediate structural obstruction    |
| 2        | Graph representation lemma | Needed for the lower dimension bound           |
| 3        | Eigenvalue obstruction     | Completes the structural theorem               |
| 4        | Full structural bound      | Establishes the \\(2\ell\\) dimension cap      |
| 5        | Minimum-order theorem      | Formalises the optimization consequence        |
| 6        | Encoding equivalence       | More technically demanding                     |
| 7        | Complexity analysis        | Requires substantial additional infrastructure |

The most valuable immediate milestone is to complete the structural theorem.

It is the mathematical bridge between the original problem and the FPT algorithm.

# 13. Answers to the six questions

For clarity, here are my direct answers.

| Question                              | Assessment                                                | Recommendation                                                         |
| ------------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------- |
| 1. Is the paper proof acceptable?     | Mostly, but some details need correction                  | Retain the structural argument; clarify coordinates and certificate    |
| 2. Is row-slot scope sufficient?      | Yes                                                       | State the distinction prominently                                      |
| 3. Is the bit model correct?          | Not yet fully established                                 | Separate arithmetic complexity, algebraic degree and output bit length |
| 4. Is the Bézout encoding correct?    | Yes, subject to explicit degree and dimension bookkeeping | Keep \\(B^{\mathsf T}B\\), correct the column count                    |
| 5. Which parameter?                   | \\(\ell\\)                                                | Use \\(S\_\*\\) only as a proved refinement                            |
| 6. Can Lean obstructions be overcome? | Yes                                                       | Use product equivalences and the existing eigenvalue development       |

# 14. Recommended revisions before submission

I would organize the remaining work into four groups.

Priority A — Mathematical corrections

Essential

1. Correct the statement about row spaces under invertible coordinate transformations.
2. Explicitly distinguish real spaces and their complexifications.
3. State the Grassmannian parameterization in the quotient \\(V/W_0\\).
4. Give the effective Bézout degree lemma.
5. Specify the dimensions and orientation of \\(B\\).

   Priority B — Complexity corrections

   Essential
6. Replace \\(\binom{k}{\omega}\\) with \\(\binom{\ell}{\omega}\\) after coordinate compression.
7. Prove the coefficient-height bound for \\(B^{\mathsf T}B\\).
8. Bound the preprocessing and polynomial-system construction costs.
9. Separate Renegar's decision bound from the BPR sample-point construction bound.
10. Establish the algebraic output representation and its bit length.

    Priority C — Formalisation

    Important
11. Complete the product-dimension lemma.
12. Formalize the graph representation.
13. Formalize eigenvalue existence and the strict dimension inequality.
14. Complete the structural theorem.
15. Formalize the minimum-order consequence.

    Priority D — Presentation

    Recommended
16. Make the row-slot model explicit in the abstract.
17. Promote the structural theorem to an independent result.
18. Separate arithmetic complexity and bit complexity.
19. Present \\(S\_\*\\) as a possible refinement rather than a competing main parameter.
20. Clearly identify what Lean has and has not verified.

## 15. What I would make the main theorem

I recommend consolidating the paper around the following theorem.

Proposed Main Theorem — FPT of row-slot feasibility, minimum order, and witness construction.

Let

\\[ A\in\mathbb Q^{n\times n},\quad C\in\mathbb Q^{p\times n},\quad L_0\in\mathbb Q^{r_0\times n}. \\]

Let \\(N\\) be a rational basis matrix of

\\[ \ker\begin{bmatrix}C\\\CA\end{bmatrix}, \\]

and define

\\[ \ell=\operatorname{rank}(AN). \\]

Under the row-slot model, the following problems admit algorithms with parameter dependence

\\[ f(\ell)=\exp(O(\ell^2\log(\ell+2))): \\]

1. DEC: Determine whether a feasible extension with a prescribed number of rows exists.
2. OPT: Determine the minimum feasible row-slot order, or establish infeasibility.
3. FIND: Construct an exact real-algebraic feasible witness at minimum order whenever one exists.

The intended complexity bound is

\\[ \boxed{ f(\ell)\operatorname{poly}(\mathcal L) } \\]

for decision and optimization, and the corresponding output-sensitive bound for exact witness construction.

This formulation is appropriately ambitious but does not claim a result for the reduced-order problem or guarantee rational witnesses.

The theorem should be stated with the bit-complexity qualifications discussed above.

## 16. Final verdict

# Promising, with essential technical revisions

The mathematical architecture is coherent, and I do not see a fundamental obstruction to the proposed FPT strategy.

What is strongest:

- The compression to \\(W\\).
- The structural dimension bound.
- The reduction to \\(\ell\\).
- The Grassmannian parameterization.
- The Bézout-based constant-rank encoding.
- The monotonicity argument for OPT.

What is not yet sufficiently established:

- Uniform coefficient-height bounds.
- The precise bit complexity of FIND.
- The construction complexity after coordinate compression.
- The formal verification of the central structural theorem.

My most important recommendation is to protect the structural theorem and the Bézout encoding as the central contributions. They are the parts that make the algorithm possible.

Do not spend disproportionate effort expanding the scope to reduced order or pursuing \\(S\_\*\\) before the current complexity proof is airtight.

The next revision should concentrate on making every exponential factor depend exclusively on \\(\ell\\), and on proving the coefficient and output-size estimates rather than merely asserting them.

Once those issues are settled, the paper will have a much stronger claim: not just an experimental observation or an abstract decidability result, but an explicit exact algorithm with a meaningful structural parameter.

My suggested next step: produce a corrected technical appendix containing the effective Bézout lemma, the reduced-coordinate Cauchy–Binet construction, and the coefficient-height proof. These are the most important remaining pieces to audit before treating the FPT theorem as submission-ready.

I can also conduct a second, stricter proof audit of that revised appendix, checking every dimension, polynomial degree, coefficient-height estimate, and complexity exponent.