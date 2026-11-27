# Progress toward $q1$: what is settled, what blocks, and where to go next

This note is written with one purpose: to advance question $q1$ (the complexity of the minimal-order
problem). It is not about producing a paper. We therefore report only the facts that bear on $q1$,
state plainly what we believe the remaining obstruction is, and ask for direction.

---

# Part I. Problem and the formal decision object

## I.1 Data and conditions

Given $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, a row block $L_0\in\mathbb C^{r\times n}$,
and an integer $q\ge r$, let $\mathcal L=\begin{bmatrix}L_0\\R\end{bmatrix}\in\mathbb C^{q\times n}$ and require

$$(5a)\ \operatorname{rank}\begin{bmatrix}\mathcal LA\\ \mathcal L\\ CA\\ C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}\mathcal L\\ CA\\ C\end{bmatrix},
\qquad
(5b)\ \operatorname{rank}\bigl[\lambda\mathcal L-\lambda\mathcal LA;\ CA;\ C\bigr]=h\ \ \forall\lambda\in\mathbb C,$$

with $h=\operatorname{rank}[\mathcal L;CA;C]$. Let $q_{\min}=\min\{q:\exists R\text{ satisfying }(5a),(5b)\}$.
Question $q1$: is computing $q_{\min}$ NP-hard?

## I.2 The formal object we work with

Following earlier advice, the complexity object is the decision problem

$$\mathrm{DEC}(q):\quad \text{given }(A,C,L_0,q),\ \text{does there exist } R\in\mathbb R^{(q-r)\times n}
\text{ with }(5a),(5b)?$$

The optimisation problem is at least as hard as its threshold version, so hardness for $\mathrm{DEC}$
suffices for $q1$, and an algorithm for $q_{\min}$ yields an algorithm for $\mathrm{DEC}$.

## I.3 What the literature already settles

Fernando (arXiv:2609.33615, arXiv:2609.37992) gives the order spectrum, a per-order necessary and
sufficient condition (existence of $Z$, and of a chart $Z_I(\Theta)$ with $\Theta$ semialgebraic), the
minimal order as the least spectrally feasible order, and constructions. So existence and the
characterisation are not open; the open question is the **complexity of deciding** the existence of
$\Theta$. Static output feedback with bounded order is NP-hard (L\"ofberg, arXiv:2609.16886), which is the
nearest known hardness result.

---

# Part II. Facts we have established that bear on $q1$

## II.1 The spectral obstruction has a small algebraic carrier

Everything is governed by a single subspace. With $K=\ker[C;CA]$, $W_K=\mathcal LK$, $\omega=\dim W_K$,
$D=K\cap\ker\mathcal L$, $d=\dim D=k-\omega$, and $\Phi_K(\mathcal Lv)=\mathcal LAv$ for $v\in K$
(well defined under $(5a)$), one has

$$\dim\ker Q_{\mathcal L}(\lambda)=\dim D+\dim\ker P_K(\lambda),\qquad P_K(\lambda)=\lambda\iota_K-\Phi_K ,$$

and hence $(5b)$ fails iff $\Phi_K$ has an invariant line in $W_K$. The set of such lines is
$$\mathcal E_K=\{[w]\in\mathbb P(W_K):\ \Phi_K(w)\wedge\iota_K(w)=0\},$$
cut by quadratics; no parameter $[\alpha:\beta]$ is needed. Consequently the obstruction lives in
$\mathbb P(W_K)$, of dimension $\omega-1$, and the projection
$\pi:\mathbb P(K)\setminus\mathbb P(D)\to\mathbb P(W_K)$ has fibre dimension exactly $d=k-\omega$.

## II.2 Fixed candidates are decided by gcd of $\omega$-minors

$(5b)\iff\gcd\{\text{all }\omega\times\omega\text{ minors of }P_K\}\in\mathbb C^\times .$

Two consequences we consider important for $q1$:

* the number of minors is $\binom{q}{\omega}$, i.e. a **single** binomial, not a product;
  it is polynomially bounded exactly when $\min(\omega,q-\omega)=O(1)$;
* the criterion is exact, not merely sufficient, and it does not require any Kronecker-form hypotheses.

## II.3 Feasibility is constructible on admissible rank strata

For $0\le k\le\min(q+2p,n)$, put $B(R)=\begin{bmatrix}\mathcal L\\CA\\C\end{bmatrix}$ and
$$\mathcal A_k=\{R:\operatorname{rank}B(R)=k,\ \operatorname{rank}[\mathcal LA;B(R)]=k\},\qquad
\mathcal C_k=\{R\in\mathcal A_k:\ \Delta_k(R)\in\mathbb C^\times\}.$$
Then each $\mathcal A_k$ is constructible, each $\mathcal C_k$ is constructible, and
$$\mathrm{FEAS}=\bigcup_{k=0}^{\min(q+2p,n)}\mathcal C_k ,$$
a finite union of at most $n+1$ strata. The proof of constructibility is: $\Delta_k\in\mathbb C^\times\iff$
there are Bézout multipliers of degree $\le k-1$ with $\sum u_ip_i=1$; matching coefficients gives a linear
system in the multipliers whose data are polynomial in $R$; solvability is the rank condition
$\operatorname{rank}[M(R)\mid b]=\operatorname{rank}M(R)$. A bounded-degree Bézout lemma with bound $d-1$
is elementary and we have a proof.

So the decision problem is: **is a certain explicit constructible set non-empty?** This is a different
object from a general semialgebraic feasibility problem. In particular it is *not* the case that the
bounded tree-width or chart-enumeration obstructions of the general $\exists\mathbb R$ formulation
immediately apply.

## II.4 What is still missing for $q1$

We see only three gaps, and none of them is about the structure of the obstruction:

1. **No reduction.** We have no reduction from a known hard problem to $\mathrm{DEC}$, and no argument
   that the constructible-set formulation is hard. The natural candidates (rank-one feasibility, ideal
   membership, quadratic feasibility over $\mathbb C$) all have the wrong shape so far.
2. **No algorithm.** Deciding non-emptiness of a constructible set given by rank conditions is decidable
   by elimination, but the size of the resulting system grows like $\binom{q}{\omega}$ in the worst
   stratum, so we do not get a polynomial algorithm from the description alone.
3. **Charts versus strata.** The literature's $\Theta$ is a chart-dependent semialgebraic object; our
   stratified description is chart-free. We do not know whether the two formulations have the same
   complexity, and we do not know whether the stratified version is easier.

## II.5 A remark about what the structure does and does not give

The constructibility result does **not** by itself suggest that $\mathrm{DEC}$ is easy. Deciding whether a
constructible set is non-empty can encode hard problems (ideal membership, rank conditions with parameter
dependence). Conversely it also does not suggest hardness: our sets have very special shape (rank
conditions in a matrix that is affine in $R$).

We think the honest summary is: *the obstruction is a low-dimensional projective-algebraic condition whose
dependence on $R$ is affine; the complexity question is whether "$\exists R$ making an affine family of
pencils spectrally clear" is hard.*

---

# Part III. Request: direction

We are not asking about presentation, and we are not interested in writing up results that do not move
$q1$. Concretely:

**Question 1.** Which of the following three routes would you pursue first, and why?

(a) **Hardness.** Look for a reduction to $\mathrm{DEC}$ from a problem about affine families of matrices
with prescribed spectral behaviour (for instance from a rank/eigenvalue feasibility problem, or from
$\exists\mathbb R$-complete geometric problems that admit an affine pencil encoding). Which source
problems would you consider plausible, and which are certainly hopeless?

(b) **Algorithm.** Attempt an algorithm exploiting that the condition is a single gcd of
$\binom{q}{\omega}$ minors with affine dependence on $R$; for example by deciding the existence of $R$
making a family of polynomials have gcd one, which is a question about the ideal generated by the minors
in $\mathbb C[R,\lambda]$. Is the resulting problem one for which the known algorithms (Gr\"obner,
resultants, or the polynomial-matrix literature) give something better than elimination over
$\mathbb C[R]$?

(c) **Barrier.** Show that $\mathrm{DEC}$ is equivalent to a known problem (so that neither hardness nor an
algorithm is available), which would be a genuine result about $q1$ even without resolving it.

**Question 2.** Is there a *known* reduction from static output feedback with bounded order
(L\"ofberg's setting) to the affine-pencil formulation here, or is the gap between the two real? If the
gap is real, does it consist in the quotient structure (the fact that $W_K$ depends on $R$), or in
something else?

**Question 3.** For the smallest nontrivial family ($n=4$, $p=1$, $q=2$, $r=1$), is the feasible set for
$R$ known to be a proper subvariety of $\mathbb R^{2\times 4}$ — and if so, of what dimension and degree?
A concrete small case with a complete description might indicate which of (a)–(c) is realistic.

**Question 4.** If you had to bet on the eventual answer to $q1$ on the basis of the structure in Part II,
which way would you bet, and what single computation or estimate would most cheaply falsify that bet?

We will follow the direction you indicate; our own inclination is (c) first, because it is cheap and it
would tell us whether the problem is genuinely new.
