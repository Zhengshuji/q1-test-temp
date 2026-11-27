# Review of `23_controlled_profile.md`

This is a useful follow-up: it resolves the definition of \\(q_0\\), reports a controlled comparison with fixed \\(A\\), and implements several of the verification safeguards discussed previously. The controlled experiment is a genuine improvement over comparing unrelated random systems.

My assessment is that the new evidence supports a more focused research programme, but two mathematical definitions need clarification before the conclusions can safely be used in the paper:

1. The proposed row-by-row algorithm for \\(q_0\\) needs a precise specification. Its claimed interpretation as an algebraic minimum does not follow automatically from the description.
2. The definition of \\(q\_{\rm geom}\\) in the table is inconsistent with the \\(\rho=1\\) row: there is no intermediate stratum when \\(\rho=1\\), yet the table reports \\(q\_{\rm geom}=4\\).

There are also important qualifications concerning what the controlled experiment establishes, how to extend it, and how to formulate the complexity problem.

23_controlled_profile.md

## 1. Q0: the definition and the bound \\(q_0\leq n-p\\)

### 1.1 The bound is automatic under a precise interpretation

Let

\\[ R=\operatorname{row}C,\qquad \dim R=p. \\]

Suppose the algorithm processes the rows of \\(L_0\\), and counts a vector \\(\ell_iA^k\\) only when it is linearly independent modulo the span of:

- \\(R\\);
- all previously accepted vectors;
- the vectors accepted earlier in processing the current row.

Then every accepted vector contributes one new independent direction in the quotient space

\\[ \mathbb C^{1\times n}/R, \\]

whose dimension is \\(n-p\\).

Consequently,

\\[ \boxed{q_0\leq n-p.} \\]

This is a direct dimension argument. It does not require a separate observability theorem, provided the algorithm is defined exactly as above and the initial rows of \\(L_0\\) are independent modulo \\(R\\), which follows from

\\[ \operatorname{rank}\begin{bmatrix}C\\\L_0\end{bmatrix}=p+r. \\]

Thus, under this interpretation, the inequality should be a lemma, not an additional hypothesis of the terminal-order theorem.

### 1.2 But the stated greedy procedure does not yet establish that \\(q_0\\) is an algebraic minimum

This is the point I would investigate before accepting the terminology in Part I.

The report says that, for each row \\(\ell_i\\), one counts consecutive vectors

\\[ \ell_i,\quad \ell_iA,\quad \ell_iA^2,\quad\ldots \\]

and stops as soon as one fails to add a new direction modulo everything previously collected.

There is a potential problem: a dependence at one step does not necessarily imply dependence at all later steps, because the span of the previously collected vectors need not be \\(A\\)-invariant.

For example, it is possible that

\\[ \ell_iA\in W, \qquad \ell_iA^2\notin W, \\]

where \\(W\\) is the span of the vectors collected before processing \\(\ell_iA^2\\). The first relation does not imply that \\(W\\) is invariant under right multiplication by \\(A\\).

Therefore, stopping at the first dependent vector can omit a later independent direction.

There is a second issue: processing rows one at a time can make the result depend on the chosen basis and ordering of the rows of \\(L_0\\). A quantity called an algebraic minimum should be invariant under replacing \\(L_0\\) by another full-row-rank matrix with the same row space.

I would therefore distinguish three objects until their equivalence is proved:

- \\(q_0^{\rm greedy}\\): the value produced by the stated row-by-row algorithm;
- \\(q_0^{\rm canonical}\\): the intended invariant defined through the relevant functional-observability indices;
- \\(q_0^{\min}\\): the actual minimum augmentation order in the corresponding algebraic relaxation.

The report currently identifies these without supplying the equivalence proof.

### 1.3 What should be done

I recommend three exact tests before using \\(q_0\\) in a theorem.

Test A: basis invariance. Replace \\(L_0\\) by

\\[ L_0'=UL_0,\qquad U\in GL_r(\mathbb Q), \\]

and verify that the computed \\(q_0\\) is unchanged.

Test B: row-order invariance. Permute the rows of \\(L_0\\) and compare the result.

Test C: comparison with a canonical rank-based computation. Independently compute the relevant functional-observability indices using a rank-increment or canonical staircase construction, rather than the same greedy routine.

If all three agree, that is useful evidence. But the paper still needs a proof that the greedy algorithm computes the canonical indices.

In particular, I would not yet write “This is the algebraic minimum order” as an established fact unless the definition of the algebraic relaxation and the equivalence theorem are both supplied.

### 1.4 Answer to Q3

My answer is:

- The inequality \\(q_0\leq n-p\\) should be automatic if \\(q_0\\) counts independent directions added modulo \\(\operatorname{row}C\\).
- It should not be imposed as an independent hypothesis in the terminal-only theorem.
- The more important open point is whether the reported `eta_and_q0` algorithm actually computes the intended canonical minimum.

Once that is settled, the comparison with terminal order becomes clean:

\\[ q_0\leq n-p=q\_{\rm terminal}. \\]

The terminal construction supplies the upper endpoint; \\(q_0\\) supplies a lower endpoint only if its algebraic-minimum interpretation has been proved.

## 2. Part IV: the controlled experiment

### 2.1 The first three rows are a useful controlled comparison

The most useful comparison is:

| System        | Profile       | \\(\rho\\) | \\(q_0\\) | \\(q\_{\min}\\) | Gap |
| ------------- | ------------- | ---------- | --------- | --------------- | --- |
| \\(C\_{33}\\) | \\((2,2)\\)   | 2          | 2         | 3               | 1   |
| \\(C\_{42}\\) | \\((2,1,1)\\) | 2          | 2         | 3               | 1   |
| \\(C\_{24}\\) | \\((2,1,1)\\) | 2          | 2         | 3               | 1   |

This is a much better comparison than the earlier experiment in which both \\(n\\) and the profile varied.

Assuming the same \\(A,L_0,n,p,r\\) are used and all standing hypotheses hold, the comparison isolates the effect of changing the profile tail while keeping

\\[ n=6,\quad p=2,\quad \rho=2,\quad q_0=2 \\]

fixed.

It provides evidence that the tail of the profile does not affect \\(q\_{\min}\\) in this particular family.

There is an important limitation, however: the profiles \\((2,2)\\) and \\((2,1,1)\\) are only two possibilities, and the experiment has a highly structured diagonal realization. The result is evidence for profile irrelevance in this family, not evidence that profile irrelevance holds for general systems.

I would describe it as a successful controlled experiment, not as a decisive test of the universal conjecture.

### 2.2 There is a definition inconsistency in the fourth row

The report defines

\\[ q\_{\rm geom} = \text{the first order at which an admissible intermediate-}\delta \text{ candidate exists}. \\]

But for \\(C\_{51}\\), the report has \\(\rho=1\\). In that case,

\\[ \\{\\,\delta\in\mathbb Z:1\leq\delta<\rho\\,\\} =\varnothing. \\]

There is no intermediate stratum at any order. Therefore, under the stated definition, \\(q\_{\rm geom}\\) does not exist for \\(C\_{51}\\), and it cannot equal 4.

The table's value 4 makes sense if \\(q\_{\rm geom}\\) is instead defined as the first order at which a candidate passes the geometric stage, where that stage includes the terminal branch.

I recommend choosing one of the following two conventions.

Convention A — Keep the intermediate definition.

Use

\\[ q\_{\rm geom}^{\rm int} = \min\\{q:\exists\delta,\ 1\leq\delta<\rho,\ \mathfrak S\_{q,\delta}\ne\varnothing\\}. \\]

Then \\(q\_{\rm geom}^{\rm int}\\) is undefined when \\(\rho\leq1\\), and the terminal case is recorded separately.

Convention B — Define a unified geometric threshold.

Let

\\[ q\_{\rm geom} = \min\\{q:\text{a geometrically admissible candidate exists}\\}, \\]

where the geometric candidate set includes:

- intermediate-stratum candidates for \\(q+p\<n\\);
- the terminal candidate when \\(q+p=n\\).

Then the \\(C\_{51}\\) entry \\(q\_{\rm geom}=4\\) is consistent.

I prefer Convention B for experimental tables, because it permits a single comparison with \\(q\_{\min}\\). But the paper should retain the distinction between the intermediate and terminal branches in its theorems.

### 2.3 The equality \\(q\_{\rm geom}=q\_{\rm spec}\\) needs careful wording

The report says that in all four systems,

\\[ q\_{\rm geom}=q\_{\rm spec}. \\]

This establishes that the first geometrically admissible order in these examples is also spectrally feasible.

It does not establish that every geometrically admissible candidate at that order passes the spectral test. These are different assertions:

\\[ \begin{aligned} &\text{Threshold equality:}\quad q\_{\rm geom}=q\_{\rm spec},\\\ &\text{Candidate-wise spectral sufficiency:}\quad \mathfrak S\_{q,\delta}^{\rm geom} =\mathfrak S\_{q,\delta}^{\rm sp}. \end{aligned} \\]

The first says that at least one geometric candidate at the first eligible order is spectrally feasible. The second says that every geometric candidate is spectrally feasible.

The 1107/1107 result reported earlier is evidence for the second assertion on that finite sample. The four-row table, by itself, supports only the first.

I recommend reporting both quantities:

\\[ N\_{\rm geom}(q,\delta) = \\#\\{\text{geometrically admissible sampled candidates}\\}, \\]

\\[ N\_{\rm sp}(q,\delta) = \\#\\{\text{spectrally feasible sampled candidates}\\}. \\]

Then candidate-wise spectral rejection is measured by

\\[ N\_{\rm geom}(q,\delta)-N\_{\rm sp}(q,\delta). \\]

This will help determine whether the spectral stage is genuinely redundant in some structured families or merely does not delay the minimum order.

### 2.4 Reproducibility details still needed

The table is promising, but a research report intended for independent verification should include:

- the exact entries of \\(L_0\\);
- the exact entries of each \\(C\\);
- the precise value of \\(r\\);
- the exact definition of \\(q_0\\) used in the computation;
- the candidate-generation method for each order;
- the number of geometric candidates and spectral successes at each order;
- the exact gcd certificates for the first feasible candidates.

The fixed-\\(A\\) construction is particularly suitable for rational exact arithmetic, so there is no reason not to publish the matrices.

## 3. Q1: how should the bounded-gap conjecture now be stated?

With the definition of \\(q_0\\) clarified, the conjecture is more meaningful. I would still separate its mathematical formulation from the evidence supporting it.

### 3.1 A precise version

Let \\(q_0(A,C,L_0)\\) denote the correctly defined algebraic lower-bound quantity, and let \\(q\_{\min}(A,C,L_0)\\) denote the minimum feasible observer order.

The conjecture should be written as:

Conjecture (uniform bounded gap at fixed \\(\rho\\)). There exists a function

\\[ f:\mathbb N\longrightarrow\mathbb N \\]

such that, for every admissible observable system satisfying the standing assumptions,

\\[ \boxed{ q\_{\min}(A,C,L_0)-q_0(A,C,L_0) \leq f(\rho), \qquad \rho=\operatorname{rank}\begin{bmatrix}C\\\CA\end{bmatrix}-p. } \\]

The intended uniformity should be stated explicitly: the bound is independent of \\(n\\), the detailed observability profile, the eigenvalues of \\(A\\), and the particular matrices \\(C,L_0\\), subject to the fixed value of \\(\rho\\) and the stated assumptions.

If you intend the bound to be uniform only when \\(p,r,\rho\\) are fixed, then the conjecture is weaker:

\\[ q\_{\min}-q_0\leq f\_{p,r}(\rho). \\]

These are not equivalent formulations. Since you ask whether the bound can depend on \\(\rho\\) alone, I would investigate the stronger version first.

### 3.2 What the new experiment contributes

For the first three systems,

\\[ q\_{\min}-q_0=1 \quad\text{when }\rho=2. \\]

For the fourth,

\\[ q\_{\min}-q_0=1 \quad\text{when }\rho=1. \\]

This is consistent with a particularly strong conjecture:

\\[ \boxed{ q\_{\min}-q_0\leq1. } \\]

But the data are far too limited to propose this as the main conjecture. The earlier project results and the whole-family examples should also be checked against it before it is promoted.

I would maintain two hypotheses:

- Weak conjecture: the gap is bounded by a function of \\(\rho\\);
- Strong conjecture: the gap is at most 1, or at most a simple linear function of \\(\rho\\).

The weak conjecture is the safer central research question. The strong conjecture is an attractive target to falsify.

### 3.3 A useful experiment to distinguish the conjectures

For each fixed \\(\rho\\), search for systems with increasing \\(n\\) and varying observability-profile length.

The most important test is not whether the mean gap stays small, but whether the maximum exact gap increases with \\(n\\).

For example, for \\(\rho=2\\), compare families whose profiles have increasing lengths, such as

\\[ (2,2),\quad (2,1,1),\quad (2,1,1,1),\quad (2,1,1,1,1). \\]

These profiles correspond to different \\(n\\), so they do not isolate profile effects as cleanly as the existing \\(n=6\\) comparison. But they are appropriate for testing whether a fixed-\\(\rho\\) gap can grow with profile length.

For every family member, record

\\[ q_0,\quad q\_{\rm geom},\quad q\_{\rm spec},\quad q\_{\min}, \\]

and, importantly, the geometric and spectral candidate counts at every order.

A single exact member with a gap exceeding the proposed bound would be decisive evidence against that conjecture.

## 4. Q2: which extension is more informative?

My recommendation is to pursue non-diagonal \\(A\\) with prescribed observability indices next, but not before completing a modest extension of the existing diagonal experiment.

There are two distinct goals:

1. test whether the profile matters;
2. test whether the diagonal structure is responsible for the observed behavior.

The two proposed extensions address these goals differently.

### 4.1 First: extend the fixed-\\(A\\) diagonal experiment

The current comparison is well designed. I would add a few more systems with the same \\((n,p,\rho)\\) where possible, and test different row weights and different \\(L_0\\) matrices.

For instance, for \\(n=8,p=3\\), compare support partitions

\\[ (4,2,2) \qquad\text{and}\qquad (3,3,2). \\]

Both have three output rows, each supported on a disjoint block of at least two coordinates. Their profiles are

\\[ (3,1,1) \qquad\text{and}\qquad (3,2), \\]

respectively, so both have

\\[ \rho=3. \\]

This gives a controlled comparison of different profile tails at fixed \\(n,p,\rho\\), in a higher-\\(\rho\\) setting.

It is particularly useful because it tests whether the apparent irrelevance of the tail at \\(\rho=2\\) persists at \\(\rho=3\\).

### 4.2 Second: non-diagonal block-cyclic systems

After the diagonal experiment is expanded, I would move to block-cyclic or companion-type matrices with prescribed observability indices.

The reason is that the diagonal construction has special spectral properties:

- distinct eigenvalues;
- a transparent Vandermonde structure;
- disjoint coordinate supports;
- simple invariant coordinate subspaces.

These features make the profile easy to prescribe, but they may also make the spectral stage unusually well behaved.

A non-diagonal construction can preserve the observability profile while changing the matrix representation and the interaction of the quotient pencil with the spectrum.

This is the right way to test whether the observed relation

\\[ q\_{\rm geom}=q\_{\rm spec} \\]

is structural or an artifact of the diagonal family.

### 4.3 Suggested order of experiments

| Stage | Construction                                                        | Main question                                                 |
| ----- | ------------------------------------------------------------------- | ------------------------------------------------------------- |
| 1     | Existing diagonal family, varied rational row weights and \\(L_0\\) | Is the current result robust within the same profile family?  |
| 2     | Diagonal family with \\(n=8,p=3,\rho=3\\)                           | Does profile-tail irrelevance persist at higher \\(\rho\\)?   |
| 3     | Non-diagonal block-cyclic \\(A\\)                                   | Is the phenomenon independent of diagonal spectral structure? |
| 4     | Perturbations preserving observability indices                      | Is the phenomenon stable under changes of matrix entries?     |

One caution: generic perturbations of \\(A\\) and \\(C\\) do not necessarily preserve the exact observability profile. If profile preservation is required, the perturbation should be performed within a parameterization that enforces the rank-increment conditions, followed by exact verification.

## 5. Q4: separate geometric existence from spectral synthesis

Yes. I agree with this formulation, and I think it is now the right way to organize the complexity question.

However, I would make the two decision problems mathematically precise and avoid suggesting that they are necessarily computationally independent.

### 5.1 Define the geometric candidate set

For a subterminal order \\(q\\), define

\\[ \mathfrak S\_{q,\delta}^{\rm geom} \\]

to consist of all admissible augmentations \\(\mathcal L\\) satisfying:

\\[ \operatorname{row}L_0\subseteq\operatorname{row}\mathcal L, \\]

\\[ \operatorname{rank}\begin{bmatrix}C\\\\\mathcal L\end{bmatrix}=p+q, \\]

\\[ \mathcal VA\subseteq\mathcal V+\operatorname{row}(CA), \\]

and

\\[ \delta=h-(p+q). \\]

The third condition is exactly (5a) in the subspace formulation.

For a subterminal candidate, the relevant strata have

\\[ 1\leq\delta<\rho. \\]

The geometric existence problem is therefore:

\\[ \boxed{ \text{GEO}(q): \quad \bigcup\_{\delta=1}^{\rho-1} \mathfrak S\_{q,\delta}^{\rm geom} \ne\varnothing? } \\]

The terminal case should be a separate branch, because the intermediate interval is empty when \\(\rho\leq1\\), and because terminal feasibility is established by the terminal-order construction.

### 5.2 Define the spectral synthesis problem

Let

\\[ \mathfrak S\_{q,\delta}^{\rm sp} = \left\\{ \mathcal L\in\mathfrak S\_{q,\delta}^{\rm geom}: \overline N\_{\mathcal Z}(\lambda) \text{ is injective for every }\lambda\in\mathbb C \right\\}. \\]

Then the subterminal spectral synthesis problem is:

\\[ \boxed{ \text{SPEC-SYNTH}(q): \quad \bigcup\_{\delta=1}^{\rho-1} \mathfrak S\_{q,\delta}^{\rm sp} \ne\varnothing? } \\]

This is precisely the problem that determines whether a subterminal feasible augmentation exists.

The distinction is:

\\[ \text{SPEC-SYNTH}(q)\Longrightarrow\text{GEO}(q), \\]

but the converse is not automatic.

The minimum order is determined by the first order at which spectral synthesis succeeds, together with the terminal branch.

### 5.3 The geometric problem deserves its own complexity analysis

I agree that the geometric problem is worth studying separately. It may be significantly easier than the full problem, but that should be established rather than assumed.

In a Grassmannian chart, one can parameterize the candidate subspace using a basis matrix with a normalized pivot block. The target containment, admissibility, invariance-modulo-\\(D\\), and fixed-\\(\delta\\) conditions can then be expressed using polynomial equalities and nonvanishing minors.

This gives a natural algebraic decision problem.

But there is a subtle point: the invariance condition

\\[ \mathcal VA\subseteq\mathcal V+D \\]

contains the unknown subspace on both sides. In coordinates, this generally produces bilinear or higher-degree polynomial constraints. It is not simply a fixed linear-system feasibility problem.

Therefore, I would not assume GEO is polynomial-time solvable just because it does not contain the spectral condition.

### 5.4 The spectral problem is not just a second independent filter

For a fixed candidate, the spectral test is straightforward exact algebra:

\\[ \gcd\\{\text{maximal minors of }\overline N\_{\mathcal Z}(\lambda)\\}=1. \\]

But in the synthesis problem, the entries of the pencil depend on the unknown subspace. The difficulty is finding a subspace for which the polynomial gcd condition holds.

Thus the distinction is:

- fixed-candidate spectral verification: univariate polynomial computation;
- existence of a geometrically admissible candidate: algebraic subspace feasibility;
- joint spectral synthesis: algebraic subspace feasibility with a universal spectral condition.

The third is the natural main complexity target.

### 5.5 A recommended complexity roadmap

I would formulate three separate problems in the paper:

| Problem     | Question                                                             | Purpose                           |
| ----------- | -------------------------------------------------------------------- | --------------------------------- |
| GEO         | Does the geometric stratum contain an admissible candidate?          | Isolate the Grassmannian geometry |
| SPEC-SYNTH  | Does it contain a candidate with pointwise-injective reduced pencil? | Main synthesis problem            |
| SPEC-VERIFY | Does a specified candidate satisfy the spectral condition?           | Exact verification baseline       |

The first two are existence problems; the third is a verification problem.

A useful first theorem would be an explicit existential-real-algebraic encoding for GEO. A second would encode the maximal-minor gcd-one condition for SPEC-SYNTH using a Bézout identity with bounded-degree auxiliary polynomials.

I would then investigate hardness for SPEC-SYNTH. A hardness result for GEO would also be interesting, but it is not necessary for the main problem to be difficult.

## 6. Q5: standardizing the evidence labels

The six labels in the report are good. I would adopt them, with two additions to make the system complete.

### 6.1 Recommended standard

| Label                                   | Exact meaning                                                                                                             |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `[Lean]`                                | Complete formal statement and proof in Lean, with the intended mathematical hypotheses represented correctly              |
| `[Lean-conditional]`                    | Formal logical or algebraic consequence proved under hypotheses whose mathematical content is not fully formalized        |
| `[Paper proof]`                         | Complete human-written mathematical proof, not yet formalized                                                             |
| `[Exact finite enumeration]`            | Every member of a genuinely finite, explicitly specified candidate set has been checked exactly                           |
| `[Finite chart-sample verification]`    | A finite collection of exact points sampled from specified Grassmannian charts has been checked                           |
| `[Empirical regularity]`                | A pattern observed across a stated finite sample, without a universal proof                                               |
| `[Symbolic generic chart verification]` | A symbolic computation establishes the claim over the rational-function field of a chart, hence generically on that chart |
| `[Whole-family theorem]`                | A proof covers every member of a specified parameterized family, including any claimed exceptional cases                  |

The two additions are important.

A symbolic generic chart calculation is stronger than finite chart sampling, but it does not automatically establish all-specialization feasibility. A whole-family theorem should be reserved for a proof that handles all parameter values in the stated domain.

I would also use `[Numerical exploration]` if floating-point computations appear anywhere in the project. It should never be conflated with exact rational verification.

### 6.2 A label should attach to a claim, not merely to a document

One report may contain all of the following:

- a `[Paper proof]` of the terminal-order theorem;
- a `[Lean-conditional]` formalization of its arithmetic consequence;
- an `[Exact finite enumeration]` of a finite candidate set;
- an `[Empirical regularity]` concerning the gap.

It is therefore better to label individual statements or table rows than to label an entire report as “Lean verified” or “exactly verified.”

For each empirical table, include a status column. For each theorem, include a proof-status note.

## 7. Additional recommendations

There are three further directions I would prioritize.

### 7.1 Investigate whether the spectral stage is generically redundant

The repeated observations

\\[ q\_{\rm geom}=q\_{\rm spec} \\]

and the earlier 1107/1107 candidate-wise success are sufficiently interesting to motivate a separate conjecture.

A possible formulation is:

Conjecture (generic spectral feasibility on a nonempty intermediate stratum). For a specified class of observable systems, if the geometric stratum

\\[ \mathfrak S\_{q,\delta}^{\rm geom} \\]

is nonempty, then its spectrally feasible subset is nonempty and contains a relatively Zariski-open subset.

This is stronger and more informative than simply saying that geometric and spectral minimum orders agree.

But it is also a delicate conjecture. The spectral failure locus is described by the existence of a finite \\(\lambda\\) at which all maximal minors vanish. Its projection from the product with the affine \\(\lambda\\)-line is constructible, not automatically closed. A proof of generic feasibility must address the closure of that projection, including possible roots escaping to infinity.

I would not state this conjecture for all systems yet. First identify a precise structured class for which the spectral-feasibility locus can be analyzed.

### 7.2 Separate minimum-order statistics from candidate-wise statistics

The minimum-order gap is a coarse summary. Two systems can have the same \\(q\_{\min}\\) but very different spectral success rates among candidates.

For each order, record:

\\[ \begin{aligned} G_q&=\text{number of geometric candidates},\\\ S_q&=\text{number of spectrally feasible candidates},\\\ \gamma_q&=S_q/G_q \quad (G_q>0). \end{aligned} \\]

Then report both

\\[ q\_{\rm geom},\quad q\_{\rm spec} \\]

and the sequence \\((G_q,S_q,\gamma_q)\\).

This will distinguish three phenomena:

- geometry first becomes possible, and nearly every candidate is spectrally feasible;
- geometry first becomes possible, but only a small fraction of candidates are feasible;
- geometry becomes possible substantially earlier than spectral feasibility.

Those cases have different mathematical explanations and potentially different complexity behavior.

### 7.3 Test invariance under state-coordinate transformations

Since the problem is fundamentally about row spaces and induced quotient maps, it should be invariant under invertible state-coordinate changes.

For \\(P\in GL_n(\mathbb Q)\\), the transformed system is

\\[ A'=P^{-1}AP,\qquad C'=CP,\qquad L_0'=L_0P. \\]

A candidate \\(\mathcal L\\) transforms to

\\[ \mathcal L'=\mathcal LP. \\]

The values of \\(q\_{\min}\\), \\(q_0\\), \\(\rho\\), \\(\delta\\), and the spectral feasibility verdict should be unchanged.

This is a stronger metamorphic test than changing the basis of \\(\operatorname{row}\mathcal L\\), because it checks that the entire implementation respects the underlying state-space geometry.

I would add it to the mandatory test suite.

## 8. Final assessment and recommended next steps

The new report resolves several issues from the previous round. The controlled experiment is a genuine improvement, the corrected \\(\delta\\) is consistently used, and the verification checklist is becoming a reliable part of the research infrastructure.

My recommendations, in order of importance, are:

| Priority | Task                                                                                     | Reason                                                                     |
| -------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| 1        | Prove that `eta_and_q0` computes the intended canonical functional-observability indices | The definition of the lower bound \\(q_0\\) underlies every gap conjecture |
| 2        | Correct the definition of \\(q\_{\rm geom}\\) in the \\(\rho=1\\) case                   | The current definition and fourth table entry are inconsistent             |
| 3        | Publish exact matrices for the controlled experiment                                     | Makes the result independently reproducible                                |
| 4        | Extend the diagonal experiment to \\(n=8,p=3,\rho=3\\)                                   | Tests whether profile-tail irrelevance persists at higher \\(\rho\\)       |
| 5        | Move to non-diagonal block-cyclic systems                                                | Tests whether the diagonal structure explains spectral success             |
| 6        | Formalize GEO and SPEC-SYNTH as separate algebraic decision problems                     | Establishes a precise foundation for complexity analysis                   |

### My answers to the five questions

- Q1: Yes, test a uniform bound depending only on \\(\rho\\), but distinguish it from the weaker bound depending on \\(p,r,\rho\\). The new experiment supports the conjecture but is not sufficient to establish it. First prove that \\(q_0\\) is correctly defined.
- Q2: Extend the diagonal family briefly, then prioritize non-diagonal block-cyclic constructions. The latter provide the more informative test of structural generality.
- Q3: \\(q_0\leq n-p\\) is automatic if it counts independent directions modulo \\(\operatorname{row}C\\). The unresolved issue is the equivalence of the greedy algorithm with the intended canonical minimum.
- Q4: Yes. Separate GEO, SPEC-SYNTH, and fixed-candidate SPEC-VERIFY. This is the cleanest complexity framework.
- Q5: Adopt the six labels and add `[Symbolic generic chart verification]` and `[Whole-family theorem]`. Add `[Numerical exploration]` if floating-point computations are used.

### One particularly important point

I would make the \\(q_0\\) issue the immediate next task, ahead of expanding the experiments. If \\(q_0\\) is not invariant under a change of basis of \\(L_0\\), or if the greedy stopping rule does not compute the intended functional-observability indices, then the numerical gap

\\[ q\_{\min}-q_0 \\]

may not be measuring the mathematical quantity the project intends to study.

Once that is settled, the controlled-profile experiment becomes a much stronger foundation for the bounded-gap conjecture.

Overall: the project is progressing from a collection of feasibility computations toward a coherent theory of geometric lower bounds, spectral synthesis, and minimum-order gaps. The next decisive advance should be a proof of the \\(q_0\\) characterization, followed by a non-diagonal family that tests whether the current spectral regularity survives beyond the diagonal construction.

I would be happy to examine the exact `eta_and_q0` implementation or its mathematical definition next, since that is now the most consequential foundational issue.

23_controlled_profile.md