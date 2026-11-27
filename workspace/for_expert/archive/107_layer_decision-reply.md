# **Detailed review of&#x20;**`107_layer_decision.md`

## **1. Overall assessment**

This report is a substantial improvement over `106_layer_table.md`. In particular, it makes three important corrections:

1. It withdraws the claim that every middle layer is infeasible.
2. It replaces the incorrect condition \\(\mathcal T_W=W\oplus W\\) with a criterion based on the evaluation maps \\(E\_\lambda\\).
3. It acknowledges that the search over \\(W\\) remains unresolved, rather than claiming that the entire decision problem is polynomial-time decidable.

These are the right directions. The middle-layer proposition is a genuine structural advance: it identifies a finite-dimensional linear space of admissible compressed row pairs and turns the spectral condition into a polynomial gcd test.

However, **the central proposition is incomplete as stated**. It establishes the spectral part of feasibility but omits a separate requirement: the selected rows must actually make \\(\operatorname{rank}H=\omega\\). Surjectivity of \\(E\_\lambda\\) for all finite \\(\lambda\\) does not imply this.

There is also an important unresolved issue in the top layer. The condition that no eigenvector of \\(A\\) lies in \\(K_0\\) is a pointwise necessary condition, but the report has not established that a fixed, finite collection of admissible rows can satisfy the pencil condition simultaneously for every \\(\lambda\\).

My overall assessment is:



Significant progress

&#x20;The middle-layer reformulation is mathematically useful and likely worth retaining.





Major theorem correction needed

&#x20;The middle-layer equivalence needs a rank-completion hypothesis, and the top-layer sufficiency remains unproved.





Research direction

&#x20;The main unresolved complexity issue is now the existential search over \\(W\\), together with the interaction between rank completion and spectral regularity.



I will examine the report in detail.

## **2. The middle-layer proposition: correct idea, incomplete statement**

The report states:

> Fix a compatible \\(W\\) and let \\(m\\) be the number of free rows. If \\(m\geq\dim\mathcal T_W\\), then the layer is feasible on the fibre of \\(W\\) if and only if \\(E\_\lambda(\mathcal T_W)=W\\) for every \\(\lambda\\).

107_layer_decision.md

Here

\\[ \mathcal T_W=\mathcal S\cap(W\oplus W), \qquad E\_\lambda(x,y)=\lambda x-y. \\]

The proposition has an important strength: it reduces a potentially complicated choice of free rows to a property of the entire admissible pair space.

But it overlooks one of the two conditions defining the layer.

Recall that

\\[ H=LN,\qquad H_A=LAN, \\]

and the layer number is

\\[ \omega=\operatorname{rank}H. \\]

The feasibility requirements are

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H \\]

and

\\[ \operatorname{rank}(\lambda H-H_A)=\omega \quad\forall\lambda\in\mathbb C. \\]

The second condition does not, by itself, establish that \\(\operatorname{rank}H=\omega\\).

### **2.1 Why evaluation surjectivity does not imply rank completion**

Suppose

\\[ \mathcal T_W=\\{(0,y):y\in W\\}=\\{0\\}\oplus W. \\]

Then

\\[ E\_\lambda(\mathcal T_W) =\\{-y:y\in W\\} =W \\]

for every \\(\lambda\\).

Thus the proposed evaluation condition holds perfectly.

However,

\\[ \pi_1(\mathcal T_W)=\\{0\\}. \\]

If the fixed first components also vanish, then every possible choice of free rows satisfies

\\[ H=0, \\]

so the required rank condition

\\[ \operatorname{rank}H=\omega>0 \\]

is impossible.

This exposes the missing logical implication:

\\[ E\_\lambda(\mathcal T_W)=W\quad\forall\lambda \quad\centernot\Longrightarrow\quad \pi_1(\mathcal T_W)=W. \\]

The evaluation maps can be surjective entirely because of the second components \\(y\\), even if the first components \\(x\\) never generate \\(W\\).

This is not a minor technicality. It means that the proposition, as written, does not characterize feasibility.

### **2.2 The missing rank-completion condition**

Let the fixed compressed pairs be

\\[ (h_i^0,g_i^0)\in W\oplus W, \qquad i=1,\ldots,r_0. \\]

Define

\\[ V_0=\operatorname{span}\\{h_1^0,\ldots,h\_{r_0}^0\\} \\]

and

\\[ V_1(W)=\pi_1(\mathcal T_W). \\]

The exact rank-completion condition is

\\[ \boxed{V_0+V_1(W)=W.} \\]

This is the condition that must accompany the evaluation-map condition.

The good news is that the report's row-count hypothesis \\(m\geq\dim\mathcal T_W\\) makes rank completion particularly easy to handle: choosing a basis of \\(\mathcal T_W\\) as the free rows realizes every possible first component in \\(\pi_1(\mathcal T_W)\\).

Therefore, a corrected proposition is available.

### **2.3 Corrected middle-layer proposition**

**Proposition (fixed-fibre feasibility with sufficient free rows).**

Fix a compatible \\(\omega\\)-dimensional subspace \\(W\\), and let

\\[ D_W=\dim\mathcal T_W. \\]

Assume that the free-row count satisfies

\\[ m\geq D_W. \\]

Then the layer is feasible on the fibre of \\(W\\) if and only if both conditions hold:

\\[ \tag{R} \operatorname{span}\left( \\{h_i^0\\}\_{i=1}^{r_0} \cup \pi_1(\mathcal T_W) \right)=W, \\]

and

\\[ \tag{E} E\_\lambda(\mathcal T_W)=W \qquad\forall\lambda\in\mathbb C. \\]

**Proof.**

*Necessity.*

Suppose a feasible collection of free rows has compressed pairs

\\[ (x_j,y_j)\in\mathcal T_W. \\]

Since

\\[ \operatorname{rank}H=\omega=\dim W, \\]

the first components of the fixed and free rows span \\(W\\). Hence

\\[ \operatorname{span}\left( \\{h_i^0\\}\cup\pi_1(\mathcal T_W) \right)=W. \\]

Next, the rows of the pencil \\(\lambda H-H_A\\) are exactly the evaluations

\\[ \lambda h_i^0-g_i^0,\qquad \lambda x_j-y_j. \\]

All these vectors belong to \\(E\_\lambda(\mathcal T_W)\\), because every fixed and free pair belongs to \\(\mathcal T_W\\).

Since the pencil has rank \\(\omega\\), its rows span \\(W\\). Therefore

\\[ E\_\lambda(\mathcal T_W)=W \\]

for every \\(\lambda\\).

*Sufficiency.*

Choose a basis

\\[ t_1,\ldots,t\_{D_W} \\]

of \\(\mathcal T_W\\), and use these pairs as the free compressed rows. This is possible because every element of \\(\mathcal S\\) is realizable as \\((rN,rAN)\\) for some row \\(r\\).

By (R), the fixed first components together with the first components of the chosen basis span \\(W\\). Thus

\\[ \operatorname{rank}H=\omega. \\]

Since all fixed and free pairs lie in \\(W\oplus W\\),

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H. \\]

Finally, the pencil rows include the evaluations of a basis of \\(\mathcal T_W\\). By (E), those evaluations span \\(W\\) for every \\(\lambda\\). Consequently,

\\[ \operatorname{rank}(\lambda H-H_A)=\omega \\]

for every \\(\lambda\\).

This proves feasibility. \\(\square\\)

This should replace the current Proposition II.1.

## **3. The gcd test: mathematically correct, but it needs one additional test**

The report proposes choosing a basis

\\[ p_j=(x_j,y_j),\qquad j=1,\ldots,D_W, \\]

of \\(\mathcal T_W\\), forming

\\[ M_W(\lambda)= \begin{pmatrix} \lambda x_1-y_1\\\ \vdots\\\ \lambda x\_{D_W}-y\_{D_W} \end{pmatrix}, \\]

and checking whether the \\(\omega\times\omega\\) minors have gcd one.

107_layer_decision.md

This is correct for condition (E).

Indeed,

\\[ E\_\lambda(\mathcal T_W)=W \\]

is equivalent to

\\[ \operatorname{rank}M_W(\lambda)=\omega \quad\forall\lambda\in\mathbb C. \\]

Let

\\[ \Delta_1(\lambda),\ldots,\Delta_s(\lambda) \\]

be all maximal minors of \\(M_W(\lambda)\\). Then

\\[ \operatorname{rank}M_W(\lambda)<\omega \\]

if and only if all maximal minors vanish at \\(\lambda\\).

Over \\(\mathbb C\\), this is equivalent to

\\[ \gcd(\Delta_1,\ldots,\Delta_s)\ne1. \\]

Therefore,

\\[ \boxed{ E\_\lambda(\mathcal T_W)=W\ \forall\lambda\in\mathbb C \iff \gcd(\Delta_1,\ldots,\Delta_s)=1. } \\]

However, this test must be accompanied by the separate rank-completion test (R).

### **3.1 An improved computational formulation**

There is a useful simplification.

Instead of computing a basis of \\(\mathcal T_W\\), one can choose a basis matrix

\\[ Z_W\in\mathbb F^{D_W\times 2k} \\]

whose rows form a basis of \\(\mathcal T_W\\).

Write

\\[ Z_W=[X_W\mid Y_W], \\]

where

\\[ X_W,Y_W\in\mathbb F^{D_W\times k}. \\]

Then

\\[ M_W(\lambda)=\lambda X_W-Y_W. \\]

The two tests become:

**Rank completion**

\\[ \boxed{ \operatorname{rank} \begin{pmatrix} H_0\\\X_W \end{pmatrix} =\omega, } \\]

where \\(H_0\\) is the matrix of fixed first components expressed in a basis of \\(W\\).

**Spectral regularity**

\\[ \boxed{ \gcd\left( \text{all }\omega\times\omega\text{ minors of } \lambda X_W-Y_W \right)=1. } \\]

This is an especially clean exact-algebraic formulation.

### **3.2 Homogenization and the point at infinity**

There is another detail worth adding to the report.

The gcd test detects common finite roots in \\(\lambda\\). It does not automatically test the point at infinity of the projective parameter line.

The point at infinity corresponds to the leading coefficient \\(X_W\\). Thus, if one wants to formulate spectral regularity as a projective condition, homogenize:

\\[ M_W(s,t)=sX_W-tY_W. \\]

Then regularity in the affine chart \\(t=1\\) is

\\[ \operatorname{rank}(sX_W-Y_W)=\omega \quad\forall s\in\mathbb C. \\]

The additional projective point \\([1:0]\\) requires

\\[ \operatorname{rank}X_W=\omega. \\]

This is exactly the first-component rank-completion issue, after incorporating the fixed rows appropriately.

This observation suggests a useful unification:

> Rank completion and spectral regularity can be interpreted as the absence of common projective rank-deficiency points, including the point at infinity, for a suitably augmented pencil.

I would explore this formulation in the next report. It may simplify the algebraic-geometric treatment of the two conditions.

## **4. The analytic counterexample in II.1 is valid and important**

The report gives a subspace

\\[ \mathcal T=\ker\varphi\subseteq W\oplus W, \\]

where

\\[ \varphi(x,y)=\alpha(x)+\beta(y), \\]

with \\(\alpha\\) and \\(\beta\\) linearly independent.

It claims that

\\[ \dim\mathcal T=2\omega-1 \\]

and

\\[ E\_\lambda(\mathcal T)=W \qquad\forall\lambda. \\]

107_layer_decision.md

The argument is correct.

To see this more transparently, suppose that \\(E\_\lambda(\mathcal T)\ne W\\). Then there is a nonzero functional

\\[ \gamma\in W^\* \\]

that annihilates \\(E\_\lambda(\mathcal T)\\). Thus

\\[ \lambda\gamma(x)-\gamma(y)=0 \\]

for every \\((x,y)\in\ker\varphi\\).

The annihilator of \\(\ker\varphi\\) is the one-dimensional span of \\(\varphi\\). Hence

\\[ (\lambda\gamma,-\gamma)=c(\alpha,\beta) \\]

for some scalar \\(c\\).

Since \\(\gamma\ne0\\), we must have \\(c\ne0\\), and therefore

\\[ \alpha=\frac{\lambda}{c}\gamma, \qquad \beta=-\frac1c\gamma. \\]

This implies that \\(\alpha\\) and \\(\beta\\) are proportional, contradicting their assumed independence.

Therefore

\\[ E\_\lambda(\mathcal T)=W \\]

for every \\(\lambda\\).

This establishes a useful fact:

\\[ \boxed{ \dim\mathcal T=2\omega-1 \text{ can be sufficient for spectral regularity.} } \\]

The example is particularly valuable because it rules out a tempting but incorrect simplification based only on the dimension of \\(\mathcal T_W\\).

### **Recommendation**

Retain this example, but add the rank-completion qualification.

For example, if the first projection of \\(\mathcal T\\) is surjective, the example satisfies both conditions in the corrected proposition. If not, its spectral regularity alone does not guarantee feasibility.

This will make the example more useful as a reference case.

## **5. Q1: Can the row-count hypothesis be sharpened?**

This is the most promising question in the report.

The present condition

\\[ m\geq D_W:=\dim\mathcal T_W \\]

is sufficient because it allows the free rows to form a basis of the entire admissible pair space.

But it is not necessary.

The actual problem is to find an \\(m\\)-dimensional subspace

\\[ Q\leq\mathcal T_W \\]

such that

\\[ V_0+\pi_1(Q)=W \\]

and

\\[ E\_\lambda(Q)+E\_\lambda(T_0)=W \qquad\forall\lambda, \\]

where

\\[ T_0=\operatorname{span}\\{(h_i^0,g_i^0)\\}. \\]

Since \\(T_0\subseteq\mathcal T_W\\), this can be simplified to

\\[ E\_\lambda(T_0+Q)=W \qquad\forall\lambda. \\]

Thus the exact fixed-fibre problem is:

\\[ \boxed{ \begin{aligned} &\text{Find }Q\leq\mathcal T_W,\quad\dim Q\leq m,\\\ &V_0+\pi_1(Q)=W,\\\ &E\_\lambda(T_0+Q)=W\quad\forall\lambda\in\mathbb C. \end{aligned} } \\]

This is the natural formulation when \\(m\<D_W\\).

### **5.1 A necessary dimension bound**

Let

\\[ \rho_0=\dim V_0. \\]

Since each free row adds at most one dimension to the first-component span,

\\[ \boxed{m\geq\omega-\rho_0} \\]

is necessary.

This is the rank-completion lower bound.

There is also a spectral dimension lower bound. Since the fixed rows contribute at most \\(\dim T_0\\) independent directions in pair space, a crude necessary condition is

\\[ \dim(T_0+Q)\geq\omega, \\]

because \\(E\_\lambda(T_0+Q)\\) cannot have dimension greater than \\(\dim(T_0+Q)\\).

Thus

\\[ \dim T_0+m\geq\omega \\]

is necessary, although generally weak.

The two bounds address different requirements and should not be confused.

### **5.2 Why&#x20;**\\(m\geq\omega+1\\)**&#x20;is a plausible generic threshold**

Suppose, for a moment, that the fixed rows are absent and that

\\[ E\_\lambda:\mathcal T_W\to W \\]

is surjective for every \\(\lambda\\).

If we choose \\(m\\) generic elements of \\(\mathcal T_W\\), then for a fixed \\(\lambda\\), their images are generic vectors in \\(W\\).

For a fixed \\(\lambda\\), the condition that \\(m\\) vectors fail to span an \\(\omega\\)-dimensional space has codimension

\\[ m-\omega+1 \\]

when \\(m\geq\omega\\).

The parameter \\(\lambda\\) ranges over a one-dimensional space. A dimension-counting heuristic therefore suggests that

\\[ m-\omega+1>1, \\]

or

\\[ \boxed{m\geq\omega+1,} \\]

should be enough for generic simultaneous spanning.

This is a useful conjectural threshold, but it is not yet a proof in the present setting. One must carefully establish the codimension of the rank-deficiency incidence variety for the actual restricted linear family.

There are also two complications:

1. The fixed rows may already contribute some directions, reducing the required \\(m\\).
2. Rank completion at infinity requires the first components to span \\(W\\), not merely the evaluations at finite \\(\lambda\\).

### **5.3 My recommendation for Q1**

Study three row-count regimes separately:

| Regime                         | Meaning                                   | Status                        |
| ------------------------------ | ----------------------------------------- | ----------------------------- |
| \\(m<\omega-\rho_0\\)          | Insufficient first-component rank         | Infeasible                    |
| \\(\omega-\rho_0\leq m< D_W\\) | Partial selection from \\(\mathcal T_W\\) | Main unresolved case          |
| \\(m\geq D_W\\)                | Entire pair space can be represented      | Corrected proposition applies |

The middle regime is where the most interesting mathematics lies.

I would not try to prove a single optimal formula immediately. First establish a general generic upper bound and then study whether it is sharp.

## **6. Q2: Is the existential search over&#x20;**\\(W\\)**&#x20;polynomial-time decidable?**

This is the most important question for the complexity programme.

The report correctly identifies the remaining obstacle as the search over

\\[ W\in\operatorname{Gr}(\omega-d,k-d). \\]

107_layer_decision.md

For a fixed \\(W\\), the corrected criterion consists of:

1. a linear-algebraic rank-completion test;
2. a gcd test for the maximal minors of \\(\lambda X_W-Y_W\\).

Both are polynomial-time computations for explicitly represented rational data.

But the existential quantifier

\\[ \exists W\in\operatorname{Gr}(\omega-d,k-d) \\]

is not automatically polynomial-time decidable.

### **6.1 Why a Grassmannian parametrization does not remove the search**

On a standard affine chart, write

\\[ W=\operatorname{row}[I\_\omega\ X], \\]

where

\\[ X\in\mathbb F^{\omega\times(k-\omega)}. \\]

The compatibility condition \\(U\subseteq W\\) becomes a collection of polynomial equations in the entries of \\(X\\).

The space

\\[ \mathcal T_W=\mathcal S\cap(W\oplus W) \\]

is obtained as a kernel of a matrix whose entries are polynomial in \\(X\\).

On a constant-rank stratum, one can choose a rational basis for \\(\mathcal T_W\\). Then the maximal minors of the corresponding pencil are polynomial or rational functions of \\(X\\) and \\(\lambda\\).

The condition that their gcd in \\(\lambda\\) be one can be expressed through polynomial conditions on their coefficients, using resultants or subresultants.

Therefore, after stratification, the problem becomes an existential algebraic problem over the Grassmannian.

But that does not prove polynomial-time solvability. General existential polynomial systems can be computationally difficult.

### **6.2 What would be needed for a polynomial-time theorem?**

There are several possible ways to obtain a genuine polynomial-time result.

**Route A: prove that the active set is the whole compatibility Grassmannian or is empty.**

If the spectral and rank conditions were independent of \\(W\\), the search would disappear.

The report has not established this, and the earlier active-subspace analysis suggests that \\(\mathcal T_W\\) can vary with \\(W\\).

**Route B: prove that feasibility is determined by a finite collection of rank conditions on the original matrices.**

For example, if one could show that every feasible \\(W\\) exists whenever a certain fixed matrix has a prescribed rank, then the Grassmannian search might reduce to ordinary Gaussian elimination.

This would be a powerful theorem, but there is no proof yet.

**Route C: exploit special structure of the map&#x20;**\\(W\mapsto\mathcal T_W\\)**.**

The spaces

\\[ \mathcal T_W=\mathcal S\cap(W\oplus W) \\]

are not arbitrary kernels. They arise from the same subspace \\(W\\) appearing in both components.

There may be a useful structural theorem governing their dimensions and evaluation maps.

This is the route I would investigate first.

### **6.3 A useful reformulation of the search**

Define the active locus

\\[ \mathcal X\_{\mathrm{act}} = \left\\{ W\in\mathcal X\_{\mathrm{comp}}: \begin{array}{l} V_0+\pi_1(\mathcal T_W)=W,\\\ E\_\lambda(\mathcal T_W)=W\quad\forall\lambda \end{array} \right\\}. \\]

Under the sufficient row-count condition

\\[ m\geq\dim\mathcal T_W, \\]

the fixed-fibre feasibility problem is exactly the membership problem

\\[ W\in\mathcal X\_{\mathrm{act}}. \\]

The global layer problem is therefore

\\[ \boxed{ \mathcal X\_{\mathrm{act}}\ne\varnothing. } \\]

This is a much cleaner target for algebraic-geometric analysis than the original free-row formulation.

The next report should investigate:

- Is \\(\mathcal X\_{\mathrm{act}}\\) constructible?
- Is it open on constant-rank strata?
- Can its nonemptiness be tested by finitely many polynomial rank conditions?
- Are there special cases where it is automatically nonempty?

I would not claim polynomial-time decidability until one of these questions is resolved constructively.

## **7. Q3: How does fibrewise rigidity interact with the new criterion?**

The report asks whether fibrewise rigidity can be combined with the evaluation-space criterion.&#x20;

107_layer_decision.md



Yes, but the two statements describe different aspects of the same geometry.

Fibrewise rigidity says that once \\(W\\) is fixed, the feasible set of free-row choices is Zariski open in the appropriate parameter space, provided it is nonempty.

The new criterion identifies when that open set is nonempty under a sufficient row budget.

The correct relationship is:

\\[ \boxed{ \begin{array}{c} \text{Pair-space geometry determines whether a feasible choice exists};\\\ \text{fibrewise rigidity determines the algebraic structure of all such choices}. \end{array} } \\]

### **7.1 Codimension of&#x20;**\\(\mathcal T_W\\)

Let

\\[ c_W=2\omega-\dim\mathcal T_W. \\]

This is the codimension of the admissible pair space inside \\(W\oplus W\\).

If

\\[ c_W=0, \\]

then

\\[ \mathcal T_W=W\oplus W. \\]

The evaluation maps are automatically surjective, and the first projection is automatically surjective.

Thus, for sufficiently many free rows, the fibre is feasible.

If

\\[ c_W=1, \\]

the situation is more interesting. The analytic example in the report shows that the evaluation maps can still be surjective for all \\(\lambda\\).

If

\\[ c_W\geq2, \\]

surjectivity may or may not hold. The codimension alone cannot decide the question.

The reason is that codimension records the size of the pair-space restriction, but not its orientation relative to the two coordinate projections and the family of maps

\\[ (x,y)\mapsto\lambda x-y. \\]

### **7.2 A stronger invariant than codimension**

I recommend introducing the evaluation-defect function

\\[ \delta_W(\lambda) = \omega-\dim E\_\lambda(\mathcal T_W). \\]

Then spectral feasibility of the full pair space is exactly

\\[ \boxed{ \delta_W(\lambda)=0 \quad\forall\lambda\in\mathbb C. } \\]

Similarly define the first-projection defect

\\[ \delta_W^{(1)} = \omega-\dim\pi_1(\mathcal T_W+T_0). \\]

The corrected sufficient-row-count criterion becomes

\\[ \boxed{ \delta_W^{(1)}=0, \qquad \delta_W(\lambda)=0\quad\forall\lambda. } \\]

This is a better description than codimension alone.

One can then ask whether the defects are constrained by \\(c_W\\), or by the geometry of \\(\mathcal S\\).

For example:

- \\(c_W=0\\) forces both defects to vanish.
- \\(c_W=1\\) can still permit both defects to vanish.
- For larger \\(c_W\\), the answer depends on the orientation of the admissible subspace.

This is a promising direction for a structural classification.

## **8. Q4: Is the top-layer spectral condition sufficient?**

This remains unresolved, and the report is right to flag it.

In the top layer,

\\[ W=V=\mathbb F^{1\times k}, \qquad \mathcal T_V=\mathcal S. \\]

For a free row \\(r\\), the evaluation is

\\[ E\_\lambda(rN,rAN) = r(\lambda I-A)N. \\]

Therefore,

\\[ E\_\lambda(\mathcal S) = \operatorname{row}((\lambda I-A)N). \\]

The condition

\\[ E\_\lambda(\mathcal S)=V \qquad\forall\lambda \\]

is equivalent to

\\[ \operatorname{rank}((\lambda I-A)N)=k \qquad\forall\lambda. \\]

This is exactly the no-eigenvector condition.

So the condition is sufficient for the *entire admissible pair space* to have full evaluation rank at every \\(\lambda\\).

But the actual witness contains only \\(m\\) free rows, not necessarily a basis of all of \\(\mathcal S\\).

That distinction is essential.

### **8.1 A simple obstruction: a square pencil**

Suppose the total number of rows is

\\[ r_0+m=k. \\]

If the top layer is feasible, then \\(H\\) is a square invertible matrix. Hence

\\[ \det(\lambda H-H_A) \\]

is a polynomial of degree \\(k\\), with leading coefficient

\\[ \det H\ne0. \\]

By the fundamental theorem of algebra, this polynomial has a complex root.

At that root,

\\[ \operatorname{rank}(\lambda H-H_A)\<k, \\]

contradicting the top-layer condition.

Thus:

\\[ \boxed{r_0+m=k\implies\text{top layer infeasible}.} \\]

This obstruction holds even if

\\[ \operatorname{rank}((\lambda I-A)N)=k \quad\forall\lambda. \\]

It follows that the no-eigenvector condition cannot be a sufficient top-layer criterion without an appropriate row-count condition.

### **8.2 A more promising generic-completion question**

Suppose the no-eigenvector condition holds. Then

\\[ E\_\lambda(\mathcal S)=V \quad\forall\lambda. \\]

Can one choose a relatively small number of elements

\\[ s_1,\ldots,s_m\in\mathcal S \\]

such that

\\[ \operatorname{span}\\{E\_\lambda(s_1),\ldots,E\_\lambda(s_m), \text{fixed evaluations}\\}=V \\]

for every \\(\lambda\\)?

This is the same simultaneous generic-completion problem as in Q1, now with

\\[ \mathcal T_W=\mathcal S. \\]

A useful first theorem to attempt is:

**Proposed top-layer completion theorem.**

Assume

\\[ \operatorname{rank}((\lambda I-A)N)=k \quad\forall\lambda\in\mathbb C. \\]

Find an explicit bound \\(m\_\*(k,r_0,\operatorname{rank}L_0N)\\) such that for every \\(m\geq m\_\*\\), a choice of \\(m\\) free rows exists that makes the top-layer pencil regular and has \\(\operatorname{rank}H=k\\).

The report's current rank-completion threshold

\\[ m\geq k-\operatorname{rank}(L_0N) \\]

only guarantees that \\(H\\) can have rank \\(k\\). It does not guarantee that the pencil is regular for all \\(\lambda\\).

These should remain two separate bounds until a theorem connects them.

## **9. Q5: Does optimizing&#x20;**\\(N\\)**&#x20;change the problem?**

This question deserves a careful distinction.

In the stated problem,

\\[ K_0=\ker[C;CA] \\]

is determined by \\(A\\) and \\(C\\). Once \\(A,C\\) are fixed, its dimension \\(k\\) and any basis \\(N\\) are determined up to an invertible basis transformation.

Thus \\(N\\) is not an independent decision variable in the original formulation.

If \\(N'=NT\\), where \\(T\\) is invertible, then

\\[ H'=HT,\qquad H_A'=H_AT. \\]

Consequently,

\\[ \lambda H'-H_A'=(\lambda H-H_A)T, \\]

so the pencil rank is unchanged.

The compressed subspaces are merely expressed in a different coordinate system.

Therefore, optimizing the basis \\(N\\) itself cannot introduce additional combinatorial complexity.

There is, however, a different problem in which \\(K_0\\) is allowed to vary as part of the input or witness. That would be a different decision problem and would need a separate formulation.

For the current problem, the correct complexity question remains:

\\[ \exists W\in\operatorname{Gr}(\omega-d,k-d) \\]

subject to the corrected rank and spectral conditions.

I would not introduce an optimization over \\(N\\) into the present project. It risks changing the problem rather than resolving its complexity.

## **10. A more efficient research programme**

I recommend splitting the next stage into three mathematical projects rather than trying to settle all five questions at once.

### **Project A — Fixed-fibre characterization**

Highest priority

Establish the corrected theorem:

\\[ \begin{aligned} \text{fibre feasibility} \iff{}& V_0+\pi_1(\mathcal T_W)=W,\\\ & E\_\lambda(\mathcal T_W)=W \quad\forall\lambda, \end{aligned} \\]

under

\\[ m\geq\dim\mathcal T_W. \\]

Then investigate the sharp row budget for \\(m<\dim\mathcal T_W\\).

This project is finite-dimensional and self-contained. It should be completed before further complexity claims are made.

### **Project B — Generic row selection**

Study the following problem:

Given a finite-dimensional subspace

\\[ T\leq W\oplus W \\]

and fixed pairs \\(T_0\leq T\\), determine the smallest \\(m\\) for which there exist

\\[ Q\leq T,\qquad \dim Q\leq m, \\]

such that

\\[ \operatorname{span}\bigl(\pi_1(T_0+Q)\bigr)=W \\]

and

\\[ E\_\lambda(T_0+Q)=W \quad\forall\lambda. \\]

This is the correct abstract problem behind both the middle-layer and top-layer questions.

It may have an independent mathematical interest as a simultaneous spanning problem for a one-parameter family of linear maps.

### **Project C — Global Grassmannian search**

Once the fixed-fibre problem is understood, study

\\[ \mathcal X\_{\mathrm{act}} = \\{W\in\mathcal X\_{\mathrm{comp}}: W\text{ satisfies the fixed-fibre conditions}\\}. \\]

The main goals are:

1. determine its algebraic structure;
2. obtain a polynomial description;
3. identify cases where nonemptiness is easy to decide;
4. determine whether general nonemptiness is computationally hard.

This is where the original NP-hardness programme should eventually return.

## **11. Specific improvements to the report**

Here is what I would change before treating `107_layer_decision.md` as a reliable project milestone.

| Location               | Current issue                                                                                      | Recommended change                                                                   |
| ---------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| II.1, Proposition      | Omits \\(\operatorname{rank}H=\omega\\)                                                            | Add the first-projection rank-completion condition                                   |
| II.1, proof            | Basis of \\(\mathcal T_W\\) establishes pencil rank but not necessarily \\(\operatorname{rank}H\\) | Prove both conditions separately                                                     |
| II.1, gcd test         | Tests finite \\(\lambda\\) only                                                                    | Explicitly include the first-component rank test, or homogenize and discuss infinity |
| II.1, analytic example | Valid, but does not discuss rank completion                                                        | Add a sentence explaining that spectral surjectivity alone is insufficient           |
| II.2, top layer        | Necessity proved, sufficiency only experimentally verified                                         | State as an open conjecture with a precise row-count hypothesis                      |
| II.2, polynomial claim | Fixed-\\(W\\) gcd test does not settle the global search                                           | Restrict the claim to fixed \\(W\\) and explicitly leave global nonemptiness open    |
| Part III, Q1           | Good question but lacks exact formulation                                                          | Introduce the subspace \\(Q\leq\mathcal T_W\\)                                       |
| Part III, Q3           | Codimension may be too coarse                                                                      | Introduce evaluation-defect and first-projection-defect invariants                   |

The reliability table should also be revised. In particular, the current middle-layer proposition should not be labelled simply “proved” until the missing rank-completion condition is added.

## **12. Final verdict**

The report has made a genuine conceptual advance: it has identified the evaluation map

\\[ E\_\lambda:\mathcal T_W\to W \\]

as the right object for studying middle-layer spectral regularity.

That is the most important achievement of this iteration.

But the current formulation still conflates two different problems:

- Can the admissible pairs generate a pencil that is full rank at every finite \\(\lambda\\)?
- Can the admissible pairs also generate an \\(H\\) of rank exactly \\(\omega\\)?

The first is the evaluation-map problem. The second is the first-projection rank-completion problem. They must be treated together.

The top-layer analysis has the same underlying issue: pointwise surjectivity of the entire admissible row space does not automatically provide a sufficiently small finite selection of rows.

**My strongest recommendation is to make&#x20;**`108`**&#x20;a fixed-fibre and generic-completion report, not another global complexity report.** The key theorem should be the corrected proposition above, followed by a sharp or near-sharp bound on the number of free rows.

Once that theorem is established, the project will have a sound basis for returning to the global Grassmannian search and the NP-hardness question.

At this stage, the appropriate complexity conclusion is:

- the zero layer is understood under the stated witness definition;
- fixed-\\(W\\) middle-layer feasibility is understood when enough free rows are available, after adding the missing rank-completion condition;
- the top-layer necessity condition is understood, but sufficiency is open;
- the global search over compatible \\(W\\) is open.

Therefore, **the polynomial-time decidability of the full compressed-observer decision problem remains unproved, and the NP-hardness question remains open.**