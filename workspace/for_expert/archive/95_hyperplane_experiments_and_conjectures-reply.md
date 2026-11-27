# **Review of Report 95: The hyperplane layer — experiments and conjectures**

This is a useful and substantially more focused report than Report 94. It does something important: it moves from the general componentwise generic-gcd framework to the special geometry of the hyperplane layer, where the kernel direction \\(v\\) is fixed on each lifted incidence fibre and the spectral pencil has additional structure.

My overall assessment is:

- **The fixed-kernel-direction observation is correct and potentially important.**
- **The reduction in H3 is mathematically promising, but its precise scope and dimensions need to be stated more carefully.**
- **H1 is plausible as a generic statement, but I would not conjecture constancy at every point of a component. In fact, there are simple structured pencil families where the gcd degree jumps.**
- **H2 needs clarification. A finite algebraic cover with moving roots is not exceptional in algebraic geometry; it is a natural possibility for parameterized polynomial families.**
- **H4 is currently the weakest conjecture. The two examples do not provide a convincing basis for a general theorem.**

My recommendation is to prioritize **H3, then a corrected generic version of H1, and then H2**. I would postpone H4 until there is a structural theorem about the eigen fibres.

The report's computational evidence is clearly separated from its proved results, which is good practice. In particular, E3 and E4 should remain evidence, not be promoted to a theorem about the entire component.&#x20;

95_hyperplane_experiments_and_conjectures.md



## **1. First, the strongest mathematical observation: the fixed kernel direction**

The central observation in II.1(4) is

\\[ M(\lambda)=Q(\lambda I-A)N, \\]

where the rows of \\(Q\\) form a basis of \\(U^\perp\\), with

\\[ U=\operatorname{span}(v,Av). \\]

Since \\(Qv=0\\) and \\(QAv=0\\),

\\[ M(\lambda)c_v =Q(\lambda I-A)Nc_v =Q(\lambda v-Av) =0. \\]

Thus

\\[ \boxed{M(\lambda)c_v=0\qquad\forall\lambda.} \\]

This is immediate, but its consequences are substantial.

It says that the spectral pencil is not merely a generic affine pencil. It has a **parameter-independent right kernel direction**. Consequently, the rank problem can be considered on the quotient of the domain by that direction.

This is exactly the kind of structure that could make the hyperplane layer substantially easier than the general prescribed-row problem.

There is, however, one qualification to the report's wording.

### **1.1 The determinant statement needs a dimension qualification**

The report says that \\(\det M\equiv0\\). This is valid when \\(M\\) is square. In the stated general setting,

\\[ M(\lambda)\in\mathbb Q[\lambda]^{(n-2)\times k}, \\]

so it need not be square.

The dimension-independent statement is

\\[ \boxed{\operatorname{rank}M(\lambda)\le k-1 \qquad\forall\lambda.} \\]

Equivalently, all \\(k\times k\\) minors vanish identically whenever those minors are defined.

In the E2 dimensions, \\(n-2=k=3\\), so the determinant statement is indeed meaningful. But the theorem should not be written in a way that implicitly assumes this equality in the general setting.

### **1.2 The quotient pencil is the natural object**

Choose a basis of \\(K_0\\) whose final vector is \\(v\\). In this basis, the last column of \\(M(\lambda)\\) is identically zero:

\\[ M(\lambda)= \begin{bmatrix} \widetilde M(\lambda)&0 \end{bmatrix}, \\]

where

\\[ \widetilde M(\lambda)\in \mathbb Q[\lambda]^{(n-2)\times(k-1)}. \\]

Since \\(H=QN\\) has rank \\(k-1\\), the leading coefficient of \\(\widetilde M\\) has full column rank.

For the maximal-minor rank condition, we therefore have

\\[ \operatorname{rank}M(\lambda)\<k-1 \iff \operatorname{rank}\widetilde M(\lambda)\<k-1. \\]

This is the most useful form of the reduction.

It converts the original pencil, which has a forced kernel, into a pencil with full-column-rank leading coefficient and no longer has a trivial forced kernel.

**I would make this quotient-pencil formulation the central theorem of the next report.**

## **2. H1: degree constancy of the gcd**

The conjecture is:

> On each irreducible component, the degree of the gcd of the maximal minors is constant.

This is the conjecture I would revise most urgently.

There is a general algebraic-geometric reason to be cautious: **the degree of a polynomial gcd is generally constant only on a dense open subset, not necessarily on an entire irreducible parameter space.**

Special parameter values can create additional common factors or increase their multiplicities.

### **2.1 A simple structured pencil showing the danger**

Consider the parameterized \\(3\times2\\) pencil

\\[ B_t(\lambda)= \begin{bmatrix} \lambda&0\\\ 0&\lambda\\\ 0&t \end{bmatrix}. \\]

Its leading coefficient is

\\[ B_1= \begin{bmatrix} 1&0\\\ 0&1\\\ 0&0 \end{bmatrix}, \\]

which has full column rank for every \\(t\\).

The three maximal minors are

\\[ \lambda^2,\qquad \lambda t,\qquad 0. \\]

Therefore,

\\[ \gcd(\text{maximal minors})= \begin{cases} \lambda,&t\ne0,\\\ \lambda^2,&t=0. \end{cases} \\]

The gcd degree jumps from \\(1\\) to \\(2\\) at the special parameter value \\(t=0\\).

This example also has the fixed-kernel-direction structure of the report if we append a zero column:

\\[ M_t(\lambda)= \begin{bmatrix} \lambda&0&0\\\ 0&\lambda&0\\\ 0&t&0 \end{bmatrix}. \\]

The third coordinate vector is a fixed right kernel vector, and the leading coefficient has rank \\(2\\).

Thus, **a fixed kernel direction and a constant-rank leading coefficient do not, by themselves, force global gcd-degree constancy.**

This does not disprove H1 for the particular incidence components in the report. Those components may impose additional restrictions that exclude the exceptional behaviour. But it shows that the argument cannot rely only on the fixed kernel direction.

### **2.2 What is actually plausible**

I would replace H1 with the following two-level conjecture.

**H1a — Generic degree constancy.**

On every irreducible component \\(Y\\), there exists a dense Zariski-open subset \\(Y^\circ\\) such that

\\[ \deg\gcd_I m_I(y;\lambda) \\]

is constant for \\(y\in Y^\circ\\).

This is the natural generic behaviour of a parameterized polynomial family.

**H1b — No degree jumps on the relevant components.**

For the special components \\(Z^\circ\\) and \\(F\_\lambda\\) of the hyperplane incidence space, the gcd degree is constant even at exceptional points.

This is the genuinely interesting conjecture, but it needs a structural explanation.

The distinction matters algorithmically. H1a gives a generic certificate. H1b gives a component-wide certificate.

### **2.3 A possible route through Smith normal form**

For a polynomial matrix \\(B(\lambda)\\) over a field, the gcd of its maximal minors is closely related to its invariant factors under polynomial unimodular transformations.

For a full-column-rank polynomial matrix

\\[ B(\lambda)\in F[\lambda]^{m\times r}, \\]

its Smith normal form has diagonal invariant factors

\\[ d_1(\lambda)\mid d_2(\lambda)\mid\cdots\mid d_r(\lambda), \\]

and, up to multiplication by a nonzero constant,

\\[ \gcd(\text{all }r\times r\text{ minors}) =d_1(\lambda)\cdots d_r(\lambda). \\]

This suggests that the gcd degree might be controlled by polynomial-matrix invariants.

However, the invariant factors can change under specialization of the parameters. The example above is precisely the sort of specialization phenomenon that must be ruled out.

A potentially useful approach is to investigate whether the quotient pencil arising from the hyperplane geometry has a fixed polynomial-module structure, not merely a fixed leading-coefficient rank.

**Verdict on H1:** pursue generic degree constancy first. Treat full component-wide constancy as a separate, stronger conjecture.

## **3. H2: fixed roots versus moving roots**

The report distinguishes:

1. A fixed root.
2. A finite cover.
3. Genuine movement of roots.

It then conjectures that the middle case does not occur.

I do not think the current formulation is sufficiently precise to support this conjecture.

### **3.1 A finite algebraic cover with moving roots is natural**

Consider the polynomial family

\\[ f_t(\lambda)=\lambda^2-t. \\]

For generic \\(t\\), there are two roots,

\\[ \lambda=\pm\sqrt t. \\]

There is no fixed root common to all parameter values. The roots form a finite algebraic cover of the parameter line, ramified at \\(t=0\\).

This is the standard situation for roots of a parameterized polynomial.

In particular, if “finite cover” means that the root incidence projects finitely onto the parameter space, then a nonconstant finite cover is not an unusual intermediate phenomenon. It is a basic way in which roots move.

### **3.2 The distinction should be reformulated geometrically**

Let

\\[ \mathcal E= \\{(y,\lambda)\in Y\times\mathbb A^1: m_I(y;\lambda)=0\ \text{for all }I\\}. \\]

There is a projection

\\[ \pi:\mathcal E\to Y. \\]

The relevant possibilities include:

- **Fixed-root mechanism:** there is a \\(\lambda_0\\) such that \\(\lambda_0\\) is a common root for every \\(y\in Y\\).
- **Finite moving-root mechanism:** \\(\pi\\) is generically finite, but no fixed \\(\lambda_0\\) works on all of \\(Y\\).
- **Positive-dimensional root fibres:** for some parameters, the common-root set is positive-dimensional, or the incidence has a component whose projection has positive-dimensional generic fibres.

For a nonzero univariate gcd, the fibre over a fixed parameter is finite. Thus the generic root incidence is often finite over the base after restricting to a suitable open set.

The genuinely important distinction is not “finite cover versus genuine movement.” It is whether the projection has a fixed root section, whether it is generically finite and nontrivial, or whether it has positive-dimensional fibres.

### **3.3 A better question**

I suggest replacing H2 by:

> **H2′. Root-incidence structure.** On each hyperplane component, is the root-incidence projection either dominated by a fixed-root component or generically finite with a prescribed degree? Can positive-dimensional generic fibres occur?

This formulation is more precise and is directly connected to the geometry of the pencil.

It also gives you a concrete computational target: compute the dimension and degree of the incidence variety, rather than just comparing sampled root sets.

**Verdict on H2:** do not try to prove the current dichotomy before clarifying the meaning of “finite cover.” A nontrivial finite cover with moving roots is entirely plausible.

## **4. H3: the reduced pencil suffices**

This is, in my view, the most promising conjecture in the report.

The reduction is not merely a heuristic compression. On the non-eigen stratum, where

\\[ \dim U=2, \\]

the row space of \\(Q\\) is exactly \\(U^\perp\\), so

\\[ M(\lambda)=Q(\lambda I-A)N \\]

is the spectral pencil associated with the maximal row space.

Since \\(M(\lambda)c_v=0\\) identically, we can quotient out the direction \\(c_v\\).

The resulting pencil is

\\[ \widetilde M(\lambda)\in \mathbb Q[\lambda]^{(n-2)\times(k-1)}. \\]

Its leading coefficient has full column rank, and the badness condition becomes

\\[ \boxed{ \operatorname{rank}\widetilde M(\lambda)\<k-1 \quad\text{for some }\lambda\in\mathbb C. } \\]

This is a cleaner problem than checking all \\(\binom q\omega\\) maximal minors of the original \\(q\times k\\) pencil.

### **4.1 One qualification: the distinction between equality and sufficiency**

The report correctly distinguishes the case

\\[ \operatorname{row}L=U^\perp \\]

from the case

\\[ \operatorname{row}L\subsetneq U^\perp. \\]

In the equality case, the reduced pencil captures the spectral condition exactly.

In the strict-inclusion case, the condition derived from \\(Q\\) is sufficient, not necessarily equivalent.

This distinction should remain explicit in every theorem based on H3. Otherwise, the algorithm might incorrectly reject a feasible lower-dimensional row space merely because the maximal-space pencil is bad.

### **4.2 Is the reduced problem polynomial-time decidable?**

For a fixed parameter \\(v\\), yes: the problem is substantially simpler than the original formulation.

Given a rational affine pencil

\\[ \widetilde M(\lambda)=\lambda X-G, \qquad X\in\mathbb Q^{m\times r},\quad \operatorname{rank}X=r, \\]

we want to decide whether

\\[ \operatorname{rank}(\lambda X-G)=r \quad\forall\lambda\in\mathbb C. \\]

This is a standard polynomial-matrix rank problem. The condition is equivalent to the maximal minors having no common complex root.

There are several exact approaches:

- Compute the gcd of the maximal minors.
- Use polynomial-matrix normal forms.
- Use a resultant or subresultant construction.
- Use a suitable Bézout or Sylvester-type matrix.

For a fixed rational pencil, these are exact algebraic computations. The important algorithmic question is the size of the polynomial representation and the dependence on \\(m,r\\).

### **4.3 The&#x20;**\\(3\times2\\)**&#x20;case**

The report specifically asks about a \\(3\times2\\) affine pencil. This is a good test case.

Write

\\[ B(\lambda)= \begin{bmatrix} a_1\lambda+b_1 & a_2\lambda+b_2\\\ c_1\lambda+d_1 & c_2\lambda+d_2\\\ e_1\lambda+f_1 & e_2\lambda+f_2 \end{bmatrix}. \\]

Its three \\(2\times2\\) minors are polynomials of degree at most two:

\\[ p\_{12}(\lambda),\quad p\_{13}(\lambda),\quad p\_{23}(\lambda). \\]

The badness condition is exactly

\\[ \gcd(p\_{12},p\_{13},p\_{23})\ne1. \\]

This is easy to decide for a single rational instance.

The harder question is the **parameterized** version, where the coefficients themselves depend on \\(v\\). Then we need to decide whether the generic gcd is nontrivial on an entire irreducible component.

That is where the algorithmic challenge in Report 94 reappears.

### **4.4 A potentially useful structural simplification**

Because the leading coefficient has full column rank, we can choose an invertible row transformation and normalize it to

\\[ X= \begin{bmatrix} I_r\\\ 0 \end{bmatrix}. \\]

Then

\\[ B(\lambda)= \begin{bmatrix} \lambda I_r-G_1\\\ -G_2 \end{bmatrix}. \\]

The pencil has full column rank at every complex \\(\lambda\\) precisely when

\\[ \operatorname{rank} \begin{bmatrix} \lambda I_r-G_1\\\ G_2 \end{bmatrix} =r \qquad\forall\lambda\in\mathbb C. \\]

By the Hautus criterion, this is equivalent to observability of the pair \\((G_1,G_2)\\).

This gives an important interpretation:

\\[ \boxed{ \text{Reduced-pencil spectral feasibility} \iff (G_1,G_2)\text{ is observable}. } \\]

The fixed-parameter problem is therefore a standard observability test.

For the parameterized problem, H3 becomes a question about **generic observability of a structured family of matrix pairs**.

This is likely a more productive direction than treating the minors as unrelated quadratic polynomials.

**Verdict on H3:** prioritize it. It offers both a smaller algebraic representation and a connection to a well-developed theory.

## **5. H4: are the eigen fibres generically good?**

The conjecture is:

> The fibres \\(F\_\lambda\\) are generically good whenever they are nonempty.

The evidence is E1 and E2, but the report itself correctly notes that two examples are insufficient.

There is a structural reason why this conjecture is not immediately obvious.

On a non-eigen stratum,

\\[ U=\operatorname{span}(v,Av) \\]

has dimension two, and the row space \\(U^\perp\\) has dimension \\(n-2\\).

On an eigen fibre,

\\[ Av=\lambda_0v, \\]

so

\\[ U=\operatorname{span}(v) \\]

has dimension one, and \\(U^\perp\\) has dimension \\(n-1\\).

Thus the eigen fibre is not simply a special parameter value of the same constant-dimensional construction. The geometry of the row constraints changes.

In particular:

- The condition \\(Rv=0\\) and \\(RAv=0\\) becomes a single independent condition.
- The ambient row space becomes larger.
- The full fibre may contain row spaces of different dimensions before the rank constraints are imposed.
- The spectral pencil has a different geometric interpretation.

Consequently, the observed good behaviour could be caused by the additional freedom in the eigen fibre, but it is not automatic.

### **5.1 A better way to investigate H4**

For a fixed eigenvalue \\(\lambda_0\\), first determine

\\[ E\_{\lambda_0} = \mathbb P(K_0\cap\ker(A-\lambda_0I))\cap B. \\]

Then describe the full fibre over a generic \\(v\in E\_{\lambda_0}\\), imposing the open rank conditions.

On that fibre, compute the generic rank of

\\[ P(\lambda)=\lambda H-H_A \\]

at the two levels:

\\[ \lambda=\lambda_0 \\]

and

\\[ \lambda\ne\lambda_0. \\]

The first question is whether the eigenvalue itself is generically a common root. The second is whether any other common root exists.

This separates two possible obstructions that are currently mixed together in H4.

### **5.2 What would disprove H4?**

A single explicit rational example in which a nonempty eigen fibre is generically bad would disprove the conjecture.

I would therefore search for such a counterexample before attempting a proof.

The construction should not merely find one bad row choice in an eigen fibre. It should show that the generic point of the relevant irreducible fibre component is bad.

**Verdict on H4:** keep it as an exploratory conjecture, not a main theorem target.

## **6. Reassessing the computational evidence**

The report's experiments are useful, but their evidential strength differs.

| Experiment | What it supports                                                         | What it does not establish                                               |
| ---------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| E1         | Distinct lifted components can have different generic spectral behaviour | That all components have the same two-component pattern                  |
| E2         | Eigen and non-eigen strata can behave differently                        | That eigen fibres are always good                                        |
| E3         | The common roots can vary with \\(v\\)                                   | That the observed root movement is generic on the entire component       |
| E4         | Degree \\(2\\) persists across the sampled matrices                      | That the degree is invariant under all specializations or all components |

The most valuable observation is E3: it warns against trying to characterize every bad component through a single fixed eigenvalue.

But I would strengthen the experiments in a different way.

### **6.1 Sample special parameter values, not only random ones**

Random sampling tends to find generic behaviour. It is less effective at finding the exceptional loci where algebraic invariants jump.

For H1, specifically sample:

- Points where the rank of the coefficient matrices drops.
- Points where discriminants vanish.
- Points where two roots collide.
- Points where the degree of the gcd increases.
- Points where the kernel of the reduced pencil has dimension greater than one.

For H2, sample points on the discriminant locus of the root polynomial.

For H4, sample generic points on each eigen fibre, not merely arbitrary row choices.

### **6.2 Use exact symbolic tests for the conjectures**

For each parameterized component, calculate:

\\[ g(y,\lambda)=\gcd_I m_I(y;\lambda) \\]

over the relevant rational-function field, not only at sampled rational points.

Then separately calculate the gcd after specialization at selected exceptional parameter values.

This distinguishes:

\\[ \deg g\_{\mathrm{generic}} \\]

from

\\[ \deg g\_{\mathrm{special}}. \\]

That distinction is essential for H1.

## **7. Which conjecture should be attacked first?**

My recommended order is:

Priority 1

**H3 — Reduced-pencil sufficiency**

This is the strongest structural simplification. Prove the quotient-pencil theorem carefully, identify the exact relationship to observability, and determine whether the parameterized family has additional structure.

Priority 2

**H1a — Generic degree constancy**

This is a natural algebraic-geometric statement and may yield a componentwise generic certificate. Do not initially insist on constancy at exceptional points.

Priority 3

**H2′ — Root-incidence structure**

Reformulate the conjecture in terms of the projection of the common-root incidence variety. The current trichotomy needs clarification.

Priority 4

**H4 — Eigen fibres are generically good**

Search for counterexamples first. The present evidence is too limited to justify a proof attempt.

## **8. Concrete next steps**

I would organize the next stage around three results.

### **Result A: Quotient-pencil theorem**

Prove the following precisely.

Let \\(v\in K_0\\) be non-eigen, let

\\[ U=\operatorname{span}(v,Av), \\]

and let \\(Q\\) have row space \\(U^\perp\\). Suppose

\\[ \operatorname{rank}(QN)=k-1. \\]

Then there is a basis of \\(K_0\\) whose final vector is \\(v\\), in which

\\[ Q(\lambda I-A)N = \begin{bmatrix} \widetilde M(\lambda)&0 \end{bmatrix}, \\]

with

\\[ \widetilde M(\lambda) =\lambda X-G, \qquad \operatorname{rank}X=k-1. \\]

Furthermore,

\\[ \operatorname{rank}\widetilde M(\lambda)=k-1 \quad\forall\lambda\in\mathbb C \\]

if and only if the normalized pair \\((G_1,G_2)\\) is observable.

This would make H3 a theorem rather than a conjecture.

### **Result B: Generic gcd-degree theorem**

For every irreducible component \\(Y\\), establish that there is a dense open subset \\(Y^\circ\\) on which

\\[ \deg\gcd_I m_I(y;\lambda)=d_Y \\]

is constant.

Then investigate whether the hyperplane geometry forces

\\[ \deg\gcd_I m_I(y;\lambda)=d_Y \qquad\forall y\in Y. \\]

If not, characterize the exceptional locus

\\[ \\{y\in Y:\deg\gcd_I m_I(y;\lambda)>d_Y\\}. \\]

This is a more realistic and useful version of H1.

### **Result C: Eigen-fibre genericity test**

For each nonempty \\(F\_\lambda\\), determine the generic gcd over its function field:

\\[ g\_{F\_\lambda}(\mu) = \gcd_I m_I(\eta;\mu) \in \overline{\mathbb Q(F\_\lambda)}[\mu]. \\]

Then H4 becomes the exact statement

\\[ g\_{F\_\lambda}(\mu)=1 \\]

for every nonempty eigen-fibre component.

This gives a clean algebraic test and avoids relying on random row choices.

## **9. Implications for the original decision-complexity problem**

The most important potential consequence is that the hyperplane layer might admit a much more efficient algorithm than the general layer.

The present strategy can be organized as

\\[ \boxed{ \begin{aligned} &\text{hyperplane incidence components}\\\ &\quad\downarrow\\\ &\text{quotient by the forced kernel direction}\\\ &\quad\downarrow\\\ &\text{parameterized observable-pair problem}\\\ &\quad\downarrow\\\ &\text{generic observability / generic gcd test}. \end{aligned} } \\]

This is a more promising route than directly computing all maximal minors of the original pencil.

However, one complexity distinction must remain explicit:

- **Fixed-parameter spectral testing:** given a rational \\(v\\), decide whether the corresponding pencil is spectrally feasible.
- **Generic component testing:** decide whether the generic point of a component is spectrally feasible.
- **Original rational feasibility:** decide whether there exists a rational admissible row choice satisfying all conditions.

The first can be handled by exact polynomial-matrix methods. The second requires parameterized algebraic computation. The third also requires rational-point considerations.

Even a complete proof of H1a and H3 would not, by itself, settle the original rational DEC problem.

## **10. Final assessment**

The report makes real progress because it identifies a special structural feature that was not fully exploited in the earlier componentwise analysis: the hyperplane kernel direction gives the spectral pencil a fixed right kernel, and quotienting out that direction produces a full-column-rank reduced pencil.

That is the central result to develop.

My main corrections are:

1. State the determinant claim only in the square case; use the rank bound in general.
2. Replace global H1 with generic degree constancy as the initial target. The fixed-kernel property alone does not imply constancy on an entire component.
3. Reformulate H2 using the geometry of the common-root incidence projection. A finite moving-root cover is a natural possibility, not something that should be excluded without a precise definition.
4. Promote H3 to a theorem about the quotient pencil and its observability interpretation.
5. Treat H4 as a conjecture to be stress-tested, not as a likely theorem.

**My strongest recommendation:** make the quotient-pencil/observability reduction the next mathematical milestone. It is the one result here that can directly reduce the complexity of the hyperplane algorithm. Once it is established, the generic gcd problem becomes a structured generic-observability problem, which is a much more informative formulation for both theory and algorithm design.