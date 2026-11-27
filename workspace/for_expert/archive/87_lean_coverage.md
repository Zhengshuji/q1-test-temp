# Formalization coverage of the paper, and where we are stuck

## Part I. What is claimed, what is formalized

The paper proves two parameterized upper bounds for the following decision problem.

**Data.** Rational matrices $A\in\mathbb Q^{n\times n}$, $C\in\mathbb Q^{p\times n}$,
$L_0\in\mathbb Q^{r_0\times n}$, and an integer $q\ge r_0$. The design variable is the
block of free rows $R\in\mathbb R^{r\times n}$, $r=q-r_0$, and $L=[L_0;R]$.

**Conditions.**

$$(1)\quad \operatorname{rank}\begin{bmatrix}LA\\ L\\ CA\\ C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}L\\ CA\\ C\end{bmatrix},
\qquad
(2)\quad \operatorname{rank}\begin{bmatrix}\lambda L-LA\\ CA\\ C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}L\\ CA\\ C\end{bmatrix}\ \ \forall\lambda\in\mathbb C .$$

$\mathrm{DEC}$ asks whether some $R$ satisfies (1) and (2).

**Compression.** $K_0=\ker[C;CA]$, $N$ a basis of $K_0$, $H=LN$, $H_A=LAN$,
$\omega=\operatorname{rank}H$. The key identity, for any matrix $J$ and any basis $N_J$ of
$\ker J$, is

$$\operatorname{rank}\begin{bmatrix}J\\ M\end{bmatrix}
=\operatorname{rank}J+\operatorname{rank}(MN_J). \tag{$\ast$}$$

**Results.** For fixed $q$, $\mathrm{DEC}$ is decidable in $\mathcal L^{O(q^2)}$ bit
operations, where $\mathcal L$ is the input bit length. With
$\kappa_{\rm obs}=r\operatorname{rank}[N\ AN]$, it is decidable in
$f(\kappa_{\rm obs})\operatorname{poly}(\mathcal L)$ bit operations. The case $r=0$ is
decided exactly in polynomial time by a rational linear system. Finally
$\mathrm{DEC}(q)\in\exists\mathbb R$.

**What is formalized in Lean 4 (Mathlib), axiom-clean.** The *abstract linear-map core* of
four statements, over an arbitrary field:

1. $K_0$-compression: the inclusion of row spaces of $H$ and $H_A$ is equivalent to the
   corresponding kernel condition. (`ker_compressed_iff`)
2. The space of attainable row pairs: the map $x\mapsto(xN,xAN)$ has image of dimension
   $d_0$ and kernel $K_0$, so $k\le d_0\le\kappa_{\rm obs}$. (`freePairSpace`,
   `finrank_freePairSpace_add_ker`, `kappaObs_eq_mul_freePairSpace`)
3. Rank consistency: $Mb=c$ is consistent iff $c\in\operatorname{im}M$ iff
   $\operatorname{span}\{c\}\subseteq\operatorname{im}M$ iff
   $\operatorname{im}M=\operatorname{im}[M\ c]$. (`RankConsistency`)
4. Bézout for two polynomials: $\gcd(f,g)=1$ gives $u,v$ with $uf+vg=1$.
   (`bezout_of_gcd_eq_one`)

**What is paper-level only.** Everything matrix-level, everything with degrees and bit
sizes, and the encoding: the identity $(\ast)$ itself, the pencil/gcd bridge, the
matrix form of the attainable-pair space, the Gram/rank identity for positive semidefinite
matrices, the Bézout degree bound for $s$ polynomials, the rectangular adjugate
construction, the linear system for the $r=0$ case and its complexity, the coefficient-size
lemma, and the $\exists\mathbb R$ encoding.

## Part II. The five gaps, stated so they can be judged

**(G1) Rectangular Cauchy–Binet.** For $\omega\times k$ and $k\times\omega$ matrices,

$$\det(AB)=\sum_{|J|=\omega}\det(A_{:,J})\det(B_{J,:}).$$

This is the step that replaces the enumeration of the $\binom{k}{\omega}$ maximal minors by
one bivariate polynomial. I searched the Mathlib checkout we have (a release matching Lean
4.35) for the substring `binet`, case-insensitive, and found no file. Is there a
formalization under another name (an exterior-power or alternating-map route), and if not,
what is the shortest path — exterior algebra, or induction on $\omega$?

**(G2) Bézout with degree bounds for $s$ polynomials.** If $f_1,\dots,f_s\in K[\lambda]$
have degree $\le\omega$ and no common root over an algebraically closed $K$, there are
$g_i$ with $\deg g_i<\omega$ and $\sum_i g_if_i=1$. The two-polynomial case is formalized;
the degree bookkeeping for $s$ polynomials is not. Is the intended route induction on $s$
via $\gcd(f_1,f_2)$, and does that keep $\deg g_i<\omega$ without an extra argument?

**(G3) The linear system for $r=0$.** With $Q(\lambda)=\lambda X-G$ of size $q\times\omega$
and $\omega\ge1$: $Q$ has full column rank at every finite $\lambda\in\mathbb C$ iff there
is $S(\lambda)\in K[\lambda]^{\omega\times q}$ with $S(\lambda)Q(\lambda)=I_\omega$ and
$\deg S\le2\omega-2$; equivalently iff the rational linear system in
$S_0,\dots,S_{2\omega-2}$

$$-S_0G=I_\omega,\qquad S_{j-1}X-S_jG=0\ (1\le j\le2\omega-2),\qquad S_{2\omega-2}X=0
\tag{$\ast\ast$}$$

is solvable. The construction is the rectangular adjugate: for each $\omega$-element row
set $I$, $Q_I=E_IQ$, $f_I=\det Q_I$, $\operatorname{adj}(Q_I)E_IQ=f_II_\omega$, and
Bézout coefficients with $\sum_Ig_If_I=1$ give $S=\sum_Ig_I\operatorname{adj}(Q_I)E_I$.
Two questions: is there a Mathlib formalization of the rectangular adjugate identity that
we could reuse, and is the equivalence between "no common root of the maximal minors" and
"solvability of $(\ast\ast)$" better attacked through resultants or through the
Bezout/Sylvester matrix?

**(G4) Coefficient sizes.** Every quantity above has bit length $\operatorname{poly}(n,
\mathcal L)$: the kernel basis, the row-space basis of $[N\ AN]$, the matrices $H,H_A$, the
maximal minors and their coefficients, and the Gram matrix. The paper's argument is
Cramer's rule plus Hadamard's inequality, with the number of terms counted explicitly. Is
there any existing formal treatment of bit sizes of rational Gaussian elimination in
Mathlib (or in a Lean project you would point us to), or is a bespoke development needed?

**(G5) The $\exists\mathbb R$ encoding.** The formula is a finite disjunction over
$\omega$ and over column sets $J$, with variables $X,G,x$ and the constraints (1) expressed
through the rank-consistency formula, plus $Z^{\mathsf T}Zx=e_0$ for the spectral part.
Membership in $\exists\mathbb R$ follows from the standard quantifier-elimination decision
procedure. We do not intend to formalize real quantifier elimination. The question is
whether a partial formalization is worth anything: e.g. proving in Lean that the formula
*is* equivalent to (1) and (2) for a fixed $\omega$ and $J$, and leaving only the
"$\exists\mathbb R$ is decidable" step as external.

## Part III. What we would like to know

1. **Priority.** Given the five gaps, which two would you formalize first if the goal is
   that the paper's main theorems are kernel-checked up to a small, clearly listed residue?
2. **G1.** Is rectangular Cauchy–Binet available in Mathlib under a name we did not find,
   and if not, is the exterior-algebra route the standard one?
3. **G2.** Is the induction on $s$ the accepted route, and does it keep the degree bound
   $\deg g_i<\omega$?
4. **G3.** Rectangular adjugate: is there prior art in Lean, and which of the two
   equivalences (maximal-minor gcd versus linear-system solvability) is the cheaper one to
   formalize?
5. **G4.** Is a formal treatment of bit sizes worth attempting at all, or is it the kind of
   statement that is better left as a paper-level estimate with an explicit audit?
6. **G5.** Does a partial encoding formalization carry any weight in your view, or is it
   better to state the membership result and cite the classical decision procedure?

We would also welcome a correction if any of the statements in Part II is not the statement
we think it is.
