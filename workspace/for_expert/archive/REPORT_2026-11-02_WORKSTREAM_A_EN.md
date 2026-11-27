# Workstream A: first experimental results — and a question about the direction

**Date:** 2026-11-02
**Follows:** our report of 2026-11-01 (`REPORT_2026-11-01_EN.md`) and your review of the same day.
**Scope of this note:** we executed the first steps of your **Workstream A** (the minimal-rank layer
$\rho=\rho_{ci}$). The outcome is negative in a precise, checkable sense. We would like your view on
whether the reduction should be re-parameterized or abandoned in favour of **Workstream B**
(Kronecker structure of the intermediate layer).

Everything below is exact rational arithmetic; both scripts are in the repository and reproduce
with one command.

---

## 1. What we did

1. **Read the two SOF papers** (as advised): Liu, arXiv:2610.00390 (∃ℝ-completeness, effective gain
   dimension, bit bounds) and Löfberg, arXiv:2609.16886 (NP-hardness via Betweenness, the universal
   cubic with Routh determinant $Nuv-1$). Notes are in `literature/notes/`.
   The construction we found most transferable is Liu §4.1:
   $\det\begin{pmatrix}s^q+a&b\\-1&s^q-a\end{pmatrix}=s^{2q}+b-a^2$, which puts **equation residuals
   into coefficients** of a characteristic polynomial.

2. **Built the quotient machinery for the minimal layer.** For an instance $(A,C,L_0)$ we compute,
   in exact rational arithmetic, the quotient $X=\mathbb C^n/\mathcal J$ with $\mathcal J=\operatorname{row}[C;CA]$,
   together with $T$ (the action of $A$ on $X$), $B=\pi(\mathcal J A)$ and $U_0=\pi(\operatorname{row}L_0)$.
   Then $P=\rho_{ci}$ is computed by a closure iteration $U\mapsto U+TU+B$ starting from $U_0$.
   Script: `tools/verification/min_layer_closure.py`.

3. **Set up the chart comparison** you asked about: in a chart $I$ ($|I|=\rho$), every $\rho$-dimensional
   $U$ is $G(\Theta)=[I_\rho;\Theta]$; we compare
   * $A_{\rm lin}=\{\Theta: U_0\subseteq\operatorname{im}G(\Theta)\}$ — linear equations, and
   * $A_{\rm full}=A_{\rm lin}\cap\{\Theta: TU\subseteq U+B\}$ — plus the determinantal condition.
   Script: `tools/verification/layer_min_affine.py`, plus a search driver
   `tools/verification/find_layer_instance.py`.

---

## 2. Results

### 2.1 The closure algorithm agrees with the recursion (4/4), after a convention fix

On four instances (including the project's `R17`, the "second" example and a chain system) the closure
value equals the recursive $P$ of the existing implementation. One *apparent* mismatch turned out to be
a **row-vs-column convention** difference between the two implementations: the existing `P_alg` acts
by $x\mapsto xA$ (row convention), our $T$ acts by matrix-vector product. Transposing makes them agree.
This is recorded in the scripts so that future cross-checks do not repeat the error.

### 2.2 The chart comparison is degenerate on the instances we first tried

On the three real instances with $d\le 4$ and $\rho_{ci}\le 2$ and $\dim U_0=1$, the linear set
$A_{\rm lin}$ is **zero-dimensional**: $U_0\subseteq U$ already pins $U$ down in the chart. No information.

### 2.3 On synthetic data, and then on real data, the determinantal condition is **not** implied

* Synthetic data ($d=4$, $\rho=3$, $B=0$, $U_0=\operatorname{span}\{e_0\}$, $T:e_0\mapsto e_1\mapsto e_2\mapsto0$):
  $A_{\rm lin}$ is $2$-dimensional, and we exhibit **exact rational points** $\Theta$ that satisfy
  $U_0\subseteq U$ but violate $TU\subseteq U+B$ (the cleanest is $\Theta=0$ in charts $(0,1,3)$ and
  $(0,2,3)$).
* **Real instances.** Searching $n=6$, $p=1$, $C=e_0^{\mathsf T}$, $L_0=e_1^{\mathsf T}$ over $400$
  integer matrices, $227$ instances satisfy $2\le\rho_{ci}\le d-1$ (so $A_{\rm lin}$ can be
  positive-dimensional). Two of them give the same phenomenon with exact certificates:
  * `seed=1002`: $d=5$, $\rho_{ci}=4$, $\dim B=1$; charts $(0,1,2,3)$ and $(0,1,2,4)$ have
    $3$-dimensional $A_{\rm lin}$, and $\Theta=0$ violates $TU\subseteq U+B$;
  * `seed=1003`: $d=4$, $\rho_{ci}=2$, $\dim B=2$; chart $(0,1)$ has $2$-dimensional $A_{\rm lin}$,
    and $\Theta=0$ violates the same condition.

**Interpretation.** In the chart coordinates, $\mathcal A_{\min}$ is the intersection of a linear set with
a determinantal variety, and the intersection is a *proper* subset. So the natural hope that
$\mathcal A_{\min}$ is affine (or Zariski-open in an affine space) **fails**.

### 2.4 The feasible $U$ on the minimal layer is **not unique**

This was the surprise. On `seed=1002` ($d=5$, $\rho_{ci}=4$), in the chart $(0,1,3,4)$ we enumerated
small integer coefficients and found **three distinct** rational points $\Theta$ that all satisfy
$TU\subseteq U+B$ (they differ only in the last entry, taking values $-1,0,1$); the same happens in
chart $(0,2,3,4)$. Hence:

* the minimal layer carries a **positive-dimensional family** of feasible $U$;
* the existential quantifier at the minimal layer **cannot be eliminated trivially**;
* consequently $\mathcal A_{\min}$ is a positive-dimensional determinantal variety — not a point, not
  affine.

---

## 3. What this does to the "minimal-rank-layer reduction"

The candidate theorem from your review was:

$$\mathrm{DEC}_{\rho_{ci}}(q)\iff\exists x\in\mathcal A_{\min}:F(x)\ne0
\quad\Longrightarrow\quad
\mathrm{DEC}_{\rho_{ci}}(q)\iff F|_{\mathcal A_{\min}}\not\equiv0 .$$

Our experiments show that the *implication* is not available through the route you suggested, because:

1. $\mathcal A_{\min}$ is not affine (2.3);
2. $\mathcal A_{\min}$ is not a point, so the $F(x)\ne0$ condition is not evaluated at a single
   candidate (2.4).

The implication would still hold if $F$ restricted to the variety were "generically nonzero" — but that
needs an argument on the variety (and, as you noted, even then the resulting test is a PIT-type problem,
not automatically polynomial time).

**We did not refute the theorem; we refuted the natural way of establishing its hypothesis.**

---

## 4. Questions

**Q4.1** Given 2.3–2.4, is the minimal-rank-layer reduction still the right first target? Or is the
non-uniqueness of $U$ on that layer a well-known phenomenon that already tells us the layer carries a
genuine existential quantifier (in which case the reduction buys less than hoped)?

**Q4.2** Should we (a) try a different parameterization — e.g. parameterize the admissible $U$'s through
the lattice of $T$-invariant subspaces so that $TU\subseteq U+B$ becomes an identity in the new
coordinates — or (b) move to **Workstream B** (Kronecker canonical form / minimal indices for
$0<\rho<d$)? Our inclination is (b), since (a) has no guarantee of removing the determinantal condition.

**Q4.3** Is there a known result on "generic feasibility on a determinantal variety" that applies here —
i.e. a criterion under which a nonvanishing condition $F\ne0$ is generic on
$\{\operatorname{rank}\ \text{conditions}\}$? If such a criterion exists, the minimal layer might still be
reducible to PIT.

**Q4.4** For the hardness route (Workstream C): our reading of Liu §4.1 is that the "residuals into
coefficients" construction works when the target condition is a *coefficient-level* condition. In the
square case ($q=t$) our $(5b)$ is exactly "all non-leading coefficients of $\det[U\mid P(\lambda)]$ vanish
and the constant term does not". Is that the right place to attempt the encoding, or do you see an
obstruction that makes it hopeless?

---

## 5. Limits of what we claim

* The scripts are exact (rational arithmetic), but the *interpretation* above is ours; we are not claiming
  any theorem about the layer.
* 2.3 uses $\Theta=0$, i.e. the coordinate subspace of the chart; 2.4 uses enumeration over
  $\{-1,0,1\}^{\dim\ker}$; the three points found do not prove that the solution set has dimension exactly
  one, only that it is **not** a point.
* The "synthetic" example in 2.3 is not claimed to come from an $(A,C,L_0)$ instance; the real-instance
  certificates in 2.3–2.4 are the ones that matter.

---

## 6. Pointers

| file | what |
|---|---|
| `tools/verification/min_layer_closure.py` | quotient data $(T,B,U_0)$, closure algorithm, cross-check with the recursive $P$ |
| `tools/verification/layer_min_affine.py` | chart comparison $A_{\rm lin}$ vs $A_{\rm full}$, prints exact counterexamples |
| `tools/verification/find_layer_instance.py` | search for real instances with $2\le\rho_{ci}\le d-1$ and run the comparison |
| `workspace/q1_false/attempts/10_minimal_rank_layer.md` | full log (Chinese): derivation, three experiments, state table |
| `literature/notes/LIU_2026_SOF_EXISTS_R.md`, `LOFBERG_2026_SOF_NP_HARD.md` | reading notes |
| `docs/05_open_questions.md` §Q1 | the open problem with your four points incorporated |
