# Mathematical assessment of `47_formulations_and_plan.md`

The report contains several important advances, especially the exact implementation of the Grassmannian criterion and the matrix-identity argument in the \\(q=3\\) stratum. It also identifies the right distinction between decision, optimization, and construction.

However, there is one serious inconsistency in Part II.3, and it affects the claimed value of \\(q\_{\min}\\). In fact, using the data in the report, the alleged rank-one feasible stratum cannot be admissible. Moreover, the \\(n=4\\) example in Part II.4 appears to admit a stronger conclusion than the report states: it is infeasible at every permitted order, not merely at \\(q=2,3\\).

My overall recommendation is therefore:

1. Correct the formulation of the computational problems, particularly the claimed binary-search equivalence.
2. Repair or withdraw the conclusion in II.3.
3. Strengthen II.4 to a complete infeasibility result.
4. Test the proposed “empty or uniformly bad by a fixed matrix identity” pattern against general admissible pencil families.
5. Make the next main research objective a structural description of the spectral behavior over the admissible Grassmannian fibres, rather than immediately pursuing a hardness reduction.

I explain each point below.&#x20;

47_formulations_and_plan.md



## 1. Part I: the three formulations are useful, but two complexity claims need qualification

### 1.1 The distinction between DEC, OPT, and FIND is correct

The three problems should indeed be stated separately:

\\[ \mathrm{DEC}(q): \quad \exists R\text{ such that }\mathcal L=\binom{L_0}{R} \text{ satisfies (5a) and (5b)}; \\]

\\[ \mathrm{OPT}: \quad \text{determine the smallest feasible }q; \\]

\\[ \mathrm{FIND}: \quad \text{produce a feasible }R\text{ at the optimal order, together with a minimality certificate}. \\]

This distinction is mathematically and computationally important.

- DEC is an existence problem.
- OPT is an optimization problem over the finite set of possible row dimensions.
- FIND is a witness-construction problem, with an additional output-size requirement.

It is also correct that a hardness claim must specify which of these problems is being studied. In particular, a hardness result for finding a minimum-order augmentation is not automatically a hardness result for the fixed-order decision problem.

### 1.2 The binary-search assertion requires a monotonicity theorem

The report states

\\[ \mathrm{FIND}\geq\mathrm{OPT}\equiv\mathrm{DEC} \quad\text{by binary search}. \\]

The implication from DEC to OPT by binary search is not justified yet.

Binary search requires that feasibility be monotone in \\(q\\), namely

\\[ \mathrm{DEC}(q)=\mathrm{YES} \quad\Longrightarrow\quad \mathrm{DEC}(q+1)=\mathrm{YES}. \tag{1.1} \\]

But this monotonicity is not immediate from the definitions.

Suppose \\(\mathcal L\\) is feasible with \\(q\\) rows. To construct a feasible augmentation with \\(q+1\\) rows, one would need to append a new row \\(\ell\\) such that:

1. the enlarged \\(\mathcal L\\) still has full row rank;
2. the enlarged system satisfies (5a);
3. the enlarged pencil satisfies (5b).

Appending a row of \\(C\\), when it is linearly independent of the existing rows of \\(\mathcal L\\), is a natural possibility: its image under \\(A\\) is already represented among the \\(CA\\) rows. But there need not be a row of \\(C\\) outside the row space of \\(\mathcal L\\).

Appending a row of \\(CA\\) is not automatically valid, because its image under \\(A\\) involves \\(CA^2\\), which is not controlled by (5a) in general.

Consequently, I would not use binary search in the formal problem statement until monotonicity has been proved.

There is no difficulty with the finite search space itself:

\\[ r\le q\le n. \\]

One can always determine the minimum by testing all permitted orders, provided each DEC instance is decidable. This takes at most \\(n-r+1\\) decision tests.

Thus the safe formulation is

\\[ \mathrm{OPT}: \quad \min\\{q\in\\{r,\ldots,n\\}:\mathrm{DEC}(q)=\mathrm{YES}\\}, \\]

with the convention \\(q\_{\min}=+\infty\\) if no feasible order exists.

Only after establishing (1.1) should the paper replace exhaustive testing by binary search.

### 1.3 FIND should be specified by its output representation

The report is right to identify the output-field issue. I would make the computational model explicit from the beginning.

For rational input matrices, at least three versions are natural:

| Version                                          | Witness requirement               |
| ------------------------------------------------ | --------------------------------- |
| \\(\mathrm{FIND}\_{\mathbb Q}\\)                 | Rational entries in \\(R\\)       |
| \\(\mathrm{FIND}\_{\overline{\mathbb Q}}\\)      | Algebraic entries in \\(R\\)      |
| \\(\mathrm{FIND}\_{\mathbb R\_{\mathrm{alg}}}\\) | Real algebraic entries in \\(R\\) |

These are different problems.

The rotation example in the report illustrates the distinction between complex and real invariant subspaces, and also shows why rational output can be too restrictive. For

\\[ A=\begin{pmatrix}0&-1\\\1&0\end{pmatrix}, \\]

there are complex invariant lines, but there is no real invariant line. Thus it distinguishes complex feasibility from real feasibility, not merely rational feasibility from real feasibility.

A separate example illustrates the rational-output issue. Take

\\[ A=\begin{pmatrix}0&1\\\1&1\end{pmatrix}. \\]

Its eigenvalues are irrational algebraic numbers. Its one-dimensional invariant subspaces are therefore not rational lines, although they are real algebraic lines.

For an algebraic input model, the natural general-purpose witness representation is a real or complex algebraic-number representation, for example minimal polynomials together with isolating data. One must then account for the degree and coefficient height of the output.

I recommend defining the principal existence problem over the intended field first, and treating output representation as a separate computational refinement.

### 1.4 Is FIND genuinely harder than DEC?

Potentially, yes, but the distinction should not be overstated.

A decision procedure does not automatically provide a witness. Conversely, in a semialgebraic or algebraic-geometric setting, a constructive decision method can often be supplemented by sample-point extraction.

For rational input, if a finite system of polynomial equations and inequations has a complex solution, it has an algebraic solution over \\(\overline{\mathbb Q}\\). Similarly, a nonempty semialgebraic set defined over the rationals has real algebraic sample points.

That does not give a polynomial bound on the degree or height of the sample point. It does, however, mean that an algebraic output model is mathematically natural.

My recommendation is:

- Make \\(\mathrm{DEC}\_{\mathbb C}\\) or \\(\mathrm{DEC}\_{\mathbb R}\\) the primary decision problem, according to the intended application.
- Define \\(\mathrm{FIND}\_{\overline{\mathbb Q}}\\) or \\(\mathrm{FIND}\_{\mathbb R\_{\mathrm{alg}}}\\) as the corresponding constructive problem.
- Track output degree and height separately.
- Do not require rational witnesses unless the application genuinely needs rational augmentation matrices.

## 2. Part II.1: the Grassmannian implementation is a substantial result

The new computation for

\\[ n=5,\qquad p=1,\qquad q=3,\qquad r=1, \\]

with

\\[ K=\langle e_2,e_3\rangle,\qquad L_0=e_4^{\mathsf T}, \\]

is important.

The report gives

\\[ E=\operatorname{row}(0,1),\qquad F_0=\operatorname{row}(1,0), \\]

and

\\[ Z_1= \begin{pmatrix} 0&-1\\\ -1&0 \end{pmatrix}, \qquad Z_2=I_2. \\]

It reports that exactly two projective candidates,

\\[ \sigma=(1,1,0), \qquad \sigma=(1,-1,0), \\]

satisfy the Grassmannian criterion.

This has two implications.

### 2.1 It confirms why naive sampling failed

The admissible rank-two designs are not spread through the ambient \\(R\\)-space in a generic way. Their associated two-dimensional row spaces are restricted to two points of

\\[ \operatorname{Gr}(2,3). \\]

The fibres over those points can still contain continuous families of \\(R\\), but the possible Grassmannian directions are discrete.

This explains why random sampling in the original matrix coordinates can be ineffective even when the admissible stratum is nonempty.

It also demonstrates why the Grassmannian parameterization is more informative than direct random search.

### 2.2 The exact recovery is valuable independently

The three convention corrections listed in the report are not merely implementation details. They concern the exact correspondence between:

\\[ S\in\operatorname{Gr}(\omega,k), \\]

the compatible row pairs

\\[ (x,y)\in\mathcal C_S, \\]

and the actual matrix \\(R\\).

The recovery procedure should be treated as part of the mathematical algorithm, not just as a numerical post-processing step.

I recommend that the implementation produce an exact verification record containing:

1. the basis matrix \\(N_K\\);
2. the basis \\(Z\\) of \\(\ker T\\);
3. the candidate subspace \\(S\\);
4. the compatible bottom row pairs;
5. the recovered \\(R\\);
6. the reconstructed \\(H,H_A\\);
7. the exact ranks of \\(H\\) and \\(\binom{H}{H_A}\\).

This will make the computation independently reproducible.

## 3. Part II.2: the scaling argument is valid, with a small qualification

The report claims that for each of the two admissible Grassmannian points, the recovered family has

\\[ R(t)=tR(1), \\]

while the fixed top blocks remain unchanged.

The resulting pencil has the form

\\[ P(t,\lambda)=\lambda H(t)-H_A(t). \\]

The key observation is that the top row of \\(H(t)\\) and \\(H_A(t)\\) is independent of \\(t\\), while the bottom rows are multiplied by \\(t\\).

For any selected \\(\omega\\)-row minor, its determinant is therefore multiplied by a power of \\(t\\):

\\[ \Delta_I(t,\lambda)=t^{s_I}\Delta_I(1,\lambda), \\]

where \\(s_I\\) is the number of selected bottom rows.

Since \\(t\\) is a unit in \\(\mathbb Q(t)\\), multiplication by \\(t^{s_I}\\) does not affect the gcd in \\(\mathbb Q(t)[\lambda]\\). Hence

\\[ \gcd_I\Delta_I(t,\lambda) \sim \gcd_I\Delta_I(1,\lambda) \quad\text{in }\mathbb Q(t)[\lambda]. \\]

Thus the positive-degree gcd at \\(t=1\\) proves that the generic member of the scaling family is bad.

In fact, for every nonzero specialization \\(t\\), the same row-scaling argument preserves the gcd up to nonzero scalar factors.

There is one qualification: the specialization \\(t=0\\) must be considered separately. It may not belong to the rank-\\(\omega\\) stratum at all. Therefore the clean statement is:

> Every member of the scaling family with \\(t\ne0\\) is bad, and the generic member is bad over \\(\mathbb Q(t)\\).

This is a valid and reusable lemma.

However, I would avoid stating the broader principle as “a stratum that degenerates to a scaling ray is uniformly bad” without specifying the exact row-scaling structure. What matters is not merely that \\(R(t)\\) is proportional to \\(R(1)\\), but that each maximal minor is multiplied by a nonzero scalar factor independent of \\(\lambda\\).

## 4. Part II.3: the claimed lower-order feasible design is inconsistent with the stated admissibility condition

This is the most important correction in the report.

The report says that for the same \\(n=5\\) instance, a rank-one stratum is feasible by taking \\(B_1\\) and \\(B_2\\) with rows in the span of

\\[ (0,0,1), \\]

and that this yields

\\[ q\_{\min}=2. \\]

But the reported top blocks are

\\[ U_0=(0,1,0), \qquad V_0=(1,0,0). \\]

Recall that the admissibility condition is

\\[ \operatorname{rank} \begin{bmatrix} H\\\H_A \end{bmatrix} = \operatorname{rank}H. \tag{4.1} \\]

In particular, every row of \\(H_A\\) must belong to the row space of \\(H\\).

Let us examine the proposed construction.

If \\(B_1\\) has a row in the span of \\((0,0,1)\\), then the rows of \\(H\\) include

\\[ (0,1,0),\qquad (0,0,1). \\]

Consequently,

\\[ \operatorname{row}(H) = \operatorname{span}\\{(0,1,0),(0,0,1)\\}, \\]

assuming the bottom row is nonzero.

But the fixed top row of \\(H_A\\) is

\\[ (1,0,0), \\]

which does not belong to this row space.

Therefore

\\[ \operatorname{rank} \begin{bmatrix} H\\\H_A \end{bmatrix} > \operatorname{rank}H. \\]

So the proposed pair \\(B_1,B_2\\) is not admissible under (5a).

There is also a notation problem. The report writes

\\[ \operatorname{rank}[H\ H_A]=2. \\]

This is the rank of a horizontal concatenation. It is not the rank condition in (5a), which involves the vertical concatenation

\\[ \operatorname{rank} \begin{bmatrix} H\\\H_A \end{bmatrix}. \\]

These two rank conditions are not interchangeable.

### 4.1 The Grassmannian criterion independently rules out the claimed rank-one stratum

For the same instance,

\\[ E=\operatorname{span}\\{(0,1,0)\\}, \qquad F_0=\operatorname{span}\\{(1,0,0)\\}. \\]

Thus

\\[ \dim(E+F_0)=2. \\]

Any admissible row space \\(S\\) must contain \\(E+F_0\\). Therefore

\\[ \dim S=\omega\ge2. \\]

In particular, the \\(\omega=1\\) stratum is empty.

This is exactly the necessary condition N1 from the previous Grassmannian analysis:

\\[ \boxed{\dim(E+F_0)\le\omega.} \\]

So the proposed rank-one feasible stratum is ruled out before any spectral computation.

### 4.2 Consequence: the conclusion \\(q\_{\min}=2\\) must be withdrawn

The report's claim

\\[ q\_{\min}=2 \\]

does not follow from the proposed construction. Indeed, that construction violates (5a).

I would mark II.3 as not verified and presently incorrect, rather than as a correction to the previous research conclusion.

The correct conclusion from II.1 and II.2 is:

- the rank-two admissible stratum is nonempty;
- both of its reported Grassmannian families are spectrally bad;
- therefore \\(q=3\\) is infeasible.

It does not follow that \\(q=2\\) is feasible.

## 5. Part II.4: the \\(n=4\\) example can be strengthened to complete infeasibility

The report proves that \\(q=2\\) and \\(q=3\\) are infeasible and concludes

\\[ q\_{\min}\ge4. \\]

The data actually allow us to examine \\(q=4\\) as well.

The matrices are

\\[ C=e_1^{\mathsf T}, \qquad L_0=e_3^{\mathsf T}, \\]

and

\\[ A= \begin{pmatrix} 0&0&0&1\\\ 0&0&1&0\\\ 0&1&0&0\\\ 0&0&0&0 \end{pmatrix}. \\]

The action of \\(A\\) on the standard basis is

\\[ Ae_1=0,\qquad Ae_2=e_3,\qquad Ae_3=e_2,\qquad Ae_4=e_1. \\]

Therefore

\\[ v\_+=e_2+e_3,\qquad v\_-=e_2-e_3 \\]

are eigenvectors:

\\[ Av\_+=v\_+,\qquad Av\_-=-v\_-. \\]

Moreover,

\\[ Cv\_+=Cv\_-=0. \\]

Since

\\[ CA=e_4^{\mathsf T}, \\]

we also have

\\[ CAv\_+=CAv\_-=0. \\]

Thus both eigenvectors are invisible to the fixed rows \\(C\\) and \\(CA\\).

Now consider \\(q=4\\). Since \\(\mathcal L\\) has four rows and must have full row rank in \\(\mathbb C^{4\times4}\\), it is invertible.

For either eigenpair \\((\lambda,v)\\), with \\(v=v\_+\\) or \\(v\_-\\), we have

\\[ (\lambda\mathcal L-\mathcal LA)v = \mathcal L(\lambda I-A)v =0. \\]

Also,

\\[ CAv=Cv=0. \\]

Consequently,

\\[ \begin{bmatrix} \lambda\mathcal L-\mathcal LA\\\ CA\\\ C \end{bmatrix}v=0. \\]

The left-hand side of (5b) therefore has rank at most \\(3\\).

On the other hand, because \\(\mathcal L\\) is invertible,

\\[ \operatorname{rank} \begin{bmatrix} \mathcal L\\\CA\\\C \end{bmatrix} =4. \\]

Thus (5b) fails at \\(\lambda=1\\) and at \\(\lambda=-1\\), regardless of the choice of \\(R\\).

Therefore \\(q=4\\) is infeasible too.

### 5.1 Complete conclusion for this example

The permitted orders are

\\[ 1\le q\le4. \\]

The report has already established:

- \\(q=1\\): the fixed top rows \\(E,F_0\\) cannot lie in a one-dimensional row space;
- \\(q=2\\): the \\(\omega=0,1\\) strata are empty, and the \\(\omega=2\\) square pencil must lose rank at some complex \\(\lambda\\);
- \\(q=3\\): the only nonempty admissible stratum has \\(\omega=2\\), and the identity \\(H_A=-HZ_1\\) forces spectral failure;
- \\(q=4\\): the unobservable eigenvectors \\(e_2\pm e_3\\) force spectral failure.

Hence the stronger conclusion is

\\[ \boxed{ \text{There is no feasible augmentation for this instance at any permitted order.} } \\]

Equivalently, with the convention that the minimum is \\(+\infty\\) when no design exists,

\\[ \boxed{q\_{\min}=+\infty.} \\]

This is a much stronger and more useful result than \\(q\_{\min}\ge4\\).

It also illustrates an important general obstruction:

> If there is an eigenvector \\(v\\) of \\(A\\) satisfying \\(Cv=CAv=0\\), then at its eigenvalue the left-hand pencil in (5b) annihilates \\(v\\), independently of \\(\mathcal L\\). If a candidate \\(\mathcal L\\) is invertible, this immediately contradicts (5b).

For non-square \\(\mathcal L\\), the conclusion is more delicate because the right-hand rank in (5b) may also be deficient. The invertible case is particularly strong.

## 6. Question 2: the proposed empty-or-rigidly-bad pattern is not a general theorem

The report asks whether every admissible stratum might have the following structure:

1. it is empty, as decided by the Grassmannian criterion; or
2. it is nonempty, and its spectral failure follows from a fixed identity\
   \\[\
   H_A\equiv-HZ.\
   \\]

If true, this would give a remarkably simple algorithm: enumerate strata, solve the Grassmannian condition, and test the spectrum of a fixed matrix.

I do not think this is a plausible general theorem without substantial additional hypotheses.

### 6.1 Why the Grassmannian criterion does not imply a fixed spectral matrix

For a fixed \\(S\\), the compatible row pairs are

\\[ \mathcal C_S = \\{(x,y)\in S\times S:xZ_1+yZ_2=0\\}. \\]

The possible bottom rows are obtained by selecting elements of \\(\mathcal C_S\\).

The Grassmannian criterion says that the first-coordinate projections of these pairs, together with \\(E\\), span \\(S\\). It establishes the existence of an admissible \\(H,H_A\\).

It does not say that the second-coordinate rows are uniquely determined by the first-coordinate rows.

In general, there can be several compatible \\(y\\)'s for the same \\(x\\), or several different ways of choosing the bottom row pairs while retaining the same \\(S\\).

Thus the pencil

\\[ P(\lambda)=\lambda H-H_A \\]

can vary within the fibre over \\(S\\).

A fixed identity

\\[ H_A=-HZ \\]

requires much more than admissibility. It requires that the second block be a particular linear function of the first block, with the same matrix \\(Z\\) throughout the entire family.

That is a special structural property of the example in II.2 and II.4, not a consequence of the Grassmannian criterion itself.

### 6.2 A useful counter-indication: identical ordinary rank data can have different spectral behavior

Recall the earlier pair of pencils with

\\[ U= \begin{pmatrix} 1&0\\\ 0&1\\\ 0&0 \end{pmatrix}, \\]

and

\\[ G_a= \begin{pmatrix} -1&-1\\\ -1&-1\\\ -1&0 \end{pmatrix}, \qquad G_b= \begin{pmatrix} -1&-1\\\ -1&-1\\\ -1&1 \end{pmatrix}. \\]

Both pairs have the same ordinary rank invariants:

\\[ \rank U=2,\qquad \rank G=2,\qquad \rank[U\ G]=3,\qquad \rank\binom UG=2. \\]

Yet the two pencils have different spectral behavior.

For \\(G_a\\), the maximal minors are

\\[ m\_{12}=\lambda^2+2\lambda,\qquad m\_{13}=-1,\qquad m\_{23}=-(\lambda+1), \\]

so their gcd is \\(1\\). The pencil is good.

For \\(G_b\\), the maximal minors are

\\[ m\_{12}=\lambda^2+2\lambda,\qquad m\_{13}=-(\lambda+2),\qquad m\_{23}=-(\lambda+2), \\]

so their gcd is

\\[ \lambda+2. \\]

The pencil is bad.

This example does not, by itself, establish that every such pair arises from every fixed-\\(L_0\\) observer family. It does establish that ordinary rank data are insufficient to determine the spectral condition.

More importantly, it illustrates why a general theorem based solely on the dimension of \\(S\\), the rank of the pair, or a small collection of ordinary rank invariants is unlikely.

### 6.3 What would be a meaningful replacement theorem?

I would investigate the following more general statement.

For a fixed admissible \\(S\\), define the fibre of compatible bottom-row choices

\\[ \mathfrak F_S = \left\\{ (B_1,B_2): \begin{array}{l} \text{each row pair belongs to }\mathcal C_S,\\\ \operatorname{row}(E;B_1)=S \end{array} \right\\}. \\]

The associated pencil family is

\\[ P\_{B_1,B_2}(\lambda) = \lambda \begin{bmatrix}U_0\\\B_1\end{bmatrix} - \begin{bmatrix}V_0\\\B_2\end{bmatrix}. \\]

The question becomes:

> On a given irreducible component of \\(\mathfrak F_S\\), is the generic pencil good or bad?

This is substantially more general than asking whether a single fixed \\(Z\\) controls the whole family.

The exact spectral theorem and the genericity results developed earlier are well suited to this formulation.

For an irreducible component \\(X\\) of the admissible family, pass to its function field \\(\mathbb C(X)\\) and compute the gcd of the maximal minors of the generic pencil.

- If the gcd has degree zero, the component contains a nonempty Zariski-open set of good points.
- If the gcd has positive degree, the entire component is bad.

This gives a rigorous componentwise classification without requiring a fixed matrix identity \\(H_A=-HZ\\).

My answer to Question 2 is therefore no: the proposed dichotomy is too restrictive as a general theorem. A more plausible general theorem is a componentwise generic-gcd classification.

## 7. Question 3: what would be required for a general algorithm?

The report identifies three components:

(a) a polynomial bound on the number of strata;

(b) an algorithm for the Grassmannian condition;

(c) a decision procedure for the spectral property.

I would treat these in the following order.

### 7.1 Component (a): the number of rank strata is not the main difficulty

For a fixed \\(q\\), the rank

\\[ \omega=\rank H \\]

can take at most \\(k+1\\) values:

\\[ 0\le\omega\le\min(q,k). \\]

Thus there are at most

\\[ \min(q,k)+1 \\]

rank strata for that order.

Across all permitted \\(q\\), there are at most

\\[ \sum\_{q=r}^{n}(\min(q,k)+1) =O(nk) \\]

order-rank pairs.

This is polynomial in the matrix dimensions.

Therefore the number of rank values to examine is not the bottleneck.

The difficulty is the internal geometry of each stratum.

In particular, one must distinguish:

- a rank stratum being nonempty;
- a rank stratum having one irreducible component;
- a rank stratum having several irreducible components;
- a component being entirely bad;
- a component containing good points.

The first of these can be addressed by the Grassmannian criterion. The last two require spectral analysis over the corresponding families.

### 7.2 Component (b): the Grassmannian condition is the central structural problem

The exact criterion is

\\[ E+F_0\subseteq S, \qquad E+X_S=S, \qquad \omega-\dim E\le m, \\]

where

\\[ X_S=\\{x\in S:xZ_1\in SZ_2\\}. \\]

This is a significant reduction: instead of searching directly over \\(R\\), one searches over

\\[ S\in\operatorname{Gr}(\omega,k). \\]

However, it is still an algebraic-geometric existence problem.

The condition \\(E+X_S=S\\) is not simply a dimension inequality involving \\(E,F_0\\). It depends on the position of \\(S\\) relative to the fixed matrices \\(Z_1,Z_2\\).

The report's two-point example is particularly instructive: the ambient Grassmannian is two-dimensional, but the admissible set consists of only two points.

That is exactly the kind of geometry that ordinary dimension counting cannot capture.

I would not promise a polynomial-time algorithm for this condition in general.

Nevertheless, it is a reasonable target for exact algebraic computation. A Grassmannian chart can represent \\(S\\) by a matrix \\(B\\) of full row rank \\(\omega\\). The compatibility condition can then be expressed through ranks and kernels of matrices polynomial in the entries of \\(B\\).

This provides a finite algebraic description, even if its general complexity remains unresolved.

### 7.3 Component (c): the spectral test is comparatively well understood

For a fixed candidate \\(R\\), or a fixed algebraic point in a Grassmannian fibre, the spectral test is exact.

Factor

\\[ H=UV,\qquad H_A=GV, \\]

with \\(U\\) full column rank and \\(V\\) full row rank. Then the reduced pencil is

\\[ \lambda U-G. \\]

The condition is

\\[ \gcd\\{\omega\text{-minors of }\lambda U-G\\}=1. \\]

This is an exact polynomial computation.

The challenge is not testing a single candidate. It is deciding whether a whole algebraic family contains a good candidate.

The componentwise function-field method gives a natural approach:

1. determine the irreducible components of the admissible parameter variety;
2. compute the generic pencil on each component;
3. compute the gcd of its maximal minors over the component's function field;
4. decide whether at least one component is generically good.

This is a mathematically clean decision procedure over an algebraically closed field, assuming the component decomposition and function-field computations are carried out exactly.

For real feasibility, there is an additional issue: a complex component may have no suitable real points, or its real points may fail to be Zariski dense. The complex generic-gcd result alone does not settle real feasibility.

### 7.4 Which component is most difficult?

My assessment is:

| Component                        | Current status             | Main difficulty                         |
| -------------------------------- | -------------------------- | --------------------------------------- |
| Number of \\(\omega\\)-strata    | Essentially solved         | None of major significance              |
| Grassmannian admissibility       | Exact criterion available  | General algebraic existence             |
| Spectral test at a point         | Solved                     | Exact arithmetic                        |
| Spectral behavior on a component | Strong framework available | Component decomposition and generic gcd |
| Real witness extraction          | General methods exist      | Complexity and output size              |
| Polynomial-time complexity       | Open                       | No general algorithm established        |
| Hardness                         | Open                       | Must preserve shared \\(R\\)-dependence |

I would attack the Grassmannian admissibility problem first, but not in isolation. The objective should be to parameterize the admissible fibres well enough that the spectral family can be studied at the same time.

## 8. Question 4: I recommend a change in research strategy

The report correctly recognizes that a long sequence of structural reductions can become unproductive if every round merely narrows the problem without producing a definite theorem.

I would not abandon the structural approach. Rather, I would change its objective.

Instead of asking for a complete classification of all feasible augmentations immediately, aim first for a theorem that settles a meaningful class of instances.

I recommend three workstreams.

### Workstream A: prove a general componentwise theorem

The central statement should be:

> Let \\(X\\) be an irreducible component of a fixed rank-\\(\omega\\), (5a)-admissible parameter variety. Then either every point of \\(X\\) is spectrally bad, or the spectrally good points contain a nonempty Zariski-open dense subset of \\(X\\).

The geometric closedness argument developed earlier supports this statement.

The generic gcd over \\(\mathbb C(X)\\) then provides the exact algebraic test distinguishing the two alternatives.

This theorem would be a genuine general result, not tied to the special identity \\(H_A=-HZ\\).

It would also give a natural bridge between the Grassmannian formulation and the spectral problem.

### Workstream B: settle the case \\(k=\omega\\)

This is the most promising tractable regime.

When

\\[ k=\omega, \\]

the matrix \\(H\\) has full column rank, so

\\[ \ker H=0. \\]

Consequently, condition (5a) is automatic at the level of the restricted maps on \\(K\\).

The reachable-pair map

\\[ R\longmapsto(H(R),H_A(R)) \\]

is affine-linear in \\(R\\). The rank condition \\(\rank H=\omega\\) defines an open subset of the parameter space.

Therefore the earlier affine-family genericity theorem applies.

This gives a particularly useful equivalence:

\\[ \boxed{ \text{A good design exists in the nonempty rank-full affine family} \iff \text{the generic pencil is good}. } \\]

Equivalently, one can test whether the maximal minors of the generic pencil have gcd \\(1\\) over the rational function field of the affine parameters.

This is a much more concrete result than the full problem.

For fixed \\(q,\omega\\), bounded-degree resultant methods can be used in small cases. For example, the \\(q=3,\omega=2\\) case admits a particularly simple resultant construction.

I would aim to turn this into a complete theorem, with explicit input-size and arithmetic-complexity statements.

### Workstream C: treat \\(k>\omega\\) as the genuinely difficult regime

When \\(k>\omega\\), the matrix \\(H\\) has a nontrivial kernel, and (5a) imposes a genuine compatibility constraint.

The admissible set is no longer simply an open subset of an affine space. The Grassmannian criterion becomes essential.

This is where the complexity of the full problem is most likely to reside.

I would focus on two subcases:

1. \\(k-\omega=1\\);
2. \\(k-\omega\\) fixed.

The reason is geometric. The Grassmannian dimension is

\\[ \dim\operatorname{Gr}(\omega,k) = \omega(k-\omega). \\]

If \\(k-\omega=d\\) is fixed, this becomes

\\[ d\omega, \\]

which grows only linearly in \\(k\\).

This does not prove polynomial-time solvability, but it provides a promising parameterized regime for exact algorithms and classification.

## 9. A concrete research plan

I would organize the next stages as follows.

Phase 1 — Repair and certify the current examples

Immediate priority

- Recheck II.3 using the vertical rank condition.
- Remove the claimed \\(q\_{\min}=2\\) conclusion unless a genuinely admissible construction is found.
- Strengthen II.4 to the all-orders infeasibility theorem above.
- Save exact rank and eigenvector certificates for the \\(n=4\\) example.

Phase 2 — Establish the general geometry

- Write the Grassmannian criterion as a formal theorem with all field assumptions.
- Describe the compatible fibre \\(\mathfrak F_S\\) explicitly.
- Determine when the fibre is affine-linear and when it has additional rank constraints.
- Identify the irreducible components of the admissible family in small dimensions.

Phase 3 — Study spectral behavior over each fibre

- Compute generic maximal-minor gcds over function fields.
- Determine whether the gcd is constant on particular classes of fibres.
- Search for examples where the same \\(S\\) supports both good and bad pencils.
- Test whether \\(H_A=-HZ\\) is a special case of a broader affine relation.

Phase 4 — Prove tractable special cases

- Complete the \\(k=\omega\\) theorem.
- Study \\(k-\omega=1\\).
- Complete the \\(q=3,\omega=2\\) classification.
- Establish exact witness-extraction procedures.

Phase 5 — Reassess complexity

- If the Grassmannian condition admits a uniform structural solution, pursue an algorithm.
- If the compatible fibres exhibit sufficiently rich nonlinear geometry, investigate hardness reductions.
- Require any reduction to preserve the common \\(R\\)-dependence of \\(H\\) and \\(H_A\\).

### Suggested priority order

I would prioritize:

1. Correct the current examples.
2. Prove the \\(k=\omega\\) affine-family theorem in its strongest useful form.
3. Construct a same-\\(S\\), different-spectral-behavior example in the \\(k>\omega\\) regime.
4. Develop the \\(k-\omega=1\\) case.
5. Only then decide whether a hardness reduction is warranted.

I would not spend the next round trying to prove the rigid identity pattern in full generality. The available mathematics does not support that direction yet.

## 10. What would count as a definite result?

I suggest aiming for a paper with the following structure.

### Theorem A: exact Grassmannian characterization

For fixed \\(A,C,L_0,q,\omega\\), give necessary and sufficient conditions for the nonemptiness of the rank-\\(\omega\\), (5a)-admissible stratum.

The criterion already developed is a strong candidate.

### Theorem B: componentwise generic spectral dichotomy

For each irreducible component of the admissible variety, show that either:

- the whole component is bad; or
- its good points form a nonempty Zariski-open dense subset.

Identify the generic gcd as the exact algebraic invariant.

### Theorem C: affine-family tractability

For \\(k=\omega\\), reduce existence of a good augmentation to a generic-pencil test over the affine parameter space.

For fixed \\(q,\omega\\), derive explicit complexity bounds.

### Theorem D: a complete low-dimensional classification

For example, classify all instances with

\\[ q=3,\qquad \omega=2,\qquad k\le3, \\]

or all instances with

\\[ k-\omega=1 \\]

under a clearly stated set of assumptions.

A complete classification of a meaningful special case is preferable to an incomplete claim about the complexity of the unrestricted problem.

## 11. Final answers to the four questions

Question 1 — Are the three formulations right?

Yes, with two modifications.

- Keep DEC, OPT, and FIND separate.
- Do not assert binary-search equivalence until feasibility monotonicity in \\(q\\) is proved.
- Define the output field and algebraic representation for FIND.
- Include the possibility that no feasible order exists.

Question 2 — Is every stratum either empty or rigidly bad?

No general theorem of that form is currently justified.

The scaling identity is a powerful special mechanism, but the Grassmannian criterion does not force it. The correct general framework is to study the spectral gcd over each irreducible component of each compatible fibre.

Question 3 — Which algorithmic component should be attacked first?

The number of rank strata is already under control. The principal difficulty is the geometry of the Grassmannian admissible set and its compatible fibres.

The pointwise spectral test is comparatively well understood. The componentwise generic spectral test is the next natural extension.

Question 4 — Continue the structural route or change strategy?

Continue, but change the target.

Do not attempt to classify every possible augmentation immediately. First prove a complete theorem for \\(k=\omega\\), establish the componentwise generic dichotomy, and investigate \\(k-\omega=1\\).

That plan can produce a definite mathematical result without prematurely committing to either polynomial-time solvability or hardness.

## 12. My strongest recommendation

There is one particularly important correction and one particularly promising opportunity.

The correction is that the claimed rank-one feasible stratum in II.3 violates the vertical rank condition. The resulting \\(q\_{\min}=2\\) conclusion should be withdrawn. In the separate \\(n=4\\) example, the unobservable eigenvectors actually establish infeasibility at \\(q=4\\) too, so that example gives a complete all-orders obstruction.

The opportunity is the \\(k=\omega\\) regime. There the compatibility obstruction disappears, the parameter family becomes affine, and the generic-pencil theorem gives a clean existence criterion. This is the best candidate for the next theorem.

I would make the next research deliverable a rigorous paper-ready theorem for \\(k=\omega\\), together with a complete exact audit of the two examples in this report. That would turn the current sequence of structural reductions into a definite result, while preserving the more difficult \\(k>\omega\\) problem as a clearly separated research direction.