# What the compressed model can express, and what a reduction would actually require

This note reports the state of the "encode the source problem in \((A,C,L_0)\), free rows as witnesses"
programme. Six primitives are now proved. One earlier conclusion of ours — that this architecture cannot support a
reduction from an existential problem — was **withdrawn after a self-check**; what remains is a precise, open
question about expressive power. The characterisation itself is not at issue.

---

## Part I. Setting

Fix \(A\in\mathbb Q^{n\times n}\), \(C\in\mathbb Q^{p\times n}\), \(L_0\in\mathbb Q^{r_0\times n}\);
\(\mathcal L=[L_0;R]\), \(R\) the \(m\times n\) free rows,
\[
K_0=\ker[C;CA],\quad k=\dim K_0,\quad N\text{ a basis},\quad H=LN,\quad H_A=LAN,\quad \omega=\operatorname{rank}H,
\]
\[
(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \operatorname{rank}(\lambda H-H_A)=\omega\ \ \forall\lambda .
\]

**Kernel lemma.** Every feasible pair satisfies \(\ker H=\ker H_A\). (From \((5b)\) at \(\lambda=0\) and \((5a)\).)
Consequences: \(H\) and \(H_A\) have the same zero columns, and \(\operatorname{rank}H_{[:,J]}=\operatorname{rank}(H_A)_{[:,J]}\)
for every set \(J\) of compressed coordinates.

**Fibrewise rigidity.** For an \(\omega\)-dimensional space \(W\), let \(M_W=\{R:h_i,g_i\in W\}\), a
linear subspace. On the exact-rank part of \(M_W\), \((5a)\) is automatic and \((5b)\) is open, so the feasible
set is Zariski open in \(M_W\), hence dense whenever non-empty. Therefore **every polynomial relation satisfied
by all feasible points of an active fibre is already an identity on that fibre.**

---

## Part II. Results

### II.1 Primitives (all acting on the instance data)

Per block: \(C_i=[0\,0\,1]\), \(A_i(t)=\begin{pmatrix}0&0&0\\t&0&0\\0&1&0\end{pmatrix}\), and with
\(L_{0,i}=[a_i\ b_i\ c_i]\) the compressed columns are
\[
H\text{'s column }i=(a_i;u_i),\qquad H_A\text{'s column }i=t_i(b_i;v_i),
\]
with \(u_i,v_i\) free.

1. **Literal gate**: \(a_i=1,b_i=0\) is feasible iff \(t_i\ne0\).
2. **Negation**: the reduction computes the data, so feeding \(1-x\) tests \(\neg x\) for Boolean \(x\).
3. **Conjunction, arbitrary \(k\)**: the anchored block-diagonal direct sum (\(C\) *stacked*, not concatenated)
   with \(m=k\) free rows is feasible iff \(\prod_{i}t_i\ne0\). Soundness is the kernel lemma
   (\(t_i=0\) kills \((H_A)_{\bullet i}\) but not \(H_{\bullet i}\)); completeness is explicit
   (\(H=[\mathbf 1^{\mathsf T};I_k]\), \(H_A=[0;D]\) with \(D\) diagonal with distinct non-zero entries).
4. **Equation gate**: with \(\dim(AK_0)=1\) only layer 1 survives; then
   \(H=\begin{pmatrix}t&0\\u_1&u_2\end{pmatrix}\), \(H_A=\begin{pmatrix}1&1\\w&w\end{pmatrix}\)
   (the two free entries coincide), and feasibility is equivalent to \(t=0\) — by the row-space argument:
   \(\operatorname{row}H_A=\operatorname{span}\{(1,1)\}\) must equal \(\operatorname{row}H\), and \(H\)'s first
   row \((t,0)\) lies there iff \(t=0\).
5. **Booleanity gate**: at layer 1 with \(k=2\) and \(r=r_0+m=2=k\), the fixed-row parts give
   \[
   \det\begin{pmatrix}a_1&a_2\\ t_1b_1&t_2b_2\end{pmatrix}=0 .
   \]
   Taking \(a=(x,0)\), \(b=(1,1)\), \(t=(1,x-1)\) makes this \(x(x-1)=0\), i.e. **feasible iff \(x\in\{0,1\}\)**.
   (Layer 2 is a square pencil and hence impossible, so nothing is masked.)
6. **Conjunction of equations**: two fixed rows give \(v\) twice as many equations, so the layer-1 condition
   becomes a system. With \(L_0=\begin{pmatrix}x&0&1&0\\ y&0&1&0\end{pmatrix}\) and \(\dim(AK_0)=1\),
   feasibility is equivalent to \(x=0\wedge y=0\).

All six were proved, and 4–6 were additionally checked exactly on rational parameter values.

### II.2 The witness side cannot filter — but that is not an obstruction

By fibrewise rigidity, a closed condition satisfied at every feasible point holds identically on each active
fibre; so it **cannot exclude any witness**. This is a genuine limitation, and it explains why every gadget of
the "force a relation among the free rows" type failed, including a long series of multiplication-gate attempts.

Our earlier conclusion — that this makes reductions from existential problems impossible — **was wrong** and we
withdraw it. The error was to infer "no reduction" from "no filtering". A reduction requires

\[
\text{source instance satisfiable}\iff\text{the instance }(A,C,L_0)\text{ is feasible},
\]

and feasibility is a condition **on the instance data**; it is not necessary to filter witnesses at all. Indeed a
constraint that holds automatically on a fibre is exactly what soundness wants: every feasible witness then
decodes to a valid solution.

### II.3 What a reduction would require

The source instance supplies **coefficients**; its satisfiability is "\(\exists x\): the system holds". The
reduction must map the coefficients to \((A,C,L_0)\) so that

\[
\exists x:\text{system}(x)=0\iff\exists R:\ (5a)\wedge(5b).
\]

The witness \(R\) implements the existential quantifier; it does not need to be filtered. So the real question is
about **expressive power of the feasibility condition, as a function of the instance data**:

> Which sets of coefficient vectors arise as \(\{(A,C,L_0):\exists R,\ (5a)\wedge(5b)\}\)?

The primitives above show that the answer includes, at least, systems of polynomial equations in the data
(including Booleanity conditions), so the data side is not poor. What is missing is a characterisation, and a
match with the coefficient-condition of a hard source problem.

---

## Part III. Questions

**Q1.** Is the reformulation of §II.3 the right target? Namely: characterise the family
\(\{\,\{(A,C,L_0):\exists R\}\,:\ (5a),(5b)\,\}\), and ask whether it contains the coefficient-condition of a
known hard problem. Or is there a structural reason why this family is too small?

**Q2.** The six primitives all act on the instance data; is there a natural *upper bound* on what the data side
can express? For instance, is the feasibility condition always a constructible set of a restricted kind
(e.g. defined by minors of bounded degree in the data), and would such a bound obstruct a reduction?

**Q3.** If a reduction is to be attempted, which source problem should be targeted? We have been aiming at
existential polynomial feasibility; the coefficient-condition viewpoint suggests instead a problem whose
satisfiability is naturally a condition on its data.

**Q4.** Our Booleanity gate produces \(x\in\{0,1\}\) for a parameter \(x\) of the *instance data*. Is there a way
to make the "variable" of a 0–1 feasibility problem range over instance data rather than over witnesses — for
example by having the reduction quantify over a family of instances?

**Q5.** Given that the witness side cannot filter and the data side is expressive but uncharacterised, what would
you consider the decisive next computation or theorem?

### Reliability

| item | label |
|---|---|
| kernel lemma, fibrewise rigidity | proved (fixed-row compatibility; field stated) |
| literal gate, negation, arbitrary-\(k\) conjunction | proved |
| equation gate | proved (display corrected after an earlier audit) |
| Booleanity gate, conjunction of equations | proved; checked exactly on rational values |
| "witness side cannot filter" | proved — but it does **not** obstruct reductions |
| "reduction impossible" | **withdrawn** (our own self-check) |
| expressive power of the data side | **open** — the question of §II.3 |
