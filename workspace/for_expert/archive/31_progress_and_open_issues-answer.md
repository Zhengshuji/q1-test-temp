# Review of `31_progress_and_open_issues.md`

The report records a substantial and important correction: the spectral map must be defined on \\(W_K=\mathcal LK\\), not on \\(W_0=\mathcal L(V\cap K)\\). The counterexample in Part II.2 means this is not a matter of notation or a harmless choice of quotient. The two spaces can have different dimensions, so any theorem that identifies the spectral pencil with an operator on \\(V/S\\) now needs an explicit comparison map and a proof of what spectral data it preserves.

My main recommendation is to make the next phase structural first, computational second—but not to postpone the determinantal-divisor route. The exact \\(\Delta_h\\) criterion is a valuable independent route to a finite algebraic encoding. The structural work should now focus on reconciling the two pencils without assuming they are equivalent.

I will address the five questions in order, distinguishing conclusions that follow from the stated setup from claims that need additional hypotheses.

## 1. The Kronecker accounting identity and reversal

There is an important issue to resolve before choosing a reference or debugging the script: the identity in Question 1 is not the general rectangular-pencil identity unless left minimal indices are absent.

Let

\\[ Q(\lambda)=Q_0+\lambda Q_1\in\mathbb C[\lambda]^{m\times n} \\]

have normal rank \\(h\\). In its Kronecker canonical form, write:

- \\(\epsilon_1,\ldots,\epsilon\_{n-h}\\) for the right minimal indices;
- \\(\eta_1,\ldots,\eta\_{m-h}\\) for the left minimal indices;
- \\(d\_{\mathrm{fin}}\\) for the total size of all finite regular elementary-divisor blocks;
- \\(d\_\infty\\) for the total size of all infinite elementary-divisor blocks.

Then the rank accounting is

\\[ \boxed{ h= \sum_j\epsilon_j+ \sum_i\eta_i+ d\_{\mathrm{fin}}+ d\_\infty. } \tag{1} \\]

The reason is transparent block by block. A right singular block of index \\(\epsilon\\) has normal rank \\(\epsilon\\); a left singular block of index \\(\eta\\) has normal rank \\(\eta\\); and a regular finite or infinite block contributes its full size. Adding these contributions gives (1).

Thus the proposed identity

\\[ h=\sum_j\epsilon_j+d\_{\mathrm{fin}}+d\_\infty \\]

is valid if the pencil has no left minimal indices—equivalently, if it has full row normal rank \\(m=h\\). It is also valid under any separately established condition that makes the sum of the left minimal indices zero. But it should not be presented as the unrestricted rectangular identity.

This distinction matters for your pencil, whose row count is \\(q+2p\\), while its normal rank need not equal \\(q+2p\\).

### 1.1 What is \\(d\_\infty\\)?

A coordinate-free way to define the finite and infinite contributions is through homogeneous regular structure.

Homogenise the pencil:

\\[ Q^{\mathrm h}(\alpha,\beta)=\alpha Q_1+\beta Q_0. \\]

The affine parameter \\(\lambda\\) corresponds to \\([\alpha:\beta]=[\lambda:1]\\). The point at infinity is \\([1:0]\\). The regular part of the pencil has elementary divisors supported at points of the projective line:

- finite elementary divisors are supported at \\([\lambda_0:1]\\);
- infinite elementary divisors are supported at \\([1:0]\\).

The total sizes of the corresponding regular blocks are \\(d\_{\mathrm{fin}}\\) and \\(d\_\infty\\), respectively. This definition is independent of a particular reversal convention.

For a degree-one pencil, the reversal

\\[ \operatorname{rev}Q(\mu)=Q_1+\mu Q_0 \\]

is the affine chart at infinity. Its elementary divisors at \\(\mu=0\\) are precisely the infinite elementary divisors of the original pencil. So the swap you proposed is the right reversal for extracting the infinite elementary divisors, provided the pencil is treated as a homogeneous degree-one pencil and the regular part is separated from the singular blocks.

The homogeneous formulation is conceptually cleaner because it makes the two charts explicit:

\\[ [\alpha:\beta]=[\lambda:1] \quad\text{and}\quad [\alpha:\beta]=[1:\mu]. \\]

The second chart is exactly the reversal above. Homogenisation is not a competing alternative to reversal; it is the projective framework in which reversal is the local coordinate change at infinity.

### 1.2 Why the current numerical experiment is unusable

Your report correctly rejects the output. The repeated rows and the impossible degree totals indicate a defect in the implementation or data flow, not evidence against the structural identity.

I would not attempt to repair the existing script by changing only the reversal. First separate the computation into independently testable stages:

1. Assemble the pencil. Verify \\(Q_0,Q_1\\) against the original block definition.
2. Compute normal rank. Check it independently at several generic parameter values, and compare with an exact symbolic rank over \\(\mathbb Q(\lambda)\\) on small examples.
3. Compute minimal indices. Do not infer them from the Smith form of a square submatrix.
4. Extract the regular part. Only after separating left and right singular blocks should the finite and infinite elementary divisors be counted.
5. Check the full identity (1). Include both left and right minimal-index contributions.
6. Check the reversal. Compare the infinite elementary divisors obtained from \\(Q_1+\mu Q_0\\) with those obtained from the homogeneous pencil at \\([1:0]\\).

A Smith form of a rectangular polynomial matrix can describe its determinantal divisors, but it does not by itself provide the complete Kronecker structure. In particular, it does not replace the minimal-index computation.

### 1.3 References to consult

For a canonical treatment, I would start with the standard matrix-pencil and Kronecker-form literature rather than relying on a single formula quoted in isolation. Useful reference points include:

- F. R. Gantmacher, The Theory of Matrices, Vol. II — classical canonical-form treatment.
- P. Lancaster and M. Tismenetsky, The Theory of Matrices — matrix pencils and canonical forms.
- P. Van Dooren's work on the computation of the Kronecker canonical form and singular matrix pencils — particularly useful for computational algorithms and the separation of singular and regular structure.

I would verify the precise edition, theorem numbering, and notation before citing a particular proposition in the paper. The key search terms are Kronecker canonical form of a singular matrix pencil, left and right minimal indices, infinite elementary divisors, and reversal of a matrix pencil.

Recommendation: amend the ledger now to include both minimal-index sums. Then state explicitly whether your problem-specific pencil has full row normal rank or another property that eliminates the left-index contribution. Do not build a theorem on the shorter identity until that property has been proved.

A particularly useful source here is Van Dooren's paper, The Computation of Kronecker's Canonical Form of a Singular Pencil (1979). Its abstract explicitly treats the finite and infinite elementary divisors and the Kronecker indices of arbitrary singular pencils, making it directly relevant to the failed numerical ledger.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

ScienceDirect+1

&#x20;A modern exposition that explicitly lists both right and left singular blocks alongside finite and infinite regular blocks is also available.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://link.springer.com\&sz=32)

Springer Nature Link+1



## 2. An idiomatic Mathlib route for L1

The missing step is a standard finite-dimensional factorisation-and-extension argument. I would formalise it in two stages rather than trying to construct \\(\Lambda,G_0,G_1\\) simultaneously.

Let

\\[ E=\mathbb C^n,\qquad F=F_1\times F_2\times F_3, \\]

and define

\\[ \Phi:E\longrightarrow F,\qquad \Phi(v)=(\mathcal Lv,CAv,Cv), \qquad T:E\longrightarrow G,\quad T(v)=\mathcal LAv. \\]

The hypothesis is

\\[ \ker\Phi\subseteq\ker T. \tag{2} \\]

### 2.1 First factor through the image

Define a map on \\(\operatorname{range}\Phi\\) by

\\[ \widetilde T(\Phi(v))=T(v). \tag{3} \\]

This is well-defined: if \\(\Phi(v_1)=\Phi(v_2)\\), then

\\[ v_1-v_2\in\ker\Phi\subseteq\ker T, \\]

so \\(T(v_1)=T(v_2)\\).

This is the mathematical content of the quotient-factorisation step. In Mathlib, the quotient route is natural:

1. Use `LinearMap.liftQ` to factor \\(T\\) through \\(E/\ker\Phi\\).
2. Identify \\(E/\ker\Phi\\) with \\(\operatorname{range}\Phi\\) by the first isomorphism theorem for linear maps.
3. Obtain \\(\widetilde T:\operatorname{range}\Phi\to G\\).

The exact theorem names and argument order can vary with the Mathlib version, so I would check the local API rather than hard-code an unverified name. The conceptual route is the important point: `liftQ` handles the kernel condition; the quotient-to-range equivalence handles the image identification.

### 2.2 Extend from the image to the whole product

Now use finite dimensionality. Choose a complement \\(U\\) of \\(\operatorname{range}\Phi\\) in \\(F\\):

\\[ F=\operatorname{range}\Phi\oplus U. \\]

Every \\(f\in F\\) has a unique decomposition \\(f=f_1+u\\), where \\(f_1\in\operatorname{range}\Phi\\), \\(u\in U\\). Define

\\[ \widehat T(f_1+u)=\widetilde T(f_1). \tag{4} \\]

Then \\(\widehat T:F\to G\\) is linear and satisfies

\\[ \widehat T\circ\Phi=T. \\]

This is the extension you need. It is not necessary to extend separately to the three factors.

Finally, since \\(F=F_1\times F_2\times F_3\\), every linear map \\(\widehat T:F\to G\\) decomposes into its restrictions to the three coordinate injections:

\\[ \widehat T(f_1,f_2,f_3) =T_1(f_1)+T_2(f_2)+T_3(f_3). \\]

In matrix form this gives

\\[ \mathcal LA=\Lambda\mathcal L+G_1CA+G_0C, \\]

with the ordering of \\(G_0,G_1\\) adjusted to your chosen block order.

### 2.3 What I would formalise

I recommend a reusable lemma, independent of the observer problem:

> Finite-dimensional factor-and-extend lemma. Let \\(E,F,G\\) be finite-dimensional vector spaces over a field, and let \\(\Phi:E\to F\\), \\(T:E\to G\\) be linear maps. If \\(\ker\Phi\subseteq\ker T\\), then there exists \\(\widehat T:F\to G\\) such that \\(T=\widehat T\circ\Phi\\).

Then the L1 proof becomes an application of this lemma with the product map above. This is preferable to a proof that directly manipulates row spaces, because it can be reused for other quotient constructions in the project.

The complement construction is mathematically clean, but if the current Mathlib version provides a general linear-map extension theorem from a submodule, use it. The important point is to avoid building the extension by coordinates unless the library API makes the complement route unusually cumbersome.

## 3. Relation between \\(\overline N\_{\mathcal Z}(\lambda)\\) and \\(P_K(\lambda)\\)

The report does not define \\(X\\), \\(\mathcal Z\\), or the construction of \\(\overline N\_{\mathcal Z}(\lambda)\\). Consequently, I cannot establish a specific equivalence between these two pencils from this file alone. In particular, I would not yet assert that they have the same finite elementary divisors.

There is, however, a clean way to formulate the comparison problem.

Recall

\\[ P_K(\lambda)=\lambda\iota_K-\Phi_K: W_K\longrightarrow\mathbb C^q. \\]

The other pencil is stated to have domain \\(V/S\\):

\\[ \overline N\_{\mathcal Z}(\lambda): V/S\longrightarrow X/\mathcal Z. \\]

The dimensions of the domains are potentially different:

\\[ \dim(V/S)=\rho_W \quad\text{(if \\(S=\ker(\mathcal L|\_V)\\)),} \qquad \dim W_K=\omega. \\]

The counterexample in Part II.2 shows that one cannot identify these dimensions by replacing \\(W_K\\) with \\(W_0\\).

### 3.1 The right comparison is a diagram, not an assumed identification

The first task is to construct, if possible, constant linear maps

\\[ a:V/S\longrightarrow W_K, \qquad b:X/\mathcal Z\longrightarrow\mathbb C^q \\]

or maps in the opposite direction, such that the pencil maps intertwine:

\\[ b\\,\overline N\_{\mathcal Z}(\lambda) = P_K(\lambda)\\,a. \tag{5} \\]

Since both pencils are affine-linear in \\(\lambda\\), this identity is equivalent to two constant identities, one for the coefficient of \\(\lambda\\) and one for the constant term.

That is the first concrete algebraic test I would perform. It will tell you whether the two constructions are genuinely related, and in which direction.

But even (5) is not enough by itself to imply equality of finite elementary divisors. For that, you need additional information about the kernels and cokernels of \\(a,b\\), or a stronger equivalence.

### 3.2 Sufficient conditions for equality of finite elementary divisors

There are several possible levels of result.

Strongest and easiest to use: if the two pencils are strictly equivalent, meaning that there are constant invertible matrices \\(U,V\\) with

\\[ \overline N\_{\mathcal Z}(\lambda) =U\\,P_K(\lambda)\\,V, \\]

then they have the same complete Kronecker structure, including finite and infinite elementary divisors and both sets of minimal indices.

A weaker, potentially more realistic target: show that both pencils reduce, by constant invertible row and column operations, to a common regular finite part plus possibly different singular and infinite blocks. Then their finite elementary divisors agree even if their full Kronecker structures do not.

This distinction is important. Equality of finite elementary divisors is weaker than strict equivalence. The latter also forces agreement of the singular structure and the infinite elementary divisors.

### 3.3 A practical route to a theorem

I suggest the following sequence.

1. Write down the coefficient pair for \\(\overline N\_{\mathcal Z}(\lambda)\\):\
   \\[\
   \overline N\_{\mathcal Z}(\lambda)\
   \=\lambda N_1-N_0.\
   \\]
2. Write down the pair for \\(P_K(\lambda)\\):\
   \\[\
   P_K(\lambda)=\lambda\iota_K-\Phi_K.\
   \\]
3. Determine whether the two coefficient pairs are related by a common pair of constant transformations.
4. If not, identify the additional domain and codomain directions in one pencil that are absent from the other.
5. Test whether those directions contribute only singular blocks or infinite elementary divisors, rather than finite regular blocks.

The last step is where an exact-sequence or block-triangular decomposition could be useful. For example, if a suitable decomposition gives

\\[ U\\,\overline N\_{\mathcal Z}(\lambda)\\,V = \begin{bmatrix} P_K(\lambda)& \*\\\ 0&D(\lambda) \end{bmatrix}, \\]

then you still need to analyse \\(D(\lambda)\\) and the off-diagonal block. You cannot simply discard them. A proof that \\(D\\) contributes no finite regular elementary divisors, together with a valid elimination of the off-diagonal block, would be a meaningful structural theorem.

My assessment: the same-finite-elementary-divisors conjecture is a reasonable research target, but it is not currently supported by the report. The first deliverable should be the coefficient-level intertwining diagram, not the desired spectral conclusion.

## 4. Should the incidence construction move to \\(\mathbb P(W_K)\\)?

At the level of a fixed admissible candidate \\(\mathcal L\\), yes: the spectral incidence problem naturally lives on \\(\mathbb P(W_K)\\). At the level of a parameterised family of candidates, not automatically. The distinction is important for your dimension estimate.

### 4.1 The fixed-candidate incidence set

For a fixed \\(\mathcal L\\), define

\\[ \mathcal E_K = \bigl\\{[w]\in\mathbb P(W_K): \Phi_K(w)\in\mathbb Cw\bigr\\}. \tag{6} \\]

This is exactly the projectivised partial-eigenvector locus. It is the right space for the spectral condition because \\(w\\) is the object on which \\(\Phi_K\\) acts.

Equivalently, using the injective inclusion \\(\iota_K:W_K\hookrightarrow\mathbb C^q\\), the condition is

\\[ \Phi_K(w)\wedge\iota_K(w)=0. \\]

In coordinates, this is a collection of homogeneous quadratic equations in \\(w\\). Thus \\(\mathcal E_K\\) is a projective algebraic set.

This is cleaner than using \\(\mathbb P(K)\\), where different state vectors can represent the same \\(w=\mathcal Lv\\), and vectors in \\(K\cap\ker\mathcal L\\) represent \\(w=0\\), which is not a projective point of \\(W_K\\).

### 4.2 The precise relation between \\(\mathbb P(K)\\) and \\(\mathbb P(W_K)\\)

Let

\\[ D:=K\cap\ker\mathcal L,\qquad d:=\dim D=k-\omega. \\]

The restriction

\\[ \mathcal L|\_K:K\longrightarrow W_K \\]

is surjective with kernel \\(D\\). It induces a projective map

\\[ \mathbb P(K)\setminus\mathbb P(D) \longrightarrow\mathbb P(W_K), \qquad [v]\longmapsto[\mathcal Lv]. \tag{7} \\]

For every \\([w]\in\mathbb P(W_K)\\), its fibre is an open subset of the projectivisation of \\((\mathcal L|\_K)^{-1}(\mathbb Cw)\\). This preimage has vector-space dimension \\(d+1\\), so its projectivisation has dimension \\(d\\). Removing the points in \\(\mathbb P(D)\\) does not change the fibre dimension. Hence every fibre has dimension

\\[ \boxed{\dim\text{ fibre}=k-\omega.} \tag{8} \\]

Consequently, if an incidence set in \\(\mathbb P(K)\setminus\mathbb P(D)\\) is exactly the pullback of a set in \\(\mathbb P(W_K)\\), its dimension is larger by \\(k-\omega\\), assuming the usual dimension formula for this projective bundle-type map.

This gives a useful diagnostic for the old estimate: replacing \\(k-1\\) by \\(\omega-1\\) is not merely a cosmetic improvement. It changes the ambient projective dimension, and the relationship between the two incidence dimensions is controlled by the fibre dimension \\(k-\omega\\).

### 4.3 Why the old coverage bound cannot simply be edited

Your previous estimate was

\\[ \dim\mathfrak I \le \max\\{v,\dim\mathcal B+k-1\\}. \tag{9} \\]

It is not safe to replace \\(k\\) by \\(\omega\\) without re-deriving the incidence construction.

There are three separate questions:

1. Does the incidence condition depend on \\(v\in K\\) only through \\(w=\mathcal Lv\\)?
2. Is the base locus \\(\mathcal B\\) the image of the old base locus under (7), or is it a genuinely different set?
3. Does the parameter space of candidate augmentations have constant \\(\omega=\dim W_K\\)?

If the first two answers are yes and the third is fixed on the stratum under consideration, then a reformulation on \\(\mathbb P(W_K)\\) is justified. The projective dimension of the spectral variable becomes \\(\omega-1\\), and the fibre correction in (8) explains how this relates to the old calculation.

But in a family \\(\mathcal L=\mathcal L(R)\\), the subspace

\\[ W_K(R)=\mathcal L(R)K \\]

can vary with \\(R\\), and its dimension can jump. There may be no single fixed projective space \\(\mathbb P(W_K)\\) over the entire parameter space. The natural treatment is then to stratify the parameter space by the rank of \\(\mathcal L(R)|\_K\\), or to work with the associated projective bundle on each constant-rank stratum.

My recommendation: formulate the fixed-candidate spectral theorem on \\(\mathbb P(W_K)\\), but retain \\(\mathbb P(K)\\) as a possible parameter-independent ambient space for the global incidence argument. Then prove that the incidence condition is saturated along the fibres of (7). This gives you the best of both descriptions without assuming that the image spaces form a fixed bundle.

## 5. Which direction should be prioritised?

I would prioritise the structural reconciliation, with one narrow computational task continuing in parallel.

The reason is not that the determinantal-divisor route is less valuable. It is that the structural correction has changed the objects in the main theorem. Until the relationship between \\(V/S\\) and \\(W_K\\) is settled, the paper risks presenting two spectral descriptions as if they were interchangeable when they need not be.

### 5.1 Recommended order of work

| Priority | Task                                                                                                                           | Why it comes now                                                 |
| -------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| 1        | Write the exact definitions of \\(\overline N\_{\mathcal Z}\\), \\(X\\), and \\(\mathcal Z\\), and derive its coefficient pair | Necessary to formulate the comparison theorem precisely          |
| 2        | Establish or refute a coefficient-level intertwining relation with \\(P_K\\)                                                   | The decisive first test for a common spectral structure          |
| 3        | Prove the fixed-candidate incidence theorem on \\(\mathbb P(W_K)\\)                                                            | Uses the corrected domain directly                               |
| 4        | Re-derive the coverage dimension estimate, stratifying by \\(\omega\\) if necessary                                            | Prevents a hidden constant-rank assumption                       |
| 5        | Continue the determinantal-divisor encoding independently                                                                      | It is exact and does not depend on the disputed Kronecker ledger |
| 6        | Repair the KCF numerical implementation only after the theoretical ledger includes both minimal-index families                 | Avoids debugging against an incomplete identity                  |

I would not spend the next period trying to prove equality of finite elementary divisors directly. First establish the coefficient-level diagram in Question 3. If that fails, it will identify exactly what additional hypotheses or correction terms are needed.

### 5.2 Minimal publishable structural content

I think there is a coherent structural paper even if the strongest proposed comparison theorem turns out to be false.

A minimal, defensible package would be:

Theorem A — Intrinsic partial-eigenvector reduction. Under (5a), the map

\\[ \Phi_K:W_K\to\mathbb C^q,\qquad \Phi_K(\mathcal Lv)=\mathcal LAv \\]

is well-defined and independent of the extension \\(\Lambda\\). Moreover,

\\[ (5b)\text{ fails} \quad\Longleftrightarrow\quad \exists\\,0\ne w\in W_K: \Phi_K(w)\in\mathbb Cw. \tag{10} \\]

This is the central structural result. It should be stated with the normal-rank argument made explicit: the leading coefficient \\(\iota_K\\) is injective, so \\(P_K(\lambda)=\lambda\iota_K-\Phi_K\\) has full column normal rank \\(\omega\\); a finite rank drop is exactly a partial eigenvector.

Theorem B — Exact determinantal criterion. If \\(h\\) is the normal rank of \\(Q\_{\mathcal L}\\), then

\\[ (5b)\quad\Longleftrightarrow\quad \gcd\\{\text{all }h\text{-minors of }Q\_{\mathcal L}(\lambda)\\} \in\mathbb C^\times. \tag{11} \\]

I would call these all \\(h\\)-minors, not “maximal minors” unless \\(h=\min(m,n)\\). The gcd statement is exact over \\(\mathbb C\\): the rank is below \\(h\\) at some finite \\(\lambda_0\\) precisely when all \\(h\\)-minors vanish at \\(\lambda_0\\), which is equivalent to a nonconstant common polynomial factor.

Theorem C — Incidence reformulation. For a fixed candidate, the bad spectral locus is the projective set \\(\mathcal E_K\subseteq\mathbb P(W_K)\\) in (6). The relation to the state-space incidence construction is given by the projective map (7), with fibre dimension \\(k-\omega\\).

These three results fit together: Theorem A gives the intrinsic spectral object, Theorem B gives an exact algebraic certificate, and Theorem C gives the geometric interpretation. They do not depend on the unresolved claim that the \\(V/S\\) pencil has the same finite elementary divisors.

A stronger comparison theorem between \\(\overline N\_{\mathcal Z}\\) and \\(P_K\\) would be a substantial addition, but it is not necessary for this core package.

## 6. Further audit findings

There are several points in the report that I would correct or sharpen before the next review round.

### 6.1 The partial-eigenvector criterion can be proved directly

The report states

\\[ (5b)\text{ fails} \iff \exists\\,0\ne w\in W_K: \Phi_K(w)\in\mathbb Cw. \\]

This is correct under (5a), and there is a short proof that is worth including in the paper.

Set

\\[ D:=K\cap\ker\mathcal L. \\]

By (5a), if \\(v\in D\\), then

\\[ \mathcal Lv=CAv=Cv=0 \quad\Longrightarrow\quad \mathcal LAv=0. \\]

Thus \\(D\\) is contained in the kernel of \\(Q\_{\mathcal L}(\lambda)\\) for every \\(\lambda\\).

For each \\(\lambda\\), the map

\\[ \ker Q\_{\mathcal L}(\lambda)\longrightarrow\ker P_K(\lambda), \qquad v\longmapsto\mathcal Lv \\]

is surjective, and its kernel is \\(D\\). Consequently,

\\[ \dim\ker Q\_{\mathcal L}(\lambda) = \dim D+\dim\ker P_K(\lambda). \tag{12} \\]

Now \\(P_K(\lambda)=\lambda\iota_K-\Phi_K\\) has full column normal rank \\(\omega\\): choose a left inverse \\(J\\) of the injective map \\(\iota_K\\). Then

\\[ J P_K(\lambda)=\lambda I-J\Phi_K, \\]

whose determinant is a monic polynomial of degree \\(\omega\\). Hence \\(P_K(\lambda)\\) has full column rank for all but finitely many \\(\lambda\\).

It follows from (12) that

\\[ \operatorname{nrank}Q\_{\mathcal L}=n-\dim D, \\]

and that the rank of \\(Q\_{\mathcal L}(\lambda)\\) drops below its normal rank exactly when \\(P_K(\lambda)\\) loses column rank. This is equivalent to the existence of a nonzero \\(w\in W_K\\) with

\\[ \Phi_K(w)=\lambda w. \\]

This proof is important because it establishes the criterion without needing the Kronecker accounting identity. It should become the central proof of Theorem A.

### 6.2 Clarify the joint-profile formula

There appears to be a possible notation or inequality issue in Part II.5.

You write

\\[ q\_{\min}=\min\_{(\rho,c)\in\mathfrak P}(\rho+c) \\]

and then define \\(c\_{\min}(\rho)\\) using \\(\mathfrak P\_{\rm spec}\\). If \\(\mathfrak P\_{\rm spec}\subseteq\mathfrak P\\), then

\\[ \min\_{(\rho,c)\in\mathfrak P}(\rho+c) \le \min\_{(\rho,c)\in\mathfrak P\_{\rm spec}}(\rho+c), \\]

not the reverse.

There are two consistent ways to write the result:

\-&#x20;

# If \\(q\_{\min}\\) is the minimum over spectrally feasible candidates, define \\(\mathfrak P\_{\rm spec}\\) as their profile set and write \\[ \boxed{ q\_{\min}

\min\_{\rho}\
\bigl(\rho+c\_{\min}(\rho)\bigr).\
}\
\\]\
This is an equality, assuming the minima are attained and the relevant \\(\rho\\)-values are included.

\- If \\(\mathfrak P\\) describes a larger, relaxed feasible set, then its minimum is a lower bound for the spectral minimum:\
\\[\
\min\_{(\rho,c)\in\mathfrak P}(\rho+c)\
\le q\_{\min}.\
\\]

Please check which interpretation the report intends. The joint-profile idea is sound, but the set over which \\(q\_{\min}\\) is minimised and the direction of the inequality must be aligned.

### 6.3 The Bézout encoding needs a complexity qualification

The identity

\\[ \sum_i u_i(\lambda)p_i(\lambda;R)=1 \tag{13} \\]

is an exact algebraic certificate for the gcd condition. But there are two separate issues:

1. Existence of a degree bound. Since the \\(p_i\\) are univariate polynomials of degree at most \\(h\\), a finite Bézout degree bound can be obtained by repeated extended-Euclidean computations. The paper should state an explicit bound and prove it, rather than merely say “polynomially bounded.”
2. Size of the encoding. The number of \\(h\\)-minors of an \\(m\times n\\) pencil is\
   \\[\
   \binom mh\binom nh.\
   \\]\
   This can be very large. A bounded-degree Bézout certificate therefore gives a finite existential-real encoding, but does not automatically give a polynomial-size encoding.

There is another issue for a parameterised family: the normal rank \\(h\\) may depend on the augmentation parameters \\(R\\). A rigorous encoding should either stratify by the possible values of \\(h\\), or establish a fixed normal-rank condition on the candidate family being considered.

These qualifications do not weaken the value of the \\(\Delta_h\\) criterion. They prevent an exact algebraic characterisation from being mistaken for an efficient complexity reduction.

### 6.4 The counterexample is decisive; the random sweep is supplementary

The displayed \\(n=4\\) example is enough to refute

\\[ \mathcal LK=\mathcal L(V\cap K) \\]

provided the four dimension assertions and admissibility conditions are verified exactly. The random sweep is useful as a diagnostic, but it is not needed for the mathematical conclusion.

I would include a compact exact certificate in the paper or supplement:

- exact ranks of \\([C;CA]\\), \\([\\,\mathcal L;CA;C\\,]\\), and the relevant restrictions;
- exact bases for \\(K\\) and \\(V\cap K\\);
- exact ranks of \\(\mathcal L|\_K\\) and \\(\mathcal L|\_{V\cap K}\\);
- verification of (5a) and (5b).

Because all entries are rational, these checks should be performed over \\(\mathbb Q\\), not by floating-point rank tolerances.

## 7. Suggested next work package

I would organise the next round around the following deliverables.

Work package A — Structural foundations

First priority

- Write the full proof of (12) and the corrected partial-eigenvector theorem.
- State the factor-and-extend lemma and complete the L1 formalisation.
- Give the exact definitions of \\(X,\mathcal Z,\overline N\_{\mathcal Z}\\).
- Derive the two coefficient matrices of \\(\overline N\_{\mathcal Z}(\lambda)\\).
- Test whether a constant intertwining diagram with \\(P_K(\lambda)\\) exists.

Work package B — Incidence geometry

- Define \\(\mathcal E_K\subseteq\mathbb P(W_K)\\).
- Prove the projective map and fibre-dimension formula (7)–(8).
- Determine whether the old incidence set is saturated along the fibres.
- Stratify the augmentation parameter space by \\(\omega=\operatorname{rank}(\mathcal L|\_K)\\), if necessary.

Work package C — Algebraic certificate

- Rename the \\(h\times h\\) minors precisely.
- Prove a uniform Bézout degree bound.
- Account for the parameter-dependent normal rank.
- Estimate the size of the resulting existential-real formula.

Work package D — Kronecker verification

- Correct the ledger to include left and right minimal indices.
- Establish whether the specific pencil has full row normal rank.
- Rebuild the KCF tests from small exact examples before testing random pencils.

## 8. Overall assessment

The most important progress in this report is not the number of formalised declarations. It is the correction of the spectral domain and the explicit refutation of the equality that would have identified it with the earlier quotient construction.

That correction has three consequences:

1. \\(W_K=\mathcal LK\\) is now the intrinsic domain for the partial-eigenvector problem.
2. The \\(V/S\\) pencil must be treated as a separate construction until a comparison theorem is proved.
3. The incidence argument must be re-derived with attention to the map \\(K\to W_K\\) and to rank variation across candidate augmentations.

The project now has a solid route to a publishable structural result even if the proposed equivalence of finite elementary divisors fails. The intrinsic map, its exact spectral criterion, and the corrected incidence geometry form a coherent mathematical contribution. The determinantal-divisor criterion supplies an independent algebraic formulation. The KCF accounting and the comparison with \\(\overline N\_{\mathcal Z}\\) should be presented as open questions until their hypotheses and proofs are complete.

My strongest recommendation: make the next report focus on the coefficient-level relationship between \\(\overline N\_{\mathcal Z}(\lambda)\\) and \\(P_K(\lambda)\\), with all spaces and quotient maps explicitly defined. That is now the main structural bottleneck. Do not spend the next round trying to force equality of finite elementary divisors before that relationship has been established.