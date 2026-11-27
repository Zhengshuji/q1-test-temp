# **Review of&#x20;**`99_linear_decoding_exclusion.md`

This report makes a substantial advance over the previous multiplication-gate analysis. The proposed exclusion theorem is promising, and—after a small but important correction to the Grassmannian decomposition—it appears to establish a genuine obstruction to **non-degenerate multiplication gates with affine-linear decoding**.

However, there are several statements that need correction before I would regard the report as mathematically airtight. The most important issues are:

1. The equality in II.1 between the entire rank stratum and the union of the \\(M_W\\) is false as written.
2. The claim that (5a) is automatic on each \\(M_W\\) needs the fixed-row compatibility assumption.
3. The two-point counterexample is convincing, but its closure argument should use the closed determinantal variety \\(\\{\operatorname{rank}H\leq\omega\\}\\), not the exact-rank stratum.
4. The exclusion theorem proves a stronger global disjunction than the report explicitly states, but its interpretation as a no-multiplication theorem needs a precise non-degeneracy condition.
5. The conclusion about affine-rank-minimisation reductions is broader than what the theorem establishes.

I will go through the arguments in order.

## **1. II.1: the Grassmannian decomposition needs correction**

This is the first mathematical error to fix.

The report defines

\\[ M_W=\\{R:h_i\in W,\ g_i\in W\\}, \\]

where \\(W\\) has dimension \\(\omega\\) and contains \\(W_0=\operatorname{row}H_0\\).

It then claims

\\[ \\{R:\operatorname{rank}H=\omega\\} = \bigcup\_{W\in\operatorname{Gr}(\omega,k)}M_W. \tag{A} \\]

This equality is false.

The condition

\\[ \operatorname{rank}H=\omega \\]

only constrains the \\(h_i\\)'s, because \\(H\\) is constructed from the \\(h_i\\)'s and the fixed \\(H_0\\). It does not imply that the \\(g_i\\)'s lie in the row space of \\(H\\).

For example, take \\(W_0=0\\), \\(m=1\\), and \\(\omega=1\\). Choose a pair

\\[ h\in W,\qquad g\notin W. \\]

Then \\(\operatorname{rank}H=1\\), but the corresponding parameter does not belong to \\(M_W\\), nor to any \\(M\_{W'}\\) with \\(W'=\operatorname{row}H\\).

The missing condition is precisely the first feasibility condition (5a).

### **1.1 The correct decomposition**

Define

\\[ \mathcal F\_\omega = \\{R:R\text{ is feasible and }\operatorname{rank}H=\omega\\}. \\]

Assume the fixed-row compatibility condition

\\[ \operatorname{row}H\_{A,0}\subseteq W_0. \tag{C} \\]

Then the correct statement is

\\[ \boxed{ \mathcal F\_\omega = \bigcup\_{\substack{W\in\operatorname{Gr}(\omega,k)\\\W_0\subseteq W}} \left[ M_W\cap\\{\operatorname{rank}H=\omega\\} \cap\\{(5b)\\} \right]. } \tag{B} \\]

Here is the proof.

**Forward inclusion.** Let \\(R\in\mathcal F\_\omega\\), and put

\\[ W=\operatorname{row}H. \\]

Then \\(\dim W=\omega\\), and \\(W_0\subseteq W\\). Every free \\(h_i\\) belongs to \\(W\\), since it is a row of \\(H\\). By (5a), every free \\(g_i\\) also belongs to \\(W\\), since it is a row of \\(H_A\\). Thus \\(R\in M_W\\).

**Reverse inclusion.** Suppose

\\[ R\in M_W,\qquad \operatorname{rank}H=\omega. \\]

By definition of \\(M_W\\), every row of \\(H\\) belongs to \\(W\\). Therefore

\\[ W_0\subseteq\operatorname{row}H\subseteq W. \\]

Both \\(\operatorname{row}H\\) and \\(W\\) have dimension \\(\omega\\), so

\\[ \operatorname{row}H=W. \\]

All free \\(g_i\\)'s belong to \\(W\\), and (C) ensures that the fixed rows of \\(H_A\\) also belong to \\(W\\). Hence

\\[ \operatorname{row}H_A\subseteq W=\operatorname{row}H, \\]

which is (5a). Adding (5b) gives feasibility.

This proves (B).

### **1.2 Does this correction destroy the open-set argument?**

No. In fact, it preserves the central argument almost unchanged.

For a fixed \\(W\\), the set \\(M_W\\) is a linear subspace of the free-parameter space. Since every \\(h_i\\) belongs to \\(W\\), we have

\\[ \operatorname{rank}H\leq\omega \qquad\text{throughout }M_W. \\]

Consequently,

\\[ \\{R\in M_W:\operatorname{rank}H=\omega\\} \\]

is Zariski open in \\(M_W\\): it is the complement of the determinantal closed set

\\[ \\{R\in M_W:\operatorname{rank}H\leq\omega-1\\}. \\]

On this rank-exact open subset, the bad locus for (5b) is relatively closed by (B1). Its complement is relatively open.

Therefore, under (C),

\\[ \boxed{\mathcal F\cap M_W \text{ is Zariski open in }M_W.} \\]

This is the key structural statement. It remains valid after correcting the erroneous equality (A).

**Recommendation:** replace the first displayed equality in II.1 with (B), and state fixed-row compatibility before claiming automatic validity of (5a).

## **2. II.2: the one-row result is correct, with a compatibility qualification**

The one-row argument is sound.

Let

\\[ r=\operatorname{rank}H_0. \\]

### **Case 1:&#x20;**\\(\omega=r\\)

Since

\\[ W_0\subseteq\operatorname{row}H \\]

and both spaces have dimension \\(r\\),

\\[ \operatorname{row}H=W_0. \\]

Thus feasibility requires

\\[ h,g\in W_0 \\]

for the single free row, together with fixed-row compatibility and the spectral condition.

The feasible set is therefore an open subset of the linear space

\\[ W_0\times W_0 \\]

pulled back through the row-pair map.

### **Case 2:&#x20;**\\(\omega>r\\)

There is one new independent \\(h\\)-direction, so

\\[ W=W_0+\langle h\rangle,\qquad h\notin W_0. \\]

By (5a),

\\[ g=\alpha h+w,\qquad w\in W_0. \\]

At \\(\lambda=\alpha\\),

\\[ \alpha h-g=-w\in W_0. \\]

The fixed pencil rows also belong to \\(W_0\\) under compatibility, and hence the pencil at \\(\alpha\\) has rank at most \\(r\\). But

\\[ \operatorname{rank}H=r+1. \\]

This contradicts (5b).

Therefore no feasible witness exists in this rank stratum.

The report's conclusion is correct. I would simply state explicitly that the fixed-row compatibility condition is assumed in both cases. Otherwise the \\(\omega=r\\) description may incorrectly suggest that feasibility is determined solely by the free pair.

## **3. II.2: the two-row counterexample is important**

The proposed example is a valuable counterexample to the candidate linearity principle.

The matrices are

\\[ H_p= \begin{pmatrix} 1&0&0\\\ -1&-1&-1\\\ -1&-1&-1 \end{pmatrix}, \qquad H_q= \begin{pmatrix} 1&0&0\\\ -1&-1&0\\\ -1&0&0 \end{pmatrix}. \\]

Both have rank two, and both contain the same fixed first row. Their row spaces differ.

Their midpoint is

\\[ H_m=\frac{H_p+H_q}{2} = \begin{pmatrix} 1&0&0\\\ -1&-1&-\frac12\\\ -1&-\frac12&-\frac12 \end{pmatrix}. \\]

A direct calculation gives

\\[ \det H_m=\frac14\neq0. \\]

Thus

\\[ \operatorname{rank}H_m=3. \\]

### **3.1 The closure argument needs one correction**

The report says that if the Zariski closure were a linear space \\(L\\), then

\\[ L\subseteq\\{\operatorname{rank}H=\omega\\} \\]

because the exact-rank stratum is closed.

That last assertion is incorrect: an exact-rank stratum is generally locally closed, not closed.

The correct argument is even simpler.

Every feasible point has rank \\(\omega=2\\), so its Zariski closure is contained in the closed determinantal variety

\\[ D_2=\\{H:\operatorname{rank}H\leq2\\}. \\]

If the closure were a linear space \\(L\\), then \\(H_p,H_q\in L\\), and therefore their midpoint would belong to \\(L\\). But

\\[ H_m\notin D_2. \\]

This contradicts \\(L\subseteq D_2\\).

Hence the Zariski closure of the feasible set cannot be a linear space.

This argument does not need irreducibility.

### **3.2 A reproducibility issue**

The report says both points are exactly feasible, with gcd of maximal minors equal to one. But it only displays \\(H_p,H_q\\), not their corresponding \\(H_A\\) matrices or the row-pair map \\(\mathcal T\\).

That means the rank calculations and midpoint obstruction are independently verifiable from the displayed data, but the feasibility certificates are not reproducible from the report alone.

I recommend adding, for each point:

- the corresponding \\(H_A\\);
- the relevant \\(\mathcal T\\), or an explicit construction of \\(A,C,N\\) realizing the pair;
- the maximal minors of \\(\lambda H-H_A\\), or a Bézout identity certifying their gcd is one.

The two-point example is potentially an important structural result. It deserves a fully checkable certificate.

## **4. II.3: the exclusion theorem is essentially correct**

Core argument valid after the II.1 correction

This is the strongest result in the report.

Fix \\(W\\) such that

\\[ \mathcal F\cap M_W\neq\varnothing. \\]

By the corrected II.1, under fixed-row compatibility,

\\[ \mathcal F\cap M_W \\]

is a nonempty Zariski-open subset of the linear space \\(M_W\\).

Since \\(M_W\\) is an affine space, it is irreducible. Thus

\\[ \overline{\mathcal F\cap M_W}^{\\,\mathrm{Zar}}=M_W. \\]

If

\\[ z=xy \\]

holds at every feasible point, then the polynomial

\\[ f=z-xy \\]

vanishes on \\(\mathcal F\cap M_W\\). It must therefore vanish identically on \\(M_W\\).

Now restrict the affine-linear decoding functions to \\(M_W\\). Write

\\[ x|\_{M_W}=a+\ell,\qquad y|\_{M_W}=b+m,\qquad z|\_{M_W}=c+q, \\]

where \\(\ell,m,q\\) are linear forms on \\(M_W\\).

The identity

\\[ c+q=(a+\ell)(b+m) \\]

holds as a polynomial identity.

Its homogeneous degree-two part is

\\[ \ell m=0. \\]

The coordinate ring of a linear space is a polynomial ring over a field, hence an integral domain. Therefore

\\[ \boxed{\ell=0\quad\text{or}\quad m=0.} \\]

Equivalently,

\\[ \boxed{ x|\_{M_W}\text{ is constant, or } y|\_{M_W}\text{ is constant}. } \\]

This proof is correct.

### **4.1 A useful strengthening: the disjunction is global**

The report currently states the conclusion separately for every \\(W\\). There is a stronger consequence that should be made explicit.

Every \\(M_W\\) is a **linear subspace**, not merely an affine subspace. In particular, it contains the zero free-row parameter.

Suppose

\\[ x(R)=a+\ell_x(R) \\]

is the global affine-linear decoding function. If \\(x\\) is constant on \\(M_W\\), that constant must be

\\[ x(0)=a. \\]

It cannot be a different constant for different \\(W\\).

Similarly, if \\(y\\) is constant on \\(M_W\\), its constant value must be \\(y(0)\\).

Therefore, for every feasible \\(R\\), choose a \\(W\\) with \\(R\in M_W\\). The theorem implies

\\[ \boxed{ x(R)=x(0) \quad\text{or}\quad y(R)=y(0). } \\]

Thus the entire feasible set satisfies the global disjunction

\\[ \boxed{ \mathcal F \subseteq \\{x=x(0)\\}\cup\\{y=y(0)\\}. } \tag{D} \\]

This is stronger than simply saying that one factor is constant on each Grassmannian piece.

It has a very useful interpretation: **the feasible set cannot project onto a Zariski-dense subset of the&#x20;**\\((x,y)\\)**-plane.** Its projection is contained in the union of one vertical and one horizontal affine line.

Consequently, if a multiplication gate is required to permit \\(x\\) and \\(y\\) to vary independently over a nonempty open subset of the scalar plane, such a gate is impossible.

I would add (D) as a corollary of Theorem II.3.

## **5. The definition of “expresses multiplication” should be strengthened**

The report defines a gadget as expressing multiplication whenever

\\[ z=xy \\]

at every feasible point.

This is too weak to distinguish a genuine multiplication gate from a degenerate one.

For example, the conditions

\\[ x=0,\qquad z=0 \\]

make \\(z=xy\\) true for every value of \\(y\\), but no multiplication operation has actually been encoded.

The exclusion theorem does not rule out this kind of vacuous identity. It rules out the stronger and more useful notion of multiplication in which the two inputs can vary independently.

I recommend the following definition.

**Definition (non-degenerate multiplication gate).** A gadget with decoded variables \\((x,y,z)\\) expresses non-degenerate multiplication if:

1. \\(z=xy\\) at every feasible point; and
2. the projection of its feasible set onto the \\((x,y)\\)-coordinates is Zariski dense in \\(\mathbb A^2\\).

Under this definition, the global disjunction (D) immediately gives:

**Corollary (no affine-linear non-degenerate multiplication gate).** Under the hypotheses of Theorem II.3, no non-degenerate multiplication gate with affine-linear decoding exists.

This is a strong, clean, and mathematically precise result.

It also clarifies the scope: the theorem does not forbid every possible gadget whose feasible points happen to satisfy \\(z=xy\\). It forbids one that genuinely represents multiplication with independently variable inputs.

## **6. Q2: nonlinear decoding and degree obstructions**

The report is right that the final step of the affine-linear proof does not extend automatically to nonlinear decoding.

Suppose \\(x,y,z\\) are polynomial functions on the free parameter space. The density argument still gives

\\[ z|\_{M_W}=x|\_{M_W}\\,y|\_{M_W} \\]

as an identity in the coordinate ring of \\(M_W\\).

But the integral-domain argument no longer implies that either factor is constant.

For example, on a two-dimensional affine space with coordinates \\(u,v\\), the polynomial functions

\\[ x=u,\qquad y=v,\qquad z=uv \\]

satisfy the multiplication identity identically. There is no contradiction.

### **6.1 What degree information can be extracted?**

Let

\\[ a=\deg(x|\_{M_W}),\qquad b=\deg(y|\_{M_W}). \\]

If neither restricted polynomial is zero, then

\\[ \deg\big((x|\_{M_W})(y|\_{M_W})\big)=a+b. \\]

Since this equals \\(z|\_{M_W}\\),

\\[ \boxed{\deg(z|\_{M_W})=a+b.} \\]

Thus if all three decoding functions have degree at most \\(d\\), we obtain

\\[ a+b\leq d. \\]

This gives a modest degree restriction, but it does not rule out nonlinear decoding for \\(d\geq2\\). For instance, linear inputs and a quadratic output are entirely compatible with the bound.

There is one useful special case:

If all three restricted decoding functions are required to have degree at most one, then

\\[ a+b\leq1. \\]

At least one of \\(a,b\\) must be zero, recovering the affine-linear exclusion.

For general \\(d\\), however, this degree argument does not yield a no-go theorem.

### **6.2 The determinantal ideal argument needs a correction**

The report says that

\\[ \bigcup_W M_W \\]

is the determinantal variety

\\[ \\{\operatorname{rank}H\leq\omega\\}. \\]

This is not generally correct. The spaces \\(M_W\\) constrain both \\(h_i\\) and \\(g_i\\). Their union is more naturally described by the condition that the combined collection of fixed and free \\(h\\)- and \\(g\\)-rows spans a space of dimension at most \\(\omega\\).

In matrix language, under compatible fixed-row data, this is a condition of the form

\\[ \operatorname{rank} \begin{bmatrix} H\\\ H_A \end{bmatrix} \leq\omega, \\]

not merely \\(\operatorname{rank}H\leq\omega\\).

On the feasible set, (5a) already ensures that these two row spaces coincide, but that does not make the two ambient determinantal conditions equivalent away from feasibility.

For nonlinear decoding, the correct algebraic object to study is therefore the ideal of the relevant union of the \\(M_W\\)'s—or, more precisely, of the subfamily of \\(M_W\\)'s that actually meets the feasible locus.

This is a potentially interesting direction, but I do not see a general factorization theorem that would force multiplication degeneracy for arbitrary polynomial decoding.

## **7. Q3: how far does the exclusion theorem rule out hardness reductions?**

The report's conclusion is too strong in its current wording.

It says that the affine-rank-minimisation translation is excluded, and suggests that a reduction must abandon the common row-space discipline or use nonlinear decoding.

The first part needs qualification.

The theorem establishes an obstruction to **non-degenerate multiplication gates with affine-linear decoding**. It does not establish that every reduction from affine rank minimisation must implement multiplication gates.

A reduction could conceivably encode a rank condition directly, without implementing an arithmetic circuit whose gates include \\(z=xy\\).

In particular, the fact that entries of an affine matrix are affine-linear functions of the reduction variables does not, by itself, imply that every rank constraint must be implemented through multiplication gadgets. Rank conditions are determinantal conditions and might be represented by other structural mechanisms.

I would therefore replace the conclusion with:

> The theorem rules out a broad class of arithmetic-gadget reductions in which scalar multiplication is represented by a non-degenerate multiplication gate whose decoded variables are affine-linear in the free-row parameters. It does not rule out reductions that encode rank constraints directly or use a different representation of the source problem.

This is a meaningful limitation on the original hardness strategy without claiming a universal impossibility result.

### **My view of the remaining options**

- **Abandoning the common row-space discipline:** This directly escapes the hypotheses of the theorem, but it changes the architecture and may no longer correspond to the original observer problem.
- **Nonlinear decoding:** This is mathematically possible in principle, but it risks making the reduction difficult to verify and the encoded variables difficult to interpret.
- **A reduction without multiplication gates:** This is the most promising direction if the objective is to prove hardness for the original model without changing its definition.

I would prioritize the third option.

## **8. Q5: does the Grassmannian decomposition improve the algorithm?**

Potentially yes, but it is not yet an algorithmic improvement by itself.

The corrected decomposition gives

\\[ \mathcal F\_\omega = \bigcup\_{W\in\operatorname{Gr}(\omega,k),\\,W_0\subseteq W} \mathcal F\_{\omega,W}, \\]

where

\\[ \mathcal F\_{\omega,W} = \mathcal F\cap M_W \\]

is a Zariski-open subset of the linear space \\(M_W\\).

This leads to an important observation:

**For a fixed&#x20;**\\(W\\)**, feasibility is a generic spectral-feasibility problem on a linear parameter space.**

More precisely, suppose the rank-\\(\omega\\) subset of \\(M_W\\) is nonempty. Then it is a nonempty open subset. The bad spectral locus is relatively closed there. Thus

\\[ \mathcal F\_{\omega,W}\neq\varnothing \\]

if and only if the generic point of that rank-\\(\omega\\) part of \\(M_W\\) is spectrally good.

This suggests using the same generic-gcd machinery developed in Paper I, but now on the parameter space \\(M_W\\).

### **8.1 What the resulting algorithm would need to do**

A possible algorithmic route is:

1. Enumerate the possible ranks \\(\omega\\), subject to\
   \\[\
   \operatorname{rank}H_0\leq\omega\leq\dim(AK_0).\
   \\]
2. Parameterize the Grassmannian of \\(\omega\\)-dimensional subspaces \\(W\\) containing \\(W_0\\), using finitely many standard affine charts.
3. For each chart, express the constraints\
   \\[\
   (h_i,g_i)\in\mathcal T\cap(W\times W)\
   \\]\
   as linear constraints on the free rows.
4. Determine whether the rank-\\(\omega\\) subset of the resulting \\(M_W\\) is nonempty.
5. Compute the generic maximal-minor gcd of the pencil over the function field of the corresponding parameter space.
6. Determine whether some \\(W\\) produces a nonempty spectral-good fibre.

There is a serious difficulty in Step 6: \\(W\\) itself is quantified over an algebraic variety. A generic-gcd test for a generic \\(W\\) is not enough. A special \\(W\\) may be feasible even when generic \\(W\\)'s are not.

So the Grassmannian decomposition does not immediately give a faster decision algorithm. It gives a new **parameterized algebraic-geometric formulation** of the decision problem.

It may eventually support a stratified elimination algorithm, but that would need a separate complexity analysis.

### **8.2 One particularly useful consequence**

The decomposition also provides a way to organize computational experiments.

Instead of sampling arbitrary free-row matrices \\(R\\), one can:

- sample \\(W\\);
- construct the corresponding linear space \\(M_W\\);
- test whether the rank-\\(\omega\\) part is nonempty;
- test generic spectral feasibility on that fibre.

This separates two sources of difficulty:

- the geometry of the possible compressed row spaces \\(W\\);
- the spectral feasibility inside each fixed row-space fibre.

That separation may make the computational exploration much more informative.

## **9. Recommended revisions to the report**

I would make the following changes before treating this as a settled result.

| Section  | Required revision                                                                                                     |
| -------- | --------------------------------------------------------------------------------------------------------------------- |
| II.1     | Replace the equality for the entire rank stratum with the corrected decomposition of the feasible rank stratum        |
| II.1     | State fixed-row compatibility before claiming (5a) is automatic                                                       |
| II.2     | Replace the exact-rank closedness argument with the closed determinantal variety \\(\operatorname{rank}H\leq\omega\\) |
| II.2     | Add the full \\(H_A\\) and Bézout certificates for the two feasible points                                            |
| II.3     | Add the global disjunction \\(x=x(0)\\) or \\(y=y(0)\\) on the feasible set                                           |
| II.3     | Define non-degenerate multiplication by requiring Zariski-dense projection onto the input plane                       |
| II.4     | Correct the description of \\(\bigcup_W M_W\\)                                                                        |
| Part III | Distinguish affine-linear gate exclusion from general hardness-reduction impossibility                                |
| Q5       | Present the Grassmannian approach as a possible algorithmic framework, not yet as an improved algorithm               |

## **10. Overall assessment and next research step**

Core theorem salvageable and strong

The central exclusion argument is sound after correcting II.1. More importantly, it yields a global consequence:

\\[ \boxed{ \mathcal F\subseteq \\{x=x(0)\\}\cup\\{y=y(0)\\}. } \\]

This means that affine-linear decoding cannot produce a multiplication gate whose two inputs vary independently on a Zariski-dense subset of the input plane.

That is a strong and useful theorem. It is more precise than the earlier pinned-instance result because it applies across all the Grassmannian pieces, not just a single pinned row space.

However, it does not prove that the original observer feasibility problem is incapable of being NP-hard. It rules out one important family of reduction architectures.

### **The next mathematical question I would prioritize**

I recommend investigating the following:

**Question: Can the union of feasible Grassmannian fibres have a Zariski-dense projection onto two affine-linear decoded variables, even though each individual fibre has one input fixed?**

The global disjunction derived above says no, under the present hypotheses. This is the decisive reason the affine-linear multiplication-gate approach fails.

The next challenge is to determine whether a direct reduction can exploit the nonlinear geometry of the Grassmannian family without relying on scalar multiplication gates.

In parallel, I would investigate whether the family of feasible fibres admits an effective algebraic description that can be used for a decision algorithm. That may be a more fruitful route for the complexity programme than trying to force a multiplication gate into an architecture whose geometry strongly resists it.

**Final verdict:** The report contains a genuinely strong exclusion theorem, but its II.1 decomposition and several broad conclusions need correction. Once revised, it should be retained as a significant negative result for affine-linear arithmetic-gadget reductions—not as a universal no-go theorem for NP-hardness of functional-observer feasibility.

99_linear_decoding_exclusion.md