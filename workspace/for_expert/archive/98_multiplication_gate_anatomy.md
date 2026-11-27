# The anatomy of a multiplication gate: two locking mechanisms, one exclusion theorem

This note reports what we now know about *why* a sound multiplication gate has not been found, and
asks whether the resulting picture is correct and whether it should be pushed to a no-go theorem.
Everything below is about the compressed formulation; the characterisation itself is from the
literature and is not at issue.

---

## Part I. Setting

Fix rational \(A\in\mathbb Q^{n\times n}\), \(C\in\mathbb Q^{p\times n}\) of rank \(p\), and
\(L_0\in\mathbb Q^{r_0\times n}\). For a candidate \(q\) put \(\mathcal L=[L_0;R]\) with \(R\) the
\(m\times n\) free rows, and

\[
K_0=\ker[C;CA],\quad k=\dim K_0,\quad N \text{ a basis},\quad
H=LN,\quad H_A=LAN,\quad \omega=\operatorname{rank}H .
\]

The two conditions are

\[
(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H ,\qquad
(5b)\ \operatorname{rank}(\lambda H-H_A)=\omega\quad\forall\lambda\in\mathbb C .
\]

Each free row contributes a pair \((h_i,g_i)=(r_iN,\,r_iAN)\in\mathbb C^{2k}\), and the pairs range
exactly over
\[
\mathcal T=\operatorname{row}[N\ AN],\qquad d_0=\dim\mathcal T .
\]
So the free data is an \(m\times d_0\) matrix with rows in \(\mathcal T\); we call it \(\Phi\).

---

## Part II. What we can prove

### II.1 The \(\lambda=0\) bound

Because \(\lambda=0\) is one of the values in \((5b)\),

\[
(5a)\wedge(5b)\ \Longrightarrow\ \operatorname{rank}H=\operatorname{rank}H_A=\operatorname{rank}(LAN)\le\dim(A K_0).
\tag{1}
\]

This is purely linear-algebraic and does not involve the spectrum: it is an *upper* bound on the
rank stratum.

### II.2 Pinning

Let \(\omega_0=\operatorname{rank}H_0\) be the rank contributed by the fixed rows. By \((5a)\),
\(\operatorname{row}H\supseteq\operatorname{row}H_0\), so \(\operatorname{rank}H\ge\omega_0\); by (1),
\(\operatorname{rank}H\le\dim(A K_0)\). Hence:

> **Lemma 1 (pinning).** If \(\dim(A K_0)=\omega_0\), then every feasible \(R\) satisfies
> \(\operatorname{rank}H=\omega_0\) and \(\operatorname{row}H=\operatorname{row}H_0\).

We call such an instance *pinned*; the stratum and even the row space are forced.

### II.3 Pinned instances have linear expressive power

Let \(\mathcal F\) be the feasible set and \(\mathcal L=\{R:\text{each }(h_i,g_i)\in\mathcal T\cap(W_0\times W_0)\}\),
\(W_0=\operatorname{row}H_0\).

> **Theorem 2.** If the instance is pinned, then \(\mathcal F=\mathcal L\cap\mathcal O\), where
> \(\mathcal L\) is a linear subspace and \(\mathcal O\) is Zariski open (the complement of the closed
> bad locus of \((5b)\), see below). If \(\mathcal F\ne\varnothing\) then \(\mathcal F\) is Zariski dense
> in \(\mathcal L\); consequently every polynomial vanishing on \(\mathcal F\) vanishes on
> \(\mathcal L\) — i.e. the only relations a pinned instance can impose are consequences of linear
> ones.

The closedness of the bad locus used here is the projective-incidence argument: homogenising the
pencil and projecting from \(Y\times\mathbb P^1\), which is proper, with no bad points at infinity
because \(\operatorname{rank}H=\omega_0\) throughout.

**Consequence.** A pinned instance can force \(z=xy\) only degenerately (i.e. only when the linear
constraints already make the relation linear, e.g. one factor constant). "Force the intended rank
stratum" therefore cannot produce a multiplication gate — although it is an excellent device for
imposing affine constraints, which is exactly what the affine-rank-minimisation translation lacks.

### II.4 The maximality lemma

> **Lemma 3.** Let \(R\) be feasible with \(W=\operatorname{row}H\), and let \(R'\) be obtained from
> \(R\) by adding one free row \((h,g)\in\mathcal T\) with \(h\notin W\). Then \(R'\) is infeasible.

*Proof.* Suppose \((5a)\) holds for \(R'\). Then \(g\in\operatorname{row}H_A'\subseteq\operatorname{row}H'=W+\langle h\rangle\),
so \(g=\alpha h+w\) with \(w\in W\). At \(\lambda=\alpha\) the new pencil row is
\(\alpha h-g=-w\in W\), and every old pencil row already lies in \(W\) (feasibility of \(R\)).
Hence \(\operatorname{rank}P'(\alpha)\le\dim W=\omega<\omega+1=\operatorname{rank}H'\), violating
\((5b)\). \(\square\)

In words: **adding a row always manufactures a common root**, namely at the coefficient that expresses
the new output row in terms of the new row space. This is the "punishment of extra rows" that a
global gadget design needs, and it is built into \((5b)\) — it does not have to be designed.

### II.5 The escape taxonomy

Combining 1–3, the ways a witness can avoid a gadget's intended stratum are exactly:

| escape | possible? | mechanism |
|---|---|---|
| enlarge \(\operatorname{row}H\) | **no** | Lemma 3 |
| shrink to a lower stratum | yes | only the fixed rows bound the stratum from below |
| change the row space at the same dimension | no (once the lower bound is met) | \(W_0\subseteq W\), equal dimensions |

So the only real escape is *shrinking*. This re-diagnoses the earlier failure: the classical
multiplication construction was defeated by \(R=0\), which is a *shrink*, not an enlargement, and the
reason it is available is that its fixed rows have rank one while the intended witness has rank two.

### II.6 The affine-rank-minimisation side (for context)

The same compressed objects impose a hard limit on any translation from affine rank minimisation: all
columns of \([N\ AN]\) are annihilated by \(C\), so
\[
d_0=\operatorname{rank}[N\ AN]\le n-p .
\]
A faithful row-wise encoding of an \(m\times n\) carrier into the \(m\times d_0\) free data is therefore
impossible when \(p\ge1\). Worse, the only affine control over the free data is the pinning of the
first \(r_0\) rows by \(L_0\); general linear functionals of the free data cannot be imposed.

---

## Part III. Questions

**Q1.** Is Lemma 1 and Theorem 2 correct as stated? In particular, is the Zariski-density step
sound when \(\mathcal O\) is only *Zariski* open in \(\mathcal L\) and \(\mathcal F\) may be a proper
subset of the real points? We are using it only to rule out polynomial relations, not to claim
real-point existence.

**Q2.** Is Lemma 3 known? It seems to say that for a polynomial observer pencil, a feasible compressed
witness is *maximal*: it admits no extension by an independent free row. If this is standard, a
reference would let us cite it instead of proving it.

**Q3.** Granting 1–3, the only region in which a multiplication gate could live is
"not pinned, with the row space maximal". Is anything known about gate constructions there — or, on
the contrary, about a no-go?

**Q4.** Would you advise aiming at a no-go theorem — "in this architecture (row-wise common
\(\mathcal T\), the two rank conditions) no gadget can express multiplication" — rather than
continuing to search for a construction? If so, what is the weakest hypothesis under which such a
statement is provable and still meaningful for the hardness programme?

**Q5.** On the affine side: is the bound \(d_0\le n-p\) and the "only the fixed rows give affine
control" observation a known obstruction to translating affine rank minimisation into this model, or
is there a standard way around it that we are missing?

### Reliability

| item | label |
|---|---|
| \(\lambda=0\) bound (1), Lemma 1, Lemma 3 | proved |
| Theorem 2 (pinned ⟹ linear) | proved, conditional on the closedness of the bad locus |
| the escape taxonomy | proved as the combination of the three |
| \(d_0\le n-p\) | proved; checked on seven dimension patterns, all with equality |
| "no multiplication gate exists" | **not proved**; the region of II.5 is still open |
