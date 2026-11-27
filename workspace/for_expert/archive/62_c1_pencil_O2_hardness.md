# The \(c=1\) pencil criterion, the \(O_2\) reduction, and a request for advice on unbounded-\(c\) hardness

This report closes the pencil branch of the \(c=1\) analysis, reduces the \(O_2\) continuous family, and asks for guidance on the unbounded-\(c\) hardness direction relevant to \(q1\).

## Part I. Setting

With \(K_0=\ker[C;CA]\), \(N=N_K\), \(H=LN\), \(H_A=LAN\), \(\omega=\operatorname{rank}H\), \(c=k-\omega\), and
\(P(\lambda)=\lambda H-H_A\). For \(c=1\), \(V=L=\mathbb Cv\subseteq W_L=\ker[L_0N;L_0AN]\) and
\(D=K_0\cap A^{-1}K_0\).

## Part II. Results

### II.1 O1: the pencil-bad criterion

Write \(W=\operatorname{im}H\), \(\mathbb C^q=W\oplus W'\), and \(Z:W\to\mathbb C^q\) with \(H_A=ZH\):
\[
Z=\begin{bmatrix}A_*\\B_*\end{bmatrix},\qquad
P(\lambda)=(\lambda I-Z)H=\begin{bmatrix}(\lambda I-A_*)H\\-B_*H\end{bmatrix}.
\]
Then
\[
\operatorname{rank}P(\lambda)<\omega\iff\exists\,0\ne y\in W:\ A_*y=\lambda y,\ B_*y=0.
\]
Consequences:
- \(B_*=0\) (i.e. \(H_A\in\operatorname{row}H\), \(H_A=SH\)): \(P(\lambda)=H(\lambda I-S)\), and
  \(\det(\lambda I-S)\) has a root, so the stratum is **infeasible**;
- \(B_*\ne0\) and \(A_*\) diagonalisable: the eigenvectors span \(W\), so not all can lie in the proper subspace
  \(\ker B_*\); hence the pencil is **good**;
- \(B_*\ne0\) and \(A_*\) non-diagonalisable: a single eigenline may be killed by \(\ker B_*\); this is the only
  remaining special case.

### II.2 The O1 small algorithm and a synthetic family

For a fixed candidate \((H,H_A)\), the definitive test is the gcd of the \(\omega\)-minors of \(P\). We implemented
the block quantities \(A_*,B_*\) together with this gcd. On the synthetic family
\[
L_0=[e_4;e_5;e_6],\qquad Ae_3=e_1,\qquad Ae_4=e_4,\ Ae_5=e_5,\ Ae_6=e_6,
\]
the computation gives \(B_*=0\) and \(\gcd=-(\lambda-1)^3\): the stratum is infeasible. Structurally, for every
admissible bottom row \(h=lN\) one has \(h_A=lAN=h-l_3e_3^*\), and \(e_3^*\in\operatorname{row}H\) whenever
\(l_3\ne0\); hence \(h_A\in\operatorname{row}H\) always, so \(B_*=0\). This proves the whole family infeasible.

### II.3 \(O_2\): reducing the continuous family

For \(c=1\) with \(d=\dim W_L>1\), write \(v(a)=\sum a_iw_i\). The condition \(Av(a)\in K_0\) is linear in \(a\);
let \(U\subseteq\mathbb C^d\) be its solution space. Then
\[
\mathbb P(W_L)=\underbrace{\mathbb P(U)}_{L\subseteq D}\ \cup\ \underbrace{\mathbb P(W_L)\setminus\mathbb P(U)}_{\text{open}}.
\]
- On \(\mathbb P(U)\): 182/183 apply — non-eigenlines are infeasible; eigenlines are finite (the equation
  \(\det[v,Av]=0\) is a quadratic form on \(\mathbb P(U)\)), and each is tested by \(\varphi\);
- On the open complement: \(Av\notin K_0\), so by 188 every \(h\in\operatorname{Ann}(L)\) has an admissible lift;
  the admissibility condition is vacuous, and feasibility reduces to the rank condition and the pencil condition,
  both of which are **open** conditions on \((v,H,\text{lifts})\).
Thus a witness on the open set proves feasibility; proving emptiness requires a structural argument (the
synthetic family of II.2 is an example where the whole open set is bad).

### II.4 Status of the \(c=1\) decision tree

| Branch | Status |
|---|---|
| \(L\subseteq D\), non-eigenline | infeasible (182) |
| \(L\subseteq D\), eigenline with \(\varphi\ne0\) | infeasible (183) |
| pencil \(B_*=0\) | infeasible (II.1) |
| pencil \(B_*\ne0\), diagonalisable | good |
| pencil \(B_*\ne0\), non-diagonalisable | eigenline check (II.2) |
| \(L\subseteq D\), \(\varphi=0\) or \(A|_{W_L}=\lambda I\) | separate branch |
| \(O_2\) outside open set | witness or structural emptiness |

## Part III. Questions

**Question 1 (O1 completeness).** Is the block criterion complete? In particular, in the non-diagonalisable case,
is it enough to check the (finitely many) eigenlines of \(A_*\) against \(\ker B_*\), or can a generalized
eigenvector chain produce a bad \(\lambda\) not detected by an eigenline?

**Question 2 (\(O_2\) emptiness).** Is the reduction of II.3 acceptable, and what is the right method to decide the
emptiness of the open outside set? Is a symbolic elimination over \(\mathbb P(W_L)\) (resultants in the parameters
of \(v\)) the standard route, or is there a structural criterion (e.g. an invariant forcing \(B_*=0\)) that avoids it?

**Question 3 (unbounded-\(c\) hardness for \(q1\)).** The decision problem is in \(\exists\mathbb R\). Which known
\(\exists\mathbb R\)-complete problem is the best target for a reduction to \(\mathrm{DEC}(q)\) with unbounded \(c\)?
Candidates we are considering: feasibility of quadratic systems (ETR), rank minimisation, and static output
feedback. Are there existing reductions from these to observer-order problems, or reasons to expect that the
observer structure is too rigid?

**Question 4 (fixed-\(c\) algorithm).** Is completing the fixed-\(c\) algorithm (c=1, then c=2) the right way to
approach \(q1\), or should the hardness direction take priority? We can prove \(c=1\) decisions and are close on
\(c=2\), but unbounded \(c\) is where hardness must live.

**Question 5 (literature).** Are you aware of work on the complexity of the \(\exists\Theta\) condition in the
observer-order characterisation (the \(q1\) question), or of lower bounds for minimal-order functional observers?
Any pointer would help us avoid repeating known reductions.
