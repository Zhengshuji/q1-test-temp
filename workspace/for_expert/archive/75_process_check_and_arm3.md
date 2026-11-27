# Where the hardness programme stands, and a request for a process check

This note summarizes the recent negative results on multiplication gates, the current positive results, and asks for a check of the reasoning and for new directions.

## Part I. Problem and notation

For fixed \(A,C,L_0\), find \(L=[L_0;R]\) with
\[
(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\ \forall\lambda.
\]
Characterization, order spectrum and minimum order are settled (Fernando 2026); the open problem is the complexity of \(\exists\Theta\), i.e. \(q1\).

Compressed notation: \(K_0=\ker[C;CA]\), \(N\) a basis, \(H=LN\), \(H_A=LAN\), \(\omega=\operatorname{rank}H\), \(c=k-\omega\), \(P(\lambda)=\lambda H-H_A\).

## Part II. Recent results

### II.1 The \(q=2\) gate is closed

- If \(u=[L_0A]\ne0\), \((5a)\) is linear.
- If \(u=0\), \((5a)\iff\det[S;l;lA]=0\).
- For \(n=5\), the resulting quadratic has rank \(\le3\), so \(xy-zw\) (rank 4) is impossible.
- The first complete rank-4 gate exists at \(n=7,p=2\): \(C=e_5^*,e_6^*\), \(L_0=e_7^*\), and \(A\) with \(\operatorname{col}_1=e_3,\operatorname{col}_2=e_4,\operatorname{row}_5=e_3,\operatorname{row}_6=e_4\); then
  \[
  (5a)\iff l_1l_4-l_2l_3=0.
  \]
- But \((5b)\) always fails: \(L_0A\in S\) gives \(L_0A=\alpha L_0+\beta CA+\gamma C\), hence \(H_{A,1}=\alpha H_1\); at \(\lambda=\alpha\) the first row of \(P\) vanishes, so \(\operatorname{rank}P(\alpha)\le1<2\).
- If \(\omega\le1\), then \(H\) has rank at most one; since \(S^\perp\subseteq K_0\) and \(L_0|S^\perp=0\), we get \(x=0\), so the gate is trivial.

**Conclusion**: no \(q=2\) instance has a nontrivial single-row multiplication gate together with \((5a)(5b)\).

### II.2 \(q=3\) restores \((5b)\) but absorbs the gate

An explicit \(q=3,n=7,p=2\) instance satisfies both \((5a)\) and \((5b)\) (rank 6; gcd of \(2\times2\) minors of \(P\) is 1), with rows
\[
l_1=(1,2,3,6,0,0,0),\quad l_2=(3,6,3,6,0,0,1).
\]
But the vector \(v_1=[l_1A]\) is absorbed by \(x_2=[l_2]\): choosing \(x_2=v_1\) makes the condition vacuous for \(l_1\).

### II.3 Coupled-plane gate: the invariance condition is linear

For \(q=3\), \((5a)\) mod \(S\) is \(v_1,v_2\in U=\operatorname{span}\{x_1,x_2\}\subseteq Q\).

- \(\dim Q=2\): if \(x_1,x_2\) are independent, \(U=Q\), so \((5a)\) is automatic; the only quadratic condition is \(x_1\wedge x_2=0\), not multiplication.
- \(\dim Q=3\): if \(v_i=Mx_i\) for a fixed induced \(M\), then \((5a)\iff MU\subseteq U\). Invariant 2-planes of a fixed \(M\) are finite or linear families.
- \(\dim Q\ge4\): \(MU\subseteq U\) is linear in Plücker coordinates; the Plücker relation is an identity for every 2-plane, not a gate.

The \(S\)-lift offsets are also linear. So in the fixed-\(A\) framework the coupled-plane condition cannot produce a quadratic multiplication gate.

### II.4 Coefficient encoding: nonvanishing versus equations

- Encoding \(\ell^2-h=0\) into a coefficient of a maximal minor conflicts with \((5b)\), which requires rank preservation/nonvanishing at every \(\lambda\).
- Encoding it into a coefficient of \((5a)\) does not test row inclusion: a local minor of \(H_A\) can vanish or not without deciding \(\operatorname{row}(H_A)\subseteq\operatorname{row}(H)\).

Thus the three gate variants (single-row, coupled-plane, coefficient) are all blocked in the fixed-\(A\) framework.

### II.5 Positive results

- **Spectral criterion**: \((5a)\Rightarrow H_A=FH\) for some \(F\), hence \(P=(\lambda I-F)H\) and
  \[
  (5b)\iff \operatorname{im}H\cap E_\lambda(F)=\{0\}\ \forall\lambda.
  \]
  Consequently \(\omega\le q-1\). This gives a one-line proof of the \(q=2,\omega=2\) obstruction.
- **Fixed \((q,c)\) tractability**: \(k=\omega+c\le q-1+c\). For fixed \((q,c)\), the compressed data and \(\kappa_{\rm obs}=r\operatorname{rank}[N,AN]\) are bounded, and feasibility reduces to a constant-dimensional real algebraic problem (polynomial time by quantifier elimination in theory).
- **Effective observer dimension**: \(\kappa_{\rm obs}=r\operatorname{rank}[N,AN]\). Fixed \(c\) does not bound it: in one instance \(c=1,\kappa_{\rm obs}=10\); in another \(c=2,\kappa_{\rm obs}=14\).
- **Fixed \(\kappa_{\rm obs}\) is not automatically XP**: \(q,\omega,r\) are bounded but \(k\) can grow; the rank conditions need \(\binom{k}{\omega+1}\) minors. Eliminating the auxiliary \(R\) in the compact certificate does not help, since it reduces to the unit ideal of the \(\omega\)-minors of \(QP\), again \(\binom{k}{\omega}\) minors.
- **Compact certificate**: \((5b)\iff\exists Q(\lambda),R(\lambda):QPR=I_\omega\). This uses \(\omega^2\) equations and no minor enumeration; for fixed \((q,c)\) it is a clean finite certificate. An explicit certificate for the \(3\times3\) pencil with \(Q=[[1,2,-1],[-2,2,2]]\) has been verified exactly.
- A Lean kernel verifies the rank-nullity core of \(\kappa_{\rm obs}\) (pair-map kernel dimension), with no extra axioms.

## Part III. Questions

**Question 1 (process check).** Please check the no-go arguments, especially:
- the \(q=2\) proof that \(\omega\le1\) forces \(x=0\);
- the claim that the coupled-plane condition is linear for fixed \(A\);
- the claim that coefficient encoding conflicts with the nonvanishing in \((5b)\).
Are there gaps, hidden assumptions, or a missed mechanism?

**Question 2 (ARM(3)).** A direct embedding \(X=L\) fails: \(q=3\) makes \(\operatorname{rank}L\le3\) automatic, while \(q>3\) gives no rank bound. The only interface I see is \(X=[L;L_{\rm fix}]\), where \(\operatorname{rank}X\le3\) becomes a row-inclusion condition, matching \((5a)\). Is this viable? How should the affine constraints and the spectral guard be encoded?

**Question 3 (fixed \((q,c)\)).** Is the fixed-\((q,c)\) tractability theorem correct and interesting enough to be the main algorithmic result? Is there a route to fixed-\(\kappa_{\rm obs}\) XP via the special structure \(P=\lambda H-H_A\), rather than generic Smith forms?

**Question 4 (new directions).** Given that the gate programme is blocked in the fixed-\(A\) framework, is there a mechanism I have not considered—e.g., encoding into the input \((A,C,L_0)\), using several observer rows with a fixed gauge, or a completely different reduction source?

**Question 5 (priority).** Should the next effort go to ARM(3)/gauge, to the structural/algorithmic paper, or to a different hardness source?
