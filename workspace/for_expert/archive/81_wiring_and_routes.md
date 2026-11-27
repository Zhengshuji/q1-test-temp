# Wiring at a fixed local subspace: port rigidity, moving ports, and a request for route guidance

This note reports the soundness problem in the gate programme, two local-incidence obstructions, and asks for guidance on both wiring and the overall route.

## Part I. Setting and the soundness distinction

For fixed \(A,C,L_0\), find \(L=[L_0;R]\) with
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

Two different notions:

- **Realization**: a particular compressed pair \((H,H_A)\) is produced by some \(R\).
- **Sound q1 gadget**: for the fixed \(A,C,L_0\), every feasible \(R\) decodes to the intended relation.

The universal lift in dimension \(3k\) makes every prescribed compressed pair realizable, but it does not constrain the free rows. This is the source of the soundness gap.

## Part II. What is sound and what is not

### II.1 Sound: nonzero gadget

\[
n=3,\ p=1,\ q=2,\ r_0=1,\ r=1,\ k=1,\ \omega=1,
\]
\[
C=\begin{bmatrix}0&0&1\end{bmatrix},\quad
A=\begin{bmatrix}0&0&0\\1&0&0\\0&1&0\end{bmatrix},\quad
L_0=\begin{bmatrix}1&0&0\end{bmatrix},\quad
R=\begin{bmatrix}u&v&w\end{bmatrix}.
\]
Then \(N=e_1\),
\[
H=\begin{bmatrix}1\\u\end{bmatrix},\qquad
H_A=\begin{bmatrix}0\\v\end{bmatrix},\qquad
P(\lambda)=\begin{bmatrix}\lambda\\ \lambda u-v\end{bmatrix}.
\]
For every \(R\), \((5a)\) holds and
\[
(5b)\iff v\ne0.
\]
This is sound.

### II.2 Sound: input-controlled nonzero

\[
C=\begin{bmatrix}0&0&1\end{bmatrix},\quad
A(x)=\begin{bmatrix}0&0&0\\x&0&0\\0&1&0\end{bmatrix},\quad
L_0=\begin{bmatrix}1&0&0\end{bmatrix},\quad
R=\begin{bmatrix}u&v&w\end{bmatrix}.
\]
Then \(K_0=\operatorname{span}(e_1)\) independent of \(x\),
\[
H=\begin{bmatrix}1\\u\end{bmatrix},\qquad
H_A=\begin{bmatrix}0\\xv\end{bmatrix},
\]
and for every \(R\),
\[
(5a)\ \text{holds},\qquad
(5b)\iff x\ne0.
\]
This is sound.

### II.3 Not sound: the multiplication gate

With the \(3k\) universal lift, \(k=3\),
\[
H=\begin{bmatrix}e\\e\\v_x\\0\end{bmatrix},\qquad
H_A=\begin{bmatrix}0\\e\\(0,y,z)\\(0,\beta,w)\end{bmatrix},\quad
e=(1,0,0),\ v_x=(0,1,x),
\]
one has, **on the displayed witness**,
\[
(5a)\iff z=xy,\quad w=\beta x,\qquad
(5b)\iff\beta\ne0.
\]
But this is not sound: taking \(R=0\) gives
\[
H=\begin{bmatrix}e\\e\\0\\0\end{bmatrix},\qquad
H_A=\begin{bmatrix}0\\e\\0\\0\end{bmatrix},\qquad
P(\lambda)=\begin{bmatrix}\lambda e\\(\lambda-1)e\\0\\0\end{bmatrix}.
\]
For every \(\lambda\), at least one of \(\lambda,\lambda-1\) is nonzero, so \(\operatorname{rank}P=1=\operatorname{rank}H\). The instance is feasible and imposes no condition on \(x,y,z\).

Thus the gate is a full-observer **realization** of a prescribed compressed witness, not a sound q1 gadget.

## Part III. Two local-incidence obstructions

### III.1 Port rigidity

Let
\[
E_1=\operatorname{span}(e_1,e_2),\qquad
E_2=\operatorname{span}(e_1,e_3),\qquad
E_1\cap E_2=\operatorname{span}(e_1).
\]
Suppose \(W\supseteq E_1\), \(\dim W=3\), and
\[
W\cap E_2=\operatorname{span}(e_1).
\]
Write \(W=\operatorname{span}(e_1,e_2,v)\), \(v=a e_1+b e_2+c e_3\).
If \(c\ne0\), then
\[
e_3=\frac1c(v-a e_1-b e_2)\in W,
\]
so \(e_3\in W\cap E_2\), contradiction.
If \(c=0\), then \(v\in E_1\), so \(W=E_1\), contradicting \(\dim W=3\).

Hence a fixed local subspace \(E_2\) with a fixed port line forces \(W=E_1\). It excludes extra rows, but it also freezes \(W\).

### III.2 Moving the port does not help

Multiplication requires \(W\) to contain
\[
v_x=(0,1,x).
\]
If \(E_1=\operatorname{span}(e_1,e_2)\subseteq W\), then
\[
v_x-e_2=x e_3\in W,
\]
so \(e_3\in W\) for \(x\ne0\). Therefore:

- a fixed \(E_2\subseteq\operatorname{span}(e_1,e_3)\) is contained in \(W\), and \(W\cap E_2=E_2\) is two-dimensional;
- a fixed \(E_2\) with a direction outside \(W\) (e.g. \(e_4\)) has \(W\cap E_2=\operatorname{span}(e_1)\), a fixed line;
- a moving intersection \(\operatorname{span}(e_1+x e_3)\) requires \(E_2\) to depend on \(x\), which fixed data cannot supply.

So in the “fixed \(E_j\) + variable \(W\)” framework, a moving port is not available.

## Part IV. The remaining proof obligations

A sound q1 gate would need:

- **C (completeness)**: every source solution lifts to a feasible \(R\);
- **S (soundness)**: every feasible \(R\), including extra nonzero rows and cross-block components, decodes to a source solution;
- **R (rank stratum)**: the feasible \(\omega=\operatorname{rank}H\) is forced in the intended stratum, or all other strata are excluded.

The present gates satisfy C, not S or R. A direct-sum composition also fails S: block-diagonal \(A,C\) do not force block-diagonal \(R\), so cross-block components can create unintended solutions.

## Part V. Questions

### Wiring

1. **Is the fixed-subspace obstruction fundamental?** Is it true that with fixed coordinate subspaces \(E_j\) and a variable \(W\) containing \(v_x=(0,1,x)\), no intersection \(W\cap E_j\) can be a moving line? If so, what is the correct no-go statement?

2. **Can \(E_j\) be witness-defined?** If the local subspaces are themselves defined by free witness rows, how can they be prevented from being enlarged by extra free rows? Is there a mechanism that controls all free rows at once?

3. **Alternative encodings.** Is there a wiring encoding that avoids local-subspace intersections altogether—for example a projective line bundle, a global linear-algebra identity, or an incidence structure on the whole row space?

4. **Sound multiplication.** Is a sound q1 multiplication gadget (for unrestricted \(R\)) possible at all? If not, is there a no-go theorem, and what is its exact statement?

### Other routes

5. **Algorithmic route.** The fixed-\(\kappa_{\rm obs}\) Gram certificate remains the most mature positive result:
\[
G_H=H^{\mathsf T}H,\quad G_S=H^{\mathsf T}H+H_A^{\mathsf T}H_A,
\]
\[
(5a)\iff e_\omega(G_H)>0,\ e_{\omega+1}(G_S)=0,
\]
\[
(5b)\iff\exists x\in\mathbb R^{2\omega}:\ B^{\mathsf T}Bx=e_0,
\]
with \(B^{\mathsf T}B\) obtained from
\[
K(\lambda,\mu)=\sum_{|J|=\omega}\det(P(\lambda)_{:,J}^{\mathsf T}P(\mu)_{:,J}).
\]
Is this a publishable FPT theorem once the coefficient indexing, \(\omega=0\), and bit-complexity are written out? Should it be the main line while the hardness programme is blocked?

6. **Fixed \(q\) route.** The \(Z,U\) reformulation
\[
H_A=ZH,\qquad U=\operatorname{im}H,\qquad
(5b)\iff U\cap E_\lambda(Z)=\{0\}
\]
reduces to a parametric linear-elimination problem. Is there a known lemma that would make fixed \(q\) polynomial, or is the parametric rank attainment genuinely hard?

7. **Route guidance.** Given the soundness obstruction, should the project:
   - (a) continue the gate/wiring programme;
   - (b) switch to the algorithmic FPT paper;
   - (c) treat \(q1\) as intermediate/parameterized (fixed parameter tractable, unrestricted open);
   - (d) look for a different hardness source (not gates)?

## Part VI. Bottom line

- Two sound gadgets exist: nonzero and input-controlled nonzero.
- The multiplication gate is a realization, not a sound q1 gadget; \(R=0\) is an explicit counterexample.
- Fixed local subspaces freeze the row space; moving ports are not available in the fixed-subspace framework.
- The remaining target is a global incidence/wiring mechanism that controls every feasible \(R\), or a no-go theorem showing that sound multiplication is impossible.
- Guidance is requested on whether to continue this programme or to prioritize the fixed-\(\kappa_{\rm obs}\) algorithmic result.
