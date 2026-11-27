# Mathematical review of `30_conventions_and_open_questions.md`

The most important issue in this report is Question 1. I would resolve it before undertaking any further computation or revising the unified theorem.

My principal conclusion is that the correct domain of the partial-eigenvector obstruction is \\(W_0=\mathcal L(V\cap K)\\), not \\(W=\mathcal LV\\), provided the map is defined through the identity on \\(V_0\\) in the report.

There is, however, a subtle distinction between two constructions of \\(\Phi\\). The report has correctly identified that they agree on \\(W_0\\), but that does not establish that the larger-domain construction gives the same spectral criterion.

I will distinguish the conclusions that follow rigorously from the supplied identities from the additional statements that require a proof.

The seven questions deserve different levels of confidence:

| Question                                 | Assessment                                                               |
| ---------------------------------------- | ------------------------------------------------------------------------ |
| Q1: Correct domain of \\(\Phi\\)         | \\(W_0\\) for the stated kernel-based construction                       |
| Q2: Equivalence of \\((\ast)\\) and (5a) | Yes, under the stated finite-dimensional row-space interpretation        |
| Q3: Third AVOID interface                | Yes: finite elementary divisors and determinantal divisors               |
| Q4: Improve lower bounds                 | Possible, but requires joint optimization rather than separate minima    |
| Q5: Degenerate cases                     | Several additional cases need explicit treatment                         |
| Q6: Novelty of unified theorem           | Structural contribution, not a new order-existence characterization      |
| Q7: Publication strategy                 | Publish the structural results without waiting for complexity resolution |

The most important recommendation is to separate the two partial-map constructions and rebuild the unified theorem with the correct domain.

# 1. Question 1 — What is the correct domain: \\(W\\) or \\(W_0\\)?

## 1.1 First distinguish the two constructions

Your report contains two possible definitions.

The first is

\\[ \Phi\_\Lambda(w)=\Lambda w,\qquad w\in W. \\]

The second is

\\[ \Phi_0(\mathcal Lv)=\mathcal LAv, \qquad v\in V_0:=V\cap K. \\]

These are different constructions.

The first uses the matrix identity

\\[ \mathcal LA = \Lambda\mathcal L+G_0C+G_1CA. \tag{\*} \\]

The second uses the restriction of the original action to the subspace

\\[ V_0=V\cap\ker[C;CA]. \\]

The distinction is not merely notational.

For the first construction, the domain is naturally

\\[ W=\mathcal LV. \\]

For the second, the domain is naturally

\\[ W_0=\mathcal LV_0. \\]

The identity \\((\ast)\\) proves that the two constructions agree on \\(W_0\\), but does not prove that the partial eigenvector criterion on \\(W\\) is equivalent to the original condition (5b).

## 1.2 Why \\(W_0\\) is the correct domain for the kernel-based criterion

Write

\\[ Q\_{\mathcal L}(\lambda) = \begin{bmatrix} \lambda\mathcal L-\mathcal LA\\\ CA\\\ C \end{bmatrix}. \\]

A column vector \\(v\in\mathbb C^n\\) belongs to its kernel precisely when

\\[ \mathcal Lv\lambda-\mathcal LAv=0, \\]

\\[ CAv=0, \\]

and

\\[ Cv=0. \\]

Equivalently,

\\[ v\in V_0, \qquad \mathcal LAv=\lambda\mathcal Lv. \\]

Thus

\\[ \boxed{ \ker Q\_{\mathcal L}(\lambda) = \\{v\in V_0:\mathcal LAv=\lambda\mathcal Lv\\}. } \tag{1} \\]

This identity is the decisive observation.

It means that every finite rank-drop vector of the original pencil comes from \\(V_0\\), not from arbitrary \\(V\\).

Moreover, if \\(v\in V_0\\) and \\(\mathcal Lv=0\\), then

\\[ \mathcal LAv=0 \\]

under (5a).

Therefore, the map

\\[ \Phi_0:W_0\longrightarrow\mathbb C^q, \qquad \Phi_0(\mathcal Lv)=\mathcal LAv \tag{2} \\]

is well-defined.

Indeed, if

\\[ \mathcal Lv_1=\mathcal Lv_2, \\]

then \\(v_1-v_2\in V_0\\) and

\\[ \mathcal L(v_1-v_2)=0. \\]

Condition (5a) gives

\\[ \mathcal LA(v_1-v_2)=0. \\]

Hence

\\[ \mathcal LAv_1=\mathcal LAv_2. \\]

Now (1) gives

\\[ \boxed{ (5b)\text{ fails} \iff \exists\\,0\ne w\in W_0: \Phi_0(w)=\lambda w \text{ for some }\lambda\in\mathbb C. } \tag{3} \\]

There is one detail worth making explicit: if \\(w=0\\), the corresponding \\(v\\) can belong to the permanent kernel. Such a vector does not produce a rank drop beyond the normal rank. This is why the nonzero condition on \\(w\\) is essential.

Thus the correct partial-eigenvector domain for this construction is unambiguously \\(W_0\\).

## 1.3 The dimension of \\(W_0\\)

There is an additional useful identity that should be included in the paper.

The kernel of the restriction

\\[ \mathcal L|\_{V_0}:V_0\longrightarrow\mathbb C^q \\]

is

\\[ \ker(\mathcal L|\_{V_0}) = V\cap K\cap\ker\mathcal L. \\]

Since

\\[ V=\operatorname{row}[\mathcal L;C]^{\mathsf T}, \\]

we have

\\[ V^\perp=\ker[\mathcal L;C]. \\]

Consequently,

\\[ V\cap\ker\mathcal L = V\cap V^\perp =:S. \\]

Because \\(S\subseteq K\\), it follows that

\\[ \ker(\mathcal L|\_{V_0})=S. \\]

Therefore,

\\[ \boxed{ \dim W_0=\dim V_0-\dim S. } \tag{4} \\]

This is useful for determining the degree of the maximal minors in the correct rectangular pencil.

It also clarifies why the earlier \\(W=\mathcal LV\\) formulation can be misleading: its dimension is \\(\rho\\), whereas the correct partial-eigenvector pencil has column dimension

\\[ \dim V_0-\dim S. \\]

There is no general reason for these two dimensions to coincide.

## 1.4 What happens to the \\(\Lambda\\)-based construction?

From \\((\ast)\\), for \\(v\in V_0\\),

\\[ \Lambda\mathcal Lv = \mathcal LAv. \\]

Thus

\\[ \Phi\_\Lambda|\_{W_0}=\Phi_0. \\]

But the existence of an eigenvector in \\(W\\) is a different question:

\\[ \exists\\,0\ne w\in W: \Lambda w=\lambda w. \\]

There may be vectors in \\(W\setminus W_0\\) satisfying this condition.

Such vectors do not necessarily correspond to kernel vectors of \\(Q\_{\mathcal L}(\lambda)\\), because they need not satisfy the two additional equations

\\[ Cv=0,\qquad CAv=0. \\]

Therefore, an eigenvector of \\(\Lambda|\_W\\) can be spurious relative to (5b).

The correct conclusion is:

\\[ \boxed{ \text{The full-domain eigenvector condition is not justified by }(\*). } \\]

It may be equivalent under additional assumptions, but those assumptions must be stated and proved.

## 1.5 Recommended corrected four-way equivalence

I recommend replacing the existing statement with the following.

Recommended corrected formulation

Theorem — Kernel-based partial-eigenvector characterization

Assume (5a), and set

\\[ V_0=V\cap\ker[C;CA], \qquad S=V\cap\ker\mathcal L, \qquad W_0=\mathcal LV_0. \\]

Define

\\[ \Phi_0(\mathcal Lv)=\mathcal LAv, \qquad v\in V_0. \\]

Let \\(\iota_0:W_0\hookrightarrow\mathbb C^q\\) be inclusion.

Then:

\\[ \begin{aligned} (5b) &\iff \ker Q\_{\mathcal L}(\lambda)=S      \quad\forall\lambda\in\mathbb C\\\ &\iff \ker(\lambda\iota_0-\Phi_0)=\\{0\\}      \quad\forall\lambda\in\mathbb C\\\ &\iff \nexists\\,0\ne w\in W_0: \Phi_0(w)\in\mathbb Cw\\\ &\iff \gcd\\{\text{maximal minors of } \lambda\iota_0-\Phi_0\\}\in\mathbb C^\times. \end{aligned} \\]

The first equivalence uses the permanent kernel \\(S\\), and the final equivalence uses the one-variable determinantal-divisor criterion.

One qualification: the displayed permanent-kernel identity must be verified from your precise definitions and B.17. The kernel calculation above proves that \\(S\\) is contained in every kernel. The equality of the kernel with \\(S\\) is precisely the spectral injectivity requirement, not an automatic consequence of (5a).

This distinction is important for the formal statement.

# 2. Question 2 — Is the existence of \\((\Lambda,G_0,G_1)\\) equivalent to (5a)?

Here the answer is affirmative, under exactly the definitions in the report.

This is an important point because it establishes that the two constructions of \\(\Phi\\) are not based on different assumptions concerning admissibility.

## 2.1 Proof of equivalence

Recall that (5a) is

\\[ \operatorname{rank} \begin{bmatrix} \mathcal LA\\\ \mathcal L\\\ CA\\\ C \end{bmatrix} = \operatorname{rank} \begin{bmatrix} \mathcal L\\\ CA\\\ C \end{bmatrix}. \\]

Equality of these row ranks is equivalent to

\\[ \operatorname{row}(\mathcal LA) \subseteq \operatorname{row} \begin{bmatrix} \mathcal L\\\CA\\\C \end{bmatrix}. \\]

Consequently, there exist matrices \\(\Lambda,G_0,G_1\\) such that

\\[ \boxed{ \mathcal LA = \Lambda\mathcal L+G_0C+G_1CA. } \\]

Conversely, if this identity holds, every row of \\(\mathcal LA\\) belongs to the row space of the matrix on the right. Therefore (5a) follows.

We have proved

\\[ \boxed{ (5a) \iff \exists(\Lambda,G_0,G_1)\text{ satisfying }(\*). } \tag{5} \\]

No full-row-rank assumption on \\(\mathcal L\\) is needed.

No uniqueness of \\(\Lambda,G_0,G_1\\) is needed either.

## 2.2 Independence of the choice of extension

Suppose two triples satisfy

\\[ \mathcal LA = \Lambda_1\mathcal L+G\_{01}C+G\_{11}CA \\]

and

\\[ \mathcal LA = \Lambda_2\mathcal L+G\_{02}C+G\_{12}CA. \\]

Subtracting,

\\[ (\Lambda_1-\Lambda_2)\mathcal L + (G\_{01}-G\_{02})C + (G\_{11}-G\_{12})CA=0. \\]

For \\(v\in V_0\\), we have \\(Cv=CAv=0\\). Hence

\\[ (\Lambda_1-\Lambda_2)\mathcal Lv=0. \\]

Thus

\\[ \boxed{ \Lambda_1|\_{W_0}=\Lambda_2|\_{W_0}. } \\]

This establishes an important intrinsic property:

Although the matrix \\(\Lambda\\) is not necessarily unique, its restriction to \\(W_0\\) is uniquely determined.

Therefore the partial map

\\[ \Phi_0:W_0\longrightarrow\mathbb C^q \\]

is intrinsic to the original data and does not depend on the chosen extension.

This is stronger than simply saying that the partial map is well-defined.

## 2.3 What should happen to B.24?

I recommend retaining B.24, but changing its domain from \\(W\\) to \\(W_0\\).

The corrected result is:

\\[ \boxed{ (5b)\text{ fails} \iff \exists\\,0\ne w\in W_0: \Phi_0(w)\in\mathbb Cw. } \\]

The extension matrix \\(\Lambda\\) can still be used for computation, because

\\[ \Phi_0=\Lambda|\_{W_0}. \\]

This is a particularly clean resolution:

- (5a) guarantees the existence of the extension.
- The extension is nonunique on the entire ambient space.
- Its restriction to \\(W_0\\) is unique.
- The spectral obstruction depends only on that restriction.

I would make this the definitive convention in the paper.

# 3. Question 3 — Is there a third AVOID interface?

Yes. I recommend developing a finite-elementary-divisor interface, supplemented by a determinantal-divisor certificate.

In fact, this is more directly connected to the actual rank condition than the incidence-variety method.

## 3.1 The finite-elementary-divisor interface

Let

\\[ Q(\lambda)=Q\_{\mathcal L}(\lambda) \\]

and suppose its normal rank is \\(h\\).

Under (5a), your B.6 establishes:

1. All right minimal indices are zero.
2. All infinite elementary divisors have degree one.
3. The total degree of the infinite elementary divisors is

\\[ d\_\infty=h-\operatorname{rank}\mathcal L. \\]

The remaining spectral structure is therefore encoded in the finite elementary divisors.

In particular, under these hypotheses,

\\[ \boxed{ (5b)\iff d\_{\mathrm{fin}}=0. } \tag{6} \\]

This is an exact criterion, rather than merely a sufficient infeasibility condition.

That makes it attractive as a third interface.

## 3.2 Why it is stronger than an incidence-dimension condition

Compare the three approaches:

| Interface       | Mathematical object            | Character                      |
| --------------- | ------------------------------ | ------------------------------ |
| F.1             | Quotient rank \\(r(\lambda)\\) | Necessary condition            |
| B.13            | Incidence projection           | Sufficient geometric condition |
| Finite divisors | Kronecker/Smith structure      | Exact spectral criterion       |

The third approach has an important advantage: it does not require the empty-base-locus hypothesis of B.13c.

It also does not require proving a dimension inequality for an incidence variety.

Instead, it directly measures whether the pencil has finite spectral obstructions.

## 3.3 A particularly useful formulation through the determinantal divisor

Let

\\[ \Delta_h(\lambda) = \gcd\\{\text{all }h\times h\text{ minors of }Q(\lambda)\\}. \\]

Then

\\[ (5b) \iff \Delta_h(\lambda)\in\mathbb C^\times. \\]

Equivalently,

\\[ d\_{\mathrm{fin}}=0. \\]

This gives a chain of equivalences:

\\[ \boxed{ (5b) \iff d\_{\mathrm{fin}}=0 \iff \Delta_h(\lambda)\text{ is constant}. } \\]

The advantage is that it connects the original pencil directly to an algebraic invariant.

## 3.4 How to use this in the AVOID problem

For a fixed augmentation \\(\mathcal L\\), the criterion is computable.

For the family of admissible augmentations, the problem becomes

\\[ \exists R: \quad (5a) \quad\land\quad \Delta_h(\lambda;R)\in\mathbb C^\times. \\]

This is an exact parameterized determinantal-divisor problem.

It is important not to overstate the computational conclusion: computing \\(\Delta_h\\) for a fixed \\(R\\) does not immediately give a polynomial-time method for finding \\(R\\).

Nevertheless, it gives a better formulation of AVOID.

## 3.5 A further improvement: a bounded Bézout certificate

There is an especially useful algebraic formulation.

Suppose the maximal minors are

\\[ p_1(\lambda;R),\ldots,p_N(\lambda;R). \\]

Then

\\[ \Delta_h(\lambda;R)\in\mathbb C^\times \\]

if and only if there exist polynomials \\(u_i(\lambda)\\) such that

\\[ \boxed{ \sum\_{i=1}^{N}u_i(\lambda)p_i(\lambda;R)=1. } \tag{7} \\]

Because the minors have bounded degree, the Bézout multipliers can be chosen with bounded degree.

For example, if all nonzero \\(p_i\\) have degree at most \\(D\\), a common-gcd-one family admits a Bézout representation with multiplier degrees bounded by a quantity polynomial in \\(D\\) and \\(N\\). More precisely, one can first take a nonzero polynomial \\(p_j\\), compute the gcd successively with the remaining polynomials, and use the two-polynomial Bézout degree bounds at each step.

This converts the spectral avoidance condition into a finite system of coefficient equations.

If the coefficients of \\(p_i\\) are polynomial functions of the augmentation parameters, (7) gives a direct existential-real formulation.

This is a useful alternative to encoding the condition through chart-specific rank tests.

### My recommendation

Retain all three interfaces, but assign them different purposes:

- F.1 for cheap necessary layer elimination.
- B.13 for geometric sufficient infeasibility.
- Finite divisors/Bézout for exact algebraic characterization.

This is a much more complete AVOID framework.

# 4. Question 4 — Can the lower bound for \\(q\_{\min}\\) be improved?

Your current lower bound is

\\[ q\_{\min} \ge \max\left\\{ r+\varepsilon,\\, \rho+\max(c_0,1) \right\\}. \tag{8} \\]

My assessment is that the current lower bound is structurally sound, but it may be weaker than necessary because it combines several independently minimized quantities.

The most promising improvement is to exploit their joint dependence.

## 4.1 The problem with separate minimization

Suppose the admissible augmentation is parameterized by some object \\(U\\), and the order decomposition is

\\[ q(U)=\rho(U)+c(U). \\]

The separate bounds may be obtained from

\\[ \rho(U)\ge \rho\_{\min}, \qquad c(U)\ge c\_{\min}. \\]

Then

\\[ q(U)\ge\rho\_{\min}+c\_{\min}. \\]

This is valid.

But it may be weak if the configurations minimizing \\(\rho(U)\\) and \\(c(U)\\) are incompatible.

The actual minimum is

\\[ \min\_{U\in\mathfrak F} \\{\rho(U)+c(U)\\}, \\]

where \\(\mathfrak F\\) is the admissible family.

In general,

\\[ \min_U(\rho(U)+c(U)) \ge \min_U\rho(U)+\min_U c(U). \\]

The inequality can be strict.

This suggests defining the joint feasible profile

\\[ \mathfrak P = \\{(\rho(U),c(U)):U\in\mathfrak F\\}. \\]

Then

\\[ \boxed{ q\_{\min} = \min\_{(\rho,c)\in\mathfrak P} (\rho+c) } \\]

before imposing the additional spectral condition.

The spectral condition further restricts the profile to

\\[ \mathfrak P\_{\mathrm{spec}} = \\{(\rho(U),c(U)):U\in\mathfrak F,\ (5b)\\}. \\]

Hence

\\[ \boxed{ q\_{\min} = \min\_{(\rho,c)\in\mathfrak P\_{\mathrm{spec}}} (\rho+c). } \tag{9} \\]

This is a more precise optimization formulation than the additive lower bound.

## 4.2 A stronger lower-bound strategy

I would introduce the function

\\[ c\_{\min}(\rho) = \min\\{c(U):U\in\mathfrak F,\ \rho(U)=\rho\\}, \\]

with value \\(+\infty\\) if no such \\(U\\) exists.

Then

\\[ q\_{\min} \ge \min\_\rho \\{\rho+c\_{\min}(\rho)\\}. \\]

The current bound uses a global minimum of \\(c\\), whereas this function retains the dependence on \\(\rho\\).

It can be strictly stronger.

For example, suppose the possible pairs are

\\[ \mathfrak P=\\{(2,5),(3,2),(4,1)\\}. \\]

The separate minima give

\\[ \rho\_{\min}+c\_{\min}=2+1=3. \\]

But the actual minimum of the sum is

\\[ \min\\{7,5,5\\}=5. \\]

This illustrates exactly what is lost by separate minimization.

## 4.3 Add the spectral barrier to the profile

Your F.1 result gives

\\[ \rho\le\min\_\lambda r(\lambda) \\]

for every feasible augmentation.

Therefore, the profile can be restricted to

\\[ \rho\le r\_\*, \qquad r\_\*:=\min\_{\lambda\in\mathbb C}r(\lambda). \\]

Combining the structural and spectral constraints yields

\\[ q\_{\min} \ge \min\_{\substack{\rho\le r\_\*\\\ c\ge c\_{\min}(\rho)}} (\rho+c). \\]

This is a legitimate improvement in the formulation, although it is not yet an explicit stronger numerical bound until \\(c\_{\min}(\rho)\\) is computed or bounded.

## 4.4 A second possible improvement: exploit the permanent kernel

Since

\\[ \dim W_0=\dim V_0-\dim S, \\]

the corrected partial-eigenvector formulation gives an additional structural quantity.

The rectangular pencil

\\[ \lambda\iota_0-\Phi_0 \\]

has

\\[ \dim W_0 \\]

columns.

If \\(W_0\ne0\\), its full-column-rank condition must hold for every finite \\(\lambda\\).

This places restrictions on the possible Kronecker structure.

I would investigate whether these restrictions can be converted into a lower bound involving

\\[ \dim(V\cap K)-\dim S. \\]

I would not assert a universal additive inequality involving this quantity yet. The dimension alone does not determine whether a rectangular pencil has a finite rank-drop point.

The useful direction is to combine it with the dimensions of the image and the relevant quotient.

## 4.5 Is the current bound optimal in general?

I would not assume either optimality or nonoptimality without constructing examples.

A good way to settle this is to construct three families:

1. A family attaining the first term of (8).
2. A family attaining the second term.
3. A family in which the two bounds are individually sharp but cannot be attained simultaneously.

The third family is particularly valuable because it would demonstrate that the current bound loses information through separate minimization.

A general-purpose exact benchmark should record

\\[ (q\_{\min},\rho\_{\min},c\_{\min}, \min\_{\lambda}r(\lambda),d\_{\mathrm{fin}}). \\]

Your existing computational framework should be able to generate such examples.

My recommendation: prioritize the joint-profile approach. It is the most principled way to improve the lower bound without introducing speculative inequalities.

# 5. Question 5 — Which degenerate cases must be treated explicitly?

The four cases listed in the report are important, but I would add several others.

There is a distinction between:

- cases in which the theorem remains true but its formulation becomes vacuous;
- cases in which a dimension or rank formula changes;
- cases in which a projective-geometric argument is no longer applicable;
- cases in which the original problem itself becomes trivial.

I recommend including a dedicated section titled Degenerate and boundary cases.

## 5.1 The cases already identified

### Case 1: \\(K=0\\)

Since

\\[ K=\ker[C;CA], \\]

the condition \\(K=0\\) implies

\\[ \operatorname{rank}[C;CA]=n. \\]

Consequently,

\\[ \operatorname{row}[C;CA]=\mathbb C^n. \\]

Thus

\\[ \mathcal J=\mathbb C^n. \\]

For every \\(\mathcal L\\), the matrix \\(Q\_{\mathcal L}(\lambda)\\) contains a row block \\([CA;C]\\) of rank \\(n\\).

Therefore,

\\[ \operatorname{rank}Q\_{\mathcal L}(\lambda)=n \\]

for every \\(\lambda\\).

Condition (5b) holds automatically.

Also, the incidence space \\(\mathbb P(K)\\) is empty, so B.13 must be interpreted separately.

Recommendation: state this as a trivial-feasibility proposition before the incidence theorem.

### Case 2: \\(V=0\\)

Since

\\[ V=\operatorname{row}[\mathcal L;C]^{\mathsf T}, \\]

this implies

\\[ \mathcal L=0,\qquad C=0. \\]

Then

\\[ Q\_{\mathcal L}(\lambda)=0, \qquad h=0. \\]

Both (5a) and (5b) hold.

The zero-dimensional partial-eigenvector space also gives a vacuous obstruction condition.

This case should be separated because statements involving projective spaces of \\(V\\) or \\(W_0\\) are otherwise undefined.

### Case 3: \\(\operatorname{rank}\mathcal L\<q\\)

This case is particularly important.

Do not assume that

\\[ \operatorname{rank}\mathcal L=q. \\]

The original problem permits redundant rows in \\(\mathcal L\\), and the structural formulas must account for them.

The rank of the pencil's coefficient matrix and the number of rows of \\(\mathcal L\\) are not interchangeable.

In particular, the infinite elementary-divisor formula in B.6 involves

\\[ d\_\infty=h-\operatorname{rank}\mathcal L, \\]

not \\(h-q\\).

This distinction should be preserved throughout.

### Case 4: \\(L_0=0\\)

This is important because the strict inequality in B.9 is explicitly stated under

\\[ L_0\ne0. \\]

When \\(L_0=0\\), some of the boundary arguments may change.

The problem may also admit a simpler augmentation because the fixed-row constraint disappears.

I recommend treating this as a separate special family, rather than silently applying the general lower bounds.

## 5.2 Additional cases I recommend adding

### Case 5: \\(W_0=0\\)

This is one of the most important additions following the correction to Question 1.

If

\\[ W_0=\mathcal L(V\cap K)=0, \\]

then the partial-eigenvector obstruction is automatically absent.

Indeed, there is no nonzero \\(w\in W_0\\).

By the corrected equivalence,

\\[ \boxed{ W_0=0 \Longrightarrow (5b)\text{ holds}. } \\]

This should be a separate corollary.

Notice that \\(W_0=0\\) does not necessarily imply \\(V_0=0\\). It is possible that

\\[ V_0=S. \\]

In that situation, the entire restricted subspace is mapped to zero by \\(\mathcal L\\).

### Case 6: \\(S=0\\)

Here

\\[ S=V\cap\ker\mathcal L=0. \\]

Then \\(\mathcal L|\_V\\) is injective.

Consequently,

\\[ \dim W_0=\dim V_0. \\]

This is the cleanest situation for the partial-eigenvector formulation.

It is also the case in which the distinction between the quotient domain and the original subspace is easiest to manage.

However, do not identify \\(W_0\\) with \\(W\\) merely from \\(S=0\\).

That equality requires

\\[ V_0=V, \\]

or an equivalent condition such as \\(V\subseteq K\\).

The statement in the report that \\(W\\) and \\(W_0\\) coincide when \\(S=0\\) needs correction.

This is an important logical point.

### Case 7: \\(V_0=0\\)

Then

\\[ W_0=0. \\]

Thus (5b) holds automatically.

This case should be stated explicitly because it is stronger and easier to verify than \\(W_0=0\\).

### Case 8: \\(\rho=0\\)

Recall that

\\[ \rho=\dim\pi(V) \\]

in the earlier quotient notation.

The zero-layer case should be treated separately because some arguments involving a nonzero effective pencil or positive-dimensional projective space become vacuous.

Be careful to distinguish this \\(\rho\\) from \\(\dim W_0\\): after correcting the domain, they need not agree.

I recommend using different symbols for the two dimensions throughout the revised paper.

For example,

\\[ \rho_W:=\dim W, \qquad \omega:=\dim W_0. \\]

### Case 9: \\(q=0\\)

If zero-order augmentations are permitted, the empty matrix \\(\mathcal L\\) must be included in the definitions.

This case may be excluded by the prescribed lower bound \\(q\ge r\\) when \\(r>0\\), but it should be addressed if \\(r=0\\).

### Case 10: \\(h=0\\)

This is the completely zero-pencil case.

The definition of normal rank and the convention for the gcd of zero-size minors must be specified.

It is safer to handle this case directly rather than apply the positive-rank determinantal-divisor theorem without qualification.

### Case 11: Empty and zero-dimensional projective spaces

B.13 uses

\\[ \mathbb P(K),\qquad \mathbb P(V). \\]

If either vector space is zero, the corresponding projective space is empty.

The incidence dimension statements should therefore be written under positive-dimension assumptions, followed by explicit empty-space cases.

### Case 12: Infinite spectral parameter

Your original condition (5b) quantifies over finite

\\[ \lambda\in\mathbb C. \\]

It does not require the pencil to have full rank at infinity.

This matters because the pencil may have infinite elementary divisors even when (5b) holds.

Indeed, B.6 predicts precisely such infinite structure.

The paper should distinguish:

\\[ \text{finite rank-drop avoidance} \\]

from

\\[ \text{full projective rank preservation, including infinity}. \\]

These are different properties.

## 5.3 Recommended degenerate-case table

| Condition                              | Consequence                         | Treatment                       |
| -------------------------------------- | ----------------------------------- | ------------------------------- |
| \\(K=0\\)                              | (5b) automatic                      | Separate proposition            |
| \\(V=0\\)                              | Entire pencil zero, \\(h=0\\)       | Separate trivial case           |
| \\(\operatorname{rank}\mathcal L\<q\\) | Redundant augmentation rows         | Retain in general theorem       |
| \\(L_0=0\\)                            | Fixed-row boundary disappears       | Separate special case           |
| \\(V_0=0\\)                            | (5b) automatic                      | Corollary                       |
| \\(W_0=0\\)                            | No partial eigenvector              | Corollary                       |
| \\(S=0\\)                              | Restricted map has no quotient loss | Simplified formula              |
| \\(\rho=0\\)                           | Zero quotient layer                 | Separate layer                  |
| \\(q=0\\)                              | Empty augmentation                  | Boundary case                   |
| \\(h=0\\)                              | Zero pencil                         | Separate convention             |
| \\(K=0\\) or \\(V=0\\) in B.13         | Empty projective factors            | Exclude from dimension argument |
| Infinite elementary divisors           | Not forbidden by (5b)               | Explicit clarification          |

My strongest recommendation: add \\(W_0=0\\), \\(V_0=0\\), and the distinction between \\(S=0\\) and \\(W=W_0\\) to the immediate revision checklist.

# 6. Question 6 — Is the four-way unified statement sufficiently new?

My answer is qualified:

It is a potentially publishable structural contribution, but it should be presented as a structural refinement of the existing existence characterization, not as a new characterization of the minimum-order problem.

This distinction is important.

## 6.1 What the four-way theorem actually establishes

The corrected theorem connects four formulations:

\\[ \begin{aligned} &\text{Original rank condition}\\\ &\quad\Updownarrow\\\ &\text{Quotient-pencil injectivity}\\\ &\quad\Updownarrow\\\ &\text{Absence of a partial eigenvector on }W_0\\\ &\quad\Updownarrow\\\ &\text{Constant maximal-minor gcd}. \end{aligned} \\]

These formulations have different mathematical meanings.

The quotient-pencil formulation identifies the effective vector space after removing the permanent kernel.

The partial-eigenvector formulation identifies the geometric mechanism of failure.

The determinantal-divisor formulation identifies an exact polynomial certificate.

This is more than a change of notation if the results are established independently and the relationship among them is not explicit in the earlier characterization.

## 6.2 What it does not establish

The theorem does not, by itself, give a new description of the set of feasible orders.

It does not replace the existing \\(\exists Z\\) criterion.

Nor does it establish an algorithm for finding a suitable \\(Z\\) or \\(R\\).

The correct distinction is:

| Existing order characterization                                            | Your structural theory                                        |
| -------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Determines whether a given order is feasible through an auxiliary subspace | Explains the spectral obstruction for an admissible candidate |
| Gives a necessary and sufficient existence condition                       | Gives a kernel and partial-eigenvector interpretation         |
| Provides an order spectrum                                                 | Provides spectral and determinantal invariants                |
| Provides an existence construction                                         | Provides fixed-candidate verification criteria                |

Thus, the new work is best positioned as a structural theory of the spectral condition underlying the existing order characterization.

## 6.3 Which results are strongest from a novelty perspective?

My ranking is as follows.

1\. Corrected partial-eigenvector theorem

Strong candidate

The precise domain \\(W_0\\), intrinsic map, and equivalence with rank failure.

2\. Equality obstruction B.22

Strong candidate

A concrete additional impossibility theorem for a boundary order.

3\. Necessary condition B.31

Strong candidate

A nontrivial restriction on the possible intersection dimension.

4\. Rank barrier F.1

Good candidate

An explicit spectral obstruction for admissible layers.

5\. B.17 quotient-kernel theorem

Good candidate

A structural result whose novelty depends on the exact comparison with the existing quotient criterion.

6\. \\(\exists\mathbb R\\) upper bound

Independent contribution

A complexity-theoretic result, subject to a complete encoding proof.

The gcd criterion alone should not be claimed as a new theorem: the one-variable determinantal-divisor principle is standard.

Likewise, the equivalence of (5a) with the existence of \\(\Lambda,G_0,G_1\\) is elementary row-space linear algebra.

Their value is in how they are combined with the problem-specific structural results.

## 6.4 An important novelty issue introduced by the correction to \\(W_0\\)

There is one further point.

Because the earlier B.24 used \\(W\\), but the correct domain is \\(W_0\\), the corrected theorem should not be described as merely a cosmetic revision.

The proof must explicitly show that the quotient-kernel construction and the partial map use the same effective space.

I would formulate the contribution as:

> We identify the precise subspace on which the spectral obstruction acts, prove that the induced partial map is intrinsic, and characterize finite rank loss through its projective eigenvector incidence and determinantal divisor.

That is a much more precise novelty claim.

## 6.5 How to avoid overlap with the existing papers

I recommend including a comparison table in the introduction.

For example:

| Subject                        | Previous characterization                                | Present contribution                         |
| ------------------------------ | -------------------------------------------------------- | -------------------------------------------- |
| Feasible orders                | Necessary and sufficient \\(\exists Z\\) criterion       | Not claimed as new                           |
| Order spectrum                 | Previously established                                   | Used as the algebraic framework              |
| Quotient-pencil representation | Related reformulation                                    | Developed for spectral analysis              |
| Permanent kernel               | Structural analysis                                      | New if not explicitly established previously |
| Partial eigenvectors           | Not claimed to follow automatically from \\(\exists Z\\) | Main structural contribution                 |
| Finite elementary divisors     | Additional pencil analysis                               | Main structural contribution                 |
| Equality obstruction           | Additional infeasibility result                          | New theorem                                  |
| Complexity upper bound         | Separate encoding                                        | Independent contribution                     |

Before making these novelty claims, compare the actual theorem statements and proofs in arXiv:2609.33615 and arXiv:2609.37992, rather than relying only on their abstracts.

I would also explicitly acknowledge the existing papers as the starting point for the order characterization.

# 7. An important correction to the domain argument

There is one additional issue that I need to correct before finalizing the answer to Questions 1–2.

On checking the kernel calculation against the definitions in your note, I found that my earlier conclusion that \\(W_0=\mathcal L(V\cap K)\\) is automatically the correct domain was too quick.

The problem is that the right-kernel equation does not impose \\(v\in V\\).

Indeed,

\\[ Q\_{\mathcal L}(\lambda)v=0 \\]

is equivalent to

\\[ v\in K,\qquad \mathcal LAv=\lambda\mathcal Lv. \tag{10} \\]

It does not, in general, imply

\\[ v\in V\cap K. \\]

This is a significant distinction, and I recommend resolving it before changing the Lean definitions.

## 7.1 The domain obtained directly from the kernel equation

Define

\\[ \boxed{ W_K:=\mathcal L K. } \\]

Under (5a), define

\\[ \boxed{ \Phi_K:W_K\longrightarrow\mathbb C^q, \qquad \Phi_K(\mathcal Lv)=\mathcal LAv,\quad v\in K. } \tag{11} \\]

This map is well-defined.

To see this, suppose \\(v_1,v_2\in K\\) and

\\[ \mathcal Lv_1=\mathcal Lv_2. \\]

Put \\(u=v_1-v_2\\). Then

\\[ \mathcal Lu=0,\qquad Cu=0,\qquad CAu=0. \\]

By (5a),

\\[ \mathcal LAu=0. \\]

Therefore,

\\[ \mathcal LAv_1=\mathcal LAv_2. \\]

Furthermore, from (5),

\\[ \mathcal LAv = \Lambda\mathcal Lv \qquad(v\in K). \\]

Hence

\\[ \boxed{ \Phi_K=\Lambda|\_{W_K}. } \tag{12} \\]

This also proves that \\(\Phi_K\\) is independent of the chosen extension \\(\Lambda\\).

## 7.2 The exact connection with the pencil

For \\(v\in K\\),

\\[ Q\_{\mathcal L}(\lambda)v=0 \iff \Phi_K(\mathcal Lv)=\lambda\mathcal Lv. \\]

Moreover,

\\[ \mathcal Lv=0 \\]

describes the permanent kernel component.

Using the permanent-kernel conclusion of B.17, the appropriate failure criterion is therefore

\\[ \boxed{ (5b)\text{ fails} \iff \exists\\,0\ne w\in W_K: \Phi_K(w)\in\mathbb Cw. } \tag{13} \\]

The corresponding rectangular pencil is

\\[ P_K(\lambda) = \lambda\iota_K-\Phi_K, \qquad \iota_K:W_K\hookrightarrow\mathbb C^q. \\]

Its maximal-minor gcd gives the fixed-candidate criterion.

## 7.3 Where does \\(W_0\\) fit?

Your proposed space is

\\[ W_0=\mathcal L(V\cap K). \\]

Certainly,

\\[ W_0\subseteq W_K. \\]

But equality requires the additional statement

\\[ \boxed{ \mathcal L K=\mathcal L(V\cap K). } \tag{14} \\]

This is not a consequence of the definitions alone.

It may follow from an additional decomposition or quotient-representative lemma in your earlier work, but that lemma must be identified explicitly.

In particular, the condition \\(S=0\\) alone does not establish (14).

This is the precise mathematical issue I would ask the Lean development to check.

## 7.4 What about the earlier domain \\(W=\mathcal LV\\)?

The same issue occurs in the other direction.

Neither

\\[ \mathcal LV \\]

nor

\\[ \mathcal L(V\cap K) \\]

can automatically be identified with \\(\mathcal LK\\).

The correct domain derived directly from the original kernel equation is \\(\mathcal LK\\).

If an earlier quotient construction proves that the image of \\(K\\) can be represented using \\(V\cap K\\), then \\(W_0\\) is an equivalent realization of that domain. But this requires proof.

My revised recommendation for Question 1 is therefore: use \\(W_K=\mathcal LK\\) as the primary definition, and establish (14) as a separate lemma before replacing it by \\(W_0\\).

This is more robust than choosing \\(W_0\\) merely because it appears in the current computation.

It also gives a clean formalization strategy:

1. Prove the kernel identity (10).
2. Prove well-definedness of \\(\Phi_K\\).
3. Prove independence from \\(\Lambda\\).
4. Prove the permanent-kernel quotient statement.
5. Only then prove any equivalence with \\(W_0\\) or another quotient-space representation.

This correction is important enough that I would postpone rerunning the dependent Lean theorems until the underlying domain lemma is settled.

# 8. Question 7 — Should you publish the structural results while complexity remains open?

My recommendation is yes.

I would not make publication conditional on solving the NP-hardness versus polynomial-time dichotomy.

There are three reasons.

## 8.1 The structural results form an independent mathematical contribution

The project has established several types of results that do not depend on resolving the complexity question:

- Quotient-space and kernel structure.
- Restrictions on the finite elementary divisors.
- Exact partial-eigenvector characterization.
- Equality-based infeasibility.
- Necessary conditions on the intersection dimension.
- Geometric coverage criteria.
- A real-algebraic upper-bound formulation.

These are meaningful mathematical results independently of whether the decision problem turns out to be polynomial-time solvable or hard.

A paper need not solve every computational question arising from its structural theory.

## 8.2 Waiting for a complexity classification carries unnecessary risk

Suppose the hardness programme takes another year and produces no reduction.

The structural results would still be valid.

Suppose the polynomial-time programme eventually succeeds.

That would make the paper stronger, but it would not invalidate the value of the structural theory.

Therefore, I would separate the publication objectives.

Paper 1: Structural and spectral theory.

Present the corrected unified theorem, the Kronecker structure, the equality obstruction, the rank barrier, and the necessary feasibility conditions.

Paper 2: Computational complexity.

If a hardness reduction or polynomial algorithm is eventually obtained, develop it as a separate contribution, building on the first paper.

If the results ultimately fit more naturally into one paper, they can be combined. But the structural paper should not be held hostage by an unresolved complexity question.

## 8.3 What I would require before submission

I would impose five conditions:

1. Resolve the domain of the partial map, particularly the relationship between \\(\mathcal LK\\) and \\(\mathcal L(V\cap K)\\).
2. State the permanent-kernel theorem with exact mathematical notation.
3. Complete the novelty comparison with the two existing Fernando papers.
4. Resolve the coefficient-field and degenerate-case conventions.
5. Separate fully machine-checked statements from paper-only proof steps.

Once these are satisfied, I would consider the structural manuscript ready for external mathematical review.

# 9. Revised research priorities

Taking the new convention issue into account, I would change the priorities I proposed in my previous review.

The first priority is now more fundamental.

## Revised research roadmap

1. Resolve the effective domain

   Establish whether

   \\[ \mathcal LK=\mathcal L(V\cap K). \\]

   If not, use \\(\mathcal LK\\) as the primary domain.
2. Prove the intrinsic partial-map theorem

   Define \\(\Phi_K\\) and establish the exact equivalence with (5b), using the permanent-kernel theorem.
3. Reconcile the two pencil representations

   Prove the relationship between the B.17 quotient pencil and

   \\[ \lambda\iota_K-\Phi_K. \\]
4. Recheck the determinantal-divisor results

   Determine the precise dimensions, maximal minors, and degree bounds for the corrected pencil.
5. Complete the infeasibility theory

   Combine F.1, B.13, B.22, B.31, and the finite-elementary-divisor criterion.
6. Develop the complexity programme

   Investigate the parameterized determinantal divisor and the realization problem for admissible partial pencils.

# 10. Specific instructions I would give your Lean verification programme

I would now make the convention problem an explicit verification milestone.

The following are the propositions I would ask the programme to check independently.

| ID | Proposition                                                                           | Purpose                            |
| -- | ------------------------------------------------------------------------------------- | ---------------------------------- |
| L1 | \\((5a)\iff\exists\Lambda,G_0,G_1:(\*)\\)                                             | Establish extension existence      |
| L2 | \\(\Phi_K\\) is well-defined                                                          | Establish intrinsic map            |
| L3 | \\(\Phi_K=\Lambda\|\_{\mathcal LK}\\)                                                 | Establish extension independence   |
| L4 | \\(\ker Q(\lambda)\\) corresponds to partial eigenvectors modulo the permanent kernel | Establish spectral equivalence     |
| L5 | \\(\mathcal LK=\mathcal L(V\cap K)\\)                                                 | Test the proposed domain reduction |
| L6 | \\(\dim\mathcal LK=\dim K-\dim(K\cap\ker\mathcal L)\\)                                | Establish dimension formula        |
| L7 | The determinantal-divisor criterion holds for the corrected rectangular pencil        | Establish algebraic equivalence    |

For L5, I would not ask Lean to prove the proposition under implicit assumptions.

Instead, give it the exact definitions of \\(V,K,\mathcal L\\), and let it either prove the equality or produce a counterexample.

If L5 fails, that is valuable information: it tells us that the earlier \\(W_0\\)-based statement requires modification.

Also, I would explicitly retract one implication from my preceding review: the statement

\\[ W_0=0\Longrightarrow(5b) \\]

is not established until \\(W_0=W_K\\) has been proved. The unconditional statement is

\\[ W_K=0\Longrightarrow(5b), \\]

under the permanent-kernel result.

This is exactly the kind of logical distinction that should be preserved in the formal development.

# 11. Final conclusions

Let me summarize the answers to the seven questions.

| Question | My final recommendation                                                                                                  |
| -------- | ------------------------------------------------------------------------------------------------------------------------ |
| Q1       | Use \\(W_K=\mathcal LK\\) as the primary domain. Prove its equivalence with \\(W_0\\) before using \\(W_0\\).            |
| Q2       | Yes. The extension identity \\((\*)\\) is exactly equivalent to (5a). Its restriction to \\(\mathcal LK\\) is unique.    |
| Q3       | Use finite elementary divisors and the determinantal divisor as the third, exact AVOID interface.                        |
| Q4       | Improve the lower bound through joint optimization of \\((\rho,c)\\), rather than separate minima.                       |
| Q5       | Add \\(W_K=0\\), \\(V_0=0\\), \\(S=0\\), \\(h=0\\), and the finite-versus-infinite spectral distinction.                 |
| Q6       | Present the unified theorem as a new structural spectral characterization, not as a new feasible-order characterization. |
| Q7       | Publish the structural results without waiting for the complexity problem to be resolved.                                |

## My most important advice

There is one mathematical principle I would keep in mind throughout the next stage:

\\[ \boxed{ \text{The domain of a spectral obstruction must be derived from the kernel equation, not guessed from a convenient subspace representation.} } \\]

Your current convention problem is not a minor issue of notation. It determines the dimension of the rectangular pencil, the maximal minors, the determinantal divisor, and potentially the validity of the unified theorem.

I would settle it before any additional computational experiments.

Once that is done, the project will have a much firmer foundation for the structural paper and for the subsequent complexity investigation.

The immediate next task should be a proof or counterexample for

\\[ \boxed{ \mathcal LK=\mathcal L(V\cap K). } \\]

That single result will determine which version of the partial-eigenvector theorem should become the definitive one.