Research-direction assessment
I agree with the change of objective: the next phase should focus on the complexity of \(q_{\min}\), not on preparing the paper. I would, however, slightly change the order of attack proposed in the report.

My recommended priority is:
1. A — study the canonical Grassmannian formulation, but first identify its exact geometric problem class.
2. B — search systematically for a family of whole-family counterexamples, not just more random examples.
3. D1 — investigate a reduction from quadratic feasibility through the bilinear observability encoding.
4. E — pursue a positive polynomial-time class in parallel, but only under a verifiable structural hypothesis.
5. C — repair the incidence/covering argument only if A or B reveals a useful geometric route.
I would not start with D2 (static output feedback) and would not spend much time refining the existing \(\exists\mathbb R\) encoding unless a specific reduction or algorithm needs it.

The key distinction is between two questions that are easy to conflate:
- Candidate verification: given \(\mathcal L\), can we decide whether it satisfies (5a) and (5b)?
- Minimum-order synthesis: does there exist a suitable \(\mathcal L\) of a given order?
Your observability theorem makes the first question much more manageable. The hard part is the second: choosing a subspace \(\mathcal Z\) while avoiding a family of algebraically defined obstructions.

I would make that synthesis problem—not the pencil computation—the central object of the next phase.
1. Proposal A: the Grassmannian formulation is the right object, with one refinement
Your reformulation is useful:
\[
\exists\,\mathcal Z\in\operatorname{Gr}(d,K)\quad
\forall x\in V\setminus\mathcal Z,\ \forall\lambda\in\mathbb C:
(\lambda I-A)x\notin\mathcal Z,
\]

with (5a) imposed unless it is automatic.

I would call this a Grassmannian incidence-avoidance problem, or more explicitly, a constructible incidence-avoidance problem. I would not yet identify it with a standard named complexity problem.
The exact incidence object
For \(h=n\), so that (5a) is automatic, define
\[
\mathcal B=
\left\{(\mathcal Z,[x],\lambda):
\begin{array}{l}
\mathcal Z\in\operatorname{Gr}(d,K),\\
[x]\in\mathbb P(V),\\
x\notin\mathcal Z,\\
(\lambda I-A)x\in\mathcal Z
\end{array}
\right\}.
\]

Here \(\lambda\) is finite. The bad Grassmannian locus is the projection
\[
\operatorname{Bad}=\operatorname{pr}_{\operatorname{Gr}(d,K)}(\mathcal B).
\]

Then
\[
\mathcal Z\text{ is spectrally feasible}
\iff \mathcal Z\notin\operatorname{Bad}.
\]

This formulation preserves the important condition \(x\notin\mathcal Z\). It also makes clear why the earlier attempt to replace the problem by avoiding a fixed set \(S\subseteq\mathbb P(K)\) was incomplete: whether a point \((\lambda I-A)x\) is bad depends on the source \(x\), including whether that source belongs to \(\mathcal Z\).

By Chevalley's theorem, the projection of a constructible set is constructible. Thus the bad locus is constructible, although not necessarily closed. This is a useful geometric fact, but it does not by itself give a complexity classification.
A useful connection in the literature
There is a nearby notion called variety-evasive subspaces. Guo's 2024 paper studies families of subspaces whose intersections with prescribed varieties have controlled dimension, and connects the problem to polynomial identity testing and rank condensers. 

Springer Nature Link+1

That is related in spirit, but not the same problem. Variety-evasiveness controls intersection dimensions; your condition asks for the absence of a particular incidence witness involving both a source vector and its image under \(\lambda I-A\).

I would use that literature as a source of techniques—Chow forms, incidence varieties, dimension estimates—not as a direct complexity theorem for your problem.
The most important observation about the apparent \(\exists\forall\) structure
The displayed formulation looks like an \(\exists\forall\) problem. But the observability certificate from your previous report gives an existential algebraic description of feasibility for a fixed candidate. After introducing the auxiliary variables, the synthesis problem can also be expressed existentially.

Therefore, I would not infer that the problem has the complexity of a generic \(\exists\forall\) theory merely from this formulation. The quantifier alternation is a natural geometric description, but it is not necessarily an intrinsic complexity barrier.

Verdict on A: retain it as the conceptual formulation. The next useful step is to derive the incidence variety and its projection carefully, then compare its special structure with known Grassmannian and constructible-set problems. Do not spend time looking for a generic \(\exists\forall\)-completeness theorem that may not apply.

2. Proposal B: search for a family, but first characterize \(\varepsilon=0\)
This is the direction I would pursue immediately after A. I think there is a useful matrix-theoretic result available here.

Write
\[
U_0=L_0|_V:V\to\mathbb C^r,\qquad
U_1=L_0A|_V:V\to\mathbb C^r.
\]

Your proportionality locus is
\[
P=\{x\in V:U_0x\wedge U_1x=0\}.
\]

Since \(V\) is an irreducible vector space and \(P\) is algebraic,
\[
\boxed{\varepsilon=0\iff P=V.}
\]

In other words, \(\varepsilon=0\) means that \(U_0x\) and \(U_1x\) are linearly dependent for every \(x\in V\), not merely generically.

This condition has a simple classification.
Proposition: matrix characterization of \(\varepsilon=0\)
For linear maps \(U_0,U_1:V\to\mathbb C^r\), the following are equivalent:
\[
\varepsilon=0
\quad\Longleftrightarrow\quad
U_0x\wedge U_1x=0\quad\forall x\in V.
\]

Moreover, precisely one of the following cases applies:
1. If \(\operatorname{rank}U_0=0\), the condition is automatic, with no restriction on \(U_1\).
2. If \(\operatorname{rank}U_0=1\), the condition is equivalent to
   \[
   \operatorname{im}U_1\subseteq\operatorname{im}U_0.
   \]
3. If \(\operatorname{rank}U_0\ge2\), the condition is equivalent to
   \[
   \boxed{U_1=\alpha U_0\quad\text{for some }\alpha\in\mathbb C.}
   \]
Proof.

If \(\operatorname{rank}U_0=1\), then whenever \(U_0x\ne0\), dependence forces \(U_1x\in\operatorname{im}U_0\). For \(k\in\ker U_0\), choose \(x_0\) with \(U_0x_0\ne0\). Both \(U_1x_0\) and \(U_1(x_0+k)\) lie in \(\operatorname{im}U_0\), so \(U_1k\) does too. Hence \(\operatorname{im}U_1\subseteq\operatorname{im}U_0\). The converse is immediate.

Now suppose \(\operatorname{rank}U_0\ge2\). For every \(x\) with \(U_0x\ne0\), write
\[
U_1x=\alpha_xU_0x.
\]

If \(U_0x\) and \(U_0y\) are independent, applying dependence to \(x+y\) forces \(\alpha_x=\alpha_y\). Using a third vector with independent image handles the case where two nonzero images are proportional. Thus all \(\alpha_x\) are equal to a common \(\alpha\). Finally, if \(k\in\ker U_0\), comparison with two vectors whose \(U_0\)-images are independent forces \(U_1k=0\). Hence \(U_1=\alpha U_0\). The converse is immediate. \(\square\)

This gives a practical test for \(\varepsilon=0\) using only matrix ranks and proportionality:
- rank zero: automatic;
- rank one: compare image spaces;
- rank at least two: test whether the two restricted maps are scalar multiples.
Does this make whole-family failure codimension one?
I would say probably not in general.

For a fixed \(U_0\) of rank at least two, requiring \(U_1=\alpha U_0\) is a strong restriction on the map \(U_1\). If \(U_0\) has rank one, requiring \(\operatorname{im}U_1\subseteq\operatorname{im}U_0\) is also a substantial restriction. These are not naturally codimension-one conditions in the unrestricted space of linear maps.

The actual parameter space is more complicated because \(V=\ker[C;CA]\) itself depends on \(A\), so these rough codimension counts do not establish the codimension in the space of instances. But they do make me skeptical of a universal codimension-one expectation.

I would instead expect different components of the exceptional set, with different codimensions depending on \(\operatorname{rank}(L_0|_V)\).
What to search for
Your current \(n=6,p=r=2\) example has \(\operatorname{rank}U_0=1\), so the structural characterization says that its \(\varepsilon=0\) phenomenon is exactly
\[
\operatorname{im}(L_0A|_V)\subseteq\operatorname{im}(L_0|_V).
\]

That is a much more concrete condition to impose in a structured search.

I would search separately in three regimes:
- \(\operatorname{rank}(L_0|_V)=1\), with \(L_0A(V)\subseteq L_0(V)\);
- \(\operatorname{rank}(L_0|_V)\ge2\), with \(L_0A|_V=\alpha L_0|_V\);
- \(\operatorname{rank}(L_0|_V)=0\), where proportionality is automatic.
For each regime, vary the Jordan structure of \(A\), the relative position of \(C\), and the dimension of \(V\). This is a much better search strategy than unrestricted random sampling.

Verdict on B: retain and prioritize. The matrix characterization above should be proved and implemented before launching the next search.
3. Proposal C: choose C2; do not try to repair C1 first
I would choose C2, the per-\(\mathcal Z\) construction, if you continue this line at all.

The difficulty with C1 is not just that the image is nonclosed. There are two ways a sequence of genuine failure witnesses can degenerate:
1. \(x_j\notin\mathcal Z_j\) can converge to \(x\in\mathcal Z\), so the limiting witness becomes trivial.
2. The finite parameters \(\lambda_j\) can diverge, so the limit represents an infinite-eigenvalue phenomenon rather than a finite spectral obstruction.
These are precisely the boundary effects that make a naive upper-semicontinuity argument insufficient.

Rank is upper-semicontinuous under specialization: rank can drop in a limit. But the statement you need is not simply that a matrix rank drops. You need a nontrivial source vector outside the limiting subspace and a finite \(\lambda\). Upper-semicontinuity does not preserve either condition.

A compactification with \(\lambda\in\mathbb P^1\) could help organize the boundary, but it would introduce the point \(\lambda=\infty\). You would then need to separate the finite-root locus from the infinite-root locus and also control the boundary \(x\in\mathcal Z\). This is a substantial project, not a one-line semicontinuity repair.
Why C2 is more promising
For a fixed \(\mathcal Z\), failure is equivalent to the existence of
\[
x\in V\setminus\mathcal Z,\qquad
(\lambda I-A)x\in\mathcal Z.
\]

If you can construct such an \(x\) for every admissible \(\mathcal Z\) in a particular family, you obtain whole-family failure directly, with no projection-closure argument.

I would look for a formula based on:
- the quotient \(X/\mathcal Z\), where \(X\) is the ambient state space;
- the induced maps from \(V\) into \(X/\mathcal Z\);
- dimension comparisons for the image and kernel of these maps;
- a generalized-eigenvector argument for the resulting pair of maps.
In particular, the condition can be written as
\[
\overline A_{\mathcal Z}x=\lambda\,\overline I_{\mathcal Z}x,
\qquad \overline I_{\mathcal Z}x\ne0,
\]

where \(\overline I_{\mathcal Z}:V\to X/\mathcal Z\) is the quotient of the inclusion map and \(\overline A_{\mathcal Z}:V\to X/\mathcal Z\) is the quotient of \(A|_V\). This is a generalized-eigenvector problem for a pair of maps, rather than an arbitrary polynomial incidence condition.

The advantage is that it retains \(x\notin\mathcal Z\) automatically through \(\overline I_{\mathcal Z}x\ne0\).

Verdict on C: put C1 aside. Keep C2 as a targeted attempt, particularly if the structured search in B produces a repeatable family.

4. Proposal D: D1 before D2, but settle the field before reducing
I agree with your concern that the constraints may leave too little freedom for a quadratic-feasibility reduction. Nevertheless, D1 is the more natural first attempt because your formulation already contains bilinear products.

There is an important issue that I would resolve before either reduction.
Is the problem genuinely over \(\mathbb C\), or are you willing to restrict to \(\mathbb R\)?
Your setting explicitly uses
\[
A,C,L_0,\mathcal L\in\mathbb C^{\cdots}.
\]

For rational input matrices, your polynomial-size existential-real encoding is valid: split each complex variable into real and imaginary parts, and express the complex polynomial constraints as real polynomial equations.

But membership in \(\exists\mathbb R\) is not the same as a natural \(\exists\mathbb R\)-hardness route.

A reduction from real quadratic feasibility must preserve the distinction between real and complex solutions. A real polynomial system can have complex solutions even when it has no real solution. Therefore, one cannot simply take an arbitrary real quadratic system, substitute its variables into complex matrix entries, and conclude that the reduction works.

This is not a minor technicality. The source problem and target problem must use compatible fields.

I recommend deciding between two explicit variants:
- Complex synthesis problem: matrices and augmentations may be complex. Investigate reductions from complex algebraic feasibility problems, or construct a real-hardness reduction that rigorously handles the real-versus-complex issue.
- Real synthesis problem: input matrices and admissible augmentations are required to be real. Then real quadratic feasibility is a much more natural source for \(\exists\mathbb R\)-hardness.
Your existing \(\exists\mathbb R\) upper bound can be retained for the complex problem, but the hardness proof needs to respect this distinction.
D1: how I would test it
Start with a very small multiplication-gate experiment. Do not begin with a complete reduction.

You have
\[
E_{j+1}=E_j\Lambda,\qquad M=\mathcal LV_0=AB.
\]

These are bilinear constraints, but their products are highly structured. The question is whether the structure can encode arbitrary products \(x_ix_j\), or whether the equations merely describe matrix powers and factorizations with too much invariance.

I would test the following:
1. Can you make selected entries of \(\Lambda\) represent independent source variables?
2. Can selected entries of \(E_j\) represent products of those variables?
3. Can the observer equation and the rank constraints force the intended entries to be equal to the required products?
4. Can every unintended degree of freedom be removed without destroying the source solution?
The key experiment is not “can I write a multiplication gate?” It is:
Can I construct a small observer instance in which feasibility is equivalent to a prescribed system of two or three quadratic equations, with no spurious solutions?

If that cannot be done even for a small gate system, a full reduction is unlikely to be straightforward.
D2: a genuine hardness result exists, but the interface is not yet right
There is a very relevant recent result. Liu's September 2026 preprint proves that static output-feedback stabilization with rational plant data is \(\exists\mathbb R\)-complete, even for controllable and observable plants with two inputs. It also gives a polynomial-time result when the effective gain dimension is fixed. 

arXiv+1

This makes static output feedback a serious candidate source problem, not merely a vague analogy.

However, the target conditions are different:
- Static output-feedback stabilization asks for a real gain making a closed-loop matrix Hurwitz.
- Your spectral condition asks for an observability/rank property, equivalently the absence of a finite elementary divisor.
Hurwitz stability is a real semialgebraic condition involving the location of eigenvalues. Your fixed-candidate observability condition is an algebraic rank condition. A direct identification of the two would be unjustified.

A reduction would need a gadget translating the Hurwitz inequalities into your rank/observability constraints. I do not currently see a simple one.

Verdict on D: D1 first, after fixing the real/complex model. Keep D2 as a candidate source to revisit if you find a way to encode spectral-location inequalities. Do not attempt a direct identification between stability and observability.

5. Proposal E: retain it, but the proposed implication is false in its current form
The proposed statement
\[
\text{Type III}\Longrightarrow \varepsilon=0
\]

is already contradicted by the report's own examples.

The \(n=7\) and \(n=8\) cases have individual spectral failures even though proportionality fails on \(V\), so \(\varepsilon\ge1\). These are Type III candidates, albeit isolated ones. Therefore, no theorem asserting that every Type III candidate forces \(\varepsilon=0\) can be true. 
12_research_direction.md

A more plausible statement would be:
If every admissible augmentation at a fixed order fails spectrally, then the proportionality locus must satisfy a stronger dimension condition.

But even this needs proof, and the current incidence argument has exactly the open-image and boundary problems discussed above.
A better route to a positive class
I would formulate a positive-class problem independently of \(\varepsilon\):

Find a verifiable structural condition on \((A,C,L_0)\) under which
\[
\text{every admissible }\mathcal L
\text{ with }h<q+r_1
\quad\Longrightarrow\quad (5b).
\]

The condition should be stated in terms of computable matrices or invariant subspaces, not in terms of “there is no Type III candidate,” which is just the property you want to establish.

One possible route is to study the induced maps
\[
\overline I_{\mathcal Z}:V\to X/\mathcal Z,
\qquad
\overline A_{\mathcal Z}:V\to X/\mathcal Z.
\]

A sufficient condition would ensure that the pencil
\[
\lambda\overline I_{\mathcal Z}-\overline A_{\mathcal Z}
\]

has no nontrivial generalized eigenvector for every admissible \(\mathcal Z\). The challenge is to express that uniformly over \(\mathcal Z\) through simple rank or invariant-subspace conditions.

This seems more promising than trying to prove that \(\varepsilon\) and a dimension equality characterize all spectral failures.

Verdict on E: retain as a secondary direction. Do not pursue the proposed implication as stated.
6. QF: a stronger answer about \(\varepsilon=0\)
The matrix characterization above answers QF directly. In particular, when
\[
\operatorname{rank}(L_0|_V)\ge2,
\]

the condition \(\varepsilon=0\) means
\[
L_0A|_V=\alpha L_0|_V.
\]

This says that, on \(V\), the two output maps differ by a single scalar factor.

When \(\operatorname{rank}(L_0|_V)=1\), the condition is weaker: only the image inclusion
\[
L_0A(V)\subseteq L_0(V)
\]

is required. This is exactly the regime of your \(n=6\) example.

So \(\varepsilon=0\) has a clean matrix-theoretic characterization. It is not necessary to compute a Gröbner basis to test this special case.

I would add a small exact-arithmetic test for this proposition to your Lean and Python verification suite. It is a useful bridge between the geometric invariant and the original matrices.

7. QG: the three directions I would drop or pause
If I had to remove three directions from the immediate research programme, I would choose:
Direction	Decision	Reason
Incidence/covering line (C1)	Pause	Boundary and properness issues; no reliable covering theorem yet
Direct static-output-feedback reduction (D2)	Defer	The stability condition does not directly match your observability condition
Further encoding refinements	Pause	You already have a polynomial-size upper-bound encoding; more optimization does not settle hardness

I would retain:
- A: canonical Grassmannian formulation;
- B: structured search for more whole-family examples;
- D1: quadratic-feasibility reduction experiment;
- E: positive polynomial-time class.
I would not drop the search for more counterexamples. In fact, I would make it much more targeted using the characterization of \(\varepsilon=0\) above.

8. My proposed next research sequence
Here is the order I would actually execute.
Step 1 — Structural characterization
First

Prove and machine-check the three-case characterization of \(\varepsilon=0\), according to \(\operatorname{rank}(L_0|_V)\).

Deliverable: a theorem and a matrix-only test.

Step 2 — Structured whole-family search

Generate instances satisfying the rank-one condition
\[
\operatorname{im}(L_0A|_V)\subseteq\operatorname{im}(L_0|_V)
\]

and the higher-rank condition
\[
L_0A|_V=\alpha L_0|_V.
\]

Vary Jordan structures and the relative positions of \(C,L_0\).

Deliverable: either a second genuinely different whole-family counterexample, or evidence that the known example relies on a special additional structure.

Step 3 — Small-gadget hardness experiment

Fix whether the target problem is over \(\mathbb R\) or \(\mathbb C\). Then try to encode a two- or three-equation quadratic system using the observability constraints.

Deliverable: a small exact equivalence, or a rigorous explanation of which observer constraints prevent the gadget.

Step 4 — Per-subspace generalized-eigenvector formulation

Develop the quotient maps
\[
\overline I_{\mathcal Z},\quad\overline A_{\mathcal Z}
\]

and search for uniform sufficient conditions excluding generalized eigenvectors.

Deliverable: a candidate tractable subclass, or a counterexample to the proposed sufficient condition.

I would not set a deadline for a full \(\exists\mathbb R\)-hardness proof yet. First establish whether the design variables have enough freedom to encode even a small system of quadratic equations.
9. One additional direction I would add
There is a potentially useful bridge between B and E: classify the spectral failure using the quotient pencil before trying to classify the whole incidence image.

For each admissible \(\mathcal Z\), define
\[
J_{\mathcal Z}:V\longrightarrow X/\mathcal Z,
\qquad
T_{\mathcal Z}:V\longrightarrow X/\mathcal Z,
\]

by
\[
J_{\mathcal Z}x=x+\mathcal Z,\qquad
T_{\mathcal Z}x=Ax+\mathcal Z.
\]

Then failure is exactly
\[
\exists x\in V:
\quad J_{\mathcal Z}x\ne0,\qquad
T_{\mathcal Z}x=\lambda J_{\mathcal Z}x.
\]

This formulation makes the role of the source condition transparent. It is a generalized eigenvector of the pair \((T_{\mathcal Z},J_{\mathcal Z})\), with nonzero \(J_{\mathcal Z}x\).

The benefit is that you can study the rank and invariant structure of a pair of linear maps rather than a rational map from a proportionality variety. This may yield a classification of the cases in which failure is impossible for every \(\mathcal Z\).

I would explore this before returning to projective covering arguments.

Final recommendation
The immediate next target should be:
\[
\boxed{\text{Characterize }\varepsilon=0
\quad+\quad
\text{find a second structured whole-family example}.}
\]

That is the best combination of a provable structural result and an experiment likely to reveal the real mechanism behind the counterexample.

In parallel, settle the real-versus-complex formulation and attempt one small D1 gadget. If the gadget works, the project can move decisively toward hardness. If it fails for a structural reason, that failure may point directly toward the positive tractable class.

I would not spend the next round on a general incidence-covering theorem or on further polishing the \(\exists\mathbb R\) encoding. Those are not currently the bottlenecks.