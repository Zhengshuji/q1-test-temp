# State of the work: corrections, settled results, an assessment, and eight questions

This note is self-contained and replaces the two previous ones. It has three parts: what was corrected (II.A),
what we regard as settled (II.B–II.E, with the explicit certificates), our own reading of the position and of what
should be written (II.F–II.G), and eight questions (Part III).

---

# Part I. Setting

For $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$ with $L_0\ne0$ and
$\operatorname{rank}[C;L_0]=p+r$, and a $q\times n$ matrix $\mathcal L$ whose row space contains $\operatorname{row}L_0$:

$$(5a)\ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\quad\forall\lambda\in\mathbb C .$$

$q_0$ is the least $q$ for which $(5a)$ has a solution; $n_0=\operatorname{rank}\mathcal O_C$ with
$\mathcal O_C=[C;CA;\dots;CA^{n-1}]$; the order interval used below is $[q_0,\,n_0-p]$.

Notation. $W=\operatorname{row}[C;CA]$, $r_1=\dim W$, $V=\ker[C;CA]$, $K=\ker[C;L_0]$,
$S=\operatorname{row}[C;L_0]+W$, $s_0=\dim S$, $\mathcal Z=\ker[C;\mathcal L]$ with $d=\dim\mathcal Z=n-p-q$,
$h=\operatorname{rank}[\mathcal L;CA;C]$, $\pi:\mathbb C^n\to\mathbb C^n/S$. Two facts:

$$(5b)\iff d_{\rm fin}=0;\qquad h=\dim(\mathcal Z^\perp+W)=s_0+\dim\pi(V').\tag{1}$$

---

# Part II. The work

## II.A What was corrected

| earlier claim | correction |
|---|---|
| a certain $n=7$, $p=r=2$ instance has no admissible order | it has an order-three solution (II.C); $q_{\min}=3$ |
| for it, $h=6$ at $q=2$ | $h=\operatorname{rank}[L_0;CA;C]=5$; the maximal-minor gcd is $\lambda-1$, so $(5b)$ fails at $\lambda=1$ |
| three candidates at order three, all failing | the enumeration was incomplete; a complete scan of $\operatorname{Gr}(2,3)$ gives 18 admissible nullspaces, 2 of which work |
| the occlusion argument holds as stated | it needs $h=n$ at that order; a nonzero kernel vector alone does not force a drop below $h$ |
| surjectivity of the bad-point map is the criterion | the correct sufficient condition is $\dim\overline{\Phi(\mathbb P(V))}\ge q-r$ |
| rational maps of projective spaces always extend to morphisms | false above dimension one; only the curve case was used correctly |
| orders $q=4,5$ of that instance were relevant | they lie outside $[q_0,n_0-p]=[2,3]$ |

## II.B The order-three solution, and why the earlier search missed it

Take $n=7$, $p=r=2$,

$$A=\begin{pmatrix}
1&0&0&-1&0&-1&1\\
1&0&0&0&1&0&0\\
1&1&0&-1&0&0&0\\
0&0&0&0&0&0&0\\
0&0&0&0&0&0&0\\
0&-1&0&0&1&0&0\\
0&-1&0&1&1&1&0
\end{pmatrix},\quad
C=\begin{pmatrix}0&-1&0&0&1&0&0\\ 1&0&0&0&0&0&0\end{pmatrix},\quad
L_0=\begin{pmatrix}-1&0&0&0&-1&0&0\\ 1&0&0&0&0&0&1\end{pmatrix},$$

and
$$\mathcal L_*=\begin{pmatrix}-1&0&0&0&-1&0&0\\ 1&0&0&0&0&0&1\\ 1&0&0&-1&0&-1&1\end{pmatrix},$$
whose third row is the second row of $CA$. Then
$$\operatorname{rank}[C;\mathcal L_*]=5,\qquad\operatorname{rank}[\mathcal L_*;CA;C]=5=h,\qquad
\operatorname{rank}[\mathcal L_*A;\mathcal L_*;CA;C]=5,$$
so $(5a)$ holds. Two $5\times5$ minors of $Q_*(\lambda)=[\lambda\mathcal L_*-\mathcal L_*A;CA;C]$ are constant and
nonzero: rows $1,2,3,4,7$ with columns $1,2,4,5,7$ give $-1$, and the same rows with columns $1,2,5,6,7$ give $+1$.
Hence $\operatorname{rank}Q_*(\lambda)\ge5$ for all $\lambda$, while $(5a)$ gives
$\operatorname{rank}Q_*(\lambda)\le h=5$; so $(5b)$ holds and $q_{\min}=3$.

The nullspace is $\ker[C;\mathcal L_*]=\operatorname{span}\{e_3,\,-e_4+e_6\}$, a two-dimensional subspace of
$K=\operatorname{span}\{e_3,e_4,e_6\}$. A complete scan of $\operatorname{Gr}(2,3)$ — three charts, a rational grid
on each, exact arithmetic — finds 18 nullspaces satisfying $(5a)$, of which 2 satisfy $(5b)$; one of them
corresponds to the augmentation $[L_0;(0,0,0,1,0,1,0)]$, different from $\mathcal L_*$. The earlier report examined
three candidates, so the miss was a gap in the enumeration, not a nonexistence result.

## II.C What we regard as settled

| statement | level |
|---|---|
| $(5b)$ at a fixed augmentation $\iff$ the single block-Toeplitz identity $\nu_s=(s+1)m-s$ with $m=q+2p-h$; the left indices are recovered by $\nu_d-2\nu_{d-1}+\nu_{d-2}$ | paper proof, independent certificate 66/66 against a Smith-form route |
| $(5b)\iff d_{\rm fin}=0\iff\sum_j\varepsilon_j=\operatorname{rank}\mathcal L$ | paper proof |
| $(5b)$ need only be tested at $\operatorname{spec}\Lambda$, where $Q_{\mathcal L}(\lambda)=D(\lambda)H$; the obstructing divisors can be nonreal | paper proof, 3 checks |
| $h=\dim(\mathcal Z^\perp+W)=s_0+\dim\pi(V')$, hence the integer obstruction $h\ge q+r_1$ is equivalent to $\dim\pi(V')\ge q+r_1-s_0$; if $V'\cap S=0$ it is equivalent to $s_0\ge r_1+r$ and is then a property of the order, not of the augmentation | paper proof, 495 sampled augmentations |
| the published two-order-gap example fails at $q_0$ and at $q_0+1$ by the integer obstruction ($h=q+r_1$ at both) and admits an explicit augmentation at $q_0$ | paper proof at $q_0$; complete scan 486/486 at $q_0+1$ |
| an $n=6$, $p=r=2$ instance has $h<q_0+r_1$ at $q_0$ and nevertheless fails, and the whole family fails there | counterexample with three independent checks; family-wide statement proved as the next two rows |
| for that instance $(5a)$ is automatic at $q_0$ ($h=n$), and the bad-point map $\mathbb P(V)\to\mathbb P(K)$, $x\mapsto\operatorname{span}((\lambda(x)I-A)x)$, is a nonconstant $\mathbb P^1\to\mathbb P^1$, hence surjective, so every nullspace carries a rank-dropping $\lambda$ | paper proof with an exact certificate |
| occlusion criterion: if $h=n$ at an order and $\dim Y\ge q-r$ with $Y=\overline{\Phi(\mathbb P(V))}$, then the order has no solution | paper proof (projective dimension theorem); on the $n=6$ instance $\dim Y=1=q-r$ |
| the $n=7$, $p=r=2$ instance has $q_{\min}=3$ with an explicit $\mathcal L$ certified by two constant maximal minors | exact certificate, independent regression |

## II.D The integer criterion in the form we use

Fix an order $q$, put $t=q-r$, and write $\mathcal Z^\perp=K^\perp+V'$ with $\dim V'=t$. By (1),
$$h=\dim(S+V')=s_0+\dim\pi(V'),$$
so
$$h\ge q+r_1\iff \dim\pi(V')\ \ge\ q+r_1-s_0 .$$
On orders with $V'\cap S=0$ (equivalently $\dim\pi(V')=t$) the condition becomes
$$h\ge q+r_1\iff s_0\ \ge\ r_1+r,$$
which does not involve the augmentation: on such an order either every admissible augmentation is excluded, or none
is. The hypothesis $V'\cap S=0$ must be checked for the family in question; it does not follow from dimensions alone.

**Verification.** On 495 sampled admissible augmentations, $h=s_0+q-r$ held in every case with $V'\cap S=0$; the
identity $h=\dim(\mathcal Z^\perp+W)$ was checked separately on 360 samples.

**The published example** ($n=8$, $p=r=2$, $r_1=4$, $q_0=3$, $s_0=6$): at $q=3$, $t=1$ and $q+r_1=7=s_0+t$, so
$h=7=q+r_1$ for every admissible augmentation, and an explicit admissible augmentation exists; at $q=4$ a complete
scan of 486 admissible nullspaces gives $h=8=q+r_1$ in every case; at $q=5$, $\dim\pi(V')\le n-s_0=2<t=3$, so
$h\le8<9=q+r_1$ and the integer obstruction is impossible. The order spectrum of that example therefore has an
integer explanation, and both its failures are of the integer type.

## II.E Whole-family infeasibility, and the reach of the occlusion criterion

Suppose that at an order $q$ every admissible augmentation has $h=n$; then $\mathcal Z^\perp+W=\mathbb C^n$ and
$(5a)$ holds for every $\mathcal L$. For $x\in V$ with $L_0x\ne0$ put
$$\lambda(x)=\frac{L_0Ax}{L_0x},\qquad z(x)=(\lambda(x)I-A)x .$$
If $z(x)\in K$, then for $\mathcal Z=\operatorname{span}z(x)$ one has
$[\lambda(x)\mathcal L-\mathcal LA;CA;C]\,x=0$ with $x\ne0$, and since $h=n$ this forces a drop. With
$Y=\overline{\Phi(\mathbb P(V))}\subseteq\mathbb P(K)$, the projective dimension theorem gives: if
$$\dim Y\,+\,(d-1)\ \ge\ \dim\mathbb P(K)-1\iff \dim Y\ \ge\ k-d=q-r\qquad(k=\dim K),$$
then $Y$ meets $\mathbb P(\mathcal Z)$ for every admissible $\mathcal Z$, and the order has no solution.

**The instance where this is sharp** is the $n=6$, $p=r=2$, $q_0=3$ one with $r_1=p+r=4$: there
$h=s_0+t=5+1=6=n$, and an exact Jacobian computation gives $\dim Y=1=q-r$, so the order is excluded — this is the
instance whose whole family at $q_0$ fails.

**Reach.** The map requires $z(x)\in K$, i.e. $\lambda(x)L_0x=L_0Ax$ for every row of $L_0$. For $r=1$ this is
automatic; for $r\ge2$ it is two equations for one unknown and usually fails; and if $V\subseteq\ker L_0$ the map is
not defined at all. In addition the criterion needs $h=n$, which held in 3 of 22 random instances with $r=1$; in
those 3 it was correct (two predicted exclusion and the order was excluded, one predicted feasibility and the order
was feasible).

## II.F Our reading of the position

We state this as our own assessment, so that it can be corrected as directly as the earlier claims were.

* **The problem splits cleanly in two.** The integer obstruction is decided by $s_0$, $r_1$, $r$ together with the
  placement of $V'$ in $S$; the spectral obstruction is what remains. This split is the most useful thing we have,
  because it removes the augmentation from half of the problem.
* **The integer criterion is our most defensible standalone statement.** It has a two-line proof, needs no spectral
  computation, and on orders with $V'\cap S=0$ it classifies the whole family at once.
* **The occlusion criterion is a sufficient condition of narrow reach** — it requires both $h=n$ and the map to be
  defined — yet it is the only mechanism for which we have a proof of whole-family infeasibility, so we do not think
  it should be the main theorem.
* **The published example is no longer a mystery.** Its order spectrum follows from integers alone. This is the
  cleanest single illustration we have.
* **The gap to the complexity question is the $r\ge2$ occlusion problem.** Without a per-order criterion covering
  $h<n$ we have no decision procedure to analyse. That step separates the present state from $q1$.
* **Our experimental evidence is weaker than it looks.** The claim that the integer obstruction is the only one in
  generic instances rests on families with $n\le9$, $p,r\le3$; we now treat it as a guess, not a claim.
* **Our errors had one pattern:** incomplete enumeration, or a hypothesis left implicit ($h=n$, the order interval,
  the constant-minor certificate). We have since added a regression test built on the order-three augmentation and a
  per-order procedure that enumerates the Grassmannian chart by chart in exact arithmetic.

## II.G What we would write, and in what order

1. the integer criterion and the order spectrum of the published example (II.C, rows 4–5);
2. the $n=6$ counterexample with its whole-family proof and the occlusion criterion with its hypotheses
   (II.C rows 6–9, II.E);
3. the exact per-order examples, including the order-three augmentation with the two constant minors;
4. the boundary observation as a conjecture with sample sizes stated;
5. the complexity question as open, naming the $r\ge2$ occlusion problem as the gap.

We would not present functional observability itself, or the design rank conditions, as our contribution.

---

# Part III. Questions

**Q1 (the gap).** The obstruction of II.E is defined through a pair $(x,\lambda)$ with $x\in V$, $x\ne0$ and
$\lambda x-Ax\in\ker\mathcal L$. We would like a formulation in which this is a condition on $\mathcal Z$ alone, so
that the occlusion criterion survives when $r\ge2$ and when $h<n$ — for instance through the pencil
$[\lambda\mathcal L-\mathcal LA]$ restricted to $V$, or through a map into $\mathbb C^n/\ker\mathcal L$ with
$\mathcal Z$ as the parameter. This is the one point on which we have no plan.

**Q2 (novelty of the integer criterion).** Is the threshold $h\ge q+r_1$, equivalently
$\dim\pi(V')\ge q+r_1-s_0$, familiar from the observer literature under another name? And does the nullspace
parametrisation of the 2026 preprint make the uniformity statement of II.D (failure type constant over the family
when $V'\cap S=0$) visible? It is the statement we would most like to be sure of, since it turns a search into a
computation.

**Q3 (complexity).** Is any restricted version of the minimal-order problem known to be hard — with fixed $p,r$,
with $A$ in companion form, or with $\mathcal L$ restricted to a coordinate subspace? A hardness result for a
restricted class would tell us whether the per-order criterion aims at the right object.

**Q4 (the order interval).** Is $n_0-p$ always the correct upper end, and is $q_{\min}\le n_0-p$ guaranteed for
functionally observable data? One of our searches initially ranged over $[q_0,n-p]$ and produced a spurious case.

**Q5 (terminology).** We write "integer obstruction" and "spectral obstruction" for $h\ge q+r_1$ and for
$d_{\rm fin}>0$ with $h<q+r_1$. Is there established terminology we should adopt?

**Q6 (what is enough for a note).** Of the five items in II.G, which would you regard as sufficient for a short
note, and which would you leave out as too speculative? In particular, would you include the $n=6$ counterexample
on its own, given that its mechanism has narrow reach?

**Q7 (the Toeplitz criterion).** The Toeplitz identity of II.C was your suggestion and we have kept it as the
primary test of $(5b)$ at a fixed augmentation, with the maximal-minor gcd as the independent check. For a written
version, would you present it, or treat it as an implementation detail behind the gcd?

**Q8 (where we could still be wrong).** Given the corrections in II.A, where are our checks most likely to be
systematically wrong? We are aware of two risks: the treatment of $\lambda=0$ together with singular $A$, and the
convention for stacking ranks (rows versus columns). A third opinion on where to look would be worth more than
another experiment.
