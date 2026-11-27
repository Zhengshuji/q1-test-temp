# **Research review of Report 108: the&#x20;**\\(c=2\\)**&#x20;layer**

## **1. Overall assessment**

Report 108 makes substantial progress over Report 107. In particular, it corrects the fixed-kernel fibre, separates the unrestricted and \\(K_0\\)-split problems, gives a concrete Grassmannian description of the split fibre, and identifies a potentially important non-monotonicity phenomenon.

My overall assessment is:



Strong mathematical progress

&#x20;The fixed-\\(D\\) fibre in II.1 is largely correct, and the \\(K_0\\)-split decomposition is a useful structural result.





Several points need correction

&#x20;The invariant-two-plane classification in II.2 is incomplete as stated; the prescribed-row compatibility condition is missing from the split fibre; and the complexity conclusion in II.5 does not follow from the stated dimension count.





Counterexample needs a complete certificate

&#x20;The non-monotonicity example is interesting and may be correct, but the \\(c=1\\) parameterization appears to omit a projective direction, and the report does not provide enough raw data to independently verify both sides.



The most important recommendation is to **stabilize the&#x20;**\\(c=2\\)**&#x20;geometry before making a general complexity claim**. The project now has a promising structural framework, but several logical steps between the geometric parameterization and the decision algorithm still need to be established.

# **Part I. The fixed-direction fibre**

## **2. Unrestricted fibre: II.1(a) is correct**

The report defines

\\[ U_D=D+AD \\]

and

\\[ \mathcal F_D= \left\\{ V\in\operatorname{Gr}(q,U_D^\perp): V_0\subseteq V,\quad K_0\cap V^\perp=D \right\\}. \\]

It then asserts that exactness of the compressed kernel is equivalent to

\\[ \boxed{K_0\cap(D+AD)=D.} \tag{1} \\]

This is correct, provided the candidate \\(D\\) is already a \\(c\\)-dimensional subspace of \\(K_0\\).

### **Proof**

Suppose \\(V\\) satisfies (5a) and

\\[ D=K_0\cap V^\perp. \\]

For every \\(d\in D\\), (5a) implies

\\[ Ad\perp V. \\]

Since also \\(d\perp V\\), we have

\\[ D+AD\subseteq V^\perp. \\]

Consequently,

\\[ K_0\cap(D+AD)\subseteq K_0\cap V^\perp=D. \\]

The reverse inclusion follows from \\(D\subseteq D+AD\\), so (1) is necessary.

Conversely, suppose

\\[ K_0\cap(D+AD)=D \\]

and choose \\(V\\) such that

\\[ V_0\subseteq V\subseteq(D+AD)^\perp. \\]

Then

\\[ D\subseteq K_0\cap V^\perp. \\]

But

\\[ K_0\cap V^\perp \subseteq K_0\cap(D+AD)=D. \\]

Therefore

\\[ K_0\cap V^\perp=D. \\]

This proves the equivalence.

### **One refinement to the report**

The report says that (1), together with

\\[ V_0\subseteq U_D^\perp,\qquad \dim U_D\le n-q, \\]

is sufficient. This is correct for the existence of a \\(q\\)-dimensional ambient row space \\(V\\) containing \\(V_0\\), provided \\(\dim V_0\le q\\).

However, the actual fibre also has to be considered alongside the remaining condition (5b). The exact-kernel criterion alone does not establish pencil feasibility.

I suggest explicitly separating the two stages:

1. **Structural fibre:** all \\(V\\) satisfying the prescribed-row, containment, and exact-kernel conditions.
2. **Pencil-feasible fibre:** the subset of the structural fibre satisfying (5b).

That distinction will make later algebraic-geometric arguments much clearer.

108_c2_layer.md

## **3. Split fibre: the decomposition is correct, but one condition is missing**

This is the most important technical correction to II.1(b).

Let

\\[ X=K_0\oplus K_0^\perp, \qquad D=K_0\cap V^\perp, \\]

and assume \\(V\\) is \\(K_0\\)-split:

\\[ V=(V\cap K_0)\oplus(V\cap K_0^\perp). \\]

Then

\\[ V\cap K_0=D^{\perp\_{K_0}}. \\]

Writing

\\[ W=V\cap K_0^\perp, \\]

we obtain

\\[ \boxed{ V=D^{\perp\_{K_0}}\oplus W. } \tag{2} \\]

This part is correct.

Now suppose \\(M(D)\subseteq D\\), and write

\\[ A|\_{K_0}=M+A\_{21}, \qquad A\_{21}:K_0\to K_0^\perp. \\]

For \\(d\in D\\) and \\(v=x+w\\), with

\\[ x\in D^{\perp\_{K_0}},\qquad w\in W, \\]

we have

\\[ \langle Ad,v\rangle = \langle Md,x\rangle + \langle A\_{21}d,w\rangle. \\]

Since \\(Md\in D\\), the first term vanishes. Thus

\\[ AD\perp V \iff A\_{21}D\perp W. \\]

Consequently,

\\[ W\subseteq T_D:=K_0^\perp\cap(A\_{21}D)^\perp. \\]

This proves the main geometric decomposition.

### **The missing prescribed-row compatibility**

The report writes

\\[ W_0=P\_{K_0^\perp}(V_0) \\]

and then gives the fibre

\\[ \operatorname{Gr}(t-w_0,T_D/W_0). \\]

But \\(V_0\subseteq V\\) requires **two** independent conditions:

\\[ \boxed{ P\_{K_0}(V_0)\subseteq D^{\perp\_{K_0}}, \qquad W_0\subseteq W. } \tag{3} \\]

The second is represented in the Grassmannian quotient. The first is not.

This means the base of the relative Grassmann bundle must be restricted to

\\[ \boxed{ \mathcal B\_{\mathrm{pres}} = \left\\{ D\in\mathcal I_c(M): P\_{K_0}(V_0)\subseteq D^{\perp\_{K_0}} \right\\}. } \tag{4} \\]

Equivalently,

\\[ D\perp P\_{K_0}(V_0). \\]

Only over this restricted base is the fibre formula in the report correct.

### **Corrected theorem**

Let

\\[ W_0=P\_{K_0^\perp}(V_0),\qquad w_0=\dim W_0, \\]

and define

\\[ T_D=K_0^\perp\cap(A\_{21}D)^\perp. \\]

For a \\(K_0\\)-split design with \\(M(D)\subseteq D\\), the prescribed-row-compatible fibre is

\\[ \boxed{ \mathcal F_D^{\mathrm{split}} \cong \operatorname{Gr} \left(t-w_0,\ T_D/W_0\right) } \tag{5} \\]

**provided**

\\[ P\_{K_0}(V_0)\subseteq D^{\perp\_{K_0}}, \qquad W_0\subseteq T_D. \\]

Its nonemptiness conditions are

\\[ \boxed{ w_0\le t\le(n-k)-r(D), } \tag{6} \\]

where

\\[ r(D)=\operatorname{rank}(A\_{21}|\_D). \\]

Its dimension is

\\[ \boxed{ (t-w_0)\bigl((n-k)-r(D)-t\bigr). } \tag{7} \\]

The dimension calculation is correct.

### **Why this matters**

This is more than a technicality. The prescribed-row condition can eliminate entire components of the invariant-subspace base.

For example, if \\(P\_{K_0}(V_0)\\) contains a vector that has nonzero inner product with every vector in some invariant subspace \\(D\\), that \\(D\\) cannot support a prescribed-row-compatible split design, regardless of the available \\(W\\)-fibre.

The base geometry must therefore incorporate the prescribed rows before the pencil condition is analyzed.

108_c2_layer.md

# **Part II. The invariant two-plane base**

## **4. II.2 is not yet a complete classification**

The report correctly identifies the central object:

\\[ \mathcal I_2(M) = \\{D\in\operatorname{Gr}(2,K_0):M(D)\subseteq D\\}. \\]

It also correctly observes that repeated eigenvalues and repeated irreducible quadratic factors can produce positive-dimensional families.

However, the listed classification is incomplete for general Jordan structures.

The statement

> for a Jordan block only the first two vectors of a chain (isolated)

is correct for a **single Jordan block**, with a suitable convention for the ordering of the chain. It is not a general classification of invariant two-planes in a primary component containing several Jordan blocks.

### **4.1 Why multiple Jordan blocks cause additional families**

Consider

\\[ M=\lambda I+N, \qquad N= \begin{pmatrix} 0&1&0&0\\\ 0&0&0&0\\\ 0&0&0&1\\\ 0&0&0&0 \end{pmatrix}. \\]

This is the direct sum of two Jordan blocks of size two.

The eigenspace is

\\[ E\_\lambda=\ker N =\operatorname{span}(e_1,e_3). \\]

Every two-dimensional subspace of \\(E\_\lambda\\) is invariant. In this particular example \\(E\_\lambda\\) itself is two-dimensional, so it gives one plane.

But invariant planes can also be generated using generalized eigenvectors. For example,

\\[ D_a=\operatorname{span}(e_1,e_2+a e_4) \\]

is not invariant for arbitrary \\(a\\), since

\\[ N(e_2+a e_4)=a e_3. \\]

It becomes invariant only if \\(a=0\\) or if the second vector is adjusted to include the appropriate eigenvector component.

The point is that for multiple Jordan blocks, the classification involves the relative positions of the eigenvectors and generalized eigenvectors, not just the first two vectors of each chain.

More generally, invariant subspaces of a nilpotent operator are submodules over \\(\mathbb R[x]\\). Their classification depends on the Jordan partition and is richer than a list of isolated chain prefixes.

### **4.2 A safer formulation**

I recommend replacing the current three-item list with the following theorem-level structure.

Decompose \\(K_0\\) into real primary components:

\\[ K_0=\bigoplus\_{\lambda\in\mathbb R}K\_\lambda \oplus \bigoplus\_{\\{\mu,\bar\mu\\}}K\_{\\{\mu,\bar\mu\\}}. \\]

Every \\(M\\)-invariant subspace decomposes across these primary components. Therefore, an invariant two-plane \\(D\\) is one of:

1. A two-dimensional invariant subspace contained in one real primary component.
2. A direct sum of invariant lines from two distinct real primary components.
3. A real invariant plane associated with an irreducible quadratic primary component.

This is a correct structural classification, but the first and third cases still require a more detailed description in terms of Jordan structure and geometric multiplicity.

### **4.3 The repeated irreducible quadratic case**

There is a particularly clean correction here.

Suppose \\(\mu\notin\mathbb R\\) is a complex eigenvalue. A real invariant two-plane on which \\(M\\) has irreducible quadratic characteristic polynomial corresponds to a complex eigenline in the complex eigenspace

\\[ E\_\mu=\ker(M\_\mathbb C-\mu I). \\]

Thus the family is naturally parameterized by

\\[ \boxed{\mathbb P\_{\mathbb C}(E\_\mu).} \\]

If

\\[ g\_\mu=\dim\_{\mathbb C}E\_\mu, \\]

the family is

\\[ \mathbb{CP}^{g\_\mu-1}, \\]

which has real dimension

\\[ 2(g\_\mu-1). \\]

This depends on the **geometric multiplicity**, not merely the algebraic multiplicity of the irreducible quadratic factor.

That distinction should be explicit in the paper.

## **5. The simple-spectrum conclusion is correct**

If \\(M\\) has simple spectrum over \\(\mathbb C\\), then it is diagonalizable over \\(\mathbb C\\), and the invariant real two-planes are exactly:

- spans of two real eigenvectors;
- realifications of complex-conjugate eigenpairs.

Hence the count

\\[ \boxed{ \binom{k\_{\mathbb R}}2+ \\#\\{\text{nonreal conjugate pairs}\\} } \\]

is correct, where \\(k\_{\mathbb R}\\) is the number of real eigenvalues.

The conclusion that no positive-dimensional base charts are required in this case is also correct.

There is one additional detail: the number of planes is polynomial in \\(k\\) for \\(c=2\\), but the analogous number for general \\(c\\) can be exponential. For a diagonal matrix with \\(k\\) distinct real eigenvalues,

\\[ |\mathcal I_c(M)|=\binom{k}{c}. \\]

Thus the finite-base simplification is particularly useful for \\(c=2\\), but it does not automatically yield a uniform-in-\\(c\\) polynomial algorithm.

108_c2_layer.md

# **Part III. Total charts and the gcd algorithm**

## **6. The total-space construction is sound in principle**

The report proposes:

- a component \\(\mathcal C\\) of \\(\mathcal I_2(M)\\);
- a constant-rank stratum for \\(A\_{21}|\_D\\);
- a relative Grassmann bundle over \\(\mathcal C\\);
- finite charts for the base and fibre;
- a function-field gcd test on each total chart.

This is a reasonable continuation of the \\(c=1\\) methodology.

However, I would distinguish three mathematical claims.

### **Claim A: finite algebraic chart coverage**

For a finite-dimensional algebraic variety and a vector bundle over it, finite algebraic chart covers exist.

The Grassmann bundle is locally trivial, and the constant-rank condition on \\(A\_{21}|\_D\\) gives a vector bundle \\(D\mapsto T_D\\) over the relevant stratum.

This part is plausible.

### **Claim B: the chart is suitable for exact arithmetic**

This requires more than existence of a finite cover.

The paper should specify:

1. the coefficient field;
2. how the invariant-subspace components are represented;
3. how the rank strata are defined;
4. how the quotient bundle \\(T_D/W_0\\) is trivialized;
5. which pivot minors are required to be nonzero;
6. how denominators are cleared;
7. how the resulting polynomial systems are encoded.

In particular, if \\(M\\) has irrational eigenvalues, the charts may naturally be defined over a number field rather than \\(\mathbb Q\\). The field representation and selected real embedding must be part of the exact algorithm.

### **Claim C: the gcd test decides real feasibility**

This is the most delicate step.

Suppose the pencil minors on a chart are

\\[ m_1(X,\lambda),\ldots,m_s(X,\lambda). \\]

The function-field gcd is computed in

\\[ \mathbb K(X)[\lambda]. \\]

If this gcd has positive degree, the full-rank leading-coefficient lemma can show that every specialization in the chart is bad, provided the rank-\\(\omega\\) condition holds everywhere on the chart.

If the generic gcd is \\(1\\), then the good specializations form a nonempty Zariski-open subset of the chart.

But **nonempty Zariski-open does not automatically imply a real point**.

The algorithm needs a real-point density condition, or an explicit real-point construction.

For the simple-spectrum case, this is relatively straightforward because the base directions are real algebraic points and the fibre is a real Grassmannian. For positive-dimensional repeated-eigenspace components, the paper should state and prove the needed real-density property.

### **Recommendation**

State a separate proposition:

> **Real generic-point criterion.** Let \\(\mathcal X\\) be an irreducible chart defined over a real number field, with a Zariski-dense set of real points. Suppose the pencil has rank-\\(\omega\\) leading coefficient at every real point of the chart. Then the generic gcd is \\(1\\) if and only if the chart contains a real pencil-feasible point.

This proposition should be proved once and then used throughout the \\(c\geq2\\) analysis.

The converse direction relies on the density of real points, not merely on algebraic irreducibility.

## **7. Algorithm semantics need a small but important correction**

The report says:

- feasible on the first chart whose gcd is constant;
- infeasible if every chart has positive-degree gcd;
- otherwise undecided.

This is not quite sufficient unless the chart's real-point conditions are included.

A chart may be algebraically nonempty but have no real points. A constant generic gcd on such a chart does not prove real feasibility.

I recommend a three-way exact decision procedure:

1. **Feasible:** a real point is explicitly obtained, or the real generic-point criterion is proved applicable.
2. **Infeasible:** every real-admissible chart has a certified positive-degree generic gcd.
3. **Undecided:** a chart has not been shown to possess a real point or the required rank/regularity conditions have not been certified.

The distinction is particularly important when moving from rational charts to components defined over algebraic number fields.

# **Part IV. The non-monotonicity counterexample**

## **8. The proposed phenomenon is important**

The report claims that, at fixed order \\(q=3\\),

- the \\(c=2\\) layer contains a feasible design;
- the \\(c=1\\) layer contains no feasible design.

If verified, this is an important result.

It shows that the layer decomposition is not monotone in the direction

\\[ \text{feasible at larger }c \Longrightarrow \text{feasible at smaller }c. \\]

This matters because it rules out a tempting complexity strategy: solve only small layers and infer the rest from monotonicity.

I agree that this is a valuable counterexample to pursue.

## **9. The&#x20;**\\(c=1\\)**&#x20;argument appears to omit a projective direction**

The report parameterizes the repeated eigenspace by

\\[ D=\operatorname{span}(e_1+s e_2), \qquad s\in\mathbb R. \\]

But the set of lines in

\\[ E_1=\operatorname{span}(e_1,e_2) \\]

is

\\[ \mathbb P(E_1)\cong\mathbb{RP}^1. \\]

The parameterization above covers all lines except

\\[ \operatorname{span}(e_2). \\]

Indeed, the line \\([0:1]\\) cannot be represented as \\([1:s]\\) for finite \\(s\\).

Thus the assertion that the entire projective family is bad requires one additional check:

\\[ D=\operatorname{span}(e_2). \\]

This is the most concrete gap in the non-monotonicity argument.

### **How to repair it**

Use two projective charts:

\\[ D=\operatorname{span}(e_1+s e_2) \\]

and

\\[ D=\operatorname{span}(u e_1+e_2). \\]

Alternatively, prove that the homogenized gcd certificate is valid on the entire projective line, including the point at infinity.

The two isolated directions \\(e_3,e_4\\) must also be checked as stated.

## **10. The symbolic gcd certificate should be made explicit**

The report gives

\\[ H= \begin{pmatrix} -s&1&0&0\\\ 0&0&1&0\\\ 0&0&0&1 \end{pmatrix} \\]

and claims that the gcd of the two nonzero maximal minors is

\\[ (\lambda-1)(\lambda-2)(\lambda-3) \\]

independently of \\(s\\).

This is useful, but the paper should include:

- the full \\(H_A\\) matrix;
- all nonzero maximal minors;
- the exact gcd computation;
- a verification of the missing projective direction;
- the two remaining directions \\(e_3,e_4\\).

The claim is stronger than saying that several sample directions are bad. It asserts that every admissible \\(c=1\\) direction is bad. The complete projective coverage is therefore essential.

## **11. The&#x20;**\\(c=2\\)**&#x20;design also needs a reproducible certificate**

The report gives

\\[ D=\operatorname{span}(e_1+e_2,e_3) \\]

and a vector

\\[ W=(0,0,1,1,0,0,0,0). \\]

It asserts that the resulting design has \\(\omega=2\\), satisfies (5a), satisfies exactness, and has six coprime \\(2\times2\\) maximal minors.

This is the right type of certificate. However, the report should display the full data needed to reproduce it.

In particular, provide:

1. the explicit basis \\(N\\) of \\(K_0\\);
2. the full matrix \\(A\\), or the relevant blocks \\(M,A\_{21}\\);
3. the resulting row-space basis \\(V\\);
4. the matrices \\(H,H_A\\);
5. the six maximal minors;
6. a Bézout identity or exact gcd computation certifying that their common gcd is \\(1\\).

The coordinate convention also needs to be made explicit. The report uses \\(e_1,\ldots,e_4\\) for vectors in the compressed \\(K_0\\)-coordinates while \\(W\\) is displayed as an eight-dimensional ambient vector. This is legitimate, but it should be stated clearly to avoid ambiguity.

### **Verdict on Q3**

The non-monotonicity claim is **plausible and potentially correct, but not fully certified in the report as written**. The omitted projective point is a specific coverage gap that must be closed before the claim is regarded as proved.

108_c2_layer.md

# **Part V. Gcd degree versus positivity**

## **12. The methodological remark in II.3 is mathematically sound, with qualifications**

The report observes that the generic gcd degree can vary among specializations, while its positivity is the relevant property.

This is consistent with the full-rank leading-coefficient argument.

Suppose the maximal minors satisfy

\\[ \deg\_\lambda m_I(X,\lambda)=\omega \\]

for at least one minor at every admissible point \\(X\\).

If the generic gcd has positive degree, the specialization lemma implies that every admissible specialization has a nonconstant common divisor.

The degree of the specialized gcd can increase at special points. Therefore, it is unnecessary to prove that the gcd degree is constant throughout a chart.

This is an important simplification.

### **Why can the degree vary?**

For a polynomial family, the degree of the gcd is generally upper-semicontinuous under suitable fixed-degree hypotheses: specializations can acquire additional common factors, but generic specializations have the minimal gcd degree.

For example, consider

\\[ f_1(x,\lambda)=\lambda(\lambda-x), \qquad f_2(x,\lambda)=\lambda(\lambda-1). \\]

For generic \\(x\ne1\\), the gcd is \\(\lambda\\). At \\(x=1\\), the two polynomials coincide and the gcd degree increases.

The same general phenomenon can occur in the pencil-minor family: special parameter values may create additional common eigenvalue factors.

### **A wording correction**

The report says:

> Within one rank stratum the gcd degree is not constant (values 1 and 2 both occur) ...

It should clarify that this means **as&#x20;**\\(D\\)**&#x20;varies within the rank stratum**. At a fixed direction \\(D\\), the specialized gcd has a definite degree.

I would state the result as:

> The generic gcd degree need not be constant under specialization within a rank stratum. Nevertheless, for the chartwise decision procedure, only whether the generic gcd degree is zero or positive is required.

### **One further point**

A chart with generic gcd \\(1\\) does not imply that every point on that chart is feasible. It implies that a nonempty Zariski-open subset is algebraically good, and—with the appropriate real-point density hypothesis—that at least one real feasible point exists.

The distinction between generic feasibility and universal feasibility should be emphasized throughout.

108_c2_layer.md

# **Part VI. The complexity claim**

## **13. II.5 contains the most serious complexity issue**

The report states that enumerating \\(c\\) and the components of \\(\mathcal I_c(M)\\) is polynomial, and that the chart route gives

\\[ n^{O(c^2)}. \\]

I do not think either conclusion is established by the current argument.

There are two separate problems.

## **13.1 The number of invariant-subspace components is not uniformly polynomial**

Consider

\\[ M=\operatorname{diag}(\lambda_1,\ldots,\lambda_k) \\]

with distinct real eigenvalues.

Every invariant \\(c\\)-dimensional subspace is the span of a choice of \\(c\\) coordinate eigenvectors. Hence

\\[ |\mathcal I_c(M)|=\binom{k}{c}. \\]

For fixed \\(c\\), this is \\(O(k^c)\\), which is polynomial for every fixed \\(c\\).

But if \\(c\\) is part of the input and is allowed to vary, the number of components can be exponential:

\\[ \binom{k}{\lfloor k/2\rfloor} =\Theta\left(\frac{2^k}{\sqrt{k}}\right). \\]

Thus the statement that enumeration is polynomial is correct only under a fixed-\\(c\\) interpretation, or under additional restrictions on the spectrum and component structure.

This distinction should be made explicit.

## **13.2 The claimed&#x20;**\\(n^{O(c^2)}\\)**&#x20;bound does not follow from the dimension count**

The report gives a chart dimension of the form

\\[ c(d\_\lambda-c) + (t-w_0)\bigl((n-k)-r-t\bigr). \tag{8} \\]

The second term is bounded in terms of \\(n-k\\), and in this problem

\\[ n-k=\operatorname{codim}K_0\le 2p. \\]

Thus the fibre dimension is at most \\(O(p^2)\\).

But the base term

\\[ c(d\_\lambda-c) \\]

can be \\(O(cn)\\).

In particular, for \\(c=2\\) and a repeated eigenspace of dimension \\(\Theta(n)\\), the base chart dimension is \\(\Theta(n)\\), not \\(O(1)\\).

The conclusion

\\[ n^{O(c^2)} \\]

therefore requires a complexity argument beyond the chart-dimension count. The fact that a chart has \\(m\\) variables does not automatically produce a complexity bound with exponent \\(O(c^2)\\).

If the algebraic decision procedure has complexity polynomial in the degrees and coefficient sizes but exponential in the number of variables, then a chart with \\(O(cn+p^2)\\) variables may yield a bound of the form

\\[ n^{O(cn+p^2)}, \\]

not \\(n^{O(c^2)}\\).

I am not asserting that this is necessarily the optimal bound. I am saying that the report has not justified the stated one.

### **What can safely be claimed now?**

A more defensible statement is:

> For fixed \\(c\\), the invariant-subspace base can be represented by finitely many algebraic charts. The chart dimension and the complexity of the resulting exact decision procedure depend on the multiplicities and Jordan structure of \\(M\\). A uniform bit-complexity bound remains to be established.

For simple spectrum and \\(c=2\\), the base is finite and the problem reduces to finitely many fixed-direction fibre tests. This is the strongest clean complexity result presently supported by the report.

## **14. A more useful intermediate target than a uniform algorithm**

Before attempting a uniform-in-\\(c\\) algorithm or a hardness reduction, I recommend studying whether the fibre condition can be eliminated structurally for fixed \\(D\\).

This is especially promising because the split fibre is now explicit.

For fixed \\(D\\), define

\\[ T_D=K_0^\perp\cap(A\_{21}D)^\perp, \qquad W_0=P\_{K_0^\perp}(V_0). \\]

The fibre consists of \\(t\\)-dimensional \\(W\\) satisfying

\\[ W_0\subseteq W\subseteq T_D. \\]

The remaining problem is to determine whether at least one such \\(W\\) makes the pencil

\\[ \lambda H(W)-H_A(W) \\]

have full rank for every \\(\lambda\\).

A useful first question is:

> Can the existence of such a \\(W\\) be characterized by a rank, controllability, observability, or subspace-separation condition involving only the induced maps on \\(T_D/W_0\\)?

If the answer is yes, then one may eliminate the Grassmannian fibre and reduce the search to the base \\(\mathcal I_c(M)\\).

That could be much more valuable than immediately trying to solve the full real algebraic feasibility problem.

# **Part VII. The compressed-pair dictionary**

## **15. II.6 is conceptually correct**

The report writes

\\[ U=\pi_1(W)=\operatorname{row}(VN), \qquad D=U^{\perp\_{K_0}}. \\]

Then

\\[ c=k-\dim U. \\]

This is correct.

It also states that

\\[ (5a)\iff\pi_2(W)\subseteq\pi_1(W). \\]

That is the same compressed-pair inclusion used in the earlier project.

The additional equivalence

\\[ M(D)\subseteq D \iff M^\*(U)\subseteq U \\]

is also correct, where \\(M^\*\\) is the adjoint with respect to the chosen inner product on \\(K_0\\).

This is an important conceptual point: the split \\(c\\)-layer can be viewed either as an invariant kernel problem or as a codimension-\\(c\\) invariant row-subspace problem in the dual coordinates.

I recommend making this dictionary a formal proposition, since it connects the new layer theory to Papers I and II.

One caution: the compressed-pair map may lose information about ambient row-space lifts. The equality of the projected subspace \\(U\\) does not by itself reconstruct \\(V\\); the fibre data still matter.

108_c2_layer.md

# **Part VIII. Lean formalization and proof reliability**

## **16. The Lean results are useful, but their scope should be stated narrowly**

The report says that three lemmas establish:

1. \\(V\cap K_0=K_0\cap D^\perp\\);
2. the dimension decomposition of \\(V\\);
3. the relevant set/dimension assertions.

This is useful formal verification.

However, the two central implications remain unformalized:

- the equivalence between \\(V\perp AD\\) and \\(W\subseteq T_D\\);
- the exactness condition in the unrestricted fibre.

These are not particularly difficult to formalize, and I would prioritize them.

In particular, the Lean development should eventually verify the full theorem:

\\[ \begin{aligned} &V\text{ is }K_0\text{-split},\\\ &D=K_0\cap V^\perp,\quad M(D)\subseteq D,\\\ &V_0\subseteq V,\quad AD\perp V \end{aligned} \\]

if and only if

\\[ \begin{aligned} &V=D^{\perp\_{K_0}}\oplus W,\\\ &W_0\subseteq W\subseteq T_D,\\\ &P\_{K_0}(V_0)\subseteq D^{\perp\_{K_0}}. \end{aligned} \\]

This is a clean formalization target and would eliminate the current missing-condition ambiguity.

The Lean audit should also be reported with the exact theorem statements, not just a description of the three lemmas. An axiom audit is valuable, but it does not automatically establish that the formalized theorem is the same as the theorem stated in the paper.

# **Part IX. Recommended revised theorem structure**

I would reorganize the next \\(c=2\\) paper as follows.

## **Theorem 1. Layer identities**

Establish

\\[ \rho=\operatorname{rank}H,\qquad c=k-\rho,\qquad t=q-\rho, \\]

and

\\[ q=\rho+t,\qquad c-t=k-q. \\]

State the full-row-rank assumption.

## **Theorem 2. Unrestricted fixed-kernel fibre**

For fixed \\(D\subseteq K_0\\), give the exact fibre

\\[ \mathcal F_D= \left\\{ V\in\operatorname{Gr}(q,(D+AD)^\perp): V_0\subseteq V,\ K_0\cap V^\perp=D \right\\}. \\]

Prove that the exact-kernel condition is equivalent to

\\[ K_0\cap(D+AD)=D. \\]

## **Theorem 3.&#x20;**\\(K_0\\)**-split invariant-kernel theorem**

Under the split condition,

\\[ M(D)\subseteq D. \\]

Also prove

\\[ V=D^{\perp\_{K_0}}\oplus W. \\]

## **Theorem 4. Prescribed-row-compatible split fibre**

State the missing compatibility condition:

\\[ P\_{K_0}(V_0)\subseteq D^{\perp\_{K_0}}. \\]

Then prove the Grassmannian fibre formula (5) and dimension formula (7).

## **Theorem 5. The invariant-two-plane base**

Give the correct classification in terms of real primary components and Jordan structure.

For simple spectrum, prove the finite count.

For repeated eigenvalues, provide the relevant component dimensions.

## **Theorem 6. Total chart and gcd criterion**

Prove:

- finite chart coverage;
- constant-rank bundle construction;
- rank-\\(\omega\\) leading coefficient;
- generic gcd criterion;
- real-point density condition.

## **Theorem 7. Non-monotonicity at fixed order**

Present the \\(n=8\\) example with complete rational matrices and exact gcd certificates. Explicitly cover the point at infinity in the \\(c=1\\) projective family.

This is a useful standalone structural result and should not be buried inside the algorithm section.

# **Part X. Priority roadmap**

**Priority 1 — correctness**

Do first

1. Add the missing prescribed-row base condition \\(P\_{K_0}(V_0)\subseteq D^\perp\\).
2. Repair the invariant-two-plane classification for multiple Jordan blocks.
3. Check the missing projective point in the \\(c=1\\) counterexample.
4. Publish complete exact certificates for both sides of the counterexample.

   **Priority 2 — exact decidability**

   Next
5. Prove the real generic-point criterion.
6. Specify number-field and chart representations.
7. Make the finite-cover construction effective.
8. Formalize the two remaining fibre equivalences in Lean.

   **Priority 3 — complexity**

   Afterwards
9. Correct the \\(n^{O(c^2)}\\) claim or provide a new proof.
10. Establish the fixed-\\(c=2\\) complexity bound under explicit spectral assumptions.
11. Investigate elimination of the fibre variable \\(W\\).
12. Only then choose between uniform algorithms and hardness reductions.

## **17. My recommendation for the next mathematical result**

I would not make the next paper's central theorem a general \\(c=2\\) complexity result. Instead, I would aim for a more focused structural theorem:

> **Proposed theorem: Complete structure of the&#x20;**\\(K_0\\)**-split&#x20;**\\(c=2\\)**&#x20;design family.**\
> The admissible kernel directions are precisely the real \\(M\\)-invariant two-planes satisfying the prescribed-row orthogonality condition. On each constant-rank stratum of \\(A\_{21}|\_D\\), the prescribed-row-compatible row-space choices form a relative Grassmann bundle. The pencil-feasible designs constitute the subset on which the maximal minors of the compressed pencil have no common real-affine spectral root.

This theorem would establish a clean bridge between the \\(c=1\\) hyperplane paper and the higher-layer program.

The most interesting subsequent question is then whether the pencil condition can be reduced to a criterion on \\(D\\) alone, or whether the fibre variable \\(W\\) is genuinely essential.

# **Final verdict**

**Report 108 is a substantial improvement and gives a credible foundation for the&#x20;**\\(c=2\\)**&#x20;program, but it is not yet ready to support its full algorithmic and complexity conclusions.**

The strongest results are:

- the unrestricted exact-kernel fibre;
- the \\(K_0\\)-split decomposition;
- the invariant-kernel theorem;
- the Grassmannian description of the split fibre;
- the simple-spectrum finite-base reduction.

The most important corrections are:

1. Add the missing prescribed-row compatibility condition to the split base.
2. Complete the invariant-two-plane classification beyond isolated Jordan blocks.
3. Close the missing projective point in the non-monotonicity example.
4. Establish real-point density for the generic gcd argument.
5. Rework the uniform complexity estimate; the current \\(n^{O(c^2)}\\) conclusion is not justified.

**My strategic advice:** finish and rigorously certify the \\(c=2\\) geometry first. Then investigate elimination of the fibre variable \\(W\\). That intermediate result has the best chance of producing a genuinely new structural theorem and may determine whether the eventual complexity question is tractable or calls for a hardness reduction.