# The single-row multiplication gate is closed for \(q=2\); four 2026 hardness papers and the next route

This note reports a negative structural result for the \(q=2\) multiplication gate, assesses four recent 2026 papers, and asks how to proceed.

## Part I. Setting and current status

For fixed \(A,C,L_0\), find \(L=[L_0;R]\) with
\[
(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\ \forall\lambda.
\]
The characterization, order spectrum, per-order conditions and minimum order are settled (Fernando 2026). The open problem is the complexity of \(\exists\Theta\), i.e. \(q1\).

Write \(S=\operatorname{row}[L_0;CA;C]\), \(Q=(\mathbb C^n)^*/S\), \(u=[L_0A]\), \(x=[l]\), \(v=[lA]\). For \(q=2\), \((5a)\) is \(u,v\in\operatorname{span}\{x\}\).

## Part II. The gate is closed for \(q=2\)

### II.1 The \(q=2\) dichotomy

- If \(u\ne0\), then \(x=\alpha u\) and the remaining condition on \(v\) is **linear** in \(l\).
- If \(u=0\), then \((5a)\) is the single quadratic condition \(\det[S;l;lA]=0\).

### II.2 Rank obstruction for \(n=5\)

For \(n=5\), \(q=2\), \(u=0\), one has \(W=\ker C\cap\ker L_0=S^\perp\oplus\langle w\rangle\), and the first two columns of \(A\) lie in \(W\). Hence
\[
D(l)=l_1(\operatorname{col}_2\cdot l)-l_2(\operatorname{col}_1\cdot l)
\]
depends only on \(l_1,l_2,l(w)\), so \(\operatorname{rank}D\le3\). The form \(xy-zw\) (rank 4, signature \((2,2)\)) is impossible.

The minimum for a **single** determinant with rank 4 is \(n=7,p=2\): \(S\) has rank 5, \(Q\) has dimension 2, and \(\dim W=4\).

### II.3 A complete rank-4 gate and its failure

Take \(n=7,p=2\), \(C=e_5^*,e_6^*\), \(L_0=e_7^*\), and \(A\) with
\[
\operatorname{col}_1=e_3,\quad \operatorname{col}_2=e_4,\quad
\operatorname{row}_5=e_3,\quad \operatorname{row}_6=e_4,\quad \operatorname{row}_7=0.
\]
Then \(L_0A=0\), \(S=\operatorname{span}\{e_3,e_4,e_5,e_6,e_7\}\), \(Q\) has coordinates \((l_1,l_2)\), and
\[
(5a)\iff l_1l_4-l_2l_3=0.
\]
This is a genuine full \((5a)\) gate, and \(D=l_1l_4-l_2l_3\) has rank 4 and signature \((2,2)\).

But \((5b)\) always fails. In general, \(u=0\) means \(L_0A=\alpha L_0+\beta CA+\gamma C\). Multiplying by a basis \(N\) of \(K_0=\ker[C;CA]\) gives
\[
H_{A,1}=L_0AN=\alpha L_0N=\alpha H_1.
\]
At \(\lambda=\alpha\) the first row of \(P(\lambda)=\lambda H-H_A\) vanishes, so
\[
\operatorname{rank}P(\alpha)\le1<2=\operatorname{rank}H
\]
whenever \(\omega=2\).

### II.4 The complete \(q=2\) no-go

- \(\omega=2\): \((5b)\) fails by the argument above.
- \(\omega\le1\): \(H\) has rank at most one, so \(lN\) is proportional to \(L_0N\) (or zero). Since \(S^\perp\subseteq K_0\) and \(L_0\in S\), we get \(x=l|_{S^\perp}=0\), hence \(v=0\): the gate is trivial.
- \(u\ne0\): \((5a)\) is linear.

Therefore **no \(q=2\) instance has a nontrivial multiplication gate together with \((5a)\) and \((5b)\)**.

### II.5 \(q=3\) restores \((5b)\) but absorbs the gate

For \(n=7,p=2,q=3\), the rows
\[
l_1=(1,2,3,6,0,0,0),\qquad l_2=(3,6,3,6,0,0,1)
\]
give a feasible instance: \(\operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C]=6\), and the \(2\times2\) minors of \(P\) have gcd 1 (so \((5b)\) holds).

However, in \(Q\) the vector \(v_1=[l_1A]\) is absorbed by \(x_2=[l_2]\): choosing \(x_2=v_1\) makes \(v_1\in\operatorname{span}\{x_1,x_2\}\), and \(l_1\) is unconstrained. The single-row gate is gone.

**Conclusion**: the single-row determinant gate architecture is closed. Either the gate must live in a **coupling** between rows (so \(x_2\) is forced by \(x_1\), not free), or the encoding must use a different mechanism.

## Part III. The four 2026 papers

### III.1 Löfberg, arXiv:2609.16886 (SOF is NP-hard)

Reduction from Betweenness to single-input multiple-output SOF; the Routh determinant \(\Delta=Nuv-1\) encodes betweenness; frequency separation aggregates conditions into one affine polynomial; fixed anchor values exclude spurious gains. **Use**: anchor values and gain bounds; NP-hard only, not complete.

### III.2 Ahmadi–Chaudhry–Narang–Tang, arXiv:2609.20636 (output feedback stabilization is NP-hard)

No polynomial (or pseudo-polynomial) algorithm unless P=NP, continuous and discrete; also plants where no polynomial-time algorithm can write a stabilizing controller in standard form. **Use**: hardness background and the “witness representation may be large” phenomenon; the condition is Hurwitz, not pencil rank, so it is not a direct source.

### III.3 Barkai–Shames, arXiv:2609.38728 (unconstrained SOF is NP-hard)

Reduction from Subset Sum; one input, \(N\) outputs, \(10N+3\) states; band-pass scalar prototypes with stabilizing gains near 1 and 2; a shared summing block forces \(\sum_i a_i k_i\) into a narrow interval; frequency separation plus Rouché root counts; explicit bounds and modulus margins. **Use**: bounded-gain techniques and root counting for all-frequency conditions; NP-hard only.

### III.4 Liu, arXiv:2610.00390 (SOF is \(\exists\mathbb R\)-complete)

SOF is \(\exists\mathbb R\)-complete for rational data, even controllable/observable two-input integer plants. The **effective gain dimension** \(\kappa\) (the number of gain directions that affect the characteristic polynomial) controls complexity: for fixed \(\kappa\), feasibility and rational synthesis are polynomial. There is also a strongly NP-hard minimal single-input family. The gadget \(\det\begin{pmatrix}s^q+a&b\\-1&s^q-a\end{pmatrix}=s^{2q}+b-a^2\) encodes residuals into coefficients. **Use**: the closest completeness source and the “fixed effective dimension ⇒ polynomial” template, which parallels fixed \(c\).

Also relevant: Majumdar, arXiv:2602.14037, proves ARM(3) \(\exists\mathbb R\)-complete using rank-forcing gadgets, a fixed-rank gauge block, and a composition lemma.

## Part IV. Questions

**Question 1.** Is the single-row determinant gate architecture genuinely dead, or is there a coupling construction that keeps \(x_2\) forced by \(x_1\) while preserving \((5a)(5b)\)? If it is dead, should the project abandon rank-4 gates entirely?

**Question 2.** Which route should come next:
(a) \(q\ge3\) coupling gate; (b) ARM(3) gauge/rank-forcing; (c) Liu-style coefficient encoding into the pencil; (d) fixed-\(c\) tractability and the structural paper?

**Question 3.** Can Liu's effective gain dimension be adapted to the observer as a fixed-\(c\) parameter, giving an analogue of “fixed \(\kappa\) ⇒ polynomial”? What would the observer analogue of \(\mathcal N_{\rm pole}\) be?

**Question 4.** Do the bounded-gain and root-counting techniques of Löfberg and Barkai–Shames help with the spurious-witness problem and the all-\(\lambda\) condition, even though their target is Hurwitz?

**Question 5.** Given the negative gate results, is the most valuable next output a structural paper (low-\(c\), rigidity, \(\exists\mathbb R\) upper bound, no-go theorems), or should we keep pushing one of the hardness routes?
