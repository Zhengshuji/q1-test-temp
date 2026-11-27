# Report 109: the layer c = 2, consolidated — fibre, base, elimination of W, decidability, and the boundary of complexity

This report consolidates the work on the layer c = 2 that followed the previous report (108). It records
the corrections that were made in response to that review, states the new results with their proofs,
reports which parts are machine-checked, and asks for a check of the parts that are new since then.

Self-contained; the c = 1 paper is called the hyperplane paper.

---

## Part I. Setting

$K_0=\ker[C;CA]$, $k=\dim K_0$, $N$ a basis, $H=LN$, $H_A=LAN$ for a $q$-row design $\mathcal L$ with
row space $V$ of dimension $q$ (full row rank is assumed throughout), and

$$(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \rank(\lambda H-H_A)=\omega:=\rank H\quad\forall\lambda .$$

Layer parameters, kept distinct:

$$c:=k-\rho\ \ (\rho=\rank H=\dim\pi_{K_0}(V)),\qquad t:=q-\rho,\qquad q=\rho+t,\quad c-t=k-q .$$

The direction space is $D=\ker H=K_0\cap V^\perp$, $\dim D=c$. Two problems are separated:

- **unrestricted** layer: all designs with $\dim\ker H=c$;
- **$K_0$-split** layer: those additionally satisfying $\dim(V\cap K_0)=\rho$, equivalently
  $V=(V\cap K_0)\oplus(V\cap K_0^\perp)$.

The direction theorem (a conditional result of report 107) says: for a $K_0$-split design with $(5a)$,
$M(D)\subseteq D$ where $M=\pi_{K_0}A|_{K_0}$.

---

## Part II. Results

### II.1 The fixed-direction fibre, with the prescribed-row condition

**(a) Unrestricted problem.** With $U_D=D+AD$,

$$\mathcal F_D=\bigl\{V\in\operatorname{Gr}(q,U_D^\perp):\ V_0\subseteq V,\ K_0\cap V^\perp=D\bigr\},$$

and exactness of the kernel is equivalent to $K_0\cap(D+AD)=D$ (necessary by $(5a)$, sufficient together
with $V_0\subseteq U_D^\perp$ and $\dim(D+AD)\le n-q$).

**(b) $K_0$-split problem.** With $A_{21}=\pi_{K_0^\perp}A|_{K_0}$ and $T_D=K_0^\perp\cap(A_{21}D)^\perp$,
$M(D)\subseteq D$ gives

$$V\cap K_0=D^{\perp_{K_0}},\qquad V=D^{\perp_{K_0}}\oplus W,\qquad W_0\subseteq W\subseteq T_D,
\qquad \mathcal F_D^{\rm split}\cong\operatorname{Gr}\bigl(t-w_0,\ T_D/W_0\bigr),$$

$$\dim T_D=(n-k)-r(D),\quad r(D)=\rank(A_{21}|_D),\quad
\dim\mathcal F_D^{\rm split}=(t-w_0)\bigl((n-k)-r(D)-t\bigr),$$

$$\text{nonempty}\iff w_0\le t\le(n-k)-r(D),$$

**provided the base is restricted to**

$$\mathcal B_{\rm pres}=\bigl\{D\in\mathcal I_c(M):\ P_{K_0}(V_0)\subseteq D^{\perp_{K_0}}\bigr\}
\quad(\text{equivalently } D\perp P_{K_0}(V_0)),$$

and $W_0\subseteq T_D$. This is the correction requested in the previous review: $V_0\subseteq V$ is two
conditions, one on the base and one on the fibre.

The two set/dimension assertions of (b) — $V\cap K_0=K_0\cap D^\perp$ and
$\dim V=\dim(K_0\cap D^\perp)+\dim W$ — are machine-checked (axiom audit: only the three standard axioms).

### II.2 The base

With the real primary decomposition $K_0=\bigoplus_\lambda K_\lambda\oplus\bigoplus_{\{\mu,\bar\mu\}}K_{\{\mu,\bar\mu\}}$,
an $M$-invariant two-plane is one of:

1. a two-dimensional invariant subspace inside one real primary component (for a single Jordan block
   only the first two vectors of a chain; for several Jordan blocks the classification depends on the
   relative position of eigenvectors and generalized eigenvectors, not only on chain prefixes);
2. a sum of invariant lines from two distinct real primary components, i.e.
   $\mathbb P(K_\lambda)\times\mathbb P(K_\mu)$, of dimension $(d_\lambda-1)+(d_\mu-1)$;
3. a real invariant plane attached to an irreducible quadratic primary component: the family is
   $\mathbb P_{\mathbb C}(E_\mu)\cong\mathbb{CP}^{g_\mu-1}$ of real dimension $2(g_\mu-1)$, where $g_\mu$
   is the **geometric** multiplicity; for $g_\mu=1$ a single point.

If all eigenvalues are simple, $\mathcal I_2(M)$ is a finite set of
$\binom{k_{\mathbb R}}{2}+\#\{\text{conjugate pairs}\}$ points.

### II.3 A real generic-point criterion (the replacement for a Zariski-open argument)

Let $\mathcal X$ be an irreducible affine chart defined over a real algebraic number field $F\subset\mathbb R$,
$m_1,\dots,m_s\in F[\mathcal X][\lambda]$ the maximal minors of the cleared pencil, and
$d_{\rm gen}=\deg_\lambda\gcd_{F(\mathcal X)[\lambda]}(m_1,\dots,m_s)$.

**Lemma 1 (the generic degree is a lower bound).** If $x$ is a *full-rank* point, i.e. no $\lambda$-leading
coefficient of any $m_i$ vanishes at $x$, then
$\deg_\lambda\gcd(m_1(x,\cdot),\dots,m_s(x,\cdot))\ge d_{\rm gen}$.

*Proof.* Let $A=F[\mathcal X]$, a UFD. Divide out contents so that the $m_i$ are primitive. By Gauss's lemma
the gcd over $\operatorname{Frac}(A)[\lambda]$ may be taken primitive, $G\in A[\lambda]$, and then
$G\mid m_i$ **in $A[\lambda]$** — no denominators and no excluded points. Write $m_i=G\,q_i$; then
$\operatorname{lc}_\lambda(m_i)=\operatorname{lc}_\lambda(G)\operatorname{lc}_\lambda(q_i)$ in $A$, so
$\operatorname{lc}_\lambda(G)(x)=0$ would force $\operatorname{lc}_\lambda(m_i)(x)=0$, contradicting full rank.
Hence $\deg_\lambda G(x,\cdot)=d_{\rm gen}$ and $G(x,\cdot)\mid m_i(x,\cdot)$ for all $i$. $\square$

The full-rank hypothesis cannot be dropped: for $m_1=x\lambda-1$, $m_2=(x\lambda-1)(\lambda-1)$ one has
$d_{\rm gen}=1$ while at $x=0$ the two specializations are $-1$ and $-(\lambda-1)$, whose gcd is $1$.

**Lemma 2.** $U=\{x:\ \deg\gcd(x)=d_{\rm gen}\ \text{and }x\text{ full rank}\}$ is a nonempty Zariski-open set.
Indeed $\{\deg\gcd\ge d\}$ is closed (vanishing of subresultants, which are polynomials in the coefficients),
and by Lemma 1 the full-rank set satisfies $\deg\gcd\ge d_{\rm gen}$, so
$U=\{\deg\gcd\le d_{\rm gen}\}\cap\{\text{full rank}\}$ is open; it is nonempty by the definition of $d_{\rm gen}$.

**Theorem (real generic-point criterion).** If in addition the real points of $\mathcal X$ are Zariski dense
and every real point is full-rank, then
$$d_{\rm gen}=0\iff \mathcal X\ \text{contains a real pencil-feasible point}.$$

*Proof.* If $d_{\rm gen}=0$, the open set $U$ is nonempty; if it had no real point then
$\mathcal X(\mathbb R)$ would lie in the proper closed set $\mathcal X\setminus U$, contradicting density; a
real point of $U$ has gcd of degree $0$, hence is feasible. Conversely a real feasible point has gcd degree
$0$, so $d_{\rm gen}\le 0$ by Lemma 1. $\square$

This closes the gap identified in the previous review, and it fixes the algorithm semantics to three
outcomes (feasible / infeasible / undecided), where "infeasible" requires a positive-degree generic gcd on
**every** real-admissible full-rank chart.

### II.4 Elimination of the fibre variable $W$ (the central new result)

Fix a $K_0$-split design, $D$ with $M(D)\subseteq D$, $W_0\subseteq T_D$, and
$V=D^{\perp_{K_0}}\oplus W$ with $W_0\subseteq W\subseteq T_D$, $\dim W=t$. Define

$$\Phi(W):=\bigl\{\varphi_w\in K_0^*:\ \varphi_w(u)=\langle w,A_{21}u\rangle,\ w\in W\bigr\}.$$

**Theorem.** (i) $\Phi(W)\subseteq D^\circ$, hence $\dim\Phi(W)\le c$;
(ii) for every $\lambda$,
$$\operatorname{row}\bigl(\lambda H-H_A\bigr)=\operatorname{row}\bigl(\lambda H_K-(H_A)_K\bigr)+\Phi(W),$$
where $H_K,(H_A)_K$ are the rows coming from $D^{\perp_{K_0}}$;
(iii) consequently the pencil condition depends on $W$ only through $\Phi(W)$.

*Proof.* (i) for $d\in D$, $\varphi_w(d)=\langle w,A_{21}d\rangle=0$ because $w\in T_D\subseteq(A_{21}D)^\perp$.
(ii) the $W$-rows of $H$ are $w^{\mathsf T}N=\langle w,N\cdot\rangle=0$ since $w\perp K_0$; the $W$-rows of
$H_A$ are $w^{\mathsf T}AN=w^{\mathsf T}MN+w^{\mathsf T}A_{21}N=0+\varphi_w$ since $w\perp K_0\ni MN$.
(iii) is immediate from (ii). $\square$

**Corollary (what replaces the Grassmannian).**
$$\exists W\ (W_0\subseteq W\subseteq T_D,\ \dim W=t)\ \text{making }(5b)\text{ hold}
\iff \exists\Phi\subseteq D^\circ\ (\varphi(W_0)\subseteq\Phi,\ \Phi\text{ realizable})$$
making $(5b)$ hold, and the verdict is the same for **every** $W$ with the same $\Phi$. Realizability of a
given $\Phi$ is a linear condition ($\Phi\subseteq\varphi(T_D)$ together with dimension bookkeeping).
For $c=2$ the space $\operatorname{Gr}(\le 2,D^\circ)$ consists of $\{0\}$, the lines (a $\mathbb{P}^1$ family),
and $D^\circ$ itself — so the fibre quantifier collapses from a Grassmannian of dimension up to $O(n^2)$ to at
most one projective line.

**Machine-checked part.** The following are formalized and pass an axiom audit whose only axioms are
`propext`, `Classical.choice`, `Quot.sound`:

- $V\le D^\perp$ for $D\le K_0$, $W\le K_0^\perp$;
- $V\le(D+AD)^\perp\iff W\le(A_{21}D)^\perp$ (this is $(5a)\iff W\subseteq T_D$);
- $\varphi_w$ vanishes on $D$ for $w\le(A_{21}D)^\perp$, i.e. $\Phi(W)\subseteq D^\circ$.

The row-space identity (ii) itself is **not** formalized: it is a matrix-level statement requiring the
explicit construction of $H$ and $H_A$ from $V$, $N$ and $A$ together with the block decomposition. It is
verified on a concrete chart instead: with $D=\operatorname{span}\{e_1+e_2,e_3\}$, $T_D$ of dimension $3$ and
$W=\operatorname{span}\{w_0+s\,w_1\}$, one finds $H$ independent of $s$, $\max\deg_s H_A=1$, the six nonzero
$2\times2$ minors of $(\deg_s,\deg_\lambda)$ equal to $(0,2)$ twice and $(1,1)$ four times, and the gcd
identically $1$ — feasible, and equal to the verdict obtained from nine other $W$ with the same $\Phi$.

### II.5 Charts over the rationals, not over a number field

The previous review asked whether irrational eigenvalues force a number field. They do not, if one uses the
primary decomposition instead of eigenvalues. $M$ is a rational matrix, so its minimal polynomial factors over
$\mathbb Q$; the primary components $K_f=\ker f(M)$ for $f\in\mathbb Q[t]$ irreducible are $\mathbb Q$-defined,
and the invariant two-plane family attached to $f$ is:

- for $\deg f=1$: $\operatorname{Gr}(2,K_f)$;
- for $\deg f=2$: the image of $[v]\in\mathbb P(K_f)\mapsto\operatorname{span}\{v,Mv\}$ (well defined because
  $M^2v=cMv+dv$ when $f=t^2-ct-d$), a $\mathbb Q$-morphism;
- for two factors $i\ne j$: $\mathbb P(K_{f_i})\times\mathbb P(K_{f_j})$.

Rank strata, the prescribed-row condition, pivot trivializations of $D\mapsto(D^{\perp_{K_0}},T_D)$, and the
cleared pencil are all rational; only the final *real* point test is real (II.3). The only unproved point is
whether, when $f$ has two real roots, the sums of two real eigenlines are also real points of the image above.

### II.6 Complexity at fixed $c=2$, and where the boundary is

**Theorem.** Assume (i) $c=2$, (ii) all eigenvalues of $M$ are simple, (iii) $K_0$-split. Then the layer
decision (three-valued) runs in $\mathrm{poly}(n,\tau)$, where $\tau$ is the input bit length.

*Sketch.* Simple spectrum makes $\mathcal I_2(M)$ finite (II.2), of $O(k^2)$ points, so there are no base
charts. For each point the effective fibre is at most a $\mathbb{P}^1$ (II.4), needing two charts. On each
chart there is exactly one free variable $s$; the $W$-rows of $H$ vanish, so $\deg_s\le 1$, and
$\deg_\lambda\le\omega\le k$; the heights are $\mathrm{poly}(n,\tau)$. Hence $O(k^2)$ charts, one gcd over
$\mathbb Q(s)[\lambda]$ each, total $\mathrm{poly}(n,\tau)$.

Two boundaries are essential and are not technicalities: dropping the simplicity of the spectrum makes the
base positive-dimensional (a Grassmannian of dimension $2(d_\lambda-2)=O(n)$), and letting $c$ vary makes the
number of components $\binom{k}{c}$ exponential. So the present route gives $\mathrm{poly}$ only under both
restrictions, and $n^{O(cn+c^2)}$ in general.

### II.7 General $c$

Everything in II.1, II.2, II.4 and II.5 generalizes verbatim with $2$ replaced by $c$: the only place where
$c=2$ entered was the numerical value of $\dim D^\circ$. In particular the elimination theorem gives an
effective fibre $\operatorname{Gr}(\le c,D^\circ)$ of dimension at most $c^2$, the rank strata are
$r(D)\in\{0,\dots,c\}$, and the base has components of dimension $c(d_\lambda-c)$. The three questions that
remain, in order of expected value:

- **Q-A**: can the number of components of $\mathcal I_c(M)$ be avoided, by rewriting "some component" as an
  algebraic condition on $M$?
- **Q-B**: can $\Phi$ be eliminated for general $c$, i.e. can "some $\Phi$ makes the pencil full-rank" be
  expressed as a rank/separation condition on the induced maps on $T_D/W_0$ alone?
- **Q-C**: is it better to index layers by $\dim U$ rather than by $c$? Since $c=k-\dim U$ with
  $U=\pi_1(W)$, large $c$ means small $\dim U$, and the $\rho$ side is already polynomial.

---

## Part III. Corrections recorded

1. **Prescribed-row base condition** (from the previous review): added, II.1(b).
2. **Base classification** (from the previous review): replaced by the primary-component statement, II.2,
   including the geometric-multiplicity correction for conjugate pairs.
3. **Withdrawal of $n^{O(c^2)}$** (from the previous review): the base term $c(d_\lambda-c)$ can be $O(cn)$,
   so the honest bound is $n^{O(cn+c^2)}$; and component enumeration is polynomial only at fixed $c$.
4. **A notational overloading**: the dimension of $T_D$ involves $n-k$, not $\rank H$; these coincide only
   when $n-k=\rank H$. All formulas above use $(n-k)$.
5. **Missing projective point in the non-monotonicity example** (from the previous review): the point
   $\operatorname{span}\{e_2\}$ was checked; its gcd is $(\lambda-1)(\lambda-2)(\lambda-3)$, the same as for
   the one-parameter family, so the $c=1$ side now covers the whole projective line, together with the two
   isolated directions.
6. **gcd degree versus positivity**: within a rank stratum the degree varies with $D$ (values $1$ and $2$
   both occur) but positivity was always the relevant and constant property; a chartwise decision needs only
   positivity.

---

## Part IV. Requests

**Q1 (the elimination theorem).** Is II.4 correct as stated? In particular: (a) is the row-space identity
(ii) right in the convention where rows of $H$ are $V^{\mathsf T}N$; (b) is the realizability condition for a
prescribed $\Phi$ correctly described as linear; (c) is it legitimate to conclude that for $c=2$ the fibre
search reduces to at most one projective line, or does the prescribed-row condition $W_0\subseteq T_D$
introduce further components?

**Q2 (the criterion).** Is Lemma 1 with the Gauss argument the right form of the specialization statement?
Is the full-rank hypothesis (no $\lambda$-leading coefficient vanishes at the point) the minimal one, or
should it be stated as "$d_{\rm gen}$ equals the degree of the specialized gcd on a dense open set"?

**Q3 (complexity).** In II.6, is $\deg_s\le 1$ correct on every chart of the reduced fibre, or only on the
chart chosen so that $\Phi$ varies linearly? Is the chart count $O(k^2)$ right, or should the $\mathbb{P}^1$
of $\Phi$ be counted with multiplicity over the rank strata?

**Q4 (the general-$c$ plan).** Of Q-A, Q-B, Q-C in II.7, which would you pursue first? My own reading is that
Q-B is the natural continuation of II.4 and the most likely to produce a new structural theorem.

### Reliability

| Item | Status |
|---|---|
| II.1(a) exactness | paper proof |
| II.1(b) set/dimension part | machine-checked (axiom audit) |
| II.1(b) equivalence $V\perp AD\iff W\le(A_{21}D)^\perp$ | machine-checked |
| II.2 base description | paper proof (classical), multiplicity qualified |
| II.3 Lemmas 1–2, Theorem | paper proofs (Gauss, subresultants) |
| II.4 (i),(iii) and the equivalence of (ii)'s two sides | (i),(iii) paper, the equivalence machine-checked; (ii) itself paper + one chart checked numerically |
| II.5 | paper argument; one point open |
| II.6 | paper proof sketch, one degree bound checked numerically |
| II.7 | structural remarks, no proof |
