# Report 105: the hyperplane layer — parameterization with prescribed rows, chartwise decision, and the bit-complexity question

This report has two purposes: to report the changes made in response to the audit of Report 103, and
to ask for two things — an audit of the corrected parameterization theorem, and guidance on the
bit-complexity bounds that the fixed-\(p\) claim still needs.

Everything is self-contained: only Papers I and II are assumed.

---

## Part I. Setting

$K_0=\ker[C;CA]$, $k=\dim K_0$, $N$ a basis of $K_0$, $H=LN$, $H_A=LAN$,
$\omega=\operatorname{rank}H$, $P(\lambda)=\lambda H-H_A$, $\mathcal L=[L_0;R]$ with $q$ rows,
$V=\operatorname{row}\mathcal L$, $V_0=\operatorname{row}L_0$, $\rho=\operatorname{rank}[C;CA]$
(so $k=n-\rho$), and the conditions
$$
(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \operatorname{rank}P(\lambda)=\omega\ \ \forall\lambda\in\mathbb C .
$$

**The layer studied here** is $c=1$, i.e. $\omega=k-1$. Then $\ker H$ is a line $\mathbb C v$,
$v\in K_0$; every row of $\mathcal L$ annihilates $v$ and $Av$; and
$$\dim(V\cap K_0)=k-1,\qquad V\subseteq U_v^\perp,\qquad U_v=\operatorname{span}(v,Av).$$
Throughout, the standard Euclidean inner product on $\mathbb R^n$ is used (so no nondegeneracy
hypothesis is needed: restrictions to subspaces are positive definite).

---

## Part II. Results since the audit of Report 103

### II.1 The parameterization with prescribed rows (the main correction)

The audit's principal objection was that the parameterization ignored $V_0$. The corrected statement
uses three new objects:
$$E_\mu=\ker(M-\mu I),\quad M=\pi_{K_0}A|_{K_0};\qquad
E_\mu^0=E_\mu\cap\ker(L_0N)\cap\ker(L_0AN);\qquad
\delta=\dim V_0-\dim(V_0\cap K_0).$$

**Lemma A (prescribed rows are compatible automatically).** Let $v\in E_\mu^0\setminus\{0\}$. Then
$V_0\subseteq U_v^\perp$, $V_0\cap D_v=V_0\cap K_0$ for $D_v=K_0\cap U_v^\perp$, and $\delta$ is
independent of $v$.

*Proof.* $v\in E_\mu^0$ means $L_0v=L_0Av=0$, so each row of $L_0$ annihilates $v$ and $Av$, i.e.
$V_0\subseteq U_v^\perp$. Then $V_0\cap D_v=V_0\cap K_0\cap U_v^\perp=V_0\cap K_0$; the right-hand
side does not involve $v$. $\square$

Note that this is slightly stronger than the audit's formulation, where $V_0\subseteq U_v^\perp$ was
assumed: it is automatic once the direction is restricted to $E_\mu^0$.

**Lemma B (the fibre with prescribed rows).** For $[v]\in\mathbb P(E_\mu^0)$, put
$\mathcal Q_v=U_v^\perp/D_v$ and $\overline V_{0,v}=(V_0+D_v)/D_v\subseteq\mathcal Q_v$ ($\dim=\delta$).
With $s=q-k+1$, the admissible row spaces are exactly the $s$-dimensional subspaces of $\mathcal Q_v$
containing $\overline V_{0,v}$, i.e.
$$\operatorname{Gr}\bigl(s-\delta,\ \mathcal Q_v/\overline V_{0,v}\bigr),$$
of dimension $(s-\delta)(r(v)-s)$, nonempty iff $\delta\le s\le r(v)$, where $r(v)=\rho$ for eigen
directions and $\rho-1$ for non-eigen ones.

**Lemma C (full row rank).** If a feasible design exists and $q\le\dim U_v^\perp$, then one exists
with $V$ of dimension $q$.

**Theorem 1′ (complete parameterization).** The hyperplane layer is the disjoint union, over the real
eigenvalues $\mu$ of $M$, of the two **relative** Grassmann bundles
$$
\operatorname{Gr}_{B^{\mathrm{eig}}_\mu}\!\bigl(s-\delta,\ \mathcal Q/\overline V_0\bigr),
\qquad
\operatorname{Gr}_{B^{\mathrm{non}}_\mu}\!\bigl(s-\delta,\ \mathcal Q/\overline V_0\bigr),
$$
with bases $B^{\mathrm{eig}}_\mu=\mathbb P(E_\mu^0\cap\ker A_{21})$ and
$B^{\mathrm{non}}_\mu=\mathbb P(E_\mu^0)\setminus B^{\mathrm{eig}}_\mu$, where
$A_{21}=\pi_{K_0^\perp}A|_{K_0}$. Their dimensions are
$$h_\mu^0-1+(s-\delta)(\rho-s),\qquad d_\mu^0-1+(s-\delta)(\rho-1-s),$$
where $h_\mu^0=\dim(E_\mu^0\cap\ker A_{21})$ and $d_\mu^0=\dim E_\mu^0$. Each nonempty piece is
irreducible and defined over $\mathbb R$. The theorem parameterizes structural candidates; spectral
feasibility is tested separately.

*Proof.* Lemma B gives the fibre over each direction, Lemma A gives the constant-rank structure, and
the dimension formula is the standard one for a relative Grassmann bundle. The change from products to
relative bundles (the audit's second correction) is what makes the statement correct without assuming
the quotient bundles are trivial. The eigen-stratum dimension is $h_\mu^0-1$, not $d_\mu^0-1$ (the
audit's third correction). $\square$

When $L_0$ is empty, $\delta=0$ and $E_\mu^0=E_\mu$, and Theorem 1′ reduces to the version of
Report 103.

### II.2 Chartwise decision

Since each piece of Theorem 1′ is a relative Grassmannian, it is covered by finitely many affine
charts. On a chart of $\operatorname{Gr}(m,R)$ with $m=s-\delta$ and $R$ the rank of the quotient, the
$m$ chart rows are
$$\text{row}_i=\text{comp}_i+\sum_{j=1}^{R-m}X_{ij}\,\text{comp}_{m+j},$$
with $X$ a symbolic $m\times(R-m)$ matrix. Substituting into the pencil gives the maximal minors
$m_I(X,\lambda)$, and the generic-gcd criterion of Report 101 applies verbatim:

* $\deg_\lambda\gcd_I m_I=0$ over the function field of the chart: the chart is generically good;
* positive degree: the whole chart is bad.

I implemented this with exact rational arithmetic only. For $m=0$ the fibre is a point; for
$m=1$ it is a projective space and the gcd is computed in one variable; for $m\ge2$ the same
one-variable machinery is used after setting the number of parameters to $m(R-m)$. A cheaper
sufficient test for goodness is a single non-vanishing resultant: if
$\operatorname{Res}_\lambda(m_I,m_J)\not\equiv0$ as a polynomial in $X$, then $\gcd=1$.

Two-way decisions are available for rational eigenvalues; for irrational ones the direction screen is
implemented over the number field $\mathbb Q[\mu]/(f)$, and the chart computation is still on rational
eigenvalues only.

### II.3 The repeated-eigenvalue counterexample, with certificates

The audit asked for complete data and certificates. Take $n=8$, $p=2$, $C=[e_1;e_2]$, $L_0$ empty,
and arrange the compression to be $M=\operatorname{diag}(1,1,2,3)$ (by choosing the action of $A$ on
$K_0$). Then $\rho=4$, $k=4$, $\omega=3$, $\chi_M=(x-3)(x-2)(x-1)^2$, and $E_1$ is two-dimensional.

| direction in $E_1$ | $\deg_\lambda\gcd$ | verdict |
|---|---|---|
| $(1,0)$ | 2 | entirely bad |
| $(0,1)$ | 2 | entirely bad |
| $(1,1)$ | **0** | **generically good** |
| $(1,2)$ | 2 | entirely bad |
| $(2,-1)$ | 2 | entirely bad |
| $(3,1)$ | 2 | entirely bad |

For the bad directions the computed gcd divides every maximal minor (verified by division in the
function field); for $(1,1)$ a rational chart point gives $\gcd=1$. Note that $(1,1)$ is in fact an
*eigen* direction of $A$ (its image under $A_{21}$ vanishes), so its fibre has one more parameter than
the others.

This confirms, with explicit data, that feasibility is not constant on a repeated eigenspace.

### II.4 Prescribed rows can eliminate entire eigenspaces

A small observation that supports the audit's warning. For the instance with $\chi_M=x(x-1)(x^2-8)$
and $L_0$ equal to the sixth coordinate row, the directions over the factors $x-1$ and $x$ are
admissible, but the direction over $x^2-8$ is **not**: the prescribed row kills it. Since the
prescribed-row condition is linear on $E_\mu$, the admissible directions are the intersection of a
projective eigenspace with a linear subspace — so the base of the layer can be strictly smaller than
$\mathbb P(E_\mu)$, and it can even be empty. When every $E_\mu^0$ is zero, the layer is infeasible,
which is a free negative certificate.

### II.5 Corrections

Two errors of mine were caught by implementing the charts properly, and I record them because they
show where the arguments are delicate.

1. With $L_0=e_6$ and $q=4$ I had reported "no feasible design found" from a search that tested a
   single point of the fibre. The chart computation shows the fibre is a projective space whose
   generic gcd is one, so the instance is feasible. A single point of a fibre is not enough, because
   feasibility is an open condition there.
2. In an earlier version the fibre was written as a product $\mathbb P\times\operatorname{Gr}$, and
   the eigen-stratum dimension was computed with $d_\mu$ instead of $h_\mu$; both are corrected in
   Theorem 1′.

---

## Part III. Questions

### Q1 (main). Bit-complexity bounds for the fixed-\(p\) claim

The audit listed the quantities that must be bounded: the number of chart parameters
($\le p^2$), the degrees in the parameters and in $\lambda$ ($O(n)$), the number of maximal minors
($n^{O(p)}$ for fixed $p$), the coefficient bit lengths, the field degree, and the number of charts.
Two of these I do not know how to bound cleanly:

1. **Heights.** The compression $M=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN$ is rational; its
   characteristic polynomial has integer coefficients whose size can grow with the input. The
   eigenvector coordinates over a number field of degree $d\le k$ are computed by exact linear
   algebra; the natural bound involves the height of the characteristic polynomial and of $M$. Is
   there a standard height bound I should cite, or is this something to prove here?
2. **Coefficient growth in the gcd.** The Euclidean algorithm over $K(X)[\lambda]$ can inflate
   numerators and denominators. For a *degree-bounded* claim one normally replaces it by a
   fraction-free (subresultant) computation. Is that the right route for a polynomial-time statement,
   or should the claim be stated only for the resultant test (which is a determinant, hence
   fraction-free)?

I would be content with a theorem of the form "for fixed $p$, on the geometrically simple subclass,
the decision runs in polynomial bit complexity", but I do not want to state it until these two points
are settled.

### Q2. Audit request: is Theorem 1′ correct?

Specifically: (i) is Lemma A's conclusion ($V_0\subseteq U_v^\perp$ automatic from $v\in E_\mu^0$)
right; (ii) is the fibre really $\operatorname{Gr}(s-\delta,\mathcal Q_v/\overline V_{0,v})$ with the
stated dimension; (iii) is the disjointness of the eigen and non-eigen pieces correct at the level of
the bases $B^{\mathrm{eig}}_\mu$ and $B^{\mathrm{non}}_\mu$?

### Q3. The repeated-spectrum case

The audit suggested as Outcome B a structural classification of repeated eigenspaces. Given the
counterexample of II.3, the natural object seems to be the set of directions in $\mathbb P(E_\mu)$ for
which a common factor exists — a closed subset defined by the gcd condition. Is it worth trying to
describe it via the rank stratification of $A_{21}|_{E_\mu}$ (the audit's three cases
$s=0$, $0<s<d$, $s=d$), or is there a better invariant?

### Q4. The Paper II duality

The audit observed that in the hyperplane layer the direction is the annihilator of the common
projection: with $\mathsf M=[N\ AN]$ and $W=\operatorname{row}(V\mathsf M)$,
$$U=\pi_1(W)=\pi_2(W)=a^\circ,\qquad [a]=\mathbb P(\operatorname{Ann}(U)),\qquad v=Na .$$
Should this be stated as a theorem in its own right (a dictionary between the ambient description and
Paper II's compressed description), and if so, what is the cleanest formulation of the map
$V\mapsto W$ and of its fibres?

### Q5. Scope of the negative certificates

The direction screen (II.4) gives a negative certificate when every $E_\mu^0$ vanishes. Is there a
useful *general* negative certificate in this layer, i.e. a condition on the data that guarantees that
every chart is bad, short of computing each chart's gcd?

### Reliability

| Statement | Status |
|---|---|
| Lemma A, B, C; Theorem 1′ | proved (paper), under the Euclidean inner product |
| Chartwise decision (rational eigenvalues) | exact computation, two independent implementations (gcd and resultant) that agree |
| Counterexample II.3 | exact computation with certificates |
| II.4 observation | exact computation |
| Fixed-\(p\) polynomial claim | **not claimed here**; see Q1 |
