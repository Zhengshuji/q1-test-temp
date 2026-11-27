# Workstream B — consolidated report (2 November 2026, evening)

**Status:** this supersedes and extends `REPORT_2026-11-02_WORKSTREAM_B_EN.md`.
That earlier report contained an error (§5, "constant rank $\Rightarrow$ zero right minimal indices"),
which you correctly refuted. The error is retracted (registered as **R18** in `proof/refuted/`), and the
corrected theory produced a *different* and, we think, cleaner result: a genuine theorem about observer
pencils, plus one surviving conjecture with a quantitative form.

Everything below is exact rational arithmetic. All scripts are in the repository.

---

## 0. What changed since the last report

| item | status |
|---|---|
| §5 of the previous report ("$(5b)\Rightarrow$ right indices $=0$") | **WITHDRAWN** (R18; your counterexample $[\lambda\;1]$) |
| correct global identity | stated and **verified 103/103** |
| new theorem **B.6**: $(5a)\Rightarrow$ right minimal indices $=0$ | **[proved (paper)] + [verified 150/150]** |
| normalization question (your Q4) | **answered**: original $\to$ quotient is a *compression*, not an equivalence |
| feasible sample | **103 pencils**, $n=6,7,8$, $\rho$ from $0$ to $5$ |
| new quantitative observation | $d_\infty = h-\operatorname{rank}L$ in **103/103** samples (general pencils only satisfy $\ge$) |
| remaining conjecture | **T4-b** (all infinite elementary divisors of degree 1); T4-c collapses into it |

---

## 1. Toolbox (all exact)

| file | what |
|---|---|
| `tools/verification/kronecker_pencil.py` | Kronecker data: normal rank, finite/infinite elementary divisors, left/right minimal indices (degree-truncated linear algebra; adaptive stopping) |
| `tools/verification/observer_pencils.py` | builds the **actual** observer pencil $Q_L(\lambda)=[\lambda L-LA;CA;C]$ from an instance and a candidate $\mathcal V$; $(5a)/(5b)$ verdicts; cross-check |
| `tools/verification/kron_struct_scan.py` | five-step programme |
| `tools/verification/modJ_candidates.py` | candidates satisfying only $(5a)$ (invariance modulo $\mathcal J$) |
| `tools/verification/kron_known_instances.py` | analyses the known-feasible $(\rho,c)=(3,1)$ instance |
| `tools/verification/kron_sweep.py` | multi-instance / multi-$n$ sweep |
| `tools/verification/kron_dinfty_stats.py` | statistics of $d_\infty$, $\sum\varepsilon$, $\operatorname{rank}L$ on feasible pencils |
| `tools/verification/kron_identity_probe.py` | records why a naive proxy for $\sum\deg\gamma_k$ fails |
| `tools/verification/kron_layer_relation.py` | original vs quotient pencil: rank identity + Kronecker comparison |
| `proof/kron_null_module/` | theorem B.6 + `verify.py` (150 pencils) |

Every pencil is cross-checked against an independent path (determinant degree when regular and square,
sampled ranks otherwise). Standard blocks $L_k$, $L_\eta$, $J_k(\alpha)$, zero blocks are recovered
exactly.

---

## 2. Retraction and the corrected identity

Your counterexample $Q(\lambda)=[\lambda\;\;1]$: rank $1$ everywhere, right nullspace
$\operatorname{span}\{(1,-\lambda)^{\mathsf T}\}$ moving with $\lambda$, right minimal index $1$.

What we now state instead:

* constant rank $\iff$ no finite elementary divisors (regular part only);
* global identity (your (1)): $\sum_i\eta_i+\sum_j\varepsilon_j+\sum_k\deg\gamma_k=r$,
  which in the $(5b)$ case becomes $\sum\eta+\sum\varepsilon+d_\infty=h$.

We verified the $(5b)$ form on **103/103** feasible pencils.
We also found and recorded that the naive proxy
$\sum\deg\gamma_k\ne\sum\deg(\text{finite})+\sum\deg(\text{reversed})$ (counterexamples give $7\ne5$, $6\ne4$).

---

## 3. New theorem B.6: $(5a)$ forces every right minimal index to be $0$

**Statement.** Let $L$ satisfy $(5a)$, i.e. $\operatorname{row}(LA)\subseteq\operatorname{row}(L;CA;C)$.
Then every polynomial right null vector $v(\lambda)=\sum_{k\le d}\lambda^kv_k$ of
$$Q_L(\lambda)=\begin{bmatrix}\lambda L-LA\\ CA\\ C\end{bmatrix}$$
has all coefficients in the constant nullspace $N=\{w:Lw=0,\ LAw=0,\ Cw=0,\ CAw=0\}$.
Hence the right null module is $N\otimes\mathbb C[\lambda]$, and all right minimal indices of $Q_L$ are $0$.

**Proof.** Expand $Q_L(\lambda)v(\lambda)\equiv0$ in powers of $\lambda$:
$LA\,v_0=0$; $L\,v_k=LA\,v_{k+1}$ for $0\le k\le d$ (with $v_{d+1}=0$), so $L\,v_d=0$; and
$C\,v_k=CA\,v_k=0$ for all $k$. Thus $v_d$ satisfies $Lv_d=Cv_d=CAv_d=0$, and by
$(5a')$ every row of $LA$ is a combination of rows of $L,CA,C$, hence $LA\,v_d=0$.
So $v_d\in N$; subtracting $\lambda^dv_d$ (also a null vector) and inducting on $d$ gives the claim. ∎

**Notes.**
* $(5b)$ is not used — the statement holds for **infeasible** pencils too.
* It does not conflict with your counterexample: that is a general pencil, whereas $Q_L$ has the
  $CA,C$ blocks and satisfies $(5a')$.
* Verification: 150 pencils (50 each for $n=6,7,8$) with $(5a)$, all with $\eta$ identically $0$.

We are aware this is a *consequence of $(5a)$*, not a deep observer-specific theorem; we are stating it
because it settles one of the three open items in the target form T, and because it says the **only**
remaining freedom is on the left/infinite side.

---

## 4. Normalization (your Q4): compression, not equivalence

We built both pencils and compared them:

$$\operatorname{rank}Q_L(\lambda)=j+\operatorname{rank}Q_{\rm quot}(\lambda)\qquad\text{for all }\lambda
\quad(17\text{ rational }\lambda,\ 2\text{ instances};\ j=\dim\mathcal J),$$

so the quotient kills exactly the $\mathcal J$-part. But the Kronecker data differ:

| instance | pencil | shape | rank | $\eta$ | $\varepsilon$ | finite |
|---|---|---|---|---|---|---|
| seed 1002 | original | $6\times6$ | 4 | $[0,0]$ | $[1,0]$ | $[0,0,0,3]$ |
| | quotient | $4\times5$ | 3 | $[1,0]$ | $[0]$ | $[0,0,2]$ |
| seed 1010 | original | $6\times6$ | 5 | $[0]$ | $[4]$ | all zero |
| | quotient | $4\times4$ | 3 | $[3]$ | $[0]$ | all zero |

A left index $4$ becomes a *right* index $3$. By your trichotomy this is a **compression**, so Kronecker
invariants may not be transferred, and the structural statement must be formulated on the **original**
$Q_L$. (We also checked your remark: $\operatorname{rank}Q_1=\rho$ alone does not exclude infinite
divisors; the correct criterion is $\operatorname{rank}Q_1=\operatorname{nrank}$.)

---

## 5. Feasible samples: 103 pencils, $n=6,7,8$

Two families were used:

* **constructive**: the *observability chain* $L_k=[C;CA;\dots;CA^{k-1}]$. **Claim:** it always satisfies
  $(5b)$. *Proof:* the rows of $\lambda L-LA$ are $\lambda CA^i-CA^{i+1}$, hence lie in
  $\operatorname{row}(L;CA;C)$ (giving $\le h$); for $\lambda\ne0$ they span the same space as
  $\{CA^i-\lambda^{-1}CA^{i+1}\}$, from which $CA^i$ ($i<k$) can be recovered, giving $\ge h$;
  at $\lambda=0$ the rows are $-CA^{i+1}$ together with $CA,C$, again spanning $h$. ∎
  (This is a paper-level lemma; 101 instances verify it.)
* **search**: invariant closures and their mod-$\mathcal J$ lifts, filtered by an exact $(5a)$ test.

Statistics over the 103 feasible pencils:

| check | result |
|---|---|
| $\sum\eta+\sum\varepsilon+d_\infty=h$ | 103/103 |
| $\sum\eta=0$ (B.6) | 103/103 |
| $d_\infty=0\iff\operatorname{rank}L=h$ | 103/103 |
| $d_\infty=h-\operatorname{rank}L$ | **103/103** |

The last line is the new observation. For a general pencil one only has
$d_\infty\ge h-\operatorname{rank}Q_1$, with $Q_1=[L;0;0]$ here. Equality in all samples means:

> **every infinite elementary divisor of an observer pencil has degree $1$.**

Equivalently $\ker L=N$. **This is a conjecture**, not a proof (the missing step is an analysis of the
Kronecker chains on $\ker Q_1=\ker L$).

**Consequence.** By B.6, $\sum\varepsilon=h-d_\infty$, so the "left lower bound" conjecture is not
independent: everything reduces to the single statement $d_\infty=h-\operatorname{rank}L$.

---

## 6. Questions

**Q1.** Is "$d_\infty=h-\operatorname{rank}L$" (equivalently: all infinite elementary divisors have
degree $1$, equivalently $\ker L=N$) a known structural property of functional-observer pencils? It is a
sharp statement and our search found no exception in 103 cases.

**Q2.** Is our proof of B.6 the standard argument, or is there a cleaner canonical-form proof
(the result suggests that for observer pencils all the "singular freedom" sits on the left)?

**Q3.** Is the "observability chain $[C;CA;\dots;CA^{k-1}]$ always feasible" lemma in the literature?
It is elementary but explains why feasible pencils are abundant at large $q$.

**Q4.** How would you attack T4-b? Our plan is to analyse $\ker Q_1=\ker L$: an infinite divisor of degree
$\ge2$ would require a vector $w\in\ker L$ with $Q_0w\notin \operatorname{im}$-structure of a chain
$w, w', \dots$. Is there a standard "no Jordan block at infinity" criterion for such block pencils that
we should apply?

**Q5.** Given B.6 and the compression result, would you now reformulate the target form T purely in terms
of $(\{\varepsilon_j\}, d_\infty)$ with $d_\infty=h-\operatorname{rank}L$ as a stated conjecture?
Or do you prefer that we first try to *disprove* T4-b by constructing an observer pencil with a degree-2
infinite divisor?

---

## 7. Limits

* 103 feasible pencils, $n\le8$; the candidate families are still far from all of $\mathfrak F_{\rho,c}$;
* T4-b is evidence only (103/103);
* B.6 is proved on paper, verified on 150 pencils; no Lean yet (we would formalise only if it becomes
  load-bearing for $q1$);
* the compression result is verified on two instances (rank identity over 17 values of $\lambda$),
  not proved in general — though the argument
  $\operatorname{row}(Q_L)=\mathcal J\oplus\pi(\operatorname{row}Q_L)$ is a one-line proof we have not yet
  written down formally.

---

## 8. File pointers

* `proof/kron_null_module/` — theorem B.6 (README, theorem.md, verify.py)
* `proof/refuted/README.md` — R18 (the retracted claim + your counterexample)
* `workspace/kronecker/` — README (results), TARGET_FORM_T.md (provisional target form),
  attempts/01 (running log), data/*.tsv (raw data)
* `docs/02_theorems_proven.md` — B.6 registered
* `docs/05_open_questions.md` — Workstream B section
