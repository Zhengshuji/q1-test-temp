# Progress report: domain correction, formalised milestones, and two open verification issues

This note reports what was done since the previous report, states what is now proved, what was refuted,
and what remains unresolved. It closes with specific questions.

---

# Part I. Setting

## I.1 Problem and notation

Given $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$ and a row block $L_0\in\mathbb C^{r\times n}$,
let $\mathcal L=\begin{bmatrix}L_0\\R\end{bmatrix}\in\mathbb C^{q\times n}$ and require

$$(5a)\ \operatorname{rank}\begin{bmatrix}\mathcal LA\\ \mathcal L\\ CA\\ C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}\mathcal L\\ CA\\ C\end{bmatrix},
\qquad
(5b)\ \operatorname{rank}\bigl[\lambda\mathcal L-\mathcal LA;\ CA;\ C\bigr]=h\ \ \forall\lambda\in\mathbb C,$$

with $h$ the normal rank. Question $q1$: is computing $q_{\min}$ NP-hard?

Column convention throughout. $V:=\operatorname{row}[\mathcal L;C]^{\mathsf T}$,
$K:=\ker[C;CA]$, $V_0:=V\cap K$, $W:=\mathcal LV$, $W_0:=\mathcal LV_0$,
$W_K:=\mathcal LK$, $S:=V\cap\ker\mathcal L$, $\rho_W:=\dim W$, $\omega:=\dim W_K$.

## I.2 Status

Thirty propositions are recorded; all have paper proofs; twenty-two have machine-checked Lean kernels
(eight literal statements, fourteen non-trivial cores). Five review rounds have been completed.
The three verification gates (layout, Lean-statement registry, coverage registry) are green,
and the machine-checked library contains 222 declarations in 79 files.

---

# Part II. What was done since the previous report

## II.1 The domain question is settled

**Answer applied.** The primary domain is $W_K=\mathcal LK$, with

$$\Phi_K(\mathcal Lv):=\mathcal LAv\quad(v\in K),\qquad P_K(\lambda):=\lambda\iota_K-\Phi_K,\qquad
\iota_K:W_K\hookrightarrow\mathbb C^q .$$

**Well-definedness.** If $v_1-v_2\in K$ and $\mathcal L(v_1-v_2)=0$, then $v_1-v_2\in\ker[\mathcal L;CA;C]$
and $(5a)$ gives $\mathcal LA(v_1-v_2)=0$.

**Intrinsicality.** For $v\in K$ one has $\mathcal LAv=\Lambda\mathcal Lv$, so $\Phi_K=\Lambda|_{\mathcal LK}$;
hence $\Phi_K$ does not depend on the choice of the extension.

**Criterion.** $(5b)$ fails iff there is $0\ne w\in W_K$ with $\Phi_K(w)\in\mathbb Cw$.

**Dimension.** $\dim W_K=\dim K-\dim\ker(\mathcal L|_K)$.

## II.2 The equality $\mathcal LK=\mathcal L(V\cap K)$ is false

We were asked to prove or refute it. It is **false**.

Fixed admissible instance ($n=4$, $p=1$, $q=2$):
$$A=\begin{pmatrix}0&-1&2&1\\0&0&-1&2\\0&-1&0&2\\2&1&2&-1\end{pmatrix},\quad
C=\begin{pmatrix}1&1&-2&2\end{pmatrix},\quad
\mathcal L=\begin{pmatrix}-1&-2&-2&0\\0&-1&-1&1\end{pmatrix},$$
for which $\dim K=2$, $\dim(V\cap K)=1$, $\dim\mathcal LK=2$, $\dim\mathcal L(V\cap K)=1$.

A random sweep over admissible instances ($n=4$, $p=1$, $q=2$, $r=1$, rational entries) gives:
382 admissible instances, **0** with $\mathcal LK=\mathcal L(V\cap K)$, **382** without.
The certificate is re-runnable and asserts the four dimensions above before reporting.

Consequently $W_0$ cannot be used as an equivalent realisation of the domain, and the four-way
equivalence is now stated with $W_K$.

## II.3 Formalised milestones

Three of the seven proposed milestones are now machine-checked (module `B37Domain`, three declarations):

| Milestone | Statement | Declaration |
|---|---|---|
| L2 | $\ker(L|_K)\le\ker(T|_K)\Rightarrow T|_K$ factors through $L|_K$: there is $\Phi:K/\ker(L|_K)\to F$ with $\Phi([v])=Tv$ | `l2_factor` |
| L3 | that $\Phi$ is unique, hence independent of the extension | `l3_unique` |
| L6 | $\dim(LK)=\dim K-\dim\ker(L|_K)$ | `l6_finrank` |

Recorded difference: L2 is formalised in quotient form; the identification of the quotient with the image
$W_K$ is a standard isomorphism and remains on paper. L1, L4, L7 are not formalised.

## II.4 The third AVOID interface is documented

Besides the rank barrier (necessary) and the incidence-coverage criterion (sufficient, with the empty
base locus), we now record the determinantal-divisor interface, which is **exact**:

$$(5b)\iff\Delta_h(\lambda):=\gcd\{\text{all }h\times h\text{ maximal minors of }Q_{\mathcal L}(\lambda)\}\in\mathbb C^\times .$$

Its Bézout form, $\sum_i u_i(\lambda)p_i(\lambda;R)=1$ with polynomially bounded $\deg u_i$, converts the
spectral condition into finitely many coefficient equations, which suits an existential-real encoding
better than chart-wise rank tests.

## II.5 The lower bound is restated as a joint profile

Instead of adding separately minimised quantities, we record

$$q_{\min}=\min_{(\rho,c)\in\mathfrak P}(\rho+c),\qquad
c_{\min}(\rho):=\min\{c:(\rho,c)\in\mathfrak P_{\rm spec}\},\qquad
q_{\min}\ \ge\ \min_{\rho}\{\rho+c_{\min}(\rho)\},$$

and, using the rank barrier, $\rho\le r_*:=\min_\lambda r(\lambda)$. The additive bound remains valid but may
be strictly weaker: for $\mathfrak P=\{(2,5),(3,2),(4,1)\}$ the additive bound gives $3$ while the true
minimum is $5$.

## II.6 Degenerate cases are catalogued

Twelve cases are now listed with their consequences, including two immediate corollaries:

* if $K=0$ then $\operatorname{rank}[C;CA]=n$ and $(5b)$ holds for every $\mathcal L$;
* if $W_K=0$ then $(5b)$ holds.

We also record that $(5b)$ quantifies over finite $\lambda$ only and therefore does not require full rank
at infinity, and that $d_\infty=h-\operatorname{rank}\mathcal L$ rather than $h-q$.

---

# Part III. Unresolved issues

## III.1 The Kronecker ledger is not verified

We attempted to check numerically the accounting identity $h=\sum_j\varepsilon_j+d_{\mathrm{fin}}+d_\infty$
and the equivalence $(5b)\iff d_{\mathrm{fin}}=0$. The attempt is **not usable**:

1. the Smith-form implementation was calibrated on $\operatorname{diag}(\lambda,1)$ and $[\lambda\ \,1]$
   and is correct (giving $d_{\mathrm{fin}}=1$ and $d_{\mathrm{fin}}=0$ respectively);
2. but on $4\times4$ pencils the script produced $d_{\mathrm{fin}}=2$ and $d_\infty=4$, contradicting
   $d_{\mathrm{fin}}+d_\infty=n=4$ for a regular pencil;
3. further, all eight printed rows were identical, which is impossible for random instances.

We conclude that the pencil assembly or the reversal step in our script is wrong, and we have marked its
output as unusable. Since the $\Delta_h$ criterion does not need the accounting identity, we currently use
only $\Delta_h$.

**Question 1.** Is there a canonical reference for the accounting identity in the form
$h=\sum_j\varepsilon_j+d_{\mathrm{fin}}+d_\infty$ for rectangular pencils with row blocks of mixed degree
(degree-one and degree-zero blocks)? In particular, is the correct reversal the swap $Q_1+\mu Q_0$,
or the homogenisation $\alpha Q_1+\beta Q_0$ evaluated on $\mathbb P^1$, and how is $d_\infty$ then defined?

## III.2 L1 is not formalised

**Question 2.** For $(5a)\iff\exists(\Lambda,G_0,G_1)$ with $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$,
the missing formal step is: if $\ker\Phi\le\ker T$ for $\Phi=(\mathcal L,C,CA):E\to F_1\times F_2\times F_3$,
then $T$ factors through $\Phi$ and the factor extends to the whole product. Is there an idiomatic
Mathlib route (a complement plus `prodEquivOfIsCompl`, or a `liftOfSurjective` variant) that avoids
building the extension by hand?

## III.3 Consequences of the refuted equality

Since $\mathcal LK\ne\mathcal L(V\cap K)$ in general, the earlier statement that the quotient pencil
"acts on the effective quotient $V/S$" must be re-examined: the two dimensions $\rho_W=\dim W$ and
$\omega=\dim W_K$ need not agree.

**Question 3.** Is there a clean relation between $\overline N_{\mathcal Z}(\lambda):V/S\to X/\mathcal Z$
and $P_K(\lambda)=\lambda\iota_K-\Phi_K$? We would like a statement of the form "the two pencils have the
same finite elementary divisors", but we have not been able to prove or refute it, and we do not want to
assert it prematurely.

## III.4 Incidence criteria after the correction

The coverage criterion uses $\mathbb P(K)$ and the base locus. With the domain corrected to $W_K$, the
natural ambient space may be $\mathbb P(W_K)$ rather than $\mathbb P(K)$.

**Question 4.** Should the incidence construction be reformulated on $\mathbb P(W_K)$, and if so does the
dimension estimate of the coverage lemma change? Our present estimate
$\dim\mathfrak I\le\max\{v,\dim\mathcal B+k-1\}$ uses $v=\dim V$ and $k=\dim K$ and would need
re-derivation.

## III.5 Priorities

Given the correction and the refutation, we are unsure whether to spend the next period on the structural
statement (domain, intrinsic map, reconciliation of the two pencils) or on the computational side
(parameterised determinantal divisor, Bézout encoding).

**Question 5.** Which of the two would you prioritise now, and what would you consider the minimal
publishable structural content in either case?
