I have reviewed the report. The central issue in II.5 is not, by itself, a contradiction in the definition of functional observability: functional observability is an algebraic condition on the row space of the observability matrix, whereas (5b) imposes an additional condition at every finite \\(\lambda\\), including \\(\lambda=0\\).

In particular, if (5b) is intended exactly as written, then \\(\lambda=0\\) must be included. A singular \\(A\\) is not automatically excluded by that definition, but it can create a genuine obstruction at zero. There is a simple structural test for this at the maximal order \\(q=n-p\\), which I will apply to your matrices below.

05_integer_obstruction_occlusion_anomaly.md

# Overall verdict

The report contains two valuable developments—the integer obstruction formula and the projective-geometric viewpoint on spectral failure—but II.5 is resolved by an explicit order-three augmentation that your search has missed.

In fact, I found a particularly simple witness: its third row is just the second row of \\(CA\\). It satisfies both (5a) and the stronger version of (5b), for every complex \\(\lambda\\).

There are also two mathematical qualifications to make to II.3: a nonzero kernel vector does not always imply a rank drop below \\(h\\), and a rational map between higher-dimensional projective spaces does not automatically extend to a morphism.

I'll go through the six questions and then give the exact correction to II.5.

# 1. Q1 — The anomaly in II.5

## 1.1 Is \\(\lambda=0\\) included?

Under the definition in your report,

\\[ \operatorname{rank} \begin{bmatrix} \lambda\mathcal L-\mathcal LA\\\CA\\\C \end{bmatrix} = \operatorname{rank} \begin{bmatrix} \mathcal L\\\CA\\\C \end{bmatrix} \qquad \forall\lambda\in\mathbb C, \\]

zero is unquestionably included. There is no justification for excluding it.

There is, however, a distinction worth preserving when comparing this condition with classical functional-observer existence theorems. For example, the functional-observability result described in the 2021 PNAS paper tests its corresponding spectral rank condition at every eigenvalue of \\(A\\), rather than at every \\(\lambda\in\mathbb C\\). Since zero is an eigenvalue of your matrix \\(A\\), it is still tested in this example.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://pmc.ncbi.nlm.nih.gov\&sz=32)

PMC



Thus, the two formulations should not be silently identified:

- Your (5b): rank equality for every \\(\lambda\in\mathbb C\\).
- The cited classical condition: rank equality at every \\(\lambda\in\sigma(A)\\).

The former is stronger in general.

## 1.2 The claimed nonexistence is false: here is an exact order-three solution

For the matrices in II.5, take

\\[ \boxed{ \mathcal L\_\*= \begin{pmatrix} -1&0&0&0&-1&0&0\\\ 1&0&0&0&0&0&1\\\ 1&0&0&-1&0&-1&1 \end{pmatrix}. } \\]

The first two rows are exactly \\(L_0\\). The third row is the second row of \\(CA\\).

The following identities hold:

\\[ \operatorname{rank}[C;\mathcal L\_\*]=5, \\]

\\[ \operatorname{rank} \begin{bmatrix} \mathcal L\_\*\\\CA\\\C \end{bmatrix}=5, \\]

and

\\[ \operatorname{rank} \begin{bmatrix} \mathcal L\_\*A\\\ \mathcal L\_\*\\\ CA\\\C \end{bmatrix}=5. \\]

Consequently, (5a) holds.

More importantly, define

\\[ Q\_\*(\lambda)= \begin{bmatrix} \lambda\mathcal L\_\*-\mathcal L\_\*A\\\ CA\\\C \end{bmatrix}. \\]

Two of its \\(5\times5\\) minors are identically constant:

- Rows \\(1,2,3,4,7\\), columns \\(1,2,4,5,7\\): determinant \\(-1\\).
- Rows \\(1,2,3,4,7\\), columns \\(1,2,5,6,7\\): determinant \\(+1\\).

Therefore,

\\[ \operatorname{rank}Q\_\*(\lambda)\ge 5 \qquad\forall\lambda\in\mathbb C. \\]

On the other hand, (5a) implies that every row of \\(Q\_\*(\lambda)\\) belongs to the row space of \\([\mathcal L\_\*;CA;C]\\), which has dimension five. Hence

\\[ \operatorname{rank}Q\_\*(\lambda)\le5. \\]

Combining the two inequalities,

\\[ \boxed{ \operatorname{rank}Q\_\*(\lambda)=5 =\operatorname{rank} \begin{bmatrix} \mathcal L\_\*\\\CA\\\C \end{bmatrix} \quad\forall\lambda\in\mathbb C. } \\]

This proves (5b), including at \\(\lambda=0\\).



Exact resolution

&#x20;The example in II.5 has an admissible augmentation at order \\(q=3\\). In fact,



\\[ \boxed{q\_{\min}=3.} \\]

## 1.3 There is also an error in the reported order-two rank

Your table states that at \\(q=2\\),

\\[ h=\operatorname{rank}[L_0;CA;C]=6. \\]

For the displayed matrices, the exact rank is instead

\\[ \boxed{\operatorname{rank}[L_0;CA;C]=5.} \\]

The rank of the left side of (5a) is also five, so (5a) does hold for \\(L_0\\).

The maximal-minor gcd of the pencil at \\(q=2\\), using the correct target rank \\(h=5\\), is

\\[ \boxed{\lambda-1.} \\]

Thus the order-two augmentation fails (5b) at \\(\lambda=1\\), not because \\(h=6\\).

This is a concrete reason to audit the rank calculations in the code before using the reported order-by-order table.

## 1.4 Why did the search miss the order-three solution?

The nullspace corresponding to \\(\mathcal L\_\*\\) is

\\[ \ker[C;\mathcal L\_\*] = \operatorname{span} \left\\{ \begin{pmatrix}0\\\0\\\1\\\0\\\0\\\0\\\0\end{pmatrix}, \begin{pmatrix}0\\\0\\\0\\\\-1\\\0\\\1\\\0\end{pmatrix} \right\\}. \\]

Meanwhile,

\\[ \ker[C;L_0] = \operatorname{span}\\{e_3,e_4,e_6\\}. \\]

So the successful two-dimensional nullspace is

\\[ Z\_\*=\operatorname{span}\\{e_3,-e_4+e_6\\}. \\]

Your report says that only three candidates were examined at order three. That is not an exhaustive search over the two-dimensional subspaces of this three-dimensional \\(K\\). The missing solution is an explicit counterexample to the completeness of that candidate enumeration.

## 1.5 What about the zero eigenvalue and the order-five failures?

There is a genuine zero-eigenvalue obstruction at order five, but it does not imply that every order fails.

Indeed, for the displayed \\(A,C\\),

\\[ e_3\in\ker A\cap\ker C. \\]

At \\(q=5=n-p\\), the matrix \\([C;\mathcal L]\\) is square and nonsingular for a full complement \\(\mathcal L\\), and

\\[ h=7=n. \\]

For every such \\(\mathcal L\\),

\\[ Q\_{\mathcal L}(0)e_3 = \begin{bmatrix} -\mathcal LAe_3\\\CAe_3\\\Ce_3 \end{bmatrix} =0. \\]

Since \\(e_3\ne0\\), \\(Q\_{\mathcal L}(0)\\) cannot have rank seven. Thus every order-five complement fails (5b) at zero. This part of the report has a simple structural explanation.

The mistake was to extrapolate this order-five failure to all orders.

## 1.6 The corrected order spectrum

The relevant observability rank is \\(n_0=5\\), so

\\[ n_0-p=3. \\]

The useful interval is therefore \\(q=2,3\\), and we have now established:

| Order       | Result                                                                                                       |
| ----------- | ------------------------------------------------------------------------------------------------------------ |
| \\(q=2\\)   | (5a) holds, but (5b) fails at \\(\lambda=1\\)                                                                |
| \\(q=3\\)   | Both (5a) and (5b) hold for every \\(\lambda\in\mathbb C\\)                                                  |
| \\(q=4,5\\) | Outside the interval \\(q_0\le q\le n_0-p\\); order five has the zero-eigenvalue obstruction described above |

The claim in II.5 that no admissible order exists must be withdrawn.

# 2. Q2 — The integer criterion

I agree that II.1 is a useful result, and its derivation is sound under the stated decomposition.

You have

\\[ \mathcal Z^\perp=K^\perp+V', \qquad \dim V'=q-r, \\]

and

\\[ S=\operatorname{row}[C;L_0]+W. \\]

Since \\(W\subseteq S\\),

\\[ \begin{aligned} h &=\dim(\mathcal Z^\perp+W)\\\ &=\dim(K^\perp+V'+W)\\\ &=\dim(S+V')\\\ &=\dim S+\dim\pi(V'). \end{aligned} \\]

Thus

\\[ \boxed{h=s_0+\dim\pi(V').} \\]

The integer obstruction \\(h\ge q+r_1\\) is therefore equivalent to

\\[ \boxed{\dim\pi(V')\ge q+r_1-s_0.} \\]

This is more informative than merely restating the rank inequality: it isolates the contribution of the augmentation from the fixed subspace \\(S\\).

### Is it already in the literature?

I would distinguish two things:

1. The underlying identity for the dimension of a sum of subspaces is standard linear algebra.
2. The use of \\(S\\), the quotient projection \\(\pi\\), and the decomposition of the augmentation space to obtain an order-dependent integer obstruction is a potentially useful formulation of your problem.

The 2026 Fernando preprint already develops a nullspace-based, order-by-order characterization of algebraic and spectral feasibility. That makes it important to compare your formula with its nullspace parametrization before making a novelty claim.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://papers.cool\&sz=32)

Cool Papers - Immersive Paper Discovery



I would not claim that the dimension identity itself is a new theorem. The stronger contribution would be a theorem stating exactly when the integer obstruction is unavoidable for an entire order, and how that interacts with the spectral condition.

One qualification: the condition

\\[ V'\cap S=0 \\]

must be established for the family of complements under discussion. It is not automatic merely from the dimensions of \\(V'\\) and \\(S\\).

# 3. Q3 — Is the boundary \\(r_1=p+r\\) structurally special?

It is special, but I do not think your present experiments justify the stronger claim that spectral failure can occur only there.

Recall

\\[ \dim V=n-r_1,\qquad \dim K=n-p-r. \\]

Hence

\\[ \dim V-\dim K=p+r-r_1. \\]

The boundary \\(r_1=p+r\\) is precisely the equal-dimension case.

However, the dimension argument does not establish that dominance is possible only on this boundary.

- If \\(r_1\<p+r\\), then \\(\dim V>\dim K\\). A rational map from a larger projective space to a smaller one can certainly be dominant.
- If \\(r_1=p+r\\), then the projective spaces have equal dimension. A nonconstant rational map from \\(\mathbb P^1\\) to \\(\mathbb P^1\\), for example, is surjective.
- If \\(r_1>p+r\\), then \\(\dim V<\dim K\\). Dominance is impossible, but the image may still intersect every admissible subspace if those subspaces have sufficiently large dimension.

Thus the boundary is the natural equal-dimension case, not the only case in which total occlusion could occur.

My interpretation is that your observed boundary phenomenon is a promising conjecture about the particular algebraic structure of \\(\Phi\\), rather than a consequence of projective dimension counting alone.

05_integer_obstruction_occlusion_anomaly.md

# 4. Q4 — Is occlusion a useful general obstruction?

Yes. I think this is one of the strongest directions in the report, but II.3 needs a precise correction.

## 4.1 The rank-drop step needs \\(h=n\\)

You write that if \\(z(x)\in\mathcal Z\\), then

\\[ Q\_{\mathcal L}(\lambda(x))x=0, \\]

and conclude

\\[ \operatorname{rank}Q\_{\mathcal L}(\lambda(x))\<h. \\]

That conclusion is valid if \\(h=n\\), because the pencil has \\(n\\) columns and the reference rank is \\(n\\). A nonzero kernel vector then forces a rank drop below \\(n\\).

But if \\(h\<n\\), a matrix can have a nonzero kernel and still have rank \\(h\\). Therefore,

\\[ Q\_{\mathcal L}(\lambda)x=0,\quad x\ne0 \\]

does not by itself imply that (5b) fails.

This distinction is essential. The occlusion theorem should explicitly assume

\\[ \boxed{h=n\quad\text{for every admissible }\mathcal Z \text{ at the order under consideration}.} \\]

If \\(h=n\\) holds only for some candidates, the argument only proves failure for those candidates.

## 4.2 A stronger geometric criterion than surjectivity

There is a useful improvement to the surjectivity condition.

Let

\\[ Y=\overline{\Phi(\mathbb P(V))} \subseteq\mathbb P(K) \\]

be the projective closure of the image, and put

\\[ m=\dim Y,\qquad k=\dim K. \\]

Every admissible \\(\mathcal Z\\) is a \\(d\\)-dimensional subspace of \\(K\\), so \\(\mathbb P(\mathcal Z)\\) is a projective \\((d-1)\\)-plane in \\(\mathbb P(K)\\), whose dimension is \\(k-1\\).

The projective dimension theorem says that two projective varieties in \\(\mathbb P^{k-1}\\) must intersect if the sum of their dimensions is at least \\(k-1\\). Consequently, if

\\[ m+(d-1)\ge k-1, \\]

or equivalently

\\[ \boxed{m\ge k-d=q-r,} \\]

then \\(Y\\) meets every projective \\((d-1)\\)-plane in \\(\mathbb P(K)\\).

Thus, subject to the full-rank assumption \\(h=n\\), you can replace the requirement that \\(\Phi\\) be surjective by the weaker sufficient condition

\\[ \boxed{ \dim\overline{\Phi(\mathbb P(V))}\ge q-r. } \\]

This is potentially important: the image need not fill all of \\(\mathbb P(K)\\) to intersect every admissible nullspace.

For the special case \\(\dim V=\dim K=2\\), a nonconstant map \\(\mathbb P^1\to\mathbb P^1\\) has one-dimensional image, so the condition is automatic. That is exactly the situation in which your surjectivity argument is particularly clean.

## 4.3 A technical correction about rational maps

The statement

> A rational map between projective spaces extends to a morphism

is false in general when the domain has dimension greater than one.

A rational map from \\(\mathbb P^1\\) to a projective variety does extend across its finitely many indeterminacy points, so your argument for a map \\(\mathbb P^1\to\mathbb P^1\\) is valid. In higher dimensions, however, a rational map can have a genuine indeterminacy locus.

For the general theorem, work with the closure of the image of the domain of definition, as above, rather than assuming an extension to a morphism.

05_integer_obstruction_occlusion_anomaly.md

# 5. Q5 — Where should the research effort go?

My recommended order is:

## First: make the per-order algorithm mathematically complete

The II.5 miss is a warning that the candidate-generation procedure is not yet exhaustive. Before investigating statistical patterns, make sure the parametrization covers the full Grassmannian family of admissible nullspaces.

For each order, I would separate the computation into:

1. The complete parameter space of admissible \\(\mathcal Z\\).
2. The algebraic condition (5a).
3. The integer obstruction \\(h\ge q+r_1\\).
4. The spectral condition, checked exactly on the remaining candidates.

The order-three witness above should become a permanent regression test.

## Second: develop the occlusion criterion

This is the most promising theoretical direction once the enumeration is reliable.

I would formulate a theorem along these lines:

> Suppose \\(h=n\\) for every admissible augmentation at order \\(q\\). Let \\(Y\\) be the projective closure of the image of the bad-point map \\(\Phi\\). If \\(\dim Y\ge q-r\\), then every admissible nullspace intersects the bad-point locus, and no augmentation at order \\(q\\) satisfies (5b).

This gives a clean sufficient condition for whole-family spectral infeasibility.

It is also computationally meaningful: the dimension of the image closure can, in principle, be studied through elimination theory and rational-map calculations.

## Third: investigate the off-boundary cases

Do not yet try to prove that spectral feasibility always holds off the boundary. The current sample is too small to support such a universal statement, and the dimension argument does not establish it.

Instead, classify the possible dimensions of the image closure \\(Y\\) and compare them with \\(q-r\\). This is more precise than dividing cases only according to whether \\(r_1=p+r\\).

# 6. Q6 — What is worth writing up now?

Here is my assessment.

| Result                                       | Assessment                                       | Recommendation                                   |
| -------------------------------------------- | ------------------------------------------------ | ------------------------------------------------ |
| Integer criterion II.1                       | Solid and useful                                 | Include                                          |
| Integer explanation of the published example | Potentially strong                               | Include after proving the family-wide claims     |
| Occlusion mechanism II.3                     | Promising, but needs the \\(h=n\\) qualification | Include as a theorem with corrected hypotheses   |
| Boundary observation II.4                    | Empirical only                                   | Present as a conjecture or numerical observation |
| No-admissible-order anomaly II.5             | False as currently stated                        | Replace with the explicit order-three solution   |

I would not write a paper claiming that II.5 is a counterexample to functional-observer existence. It is not.

The most compelling package at this stage is:

1. An exact integer obstruction criterion.
2. A geometric description of when that obstruction is unavoidable across an entire order.
3. A corrected occlusion theorem for spectral infeasibility.
4. Exact examples distinguishing integer obstruction from spectral obstruction.
5. A carefully qualified discussion of the boundary phenomenon.

The general functional-observability condition and the observer-design rank conditions are established topics, so the paper's contribution should be framed around the order-by-order geometry of admissible augmentations, not around rediscovering functional observability itself.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://pmc.ncbi.nlm.nih.gov\&sz=32)

PMC+1



# 7. Immediate corrections to make in the report and code

I would make these changes before the next round of experiments:

- II.5: Replace the claimed nonexistence result with the explicit \\(\mathcal L\_\*\\) above.
- The \\(q=2\\) row: Correct \\(h\\) from 6 to 5; verify that the pencil's maximal-minor gcd is \\(\lambda-1\\).
- The \\(q=3\\) row: Add \\(\mathcal L\_\*\\) as an exact feasible witness. The previous three-candidate search was incomplete.
- The \\(q=5\\) discussion: Retain the zero-eigenvalue obstruction, but state that it is an order-specific result, not a proof of nonexistence at every order.
- II.3: Explicitly assume \\(h=n\\) for every candidate to which the universal occlusion conclusion is applied.
- II.3 generalization: Replace the blanket rational-map extension claim with an image-closure argument.
- II.4: Keep the boundary observation empirical until it is supported by a structural theorem or a much broader exact analysis.

The key new benchmark is the order-three matrix \\(\mathcal L\_\*\\). It is especially useful because the proof of (5b) does not depend on numerical root finding or a numerical gcd: two constant maximal minors certify full rank for every complex \\(\lambda\\).

My strongest recommendation: fix the candidate-generation and rank-verification code first, then use the projective image-dimension criterion to develop the occlusion theory. That gives you a much firmer foundation than trying to prove the current boundary conjecture directly.