# Mathematical audit of `50_rp_free_fibre_and_all_bad.md`

This report contains two important advances: a credible route to an RP result for \\(k=\omega\\), and a substantially sharper free-fibre criterion for \\(q=3,\omega=2\\). The constrained-stratum calculation is also a valid and useful exact obstruction.

There is, however, one serious error in the final conclusion of II.3: proving that the entire \\(\omega=2\\) stratum at \\(q=3\\) is bad does not prove that \\(q=3\\) is infeasible. The report does not exclude the \\(\omega=1\\) stratum. In fact, the data given in II.3 admit an augmentation with only \\(q=2\\) rows. Thus the claim \\(q\_{\min}=4\\) is not supported and, for the stated data, is false.

I will distinguish this decisive correction from the results that survive, and then answer the three questions.

## 1. The RP theorem for \\(k=\omega\\)

### 1.1 The main argument is sound

The structural argument in II.1 is correct.

When \\(k=\omega\\), the matrix \\(H(R)\\) has full column rank \\(k\\), so

\\[ \ker H(R)=\\{0\\}\subseteq\ker H_A(R). \\]

Thus (5a) is automatic on this rank stratum.

The admissible parameter domain

\\[ D=\\{R:\rank H(R)=k,\ \rank L(R)=q\\} \\]

is a Zariski-open subset of the affine parameter space. If nonempty, it is irreducible. By the closedness theorem for the bad spectral locus, either

\\[ D\subseteq\mathcal B \\]

or

\\[ D\setminus\mathcal B \\]

is nonempty and Zariski open dense in \\(D\\).

Consequently,

\\[ \boxed{ \exists R\in D\text{ good} \iff \text{the generic point of }D\text{ is good}. } \\]

This is the correct structural basis for a one-sided randomized algorithm.

### 1.2 The lemma on two constant linear combinations is true, but its proof needs repair

The report states that if the gcd of all minors \\(m_i\\) is one over \\(\mathbb Q(R)[\lambda]\\), then two constant rational linear combinations \\(f,g\\) can be chosen with

\\[ \gcd(f,g)=1. \\]

The lemma is correct. However, the proof in lines 59–62 has a logical gap: it invokes a finite-union-of-proper-subspaces argument over all irreducible polynomials \\(p\\), but there can be infinitely many such \\(p\\). A finite-union argument cannot be applied to that infinite collection.

There is a simple repair.

Let

\\[ V_0=\operatorname{span}\_{\mathbb Q}\\{m_1,\ldots,m_N\\}. \\]

Choose any nonzero \\(f\in V_0\\). If \\(f\\) is a nonzero constant in \\(\lambda\\), the conclusion is immediate. Otherwise, \\(f\\) has only finitely many irreducible factors

\\[ p_1,\ldots,p_s \\]

in \\(\mathbb Q(R)[\lambda]\\).

For each \\(p_j\\), define

\\[ V\_{p_j}=\\{g\in V_0:p_j\mid g\\}. \\]

Because the gcd of all \\(m_i\\) is one, not all \\(m_i\\) are divisible by \\(p_j\\). Hence \\(V\_{p_j}\\) is a proper \\(\mathbb Q\\)-linear subspace of \\(V_0\\).

Now there are only finitely many subspaces \\(V\_{p_j}\\). Since \\(\mathbb Q\\) is infinite, they cannot cover \\(V_0\\). Choose

\\[ g\in V_0\setminus\bigcup\_{j=1}^s V\_{p_j}. \\]

Then no irreducible factor of \\(f\\) divides \\(g\\), and therefore

\\[ \gcd(f,g)=1. \\]

This sequential argument is the appropriate proof to put in the paper.

### 1.3 The resultant bound is appropriate

Once \\(f,g\in\mathbb Q[R,\lambda]\\) have been chosen with gcd one over \\(\mathbb Q(R)[\lambda]\\), their resultant is a nonzero polynomial in \\(R\\):

\\[ \mathcal R(R)=\operatorname{Res}\_{\lambda}(f,g)\ne0. \\]

Each \\(k\times k\\) minor has degree at most \\(k\\) in the entries of \\(R\\), and degree at most \\(k\\) in \\(\lambda\\). The Sylvester matrix has size at most \\(2k\\). Thus

\\[ \deg_R\mathcal R\le 2k^2 \\]

is a valid crude bound, provided the resultant is formed using the actual generic \\(\lambda\\)-degrees of \\(f\\) and \\(g\\).

If a specialization \\(R_0\\) is bad, all maximal minors have a common finite root. The same root is shared by \\(f(R_0,\lambda)\\) and \\(g(R_0,\lambda)\\), so

\\[ \mathcal R(R_0)=0. \\]

The rank conditions are also covered by nonzero witness minors \\(h,\ell\\), with degrees bounded by \\(k\\) and \\(q\\), respectively. Therefore the exceptional set is contained in the zero set of a nonzero polynomial of degree at most

\\[ 2k^2+k+q. \\]

The proposed grid size

\\[ N=2(2k^2+k+q) \\]

then gives the stated Schwartz–Zippel false-negative bound of at most \\(1/2\\).

One small presentational point: \\(h\\) and \\(\ell\\) need not be known to the algorithm. They are nonzero witness polynomials used in the analysis. The algorithm itself checks the rank conditions directly. That is entirely legitimate.

### 1.4 Rational sampling is justified

The report's rational-point observation is correct.

All input data are rational, so the relevant open sets are defined over \\(\mathbb Q\\). If the good locus is nonempty over \\(\mathbb C\\), it is a nonempty Zariski-open subset of affine parameter space defined over \\(\mathbb Q\\). Since \\(\mathbb Q^s\\) is Zariski dense in \\(\mathbb C^s\\), this open set contains rational points.

For the randomized algorithm, integer grid points are even more convenient: they give explicit coefficient-size bounds.

### 1.5 The remaining issue is the polynomial bit-complexity citation

The report is right to identify this as the step needing a precise external theorem. The algebraic argument alone does not establish a polynomial-time algorithm for computing the determinantal divisor when \\(q,k\\) vary.

I would not regard author names and publication years alone as a complete proof. The paper should specify the exact computational statement being used: polynomial-matrix Smith form or determinantal-divisor computation over \\(\mathbb Q[\lambda]\\), with complexity polynomial in matrix dimensions, polynomial degrees, and coefficient bit sizes.

I would also explicitly account for the bit sizes introduced by:

- computing a rational basis \\(N_K\\) of \\(K\\);
- forming \\(H(R_0)\\) and \\(H_A(R_0)\\);
- sampling integer entries of magnitude at most \\(N\\);
- computing the determinantal divisor.

The input condition \\(q\\) unary is useful because it ensures the sampled matrix dimensions are polynomially bounded in the input length.

Assessment: the RP proof is structurally sound, and its specialization bound is now essentially complete. The remaining task is to cite and state a polynomial-bit-complexity result that applies to the exact determinantal-divisor computation being performed. With that result and the sequential repair of the lemma, the RP statement can be made unconditional in the paper. ZPP still does not follow.

## 2. The free-fibre criterion in II.2

### 2.1 The proposed classification is plausible and, with the stated standing assumptions, appears correct

The normal rank

\\[ \rho=\operatorname{nrank}\_{\mathbb C(\lambda)}        (\lambda U_0-V_0) \\]

is the right invariant for this classification. It captures the generic rank of the fixed top-block pencil, which is exactly what the completion rows must augment.

The earlier invariant \\(\dim(E+F_0)\\) is not enough. The report's counterexample

\\[ U_0=\begin{pmatrix}1&0\\\0&0\end{pmatrix}, \qquad V_0=\begin{pmatrix}0&1\\\0&0\end{pmatrix} \\]

has \\(\dim(E+F_0)=2\\), but its fixed pencil has normal rank one. One free row cannot complete it for every \\(\lambda\\). This correction is important.

The four cases also have a natural interpretation:

| Fixed-pencil normal rank                                       | Completion mechanism                                                                                                                                |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| \\(\rho=2\\), no scalar proportionality \\(V_0=\lambda_0U_0\\) | Fixed pencil is generically rank two; free rows repair its finitely many finite rank drops.                                                         |
| \\(\rho=2\\), \\(V_0=\lambda_0U_0\\)                           | Fixed pencil vanishes at \\(\lambda_0\\); two free rows are needed there.                                                                           |
| \\(\rho=1\\)                                                   | One free row cannot avoid a rank drop over all complex \\(\lambda\\); two free rows can generically do so.                                          |
| \\(\rho=0\\)                                                   | No fixed pencil contribution; two free rows give a square pencil with a determinant root, while three free rows can give a good rectangular pencil. |

This is a meaningful classification, not just a list of experimental cases.

There are, however, two points that should be strengthened before presenting it as a complete theorem.

### 2.2 Case (c) needs an incidence-dimension argument

In case (c), \\(\rho=1\\) and \\(m=2\\). The report says that at every \\(\lambda\\), at least one of the two free rows can be chosen outside the line \\(L(\lambda)\\), and refers to finitely many proper conditions. But \\(\lambda\\) ranges over all of \\(\mathbb C\\), so the exceptional conditions are not simply a finite list.

The intended conclusion is still valid, but the clean proof is an incidence argument.

Write

\\[ a(\lambda)=\lambda U_0-V_0. \\]

For all but finitely many \\(\lambda\\), its row space is a line \\(L(\lambda)\subset S\\). For two free rows, put

\\[ b_i(\lambda)=\lambda x_i-y_i,\qquad i=1,2. \\]

At a fixed \\(\lambda\\) for which \\(a(\lambda)\ne0\\), the condition

\\[ b_1(\lambda),b_2(\lambda)\in L(\lambda) \\]

imposes one independent linear condition on each of the two independently chosen pairs \\((x_i,y_i)\\). Thus it has codimension two in the eight-dimensional parameter space

\\[ (S\times S)^2. \\]

Allowing \\(\lambda\\) to vary adds one dimension. The incidence variety therefore has dimension at most seven, so its projection cannot fill the eight-dimensional parameter space.

At any exceptional \\(\lambda_0\\) where \\(a(\lambda_0)=0\\), impose separately

\\[ b_1(\lambda_0),b_2(\lambda_0)\text{ linearly independent}. \\]

This is a nonempty Zariski-open condition. There are only finitely many such exceptional values.

Finally, the requirement \\(\rank H=2\\) is also a nonempty open condition under \\(m=2\\) and \\(m\ge 2-\dim E\\). The intersection of these nonempty open conditions in the irreducible parameter space is nonempty.

This supplies the missing rigorous argument for case (c). It is preferable to the current phrase “finitely many proper conditions.”

### 2.3 The full-row-rank condition on \\(L\\) should be addressed explicitly

The criterion is stated for an augmentation \\(L=[L_0;R]\\) that must have full row rank. The proof mostly works with the pairs

\\[ (x_i,y_i)=(R_iN_K,R_iAN_K). \\]

In the free case, \\(\ker T=0\\) makes the map from a row covector \\(R_i\\) to this pair surjective. But surjectivity alone does not automatically state that the selected lifts, together with the fixed rows of \\(L_0\\), are independent.

This can be handled cleanly, and does not appear to require a new numerical condition, provided the standing hypothesis

\\[ \rank L_0=r \\]

is included.

Indeed, let

\\[ \Psi(\ell)=(\ell N_K,\ell AN_K). \\]

The top rows of \\(L_0\\) map into \\(S\times S\\), a four-dimensional space. Their image has dimension at most \\(r\\). Since \\(m=3-r\\), the quotient of \\(S\times S\\) by that top-row image has dimension at least

\\[ 4-r=m+1. \\]

Thus one can choose \\(m\\) bottom pairs whose images are linearly independent modulo the image of the top rows. Their actual row-covector lifts are then independent modulo the span of \\(L_0\\). This guarantees \\(\rank L=3\\).

The required independence is an open condition on the bottom pairs. The spectral-good conditions in the four cases are also open once a good completion has been exhibited. Since the parameter space is irreducible, the two nonempty open sets intersect.

I recommend adding this argument once, before the four cases, rather than repeatedly inserting full-row-rank checks into each case.

If \\(\rank L_0=r\\) is not already an assumption in the paper, it must be added to the theorem: otherwise full row rank of \\(L\\) is impossible whenever the fixed rows of \\(L_0\\) are dependent.

### 2.4 Necessity and sufficiency, case by case

My assessment of the four alternatives is:

- (a): Correct. If \\(V_0\ne\lambda U_0\\) for every \\(\lambda\\), a finite rank drop of a normal-rank-two fixed pencil has rank exactly one, so one free row can repair it. If there are no free rows, the fixed pencil itself must be good.
- (b): Correct. At \\(\lambda_0\\), all fixed rows vanish, so two free rows must be independent there. Away from \\(\lambda_0\\), the fixed rows already have rank two.
- (c): The necessity argument is sound. With one free row and \\(\rank U_0=1\\), the determinant of the fixed row and free row has a nonzero quadratic leading coefficient, so it has a complex root. The sufficiency needs the incidence proof above.
- (d): Correct. With two free rows and no fixed contribution, the resulting square pencil has a nonzero quadratic determinant and therefore a finite complex root. With three free rows, the displayed example is a valid witness; its three maximal minors have gcd one.

The explicit witness in (d) is correctly computed:

\\[ 3\lambda^2+\lambda-2,\qquad -\lambda-1,\qquad 3\lambda^2+2\lambda-4. \\]

The middle minor is linear, and the other two do not both vanish at its root, so the gcd is one.

### 2.5 Should the criterion be stated for general \\(k\\)?

Yes, with a small clarification: it already appears to be a theorem for arbitrary \\(k\ge2\\), not just \\(k=2,3\\).

The reason is that all fixed and free row vectors lie in the same two-dimensional space \\(S\\). The spectral calculations take place entirely inside \\(S\\). For case (d), the witness is embedded in any chosen two-plane in \\(\mathbb C^k\\). The conditions involving \\(E\\), \\(F_0\\), and \\(\rho\\) are likewise defined in the ambient \\(k\\)-dimensional coordinate space.

Thus the theorem should say explicitly:

> The free-fibre criterion holds for every \\(k\ge2\\), provided the standing hypotheses \\(\ker T=0\\), \\(\rank L_0=r\\), and the stated rank-stratum assumptions hold.

The 1200 random tests are useful corroboration, but they should remain labelled as experiments. The proof, not the experiments, should support the all-\\(k\\) statement.

## 3. The constrained all-bad stratum

### 3.1 The fixed-\\(\lambda\\) collapse criterion is a valid sufficient condition

The mechanism isolated in II.3 is sound.

For \\(q=3,\omega=2\\), suppose that there is a fixed \\(\lambda_0\\) such that, for every admissible point in a fibre,

\\[ \rank(\lambda_0H-H_A)\le1. \\]

Then every point in that fibre is spectrally bad. The rank-two condition required by (5b) fails at the same \\(\lambda_0\\), uniformly over the entire fibre.

More generally, for arbitrary \\(\omega\\), the natural statement is:

> If there exists a fixed \\(\lambda_0\\) such that every admissible pair in a given fibre satisfies\
> \\[\
> \rank(\lambda_0H-H_A) \\]\
> then the entire fibre is bad.

This is a useful sufficient obstruction because it can often be proved by linear compatibility identities without computing any gcd.

### 3.2 It is not a necessary condition

There is no reason for a whole fibre to have a common bad eigenvalue. The bad eigenvalue may vary with the point of the fibre.

The exact necessary-and-sufficient formulation is instead:

\\[ \forall\theta\in\mathfrak F,\quad \exists\lambda\in\mathbb C: \rank P\_\theta(\lambda)<\omega, \\]

where \\(\mathfrak F\\) is the admissible fibre and \\(P\_\theta(\lambda)\\) is its pencil.

Equivalently, the projection to \\(\mathfrak F\\) of the projective rank-drop incidence variety is all of \\(\mathfrak F\\). On an irreducible fibre, this is equivalent to the generic pencil over the function field of that fibre having a nonconstant determinantal divisor.

Thus the common-\\(\lambda_0\\) criterion is a particularly transparent uniform obstruction, but not a necessary one.

For research purposes, I would retain it as a named sufficient criterion and not attempt to turn it into an equivalence.

### 3.3 The calculation for \\(S_1,S_2\\) is correct

The compatibility equations give the two possible Grassmannian points, and the report's row calculations show:

- on \\(S_1\\), every admissible pencil has rank at most one at \\(\lambda=-1\\);
- on \\(S_2\\), every admissible pencil has rank at most one at \\(\lambda=+1\\).

The conclusion that the entire \\(q=3,\omega=2\\) stratum is bad is therefore proved, assuming the preceding Grassmannian analysis has indeed shown that these are the only admissible Grassmannian points.

This is stronger than the earlier finite-sampling observation. It is now an exact all-parameter result.

## 4. A decisive correction: the conclusion \\(q\_{\min}=4\\) in II.3 is false

This is the most important issue in the report. The proof that the \\(\omega=2\\) stratum is entirely bad is valid, but the conclusion

\\[ q\_{\min}\ge4 \\]

does not follow. It excludes only the \\(\omega=2\\) stratum at \\(q=3\\), not other possible values of \\(\omega\\). More seriously, the given data admit a valid augmentation with \\(q=2\\).

### 4.1 Construct an augmentation with \\(q=2\\)

The data in II.3 specify

\\[ C=e_1^{\mathsf T},\qquad L_0=e_4^{\mathsf T}, \qquad CA=e_5^{\mathsf T}, \\]

and columns \\(2,3,4\\) of \\(A\\) are \\(e_3,e_2,e_5\\), respectively.

The specified columns imply

\\[ e_4^{\mathsf T}A =\alpha e_1^{\mathsf T}+\beta e_5^{\mathsf T} \\]

for some scalars \\(\alpha,\beta\\), because row 4 of columns 2, 3 and 4 is zero. They also imply

\\[ e_5^{\mathsf T}A =\gamma e_1^{\mathsf T}+e_4^{\mathsf T} +\delta e_5^{\mathsf T} \\]

for some scalars \\(\gamma,\delta\\), because row 5 of those three columns is \\((0,0,1)\\).

Now choose

\\[ \boxed{ L=\begin{pmatrix}e_4^{\mathsf T}\\\e_5^{\mathsf T}\end{pmatrix}. } \\]

This is a full-row-rank \\(2\times5\\) matrix with the required first row \\(L_0=e_4^{\mathsf T}\\).

The reference rank is

\\[ \rank\begin{pmatrix}L\\\CA\\\C\end{pmatrix} =\rank\begin{pmatrix}e_4^{\mathsf T}\\\e_5^{\mathsf T}\\\e_1^{\mathsf T}\end{pmatrix} =3. \\]

For (5a), both rows of \\(LA\\) lie in

\\[ \operatorname{span}\\{e_1^{\mathsf T},e_4^{\mathsf T},e_5^{\mathsf T}\\}, \\]

so

\\[ \rank\begin{pmatrix}LA\\\L\\\CA\\\C\end{pmatrix} =3. \\]

For (5b), modulo the fixed row space

\\[ \operatorname{span}\\{e_1^{\mathsf T},e_5^{\mathsf T}\\}, \\]

the two rows of \\(\lambda L-LA\\) are

\\[ \lambda e_4^{\mathsf T},\qquad -e_4^{\mathsf T}. \\]

They therefore contribute exactly one additional independent row for every \\(\lambda\in\mathbb C\\). Consequently,

\\[ \boxed{ \rank\begin{pmatrix}\lambda L-LA\\\CA\\\C\end{pmatrix} =3 =\rank\begin{pmatrix}L\\\CA\\\C\end{pmatrix} \quad\forall\lambda\in\mathbb C. } \\]

Thus this is an actual valid augmentation of order \\(q=2\\).

### 4.2 In fact, \\(q\_{\min}=2\\) for the stated data

Since \\(r=1\\), the only possible order below 2 is \\(q=1\\), in which case \\(L=L_0=e_4^{\mathsf T}\\).

The reference rank is then

\\[ \rank\begin{pmatrix}L_0\\\CA\\\C\end{pmatrix}=3. \\]

But at \\(\lambda=0\\),

\\[ -L_0A=-e_4^{\mathsf T}A \in\operatorname{span}\\{e_1^{\mathsf T},e_5^{\mathsf T}\\}. \\]

Hence

\\[ \rank\begin{pmatrix}-L_0A\\\CA\\\C\end{pmatrix}=2<3. \\]

Condition (5b) fails.

Therefore, under the stated setup,

\\[ \boxed{q\_{\min}=2.} \\]

This conclusion does not depend on how the unspecified columns 1 and 5 of \\(A\\) are completed.

### 4.3 The observability assertion is also impossible for the specified data

There is a second issue in lines 148–150. The report claims that \\((C,A)\\) is observable. But define

\\[ \mathcal U =\operatorname{span}\\{e_1^{\mathsf T},e_4^{\mathsf T},e_5^{\mathsf T}\\}. \\]

The specified first row and columns imply

\\[ e_1^{\mathsf T}A=e_5^{\mathsf T},\qquad e_4^{\mathsf T}A\in\mathcal U,\qquad e_5^{\mathsf T}A\in\mathcal U. \\]

Thus

\\[ \mathcal U A\subseteq\mathcal U. \\]

Since \\(C=e_1^{\mathsf T}\in\mathcal U\\), every row \\(CA^j\\) belongs to \\(\mathcal U\\). The observability matrix consequently has rank at most 3, whereas \\(n=5\\).

So the pair \\((C,A)\\) cannot be observable, regardless of the unspecified columns. The terminal-region result invoked in the report cannot be applied to this example.

### 4.4 What survives from II.3?

The following statement remains correct and worth retaining:

> The entire admissible stratum \\(q=3,\omega=2\\) is bad. On its two admissible Grassmannian fibres, a fixed value of \\(\lambda\\) forces rank loss uniformly over the fibre.

What must be withdrawn is the inference from that statement to \\(q\_{\min}\ge4\\). The correct distinction is:

- Stratum-level infeasibility: established for \\(q=3,\omega=2\\).
- Order-level infeasibility: not established by that calculation, and contradicted here by a \\(q=2,\omega=1\\) augmentation.

I recommend keeping the all-bad theorem but deleting the claimed \\(q\_{\min}=4\\) conclusion for this data set. If the intention was to construct an example with \\(q\_{\min}=4\\), the example must be redesigned; the present specified first row and columns already force an invariant three-dimensional row space and permit the \\(q=2\\) completion above.

## 5. Answers to the three questions

### Question 1 — Are the Smith-form citations sufficient, and can RP be stated unconditionally?

The citations are relevant, but the paper should state the exact algorithmic theorem being used.

Kaltofen, Krishnamoorthy and Saunders, Fast Parallel Computation of Hermite and Smith Forms of Polynomial Matrices, SIAM Journal on Algebraic Discrete Methods 8 (1987), 683–690, explicitly report polynomial-time deterministic sequential Smith-form computation over the rationals. This is the most directly relevant reference for a deterministic polynomial-time subroutine.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://epubs.siam.org\&sz=32)

应用数学学会



Storjohann and Labahn, A fast Las Vegas algorithm for computing the Smith normal form of a polynomial matrix, Linear Algebra and its Applications 253 (1997), 155–173, give a Las Vegas algorithm with an explicit expected bit-complexity bound for square nonsingular polynomial-matrix input over \\(\mathbb Z[x]\\). It is a useful faster-algorithm reference, but its stated input form should not be silently identified with the rectangular full-column-rank pencil in this application.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车+1



For the paper, I recommend stating the exact needed consequence as a separate lemma:

> Polynomial-matrix determinantal-divisor lemma. Given a rational polynomial matrix \\(P(\lambda)\in\mathbb Q[\lambda]^{q\times k}\\) of degree at most one and full column normal rank \\(k\\), the gcd of its \\(k\times k\\) minors can be computed in deterministic polynomial bit complexity in \\(q,k\\), and the coefficient bit size of \\(P\\).

Then explain that this follows from an appropriate rectangular Smith-form or Hermite-form algorithm. If the cited result is initially stated for square matrices, include the reduction from the rectangular full-column-rank problem to that setting. Clearing rational denominators first is harmless: it only multiplies the determinantal divisor by a nonzero rational constant.

With this lemma stated and cited precisely, together with the corrected two-combination lemma, the RP theorem can be made unconditional. The RP proof itself does not need to be weakened further.

I would use the deterministic KKS route for the cleanest RP statement. The Storjohann–Labahn Las Vegas algorithm can be mentioned as a faster alternative, but if used inside the RP algorithm its expected-time guarantee and any runtime truncation must be accounted for separately.

### Question 2 — Is the free-fibre criterion complete, and should it be made explicit?

My assessment is:

- The normal-rank formulation is the right one.
- The four alternatives are mathematically well motivated and appear complete under the stated free-fibre assumptions.
- Case (c) needs the incidence-dimension proof.
- The full-row-rank condition on \\(L\\) should be explicitly incorporated, as discussed above.
- The theorem should be stated for arbitrary \\(k\ge2\\), not just \\(k=2,3\\).

I do not think explicit closed-form numerical choices are necessary in every case. A rigorous existence proof by nonempty Zariski-open intersection is entirely acceptable in algebraic geometry. But the paper must actually establish that the relevant good set is nonempty and open. In particular, the current “finitely many proper conditions” phrase in case (c) should be replaced by the incidence argument.

I would present the theorem in a form that separates the geometric conditions from the four pencil cases:

1. There must exist a two-plane \\(S\\) containing \\(E+F_0\\).
2. There must be enough free rows to complete \\(H\\) to rank two.
3. The fixed pencil's normal rank and proportionality type determine which completion mechanism is available.
4. The free compatibility map permits the bottom rows to be selected independently.
5. The spectral-good and full-row-rank conditions are simultaneously attainable because they define nonempty open subsets of the free parameter space.

This gives the result a clearer mathematical structure than a list of four cases alone.

### Question 3 — Is common-\\(\lambda_0\\) collapse the right constrained criterion, and what next?

It is a useful sufficient condition, but not a necessary one.

The exact constrained-fibre criterion is the generic determinantal-divisor condition on each irreducible component:

\\[ \text{a component is entirely bad} \iff \gcd\\{\text{maximal minors over its function field}\\} \text{ is nonconstant}. \\]

A fixed common \\(\lambda_0\\) is a particularly simple certificate of this condition, because it makes every maximal minor vanish at that value. But a component may be entirely bad even when the bad root varies with the point.

For general \\(q=\omega+1\\), the next theoretical target should be a componentwise constrained-fibre criterion. However, I would not make that the immediate next deliverable. The free-fibre theorem and RP theorem are already close to publication quality after the corrections above.

## 6. Recommended revisions and research priorities

| Priority | Action                                                                                        | Reason                                                        |
| -------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| 1        | Correct the \\(q\_{\min}\\) conclusion in II.3.                                               | The stated data admit a \\(q=2\\) augmentation.               |
| 2        | Repair the two-combination lemma and complete the rectangular Smith-form complexity citation. | This closes the RP proof.                                     |
| 3        | Formalise the free-fibre criterion, especially case (c) and full row rank of \\(L\\).         | This turns a strong classification into a rigorous theorem.   |
| 4        | Keep the common-\\(\lambda_0\\) collapse as a named sufficient obstruction.                   | It is reusable and easy to verify exactly.                    |
| 5        | Then develop the general constrained-fibre criterion at \\(q=\omega+1\\).                     | This is the natural extension after the free case is settled. |

## 7. Overall verdict



RP argument structurally sound

Free-fibre classification promising

Constrained all-bad theorem valid

Claim \\(q\_{\min}=4\\) refuted



This report is a substantial advance, but it should not be treated as uniformly correct in its current form.

The RP argument is now close to a rigorous complexity theorem. The free-fibre criterion is a promising necessary-and-sufficient classification, with a repairable gap in case (c) and a missing explicit full-row-rank discussion. The constrained all-bad result is a valid exact theorem and identifies a useful uniform-collapse obstruction.

The critical correction is the final order-minimality claim. The example proves that the \\(\omega=2\\) stratum at \\(q=3\\) is bad; it does not prove that \\(q=3\\) is infeasible, and the specified data actually allow \\(q=2\\). This also exposes an impossible observability assertion. I would fix that example before using it as evidence for any terminal-region or minimum-order theorem.

The best next paper-level package is therefore: the corrected RP theorem, the complete free-fibre theorem for arbitrary \\(k\ge2\\), and the constrained uniform-collapse lemma—without the erroneous \\(q\_{\min}=4\\) conclusion.



50_rp_free_fibre_and_all_bad.md

50_rp_free_fibre_and_all_bad.md

50_rp_free_fibre_and_all_bad.md

50_rp_free_fibre_and_all_bad.md
