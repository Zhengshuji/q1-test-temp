# **Comprehensive review of&#x20;**`100_architecture_limits.md`

## **1. Overall assessment**

This report makes an important conceptual shift: instead of trying to encode arithmetic relations among the free observer rows, it considers placing the source-problem data in \\((A,C,L_0)\\) and using the free rows only as existential witnesses.

That is a worthwhile direction. The report also contains two genuine positive results:

1. A literal gate can test whether a prescribed affine function of the instance data is nonzero.
2. An anchored block-diagonal construction gives a conjunction mechanism. In fact, the proposed \\(k\\)-block soundness conjecture can be strengthened to a theorem by using the rank equality at \\(\lambda=0\\).

However, **the report's central negative conclusion is not established**. There are three important logical gaps:

- Theorem A is a correct fibrewise density statement, but it does not imply that the entire architecture cannot enforce polynomial relations.
- The fact that fixed-fibre feasibility is open does not imply that the full feasible locus, or the accepted instance set, is open.
- Constructibility does not preclude NP-hardness.

The report is therefore best understood as establishing a limitation on the *spectral part of the feasibility condition within a fixed compressed row-space fibre*, not as establishing that the architecture can express only open conditions.

My assessment is:



Established

&#x20;Theorem A as a fibrewise statement, subject to the field qualification below.





Established

&#x20;Literal gate and two-block conjunction.





Strengthenable

&#x20;Arbitrary \\(k\\)-block conjunction.





Overstated

&#x20;"No relation-forcing gadget of any decoding degree."





Not established

&#x20;"Open conditions only" and the resulting no-hardness conclusion.



The most promising next step is to formulate an exact description of the feasible locus as a union of open subsets of linear fibres, then investigate what the *family of fibres* can encode. That is the real geometric issue left by this report.

# **2. Q1: Theorem A is correct, but its conclusion needs a more precise interpretation**

The report considers a fixed instance \\((A,C,L_0)\\) and a fixed compressed rank \\(\omega\\).

Recall the compressed data:

\\[ H=LN,\qquad H_A=LAN, \\]

with

\\[ (5a)\quad \operatorname{row}H_A\subseteq\operatorname{row}H, \\]

and

\\[ (5b)\quad \operatorname{rank}(\lambda H-H_A)=\omega \quad\forall\lambda\in\mathbb C. \\]

Let

\\[ W_0=\operatorname{row}H_0 \\]

be the row space contributed by the fixed rows. For an \\(\omega\\)-dimensional space \\(W\supseteq W_0\\), define

\\[ M_W= \\{R:h_i\in W,\ g_i\in W\text{ for every free row }i\\}. \\]

The key point is that \\(M_W\\) is a linear subspace of the free-parameter space.

## **2.1 The fixed-row compatibility condition is sufficient**

The report assumes

\\[ \operatorname{row}H\_{A,0}\subseteq W_0. \tag{C} \\]

This is exactly the compatibility condition needed.

For every \\(R\in M_W\\), all free \\(h_i\\)'s and \\(g_i\\)'s belong to \\(W\\). The fixed rows satisfy

\\[ \operatorname{row}H_0=W_0\subseteq W \\]

and, by (C),

\\[ \operatorname{row}H\_{A,0}\subseteq W_0\subseteq W. \\]

Consequently, throughout \\(M_W\\),

\\[ \operatorname{row}H\subseteq W, \qquad \operatorname{row}H_A\subseteq W. \\]

Now restrict to the exact-rank subset

\\[ M_W^{(\omega)} = \\{R\in M_W:\operatorname{rank}H=\omega\\}. \\]

Because \\(W\\) has dimension \\(\omega\\),

\\[ W_0\subseteq\operatorname{row}H\subseteq W, \qquad \dim\operatorname{row}H=\dim W=\omega. \\]

Therefore

\\[ \operatorname{row}H=W. \\]

Since all rows of \\(H_A\\) lie in \\(W\\), we obtain

\\[ \operatorname{row}H_A\subseteq W =\operatorname{row}H. \\]

Thus (5a) is automatic on the exact-rank part of \\(M_W\\).

This part of the argument is correct.

## **2.2 The exact-rank condition is open in&#x20;**\\(M_W\\)

Throughout \\(M_W\\), we already know

\\[ \operatorname{rank}H\leq\omega. \\]

The set

\\[ \\{R:\operatorname{rank}H\leq\omega-1\\} \\]

is determinantal and therefore Zariski closed.

Its complement in \\(M_W\\) is precisely \\(M_W^{(\omega)}\\). Hence

\\[ M_W^{(\omega)} \\]

is Zariski open in \\(M_W\\).

## **2.3 The spectral condition is also open on this exact-rank subset**

By the projective-incidence argument established earlier, on a constant-rank stratum the bad spectral locus is relatively closed.

Therefore the good spectral locus is relatively open.

Combining this with the automatic validity of (5a), we obtain

\\[ \boxed{ \mathcal F\_\omega\cap M_W \text{ is Zariski open in }M_W, } \\]

where \\(\mathcal F\_\omega\\) denotes the feasible set at rank \\(\omega\\).

Since \\(M_W\\) is a linear space, it is irreducible. Thus, whenever

\\[ \mathcal F\_\omega\cap M_W\neq\varnothing, \\]

we have

\\[ \boxed{ \overline{\mathcal F\_\omega\cap M_W}^{\\,\mathrm{Zar}} =M_W. } \tag{1} \\]

This proves the essential statement in Theorem A.

### **A qualification about the field of feasible points**

The density conclusion should specify what is meant by a feasible point.

- Over \\(\mathbb C\\), a nonempty Zariski-open subset of \\(M_W\\) is automatically dense.
- Over \\(\mathbb R\\), a nonempty real Zariski-open subset defined over \\(\mathbb R\\) contains a nonempty Euclidean-open subset of the real linear space, so it is Zariski dense.
- Over \\(\mathbb Q\\), the corresponding conclusion holds when the relevant linear space and open set are defined over \\(\mathbb Q\\) and there is a rational feasible point. Rational points are Zariski dense in a rational linear space.

A nonempty complex open set alone does not guarantee a rational feasible point.

I recommend explicitly saying that Theorem A is a statement over \\(\mathbb C\\), or stating the corresponding real/rational version with its nonemptiness assumption.

# **3. The major logical issue: Theorem A does not imply that all polynomial relations are impossible**

This is the most important correction to the report.

Theorem A states:

> If a polynomial \\(q\\) vanishes on every feasible point, then it vanishes identically on every \\(M_W\\) that meets the feasible set.

That statement is correct.

But the report then concludes:

> So no relation-forcing gadget exists — regardless of the decoding degree.

That conclusion is too strong.

## **3.1 Why the conclusion does not follow**

Theorem A says that a relation must hold on every active linear fibre.

It does not say that the union of those fibres is the entire free-parameter space.

Let

\\[ \mathcal W\_\omega^{\mathrm{act}} = \\{W:\dim W=\omega,\ W_0\subseteq W,\ \mathcal F\_\omega\cap M_W\neq\varnothing\\}. \\]

Then the feasible set is

\\[ \mathcal F\_\omega = \bigcup\_{W\in\mathcal W\_\omega^{\mathrm{act}}} (\mathcal F\_\omega\cap M_W). \\]

By (1), each nonempty piece is dense in its corresponding \\(M_W\\). It follows that

\\[ \boxed{ \overline{\mathcal F\_\omega}^{\\,\mathrm{Zar}} = \overline{ \bigcup\_{W\in\mathcal W\_\omega^{\mathrm{act}}}M_W }^{\\,\mathrm{Zar}}. } \tag{2} \\]

This is a stronger and more informative formulation of Theorem A.

It says that the spectral condition cannot remove a proper algebraic subset from an individual active fibre. But it can select which fibres are active.

And the union of a family of linear spaces can be nonlinear.

For example, the variety of matrices of rank at most one is the union of many linear spaces parameterized by their possible row or column spaces. Each individual fibre is linear, but their union is a nonlinear determinantal variety.

That is precisely the kind of geometry that can arise here.

## **3.2 There are already polynomial relations in the compressed model**

Consider the stacked matrix

\\[ S= \begin{bmatrix} H\\\H_A \end{bmatrix}. \\]

For every feasible point,

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H. \\]

Since \\(\operatorname{rank}H=\omega\\), this gives

\\[ \operatorname{rank}S=\omega. \\]

Consequently, all \\((\omega+1)\times(\omega+1)\\) minors of \\(S\\) vanish:

\\[ \boxed{ \det S\_{I,J}=0 \quad \text{for all }|I|=|J|=\omega+1. } \tag{3} \\]

These are polynomial relations in the free-row parameters.

They are not necessarily identically zero on the entire free-parameter space. They are imposed by the row-space inclusion condition and the rank restriction.

Thus, under the report's own definition—

> a gadget expresses a relation if that relation holds at every feasible point—

the architecture does express polynomial relations.

Theorem A does not contradict this. It says that these relations must already vanish on every active \\(M_W\\).

### **3.3 What Theorem A actually proves**

I recommend replacing the sentence "no relation-forcing gadget exists" with the following:

> **Fibrewise relation rigidity.** Once a compressed row space \\(W\\) is fixed, the spectral feasibility condition cannot impose any additional polynomial relation on the free parameters within a nonempty fibre \\(M_W\\). Every polynomial relation satisfied by all feasible points of that fibre is already an identity on the entire linear space \\(M_W\\). Any nonlinear algebraic restrictions on the full feasible set must therefore arise from the geometry of the family of active row spaces \\(W\\), rather than from further algebraic cutting inside an individual active fibre.

This is a strong theorem, and it is exactly what the proof establishes.

It is also a much more useful starting point for studying the second paradigm.

# **4. Q2: the two-block conjunction proof is correct, and the&#x20;**\\(k\\)**-block conjecture can be proved**

The report's two-block proof is valid. But it uses more of the pencil condition than is necessary.

There is a simpler general argument that proves the soundness part for every number of blocks.

## **4.1 A general kernel lemma**

Let \\(H,H_A\\) be a feasible compressed pair, and write

\\[ \omega=\operatorname{rank}H. \\]

From (5b), setting \\(\lambda=0\\), we get

\\[ \operatorname{rank}H_A=\omega. \\]

From (5a),

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H. \\]

The two row spaces have equal dimension. Therefore

\\[ \boxed{ \operatorname{row}H_A=\operatorname{row}H. } \tag{4} \\]

As linear maps from the compressed coordinate space \\(\mathbb C^k\\) to the row-coordinate space, \\(H\\) and \\(H_A\\) therefore have the same kernel:

\\[ \boxed{ \ker H=\ker H_A. } \tag{5} \\]

In particular, for every standard coordinate vector \\(e_i\\),

\\[ He_i=0 \quad\Longleftrightarrow\quad H_Ae_i=0. \tag{6} \\]

This means that a feasible compressed pair must have exactly the same zero-column pattern in \\(H\\) and \\(H_A\\).

This is a useful general structural lemma in its own right.

## **4.2 Apply it to the block construction**

For the \\(k\\)-block direct sum, the report has

\\[ H\_{\bullet i}= \begin{pmatrix} 1\\\u_i \end{pmatrix}, \qquad (H_A)\_{\bullet i}= \begin{pmatrix} 0\\\t_i v_i \end{pmatrix}. \\]

If \\(t_i=0\\), then

\\[ (H_A)\_{\bullet i}=0. \\]

But the fixed anchor ensures

\\[ H\_{\bullet i}\neq0. \\]

This contradicts (6).

Therefore

\\[ \boxed{ \text{If any }t_i=0,\text{ the block construction is infeasible.} } \tag{7} \\]

Notice that this argument does not require \\(m=2\\), \\(m=k\\), or any comparison of the pencil at nonzero \\(\lambda\\).

It proves the soundness direction for arbitrary \\(k\\) and arbitrary numbers of free rows.

This is stronger than the report's current two-block result.

## **4.3 The converse: if all&#x20;**\\(t_i\neq0\\)**, construct a feasible witness**

We can also give an explicit witness when \\(m=k\\).

Assume

\\[ t_i\neq0,\qquad i=1,\ldots,k. \\]

Choose pairwise distinct nonzero scalars

\\[ d_1,\ldots,d_k. \\]

Set

\\[ H= \begin{bmatrix} 1&1&\cdots&1\\\ 1&0&\cdots&0\\\ 0&1&\cdots&0\\\ \vdots&\vdots&\ddots&\vdots\\\ 0&0&\cdots&1 \end{bmatrix} = \begin{bmatrix} \mathbf 1^T\\\I_k \end{bmatrix}, \\]

and

\\[ H_A= \begin{bmatrix} 0&0&\cdots&0\\\ d_1&0&\cdots&0\\\ 0&d_2&\cdots&0\\\ \vdots&\vdots&\ddots&\vdots\\\ 0&0&\cdots&d_k \end{bmatrix} = \begin{bmatrix} 0\\\D \end{bmatrix}, \qquad D=\operatorname{diag}(d_1,\ldots,d_k). \\]

These matrices are realizable in the block construction:

- The free-row entries can be chosen to give \\(I_k\\) in the \\(H\\) block.
- Since every \\(t_i\neq0\\), choose the corresponding free-row entries in the \\(H_A\\) block to give \\(d_i/t_i\\) on the diagonal and zero elsewhere.

We have

\\[ \operatorname{rank}H=k,\qquad \operatorname{rank}H_A=k. \\]

Since \\(H\\) has full column rank, (5a) is automatic:

\\[ \operatorname{row}H=\mathbb C^k. \\]

Now consider

\\[ P(\lambda)=\lambda H-H_A = \begin{bmatrix} \lambda\mathbf1^T\\\ \lambda I_k-D \end{bmatrix}. \\]

We prove that \\(P(\lambda)\\) has full column rank for every \\(\lambda\in\mathbb C\\).

**Case 1:&#x20;**\\(\lambda\notin\\{d_1,\ldots,d_k\\}\\)**.**

Then

\\[ \lambda I_k-D \\]

is invertible. Thus \\(P(\lambda)\\) has full column rank.

**Case 2:&#x20;**\\(\lambda=d_j\\)**&#x20;for some&#x20;**\\(j\\)**.**

Because the \\(d_i\\)'s are pairwise distinct,

\\[ \lambda I_k-D \\]

has a one-dimensional kernel:

\\[ \ker(\lambda I_k-D)=\operatorname{span}\\{e_j\\}. \\]

The top row satisfies

\\[ \lambda\mathbf1^Te_j=d_j\neq0. \\]

Therefore the top row eliminates the only possible kernel direction, and \\(P(\lambda)\\) has full column rank.

Hence

\\[ \operatorname{rank}(\lambda H-H_A)=k \qquad\forall\lambda\in\mathbb C. \\]

This proves feasibility.

Combining this with (7), we obtain the following theorem.

Proved

**Theorem: arbitrary-**\\(k\\)**&#x20;conjunction gate**

For the anchored \\(k\\)-block direct-sum construction, with \\(m=k\\) free rows, the instance is feasible if and only if

\\[ \boxed{\prod\_{i=1}^k t_i\neq0.} \\]

Equivalently, feasibility holds exactly when every block parameter is nonzero.

This is a substantial improvement over the report's current reliability table.

It also means the three-block exhaustive checks are no longer needed to support the general soundness claim. They can remain as computational validation of the construction, but the general result has an exact proof.

### **A further consequence**

The zero-column argument is not specific to this block construction.

For any feasible compressed pair,

\\[ \ker H=\ker H_A. \\]

Therefore the two matrices have the same linear dependence relations among their columns, not merely the same zero columns.

In particular, for every subset \\(J\\) of compressed coordinates,

\\[ \operatorname{rank}H\_{[:,J]} = \operatorname{rank}(H_A)\_{[:,J]}. \\]

This gives a family of necessary conditions that could be useful in designing or excluding other gates.

# **5. The literal gate: correct, but clarify what it computes**

The report uses one block with

\\[ C_i=[0\ 0\ 1],\qquad A_i(t)= \begin{pmatrix} 0&0&0\\\ t&0&0\\\ 0&1&0 \end{pmatrix}, \qquad L\_{0,i}=[1\ 0\ 0]. \\]

Here

\\[ K_0=\ker \begin{bmatrix} 0&0&1\\\ 0&1&0 \end{bmatrix} =\operatorname{span}\\{e_1\\}. \\]

Taking \\(N=e_1\\), a free row \\(r=(r_1,r_2,r_3)\\) gives

\\[ H= \begin{pmatrix} 1\\\r_1 \end{pmatrix}, \qquad H_A= \begin{pmatrix} 0\\\tr_2 \end{pmatrix}. \\]

Thus

\\[ P(\lambda)= \begin{pmatrix} \lambda\\\ \lambda r_1-tr_2 \end{pmatrix}. \\]

Because

\\[ \operatorname{rank}H=1, \\]

feasibility requires \\(P(\lambda)\neq0\\) for every \\(\lambda\\).

If \\(t=0\\), then at \\(\lambda=0\\),

\\[ P(0)=0. \\]

So the instance is infeasible.

If \\(t\neq0\\), choose \\(r_2\neq0\\). Then:

- at \\(\lambda=0\\), the second component is nonzero;
- at every \\(\lambda\neq0\\), the first component is nonzero.

Thus the instance is feasible.

Therefore

\\[ \boxed{\text{literal block feasible}\iff t\neq0.} \\]

This is correct.

## **5.1 Negation**

If \\(x\in\\{0,1\\}\\), then

\\[ 1-x\neq0 \quad\Longleftrightarrow\quad x=0. \\]

So feeding \\(1-x\\) into the literal gate tests the negated Boolean literal.

This is correct, provided Booleanity of \\(x\\) is already guaranteed by the source problem or another part of the construction.

## **5.2 What the literal gate does not provide**

The gate does not itself enforce

\\[ x(1-x)=0. \\]

If \\(x\\) is an unrestricted complex or rational parameter, then

\\[ x\neq0 \quad\text{and}\quad 1-x\neq0 \\]

are simply two open conditions. They do not imply that \\(x\\) is Boolean.

This distinction is crucial for the hardness programme.

The literal gate is a nonzero tester. It is not a Booleanity gate.

# **6. The conjunction mechanism is now established, but it does not solve the disjunction problem**

The report correctly identifies that the anchored direct sum makes each block contribute a nonzero column to \\(H\\), while the corresponding column of \\(H_A\\) disappears when \\(t_i=0\\).

The general proof above shows that this gives

\\[ t_1\neq0\land\cdots\land t_k\neq0. \\]

However, conjunction of nonzero tests is not the same as disjunction.

For two arbitrary field elements \\(a,b\\), the condition

\\[ a\neq0\ \lor\ b\neq0 \\]

is different from

\\[ a+b\neq0. \\]

The second can fail when \\(a=-b\neq0\\).

If \\(a,b\\) are Boolean values, then

\\[ a+b\neq0 \quad\Longleftrightarrow\quad a\lor b. \\]

But that equivalence depends on Booleanity.

This is another reason the missing Booleanity condition matters.

### **6.1 The report's disjunction experiments are not a general impossibility result**

The two failed constructions show that:

- removing the anchor can introduce a rank-zero witness;
- the tested layer-separation construction gives an open condition rather than the desired disjunction.

These are useful observations, but they do not establish that all disjunction gadgets fail.

In particular, the first failure should be explained more precisely.

If removing the anchor permits

\\[ R=0,\qquad H=0,\qquad H_A=0, \\]

then

\\[ \omega=0 \\]

and both rank conditions hold trivially. This is the vacuous witness.

The issue is not that every nonzero single-column pencil is automatically feasible. For a nonzero \\(h\\), the condition

\\[ \lambda h-g\neq0\quad\forall\lambda \\]

requires \\(g\notin\operatorname{span}\\{h\\}\\). The zero witness is the more direct explanation of the failure.

I recommend replacing the current discussion with that rank-zero explanation.

# **7. Q3: the "open conditions only" conclusion is not a theorem**

This is the second major conceptual issue.

The report observes that feasibility is open within each fixed-\\(W\\) fibre. It then concludes that the architecture can express only open conditions, or disjunctions of open conditions.

That inference is invalid.

## **7.1 Fixed-fibre openness does not imply global openness**

For each fixed \\(W\\),

\\[ \mathcal F\_\omega\cap M_W \\]

is open in \\(M_W\\).

But the full feasible set is

\\[ \mathcal F\_\omega = \bigcup\_{W\in\mathcal W\_\omega^{\mathrm{act}}} (\mathcal F\_\omega\cap M_W). \\]

The spaces \\(M_W\\) themselves vary with \\(W\\).

A union of open subsets of different linear subspaces need not be open in the ambient parameter space. It can be a nonlinear algebraic variety, or a locally closed subset of one.

A standard geometric example is the variety of matrices of rank at most one. It is a union of linear spaces parameterized by possible row spaces, but the union is defined by quadratic determinantal equations.

The compressed observer model has the same basic geometric possibility.

## **7.2 The full feasible rank stratum has an explicit determinantal description**

Let

\\[ S= \begin{bmatrix} H\\\H_A \end{bmatrix}. \\]

On the rank-\\(\omega\\) stratum, condition (5a) is equivalent to

\\[ \operatorname{rank}S\leq\omega. \\]

Indeed, since \\(H\\) is already a submatrix of \\(S\\),

\\[ \operatorname{rank}S\geq\operatorname{rank}H=\omega. \\]

Thus \\(\operatorname{rank}S\leq\omega\\) forces equality, which is exactly the row-space inclusion.

Consequently, the feasible rank-\\(\omega\\) locus can be written as

\\[ \boxed{ \mathcal F\_\omega = \left\\{ R: \begin{array}{l} \operatorname{rank}H=\omega,\\\ \operatorname{rank}\begin{bmatrix}H\\\H_A\end{bmatrix}\leq\omega \end{array} \right\\} \cap\mathcal O\_\omega, } \tag{8} \\]

where \\(\mathcal O\_\omega\\) denotes the good spectral locus within the rank-\\(\omega\\) stratum.

The first condition is locally closed. The second is determinantal and closed. The spectral condition is open relative to the appropriate rank stratum.

Thus the complete feasible set is not simply an open set. It is an open subset of a determinantal, locally closed locus.

That determinantal locus can impose polynomial equations on the free rows.

This is exactly why the conclusion "open conditions only" is too strong.

## **7.3 What is genuinely open?**

The following statement is correct:

> Once \\(W\\) is fixed and the fixed rows are compatible, spectral feasibility is a Zariski-open condition on the exact-rank part of the linear fibre \\(M_W\\).

But this does not establish that the full feasibility problem is open in:

- the free-row parameters;
- the instance parameters \\((A,C,L_0)\\);
- or the source-problem variables used in a reduction.

The distinction between these three parameter spaces must be preserved.

# **8. Constructibility does not preclude NP-hardness**

Even if the accepted instance set were constructible, this would not imply that the problem is easy or not NP-hard.

This is a fundamental point for the complexity argument.

## **8.1 What Chevalley's theorem would give**

Suppose the instance data are parameterized by coordinates \\(a\\), and the free-row witness by coordinates \\(r\\).

If feasibility can be expressed by a finite constructible condition

\\[ \mathcal X\subseteq\mathcal A\times\mathcal R, \\]

then the set of accepted instance parameters is the projection

\\[ \pi(\mathcal X) = \\{a:\exists r,\ (a,r)\in\mathcal X\\}. \\]

Over an algebraically closed field, Chevalley's theorem says that the projection of a constructible set is constructible.

This is a valid structural statement, assuming the spectral condition has been replaced by a finite algebraic certificate, as in the earlier gcd/Bézout formulation.

But it is not a complexity bound.

## **8.2 A concrete counterexample to the proposed inference**

Boolean satisfiability itself can be expressed as an existential polynomial system.

For each Boolean variable \\(x_i\\), impose

\\[ x_i(1-x_i)=0. \\]

For a clause with literals \\(\ell_1,\ell_2,\ell_3\\), impose

\\[ (1-\ell_1)(1-\ell_2)(1-\ell_3)=0. \\]

Over \\(\mathbb C\\), the first equations force

\\[ x_i\in\\{0,1\\}, \\]

and the clause equation forces at least one literal to equal one.

Therefore a Boolean formula is satisfiable exactly when the corresponding polynomial system has a complex solution.

The set of coefficients for which such a solution exists is a projection of an algebraic set, hence constructible by Chevalley's theorem.

Yet SAT is NP-complete.

So:

\\[ \boxed{ \text{Constructibility does not imply tractability or rule out NP-hardness.} } \\]

Likewise, an open condition on a continuous ambient parameter space need not make a decision problem easy on a discrete encoded input domain.

## **8.3 The "finite intersection of open sets is nonempty" argument also needs qualification**

The report says that finitely many nonzero polynomial conditions can always be made simultaneously nonzero over an algebraically closed field.

This is true if all the conditions define nonempty Zariski-open subsets of the **same irreducible parameter space**.

It does not apply automatically when:

- the instance parameters are fixed;
- the parameter space is a constrained subvariety;
- some constraints are equations;
- or the existential variables are restricted to a discrete set.

For example, the two conditions

\\[ x\neq0,\qquad 1-x\neq0 \\]

have a nonempty intersection over \\(\mathbb C\\), but this does not mean they are satisfiable for every fixed input \\(x\in\\{0,1\\}\\).

The report needs to distinguish:

1. variables ranging freely over an irreducible algebraic variety;
2. fixed input data;
3. existential witness variables;
4. Boolean or other discrete source variables.

Without this distinction, the open-set argument cannot support a complexity conclusion.

# **9. Q4: where can equations come from?**

The report says that the only possible sources of equations are structural quantities such as \\(\dim K_0\\), the layer, and rank identities.

This is a good starting point, but it understates the role of the first compressed rank condition.

There are already several sources of equations.

## **9.1 Row-space inclusion is a determinantal equation**

Condition (5a) is equivalent to

\\[ \operatorname{rank} \begin{bmatrix} H\\\H_A \end{bmatrix} = \operatorname{rank}H. \\]

On a fixed rank-\\(\omega\\) stratum, this is equivalent to the vanishing of all \\((\omega+1)\\)-minors of the stacked matrix.

These are polynomial equations in the free-row parameters.

Thus the architecture does have an equation-producing mechanism on the witness side.

Theorem A only says that these equations are already present throughout every active \\(M_W\\); it does not eliminate them.

## **9.2 The rank of&#x20;**\\(H\\)**&#x20;is itself a stratifying condition**

The equation

\\[ \operatorname{rank}H=\omega \\]

combines:

- the vanishing of all \\((\omega+1)\\)-minors;
- the nonvanishing of at least one \\(\omega\\)-minor.

It is a locally closed algebraic condition.

The layer structure therefore is not purely open.

## **9.3 The&#x20;**\\(\lambda=0\\)**&#x20;condition imposes another rank identity**

Feasibility gives

\\[ \operatorname{rank}H_A=\operatorname{rank}H. \\]

Together with (5a), this forces

\\[ \operatorname{row}H_A=\operatorname{row}H \\]

and hence

\\[ \ker H=\ker H_A. \\]

This is a strong structural restriction on the compressed pair.

## **9.4 The instance data can also encode rank equations**

The quantity

\\[ k=\dim\ker[C;CA] \\]

is determined by the rank of \\([C;CA]\\).

Likewise,

\\[ \dim(AK_0) \\]

is determined by the rank of the restriction of \\(A\\) to \\(K_0\\).

These quantities change on determinantal strata of the instance parameter space.

Thus, in principle, the instance side contains algebraic rank conditions as well as open spectral conditions.

The real question is not whether equations exist. They do.

The real question is:

> Can the available determinantal restrictions, together with existential quantification over the free rows, encode a sufficiently expressive family of algebraic constraints to support a hardness reduction?

The present report does not answer that question.

# **10. Q5: should the multiplication-gadget route be abandoned?**

I would separate the two paradigms much more sharply.

## **10.1 Paradigm 1: source variables in the free rows**

Theorem A gives a genuine obstruction:

- For a fixed \\(W\\), the feasible subset is open in \\(M_W\\).
- Therefore no new polynomial relation can be imposed *inside that fixed fibre* by spectral feasibility.
- Any polynomial relation satisfied by the full feasible set must hold on every active fibre.

For affine-linear decoding, the earlier exclusion theorem gives a stronger conclusion: the feasible set is contained in a union of two fixed affine hyperplanes whenever the intended multiplication relation holds.

That rules out a non-degenerate multiplication gate with independently variable inputs.

But the degree-free conclusion in the present report is too strong. Polynomial decoding can implement multiplication identically on a linear fibre, and the family of active fibres may have nonlinear geometry.

My recommendation is:

**Do not claim a degree-free impossibility theorem.** Retain Theorem A as a fibrewise rigidity theorem, and retain the affine-linear multiplication exclusion as a separate, stronger theorem under its specific decoding assumptions.

## **10.2 Paradigm 2: source data in the instance, free rows as witnesses**

This is a potentially more promising route, but the report has not yet demonstrated a full reduction.

The literal gate gives

\\[ t\neq0. \\]

The anchored direct sum gives

\\[ t_1\neq0\land\cdots\land t_k\neq0. \\]

These are useful primitives.

However, to obtain a hardness reduction, one must also address:

1. How are existential source variables represented?
2. How is Booleanity enforced, if the source variables are intended to be Boolean?
3. How is disjunction implemented?
4. How are clauses combined without creating unintended lower-rank witnesses?
5. How is the construction uniform and polynomial in the source input size?
6. How is the reduction sound and complete for all possible free-row witnesses?

The report currently addresses the literal and conjunction parts, but not the other requirements.

The missing Booleanity and disjunction mechanisms are especially important. A conjunction of nonzero tests does not by itself simulate general Boolean satisfiability.

## **10.3 My recommendation**

I would not abandon the whole gadget programme yet, but I would stop trying to prove the current "open conditions only" theorem.

Instead, I would focus on whether the rank structure can enforce a Boolean choice.

A promising question is:

> Can one construct a small block for which the feasible rank strata correspond exactly to two alternatives, with no rank-zero or unintended higher-rank witness?

That is more concrete than attempting an arbitrary OR gate immediately.

The equality

\\[ \ker H=\ker H_A \\]

may help in designing such a construction, because it gives an exact condition on the dependence patterns of the compressed columns.

# **11. A revised mathematical statement that I recommend publishing**

I would replace the current Theorem A and its claimed consequence with the following formulation.

## **Theorem: fibrewise spectral rigidity**

Fix an instance \\((A,C,L_0)\\) with compatible fixed rows, and fix a compressed rank \\(\omega\\).

For every \\(\omega\\)-dimensional subspace \\(W\supseteq W_0\\), let

\\[ M_W=\\{R:h_i,g_i\in W\text{ for all free rows }i\\}. \\]

Then:

1. \\(M_W\\) is a linear subspace of the free-parameter space.
2. The feasible subset \\(\mathcal F\_\omega\cap M_W\\) is Zariski open in \\(M_W\\).
3. If \\(\mathcal F\_\omega\cap M_W\neq\varnothing\\), then it is Zariski dense in \\(M_W\\).
4. Consequently, every polynomial vanishing on the full feasible set vanishes identically on every active fibre.
5.

# **In particular, \\[ \overline{\mathcal F\_\omega}^{,\mathrm{Zar}}**

\overline{\
\bigcup\_{W\in\mathcal W\_\omega^{\mathrm{act}}}M_W\
}^{,\mathrm{Zar}}.\
\\]

**Interpretation.** The spectral condition selects active row-space fibres but does not impose additional polynomial equations inside any active fibre. Any nonlinear algebraic relations in the full feasible locus must arise from the geometry of the family of active row spaces.

This is, in my view, the strongest correct version of the report's main insight.

## **Theorem: arbitrary-block conjunction**

For the anchored direct-sum literal construction with \\(k\\) blocks and \\(m=k\\) free rows, feasibility holds if and only if

\\[ \prod\_{i=1}^k t_i\neq0. \\]

The proof is the zero-column/kernel argument for soundness and the explicit diagonal construction for completeness.

These two theorems would make a good core for a revised report.

# **12. Revised reliability table**

| Claim                                                             | Assessment                                                                                |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Theorem A: nonempty feasible fibre is open and dense in \\(M_W\\) | Proved, with compatibility and field qualifications                                       |
| Theorem A implies no polynomial relation of any degree            | False as stated                                                                           |
| Theorem A implies fibrewise polynomial rigidity                   | Proved                                                                                    |
| \\(\ker H=\ker H_A\\) for every feasible compressed pair          | Proved                                                                                    |
| Literal gate \\(t\neq0\\)                                         | Proved                                                                                    |
| Negation by \\(t\mapsto1-x\\)                                     | Proved, assuming Boolean inputs                                                           |
| Two-block conjunction soundness                                   | Proved                                                                                    |
| Arbitrary-\\(k\\) conjunction soundness                           | Proved by the kernel lemma                                                                |
| Arbitrary-\\(k\\) conjunction completeness with \\(m=k\\)         | Proved by explicit construction                                                           |
| Disjunction impossible                                            | Not proved                                                                                |
| Full feasible locus is open                                       | Not proved; generally false as an inference                                               |
| Accepted instance set is constructible                            | Plausible under a finite algebraic certificate and algebraically closed-field formulation |
| Constructibility rules out NP-hardness                            | False                                                                                     |
| Architecture cannot encode equations                              | False as stated; determinantal equations are already present                              |
| Original decision problem cannot be NP-hard                       | Not established                                                                           |

# **13. The most important next research tasks**

I recommend the following order.

**1. Formalize the kernel-equality lemma**

Immediate

Put

\\[ \ker H=\ker H_A \\]

into the main structural theory. Derive its consequences for column dependencies, zero columns, and possible block constructions.

**2. Upgrade conjunction to the arbitrary-**\\(k\\)**&#x20;theorem**

Immediate

Replace the conjecture and exhaustive checks with the explicit construction

\\[ H=\begin{bmatrix}\mathbf1^T\\\I_k\end{bmatrix}, \qquad H_A=\begin{bmatrix}0\\\D\end{bmatrix}, \\]

where \\(D\\) is diagonal with distinct nonzero entries.

**3. Rewrite Theorem A as fibrewise rigidity**

Immediate

Keep the density theorem but remove the claim that it rules out every polynomial relation. Emphasize that the family of active \\(W\\)'s can have nonlinear geometry.

**4. Investigate Booleanity and disjunction**

Main gadget problem

A useful target is a two-alternative block whose feasible locus has exactly two intended branches and no rank-zero escape.

**5. Reassess hardness through existential instance feasibility**

Main complexity problem

Identify exactly what the source variables are, which are fixed in the instance, which are existentially quantified, and which are represented by free-row witnesses. Then formulate a reduction without relying on an unproved open-only limitation.

# **14. Final verdict**

The report has two important contributions, but its most ambitious conclusion is not yet justified.

The first contribution is the fibrewise density theorem. It shows that once the compressed row space \\(W\\) is fixed, the spectral condition cannot impose a further algebraic relation inside that linear fibre. This is a useful structural limitation and a natural continuation of the previous pinned-instance and affine-linear decoding results.

The second contribution is the anchored literal gate. More importantly, its conjunction mechanism can be proved for arbitrary \\(k\\), using a simple consequence of the \\(\lambda=0\\) condition:

\\[ \boxed{\ker H=\ker H_A.} \\]

That identity is worth emphasizing in the larger research project.

But the report's proposed architecture-level no-go conclusion needs to be withdrawn or substantially narrowed. Fibrewise openness does not imply global openness; constructibility does not imply tractability; and the model already contains determinantal equations through (5a) and the rank conditions.

My recommendation is to **retain the structural results, strengthen the conjunction theorem, and abandon the claim that the architecture can express only open conditions**.

The most promising remaining question is whether the determinantal geometry of the active row-space family can enforce Boolean choices or disjunctions without admitting unintended witnesses. That is a concrete mathematical problem, and solving it would tell us much more about the actual hardness potential of the compressed observer model than the current open-only argument.

100_architecture_limits.md