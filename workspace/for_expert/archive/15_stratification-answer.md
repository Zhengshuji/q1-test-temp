# Review of `15_stratification.md`

The report makes a substantial advance. In particular, it has clarified that the rank of the compressed pencil and the spectral feasibility condition are not interchangeable, refuted a plausible but false conjecture about the middle strata, and produced a more precise formulation of the remaining decision problem.

My overall assessment is:

1. The stratification by \\(s=\dim(V\cap\mathcal Z)\\) is mathematically complete as a bookkeeping stratification, but it is not a useful spectral classification by itself.
2. There is a more promising intrinsic stratification: stratify the induced pencil by its finite generalized eigenstructure, or equivalently stratify the bad incidence variety by the dimension and geometry of its fibers.
3. The constrained subpencil problem should now become the principal research target. However, the formulation in Q2 needs one important correction: when \\(s>0\\), the pencil on \\(V\\) has a permanent kernel \\(S\\), so the correct full-column-rank problem is on the quotient domain \\(V/S\\), not on all of \\(V\\).
4. The \\(67\\%\\) versus \\(25\\%\\) experiment is useful evidence that the structured geometry matters, but it is not yet evidence of computational hardness.
5. The permanently rank-deficient yet feasible example deserves a formal proposition or lemma, not merely a remark, because it rules out a tempting but incorrect class of spectral tests.

I will discuss each question in turn. I will distinguish what follows rigorously from the report from the additional research directions I recommend.

## 1. Q1 — Is the stratification programme finished?

### 1.1 The \\(s\\)-stratification has reached its natural limit

The report establishes

\\[ S=V\cap\mathcal Z,\qquad \ker J\_{\mathcal Z}=S, \\]

and hence

\\[ \operatorname{rank}(J\_{\mathcal Z}|\_V)=\dim V-s. \\]

This is a natural stratification of the admissible Grassmannian by the intersection dimension with \\(V\\). It is useful for at least three purposes:

- organizing the admissible set into finitely many locally closed pieces;
- simplifying the algebraic encoding by replacing a rank condition with finitely many cases;
- identifying the extreme cases \\(s=0\\) and \\(s=\dim V\\).

But the report has now demonstrated that it cannot, by itself, classify spectral feasibility. The counterexample with \\(s=1\\), \\(q=1\\), (5a) satisfied and (5b) violated is decisive against the conjecture that all middle strata are feasible.

The structural explanation is also correct in spirit: the dimension of \\(U=\mathcal LV\\) does not determine its position relative to the relevant eigenstructure. Two subspaces of the same dimension can have different intersections with the relevant eigendirections.

I would therefore regard the original \\(s\\)-stratification programme as complete for its intended purpose. I would not spend another major research cycle trying to extract a spectral criterion from \\(s\\) alone.

There is, however, a better refinement.

### 1.2 Replace dimension strata by eigenstructure-incidence strata

The report gives the equivalent observability formulation

\\[ (5b)\iff (E,\Lambda)\text{ is observable}, \qquad \ker E=\mathcal LV. \\]

For a fixed pair \\((E,\Lambda)\\), the PBH criterion says that observability fails precisely when there is an eigenvalue \\(\mu\\) of \\(\Lambda\\) and a nonzero vector \\(u\\) such that

\\[ \Lambda u=\mu u,\qquad Eu=0. \\]

Equivalently,

\\[ \ker E\cap\ker(\Lambda-\mu I)\ne\\{0\\} \\]

for some \\(\mu\in\sigma(\Lambda)\\).

Thus the relevant geometric information is not merely \\(\dim\ker E\\), but the position of \\(\ker E\\) relative to the eigenspaces of \\(\Lambda\\).

For a fixed \\(\Lambda\\), this suggests the following refined stratification. Let its distinct eigenvalues be \\(\mu_1,\ldots,\mu_t\\), and write

\\[ \mathcal E_i=\ker(\Lambda-\mu_i I). \\]

Then stratify the possible kernels \\(U=\ker E\\) by the intersection data

\\[ \rho_i(U)=\dim(U\cap\mathcal E_i), \qquad i=1,\ldots,t. \\]

The failure locus is exactly the union of the strata for which at least one \\(\rho_i(U)\\) is positive.

This is a genuine simplification for a fixed \\(\Lambda\\): it replaces a quantified eigenvalue condition by finitely many intersection conditions, one for each distinct eigenvalue.

There is an important qualification. In your augmentation problem, \\(\Lambda\\) is part of a representation of (5a), and may depend on the candidate augmentation and on the chosen representation. Consequently, I would not yet regard the \\(\rho_i\\)-stratification as an intrinsic stratification of the original admissible Grassmannian. It is a useful representation-level description, but the induced-pencil formulation is safer for a global theorem.

### 1.3 The intrinsic alternative: stratify the bad incidence variety

The most promising formulation remains

\\[ N\_{\mathcal Z}(\lambda) =T\_{\mathcal Z}-\lambda J\_{\mathcal Z}. \\]

The report gives

\\[ (5b)\text{ fails} \iff \exists\lambda: \ker N\_{\mathcal Z}(\lambda)\not\subseteq S. \\]

This suggests studying the incidence set

\\[ \mathfrak I= \left\\{ (\mathcal Z,[x],\lambda): \begin{array}{l} \mathcal Z\in\mathscr G,\quad [x]\in\mathbb P(V/S),\\\ (\lambda I-A)x\in\mathcal Z \end{array} \right\\}, \\]

where the notation \\([x]\in\mathbb P(V/S)\\) means that \\(x\\) represents a nonzero class modulo \\(S\\). More carefully, this incidence relation should be expressed using the induced map on the quotient, as explained in Section 2 below.

Projecting \\(\mathfrak I\\) onto the \\(\mathcal Z\\)-coordinate gives the bad locus. This leads to a more informative classification than the \\(s\\)-stratification:

- fiber dimension: how many projective classes \\([x]\\) cause failure for a given \\(\mathcal Z\\);
- eigenvalue multiplicity: whether the failure is associated with isolated or repeated finite generalized eigenvalues;
- rank-drop multiplicity: the order of vanishing of the relevant maximal minors;
- projection behavior: whether a component of the incidence variety projects dominantly onto an admissible Grassmannian component.

The last item is especially important for whole-family counterexamples. A candidate can fail at an isolated parameter value without implying that every candidate fails. Conversely, a component of the incidence variety that dominates the entire admissible Grassmannian would provide a structural route to proving whole-family infeasibility.

Recommendation for Q1: close the \\(s\\)-stratification section. Add a short subsection introducing eigenstructure-incidence stratification as the next framework, but do not attempt to classify every possible eigenstructure stratum before you have established the basic constrained-pencil complexity result.

## 2. Q2 — How should the constrained subpencil problem be attacked?

This is the central question. Before discussing algorithms and complexity, I want to correct the formulation.

### 2.1 A necessary correction: pass to \\(V/S\\)

The report defines

\\[ N\_{\mathcal Z}(\lambda) =T\_{\mathcal Z}-\lambda J\_{\mathcal Z} :V\longrightarrow X/\mathcal Z. \\]

It also establishes, from (5a),

\\[ A(S)\subseteq\mathcal Z. \\]

Since \\(S\subseteq\mathcal Z\\), this implies, for every \\(x\in S\\),

\\[ J\_{\mathcal Z}x=0,\qquad T\_{\mathcal Z}x=0. \\]

Therefore

\\[ S\subseteq\ker N\_{\mathcal Z}(\lambda) \qquad\text{for every }\lambda. \\]

This has an immediate consequence:

\\[ s>0 \quad\Longrightarrow\quad N\_{\mathcal Z}(\lambda) \text{ is never full column rank on }V. \\]

So the decision problem in Q2, if interpreted literally as asking for full column rank on all of \\(V\\), cannot be equivalent to (5b) on the middle strata.

The correct construction is to factor through the quotient domain. Because both \\(J\_{\mathcal Z}\\) and \\(T\_{\mathcal Z}\\) vanish on \\(S\\), they induce maps

\\[ \overline J\_{\mathcal Z}:V/S\longrightarrow X/\mathcal Z, \qquad \overline T\_{\mathcal Z}:V/S\longrightarrow X/\mathcal Z. \\]

Define the reduced pencil

\\[ \boxed{ \overline N\_{\mathcal Z}(\lambda) = \overline T\_{\mathcal Z} -\lambda\overline J\_{\mathcal Z} : V/S\longrightarrow X/\mathcal Z. } \\]

Then

\\[ \ker\overline N\_{\mathcal Z}(\lambda) = \ker N\_{\mathcal Z}(\lambda)/S. \\]

Consequently,

\\[ \boxed{ (5b)\text{ holds} \iff \overline N\_{\mathcal Z}(\lambda) \text{ is injective for every }\lambda\in\mathbb C. } \\]

This is the right formulation for all strata, including \\(s>0\\).

It also unifies the two extreme cases:

- If \\(s=0\\), then \\(V/S=V\\), and we recover the original pencil.
- If \\(s=\dim V\\), then \\(V/S=\\{0\\}\\), so injectivity is automatic, exactly as in the report.

This quotient construction should be made explicit in the paper. It is more than a notational improvement: it removes the permanent kernel and gives a single spectral criterion valid across all strata.

### 2.2 Distinguish normal rank from pointwise full column rank

There is a second subtlety.

For a polynomial matrix \\(P(\lambda)\\), the statement

\\[ \operatorname{rank}\_{\mathbb C(\lambda)}P(\lambda) =\text{number of columns} \\]

means full normal rank. It does not imply full column rank at every finite \\(\lambda\\).

Your condition requires

\\[ \operatorname{rank}\overline N\_{\mathcal Z}(\lambda) =\dim(V/S) \qquad\forall\lambda\in\mathbb C. \\]

This is stronger.

For a polynomial matrix with at least as many rows as columns, pointwise full column rank at every finite complex \\(\lambda\\) is equivalent to the maximal minors having no common finite complex root. Equivalently, their gcd is a nonzero constant.

Thus the exact test is

\\[ \boxed{ \gcd\\{\text{maximal minors of }\overline N\_{\mathcal Z}(\lambda)\\} \in\mathbb C^\times. } \\]

The convention for a zero-dimensional domain should be stated separately: when \\(V/S=\\{0\\}\\), the condition is vacuous and the candidate is feasible.

This distinction matters for the algorithmic problem. A Kronecker canonical form determines the generic structure of a pencil, but the requirement that no finite parameter value causes a rank drop is a specific spectral condition. A reduction or algorithm must preserve that distinction.

### 2.3 What exactly is the constrained problem?

I would formulate the central decision problem as follows.

Constrained pointwise-injective subpencil problem.

Input:

- a linear map \\(A:X\to X\\);
- fixed subspaces \\(V,K\le X\\);
- an integer \\(d\\);
- any additional prescribed incidence constraints defining the admissible family \\(\mathscr G\\).

Question: does there exist

\\[ \mathcal Z\in\mathscr G \\]

such that the induced pencil

\\[ \overline N\_{\mathcal Z}(\lambda): V/(V\cap\mathcal Z)\to X/\mathcal Z \\]

is injective for every \\(\lambda\in\mathbb C\\)?

This is more precise than simply saying “constrained deflation.” It makes clear that the unknown subspace controls both the domain quotient and the codomain quotient.

That coupling is likely the central source of difficulty.

### 2.4 Why the unconstrained Kronecker problem does not settle this problem

For a fixed pencil, Kronecker canonical form provides a structural classification of its regular and singular parts. But here \\(\mathcal Z\\) is not given: it must be selected from a prescribed Grassmannian family, and the same \\(\mathcal Z\\) determines the quotient maps.

So there are two nested problems:

1. for a fixed \\(\mathcal Z\\), test the spectral condition;
2. choose \\(\mathcal Z\\) so that the condition holds.

The first is a polynomial-time algebraic computation in the input size, using maximal minors and a polynomial gcd (assuming exact arithmetic over an appropriate effective field).

The second is a geometric search problem over a Grassmannian with a polynomially defined bad locus.

This is the distinction I would emphasize. A polynomial algorithm for the fixed-pencil test does not automatically give a polynomial algorithm for the existential subspace-selection problem.

### 2.5 Which direction should the complexity reduction take?

I recommend investigating both directions initially, but with different priorities.

Priority A: reduce a known hard subspace-selection problem to your problem.

This is usually the more direct route to a hardness theorem. You would start with a problem whose unknown is a subspace subject to incidence or rank constraints, then encode its feasible solutions as admissible \\(\mathcal Z\\)'s.

The reduction must ensure that:

- every source solution gives an admissible \\(\mathcal Z\\);
- every admissible spectrally feasible \\(\mathcal Z\\) gives a source solution;
- the construction has polynomial encoding size;
- no unintended \\(\mathcal Z\\)'s create false positives.

The most important issue is the last one. It is easy to make a construction in which a source solution yields a feasible augmentation. It is much harder to prove the converse.

Priority B: reduce your problem to a known algebraic-geometric problem.

This is useful for obtaining upper bounds and identifying the correct complexity class. Your problem already has a natural existential algebraic formulation:

- represent \\(\mathcal Z\\) in Grassmannian charts;
- express the incidence constraints algebraically;
- express failure through a witness \\((x,\lambda)\\);
- express feasibility as the nonexistence of such a witness.

The difficulty is that feasibility is a universal condition over \\(\lambda\\), or equivalently a polynomial gcd condition. It is not automatically a simple existential-real formula without additional transformations.

I would therefore separate two tasks:

1. establish a rigorous algebraic upper bound for the decision problem;
2. seek a hardness reduction from a known subspace-selection problem.

Do not jump directly to a hardness claim based on the fact that the problem contains determinants or rank constraints. Determinantal conditions alone are not sufficient evidence of hardness.

### 2.6 Which small-instance classes should be studied first?

I would prioritize the following.

Class I: \\(p=r=1\\), with \\(n\\) variable.

This is the best first simplification. It removes much of the bookkeeping while retaining a nontrivial Grassmannian selection problem.

The key questions are:

- Does the admissible family become a single Grassmannian, or a constrained open subset?
- Can the pencil be represented using a single scalar functional?
- Does the problem reduce to avoiding a projective algebraic set?
- Can the projective incidence criterion be made necessary as well as sufficient in this special case?

If the answer to the last question is yes, this class may be completely classifiable.

Class II: companion-form \\(A\\).

This is also promising, because the action of \\(A\\) on a cyclic basis is explicit. However, companion form alone does not guarantee that the admissible subspace constraints become simple. The important issue is whether the pair \\((A,C)\\) and the prescribed \\(L_0\\) can be simultaneously normalized in a way that preserves the relevant Grassmannian geometry.

I would use companion form as a controlled test class, not as the first general theorem.

Class III: fixed \\(p,r\\), variable \\(n\\).

This is the most meaningful complexity target. It avoids the fixed-dimension obstruction discussed in earlier work while preserving the small-observation/small-target structure that appears central to your examples.

My recommendation: begin with \\(p=r=1\\), then move to fixed \\(p,r\\) and variable \\(n\\). Keep companion-form examples as a separate experimental track.

### 2.7 What does the literature say?

I searched for work specifically on constrained deflation, prescribed-kernel pencil selection, and matrix-pencil completion. I did not find a standard polynomial-time algorithm or a directly matching hardness theorem for the exact problem above. I would not interpret that as proof that none exists; the terminology is not standardized, and closely related problems are often formulated differently.

There is, however, a relevant neighboring literature:

- Dodig and Stošić study the general matrix-pencil completion problem, asking which Kronecker invariants can occur when a prescribed subpencil is extended. They solve a minimal completion case. This is relevant to the structural side of your problem, but it is not the same as selecting a quotient subspace so that a pencil has full pointwise column rank.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://epubs.siam.org\&sz=32)

  工业与应用数学学会+1

- Earlier work on matrix-pencil completion studies prescribed Kronecker invariants and regular subpencils. This may provide useful language and structural tools for analyzing your induced pencil.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

  ScienceDirect+1

- Work on deflating subspaces primarily concerns computing invariant or deflating subspaces of a given pencil, often numerically. That is a different task from choosing an unknown subspace subject to your fixed-\\(V\\), fixed-\\(K\\) incidence constraints.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

  ScienceDirect+1



My conclusion is therefore deliberately conservative:

> The literature located so far does not settle the complexity of your constrained subpencil-selection problem. Matrix-pencil completion is the closest structural neighbor, but a reduction between the two problems would need to be constructed and proved.

I would avoid claiming that “constrained deflation is known to be hard” or that “Kronecker theory gives a polynomial algorithm” until such a bridge is established.

### 2.8 A concrete first attack: incidence geometry

For fixed \\(\mathcal Z\\), failure is witnessed by a nonzero class \\([x]\in\mathbb P(V/S)\\) and a scalar \\(\lambda\\) satisfying

\\[ (\lambda I-A)x\in\mathcal Z. \\]

Because \\(A(S)\subseteq\mathcal Z\\), this condition is independent of the representative of \\(x+S\\).

Consider the incidence variety

\\[ \mathfrak I= \left\\{ (\mathcal Z,[x+S],\lambda): \mathcal Z\in\mathscr G,\  [x+S]\in\mathbb P(V/S),\ (\lambda I-A)x\in\mathcal Z \right\\}. \\]

Its projection onto \\(\mathscr G\\) is precisely the bad locus. This suggests a practical sequence of mathematical tasks:

1. Fix a projective class and a spectral parameter. Determine the set of admissible \\(\mathcal Z\\)'s containing \\((\lambda I-A)x\\).
2. Compute the fiber dimension. This is a Grassmannian incidence calculation, with additional restrictions coming from \\(\mathcal Z\subseteq K\\) and the prescribed dimension.
3. Project over \\([x+S]\\) and \\(\lambda\\). Determine whether the resulting bad locus is proper, dense, or all of a component of \\(\mathscr G\\).
4. Separate generic failure from universal failure. A dense bad locus is not the same as a bad locus equal to the entire admissible family.

This framework is particularly well suited to your existing whole-family counterexamples. Their symbolic chart computations could be interpreted as showing that a certain rank-drop polynomial is independent of the chart parameters. The incidence viewpoint may explain why this happens, rather than merely verifying it.

One further point: the report's phrase “the pencil has full column rank over \\(\mathbb C[\lambda]\\)” should be replaced by “the induced pencil has full column rank at every finite \\(\lambda\in\mathbb C\\).” The latter is the actual condition. It is equivalent to a constant gcd of maximal minors, not merely to full normal rank.

## 3. Q3 — Are you over-structuring the problem?

I would now stop broad structural exploration and make complexity and classification the principal workstream. But I would not abandon structural work altogether.

The project already has several meaningful structural results:

- an exact failure criterion;
- an observability reformulation;
- a dimension obstruction;
- a stratification by \\(s\\);
- a refutation of the middle-strata feasibility conjecture;
- a distinction between generic rank deficiency and actual spectral failure;
- whole-family counterexamples;
- unbounded order gaps.

That is enough to support a coherent structural paper or a substantial structural section of a larger paper.

The next phase should not add more isolated examples or more equivalent reformulations unless they directly contribute to one of the following:

1. a necessary-and-sufficient classification in a meaningful special case;
2. a polynomial-time algorithm;
3. a hardness reduction;
4. a sharper upper bound or lower bound on the complexity of the general decision problem.

### 3.1 The single formulation I would fix

I recommend fixing the following as the main decision problem:

> Constrained pointwise-injective quotient-pencil problem. Given \\(A,V,K,d\\), and the admissibility conditions inherited from the augmentation problem, determine whether there exists an admissible \\(\mathcal Z\subseteq K\\), \\(\dim\mathcal Z=d\\), for which\
> \\[\
> \overline T\_-\lambda\overline J\_\
> \\]\
> is injective for every \\(\lambda\in\mathbb C\\), where the domain is \\(V/(V\cap\mathcal Z)\\).

This formulation is preferable to the unreduced pencil on \\(V\\) because it works uniformly across all \\(s\\)-strata.

I would organize the next phase around three results:

- Upper-bound result: give a rigorous algebraic encoding of this decision problem.
- Special-case result: solve or classify the case \\(p=r=1\\), or a carefully selected companion-form subclass.
- Hardness result or algorithmic theorem: either construct a reduction from a recognized subspace-selection problem, or prove a polynomial algorithm under clearly stated restrictions.

If the complexity result remains elusive, a complete classification for \\(p=r=1\\) would still be a substantial and publishable mathematical result, provided it is genuinely necessary and sufficient.

### 3.2 A practical stop rule

I suggest the following rule for deciding whether to pursue another structural lemma:

- If it improves the quotient-pencil formulation, keep it.
- If it helps compute or characterize the bad incidence variety, keep it.
- If it sharpens the dimension obstruction or explains the unbounded gap construction, keep it.
- If it only gives another equivalent description of the same failure condition, defer it.
- If it is another numerical example without a new mechanism, do not prioritize it.

This should prevent the project from accumulating many technically correct but disconnected observations.

## 4. Q4 — What does the 67% versus 25% control experiment tell us?

The experiment is interesting:

| Group      | Samples | Failures | Rate  |
| ---------- | ------- | -------- | ----- |
| Structured | 537     | 360      | 67.0% |
| Random     | 873     | 216      | 24.7% |

The observed failure-rate ratio is approximately

\\[ \frac{0.670}{0.247}\approx 2.71. \\]

This is evidence that the structured construction of \\(V\\) and \\(K\\) is associated with a substantially higher failure rate in the sampled setting.

However, there are three levels of interpretation, and they should not be conflated.

### 4.1 What the experiment does establish

It establishes an empirical difference between the two sampling procedures, conditional on:

- the chosen dimensions;
- the selected distribution of matrices \\(A,C,L_0\\);
- the chosen procedure for generating structured and random subspaces;
- restriction to the \\(s=0\\) stratum;
- the exact gcd-based failure test.

The experiment is valuable because it weakens the hypothesis that the structured constraints are irrelevant to the observed failures.

### 4.2 What it does not establish

It does not establish that:

- structured instances are harder to decide;
- the structured family has a larger algebraic bad locus in every dimension;
- the failure probability is asymptotically higher;
- the difference is caused by one specific structural feature of \\(V\\) or \\(K\\).

A failure probability is not a complexity measure. A problem may have a high failure rate and still be easy to decide; it may have a low failure rate and still be computationally difficult.

The report is correct to emphasize that classical decidability of an unconstrained pencil is not a statement about the probability of rank failure.

### 4.3 How to make the experiment more informative

I would run three follow-up experiments.

Experiment A: stratify by dimensions.

Repeat the comparison over a grid of dimension tuples, rather than reporting a single pooled rate. In particular, vary

\\[ \dim V,\quad \dim K,\quad d,\quad \dim(V\cap K) \\]

independently where possible.

This will help determine whether the observed ratio is robust or an artifact of one dimension choice.

Experiment B: match the intersection geometry.

The structured and random samples should be matched not only in \\(\dim V\\) and \\(\dim K\\), but also in relevant intersection dimensions and incidence data. Otherwise the two groups may be sampling substantially different geometric regimes.

Experiment C: measure the bad-locus geometry, not only candidate failure.

For each sampled instance, estimate or calculate algebraic properties of the bad locus, where feasible:

- whether it is empty;
- whether it is the whole admissible family;
- whether it has a proper component;
- its codimension when the calculation is tractable.

This would connect the experiment directly to the incidence-variety programme.

### 4.4 Where should a hardness gadget bite?

The experiment suggests a useful heuristic, but not yet a theorem:

> Look for a gadget that exploits the dependence between \\(V\\), \\(K\\), and the action of \\(A\\), rather than a gadget that merely creates an arbitrary matrix pencil.

In particular, a reduction should try to encode combinatorial or algebraic choices through the possible positions of \\(\mathcal Z\\) relative to \\(V\\), \\(K\\), and \\(A(V)\\).

That is a plausible place for the structured problem to acquire complexity absent from the unconstrained pencil test.

I would not use the factor \\(2.7\\) as a parameter in a proof or as evidence of hardness. It is a useful experimental clue about where to search for the mechanism.

## 5. Q5 — Should “permanent rank deficiency is not failure” be a lemma?

Yes. I recommend stating it as a formal proposition.

It is not merely an illustrative numerical observation. It corrects a potentially serious logical error in the analysis of the spectral condition.

The report gives an admissible candidate for which

\\[ \operatorname{rank}N\_{\mathcal Z}(\lambda) =1<\dim V=2 \\]

at all the sampled values of \\(\lambda\\), while (5b) holds. The important point is not the particular sample set: the underlying explanation is that the kernel can be contained entirely in \\(S\\).

I would formulate the result in a slightly stronger, general form.

### Proposition — Permanent kernel and spectral feasibility

Let \\(\mathcal Z\\) be an admissible subspace satisfying (5a), and define

\\[ S=V\cap\mathcal Z,\qquad N\_{\mathcal Z}(\lambda)=T\_{\mathcal Z}-\lambda J\_{\mathcal Z}. \\]

Then

\\[ S\subseteq\ker N\_{\mathcal Z}(\lambda) \qquad\text{for every }\lambda\in\mathbb C. \\]

Moreover,

\\[ \boxed{ (5b)\text{ holds} \iff \ker N\_{\mathcal Z}(\lambda)=S \quad\text{for every }\lambda\in\mathbb C. } \\]

Equivalently, (5b) holds if and only if the induced pencil on \\(V/S\\) is injective at every finite complex parameter.

Proof. Since \\(S\subseteq\mathcal Z\\), we have \\(J\_{\mathcal Z}x=0\\) for every \\(x\in S\\). By (5a), the report establishes \\(A(S)\subseteq\mathcal Z\\), so \\(T\_{\mathcal Z}x=0\\) for every \\(x\in S\\). Therefore \\(N\_{\mathcal Z}(\lambda)x=0\\) for all \\(x\in S\\) and all \\(\lambda\\).

The failure criterion gives

\\[ (5b)\text{ fails} \iff \exists\lambda: \ker N\_{\mathcal Z}(\lambda)\not\subseteq S. \\]

Since \\(S\\) is always contained in this kernel, the negation is exactly

\\[ \ker N\_{\mathcal Z}(\lambda)=S \qquad\forall\lambda. \\]

This proves the result. \\(\square\\)

This proposition is stronger and cleaner than merely saying that rank deficiency does not imply failure. It identifies exactly what the kernel is allowed to be.

### Suggested placement in the paper

I would place the proposition immediately after the general failure criterion, before introducing the \\(s\\)-stratification.

The subsequent discussion can then say:

- On the \\(s=0\\) stratum, the kernel must be zero at every finite \\(\lambda\\), so the ordinary maximal-minor gcd test applies directly.
- On a middle stratum, the kernel must equal \\(S\\), not necessarily zero.
- On the top stratum \\(S=V\\), the condition is automatic.

This makes the three cases logically transparent.

I would use the title “The permanent kernel and the correct quotient-pencil criterion” rather than “Rank-deficiency is not failure.” The latter is memorable, but the former better captures the mathematical result.

## 6. Two additional corrections and refinements to the report

There are two details I would tighten before treating the note as paper-ready.

### 6.1 Refine the phrase “generalised-eigenvector direction”

The report says that if \\(A(S)\subseteq S\\), then observability is contradicted, and concludes that on middle strata \\(S\\) is necessarily a generalized-eigenvector direction.

The first implication is valid:

\\[ S\ne\\{0\\},\quad S\subseteq\ker C,\quad A(S)\subseteq S \\]

would give a nonzero \\(A\\)-invariant subspace inside \\(\ker C\\), contradicting observability of \\((C,A)\\).

But the conclusion that \\(S\\) is a “generalized-eigenvector direction” is stronger than what has been established. What follows directly is only

\\[ A(S)\subseteq\mathcal Z, \qquad A(S)\not\subseteq S \\]

when \\(S\ne0\\).

I would replace that phrase with:

> On every nonzero middle stratum, \\(S\\) is not \\(A\\)-invariant, although (5a) forces \\(A(S)\subseteq\mathcal Z\\). Thus the action of \\(A\\) moves \\(S\\) into the larger admissible kernel \\(\mathcal Z\\), rather than preserving \\(S\\).

This is precise and does not suggest a Jordan-chain or generalized-eigenvector structure that has not yet been proved.

### 6.2 State the whole-family symbolic verification hypotheses explicitly

The report's claim that the two whole-family counterexamples are exhaustive is important. It is stronger than a finite random or rational-grid search.

The use of all standard coordinate charts of

\\[ \operatorname{Gr}(d,K) \\]

and symbolic computations over \\(\mathbb Q(\theta)[\lambda]\\) is the right kind of method.

For the paper, I would explicitly document:

1. why the coordinate charts cover the entire admissible Grassmannian;
2. how the chart variables parameterize every admissible subspace;
3. whether any chart denominators or excluded loci need separate treatment;
4. why the calculated gcd is invariant under the chart changes being used;
5. why the calculation over \\(\mathbb Q(\theta)\\) establishes the claimed result for the intended parameter values;
6. how exceptional parameter values are handled.

The last two points deserve particular care. A symbolic identity over a rational-function field does not automatically establish a statement after every possible specialization of \\(\theta\\): denominators may vanish, and polynomial degrees or ranks can change at exceptional parameter values. If your examples use fixed rational data, this issue may be straightforward, but the proof should say so explicitly.

## 7. Recommended next research plan

I would now divide the work into three tracks, in this order.

Priority 1

Make the quotient-pencil theory definitive

- Prove and publish the permanent-kernel proposition.
- Define the induced pencil on \\(V/S\\).
- State the exact pointwise-injectivity and maximal-minor gcd equivalence.
- Make the distinction between normal rank and pointwise full rank explicit.

Priority 2

Solve the smallest nontrivial constrained case

- Start with \\(p=r=1\\) and variable \\(n\\).
- Determine whether the bad locus has a projective-geometric characterization.
- Investigate companion-form \\(A\\) as a controlled subclass.
- Aim for a necessary-and-sufficient theorem, not just another sufficient obstruction.

Priority 3

Develop the general complexity result

- Formalize the constrained pointwise-injective quotient-pencil problem.
- Establish an algebraic upper bound.
- Investigate reductions from subspace-selection or matrix-pencil completion problems.
- Use the structured-versus-random experiment to guide gadget design, not to support a hardness claim.

## 8. Final assessment

The most important development in this report is not the numerical failure-rate comparison or even the refutation of the middle-strata conjecture. It is the emergence of a clean, uniform mathematical object:

\\[ \boxed{ \overline N\_{\mathcal Z}(\lambda): V/(V\cap\mathcal Z)\longrightarrow X/\mathcal Z. } \\]

The original spectral condition is exactly the requirement that this induced pencil have full column rank at every finite complex parameter.

This formulation resolves the permanent-kernel issue, unifies all \\(s\\)-strata, and isolates the true difficulty: selecting \\(\mathcal Z\\) under the fixed geometric constraints so that the induced pencil avoids every finite rank drop.

That is the problem I would now focus the project around.

My strongest recommendation: make the quotient-pencil formulation the central theorem of the next report, and use \\(p=r=1\\) as the first serious attempt at a complete classification. I would postpone further general stratification until that special case reveals what the constrained geometry is actually doing.

The report is a real step forward. It also provides a good stopping point for the original stratification programme: the next substantial advance should be an algorithm, a classification theorem, or a complexity reduction—not another refinement of the dimension parameter \\(s\\).

15_stratification.md