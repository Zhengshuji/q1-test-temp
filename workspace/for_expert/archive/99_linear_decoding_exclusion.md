# A complete exclusion result for gadget encodings: linear decoding cannot simulate multiplication

This note reports three results on the "gadget" programme for the hardness question, and asks whether the
last one is airtight and how far it extends. Throughout, a *gadget* means a fixed triple \((A,C,L_0)\) with
free rows \(R\), together with decoding functions \((x,y,z)\) of the free parameters; it *expresses
multiplication* if \(z=xy\) at every feasible point.

---

## Part I. Setting and definitions

Let \(A\in\mathbb Q^{n\times n}\), \(C\in\mathbb Q^{p\times n}\) of rank \(p\), \(L_0\in\mathbb Q^{r_0\times n}\),
\(\mathcal L=[L_0;R]\) with \(R\) the \(m\times n\) free rows, and

\[
K_0=\ker[C;CA],\quad k=\dim K_0,\quad N \text{ a basis},\quad H=LN,\quad H_A=LAN,\quad \omega=\operatorname{rank}H,
\]
\[
(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \operatorname{rank}(\lambda H-H_A)=\omega\ \ \forall\lambda\in\mathbb C .
\]

Each free row contributes \((h_i,g_i)=(r_iN,\,r_iAN)\in\mathcal T=\operatorname{row}[N\ AN]\); conversely every
element of \(\mathcal T\) occurs. We call \(R\) *feasible* if \((5a)\) and \((5b)\) hold.

Two facts used below (proved earlier in this correspondence): [the \((5b)\)-failure locus is closed, and the
compressed rank is bounded by the fixed data through \(\lambda=0\).] For self-containedness:

- **(B1)** \(\{(5b)\ \text{fails}\}\) is a closed subset of the parameter space (homogenise the pencil and
  project from the proper scheme over \(\mathbb P^1\); there are no bad points at infinity once
  \(\operatorname{rank}H=\omega\) is fixed).
- **(B2)** \((5a)\wedge(5b)\Rightarrow\operatorname{rank}H=\operatorname{rank}H_A\le\dim(AK_0)\).

---

## Part II. Results

### II.1 The stratum is a union of linear pieces over a Grassmannian

Fix \(\omega\). For each \(\omega\)-dimensional subspace \(W\subseteq\mathbb C^k\) containing \(\operatorname{row}H_0\)
put
\[
M_W=\{R:\ h_i\in W,\ g_i\in W\}\qquad(\text{a linear subspace of the parameter space}).
\]
Then
\[
\{R:\operatorname{rank}H=\omega\}=\bigcup_{W\in\mathrm{Gr}(\omega,k)}M_W ,
\]
and on \(M_W\cap\{\operatorname{rank}H=\omega\}\) we have \(\operatorname{row}H=W\supseteq\{g_i\}\), so **\((5a)\)
holds automatically**. Hence, writing \(\mathcal F\) for the feasible set,
\[
\mathcal F\cap M_W=\{\operatorname{rank}H=\omega\}\cap\{(5b)\}\cap M_W
\]
is a **Zariski-open** subset of \(M_W\): the first factor is open inside \(M_W\) (its complement is the closed
determinantal set \(\operatorname{rank}H\le\omega-1\)) and the second is open by (B1).

### II.2 The candidate linearity principle: true for one free row, false from two

The question raised previously was whether \(\mathcal F\), restricted to a rank stratum, is Zariski dense in a
*linear* subspace.

**One free row (\(m=1\)).** Let \(r=\operatorname{rank}H_0\). Then
- \(\omega=r\): \(\mathcal F=\{h,g\in\operatorname{row}H_0\}\cap(5b)\) — Zariski open in the linear space
  \((\operatorname{row}H_0)^2\);
- \(\omega>r\): \(\mathcal F=\varnothing\). Indeed \((5a)\) forces \(g=\alpha h+w\) with \(w\in\operatorname{row}H_0\),
  and then \(\alpha h-g=-w\in\operatorname{row}H_0\), so \(\operatorname{rank}P(\alpha)\le r<r+1\).

So the principle holds for \(m=1\), with the common root of the maximal minors **equal to** \(\alpha\)
(verified exactly on an explicit instance: the gcd of the minors is \(\lambda-\alpha\)).

**Two free rows (\(m=2\)).** It fails. Take \(k=3\), \(r_0=1\), \(m=2\), \(\omega=2\), so \(H\) is \(3\times3\) and
\(\operatorname{rank}H=2\) is the condition \(\det H=0\) — an irreducible cubic hypersurface. Two feasible points
(exact rationals, both with \(\gcd\) of minors \(=1\), and with *different* compressed row spaces) are
\[
H_p=\begin{pmatrix}1&0&0\\-1&-1&-1\\-1&-1&-1\end{pmatrix},\qquad
H_q=\begin{pmatrix}1&0&0\\-1&-1&0\\-1&0&0\end{pmatrix},
\]
and their midpoint satisfies \(\det H_m=\tfrac14\ne0\). Since a linear subspace containing both points must
contain the midpoint, **no linear space can contain the feasible set**; in particular the "closure is linear"
form of the principle is false. No irreducibility hypothesis is needed: if the closure were a linear space
\(L\), then \(L\subseteq\{\operatorname{rank}H=\omega\}\) (closed), yet the midpoint lies in \(L\) and has rank
\(\omega+1\) — contradiction.

The correct statement is a dichotomy: the feasible set is linear-open exactly when the **compressed row space
is locked** — which happens in the pinned regime and in the bottom layer — and otherwise the stratum is a
non-linear union over a Grassmannian.

### II.3 The exclusion theorem (linear decoding)

> **Theorem.** Assume (i) the fixed rows are compatible, \(\operatorname{row}H_{A,0}\subseteq\operatorname{row}H_0\);
> (ii) the decoding functions \(x,y,z\) are **affine-linear** in the free parameters; (iii) the feasible set is
> non-empty and \(z=xy\) at every feasible point. Then for every \(W\) with \(\mathcal F\cap M_W\ne\varnothing\),
> either \(x|_{M_W}\) or \(y|_{M_W}\) is **constant**; hence on that piece \(z=xy\) degenerates to a linear
> relation, and no non-trivial multiplication is expressed.

*Proof.* By II.1, \(\mathcal F\cap M_W\) is Zariski open in the irreducible affine space \(M_W\); being non-empty it
is Zariski dense. The polynomial \(z-xy\) vanishes on it, hence on \(M_W\). On the affine space \(M_W\) the three
restrictions are affine-linear; comparing quadratic parts in
\(z|_{M_W}=(x|_{M_W})(y|_{M_W})\) gives \(\dot x\cdot\dot y=0\), and the polynomial ring is a domain, so
\(\dot x=0\) or \(\dot y=0\). \(\square\)

Two consequences:

1. The earlier "pinned" exclusion is the special case in which only one piece \(W_0\) occurs, and the
   one-row result is the case \(m=1,\ \omega=r\).
2. The affine-rank-minimisation translation is excluded as well: in that reduction the encoded variables are
   *entries of a matrix*, i.e. affine-linear functions of the free parameters, so a gadget expressing
   \(z=xy\) there would contradict the theorem. In particular the requirement of encoding
   "\(\operatorname{rank}\Phi\le 3\)" by the two rank conditions cannot be met by a linear decoding.

### II.4 What the theorem does not cover

Only affine-linear decoding. If \(x,y,z\) are polynomials of degree \(d\ge2\), then \(z-xy\) has degree \(2d\);
step II.1 and the density argument still give "\(z-xy\) vanishes on \(M_W\)", but the last step (comparing
quadratic parts) has no analogue: a degree-\(2d\) polynomial can vanish on an affine space for structural
reasons. So nonlinear decoding is the remaining opening.

---

## Part III. Questions

**Q1.** Is the exclusion theorem correct as stated? The two steps I would most like checked are (a) that
\((5a)\) is automatic on \(M_W\cap\{\operatorname{rank}H=\omega\}\), so that the feasible set is genuinely
open in the piece (this is the step that makes the density argument apply), and (b) the degeneration step at
the end.

**Q2.** For nonlinear decoding, is there a degree obstruction? Concretely: the union \(\bigcup_W M_W\) is the
determinantal variety \(\{\operatorname{rank}H\le\omega\}\), whose ideal is generated by the
\((\omega+1)\)-minors. A polynomial of degree \(2d\) can of course lie in that ideal. Is there nonetheless a
reason (e.g. a factorisation or a "rank of the multiplication tensor" argument) that forces degeneracy for
all \(d\)?

**Q3.** If the theorem stands, is the conclusion correct that hardness for this model cannot be obtained by
gadget encodings, and that a reduction must either abandon the common row-space discipline (per-row common
\(\mathcal T\)) or use a decoding that is not polynomial in the free parameters?

**Q4.** Which alternative architecture would you consider most promising for a hardness proof — nonlinear
decoding, a different compressed object, or a problem-to-problem reduction that avoids gates altogether?

**Q5.** Does the same argument say anything about the *algorithmic* side — e.g. does the Grassmannian
decomposition of II.1 give a better algorithm for the layer decision than the generic-gcd test?

### Reliability

| item | label |
|---|---|
| (B1), (B2) | proved (previous reports) |
| II.1 Grassmannian decomposition; \((5a)\) automatic on the piece | proved |
| II.2 \(m=1\) dichotomy | proved, and checked exactly (common root \(=\alpha\)) |
| II.2 \(m=2\) counterexample | exact rational certificate (two feasible points, midpoint of rank \(\omega+1\)) |
| II.3 exclusion theorem (linear decoding) | proved; covers pinned, \(m=1\), and all strata |
| nonlinear decoding | **not covered** — the only gap |
