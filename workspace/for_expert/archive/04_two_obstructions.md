# Two obstructions to $(5b)$: an integer one and a spectral one

This document is self-contained. It reports the results obtained after the previous exchange and asks seven
questions.

---

# Part I. Setting and notation

For $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$ with $L_0\ne0$ and
$\operatorname{rank}[C;L_0]=p+r$, and a $q\times n$ matrix $\mathcal L$ whose row space contains $\operatorname{row}L_0$:

$$(5a)\ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\ \forall\lambda .$$

$q_{\min}$ is the least such $q$; $q_0$ is the minimum algebraic order (functional-observability indices), and
$\mathrm{DEC}(q)$ is the decision problem. Instances are assumed functionally observable
($\operatorname{row}L_0\subseteq\operatorname{row}\mathcal O_C$, $\mathcal O_C=[C;CA;\dots;CA^{n-1}]$).

Notation: $W=\operatorname{row}[C;CA]$, $r_1=\dim W$; for a full-row-rank $(5a)$-satisfying $\mathcal L$,
$\mathcal Z=\ker[C;\mathcal L]$ (so $\operatorname{row}[C;\mathcal L]=\mathcal Z^\perp$, $\dim\mathcal Z=n-p-q$),
$H=[\mathcal L;CA;C]$, $h=\operatorname{rank}H$, $s=\operatorname{rank}\mathcal L=q$, and $d_{\rm fin}$ is the total
degree of the finite elementary divisors of $Q_{\mathcal L}(\lambda)=[\lambda\mathcal L-\mathcal LA;CA;C]$. The
identity used throughout is
$$(5b)\iff d_{\rm fin}=0\iff\sum_j\varepsilon_j=s,\tag{1}$$
where $\varepsilon_j$ are the left minimal indices of $Q_{\mathcal L}$.

From $(5a)$ one has $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ and hence $Q_{\mathcal L}(\lambda)=D(\lambda)H$ with
$$D(\lambda)=\begin{pmatrix}\lambda I-\Lambda&-G_1&-G_0\\0&I&0\\0&0&I\end{pmatrix}.$$

---

# Part II. Results

## II.1 The conjecture T is false

Earlier we proposed: *at $q=q_0$, $(5b)\iff h<q_0+r_1$.* It is refuted by the following exact counterexample.

Take $n=6$, $p=r=2$,
$$A=\begin{pmatrix}1&1&&&&\\&1&&&&\\&&2&1&&\\&&&2&&\\&&&&1&1\\&&&&&1\end{pmatrix},\quad
C=\begin{pmatrix}0&0&1&1&1&1\\1&0&0&0&0&0\end{pmatrix},\quad
L_0=\begin{pmatrix}0&0&8&20&1&4\\1&3&0&0&0&0\end{pmatrix}.$$
Here $r_1=\operatorname{rank}[C;CA]=4$ and $q_0=3$. The augmentation
$$L=\begin{pmatrix}0&0&8&20&1&4\\1&3&0&0&0&0\\0&0&1/4&1&0&0\end{pmatrix}$$
satisfies $(5a)$, contains $L_0$, has rank $q_0=3$, and
$$h=6<7=q_0+r_1,\qquad k:=q_0+r_1-h=1\le s=3,\qquad \varepsilon=[1],\qquad d_{\rm fin}=2>0 .$$
So $(5b)$ fails although the integer obstruction does not apply.

**Verification** is by three independent routes: the Toeplitz nullity test, the gcd of maximal minors of
$[\lambda\mathcal L-\mathcal LA;CA;C]$, and the nullspace criterion
$\operatorname{rank}[(\lambda I-A)V\mid Z]=\operatorname{rank}[V\mid Z]$ with $V$ spanning $\ker[C;CA]$ and $Z$
spanning $\ker[C;\mathcal L]$.

In a structured family (diagonal with repeated eigenvalues, and Jordan blocks; $p,r\in\{1,2\}$), 17 of 45
sampled augmentations with $h<q_0+r_1$ failed $(5b)$. Hence such failures ("Type III") are common once the
matrix $A$ has repeated eigenvalues or Jordan structure.

## II.2 The value of $h$ is a function of $\mathcal Z$ alone

$$\boxed{\ h=\operatorname{rank}[\mathcal L;CA;C]=\dim\bigl(\mathcal Z^\perp+W\bigr)\ }$$

*Proof.* $h=\dim(\operatorname{row}\mathcal L+W)$. Since $\mathcal Z^\perp=\operatorname{row}[C;\mathcal L]
=\operatorname{row}C+\operatorname{row}\mathcal L$ and $\operatorname{row}C\subseteq W$, we get
$\mathcal Z^\perp+W=\operatorname{row}\mathcal L+W$. $\square$

Consequently, with $\delta:=\dim(\mathcal Z^\perp\cap W)-p\ \ge0$,
$$h=q+r_1-\delta,$$
and the zero-index obstruction (the earlier necessary condition $h<q+r_1$) takes the geometric form
$$(5b)\ \Longrightarrow\ \delta\ge1\iff \mathcal Z^\perp\cap W\supsetneq\operatorname{row}C
\iff \exists\,w\in W\setminus\operatorname{row}C\ \text{with}\ \mathcal Z\subseteq\ker(w^{\mathsf T}).$$
Also, if $q+r_1>n$ then $\dim(\mathcal Z^\perp+W)\le n<q+r_1$, so the integer obstruction cannot apply at all:
it can only occur for $q\le n-r_1$.

Verified on 240 sampled pencils (360 in a second run), with no exception.

## II.3 Why the published two-order-gap example fails at $q_0+1$: a structural reason

For the published example ($n=8$, $p=r=2$, $r_1=4$, $q_0=3$) at $q=4$ we have $q+r_1=8=n$, hence
$\dim(\mathcal Z^\perp+W)\le n=q+r_1$ and therefore $\delta=0$, i.e. $h=q+r_1=8$ always. So the failure at $q=4$
is the integer obstruction, forced by $h=n$. At $q=5$ one finds $\dim(\mathcal Z^\perp\cap W)=3$, hence $\delta=1$,
$h=8<9$, and $(5b)$ holds.

Numerically: at $q=4$, 2000 random admissible samples all have $h=8$ (1999 admissible ones), and at $q=5$ all 40
samples succeed. The example therefore satisfies $h=\min(q+r_1,n)$ for the orders examined, which forces failure
for all $q\le n-r_1=4$ and gives $q_{\min}=n-r_1+1=5$.

**Caveat.** $h=\min(q+r_1,n)$ is *not* a general identity: the instance with $n=6$, $p=2$, $r=1$, $q_0=1$ has
$r_1=4$ and $h=4<\min(5,6)$.

## II.4 When $(5a)$ is automatic

$$\boxed{\ h=n\ \Longrightarrow\ (5a)\ \text{holds for every}\ \mathcal L\ \text{with}\ \operatorname{row}[C;\mathcal L]=\mathcal Z^\perp .}$$

Indeed $h=n$ means $\mathcal Z^\perp+W=\mathbb C^n$, so $\ell A\in\mathcal Z^\perp+W$ for every $\ell$.

Verified on 117 sampled cases with $h=n$, without exception. This explains why in the published example at
$q=4,5$ every constructed augmentation satisfies $(5a)$.

## II.5 A computable criterion for $(5a)$

$$(5a)\iff \operatorname{row}\mathcal L\subseteq G_{\mathcal Z},\qquad
G_{\mathcal Z}:=\{\ell\in\mathcal Z^\perp:\ \ell A\in\mathcal Z^\perp+W\}.$$

$G_{\mathcal Z}$ is the kernel of the quotient map
$$\varphi:\mathcal Z^\perp\longrightarrow\mathbb C^n/(\mathcal Z^\perp+W),\qquad \ell\mapsto \ell A\ \mathrm{mod}\ (\mathcal Z^\perp+W),$$
so $\dim G_{\mathcal Z}=(p+q)-\operatorname{rank}\varphi$, and a necessary condition for the existence of an
$(5a)$-satisfying $\mathcal L$ with the given $\mathcal Z$ is
$$\dim G_{\mathcal Z}\ge q\iff \operatorname{rank}\varphi\le p .$$

Note that $(5a)$ depends on the actual rows of $\mathcal L$, not only on $\mathcal Z$: an earlier claim of ours to
the contrary was wrong (it was based on examples where $h=n$, so that $(5a)$ was automatic by II.4). With
$\dim G_{\mathcal Z}=q$ there are $\mathcal Z$ for which no randomly chosen complement of $\operatorname{row}C$ in
$\mathcal Z^\perp$ satisfies $(5a)$.

Constructing $\mathcal L$ inside $G_{\mathcal Z}$ is much more efficient than drawing arbitrary complements: over
89 functionally observable instances at $q=q_0$ we obtain

| outcome | instances |
|---|---|
| $(5b)$ witnessed at $q_0$, so $q_{\min}=q_0$ exactly | 38 |
| candidates exist but all fail (only $q_{\min}\ge q_0+1$) | 29 |
| no candidate (either $d=0$ or every $\mathcal Z$ violates the necessary condition) | 22 |

The number of $\mathcal Z$ satisfying the necessary condition varies between 2 and 79 across instances, so the
"thickness" of the algebraically admissible family is itself a structural quantity.

## II.6 Where the spectral obstruction can occur

Since $Q_{\mathcal L}=D(\lambda)H$ and $D(\lambda)$ is invertible unless $\lambda$ is an eigenvalue of $\Lambda$,
$$\lambda\notin\operatorname{spec}\Lambda\ \Longrightarrow\ \operatorname{rank}Q_{\mathcal L}(\lambda)=h .$$
Hence $(5b)$ need only be tested on $\operatorname{spec}\Lambda$, equivalently
$$(5b)\iff \operatorname{im}H\cap J\ker(\lambda I-\Lambda)=\{0\}\ \ \forall\lambda,\qquad Jv=(v,0,0).$$
The eigenvalues of $\Lambda$ can be complex: in one of the sampled counterexamples the obstructing divisor is a
quadratic with no real root. So scanning rational (or real) values of $\lambda$ is not a decision procedure.

## II.7 The gap between $q_0$ and $q_{\min}$

| instance | $n,p,r$ | $q_0$ | $q_{\min}$ | gap | mechanism at the failing orders |
|---|---|---|---|---|---|
| published example | $8,2,2$ | 3 | 5 | 2 | integer ($h=q+r_1=n$) |
| diagonal with distinct eigenvalues | $7,2,1$ | 2 | 4 | 2 | integer ($h\ge q+r_1$) |
| counterexample of II.1 | $6,2,2$ | 3 | 4 | 1 | **spectral** ($h<q+r_1$ but $d_{\rm fin}>0$) |

So the *size* of the gap and the *mechanism* of the failure are independent: gaps of one and of two occur with
both mechanisms.

## II.8 What is not claimed

* $(5b)$ at fixed $\mathcal L$ is decided by the Toeplitz nullity or by the gcd; both are exact.
* The identity $h=\dim(\mathcal Z^\perp+W)$ and the implication $h=n\Rightarrow(5a)$ are proved; the rest of
  II.5 is verified on samples.
* The numbers in II.5 are statistics over a chosen instance family, not an estimate of a probability.
* No complexity statement: $\mathrm{DEC}(q)$ is still only known to be in $\exists\mathbb R$. Refuting the earlier
  conjecture removes the hope that $\mathrm{DEC}(q_0)$ reduces to integer data.

---

# Part III. Questions

**Q1.** Is the phenomenon of II.1 known? At the minimum algebraic order, an augmentation can fail $(5b)$ while the
integer obstruction does not apply. We have an exact example with $n=6$ and Jordan structure in $A$; the literature's
examples of failure at $q_0$ are, as far as we can see, also of this kind, but we have not verified whether the
*reason* there is the same.

**Q2.** Is the identity $h=\dim(\mathcal Z^\perp+W)$ stated anywhere? It is elementary, but it makes $h$ a function
of the nullspace alone, which seems the natural way to organise the fixed-order problem.

**Q3.** Is the dichotomy "integer obstruction ($\delta=0$) versus spectral obstruction ($\delta\ge1$)" the right way
to organise failures? If so, is anything known about the set of $\mathcal Z$ with $\delta\ge1$ for which the
spectral condition still fails?

**Q4.** The necessary condition $\operatorname{rank}\varphi\le p$ (with $\varphi:\mathcal Z^\perp\to\mathbb C^n/
(\mathcal Z^\perp+W)$ induced by $A$) — is it recognisable as a Schubert-type condition on $\mathcal Z$? If so, is
there a known formula for the class (or the number) of admissible $\mathcal Z$? In our samples this count varies
between 2 and 79 over 89 instances.

**Q5.** In one of the sampled counterexamples the obstructing eigenvalue is not real. Is there a standard way to
treat complex eigenvalues in this problem, or is the intended approach always to work with the gcd of maximal
minors (which is root-free)?

**Q6.** With the earlier conjecture refuted, is the target "characterise the smallest $k$ with an order-$(q_0+k)$
augmentation satisfying $(5b)$" still the right main line? Or would you now put the identity of II.2, together with
the two-obstruction dichotomy, at the centre?

**Q7.** Which of the present results would you regard as publishable now, and in what order? We have: the Toeplitz
criterion for a fixed augmentation (with independent verification), the identity of II.2, the automatic-$5a$
statement of II.4, the counterexample of II.1, and the reproduced two-order-gap example with its structural
explanation.

---

# Part IV. State in brief

* $(5b)$ at a fixed augmentation: decided by one Toeplitz matrix, independently by the gcd of maximal minors.
* $h=\dim(\mathcal Z^\perp+W)$; hence the integer obstruction is $\delta=0$, and it can occur only for $q\le n-r_1$.
* The published two-order-gap example fails at $q_0+1$ because $h=n$ there; the mechanism is integer, not spectral.
* Spectral failures at the minimum order exist (counterexample of II.1); they are common with repeated eigenvalues.
* $q_{\min}=q_0$ was certified for 38 of 89 instances; in 29 further instances only a lower bound is available.
* Complexity of $\mathrm{DEC}(q)$: open; only $\in\exists\mathbb R$ is known.
