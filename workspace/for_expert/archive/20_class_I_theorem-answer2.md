# Referee report on `20_class_I_theorem.md`



Main theorem B.27: proof is valid

Class I minimum order: established



The central result is a substantial advance: the Class I minimum-order conjecture is proved, not merely supported by computation. The two-case argument is mathematically sound, and its strength lies in the way it combines the equality obstruction B.22 with observability. The proof does not require \\((\ell,A)\\) to be observable, and it does not require a separate spectral analysis in the second case.

There is one point in B.26(3) whose proof should be written more explicitly: the equivalence between (5a) and

\\[ \mathcal VA\subseteq\mathcal V+\langle cA\rangle. \\]

It is correct, but the argument should explicitly use the direct-sum decomposition

\\[ \mathcal V=\operatorname{row}\mathcal L\oplus\langle c\rangle. \\]

I will verify that equivalence carefully, then discuss the boundary case, generalizations, possible sharper lower bounds, paper organization, and the next research target.

## 1. Q1: Is B.26–B.27 complete?

### 1.1 The reduction from \\(\mathcal L\\) to \\(\mathcal Z\\) is correct

Let

\\[ \mathcal Z=\ker\begin{bmatrix}C\\\\\mathcal L\end{bmatrix}, \qquad \mathcal V=\mathcal Z^\perp. \\]

Here \\(C=c^{\mathsf T}\\) and \\(\mathcal L\\) has \\(q\\) rows.

By admissibility,

\\[ \operatorname{rank}\begin{bmatrix}C\\\\\mathcal L\end{bmatrix}=q+1. \\]

The row space of this matrix is exactly \\(\mathcal Z^\perp\\), so

\\[ \mathcal V =\operatorname{row}\begin{bmatrix}\mathcal L\\\c^{\mathsf T}\end{bmatrix}, \qquad \dim\mathcal V=q+1. \\]

This is simply the fundamental theorem of orthogonal complements in finite-dimensional Euclidean space (or annihilators in the algebraic dual, if the paper works over \\(\mathbb C\\)).

Because \\(c^{\mathsf T}\notin\operatorname{row}\mathcal L\\), we have the direct sum

\\[ \boxed{ \mathcal V=\operatorname{row}\mathcal L\oplus \langle c^{\mathsf T}\rangle. } \tag{1.1} \\]

The non-membership follows from the full row-rank condition on the stacked matrix.

This identity is the key to the whole proof. It says that, once \\(\mathcal Z\\) is fixed, the subspace \\(\mathcal V\\) is fixed, and every admissible \\(\mathcal L\\) is a choice of a complementary \\(q\\)-dimensional subspace to \\(\langle c^{\mathsf T}\rangle\\) inside \\(\mathcal V\\).

That is a much more precise statement than merely saying that the spectral condition depends on \\(\mathcal Z\\).

### 1.2 The rank formula for \\(h\\) is correct

For \\(p=r=1\\),

\\[ r_1=\operatorname{rank}\begin{bmatrix}CA\\\C\end{bmatrix} =\operatorname{rank}\begin{bmatrix}c^{\mathsf T}A\\\c^{\mathsf T}\end{bmatrix}. \\]

Since \\((c,A)\\) is observable and \\(n\ge2\\), the rows \\(c^{\mathsf T}\\) and \\(c^{\mathsf T}A\\) are linearly independent. In particular,

\\[ r_1=2. \\]

The row space defining \\(h\\) is

\\[ \operatorname{row}\begin{bmatrix}\mathcal L\\\CA\\\C\end{bmatrix} =\mathcal V+\langle c^{\mathsf T}A\rangle. \\]

Thus

\\[ \boxed{ h=\dim\bigl(\mathcal V+\langle c^{\mathsf T}A\rangle\bigr) = \begin{cases} q+1,&c^{\mathsf T}A\in\mathcal V,\\\ q+2,&c^{\mathsf T}A\notin\mathcal V. \end{cases} } \tag{1.2} \\]

This part does not use \\((\ell,A)\\) observability.

### 1.3 The equivalence in B.26(3) is valid

Condition (5a) means that there exist matrices \\(\Lambda,G_0,G_1\\) such that

\\[ \mathcal LA=\Lambda\mathcal L+G_0c^{\mathsf T} +G_1c^{\mathsf T}A. \\]

Equivalently,

\\[ \operatorname{row}(\mathcal LA) \subseteq \operatorname{row}\mathcal L+ \langle c^{\mathsf T},c^{\mathsf T}A\rangle. \\]

Using (1.1), this is

\\[ \operatorname{row}(\mathcal LA) \subseteq \mathcal V+\langle c^{\mathsf T}A\rangle. \tag{1.3} \\]

Now suppose (5a) holds. Every \\(v\in\mathcal V\\) has a unique representation

\\[ v=u+\alpha c^{\mathsf T}, \qquad u\in\operatorname{row}\mathcal L. \\]

Then

\\[ vA=uA+\alpha c^{\mathsf T}A. \\]

By (1.3), \\(uA\in\mathcal V+\langle c^{\mathsf T}A\rangle\\), and clearly \\(\alpha c^{\mathsf T}A\\) belongs to the same space. Therefore

\\[ \mathcal VA\subseteq\mathcal V+\langle c^{\mathsf T}A\rangle. \\]

Conversely, if

\\[ \mathcal VA\subseteq\mathcal V+\langle c^{\mathsf T}A\rangle, \\]

then in particular

\\[ \operatorname{row}(\mathcal LA) \subseteq\mathcal VA \subseteq\mathcal V+\langle c^{\mathsf T}A\rangle. \\]

Using (1.1), this is precisely (1.3), hence (5a).

Consequently,

\\[ \boxed{ (5a)\iff \mathcal VA\subseteq\mathcal V+\langle c^{\mathsf T}A\rangle. } \tag{1.4} \\]

This proof should replace the brief sentence in B.26(3). It makes clear that the equivalence depends on the full-row-rank admissibility condition, not on observability of \\((\ell,A)\\).

### 1.4 The invariant-subspace case is correct

If

\\[ c^{\mathsf T}A\in\mathcal V, \\]

then (1.4) reduces to

\\[ \boxed{\mathcal VA\subseteq\mathcal V.} \tag{1.5} \\]

Conversely, if \\(\mathcal V\\) is \\(A\\)-invariant, then (1.4) automatically holds, regardless of whether \\(c^{\mathsf T}A\\) belongs to \\(\mathcal V\\). But in the second case under consideration, it does belong to \\(\mathcal V\\).

Thus B.26(4) is correct.

### 1.5 B.27: the two-case proof is complete

We can now verify the theorem without relying on any numerical evidence.

Suppose

\\[ 1\le q\le n-2. \\]

By (1.2), exactly one of two cases occurs.

Case I: \\(c^{\mathsf T}A\notin\mathcal V\\).

Then

\\[ h=q+2=q+r_1. \\]

The equality obstruction B.22 applies because \\(q\ge1\\). Therefore (5b) fails.

Case II: \\(c^{\mathsf T}A\in\mathcal V\\).

By (1.5), \\(\mathcal V\\) is \\(A\\)-invariant. Since \\(c^{\mathsf T}\in\mathcal V\\), induction gives

\\[ c^{\mathsf T}A^k\in\mathcal V \qquad\text{for all }k\ge0. \\]

Observability of \\((c,A)\\) means

\\[ \operatorname{span}\\{c^{\mathsf T},c^{\mathsf T}A,\ldots, c^{\mathsf T}A^{n-1}\\} =\mathbb C^{1\times n}. \\]

Hence

\\[ \mathbb C^{1\times n}\subseteq\mathcal V. \\]

It follows that

\\[ n\le\dim\mathcal V=q+1, \\]

contradicting \\(q\le n-2\\).

So Case II is impossible, and every admissible candidate falls into Case I. Hence (5b) fails.

We have therefore proved

\\[ \boxed{ p=r=1,\quad 1\le q\le n-2 \quad\Longrightarrow\quad \text{every admissible }\mathcal L\text{ fails (5b)}. } \tag{1.6} \\]

Together with the terminal-order construction at \\(q=n-1\\), this gives

\\[ \boxed{q\_{\min}=n-1.} \\]

Conclusion on Q1: the proof is complete, conditional only on the previously established B.22 and the terminal-order feasibility construction. No use of \\((\ell,A)\\) observability occurs in the argument. The only observability assumption needed for the exclusion is observability of \\((c,A)\\).

A small technical point for the paper: explicitly state \\(n\ge2\\), or otherwise explain the degenerate \\(n=1\\) case. The range \\(1\le q\le n-2\\) is empty when \\(n\le2\\), but the assertion \\(r_1=2\\) requires \\(n\ge2\\). For the nontrivial theorem this is harmless, but the assumptions should be internally consistent.

## 2. Q2: Does the mechanism generalize to arbitrary \\((p,r)\\)?

There is a genuine generalization of B.26, but the decisive two-case argument in B.27 does not carry over unchanged. The distinction is important: the subspace reduction generalizes cleanly, whereas the dimension dichotomy is special to the single-output case.

I will derive the general version first.

### 2.1 General form of the subspace reduction

Let

\\[ U:=\operatorname{row}\mathcal L,\qquad R:=\operatorname{row}C,\qquad W_0:=\operatorname{row}\begin{bmatrix}CA\\\C\end{bmatrix}. \\]

Assume, as in the original setup, that

\\[ \operatorname{rank}\begin{bmatrix}C\\\\\mathcal L\end{bmatrix}=p+q. \\]

Then

\\[ \mathcal V:=\mathcal Z^\perp =\operatorname{row}\begin{bmatrix}\mathcal L\\\C\end{bmatrix} =U\oplus R, \qquad \dim\mathcal V=q+p. \tag{2.1} \\]

Here, over a complex state space, \\(\mathcal Z^\perp\\) should be interpreted as the algebraic annihilator of \\(\mathcal Z\\) under the row-column pairing. If the original problem is over \\(\mathbb R\\), the usual Euclidean orthogonal complement gives the same result.

Now (5a) is equivalent to

\\[ UA\subseteq U+W_0. \\]

Since \\(R\subseteq\mathcal V\\), and

\\[ RA\subseteq\operatorname{row}(CA)\subseteq W_0, \\]

we obtain the following equivalence:

\\[ \boxed{ (5a) \iff \mathcal VA\subseteq\mathcal V+W_0 \iff \mathcal VA\subseteq\mathcal V+\operatorname{row}(CA). } \tag{2.2} \\]

To see the reverse implication explicitly, suppose

\\[ \mathcal VA\subseteq\mathcal V+W_0. \\]

Then \\(UA\subseteq\mathcal VA\subseteq\mathcal V+W_0=U+R+W_0=U+W_0\\), which is exactly (5a).

This is the general analogue of B.26(3). It is worth recording as a lemma in its own right:

> General subspace characterization. For every admissible \\(\mathcal L\\), condition (5a) depends only on \\(\mathcal V=\mathcal Z^\perp\\), and is equivalent to\
> \\[\
> \mathcal VA\subseteq\mathcal V+\operatorname(CA).\
> \\]

Thus the reduction from \\(\mathcal L\\) to \\(\mathcal Z\\) is not peculiar to Class I. It is a general structural fact.

### 2.2 The generalized dimension formula

Since

\\[ h=\operatorname{rank}\begin{bmatrix}\mathcal L\\\CA\\\C\end{bmatrix}, \\]

we have

\\[ \boxed{ h=\dim(\mathcal V+W_0) =q+p+r_1-\dim(\mathcal V\cap W_0). } \tag{2.3} \\]

Because \\(R\subseteq\mathcal V\cap W_0\\), and \\(\dim R=p\\),

\\[ q+p\le h\le q+r_1. \tag{2.4} \\]

This recovers the general counting bound.

In Class I, \\(p=1\\) and \\(r_1=2\\). The intersection \\(\mathcal V\cap W_0\\) has dimension at least one and at most two. There are only two possibilities:

\\[ \dim(\mathcal V\cap W_0)=1 \quad\text{or}\quad \dim(\mathcal V\cap W_0)=2. \\]

These give, respectively,

\\[ h=q+2 \quad\text{or}\quad h=q+1. \\]

In the first case, B.22 applies. In the second, \\(W_0\subseteq\mathcal V\\), so \\(\operatorname{row}(CA)\subseteq\mathcal V\\), and (2.2) reduces to \\(A\\)-invariance.

This explains exactly why the Class I proof is so short: the intersection dimension has only two possible values, and the lower one is precisely the equality boundary.

### 2.3 What happens for general \\(p,r\\)?

For general dimensions, write

\\[ t:=\dim\bigl(\operatorname{row}(CA)\bigr) -\dim\bigl(\operatorname{row}(CA)\cap\mathcal V\bigr). \\]

Then

\\[ h=q+p+t,\qquad 0\le t\le r_1-p. \tag{2.5} \\]

There can be many intermediate values of \\(t\\).

The two extreme cases have useful interpretations:

- \\(t=0\\): \\(\operatorname{row}(CA)\subseteq\mathcal V\\), so (2.2) gives \\(\mathcal VA\subseteq\mathcal V\\). Thus \\(\mathcal V\\) is \\(A\\)-invariant.
- \\(t=r_1-p\\): \\(\mathcal V\cap W_0=R\\), so \\(h=q+r_1\\), and B.22 gives failure.

But when

\\[ 0\<t\<r_1-p, \\]

neither conclusion follows. The subspace \\(\mathcal V\\) need not be invariant, and the equality theorem need not apply.

This is the precise obstruction to a direct generalization of B.27.

### 2.4 The invariant-subspace argument still gives a useful exclusion theorem

Suppose

\\[ \operatorname{row}(CA)\subseteq\mathcal V. \\]

Then \\(\mathcal VA\subseteq\mathcal V\\). Since \\(R=\operatorname{row}C\subseteq\mathcal V\\), induction yields

\\[ \operatorname{row}(CA^k)\subseteq\mathcal V \qquad(k\ge0). \\]

If \\((C,A)\\) is observable, the observability matrix has full column rank, equivalently

\\[ \operatorname{span}\\{\operatorname{row}(CA^k):k\ge0\\} =\mathbb C^{1\times n}. \\]

Therefore

\\[ \mathcal V=\mathbb C^{1\times n}, \\]

which forces

\\[ q+p\ge n. \\]

Consequently,

\\[ \boxed{ q+p\<n \quad\Longrightarrow\quad \operatorname{row}(CA)\not\subseteq\mathcal V } \tag{2.6} \\]

for every admissible candidate satisfying (5a).

This is a genuine general theorem. It says that below the terminal dimension, the \\(CA\\)-row space must contribute at least one new direction outside \\(\mathcal V\\).

However, one new direction is not enough to force \\(h=q+r_1\\) when \\(r_1-p>1\\). The missing step is to show that the remaining directions must also be outside \\(\mathcal V\\), or to find another mechanism that forces a spectral rank drop at intermediate values of \\(t\\).

### 2.5 A possible generalization through quotient dynamics

The inclusion

\\[ \mathcal VA\subseteq\mathcal V+\operatorname{row}(CA) \\]

suggests studying the induced map on the quotient

\\[ \mathbb C^{1\times n}/\mathcal V. \\]

Let \\(\pi\_{\mathcal V}\\) denote the quotient map. Then (5a) implies

\\[ \pi\_{\mathcal V}(\mathcal VA) \subseteq \pi\_{\mathcal V}(\operatorname{row}(CA)). \tag{2.7} \\]

In particular, the image of \\(\mathcal V\\) under right multiplication by \\(A\\), modulo \\(\mathcal V\\), is controlled by the \\(CA\\)-directions.

This is a useful reformulation, but I would be cautious about calling it an induced action of \\(A\\) on the quotient: unless \\(\mathcal V\\) is \\(A\\)-invariant, right multiplication by \\(A\\) does not define an endomorphism of the quotient. What is well-defined here is the restricted quotient map

\\[ \mathcal V\longrightarrow \mathbb C^{1\times n}/\mathcal V,\qquad v\longmapsto vA+\mathcal V. \\]

Condition (5a) constrains its image to a subspace of dimension at most \\(r_1-p\\).

That may be a useful starting point for a rank or incidence argument. In Class I, the quotient image is at most one-dimensional. In general, its dimension can be larger, and the spectral problem must account for the geometry of this image.

My conclusion on Q2: the reduction to \\(\mathcal V\\) generalizes completely, and the invariant-subspace exclusion generalizes as well. What does not generalize automatically is the two-case collapse. For general \\((p,r)\\), the intermediate intersection strata are the central difficulty.

## 3. Q3: Is Class I structurally the worst case?

The theorem establishes that Class I has

\\[ q\_{\min}=n-1. \\]

This is an exceptionally strong lower bound: only one augmentation row can be omitted from the maximum possible \\(n-1\\) independent rows, under the stated assumptions.

But I would distinguish three claims:

1. Class I has a maximal-looking minimum order.
2. Small \\(p,r\\) generally produce larger gaps.
3. Class I is the worst case among all admissible parameter classes.

The first is proved. The second and third are not established by the current examples.

### 3.1 Why Class I has such a large minimum order

There are two structural features.

First: the observation row \\(C\\) is one-dimensional.

The space

\\[ \mathcal V=\operatorname{row}\begin{bmatrix}\mathcal L\\\C\end{bmatrix} \\]

has dimension exactly \\(q+1\\). Adding \\(CA\\) can increase its dimension by at most one. Therefore the possible values of \\(h\\) are only

\\[ q+1,\qquad q+2. \\]

Second: observability forces every \\(A\\)-invariant row space containing \\(C\\) to be the entire state row space.

Thus the lower-rank case \\(h=q+1\\) is impossible below terminal order, while the other case is exactly the equality obstruction.

The combination is unusually rigid. There is no intermediate rank stratum in which a candidate might evade both arguments.

This is the real structural reason for the Class I result.

### 3.2 Why small \\(p,r\\) do not automatically imply a larger gap

The dimension \\(p\\) controls the size of the initial row space \\(R=\operatorname{row}C\\), while \\(r\\) controls the dimension of the target row space. But the gap also depends on:

- the relative position of \\(\operatorname{row}(CA)\\) and \\(\mathcal V\\);
- the dimension \\(r_1=\operatorname{rank}[CA;C]\\);
- the geometry of the admissible subspaces inside \\(K=\ker[C;L_0]\\);
- the spectral behavior of the induced quotient pencil;
- the way the target row space constrains the admissible augmentation.

There is no immediate monotonicity in \\(p\\) or \\(r\\). Increasing \\(p\\) may increase the dimension of \\(\mathcal V\\), making it easier to contain more of the \\(CA\\)-row space. But it may also change the admissible parameter space and the spectral constraints in ways that make feasibility harder.

Likewise, increasing \\(r\\) imposes more target directions, which can reduce the freedom to choose \\(\mathcal Z\\), but it does not by itself imply a larger or smaller minimum augmentation order.

### 3.3 A more defensible conjectural direction

Instead of conjecturing immediately that small \\((p,r)\\) force maximal gaps, I suggest formulating a structural parameter that measures the rigidity of the row-space extension.

For example, define

\\[ \delta(\mathcal V) := \dim\bigl(\operatorname{row}(CA)/ (\operatorname{row}(CA)\cap\mathcal V)\bigr). \\]

Then

\\[ h=q+p+\delta(\mathcal V). \\]

The equality obstruction occurs when

\\[ \delta(\mathcal V)=r_1-p. \\]

The invariant-space argument rules out

\\[ \delta(\mathcal V)=0 \\]

when \\(q+p\<n\\).

The unresolved cases are therefore

\\[ 1\le\delta(\mathcal V)\<r_1-p. \\]

This parameter isolates exactly how much of the \\(CA\\)-row space lies outside \\(\mathcal V\\). It is likely to be more useful than \\(p\\) or \\(r\\) alone in understanding the gap.

A natural research question is:

> Under what structural assumptions on \\((C,A,L_0)\\) can an admissible \\(\mathcal V\\) have an intermediate value of \\(\delta(\mathcal V)\\) and still satisfy (5b)?

This question is specific, testable, and directly connected to the quotient-pencil framework.

### 3.4 What can be said about the gap at present?

Let \\(q_0\\) denote the lower bound from the dimension/counting framework. In Class I, the theorem gives

\\[ q\_{\min}-q_0=n-1-q_0. \\]

The reports mention examples with gaps one and two for \\(n=6,p=r=2\\). These examples show that the Class I gap can be much larger than gaps observed in other parameter settings.

They do not establish a universal comparison. To claim Class I is worst, one would need either:

- a general upper bound on \\(q\_{\min}\\) for all other parameter classes that is strictly smaller than \\(n-1\\); or
- a structural theorem showing that the single-output/single-target case maximizes the minimum-order obstruction.

Neither follows from B.27 alone.

Recommendation: describe Class I as a particularly rigid extreme case, and state the observed comparison with the other examples as evidence. Do not yet claim it is universally the worst case.

## 4. Q4: How should the paper be organized?

I agree with the proposed theorem hierarchy, but I would make one adjustment: put the subspace reduction before the counting/spectral dichotomy, rather than introducing B.22 first and then returning to the geometric structure.

The new Class I proof shows that the subspace viewpoint is not just a convenient alternative representation. It is the mechanism that makes the classification possible. It should therefore appear early enough to inform the reader's understanding of the later spectral results.

I suggest the following structure.

### Part I. Problem formulation and geometric reduction

Section 1. Problem formulation and admissible augmentations

- Define the minimum-order augmentation problem.
- State (5a), (5b), the admissibility conditions, and the target inclusion.
- Define\
  \\[\
  \mathcal Z=\ker\begin{bmatrix}C\\\mathcal L\end{bmatrix},\
  \qquad\
  \mathcal V=\mathcal Z^\perp.\
  \\]
- Explain the correspondence between admissible augmentations and admissible subspaces \\(\mathcal Z\\).

Section 2. The subspace characterization of (5a)

State the general identity

\\[ \mathcal V =\operatorname{row}\begin{bmatrix}\mathcal L\\\C\end{bmatrix}, \qquad \dim\mathcal V=q+p, \\]

and prove

\\[ \boxed{ (5a)\iff \mathcal VA\subseteq\mathcal V+\operatorname{row}(CA). } \tag{4.1} \\]

This is the general version of B.26(3). It makes clear that the algebraic condition (5a) is determined by \\(\mathcal Z\\), not by the particular choice of basis for the complementary augmentation rows.

Also introduce

\\[ h=\dim\left(\mathcal V+ \operatorname{row}\begin{bmatrix}CA\\\C\end{bmatrix}\right). \\]

### Part II. The counting and spectral framework

Section 3. Rank bounds and the counting obstruction

Establish

\\[ q+p\le h\le q+r_1. \\]

Then explain why

\\[ h\<q+r_1 \\]

is necessary for (5b).

Section 4. Quotient-pencil and spectral characterizations

Introduce the quotient-pencil formulation and the intrinsic partial operator

\\[ \Phi:\mathcal LV\to\mathbb C^q, \qquad \Phi(\mathcal Lx)=\mathcal LAx,\quad x\in V. \\]

State the equivalence

\\[ (5b)\text{ fails} \iff \exists\\,0\ne u\in\mathcal LV: \Phi(u)\in\operatorname{span}\\{u\\}. \\]

This is the most informative interpretation of the spectral condition. It makes the dependence on the admissible subspace explicit and avoids treating an arbitrary extension \\(K_1\\) as intrinsic.

Section 5. The equality obstruction

State B.22:

\\[ \boxed{ h=q+r_1,\ q\ge1 \quad\Longrightarrow\quad (5b)\text{ fails}. } \\]

Give the square-factorization proof, including the stronger conclusion

\\[ d\_{\rm fin}=q,\qquad d\_\infty=r_1. \\]

This theorem should be highlighted as the decisive spectral obstruction.

### Part III. Classification and examples

Section 6. Class I: complete minimum-order classification

State B.27:

\\[ p=r=1 \quad\Longrightarrow\quad q\_{\min}=n-1. \\]

Present the two cases in the order used in the proof:

1. \\(c^{\mathsf T}A\notin\mathcal V\\): equality obstruction.
2. \\(c^{\mathsf T}A\in\mathcal V\\): invariance and observability contradiction.

This is a particularly elegant application of the general framework, and it deserves a prominent position rather than being buried in an appendix.

Section 7. Higher-dimensional examples and unresolved cases

Present the \\(n=6,p=r=2\\) examples and the larger-gap constructions. Separate:

- exact theorems;
- exact finite-instance verification;
- numerical evidence;
- conjectures.

Do not mix these evidentiary levels in the same theorem statement.

### Part IV. Complexity and future directions

Section 8. Complexity and algorithmic questions

Present the quotient-pencil and incidence formulations as the basis for the complexity problem. Keep the general complexity question explicitly open unless a rigorous reduction is obtained.

Appendices

- Kronecker canonical form bookkeeping and the corrected B.8b.
- Detailed equality-theorem calculations.
- Lean formalization definitions and verification status.
- Exact computational protocols and reproducibility information.

### One important editorial distinction

I would not describe the general counting/spectral framework as a complete characterization of feasibility. It gives:

- a necessary counting inequality;
- an exact spectral condition;
- a complete obstruction at equality.

But for \\(h\<q+r_1\\), feasibility still depends on the spectral condition. The paper should say this explicitly to avoid suggesting that the counting inequality alone solves the problem.

## 5. Q5: Which research target should come next?

I recommend a two-stage strategy:

1. First study \\(p=1,r=2\\).
2. Then study \\(p=2,r=1\\).
3. After those two cases, decide whether to formulate a general complexity theorem or continue with a structural classification.

I would not immediately jump to the general complexity question.

### 5.1 Why \\(p=1,r=2\\) is the natural next case

This case retains the most valuable feature of Class I: \\(C\\) is still a single row.

Consequently, under observability of \\((c,A)\\), one can still use a cyclic basis:

\\[ c^{\mathsf T},\ c^{\mathsf T}A,\ \ldots,\ c^{\mathsf T}A^{n-1}. \\]

The main difference is that the target space has dimension two rather than one.

This makes it a controlled extension of the Class I theorem. It isolates the effect of increasing the target dimension while retaining the scalar-output structure.

The general subspace reduction becomes

\\[ \dim\mathcal V=q+1, \\]

and

\\[ h=q+1+\delta, \\]

where

\\[ \delta= \dim\left( \operatorname{row}(CA)/ (\operatorname{row}(CA)\cap\mathcal V) \right). \\]

Since \\(r_1\\) may now be as large as three,

\\[ 0\le\delta\le r_1-1. \\]

The cases are:

- \\(\delta=0\\): \\(\mathcal V\\) is \\(A\\)-invariant, so observability rules it out below terminal order.
- \\(\delta=r_1-1\\): equality \\(h=q+r_1\\), so B.22 rules it out by spectral failure.
- Intermediate values: these are the genuinely new cases.

For \\(r_1=3\\), there is only one intermediate value:

\\[ \delta=1. \\]

This is an excellent next target. It is the smallest setting in which the clean Class I dichotomy breaks down.

The central question becomes:

> Can an admissible \\(\mathcal V\\) with \\(\delta=1\\) satisfy the spectral condition (5b)?

That is a sharply defined mathematical problem.

### 5.2 Why \\(p=2,r=1\\) should come second

This case retains a one-dimensional target space but has a two-dimensional observation space.

It may preserve some of the target-side simplifications, but the observation pair \\((C,A)\\) is no longer necessarily cyclic in the scalar-output sense. The natural canonical structure is a multi-input/multi-output observability structure, with several Krylov chains rather than one.

Thus it is a useful complementary case, but it changes a different part of the geometry.

Comparing the two cases should help separate the roles of \\(p\\) and \\(r\\):

| Case          | Feature retained                 | Main new difficulty                 |
| ------------- | -------------------------------- | ----------------------------------- |
| \\(p=1,r=2\\) | Single-output cyclic coordinates | Larger target row space             |
| \\(p=2,r=1\\) | Single target row                | Multi-output observability geometry |

I would study them separately rather than trying to handle arbitrary \\(p,r\\) immediately.

### 5.3 Why not attack complexity first?

The quotient-pencil formulation is a strong candidate for a complexity investigation, but there are two reasons to defer a definitive complexity claim.

First, the admissible subspace is not arbitrary. It must arise from a subspace \\(\mathcal Z\le K\\) satisfying the target constraints and the linear invariance-type condition (5a). A hardness reduction must preserve all of these constraints.

Second, a general complexity result may obscure the structural mathematics that has just become clearer. The \\(p=1,r=2\\) case is likely to reveal whether the Class I mechanism is a special one-dimensional phenomenon or the first instance of a broader theorem.

That distinction matters before choosing a complexity framework.

I would nevertheless begin recording the algorithmic formulation now. For a fixed admissible \\(\mathcal Z\\), the spectral test can be carried out through the polynomial minors of the induced pencil. The harder part is the existential search over the admissible Grassmannian.

This naturally separates the problem into:

- verification: given \\(\mathcal Z\\), decide whether (5b) holds;
- synthesis: determine whether there exists an admissible \\(\mathcal Z\\) for which (5b) holds.

The second is the genuine global search problem. It is a better starting point for complexity analysis than simply referring to matrix-pencil completion.

## 6. Additional technical and presentation points

There are several details I would settle before treating B.27 as camera-ready.

### 6.1 Be precise about the observability assumptions

The proof of B.27 uses only observability of \\((C,A)\\), in the Class I case \\((c,A)\\). It does not use observability of \\((L_0,A)\\).

This is worth stating explicitly in a remark:

> The exclusion of all orders \\(q\le n-2\\) uses only observability of \\((c,A)\\), together with admissibility and (5a). Observability of \\((L_0,A)\\), if included in the global problem assumptions, is not needed for this particular lower-bound argument.

This identifies a potentially stronger theorem. It may be useful later when considering variants in which the target pair is not observable.

### 6.2 Separate the lower-bound theorem from terminal feasibility

The proof that no \\(q\le n-2\\) works is independent of the construction at \\(q=n-1\\).

For logical clarity, state two results:

- Lower-bound theorem: every admissible candidate with \\(1\le q\le n-2\\) fails.
- Terminal feasibility theorem: there exists an admissible candidate with \\(q=n-1\\) satisfying both conditions.

Then combine them into the minimum-order corollary.

This prevents the reader from confusing the assumptions needed for the lower bound with those needed for the upper-bound construction.

### 6.3 The exact verification is corroboration, not part of the proof

The 2,954/2,954 and 2,454/2,454 checks are useful, particularly for testing the implementation of the subspace characterization and the case split. But the theorem is established by the paper proof.

I would report the computational evidence in a separate paragraph or appendix and explain:

- the parameter ranges tested;
- how admissibility was checked;
- how charts were enumerated;
- whether all chart denominators and exceptional specializations were treated;
- whether the arithmetic was exact or floating-point.

In particular, “all charts” should be backed by a precise description of the chart cover and its treatment of chart boundaries. Since the proof is now analytic, the computational section need not carry the burden of proving completeness.

### 6.4 The Lean status is appropriately qualified

The report correctly distinguishes the formalized Krylov-space argument from the paper-only row-space reduction.

The full B.27 theorem should therefore be labelled `[Lean-conditional]`, not `[Lean-verified]`, unless the missing instantiation and equivalence steps are subsequently formalized.

This is a good example of rigorous reporting of formalization status. I would preserve the distinction.

## 7. A polished statement of the Class I theorem

For the paper, I suggest the following formulation.

> Theorem (Class I minimum-order classification).\
> Let \\(A\in\mathbb C^{n\times n}\\), let \\(C=c^{\mathsf T}\in\mathbb C^{1\times n}\\), and let \\(L_0=\ell^{\mathsf T}\\) be the prescribed target row. Assume \\((c^{\mathsf T},A)\\) is observable. Let \\(\mathcal L\in\mathbb C^{q\times n}\\) be admissible, so that\
> \\[\
> \operatorname(L_0)\subseteq\operatorname(\mathcal L),\
> \qquad\
> \operatorname\beginC\\\mathcal L\end=q+1,\
> \\]\
> and suppose \\(\mathcal L\\) satisfies (5a). Then, for every \\(1\le q\le n-2\\), condition (5b) fails.
>
> If, in addition, the terminal-order construction at \\(q=n-1\\) is admissible and satisfies (5a)–(5b), then\
> \\[\
> \boxed