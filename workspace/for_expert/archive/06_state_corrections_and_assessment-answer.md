I have reviewed the revised note. The corrections in II.A are important, and the new order-three certificate is a substantial improvement. I would now make one further conceptual move: there is an exact formulation of (5b) on \\(V=\ker[C;CA]\\), parametrized by \\(\mathcal Z\\), that works even when \\(h\<n\\). It is stronger than the earlier bad-point/occlusion argument and directly addresses your Q1.

The key is to quotient out the fixed row space \\(W=\operatorname{row}[C;CA]\\) before testing the pencil. This also gives a useful way to separate what depends on the chosen basis \\(\mathcal L\\) from what depends only on its nullspace.

# 1. Q1 — An exact condition on \\(\mathcal Z\\), including \\(h\<n\\)

This question has a clean answer, and it is already very close to a theorem in Fernando's 2026 preprint. More importantly, it gives you the exact formulation you were looking for.

Let \\(V\\) be a full-column-rank basis matrix for

\\[ \ker\begin{bmatrix}C\\\CA\end{bmatrix}, \\]

and let \\(Z\\) be a full-column-rank basis matrix for

\\[ \mathcal Z=\ker\begin{bmatrix}C\\\\\mathcal L\end{bmatrix}. \\]

Assume (5a). Then (5b) is equivalent to

\\[ \boxed{ \operatorname{rank}\begin{bmatrix}(\lambda I-A)V&Z\end{bmatrix} = \operatorname{rank}\begin{bmatrix}V&Z\end{bmatrix} \quad\forall\lambda\in\mathbb C. } \tag{Q1.1} \\]

This is precisely the nullspace pencil characterization in Theorem 4 of the 2026 preprint. It is a condition on \\(\mathcal Z\\), not on a particular choice of basis \\(\mathcal L\\), and it does not require \\(h=n\\).&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



## 1.1 Quotient-space interpretation

Let

\\[ \pi_Z:\mathbb C^n\longrightarrow\mathbb C^n/\mathcal Z \\]

be the quotient map. Since

\\[ \operatorname{rank}[M\ Z] =\dim\mathcal Z+\operatorname{rank}(\pi_ZM), \\]

(Q1.1) is equivalent to

\\[ \boxed{ \operatorname{rank}\left( \pi_Z\circ(\lambda I-A)|\_V \right) = \operatorname{rank}\left(\pi_Z|\_V\right) \quad\forall\lambda\in\mathbb C. } \tag{Q1.2} \\]

This is perhaps the most natural answer to the question in your Part III: it is a pencil of maps from \\(V\\) into \\(\mathbb C^n/\mathcal Z\\), with \\(\mathcal Z\\) as the parameter.

There is an even more geometric formulation. Under (5a),

\\[ \ker(\pi_Z|\_V) \subseteq \ker\big(\pi_Z\circ(\lambda I-A)|\_V\big). \\]

Therefore equality of ranks in (Q1.2) is equivalent to equality of these kernels:

\\[ \boxed{ \\{v\in V:(\lambda I-A)v\in\mathcal Z\\} = V\cap\mathcal Z \quad\forall\lambda\in\mathbb C. } \tag{Q1.3} \\]

In words:

> No vector in \\(V\\) outside \\(\mathcal Z\\) may be mapped by \\(\lambda I-A\\) into \\(\mathcal Z\\), for any finite complex \\(\lambda\\).

This is the exact version of the bad-point idea. It handles \\(h\<n\\) because it compares the dimension of the additional kernel with the reference kernel \\(V\cap\mathcal Z\\), rather than relying on a nonzero kernel vector to force a rank drop below \\(h\\).

## 1.2 How this improves the occlusion argument

Your previous construction looks for \\(v\in V\\) and \\(\lambda\\) such that

\\[ (\lambda I-A)v\in\mathcal Z, \qquad v\notin\mathcal Z. \\]

That is exactly a violation of (Q1.3).

So the natural bad set is not necessarily a projective image in \\(\mathbb P(K)\\). It is the incidence set

\\[ \mathfrak B= \left\\{ (\mathcal Z,[v],\lambda): v\in V\setminus\mathcal Z,\  (\lambda I-A)v\in\mathcal Z \right\\}. \\]

The question of whether an order is feasible becomes:

\\[ \text{Does there exist an admissible }\mathcal Z \text{ whose fibre contains no point of }\mathfrak B? \\]

This formulation:

- works for \\(r\ge2\\);
- works for \\(h\<n\\);
- does not require a scalar \\(\lambda(x)=L_0Ax/L_0x\\);
- is invariant under the choice of basis for \\(\mathcal Z\\).

Recommendation: make (Q1.1), or equivalently (Q1.2), your primary spectral condition. Keep the projective occlusion theorem as a special sufficient condition, not as the general formulation.

# 2. Q2 — Is the integer criterion already known?

I would separate the novelty of the formula from the novelty of its use.

Your identity

\\[ h=s_0+\dim\pi(V') \\]

is a direct application of the dimension formula for subspaces. The threshold

\\[ h\ge q+r_1 \iff \dim\pi(V')\ge q+r_1-s_0 \\]

is then an exact reformulation of the integer obstruction.

I have not found an established observer-theory term for this particular quotient-space criterion in the sources examined. However, it is closely connected to the minimal-index argument already used in your work: the spectral condition requires the total left minimal-index degree to be sufficiently large, while the pencil dimensions constrain the number of positive left minimal indices.

The 2026 preprint already provides:

- a complete nullspace parameterization at each admissible order;
- a matrix-pencil test for the spectral condition;
- a finite Grassmann-chart parameterization of all candidate nullspaces.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

  arXiv+1



What I do not see stated there in your precise form is the uniformity result:

\\[ V'\cap S=0 \quad\Longrightarrow\quad h=s_0+q-r, \\]

so that the integer obstruction is constant over the entire family at that order.

That is the part I would emphasize. It says that, on an order where the intersection condition holds throughout the admissible family, the integer obstruction can be decided before searching for any augmentation.

There is one important wording issue. Your report correctly says that \\(V'\cap S=0\\) must be checked. I would strengthen this in the paper:

> If \\(V'\cap S=0\\) for every admissible \\(V'\\) at a given order, then the integer obstruction is uniform over that order.

Do not say it is a property of the order without retaining that hypothesis.

My assessment: the dimension identity is elementary; the family-uniformity corollary is a useful structural result. Its novelty claim should be modest and should be checked against the detailed nullspace parametrization in the Fernando preprint.

# 3. Q3 — Complexity and possible hardness results

I did not find an established NP-hardness theorem for your exact minimum-order problem, including the restricted cases you mention.

There is a nearby but different result: minimum sensor placement for structural functional observability has been shown to be NP-hard. That problem selects sensors from a candidate set; it is not the problem of finding a minimum-dimensional augmented functional matrix \\(\mathcal L\\) for fixed \\(A,C,L_0\\). The hardness result cannot simply be transferred.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://ieeexplore.ieee.org\&sz=32)

IEEE Xplore



I suggest formulating your problem as an algebraic feasibility problem first.

## 3.1 A natural algebraic formulation

Fix an order \\(q\\), and parameterize the admissible \\(d\\)-dimensional nullspaces using Grassmann charts, where

\\[ d=n-p-q. \\]

The algebraic condition (5a) is a collection of polynomial rank constraints in the chart parameters.

For the spectral condition, use (Q1.1). Equivalently, take all maximal minors of

\\[ P_Z(\lambda)= \begin{bmatrix} (\lambda I-A)V&Z \end{bmatrix}. \\]

The spectral condition requires that these maximal minors have no common finite zero. Over \\(\mathbb C\\), this is equivalent to their polynomial gcd being a nonzero constant.

A univariate polynomial gcd condition can be expressed through a Bézout identity, with bounded-degree polynomial coefficients. Consequently, after introducing auxiliary variables for those coefficients, the fixed-order existence problem can be represented by polynomial equations and nonvanishing constraints in the Grassmann-chart variables.

For rational real input matrices and real candidate augmentations, this places the fixed-order decision problem naturally in the framework of existential real algebraic feasibility. For genuinely complex input and complex candidate matrices, the analogous framework is existential algebraic geometry over \\(\mathbb C\\).

This is a useful upper-level complexity description. It does not establish hardness.

## 3.2 Which restrictions should you investigate?

I would prioritize them as follows:

1. Fixed \\(r\\), variable \\(n\\). This is the most natural restriction because the number of prescribed functionals is often small in applications.
2. Coordinate-subspace restrictions on \\(\mathcal L\\). This may expose a combinatorial core and make a reduction more manageable.
3. Companion-form \\(A\\). This is mathematically attractive, but I would not start here unless it simplifies the pencil structure substantially.

A promising intermediate goal is to determine whether the fixed-order problem is polynomial-time solvable for \\(r=1\\), or whether even that restricted case can encode a difficult algebraic feasibility problem.

I would not announce an NP-hardness conjecture yet. First identify a concrete reduction target and show how its variables and constraints are represented by your nullspace pencil.

# 4. Q4 — Is \\(n_0-p\\) always the correct upper endpoint?

Yes, under functional observability

This question has a definite answer in the 2026 preprint.

Theorem 7 of Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger establishes that the terminal order

\\[ \boxed{q=n_0-p} \\]

is spectrally feasible under functional observability. The paper then uses this result to establish that the minimum feasible observer order exists and satisfies

\\[ \boxed{q\_{\min}\le n_0-p.} \\]

It also proves that the algebraic condition is feasible at every order in

\\[ [q_0,n_0-p], \\]

while explicitly warning that joint algebraic-spectral feasibility need not be an interval.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+2



This distinction is essential:

- Algebraic feasibility has no gaps in the stated interval.
- Spectral feasibility can fail at intermediate orders.
- The terminal order is nevertheless spectrally feasible.

Thus your order interval is correct, provided the assumptions and the same notion of functional observability as in the preprint are used.

Your earlier search over \\([q_0,n-p]\\) was too broad when \\((A,C)\\) is not completely observable. The correct upper endpoint is \\(n_0-p\\), not \\(n-p\\).

# 5. Q5 — Terminology

I recommend using terminology that describes the mathematical mechanism without suggesting that the obstruction is merely a numerical accident.

| Your term            | Suggested term                                      | Reason                                                                                                 |
| -------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Integer obstruction  | Dimension obstruction or rank-count obstruction     | The decisive condition is a rank threshold                                                             |
| Spectral obstruction | Finite-eigenvalue obstruction or pencil obstruction | Failure occurs when the pencil loses normal rank at a finite \\(\lambda\\)                             |
| Whole-family failure | Uniform infeasibility at order \\(q\\)              | Every admissible nullspace at that order fails                                                         |
| Occlusion            | Incidence obstruction                               | The failure is expressed by an incidence relation between \\(V\\), \\(\mathcal Z\\), and \\(\lambda\\) |

My preference is:

- dimension obstruction for \\(h\ge q+r_1\\);
- spectral obstruction for \\(h\<q+r_1\\) but \\(d\_{\rm fin}>0\\);
- uniform spectral infeasibility when every admissible nullspace fails the spectral test.

You can introduce “occlusion” as an informal geometric term, but I would not make it the principal terminology of the paper. The incidence formulation in Section 1 is more precise and general.

# 6. Q6 — Is there enough for a short note?

Potentially yes, but I would not submit the present collection of results without a careful novelty comparison.

The 2026 Fernando preprint already covers a substantial amount of the surrounding territory:

- order range \\(q_0\\) through \\(n_0-p\\);
- fixed-order nullspace characterization;
- spectral matrix-pencil characterization;
- finite Grassmann-chart parameterization;
- complete order-spectrum characterization;
- an example with two consecutive infeasible orders.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

  arXiv+1



That means a note whose main contribution is simply “we also characterize all admissible nullspaces at each order” would have a serious overlap problem.

## My suggested short-note structure

I would organize it around two results.

Result 1: The dimension obstruction and its uniformity.

Prove

\\[ h=s_0+\dim\pi(V') \\]

and derive the exact order-uniform criterion under \\(V'\cap S=0\\). Then use the published example as a clean illustration of a failure explained entirely by dimensions.

Result 2: A genuinely different spectral obstruction.

Present the \\(n=6\\) example where the integer obstruction is impossible, but every admissible nullspace at \\(q_0\\) fails the spectral condition. Give:

- the exact matrices;
- the exact nullspace and map calculations;
- the proof that the image is surjective in the relevant \\(\mathbb P^1\\) case;
- the hypothesis \\(h=n\\);
- the resulting whole-family infeasibility theorem.

This second result is more interesting than a further random example because it separates the dimension obstruction from a genuinely spectral mechanism.

I would leave the boundary statistics in a short numerical section, explicitly labelled as exploratory evidence. I would not make the complexity question a central result until you have a theorem or reduction.

One qualification: before claiming that the note is ready, resolve the issue with the finite rational-grid scans discussed in Section 8 below. A finite grid is not a complete Grassmannian enumeration.

# 7. Q7 — Should the Toeplitz criterion appear in the paper?

Yes. I would include it as a theorem or proposition, not hide it as an implementation detail.

The Toeplitz criterion and the maximal-minor gcd test do different jobs.

| Method                 | What it certifies                                 | Main value                              |
| ---------------------- | ------------------------------------------------- | --------------------------------------- |
| Block-Toeplitz nullity | Left minimal indices and their degrees            | Structural information about the pencil |
| Maximal-minor gcd      | Absence or presence of finite elementary divisors | Direct spectral feasibility test        |

For the Toeplitz criterion, present:

1. The precise definition of the block-Toeplitz matrix.
2. The definition of \\(\nu_d\\).
3. The identity\
   \\[\
   \nu_s=(s+1)m-s,\qquad m=q+2p-h,\
   \\]\
   with the hypotheses under which it holds.
4. The second-difference formula recovering the left minimal-index multiplicities:\
   \\[\
   \nu_d-2\nu\_{d-1}+\nu\_{d-2}.\
   \\]
5. The proof that the criterion is equivalent to the absence of finite elementary divisors in your pencil setting.

I would put the full block construction and proof in an appendix if it takes too much space.

The maximal-minor gcd is more immediately recognizable to readers familiar with polynomial matrices. It should remain the independent certificate. The Toeplitz criterion has the advantage that it tells you more than whether the pencil has a finite rank drop: it reveals the left minimal-index structure.

One caution: the reported 66/66 agreement with the Smith-form route is excellent regression evidence, but it is not a substitute for the mathematical equivalence proof. Also make clear that the Toeplitz identity uses the correct pencil normal rank and the correct indexing conventions for \\(\nu_d\\).

# 8. Q8 — Where could the checks still be systematically wrong?

I agree that the two risks you identified—\\(\lambda=0\\) and row/column conventions—deserve attention. But I would put completeness of the Grassmannian enumeration at the top of the audit list.

## 8.1 A rational grid is not a complete Grassmannian scan

Your report says that a complete scan of \\(\operatorname{Gr}(2,3)\\) uses three charts and a rational grid on each chart.&#x20;

06_state_corrections_and_assessment.md



The three standard charts do cover the Grassmannian. But a rational grid inside each chart does not cover the chart: each chart has continuously many points.

Even if the entries of the input matrices are rational, the admissible subspaces need not have rational coordinates. They may be defined over an algebraic extension, or form a positive-dimensional algebraic family.

Therefore:

- A rational grid can discover witnesses.
- It can test conjectures.
- It can provide a useful regression suite.
- It cannot, by itself, prove that exactly 18 admissible nullspaces exist or that the other nullspaces fail.

To make the enumeration exhaustive, you need to solve the polynomial rank constraints on every chart and prove that the resulting algebraic set has been completely described. Depending on the problem, that could use Gröbner bases, triangular decomposition, resultants, or real/complex quantifier elimination.

This is particularly important because the Fernando preprint already emphasizes that a finite collection of Grassmann charts, with an exact treatment of the parameters within each chart, is what establishes completeness.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



## 8.2 Distinguish real and complex candidate subspaces

Your problem is stated over \\(\mathbb C\\), but many of the computations appear to use rational or real candidates.

If the intended observer matrices must be real, then the search should be over real Grassmannian points, while the spectral parameter \\(\lambda\\) must still range over \\(\mathbb C\\).

If complex augmentation matrices are allowed, the candidate space is different.

These are not interchangeable. A complex feasible nullspace need not have a real representative satisfying the same constraints. State explicitly which field is used for the candidate matrices.

## 8.3 Verify the rank target in every pencil test

For

\\[ Q\_{\mathcal L}(\lambda)= \begin{bmatrix} \lambda\mathcal L-\mathcal LA\\\CA\\\C \end{bmatrix}, \\]

the target rank is

\\[ h=\operatorname{rank}[\mathcal L;CA;C]. \\]

The correct gcd test uses the \\(h\times h\\) minors. Using minors of an incorrect size can make the gcd result meaningless.

I would put the following assertions in the implementation:

\\[ \operatorname{normalrank}Q\_{\mathcal L}=h \\]

before computing the maximal-minor gcd, and verify that the gcd is computed from all nonzero minors of the correct size.

## 8.4 Keep the \\(\lambda=0\\) convention explicit

For pole assignability, the spectral domain is all of \\(\mathbb C\\), as stated in the 2026 preprint. Thus zero must be included. For detectability, the domain is different.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



The code should take the spectral domain as an explicit parameter, rather than silently excluding zero or testing only a selected list of eigenvalues.

## 8.5 Make the bad-point map fully explicit for \\(r\ge2\\)

Your report correctly recognizes that

\\[ \lambda(x)=\frac{L_0Ax}{L_0x} \\]

is not automatically meaningful when \\(L_0x\\) and \\(L_0Ax\\) are vectors in \\(\mathbb C^r\\).&#x20;

06_state_corrections_and_assessment.md



For the \\(n=6\\), \\(r=2\\) example, you need to exhibit the exact identity showing that, for every \\(x\in V\\) in the domain,

\\[ L_0Ax=\lambda(x)L_0x. \\]

Equivalently, the two vectors must be proportional. In coordinates, this means proving the relevant \\(2\times2\\) determinant vanishes identically on \\(V\\).

Also, in the general projective-image theorem, be careful about using the closure of the image. The projective dimension theorem guarantees an intersection with the closure \\(Y\\). If the rational map is not a morphism, that intersection need not lie in the actual image. To infer a genuine bad point, establish that the image is closed—for example, by proving that the map extends to a morphism—or separately prove that every relevant intersection is attained.

This does not invalidate your \\(\mathbb P^1\to\mathbb P^1\\) example if the map is correctly defined and extended there. It does limit the generality of the closure-based statement.

## 8.6 Add a compact set of exact consistency checks

For every candidate, I would verify:

1. \\(\operatorname{rank}[C;\mathcal L]=p+q\\).
2. \\(\dim\ker[C;\mathcal L]=n-p-q\\).
3. The nullspace basis satisfies \\(CZ=0\\) and \\(\mathcal LZ=0\\).
4. The algebraic condition is equivalent to the appropriate nullspace rank test.
5. The target pencil rank is exactly \\(h\\).
6. The maximal-minor gcd and Toeplitz test agree.
7. All calculations are performed over the intended coefficient field.

This is a much more valuable safeguard than merely increasing the number of random samples.

# 9. Final assessment

Your revised note is much stronger than the previous version. The false nonexistence claim has been removed, the order-three witness is exact, and the distinction between algebraic and spectral feasibility is now much clearer.

I would make three decisions:

1. Promote the quotient-nullspace pencil criterion (Q1.1) to the central spectral formulation. It answers your hardest open question and works beyond the \\(h=n\\) case. It is already present in the 2026 preprint, so cite it and build on it rather than claiming it as new.
2. Keep the dimension obstruction and its uniformity result as a principal contribution. It gives a simple order-level decision before the spectral search.
3. Keep the \\(n=6\\) whole-family spectral counterexample, but tighten the projective proof. In particular, prove the proportionality defining \\(\lambda(x)\\), and distinguish the image from its closure.

The single most important correction before writing is this:

Do not describe a finite rational-grid sample as a complete scan of a Grassmannian. Use exact algebraic chart analysis for completeness, and use rational grids only for exploration and testing.

With those changes, I think you have the basis for a focused research note. The strongest version would be a note about dimension obstructions and uniform spectral infeasibility in functional-observer order selection, rather than a general attempt to solve the full complexity problem immediately.