# Review of `28_open_items_and_requests.md`

The six-item gap list is well organized, and the distinctions between mathematical validity, paper proof, and Lean verification are important. My answers to the four questions are:

1. B.4: I recommend an abstract dual-pairing formalization, not an identification \\(E^{\*\*}\cong E\\). A matrix-level formulation is a reasonable fallback, but it is not mathematically necessary.
2. B.8: The proposed route avoiding Smith normal form is sound and, in my view, is the preferred route. It reduces the theorem to a finite-family Bézout/gcd lemma and the fact that a nonconstant polynomial over \\(\mathbb C\\) has a root.
3. B.13: The proposed implication is correct. The dimension condition \\(\dim\mathfrak I\<k-1\\) guarantees a point of \\(\mathbb P(K)\\) outside the projection. However, the useful sufficient condition obtained from B.13a is specifically \\(\mathcal B=\varnothing\\) and \\(v\<k-1\\).
4. L3 accounting: Under the acceptance rule written in this report, B.4, B.10, B.14, and B.24 cannot automatically be upgraded to L3 merely because their paper mathematics is accepted. If their relevant nontrivial content has no Lean kernel coverage, they remain L2. I recommend separating mathematical status from formalization status in the project ledger.

I will also address the two matters in §II.3: the D.1 correction construction and the B.13a dimension estimate. The report itself records the six gaps and the proposed acceptance standard.&#x20;

28_open_items_and_requests.md



# I. B.4 — The standard way to handle the duality without \\(E^{\*\*}\cong E\\)

## I.1. The mathematical identity

Let \\(E\\) be a finite-dimensional vector space over a field \\(\mathbb F\\), and let

\\[ M:E\longrightarrow E \\]

be linear. Its dual map is

\\[ M^\vee:E^\*\longrightarrow E^\*, \qquad M^\vee(f)=f\circ M. \\]

Let \\(J\leq E^\*\\). Define its annihilator in \\(E\\) by

\\[ J^\circ = \\{x\in E:\ f(x)=0\text{ for every }f\in J\\}. \\]

The statement in the report is

\\[ J+\operatorname{range}M^\vee=E^\* \quad\Longleftrightarrow\quad \ker M\cap J^\circ=\\{0\\}. \tag{B.4-P} \\]

Here I write \\(+\\), or equivalently the subspace lattice supremum \\(\sqcup\\), rather than \\(\sqcup\\) as though it were a disjoint union.

The key observation is that one can prove the required annihilator identity directly in \\(E\\). There is no need to construct a subspace of \\(E^{\*\*}\\) and then transport it back to \\(E\\).

First,

\\[ (J+\operatorname{range}M^\vee)^\circ = J^\circ\cap(\operatorname{range}M^\vee)^\circ. \tag{1} \\]

Second,

\\[ \boxed{ (\operatorname{range}M^\vee)^\circ=\ker M. } \tag{2} \\]

Indeed, for \\(x\in E\\),

\\[ \begin{aligned} x\in(\operatorname{range}M^\vee)^\circ &\iff (M^\vee f)(x)=0 \quad\text{for every }f\in E^\*\\\ &\iff f(Mx)=0 \quad\text{for every }f\in E^\*\\\ &\iff Mx=0. \end{aligned} \\]

The last equivalence follows because the algebraic dual separates points: if \\(y\ne0\\), there exists a linear functional \\(f\\) with \\(f(y)\ne0\\).

Combining (1) and (2),

\\[ \boxed{ (J+\operatorname{range}M^\vee)^\circ = J^\circ\cap\ker M. } \tag{3} \\]

Finally, in finite dimension, a subspace \\(H\leq E^\*\\) is all of \\(E^\*\\) if and only if its annihilator in \\(E\\) is zero:

\\[ H=E^\* \quad\Longleftrightarrow\quad H^\circ=\\{0\\}. \tag{4} \\]

Equations (3) and (4) give (B.4-P).

## I.2. Recommended Lean architecture

I recommend formalizing this through the evaluation pairing

\\[ E^\*\times E\longrightarrow\mathbb F, \qquad (f,x)\longmapsto f(x), \\]

and defining the annihilator as a submodule of \\(E\\).

The important design decision is:

> Define the annihilator of a submodule of \\(E^\*\\) directly as a submodule of \\(E\\). Do not define it by passing through a double-dual space.

A useful conceptual interface is:

```
annihilator (J : Submodule 𝔽 E*) : Submodule 𝔽 E
```

with membership specified by

```
x ∈ annihilator J ↔ ∀ f ∈ J, f x = 0.
```

The formal proof can then be divided into four independent lemmas.

Lemma 1 — Annihilator of a sum.

\\[ \operatorname{Ann}(J_1+J_2) = \operatorname{Ann}(J_1)\cap\operatorname{Ann}(J_2). \\]

This is essentially a submodule-extensionality argument. It should be a relatively straightforward lemma.

Lemma 2 — Annihilator of the range of the dual map.

\\[ \operatorname{Ann}(\operatorname{range}M^\vee) = \ker M. \\]

The proof should proceed directly from the evaluation formula

\\[ (M^\vee f)(x)=f(Mx). \\]

The only nontrivial ingredient is the separation-of-points property:

\\[ \bigl(\forall f\in E^\*,\ f(y)=0\bigr)\Longrightarrow y=0. \\]

This is the right place to use finite-dimensionality or an existing dual-separation theorem.

Lemma 3 — Zero annihilator criterion.

For \\(H\leq E^\*\\),

\\[ \operatorname{Ann}(H)=\\{0\\} \quad\Longleftrightarrow\quad H=E^\*. \\]

This is where finite-dimensionality is essential. One can prove it through a dimension formula for annihilators, or by showing that a proper subspace of \\(E^\*\\) has a nonzero common annihilator.

Lemma 4 — B.4-P.

Apply Lemmas 1–3.

This organization keeps the formalization close to the mathematical proof and prevents the type mismatch between \\(E\\) and \\(E^{\*\*}\\) from spreading through the development.

## I.3. Should B.4 be rewritten as a matrix statement?

My recommendation is not initially.

A matrix-level proof is certainly possible. Choose a basis of \\(E\\), represent \\(M\\) by a square matrix, represent \\(J\\) by a row-space basis, and use the transpose matrix to represent the dual map. The statement then becomes a familiar row-space/orthogonal-complement identity.

However, this introduces several additional formalization concerns:

- basis choices and coordinate conversions;
- row-space versus column-space conventions;
- the exact relation between the dual map and the transpose;
- transporting the result back to the basis-independent theorem.

The abstract evaluation-pairing proof avoids all of these.

I would use the matrix formulation only if the existing Mathlib interface for dual maps and annihilators makes the abstract proof unexpectedly difficult. Even then, I would preserve the abstract theorem as the mathematical target and prove it from the matrix result, rather than replacing the mathematical statement with a basis-dependent one.

Verdict on B.4: the mathematical argument is complete. The formalization obstacle identified in the report is an API/type-organization issue, not a mathematical obstruction. The best solution is to introduce a custom annihilator in \\(E\\) and prove the four lemmas above.

# II. B.8 — A route around polynomial-matrix Smith normal form

I agree with the proposed direction in §III.2. In fact, I think the gcd/Bézout route is preferable to formalizing Smith normal form for this particular theorem.

The key is to isolate the following elementary polynomial fact.

## II.1. The underlying polynomial lemma

Let \\(\mathbb F\\) be a field, let \\(\overline{\mathbb F}\\) be an algebraic closure, and let

\\[ p_1,\ldots,p_N\in\mathbb F[t] \\]

be a finite family of polynomials, not all zero.

Let

\\[ g=\gcd(p_1,\ldots,p_N), \\]

defined up to multiplication by a nonzero scalar.

Then

\\[ \boxed{ g\text{ is a nonzero constant} \quad\Longleftrightarrow\quad \text{there is no }\alpha\in\overline{\mathbb F} \text{ for which }p_i(\alpha)=0\text{ for every }i. } \tag{5} \\]

This result does not require Smith normal form.

There are two elementary divisibility properties of the gcd:

1. \\(g\mid p_i\\) for every \\(i\\).
2. There exist \\(a_1,\ldots,a_N\in\mathbb F[t]\\) such that\
   \\[\
   g=\sum\_{i=1}^N a_i p_i.\
   \tag{6}\
   \\]

The second property is the finite-family Bézout identity. It follows from the fact that \\(\mathbb F[t]\\) is a Euclidean domain.

Now suppose that every \\(p_i(\alpha)=0\\). Evaluating (6) gives

\\[ g(\alpha)=\sum_i a_i(\alpha)p_i(\alpha)=0. \\]

Conversely, if \\(g(\alpha)=0\\), then \\(g\mid p_i\\) implies

\\[ p_i(\alpha)=0 \qquad\text{for every }i. \\]

Thus

\\[ \boxed{ g(\alpha)=0 \quad\Longleftrightarrow\quad p_i(\alpha)=0\text{ for every }i. } \tag{7} \\]

If \\(g\\) is a nonzero constant, it has no root. If \\(g\\) is nonconstant, the algebraic-closure property guarantees that it has a root. This proves (5).

Notice that the proof uses only:

- polynomial divisibility;
- a finite Bézout identity;
- evaluation of polynomials;
- the existence of a root for every nonconstant polynomial over an algebraically closed field.

No polynomial-matrix normal form is involved.

## II.2. Application to the maximal minors

Let

\\[ Q(t)\in\mathbb F[t]^{a\times b} \\]

have normal rank \\(h\\).

Let

\\[ \Delta_1(t),\ldots,\Delta_N(t) \\]

be all its \\(h\times h\\) minors, and define

\\[ \Delta_h(t)=\gcd(\Delta_1(t),\ldots,\Delta_N(t)). \\]

The normal-rank assumption gives two facts:

- at least one \\(h\times h\\) minor is nonzero as a polynomial;
- every \\((h+1)\times(h+1)\\) minor is identically zero.

Consequently,

\\[ \operatorname{rank}Q(\alpha)\leq h \qquad\text{for every }\alpha\in\overline{\mathbb F}. \tag{8} \\]

At a fixed \\(\alpha\\), the usual rank criterion for a matrix over a field says

\\[ \operatorname{rank}Q(\alpha)\<h \quad\Longleftrightarrow\quad \Delta_i(\alpha)=0 \quad\text{for every }i. \tag{9} \\]

By (7),

\\[ \operatorname{rank}Q(\alpha)\<h \quad\Longleftrightarrow\quad \Delta_h(\alpha)=0. \tag{10} \\]

Combining (8) and (10),

\\[ \boxed{ \operatorname{rank}Q(\alpha)=h \text{ for every }\alpha\in\overline{\mathbb F} \quad\Longleftrightarrow\quad \Delta_h\text{ is a nonzero constant}. } \tag{11} \\]

For the report's rational-coefficient setting, one can work over \\(\mathbb Q[t]\\), extend the polynomials to \\(\mathbb C[t]\\), and use the fact that every nonconstant polynomial over \\(\mathbb C\\) has a complex root. Equivalently, one can formulate the gcd over \\(\mathbb C[t]\\); its degree is unchanged by extending the coefficient field from \\(\mathbb Q\\) to \\(\mathbb C\\).

Thus the intended statement

\\[ \boxed{ \operatorname{rank}Q(\lambda)=h\quad\forall\lambda\in\mathbb C \iff \Delta_h(\lambda)\in\mathbb Q^\times } \\]

is justified, provided \\(\Delta_h\\) is defined as a nonzero gcd of the maximal minors and the normal-rank assumption is in force.

## II.3. An important field qualification

The quantifier over \\(\lambda\\) matters.

The equivalence above is a statement about evaluation over an algebraically closed field, such as \\(\mathbb C\\).

If the condition were instead

\\[ \operatorname{rank}Q(\lambda)=h \qquad\forall\lambda\in\mathbb R, \\]

then a constant gcd would still be sufficient, but it would no longer be necessary.

For example,

\\[ g(t)=t^2+1 \\]

is nonconstant but has no real root. A family of minors with gcd \\(t^2+1\\) can therefore have no common real zero while its gcd is not constant.

Since your setup uses complex matrices and the spectral parameter is complex, the algebraically closed formulation is the appropriate one. Nevertheless, I would make this explicit in the theorem statement and in the Lean theorem's assumptions.

## II.4. Recommended Lean decomposition

I suggest avoiding the direct formalization of the full matrix theorem at first. Build the following layers.

### Layer A — Finite-family gcd lemma

Prove a theorem for a finite family of polynomials:

\\[ g=\gcd(p_1,\ldots,p_N) \\]

satisfies

\\[ g(\alpha)=0 \iff \forall i,\ p_i(\alpha)=0. \\]

This is the central algebraic lemma.

There are two implementation strategies:

- define a recursive gcd over a finite list, using the binary polynomial gcd;
- use the ideal generated by the finite family and identify its generator in the principal ideal domain \\(\mathbb F[t]\\).

I would start with the recursive finite-list version if the relevant polynomial gcd API is convenient. The ideal-theoretic version is more conceptual and may be cleaner if the principal-ideal machinery is already available.

The crucial proof obligation is the Bézout identity (6). It is better to formalize that explicitly than to try to prove the root equivalence directly by manipulating polynomial roots.

### Layer B — Matrix rank and minors

Prove or reuse the standard field-matrix theorem:

\\[ \operatorname{rank}Q\<h \iff \text{all }h\times h\text{ minors vanish}. \\]

The main engineering work here is likely to be the indexing of minors of a rectangular matrix. The mathematical content is standard; the implementation needs a convenient finite index type for row and column subsets of cardinality \\(h\\).

### Layer C — Polynomial matrix specialization

Instantiate Layer A with the finite family of maximal minors from Layer B.

Then use the normal-rank assumption to establish the upper bound (8).

### Layer D — Algebraic closure

Use the root theorem for nonconstant polynomials over an algebraically closed field.

This yields the final equivalence.

## II.5. Edge cases

There are two cases worth treating explicitly.

Case \\(h=0\\). If the normal rank is zero, then every entry of \\(Q(t)\\) is the zero polynomial, so the pointwise rank is zero everywhere. The natural convention for the gcd of the empty family of \\(0\times0\\) minors is

\\[ \Delta_0=1. \\]

This makes the criterion consistent, but the convention should be stated.

Case \\(h>0\\). The normal-rank assumption guarantees that at least one \\(h\times h\\) minor is nonzero. Therefore the gcd is nonzero, and the phrase “nonzero constant” is appropriate.

Verdict on B.8: I recommend pursuing the proposed gcd/Bézout route. It is mathematically complete and avoids the missing polynomial-matrix Smith normal form machinery. The formalization is not trivial, particularly the indexing of rectangular minors, but the algebraic core is considerably more manageable than a full Smith-form development.

# III. B.13 — The coverage implication

The implication proposed in §III.3 is correct.

I will first prove it directly, then identify exactly what follows from B.13a.

## III.1. The geometric setup

Write

\\[ P\_{\alpha,\beta}=\alpha I-\beta A, \qquad [\alpha:\beta]\in\mathbb P^1. \\]

Let

\\[ \mathfrak I = \left\\{ ([x],[z],[\alpha:\beta]): z\wedge P\_{\alpha,\beta}x=0 \right\\} \\]

be the incidence set in

\\[ \mathbb P(V)\times\mathbb P(K)\times\mathbb P^1. \\]

Here \\(x\ne0\\) and \\(z\ne0\\), since they represent projective points.

Let

\\[ \operatorname{pr}\_z: \mathfrak I\longrightarrow\mathbb P(K) \\]

be the projection

\\[ ([x],[z],[\alpha:\beta])\longmapsto[z]. \\]

The proposed implication is

\\[ \boxed{ \dim\mathfrak I<\dim\mathbb P(K)=k-1 \quad\Longrightarrow\quad \operatorname{pr}\_z(\mathfrak I)\ne\mathbb P(K). } \tag{12} \\]

This is valid.

Indeed, for any morphism of algebraic varieties, the dimension of the image is at most the dimension of the source. Thus

\\[ \dim\operatorname{pr}\_z(\mathfrak I) \leq\dim\mathfrak I \<k-1. \\]

But

\\[ \dim\mathbb P(K)=k-1. \\]

Therefore the image cannot be all of \\(\mathbb P(K)\\).

In fact, because the incidence set is closed in a product of projective varieties, the projection is a projective morphism and its image is closed. Hence the image is a proper closed subset of \\(\mathbb P(K)\\).

It follows that there exists

\\[ [z]\in\mathbb P(K)\setminus\operatorname{pr}\_z(\mathfrak I). \tag{13} \\]

By the definition of \\(\mathfrak I\\), this means

\\[ \boxed{ z\wedge(\alpha x-\beta Ax)\ne0 } \tag{14} \\]

for every nonzero \\(x\in V\\) and every \\([\alpha:\beta]\in\mathbb P^1\\).

This is precisely the conclusion proposed in the report, with one minor but important clarification: the quantifier over \\(x\\) must be over nonzero \\(x\\). If \\(x=0\\) were included, the wedge expression would always vanish.

## III.2. Why the base locus matters

Recall the base locus

\\[ \mathcal B = \left\\{ ([x],[\alpha:\beta]): P\_{\alpha,\beta}x=0 \right\\}. \\]

If \\(\mathcal B\ne\varnothing\\), choose

\\[ ([x_0],[\alpha_0:\beta_0])\in\mathcal B. \\]

Then

\\[ P\_{\alpha_0,\beta_0}x_0=0. \\]

Consequently,

\\[ z\wedge P\_{\alpha_0,\beta_0}x_0=0 \\]

for every \\([z]\in\mathbb P(K)\\).

Thus

\\[ \\{([x_0],[z],[\alpha_0:\beta_0]): [z]\in\mathbb P(K)\\} \subseteq\mathfrak I. \\]

In particular,

\\[ \boxed{ \mathcal B\ne\varnothing \quad\Longrightarrow\quad \operatorname{pr}\_z(\mathfrak I)=\mathbb P(K). } \tag{15} \\]

This is a strong structural observation: the presence of even one base point makes the incidence projection surjective.

It also shows why the base locus cannot be ignored in the dimension estimate. It is not merely a technical complication in bounding fibers; it represents a genuine obstruction to finding a point outside the incidence projection.

## III.3. What B.13a actually gives

The B.13a estimate is

\\[ \boxed{ \dim\mathfrak I \leq \max\\{v,\dim\mathcal B+k-1\\}. } \tag{16} \\]

If \\(\mathcal B=\varnothing\\), then the second contribution disappears, and the estimate becomes

\\[ \boxed{\dim\mathfrak I\leq v.} \tag{17} \\]

Therefore, if

\\[ v\<k-1, \tag{18} \\]

we obtain

\\[ \dim\mathfrak I\leq v\<k-1. \\]

Applying (12), the projection is not surjective, and the desired \\([z]\\) exists.

Thus a clean sufficient condition is

\\[ \boxed{ \mathcal B=\varnothing \quad\text{and}\quad v\<k-1 \quad\Longrightarrow\quad \exists[z]\in\mathbb P(K): \ z\wedge(\alpha x-\beta Ax)\ne0 \ \forall [x],[\alpha:\beta]. } \tag{19} \\]

This is the direct coverage criterion obtained from B.13a.

There is an important point about the dimension bound. If \\(\mathcal B\ne\varnothing\\), then

\\[ \dim\mathcal B+k-1\geq k-1, \\]

so (16) cannot imply \\(\dim\mathfrak I\<k-1\\). This is not a weakness of the estimate: by (15), the projection is then actually surjective.

## III.4. Is the proposed condition \\(\dim\mathfrak I\<k-1\\) itself the coverage criterion?

Yes. It is the cleanest abstract coverage criterion:

> A family of incidence conditions does not cover \\(\mathbb P(K)\\) if its incidence variety has dimension strictly smaller than \\(\dim\mathbb P(K)\\).

The role of B.13a is to provide a computable or structurally interpretable upper bound for that dimension.

I would distinguish the two results in the paper:

B.13b — Abstract coverage lemma.

\\[ \dim\mathfrak I\<k-1 \implies \mathbb P(K)\setminus\operatorname{pr}\_z(\mathfrak I)\ne\varnothing. \\]

B.13c — Sufficient condition from the base-locus estimate.

\\[ \mathcal B=\varnothing,\quad v\<k-1 \implies \dim\mathfrak I\<k-1. \\]

This separation is worthwhile. B.13b is a general geometric principle. B.13c is the application of your particular incidence-dimension estimate.

## III.5. A useful interpretation of the homogeneous pencil

The homogeneous convention should remain

\\[ P\_{\alpha,\beta}=\alpha I-\beta A. \\]

Its values at the two distinguished points of \\(\mathbb P^1\\) are

\\[ P\_{1,0}=I,\qquad P\_{0,1}=-A. \\]

Thus the projective parameter includes both the identity direction and the \\(A\\)-direction. In particular, the point at infinity is not represented by \\(Ax\\) with a positive sign; it is represented by \\(-Ax\\). Since the incidence equation is homogeneous in the pencil vector, the sign does not affect the zero-wedge condition, but the exact formula should nevertheless be kept consistent.

## III.6. Degenerate cases

The statement needs the usual dimension conventions.

- If \\(K=\\{0\\}\\), then \\(\mathbb P(K)=\varnothing\\), so there is no projective point \\([z]\\) to find. The result should be stated only for \\(k=\dim K\geq1\\).
- If \\(V=\\{0\\}\\), then \\(\mathbb P(V)=\varnothing\\), the incidence set is empty, and the coverage conclusion is immediate whenever \\(\mathbb P(K)\ne\varnothing\\).
- The condition in (14) concerns projective \\(x\\), hence nonzero \\(x\\), and projective \\([\alpha:\beta]\\), hence \\((\alpha,\beta)\ne(0,0)\\).

Verdict on B.13: the requested implication is correct and admits a short paper proof. I recommend promoting it to a separate lemma. The strongest useful consequence of B.13a is the sufficient condition (19). It is important not to claim that the dimension estimate alone always yields a non-covering result: the base-locus term must first be eliminated.

# IV. Confirmation of B.13a

The five claims in §II.3 are correct, with the standard nondegeneracy condition \\(k=\dim K\geq1\\) when referring to \\(\mathbb P(K)\\).

I will verify them explicitly.

## IV.1. Closedness of \\(\mathfrak I\\)

The condition

\\[ z\wedge(\alpha x-\beta Ax)=0 \\]

is a collection of homogeneous polynomial equations in the projective coordinates of \\(x,z,\alpha,\beta\\).

Therefore \\(\mathfrak I\\) is a closed algebraic subset of

\\[ \mathbb P(V)\times\mathbb P(K)\times\mathbb P^1. \\]

This is the correct way to establish closedness. One should not first remove the base locus or impose an open restriction and then assert that the resulting projection is closed. The full incidence variety is closed; its relevant strata can subsequently be treated separately.

## IV.2. Fibers outside \\(\mathcal B\\)

Fix

\\[ ([x],[\alpha:\beta])\notin\mathcal B. \\]

Then

\\[ P\_{\alpha,\beta}x\ne0. \\]

The fiber in the \\(z\\)-coordinate consists of projective points satisfying

\\[ z\wedge P\_{\alpha,\beta}x=0. \\]

For nonzero vectors, vanishing of the wedge product is equivalent to linear dependence. Hence \\(z\\) must be proportional to \\(P\_{\alpha,\beta}x\\).

There are two possibilities:

- If \\(P\_{\alpha,\beta}x\notin K\\), there is no such projective \\(z\in\mathbb P(K)\\), so the fiber is empty.
- If \\(P\_{\alpha,\beta}x\in K\\), there is exactly one such projective point:\
  \\[\
  [z]=[P\_{\alpha,\beta}x].\
  \\]

Therefore every fiber outside \\(\mathcal B\\) has dimension at most zero.

## IV.3. Fibers over \\(\mathcal B\\)

If

\\[ P\_{\alpha,\beta}x=0, \\]

then

\\[ z\wedge P\_{\alpha,\beta}x=0 \\]

for every \\(z\in K\\).

The fiber is consequently all of \\(\mathbb P(K)\\), of dimension \\(k-1\\).

Thus the fiber dimension is exactly \\(k-1\\) over every point of \\(\mathcal B\\).

## IV.4. The total dimension estimate

The base parameter space is

\\[ \mathbb P(V)\times\mathbb P^1, \\]

whose dimension is

\\[ (v-1)+1=v. \\]

Stratify the incidence variety into the part lying over the complement of \\(\mathcal B\\) and the part lying over \\(\mathcal B\\).

Over the complement of \\(\mathcal B\\), all fibers have dimension at most zero, giving the bound

\\[ \dim\mathfrak I\_{\mathrm{off}\ \mathcal B}\leq v. \\]

Over \\(\mathcal B\\), all fibers have dimension \\(k-1\\), giving

\\[ \dim\mathfrak I\_{\mathrm{over}\ \mathcal B} \leq \dim\mathcal B+k-1. \\]

Taking the maximum,

\\[ \boxed{ \dim\mathfrak I \leq \max\\{v,\dim\mathcal B+k-1\\}. } \\]

If \\(\mathcal B=\varnothing\\), only the first stratum remains, so

\\[ \boxed{\dim\mathfrak I\leq v.} \\]

Verdict: B.13a is correct as stated, subject to the ordinary projective-dimension conventions. I would accept it as a complete paper lemma.

# V. D.1 — The \\(\gamma,\beta,\sigma\\) correction construction

The equations in §II.3 contain a valid and useful cancellation mechanism. However, I would distinguish that local algebraic mechanism from the full proof of the recursive identity.

The supplied fragment gives

\\[ \widehat\pi\Phi(\gamma c)=c, \tag{20} \\]

\\[ U'.\mathrm{mkQ}(\beta u) = U'.\mathrm{mkQ}(\widehat\pi\Phi(su)), \tag{21} \\]

and

\\[ \sigma=-\gamma\circ\beta. \tag{22} \\]

The proposed lift is

\\[ U= \operatorname{span} \bigl(T\cup\\{su+\sigma(u):u\in U'\\}\bigr). \tag{23} \\]

## V.1. The central cancellation identity

Assume the maps have the types suggested by the equations:

- \\(\gamma\\) is defined on the space containing \\(\beta(u)\\);
- \\(\widehat\pi\Phi\\) is linear on the relevant subspace;
- \\(\beta(u)\\) belongs to the domain of \\(\gamma\\);
- the quotient map \\(U'.\mathrm{mkQ}\\) has kernel \\(U'\\).

Then, for \\(u\in U'\\),

\\[ \begin{aligned} \widehat\pi\Phi(su+\sigma(u)) &=\widehat\pi\Phi(su-\gamma(\beta(u)))\\\ &=\widehat\pi\Phi(su)   -\widehat\pi\Phi(\gamma(\beta(u)))\\\ &=\widehat\pi\Phi(su)-\beta(u), \end{aligned} \tag{24} \\]

where the final equality uses (20).

On the other hand, (21) says

\\[ \widehat\pi\Phi(su)-\beta(u)\in U'. \tag{25} \\]

Therefore

\\[ \boxed{ \widehat\pi\Phi(su+\sigma(u))\in U'. } \tag{26} \\]

This is exactly the intended correction: the term \\(\sigma(u)\\) cancels the component of \\(\widehat\pi\Phi(su)\\) that would otherwise obstruct quotient feasibility.

So the central algebraic idea is sound.

## V.2. The dimension estimate

Suppose \\(u\mapsto su+\sigma(u)\\) is linear. Then its image has dimension at most \\(\dim U'\\). Since \\(U\\) is generated by \\(T\\) together with this image,

\\[ \dim U \leq \dim T+\dim U'. \tag{27} \\]

This inequality does not require the map \\(u\mapsto su+\sigma(u)\\) to be injective. It follows simply because the dimension of the image of a linear map cannot exceed the dimension of its domain.

Thus the proposed dimension bound is justified once the linearity and domain assumptions are in place.

## V.3. What remains to be checked before accepting the recursive identity

The cancellation identity (26) is not by itself the whole lifting proof.

For the recursive equality, the paper must still verify:

1. Type correctness: the domains and codomains of \\(s,\beta,\gamma,\sigma,\widehat\pi\Phi\\) must make (20)–(24) meaningful.
2. Linearity: \\(\sigma\\) and the map \\(u\mapsto su+\sigma(u)\\) must be linear.
3. Containment of the prescribed subspace: the lifted \\(U\\) must contain the original \\(S\\) and satisfy any required containment of \\(T\\).
4. Feasibility on \\(T\\): the generators in \\(T\\) must satisfy the relevant quotient feasibility condition, not merely the generators of the form \\(su+\sigma(u)\\).
5. Feasibility on all of \\(U\\): because the constraint is linear, checking it on the generators is sufficient, but the paper must explicitly make that reduction.
6. Dimension comparison: the quotient minimizer \\(U'\\) must be finite-dimensional and the construction must use a linear map from \\(U'\\) to the lifted space.

The available excerpt does not provide all definitions needed to verify these six points. Therefore my conclusion is:

- The \\(\gamma\\)-equation and \\(\beta\\)-equation give the right cancellation mechanism.
- The definition \\(\sigma=-\gamma\circ\beta\\) is algebraically appropriate.
- The dimension estimate follows from linearity.
- The full recursive equality is not yet confirmed solely from these equations.

I would retain D.1's direct lower-bound theorem as proved, but keep the recursive identity marked as requiring the complete type and feasibility verification. This is consistent with the distinction already made in the earlier review.

# VI. L3 accounting — a distinction between mathematical proof and formal verification

This is primarily a question of maintaining a consistent acceptance standard.

The report defines:

- L4: Lean covers the literal statement.
- L3: the paper proof is reviewed or supported by a trustworthy reference, and the nontrivial part has Lean-kernel coverage.
- L2: the paper proof is acceptable, but there is no Lean coverage.
- L1: self-checking or experimental support only.

It also explicitly says that only L3 and L4 count as completed proofs.&#x20;

28_open_items_and_requests.md



Under that definition, the answer is straightforward:

\\[ \boxed{\text{A mathematically accepted paper proof without the required Lean coverage is L2, not L3.}} \\]

This does not mean that the theorem is mathematically doubtful. It means that it has not met the project's chosen verification standard.

## VI.1. The four individual cases

| Item | Mathematical status                                       | Formalization gap                                                       | Recommended status |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------ |
| B.4  | Paper argument accepted; dual-pairing proof available     | The corrected (P) statement lacks the required Lean kernel proof        | L2                 |
| B.10 | Mathematical factorization and spectral argument accepted | Domainity/invertibility assertion lacks Lean coverage                   | L2                 |
| B.14 | Sufficient projection-pencil condition accepted           | Construction of the projection pencil lacks Lean coverage               | L2                 |
| B.24 | Intrinsic partial-map criterion accepted                  | Well-definedness and partial-eigenvector equivalence lack Lean coverage | L2                 |

There is one qualification. If an item already has Lean coverage for its genuinely nontrivial core, and the remaining paper-only part is a routine bridge that is explicitly accepted under the L3 definition, then L3 may be justified. But that is not what the present gap descriptions establish.

In particular, the B.4 report explicitly identifies the missing Lean kernel for the corrected (P) version. For B.10, B.14, and B.24, the stated missing formalization concerns a substantive component of the corresponding result. On the evidence supplied, I would not upgrade any of these four items.

## VI.2. A recommended improvement to the ledger

I suggest separating two dimensions of status rather than trying to make one level encode both mathematical confidence and formalization coverage.

For example:

| Dimension           | Possible values                                                                                                                    |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Mathematical status | M0: unproved; M1: experimental evidence; M2: paper proof drafted; M3: paper proof independently checked; M4: established reference |
| Formal status       | F0: none; F1: auxiliary lemmas; F2: nontrivial core formalized; F3: literal theorem formalized                                     |

Then the existing L-level can be derived from the pair \\((M,F)\\).

For example:

- B.4 could be \\((M3,F1)\\): mathematically accepted, but its corrected target theorem is not yet formalized.
- B.8 could be \\((M3,F1)\\) once the gcd/Bézout paper proof is fully written, while its formalization remains incomplete.
- B.13a could be \\((M3,F2)\\) if its nontrivial dimension argument is indeed covered by Lean.
- B.13b, the coverage lemma, should be tracked separately from B.13a until its paper proof and any required Lean coverage are complete.

This would prevent a misleading situation in which a mathematically established theorem is described as though it were mathematically unresolved merely because its Lean formalization is unfinished.

It also makes the project more auditable: a reader can see precisely whether a gap is mathematical, formal, or both.

# VII. Consolidated recommendations

I would now make the following changes to the project plan.

| Item  | Recommendation                                                | Next concrete action                                                            |
| ----- | ------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| B.4   | Retain abstract duality formulation                           | Define annihilator directly in \\(E\\); prove the four lemmas in §I.2           |
| B.8   | Avoid Smith normal form                                       | Formalize finite-family polynomial gcd and Bézout first                         |
| B.13a | Accept as complete                                            | Preserve the base-locus stratification and dimension bound                      |
| B.13b | Accept the paper implication                                  | Prove \\(\dim\mathfrak I\<k-1\Rightarrow\\) non-surjective projection           |
| B.13c | State the useful sufficient condition                         | Use \\(\mathcal B=\varnothing\\) and \\(v\<k-1\\)                               |
| D.1   | Accept the cancellation mechanism, not yet the full recursion | Write all map types and verify feasibility on every generator                   |
| B.10  | Keep at L2                                                    | Formalize the domainity/invertibility step                                      |
| B.14  | Keep at L2                                                    | Formalize the projection-pencil construction                                    |
| B.24  | Keep at L2                                                    | Formalize \\(\Phi\\)'s well-definedness and the partial-eigenvector equivalence |

## Priority order

My suggested order is:

First: B.13b. This is the quickest mathematical completion. It has a short, clean proof and closes the most visible paper-level gap.

Second: B.4. The abstract pairing route is conceptually clean. It should be possible to isolate the only genuinely difficult point—dual separation of points—and reuse the resulting annihilator API elsewhere.

Third: B.8. The gcd/Bézout approach is the right long-term route. I would first prove the polynomial lemma independently of matrices, then instantiate it for maximal minors.

Fourth: D.1. Complete the type and generator checks before spending time on additional Lean infrastructure. A formally elegant \\(\sigma\\)-construction is not enough unless the lifted subspace is shown to satisfy the exact original feasibility condition.

B.10, B.14, and B.24 can then be treated as focused formalization tasks. They should not be allowed to obscure the mathematical completion of B.13 or the reusable algebraic infrastructure for B.4 and B.8.

## Final assessment

The most important mathematical conclusion from this report is that B.13 is now much closer to completion than its current status suggests. B.13a is sound, and the missing coverage step follows from a standard dimension-of-image argument. The resulting sufficient condition is particularly transparent:

\\[ \boxed{ \mathcal B=\varnothing,\quad v\<k-1 \quad\Longrightarrow\quad \exists[z]\in\mathbb P(K) \text{ avoiding the entire incidence family}. } \\]

For B.4 and B.8, I would not recommend changing the underlying mathematics to accommodate the current Lean library gaps. In both cases there is a direct proof architecture that avoids the problematic machinery:

- B.4: evaluation pairing and annihilators in the original vector space;
- B.8: finite-family gcd, Bézout identity, and algebraic closedness.

Finally, I agree with the report's insistence that experimental evidence should not count as proof. I would apply the same rigor to the formalization ledger: a paper proof can be mathematically complete while still being L2 under the project's chosen standard. Keeping those two statements separate will make the final research account considerably more precise.