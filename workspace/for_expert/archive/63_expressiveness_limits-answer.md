# Research assessment of Report 63: expressiveness limits and the next hardness gadget

## 1. Overall assessment

Report 63 identifies three genuine restrictions on a direct reduction:

1. The compressed matrix \\(H=LN\\) is constrained primarily through a row-space inclusion, rather than through arbitrary affine equations on its entries.
2. In a Grassmannian chart, the invariant-subspace equation is generally a quadratic matrix equation, not an arbitrary affine system.
3. In the special case where the quadratic term vanishes, the remaining Sylvester operator has a highly structured form; diagonal blocks give only entrywise difference coefficients.

These observations are useful, but they do not rule out an \\(\exists\mathbb R\\)-hardness reduction. They rule out certain naive identifications of the source variables with \\(H\\) or \\(X\\), and they show that the most obvious linear encoding is too restrictive. They do not establish a general expressiveness barrier.

There is, however, one important correction to the report's structural description: the rows of \\(H\\) are not generally free inside \\(\operatorname{Ann}(V)\\). The corresponding rows of \\(H_A\\) are coupled to them through the same lift \\(l\\). This coupling is precisely where the observer problem may have more structure—and possibly more expressive power—than the row-space description alone suggests.

My recommendation is therefore:

- First, formulate the exact achievable compressed-pair space.
- In parallel, test a small multiplication gadget in the invariant-subspace equation.
- Do not yet attempt a full ETR reduction.
- Do not try to prove a sweeping rigidity theorem before testing whether the quadratic term can actually encode a gate.

The report's three observations and its six questions are the right starting point, but the next step should be a more exact model of the joint pair \\((H,H_A)\\).&#x20;

63_expressiveness_limits.md



## 2. Question 1: Do the three observations rule out a direct reduction?

### 2.1 What the row-space observation really establishes

The report correctly observes that

\\[ \ker H=V \quad\Longrightarrow\quad \operatorname{row}H\subseteq\operatorname{Ann}(V). \\]

For a fixed \\(V\\), this is a subspace constraint on the rows of \\(H\\). It is not, by itself, a system of arbitrary affine equations

\\[ \langle A_i,H\rangle=b_i. \\]

Consequently, a reduction that simply takes an arbitrary source matrix \\(X\_{\rm src}\\), identifies it with \\(H\\), and expects the observer conditions to enforce arbitrary affine constraints on \\(X\_{\rm src}\\) has no apparent mechanism for doing so. The report is right to reject that direct approach.

But there is a further restriction that should be included.

For each row \\(l\\) of \\(L\\), the corresponding compressed pair is

\\[ (h,g)=(lN,lAN). \\]

The two components are not independently chosen. They are the images of the same row \\(l\\) under two linear maps.

Thus, even if \\(h\in\operatorname{Ann}(V)\\), it does not follow that \\(g\\) can be chosen arbitrarily in \\(\operatorname{Ann}(V)\\). The condition (5a) requires

\\[ g|\_V=0, \\]

but the possible \\(g\\)'s are constrained by the fact that \\(h\\) and \\(g\\) must have a common lift \\(l\\).

This means that the report's phrase “inside \\(\operatorname{Ann}(V)\\) the rows are free” is too strong unless an additional surjectivity statement about the pair-lift map has been proved.

### 2.2 The exact pair-space formulation

Define the linear map

\\[ \Theta:\mathcal X^\*\longrightarrow K_0^\*\oplus K_0^\*, \qquad \Theta(l)=(lN,lAN), \\]

where \\(\mathcal X^\*\\) denotes the row space of all ambient covectors on \\(\mathbb C^n\\).

Its image

\\[ \mathscr P\_{A,C} = \operatorname{im}\Theta \subseteq K_0^\*\oplus K_0^\* \\]

is a fixed linear subspace determined by \\((A,C)\\).

The actual compressed rows must satisfy

\\[ \boxed{ (h_i,g_i)\in\mathscr P\_{A,C}. } \\]

For a candidate \\(V\\), condition (5a) further requires

\\[ h_i|\_V=0,\qquad g_i|\_V=0. \\]

Hence the admissible row pairs belong to

\\[ \boxed{ \mathscr P\_{A,C} \cap \bigl(\operatorname{Ann}(V)\oplus\operatorname{Ann}(V)\bigr). } \\]

This is a more faithful description of the observer's linear constraints than the condition on \\(H\\) alone.

It also identifies the precise obstacle to a direct affine-rank reduction: the source variables would have to be encoded in a family of row pairs lying in a fixed linear subspace, with both components tied to the same lift.

### 2.3 What is ruled out—and what is not

The three observations support the following conclusions.

| Proposed approach                                                              | Assessment                                                                                                |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| Identify an arbitrary source matrix directly with \\(H\\)                      | Not justified; the observer gives a kernel-dependent row-space constraint, not arbitrary affine equations |
| Identify an arbitrary source matrix directly with the chart coordinate \\(X\\) | Not justified; the chart equation is a structured quadratic system                                        |
| Use only diagonal Sylvester equations to encode arbitrary affine constraints   | Not supported; the coefficients are difference-structured                                                 |
| Use auxiliary variables and several coupled blocks                             | Not ruled out                                                                                             |
| Use the quadratic term \\(XA\_{12}X\\) to encode multiplication                | Promising, but requires a realization inside the full observer feasibility problem                        |
| Reduce from ETR through a restricted algebraic system                          | Still open                                                                                                |

So the correct conclusion is not that affine rank minimisation or ETR reductions are impossible. It is that the direct variable identifications proposed in the report do not provide a reduction.

There is no general no-go theorem here. A gadget reduction can use auxiliary variables, projections, block couplings, and existentially quantified coordinates. The source variables need not coincide with either \\(H\\) or \\(X\\).

## 3. Question 2: Can \\(XA\_{12}X\\) be used as a multiplication gadget?

Yes, at the level of the invariant-subspace equation, the quadratic term can encode a genuine multiplication gate. This is the most constructive observation I would add to Report 63.

It is not yet an observer-hardness reduction, because one must still force the observer-feasible subspaces to satisfy the invariant-subspace equation. Nevertheless, it gives a concrete gadget to investigate rather than merely a general suggestion that the quadratic term might be expressive.

### 3.1 A \\(2\times2\\) multiplication gadget

Consider the graph chart

\\[ V=\operatorname{graph}(X),\qquad X= \begin{bmatrix} x&z\\\ w&y \end{bmatrix}. \\]

Take the block matrix

\\[ A= \begin{bmatrix} A\_{11}&A\_{12}\\\ A\_{21}&A\_{22} \end{bmatrix}, \\]

with

\\[ A\_{11}=A\_{22}= \begin{bmatrix}0&0\\\0&1\end{bmatrix}, \qquad A\_{12}= -\begin{bmatrix}0&1\\\0&0\end{bmatrix}, \qquad A\_{21}=0. \\]

The invariant-subspace condition is

\\[ A\_{21}+A\_{22}X-XA\_{11}-XA\_{12}X=0. \\]

A direct calculation gives

\\[ A\_{22}X-XA\_{11}-XA\_{12}X = \begin{bmatrix} xw&-z+xy\\\ w+w^2&wy \end{bmatrix}. \\]

Thus invariance is equivalent to

\\[ \begin{cases} xw=0,\\\ z=xy,\\\ w(1+w)=0,\\\ wy=0. \end{cases} \\]

The second equation is exactly the desired multiplication gate:

\\[ \boxed{z=xy.} \\]

The auxiliary variable \\(w\\) does not create spurious violations of this relation. Indeed, every solution of the full system satisfies \\(z=xy\\). Conversely, for every \\(x,y\in\mathbb C\\), choosing

\\[ w=0,\qquad z=xy \\]

satisfies all four equations.

Therefore the invariant-subspace equation has a genuine existential multiplication-gadget interpretation:

\\[ \boxed{ \exists w:\ F_A(X)=0 \quad\Longleftrightarrow\quad z=xy, } \\]

where \\(x,y,z\\) are the designated entries of \\(X\\).

This is stronger than simply observing that the equation contains quadratic terms. It gives a small, explicit realization of a multiplication gate.

### 3.2 What this gadget does—and does not—prove

It establishes that the family of invariant-subspace equations

\\[ A\_{21}+A\_{22}X-XA\_{11}-XA\_{12}X=0 \\]

can express at least one nontrivial bilinear relation among chart coordinates.

It does not yet establish that the observer-feasibility problem can express the same relation. There are two missing steps.

First, one must force invariance. The observer's algebraic condition is

\\[ H_A|\_V=0. \\]

It does not require

\\[ A(V)\subseteq V. \\]

Invariance is sufficient for this condition, but it is not necessary. A reduction using the gadget must construct observer data for which every feasible \\(V\\) in the relevant chart is invariant, or otherwise prove that non-invariant feasible \\(V\\)'s cannot yield false positive instances.

Second, one must realize the required compressed rows. Even if a candidate \\(V\\) is invariant, the rows of \\(H\\) must come from actual rows of \\(L\\), and the resulting pencil must have full rank at every finite \\(\lambda\\). The multiplication gadget only handles the geometry of \\(V\\); it does not yet handle the lift and spectral conditions.

In particular, taking \\(C=0\\) and \\(N=I\\) would not solve the problem: then \\(H=L\\), so under a full-row-rank requirement on \\(L\\), one has \\(\operatorname{rank}H=q\\). The compressed pencil is square, and its determinant has a complex root. Thus the usual \\(q>\omega\\) mechanism needed to avoid the square-pencil obstruction must be retained.

### 3.3 A useful way to organize a future gadget library

I would distinguish three layers:

| Layer                     | Required gadget                                                                        | Current status                       |
| ------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------ |
| Grassmannian geometry     | Encode \\(z=xy\\) using invariant graph subspaces                                      | Explicit \\(2\times2\\) gadget above |
| Observer realization      | Force feasible \\(V\\)'s to satisfy the desired invariant-subspace equations           | Open                                 |
| Full observer feasibility | Realize the required row pairs, rank, and pencil conditions without spurious solutions | Open                                 |

This separation is important. A successful invariant-subspace gadget is a genuine algebraic result, but it is not yet a reduction to the observer problem.

### 3.4 A technical qualification about the chart equation

There is another point that should be made explicit in the report.

The displayed equation

\\[ A\_{21}+A\_{22}X-XA\_{11}-XA\_{12}X=0 \\]

is complete if \\(A(K_0)\subseteq K_0\\), or if the block decomposition is otherwise arranged so that the component outside \\(K_0\\) vanishes automatically.

In the general observer setting, \\(A\\) need not preserve \\(K_0\\). Choose a decomposition

\\[ K_0=E\oplus F,\qquad \dim E=c, \\]

and a complementary ambient space \\(G\\), so that

\\[ \mathbb C^n=E\oplus F\oplus G. \\]

Write the restriction of \\(A\\) to \\(K_0\\) as

\\[ A|\_{K_0} = \begin{bmatrix} A\_{11}&A\_{12}\\\ A\_{21}&A\_{22}\\\ A\_{31}&A\_{32} \end{bmatrix}. \\]

Then \\(V=\operatorname{graph}(X)\\) is \\(A\\)-invariant precisely when both

\\[ \boxed{ A\_{21}+A\_{22}X-XA\_{11}-XA\_{12}X=0 } \\]

and

\\[ \boxed{ A\_{31}+A\_{32}X=0 } \\]

hold.

The second equation ensures that \\(A(V)\\) remains inside \\(K_0\\). It is linear in \\(X\\), but it is an additional constraint that cannot be omitted in a general reduction.

This matters because a gadget that works in the \\(A\\)-invariant-\\(K_0\\) special case may fail when embedded in the full observer instance.

## 4. Question 3: Can block-diagonal Sylvester gadgets generate arbitrary affine constraints?

### 4.1 The limitation of the diagonal case

When \\(A\_{12}=0\\), the chart equation is

\\[ A\_{21}+A\_{22}X-XA\_{11}=0. \\]

If

\\[ A\_{11}=\operatorname{diag}(\lambda_1,\ldots,\lambda_c), \qquad A\_{22}=\operatorname{diag}(\mu_1,\ldots,\mu\_{k-c}), \\]

then

\\[ (\mu_i-\lambda_j)X\_{ij}=-(A\_{21})\_{ij}. \\]

This is a collection of independent scalar equations. Each entry is either fixed to a prescribed value or left free, depending on the corresponding eigenvalue difference.

Taking several independent diagonal blocks does not, by itself, turn these equations into arbitrary linear forms such as

\\[ \sum\_{i,j}a\_{ij}X\_{ij}=b. \\]

The reason is structural: the Sylvester operator

\\[ \mathcal S(X)=A\_{22}X-XA\_{11} \\]

has the Kronecker representation

\\[ \operatorname{vec}(\mathcal S(X)) = \left(I_c\otimes A\_{22}-A\_{11}^{\mathsf T}\otimes I\_{k-c}\right) \operatorname{vec}(X). \\]

Its coefficient matrix is not an arbitrary matrix on the vectorized chart coordinates. It belongs to a restricted Kronecker-sum family.

### 4.2 What happens when several blocks are combined?

There are two different constructions to distinguish.

Independent direct sums. If the gadgets are genuinely independent, their equations remain independent. One obtains a conjunction of separate constraints, not arbitrary linear combinations of the variables across the blocks.

Coupled block constructions. If off-diagonal blocks or shared coordinates are introduced, the equations may couple variables from different blocks. This is more promising, but it is no longer the simple diagonal difference-matrix construction. One must analyze the resulting Kronecker-structured operator or the full Riccati equation.

Thus, I would not claim that difference matrices are an absolute obstruction to all block-based constructions. The justified conclusion is narrower:

> Direct sums of diagonal Sylvester gadgets do not provide arbitrary affine constraints. Any successful block construction must introduce additional coupling or auxiliary-variable relations, and those relations need to be demonstrated explicitly.

### 4.3 A concrete test for the next block construction

Instead of trying to represent an arbitrary affine functional immediately, try to realize the smallest nontrivial shared-variable relation:

\\[ z=x+y. \\]

Use two copies of a small block, with \\(x\\) and \\(y\\) represented in separate coordinates, and ask whether the same chart coordinate \\(z\\) can be forced to equal their sum through the combined invariance equations.

This is a more informative test than asking whether a large block-diagonal construction can encode arbitrary affine rank minimisation. If even this one addition gate cannot be realized under the required block structure, that gives useful evidence about the limits of the Sylvester-only route.

There is also a possible algebraic-circuit strategy: represent addition using multiplication and constants, for example

\\[ x+y=(x+1)(y+1)-xy-1. \\]

But this is only useful after one has a reliable mechanism for identifying and reusing the same variable across multiple multiplication gadgets. Variable sharing is not automatic in a direct-sum construction.

## 5. Question 4: Is ETR a better source than affine rank minimisation?

### 5.1 My recommendation: use arithmetic circuits as the working source

Yes. Given the restrictions identified in Report 63, I would now use an arithmetic-circuit formulation of ETR as the primary source problem.

This is not because affine rank minimisation has been ruled out. Rather, affine rank minimisation presents the wrong interface for the current construction: it begins with arbitrary affine constraints on matrix entries, whereas the observer geometry naturally supplies structured quadratic equations and constrained row pairs.

An arithmetic circuit has a more compatible interface:

\\[ z=xy,\qquad z=x+y,\qquad z=\alpha x,\qquad z=\beta. \\]

The multiplication gate is already naturally present in the Riccati-type chart equation. The remaining challenge is to implement addition, constants, variable reuse, and output constraints.

The important strategic change is:

> Do not try to reproduce an arbitrary affine matrix family immediately. Try to build a small arithmetic-circuit interpreter inside the observer geometry.

### 5.2 Which gadget should be attempted first?

My suggested order is:

1. Multiplication gate. This is the most natural operation for the quadratic chart equation, and the \\(2\times2\\) construction above gives a concrete starting point.
2. Variable-sharing gadget. Establish how a variable represented by one chart coordinate can be reused in several gate blocks without creating unwanted solutions.
3. Addition gate. Either construct it directly or implement it using a small network of multiplication gates and constants.
4. Constant and output gadgets. Fix selected coordinates and enforce a final polynomial equation.
5. Observer-realization gadget. Only after the geometric circuit works should it be embedded into \\((A,C,L_0)\\), with the row-lift and spectral constraints controlled.

I would not begin with a rank-forcing gadget. Rank conditions are certainly part of the observer problem, but they are not the immediate bottleneck. The immediate bottleneck is whether the geometric variables can carry an arithmetic computation at all.

### 5.3 An important complexity-model issue: real versus complex variables

There is one foundational issue that should be settled before claiming an ETR reduction.

The report's mathematical setting uses complex matrices:

\\[ A\in\mathbb C^{n\times n},\qquad C\in\mathbb C^{p\times n}. \\]

But ETR is ordinarily the existential theory of the real numbers.

You must specify:

- Are the input matrices rational real matrices or rational complex matrices?
- Are the unknown observer matrices \\(L\\) required to be real or allowed to be complex?
- Is the pencil condition required for every \\(\lambda\in\mathbb C\\), even when the decision variables are real?

These choices affect the appropriate complexity class and the validity of a reduction.

If the unknown chart variables are complex, a real ETR reduction cannot simply be assumed: a complex variable is not automatically a real variable, and polynomial equations over \\(\mathbb C\\) do not by themselves impose that a variable lies in \\(\mathbb R\\).

If the unknown variables are real, an ETR reduction is more natural, although the all-complex-\\(\lambda\\) pencil condition still needs an exact real-algebraic encoding.

I would make this distinction explicit in the next report. It is not a cosmetic convention; it determines what the target decision problem actually is.

## 6. Question 5: Are there existing observer-theoretic results that describe the achievable compressed pairs?

There is relevant literature, but I would distinguish two levels of result.

### 6.1 Existing observer characterisations

The observer literature already contains algebraic and spectral characterisations of functional-observer existence.

For example:

- Darouach and Fernando's 2025 Automatica paper develops algebraic conditions for functional observability and observer design, and describes the observer parameters through a constrained Sylvester equation.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

  sciencedirect.com+1

- Fernando's 2026 preprints give order-by-order characterisations of minimum-order functional observers, including nullspace representations and rank and matrix-pencil conditions. These are particularly close to the framework of the present project.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

  arXiv+1

- Darouach and Fernando's 2020 IEEE Transactions on Automatic Control paper gives a general formulation and a parametrisation of functional observers.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

  DOI



These works are relevant for checking whether the observer equations or their parameterisations can be simplified before attempting a complexity reduction.

However, the abstracts and descriptions I checked do not establish that the exact pair space

\\[ \mathscr P\_{A,C} = \\{(lN,lAN):l\in\mathcal X^\*\\} \\]

has already been characterized in the form needed for this reduction. I would not claim that the pair-space theorem below is already a named theorem from the literature.

### 6.2 The exact pair-space theorem worth proving and using

The following is a direct linear-algebraic characterisation.

Let

\\[ \Theta:\mathcal X^\*\to K_0^\*\oplus K_0^\*, \qquad \Theta(l)=(lN,lAN). \\]

Then the set of achievable compressed row pairs is exactly

\\[ \mathscr P\_{A,C}=\operatorname{im}\Theta. \\]

For a fixed candidate subspace \\(V\subseteq K_0\\), define

\\[ \mathcal L_V = \\{l\in\mathcal X^\*: lN|\_V=0,\quad lAN|\_V=0\\}. \\]

Equivalently,

\\[ \mathcal L_V = \ker\left[ l\longmapsto \bigl(lN|\_V,\ lAN|\_V\bigr) \right]. \\]

This gives an exact description of the rows that can be used for a candidate \\(V\\). In particular:

- Every row of \\(L\\) must belong to \\(\mathcal L_V\\).
- The prescribed rows of \\(L_0\\) must already belong to \\(\mathcal L_V\\).
- The bottom rows must be chosen from \\(\mathcal L_V\\) so that the required compressed rank is attained.
- If row independence modulo \\(\operatorname{row}C\\) is part of the observer convention, the simultaneous completion condition must also be imposed.

This formulation is useful because it turns the lift problem into a linear-algebraic fibre calculation for each \\(V\\). It also makes clear that the lift constraints are not merely conditions on \\(H\\).

The pair-space formulation is therefore a natural bridge between the geometric variables \\(V\\) and the actual observer rows.

### 6.3 The pencil condition is an additional, separate restriction

Even after the row-pair lift is solved, the spectral condition remains.

Under the kernel inclusion, define \\(Z\\) by

\\[ H_A=ZH,\qquad Z:\operatorname{im}H\to\mathbb C^q. \\]

With a splitting

\\[ \mathbb C^q=\operatorname{im}H\oplus W', \qquad Z=\begin{bmatrix}A\_\*\\\B\_\*\end{bmatrix}, \\]

the compressed pencil is good precisely when

\\[ \ker(A\_\*-\lambda I)\cap\ker B\_\*=\\{0\\} \\]

for every \\(\lambda\in\sigma(A\_\*)\\).

Equivalently, \\(B\_\*\\) must be injective on every eigenspace of \\(A\_\*\\).

This is the Hautus-type observability criterion for the pair \\((B\_\*,A\_\*)\\). It is not an arbitrary open condition on \\(H\\) independent of the lift: \\(A\_\*\\) and \\(B\_\*\\) are induced by the achievable pair data.

Thus, a useful structural theorem should characterize the interaction of three objects:

\\[ \boxed{ \text{achievable row-pair space} \quad+\quad \text{rank of }H \quad+\quad \text{eigenspace injectivity of }B\_\*. } \\]

That is a more promising target than a theorem about \\(H\\) alone.

### 6.4 Adjacent hardness results should not be confused with this problem

There is an NP-hardness result for optimal sensor placement in functional observability and structural functional observability. But that concerns selecting sensors, not deciding whether an augmentation \\(R\\) of a prescribed functional observer can satisfy the given rank and pencil conditions. It is relevant background, not a reduction to the present problem.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://ieeexplore.ieee.org\&sz=32)

IEEE Xplore+1



## 7. Question 6: Should the project pursue a gadget construction or a rigidity theorem first?

I recommend a short, targeted rigidity phase followed immediately by a gadget experiment. I would not spend a long period trying to prove a global rigidity theorem before testing the multiplication gate.

There are two distinct reasons.

First, the achievable-pair space is an exact linear object that can be characterized without resolving the full nonlinear observer problem. It should be understood before any reduction is attempted.

Second, the \\(2\times2\\) multiplication gadget shows that the Grassmannian invariance equation has at least some arithmetic expressiveness. A global rigidity theorem would need to explain why that expressiveness cannot survive the observer lift and pencil constraints. We do not yet have evidence for such a theorem.

### 7.1 The first rigidity theorem I would formulate

For each \\(V\in\operatorname{Gr}(c,K_0)\\), define

\\[ \mathcal L_V = \\{l:lN|\_V=0,\ lAN|\_V=0\\}. \\]

Then establish a theorem giving necessary and sufficient conditions for a prescribed number of rows to be selected from \\(\mathcal L_V\\) so that:

1. the prescribed top rows \\(L_0\\) are included;
2. the compressed matrix \\(H=LN\\) has rank \\(\omega\\);
3. the chosen rows satisfy the relevant independence convention;
4. the induced map \\(Z\\) has the eigenspace-injectivity property required by the pencil condition.

The first three items are fundamentally linear-algebraic once \\(V\\) is fixed. The fourth is spectral.

This theorem would provide a precise description of the fibre over \\(V\\): which observer matrices \\(L\\) can be realized for that particular kernel subspace?

It would also help identify whether the observer constraints can force \\(V\\) into the invariant-subspace locus.

### 7.2 The second theorem should be a nontriviality or obstruction result

A useful next question is whether the row-pair space imposes a restriction on the set of feasible \\(V\\)'s beyond the requirement that the fixed rows belong to \\(\mathcal L_V\\).

For example, can one derive a condition of the form

\\[ V\in\mathcal Z(A,C,L_0) \\]

where \\(\mathcal Z\\) is a proper algebraic subset of the Grassmannian, or perhaps show that all feasible \\(V\\)'s in a certain parameter regime are \\(A\\)-invariant?

Such a result could either help the reduction or rule out a proposed gadget.

But I would avoid aiming immediately for a theorem saying that the observer-feasible locus is always simple, low-dimensional, or incapable of encoding arithmetic. The current results do not support such a broad assertion.

## 8. Recommended next research programme

I would organize the next phase into four tightly defined tasks.

Task A — Exact pair-lift theorem

Prove the fibre description using

\\[ \mathcal L_V=\ker(l\mapsto(lN|\_V,lAN|\_V)). \\]

State separately the conclusions under full row rank and under independence modulo \\(\operatorname{row}C\\).

First priority

Task B — Multiplication-gate realization

Start with the \\(2\times2\\) Riccati gadget above. Determine whether observer data can force its graph subspace to be invariant and preserve the desired chart coordinates.

First construction experiment

Task C — Spectral and lift gadget

Construct a small extension in which the induced pair \\((B\_\*,A\_\*)\\) satisfies the Hautus injectivity criterion for every intended gate solution. Prove that the row-pair lifts can be completed simultaneously.

Main observer-specific obstacle

Task D — Circuit composition

Only after Tasks A–C succeed, investigate variable sharing, addition, constants, and output constraints. Then attempt a reduction from a precisely specified real or complex arithmetic-circuit feasibility problem.

### Suggested stopping criteria

A small gadget experiment should be regarded as successful only if it proves both directions:

- Every source assignment satisfying the intended gate gives a feasible observer witness.
- Every feasible observer witness yields a source assignment satisfying the intended gate.

A construction that only embeds source solutions into observer solutions is not enough: spurious observer solutions would invalidate the reduction.

Likewise, a pencil-goodness argument based only on genericity is insufficient unless the construction proves that the required generic choice is compatible with the fixed top rows and the row-pair lift constraints.

## 9. Final answers to the six questions

| Question                                                            | Conclusion                                                                                                                                                                         |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Q1. Do the three observations rule out a direct reduction?          | They rule out the naive identifications \\(H=X\_{\rm src}\\) and \\(X=X\_{\rm src}\\) as complete reductions. They do not rule out auxiliary-variable or coupled-block reductions. |
| Q2. Can the quadratic term encode multiplication?                   | Yes, at the invariant-subspace level. The explicit \\(2\times2\\) gadget above realizes \\(z=xy\\). Its realization inside observer feasibility remains open.                      |
| Q3. Can diagonal block gadgets encode arbitrary affine constraints? | Not by direct sums alone. The difference-matrix structure is a real restriction. Coupled blocks may be more expressive, but need explicit constructions.                           |
| Q4. Is ETR a better source?                                         | Yes, as a working source problem. Start with multiplication, then variable sharing and addition. Specify whether the target problem has real or complex unknowns.                  |
| Q5. Are there relevant observer-theoretic structural results?       | Yes: algebraic, nullspace, Sylvester, and pencil characterisations exist. The exact achievable compressed-pair space is the most useful additional formulation for this project.   |
| Q6. Rigidity or gadgets first?                                      | Prove the exact pair-lift theorem first, then test the multiplication gadget immediately. Do not postpone gadget construction until after a broad rigidity programme.              |

## 10. Overall research judgement

Report 63 makes a valuable transition from asking whether arbitrary affine constraints can be placed directly into the observer equations to asking what algebraic computations the observer geometry can actually represent.

That is the right change in viewpoint.

The key positive result is that the Grassmannian chart equation is not merely an awkward quadratic constraint: it can encode a multiplication gate. The key negative result is that the observer does not freely choose the two compressed rows \\(lN\\) and \\(lAN\\); they must arise from a common lift. The central research question is therefore no longer simply whether the Riccati equation is expressive enough. It is:

\boxed{\
\begin{minipage}{0.88\linewidth}\
Can one realize a sufficiently expressive family of invariant-subspace equations as the feasible-kernel locus of an observer instance, while preserving simultaneous row lifting and the all-\\(\lambda\\) pencil condition?\
\end{minipage}\
}

I would make that the central question of Report 64.

A successful answer in either direction would be significant:

- A positive answer would give a plausible route to an \\(\exists\mathbb R\\)-hardness proof.
- A negative answer, if supported by a genuine structural theorem, would identify a substantive limitation of the observer-feasible geometry and redirect the hardness search.

At present, the evidence supports neither a hardness conclusion nor a general rigidity conclusion. It does support a concrete next experiment: embed the multiplication gadget into the full observer problem, rather than trying to encode an entire affine rank-minimisation instance at once.

The pair-lift theorem and that one-gate realization are the two most valuable immediate deliverables.