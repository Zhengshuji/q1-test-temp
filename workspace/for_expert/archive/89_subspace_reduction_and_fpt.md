# A subspace reduction for functional observer feasibility, and parameterized bounds in the nullspace dimension

## Part I. Problem, notation, and the reduction

**Data.** Rational matrices $A\in\mathbb Q^{n\times n}$, $C\in\mathbb Q^{p\times n}$,
$L_0\in\mathbb Q^{r_0\times n}$, and an integer $q\ge r_0$. With $r=q-r_0$ the free rows
$R\in\mathbb R^{r\times n}$ are the design variables and $L=[L_0;R]$. Feasibility is

$$\operatorname{rank}\begin{bmatrix}LA\\L\\CA\\C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}L\\CA\\C\end{bmatrix}
\quad\text{and}\quad
\operatorname{rank}\begin{bmatrix}\lambda L-LA\\CA\\C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}L\\CA\\C\end{bmatrix}\ \ \forall\lambda\in\mathbb C .$$

$\mathrm{DEC}(q)$ is the decision problem at order $q$; $\mathrm{OPT}$ asks for the least
feasible $q$, $\mathrm{FIND}$ for a witness $R$ at that order.

**Compression.** $K_0=\ker[C;CA]$, $N\in\mathbb R^{n\times k}$ a basis of $K_0$,
$M=[N\ AN]\in\mathbb R^{n\times 2k}$, $T=\operatorname{row}M\subseteq\mathbb R^{2k}$,
$d=\dim T=\operatorname{rank}[N\ AN]\le\min(2k,n)$. For $L=[L_0;R]$ put $B=LM=[H\ H_A]$
and $W=\operatorname{row}B\subseteq T$. Finally $W_0=\operatorname{row}(L_0M)$,
$s=\dim W_0$, $m=d-s$.

**The four statements.**

1. *(sandwich)* $W_0\subseteq W\subseteq T$ and $\dim(W/W_0)\le r$;
2. *(realization)* every $W$ with $W_0\subseteq W\subseteq T$ and $\dim(W/W_0)\le r$ is
   realized by some $R$, using exactly $\dim(W/W_0)$ free rows (preimages under
   $u\mapsto uM$, which is onto $T$; the remaining rows are zero);
3. *(the conditions see only $W$)* with $\pi_1(h,g)=h$, $\pi_2(h,g)=g$,
   $\pi_\lambda(h,g)=\lambda h-g$, feasibility is exactly
   $\pi_2(W)\subseteq\pi_1(W)$ and $\dim\pi_\lambda(W)=\dim\pi_1(W)$ for all $\lambda$;
4. *(monotonicity and saturation)* appending zero rows preserves feasibility, so
   $\mathrm{DEC}(q)\Rightarrow\mathrm{DEC}(q+1)$, $\mathrm{DEC}(r_0+r)=\mathrm{DEC}(r_0+m)$
   for $r\ge m$, and $\mathrm{MINDEC}(Q)=\mathrm{DEC}(Q)$.

**A structural bound.** If $W$ is feasible and $\omega=\dim\pi_1(W)>0$, then
$\pi_1(W)=\pi_2(W)$ (from (5a) plus the spectral condition at $\lambda=0$), hence
$W\subseteq U\times U$ for $U=\pi_1(W)$ and $\dim W\le2\omega$; and $\dim W\ge\omega+1$,
because $\dim W=\omega$ would make $W$ the graph of an endomorphism of $U$, which has an
eigenvalue $\lambda_0$ at which $\lambda_0\pi_1-\pi_2$ drops rank. So
$$\omega+1\le\dim W=s+t\le2\omega .$$

**Consequence for the parameter.** Write $W=W_0\oplus U$ with $U\subseteq V$, $V$ a
complement of $W_0$ in $T$, $\dim V=m$. Then $t=\dim U\le\min(r,m)\le2k$, and the problem
becomes: choose $U$ in the Grassmannian $\mathrm{Gr}(t,m)$ so that $W$ satisfies the two
projection conditions. In particular

$$q_{\min}=r_0+t_{\min},\qquad t_{\min}=\min\{\dim(W/W_0):W\text{ feasible}\}\le m\le2k .$$

## Part II. What is proved, what is checked, what is only argued

**Proved on paper.** Statements 1–4 above, the structural bound, and $q_{\min}=r_0+t_{\min}$.
The proofs are short: (1) and (2) are the definition of $T$ and surjectivity of
$u\mapsto uM$; (3) is the compression identity $\operatorname{rank}[J;M]=\operatorname{rank}J+\operatorname{rank}(MN_J)$
applied to $J=[CA;C]$; (4) is immediate from the definitions.

**Checked by exact computer algebra.** With rational arithmetic and an exact
spectral test (gcd of the maximal minors of the pencil):
(i) on random instances, every feasible witness was compressed to $t=\dim(W/W_0)$ and the
compressed witness was re-verified, $36$ out of $36$;
(ii) the sandwich, the bound $\dim(W/W_0)\le r$, the structural bound
$\omega+1\le\dim W\le2\omega$, the round trip from $W$ back to $R$, and monotonicity were
checked on the witnesses found, with no failure after one implementation error of our own
was fixed (we had counted the rows of $W_0$ as free rows in the reconstruction).

**Checked in a proof assistant.** Three lemmas in Lean 4 with Mathlib: the row space of
$M$ is exactly the range of $u\mapsto uM$; every element of the row space has a preimage
(realization); and the row space of $L_0$ is contained in that of $[L_0;R]$ (sandwich).
The remaining three statements need the rank conditions on pencils and are not formalized.

**Argued on paper, with an explicit bit-complexity audit.** For each $(t,\omega)$ and each
chart of $\mathrm{Gr}(t,m)$ the feasibility question is a quantifier-free formula over
$\mathbb R$ in the chart coordinates $Y\in\mathbb R^{t\times(m-t)}$ and the certificate
vector $x\in\mathbb R^{2\omega}$, with
$$N_{\rm var}=t(m-t)+2\omega\le k^2+2k,\qquad s=O(\omega)\le O(k),$$
$$D\le2\omega+2\le2k+2,\qquad
B=\operatorname{poly}(\mathcal L)\cdot2^{O(k\log k)},$$
and the number of charts is $\sum_t\binom mt=2^m\le4^k$. Renegar's Part II bound gives
$$(\text{per chart})\ \le (sD)^{O(N_{\rm var})}B\log B\log\log B
=\exp\bigl(O(k^2\log k)\bigr)\operatorname{poly}(\mathcal L),$$
hence
$$T_{\rm DEC}\le 4^k\cdot O(k^2)\cdot\exp\bigl(O(k^2\log k)\bigr)\operatorname{poly}(\mathcal L)
=f(k)\operatorname{poly}(\mathcal L),\qquad f(k)=\exp\bigl(O(k^2\log k)\bigr),$$
which depends on $k$ only — not on $n$, not on $r$. Consequently
$T_{\rm OPT}\le(2k+1)\,T_{\rm DEC}=f(k)\operatorname{poly}(\mathcal L)$.

**Conditional.** $\mathrm{FIND}$ needs a witness, not only a decision. Under the assumption
that the decision procedure can be made witness-producing at the same asymptotic cost
(sample-point algorithms of the critical-point method, e.g. the "sample points" chapter of
Basu–Pollack–Roy), $\mathrm{FIND}\in\mathrm{FPT}(k)$ with the same $f$. Without that
assumption FIND degrades to "decision plus numerical approximation", which is not exact.

## Part III. Questions

1. **Is the bit-complexity audit right?** In particular the coefficient bound
   $B=\operatorname{poly}(\mathcal L)\cdot2^{O(k\log k)}$ for the certificate built by
   Cauchy–Binet: the entries of the Gram matrix are sums of $\binom{k}{\omega}\le2^k$
   products of two minor coefficients, and each coefficient of a minor is a sum of at most
   $\omega!$ terms, each a product of at most $\omega$ entries of the basis matrices. Is there a factor we are
   missing, and does it matter for the exponent in $f$?

2. **Witness extraction.** Which theorem should we cite for producing a point, and at what
   cost? We need: given a quantifier-free formula with $s$ polynomials of degree $\le D$ in
   $N$ variables and coefficients of bit length $B$, output either "no solution" or a
   solution, in time $(sD)^{O(N)}\operatorname{poly}(B)$ times the bit size of the output.
   Is this available in the form we state, or is the correct bound weaker (for instance with
   an extra factor in $s$ or $D$)?

3. **Is the parameter $k$ interesting to anyone but us?** The chart coordinates of the
   order-by-order characterization available in the literature number $d(m_L-d)=(n-p-q)(q-r)$
   per chart, which grows with $n$ even for fixed $q$; ours number $t(m-t)\le k^2$ and are
   independent of $r$. Is that the right way to state the improvement, or should we compare
   something else?

4. **Does the reduction need a hypothesis we have overlooked?** We use only that the free
   rows are unconstrained real vectors; in particular we do not require $L$ to have full row
   rank. Is there a standard convention under which this reduction would be invalid?

5. **Sample points versus an open feasible set.** The feasible locus in a chart is not
   closed (it contains the strict conditions $e_\omega(G_H)>0$). Do sample-point algorithms
   as usually stated return a point of such a set when the set is nonempty, or do they
   require closedness or compactness first? This is the point on which our FIND claim turns.

6. **Is the structural bound $\omega+1\le\dim W\le2\omega$ known?** It follows in three
   lines from the two conditions, and it prunes the search, but we would rather cite it than
   claim it if it appears somewhere.
