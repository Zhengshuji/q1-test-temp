# Research review of Report 72: The conditional multiplication gate and the anchored-block problem

## 1. Executive assessment

Report 72 makes an important correction to the previous multiplication-gate analysis. In particular, it correctly identifies the conditional nature of the determinant identity, the failure of generic pencil coprimality to imply universal feasibility, and the existence of genuine boundary witnesses.

However, there is a more fundamental issue that has not yet been resolved in the report:



Critical issue

&#x20;The matrix \\(M\\) used to derive the determinant identity does not contain all the rows required by the original observer condition (5a).



For \\(L=[L_0;l]\\), condition (5a) is

\\[ \operatorname{rank} \begin{bmatrix} L_0A\\\ lA\\\ L_0\\\ l\\\ CA\\\ C \end{bmatrix} = \operatorname{rank} \begin{bmatrix} L_0\\\ l\\\ CA\\\ C \end{bmatrix}. \tag{1} \\]

But Report 72 defines

\\[ M= \begin{bmatrix} lA\\\ L_0\\\ l\\\ CA\\\ C \end{bmatrix}, \qquad M_0= \begin{bmatrix} L_0\\\ l\\\ CA\\\ C \end{bmatrix}. \tag{2} \\]

The row \\(L_0A\\) is missing from \\(M\\).

This is not a cosmetic omission. It changes the feasible set, and in this particular example it destroys the proposed multiplication gate entirely when the actual observer condition is imposed.

The determinant identity

\\[ \det M=ad-bc \\]

is correct for the matrix \\(M\\) defined in the report. But it only tests whether the additional row \\(lA\\) belongs to the row space of \\(M_0\\). It does not test whether both rows \\(L_0A\\) and \\(lA\\) belong to that row space.

I will first establish this correction exactly, then discuss the four questions and recommend a revised research direction.

## 2. The fundamental correction: the full \\((5a)\\) condition

The report uses

\\[ A=\begin{bmatrix} 1&1&-1&0&1\\\ -1&0&0&-1&1\\\ 0&1&-1&0&1\\\ 0&0&0&-1&0\\\ -1&1&0&0&0 \end{bmatrix}, \qquad C=e_5^\*, \qquad L_0=e_1^\*, \\]

and

\\[ L=\begin{bmatrix}e_1^\*\\\l\end{bmatrix}, \qquad l=(a,b,c,d,e). \\]

The original condition is

\\[ \operatorname{row}(LA) \subseteq \operatorname{row}[L;CA;C]. \\]

Since

\\[ LA= \begin{bmatrix} L_0A\\\ lA \end{bmatrix}, \\]

this means that both \\(L_0A\\) and \\(lA\\) must belong to the denominator row space.

### 2.1 Compute the fixed rows

We have

\\[ L_0=e_1^\*=(1,0,0,0,0), \\]

\\[ L_0A=(1,1,-1,0,1), \\]

\\[ C=e_5^\*=(0,0,0,0,1), \\]

and

\\[ CA=(-1,1,0,0,0). \\]

Let

\\[ S=\operatorname{row}[L_0;CA;C]. \\]

Then

\\[ S=\operatorname{span}\\{e_1^\*,e_2^\*,e_5^\*\\}. \\]

In particular,

\\[ \dim S=3. \\]

The quotient of the ambient row space by \\(S\\) can be identified with the two coordinates corresponding to \\(e_3^\*,e_4^\*\\).

In this quotient,

\\[ L_0A\equiv -e_3^\*. \\]

On the other hand,

\\[ l\equiv c e_3^\*+d e_4^\*. \\]

The denominator row space is

\\[ \operatorname{row}M_0=S+\operatorname{span}\\{l\\}. \\]

Therefore, the first requirement imposed by (5a) is

\\[ L_0A\in S+\operatorname{span}\\{l\\}. \\]

Modulo \\(S\\), this becomes

\\[ (-1,0)\in\operatorname{span}\\{(c,d)\\}. \\]

This is equivalent to

\\[ \boxed{c\ne0,\qquad d=0.} \tag{3} \\]

This condition is completely absent from the determinant calculation in Report 72.

### 2.2 Now impose the condition on \\(lA\\)

Direct multiplication gives

\\[ lA= \begin{bmatrix} a-b-e& a+c+e& -a-c& -b-d& a+b+c \end{bmatrix}. \\]

Modulo \\(S\\),

\\[ lA\equiv(-a-c,-b-d). \\]

Once (3) holds, we have \\(d=0\\), \\(c\ne0\\), and

\\[ \operatorname{span}\\{l\bmod S\\} = \operatorname{span}\\{(c,0)\\}. \\]

Thus the second requirement

\\[ lA\in S+\operatorname{span}\\{l\\} \\]

is equivalent to

\\[ -b=0. \\]

Consequently,

\\[ \boxed{b=0.} \tag{4} \\]

Combining (3) and (4), we obtain the exact feasible locus for the original condition (5a):

\\[ \boxed{ (5a)\iff b=0,\quad d=0,\quad c\ne0. } \tag{5} \\]

The coordinates \\(a\\) and \\(e\\) are unrestricted.

This is the correct characterization for the matrices in Report 72.

### 2.3 Why the determinant identity does not characterize (5a)

The report correctly calculates

\\[ \det \begin{bmatrix} lA\\\L_0\\\l\\\CA\\\C \end{bmatrix} =ad-bc. \\]

But this determinant only tests

\\[ lA\in\operatorname{row}M_0 \\]

when \\(\operatorname{rank}M_0=4\\).

The actual observer condition additionally requires

\\[ L_0A\in\operatorname{row}M_0. \\]

The two requirements are independent. In this example, the second one forces \\(c\ne0,d=0\\), after which the first forces \\(b=0\\).

Thus the determinant equation \\(ad-bc=0\\) is not the observer gate. It is only one part of the observer condition.

This is the most important correction to Report 72.&#x20;

72_conditional_gate_anchored_request.md



## 3. Consequence: the actual instance has no feasible observer

There is an even stronger consequence.

Recall the compressed matrices calculated in the previous analysis:

\\[ N= \begin{bmatrix} 1&0&0\\\ 1&0&0\\\ 0&1&0\\\ 0&0&1\\\ 0&0&0 \end{bmatrix}, \\]

\\[ H=LN= \begin{bmatrix} 1&0&0\\\ a+b&c&d \end{bmatrix}, \\]

and

\\[ H_A=LAN= \begin{bmatrix} 2&-1&0\\\ 2a-b+c&-a-c&-b-d \end{bmatrix}. \\]

Substitute the actual \\((5a)\\) conditions

\\[ b=d=0,\qquad c\ne0. \\]

Then

\\[ H= \begin{bmatrix} 1&0&0\\\ a&c&0 \end{bmatrix}, \\]

and

\\[ H_A= \begin{bmatrix} 2&-1&0\\\ 2a+c&-a-c&0 \end{bmatrix}. \\]

The pencil is

\\[ P(\lambda)=\lambda H-H_A = \begin{bmatrix} \lambda-2&1&0\\\ a\lambda-2a-c& c\lambda+a+c& 0 \end{bmatrix}. \\]

Its only potentially nonzero maximal minor is

\\[ \Delta\_{12}(\lambda) = c\lambda^2-c\lambda-c. \\]

Therefore

\\[ \boxed{ \Delta\_{12}(\lambda) = c(\lambda^2-\lambda-1). } \\]

Since \\(c\ne0\\), this is a nonconstant quadratic polynomial over \\(\mathbb C\\). It has two complex roots.

At either root,

\\[ \operatorname{rank}P(\lambda)<2. \\]

But

\\[ \operatorname{rank}H=2 \\]

because \\(c\ne0\\).

Consequently, (5b) fails for every point satisfying the actual (5a) condition.

We obtain the striking conclusion:

\\[ \boxed{ \text{For the matrices in Report 72, there is no }L \text{ satisfying both (5a) and (5b).} } \tag{6} \\]

This conclusion also means that the report's proposed boundary witness

\\[ l=(0,0,1,1,0) \\]

cannot be a feasible observer for the original problem. It satisfies the report's reduced determinant test and its compressed-pencil test, but it fails the missing \\(L_0A\\) row-inclusion requirement.

Likewise, the two intended-chart counterexamples in Part II.3 are not the main issue anymore: the entire intended gate analysis is based on a condition that omits one required row.

The previous review also missed this omission. The earlier determinant and pencil calculations were correct for the reduced matrices defined in the report, but they were not sufficient to establish the original observer feasibility claims. The present correction supersedes those conclusions.

## 4. What this means for the anchored-block request

The report asks for matrices \\(A,C,L_0\\) such that a fixed-pivot residual determinant gives

\\[ \det\begin{bmatrix} 1&x\\\ y&z \end{bmatrix} =z-xy, \\]

with constant \\(\operatorname{rank}M_0\\).&#x20;

72_conditional_gate_anchored_request.md



This is a sensible target, but the construction must begin with the correct matrix.

For \\(q=2\\), write

\\[ L=\begin{bmatrix}L_0\\\l\end{bmatrix}. \\]

Define

\\[ M_0=[L_0;l;CA;C]. \\]

Then the actual condition is

\\[ \boxed{ \operatorname{rank} \begin{bmatrix} L_0A\\\ lA\\\ M_0 \end{bmatrix} = \operatorname{rank}M_0. } \tag{7} \\]

There are two additional rows, not one.

A determinant construction that only considers

\\[ \begin{bmatrix} lA\\\M_0 \end{bmatrix} \\]

cannot establish (7), unless one separately proves that

\\[ L_0A\in\operatorname{row}M_0 \\]

for every candidate \\(l\\).

That is the first requirement for any new anchored construction.

### 4.1 The right residual formulation

Let

\\[ S=\operatorname{row}[L_0;CA;C]. \\]

Then

\\[ \operatorname{row}M_0=S+\operatorname{span}\\{l\\}. \\]

The full condition (5a) becomes

\\[ L_0A\in S+\operatorname{span}\\{l\\}, \qquad lA\in S+\operatorname{span}\\{l\\}. \\]

Equivalently, in the quotient space

\\[ Q=(\mathbb C^n)^\*/S, \\]

write

\\[ u=[L_0A]\in Q,\qquad x=[l]\in Q,\qquad v=[lA]\in Q. \\]

Then

\\[ \boxed{ u\in\operatorname{span}\\{x\\}, \qquad v\in\operatorname{span}\\{x\\}. } \tag{8} \\]

This is the correct algebraic form of the \\(q=2\\) problem.

The first inclusion is the fixed-row condition. The second is the variable-row condition.

The determinant in the report only captures the second inclusion.

### 4.2 A useful structural consequence

If \\(u\ne0\\), then the first condition in (8) forces

\\[ x=\alpha u \\]

for some nonzero scalar \\(\alpha\\).

Thus the quotient class of the variable row is forced to lie on a fixed one-dimensional line.

This observation is potentially useful for designing a new construction, but it does not by itself prove that an anchored multiplication gate is impossible for \\(q=2\\). The components of \\(l\\) lying in \\(S\\) may still vary, and those components can influence \\(lA\bmod S\\).

The correct research problem is therefore to understand the induced affine-linear dependence of \\(lA\bmod S\\) on the part of \\(l\\) lying in \\(S\\), after the quotient class has been anchored.

That is substantially different from the one-determinant problem considered in the report.

## 5. Answers to the four questions

### Question 1. Can we give a concrete anchored block with constant \\(\operatorname{rank}M_0\\) and determinant \\(z-xy\\)?

I cannot responsibly give such a construction from the current report, because the proposed determinant calculation does not represent the full condition (5a).

A new construction should satisfy the following requirements simultaneously.

Let

\\[ M_0=[L_0;l;CA;C]. \\]

First, the denominator rank must be constant:

\\[ \operatorname{rank}M_0=r \qquad\text{for every admissible parameter choice}. \tag{9} \\]

Second, both added rows must lie in the denominator row space:

\\[ L_0A\in\operatorname{row}M_0, \qquad lA\in\operatorname{row}M_0. \tag{10} \\]

Third, after eliminating a fixed pivot block, the residual conditions must include the desired equation

\\[ z-xy=0. \tag{11} \\]

A useful abstract target is a Schur-complement identity. Suppose a fixed invertible block \\(B\\) occurs in the denominator matrix, and the relevant augmented matrix has block form

\\[ \mathcal M= \begin{bmatrix} B&U\\\ V&W \end{bmatrix}. \\]

Then

\\[ \det\mathcal M = \det B\cdot\det(W-VB^{-1}U). \\]

If \\(B\\) is fixed and invertible, the residual determinant is well-defined for every assignment. One can aim for

\\[ W-VB^{-1}U=z-xy. \\]

This is the right general design principle.

But there is an important distinction: a Schur-complement determinant alone does not prove the full rank equality. One must verify that the fixed block is indeed present in the denominator matrix, that its rank is uniform, and that all rows of \\(LA\\), including \\(L_0A\\), are controlled.

I would therefore treat the fixed-pivot Schur-complement layout as a design template, not as an established observer construction.

### Question 2. Is \\(n=5,q=2\\) provably too small?

The report's experiments do not establish this.

The failed searches over random \\(A\\) and alternative \\(L_0\\) choices are evidence about the tested parameterizations, not a dimension lower bound.&#x20;

72_conditional_gate_anchored_request.md



There is, however, a useful distinction between the current example and the general question.

For \\(q=2\\), the quotient formulation (8) shows that the fixed row \\(L_0A\\) imposes a constraint on the quotient class of \\(l\\). If that class is nonzero, it must be proportional to a fixed vector.

This can substantially restrict the degrees of freedom available to the variable row. But the remaining components of \\(l\\) in \\(S\\) may still carry several independent coordinates.

Therefore, one cannot conclude from this observation that multiplication is impossible when \\(q=2\\).

Nor can one infer that \\(n=6\\) is sufficient. Increasing \\(n\\) adds ambient coordinates, but whether they can carry an anchored gate depends on the action of \\(A\\) on the relevant row-space quotient.

My recommendation is not to search for a minimal \\(n\\) yet. First formulate and solve the correct quotient-space realization problem for \\(q=2\\). Only then can one prove a lower bound or exhibit a dimension-six construction.

A rigorous minimal-dimension theorem would require a classification of the possible bilinear equations induced by the two row-inclusion conditions in (8), under the fixed-\\(A,C,L_0\\) constraint.

### Question 3. How should the uniform spectral condition be combined with the anchored gate?

The correct approach remains to separate the arithmetic and spectral mechanisms.

However, the order matters.

The present report tries to construct an arithmetic gate using only the \\(lA\\) row. Before adding a spectral guard, one must first construct an arithmetic gate satisfying both rows of (10).

After that, the spectral condition should be handled using a uniform certificate, not a generic gcd calculation.

A particularly strong certificate is a fixed maximal minor of

\\[ P(\lambda)=\lambda H-H_A \\]

equal to a nonzero constant. If such a minor exists, then

\\[ \operatorname{rank}P(\lambda)=\omega \qquad\forall\lambda\in\mathbb C \\]

follows immediately.

The shift-chain construction discussed in the preceding reports is a suitable candidate for this role. Its selected minor has determinant

\\[ (-1)^\omega, \\]

independent of the arithmetic variables.

The architecture should therefore be:

1. Arithmetic layer: construct a fixed-pivot rank condition encoding \\(z=xy\\), with the full (5a) condition enforced.
2. Spectral layer: arrange a fixed unit minor in the pencil.
3. Compatibility layer: prove that the spectral guard does not make the arithmetic rank condition redundant.
4. Lift layer: prove that all admissible row lifts preserve the extracted arithmetic assignment.

One should not simply append a large collection of fixed rows. If those rows saturate the denominator row space, then (5a) may become automatic. This is the same concern identified in the report, and it remains valid.&#x20;

72_conditional_gate_anchored_request.md



### Question 4. How should the full witness-extraction theorem be proved?

The cleanest approach is to formulate the reduction in terms of a projection from the observer witness space to the source assignment space.

Suppose the source multiplication relation is

\\[ z=xy. \\]

Let \\(\mathcal W\\) be the set of all observer witnesses satisfying the complete conditions:

\\[ \mathcal W= \left\\{ L: (5a),(5b),\text{ and all required independence conditions hold} \right\\}. \\]

A reduction requires a map

\\[ \pi:\mathcal W\longrightarrow\mathbb C^3 \\]

such that

\\[ \pi(L)=(x(L),y(L),z(L)) \\]

satisfies

\\[ z(L)=x(L)y(L) \\]

for every \\(L\in\mathcal W\\).

It also requires a lifting map in the other direction, or at least a proof that every source solution has an admissible observer witness.

The theorem should be stated in two directions.

Soundness. For every \\(L\in\mathcal W\\),

\\[ \pi(L)\in\mathcal V, \qquad \mathcal V=\\{(x,y,z):z=xy\\}. \\]

Completeness. For every \\((x,y,z)\in\mathcal V\\), there exists \\(L\in\mathcal W\\) such that

\\[ \pi(L)=(x,y,z). \\]

The important issue is that \\(\pi\\) must be defined on the entire feasible witness set, not just on a preferred chart.

For example, the formula \\(x=b/a\\) is not a global extraction map. It is only defined when \\(a\ne0\\). If the observer conditions permit a feasible witness with \\(a=0\\), the reduction must either:

- prove that such a witness cannot occur;
- give it a different, valid decoding;
- or show that it can be transformed into an equivalent witness with \\(a\ne0\\), preserving the intended source assignment.

The third possibility requires an actual normalization theorem, not an informal assertion that one may choose a convenient representative.

### 5.1 A useful proof decomposition

I recommend dividing the witness-extraction theorem into four lemmas.

Lemma A: Fixed-rank lemma.

Show that the denominator matrix has the required constant rank for every witness under consideration.

This prevents determinant conditions from acquiring exceptional branches when the denominator rank drops.

Lemma B: Arithmetic extraction lemma.

Show that every feasible witness determines a well-defined tuple \\((x,y,z)\\), and derive

\\[ z=xy \\]

from the full (5a) condition.

Lemma C: Spectral admissibility lemma.

Show that the pencil has constant rank at every finite complex \\(\lambda\\), preferably by a fixed maximal minor.

Lemma D: Lifting lemma.

Given any source assignment satisfying \\(z=xy\\), construct an observer witness satisfying all conditions.

The decomposition is useful because it separates the four principal failure modes:

- rank degeneration;
- spurious algebraic branches;
- pencil rank loss;
- failure of completeness.

For the current construction, the first two and third problems are all present, so the full theorem cannot be established.

## 6. Recommended revision to the research programme

I would revise the next stage of the project as follows.

### Priority 1: Re-audit every determinant gate against the complete observer condition

For every proposed construction, write the matrices in the order

\\[ M_0=[L;CA;C], \\]

\\[ M\_{\mathrm{full}}= \begin{bmatrix} LA\\\M_0 \end{bmatrix}. \\]

Then check

\\[ \operatorname{rank}M\_{\mathrm{full}} = \operatorname{rank}M_0. \\]

Do not replace \\(LA\\) by only its variable rows unless the fixed rows of \\(L_0A\\) have already been proved to lie in the denominator row space for every candidate witness.

This should become a permanent item on the project review checklist.

### Priority 2: Formulate the quotient-space gate problem correctly

For \\(q=2\\), use

\\[ S=\operatorname{row}[L_0;CA;C], \qquad Q=(\mathbb C^n)^\*/S. \\]

The full condition is

\\[ [L_0A]\in\operatorname{span}\\{[l]\\}, \qquad [lA]\in\operatorname{span}\\{[l]\\}. \\]

This formulation makes the fixed-row constraint explicit.

It also provides a natural starting point for classifying the polynomial equations that can arise from a one-free-row observer.

### Priority 3: Separate the three algebraic tasks

Do not conflate:

1. creating a multiplication determinant;
2. ensuring the denominator rank is constant;
3. ensuring the pencil has constant rank.

They are distinct requirements.

A construction may solve one and fail the other two. The current example is an illustration: the determinant identity is exact, but the full row inclusion and the pencil condition invalidate the intended gadget.

### Priority 4: Do not infer dimension bounds from random searches

The random searches reported in Part III are useful for exploring candidate structures, but they cannot establish that the \\(n=5,q=2\\) setting is impossible or that a particular dimension is minimal.

A dimension lower bound should come from a structural theorem about the quotient-space conditions.

## 7. Final verdict

Report 72 correctly records several important corrections to the earlier reduced determinant analysis, but it still does not describe the actual observer feasibility set.

The decisive issue is the omission of \\(L_0A\\) from the matrix used to test (5a).

For the specified \\(A,C,L_0\\), the full condition is

\\[ \boxed{b=d=0,\qquad c\ne0.} \\]

On this locus, the compressed pencil has the nonconstant maximal minor

\\[ \boxed{c(\lambda^2-\lambda-1),} \\]

which necessarily vanishes at finite complex values of \\(\lambda\\).

Therefore the proposed instance has no feasible observer satisfying both (5a) and (5b).

The consequences for the four questions are:

1. Anchored block: the present determinant gate is not a valid starting construction. A new construction must enforce both \\(L_0A\\) and \\(lA\\) in the denominator row space.
2. Minimal dimension: the report's experiments do not prove that \\(n=5,q=2\\) is too small. A quotient-space classification is needed.
3. Spectral guard: retain the shift-chain unit-minor idea, but introduce it only after a valid full (5a) arithmetic gate has been constructed.
4. Witness extraction: formulate soundness and completeness on the entire observer witness set, including all possible rank strata and lift freedoms.

The immediate next task should not be to search for a fixed-pivot determinant in the current reduced matrix. It should be to redesign the gate using the full matrix in (7). Otherwise, even a successful anchored determinant calculation could encode an equation that the actual observer problem does not impose.

This is a substantive correction to the project, but it is also useful: it identifies a precise algebraic source of the discrepancy and gives a quotient-space formulation from which a valid construction can be developed.