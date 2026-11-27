# Stratification results, a refuted conjecture, and a control experiment

This note reports the outcome of the stratification programme we took up on your suggestion, one conjecture that was
refuted by experiment and structurally explained, and a control experiment on whether the subspace constraints are
what bias the problem toward failure. It ends with questions, including one specifically about how to attack the
constrained-subpencil problem.

Levels: **L1** paper proof; **L2** exact arithmetic; **L3** Lean (machine-checked).

---

# Part I. Setting

$A$, $C$ ($p$ rows), $L_0$ ($r$ rows), with $\operatorname{rank}[C;L_0]=p+r$, both pairs observable. A candidate
$\mathcal L$ ($q$ rows) satisfies $\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$ and
$\operatorname{rank}[C;\mathcal L]=p+q$; $h=\operatorname{rank}[\mathcal L;CA;C]$; conditions $(5a)$, $(5b)$ as usual.
$V=\ker[C;CA]$, $K=\ker[C;L_0]$, $\mathcal Z=\ker[C;\mathcal L]$, $d=n-p-q$.

For an admissible $\mathcal Z$ put
$$S:=V\cap\mathcal Z,\qquad s=\dim S,\qquad
J_{\mathcal Z}:V\to X/\mathcal Z,\ x\mapsto x+\mathcal Z,\qquad
T_{\mathcal Z}:V\to X/\mathcal Z,\ x\mapsto Ax+\mathcal Z,$$
$$N_{\mathcal Z}(\lambda)=T_{\mathcal Z}-\lambda J_{\mathcal Z}.$$

---

# Part II. Results

## 1. The failure criterion, in three equivalent forms (L1; L2; you independently derived the first)

$$(5b)\ \text{fails at}\ \mathcal Z
\iff\exists x\in V\setminus\mathcal Z,\ \lambda:\ (\lambda I-A)x\in\mathcal Z
\iff\exists x:\ J_{\mathcal Z}x\ne0,\ T_{\mathcal Z}x=\lambda J_{\mathcal Z}x .$$
Equivalently, with $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$, $\ker E=\mathcal LV$:
$(5b)\iff(E,\Lambda)$ observable.

**One instance worth recording.** There is an admissible $\mathcal Z$ (with $n=6$, $p=r=2$, $d=2$, $s=1$) for which
$\operatorname{rank}N_{\mathcal Z}(\lambda)=1<\dim V=2$ for **every** sampled $\lambda$ ($0,\pm1,\pm2,3$), yet
$(5b)$ **holds**. This is exactly the situation you warned about: "not full column rank" is not failure, because the
kernel may sit inside $S$. Consequence: on strata with $s>0$ only the kernel criterion is valid, never the
full-column-rank criterion.

## 2. Stratification by $\operatorname{rank}(J_{\mathcal Z}|_V)$ (L1; L2 on the $s=0$ stratum, 402/402)

Since $\ker J_{\mathcal Z}=S$, one has $\operatorname{rank}(J_{\mathcal Z}|_V)=\dim V-s$; stratifying by this rank is
stratifying by $s\in\{0,\dots,\min(d,\dim V)\}$ — the same parameter as the $O(n)$ disjunction in our encodings.
The strata are admissible in a very restricted way:

**(a)** if $s=\dim V$ (i.e. $V\subseteq\mathcal Z$) then $\mathcal Z$ is spectrally feasible (there is no
$x\in V\setminus\mathcal Z$);
**(b)** if $s=0$ then failure $\iff\exists\lambda:\operatorname{rank}N_{\mathcal Z}(\lambda)<\dim V\iff$ the maximal
minors of $N_{\mathcal Z}$ have a common root;
**(c)** in general, failure $\iff\exists\lambda:\ker N_{\mathcal Z}(\lambda)\not\subseteq S$.

Moreover **(5a) forces** $A(S)\subseteq\mathcal Z$: from $\mathcal LA=T[\mathcal L;CA;C]$, any $x\in S$ has
$\mathcal Lx=Cx=CAx=0$, hence $\mathcal L(Ax)=0$ and $Ax\in\ker[C;\mathcal L]=\mathcal Z$. If in addition
$A(S)\subseteq S$ then $S$ would be an $A$-invariant subspace inside $\ker C$, contradicting observability of
$(C,A)$; so on middle strata $S$ is necessarily a generalised-eigenvector direction.

## 3. A conjecture that we refuted, and why it had to fail

We conjectured that middle strata ($s>0$) never fail, which would have collapsed the three criteria into the
$s=0$ pencil test. **It is false.** The structural reason is visible in the observability form: failure means that
$U=\mathcal LV$ contains a nonzero eigenvector of $\Lambda$, while
$$s=\dim V-\dim U.$$
So $s$ constrains only the *dimension* of $U$, whereas failure depends on the *position* of $U$ relative to the
eigenvectors of $\Lambda$. There is no implication between the two, and indeed an explicit instance exists with
$s=1$, $q=1$, $(5a)$ satisfied and $(5b)$ violated (then $U=\mathbb C^q$ necessarily contains eigenvectors).

Consequence: the $s$-stratification is useful for bookkeeping (the encoding disjunction, admissibility pruning) but
**does not simplify the spectral condition**. Anything that collapses the criterion has to be done in the
$(E,\Lambda)$ picture.

## 4. A control experiment: do the constraints bias the problem toward failure?

Same matrix $A$, same dimensions $(d_V,d_K,d)$; per-candidate failure rate on the $s=0$ stratum, computed exactly by
the gcd test:

| group | samples | failing | rate |
|---|---|---|---|
| structured: $V=\ker[C;CA]$, $K=\ker[C;L_0]$ | 537 | 360 | **67.0%** |
| random: $V,K$ random subspaces of the same dimensions | 873 | 216 | **24.7%** |

So the constraints do bias the problem toward failure (by a factor of about 2.7), which is consistent with the view
that hardness, if any, is most naturally encoded through the structured side. But the random case still fails a
quarter of the time: "the unconstrained problem is classically decidable" (Kronecker) is a statement about
*decidability*, not about the failure *rate*, and the two must not be conflated.

## 5. Two whole-family counterexamples, and unbounded gaps

* $n=6$, $p=r=2$, $q_0=3$: every admissible augmentation of order three fails, gap 1, $q_{\min}=4$;
* the same parameters, designed: order two is a Type I (dimension) failure, order three is whole-family spectral
  (the gcd of the relevant maximal minors is $\lambda+2$, monic and independent of the chart parameter, so there is
  no drop locus), order four has an explicit witness — gap 2;
* $k$ identical copies of the second example: $q_{\min}$ and the gap are multiplied by $k$, because the copies share
  the same certificate value $\lambda_0$ (so the sum satisfies the single-$\lambda$ certificate at the same
  $\lambda_0$). Hence the gap is unbounded. The two abstract steps (avoidance lemma, rank additivity of direct
  sums) are machine-checked; the block bookkeeping is paper.

Coverage: the charts we use are the $\binom{k}{d}$ standard coordinate charts, whose union is the whole
$\operatorname{Gr}(d,K)$, and the computations are symbolic in the chart parameters over $\mathbb Q(\theta)[\lambda]$,
not sampled — so the two whole-family claims are exhaustive over the Grassmannian.

---

# Part III. Questions

**Q1 (the stratification programme).** We have completed your steps 1 and 2 and shown that step 3 cannot be done in
the way we hoped (no stratum is automatically feasible except the top one, and middle strata can fail). Do you
regard the stratification as finished, or is there a different stratification (not by $s$, but by the position of
$U=\mathcal LV$ relative to the eigenstructure of $\Lambda$) that could still collapse the criterion?

**Q2 (attacking the constrained subpencil problem — this is the question we most need).** The decision problem now
has the form: does there exist $\mathcal Z\le K$ of dimension $d$ such that
$\Pi_{\mathcal Z}(\lambda I-A)B_V$ has full column rank over $\mathbb C[\lambda]$? We know that the unconstrained
version is classical (Kronecker). **How would you attack the constrained version?** Specifically:
(i) is there a known polynomial algorithm for "constrained deflation" with fixed $V$ and a kernel restricted to a
fixed subspace $K$, or is this known to be hard in the matrix-pencil literature?
(ii) would you look for a reduction *from* our problem to a known hard problem, or *to* our problem from one?
(iii) is there a small instance class (say $p=r=1$ with $n$ growing, or $A$ in companion form) where the
constrained problem degenerates to something already classified?

**Q3 (are we over-structuring?).** We now have eight structural results and two counterexamples but no complexity
statement. Is the balance right, or would you stop the structural work here and invest entirely in the complexity
side? If the latter, which single formulation would you fix as the target?

**Q4 (the control experiment).** The structured case fails at 67% and the random case at 25%. Does that ratio carry
any information for you about where a gadget should bite, or is it an artefact of our particular sampling of
dimensions?

**Q5 (the counterexample in item 1).** The instance where the pencil is permanently rank deficient yet feasible is,
we believe, the cleanest illustration of your (T*) warning. Would you want it as a lemma in the paper (a
"rank-deficiency is not failure" proposition), or is it better as a remark?
