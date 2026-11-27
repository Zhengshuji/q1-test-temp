# Dimension obstructions and uniform spectral infeasibility in functional-observer order selection

**Status**: draft skeleton (2026-11-03). Every numbered claim below is already backed by a proof and/or an exact
certificate in this repository; the bracketed tags say which. Sections marked ⟨TODO⟩ are not yet written.

---

## Abstract

For functionally observable data $(A,C,L_0)$, observers of a prescribed functional are known to exist for every
order in $[q_0,n_0-p]$, and the minimal order $q_{\min}$ is the least spectrally feasible order. We isolate two
mechanisms that can make an order infeasible. The first is a **dimension obstruction**: we show that
$h=\operatorname{rank}[\mathcal L;CA;C]$ satisfies $h=\dim(\mathcal Z^\perp+W)$, where $\mathcal Z=\ker[C;\mathcal L]$
and $W=\operatorname{row}[C;CA]$, so that $h$ depends only on the nullspace of the augmentation and not on its rows.
Writing $S=\operatorname{row}[C;L_0]+W$ and $s_0=\dim S$, this makes the obstruction $h\ge q+r_1$ an integer
condition on the placement of the complement of $\ker[C;L_0]$ in $\mathcal Z^\perp$; on orders where that
complement meets $S$ trivially, the condition reduces to $s_0\ge r_1+r$ and is therefore **uniform over the whole
family** at that order. The second is a genuinely **spectral** obstruction: we give an exact instance in which the
dimension obstruction is impossible ($h=n$) and yet every admissible nullspace at $q_0$ fails the spectral test; the
proof is a surjectivity argument for a rational map $\mathbb P^1\to\mathbb P^1$. The published two-order-gap example
is re-derived as a pure illustration of the first mechanism.

---

## 1. Setting

For $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$ with $L_0\ne0$ and
$\operatorname{rank}[C;L_0]=p+r$, let $\mathcal L$ be $q\times n$ with $\operatorname{row}L_0\subseteq
\operatorname{row}\mathcal L$, and consider
$$(5a)\ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\quad\forall\lambda\in\mathbb C .$$

Notation: $\mathcal O_C=[C;CA;\dots;CA^{n-1}]$, $n_0=\operatorname{rank}\mathcal O_C$, $q_0$ the least order at
which $(5a)$ is solvable, $W=\operatorname{row}[C;CA]$, $r_1=\dim W$, $\mathcal Z=\ker[C;\mathcal L]$,
$d=n-p-q$, $h=\operatorname{rank}[\mathcal L;CA;C]$, $Q_{\mathcal L}(\lambda)=[\lambda\mathcal L-\mathcal LA;CA;C]$.

Two facts from the literature are used and not reproved: the order interval is $[q_0,n_0-p]$ with $q_{\min}$ the
least spectrally feasible order in it [Fernando 2026]; and $(5b)$ is equivalent to the nullspace-pencil condition
$$\operatorname{rank}\bigl[(\lambda I-A)V\ \ Z\bigr]=\operatorname{rank}\bigl[V\ \ Z\bigr]\quad\forall\lambda,
\qquad V\ \text{a basis of}\ \ker[C;CA],\ Z\ \text{a basis of}\ \mathcal Z ,$$
which we use as the primary exact test [Fernando 2026, Thm 4].

**Working identity.** $(5b)\iff d_{\rm fin}=0\iff\sum_j\varepsilon_j=\operatorname{rank}\mathcal L$, where
$\varepsilon_j$ are the left minimal indices of $Q_{\mathcal L}$ [our B.6–B.8].

## 2. The dimension obstruction and its uniformity

**Theorem A.** If $\mathcal L$ satisfies $(5a)$ and has full row rank, then
$$h=\dim\bigl(\mathcal Z^\perp+W\bigr).$$
*Proof.* $h=\dim(\operatorname{row}\mathcal L+W)$; and $\mathcal Z^\perp=\operatorname{row}[C;\mathcal L]
=\operatorname{row}C+\operatorname{row}\mathcal L$, with $\operatorname{row}C\subseteq W$; hence
$\mathcal Z^\perp+W=\operatorname{row}\mathcal L+W$. $\square$

**Corollary A1 (dimension obstruction).** With $V'$ a complement of $K^\perp=\operatorname{row}[C;L_0]$ in
$\mathcal Z^\perp$ (so $\dim V'=q-r$), $S=\operatorname{row}[C;L_0]+W$, $s_0=\dim S$, and
$\pi:\mathbb C^n\to\mathbb C^n/S$:
$$h=s_0+\dim\pi(V'),\qquad\text{hence}\qquad h\ge q+r_1\iff \dim\pi(V')\ \ge\ q+r_1-s_0 .$$

**Corollary A2 (uniformity).** If $V'\cap S=0$ then $h=s_0+q-r$, so
$$h\ge q+r_1\iff s_0\ \ge\ r_1+r,$$
independently of $\mathcal L$. On such an order the failure type is the same for the entire admissible family: it
can be decided before any augmentation is constructed.

*Hypothesis must be kept.* $V'\cap S=0$ does not follow from dimensions; it has to be verified for the family in
question.

**Verification.** $h=s_0+q-r$ on 495 sampled admissible augmentations with $V'\cap S=0$; Theorem A on 360 samples.

**Lemma A3 (when $(5a)$ is automatic).** If $h=n$ then $\mathcal Z^\perp+W=\mathbb C^n$ and $(5a)$ holds for every
$\mathcal L$ with $\operatorname{row}[C;\mathcal L]=\mathcal Z^\perp$. (117 sampled cases.)

## 3. The published two-order-gap example, re-derived by dimensions

For the example of [Fernando 2026] ($n=8$, $p=r=2$, $r_1=4$, $q_0=3$) one computes $s_0=6$.

| order | $t=q-r$ | bound on $\dim\pi(V')$ | $h$ | $q+r_1$ | conclusion |
|---|---|---|---|---|---|
| $3$ | 1 | $\le\min(1,n-s_0)=1$ | $7$ | 7 | dimension obstruction ($h=q+r_1$) |
| $4$ | 2 | $\le2$ | $8$ | 8 | dimension obstruction ($h=q+r_1$), 486/486 scanned |
| $5$ | 3 | $\le n-s_0=2$ | $\le8$ | 9 | obstruction impossible |

At $q=3$ an admissible augmentation exists and can be written down:
$$v=\Big(-\tfrac{42919}{32067},-\tfrac{55096}{10689},1,0,0,0,0,0\Big),\qquad
\mathcal L=\begin{pmatrix}L_{0,1}\\ L_{0,2}\\ v\end{pmatrix},$$
with $(5a)$ satisfied, $h=7=q+r_1$, $\varepsilon=[\,]$, $d_{\rm fin}=3$; so the failure at $q_0$ is a dimension
obstruction, and it takes an explicit augmentation to see that $(5a)$ is not the obstruction. Hence
$q_{\min}=5=n-r_1+1$, and the whole spectrum has an integer explanation.

⟨TODO⟩ include the matrices of the example in an appendix, taken from the source, and note the discrepancy with
the "structural explanation" phrasing of our earlier note (there it was claimed from $q+r_1=n$ alone, which is not
a valid inference; the correct statement is Corollary A2 with its hypothesis, verified here by exhaustive scan at
$q=4$).

## 4. A genuinely spectral obstruction

**Theorem B.** There is an instance with $n=6$, $p=r=2$, $q_0=3$, $r_1=4$ at which:
(i) $(5a)$ holds for every $\mathcal L$ of order $3$ (because $h=n$);
(ii) every such $\mathcal L$ fails $(5b)$;
(iii) $q_{\min}=4$.

*Ingredients of the proof.*
1. $s_0=5$, $t=q_0-r=1$, so $h=s_0+t=6=n$ and Lemma A3 gives (i). ⟨exact numbers⟩
2. Define $V=\ker[C;CA]$ ($\dim2$) and, for $x\in V$ with $L_0x\ne0$, $\lambda(x)=L_0Ax/L_0x$ and
   $z(x)=(\lambda(x)I-A)x$. For this instance $z(x)\in K=\ker[C;L_0]$ for all such $x$: the two vectors $L_0Ax$ and
   $L_0x$ are proportional, because the $2\times2$ determinant
   $\det\begin{pmatrix}L_{0,1}Ax&L_{0,1}x\\ L_{0,2}Ax&L_{0,2}x\end{pmatrix}$ is a quadratic form vanishing on a basis
   of $V$ and on pairwise sums, hence identically on $V$ ⟨certificate⟩.
3. If $\mathcal Z=\operatorname{span}z(x)$ then $[\lambda(x)\mathcal L-\mathcal LA;CA;C]\,x=0$ with $x\ne0$, so
   $Q_{\mathcal L}$ drops rank at $\lambda(x)$ (here $h=n$, so a nonzero kernel vector forces the drop).
4. The map $x\mapsto\operatorname{span}z(x)$ is $\mathbb P(V)\to\mathbb P(K)$ with $\dim V=\dim K=2$, i.e.
   $\mathbb P^1\to\mathbb P^1$; it is nonconstant ($[12/5:0]$ and $[4:-4]$ are both attained), hence a surjective
   morphism; therefore every $\mathcal Z\in\operatorname{Gr}(d,K)$ is $\operatorname{span}z(x)$ for some $x$, and
   every admissible $\mathcal L$ fails $(5b)$. This gives (ii).
5. At $q=4$ the family is nonempty and all of it works ⟨scan⟩, giving (iii).

**Remark B1 (general sufficient condition).** With $Y=\overline{\Phi(\mathbb P(V))}\subseteq\mathbb P(K)$,
$k=\dim K$, the projective dimension theorem gives: if $h=n$ at an order and
$$\dim Y+(d-1)\ge k-1,\quad\text{i.e.}\quad \dim Y\ \ge\ q-r,$$
then every admissible $\mathcal Z$ meets $Y$ and the order has no solution. Theorem B is the case
$\dim Y=1=q-r$. The closure has to be replaced by the image where the map is not known to extend; in Theorem B the
map is a morphism of curves, so this does not arise.

## 5. Relation to the nullspace-pencil criterion

Theorem B's ingredient 3 is a special case of the nullspace-pencil criterion of §1: the pair $(x,\lambda(x))$ is a
witness that $\operatorname{rank}[({\lambda}I-A)V\ Z]<\operatorname{rank}[V\ Z]$ for $\mathcal Z=\operatorname{span}z(x)$.
The pencil criterion is the exact per-order test; the geometric statement of Theorem B explains *why* the test
fails for every $\mathcal Z$ at once.

## 6. What is and is not claimed

* The dimension identity is elementary; what we have not seen stated is the **uniformity** of Corollary A2, namely
  that on an order with $V'\cap S=0$ the obstruction is decided before any augmentation is constructed.
* The spectral counterexample of §4 separates the two mechanisms; it is not a general classification.
* We do not claim any complexity result. Restricted-case hardness for the minimum-order problem is not known to us;
  a nearby but different problem (sensor placement for structural functional observability) is NP-hard.
* Boundary statistics (frequency of the spectral case in random families) are exploratory and are reported as such.

⟨TODO⟩ Section 6 to be expanded once the referee-facing claim list is fixed.

## Appendix A. A Toeplitz test for $(5b)$ at a fixed augmentation

For the reduced descriptor pencil $R(\lambda)=[\lambda E-F\ \,B]$ of size $h\times(q+2p)$, let $T_d$ be the block
Toeplitz matrix of the polynomial equation $R(\lambda)y(\lambda)=0$ with $\deg y\le d$, and
$\nu_d=\dim\ker T_d$. Then, with $s=\operatorname{rank}\mathcal L$ and $m=q+2p-h$,
$$(5b)\iff \nu_s=(s+1)m-s,$$
and the left minimal indices are recovered by $\nu_d-2\nu_{d-1}+\nu_{d-2}$. [paper proof; 66/66 agreement with a
Smith-form route; the maximal-minor gcd remains the independent certificate]

## Appendix B. Certificates

| claim | certificate |
|---|---|
| Theorem A, Corollary A1 | 495 and 360 exact samples; `h_formula/verify.py` |
| Corollary A2 numbers for §3 | 486/486 exhaustive chart scan at $q=4$; explicit $L$ at $q=3$ |
| Theorem B | proportionality certificate; surjectivity ($\dim Y=1$, $q-r=1$); $q=4$ scan |
| Appendix A | 66/66 |

⟨TODO⟩ Replace the internal pointers by self-contained statements (matrices, determinants) before submission.
