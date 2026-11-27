# From Class I to all $(p,r)$: a necessary condition for feasibility, and one correction

This note reports three results that came out of following your suggestions: the Class I theorem extends to all $p=1$
with arbitrary $r$; the stratification parameter $\delta$ that you introduced governs feasibility in general; and there
is one point where your suggestion for the next case does not apply, for a reason worth recording. Proofs are written
out; at the end we ask you to check them.

---

# Part I. The three results

## B.29 ($p=1$, arbitrary $r$: $q_{\min}=n-1$)

**Theorem.** Let $p=1$ ($C=c^{\mathsf T}$), let $r\ge1$, let $\operatorname{rank}[C;L_0]=1+r$, let $(c,A)$ be
observable, and let $\mathcal L$ be admissible. Then every admissible candidate with $1\le q\le n-2$ violates $(5b)$,
and $q=n-1$ is feasible; hence $q_{\min}=n-1$.

*Proof.* The proof of the Class I theorem never uses $r$. Indeed:

1. $r_1=\operatorname{rank}[CA;C]\le 2p=2$ (the block $[CA;C]$ has $2p$ rows), and observability makes $c,cA$
   independent, so $r_1=2$;
2. $\mathcal V=\mathcal Z^\perp=\operatorname{row}[\mathcal L;c]$, so $\dim\mathcal V=q+p=q+1$ and $c\in\mathcal V$;
3. $W_0=\operatorname{row}[CA;C]=\langle cA,c\rangle$, so $h=\dim(\mathcal V+\langle cA\rangle)\in\{q+1,q+2\}$, with
   $h=q+2\iff cA\notin\mathcal V$;
4. if $cA\notin\mathcal V$ then $h=q+2=q+r_1$ and your equality theorem gives failure;
5. if $cA\in\mathcal V$ then $W_0\subseteq\mathcal V$, so (5a) forces $\mathcal VA\subseteq\mathcal V$; then
   $cA^k\in\mathcal V$ for all $k$, observability gives $\operatorname{span}\{cA^k\}=\mathbb C^{1\times n}$, hence
   $n\le\dim\mathcal V=q+1$, contradicting $q\le n-2$.

Exact verification: 597, 593 and 589 admissible candidates at orders $q\le n-2$ for $r=1,2,3$; all fail.

**A correction to your suggestion.** You proposed $p=1,r=2$ as the next case, with $r_1$ up to $3$ and hence an
intermediate value $\delta=1$. But $r_1=\operatorname{rank}[CA;C]\le 2p$, so for $p=1$ one always has $r_1\le2$ and
therefore $r_1-p\le1$: the intermediate range $1\le\delta<r_1-p$ is **empty for every $r$**. The intermediate stratum
requires $p\ge2$. (This is why the $p=1$ theorem is uniform in $r$: there is nothing for $r$ to change.)

## B.30 ($\delta$ trichotomy)

With $\delta(\mathcal V)=\dim\bigl(\operatorname{row}(CA)/(\operatorname{row}(CA)\cap\mathcal V)\bigr)$ and
$h=q+p+\delta$:

| stratum | verdict |
|---|---|
| $\delta=r_1-p$ | **never feasible** (equality $h=q+r_1$; your B.22) |
| $\delta=0$ | **never feasible** when $q+p<n$ (invariance plus observability) |
| $1\le\delta<r_1-p$ | **almost always feasible**: 1060 of 1061 samples, with exactly one failure |

The data, by $(p,r,r_1)$:

| $p$ | $r$ | $r_1$ | $\delta=0$ | intermediate |
|---|---|---|---|---|
| 2 | 1 | 4 | 0/387 | 386/387 |
| 2 | 2 | 4 | 0/371 | 373/373 |
| 3 | 1 | 6 | 0/192 | 744/744 |
| 3 | 2 | 6 | — | 542/542 |

So the intermediate stratum is *not* uniformly feasible either; its failure set is apparently a proper algebraic
subset. Also, for $(2,2)$, 600 random instances all have $q_{\min}<n-1$, with $q_{\min}-q_0\in\{0,1\}$.

## B.31 (necessary condition for feasibility, any $(p,r)$)

**Theorem.** Let $\mathcal L$ be admissible and $q+p<n$. If $(5b)$ holds then
$$1\le\delta(\mathcal V)<r_1-p .$$

*Proof.* Both extremes are excluded:
* if $\delta=r_1-p$ then $\operatorname{row}(CA)\cap\mathcal V=0$, hence $h=q+r_1$, and the equality theorem gives
  failure;
* if $\delta=0$ then $\operatorname{row}(CA)\subseteq\mathcal V$, hence (5a) gives $\mathcal VA\subseteq\mathcal V$;
  since $\operatorname{row}C\subseteq\mathcal V$, induction gives $\operatorname{row}(CA^k)\subseteq\mathcal V$ for all
  $k$, and observability gives $\mathcal V=\mathbb C^{1\times n}$, i.e. $n\le q+p$, contradiction. $\square$

**Consequence.** For $p=1$ the intermediate range is empty, so no candidate below the terminal order can be feasible —
which is B.29 again, now with a one-line reason rather than a two-case coincidence. In this sense the Class I behaviour
is not a quirk of small parameters: it is "the stratum where feasibility could live is empty".

**Sharpness.** The necessary condition is not vacuous: we exhibit an admissible candidate with $n=6$, $p=r=2$, $q=3$
($q_0=2$), $r_1=4$, $\delta=1$ that satisfies $(5a)$, $\operatorname{rank}[C;\mathcal L]=5$,
$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$ and $(5b)$. The data are
$$A=\begin{pmatrix}-2&0&1&2&-1&-2\\2&1&-1&1&-2&0\\2&1&-2&2&0&-2\\-2&2&0&2&-1&2\\-2&-1&0&1&0&-1\\0&0&0&2&0&-2\end{pmatrix},\quad
C=\begin{pmatrix}0&2&1&1&1&-2\\1&-1&-1&1&1&-1\end{pmatrix},$$
$$L_0=\begin{pmatrix}2&1&-2&2&-1&0\\1&-2&-2&-2&2&1\end{pmatrix},\quad
\mathcal L=\begin{pmatrix}2&1&-2&2&-1&0\\1&-2&-2&-2&2&1\\ \tfrac16&1&0&0&0&0\end{pmatrix},$$
with $\mathcal Z=\langle(-6,1,-\tfrac92,\tfrac32,1,0)\rangle$. Every assertion is checked by exact rational arithmetic.

So: feasibility lives **exactly** in the intermediate stratum — the two boundary strata are excluded by proof, and the
intermediate one is non-empty and contains a feasible point.

---

# Part II. Questions

**Q1 (check B.31).** The argument is two contrapositives. Our worries:
(a) the hypothesis $q+p<n$ is needed only for the $\delta=0$ branch; at $q+p\ge n$ (terminal and above) $\delta=0$ is
consistent with feasibility — do you agree that the statement should keep $q+p<n$ explicitly?
(b) in the $\delta=0$ branch we use $\operatorname{row}C\subseteq\mathcal V$; for $p\ge2$ this is automatic
($\operatorname{row}C\subseteq\operatorname{row}[\mathcal L;C]$), but we would like your confirmation that no
hypothesis on $L_0$ enters.

**Q2 (the intermediate failure).** We found exactly one failing candidate in the intermediate stratum
($(p,r,r_1)=(2,1,4)$). Is the expected statement "the failure set is a proper algebraic subset of the stratum", and
would you prove that by exhibiting a feasible point (as we did) or by a dimension count on the incidence variety?

**Q3 (the new formulation of $q_{\min}$).** With B.31, $q_{\min}$ becomes: *the smallest order at which an admissible
$\mathcal V$ with $1\le\delta<r_1-p$ exists*. This is a question about the position of $\operatorname{row}(CA)$ relative
to admissible subspaces — no spectral condition. Do you agree that this is the right formulation to attack next, and
would you compute it by incidence geometry (the $\delta$-strata of the admissible Grassmannian)?

**Q4 (Class I vs the rest).** We can now say: $p=1$ forces $q_{\min}=n-1$ because the intermediate stratum is empty;
$p\ge2$ has $q_{\min}-q_0\in\{0,1\}$ in our $(2,2)$ data. Is it worth stating this as a structural dichotomy
("small $p$ vs large $p$"), or is it premature given we have only $(2,2)$ and $(2,1)$ data?

**Q5 (what to write).** We would order the paper as: subspace reduction (your §2) → counting/spectral framework →
equality obstruction → B.31 as the feasibility criterion → B.29 as the $p=1$ classification → examples. Is that the
right order, or would you put B.31 earlier (right after the reduction) since it is the general feasibility statement?
