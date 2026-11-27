# **Research assessment of&#x20;**`104_what_a_reduction_requires.md`

## **Overall assessment**

This report makes an important conceptual advance over the earlier gadget-based discussion. Its central correction is right:

**The failure to impose additional polynomial relations on the free-row witnesses does not imply that reductions are impossible.** The decision problem is an existential feasibility problem in which the input data determine the constraints and the free rows provide witnesses. A reduction need not force arbitrary algebraic relations among the witness coordinates if the architecture can encode the source problem's satisfiability condition through the geometry of the instance data and the admissible witness spaces.

I agree with the report's decision to withdraw the earlier impossibility claim. The reformulation in §II.3 is the right general target: characterize the set of coefficient data for which at least one admissible free-row matrix exists.&#x20;

104_what_a_reduction_requires(2).md



However, I would sharpen the report in four ways.

1. **The six primitives should be interpreted as tests on the instance data, not as a collection of existential-variable gadgets.** In particular, the Booleanity gate does not yet provide Boolean witness variables for a reduction from 0–1 feasibility.
2. **Fibrewise rigidity must not be confused with global witness rigidity.** It says that feasibility cannot impose a new polynomial relation inside a fixed active fibre. It does not say that all fibres are active, nor that the choice of fibre is unconstrained.
3. **The correct geometric object is not just the set of feasible free rows.** It is the family of subspaces \\(W\\) that can occur as the common row space of \\(H\\) and \\(H_A\\), together with a generic spectral condition on the linear space of free-row choices compatible with \\(W\\).
4. **The decisive next step should be a geometric characterization of active&#x20;**\\(W\\)**-spaces, followed by a complexity analysis of that characterization.** This is more focused than attempting further isolated multiplication or Boolean gates.

My assessment of the five questions is:

| Question                                                         | Assessment                                                                                                                                                              |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Q1: Is the coefficient-condition reformulation the right target? | Yes. It is the right formulation, but it needs a fixed field, input encoding, and dimension regime.                                                                     |
| Q2: Is there a structural upper bound?                           | Yes: a constructible/semialgebraic description with dimension-dependent degree bounds. This is not, by itself, a complexity obstruction.                                |
| Q3: Which source problem should be targeted?                     | Existential real feasibility is the natural broad target; Boolean linear feasibility is a more focused NP-hard target. Neither is reduced yet.                          |
| Q4: Can input-data Booleanity replace witness Booleanity?        | Not in an ordinary many-one reduction. It tests the supplied input; it does not existentially choose Boolean variables.                                                 |
| Q5: What is the decisive next result?                            | A Grassmannian-level characterization of active row spaces and a polynomial-time computable generic-pencil criterion, or a hardness reduction to that characterization. |

I will first verify the mathematical foundation, then address the reduction framework and each question.

# **Part I. What the six primitives actually establish**

## **1. The kernel lemma and fibrewise rigidity**

The report starts from

\\[ K_0=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \qquad H=LN,\qquad H_A=LAN, \\]

and the compressed feasibility conditions

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H, \tag{5a} \\]

\\[ \operatorname{rank}(\lambda H-H_A)=\omega \quad\forall\lambda\in\mathbb C, \qquad \omega=\operatorname{rank}H. \tag{5b} \\]

The kernel lemma is correct. Taking \\(\lambda=0\\) gives

\\[ \operatorname{rank}H_A=\operatorname{rank}H=\omega. \\]

Since the row space of \\(H_A\\) is contained in that of \\(H\\), equality follows:

\\[ \operatorname{row}H_A=\operatorname{row}H. \\]

Consequently,

\\[ \boxed{\ker H=\ker H_A.} \\]

The report correctly records the stronger consequence:

\\[ \operatorname{rank}H\_{[:,J]} = \operatorname{rank}(H_A)\_{[:,J]} \quad\text{for every }J\subseteq\\{1,\ldots,k\\}. \\]

This is not merely a statement about corresponding zero columns. It says that every linear dependence among the compressed columns of \\(H\\) is also a dependence among the corresponding columns of \\(H_A\\), and conversely.&#x20;

104_what_a_reduction_requires(2).md



### **1.1 The precise meaning of fibrewise rigidity**

Fix an \\(\omega\\)-dimensional subspace \\(W\\) of the compressed row-coordinate space. The fibre is

\\[ M_W=\\{R:\text{every row of }H(R)\text{ and }H_A(R)\text{ belongs to }W\\}. \\]

On this fibre, if

\\[ \operatorname{rank}H(R)=\omega, \\]

then automatically

\\[ \operatorname{row}H(R)=W. \\]

Since every row of \\(H_A(R)\\) belongs to \\(W\\), condition (5a) follows.

The exact-rank condition is open in \\(M_W\\). On the constant-rank part, the spectral condition is also open: after homogenizing the pencil and considering its rank-drop incidence over \\(\mathbb P^1\\), the bad locus is closed under projection because \\(\mathbb P^1\\) is proper. Therefore, if the feasible part of \\(M_W\\) is nonempty, it is a nonempty Zariski-open subset of the linear space \\(M_W\\), and hence Zariski dense.

The report's conclusion is therefore valid:

\\[ \boxed{ \text{Every polynomial identity holding on all feasible points of an active fibre holds on the whole fibre.} } \\]

But there is an important logical qualification.

### **1.2 What fibrewise rigidity does not imply**

It does not imply that the union of active fibres is unrestricted.

Let

\\[ \mathcal W\_{\mathrm{act}} = \\{W:\dim W=\omega,\ M_W\cap\mathcal F\_\omega\ne\varnothing\\}. \\]

The feasible set is contained in the union of the active fibres:

\\[ \mathcal F\_\omega \subseteq \bigcup\_{W\in\mathcal W\_{\mathrm{act}}}M_W. \\]

Under the fibrewise density statement, its Zariski closure is

\\[ \boxed{ \overline{\mathcal F\_\omega}^{\\,\mathrm{Zar}} = \overline{\bigcup\_{W\in\mathcal W\_{\mathrm{act}}}M_W}^{\\,\mathrm{Zar}}. } \\]

The family \\(\mathcal W\_{\mathrm{act}}\\) can itself be highly constrained. The geometry of that family can encode algebraic information even though feasibility is dense inside each active fibre.

This is the central point I would emphasize in the revised report:

> The architecture may be unable to impose additional polynomial constraints inside a fixed active fibre, while still imposing strong constraints on which fibres are active.

That distinction is the mathematical basis for the new research direction.

## **2. The six primitives: what they prove and what they do not**

The report lists six proved primitives, all acting on instance data. I agree that these are meaningful results, but their role in a reduction needs to be stated precisely.&#x20;

104_what_a_reduction_requires(2).md



### **2.1 Literal gate**

The literal gate has

\\[ H=\begin{pmatrix}1\\\u\end{pmatrix}, \qquad H_A=\begin{pmatrix}0\\\tv\end{pmatrix}. \\]

Since \\(H\\) has rank one, feasibility requires \\(H_A\\) to have rank one as well. Thus \\(tv\ne0\\) is necessary.

Conversely, if \\(t\ne0\\), choose \\(v\ne0\\). The pencil is

\\[ \lambda H-H_A = \begin{pmatrix} \lambda\\\ \lambda u-tv \end{pmatrix}. \\]

At \\(\lambda=0\\), its second entry is nonzero; at \\(\lambda\ne0\\), its first entry is nonzero. Hence it has rank one for every complex \\(\lambda\\).

Therefore

\\[ \boxed{\text{feasible}\iff t\ne0.} \\]

This is a sound nonzero test on an input coefficient.

### **2.2 Negation**

Feeding \\(1-x\\) into the literal gate tests \\(1-x\ne0\\). If \\(x\in\\{0,1\\}\\), this is equivalent to \\(x=0\\).

The qualification is essential:

\\[ 1-x\ne0 \quad\not\Longleftrightarrow\quad \neg(x\ne0) \\]

for arbitrary field values.

This is a conditional Boolean negation construction, not a general logical negation gate.

### **2.3 Arbitrary-**\\(k\\)**&#x20;conjunction**

The arbitrary-\\(k\\) construction is especially valuable because it is explicit and dimension-independent in the number of blocks.

For \\(t_i\ne0\\), the report chooses

\\[ H= \begin{bmatrix} \mathbf 1^{\mathsf T}\\\ I_k \end{bmatrix}, \qquad H_A= \begin{bmatrix} 0\\\ D \end{bmatrix}, \\]

where \\(D=\operatorname{diag}(d_1,\ldots,d_k)\\), with distinct nonzero \\(d_i\\).

The pencil is

\\[ P(\lambda)= \begin{bmatrix} \lambda\mathbf 1^{\mathsf T}\\\ \lambda I_k-D \end{bmatrix}. \\]

If \\(\lambda\notin\\{d_1,\ldots,d_k\\}\\), the lower block is invertible. If \\(\lambda=d_j\\), the lower block has kernel \\(\operatorname{span}\\{e_j\\}\\), and the top row evaluates to \\(d_j\ne0\\) on \\(e_j\\). Thus \\(P(\lambda)\\) has full column rank for all \\(\lambda\\).

For soundness, if \\(t_i=0\\), the \\(i\\)-th column of \\(H_A\\) vanishes while the anchored \\(i\\)-th column of \\(H\\) does not. This contradicts

\\[ \ker H=\ker H_A. \\]

Hence

\\[ \boxed{\text{feasible}\iff \prod\_{i=1}^k t_i\ne0.} \\]

This is a genuine conjunction of nonzero tests.

### **2.4 Equation gate**

The corrected matrix in the report is important:

\\[ H= \begin{pmatrix} t&0\\\ u_1&u_2 \end{pmatrix}, \qquad H_A= \begin{pmatrix} 1&1\\\ w&w \end{pmatrix}. \\]

The repeated entry \\(w,w\\) is forced by the underlying block construction; it should not be replaced by two independent free parameters.

Since \\(\dim(AK_0)=1\\), feasibility has \\(\omega=1\\). The row space of \\(H_A\\) is

\\[ \operatorname{row}H_A=\operatorname{span}\\{(1,1)\\}. \\]

Feasibility requires

\\[ \operatorname{row}H=\operatorname{span}\\{(1,1)\\}. \\]

The fixed row \\((t,0)\\) must therefore lie in this space, which happens if and only if \\(t=0\\).

Conversely, if \\(t=0\\), choose \\(u_1=u_2=u\ne0\\). Then

\\[ \lambda H-H_A = \begin{pmatrix} -1&-1\\\ \lambda u-w&\lambda u-w \end{pmatrix} \\]

has rank one for every \\(\lambda\\).

Thus the equation gate is sound:

\\[ \boxed{\text{feasible}\iff t=0.} \\]

### **2.5 Booleanity gate**

The Booleanity gate is a significant addition. Its fixed rows yield the necessary determinant condition

\\[ \det \begin{pmatrix} a_1&a_2\\\ t_1b_1&t_2b_2 \end{pmatrix}=0. \\]

The report chooses

\\[ a=(x,0),\qquad b=(1,1),\qquad t=(1,x-1), \\]

giving

\\[ \det \begin{pmatrix} x&0\\\ 1&x-1 \end{pmatrix} =x(x-1). \\]

Therefore feasibility requires

\\[ x(x-1)=0. \\]

The square-pencil obstruction excludes layer two, while the fixed-row condition excludes layer zero. At \\(x=0\\) and \\(x=1\\), the layer-one construction can be completed by suitable free rows.

For clarity, explicit choices can be given. With

\\[ H= \begin{pmatrix} x&0\\\ u_1&u_2 \end{pmatrix}, \qquad H_A= \begin{pmatrix} 1&x-1\\\ v_1&(x-1)v_2 \end{pmatrix}, \\]

take:

- If \\(x=0\\), choose \\((u_1,u_2)=(1,-1)\\) and \\((v_1,v_2)=(0,0)\\). Then both rows of the pencil lie in \\(\operatorname{span}\\{(1,-1)\\}\\), and its first row is nonzero.
- If \\(x=1\\), choose \\((u_1,u_2)=(1,0)\\) and \\((v_1,v_2)=(0,0)\\). The two pencil rows are \\((\lambda-1,0)\\) and \\((\lambda,0)\\), which are never simultaneously zero.

Thus the claimed equivalence is supported:

\\[ \boxed{\text{feasible}\iff x\in\\{0,1\\}.} \\]

But this result must be interpreted correctly:

**It makes an input coefficient Boolean. It does not yet create an existential Boolean variable.**

That distinction is decisive for Q4.

### **2.6 Conjunction of equations**

The two-fixed-row construction gives a simultaneous condition:

\\[ x=0,\qquad y=0. \\]

The reason is that the fixed rows of \\(H\\) are

\\[ (x,0),\qquad(y,0), \\]

while the fixed rows of \\(H_A\\) are both \\((1,1)\\). Since the row space of \\(H_A\\) must equal that of \\(H\\), both fixed \\(H\\)-rows must belong to \\(\operatorname{span}\\{(1,1)\\}\\). This forces

\\[ x=y=0. \\]

This is a valid conjunction-of-equations primitive.

### **2.7 The correct interpretation of the primitive library**

The six results establish that the coefficient dependence of the feasibility problem can express certain elementary algebraic conditions:

\\[ t\ne0,\qquad t=0,\qquad x(x-1)=0, \\]

and finite conjunctions of such conditions.

They do **not** yet establish that the feasibility problem can represent arbitrary polynomial systems in existential variables.

The distinction is:

| Established                                              | Not yet established                                       |
| -------------------------------------------------------- | --------------------------------------------------------- |
| Testing whether supplied data coefficients vanish        | Choosing an unknown coefficient as a witness              |
| Testing whether supplied data coefficients are Boolean   | Encoding a Boolean assignment in \\(R\\) or \\(W\\)       |
| Conjoining fixed-parameter equations                     | Multiplication of existential variables                   |
| Making feasibility depend on a fixed algebraic condition | Representing arbitrary existential polynomial feasibility |

The primitives are useful, but the reduction programme needs a bridge from input-coefficient tests to existentially quantified variables.

# **Part II. Q1 — Is the coefficient-condition reformulation the right target?**

## **3. Yes, but it should be made into a precise decision language**

The report's reformulation is conceptually correct:

\\[ \exists x:\operatorname{System}(x)=0 \quad\Longleftrightarrow\quad \exists R:\ (5a)\wedge(5b). \\]

The source instance supplies coefficients; the free rows provide the existential witness. The real object to characterize is therefore

\\[ \mathcal S = \\{(A,C,L_0):\exists R,\ (5a),(5b)\\}. \\]

This is the right target, but the notation suppresses several choices that affect the mathematical and complexity-theoretic problem.

### **3.1 Fix the dimensions**

A complexity problem needs a specified family of inputs. One should decide whether \\(n,p,r_0,m\\) are:

- fixed constants;
- part of the input;
- bounded by a polynomial in the source input size.

These alternatives can lead to very different expressive power.

For example, if all dimensions are fixed, the number of matrix entries is fixed, so the target problem is not even an ordinary growing input family unless the coefficient bit lengths are allowed to grow. If dimensions vary, the number of algebraic variables and the degrees of the relevant determinantal conditions can grow with the input.

For a hardness reduction, the natural setting is that the dimensions are part of the output of the reduction and are polynomially bounded in the source input length.

### **3.2 Specify the witness field**

The report uses rational input matrices, but it does not state explicitly whether the free rows \\(R\\) must be rational, real, or complex. This must be fixed.

There are three materially different languages:

\\[ \begin{aligned} \mathcal S\_{\mathbb Q} &=\\{(A,C,L_0):\exists R\in\mathbb Q^{m\times n},\ \mathrm{Feas}\\},\\\ \mathcal S\_{\mathbb R} &=\\{(A,C,L_0):\exists R\in\mathbb R^{m\times n},\ \mathrm{Feas}\\},\\\ \mathcal S\_{\mathbb C} &=\\{(A,C,L_0):\exists R\in\mathbb C^{m\times n},\ \mathrm{Feas}\\}. \end{aligned} \\]

These are not interchangeable.

- For \\(\mathbb C\\)-valued witnesses, algebraic geometry and constructible sets are the natural language.
- For \\(\mathbb R\\)-valued witnesses, real algebraic geometry and semialgebraic sets are the natural language.
- For \\(\mathbb Q\\)-valued witnesses, rational-point existence is a different problem; it is not captured simply by real quantifier elimination or by constructibility over \\(\mathbb C\\).

For the usual real functional-observer interpretation, I would formulate the primary decision problem with \\(R\in\mathbb R^{m\times n}\\), while retaining the complex spectral parameter \\(\lambda\in\mathbb C\\).

This distinction also matters when using the word “open.” A complex Zariski-open subset and its real points behave well when the relevant linear space is defined over \\(\mathbb R\\), but existence of a complex witness does not automatically imply existence of a real witness.

### **3.3 A more precise target definition**

For fixed dimensions and a specified witness field \\(\mathbb F\\), define

\\[ \mathsf{FO}\_{n,p,r_0,m}(\mathbb F) = \left\\{ (A,C,L_0): \exists R\in\mathbb F^{m\times n} \text{ such that }[L_0;R]\text{ is feasible} \right\\}. \\]

A polynomial-time many-one reduction from a source language \\(\mathcal L\\) must construct, from each source input \\(z\\), rational matrices

\\[ (A_z,C_z,L\_{0,z}) \\]

of polynomial encoding size such that

\\[ \boxed{ z\in\mathcal L \iff (A_z,C_z,L\_{0,z}) \in\mathsf{FO}\_{n_z,p_z,r\_{0,z},m_z}(\mathbb F). } \\]

This formulation makes the roles unambiguous:

- \\(z\\) is the source input;
- its coefficients are encoded in \\(A_z,C_z,L\_{0,z}\\);
- the existential source assignment must be represented by the target witness \\(R\\), or by an equivalent existential geometric object;
- the output dimensions and bit lengths must be polynomially bounded.

The report's §II.3 is therefore the right conceptual pivot, but this formal decision-language definition should be added.&#x20;

104_what_a_reduction_requires(2).md



## **4. A stronger geometric reformulation: the active-subspace problem**

I think the report can go beyond the abstract coefficient-condition formulation. There is a natural intermediate characterization that isolates exactly where the existential freedom resides.

Let \\(\mathbb F\\) be the field over which the row spaces and free rows are chosen. For fixed \\(A,C\\), define the linear map

\\[ \Phi:\mathbb F^{1\times n} \longrightarrow \mathbb F^{1\times k}\oplus\mathbb F^{1\times k} \\]

by

\\[ \Phi(r)=(rN,rAN). \\]

Let

\\[ \mathcal S\_{A,C}=\operatorname{im}\Phi. \\]

This is a linear subspace of the compressed pair space.

For an \\(\omega\\)-dimensional subspace

\\[ W\subseteq\mathbb F^{1\times k}, \\]

define the admissible pair space

\\[ \mathcal T_W = \mathcal S\_{A,C}\cap(W\oplus W). \\]

A free row \\(r\\) belongs to the fibre \\(M_W\\) precisely when

\\[ \Phi(r)\in\mathcal T_W. \\]

The fixed rows \\(L_0\\) give fixed compressed pairs

\\[ (h_i^0,g_i^0) = \big((L_0)\_iN,(L_0)\_iAN\big). \\]

For \\(W\\) to be compatible, every such pair must belong to \\(W\oplus W\\).

Now let

\\[ \pi_1:\mathcal T_W\to W,\qquad \pi_2:\mathcal T_W\to W \\]

be the two coordinate projections.

The first projection determines whether the free rows can help \\(H\\) attain rank \\(\omega\\). In particular, a necessary and sufficient condition for the existence of choices of \\(m\\) free rows with

\\[ \operatorname{rank}H=\omega \\]

is

\\[ \boxed{ \operatorname{span}\left( \\{h_i^0\\}\_{i=1}^{r_0}\cup\pi_1(\mathcal T_W) \right)=W, } \\]

provided the number of free rows is sufficient to supply the missing dimensions.

More precisely, if the fixed \\(H\\)-rows span a subspace of dimension \\(d_0\\), then at least \\(\omega-d_0\\) free rows are needed. When \\(m\ge\omega-d_0\\), the displayed spanning condition is sufficient: choose free rows whose first projections complete a basis of \\(W\\).

The remaining question is spectral feasibility.

### **4.1 The spectral condition is generic within a fixed fibre**

Suppose the rank-completion condition above holds. The admissible free-row choices form an affine or linear parameter space, and the condition

\\[ \operatorname{rank}H=\omega \\]

defines a nonempty Zariski-open subset.

Within this exact-rank subset, spectral feasibility is also open. Since the parameter space is irreducible, the following equivalence holds over an algebraically closed field:

\\[ \boxed{ \begin{aligned} &\text{There exists a feasible free-row choice in }M_W\\\ &\qquad\Longleftrightarrow\\\ &\text{a generic admissible free-row choice in }M_W \text{ is feasible.} \end{aligned} } \\]

The point is not that every free-row choice is feasible. It is that, once one feasible point exists, the feasible points form a dense open subset of that fibre.

Thus the existential quantifier over \\(R\\), for a fixed \\(W\\), can be replaced by a generic-pencil test.

### **4.2 A candidate active-subspace criterion**

This suggests the following formulation.

For each candidate \\(W\\), form the generic pencil obtained by choosing generic admissible free-row pairs from \\(\mathcal T_W\\), together with the fixed compressed rows. Then test:

1. compatibility of the fixed rows with \\(W\\);
2. whether the first-coordinate projections can complete \\(H\\) to rank \\(\omega\\);
3. whether the generic pencil has rank \\(\omega\\) for every \\(\lambda\in\mathbb C\\).

The original feasibility problem becomes:

\\[ \boxed{ \exists\\,W\in\operatorname{Gr}(\omega,k) \text{ satisfying the compatibility, rank-completion, and generic spectral tests.} } \\]

This is a much more informative reformulation than simply writing \\(\exists R\\).

It separates the problem into:

- an existential choice of a subspace \\(W\\);
- linear-algebraic conditions on the admissible pair space \\(\mathcal T_W\\);
- a generic algebraic condition on a matrix pencil.

This is where I would direct the next mathematical effort. It makes the witness-side rigidity useful rather than treating it as a dead end.

# **Part III. Q2 — What upper bound exists on the data-side expressive power?**

## **5. Constructibility is a valid upper bound, but not a hardness obstruction**

The report asks whether the feasibility condition is always a constructible set, perhaps described by minors of bounded degree in the input data.

The answer is broadly yes, after fixing dimensions and working over an algebraically closed field, with an important qualification about the choice of witness field.

### **5.1 The spectral condition has a finite algebraic certificate**

On a constant-rank stratum, let

\\[ P(\lambda)=\lambda H-H_A. \\]

Because of (5a), the rank of \\(P(\lambda)\\) is at most \\(\omega\\). The requirement that its rank equal \\(\omega\\) for every \\(\lambda\in\mathbb C\\) is equivalent to saying that its \\(\omega\times\omega\\) minors have no common complex root.

Let these maximal minors be

\\[ m_1(\lambda),\ldots,m_s(\lambda). \\]

Then

\\[ \boxed{ \operatorname{rank}P(\lambda)=\omega\ \forall\lambda\in\mathbb C \iff \gcd(m_1,\ldots,m_s)=1. } \\]

For univariate polynomials, this condition has a finite Bézout certificate:

\\[ q_1(\lambda)m_1(\lambda)+\cdots+ q_s(\lambda)m_s(\lambda)=1 \\]

for suitable polynomial coefficients \\(q_i\\), with a degree bound depending on the number and degrees of the minors.

This converts the universal quantifier over \\(\lambda\\) into finitely many algebraic equations in the coefficients of the \\(q_i\\) and the matrix entries.

The report is right to treat the spectral condition as a finite algebraic condition rather than as an irreducible universal quantifier. This is also consistent with the certificate framework developed in Paper I.

### **5.2 What happens to the dependence on&#x20;**\\(N\\)**?**

There is a technical point that should be included if the report wants a statement about polynomial degree in the raw input data.

The matrix \\(N\\), a basis of

\\[ \ker\begin{bmatrix}C\\\CA\end{bmatrix}, \\]

is not itself a polynomial function of \\(A,C\\). It is defined by solving a linear system and choosing a basis.

A clean algebraic treatment is to stratify the input space according to the rank of

\\[ B=\begin{bmatrix}C\\\CA\end{bmatrix}. \\]

On each rank stratum, choose a nonzero pivot minor and use it to construct a rational coordinate chart for the kernel. The entries of \\(N\\) are then rational functions of the entries of \\(A,C\\), with denominators given by the selected pivot minor.

After clearing denominators, all the compressed rank conditions and the coefficients of the pencil minors become polynomial conditions on that chart.

There are finitely many possible pivot charts. Consequently, for fixed matrix dimensions, the full feasibility relation can be expressed by a finite union of algebraic or constructible conditions.

This gives a meaningful upper bound:

> For fixed dimensions, the feasibility relation is a constructible condition on the input and witness variables over an algebraically closed field. Its defining equations and inequations have degree bounded in terms of the dimensions.

For real witnesses, the corresponding existential relation is semialgebraic, because the finite polynomial conditions can be expressed over the reals and projected using real quantifier elimination.

### **5.3 Why this does not rule out NP-hardness or ETR-hardness**

The key distinction is between **algebraic definability** and **computational complexity**.

Constructibility does not mean that membership can be decided in polynomial time. Nor does a degree bound depending on the dimensions imply that the resulting decision problem is easy.

For example, Boolean satisfiability can be represented by polynomial equations:

\\[ x_i(1-x_i)=0 \\]

for each Boolean variable, together with polynomial equations encoding the clauses. The existence of a complex solution to this system is equivalent to the existence of a Boolean satisfying assignment, because the Booleanity equations force every \\(x_i\\) to be either zero or one.

Thus an existential algebraic feasibility problem can encode an NP-complete problem, despite being a projection of an algebraic set.

Likewise, existential real feasibility is a natural semialgebraic decision problem and is computationally hard.

So the following inference is invalid:

\\[ \text{constructible or semialgebraic} \quad\Longrightarrow\quad \text{not NP-hard}. \\]

A structural upper bound becomes a genuine complexity obstruction only if it is strengthened into something algorithmic, such as:

- a polynomial-time membership algorithm;
- a polynomial-time reduction to a known tractable algebraic problem;
- a fixed-parameter algorithm with a parameter bounded independently of the source input;
- a strong restriction on the dimension, degree, or form of the defining equations that is known to make the problem tractable.

The report should therefore present constructibility as a structural classification target, not as evidence against hardness.

## **6. A more useful form of the upper bound: bounded algebraic complexity**

I would formulate the result at two levels.

**Geometric level.** For fixed dimensions, the feasible-data set is constructible over an algebraically closed field, and semialgebraic for real witnesses.

**Quantitative level.** On each kernel-coordinate chart, the feasibility relation admits a finite polynomial description whose number of variables and degrees are bounded in terms of \\(n,p,r_0,m\\).

The quantitative statement is more valuable for complexity work. It allows one to ask whether the family of polynomial conditions generated by this architecture is expressive enough to represent a known hard family.

However, one must not claim that the degree bound is an absolute constant independent of the matrix dimensions. The number of maximal minors, their degrees, and the Bézout-certificate bounds all depend on the dimensions. In a reduction, those dimensions can grow with the source input.

# **Part IV. Q3 — Which source problem should be targeted?**

## **7. The most natural broad target is existential real feasibility**

The report's earlier programme aimed at existential polynomial feasibility. I would not abandon that target, but I would distinguish two versions.

### **7.1 Existential polynomial feasibility over the reals**

A typical instance is

\\[ \exists x_1,\ldots,x_s\in\mathbb R: \quad f_1(x)=0,\ldots,f\_\ell(x)=0, \\]

possibly with inequalities as well.

This is the natural target if the observer's free rows are real-valued. It matches the basic logical form

\\[ \exists R:\operatorname{Feas}(A,C,L_0,R). \\]

It also provides a direct test of the architecture's expressive power: can the dependence of the compressed feasibility condition on \\(R\\) and the data simulate general polynomial constraints?

But the report has correctly identified the obstacle: the existing primitives mostly test the supplied coefficients. They do not yet demonstrate how to represent arbitrary multiplication of existential variables.

The key missing theorem is not merely another scalar gate. It is a representation theorem of the form:

> Given a polynomial system \\(f_1(x)=\cdots=f\_\ell(x)=0\\), construct in polynomial time matrices \\((A,C,L_0)\\) such that a feasible observer exists if and only if the polynomial system has a real solution.

That theorem would immediately establish hardness for the corresponding existential-real problem, subject to the precise witness-field convention and encoding.

### **7.2 Existential polynomial feasibility over the complex numbers**

If the free rows are allowed to be complex, the analogous target is

\\[ \exists x\in\mathbb C^s: \quad f_1(x)=\cdots=f\_\ell(x)=0. \\]

This is a natural algebraic-geometric source problem. It aligns especially well with the constructible-set formulation and the Bézout certificates for the spectral condition.

However, this is not automatically the same as the real observer problem. A reduction that produces complex feasible rows when the source system has a complex solution may fail to produce real feasible rows.

The report should therefore not use the phrase “existential polynomial feasibility” without specifying the field.

## **8. A more focused NP-hard target: 0–1 linear feasibility**

A second candidate is

\\[ Bx=b,\qquad x\in\\{0,1\\}^s, \\]

where \\(B,b\\) are integer data.

This problem is NP-hard. It is attractive because it requires only:

- Booleanity constraints \\(x_i(1-x_i)=0\\);
- linear equations \\(Bx=b\\).

It avoids the need to encode arbitrary multiplication of witness variables.

But the current Booleanity gate does not yet solve this problem.

The gate proves that if the input coefficient \\(x\\) is supplied, feasibility can test whether

\\[ x\in\\{0,1\\}. \\]

In 0–1 linear feasibility, by contrast, \\(x\\) is an unknown assignment. The reduction receives \\(B,b\\), not the solution \\(x\\). It must arrange for the target witness to encode the unknown assignment.

Thus the missing construction is one of the following:

1. a Booleanity constraint on coordinates of the active subspace \\(W\\);
2. a way to represent an unknown Boolean vector by the choice of \\(W\\);
3. a direct construction in which the free-row witness \\(R\\) encodes Boolean values, with the equations \\(Bx=b\\) enforced by the active-subspace condition.

This is why the 0–1 feasibility route is promising but not yet established.

## **9. An intermediate target may be better than either full ETR or 0–1 feasibility**

I would also investigate problems whose existential variables are naturally subspaces or matrices, rather than scalar polynomial variables.

The observer problem already has a natural existential geometric object:

\\[ W=\operatorname{row}H=\operatorname{row}H_A. \\]

Potential source families include:

- constrained subspace selection;
- rank-constrained matrix completion;
- existence of a subspace satisfying prescribed linear incidence conditions;
- simultaneous invariant-subspace or matrix-pencil conditions;
- algebraic feasibility problems formulated directly on Grassmannians.

I am not asserting that any one of these is automatically hard under the exact restrictions of this model. The point is methodological: the target problem's witness is naturally a subspace together with a generic pencil, so a source problem with the same witness structure may be much easier to encode than a scalar polynomial system.

A particularly useful intermediate question is:

> What is the complexity of deciding whether there exists an \\(\omega\\)-dimensional subspace \\(W\\) satisfying the fixed-row compatibility, rank-completion, and generic-pencil conditions derived in Part II?

If this subspace-selection problem is already hard, then the observer problem may inherit that hardness. If it is tractable, it may provide an algorithmic route for the original problem.

# **Part V. Q4 — Can Booleanity of input data replace existential Boolean variables?**

## **10. Not in an ordinary many-one reduction**

The report asks whether a variable of a 0–1 feasibility problem can range over instance data rather than witnesses, perhaps by quantifying over a family of instances.

I think this question reveals an important distinction that should be made explicit.

In a standard many-one reduction, the reduction receives a source input \\(z\\) and produces one target input \\(I(z)\\). It cannot choose an unknown satisfying assignment and place it into the target input, because doing so would already solve the source problem.

For 0–1 feasibility, the source input is

\\[ (B,b). \\]

The unknown Boolean vector \\(x\\) is not part of the input. The reduction must construct target data from \\(B,b\\) such that the target witness represents a possible \\(x\\).

A Booleanity gate acting on an entry of \\(L_0\\) only checks whether that entry, already supplied by the reduction, is zero or one. It does not choose that entry existentially.

This gives a simple but important conclusion:

\\[ \boxed{ \text{A test that input coefficients are Boolean is not a Boolean witness-variable gadget.} } \\]

If the reduction itself chooses the coefficients \\(x_i\\), it must choose them without knowing whether the source instance is satisfiable. Otherwise the reduction is circular.

## **11. Why quantifying over a family of instances changes the target problem**

Suppose one tries to replace the fixed output \\(I(z)\\) by a family

\\[ \\{I(z,x):x\in\\{0,1\\}^s\\} \\]

and then asks whether at least one member of the family is feasible.

The resulting statement is

\\[ \exists x\in\\{0,1\\}^s: \quad I(z,x)\in\mathsf{FO}. \\]

This may be a perfectly meaningful new decision problem, but it is not the original observer-feasibility language on a single input. The existential choice \\(x\\) has simply been moved into the definition of the target problem.

It can be useful if the family itself is represented succinctly and its existential choice is part of the target problem's formal input. But then the complexity of that new problem must be analyzed independently. One cannot use it to establish hardness of the original fixed-instance feasibility problem without an additional construction that compiles the family into one instance.

## **12. The correct route: make the existential choice a subspace choice**

The more promising approach is to encode the Boolean assignment in the choice of \\(W\\), not in the supplied coefficients.

For example, suppose a suitable coordinate chart on the Grassmannian represents a candidate subspace by parameters

\\[ z_1,\ldots,z_s. \\]

One could aim to construct the instance so that active subspaces exist precisely when

\\[ z_i(1-z_i)=0,\qquad i=1,\ldots,s, \\]

and

\\[ Bz=b. \\]

The important difference from the existing Booleanity gate is that now the \\(z_i\\) are coordinates of the existential geometric witness \\(W\\), rather than entries of the input matrices.

This is a genuine reduction strategy. But it requires proving that the observer's active-subspace conditions can impose the Booleanity equations on the Grassmannian coordinates.

There is no contradiction with fibrewise rigidity. The rigidity theorem concerns polynomial relations among free rows inside a fixed fibre \\(M_W\\). It does not prevent the set of admissible subspaces \\(W\\) from being restricted by equations.

That is precisely where the next construction should focus.

# **Part VI. Q5 — What is the decisive next computation or theorem?**

## **13. The decisive next result should characterize active subspaces**

I would prioritize the following theorem over further ad hoc gate searches.

### **Proposed theorem: active-subspace characterization**

Fix \\(A,C,L_0\\), a compressed rank \\(\omega\\), and a field \\(\mathbb F\\). Define

\\[ \Phi(r)=(rN,rAN), \qquad \mathcal S\_{A,C}=\operatorname{im}\Phi. \\]

For a candidate \\(\omega\\)-dimensional subspace \\(W\subseteq\mathbb F^{1\times k}\\), define

\\[ \mathcal T_W=\mathcal S\_{A,C}\cap(W\oplus W). \\]

Then characterize exactly when there exists a feasible \\(R\\) with

\\[ \operatorname{row}H=\operatorname{row}H_A=W. \\]

The characterization should have three components:

**(i) Fixed-row compatibility**

\\[ (h_i^0,g_i^0)\in W\oplus W \quad\text{for every fixed row }i. \\]

**(ii) Rank completion**

\\[ \operatorname{span}\left( \\{h_i^0\\}\_{i=1}^{r_0}\cup\pi_1(\mathcal T_W) \right)=W, \\]

with enough free rows to complete the rank.

**(iii) Generic spectral feasibility**

Choose generic admissible free-row pairs from \\(\mathcal T_W\\), append the fixed compressed rows, and test whether the resulting pencil has rank \\(\omega\\) for every complex \\(\lambda\\).

The key assertion to prove is that, once the rank-completion condition is satisfied, existence of one spectrally feasible choice is equivalent to generic spectral feasibility in the fibre.

This should follow from the fibrewise rigidity/open-density argument, but the exact parameterization of the generic pencil must be handled carefully.

## **14. The decisive computation: a generic gcd test**

For a fixed \\(W\\), choose coordinates on \\(\mathcal T_W\\). Let

\\[ z_1,\ldots,z_d \\]

be independent parameters for the admissible free-row choices.

Construct the generic pencil

\\[ P_W(\lambda,z)=\lambda H_W(z)-H\_{A,W}(z). \\]

Let

\\[ m_1(\lambda,z),\ldots,m_s(\lambda,z) \\]

be its \\(\omega\times\omega\\) minors. The generic spectral condition is

\\[ \boxed{ \gcd\_{\overline{\mathbb F(z)}[\lambda]} \big(m_1(\lambda,z),\ldots,m_s(\lambda,z)\big)=1. } \\]

This is a finite symbolic computation over the rational function field in the parameters \\(z\\). It can be checked using subresultants, polynomial remainder sequences, or a suitable Bézout certificate.

This gives a concrete algorithmic question:

> Given a candidate \\(W\\), can one decide in polynomial time whether the generic admissible pencil is spectrally feasible?

The answer may depend on the dimensions and on how \\(W\\) is represented. Even if the algorithm is not polynomial-time, the generic gcd criterion is a much sharper mathematical object than an unconstrained search over all free rows.

### **14.1 Why this is more decisive than more gate enumeration**

The existing gates demonstrate individual algebraic tests. They do not explain the full expressive power of the architecture.

The generic-subspace characterization would identify the exact mechanism through which the data influence feasibility:

\\[ (A,C,L_0) \longrightarrow \mathcal S\_{A,C} \longrightarrow \mathcal T_W \longrightarrow \text{generic pencil}. \\]

Once this mechanism is understood, one can make progress in either direction:

- **Hardness direction:** encode a known hard subspace-selection problem into the choice of \\(W\\).
- **Algorithmic direction:** prove that the possible \\(W\\)-spaces or their generic-pencil conditions have a tractable structure.

Either outcome would be more decisive than another isolated scalar gadget.

## **15. A useful preliminary computation: determine the structure of&#x20;**\\(\mathcal S\_{A,C}\\)

Before implementing the generic gcd calculation, I would compute the image space

\\[ \mathcal S\_{A,C} = \\{(rN,rAN):r\in\mathbb F^{1\times n}\\}. \\]

This is the row-space image of the block matrix

\\[ [N\ \ AN]. \\]

Equivalently,

\\[ \mathcal S\_{A,C} = \operatorname{row}[N\ \ AN]. \\]

Its dimension is

\\[ \dim\mathcal S\_{A,C} = \operatorname{rank}[N\ \ AN]. \\]

This quantity measures how much independent freedom a free row has in choosing its two compressed components. It may be substantially smaller than \\(2k\\), and its structure depends on the interaction of \\(A\\) with \\(K_0\\).

For each candidate \\(W\\), the admissible pair space is simply

\\[ \mathcal T_W = \operatorname{row}[N\ \ AN]\cap(W\oplus W). \\]

This is a linear-algebraic intersection problem. It is a natural place to look for structural obstructions or dimension formulas.

A useful first computational study would therefore record, for random and structured instances:

1. \\(\dim\mathcal S\_{A,C}\\);
2. \\(\dim\mathcal T_W\\);
3. \\(\dim\pi_1(\mathcal T_W)\\);
4. whether the fixed rows are compatible with \\(W\\);
5. whether the generic pencil has gcd one.

These measurements would directly investigate the geometry that controls feasibility, rather than merely collecting feasible or infeasible examples.

# **Part VII. What a valid reduction must prove**

## **16. The reduction theorem should have four separate obligations**

The report's new formulation is correct, but I recommend explicitly separating the obligations of a hardness proof. This will prevent the project from returning to the earlier pattern of proving a local gate and treating it as a reduction.

Suppose the source problem is a polynomial feasibility problem

\\[ \exists x\in\mathbb F^s: \quad f_1(x)=\cdots=f\_\ell(x)=0. \\]

A reduction must construct

\\[ (A_f,C_f,L\_{0,f}) \\]

such that

\\[ \exists x\in\mathbb F^s: f_1(x)=\cdots=f\_\ell(x)=0 \iff \exists R: \operatorname{Feas}(A_f,C_f,L\_{0,f},R). \\]

This equivalence has four logically distinct parts.

### **16.1 Encoding**

There must be a specified way to extract a candidate source assignment from a target witness.

For the present architecture, the natural possibility is

\\[ R\longmapsto W=\operatorname{row}(RN) \\]

or, more accurately, the common row space

\\[ W=\operatorname{row}H=\operatorname{row}H_A. \\]

If the assignment is represented by a coordinate chart of \\(W\\), that chart and the decoding map must be specified.

### **16.2 Completeness**

If the source system has a solution \\(x\\), the construction must produce an actual feasible \\(R\\).

It is not enough to show that some formal pencil has the desired spectral property. The pencil must be realizable through the specified matrices \\(A,C,L_0\\), and the constructed free rows must have the required dimensions and ranks.

### **16.3 Soundness**

If the constructed observer instance is feasible, the source system must have a solution.

This must hold for **every** feasible observer witness, not merely for a specially selected one. If different active subspaces \\(W\\) are possible, every one of them must decode to a valid source solution.

Fibrewise rigidity can help here: if a polynomial decoding relation holds on the feasible points of an active fibre, it holds throughout that fibre. But one must first prove that the decoding relation is indeed satisfied on all feasible points. Fibrewise rigidity does not establish soundness by itself.

### **16.4 Uniformity and size**

The construction must be polynomial-time uniform:

- the matrix dimensions must be polynomially bounded;
- all entries must have polynomial bit length;
- the construction must not use a source solution;
- all constants used in the construction must be explicitly computable;
- the soundness and completeness proofs must be uniform in the source input.

This last point is especially important if one uses distinct constants in a pencil construction. It is easy to prove the existence of suitable constants abstractly; a reduction must also show that they can be selected with polynomial encoding size.

# **Part VIII. A recommended research strategy**

## **17. Three routes, in priority order**

I would organize the next stage into three routes.



Priority 1

**Geometric characterization of active subspaces.**



This is the most important immediate task. Prove the \\(W\\)-level characterization described above. It will identify precisely which part of the input data controls feasibility and where the existential choice resides.



Priority 2

**Subspace-selection hardness.**



Once the active-subspace problem is formalized, look for a source problem whose existential witness is itself a subspace, rank-constrained matrix, or matrix-pencil configuration. This is structurally closer to the observer problem than a direct scalar polynomial-system reduction.



Priority 3

**Boolean witness encoding.**



Try to encode Boolean assignments in Grassmannian coordinates or another parameterization of active \\(W\\)-spaces. The existing Booleanity gate is a useful algebraic primitive, but it must be transferred from supplied coefficients to existential geometric variables.

## **18. A concrete sequence of next results**

I would set the following milestones.

| Milestone | Mathematical deliverable                                                   | Why it matters                                           |
| --------- | -------------------------------------------------------------------------- | -------------------------------------------------------- |
| 1         | Exact characterization of \\(\mathcal T_W\\) and rank completion           | Removes the free-row search for fixed \\(W\\)            |
| 2         | Generic-pencil gcd criterion over the function field of \\(\mathcal T_W\\) | Replaces existential free-row choices by a symbolic test |
| 3         | Algebraic description of the set of active \\(W\\)-spaces                  | Identifies the actual existential geometry               |
| 4         | A Booleanity or linear-equation gadget on \\(W\\)                          | Creates genuine existential source variables             |
| 5         | A uniform polynomial-size reduction                                        | Establishes hardness rather than isolated expressiveness |

I would not return to general multiplication-gate searches until Milestones 1–3 are understood. The previous multiplication-gate attempts were directed at relations inside the free-row fibre, precisely where the rigidity theorem predicts limited expressive power.

## **19. What I would not claim yet**

The report is appropriately cautious about its open questions. I would retain that caution and explicitly avoid the following conclusions:

1. **Do not claim that the architecture can encode arbitrary polynomial systems.** The six primitives do not establish this.
2. **Do not claim that the architecture cannot encode arbitrary polynomial systems.** Fibrewise rigidity does not establish this either.
3. **Do not claim that the Booleanity gate gives a Boolean witness.** It tests an input coefficient.
4. **Do not infer tractability from constructibility.** Constructibility is a structural property, not a polynomial-time algorithm.
5. **Do not infer hardness from the existence of equation gates.** A hardness reduction must encode existential variables and establish both soundness and completeness.
6. **Do not confuse a family of target instances with a single target instance.** Quantifying over that family changes the decision problem unless the family choice is compiled into one ordinary instance.

These qualifications are not weaknesses of the project. They make the research question more precise.

# **Part IX. Suggested replacement text for the report's central conclusion**

I would replace the final paragraph of §II.3 with something like the following.

### The actual expressive-power question

The preceding results show that the observer-feasibility condition can impose nontrivial algebraic restrictions on the instance data, including polynomial equations, Booleanity conditions, and finite conjunctions of such conditions. At the same time, fibrewise rigidity shows that, once the common compressed row space (W) is fixed, spectral feasibility is a nonempty open condition on the corresponding free-row fibre. Thus the architecture does not obtain its expressive power by imposing arbitrary additional polynomial relations among free rows inside a fixed active fibre.

This does not imply that existential reductions are impossible. The active row space (W) remains an existential geometric choice, and the family of subspaces for which the corresponding fibre is spectrally feasible may itself be algebraically constrained by the input data.

The appropriate next step is therefore to characterize the active-subspace set. For fixed (A,C), define\
[\
\Phi(r)=(rN,rAN),\qquad\
\mathcal S\_{A,C}=\operatorname{im}\Phi,\
]\
and, for an (\omega)-dimensional subspace (W),\
[\
\mathcal T_W=\mathcal S\_{A,C}\cap(W\oplus W).\
]\
The feasibility problem can then be studied through the compatibility of the fixed rows with (W), the ability of the first-coordinate projection of (\mathcal T_W) to complete (H) to rank (\omega), and the generic spectral feasibility of the resulting pencil.

The central open question is whether the resulting existential problem over active subspaces is expressive enough to encode a known hard coefficient-feasibility problem, or whether its geometry admits a more restrictive characterization. The existing primitives provide evidence of nontrivial data-side expressiveness, but neither a general hardness reduction nor a general tractability theorem has yet been established.

This wording is stronger than the report's current conclusion because it identifies the next mathematical object, rather than merely restating that expressive power is open.

# **Part X. Final answers to Q1–Q5**

## **Q1. Is the coefficient-condition reformulation the right target?**

**Yes.** It is the correct formulation of the reduction problem:

\\[ \\{(A,C,L_0):\exists R,\ \mathrm{Feas}\\}. \\]

But it should be made precise by fixing the witness field, dimensions, and input encoding. More importantly, it should be refined into an existential problem over active subspaces \\(W\\), with a generic-pencil condition on each fibre.

## **Q2. Is there a structural upper bound?**

**Yes.** For fixed dimensions, the feasibility relation admits a finite algebraic description over an algebraically closed field, and a semialgebraic description for real witnesses. The degrees are bounded in terms of the dimensions after stratifying the kernel-basis construction into coordinate charts.

This does not obstruct NP-hardness or ETR-hardness. It becomes useful only if one can turn the structural description into an efficient algorithm or prove a stronger restriction.

## **Q3. Which source problem should be targeted?**

I would retain existential real feasibility as the broad target, but investigate subspace-selection problems first because they match the geometry of the observer witness.

0–1 linear feasibility is a promising NP-hard target if the Boolean assignment can be encoded in the active subspace. The current Booleanity gate alone does not accomplish this.

## **Q4. Can input-data Booleanity replace existential Boolean variables?**

**No, not in an ordinary many-one reduction.** A reduction cannot choose unknown source variables and place them in the output data. The Booleanity gate checks supplied coefficients; it does not existentially choose them.

The more promising route is to encode the assignment in the choice of \\(W\\), or in another genuine witness parameter.

## **Q5. What is the decisive next result?**

Prove an active-subspace characterization, then derive a generic gcd criterion for the pencil associated with each candidate \\(W\\). This would replace an unconstrained search over free rows with an explicit geometric feasibility problem.

The resulting active-subspace problem is the best candidate for either a hardness reduction or a structural tractability theorem.

## **Final verdict**

Conceptual correction accepted

The report's central correction is sound: **failure to filter free rows inside a fixed fibre is not a proof that existential reductions are impossible.** The relevant expressive power may reside in the input-dependent family of active fibres.

The six primitives are meaningful and, as stated in the report, establish nontrivial algebraic conditions on the instance data. The Booleanity and equation gates are particularly useful additions. But they should not be mistaken for a construction of existential Boolean or polynomial variables.

The strongest next direction is therefore not another isolated gate. It is the characterization

\\[ \boxed{ \text{input data} \longrightarrow \text{admissible subspaces }W \longrightarrow \text{generic compressed pencils} \longrightarrow \text{feasibility}. } \\]

If this characterization yields a hard existential subspace-selection problem, it could provide the missing foundation for an NP-hardness or ETR-hardness result. If instead it yields a tractable structure, it could provide an algorithmic classification of the observer-feasibility problem.

**My recommendation is to treat the active-subspace characterization as the next central theorem of the project.** It is the most direct way to turn the report's new insight into a concrete mathematical result, and it will determine whether the reduction programme should proceed toward hardness or toward a structural algorithm.