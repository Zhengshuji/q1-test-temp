# A counterexample to the local leakage rigidity, and the corrected hardness route

This report records a correction to the previous discussion of local rigidity. The boundary case \(\omega=0\) is accepted as in your review. However, the local leakage rigidity (Section 4/5.1 of your previous report) appears to fail: the pencil step needs global \(A(K_0)\subseteq K_0\), and a feasible counterexample is given below. This reopens the invariant-subspace gadget route, under a corrected set of conditions.

## Part I. Setting

With \(K_0=\ker[C;CA]\), \(N=N_K\), \(H=LN\), \(H_A=LAN\), \(\omega=\operatorname{rank}H\), \(c=k-\omega\), \(P(\lambda)=\lambda H-H_A\), and the usual \((5a)(5b)\).

## Part II. The counterexample

Take the instance (all data rational)
\[
A=\begin{bmatrix}
0&0&0&0&0&0&1\\
0&1&0&-1&0&0&1\\
-1&0&0&-1&0&0&-1\\
-1&0&0&0&1&0&0\\
1&1&-1&0&-1&0&0\\
0&0&0&1&0&0&-1\\
0&0&0&0&0&0&1
\end{bmatrix},\quad
C=\begin{bmatrix}0&0&0&0&0&0&-1\\0&-1&0&1&0&0&0\end{bmatrix},\quad
L_0=\begin{bmatrix}0&0&-1&1&0&0&-3\end{bmatrix}.
\]
Here \(n=7\), \(p=2\), \(r=1\), \(k=4\). The witness
\[
L=\begin{bmatrix}
0&0&-1&1&0&0&-3\\
0&-1&0&0&-1&0&0\\
2&-1&2&0&-1&0&0
\end{bmatrix}
\]
satisfies \(\operatorname{rank}[C;L]=5=p+q\), \((5a)\) and \((5b)\) (verified by the seven consistency checks).

The compressed data:
\[
H=LN=\begin{bmatrix}-1&1&0&0\\0&-1&-1&0\\2&-1&1&0\end{bmatrix},\qquad
V=\ker H=\operatorname{span}\{(-1,-1,1,0),(0,0,0,1)\},
\]
so \(\omega=2\), \(c=2\). Computed in \(K_0\)-coordinates,
\[
A(-1,-1,1,0)=(0,0,0,-1),\qquad A(0,0,0,1)=(0,0,0,0).
\]
Hence
\[
A(V)\subseteq V\subseteq K_0,
\]
while \(A(K_0)\not\subseteq K_0\) (the announced rows contain a component outside \(K_0\)).

This contradicts the statement
\[
A(V)\subseteq K_0,\ \omega>0,\ (5a),(5b)\ \Longrightarrow\ \text{infeasible},
\]
and hence also the stronger conclusion “every feasible positive-rank observer must have \(A(V)\not\subseteq K_0\)”.

### II.1 Where the local argument fails

The first part is correct: from \(A(V)\subseteq K_0\) and \((5a)\), every row \(h\) of \(H\) annihilates both \(V\) and \(A(V)\), so \(\operatorname{row}H\subseteq(V+AV)^\perp\) and \(\omega\le k-\dim(V+AV)\); hence \(A(V)\subseteq V\).

The second part requires a global compressed matrix \(T\) with \(AN=NT\) and \(H_A=HT\), so that \(P(\lambda)=H(\lambda I-T)\) and \(T^{\mathsf T}|_{V^\perp}\) has an eigenvector. When only \(A(V)\subseteq K_0\) is assumed, \(A(K_0)\not\subseteq K_0\), the rows of \(H_A\) are not of the form \(hT\), and \(lA\) is not a functional on \(K_0\). The eigenvector argument does not apply. The instance above shows that the pencil can indeed be good in this situation.

### II.2 Consequences

- The global theorem \(A(K_0)\subseteq K_0\), \(0<\omega<k\) \(\Rightarrow\) infeasible, remains valid.
- The local lemma should be stated only as: \(A(V)\subseteq K_0\) and \(\omega>0\) \(\Rightarrow A(V)\subseteq V\). It does not imply infeasibility.
- The invariant-subspace multiplication gadget is therefore not excluded by local rigidity. A successful embedding may exist with \(A(K_0)\not\subseteq K_0\) but \(A(V)\subseteq K_0\) for the candidate \(V\).

### II.3 A leakage gadget attempt

We tried the natural construction: place the \(2\times2\) multiplication gadget on \(K_0\), add a leakage block to \(G=\mathbb C^2\) so that \(A(K_0)\not\subseteq K_0\), and choose an invariant \(V\) with \(A(V)\subseteq K_0\). Concretely, with \(K_0=\operatorname{span}\{e_1,\dots,e_4\}\), \(C=e_5^*\), gadget \(Ae_1=0\), \(Ae_2=e_2\), \(Ae_3=0\), \(Ae_4=e_4-e_1\), and leakage \(Ae_1\mapsto e_6\), one has \(V=\operatorname{span}(e_2,e_3)\) invariant and \(A(V)\subseteq V\subseteq K_0\). However, on \(V^\perp=\operatorname{span}(e_1^*,e_4^*)\) the map \(l\mapsto lA\) has rank one (the \(K_0\)-component of \(Ae_1\) is zero), so \(\operatorname{rank}P(0)\le1<2\). A random search over 40 instances with \(k=4\), \((q,\omega)\in\{(4,2),(3,2)\}\) found no witness.

## Part III. Questions

**Question 1.** Do you agree that the displayed witness is a counterexample to the local leakage rigidity? The check of \((5a)(5b)\) is exact; the key point is that \(A(V)\subseteq K_0\) but \(A(K_0)\not\subseteq K_0\).

**Question 2.** Given the correction, how should the leakage gadget be arranged so that on \(V^\perp\) the map \(l\mapsto lA\) has full rank \(\omega\), while \(A(V)\subseteq K_0\)? In the attempt above the obstruction is that \(Ae_1\) has zero \(K_0\)-component; should the gadget chart be chosen so that the invariant \(V\) does not involve the killed coordinate, or should the leakage be placed on a different block?

**Question 3.** Is the invariant-subspace gadget feasible at all with \(A(K_0)\not\subseteq K_0\), or is there a further rigidity (weaker than the local claim) that rules it out?

**Question 4.** The pair-lift fibre theorem now reads \(\mathcal L_V=(V+AV)^\perp\), with the fibre over a row \(h\) being \(l_0+\{g\in\operatorname{row}[C;CA]:g|_{AV}=-l_0|_{AV}\}\). Is there a simultaneous-lift obstruction (beyond \(d'_C\ge\dim\ker Z_{\mathrm{pair}}\)) that we should add to the solver?

**Question 5.** For the priority order: should we now (i) search for the corrected leakage gadget systematically (e.g., over chart rotations and leakage placements), (ii) revisit the \(\omega=0\) branch as a source of hardness, or (iii) consolidate the structural results? We would especially value a concrete suggestion for the chart/leakage placement in Question 2.
