# Report on the recommended programme: status, what changed, and what remains

This note is self-contained and reports on the programme proposed in your last two replies. Part II gives the
status of every item, including three corrections we had to make to our own claims. Part III states the two
problems we cannot resolve and four questions.

---

# Part I. Setting (recall)

For $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$ with
$\operatorname{rank}[C;L_0]=p+r$ and a $q\times n$ matrix $\mathcal L$ whose row space contains $\operatorname{row}L_0$:

$$(5a)\ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\quad\forall\lambda\in\mathbb C .$$

$q_0$ is the least order solvable for $(5a)$; $n_0=\operatorname{rank}\mathcal O_C$; the order interval is
$[q_0,n_0-p]$. Notation: $W=\operatorname{row}[C;CA]$, $r_1=\dim W$, $V=\ker[C;CA]$,
$K=\ker[C;L_0]$, $S=\operatorname{row}[C;L_0]+W$, $s_0=\dim S$, $h=\operatorname{rank}[\mathcal L;CA;C]$,
$Q_{\mathcal L}(\lambda)=[\lambda\mathcal L-\mathcal LA;CA;C]$.

---

# Part II. Status of the recommended items

## II.1 Your §1 (use the nullspace pencil as the primary spectral test)

Implemented exactly. We compute the maximal minors of $P_{\mathcal Z}(\lambda)=[(\lambda I-A)V\ |\ Z]$ and take
their gcd over $\mathbb Q$; this agrees with the Toeplitz test and with the gcd of the $Q_{\mathcal L}$-minors on
6 of 6 test pencils (including two deliberately failing ones). A sampled-$\lambda$ version of the same test was
found to give a **wrong** verdict on one candidate (the drop sits at a non-rational $\lambda$), so only the
identity-based version is used.

## II.2 Your §2 (dimension obstruction and uniformity)

Both kept, with the hypothesis $V'\cap S=0$ stated every time. Verified on 495 augmentations
($h=s_0+q-r$ whenever the hypothesis holds) plus 360 for the underlying identity. The published example's whole
order spectrum is explained by integers.

## II.3 Your §3.1 (algebraic feasibility formulation) — done

The fixed-order problem is written as
$$\exists\Theta\,\exists\{u_i\}:\quad \sum_i u_i(\lambda)\,m_i(\lambda;\Theta)=1,\quad \deg u_i\le\dim V,$$
with $m_i$ the maximal minors of $P_{\mathcal Z}$; linear in $u$, degree $\le s$ in $\Theta$. Variable and degree
counts are polynomial, consistent with $\exists\mathbb R$.

## II.4 Your §3.2 (which restrictions to investigate)

* **$r=1$**: done. The system above is written explicitly; a midpoint test on the chart coordinates shows the
  $(5a)$-locus is **not** affine (violations 12/15 and 36/40), so the "linear degeneration $\Rightarrow$
  polynomial algorithm" hope is dead in that form.
* **coordinate-row restriction on $\mathcal L$**: done, and it produced a *negative* logical finding. Restricting
  $\mathcal L$ to coordinate rows restricts the **solution set**, not the **instance class**; hardness of a
  solution-restricted problem does not transfer to the general problem. This is exactly the trap our own archived
  notes had recorded for the graph reduction (TAP specialisation), and we reproduced it before catching it.
* **companion form**: not started, as you advised against starting there.

## II.5 Your §4 (order interval) — confirmed and adopted

All per-order procedures now run over $[q_0,n_0-p]$. We had earlier used $[q_0,n-p]$, which produced a spurious
case; that error is recorded.

## II.6 Your §5 (terminology) — adopted

"dimension obstruction", "spectral obstruction", "uniform spectral infeasibility", "incidence obstruction".

## II.7 Your §7 (Toeplitz criterion) — kept as a proposition

It appears as an appendix proposition with the block construction, the identity
$\nu_s=(s+1)m-s$, $m=q+2p-h$, and the second-difference recovery of the left indices; the maximal-minor gcd stays
as the independent certificate. The 66/66 agreement is stated as regression evidence, not as proof.

## II.8 Your §8.1 (a rational grid is not a complete chart scan) — substantially done

This was the item you flagged twice, and it is where the work went. We found that the available Python has sympy,
which changed what is feasible:

* **$(5a)$ layer.** Per chart, with $h_0=\operatorname{rank}B$, $B=[\mathcal Z^\perp\,|\,W]$, we impose all
  $(h_0+1)$-minors of $M=[(\mathcal Z^\perp)A^{\mathsf T}\,|\,B]$ and saturate "some $h_0$-minor $\ne0$" by the
  Rabinowitsch trick ($zf-1=0$). Gröbner basis $=[1]$ is a certificate of emptiness. We obtained one: on one chart
  of the $n=7$ instance at $q=3$, $(5a)$ has no solution at all.
* **Spectral layer.** Per chart we compute the gcd of the maximal minors over $\mathbb Q(\theta)[\lambda]$. Its
  $\lambda$-degree decides the generic case: degree $0$ means $(5b)$ holds for generic $\theta$ (and substituting a
  rational $\theta$ gives a witness that then passes the seven consistency checks); degree $\ge1$ means generic
  failure, and the gcd itself exhibits the common factor.
* **The $n=6$ counterexample now has a second, purely algebraic proof.** Both charts have generic degree $\color{red}{2}$,
  and at the only exceptional parameters ($\theta=5/4$ and $\theta=4/5$, the zeros of the denominators) the degree is
  $\color{red}{1}$, not $0$. So no parameter value admits $(5b)$ — independent of the earlier projective-surjectivity
  argument.
* **The published example at $q=5$**: all four charts have degree $0$; substituting $\theta=0$ produces an explicit
  5-row witness which passes the consistency checks.

## II.9 Your §8.2–§8.6 — done

* **§8.2** candidate matrices are rational, hence real; this is now an assertion in the checker.
* **§8.3** the target rank is verified as the normal rank in every pencil test.
* **§8.4** the spectral domain is an explicit parameter, with $\lambda=0$ included for $\mathbb C$; we also added a
  diagnostic that reports whether sampling in a given domain would *miss* the drop.
* **§8.5** for the $n=6$, $r=2$ counterexample the proportionality $L_0Ax\parallel L_0x$ on $V$ is now proved: the
  $2\times2$ determinant is a quadratic form vanishing on a basis of $V$ and on pairwise sums, hence identically.
  The image-versus-closure distinction is stated where it matters; in that example the map is a morphism of curves.
* **§8.6** the seven consistency checks are a module, and the regression test built on the order-three witness now
  runs them.

## II.10 Your §9 (the three decisions)

1. Pencil criterion promoted — done. 2. Dimension obstruction and uniformity kept as the principal contribution —
   done. 3. The counterexample kept with a tightened proof (proportionality, image/closure, plus the new algebraic
   proof) — done.

## II.11 Corrections we had to make to our own claims

| claim | what was wrong |
|---|---|
| "a chart with generic gcd degree $\ge1$ is uniformly bad" | **false**: the gcd degree can *drop* at special parameters, and $(5b)$ then holds. Two instances where the grid had found witnesses were being declared infeasible. The tool now reports `UNKNOWN` instead. |
| "the chart analysis found a defect in the nullspace generator" | false; the defect was a transpose in our own new code ($(5a)$ requires $xA$, i.e. $A^{\mathsf T}$ on columns, not $A$). |
| "a rational grid confirms there are exactly 18 admissible nullspaces" | withdrawn; grid counts are exploration, never certificates. |

The drop phenomenon turned out to be informative rather than merely an error:

## II.12 Observation: at $q_0$ the feasible points are the drop locus

On six small instances at $q_0$, **every** chart has generic gcd degree $\ge1$: generic positions all fail.
Wherever the grid found a witness, it lay at a parameter value where the gcd drops to degree $0$. So at the minimal
order

$$\{\text{feasible }\theta\}\ =\ \{\theta:\ \text{the generic gcd drops to degree }0\},$$

a finite determinantal set rather than an open one. This explains, in one stroke, why the $q_0$ level is thin, why
sampling almost always fails, and why witnesses nevertheless exist. For the $n=6$ counterexample this set is empty,
which is precisely why its whole family fails.

---

# Part III. Problems, next steps, questions

## III.1 The two open technical problems

**(a) Deciding "does the gcd ever drop to degree $0$?"** We can only produce *necessary* candidates (zeros of the
gcd's $\lambda$-leading coefficient and of its denominator). The drop can also occur at zeros of the individual
minors' leading coefficients, so our candidate set is incomplete and the tool deliberately refuses to certify
"no drop". The right condition is presumably a subresultant degeneracy of the whole family $m_1,\dots,m_N$; we have
not found the correct formulation (and would welcome one).

**(b) Companion-form and other instance restrictions.** Not started, per your advice.

## III.2 Questions

**Q1.** Is there a standard way to decide "$\exists\theta$: the maximal minors of $P_{\mathcal Z}(\theta,\lambda)$
are coprime" — e.g. a subresultant condition on the family, or a statement about the ideal of maximal minors of the
Bézout matrix of §II.3 being the unit ideal? Our present approach is unsound in the "no drop" direction.

**Q2.** Does the observation of II.12 match something in the 2026 preprint? If the algebraically admissible
nullspaces form a variety and the spectral condition cuts a proper subvariety out of it, the thinness at $q_0$ would
be a corollary rather than a surprise.

**Q3.** We are ready to write the short note in the shape you proposed (dimension obstruction plus uniformity as the
first result; the $n=6$ counterexample, now with two proofs, as the second). Should the drop-locus observation of
II.12 appear in it, and if so as a remark or as a conjecture?

**Q4.** Given that the quantity that decides the minimal order appears to be a determinantal (non-open) condition,
would you still advise against attempting a reduction for hardness — or does this change the picture, since
"feasible = zeros of a polynomial system" is exactly the shape that hardness reductions like?

---

# Part IV. State in brief

* Every recommendation of your last two replies has been carried out, except the companion-form restriction
  (which you advised against) and the final writing of the note.
* The per-order decision is now certificate-based and grid-free for charts with at most three parameters: feasible
  gives a witness passing seven consistency checks; infeasible gives an integer, an algebraic-emptiness, or a gcd
  certificate.
* The $n=6$ counterexample has two independent proofs; the published example is settled at both ends
  ($q_{\min}=5$ with an explicit witness at $q=5$).
* The open problem is the completeness of the drop-locus decision (III.1a).
* No complexity result, and none claimed.
