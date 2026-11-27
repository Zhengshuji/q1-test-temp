# The $q_0$ audit: what our code actually computes, and the corrected $q_{\rm geom}$

This note answers the two mathematical points you raised, reports an audit of the $q_0$ implementation you offered to
examine (the code is reproduced verbatim below), and records the corrected definition of $q_{\rm geom}$.

---

# Part I. The corrected $q_{\rm geom}$ (your point 2)

You are right: with $\rho=1$ there is no intermediate stratum, so $q_{\rm geom}$ cannot be $4$. The definition we are
now using:

* $q_{\rm geom}$ — the least subterminal order ($q+p<n$) at which an admissible candidate with $1\le\delta<\rho$
  exists; **equal to $+\infty$ when $\rho=1$**;
* $q_{\rm spec}$ — the least subterminal order at which such a candidate also satisfies $(5b)$;
* $q_{\min}$ — the least order over **all** $q$, terminal included.

With that, the controlled table becomes

| $C$ | profile | $q_0$ | $r_1$ | $\rho$ | $q_{\rm geom}$ | $q_{\rm spec}$ | $q_{\min}$ |
|---|---|---|---|---|---|---|---|
| $C_{33}$ | $(2,2)$ | 2 | 4 | 2 | 3 | 3 | 3 |
| $C_{42}$ | $(2,1,1)$ | 2 | 4 | 2 | 3 | 3 | 3 |
| $C_{24}$ | $(2,1,1)$ | 2 | 4 | 2 | 3 | 3 | 3 |
| $C_{51}$ | $(1,1,1,1)$ | 3 | 3 | 1 | $+\infty$ | $+\infty$ | 4 $=n-p$ |

So the $\rho=1$ row is now consistent: no intermediate stratum, terminal order only.

---

# Part II. Your §1.1: $q_0\le n-p$ is a lemma

We agree, and we have adopted exactly your reading: the algorithm counts a vector only when it is independent modulo
$R=\operatorname{row}C$ together with everything previously accepted; then every accepted vector is a new independent
direction in $\mathbb C^{1\times n}/R$, whose dimension is $n-p$. Hence $q_0\le n-p$ by dimension count, and we no
longer carry it as a hypothesis. (Our implementation does quotient by $R$ implicitly, because the rows of $C$ are
loaded first into the "kept" list.)

---

# Part III. The audit you offered to examine

## 3.1 The implementation, verbatim

```
def eta_and_q0(A, C, L0):
    n = len(A)
    gens = [list(r) for r in C] + [list(r) for r in L0]   # rows of C first, then rows of L0
    kept, alive = [], [True] * len(gens)
    eta = [0] * len(gens)
    for q in range(n):                    # q = power of A
        for i, g in enumerate(gens):      # each generator still alive
            if not alive[i]:
                continue
            v = g
            for _ in range(q):
                v = matvec(v, A)          # v = g·A^q
            if rank(kept + [v]) > len(kept):
                kept.append(v); eta[i] += 1
            else:
                alive[i] = False          # this generator is switched off permanently
    return sum(eta[len(C):])              # q0 = sum over the rows of L0
```

So $q_0$ is the sum, over the rows of $L_0$, of the number of accepted vectors, where **a row is switched off at its
first dependent power and never re-examined**.

## 3.2 Three questions, three experiments

**(a) Invariance.** Replacing $L_0$ by $ML_0$ with $M$ invertible: $q_0$ unchanged in **1176/1176** trials.
Permuting the rows of $L_0$: unchanged in **242/242**. So the value does not depend on the basis of $\operatorname{row}L_0$
in these samples, despite the row-by-row processing.

**(b) Does early stopping lose directions?** We searched for the configuration you describe (a dependent
$\ell_iA^k$ whose successor $\ell_iA^{k+1}$ would have been independent of the current span): it occurs in **2 of 489**
instances. So the mechanism is real but rare; whether it changes the value is a separate question.

**(c) Is it the minimal admissible order?** Let $q_{\rm adm}$ be the least order at which an admissible
$\mathcal L$ exists (scanned per chart with several parameter values). Comparing:

| variant | difference to $q_{\rm adm}$ |
|---|---|
| **A** (current implementation, stop the row at first dependence) | $0$: 285, $-1$: **108** (never positive) |
| **B** (no early stop; scan all powers) | $+1$: 263, $+2$: 130 |
| **C** (global greedy over all $(\ell_iA^k)$ by increasing $k$) | identical to B, 393/393 |

So: the current implementation is a **lower bound** (it never exceeds $q_{\rm adm}$), variants B and C always
**overshoot**, and B = C exactly (so dropping the per-row stopping rule makes the value order-independent).

**Caveat we want on the record**: $q_{\rm adm}$ is computed by chart sampling, so it may itself be overestimated when
the admissible set is thin inside a chart. Under that caveat, the honest summary is: *we do not know whether the
current $q_0$ equals the intended algebraic minimum, but we know it is a lower bound for the sampled $q_{\rm adm}$ and
that the two natural repairs overshoot.*

---

# Part IV. Questions

**Q1 (which object is $q_0$?).** Given the code above, is the intended functional-observability index for row $i$ equal
to the number of accepted vectors under rule A, or under rule B/C? In particular: in the literature's construction, is a
row abandoned at its first dependent power, or is the index defined as the maximal $k$ such that $\ell_i,\dots,\ell_iA^{k}$
are independent modulo the previously collected span (which is a maximum, not a greedy count)?

**Q2 (if A is wrong, what is the repair?).** If the intended object is neither A nor B/C, would you state the
definition you would use — for instance via the Kronecker form of $(C,A,L_0)$, or as
$\sum_j \dim(\mathcal K_j/\mathcal K_{j-1})$ for the filtration $\mathcal K_j=\operatorname{row}L_0+\operatorname{row}L_0A+\dots$?

**Q3 (does the gap depend on this?).** If $q_0$ changes by $+1$ in 28% of instances, our reported gaps
$q_{\min}-q_0$ shift correspondingly. Would you then prefer that we report the gap as $q_{\min}-q_{\rm adm}$ (a
definition-free quantity) and treat $q_0$ as a separate, defined object?

**Q4 (the Lemma $q_0\le n-p$).** We have adopted your dimension argument. Should it be stated as a lemma in the paper
with the exact quotient interpretation, and does the same argument give $q_0\ge$ (number of rows of $L_0$), i.e. is
$r\le q_0\le n-p$ the sharp range?

---

# Part V. What else changed

1. the checklist now includes the three-way $\delta$ identity and the metamorphic test (row-basis change); it passes on
   1003 candidates and 877 metamorphic pairs;
2. the two-stage pipeline (geometric filter first) is in place: 3400 spectral tests become 1905, and no discarded
   candidate is feasible;
3. we re-ran the controlled experiment with the corrected $q_{\rm geom}$; the conclusion that the profile does not move
   $q_{\min}$ in this family is unchanged;
4. the Lean side now has six more declarations (`logic`, `necessary`, `no_intermediate`, `terminal_only`,
   `dim_quotient`, `dim_arith`), all labelled `[Lean-conditional]`.
