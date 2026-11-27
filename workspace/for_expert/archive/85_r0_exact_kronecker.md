# The \(r=0\) branch: exact polynomial-time test for a degree-one pencil

## Part I. The problem

The observer decision problem uses the compressed pair
\[
H=LN,\qquad H_A=LAN,
\]
where \(N\) is a basis of \(\ker[C;CA]\). When the number of free rows is
\(r=0\), the instance is fixed by \(L_0\), and the only remaining condition is
the spectral one. Write
\[
Q(\lambda)=\lambda X-G,\qquad X,G\in\mathbb Q^{q\times\omega},
\]
where \(q\) is the number of observer rows and \(\omega\) is the rank of the
compressed matrix. The condition is
\[
\operatorname{rank}Q(\lambda)=\omega\quad\forall\lambda\in\mathbb C.
\]
Equivalently, the maximal \(\omega\times\omega\) minors of \(Q\) have gcd one,
or \(Q\) admits a polynomial left inverse
\[
S(\lambda)Q(\lambda)=I_\omega.
\]

## Part II. What is already established

1. The adjugate construction is correct and gives the degree bound
   \[
   \deg S\le 2\omega-2.
   \]
   It uses all \(\omega\)-element row subsets \(I\):
   \[
   S_IQ=f_I I_\omega,\qquad f_I=\det Q_I,\qquad
   S=\sum_I g_I S_I.
   \]
2. The number of such subsets is \(\binom q\omega\), which is exponential in
   \(q\). Therefore the adjugate construction proves the degree bound but does
   not give a polynomial-time algorithm when \(q,\omega\) are unrestricted.
3. The condition is equivalent to the Kronecker canonical form of the pencil
   \(\lambda X-G\) having neither a right singular block nor a regular block.
   Staircase/Kronecker algorithms are standard in numerical linear algebra.
4. For a fixed candidate \(L\), deciding whether the pencil has constant rank
   is known to be polynomially solvable in the dimensions; the open point is
   the exact rational bit complexity when \(q,\omega\) are part of the input.

## Part III. Questions

### III.1 Exact algorithm

1. Is there a published deterministic algorithm that decides
   \[
   \operatorname{rank}(\lambda X-G)=\omega\quad\forall\lambda\in\mathbb C
   \]
   in time polynomial in \(q,\omega\) and the input bit length, using exact
   rational arithmetic?
2. If yes, what is the reference and the stated bit complexity? In particular,
   does it avoid enumerating the maximal minors?
3. If the standard Kronecker/staircase algorithm uses orthogonal
   transformations, can its rank decisions be replaced by exact Gaussian
   elimination without changing the polynomial bit bound?

### III.2 Acceptable weaker statements

4. If no fully exact polynomial-time reference is available, is it acceptable
   to state Theorem 3 for \(r\ge1\) and record \(r=0\) as an explicit open
   branch?
5. Alternatively, is a randomized polynomial-time test (Las Vegas, with
   certification) acceptable for the \(r=0\) branch, and how should it be
   stated?
6. Is it enough to cite a numerical Kronecker algorithm if all rank decisions
   are made exactly, or does the paper need a separate exact-arithmetic
   algorithm and bit bound?

### III.3 Structural alternatives

7. Is there a direct rank test for \(\lambda X-G\) using only ranks of constant
   matrices derived from \(X,G\), avoiding a full Kronecker form?
8. Can the \(r=0\) case be absorbed into the \(r\ge1\) FPT theorem by changing
   the parameter or by a reduction that adds one free row without changing
   feasibility?
9. Does the degree-one structure of the pencil admit a simpler polynomial
   algorithm than the general matrix-pencil case?

### III.4 Consequence for the paper

10. If \(r=0\) remains open, is the paper still publishable with the explicit
    restriction \(r\ge1\), or does the main FPT claim lose too much strength?
11. Would it be better to present the \(r=0\) branch as an open problem and
    submit the algorithmic paper, or to wait until the exact Kronecker
    complexity is settled?

## Summary

The mathematical criterion for \(r=0\) is clear, and the degree bound
\(2\omega-2\) is proved. The missing piece is an exact polynomial-time
decision procedure for the full-column-rank condition of a degree-one pencil,
with a controlled bit bound.
