# Machine-checked kernels, the two-stage pipeline, and three questions about method

This note reports what has been machine-checked since the last exchange, records the two-stage pipeline you
recommended, and asks three things: your view of the open problems, your view of our experimental methodology, and
whether anything in the current picture is being stated too strongly.

---

# Part I. What is now machine-checked, and what is not

## 1. New Lean declarations (compiled with zero errors and zero warnings)

| declaration | content |
|---|---|
| `logic`, `necessary` (in `B31`) | if $\delta\le\rho$ and both extreme strata ($\delta=\rho$, $\delta=0$) are infeasible, then feasibility forces $1\le\delta<\rho$ |
| `no_intermediate` (in `B32`) | for $\rho\le1$ there is no integer $\delta$ with $1\le\delta<\rho$ |
| `terminal_only` (in `B32`) | if every subterminal order is infeasible and the terminal order is feasible, then the minimum feasible order is the terminal one (`IsLeast`) |
| `dim_quotient` (in `B33`) | $\dim(V/S)=\dim V-\dim S$ |
| `dim_arith` (in `B33`) | from $\dim V=n-r_1$, $\dim S=n-h$, $h=q+p+\delta$, $r_1=p+\rho$ one gets $\dim V-\dim S=q+\delta-\rho$ |

So the **logical and arithmetic skeleton** of B.31–B.33 is machine-checked, and the statements are labelled
**[Lean-conditional]** rather than **[Lean]**: the entry point in each case is a hypothesis standing for a
row-space/annihilator argument that is still paper (for instance "$\delta=0$ implies infeasibility", which rests on
$A\mathcal V\subseteq\mathcal V$ plus observability). Your earlier convention is what we are following here.

Cumulatively the project has 189 Lean declarations in 70 files, 178 registered statements, no discrepancy in the two
audit scripts, and no `sorry`.

## 2. What stays paper, and why

| item | why it is not machine-checked |
|---|---|
| B.22 (equality obstruction) | needs the explicit block factorization $Q=P(\lambda)H_0$ at the matrix level and the rank identity $\operatorname{rank}(PH)=\operatorname{rank}H-\dim(\ker P\cap\operatorname{im}H)$; the latter is machine-checked, the matrix instantiation is not |
| B.28(3) (invariance plus observability) | the row-space/annihilator translation; the Krylov containment and the $\mathcal V=\top$ step are machine-checked |
| B.30, B.34, B.35 | these are exact-verification statements (finite samples), not theorems |

## 3. The two-stage pipeline you asked for

Implemented: for every candidate, compute $h$ and $\dim\mathcal V$ (two rank computations), form
$\delta=h-\dim\mathcal V$, keep only $1\le\delta<\rho$ (or the terminal branch $q+p\ge n$), and only then run the
spectral test. On 599 instances and 3400 admissible candidates:

* spectral tests drop from 3400 to **1905 (56.0%)**;
* **no candidate discarded by the filter is feasible** (0 counterexamples, so the filter is sound on this sample);
* the feasible counts agree before and after (1905 = 1905).

## 4. Rank-growth profile versus gap (your §8.2 direction), preliminary

With $\Delta_k=\operatorname{rank}[C;\dots;CA^k]-\operatorname{rank}[C;\dots;CA^{k-1}]$ and $\rho=2$:

| profile | $n$ | samples | mean gap $q_{\min}-q_0$ |
|---|---|---|---|
| $(2,2)$ | 6 | 766 | 1.00 (always 1) |
| $(2,2,1)$ | 7 | 733 | 1.50 (1 or 2) |

The profile and $n$ vary together here, so we do not read a conclusion from it yet.

## 5. Corrections and bugs, recorded

* our $\delta$ was computed as $\dim(\operatorname{row}(CA)\cap\mathcal V)$ — the intersection dimension, not the
  stratum parameter. With the correct $\delta=h-(q+p)$ the strata table changes labels (the earlier "$\delta=0$"
  column was in fact the equality stratum), and the intermediate stratum is **1107/1107 feasible**;
* the rank-growth profile was first computed as $\operatorname{rank}[C;CA^k]$, missing the intermediate powers;
* an earlier "top-stratum" construction placed $V$ inside a subspace that was not a kernel, so its samples were not
  what we thought.

All three are now fixed and recorded in the development log.

---

# Part II. Questions about the three open points

**Q1 (bounded gap).** We conjecture: for $\rho=2$ the gap is at most 2 (745 instances agree), and in general the gap
is bounded by a function of $\rho$ alone. Is that the right form of the conjecture, or should the bound involve the
whole profile $(\Delta_k)$ rather than only $\Delta_1=\rho$? And would you expect the bound to be linear in $\rho$?

**Q2 ($\Delta$-profile, controlled).** To test whether the profile matters beyond $\rho$, we plan to fix $n$, $p$, $r$
and $\rho$ and vary only the profile (e.g. $(2,2)$ versus $(2,1,1)$ at $n=6$ with $p=r=1$). Is that the right
controlled experiment, and is there a canonical family where the profile can be prescribed independently of the rest
of the data — for instance $A$ block-diagonal with prescribed cyclic blocks?

**Q3 (the complexity question, $q1$).** With the structural picture now fairly complete (two boundary strata excluded
by proof, feasibility confined to the intermediate stratum, $p=1$ fully classified), what would you now regard as the
sharpest form of the complexity question? Our own best formulation is: given $(C,A,L_0)$ and a target order $q$, decide
whether the intermediate stratum contains a point whose reduced pencil is pointwise injective. We do not know whether to
attack this directly or to look for a restricted family where it becomes a known problem.

---

# Part III. Questions about method

**M1 (sampling versus symbolic).** Our scans enumerate the $\binom{k}{d}$ standard charts of the Grassmannian and, inside
each chart, sample the chart parameter $\theta$ at a few values plus random ones. Exact arithmetic is used throughout,
and every verdict is cross-checked against an independent criterion (observability form versus maximal-minor gcd).
Is chart sampling acceptable for statements we label **[Exact verification]**, or should every scan be symbolic in
$\theta$ (that is, compute the gcd over $\mathbb Q(\theta)[\lambda]$)? The cost difference is large, and the earlier
whole-family arguments were symbolic.

**M2 (which checks should be mandatory).** After three bugs of the same shape — a quantity that looked right but was a
different invariant — we now print and assert, before any conclusion: the ranks that define $h$, the dimension of
$\mathcal V$, the stratum parameter $\delta$, the identity $\ker B=V$, and that the constructed subspace really is a
kernel. Is there a checklist you would add for this kind of geometry-plus-spectrum computation?

**M3 (how much evidence is enough for a conjecture).** Our empirical statements currently rest on $10^3$–$10^4$
instances. Given that several of these quantities live on thin sets, would you advise a different standard — for
instance, insisting that every conjecture be accompanied by either a proof or a family with a parameter?

---

# Part IV. Anything else we should be saying

Two things we want to flag rather than bury:

1. the terminal-order claim ($q_{\min}\le n-p$) is used twice above (in B.32 and in the pipeline's terminal branch);
   it is proved only under $(C,A)$ observable plus $\operatorname{rank}[C;L_0]=p+r$, and we would like that hypothesis
   set to be the canonical one in the paper;
2. the equality obstruction B.22 is what makes the boundary stratum die, and B.28(3) is what makes the other boundary
   die; both are proved, but both are used far more often than they are stated, so they deserve to be stated as
   standalone lemmas early in the paper.
