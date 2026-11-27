# Research assessment of the paper and recommendations for revision

**Manuscript:** *Two parameterized algorithms for minimum-order functional observer design* \\(\`q1_parametric_algorithms.md\`\\)

**Research report:** *Paper status and open questions* \\(\`84_paper_status_and_questions.md\`\\)

## 1. Overall assessment

My assessment is that the manuscript has a coherent mathematical direction and a potentially publishable contribution. More importantly, its central strategy is substantially better defined than an attempt to resolve the unrestricted complexity of \\(q1\\) through an ambitious hardness reduction before the underlying algebraic decision problem has been fully consolidated.

The paper has a clear proposed contribution:

1. Compress the functional-observer conditions to a matrix pair \\((H,H_A)\\).
2. Replace the existential choice of the free observer rows by a low-dimensional parametrization.
3. Use rank factorization and a parametric linear-consistency condition to obtain a fixed-order algorithm.
4. Use a polynomial-pencil certificate to encode the spectral condition.
5. Exploit the effective dimension of the free-row space to obtain a second parameterized algorithm.
6. Establish membership in \\(\exists\mathbb R\\), without claiming completeness or hardness.

This is a legitimate algorithmic-complexity programme. The two parameterized results address different sources of complexity:

- The fixed-\\(q\\) result controls the number of algebraic variables.
- The fixed-\\(\kappa\_{\rm obs}\\) result controls the effective dimension of the freely selectable observer data.

That distinction is important. The second result is not merely a restatement of the first: its intended advantage is that the number of free observer rows and the ambient state dimension need not be bounded individually, provided their effective interaction dimension is bounded.

However, I would **not recommend freezing and submitting the current manuscript yet**.

There are several issues that should be resolved before submission. Some are matters of presentation, but others concern the exact mathematical model and the validity of the complexity statements.

My priorities are:

(Must resolve) The distinction between complex algebraic data and real polynomial feasibility, including the use of transpose, Gram matrices, and parameter counts.

(Must resolve) The exact bit-complexity theorem used to deduce unconditional FPT in the binary model.

(Important) The complete proof of the real-algebraic certificate, including the treatment of rank strata and polynomial left inverses.

(Important) The explicit construction and complexity analysis of the fixed-\\(q\\) decision formula.

(Promising) The compression, rank-factorization, free-row parametrization, and Bezout-based spectral reduction.

The central recommendation is to continue developing the algorithmic paper, but to make the mathematical foundations and complexity model completely precise before treating the results as established theorems.

---

## 2. Positioning and originality

### 2.1 What the manuscript contributes beyond the observer characterization

The manuscript correctly distinguishes the observer-characterization problem from the computational problem.

The observer conditions are

\\[ \operatorname{rank} \begin{bmatrix} LA\\\L\\\CA\\\C \end{bmatrix} = \operatorname{rank} \begin{bmatrix} L\\\CA\\\C \end{bmatrix}, \tag{5a} \\]

and

\\[ \operatorname{rank} \begin{bmatrix} \lambda L-LA\\\CA\\\C \end{bmatrix} = \operatorname{rank} \begin{bmatrix} L\\\CA\\\C \end{bmatrix}, \quad \forall\lambda\in\mathbb C. \tag{5b} \\]

The characterization literature addresses the existence of functional observers, their possible orders, and their construction.

Your paper addresses a different question:

> Given rational input data and an order bound, how computationally difficult is it to determine whether the required free observer rows exist?

This distinction should be made central to the introduction.

The existence of an algebraic characterization does not automatically give an efficient algorithm. In particular, the presence of a universal spectral condition and an existentially chosen matrix \\(R\\) makes the complexity question nontrivial.

The manuscript's most useful contribution is therefore not simply another characterization of minimum-order observers. It is the identification of two structural parameters that control the computational cost of deciding observer feasibility.

### 2.2 The two parameterized results are genuinely complementary

The first theorem is

\\[ T\leq \mathcal L^{O(q^2)}. \\]

Its advantage is that the complexity is polynomial in the input length whenever \\(q\\) is fixed.

Its limitation is that the exponent depends on \\(q\\).

The second theorem introduces

\\[ d_0=\operatorname{rank}[N\ AN] \\]

and

\\[ \kappa\_{\rm obs}=r d_0, \qquad r=q-r_0. \\]

Its intended bound is

\\[ T\leq f(\kappa\_{\rm obs})\operatorname{poly}(\mathcal L). \\]

This is stronger in the parameterized-complexity sense: the polynomial exponent is independent of \\(\kappa\_{\rm obs}\\).

The distinction should be emphasized more carefully.

| Feature                 | Fixed-order theorem              | Effective-dimension theorem                   |
| ----------------------- | -------------------------------- | --------------------------------------------- |
| Parameter               | \\(q\\)                          | \\(\kappa\_{\rm obs}\\)                       |
| Main reduction          | Pivot factorization              | Direct free-row parametrization               |
| Main advantage          | Polynomial time for fixed order  | FPT with respect to effective dimension       |
| Main limitation         | Parameter-dependent exponent     | Depends on real-algebraic feasibility bound   |
| Main structural insight | Low-dimensional pencil variables | Low-dimensional space of selectable row pairs |

A particularly useful observation is

\\[ k\leq d_0\leq \kappa\_{\rm obs} \quad (r\geq 1). \\]

Thus, bounded effective dimension also bounds the dimension \\(k\\) of the compressed state space.

This is what makes the second algorithm plausible: the number of relevant compressed columns is itself bounded by the parameter.

### 2.3 Recommended positioning

I recommend positioning the paper as an **algorithmic and parameterized-complexity paper**, not as a structural paper with algorithms as secondary applications.

The structural lemmas are important, but their role is to establish the algorithms.

The title is appropriate:

*Two parameterized algorithms for minimum-order functional observer design.*

I would retain it.

The abstract should, however, distinguish three levels of results:

- An unconditional fixed-order polynomial-time result, if the proof is completed.
- An FPT result in the real-RAM model.
- A bit-complexity FPT result only if the precise real-algebraic decision bound supports it.

These are not interchangeable claims.

### 2.4 Is the contribution sufficiently strong?

Potentially yes, but the answer depends on the final status of Theorem 3.

If both parameterized algorithms are rigorously established, the paper has a coherent contribution even without hardness.

In particular, the effective-dimension theorem gives a structural explanation for tractability that is not apparent from the original observer equations.

However, if the second theorem remains only a real-RAM result, the manuscript will need a more careful discussion of its computational significance.

The paper should not compensate for an unresolved bit-complexity issue by presenting the real-RAM theorem as ordinary binary-input FPT.

---

## 3. The Renegar issue: an important conclusion

The status report identifies the Renegar bit-complexity bound as the principal unresolved technical issue. I investigated the original 1992 source rather than relying on secondary summaries.

The relevant reference is:

James Renegar, *On the Computational Complexity and Geometry of the First-Order Theory of the Reals. Part II: The General Decision Problem. Preliminaries for Quantifier Elimination*, Journal of Symbolic Computation 13 (1992), 301–327.

The original paper is available through Renegar's Part II paper. The theorem statement explicitly distinguishes the real-number model from the sequential bit model. In the integer-coefficient case, its bit bound has the form

\\[ B(\log B)(\log\log B)(sD)^{O(N)}, \\]

up to the notation and polynomial factors used in the original theorem, where:

- \\(N\\) is the number of real variables;
- \\(s\\) is the number of polynomials;
- \\(D\\) is their maximum degree;
- \\(B\\) is the maximum coefficient bit length.

The original theorem states the sequential bit bound at the beginning of the paper, rather than merely asserting a real-RAM bound.

This is significant for your manuscript.

### 3.1 Consequence for Theorem 3

The manuscript has the following estimates:

\\[ N=f(\kappa\_{\rm obs}), \\]\\[ s=f(\kappa\_{\rm obs}), \\]\\[ D=f(\kappa\_{\rm obs}), \\]

and

\\[ B=f(\kappa\_{\rm obs})\operatorname{poly}(\mathcal L). \\]

Substitution into the Renegar bound gives

\\[ \begin{aligned} T &\leq B(\log B)(\log\log B)(sD)^{O(N)} \\\ &= f(\kappa\_{\rm obs}) \operatorname{poly}(\mathcal L). \end{aligned} \\]

The reason is that every factor depending exponentially on \\(N\\) depends only on \\(\kappa\_{\rm obs}\\). The coefficient-bit-length contribution remains polynomial in the original input length, with an exponent independent of the parameter.

Therefore, **the conditional bit-model conclusion in Corollary 3b appears capable of being strengthened to an unconditional bit-model FPT theorem using Renegar's original result.**

This is my recommendation:

1. Retain the real-RAM theorem.
2. Retain the bit-model FPT conclusion.
3. Remove the conditional wording from Corollary 3b once the exact theorem and its hypotheses have been checked against the constructed formula.
4. State the bit bound explicitly, including the dependence on coefficient bit length.

There is one qualification: the coefficient-length estimate in your own construction must be established, not merely asserted. In particular, the coefficients produced by the Gram matrices, elementary symmetric polynomials, and Cauchy–Binet expansion must have bit length bounded by

\\[ f(\kappa\_{\rm obs})\operatorname{poly}(\mathcal L). \\]

The manuscript already gives an outline of this argument in Appendix A.5. It should be made a formal part of the theorem proof.

### 3.2 Why this changes the paper

Without the bit-model result, the second theorem is principally a real-algebraic algorithmic result.

With the bit-model result, the paper establishes an ordinary parameterized complexity statement for rational input:

\\[ \boxed{ \mathsf{DEC}\in\operatorname{FPT}(\kappa\_{\rm obs}). } \\]

That is substantially more satisfactory as a theoretical computer science contribution.

I would make this a central theorem rather than burying it in a conditional corollary.

---

## 4. Critical mathematical issue: the coefficient field and realification

This is the first issue I would resolve before further formalization.

The manuscript begins with

\\[ A\in\mathbb C^{n\times n},\qquad C\in\mathbb C^{p\times n},\qquad L_0\in\mathbb C^{r_0\times n}, \\]

and says that the decision problem is over \\(\mathbb C\\), with standard realification of complex variables.

However, several subsequent lemmas are stated for real matrices and use ordinary transposes:

\\[ MM^{\mathsf T},\qquad H^{\mathsf T}H,\qquad B^{\mathsf T}B. \\]

The distinction is mathematically essential.

### 4.1 The Gram identity is not valid over arbitrary complex matrices

For real matrices,

\\[ \operatorname{im}(MM^{\mathsf T}) = \operatorname{im}(M). \\]

For complex matrices, the corresponding statement with ordinary transpose is false in general.

For example, take

\\[ M=\begin{bmatrix}1&i\end{bmatrix}. \\]

Then

\\[ MM^{\mathsf T}=1+i^2=0, \\]

although \\(M\\) has rank one.

Consequently, the rank-consistency criterion in Lemma C cannot be applied to arbitrary complex matrices using \\(MM^{\mathsf T}\\).

The correct complex identity is

\\[ \operatorname{im}(MM^\*) = \operatorname{im}(M), \\]

where \\(M^\*\\) denotes the conjugate transpose.

Thus, for complex \\(M,c\\),

\\[ \boxed{ \exists b\in\mathbb C^m:\ Mb=c \iff \operatorname{rank}(MM^\*) = \operatorname{rank}(MM^\*+cc^\*). } \\]

This is the appropriate Hermitian analogue of Lemma C.

Similarly, the compressed rank condition should use

\\[ G_H=H^\*H, \\]

and

\\[ G_S=H^\*H+H_A^\*H_A. \\]

These are Hermitian positive semidefinite matrices, so their elementary symmetric functions have the required nonnegativity and rank-detection properties.

### 4.2 The spectral certificate also needs a field-consistent formulation

The manuscript establishes

\\[ e_0\in\operatorname{row}B \iff \exists x:\ B^{\mathsf T}Bx=e_0. \\]

This is correct for real \\(B\\).

For complex \\(B\\), the corresponding formulation is

\\[ \boxed{ e_0\in\operatorname{row}B \iff \exists x\in\mathbb C^{2\omega}: B^{\mathsf T}\overline B\\,x=e_0. } \\]

Here \\(B^{\mathsf T}\overline B\\) is Hermitian positive semidefinite and has the same column space as \\(B^{\mathsf T}\\).

Its complex equation can be converted into two real polynomial equations per complex scalar equation.

An alternative is to realify the entire coefficient matrix and use an ordinary real Gram matrix.

The same issue affects the Cauchy–Binet compression. For complex coefficients, the kernel must be constructed with conjugation so that its coefficient matrix represents the Hermitian Gram matrix, rather than the bilinear expression obtained from an ordinary transpose.

### 4.3 The parameter count must match the field

There are two possible mathematical conventions.

**Convention A: real observer design.**

If the intended problem is

\\[ A,C,L_0\in\mathbb Q, \qquad R\in\mathbb R^{r\times n}, \\]

then the current real-coordinate parameter count is appropriate:

\\[ \kappa\_{\rm obs}=rd_0. \\]

The spectral parameter \\(\lambda\\) can still range over \\(\mathbb C\\). There is no conflict between real observer matrices and a complex spectral parameter.

This is arguably the cleanest convention for a control-theoretic observer-design paper.

**Convention B: complex observer design.**

If \\(R\\) is allowed to be complex, then each free row requires \\(d_0\\) complex coordinates, corresponding to \\(2d_0\\) real coordinates.

The real algebraic variable count becomes

\\[ 2rd_0=2\kappa\_{\rm obs}. \\]

The spectral certificate must also be realified consistently.

The FPT result survives because multiplying the parameter by a constant does not change fixed-parameter tractability:

\\[ f(2\kappa\_{\rm obs}) = \widetilde f(\kappa\_{\rm obs}). \\]

But the proof as currently written cannot simply alternate between these two conventions.

### 4.4 My recommendation

I recommend explicitly adopting Convention A if it agrees with the intended functional-observer problem.

Then revise the opening definitions to say:

\\[ A,C,L_0\text{ have rational entries},\qquad R\text{ is real}, \\]

while retaining

\\[ \lambda\in\mathbb C \\]

in (5b).

This preserves the existing real Gram calculations, the \\(rd_0\\) parameter count, and the real-polynomial Bezout argument.

If complex observer matrices are essential to the problem, adopt Convention B and revise all three Gram constructions consistently.

**Do not leave the current ambiguity in the submitted manuscript.** It affects Lemmas C and D, Theorems 1–3, and the exact parameter count.

---

## 5. Detailed audit of the mathematical arguments

I now turn to the actual proofs. I distinguish between arguments that appear mathematically sound, arguments that need clarification, and arguments that should be corrected before submission.

### 5.1 Lemma A: compression and pencil criterion

(Mathematically sound, with one proof correction)

The compression is the right starting point.

Let

\\[ K_0=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \\]

and let \\(N\\) be a basis matrix for \\(K_0\\). Define

\\[ H=LN,\qquad H_A=LAN. \\]

The central equivalences are

\\[ (5a)\iff \operatorname{row}H_A\subseteq\operatorname{row}H \\]

and

\\[ (5b)\iff \operatorname{rank}(\lambda H-H_A) = \operatorname{rank}H \quad\forall\lambda\in\mathbb C. \\]

These reductions are correct.

**The forward implication in (5a).**

The original rank equality is equivalent to

\\[ \operatorname{row}(LA) \subseteq \operatorname{row}[L;CA;C]. \\]

Restricting the row vectors to \\(K_0\\), the rows of \\(CA\\) and \\(C\\) vanish. Consequently,

\\[ \operatorname{row}(LAN) \subseteq \operatorname{row}(LN). \\]

This gives the desired inclusion.

**The converse.**

Suppose

\\[ H_A=FH. \\]

Then

\\[ (LA-FL)N=0. \\]

Every row of \\(LA-FL\\) therefore annihilates \\(K_0\\). By the annihilator identity,

\\[ K_0^\perp=\operatorname{row}[C;CA], \\]

we obtain

\\[ \operatorname{row}(LA-FL) \subseteq\operatorname{row}[C;CA]. \\]

Hence

\\[ \operatorname{row}(LA) \subseteq\operatorname{row}[L;CA;C], \\]

which proves (5a).

This is a particularly clean argument because it converts a rank equality into a linear factorization.

**A correction is needed in Appendix A.1.**

The manuscript says:

> Right multiplication by the full-column-rank matrix \\(N\\) preserves rank.

This statement is false in general.

A full-column-rank right multiplier need not preserve the rank of an arbitrary matrix. For example,

\\[ I_2 \begin{bmatrix}1\\\0\end{bmatrix} = \begin{bmatrix}1\\\0\end{bmatrix} \\]

has rank one, whereas \\(I_2\\) has rank two.

The intended argument is restriction to \\(K_0\\), or equivalently passage to the quotient by \\(\operatorname{row}[C;CA]\\). It does not require preservation of the original matrix rank.

I recommend replacing that sentence with the following statement:

\\[ \operatorname{rank} \begin{bmatrix} J\\\M \end{bmatrix} = \operatorname{rank}J+ \operatorname{rank}(MN), \\]

where \\(N\\) is a basis of \\(\ker J\\), provided the row spaces are interpreted over the same field.

This identity follows because the restriction map from row vectors to functionals on \\(\ker J\\) has kernel \\(\operatorname{row}J\\). Thus, the dimension of the additional row space contributed by \\(M\\) is precisely \\(\operatorname{rank}(MN)\\).

Apply it with

\\[ J=\begin{bmatrix}C\\\CA\end{bmatrix}. \\]

Then

\\[ \operatorname{rank} \begin{bmatrix} CA\\\C\\\\\lambda L-LA \end{bmatrix} = \operatorname{rank}J+ \operatorname{rank}(\lambda H-H_A), \\]

and

\\[ \operatorname{rank} \begin{bmatrix} L\\\CA\\\C \end{bmatrix} = \operatorname{rank}J+\operatorname{rank}H. \\]

This proves the pencil criterion directly.

**Another small improvement:** explicitly state that

\\[ \operatorname{rank}(\lambda H-H_A)\leq\omega \\]

follows from (5a), since \\(H_A=FH\\) implies

\\[ \lambda H-H_A=(\lambda I-F)H. \\]

Then the maximal minors of order \\(\omega\\) are exactly the minors needed to detect whether the rank drops below \\(\omega\\).

The gcd formulation follows from the fact that a finite family of univariate complex polynomials has a common complex root precisely when its gcd has positive degree.

One must handle \\(\omega=0\\) separately.

**Recommendation:** retain Lemma A. It is one of the strongest and most reusable parts of the manuscript. Correct the Appendix A.1 sentence and make the quotient-space argument the principal proof.

Reference:&#x20;

---

### 5.2 Lemma B: free-row parametrization

(Correct and structurally important)

The definition

\\[ \mathcal T=\operatorname{row}[N\ AN] \\]

is natural.

For a free observer row \\(r_i\\),

\\[ (H_i,(H_A)\_i)=r_i[N\ AN]. \\]

Therefore the attainable pairs are exactly the elements of \\(\mathcal T\\).

The map

\\[ \Phi:\mathbb F^{1\times n} \longrightarrow \mathbb F^{1\times 2k}, \qquad r\longmapsto r[N\ AN], \\]

where \\(\mathbb F\\) is the chosen coefficient field, has image \\(\mathcal T\\). Thus

\\[ \dim\mathcal T=\operatorname{rank}[N\ AN]=d_0. \\]

Each free row requires exactly \\(d_0\\) coordinates in a basis of this image.

For \\(r\\) free rows, the total number of coordinates is

\\[ \kappa\_{\rm obs}=rd_0. \\]

The inequalities

\\[ k\leq d_0\leq\kappa\_{\rm obs} \\]

for \\(r\geq1\\) are also correct.

The first follows because \\(N\\) has full column rank and its columns are included in the stacked matrix \\([N\ AN]\\). The second is immediate.

#### An important algorithmic improvement

The manuscript currently describes choosing a rational basis of \\(\mathcal T\\).

I recommend explaining how this basis is computed.

Since

\\[ \mathcal T=\operatorname{row}[N\ AN], \\]

one can compute a rational row-space basis using exact Gaussian elimination.

Moreover, if the algorithm is only deciding existence, it does not need to recover the original free row \\(r_i\\). It can work directly with coordinates of the attainable pair.

If an actual observer construction is later desired, a rational right inverse of the map \\(\Phi\\), restricted to its image, can recover a representative row.

This distinction is useful: the decision algorithm should not carry unnecessary variables corresponding to the kernel of \\(\Phi\\).

#### One additional conceptual point

The parameter \\(d_0\\) measures the number of independent ways a free row can affect the two compressed matrices simultaneously.

It is not merely the dimension of the compressed state space.

In fact,

\\[ d_0 = \dim\operatorname{span} \left\\{ (rN,rAN):r\in\mathbb F^{1\times n} \right\\}. \\]

This makes \\(\kappa\_{\rm obs}\\) a meaningful effective-design parameter.

I would emphasize this interpretation in the introduction.

Reference:

---

### 5.3 Lemma C: rank factorization and linear consistency

(Core reduction is sound)

This section is important because it eliminates a potentially much larger collection of unknown entries.

For \\(\omega>0\\), choose a column set \\(J\\) such that

\\[ X=H\_{:,J} \\]

has full column rank.

Then

\\[ H=XB, \qquad B\_{:,J}=I\_\omega. \\]

This is a valid rank factorization.

The normalization \\(B\_{:,J}=I\_\omega\\) is particularly useful because it removes the nonuniqueness of general rank factorizations.

The substitution

\\[ G=FX \\]

is also correct.

Indeed,

\\[ H_A=FH=FXB=GB. \\]

Conversely, if \\(H_A=GB\\), and \\(X_LX=I\_\omega\\), then

\\[ F=GX_L \\]

satisfies

\\[ FH=GX_LXB=GB=H_A. \\]

This proves that the factorization preserves the original row-space condition.

#### The rank-consistency criterion

The proposed criterion is

\\[ \exists b:\ Mb=c \iff \operatorname{rank}(MM^{\mathsf T}) = \operatorname{rank}(MM^{\mathsf T}+cc^{\mathsf T}). \\]

For real matrices, this is correct.

The proof is straightforward:

\\[ Mb=c \iff c\in\operatorname{im}M. \\]

Furthermore,

\\[ \operatorname{im}(MM^{\mathsf T}) = \operatorname{im}M, \\]

and

\\[ \operatorname{im}(MM^{\mathsf T}+cc^{\mathsf T}) = \operatorname{im}[M\ c]. \\]

Thus the equality of ranks is exactly the consistency condition.

The elementary symmetric polynomial formulation is also correct for positive semidefinite matrices:

\\[ e_t(\Gamma)>0,\qquad e\_{t+1}(\Gamma)=0 \\]

is equivalent to

\\[ \operatorname{rank}\Gamma=t. \\]

The reason is that the eigenvalues are all nonnegative, and \\(e_t\\) is the sum of all products of \\(t\\) distinct eigenvalues.

The disjunction over possible \\(t\\) therefore gives a polynomial formula for consistency.

#### A point that should be made more explicit

The parametric system

\\[ M(X,G)b=c(X,G) \\]

must be written out sufficiently explicitly that a reader can verify the polynomial dependence on \\(X,G\\).

In particular, explain:

1. Which entries of \\(B\\) are fixed by the pivot normalization.
2. Which entries are included in \\(b\\).
3. Which equations arise from the fixed rows \\(L_0\\).
4. Which equations impose membership of each free row pair in \\(\mathcal T\\).
5. Why every equation is linear in \\(b\\).
6. Why \\(M\\) and \\(c\\) have polynomial entries in \\(X,G\\).

The current manuscript gives the correct architecture, but the construction deserves a compact displayed derivation.

This will make the fixed-order algorithm much easier to audit.

#### An additional notation problem

The letter \\(B\\) is used both for the rank-factorization matrix and for the spectral coefficient matrix in Lemma D.

I recommend using different notation, for example:

\\[ H=XB, \qquad \mathscr B=\text{spectral coefficient matrix}. \\]

This avoids unnecessary confusion when the two constructions are combined.

Reference:

---

### 5.4 Lemma D: the Bezout spectral certificate

(The central idea is correct)

This is probably the most interesting algebraic part of the paper.

The condition

\\[ \operatorname{rank}(\lambda X-G)=\omega \quad\forall\lambda\in\mathbb C \\]

is converted into a finite-dimensional polynomial identity.

Let

\\[ Q(\lambda)=\lambda X-G. \\]

Let \\(f_1,\ldots,f_s\\) be its maximal minors.

Then

\\[ \operatorname{rank}Q(\lambda)=\omega \quad\forall\lambda\in\mathbb C \\]

is equivalent to the absence of a common complex root of the \\(f_i\\).

Equivalently,

\\[ \gcd(f_1,\ldots,f_s)=1. \\]

The next step is the bounded-degree Bezout identity.

#### 5.4.1 The degree bound

The manuscript asserts

\\[ \deg f_i\leq\omega \\]

and

\\[ \gcd(f_1,\ldots,f_s)=1 \Longrightarrow \exists g_i: \quad \deg g_i<\omega, \quad \sum_i g_i f_i=1. \\]

For \\(\omega\geq1\\), this is correct.

The generic-combination argument is valid.

Choose a nonzero linear combination

\\[ g=\sum_i a_i f_i. \\]

At every complex root \\(\alpha\\) of \\(g\\), not all \\(f_i(\alpha)\\) vanish. Otherwise, \\(\alpha\\) would be a common root of the original family.

Consequently, the condition

\\[ h(\alpha)=0, \qquad h=\sum_i b_i f_i, \\]

defines a proper linear condition on the coefficients \\(b_i\\).

There are only finitely many roots of \\(g\\). Hence one can choose \\(b_i\\) outside the finite union of these proper linear subspaces.

The resulting \\(g,h\\) are coprime.

The Euclidean algorithm gives

\\[ ug+vh=1 \\]

with

\\[ \deg u<\deg h\leq\omega, \qquad \deg v<\deg g\leq\omega. \\]

Substituting the definitions of \\(g,h\\) yields

\\[ 1=\sum_i(ua_i+vb_i)f_i. \\]

The new multipliers have degree strictly less than \\(\omega\\).

There is no missing genericity assumption beyond the nonexistence of a common root and the condition \\(\omega\geq1\\).

I would, however, formulate the proof over the actual coefficient field. If the \\(f_i\\) are complex polynomials, the combinations and Bezout multipliers should be complex polynomials. If the input and observer variables are real, the real-polynomial proof in the manuscript applies.

#### 5.4.2 The coefficient-matrix identification

The matrix construction is also correct.

Write

\\[ f_i(\lambda)=\sum\_{a=0}^{\omega}c\_{i,a}\lambda^a. \\]

Define

\\[ \mathscr B\_{(i,j),t}=c\_{i,t-j}, \\]

where

\\[ 0\leq j<\omega, \qquad 0\leq t<2\omega. \\]

Each row is exactly the coefficient vector of

\\[ \lambda^j f_i(\lambda). \\]

Therefore

\\[ \operatorname{row}\mathscr B = \left\\{ \operatorname{coeff} \left( \sum_i g_i f_i \right): \deg g_i<\omega \right\\}. \\]

In particular,

\\[ (5b) \iff e_0\in\operatorname{row}\mathscr B. \\]

The indexing is correct.

One should explicitly define

\\[ c\_{i,a}=0 \\]

whenever \\(a<0\\) or \\(a>\omega\\). This eliminates any ambiguity in the shifted indexing.

#### 5.4.3 The Gram certificate

For real \\(\mathscr B\\),

\\[ \operatorname{row}\mathscr B = \operatorname{im}(\mathscr B^{\mathsf T}\mathscr B). \\]

Hence

\\[ e_0\in\operatorname{row}\mathscr B \iff \exists x: \mathscr B^{\mathsf T}\mathscr Bx=e_0. \\]

This is a particularly useful conversion because it replaces a row-space membership condition by a finite system of polynomial equations.

There is no need to quantify the Bezout polynomials individually after this conversion.

This is exactly the type of reduction that makes the parameterized algorithm practical at the level of algebraic formulation.

#### 5.4.4 Cauchy–Binet compression

The kernel

\\[ K(\lambda,\mu) = \sum\_{|J|=\omega} \det\left( Q(\lambda)\_{:,J}^{\mathsf T} Q(\mu)\_{:,J} \right) \\]

is a good construction.

By Cauchy–Binet,

\\[ K(\lambda,\mu) = \sum\_{I,J} f\_{I,J}(\lambda)f\_{I,J}(\mu). \\]

Thus the coefficient matrix of \\(K\\) contains the information needed to reconstruct the Gram matrix of the shifted coefficient rows.

The shifted formula

\\[ (\mathscr B^{\mathsf T}\mathscr B)\_{t,t'} = \sum\_{j=0}^{\omega-1} S\_{t-j,t'-j} \\]

is correct.

The important algorithmic gain is that one need not explicitly enumerate all row and column pairs of maximal minors. The determinant of the smaller Gram matrix already sums over the row choices.

This is particularly valuable in Theorem 3, where \\(q\\) may be large but \\(\omega\leq\kappa\_{\rm obs}\\).

**I do not consider the absence of a Lean Cauchy–Binet theorem a reason to delay submission.** Cauchy–Binet is a standard mathematical identity. A complete paper proof is sufficient.

I would nevertheless include a short proof of the rectangular version in Appendix A, as the current draft does.

Reference:&#x20;

---

### 5.5 Appendix B: polynomial left inverses and \\(\exists\mathbb R\\)

(Requires substantial clarification)

The central statement is

\\[ Q(\lambda)\text{ has full column rank for all }\lambda\in\mathbb C \\]

if and only if there exists a polynomial matrix \\(S(\lambda)\\) satisfying

\\[ S(\lambda)Q(\lambda)=I\_\omega. \\]

For a univariate polynomial matrix, this is correct.

The maximal minors generate the unit ideal precisely when they have no common complex root. The Bezout identity and adjugate construction then produce a polynomial left inverse.

#### 5.5.1 The degree bound \\(2\omega-2\\)

The manuscript correctly identifies the bound

\\[ \boxed{\deg S\leq 2\omega-2.} \\]

The construction is:

\\[ S_IQ=f_I I\_\omega, \\]

where

\\[ f_I=\det Q_I. \\]

Since

\\[ \deg f_I\leq\omega \\]

and

\\[ \deg\operatorname{adj}(Q_I)\leq\omega-1, \\]

the bounded-degree Bezout multipliers satisfy

\\[ \deg g_I<\omega. \\]

Therefore

\\[ S=\sum_I g_I S_I \\]

has degree at most

\\[ (\omega-1)+(\omega-1)=2\omega-2. \\]

This is a valid sufficient bound.

I would not claim that it is sharp without a separate lower-bound example. The construction proves an upper bound, not optimality.

#### 5.5.2 Correct the terminology concerning polynomial rank

Appendix B says:

> If \\(Q\\) has rank \\(\omega\\) over \\(\mathbb C[\lambda]\\), the maximal minors have gcd one.

This needs correction.

Full column rank over the fraction field \\(\mathbb C(\lambda)\\) only guarantees that at least one maximal minor is nonzero. It does not imply that the maximal minors have gcd one.

For example,

\\[ Q(\lambda)= \begin{bmatrix} \lambda\\\ \lambda \end{bmatrix} \\]

has column rank one over \\(\mathbb C(\lambda)\\), but its maximal minors have the common factor \\(\lambda\\).

The correct statement is:

\\[ \boxed{ \operatorname{rank}Q(\lambda)=\omega \quad\text{for every }\lambda\in\mathbb C } \\]

if and only if the maximal minors generate the unit ideal in \\(\mathbb C[\lambda]\\).

Equivalently, \\(Q\\) admits a polynomial left inverse.

This terminology should be corrected throughout Appendix B.

#### 5.5.3 The finite disjunction over rank strata

The final paragraph of Appendix B introduces

\\[ \dim(Z\cap\mathcal V)=s \\]

and says that a finite disjunction over \\(s\\) completes the compact encoding.

This is not adequately explained in the current manuscript.

The objects \\(Z\\) and \\(\mathcal V\\) have not been introduced in the preceding development. A reader cannot reconstruct the meaning of this stratification or verify that the disjunction covers every possible instance.

I recommend removing this unexplained construction and replacing it with a direct rank-factorization encoding.

Here is a cleaner route.

For each

\\[ \omega=0,\ldots,\min(q,k), \\]

introduce matrices

\\[ X\in\mathbb R^{q\times\omega}, \qquad B\in\mathbb R^{\omega\times k}, \qquad G\in\mathbb R^{q\times\omega}. \\]

Require

\\[ H=XB,\qquad H_A=GB. \\]

Enforce full rank by introducing matrices \\(U,V\\) such that

\\[ UX=I\_\omega, \qquad BV=I\_\omega. \\]

These are polynomial equations.

Then impose

\\[ S(\lambda)(\lambda X-G)=I\_\omega \\]

with

\\[ \deg S\leq2\omega-2. \\]

All coefficients of \\(S\\) become existential real variables (or real and imaginary parts in the complex-observer formulation).

This is a complete finite polynomial encoding.

It uses:

- Polynomially many variables.
- Polynomially many equations.
- Polynomially bounded degrees.
- Only \\(O(n)\\) rank-stratum branches.

The equations are bilinear or polynomial, and their size is polynomial in the original matrix dimensions.

The \\(\omega=0\\) case is handled separately by requiring \\(H=H_A=0\\).

This alternative has the additional advantage that it uses the same rank factorization already established in Lemma C.

**My recommendation is to rewrite Appendix B around this encoding.**

It is easier to verify than an unexplained auxiliary stratification and makes Theorem 1 much more convincing.

Reference:

---

## 6. Theorem 2: fixed observer order

(A meaningful XP result; proof needs fuller accounting)

Theorem 2 claims

\\[ T\leq\mathcal L^{O(q^2)}. \\]

The variable count is

\\[ N=2q\omega+2\omega=O(q^2) \\]

for the real formulation in the manuscript.

The polynomial degrees are \\(O(k)\\), and the number of constraints is polynomial in \\(k\\).

This is a valid general strategy for obtaining a fixed-\\(q\\) polynomial-time algorithm.

### 6.1 The pivot-chart enumeration

The algorithm enumerates

\\[ \omega=0,\ldots,q \\]

and the possible pivot sets \\(J\\).

The number of charts is bounded by

\\[ \sum\_{\omega=0}^q\binom{k}{\omega} \leq (q+1)k^q \\]

when \\(k\geq1\\).

For fixed \\(q\\), this is polynomial in \\(k\\).

The chart enumeration is therefore not a problem.

### 6.2 The real-feasibility formula

For each chart, the algorithm must impose:

1. Full column rank of \\(X\\).
2. The fixed-row equations.
3. Free-row membership in \\(\mathcal T\\).
4. Consistency of the parametric linear system.
5. The spectral Bezout certificate.

The rank-consistency condition is a disjunction over possible ranks.

This introduces \\(O(k)\\) additional polynomial conditions, but it does not introduce additional quantified variables.

The number of branches is polynomial for fixed \\(q\\), and the total formula size remains polynomial.

### 6.3 The monomial count

This part of the manuscript is important and should be retained.

With

\\[ N=O(q^2) \\]

variables and degree \\(O(k)\\), the number of monomials in a dense polynomial representation is bounded by

\\[ \binom{O(k)+O(q^2)}{O(q^2)} = k^{O(q^2)}. \\]

Thus, for fixed \\(q\\), polynomial expansion and representation remain polynomial in the original input size.

The chart count contributes another factor of at most \\(k^q\\).

Consequently,

\\[ \mathcal L^{O(q^2)} \\]

is a reasonable coarse bound.

### 6.4 What should be improved

I recommend presenting the theorem as an XP result parameterized by \\(q\\).

Formally,

\\[ \boxed{ \mathsf{DEC}\in\operatorname{XP}(q). } \\]

The theorem implies polynomial-time decidability for every fixed \\(q\\), but it does not establish FPT in \\(q\\).

The manuscript should make this terminology explicit.

Also, distinguish the complexity of the individual decision problem from the optimization problem of finding \\(q\_{\min}\\).

If one tests all possible orders, the running time is not automatically \\(\mathcal L^{O(q^2)}\\) for an unrestricted input \\(q\\).

The theorem is best stated for the language

\\[ \mathsf{DEC} = \left\\{ (A,C,L_0,q): \exists R\text{ satisfying (5a),(5b)} \right\\}. \\]

Then the fixed-\\(q\\) theorem is a parameterized decision result.

The minimum-order problem can be discussed separately.

Reference:&#x20;

---

## 7. Theorem 3: fixed effective dimension

(The strongest potential contribution)

Theorem 3 is the theorem I would emphasize most strongly in the final paper.

The parameter is

\\[ \kappa\_{\rm obs} = r\operatorname{rank}[N\ AN]. \\]

The key inequality is

\\[ k\leq d_0\leq\kappa\_{\rm obs} \\]

for \\(r\geq1\\).

This immediately implies

\\[ k\leq\kappa\_{\rm obs}, \qquad \omega\leq\kappa\_{\rm obs}. \\]

Therefore, every object whose dimension depends on the compressed state dimension is now bounded by the parameter.

### 7.1 Why the direct parametrization is better

Unlike Theorem 2, Theorem 3 does not need to enumerate pivot sets.

Instead, it directly parametrizes the free row pairs.

This gives a finite algebraic system with

\\[ \kappa\_{\rm obs} \\]

free-row coordinates in the real formulation.

The rank condition (5a) can be expressed using

\\[ G_H=H^{\mathsf T}H \\]

and

\\[ G_S=H^{\mathsf T}H+H_A^{\mathsf T}H_A. \\]

For real matrices,

\\[ \operatorname{rank}G_H=\operatorname{rank}H \\]

and

\\[ \operatorname{rank}G_S = \operatorname{rank} \begin{bmatrix}H\\\H_A\end{bmatrix}. \\]

Thus, for a fixed rank stratum \\(\omega\\),

\\[ e\_\omega(G_H)>0 \\]

and

\\[ e\_{\omega+1}(G_S)=0 \\]

are sufficient and necessary for (5a).

This is an elegant way to encode the row-space inclusion without explicitly introducing \\(F\\).

### 7.2 The spectral certificate

The second component is

\\[ \mathscr B^{\mathsf T}\mathscr Bx=e_0. \\]

The Cauchy–Binet kernel computes the required Gram matrix without enumerating all maximal minors.

Since

\\[ \binom{k}{\omega}\leq 2^k \leq 2^{\kappa\_{\rm obs}}, \\]

the number of determinant terms depends only on the parameter.

Each determinant has order at most \\(\kappa\_{\rm obs}\\).

The preprocessing is therefore fixed-parameter bounded, multiplied by polynomial input-processing costs.

This is the central algorithmic advantage.

### 7.3 A point to correct in the variable count

The manuscript states

\\[ N=\kappa\_{\rm obs}+2\omega+1. \\]

This count needs explanation.

The finite choice of \\(\omega\\) is a discrete rank-stratum disjunction, not an ordinary existential real variable.

I recommend stating the variable count as

\\[ N\leq\kappa\_{\rm obs}+2\omega \\]

for the current real formulation, unless the additional variable has a clearly defined purpose.

If a complex formulation is adopted, the number of real variables changes accordingly.

In either case,

\\[ N=f(\kappa\_{\rm obs}) \\]

is the essential fact.

### 7.4 The case \\(r=0\\)

The special case is necessary.

When

\\[ r=0, \\]

there are no free rows, so

\\[ \kappa\_{\rm obs}=0 \\]

regardless of the size of \\(N\\).

It would be incorrect to infer that the entire problem is trivial from the parameter being zero.

The fixed-row instance still requires checking the spectral condition.

The manuscript correctly separates this case and proposes a polynomial left-inverse test.

This is the appropriate approach.

However, the proof should explicitly establish that the rectangular polynomial left-inverse test is polynomial-time computable.

One can compute the maximal minors and their gcd using exact univariate polynomial arithmetic. When the number of rows is part of the input, there are polynomially many minors only if the column dimension \\(\omega\\) is fixed. In the \\(r=0\\) branch, however, \\(\omega\\) need not be fixed.

A more efficient approach is needed if the claimed polynomial-time test is intended for unrestricted \\(\omega\\).

In fact, the particular pencil has degree one and special structure, so a direct polynomial-matrix algorithm may be available. But the manuscript should cite and establish the appropriate complexity result rather than relying solely on the adjugate formula, which explicitly sums over row subsets.

This is a point I would investigate before finalizing Theorem 3.

### 7.5 The bit-model conclusion

With the Renegar issue resolved as discussed above, the intended result is

\\[ \boxed{ \mathsf{DEC}\in \operatorname{FPT}(\kappa\_{\rm obs}) } \\]

in the binary model.

This is the most important theorem of the paper.

Reference:&#x20;

---

## 8. Theorem 1: \\(\exists\mathbb R\\) membership

I support including this theorem.

It is useful for three reasons:

1. It places the decision problem in a recognized complexity class.
2. It establishes a general decidability result independently of the parameterized algorithms.
3. It provides a natural upper-bound framework against which future hardness results can be compared.

However, there is an important distinction between the following statements:

\\[ \mathsf{DEC}\in\exists\mathbb R \\]

and

\\[ q\_{\min}\text{ can be computed in polynomial time}. \\]

The former is a membership result for a decision language. It does not establish the latter.

### 8.1 Define the decision language precisely

I recommend introducing

\\[ \mathsf{FO\mbox{-}DEC} = \left\\{ (A,C,L_0,q): \exists R\text{ satisfying (5a),(5b)} \right\\}. \\]

Then state

\\[ \boxed{\mathsf{FO\mbox{-}DEC}\in\exists\mathbb R.} \\]

The optimization problem is

\\[ q\_{\min} = \min\left\\{ q:\mathsf{FO\mbox{-}DEC}(A,C,L_0,q)=\mathrm{YES} \right\\}. \\]

The optimization problem can be solved using decision calls, but this does not mean that its unrestricted complexity has been resolved.

This terminology should be consistent in the abstract, introduction, theorem statements, and conclusion.

### 8.2 The polynomial left-inverse encoding is the right approach

For

\\[ Q(\lambda)=\lambda X-G, \\]

the condition

\\[ \operatorname{rank}Q(\lambda)=\omega \quad\forall\lambda\in\mathbb C \\]

is equivalent to the existence of a polynomial left inverse

\\[ S(\lambda)Q(\lambda)=I\_\omega. \\]

The bounded-degree construction gives

\\[ \deg S\leq2\omega-2. \\]

Writing

\\[ S(\lambda)= S_0+S_1\lambda+\cdots+ S\_{2\omega-2}\lambda^{2\omega-2}, \\]

the identity

\\[ S(\lambda)(\lambda X-G)=I\_\omega \\]

becomes a finite set of polynomial equations in the entries of the coefficient matrices \\(S_j\\), \\(X\\), and \\(G\\).

The number of unknowns and equations is polynomial in the input dimensions.

The rank factorization encoding from Section 5.5 completes the argument.

This gives a direct proof of \\(\exists\mathbb R\\) membership.

### 8.3 Does the finite disjunction have polynomial size?

Yes, if it is formulated using the rank index

\\[ \omega=0,\ldots,\min(q,k). \\]

There are at most \\(n+1\\) alternatives.

Each alternative has polynomial size.

The total disjunction therefore has polynomial size.

This is preferable to leaving an undefined geometric stratification in Appendix B.

### 8.4 A useful improvement

I suggest making the following observation explicit:

The membership proof does not need the fixed-\\(q\\) pivot-chart enumeration.

It can use an unrestricted existential rank factorization.

This is important because the membership proof should not inherit an unnecessarily complicated chart enumeration from Theorem 2.

It also makes the logical relationship between Theorems 1 and 2 clearer:

- Theorem 1 gives a uniform existential-algebraic representation.
- Theorem 2 gives a more efficient algorithm when \\(q\\) is fixed.
- Theorem 3 gives a more efficient algorithm when \\(\kappa\_{\rm obs}\\) is fixed.

These are three different uses of the same algebraic structure.

---

## 9. Theorem 4: combined bound

The proposed bound is

\\[ T\leq \min\left\\{ \mathcal L^{O(q^2)}, f(\kappa\_{\rm obs})\operatorname{poly}(\mathcal L) \right\\}. \\]

This is mathematically reasonable provided both algorithms solve the same decision problem in the same computational model.

There is, however, a presentation issue.

Theorem 2 is explicitly a bit-complexity statement, while Theorem 3 is initially stated in the real-RAM model.

One should not combine bounds from different computational models without explaining the conversion.

I recommend giving two separate statements.

**Bit model:**

Once the Renegar bit-complexity consequence has been incorporated,

\\[ \boxed{ T\_{\rm bit} \leq \min\left\\{ \mathcal L^{O(q^2)}, f(\kappa\_{\rm obs})\operatorname{poly}(\mathcal L) \right\\}. } \\]

**Real-RAM model:**

Give the corresponding arithmetic-operation bounds separately, using the appropriate dimension-dependent estimates.

The advantage of the combined result is that the algorithm can choose whichever parameter is smaller in the relevant instance.

This is a useful practical interpretation of the two theorems.

Reference:

---

## 10. The Lean verification and computational evidence

The verification programme is a positive feature of the project.

The manuscript reports Lean verification of:

- The compression kernel.
- The free-pair space and dimension count.
- The \\(G=FX\\) substitution.
- The subspace consistency criterion.
- The Bezout core.
- The real sum-of-squares identity.
- The left-inverse/injectivity core.
- The effective-dimension inequalities.

It also reports exact computational checks for the Gram certificate, Cauchy–Binet, shifted indexing, and the rectangular adjugate construction.

This is good research practice, especially for a paper with several layers of algebraic reductions.

Nevertheless, I would be careful about the language used to describe formal verification.

### 10.1 What the Lean development establishes

The Lean kernel establishes the correctness of the formalized statements under their declared assumptions.

It does not automatically establish the correctness of the paper's complete algorithm.

In particular, the following steps remain outside the formalized algebraic kernel:

1. The matrix-to-subspace bridge in Lemma A.
2. The matrix identification of the free-row space.
3. The matrix Gram/rank identity.
4. The degree bookkeeping in the Bezout certificate.
5. The full Cauchy–Binet compression.
6. The real-algebraic complexity estimates.
7. The complete fixed-\\(q\\) and FPT algorithms.

The manuscript correctly acknowledges these limitations.

### 10.2 What I recommend

Do not attempt to formalize the entire paper before submission.

Instead, complete a focused verification pass on the statements with the highest mathematical risk:

- The annihilator/restriction identity used in Lemma A.
- The complex-versus-real Gram identities, according to the final field convention.
- The bounded-degree Bezout construction.
- The Cauchy–Binet coefficient identity.
- The exact \\(r=0\\) polynomial-time procedure.

The Cauchy–Binet argument is elementary enough to present as a conventional proof if formalization remains inconvenient.

### 10.3 How to present the verification record

I would retain Appendix C but make it more precise.

For each declaration, provide:

| Item                 | Formalized result                | Remaining paper-level step           |
| -------------------- | -------------------------------- | ------------------------------------ |
| Compression          | Abstract kernel equivalence      | Matrix restriction argument          |
| Free rows            | Image and dimension              | Matrix identification                |
| Consistency          | Subspace criterion               | Gram/rank translation                |
| Bezout               | Coprime polynomial identity      | Degree bookkeeping                   |
| Spectral certificate | Positivity core                  | Full coefficient-matrix construction |
| FPT                  | Injectivity and dimension bounds | Complete algorithm and complexity    |

The current verification appendix already contains much of this information.

It should be presented as supporting evidence rather than as an alternative proof of the main theorems.

Reference:

---

## 11. Answers to the sixteen questions in the status report

The following gives my direct recommendations on the questions raised in `84_paper_status_and_questions.md`.

### III.1 Positioning and publishability

**Question 1: Is the theorem set coherent and sufficiently strong?**

Yes, provided the proofs are completed.

The three results have distinct roles:

\\[ \mathsf{DEC}\in\exists\mathbb R, \\]\\[ \mathsf{DEC}\in\operatorname{XP}(q), \\]

and

\\[ \mathsf{DEC}\in\operatorname{FPT}(\kappa\_{\rm obs}). \\]

The paper should emphasize that these are upper bounds, not a classification of unrestricted complexity.

The effective-dimension theorem is the principal contribution.

**Question 2: Algorithmic or structural positioning?**

Algorithmic and parameterized complexity.

The structural results should be presented as the mathematical mechanism enabling the algorithms.

**Question 3: Is the fixed-order bound too coarse?**

No.

\\[ \mathcal L^{O(q^2)} \\]

is a meaningful fixed-parameter-dependent polynomial bound.

It establishes polynomial-time decidability for every fixed order.

However, it is an XP-type result rather than FPT in \\(q\\).

It should be a secondary theorem, with the effective-dimension FPT result receiving greater emphasis.

### III.2 Renegar and the bit model

**Question 4: What is the exact bit-complexity form?**

The original Renegar result supports a bound of the form

\\[ B(\log B)(\log\log B)(sD)^{O(N)} \\]

for the existential real decision problem, under the theorem's integer-coefficient and input-encoding conventions.

This supports the manuscript's desired \\((sD)^{O(N)}\operatorname{poly}(B)\\) formulation.

**Question 5: Is it acceptable to state real-RAM FPT and conditional bit FPT?**

It is mathematically acceptable, but unnecessarily conservative if the hypotheses of Renegar's bit theorem are verified.

I recommend making the bit-model result unconditional.

**Question 6: Is there a reference supporting the bit-model consequence?**

Yes. Renegar's 1992 Part II is the appropriate primary reference.

Cite the actual theorem and explicitly specialize it to an existential sentence.

### III.3 Fixed-order complexity

**Question 7: Are the variable and degree counts sufficient?**

The strategy is correct.

The manuscript should additionally state:

- The number of pivot charts.
- The number of rank-consistency branches.
- The total number of polynomial predicates.
- The dense monomial count.
- The coefficient bit-length bound.
- The bit complexity of constructing the formula.

The current estimates are plausible, but these points should be consolidated into one complexity proposition.

### III.4 Proof reliability

**Question 8: Is the Bezout degree bound correct?**

Yes, for \\(\omega\geq1\\).

The generic-combination proof is sound. The coefficient field should be made consistent with the observer-design model.

**Question 9: Is the row-space indexing correct?**

Yes.

The definition

\\[ \mathscr B\_{(i,j),t}=c\_{i,t-j} \\]

correctly represents the coefficient vectors of \\(\lambda^j f_i\\).

**Question 10: Is the rectangular adjugate construction correct?**

Yes.

The identity

\\[ S_IQ=f_I I\_\omega \\]

is correct, and the resulting bound

\\[ \deg S\leq2\omega-2 \\]

is valid.

The manuscript has not established that the bound is optimal.

**Question 11: Must Cauchy–Binet be formalized?**

No.

A conventional complete proof is sufficient.

Formalization would be useful, but it is not a publication requirement.

### III.5 The \\(\exists\mathbb R\\) encoding

**Question 12: Is the polynomial left-inverse degree bound valid on degenerate strata?**

The bound is valid whenever the pencil has full column rank at every complex spectral parameter.

The manuscript should distinguish this condition from ordinary full column rank over the fraction field.

Use the direct rank-factorization encoding described in Section 5.5 of this assessment.

**Question 13: Must the number of disjuncts be bounded?**

Yes.

The rank index ranges over at most \\(n+1\\) values, so the total encoding has polynomial size.

### III.6 Next step

**Question 14: What should happen next?**

My recommendation is:

1. Resolve the coefficient-field convention.
2. Complete the Renegar bit-model justification.
3. Repair the Appendix A.1 rank argument.
4. Rewrite Appendix B with an explicit polynomial-size encoding.
5. Establish the polynomial-time \\(r=0\\) procedure.
6. Complete the complexity estimates.
7. Freeze the paper.

I would not return to unrestricted hardness as the immediate next step.

**Question 15: What is the most likely referee objection?**

The most serious likely objection is not the overlap with Fernando 2026.

It is the rigor of the complexity arguments, especially:

- The real-versus-complex formulation.
- The bit-model conclusion.
- The \\(r=0\\) branch.
- The exact size of the existential encoding.

The coarse fixed-\\(q\\) bound is a secondary concern.

The overlap with Fernando 2026 can be handled by clearly distinguishing characterization from computational complexity.

### III.7 What would change the recommendation?

**Question 16: Is unconditional bit-model FPT possible without real QE?**

Possibly, but I would not make it a prerequisite for this paper.

A direct combinatorial or algebraic algorithm could be valuable, particularly if it exploited the special pencil structure.

However, the current real-algebraic approach already provides a plausible route to bit-model FPT through Renegar.

A second algorithm avoiding real QE would be a separate strengthening.

**Question 17: Would W\\(1\\)-hardness in \\(q\\) strengthen the paper?**

Potentially, yes.

A W\\(1\\)-hardness result parameterized by \\(q\\) would help explain why the fixed-\\(q\\) algorithm has a parameter-dependent exponent.

But this would be a separate complexity result.

It is not necessary to establish the present contribution, and introducing an incomplete hardness programme would weaken the focus of the manuscript.

Reference:

---

## 12. A further issue that deserves immediate attention: the \\(r=0\\) algorithm

I want to emphasize one issue separately because it affects the validity of Theorem 3.

The manuscript says that when \\(r=0\\), the problem can be decided in polynomial time using a polynomial left-inverse test.

The mathematical criterion is correct. However, the proposed adjugate construction in Appendix B does not by itself establish polynomial running time when the matrix dimensions are unrestricted.

For a \\(q\times\omega\\) pencil, the construction explicitly involves all \\(\omega\\)-element row subsets:

\\[ \binom q\omega. \\]

This number can be exponential in \\(q\\).

The fact that the resulting left inverse has polynomial degree does not imply that it can be constructed in polynomial time by enumerating all its constituent minors.

### Recommended resolution

Investigate polynomial-matrix algorithms based on:

- Smith normal form over \\(\mathbb Q[\lambda]\\);
- polynomial-matrix unimodular completion;
- algorithms for computing polynomial bases and minimal indices;
- exact polynomial-matrix rank and divisibility tests.

The desired condition is that the maximal minors generate the unit ideal.

A polynomial-time algorithm for deciding this condition, with controlled coefficient growth, would establish the missing \\(r=0\\) branch.

The proof should explicitly account for:

1. Polynomial degrees.
2. Intermediate coefficient bit lengths.
3. The number of polynomial operations.
4. The conversion to bit operations.

The random checks reported in Appendix C are useful for detecting errors, but they do not establish this complexity bound.

**Until this branch is rigorously justified, I would regard Theorem 3 as having an outstanding proof obligation.**

This is separate from the Renegar issue: resolving the latter does not automatically resolve the former.

---

## 13. Recommended restructuring of the manuscript

The present organization is reasonable, but I think the paper can be made substantially more persuasive by making the logical dependency of the results explicit.

I suggest the following structure.

## Proposed paper architecture

**1. Introduction and contributions**

Define the decision problem, distinguish it from observer characterization, introduce the two parameters, and state the claim boundary.

---

**2. Compression and structural parametrization**

- Lemma A: compression and pencil criterion.
- Lemma B: free-row space and effective dimension.

---

**3. Algebraic certificates**

- Lemma C: rank factorization and consistency.
- Lemma D: bounded-degree Bezout certificate.
- Cauchy–Binet compression.

---

**4. Fixed-order algorithm**

State the algorithm, prove correctness, and establish the bit-complexity bound.

---

**5. Effective-dimension FPT algorithm**

Direct parametrization, spectral certificate, preprocessing, special cases, and FPT complexity.

---

**6. Existential real membership**

Give the independent polynomial-size encoding.

---

**7. Combined bounds and discussion**

Compare the parameters, discuss limitations, and identify the unrestricted complexity question.

---

**Appendices**

Detailed algebraic proofs, polynomial-matrix construction, formal verification record, and complexity accounting.

One reason for this arrangement is that the spectral certificate is used by both algorithms. It should be fully established before either algorithm invokes it.

The \\(\exists\mathbb R\\) theorem should be presented separately because it does not depend on the fixed-order chart enumeration or the effective-dimension preprocessing.

---

## 14. The most valuable additional theoretical improvements

Beyond fixing the outstanding proof obligations, I see four directions that could improve the paper.

### 14.1 Explain the relationship between the two parameters

The two algorithms are complementary, but their relationship could be developed more explicitly.

Recall

\\[ \kappa\_{\rm obs}=r d_0, \qquad k\leq d_0. \\]

Thus

\\[ k\leq\kappa\_{\rm obs} \\]

when \\(r\geq1\\).

However, \\(q\\) and \\(\kappa\_{\rm obs}\\) measure different things.

A fixed \\(q\\) does not imply bounded \\(\kappa\_{\rm obs}\\), because \\(d_0\\) can grow with the state dimension.

Conversely, bounded \\(\kappa\_{\rm obs}\\) does not imply bounded \\(q\\), because the number of fixed observer rows can be large.

This is the precise reason that both theorems are worth retaining.

I suggest including a short proposition or explanatory remark showing that neither parameterization subsumes the other.

### 14.2 Investigate a sharper fixed-order bound

The current result is

\\[ \mathcal L^{O(q^2)}. \\]

The main source of the \\(q^2\\) exponent is the number of variables in \\(X,G\\) and the spectral certificate.

There may be opportunities to reduce the variable count through:

- Eliminating redundant coordinates in \\(G\\).
- Exploiting the fixed-row structure.
- Using a smaller pencil representation.
- Avoiding unnecessary rank-stratum variables.
- Exploiting the affine dependence on the pencil parameter.

I would not delay submission to pursue this.

The current result is already meaningful. A sharper exponent is a possible later improvement.

### 14.3 Investigate whether the effective parameter can be reduced

The current parameter is

\\[ \kappa\_{\rm obs}=r d_0. \\]

It is natural but may not be minimal.

The actual free-row design problem could depend on a smaller subspace after imposing the fixed-row constraints and the spectral requirements.

For example, one could investigate whether some directions in

\\[ \mathcal T=\operatorname{row}[N\ AN] \\]

are redundant once the fixed observer rows are imposed.

A smaller parameter might be obtained by passing to an appropriate quotient space.

This could produce a stronger FPT result.

However, this is a research direction, not something the current manuscript needs to establish.

### 14.4 Investigate a direct algebraic algorithm for the spectral certificate

The current Gram–Bezout construction is elegant but relies on real-algebraic feasibility.

There may be a more specialized algorithm exploiting the pencil structure

\\[ Q(\lambda)=\lambda X-G. \\]

For example, the question of whether the pencil has full column rank at every finite complex \\(\lambda\\) can be studied through polynomial-matrix methods.

A specialized method might avoid generic real quantifier elimination.

This could eventually improve the dependence on \\(\kappa\_{\rm obs}\\), and perhaps reveal additional structural properties of the observer problem.

Again, I would treat this as future work rather than a condition for submitting the current paper.

---

## 15. Publication assessment

My assessment is that the paper has a coherent potential contribution, but the present draft is not yet submission-ready.

Here is how I would evaluate its components.

| Component                         | Assessment                  | Recommendation                           |
| --------------------------------- | --------------------------- | ---------------------------------------- |
| Compression theorem               | Strong                      | Retain and polish                        |
| Free-row parametrization          | Strong                      | Retain                                   |
| Rank factorization                | Strong                      | Expand the construction                  |
| Rank-consistency certificate      | Correct in real setting     | Make field convention explicit           |
| Bezout degree bound               | Correct                     | Retain                                   |
| Gram certificate                  | Correct in real setting     | Correct complex formulation if necessary |
| Cauchy–Binet compression          | Strong                      | Retain                                   |
| Fixed-order algorithm             | Promising                   | Complete complexity accounting           |
| Effective-dimension FPT           | Most important contribution | Resolve \\(r=0\\) branch                 |
| \\(\exists\mathbb R\\) membership | Promising                   | Rewrite Appendix B                       |
| Lean verification                 | Valuable supporting work    | Retain with precise scope                |
| Combined theorem                  | Useful                      | Separate computational models            |

### What is the likely referee response?

I would expect a technically sophisticated referee to focus on four questions.

**First:** Is the field convention consistent throughout the proof?

This is the first issue to eliminate.

**Second:** Does the effective-dimension algorithm really have a polynomial-time special case when \\(r=0\\)?

This is an important algorithmic detail, not merely an editorial concern.

**Third:** Are the real-algebraic complexity estimates justified at the bit level?

The original Renegar result provides a promising answer, but the formula construction and coefficient bounds must be fully documented.

**Fourth:** Does the \\(\exists\mathbb R\\) encoding have polynomial size?

The direct rank-factorization construction should resolve this.

The coarse fixed-order exponent is unlikely to be the most serious objection, provided it is correctly derived.

---

## 16. Final recommendations and research priorities

I would divide the remaining work into three stages.

**Stage I — Mathematical correctness** (Highest priority)

1. Fix the real-versus-complex convention.
2. Correct the false rank-preservation statement in Appendix A.1.
3. Make the Hermitian Gram identities consistent if complex observer variables are retained.
4. Correct the polynomial-matrix rank terminology in Appendix B.
5. Replace the unexplained rank-stratum construction with an explicit existential encoding.
6. Establish the polynomial-time \\(r=0\\) algorithm.

---

**Stage II — Complexity certification** (High priority)

1. Incorporate Renegar's actual bit bound.
2. Establish the coefficient bit-length estimates.
3. Complete the fixed-order chart and formula-size accounting.
4. Establish polynomial preprocessing for \\(N\\), \\(\mathcal T\\), and the kernel coefficients.
5. State the combined bounds separately in the bit and real-RAM models.
6. Define the decision language independently of the optimization problem.

---

**Stage III — Manuscript preparation** (After Stages I–II)

1. Strengthen the introduction and literature positioning.
2. Present the two parameterized algorithms as complementary.
3. Clarify the precise contribution beyond Fernando's characterization.
4. Consolidate the verification record.
5. Remove conditional language where the required theorem has been established.
6. Freeze the manuscript and prepare it for submission.

## 17. Overall conclusion

I want to distinguish two questions.

**Is the research direction correct?**

Yes. The compression, free-row parametrization, rank factorization, and polynomial-pencil certificate form a coherent approach to the computational problem.

The effective-dimension parameter is particularly promising:

\\[ \kappa\_{\rm obs} = r\operatorname{rank}[N\ AN]. \\]

It captures the total number of independent compressed directions available to the free observer rows.

The Cauchy–Binet construction then exploits the fact that the compressed pencil has only parameter-bounded column dimension.

This is the strongest conceptual contribution of the manuscript.

**Is the current paper ready to be frozen?**

No. The field convention, the \\(r=0\\) polynomial-time test, and the precise complexity encoding must be settled first.

The Renegar issue is more encouraging than the status report suggests: the original bit-complexity result supports the desired unconditional FPT conclusion, subject to verifying the coefficient-size hypotheses.

I would not return to unrestricted hardness at this stage. There is enough material here for a focused algorithmic paper, and completing the existing upper-bound programme is a more valuable immediate objective.

My final recommendation is:

\\[ \boxed{ \begin{gathered} \text{Retain both parameterized algorithms.}\\\ \text{Strengthen the bit-model FPT theorem.}\\\ \text{Repair the polynomial-matrix and field-level arguments.}\\\ \text{Complete the }r=0\text{ complexity proof.}\\\ \text{Then freeze the algorithmic manuscript.} \end{gathered} } \\]

The paper should make a deliberately limited but rigorous claim: it establishes two complementary tractability results and an existential-real upper bound for minimum-order functional observer decision. It does not solve the unrestricted complexity classification.

That is a defensible and worthwhile mathematical contribution. The priority now should be to make every theorem in that claim boundary completely airtight, rather than expanding the paper with additional speculative results.

---

**One particularly useful next piece of work** would be a focused proof audit of the \\(r=0\\) branch and Appendix B together. They share the polynomial-matrix left-inverse construction, but require different complexity arguments: polynomial-size existential encoding in one case and an efficient exact decision algorithm in the other. Separating those two obligations will make it much easier to determine exactly what remains before submission.