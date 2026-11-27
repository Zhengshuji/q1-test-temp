# Status report: rank gates, spectral gates, and the fixed-\(\kappa_{\rm obs}\) FPT route

This note reports what has been established, what has been retracted, and what remains open. The reliability labels are:

- **P**: paper proof, not machine-checked;
- **E**: exact finite computation for the stated instance or identity;
- **S**: sketch or route, with a named missing step;
- **R**: retracted.

## Part I. Setting

For fixed \(A,C,L_0\), find \(L=[L_0;R]\) with
\[
(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\ \forall\lambda.
\]
Let \(K_0=\ker[C;CA]\), \(N\) a basis, \(k=\dim K_0\), \(H=LN\), \(H_A=LAN\), \(\omega=\operatorname{rank}H\). Then
\[
(5a)\iff \operatorname{row}(H_A)\subseteq\operatorname{row}H,
\]
and \((5a)\) gives \(H_A=FH\) for some \(q\times q\) matrix \(F\). With \(P(\lambda)=\lambda H-H_A\),
\[
(5b)\iff \operatorname{rank}P(\lambda)=\omega\ \forall\lambda
\iff \operatorname{im}H\cap E_\lambda(F)=\{0\}\ \forall\lambda.
\]
The complexity of \(\exists L\) is \(q1\).

## Part II. What has been done

### II.1 Rank-gate route: from fixed rows to a structural bound

Take \(q=4\), \(r_0=2\), \(r=2\), \(L=[L_0;R]\). With \(AN=NM+E\), \(M=N^+AN\), \(E=(I-NN^+)AN\), and \(Y=RN\),
\[
H=\begin{bmatrix}H_0\\Y\end{bmatrix},\qquad
H_A=\begin{bmatrix}H_{A,0}\\YM+RE\end{bmatrix},
\]
and
\[
(5a)\iff H_{A,0}\in\operatorname{row}H\ \text{and}\ RE\in\operatorname{row}H.
\]
The second condition is a Grassmannian incidence \(W_R=\operatorname{row}(RE)\subseteq\operatorname{row}H\), not an affine hyperplane in the entries of \(H\). This rules out the naive one-equation-per-incidence translation, not the route itself. (P; the expert has already confirmed this reading.)

A compressed determinant gate was constructed for \(q=4\), \(k=4\):
\[
H_0=[e_1;e_2],\qquad
Y=\begin{bmatrix}0&0&r_{11}&r_{12}\\0&0&r_{21}&r_{22}\end{bmatrix},
\]
so that
\[
\operatorname{rank}H=3\iff r_{11}r_{22}-r_{12}r_{21}=0
\]
(the determinant of the \(2\times2\) block; rank exactly 3 also needs the block nonzero, automatic on the chart \(r_{11}=1\)). (E for the identity.)

This compressed gate is **not liftable**: every free row of \(H_A=LAN\) satisfies \((H_A)_i=r_iAN\), so it depends only on the same free row \(r_i\). A construction whose \((H_A)_2\) contains \(r_{11},r_{12}\) (data of the first free row) cannot be realized by a fixed \(A\). (P)

A stronger structural result came out of this:

**Theorem (P).** Let \(H=[H_0;Y]\), \(H_0=L_0N\), \(Y=RN\), \(r=q-r_0\), \(\omega=\operatorname{rank}H\). If \((5a)\) and \((5b)\) hold, then
\[
\boxed{\omega\le r=q-r_0.}
\]

*Proof.* From \(L_0A\in\operatorname{row}[L_0;CA;C]\), right multiplication by \(N\) (which kills \(CA\) and \(C\)) gives
\[
H_{A,0}=M H_0
\]
for an \(r_0\times r_0\) matrix \(M\).

If \(\operatorname{row}H_0\cap\operatorname{row}Y=0\), then \(\operatorname{rank}H=\operatorname{rank}H_0+\operatorname{rank}Y\). At an eigenvalue \(\lambda\) of \(M\) on \(\operatorname{row}H_0\),
\[
\operatorname{rank}(\lambda I-M)H_0\le\operatorname{rank}H_0-1.
\]
The free \(P\)-rows are \(\lambda Y-H_{A,\rm free}\), of rank at most \(\operatorname{rank}Y\). Hence
\[
\operatorname{rank}P(\lambda)\le(\operatorname{rank}H_0-1)+\operatorname{rank}Y=\omega-1,
\]
contradicting \((5b)\).

If \(\operatorname{row}H_0\cap\operatorname{row}Y\ne0\), then
\[
\operatorname{rank}H\le\operatorname{rank}Y\le r.\qquad\square
\]

**Corollaries (P).**
- \(q=2\), \(r_0=1\): \(r=1<\omega=2\), so the \(q=2\) gate is impossible;
- \(q=4\), \(r_0=2\): \(r=2<\omega=3\), so the \(q=4,\omega=3\) gate is impossible;
- feasible instances must have \(\operatorname{row}H_0\subseteq\operatorname{row}Y\): the fixed rows are “absorbed” by the free rows.

### II.2 The rank window for a nontrivial gate

From \(\omega\le r\) and absorption, \(\operatorname{rank}H=\operatorname{rank}Y\). If \(\omega=r\), then \(\operatorname{rank}Y=r\) is an open condition, not a determinant equation; if \(\operatorname{rank}H_0=\omega\), absorption forces \(\operatorname{row}Y=\operatorname{row}H_0\), a linear condition. Therefore a quadratic rank gate can only live in
\[
\boxed{\operatorname{rank}H_0<\omega<r.}
\]
The minimal window is \(r=3\), \(\operatorname{rank}H_0=1\), \(\omega=2\). (P)

In this window, the natural \(q=5\) construction is
\[
H_0=[e_1;e_1],\qquad
Y=\begin{bmatrix}e_1\\(0,0,1,x)\\(0,0,y,z)\end{bmatrix},
\]
for which
\[
\det\begin{bmatrix}1&0&0\\0&1&x\\0&y&z\end{bmatrix}=z-xy.
\]
So \(\operatorname{rank}H=3\iff z\ne xy\), and the gate is \(z=xy\). (E)

But \(E=0\) (i.e. \(A(K_0)\subseteq K_0\)) is incompatible with \((5a)(5b)\) when \(\omega>0\): the standard rigidity argument shows that a feasible \(V\) is \(A\)-invariant, \(\operatorname{row}H=V^\perp\), and an eigenvector of \(A^{\mathsf T}|_{V^\perp}\) makes \(P(\lambda)\) row-dependent. So a liftable \(q=5\) gate needs \(E\ne0\). (P)

For \(E\ne0\), the obstruction is a spectral one. In the simplest model \(H_{A,\rm free}=YM\), the fixed rows of \(P\) are \((\lambda-1)e_1\), and \((5b)\) requires \(e_1\in\operatorname{row}(Y(\lambda I-M))\) for all \(\lambda\ne1\); random search over \(5000\) matrices \(M\) found no example. (P for the condition, E for the negative search.)

A sample-level liftable gate was found: at \(x=2,y=3,z=6\), with explicit \(M,u,v\), the data
\[
H=\begin{bmatrix}1&0&0&0\\1&0&0&0\\1&0&0&0\\0&0&1&2\\0&0&3&6\end{bmatrix},\qquad
H_A=\begin{bmatrix}1&0&0&0\\1&0&0&0\\7/4&0&-3/2&-3\\-1&0&13/2&13\\-3&0&39/2&39\end{bmatrix}
\]
satisfy \((5a)\), \((5b)\), and every free-row offset lies in the span of the two rows of \(E\). (E)

However, symbolizing \(x,y,z\) makes the offsets quadratic in \(x\), so \(H_A\) would not be linear in \(L\); the sample is not a symbolic gate. Searching for linear offsets gives only \(\gcd=\lambda-1\), i.e. a rank drop at \(\lambda=1\). (E/P)

The source of this drop is the pairing \(Y_1=e_1\), \(H_{A,1}=e_1\): the row \((\lambda-1)e_1\) vanishes at \(\lambda=1\). If \(Y_1\ne e_1\), then \(\operatorname{row}Y=\operatorname{span}(e_1,Y_1)\) is a fixed plane, so \(Y_2,Y_3\) satisfy linear conditions and there is no quadratic gate; hence a quadratic gate forces \(Y_1=e_1\). (P)

Thus the \(q=5\) rank gate is caught in:
- \(Y_1\ne e_1\): no quadratic gate;
- \(Y_1=e_1\): a rank drop at \(\lambda=1\), unless the offset of \(H_{A,1}\) has \(e_3,e_4\) components; 2000 random trials found no such liftable example. (E)

The \(q=5\) rank gate is therefore closed in the sense that no construction was found in any of the three natural cases; this is not an impossibility theorem. (S)

### II.3 The liftability rank bound

A proposed sufficient condition for lifting arbitrary compressed pairs, “[N E] invertible”, is impossible: \(N\subseteq\ker C\) and \(AN\subseteq\ker C\), since \(C(AN)=(CA)N=0\). Hence
\[
\operatorname{rank}[N\ AN]\le n-p<n,
\]
so \(R\mapsto(RN,RAN)\) is never surjective. The earlier “surjectivity” claim is retracted. (P; the retraction is itself P.)

The correct per-row test remains
\[
(H_i,H_{A,i})\in\operatorname{row}[N\ AN]\qquad(i=1,\dots,r).
\]

### II.4 Spectral route

The polarity is:
- \((5a)\) is a rank equality, hence polynomial **equations**;
- \((5b)\) is \(\gcd\{\text{maximal minors of }P\}=1\), a **nonvanishing** condition.

This matches the usual \(\exists\mathbb R\) format. (P)

A previous compressed “nonzero gadget” with \(H=fH_0\) and \(\gcd=f\) is retracted: at \(f=0\), \(H=0\), so \(\operatorname{rank}H\) changes and \((5b)\)'s fixed-\(\omega\) hypothesis fails. It is a gcd identity, not a \((5b)\iff f\ne0\) gadget. (R)

The correct requirements for a nonzero gadget are:
1. \(\operatorname{rank}H\) is constant in \(f\) (including \(f=0\));
2. the maximal-minor gcd of \(P\) is the scalar \(f\);
3. at \(f=0\), \(\operatorname{rank}P(\lambda)<\omega\) for some \(\lambda\);
4. at \(f\ne0\), \(\operatorname{rank}P(\lambda)=\omega\) for all \(\lambda\).

No construction satisfying all four is known. (S)

### II.5 Algorithms: fixed \(\kappa_{\rm obs}\)

Let
\[
\kappa_{\rm obs}=r\operatorname{rank}[N,AN].
\]
Since \(N\) has full column rank, \(k\le\kappa_{\rm obs}\) and \(r\le\kappa_{\rm obs}\). But \(q=r_0+r\) is **not** bounded by \(\kappa_{\rm obs}\), because \(r_0\) can grow. The earlier FPT proof using \(\binom{q}{\omega}\binom{k}{\omega}\) Bezout variables therefore does not give FPT as stated. (This was a correction from the previous report.)

A Gram certificate repairs the \(q\)-dependence:
- \((5a)\): with \(G_H=H^{\mathsf T}H\), \(G_S=H^{\mathsf T}H+H_A^{\mathsf T}H_A\),
  \[
  (5a)\iff e_\omega(G_H)>0\ \text{and}\ e_{\omega+1}(G_S)=0;
  \]
- \((5b)\): for the maximal minors \(f_i\) of \(P\), put the coefficient vectors of \(f_i,\lambda f_i,\dots,\lambda^{\omega-1}f_i\) into a matrix \(B\) with \(2\omega\) columns; then
  \[
  (5b)\iff e_0\in\operatorname{row}B\iff\exists x\in\mathbb R^{2\omega}:\ B^{\mathsf T}Bx=e_0.
  \]
  The matrix \(B^{\mathsf T}B\) is computed from
  \[
  K(\lambda,\mu)=\sum_{|J|=\omega}\det\big(P(\lambda)_{:,J}^{\mathsf T}P(\mu)_{:,J}\big),
  \]
  which has only \(\binom{k}{\omega}\le2^{\kappa_{\rm obs}}\) terms (Cauchy–Binet).

Hence the quantified variables are \(\kappa_{\rm obs}+2\omega+1=f(\kappa_{\rm obs})\), while \(q\) enters only polynomially in the coefficient computation. This gives a route to
\[
\text{fixed }\kappa_{\rm obs}\Rightarrow q1\in\mathrm{FPT}
\]
modulo standard real quantifier elimination. (P, modulo QE; E for the identity on a \(3\times3\) pencil, where \(B\) is \(18\times4\), \(e_0\in\operatorname{row}B\), \(B^{\mathsf T}Bx=e_0\), and \(e_2(G_H)=55>0\), \(e_3(G_S)=0\).)

The fixed-\(q\) polynomial claim is only a sketch: quantifying over \(Z,U\) and eliminating \(L\) linearly does not by itself give a polynomial algorithm, because a parametric linear-elimination lemma is missing. (S)

## Part III. Questions

1. **Audit the structural bound.** Is the proof of \(\omega\le r=q-r_0\) correct as stated, in particular:
   - the step \(H_{A,0}=M H_0\) from \(L_0A\in\operatorname{row}[L_0;CA;C]\);
   - the rank drop of \((\lambda I-M)H_0\) at an eigenvalue of \(M\);
   - the conclusion that a feasible instance must have \(\operatorname{row}H_0\subseteq\operatorname{row}Y\)?

2. **Audit the liftability bound.** Is \(\operatorname{rank}[N\ AN]\le n-p\) the right obstruction, and is the per-row test
   \[
   (H_i,H_{A,i})\in\operatorname{row}[N\ AN]
   \]
   the exact liftability criterion?

3. **Is the \(q=5\) rank gate really closed?** We have:
   - \(Y_1\ne e_1\) ⇒ fixed row space ⇒ linear condition;
   - \(Y_1=e_1\) ⇒ \(\lambda=1\) drop unless the offset of \(H_{A,1}\) has \(e_3,e_4\) components;
   - 2000 random trials found no such liftable example.
   Is there a structural reason, or is this only a search boundary? If it is structural, what is the correct no-go statement?

4. **Spectral gadget.** Can a \((5b)\iff f\ne0\) gadget satisfy all four requirements with \(H\) independent of \(f\)? The natural candidate is a pencil whose maximal minors have gcd exactly \(f\), with \(H\) full rank and a rank drop in \(P(\lambda)\) only at \(f=0\). What is the simplest construction?

5. **Fixed \(\kappa_{\rm obs}\):** is the Gram certificate
   \[
   B^{\mathsf T}Bx=e_0,\qquad
   B^{\mathsf T}B\text{ from }K(\lambda,\mu)
   \]
   sufficient to make the FPT proof rigorous, and what is the correct bit-complexity bound?

## Part IV. Bottom line

- The rank-gate route is strongly constrained: \(\omega\le r\), \(q=4\) is closed, and \(q=5\) has no construction in the three natural cases.
- The spectral route has the right polarity, but the earlier nonzero gadget is retracted; a correct four-condition gadget is still missing.
- The fixed-\(\kappa_{\rm obs}\) FPT has a repaired Gram-certificate route, with a verified identity on a small pencil.
- The fixed-\(q\) polynomial claim remains a sketch.
