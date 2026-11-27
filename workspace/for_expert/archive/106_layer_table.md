# Layer-by-layer decidability of the compressed observer: every layer is either polynomial or empty

This report closes the layer analysis of the compressed model that began with the active-subspace
reformulation. Its outcome is negative for the hardness programme: every layer turns out either to be
decidable in polynomial time, or to be infeasible for every instance. The questions at the end ask
whether the remaining gap can be closed into a theorem.

---

## Part I. Setting

Fix \(A\in\mathbb Q^{n\times n}\), \(C\in\mathbb Q^{p\times n}\), \(L_0\in\mathbb Q^{r_0\times n}\). A witness is
\(R\in\mathbb F^{m\times n}\), \(\mathcal L=[L_0;R]\), and
\[
K_0=\ker[C;CA],\quad k=\dim K_0,\quad N\ \text{a basis},\quad H=LN,\quad H_A=LAN,\quad \omega=\operatorname{rank}H,
\]
\[
(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \operatorname{rank}(\lambda H-H_A)=\omega\ \ \forall\lambda .
\]
The decision is \(\exists R\) satisfying \((5a)\) and \((5b)\); it decomposes over the layer number
\[
\text{decision}=\bigvee_{\omega=0}^{k}\bigl(\text{layer }\omega\text{ is feasible}\bigr).
\]
Hence any hardness must reside in the feasibility problem of a single layer.

**Kernel lemma.** Feasibility implies \(\ker H=\ker H_A\) (from \((5b)\) at \(\lambda=0\) and \((5a)\)).

**Fibrewise rigidity.** For an \(\omega\)-dimensional \(W\), let \(M_W\) be the linear space of free rows whose
compressed rows lie in \(W\). On the exact-rank part of \(M_W\), \((5a)\) is automatic and \((5b)\) is open, so
the feasible set is Zariski open in \(M_W\); a polynomial relation satisfied at all feasible points of an active
fibre is an identity on that fibre. Consequently no polynomial condition can be imposed on the free rows beyond
what the fibre already forces.

**Compatibility.** With fixed pairs \((h_i^0,g_i^0)=((L_0)_iN,(L_0)_iAN)\) and
\(U=\operatorname{span}\{h_i^0,g_i^0\}\), \(d=\dim U\), the compatible row spaces are
\[
\mathcal X_{\mathrm{comp}}=\{W\in\operatorname{Gr}(\omega,k):U\subseteq W\}\cong\operatorname{Gr}(\omega-d,k-d),
\qquad \dim=(\omega-d)(k-\omega).
\]

**Active-subspace test.** With \(\mathcal S=\operatorname{row}[N\ AN]\) and
\(\mathcal T_W=\mathcal S\cap(W\oplus W)\), a free row may be placed in the fibre of \(W\) exactly when its pair
lies in \(\mathcal T_W\); feasibility at layer \(\omega\) is equivalent to the existence of a compatible \(W\) whose
generic admissible pencil has coprime \(\omega\)-minors. Because the fibre is irreducible and both the exact-rank
condition and spectral regularity are open in it, spectral regularity may be tested on the whole fibre and
separately from rank completion.

---

## Part II. Results

### II.1 The layer table

**(a) Layer \(\omega=0\).** \(H=H_A=0\), i.e. \(L[N\ AN]=0\); then \((5a),(5b)\) hold automatically. So the
layer is feasible exactly when \(L_0\) annihilates \([N\ AN]\) and \(n>\dim\mathcal S\). An instance with
\(r_0=0\), or with \(L_0[N\ AN]=0\), is therefore **always feasible** and carries no information.

**(b) Top layer \(\omega=k\).** Here \(W=V\) is unique, \(\mathcal T_V=\mathcal S\), and both compatibility and rank
completion are automatic as soon as \(m\ge1\). Writing \(P(\lambda)=L(\lambda I-A)N\) one has
\[
\operatorname{rank}P(\lambda)\le\operatorname{rank}\bigl((\lambda I-A)N\bigr)=k-\dim\bigl(K_0\cap\ker(\lambda I-A)\bigr),
\]
so a necessary condition is that no eigenvector of \(A\) lies in \(K_0\). Conversely, with \(r=r_0+m\ge k+1\) the
condition is sufficient (checked on rational instances). Hence, for \(r\ge k+1\),
\[
\boxed{\text{top layer feasible}\iff K_0\cap\ker(\lambda I-A)=0\ \ \forall\lambda
\iff \gcd\text{ of the }k\text{-minors of }(\lambda I-A)N \text{ is constant.}}
\]
Two consequences: the criterion is **independent of \(L_0\)**, and it is decidable in polynomial time (a gcd
computation). Also \(r<k\) gives no \(k\times k\) minor and \(r=k\) gives a square pencil whose determinant has
degree \(k\) with leading coefficient \(\det H\neq0\), hence a root; both are infeasible.

**(c) Middle layers, non-characteristic.** If \(K_0\cap\ker(\lambda I-A)=0\) for all \(\lambda\), the layer is
infeasible; this reproduces the "non-characteristic layer is always bad" phenomenon: the pencil's determinant
is quadratic in \(\lambda\) and therefore has a complex root.

**(d) Middle layers, characteristic (new).** Take the programmed family
\[
K_0=\operatorname{span}\{e_1,\dots,e_k\},\qquad C=[0\,|\,I_k],\qquad A=\operatorname{blockdiag}(B,D).
\]
Then \(A\) acts on \(K_0\) by \(B\), so the drops
\(\dim(K_0\cap\ker(\lambda I-A))=\dim\ker(\lambda I-B)\) are **programmable**: their location is the spectrum of
\(B\) and their size its geometric multiplicity. For \(\omega=k-1\) the drop criterion requires all drops
\(\le1\), which distinct eigenvalues of \(B\) provide. The exact computation (symbolic fibre parameters, gcd over
\(\mathbb Q(\tau)[\lambda]\)) gives, for every case tested,
\[
\text{infeasible},\qquad \gcd=\text{a product of eigenvalue factors}:
\]
\(\operatorname{diag}(1,2,3)\mapsto(\lambda-3)(\lambda-1)\),
\(\operatorname{diag}(1,1,2)\mapsto(\lambda-2)(\lambda-1)\),
\(\operatorname{diag}(0,1,2)\mapsto\lambda(\lambda-2)\).
So the drop criterion is necessary but not sufficient: the eigenvalue factors cannot be removed by choosing the
free rows.

### II.2 What the table implies

Every layer falls into one of two classes: **polynomial-time decidable** (\(\omega=0\) and the top layer, both by
gcd computations), or **infeasible** (the middle layers, characteristic or not). Hence the decision
\(\bigvee_\omega\) is decidable in polynomial time on everything tested. This is evidence for the *positive*
side of the question, not for hardness.

### II.3 Corrections of earlier statements of this programme

1. *"Any number of relation-forcing gadgets is impossible"* — over-stated; replaced by fibrewise rigidity.
2. *"Only open conditions can be imposed, hence no hardness"* — withdrawn; that inference is invalid.
3. *"Layer two masks lower layers"* — withdrawn; the instance used had a square pencil and was infeasible at
   every layer.
4. *"The reduction programme is impossible because the source variables fit neither the data nor the witness"* —
   withdrawn; the error was to infer "no reduction" from "no witness filtering".
5. *"Two active subspaces on \(\operatorname{Gr}(2,3)\)"* — withdrawn; a sampling artifact (free rows were drawn
   outside \(\mathcal T_W\)).
6. *"For \(\omega<\min(k,r)\) the pencil must be identically rank-deficient, so random instances fail"* —
   withdrawn; \(\operatorname{rank}P\le\omega\) follows automatically from \((5a)\), so that is not a condition.
7. *"The middle layers die of the fixed common factor produced by the drop"* — refined; the drop is one
   mechanism, and the non-characteristic layers die of a different one.

---

## Part III. Questions

**Q1.** Is there a theorem saying that for \(0<\omega<k\) the gcd of the \(\omega\)-minors always contains a
factor coming from \(\operatorname{spec}(A|_{K_0})\)? The three programmed cases suggest it, and it would make the
"middle layers are always infeasible" statement a theorem rather than a table of examples. What hypothesis on
\(B\), \(D\), \(L_0\), \(m\) would be needed?

**Q2.** If the middle layers are always infeasible and the top layer is decidable by a gcd, then the decision is
in polynomial time. Is there an obstruction to turning this into a theorem — for instance, must one still handle
the case where the fixed row is not generic (so that the top-layer criterion could fail for a reason not captured
by \(K_0\cap\ker(\lambda I-A)\))?

**Q3.** The top-layer criterion is independent of \(L_0\). Is that a general phenomenon — that the *decision*
never depends on \(L_0\) except through the trivial layer — or is it an artefact of the top layer's automatic
compatibility?

**Q4.** The programmed family \(A=\operatorname{blockdiag}(B,D)\), \(C=[0\,|\,I]\) makes the drop structure
exactly \(\operatorname{spec}(B)\). Is the failure in (d) explained by the fixed row lying in the image of
\((\lambda I-A)N\) at the eigenvalues — i.e. by a rank deficiency of one that the single fixed row cannot repair?
If so, is there a choice of \(r_0>1\) that repairs it?

**Q5.** Given this table, what would a hardness witness have to look like? We can see only two ways out: either
the middle-layer failure has an exception we have not found, or hardness must come from a regime where the
compression itself (the choice of \(N\), hence of \(K_0\)) is part of the input in a way that defeats the gcd
tests.

### Reliability

| item | label |
|---|---|
| kernel lemma, fibrewise rigidity, compatibility Grassmannian | proved |
| layer \(\omega=0\) criterion | proved |
| top-layer criterion | necessity proved; sufficiency verified on rational instances for \(r\ge k+1\) |
| middle layers, non-characteristic | proved (via the quadratic determinant) |
| middle layers, characteristic | **verified on three programmed families**; no general proof |
| the layer table as a whole | **not yet a theorem**; it is what the cases support |
