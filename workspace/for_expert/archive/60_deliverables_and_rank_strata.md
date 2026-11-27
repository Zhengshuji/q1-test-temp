# Three deliverables and the rank strata \(B_{u,v}\): a request for adjudication and a direct proof

This report has two aims: to deliver the \(c=2\) feasibility criterion, the invariant-part repair, and the exact \(c=3\) list; and to ask whether the remaining general-\(c\) piece, the rank strata \(B_{u,v}\), can be settled directly.

## Part I. Setting

With \(K_0=\ker[C;CA]\), \(N=N_K\), \(H=LN\), \(H_A=LAN\), \(\omega=\operatorname{rank}H\), \(c=k-\omega\), and
\(P(\lambda)=\lambda H-H_A\). For \(V=\ker H\in\operatorname{Gr}(c,K_0)\),
\[
W=V\cap A^{-1}V,\quad t=\dim W,\quad U=W+A(W),\quad u=\dim U.
\]

## Part II. Results

### II.1 \(c=2\), \(q=3\): the forced-plane criterion

When \(\dim W_L=c\) (with \(W_L=\ker[L_0N;L_0AN]\), so \(V=W_L\) is forced), write
\(\operatorname{Ann}(V)=\langle h_0,u_1\rangle\), \(h_0=L_0N\), and any bottom row as
\(h_i=a_ih_0+b_iu_1\). If \(b_i=0\), then \(h_i\propto h_0\); if both bottom rows have \(b_i=0\), then
\(\operatorname{rank}H=1<\omega\), impossible. The admissibility equations \(H_{A,i}|_V=0\) are linear in
\((a_i,b_i,c_i)\), and

\[
\boxed{b_i\ \text{is forced to }0\iff e_b\in\operatorname{rowspace}(\mathrm{Des}_i).}
\]

If both rows are forced, the instance is infeasible. On the tested instances: instance 10 is feasible
(with witness \(L\)), instances 16 and 21 are infeasible for \(q=3\) (both bottom rows forced). This
is structural, not a failure of random search.

For \(\dim W_L>2\) we enumerated \(V\in\operatorname{Gr}(2,W_L)\) and constructed a feasible instance with
\(\dim W_L=3\): \(n=6\), \(p=1\), \(k=4\), \(q=3\),
\[
A: e_1\mapsto e_2,\ e_2\mapsto e_1,\ e_3\mapsto e_3+e_2,\ e_4\mapsto e_4,\ e_5\mapsto e_5,\ e_6\mapsto3e_6+e_2,
\]
\(C=e_1^{\mathsf T}\), \(L_0=e_3^{\mathsf T}\), and
\[
L=\begin{bmatrix}0&0&1&0&0&0\\0&0&1&0&0&1\\0&1&1&0&0&1\end{bmatrix},
\]
which satisfies \(\operatorname{rank}[C;L]=4\) and both \((5a)\) and \((5b)\).

### II.2 Invariant part: the cyclic-vector repair

The previous objection was that (i) the chain conditions were necessary but not sufficient, and (ii) the
quotient from chain bases to subspaces was uncontrolled. Both are bypassed by using a single **cyclic vector**.
For a single block of size \(c\) and eigenvalue \(\lambda\), put \(T=A-\lambda I\) and
\[
U_\lambda=\{x\in K_0:\ T^cx=0,\ T^{c-1}x\ne0\}.
\]
These two conditions are necessary **and sufficient**: they make \(x,Tx,\dots,T^{c-1}x\) independent
(if \(\sum a_jT^jx=0\), take the least \(j\) and apply \(T^{c-1-j}\) to get \(a_jT^{c-1}x=0\)), so
\[
\Phi:U_\lambda\longrightarrow\operatorname{Gr}(c,K_0),\qquad x\longmapsto\operatorname{span}\{x,Tx,\dots,T^{c-1}x\}
\]
has image exactly the single-block stratum. \(U_\lambda\) is open in the linear subspace \(\ker T^c\), hence
irreducible; \(\Phi\) is a morphism (Plücker coordinates are polynomial in \(x\)); the image of an irreducible
variety is irreducible. No quotient is taken.

For a fixed eigenvalue-labelled Jordan type \(\tau=\{(\lambda_i,c_i)\}\), the parameter space is
\[
\Omega=\Big\{(x_i)\in\prod_iU_{\lambda_i}:\ \operatorname{rank}\big[T_{\lambda_i}^jx_i\big]_{i,j}=c\Big\},
\]
an open subset of an irreducible product, and
\(\Phi_\tau((x_i))=\bigoplus_i\operatorname{span}\{T_{\lambda_i}^jx_i\}\) is a morphism whose image is the
stratum \(S_\tau\). Hence every \(S_\tau\) is irreducible or empty, and
\[
\boxed{N_{\rm inv}(c)\le\#\{\text{eigenvalue-labelled Jordan types}\}\le\sum_{\lambda\vdash c}s^{b(\lambda)}.}
\]

### II.3 The exact \(c=3\) list

The strata are indexed by \(t=\dim(V\cap A^{-1}V)\in\{0,1,2,3\}\). The list:

| # | Layer | \(t\) | \(u\) | Structural data |
|---|---|---|---|---|
| 1 | (3a) | 3 | 3 | three distinct eigenvalues: \(V=\ell_\lambda\oplus\ell_\mu\oplus\ell_\nu\) |
| 2 | (3b) | 3 | 3 | \(1+1+1\): \(V\subseteq E_\lambda\cap K_0\) |
| 3 | (3b′) | 3 | 3 | \(1+1\) at \(\lambda\), \(1\) at \(\mu\ne\lambda\) |
| 4 | (3c) | 3 | 3 | \(2+1\) at \(\lambda\): \(\langle u,T_\lambda u\rangle\oplus\ell_\lambda\), \(T_\lambda u\ne0\) |
| 5 | (3c′) | 3 | 3 | \(2\) at \(\lambda\), \(1\) at \(\mu\ne\lambda\) |
| 6 | (3d) | 3 | 3 | \(3\): \(\langle u,T_\lambda u,T_\lambda^2u\rangle\), \(T_\lambda^2u\ne0\) |
| 7 | (2a) | 2 | 3 | \(\dim(W+A(W))=3\), \(V=W+A(W)\) |
| 8 | (2b) | 2 | 2 | \(A(W)\subseteq W\), \(V=W\oplus\langle x\rangle\), \(Ax\notin W+\langle x\rangle\) |
| 9 | (1a) | 1 | 1 | \(AL\subseteq L\), \(V=L\oplus U'\), \(U'\cap\bar A^{-1}U'=0\) |
| 10 | (1b) | 1 | 2 | \(AL\not\subseteq L\), \(V=U\oplus\langle x\rangle\), \(Ax,A^2L\) independent mod \(V\) |
| 11 | (0) | 0 | 0 | \(V\cap A^{-1}V=0\) |

Exhaustiveness: \(t\in\{0,1,2,3\}\); for \(t=3\), \(V\) is invariant and the \(3\times3\) Jordan type is one of
the six above; for \(t=2\), \(U=W+A(W)\subseteq V\) and \(W\subseteq U\), so \(u\in\{2,3\}\); for \(t=1\),
\(AL\subseteq V\) and either \(AL\subseteq L\) or \(U=L+AL\); for \(t=0\), one open stratum. Mutual exclusivity
is immediate from \(t\) and the listed sub-cases. Irreducibility: (3a),(3b),(3b′) are products of projective
spaces/Grassmannians; (3c),(3c′),(3d) are the invariant strata covered by II.2; (2a),(2b),(1a),(1b),(0) are
open subsets of irreducible bases (note \(U\subseteq V\) and \(\dim V=3\) make \(u\le3\) automatic in (2a)).

### II.4 The remaining general-\(c\) piece: \(B_{u,v}\)

For \(t<c\), the stratum \(S_{t,u}\) is the image of
\[
\mathcal I_{t,u}=\{(W,U):W\subseteq U,\ A(W)\subseteq U,\ U\in\operatorname{Gr}(u,K_0)\},
\]
and the fibre over \(U\) is \(\operatorname{Gr}(t,U\cap A^{-1}U)\). Stratifying by \(v=\dim(U\cap A^{-1}U)\),
\[
\#\{\text{components of }S_{t,u}\}\le\sum_{v=t}^{u}\#\{\text{components of }B_{u,v}\},
\qquad
B_{u,v}=\{U\in\operatorname{Gr}(u,K_0):\ \dim(U\cap A^{-1}U)=v\}.
\]
The sets \(B_{u,v}\) depend only on \((A,u,v)\), not on \(c\).

## Part III. Questions

**Question 1.** Is the cyclic-vector argument (II.2) an acceptable proof that each fixed-type invariant
stratum is irreducible or empty, and hence that \(N_{\rm inv}(c)\le\sum_{\lambda\vdash c}s^{b(\lambda)}\)
is a component bound?

**Question 2.** Is the \(c=3\) list (II.3) exhaustive and mutually exclusive as stated? Are any strata
missing (for instance, a case where \(u=4\) is possible), or is the automatic bound \(u\le\dim V=3\)
correct in every stratum?

**Question 3.** Can you give a direct proof — or a counterexample — for the component count of \(B_{u,v}\)?
Specifically:
- Is \(B_{u,v}\) irreducible for all \((u,v)\), or are there reducible cases?
- If reducible, is there a uniform bound (in terms of \(u\), \(v\), and the Jordan structure of \(A\)) that
  does not require enumerating \(c\)?
- References on the rank strata of \(U\mapsto U\cap A^{-1}U\) (determinantal rank strata, quiver
  Grassmannians, degeneracy loci) would be very helpful.

**Question 4.** For the forced-plane \(c=2\) criterion (II.1), is the equivalence
"\(b_i\) forced to \(0\) \(\iff\) \(e_b\in\operatorname{rowspace}(\mathrm{Des}_i)\)" exactly right, and is the
infeasibility conclusion for instances 16/21 correct?

**Question 5.** If the answer to Question 3 is positive and uniform, is the resulting general-\(c\) bound
\[
N(c)\le\sum_{\lambda\vdash c}s^{b(\lambda)}+\sum_{t<c}\ \sum_{v=t}^{u}\#\{\text{components of }B_{u,v}\}
\]
the right shape, or should the two parts be combined differently?
