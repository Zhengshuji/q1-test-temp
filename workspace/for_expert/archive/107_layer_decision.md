# The layer-by-layer decision of the compressed observer: a corrected picture

This report supersedes part of the previous one. The earlier claim that the layer decision is a
dichotomy — "polynomial, or infeasible" — was wrong in both directions, and the corrections are
recorded below because they change what the layer analysis can be used for. What survives is a
small set of statements, and the questions at the end ask whether they can be assembled into a
theorem about the decision problem.

---

## Part I. Setting

\(A\in\mathbb Q^{n\times n}\), \(C\in\mathbb Q^{p\times n}\), \(L_0\in\mathbb Q^{r_0\times n}\),
witness \(R\in\mathbb F^{m\times n}\), \(\mathcal L=[L_0;R]\), and
\[
K_0=\ker[C;CA],\quad k=\dim K_0,\quad N\text{ a basis},\quad H=LN,\quad H_A=LAN,\quad \omega=\operatorname{rank}H,
\]
\[
(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \operatorname{rank}(\lambda H-H_A)=\omega\ \ \forall\lambda .
\]
The decision is \(\exists R\), decomposed over the layer number:
\(\text{decision}=\bigvee_{\omega=0}^{k}(\text{layer }\omega\text{ feasible})\).

Notation: \(\mathcal S=\operatorname{row}[N\ AN]\subseteq V\oplus V\) (pairs \((rN,rAN)\)),
\(\mathcal T_W=\mathcal S\cap(W\oplus W)\) for an \(\omega\)-dimensional \(W\subseteq V=\mathbb F^{1\times k}\),
and the evaluation map
\[
E_\lambda:\mathcal T_W\to W,\qquad (x,y)\mapsto\lambda x-y .
\]

Two standing facts. **Kernel lemma:** feasibility implies \(\ker H=\ker H_A\). **Fibrewise rigidity:** the
feasible set inside each fibre is Zariski open, so no polynomial condition can be imposed on the free rows
beyond what the fibre itself forces. Also, the compatible row spaces are
\(\{W:U\subseteq W\}\cong\operatorname{Gr}(\omega-d,k-d)\), where \(U=\operatorname{span}\{h_i^0,g_i^0\}\) and \(d=\dim U\).

---

## Part II. Results

### II.1 The middle layers: the correct criterion

> **Proposition (middle layer).** Fix a compatible \(W\) and let \(m\) be the number of free rows.
> If \(m\ge\dim\mathcal T_W\), then
> \[
> \text{layer }\omega\text{ feasible on the fibre of }W\iff E_\lambda(\mathcal T_W)=W\ \ \forall\lambda .
> \]

*Proof.* \((\Leftarrow)\) take a basis of \(\mathcal T_W\) as the free rows: every admissible pair is realised by some
row, so the pencil's rows span \(E_\lambda(\mathcal T_W)=W\) at every \(\lambda\), giving rank \(\omega\).
\((\Rightarrow)\) the rows lie in \(E_\lambda(\mathcal T_W)\), so rank \(\omega\) for all \(\lambda\) forces surjectivity. \(\square\)

The condition \(E_\lambda(\mathcal T_W)=W\ \forall\lambda\) is decidable: choose a basis \(p_1,\dots,p_D\) of
\(\mathcal T_W\), form the \(D\times\omega\) matrix \(M(\lambda)=(\lambda x_j-y_j)_j\), and test whether its
\(\omega\times\omega\) minors are coprime — a gcd computation.

**An analytic counterexample to a tempting simplification.** One might guess that surjectivity for all
\(\lambda\) forces \(\mathcal T_W=W\oplus W\). It does not. Take \(\omega=2\),
\(\mathcal T=\ker\varphi\subseteq W\oplus W\) with \(\varphi(x,y)=\alpha(x)+\beta(y)\), where
\(\alpha\notin\operatorname{span}\{\beta\}\). Then \(\dim\mathcal T=2\omega-1\), and \(E_\lambda(\mathcal T)\ne W\)
would require some \(0\ne\gamma\) with \((\lambda\gamma,-\gamma)\in\operatorname{span}\{\varphi\}\), i.e.
\(\alpha=-\lambda\beta\) — impossible. So surjectivity holds for every \(\lambda\) with
\(\dim\mathcal T_W=2\omega-1\).

### II.2 The layers that are decided

* **Layer \(\omega=0\):** feasible iff \(L_0[N\ AN]=0\) (take \(R=0\)). No further condition under the stated
  witness definition.
* **Top layer \(\omega=k\):** \(W=V\), so compatibility is automatic; rank completion is possible iff
  \(m\ge k-\operatorname{rank}(L_0N)\). Given rank completion, a necessary condition is that
  \((\lambda I-A)N\) have rank \(k\) for every \(\lambda\) (i.e. no eigenvector of \(A\) lies in \(K_0\)); this
  was verified sufficient on rational instances. It is a gcd test and does not involve \(L_0\) beyond the
  rank-completion threshold.
* **Middle layers:** the proposition above, so the layer decision reduces to a gcd test on \(M(\lambda)\).

In each case the test is a gcd computation, hence polynomial for fixed bounds.

### II.3 Corrections recorded

1. *"Every middle layer is infeasible"* — false; a rational feasible example exists (non-characteristic,
   \(\omega=1<k=2\)). Withdrawn.
2. *"The top layer's rank completion is automatic for \(m\ge1\)"* — false; the threshold is
   \(m\ge k-\operatorname{rank}(L_0N)\). Corrected.
3. *"The middle-layer criterion is \(\mathcal T_W=W\oplus W\), i.e. \(\dim=2\omega\)"* — false; the counterexample
   of II.1 has \(\dim=2\omega-1\) and is feasible. Replaced by the proposition above.
4. *"Surjectivity for all \(\lambda\) is not sufficient, because a finite selection of rows cannot cover all
   \(\lambda\)"* — false; taking a basis of \(\mathcal T_W\) always works when \(m\ge\dim\mathcal T_W\). Withdrawn.
5. Several earlier numerical "refutations" of the sufficiency were artifacts of testing a weakened condition
   (projection ranks instead of coprimality). The comparison that exposed this was a constructive test
   (basis of \(\mathcal T_W\) as rows) against the symbolic gcd; they agree verbatim in every case tested.

---

## Part III. Questions

**Q1.** Is the proposition of II.1 the right level of generality, or should the row-count hypothesis be
sharpened? In particular, when \(m<\dim\mathcal T_W\), is there a useful criterion in terms of the
\(m\)-dimensional subspaces of \(\mathcal T_W\)?

**Q2.** For a general \(\mathcal S\), is "\(\exists W\) with \(E_\lambda(\mathcal T_W)=W\) for all \(\lambda\)"
decidable in polynomial time? The condition is a gcd on minors whose entries are linear in \(\lambda\) and
whose size is \(\dim\mathcal T_W\); the search over \(W\) is the only apparent obstruction. Is there a
Grassmannian-level argument that removes the search?

**Q3.** Does the fibre-rigidity obstruction interact with II.1? The proposition says the fibre is feasible
exactly when the pair space is large enough; but rigidity says the feasible set is open in the fibre.
Do these two statements have a common refinement, for instance in terms of the codimension of
\(\mathcal T_W\) in \(W\oplus W\)?

**Q4.** In the top layer, is the "no eigenvector of \(A\) in \(K_0\)" condition really sufficient, or can the
fixed row \(L_0\) obstruct the spectral completion even when it holds? A clean counterexample either way
would settle whether the top layer is decidable by two independent gcd tests.

**Q5.** If every layer is decidable by a gcd, the decision is polynomial. Is there any part of the layer
analysis that the present arguments do **not** cover — for instance, the interaction between the choice of
\(N\) and the top-layer criterion when \(N\) is not fixed but optimised?

### Reliability

| item | label |
|---|---|
| kernel lemma, fibrewise rigidity, compatibility Grassmannian | proved |
| middle-layer proposition (with \(m\ge\dim\mathcal T_W\)) | proved |
| analytic counterexample to "\(\dim=2\omega\)" | proved |
| top-layer: necessity of "no eigenvector in \(K_0\)" | proved |
| top-layer: sufficiency | verified on rational instances only |
| layer \(\omega=0\) | proved |
| "every layer decidable in polynomial time" | **not proved** — the search over \(W\) is open |
