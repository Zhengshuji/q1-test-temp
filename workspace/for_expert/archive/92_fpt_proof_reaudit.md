# Second audit request: the bit-complexity proof of DEC, OPT and FIND in FPT(rank AN)

## Part I. Problem, model, and the claim under audit

**Data.** Rational $A\in\mathbb Q^{n\times n}$, $C\in\mathbb Q^{p\times n}$, $L_0\in\mathbb Q^{r_0\times n}$,
integer $q\ge r_0$. With $r=q-r_0$, free rows $R\in\mathbb R^{r\times n}$, $L=[L_0;R]$, feasibility is

$$\operatorname{rank}\begin{bmatrix}LA\\L\\CA\\C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}L\\CA\\C\end{bmatrix},\qquad
\operatorname{rank}\begin{bmatrix}\lambda L-LA\\CA\\C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}L\\CA\\C\end{bmatrix}\ \ \forall\lambda\in\mathbb C .$$

**Model (row slot).** The order is the number of rows of $L$; redundant and zero rows are allowed; the
only conditions are the two rank equalities. The reduced order of the control literature,
$\operatorname{rank}[C;L]-\operatorname{rank}C$, is a different problem: zero padding does not
increase it, so the monotonicity and the formula for $q_{\min}$ below do not transfer.

**Notation.** $K_0=\ker[C;CA]$, $N$ a rational basis of $K_0$ ($n\times k$), $M=[N\ AN]$,
$T=\operatorname{row}M$, $S=\operatorname{row}(AN)\subseteq\mathbb R^k$, $\ell=\dim S=\operatorname{rank}(AN)$,
$B=LM=[H\ H_A]$, $W=\operatorname{row}B$, $W_0=\operatorname{row}(L_0M)$, $s_0=\dim W_0$,
$V=T\cap(S\times S)$, $m'=\dim V-s_0$. $\mathcal L$ is the input bit length.

**Claim.** With $\ell=\operatorname{rank}(AN)$, the row-slot problems satisfy

$$\mathrm{DEC},\ \mathrm{OPT}:\ f(\ell)\operatorname{poly}(\mathcal L),\qquad
\mathrm{FIND}:\ f(\ell)\operatorname{poly}(\mathcal L)\ \text{with an exact algebraic witness},\qquad
f(\ell)=\exp\bigl(O(\ell^2\log(\ell+2))\bigr).$$

**Notation used below.** $\sigma_j(X)$ is the $j$-th elementary symmetric polynomial of a real symmetric
$X$ (the sum of its principal minors of order $j$; $\sigma_j=0$ by convention if $j$ exceeds the size);
$\mathbf e_1=(1,0,\dots,0)^{\mathsf T}$.

## Part II. The proof, with the five corrections of the previous round applied

### Lemma 1 (rank compression)
For $J=[CA;C]$ and any $Q$ with $n$ columns, $\operatorname{rank}[J;Q]=\operatorname{rank}J+\operatorname{rank}(QN)$.
Proof: $N$ spans $\ker J$, so adjoining $Q$ contributes exactly the rank of $Q$ restricted to $\ker J$.

### Lemma 2 (the conditions see only $W$)
(5a) $\iff\pi_2(W)\subseteq\pi_1(W)$; (5b) $\iff\dim\pi_\lambda(W)=\dim\pi_1(W)$ for all $\lambda$, where
$\pi_1(h,g)=h$, $\pi_2(h,g)=g$, $\pi_\lambda(h,g)=\lambda h-g$.

**Complexification.** \(W\) is real and $\lambda$ is complex, so $\pi_\lambda$ is meant on
$W_{\mathbb C}=W\otimes_{\mathbb R}\mathbb C\subseteq\mathbb C^{2k}$. A real matrix has the same rank over
$\mathbb R$ and $\mathbb C$, so the conditions are unchanged, but the statement now makes sense for
complex $\lambda$.

### Lemma 3 (sandwich and realisation)
For $L=[L_0;R]$: $W_0\subseteq W\subseteq T$ and $\dim(W/W_0)\le r$. Conversely every $W$ with these
properties is realised by some $R$ with exactly $t=\dim(W/W_0)$ free rows ($u\mapsto uM$ is onto $T$;
take preimages of a basis of $W/W_0$).

### Lemma 4 (structural bound)
If $W$ is feasible with $\omega=\dim\pi_1(W)>0$, then $\omega+1\le\dim W\le2\omega$.

Upper: (5a) gives $\pi_2\subseteq\pi_1$; (5b) at $\lambda=0$ gives $\dim\pi_2=\dim\pi_1$, so
$\pi_1(W)=\pi_2(W)=U$ and $W\subseteq U\times U$. Lower: if $\dim W=\omega$ then $W$ is the graph of an
endomorphism $F$ of $U$; over $\mathbb C$ it has an eigenvalue $\lambda_0$, and $\pi_{\lambda_0}(W)$ is
$(\lambda_0 I-F)U$, of dimension $<\omega$. For $\omega=0$, $W=0$.

Consequently $s_0+t\in\{\omega+1,\dots,2\omega\}\cup\{0\}$ and
$\max(0,\omega+1-s_0)\le t\le\min(r,2\omega-s_0)$.

### Lemma 5 (monotonicity and saturation)
Zero padding preserves feasibility, so $\mathrm{DEC}(q)\Rightarrow\mathrm{DEC}(q+1)$, and
$\mathrm{DEC}(r_0+r)=\mathrm{DEC}(r_0+d-s_0)$ for $r\ge d-s_0$.

### Lemma 6 (minimum order)
$q_{\min}=r_0+t_{\min}$ with $t_{\min}=\min\{\dim(W/W_0):W\text{ feasible}\}\le2\ell$, since
$\dim W\le2\omega\le2\ell$ and $t=\dim W-s_0$. Binary search on $[0,2\ell]$ therefore works:
$\lceil\log_2(2\ell+1)\rceil+1$ decisions.

### Reduction to $\ell$ (correction 1 applied)
A feasible $W$ has $\pi_1(W)=\pi_2(W)=U\subseteq S$, hence $W\subseteq U\times U\subseteq S\times S$ and in
particular $W_0\subseteq S\times S$; if this finite exact test fails, the instance is infeasible at every
order. Choose a rational basis of $S$, extend it to a rational basis of $\mathbb Q^k$, and let $P$ be the
corresponding invertible matrix. **Right multiplication by $P$ does not preserve row spaces as subsets**
($\operatorname{row}(XP)\ne\operatorname{row}(X)$); what it preserves is ranks, row-space inclusions,
row-space equalities, and the pencil rank conditions. After the change, every feasible row is supported
on the first $\ell$ coordinates.

### Encoding (corrections 2, 3 applied)
Fix $t$, $\omega\ge1$ and a chart of $\operatorname{Gr}(t,m')$, $m'\le2\ell$; the number of charts is
$2^{m'}\le4^\ell$.

**$\omega=0$ is handled before the encoding**: $W=0$ is feasible iff $W_0=0$, with no free rows. So only
$\omega\ge1$ enters the formulas below.

**Chart in the quotient.** Fix a rational basis $E_0$ of $W_0$ and a rational complement $E_Q$ of $W_0$ in
$V$; a chart gives $[I_t\mid Y]$, $Y\in\mathbb R^{t\times(m'-t)}$, and
$$Z(Y)=\begin{bmatrix}E_0\\ [I_t\mid Y]E_Q\end{bmatrix}\in\mathbb R^{\nu\times2k},\qquad \nu=s_0+t,$$
with affine entries. Candidates automatically contain $W_0$.

**Formulas**, with $Z(Y)=[H(Y)\ G(Y)]$ and $P_Y(\lambda)=\lambda H(Y)-G(Y)$:
$$\sigma_\omega(HH^{\mathsf T})>0,\qquad
\sigma_{\omega+1}\!\left(\begin{bmatrix}H\\G\end{bmatrix}
\begin{bmatrix}H\\G\end{bmatrix}^{\!\mathsf T}\right)=0,\qquad
B(Y)^{\mathsf T}B(Y)\,x=\mathbf e_1 .$$
$B(Y)$ has rows indexed by the coefficient vectors of $\lambda^j f_{I,J}$, $0\le j<\omega$,
$f_{I,J}(\lambda;Y)=\det P_Y(\lambda)_{I,J}$, so
$$B(Y)\in\mathbb R^{\,\omega\binom{\nu}{\omega}\binom{\ell}{\omega}\times2\omega},$$
**exactly $2\omega$ columns**. $B^{\mathsf T}Bx=\mathbf e_1\iff\mathbf e_1\in\operatorname{row}B(Y)\iff$
the $f_{I,J}$ have a Bézout identity of degree $<\omega\iff$ no common complex zero.

Sizes: $S_{\rm poly}=2+2\omega$, $D\le2\omega+2$, $N_{\rm var}=t(m'-t)+2\omega\le\ell^2+2\ell$.

**Branch pruning before construction.** $\sigma_{\omega+1}$ acts on a $\nu\times\nu$ Gram matrix whose
minors number $\binom{\nu}{\omega}$; this is $\le\binom{2\omega}{\omega}\le4^\omega$ only when
$\nu\le2\omega$. Without the pruning there is no bound in terms of $\ell$.

**Cauchy–Binet.** $\sum_{|J|=\omega}\det(P_{:,J}(\lambda)^{\mathsf T}P_{:,J}(\mu))
=\sum_{I,J}f_{I,J}(\lambda)f_{I,J}(\mu)$; the row sum is eliminated and the column subsets are those of
the **reduced** matrix, so the factor is $\binom{\ell}{\omega}\le2^\ell$, not $\binom{k}{\omega}$.

### Lemma 8 (coefficient height, correction 4 applied)
After rational preprocessing and coordinate compression, every coefficient of every polynomial defining
the system has bit height
$$\tau_{\rm cert}\le\operatorname{poly}(\mathcal L)+O\bigl(\omega\log(\omega+2)\bigr)+\ell
=\operatorname{poly}(\mathcal L).$$
*Proof sketch.* (a) The bases $N$, $S$, $E_0$, $E_Q$ come from Gaussian elimination on $n\times n$ rational
matrices; by Hadamard, $j$-th order minors have height $O(j(\tau_{\rm in}+\log j))$, and elimination does
not increase this beyond a polynomial factor, so all four matrices have height $\tau_0=\operatorname{poly}(\mathcal L)$.
(b) The chart matrix $Z(Y)$ is affine in $Y$ with coefficients from $E_0,E_Q$, height $\tau_0$.
(c) Each entry of $P_Y(\lambda)_{I,J}$ is affine in $(\lambda,Y)$ with height $\tau_0+1$; expanding an
$\omega\times\omega$ determinant gives at most $\omega!$ products of $\omega$ factors, so the coefficients
of $f_{I,J}$ have height $O(\omega\tau_0+\log(\omega!)+O(\omega\log(\omega+2)))$.
(d) The Cauchy–Binet kernel is a sum of $\binom{\ell}{\omega}\le2^\ell$ such determinants, which adds only
$\ell$ bits; $\sigma_\omega$ and $\sigma_{\omega+1}$ are sums of at most $\binom{\nu}{\omega}\le4^\omega$
principal minors, adding $2\omega$ bits.

### Lemma 9 (representation length, correction 5 applied — the previously open gap)
**Citation.** Basu–Pollack–Roy, *Algorithms in Real Algebraic Geometry*, 2nd ed., Springer 2006,
§13.1, **Theorem 13.11**: for $s$ polynomials of degree $\le d$ in $k$ variables with integer coefficients
of bit size $\le\tau$, the algorithm produces points meeting every nonempty sign condition with univariate
representations satisfying
$$\deg\le O(d)^k,\qquad \text{coefficient bit size}\le\tau\,d^{O(k)},\qquad
\#\text{points}\le s^{O(k)}d^{O(k)} .$$

**Substitution.** Variables $k\leftarrow N_{\rm var}\le\ell^2+2\ell$; degree $d\leftarrow D\le2\ell+2$;
$s\leftarrow S_{\rm poly}\le2\omega+2$; height $\tau\leftarrow\tau_{\rm cert}\le\operatorname{poly}(\mathcal L)$
(Lemma 8), after clearing denominators (which multiplies by a rational of bit size
$\operatorname{poly}(\mathcal L)$ and does not change the zero set). Then
$$\deg\le(2\ell+2)^{O(\ell^2)}=\exp\bigl(O(\ell^2\log(\ell+2))\bigr),$$
$$\text{height}\le\operatorname{poly}(\mathcal L)(2\ell+2)^{O(\ell^2)}
=\exp\bigl(O(\ell^2\log(\ell+2))\bigr)\operatorname{poly}(\mathcal L).$$
The representation consists of $N_{\rm var}+1$ polynomials ($P,Q_0,\dots,Q_{N_{\rm var}}$), each of degree
$\le\deg$ and coefficients of that height, hence
$$L_{\rm out}\le(N_{\rm var}+1)(\deg+1)(\text{height}+1)
=\exp\bigl(O(\ell^2\log(\ell+2))\bigr)\operatorname{poly}(\mathcal L).$$

**From arithmetic to bits.** Every arithmetic operation acts on coefficients of height $\le B$, at cost
$\operatorname{poly}(B)$, and the operation count is $\exp(O(\ell^2\log(\ell+2)))$; hence the bit cost is
$\exp(O(\ell^2\log(\ell+2)))\operatorname{poly}(\mathcal L)$.

**Recovering $R$.** Each entry of $R$ is $Q_j(\theta)/Q_0(\theta)$ for an algebraic $\theta$ of degree
$\le\deg$; building the multiplication table of $\theta$ costs $O(\deg^2)$ coefficient operations and
evaluating entry by entry costs $\operatorname{poly}(L_{\rm out})$, so the reconstruction does not change
the order. The witness is an exact real algebraic number; no rational witness is promised.

### Lemma 10 (preprocessing, new)
Given rational input, the following are constructed in
$\exp(O(\ell\log(\ell+2)))\operatorname{poly}(\mathcal L)$ bit operations: $N$ and a basis of $K_0$,
$M=[N\ AN]$, bases of $T$ and $S$, a basis of $W_0$, a basis of $V=T\cap(S\times S)$, the complement
$E_Q$, and the affine coefficient data of every chart matrix $Z(Y)$.
*Proof sketch.* The first items are null-space and row-space computations on $n\times n$ rational
matrices ($O(n^3)$ field operations of height $\operatorname{poly}(\mathcal L)$). $V$ is computed from
$\dim(V_1\cap V_2)=\dim V_1+\dim V_2-\operatorname{rank}[B_1;B_2]$ by elimination on the stacked bases.
$Z(Y)$ needs no extra computation: its coefficients are the entries of $E_0,E_Q$. There are
$\binom{m'}{t}\le2^\ell$ charts, each with $O(\ell^2)$ coefficients.

### Decision bound
Renegar's Part II: $B(\log B)(\log\log B)(SD)^{O(N)}$ with $B=\tau_{\rm cert}$. Then
$(S_{\rm poly}D)^{O(N_{\rm var})}=(O(\omega^2))^{O(\ell^2)}=\exp(O(\ell^2\log(\ell+2)))$, and the height
factor is absorbed. Multiplying by $4^\ell$ charts and $O(\ell^2)$ pairs $(t,\omega)$,
$$T_{\rm DEC}=\exp\bigl(O(\ell^2\log(\ell+2))\bigr)\operatorname{poly}(\mathcal L).$$

### OPT
By monotonicity and Lemma 6, binary search on $[0,2\ell]$:
$T_{\rm OPT}=\exp(O(\ell^2\log(\ell+2)))\operatorname{poly}(\mathcal L)$; if $t=2\ell$ is infeasible,
$q_{\min}=+\infty$.

### Scope and model
Row-slot model only. The reduced-order problem is not addressed. The abstract, the problem section and
the limitations section state this. The row-slot model is meaningful on its own: the number of available
design slots is often itself the resource, independently of whether a row is redundant.

## Part III. Questions

1. **Lemma 8.** Are the four parts (a)–(d) complete, and are the constants right? In particular: is the
   height of the chart matrix really $\tau_0$, i.e. do we avoid reintroducing $k$ through the basis
   matrices of $S$ and of the complement? And is the $\binom{\nu}{\omega}\le4^\omega$ step in (d) the
   right place to use the pruning?

2. **Lemma 9.** Is the substitution $k\leftarrow N_{\rm var}$, $d\leftarrow D$, $\tau\leftarrow\tau_{\rm cert}$
   the intended use of Theorem 13.11? In particular: (i) does Theorem 13.11 apply to a formula that is a
   Boolean combination of sign conditions rather than to a single sign condition; (ii) is the height in
   Theorem 13.11 the height of the input coefficients only, or must we add the cost of the sign-condition
   enumeration; (iii) is the recovery step from a univariate representation to the rows of $R$ correctly
   accounted, or does evaluating $Q_j(\theta)/Q_0(\theta)$ hide a factor?

3. **Lemma 10.** Is $\exp(O(\ell\log(\ell+2)))\operatorname{poly}(\mathcal L)$ the right shape for the
   preprocessing, or should one of the terms be larger (for instance the construction of $V$ or of the
   complement $E_Q$)?

4. **The $\omega=0$ branch.** We test $W_0=0$ before the encoding and then restrict to $\omega\ge1$. Does
   this interact badly with $t$ (for instance, could an instance with $W_0=0$ and $t>0$ require an
   $\omega\ge1$ branch), and is the statement "feasible iff $W_0=0$" correct at every order?

5. **Scope.** Is stating the row-slot model in the abstract, the problem section and the limitations
   section enough, or should the title itself carry the restriction?

6. **Anything else that blocks submission.** With the corrections of the previous round applied and
   Lemma 9 closing the witness-size gap, is there any remaining mathematical or complexity objection that
   would prevent treating the three-part theorem as submission-ready?
