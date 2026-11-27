# Per-order decision: what worked, what broke, and two questions on formulation

This note is self-contained. It reports the last stage of work on the per-order decision problem, including two
failed attempts and one structural finding, and asks for advice on formulation.

---

# Part I. Setting (recall)

For $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$ with
$\operatorname{rank}[C;L_0]=p+r$ and a $q\times n$ matrix $\mathcal L$ whose row space contains $\operatorname{row}L_0$:

$$(5a)\ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\quad\forall\lambda .$$

$V=\ker[C;CA]$, $K=\ker[C;L_0]$, $\mathcal Z=\ker[C;\mathcal L]$ with $\dim\mathcal Z=d=n-p-q$,
$W=\operatorname{row}[C;CA]$, $r_1=\dim W$, and for a chart of $\operatorname{Gr}(d,K)$ we write
$Z=Z(\theta)$ for a basis of $\mathcal Z$.

The spectral test we use is yours: with $P_{\mathcal Z}(\lambda)=[(\lambda I-A)V\,|\,Z]$ and $m_1,\dots,m_N$ its
maximal minors, $(5b)$ at $\theta$ holds iff $e_0\in\operatorname{col}M(\theta)$, where $M(\theta)$ is the
$2D\times ND$ Bézout coefficient matrix of the $m_i$ and $D=\max_i\deg_\lambda m_i$.

---

# Part II. What was done

## II.1 The double stratification does not terminate in practice

Following your remark that one must take a *finite disjunction over the specialized degrees*, we implemented two
stratifications:

* $\rho=\operatorname{rank}[V|Z]$, which fixes the size of the maximal minors of $P_{\mathcal Z}$;
* $r=\operatorname{rank}[\mathcal Z^\perp\,|\,W]$, which fixes the rank condition of $(5a)$.

Every stratum is described by "all $(\rho+1)$-minors vanish" together with a non-vanishing condition, which we
encoded by Rabinowitsch's trick ($zf-1=0$) for each candidate minor $f$. The resulting computations are
\[
\#\rho\times\#r\times\#\{\text{witness minors}\}^2
\]
Gröbner bases, each with two saturation variables **plus** the chart parameters. On a single $n=6$ chart this did
not finish in ten minutes; on the $n=7$ instance it did not finish in twenty. **So the double stratification is
correct in principle but not usable at these sizes.**

## II.2 The single stratification does work, for the feasible direction

Restricting to charts with one chart parameter and stratifying only by $\rho$, we obtained a working procedure for
the feasible direction: on stratum $\rho$, if $M_\rho$ has full row rank then $e_0\in\operatorname{col}M_\rho$
automatically, so any point of the stratum is spectrally feasible; we then verify $(5a)$, $(5b)$ and your seven
consistency checks at a rational point. Four instances were decided this way at $q_0$, each with a witness:

| instance | stratum | parameter | outcome |
|---|---|---|---|
| $n=5$, $p=1$, $r=2$, one seed | chart $(0)$, $\rho=3$ | $\theta=0$ | witness, checks pass |
| $n=5$, $p=1$, $r=2$, another seed | chart $(1)$, $\rho=3$ | $\theta=0$ | witness, checks pass |
| $n=5$, $p=2$, $r=1$ | chart $(0)$, $\rho=2$ | $\theta=0$ | witness, checks pass |
| $n=6$, $p=2$, $r=2$ | chart $(0)$, $\rho=3$ | $\theta=0$ | witness, checks pass |

## II.3 The rank drops, and this was the source of earlier contradictions

At $\theta=0$ in one of the above instances, $\operatorname{rank}[V|Z]$ is $3$ while its generic value is $4$. The
maximal minors of $P_{\mathcal Z}$ therefore change size at that parameter. Using a fixed size (the generic one) at
such a point gives $\operatorname{rank}M(0)=0$ and $\operatorname{rank}[M(0)|e_0]=1$, i.e. your criterion would
report failure, whereas both the Toeplitz test and the nullspace-pencil test report success. **The criterion is not
violated; the minor size was wrong.** Stratifying by $\rho$ repairs exactly this.

## II.4 A stratum can be nonempty yet contain no admissible point

In the $n=6$ counterexample, stratum $\rho=2$ consists of the single parameter $\theta=5/4$. There
$\operatorname{rank}[V|Z]=2$, and $M_2$ has full row rank, so the *spectral* condition is satisfied — but $(5a)$
fails at that point (we verified: $\operatorname{rank}[\mathcal LA;\mathcal L;CA;C]>\operatorname{rank}[\mathcal L;CA;C]$).
Hence layer-emptiness certificates must include the $(5a)$ conditions; the spectral stratification alone does not
suffice. This is the reason for the second stratification in II.1, and hence for the cost.

## II.5 Two classes of instances at the minimal order

Comparing the generic degree of the gcd of the $m_i$ across instances separates them cleanly:

* **generic degree $0$** (and $M$ of full row rank): $X_{\rm sp}=X$; the spectrally feasible set is open. Two
  instances of this kind ($n=5,p=2,r=1$ and $n=6,p=2,r=2$) are feasible at *every* parameter of every chart;
* **generic degree $\ge1$**: $X_{\rm sp}\subsetneq X$; feasible parameters, when they exist, lie on the locus where
  the generic gcd drops to degree $0$. The $n=6$ counterexample is the extreme case in which that locus is empty.

We earlier described this as "the feasible set is always thin"; that was too strong and we have corrected it. The
correct statement is the two-case one above, and even it is an observation over six instances, not a theorem.

## II.6 Encoding size is exponential, which voids the $\exists\mathbb R$ route

You warned that $N$ may blow up; we measured it. At the controlled order $q=\lfloor n/2\rfloor$ with $p=r=1$ one has
$\mathrm{ncols}=\dim V+d\approx1.5n-3$ and maximal minors of size $s=n$, so
$$N=\binom{1.5n-3}{n},\qquad \#\text{charts}=\binom{n-2}{\lfloor n/2\rfloor-1}.$$
Measured: $\log_2 N/n$ rises from $0.40$ at $n=8$ to $1.09$ at $n=28$ (where $N\approx1.7\times10^9$), and the
number of charts reaches $1.0\times10^7$ at $n=28$. Both are exponential.

Consequences we accept: (i) the subdeterminant/Bézout representation is **not** of polynomial size, so
$\mathrm{DEC}(q)\in\exists\mathbb R$ does **not** follow by this route; (ii) no polynomial algorithm can proceed by
enumerating charts and minors, so any algorithm must use the structure (for instance an implicit treatment of the
rank equation $(\star)$, or a polynomial description of the stratification itself).

## II.7 Two tools we had to abandon

For completeness, and because the failure modes may be informative:

* one implementation of the stratified decision gave verdicts *contradicting* the validated Bézout tool on the same
  stratum (its minor set and degree bound differed by a re-filtering step). We discarded it rather than repair it,
  and recorded the discrepancy;
* the double-stratified one is II.1.

Everything we still use is certified: for a fixed augmentation there are three independent tests of $(5b)$ (Toeplitz
nullity, gcd of maximal minors, nullspace pencil) which agree on all comparisons we ran; the seven consistency
checks are applied to every witness before it is reported.

---

# Part III. Questions

**Q1 (formulation of the disjunction).** Is there a cheaper way to encode the double stratification than
Rabinowitsch saturation on every witness minor? Two alternatives we can imagine: (a) work in the chart's coordinate
ring with the Plücker relations and use a single saturation by the ideal of $\rho$-minors (we could not get sympy to
do ideal quotients efficiently); (b) choose the chart and the stratum so that $(5a)$ is automatic (for instance
charts where $h=n$, where $(5a)$ holds identically), which would eliminate the second stratification entirely.
Is (b) legitimate as a completeness argument, or does it lose cases?

**Q2 (which compact representation to try).** Given the measured growth in II.6, which of the four possibilities you
listed would you attempt first: explicit generators, a linear combination with resultants, keeping the pencil
implicit (so that the rank equation is tested structurally rather than expanded), or an abstract framework? We have
no intuitions about which has a chance of being polynomial.

**Q3 (the two classes of II.5).** Is the dichotomy "generic gcd degree $0$ versus $\ge1$" a known invariant of the
pair $(V,W)$? If the spectral condition is a determinantal condition on the Grassmannian, the first class should be
the complement of a proper subvariety and the second its complement — and the thinness would be a corollary of the
codimension rather than a curiosity. We would rather cite this than rediscover it.

**Q4 (the $(5a)$ failure inside a spectral stratum).** The point of II.4 shows that the spectral condition can hold
exactly where algebraic admissibility fails. Is there a reason, in the chart framework, to expect the two conditions
to be *complementary* in this way, or is it an artefact of the degenerate point? If it is structural, the per-order
problem may reduce to a single determinantal condition rather than two.

**Q5 (priority).** Given that the honest state is "the decision procedure is certified but incomplete, and its
natural algebraisation is exponential", would you still put the per-order decision first, or is the more useful next
step the write-up of the two results we do have (the dimension obstruction with its uniformity, and the counterexample
with its three proofs)?
