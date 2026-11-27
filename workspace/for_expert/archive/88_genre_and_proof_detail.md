# What kind of paper is this, and how much proof detail does it need?

## Part I. The object and the two results

**Data.** Rational matrices $A\in\mathbb Q^{n\times n}$, $C\in\mathbb Q^{p\times n}$,
$L_0\in\mathbb Q^{r_0\times n}$, an integer $q\ge r_0$, and free rows
$R\in\mathbb R^{r\times n}$, $r=q-r_0$, with $L=[L_0;R]$. The decision problem asks
whether some $R$ satisfies

$$\operatorname{rank}\begin{bmatrix}LA\\ L\\ CA\\ C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}L\\ CA\\ C\end{bmatrix}
\quad\text{and}\quad
\operatorname{rank}\begin{bmatrix}\lambda L-LA\\ CA\\ C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}L\\ CA\\ C\end{bmatrix}\ \ \forall\lambda\in\mathbb C .$$

**Results.** With $K_0=\ker[C;CA]$, $N$ a basis of $K_0$, $H=LN$, $H_A=LAN$,
$\omega=\operatorname{rank}H$, and $\kappa_{\rm obs}=r\operatorname{rank}[N\ AN]$: the
problem is decidable in $\mathcal L^{O(q^2)}$ bit operations for fixed $q$, and in
$f(\kappa_{\rm obs})\operatorname{poly}(\mathcal L)$ bit operations in general; the case
$r=0$ is decided exactly in polynomial time; and the problem lies in $\exists\mathbb R$.

## Part II. Two things we are unsure about

### A. Genre

The text sits between three genres, and we do not know which one it should be.

- **A mathematics paper** would give complete proofs of each lemma, with the degree and
  rank bookkeeping written out, and would treat "$\exists\mathbb R$ membership" as a
  corollary of the encoding.
- **A complexity paper** would state the algorithm, prove correctness, and then *cite*
  classical tools (Hadamard's inequality, Cramer's rule, Renegar's bound) with the
  parameters mapped explicitly, without re-deriving them.
- **A control paper** would foreground the structural reduction (compression, effective
  dimension) and treat the two algorithms as the payoff.

The current draft is a hybrid, and we suspect that is why the proofs read as "detailed in
appearance, framework in substance".

### B. Proof detail: six places where a step is named rather than derived

1. *Lemma 1(iii), maximal-minor criterion.* "A pencil of rank $\omega$ loses rank at
   exactly those $\lambda$ at which all its $\omega\times\omega$ maximal minors vanish,
   which is the standard maximal-minor criterion for constant rank." — no proof, no
   reference.
2. *Lemma 2, dimension count.* "The dimension count is the rank-nullity theorem for
   $r_i\mapsto(r_iN,r_iAN)$, whose image is $\mathcal T$." — the kernel is not identified.
3. *Lemma 3, rank consistency.* The chain $Mb=c\iff c\in\operatorname{im}M\iff
   \operatorname{im}M=\operatorname{im}[M\ c]$ is asserted in one sentence.
4. *Lemma 5, row space of the coefficient matrix.* "Row $(i,j)$ of $Z$ is the coefficient
   vector of $\lambda^jf_i$. Hence a combination with weights $y_{i,j}$ is the coefficient
   vector of $\sum_{i,j}y_{i,j}\lambda^jf_i$" — the identification is plausible but is
   carried by prose.
5. *Theorem 1, complexity.* "the chart factor $(q+1)k^q\le\mathcal L^{O(q)}$ is absorbed."
   The exponent arithmetic is asserted.
6. *Coefficient-size lemma.* "Gaussian elimination on $[C;CA]$ writes $N$ as ratios of
   minors of the input; Cramer's rule and Hadamard's bound give $\operatorname{poly}(n,
   \mathcal L)$ bits." — this is the step we trust least; no constant or exponent is
   written down, and an error here would not affect correctness but would affect both
   stated bounds.

In a mathematics paper all six would be expanded. In a complexity paper, 1, 3 and 6 would
normally be cited (with a reference for the maximal-minor criterion and for Hadamard), and
2, 4, 5 expanded. We do not know which treatment a referee in this area would expect.

### C. Formalization coverage, briefly

Four statements are formalized in Lean 4 with Mathlib and are axiom-clean: the compression
criterion, the attainable-pair space with its dimension, rank consistency, and Bézout for
two polynomials. Everything matrix-level, everything with degrees or bit sizes, and the
encoding are paper-level. The formalization gaps are (i) rectangular Cauchy–Binet, which
Mathlib does not appear to have; (ii) Bézout with the degree bound for $s$ polynomials;
(iii) the rectangular adjugate and the linear system for $r=0$; (iv) coefficient bit sizes;
(v) the $\exists\mathbb R$ encoding. Questions on these are being asked separately; the
question here is whether the answer depends on the genre.

## Part III. Questions

1. **Which genre should this paper be?** If it is a complexity paper, is it acceptable that
   the structural reduction (Sections III–V) is proved in full while the classical analytic
   facts (maximal-minor criterion, Hadamard, Renegar) are cited?
2. **Are the six steps in B acceptable as written** for the genre you recommend, or which of
   them must be expanded? Our own ranking of risk is 6 (coefficient sizes) highest, then 5,
   then 2 and 4.
3. **What would a referee check first?** If only a limited amount of work can go into
   expanding proofs, which of the six would you expand?
4. **Does the genre change the formalization priority?** For instance, is it defensible to
   formalize the four algebraic cores and the main statements, and leave the analytic and
   bit-size facts as paper-level with an explicit audit, or does the paper's claim require
   kernel-checking the complexity bounds as well?
5. **Is the emphasized contribution the right one?** We foreground the Cauchy–Binet
   compression of the Gram certificate. An alternative framing is that the real observation
   is structural: the two conditions act on matrices that come from *one* block of free
   rows, so the free parameters are constrained to a subspace rather than filling the
   matrices. If you were writing this paper, which would you make the headline?
6. **Is the current title and abstract consistent with that genre?**
