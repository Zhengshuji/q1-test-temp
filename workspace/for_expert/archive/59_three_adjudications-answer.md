# Research adjudication of Report 59: the three corrections and the project's next bottlenecks

The report identifies three points that materially affect the project’s direction: the constraint imposed by the fixed rows \\(L_0\\), the geometry of \\(S\_{2,3}\\), and the proposed count of invariant subspaces. It also raises three practical questions about the normalized \\(c=2\\) instances, the \\(\exists\mathbb R\\) certificate, and the \\(c=3\\) classification.

My overall assessment is:

1. The \\(W_L\\) constraint is correct and should be incorporated into the main reduction. In the important case \\(\dim W_L=c\\), the admissible plane is forced. The six-layer classification then becomes a classification of one plane, not an enumeration of candidate planes.
2. The proposed correction concerning \\(S\_{2,3}\\) is conditionally correct. The set is open and irreducible only if the ambient setup really guarantees \\(\dim(W+A_0(W))\leq 3\\) for every \\(W\\). That dimension restriction must be stated and proved. Without it, the report's argument is incomplete.
3. The invariant-part component bound is not yet established. The proposed chain parametrization contains a necessary-condition problem for Jordan blocks of length \\(c>2\\), and the claimed affine-fibre structure requires a more careful proof.
4. The normalized \\(c=2\\) feasibility problem is now the most valuable immediate mathematical target. It admits a particularly simple spectral criterion in the \\(q=3,\omega=2\\) case. This should be used to replace random search with an exact symbolic test.
5. The direct polynomial certificate for \\(\exists\mathbb R\\) membership is sound in principle, provided normal rank is imposed separately and the rank upper bound supplied by (5a) is encoded correctly.
6. The eleven \\(c=3\\) strata cannot be certified from the current report alone. The exact list is needed.
7. I recommend a revised order: first formalize the \\(W_L\\) reduction, then attack normalized \\(c=2\\) feasibility, prove the pair-preserving lift theorem, and develop the \\(\exists\mathbb R\\) result in parallel.

I discuss each point below.

## 1. The \\(W_L\\) constraint: correct, important, and algorithmically consequential

The report defines

\\[ W_L=\ker \begin{bmatrix} L_0N_K\\\ L_0AN_K \end{bmatrix}. \\]

It then claims

\\[ V=\ker H\subseteq W_L. \\]

This is correct.

### 1.1 Proof

Recall

\\[ H=LN_K,\qquad H_A=LAN_K, \\]

and

\\[ V=\ker H. \\]

The first \\(r\\) rows of \\(H\\) and \\(H_A\\) are respectively

\\[ L_0N_K,\qquad L_0AN_K. \\]

The compression of condition (5a) gives

\\[ \ker H\subseteq\ker H_A. \\]

Thus, for every \\(v\in V\\),

\\[ Hv=0,\qquad H_Av=0. \\]

Taking the first \\(r\\) coordinates of these two equations gives

\\[ L_0N_Kv=0,\qquad L_0AN_Kv=0. \\]

Therefore

\\[ \boxed{ V\subseteq \ker \begin{bmatrix} L_0N_K\\\ L_0AN_K \end{bmatrix} =W_L. } \\]

There is no additional hypothesis needed for this inclusion beyond the stated definitions and (5a).

### 1.2 The forced-plane consequence is also correct

Since

\\[ \dim V=c, \\]

we have

\\[ c\leq \dim W_L. \\]

If

\\[ \boxed{\dim W_L=c,} \\]

then the inclusion \\(V\subseteq W_L\\) between two subspaces of equal dimension forces

\\[ \boxed{V=W_L.} \\]

Consequently, in the reported cases

\\[ k=4,\qquad \omega=2,\qquad c=2, \\]

and

\\[ \operatorname{rank} \begin{bmatrix} L_0N_K\\\ L_0AN_K \end{bmatrix}=2, \\]

the plane \\(V\\) is uniquely determined.

This is a meaningful simplification. The six-layer classification is no longer an enumeration of six possible families of planes. Instead, one computes the unique plane and determines which geometric type it belongs to.

That distinction should be made explicit in the paper and in the implementation.

### 1.3 What if \\(\dim W_L>c\\)?

Then the correct candidate space is

\\[ \boxed{\operatorname{Gr}(c,W_L),} \\]

not the full Grassmannian \\(\operatorname{Gr}(c,K_0)\\).

The six-layer classification can still be used, but each stratum must be intersected with this restricted Grassmannian.

There is one important qualification: the classification is still governed by the action of \\(A\\) on the relevant ambient space, not necessarily by an endomorphism of \\(W_L\\). In general,

\\[ A(W_L)\not\subseteq W_L. \\]

Thus, one must retain the original definitions

\\[ W=V\cap A^{-1}V,\qquad U=W+A(W). \\]

One cannot automatically replace \\(A\\) by a restriction \\(A|\_{W_L}\\).

### 1.4 A useful rank identity

Let

\\[ D_L= \begin{bmatrix} L_0N_K\\\ L_0AN_K \end{bmatrix}. \\]

Then

\\[ \dim W_L=k-\operatorname{rank}D_L. \\]

Since \\(V\subseteq W_L\\), every feasible compression satisfies

\\[ \boxed{ \omega=k-\dim V \geq \operatorname{rank}D_L. } \\]

This gives an immediate necessary lower bound on the compression rank:

\\[ \boxed{ \omega\geq \operatorname{rank} \begin{bmatrix} L_0N_K\\\ L_0AN_K \end{bmatrix}. } \\]

This is useful even when \\(V\\) is not forced. It can eliminate entire rank layers before any spectral calculation.

### 1.5 Recommendation: make this a preliminary theorem

I would place the following lemma before the six-layer classification.

Fixed-row compression lemma. For every feasible \\(L=[L_0;R]\\), the compression kernel \\(V=\ker(LN_K)\\) satisfies

\\[ V\subseteq W_L. \\]

Consequently,

\\[ \omega\geq \operatorname{rank}D_L. \\]

If equality holds, then \\(V=W_L\\) is uniquely determined.

This is elementary, but its algorithmic consequences are substantial.

My recommendation: divide the \\(c=2\\) algorithm into two branches.

- Forced-plane branch: \\(\dim W_L=2\\). Compute \\(V=W_L\\), determine its type, and test the corresponding pencil.
- Variable-plane branch: \\(\dim W_L>2\\). Enumerate the appropriate strata inside \\(\operatorname{Gr}(2,W_L)\\), not \\(\operatorname{Gr}(2,K_0)\\).

This is a better algorithmic description than beginning with six unrestricted families. It also makes the algorithm more efficient and more faithful to the actual constraints. The report's argument and numerical setting are given in its first adjudication point.&#x20;

59_three_adjudications.md



## 2. The \\(S\_{2,3}\\) issue: the correction is right under an additional dimension hypothesis

This is the most important geometric correction in the report, because it affects the proposed \\(c=2\\) component bound.

The report claims

\\[ S\_{2,3} = \\{W\in\operatorname{Gr}(2,D): \dim(W+A_0(W))=3\\} \\]

is open and irreducible.

The argument is that, for a two-dimensional \\(W\\),

\\[ \dim(W+A_0(W))\in\\{2,3\\}, \\]

so

\\[ \dim(W+A_0(W))=3 \iff A_0(W)\not\subseteq W. \\]

If this dimension restriction is valid, the argument is correct.

The problem is that the dimension restriction is not automatic for an arbitrary linear map \\(A_0:D\to D\\).

### 2.1 The general dimension calculation

For any two-dimensional subspace \\(W\\),

\\[ \dim(W+A_0(W)) = \dim W+\dim A_0(W)-\dim(W\cap A_0(W)). \\]

Since \\(\dim W=2\\) and \\(\dim A_0(W)\leq2\\), the possible values are

\\[ 2,\quad 3,\quad 4. \\]

In particular,

\\[ \dim(W+A_0(W))=4 \\]

is possible when

\\[ \dim A_0(W)=2,\qquad W\cap A_0(W)=\\{0\\}. \\]

Therefore, in the unrestricted setting,

\\[ A_0(W)\not\subseteq W \\]

means

\\[ \dim(W+A_0(W))>2, \\]

but it does not necessarily mean that the dimension equals three.

The correct general identity is

\\[ \boxed{ \begin{aligned} S\_{2,3} &=\\{W:\dim(W+A_0(W))=3\\}\\\ &=\\{W:\operatorname{rank}([W,A_0(W)])=3\\}, \end{aligned} } \\]

where the last expression is interpreted in a local coordinate chart for the Grassmannian.

This is an exact-rank condition in the unrestricted setting.

### 2.2 When is the report's open-set argument valid?

Suppose the project has an additional structural hypothesis ensuring

\\[ \boxed{ \dim(W+A_0(W))\leq3 \quad\text{for every }W\in\operatorname{Gr}(2,D). } \\]

Then the dimension can only be two or three, and

\\[ \dim(W+A_0(W))=2 \iff A_0(W)\subseteq W. \\]

The invariant-plane condition

\\[ A_0(W)\subseteq W \\]

is closed: in a local basis \\(u,v\\) for \\(W\\), it is expressed by the vanishing of the appropriate \\(3\times3\\) minors of

\\[ [u,v,A_0u,A_0v]. \\]

It follows that

\\[ \boxed{ S\_{2,3} = \operatorname{Gr}(2,D) \setminus \\{W:A_0(W)\subseteq W\\} } \\]

is open.

The Grassmannian \\(\operatorname{Gr}(2,D)\\) is irreducible. Every nonempty open subset of an irreducible variety is irreducible. Hence

\\[ \boxed{S\_{2,3}\text{ is irreducible, if nonempty.}} \\]

This is a valid argument.

### 2.3 The previous rank-one description is not equivalent

The report also correctly identifies a weakness in the previous audit's description involving

\\[ \operatorname{rank}(f|\_W)=1. \\]

The condition

\\[ \dim(W\cap A_0(W))=1 \\]

is not equivalent to

\\[ \dim(W+A_0(W))=3 \\]

without further assumptions on \\(\dim A_0(W)\\).

For example, if

\\[ W\cap A_0(W)=\\{0\\} \quad\text{and}\quad \dim A_0(W)=1, \\]

then

\\[ \dim(W+A_0(W))=3 \\]

although the intersection has dimension zero.

Conversely, the rank of a map describing the intersection depends on the precise map and its domain/codomain. It cannot be substituted for the dimension of the sum without proving the relevant rank identity.

Thus, I agree with the report's objection: the rank-one condition is not a general characterization of \\(S\_{2,3}\\).

### 2.4 What must be checked before restoring the component bound?

The report proposes restoring

\\[ \boxed{ \binom{s}{3} +\binom{s}{2} +2s^2+4s+3. } \\]

I would not restore this bound yet. First, establish the following lemma in the exact setting of the previous component-count argument.

Required lemma. For every \\(W\in\operatorname{Gr}(2,D)\\),

\\[ \dim(W+A_0(W))\leq3. \\]

If this follows from the definition of \\(D\\) and \\(A_0\\), prove it explicitly. If it follows only on a particular eigenspace, quotient, or restricted stratum, state that restriction.

Then prove that the relevant \\(S\_{2,3}\\) is a nonempty open subset of the relevant irreducible base. Finally, verify that the associated \\(V\\)-fibres and lifted fibres preserve irreducibility.

The last point matters: an irreducible base stratum does not by itself imply that the corresponding compressed or lifted incidence space is irreducible.

### 2.5 Recommendation

I recommend replacing the previous audit's blanket statement that \\(S\_{2,3}\\) is a potentially reducible exact-rank stratum with the following conditional conclusion:

> If the ambient construction guarantees \\(\dim(W+A_0(W))\leq3\\) for every \\(W\in\operatorname{Gr}(2,D)\\), then \\(S\_{2,3}\\) is a Zariski-open subset of the Grassmannian and is irreducible whenever nonempty. Without this dimension bound, the claimed openness does not follow.

This is the mathematically safe resolution. The report's proposed corrected bound remains a candidate, not yet a theorem.&#x20;

59_three_adjudications.md



## 3. The invariant-part count: promising idea, but the present argument is insufficient

The report proposes that, for \\(t=c\\), the Jordan type of \\(A|\_V\\) is an eigenvalue-labelled partition and that each block of invariant subspaces is irreducible.

It then concludes

\\[ N\_{\mathrm{inv}}(c) \leq \sum\_{\lambda\vdash c}s^{b(\lambda)} \leq p(c)s^c. \\]

This conclusion is not yet justified.

The difficulty is not the fact that invariant subspaces can be described using Jordan chains. That is standard. The difficulty is the assertion that the parameter space of chains of a prescribed Jordan type is irreducible, with the stated projective base and affine fibres.

### 3.1 A necessary condition for a Jordan chain of length \\(c\\)

Fix an eigenvalue \\(\lambda\\) and write

\\[ T=A-\lambda I. \\]

A Jordan chain of length \\(c\\) in \\(K_0\\) consists of vectors

\\[ x_0,x_1,\ldots,x\_{c-1}\in K_0 \\]

such that

\\[ Tx_0=0,\qquad Tx_1=x_0,\qquad \ldots,\qquad Tx\_{c-1}=x\_{c-2}, \\]

with \\(x_0\neq0\\).

In particular,

\\[ x_0=T^{c-1}x\_{c-1}. \\]

Therefore

\\[ \boxed{ x_0\in \ker T\cap T^{c-1}(K_0). } \\]

This is a necessary condition for the bottom eigenvector of a length-\\(c\\) chain.

The report's proposed base is

\\[ \left\\{ \ell\subseteq E\_\lambda\cap K_0: \ell\subseteq(A-\lambda I)(K_0) \right\\}. \\]

For \\(c>2\\), this only imposes one image condition. It does not impose the necessary condition

\\[ \ell\subseteq(A-\lambda I)^{c-1}(K_0). \\]

Thus, the stated base is too large in general.

For \\(c=2\\), the single-image condition is the correct first condition. For longer chains, it must be strengthened.

### 3.2 The corrected base is still not enough to prove irreducibility

One might replace the base by

\\[ \mathbb P\big( \ker T\cap T^{c-1}(K_0) \big). \\]

This is a projective linear subspace, so it is irreducible whenever nonempty.

However, that does not finish the argument.

One must still show that the space of all compatible chain lifts, modulo the change-of-chain operations that preserve the same invariant subspace, has irreducible fibres over this base.

The raw set of chain vectors is not the same as the variety of invariant subspaces. A single invariant subspace may admit multiple chain bases. The basis-change freedom must be accounted for.

A valid proof needs to specify:

1. the parameter space of chains;
2. the equivalence relation identifying chains that span the same subspace;
3. the map from the chain parameter space to the relevant Grassmannian;
4. the fibres of that map;
5. why the resulting image, or its appropriate quotient, is irreducible.

A statement that the chain preimages are affine does not by itself prove that the variety of invariant subspaces is an affine bundle over the proposed base.

### 3.3 Multiple Jordan blocks introduce further interactions

For a fixed eigenvalue, a partition

\\[ \lambda=(\lambda_1,\ldots,\lambda_m) \\]

describes the Jordan block sizes of the restriction \\(A|\_V\\).

When \\(m>1\\), the chains need not be independent in the ambient space. Their intersections, linear independence, and compatibility with the ambient Jordan filtration all matter.

The space of submodules of a fixed module with a prescribed module type is generally a representation-theoretic parameter space. Its irreducibility is not automatic merely because the partition is fixed.

This is precisely why the language of invariant-subspace varieties and quiver Grassmannians is useful, but it should not be used as a shortcut to an irreducibility assertion.

### 3.4 What can safely be claimed now?

The number

\\[ \sum\_{\lambda\vdash c}s^{b(\lambda)} \\]

is a count of possible eigenvalue-labelled Jordan-type descriptions, under the intended interpretation of the notation.

It is not yet a proven upper bound on irreducible components.

The distinction is:

- Jordan-type count: counts possible labels or combinatorial types.
- Component count: requires a proof that each corresponding parameter space has at most one irreducible component, or a bound on the number of components within each type.

The report establishes the former more convincingly than the latter.

### 3.5 Recommendation: isolate the one-block theorem first

Do not try to prove the general invariant-part bound immediately.

Start with the following restricted problem:

> Fix \\(\lambda\\) and \\(c\\). Describe the variety of \\(c\\)-dimensional \\(A\\)-invariant subspaces \\(V\subseteq K_0\\) such that \\(A|\_V\\) has one Jordan block of size \\(c\\). Determine whether this variety is irreducible.

For this case, the corrected bottom-vector condition is

\\[ \ell\subseteq \ker(A-\lambda I) \cap (A-\lambda I)^{c-1}(K_0). \\]

Then construct the chain-lifting variety and prove its relation to the invariant-subspace variety.

If that result succeeds, proceed to partitions with two blocks. This will expose exactly where interactions between chains begin.

My verdict is therefore:



Not yet proved

&#x20;The proposed invariant-part component bound is a plausible research direction, but the current chain-parametrization argument does not establish it.&#x20;

59_three_adjudications.md



## 4. The normalized \\(c=2\\) instances: a much simpler spectral criterion is available

This is, in my view, the most important immediate computational and mathematical opportunity in the report.

The report says that in instances 16/21,

\\[ V=W_L \\]

is forced, the admissibility equations are consistent, but no good \\(3\times k\\) pencil appeared in 600 random choices of the free parameters.

A random search failure is not a proof of infeasibility. However, the dimensions

\\[ q=3,\qquad \omega=2 \\]

make it possible to write a particularly simple exact criterion for spectral feasibility.

### 4.1 Reduce the pencil to a map on a two-dimensional space

Assume

\\[ \operatorname{rank}H=2,\qquad \ker H=V,\qquad \ker H\subseteq\ker H_A. \\]

Then there is a unique linear map

\\[ Z:\operatorname{im}H\longrightarrow\mathbb C^3 \\]

such that

\\[ H_A=ZH. \\]

The pencil becomes

\\[ P(\lambda)=\lambda H-H_A =(\lambda I\_{\mathbb C^3}-Z)H, \\]

where \\(Z\\) is understood on \\(\operatorname{im}H\\).

Since \\(H\\) maps onto the two-dimensional space \\(\operatorname{im}H\\),

\\[ \operatorname{rank}P(\lambda) = \operatorname{rank} \left((\lambda I-Z)|\_{\operatorname{im}H}\right). \\]

Choose a complement

\\[ \mathbb C^3=\operatorname{im}H\oplus E, \qquad \dim E=1. \\]

Relative to this decomposition, write

\\[ Z= \begin{bmatrix} A\_\*\\\ b \end{bmatrix}, \\]

where

\\[ A\_\*\in\mathbb C^{2\times2}, \qquad b\in\mathbb C^{1\times2}. \\]

Then

\\[ P(\lambda) \quad\text{has rank }2 \\]

for every \\(\lambda\in\mathbb C\\) if and only if

\\[ \boxed{ \ker b\text{ contains no eigenvector of }A\_\*. } \\]

This is exactly the block criterion specialized to the case \\(q=3,\omega=2\\).

### 4.2 Equivalent determinant criterion

If \\(b\neq0\\), then \\(\ker b\\) is a one-dimensional subspace of \\(\mathbb C^2\\).

It contains an eigenvector of \\(A\_\*\\) precisely when it is \\(A\_\*\\)-invariant. Since \\(\ker b\\) is one-dimensional, invariance is equivalent to

\\[ bA\_\*=\mu b \\]

for some scalar \\(\mu\\).

Equivalently, the rows \\(b\\) and \\(bA\_\*\\) are linearly dependent.

Therefore the good-pencil condition is

\\[ \boxed{ \operatorname{rank} \begin{bmatrix} b\\\ bA\_\* \end{bmatrix}=2. } \\]

In coordinates, this is the nonvanishing of one \\(2\times2\\) determinant:

\\[ \boxed{ \det \begin{bmatrix} b\\\ bA\_\* \end{bmatrix}\neq0. } \\]

This is a very useful simplification.

It avoids computing a polynomial gcd for every random candidate. It also avoids searching over \\(\lambda\\).

### 4.3 Interpretation

The condition has a simple meaning:

- \\(A\_\*\\) describes the part of \\(Z\\) that remains inside \\(\operatorname{im}H\\).
- \\(b\\) measures the component of \\(Z\\) transverse to \\(\operatorname{im}H\\).
- A bad eigenvector is one that remains entirely inside \\(\operatorname{im}H\\) and is also an eigenvector of \\(A\_\*\\).
- The condition\
  \\[\
  \operatorname{rank}\begin{bmatrix}b\bA\_\*\end{bmatrix}=2\
  \\]\
  says that the transverse component detects every eigenvector direction of \\(A\_\*\\).

Over \\(\mathbb C\\), every \\(2\times2\\) matrix has an eigenvector. Thus, for a good pencil, \\(b\\) must be nonzero and must not annihilate any eigenvector of \\(A\_\*\\).

### 4.4 How to use this to settle instances 16/21

The key is to parameterize the free row or rows of \\(L\\) exactly.

Suppose the free rows are parameterized by variables

\\[ \theta=(\theta_1,\ldots,\theta_m). \\]

The matrices \\(H(\theta)\\) and \\(H_A(\theta)\\) are affine-linear in these variables. On a coordinate chart where a chosen \\(2\times2\\) minor of \\(H\\) is nonzero, one can calculate \\(Z(\theta)\\), and hence \\(A\_\*(\theta)\\) and \\(b(\theta)\\).

The good locus is then described by

\\[ \boxed{ \det \begin{bmatrix} b(\theta)\\\ b(\theta)A\_\*(\theta) \end{bmatrix}\neq0. } \\]

Because the chosen chart involves a nonzero denominator, clear denominators to obtain a polynomial numerator

\\[ g(\theta). \\]

Then there are two possibilities.

Case A: \\(g\\) is identically zero.

Then no admissible parameter in that chart produces a good pencil. Repeat over all possible nonzero \\(2\times2\\) pivot minors of \\(H\\). If the numerator vanishes identically on every chart, the instance is infeasible.

Case B: \\(g\\) is not identically zero.

Then the good locus is a nonempty Zariski-open subset of the admissible parameter space, provided that parameter space itself is nonempty and the chart is genuinely attainable.

In particular, generic parameter choices in that chart are good.

This gives a much stronger interpretation of the 600 failed random trials.

- If the good polynomial is nonzero, repeated failures may indicate that the random sampling distribution is poor, the chart is poorly conditioned, or the parameterization has hidden restrictions.
- If the polynomial is identically zero, the numerical failure is explained by a structural obstruction.

### 4.5 An alternative exact test

For a fixed candidate pencil, compute the \\(2\times2\\) minors of

\\[ P(\lambda)=\lambda H-H_A. \\]

The pencil is good precisely when:

1. its normal rank is two; and
2. the gcd of all its \\(2\times2\\) minors is a nonzero constant.

For the normalized \\(3\times4\\) case, the block determinant above is a more efficient structural test once \\(A\_\*,b\\) are available.

### 4.6 Recommendation

I would stop random search for instances 16/21 until the following has been done:

1. Compute the forced plane \\(V=W_L\\) exactly.
2. Construct a symbolic affine parameterization of all free rows satisfying the kernel constraints.
3. Identify all possible pivot charts for \\(H\\).
4. Derive the corresponding good determinant polynomial.
5. Determine whether each polynomial is identically zero.
6. If all vanish, write down a certificate of infeasibility.
7. If one is nonzero, produce an exact rational or algebraic point in the good locus.

This is likely to settle the most pressing \\(c=2\\) question more efficiently than further random experiments.

The determinant criterion is my additional deduction from the report's compressed-pencil framework; it is not itself stated in the uploaded report.

## 5. The direct \\(\exists\mathbb R\\) certificate: the normal-rank condition is essential and correctly placed

I agree with the report's concern that

\\[ QYQ=Q \\]

alone does not force the desired rank.

Let

\\[ D_0= \begin{bmatrix} L\\\CA\\\C \end{bmatrix}, \qquad s=\operatorname{rank}D_0, \\]

and

\\[ Q(\lambda)= \begin{bmatrix} \lambda L-LA\\\ CA\\\ C \end{bmatrix}. \\]

### 5.1 Why (5a) gives the rank upper bound

Condition (5a) says

\\[ \operatorname{rank} \begin{bmatrix} LA\\\D_0 \end{bmatrix} = \operatorname{rank}D_0=s. \\]

Hence every row of \\(LA\\) belongs to the row space of \\(D_0\\).

Since the rows of \\(L\\), \\(CA\\), and \\(C\\) also belong to that row space, every row of \\(Q(\lambda)\\) belongs to the row space of \\(D_0\\).

Therefore

\\[ \boxed{ \operatorname{rank}Q(\lambda)\leq s \quad\text{for every }\lambda. } \\]

Thus (5b) is equivalent to

\\[ \operatorname{rank}Q(\lambda)=s \quad\text{for every }\lambda\in\mathbb C. \\]

### 5.2 Why normal rank must be imposed separately

The polynomial identity

\\[ QYQ=Q \\]

does not imply that the normal rank is \\(s\\).

For example, the zero polynomial matrix satisfies this identity with \\(Y=0\\), regardless of the target rank \\(s\\).

More generally, the identity only certifies that the polynomial matrix admits a generalized inverse on its own image. It does not say that its generic rank equals the required value.

Therefore one must impose

\\[ \boxed{\operatorname{normalrank}Q=s.} \\]

Because the rank is already bounded above by \\(s\\), this is equivalent to requiring that at least one \\(s\times s\\) minor is not the zero polynomial.

For a degree-one pencil, that condition can be encoded by introducing an auxiliary scalar \\(\lambda_0\\) and requiring that at least one \\(s\times s\\) minor of \\(Q(\lambda_0)\\) be nonzero.

The auxiliary \\(\lambda_0\\) is not required to be a special eigenvalue. It is simply a witness that the normal rank is \\(s\\).

### 5.3 Why the polynomial identity then gives constant rank

Assume:

1. \\(Q(\lambda)\\) has normal rank \\(s\\);
2. \\(Q(\lambda)Y(\lambda)Q(\lambda)=Q(\lambda)\\) as a polynomial identity.

Use the Smith normal form over \\(\mathbb C[\lambda]\\):

\\[ U(\lambda)Q(\lambda)V(\lambda) = \operatorname{diag}(d_1,\ldots,d_s,0,\ldots,0), \\]

where \\(U,V\\) are unimodular polynomial matrices and the \\(d_i\\) are nonzero invariant factors.

Transforming the generalized-inverse identity by \\(U,V\\) gives a polynomial generalized inverse identity for the diagonal Smith form.

For each \\(i\leq s\\), the corresponding diagonal equation implies

\\[ d_i^2 y\_{ii}=d_i \\]

for some polynomial \\(y\_{ii}\\). Since \\(d_i\neq0\\),

\\[ d_i y\_{ii}=1. \\]

Thus \\(d_i\\) is a unit in \\(\mathbb C[\lambda]\\), so it is a nonzero constant.

Consequently, every nonzero invariant factor is constant, and the Smith form has rank \\(s\\) at every finite complex \\(\lambda\\).

Hence

\\[ \boxed{ \operatorname{rank}Q(\lambda)=s \quad\forall\lambda\in\mathbb C. } \\]

This proves the converse that the report is seeking.

### 5.4 Degree bound

The report uses

\\[ \deg Y\leq2s-2. \\]

For a degree-one polynomial matrix whose rank is constantly \\(s\\), this is consistent with the polynomial generalized-inverse construction based on maximal minors, Bézout coefficients, and embedded adjugates.

The argument is:

- Every \\(s\times s\\) minor has degree at most \\(s\\).
- Constant rank at every finite complex point implies that the maximal minors have no common finite root.
- Their gcd is therefore a nonzero constant.
- Bézout's identity gives a polynomial combination of the maximal minors equal to one.
- Embedded adjugates convert that scalar identity into a matrix identity \\(QYQ=Q\\).
- The adjugate terms have degree at most \\(s-1\\), and the Bézout coefficients can be chosen with degree at most \\(s-1\\), giving\
  \\[\
  \deg Y\leq2s-2.\
  \\]

This is the right route to a finite existential certificate.

### 5.5 Is \\(s=0\\) the only boundary case?

For this degree bound, yes.

If \\(s=0\\), then \\(D_0=0\\), and (5a) forces \\(LA=0\\). Also \\(L=CA=C=0\\) as matrices in the relevant row space. Thus

\\[ Q(\lambda)=0 \\]

and (5b) is automatic.

The certificate is simply \\(Y=0\\), but the expression

\\[ 2s-2=-2 \\]

is not meaningful as a polynomial-degree bound.

So the correct formulation is:

- If \\(s=0\\), treat the case separately and take \\(Y=0\\).
- If \\(s\geq1\\), use \\(\deg Y\leq2s-2\\).

No additional boundary case appears from this degree argument.

### 5.6 One qualification for the complexity theorem

The direct certificate is a route to membership in \\(\exists\mathbb R\\), not hardness.

To complete the formal reduction, encode all of the following:

- the fixed rows \\(L_0\\);
- the variable entries of \\(R\\);
- the full-row-rank condition on \\(L\\);
- the exact rank \\(s\\) of \\(D_0\\);
- the rank equality in (5a);
- the normal-rank witness for \\(Q\\);
- the coefficients of \\(Y\\);
- the polynomial identity \\(QYQ=Q\\), coefficient by coefficient.

The rank conditions can be expressed using vanishing and nonvanishing of minors. Over \\(\mathbb C\\), convert complex variables into real and imaginary parts.

For a minimum-order problem, use a finite disjunction over the allowed values of \\(q\\). Do not assume feasibility is monotone in \\(q\\) unless that has been separately proved.

Verdict: the normal-rank condition is essential and correctly placed. The direct certificate is a sound candidate for an \\(\exists\mathbb R\\)-membership proof, with \\(s=0\\) handled separately. It does not establish \\(\exists\mathbb R\\)-hardness.&#x20;

59_three_adjudications.md



## 6. The eleven \\(c=3\\) strata: the exact list is necessary

The report asks whether the eleven strata are exhaustive and mutually exclusive.

I cannot responsibly certify this from the current report because the actual list is not included.

The number eleven is not enough to establish exhaustiveness. In particular, one must distinguish:

1. the dimension \\(t=\dim(V\cap A^{-1}V)\\);
2. the dimension \\(u=\dim(W+A(W))\\);
3. the eigenvalue data of \\(A|\_W\\);
4. the Jordan partition of each eigenvalue;
5. the relative position of \\(W\\) and \\(A(W)\\);
6. any additional chain-lifting or incidence conditions.

Two strata with the same Jordan partition may still have different ambient embedding behavior. Conversely, two descriptions that look different may parameterize the same geometric locus.

### 6.1 What I would require for the audit

For each proposed stratum, provide:

- an exact definition as a subset of the relevant Grassmannian or incidence variety;
- the values of \\(t\\) and \\(u\\);
- the Jordan data;
- the defining rank conditions;
- the nonemptiness conditions;
- the proof that it is locally closed;
- the proof that it is disjoint from the other strata;
- the proof that the union covers the entire admissible set.

Only after these checks should component counts be attached.

In particular, the exact-rank strata

\\[ B\_{u,v} = \left\\{ U\in\operatorname{Gr}(u,K_0): \dim(U\cap A^{-1}U)=v \right\\} \\]

are useful as a general organizing framework, but they are not automatically irreducible.

Recommendation: send the eleven-stratum list next. I would audit it in a table with columns for \\((t,u)\\), Jordan type, defining equations, local-closedness, nonemptiness, disjointness, and component status.&#x20;

59_three_adjudications.md



## 7. Revised research priorities

The report's original order is:

1. lift theorem;
2. \\(c=2\\) feasibility;
3. component theorem;
4. \\(\exists\mathbb R\\) in parallel.

I would modify it slightly because the new \\(W_L\\) observation gives a simpler first step.

### Priority 1: formalize the \\(W_L\\) reduction

This should be done immediately.

It gives a rigorous restriction on the admissible Grassmannian:

\\[ V\in\operatorname{Gr}(c,W_L). \\]

It also gives the lower bound

\\[ \omega\geq\operatorname{rank} \begin{bmatrix} L_0N_K\\\ L_0AN_K \end{bmatrix}. \\]

In the equality case, the candidate plane is forced.

This is a short theorem with direct algorithmic value.

### Priority 2: solve the forced \\(c=2\\) feasibility problem

For instances 16/21, do not continue with random sampling as the primary method.

Use

\\[ \operatorname{rank} \begin{bmatrix} b\\\bA\_\* \end{bmatrix}=2 \\]

as the exact spectral condition in the \\(q=3,\omega=2\\) case.

The central question becomes whether the resulting determinant polynomial is identically zero on the admissible free-parameter space.

This can produce either:

- an exact infeasibility proof; or
- an explicit good candidate and a proof of genericity in the corresponding chart.

This is the most concrete unresolved problem in the report.

### Priority 3: complete the pair-preserving lift theorem

The forced-plane reduction concerns the compressed geometry. It does not eliminate the need to prove that the compressed pair \\((H,H_A)\\) can be lifted to actual rows \\(L\\).

The lift theorem should preserve both

\\[ LN_K=H \quad\text{and}\quad LAN_K=H_A. \\]

In particular, the pair-image compatibility condition must be retained. It is not enough to count rows invisible to \\(H\\) alone.

The relevant map is

\\[ \Psi: \mathcal X^\*/\operatorname{row}C \longrightarrow K_0^\*\oplus K_0^\*, \qquad \bar g\longmapsto(gN_K,gAN_K). \\]

A prescribed pair must lie in \\(\operatorname{im}\Psi\\), and the kernel dimension must be large enough to complete the required rows injectively.

This is a structural theorem that should be proved independently of the \\(c=2\\) special case.

### Priority 4: finish \\(\exists\mathbb R\\) membership in parallel

This is a relatively independent route.

The direct-pencil certificate is promising and avoids the need to encode the entire Grassmannian stratification. It can therefore provide a complexity-theoretic result even if the general component geometry remains unresolved.

I would aim for a theorem of the form:

> For rational input data, the fixed-order feasibility problem belongs to \\(\exists\mathbb R\\).

Do not claim completeness or hardness until a reduction from a known \\(\exists\mathbb R\\)-hard problem is supplied.

### Priority 5: prove the \\(c=2\\) component bound

Only after the \\(S\_{2,3}\\) dimension hypothesis and all fibre conditions have been verified should the corrected bound be stated as a theorem.

There are three distinct spaces whose component counts must not be conflated:

1. the base \\(W\\)-strata;
2. the compressed incidence space of \\((H,H_A)\\);
3. the lifted observer space of actual \\(L\\).

An irreducible base stratum does not automatically imply irreducibility of either of the latter two spaces.

### Priority 6: audit \\(c=3\\)

The eleven strata should be checked after the \\(c=2\\) framework is stable. The \\(c=3\\) audit should reuse the same definitions and conventions, rather than introducing a second informal classification.

### Priority 7: return to the general-\\(c\\) component theorem

The general component bound is the most ambitious geometric goal. The invariant-part count should not be used as a theorem until the chain parametrization is repaired. Likewise, the non-invariant part requires actual component bounds for its determinantal strata.

The order I recommend is therefore:

## Recommended work plan

1. Prove the \\(W_L\\) lemma and forced-plane corollary.

   Establish the reduced candidate Grassmannian and the compression-rank lower bound.
2. Resolve the normalized \\(c=2\\) instances exactly.

   Derive the good determinant polynomial and prove whether it vanishes identically.
3. Formalize the pair-preserving lift theorem.

   Include image compatibility and injective completion.
4. Complete the direct-pencil \\(\exists\mathbb R\\) certificate.

   Include normal rank, the polynomial generalized inverse, and the \\(s=0\\) case.
5. Prove the corrected \\(c=2\\) component bound.

   Verify \\(S\_{2,3}\\), all other base strata, and the lifted fibres.
6. Audit the eleven \\(c=3\\) strata.

   Establish exhaustiveness, disjointness, and irreducibility separately.
7. Develop the general-\\(c\\) component theory.

   Repair the invariant-chain argument and establish bounds for the non-invariant strata.

## 8. What I would change in the project's algorithm immediately

The report suggests that the current \\(c=2\\) algorithm may be unnecessarily general for the tested instances. I agree.

I would organize the algorithm as follows.

### Step A: compute the fixed-row restriction

Compute

\\[ D_L= \begin{bmatrix} L_0N_K\\\ L_0AN_K \end{bmatrix}, \qquad W_L=\ker D_L. \\]

If

\\[ \dim W_L\<c, \\]

the rank layer is infeasible.

If

\\[ \dim W_L=c, \\]

set

\\[ V=W_L. \\]

If

\\[ \dim W_L>c, \\]

work over \\(\operatorname{Gr}(c,W_L)\\).

### Step B: impose the invariant-intersection geometry

For each candidate \\(V\\), compute

\\[ W=V\cap A^{-1}V, \qquad t=\dim W, \qquad U=W+A(W). \\]

Use the \\(c=2\\) or \\(c=3\\) classification only after the fixed-row restriction has been imposed.

### Step C: construct the compressed pair

Construct \\(H\\) with

\\[ \ker H=V,\qquad \operatorname{rank}H=\omega. \\]

Then impose

\\[ H_A V=0. \\]

Equivalently,

\\[ \ker H\subseteq\ker H_A. \\]

### Step D: apply the spectral criterion

For each fixed candidate, test

\\[ \operatorname{rank}(\lambda H-H_A)=\omega \quad\forall\lambda. \\]

For the \\(q=3,\omega=2\\) case, use the simpler determinant criterion

\\[ \det \begin{bmatrix} b\\\bA\_\* \end{bmatrix}\neq0. \\]

For more general dimensions, use the gcd of maximal minors or the polynomial generalized-inverse certificate.

### Step E: perform the actual row lift

Use the pair map \\(\Psi\\), not just the first compression map.

Verify:

- the prescribed pair lies in \\(\operatorname{im}\Psi\\);
- the kernel dimension permits injective completion;
- the fixed rows remain fixed;
- the resulting \\(L\\) has full row rank.

### Step F: verify the original conditions

Every successful candidate should finally be checked directly against

\\[ \operatorname{rank}[LA;L;CA;C] = \operatorname{rank}[L;CA;C] \\]

and

\\[ \operatorname{rank} \begin{bmatrix} \lambda L-LA\\\CA\\\C \end{bmatrix} = \operatorname{rank}[L;CA;C] \quad\forall\lambda. \\]

This final check is essential because the project has several layers of reductions. A correct compressed construction is not yet a proof of a valid observer unless the lift has also been verified.

## 9. Three concrete deliverables I would request next

To make the next research round decisive rather than exploratory, I would request three specific outputs.

### Deliverable 1: a normalized \\(c=2\\) feasibility certificate

For instances 16/21, provide:

- exact input matrices;
- the exact basis \\(N_K\\);
- the exact matrix \\(D_L\\);
- the forced plane \\(V=W_L\\);
- the parameterization of all admissible free rows;
- the symbolic determinant polynomial for the good-pencil criterion;
- a proof that it is identically zero or an exact good candidate.

This will settle whether the observed absence of good pencils is structural.

### Deliverable 2: a corrected invariant-subspace parametrization

For a single Jordan block of length \\(c\\), provide:

- the correct base\
  \\[\
  \mathbb P\big(\
  \ker(A-\lambda I)\
  \cap(A-\lambda I)^{c-1}(K_0)\
  \big);\
  \\]
- the chain-lifting parameter space;
- the map to the invariant-subspace Grassmannian;
- the equivalence between chain bases spanning the same subspace;
- a proof of irreducibility, or a counterexample to irreducibility.

This will tell us whether the invariant-part count can be repaired.

### Deliverable 3: the exact eleven-stratum \\(c=3\\) list

The list should contain the defining conditions and not just informal Jordan labels. That will allow a real audit of exhaustiveness and mutual exclusivity.

## 10. Final assessment

The most consequential development in Report 59 is not the proposed component-count correction. It is the discovery that the fixed rows \\(L_0\\) can force the compression kernel \\(V\\).

That observation changes the computational problem substantially. In the forced case, the project is not searching over a Grassmannian at all. It is testing one prescribed plane, followed by a compressed-pencil feasibility problem and a lift problem.

The second important development is the possibility of replacing random \\(c=2\\) pencil search with a single determinant condition. In the \\(q=3,\omega=2\\) case, the condition

\\[ \operatorname{rank} \begin{bmatrix} b\\\bA\_\* \end{bmatrix}=2 \\]

is a sharp, exact test. It should be the next target for the instances where 600 random choices failed.

The geometric corrections also matter. The openness of \\(S\_{2,3}\\) is a real simplification if the dimension bound is valid, but that bound must be proved in the actual ambient setting. The invariant-part count remains unproved because the proposed chain base is insufficient for longer Jordan chains and the quotient from chains to invariant subspaces has not been controlled.

Finally, the direct-pencil certificate offers a valuable independent result: it appears to give a rigorous path to \\(\exists\mathbb R\\)-membership without resolving the difficult general component geometry. This should be completed in parallel.

My strongest recommendation is to make the next research round about the forced \\(c=2\\) case, not the general component bound. It is the most sharply formulated unresolved problem, the new \\(W_L\\) observation reduces its dimension, and the block criterion gives an exact algebraic test. A rigorous feasibility or infeasibility result there would be a substantial advance and would clarify which parts of the larger geometric program are genuinely necessary.

I would next examine the exact symbolic parameterization and determinant polynomial for instances 16/21; that is the most likely route to a decisive result.