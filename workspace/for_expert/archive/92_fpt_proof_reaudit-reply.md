# Second proof audit: DEC, OPT and FIND parameterized by \\(\operatorname{rank}(AN)\\)

I have examined the new report against the previous version, paying particular attention to the five corrections, Lemmas 8–10, the Bézout certificate, and the newly proposed bit-complexity argument.

My assessment is that the new version is substantially stronger, but I would not yet declare the complete three-part FPT theorem submission-ready. The main structural mathematics is sound. The new representation-length argument is a meaningful improvement. However, there are still several points where the current proof claims more than its derivation establishes.

The most important distinction is between:

- a correct mathematical characterization;
- an effective construction of the polynomial system;
- an arithmetic-complexity bound;
- a bit-complexity bound for the algorithm and its exact output.

The first three are now close to being established. The fourth still needs a more careful treatment.

Overall assessment

Structural reduction and dimension bound

Sound

Bézout certificate

Sound, with clarifications

Coordinate compression and parameter

Sound

Coefficient-height Lemma 8

Needs a complete derivation

Sample-point Lemma 9

Needs theorem-level verification

Preprocessing Lemma 10

Correct direction, incomplete accounting

DEC and OPT

Strong, conditional on encoding

FIND bit complexity

Not fully established

I will distinguish genuine mathematical gaps from corrections that only improve rigor or presentation.

# Part I. The mathematical structure

## 1. Lemmas 1–4: the fundamental reduction is correct

I find no substantive problem with the central compression argument.

The identity

\\[ \operatorname{rank}\begin{bmatrix}J\\\Q\end{bmatrix} = \operatorname{rank}J+\operatorname{rank}(QN) \\]

is valid when the columns of \\(N\\) form a basis of \\(\ker J\\).

Consequently, the original conditions reduce to

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H \tag{1} \\]

and

\\[ \operatorname{rank}(\lambda H-H_A) = \operatorname{rank}H \qquad(\forall\lambda\in\mathbb C). \tag{2} \\]

The complexification paragraph in the new report fixes an important ambiguity in the previous version.

The structural argument is also correct:

\\[ \pi_1(W)=\pi_2(W)=U \\]

and therefore

\\[ W\subseteq U\times U. \\]

This gives

\\[ \dim W\le2\omega. \\]

If equality \\(\dim W=\omega\\) held, \\(W\\) would be the graph of an endomorphism \\(F\\) of \\(U\\). Since the complexification of \\(U\\) is a nonzero finite-dimensional complex vector space, \\(F\\) would have an eigenvalue.

At that eigenvalue,

\\[ \dim\pi\_{\lambda_0}(W)<\omega, \\]

a contradiction.

Thus

\\[ \boxed{\omega+1\le\dim W\le2\omega} \\]

for \\(\omega>0\\).

I would retain this proof essentially unchanged.

### 1.1 A minor improvement to Lemma 3

The converse realization statement is correct, but it is worth making one detail explicit.

Let

\\[ \phi:\mathbb R^{1\times n}\to T, \qquad u\mapsto uM. \\]

The map is surjective by the definition of \\(T\\).

Given \\(W_0\subseteq W\subseteq T\\), choose a basis

\\[ w_1,\ldots,w_t \\]

of a complement of \\(W_0\\) in \\(W\\).

For each \\(w_i\\), choose a preimage \\(u_i\\) under \\(\phi\\).

Then

\\[ R=\begin{bmatrix}u_1\\\\\vdots\\\u_t\end{bmatrix} \\]

realizes \\(W\\).

This proves existence of a witness with exactly \\(t\\) additional rows.

It does not assert that every possible realizing \\(R\\) has exactly \\(t\\) rows. That distinction is useful when formulating FIND.

## 2. Lemma 5 and Lemma 6: the optimization argument is correct

Zero padding gives

\\[ \mathrm{DEC}(q)\implies\mathrm{DEC}(q+1). \\]

The saturation threshold is

\\[ d-s_0=\dim(T/W_0). \\]

The structural bound gives

\\[ t=\dim(W/W_0) \le2\omega-s_0 \le2\ell. \\]

Therefore,

\\[ q\_{\min}=r_0+t\_{\min} \\]

and binary search on

\\[ 0\le t\le2\ell \\]

is justified.

One small correction:

The statement

\\[ \mathrm{DEC}(r_0+r) = \mathrm{DEC}(r_0+d-s_0) \qquad(r\ge d-s_0) \\]

is correct if DEC denotes feasibility at the indicated order. I recommend spelling out that this follows from saturation of the available extension space, rather than from the structural bound alone.

The structural bound supplies the smaller \\(2\ell\\) search interval; the saturation identity supplies the equivalence beyond \\(d-s_0\\).

These are two distinct arguments.

## 3. The reduction from \\(k\\) to \\(\ell\\): correct, but the coordinate implementation must be made explicit

The new report correctly retracts the earlier incorrect statement about row-space invariance.

The correct transformation is

\\[ \operatorname{row}(XP)\ne\operatorname{row}(X) \\]

in general, but

\\[ \operatorname{rank}(XP)=\operatorname{rank}(X) \\]

and

\\[ \operatorname{row}(X)\subseteq\operatorname{row}(Y) \iff \operatorname{row}(XP)\subseteq\operatorname{row}(YP). \\]

This is the right formulation.

The infeasibility test is also valid:

\\[ W_0\not\subseteq S\times S \implies \text{no feasible extension at any order}. \\]

There is no hidden issue here.

### 3.1 An important dimensional correction in the new report

There is one inconsistency that must be repaired.

In the quotient-chart construction, the report defines

\\[ Z(Y)\in\mathbb R^{\nu\times2k}. \\]

But in the Bézout matrix construction, it uses

\\[ \binom{\ell}{\omega} \\]

and treats \\(H,G\\) as matrices with \\(\ell\\) columns.

These are not yet the same coordinate representation.

You need to make the coordinate reduction explicit at the level of the chart basis.

The clean construction is:

1. Compute the rational coordinate transformation \\(P\\).
2. Transform every vector in \\(V\subseteq T\subseteq\mathbb Q^{2k}\\) using the block transformation\
   \\[\
   \operatorname{diag}(P,P).\
   \\]
3. Use the fact that \\(V\subseteq S\times S\\) to delete the last \\(2(k-\ell)\\) zero coordinates.
4. Express \\(E_0,E_Q\\) in the resulting \\(2\ell\\)-dimensional ambient space.
5. Define\
   \\[\
   Z(Y)\in\mathbb R^{\nu\times2\ell}.\
   \\]

Then

\\[ Z(Y)=[H(Y)\ G(Y)], \qquad H,G\in\mathbb R^{\nu\times\ell}. \\]

This makes every later formula consistent.

This is not a mathematical obstruction. It is an essential correction to the written construction.

# Part II. Lemma 8: coefficient-height audit

This is the first major technical issue in the new report.

I agree with the overall strategy of Lemma 8. The claimed polynomial dependence on the original input bit length is plausible. But the current proof sketch does not yet justify every step, and there is one indexing error.

## 4. Part (a): rational basis heights

The report claims that

\\[ N,\quad S,\quad E_0,\quad E_Q \\]

have rational coefficient heights bounded by

\\[ \tau_0=\operatorname{poly}(\mathcal L). \\]

This is correct in principle.

The relevant matrices are constructed by rational linear algebra:

- \\(N\\) is obtained from the kernel of \\([C;CA]\\).
- \\(S\\) is obtained from the row space of \\(AN\\).
- \\(T\\) is obtained from the row space of \\(M\\).
- \\(W_0\\) is obtained from the row space of \\(L_0M\\).
- \\(V\\) is obtained by intersecting \\(T\\) with \\(S\times S\\).
- \\(E_Q\\) is a basis of a rational complement of \\(W_0\\) in \\(V\\).

All these operations have polynomial bit complexity in the input length when performed using exact rational linear algebra with controlled normalization.

### 4.1 Does \\(k\\) reappear in the height bound?

No problematic exponential dependence on \\(k\\) is necessary.

Since \\(k\le n\\), and the original input explicitly contains matrices of dimensions involving \\(n\\), polynomial dependence on \\(k\\) is polynomial dependence on the input length.

More importantly, the coordinate transformation and basis extension can be computed using rational matrices of dimension at most polynomial in \\(n\\).

The key is to avoid treating a basis of \\(S\\) as an arbitrary real basis.

It must be a rational basis constructed by exact elimination.

### 4.2 What is missing?

The statement

> Hadamard bounds the minors, and elimination does not increase this beyond a polynomial factor.

is too compressed for a paper-level complexity proof.

I recommend replacing it with the following argument.

Suppose the input rational matrix has entries with numerators and denominators bounded in bit length by \\(\tau\\).

After clearing denominators, obtain an integer matrix with entries of bit size \\(O(\tau+\log m)\\), where \\(m\\) is the relevant matrix dimension.

Every \\(j\times j\\) minor then has bit size

\\[ O\bigl(j(\tau+\log m+\log j)\bigr) \\]

by Hadamard's inequality.

A basis of the kernel or row space can be represented using ratios of such minors, after choosing pivot columns or rows.

Consequently, the bit size of every rational basis entry is polynomial in the original input length.

This is a sufficiently explicit argument.

## 5. Part (b): chart matrix height

Once the coordinate transformation has been applied, write

\\[ E_0\in\mathbb Q^{s_0\times2\ell}, \qquad E_Q\in\mathbb Q^{m'\times2\ell}. \\]

Then

\\[ Z(Y)= \begin{bmatrix} E_0\\\ [I_t\mid Y]E_Q \end{bmatrix}. \\]

Every coefficient of every affine entry of \\(Z(Y)\\) is an entry of \\(E_0\\) or \\(E_Q\\), or a sum of at most \\(m'\\) such entries.

Therefore, if their rational heights are bounded by \\(\tau_0\\), the chart coefficients have height

\\[ \tau_0+O(\log(m'+1)) \\]

up to the usual numerator/denominator normalization.

Since

\\[ m'\le2\ell, \\]

this remains polynomial in \\(\mathcal L\\).

Conclusion: the chart matrix does not reintroduce \\(k\\) in the parameter dependence.

I would make the reduced \\(2\ell\\)-coordinate representation explicit before claiming this.

## 6. Part (c): maximal-minor coefficient height

This estimate is essentially correct.

Each maximal minor is

\\[ f\_{I,J}(\lambda;Y) = \det(\lambda H(Y)-G(Y))\_{I,J}. \\]

Every matrix entry is affine in \\(Y\\), with coefficients of height at most \\(\tau_0+O(1)\\), and is affine in the formal indeterminate \\(\lambda\\).

Expanding the determinant gives at most

\\[ \omega! \\]

products of \\(\omega\\) entries.

Therefore the coefficient heights are bounded by

\\[ O\left( \omega\tau_0+ \log(\omega!)+ \omega\log(\omega+2) \right). \\]

Using

\\[ \log(\omega!)=O(\omega\log(\omega+2)), \\]

we obtain

\\[ \tau_f = O\left( \omega\tau_0+\omega\log(\omega+2) \right). \\]

Since \\(\omega\le\ell\le n\\), this is polynomial in the original input length.

I agree with this calculation.

One refinement: explicitly say that \\(\lambda\\) is a formal polynomial indeterminate, not one of the semialgebraic decision variables. Otherwise readers may misinterpret the degree bound \\(D\\).

## 7. Part (d): Cauchy–Binet and the Gram polynomials

This is where I found a concrete correction.

The report says that the number of principal minors in

\\[ \sigma\_{\omega+1} \left( \begin{bmatrix}H\\\G\end{bmatrix} \begin{bmatrix}H\\\G\end{bmatrix}^{\mathsf T} \right) \\]

is

\\[ \binom{\nu}{\omega}. \\]

That is incorrect.

It is

\\[ \boxed{\binom{\nu}{\omega+1}.} \\]

The first Gram polynomial,

\\[ \sigma\_\omega(HH^{\mathsf T}), \\]

does involve

\\[ \binom{\nu}{\omega} \\]

principal minors.

The second one involves

\\[ \binom{\nu}{\omega+1}. \\]

### 7.1 Does this invalidate the complexity bound?

No.

The structural pruning condition is

\\[ \nu=s_0+t\le2\omega. \\]

Thus

\\[ \binom{\nu}{\omega+1} \le 2^\nu \le4^\omega. \\]

The same bound applies to the first Gram polynomial.

So the intended complexity estimate survives.

The correction is nevertheless important because the proof should use the actual number of minors.

### 7.2 Where should the pruning occur?

Before constructing the polynomial system.

For each pair \\((t,\omega)\\), reject the branch whenever

\\[ s_0+t>2\omega. \\]

Also reject impossible rank choices such as

\\[ \omega>\ell \\]

or

\\[ \omega>\nu. \\]

After pruning, every surviving branch satisfies

\\[ \nu\le2\omega. \\]

This is what makes the number of principal minors bounded by a function of \\(\ell\\).

I would state the branch-enumeration procedure explicitly:

\\[ \begin{aligned} &0\le t\le\min(r,m'),\\\ &1\le\omega\le\ell,\\\ &\omega\le\nu=s_0+t\le2\omega. \end{aligned} \\]

The last lower inequality is also a necessary structural condition for a positive-dimensional feasible space.

### 7.3 Cauchy–Binet height

The kernel identity is correct:

\\[ \sum\_{|J|=\omega} \det\left( P\_{:,J}(\lambda)^{\mathsf T} P\_{:,J}(\mu) \right) = \sum\_{I,J} f\_{I,J}(\lambda)f\_{I,J}(\mu). \\]

The number of column subsets is

\\[ \binom{\ell}{\omega}\le2^\ell. \\]

The sum therefore introduces at most \\(O(\ell)\\) additional bits in the coefficient height, assuming a common controlled denominator.

The number of row subsets is eliminated from the construction.

The second Gram polynomial is handled separately, using the branch pruning.

I recommend writing the height argument in this order:

1. Bound the height of the entries of \\(Z(Y)\\).
2. Bound the height of the coefficients of the maximal minors.
3. Bound the height of the Cauchy–Binet kernel.
4. Bound the height of \\(\sigma\_\omega\\).
5. Bound the height of \\(\sigma\_{\omega+1}\\).
6. Bound the height of the final polynomial equations.

This will prevent the reader from confusing the number of maximal minors with the number of coefficients of the final polynomial system.

Lemma 8: repairable

My conclusion: the desired estimate

\\[ \tau\_{\mathrm{cert}}=\operatorname{poly}(\mathcal L) \\]

is credible and can be proved. But I recommend replacing the current proof sketch with a precise coefficient-height lemma, including the corrected \\(\omega+1\\) indexing and a common-denominator argument.

# Part III. Lemma 9: the most important remaining issue

This is the part on which I would be most cautious.

The new report correctly recognizes that the arithmetic complexity of sample-point construction is not the same as the bit complexity of the exact output.

That is a significant improvement.

However, I do not think the current Lemma 9, as written, closes the entire issue.

## 8. Bibliographic verification of the BPR theorem

The report cites:

> Basu–Pollack–Roy, Algorithms in Real Algebraic Geometry, 2nd ed., §13.1, Theorem 13.11.

There is a bibliographic problem here.

The second edition's table of contents places Existential Theory of the Reals in Chapter 15, whereas Chapter 13 is Cylindrical Decomposition Algorithm. Thus the stated chapter and edition do not match.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

doi.org+1



The likely issue is that the section numbering from the first edition has been combined with the second-edition publication information.

This does not invalidate the mathematical result, but it must be corrected.

The relevant second-edition chapter is Chapter 15, Existential Theory of the Reals, with Section 15.1 concerning finding realizable sign conditions.

I would verify the precise theorem number and statement directly from the book before submission. The online bibliographic information confirms the chapter structure, but does not independently establish every quantitative bound quoted in the report.

## 9. Question (i): does sign-condition sampling apply to Boolean combinations?

Yes, provided the theorem really supplies a sample point for every nonempty realizable sign condition.

Suppose the defining polynomials are

\\[ F_1,\ldots,F_s. \\]

A sign condition is an assignment

\\[ \varepsilon\in\\{-1,0,1\\}^s. \\]

Its realization is

\\[ \mathcal R(\varepsilon) = \\{x\in\mathbb R^N: \operatorname{sign}F_i(x)=\varepsilon_i \text{ for every }i\\}. \\]

Your feasible set is defined by

\\[ \sigma\_\omega(HH^{\mathsf T})>0, \\]

\\[ \sigma\_{\omega+1}(\cdots)=0, \\]

and

\\[ B(Y)^{\mathsf T}B(Y)x-\mathbf e_1=0. \\]

This is a Boolean combination of sign conditions.

For example, the first condition requires sign \\(+1\\), while the remaining equations require sign zero.

Therefore the feasible set is a union of realizable sign conditions.

If the union is nonempty, at least one of those sign conditions is nonempty, and its sample point satisfies the formula.

No closedness assumption is needed.

This part is correct.

## 10. Question (ii): sign-condition enumeration and coefficient height

The report's separation of the number of sample points from the height of each sample point is appropriate.

The number of realizable sign conditions is bounded in terms of \\(s,d,N\\), and the sample-point theorem can construct a representative of each relevant sign condition.

However, I would distinguish three quantities:

\\[ \tau\_{\mathrm{input}}, \qquad L\_{\mathrm{representation}}, \qquad T\_{\mathrm{algorithm}}. \\]

- \\(\tau\_{\mathrm{input}}\\): maximum bit length of the integer polynomial coefficients.
- \\(L\_{\mathrm{representation}}\\): total bit length of the algebraic sample-point representations.
- \\(T\_{\mathrm{algorithm}}\\): total bit complexity of constructing the representations.

A bound on the second does not automatically give a bound on the third.

The report currently gives

\\[ \deg\le D^{O(N)} \\]

and

\\[ \text{coefficient height} \le\tau\_{\mathrm{cert}}D^{O(N)}. \\]

These are the right types of bounds to establish, but you need to verify that the precise theorem provides both bounds for the particular sample-point representation being used.

In particular, the output representation must include:

1. The univariate polynomial \\(P\\).
2. The coordinate polynomials \\(Q_0,\ldots,Q_N\\).
3. A specification of the selected real root, for example a Thom encoding or isolating interval.

The third item is not optional. Without it, the univariate representation may identify multiple real points.

The standard real-univariate-representation framework explicitly includes a root specification.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.math.purdue.edu\&sz=32)

math.purdue.edu+1



### 10.1 The output-length calculation

Assume the theorem gives:

\\[ \deg P,\deg Q_i\le\Delta, \\]

and all coefficients have bit length at most \\(H\\).

Then a crude representation-length bound is

\\[ L\_{\mathrm{out}} = O\left( (N+1)(\Delta+1)H + L\_{\mathrm{root}} \right). \\]

Here \\(L\_{\mathrm{root}}\\) is the size of the root specification.

If the root specification has polynomial size in \\(\Delta,H\\), it can be absorbed into the resulting parameter bound.

With

\\[ N=O(\ell^2), \qquad D=O(\ell+1), \\]

and

\\[ \Delta=D^{O(N)}, \\]

we obtain

\\[ \Delta = \exp(O(\ell^2\log(\ell+2))). \\]

Thus the desired output-size shape is plausible:

\\[ \boxed{ L\_{\mathrm{out}} = \exp(O(\ell^2\log(\ell+2))) \operatorname{poly}(\mathcal L). } \\]

But the exact theorem must be checked for the coefficient-height and root-encoding components.

I would not quote the shorter expression

\\[ (\tau+\log s)D^{O(N)} \\]

without explaining that it includes the root specification and all coordinate polynomials.

## 11. Question (iii): reconstructing \\(R\\)

The reconstruction idea is correct, but the current explanation contains unnecessary and potentially misleading language about building a multiplication table.

Suppose the sample point is represented by

\\[ Y_i=\frac{Q_i(\theta)}{Q_0(\theta)}, \\]

where \\(\theta\\) is a specified real algebraic root of \\(P\\).

Every entry of the desired witness is a rational affine-linear combination of the chart coordinates \\(Y_i\\), because:

- \\(Z(Y)\\) is affine in \\(Y\\).
- The section \\(\sigma\\) is rational and linear.
- The basis recovery uses rational matrix operations.

Therefore every witness entry can also be written as

\\[ R\_{ab}=\frac{\widetilde Q\_{ab}(\theta)}{Q_0(\theta)} \\]

after combining the rational coefficients.

The degree does not increase.

The coefficient heights increase by at most the height of the rational preprocessing data and logarithmic factors associated with the number of summands.

There is no need to construct a full multiplication table merely to evaluate these affine-linear expressions.

Recommended correction: replace the multiplication-table paragraph with a direct rational-linear transformation of the coordinate polynomials.

This is simpler and gives a cleaner output-size argument.

## 12. The unresolved problem: arithmetic complexity versus bit complexity

This is the most important issue I found.

The report says:

> Every arithmetic operation acts on coefficients of height at most \\(B\\), at cost \\(\operatorname{poly}(B)\\).

This does not follow from the coefficient-height bound on the input polynomials.

Intermediate quantities in an exact algebraic algorithm can have much larger bit lengths than the original coefficients.

For example, repeated polynomial remainder operations, subresultant calculations, resultants, and algebraic-number operations can produce intermediate coefficients whose sizes are not bounded by the initial coefficient height.

A bound on the final output size does not automatically bound every intermediate representation.

### 12.1 Why this matters

Suppose the arithmetic operation count is

\\[ T\_{\mathrm{arith}} = \exp(O(\ell^2\log(\ell+2))). \\]

This is not, by itself, a bit-complexity bound.

To obtain one, you need either:

- a bit-complexity theorem for the actual sample-point algorithm; or
- an explicit bound on intermediate coefficient sizes and the cost of every arithmetic operation.

I strongly recommend the first route.

Use a theorem that directly gives the bit complexity of constructing the real-algebraic sample points from integer polynomial input.

Then state separately:

\\[ T\_{\mathrm{sample}} \le \exp(O(\ell^2\log(\ell+2))) \operatorname{poly}(\mathcal L). \\]

The output-size bound can be used as a consistency check and for witness reconstruction.

It should not be used as a substitute for an intermediate-height analysis.

### 12.2 A second subtlety: the algorithm may have additional logarithmic factors

The exact bit-complexity theorem may include factors such as

\\[ \log \tau,\quad \log D,\quad \log s, \\]

or polynomial factors in the output representation size.

These are harmless if they are polynomial in the input size and absorbed by the parameter function.

But they must be included in the derivation.

### 12.3 My recommended replacement

I would rewrite the FIND complexity section using two explicitly separated theorems.

Theorem A — Sample-point existence and representation.

For a rational polynomial family with \\(s\\) polynomials, degree at most \\(D\\), \\(N\\) variables and coefficient height \\(\tau\\), every nonempty realizable sign condition has an exactly representable real-algebraic sample point with the stated degree and height bounds.

Theorem B — Bit-complexity of sample-point construction.

The algorithm constructing the required sample points runs in

\\[ (sD)^{O(N)} \operatorname{poly}(\tau) \\]

bit operations, or the exact bound supplied by the chosen reference.

The actual exponent and polynomial factors must match the theorem you cite.

Then substitute

\\[ N\le\ell^2+2\ell,\qquad D\le2\ell+2,\qquad s\le2\ell+2. \\]

This yields the claimed FPT dependence.

I would not retain the current conversion argument as a proof of the bit bound.

Essential before claiming FIND bit-FPT

# Part IV. Lemma 10: preprocessing complexity

## 13. Is the proposed bound plausible?

Yes.

The proposed bound is

\\[ T\_{\mathrm{pre}} = \exp(O(\ell\log(\ell+2))) \operatorname{poly}(\mathcal L). \\]

I believe this is achievable, and in fact much of the preprocessing should be polynomial in \\(\mathcal L\\), with the exponential factor arising from enumerating Grassmannian charts or constructing chart-specific data.

However, the current proof sketch omits some important operations.

### 13.1 Computing \\(V\\)

You need

\\[ V=T\cap(S\times S). \\]

The standard dimension formula is

\\[ \dim(V_1\cap V_2) = \dim V_1+\dim V_2-\dim(V_1+V_2). \\]

In matrix terms, the dimension can be computed by exact row reduction on stacked basis matrices.

This is polynomial-time rational linear algebra.

There is no hidden exponential factor here.

### 13.2 Computing the complement \\(E_Q\\)

This is also polynomial-time.

Given rational basis matrices for \\(W_0\\) and \\(V\\), extend a basis of \\(W_0\\) to a basis of \\(V\\).

This can be done by Gaussian elimination.

The resulting basis matrix has polynomially bounded rational height.

### 13.3 Constructing the charts

The number of charts is

\\[ 2^{m'}\le4^\ell. \\]

Each chart has at most

\\[ t(m'-t)\le\ell^2 \\]

variables.

The affine chart matrix is constructed from the fixed rational basis matrices \\(E_0,E_Q\\).

Thus the total cost of generating all chart descriptions is bounded by

\\[ 4^\ell\operatorname{poly}(\ell,\mathcal L). \\]

This is actually stronger than the proposed

\\[ \exp(O(\ell\log(\ell+2))) \operatorname{poly}(\mathcal L). \\]

### 13.4 What is missing?

There is an important distinction between constructing the chart matrices and constructing the expanded polynomial systems.

The report's Lemma 10 establishes the former.

The expanded system also requires:

- Gram-polynomial construction.
- Cauchy–Binet polynomial construction.
- Polynomial coefficient collection.
- Denominator normalization.

These operations should be included in the preprocessing bound, or explicitly assigned to the decision-algorithm construction cost.

I recommend changing the statement to:

Preprocessing Theorem. All rational linear-algebraic data, reduced coordinates, quotient bases and Grassmannian chart descriptions can be constructed in polynomial time in the input bit length, multiplied by the number of charts.

Then add a separate polynomial-encoding construction lemma.

This avoids claiming that all of the polynomial-system work is already covered by Lemma 10.

Lemma 10: plausible and repairable

# Part V. The \\(\omega=0\\) branch

## 14. The branch is correct

The report asks whether \\(W_0=0\\) and \\(t>0\\) might require an \\(\omega=0\\) branch.

No.

If \\(\omega=0\\), then

\\[ \dim\pi_1(W)=0. \\]

The first condition gives

\\[ \pi_2(W)\subseteq\pi_1(W)=0. \\]

Hence

\\[ W\subseteq0\times0, \\]

so

\\[ W=0. \\]

Therefore

\\[ W_0=0 \\]

and

\\[ t=\dim(W/W_0)=0. \\]

Conversely, if \\(W_0=0\\), choosing \\(W=0\\) gives a feasible realization with no additional rows.

Thus:

\\[ \boxed{ \omega=0\text{ is feasible exactly when }W_0=0, \text{ and its minimum additional row count is }0. } \\]

There is no conflict with positive \\(t\\).

If \\(W_0=0\\) and a feasible extension with \\(t>0\\) exists, it necessarily belongs to a positive-\\(\omega\\) branch.

### 14.1 Feasibility at every order

One wording improvement is necessary.

The statement "feasible iff \\(W_0=0\\)" is true for the \\(\omega=0\\) branch, not for the entire problem.

When \\(W_0=0\\), the zero-dimensional solution is feasible at order \\(r_0\\), and zero padding makes it feasible at every larger row-slot order.

Thus the correct wording is:

> The \\(\omega=0\\) branch is feasible if and only if \\(W_0=0\\). In this case the minimum order is \\(r_0\\), and every larger row-slot order is feasible by zero padding.

That completely settles the issue.

# Part VI. Scope and title

## 15. Should the title carry the row-slot restriction?

My recommendation is yes, if the current title could reasonably be interpreted as solving the general minimum-order problem in the control literature.

The distinction is important enough that I would not rely solely on the abstract and limitations section.

You have two good options.

Option A — Explicit title

Fixed-Parameter Algorithms for the Row-Slot Feasibility and Minimum-Order Problems in Compressed Linear Systems

Option B — Broader title with a subtitle

Fixed-Parameter Tractability of Compressed Linear-System Design: A Row-Slot Formulation

I prefer Option B.

It keeps the main mathematical contribution visible while explicitly limiting the model.

The reduced-order problem need not be solved to make the current paper publishable.

A well-defined, nontrivial problem with a rigorous FPT theorem is a valid research contribution.

The important thing is not to imply that the result automatically applies to

\\[ \operatorname{rank}[C;L]-\operatorname{rank}C. \\]

# Part VII. Additional issues that should be checked before submission

## 16. Polynomial-system size and construction

There is one more distinction worth making.

The report states

\\[ S\_{\mathrm{poly}}=2+2\omega, \qquad D\le2\omega+2, \\]

and

\\[ N\_{\mathrm{var}}\le\ell^2+2\ell. \\]

These bounds are correct under the proposed encoding.

Here is the degree calculation:

| Polynomial                                       | Degree in \\(Y,x\\) |
| ------------------------------------------------ | ------------------- |
| \\(\sigma\_\omega(HH^{\mathsf T})\\)             | \\(\le2\omega\\)    |
| \\(\sigma\_{\omega+1}([H;G][H;G]^{\mathsf T})\\) | \\(\le2\omega+2\\)  |
| Entries of \\(B^{\mathsf T}Bx\\)                 | \\(\le2\omega+1\\)  |

Thus

\\[ D\le2\omega+2. \\]

The number of scalar equations is \\(2\omega\\), because the certificate equation has \\(2\omega\\) coordinates.

The two Gram conditions contribute two additional polynomials.

This part is correct.

### 16.1 Expanded polynomial length

The report should explicitly distinguish the following:

- The mathematical definition of \\(B\\), which can have many rows.
- The computation of \\(B^{\mathsf T}B\\), which can use Cauchy–Binet.
- The expanded polynomial representation supplied to the real-algebraic algorithm.

The Cauchy–Binet formula avoids enumerating all row minors, but it does not mean that the polynomial system can be represented with constant-size data.

An explicit monomial-count estimate is needed.

For \\(N_Y\le\ell^2\\) chart variables and total degree \\(O(\ell)\\), the number of possible monomials is bounded by

\\[ \binom{N_Y+O(\ell)}{O(\ell)} = \exp(O(\ell\log(\ell+2))). \\]

This is compatible with the claimed formula-construction complexity.

I recommend including this calculation.

## 17. Renegar's decision bound

The DEC estimate is structurally convincing:

\\[ (S\_{\mathrm{poly}}D)^{O(N\_{\mathrm{var}})} = \exp(O(\ell^2\log(\ell+2))). \\]

The chart count is

\\[ 4^\ell, \\]

and the number of \\((t,\omega)\\) pairs is polynomial in \\(\ell\\).

Thus the final bound remains

\\[ T\_{\mathrm{DEC}} = \exp(O(\ell^2\log(\ell+2))) \operatorname{poly}(\mathcal L). \\]

One detail: define the coefficient parameter \\(B\\) in Renegar's theorem precisely. If the theorem uses the maximum bit size of integer coefficients, it should be the height after controlled denominator clearing, not the expanded formula length.

Also, the logarithmic factors in the theorem should be interpreted with the small-\\(B\\) cases handled separately.

I do not see a fundamental problem with the DEC asymptotic once Lemmas 8 and 10 are fully proved.

## 18. The parameter-zero case

There is one additional boundary case to state explicitly.

If

\\[ \ell=0, \\]

then the structural theorem forces every feasible \\(W\\) to be zero.

Therefore feasibility is equivalent to

\\[ W_0=0. \\]

The minimum row-slot order is then

\\[ q\_{\min}=r_0 \\]

when \\(W_0=0\\), and \\(+\infty\\) otherwise.

The expression

\\[ \exp(O(\ell^2\log(\ell+2))) \\]

is well-defined at \\(\ell=0\\), but the algorithm should handle this case before entering loops that assume \\(\omega\ge1\\).

This is straightforward and makes the theorem complete for all parameter values.

# Part VIII. Answers to the six questions

| Question                | My answer                                                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 1. Lemma 8              | Correct strategy; one indexing error and missing details in denominator and coordinate bookkeeping                 |
| 2. Lemma 9              | The sign-condition logic is correct; theorem citation and bit-complexity justification need verification           |
| 3. Lemma 10             | Bound is plausible; separate rational preprocessing from expanded polynomial construction                          |
| 4. \\(\omega=0\\)       | Correct; positive \\(t\\) necessarily belongs to a positive-\\(\omega\\) branch                                    |
| 5. Scope                | Row-slot restriction is sufficient; include it in the title or subtitle                                            |
| 6. Submission readiness | The structural theorem is strong, but the complete FIND bit-FPT claim still needs a rigorous computational theorem |

## 19. A corrected version of the central complexity argument

I would replace the current combined complexity argument with the following structure.

Stage 1. Rational preprocessing

Compute

\\[ N,\ S,\ T,\ W_0,\ V,\ E_0,\ E_Q. \\]

Establish polynomial bit complexity and polynomial coefficient heights.

Stage 2. Parameter-dependent enumeration

Enumerate only branches satisfying

\\[ 1\le\omega\le\ell,\qquad \omega+1\le s_0+t\le2\omega. \\]

Enumerate at most

\\[ 4^\ell \\]

Grassmannian charts.

Stage 3. Polynomial-system construction

For each branch construct the \\(2+2\omega\\) polynomial constraints in at most

\\[ \ell^2+2\ell \\]

variables, with degree at most \\(2\ell+2\\).

Prove the coefficient-height and expanded representation-length bounds.

Stage 4. Decision

Apply a real-algebraic decision algorithm with the precise coefficient-height convention.

Obtain the DEC FPT bound.

Stage 5. Optimization

Use monotonicity and the \\(2\ell\\) upper bound to obtain OPT.

Stage 6. Exact construction

Apply a bit-complexity sample-point theorem, retain a root specification, and reconstruct the algebraic witness using rational-linear operations.

Prove the output-size and reconstruction bounds.

This division makes the logical dependencies transparent. It also prevents the arithmetic complexity of one stage from being silently used as the bit complexity of another.

# Part IX. My recommended revision priorities

I would not recommend rewriting the entire paper. The main architecture should be preserved. Instead, concentrate on the following corrections.

P0 — Required for the main theorem

Must fix

- Make every chart matrix explicitly \\(\nu\times2\ell\\), after coordinate reduction.
- Correct the principal-minor count for \\(\sigma\_{\omega+1}\\).
- Explicitly prune branches with \\(\nu>2\omega\\).
- Verify the exact BPR theorem, edition, numbering and output guarantees.
- Establish the bit complexity of sample-point construction directly.
- Include the root specification in the algebraic output representation.\

  P1 — Required for a rigorous complexity proof

  Important
- Complete the rational basis-height proof.
- Give a common-denominator argument.
- Bound the expanded polynomial-system construction.
- Separate preprocessing from chart-specific construction.
- Replace the multiplication-table reconstruction argument with rational-linear evaluation.\

  P2 — Presentation and completeness

  Recommended
- State the \\(\ell=0\\) case separately.
- State the \\(\omega=0\\) branch separately.
- Make the row-slot restriction visible in the title or subtitle.
- Clarify the formalisation status.

# Part X. Final research assessment

I want to distinguish two questions.

Is the underlying mathematical strategy correct?

My answer is yes. I find the following chain convincing:

\\[ \begin{aligned} \text{Original rank conditions} &\longrightarrow W\\\ &\longrightarrow W\subseteq S\times S\\\ &\longrightarrow \dim W\le2\ell\\\ &\longrightarrow \text{Grassmannian charts}\\\ &\longrightarrow \text{Gram and Bézout certificates}\\\ &\longrightarrow \text{real-algebraic decision}. \end{aligned} \\]

This is a coherent and nontrivial mathematical construction.

Has the complete bit-FPT theorem been proved?

Not quite. The main outstanding issue is no longer the structural linear algebra. It is the precise computational theorem supporting FIND and the connection between polynomial input height, intermediate computation, and exact algebraic output.

I would classify the present status as follows:

| Result                             | Current status                                    |
| ---------------------------------- | ------------------------------------------------- |
| Compression and structural theorem | Mathematically established                        |
| Reduction to \\(\ell\\)            | Established, coordinate notation needs correction |
| Bézout equivalence                 | Established, with explicit degree lemma           |
| Polynomial-system dimension        | Established                                       |
| DEC FPT                            | Strong conditional proof                          |
| OPT FPT                            | Follows from DEC                                  |
| FIND arithmetic construction       | Strong conditional proof                          |
| FIND bit complexity                | Requires a stronger computational justification   |
| Lean structural theorem            | Still incomplete                                  |

## 20. The most important strategic recommendation

I would not pursue further structural refinements such as \\(S\_\*\\) at this stage.

Nor would I expand the paper to the reduced-order problem.

The best use of research effort is to close the computational gap.

In particular, I recommend obtaining a precise, independently verified statement of the BPR sample-point theorem in the correct edition, including:

1. Its input model.
2. Its arithmetic or bit-complexity guarantee.
3. Its coefficient-height guarantee.
4. Its univariate representation guarantee.
5. Its real-root specification.
6. Its applicability to arbitrary nonempty sign conditions.

The book's second-edition chapter structure confirms that the current §13.1 citation needs correction.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

doi.org+1



Do not rely on a theorem number copied from the first edition without checking the second-edition statement.

If this computational gap is closed, I would be comfortable treating the main FPT architecture as established, subject to the routine corrections identified above.

# Final verdict

Not yet submission-ready as a complete bit-complexity theorem

The new report represents genuine progress. The structural mathematics is strong, the Bézout encoding is a particularly good idea, and the parameter \\(\ell=\operatorname{rank}(AN)\\) is well justified.

I do not recommend abandoning or fundamentally changing the approach.

The remaining task is to turn the plausible FIND bit-complexity argument into a theorem-backed proof.

That is the main obstacle separating the current result from a submission-ready paper.

My suggested next deliverable is a short technical note, rather than another full paper rewrite, containing corrected Lemmas 8–10 and the exact real-algebraic complexity theorem. Once that is complete, the entire DEC–OPT–FIND argument can be audited as one continuous proof.

I can re-audit that technical note when you upload the revision.