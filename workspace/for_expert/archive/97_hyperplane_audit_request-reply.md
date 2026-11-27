# **Audit of Report 97: the hyperplane layer**

The new report contains several solid results, but there is one important structural issue that affects Claims 5–6: **the pencil built from a basis of&#x20;**\\(U^\perp\\)**&#x20;is not automatically the same pencil as the one in the feasibility condition.** The rank argument is valid in the full-row-space pattern where \\(V=U^\perp\\), but it cannot be transferred unchanged to an arbitrary \\(V\subsetneq U^\perp\\).

My overall assessment is:

- **Claim 2:** correct.
- **Claim 3:** correct for complex geometric feasibility, with a rational-point qualification.
- **Claim 5:** correct for the auxiliary \\(U^\perp\\)-pencil; it implies the desired feasibility obstruction only under an additional equality condition.
- **Claim 6:** correct in the stated \\(n=5,p=1,q=3\\) pattern, and more generally when \\(V=U^\perp\\); not established as a theorem for arbitrary \\(q\\).
- **Claim 7:** correct.
- **Claim 8:** correct, with the stated nonzero-eigenvalue hypothesis.
- **Claim 9:** a valid structural counterexample to eigen-fibre sufficiency.
- **Claim 1:** the component argument is incomplete; the Grassmannian-limit sentence does not establish incomparability.
- **Claim 10:** useful computational evidence, not yet a theorem.
- **Claim 11:** the generic-tall-pencil intuition is correct in an unrestricted pencil space, but the structured family needs an additional dominance or non-containment argument.

I will go through the claims and then give a revised theorem package and a concrete route forward.

## **1. Claim 1 — the component decomposition is not proved yet**

The proposed decomposition is plausible, and the bound on the number of eigenvalues is sound. However, the proof of irreducible-component status has a gap.

### **1.1 What is correct**

Let

\\[ B=\mathbb P\\{v\in K_0:L_0v=L_0Av=0\\}. \\]

This is a projective linear subspace, provided it is nonempty. Hence it is irreducible.

For each eigenvalue \\(\lambda\\),

\\[ E\_\lambda = \mathbb P\bigl(K_0\cap\ker(A-\lambda I)\bigr)\cap B \\]

is also a projective linear subspace, if nonempty. In particular, it is irreducible.

Distinct eigenspaces for distinct eigenvalues are linearly independent. Moreover, if \\(v\in E\_\lambda\\), then

\\[ v\in K_0,\qquad Av=\lambda v\in K_0, \\]

so

\\[ v\in K_0\cap A^{-1}K_0. \\]

Choosing one nonzero vector from each nonempty \\(E\_\lambda\\), for distinct eigenvalues, gives linearly independent vectors in \\(K_0\cap A^{-1}K_0\\). Therefore

\\[ \\#\\{\lambda:E\_\lambda\ne\varnothing\\} \le \dim(K_0\cap A^{-1}K_0) =\delta. \\]

Thus the proposed count \\(1+\delta\\) is a valid upper bound **if** each eigen fibre really contributes at most one irreducible component and the non-eigen closure contributes at most one.

### **1.2 The Grassmannian-limit argument is insufficient**

The issue is the assertion:

> Over \\(\sigma\in E\_\lambda\\), the fibre of \\(Z^\circ\\) is a Grassmannian limit of \\((d_0-2)\\)-dimensional spaces while \\(F\_\lambda\\)'s fibre has dimension \\(d_0-1\\).

A difference in fibre dimensions does not, by itself, prove that \\(F\_\lambda\\) is not contained in \\(\overline{Z^\circ}\\).

There are two separate problems.

**First**, the fibre of the closure is not necessarily the closure of the fibres:

\\[ \overline{Z^\circ}\cap\pi^{-1}(\sigma) \quad\text{need not equal}\quad \overline{Z^\circ\cap\pi^{-1}(\sigma)}. \\]

Limits may be taken while the base point \\(\sigma\\) also varies. This is particularly relevant when \\(E\_\lambda\\) is positive-dimensional.

**Second**, the relevant Grassmannian family has to be specified precisely. The row spaces are constrained not only by containment in \\(U(\sigma)^\perp\\), but also by their dimension and by the prescribed intersection condition

\\[ \dim(V\cap K_0)=k-1. \\]

The family of such spaces need not be a vector bundle over the whole base without a constant-rank argument.

### **1.3 What would complete the proof?**

You need a statement of the following form.

For each \\(\sigma\in E\_\lambda\\), identify the limiting row spaces arising from non-eigen directions approaching \\(\sigma\\), and prove that they form a proper closed subset of the admissible eigen fibre.

One possible approach is to work with the Grassmannian embedding

\\[ V\longmapsto [\wedge^q V] \\]

and calculate the limiting Plücker coordinates as \\(U(\sigma')\\) degenerates from dimension two to dimension one. The key question is whether every limit necessarily satisfies an additional incidence condition that a general point of \\(F\_\lambda\\) does not satisfy.

If that can be shown, then \\(F\_\lambda\not\subseteq\overline{Z^\circ}\\). But the dimension comparison in the report is not yet that proof.

**Verdict:** the eigenvalue count is proved; the component decomposition and the component count are not yet proved.

## **2. Claim 2 — the bad locus is closed**

Correct

The properness argument works even when \\(Y\\) is open.

Suppose \\(Y\\) is a locally closed variety on which

\\[ \operatorname{rank}H(y)=\omega \\]

holds everywhere. Define

\\[ \mathcal D = \left\\{ (y,[s:t])\in Y\times\mathbb P^1: \operatorname{rank}(sH(y)-tH_A(y))<\omega \right\\}. \\]

The vanishing of all \\(\omega\times\omega\\) minors makes \\(\mathcal D\\) closed in \\(Y\times\mathbb P^1\\).

At \\([s:t]=[1:0]\\), the matrix is \\(H(y)\\), which has rank \\(\omega\\). Thus

\\[ \mathcal D\cap (Y\times\\{[1:0]\\})=\varnothing. \\]

Consequently, the projection of \\(\mathcal D\\) to \\(Y\\) is exactly the affine bad locus.

Now for your specific question: yes,

\\[ Y\times\mathbb P^1\longrightarrow Y \\]

is proper. It is the base change of the proper morphism

\\[ \mathbb P^1\longrightarrow\operatorname{Spec}\mathbb C. \\]

Properness is preserved by base change, and there is no requirement that \\(Y\\) be complete or projective.

Therefore the image of \\(\mathcal D\\) is closed in \\(Y\\).

**One qualification:** if \\(Y\\) is merely locally closed in a larger ambient variety, this establishes closedness relative to \\(Y\\), not necessarily closedness in the ambient variety. That is exactly what Claim 3 needs.

## **3. Claim 3 — generic-gcd criterion**

Correct, for complex feasibility

The argument is correct, provided \\(Y\\) is an irreducible algebraic variety and the minors are regarded as functions on \\(Y\\).

Let

\\[ K=\overline{\mathbb Q(Y)} \\]

be the algebraic closure of the function field, with the understanding that the variety has been base-changed appropriately if necessary. Then

\\[ \gcd_I m_I=1\quad\text{in }K[\lambda] \\]

is equivalent to the generic pencil having no common root.

By Claim 2, the bad locus \\(\mathcal B\\) is closed in \\(Y\\). Since \\(Y\\) is irreducible, either

- \\(\mathcal B=Y\\), or
- \\(Y\setminus\mathcal B\\) is a nonempty open dense subset.

Thus

\\[ Y\text{ has a complex feasible point} \iff \gcd_I m_I=1 \text{ over }\overline{\mathbb Q(Y)}[\lambda]. \\]

There is an important limitation for the original rational synthesis problem:

\\[ \boxed{\text{A nonempty complex open subset need not contain a rational point.}} \\]

Therefore Claim 3 is a criterion for complex geometric feasibility on \\(Y\\), not automatically for the existence of a rational observer.

There are useful special cases where rational points can be recovered. For example, if \\(Y\\) is rationally parametrized by an affine parameter \\(t\\), and the generic gcd is one in \\(\mathbb Q(t)[\lambda]\\), clearing denominators gives a nonzero polynomial \\(d(t)\\) such that every rational specialization with \\(d(t)\ne0\\) is good. This yields rational feasible points.

But that conclusion requires the rational parametrization and a rational specialization argument; it does not follow from Claim 3 alone.

## **4. Claim 4 — quotient pencil**

The quotient-pencil argument is valid in the specific full-row-space setting used in Report 96, but its hypotheses should be made explicit.

Let \\(Q\\) be a basis matrix of \\(U^\perp\\). For a non-eigen \\(v\\), choose a basis

\\[ [N_1\ \ v] \\]

of \\(K_0\\). Since \\(v,Av\in U\\), we have

\\[ Qv=0,\qquad QAv=0. \\]

The \\(v\\)-column of

\\[ Q(\lambda I-A)[N_1\ \ v] \\]

is therefore zero.

Since \\(C\\) has full row rank and its rows lie in \\(U^\perp\\), they can be included among the rows of \\(Q\\). For every row \\(c\\) of \\(C\\),

\\[ c(\lambda I-A)N = \lambda cN-cAN=0. \\]

So the corresponding rows vanish identically.

In the \\(n=5,p=1,q=3\\) pattern, \\(Q\\) has three rows. Removing the \\(C\\)-row and the fixed kernel column leaves a \\(2\times2\\) pencil.

The key remaining issue is the leading coefficient. If

\\[ \operatorname{rank}(QN)=k-1, \\]

then after removing the zero column and the \\(p\\) zero rows, the remaining leading coefficient has full column rank. In the square case it is invertible.

This rank condition follows if the actual observer row space is \\(V=U^\perp\\) and \\(\operatorname{rank}H=k-1\\). It does not follow merely from \\(V\subseteq U^\perp\\).

That distinction is essential in the next claims.

## **5. Claim 5 — rank bound**

Correct for the auxiliary pencil; qualification needed for the observer pencil

The proof of the displayed rank bound is correct for

\\[ M(\lambda)=Q(\lambda I-A)N, \\]

where \\(Q\\) is a basis matrix of \\(U^\perp\\).

Indeed, for non-eigen \\(v\\),

\\[ \dim U=2,\qquad \dim U^\perp=n-2. \\]

Every row of \\(C\\) lies in \\(U^\perp\\), and

\\[ C(\lambda I-A)N=0. \\]

Because \\(\operatorname{rank}C=p\\), the \\(p\\) rows of \\(C\\) are linearly independent and can be included in a basis of \\(U^\perp\\). Hence \\(M\\) has \\(p\\) identically zero rows, and

\\[ \boxed{\operatorname{rank}M(\lambda)\le n-2-p.} \\]

Your question about independence is straightforward: yes, it is automatic from \\(\operatorname{rank}C=p\\).

However, there is a distinction between \\(M\\) and the actual observer pencil

\\[ \lambda H-H_A = L(\lambda I-A)N. \\]

If \\(V=\operatorname{row}L\\) is a proper subspace of \\(U^\perp\\), then \\(L\\) is not a basis matrix of \\(U^\perp\\). The rank bound for \\(Q(\lambda I-A)N\\) does not automatically give a rank bound for \\(L(\lambda I-A)N\\).

The clean corrected statement is:

> **Claim 5, corrected.** For every non-eigen \\(v\\), the auxiliary pencil obtained by restricting \\(\lambda I-A\\) to \\(U^\perp\\) has rank at most \\(n-2-p\\). If the actual observer row space is \\(V=U^\perp\\), this is also a rank bound for the observer pencil.

For the original observer problem, this equality is available in the pattern

\\[ q=n-2,\qquad \dim V=q,\qquad V\subseteq U^\perp, \\]

because then necessarily \\(V=U^\perp\\).

## **6. Claim 6 —&#x20;**\\(p=1\\)**&#x20;implies non-eigen infeasibility**

Correct in the full-row-space pattern

The dimension comparison is correct.

Write

\\[ r=\operatorname{rank}\begin{bmatrix}C\\\CA\end{bmatrix}, \qquad k=n-r. \\]

Then

\\[ (n-2-p)-(k-1)=r-p-1. \\]

Therefore

\\[ n-2-p\begin{cases} \<k-1,&r\<p+1,\\\ =k-1,&r=p+1,\\\ >k-1,&r>p+1. \end{cases} \\]

For \\(p=1\\), the stacked matrix \\([C;CA]\\) has two rows, so

\\[ r\le2=p+1. \\]

Thus only the first two cases occur.

### **Case 1:&#x20;**\\(r<2\\)

Here

\\[ n-3\<k-1. \\]

By Claim 5, the auxiliary pencil has rank at most \\(n-3\\), strictly less than the required rank \\(k-1\\). Therefore the pencil cannot satisfy (5b).

### **Case 2:&#x20;**\\(r=2\\)

Here

\\[ n-3=k-1. \\]

The auxiliary pencil has \\(p=1\\) identically zero row. After deleting it, the remaining pencil is square of size \\(k-1\\).

If the actual row space is \\(V=U^\perp\\) and \\(\operatorname{rank}H=k-1\\), then the leading coefficient of this square pencil has rank \\(k-1\\), hence is invertible. Thus

\\[ \det(\lambda X'-G') \\]

has degree exactly \\(k-1\\). Provided \\(k-1\ge1\\), it has a complex root, and the pencil loses rank there.

This proves infeasibility.

### **The two qualifications**

1. **The assumption&#x20;**\\(r\le2\\)**&#x20;is correct** because \\(p=1\\) and \\([C;CA]\\) has two rows.
2. **The invertibility of&#x20;**\\(X'\\)**&#x20;needs the rank condition** \\(\operatorname{rank}H=k-1\\), together with \\(V=U^\perp\\). It is not a consequence of the dimension comparison alone.

There is also a degenerate case \\(k=1\\), for which the required rank is \\(\omega=0\\). The usual hyperplane-pencil argument is then vacuous. Your intended pattern has \\(k=3\\), so this does not affect the result there.

### **A theorem you can safely state**

For the pattern

\\[ p=1,\qquad q=n-2,\qquad r_0=0, \\]

every admissible non-eigen point in the hyperplane layer is spectrally infeasible.

This includes the \\(n=5,p=1,q=3\\) case.

I would not yet state the unrestricted version for arbitrary \\(q\\) without a different argument using the actual observer pencil.

## **7. Claim 7 — the&#x20;**\\(\lambda=0\\)**&#x20;obstruction**

Correct

The rank identity is correct. Let

\\[ W=AK_0. \\]

Since \\(N\\) is a basis of \\(K_0\\),

\\[ \operatorname{im}(AN)=W. \\]

Therefore

\\[ \operatorname{rank}(LAN) = \dim L(W). \\]

By rank-nullity applied to the restriction \\(L|\_W\\),

\\[ \operatorname{rank}(LAN) = \dim W-\dim(W\cap\ker L). \\]

Since

\\[ \ker L=V^\perp, \\]

we get exactly

\\[ \boxed{ \operatorname{rank}H_A = \dim(AK_0)-\dim(AK_0\cap V^\perp). } \\]

Now every row of \\(L\\) annihilates \\(v\\), so

\\[ v\in V^\perp. \\]

If also \\(v\in AK_0\\), then

\\[ v\in AK_0\cap V^\perp, \\]

and hence

\\[ \boxed{ \operatorname{rank}H_A\le\dim(AK_0)-1. } \\]

No additional assumption is needed for this inequality.

The consequence for feasibility is particularly useful because (5b) at \\(\lambda=0\\) requires

\\[ \operatorname{rank}(-H_A)=\omega. \\]

Thus

\\[ \dim(AK_0)\ge\omega+1 \\]

is necessary whenever \\(v\in AK_0\\).

## **8. Claim 8 — nonzero eigenvalues and the case&#x20;**\\(v\notin AK_0\\)

Correct

If

\\[ Av=\lambda_0v,\qquad \lambda_0\ne0, \\]

then

\\[ v=A(v/\lambda_0)\in AK_0. \\]

Consequently, Claim 7 gives

\\[ \omega = \operatorname{rank}H_A \le \dim(AK_0)-1. \\]

So

\\[ \boxed{\dim(AK_0)\ge\omega+1=k.} \\]

In particular, if

\\[ \operatorname{rank}(A|\_{K_0})\<k, \\]

then no such eigen fibre can be feasible.

### **What replaces this condition when&#x20;**\\(v\notin AK_0\\)**?**

The exact necessary condition is obtained directly from the rank identity:

\\[ \operatorname{rank}H_A = \dim(AK_0)-\dim(AK_0\cap V^\perp). \\]

Since feasibility requires rank \\(\omega\\), we need

\\[ \boxed{ \dim(AK_0)-\dim(AK_0\cap V^\perp)=\omega. } \\]

In particular,

\\[ \boxed{\dim(AK_0)\ge\omega} \\]

is necessary, but not sufficient.

The distinction is:

- If \\(v\in AK_0\\), then the intersection \\(AK_0\cap V^\perp\\) is forced to be nonzero, giving the stronger lower bound \\(\dim(AK_0)\ge\omega+1\\).
- If \\(v\notin AK_0\\), there is no such forced intersection. The weaker bound \\(\dim(AK_0)\ge\omega\\) is all that follows from this argument alone.

There may still be other vectors in \\(AK_0\cap V^\perp\\), so even when \\(v\notin AK_0\\), the dimension condition alone does not guarantee that \\(\operatorname{rank}H_A=\omega\\).

## **9. Claim 9 — the eigen-fibre sufficiency conjecture is refuted**

Valid structural counterexample

This is an important result. The argument is not merely supported by the 20 random samples; the failure follows for every admissible row space in the indicated fibre.

Let

\\[ v=e_1,\qquad Av=2e_1. \\]

Then

\\[ U=\operatorname{span}(e_1),\qquad U^\perp=e_1^\perp. \\]

Every admissible observer row space in this fibre satisfies

\\[ V\subseteq e_1^\perp, \\]

so

\\[ e_1\in V^\perp. \\]

You have

\\[ K_0 = \operatorname{span}\\{e_1,w,e_4\\}, \qquad w=(0,2,1,0,0)^\top. \\]

Direct calculation gives

\\[ Ae_1=2e_1,\qquad Aw=(3,-3,0,0,0)^\top,\qquad Ae_4=0. \\]

Therefore

\\[ AK_0 = \operatorname{span} \left\\{ (2,0,0,0,0)^\top,\\, (3,-3,0,0,0)^\top \right\\} \\]

and

\\[ \dim(AK_0)=2=\omega. \\]

Moreover,

\\[ e_1\in AK_0\cap V^\perp. \\]

Consequently,

\\[ \operatorname{rank}H_A = 2-\dim(AK_0\cap V^\perp) \le1<2. \\]

Thus (5b) fails at \\(\lambda=0\\), for every admissible row space in this fibre.

There is no escape through another point of \\(E_2\\): in the given \\(K_0\\), the eigenspace for eigenvalue \\(2\\) is exactly \\(\operatorname{span}\\{e_1\\}\\). Indeed, for

\\[ x=ae_1+bw+ce_4, \\]

the equation \\(Ax=2x\\) forces \\(b=c=0\\).

Therefore the entire eigen fibre over \\(E_2\\) is infeasible.

**Conclusion:** the conjecture

\\[ K_0\text{ contains an eigenvector} \quad\Longrightarrow\quad \text{the hyperplane layer is feasible} \\]

is false.

This counterexample should be promoted to a proposition, with the structural rank argument as its proof. It also shows that the eigenvector criterion cannot be repaired simply by restricting attention to nonzero eigenvalues: the obstruction is the dimension of \\(AK_0\\) and its intersection with \\(V^\perp\\).

## **10. Claim 10 — moving roots and fixed roots**

The two observations are mathematically meaningful, but they have different levels of evidential strength.

### **10.1 Moving roots**

Your ten sampled non-eigen points, with eight distinct quadratic root sets, show that the badness of all sampled points need not be explained by one fixed spectral value.

That is useful evidence against a proposed criterion of the form:

> There exists one fixed \\(\lambda_0\\) at which every point in the family loses rank.

But ten points do not prove that the entire family is bad, nor do they prove that no fixed root exists elsewhere in the family.

There is a clean algebraic way to turn this into a theorem.

Let \\(Y\\) be an irreducible parameter space and let

\\[ m_I(y,\lambda) \\]

be the maximal minors. Define

\\[ g_Y(\lambda)=\gcd_I m_I(y,\lambda) \quad\text{in }\overline{\mathbb Q(Y)}[\lambda]. \\]

Then:

- If \\(g_Y=1\\), the generic point of \\(Y\\) is good.
- If \\(g_Y\\) has positive degree, the generic point of \\(Y\\) is bad.
- If\
  \\[\
  g_Y(\lambda)=\lambda-\lambda_0\
  \\]\
  for a constant \\(\lambda_0\\), the generic badness is explained by a fixed root.
- If \\(g_Y\\) has positive degree but no constant linear factor over the ground field, then the generic badness is not explained by that fixed-root mechanism.

For example, a factor such as

\\[ \lambda^2-t \\]

describes roots that move with the parameter \\(t\\). It is a genuine algebraic moving-root obstruction.

This suggests a much sharper statement than “all sampled points are bad”:

> The generic pencil on the parameter component has a nonconstant common spectral factor.

That is an exact symbolic certificate, not a sampling observation.

### **10.2 Fixed root at&#x20;**\\(-2\\)

The second observation is more directly structural. If the gcd of all maximal minors is

\\[ \lambda+2, \\]

then \\(\lambda=-2\\) is a common rank-drop value for every point of the parameter family, at least wherever the specialization is defined.

This is exactly the sort of obstruction that a symbolic gcd detects.

However, a finite sample with no good point is not enough to prove that the whole family has this factor. The report says that the inspected instance has the symbolic identity \\(\gcd\equiv\lambda+2\\); if that identity is established over the parameter function field, it is a proof of generic badness on that family.

**Conclusion:** fixed-root checking alone is not a criterion. The right object is the generic gcd over the function field of each irreducible parameter component.

## **11. Claim 11 — excess regime and generic goodness**

This is the most interesting positive direction, but the current argument is not sufficient to prove the desired result.

Let

\\[ m=n-2-p,\qquad \omega=k-1=n-r-1. \\]

Then

\\[ m-\omega=r-p-1. \\]

So in the excess regime \\(r>p+1\\), the reduced auxiliary pencil has more rows than columns.

### **11.1 The unrestricted tall-pencil theorem**

There is a useful general fact.

Consider an unrestricted pencil

\\[ P(\lambda)=\lambda X-G \in\mathbb C[\lambda]^{m\times\omega}, \qquad m>\omega, \\]

where \\(X\\) has full column rank.

For a fixed \\(\lambda\\), the condition

\\[ \operatorname{rank}P(\lambda)<\omega \\]

has codimension

\\[ m-\omega+1 \\]

in the space of all \\(m\times\omega\\) matrices.

Allowing \\(\lambda\\) to vary over \\(\mathbb P^1\\) adds one parameter. Thus the incidence variety of pencils with a rank drop somewhere has codimension at least

\\[ m-\omega. \\]

Since \\(m>\omega\\), this codimension is positive.

Therefore a generic unrestricted tall pencil with full-column-rank leading coefficient has full column rank for every \\(\lambda\in\mathbb C\\).

This confirms your intuition: **tall pencils are generically good in the unrestricted coefficient space.**

### **11.2 Why this does not yet prove Claim 11**

The pencils arising from your observer construction are not unrestricted.

Their rows are generated by

\\[ r\longmapsto \bigl(rN,\ rAN\bigr), \qquad r\in U^\perp, \\]

and the selected row space must also satisfy

\\[ \dim(V\cap K_0)=k-1. \\]

Thus the actual family of pairs \\((H,H_A)\\) is a structured subvariety of the space of all pairs of matrices. It might lie entirely inside the bad-pencil locus even when the unrestricted bad-pencil locus has positive codimension.

The calculation in Claim 11 itself illustrates this danger: the family with \\(AK_0\subseteq K_0\\) has a structural factor and is entirely bad in the tested configuration, despite being in the excess regime.

So the unrestricted dimension count is not enough. You need to show that the structured family is not contained in the bad-pencil variety.

### **11.3 The cleanest route to a proof**

For a fixed non-eigen base point \\(v\\), define the linear map

\\[ \Phi_v:U(v)^\perp\longrightarrow \mathbb Q^{1\times k}\times\mathbb Q^{1\times k}, \qquad r\longmapsto(rN,rAN). \\]

The observer pencil is obtained by selecting \\(q\\) rows from the image of \\(\Phi_v\\), subject to the required intersection-rank conditions.

The proof should proceed in three steps.

**Step 1: Parameterize the admissible row spaces.**

Construct the relevant Grassmannian stratum

\\[ \mathfrak G_v = \left\\{ V\in\operatorname{Gr}(q,U(v)^\perp): \dim(V\cap K_0)=k-1 \right\\}, \\]

with any additional conditions arising from \\(L_0\\).

You need to establish that the desired rank stratum is nonempty and irreducible, or decompose it into irreducible pieces if it is not.

**Step 2: Pull back the bad-pencil variety.**

Let \\(\mathfrak D\\) be the algebraic locus of pencils whose maximal minors have a common root. The family is generically good exactly when

\\[ \Phi_v(\mathfrak G_v)\not\subseteq\mathfrak D, \\]

with \\(\Phi_v\\) interpreted as the induced map on row spaces.

Equivalently, you need one admissible row space \\(V\_\*\\) such that

\\[ \gcd_I m_I(V\_\*;\lambda)=1. \\]

Once one such point exists, the good set is a nonempty Zariski-open subset of the irreducible parameter stratum.

**Step 3: Prove non-containment structurally.**

This is the missing mathematical step. It may follow from a sufficiently strong controllability/observability condition on the induced quotient pair, but it will not follow from \\(r>p+1\\) alone.

A natural candidate is a condition ensuring that the induced family of pairs \\((H,H_A)\\) is sufficiently rich to avoid the resultant locus. For example, surjectivity of an appropriate induced coefficient map would reduce the problem to the unrestricted tall-pencil theorem. But you must prove that surjectivity from the original \\(A,C,K_0\\) geometry; it cannot be assumed.

### **11.4 What you can claim now**

The safe statement is:

> In the excess regime \\(r>p+1\\), the reduced auxiliary pencil is tall. An unrestricted generic pencil of this size is spectrally full-column-rank. In the observer problem, however, the pencil coefficients are structurally coupled, and generic feasibility requires proving that the structured family is not contained in the bad-pencil locus.

That is a useful theorem-plus-open-problem formulation. I would not state “excess implies generically good” yet.

# **12. A revised theorem package**

I recommend organizing the results into the following statements.

## **Theorem A — closed bad locus and generic criterion**

Let \\(Y\\) be an irreducible parameter variety on which \\(\operatorname{rank}H=\omega\\) is constant. Then the bad locus

\\[ \mathcal B = \\{y\in Y:\exists\lambda\in\mathbb C,\ \operatorname{rank}(\lambda H(y)-H_A(y))<\omega\\} \\]

is closed in \\(Y\\).

Consequently,

\\[ Y\setminus\mathcal B\ne\varnothing \iff \gcd_I m_I=1 \quad\text{in }\overline{\mathbb Q(Y)}[\lambda]. \\]

This is Claims 2–3.

## **Theorem B — non-eigen infeasibility in the&#x20;**\\(p=1\\)**, full-row-space pattern**

Assume

\\[ p=1,\qquad q=n-2,\qquad r_0=0, \\]

and consider an admissible non-eigen point in the hyperplane layer

\\[ \omega=k-1. \\]

Then the observer row space satisfies

\\[ V=U^\perp. \\]

The reduced pencil has either fewer rows than columns, or is square with invertible leading coefficient. In either case, (5b) fails.

This is the corrected version of Claim 6. It is especially useful because it is uniform in \\(A\\).

## **Proposition C — zero-frequency obstruction**

For any admissible \\(V\\) and \\(v\\) in the hyperplane layer,

\\[ \operatorname{rank}H_A = \dim(AK_0)-\dim(AK_0\cap V^\perp). \\]

If \\(v\in AK_0\\), then

\\[ \operatorname{rank}H_A\le\dim(AK_0)-1. \\]

In particular, if \\(v\\) is an eigenvector with nonzero eigenvalue, feasibility requires

\\[ \dim(AK_0)\ge k. \\]

This is Claims 7–8.

## **Proposition D — eigen-fibre sufficiency fails**

The matrix in Claim 9 has a nonempty eigen fibre but no feasible row space in that fibre, because every admissible row space has

\\[ \operatorname{rank}H_A<\omega. \\]

This is a clean counterexample to the eigenvector-sufficiency conjecture.

# **13. What is the correct criterion for eigen fibres?**

The results now point to a better criterion than the existence of an eigenvector.

Fix an eigenvector \\(v\\) with eigenvalue \\(\lambda_0\\), and let

\\[ U=\operatorname{span}(v),\qquad U^\perp=v^\perp. \\]

The admissible row spaces satisfy

\\[ V\subseteq v^\perp,\qquad \dim(V\cap K_0)=k-1, \\]

along with the prescribed \\(L_0\\)-constraints.

For each such \\(V\\), the spectral condition is

\\[ \operatorname{rank}\bigl(L(\lambda I-A)N\bigr)=k-1 \quad\forall\lambda\in\mathbb C. \\]

There are two levels of obstruction.

### **Level 1: zero-frequency rank**

A necessary condition is

\\[ \dim(AK_0)-\dim(AK_0\cap V^\perp)=k-1. \\]

This is an exact linear-algebraic condition on \\(V\\). It is stronger and more informative than merely requiring an eigenvector in \\(K_0\\).

### **Level 2: common spectral roots**

Even if the zero-frequency condition holds, there may be a nonzero common root. For a parameter component \\(Y\\) of the admissible eigen-fibre row spaces, the exact complex-geometric criterion is

\\[ \boxed{ \gcd_I m_I=1 \quad\text{in }\overline{\mathbb Q(Y)}[\lambda]. } \\]

This gives a conceptually complete criterion, but not yet an efficient algorithm. The hard part is describing the irreducible components \\(Y\\), computing the generic gcd, and dealing with rational points.

In other words, the eigen-fibre problem has become:

1. Find the admissible row-space strata satisfying the \\(\lambda=0\\) rank condition.
2. Determine whether any such stratum has generic gcd equal to one.
3. If rational synthesis is required, establish a rational point in the good open subset.

That is the natural next theorem target.

# **14. Recommended next research steps**

I would prioritize the following work.

1. **Repair Claim 1.** Make the row-space incidence variety and its Grassmannian strata explicit. Do not rely on fibre-dimension comparison alone. This is important if you want to use componentwise generic-gcd tests.
2. **Promote Theorem B.** State and prove the \\(p=1,q=n-2\\) non-eigen obstruction cleanly. It is now a strong, uniform result.
3. **Promote Claim 9.** It is a genuine structural counterexample and eliminates the simple eigenvector criterion.
4. **Use Claim 7 as a preprocessing test.** On each eigen fibre, compute \\(AK_0\\) and determine whether the zero-frequency rank condition can be met. If it cannot, discard the fibre immediately.
5. **Investigate Claim 11 through the structured coefficient map.** The main task is not to prove that generic tall pencils are good; that part is standard. The task is to prove that your structured family can actually reach one.
6. **Replace sampling with generic gcd certificates.** For each irreducible parameter family, calculate the gcd in its function field. This distinguishes fixed-root obstructions from genuinely moving-root obstructions.

The most valuable new insight in this report is arguably Claim 9, not Claim 11. It changes the eigen-fibre problem from “does \\(K_0\\) contain an eigenvector?” to “does an admissible row-space stratum survive both the zero-frequency rank test and the full generic spectral test?”

That is a substantially more accurate formulation of the remaining problem.