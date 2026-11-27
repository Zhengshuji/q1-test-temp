# Can the compressed model simulate an arithmetic circuit? A negative answer for one architecture

This note reports what we now know about the "gadget" programme for the hardness question, and asks whether
the resulting limitation is a theorem or a dead end. The characterisation itself is not at issue; the question
is the decision complexity of the prescribed-row problem.

---

## Part I. The model, and the two paradigms

Fix rational \(A\in\mathbb Q^{n\times n}\), \(C\in\mathbb Q^{p\times n}\) of rank \(p\),
\(L_0\in\mathbb Q^{r_0\times n}\). For candidate \(q\) put \(\mathcal L=[L_0;R]\), \(R\) the \(m\times n\) free
rows, and
\[
K_0=\ker[C;CA],\quad k=\dim K_0,\quad N \text{ a basis},\quad H=LN,\quad H_A=LAN,\quad \omega=\operatorname{rank}H,
\]
\[
(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \operatorname{rank}(\lambda H-H_A)=\omega\ \ \forall\lambda\in\mathbb C .
\]
Each free row contributes \((h_i,g_i)=(r_iN,r_iAN)\in\mathcal T=\operatorname{row}[N\ AN]\), and conversely
every element of \(\mathcal T\) occurs; so the free data is an \(m\times d_0\) matrix \(\Phi\) with rows in
\(\mathcal T\), \(d_0=\dim\mathcal T\).

A *gadget* means a fixed triple \((A,C,L_0)\) together with decoding functions of the free parameters; it
expresses a relation if that relation holds at every feasible point.

**Two paradigms.** In the *first*, the source problem's variables are placed in the free rows \(R\), and the
gadget must force relations among them. In the *second*, the variables are placed in the instance data
\((A,C,L_0)\) and the free rows are only a witness; the encoding is then an *existential* statement
\(\exists R\) about the instance.

---

## Part II. Results

### II.1 The first paradigm is impossible (any decoding degree)

> **Theorem A.** Fix \((A,C,L_0)\) (with compatible fixed rows) and a layer \(\omega\). If a polynomial \(q\)
> in the free parameters vanishes at every feasible point, then for every \(\omega\)-piece \(W\) that the
> feasible set meets, \(q\) vanishes identically on the linear space
> \(M_W=\{R:h_i\in W,\ g_i\in W\}\).

*Proof.* On \(M_W\), the exact-rank condition \(\operatorname{rank}H=\omega\) is open (its complement is
determinantal), \((5b)\) is open (the bad locus is closed), and on the exact-rank set \((5a)\) is automatic.
So the feasible set is Zariski open in the irreducible affine space \(M_W\), hence dense whenever non-empty;
\(q\) vanishes on it, hence on \(M_W\). \(\square\)

So no relation-forcing gadget exists — in particular no multiplication gate — **regardless of the decoding
degree**. The affine-linear version of this statement was proved earlier in this correspondence; the
argument above shows the degree plays no role, because only the openness of the feasible set is used.

### II.2 Why the first paradigm could never work

In a reduction the source variables belong in the instance data; the free rows are the witness. Theorem A says
precisely that the witness side can only ever provide *non-emptiness*, never a relation. This also explains a
long series of failed local gadget constructions: the variables were in the wrong place.

### II.3 The second paradigm: what does work

A single block ("literal gate"), with \(C_i=[0\,0\,1]\), \(A_i(t)=\begin{pmatrix}0&0&0\\ t&0&0\\0&1&0\end{pmatrix}\),
\(L_{0,i}=[1\,0\,0]\), has
\[
H\text{'s column}=(1;u),\qquad H_A\text{'s column}=t\,(0;v),
\]
(\(u,v\) free), and is feasible **iff \(t\ne0\)**. The anchor (the fixed row) is what makes the \(H\)-column
non-zero for every choice of free data.

**Negation is free.** The gate reads "some affine function of the variables is non-zero"; since the reduction
computes the instance data itself, it may feed the complementary affine function. For a Boolean source variable,
\(t\mapsto 1-x\) gives \(\neg x\).

**Conjunction works.** Take the block-diagonal direct sum: \(C\) *stacked* block-diagonally (not concatenated —
concatenation couples \(K_0\) and destroys everything), \(A\) block diagonal, \(L_0\) concatenated. Then:

> **Structural lemma.** \(H\)'s \(i\)-th column is \((1;u_i)\) and \(H_A\)'s is \(t_i(0;v_i)\); in particular if
> some \(t_i=0\), that \(H_A\) column vanishes while the corresponding \(H\) column stays anchored.

> **Two-block soundness.** For two blocks and \(m=2\): if \(t_1=0\) then the sum is infeasible.
> *Proof:* with \(H=\begin{pmatrix}1&1\\a&b\\c&d\end{pmatrix}\), \(H_A=\begin{pmatrix}0&0\\0&e\\0&f\end{pmatrix}\),
> \((5b)\) at \(\lambda=0\) forces \(\omega=1\); then \(\operatorname{rank}H=1\) forces \(a=b\), \(c=d\); then the
> proportionality of the two pencil columns for \(\lambda\ne0\) forces \(e=f=0\); but then \(P(0)=0\), contradicting
> \((5b)\). \(\square\)

Exhaustively, over all \((a,b,c,d,e,f)\in\{-2,\dots,2\}^6\) satisfying the rank requirements (600 cases), no
feasible point exists. For three blocks all eight patterns of \((t_1,t_2,t_3)\) were tested, and feasibility
matches "all \(t_i\ne0\)" in every case (with two different values of \(m\)). The general \(k\) is a conjecture:
the natural strategy reduces to comparing the rank of the "difference" pencil \(D(\lambda)\) at \(\lambda=0\)
and at \(\lambda=\infty\).

### II.4 What fails

**Disjunction.** Two attempts fail.

- *Removing the anchor* (so that the free data can zero a block) does not produce a gate reading \(t=0\); it
  produces a **vacuous** gate, feasible for every \(t\), because with a single column \((5b)\) only asks the
  column to be non-zero for every \(\lambda\), which any non-zero data achieves.
- *Layer separation*, i.e. asking different layers to encode different disjuncts, was tested on the natural
  two-column template with parameters \(t_1=x\), \(t_2=1-x\). Layer \(1\) turns out to be non-empty exactly when
  \(t_1t_2\ne0\), i.e. \(x\notin\{0,1\}\) — again an **open** condition, not an equation.

### II.5 The fundamental limitation

Combining II.1 and II.4: every condition this architecture can express appears to be an **open** condition in the
instance parameters (a complement of a closed set), or a disjunction of such. But a finite system of open
conditions over an algebraically closed field is always satisfiable, since finitely many non-zero polynomials can
always be made simultaneously non-zero. Consequently a reduction built only from literals, conjunction and
disjunction cannot be hard.

Equations (for instance a Booleanity condition \(x(1-x)=0\), or the totality of a gate) would have to come from
somewhere. Theorem A rules them out on the witness side. On the instance side the only sources we have identified
are structural: the value of \(\dim K_0\), the layer \(\omega\), and the rank identities coming from \(\lambda=0\).

### II.6 Summary

| item | status |
|---|---|
| relation-forcing gadget (any degree) | **impossible** (Theorem A) |
| literal gate ("affine \(\ne0\)") | works |
| negation | free (parameter substitution) |
| conjunction (anchored direct sum) | proved for 2 blocks; verified for 3; conjecture for \(k\) |
| disjunction | not achieved (two failures) |
| equations | **no source identified** |

---

## Part III. Questions

**Q1.** Is Theorem A correct as stated? The step I would most like checked is that the feasible set is Zariski
open in each piece \(M_W\) — in particular that \((5a)\) is automatic on the exact-rank locus, which is what makes
the piece irreducible and the density argument work.

**Q2.** Is the two-block soundness argument correct, and is its \(k\)-block generalisation plausible as stated
(comparing the difference-pencil rank at \(0\) and \(\infty\))? If the general statement is false, a counterexample
would be valuable: it would mean that conjunction itself is unsound in this architecture.

**Q3.** Is the "open conditions only" limitation a theorem? Concretely: is there a precise sense in which a
reduction whose instances are parameterised by \((A,C,L_0)\) and whose acceptance is "the layer problem is
feasible" can only express constructible conditions — and if so, does that preclude NP-hardness?

**Q4.** Where could equations come from? We see only structural sources (the dimension of the compression, the
layer, the \(\lambda=0\) rank identity). Is there a mechanism we are missing, or is this architecture provably
unable to encode an equation?

**Q5.** If the limitation is real, is the right conclusion that the gadget route to hardness should be abandoned —
and if so, is the architecture-level negative result itself worth writing up (it would say that a whole family of
reduction strategies cannot work, rather than that the problem is easy)?

### Reliability

| item | label |
|---|---|
| Theorem A | proved (degree-free) |
| literal gate, negation by substitution | proved |
| two-block soundness | proved, plus exhaustive check (600 cases) |
| three-block patterns | exact verification, 8/8 patterns, two values of \(m\) |
| \(k\)-block conjunction | **conjecture** with a proof strategy |
| disjunction, equations | **not achieved** |
