# Three points for adjudication: the \(W_L\) constraint, \(S_{2,3}\), and the invariant-part count

This short report asks for adjudication on three points where our reading differs from the previous audit. Each point is stated with the exact claim and the argument, so that a one-line verdict (correct / gap / needs hypothesis) is enough.

## Part I. Setting

With \(K_0=\ker[C;CA]\), \(N=N_K\), \(H=LN\), \(H_A=LAN\), \(\omega=\operatorname{rank}H\), \(c=k-\omega\), and
\(P(\lambda)=\lambda H-H_A\). The admissible plane is \(V=\ker H\in\operatorname{Gr}(c,K_0)\), and
\(W=V\cap A^{-1}V\), \(t=\dim W\), \(U=W+A(W)\).

## Part II. The three points

### II.1 The \(W_L\) constraint

**Claim.** \(V\subseteq W_L:=\ker[L_0N_K;\ L_0AN_K]\).

**Argument.** The top \(r\) rows of \(H\) are \(L_0N\), and the top \(r\) rows of \(H_A\) are \(L_0AN\).
Since \(V=\ker H\) and \(\ker H\subseteq\ker H_A\), every \(v\in V\) satisfies \(L_0Nv=0\) and
\(L_0ANv=0\). Hence \(V\subseteq W_L\).

**Consequence.** If \(\dim W_L=c\), then \(V\) is forced. In the instances we tested
(\(k=4\), \(\omega=2\), \(c=2\), \(\operatorname{rank}[L_0N;L_0AN]=2\)) this is the case: \(\dim W_L=2=c\).
Then the six-layer classification classifies the type of a **single** plane, not a family of planes.

**Question 1.** Is this constraint correct, and is the consequence the intended reading? If \(V\) is forced,
should the \(c=2\) "algorithm" be described as: compute \(W_L\), determine the type of the single plane, and
run the lift/gcd test — rather than enumerating six families? If \(\dim W_L>c\), is the classification then
over \(\operatorname{Gr}(c,W_L)\) rather than \(\operatorname{Gr}(c,K_0)\)?

### II.2 Is \(S_{2,3}\) open or rank-exact?

**Our claim.** For \(t=2\), \(u=3\),
\[
S_{2,3}=\{W\in\operatorname{Gr}(2,D):\dim(W+A_0(W))=3\}=\{W:A_0(W)\not\subseteq W\}
\]
is the complement of the closed condition \(A_0(W)\subseteq W\), hence **open** in
\(\operatorname{Gr}(2,D)\), hence irreducible (if nonempty).

**Why.** For a 2-plane \(W\), \(\dim(W+A_0(W))\in\{2,3\}\); it equals 2 exactly when \(A_0(W)\subseteq W\).
The condition \(A_0(W)\subseteq W\) is the vanishing of all \(3\times3\) minors of \([u,v,A_0u,A_0v]\).
Therefore its complement is open.

**The previous audit's statement.** The audit said \(S_{2,3}\) is an exact-rank condition (possibly
reducible), via "\(\operatorname{rank}(f|_W)=1\) when \(W\cap A_0(W)\) has dimension one".

**Question 2.** Is the audit's condition equivalent to \(\dim(W+A_0(W))=3\)? We believe it is only
**sufficient**: when \(W\cap A_0(W)=0\) we also have \(\dim(W+A_0(W))=3\), but \(\operatorname{rank}(f|_W)\)
is not 1 in that case. If our reading is correct, \(S_{2,3}\) is open and the corrected component bound
\[
\binom{s}{3}+\binom{s}{2}+2s^2+4s+3
\]
should be restored (with the invariant-layer counts as in the previous report).

### II.3 The invariant-part count

**Our claim.** For \(t=c\) (invariant \(V\)), the Jordan type of \(A|_V\) is an eigenvalue-labeled partition;
each block is a product of projective eigenspaces/Grassmannians and affine chain fibres, hence irreducible
or empty. Therefore the number of components is at most the number of blocks:
\[
N_{\rm inv}(c)\le\sum_{\lambda\vdash c}s^{b(\lambda)}\le p(c)s^{c},
\]
where \(b(\lambda)\) is the number of blocks. This is a component bound, not merely a label count, because
each block is irreducible by construction.

**Question 3.** Is the per-block irreducibility argument acceptable? In particular, for the Jordan block of
size \(c\) the base is
\[
\{\ell\subseteq E_\lambda\cap K_0:\ \ell\subseteq(A-\lambda I)(K_0)\}
\]
(a projective linear subspace) and the fibre is affine (the chain preimages), so the block is irreducible or
empty. If this is accepted, the invariant part of the general-\(c\) bound is a theorem; the non-invariant part
reduces to the rank strata
\[
B_{u,v}=\{U\in\operatorname{Gr}(u,K_0):\ \dim(U\cap A^{-1}U)=v\}
\]
as described previously.

## Part III. Further questions

**Question 4 (the \(c=2\) instances 16/21).** With \(V=W_L\) forced, the admissibility equations
\(H_{A,i}|_V=0\) are consistent, but no good \(3\times k\) pencil appears in 600 random free parameters.
Can you give a criterion for the good locus to be nonempty in this normalized setting, or a reason why it
is empty? A single infeasible instance with proof would settle the algorithm's completeness.

**Question 5 (the direct certificate).** We have written the \(\exists\mathbb R\) proof with the original
pencil \(Q(\lambda)=[\lambda L-LA;CA;C]\), \(s=\operatorname{rank}[L;CA;C]\), the normal-rank condition and
the local-Smith converse, \(\deg Y\le2s-2\). Is the normal-rank condition correctly placed (it is not implied
by \(QYQ=Q\) alone), and is the \(s=0\) case the only boundary case?

**Question 6 (the eleven strata).** Are the eleven \(c=3\) strata, written with eigenvalue-labeled Jordan
data, exhaustive and mutually exclusive as stated? We have a written list; we would be glad to send it if the
answer depends on the exact notation.

**Question 7 (priorities).** Given the two corrections above, is the order still: (i) lift theorem
(formalise), (ii) \(c=2\) feasibility, (iii) component theorem, with \(\exists\mathbb R\) in parallel?
Or should the \(W_L\)-forced case be treated first as a separate, simpler theorem?
