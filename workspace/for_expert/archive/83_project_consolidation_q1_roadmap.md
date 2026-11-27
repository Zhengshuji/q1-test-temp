# Project consolidation and q1 roadmap: two parameterized algorithms, an open unrestricted problem

This note consolidates the current state after the algorithmic audits, records what is verified, and asks for a concrete roadmap toward q1.

## Part I. The problem and what is already settled

For fixed rational \(A,C,L_0\), find \(L=[L_0;R]\) with
\[
(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\ \forall\lambda.
\]
Let \(K_0=\ker[C;CA]\), \(N\) a basis, \(k=\dim K_0\), \(H=LN\), \(H_A=LAN\), \(\omega=\operatorname{rank}H\). Then
\[
(5a)\iff\operatorname{row}H_A\subseteq\operatorname{row}H,
\qquad
(5b)\iff\operatorname{rank}(\lambda H-H_A)=\omega\ \forall\lambda.
\]

The characterization problem—existence, order spectrum, per-order necessary and sufficient conditions, minimal order, construction—is settled by Fernando's 2026 work. The remaining problem is the decision complexity of \(\exists\Theta\), i.e. q1.

**Status of q1:** open. There is no unrestricted polynomial algorithm and no hardness reduction.

## Part II. What is now proved or strongly supported

### II.1 Fixed \(q\): polynomial time (XP)

Using \(H=XB\), \(B_{:,J}=I_\omega\), and \(G=FX\), one has
\[
H_A=GB,\qquad P(\lambda)=(\lambda X-G)B.
\]
The fixed-row and free-row constraints become a linear system in the remaining entries of \(B\):
\[
M(X,G)b=c(X,G),
\]
and consistency is expressed by
\[
\operatorname{rank}(MM^{\mathsf T})=\operatorname{rank}(MM^{\mathsf T}+cc^{\mathsf T}).
\]
The spectral condition reduces to
\[
\operatorname{rank}((\lambda X-G)B)=\omega\ \forall\lambda,
\]
which depends only on \(X,G\) and is encoded by a \(2\omega\)-variable Gram–Bezout certificate.

The quantified variables are \(O(q^2)\). Hence, for every fixed \(q\),
\[
\boxed{q1\in\mathrm P,\qquad T_A\le \mathcal L^{O(q^2)}}.
\]
This is XP-style: the exponent depends on \(q\).

### II.2 Fixed \(\kappa_{\rm obs}\): FPT

Let
\[
d_0=\operatorname{rank}[N\ AN],\qquad \kappa_{\rm obs}=r d_0.
\]
Every free row pair lies in \(\mathcal T=\operatorname{row}[N\ AN]\), so the free data have exactly \(\kappa_{\rm obs}\) coordinates.

Encode \((5a)\) by
\[
G_H=H^{\mathsf T}H,\quad G_S=H^{\mathsf T}H+H_A^{\mathsf T}H_A,
\qquad
(5a)\iff e_\omega(G_H)>0,\ e_{\omega+1}(G_S)=0.
\]
Encode \((5b)\) by the \(2\omega\)-variable certificate
\[
\exists x\in\mathbb R^{2\omega}:\ B^{\mathsf T}Bx=e_0,
\]
with the shifted-index matrix
\[
B_{(i,j),t}=c_{i,t-j},
\]
and compute \(B^{\mathsf T}B\) from
\[
K(\lambda,\mu)=\sum_{|J|=\omega}\det(P(\lambda)_{:,J}^{\mathsf T}P(\mu)_{:,J})
\]
via
\[
(B^{\mathsf T}B)_{t,t'}=\sum_{j=0}^{\omega-1}S_{t-j,t'-j}.
\]
Only \(\binom{k}{\omega}\le2^{\kappa_{\rm obs}}\) determinants occur, so \(q\) enters only polynomially. Therefore
\[
\boxed{\text{fixed }\kappa_{\rm obs}\Rightarrow q1\in\mathrm{FPT},\qquad
T_B\le f(\kappa_{\rm obs})\operatorname{poly}(\mathcal L).}
\]
The \(r=0\) branch is decided separately by a polynomial left-inverse test for \(Q(\lambda)=\lambda X-G\); the cases \(k=0,\omega=0\) are direct.

### II.3 Verification status

Exact checks (finite instances, not general proofs):

- nonzero gadget: full observer, \((5b)\iff f\ne0\);
- Gram certificate on the 244 pencil: \(B^{\mathsf T}Bx=e_0\), Cauchy–Binet, \(e_2(G_H)=55\), \(e_3(G_S)=0\);
- rank-consistency identity on 200 random systems;
- fixed-\(q\) factorization \(H=XB\), \(B_J=I\), \(H_A=FH\);
- shifted-index formula;
- \(G=FX\) form.

The two algorithmic results are paper skeletons (M2) with expert audit (M3 for the route), not yet complete formal proofs: explicit bit-complexity constants and a fully written proof remain.

## Part III. The hardness barrier

Only two sound q1 gadgets are known:

- the nonzero gadget \((5b)\iff f\ne0\);
- the input-controlled nonzero gadget \(\exists R:(5a)\wedge(5b)\iff x\ne0\).

The multiplication construction is a full-observer realization but not sound: \(R=0\) gives a feasible instance with no condition on the intended variables. Local port rigidity is only conditional; disjoint fixed subspaces can have moving intersections.

The missing object is a sound multiplication gadget under unrestricted \(R\), or a no-go theorem. No hardness reduction exists.

## Part IV. What would count as resolving q1

Possible outcomes:

1. **q1 in P** for unrestricted \(q\): a uniform polynomial algorithm, not merely fixed-\(q\).
2. **q1 is \(\exists\mathbb R\)-complete** (or NP-hard): a reduction from a suitable source, with a sound gadget library and both directions.
3. **Intermediate/parameterized**: a proof that some natural parameter (e.g. \(q\), \(\kappa_{\rm obs}\), or \(c\)) gives a complete classification, with hardness for the unrestricted case.
4. **A no-go theorem**: sound multiplication is impossible in this observer model, so q1 cannot be hard via gates.

At present, the fixed-\(q\) and fixed-\(\kappa_{\rm obs}\) results suggest option 3 is the most likely, but they do not prove it.

## Part V. Questions

1. **Likely complexity of q1.** Given that q1 is in \(\exists\mathbb R\), fixed-\(q\) is in P, and fixed-\(\kappa_{\rm obs}\) is FPT, what is the most plausible outcome: P, \(\exists\mathbb R\)-complete, or an intermediate/parameterized classification? What evidence would distinguish them?

2. **Best route to hardness.** If q1 is hard, what source best respects the global condition \(\operatorname{row}H_A=\operatorname{row}H\) and the per-row space \(\mathcal T\): matroid realization, structured matrix completion, polynomial-matrix unimodularity, or a global subspace-realization problem? Is a sound multiplication gadget necessary, or can hardness be proved directly on the global row-space system?

3. **Sound multiplication.** Is there a no-go theorem for sound multiplication under unrestricted \(R\)? If yes, what is its exact class of architectures? If no, what is the most promising construction principle?

4. **Parameterized hardness.** Is q1 W[1]-hard (or similar) for parameter \(q\) or \(\kappa_{\rm obs}\)? If fixed-\(q\) is in P but the exponent depends on \(q\), the natural question is whether the parameter dependence can be improved or is inherent.

5. **Algorithmic paper.** Are the fixed-\(q\) polynomial and fixed-\(\kappa_{\rm obs}\) FPT results sufficiently novel and complete to stand as an algorithmic paper? What is the correct positioning relative to Fernando 2026 and the parametric-linear-system literature?

6. **Next concrete step.** Should the project
   - (a) finish the algorithmic paper (bit complexity, full proofs);
   - (b) attempt a global hardness reduction;
   - (c) prove parameterized hardness for \(q\) or \(\kappa_{\rm obs}\);
   - (d) look for a no-go theorem for sound multiplication?

## Part VI. Bottom line

- q1 remains open in the unrestricted setting.
- Two parameterized algorithms are strongly supported: fixed \(q\) in P (XP), fixed \(\kappa_{\rm obs}\) in FPT.
- The hardness programme has no sound multiplication gadget and no reduction.
- A concrete roadmap is requested: which of the four outcomes to target, and which next step is most likely to resolve q1.
