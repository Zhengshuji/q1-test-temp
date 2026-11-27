# Project status, new structural results, and request for direction

This note reports what has changed since the previous report and asks how to proceed. It is self-contained:
Part I fixes the problem and the notation, Part II states what is established and how it is checked, Part III lists
the open ends and the questions.

Verification levels: **L1** = paper proof written out; **L2** = exact rational/integer arithmetic on finite
instances (a filter, never a confirmation); **L3** = machine-checked (Lean 4 + Mathlib, declaration names given).

---

# Part I. Setting

$A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$ with
$\operatorname{rank}[C;L_0]=p+r$, and $L_0$ observable for $(C,A)$. A candidate $\mathcal L\in\mathbb C^{q\times n}$
satisfies $\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$ and $\operatorname{rank}[C;\mathcal L]=p+q$
(hence $\operatorname{rank}\mathcal L=q$). With $h=\operatorname{rank}[\mathcal L;CA;C]$ the normal rank of
$Q_{\mathcal L}(\lambda)=[\lambda\mathcal L-\mathcal LA;CA;C]$:

$$(5a)\ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\ \operatorname{rank}Q_{\mathcal L}(\lambda)=h\ \ \forall\lambda .$$

Notation: $R=\operatorname{row}\mathcal L$, $C$ also denotes $\operatorname{row}C$,
$W=\operatorname{row}[C;CA]$ ($\dim W=r_1$), $S=\operatorname{row}[C;L_0]+W$ ($\dim S=s_0$),
$V=\ker[C;CA]$, $K=\ker[C;L_0]$, $\mathcal Z=\ker[C;\mathcal L]$, $\mathcal Z^\perp=\operatorname{row}[C;\mathcal L]$,
$\pi$ = quotient map modulo $C$, $d=n-p-q$, $q_0$ = minimal admissible order, $n_0$ = observability index.

**Type I** $:=$ $h\ge q+r_1$ (counting); **Type III** $:=$ $h<q+r_1$ with $d_{\rm fin}>0$ (spectral).

---

# Part II. What is established

## II.1 Two failure mechanisms, not three

$k:=q+r_1-h\le\operatorname{rank}\mathcal L$ always, since $h\ge r_1$ (row stacking) and
$\operatorname{rank}\mathcal L=q$; the "counting-deficiency" case is empty. So $(5b)$ fails for exactly two reasons:
counting and spectral. L1 + **L3** (`TypeII.typeII_vacuous`) + L2 (93/93).

## II.2 The counting side is arithmetic, in unconditional form

$$h=s_0+q-\dim(R\cap S).$$

*Proof.* $\mathcal Z^\perp=C\oplus R$; since $\operatorname{row}L_0\subseteq R\subseteq\mathcal Z^\perp$,
$\mathcal Z^\perp+S=\mathcal Z^\perp+W$, so $h=(p+q)+s_0-\dim(\mathcal Z^\perp\cap S)$; and
$(C\oplus R)\cap S=C\oplus(R\cap S)$ because $C\subseteq S$, $C\cap R=0$. $\square$

Consequences (same proof):

* $h\le s_0+q-r$; $s_0\le r_1+r$;
* $\text{Type I}\iff R\cap W=0$;
* $\text{Type I}\iff s_0=r_1+r$ **and** $R\cap S=\operatorname{row}L_0$;
* if $s_0<r_1+r$, **no** augmentation at that order is Type I, at any order of the instance.

Verified: identity 35/35, inequality and equality criterion 54/54, $\text{Type I}\iff R\cap W=0$ 56/56,
the joint criterion $33/33$; and on 89 instances $s_0\ge r_1+r$ predicted a positive order gap in 18 cases with no
false positive and one miss. The equivalent geometric form $h=q+r_1-\dim(\pi R\cap\pi W)$ (hence
$\text{Type I}\iff\pi R\cap\pi W=0$) is machine-checked (`TypeIGeom.*`), with the generic consequence: if
$q+\dim\pi W>n-p$ no $R$ avoids $\pi W$, and if $q+\dim\pi W\le n-p$ avoidance is generic.

## II.3 The spectral condition for one candidate is a $q$-dimensional observability test

Choose $\Lambda,G_0,G_1$ with $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ (exists under $(5a)$), put
$U=\mathcal LV\subseteq\mathbb C^q$, and let $E$ satisfy $\ker E=U$. Then

$$(5b)\iff U\ \text{contains no nonzero eigenvector of}\ \Lambda
\iff (E,\Lambda)\ \text{observable}
\iff \operatorname{rank}[E;E\Lambda;\dots;E\Lambda^{q-1}]=q .$$

*Proof.* $Q_{\mathcal L}=D(\lambda)H$ with $H=[\mathcal L;CA;C]$ and
$D=\begin{pmatrix}\lambda I-\Lambda&-G_1&-G_0\\0&I&0\\0&0&I\end{pmatrix}$; then
$\operatorname{rank}(DH)=\operatorname{rank}H\iff\ker D\cap\operatorname{im}H=0$, and
$\ker D(\lambda)=\{(u,0,0):(\lambda I-\Lambda)u=0\}$, $\operatorname{im}H=\{(\mathcal Lx,CAx,Cx)\}$, so a rank drop
at $\lambda$ is exactly an $x\in V$ with $\mathcal Lx\ne0$ and $\Lambda\mathcal Lx=\lambda\mathcal Lx$. The last
equivalence is the PBH test. $\square$

L1 + L2 (44/44 candidates agree with the Toeplitz criterion, including rank-drop cases). Consequence: **for a fixed
candidate, the spectral condition is a single $q\times q$-observability rank computation** — no maximal minors, no
gcd, no Smith form, no quantification over $\lambda$.

## II.4 The whole-family spectral obstruction: incidence dimension and a codimension condition

Let $u=L_0x$, $v=L_0Ax$. For $x\in V$ we have $C(\lambda x-Ax)=0$ automatically, while
$L_0(\lambda x-Ax)=\lambda u-v$; hence $(\lambda I-A)x\in K$ iff $\lambda u=v$, which determines $\lambda$ whenever
$v\wedge u=0$. The **incidence variety**

$$\mathfrak I=\{([x],\lambda,[z]):x\in V\setminus0,\ L_0x\ne0,\ z=(\lambda I-A)x\ne0,\ z\in K\}$$

is therefore a graph over (an open subset of) the **proportionality locus**

$$P=\{x\in V:\ q_{ij}(x):=v_iu_j-v_ju_i=0\ \ \forall i<j\}.$$

Writing $\varepsilon=\dim V-\dim P\ge0$ (the codimension cut by the proportionality quadrics; $\varepsilon=0$ when
$r=1$), the image $S\subseteq\mathbb P(K)$ of the bad lines satisfies

$$\dim S\le\dim\mathbb P(P)=n-r_1-1-\varepsilon .$$

**Covering criterion.** If $\dim S\ge q-r$ (and $h=n$, so $(5a)$ holds for every $\mathcal Z$), then by the
projective dimension theorem $S$ meets every $\mathbb P^{d-1}\subseteq\mathbb P(K)$, so every $d$-dimensional
$\mathcal Z\subseteq K$ contains a bad line and the order is infeasible for the whole family. Contrapositively, the
covering mechanism needs

$$\boxed{\ q-r+\varepsilon\le n-r_1-1\ }$$

**Measured** (proportionality decided exactly):

| instance | $\dim V$ | $r_1$ | $q_0$ | proportionality on $V$ | $n-r_1-1$ | $q_0-r$ | outcome |
|---|---|---|---|---|---|---|---|
| $n=6,p=r=2$ (whole-family case) | 2 | 4 | 3 | holds identically ($\varepsilon=0$) | 1 | 1 | equality; covering happens |
| $n=7,p=2,r=2$ | 3 | 4 | 4 | fails | 2 | 2 | $\varepsilon\ge1$; only isolated candidates fail |
| $n=8,p=3,r=2$ | 2 | 6 | 3 | fails | 1 | 1 | as above (1 of 30 candidates fails) |
| $n=5,p=2,r=1$ | 1 | 4 | 2 | not applicable | 0 | 1 | dimension too small |

This replaces an earlier guess of ours ($r_1=p+r$) which the table refutes: the right invariant involves
$\varepsilon$, i.e. the action of $A$ on $V$, not only dimensions of $C$, $L_0$ and $W$.

## II.5 The whole-family counterexample, with an explicit upper-bound witness

$n=6$, $p=r=2$, $q_0=3$, $r_1=4$, $s_0=5$: every $(5a)$-admissible augmentation at $q_0$ fails $(5b)$, and
$q_{\min}=4$. Three algebraic proofs cover all parameters (per-chart gcd over $\mathbb Q(\theta)[\lambda]$ with
generic degree $2$ and no degree-$0$ specialization; a Bézout left-null-space computation generating the unit ideal;
a $\theta$-only determinantal elimination of $(5a)+(5b)$ with Gröbner basis $[1]$). The geometric proof is
**conditional**: the proportionality needed for $\lambda(x)$ is proved (the $2\times2$ determinant vanishes on a
basis and on a sum of basis vectors, hence identically), but $L_0|_V$ has rank $1$, so the formula is undefined at
one point of $\mathbb P(V)$ and properness cannot be applied on an open subset; one target line may be missed.

For the upper bound $q_{\min}\le4$ we now give an explicit witness (previously missing):

$$\mathcal L=\begin{pmatrix}
0&0&8&20&1&4\\
1&3&0&0&0&0\\
-1&-2&0&2&-3&-3\\
3&1&-3&-1&1&-3\end{pmatrix}$$

$[L_0;R]$ with $R$ the last two rows. Checks: $\operatorname{rank}[C;\mathcal L]=6=p+q$;
$\dim\ker[C;\mathcal L]=0=d$; $CZ=\mathcal LZ=0$; $(5a)$ true; $h=6$ equals the normal rank; the gcd and Toeplitz
tests agree that $(5b)$ holds; coefficients rational. Note $h=6<q+r_1=8$: the feasible point at order four is *not*
of counting type.

## II.6 Two polynomial-size existential-real encodings

$(5b)$ can be written without expanding maximal minors (whose number $\binom{n}{\rho}\binom{\rho+d}{\rho}$ is
exponential; a controlled-regime measurement gives $\log_2N/n\to1.09$):

* **Structured left inverse**: $X(\lambda)P(\lambda)=I_t$ with $\deg X\le t-1$ (the bound from the pencil
  right-inverse criterion of Noferini–Van Dooren, conditions checked), linear in the coefficients of $X$;
  rank-drop strata are handled by an $O(n)$ disjunction on $\dim(Z\cap V)$ together with working modulo $S$.
* **Observability form (new)**: stratify by $s=\operatorname{rank}\mathcal LV$ ($q+1$ branches) and encode
  $M=\mathcal LV_0=AB$ with two-sided inverses, an annihilator $E$ with $\ker E=\operatorname{im}M$, and a left
  inverse $Y_O$ of $[E;E\Lambda;\dots;E\Lambda^{q-1}]$. All constraints are linear or bilinear; variables and
  constraints are $O(q^3+qn)$ and the degree is $\le2$.

Both were checked by constructing all auxiliary variables explicitly on known feasible witnesses (the counterexample
above at $q=4$, and an $n=5,p=2,r=1$ instance at $q=2$), verifying every constraint exactly (16 constraints per
witness, including $Y_O\mathcal O=I_q$). Coefficient bit lengths are $O(n^2(B+\log n))$ (Hadamard and Cramer), so
each fixed order's decision problem lies in $\exists\mathbb R$ with polynomial-size encoding. **This is an upper
bound, not an algorithm.**

## II.7 A conditional tractability observation

Suppose that at each order the infeasibility is decided by counting, i.e. every admissible augmentation that is not
of Type I is spectrally feasible ("no Type III on the admissible locus"). Then $q_{\min}$ is computable in
polynomial time: test $s_0=r_1+r$ and, when it holds, whether every admissible $R$ has $R\cap S=\operatorname{row}L_0$
(a rank comparison when $(5a)$ is automatic); otherwise take a non-Type-I candidate and apply II.3. The counterexample
of II.5 shows the hypothesis is not automatic, so this is a sufficient structural condition, not an answer.

## II.8 Corrections made (all recorded)

Type II as a separate case (empty); "$\dim(\operatorname{row}L_0\cap W)\le p$ implies Type I" (55 false positives in 89
instances; correct form is $\operatorname{row}L_0\cap W\subseteq\operatorname{row}C$, equivalently $s_0=r_1+r$); the
"uniformity under $V'\cap S=0$" (that object had no intrinsic definition; replaced by II.2); "the $\exists\mathbb R$
route is void because the encoding is exponential" (it was the unstructured variant that is exponential); "the
feasible set is not open" (open on each stratum, constructible across strata); the old proof of the infinite-divisor
formula (invalid, replaced); the geometric surjectivity argument (conditional); a negative statement about
$\overline T$-invariance (withdrawn pending reproduction of a counterexample); and "$r_1=p+r$" (refuted by II.4).

## II.9 Verification inventory

41 propositions are registered in the proved-theorems document; 24 have Lean content, 159 declarations in 59 files,
each mapped to its proposition and to its difference (0 audit issues). The Lean part covers the pencil equivalence,
the top/zero-layer/full-space cases, the cyclic-vector criterion, the vacuity of Type II, the geometric form of
Type I, the dimension formula, the matrix row-space form of $(5a)$, and a row-space bridge. Not machine-checkable at
present: the Kronecker/Smith chain, the incidence-dimension argument (needs projective dimension theory), and the
algorithmic statements. Independent exact scripts reproduce every numerical claim quoted above.

---

# Part III. Questions

**Q1 (next target).** Which comes first: (a) turning II.7 into a theorem, i.e. exhibiting a decidable sufficient
condition for "no Type III on the admissible locus" and thereby an unconditional polynomial class; (b) attempting an
$\exists\mathbb R$-hardness reduction in the Type III world, using the observability shape of II.3 as the interface;
or (c) writing up the two results of II.2 and II.5?

**Q2 (the tractable class).** Is "no Type III on the admissible locus" the right hypothesis to make explicit, or
would you state II.7 with a different hypothesis (for instance directly as "the count decides every order")? Do you
regard such a statement as worth a proposition, or only as a remark?

**Q3 (the proportionality codimension).** The quantity $\varepsilon$ of II.4 is the codimension in $V$ of the quadric
system $v\wedge u=0$. Is this invariant familiar — can it be read off from the Kronecker data of the pencil
$(\lambda I-A)$ restricted to $V$, and is there a standard name for it? A formula for $\varepsilon$ would turn
II.4's necessary condition into a computable one.

**Q4 (hardness).** Given that the encoding is bilinear plus rank conditions of polynomial size, do you see the
bilinear/rank structure as a genuine barrier to a polynomial algorithm, and which $\exists\mathbb R$-complete source
would you try to reduce from first?

**Q5 (novelty check).** Has the observability form of II.3 — $\ker E=\mathcal L(V)$ and observability of
$(E,\Lambda)$ — appeared in the observer-design literature? If so we should cite it rather than present it as a
reduction; if not, we would like to know whether you consider it the right "interface" object.

**Q6 (priority).** We can write the paper on II.2 and II.5 with II.3 and II.6 as appendices. Is that the right move
now, or would you rather see one more structural result (Q1(a) or Q3) before writing?
