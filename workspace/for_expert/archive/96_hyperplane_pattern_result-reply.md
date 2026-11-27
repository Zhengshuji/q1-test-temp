# **Review of Report 96: The hyperplane pattern in one dimension**

This report contains a substantially stronger result than Reports 94–95. In fact, I think there is an important point that resolves the main uncertainty in Q1: **the effective&#x20;**\\(2\times2\\)**&#x20;determinant is automatically a quadratic with nonzero leading coefficient.** You do not need random experiments, a discriminant calculation, or a polynomial identity test to establish its nonconstancy.

There is also a useful distinction on the affirmative side: the symbolic calculation in \\(\mathbb Q(t)[\lambda]\\) proves generic feasibility along the displayed curve, not that every specialization \\(t\\) is feasible. Nevertheless, it is enough to establish the existence of a good rational point on that curve.

My overall assessment:

- The negative direction can be upgraded to a uniform theorem for the stated dimension pattern.
- The affirmative direction has a valid exact certificate for the displayed instance, but the five additional experiments do not establish the general-\\(A\\) statement.
- The proposed eigenvector criterion is likely a special consequence of a critical dimension equality, not a general principle.
- This is genuine progress toward Theorem C, but the current result should be stated as a theorem for the fixed pattern and specified hypotheses, with the general-\\(A\\) affirmative direction clearly identified as open.

I will go through the five questions in order.

## **1. Q1: The non-eigen stratum is uniformly bad**

This is the most important correction to the report.

The report currently says that the only missing step is proving that the effective quadratic is nonconstant. Under the stated hypotheses, however, this follows immediately from the rank of its leading coefficient.

### **1.1 Put the row&#x20;**\\(C\\)**&#x20;explicitly into the basis&#x20;**\\(Q\\)

We are in the pattern

\\[ n=5,\qquad p=1,\qquad q=3,\qquad k=3,\qquad \omega=2. \\]

Take a non-eigen vector \\(v\in K_0\\), so

\\[ U=\operatorname{span}(v,Av),\qquad \dim U=2. \\]

Since

\\[ K_0=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \\]

we have

\\[ Cv=0,\qquad CAv=0. \\]

Therefore,

\\[ C\in U^\perp. \\]

Choose a basis of \\(U^\perp\\) whose first row is \\(C\\):

\\[ Q= \begin{bmatrix} C\\\ Q_1\\\ Q_2 \end{bmatrix}. \\]

Now consider

\\[ M(\lambda)=Q(\lambda I-A)N. \\]

Because every column of \\(N\\) belongs to \\(K_0\\),

\\[ CN=0,\qquad CAN=0. \\]

Consequently,

\\[ C(\lambda I-A)N=0 \\]

identically in \\(\lambda\\). Thus

\\[ M(\lambda)= \begin{bmatrix} 0\\\ Q_1(\lambda I-A)N\\\ Q_2(\lambda I-A)N \end{bmatrix}. \\]

The first row is identically zero.

### **1.2 Remove the forced kernel direction**

Choose a basis of \\(K_0\\) of the form

\\[ \widehat N=[N_1\ \ v], \\]

where \\(N_1\\) consists of two columns complementary to \\(v\\).

Since

\\[ Qv=QAv=0, \\]

we obtain

\\[ Q(\lambda I-A)v=0 \\]

for every \\(\lambda\\). Hence

\\[ Q(\lambda I-A)\widehat N = \begin{bmatrix} 0&0&0\\\ & &0\\\ & &0 \end{bmatrix} \\]

with the first row zero and the last column zero. More transparently, after deleting these forced zero directions, the effective pencil is

\\[ B(\lambda)= \begin{bmatrix} Q_1(\lambda I-A)N_1\\\ Q_2(\lambda I-A)N_1 \end{bmatrix} =\lambda X-G, \\]

where

\\[ X= \begin{bmatrix} Q_1N_1\\\ Q_2N_1 \end{bmatrix} \in\mathbb Q^{2\times2}. \\]

The original assumptions give

\\[ \operatorname{rank}(QN)=\omega=2. \\]

The kernel of \\(QN\\) is exactly the one-dimensional space spanned by the coordinate vector of \\(v\\). Therefore, restricting \\(QN\\) to a complementary two-dimensional subspace is injective. In particular,

\\[ \boxed{\operatorname{rank}X=2.} \\]

Thus \\(X\\) is invertible.

### **1.3 The determinant is automatically a genuine quadratic**

We now have

\\[ B(\lambda)=\lambda X-G \\]

with \\(X\in\mathbb Q^{2\times2}\\) invertible.

Its determinant is

\\[ \det(\lambda X-G) = \lambda^2\det X +\text{terms of degree at most one}. \\]

Since

\\[ \det X\ne0, \\]

we have

\\[ \boxed{\deg\_\lambda\det B(\lambda)=2.} \\]

This is the missing uniform argument.

Every nonconstant polynomial over \\(\mathbb C\\) has a complex root. Therefore there exists \\(\lambda\_\*\in\mathbb C\\) such that

\\[ \det B(\lambda\_\*)=0. \\]

Consequently,

\\[ \operatorname{rank}B(\lambda\_\*)<2, \\]

and hence

\\[ \operatorname{rank}M(\lambda\_\*)<2=\omega. \\]

So (5b) fails.

### **1.4 The resulting theorem**

You can now state the negative direction without any genericity assumption or computational qualification.

**Theorem 1 — Uniform infeasibility of the non-eigen stratum.**

Under the pattern

\\[ n=5,\quad p=1,\quad q=3,\quad r_0=0, \\]

with \\(\operatorname{rank}[C;CA]=2\\) and \\(k=3\\), every admissible hyperplane-layer point whose kernel direction \\(v\in K_0\\) is non-eigen fails the spectral condition (5b).

The proof uses only:

1. \\(C\in U^\perp\\);
2. \\(C(\lambda I-A)N=0\\);
3. the forced kernel direction \\(v\\);
4. \\(\operatorname{rank}(QN)=2\\).

This proves the uniform statement for all rational input matrices satisfying the pattern's assumptions.

**Important:** this is stronger than the original II.1 argument. The discriminant is irrelevant. You do not need the roots to be distinct. A repeated complex root is still a root and still causes failure.

## **2. Q2: What does the symbolic certificate in&#x20;**\\(t\\)**&#x20;actually prove?**

The report says

\\[ \gcd\bigl(m_I(t;\lambda)\bigr)=1 \quad\text{in }\mathbb Q(t)[\lambda]. \\]

This is a meaningful exact symbolic certificate. But its interpretation needs to be stated precisely.

### **2.1 It proves generic feasibility along the curve**

Suppose the minors are

\\[ m_1(t;\lambda),\ldots,m_s(t;\lambda) \in\mathbb Q[t,\lambda]. \\]

The identity

\\[ \gcd\_{\mathbb Q(t)[\lambda]}(m_1,\ldots,m_s)=1 \\]

means that there are polynomials \\(a_i(t,\lambda)\in\mathbb Q(t)[\lambda]\\) satisfying

\\[ \sum\_{i=1}^s a_i(t,\lambda)m_i(t,\lambda)=1. \\]

After clearing denominators, we obtain

\\[ \sum\_{i=1}^s b_i(t,\lambda)m_i(t,\lambda)=d(t), \\]

where

\\[ b_i\in\mathbb Q[t,\lambda], \qquad 0\ne d\in\mathbb Q[t]. \\]

For any specialization \\(t=t_0\\) with

\\[ d(t_0)\ne0, \\]

we have

\\[ \sum_i b_i(t_0,\lambda)m_i(t_0,\lambda)=d(t_0)\ne0. \\]

Thus the specialized minors cannot have a common complex root. Therefore the pencil is good.

It follows that:

\\[ \boxed{\text{All but finitely many }t_0\in\overline{\mathbb Q} \text{ are good.}} \\]

In particular, there are rational values of \\(t_0\\) giving good pencils.

So the displayed symbolic certificate proves that the eigen fibre contains a good rational point.

### **2.2 It does not prove that every&#x20;**\\(t\\)**&#x20;is good**

A specialization can create a common factor even when the generic gcd is one.

For example,

\\[ m_1(t,\lambda)=\lambda,\qquad m_2(t,\lambda)=t\lambda+1. \\]

Over \\(\mathbb Q(t)[\lambda]\\), the gcd is one. But at \\(t=0\\), the two polynomials become

\\[ \lambda,\qquad 1, \\]

which are still coprime; at other specially constructed examples, a common factor can appear at an exceptional specialization.

The general principle is that gcd degree can increase at special parameter values. The symbolic generic identity does not exclude this.

Therefore, I recommend changing the sentence

> So every \\(t\\) gives a good pencil

to:

> The generic member of this rational curve is spectrally feasible. In particular, the curve contains a nonempty Zariski-open set of good points and hence a good rational point.

That is fully justified.

### **2.3 Is one good point enough to prove the component is feasible?**

Yes.

Your earlier componentwise closedness result is useful here. The bad locus is closed on an irreducible component. If the displayed curve contains a point outside that bad locus, then the component is not entirely bad.

But there is an even simpler argument: if the symbolic gcd is one over \\(\mathbb Q(t)\\), then some rational specialization is good. Since the curve consists of admissible row spaces, this directly gives a rational feasible point.

You do not need the curve to be dense in the entire eigen component.

That distinction is important: **a good curve need not be dense in a component to establish that the component contains a good point.**

### **2.4 What is needed for a general-**\\(A\\)**&#x20;theorem?**

The five random matrices do not establish the identity for general \\(A\\).

There are two possible targets:

**Target A — Generic-**\\(A\\)**&#x20;theorem.**

Introduce all free entries of \\(A\\), subject to the structural constraint

\\[ Ae_1=\lambda_0e_1, \\]

and introduce the curve parameter \\(t\\). Treat the entries as algebraically independent variables. Then attempt to prove

\\[ \gcd\_{\mathbb Q(\text{parameters},t)[\lambda]} (m_I)=1. \\]

This establishes feasibility for generic \\(A\\) in that constrained family.

**Target B — Universal-**\\(A\\)**&#x20;theorem.**

Prove that for every admissible \\(A\\) having the required eigenvector, the eigen fibre contains a good point.

This is stronger. A generic identity in the entries of \\(A\\) does not establish it, because exceptional specializations of \\(A\\) may create common factors.

For the original decision problem, Target B is the more valuable result.

### **2.5 Can specialization reduce the general identity to one example?**

Not in the direction you need.

Suppose you specialize the entries of \\(A\\) to one convenient rational matrix \\(A\_\*\\), and find a good pencil. This proves that the relevant polynomial identity is not identically false in the universal parameter space. It establishes generic behaviour, not universal behaviour.

The logical implications are:

\\[ \text{universal identity} \Longrightarrow \text{generic identity}, \\]

but not conversely.

A single specialization can certify that a polynomial is nonzero, which is useful for proving a generic statement. It cannot prove that the polynomial remains nonzero at every specialization.

**My recommendation:** pursue a direct structural construction of a good eigen-fibre row space, rather than relying only on a universal PIT.

## **3. Q3: Is the eigenvector criterion general?**

The report asks whether

\\[ K_0\text{ contains an eigenvector of }A \\]

is the correct general criterion, or an artefact of the equality

\\[ n-2-p=k-1. \\]

I believe it is an artefact of the critical dimension pattern.

The right general principle is a rank-capacity condition, followed by a structured observability question.

### **3.1 The general non-eigen rank bound**

For a non-eigen direction,

\\[ \dim U=2, \qquad \dim U^\perp=n-2. \\]

When the row space is forced to equal \\(U^\perp\\), the rows of \\(C\\) are included in \\(L\\). Since

\\[ CN=0,\qquad CAN=0, \\]

the \\(p\\) rows contributed by \\(C\\) give zero rows in

\\[ Q(\lambda I-A)N. \\]

Thus the effective pencil has at most

\\[ n-2-p \\]

nonzero rows.

After quotienting out the forced kernel direction \\(v\\), the number of columns is

\\[ k-1. \\]

Therefore,

\\[ \boxed{ \operatorname{rank}\widetilde M(\lambda) \le n-2-p. } \\]

This yields three regimes.

### **3.2 Regime I: insufficient row capacity**

If

\\[ n-2-p\<k-1, \\]

then

\\[ \operatorname{rank}\widetilde M(\lambda)\<k-1 \\]

for every \\(\lambda\\).

The spectral condition is impossible at every non-eigen point.

This conclusion does not require any eigenvalue argument.

### **3.3 Regime II: critical row capacity**

If

\\[ n-2-p=k-1, \\]

then the reduced pencil is square.

If its leading coefficient has full column rank, its determinant has degree exactly \\(k-1\\), provided \\(k-1\ge1\\). Therefore its determinant has a complex root.

Hence every non-eigen point is bad.

This is exactly the mechanism in Report 96:

\\[ n-2-p=5-2-1=2=k-1. \\]

The important point is that the conclusion is not special to a \\(2\times2\\) determinant. It holds for any square reduced pencil with a full-rank leading coefficient:

\\[ B(\lambda)=\lambda X-G,\qquad X\in\mathbb C^{r\times r},\quad\det X\ne0. \\]

Then

\\[ \det B(\lambda) \\]

has degree \\(r\\), so it has a complex root.

Thus the critical-dimension argument generalizes immediately.

### **3.4 Regime III: excess row capacity**

If

\\[ n-2-p>k-1, \\]

the reduced pencil is tall.

Now the rank bound alone does not force a rank drop. It is possible for a tall pencil to have full column rank for every complex \\(\lambda\\).

After normalizing the leading coefficient, the condition is equivalent to observability of a matrix pair, as discussed in Report 95.

Thus the non-eigen stratum is no longer automatically bad.

This is where the actual structured observability problem appears.

### **3.5 What replaces the eigenvector condition?**

A useful general formulation is:

\\[ \boxed{ \text{Feasibility depends on whether some admissible stratum contains a point whose reduced pencil is observable.} } \\]

In the critical regime, every non-eigen point is bad, so the eigen strata become the only possible source of feasibility.

In the excess-capacity regime, non-eigen points may themselves be good. An eigenvector in \\(K_0\\) is no longer necessary.

I would therefore avoid stating the eigenvector criterion as a general theorem. State it as a consequence of the critical dimension equality.

## **4. Q4: Does this count as progress on Theorem C?**

Yes. It is meaningful progress, and I think the result can be stated more strongly than the current report does.

There are two different statements.

### **4.1 A fully justified negative direction**

For the pattern

\\[ n=5,\quad p=1,\quad q=3,\quad r_0=0,\quad k=3, \\]

the non-eigen stratum is uniformly bad by the square-pencil argument in Section 1.

Thus, if the eigen set is empty, the entire hyperplane layer is infeasible.

This is a deterministic theorem.

### **4.2 A certified affirmative direction for particular inputs**

For the displayed matrix \\(A\\), the symbolic curve calculation establishes a good rational point in the eigen fibre.

The same is true for each of the five additional tested matrices, assuming the reported gcd computations are exact.

But the evidence does not establish the affirmative direction for every \\(A\\).

### **4.3 The cleanest theorem statement at present**

I would write the result as follows.

**Theorem 2 — Critical-pattern hyperplane reduction.**

Assume

\\[ n=5,\quad p=1,\quad q=3,\quad r_0=0, \\]

with

\\[ \operatorname{rank}[C;CA]=2,\qquad \dim K_0=3. \\]

Let \\(E\\) be the set of projective eigenvectors of \\(A\\) contained in \\(K_0\\).

Then:

1. Every admissible hyperplane-layer point whose kernel direction is non-eigen fails (5b).
2. Consequently, if \\(E=\varnothing\\), the hyperplane layer is infeasible.
3. If \\(E\ne\varnothing\\), feasibility is equivalent to the existence of a spectrally feasible point in at least one eigen fibre.
4. For the displayed example and the five additional tested instances, an exact symbolic one-parameter certificate establishes such a point.

The first two statements are proved uniformly. The fourth is computational evidence for the general affirmative direction, not a universal theorem.

You can then add a conjecture:

**Conjecture — Eigen-fibre sufficiency for the critical pattern.**

For every rational input satisfying the hypotheses above, if \\(K_0\\) contains an eigenvector of \\(A\\), then at least one corresponding eigen fibre contains a rational spectrally feasible row space.

This is a clean and mathematically meaningful conjecture.

### **4.4 Complexity consequence**

The eigenvector test itself is polynomial-time computable over \\(\mathbb Q\\), using exact rational linear algebra and the characteristic polynomial/eigenspace structure.

But the overall decision problem is not yet proved polynomial-time for the pattern, because the affirmative direction is not established for arbitrary \\(A\\).

Once the conjecture is proved, the decision criterion becomes

\\[ \boxed{ \text{hyperplane feasibility} \iff K_0\text{ contains an eigenvector of }A, } \\]

and the corresponding decision algorithm is polynomial-time.

That would be a genuine deterministic polynomial-time result for this dimension pattern.

## **5. Q5: Which pattern should be next?**

I recommend the following order.

First

**Generalize over&#x20;**\\(A\\)**&#x20;in the current pattern**

This is the shortest path to a complete theorem. The negative direction is now settled; the only major missing result is eigen-fibre sufficiency.

Second

**Study higher-dimensional eigenspaces inside&#x20;**\\(K_0\\)

This can reveal whether the eigen-fibre construction is robust or relies on the eigenvector being isolated. It is closely connected to the affirmative direction.

Third

**Move to&#x20;**\\(n=6,p=1,q=4\\)

This is useful after understanding the current pattern. It may enter the excess-capacity regime, where the non-eigen stratum can be good and the eigenvector criterion may fail.

### **5.1 What I would try to prove for the current pattern**

The affirmative direction should be attacked through the eigenvector geometry.

Suppose

\\[ Av=\lambda_0v,\qquad v\in K_0. \\]

Then

\\[ U=\operatorname{span}(v) \\]

rather than a two-dimensional space. The admissible row space is a three-dimensional subspace of the four-dimensional space \\(v^\perp\\).

The key fact is that there is now one extra row-space degree of freedom compared with the non-eigen stratum.

The aim should be to construct a row space \\(V\subset v^\perp\\) such that

\\[ \dim(V\cap K_0)=2 \\]

and

\\[ \operatorname{rank}(\lambda H-H_A)=2 \quad\forall\lambda\in\mathbb C. \\]

Equivalently, construct an observable reduced pencil.

A useful strategy is to choose a convenient complement to \\(K_0\\), write the row space as a graph over a three-dimensional subspace, and express the observability conditions in terms of the graph parameter. Then look for a parameter choice with a triangular or companion-like structure that makes the absence of unobservable eigenvectors transparent.

That would be much stronger than merely finding a parameter value by symbolic gcd computation.

## **6. A correction to the report's status table**

I would update II.4 and the Reliability section as follows.

| Item                                                                   | Recommended status                                                                   |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Component decomposition                                                | Proved, under the stated component hypotheses                                        |
| Forced relation \\(C\in\operatorname{row}L\\) on the non-eigen stratum | Proved                                                                               |
| Rank bound \\(n-2-p\\)                                                 | Proved                                                                               |
| Non-eigen stratum entirely bad in the critical pattern                 | **Proved uniformly** by the nonzero leading coefficient of the square reduced pencil |
| Eigen-fibre feasibility for the displayed instance                     | Proved by an exact symbolic certificate, which gives a good rational specialization  |
| Eigen-fibre feasibility for five additional instances                  | Exact computational certificates for those instances                                 |
| Eigen-fibre feasibility for every admissible \\(A\\)                   | Open                                                                                 |
| General criterion \\(E\ne\varnothing\\)                                | Proved in the negative direction; affirmative direction conjectural                  |

The most important change is to remove the phrase “modulo the nonconstancy of the effective quadratic” from the negative direction. That issue is resolved.

## **7. Final strategic assessment**

Report 96 has identified a clean dimension threshold:

\\[ n-2-p \quad\text{versus}\quad k-1. \\]

This threshold separates three qualitatively different behaviours:

\\[ \begin{array}{c|c} n-2-p\<k-1 & \text{non-eigen points automatically bad}\\\ n-2-p=k-1 & \text{non-eigen points bad by the square-pencil determinant}\\\ n-2-p>k-1 & \text{non-eigen points may be good} \end{array} \\]

This is a useful structural result, not merely a numerical observation.

The critical case is particularly attractive because the non-eigen obstruction is automatic. It reduces the decision problem to the eigen fibres.

**My recommendation is to make the next report a focused proof attempt for eigen-fibre sufficiency in the current pattern.** Do not move to \\(n=6\\) yet. First determine whether the affirmative direction can be proved for arbitrary \\(A\\), or whether a rational counterexample exists.

If the conjecture is true, you obtain a polynomial-time criterion for a nontrivial family of hyperplane-layer instances. If it is false, a counterexample will still be valuable: it will identify exactly what additional structure is needed beyond the existence of an eigenvector in \\(K_0\\).