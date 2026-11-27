# Composing the nonzero gadget: what is verified, what is only compressed, and where the arithmetic gate stands

This note reports the composition experiments around the \((5b)\iff f\ne0\) gadget, separates exact finite checks from proofs, and asks four questions.

## Part I. Setting and labels

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

Labels:
- **P**: paper proof;
- **E**: exact finite computation (symbolic/rational), for the displayed matrices only;
- **S**: sketch or compressed construction, with a named missing step.

A **PASS** in this note means an exact script checked the displayed matrices and the stated rank/gcd identities. It does **not** mean the construction is lifted to a full observer, and it is not a Lean proof.

## Part II. What has been constructed

### II.1 A full observer realization of \((5b)\iff f\ne0\) (P/E)

Take
\[
n=3,\ p=1,\ q=2,\ r_0=1,\ r=1,\ k=1,\ \omega=1,
\]
\[
C=\begin{bmatrix}0&0&1\end{bmatrix},\quad
A=\begin{bmatrix}0&0&0\\1&0&0\\0&1&0\end{bmatrix},\quad
L_0=\begin{bmatrix}1&0&0\end{bmatrix},\quad
R(f)=\begin{bmatrix}0&f&0\end{bmatrix}.
\]
Then \(K_0=\operatorname{span}(e_1)\), \(N=e_1\), and
\[
H=\begin{bmatrix}1\\0\end{bmatrix},\qquad
H_A=\begin{bmatrix}0\\f\end{bmatrix},\qquad
P(\lambda)=\begin{bmatrix}\lambda\\-f\end{bmatrix}.
\]
\((5a)\) holds for every \(f\); \((5b)\iff f\ne0\). This is a **full observer** (all matrices are given), verified exactly (E). It is a nonzero/inequality gadget, not a multiplication gate.

### II.2 Direct sum: conjunction of nonzeros (E, compressed)

Two copies of II.1 give \(q=4,n=6,p=2,k=2,\omega=2\):
\[
H=\operatorname{diag}(H_1,H_2),\qquad
H_A=\operatorname{diag}(H_{A,1},H_{A,2}),
\]
and
\[
(5b)\iff f_1\ne0\ \wedge\ f_2\ne0.
\]
This is exact for the displayed block-diagonal matrices. It is **not** written as a full \(A,C,L_0\) realization in the note, though the block-diagonal construction is the natural candidate.

Setting \(f_1=f_2=f\) gives only \((5b)\iff f\ne0\): sharing a parameter is a copy, not a new constraint.

### II.3 A mixed block forcing \(z=xy\) through \((5a)\) (E, compressed)

Take \(q=3,k=3,\omega=2\):
\[
H=\begin{bmatrix}1&0&0\\0&1&x\\0&0&0\end{bmatrix},\qquad
H_A=\begin{bmatrix}a&0&0\\0&y&z\\\alpha&\beta&w\end{bmatrix}.
\]
Since
\[
\operatorname{row}H=\operatorname{span}\{(1,0,0),(0,1,x)\},
\]
\[
(5a)\iff z=xy\ \text{and}\ w=\beta x.
\]
On the gate \(z=xy,w=\beta x\), the \(2\times2\) minors of \(P(\lambda)=\lambda H-H_A\) have gcd \(1\), and \(\det P\equiv0\); hence \((5b)\) holds automatically. This is exact (E), but \(x,y,z,w\) are **witness variables**, not input constants.

### II.4 Two multiplication relations sharing \(x\) (E, compressed)

Take \(q=4,k=3,\omega=2\):
\[
H=\begin{bmatrix}1&0&0\\0&1&x\\0&0&0\\0&0&0\end{bmatrix},\qquad
H_A=\begin{bmatrix}
a&0&0\\
0&y_1&z_1\\
0&y_2&z_2\\
\alpha&\beta&\beta x
\end{bmatrix}.
\]
Two gate rows in \(\operatorname{span}\{(1,0,0),(0,1,x)\}\) give
\[
z_1=xy_1,\qquad z_2=xy_2,
\]
and the support row keeps \((5b)\) (gcd \(1\), rank \(2\) at sampled and symbolic \(\lambda\)). Again all variables are witness variables.

## Part III. What is not done

1. **Lifting II.3/II.4 to a full observer.** The compressed matrices satisfy \((5a)(5b)\), but the per-row liftability test
\[
(H_i,H_{A,i})\in\operatorname{row}[N\ AN]
\]
has not been carried out for these blocks. A compressed gate may fail this test.
2. **Input-fixed variables.** In II.3/II.4, \(x,y,z\) are chosen by the witness \(R\). For any \(x,y\), one can choose \(z=xy\), so the gate does not constrain the input; this is the free-witness issue.
3. **A genuine arithmetic circuit.** No composition of II.3 blocks into a circuit is known; the global \(F\) consistency (one \(A\) for all blocks) is not addressed.

### III.1 Two failed attempts to fix \(x\) from the input

Take \(C=e_3\), \(CA=e_1+x e_2\), so
\[
N=\operatorname{span}\{(-x,1,0,0),(0,0,0,1)\}.
\]
Then \(H=LN\) has \(x\) in its coefficients.

- With \(H=\begin{bmatrix}-x&0\\0&1\\0&0\end{bmatrix}\), at \(x=0\) the rank drops to \(1\), and \((5b)\) holds with \(\omega=1\); the instance is still feasible at \(x=0\). Not a nonzero gate.
- With \(H=\begin{bmatrix}-x&0\\0&1\\0&1\end{bmatrix}\), the rank is constant \(2\), but two rows are both in the \(e_2\) direction, and at the common eigenvalue both vanish; \((5b)\) fails for every \(x\). Not a gate either.

The needed mechanism is a pencil \(F(x)\) whose eigenline meets \(\operatorname{im}H\) at \(x=0\) and avoids it for \(x\ne0\). No construction is known.

## Part IV. Questions

1. **Are witness-variable multiplication gates enough?** II.3 and II.4 encode \(z=xy\) among witness variables. For an \(\exists\mathbb R\)-hardness reduction, is this sufficient (the witness variables are the ETR variables), or must the multiplication variables be tied to input constants? If witness variables are enough, what is the missing soundness/completeness step?

2. **How to lift II.3/II.4?** Given the compressed matrices, the exact per-row test is
\[
(H_i,H_{A,i})\in\operatorname{row}[N\ AN].
\]
Is there a general recipe to choose \(N,AN\) (equivalently \(A,C\)) so that the gate rows pass this test, or is the test the main obstruction?

3. **Input-controlled nonzero.** Is there a construction of \(F(x)\) (with \(x\) an entry of \(A\)) such that
\[
\operatorname{im}H\cap E_\lambda(F(x))=\{0\}\ \forall\lambda
\iff x\ne0?
\]
The two attempts above fail because either the rank drops with \(x\), or an eigenline is always present.

4. **Composition.** If II.3 blocks are stacked, one \(A\) must serve all blocks. Is the global consistency of \(F\) the main obstruction, or can the blocks be made independent by a block-diagonal \(A\) with shared \(R\)?

## Part V. Bottom line

- There is a **full observer** realization of \((5b)\iff f\ne0\) (II.1).
- There are **compressed** blocks forcing \(z=xy\) and sharing \(x\) (II.3/II.4), verified exactly but not lifted.
- The central open point is whether witness-variable multiplication is enough for a reduction; if not, the input-controlled nonzero mechanism is missing.
