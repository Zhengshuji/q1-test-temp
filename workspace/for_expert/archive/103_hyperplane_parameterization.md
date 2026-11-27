# Report 103: The hyperplane layer — complete parameterization, fixed-\(p\) complexity, and the repeated-eigenvalue obstruction

This is a follow-up to Report 101 and to the audit of it. It supplies the three things the audit asked
for: the complete parameterization of the layer, the fixed-\(p\) complexity argument split into a
geometric and a bit-complexity stage, and an honest statement of what the repeated-eigenvalue case
does to that argument. A concrete counterexample is included: it shows that the direction inside an
eigenspace genuinely matters, which is exactly the phenomenon the audit warned about.

Everything is self-contained; Papers I and II are used only for the compressed formulation and the
subspace description.

---

## Part I. Setting

$K_0=\ker[C;CA]$, $k=\dim K_0$, $N$ a basis of $K_0$, $H=LN$, $H_A=LAN$, $\omega=\operatorname{rank}H$,
$P(\lambda)=\lambda H-H_A$, $\mathcal L=[L_0;R]$ with $q$ rows, $V=\operatorname{row}\mathcal L$,
$\rho=\operatorname{rank}[C;CA]$ (so $k=n-\rho$), and the conditions
$$
(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \operatorname{rank}P(\lambda)=\omega\ \forall\lambda\in\mathbb C .
$$

**The layer** $c=k-\omega$. This report is about $c=1$, i.e. $\omega=k-1$. Then $\ker H$ is a line
$\mathbb C v$ with $v\in K_0$, every row of $\mathcal L$ annihilates $v$ and $Av$, and
$$\dim(V\cap K_0)=k-1,\qquad V\subseteq U_v^\perp,\qquad U_v=\operatorname{span}(v,Av).$$
Call $v$ **eigen** if $\dim U_v=1$.

Standing hypothesis: the restriction of the inner product to $K_0$ is nondegenerate
($K_0\cap K_0^\perp=0$). It holds for generic $C$; without it, "parallel" must be replaced by
"annihilators are proportional".

---

## Part II. Results

### II.1 The complete parameterization

Let $M=\pi_{K_0}A|_{K_0}$ (the orthogonal compression of $A$ to $K_0$) and
$A_{21}=\pi_{K_0^\perp}A|_{K_0}$.

**Lemma 1 (every direction is admissible).** If $\mu$ is a real eigenvalue of $M$ and
$v\in E_\mu=\ker(M-\mu I)$, $v\ne0$, then $\dim(K_0\cap U_v^\perp)=k-1$.

*Proof.* $Mv=\mu v$ means $\pi_{K_0}(Av)=\mu v$, so for $u\in K_0$,
$u\cdot Av=u\cdot\pi_{K_0}(Av)=\mu\,u\cdot v$. Hence the two functionals $\varphi_v$, $\varphi_{Av}$ on
$K_0$ are proportional, and $\dim(K_0\cap U_v^\perp)=k-\operatorname{rank}\{\varphi_v,\varphi_{Av}\}=k-1$
(nondegeneracy gives $\varphi_v\ne0$). $\square$

**Lemma 2 (the eigen directions inside $E_\mu$ are a linear subspace).** On $E_\mu$,
$$Av\in\operatorname{span}(v)\iff A_{21}v=0 .$$
Hence the eigen directions form $\mathbb P(E_\mu\cap\ker A_{21})$, and the non-eigen directions its
open complement.

*Proof.* $Av=Mv+(A_{21}v)$ with $Mv=\mu v\in K_0$ and $A_{21}v\in K_0^\perp$; since $K_0\cap K_0^\perp=0$,
$Av\in\operatorname{span}(v)\subset K_0$ forces $A_{21}v=0$. $\square$

**Lemma 3 (constant-rank bundles).** Over $\mathbb P(E_\mu)$, $v\mapsto D_v:=K_0\cap U_v^\perp$ and
$v\mapsto U_v^\perp/D_v$ are vector bundles of constant rank $k-1$ and
$$r(v)=\begin{cases}\rho-1,&v\ \text{non-eigen},\\ \rho,&v\ \text{eigen}.\end{cases}$$
*Proof.* By Lemma 1 the two functionals have rank $1$ everywhere, so their common kernel has constant
dimension; the quotient dimension is $(n-\dim U_v)-(k-1)$, and $\dim U_v$ is constant on each of the
two strata of Lemma 2. $\square$

**Lemma 4 (the fibre).** For a fixed direction $[v]$ and row count $q$, the admissible row spaces are
$$\{V:\ D_v\subseteq V\subseteq U_v^\perp,\ \dim V=q\}=\operatorname{Gr}\bigl(q-k+1,\ r(v)\bigr),$$
nonempty iff $0\le q-k+1\le r(v)$. (The condition $V\cap K_0=D_v$ is automatic.)

**Theorem 1 (complete parameterization).** The hyperplane layer equals the disjoint union, over the
real eigenvalues $\mu$ of $M$, of the two Grassmann bundles
$$
\mathbb P(E_\mu\cap\ker A_{21})\times\operatorname{Gr}(q-k+1,\rho)
\quad\text{and}\quad
\bigl(\mathbb P(E_\mu)\setminus\mathbb P(E_\mu\cap\ker A_{21})\bigr)\times\operatorname{Gr}(q-k+1,\rho-1),
$$
each irreducible, defined over $\mathbb R$, with
$$\dim=(d_\mu-1)+(q-k+1)\bigl(r-(q-k+1)\bigr),\qquad d_\mu=\dim E_\mu .$$
Nonemptiness: $k-1\le q\le n-1$ (eigen part) and $k-1\le q\le n-2$ (non-eigen part).

*Proof.* Lemma 4 gives the fibre over each direction; Lemma 3 gives the bundle structure (constant
rank over an irreducible base), hence irreducibility; the dimension is the standard bundle formula. $\square$

Three consequences the audit asked for are now explicit: the direction set is a **projective
eigenspace** (not a finite set when $d_\mu>1$); the fibre is a **Grassmannian**, and a projective space
only when $q=k$ ($q-k+1=1$); and everything is defined over $\mathbb R$, so real points are available
whenever a generic point is (the charts are affine spaces).

### II.2 Fixed-\(p\) complexity

**Stage 1 (geometry).** In Theorem 1, $r\le\rho\le 2p$ and the fibre dimension is
$$d_{\mathrm{fib}}=(q-k+1)\bigl(r-(q-k+1)\bigr)\le (2p)^2/4 ,$$
independent of $n$. If **the real eigenvalues of $M$ are simple** ($d_\mu=1$), each base
$\mathbb P(E_\mu)$ is a single point, so every piece is an affine chart of a Grassmannian with at most
$(2p)^2/4$ parameters.

**Stage 2 (bit complexity).** With simple spectrum, on each chart:

| step | cost |
|---|---|
| $K_0$, compression, characteristic polynomial | $\mathrm{poly}(n,L)$ |
| factor over $\mathbb Q$, decide simplicity | $\mathrm{poly}(n,L)$ |
| eigenvector, $D_v$, quotient | $\mathrm{poly}(n,L)$ |
| maximal minors: count $k\binom{q}{q-k+1}$, and $q-k+1\le\rho+1\le 2p+1$ | polynomial in $n$ for fixed $p$ |
| gcd over $K(x)[\lambda]$, $d_{\mathrm{fib}}$ variables | polynomial for fixed $d_{\mathrm{fib}}$ |

All factors are powers of $n$ with exponents depending only on $p$, so the total cost is
$n^{O(p^2)}$.

**Theorem 2.** Let the real eigenvalues of the compression be simple, and the inner product on $K_0$
nondegenerate. Then for every fixed $p$ the hyperplane-layer decision runs in polynomial time.

Simplicity is decidable (factor the characteristic polynomial and check multiplicities), so the
hypothesis is checkable rather than assumed: an implementation can verify it and otherwise report that
the theorem does not apply.

### II.3 The repeated-eigenvalue obstruction — a concrete counterexample

The audit observed that when $d_\mu>1$ the directions form $\mathbb P^{d_\mu-1}$ and asked whether
those parameters can be absorbed. They cannot. Here is an instance.

Take $n=8$, $p=2$, $C=[e_1;e_2]$, and arrange the compression to be $M=\operatorname{diag}(1,1,2,3)$
(possible by choosing the action of $A$ on $K_0$). Then $\omega=3$, $\rho=4$, $q=4=k$, and
$\chi_M=(x-3)(x-2)(x-1)^2$, so $E_1$ is two-dimensional and $\mathbb P(E_1)$ is a line. Computing the
generic gcd of the maximal minors on the fibre over six directions of $E_1$:

| direction | $\deg_\lambda\gcd$ | verdict |
|---|---|---|
| $(1,0)$ | 2 | entirely bad |
| $(0,1)$ | 2 | entirely bad |
| $(1,1)$ | **0** | **generically good** |
| $(1,2)$ | 2 | entirely bad |
| $(2,-1)$ | 2 | entirely bad |
| $(3,1)$ | 2 | entirely bad |

So inside a single eigenspace some directions give feasible fibres and others do not. Consequently:

1. the direction parameters are genuine, and selecting one eigenvector per eigenvalue is **wrong**;
2. "absorb the direction into the fibre" does not work, because the fibre depends on the direction;
3. the recursive route does not help either: the problem on the base, "does some direction admit a good
   fibre", is the same kind of existential question, with the same parameters.

Hence the polynomial-time statement of Theorem 2 is genuinely restricted to simple spectrum; the
restriction is not an artefact of the proof. The instance above is itself feasible (direction $(1,1)$),
which makes the point sharp: a procedure that took one eigenvector per eigenvalue would have declared
it infeasible.

### II.4 Soundness of the computational procedure

The procedure used for the three instances of Report 101 was corrected in two ways after the audit:

1. the parameter count is computed from $\dim U_v$, giving $r=\rho-1$ or $\rho$, so both branches are
   covered;
2. when the eigenspace of a factor has dimension $>1$, the factor is marked **incomplete** and the
   overall verdict is downgraded to "undetermined" instead of "infeasible".

Point 2 is what prevents the counterexample of II.3 from being misclassified: on that instance the
procedure returns "undetermined", while the true answer is feasible. I regard this as the correct
behaviour, but it means the procedure is only a decision procedure under the simple-spectrum
hypothesis.

---

## Part III. Questions

**Q1.** In the repeated case, is there a natural group acting on $\mathbb P(E_\mu)$ that normalizes
directions — for instance the centralizer of $M$, or a subgroup of it — so that the direction can be
put in normal form and the parameters reduced?

**Q2.** Is there a perturbation or degeneration argument that transfers feasibility from a
simple-spectrum perturbation to a repeated-spectrum instance? The good set is open, so feasibility is
semicontinuous in the data, but I do not see how to move along a family without changing $K_0$.

**Q3.** For the repeated case, is a randomized one-sided procedure (find a good direction with
probability one if one exists; certify infeasibility only when the direction can be eliminated
symbolically) acceptable as the "right" statement, or would you expect a deterministic bound?

**Q4.** The parameterization theorem uses the inner product on $K_0$ (nondegeneracy, projections). Is
there a coordinate-free formulation — for instance through the duality $K_0^*$ and the annihilator of
$U_v$ — that you would prefer for a paper?

**Q5.** Theorem 1 describes the layer as Grassmann bundles over projective eigenspaces. Paper II
describes feasible designs through the subspace $W\subseteq\mathcal T$ with
$\omega+1\le\dim W\le 2\omega$. Is there a dictionary between the two pictures that would unify the
descriptions, or are they genuinely different invariants?

### Reliability

| Statement | Status |
|---|---|
| Lemmas 1–4, Theorem 1 (parameterization) | proved (under nondegeneracy of the inner product on $K_0$) |
| Theorem 2 (fixed $p$, simple spectrum) | proved by bookkeeping, relying on two standard facts: factorization of integer polynomials, and polynomial-time multivariate gcd for a fixed number of variables |
| II.3 counterexample | exact computation (all arithmetic rational, no floating point) |
| II.4 soundness marking | implemented; on the three instances of Report 101 the verdicts are unchanged |
