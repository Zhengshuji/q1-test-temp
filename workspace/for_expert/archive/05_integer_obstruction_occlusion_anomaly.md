# Two obstructions, a boundary, and a case with no admissible order

This document is self-contained. It reports work done since the previous note, states one anomaly that we cannot
resolve without help, and asks six questions. The materials needed to check every claim are displayed here.

---

# Part I. Setting

For $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$ with $L_0\ne0$ and
$\operatorname{rank}[C;L_0]=p+r$, and a $q\times n$ matrix $\mathcal L$ whose row space contains $\operatorname{row}L_0$:

$$(5a)\ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\quad\forall\lambda\in\mathbb C .$$

$q_0$ is the least $q$ for which $(5a)$ has a solution; $q_{\min}$ is the least $q$ for which both hold.

Notation. $W=\operatorname{row}[C;CA]$, $r_1=\dim W$; $\mathcal Z=\ker[C;\mathcal L]$ (so $\operatorname{row}[C;\mathcal L]=\mathcal Z^\perp$
and $\dim\mathcal Z=d=n-p-q$); $h=\operatorname{rank}[\mathcal L;CA;C]$; $d_{\rm fin}$ is the total degree of the finite
elementary divisors of $Q_{\mathcal L}(\lambda)=[\lambda\mathcal L-\mathcal LA;CA;C]$. Two facts are used repeatedly:

$$(5b)\iff d_{\rm fin}=0;\qquad h=\dim(\mathcal Z^\perp+W).\tag{1}$$

(The second identity: $\operatorname{row}\mathcal L+W=\mathcal Z^\perp+W$ because $\operatorname{row}C\subseteq W$.)

Two settings are used below:

$$V=\ker[C;CA],\qquad K=\ker[C;L_0],\qquad S=\operatorname{row}[C;L_0]+W,\qquad s_0=\dim S .$$

---

# Part II. Results

## II.1 The failure type is decided by integers

Fix an order $q$ and write $t=q-r$. For any $(5a)$-satisfying $\mathcal L$ one has $\mathcal Z^\perp=K^\perp+V'$ with
$V'$ a $t$-dimensional complement of $K^\perp$ inside $\mathcal Z^\perp$, and (1) gives
$$h=\dim(S+V')=s_0+\dim\pi(V'),\qquad \pi:\mathbb C^n\to\mathbb C^n/S .$$
Hence
$$\text{integer obstruction }(h\ge q+r_1)\iff \dim\pi(V')\ge q+r_1-s_0 .$$
When $V'\cap S=0$ (equivalently $\dim\pi(V')=t$) this becomes
$$h\ge q+r_1\iff s_0\ \ge\ r_1+r,$$
which does **not** depend on the particular $\mathcal L$: on such an order, either every admissible augmentation
fails by the integer obstruction, or none does.

**Verification.** On 495 sampled admissible augmentations, $h=s_0+q-r$ held in every case where $V'\cap S=0$
(no exception); the identity $h=\dim(\mathcal Z^\perp+W)$ was checked separately on 360 samples.

## II.2 The published two-order-gap example fails by the integer obstruction at both orders

For the example of Fernando 2026 (arXiv:2609.37992), $n=8$, $p=r=2$, $r_1=4$, $q_0=3$, one computes
$s_0=6$.

* At $q=3$: $t=1$ and $q+r_1=7=s_0+t$, so $h=7=q+r_1$ for every admissible augmentation. This is a proof
  (see II.3 below for the mechanism), and we can also exhibit an admissible augmentation explicitly:
  with $x$ ranging over $V$, $\lambda(x)=L_0Ax/L_0x$ and $z(x)=(\lambda(x)I-A)x\in K$; one solution is
  $$v=\Big(-\tfrac{42919}{32067},\ -\tfrac{55096}{10689},\ 1,0,0,0,0,0\Big),\qquad
  \mathcal L=\begin{pmatrix}L_{0,1}\\ L_{0,2}\\ v\end{pmatrix},$$
  for which $(5a)$ holds, $h=7=q+r_1$, $\varepsilon=[\,]$, $d_{\rm fin}=3$, so $(5b)$ fails.
* At $q=4$: $h=8=q+r_1$ on 1999 of 2000 admissible samples.
* At $q=5$: $\dim\pi(V')\le n-s_0=2<t=3$, hence $h\le8<9=q+r_1$: the integer obstruction is impossible, and a
  feasible augmentation exists.

So the order spectrum of that example has a purely integer explanation, and its failures are of the integer type
at both orders.

## II.3 Whole-family infeasibility: the occlusion argument

Let $q$ be an order with $h=n$ (then $(5a)$ holds for every $\mathcal L$, since $\mathcal Z^\perp+W=\mathbb C^n$).
For $x\in V$ with $L_0x\ne0$ put $\lambda(x)=L_0Ax/L_0x$ and $z(x)=(\lambda(x)I-A)x$. Then
$$Cz(x)=\lambda(x)Cx-CAx=0,\qquad L_0z(x)=\lambda(x)L_0x-L_0Ax=0,$$
so $z(x)\in K$, and if $\mathcal Z=\operatorname{span}z(x)$ then
$$\big[\lambda(x)\mathcal L-\mathcal LA;CA;C\big]\,x=0\quad\text{with }x\ne0,$$
i.e. $\operatorname{rank}Q_{\mathcal L}(\lambda(x))<h$ and $(5b)$ fails. Consequently: **if the map
$\Phi:\mathbb P(V)\dashrightarrow\mathbb P(K)$, $x\mapsto\operatorname{span}z(x)$, is surjective, then every
$\mathcal Z$, hence every admissible augmentation, fails $(5b)$.**

$\Phi$ is a rational map between projective spaces, so it extends to a morphism; a nonconstant map
$\mathbb P^1\to\mathbb P^1$ is surjective. For the counterexample of the previous note (an instance with $n=6$,
$p=r=2$, $q_0=3$, where $r_1=p+r=4$ and $\dim V=\dim K=2$) the map is nonconstant — for instance
$t=0$ gives $[12/5:0]$ and $t=-2$ gives $[4:-4]$ — hence surjective, and the whole family at $q_0$ fails. This is
a proof, not a sample: the same instance has $s_0=5$, $t=1$, hence $h=s_0+t=6=n$, so $(5a)$ is automatic there.

## II.4 How often does the spectral obstruction occur?

We generated random integer instances with $n=5,\dots,9$, $p,r\le3$, and kept only those where, at $q=q_0$, the
integer obstruction is impossible ($s_0+\min(t,n-s_0)<q+r_1$). Results:

| family | instances | admissible samples | with $(5b)$ | whole family failing |
|---|---|---|---|---|
| random, $n=5,6,7$ | 67 | 1501 | 1501 | 0 |
| random, $n=7,8,9$ | 37 | 959 | 921 | 3 |

In the larger family, the three failures all satisfy $r_1=p+r$; the breakdown is

| relation | instances | feasible | whole family failing |
|---|---|---|---|
| $r_1<p+r$ | 12 | 12 | 0 |
| $r_1=p+r$ | 17 | 14 | 3 |
| $r_1>p+r$ | 8 | 8 | 0 |

So the spectral (non-integer) obstruction was only observed on the boundary $r_1=p+r$, i.e. when
$\dim V=\dim K$ and $\Phi$ may be a self-map of the same projective space. In two of the three failing instances
$\dim K=d$, so the admissible family is a single point and the verdict is decided by one gcd computation.

## II.5 An instance with no admissible order

While turning the above into a per-order decision procedure we met the following instance, which we cannot
reconcile with the existence statements we know. Take $n=7$, $p=2$, $r=2$,

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
L_0=\begin{pmatrix}-1&0&0&0&-1&0&0\\ 1&0&0&0&0&0&1\end{pmatrix}.$$

For this instance $q_0=2$, $r_1=\operatorname{rank}[C;CA]=4$, and functional observability holds in the usual
sense: $\operatorname{rank}\mathcal O_C=\operatorname{rank}[\mathcal O_C;L_0]=5$, so
$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal O_C$.

Nevertheless, no admissible augmentation exists at any order:

| order $q$ | situation | candidates examined | satisfying $(5b)$ | $h$ | $q+r_1$ |
|---|---|---|---|---|---|
| 2 ($=r$; the family is the single point $\mathcal L=L_0$) | one point | — | 0 | 6 | 6 |
| 3 | $Z$-parametrisation | 3 | 0 | 6 | 7 |
| 4 | $Z$-parametrisation | 54 | 0 | 6–7 | 8 |
| 5 ($=n-p$; $d=0$) | complements of $\operatorname{row}C$ | 400 | 0 | 7 | 9 |

At $q=5$ the gcd of the maximal minors is $\lambda$, i.e. the rank drops at $\lambda=0$; the Toeplitz nullity test
gives the same verdict. Two further observations:

* dropping the requirement $\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$ does not help: 300 random
  complements of $\operatorname{row}C$ in $\mathbb C^7$ also all fail $(5b)$ at $q=5$;
* $A$ has two zero rows ($\operatorname{rank}A=5$), so $\lambda=0$ is an eigenvalue with a two-dimensional kernel.

Three explanations are conceivable, and we cannot decide between them from the material at hand:
(i) the condition $(5b)$ is meant to be checked only on a subset of $\mathbb C$ (for instance excluding $\lambda=0$,
or only at the eigenvalues of $A$ in some formulation), and our reading is too strong;
(ii) the existence statements carry an extra hypothesis that this instance violates (e.g. $\det A\ne0$);
(iii) one of our checks is wrong — though three independent tests agree on the instances where they were compared,
and the same code produces witnesses on many other instances (38 instances with a certified $q_{\min}=q_0$).

## II.6 Summary of the picture we now have

$$\text{failure at order }q\iff\underbrace{h\ge q+r_1}_{\text{integer, decided by }s_0,\ \pi(V')}\ \text{or}\ \underbrace{h<q+r_1,\ d_{\rm fin}>0}_{\text{spectral}} .$$

The integer part is decided by integers (II.1). The spectral part, in all instances we examined, is an occlusion
phenomenon (II.3): the bad points $\Phi(\mathbb P(V))$ meet every admissible $\mathcal Z$; it was observed only
on the boundary $r_1=p+r$ (II.4). And II.5 shows that on some instances the spectral part is total, i.e. no order
works.

---

# Part III. Questions

**Q1 (the anomaly of II.5).** For that instance functional observability holds and yet no order admits a
$(5a)\wedge(5b)$ augmentation. That contradicts the existence statements we are aware of. Is $(5b)$ in the intended
formulation required for all $\lambda\in\mathbb C$, including $\lambda=0$? Is an extra hypothesis (nonsingularity
of $A$, or detectability of the zero eigenvalue, or $r_1\ge p+r-1$, or something else) part of the existence
theorem? If our reading is correct, is this instance a counterexample to that theorem?

**Q2 (the integer criterion).** Is the criterion of II.1 — $h=s_0+\dim\pi(V')$, hence failure by the integer
obstruction iff $\dim\pi(V')\ge q+r_1-s_0$, and on orders with $V'\cap S=0$ iff $s_0\ge r_1+r$ — equivalent to a
condition already in the literature? It removes the augmentation from the question, so it ought to be visible
somewhere.

**Q3 (the boundary $r_1=p+r$).** In our samples the spectral obstruction occurs only when $r_1=p+r$. Is there a
reason for this? On the boundary $\dim V=\dim K$, which is what allows the map $\Phi$ to be dominant; off the
boundary we found no failure at all. Is this an artefact of the instance families we used, or is it structural?

**Q4 (the occlusion mechanism).** Is the mechanism of II.3 — "the bad points $\Phi(\mathbb P(V))$ meet every
admissible $\mathcal Z$" — a known way to exclude an order? It seems to be the natural obstruction after the
integer one is removed, but we have not seen it stated.

**Q5 (what to do next).** Given that the integer obstruction is fully decided, and the spectral one appears only
on the boundary and only sometimes, where would you put the effort: (a) proving that off the boundary the spectral
condition can always be met; (b) deciding occlusion algorithmically on the boundary; (c) resolving II.5, which
affects the formulation itself?

**Q6 (what is worth writing up).** Which of the following would you regard as worth a note now: the integer
criterion of II.1 together with the pure-integer explanation of the published example (II.2); the whole-family
infeasibility argument of II.3 with its instance; the boundary observation of II.4; or the anomaly of II.5 pending
its resolution?

---

# Part IV. State in brief

* $(5b)$ at a fixed augmentation: decided by a Toeplitz nullity test and independently by the maximal-minor gcd.
* $h=\dim(\mathcal Z^\perp+W)=s_0+\dim\pi(V')$; this decides the integer obstruction with integers alone.
* The published example fails at $q_0$ and $q_0+1$ by the integer obstruction ($h=q+r_1$ at both).
* Spectral failures at $q_0$ exist and can be proved total for a given instance (occlusion, II.3).
* In random instances the spectral failure was observed only on the boundary $r_1=p+r$ (3 of 17 instances there,
  0 of 20 elsewhere).
* One instance (II.5) is functionally observable yet appears to admit no order; this is the open point.
