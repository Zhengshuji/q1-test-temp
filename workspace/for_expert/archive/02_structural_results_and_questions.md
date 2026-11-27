# Structural results on the spectral condition, and six questions

This document is self-contained. It reports results obtained after the previous report and asks six
questions.

---

# Part I. Problem and notation

Let $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$
(with $L_0\neq0$, $\operatorname{rank}[C;L_0]=p+r$). For a $q\times n$ matrix $\mathcal L$ containing
$L_0$ in its row space,

$$(5a)\quad \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\quad \operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\ \ \forall\lambda .$$

$q_{\min}(A,C,L_0)=\min\{q:\exists\,\mathcal L\ (q\times n),\ \operatorname{row}L_0\subseteq\operatorname{row}\mathcal L,\ (5a)\wedge(5b)\}$;
$\mathrm{DEC}(q)$ is the corresponding decision problem.

**Kronecker data.** For $\mathcal L$ satisfying $(5a)$, let
$Q_{\mathcal L}(\lambda)=[\lambda\mathcal L-\mathcal LA;\;CA;\;C]$, $h=\operatorname{rank}Q_{\mathcal L}$ (normal rank),
$s=\operatorname{rank}\mathcal L$, $m=q+2p-h$ (the number of left minimal indices),
$\varepsilon_1\ge\cdots\ge\varepsilon_m\ge0$ the left minimal indices,
$d_{\rm fin}$ the total degree of the finite elementary divisors. The following was established earlier
and is used throughout:

$$(5b)\iff d_{\rm fin}=0\iff \sum_{j}\varepsilon_j=s .\tag{1}$$

Two further quantities are used below:

* $r_1:=\operatorname{rank}[C;CA]$;
* $\mathrm{cl}(A,C,L_0):=\min\{\dim V:\ \operatorname{row}L_0\subseteq V,\ VA\subseteq V+\operatorname{row}[C;CA]\}$,
  the **minimum row count for $(5a)$ alone**. Equivalently, $(5a)$ is the inclusion
  $\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}\mathcal L+\operatorname{row}[C;CA]$.

Throughout, an instance is called **functionally observable** if $\operatorname{row}L_0\subseteq\operatorname{row}\mathcal O_C$
with $\mathcal O_C=[C;CA;\dots;CA^{n-1}]$; this is the standing assumption for existence in the literature.

---

# Part II. Results

## II.1 The single-Toeplitz criterion (from the earlier exchange): adopted and verified

For $d\ge0$ let $T_d$ be the block Toeplitz matrix of the system $R(\lambda)y(\lambda)=0$, $\deg y\le d$,
where $R(\lambda)=[\lambda E-E\Lambda^{\mathsf T}\ \,B]$ is the reduced descriptor pencil, and set
$\nu_d=\dim\ker T_d$. Then

$$\nu_d=\sum_{j}\max\{0,d-\varepsilon_j+1\},\qquad
\#\{j:\varepsilon_j=d\}=\nu_d-2\nu_{d-1}+\nu_{d-2},\qquad
(5b)\iff \nu_s=(s+1)m-s .$$

**Verification.** On 66 $(5a)$-satisfying pencils ($n=6,7,8$) the sequence recovered from
$\nu_0,\dots,\nu_s$ coincides with the one computed from Smith forms of $Q_{\mathcal L}$
(66/66), and the criterion agrees in 66/66 cases. The criterion requires only one constant matrix
(of size $h(s+2)\times(q+2p)(s+1)$); no Smith form is needed. It is used for all evaluations reported below.

## II.2 The $(5a)$-minimum $\mathrm{cl}$ and its role

$V_{\min}$ is computed by the standard closure: start from $\operatorname{row}L_0$ and add $xA$ for
$x\in V$ whenever $xA\notin V+\operatorname{row}[C;CA]$, until closed. This is polynomial-time and gives the
**exact** minimum: every $(5a)$-satisfying $\mathcal L$ has $\operatorname{row}\mathcal L\supseteq V_{\min}$.

Consequences used below:

* $q_{\min}\ge\mathrm{cl}$ (since $(5b)$-solutions are $(5a)$-solutions);
* at $q=\mathrm{cl}$ there is **exactly one** $(5a)$-satisfying row space (equal to $V_{\min}$;
  different matrices with this row space differ only by rows of $\operatorname{row}C$ and have the same
  $(5b)$ verdict). Hence the question "does $(5b)$ hold at the minimal order" is a **single** yes/no
  structural question, not a search.

This quantity is not a claim about $(5a)$ (which is settled); it is used as the baseline that makes the
"cost of $(5b)$" measurable.

## II.3 Theorem B.9: zero left indices, and a necessary condition

**Lemma 1.** The space of *constant* left null vectors of $Q_{\mathcal L}$ has dimension $2p-r_1$.
Indeed, writing $\varphi=(\varphi_1,\varphi_2,\varphi_3)$, the coefficient of $\lambda$ gives
$\varphi_1\mathcal L=0$; since $\mathcal L$ has full row rank, $\varphi_1=0$; the constant term then gives
$(\varphi_2,\varphi_3)\in\ker_{\rm left}[CA;C]$, of dimension $2p-r_1$.

**Lemma 2.** $\#\{j:\varepsilon_j=0\}=2p-r_1$ and $\#\{j:\varepsilon_j>0\}=q+r_1-h$.
(The degree-zero elements of a minimal left basis span exactly the constant left null vectors.)

**Corollary B.9.**
$$\boxed{(5b)\ \Longrightarrow\ h<q+r_1 .}$$
For if $h\ge q+r_1$ there is no nonzero left index, so $\sum_j\varepsilon_j=0$; by (1),
$d_{\rm fin}=s=\operatorname{rank}\mathcal L>0$, and $(5b)$ fails.

**Verification.** On 56 functionally observable instances ($n=5,6$; $p,r\in\{1,2\}$) the three counting
identities (number of left indices $=q+2p-h$, number of zeros $=2p-r_1$, number of nonzero $=q+r_1-h$)
and B.9 hold without exception; B.9 is triggered 16 times and in all 16 cases $d_{\rm fin}>0$.

B.9 is a cheap necessary condition: it uses only the three integers $q,r_1,h$. It is complementary to the
complementary-obstruction theorem (which is a sufficient failure condition and can occur only at
$q=n-r_1$).

## II.4 The converse of B.9 fails

"$h<q+r_1$ is sufficient" is **false**: among 912 $(5a)$-satisfying pencils obtained by adding vectors from
the one-step preimages of $V_{\min}$, **415** satisfy $h<q+r_1$ but have $d_{\rm fin}>0$. Minimal example
($n=5$, $p=r=1$, $q=4$): $h=5$, $r_1=2$, $\varepsilon=[3]$, $s=4$, $d_{\rm fin}=1$. Here the count of nonzero
left indices is $q+r_1-h=1$, as B.9 predicts, but its value is $3<s=4$.

The structural reason: B.9 counts the nonzero left indices, whereas $(5b)$ requires their **sum** to equal $s$.

## II.5 Experiment: $q_{\min}$ versus $\mathrm{cl}$

Instances are generated with sparse integer data ($A\in\{0,\pm1\}^{n\times n}$, $C$ sparse, and
$L_0$ taken from rows of $[C;CA;CA^2]$ so that functional observability holds automatically).
56 functionally observable instances ($n=5,6$; $p,r\in\{1,2\}$; ten seeds each).

For each instance the orders $q=\mathrm{cl},\mathrm{cl}+1,\mathrm{cl}+2$ were examined; at each order,
$(5a)$-satisfying augmentations were built from $V_{\min}$ by adding vectors from one-step preimages
(each step is exact linear algebra; every sample is asserted to be full-row-rank, to contain $L_0$, and to
satisfy $(5a)$), and $(5b)$ was tested by the Toeplitz criterion.

| relation | instances |
|---|---|
| $q_{\min}=\mathrm{cl}$ (the unique minimal candidate satisfies $(5b)$) | **40** |
| $q_{\min}=\mathrm{cl}+1$ (minimal candidate fails; explicit witness one order higher) | **14** |
| unresolved (no witness at $\mathrm{cl}+1$) | 2 |

Two observations:

1. The guess $q_{\min}=\mathrm{cl}+1$ suggested by an earlier, denser instance family is **false**
   (40 counterexamples). The instance family matters: with $L_0$ a dense combination of rows of
   $\mathcal O_C$, $\mathrm{cl}=3$ and the minimal candidate always failed; with $L_0$ a single row of
   $[C;CA;CA^2]$, $\mathrm{cl}\in\{1,2\}$ and the minimal candidate usually succeeds.
2. The surviving empirical statement is $q_{\min}\in\{\mathrm{cl},\ \mathrm{cl}+1\}$ (54 of 56 instances;
   the 2 remaining are undecided). **This is not proved.**

## II.6 $(5b)$ is a genuine existential condition over the family

For a fixed instance and fixed $q$, different augmentations give different verdicts. Example
($n=5$, $q=3$, two augmentations containing $L_0$ and both satisfying $(5a)$): one has $\varepsilon=[]$
and $d_{\rm fin}=3$ (fails), the other has $\varepsilon=[3]$ and $d_{\rm fin}=0$ (holds). In a scan over
23 instance-order groups, 3 groups contained augmentations with opposite verdicts. Hence the verdict is not a
function of the aggregate data $(q,p,h,\operatorname{rank}\mathcal L)$.

## II.7 What is not claimed

* $q_{\min}\in\{\mathrm{cl},\mathrm{cl}+1\}$ is an empirical statement over 56 instances, not a theorem.
* $h<q+r_1$ is necessary, not sufficient (see II.4).
* No complexity statement is made: $\mathrm{DEC}(q)$ is still only known to lie in $\exists\mathbb R$.

---

# Part III. Questions

**Q1.** For the minimal $(5a)$-augmentation (the closure $V_{\min}$), is any criterion for $d_{\rm fin}=0$
known other than computing the Kronecker data? In particular, is it known which structural features make
the minimal augmentation fail? (In our data, failure happens exactly when $h\ge q+r_1$, or — for 415
further pencils at larger orders — when the single nonzero left index is smaller than $s$.)

**Q2.** Is the quantity $\mathrm{cl}$ (minimum row count for $(5a)$ alone) the same as $\sum_j\eta_j$ as
defined in the functional-observability-indices literature? We find instances where the closure has
dimension $4$ or $5$ while a straightforward implementation of the rank-preserving selection over the
generators gives $3$. If these are different quantities, is the difference documented (functional dimension
versus row count), and which of them is the one appearing in the order spectrum?

**Q3.** Is the statement $q_{\min}\in\{\mathrm{cl},\mathrm{cl}+1\}$ consistent with the known order spectrum
of functional observers? If the spectrum is an interval $[\nu_{\min},n_0-p]$, this would say
$\nu_{\min}-\mathrm{cl}\le1$. Is a larger gap known (or known to be impossible)?

**Q4.** Which structural feature would produce $q_{\min}\ge\mathrm{cl}+2$? We ask for a candidate
mechanism, so that a counterexample can be searched deliberately rather than by sampling.
(Our failures at the minimal order are explained by B.9; the unresolved question is what can force a
second extra row.)

**Q5.** The zero-index count in B.9 (exactly $2p-r_1$ left indices equal to zero, coming from the constant
left null vectors of $[CA;C]$) — is this standard in the matrix-pencil literature, or is it worth stating
explicitly? It affects how the sum in (1) should be counted.

**Q6.** Methodologically: the set of augmentations satisfying $(5b)$ appears to be thin (zero measure in
the natural parametrisation). Is a Gröbner/resultant treatment of the exceptional set feasible at small
$n$, or is the recommended route the geometric one (irreducibility of the family, generic feasibility on
each irreducible component)?

---

# Part IV. Short summary of the state

* For fixed $\mathcal L$, $(5b)$ is decided by one Toeplitz matrix (verified, 66/66), and equivalently by
  $d_{\rm fin}=0$ / $\sum\varepsilon=s$.
* For the minimal $(5a)$-augmentation, $(5b)$ is a single structural question; the one proved necessary
  condition is $h<q+r_1$ (B.9).
* Empirically, over 56 functionally observable instances, $q_{\min}$ equals $\mathrm{cl}$ (40) or
  $\mathrm{cl}+1$ (14), with 2 undecided; the stronger equality $q_{\min}=\mathrm{cl}+1$ is false.
* Complexity of $\mathrm{DEC}(q)$: open; only $\in\exists\mathbb R$ is known.
