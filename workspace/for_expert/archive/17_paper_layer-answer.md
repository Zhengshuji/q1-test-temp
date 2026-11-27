# Referee report on `17_paper_layer.md`

## Overall assessment

The paper layer is substantially more mature than a collection of exploratory arguments. In particular, the quotient-pencil criterion, the PBH reduction, the permanent-kernel argument, and the Class I canonical-coordinate calculation form a coherent mathematical framework. The distinction between a fully formalized theorem and a formalized inference under mathematical hypotheses is also a good methodological decision.

However, I would not yet regard the paper layer as ready for incorporation into a final paper. There are several points that need correction or additional hypotheses:

1. B.11d: the proof does not establish the claimed strict inequality at the boundary \\(h=q+r_1\\). The boundary cannot be dismissed by the rank estimate alone.
2. B.8: the Kronecker-index identity is not valid for arbitrary rectangular pencils in the form stated. The conventions for left and right minimal indices, and the contribution of infinite elementary divisors, must be made explicit.
3. B.13f: the statement that the pencil determinant vanishes identically is incorrect under the natural quotient-pencil interpretation.
4. B.9: the distinction between the number of left minimal indices and the number of nonzero left minimal indices needs to be stated carefully.
5. B.18e(ii): the conclusion is correct, but the proof should explicitly explain why the rank becomes \\(n\\), and why that gives (5a).

On the positive side, I find the elementwise proof of B.13d sound, and I find the canonical-coordinate argument in B.18e quite promising. The latter gives a genuine structural result, not merely an experimental observation.

I will go through the five questions first, then audit the remaining propositions.

# Part I. Answers to the five questions

## Q1(a). The boundary case \\(h=q+r_1\\) in B.11d

Proof gap

The argument in B.11d is correct for \\(h>q+r_1\\), but it does not establish the claimed equivalence when \\(h=q+r_1\\).

Let

\\[ m=q+r_1. \\]

Since \\(Q\_{\mathcal L}(\lambda)\\) has \\(m\\) rows,

\\[ \operatorname{rank}Q\_{\mathcal L}(\lambda)\le m. \\]

Condition (5b), however, asks for

\\[ \operatorname{rank}Q\_{\mathcal L}(\lambda)=h \qquad\text{for every }\lambda. \\]

There are three cases:

- If \\(h>m\\), condition (5b) is impossible.
- If \\(h=m\\), condition (5b) is possible in principle: it asks that \\(Q\_{\mathcal L}(\lambda)\\) have full row rank for every finite \\(\lambda\\).
- If \\(h\<m\\), condition (5b) asks that the pencil have constant rank \\(h\\), which is a different situation.

Consequently, the argument

\\[ h\ge q+r_1 \quad\Longrightarrow\quad \text{(5b) impossible} \\]

is not valid. What has actually been proved is

\\[ \boxed{h>q+r_1\quad\Longrightarrow\quad\text{(5b) impossible}.} \\]

The equality case needs a separate argument.

### What would repair B.11d?

There are two reasonable formulations.

Option 1: strengthen the CSS hypothesis.

Define a stronger property:

\\[ \text{for every admissible }\mathcal L,\quad h=q+r_1\Longrightarrow \text{(5b) fails}, \\]

and retain the existing CSS condition for \\(h\<q+r_1\\).

Then the desired reduction follows.

Option 2: prove a structural equality-exclusion lemma.

Prove, under the actual observer hypotheses, that

\\[ h=q+r_1 \quad\Longrightarrow\quad \exists\lambda\in\mathbb C: \operatorname{rank}Q\_{\mathcal L}(\lambda)\<h. \\]

This would settle the boundary without changing the definition of CSS.

I would prefer Option 2 if it is true. It would be a stronger and more useful theorem.

There is one potentially important route: use the PBH formulation in B.12. At equality, \\(Q\_{\mathcal L}\\) has as many rows as its normal rank. The question becomes whether the special structure of the observer representation forces the subspace

\\[ U=\mathcal LV \\]

to contain an eigenvector of \\(\Lambda\\). If it does, B.12 gives the required rank drop.

But this is a new mathematical assertion. It does not follow merely from the number of rows.

### A useful distinction

The equality case is not a technical nuisance in the proof. It is a genuinely different geometric regime:

\\[ h=q+r_1 \quad\Longleftrightarrow\quad k=q+r_1-h=0. \\]

In particular, it is the regime in which there are no left minimal indices if the standard row-pencil convention is being used and the zero-index issue has been excluded.

I would therefore keep equality as a separate case throughout the paper until it has been settled.

Verdict: B.11d is not proved as currently written. The strict inequality in the conclusion must either be justified by an additional theorem or replaced by a non-strict formulation with a separate equality analysis.&#x20;

17_paper_layer.md



## Q1(b). The canonical-coordinate argument in B.18e(ii)

Conclusion correct; proof should be completed

I agree with the conclusion. There is no hidden assumption that

\\[ \ell\in\operatorname{span}\\{c,cA\\}. \\]

In fact, the argument works precisely because \\(z\in K\\) and \\(z\notin V\\).

Recall

\\[ K=\ker\begin{bmatrix}c\\\\\ell\end{bmatrix}, \qquad V=\ker\begin{bmatrix}c\\\cA\end{bmatrix}. \\]

Take

\\[ 0\ne z\in K\setminus V. \\]

Then

\\[ cz=0,\qquad \ell z=0, \\]

but

\\[ cAz\ne0. \\]

In the canonical coordinates,

\\[ c=e_1^{\mathsf T},\qquad cA=e_2^{\mathsf T}. \\]

Thus

\\[ z_1=0,\qquad z_2\ne0. \\]

Now construct a candidate \\(\mathcal L\\) with

\\[ \ker\begin{bmatrix}c\\\\\mathcal L\end{bmatrix} =\langle z\rangle, \qquad \ell\in\operatorname{row}\mathcal L. \\]

This is possible because

\\[ \langle c,\ell\rangle\subseteq z^\perp \\]

and

\\[ \dim z^\perp=n-1. \\]

We can choose an \\((n-1)\\)-dimensional row space \\(z^\perp\\) containing \\(c\\) and \\(\ell\\), then choose the remaining \\(n-2\\) rows as \\(\mathcal L\\).

Now consider

\\[ H=\begin{bmatrix}\mathcal L\\\cA\\\c\end{bmatrix}. \\]

Since

\\[ \operatorname{row}\begin{bmatrix}c\\\\\mathcal L\end{bmatrix} =z^\perp, \\]

we have

\\[ \operatorname{rank}H=n \\]

if and only if

\\[ cA\notin z^\perp. \\]

But

\\[ cA\notin z^\perp \iff cAz\ne0, \\]

which is true.

Therefore

\\[ \boxed{\operatorname{rank}H=n.} \\]

This is the point that should be stated explicitly in the report.

Once \\(\operatorname{rank}H=n\\), the row space of \\(H\\) is all of \\(\mathbb C^{1\times n}\\). In particular,

\\[ \operatorname{row}(\mathcal LA) \subseteq \operatorname{row}H. \\]

Thus the representation

\\[ \mathcal LA=\Lambda\mathcal L+G_0c+G_1cA \\]

exists, and (5a) holds.

Notice that this proof does not use any special relation between \\(\ell\\) and \\(cA\\). It uses only

\\[ z\in\ker c\cap\ker\ell, \qquad cAz\ne0. \\]

Verdict: B.18e(ii) is correct. I recommend replacing its current compressed explanation with the above three-step argument: construct the row space, prove \\(h=n\\), conclude (5a).

## Q2. B.13d: the elementwise argument

Theorem correct

I checked both degenerate cases. The argument is sound, although I would rewrite the rank-\\(\ge2\\) part to make the scalar consistency argument completely transparent.

Let

\\[ U_0,U_1:V\longrightarrow W \\]

be linear maps, and suppose

\\[ P=\\{x\in V:U_0x\wedge U_1x=0\\}=V. \\]

Equivalently,

\\[ U_0x,\ U_1x \quad\text{are linearly dependent for every }x\in V. \\]

We want to establish the stated classification.

### Case 1: \\(\operatorname{rank}U_0=0\\)

Then \\(U_0=0\\). Hence

\\[ U_0x\wedge U_1x=0 \\]

for every \\(x\\), automatically.

This case is correct.

### Case 2: \\(\operatorname{rank}U_0=1\\)

Let

\\[ \operatorname{im}U_0=\langle u\rangle. \\]

For every \\(x\\) with \\(U_0x\ne0\\), dependence gives

\\[ U_1x\in\langle u\rangle. \\]

Choose \\(x_0\\) such that \\(U_0x_0\ne0\\). For any

\\[ k\in\ker U_0, \\]

we have

\\[ U_0(x_0+k)=U_0x_0\ne0. \\]

Therefore

\\[ U_1x_0\in\operatorname{im}U_0, \qquad U_1(x_0+k)\in\operatorname{im}U_0. \\]

Subtracting,

\\[ U_1k =U_1(x_0+k)-U_1x_0 \in\operatorname{im}U_0. \\]

Thus \\(U_1\\) maps every vector into \\(\operatorname{im}U_0\\):

\\[ \boxed{\operatorname{im}U_1\subseteq\operatorname{im}U_0.} \\]

The rank-one case is fully correct.

### Case 3: \\(\operatorname{rank}U_0\ge2\\)

For every \\(x\\) satisfying \\(U_0x\ne0\\), write

\\[ U_1x=\alpha_xU_0x. \\]

Choose \\(x,y\\) such that \\(U_0x\\) and \\(U_0y\\) are linearly independent.

By linearity,

\\[ U_1(x+y) =\alpha_xU_0x+\alpha_yU_0y. \\]

On the other hand, dependence applied to \\(x+y\\) gives

\\[ U_1(x+y)=\alpha\_{x+y}(U_0x+U_0y). \\]

Independence of \\(U_0x,U_0y\\) yields

\\[ \alpha_x=\alpha_y=\alpha\_{x+y}. \\]

Now take an arbitrary \\(z\\) with \\(U_0z\ne0\\).

- If \\(U_0z\\) is independent of \\(U_0x\\), compare \\(z\\) with \\(x\\).
- If \\(U_0z\\) is proportional to \\(U_0x\\), compare \\(z\\) with \\(y\\), since \\(U_0y\\) is independent of \\(U_0x\\).

In either case,

\\[ \alpha_z=\alpha_x. \\]

Hence there is a single scalar \\(\alpha\\) such that

\\[ U_1z=\alpha U_0z \qquad \text{whenever }U_0z\ne0. \\]

It remains to consider \\(k\in\ker U_0\\). We have

\\[ U_1(x+k)-U_1x=U_1k. \\]

Both \\(x\\) and \\(x+k\\) have the same nonzero \\(U_0\\)-image, so

\\[ U_1(x+k)=\alpha U_0(x+k)=\alpha U_0x \\]

and

\\[ U_1x=\alpha U_0x. \\]

Consequently,

\\[ U_1k=0. \\]

Thus

\\[ \boxed{U_1=\alpha U_0.} \\]

The third-vector device is valid. In fact, the independent-image argument above is a slightly cleaner presentation.

### Conclusion

B.13d is correct as stated, assuming the underlying field is \\(\mathbb C\\) and \\(P\\) is indeed the algebraic proportionality locus.

The irreducibility argument also works:

\\[ \varepsilon=0 \iff \dim P=\dim V \iff P=V, \\]

because a proper algebraic subset of an irreducible affine space has strictly smaller dimension.

I would retain B.13d. It is one of the stronger paper-level results in the report.

## Q3. The Kronecker chain: is the identity in B.8 correct?

Requires substantial correction

This is the most important issue in the paper layer.

The statement

\\[ \boxed{h=\sum_j\varepsilon_j+d\_{\rm fin}} \\]

is not a general identity for arbitrary polynomial pencils, especially not for rectangular pencils, unless the \\(\varepsilon_j\\), the regular part, and the absence of other Kronecker blocks have been specified very carefully.

### 1. The general Kronecker decomposition

Let \\(P(\lambda)\\) be an \\(m\times n\\) pencil of normal rank \\(h\\).

Under strict equivalence, its Kronecker canonical form contains:

1. left singular blocks, with left minimal indices;
2. right singular blocks, with right minimal indices;
3. a regular part, containing finite and infinite elementary divisors.

With the standard convention, write:

- \\(\epsilon_i\\): left minimal indices;
- \\(\eta_j\\): right minimal indices;
- \\(d\_{\rm fin}\\): total size of the finite elementary divisors;
- \\(d\_\infty\\): total size of the infinite elementary divisors.

Then the normal-rank dimension identity is

\\[ \boxed{ h = \sum_i\epsilon_i + \sum_j\eta_j + d\_{\rm fin} + d\_\infty. } \\]

The exact block dimensions also give

\\[ m = \sum_i\epsilon_i + \sum_j(\eta_j+1) + d\_{\rm fin}+d\_\infty, \\]

and

\\[ n = \sum_i(\epsilon_i+1) + \sum_j\eta_j + d\_{\rm fin}+d\_\infty. \\]

These formulas are the safe general identities to use.

In particular, the formula in B.8 omits contributions unless additional hypotheses eliminate them.

### 2. A simple rectangular-pencil example

Consider

\\[ P(\lambda)=\begin{bmatrix}\lambda&1\end{bmatrix}. \\]

Its normal rank is

\\[ h=1. \\]

It has no left minimal indices, since it has only one row and no nontrivial polynomial row relation.

It has one right minimal index equal to \\(1\\), represented by the polynomial null vector

\\[ \begin{bmatrix}-1\\\\\lambda\end{bmatrix}. \\]

There are no finite elementary divisors.

Thus

\\[ h=1=\sum_j\eta_j, \\]

whereas the sum of the left minimal indices plus \\(d\_{\rm fin}\\) is zero.

This demonstrates that the formula in B.8 cannot be used as a general rectangular-pencil identity with \\(\varepsilon_j\\) interpreted as standard left minimal indices.

### 3. Infinite elementary divisors matter too

Consider the \\(1\times1\\) constant pencil

\\[ P(\lambda)=[1]. \\]

It has normal rank one and no finite elementary divisor. Its regular part is an infinite elementary divisor of size one.

Thus

\\[ h=1,\qquad d\_{\rm fin}=0,\qquad d\_\infty=1. \\]

So even in the square regular case, \\(h=d\_{\rm fin}\\) is not generally true unless infinite elementary divisors are excluded.

### 4. What is true about the first equivalence in B.8?

The statement

\\[ (5b)\iff d\_{\rm fin}=0 \\]

is correct, provided \\(d\_{\rm fin}\\) means the total degree of the finite invariant factors of the polynomial matrix \\(Q\_{\mathcal L}(\lambda)\\).

Indeed, let its Smith form have nonzero invariant factors

\\[ d_1(\lambda),\ldots,d_h(\lambda). \\]

At a finite \\(\lambda_0\\), the rank drops below \\(h\\) exactly when at least one nonzero invariant factor vanishes at \\(\lambda_0\\).

Over \\(\mathbb C\\), a nonconstant polynomial has a root. Therefore

\\[ \operatorname{rank}Q\_{\mathcal L}(\lambda)=h \quad\forall\lambda\in\mathbb C \\]

if and only if every nonzero invariant factor is a nonzero constant. Equivalently,

\\[ d\_{\rm fin}=0. \\]

This part is sound.

The problem is the subsequent identification

\\[ d\_{\rm fin}=0 \iff \sum_j\varepsilon_j=\operatorname{rank}\mathcal L. \\]

That identification requires an additional structural identity. It does not follow from the general Smith form alone.

### 5. The terminology in B.8 and B.9 needs to be reconciled

There is also a convention issue.

B.8 describes \\(\varepsilon_j\\) as left minimal indices. B.9 describes the left minimal indices as degrees of polynomial relations among the rows of \\(Q\_{\mathcal L}\\). That is the standard left-nullspace convention.

But the dimension contribution that is naturally associated with a rectangular pencil such as

\\[ [\lambda\quad 1] \\]

is a right minimal index.

I recommend making the following distinctions explicit in the paper:

- Left minimal indices: polynomial dependencies among rows.
- Right minimal indices: polynomial dependencies among columns.
- Finite elementary divisors: finite spectral structure.
- Infinite elementary divisors: structure at infinity.

Then state exactly which of these vanish for the special observer pencil.

### 6. Recommended replacement for B.8

I would split B.8 into two propositions.

B.8a (Smith criterion).

\\[ \boxed{ (5b)\iff d\_{\rm fin}=0. } \\]

This is a general polynomial-matrix result and should be proved directly from Smith form.

B.8b (observer-specific index identity).

State a separate identity of the form

\\[ \sum_j\varepsilon_j = \operatorname{rank}\mathcal L \qquad\text{when }d\_{\rm fin}=0, \\]

but only after proving the relevant special properties of \\(Q\_{\mathcal L}\\), including the treatment of right minimal indices and infinite elementary divisors.

Do not attribute B.8b to the general Kronecker theorem unless the exact hypotheses are supplied.

### 7. References

For the general Kronecker theory and matrix-pencil canonical forms, the following are standard references:

- F. R. Gantmacher, The Theory of Matrices, Vol. II, for canonical forms and singular pencils.
- P. Lancaster and M. Tismenetsky, The Theory of Matrices, for matrix pencils and elementary divisors.
- P. Van Dooren, “The computation of Kronecker’s canonical form of a singular pencil,” Linear Algebra and its Applications 27 (1979), 103–140.

These references are useful for the general decomposition, but they should not be cited as proving the observer-specific identity in B.8b. That identity still needs its own derivation.

Verdict: B.8's Smith criterion is correct. Its second equivalence and its stated index identity require clarification and additional proof. B.9 and B.10 should not be treated as fully established until this is repaired.

## Q4. What should be machine-checked next?

My recommendation is:

Priority 1 — Matrix-rank and row-space layer

Do first

Formalize the elementary rank identities, factorization consequences, and the exact relationship between rank \\(Q\_{\mathcal L}(\lambda)\\) and rank \\(H\\). This is relatively manageable and supports many later results.

Priority 2 — PBH/eigenvector layer

Next

Formalize the factorization \\(Q=DH\\), the rank-drop equivalence, and the PBH criterion. This gives a robust machine-checked spectral foundation.

Priority 3 — Polynomial-matrix/Smith layer

Largest project

Build the polynomial-matrix theory needed for B.8–B.10. This is important, but it is also the largest library project and should be undertaken after the exact intended index conventions and identities have been settled.

### Why this order?

The immediate risk in the current development is not that the PBH argument is wrong. It is that the paper uses rank and index statements whose hypotheses are not yet sufficiently explicit.

A useful intermediate target would be a Lean theorem proving:

\\[ \operatorname{rank}(DH) = \operatorname{rank}H - \dim(\ker D\cap\operatorname{im}H). \\]

Then prove the exact rank-drop criterion for the particular block matrix \\(D(\lambda)\\).

This would make B.12 and B.13c considerably stronger from a verification perspective.

For B.11d, however, I would not simply formalize the current proof. First settle the equality case mathematically. Formalizing an incomplete implication only makes the gap more difficult to notice.

For B.8, I would first write down the correct KCF bookkeeping in a standalone mathematical note. Only then should you invest in Lean formalization.

## Q5. Is the label `[Lean kernel]` acceptable?

Yes, provided the terminology is made more precise.

There is a legitimate distinction between:

1. a theorem whose complete mathematical content is proved in Lean from the stated definitions and previously established theorems;
2. a theorem whose inference is checked in Lean but whose substantive mathematical assumptions remain unproved.

The second category is useful. It makes the logical dependency structure explicit and prevents informal reasoning from being hidden inside a long proof.

But I would avoid the label `[Lean kernel]` by itself. It is potentially ambiguous: readers may interpret it as meaning that the mathematical proposition has been proved in Lean.

I recommend the following labels.

| Label                  | Meaning                                                                                              |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| `[Lean-verified]`      | The theorem is proved in Lean from definitions and already verified results.                         |
| `[Lean-conditional]`   | Lean verifies the implication, but one or more substantive mathematical assumptions remain unproved. |
| `[Paper proof]`        | A complete mathematical proof is supplied but not formalized.                                        |
| `[Exact verification]` | A finite collection of instances has been checked exactly.                                           |
| `[Experimental]`       | Numerical or randomized evidence only.                                                               |

For example, suppose Lean proves

\\[ \bigl(\text{CountingObstruction}\bigr) \land \bigl(\text{CSS}\bigr) \Longrightarrow \bigl(\text{DesiredEquivalence}\bigr). \\]

If `CountingObstruction` and `CSS` are hypotheses rather than proved theorems, then the correct label is

\\[ \boxed{\text{[Lean-conditional]}} \\]

rather than `[Lean-verified]`.

I would also recommend running an axiom audit on the central declarations, for example using Lean's `#print axioms` mechanism. The absence of errors and warnings is good, but it is not by itself a complete audit of the assumptions on which a declaration depends.

Verdict: The methodological choice is acceptable and, in fact, desirable. The labeling must make the conditional nature unmistakable.

# Part II. Audit of the remaining propositions

## A. The Kronecker/Smith chain

### B.8 — Smith criterion

As discussed above, the first equivalence

\\[ (5b)\iff d\_{\rm fin}=0 \\]

is correct.

The second equivalence needs the missing observer-specific index theorem.

I would not retain the present proof as a single argument.

### B.9 — Structural trichotomy

There are two separate assertions here.

First,

\\[ k=q+r_1-h \\]

is the number of left minimal indices, assuming the pencil has \\(q+r_1\\) rows and normal rank \\(h\\). This is the standard dimension count for the left polynomial nullspace.

Second, the report says that \\(k\\) is the number of nonzero left minimal indices. This needs the constant-row-dependence argument.

That argument can be made rigorous.

Suppose a constant row relation among the rows of \\(Q\_{\mathcal L}(\lambda)\\) is given. Write its coefficients as

\\[ \alpha,\beta, \\]

where \\(\alpha\\) multiplies the \\(\lambda\mathcal L-\mathcal LA\\) block and \\(\beta\\) multiplies the chosen independent basis of the \\([CA;C]\\) row space.

The coefficient of \\(\lambda\\) gives

\\[ \alpha^{\mathsf T}\mathcal L=0. \\]

Since \\(\mathcal L\\) has full row rank,

\\[ \alpha=0. \\]

The remaining relation is a constant dependence among the chosen independent rows of the \\([CA;C]\\) basis, so

\\[ \beta=0. \\]

Thus there is no degree-zero left minimal index.

This is a valid argument, provided the \\(CA,C\\) block is genuinely represented by an independent row basis of dimension \\(r_1\\). If the raw rows are used without compression, the proof needs to account for their internal dependencies.

The last sentence of B.9 is less satisfactory:

> \\(d\_{\rm fin}=0\\) with \\(k=0\\) is impossible when \\(\mathcal L\\) has dependent rows.

This does not fit the admissible setting, where \\(\operatorname{rank}\mathcal L=q\\). It should either be removed or rewritten with the exact matrix whose rows are supposed to be dependent.

### B.9b — Type II is empty

This is correct:

\\[ h\ge r_1 \\]

because \\(H\\) contains the row space of \\([CA;C]\\). Therefore

\\[ k=q+r_1-h\le q. \\]

Since \\(\operatorname{rank}\mathcal L=q\\), the stated inequality follows.

This is a clean result.

### B.10 — Dichotomy

The argument is valid once the B.8 index relation is repaired.

As written, it depends on an index identity that has not yet been justified. I would mark B.10 as conditional on the corrected B.8.

## B. The spectral side

### B.12 — Observability reduction

Correct

I checked the factorization:

\\[ Q\_{\mathcal L}(\lambda) = D(\lambda) \begin{bmatrix} \mathcal L\\\CA\\\C \end{bmatrix}, \\]

where

\\[ D(\lambda)= \begin{pmatrix} \lambda I-\Lambda&-G_1&-G_0\\\ 0&I&0\\\ 0&0&I \end{pmatrix}. \\]

The first block row is indeed

\\[ (\lambda I-\Lambda)\mathcal L-G_1CA-G_0C = \lambda\mathcal L-\mathcal LA. \\]

The rank identity

\\[ \operatorname{rank}(DH) = \operatorname{rank}H - \dim(\ker D\cap\operatorname{im}H) \\]

is correct.

The kernel of \\(D(\lambda)\\) consists of vectors

\\[ (u,0,0) \quad\text{with}\quad (\lambda I-\Lambda)u=0. \\]

Such a vector belongs to the image of \\(H\\) precisely when

\\[ u=\mathcal Lx,\qquad CAx=0,\qquad Cx=0. \\]

That is, precisely when

\\[ x\in V,\qquad \mathcal Lx=u. \\]

Therefore rank drops occur exactly when \\(U=\mathcal LV\\) contains a nonzero eigenvector of \\(\Lambda\\).

Finally, PBH gives

\\[ U\text{ contains no nonzero eigenvector of }\Lambda \iff (E,\Lambda)\text{ is observable}, \\]

when \\(\ker E=U\\).

The proof is sound.

One small presentation recommendation: explicitly state that the PBH condition is over \\(\mathbb C\\), since the existence of eigenvalues and eigenvectors is being used.

### B.13c — Exact failure criterion

Correct

The identity

\\[ \mathcal L(\lambda I-A)x = (\lambda I-\Lambda)\mathcal Lx \qquad(x\in V) \\]

is correct under (5a).

Since \\(Cx=0\\) and \\(CAx=0\\),

\\[ C(\lambda I-A)x=0. \\]

Thus

\\[ (\lambda I-A)x\in\mathcal Z \iff \mathcal L(\lambda I-A)x=0. \\]

Also, for \\(x\in V\\),

\\[ x\notin\mathcal Z\iff\mathcal Lx\ne0. \\]

This proves the criterion.

It is an important theorem and should remain central in the paper.

### B.13d — Proportionality-locus classification

As discussed in Q2, correct.

### B.13e — Single-\\(\lambda\\) certificate

Correct under its stated hypotheses

Let

\\[ T=(\lambda_0I-A)|\_V:V\longrightarrow K \\]

be an isomorphism.

For every nonzero \\(z\in\mathcal Z\\), set

\\[ x=T^{-1}z. \\]

Then

\\[ (\lambda_0I-A)x=z\in\mathcal Z. \\]

By B.13c, this is a failure witness whenever

\\[ x\notin\mathcal Z. \\]

Therefore the only exception is

\\[ T^{-1}\mathcal Z\subseteq\mathcal Z. \\]

The assertion about \\(V\cap K=0\\) is also correct. If

\\[ T^{-1}\mathcal Z\subseteq\mathcal Z, \\]

then for every \\(z\in\mathcal Z\\),

\\[ T^{-1}z\in V\cap\mathcal Z. \\]

If \\(V\cap K=0\\), and \\(\mathcal Z\subseteq K\\), this forces

\\[ T^{-1}z=0, \\]

hence \\(z=0\\). Thus no nonzero \\(\mathcal Z\\) can be exceptional.

Finally,

\\[ \dim(V\cap K) = \dim\ker\begin{bmatrix}C\\\CA\\\L_0\end{bmatrix} \ge n-(2p+r) \\]

is a valid rank bound.

This proposition is worth retaining. It gives a useful sufficient condition for whole-family spectral failure at a fixed \\(\lambda_0\\).

### B.13f — Scalar case

One assertion is incorrect

The claim that the failure criterion reduces to

\\[ V\ne K \\]

is correct in the Class I scalar setting, provided

\\[ \dim V=\dim K=1,\qquad V,K\subseteq\ker c, \qquad \dim\ker c=2. \\]

Indeed, if \\(V\ne K\\), then

\\[ \ker c/K \\]

is one-dimensional and the image of a generator \\(v\in V\\) is nonzero. Since

\\[ (\lambda I-A)v\in\ker c, \\]

its image modulo \\(K\\) is a scalar linear polynomial in \\(\lambda\\). It must vanish for some \\(\lambda\in\mathbb C\\). Thus the spectral failure criterion is met.

If \\(V=K\\), then \\(S=V\\), and the quotient domain \\(V/S\\) is zero, so (5b) is automatic.

However, the sentence

> in particular the pencil determinant vanishes identically

is not correct under the natural quotient-pencil interpretation.

When \\(V\ne K\\), the induced pencil is a scalar polynomial of the form

\\[ \lambda-\alpha, \\]

up to a nonzero scalar factor. It has a finite root, but it is not identically zero.

The distinction matters:

- Identically zero: rank is deficient for every \\(\lambda\\).
- Nonzero polynomial with a root: rank drops at at least one finite \\(\lambda\\).

The latter is exactly what is needed for failure of (5b).

I recommend changing the final sentence to:

\\[ \boxed{\text{The scalar quotient pencil is a nonzero affine polynomial and therefore has a finite root.}} \\]

Also, the condition \\(n=p+r+1=3\\) relies on the Class I assumptions \\(p=r=1\\). State that explicitly in the proposition.

### B.14 — Tractable class

Correct

The proof is direct.

If (5b) fails, B.13c gives

\\[ x\in V\setminus\mathcal Z,\qquad (\lambda I-A)x\in\mathcal Z\subseteq K. \\]

Hence

\\[ P_K(\lambda I-A)x=0. \\]

Condition (T\*) says that the map

\\[ P_K(\lambda I-A)B_V \\]

has full column rank for every \\(\lambda\\). Therefore \\(x=0\\), a contradiction.

The caveat is also correct: failure of (T\*) does not imply failure of (5b). The report correctly distinguishes a sufficient condition from a necessary one.

## C. Counting and stratification

### B.11c — Counting identity

The dimension calculation is plausible and the displayed proof is internally consistent, provided the definitions of \\(R,S,W\\) are exactly those used in the earlier sections.

The critical identities are

\\[ \mathcal Z^\perp=C\oplus R \\]

and

\\[ \mathcal Z^\perp\cap S=C\oplus(R\cap S). \\]

Given these, the modular dimension identity gives

\\[ h = \dim(\mathcal Z^\perp+S) = \dim\mathcal Z^\perp+\dim S -\dim(\mathcal Z^\perp\cap S). \\]

The displayed expression

\\[ h=s_0+q-\dim(R\cap S) \\]

then follows from the stated dimensions.

I cannot independently verify the equivalence involving \\(R\cap W\\) without the complete definitions of \\(R,S,W\\) and the Type I condition. The algebraic dimension calculation itself is sound.

### B.11d — CSS reduction

As already explained, the strict inequality is not justified at equality.

The machine-checked logical implication is useful, but the paper statement needs repair before it should be treated as a theorem.

I would explicitly separate:

- the rank obstruction \\(h>q+r_1\\);
- the equality case \\(h=q+r_1\\);
- the CSS regime \\(h\<q+r_1\\).

This will also make the subsequent Class I analysis easier to organize.

## D. Class I: \\(p=r=1\\)

This section contains some of the most interesting results in the report.

### B.18 — Basic dimensions

The dimension identities

\\[ r_1=2,\qquad \dim V=\dim K=n-2 \\]

are correct under the observability and independence assumptions.

Also,

\\[ \dim(V\cap K)\ge n-3 \\]

follows from

\\[ \operatorname{rank} \begin{bmatrix} c\\\cA\\\\\ell \end{bmatrix} \le3. \\]

The assertion

\\[ s_0=3 \iff \ell\notin\operatorname{span}\\{c,cA\\} \\]

is also correct.

The quotient dimensions for \\(\mathcal Z\subseteq V\cap K\\) are consistent:

\\[ \dim(V/S)=q-1, \qquad \dim(X/\mathcal Z)=q+1. \\]

### B.18b — Terminal order

Correct

At \\(q=n-1\\), we have

\\[ \mathcal Z=0. \\]

A failure witness would require

\\[ x\in V\setminus\\{0\\},\qquad (\lambda I-A)x=0. \\]

Thus \\(x\\) would be an eigenvector of \\(A\\) lying in \\(\ker c\\), contradicting observability of \\((c,A)\\).

For (5a),

\\[ \operatorname{rank}\begin{bmatrix}\mathcal L\\\c\end{bmatrix}=n \\]

already holds. Therefore

\\[ \operatorname{rank}\begin{bmatrix}\mathcal L\\\cA\\\c\end{bmatrix}=n, \\]

and (5a) is automatic.

This is a clean terminal-order existence result.

### B.18c — The map \\(\psi\\)

The inclusion

\\[ \operatorname{im}\psi\subseteq\ker c \\]

is immediate:

\\[ c(\lambda I-A)x=\lambda cx-cAx=0 \qquad(x\in V). \\]

The \\(d=1\\) equivalence is also correct for admissible lines satisfying \\(z\notin V\\):

\\[ \boxed{ \text{(5b) fails for }\mathcal Z=\langle z\rangle \iff z\in\operatorname{im}\psi. } \\]

The restriction \\(z\notin V\\) is essential. If \\(z\in V\\), then

\\[ S=V\cap\mathcal Z=\mathcal Z, \\]

and the quotient domain is zero. One cannot use the \\(S=0\\) line criterion there.

I would state B.18c with this qualification explicitly.

### B.18d — Canonical coordinates

Correct

The recurrence is consistent with the companion-form coordinates.

For

\\[ w\in\ker c, \\]

the first \\(n-1\\) coordinates of

\\[ (\lambda I-A)x=w,\qquad x\in V, \\]

determine

\\[ x_3=-w_2,\qquad x\_{k+1}=\lambda x_k-w_k. \\]

The final coordinate gives

\\[ P_w(\lambda)=0. \\]

Since every nonconstant complex polynomial has a root,

\\[ w\in\operatorname{im}\psi \iff P_w\text{ is not a nonzero constant}. \\]

This criterion is exact, including the case \\(P_w\equiv0\\).

### B.18e — Whole-family failure at \\(d=1\\)

This is a significant result. I agree with the three-part argument, with one wording clarification.

For a nonzero line \\(\mathcal Z=\langle z\rangle\subseteq K\\):

(i) If \\(z\in V\\):

Then \\(\mathcal Z\subseteq V\\), so (5a) forces

\\[ A(\mathcal Z)\subseteq\mathcal Z. \\]

Thus \\(z\\) is an eigenvector of \\(A\\) in \\(\ker c\\), contradicting observability. Hence there is no admissible candidate satisfying (5a).

(ii) If \\(z\notin V\\):

As shown in Q1(b),

\\[ cAz\ne0. \\]

Thus

\\[ \operatorname{rank} \begin{bmatrix} \mathcal L\\\cA\\\c \end{bmatrix}=n. \\]

So (5a) holds.

(iii) The spectral condition fails:

The canonical-coordinate recurrence gives

\\[ \deg P_z=n-2 \\]

because the leading coefficient is \\(-z_2\ne0\\).

For \\(n\ge3\\), this is positive. Therefore \\(P_z\\) has a complex root, and

\\[ z\in\operatorname{im}\psi. \\]

By B.18c, (5b) fails.

Hence the following conclusion is justified:

\\[ \boxed{ \text{Every admissible Class I candidate at }d=1 \text{ fails (5b).} } \\]

This is stronger than a numerical observation.

One wording issue: the phrase “the order fails for the whole family” should be specified as “every admissible candidate at this order fails the spectral condition (5b).” It does not mean that every line in \\(K\\) is an admissible candidate; lines in \\(K\cap V\\) are excluded by (i).

### What B.18e does not establish

It does not, by itself, prove

\\[ q\_{\min}=n-1. \\]

It establishes:

- no admissible solution at \\(d=1\\);
- existence at terminal order \\(d=0\\).

To conclude minimum order \\(n-1\\), you still need to exclude all orders with

\\[ d\ge2. \\]

That is an important logical distinction. The numerical observation that \\(q\_{\min}=n-1\\) in the scanned instances is useful evidence, but it is not a proof for the full Class I.

# Part III. The older counting-side results

The report lists A.4, D.3, E.1, E.2, F.2, B.13b, K.1, K.3 and K.4, but the full definitions of their objects and the underlying proofs are not included in this file. I can assess the proof sketches, but I cannot certify the full propositions from the supplied material alone.

A few comments are nevertheless possible.

| Proposition | Assessment                                                                                                                                                                             |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A.4         | Dimension bookkeeping may be straightforward, but the layer definitions are needed to verify it.                                                                                       |
| D.3 / E.2   | The \\(O(n^4)\\) estimate is consistent with \\(O(n)\\) iterations of \\(O(n^3)\\) work, assuming the iteration count and matrix dimensions are as stated.                             |
| E.1         | The invariant-subspace optimization formulation needs its reduction proof checked against the exact definitions of \\(T,B,U_0\\).                                                      |
| F.2         | The implication is valid if the inequalities from E.1 and F.1 have exactly the stated directions and apply to the same feasible set.                                                   |
| B.13b       | The algebraic-geometric interpretation is plausible: the proportionality locus is the inverse image of a rank-at-most-one determinantal variety.                                       |
| K.1         | Correct: every bivector in \\(\Lambda^2\mathbb C^3\\) is decomposable.                                                                                                                 |
| K.3         | A projective dimension argument can guarantee a complex intersection, but it does not automatically produce a rational or real point. The report appropriately flags this distinction. |
| K.4         | The exact verification counts are evidence about the tested cases, not a proof of the general algorithmic claim. The ideal-membership and rational-point steps need their own proofs.  |

The most important point here is that complex projective intersection and existence of a rational point are different assertions. A projective dimension theorem over \\(\mathbb C\\) does not automatically settle a rational feasibility question.

# Part IV. Recommended revisions

I would make the following changes before proceeding to another large computational campaign.

## 1. Correct the theorem inventory

Use these labels:

| Proposition         | Recommended status                                  |
| ------------------- | --------------------------------------------------- |
| B.8 Smith criterion | Retain, as B.8a                                     |
| B.8 index identity  | Rework; observer-specific hypotheses needed         |
| B.9                 | Retain after clarifying minimal-index conventions   |
| B.9b                | Retain                                              |
| B.10                | Conditional on corrected B.8                        |
| B.11c               | Retain, subject to definitions in the earlier setup |
| B.11d               | Revise; equality case unresolved                    |
| B.12                | Retain                                              |
| B.13c               | Retain                                              |
| B.13d               | Retain                                              |
| B.13e               | Retain                                              |
| B.13f               | Correct the determinant sentence                    |
| B.14                | Retain                                              |
| B.18b               | Retain                                              |
| B.18c               | Retain with \\(z\notin V\\) qualification           |
| B.18d               | Retain                                              |
| B.18e               | Retain, with the clarified admissibility proof      |

## 2. Keep three different notions separate

The paper should consistently distinguish:

\\[ \begin{aligned} &\text{normal rank:} && \max\_{\lambda}\operatorname{rank}Q(\lambda),\\\ &\text{pointwise rank:} && \operatorname{rank}Q(\lambda_0),\\\ &\text{constant-rank property:} && \operatorname{rank}Q(\lambda)=h \quad\forall\lambda\in\mathbb C. \end{aligned} \\]

In particular, a pencil can have full normal row rank and still lose rank at finitely many values of \\(\lambda\\). It can also have constant rank smaller than its number of rows.

This distinction is essential in B.8–B.12.

## 3. Keep the two feasibility conditions separate

The report generally does this correctly, but I would reinforce it in the Class I section:

- The \\(\psi\\)-image criterion concerns (5b).
- The row-space condition concerns (5a).
- Full admissibility requires both.

B.18e is particularly valuable because it proves admissibility for \\(z\notin V\\) and then separately proves spectral failure.

## 4. Do not overstate the Class I conclusion

The current theorem is:

\\[ \text{No admissible candidate at }d=1 \text{ satisfies both (5a) and (5b).} \\]

Together with terminal-order existence, this leaves the intermediate orders \\(d\ge2\\) open.

That is still a strong theorem. It should not be weakened by claiming more than it proves.

# Part V. Research direction

My recommendation is to stop expanding the general Kronecker chain temporarily and focus on two mathematically concrete questions.

## Direction A: settle the equality case \\(h=q+r_1\\)

This is the first priority because it affects the logical foundation of the counting/spectral dichotomy.

A good route is:

1. Start from the PBH representation in B.12.
2. Impose the equality \\(h=q+r_1\\).
3. Express the dimension of \\(U=\mathcal LV\\) in terms of the intersection dimensions in B.11c.
4. Determine whether those dimensions force \\(U\\) to contain an eigenvector of \\(\Lambda\\).
5. If not, construct an admissible counterexample or identify an additional hypothesis.

The key is to prove or disprove the equality-exclusion statement directly, rather than infer it from the row-counting argument.

## Direction B: finish the Class I order classification

B.18e has already settled \\(d=1\\). The remaining question is whether there can be a solution for

\\[ d\ge2. \\]

The quotient-pencil formulation suggests the right approach:

\\[ \overline N\_{\mathcal Z}(\lambda): V/S\longrightarrow X/\mathcal Z. \\]

For Class I, the dimensions are especially structured:

\\[ \dim V=n-2,\qquad \dim\mathcal Z=n-1-q. \\]

One possible route is to study the incidence variety

\\[ \mathcal I = \left\\{ (\mathcal Z,[x],\lambda): x\in V\setminus\mathcal Z,\  (\lambda I-A)x\in\mathcal Z \right\\}. \\]

Projecting onto the Grassmannian of admissible \\(\mathcal Z\\)'s gives the set of spectrally bad candidates.

The \\(d=1\\) theorem is an especially favorable case because the bad incidence condition reduces to membership in the image of \\(\psi\\), and the canonical recurrence proves that membership for every admissible line.

For \\(d\ge2\\), the problem is no longer a single-vector membership question. It becomes a subspace-incidence problem. This is where the Grassmannian geometry and the quotient-pencil criterion should be combined.

## Final verdict

The most reliable results in this report are B.12, B.13c–e, B.14, B.18b, and B.18d–e. B.13d is also correct and should be retained.

The two areas requiring the most attention are:

- B.11d: the equality boundary is not settled by the stated proof.
- B.8–B.10: the general Kronecker bookkeeping needs to be corrected before it can support the claimed dichotomy.

The Class I result B.18e is a real advance: it proves that the entire admissible \\(d=1\\) family is spectrally bad. But the full minimum-order conclusion still requires excluding \\(d\ge2\\).

My suggested next deliverable is a short technical note containing (i) a corrected B.8 with explicit left/right/infinite index conventions, and (ii) a standalone equality-case theorem for \\(h=q+r_1\\). Those two results would resolve the most consequential logical uncertainties in the current paper layer.