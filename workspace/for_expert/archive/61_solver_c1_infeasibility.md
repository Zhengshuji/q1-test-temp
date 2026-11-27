# Solver, \(c=1\) infeasibility, and all-\(q\) infeasibility of two instances: results and questions

This report collects the work since the previous one: a uniform stratum solver, the \(c=1\) structural lemma, the \(c=0\) obstruction, and the conclusion that two test instances are infeasible for every \(q\) under the project's convention. It ends with questions, the most important being whether that convention matches the original observer problem.

## Part I. Setting

With \(K_0=\ker[C;CA]\), \(N=N_K\), \(H=LN\), \(H_A=LAN\), \(\omega=\operatorname{rank}H\), \(c=k-\omega\), and
\(P(\lambda)=\lambda H-H_A\). The project convention is:

\[
L=[L_0;R]\ \text{full row rank},\qquad \operatorname{rank}[C;L]=p+q,
\]

together with \((5a)\) and \((5b)\). For a candidate \(V=\ker H\in\operatorname{Gr}(c,K_0)\),
\[
W_L=\ker[L_0N;L_0AN],\qquad W=V\cap A^{-1}V,\quad t=\dim W,\quad U=W+A(W).
\]
The constraint \(V\subseteq W_L\) is forced by \((5a)\) (the top \(r\) rows of \(H\) and \(H_A\) are fixed).

## Part II. Results

### II.1 A uniform stratum solver

For any \((q,\omega,c)\) the same pipeline applies:
1. \(c=k-\omega\), \(W_L\); enumerate \(V\in\operatorname{Gr}(c,W_L)\);
2. \(\operatorname{Ann}(V)=\langle h_0,u_1,\dots,u_{\omega-1}\rangle\), \(h_0=L_0N\);
3. bottom rows \(h_i=a_ih_0+\sum_j b_{ij}u_j\); admissibility \(H_A|_V=0\) is linear in \((a,b,g)\);
4. \(\operatorname{rank}H=\omega\) iff the \((q-1)\times(\omega-1)\) matrix \((b_{ij})\) has rank \(\omega-1\);
5. pencil test: the \(\omega\times\omega\) minors of \(P\) have constant gcd;
6. construct \(L\), verify \(\operatorname{rank}[C;L]=p+q\) and \((5a)(5b)\).

Any returned \(L\) is an exact witness; when \(\dim W_L=c\) and every bottom row is forced to \(b=0\), the solver returns a
row-space certificate \(\alpha\) with \(e_b=\alpha^{\mathsf T}\mathrm{Des}\) (infeasible). Otherwise a negative answer is
only a failed search.

The Lean kernels
\[
\ker\varphi_U=U\cap A^{-1}U,\qquad \dim\operatorname{range}\varphi_U=u-\dim(U\cap A^{-1}U),\qquad
\varphi\in\operatorname{range}f^{\mathsf T}\iff\varphi|_{\ker f}=0
\]
are machine-checked (axioms: propext, Classical.choice, Quot.sound).

### II.2 \(c=2\): the forced-plane obstruction is row-wise

When \(\dim W_L=2=c\), \(V=W_L\) is forced. The admissibility equations of a bottom row do not depend on the total
number of rows \(q\). For the two test instances, both bottom rows force \(b_i=0\) (\(\alpha=(-1,0)\)), hence every row of
\(H\) is proportional to \(h_0\), so \(\operatorname{rank}H=1<\omega=2\). This holds for every \(q\), not only \(q=3\).

### II.3 \(c=1\): a hyperplane lemma

Let \(V=L=\mathbb Cv\subseteq W_L\), and suppose \(W_L\subseteq D=K_0\cap A^{-1}K_0\). Then
\[
L_0ANv=0,\qquad RD_j\cdot(Av)=0,
\]
because \(v\in W_L\) and \(Av\in K_0\) while \(\operatorname{row}[C;CA]\) annihilates \(K_0\). Write \(Av=Nw\). The
admissibility condition for a bottom row reduces to
\[
(l_iAN)\cdot v=l_i\cdot(Nw)=h_i\cdot w=0.
\]
If \(w\notin\operatorname{span}(v)\), then \(\{h\in\operatorname{Ann}(L):h\cdot w=0\}\) is a proper hyperplane of the
\(\omega\)-dimensional \(\operatorname{Ann}(L)\), of dimension \(\omega-1\); \(h_0\) lies in it, so all \(q\) rows of \(H\) lie
in this \((\omega-1)\)-space and \(\operatorname{rank}H\le\omega-1<\omega\), impossible.

For the two test instances, the eigenlines of \(W_L\) are explicit:
- one instance: \(a(a-b)=0\), giving the rational lines \(\mathbb Cw_1\) and \(\mathbb C(w_0+w_1)\);
- the other: \(2a^2-2ab+b^2=0\), giving the complex conjugate lines \(b/a=1\pm i\).
On each eigenline the corresponding \(\varphi=(\varphi_1,\varphi_2)\) is nonzero (for the complex lines the computation
was done over \(\mathbb Q(i)\); \(\varphi=(1,0)\)), so \(b\) lies in a hyperplane of \(\mathbb C^{\omega-1}\) and the same
rank bound \(\operatorname{rank}H\le\omega-1\) holds.

### II.4 \(c=0\): the determinant obstruction

If \(\omega=k=q\) (so \(H\) is a full-rank square matrix, \(c=0\)), then
\[
P(\lambda)=L(\lambda I-A)N,\qquad \det P(\lambda)\ \text{has degree }k\text{ and leading coefficient }\det(LN)\ne0.
\]
Hence \(\det P\) is a nonconstant polynomial, has a root \(\lambda_0\) over \(\mathbb C\), and
\(\operatorname{rank}P(\lambda_0)<k=\omega\) — \((5b)\) fails. So \(c=0\) is infeasible for every \(q=k\).

### II.5 The two test instances are infeasible for every \(q\) (under the convention)

For the two instances, \(k=4\), \(\dim W_L=2\), \(W_L\subseteq D\), and both bottom rows are forced in the \(c=2\) layer.
Classifying by \(c=k-\omega\):
- \(c\ge3\): no \(V\), since \(V\subseteq W_L\) and \(\dim W_L=2\);
- \(c=2\): the row-wise forcing above;
- \(c=1\): the hyperplane lemma and the eigenline checks;
- \(c=0\): the determinant obstruction.

Therefore no \(q\ge1\) admits a solution for these two instances, under the convention.

### II.6 Complexity position

The solver is a search with exact witness verification; it is not a polynomial-time randomized algorithm (the
enumeration and the gcd test are not polynomial in general), so it does not place the problem in RP or BPP. The
decision problem satisfies \(\mathrm{DEC}(q)\in\exists\mathbb R\) via the direct original-pencil certificate
(\(Q(\lambda)=[\lambda L-LA;CA;C]\), \(QYQ=Q\) with \(\deg Y\le2s-2\), normal rank \(s\), converse via local Smith form),
and \(\mathrm{MIN}(k)\in\exists\mathbb R\) by finite disjunction. Membership in NP is not established, since the existential
witnesses may be algebraic rather than rational.

## Part III. Questions

**Question 1 (the convention).** Does the original observer problem require \(\operatorname{rank}[C;L]=p+q\), i.e., that
the rows of \(L\) are independent modulo the rows of \(C\)? Under this convention the two instances are infeasible for
every \(q\). If the original problem only requires \(L\) to have full row rank (without independence from \(C\)), which
parts of the analysis change — in particular, is \(V=W_L\) still forced when \(\dim W_L=c\), and does the row-wise
forcing argument survive?

**Question 2 (the \(c=1\) lemma).** Is the hyperplane argument correct as stated, and is the eigenline analysis
complete? In particular, if the eigenline equation is identically zero on \(W_L\) (every \(v\in W_L\) an eigenvector),
does a different argument apply?

**Question 3 (\(c=0\)).** Is the determinant obstruction correct over \(\mathbb C\)? Is there a loophole when
\(\det P\) is the zero polynomial (impossible here since \(\det H\ne0\), but perhaps in other strata)?

**Question 4 (the solver).** Is the row-space/rank/gcd pipeline a valid (if incomplete) decision procedure for each
fixed stratum? Are any conditions missing besides the lift completion (e.g., full row rank of \(H\), the pair-preserving
lift \(d'_C\ge\dim\ker Z_{\mathrm{pair}}\))?

**Question 5 (generalisation).** Should the \(c=1\) hyperplane lemma be generalised to arbitrary \(\omega\) and to
\(W_L\not\subseteq D\), and would that give a general structural infeasibility criterion for the strata with \(c=1\)?

**Question 6 (next step).** Given that the two instances are infeasible under the convention, is the right next step
(a) to check the original convention and possibly redo the \(c=2\) analysis, (b) to find a genuinely feasible instance
(e.g., with \(\dim W_L>c\)) and test the solver there, or (c) to proceed with the general component bound, which is
independent of the feasibility of these instances?
