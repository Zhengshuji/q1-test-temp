# Workstream B — first results: Kronecker structure of observer-induced pencils

> ## ⚠️ CORRECTION (added 2026-11-02, after your review)
>
> **Section 5 of this report is wrong and is hereby withdrawn.** Constant rank does **not** imply that
> all right minimal indices vanish — your counterexample $Q(\lambda)=[\lambda\;1]$ is decisive:
> rank is $1$ everywhere, yet the right nullspace $\operatorname{span}\{(1,-\lambda)^{\mathsf T}\}$
> moves with $\lambda$, so the right minimal index is $1$.
>
> What survives:
> * constant rank $\iff$ **no finite elementary divisors** (a statement about the regular part only);
> * the global identity $\sum_i\eta_i+\sum_j\varepsilon_j+\sum_k\deg\gamma_k=r$
>   ($\gamma_k$ homogeneous invariant factors), which in the $(5b)$ case becomes
>   $\sum\eta+\sum\varepsilon+d_\infty=r$ — **checked on every feasible sample we have** ($0+4+1=5$,
>   $0+6+0=6$, $0+4+1=5$);
> * a warning for ourselves: $\sum\deg\gamma_k$ is **not** $\sum\deg(\text{finite})+\sum\deg(\text{reversed})$;
>   we exhibited pencils where that proxy gives $7$ instead of $5$ (script `kron_identity_probe.py`).
>
> The refutation is registered as **R18** in `proof/refuted/README.md`, with the certificate script
> `tools/verification/kron_identity_probe.py`. The rest of this report (toolbox, experiments, data)
> stands unchanged; only §5 and the two consequences drawn from it are withdrawn.
> The revised target form T is in `workspace/kronecker/TARGET_FORM_T.md`.

**Date:** 2026-11-02
**Follows:** our report of 2026-11-02 on Workstream A, and your review of the same day.
**Scope:** we built the Kronecker toolbox you asked for, ran the five-step programme, and collected
feasible samples at $\rho\ge1$. One observation is a *proof*, the rest is evidence.

Everything below is exact rational arithmetic. All scripts are in the repository and run in seconds
on $n=6$.

---

## 1. What we built

| file | what it does |
|---|---|
| `tools/verification/kronecker_pencil.py` | Kronecker data of a pencil $\lambda P_1+P_0$: normal rank, finite/infinite elementary divisors, left/right minimal indices |
| `tools/verification/observer_pencils.py` | builds the **actual** observer pencil $Q_L(\lambda)=[\lambda L-LA;\,CA;\,C]$ from an instance and a candidate $\mathcal V$; returns $(5a)/(5b)$ verdicts and a cross-check |
| `tools/verification/kron_struct_scan.py` | the five-step programme, with two candidate families |
| `tools/verification/modJ_candidates.py` | candidates that only satisfy $(5a)$ (invariance modulo $\mathcal J$), not full $A$-invariance |
| `tools/verification/kron_known_instances.py` | analyses a **known-feasible** instance (the $(\rho,c)=(3,1)$ one from `proof/rho1_layer/verify_mu1_good_instance.py`) |
| `tools/verification/kron_sweep.py` | multi-instance sweep collecting feasible pencils |

**Minimal indices** are computed by degree-truncated linear algebra (no polynomial arithmetic):
with $n_d=\dim\{\text{null vectors of degree}\le d\}$ one has $\#\{\eta_i=d\}=k_d-k_{d-1}$ where
$k_d=n_d-n_{d-1}$; the left indices are obtained on the transposed pencil. My first version had this
formula reversed; the standard-block test $L_2$ caught it immediately.

**Self-tests.** Standard blocks $L_2$, $L_1^{\mathsf T}$, $J_2(0)$, $L_1\oplus 0$, a constant
invertible pencil and $\lambda I_2$ are all recovered with the expected data, and every pencil is
cross-checked against an independent path (determinant degree when the pencil is regular and square,
sampled ranks otherwise). Every claim about a pencil is asserted against that cross-check.

---

## 2. Experiment 1 — five-step scan on four random instances

$n=6$, seeds $1002,1003,1015,1019$; candidate $\mathcal V$ from **(i)** $A$-invariant closures and
**(ii)** invariance modulo $\mathcal J$ (lifted, then filtered by an exact $(5a)$ test).

* 42 observer pencils; $(5a)$ holds for all of them by construction of the filter;
* $(5b)$ holds for **8**, and **all 8 are at $\rho=0$** (the "trivial" solutions, e.g. $L=C$);
* all 34 pencils with $\rho\ge1$ are infeasible;
* no pencil in the sample has only right singular blocks.

**A correction worth reporting.** An earlier run (before the $(5a)$ filter) showed two pencils with
$\rho=1$ satisfying $(5b)$, and we started to read that as "at fixed $\rho$ both feasible and
infeasible pencils occur". Those two pencils **violate $(5a)$** — they are not observer candidates at
all. After filtering they disappear. We record this because it is exactly the kind of false positive
the project has been bitten by before: the type statistics must be computed *after* the $(5a)$ filter.

---

## 3. Experiment 2 — a known-feasible instance

The $(\rho,c)=(3,1)$ instance of `proof/rho1_layer/verify_mu1_good_instance.py` with
$\mathcal V=\langle e_1,e_2,e_3,e_5\rangle$ ($q=4$) gives

| $q$ | $h$ | $(\rho,c)$ | $(5b)$ | finite | infinite | $\eta$ | $\varepsilon$ |
|---|---|---|---|---|---|---|---|
| 4 | 5 | $(3,1)$ | ✓ | $[0,0,0,0,0]$ | $[0,0,0,0,1]$ | $[0]$ | $[4]$ |

So a feasible pencil can have a **large left minimal index** ($\varepsilon=[4]$).

---

## 4. Experiment 3 — sweep for feasible samples

12 instances, 59 valid pencils, **4 feasible at $\rho\ge1$**:

| seed | $q$ | $(\rho,c)$ | $h$ | finite | $\eta$ | $\varepsilon$ |
|---|---|---|---|---|---|---|
| 1001 | 6 | $(4,2)$ | 6 | all zero | $\varnothing$ | $[5,1]$ |
| 1010 | 4 | $(3,1)$ | 5 | all zero | $[0]$ | $[4]$ |
| 1010 | 5 | $(3,2)$ | 5 | all zero | $[0]$ | $[4,1]$ |

---

## 5. ~~One observation that is a proof~~ **WITHDRAWN — see the correction block at the top**

> **$(5b)$ implies that all right minimal indices vanish.**

Indeed $(5b)$ says $\operatorname{rank}Q_L(\lambda)=h$ for every $\lambda$; hence the right null
space $\ker Q_L(\lambda)$ is a **constant** subspace of dimension $n-h$, so it has a constant basis
and every right minimal index is $0$. The same conclusion holds for any pencil of constant rank.

Two consequences:

1. the "restricted Kronecker structure" question is **trivial on the right** and non-trivial only on
   the **left** (left minimal indices and infinite elementary divisors);
2. it also explains the old, wrong phrasing "(5b) $\iff$ the pencil contains only right singular
   blocks" — constant rank forces right indices to $0$, but says nothing about the left side, and the
   samples indeed have $\varepsilon=[4]$, $[5,1]$, $[4,1]$.

**Question for you:** is this consequence standard in the pencil literature (it seems elementary),
and is there a known statement relating the **left** minimal indices of an observer pencil to
$(\rho,c,d)$? In all our samples the left indices are large ($4$ or $5$), which suggests some identity
such as "sum of left indices $=q+2p-h$" — we have not checked this yet.

---

## 6. Questions

**Q1.** Is the "right indices vanish" statement as trivial as we think, and does it appear in the
pencil-completion literature (Dodig 2008/2026, Verdier 2012)? We do not want to present a standard
fact as new.

**Q2.** Which invariant should we conjecture a restriction on? Our data suggests the **left** indices
and the **infinite** elementary divisors; the finite ones are already forced to be absent by $(5b)$.
Is there a natural candidate identity/inequality from the completion theory (e.g. an inequality
between $\varepsilon_i$, $q+2p-h$ and $n-h$) that we should test?

**Q3.** Our sample is $n=6$, $\rho\le4$, $c\le2$, and the candidate family is a small algebraic
subset of $\mathfrak F_{\rho,c}$ (invariant closures and their mod-$\mathcal J$ lifts). Is that enough
to formulate a conjecture, or should we first get samples at larger $n$ (with the risk that the
Kronecker computation stays fast but the instance search gets harder)?

**Q4.** In the layer coordinates the $\lambda$-coefficient has rank $\rho$ (so infinite elementary
divisors are absent *there*), but in the original $Q_L(\lambda)$ we do see infinite divisors
($[0,0,0,0,1]$). Which normalization should the structural statement be formulated in, so that it is
comparable with the RCP model in `proof/layer_program/RESTRICTED_COMPLETION_MODEL.md`?

**Q5.** Should we now write the "target form T" conjecture (finite inequalities on $\varepsilon$ and
the infinite divisors), given that we have only 6 feasible samples, or wait for more data?

---

## 7. Limits of this round

* samples: 6 feasible pencils, $n=6$; candidate family far from all of $\mathfrak F_{\rho,c}$;
* the scan's negative results ("no pencil with only right singular blocks") are statements about this
  sample only;
* the cross-check is exact for regular square pencils (determinant degree) and *sampled* otherwise
  (sampling can only refute);
* no Lean changes in this workstream (as you advised).

---

## 8. Pointers

* `workspace/kronecker/README.md` — direction index, all results of this note (Chinese);
* `workspace/kronecker/attempts/01_kronecker_structure.md` — running log in the project's attempt format;
* `workspace/kronecker/data/scan_2026-11-02.tsv`, `sweep_12seeds.tsv` — raw data;
* `proof/layer_program/RESTRICTED_COMPLETION_MODEL.md` — the RCP model and the "target form T" we want
  to instantiate;
* `literature/notes/DODIG_2008_row_completion.md`, `SURVEY_2026-10-28.md` — the completion theory we
  compare against.
