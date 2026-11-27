# **Academic assessment of Report 106: proposed structure for a standalone hyperplane-layer paper**

## **1. Overall recommendation**

**The proposed structure is fundamentally sound, and I recommend organizing the paper around the geometry of the hyperplane layer first, followed by the exact decision procedure and its complexity.** The structure-first approach is better suited to the actual mathematical contribution than an algorithm-first presentation.

The paper should not, however, present all seven items in the theorem package as equally central. I would organize its contribution around three main results:

1. **Structural characterization:** admissible directions are compression eigenvectors, with the prescribed-row constraints incorporated.
2. **Geometric parameterization and exact decision:** the admissible designs form relative Grassmann bundles, and spectral feasibility can be decided by exact chartwise computation.
3. **A fixed-parameter complexity result and a limitation example:** fixed-\\(p\\) polynomial bit complexity under geometric simplicity, together with a repeated-eigenspace counterexample showing why the simplicity hypothesis cannot simply be omitted.

The Paper II duality should be presented as a useful structural proposition that connects the new parameterization to the earlier compressed-subspace formulation.

The most important concern is not the section order. It is the **logical scope of the claims in Part I**. In particular, the paper must distinguish carefully between:

- an exact decision procedure for the whole hyperplane layer;
- a polynomial-time decision procedure on the geometrically simple subclass;
- a counterexample showing that a particular shortcut fails in the repeated-eigenspace case.

These are three different claims. The current outline sometimes places them close enough together that a reader might mistake one for another.

My assessment is based on the proposed structure and the reliability table in Report 106. The outline states that the underlying results have been proved and that the counterexample has exact certificates, but the structure document itself does not contain those proofs or certificates. I therefore assess the proposed presentation and the logical requirements for the claims, rather than independently verifying those calculations.&#x20;

106_paper_structure.md



## **2. Q1: Is the balance right? Structure first or algorithm first?**

**Recommendation: structure first.**

The paper's most distinctive contribution is the description of the admissible observer designs in the hyperplane layer. The algorithm is important, but its input space and its finite chart cover become much easier to understand after the geometry has been established.

An algorithm-first presentation would force the reader to understand several technical objects before knowing why they are the right objects:

- the compression eigenvector;
- the eigen/non-eigen direction strata;
- the prescribed-row-compatible space \\(E\_\mu^0\\);
- the relative Grassmann fibres;
- the full-rank property of the leading coefficient \\(H\\).

If these are introduced only as ingredients of an algorithm, the reader may regard them as technical devices rather than as the structural theorem of the paper.

### **2.1 The recommended narrative**

The logical progression should be:

\\[ \boxed{ \text{Observer problem} \longrightarrow \text{hyperplane structure} \longrightarrow \text{parameter space} \longrightarrow \text{spectral decision} \longrightarrow \text{complexity}. } \\]

More specifically:

- Section 1 explains why the hyperplane layer is the first nontrivial layer and states the contributions.
- Section 2 establishes the compressed setting and the assumptions.
- Section 3 proves the direction theorem and parameterization theorem.
- Section 4 explains how to decide spectral feasibility over that parameter space.
- Section 5 establishes the fixed-\\(p\\) complexity result.
- Section 6 explains the obstruction created by repeated eigenspaces.
- Section 7 relates the results to Papers I and II.

This order gives the reader the mathematical object first, then the algorithm for deciding its feasibility.

### **2.2 One adjustment: introduce the algorithmic question earlier**

Although the main algorithm should come after the geometry, the Introduction should state the decision problem before stating the structural theorem.

I suggest introducing the question in the following form:

> Given the system data and a prescribed observer block, determine whether there exists a completion of the prescribed block to an observer of the specified order satisfying the functional-observer conditions in the hyperplane layer.

Then explain that the paper answers this question by first characterizing the admissible design space and then testing its spectral feasibility.

This makes the geometry visibly serve the original decision problem.

### **2.3 A more precise contribution hierarchy**

I would not list seven contributions in the Introduction. Seven items are too many for a concise contribution statement, and some are supporting results rather than independent contributions.

Instead, use four contributions:

1. **Structural characterization:** the compression-eigenvector characterization of admissible directions, including prescribed rows.
2. **Geometric parameterization:** the relative Grassmann-bundle description and its dimension/nonemptiness formulas.
3. **Exact decision and complexity:** the chartwise gcd criterion and the fixed-\\(p\\) polynomial-time result under geometric simplicity.
4. **Limitations and connections:** the repeated-eigenspace counterexample and the duality with the compressed row-space formulation.

This preserves every result in Part I while giving the reader a clearer sense of what is central.

## **3. Q2: Should the counterexample open the paper?**

**Recommendation: use it as a motivating observation in the Introduction, but retain the complete counterexample as a later technical section.**

The counterexample is the sharpest illustration of why the problem is not solved by selecting one arbitrary eigenvector for each distinct eigenvalue. It deserves a prominent role. But opening the paper with a long negative example would risk giving the paper the wrong identity.

The central contribution is not merely that a tempting reduction fails. It is that the hyperplane layer admits a precise structural and algorithmic treatment.

### **3.1 How to use the counterexample in the Introduction**

I recommend a short motivating paragraph after introducing the compression matrix \\(M\\).

The paragraph should make three points:

- A repeated eigenvalue can have a multidimensional eigenspace.
- Feasibility need not be constant over the projective directions in that eigenspace.
- Consequently, testing one arbitrarily selected eigenvector for each distinct eigenvalue is not a valid general reduction.

The paragraph should not include the complete six-direction table, all maximal minors, or the Bézout certificates. Those belong in Section 6 and Appendix A.

A possible formulation is:

> A natural simplification would be to select one eigenvector for each distinct real eigenvalue of the compression. This is not valid in general: within a repeated eigenspace, the spectral feasibility of the induced observer design can depend on the projective direction. We give an exact rational example demonstrating this phenomenon. This motivates our treatment of the full projective eigenspace rather than a choice of one representative eigenvector.

This gives the reader a reason to care about the complete direction parameterization.

### **3.2 Why the complete example should remain a separate section**

The example has two jobs:

1. It motivates the need to retain the entire repeated eigenspace.
2. It establishes a precise limitation on a proposed reduction.

These jobs require different levels of detail. The Introduction needs only the first. The second requires the full input matrices, the direction table, and exact certificates.

Therefore, Section 6 should be a self-contained mathematical section, not merely a collection of numerical experiments.

Its conclusion should be stated carefully:

\\[ \boxed{ \text{Feasibility is not necessarily constant on a repeated compression eigenspace.} } \\]

It should not claim that all repeated-eigenspace cases are computationally intractable. The example disproves a particular reduction, not the possibility of a general algorithm.

## **4. Q3: Is a fixed-**\\(p\\)**&#x20;complexity theorem under geometric simplicity an acceptable headline result?**

**Yes. It is an acceptable and mathematically meaningful headline result, provided the hypothesis is stated prominently and the theorem is presented as a promise-class result rather than as a complexity classification of the unrestricted problem.**

A conditional polynomial-time theorem is not inherently weaker scholarship. In this case, the geometric simplicity condition has a direct structural meaning: every real eigenvalue of the compression has a one-dimensional eigenspace. Thus each such eigenvalue contributes at most one projective direction, and the remaining parameterization is confined to a Grassmann fibre whose dimension is bounded in terms of \\(p\\).

The hypothesis is therefore not an arbitrary technical condition introduced solely to make the complexity proof work. It controls the dimension of the direction parameter space.

### **4.1 State the hypothesis precisely**

I recommend using the term **geometric simplicity of the real spectrum**, and defining it explicitly:

\\[ \boxed{ \dim\ker(M-\mu I)=1 \quad\text{for every real eigenvalue }\mu\text{ of }M. } \\]

Do not use simply “simple spectrum.” In standard terminology, a simple eigenvalue often means algebraic multiplicity one. Your condition is weaker: an eigenvalue may have algebraic multiplicity greater than one but still have a one-dimensional eigenspace.

This distinction matters because the algorithm enumerates projective eigendirections. Its relevant condition is geometric multiplicity, not algebraic multiplicity.

The prescribed-row restriction should also be included in the statement. Some eigendirections may be eliminated by

\\[ E\_\mu^0 = E\_\mu\cap\ker(L_0N)\cap\ker(L_0AN). \\]

Thus the actual algorithm enumerates the admissible direction(s) in \\(E\_\mu^0\\), not all eigenvectors of \\(M\\).

### **4.2 Do not let the counterexample carry more weight than it proves**

The counterexample establishes that one cannot simply discard all but one direction in a repeated eigenspace. It does **not** prove that geometric simplicity is necessary for polynomial-time solvability, nor that the repeated-eigenspace problem is hard.

The correct relationship is:

- Geometric simplicity yields a bounded-dimensional family of row-space parameters for fixed \\(p\\).
- Repeated eigenspaces introduce additional direction parameters.
- The example proves that those parameters cannot generally be ignored.
- The complexity of the general repeated-eigenspace case remains open in the proposed paper.

I would explicitly say this in Section 5, perhaps in a short paragraph entitled “Scope of the complexity theorem.”

### **4.3 Separate exact decidability from polynomial-time decidability**

This is the most important editorial correction to Part I.

Item 4 currently says:

> “Two-way on rational data; the direction screen is a free negative certificate.”

Item 5 then says that polynomial-time complexity is established only under geometric simplicity.

These statements can coexist, but the paper must distinguish their meanings.

I recommend a two-level formulation:

**Exact decision theorem.** The hyperplane-layer problem admits a finite exact algebraic decision procedure. The procedure uses a finite cover of the parameter space and exact polynomial computations. This establishes decidability, not necessarily polynomial-time complexity.

**Fixed-**\\(p\\)**&#x20;complexity theorem.** Under geometric simplicity of the real spectrum, the exact decision procedure runs in deterministic polynomial bit complexity for fixed \\(p\\).

If the first theorem is genuinely implemented for repeated eigenspaces, it should be stated as an exact decision result with its actual complexity left unrestricted. If it is not implemented for all repeated-eigenspace direction charts, the wording “two-way on rational data” must be narrowed.

### **4.4 Clarify the finite-cover argument**

The statement that a finite cover by irreducible pieces suffices without decomposing into irreducible components is attractive, but it needs careful wording.

The essential argument is this:

- Each chart or parameter-space piece is irreducible.
- The maximal minors define a polynomial family over that piece.
- The function-field gcd tests whether the generic point of that piece is spectrally good.
- The full-rank leading-coefficient lemma ensures that a positive-degree generic gcd makes every point of that piece bad.
- If the generic gcd is \\(1\\), the good locus is a nonempty open subset of that piece, so the piece contains a feasible point.

Thus the existential decision can be made by checking the finite family of pieces: feasibility holds if and only if at least one piece has generic gcd \\(1\\).

The paper should not say that the finite cover makes decomposition unnecessary without explaining why the pieces themselves are irreducible and why the test is valid on each piece. Also, overlapping pieces are harmless for an existential decision; they need not be a disjoint decomposition.

A further distinction is important: **the finite-cover result does not automatically establish polynomial complexity.** A finite number of charts may still be enormous, and the direction space may have dimension growing with \\(n\\). The fixed-\\(p\\) theorem needs its separate bounds on the number of variables, charts, minors, and arithmetic operations.

### **4.5 Suggested headline theorem**

I would state the main complexity result in a box or as a clearly numbered theorem:

> **Theorem (fixed-**\\(p\\)**&#x20;complexity under geometric simplicity).**\
> Fix \\(p\\). For rational input data satisfying the standing assumptions, suppose every real eigenvalue of the compression \\(M\\) has a one-dimensional eigenspace. Then feasibility in the hyperplane layer can be decided by a deterministic algorithm in polynomial bit complexity. The polynomial degree may depend on \\(p\\), through the bounded number of parameters in the Grassmann charts.

This is strong enough to be a headline result. The abstract should include the condition explicitly, not relegate it to the final paragraph.

I would also state separately that the theorem does not cover arbitrary repeated eigenspaces.

## **5. Q4: Should the Paper II duality be a theorem or a remark?**

**Recommendation: state it as a numbered proposition, not a major theorem and not merely a remark.**

It is a clean mathematical statement with a genuine conceptual function: it identifies the projective direction in the ambient parameterization with the annihilator of the common projection in the compressed row-space formulation.

Let

\\[ W=\operatorname{row}(V[N\ \ AN]) \\]

and suppose

\\[ \pi_1(W)=\pi_2(W)=U, \qquad \dim U=k-1. \\]

For the hyperplane direction \\(v=Na\\), the structural conditions imply

\\[ W\subseteq a^\circ\times a^\circ. \\]

Therefore

\\[ U\subseteq a^\circ. \\]

Since both have dimension \\(k-1\\),

\\[ U=a^\circ. \\]

Thus

\\[ \boxed{ [a]=\mathbb P(\operatorname{Ann}(U)). } \\]

This is more than a contextual observation. It is a precise bridge between two parameterizations of the same hyperplane-layer structure.

### **5.1 Why a proposition is the right level**

A major theorem would overemphasize a relatively short result. A remark would understate its role in connecting the two papers.

A proposition is appropriate because:

- it has a short, self-contained proof;
- it gives a useful dictionary between two mathematical representations;
- it clarifies what information is retained and what information is lost under compression;
- it helps explain why the current paper is a continuation of the earlier work rather than an unrelated algorithmic treatment.

I would place it at the end of Section 3, immediately after the parameterization theorem, or in Section 7 if the authors prefer to keep all comparisons with earlier papers together.

My preference is **at the end of Section 3**. The duality is easier to appreciate immediately after the reader has seen the ambient parameterization.

### **5.2 State the limitation alongside the proposition**

The proposition identifies the direction from \\(W\\), but it does not imply that every compressed \\(W\\) has an admissible ambient lift satisfying the prescribed-row constraints.

This limitation should be stated explicitly. The map

\\[ V\longmapsto W \\]

can have a nontrivial kernel, so the compressed description forgets ambient row-space information. In particular, it does not automatically retain the information needed to enforce \\(V_0\subseteq V\\).

I would include a short remark after the proposition:

> The correspondence determines the projective hyperplane direction, but it is not in general a bijection between ambient row spaces and compressed subspaces. The existence of an ambient lift satisfying the prescribed-row and dimension constraints remains a separate condition.

This avoids overstating the duality.

## **6. Q5: What should be removed, shortened, or retained?**

**I would remove no central mathematical result. I would shorten some of the exposition and move technical material to the appendix.**

In particular, I agree with retaining both the finite-cover refinement and the relative Grassmann-bundle formulation. Neither is decorative technicality.

### **6.1 Keep the relative Grassmann-bundle formulation in the main text**

This is essential.

A product expression such as

\\[ \mathbb P(E\_\mu^0)\times\operatorname{Gr}(a,b) \\]

would suggest that the quotient spaces defining the fibres are globally identified with one fixed vector space. But the quotient

\\[ \mathcal Q_v/\overline V\_{0,v} \\]

varies with the direction \\(v\\).

The relative Grassmann bundle is the correct global description. It explains:

- why the fibre dimensions are constant on each eigen/non-eigen stratum;
- why the total parameter space has the stated dimension;
- why local Grassmann charts are appropriate for the decision procedure;
- why the eigen and non-eigen strata must be treated separately.

This is central to the structural theorem and should remain in Section 3, not be hidden in a remark or appendix.

The proof can be concise. Define the quotient vector bundle, identify its relative Grassmannian, and derive the dimension formula. There is no need to give a lengthy general introduction to Grassmann bundles.

### **6.2 Keep the finite-cover refinement in the main text, but make it short**

The finite-cover argument is also important because it connects the geometry to the decision procedure.

Without it, the generic gcd criterion might appear to apply only after a full irreducible-component decomposition. The finite-cover formulation explains why a convenient finite family of irreducible charts is sufficient.

I would retain the argument in Section 4.1, but move any general algebraic-geometric background to a short preliminary lemma or appendix.

The main text needs only:

1. the closedness statement;
2. the generic criterion on an irreducible piece;
3. the finite-cover consequence;
4. an explanation of why the chosen parameter-space charts satisfy the hypotheses.

### **6.3 Move detailed arithmetic bounds to the appendix**

Section 5 should state the complexity theorem and give the essential parameter and degree bounds. It should not become a long catalogue of technical facts about algebraic-number heights and subresultant coefficient growth.

I suggest:

- **Main text:** state the compression height lemma, the bound on the number of chart variables, the bound on the number of maximal minors, and the resulting complexity theorem.
- **Appendix A:** give the detailed height estimates and exact arithmetic constructions.
- **Appendix B, if needed:** give the precise subresultant or multi-polynomial gcd complexity argument.

The reader should be able to understand why the exponent depends on \\(p\\) without reading the appendix, while a complexity-theory reader should be able to verify the bit bounds there.

### **6.4 Keep the exact certificates in the appendix**

The complete counterexample should be introduced and explained in Section 6, but long Bézout identities and common-factor divisibility identities should go into Appendix A.

The main section should display:

- the complete input matrices or a compact table of them;
- the compression and repeated eigenspace;
- the direction classification;
- the six-direction feasibility table;
- a summary of the certificates;
- the exact conclusion.

The appendix should provide enough information for independent reproduction.

### **6.5 Avoid a redundant Section 7**

The proposed Section 7 is useful, but it should not repeat all the preliminaries from Section 2.

I would make it a concise section entitled **“Relation to the compressed formulations”**. It should have three parts:

- what is inherited from Paper I;
- what is inherited from Paper II;
- what is new in the present paper.

A comparison table is appropriate here. It should distinguish inherited results from new contributions rather than repeat technical definitions.

## **7. Two technical issues the outline should make more visible**

There are two points I would add to the proposed structure because they are logically important, even though they do not require new major sections.

### **7.1 The closedness argument and the full-rank leading-coefficient lemma should be unified**

Part I lists closedness and the generic criterion as one result, while Section 4 separates them into different subsections. I recommend making their logical connection explicit.

Let

\\[ P(X,\lambda)=\lambda H(X)-H_A(X), \\]

and let \\(m_I(X,\lambda)\\) denote its maximal minors of order \\(\omega\\). The full-rank property

\\[ \operatorname{rank}H(X)=\omega \\]

for every admissible parameter point implies that at least one maximal minor has a nonzero coefficient of \\(\lambda^\omega\\) at every such point.

Now homogenize each minor in \\(\lambda\\), using a projective coordinate \\([u:v]\\) on \\(\mathbb P^1\\). A common root at infinity, \\([u:v]=[1:0]\\), would require all leading coefficients to vanish. But the full-rank property excludes that possibility.

Consequently, the common-root incidence set can be considered inside

\\[ \mathcal X\times\mathbb P^1, \\]

where \\(\mathcal X\\) is the parameter chart. Projection onto \\(\mathcal X\\) is then closed because the second factor is projective. This yields the closedness of the bad locus.

This is a particularly clean argument because the same structural fact—the full row rank of \\(H\\)—does two jobs:

1. It prevents common roots from escaping to infinity, giving closedness.
2. It prevents a positive-degree generic common factor from specializing to a constant, giving the whole-chart badness certificate.

I would make this the conceptual centerpiece of Section 4.2. It makes the exact decision procedure feel like a consequence of the hyperplane geometry, rather than an unrelated symbolic-algebra trick.

### **7.2 State the real-point density condition in the generic criterion**

There is a subtle logical distinction between a generic algebraic point and a feasible real observer.

If a polynomial family has gcd \\(1\\) over the function field, its good locus is a nonempty Zariski-open subset of the parameter space. To conclude that this open set contains a real point, one needs the real points of the relevant parameter piece to be Zariski dense.

For the parameter spaces in this paper, that should be manageable: the direction spaces are real projective spaces or open subsets thereof, and the fibres are real Grassmannians. Their standard affine charts have real points that are Zariski dense. But the paper should state this rather than silently equating a generic algebraic point with a realizable real design.

I would add one sentence to the generic criterion:

> Since each parameter chart is a rational real chart with Zariski-dense real points, every nonempty Zariski-open good locus on that chart contains a real admissible design.

This also explains why the finite-cover argument works for the actual real feasibility problem.

## **8. My recommended revised section structure**

I would make a small but meaningful adjustment to Part II. In particular, I would put the duality proposition at the end of the geometry section, and make the closedness/leading-coefficient connection explicit in the decision section.

## **Recommended paper architecture**

1. **1. Introduction**
   - Functional-observer feasibility and the hyperplane layer
   - The repeated-eigenspace motivation
   - Four main contributions and precise scope
2. **2. Preliminaries and compressed formulation**
   - Notation from Papers I and II
   - Hyperplane-layer assumptions and row-rank conventions
   - Standing assumption \\(\operatorname{rank}L_0=r_0\\)
   - The compressed pencil and feasibility criterion
3. **3. Geometry and parameterization of the hyperplane layer**
   - Structural conditions on the row space
   - Compression-eigenvector direction theorem
   - Prescribed-row-compatible eigenspaces \\(E\_\mu^0\\)
   - Eigen/non-eigen stratification
   - Relative Grassmann-bundle parameterization and dimensions
   - Paper II direction-duality proposition
4. **4. Exact algebraic decision procedure**
   - Closedness of the bad locus
   - Generic gcd criterion on irreducible real charts
   - Finite-cover principle
   - Grassmann charts and maximal minors
   - Full-rank leading-coefficient lemma
   - Positive and negative certificates
5. **5. Fixed-**\\(p\\)**&#x20;bit complexity**
   - Compression and algebraic-number height bounds
   - Chart-variable and minor-count bounds
   - Fraction-free subresultant computation
   - Polynomial-time theorem under geometric simplicity
   - Scope and limitations for repeated eigenspaces
6. **6. Repeated-eigenspace counterexample**
   - Complete rational instance
   - Direction classification and six-direction table
   - Exact good-direction and bad-direction certificates
   - Consequence for representative-eigenvector reductions
7. **7. Relation to the earlier compressed formulations**
   - Inherited results from Paper I
   - Inherited results from Paper II
   - New structural and algorithmic contributions
8. **Appendices**
   - A. Complete instance data and exact certificates
   - B. Algebraic-number height and arithmetic bounds
   - C. Detailed subresultant and gcd complexity estimates, if needed

The difference from the original outline is not large. It mainly clarifies the progression from geometry to algebraic decision, and from algebraic decision to complexity.

## **9. A suggested abstract-level framing**

I would frame the paper as a structural and algorithmic study, not primarily as a complexity paper or a counterexample paper.

A possible abstract-level description is:

> This paper studies functional-observer feasibility in the hyperplane layer of the compressed problem. We first characterize the admissible kernel directions as real eigenvectors of a compression of the state matrix, and incorporate prescribed observer rows through a further linear restriction on the eigenspaces. We then parameterize all admissible row spaces by relative Grassmann bundles, obtaining explicit dimension and nonemptiness criteria. Based on this parameterization, we develop an exact algebraic decision procedure using Grassmann charts and common-root tests for the maximal minors of the compressed pencil. We establish polynomial bit complexity for fixed output dimension under geometric simplicity of the real compression spectrum. Finally, an exact repeated-eigenspace example shows that feasibility can vary with the projective direction, ruling out a reduction based on selecting one arbitrary eigenvector per distinct eigenvalue. A duality proposition relates the resulting direction parameterization to the compressed row-space description developed in earlier work.

This framing has several advantages:

- It identifies the mathematical object and the precise layer.
- It states the prescribed-row contribution.
- It describes the algorithm without overstating its complexity.
- It uses the counterexample to explain the limitation of the complexity hypothesis.
- It places the duality in the role of a connection, not a competing main result.

## **10. Final answers to the five questions**

| Question                                | Recommendation                                                                                                                                                                      |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Q1. Structure or algorithm first?**   | Structure first. The parameterization is the principal new mathematical contribution; the algorithm should follow from it.                                                          |
| **Q2. Counterexample placement?**       | Briefly motivate the paper with it in the Introduction; reserve the complete construction and certificates for Section 6.                                                           |
| **Q3. Conditional complexity theorem?** | Yes. It is a legitimate headline result if geometric simplicity is defined precisely and stated in the abstract and theorem.                                                        |
| **Q4. Duality as theorem or remark?**   | A numbered proposition, preferably at the end of Section 3.                                                                                                                         |
| **Q5. Remove anything?**                | Remove no central result. Keep relative Grassmann bundles and the finite-cover refinement in the main text; move lengthy arithmetic estimates and exact certificates to appendices. |

## **11. Final assessment and priority list**

Recommended: proceed with this structure

I consider Report 106 a good and coherent plan for a standalone paper. It has a clear mathematical identity: **the geometry and exact decidability of functional-observer feasibility in the hyperplane layer**.

The main risk is overclaiming, not overloading the paper with technical material. I would resolve the following points before drafting the full manuscript:

1. **Fix the theorem hierarchy.** Separate the general exact decision procedure from the fixed-\\(p\\) polynomial-time theorem.
2. **Make the geometric-simplicity hypothesis exact.** Use one-dimensional real eigenspaces, not algebraic simplicity.
3. **Connect closedness and generic gcd computation.** Explain that the full-rank leading coefficient prevents roots from escaping to infinity and also supports the whole-chart certificate.
4. **State the real-point density argument.** This is necessary to turn generic algebraic feasibility into existence of a real observer.
5. **Make the counterexample independently reproducible.** The complete matrices and exact certificates should be included, with detailed calculations in an appendix.
6. **Keep the ambient/compressed distinction explicit.** The duality identifies the direction, but does not automatically give a bijection between ambient row spaces and compressed subspaces.

One final strategic suggestion: do not title the paper around the fixed-\\(p\\) algorithm alone. The geometry is what makes the algorithm possible and what distinguishes this work from a straightforward application of the earlier compressed-pencil machinery.

A suitable title would be:

**Functional-Observer Feasibility in the Hyperplane Layer: Structural Parameterization, Exact Decision, and Fixed-Parameter Complexity**

This title accurately reflects the three principal contributions without suggesting that the unrestricted minimum-order or feasibility problem has been completely classified.

**My conclusion:** the proposed paper structure is ready to guide a full manuscript. I would preserve its structure-first orientation and concentrate the remaining effort on making the exact-decision and complexity statements maximally precise.