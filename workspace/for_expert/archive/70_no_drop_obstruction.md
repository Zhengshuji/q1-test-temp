# The no-drop obstruction: can the observer conditions force a rank-one gate?

This note asks for adjudication of a structural difficulty that has blocked the one-gate construction.

## Part I. The two observer conditions are no-drop conditions

With the usual notation, \((5a)\) and \((5b)\) are
\[
(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],
\]
\[
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\quad\forall\lambda.
\]
Both ask that a certain rank equal a **natural/maximal** value: adding rows (\(LA\)) must not increase the rank, and the pencil must not drop rank.

## Part II. A multiplication gate is a rank-drop condition

The anchored gate is
\[
\operatorname{rank}\begin{bmatrix}1&x\\y&z\end{bmatrix}=1\iff z=xy.
\]
This is a **drop** from the generic rank \(2\) to \(1\).

For a block \(G\) inside the relevant matrix:
- if \(G\) has full rank, its row space is the whole two-dimensional space, so any additional row is automatically dependent; the no-drop condition holds automatically;
- if \(G\) has rank one, the row space is smaller, and an additional row may be independent; only then can the no-drop condition fail.

Thus a no-drop condition is automatic at full rank and can only fail at rank one. It can **exclude** \(z=xy\), but it cannot **force** \(z=xy\). The directions are opposite.

## Part III. The structural-low-rank caveat

If the fixed data \((A,C)\) force a matrix to have rank \(r\) below the generic value, the no-drop condition becomes "the rows of \(LA\) lie in a fixed \(r\)-dimensional space", which is **linear** in \(L\). It does not produce a quadratic relation such as \(z-xy\).

To obtain a quadratic equation, the rank of the matrix must vary with \(L\); but the no-drop conditions compare two varying ranks and do not pin a low rank.

## Part IV. Questions

**Question 1.** Is the following statement a theorem?

> If a feasible set is defined by no-drop rank equalities (rank of an extended matrix equals the rank of the base matrix, and the pencil does not drop), then its projection onto any block of witness entries cannot be the hypersurface \(\det G=0\) for a \(2\times2\) block \(G\), unless the condition is linear.

If true, the observer conditions cannot encode the anchored multiplication gate, and the hardness programme needs a different mechanism.

**Question 2.** If the statement is false, can you give a concrete instance in which \((5a)\) or \((5b)\) forces \(\det\begin{bmatrix}1&x\\y&z\end{bmatrix}=0\) with \(x,y\) free and no extra equations? We have not found one in small searches (\(q=2\), \(n=5\), 1300 matrices; the Schur/proportionality attempts produced extra equations such as \(y^2=yz=0\)).

**Question 3.** Does the \(10\)-dimensional family change the picture? It gives a variable kernel and a fixed unit minor, but the arithmetic parameter \(t\) is free (every \(t\) is feasible), so it does not test the gate direction.

**Question 4.** If the no-drop obstruction is real, what hardness mechanism remains for \(q1\)? For instance, could the equations be encoded in a **fixed low-rank** structure of the input rather than in the witness ranks, or is \(q1\) more likely to be tractable (a generic-rank/linear-matroid type problem)?

## Part V. What we tried

- A \(q=2\), \(n=5\) search for a \((5a)\) ideal equal to \(\langle z-xy\rangle\): no example among 1300 random matrices; the found seeds had extra minors.
- A Schur/proportionality construction: the gate appears, but the \(R\)-components of the witness row produce extra equations \(y^2=yz=0\).
- A block design with \((\omega-1)\) guard rows and two gate rows: the gate rank would have to raise the pencil rank above \(\omega\), but \((5b)\) only permits rank \(\omega\).

We would value a direct adjudication: a proof that the no-drop conditions cannot force the gate, or an explicit construction that does.
