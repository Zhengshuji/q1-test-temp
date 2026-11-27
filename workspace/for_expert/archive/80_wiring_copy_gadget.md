# Wiring the multiplication gate: a row-copy obstruction and a request for a copy/format gadget

This note reports the current state of the gate library, the column-overlap wiring primitive, and the obstruction that appears when two multiplication gates are connected in series.

## Part I. Setting

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

Labels: **P** paper, **E** exact finite computation for the displayed matrices, **S** sketch.

## Part II. The gate library

### II.1 Universal lift (P/E)

For any \(k\ge1\), split \(\mathbb R^{3k}=U\oplus V\oplus W\) and take
\[
C=\begin{bmatrix}I_k&0&0\end{bmatrix},\qquad
A=\begin{bmatrix}0&0&I_k\\0&0&0\\0&I_k&0\end{bmatrix}.
\]
Then
\[
CA=\begin{bmatrix}0&0&I_k\end{bmatrix},\quad
K_0=V,\quad N=\begin{bmatrix}0\\I_k\\0\end{bmatrix},\quad
AN=\begin{bmatrix}0\\0\\I_k\end{bmatrix},
\]
\[
[N\ AN]=\begin{bmatrix}0&0\\I_k&0\\0&I_k\end{bmatrix},\qquad
\operatorname{rank}[N\ AN]=2k.
\]
The map \(r\mapsto(rN,rAN)\) is onto the \(2k\)-dimensional compressed row-pair space. For arbitrary \(H_0,H_{A,0},Y,Z\),
\[
L_0=[0\ H_0\ H_{A,0}],\qquad R=[0\ Y\ Z]
\]
realizes \(LN=[H_0;Y]\), \(LAN=[H_{A,0};Z]\). This is exact (E).

### II.2 Full multiplication gate (P/E)

With the same \(A,C\), \(k=3\), \(n=9\), \(p=3\), set
\[
e=(1,0,0),\qquad v_x=(0,1,x),
\]
\[
H=\begin{bmatrix}e\\e\\v_x\\0\end{bmatrix},\qquad
H_A=\begin{bmatrix}0\\e\\(0,y,z)\\(0,\beta,w)\end{bmatrix}.
\]
Then \(\operatorname{row}H=\operatorname{span}\{e,v_x\}\),
\[
(5a)\iff z=xy,\quad w=\beta x,
\]
and on this locus
\[
P(\lambda)=\begin{bmatrix}\lambda e\\(\lambda-1)e\\(\lambda-y)v_x\\-\beta v_x\end{bmatrix},
\]
so
\[
(5b)\iff\beta\ne0.
\]
Hence
\[
\exists\beta,w:\ (5a)\wedge(5b)\iff z=xy.
\]
This is a full observer, exact (E).

### II.3 Input-controlled nonzero (P/E)

\[
C=\begin{bmatrix}0&0&1\end{bmatrix},\quad
A(x)=\begin{bmatrix}0&0&0\\x&0&0\\0&1&0\end{bmatrix},\quad
L_0=\begin{bmatrix}1&0&0\end{bmatrix},\quad
R=\begin{bmatrix}u&v&w\end{bmatrix}.
\]
Then \(K_0=\operatorname{span}(e_1)\), \(N=e_1\) (independent of \(x\)),
\[
H=\begin{bmatrix}1\\u\end{bmatrix},\qquad
H_A=\begin{bmatrix}0\\xv\end{bmatrix},
\]
and
\[
\exists R:\ (5a)\wedge(5b)\iff x\ne0.
\]
Exact (E).

## Part III. Wiring

### III.1 Column overlap (P/E)

If
\[
A N_j=N_l,
\]
then for every \(L\),
\[
H_{A,j}=L A N_j=L N_l=H_l.
\]
This is an exact copy primitive, but it is **row-wise**: it copies a coordinate in the same row \(r\),
\[
(H_A)_{r,j}=H_{r,l},
\]
not from one row to another. It also costs rank:
\[
\operatorname{rank}[N\ AN]\le 2k-1
\]
per wire.

### III.2 The series obstruction (S)

To compute
\[
z_1=x_1y_1,\qquad z_2=z_1y_2,
\]
gate 1 has
\[
H_1=(0,1,x_1),\qquad (H_A)_1=(0,y_1,z_1),
\]
and gate 2 needs
\[
H_2=(0,1,x_2),\qquad x_2=z_1.
\]
The direct row identification
\[
H_2=(H_A)_1=(0,y_1,z_1)
\]
forces \(y_1=1\), so gate 1 degenerates to \(z_1=x_1\). Copying only the coordinate \(z_1\) would require a relation between different rows, which column overlap does not give.

### III.3 The missing object

A **copy/format gadget** that realizes
\[
(0,y,z)\longmapsto(0,1,z)
\]
while preserving \(z\), with \((5a)(5b)\) and without destroying the multiplication relation. No construction is known.

## Part IV. Questions

1. **Copy/format gadget.** Does there exist a full-observer gadget that maps \((0,y,z)\) to \((0,1,z)\), preserving \(z\), and satisfies \((5a)(5b)\)? If yes, what is the smallest \(k\) and the matrices?

2. **Row-wise limitation.** Is the row-wise nature of column overlap the fundamental obstruction to wiring, or is there another mechanism (e.g., using a row of \(H\) that is zero in \(H\) but nonzero in \(H_A\)) that can transfer a single coordinate across rows?

3. **Two-gate series.** Can the two-gate series \(z_1=x_1y_1\), \(z_2=z_1y_2\) be realized by a full observer with the universal lift? If not, what is the no-go statement?

4. **Composition primitive.** If row copy is too strong and single-coordinate copy is unavailable, is a different composition primitive (e.g., sharing the entire row, or encoding variables in different coordinates) the right approach?

5. **Soundness.** Even with a wiring gadget, block-diagonal \(A,C\) do not force block-diagonal \(R\); cross-block components can create unintended solutions. What is the recommended way to enforce a genuine circuit semantics: restrict \(R\), add equality gadgets, or use a global linear-algebra encoding?

## Part V. Bottom line

- The gate library is complete: nonzero, multiplication, input-controlled nonzero, and universal lift, all full observers and exactly verified.
- Column overlap is an exact but row-wise copy primitive.
- The first genuine difficulty is a copy/format gadget for wiring a gate output into another gate input.
- No reduction to \(\exists\mathbb R\)-hardness is claimed; the missing step is wiring and soundness.
