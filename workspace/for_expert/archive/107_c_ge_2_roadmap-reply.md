# **Review of Report 107: the next layer,&#x20;**\\(c\geq 2\\)

## **1. Overall assessment**

The report identifies the right mathematical obstruction in moving from \\(c=1\\) to \\(c\geq2\\): **the kernel of the compressed map is no longer automatically an invariant subspace of the compression of&#x20;**\\(A\\). The dimension condition in II.3 is therefore not a cosmetic technical assumption. It is precisely what makes the proposed direction-first approach work.

My assessment is:

- **II.2 is essentially correct**, provided the row-space dimension assumptions are stated explicitly.
- **The conditional direction theorem in II.3 is correct**, and its proof is complete.
- **The counterexample in II.3 is plausible but not fully verifiable from the data supplied**: the full off-diagonal block of \\(A\\) is needed to verify that the proposed \\(D\\) really is \\(\ker H\\).
- **The parameter-space idea in II.4 is promising**, especially the invariant-subspace variety and the rank stratification involving \\(A\_{21}\\).
- **The proposed fixed-**\\(D\\)**&#x20;fibre in II.4 contains a serious inconsistency**: it requires \\(D\subseteq V\\), although \\(D=\ker H\\) implies \\(D\perp V\\).
- **The main research decision is whether to study the full&#x20;**\\(c\\)**-layer or a restricted,&#x20;**\\(M\\)**-invariant subclass.** These are different problems, and the paper should not identify them without proving an equivalence.

I recommend that the project proceed with \\(c=2\\), but first repair the definitions and the fixed-direction fibre. I would not start a hardness investigation yet.

# **Part I. The layer index and the three dimensions**

## **2. The distinction in II.2 is fundamental**

Let \\(X=\mathbb R^n\\), let \\(K=K_0\\), and identify row vectors with vectors in \\(X\\) using the Euclidean inner product. Write \\(P_K\\) for orthogonal projection onto \\(K\\).

The restriction of the row space \\(V\\) to \\(K\\) is the map

\\[ \operatorname{res}\_K:V\longrightarrow K^\*, \qquad v\longmapsto \langle v,\cdot\rangle|\_K. \\]

Its rank is

\\[ \rho=\operatorname{rank}(LN)      =\dim P_K(V). \\]

Its kernel is

\\[ \ker(\operatorname{res}\_K) =V\cap K^\perp. \\]

On the other hand, the kernel of the compressed matrix \\(H=LN\\), viewed as a map from \\(K\\), is

\\[ D:=\ker H=K\cap V^\perp. \\]

Consequently,

\\[ \boxed{ \begin{aligned} \omega&=\operatorname{rank}H=\rho,\\\ c&:=\dim D=k-\rho,\\\ t&:=\dim(V\cap K^\perp)=q-\rho \end{aligned}} \tag{1} \\]

where the last equality assumes \\(\dim V=q\\).

In particular,

\\[ \boxed{t=q-k+c.} \tag{2} \\]

This is the cleanest way to resolve Q1.

### **My recommendation: use&#x20;**\\(c=k-\rho\\)**&#x20;as the geometric layer index**

The reason is that the family of designs is naturally stratified by

\\[ D=\ker H\in\operatorname{Gr}(c,K). \\]

The direction space has dimension \\(c\\), so the natural parameter space for the \\(c\\)-layer is a subset of \\(\operatorname{Gr}(c,K)\\).

However, the other quantity should not disappear. I recommend the notation

\\[ \boxed{ c:=k-\rho,\qquad t:=q-\rho. } \\]

Then:

- \\(c\\) is the **kernel dimension** or **geometric layer index**;
- \\(t\\) is the **ambient row-excess dimension**;
- \\(q=\rho+t\\);
- \\(t=q-k+c\\).

This preserves the decomposition used in Papers I and II without confusing it with the geometry of \\(\ker H\\).

The distinction matters especially when \\(q\ne k\\). In the report's \\(q=5,k=4,\rho=4\\) example, one has \\(c=0\\) but \\(t=1\\). There is an extra ambient row direction, but there is no kernel direction in \\(K\\). Calling both quantities the layer index would obscure the geometry.&#x20;

107_c_ge_2_roadmap.md



### **One qualification: independent rows**

The identity

\\[ t=q-\rho=\dim(V\cap K^\perp) \\]

requires \\(\dim V=q\\), meaning the \\(q\\) rows are independent.

If the design has dependent rows, then

\\[ \dim(V\cap K^\perp)=\dim V-\rho, \\]

not necessarily \\(q-\rho\\).

The paper should therefore either assume full row rank or use

\\[ t:=\dim V-\rho \\]

and distinguish the number of rows \\(q\\) from the dimension of their row space.

This is important for the general \\(c\geq2\\) theory, not just a matter of notation.

# **Part II. The conditional direction theorem**

## **3. Theorem II.3 is correct**

The claim is:

> If\
> \\[\
> \dim(V\cap K)=k-\dim D,\
> \\]\
> then\
> \\[\
> M(D)\subseteq D,\
> \\]\
> where \\(M=P_KA|\_K\\).

I agree with the proof in the report. It is mathematically sound.

Let

\\[ D=K\cap V^\perp,\qquad \dim D=c. \\]

First, (5a) implies

\\[ AD\perp V. \tag{3} \\]

Indeed, for \\(d\in\ker H\\), every row of \\(H_A\\) annihilates \\(d\\), because

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H. \\]

Thus every \\(v\in V\\) satisfies

\\[ \langle v,Ad\rangle=0. \\]

Now fix \\(d\in D\\). Define

\\[ \varphi_d(u)=\langle u,d\rangle,\qquad u\in K, \\]

and

\\[ \varphi\_{Ad}(u)=\langle u,Ad\rangle,\qquad u\in K. \\]

By (3), \\(\varphi\_{Ad}\\) vanishes on \\(V\cap K\\). Hence

\\[ \varphi\_{Ad}\in\operatorname{Ann}\_{K^\*}(V\cap K). \\]

The assumed dimension condition gives

\\[ \dim\operatorname{Ann}\_{K^\*}(V\cap K) =k-\dim(V\cap K) =c. \\]

Also, the functionals \\(\\{\varphi_d:d\in D\\}\\) form a \\(c\\)-dimensional subspace of this annihilator: they vanish on \\(V\cap K\\), and their linear independence follows from the nondegeneracy of the inner product restricted to \\(K\\).

Therefore,

\\[ \operatorname{Ann}\_{K^\*}(V\cap K) =\\{\varphi_d:d\in D\\}. \\]

It follows that

\\[ \varphi\_{Ad}=\varphi\_{d'} \\]

for some \\(d'\in D\\). Equivalently,

\\[ P_K(Ad)=d'\in D. \\]

Thus

\\[ \boxed{M(D)\subseteq D.} \\]

There is no gap in this annihilator argument. The nondegeneracy assumption is satisfied because \\(K\\) is a Euclidean subspace of \\(X\\).&#x20;

107_c_ge_2_roadmap.md



## **4. A useful strengthening: the dimension condition is a splitting condition**

There is a further structural interpretation that I think should be included in the paper.

Assume \\(\dim V=q\\). Since

\\[ \dim(V\cap K^\perp)=q-\rho=t, \\]

the condition

\\[ \dim(V\cap K)=\rho \\]

implies

\\[ \dim(V\cap K)+\dim(V\cap K^\perp)=q. \\]

But \\(K\cap K^\perp=\\{0\\}\\), so

\\[ (V\cap K)\oplus(V\cap K^\perp)\subseteq V. \\]

The two sides have the same dimension. Therefore

\\[ \boxed{ V=(V\cap K)\oplus(V\cap K^\perp). } \tag{4} \\]

Thus the dimension hypothesis is equivalent to saying that \\(V\\) is *split with respect to the decomposition*

\\[ X=K\oplus K^\perp. \\]

This is a much more informative interpretation than merely saying that two dimensions happen to agree.

It also explains why the hypothesis is strong: it rules out all mixed directions in the row space.

I would introduce a term such as \\(K\\)**-split row space** or **balanced row-space condition**, and state the theorem as:

> **Conditional invariant-kernel theorem.** If the design satisfies (5a) and its row space is \\(K\\)-split, then \\(\ker H\\) is invariant under \\(M=P_KA|\_K\\).

This makes the scope of the result explicit.

## **5. Should the dimension condition be retained?**

This is the most important conceptual question in the report.

My answer is:

**Retain it for a separate structured layer theory, but do not silently impose it on the original feasibility problem.**

There are two different problems:

### **Problem A: full&#x20;**\\(c\\)**-layer feasibility**

Study all designs satisfying (5a) and (5b), with

\\[ \dim\ker H=c. \\]

In this problem, \\(D=\ker H\\) need not be \\(M\\)-invariant. The direction-first invariant-subspace structure is unavailable in general.

### **Problem B:&#x20;**\\(K\\)**-split&#x20;**\\(c\\)**-layer feasibility**

Study designs satisfying (5a), (5b), and

\\[ V=(V\cap K)\oplus(V\cap K^\perp). \\]

For this restricted problem, the theorem gives

\\[ M(D)\subseteq D. \\]

This problem has a much more tractable geometric structure and is the natural setting for the proposed invariant-subspace parameterization.

The distinction is important for the project's overall objective. If the original question is minimum-order functional-observer feasibility, then proving a theorem for Problem B does not solve Problem A unless you establish a normalization theorem showing that every feasible design can be replaced by a \\(K\\)-split feasible design without increasing its order or violating prescribed rows.

The report does not establish such a normalization theorem.

Therefore, I would not define the full \\(c\\)-layer as requiring the dimension hypothesis. Instead, I would explicitly introduce the structured \\(K\\)-split subclass.

# **Part III. Checking the counterexample**

## **6. The counterexample has the right conceptual purpose**

The report is correct about the logical point it wants to establish:

\\[ \text{(5a) alone does not imply }M(D)\subseteq D. \\]

The proof of II.3 uses the dimension condition in an essential way, and it is reasonable to seek a counterexample when that condition is removed.&#x20;

107_c_ge_2_roadmap.md



However, I would not yet regard the displayed example as a fully verified counterexample in the paper.

### **The missing verification**

The report specifies

\\[ M=\operatorname{diag}(1,1,2,3) \\]

and

\\[ D=\operatorname{span}\\{e_1+e_2,\ e_3+e_4\\}. \\]

It then proposes

\\[ U=D+AD,\qquad V=U^\perp. \\]

But \\(D\\) is supposed to be the actual compressed kernel:

\\[ D=K\cap V^\perp. \\]

Since \\(V=U^\perp\\), we have

\\[ V^\perp=U, \\]

and therefore

\\[ \boxed{K\cap V^\perp=K\cap(D+AD).} \tag{5} \\]

Consequently, to verify that the proposed design really has kernel \\(D\\), the example must establish

\\[ \boxed{K\cap(D+AD)=D.} \tag{6} \\]

This is not automatic from the displayed compression \\(M\\).

In particular, if \\(A\\) maps \\(K\\) into \\(K\\), then \\(D+AD\subseteq K\\), and for this non-invariant \\(D\\),

\\[ \dim(D+AD)=3. \\]

The actual compressed kernel would then have dimension \\(3\\), not \\(2\\).

A suitable nonzero off-diagonal block \\(A\_{21}\\) might make (6) hold, but the report does not provide that block. The compression \\(M\\) alone is insufficient to verify the example.

### **What the example must display**

For the non-invariant \\(D\\), provide:

1. The full matrix \\(A\\), or at least its blocks \\(M\\) and \\(A\_{21}\\).
2. The resulting basis of \\(D+AD\\).
3. Its dimension.
4. The exact intersection \\(K\cap(D+AD)\\).
5. The resulting \\(V=(D+AD)^\perp\\).
6. The values of\
   \\[\
   \dim(K\cap V^\perp),\qquad\
   \dim(V\cap K),\qquad\
   \operatorname{rank}H.\
   \\]
7. A direct verification that \\(AD\perp V\\).

If the example is intended to show a counterexample to the implication from (5a), these checks suffice for that implication. If it is intended to exhibit a feasible functional-observer design, (5b) must also be checked.

**Verdict on the counterexample:** the underlying mathematical idea is sound, but the data in Report 107 are not sufficient to independently verify the claimed example. I would classify it as *not yet fully certified*, rather than incorrect.

# **Part IV. The most important correction to II.4**

## **7. The proposed fixed-direction fibre is inconsistent**

The report states that, for fixed \\(D\\),

\\[ V_0+D\subseteq V\subseteq(D+AD)^\perp. \tag{7} \\]

This cannot be correct if \\(D\\) denotes

\\[ D=\ker H=K\cap V^\perp. \\]

Indeed, by definition,

\\[ D\subseteq V^\perp. \\]

Equivalently,

\\[ \boxed{D\perp V.} \tag{8} \\]

Thus \\(D\subseteq V\\) is impossible unless \\(D=\\{0\\}\\).

This is not a minor notational issue. It changes the fibre and the parameter-space geometry. The \\(c=1\\) construction involved a complementary subspace of \\(K\\), not the kernel line itself. The two should not be conflated.

I regard this as the highest-priority correction to Report 107.

## **8. Correct fibre for the unrestricted problem**

For a fixed candidate kernel \\(D\\), put

\\[ U_D:=D+AD. \\]

By (5a),

\\[ U_D\subseteq V^\perp, \\]

so

\\[ V\subseteq U_D^\perp. \\]

The correct fixed-\\(D\\) family for the unrestricted problem is therefore

\\[ \boxed{ \mathcal F_D= \left\\{ V\in\operatorname{Gr}(q,U_D^\perp): V_0\subseteq V,\quad K\cap V^\perp=D \right\\}, } \tag{9} \\]

with the additional condition (5b) imposed afterward.

Here \\(V_0=\operatorname{row}L_0\\).

The two constraints in (9) have distinct roles:

- \\(V_0\subseteq V\\) is the prescribed-row condition.
- \\(K\cap V^\perp=D\\) says that \\(D\\) is the *exact* compressed kernel, rather than merely a subspace of it.

The second condition is essential. The containment \\(V\subseteq U_D^\perp\\) only guarantees

\\[ D\subseteq K\cap V^\perp. \\]

It does not guarantee equality.

### **Nonemptiness conditions**

Some immediate necessary conditions are

\\[ V_0\subseteq U_D^\perp, \qquad \dim U_D\leq n-q. \\]

Moreover, exactness requires

\\[ \boxed{K\cap U_D=D.} \tag{10} \\]

To see this, note that

\\[ U_D\subseteq V^\perp. \\]

Hence

\\[ K\cap U_D\subseteq K\cap V^\perp=D. \\]

The reverse inclusion holds because \\(D\subseteq U_D\\). Thus equality is necessary.

This condition should be incorporated into the base of the full parameter space, or enforced explicitly in the fibre construction.

For a fixed \\(D\\), the exact-kernel condition is a rank condition on the restriction map \\(V\to K^\*\\). Once the ambient Grassmannian and prescribed-row constraints are fixed, it is an open maximal-rank condition. But it can still be empty.

## **9. The fibre becomes particularly simple in the&#x20;**\\(K\\)**-split problem**

There is a useful stronger result if you deliberately impose the dimension hypothesis from II.3.

Assume

\\[ V=(V\cap K)\oplus(V\cap K^\perp). \\]

Since

\\[ D=K\cap V^\perp, \\]

the \\(K\\)-component of \\(V\\) is uniquely determined:

\\[ \boxed{ V\cap K=D^{\perp_K}, } \tag{11} \\]

where \\(D^{\perp_K}\\) denotes the orthogonal complement of \\(D\\) inside \\(K\\).

Define

\\[ W:=V\cap K^\perp. \\]

Then

\\[ \boxed{ V=D^{\perp_K}\oplus W,\qquad \dim W=t=q-\rho. } \tag{12} \\]

Thus, under the splitting condition, the \\(K\\)-part of the row space is not a free Grassmannian parameter. It is determined by \\(D\\). Only the \\(K^\perp\\)-part remains to be chosen.

Now suppose \\(D\\) is \\(M\\)-invariant. Write the block decomposition of \\(A|\_K\\) as

\\[ Ad=M d+A\_{21}d,\qquad d\in K, \\]

where \\(A\_{21}:K\to K^\perp\\).

Since \\(M(D)\subseteq D\\),

\\[ D+AD=D+A\_{21}D. \tag{13} \\]

The condition \\(V\subseteq(D+AD)^\perp\\) becomes

\\[ W\subseteq K^\perp\cap(A\_{21}D)^\perp. \\]

Set

\\[ T_D:=K^\perp\cap(A\_{21}D)^\perp. \\]

The prescribed rows require

\\[ P_K(V_0)\subseteq D^{\perp_K}, \\]

and

\\[ W_0:=P\_{K^\perp}(V_0)\subseteq W. \\]

Therefore, provided \\(W_0\subseteq T_D\\), the fixed-\\(D\\) fibre in the \\(K\\)-split problem is

\\[ \boxed{ \operatorname{Gr}\left( t-\dim W_0,\\, T_D/W_0 \right). } \tag{14} \\]

Its nonemptiness conditions are

\\[ \dim W_0\leq t\leq\dim T_D. \\]

The condition (5b) then selects the subset of this Grassmannian for which the pencil has full rank at every \\(\lambda\\).

This is, in my view, a much better starting point for the \\(K\\)-split \\(c\geq2\\) theory than the fibre proposed in II.4.

It also connects naturally with the \\(c=1\\) geometry: the kernel direction determines its orthogonal complement in \\(K\\), while the remaining free directions lie outside \\(K\\).

# **Part V. The parameter space for&#x20;**\\(c=2\\)

## **10. The proposed invariant-subspace base is correct for the restricted problem**

For the \\(K\\)-split problem, the base should be

\\[ \boxed{ \mathcal I_2(M) = \\{D\in\operatorname{Gr}(2,K):M(D)\subseteq D\\}. } \tag{15} \\]

This is the variety of \\(M\\)-invariant two-dimensional subspaces.

The next step is to stratify it by

\\[ r(D):=\operatorname{rank}(A\_{21}|\_D). \\]

By (13),

\\[ \dim(D+AD) =2+\operatorname{rank}(A\_{21}|\_D). \\]

Hence the three strata are

\\[ \begin{aligned} \mathcal I_2^{(0)} &=\\{D\in\mathcal I_2(M):r(D)=0\\},\\\ \mathcal I_2^{(1)} &=\\{D\in\mathcal I_2(M):r(D)=1\\},\\\ \mathcal I_2^{(2)} &=\\{D\in\mathcal I_2(M):r(D)=2\\}. \end{aligned} \tag{16} \\]

Their corresponding dimensions of \\(D+AD\\) are \\(2,3,4\\).

This is exactly the proposed stratification, but it is useful to express it as a rank stratification of the bundle map induced by \\(A\_{21}\\).

### **A terminology correction**

The report describes \\(A\_{21}\\) as a “nilpotent-like part.” I would avoid that expression.

In general, \\(A\_{21}:K\to K^\perp\\) is a rectangular off-diagonal block, not an endomorphism, and it need not be nilpotent. A more precise description is:

> the off-diagonal coupling from \\(K\\) to \\(K^\perp\\).

This terminology is particularly important when explaining why \\(D+AD\\) has dimension \\(2+r(D)\\).

## **11. The invariant-subspace variety is a determinantal object, but not necessarily a simple one**

Let \\(\mathcal S\\) be the tautological rank-two bundle on \\(\operatorname{Gr}(2,K)\\), and let \\(\mathcal Q\\) be the quotient bundle.

The condition \\(M(D)\subseteq D\\) is equivalent to the vanishing of the induced bundle map

\\[ \mathcal S \xrightarrow{M} K\otimes\mathcal O \longrightarrow \mathcal Q. \\]

Thus \\(\mathcal I_2(M)\\) is a closed subvariety of the Grassmannian.

The rank stratification in (16) is then given by determinantal conditions on

\\[ A\_{21}|\_{\mathcal S}:\mathcal S\longrightarrow K^\perp\otimes\mathcal O. \\]

This gives a concrete algebraic-geometric formulation of Q3 and Q5.

However, one should not assume that the resulting varieties are irreducible or have a uniform degree formula. Their geometry depends strongly on the Jordan structure of \\(M\\) and on the relative position of \\(A\_{21}\\).

### **A useful classification observation for&#x20;**\\(c=2\\)

For a real invariant two-plane \\(D\\), the restriction \\(M|\_D\\) is a real \\(2\times2\\) matrix. Its characteristic polynomial has one of three forms:

1. two real eigenvalues, possibly equal;
2. a repeated real eigenvalue with a nontrivial Jordan block;
3. an irreducible real quadratic, corresponding to a complex-conjugate pair of eigenvalues.

This means that the \\(c=2\\) theory is not merely a two-dimensional version of the \\(c=1\\) real-eigenvector theory.

In particular, a real invariant two-plane can exist even when \\(M\\) has no real eigenvector in the relevant part of its spectrum: it can be the realification of a complex-conjugate eigenpair.

This is an important phenomenon to include in the \\(c=2\\) paper.

# **Part VI. The degeneracy locus and its components**

## **12. The full degeneracy locus is correctly formulated, but it describes the unrestricted problem**

The report introduces

\\[ \mathcal D_s = \\{D\in\operatorname{Gr}(c,K): \dim(D+AD)\leq s\\}. \tag{17} \\]

This is a natural degeneracy locus.

To see its determinantal structure, let \\(\mathcal S\\) be the tautological rank-\\(c\\) bundle on \\(\operatorname{Gr}(c,K)\\). Consider

\\[ \Phi:\mathcal S\oplus\mathcal S \longrightarrow X\otimes\mathcal O, \qquad (d_1,d_2)\longmapsto d_1+Ad_2. \\]

At a point \\(D\\), the image of \\(\Phi_D\\) is exactly \\(D+AD\\). Hence

\\[ \mathcal D_s=\\{D:\operatorname{rank}\Phi_D\leq s\\}. \\]

This is a determinantal rank condition.

The minimum possible rank is \\(c\\), since \\(D\subseteq D+AD\\). The lowest-rank locus is therefore

\\[ \dim(D+AD)=c \iff AD\subseteq D. \\]

So the report's statement that the lowest stratum is \\(AD\subseteq D\\) is correct.&#x20;

107_c_ge_2_roadmap.md



But there is an important distinction:

- The full degeneracy locus \\(\mathcal D_s\\) allows non-\\(M\\)-invariant \\(D\\).
- The \\(K\\)-split problem restricts to \\(\mathcal I_c(M)\\), the \\(M\\)-invariant subspaces.
- On that restricted variety, the rank condition simplifies to a rank condition on \\(A\_{21}|\_D\\).

These should be presented as two different parameter-space constructions.

### **Are components and degrees known?**

There is no universal answer based solely on the notation \\(\mathcal D_s\\).

For generic maps of vector bundles, classical determinantal-variety theory provides expected codimensions and, under suitable hypotheses, formulas for classes and degrees. But here the map

\\[ (d_1,d_2)\longmapsto d_1+Ad_2 \\]

has special structure: its two components are related by the same fixed operator \\(A\\). The map is not a generic bundle map.

Likewise, \\(\mathcal I_2(M)\\) is a variety of invariant subspaces, and its components depend on the module structure induced by \\(M\\). Repeated eigenvalues and nontrivial Jordan blocks can change the component structure.

Therefore, I would not promise a universal component or degree formula.

For \\(c=2\\), the practical approach should be:

1. compute the rational or real Jordan structure of \\(M\\);
2. describe the invariant two-planes associated with each spectral configuration;
3. impose the rank conditions on \\(A\_{21}|\_D\\);
4. compute the resulting components and real points.

This is a manageable research program, whereas attempting to classify arbitrary \\(\mathcal D_s\\) for all \\(c\\) is likely too broad.

# **Part VII. The geometry of the total design family**

## **13. Is the total space a Grassmann bundle?**

For the \\(K\\)-split problem, the answer is promising, with a qualification.

On a stratum where

\\[ \operatorname{rank}(A\_{21}|\_D)=r \\]

is constant, the subspaces

\\[ T_D=K^\perp\cap(A\_{21}D)^\perp \\]

have constant dimension

\\[ \dim T_D=\dim K^\perp-r=\rho-r. \\]

Thus the \\(T_D\\) form a vector bundle over that stratum.

If the prescribed-row projection \\(W_0=P\_{K^\perp}(V_0)\\) is fixed and compatible with every \\(D\\) in the stratum, then the quotient \\(T_D/W_0\\) also has constant rank.

The fibres in (14) are then Grassmannians of constant dimension. This gives a relative Grassmann bundle over the relevant invariant-subspace stratum.

However, two qualifications matter:

1. If the compatibility of \\(W_0\subseteq T_D\\) varies with \\(D\\), the base must be restricted to the corresponding locally closed locus.
2. Condition (5b) cuts out a further subset of the total space. It need not preserve irreducibility.

Therefore, the correct statement is:

> Before imposing the pencil condition (5b), the \\(K\\)-split design family is a relative Grassmann bundle over each constant-rank, prescribed-row-compatible invariant-subspace stratum.

Do not claim that the final feasible family is automatically irreducible. A Grassmann bundle over an irreducible base is irreducible, but the pencil-feasible subset may have several components or may be empty.

## **14. What about the unrestricted problem?**

The unrestricted fibre (9) is also naturally related to a Grassmannian, but it has a different structure.

The exact-kernel condition

\\[ K\cap V^\perp=D \\]

is an open maximal-rank condition within the Grassmannian of \\(q\\)-planes in \\(U_D^\perp\\) containing \\(V_0\\).

The additional condition

\\[ \dim(V\cap K)=\rho \\]

is a separate intersection-dimension condition. It is generally a locally closed rank stratum, not automatically an open subset of that Grassmannian.

Thus the assertion in II.4 that the dimension hypothesis simply cuts out an open subset of the Grassmannian needs proof and should not be used in the current form.

# **Part VIII. Complexity and hardness**

## **15. What can be said about complexity at this stage?**

The report is right to prioritize \\(c=2\\) geometry before hardness.

There are three different computational questions:

1. Does an \\(M\\)-invariant two-plane \\(D\\) exist?
2. Does there exist such a \\(D\\) satisfying the \\(A\_{21}\\)-rank and prescribed-row constraints?
3. Does there exist a corresponding fibre point satisfying the full pencil condition (5b)?

These should not be collapsed into one complexity claim.

### **Question 1: invariant two-planes**

This is a structured linear-algebra problem. It can be analyzed through the real rational canonical form of \\(M\\).

For example, if \\(M\\) is diagonalizable over \\(\mathbb R\\) with distinct eigenvalues, invariant two-planes are generated by pairs of eigenvectors. If eigenvalues are repeated, there are continuous families of invariant planes inside eigenspaces. Complex-conjugate pairs introduce real invariant planes as well.

This part should be polynomial-time manageable using exact rational linear algebra and algebraic-number computations.

### **Question 2: rank constraints on invariant planes**

This is the first genuinely geometric step.

The conditions

\\[ M(D)\subseteq D,\qquad \operatorname{rank}(A\_{21}|\_D)\leq r \\]

are algebraic conditions on \\(\operatorname{Gr}(2,K)\\).

For \\(c=2\\), one can exploit the small subspace dimension. A basis matrix \\(X\in\mathbb R^{k\times2}\\) for \\(D\\) satisfies

\\[ MX=XT \\]

for some \\(2\times2\\) matrix \\(T\\), with \\(\operatorname{rank}X=2\\). The rank condition on \\(A\_{21}|\_D\\) can be expressed through minors of \\(A\_{21}X\\).

This gives an explicit algebraic formulation, although it does not by itself establish polynomial-time solvability.

### **Question 3: the pencil condition**

This is where the earlier hyperplane-layer machinery becomes useful.

The total parameter space now includes both:

- variables describing the invariant two-plane \\(D\\);
- variables describing the remaining row-space choices in the fibre.

One must construct charts on the *total* parameter space and test the pencil gcd over the function field of each relevant irreducible chart.

The fixed-direction gcd argument from the \\(c=1\\) paper cannot simply be applied while treating \\(D\\) as fixed if the objective is to decide over a positive-dimensional family of directions.

The full-rank leading-coefficient lemma remains potentially useful, but its application must be justified on each total chart.

## **16. Is the&#x20;**\\(c\geq2\\)**&#x20;problem NP-hard?**

The report does not establish hardness, and I would not infer it from the determinantal formulation.

A determinantal locus can be difficult, but that fact alone does not provide a reduction from a known hard problem. Likewise, the possible complexity of general invariant-subspace varieties does not establish hardness for this particular structured feasibility problem.

My recommendation is to avoid an NP-hardness claim until one has:

1. a precise decision problem;
2. a finite exact encoding of the real feasibility conditions;
3. a reduction from a recognized hard problem;
4. a proof that the reduction preserves the prescribed-row and pencil constraints.

For now, a sensible target is a **complete exact algorithm for&#x20;**\\(c=2\\), followed by a careful bit-complexity analysis under appropriate spectral assumptions.

# **Part IX. A recommended research roadmap**

I would organize the next stage into the following sequence.

## **Phase 1. Repair the definitions and the&#x20;**\\(c=1\\)**&#x20;paper**

Highest priority

1. Replace the ambiguous layer notation with\
   \\[\
   c=k-\rho,\qquad t=q-\rho.\
   \\]
2. State explicitly whether \\(\dim V=q\\) is assumed.
3. Correct the relation between \\(\omega\\), \\(\dim(V\cap K)\\), and \\(\dim(K\cap V^\perp)\\).
4. Identify the dimension hypothesis as the \\(K\\)-split condition.
5. Check the \\(c=1\\) paper to ensure that every use of\
   \\[\
   \omega=\dim(V\cap K)\
   \\]\
   is justified by the construction, rather than asserted as a consequence of (5a).

The report is right to flag this as a foundational correction, not merely a \\(c\geq2\\) issue.

## **Phase 2. Separate the two&#x20;**\\(c\\)**-layer problems**

Write down two formal definitions:

- **Full&#x20;**\\(c\\)**-layer:** all designs with \\(\dim\ker H=c\\).
- \\(K\\)**-split&#x20;**\\(c\\)**-layer:** full \\(c\\)-layer designs satisfying the splitting condition (4).

Then state explicitly which one the next paper studies.

I recommend making the \\(K\\)-split problem the immediate subject of the \\(c=2\\) paper, while retaining the full problem as the ultimate objective.

## **Phase 3. Rebuild the fixed-direction fibre**

For the full problem, use

\\[ \mathcal F_D= \left\\{ V\in\operatorname{Gr}(q,(D+AD)^\perp): V_0\subseteq V,\  K\cap V^\perp=D \right\\}, \\]

with (5b) imposed afterward.

For the \\(K\\)-split problem, use the simpler fibre

\\[ \operatorname{Gr}\left( t-\dim W_0,\\, T_D/W_0 \right), \\]

where

\\[ T_D=K^\perp\cap(A\_{21}D)^\perp, \qquad W_0=P\_{K^\perp}(V_0). \\]

These two formulae should replace the current II.4 fibre statement.

## **Phase 4. Complete the&#x20;**\\(c=2\\)**&#x20;base geometry**

Study

\\[ \mathcal I_2(M) = \\{D\in\operatorname{Gr}(2,K):M(D)\subseteq D\\} \\]

and its rank strata

\\[ \operatorname{rank}(A\_{21}|\_D)=0,1,2. \\]

The main deliverable should be a theorem describing the components, dimensions, and real points of these strata under specified assumptions on \\(M\\).

I would begin with three cases:

1. \\(M\\) has simple real spectrum.
2. \\(M\\) is diagonalizable but has repeated eigenvalues.
3. \\(M\\) has nontrivial Jordan blocks or nonreal conjugate eigenpairs.

This will show exactly where the geometry becomes complicated.

## **Phase 5. Reintroduce (5b)**

Once the base and fibre are correct, impose the pencil condition.

The \\(c=1\\) gcd method provides a plausible strategy, but the charts must include the direction variables. In particular:

- construct a finite chart cover of the total base–fibre family;
- separate irreducible components or otherwise account for reducibility;
- establish the full-rank leading-coefficient condition on each admissible chart;
- compute the gcd over the corresponding function field;
- justify the passage from generic chart computations to real feasible points.

This is the stage where the previous paper's algebraic decision machinery becomes relevant.

## **Phase 6. Only then investigate complexity**

After obtaining an exact \\(c=2\\) decision procedure, measure:

- the number of invariant-subspace charts;
- the number and degrees of determinantal equations;
- the number of fibre charts;
- the number and degrees of pencil minors;
- the coefficient heights and algebraic-number field degrees.

Only then is it meaningful to decide whether a polynomial-time result, a fixed-parameter result, or a hardness reduction is the right target.

# **Part X. Direct answers to Q1–Q6**

| Question                                  | Assessment                                                                                              | Recommendation                                                                                                            |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Q1: Which layer index?                    | \\(c\_{\rm new}\\) is the natural geometric index.                                                      | Use \\(c=k-\rho\\); rename \\(c\_{\rm old}\\) as \\(t=q-\rho\\).                                                          |
| Q2: Keep the dimension hypothesis?        | The conditional theorem is correct, but it describes a restricted subclass.                             | Study the \\(K\\)-split subclass first; do not redefine the full problem around it without a normalization theorem.       |
| Q3: Is the invariant-subspace base right? | Yes for the \\(K\\)-split problem.                                                                      | Use \\(\mathcal I_2(M)\\), then stratify by \\(\operatorname{rank}(A\_{21}\|\_D)\\).                                      |
| Q4: Is the proposed fibre correct?        | No. It contains the contradiction \\(D\subseteq V\\) while \\(D\perp V\\).                              | Replace it with (9) for the full problem and (14) for the split problem.                                                  |
| Q5: Are components and degrees known?     | There is a determinantal formulation, but no universal component or degree description follows from it. | Exploit the Jordan structure of \\(M\\) and the rank strata of \\(A\_{21}\|\_D\\) for \\(c=2\\).                          |
| Q6: Is II.3 correct?                      | Yes. The proof is complete under its stated dimension hypothesis.                                       | Present the hypothesis as a \\(K\\)-splitting condition and verify the counterexample using the full \\(A\_{21}\\) block. |

107_c_ge_2_roadmap.md

## **Final recommendation**

I think the project has a good and potentially productive route into \\(c\geq2\\), but Report 107 reveals that the next paper should begin with a corrected structural theorem, not immediately with a complexity theorem.

The most valuable next result would be:

> **Theorem (Structure of the&#x20;**\\(K\\)**-split&#x20;**\\(c=2\\)**&#x20;design family).**\
> Under the \\(K\\)-split condition, every admissible compressed kernel \\(D\\) is an \\(M\\)-invariant two-dimensional subspace of \\(K\\). On each constant-rank stratum of \\(A\_{21}|\_D\\), the prescribed-row-compatible row-space choices form a relative Grassmann bundle, with the pencil condition selecting the feasible subset.

This theorem would provide a rigorous bridge from the hyperplane layer to the next layer. It would also identify exactly which parts of the \\(c=1\\) paper generalize and which parts depend essentially on the one-dimensional kernel.

**My strongest advice is to settle the fibre formula before doing anything else.** The contradiction in II.4 is fundamental, but resolving it actually gives a cleaner geometry: in the split problem, the \\(K\\)-component of the row space is determined by \\(D\\), and the remaining Grassmannian freedom lies entirely in \\(K^\perp\\). That is a much more manageable starting point for the \\(c=2\\) project.