# Complete paper-level proof: DEC, OPT and FIND are fixed-parameter tractable in the rank of AN

## Part I. Problem, model, notation

**Data.** Rational matrices $A\in\mathbb Q^{n\times n}$, $C\in\mathbb Q^{p\times n}$,
$L_0\in\mathbb Q^{r_0\times n}$, and an integer $q\ge r_0$. With $r=q-r_0$ the free rows
$R\in\mathbb R^{r\times n}$ are design variables and $L=[L_0;R]$ has $q$ rows. Feasibility is

$$\operatorname{rank}\begin{bmatrix}LA\\L\\CA\\C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}L\\CA\\C\end{bmatrix},\qquad
\operatorname{rank}\begin{bmatrix}\lambda L-LA\\CA\\C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}L\\CA\\C\end{bmatrix}\ \ \forall\lambda\in\mathbb C .$$

$\mathrm{DEC}(q)$ decides feasibility at order $q$; $\mathrm{OPT}$ asks for the least feasible $q$;
$\mathrm{FIND}$ asks for a witness $R$ at that order.

**Model.** This is the *row-slot* model: the order is the number of rows of $L$; redundant rows and
zero rows are allowed; the only conditions are the two rank equalities above. This must be stated
with every claim, because the *reduced* order of the control literature, defined through
$\operatorname{rank}[C;L]-\operatorname{rank}C$, is a different decision problem: zero padding
does not increase the reduced order, so the monotonicity and the formula for $q_{\min}$ below do
not transfer to it.

**Compression.** $K_0=\ker[C;CA]$, $N\in\mathbb R^{n\times k}$ a basis of $K_0$,
$M=[N\ AN]\in\mathbb R^{n\times 2k}$, $T=\operatorname{row}M$, $d=\dim T$,
$S=\operatorname{row}(AN)\subseteq\mathbb R^k$ (the submodule of the *second* block),
$\ell=\operatorname{rank}(AN)=\dim S\le k$. For $L=[L_0;R]$ put $B=LM=[H\ H_A]$ and
$W=\operatorname{row}B$. Finally $W_0=\operatorname{row}(L_0M)$, $s_0=\dim W_0$.

## Part II. Results and proofs

### 1. The conditions are conditions on $W$

Take $J=[CA;C]$; its kernel is $\operatorname{im}N$. The rank-compression identity
$$\operatorname{rank}\begin{bmatrix}J\\Q\end{bmatrix}=\operatorname{rank}J+\operatorname{rank}(QN)$$
holds for every $Q$ with $n$ columns. With $Q=[LA;L]$ it turns (5a) into
$\operatorname{rank}[H_A;H]=\operatorname{rank}H$, i.e. $\pi_2(W)\subseteq\pi_1(W)$; with
$Q=\lambda L-LA$ it turns (5b) into $\operatorname{rank}(\lambda H-H_A)=\operatorname{rank}H$, i.e.
$\dim\pi_\lambda(W)=\dim\pi_1(W)$ for all $\lambda$. Here $\pi_1(h,g)=h$, $\pi_2(h,g)=g$,
$\pi_\lambda(h,g)=\lambda h-g$.

Two facts about $W$ then follow directly. First, $W_0\subseteq W\subseteq T$ and
$\dim(W/W_0)\le r$; conversely every $W$ with these three properties is realised by some $R$ with
exactly $t=\dim(W/W_0)$ free rows, because $u\mapsto uM$ maps onto $T$ and one takes preimages of
a basis of $W/W_0$.

Second, **monotonicity and saturation**: appending zero rows preserves both conditions, so
$\mathrm{DEC}(q)\Rightarrow\mathrm{DEC}(q+1)$; and $\dim(W/W_0)\le\dim(T/W_0)$, so
$\mathrm{DEC}(r_0+r)=\mathrm{DEC}(r_0+d-s_0)$ for $r\ge d-s_0$.

### 2. Structural bound

If $W$ is feasible with $\omega=\dim\pi_1(W)>0$, then
$$\omega+1\le\dim W\le2\omega .$$
Upper bound: (5a) gives $\pi_2(W)\subseteq\pi_1(W)$, and (5b) at $\lambda=0$ gives
$\dim\pi_0(W)=\dim\pi_1(W)=\omega$; since $\pi_0(W)=\pi_2(W)$ up to sign,
$\pi_1(W)=\pi_2(W)=:U$ and $W\subseteq U\times U$. Lower bound: if $\dim W=\omega$ then both
projections are isomorphisms, $W$ is the graph of an endomorphism $F$ of $U$; over $\mathbb C$,
$F$ has an eigenvalue $\lambda_0$ and $\pi_{\lambda_0}(W)=(\lambda_0 I-F)U$ has dimension $<\omega$.
For $\omega=0$, $W=0$, which is feasible exactly when $W_0=0$.

Consequently $s_0+t=\dim W\in\{\omega+1,\dots,2\omega\}\cup\{0\}$, so
$$\max(0,\omega+1-s_0)\le t\le\min(r,2\omega-s_0).$$

### 3. Coordinates in $S$, and why the parameter is $\ell$ and not $k$

A feasible $W$ satisfies $\pi_1(W)=\pi_2(W)=U\subseteq S$, hence $W\subseteq T\cap(S\times S)$ and
$W\subseteq U\times U$ with $\dim U=\omega\le\ell$. Choose a rational basis of $S$ and extend it to
a rational basis of $\mathbb R^k$; the corresponding invertible matrix $Y_S\in\mathbb Q^{k\times k}$
puts every $H$ and $H_A$ into coordinates in $\mathbb R^\ell$, and row spaces are unchanged by
right multiplication by an invertible matrix. All counts below therefore use $\ell$.

If $W_0\not\subseteq S\times S$, no feasible $W$ exists at any order; this is a finite, exact test.

### 4. Encoding

Fix $t$, $\omega\ge1$, and a chart of $\operatorname{Gr}(t,m')$ with
$m'=\dim\bigl(T\cap(S\times S)\bigr)-s_0\le2\ell$. The number of charts is
$\sum_t\binom{m'}{t}=2^{m'}\le4^\ell$.

**Variables**: $Y\in\mathbb R^{t\times(m'-t)}$ (chart coordinates) and $x\in\mathbb R^{2\omega}$
(the certificate), so
$$N_{\rm var}=t(m'-t)+2\omega\le\tfrac{m'^2}{4}+2\omega\le\ell^2+2\ell .$$

**Formulas**. With $Z(Y)=[H(Y)\ G(Y)]$ a basis matrix of $W$ (its entries affine in $Y$; $\nu=s_0+t$
rows), impose
$$e_\omega(HH^{\mathsf T})>0,\qquad
e_{\omega+1}\!\left(\begin{bmatrix}H\\G\end{bmatrix}
\begin{bmatrix}H\\G\end{bmatrix}^{\!\mathsf T}\right)=0,\qquad
B(Y)^{\mathsf T}B(Y)\,x=e_0 .$$
The first two say $\operatorname{rank}H=\omega$ and $\operatorname{row}G\subseteq\operatorname{row}H$.
The matrix $B(Y)$ has **exactly $2\omega$ columns**: it collects the coefficient vectors of
$f_{I,J},\lambda f_{I,J},\dots,\lambda^{\omega-1}f_{I,J}$ for all $\omega\times\omega$ minors
$f_{I,J}(\lambda;Y)=\det P_Y(\lambda)_{I,J}$ of $P_Y(\lambda)=\lambda H(Y)-G(Y)$; the equation says
$e_0\in\operatorname{row}B(Y)$, i.e. the minors have a Bézout identity of degree $<\omega$, i.e. no
common complex zero. Its Cauchy–Binet form is
$$\sum_{|J|=\omega}\det\bigl(P_{:,J}(\lambda)^{\mathsf T}P_{:,J}(\mu)\bigr)
=\sum_{I,J}f_{I,J}(\lambda)f_{I,J}(\mu),$$
so $B^{\mathsf T}B$ is computed from $\binom{k}{\omega}\le2^k$ terms without enumerating
$\binom{\nu}{\omega}$ row minors.

**Branch pruning is part of the complexity proof, not an optimisation.** The number of row subsets
is $\binom{\nu}{\omega}$, which is bounded by $\binom{2\omega}{\omega}\le4^\omega$ only under
$\nu\le2\omega$; without the pruning there is no bound in terms of $\ell$ alone.

**Sizes.** $S_{\rm poly}=2+2\omega$, $D\le2\omega+2$; the height of a single coefficient is
$\tau_{\rm cert}\le\operatorname{poly}(\mathcal L)+O(\omega\log(\omega+2))$, while the length of
the expanded formula is $L_{\rm formula}\le2^{O(\omega\log(\omega+2))}\operatorname{poly}(\mathcal L)$.
The two must be kept apart: Renegar's bound uses $\tau_{\rm cert}$; $L_{\rm formula}$ only enters the
cost of writing the formula down.

### 5. Decision bound

For each chart and each $(t,\omega)$, Renegar's Part II bound
$B(\log B)(\log\log B)(SD)^{O(N)}$ gives
$$(S_{\rm poly}D)^{O(N_{\rm var})}=(O(\omega^2))^{O(\ell^2)}
=\exp\bigl(O(\ell^2\log(\ell+2))\bigr),\qquad
B\log B\log\log B=\operatorname{poly}(\mathcal L)\cdot2^{O(\ell\log(\ell+2))},$$
the second absorbed by the first. Multiplying by the number of charts and of $(t,\omega)$ pairs,
$$T_{\rm DEC}\le4^\ell\cdot O(\ell^2)\cdot\exp\bigl(O(\ell^2\log(\ell+2))\bigr)\operatorname{poly}(\mathcal L)
=\exp\bigl(O(\ell^2\log(\ell+2))\bigr)\operatorname{poly}(\mathcal L).$$

### 6. Minimum order

By monotonicity, $t\mapsto\mathrm{DEC}(r_0+t)$ is nondecreasing, and
$t_{\min}=\min\{\dim(W/W_0):W\text{ feasible}\}$ satisfies $t_{\min}\le2\ell$ (indeed
$t_{\min}\le2\omega-s_0$). Hence $q_{\min}=r_0+t_{\min}$, and binary search on $[0,2\ell]$ uses
$\lceil\log_2(2\ell+1)\rceil+1$ decisions:
$$T_{\rm OPT}=\exp\bigl(O(\ell^2\log(\ell+2))\bigr)\operatorname{poly}(\mathcal L).$$
If $t=2\ell$ is infeasible then no feasible $W$ exists (by saturation) and $q_{\min}=+\infty$.

### 7. Construction

Use the sign-condition sample-point theorem (Basu–Pollack–Roy, *J. Complexity* 13 (1997) 28–37):
given $S_{\rm poly}$ polynomials of degree $\le D$ in $N$ variables, a set of points meeting every
nonempty sign condition can be computed in $S_{\rm poly}^{N+1}D^{O(N)}$ arithmetic operations, the
points being exact real algebraic numbers. Nonempty sign conditions include the open ones, so no
closedness assumption is needed. Our formula is a Boolean combination of sign conditions, hence
nonempty iff one of the realisable sign conditions is compatible with it.

From a sample point $Y^*$ one reconstructs a basis of $U$, then of $W$, and applies a rational
linear section $\sigma:T\to\mathbb Q^{1\times n}$ with $\sigma(w)M=w$ (a right inverse of $M$,
computed once) to obtain algebraic free rows. The result is an exact real algebraic witness $R$.

Cost: arithmetic $S_{\rm poly}^{N+1}D^{O(N)}=\exp(O(\ell^2\log(\ell+2)))$; bit cost
$\exp(O(\ell^2\log(\ell+2)))\operatorname{poly}(\mathcal L)+\operatorname{poly}(L_{\rm out})$ with
$L_{\rm out}\le(\tau_{\rm cert}+\log S_{\rm poly})D^{O(N)}$. No rational witness is promised.

### 8. Formalisation status

Lean 4 with Mathlib, full build (9116 jobs), the only axioms being `propext`, `Classical.choice`,
`Quot.sound`. Formalised: the compression identity in abstract form
$\dim\operatorname{range}(f\times g)=\dim\operatorname{range}f+\dim\operatorname{map}g(\ker f)$;
the equivalence "rank additivity iff inclusion"; the row-space bridge
$\operatorname{rank}M=\dim\operatorname{row}M$ and
$\operatorname{row}[A;B]=\operatorname{row}A\sqcup\operatorname{row}B$; the matrix form of the
algebraic condition $\operatorname{rank}[A;B]=\operatorname{rank}B\iff\operatorname{row}A\le
\operatorname{row}B$; the pencil interface (constant rank versus pointwise equality, and
$\operatorname{rank}(HA)=\operatorname{rank}H$ from the spectral condition at zero); and step 3,
$\operatorname{row}H_A=\operatorname{row}H$.

Not formalised: $\dim W\le2\omega$ (blocked, see below), $\omega+1\le\dim W$ (needs graphs and
eigenvalues), $q_{\min}=r_0+t_{\min}$, and of course the analytic complexity statements.

## Part III. Questions

1. **Is the paper proof acceptable?** In particular: Lemma 2 (the two conditions as conditions on
   $W$), the structural bound including the eigenvalue argument, and the passage from $k$ to $\ell$
   by the coordinate change in $S$. Is there a gap in the claim that $W_0\not\subseteq S\times S$
   implies infeasibility at every order?

2. **Is the row-slot scope statement sufficient?** We claim only the row-slot problem here, and we
   say explicitly that the reduced-order problem is not settled. Is that the right way to bound the
   claim, or should the reduced-order version be proved as well to be publishable?

3. **The bit model for the witness.** We state the arithmetic bound of the sample-point theorem and
   add the output-length term. Is that the correct way to turn it into a bit-complexity statement,
   and is the bound $L_{\rm out}\le(\tau+\log S)D^{O(N)}$ the one you would cite?

4. **The encoding.** We claim that $B(Y)$ has exactly $2\omega$ columns and that
   $B^{\mathsf T}Bx=e_0$ is equivalent to the existence of a Bézout identity of degree $<\omega$.
   Is the degree bookkeeping right, and is the factor $\binom{k}{\omega}\le2^k$ enough for the
   height estimate $\tau_{\rm cert}=\operatorname{poly}(\mathcal L)+O(\omega\log\omega)$?

5. **Which parameter should we advertise?** We now have three candidates: $k$,
   $\ell=\operatorname{rank}(AN)$, and the iterated common-projection core $S_*$ (terminal space of
   $T_j=T\cap(S_j\times S_j)$, $S_{j+1}=\pi_1(T_j)\cap\pi_2(T_j)$). On random instances the core did
   not shrink below $\ell$. Is $\ell$ the right headline, with $S_*$ as a refinement?

6. **Two Lean obstructions, in case you know a route.**
   (a) We need $\dim(U_1\times U_2)=\dim U_1+\dim U_2$ for submodules $U_i$ of a product; Mathlib has
   no `Submodule.finrank_prod`. Is there a canonical short proof, or should we build the linear
   equivalence by hand?
   (b) For $\omega+1\le\dim W$ we must formalise: both projections isomorphic implies $W$ is the
   graph of an endomorphism, an endomorphism of a finite-dimensional complex vector space has an
   eigenvalue, and at that eigenvalue $\pi_\lambda$ drops rank. Is there an existing Mathlib
   development of this chain (eigenvalue existence over an algebraically closed field, graph of a
   linear map as a submodule) that we should reuse instead of writing it from scratch?
