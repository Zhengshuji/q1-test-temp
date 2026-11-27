# Mathematical audit of `40_fixed_rows_corrected.md`

The correction in Part I is valid. More importantly, it resolves the fixed-row image problem in a way that is stronger and more useful than the original surjectivity criterion: it gives the entire image of the fixed-row map, including the non-surjective cases.

My main recommendation is to make one further conceptual move before writing any complexity theorem: formulate the spectral feasibility problem as a decision problem over a linear family of compatible target pairs, and use a polynomial left-inverse certificate for the reduced pencil. This gives a clean answer to Questions 1–3 and avoids making the number of maximal minors the central complexity parameter.

I will first audit the corrected mathematics, then discuss the input model, the meaningful stratum-level problems, and the compatibility-based formulation.

## 1. Part I: the corrected fixed-row image

### 1.1 Proposition 1 is correct

The report defines

\\[ T:K\oplus K\longrightarrow\mathbb C^n, \qquad T(v,w)=v+Aw, \\]

and

\\[ \Theta(R)=(RN_K,RAN_K). \\]

The assertion

\\[ \Theta\text{ is surjective} \iff T\text{ is injective} \iff \left\\{ \begin{aligned} \ker(A|\_K)&=0,\\\ K\cap AK&=0 \end{aligned} \right. \\]

is correct. The proof in the report is also correct.&#x20;

40_fixed_rows_corrected.md



Here is a useful way to understand the result.

The map \\(\Theta\\) asks whether two independently prescribed maps

\\[ B_1:K\to\mathbb C^m,\qquad B_2:K\to\mathbb C^m \\]

can be realized as

\\[ B_1=R|\_K,\qquad B_2=R\circ A|\_K \\]

by one common ambient linear map \\(R:\mathbb C^n\to\mathbb C^m\\).

If \\(T\\) is injective, then every vector in \\(K+AK\\) has a unique representation

\\[ x=v+Aw,\qquad v,w\in K. \\]

Consequently, the prescriptions

\\[ R(v+Aw)=B_1v+B_2w \\]

are consistent for arbitrary \\(B_1,B_2\\). One can then extend \\(R\\) from \\(K+AK\\) to all of \\(\mathbb C^n\\).

Conversely, if \\(T\\) has a nonzero kernel vector, then the two prescriptions cannot be independent. This proves the necessity of injectivity.

The two conditions in Proposition 1 have distinct roles:

- \\(\ker(A|\_K)=0\\) prevents a nonzero \\(w\in K\\) from satisfying \\(Aw=0\\).
- \\(K\cap AK=0\\) prevents a nonzero image \\(Aw\\), with \\(w\in K\\), from also lying in \\(K\\).

Neither condition can simply be omitted.

### 1.2 Proposition 2 is the more fundamental result

The exact image formula is

\\[ \boxed{ \operatorname{im}\Theta = \left\\{ (B_1,B_2): B_1v+B_2w=0 \text{ for all }(v,w)\in\ker T \right\\}. } \\]

This is correct, and its proof is complete.&#x20;

40_fixed_rows_corrected.md



In fact, I would make Proposition 2 the primary theorem and Proposition 1 a corollary.

To see why, define

\\[ B:K\oplus K\to\mathbb C^m,\qquad B(v,w)=B_1v+B_2w. \\]

Then

\\[ (B_1,B_2)\in\operatorname{im}\Theta \iff \ker T\subseteq\ker B. \\]

The proof is simply the universal property of a quotient: \\(B\\) factors through \\(T\\) if and only if it vanishes on \\(\ker T\\). Thus there exists a linear map

\\[ \widetilde R:\operatorname{im}T\to\mathbb C^m \\]

such that

\\[ B=\widetilde R\circ T. \\]

Extending \\(\widetilde R\\) to \\(\mathbb C^n\\) gives the required \\(R\\).

This is a particularly clean factorisation theorem. It also makes clear that the exact image is determined by the kernel of \\(T\\), not by a guessed dimension formula involving \\(K\cap AK\\).

### 1.3 The dimension formula is correct

The report gives

\\[ \ker T\cong K\cap A^{-1}K, \\]

where \\(A^{-1}K\\) means the preimage of \\(K\\), not the image under an inverse matrix. This is correct.&#x20;

40_fixed_rows_corrected.md



Indeed,

\\[ (v,w)\in\ker T \iff v=-Aw,\quad w\in K,\quad Aw\in K. \\]

Thus projection onto the second coordinate identifies \\(\ker T\\) with

\\[ \\{w\in K:Aw\in K\\}=K\cap A^{-1}K. \\]

The restriction map

\\[ \operatorname{Hom}(K,\mathbb C^m)^2 \longrightarrow \operatorname{Hom}(\ker T,\mathbb C^m), \\]

given by

\\[ (B_1,B_2)\longmapsto \left[(v,w)\mapsto B_1v+B_2w\right], \\]

is surjective: every linear map on \\(\ker T\\) extends to \\(K\oplus K\\).

Therefore its kernel has codimension

\\[ m\dim\ker T. \\]

It follows that

\\[ \boxed{ \dim\operatorname{im}\Theta = m\left(2k-\dim(K\cap A^{-1}K)\right). } \\]

This dimension formula is not merely a count of equations. It counts the number of independent linear compatibility conditions.

### 1.4 One useful improvement to Part I

The report's Proposition 2 can be converted immediately into a computational construction.

Let

\\[ Z= \begin{bmatrix} Z_1\\\ Z_2 \end{bmatrix} \\]

be a basis matrix for \\(\ker T\\), with \\(Z_1,Z_2\\) each having \\(k\\) rows. The compatibility condition becomes

\\[ B_1Z_1+B_2Z_2=0. \\]

This gives an explicit linear system in the entries of \\(B_1,B_2\\). It is a convenient representation for both symbolic calculations and complexity formulations.

For a fixed-row problem, the lower \\(m\\) rows of the two target matrices must satisfy precisely these equations. There is no need to introduce an unknown ambient matrix \\(R\\) into the target-space problem unless one specifically wants to reconstruct \\(R\\).

## 2. Part II: audit of the self-audit

The report's classification of the previous errors is useful. The three identified error types are real mathematical issues, not cosmetic corrections.&#x20;

40_fixed_rows_corrected.md



I agree with the corrected status of the fixed-row image and with the two additional qualifications in lines 78–84. There are, however, a few points I would sharpen.

### 2.1 The reduced-rank identity needs precise dimensions

The report correctly observes that the rank identity for the reduced pencil depends on the selected-column factorisation.&#x20;

40_fixed_rows_corrected.md



Let

\\[ H\in\mathbb C^{q\times k},\qquad \operatorname{rank}H=\omega, \\]

and choose a column set \\(S\\) with \\(|S|=\omega\\) such that

\\[ U=H\_{[:,S]}\in\mathbb C^{q\times\omega} \\]

has full column rank.

There is a unique matrix \\(V\in\mathbb C^{\omega\times k}\\) satisfying

\\[ H=UV,\qquad V\_{[:,S]}=I\_\omega. \\]

If

\\[ \ker H\subseteq\ker H_A, \\]

then

\\[ H_A=GV,\qquad G=H\_{A[:,S]}. \\]

Hence

\\[ \lambda H-H_A=(\lambda U-G)V. \\]

Because \\(V\\) has full row rank, it is surjective as a map \\(\mathbb C^k\to\mathbb C^\omega\\), so

\\[ \boxed{ \operatorname{rank}(\lambda H-H_A) = \operatorname{rank}(\lambda U-G). } \\]

The normalization is

\\[ V\_{[:,S]}=I\_\omega. \\]

If the report literally intends \\(V^{\mathsf T}\_{[:,S]}=I\_\omega\\), that notation should be checked: with \\(V\in\mathbb C^{\omega\times k}\\), the latter is not the corresponding dimensionally correct expression. This may just be a transpose typo.

### 2.2 The lower bound on the attainable rank is correct but should remain separate

For

\\[ \mathcal L=\begin{bmatrix}L_0\\\R\end{bmatrix}, \\]

we have

\\[ \mathcal L N_K = \begin{bmatrix} L_0N_K\\\RN_K \end{bmatrix}. \\]

Therefore

\\[ \operatorname{rank}(\mathcal L N_K) \geq \operatorname{rank}(L_0N_K). \\]

Since \\(R\\) is unrestricted, one can choose \\(R=0\\), obtaining equality. Thus

\\[ \boxed{ \min_R\operatorname{rank}(\mathcal L|\_K) = \operatorname{rank}(L_0N_K). } \\]

The report correctly warns that this is only an attainable-rank statement, not a spectral-feasibility theorem.&#x20;

40_fixed_rows_corrected.md



The distinction matters. A rank-minimizing \\(R\\) need not satisfy

\\[ \ker H\subseteq\ker H_A, \\]

and even if it does, the resulting reduced pencil may have a finite rank drop.

### 2.3 The machine-checking labels should be qualified

The report lists several statements as machine-checked.&#x20;

40_fixed_rows_corrected.md



I can audit the mathematical arguments presented in this report and the preceding research record, but I cannot independently certify a machine-checked result without seeing the corresponding formal proof, the definitions used by the formalisation, and the successful build output.

For the paper or research log, I recommend distinguishing:

- Mathematically proved: a proof has been written and checked at the mathematical level.
- Formally verified: the exact theorem has been accepted by the proof assistant in the stated development.
- Computationally tested: a program or finite collection of examples has been checked.
- Conditionally verified: the argument is valid under explicitly stated hypotheses, but the hypotheses have not yet been established in the application.

This avoids making the status table appear stronger than the available evidence.

### 2.4 The Bézout equation count is correctly identified

The report notes that the Bézout coefficient system has \\(2\omega\\), not \\(2\omega-1\\), coefficient equations.&#x20;

40_fixed_rows_corrected.md



For clarity, if the maximal minors \\(p_i(\lambda)\\) have degree at most \\(\omega\\), one may use

\\[ \sum_i u_i(\lambda)p_i(\lambda)=1, \qquad \deg u_i\leq\omega-1. \\]

The left-hand side has degree at most

\\[ (\omega-1)+\omega=2\omega-1. \\]

Matching its coefficients with the constant polynomial \\(1\\) gives equations for the coefficients of

\\[ 1,\lambda,\ldots,\lambda^{2\omega-1}, \\]

which is \\(2\omega\\) coefficient equations.

This is an important bookkeeping correction. It does not, however, mean that one must explicitly enumerate all maximal minors. That leads to a better formulation below.

# 3. Question 1: what input model should be used?

The proposed model is close, but I would change one essential feature:

\\[ \boxed{\text{Do not quantify }R\text{ over }\mathbb Q \text{ unless rational-valued augmentations are part of the intended problem.}} \\]

The natural model for a real-valued linear system is real existential quantification.

## 3.1 Rational input, real unknowns

A clean default model is:

- \\(A,C,L_0\\) have rational entries, encoded in binary;
- \\(q\\) is part of the input, with an encoding convention specified below;
- \\(R\\) is existentially quantified over \\(\mathbb R^{(q-r)\times n}\\);
- the spectral condition is required for every \\(\lambda\in\mathbb C\\).

This gives a real-algebraic decision problem.

Why is this natural? The data may be rational, but the sought observer or augmentation is generally a real matrix. There is no mathematical reason to require its entries to be rational unless that is an explicit design constraint.

The spectral condition over \\(\mathbb C\\) does not create a problem for this model. When the pencil coefficients are real, the condition that its maximal minors have no common finite complex root is equivalent to their gcd being a nonzero constant in \\(\mathbb R[\lambda]\\).

Thus one can encode the all-complex-\\(\lambda\\) condition using real polynomial equations and inequations.

## 3.2 Why existential quantification over \\(\mathbb Q\\) is dangerous

Suppose instead that the question is

\\[ \exists R\in\mathbb Q^{(q-r)\times n} \quad\text{such that the spectral condition holds.} \\]

This is not the ordinary existential theory of the reals. It is a rational-point existence problem.

The distinction is fundamental:

- Existence of a real solution to a finite system of polynomial equations and inequalities is a problem in real algebraic geometry.
- Existence of a rational solution is a problem about rational points on algebraic or constructible sets.

The latter is not generally reducible to the former by simply replacing \\(\mathbb R\\) with \\(\mathbb Q\\). In particular, the general decidability status of rational-point existence is not settled by the usual \\(\exists\mathbb R\\) framework.

Consequently, I recommend treating rational \\(R\\) as a separate arithmetic variant, not as the default complexity model.

There are three distinct formulations worth keeping apart:

| Model              | Unknown \\(R\\)             | Natural framework                   |
| ------------------ | --------------------------- | ----------------------------------- |
| Real synthesis     | \\(\mathbb R^{m\times n}\\) | Real algebraic decision             |
| Complex synthesis  | \\(\mathbb C^{m\times n}\\) | Algebraically closed-field decision |
| Rational synthesis | \\(\mathbb Q^{m\times n}\\) | Rational-point existence            |

For a real-valued observer problem, the first is the natural default.

## 3.3 Should \\(q\\) be encoded in unary?

Your concern is well-founded.

The issue is that \\(q\\) controls the number of existential variables:

\\[ m n=(q-r)n. \\]

If \\(q\\) is given in binary, it may be exponentially larger than its encoding length. Then even writing down the matrix \\(R\\) can require exponentially many entries.

There are two reasonable ways to address this.

Option A: unary \\(q\\).

This is appropriate if \\(q\\) is an explicit order parameter and the decision problem is:

> Given the rational system data and an observer order \\(q\\), does an admissible augmentation of order \\(q\\) exist?

Unary encoding ensures that the number of entries of \\(R\\) is polynomial in the input length, assuming the other matrix dimensions are explicitly represented.

It is a standard way to avoid an artificial succinct-parameter issue.

Option B: restrict \\(q\\) by a proved polynomial bound.

If the mathematical problem supplies a bound such as

\\[ q\leq f(n,p,r) \\]

for a polynomial \\(f\\), then one can encode \\(q\\) in binary without changing the polynomial-size witness property.

But such a bound should be proved from the observer problem. It should not be assumed merely because it seems natural.

### My recommendation

Use unary \\(q\\) in the first complexity definition. Later, if you prove a useful upper bound on the minimum feasible order, replace unary encoding by that bound.

This does not distort the usual matrix-input problem. It makes explicit that the number of rows being synthesized is itself part of the problem size.

A further distinction is useful: if \\(q\\) is a fixed constant rather than an input, there is no unary-versus-binary issue at all. One can study fixed-\\(q\\) slices separately.

# 4. Question 2: which stratum-level statements are meaningful?

I recommend defining three different decision tasks. They have different mathematical content and should not be conflated.

## 4.1 Task A: verification of a supplied candidate

Input: Rational \\(A,C,L_0,R\\).

Question: Does this particular \\(R\\) satisfy (5a) and (5b)?

This is the simplest and most useful baseline.

The procedure is:

1. Compute\
   \\[\
   K=\ker\begin{bmatrix}C\CA\end{bmatrix}.\
   \\]
2. Choose a basis matrix \\(N_K\\).
3. Form\
   \\[\
   H=\mathcal L N_K,\qquad H_A=\mathcal L A N_K.\
   \\]
4. Check\
   \\[\
   \ker H\subseteq\ker H_A.\
   \\]
5. Set \\(\omega=\operatorname{rank}H\\).
6. Reduce the pencil to a \\(q\times\omega\\) pencil\
   \\[\
   P(\lambda)=\lambda U-G,\
   \\]\
   where \\(U\\) has full column rank.
7. Check that \\(P(\lambda)\\) has full column rank for every finite complex \\(\lambda\\).

The last step is equivalent to saying that the gcd of all \\(\omega\times\omega\\) minors is a nonzero constant.

This is an algorithmic verification problem, not an existential synthesis problem. It is the right place to establish a polynomial-time baseline using polynomial-matrix algorithms, such as computation of the relevant determinantal divisor or Smith form over \\(\mathbb Q[\lambda]\\).

I would not claim a bit-complexity bound until coefficient growth and the chosen polynomial-matrix algorithm have been specified. But the mathematical verification task is clear and well-defined.

## 4.2 Task B: fixed-order spectral feasibility

This is the central synthesis problem:

\\[ \boxed{ \begin{aligned} \mathrm{FEAS}(q):\quad &\text{Given rational }A,C,L_0,\text{ does there exist}\\\ &R\in\mathbb R^{(q-r)\times n} \text{ satisfying (5a) and (5b)?} \end{aligned} } \\]

This is a meaningful decision problem. It captures what the observer construction actually asks.

For analysis, partition it into rank strata:

\\[ \mathrm{FEAS}(q,\omega): \quad \exists R:\  \operatorname{rank}H(R)=\omega,\  \ker H(R)\subseteq\ker H_A(R),\ (5b). \\]

Then

\\[ \mathrm{FEAS}(q) \iff \bigvee\_{\omega=0}^{\min(q,k)} \mathrm{FEAS}(q,\omega). \\]

This disjunction is the natural meaning of the rank-stratified target.

The point is not to claim that each stratum has a different complexity class. Rather, the strata give structurally different algebraic descriptions.

## 4.3 Task C: generic feasibility on a rank stratum

This is a separate question:

> On a specified irreducible component of a rank stratum, is the spectral condition satisfied generically?

This is the problem addressed by the open-or-empty dichotomy in the earlier work.

It should not be confused with \\(\mathrm{FEAS}(q,\omega)\\).

For example, a stratum can contain a nonempty open set of spectrally feasible points while also containing exceptional spectrally infeasible points. Generic feasibility says nothing about whether a particular point is feasible, and it does not itself solve the real existential problem unless the relevant real points are known to be present.

The generic question is algebraic-geometric; the existential real question is real-algebraic.

## 5. The \\(\omega=0\\) and \\(\omega=1\\) cases: what can actually be claimed?

These two cases do have useful exact descriptions, but the claims need to be stated at the correct decision level.

### 5.1 The zero-rank stratum

If

\\[ \omega=\operatorname{rank}H=0, \\]

then

\\[ H=0. \\]

The compatibility condition

\\[ \ker H\subseteq\ker H_A \\]

forces

\\[ H_A=0. \\]

Thus the target pair is exactly

\\[ \boxed{(H,H_A)=(0,0).} \\]

The reduced pencil has zero columns, so the spectral condition is automatic.

But this does not mean that the original \\(R\\)-space contains one candidate. It means that the target-space condition is the single point \\((0,0)\\). The set of \\(R\\)'s mapping to this target may be a positive-dimensional affine subspace.

For the fixed-row problem, existence on this stratum requires

\\[ L_0N_K=0,\qquad L_0AN_K=0, \\]

together with the corresponding lower-row equations. Once these fixed top-row requirements hold, the choice \\(R=0\\) satisfies the lower-row equations.

Therefore the meaningful statement is:

> The \\(\omega=0\\) target feasibility problem reduces to checking two fixed matrix equalities involving \\(L_0\\), and the spectral condition is automatic.

That is stronger and more precise than saying it is decidable by inspection.

### 5.2 The rank-one stratum

Suppose

\\[ \omega=1. \\]

The reduced pencil has the form

\\[ P(\lambda)=\lambda u-g, \qquad u,g\in\mathbb C^q,\quad u\ne0. \\]

It has full column rank for every finite \\(\lambda\\) exactly when

\\[ \lambda u-g\ne0 \qquad\text{for all }\lambda\in\mathbb C. \\]

Equivalently,

\\[ \boxed{\operatorname{rank}[u\ \ g]=2.} \\]

The bad condition is

\\[ \operatorname{rank}[u\ \ g]\leq1, \\]

which is equivalent to the quadratic equations

\\[ \boxed{ u_i g_j-u_j g_i=0 \quad(1\leq i\<j\leq q). } \\]

This gives an exact rank-one characterization.

There are two important qualifications:

- If \\(q=1\\), every nonzero \\(u\\) and every \\(g\\) are linearly dependent. Thus the rank-one stratum is spectrally bad.
- If \\(q\geq2\\), the rank-one stratum can contain both good and bad points, depending on whether \\(u,g\\) are independent.

Now consider the phrase in your report:

> deciding whether it vanishes identically on the stratum looks like linear algebra.

This needs to be split into two questions.

Question A: Is every point of the rank-one stratum spectrally bad?

This asks whether all the quadratic wedge expressions vanish identically on the relevant stratum.

Question B: Does there exist at least one spectrally good point on the rank-one stratum?

This asks whether there exists an \\(R\\) on the stratum for which at least one wedge expression is nonzero.

These are not the same decision problem.

If the rank-one stratum is described as an explicit affine-linear parametrisation, then testing polynomial identity can indeed reduce to coefficient comparison. But if the stratum is described implicitly by rank conditions and compatibility equations, identity testing may require determining the ideal or coordinate ring of that stratum. It is not automatically just ordinary linear algebra.

Recommended statement:

> For \\(\omega=1\\), candidate spectral verification reduces to testing whether \\(\operatorname{rank}[u\ g]=2\\). For an explicitly parametrised affine family, generic feasibility can be tested by determining whether the wedge polynomials vanish identically. General existential feasibility over the rank-one stratum remains a real-algebraic decision problem unless further structure is established.

This is accurate and does not assert an unsupported polynomial-time boundary.

### 5.3 The higher-rank strata

For \\(\omega\geq2\\), I agree with the report's restraint.

There is no justification at present for asserting that \\(\omega=2\\) is a complexity threshold. The algebraic description changes with \\(\omega\\), but that alone does not establish a complexity separation.

A sound paper should report the exact structural characterisation and leave the complexity classification open.

# 6. A useful improvement: replace the Bézout-minor system by a polynomial left-inverse certificate

This is the main technical suggestion I would add to the report.

The current reduced criterion is

\\[ P(\lambda)=\lambda U-G \in\mathbb R[\lambda]^{q\times\omega}, \qquad \operatorname{rank}U=\omega. \\]

The spectral condition is

\\[ \operatorname{rank}P(\lambda)=\omega \quad\text{for every }\lambda\in\mathbb C. \\]

Equivalently, the gcd of all \\(\omega\times\omega\\) minors of \\(P\\) is a nonzero constant.

That description involves

\\[ \binom q\omega \\]

maximal minors. When \\(\omega\\) and \\(q-\omega\\) both grow, this can be exponentially large.

However, there is another equivalent formulation.

## 6.1 Polynomial left-inverse theorem

For a polynomial matrix

\\[ P(\lambda)\in F[\lambda]^{q\times\omega}, \qquad q\geq\omega, \\]

over a field \\(F\\), the following are equivalent:

1. The gcd of all \\(\omega\times\omega\\) minors of \\(P\\) is a nonzero constant.
2. There exists a polynomial matrix\
   \\[\
   X(\lambda)\in F[\lambda]^{\omega\times q}\
   \\]\
   such that\
   \\[\
   \boxed{X(\lambda)P(\lambda)=I\_\omega.}\
   \\]

The implication from 2 to 1 follows from Cauchy–Binet: each entry of \\(XP=I\_\omega\\) is a polynomial combination of maximal minors of \\(P\\). Therefore those minors generate the unit ideal.

For the converse, write the maximal minors as \\(p_I(\lambda)\\), indexed by row subsets \\(I\\) of size \\(\omega\\). If their gcd is one, the bounded-degree Bézout result gives

\\[ \sum_I u_I(\lambda)p_I(\lambda)=1, \qquad \deg u_I\leq\omega-1, \\]

because each \\(p_I\\) has degree at most \\(\omega\\).

Let \\(E_I\\) select the rows indexed by \\(I\\), so

\\[ P_I=E_I P \\]

is square. Then

\\[ \operatorname{adj}(P_I)E_I P = \det(P_I)I\_\omega = p_I I\_\omega. \\]

Consequently,

\\[ X(\lambda) = \sum_I u_I(\lambda)\operatorname{adj}(P_I(\lambda))E_I \\]

satisfies

\\[ X(\lambda)P(\lambda)=I\_\omega. \\]

Since every entry of \\(\operatorname{adj}(P_I)\\) has degree at most \\(\omega-1\\), this construction gives

\\[ \boxed{\deg X\leq 2\omega-2.} \\]

Thus the reduced spectral condition has a polynomial-size certificate.

## 6.2 Why this matters for complexity

Instead of introducing a separate Bézout multiplier for every maximal minor, introduce one unknown polynomial matrix

\\[ X(\lambda)=X_0+X_1\lambda+\cdots+X\_{2\omega-2}\lambda^{2\omega-2} \\]

and impose

\\[ \boxed{ X(\lambda)(\lambda U-G)=I\_\omega. } \\]

This is a polynomial identity. Equating coefficients produces \\(2\omega\\) matrix equations:

\\[ \begin{aligned} -X_0G&=I\_\omega,\\\ X\_{j-1}U-X_jG&=0 && (1\leq j\leq 2\omega-2),\\\ X\_{2\omega-2}U&=0. \end{aligned} \\]

The exact indexing follows by expanding the product; there are coefficient equations for degrees \\(0,\ldots,2\omega-1\\).

The number of scalar unknowns in the \\(X_j\\)'s is

\\[ (2\omega-1)\omega q, \\]

which is polynomial in \\(q,\omega\\).

This is a significant improvement over explicit enumeration of all maximal minors.

It also provides a direct way to encode spectral feasibility as an existential polynomial system.

### Important qualification

The left-inverse certificate is valid because \\(P(\lambda)\\) has full column normal rank and the gcd of its maximal minors is a unit. It is exactly the finite-spectral-point condition under discussion.

It does not by itself encode the rank condition on \\(U\\). That must still be imposed separately.

For example, full column rank of \\(U\\) can be expressed by introducing a left inverse \\(J\\) satisfying

\\[ JU=I\_\omega. \\]

This observation will be useful in the next section.

# 7. Question 3: make the compatibility relations part of the input

Yes. I think this is the cleanest formulation of the target-space problem.

The exact image theorem allows us to remove the ambient unknown \\(R\\) and replace it by an explicit linear compatibility space.

## 7.1 Define the compatible-target problem

Suppose the fixed top rows give

\\[ H_0\in\mathbb R^{r\times k}, \qquad H\_{A,0}\in\mathbb R^{r\times k}. \\]

Suppose the admissible lower-row pairs form a linear subspace

\\[ \mathscr C \subseteq \mathbb R^{m\times k}\times\mathbb R^{m\times k}. \\]

For the original fixed-row problem, this subspace is

\\[ \boxed{ \mathscr C = \left\\{ (B_1,B_2): B_1v+B_2w=0 \text{ for every }(v,w)\in\ker T \right\\}. } \\]

The target matrices are

\\[ H=\begin{bmatrix}H_0\\\B_1\end{bmatrix}, \qquad H_A=\begin{bmatrix}H\_{A,0}\\\B_2\end{bmatrix}. \\]

Now define:

\\[ \boxed{ \begin{aligned} \mathrm{CTS}:\quad &\text{Given }H_0,H\_{A,0},\mathscr C,\\\ &\text{does there exist }(B_1,B_2)\in\mathscr C\\\ &\text{such that }\ker H\subseteq\ker H_A\\\ &\text{and the reduced pencil has no finite rank drop?} \end{aligned} } \\]

I call this the compatible-target spectral feasibility problem.

This formulation directly incorporates the fixed-row compatibility conditions as part of the input.

## 7.2 Does this remove the fixed-row discussion?

It removes it from the abstract complexity statement, but not from the proof that the abstract problem captures the original observer problem.

There are two logically distinct results:

1\. Reduction from the observer problem to compatible-target feasibility.

Given \\(A,C,L_0\\), compute \\(K,N_K,T\\), the fixed top-row matrices, and a basis of \\(\ker T\\). This produces the compatibility space \\(\mathscr C\\).

2\. Complexity analysis of compatible-target feasibility.

Treat the compatibility relations as part of the input and study the resulting family of polynomial constraints.

The first result uses Proposition 2. The second no longer needs to mention \\(R\\), \\(A|\_K\\), or the ambient extension argument.

That is precisely the separation you are looking for.

## 7.3 A caveat: the abstract problem is potentially more general

If \\(\mathscr C\\) is allowed to be an arbitrary linear subspace, then \\(\mathrm{CTS}\\) may include compatible-target families that cannot arise from the particular observer construction.

In the original problem, the compatibility subspace has the special form

\\[ \mathscr C=\operatorname{im}\Theta, \qquad \Theta(R)=(RN_K,RAN_K). \\]

Equivalently, it is defined by a subspace \\(\ker T\\) with the special structure induced by

\\[ T(v,w)=v+Aw. \\]

Therefore, I recommend defining two problems:

- General CTS: arbitrary rational linear compatibility relations.
- Observer-induced CTS: compatibility relations arising from \\(T(v,w)=v+Aw\\), together with the fixed top-row data.

The general problem may be useful for complexity reductions and for identifying the intrinsic algebraic difficulty. But a hardness result for general CTS does not automatically prove hardness of the observer-induced problem.

To establish equivalence, one would need either:

- a representation theorem showing that the relevant general compatibility instances can be realised by observer data; or
- a direct reduction from the general problem to the observer-induced problem.

Without such a result, the general formulation is a useful abstraction, not a complexity-equivalent replacement.

# 8. A polynomial-size existential formulation

Combining the preceding ideas gives a particularly clean formulation of the fixed-order feasibility problem.

Let

\\[ H(R)=\mathcal L(R)N_K,\qquad H_A(R)=\mathcal L(R)AN_K. \\]

Fix a candidate rank \\(\omega\\). We want to express

\\[ \operatorname{rank}H=\omega,\qquad \ker H\subseteq\ker H_A, \\]

and spectral feasibility.

Instead of selecting a column chart and enumerating minors, introduce matrices

\\[ U\in\mathbb R^{q\times\omega},\quad V\in\mathbb R^{\omega\times k},\quad G\in\mathbb R^{q\times\omega}. \\]

Impose

\\[ H=UV,\qquad H_A=GV. \\]

To enforce full column rank of \\(U\\), introduce

\\[ J\in\mathbb R^{\omega\times q}, \qquad JU=I\_\omega. \\]

To enforce full row rank of \\(V\\), introduce

\\[ Z\in\mathbb R^{k\times\omega}, \qquad VZ=I\_\omega. \\]

Then

\\[ \operatorname{rank}H=\omega. \\]

Moreover, the factorisation \\(H_A=GV\\) is equivalent to

\\[ \ker H\subseteq\ker H_A. \\]

The reduced pencil is

\\[ P(\lambda)=\lambda U-G. \\]

Introduce

\\[ X(\lambda)=\sum\_{j=0}^{2\omega-2}X_j\lambda^j, \qquad X_j\in\mathbb R^{\omega\times q}, \\]

and impose

\\[ \boxed{ X(\lambda)(\lambda U-G)=I\_\omega. } \\]

This is a finite system of polynomial equations in the entries of

\\[ R,U,V,G,J,Z,X_0,\ldots,X\_{2\omega-2}. \\]

For \\(\omega=0\\), use the separate branch \\(H=H_A=0\\); no polynomial left-inverse variables are needed.

Thus, for each \\(\omega\\), the spectral feasibility problem has a polynomial-size existential real-algebraic formulation.

The total problem is a finite disjunction over

\\[ 0\leq\omega\leq\min(q,k). \\]

This is a useful result because it shows that the apparent exponential number of maximal minors is not an inherent obstacle to an existential formulation.

It also gives a precise route to an upper-bound statement:

> For rational input and real existential \\(R\\), fixed-order spectral feasibility belongs to the existential theory of the reals, under the stated explicit matrix encoding and the polynomial-size certificate formulation above.

This is an upper-bound classification, not a hardness result. It does not show that the problem is \\(\exists\mathbb R\\)-complete.

# 9. Recommended complexity statements for the paper

I would use the following hierarchy.

| Problem                             | Mathematical question                                                       | Recommended status                      |
| ----------------------------------- | --------------------------------------------------------------------------- | --------------------------------------- |
| Candidate verification              | Does a supplied \\(R\\) satisfy (5a), (5b)?                                 | Algorithmic verification problem        |
| Zero-rank feasibility               | Is \\((H,H_A)=(0,0)\\) attainable?                                          | Linear consistency / fixed top-row test |
| Rank-one candidate verification     | Is \\(\operatorname{rank}[u\ g]=2\\)?                                       | Exact quadratic criterion               |
| Rank-one generic feasibility        | Do the wedge polynomials fail to vanish identically on the relevant family? | Algebraic identity question             |
| Fixed-order synthesis               | Does there exist a real \\(R\\) satisfying (5a), (5b)?                      | \\(\exists\mathbb R\\) upper bound      |
| General compatible-target synthesis | Does a compatible pair with spectral feasibility exist?                     | Abstract algebraic decision problem     |
| Higher-rank strata                  | Does feasibility hold for a specified \\(\omega\geq2\\)?                    | Open structural and complexity question |

The most important distinction is between candidate verification and existential synthesis. The first is an algorithmic question about one supplied matrix. The second asks whether a suitable matrix exists anywhere in a parameter space. A simple verification criterion does not imply a simple existential decision procedure.

I would not claim a polynomial-time algorithm for the \\(\omega=1\\) existential problem without additional hypotheses on the parametrisation. I would also not claim a complexity threshold at \\(\omega=2\\).

# 10. Final recommendations and a proposed revision of the research plan

The current report is mathematically sound in its main correction. I would make the following changes before treating it as the next stable research checkpoint.

1\. Promote Proposition 2 to the main fixed-row theorem. Proposition 1 should be stated as its surjectivity corollary.

2\. Add an explicit matrix representation of the compatibility equations. If \\(Z\\) is a basis matrix for \\(\ker T\\), write\
\\[\
B_1Z_1+B_2Z_2=0.\
\\]\
This is the form needed for computation and complexity.

3\. Adopt rational input and real existential unknowns as the default. Keep rational \\(R\\) as a separate variant.

4\. Define candidate verification, fixed-order feasibility, and generic feasibility separately. These are three different decision problems.

5\. Use the polynomial left-inverse certificate. This avoids enumerating all maximal minors and gives a polynomial-size existential formulation.

6\. Introduce the compatible-target problem. This cleanly separates the intrinsic spectral question from the fixed-row realisation problem.

7\. Do not claim a complexity boundary at \\(\omega=2\\). The current exact results for \\(\omega=0\\) and \\(\omega=1\\) are useful structural results, but not a complexity classification of the higher-rank problem.

## Overall verdict

Core correction accepted

The corrected fixed-row image theorem is valid. Its exact image formula and dimension formula are both correct, and they provide a better foundation than the original surjectivity claim.

Recommended next theorem

The most valuable next result is the polynomial left-inverse characterisation of the reduced pencil, followed by a formal \\(\exists\mathbb R\\) upper-bound theorem for fixed-order real synthesis.

Complexity classification remains open

The report is right not to claim a complexity boundary at \\(\omega=2\\). The next step should be to establish the precise decision problem and its upper bound before attempting hardness.

In my view, this is a meaningful advance in the research programme: it converts the fixed-row discussion from a potential obstruction into an explicit linear compatibility space, and it gives a route to a polynomial-size algebraic certificate for the spectral condition. The resulting formulation is considerably better suited to both a rigorous paper and subsequent computational or formal verification.