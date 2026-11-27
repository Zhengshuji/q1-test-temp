# The active-subspace test: which of its three conditions can be made generic, and can a component index carry a discrete choice?

Following the previous report, the decision has been reformulated as an existential choice of a row space
\(W\). This note records the primitives that are now proved, the structural facts and corrections that followed,
and three concrete questions. The central one concerns the *type* of the third condition as a function of \(W\).

---

## Part I. Setting

Fix \(A\in\mathbb Q^{n\times n}\), \(C\in\mathbb Q^{p\times n}\), \(L_0\in\mathbb Q^{r_0\times n}\); a witness is
\(R\in\mathbb F^{m\times n}\), \(\mathcal L=[L_0;R]\),
\[
K_0=\ker[C;CA],\quad k=\dim K_0,\quad N\ \text{a basis},\quad H=LN,\quad H_A=LAN,\quad \omega=\operatorname{rank}H,
\]
\[
(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \operatorname{rank}(\lambda H-H_A)=\omega\ \ \forall\lambda .
\]

**Kernel lemma.** Feasibility implies \(\ker H=\ker H_A\). (From \((5b)\) at \(\lambda=0\): \(\operatorname{rank}H_A=\operatorname{rank}H\); with \((5a)\) the two row spaces coincide.) Hence \(H,H_A\) have the same zero columns and the same rank on every set of columns.

**Fibrewise rigidity.** For an \(\omega\)-dimensional \(W\), let \(M_W\) be the linear space of free rows whose compressed rows lie in \(W\). On the exact-rank part of \(M_W\), \((5a)\) is automatic and \((5b)\) is open, so the feasible set is Zariski open in \(M_W\), hence dense whenever non-empty. Therefore every polynomial relation satisfied at all feasible points of an active fibre is an identity on that fibre.

**The three tests.** With
\[
\Phi(r)=(rN,rAN),\qquad \mathcal S=\operatorname{im}\Phi=\operatorname{row}[N\ AN],\qquad
\mathcal T_W=\mathcal S\cap(W\oplus W),
\]
a free row may be placed in the fibre of \(W\) exactly when its pair lies in \(\mathcal T_W\). For a candidate \(W\):

* (i) **compatibility**: every fixed pair \((h_i^0,g_i^0)=\bigl((L_0)_iN,(L_0)_iAN\bigr)\) lies in \(W\oplus W\);
* (ii) **rank completion**: \(\operatorname{span}\bigl(\{h_i^0\}\cup\pi_1(\mathcal T_W)\bigr)=W\), with enough free rows;
* (iii) **spectral feasibility**: for the pencil built from generic admissible data, the \(\omega\times\omega\) minors are coprime.

Feasibility is then equivalent to the existence of a \(W\in\operatorname{Gr}(\omega,k)\) passing all three.

---

## Part II. Results

### II.1 Six primitives, all acting on the instance data

Per compressed column let the data contribute
\[
H\text{'s column }i=(a_i;u_i),\qquad H_A\text{'s column }i=t_i\,(b_i;v_i),
\]
with \(a_i,b_i\) read off \(L_0\), \(t_i\) off \(A\), and \(u_i,v_i\) free. At layer one with two columns and
exactly two compressed rows, the fixed-row parts of the relation \(v\neq0\) with \(v^{\mathsf T}H=0\) and
\(v^{\mathsf T}H_A=0\) give
\[
\det\begin{pmatrix}a_1&a_2\\ t_1b_1&t_2b_2\end{pmatrix}=0 .
\]
This single identity produces the following.

1. **Literal**: \(a=(1,0)\), \(b=(0,0)\) is feasible iff \(t\neq0\).
2. **Equation**: with \(\dim(AK_0)=1\) only layer one survives; choosing the data so that \(H\)'s columns are \((t,0)\)-type and \(H_A\)'s are multiples of \((1,1)\) makes feasibility equivalent to \(t=0\).
3. **Booleanity**: \(a=(x,0)\), \(b=(1,1)\), \(t=(1,x-1)\) gives \(x(x-1)=0\), i.e. feasibility iff \(x\in\{0,1\}\). (Layer two is excluded because two compressed rows and two columns make the pencil square, see II.2(b).)
4. **Conjunction of equations**: two fixed rows give the relation twice as many equations; with \(L_0=\begin{pmatrix}x&0&1&0\\ y&0&1&0\end{pmatrix}\) and \(\dim(AK_0)=1\), feasibility is equivalent to \(x=y=0\).
5. **Conjunction of non-equalities**, arbitrary \(k\): an anchored block-diagonal direct sum is feasible iff \(\prod_i t_i\neq0\).
6. **Negation**: the reduction computes the data, so feeding \(1-x\) tests the negation of a Boolean parameter.

All six are proved; 3 and 4 were additionally checked on rational parameter values.

### II.2 Structural facts

**(a)** By \((5a)\) every row of \(P(\lambda)=\lambda H-H_A\) is a combination of rows of \(H\), so
\(\operatorname{rank}P(\lambda)\le\omega\) holds **automatically, for every instance**. Consequently the
\((\omega+1)\)-minors vanish identically for reasons that have nothing to do with the data; the content of
\((5b)\) is the *coprimality of the \(\omega\)-minors*.

**(b)** If the pencil is square, \(r=k=\omega\), then \(\det P\) has degree \(r\) with leading coefficient
\(\det H\neq0\), so it has a complex root and \((5b)\) fails. (This needs \(r=k=\omega\); for \(k>\omega\),
\(\omega\) rows can be of full row rank for all \(\lambda\), so no row-count bound follows in general.)

**(c)** Layer zero is trivial: \(H=H_A=0\) is equivalent to \(L[N\ AN]=0\), and then \((5a),(5b)\) hold. So an
instance with \(r_0=0\), or with \(L_0\) annihilating \([N\ AN]\), is **always feasible** and carries no
information. A useful reduction therefore requires \(L_0\) to act non-trivially on \(K_0\).

**(d)** If \(\omega=1\) and some fixed \(h_i^0\) or \(g_i^0\) is non-zero, the compatibility test pins \(W\)
uniquely; the active set has at most one point.

**(e)** On the witness side there is no filtering: a polynomial vanishing at all feasible points is an identity
on each active fibre, so it excludes no witness. This does not by itself obstruct a reduction, because
feasibility is a condition on the instance data, not on the witnesses.

### II.3 Corrections of earlier statements

1. *"Layer two masks lower layers"*: withdrawn. The instance we used had a \(2\times2\) pencil at layer two,
   which is square, hence impossible for every parameter; the instance was infeasible at every layer.
2. *"The reduction programme is impossible because the source variables can be placed neither in the data nor in the witness"*: withdrawn. The error was to infer "no reduction" from "no witness filtering"; a
   constraint that holds automatically on a fibre is exactly what soundness wants.
3. *"Two active subspaces on \(\operatorname{Gr}(2,3)\)"*: withdrawn. The test fixed \(W\) but sampled free rows
   outside \(\mathcal T_W\), so points belonging to other fibres were counted as active. With the correct
   parametrisation (restricting the free rows to the left null space that defines \(\mathcal T_W\)) none of the
   twelve candidates was active.
4. *"For \(\omega<\min(k,r)\) the pencil must be identically rank-deficient, so random instances fail"*: withdrawn,
   see II.2(a). The reason those probes found no active subspace is **not known**.

### II.4 Empirical facts

For the Booleanity instance the active set inside the projective line of compatible subspaces is a **single**
point, and the two Boolean values correspond to the two coordinate points \([1:0]\) and \([0:1]\): at \(x=0\)
the active space is \(\operatorname{span}\{(0,1)\}\), at \(x=1\) it is \(\operatorname{span}\{(1,0)\}\), and
elsewhere there is none. Probes over \(\operatorname{Gr}(2,3)\), correct or otherwise, produced no active
subspace at all.

---

## Part III. Questions

**Q1.** What is the type of test (iii) as a function of \(W\)? On the locus where (i) holds, is
\[
\{W:\ \text{the generic admissible pencil is spectrally regular}\}
\]
open, closed, or neither? If it is open, then the active set is relatively open in the compatibility locus, and
the only possibilities are: empty, a single point (the pinned case), or a positive-dimensional set. A naive test
once seemed to refute this, but that test was flawed, so the question is open on our side.

**Q2.** Suppose the active set is a union of finitely many connected components — something openness would
allow, while isolated points would not. Can the **component index** then serve as the discrete datum of a
Boolean assignment, with a decoding that is constant on each component? Would such a decoding satisfy the
soundness obligation (every feasible witness decodes to a valid source solution), or does it force a condition
that the fibre cannot satisfy?

**Q3.** Is there a structural criterion, in terms of \(\mathcal S=\operatorname{row}[N\ AN]\), the fixed pairs,
and \(k,\omega\), that makes the active set have exactly \(2^s\) components? For instance, can the data be chosen
so that the compatible locus is a product of \(s\) projective lines and the spectral test cuts each into two
components?

**Q4.** Since the square case is impossible and the top layer is the only one that is generically feasible for
unstructured data, is the natural object for a reduction the top layer, where \(W=\mathbb F^{1\times k}\) and no
Grassmannian appears? If so, what does the choice of witness then encode?

**Q5.** Which single computation would you regard as decisive for the existence of isolated multi-active sets?
We can exhaust \(k=2\) and \(\operatorname{Gr}(2,3)\) symbolically, so the question is what to compute there.

### Reliability

| item | label |
|---|---|
| kernel lemma, fibrewise rigidity | proved (with the field and fixed-row qualifications) |
| the six primitives | proved; 3 and 4 also checked on rational values |
| II.2(a), (b), (c), (d) | proved |
| II.3 items 1, 3, 4 | withdrawn by us; II.3 item 2 withdrawn after a self-check |
| the type of test (iii) | **open** |
| existence of isolated multi-active sets | **open** (no example, no impossibility) |
