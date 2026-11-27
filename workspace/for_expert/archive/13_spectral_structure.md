# Structural results on the spectral obstruction, and a request for direction

This note reports what changed since the last one: the proportionality invariant has been characterised and
machine-verified, a second whole-family spectral counterexample has been constructed and proved, the failure locus
has been shown to be thin in the data, and the obstruction has been written as a system of quadratic conditions.
Nothing here is about presentation; the paper remains deferred. Part III asks where to go next.

Verification levels: **L1** paper proof; **L2** exact arithmetic on instances; **L3** machine-checked (Lean).

---

# Part I. Setting

$A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$,
$\operatorname{rank}[C;L_0]=p+r$, $L_0$ and $(C,A)$ observable. A candidate $\mathcal L\in\mathbb C^{q\times n}$ has
$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$, $\operatorname{rank}[C;\mathcal L]=p+q$.
$h=\operatorname{rank}[\mathcal L;CA;C]$, and

$$(5a)\ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=h,\qquad
(5b)\ \operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=h\ \ \forall\lambda .$$

$V=\ker[C;CA]$, $K=\ker[C;L_0]$, $R=\operatorname{row}\mathcal L$, $\mathcal Z=\ker[C;\mathcal L]$, $d=n-p-q$;
$W=\operatorname{row}[C;CA]$ with $r_1=\dim W$; $S=\operatorname{row}[C;L_0]+W$ with $s_0=\dim S$.
Type I $:=$ $h\ge q+r_1$; Type III $:=$ $h<q+r_1$ with a finite elementary divisor of positive degree.
"Whole-family failure" at an order means every $(5a)$-admissible $\mathcal L$ of that order fails $(5b)$.

---

# Part II. What is new

## II.1 The exact failure criterion, in a usable form

Under $(5a)$, with $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$:
$$(5b)\ \text{fails at}\ \mathcal Z\iff\exists x\in V\setminus\mathcal Z,\ \lambda:\ (\lambda I-A)x\in\mathcal Z .$$
L1 (three lines) + L2 (six explicit $(x,\lambda_0)$ certificates on the first counterexample, with $\lambda_0$
irrational or complex). The equivalent quotient form (as you suggested) is cleaner for constructions: with
$J_{\mathcal Z}:V\to X/\mathcal Z$, $x\mapsto x+\mathcal Z$ and $T_{\mathcal Z}:x\mapsto Ax+\mathcal Z$, failure is
the existence of a **generalised eigenvector** of the pair $(T_{\mathcal Z},J_{\mathcal Z})$ with
$J_{\mathcal Z}x\ne0$.

## II.2 The proportionality invariant is now a rank test

With $U_0=L_0|_V$, $U_1=L_0A|_V:V\to\mathbb C^r$ and
$P=\{x\in V:U_0x\wedge U_1x=0\}$, $\varepsilon=\dim V-\dim P$, the three-case characterisation you proposed holds:

$$\varepsilon=0\iff\begin{cases}\operatorname{rank}U_0=0:&\text{automatic}\\ \operatorname{rank}U_0=1:&
\operatorname{im}U_1\subseteq\operatorname{im}U_0\\ \operatorname{rank}U_0\ge2:&U_1=\alpha U_0 .\end{cases}$$

L1 + L2 **5983/5983** (all three cases represented). So $\varepsilon=0$ no longer needs a Gröbner basis.

## II.3 A second whole-family counterexample, with gap 2

At $n=6$, $p=r=2$ we constructed a family by design: choose $V$, let $A$ map $V$ into $\ker C$, then choose $L_0$
with $(A-\alpha I)V\subseteq\ker L_0$. All 86 successfully built instances are whole-family Type III at the order
$q_0+1$. One of them is now a **theorem**:

* $q_0=2$: the single admissible $\mathcal Z=K$ gives $h=6=q+r_1$ — **Type I** failure;
* $q=3$: $h=6<q+r_1=7$ and **every** $\mathcal Z$ fails. Proof: $M(\theta,\lambda)=(I-P_z)(\lambda I-A)V$ is
  $6\times2$; failure $\iff\operatorname{rank}M\le1$; the gcd of its fifteen $2\times2$ minors over
  $\mathbb Q(\theta)[\lambda]$ is $\lambda+2$ — monic, **independent of $\theta$**, and all minors vanish at
  $\lambda=-2$ identically, so **the drop locus is empty**;
* $q=4$: an explicit four-row augmentation satisfies both conditions (seven independent checks).

Hence $q_{\min}=4$ and the **order gap is 2**, with both failure types occurring on the same instance. The
motivation for this instance was your remark that $\varepsilon=0$ together with the dimension equality is not the
boundary; we also note that $\varepsilon=0$ alone is *not* sufficient for whole-family failure — along the
deformation $A_{00}=t$ one has $U_1=(-t-4)U_0$ for every $t$, yet only $t=2$ is infeasible.

## II.4 The failure locus is thin in the data

Deforming a single entry of the counterexample ($A_{00}=t$) gives, at $q=q_0+1$ over 26 sampled candidates:

| $t$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---|---|---|---|---|---|---|---|---|---|
| feasible | 23 | 23 | 23 | 23 | 23 | **0** | 23 | 23 | 23 | 23 |

So whole-family infeasibility is a **codimension-$\ge1$ phenomenon** in the data, not an open condition. This is
consistent with your expectation that it is not a codimension-one boundary, and it constrains any reduction: the
infeasible locus cannot be produced by leaving a parameter free.

## II.5 A single-$\lambda$ certificate, and the design constraint it imposes

If $\dim V=\dim K$ and there is $\lambda_0$ with $(\lambda_0I-A)V=K$, then every $\mathcal Z\subseteq K$ of dimension
$d\ge1$ fails at $\lambda_0$, except those with $(\lambda_0I-A)^{-1}\mathcal Z\subseteq\mathcal Z$. The exceptions are
absent when $V\cap K=0$, and
$$\dim(V\cap K)=\dim\ker[C;CA;L_0]\ \ge\ n-(2p+r),$$
so **the exception-free case needs $2p+r\ge n$**. Both counterexamples sit exactly at $2p+r=n$ ($n=6$, $p=r=2$);
moreover $\dim V=n-r_1\ge n-2p$, so $n=6$, $p=r=2$ is the *unique smallest* configuration with
$\dim V=\dim K=2$ and $V\cap K=0$. In the one-parameter family above, the certificate holds exactly at $t=2$.

## II.6 The obstruction is a system of quadratic conditions (sufficient, not necessary)

At that base ($n=6$, $p=r=2$, $q=3$), let $K^{\perp}$ be an annihilator of $K$ and put
$M_1=K^{\perp}V$, $M_2=K^{\perp}AV$ (both $4\times2$). Then
$$\exists\lambda:\ (\lambda I-A)V=K\iff\exists\lambda:\ \lambda M_1=M_2$$
$$\iff\text{all twelve }2\times2\text{ minors of the two column pairs vanish,\ and the two columns give the same }\lambda .$$
So whole-family infeasibility is *implied* by a system of thirteen **quadratic** conditions on the data, and hence
the infeasible locus is a low-degree algebraic set. L1 + L2: over 2983 instances satisfying the base hypotheses the
implication held in 2981 cases with no false positive, and **failed in 2** — in those, the family fails with
*different* $\lambda$ for different $\mathcal Z$, so no single-$\lambda$ certificate exists. The condition is
therefore sufficient but not necessary.

## II.7 Two degenerate regimes, ruled out

* $\dim V=\dim K=1$ (only possible for $n=p+r+1$): $v\in\ker C$, $Av\in\ker C$ and $k\in\ker C$ with
  $\dim\ker C=2$, so $\det[Av,v,k]\equiv0$ — the scalar certificate is vacuous and the criterion collapses to
  $V\ne K$. Gadgets must start at $\dim V=\dim K\ge2$.
* $n=4$, $p=r=1$ with $\dim V=\dim K=2$: $2p+r=3<4$, so $V\cap K\ne0$ necessarily; no exception-free certificate.

## II.8 Corrections and methodological notes

* "Type III implies $\varepsilon=0$" is false (our own $n=7$ and $n=8$ instances have isolated Type III candidates
  with $\varepsilon\ge1$); withdrawn.
* "The structured search cannot find a second counterexample" was true only of *filtering*; the constructive route
  succeeds (II.3). $\varepsilon=0$ is rare in random data (0 in 6000 at $n=6,p=2,r=2$) but systematic by design.
* Two computer-algebra caveats: gcd over a **two-variable** fraction field returned a wrong answer (a constant where
  the truth was $\lambda+2$); symbolic rank and nullspace also failed where exact numerics worked. All computations
  here use exact rational arithmetic over one variable.
* Performance: the observability test of II.3 (last note) is two orders of magnitude faster than the Toeplitz
  criterion at this size; it is now the default in sweeps.

---

# Part III. Questions

**Q1 (is a reduction plausible at all?).** Given II.4, the infeasible locus is thin; given II.6, it is an intersection
of specific $2\times2$ minors rather than arbitrary quadratics. Do you read this as "a reduction is still possible but
must encode the thin directions" or as "the natural target is the *complement* — deciding that a family is feasible,
i.e. exhibiting witnesses?" If the latter, which known problem has that shape?

**Q2 (restricting the input class).** Since the base $n=6$, $p=r=2$ is the unique smallest non-degenerate
configuration, would it make sense to formulate $q1$ for that fixed parameter size — a "bounded-$(p,r,n)$" version —
and look for hardness there? Our feeling is that a reduction with all parameters fixed would be cleaner, but we do
not know whether the literature treats such "fixed-size" versions of observer-design problems.

**Q3 (the shape of the quadratic system).** The condition is "there exists $\lambda$ such that a linear pencil is
rank $\le1$ on a fixed subspace". Is this shape known in the algebraic-complexity literature under some name
(rank-one pencil problem, or a determinantal feasibility problem)? If it is $\exists\mathbb R$-hard in general, our
problem inherits it on the base; if it is polynomial, our problem cannot be hard for that reason. This single
question seems to decide the direction.

**Q4 (arbitrary gaps).** The second counterexample has gap 2; the first has gap 1. Do you see a way to make the gap
arbitrary by construction? A family with gap $k$ would be a strong structural statement, and it would also give a
"promise" version of $q1$ that might be more approachable than the unrestricted one.

**Q5 (tractable class).** In parallel we could formalise the "counting-spectral separation" class: at every order,
every admissible non-Type-I augmentation is spectrally feasible. The sub-problem is to find a *verifiable* sufficient
condition for that, in terms of the matrices. The single-$\lambda$ certificate of II.5 is one (it is verifiable but
strong). Would you look for a weaker but still verifiable one, and along which invariant (the pair $(U_0,U_1)$, the
quotient pencil $(J_{\mathcal Z},T_{\mathcal Z})$, or the spectrum of the compressed maps)?

**Q6 (next step).** Of the four open threads — (i) the shape question of Q3, (ii) arbitrary gaps of Q4, (iii) the
tractable class of Q5, (iv) attempting a bounded-size reduction (Q2) — which would you do first, and why?

We are not asking for a paper plan; the paper is deferred until there is either a hardness result or a clean
tractability theorem. What we need is a sense of which of these threads has a real chance of terminating.
