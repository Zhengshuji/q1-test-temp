# The conditional multiplication gate, the corrected feasible locus, and a request for an anchored block

This note reports the corrected status of the explicit \((5a)\) gate, the failed attempts to anchor it, and asks for a concrete fixed-pivot construction.

## Part I. Setting

With \(K_0=\ker[C;CA]\), \(N=N_K\), \(H=LN\), \(H_A=LAN\), \(\omega=\operatorname{rank}H\), \(c=k-\omega\), \(P(\lambda)=\lambda H-H_A\), and \((5a)(5b)\) as usual.

## Part II. The conditional gate

### II.1 Exact determinant identity

For
\[
A=\begin{bmatrix}
1&1&-1&0&1\\
-1&0&0&-1&1\\
0&1&-1&0&1\\
0&0&0&-1&0\\
-1&1&0&0&0
\end{bmatrix},\quad
C=e_5^*,\quad L_0=e_1^*,\quad L=\begin{bmatrix}e_1^*\\l\end{bmatrix},\quad l=(a,b,c,d,e),
\]
one has, with \(M=[lA;L_0;l;CA;C]\) and \(M_0=[L_0;l;CA;C]\),
\[
\det M=ad-bc.
\]

### II.2 Exact \((5a)\) locus

\(\operatorname{rank}M_0=4\) iff \((c,d)\ne(0,0)\); otherwise it is \(3\). Hence
\[
(5a)\iff
\begin{cases}
ad=bc,&(c,d)\ne(0,0),\\
a=b=0,&(c,d)=(0,0).
\end{cases}
\]
On the chart \(l=(1,x,y,z,0)\), \((5a)\iff z=xy\) **and** \(y\ne0\).

### II.3 \((5b)\) is not automatic

The maximal minors of \(P\) are
\[
\Delta_{12}=c\lambda^2-(b+c)\lambda-(b+c),\quad
\Delta_{13}=(\lambda-2)(b+d(\lambda+1)),\quad
\Delta_{23}=b+d(\lambda+1).
\]
The exact rank-two condition is
\[
(5b)\iff
\begin{cases}
b\ne0,&d=0,\\
b^2c+b^2d+3bcd+cd^2\ne0,&d\ne0.
\end{cases}
\]
Two counterexamples on the intended chart:
- \((a,b,c,d,e)=(1,0,1,0,0)\): \((5a)\) holds, \(\Delta_{12}=\lambda^2-\lambda-1\), so \((5b)\) fails;
- \((1,-5,1,-5,0)\): \((5a)\) holds, the minors share the root \(\lambda=-2\).

### II.4 Boundary witnesses

- \(l=(0,1,0,0,0)\) is **not** \((5a)\)-feasible: \(\operatorname{rank}M=4\), \(\operatorname{rank}M_0=3\).
- \(l=(0,0,1,1,0)\) **is** feasible: \(a=0\), \(\operatorname{rank}H=2\), and both \((5a)\) and \((5b)\) hold.
  Thus forcing \(\operatorname{rank}H=2\) does not remove the \(a=0\) boundary.

The variety \(ad-bc=0\) is irreducible; its slice \(a=0\) has the two components \(a=b=0\) and \(a=c=0\).

## Part III. Anchored attempts (all failed)

The target is a fixed-pivot residual determinant
\[
\det\begin{bmatrix}1&x\\y&z\end{bmatrix}=z-xy,
\]
with the \(1\) supplied by \(A,C,L_0\), and with \(\operatorname{rank}M_0\) constant so that the determinant condition is equivalent to \((5a)\) at every parameter value.

1. Changing \(L_0\) to \(e_1+e_3\) makes \(\operatorname{rank}M_0=4\) constant, but
   \[
   \det M=ab+4ad+b^2-bc+cd,
   \]
   an irreducible quadratic, not a gate. Other \(L_0\) give similar quadratics.
2. With the diagonal \(A=\operatorname{diag}(0,1,1,1,0)\), some choices give constant rank, but \(\det M\) is a monomial (e.g. \(-ad\)).
3. A search over 500 random \(A\) with \(L_0=e_1+e_3\), \(C=e_5\), requiring \(\det M=\alpha d+\beta bc+\gamma\), found nothing.

## Part IV. Questions

**Question 1.** Can you give a concrete anchored block: matrices \(A,C,L_0\) for which \(\operatorname{rank}M_0\) is constant and
\[
\det M = z-xy
\]
with the \(1\) fixed by the input? Even a parametric family with \(n=6\) or a Schur-complement layout would be enough to restart the construction.

**Question 2.** Is the \(n=5\), \(q=2\) setting provably too small for an anchored gate, or is our search simply incomplete? If there is a general reason, what is the minimal \(n\)?

**Question 3.** How should the uniform spectral condition be combined with the anchored gate? We have the shift-chain unit-minor guard, but adding it must not saturate the row space that carries \((5a)\).

**Question 4.** If an anchored gate is obtained, what is the cleanest way to prove the full witness-extraction theorem (every feasible \(L\) decodes; every \((x,y,z)\) with \(z=xy\) lifts), including all \(a=0\) boundary components?
