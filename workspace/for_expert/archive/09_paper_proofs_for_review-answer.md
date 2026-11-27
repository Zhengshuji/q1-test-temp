# Review of `09_paper_proofs_for_review.md`

The paper-proof chain is substantially stronger and more coherent than the earlier versions. In particular, B.6 has a sound elementary coefficient argument, B.8 uses the right global index identity, and B.10 gives a useful finite spectral test. However, I would not yet promote the whole chain to a proved classification: B.7 needs a corrected local Smith-form argument, B.9 needs a more precise minimal-basis justification, and the geometric proof in II.7 has a genuine gap as written.

The most important distinction is between a proposition being true and the proof supplied in the report establishing it. I separate those below, and then address all six questions.

## 1. B.6 — right minimal indices

Verdict: the proof is correct.

From (5a), the row-space inclusion gives

\\[ \mathcal LA=X\mathcal L+Y_1CA+Y_2C. \\]

For a polynomial null vector

\\[ v(\lambda)=\sum\_{k=0}^d\lambda^kv_k, \\]

the coefficient of \\(\lambda^{d+1}\\) in the first block equation gives\
\\(\mathcal Lv_d=0\\). The lower two block equations give\
\\(CAv_d=Cv_d=0\\). Substitution into the displayed row-space identity then gives

\\[ \mathcal LAv_d=0. \\]

Thus the constant vector \\(v_d\\) is itself in the right nullspace of the pencil, and \\(\lambda^dv_d\\) can be subtracted from \\(v(\lambda)\\). The degree decreases, so induction decomposes every polynomial null vector into constant null vectors.

There is no hidden use of the row-space containment \\(\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L\\) here. The only essential hypothesis is (5a).

One wording refinement: say that the right null module is generated over \\(\mathbb C[\lambda]\\) by its constant vectors. Choosing a vector-space basis of the constant nullspace then gives a polynomial-module basis, so all right minimal indices are zero. That last sentence is justified because the module is exactly the polynomial extension of the constant nullspace.

## 2. B.7 — infinite elementary divisors

Proof needs correction

The conclusion

\\[ d\_\infty=h-\operatorname{rank}\mathcal L=h-q \\]

is correct, but the argument in the report that \\(Q\_{\mathcal L}\\) and \\(H\\) have the same infinite elementary divisors is not correct as stated.

The issue is precisely the one raised in the report. The reversed factor is

\\[ D\_{\rm rev}(\mu)=\mu D(1/\mu) = \begin{pmatrix} I-\mu X&-\mu Y_1&-\mu Y_2\\\ 0&\mu I&0\\\ 0&0&\mu I \end{pmatrix}. \\]

Although its upper-left block is invertible at \\(\mu=0\\), the whole matrix is not: the lower diagonal blocks vanish there. So it is not legitimate to infer that multiplication by \\(D\_{\rm rev}\\) preserves all local Smith data at zero.

There is, however, a short direct proof that avoids this problem entirely. Reverse the original pencil:

\\[ Q\_{\rm rev}(\mu) =\mu Q\_{\mathcal L}(1/\mu) = \begin{pmatrix} \mathcal L-\mu\mathcal LA\\\ \mu CA\\\ \mu C \end{pmatrix}. \\]

At \\(\mu=0\\), this matrix has rank \\(q\\), because \\(\mathcal L\\) has full row rank. Its normal rank is \\(h\\).

Now choose \\(h\\) linearly independent rows of \\(H=[\mathcal L;CA;C]\\), including all \\(q\\) rows of \\(\mathcal L\\). This is possible because those \\(q\\) rows are independent and can be extended to a row basis of \\(H\\). Choose \\(h\\) columns making the resulting \\(h\times h\\) minor of \\(H\\) nonzero. The corresponding minor of \\(Q\_{\rm rev}(\mu)\\) has the form

\\[ \mu^{h-q}\bigl(c+O(\mu)\bigr),\qquad c\ne0, \\]

because each of the \\(h-q\\) selected lower rows contributes a factor \\(\mu\\), while the first \\(q\\) rows specialize to \\(\mathcal L\\).

On the other hand, every \\(h\times h\\) minor of \\(Q\_{\rm rev}\\) is divisible by at least \\(\mu^{h-q}\\): there are only \\(q\\) top rows, so any selection of \\(h\\) rows includes at least \\(h-q\\) lower rows. Thus the \\(h\\)-th determinantal divisor has valuation exactly \\(h-q\\).

Since the rank at \\(\mu=0\\) is \\(q\\), the first \\(q\\) local invariant factors are units. Since the normal rank is \\(h\\), the remaining \\(h-q\\) invariant factors are nonunits; their total valuation is \\(h-q\\). Consequently each has valuation exactly one. This proves that all infinite elementary divisors have degree one and that their total degree is \\(h-q\\).

This direct proof is stronger and cleaner than the factor argument in the report. I recommend replacing the existing proof with it.

## 3. B.8 — discrete spectral condition

Verdict: correct, subject to stating the pencil conventions.

For a polynomial matrix pencil, finite elementary divisors are exactly the local invariant factors at finite spectral points. A finite elementary divisor exists precisely when the rank drops below the normal rank at some finite \\(\lambda\\). Therefore

\\[ (5b)\iff d\_{\rm fin}=0. \\]

The Kronecker index identity is

\\[ \sum_j\eta_j+\sum_i\varepsilon_i+d\_{\rm fin}+d\_\infty=h, \\]

where \\(h\\) is the normal rank. This convention counts the degrees of both left and right minimal indices, and the degrees of the finite and infinite elementary divisors. It is consistent with rectangular pencils: a right singular block contributes its right minimal index to the normal rank, a left singular block contributes its left minimal index, and a regular block contributes its elementary-divisor degree.

Using B.6 and the corrected B.7,

\\[ 0+\sum_i\varepsilon_i+d\_{\rm fin}+(h-q)=h, \\]

so

\\[ \boxed{\sum_i\varepsilon_i=q-d\_{\rm fin}.} \\]

Hence the stated equivalence follows.

For the paper, cite a source that explicitly gives the Kronecker canonical form and this dimension/index identity for rectangular pencils. Avoid citing a square-pencil-only statement without explaining the extension.

## 4. B.9 — counting the left minimal indices

Verdict: the count is correct, but the identification of constant vectors with zero indices should be justified via a minimal basis.

Let \\(m=q+2p\\) be the number of rows. Over the PID \\(\mathbb C[\lambda]\\), the left null module is free. Its rank is

\\[ m-h=q+2p-h, \\]

because its rank over the fraction field \\(\mathbb C(\lambda)\\) is the dimension of the left kernel of \\(Q\_{\mathcal L}(\lambda)\\) over that field.

The number of left minimal indices, counted with multiplicity, is this module rank. The number of zero left minimal indices is the dimension of the space of constant left null vectors. To see the latter statement carefully, choose a reduced minimal polynomial basis of the left null module. The predictable-degree property of a reduced minimal basis implies that a constant element can only be a constant linear combination of basis vectors of degree zero. Thus the dimension of the constant left nullspace is exactly the number of zero minimal indices.

For a constant left null vector \\(\varphi=(\varphi_1,\varphi_2,\varphi_3)\\), the pencil identity gives

\\[ \varphi_1\mathcal L=0,\qquad -\varphi_1\mathcal LA+\varphi_2CA+\varphi_3C=0. \\]

Full row rank of \\(\mathcal L\\) implies \\(\varphi_1=0\\). The remaining condition is precisely

\\[ (\varphi_2,\varphi_3)\in\ker\_{\rm left}[CA;C]. \\]

The dimension is \\(2p-r_1\\). Therefore

\\[ \\#\\{\text{nonzero left minimal indices}\\} =(q+2p-h)-(2p-r_1) =\boxed{q+r_1-h}. \\]

There is also a useful consistency check: \\(h\ge r_1\\), since \\(H\\) contains the rows of \\([CA;C]\\), and \\(h\le q+r_1\\), since (5a) implies \\(\operatorname{row}\mathcal LA\subseteq\operatorname{row}H\\), while \\(\operatorname{rank}H\le q+r_1\\) is immediate. Thus the count \\(q+r_1-h\\) is nonnegative.

If \\(h\ge q+r_1\\), it must be zero. All left minimal indices are then zero, so their sum is zero. B.8 gives

\\[ d\_{\rm fin}=q>0 \\]

for \\(q>0\\), and hence (5b) fails.

This proves the counting obstruction. I would make the reduced-minimal-basis argument explicit in the paper; saying that constant vectors are “exactly the zero left indices” is right, but a reader may reasonably ask for the bridge between the vector-space dimension and the multiset of minimal indices.

## 5. B.10 — spectral confinement

Verdict: correct.

The factorization

\\[ Q\_{\mathcal L}(\lambda)=D(\lambda)H \\]

follows directly from (5a), with \\(X\\) a \\(q\times q\\) matrix. The matrix \\(D(\lambda)\\) is square of size \\(q+2p\\), and it is invertible whenever \\(\lambda I-X\\) is invertible. Hence

\\[ \lambda\notin\operatorname{spec}X \quad\Longrightarrow\quad \operatorname{rank}Q\_{\mathcal L}(\lambda)=\operatorname{rank}H=h. \\]

So (5b) only needs to be checked at the eigenvalues of \\(X\\).

No use is made of the containment of \\(\operatorname{row}L_0\\) in \\(\operatorname{row}\mathcal L\\). The needed hypotheses are full row rank of \\(\mathcal L\\) for the earlier setup and (5a) for the factorization.

One practical qualification: over \\(\mathbb C\\), the eigenvalues need not be rational or real. The report correctly warns that a rational-\\(\lambda\\) scan is not a valid substitute.

## 6. II.6 — dimension formula and uniformity

### The dimension formula

Verdict: correct.

The identity

\\[ h=\dim(\mathcal Z^\perp+W) \\]

follows because

\\[ \operatorname{row}\mathcal L+W =\mathcal Z^\perp+W, \\]

using \\(\operatorname{row}C\subseteq W\subseteq\mathcal Z^\perp+W\\). Since \\(\operatorname{rank}[C;\mathcal L]=p+q\\),

\\[ \dim\mathcal Z^\perp=p+q. \\]

The modular dimension formula then gives

\\[ \begin{aligned} h &=p+q+r_1-\dim(\mathcal Z^\perp\cap W)\\\ &=q+r_1-\bigl(\dim(\mathcal Z^\perp\cap W)-p\bigr)\\\ &=\boxed{q+r_1-\delta}. \end{aligned} \\]

Here \\(\delta\ge0\\), and Type I is exactly \\(\delta=0\\).

### The uniformity identity

Verdict: the conditional algebra is correct; the geometric hypothesis needs an intrinsic formulation and a precise definition of \\(V'\\).

If a chart represents the augmented subspace as a fixed base subspace plus a variable \\(t\\)-dimensional part, and if \\(V'\\) is genuinely that variable part in a fixed complement to the base, then the key condition is that the new part contributes \\(t\\) dimensions modulo \\(S\\). In intrinsic terms, the relevant condition is

\\[ \dim\bigl((S+V')/S\bigr)=t. \\]

When \\(V'\\) is a \\(t\\)-dimensional subspace, this is equivalent to

\\[ V'\cap S=\\{0\\}. \\]

Under that condition,

\\[ \dim(S+V')=s_0+t=s_0+q-r, \\]

which yields the claimed uniformity criterion.

But this interpretation depends on what \\(V'\\) actually denotes in the chart construction. If it is a parameter matrix, a graph, or a subspace in a quotient rather than the literal new subspace, the intrinsic condition should be written using its image in the relevant quotient. The invariant statement is always that the image of the augmentation direction in the quotient by \\(S\\) has dimension \\(q-r\\).

I would not yet use this as an unconditional arithmetic criterion for \\(q\_{\min}>q_0\\). The report itself says the definition of \\(V'\\) is operational. To settle this, the paper should include:

1. the ambient vector space in which \\(V'\\) lives;
2. the fixed base subspace from which the augmentation is taken;
3. the map from the chart parameter to the actual augmentation subspace;
4. a proof that \\(V'\cap S=0\\) is equivalent to the quotient-dimension condition above.

If those details are supplied, the identity is elementary. Without them, the conditional statement is not yet independently checkable.

## 7. II.7 — the whole-family counterexample

Geometric proof incomplete as written

The conclusion may well be correct, especially in view of the three independent algebraic certificates reported in the note. But Step 2 has two separate gaps that must be filled before the projective argument can be accepted.

### Gap 1: \\(\lambda(x)\\) is not automatically a scalar

Here \\(L_0\\) is \\(2\times6\\), so both \\(L_0Ax\\) and \\(L_0x\\) are vectors in \\(\mathbb C^2\\). The expression

\\[ \lambda(x)=\frac{L_0Ax}{L_0x} \\]

is not defined as a scalar ratio of vectors unless

\\[ L_0Ax\in\operatorname{span}\\{L_0x\\}. \\]

That proportionality must be proved for every \\(x\in V\\) with \\(L_0x\ne0\\).

It is not a consequence of \\(x\in\ker[C;CA]\\). It is an additional property of this particular numerical instance. The report's Step 2 omits it. If the proportionality holds, one can define the scalar locally by choosing a nonzero coordinate of \\(L_0x\\); one must also check that the resulting local definitions agree on overlaps.

### Gap 2: the domain is not automatically all of \\(\mathbb P(V)\\)

The assertion that a nonconstant morphism \\(\mathbb P^1\to\mathbb P^1\\) is surjective is correct. The problem is that the displayed formula is only defined where \\(L_0x\ne0\\), and potentially also where \\(z(x)\ne0\\). That is generally an open subset of \\(\mathbb P^1\\), not a complete curve. A nonconstant map from an open subset need not have closed image or be surjective.

For example, the inclusion \\(\mathbb A^1\hookrightarrow\mathbb P^1\\) has nonclosed image and misses the point at infinity. Thus completeness of \\(\mathbb P^1\\) cannot be invoked until an everywhere-defined morphism on the complete source has actually been constructed.

There are two ways to repair the proof:

1\. Show the formula is defined on all of \\(\mathbb P(V)\\). Prove \\(L_0x\ne0\\) and \\(z(x)\ne0\\) for every nonzero \\(x\in V\\), and prove the proportionality above. Then \\(\Phi\\) is genuinely a morphism \\(\mathbb P^1\to\mathbb P^1\\). If it is nonconstant, it is surjective.

2\. Extend the rational map and handle the excluded points. A nonconstant rational map from a smooth projective curve to \\(\mathbb P^1\\) extends to a morphism. But surjectivity of the extension alone is insufficient: a particular target line might have all its preimages among the points excluded from the original formula. You must show that every target line has at least one preimage in the original domain.

The report's reference to the chart \\(L_0x\ne0\\) does not establish the first repair. It is important to prove that this chart is all of \\(\mathbb P(V)\\), or to carry out the second repair explicitly.

My recommendation: retain the three algebraic proofs as the primary proof of whole-family infeasibility, provided their elimination and gcd computations are exact and their rank strata are correctly handled. Keep the geometric proof as an independent proof only after the two missing properties have been verified. The algebraic certificates and the geometric argument are logically separate: the former do not fill the missing steps in the latter.

## 8. II.8 — quotient form of (5a)

Verdict: correct, with a notation correction.

Let \\(\pi\\) be the quotient map by \\(W=\mathcal J\\). From the machine-checked first step,

\\[ (5a)\iff \operatorname{row}\mathcal LA \subseteq\operatorname{row}\mathcal L+W. \\]

Applying the quotient map gives

\\[ (5a)\iff \pi(\operatorname{row}\mathcal LA) \subseteq\pi(\operatorname{row}\mathcal L). \\]

This is the correct quotient statement. I would write it in row-space notation rather than \\(\pi(\mathcal VA)\subseteq\pi(\mathcal V)\\), unless \\(\mathcal V\\) has already been defined as the row space of \\(\mathcal L\\). In the report, \\(\mathcal Z\\) denotes a kernel, so using \\(\mathcal V\\) without a precise definition risks confusing row and null spaces.

The negative implication mentioned in the report is plausible and is consistent with the distinction between the quotient by \\(W\\) and a further quotient by \\(B=\pi(\mathcal JA)\\). But I would not confirm that counterexample from this note alone: the actual matrices and the precise definitions of the induced map and subspaces are not included here. The safe course is to retain the exact quotient equivalence above and omit the negative statement until its counterexample is reproduced in the paper.

## 9. Answers to Q1–Q6

### Q1. Are the left-index counts correct?

Yes. The count

\\[ \\#\\{\text{all left minimal indices}\\}=q+2p-h \\]

is correct, because the left null module is free over \\(\mathbb C[\lambda]\\) and has that rank.

The number of zero left indices is the dimension of the constant left nullspace, namely \\(2p-r_1\\). For publication-level rigor, justify this using a reduced minimal basis and its predictable-degree property. It follows that

\\[ \boxed{\\#\\{\text{nonzero left minimal indices}\\}=q+r_1-h.} \\]

The argument does not require B.6 for the count itself. B.6 is needed later when B.8 converts the sum of the left indices into the finite elementary-divisor degree.

### Q2. Does \\(D(\lambda)\\) preserve the infinite elementary divisors?

Not for the reason given in the report. The reversed \\(D\\) is not invertible at \\(\mu=0\\), so the claim that it contributes no local divisor is insufficient.

The conclusion \\(d\_\infty=h-q\\) is nevertheless correct. Replace the argument by the direct determinantal-divisor proof in Section 2 above. It establishes the exact valuation of the \\(h\\)-th determinantal divisor and hence the total degree of the infinite elementary divisors.

### Q3. What is the intrinsic form of the uniformity hypothesis?

The invariant formulation is that the augmentation contributes its full \\(q-r\\) new dimensions modulo \\(S\\):

\\[ \boxed{\dim\bigl((S+V')/S\bigr)=q-r.} \\]

When \\(V'\\) is a \\((q-r)\\)-dimensional subspace in the ambient space and is the literal new augmentation direction, this is equivalent to \\(V'\cap S=\\{0\\}\\).

Under this condition,

\\[ h=\dim(S+V')=s_0+q-r, \\]

and therefore

\\[ h\ge q+r_1\iff s_0\ge r_1+r. \\]

But the report needs to define \\(V'\\) intrinsically before using this as a general chart theorem. In particular, it must establish that \\(V'\\) is the actual new subspace, or replace it by its image in the quotient by the fixed base subspace. Until then, the uniformity criterion is valid only conditionally.

### Q4. Is the surjectivity argument in II.7 legitimate?

Not as currently written. A nonconstant morphism from \\(\mathbb P^1\\) to \\(\mathbb P^1\\) is surjective, but the formula in the report is only defined on an open subset unless the missing nonvanishing conditions are proved. Also, the vector proportionality needed to define \\(\lambda(x)\\) is not established.

Prove that the map is defined everywhere, or extend it and show that no target line has all its preimages among the excluded points. Otherwise, rely on the exact algebraic certificates for the whole-family result.

### Q5. Is the subdeterminant/Bézout route closed as a complexity route?

The explicit enumeration route is not a viable polynomial-size encoding in the controlled regime described in the report. If the number of maximal minors and the number of charts grow exponentially, enumerating them cannot establish a polynomial-size \\(\exists\mathbb R\\) formulation.

But this does not show that the problem is outside \\(\exists\mathbb R\\), nor does it rule out a compact representation of the same algebraic condition. The distinction is important: a large explicit list of determinants is one representation, not a lower bound on every possible representation.

Of the alternatives, I would prioritize them as follows:

1. Implicit polynomial-matrix formulation. Preserve the pencil as a matrix polynomial and investigate whether the required rank condition can be expressed using a polynomial-size circuit or a structured linearization. This is the most promising direction because it avoids expanding every maximal minor.
2. Fixed-witness and local certificates. For a fixed candidate augmentation, use a selected nonzero minor and exact polynomial gcd/Bézout certificates. This is valuable for verification and for a practical certificate-based decision procedure, even if it is not a polynomial-size global encoding.
3. Resultant/elimination formulations. Explore these only after identifying a compact way to represent the common-zero condition for the entire family of maximal minors. A resultant of two selected minors is not sufficient unless those two minors control all possible rank drops.
4. Abstract complexity frameworks. Defer claims about \\(\exists\mathbb R\\)-hardness or non-membership until a compact encoding or a genuine lower-bound argument is available.

One additional route deserves attention: B.10 confines every finite rank drop to \\(\operatorname{spec}\Lambda\\). This may allow a formulation using the characteristic polynomial of \\(\Lambda\\), rather than treating \\(\lambda\\) as an unrestricted variable. It does not by itself eliminate the need to encode the rank condition, but it is a useful structural reduction.

### Q6. Is there a chart-uniform invariant for Type III?

There is a natural componentwise algebraic invariant, but I do not see a universal dimension-only invariant analogous to the counting criterion.

Fix an irreducible component \\(Y\\) of an admissible chart, and fix a stratum on which the relevant pencil rank is constant. Let

\\[ P_y(\lambda) \\]

denote the corresponding polynomial matrix pencil, with \\(y\in Y\\). Consider the ideal generated by its maximal minors, over the function field \\(\mathbb C(Y)\\):

\\[ I_Y=\bigl(\text{maximal minors of }P_y(\lambda)\bigr) \subseteq \mathbb C(Y)[\lambda]. \\]

Its monic gcd, when the minors are not all zero, defines a generic finite-divisor polynomial. Its degree

\\[ g_Y=\deg\gcd\bigl(\text{maximal minors of }P_y(\lambda)\bigr) \\]

is invariant under changes of coordinates and is a useful componentwise generic invariant.

Its interpretation is:

- \\(g_Y=0\\): the generic point of that component has no finite rank drop.
- \\(g_Y>0\\): the generic point has a finite spectral obstruction.
- Specializations can change the gcd degree. In particular, a component with \\(g_Y>0\\) can still contain exceptional feasible points where the specialized gcd becomes constant.

That last phenomenon is exactly why a generic positive gcd degree does not prove that an entire chart is infeasible.

For a genuinely uniform statement, I would use the relative finite-divisor locus rather than just \\(g_Y\\). Define

\\[ \mathscr D_Y= \\{(y,\lambda):\operatorname{rank}P_y(\lambda) <\operatorname{normalrank}P_y\\}. \\]

The projection of \\(\mathscr D_Y\\) to \\(Y\\) is the spectral-failure locus. A point \\(y\\) is spectrally feasible precisely when its fiber is empty.

This gives an exact geometric characterization:

- Type III occurs at \\(y\\) exactly when the fiber over \\(y\\) is nonempty.
- The whole component is Type III exactly when the projection covers the entire component.
- The component has at least one spectrally feasible point exactly when that projection is not all of the component.

This is more informative than a generic gcd degree, because it distinguishes generic behavior from behavior at every parameter.

There is also a useful refinement from B.10. On a chart where the factorization coefficients \\(\Lambda(y)\\) can be chosen regularly, every bad \\(\lambda\\) satisfies

\\[ \det(\lambda I-\Lambda(y))=0. \\]

The characteristic polynomial is monic in \\(\lambda\\). Consequently, the projection of the rank-drop locus intersected with this characteristic equation is finite over the chart, and hence closed. On such a chart and fixed-rank stratum, the spectral-failure locus is therefore closed and the feasible locus is open.

This deserves investigation because it appears sharper than the statement in III.2 that the feasible set is merely constructible and neither open nor closed. The qualification is important: the regular choice of \\(\Lambda\\), the fixed-rank stratum, and the chart domain must all be specified. When different rank strata or different coefficient charts are combined, the global set may only be constructible.

My recommendation for Q6: use \\(g_Y\\) as the generic invariant, and the relative finite-divisor locus as the exact uniform invariant. Do not expect a formula involving only \\(\dim(\operatorname{row}L_0\cap W)\\): the spectral side depends on the action of \\(A\\) on the relevant subspaces, not just their dimensions and intersections.

## 10. Two further issues in Part III

There are two statements outside Q1–Q6 that I would correct or qualify before using the report as a formal project status document.

### 10.1 The sufficient condition in III.1 needs checking

The report states

\\[ \dim(\operatorname{row}L_0\cap W)\le p \quad\Longrightarrow\quad \text{every admissible augmentation at }q_0\text{ is Type I}. \\]

As written, this does not follow from the dimension formula in II.6. Since

\\[ \operatorname{row}L_0\subseteq\operatorname{row}\mathcal L, \\]

any nonzero vector in \\(\operatorname{row}L_0\cap W\\) also belongs to \\(\operatorname{row}\mathcal L\cap W\\). But Type I requires

\\[ \operatorname{row}\mathcal L\cap W=\\{0\\}. \\]

Thus a nonzero intersection of \\(\operatorname{row}L_0\\) with \\(W\\) points in the opposite direction.

Perhaps the intended condition was

\\[ \dim\bigl(\operatorname{row}[C;L_0]\cap W\bigr)=p, \\]

which says that the intersection is exactly the unavoidable \\(\operatorname{row}C\\), or equivalently

\\[ \operatorname{row}L_0\cap W=\\{0\\}. \\]

Those are materially different statements. Please check the original definition and the 18-instance test before retaining the current wording.

### 10.2 The claim that the feasible set is not open deserves reconciliation with B.10

As explained under Q6, on a fixed chart and fixed-rank stratum, B.10 potentially gives a finite projection of the bad spectral locus. If the factorization coefficients are regular there, this makes the bad locus closed and the feasible locus open relative to that stratum.

This does not automatically make the feasible set open in the union of all charts and rank strata. But the report should distinguish:

- open or closed relative to one fixed-rank chart;
- constructible in the union of finitely many such strata;
- open or closed in the full admissible parameter space.

I would not state simply that the feasible set is “not open” until this local finite-projection argument has been checked against the precise parameterization used by the program.

## 11. Recommended revisions and priorities

| Priority | Action                                                                  | Reason                                                                  |
| -------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| 1        | Replace B.7 with the direct reversed-pencil determinantal-divisor proof | Removes a genuine gap in the current argument                           |
| 2        | Add the reduced-minimal-basis justification to B.9                      | Makes the zero-index count rigorous                                     |
| 3        | Repair or demote the geometric proof in II.7                            | Scalar proportionality and projective-domain issues remain              |
| 4        | Define \\(V'\\) intrinsically and prove the uniformity hypothesis       | Needed before using the arithmetic criterion                            |
| 5        | Check the intersection condition in III.1                               | The current implication appears inconsistent with the dimension formula |
| 6        | Investigate the finite-projection consequence of B.10                   | May sharpen the chart-wise description of Type III                      |
| 7        | Continue the implicit polynomial-matrix route                           | The explicit minor enumeration is not a promising complexity encoding   |

Overall assessment: B.6, B.8, B.10, the basic dimension formula, and the quotient form of (5a) are in good shape. B.9 is correct but needs one standard minimal-basis detail. B.7's conclusion is right but its current proof is not. The whole-family counterexample is promising and appears well supported by the reported independent algebraic certificates, but the geometric proof should not yet be presented as complete.

The next most valuable step is to revise B.7 and B.9, then provide the exact chart definition of \\(V'\\) and the two-dimensional proportionality calculation used in II.7. Those additions would make this report substantially closer to a paper-ready proof package.