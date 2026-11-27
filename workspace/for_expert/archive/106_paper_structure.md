# Report 106: proposed structure for a standalone paper on the hyperplane layer

This is not a results report. It is a proposal for how to package the hyperplane-layer material as a
standalone paper, followed by five questions about the framing. Everything is self-contained; the two
papers are cited only as background.

---

## Part I. What the paper would claim

**Scope.** Functional-observer feasibility for the *hyperplane layer* $c=k-\omega=1$ of the compressed
problem: the structure of the admissible designs, an exact decision procedure, its complexity, and a
counterexample showing where a tempting reduction fails.

**Theorem package** (each item is proved in the current development, except where noted):

1. **Closedness and the generic criterion.** The bad locus is closed; on an irreducible parameter
   piece, feasibility is equivalent to the maximal minors having no common root over the function
   field. A finite cover by irreducible pieces suffices (no decomposition into components is needed).
2. **Direction reduction.** In the hyperplane layer the admissible kernel directions are exactly the
   eigenvectors of the compression $M=\pi_{K_0}A|_{K_0}$; with prescribed rows, the directions are
   further restricted to $E_\mu^0=E_\mu\cap\ker(L_0N)\cap\ker(L_0AN)$.
3. **Complete parameterization.** The layer is a finite disjoint union of *relative* Grassmann
   bundles over projective eigenspaces, with explicit dimensions
   $h_\mu^0-1+(s-\delta)(\rho-s)$ and $d_\mu^0-1+(s-\delta)(\rho-1-s)$, where $\delta$ measures the
   prescribed rows modulo $K_0$.
4. **Decision procedure.** Chartwise exact computation: symbolic Grassmann chart, maximal minors,
   gcd over the function field; the full-rank leading-coefficient lemma converts a positive-degree
   gcd into a certificate that the whole chart is bad. Two-way on rational data; the direction screen
   is a free negative certificate.
5. **Complexity.** Fixing $p$, on geometrically simple spectra, the decision is polynomial in the
   input bit size; the exponent depends on $p^2$ (the number of chart parameters).
6. **A counterexample.** In a repeated eigenspace, feasibility varies with the direction; explicit
   data and exact certificates show one direction feasible and the others entirely bad. Hence
   "one eigenvector per eigenvalue" is not a valid reduction.
7. **A duality.** The projective direction is the annihilator of the common projection of Paper II's
   compressed row space: $[a]=\mathbb P(\operatorname{Ann}(U))$, $U=a^\circ$.

**What the paper does not claim.** Nothing about layers $c\ge2$; nothing about the unrestricted
complexity of the original decision problem; the repeated-eigenspace case is treated only by the
counterexample, not by a classification.

---

## Part II. Proposed section structure

**1. Introduction.** The observer conditions; the compressed formulation; why the hyperplane layer is
the first nontrivial case; the four contributions (structure, decision, complexity, counterexample)
stated as a list.

**2. Preliminaries.** Notation aligned with the two papers; the layer decomposition
$(c=k-\omega)$; standing conventions (Euclidean inner product; row-full-rank input; the pre-check
$\operatorname{rank}L_0=r_0$).

**3. Geometry of the layer.**
 3.1 Kernel direction and the structural conditions ($V\subseteq U_v^\perp$, $\dim(V\cap K_0)=k-1$).
 3.2 The direction theorem: admissible directions are compression eigenvectors (proof via the two
 functionals; the prescribed-row refinement).
 3.3 Eigen/non-eigen stratification; the linear structure $\ker A_{21}$ inside $E_\mu$.
 3.4 The parameterization theorem with prescribed rows (Theorem 1′), including the correctness of the
 dimension formulas and the nonemptiness inequalities $\delta\le s\le r(v)$.

**4. Decision.**
 4.1 Closedness and the generic-gcd criterion (with the finite-cover refinement).
 4.2 Chartwise computation: Grassmann charts, minors, gcd; the full-rank leading-coefficient lemma.
 4.3 Sufficient and negative certificates (direction screen, fibre-dimension inequalities,
 resultant as a one-sided test).

**5. Complexity.** The bit-complexity lemmas (heights, chart sizes, fraction-free subresultants) and
the fixed-$p$ theorem; a discussion of where the argument stops when the spectrum is not simple.

**6. The repeated-eigenvalue counterexample.** Complete data, the six-direction table, the
certificates, and the statement of what it rules out.

**7. Relation to the two papers.** The compressed formulation (Paper I), the subspace description and
the order bound $\omega+1\le\dim W\le2\omega$ (Paper II), and the direction duality; a short table
separating inherited results from new ones.

**Appendix A. Exact computations.** The instances, the Bézout certificates and the common-factor
certificates; the number-field arithmetic used.

---

## Part III. Questions

**Q1.** Is the balance right? I am inclined to put the *structure* (Sections 3 and 7) first and the
algorithm second, because the parameterization is the part that is most clearly new, while the
decision procedure is closer to Paper I's machinery. The alternative is algorithm-first, with the
geometry as a tool.

**Q2.** Should the counterexample be a section or the opening motivation? It is the sharpest single
statement ("one eigenvector per eigenvalue is not enough"), and it is self-contained; but it is also
a negative result, and opening with it might suggest the paper is about failure modes.

**Q3.** The complexity theorem is conditioned on geometric simplicity. Is such a conditional theorem
acceptable as a headline result, provided the hypothesis is stated in the abstract and the
counterexample explains why it cannot be dropped?

**Q4.** Should the duality with Paper II be a numbered theorem or a remark? It is a clean statement
and it links the three documents; but it is also short, and a theorem may overweight it.

**Q5.** Is there anything in the current package that you would remove? In particular: the
finite-cover refinement of the closedness argument, and the "relative Grassmann bundle" formulation,
are both technical improvements over a naive statement; I am unsure whether they earn their space in a
standalone paper or belong in a remark.

### Reliability of the underlying results

| Item | Status |
|---|---|
| Closedness, generic criterion, finite cover | proved |
| Direction theorem (with prescribed rows) | proved |
| Parameterization theorem and dimensions | proved, after the prescribed-row correction |
| Chartwise decision; full-rank lemma | proved; implemented with exact arithmetic |
| Fixed-$p$ complexity | proved, relying on standard facts (factorization, root isolation, subresultant PRS) |
| Counterexample | exact computation with certificates |
| Duality | proved |
