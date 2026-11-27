# Research review of `22_method_and_kernels.md`

The report marks a meaningful improvement in the project: the geometric filter is now aligned with the correct definition of \\(\delta\\), the Lean formalization is being labelled with appropriate restraint, and the computational pipeline separates geometric screening from spectral verification.

My overall assessment is positive, but there are several points I would tighten before incorporating these results into a paper. The most important are:

1. The corrected \\(\delta\\)-definition should become a single canonical invariant throughout the code and paper.
2. The proposed bounded-gap conjecture is not yet sufficiently specified: the definition of \\(q_0\\) is needed, and the evidence does not yet distinguish a bound depending only on \\(\rho\\) from one depending on the full observability profile.
3. The proposed example in Q2 contains a parameter inconsistency: \\(\rho=2\\) is impossible when \\(p=1\\).
4. Exact chart sampling is legitimate as finite exact verification, but it is not a substitute for symbolic verification of a whole Grassmannian family.
5. The complexity question can now be formulated as a precise algebraic decision problem. There is a plausible route to an \\(\exists\mathbb R\\) upper bound, but hardness would require a separate reduction.
6. The terminal-order theorem and the two boundary obstructions should indeed be promoted to standalone results.

I will distinguish what follows from the established mathematics, what is a methodological recommendation, and what remains a conjectural research direction.

22_method_and_kernels.md

## 1. Machine-checked results: the current description is appropriately cautious

### 1.1 The label `[Lean-conditional]` is the right one

The report says that the logical and arithmetic skeleton of B.31–B.33 has been formalized, while the row-space/annihilator arguments remain paper proofs. This is a good distinction.

For example, the formalized implication

\\[ \delta\leq \rho,\qquad \delta=\rho\Longrightarrow\text{infeasible},\qquad \delta=0\Longrightarrow\text{infeasible} \\]

implies

\\[ \text{feasible}\Longrightarrow 1\leq\delta<\rho. \\]

That implication is elementary once the two boundary exclusions have been supplied. Its formalization verifies the logical assembly, but it does not independently establish the mathematical truth of the boundary exclusions.

I recommend keeping three explicit levels throughout the paper and development log:

| Label                | Meaning                                                                     | What it certifies                                                                                |
| -------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `[Lean]`             | The complete mathematical statement and proof are formalized                | The theorem, as encoded, follows from its formal hypotheses                                      |
| `[Lean-conditional]` | The formal proof assumes one or more mathematical lemmas not yet formalized | The logical or arithmetic consequence is machine-checked, but not the missing mathematical input |
| `[Paper proof]`      | A complete human-written proof exists, but is not formalized                | The result has a mathematical proof subject to ordinary proof review                             |

A fourth label is useful for the computational work:

| Label                  | Meaning                                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------------ |
| `[Exact verification]` | A particular finite instance or finite list of instances has been checked using exact arithmetic |

The distinction matters because a declaration can compile with no `sorry` and still formalize a conditional statement whose crucial hypotheses encode the difficult part of the theorem. The report already recognizes this; I would make the convention explicit in the paper's formalization appendix.

### 1.2 B.22 and B.28(3) should be standalone lemmas

I agree with the report's conclusion in Part IV.

These two results are structural boundary obstructions, not merely technical steps buried inside B.31. They should be stated early and then cited whenever the corresponding boundary is excluded.

I would organize them as follows.

Equality obstruction (B.22). Under (5a), if \\(q\geq1\\) and

\\[ h=q+r_1, \\]

then (5b) fails. More precisely, the relevant square factor has the form

\\[ P(\lambda)= \begin{bmatrix} \lambda I_q-K_1&-K_2\\\ 0&I\_{r_1} \end{bmatrix}, \\]

and

\\[ \det P(\lambda)=\det(\lambda I_q-K_1). \\]

This is a nonconstant monic polynomial, so it has a finite complex root. Thus the rank condition fails at some finite \\(\lambda\\).

Invariance obstruction (B.28(3)). If \\(\delta=0\\), then \\(D=\operatorname{row}(CA)\subseteq\mathcal V\\). From (5a),

\\[ \mathcal VA\subseteq \mathcal V+D=\mathcal V. \\]

Consequently \\(\mathcal V\\) is \\(A\\)-invariant. Since \\(R=\operatorname{row}C\subseteq\mathcal V\\), observability of \\((C,A)\\) forces

\\[ \mathcal V=\mathbb C^{1\times n}. \\]

Therefore, for a subterminal candidate, \\(\delta=0\\) is impossible.

These statements are complementary: B.22 excludes the upper boundary, and B.28(3) excludes the lower boundary. Together they give the geometric restriction

\\[ \boxed{ q+p\<n,\quad (5a),\quad (5b) \quad\Longrightarrow\quad 1\leq\delta<\rho. } \\]

The assumptions should be displayed separately in each lemma. In particular, the invariance argument needs observability of \\((C,A)\\), while the equality obstruction does not.

### 1.3 A small improvement to the Lean audit

The report's cumulative count—189 declarations, 70 files, 178 registered statements, no discrepancies between audit scripts, and no `sorry`—is useful project-management evidence. It is not, by itself, a measure of how much of the central mathematical argument has been formalized.

I would add an audit table with one row per major theorem:

- paper theorem identifier;
- Lean declaration identifier;
- exact formal hypotheses;
- mathematical hypotheses represented by assumptions;
- whether the row-space/annihilator translation is formalized;
- whether the spectral argument is formalized;
- whether the formal statement is equivalent to, or only implies, the paper statement.

The last two columns are especially important. A theorem can be formally proved at the level of an abstract finite-dimensional vector-space lemma while the application-specific construction remains in paper mathematics.

## 2. The corrected \\(\delta\\)-invariant and the two-stage pipeline

This is the most important computational correction in the report.

The canonical definition is

\\[ \boxed{ \delta = h-(q+p) = \dim\bigl(D/(D\cap\mathcal V)\bigr). } \\]

Here

\\[ D=\operatorname{row}(CA),\qquad \mathcal V=\operatorname{row}\begin{bmatrix}\mathcal L\\\C\end{bmatrix}, \qquad h=\dim(\mathcal V+D). \\]

Because admissibility gives \\(\dim\mathcal V=q+p\\), the dimension formula is

\\[ h=\dim\mathcal V+\dim D-\dim(D\cap\mathcal V) =q+p+\delta. \\]

Equivalently,

\\[ \boxed{ \delta = \dim D-\dim(D\cap\mathcal V). } \\]

This makes the previous error transparent. The intersection dimension

\\[ \dim(D\cap\mathcal V) \\]

is not \\(\delta\\); it measures the part of \\(D\\) already contained in \\(\mathcal V\\). The correct \\(\delta\\) measures the complementary quotient dimension.

The relation with \\(\rho\\) is

\\[ \rho=r_1-p =\dim\bigl(D/(D\cap R)\bigr), \\]

and \\(R\subseteq\mathcal V\\) implies

\\[ 0\leq\delta\leq\rho. \\]

I recommend printing all three expressions for \\(\delta\\) in the program's diagnostic output. That would have made the earlier error easier to detect.

### 2.1 The two-stage pipeline is mathematically justified

The proposed procedure is:

1. Compute \\(h\\) and \\(\dim\mathcal V\\).
2. Set \\(\delta=h-\dim\mathcal V\\).
3. For subterminal candidates, discard candidates unless\
   \\[\
   1\leq\delta<\rho.\
   \\]
4. Apply the spectral test only to the candidates that survive.

This is the correct architecture.

There is one useful distinction to make in the report: the filter is not merely empirically sound on the 599 instances. Under the hypotheses of the boundary-obstruction theorem, its soundness is mathematical. The zero-discarded-feasible count is a regression test of the implementation.

The report gives:

- 599 instances;
- 3,400 admissible candidates;
- 1,905 spectral tests after filtering;
- a reduction of approximately \\(44.0\\%\\) in spectral tests.

That is a meaningful computational saving.

However, I would clarify the sentence

> feasible counts agree before and after (1905 = 1905).

As written, it appears to say that there were 1,905 feasible candidates both before and after filtering, and that all 1,905 candidates surviving the filter were feasible. That may indeed be the intended result, but it should be reported with an explicit table:

| Quantity                         | Before filter | After filter |
| -------------------------------- | ------------- | ------------ |
| Candidates considered            | 3,400         | 1,905        |
| Spectral tests executed          | 3,400         | 1,905        |
| Candidates passing spectral test | ?             | ?            |
| Feasible candidates discarded    | 0             | 0            |

This prevents the number 1,905 from being mistaken for both the number of tests and the number of feasible candidates.

Also, because \\(q+p>n\\) is impossible under admissibility, the terminal branch should be written as

\\[ q+p=n, \\]

not merely \\(q+p\geq n\\). In the terminal case, \\(\mathcal V\\) is the whole row space and \\(\delta=0\\), so it must be retained by the filter even though the subterminal \\(\delta=0\\) branch is excluded.

### 2.2 The new 1107/1107 result

The corrected report says that all 1,107 sampled candidates in the intermediate stratum passed the spectral test.

This is an interesting and potentially important empirical observation. It also reconciles the previous apparent intermediate-stratum counterexample if that candidate was actually in the equality stratum because of the old definition of \\(\delta\\).

But the correct interpretation is still:

\\[ \text{All 1,107 sampled intermediate-stratum candidates were feasible.} \\]

It is not yet:

\\[ \text{Every candidate in the intermediate stratum is feasible.} \\]

The latter would be a theorem about an entire algebraic or constructible family. It requires a symbolic argument or a structural theorem. I would record the new result as a separate empirical regularity and actively attempt to falsify it before elevating it to a conjecture.

## 3. Q1 — Is the minimum-order gap bounded by \\(\rho\\), or by the full profile?

This is the most interesting structural question in the report, but I would not yet commit to a bound depending only on \\(\rho\\).

### 3.1 First, the definition of \\(q_0\\) must be made explicit

The report uses

\\[ q\_{\min}-q_0 \\]

but does not define \\(q_0\\). This is not a cosmetic omission. The plausibility of a \\(\rho\\)-only bound depends heavily on what \\(q_0\\) measures.

For example, the established terminal-only result gives

\\[ \rho\leq1 \quad\Longrightarrow\quad q\_{\min}=n-p \\]

under the standing observability and admissibility assumptions. Thus, if \\(q_0\\) does not itself track \\(n-p\\), a bound depending only on \\(\rho=1\\) would be difficult to reconcile with this result as \\(n\\) varies.

Conversely, if \\(q_0\\) is a dimension-theoretic lower bound that already grows with \\(n-p\\), the same observation may be entirely compatible with a bounded gap.

So I would not assess the conjecture's precise strength until \\(q_0\\) has been defined in the statement.

### 3.2 Why the full observability profile is a natural candidate

Recall

\\[ r_k=\operatorname{rank} \begin{bmatrix} C\\\CA\\\\\vdots\\\CA^k \end{bmatrix}, \qquad \Delta_k=r_k-r\_{k-1}, \\]

with \\(r_0=\operatorname{rank}C=p\\). Then

\\[ \Delta_1=\rho. \\]

For an observable pair with \\(\operatorname{rank}C=p\\), the increments satisfy

\\[ \Delta_1\geq\Delta_2\geq\cdots\geq0, \qquad \sum\_{k\geq1}\Delta_k=n-p. \\]

The sequence \\((\Delta_k)\\) contains substantially more information than \\(\rho\\). In particular, it records how quickly the observability row space grows beyond its initial \\(p\\)-dimensional part.

The first increment says how many new directions are revealed by one application of \\(A\\). The later increments record how many additional independent directions continue to appear at each subsequent step.

This suggests that the relevant structural quantity may be the observability index, or equivalently the length of the profile:

\\[ \nu=\max\\{k:\Delta_k>0\\}. \\]

I would test three conjecture classes, in this order:

Conjecture A — \\(\rho\\)-only bound

\\[ q\_{\min}-q_0\leq f(\rho). \\]

This is the strongest and simplest conjecture, but it should be treated as the most vulnerable to counterexamples.

Conjecture B — profile-length bound

\\[ q\_{\min}-q_0\leq f(\rho,\nu). \\]

This is more plausible if the difficulty is related to how many successive powers of \\(A\\) are needed to generate the observable row space.

Conjecture C — full-profile bound

\\[ q\_{\min}-q_0\leq F(\Delta_1,\Delta_2,\ldots). \\]

This is the most flexible formulation, but it risks becoming a restatement of the data unless \\(F\\) has a simple form.

My recommendation is to investigate A first, but to collect enough data to distinguish A from B and C. Do not assume linearity in \\(\rho\\) yet.

### 3.3 What does the current \\(\rho=2\\) evidence establish?

The report gives two profile classes:

| Profile       | \\(n\\) | Samples | Mean gap |
| ------------- | ------- | ------- | -------- |
| \\((2,2)\\)   | 6       | 766     | 1.00     |
| \\((2,2,1)\\) | 7       | 733     | 1.50     |

These data are consistent with a gap bound of 2 for \\(\rho=2\\), but they do not isolate the effect of the profile because \\(n\\) changes simultaneously.

The statement in Q1 that 745 instances agree should also be reconciled with the 766 samples in the table. Perhaps the 745 figure refers to a filtered subset, but the report should say so explicitly. Otherwise, the reader cannot tell which experiment supports the conjecture.

There is a more important logical point: observing a maximum gap of 2 in a finite sample is not evidence that the maximum over the entire admissible family is 2. A single exact counterexample with gap 3 would disprove the conjecture; no number of random successes proves it.

### 3.4 A useful strategy: separate geometric and spectral contributions

The gap may arise from two different sources:

1. the intermediate geometric stratum may first become nonempty only at a certain order;
2. even when it is nonempty, its members may fail the quotient-pencil spectral condition.

This suggests introducing two quantities, if they are not already present in the project:

\\[ q\_{\mathrm{geom}} = \min\\{q:\text{an admissible subterminal intermediate-stratum point exists}\\}, \\]

and

\\[ q\_{\mathrm{spec}} = \min\\{q:\text{an admissible intermediate-stratum point passes (5b)}\\}. \\]

Then the minimum-order gap can be decomposed conceptually into a geometric delay and a spectral delay. More precisely, when these quantities are defined over the same order range,

\\[ q\_{\min}-q_0 = (q\_{\mathrm{geom}}-q_0) + (q\_{\mathrm{spec}}-q\_{\mathrm{geom}}). \\]

The first term is controlled by the geometry of the admissible subspace family. The second is controlled by the spectral pencil.

This distinction may be more informative than trying to predict \\(q\_{\min}\\) directly from \\((\Delta_k)\\).

My recommendation for Q1: retain the \\(\rho\\)-only conjecture as the primary falsifiable conjecture, but run the experiments needed to distinguish it from profile-dependent alternatives. Do not yet claim a linear bound or even a finite bound depending only on \\(\rho\\).

## 4. Q2 — A controlled experiment for the observability profile

The experimental idea is correct: fix \\(n,p,r,\rho\\), and vary the tail of the profile. But the example in the report has an inconsistency.

### 4.1 The proposed \\(p=r=1\\) example cannot have \\(\rho=2\\)

We have

\\[ \rho=r_1-p\leq p, \\]

because

\\[ r_1=\operatorname{rank}\begin{bmatrix}C\\\CA\end{bmatrix} \leq 2p. \\]

Therefore, if \\(p=1\\),

\\[ \rho\leq1. \\]

So the example

\\[ n=6,\qquad p=r=1,\qquad (2,2)\ \text{versus}\ (2,1,1) \\]

cannot occur under the stated definitions: both profiles have first increment 2, which would require \\(\rho=2\\), but \\(p=1\\).

The natural correction is

\\[ \boxed{n=6,\quad p=2,\quad \rho=2.} \\]

The value of \\(r\\) can then be fixed at a compatible value, for example \\(r=2\\), provided the remaining admissibility and observability assumptions are satisfied.

### 4.2 A canonical construction: keep \\(A\\) fixed and vary \\(C\\)

I would actually recommend a stronger experiment than varying block-diagonal \\(A\\).

You can keep the same matrix \\(A\\), with the same spectrum and characteristic polynomial, and vary only the output matrix \\(C\\).

Take

\\[ A=\operatorname{diag}(\alpha_1,\ldots,\alpha_6), \\]

where the six \\(\alpha_i\\) are distinct. Let \\(p=2\\).

For the profile \\((2,2)\\), partition the six coordinates into two groups of three and choose the two rows of \\(C\\) to have disjoint supports on these groups. For example,

\\[ C\_{(2,2)} = \begin{bmatrix} c_1&c_2&c_3&0&0&0\\\ 0&0&0&c_4&c_5&c_6 \end{bmatrix}, \\]

where all displayed \\(c_i\\) are nonzero.

For the profile \\((2,1,1)\\), use a partition of sizes four and two:

\\[ C\_{(2,1,1)} = \begin{bmatrix} d_1&d_2&d_3&d_4&0&0\\\ 0&0&0&0&d_5&d_6 \end{bmatrix}, \\]

where all displayed \\(d_i\\) are nonzero.

Because \\(A\\) is diagonal with distinct eigenvalues, the powers of each row of \\(C\\) generate a Vandermonde family on its support. The two row supports are disjoint. Consequently, the observability rank grows by one per step for each coordinate in the corresponding support, until that support has been exhausted.

Thus:

- support sizes \\((3,3)\\) produce observability indices \\((3,3)\\), hence\
  \\[\
  \Delta=(2,2);\
  \\]
- support sizes \\((4,2)\\) produce observability indices \\((4,2)\\), hence\
  \\[\
  \Delta=(2,1,1).\
  \\]

Both systems have

\\[ n=6,\qquad p=2,\qquad \rho=2. \\]

More importantly, they have the same \\(A\\) and hence the same spectrum.

The construction uses the standard observability-index interpretation: the \\(i\\)-th output row sees a disjoint group of eigenvectors, and the corresponding Vandermonde rows generate that group's coordinate subspace.

### 4.3 How to keep \\(r\\) and \\(L_0\\) fixed as well

Choose a fixed \\(L_0\in\mathbb R^{2\times6}\\) generically, with no zero column and with the stacked matrix

\\[ \begin{bmatrix}C\\\L_0\end{bmatrix} \\]

of rank four for both choices of \\(C\\).

For the diagonal matrix with distinct eigenvalues, a row of \\(L_0\\) with all entries nonzero is already sufficient to make \\((L_0,A)\\) observable. Thus one can choose \\(L_0\\) to satisfy observability and then verify the two stacked-rank conditions exactly.

This allows a controlled comparison in which:

- \\(A\\) is fixed;
- \\(n,p,r\\) are fixed;
- \\(L_0\\) is fixed;
- \\(\rho\\) is fixed;
- only the tail of the observability profile changes through \\(C\\).

That is a much cleaner experiment than comparing unrelated random matrices with different dimensions.

### 4.4 A general canonical profile construction

The same idea extends to arbitrary valid profiles.

Suppose

\\[ \Delta_1\geq\Delta_2\geq\cdots\geq0, \qquad \Delta_1\leq p, \qquad \sum\_{k\geq1}\Delta_k=n-p. \\]

Define \\(p\\) positive integers \\(\mu_1,\ldots,\mu_p\\) by requiring

\\[ \Delta_k=\\#\\{i:\mu_i\geq k+1\\}. \\]

Equivalently, the \\(\mu_i-1\\) are the column lengths of the partition encoded by the sequence \\((\Delta_k)\\). They satisfy

\\[ \sum\_{i=1}^p\mu_i=n. \\]

A block-diagonal construction with \\(p\\) cyclic blocks of sizes \\(\mu_i\\), and one output row assigned to each block, realizes the desired profile.

This is a useful canonical family. However, for isolating the effect of the profile experimentally, the fixed-diagonal-\\(A\\), variable-support-\\(C\\) construction above is even better because it holds the spectrum fixed.

### 4.5 Experimental controls I would add

For each fixed \\((n,p,r,\rho)\\), compare profiles while keeping as many other invariants fixed as possible:

- the characteristic polynomial of \\(A\\);
- preferably the spectrum and multiplicity structure;
- the rank and observability properties of \\(L_0\\);
- the relative position of \\(\operatorname{row}L_0\\) and \\(\operatorname{row}C\\);
- the candidate-order range;
- the sampling distribution on the admissible subspace strata.

The last item is important. If the sampling distribution changes when the profile changes, a difference in observed gap may reflect the sampling scheme rather than the profile.

## 5. Q3 — A sharper complexity problem

I agree with the proposed decision problem, but I would formulate it in a way that makes the algebraic structure explicit.

### 5.1 The decision problem

A natural formal version is:

Input: Rational matrices \\((A,C,L_0)\\) and an integer \\(q\\), satisfying the relevant standing assumptions.

Question: Does there exist a real admissible augmentation \\(\mathcal L\\) of order \\(q\\) such that:

1. \\(\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L\\);
2. \\(\operatorname{rank}[C;\mathcal L]=p+q\\);
3. condition (5a) holds;
4. the intermediate-stratum condition holds when \\(q+p\<n\\):\
   \\[\
   1\leq\delta<\rho;\
   \\]
5. the reduced quotient pencil is pointwise injective for every finite complex \\(\lambda\\)?

The terminal case \\(q+p=n\\) should be treated separately, since the intermediate-stratum condition is a subterminal restriction.

This formulation is preferable to saying only that the intermediate stratum contains a point with an injective reduced pencil, because it states exactly what the candidate must satisfy.

### 5.2 The spectral condition can be expressed algebraically

For a fixed candidate, let

\\[ \overline N\_{\mathcal Z}(\lambda): V/S\longrightarrow X/\mathcal Z \\]

be the reduced pencil.

Its dimensions are

\\[ \boxed{ (p+q)\times(q+\delta-\rho). } \\]

Write

\\[ d=q+\delta-\rho. \\]

If \\(d>0\\), pointwise injectivity for every finite complex \\(\lambda\\) is equivalent to saying that the \\(d\times d\\) maximal minors have no common finite complex root.

Equivalently, if these minors are denoted by \\(m_1(\lambda),\ldots,m_t(\lambda)\\), then

\\[ \boxed{ \gcd(m_1,\ldots,m_t)=1. } \\]

This is a univariate polynomial condition. It is substantially more concrete than a universal statement over all \\(\lambda\\).

If \\(d=0\\), the domain is the zero space, so injectivity is automatic; this case should be handled separately in the implementation and formal statement.

### 5.3 Why an \\(\exists\mathbb R\\) upper bound is plausible

The existence of an augmentation can be expressed in coordinates on Grassmannian charts.

On a chosen chart, the unknown subspace is represented by a matrix whose pivot block is normalized to the identity. The remaining chart entries are scalar variables.

The following requirements can be expressed by polynomial equalities and inequalities:

- target-row-space containment;
- the rank and admissibility conditions;
- (5a);
- the specified value of \\(\delta\\);
- nonvanishing of selected pivot minors.

For the spectral condition, the maximal minors are polynomials in \\(\lambda\\), with coefficients polynomial or rational in the chart variables. After clearing chart denominators, the gcd-one condition can be expressed by a polynomial Bézout identity:

\\[ u_1(\lambda)m_1(\lambda)+\cdots+ u_t(\lambda)m_t(\lambda)=1. \\]

There is a useful degree-bound observation here. Suppose the maximal minors have degree at most \\(d\\) in \\(\lambda\\), and at least one is nonzero. If their gcd is one, a generic constant linear combination of the minors can be chosen to be coprime to a selected nonzero minor. The resulting two-polynomial Bézout identity can be taken with coefficient degrees less than \\(d\\). Thus one does not need unrestricted-degree auxiliary polynomials.

This makes it plausible to introduce finitely many auxiliary coefficient variables and impose the identity coefficient by coefficient. With real rational input and real augmentation variables, this gives a natural route to an existential-real-algebraic formulation.

I would therefore regard

\\[ \boxed{\text{membership in }\exists\mathbb R} \\]

as a reasonable target for the decision problem, subject to writing out the chart encoding and the Bézout degree argument carefully.

This is an upper-bound direction, not a hardness result.

### 5.4 What hardness question should be attacked?

I would not initially try to prove hardness for the full problem. First isolate the source of difficulty.

There are three possible subproblems:

1. Geometric feasibility: Does the admissible intermediate stratum contain any subspace satisfying (5a)?
2. Spectral feasibility for a fixed subspace: Does a specified quotient pencil have full column rank at every finite complex \\(\lambda\\)?
3. Joint synthesis: Does there exist a subspace in the intermediate stratum whose quotient pencil satisfies the spectral condition?

The second problem is not a promising hardness target: for a fixed candidate, the maximal-minor gcd can be computed by exact polynomial arithmetic.

The third is the genuinely interesting problem because the subspace variables and the spectral condition interact.

My recommended order is:

- establish a clean \\(\exists\mathbb R\\) encoding;
- study whether the geometric feasibility subproblem is tractable;
- then attempt hardness for the joint synthesis problem;
- use a restricted family only if it preserves the actual quotient-pencil structure.

A reduction from an unrelated matrix-completion problem is not enough. The reduction must preserve the constraints that arise from \\((A,C,L_0)\\), the intermediate stratum, and the induced pencil.

I would target variable \\(n\\) with small fixed \\(p,r\\), rather than claiming hardness with all dimensions literally fixed. If every matrix dimension is fixed, the number of scalar variables is fixed as well, so the usual asymptotic complexity question becomes much less meaningful.

## 6. M1 — Is chart sampling acceptable, or must every scan be symbolic?

The answer is: chart sampling is acceptable for exact finite verification, but not for universal statements about the Grassmannian.

The distinction should be made explicit in the terminology.

### 6.1 What exact chart sampling proves

Suppose you enumerate every standard Grassmannian chart and choose finitely many exact rational parameter values in each chart.

For each sampled point, you can verify exactly:

- the subspace is correctly represented;
- all admissibility conditions hold;
- the value of \\(\delta\\) is correct;
- (5a) holds;
- the maximal-minor gcd is one or nonconstant.

This is genuine exact computation. It is stronger than floating-point numerical experimentation.

But it proves a statement only about the sampled points. It does not prove that every point in the chart, or every point in the Grassmannian, has the same property.

In particular, the following inference is invalid:

\\[ \text{Every sampled point in every chart is feasible} \quad\Longrightarrow\quad \text{Every point in the Grassmannian is feasible}. \\]

A finite collection of exact samples cannot establish that implication.

### 6.2 Recommended terminology for the paper

I suggest using the following hierarchy.

| Label                                | What has been checked                                            | What may be concluded                                          |
| ------------------------------------ | ---------------------------------------------------------------- | -------------------------------------------------------------- |
| `[Exact instance verification]`      | One specified rational candidate                                 | That candidate has the stated exact properties                 |
| `[Finite chart-sample verification]` | A finite set of exact points sampled from all listed charts      | Every sampled point has the reported property                  |
| `[Exact finite enumeration]`         | Every point in a genuinely finite candidate set                  | The conclusion holds on that finite set                        |
| `[Symbolic chart verification]`      | A polynomial or rational identity/criterion over chart variables | The conclusion holds throughout the specified chart domain     |
| `[Whole-family theorem]`             | A mathematical proof covering the full family                    | The conclusion holds for every admissible member of the family |

The phrase “enumerate all Grassmannian charts” should not be used to suggest that the Grassmannian itself has been enumerated. A chart is an affine parameter space, usually containing infinitely many points.

### 6.3 When symbolic computation is essential

Symbolic computation is necessary when the intended claim is:

- every point of a chart is feasible;
- an entire stratum is feasible;
- the failure locus is empty;
- a family has a fixed \\(q\_{\min}\\) for all parameter values;
- a universal bound holds over a parameterized class.

For such claims, computing the gcd over

\\[ \mathbb Q(\theta)[\lambda] \\]

is a reasonable method when the chart parameters are \\(\theta\\). But even that needs care:

- denominators must be tracked;
- the chart domain must be specified;
- specializations where leading coefficients vanish must be handled;
- a generic symbolic result need not cover exceptional parameter values.

In particular, a gcd computation over the rational function field \\(\mathbb Q(\theta)\\) establishes a generic statement on the chart, not automatically a statement at every specialization of \\(\theta\\).

For whole-family claims, I would distinguish:

1. generic chart feasibility, proved over \\(\mathbb Q(\theta)\\);
2. all-specialization feasibility, requiring control of exceptional parameter loci as well.

This distinction is essential for the spectral condition because finite roots can appear or disappear under specialization.

### 6.4 Sampling is especially delicate on thin sets

The report correctly flags that some of the relevant sets may be thin.

There are two separate issues:

- the admissible family itself may be a lower-dimensional subset of an ambient Grassmannian chart;
- the spectral-failure or spectral-feasibility locus may be a lower-dimensional constructible subset within that admissible family.

Uniformly sampling the ambient chart and then retaining points satisfying several exact constraints may give a very poor representation of the actual admissible stratum. In some situations it may miss the relevant set entirely.

I recommend parameterizing the constrained family as directly as possible, then sampling within its own charts or parameter spaces.

Also record whether samples are:

- independently random rational points;
- a fixed deterministic grid;
- selected structured points;
- points generated by a family-specific construction.

These are not interchangeable sampling methods.

### 6.5 The independent cross-check is valuable, but qualify its independence

The report says that each verdict is cross-checked by an observability formulation and a maximal-minor gcd.

This is good engineering practice. However, if both criteria are derived from the same quotient-pencil equivalence, they are mathematically equivalent tests, not logically independent proofs.

I would describe them as independent implementations of equivalent criteria. That is still valuable: it helps catch programming errors in basis construction, polynomial extraction, rank calculation, and gcd computation.

A stronger validation scheme would add known positive and negative test cases:

- the terminal-order construction;
- a candidate on the \\(\delta=0\\) boundary;
- a candidate on the \\(\delta=\rho\\) boundary;
- an exact intermediate-stratum feasible candidate;
- an exact intermediate-stratum infeasible candidate;
- examples where the pencil has a finite root of multiplicity greater than one;
- examples where the rank drops only at a nonreal root.

The last case is particularly useful because a numerical scan over real \\(\lambda\\) would not detect it.

## 7. M2 — A mandatory verification checklist

The current assertions are a substantial improvement. I would turn them into a formal precondition-and-postcondition checklist, with the following additional items.

### 7.1 Input and dimension checks

Before constructing candidates, assert:

\\[ \operatorname{rank}C=p, \qquad \operatorname{rank}\begin{bmatrix}C\\\L_0\end{bmatrix}=p+r. \\]

Also assert the relevant observability ranks:

\\[ \operatorname{rank}\mathcal O_C=n, \qquad \operatorname{rank}\mathcal O\_{L_0}=n, \\]

when both are part of the standing assumptions for the experiment.

Do not silently assume that a generated random matrix has the intended rank or observability property.

### 7.2 Candidate admissibility and target inclusion

For every candidate \\(\mathcal L\\), assert:

\\[ \operatorname{rank}\begin{bmatrix}C\\\\\mathcal L\end{bmatrix}=p+q, \\]

and

\\[ \operatorname{row}L_0\subseteq\operatorname{row}\mathcal L. \\]

The latter can be checked by a rank identity, for example

\\[ \operatorname{rank} \begin{bmatrix} \mathcal L\\\L_0 \end{bmatrix} = \operatorname{rank}\mathcal L. \\]

Also record the dimensions of all spaces used in the calculation, not merely their ranks in isolation.

### 7.3 Geometry checks

Compute

\\[ V=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \qquad \mathcal Z=\ker\begin{bmatrix}C\\\\\mathcal L\end{bmatrix}, \qquad \mathcal V=\mathcal Z^\perp. \\]

Then assert the duality identities:

\\[ \dim V=n-r_1, \qquad \dim\mathcal Z=n-(p+q), \qquad \dim\mathcal V=p+q. \\]

If \\(B\\) is a full-row-rank basis matrix for \\(\operatorname{row}[CA;C]\\), assert

\\[ \ker B=V. \\]

Also check that the constructed \\(\mathcal Z\\) really is the kernel of the intended matrix. This sounds elementary, but it is precisely the kind of construction mismatch that caused the earlier bug.

### 7.4 The three-way \\(\delta\\) assertion

This is the most important new assertion:

\\[ \boxed{ \delta = h-(p+q) = \dim D-\dim(D\cap\mathcal V) = \dim\bigl(D/(D\cap\mathcal V)\bigr). } \\]

Compute the value in at least two independent ways and assert equality.

Then check

\\[ 0\leq\delta\leq\rho, \qquad \rho=r_1-p. \\]

If any of these identities fails, the program should stop rather than continue with a spectral test.

### 7.5 The (5a) check

Verify (5a) directly as a row-space inclusion:

\\[ \operatorname{row}(\mathcal LA) \subseteq \mathcal V+D. \\]

Equivalently,

\\[ \operatorname{rank} \begin{bmatrix} \mathcal L\\\CA\\\C\\\\\mathcal LA \end{bmatrix} = \operatorname{rank} \begin{bmatrix} \mathcal L\\\CA\\\C \end{bmatrix}. \\]

This is a useful implementation-independent check against a computed coefficient representation.

### 7.6 Quotient-pencil checks

Before computing the maximal minors, assert:

\\[ \dim(V/S)=q+\delta-\rho, \qquad \dim(X/\mathcal Z)=p+q. \\]

Thus the reduced pencil has dimensions

\\[ (p+q)\times(q+\delta-\rho). \\]

Also verify that the induced maps are well-defined on the quotient, that \\(S\\) is contained in the relevant kernels, and that the chosen quotient bases have the stated dimensions.

A basis error here can produce a perfectly consistent gcd for the wrong pencil.

### 7.7 Spectral checks

For every fixed candidate:

1. Compute all maximal minors exactly.
2. Remove identically zero minors.
3. Compute their polynomial gcd over the exact coefficient field.
4. Normalize the gcd to a canonical form.
5. Check the zero-column-domain case separately.
6. If the gcd is nonconstant, record at least one exact algebraic root or a factor witnessing the failure.
7. If the gcd is one, record the exact certificate or the computed gcd output.

For rational input, \\(\mathbb Q[\lambda]\\) is sufficient for the gcd calculation: a collection of rational polynomials has a nonconstant common factor over \\(\mathbb C\\) if and only if it has one over \\(\mathbb Q\\).

### 7.8 Metamorphic and regression tests

I would add tests that preserve the mathematical problem but change its representation:

- replace a basis of \\(\operatorname{row}\mathcal L\\) by another basis;
- replace a basis of \\(V\\), \\(S\\), or \\(X/\mathcal Z\\);
- apply invertible coordinate transformations to the state space;
- permute rows in the matrices defining the same row spaces;
- replace the pencil by an equivalent pencil under constant invertible row and column transformations.

The output classification must remain unchanged.

This is a powerful way to detect errors that ordinary rank assertions do not catch.

### 7.9 A final implementation rule

Every reported numerical or exact result should carry a record of:

- the original input matrices;
- the random seed or deterministic sample identifier;
- the chart identifier;
- the chart parameter values;
- the computed ranks and dimensions;
- the \\(\delta\\)-stratum;
- the spectral gcd;
- the software and exact-arithmetic backend version.

This will make the experiments reproducible and allow an independent researcher to audit an individual result without rerunning the entire scan.

## 8. M3 — How much evidence is enough for a conjecture?

There is no universal sample-size threshold. In this problem, the geometry of the relevant sets matters much more than whether the sample count is \\(10^3\\), \\(10^4\\), or \\(10^6\\).

A large sample can be misleading if the property of interest is concentrated on a thin algebraic set that the sampling distribution almost never reaches.

### 8.1 Separate four levels of evidence

I recommend the following terminology.

Level 1 — Empirical regularity

A pattern appears in a finite collection of exact samples.

Example:

\\[ \text{All 1,107 sampled intermediate-stratum candidates passed (5b).} \\]

This is a legitimate and useful statement. It is not a theorem.

Level 2 — Exact parameterized examples

A family of examples is constructed and checked exactly for all values in a specified parameter range.

For example, a family indexed by an integer \\(m\\) with a rigorously computed minimum-order gap \\(g(m)\\).

This is stronger than isolated examples because it reveals a structural mechanism. It still does not prove a universal bound over all systems.

Level 3 — Structural conjecture with adversarial testing

A conjecture is motivated by a structural argument and has survived targeted attempts to falsify it, including boundary cases and parameterized examples.

At this level it is reasonable to state a conjecture in a paper, provided the empirical evidence and the remaining proof gap are clearly identified.

Level 4 — Theorem

A complete proof establishes the assertion for all systems satisfying the stated hypotheses.

These labels should not be collapsed into a single phrase such as “experimentally verified.”

### 8.2 Should every conjecture have a parameterized family?

I would recommend it for every structural conjecture in this project, but with a qualification.

A parameterized family should serve one of two purposes:

1. Positive evidence: demonstrate a mechanism that produces the conjectured behavior for a nontrivial range of parameters.
2. Falsification: vary a parameter that is expected to control the behavior and search for the first value where the conjecture fails.

A family that merely reproduces one finite example does not add much.

For the bounded-gap conjecture, the most useful families would vary:

- the length of the observability profile;
- the tail \\((\Delta_2,\Delta_3,\ldots)\\);
- the spectral multiplicities of \\(A\\);
- the relative position of \\(L_0\\) and \\(C\\);
- the candidate order.

The goal is not simply to generate many examples. It is to expose which structural feature controls the gap.

### 8.3 A falsification-first experimental strategy

For each conjecture, I would maintain a table of the following form:

| Conjecture                              | Exact examples | Random samples | Adversarial families | Known boundary cases          | Status                  |
| --------------------------------------- | -------------- | -------------- | -------------------- | ----------------------------- | ----------------------- |
| Gap \\(\leq2\\) for \\(\rho=2\\)        | count          | count          | count                | specified                     | empirical / conjectural |
| Gap bounded by \\(f(\rho)\\)            | count          | count          | count                | \\(\rho=1\\) case             | conjectural             |
| Intermediate candidates always feasible | count          | count          | count                | both boundary strata excluded | empirical / conjectural |

The exact counts should be accompanied by the parameter ranges and generation method.

In particular, I would prioritize adversarial constructions over simply increasing random sample size. The strongest evidence against a universal conjecture often comes from a carefully designed family, not a much larger random experiment.

## 9. Part IV — Two statements that should be made more prominently

### 9.1 The terminal-order theorem should have its own explicit hypothesis block

The report is correct to identify the canonical assumptions as

\\[ (C,A)\text{ observable}, \qquad \operatorname{rank}\begin{bmatrix}C\\\L_0\end{bmatrix}=p+r. \\]

Under these assumptions, there exists a terminal augmentation of order \\(q=n-p\\), so

\\[ \boxed{q\_{\min}\leq n-p.} \\]

The construction is worth recording in a compact form.

Because the row spaces of \\(C\\) and \\(L_0\\) are disjoint, extend \\(\operatorname{row}L_0\\) to a subspace \\(U\\) of dimension \\(n-p\\) such that

\\[ U\cap\operatorname{row}C=\\{0\\}. \\]

Choose \\(\mathcal L\\) whose rows form a basis of \\(U\\). Then

\\[ T=\begin{bmatrix}C\\\\\mathcal L\end{bmatrix} \\]

is invertible.

Condition (5a) is automatic because the rows of \\(T\\) span the whole state-space dual.

For (5b), write

\\[ TAT^{-1} = \begin{bmatrix} A\_{11}&A\_{12}\\\ A\_{21}&A\_{22} \end{bmatrix}, \\]

with the first block row corresponding to \\(C\\). Constant row and column transformations reduce the relevant rank test to

\\[ \operatorname{rank} \begin{bmatrix} \lambda I\_{n-p}-A\_{22}\\\ A\_{12} \end{bmatrix} =n-p \quad\forall\lambda\in\mathbb C. \\]

By PBH, this is equivalent to observability of \\((C,A)\\).

An important point should be stated explicitly:

> The terminal-order existence theorem does not require observability of \\((L_0,A)\\).

If the global problem assumes observability of \\((L_0,A)\\), that assumption remains part of the global problem, but it is not needed for this particular terminal construction.

### 9.2 The two boundary lemmas should appear before the \\(\delta\\)-trichotomy

The most natural logical sequence is:

1. define \\(\rho\\) and \\(\delta\\);
2. prove the equality obstruction \\(\delta=\rho\\);
3. prove the invariance obstruction \\(\delta=0\\) for subterminal orders;
4. deduce the intermediate-stratum theorem;
5. use \\(\rho\leq p\\) to obtain the terminal-only result when \\(\rho\leq1\\).

This order makes the argument transparent. The reader sees why each boundary fails before being told that only the intermediate region can remain.

### 9.3 The terminal-only classification is stronger than the \\(p=1\\) corollary

Since

\\[ \rho\leq p, \\]

the condition \\(\rho\leq1\\) includes the entire \\(p=1\\) case. The stronger result is

\\[ \boxed{ \rho\leq1 \quad\Longrightarrow\quad q\_{\min}=n-p, } \\]

under the canonical assumptions.

For a nontrivial observable system with \\(n>p\\), one in fact has \\(\rho\geq1\\): if \\(\operatorname{row}(CA)\subseteq\operatorname{row}C\\), then \\(\operatorname{row}C\\) is \\(A\\)-invariant, contradicting observability unless \\(n=p\\).

Thus, in the usual nontrivial setting, the terminal-only regime is precisely

\\[ \rho=1. \\]

This is a cleaner theorem to present than a result restricted to \\(p=1\\).

## 10. What I would revise in the report before the next research round

I would make the following concrete edits.

| Location | Recommended revision                                                                     |
| -------- | ---------------------------------------------------------------------------------------- |
| Part I.1 | Retain `[Lean-conditional]`; add a theorem-to-Lean hypothesis mapping table              |
| Part I.3 | Clarify whether 1,905 is the number of retained candidates, feasible candidates, or both |
| Part I.4 | Reconcile 766 versus 745 samples and state the sampling subset                           |
| Part I.5 | Make the three equivalent formulas for \\(\delta\\) explicit                             |
| Part I.5 | State 1107/1107 as a finite-sample observation, not a universal result                   |
| Q1       | Define \\(q_0\\) before discussing the bounded-gap conjecture                            |
| Q1       | Test \\(\rho\\)-only versus profile-dependent bounds                                     |
| Q2       | Correct \\(p=r=1\\) to a compatible example, such as \\(p=2,\rho=2\\)                    |
| Q2       | Prefer the fixed-\\(A\\), variable-\\(C\\) construction to isolate profile effects       |
| Q3       | State the exact decision problem and develop the Bézout/\\(\exists\mathbb R\\) encoding  |
| M1       | Distinguish finite chart-sample verification from symbolic chart verification            |
| M1       | Track specializations and chart denominators in symbolic computations                    |
| M2       | Add quotient-pencil dimension checks and metamorphic tests                               |
| M3       | Use parameterized families and adversarial tests, not only larger random samples         |
| Part IV  | Promote B.22, B.28(3), and terminal-order existence to standalone theorems               |

## 11. Recommended priorities for the next research round

I would not pursue all three open questions simultaneously. The most efficient sequence is the following.

Priority 1 — Stabilize the mathematical and computational definitions

- Freeze the canonical definition of \\(\delta\\).
- Add the three-way \\(\delta\\)-assertion to every candidate calculation.
- Reconcile the 1,905 and 745/766 counts.
- Make B.22 and B.28(3) standalone lemmas.
- Ensure the terminal branch is treated separately.

Immediate

Priority 2 — Investigate the first nontrivial profile case

Fix \\(\rho=2\\), and compare profiles with identical \\(n,p,r\\). Start with the fixed-\\(A\\), variable-\\(C\\) construction:

\\[ (2,2)\quad\text{versus}\quad(2,1,1). \\]

Measure separately the geometric delay and spectral delay. This is likely to yield more insight than simply increasing the number of random samples.

Highest research value

Priority 3 — Test the bounded-gap conjecture adversarially

- Define \\(q_0\\) precisely.
- Construct parameterized families with fixed \\(\rho\\) and increasing profile length.
- Search specifically for a gap exceeding the current conjectured bound.
- Compare \\(\rho\\)-only and profile-dependent predictions.

Conjecture testing

Priority 4 — Formalize the complexity problem

Write down the Grassmannian-chart encoding, the polynomial Bézout certificate, and the resulting existential-real-algebraic formulation. Then investigate hardness for variable \\(n\\) and small fixed \\(p,r\\).

Longer-term theory

## 12. Overall assessment

The report is methodologically stronger than the earlier stages. In particular, the correction to \\(\delta\\) is not a minor bookkeeping change: it repairs the interpretation of the strata and therefore the conclusions drawn from the computational statistics.

The central structural picture is now coherent:

\\[ \begin{aligned} &\delta=0 &&\Longrightarrow \text{no subterminal feasible candidate},\\\ &\delta=\rho &&\Longrightarrow \text{spectral failure},\\\ &1\leq\delta<\rho &&\Longrightarrow \text{the only possible subterminal feasible region}. \end{aligned} \\]

The last line is a necessary geometric restriction, not yet a sufficient feasibility theorem. The new 1107/1107 observation is promising, but it should motivate a search for a structural explanation rather than be treated as one.

I would also emphasize one conceptual point in the paper: the project has moved beyond merely searching for a minimum-order augmentation. It is now studying the interaction between constrained Grassmannian geometry and pointwise spectral regularity of an induced pencil. That is the more distinctive mathematical contribution.

The most useful next document would be a controlled-experiment report for \\(\rho=2\\), with the two profiles above, a fixed \\(A\\), and a fixed \\(L_0\\). It would directly address Q1 and Q2 while providing data for the complexity and genericity questions.

One clarification needed before I can assess Q1 quantitatively: what is the exact definition of \\(q_0\\) used in the gap \\(q\_{\min}-q_0\\)? Once that is fixed, the bounded-gap conjecture can be stated precisely and tested against the terminal-only theorem.

I can also help turn the recommendations above into a concrete experimental specification, including exact matrix constructions, assertions, sampling protocol, and the tables needed for a publishable report.