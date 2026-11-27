# Paper status and open questions

## Part I. Problem and standard form

Let \(A\in\mathbb C^{n\times n}\), \(C\in\mathbb C^{p\times n}\), and
\(L_0\in\mathbb C^{r_0\times n}\) be given. For an integer \(q\ge r_0\), write
\[
L=\begin{bmatrix}L_0\\ R\end{bmatrix}\in\mathbb C^{q\times n}
\]
and impose
\[
(5a)\quad \operatorname{rank}\begin{bmatrix}LA\\ L\\ CA\\ C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}L\\ CA\\ C\end{bmatrix},
\]
\[
(5b)\quad \operatorname{rank}\begin{bmatrix}\lambda L-LA\\ CA\\ C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}L\\ CA\\ C\end{bmatrix}
\quad\forall \lambda\in\mathbb C.
\]
These are the standard functional-observer conditions. The decision problem
\(\mathrm{DEC}(q)\) asks whether such an \(R\) exists for a given \(q\); \(q1\)
asks for the complexity of computing the minimum feasible \(q\).

The characterization problem is settled in the literature (Fernando 2010;
Fernando 2026a, 2026b): order spectrum, per-order necessary and sufficient
conditions, minimum order, and construction. The complexity of the resulting
existential problem is not settled. The paper does not claim to settle it.

The compression used throughout is as follows. Let
\[
K_0=\ker\begin{bmatrix}C\\CA\end{bmatrix},\qquad k=\dim K_0,
\]
let \(N\) be a basis of \(K_0\), and set
\[
H=LN,\qquad H_A=LAN,\qquad \omega=\operatorname{rank}H.
\]
Then \((5a)\) is equivalent to
\[
\operatorname{row}H_A\subseteq\operatorname{row}H,
\]
and \((5b)\) is equivalent to
\[
\operatorname{rank}(\lambda H-H_A)=\omega\quad\forall\lambda\in\mathbb C.
\]
The free observer rows satisfy
\[
(H_i,(H_A)_i)\in\mathcal T:=\operatorname{row}[N\ AN],
\qquad d_0=\dim\mathcal T,
\]
and with \(r=q-r_0\),
\[
\kappa_{\rm obs}=r\,d_0.
\]

## Part II. Current paper

### II.1 Scope

The paper is an algorithmic and structural paper, provisionally titled
“Two parameterized algorithms for minimum-order functional observer design.”
It contains:

- a compression/pencil reduction;
- a fixed-order polynomial-time algorithm;
- a fixed-\(\kappa_{\rm obs}\) FPT algorithm;
- an \(\exists\mathbb R\) membership statement;
- a combined parameterized bound.

Hardness, gadget constructions, wiring, and failed reduction attempts are
deliberately excluded. They are kept in separate project notes.

### II.2 Lemma A: compression and pencil criterion

Statement:

1. \((5a)\iff\operatorname{row}H_A\subseteq\operatorname{row}H\).
2. If \((5a)\), there is \(F\) with \(H_A=FH\).
3. \((5b)\) iff the \(\omega\)-minors of \(P(\lambda)=\lambda H-H_A\) have gcd one.
4. If \((5a)\) and \((5b)\), then \(\operatorname{rank}H_A=\operatorname{rank}H\).

The proof is paper-level. Its abstract kernel is Lean-verified: the compressed
kernel criterion, the quotient factorization, and the dimension count. The
matrix-to-subspace annihilator step is paper-only.

### II.3 Lemma B: free-row parametrization

Every free-row pair lies in \(\mathcal T=\operatorname{row}[N\ AN]\); with
\(d_0=\dim\mathcal T\), each free row uses exactly \(d_0\) coordinates, hence
\(\kappa_{\rm obs}=rd_0\) total. Also
\[
k\le d_0\le\kappa_{\rm obs}\quad(r\ge1).
\]
The dimension inequalities are Lean-verified.

### II.4 Lemma C: rank factorization and consistency

For a pivot set \(J\),
\[
H=XB,\qquad B_{:,J}=I_\omega,
\]
and with \(G=FX\),
\[
H_A=GB,\qquad P(\lambda)=(\lambda X-G)B.
\]
The substitution \(G=FX\) is Lean-verified. The remaining part is a parametric
linear system
\[
M(X,G)b=c(X,G),
\]
with the rectangular consistency criterion
\[
\exists b:\ Mb=c
\iff
\operatorname{rank}(MM^{\mathsf T})
=\operatorname{rank}(MM^{\mathsf T}+cc^{\mathsf T}).
\]
The subspace form of consistency is Lean-verified; the Gram/rank form is
paper-level and checked on random instances.

### II.5 Lemma D: spectral certificate

Let \(f_i\) be the maximal minors of \(P(\lambda)\). The paper uses:

- Bezout: if the \(f_i\) have no common complex root and
  \(\deg f_i\le\omega\), then there are \(g_i\) with
  \(\deg g_i<\omega\) and \(\sum g_i f_i=1\);
- the \(2\omega\)-row coefficient matrix
  \[
  B_{(i,j),t}=c_{i,t-j};
  \]
- the equivalence
  \[
  (5b)\iff e_0\in\operatorname{row}B
  \iff\exists x:\ B^{\mathsf T}Bx=e_0;
  \]
- Cauchy–Binet:
  \[
  K(\lambda,\mu)=\sum_{|J|=\omega}
  \det(P(\lambda)_{:,J}^{\mathsf T}P(\mu)_{:,J})
  =\sum_i f_i(\lambda)f_i(\mu),
  \]
  and the shifted index formula for \(B^{\mathsf T}B\).

The two-polynomial Bezout core and the real sum-of-squares lemma are
Lean-verified. The degree bound, the row-space identification, and
Cauchy–Binet are paper-level; Cauchy–Binet is not available in the current
Lean library, so it is checked only on random exact examples.

### II.6 Theorems

**Theorem 1.** \(q1\in\exists\mathbb R\).

**Theorem 2.** For every fixed \(q\), \(q1\) is decidable in deterministic
polynomial time, with a coarse bound
\[
\mathcal L^{O(q^2)},
\]
where \(\mathcal L\) is the input bit length.

**Theorem 3 (real-RAM).** With
\[
\kappa_{\rm obs}=r\operatorname{rank}[N\ AN],
\]
the problem is fixed-parameter tractable in the real-RAM model with bound
\[
f(\kappa_{\rm obs})\operatorname{poly}(\mathcal L).
\]

**Corollary 3b (bit model).** If Renegar's real-feasibility bound is available
in the form
\[
(sD)^{O(N)}\operatorname{poly}(B),
\]
then the same algorithm gives
\[
f(\kappa_{\rm obs})\operatorname{poly}(\mathcal L)
\]
bit operations.

**Theorem 4.** In the real-RAM model (and in the bit model under
Corollary 3b),
\[
T\le\min\{\mathcal L^{O(q^2)},\ f(\kappa_{\rm obs})\operatorname{poly}(\mathcal L)\}.
\]

### II.7 Verification status

Lean: a separate project verifies the algebraic kernel (compression, quotient
factorization, free-pair dimension, \(G=FX\), consistency, Bezout core,
positivity, \(k\le d_0\le\kappa_{\rm obs}\), \(r=0\) left-inverse injectivity).
Axiom audits show only `propext`, `Classical.choice`, `Quot.sound`.

Exact checks: Gram certificate on random polynomial families with negative
controls; Cauchy–Binet and shifted index on random pencils; \(r=0\) rectangular
adjugate and the \(2\omega-2\) degree bound; the earlier layer/certificate
checks.

Paper: all main proofs are drafted. The paper is not yet frozen; the open
checks are listed below.

## Part III. Questions

### III.1 Positioning and publishability

1. Is the theorem set
   \[
   q1\in\exists\mathbb R,\qquad
   \text{fixed }q:\ q1\in\mathrm P,\qquad
   q1\in\mathrm{FPT}(\kappa_{\rm obs})
   \]
   a coherent and sufficiently strong paper, given that Fernando 2026 already
   settled the characterization and construction?
2. Should the paper be positioned as an algorithmic/parameterized-complexity
   paper, with the structural lemmas as preliminaries, or as a structural paper
   with algorithms as applications?
3. Is the fixed-order result \(\mathcal L^{O(q^2)}\) acceptable as a second
   theorem, or is it too coarse to be interesting?

### III.2 Renegar and the bit model

4. What is the exact bit-complexity form of Renegar's real-feasibility bound:
   is it \((sD)^{O(N)}\operatorname{poly}(B)\), or does it contain
   \(B^{O(N)}\)? This determines whether Theorem 3 holds in the bit model or
   only in the real-RAM model.
5. If only the real-RAM form is available, is it acceptable to present
   Theorem 3 as a real-RAM FPT theorem and Corollary 3b as a conditional
   bit-model statement? Or should the paper avoid the bit-model claim entirely?
6. Is there a standard reference that states the bit-model FPT consequence
   directly, so that the corollary can be made unconditional?

### III.3 Fixed-order complexity

7. Is the count
   \[
   N=O(q^2),\qquad D=O(k),\qquad s=O(k)
   \]
   sufficient to justify \(\mathcal L^{O(q^2)}\), or is there a hidden
   dependence on the number of pivot charts or on the rank-consistency
   disjunction that should be made explicit?

### III.4 Proof reliability

8. Is the Bezout degree bound
   \[
   \deg f_i\le\omega,\ \text{no common root}
   \Longrightarrow
   \exists g_i,\ \deg g_i<\omega,\ \sum g_i f_i=1
   \]
   correct as stated? The paper chooses two constant-coefficient combinations
   \(g,h\), makes them coprime, and expands the two-polynomial Bezout identity.
   Is there a missing genericity or degree hypothesis?
9. Is the row-space identification
   \[
   \operatorname{row}B
   =\left\{\text{coefficient vectors of }\sum_i g_i f_i:
   \deg g_i<\omega\right\}
   \]
   correct with the indexing \(B_{(i,j),t}=c_{i,t-j}\)?
10. Is the \(r=0\) rectangular adjugate construction
    \[
    S_I Q=f_I I_\omega,\qquad S=\sum_I g_I S_I
    \]
    correct, and is the degree bound \(2\omega-2\) sharp?
11. Is the Cauchy–Binet step acceptable as a paper-level proof, given that the
    Lean library has no rectangular Cauchy–Binet theorem, or should it be
    formalized before submission?

### III.5 \(\exists\mathbb R\) encoding

12. The paper uses a polynomial left inverse of degree at most \(2\omega-2\)
    for \(Q(\lambda)=\lambda X-G\). Is the degree bound correct in the
    degenerate rank strata, and is the finite disjunction over
    \(s=\dim(Z\cap\mathcal V)\) sufficient?
13. Does the \(\exists\mathbb R\) encoding need an explicit bound on the number
    of disjuncts and their degrees to claim polynomial size?

### III.6 Next step

14. Should the immediate next step be:
    - freeze and submit the algorithmic paper;
    - first resolve the Renegar bit dependence;
    - or return to unrestricted \(q1\) hardness?
15. If the paper is submitted, what is the most likely referee objection:
    the parameterized framing, the coarse fixed-\(q\) bound, the bit-model
    issue, or the overlap with Fernando 2026?

### III.7 What would change the recommendation

16. Is there a plausible route to unconditional bit-model FPT that avoids
    real QE, e.g. a combinatorial or algebraic decision procedure for the
    Gram–Bezout system?
17. Would a hardness result for \(q\) (XP versus W[1]) substantially strengthen
    the paper, or is it a separate project?

## Summary of the current claim boundary

The paper proves two parameterized upper bounds and an \(\exists\mathbb R\)
membership statement. It does not claim \(q1\in\mathrm P\), does not claim
\(\exists\mathbb R\)-completeness, and contains no hardness reduction.
The main unresolved technical point is the bit-model form of Renegar's bound;
the main unresolved editorial point is whether the two parameterized theorems
are enough for a standalone paper.
