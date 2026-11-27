# The compressed model as a constraint language: what it can express, and the disjunction wall

This note reports the current state of the "source data in \((A,C,L_0)\), free rows as witnesses" programme.
Four primitives are now proved; disjunction is not, and we have a structural explanation. The question is
whether that explanation is a theorem or a gap in our search.

---

## Part I. Setting

Fix \(A\in\mathbb Q^{n\times n}\), \(C\in\mathbb Q^{p\times n}\), \(L_0\in\mathbb Q^{r_0\times n}\);
\(\mathcal L=[L_0;R]\), \(R\) the \(m\times n\) free rows,
\[
K_0=\ker[C;CA],\quad k=\dim K_0,\quad N \text{ a basis},\quad H=LN,\quad H_A=LAN,\quad \omega=\operatorname{rank}H,
\]
\[
(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \operatorname{rank}(\lambda H-H_A)=\omega\ \ \forall\lambda .
\]
The decision asks whether some \(R\) (and some layer \(\omega\)) satisfies both.

**Kernel lemma.** For every feasible pair, \(\ker H=\ker H_A\). (From \((5b)\) at \(\lambda=0\),
\(\operatorname{rank}H_A=\operatorname{rank}H\); with \((5a)\), \(\operatorname{row}H_A=\operatorname{row}H\).)
Consequences: \(H\) and \(H_A\) have the same zero columns, and \(\operatorname{rank}H_{[:,J]}=\operatorname{rank}(H_A)_{[:,J]}\)
for every set \(J\) of compressed coordinates.

**Fibrewise rigidity.** For a fixed compressed row space \(W\) let \(M_W=\{R:h_i,g_i\in W\}\). On the
exact-rank part of \(M_W\), \((5a)\) is automatic and \((5b)\) is open, so the feasible set is Zariski open in the
linear space \(M_W\); hence a polynomial relation satisfied by all feasible points of an active fibre is already
an identity on that fibre. The spectral condition can therefore *select which fibres are active*, but cannot cut
inside one.

---

## Part II. The primitives

All constructions below use one block type. Per block (three coordinates), take
\(C_i=[0\ 0\ 1]\), \(A_i(t)=\begin{pmatrix}0&0&0\\ t&0&0\\ 0&1&0\end{pmatrix}\), so that
\(K_{0,i}=\operatorname{span}\{e_{3i-2}\}\), \(A_iN_i=t\,e_{3i-1}\), and with \(L_{0,i}=[a_i\ b_i\ c_i]\) the
contributions are
\[
H\text{'s column }i=(a_i;u_i),\qquad H_A\text{'s column }i=t_i\,(b_i;v_i)
\]
with \(u_i,v_i\) free.

### II.1 Literal gate

\(a_i=1\), \(b_i=0\): the block is feasible iff \(t_i\ne0\). (The anchor makes \(H\)'s column non-zero for every
choice of free data; for \(t_i=0\) the \(H_A\) column vanishes and \((5b)\) fails at \(\lambda=0\).)

### II.2 Negation

The gate reads "an affine function of the instance parameters is non-zero", and the reduction computes the
instance data, so feeding \(1-x\) tests \(\neg x\) for a Boolean source variable. This assumes Booleanity is
supplied elsewhere.

### II.3 Conjunction, arbitrary \(k\)

Anchored block-diagonal direct sum (\(C\) stacked block-diagonally — concatenating the blocks into one row
couples \(K_0\) and destroys the construction), with \(m=k\) free rows:

> **Theorem.** The instance is feasible iff \(\prod_{i=1}^k t_i\ne0\).

*Soundness* is the kernel lemma: if \(t_i=0\) then \((H_A)_{\bullet i}=0\) while \(H_{\bullet i}=(1;u_i)\ne0\).
*Completeness* is explicit: \(H=\begin{pmatrix}\mathbf1^{\mathsf T}\\ I_k\end{pmatrix}\),
\(H_A=\begin{pmatrix}0\\ D\end{pmatrix}\) with \(D=\operatorname{diag}(d_1,\dots,d_k)\), distinct non-zero; then
\(P(\lambda)=\begin{pmatrix}\lambda\mathbf1^{\mathsf T}\\ \lambda I-D\end{pmatrix}\) has full column rank for every
\(\lambda\) (off the diagonal values use invertibility of \(\lambda I-D\); at \(\lambda=d_j\) the kernel is
spanned by \(e_j\), killed by the top row).

### II.4 Equation gate

A layer can also carry an *equation*. Take \(n=4\), \(C=[0,0,0,1]\),
\[
A=\begin{pmatrix}0&0&0&0\\0&0&0&0\\1&1&0&0\\0&0&1&0\end{pmatrix},\qquad L_0=[t,0,1,0].
\]
Then \(K_0=\operatorname{span}\{e_1,e_2\}\) and \(AN=[e_3,e_3]\), so \(\dim(AK_0)=1\); the \(\lambda=0\) bound
\(\operatorname{rank}H\le\dim(AK_0)\) leaves **only the layer \(\omega=1\)** — no masking by higher layers. With
\[
H=\begin{pmatrix}t&0\\ u_1&u_2\end{pmatrix},\qquad H_A=\begin{pmatrix}1&1\\ w_1&w_2\end{pmatrix}
\]
the second column of \(H\) has first coordinate \(0\) whilst the first has \(t\), so \(\operatorname{rank}H=1\) is
impossible unless \(t=0\); and \(t=0\) is attainable with the free data. Hence

> **Theorem.** This instance is feasible iff \(t=0\).

So the language has literals, negation (Boolean inputs), conjunction (any \(k\)) and equations.

---

## Part III. The disjunction wall

Two routes, both analysed.

**Route A (the layer index is a built-in disjunction).** The decision quantifies over \(\omega\), so
"some layer is non-empty" is a disjunction. Put two equation-style gates in one instance with
\(\dim(AK_0)=2\), parameters \(t\) and \(t-1\):
\[
H=\begin{pmatrix}t&t-1\\ u_1&u_2\end{pmatrix},\qquad H_A=\begin{pmatrix}1&1\\ w_1&w_2\end{pmatrix}.
\]
*Layer 1* requires both columns on one line, which forces both anchors to vanish: \(t=0\) **and** \(t=1\) —
impossible. *Layer 2* is different: the kernel is trivial, the kernel lemma is vacuous, and the only condition is
that the \(2\times2\) minors have no common root. Taking \(u_2=0\), \(u_1=tw_2\), \(w_2\ne w_1\) makes
\(\det P\) a non-zero constant, so layer 2 is feasible **for every \(t\)**. Hence "layer 1 or layer 2" is the
whole parameter space: the disjunction is swallowed by the higher layer.

**Route B (two conditions on one layer).** On a fixed layer the mechanism that produces an equation is
"every column must lie on one line", and that forces *each* anchor to vanish — a conjunction. Rank conditions
are conjunctions of minor vanishings by nature.

The structural statement we can currently write is:

> **Observation.** Each layer's feasible set is open inside its rank stratum, and the layers are nested by rank;
> a higher layer has a trivial kernel and a generically regular pencil, so it is usually feasible. The built-in
> disjunction over layers therefore tends to collapse to "true", while a single layer can only produce
> conjunctions.

**The one direction not yet excluded.** Make a *higher* layer carry an equation as well: if the quadratic part
of \(\det P(\lambda)\) could be forced to vanish structurally, layer 2's condition would reduce to "a linear
polynomial has no root", whose truth is governed by a constant term — an equation. Then two layers could carry
two different equations and the built-in disjunction would do the job.

---

## Part IV. Questions

**Q1.** Is the "Observation" of Part III a theorem? Concretely: is there an instance in which two distinct
layers are non-empty only under two *different* equation-type conditions (with no higher layer masking them)?

**Q2.** Is the layer-2 masking argument tight? We used the freedom in \(u_i,w_i\) to make \(\det P\) a non-zero
constant. Is there a structural condition (e.g. forcing the top-row entry of \(P\) to vanish identically) that
prevents this and leaves an equation at layer 2?

**Q3.** The equation gate uses \(\dim(AK_0)=1\) to kill higher layers. Is there a way to keep two layers alive
while making *both* their conditions equations — or does the \(\lambda=0\) rank bound
\(\operatorname{rank}H\le\dim(AK_0)\) force a strict trade-off?

**Q4.** With literals, negation, conjunction and equations available but no disjunction, is there a decision
problem of matching strength that a reduction can target — e.g. a problem whose instances are systems of
polynomial equations, where the disjunction is not needed?

**Q5.** If the disjunction wall is real, is the right conclusion that this architecture cannot support a
CNF-style reduction, and what would be the honest statement of that limitation?

### Reliability

| item | label |
|---|---|
| kernel lemma | proved |
| fibrewise rigidity | proved (with fixed-row compatibility and the field stated) |
| literal gate, negation | proved |
| conjunction, arbitrary \(k\) | proved |
| equation gate | proved; checked exactly on five parameter values |
| disjunction | **not achieved** (two routes analysed and rejected) |
| the Part III "Observation" | a heuristic statement, not a theorem |
