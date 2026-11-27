# Minimum order versus the algebraic minimum: results, one conjecture, and seven questions

This document is self-contained. It reports the work done after the previous exchange and asks six
questions.

---

# Part I. Setting and notation

For $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$ with
$L_0\ne0$, $\operatorname{rank}[C;L_0]=p+r$, and a $q\times n$ matrix $\mathcal L$ containing $L_0$ in its row space,

$$(5a)\ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\ \forall\lambda .$$

$q_{\min}$ is the least $q$ admitting such an $\mathcal L$; $\mathrm{DEC}(q)$ is the decision problem.
An instance is **functionally observable** if $\operatorname{row}L_0\subseteq\operatorname{row}\mathcal O_C$,
$\mathcal O_C=[C;CA;\dots;CA^{n-1}]$; this is the standing existence assumption.

For a $(5a)$-satisfying $\mathcal L$ put
$h=\operatorname{rank}[\mathcal L;CA;C]$, $s=\operatorname{rank}\mathcal L$,
$r_1=\operatorname{rank}[C;CA]$, $m=q+2p-h$ (number of left minimal indices), $\varepsilon_j$ the left minimal
indices, $d_{\rm fin}$ the total degree of the finite elementary divisors. The identity used throughout is
$$(5b)\iff d_{\rm fin}=0\iff\sum_j\varepsilon_j=s .\tag{1}$$

$q_0=\sum_j\eta_j$ denotes the minimum algebraic order (functional-observability indices); it is computable in
polynomial time. The two quantities used below are
$$\mathrm{cl}_{\rm clos}:=\dim V_{\min},\quad V_{\min}=\text{least }V\supseteq\operatorname{row}L_0,\ VA\subseteq V+\operatorname{row}[C;CA],$$
computed by greedy closure, and the "closure" of one-step preimages used to generate candidates.

---

# Part II. Results

## II.1 Correction: the greedy closure is not the minimum

The greedy closure adds the vector $xA$ itself, not its class modulo $W=\operatorname{row}[C;CA]$; since
$xA\in U+W$ does not imply $xA\in U$, it can add too many rows. On the published example (below) it gives
$4$ while $q_0=3$. **$q_0$ is the authority**; all statements phrased in terms of $\mathrm{cl}_{\rm clos}$ in the
previous report are superseded.

## II.2 The published two-order-gap example, reproduced

For the example of Section VII of the 2026 paper ($n=8$, $p=r=2$, $(A,C)$ observable, $\eta=(2,1)$, $q_0=3$,
$\nu_{\min}=5$):

| item | value |
|---|---|
| published order-5 augmentation $\mathcal L_5$ | satisfies $(5a)$, $(5b)$; $h=8$, $s=5$, $r_1=4$, $\varepsilon=[5]$, $d_{\rm fin}=0$ |
| order $q=4$, 40 augmentations obtained from the nullspace parametrisation | all satisfy $(5a)$; **none** satisfies $(5b)$ |
| order $q=5$, 40 augmentations | all satisfy $(5a)$ and $(5b)$ |
| order $q=6$ | feasible |

This reproduces $\nu_{\min}=q_0+2=5$ within our framework, and the failure at $q=4$ is now checked on 40
independent admissible augmentations rather than 20.

A further observation identifies the mechanism at $q=4$: **all 40 admissible augmentations have
$h=8=q+r_1$**, i.e. the admissible family at that order is confined to the hypersurface $h=q+r_1$, where the
zero-index obstruction (Section II.3) forbids $(5b)$. At $q=5$ the family leaves that hypersurface
($h=8<q+r_1=9$) and $(5b)$ holds for all 40 samples.

**Order $q=c$ is a thin set.** At $q=q_0$ the condition $(5a)$ is a proper subvariety of the chart: 0 of 240
random candidates and 0 of 500 grid points on all four Grassmann charts of $\mathrm{Gr}(3,4)$ satisfy $(5a)$.
Hence **sampling cannot decide the minimum order**; an algebraic (elimination) treatment is required.

## II.3 Strengthened necessary conditions (proved)

Combining the zero-index count with integrality:

**Lemma 1.** For a full-row-rank $(5a)$-satisfying $\mathcal L$, the pencil $Q_{\mathcal L}$ has exactly
$2p-r_1$ left indices equal to $0$, hence $q+r_1-h$ positive ones.
(Proof: a constant left null vector has $\varphi_1\mathcal L=0$, so $\varphi_1=0$; the rest is
$(\varphi_2,\varphi_3)\in\ker_{\rm left}[CA;C]$.)

**Corollary.** $\sum_j\varepsilon_j\ge q+r_1-h$, hence
$$q+r_1-s\ \le\ h\ <\ q+r_1\qquad\text{(necessary for }(5b)\text{)},\qquad
d_{\rm fin}\ \le\ s-(q+r_1-h)\quad\text{(unconditional)} .$$
Verified on 698 $(5a)$-satisfying pencils without exception.

**A correction to the failure taxonomy.** In the previous exchange the Type II case was described as
"$0<k<s$ implies failure", where $k=q+r_1-h$. That implication is false: the published $\mathcal L_5$ has
$k=1<s=5$ and satisfies $(5b)$. The correct statement is $k>s\Rightarrow$ failure (from $s\ge k$); for
$k\le s$ the counting obstruction disappears.

## II.4 Candidates at the minimum order: the nullspace parametrisation

Since every admissible $\mathcal L$ has
$\mathcal Z=\ker[C;\mathcal L]\subseteq\ker[C;L_0]$ with $\dim\mathcal Z=n-p-q$, we parametrise by
$\mathcal Z$: $[C;\mathcal L]$ spans $\mathcal Z^{\perp}$, and $\mathcal L$ is chosen to contain $L_0$
(this is the variant of the problem in which $L_0$ is required to lie in $\operatorname{row}\mathcal L$).
This produces admissible augmentations **at any order, including $q_0$**, which the closure cannot.

Over 56 functionally observable instances ($n=5,6$; $p,r\in\{1,2\}$; ten seeds each), at $q=q_0$:

| outcome | instances |
|---|---|
| $(5b)$ witnessed at $q_0$, hence $q_{\min}=q_0$ **exactly** | **39** |
| no witness at $q_0$ (only $q_{\min}\ge q_0+1$) | 16 |
| no admissible sample found at $q_0$ ($(5a)$ thin) | 1 |

## II.5 At the minimum order, the only failures observed are the zero-index type

Classifying the failures at $q=q_0$ into (I) $h\ge q+r_1$, (II) $k>s$, (III) neither, over 228 samples:

| class | samples |
|---|---|
| $(5b)$ holds | 78 |
| Type I ($h\ge q_0+r_1$) | **150** |
| Type II ($k>s$) | 0 |
| Type III (neither) | 0 |

A targeted search restricted to the interesting case $h<q_0+r_1$ (175 samples, all instances, $d_{\rm fin}$
computed from the Toeplitz nullity) found **no** Type III.

## II.6 Conjecture T

$$\textbf{At } q=q_0:\qquad (5b)\iff h<q_0+r_1 .$$

Equivalently: at the minimum order, every failure is of Type I. Three independent facts are consistent with it:

* the 39 instances with $q_{\min}=q_0$ are exactly those with an admissible $q_0$-candidate of $h<q_0+r_1$;
* the 16 instances with $q_{\min}>q_0$ have $h\ge q_0+r_1$ for every sampled $q_0$-candidate;
* the published example: $r_1=4$, $q_0=3$ forces $h\ge7$, while $h\le q_0+2p=7$, so $h=7$, $m=0$,
  $\sum\varepsilon=0$, $d_{\rm fin}=s=3$: failure, as the paper states.

Consequently $q_{\min}>q_0$ is equivalent to: *no $(5a)$-satisfying augmentation of order $q_0$ has
$h<q_0+r_1$*. This is a question about the attainable values of the integer $h$.

## II.7 A structural reformulation of $(5b)$, and where a proof of T stalls

Using $(5a)$ in the form $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$, one has
$Q_{\mathcal L}(\lambda)=D(\lambda)H$ with
$$D(\lambda)=\begin{pmatrix}\lambda I-\Lambda&-G_1&-G_0\\0&I&0\\0&0&I\end{pmatrix},\qquad H=[\mathcal L;CA;C],$$
and by rank-nullity, exactly,
$$\operatorname{rank}Q_{\mathcal L}(\lambda)=h-\dim\bigl(\operatorname{im}H\cap\ker D(\lambda)\bigr),$$
so
$$(5b)\iff \operatorname{im}H\cap\ker D(\lambda)=0\quad\forall\lambda .\tag{$\star$}$$

The spectral obstruction therefore enters through the eigenvectors of $\Lambda$ that survive in $\operatorname{im}H$.
A proof of T would follow from the implication

> if $\operatorname{im}H\cap\ker D(\lambda)\ne0$ for some $\lambda$, then a $(5a)$-satisfying augmentation of
> dimension $<q_0$ exists (contradicting minimality).

This implication is not proved. The obstruction is that $(5a)$ constrains the *row space* of $\mathcal L$, while
the spectral condition constrains $\Lambda$; the only link between them is the product $D H$.

## II.8 Two checks requested in the previous exchange

**(a) The nullspace criterion, cross-checked.** The criterion
$\operatorname{rank}[(\lambda I-A)V\mid Z]=\operatorname{rank}[V\mid Z]$ for all $\lambda$ (with
$\operatorname{im}V=\ker[C;CA]$, $\operatorname{im}Z=\ker[C;\mathcal L]$) was implemented through the gcd of
maximal minors of the pencil and compared with the Toeplitz criterion on the same pencils: agreement in 30 of
30 samples (4 further samples were skipped because $\dim\ker[C;\mathcal L]=0$). The two routes are therefore
independent implementations of the same condition and can be used to cross-check each other.

**(b) The geometry at $q_0+1$.** The question of whether the spectral-degeneracy locus contains the entire
admissible family at $q_0$ and $q_0+1$ has the following answer for the published example. At $q_0+1=4$ every
sampled admissible augmentation has $h=q+r_1$ (40 of 40), so the failure is the zero-index obstruction and no
chart-by-chart spectral analysis is needed; the "responsible algebraic relation" is the confinement of the
family to the hypersurface $h=q+r_1$. At $q_0=3$ the same test cannot be performed by sampling: $(5a)$ is a
proper subvariety there (0 of 240 random candidates and 0 of 500 grid points on the four Grassmann charts), so
the admissible family would have to be obtained algebraically, which we cannot currently do.

**Status of the recommendations from the previous exchange.**

| recommendation | status |
|---|---|
| replace the order-gap conjecture by $q_0\le q_{\min}\le n_0-p$ | done |
| add the strengthened obstruction $q+r_1-s\le h<q+r_1$ | done (698 pencils) |
| use $q_0$ as the authority on the minimum dimension | done |
| reproduce the published two-order-gap example | done |
| geometry: spectral-degeneracy locus and responsible relations | done at $q_0+1$; open at $q_0$ |
| strengthen the obstruction into a structural criterion | partial |
| nullspace criterion as an alternative to Kronecker data | done (cross-checked) |

## II.9 What is not claimed

* Conjecture T is not proved; it has 175 counterexample-free samples.
* $(\star)$ is an identity, not a new criterion in terms of fewer data.
* No complexity statement: $\mathrm{DEC}(q)$ is still only known to be in $\exists\mathbb R$.

---

# Part III. Questions

**Q1.** Is Conjecture T plausible in the light of the literature? Equivalently: is it known that at the minimum
algebraic order every admissible augmentation either satisfies $(5b)$ or has $h\ge q_0+r_1$? If it is known, a
pointer would settle the matter; if it is false, a counterexample would be even more useful.

**Q2.** Does the reformulation $(\star)$ appear in the literature in this form (constant left null vectors of
$\Lambda$ versus the image of $H$)? It seems to be a transparent way to say "the spectrum of $\Lambda$ must
avoid $\operatorname{im}H$", but we have not seen it stated.

**Q3.** The missing implication in II.7: from a spectral direction killed by $D(\lambda)$, can one always
construct a smaller admissible row space? If not, is there a known counterexample to that implication (which
would also refute T)?

**Q4.** Since $(5a)$ is a thin condition at $q_0$ (0 of 240 random candidates, 0 of 500 chart-grid points), what
is the recommended exact method for the minimum order: solving $(5a)$ on each Grassmann chart by resultants or
subresultants, or working with the nullspace criterion directly on the chart parametrisation? We have no
computer algebra system available, so a method with modest symbolic overhead would be preferred.

**Q5.** Is the phenomenon "most instances are feasible at $q_0$" expected? In our sample $q_{\min}=q_0$ for 39 of
56 instances, and the gap is positive in 16. Is the gap known to be related to specific spectral properties of
$A$ (repeated eigenvalues, invariant subspaces contained in $\ker[C;CA]$), and is there a classification of
instances with a positive gap?

**Q6.** Priority: to prove T (a statement about the minimum order only), or to extend the search for Type III
failures with families where $(5a)$ is not thin at $q_0$ (for example more measured outputs, $p\ge3$, or
structured spectra)? The first would give a polynomial test of $\mathrm{DEC}(q_0)$; the second would test whether
T is even true.

**Q7.** The confinement observed at $q_0+1$ in the published example (all admissible augmentations have
$h=q+r_1$) — is this a known phenomenon? If the admissible family at a failing order is always confined to the
hypersurface $h=q+r_1$, then the zero-index obstruction would explain every failure below the first feasible
order; if not, one would expect cases where $h<q+r_1$ and $(5b)$ still fails, which is precisely what
Conjecture T denies.

---

# Part IV. State in brief

* For fixed $\mathcal L$, $(5b)$ is decided by one Toeplitz matrix (verified against Smith forms);
  equivalently by $d_{\rm fin}=0$, equivalently by $(\star)$.
* The greedy closure is not the minimum; $q_0$ is. The published two-order-gap example is reproduced
  ($q_0=3$, $q_{\min}=5$), with 40 independent failing admissible augmentations at $q=4$.
* Necessary conditions: $q+r_1-s\le h<q+r_1$, and $d_{\rm fin}\le s-(q+r_1-h)$.
* At $q_0$: 39 of 56 instances have $q_{\min}=q_0$ exactly; all observed failures are Type I.
* Conjecture T states that this is always so; it is unproved, and a proof would make $\mathrm{DEC}(q_0)$
  polynomial.
* At $q_0+1$ in the published example the admissible family is confined to $h=q+r_1$, which is the mechanism
  behind the failure; the nullspace criterion and the Toeplitz criterion agree on all compared pencils.
