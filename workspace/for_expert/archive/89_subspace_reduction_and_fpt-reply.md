# Complete audit: the main missing step is the explicit polynomial encoding

The report's central reduction is sound, but its FPT argument needs one bridge made completely explicit: how the two subspace conditions become a quantifier-free polynomial formula with only \\(2\omega\\) auxiliary variables. Once that is written down, the claimed variable and degree bounds can be checked directly. I will also sharpen two conclusions from my previous response: the coefficient-height estimate can be stated more precisely, and the monotonicity of the rank-free problem permits binary search for the minimum order.

## 1. The subspace reduction and structural bound

I confirm that Statements 1–4 and the structural bound are correct for the problem exactly as formulated, where the free rows are arbitrary real row vectors and redundant rows are allowed.

Write

\\[ J=\begin{bmatrix}CA\\\C\end{bmatrix}, \qquad \ker J=\operatorname{im}N. \\]

For any matrix \\(Q\\), the rank-compression identity is

\\[ \operatorname{rank}\begin{bmatrix}J\\\Q\end{bmatrix} =\operatorname{rank}J+\operatorname{rank}(QN). \\]

Taking \\(Q=[LA;L]\\) gives the first reduced condition

\\[ \operatorname{rank}\begin{bmatrix}H_A\\\H\end{bmatrix} =\operatorname{rank}H, \\]

and taking \\(Q=\lambda L-LA\\) gives the second:

\\[ \operatorname{rank}(\lambda H-H_A)=\operatorname{rank}H \quad(\forall\lambda\in\mathbb C). \\]

These are precisely

\\[ \pi_2(W)\subseteq\pi_1(W),\qquad \dim\pi\_\lambda(W)=\dim\pi_1(W)\quad(\forall\lambda\in\mathbb C). \\]

For realization, the map \\(u\mapsto uM\\) is onto \\(T\\). If \\(W=W_0\oplus E\\) and \\(w_1,\ldots,w_t\\) is a basis of \\(E\\), choose \\(u_i\\) with \\(u_iM=w_i\\). Then the \\(u_i\\) realize \\(W\\) using exactly \\(t=\dim(W/W_0)\\) free rows. The independence of the \\(w_i\\) modulo \\(W_0\\) ensures that no fewer than \\(t\\) free rows can realize this \\(W\\).

### Structural bound, including the zero case

Let \\(\omega=\dim\pi_1(W)\\). The algebraic condition gives

\\[ \pi_2(W)\subseteq\pi_1(W), \\]

while the spectral condition at \\(\lambda=0\\) gives

\\[ \dim\pi_2(W)=\dim\pi_1(W)=\omega. \\]

Consequently,

\\[ \pi_1(W)=\pi_2(W)=:\mathcal U. \\]

It follows that \\(W\subseteq\mathcal U\times\mathcal U\\), so

\\[ \dim W\le 2\omega. \\]

If \\(\omega>0\\) and \\(\dim W=\omega\\), then \\(\pi_1|\_W\\) is an isomorphism, and \\(W\\) is the graph of an endomorphism \\(F:\mathcal U\to\mathcal U\\). The complexification of \\(F\\) has an eigenvalue \\(\lambda_0\\). At this value, \\(\lambda_0\pi_1-\pi_2\\) is not injective on \\(W\\), contradicting the spectral condition. Thus

\\[ \boxed{\omega+1\le \dim W\le2\omega.} \\]

When \\(\omega=0\\), the algebraic inclusion forces \\(\pi_2(W)=0\\), and \\(\pi_1(W)=0\\) by definition. Hence \\(W=0\\). This case is feasible exactly when \\(W_0=0\\), and it should be handled separately in the polynomial construction.

Since \\(\dim W=s_0+t\\), where I write \\(s_0=\dim W_0\\), the structural bound gives useful pruning:

\\[ \boxed{ \max\\{0,\omega+1-s_0\\}\le t\le \min\\{m,\\,2\omega-s_0\\} } \quad(\omega>0). \\]

In particular, a branch with \\(s_0+t>2\omega\\) can be discarded before any polynomial is constructed.

The report should define \\(q\_{\min}=+\infty\\) when no feasible \\(W\\) exists. Otherwise,

\\[ q\_{\min}=r_0+t\_{\min}\le r_0+m\le r_0+2k. \\]

## 2. Make the chart certificate explicit

Fix \\(t\\), a Grassmann chart, and a branch \\(\omega>0\\). Let

\\[ Z(Y)\in\mathbb R^{(s_0+t)\times 2k} \\]

be the chart basis matrix for \\(W\\), and partition it as

\\[ Z(Y)=\begin{bmatrix}H(Y)&G(Y)\end{bmatrix}, \qquad H(Y),G(Y)\in\mathbb R^{\nu\times k}, \quad \nu=s_0+t. \\]

The entries of \\(H(Y)\\) and \\(G(Y)\\) are affine polynomials in the chart coordinates \\(Y\\).

The two observer conditions are equivalent to

\\[ \operatorname{rank}H=\omega,\qquad \operatorname{rank}\begin{bmatrix}H\\\G\end{bmatrix}=\omega, \tag{A} \\]

and

\\[ \operatorname{rank}(\lambda H-G)=\omega \quad\text{for all }\lambda\in\mathbb C. \tag{S} \\]

The second rank equality in (A) is equivalent to the row-space inclusion \\(\operatorname{row}G\subseteq\operatorname{row}H\\), because \\(H\\) already has rank \\(\omega\\).

### 2.1 Polynomial encoding of the algebraic condition

For a real matrix \\(X\\), write

\\[ e_j(XX^\top) \\]

for the \\(j\\)-th elementary symmetric polynomial of the eigenvalues of the positive-semidefinite matrix \\(XX^\top\\). Then

\\[ e\_\omega(HH^\top)>0,\qquad e\_{\omega+1}(HH^\top)=0 \\]

are equivalent to \\(\operatorname{rank}H=\omega\\). Likewise,

\\[ e\_{\omega+1}\left( \begin{bmatrix}H\\\G\end{bmatrix} \begin{bmatrix}H\\\G\end{bmatrix}^{\\!\top} \right)=0 \\]

together with \\(\operatorname{rank}H=\omega\\) imposes the second equality in (A).

Here \\(e_j\\) is nonnegative on positive-semidefinite matrices, and \\(e_j(XX^\top)>0\\) holds exactly when \\(\operatorname{rank}X\ge j\\). The zero condition \\(e\_{j+1}(XX^\top)=0\\) is equivalent to \\(\operatorname{rank}X\le j\\).

### 2.2 Polynomial encoding of the spectral condition

Set

\\[ P_Y(\lambda)=\lambda H(Y)-G(Y). \\]

Let

\\[ f\_{I,J}(\lambda;Y) =\det\big(P_Y(\lambda)\_{I,J}\big), \qquad |I|=|J|=\omega, \\]

be all its \\(\omega\times\omega\\) minors. Each \\(f\_{I,J}\\) has degree at most \\(\omega\\) in \\(\lambda\\).

The spectral condition says that these minors have no common complex zero. Equivalently, their greatest common divisor in \\(\mathbb R[\lambda]\\) is \\(1\\). Since all the minors have degree at most \\(\omega\\), an effective univariate Bézout identity gives

\\[ \gcd\_{I,J}f\_{I,J}=1 \quad\Longleftrightarrow\quad \exists\\,g\_{I,J}\in\mathbb R[\lambda],\ \deg g\_{I,J}<\omega: \quad \sum\_{I,J}g\_{I,J}f\_{I,J}=1. \tag{B} \\]

For each minor, form the coefficient vectors of

\\[ f\_{I,J},\ \lambda f\_{I,J},\ldots,\lambda^{\omega-1}f\_{I,J}. \\]

Put these vectors into a matrix \\(B(Y)\\), using coefficients of degrees\
\\(0,\ldots,2\omega-1\\) as its \\(2\omega\\) columns. Then (B) is equivalent to

\\[ e_0\in\operatorname{row}B(Y),\qquad e_0=(1,0,\ldots,0)\in\mathbb R^{2\omega}. \\]

Over the reals,

\\[ \operatorname{im}(B^\top B)=\operatorname{im}(B^\top), \\]

so this is equivalent to the existence of \\(x\in\mathbb R^{2\omega}\\) such that

\\[ \boxed{B(Y)^\top B(Y)x=e_0^\top.} \tag{C} \\]

This explains the \\(2\omega\\) auxiliary variables in the report. It is important to state that \\(B\\) has \\(2\omega\\) columns; its number of rows can be much larger.

The Cauchy–Binet compression computes the entries of \\(B^\top B\\) without listing every maximal minor separately. If \\(P\_{:,J}\\) denotes the submatrix made from the \\(\omega\\) columns \\(J\\), then

\\[ \sum\_{|J|=\omega} \det\\!\left(P\_{:,J}(\lambda)^\top P\_{:,J}(\mu)\right) = \sum\_{I,J}f\_{I,J}(\lambda)f\_{I,J}(\mu). \\]

The coefficient matrix of this bivariate kernel gives the required shifted coefficient inner products and hence \\(B^\top B\\).

Because the structural bound lets us discard branches with \\(\nu>2\omega\\), the number of row subsets \\(I\\) is parameter-bounded:

\\[ \binom{\nu}{\omega}\le\binom{2\omega}{\omega}\le4^\omega. \\]

The number of column subsets is \\(\binom{k}{\omega}\le2^k\\). This pruning is not optional for the complexity proof: without it, a direct enumeration of row minors could involve \\(\binom{s_0+t}{\omega}\\), which is not visibly bounded independently of the input order.

### 2.3 Number of variables and degree

The formula consists of the rank polynomials in (A) and the \\(2\omega\\) equations in (C), with the strict inequality \\(e\_\omega(HH^\top)>0\\). Thus the number of polynomial predicates is \\(O(\omega)\\).

Since \\(B(Y)\\) has entries of degree at most \\(\omega\\) in \\(Y\\), the equations \\(B^\top Bx=e_0^\top\\) have total degree at most \\(2\omega+1\\). The rank polynomial \\(e\_{\omega+1}(XX^\top)\\) has degree at most \\(2\omega+2\\) when the entries of \\(X\\) are affine in \\(Y\\). Therefore

\\[ D\le2\omega+2. \\]

The variable count is

\\[ N\_{\rm var}=t(m-t)+2\omega \le k^2+2k. \\]

This explicit construction validates the report's claimed number of variables and degree, provided the branch condition \\(s_0+t\le2\omega\\) is imposed before constructing the polynomial lists.

## 3. Question 1 — coefficient growth and the meaning of \\(B\\)

The proposed estimate

\\[ B=\operatorname{poly}(\mathcal L)\\,2^{O(k\log k)} \\]

is a safe upper bound if \\(B\\) means the total encoding length of the expanded polynomial data. It is unnecessarily loose if \\(B\\) means the maximum bit length of one coefficient, which is the quantity that appears in the usual Renegar bit-complexity statement.

I strongly recommend separating these quantities.

Let \\(\tau_0\\) be a bound on the bit length of the rational entries of the bases used to construct \\(Z(Y)\\). Because the original data are rational, bases for \\(K_0,T,W_0,V\\) can be chosen rationally and computed by exact Gaussian elimination. Their bit lengths are polynomial in the original input length \\(\mathcal L\\).

Let \\(N_Y=t(m-t)\le k^2\\). Every entry of \\(H(Y)\\) and \\(G(Y)\\) is affine in these \\(N_Y\\) variables. Expanding an \\(\omega\times\omega\\) determinant produces at most

\\[ \omega!(N_Y+1)^\omega \\]

raw product contributions. Therefore, after clearing denominators, a coefficient of a maximal minor has bit length bounded by

\\[ O\\!\left( \omega\tau_0+\log(\omega!)+\omega\log(N_Y+1) \right). \\]

Since \\(\omega\le k\\) and \\(N_Y\le k^2\\), this is

\\[ O(k\tau_0+k\log(k+2)). \\]

Forming \\(B^\top B\\) multiplies pairs of such coefficients and adds them. The Cauchy–Binet sum contributes at most \\(\binom{k}{\omega}\le2^k\\) terms; the row-subset contributions are also bounded by \\(2^{O(k)}\\) after the structural pruning \\(\nu\le2\omega\\). These sums contribute logarithmically to coefficient bit length. Thus a safe bound is

\\[ \boxed{ \tau\_{\rm cert} \le \operatorname{poly}(\mathcal L)+O(k\log(k+2)). } \\]

In particular, \\(\tau\_{\rm cert}\\) is polynomial in \\(\mathcal L\\). This is stronger than the reported bound if \\(B\\) is intended to be maximum coefficient bit length.

The total expanded polynomial encoding length is different. A polynomial of degree at most \\(D=O(k)\\) in \\(N\_{\rm var}=O(k^2)\\) variables has at most

\\[ \binom{N\_{\rm var}+D}{D} =2^{O(k\log(k+2))} \\]

monomials. With \\(O(k)\\) polynomials, this gives

\\[ \boxed{ L\_{\rm formula} \le 2^{O(k\log(k+2))}\operatorname{poly}(\mathcal L). } \\]

This is where an exponential factor of the form \\(2^{O(k\log k)}\\) naturally belongs.

### What this means for Renegar's bound

For one existential block, Renegar's bit-model decision bound has the form

\\[ \widetilde O\\!\left( \tau\_{\rm cert}(S\_{\rm poly}D)^{O(N\_{\rm var})} \right), \\]

where \\(S\_{\rm poly}\\) is the number of polynomial predicates and the suppressed logarithmic factors include the familiar \\(\log\tau\_{\rm cert}\\) and \\(\log\log\tau\_{\rm cert}\\) factors. Renegar's Part I states the existential decision bound in terms of the number of polynomials, degree, number of variables, and coefficient bit length; Part II develops the general decision method.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.researchgate.net\&sz=32)

ResearchGate+1



With

\\[ S\_{\rm poly}=O(k),\quad D=O(k),\quad N\_{\rm var}=O(k^2),\quad \tau\_{\rm cert}=\operatorname{poly}(\mathcal L)+O(k\log k), \\]

this gives

\\[ \boxed{ T\_{\rm chart} = \exp\\!\big(O(k^2\log(k+2))\big) \operatorname{poly}(\mathcal L). } \\]

So the exponent in your report survives the more careful coefficient audit.

A necessary notation change: in the report, \\(s\\) already denotes \\(\dim W_0\\). Do not reuse \\(s\\) for the number of polynomial predicates. Use \\(s_0=\dim W_0\\), \\(S\_{\rm poly}\\) for the number of polynomials, and \\(\tau\\) for maximum coefficient bit length. Also state whether \\(B\\) denotes \\(\tau\\) or \\(L\_{\rm formula}\\). Renegar's coefficient-size factor refers to coefficient bit length, not simply the total expanded formula length.

Finally, the complexity proof should explicitly state that the rational coefficients are cleared to integers using positive common denominators. This preserves all equalities and strict signs, and the extra bit growth is covered by the coefficient-height bound above.

## 4. Question 2 — exact witness extraction and its complexity

There is a suitable established algorithm, and the feasible set need not be closed.

A particularly relevant citation is:

S. Basu, R. Pollack, and M.-F. Roy, “On Computing a Set of Points Meeting Every Cell Defined by a Family of Polynomials on a Variety,” Journal of Complexity 13(1) (1997), 28–37, DOI: 10.1006/jcom.1997.0434.

The result computes points meeting every semialgebraically connected component of every nonempty sign condition. Its arithmetic-operation bound is

\\[ s^{N+1}D^{O(N)} \\]

in the full-dimensional case of \\(s\\) polynomials of degree at most \\(D\\) in \\(N\\) variables. The extra factor \\(s\\) is harmless here:

\\[ s^{N+1}D^{O(N)} \le (sD)^{O(N+1)}. \\]

The second edition of Basu–Pollack–Roy's Algorithms in Real Algebraic Geometry treats finding realizable sign conditions in §13.1 and algebraic representations of sample points in the polynomial-system-solving chapter.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车+1



### 4.1 Strict inequalities and nonclosed sets

For polynomials \\(P_1,\ldots,P_s\\), a sign condition is a vector

\\[ \sigma\in\\{-1,0,+1\\}^s. \\]

Its realization is

\\[ \\{x\in\mathbb R^N: \operatorname{sign}P_i(x)=\sigma_i \text{ for every }i\\}. \\]

A quantifier-free formula in equalities and strict inequalities is a Boolean combination of such sign conditions. For example, \\(P(x)>0\\) is the \\(+1\\) sign condition; it does not need to be replaced by a non-strict inequality.

The sample-point algorithm returns points in nonempty sign-condition components, not merely points in their closures. Thus it applies to open, unbounded, and nonclosed feasible sets. No compactness assumption is needed. This is exactly why a sign-condition algorithm is a better citation for your FIND question than an appeal to a decision algorithm alone.

### 4.2 What the algorithm returns

For rational input coefficients, the sample points can be represented exactly by real algebraic data, for example a real univariate representation with isolating information or a Thom encoding. A returned point need not have rational coordinates, but it is an exact real algebraic point.

This distinction matters. You cannot generally replace “real witness” by “rational witness” without an additional argument. Your stated problem allows \\(R\in\mathbb R^{r\times n}\\), so an algebraic real witness is perfectly valid.

The reconstruction is exact. Choose once and for all a rational linear section

\\[ \sigma:T\longrightarrow\mathbb Q^{1\times n}, \qquad \sigma(w)M=w. \\]

For a returned chart point \\(Y\\), the basis vectors of \\(W/W_0\\) have algebraic coordinates. Apply \\(\sigma\\) to obtain the corresponding algebraic free rows of \\(R\\). The resulting \\(R\\) realizes the returned \\(W\\).

### 4.3 What complexity statement should you actually write?

There are two different results being used:

- Renegar: a bit-complexity decision procedure for the existential real formula.
- Basu–Pollack–Roy: a sample-point procedure that supplies an exact witness.

Do not suggest that Renegar's decision bound alone outputs a witness. Renegar's separate 1992 article on approximating solutions concerns approximation; it should not be your only citation for exact algebraic sample points.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://epubs.siam.org\&sz=32)

epubs.siam.org



The BPR 1997 bound is stated in arithmetic operations. For a bit-complexity theorem, add the coefficient-height and output-representation estimates. A safe presentation is:

\\[ T\_{\rm sample} \le (sD)^{O(N)} \operatorname{poly}(\tau) \\]

including the exact algebraic output representation, where \\(\tau\\) is the maximum coefficient bit length. If you prefer an explicitly output-sensitive formulation, write

\\[ T\_{\rm sample} \le (sD)^{O(N)}\operatorname{poly}(\tau) +\operatorname{poly}(L\_{\rm out}), \\]

and give a singly exponential bound on \\(L\_{\rm out}\\) from the chosen real-univariate-representation implementation. The sample-point theorem supplies the arithmetic bound; the book's exact algebraic representation machinery supplies the appropriate output model. Do not cite the arithmetic-operation count alone as if it were already a bit-operation theorem.

For your application, \\(s=S\_{\rm poly}=O(k)\\), \\(D=O(k)\\), and \\(N=O(k^2)\\). The output degree and representation size may be large as a function of \\(k\\), but this is allowed in FPT. Thus the exact witness algorithm still has a bound of the form

\\[ \boxed{ T\_{\rm FIND} = f(k)\operatorname{poly}(\mathcal L), \qquad f(k)=\exp(O(k^2\log(k+2))), } \\]

with an exact algebraic \\(R\\).

I would therefore replace the report's conditional FIND paragraph with a theorem based on the BPR sample-point algorithm, while being explicit about the arithmetic-versus-bit-complexity distinction.

## 5. Question 3 — Is \\(k\\) a meaningful parameter, and is the literature comparison fair?

Yes. The strongest claim is that your method makes the dimension of the entire search problem, not just one chart, bounded by a function of \\(k\\).

Your chart dimensions satisfy

\\[ t(m-t)\le \left\lfloor\frac{m^2}{4}\right\rfloor\le k^2, \\]

and the total number of charts over all \\(t\\) is

\\[ \sum\_{t=0}^m\binom mt=2^m\le4^k. \\]

The polynomial-certificate variables add only \\(2\omega\le2k\\). Thus both the number of real variables and the total number of charts are controlled by \\(k\\).

The parameter has a clear linear-algebraic interpretation:

\\[ k=\dim\big(\ker C\cap\ker(CA)\big). \\]

It measures the number of state directions annihilated by both the current measurement and its first \\(A\\)-iterate. Your algorithm searches only through the image of this space under the two maps \\(N\\) and \\(AN\\), rather than through an ambient \\(n\\)-dimensional nullspace.

### 5.1 Comparison with the recent nullspace-chart approach

The comparison in the report is substantially correct, but it must be framed as a comparison of parameterization dimensions, not as a claim that the existing characterization is algorithmically inferior in every respect.

Fernando's September 2026 arXiv preprint parameterizes a fixed-order family through a Grassmannian

\\[ \operatorname{Gr}(d,m_L), \qquad d=n-p-q, \\]

and explicitly states that each chart has \\(d(m_L-d)\\) scalar parameters. Under the paper's independent-row convention, the corresponding expression reduces to

\\[ (n-p-q)(q-r). \\]

The chart count and parameter count can therefore depend on \\(n\\), even when the observer order is fixed.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



Your comparison can say:

> The fixed-order nullspace parameterization in the recent functional-observer literature uses Grassmann charts whose coordinate dimension depends on the ambient state dimension. In contrast, our reduction parameterizes intermediate row spaces inside a space of dimension at most \\(2k\\). Consequently, the number of chart coordinates is at most \\(k^2\\), and the total number of charts is at most \\(4^k\\), independently of the ambient dimension and the number of free row slots.

Two qualifications should accompany this comparison:

1. The Fernando paper is an arXiv preprint, not a verified published journal article in the sources I checked.
2. Its order convention removes redundant measured outputs and functional rows. Your model allows redundant rows and zero padding. To make the comparison fully like-for-like, first normalize the fixed functional rows and specify whether your \\(q\\) counts row slots or independent observer coordinates.

### 5.2 A sharper parameter than \\(k\\)

The earlier suggestion

\\[ \ell=\operatorname{rank}(AN)\le k \\]

is valid and should be retained. Here is the exact proof.

Since \\(N\\) has full column rank,

\\[ \pi_1(T)=\mathbb R^{1\times k}, \qquad \pi_2(T)=\operatorname{row}(AN)=:S. \\]

Every feasible \\(W\\) satisfies

\\[ \pi_1(W)=\pi_2(W)\subseteq\pi_2(T)=S. \\]

Hence

\\[ \boxed{W\subseteq T\cap(S\times S).} \\]

If \\(W_0\not\subseteq T\cap(S\times S)\\), the problem is immediately infeasible. Otherwise, the full search can be restricted to this smaller subspace. Set

\\[ d_S=\dim\big(T\cap(S\times S)\big)\le2\ell, \qquad m_S=d_S-s_0. \\]

A rational basis of \\(S\\) changes the pair coordinates from length \\(k\\) to length \\(\ell\\), without changing any of the rank conditions. The same Grassmannian and polynomial-certificate construction then has at most

\\[ \ell^2+2\ell \\]

variables and at most \\(4^\ell\\) charts.

This gives a stronger parameterized bound, subject to spelling out the coordinate transformation in the certificate construction:

\\[ T\_{\rm DEC}\le \exp(O(\ell^2\log(\ell+2)))\operatorname{poly}(\mathcal L). \\]

### 5.3 An additional refinement: an iterated common-projection core

There is an even stronger, easily computable pruning step that is not in the report.

Start with

\\[ S_0=\mathbb R^{1\times k}, \qquad T_j=T\cap(S_j\times S_j), \\]

and define

\\[ S\_{j+1}=\pi_1(T_j)\cap\pi_2(T_j). \\]

The sequence is decreasing: \\(S_1\subseteq S_0\\), and the map

\\[ S\longmapsto \pi_1\big(T\cap(S\times S)\big) \cap \pi_2\big(T\cap(S\times S)\big) \\]

is monotone under inclusion. Therefore the process stabilizes after at most \\(k\\) strict dimension decreases. Let the terminal space be \\(S\_\*\\).

For any feasible \\(W\\), suppose inductively that \\(W\subseteq T_j\\). Since its two projections are equal,

\\[ \pi_1(W)=\pi_2(W) \subseteq\pi_1(T_j)\cap\pi_2(T_j) =S\_{j+1}. \\]

Thus \\(W\subseteq S\_{j+1}\times S\_{j+1}\\), and since \\(W\subseteq T\\), it follows that \\(W\subseteq T\_{j+1}\\). By induction,

\\[ \boxed{W\subseteq T\cap(S\_\*\times S\_\*)} \\]

for every feasible \\(W\\).

This is an exact, rational-linear-algebra preprocessing step. Its dimension satisfies

\\[ \ell\_\*:=\dim S\_\* \le\operatorname{rank}(AN)=\ell\le k. \\]

If \\(W_0\\) is not contained in \\(T\cap(S\_\*\times S\_\*)\\), the instance is infeasible. Otherwise, the search may be performed entirely inside this terminal core.

My recommendation: investigate \\(\ell\_\*\\) as the principal parameter. The proof of the pruning lemma is complete; the remaining work is to rewrite the polynomial-certificate construction in a basis of \\(S\_\*\\) and verify the coefficient bounds in those coordinates. This is a potentially meaningful improvement over merely replacing \\(k\\) by \\(\operatorname{rank}(AN)\\).

## 6. Question 4 — Are there hidden hypotheses, especially full row rank?

There is no hidden full-row-rank requirement in the rank identities or the subspace realization argument. Both are valid with redundant rows.

However, there is an important distinction between the rank-free row-slot problem in the report and the usual reduced observer-order problem in control theory.

### 6.1 What the report proves without extra assumptions

The report permits:

- redundant rows in \\(L_0\\);
- redundant or zero free rows;
- arbitrary real free rows \\(R\\);
- observer conditions expressed only through the stated rank equalities.

Under this convention, zero padding is legitimate, so

\\[ \mathrm{DEC}(q)\Longrightarrow\mathrm{DEC}(q+1). \\]

The result is mathematically correct for that model.

### 6.2 What changes under the reduced-order convention

In the recent nullspace-chart formulation, redundant measured outputs and redundant functional rows are removed. The observer order is determined by the rank increase produced by adjoining the augmented functional matrix to \\(C\\), not merely by the number of row slots.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



Under that convention, the rows of the augmented functional matrix must be independent modulo the measured-output rows. Appending a zero row does not increase the observer order and does not produce a valid reduced realization of the next order.

You should therefore distinguish:

\\[ \mathrm{DEC}\_{\rm slot}(q) \quad\text{and}\quad \mathrm{DEC}\_{\rm red}(q). \\]

The monotonicity and saturation claims in the report apply directly to \\(\mathrm{DEC}\_{\rm slot}\\). They do not automatically apply to the reduced problem.

There is a useful positive point: if \\(L_0\\) is already independent modulo \\(\operatorname{row}(C)\\), then the \\(t\\) rows chosen as preimages of a basis of \\(W/W_0\\) can be made independent modulo \\(\operatorname{row}(C)+\operatorname{row}(L_0)\\). Indeed, if a linear combination of those preimages belonged to that row space, multiplication by \\(M\\) would put the corresponding combination of the basis vectors of \\(W/W_0\\) inside \\(W_0\\), forcing all coefficients to vanish. Thus the minimal realization can satisfy the usual reducedness requirement when the fixed rows have been normalized.

If the rows of \\(L_0\\) are internally dependent or have components already in \\(\operatorname{row}(C)\\), then \\(r_0\\) is not necessarily the number of independent prescribed functional directions. In that case

\\[ r_0+t\_{\min} \\]

is the minimum row-slot count in your model, not necessarily the minimum reduced observer order.

### 6.3 Other assumptions to state explicitly

There are two further modelling choices:

- Free-row restrictions. If \\(R\\) must be sparse, rational, bounded, structured, or lie in a prescribed subspace, the surjectivity argument does not automatically respect those restrictions. Your current result uses the fact that every free row is an arbitrary element of \\(\mathbb R^{1\times n}\\).
- Spectral region. Your condition is imposed for all \\(\lambda\in\mathbb C\\). This is the pole-assignability version of the spectral condition. Some functional-observer formulations use only a specified region, such as the closed right half-plane, for detectability or asymptotic convergence. The problem and certificate must be changed if that is the intended requirement. The recent Fernando preprint explicitly distinguishes the all-\\(\mathbb C\\) pole-assignability condition from a restricted-region detectability condition.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

  arXiv



These are not defects in your reduction. They define the exact scope of the theorem and should be stated in the problem formulation.

## 7. Question 5 — Do nonclosed feasible chart sets invalidate sample-point extraction?

No. The concern is resolved by using sign-condition sample points, not by assuming closedness.

Your chart formula has the form

\\[ \Phi(Y,x)= \bigwedge_i P_i(Y,x)=0 \quad\wedge\quad \bigwedge_j Q_j(Y,x)>0 \\]

or a Boolean combination of such conditions. Its solution set is semialgebraic and may be open or nonclosed.

A sign-condition sample-point algorithm computes a point in each nonempty connected component of each realizable sign condition. Strict positivity is simply one of the signs it records. Consequently, a sample point satisfies the original strict inequality, rather than merely belonging to the closure of the feasible set.

For example, if

\\[ \mathcal S=\\{(y,x):P_1(y,x)=0,\ Q_1(y,x)>0\\}, \\]

the sample-point procedure treats the signs \\(0,+1\\) and returns a point with exactly those signs. The set need not be compact, bounded, or closed.

The only implementation point to watch is that an algorithm may use infinitesimals internally. Its final output must be a point in the original real sign condition, represented exactly; an infinitesimal point in an auxiliary extension is not by itself the required witness.

For your report, I would use the following statement:

> The feasible chart locus is not assumed to be closed or bounded. We apply an exact sign-condition sample-point algorithm to the rational polynomial family defining the chart. Such algorithms return a point in each nonempty semialgebraically connected component of every realizable sign condition. Therefore strict inequalities are handled directly, and no closure or compactness assumption is needed.

The BPR sign-condition result is the appropriate reference for this point.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车+1



## 8. Question 6 — Is the dimension bound already known?

I would present

\\[ \omega+1\le\dim W\le2\omega \\]

as an elementary structural lemma proved in the paper, rather than make a literature-priority claim.

The upper bound is just

\\[ W\subseteq\mathcal U\times\mathcal U. \\]

The lower bound says that a subspace of dimension exactly \\(\omega\\), whose first projection is an isomorphism onto \\(\mathcal U\\), would define a square pencil

\\[ \lambda I-F. \\]

Its determinant is a monic polynomial of degree \\(\omega>0\\), and hence has a complex root. That root violates full rank of the pencil.

This is a basic fact about a square pencil with nonsingular leading coefficient. The observer-specific statement is its application to \\(W\\) after the two projection conditions have forced

\\[ \pi_1(W)=\pi_2(W). \\]

I have not found a reason to attribute this exact inequality to a specific functional-observer theorem. The proof is short, transparent, and stronger for your purposes than a citation alone. The recent nullspace-chart paper uses matrix-pencil rank conditions and maximal-minor gcd tests, but its chart theorem does not make this particular dimension bound its central result.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



## 9. A further algorithmic improvement: binary search for \\(\mathrm{OPT}\\)

The report gives

\\[ T\_{\rm OPT}\le(2k+1)T\_{\rm DEC}. \\]

This is correct as a sequential-search bound, but it can be improved.

In the rank-free model, \\(\mathrm{DEC}(q)\\) is monotone:

\\[ \mathrm{DEC}(q)\Longrightarrow\mathrm{DEC}(q+1). \\]

Also, no new subspace needs more than \\(m\le2k\\) free rows. Therefore:

1. Test \\(\mathrm{DEC}(r_0+m)\\). If it fails, no feasible order exists.
2. If it succeeds, binary-search the smallest feasible \\(q\\) in \\([r_0,r_0+m]\\).
3. Run the sample-point algorithm at that order to return an exact witness.

This requires

\\[ O(\log(m+2))=O(\log(k+2)) \\]

decision calls, followed by one witness extraction. Thus, for the rank-free model,

\\[ \boxed{ T\_{\rm OPT} = O(\log(k+2))\\,T\_{\rm DEC} +T\_{\rm FIND}. } \\]

The FPT classification is unchanged, but the order-search description is better.

This improvement relies on allowing zero-row padding. Do not carry it over to the reduced-order model without proving a corresponding monotonicity theorem. The recent functional-observer order-spectrum paper establishes an extension property for the algebraic condition, but explicitly distinguishes that from the joint algebraic-and-spectral feasibility question.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



## 10. What the computational and Lean checks establish

The report describes the evidence reasonably, but I would make the distinction between proof, formalization, and testing sharper.

### Exact computer-algebra checks

The 36 successful tests are useful evidence that the implementation matches the intended reduction. They do not prove the reduction or the FPT theorem. In particular, the corrected error in counting \\(W_0\\) rows as free rows should be recorded in the reproducibility material, not treated as a minor detail to omit.

For the spectral check, make the exact test explicit:

\\[ \gcd\\{f\_{I,J}(\lambda):|I|=|J|=\omega\\}=1 \\]

over \\(\mathbb Q[\lambda]\\) for rational test instances. Also state the convention that if all maximal minors are zero, spectral feasibility fails for \\(\omega>0\\). Handle \\(\omega=0\\) separately.

The test suite should include the following boundary cases, not only randomly generated generic instances:

- \\(k=0\\) and \\(\omega=0\\);
- \\(W_0=0\\) and \\(W_0=T\\);
- \\(s_0>2\omega\\), which must be rejected by the structural bound;
- \\(m=0\\);
- a pencil with a common complex root but no real common root;
- pencils with identically zero maximal minors;
- feasible subspaces on different Grassmann charts, including points where some particular chart's pivot minor vanishes.

The last two spectral cases are particularly important because the condition concerns complex \\(\lambda\\), not merely real \\(\lambda\\).

### Lean formalization

Your description is appropriately modest: the formalized lemmas establish the basic linear maps and subspace realization, not yet the observer equivalence.

I would prioritize the next Lean results in this order:

1. Formalize the rank-compression identity.
2. Formalize the equivalence between the original rank conditions and the two projection conditions.
3. Formalize \\(\pi_1(W)=\pi_2(W)\\) using the algebraic condition and the spectral condition at zero.
4. Formalize the structural dimension inequality, including the complex eigenvalue argument.
5. Only then formalize the polynomial gcd certificate and the Cauchy–Binet coefficient identity.

The first four are linear-algebraic and should be much more tractable than formalizing the complete real-algebraic decision procedure. The Lean status should continue to say exactly which results have been formalized and which have not.

## 11. Suggested replacement for Part II's complexity paragraph

I would rewrite the main complexity claim approximately as follows.

> Parameterized decision theorem (rank-free model).\
> Let \\(A,C,L_0\\) have rational entries, let\
> \\[\
> K_0=\ker\beginC\CA\end,\
> \qquad k=\dim K_0,\
> \\]\
> and allow the free rows \\(R\\) to be arbitrary real row vectors, with redundant and zero rows permitted. Then, for each prescribed \\(q\ge r_0\\), \\(\mathrm{DEC}(q)\\) can be decided in\
> \\[\
> \exp(O(k^2\log(k+2)))\operatorname(\mathcal L)\
> \\]\
> bit operations.
>
> If feasible, an exact real-algebraic witness \\(R\\) can also be returned within a bound of the same FPT form using a sign-condition sample-point algorithm. The minimum feasible row count can be found using \\(O(\log(k+2))\\) decision calls and one witness extraction.
>
> The algorithm uses rational bases for the relevant subspaces, enumerates the standard Grassmann charts, and constructs a quantifier-free existential-real formula in at most \\(k^2+2k\\) variables. The number of polynomial predicates is \\(O(k)\\), their degrees are at most \\(2k+2\\), and their coefficient bit lengths are polynomial in \\(\mathcal L\\) up to parameter-dependent additive terms. Renegar's existential-real decision procedure gives the decision bound, while the Basu–Pollack–Roy sample-point procedure gives an exact algebraic witness.

I would add a separate corollary:

> Reduced-core corollary. The same algorithm can be run in coordinates of a rational subspace \\(S\_\*\\) obtained by the iterated common-projection procedure. Writing \\(\ell\_\*=\dim S\_\*\\), all feasible intermediate spaces lie in \\(T\cap(S\_\*\times S\_\*)\\). After expressing the polynomial certificate in a basis of \\(S\_\*\\), the same argument gives\
> \\[\
> \exp(O(\ell\_^2\log(\ell\_+2)))\operatorname(\mathcal L).\
> \\]\
> In particular \\(\ell\_\*\le\operatorname{rank}(AN)\le k\\).

For the corollary, explicitly include the rational coordinate conversion in the proof. It is straightforward, but the theorem should not simply assert that replacing \\(k\\) by a smaller number leaves every certificate formula unchanged.

## 12. Recommended revisions in priority order

| Priority            | Change                                                                             | Reason                                                        |
| ------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Essential           | Write out the \\(B(Y)^\top B(Y)x=e_0^\top\\) certificate                           | Makes the \\(2\omega\\) variable claim verifiable             |
| Essential           | State the branch restriction \\(s_0+t\le2\omega\\)                                 | Keeps the number of row minors independent of \\(r_0\\)       |
| Essential           | Separate coefficient height from total formula size                                | Makes the Renegar bit-complexity substitution precise         |
| Essential           | Distinguish row-slot order from reduced observer order                             | Zero-padding monotonicity depends on the convention           |
| Essential           | Replace the conditional FIND paragraph with a sign-condition sample-point argument | Provides exact algebraic witnesses on nonclosed feasible loci |
| Strong improvement  | Replace \\(k\\) by \\(\ell=\operatorname{rank}(AN)\\)                              | Reduces the effective coordinate space                        |
| Further improvement | Compute the iterated common-projection core \\(S\_\*\\)                            | May reduce the parameter below \\(\ell\\)                     |
| Strong improvement  | Use binary search for \\(\mathrm{OPT}\\)                                           | Reduces the number of decision calls                          |
| Presentation        | Rename \\(s\\), \\(r\\), \\(d\\), and \\(U\\) where needed                         | Avoids collisions between dimension and complexity notation   |
| Reproducibility     | Publish exact test generation and corrected implementation details                 | Makes the computational evidence independently checkable      |

## 13. References to include

The following references are directly relevant to the report's claims.

Exact real-algebraic decision and witness algorithms

1\. J. Renegar, “On the Computational Complexity and Geometry of the First-Order Theory of the Reals. Part I: Introduction. Preliminaries. The Geometry of Semi-Algebraic Sets. The Decision Problem for the Existential Theory of the Reals,” Journal of Symbolic Computation 13(3), 255–299, 1992.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车



2\. J. Renegar, “On the Computational Complexity and Geometry of the First-Order Theory of the Reals. Part II: The General Decision Problem. Preliminaries for Quantifier Elimination,” Journal of Symbolic Computation 13(3), 301–327, 1992.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车+1



3\. S. Basu, R. Pollack, and M.-F. Roy, “On Computing a Set of Points Meeting Every Cell Defined by a Family of Polynomials on a Variety,” Journal of Complexity 13(1), 28–37, 1997, DOI: 10.1006/jcom.1997.0434.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车



4\. S. Basu, R. Pollack, and M.-F. Roy, Algorithms in Real Algebraic Geometry, 2nd ed., Springer, 2006. Particularly relevant are §13.1, “Finding Realizable Sign Conditions,” and the univariate-representation material in Chapter 12.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://link.springer.com\&sz=32)

Springer+1



Functional-observer comparison

5\. T. Fernando, “A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions,” arXiv:2609.33615, September 2026.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



6\. T. Fernando, “Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger,” arXiv:2609.37992, September 2026. Particularly relevant are the reduced-order assumptions and the fixed-order Grassmann-chart parameterization in §6.2.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



These last two should be cited as preprints, not as established journal publications, unless their publication status is separately verified.

## Final verdict

The mathematical core of the report is sound. Its strongest contribution is the reduction from arbitrary free rows to an intermediate subspace

\\[ W_0\subseteq W\subseteq T \\]

with the exact row-cost identity

\\[ \text{minimum additional rows to realize }W =\dim(W/W_0). \\]

The structural inequality

\\[ \omega+1\le\dim W\le2\omega \\]

then controls the size of the pencil and the polynomial certificate.

The complexity conclusion is credible, but the report should not yet present the FIND and bit-complexity claims without the explicit certificate, coefficient-height convention, and exact sample-point reference. The distinction between row-slot order and reduced observer order is also essential: it affects the interpretation of \\(q\_{\min}\\), monotonicity, and the comparison with the functional-observer literature.

The most valuable new direction is to use the common-projection core \\(S\_\*\\), rather than stopping at \\(k\\) or even \\(\operatorname{rank}(AN)\\). It is an exact preprocessing reduction and may provide the sharpest natural parameter in this framework.

My recommendation is to make the paper's main claim a parameterized algorithm for the rank-free problem, state the reduced-order version separately, and develop the \\(S\_\*\\)-reduction as the main strengthening. That gives the report a precise scope, a defensible complexity argument, and a clearer point of distinction from the existing Grassmann-chart characterization.