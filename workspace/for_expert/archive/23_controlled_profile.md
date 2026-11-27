# Controlled experiment on the profile, the mandatory checklist, and the definition of $q_0$

This note answers the points you raised: the canonical $\delta$, the reconciliation of the counts, the checklist
implemented, the controlled experiment for $\rho=2$ that you asked for, and the precise definition of $q_0$.

---

# Part I. The definition of $q_0$ (your question before Q1 can be assessed)

We use the functional observability indices of $(L_0,A)$ with respect to $(C,A)$: starting from the rows of $L_0$, take
them in order and, for each row $\ell_i$, count how many consecutive vectors
$$\ell_i,\ \ell_iA,\ \ell_iA^2,\ \dots$$
are linearly independent modulo the span of everything already collected; the process stops for a row as soon as it
fails to add a new direction. Then
$$q_0=\sum_{i=1}^{r}\eta_i,$$
where $\eta_i$ is the count for the $i$-th row of $L_0$. This is the algebraic minimum order, and it is what our code
computes (`eta_and_q0`). For the terminal-only theorem the relevant comparison is $q_0\le n-p$; in the controlled
experiment below $q_0$ is $2$ or $3$, while $n-p=4$.

---

# Part II. What we fixed after your report

1. **Canonical $\delta$.**
$$\delta\;=\;h-(q+p)\;=\;\dim\operatorname{row}(CA)-\dim\bigl(\operatorname{row}(CA)\cap\mathcal V\bigr),
\qquad 0\le\delta\le\rho:=r_1-p,$$
and the quotient-pencil size is $(p+q)\times(q+\delta-\rho)$ (your B.33). Earlier scans computed the *intersection*
dimension instead; all tables in this note use the canonical definition, and every candidate is now checked against the
three-way identity.
2. **Terminal branch kept separate**: the geometric filter never uses "$\delta$ allowed" at $q+p=n$; the terminal branch
is tested directly.
3. **Counts reconciled.** The earlier numbers measured different things: 1905 was both the number of geometrically
allowed candidates and the number of feasible ones — and these coincide because *in that sample no geometrically allowed
candidate was spectrally rejected* (see the controlled experiment below, where again $q_{\rm geom}=q_{\rm spec}$).
The 745 and 766 figures come from two different scans (the first filtered $r_1=p+2$ across $p\in\{2,3\}$; the second
used $p=2$ only).
4. **B.22 and B.28(3)** are now stated as standalone lemmas and referenced from every later result, as you recommended.

---

# Part III. The checklist (your §7), implemented and run

For every candidate we now assert, in order: input ranks; admissibility ($\operatorname{rank}[C;\mathcal L]=p+q$ and
$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$); the geometric dimensions ($\dim V=n-r_1$,
$\dim\mathcal Z=n-p-q$, $\dim\mathcal V=p+q$); that the constructed subspace really is the kernel; that
$\ker B=V$ for the row basis $B$ of $\operatorname{row}[CA;C]$; the **three-way equality for $\delta$** and
$0\le\delta\le\rho$; $(5a)$ as a row-space inclusion; the quotient-pencil dimensions; and a **metamorphic test**
(replacing the row basis of $\mathcal L$ by an invertible combination must not change the $(5a)$ verdict).

Result: **1003 candidates, all checks pass**; metamorphic test agrees in **877/877** cases.

This checklist immediately caught two of the three bugs we reported earlier, so it stays.

---

# Part IV. The controlled experiment you asked for

Fixed $A=\operatorname{diag}(1,\dots,6)$ (distinct spectrum), fixed $L_0$, $n=6$, $p=2$, and only $C$ varies: its two
rows are supported on disjoint coordinate sets, so the observability indices are $(\mu_1,\mu_2)$ and
$\Delta_k=\#\{i:\mu_i\ge k+1\}$:

| $C$ | supports | $\Delta$ profile | $q_0$ | $r_1$ | $\rho$ | $q_{\rm geom}$ | $q_{\rm spec}$ | $q_{\min}$ |
|---|---|---|---|---|---|---|---|---|
| $C_{33}$ | $(3,3)$ | $(2,2)$ | 2 | 4 | 2 | 3 | 3 | **3** |
| $C_{42}$ | $(4,2)$ | $(2,1,1)$ | 2 | 4 | 2 | 3 | 3 | **3** |
| $C_{24}$ | $(2,4)$ | $(2,1,1)$ | 2 | 4 | 2 | 3 | 3 | **3** |
| $C_{51}$ | $(5,1)$ | $(1,1,1,1)$ | 3 | 3 | **1** | 4 | 4 | **4 $=n-p$** |

Here $q_{\rm geom}$ is the first order at which an admissible intermediate-$\delta$ candidate exists, and $q_{\rm spec}$
the first order at which one of those also satisfies $(5b)$.

Three readings:

1. with $n,p,r,\rho$ fixed and only the profile changed, $q_{\min}$ is **the same** — in this family the gap depends on
   $\rho$ alone, not on the later part of the profile. This is evidence for conjecture (A) and against the
   profile-dependent variants;
2. the $\rho=1$ case reproduces $q_{\min}=n-p$, an independent confirmation of the terminal-only theorem in a controlled
   family;
3. in all four cases $q_{\rm geom}=q_{\rm spec}$: **the spectral stage never rejects a geometrically allowed candidate**,
   so in the decomposition $q_{\min}-q_0=(q_{\rm geom}-q_0)+(q_{\rm spec}-q_{\rm geom})$ the second term vanishes here.

---

# Part V. Questions

**Q1 (the conjecture's form, now testable).** Given Part IV, we would state: *for fixed $(p,r,\rho)$ the gap
$q_{\min}-q_0$ is bounded by a function of $\rho$ alone*. Is that the form you would test, or would you keep the
profile in the statement and treat Part IV as evidence that the profile is irrelevant *in this family only*?

**Q2 (extending the family).** We can extend Part IV in two directions: (i) more splits within the diagonal family
(e.g. supports $(2,2,2)$ with $p=3$, which changes $\Delta_1$ and hence $\rho$); (ii) non-diagonal $A$ with prescribed
observability indices built from block-cyclic pieces. Which would you regard as the more informative extension?

**Q3 (terminal case and $q_0$).** With the definition in Part I, is the terminal-only theorem's hypothesis
$q_0\le n-p$ automatic, or should it be stated? In our families it always holds, but we have not proved it in general.

**Q4 (the sharpest complexity statement).** Now that the geometric and spectral stages separate cleanly in the
experiments, would you formulate the decision problem as "does $\mathfrak S_{q,1}\cup\cdots\cup\mathfrak S_{q,\rho-1}$
contain a point with pointwise-injective reduced pencil", and treat the geometric existence question as a separate
(pre-)problem worth its own complexity statement?

**Q5 (labels).** We now use: `[Lean]`, `[Lean-conditional]`, `[Paper proof]`, `[Exact finite enumeration]`,
`[Finite chart-sample verification]`, `[Empirical regularity]`. Is that the set you would standardise on?
