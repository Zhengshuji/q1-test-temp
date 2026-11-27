# From the exact fibre theorem to the type-control conjecture: results, formalisation, and the next step

This report collects the results since the previous report, states the verification policy we now follow,
and asks for your judgement on the remaining paper proofs and on how to prioritise the project.

## Part I. Setting

Given \(A\in\mathbb C^{n\times n}\), \(C\in\mathbb C^{p\times n}\), \(L_0\in\mathbb C^{r\times n}\), one seeks
\(R\in\mathbb C^{(q-r)\times n}\) with \(L=[L_0;R]\) full row rank and

\[
(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\quad\forall\lambda .
\]

Put \(K=\ker[C;CA]\), \(k=\dim K\), \(N=N_K\), \(H=LN\), \(H_A=LAN\), \(c=k-\omega\),
\(W=V\cap A^{-1}V\), \(U=W+A(W)\), and \(P(\lambda)=\lambda H-H_A\).

**Verification policy.** Lean where feasible, and a reliable paper proof otherwise, is acceptable.
We do not intend to spend disproportionate effort formalising results whose paper proofs are stable;
we would rather ask you which paper proofs need your scrutiny and then move the project forward.

## Part II. Results and corrections

### II.1 The exact fibre theorem

For \(V\in\operatorname{Gr}(c,K_0)\), \(W=V\cap A^{-1}V\), \(t=\dim W\), \(U=W+A(W)\):

\[
\mathcal F_W=\{V\in\operatorname{Gr}(c,K_0):\ U\subseteq V,\ \operatorname{rank}(V\to K/V)=c-t\}.
\]

It is an open subset of \(\operatorname{Gr}(c-\dim U,K_0/U)\). The proof is the identify
\(\ker(V\to K/V)=V\cap A^{-1}V\). This replaces the incorrect condition
\(A(V)\cap V=A(W)\): the latter does not force \(V\cap A^{-1}V=W\).

### II.2 The \(c=2\) classification (rewritten)

For \(c=2\):

* \(t=2\): \(A(V)\subseteq V\). Distinct eigenvalues give
  \(\mathbb P(E_\lambda\cap K_0)\times\mathbb P(E_\mu\cap K_0)\); a scalar block gives
  \(\operatorname{Gr}(2,E_\lambda\cap K_0)\); a nontrivial Jordan block gives chain planes
  \(\operatorname{span}\{u,T_\lambda u\}\), with fibre dimension \(\dim(E_\lambda\cap K_0)-1\) for a fixed eigenline.
* \(t=1\): subtype A, \(A(L)\subseteq L\) (including \(AL=0\)): the added line \(x\) must satisfy
  \(Ax\notin V\); subtype B, \(A(L)\not\subseteq L\): \(V=L+AL\), and the exact condition is
  \(\operatorname{rank}[v,Av,A^2v]=3\). The old nonemptiness condition
  (\(D\ne0\) and \(A|_D\) not scalar) is false: a nilpotent Jordan block of size two on \(D\) satisfies it but
  \(A^2v=0\) for all \(v\in D\).
* \(t=0\): \(V\cap A^{-1}V=0\), open.

### II.3 The \(c=3\) classification (repaired)

* \(t=3\): invariant three-planes, indexed by elementary divisors (including distinct eigenvalues).
* \(t=2\): \(\dim U=3\) gives \(V=U\), admissible only if \(\operatorname{rank}\overline A_V=1\)
  (e.g. \(Ab\notin V\)); \(\dim U=2\) gives \(A(W)\subseteq W\), and \(V=W+\langle w\rangle\) with \(Aw\notin V\).
* \(t=1\): subtype A, \(AL\subseteq L\): \(V/L\) must satisfy \(U'\cap\bar A^{-1}U'=0\);
  subtype B, \(AL\not\subseteq L\): \(A^2v+V\) and \(Aw+V\) must be linearly independent in \(K_0/V\).
* \(t=0\): \(\operatorname{rank}\overline A_V=3\).

### II.4 The Kronecker representation

With \(D=K_0\cap A^{-1}K_0\), \(\iota:D\hookrightarrow K_0\), \(A_0=A|_D\), every \(W\) lies in \(D\), and
the pair \((\iota,A_0)\) is a representation of the Kronecker quiver. The incidence variety is the variety of
subrepresentations \((W,U)\) with \(\iota(W)\subseteq U\), \(A_0(W)\subseteq U\), together with the maximality
condition \(U=W+A_0(W)\) and the exact fibre condition of II.1. The pencil \(\lambda\iota-A_0\) has full
column normal rank, hence no right minimal indices; the Kronecker form classifies the ambient pair, while the
subspace strata are quiver-Grassmannian/incidence problems.

### II.5 The type-control conjecture

We no longer state a component bound as a theorem. The conjecture is: for fixed \(c\), the incidence variety
of pairs \((W,V)\) with \(W=V\cap A^{-1}V\) admits a finite stratification by locally closed varieties whose
geometry is controlled by the Kronecker type of \((\iota|_W,A|_W)\) together with the ambient embedding data,
each fibre being an open Grassmannian. The four required ingredients are: a finite base stratification, the
algebraicity of the fibre construction, the component behaviour of the total space, and a bound on the number
of base components. We also note that the Kronecker data include dimensions and multiplicities which may grow
with \(k\), so a \(k\)-independent component bound needs a separate argument.

### II.6 Formalisation

The following are formalised as standalone Lean kernels, compiled without `sorry`, with
`#print axioms` equal to `[propext, Classical.choice, Quot.sound]`:

* rank inequality: \(\dim U>\dim K-\omega\Rightarrow\operatorname{rank}f<\omega\);
* the lifting formula \(\operatorname{rank}[L_0;R]=r+\operatorname{rank}(\pi R)\);
* the explicit counterexample \(J_3(0)\), \(V=\langle e_1,e_2\rangle\): \(\dim(V\cap A^{-1}V)=1\) and no
  invariant line;
* the block criterion: \(\operatorname{rank}(\lambda I-A,-B)<\omega\iff\exists y\ne0,\ Ay=\lambda y,\ By=0\),
  together with the factorisation and splitting steps that pass from \(\lambda H-H_A\) to the block map;
* the hyperplane identities: the \(\operatorname{rank}Q\) formula, the kernel equivalence
  \(\ker[P;Q]\cong\ker[v,Av]\), and the rank identity
  \(\operatorname{rank}[P;Q]+(2-\operatorname{rank}[v,Av])=\delta\);
* the constant-matrix certificate identity \(P(V_rU_l)P=P\) for \(P=UV\).

### II.7 The polynomial certificate

For \(P\in\mathbb C[\lambda]^{q\times k}\) of rank \(\omega\) for every \(\lambda\), there is a polynomial
\(Y\) with \(\deg Y\le2\omega-2\) and \(PYP=P\). The construction uses the Smith form (the invariant factors are
nonzero constants) and the minor-Bezout generalised inverse: if \(p_I\) are the \(\omega\)-minors and
\(b_I\) Bezout coefficients with \(\sum b_I p_I=1\), \(\deg b_I<\omega\), then
\[
Y=\sum_I b_I\,\operatorname{adj}(\widehat{P_I}),
\]
and \(\deg Y\le2\omega-2\). The constant-matrix identity is formalised; the polynomial degree argument is paper.

### II.8 A correction and a scope condition

* The coefficient relation is \(Z_1u=a\sigma\), \(Z_2u=b\sigma\) with \(\sigma\in W\), not \(Z_1u=av\) with
  \(v\in X\); the earlier write-up had a type error, now corrected.
* The identity \(\operatorname{rank}[P;Q]=\delta-2+\operatorname{rank}[v,Av]\) requires \(\delta\ge2\); for
  \(\delta<2\) the natural-number subtraction wraps. We state the robust form
  \(\operatorname{rank}[P;Q]+(2-\operatorname{rank}[v,Av])=\delta\), and the paper form only under
  \(\delta\ge2\).

## Part III. Questions

**Question 1.** Are the corrected \(c=2\) and \(c=3\) classifications (II.2, II.3) acceptable as paper proofs?
Which steps would you want to see proved more carefully before they are used in a paper?

**Question 2.** Is the polynomial certificate proof (II.7) sound, in particular the degree estimate
\(\deg Y\le2\omega-2\) and the passage from the Smith form to the linear pencil case? Is there a gap you would
flag?

**Question 3.** Is the robust rank identity (II.8) the right statement for the paper, or would you state it
differently (for example, as \(\operatorname{rank}[P;Q]=\delta-(2-\operatorname{rank}[v,Av])\) with an explicit
nonnegativity hypothesis)?

**Question 4.** Given the verification policy above, which of the remaining open items should we prioritise for
project progress: proving the type-control conjecture (or a special case), the \(c=2/c=3\) algorithms, the
complexity of the component decomposition, the real-point question, or something else?

**Question 5.** Do you see a route to a genuine theorem for general \(c\), for example a bound on the number of
components via the Kronecker/quiver language, rather than a conjecture?

**Question 6.** Which paper proofs would you specifically like to review, and which would you advise us not to
attempt to formalise?

**Question 7.** What would you consider the strongest contribution of the present material, and what should we
do next to move the project forward (given that the paper itself is not being written at this stage)?
