# MIN-ROWS / q1: current results, the rigidity theorem, and a request for direct help

This report summarises the project's results and difficulties and asks for concrete help on the next steps. The most important new result is a rigidity theorem: if \(A(K_0)\subseteq K_0\) and \(c>0\), the observer problem is infeasible. This blocks the natural "invariant-subspace gadget" route to hardness and changes the strategic picture.

## Part I. The problem and the convention

Given \(A\in\mathbb C^{n\times n}\), \(C\in\mathbb C^{p\times n}\), \(L_0\in\mathbb C^{r\times n}\), find \(L=[L_0;R]\) with

\[
(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\quad\forall\lambda .
\]

Put \(K_0=\ker[C;CA]\), \(k=\dim K_0\), \(N=N_K\), \(H=LN\), \(H_A=LAN\), \(\omega=\operatorname{rank}H\), \(c=k-\omega\), and \(P(\lambda)=\lambda H-H_A\). The compression is exact:
\[
(5a)\iff\ker H\subseteq\ker H_A,\qquad (5b)\iff\operatorname{rank}P(\lambda)=\omega\ \forall\lambda.
\]
Two conventions are distinguished: \(\mathsf P_{\mathrm{ind}}\) requires \(\operatorname{rank}[C;L]=p+q\); \(\mathsf P_{\mathrm{full}}\) requires only that \(L\) has full row rank. The literature has settled the characterisation and the minimum-order existence; the open question \(q1\) is the complexity of the existential condition.

## Part II. Results

### II.1 \(\exists\mathbb R\) membership

For the original pencil \(Q(\lambda)=[\lambda L-LA;CA;C]\) and \(s=\operatorname{rank}[L;CA;C]\), one has
\[
(5b)\iff\exists Y:\ QYQ=Q,\quad \deg Y\le2s-2,\quad \operatorname{nrank}Q=s,
\]
the converse following from the local Smith form. This gives \(\mathrm{DEC}(q)\in\exists\mathbb R\) and \(\mathrm{MIN}(k)\in\exists\mathbb R\) by finite disjunction. The normal-rank condition is essential; the \(s=0\) case is separate.

### II.2 Component bounds

For the invariant part (\(t=c\)), every fixed eigenvalue-labelled Jordan type is irreducible or empty: using a cyclic vector \(x\) with \(T^c x=0\), \(T^{c-1}x\ne0\) (and every chain vector in \(K_0\)), the stratum is the image of an irreducible parameter space under a morphism. Hence
\[
N_{\mathrm{inv}}(c)\le\sum_{\lambda\vdash c}s^{b(\lambda)}.
\]
For the non-invariant part, \(S_{t,u}\) maps to the rank strata
\[
B_{u,v}=\{U:\dim(U\cap A^{-1}U)=v\},
\]
which are **not** always irreducible (e.g. \(A=\operatorname{diag}(0,1)\), \(u=v=1\) gives two points), but admit the quadratic chart
\[
F_A(X)=\begin{bmatrix}A_{21}+A_{22}X-XA_{11}-XA_{12}X\\A_{31}+A_{32}X\end{bmatrix},
\]
and a uniform Bezout bound \(b_{u,v}\le\binom{k}{u}(2(u-v+1))^{u(k-u)}\). For \(c=3\) this gives the rigorous (crude) bound \(N_3\le s+s^2+s^3+1921\) at \(k=4\).

### II.3 Low-c geometry

- \(c=0\) is impossible: if \(H\) is square invertible, \(\det P\) is a nonconstant polynomial of degree \(k\), hence has a root where the rank drops.
- \(c=1\), \(W_L\subseteq D=K_0\cap A^{-1}K_0\): \(L_0ANv=0\) and \(RD(Av)=0\), so admissibility forces \(h_i\cdot w=0\); for a non-eigenline this is a proper hyperplane of \(\operatorname{Ann}(L)\) and \(\operatorname{rank}H\le\omega-1\), infeasible. Eigenlines are handled by the functional \(\varphi\); for the tested instances all are killed.
- \(c=1\), \(W_L\not\subseteq D\): admissibility is vacuous (every \(h\) has an admissible lift, via an explicit \(g_0\) adjustment), but the pencil can still be structurally bad.
- \(c=2\), forced plane: each bottom row's admissibility system either forces \(b_i=0\) or not; if all bottom rows are forced, \(\operatorname{rank}H=1<\omega\), infeasible for every \(q\). This is certified by \(\alpha=(-1,0)\) with \(\alpha^{\mathsf T}\mathrm{Des}=e_b\).

### II.4 Two test instances and the convention

For the two test instances, \(k=4\), \(\dim W_L=2\), \(W_L\subseteq D\), and the \(c=2\) rows are forced. Classifying by \(c\):
- \(c\ge3\): no \(V\subseteq W_L\);
- \(c=2\): row-wise forcing;
- \(c=1\): the hyperplane lemma and the explicit eigenlines (two rational / two complex conjugate);
- \(c=0\): the determinant obstruction.
Hence both instances are infeasible for every \(q\) under \(\mathsf P_{\mathrm{ind}}\). The compressed arguments do not use \(\operatorname{rank}[C;L]=p+q\), so the conclusion may also hold for \(\mathsf P_{\mathrm{full}}\); this depends on the original definition and is one of the questions below. Exact certificates (bases, \(W_L\subseteq D\) witnesses, \(\mathrm{Des}/\alpha\), eigenline polynomials, functionals) have been generated.

### II.5 A uniform solver

The four-layer solver (geometry; compressed rows with the quotient rank \(\omega-\rho_0\); lift via \(d'_C\ge\dim\ker Z_{\mathrm{pair}}\); spectral gcd) returns an exact witness, or a row-space infeasibility certificate when \(\dim W_L=c\), or "not found". It reproduces the known feasible/infeasible instances.

### II.6 Rigidity: \(A(K_0)\subseteq K_0\) and \(c>0\) is infeasible

This is the main new result. If \(A(K_0)\subseteq K_0\), every feasible \(V\) is \(A\)-invariant (the rows \(h\) annihilate \(V+AV\), forcing \(\omega\le k-\dim(V+AV)\)). Then \(V^\perp\) is \(A^{\mathsf T}\)-invariant, and \(\operatorname{row}H=V^\perp\) (because \(\operatorname{row}H\subseteq V^\perp\) and both have dimension \(\omega\)). Any nonzero invariant subspace of an operator over \(\mathbb C\) contains an eigenvector: take \(l\in V^\perp\) with \(lA=\lambda l\), choose \(y\) with \(yH=l\); then
\[
yP(\lambda)=l(\lambda I-A)=0,
\]
so \(\operatorname{rank}P(\lambda)<\omega\), contradicting \((5b)\). Therefore no feasible solution with \(c>0\) exists whenever \(A(K_0)\subseteq K_0\).

Consequences:
- the \(2\times2\) multiplication gadget (which lives in the invariant-subspace equation) **cannot** be embedded in this regime; all scans return no witness, in agreement with the theorem;
- any hardness reduction must use \(A(K_0)\not\subseteq K_0\) (as the feasible test instances do);
- the specific \(2\times2\) gadget with \(A_{11}=A_{22}=\operatorname{diag}(0,1)\), \(A_{12}=-[\begin{smallmatrix}0&1\\0&0\end{smallmatrix}]\), \(A_{21}=0\) realises \(z=xy\) at the geometric level (verified symbolically), but is killed by this rigidity.

### II.7 Expressiveness results

Three limits were found: the constraints on \(H\) are row-space type (\(\operatorname{row}H\subseteq\operatorname{Ann}(V)\)); the chart constraints on \(V\) are quadratic (\(XA_{12}X\)); and the only linearisation is a Sylvester equation \(A_{21}+A_{22}X-XA_{11}=0\) when \(A_{12}=0\), with difference-matrix coefficients. A direct identification of a source matrix with \(H\) or with the chart \(X\) therefore does not give a reduction.

### II.8 Lean kernels

The following are machine-checked (axioms: propext, Classical.choice, Quot.sound):
\[
\ker\varphi_U=U\cap A^{-1}U,\quad \dim\operatorname{range}\varphi_U=u-\dim(U\cap A^{-1}U),\quad
\varphi\in\operatorname{range}f^{\mathsf T}\iff\varphi|_{\ker f}=0,
\]
and, for the present report,
\[
(V+AV)^\perp=V^\perp\cap(AV)^\perp,\qquad
\text{a nonzero invariant subspace over an algebraically closed field contains an eigenvector.}
\]

## Part III. Difficulties and questions

**Question 1 (verify the rigidity theorem).** Is the proof of II.6 correct? In particular: (i) is \(\operatorname{row}H=V^\perp\) justified (rows annihilate \(V\), dimensions equal)? (ii) is \(V^\perp\) indeed \(A^{\mathsf T}\)-invariant? (iii) does the eigenvector \(l\in V^\perp\) always give \(yP(\lambda)=0\) for some \(y\)? We would value a line-by-line check, since this theorem blocks a whole route.

**Question 2 (hardness with \(A(K_0)\not\subseteq K_0\)).** Given II.6, the multiplication gadget must be embedded with \(A(K_0)\not\subseteq K_0\). Do you see a concrete construction? For example, can the \(A_{31},A_{32}\) (the \(K_0\to G\) block) be used to break the invariance while keeping the chart equation and the spectral condition? Or is the invariant-subspace gadget route dead in general?

**Question 3 (\(O_2\) emptiness).** For \(c=1\), \(\dim W_L>1\), we reduced \(\mathbb P(W_L)=\mathbb P(U)\cup\) (open complement), with \(\mathbb P(U)\) handled by the hyperplane lemma and the complement by open conditions. Is there a structural criterion for the emptiness of the complement (e.g. a \(B_*\)-based obstruction), or is full elimination the only route?

**Question 4 (the convention).** Does the original observer problem require \(\operatorname{rank}[C;L]=p+q\)? Under \(\mathsf P_{\mathrm{ind}}\) the two instances are infeasible for all \(q\); under \(\mathsf P_{\mathrm{full}}\) the compressed arguments still apply, but the lift-completion step differs. Which convention should the project adopt?

**Question 5 (hardness source).** With affine rank minimisation blocked by the expressiveness limits, is the arithmetic-circuit ETR formulation the right source? What is the smallest gadget to attempt first with \(A(K_0)\not\subseteq K_0\): a multiplication gate, a variable-sharing gadget, or a rank-forcing gadget?

**Question 6 (direct help).** Where can you help most directly:
- (a) checking II.6 and the \(c=1\)/\(c=2\) arguments;
- (b) proposing a gadget with \(A(K_0)\not\subseteq K_0\);
- (c) suggesting a known hardness reduction or a rigidity theorem that subsumes II.6;
- (d) reviewing the component-bound programme (invariant part + \(B_{u,v}\)).

**Question 7 (priority).** Given the rigidity theorem, should the project (i) continue the hardness programme only via \(A(K_0)\not\subseteq K_0\), (ii) pivot to a fixed-\(c\) algorithm and parameterised complexity, or (iii) first consolidate the structural results (rigidity, low-\(c\) classification, \(\exists\mathbb R\)) into a paper? We would appreciate a concrete recommended order.
