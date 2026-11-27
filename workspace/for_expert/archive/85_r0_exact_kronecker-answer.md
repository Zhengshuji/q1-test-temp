# Review of `85_r0_exact_kronecker.md`: the \\(r=0\\) branch

The report identifies a genuine and important gap in the proposed effective-dimension FPT theorem. Its diagnosis is substantially correct: the polynomial left-inverse construction proves an algebraic degree bound, but it does not, by itself, give a polynomial-time algorithm when \\(q\\) and \\(\omega\\) are unrestricted.

The central distinction is between three claims which must not be conflated:

1. Algebraic characterization: the pencil \\(Q(\lambda)=\lambda X-G\\) has full column rank at every \\(\lambda\in\mathbb C\\).
2. Polynomial-size certificate: if the condition holds, there exists a polynomial matrix \\(S(\lambda)\\) of bounded degree with \\(S(\lambda)Q(\lambda)=I\_\omega\\).
3. Efficient exact decision: one can decide the condition in deterministic polynomial bit complexity, with \\(q,\omega\\) variable and rational input.

The report establishes the first characterization and the second certificate bound. The third is the unresolved algorithmic assertion. In particular, the fact that a Kronecker or staircase algorithm is standard in numerical linear algebra does not, without a separate exact-arithmetic and bit-growth analysis, establish the third claim.

My main recommendation is therefore to separate the \\(r=0\\) question from the proof of the \\(r\geq1\\) FPT theorem, rather than let an unproved exact-Kronecker complexity assertion weaken the entire paper. There is, however, a useful structural simplification specific to this pencil that deserves to be pursued before treating the branch as a long-term open problem: because the pencil is \\(\lambda X-G\\), its constant-rank property can be reduced to the absence of a certain finite-eigenvalue obstruction together with a rank condition on \\(X\\). This gives a more concrete route than computing a complete Kronecker canonical form.

I will distinguish below what follows directly from the uploaded report, what can be derived algebraically, and what still requires a literature or implementation-level complexity proof.&#x20;

85_r0_exact_kronecker.md



## 1. The main result: there is a direct deterministic polynomial-time algorithm

The most important observation is that the polynomial left-inverse certificate can be turned into a finite linear system in its unknown coefficients.

This completely changes the status of the \\(r=0\\) branch. One does not need to compute the Kronecker canonical form, enumerate maximal minors, or invoke a numerical staircase algorithm. The degree bound already established in the report is enough to give an exact deterministic polynomial-time test.

### 1.1 The algebraic criterion

Let

\\[ X,G\in\mathbb Q^{q\times\omega},\qquad Q(\lambda)=\lambda X-G, \\]

where \\(q\geq\omega\\).

The required condition is

\\[ \tag{R0} \rank Q(\lambda)=\omega \qquad\text{for every }\lambda\in\mathbb C. \\]

For \\(\omega\geq1\\), the following are equivalent:

1. Condition (R0) holds.
2. The maximal \\(\omega\times\omega\\) minors of \\(Q(\lambda)\\) have no common complex root.
3. The gcd of those maximal minors in \\(\mathbb Q[\lambda]\\) is \\(1\\).
4. There is a polynomial matrix \\(S(\lambda)\in\mathbb Q[\lambda]^{\omega\times q}\\) such that\
   \\[\
   S(\lambda)Q(\lambda)=I\_\omega.\
   \\]

The equivalence between (R0) and the gcd condition follows because \\(\mathbb C\\) is algebraically closed. Since all the minors have rational coefficients, having a common complex root is equivalent to their having a nonconstant common factor over \\(\mathbb Q\\).

The report already establishes the useful additional fact that, whenever the condition holds, one can choose \\(S\\) with

\\[ \boxed{\deg S\leq 2\omega-2.} \\]

This degree bound is the key to the algorithm below.&#x20;

85_r0_exact_kronecker.md



### 1.2 Expand the polynomial left inverse

Set

\\[ d=2\omega-2. \\]

Write the unknown polynomial matrix as

\\[ S(\lambda)=S_0+S_1\lambda+\cdots+S_d\lambda^d, \qquad S_j\in\mathbb Q^{\omega\times q}. \\]

Substituting into \\(S(\lambda)(\lambda X-G)=I\_\omega\\) gives

\\[ \left(\sum\_{j=0}^d S_j\lambda^j\right)(\lambda X-G) =I\_\omega. \\]

Collecting coefficients of the powers of \\(\lambda\\) yields the following equations:

\\[ \boxed{-S_0G=I\_\omega,} \tag{R0.1} \\]

\\[ \boxed{S\_{j-1}X-S_jG=0, \qquad j=1,\ldots,d,} \tag{R0.2} \\]

and

\\[ \boxed{S_dX=0.} \tag{R0.3} \\]

These equations are linear in the entries of the unknown matrices

\\[ S_0,\ldots,S_d. \\]

That is the decisive point. Although the original condition is phrased in terms of the rank of a matrix pencil at infinitely many complex values of \\(\lambda\\), after the bounded-degree certificate is introduced, deciding it becomes an ordinary rational linear-system feasibility problem.

There are no products between unknown entries of the \\(S_j\\). The matrices \\(X\\) and \\(G\\) are fixed input data.

### 1.3 The algorithm

The resulting test is straightforward.

Algorithm: exact polynomial-left-inverse test

Input: \\(X,G\in\mathbb Q^{q\times\omega}\\).

Step 1. If \\(q<\omega\\), reject: full column rank is impossible.

Step 2. If \\(\omega=0\\), accept: the rank condition is vacuous.

Step 3. Set \\(d=2\omega-2\\), introduce unknown matrices

\\[ S_0,\ldots,S_d\in\mathbb Q^{\omega\times q}. \\]

Step 4. Construct the rational linear system (R0.1)–(R0.3).

Step 5. Solve this system exactly over \\(\mathbb Q\\), using fraction-free Gaussian elimination or another exact rational linear-system algorithm.

Output: Accept if and only if the system is consistent.

No maximal minors need to be generated. In particular, the algorithm does not enumerate the \\(\binom q\omega\\) row subsets that appear in the adjugate proof.

## 2. Correctness proof

The proof is short, but it is important to state both directions carefully.

Theorem (exact \\(r=0\\) test). Let \\(X,G\in\mathbb Q^{q\times\omega}\\), with \\(q\geq\omega\geq1\\). The following are equivalent:

- \\(\rank(\lambda X-G)=\omega\\) for every \\(\lambda\in\mathbb C\\);
- the rational linear system (R0.1)–(R0.3) is consistent.

Proof.

Suppose first that

\\[ \rank(\lambda X-G)=\omega \qquad\forall\lambda\in\mathbb C. \\]

By the polynomial left-inverse characterization and the degree bound established in the report, there exists

\\[ S(\lambda)\in\mathbb Q[\lambda]^{\omega\times q} \\]

with

\\[ S(\lambda)(\lambda X-G)=I\_\omega, \qquad \deg S\leq 2\omega-2. \\]

Write

\\[ S(\lambda)=\sum\_{j=0}^{2\omega-2}S_j\lambda^j. \\]

Comparing coefficients gives exactly (R0.1)–(R0.3). Therefore the linear system is consistent.

Conversely, suppose the linear system is consistent. Choose a solution

\\[ S_0,\ldots,S_d. \\]

Define

\\[ S(\lambda)=\sum\_{j=0}^dS_j\lambda^j. \\]

The coefficient equations imply the polynomial identity

\\[ S(\lambda)(\lambda X-G)=I\_\omega. \\]

For every \\(\lambda_0\in\mathbb C\\), evaluation gives

\\[ S(\lambda_0)(\lambda_0X-G)=I\_\omega. \\]

Thus \\(\lambda_0X-G\\) has a left inverse and consequently has full column rank:

\\[ \rank(\lambda_0X-G)=\omega. \\]

Since \\(\lambda_0\\) was arbitrary, the required condition holds for every complex \\(\lambda\\). \\(\square\\)

This proof also shows why the algorithm is exact: it accepts precisely when the polynomial identity has a solution, not when a numerical approximation suggests that the pencil has full rank.

## 3. Exact bit complexity

The algorithm is not merely polynomial in the number of arithmetic operations. It also has polynomial bit complexity for rational input.

Let \\(\mathcal L_0\\) denote the total binary encoding length of \\(X\\) and \\(G\\).

### 3.1 Number of unknowns

There are \\(d+1=2\omega-1\\) unknown matrices, each of size \\(\omega\times q\\). Therefore the number of scalar unknowns is

\\[ N\_{\mathrm{var}} =(2\omega-1)q\omega =O(q\omega^2). \\]

### 3.2 Number of equations

Each matrix equation contributes \\(\omega^2\\) scalar equations.

- (R0.1) contributes \\(\omega^2\\).
- (R0.2) contributes \\(d\omega^2=(2\omega-2)\omega^2\\).
- (R0.3) contributes \\(\omega^2\\).

Hence the total number of scalar equations is

\\[ N\_{\mathrm{eq}} =(d+2)\omega^2 =2\omega^3. \\]

Thus the coefficient matrix of the rational linear system has

\\[ O(q\omega^2+\omega^3) \\]

rows and columns, up to the usual rectangular-system convention.

In particular, its dimensions are polynomial in \\(q\\) and \\(\omega\\).

### 3.3 Coefficient bit lengths

The coefficients in the linear system are drawn from the entries of \\(X\\) and \\(G\\), together with \\(0\\), \\(1\\), and \\(-1\\).

A common denominator can be formed by multiplying the denominators of all input entries. Its binary length is at most the sum of the binary lengths of those denominators, hence \\(O(\mathcal L_0)\\).

Multiplying the equations by this common denominator gives an integer linear system whose entries have binary length polynomial in \\(\mathcal L_0\\). The right-hand side also has polynomial bit length.

### 3.4 Exact elimination

The consistency of an integer or rational linear system can be decided using exact Gaussian elimination, with fraction-free elimination being a particularly appropriate choice.

The relevant bit-complexity observation is that intermediate determinants and minors of an integer matrix of dimension \\(M\\), with entries of bit length at most \\(B\\), have bit lengths bounded polynomially in \\(M\\) and \\(B\\). For example, Hadamard's inequality gives a bound of the form

\\[ O\bigl(M(B+\log M)\bigr) \\]

for the bit length of such determinants.

Consequently, exact elimination has polynomial bit complexity in the matrix dimensions and input bit length.

Taking

\\[ M=O(q\omega^2+\omega^3), \\]

we obtain

\\[ \boxed{ T\_{r=0} =\operatorname{poly}(q,\omega,\mathcal L_0). } \\]

This is a deterministic polynomial-time algorithm over rational input.

I would state the bound in this polynomial form unless the paper needs an explicit exponent. The important point for Theorem 3 is that it is polynomial in the input size, not that it has an especially small polynomial exponent.

### 3.5 Why this is stronger than the proposed Kronecker route

The report's concern about exact Kronecker computation is well motivated. The classical Beelen–Van Dooren paper gives an \\(O(m^2n)\\) algorithm for computing the Kronecker structure of a pencil and emphasizes numerical stability through unitary transformations. That is a numerical linear-algebra result, not, by itself, a rational bit-complexity theorem.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直接



Likewise, the Storjohann–Labahn work gives a Las Vegas algorithm for the Smith normal form of a square nonsingular polynomial matrix, with an expected bit-operation bound. It is relevant background, but it is unnecessary to rely on it for the present problem.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://uwspace.uwaterloo.ca\&sz=32)

uwspace.uwaterloo.ca+1



The direct linear-system construction avoids these issues:

- no numerical rank thresholds;
- no orthogonal transformations;
- no randomized choices;
- no computation of the full Kronecker form;
- no enumeration of maximal minors;
- no need to compute a polynomial Smith form.

It also produces a useful witness: if the test accepts, the solution matrices \\(S_j\\) explicitly provide a polynomial left inverse.

## 4. An important correction to the report's Kronecker description

There is a point in Part II of the report that I recommend correcting, independently of the new algorithm.

The report says that the condition is equivalent to the Kronecker canonical form having neither a right singular block nor a regular block. As written, this is too strong.

The condition

\\[ \rank Q(\lambda)=\omega \qquad\forall\lambda\in\mathbb C \\]

does not exclude regular blocks corresponding to infinite eigenvalues.

For example, consider the \\(1\times1\\) pencil

\\[ Q(\lambda)=1. \\]

It has rank one for every finite complex \\(\lambda\\), so it satisfies the required condition. Yet it is a regular pencil, and in the usual Kronecker terminology it has an infinite elementary divisor of size one.

The appropriate structural interpretation is:

- Right singular blocks must be absent. Such blocks give a nontrivial right polynomial nullspace and prevent full column normal rank.
- Finite regular elementary-divisor blocks must be absent. Such blocks produce a finite value of \\(\lambda\\) at which the rank drops.
- Left singular blocks may be present. They are compatible with full column rank at every finite \\(\lambda\\).
- Infinite regular elementary-divisor blocks may be present. They do not produce a rank drop at any finite complex value.

The distinction is consistent with the standard description of Kronecker form, in which finite and infinite elementary divisors are separate types of regular blocks.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://link.springer.com\&sz=32)

Springer+1



I suggest replacing the report's sentence with:

> The pencil has full column rank at every finite complex value if and only if its Kronecker form contains no right singular blocks and no finite regular elementary-divisor blocks. Left singular blocks and infinite regular elementary-divisor blocks are permitted.

This correction is not needed for the direct algorithm, but it is important if the Kronecker interpretation remains in the paper.

## 5. Answers to the report's eleven questions

### III.1 Exact algorithm

Question 1. Is there a deterministic polynomial-time algorithm in exact rational arithmetic?

Yes. The bounded-degree polynomial-left-inverse certificate yields a deterministic rational linear-system test.

Question 2. What is the reference and bit complexity? Does it avoid enumerating maximal minors?

The direct construction above is a proof and algorithm for this particular problem. It does not need to be attributed to a published Kronecker algorithm.

It avoids enumerating maximal minors entirely. The number of unknowns is \\(O(q\omega^2)\\), the number of equations is \\(2\omega^3\\), and exact rational elimination gives polynomial bit complexity.

I would not claim that a particular published Kronecker algorithm has this exact bit bound unless its source explicitly proves it. Instead, present the linear-system algorithm as the paper's own proposition, derived from the degree bound.

Question 3. Can orthogonal transformations be replaced by exact Gaussian elimination?

That replacement is not a sufficiently justified way to convert a numerical staircase algorithm into an exact bit-complexity theorem. Numerical algorithms may depend on stability, thresholding, and properties of orthogonal transformations. Merely replacing rank decisions with exact Gaussian elimination does not automatically prove that the entire algorithm remains correct or has polynomial bit complexity.

Fortunately, no such replacement is needed here.

### III.2 Acceptable weaker statements

Question 4. If no exact Kronecker reference is available, can Theorem 3 be restricted to \\(r\geq1\\)?

Yes, as a fallback. But with the direct test above, I do not recommend leaving this restriction in place.

Question 5. Would a randomized polynomial-time test be acceptable?

It would be an acceptable weaker result if correctly stated, but it is unnecessary. The proposed algorithm is deterministic and exact.

Question 6. Is a numerical Kronecker algorithm sufficient if rank decisions are exact?

No. Exact rank decisions alone do not supply a complete bit-complexity proof for all transformations, intermediate objects, and termination conditions. The paper should give an exact algorithm with a bit-complexity argument. The direct linear-system algorithm supplies exactly that.

### III.3 Structural alternatives

Question 7. Is there a direct test using only ranks of constant matrices derived from \\(X,G\\)?

There is a direct finite-dimensional test, but I would formulate it as a linear-system consistency test rather than claim that a small fixed collection of ordinary constant-matrix ranks suffices.

The coefficient equations (R0.1)–(R0.3) form a constant rational matrix equation in the entries of \\(S_0,\ldots,S_d\\). Its consistency can be decided by comparing the rank of its coefficient matrix with the rank of its augmented matrix.

Thus the infinitely many spectral conditions reduce to the rank consistency of one explicitly constructed rational matrix.

Question 8. Can the \\(r=0\\) case be absorbed into the \\(r\geq1\\) theorem by adding a free row?

I would not recommend this. Adding a free observer row changes the feasible design space, and without a carefully proved reduction it may change feasibility. There is no need to introduce such a reduction when the \\(r=0\\) case already has a polynomial-time solution.

Question 9. Does degree one allow a simpler algorithm?

Yes, in the sense that the polynomial left-inverse certificate has a degree bound linear in \\(\omega\\), and its coefficient equations are linear in the unknown certificate coefficients.

The decisive feature is not simply that the input pencil has degree one. It is the combination of:

1. a polynomial left-inverse characterization;
2. an explicit degree bound;
3. linearity of the identity \\(SQ=I\\) in the unknown entries of \\(S\\).

This combination turns the decision problem into rational linear algebra.

### III.4 Consequences for the paper

Question 10. If the \\(r=0\\) branch remains open, is the paper still publishable with \\(r\geq1\\)?

It could be, provided the theorem statement is explicitly restricted and the contribution remains substantial. But the direct test removes the reason to make that restriction.

Question 11. Should the paper present \\(r=0\\) as open or wait for exact Kronecker complexity?

Neither. The appropriate next step is to add the linear-system construction and its bit-complexity proof to the paper. There is no need to wait for a separate exact-Kronecker complexity result.

## 6. Consequences for the effective-dimension FPT theorem

This is the most consequential implication for the wider project.

Recall the effective parameter

\\[ \kappa\_{\mathrm{obs}}=r\\,d_0, \qquad d_0=\rank[N\ AN]. \\]

When \\(r=0\\),

\\[ \kappa\_{\mathrm{obs}}=0. \\]

The free-row parametrization disappears, but the fixed compressed pencil remains:

\\[ Q(\lambda)=\lambda X-G. \\]

The algorithm above decides its spectral condition in deterministic polynomial time in the input size. Therefore the zero-parameter case is polynomial-time solvable.

This is precisely what an FPT theorem needs at parameter value zero. There is no exceptional unresolved branch.

### 6.1 Recommended form of Theorem 3

Subject to the other obligations already identified in the paper review—especially the field convention, the exact construction of the compressed data, and the coefficient-size analysis—I recommend stating the theorem without an \\(r\geq1\\) restriction:

> Theorem 3 (effective-dimension fixed-parameter tractability).\
> The observer decision problem is decidable by a deterministic algorithm in time\
> \\[\
> f(\kappa\_})\operatorname(\mathcal L),\
> \\]\
> where\
> \\[\
> \kappa\_}\
> \=r,\rank[N\ AN]\
> \\]\
> and \\(\mathcal L\\) is the binary input length.

The proof should have two explicitly separated cases.

Case 1: \\(r=0\\). Use the polynomial-left-inverse coefficient system above. The running time is

\\[ \operatorname{poly}(\mathcal L). \\]

Case 2: \\(r\geq1\\). Use the free-pair parametrization, the compressed spectral certificate, and the Cauchy–Binet construction from the main FPT argument. The number of variables, determinant orders, and formula sizes are bounded by functions of \\(\kappa\_{\mathrm{obs}}\\), with polynomial dependence on the input length.

This gives the clean combined estimate

\\[ T(\mathcal I) \leq \begin{cases} \operatorname{poly}(\mathcal L), & r=0,\\\\[2mm] f(\kappa\_{\mathrm{obs}}) \operatorname{poly}(\mathcal L), & r\geq1. \end{cases} \\]

After enlarging \\(f\\) if necessary, this is one FPT bound valid for all \\(r\geq0\\).

### 6.2 Why the zero case is especially important

There is a conceptual advantage to resolving \\(r=0\\) explicitly.

An FPT theorem is intended to cover all parameter values, including zero. If the proof silently assumes \\(r\geq1\\), a referee may reasonably ask whether the parameterization is genuinely complete or whether the algorithm has an unhandled boundary case.

By proving the zero case separately, the paper demonstrates that the parameter has the intended interpretation: when there are no free observer rows, the remaining fixed spectral test is tractable without any parameter-dependent search.

This strengthens the theorem's presentation.

## 7. Suggested manuscript revisions

I recommend adding a short subsection to the algorithmic part of the paper, rather than expanding the discussion of numerical Kronecker algorithms.

### Proposed subsection title

The zero-free-row case: an exact polynomial-time pencil test

A suitable structure is:

1. State the \\(r=0\\) problem in terms of \\(Q(\lambda)=\lambda X-G\\).
2. Recall the full-column-rank / polynomial-left-inverse equivalence.
3. State the degree bound \\(\deg S\leq2\omega-2\\).
4. Expand the polynomial identity and display the linear system.
5. Prove the equivalence between the linear-system consistency and the spectral condition.
6. Give the variable and equation counts.
7. Establish polynomial bit complexity using exact rational elimination.
8. Close with the \\(r=0\\) branch of Theorem 3.

The key equations should appear in the main text, not be buried in an appendix. They are simple enough to be understood quickly and are central to closing the algorithmic gap.

### Suggested theorem text

The following is a manuscript-ready formulation, subject to matching notation with the rest of the paper.

**Proposition (Exact polynomial-time test for the zero-free-row case).**\
Let (X,G\in\mathbb Q^{q\times\omega}), where (q\geq\omega\geq1), and set\
[\
Q(\lambda)=\lambda X-G.\
]\
Suppose that whenever (Q) has full column rank at every (\lambda\in\mathbb C), it admits a polynomial left inverse (S\in\mathbb Q[\lambda]^{\omega\times q}) of degree at most (2\omega-2).

Then deciding whether\
[\
\operatorname{rank}Q(\lambda)=\omega\
\qquad\text{for every }\lambda\in\mathbb C\
]\
is possible in deterministic polynomial bit complexity.

Indeed, write\
[\
S(\lambda)=\sum\_{j=0}^{2\omega-2}S_j\lambda^j,\
\qquad S_j\in\mathbb Q^{\omega\times q}.\
]\
The identity (S(\lambda)Q(\lambda)=I\_\omega) is equivalent to the rational linear system\
[\
-S_0G=I\_\omega,\
]\
[\
S\_{j-1}X-S_jG=0,\
\qquad j=1,\ldots,2\omega-2,\
]\
and\
[\
S\_{2\omega-2}X=0.\
]\
This system has (O(q\omega^2)) scalar unknowns and (O(\omega^3)) scalar equations. It is consistent if and only if (Q(\lambda)) has full column rank for every complex (\lambda). Its consistency can be decided by exact rational linear algebra in time polynomial in (q,\omega), and the input bit length.

For (\omega=0), the spectral condition is vacuous and the instance is accepted; for (q<\omega), it is rejected.

One small writing improvement: if the degree-bound lemma is proved earlier in the paper, cite it directly rather than restating it as an assumption. The proposition should then be an unconditional consequence of that lemma.

## 8. Remaining technical checks

Although the main algorithmic obstruction is resolved, several details should be checked before the manuscript is frozen.

### 8.1 Make the degree-bound proof explicit enough

The algorithm depends critically on the degree bound. The paper should make clear why the bound applies to the rectangular pencil \\(Q\in\mathbb Q[\lambda]^{q\times\omega}\\), not only to square pencils.

The adjugate construction provides the required argument. For every \\(\omega\\)-element row subset \\(I\\), let \\(E_I\\) be the corresponding row-selection matrix and write

\\[ Q_I=E_IQ,\qquad f_I=\det Q_I. \\]

Then

\\[ \operatorname{adj}(Q_I)E_IQ=f_I I\_\omega. \\]

If the maximal minors have gcd one, choose polynomial coefficients \\(g_I\\) satisfying

\\[ \sum_I g_I f_I=1. \\]

It follows that

\\[ S(\lambda) =\sum_I g_I(\lambda)\operatorname{adj}(Q_I(\lambda))E_I \\]

is a polynomial left inverse.

Since each \\(f_I\\) has degree at most \\(\omega\\), the Bezout coefficients can be chosen with degree less than \\(\omega\\); the adjugate entries have degree at most \\(\omega-1\\). Thus

\\[ \deg S\leq 2\omega-2. \\]

The construction may involve exponentially many row subsets, but that is irrelevant to the existence proof and the degree bound. The algorithm does not construct this particular sum. It searches directly for a polynomial left inverse of the guaranteed bounded degree by solving the linear system.

This distinction deserves one explicit sentence in the manuscript.

### 8.2 Keep the coefficient field consistent

The proposition above assumes rational \\(X,G\\). That is consistent with an exact bit-model algorithm.

If the paper's observer variables or input matrices are complex, the realification convention must be applied consistently. In the \\(r=0\\) case, one can still solve the coefficient system over \\(\mathbb Q(i)\\) when the entries lie in \\(\mathbb Q(i)\\), or realify it into a rational linear system in real and imaginary parts.

For arbitrary complex input data without a finite exact encoding, a Turing bit-complexity statement is not meaningful. The paper should state its input field explicitly.

### 8.3 Distinguish an algorithm from a certificate-size statement

The existence of a bounded-degree left inverse is not itself an algorithm. The new argument supplies the missing bridge:

\\[ \text{bounded-degree certificate} \quad\Longrightarrow\quad \text{polynomial-size linear system} \quad\Longrightarrow\quad \text{deterministic exact decision}. \\]

This logical chain should be stated explicitly. It is the actual algorithmic contribution of the \\(r=0\\) subsection.

### 8.4 The algorithm may also produce a witness

When the linear system is consistent, exact elimination can return a solution \\(S_0,\ldots,S_d\\). Hence the procedure is not merely a yes/no test. It constructs a polynomial left inverse

\\[ S(\lambda)=\sum\_{j=0}^{2\omega-2}S_j\lambda^j. \\]

This is useful for verification and for possible later extensions. The returned witness can be checked simply by multiplying the two polynomial matrices and verifying that the product is \\(I\_\omega\\).

## 9. Updated assessment of the project

The new result changes my assessment of the paper's status.

| Issue from the earlier review                      | Status after this report and the new construction            |
| -------------------------------------------------- | ------------------------------------------------------------ |
| Algebraic characterization of the \\(r=0\\) branch | Established                                                  |
| Polynomial left-inverse degree bound               | Established in the report                                    |
| Avoiding maximal-minor enumeration                 | Resolved by the coefficient linear system                    |
| Deterministic exact rational algorithm             | Resolved                                                     |
| Polynomial bit complexity                          | Follows from exact rational linear-system solving            |
| Need for a numerical Kronecker algorithm           | Eliminated                                                   |
| Need to restrict Theorem 3 to \\(r\geq1\\)         | No                                                           |
| Kronecker interpretation in the report             | Needs the correction concerning infinite elementary divisors |

The principal earlier concern about the effective-dimension FPT theorem was that \\(\kappa\_{\mathrm{obs}}=0\\) when \\(r=0\\), while the fixed pencil could still have dimensions growing with the input. That concern is now resolved: the fixed pencil can be tested in polynomial time independently of \\(\kappa\_{\mathrm{obs}}\\).

This is a meaningful improvement, not merely a cosmetic clarification.

## 10. Recommended next steps

I would now prioritize the following work.

1. Insert the exact linear-system algorithm.

   Add the proposition and proof above. This should close the \\(r=0\\) branch in the main algorithmic argument.
2. Correct the Kronecker-form sentence.

   Distinguish finite regular elementary divisors from infinite ones. Do not say that all regular blocks must be absent.
3. Revisit Theorem 3.

   Remove any restriction \\(r\geq1\\), and explicitly divide its proof into the \\(r=0\\) and \\(r\geq1\\) cases.
4. Complete the global bit-complexity audit.

   The new proposition settles the \\(r=0\\) part, but the full FPT theorem still needs the coefficient-size analysis for the \\(r\geq1\\) construction and the relevant real-algebraic decision procedure.
5. Update the project status report.

   The statement that the exact rational bit-complexity of the \\(r=0\\) test is an open point should be replaced with the new deterministic polynomial-time result.

## Final conclusion

The report correctly identified the weakness of relying on numerical Kronecker algorithms and on the adjugate construction alone. But the missing exact algorithm can be obtained directly from the already established degree bound.

The key observation is:

\\[ \boxed{ \begin{aligned} &\rank(\lambda X-G)=\omega \quad\forall\lambda\in\mathbb C\\\ &\quad\Longleftrightarrow\quad \exists S_0,\ldots,S\_{2\omega-2} \text{ satisfying a finite rational linear system.} \end{aligned} } \\]

That system has polynomial dimensions and can be solved deterministically with polynomial bit complexity.

My recommendation is to treat the \\(r=0\\) branch as resolved, not as an open problem. Add the proposition, correct the Kronecker interpretation, and retain the full \\(r\geq0\\) statement of the effective-dimension FPT theorem—subject, of course, to the remaining field-consistency and bit-complexity checks elsewhere in the paper.

This is the cleanest route: it avoids an unnecessary detour into exact Kronecker canonical form computation and gives the paper a stronger, more self-contained algorithmic result.