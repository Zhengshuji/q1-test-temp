# Review of `26_d1_b13_revisions.md`

The revisions are moving in the right direction. More importantly, the team has responded correctly to the distinction between a mathematically valid result, a proof that is not yet complete, and a statement whose formalization does not actually match the paper theorem.

My assessment is:

1. B.4: The correction is accepted. The distinction between the right-eigenvector criterion and the dual criterion must also be reflected in the Lean registry.
2. D.1: The direct lower-bound proof in §II.2 is correct. The recursive \\((\le)\\) direction in §II.3 is not yet sufficiently justified. I would not accept the recursive identity as proved.
3. B.13: The three-stage decomposition is appropriate, but the proposed incidence lemma in §III.1–III.2 has another important mathematical problem: the fiber is not necessarily a singleton. The zero locus of the homogeneous pencil must be treated separately.
4. The two theorem mergers: Both are mathematically well motivated, but the proposed formulation of the intrinsic spectral characterization needs a small clarification.

I will examine each point separately.

# I. B.4 — The correction and the Lean discrepancy

修订成立

The revised criterion is

\\[ \boxed{ (5b)\iff \text{\\(A\\) has no right eigenvector in } \ker[C;CA]. } \\]

This is the correct statement under the project's row-space convention.

## 1. Why the distinction matters

The two conditions are

\\[ \exists x\ne0: \quad Ax=\lambda x,\quad Cx=CAx=0, \\]

and

\\[ \exists\varphi\ne0: \quad \varphi A=\lambda\varphi,\quad \varphi C=\varphi CA=0. \\]

They are not equivalent in general.

The first concerns the right eigenspace of \\(A\\); the second concerns the left eigenspace.

The numerical experiment reported in the revision is useful:

| Criterion             | Agreement with pencil rank loss |
| --------------------- | ------------------------------- |
| Right eigenvector (P) | 3962/3962                       |
| Left eigenvector (D)  | 3845/3962                       |

The 117 counterexamples to the dual criterion are especially useful because they demonstrate that the distinction is not merely a notational concern.

Nevertheless, the mathematical proof, not the numerical experiment, should be the basis of the theorem.

## 2. The Lean discrepancy is correctly identified

The previous Lean declaration proves

\\[ \dim(M^\top+\mathcal J)=n \iff \ker M\cap\mathcal J^\perp=\\{0\\}, \\]

or its equivalent dual-space formulation, depending on the exact definitions of the matrices involved.

This is a valid linear-algebra theorem.

But it does not establish the corrected B.4 statement.

I strongly agree with the decision to remove it from the B.4 coverage registry.

This is an important point about formal verification:

\\[ \boxed{ \text{A formally verified theorem is useful only if its formal statement matches the mathematical statement being claimed.} } \\]

The Lean declaration should be retained as a standalone auxiliary lemma, rather than discarded. It may still be useful elsewhere.

## 3. Recommended corrected theorem

I suggest the following paper formulation.

Theorem B.4 (Full-space spectral criterion).

Suppose \\(\mathcal V=\mathbb C^n\\), and let

\\[ K=\ker \begin{bmatrix} C\\\CA \end{bmatrix}. \\]

Then the full-space pencil has constant column rank if and only if

\\[ \ker(A-\lambda I)\cap K=\\{0\\} \qquad \forall\lambda\in\mathbb C. \\]

Equivalently, no right eigenvector of \\(A\\) belongs to \\(K\\).

The proof should proceed directly from the pencil kernel.

Verdict: Accept the correction. The new Lean declaration should be classified as pending, not as a previously completed theorem.

# II. D.1 — Detailed examination of the revision

This is the most important part of the present review.

I distinguish the direct lower bound from the recursive identity because they have different mathematical statuses.

## 1. Definition and empty-feasibility convention

The revised definition is

\\[ P(A,B,S)= \begin{cases} \min\\{\dim U:S\subseteq U,\ AU\subseteq U+B\\}, &\mathcal F\ne\varnothing,\\\ +\infty,&\mathcal F=\varnothing. \end{cases} \\]

Here \\(\mathcal F\\) denotes the feasible family.

成立

This is the correct convention.

It also resolves the issue that arose from taking an infimum over \\(\mathbb N\\).

The minimum exists whenever the feasible family is nonempty because the possible dimensions belong to the finite set

\\[ \\{0,1,\ldots,\dim Y\\}. \\]

Thus there is no need to use an infimum in the finite-dimensional setting.

I recommend retaining this definition throughout the paper and the Lean development.

## 2. The direct lower bound in §II.2

成立

The claimed result is

\\[ \boxed{ P(A,B,S)\ge \dim S+ \dim\frac{AS+S+B}{S+B}. } \\]

The revised proof is correct.

Let us verify each step carefully.

Take any feasible \\(U\\). Then

\\[ S\subseteq U, \qquad AU\subseteq U+B. \\]

Since \\(S\subseteq U\\),

\\[ AS\subseteq AU\subseteq U+B. \\]

Consequently,

\\[ AS+S+B\subseteq U+B. \\]

Passing to the quotient by \\(S+B\\) gives

\\[ \frac{AS+S+B}{S+B} \subseteq \frac{U+B}{S+B}. \\]

Now consider the natural map

\\[ U\longrightarrow \frac{U+B}{S+B}. \\]

It is surjective, with kernel

\\[ U\cap(S+B). \\]

Therefore

\\[ \frac{U+B}{S+B} \cong \frac{U}{U\cap(S+B)}. \\]

Since

\\[ S\subseteq U\cap(S+B), \\]

we have

\\[ \dim\frac{U}{U\cap(S+B)} \le \dim\frac US. \\]

Combining these inclusions,

\\[ \dim\frac{AS+S+B}{S+B} \le \dim\frac US. \\]

Finally,

\\[ \dim U = \dim S+\dim\frac US, \\]

so

\\[ \dim U\ge \dim S+ \dim\frac{AS+S+B}{S+B}. \\]

Taking the minimum over all feasible \\(U\\) proves the assertion.

If the feasible family is empty, the inequality remains valid under the new \\(+\infty\\) convention.

This proof is complete.

I particularly approve of the decision to eliminate the recursive argument from this lower-bound proof. The direct argument is shorter, stronger in presentation, and avoids unnecessary quotient-operator issues.

## 3. The recursive construction in §II.3

有缺口

Now consider the proposed construction:

\\[ M=T+C, \\]

\\[ \pi:Y\longrightarrow Y/M, \\]

\\[ C'=\pi\Phi(M), \qquad T'=\pi\Phi(T), \\]

and

\\[ \Phi': \frac YM\longrightarrow \frac{Y/M}{C'}, \\]

defined by

\\[ \Phi'(y+M)=\Phi(y)+C'. \\]

There are several things to distinguish.

### 3.1 The well-definedness argument

The well-definedness proof is correct, provided the notation is interpreted as follows:

\\[ \Phi:Y\to Y/C \\]

or, equivalently, \\(\Phi\\) is a map into a space in which the indicated quotient operations are defined.

If \\(y'-y=m\in M\\), then

\\[ \Phi(y')-\Phi(y)=\Phi(m). \\]

By definition,

\\[ \pi\Phi(m)\in C'. \\]

Hence the two representatives have the same image in the second quotient.

Therefore

\\[ \boxed{\Phi'(y+M)=\Phi(y)+C'} \\]

is well-defined.

The important conceptual correction is also right:

\\[ \boxed{ \Phi'\text{ is a map into a further quotient, not an endomorphism of }Y/M. } \\]

This avoids the invalid assumption that \\(M\\) is invariant under the original operator.

### 3.2 The \\((\ge)\\) direction

The proposed argument is

\\[ \dim U\ge \dim T+ \mathcal P(Y/M,C',\Phi',T'). \\]

The dimension estimate

\\[ \dim U = \dim(U\cap M)+\dim\pi(U) \\]

is correct, and

\\[ T\subseteq U\cap M \\]

gives

\\[ \dim(U\cap M)\ge\dim T. \\]

However, there is one point that needs to be stated explicitly:

You must prove that \\(\pi(U)\\) is feasible for the precise quotient problem being defined.

This requires checking that the original feasibility relation

\\[ \Phi(U)\subseteq(U+C)/C \\]

translates exactly into the corresponding relation involving \\(\Phi'\\).

The current report asserts this but does not write out the full equivalence.

I believe this direction is repairable, but I would request the exact definitions of the domain, codomain and feasibility relation before marking it complete.

### 3.3 The \\((\le)\\) direction: the unresolved \\(\sigma\\)-step

This is where I would be most cautious.

You state that for a feasible quotient subspace \\(U'\\), one takes

\\[ U=\pi^{-1}(U') \\]

and constructs a correction map

\\[ \sigma \\]

using:

- an interval-inclusion lemma;
- surjectivity of \\(M\to C'\\);
- a correction ensuring\
  \\[\
  \Phi(\sigma u')\in\pi^{-1}(U')+C.\
  \\]

The difficulty is that surjectivity alone does not establish the required inclusion.

Suppose

\\[ \theta:M\to C', \qquad \theta(m)=\pi\Phi(m). \\]

By definition, \\(\theta\\) is surjective.

But to construct a linear correction \\(\sigma\\), one needs to establish not merely that every individual target has a preimage, but that the preimages can be chosen compatibly with the required subspace constraints.

In finite-dimensional vector spaces, a surjective linear map admits a linear right inverse. This helps, but it does not automatically establish the interval inclusion or the required compatibility with \\(U'\\).

The correction must satisfy a precisely specified equation.

For example, if the goal is

\\[ \Phi(\sigma u')\in\pi^{-1}(U')+C, \\]

then one should first express this condition in the quotient \\(Y/M\\), and identify exactly which subspace must contain

\\[ \pi\Phi(\sigma u'). \\]

Only then can one use a right inverse of \\(\theta\\).

I cannot certify the \\((\le)\\) direction from the present document because the interval-inclusion lemma and the definition of the correction map are not supplied.

There is also a notation issue worth resolving: the revised report defines \\(T'=\pi\Phi(T)\\), but does not explain how this subspace enters the quotient feasibility problem. The exact role of \\(T'\\) must be specified, particularly because

\\[ T\subseteq M \quad\Longrightarrow\quad T'\subseteq C'. \\]

This is not automatically a contradiction, but it makes the quotient problem's admissibility condition important to state explicitly.

### 3.4 What I recommend

Do not present the recursive equality as a theorem yet.

Keep the two results separate:

- The direct lower bound is proved.
- The recursive identity is a conjectured or partially proved structural refinement.

The direct lower bound is already useful and does not depend on the unresolved construction.

# III. B.13 — Examination of the homogeneous incidence variety

拆分方向正确，但入射引理仍需修正

I agree with the three-stage decomposition:

1. Incidence lemma.
2. Fiber lemma.
3. Coverage lemma.

This is the right way to organize the argument.

However, I found an additional issue in the proposed homogeneous construction. It is important enough that I would correct it before writing the first lemma.

## 1. The homogeneous pencil: one incorrect statement

You define

\\[ [\alpha:\beta]\in\mathbb P^1, \qquad \lambda=\frac{\alpha}{\beta}, \\]

and homogenize

\\[ \lambda I-A \\]

as

\\[ P(\alpha,\beta)=\alpha I-\beta A. \\]

This homogenization is correct.

But the description of the point at infinity in §III.1 is not correct.

At

\\[ \beta=0,\qquad \alpha\ne0, \\]

we have

\\[ P(\alpha,0)=\alpha I. \\]

Consequently,

\\[ [z]=[P(\alpha,0)x]=[x], \\]

not

\\[ [Ax]. \\]

The latter would correspond to a different homogeneous pencil.

This is a definite algebraic correction, not merely a matter of projective convention.

I recommend explicitly recording:

\\[ \boxed{ P(\alpha,\beta)=\alpha I-\beta A, \quad P(1,0)=I, \quad P(0,1)=-A. } \\]

The point \\([1:0]\\) represents the infinite value of the affine parameter \\(\lambda\\).

The point \\([0:1]\\) represents \\(\lambda=0\\).

This distinction should be maintained throughout the proof.

## 2. A more serious issue: the zero locus of the pencil

Your proposed incidence variety is

\\[ \mathfrak I= \left\\{ ([x],[z],[\alpha:\beta]): z\wedge P(\alpha,\beta)x=0 \right\\}. \\]

Suppose

\\[ P(\alpha,\beta)x=0. \\]

Then

\\[ z\wedge P(\alpha,\beta)x=0 \\]

for every \\(z\\).

Therefore, the fiber over a fixed \\(([x],[\alpha:\beta])\\) is not necessarily a single point.

It can be the entire projective space \\(\mathbb P(K)\\).

This invalidates the proposed fiber lemma as currently stated.

The issue is not that the homogeneous equation is wrong. The equation is correct. The issue is that it also includes the base locus of the rational map

\\[ ([x],[\alpha:\beta]) \longmapsto [P(\alpha,\beta)x]. \\]

We need to separate that base locus.

## 3. The correct incidence construction

Let

\\[ v=\dim V,\qquad k=\dim K. \\]

Use the ambient space

\\[ \mathcal D=\mathbb P(V)\times\mathbb P^1 \\]

and define

\\[ P\_{\alpha,\beta}=\alpha I-\beta A. \\]

The base locus is

\\[ \boxed{ \mathcal B= \left\\{ ([x],[\alpha:\beta])\in\mathcal D: P\_{\alpha,\beta}x=0 \right\\}. } \\]

Now define

\\[ \mathfrak I= \left\\{ ([x],[z],[\alpha:\beta]) \in \mathbb P(V)\times\mathbb P(K)\times\mathbb P^1: z\wedge P\_{\alpha,\beta}x=0 \right\\}. \\]

There are two distinct strata.

Stratum A: Outside the base locus.

If

\\[ P\_{\alpha,\beta}x\ne0, \\]

then the wedge equation implies

\\[ [z]=[P\_{\alpha,\beta}x]. \\]

There is at most one possible projective point \\([z]\\).

If \\(P\_{\alpha,\beta}x\notin K\\), there is no such point.

Thus the fiber has dimension at most zero.

Stratum B: On the base locus.

If

\\[ P\_{\alpha,\beta}x=0, \\]

then the wedge equation is automatic.

The entire space

\\[ \mathbb P(K) \\]

is a fiber.

Its dimension is

\\[ k-1. \\]

This is the essential correction.

## 4. The resulting dimension estimate

The dimension of the base parameter space is

\\[ \dim\mathcal D = (v-1)+1=v. \\]

On the complement of \\(\mathcal B\\), the incidence set has fibers of dimension at most zero.

Therefore that part has dimension at most \\(v\\).

Over \\(\mathcal B\\), the fiber dimension is at most \\(k-1\\).

Consequently,

\\[ \boxed{ \dim\mathfrak I \le \max\left\\{ v,\\, \dim\mathcal B+k-1 \right\\}. } \\]

This is the appropriate starting point for the incidence dimension argument.

It is not yet the desired covering theorem. It is an intermediate estimate that can be used to establish one.

There are two further qualifications:

- If \\(K=\\{0\\}\\), then \\(\mathbb P(K)\\) is empty, so this projective construction must be treated separately.
- If the bad configurations impose additional restrictions on \\(x\\), such as \\(L_0x\ne0\\), those restrictions must be incorporated into the relevant constructible strata.

## 5. Is the proposed incidence set closed?

Yes, with an important distinction.

The equation

\\[ z\wedge P\_{\alpha,\beta}x=0 \\]

is homogeneous in the projective coordinates and defines a closed algebraic subset of

\\[ \mathbb P(V)\times\mathbb P(K)\times\mathbb P^1. \\]

However, the part on which

\\[ P\_{\alpha,\beta}x\ne0 \\]

is only an open subset of this closed incidence variety.

Thus the graph of the rational map is not automatically the same as the full closed incidence variety.

This is precisely why the base-locus analysis is necessary.

Your revised report correctly recognizes the importance of distinguishing the closed incidence set from its constructible strata, but the fiber argument must incorporate the base locus explicitly.

## 6. Recommended first lemma

I would now write the first lemma as follows.

Lemma B.13a (Homogeneous incidence and base-locus dimension bound).

Let \\(V,K\\) be nonzero finite-dimensional complex vector spaces, with \\(V,K\subseteq\mathbb C^n\\), and let \\(A\in\mathbb C^{n\times n}\\).

Define

\\[ P\_{\alpha,\beta}=\alpha I-\beta A. \\]

Let

\\[ \mathcal B= \left\\{ ([x],[\alpha:\beta])\in \mathbb P(V)\times\mathbb P^1: P\_{\alpha,\beta}x=0 \right\\} \\]

and

\\[ \mathfrak I= \left\\{ ([x],[z],[\alpha:\beta]): z\wedge P\_{\alpha,\beta}x=0 \right\\}. \\]

Then:

1. \\(\mathfrak I\\) is a closed algebraic subset of the indicated projective product.
2. Outside \\(\mathcal B\\), the fibers of the projection to \\(\mathbb P(V)\times\mathbb P^1\\) have dimension at most zero.
3. Over \\(\mathcal B\\), the fibers have dimension at most \\(\dim K-1\\).
4. Consequently,\
   \\[\
   \dim\mathfrak I\
   \le\
   \max\left{\
   \dim V,,\
   \dim\mathcal B+\dim K-1\
   \right}.\
   \\]

This is a valid standalone algebraic-geometric statement.

I would accept this as the first stage once the elementary proof is written.

An important recommendation: Do not try to prove the coverage theorem at the same time. First establish this incidence lemma and verify its dimension estimate independently.

# IV. Are the two theorem mergers appropriate?

## 1. B.16 + B.17 + B.21: Unified quotient-pencil theorem

同意合并

I agree with this merger.

In fact, I consider it one of the best organizational improvements in the revision.

The three propositions are different consequences of one underlying object:

\\[ \overline N_Z(\lambda): V/S\longrightarrow X/Z, \qquad S=V\cap Z. \\]

The unified theorem should have four parts.

### Part A. Permanent kernel

Under (5a),

\\[ S\subseteq\ker N_Z(\lambda) \qquad\forall\lambda. \\]

### Part B. Exact feasibility criterion

\\[ \boxed{ (5b) \iff \ker N_Z(\lambda)=S \qquad\forall\lambda. } \\]

Equivalently,

\\[ \overline N_Z(\lambda) \\]

is injective for every \\(\lambda\\).

### Part C. Layer stratification

With

\\[ s=\dim S, \\]

distinguish:

\\[ s=0,\qquad 0\<s<\dim V,\qquad s=\dim V. \\]

This is the correct way to separate the full-column-rank, intermediate, and automatic cases.

### Part D. Polynomial right-null module

Under the full observer-pencil hypotheses and the factorization established by (5a),

\\[ \boxed{ \ker\_{\mathbb C[\lambda]}Q_L(\lambda) = S\otimes\mathbb C[\lambda]. } \\]

Hence every right minimal index is zero.

One qualification: Part D concerns the original observer pencil \\(Q_L\\), while Parts A–C concern the quotient pencil \\(N_Z\\). They are related, but their domains and codomains should be stated separately.

I would not merge them into one unexplained matrix identity.

Instead, make the theorem a unified structural theorem with four clearly separated conclusions.

This will improve the mathematical narrative substantially.

## 2. B.23 + B.24: Intrinsic spectral characterization

同意合并，但需精确措辞

The proposed combination is

\\[ \Phi=K_1|\_W \\]

and

\\[ (5b)\text{ fails} \iff \exists\\,0\ne w\in W: \Phi(w)=K_1w\in\mathbb Cw. \\]

The mathematical idea is correct.

There is, however, a subtle point about terminology.

The map is

\\[ \Phi:W\longrightarrow\mathbb C^q. \\]

It is not necessarily an endomorphism

\\[ \Phi:W\longrightarrow W. \\]

Therefore, calling it an ordinary operator on \\(W\\) may be misleading.

The appropriate term is a partial eigenvector condition.

I suggest writing the result as

\\[ \boxed{ (5b)\text{ fails} \iff \exists\\,0\ne w\in W: \Phi(w)\in\mathbb Cw. } \\]

This is entirely intrinsic.

If a matrix extension \\(K_1\\) is used, then

\\[ \Phi(w)=K_1w,\qquad w\in W, \\]

but the result should not depend on which extension is chosen.

### Why this formulation is particularly useful

It turns the spectral obstruction into a geometric intersection problem.

Define

\\[ \mathcal E\_\Phi = \left\\{ [w]\in\mathbb P(W): \Phi(w)\in\mathbb Cw \right\\}. \\]

Then

\\[ \boxed{ (5b)\iff \mathcal E\_\Phi=\varnothing. } \\]

This is a very clean statement.

It also opens a possible connection to projective geometry: the condition describes the intersection of a projective subspace with a determinantal or eigenvector-type locus.

I would retain this formulation as the final version of the B.23–B.24 merger.

# V. One additional issue in D.1: quotient notation

There is a small but important point I would correct before the next submission.

In §II.1, the original map is

\\[ \Phi=\pi_C\circ A:Y\to Y/C. \\]

In §II.3, the expression

\\[ \pi\Phi(M) \\]

uses a map

\\[ \pi:Y\to Y/M. \\]

Strictly speaking, \\(\Phi(M)\\) consists of elements of \\(Y/C\\), not elements of \\(Y\\).

Because \\(C\subseteq M\\), there is a natural quotient map

\\[ \widehat\pi:Y/C\longrightarrow Y/M, \\]

given by

\\[ \widehat\pi(y+C)=y+M. \\]

This is well-defined precisely because \\(C\subseteq M\\).

The recursive construction should therefore be written as

\\[ C'=\widehat\pi(\Phi(M)), \qquad T'=\widehat\pi(\Phi(T)). \\]

Likewise,

\\[ \Phi'(y+M) = \widehat\pi(\Phi(y))+C'. \\]

This removes an ambiguity in the current notation.

It also makes the well-definedness proof completely transparent.

I recommend making this correction even if the underlying implementation already uses the natural quotient map.

# VI. What should be done next?

I would divide the next research round into two independent workstreams.

## Workstream A: Complete D.1

重点：证明尚未闭合

The direct lower bound is finished.

The remaining task is the recursive equality.

I suggest that the next proof document explicitly contain the following objects:

| Object            | Required information                          |
| ----------------- | --------------------------------------------- |
| \\(\Phi\\)        | Exact domain and codomain                     |
| \\(M\\)           | Exact definition and proof \\(C\subseteq M\\) |
| \\(\widehat\pi\\) | Natural quotient map \\(Y/C\to Y/M\\)         |
| \\(C'\\)          | Image of \\(M\\) under the induced map        |
| \\(T'\\)          | Image of \\(T\\) under the induced map        |
| \\(\Phi'\\)       | Exact quotient-map definition                 |
| \\(\sigma\\)      | Domain, codomain and defining equation        |
| Interval lemma    | Exact statement and proof                     |
| Lift              | Proof that the lifted subspace is feasible    |

The most important item is the defining equation for \\(\sigma\\).

I would like to see it written as an explicit linear-algebraic identity, rather than as an informal statement that a correction exists.

Once that identity is established, the proof should be straightforward to formalize.

My current verdict on D.1:

- Direct lower bound: accepted.
- Empty-family convention: accepted.
- Well-definedness of the further quotient map: accepted, with the notation correction above.
- Recursive \\((\ge)\\) direction: plausible, but requires the exact quotient feasibility verification.
- Recursive \\((\le)\\) direction: not yet proved.

Do not let the unresolved recursive equality delay publication of the direct lower-bound theorem.

## Workstream B: Complete B.13a

建议先完成第一引理

The first objective should be only

\\[ \boxed{ \dim\mathfrak I \le \max\\{v,\dim\mathcal B+k-1\\}. } \\]

Do not yet attempt to derive the global infeasibility criterion.

I suggest the following proof sequence:

1. Establish that the wedge equation defines a closed algebraic variety.
2. Identify the base locus.
3. Restrict to the complement of the base locus and establish the graph/fiber description.
4. Bound the dimension of the incidence set over the base locus.
5. Combine the two strata.

This is a self-contained projective-geometric argument.

Afterward, the coverage theorem can be developed separately.

# VII. Suggested revised status for the project registry

I would update the status of the three disputed propositions as follows.

| Claim                      | Revised status                     | What remains                                |
| -------------------------- | ---------------------------------- | ------------------------------------------- |
| B.4                        | Paper proof accepted; Lean pending | Correct right-eigenvector formalization     |
| D.1 lower bound            | Proof complete                     | None                                        |
| D.1 recursive identity     | Partial                            | Interval inclusion and \\(\sigma\\)-lifting |
| B.13 homogeneous incidence | Construction partially corrected   | Base-locus dimension proof                  |
| B.13 fiber lemma           | Requires revision                  | Separate zero and nonzero pencil images     |
| B.13 coverage theorem      | Open                               | Constructible-image dimension argument      |
| B.16–B.17–B.21             | Merger accepted                    | Consolidate hypotheses and notation         |
| B.23–B.24                  | Merger accepted                    | Use partial eigenvector terminology         |



26_d1_b13_revisions.md

26_d1_b13_revisions.md

26_d1_b13_revisions.md



# VIII. Final research judgment

There is something important about the direction of this project that I want to emphasize.

The recent revisions have improved not only individual proofs but also the organization of the mathematical theory.

Previously, several results were presented as separate technical observations:

- Permanent kernels.
- Quotient-pencil injectivity.
- Right minimal indices.
- Spectral rank loss.
- Polynomial nullspace structure.
- Intrinsic eigenvector obstructions.

They are now being organized around two central mathematical objects:

\\[ \boxed{ \overline N_Z(\lambda):V/S\to X/Z } \\]

and

\\[ \boxed{ \Phi:W\to\mathbb C^q. } \\]

This is a substantial improvement.

The first describes the quotient-pencil obstruction. The second describes the spectral obstruction intrinsically.

I would make these the organizing principles of the relevant chapters rather than retaining the original sequence of independent technical propositions.

My final recommendations are:

1. Accept the B.4 correction.
2. Accept the D.1 direct lower-bound proof as complete.
3. Do not accept the D.1 recursive equality until the \\(\sigma\\)-construction is explicitly proved.
4. Accept the three-stage strategy for B.13, but correct the infinity-point statement and incorporate the base locus into the incidence dimension estimate.
5. Proceed with both theorem mergers.

The next mathematical task I would prioritize is B.13a, because its corrected incidence construction is now precise enough to admit a clean, independent algebraic-geometric proof. D.1's lower bound can meanwhile be finalized without waiting for the recursive argument.

One important principle for the remainder of the project: keep the distinction between proved, formally verified, numerically tested, and conjectured explicit in the registry. Your recent correction of B.4 is an excellent example of why this discipline matters.