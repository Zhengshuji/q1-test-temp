Mathematical audit of the 24 propositions
I have reviewed the checklist against the available project proofs, the earlier mathematical corrections, and the recorded Lean formalization status.

My overall assessment is that the mathematical framework is substantially coherent. Several of the propositions are correct and can be accepted as stated, subject to clearly identifying their hypotheses. However, there are also points that deserve correction before these results are incorporated into a definitive paper.

In particular, I identify:
- One definite formulation defect: B.4, concerning the transpose in the eigenvector criterion.
- One substantial gap requiring additional hypotheses and clarification: D.1, concerning the recursive lower-bound argument.
- One geometric formulation requiring repair: B.13, concerning the projective incidence variety.
- Several important qualifications concerning B.8, B.9, G.1, B.16 and B.21.
I will follow your requested order and use exactly the three verdicts:
1. 成立 (Valid): The mathematical assertion follows from the stated hypotheses.
2. 有缺口 (Gap): The proof as presented does not establish the assertion, or contains a formulation error.
3. 需要额外假设 (Additional assumptions required): The assertion becomes valid after specifying the missing conditions.
An important distinction throughout this review is between the correctness of a theorem and the completeness of its proof. A proposition may be mathematically correct even if its current proof is incomplete.

I. First tier: Framework and complexity
1. A.1 — Quotient formulation of (5a)
成立
The equivalence
\[
(5a)\iff
\pi(\mathcal VA)\subseteq\pi(\mathcal V)
\]

is correct, provided that
\[
\mathcal J=\operatorname{row}[C;CA]
\]

and \(\pi\) is the quotient map modulo \(\mathcal J\).

Indeed, the original condition is
\[
\operatorname{rank}
\begin{bmatrix}
\mathcal LA\\
\mathcal L\\
CA\\
C
\end{bmatrix}
=
\operatorname{rank}
\begin{bmatrix}
\mathcal L\\
CA\\
C
\end{bmatrix}.
\]

By the elementary row-space characterization of rank equality, this is equivalent to
\[
\operatorname{row}(\mathcal LA)
\subseteq
\operatorname{row}\mathcal L+\mathcal J.
\]

Applying the quotient map gives
\[
\pi(\operatorname{row}(\mathcal LA))
\subseteq
\pi(\operatorname{row}\mathcal L).
\]

Conversely, the inclusion in the quotient implies that every row of \(\mathcal LA\) belongs to \(\operatorname{row}\mathcal L+\mathcal J\).

There is no difficulty with this equivalence.

An important qualification concerning the lower bounds.

The quotient equivalence itself does not require \(\mathcal L\) to have full row rank or to contain \(L_0\).

However, the optimization lower bounds derived from the layer decomposition do require the relevant admissibility assumptions.

For example, if
\[
q=\rho+c,
\]

and one has two independent inequalities
\[
\rho\ge \rho_0,\qquad c\ge c_0,
\]

then
\[
q\ge \rho_0+c_0.
\]

More generally,
\[
\min_x(f(x)+g(x))
\ge
\min_x f(x)+\min_x g(x).
\]

This inequality is always valid, but equality requires a common minimizer of the two terms. Separate attainability does not imply simultaneous attainability.

Regarding the additional question about
\[
c\ge c_0,\qquad c\ge1,
\]

the correct combined statement is
\[
\boxed{c\ge\max\{c_0,1\}.}
\]

The two bounds can be attained simultaneously only if an admissible candidate realizes that maximum. This is not guaranteed by the two inequalities alone.

Suggested improvement: Keep A.1 and the optimization consequences as two separate propositions. Do not make the attainability of the combined lower bound part of A.1.

2. D.1 — Recursive lower bound
需要额外假设
The claimed inequality is
\[
P(A,B,S)\ge
\dim S+
\dim\frac{AS+S+B}{S+B}.
\]

The proposed proof uses the recursive formulation
\[
P=
\min\left\{
\dim U:
T\subseteq U,\quad
\Phi(U)\subseteq\frac{U+C}{C}
\right\}.
\]

I regard this as a promising approach, but there are two issues that must be settled.

First: the quotient operator must be well-defined.

Whenever a map is supposed to induce a map on a quotient, one must verify the corresponding invariance condition.

For example, if an operator is to descend to a quotient by \(S+B\), then one needs the appropriate inclusion
\[
\Phi(S+B)\subseteq S+B.
\]

This cannot be silently assumed.

There is a related issue already encountered in your project: the original state operator does not generally induce an endomorphism on \(\mathbb C^n/\mathcal J\), because
\[
A(\mathcal J)\not\subseteq\mathcal J.
\]

The valid construction in that setting is a map into a further quotient, not an endomorphism of the original quotient.

Consequently, the definition of \(\Phi'\), its domain, and its codomain need to be written explicitly.

Second: the empty feasible-set convention.

The November 1 project report explicitly identifies this issue.

If \(P\) is defined as an infimum over natural numbers and the feasible family is empty, then the numerical infimum may be interpreted as zero rather than \(+\infty\).

The clean formulation is
\[
P=
\begin{cases}
\min\{\dim U:U\text{ feasible}\},
&\text{if feasible},\\
+\infty,&\text{otherwise}.
\end{cases}
\]

Alternatively, explicitly assume that the feasible family is nonempty.

Recommended proof direction.

I would avoid proving the result through an abstract quotient recursion until the induced map is fully established.

Instead:
1. Fix an arbitrary feasible \(U\).
2. Show that it contains the forced subspace \(S\).
3. Pass to the quotient by \(S+B\).
4. Establish that the image of the relevant operator is contained in the quotient image of \(U\).
5. Deduce the dimension inequality for this particular \(U\).
6. Take the minimum only after addressing nonemptiness.
This per-feasible-subspace argument is generally safer than beginning with an infimum.

The existing Lean declaration for the arithmetic core is useful, but it does not by itself settle the well-definedness of the underlying mathematical construction. 
REPORT_2026-11-01_EN.md


3. G.1 — The \(\exists\mathbb R\) upper bound
成立
I accept the basic strategy:
\[
\boxed{\mathrm{DEC}(q)\in\exists\mathbb R.}
\]

The important achievement here is the chart-free formulation using \(Z\), rather than enumerating Grassmannian charts.

The central equivalence is
\[
\ker(CAZ)=Z\cap\mathcal V.
\]

Under the relevant admissibility assumptions, this yields the translation
\[
(A)\iff A(S)\subseteq Z,
\qquad S=Z\cap V.
\]

This eliminates the need to encode a chart-dependent condition involving a potentially exponential number of coordinate cases.

The second important ingredient is the polynomial left-inverse certificate
\[
X(\lambda)P(\lambda)=I_t,
\]

with
\[
\deg X\le t-1.
\]

For a polynomial matrix \(P(\lambda)\) with \(t\) columns, pointwise full column rank over \(\mathbb C\) for every \(\lambda\) is equivalent to the existence of a polynomial left inverse, provided the relevant polynomial matrix has full column rank over \(\mathbb C(\lambda)\).

The Bézout identity behind this equivalence is standard over the PID \(\mathbb C[\lambda]\).

The polynomial identity can be converted into finitely many coefficient equations.

The claimed size
\[
O(n^3)
\]

is plausible and consistent with the structured certificate described in the project reports.

Two qualifications are important.
1. The degree bound on \(X\) must be justified by the precise polynomial-matrix right-inverse theorem being invoked. It should not be inferred merely from the fact that \(P\) has degree one.
2. The standard definition of \(\exists\mathbb R\) uses real variables. If the input and unknown matrices are complex, explicitly replace every complex variable and equation by its real and imaginary parts.
For rational real input, this realification changes the size only by a constant factor.

I would also recommend stating the coefficient bit-size bound explicitly. A polynomial number of variables is not, by itself, a complete polynomial-size encoding argument.

Verdict: The mathematical route is valid. The paper should make the degree-bound theorem and the realification step explicit.

The earlier project report also correctly distinguishes the Lean-checked algebraic lemmas from the full complexity encoding. 
10_status_and_direction.md


4. F.1 — Rank barrier
成立
The statement is
\[
(5b)\text{ at }\lambda_0
\quad\Longrightarrow\quad
\rho\le r(\lambda_0),
\]

where
\[
r(\lambda_0)
=
\dim\pi\bigl(\mathbb C^n(\lambda_0I-A)\bigr).
\]

This is correct.

The proof can be made particularly transparent by working directly in the quotient.

From (5a),
\[
\pi(\mathcal VA)\subseteq\pi(\mathcal V).
\]

Therefore
\[
\pi\bigl(\mathcal V(\lambda_0I-A)\bigr)
\subseteq\pi(\mathcal V).
\]

On the other hand, (5b) at \(\lambda_0\) implies that the quotient rank of the pencil is exactly \(\rho\).

Thus
\[
\dim\pi\bigl(\mathcal V(\lambda_0I-A)\bigr)=\rho.
\]

Since
\[
\mathcal V(\lambda_0I-A)
\subseteq
\mathbb C^n(\lambda_0I-A),
\]

we obtain
\[
\pi(\mathcal V)
\subseteq
\pi\bigl(\mathbb C^n(\lambda_0I-A)\bigr),
\]

and hence
\[
\boxed{\rho\le r(\lambda_0).}
\]

Consequently,
\[
\boxed{
\rho>\min_{\lambda\in\mathbb C}r(\lambda)
\Longrightarrow
\text{the layer is infeasible}.
}
\]

The condition is necessary, not sufficient.

There is no reason to expect the converse: the rank barrier sees only the ambient image of \(\lambda I-A\), not the additional constraints imposed by the fixed rows and the invariance condition.

Suggested improvement: State explicitly that the barrier is a necessary condition for feasibility, and never use it as a sufficient criterion without another theorem.

5. H.1 — Quotient equivalence (Theorem Q)
成立
The equivalence is
\[
\operatorname{rank}
\bigl[(\lambda I-A)V\mid Z\bigr]
=
\dim(V+Z)
\]

if and only if
\[
\operatorname{rank}[U\mid P(\lambda)]
=
r+t.
\]

The decisive hypothesis is
\[
A(S)\subseteq Z,
\qquad S=Z\cap V.
\]

This ensures that the induced pencil on the quotient is well-defined.

Importantly, this hypothesis is not independent of the observer conditions.

Under (5a), for \(x\in S\),
\[
Lx=0,\qquad Cx=0,\qquad CAx=0.
\]

Since
\[
\operatorname{row}(LA)
\subseteq
\operatorname{row}[L;CA;C],
\]

we obtain
\[
LAx=0.
\]

Also,
\[
CAx=0.
\]

Therefore
\[
Ax\in\ker[C;L]=Z.
\]

Thus
\[
\boxed{(5a)\Longrightarrow A(S)\subseteq Z.}
\]

Theorem Q is therefore valid in the observer setting.

However, the condition should remain an explicit hypothesis in the standalone theorem. Otherwise the induced quotient operator may not exist.

A particularly important point: the matrix \([U\mid P(\lambda)]\) need not be square in general. The square condition is associated with
\[
q=t,
\]

not with the general equivalence itself.

This distinction is important for the later determinantal-divisor arguments. 
REPORT_FOR_EXPERT_2026-11-01_EN.md


II. Second tier: Pencil and structural theorems
1. B.1 — Quotient pencil
成立
The statement
\[
(5b)
\iff
\operatorname{rank}Q_{\mathcal V}(\lambda)=\rho
\quad\forall\lambda
\]

is correct under (5a).

Indeed, the quotient rank of the full pencil is
\[
\operatorname{rank}Q_{\mathcal L}(\lambda)
=
j+
\operatorname{rank}Q_{\mathcal V}(\lambda),
\]

where
\[
j=\dim\mathcal J.
\]

Also,
\[
h=j+\rho.
\]

Thus
\[
\operatorname{rank}Q_{\mathcal L}(\lambda)=h
\]

is equivalent to
\[
\operatorname{rank}Q_{\mathcal V}(\lambda)=\rho.
\]

The equivalence is pointwise in \(\lambda\).

In particular, it remains valid at values where the quotient pencil might otherwise be suspected of degenerating. Such degenerations are precisely what the condition detects.

No additional assumption concerning \(q=t\) is needed.

2. B.2 — Top-layer PBH equivalence
成立
The top-layer condition
\[
\rho=d
\]

is essential to the particular block representation used in the proof.

The reduction to observability of
\[
(D_W^{\mathsf T},T_W)
\]

is consistent with the PBH theorem.

The important distinction is that the result is a statement about the top layer. It should not be extended to lower layers simply by retaining the same block notation.

Regarding degenerate cases:
- If the relevant state space has dimension zero, observability is vacuous under the usual convention.
- If the observation block has zero rows, the PBH condition must be interpreted directly rather than inferred from a generic block calculation.
- The block assembly must preserve the actual dimensions of the quotient spaces.
I see no mathematical reason that the result should require diagonalizability.

Suggested improvement: Include a short separate paragraph for the zero-dimensional case rather than leaving it implicit in the PBH argument.

The project’s November 1 report appropriately identifies the remaining work as the assembly of the block identity, not a new PBH theorem. 
REPORT_2026-11-01_EN.md


3. B.3 — The \(\rho=0\) layer
成立
The equivalence
\[
\rho=0
\iff
\mathcal V\subseteq\mathcal J
\]

is immediate from the definition of the quotient map.

When \(\mathcal V\subseteq\mathcal J\), condition (5a) reduces to
\[
\mathcal VA\subseteq\mathcal J.
\]

Equivalently, using the notation of the checklist,
\[
\mathcal V\subseteq\mathcal J,
\qquad
\mathcal VA\subseteq\mathcal J.
\]

Once this condition holds, the first block of the quotient pencil is zero. Consequently, the quotient pencil has rank zero, and (5b) is automatic.

The question about
\[
L_0\ne0
\]

has a straightforward answer:

This assumption is not needed for the \(\rho=0\) equivalence itself.

It may be part of the global observer-design assumptions, but it is not used in this particular argument.

4. B.4 — Full-space feasibility
有缺口
This is the first definite correction I would request.

The checklist states that
\[
\mathcal V=\mathbb C^n
\]

satisfies (5b) if and only if \(A^{\mathsf T}\) has no eigenvector in
\[
K=\ker[C;CA].
\]

Under the project's standard convention, this is not the correct eigenvector formulation.

The pencil is
\[
Q_{\mathcal L}(\lambda)
=
\begin{bmatrix}
\lambda\mathcal L-\mathcal LA\\
CA\\
C
\end{bmatrix}.
\]

Suppose
\[
x\in\ker[C;CA].
\]

Then
\[
C(\lambda I-A)x
=
\lambda Cx-CAx
=
0.
\]

Because \([C;\mathcal L]\) has full row rank and \(\mathcal L\) complements \(C\), the pencil loses rank precisely when there exists a nonzero \(x\) satisfying
\[
Cx=0,\qquad CAx=0,\qquad
(\lambda I-A)x=0.
\]

Thus the obstruction is
\[
\boxed{
\ker[C;CA]\cap\ker(\lambda I-A)\ne\{0\}.
}
\]

That is, a right eigenvector of \(A\) lies in \(K\).

It is not, under these definitions, an eigenvector of \(A^{\mathsf T}\).

The distinction is fundamental:
\[
Ax=\lambda x
\]

is a right-eigenvector equation, whereas
\[
A^{\mathsf T}y=\lambda y
\]

is a different equation on the dual space.
Required correction
Replace the current statement by
\[
\boxed{
(5b)
\iff
\text{\(A\) has no eigenvector in }\ker[C;CA].
}
\]

If the original authors intended a dual formulation, they must explicitly redefine the subspace and the action of the operator.

This is not a matter of diagonalizability. It is a matter of using the correct side of the matrix.

5. B.6 — All right minimal indices are zero
成立
This proposition is correct.

Under (5a),
\[
LA=X L+Y_1CA+Y_2C
\]

for suitable matrices \(X,Y_1,Y_2\).

Let
\[
v(\lambda)=\sum_{k=0}^d\lambda^kv_k
\]

satisfy
\[
Q_L(\lambda)v(\lambda)=0.
\]

Expanding gives
\[
(\lambda L-LA)v(\lambda)=0,
\]

together with
\[
CAv(\lambda)=0,\qquad Cv(\lambda)=0.
\]

The highest-degree coefficient gives
\[
Lv_d=0.
\]

The other two equations give
\[
CAv_d=0,\qquad Cv_d=0.
\]

Consequently,
\[
LAv_d=0
\]

by the factorization of \(LA\).

Thus \(v_d\) is itself a constant polynomial null vector.

Subtracting
\[
\lambda^dv_d
\]

from \(v(\lambda)\) lowers the degree, and induction gives the result.

Therefore the polynomial right null module is generated by constant vectors.

This is stronger than merely saying that every right minimal index is zero.

The distinction asked in the checklist is important:
- Having one constant null vector is not enough.
- Having a constant basis of the entire polynomial null module is enough.
Here the proof establishes the stronger statement.

No use of (5b) is necessary.

6. B.8 — Smith criterion
成立
The statement
\[
(5b)\iff d_{\mathrm{fin}}=0
\]

is correct for rectangular polynomial pencils, provided that the Smith invariants are defined using the normal rank.

Let
\[
Q(\lambda)\in\mathbb C[\lambda]^{m\times n}
\]

have normal rank \(h\).

Its Smith form has \(h\) nonzero invariant factors
\[
d_1(\lambda)\mid d_2(\lambda)
\mid\cdots\mid d_h(\lambda).
\]

The \(h\)-th determinantal divisor is
\[
\Delta_h(\lambda)
=
d_1(\lambda)\cdots d_h(\lambda),
\]

up to a nonzero constant factor.

The pencil loses rank at a finite value \(\lambda_0\) exactly when
\[
\Delta_h(\lambda_0)=0.
\]

Therefore constant rank over all complex values is equivalent to \(\Delta_h\) being a nonzero constant.

This is equivalent to every nonzero invariant factor being a unit, which is precisely the absence of finite elementary divisors.

Hence
\[
\boxed{
(5b)\iff d_{\mathrm{fin}}=0.
}
\]

The rectangular case
Your question about \(q\ne t\) is important.

The argument does not require the pencil to be square.

However, the correct determinantal divisor is
\[
\boxed{\Delta_h,}
\]

where \(h\) is the normal rank.

It is not automatically correct to use an arbitrary \(b\)-th determinantal divisor unless
\[
b=h.
\]

Thus the rectangular formulation is valid, with the normal-rank qualification.

Recommended proof direction: State the Smith normal form first, then derive the determinantal-divisor criterion. This is cleaner than beginning with a square determinant.

7. B.9 — Necessary condition \(h<q+r_1\)
成立
The count is correct.

The pencil has
\[
q+2p
\]

rows and normal rank \(h\).

Its number of left minimal indices is therefore
\[
q+2p-h.
\]

The constant dependencies among the rows of \([CA;C]\) account for
\[
2p-r_1
\]

zero left minimal indices.

Thus the number of nonzero left minimal indices is
\[
(q+2p-h)-(2p-r_1)
=
q+r_1-h.
\]

Under (5b), B.8 gives
\[
\sum_i\varepsilon_i=q.
\]

If \(q>0\), at least one left minimal index must be nonzero.

Consequently,
\[
q+r_1-h>0,
\]

which yields
\[
\boxed{h<q+r_1.}
\]

Is \(L_0\ne0\) the unique sufficient condition?
No.

The essential condition in this deduction is
\[
q>0.
\]

The assumption \(L_0\ne0\), together with
\[
\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L,
\]

is one way to guarantee \(q\ge1\).

It is not the only possible way.

The theorem can therefore be stated more generally with \(q\ge1\) as its explicit hypothesis.

8. B.10 — Spectral obstruction
成立
The factorization
\[
Q_{\mathcal L}(\lambda)=D(\lambda)H
\]

is correct under the assumed relation
\[
LA=\Lambda L+G_0C+G_1CA.
\]

Here
\[
D(\lambda)=
\begin{pmatrix}
\lambda I-\Lambda&-G_1&-G_0\\
0&I&0\\
0&0&I
\end{pmatrix}.
\]

When
\[
\lambda\notin\operatorname{spec}\Lambda,
\]

the matrix \(D(\lambda)\) is invertible.

Therefore
\[
\operatorname{rank}Q_{\mathcal L}(\lambda)
=
\operatorname{rank}H
=
h.
\]

No diagonalizability assumption is involved.

The determinant of the block-triangular matrix is
\[
\det D(\lambda)=\det(\lambda I-\Lambda).
\]

Invertibility depends only on whether \(\lambda\) belongs to the spectrum, not on whether \(\Lambda\) is diagonalizable.

Thus the claimed domain of possible spectral rank drops is correct.

9. B.11 — Geometric formula for \(h\)
成立
The identity
\[
h=\dim(\mathcal Z^\perp+W)
\]

is correct.

Since
\[
\mathcal Z^\perp
=
\operatorname{row}[C;\mathcal L],
\]

and
\[
W=\operatorname{row}[C;CA],
\]

we have
\[
h
=
\dim\mathcal Z^\perp+\dim W
-
\dim(\mathcal Z^\perp\cap W).
\]

Using
\[
\dim\mathcal Z^\perp=p+q,
\qquad
\dim W=r_1,
\]

we obtain
\[
h
=
q+r_1-
\left(\dim(\mathcal Z^\perp\cap W)-p\right).
\]

Therefore, with
\[
\delta=
\dim(\mathcal Z^\perp\cap W)-p,
\]

we get
\[
\boxed{h=q+r_1-\delta.}
\]

Since \(C\) is contained in the intersection,
\[
\delta\ge0.
\]

The formula is valid.
About the \(p=r=1\) geometric classification
The Type I/non-Type-I dichotomy is exhaustive as a numerical classification.

However, it does not necessarily classify every possible relative position of the subspaces.

For \(p=r=1\), one should distinguish:
- \(L_0\) lying in \(W\);
- \(L_0\) outside \(W\);
- the additional intersection of \(R=\operatorname{row}\mathcal L\) with \(W\);
- the resulting value of \(\delta\).
These are finer geometric configurations.

I would therefore avoid claiming that the binary Type I classification exhausts all geometric types unless those types have been explicitly defined.

III. Third tier: Special layers and auxiliary results
1. C.1 — Closure family
成立
Suppose
\[
\operatorname{row}(L_0)=\mathcal J
\]

and
\[
\langle\mathcal J\rangle_A=\mathbb C^n.
\]

Every admissible candidate satisfies
\[
\mathcal J\subseteq\mathcal V.
\]

Condition (5a) gives
\[
\mathcal VA\subseteq\mathcal V+\mathcal J.
\]

But \(\mathcal J\subseteq\mathcal V\), so
\[
\mathcal VA\subseteq\mathcal V.
\]

Thus \(\mathcal V\) is an \(A\)-invariant subspace containing \(\mathcal J\).

It must therefore contain the entire \(A\)-closure of \(\mathcal J\).

By hypothesis,
\[
\mathcal V=\mathbb C^n.
\]

Hence
\[
q_{\min}=n.
\]

For (5b), the full-space condition reduces to the absence of an eigenvector in \(\ker C\), which follows from observability of \((C,A)\).

The argument works for \(r\ge2\) as well.

No scalar-output assumption is required for this closure argument.

2. B.13 — Incidence variety and whole-family infeasibility
有缺口
This is the third item I would request that you revise before treating it as a finished theorem.

The proposed incidence construction is
\[
\mathfrak I
\subseteq
\mathbb P(V)\times\mathbb P^1\times\mathbb P(K),
\]

with the intended relation
\[
z=(\lambda I-A)x.
\]

There is a projective-geometric problem here.

The expression
\[
(\lambda I-A)x
\]

is affine in \(\lambda\), whereas \(\lambda\) is being treated as a projective coordinate in \(\mathbb P^1\).

At the point at infinity, this expression is not defined in the stated form.
Required correction: homogeneous pencil
Write the projective parameter as
\[
[\alpha:\beta]\in\mathbb P^1
\]

and replace the relation by
\[
z=(\alpha I-\beta A)x,
\]

interpreted projectively:
\[
[z]=[(\alpha I-\beta A)x].
\]

The zero case must be excluded.

This gives a genuinely projective formulation.
Second issue: projection and dimension
The conditions
\[
L_0x\ne0,\qquad
(\alpha I-\beta A)x\ne0
\]

define open restrictions.

Consequently, the resulting incidence set need not be closed in the ambient projective product.

The projection of a projective closed variety is closed, but that conclusion cannot automatically be applied after removing open subsets.

One must distinguish:
- the closure of the incidence variety;
- the actual constructible incidence set;
- its projection;
- the dimension of its fibers.
A dimension count alone does not establish that the projected bad set covers the entire Grassmannian.
Recommended direction
Use a homogeneous incidence variety first, prove its dimension bounds, and then handle the excluded loci separately.

In particular, formulate the covering argument using the constructible image and a fiber-dimension estimate, rather than assuming that the image is automatically closed.

The single-\(\lambda\) certificate B.13e is a much cleaner route for the special case where
\[
\dim V=\dim K,\qquad
(\lambda_0I-A)V=K,\qquad
V\cap K=0.
\]

That argument should remain separate from the more general incidence-variety theorem.

My recommendation: Repair the projective incidence formulation before investing in further dimension-counting refinements.

3. B.14 — Polynomial-time tractable class
成立
The condition is
\[
\operatorname{rank}
\bigl(P_K(\lambda I-A)B_V\bigr)
=
\dim V
\qquad\forall\lambda.
\]

Under this condition, suppose (5b) fails.

Then B.13c gives
\[
x\in V\setminus Z
\]

such that
\[
(\lambda I-A)x\in Z\subseteq K.
\]

Consequently,
\[
P_K(\lambda I-A)x=0.
\]

Since \(B_V\) spans \(V\), the full-column-rank condition forces
\[
x=0,
\]

a contradiction.

Thus the sufficient condition is valid.
Does it depend on the choice of basis?
No.

If \(B_V'\) is another basis matrix of \(V\), then
\[
B_V'=B_VR
\]

for an invertible matrix \(R\).

Therefore
\[
\operatorname{rank}
\bigl(P_K(\lambda I-A)B_V'\bigr)
=
\operatorname{rank}
\bigl(P_K(\lambda I-A)B_V\bigr).
\]

Similarly, any two full-row-rank matrices with the same kernel \(K\) differ by an invertible change of coordinates in the codomain.

Hence (T*) is intrinsic.

Important limitation: The failure of (T*) does not imply failure of (5b). This is a sufficient criterion, not a necessary one. Your checklist correctly records this distinction.

4. B.15 — Unbounded order gap
成立
The direct-sum argument is correct under the stated assumptions.

For \(k\) identical copies,
\[
V=V_1^{\oplus k},
\qquad
K=K_1^{\oplus k}.
\]

Moreover,
\[
V\cap K=0
\]

and, using the same spectral parameter,
\[
(\lambda_0I-A)V=K.
\]

The fact that the same \(\lambda_0\) works in every block is essential.

For any nonzero admissible \(Z\subseteq K\), the single-\(\lambda\) certificate gives a rank drop at \(\lambda_0\).

Thus all orders with
\[
d=n-p-q\ge1
\]

are excluded.

At \(d=0\), the block-diagonal augmentation
\[
\mathcal L=\mathcal L_1^{\oplus k}
\]

is feasible.

Since ranks add under direct sums, the upper-bound construction works.

Therefore the gap scales linearly:
\[
\boxed{\text{gap}_k=k\,\text{gap}_1.}
\]

The hypotheses \(V_1\cap K_1=0\) and the surjectivity condition are sufficient for the avoidance argument.
About the finite-union argument
Over \(\mathbb C\), a finite union of proper Zariski-closed subsets cannot cover an irreducible Grassmannian.

Thus, if the exceptional configurations are genuinely proper algebraic subsets, it is enough to establish that their complement is a nonempty Zariski-open set.

You do not need a stronger notion of thinness.

Be careful, however, to prove that each exceptional set is algebraic and proper, rather than merely having failed to appear in a finite computation.

5. B.16 — Stratification by \(\operatorname{rank}(J_Z|_V)\)
成立
This is a sound structural result.

Since
\[
\ker J_Z=S,
\]

we have
\[
\operatorname{rank}(J_Z|_V)
=
\dim V-\dim S.
\]

The three cases are correctly distinguished.

Case 1: \(s=0\).

Then \(J_Z\) is injective on \(V\).

Failure is equivalent to
\[
\exists\lambda:
\operatorname{rank}N_Z(\lambda)<\dim V.
\]

This is equivalent to the maximal minors having a common complex root.

Case 2: \(s=\dim V\).

Then
\[
V\subseteq Z.
\]

There is no \(x\in V\setminus Z\), so the failure criterion is impossible.

Thus (5b) holds.

Case 3: \(0<s<\dim V\).

The correct criterion is
\[
\boxed{
\text{Failure}
\iff
\exists\lambda:
\ker N_Z(\lambda)\not\subseteq S.
}
\]

This is the essential correction.

One must not use full-column-rank of \(N_Z(\lambda)\) in this case, because \(S\) is already a permanent kernel.

The project has also correctly identified that intermediate strata can fail. Thus the three-way stratification is not a proof that the middle stratum is automatically feasible.
Is the intermediate criterion decidable?
There are two different questions.

For a fixed \(Z\), the condition is algebraically decidable through polynomial minors or an appropriate quotient-pencil representation.

For the existential layer problem, where \(Z\) itself varies, one still has a semialgebraic feasibility problem.

Thus the criterion is a valid reduction, but it does not by itself provide a polynomial-time algorithm.

The distinction is important for the complexity question. 
15_stratification.md


6. B.17 — Permanent kernel and quotient-pencil criterion
成立
The permanent-kernel statement follows directly from (5a).

Let
\[
S=V\cap Z.
\]

As established earlier,
\[
(5a)\Longrightarrow A(S)\subseteq Z.
\]

For every \(x\in S\),
\[
J_Zx=0
\]

and
\[
T_Zx=Ax+Z=0.
\]

Therefore
\[
N_Z(\lambda)x=0
\]

for every \(\lambda\).

Hence
\[
\boxed{
S\subseteq\ker N_Z(\lambda)
\quad\forall\lambda.
}
\]

The converse part of the quotient criterion follows from the exact failure criterion:
\[
(5b)\text{ fails}
\iff
\exists\lambda,\ \exists x\in V\setminus Z:
N_Z(\lambda)x=0.
\]

Since \(V\setminus Z\) is precisely the set of vectors outside \(S\),
\[
(5b)
\iff
\ker N_Z(\lambda)=S
\quad\forall\lambda.
\]

Equivalently, the induced map
\[
\overline N_Z(\lambda):V/S\to X/Z
\]

is injective for every \(\lambda\).

No additional use of (5b) is needed to establish the permanent kernel.

The question in the checklist has a clear answer: the permanent kernel follows from (5a) alone.

7. B.21 — Right nullspace and minimal indices
成立
Both claims are correct.

First,
\[
S=V\cap Z.
\]

Since
\[
S=V\cap Z
=
W^\perp\cap Z,
\]

where
\[
W=\operatorname{row}[C;CA],
\]

we obtain
\[
S^\perp=W+Z^\perp.
\]

Therefore
\[
\begin{aligned}
s
&=n-\dim S^\perp\\
&=n-\dim(W+Z^\perp)\\
&=n-h.
\end{aligned}
\]

Hence
\[
\boxed{s=n-h.}
\]

For the polynomial nullspace, let
\[
x(\lambda)\in\mathbb C[\lambda]^n
\]

satisfy
\[
Q_L(\lambda)x(\lambda)=0.
\]

The \(C\)- and \(CA\)-blocks force every coefficient of \(x(\lambda)\) to belong to \(V\).

Using the factorization supplied by (5a),
\[
LA=\Lambda L+G_0C+G_1CA,
\]

the first block, restricted to \(V\), becomes
\[
(\lambda I-\Lambda)Lx(\lambda)=0.
\]

Since \(\lambda I-\Lambda\) is invertible over \(\mathbb C(\lambda)\),
\[
Lx(\lambda)=0.
\]

Therefore every coefficient belongs to
\[
V\cap\ker L=S.
\]

Conversely, every polynomial vector with coefficients in \(S\) belongs to the nullspace because
\[
A(S)\subseteq Z.
\]

Thus
\[
\boxed{
\ker_{\mathbb C[\lambda]}Q_L(\lambda)
=
S\otimes\mathbb C[\lambda].
}
\]

The right minimal indices are all zero.
Does this require \(q\ge1\)?
No.

The argument does not require \(q\ge1\).

If \(S=0\), the right null module is zero and there are no right minimal indices. The sum of their degrees is interpreted as zero.

If \(S\ne0\), the module has a constant basis, again giving zero minimal indices.

The statement should therefore not impose \(q\ge1\) for this particular conclusion.

The earlier equality report contains the corresponding full null-module argument. 
18_equality_and_entries.md


8. B.23 — Uniform factorization
成立
The factorization is correct:
\[
Q_L(\lambda)=P(\lambda)H_0,
\]

where
\[
H_0=
\begin{bmatrix}
L\\B
\end{bmatrix},
\]

and
\[
P(\lambda)=
\begin{pmatrix}
\lambda I_q-K_1&-K_2\\
0&I_{r_1}
\end{pmatrix}.
\]

Indeed, since
\[
LA=K_1L+K_2B,
\]

we have
\[
\lambda L-LA
=
(\lambda I_q-K_1)L-K_2B.
\]

The lower block is simply \(B\), so block multiplication gives the desired identity.

Now \(P(\lambda)\) is block triangular.

Consequently,
\[
\boxed{
\det P(\lambda)
=
\det(\lambda I_q-K_1).
}
\]

No special structure of \(K_1\) is required.

In particular:
- \(K_1\) need not be diagonalizable.
- \(K_1\) need not be invertible.
- Its eigenvalues may have arbitrary algebraic multiplicities.
- The determinant identity is independent of the choice of eigenbasis.
The important hypothesis is the factorization of \(LA\), which follows from (5a).

Suggested improvement: State the factorization and determinant identity separately. The second is simply a consequence of block triangularity.

9. B.24 — Intrinsic partial operator
成立
The definition is
\[
\Phi:W\to\mathbb C^q,
\qquad
\Phi(Lx)=LAx,\quad x\in V,
\]

where
\[
W=LV.
\]

The well-definedness proof is correct.

Suppose
\[
Lx_1=Lx_2.
\]

Then
\[
s=x_1-x_2\in V\cap\ker L=S.
\]

By (5a),
\[
LA s=0.
\]

Therefore
\[
LAx_1=LAx_2.
\]

Thus \(\Phi\) is well-defined.
Does this require \(L\) to have full row rank?
No.

Full row rank is not needed for well-definedness.

The essential conditions are:
1. \(x_1,x_2\in V\);
2. \(Lx_1=Lx_2\);
3. (5a).
The full-row-rank assumption may be needed elsewhere in the observer-design problem, but not for the construction of \(\Phi\).
The eigenvector equivalence
Using B.23,
\[
LAx=K_1Lx
\qquad (x\in V),
\]

because \(Bx=0\).

Hence
\[
\Phi(w)=K_1w,
\qquad w\in W.
\]

Therefore
\[
\Phi(w)=\lambda w
\]

is equivalent to
\[
K_1w=\lambda w.
\]

The failure of (5b) is consequently equivalent to the existence of a nonzero eigenvector of \(K_1\) lying in \(W\).

This is an excellent intrinsic reformulation.

It also explains why the partial operator is more natural than introducing an arbitrary full-space extension \(\Lambda\).

The result should be retained.
19_spectral_pair_and_class_I.md

10. K.1 — Decomposable bivectors
成立
Both parts are correct over \(\mathbb C\).
Case \(m=3\)
Every nonzero element of
\[
\Lambda^2\mathbb C^3
\]

is decomposable.

One way to see this is
\[
\dim\Lambda^2\mathbb C^3=3,
\]

and the Plücker embedding identifies
\[
\operatorname{Gr}(2,3)
=
\mathbb P(\Lambda^2\mathbb C^3).
\]

Thus every projective bivector corresponds to a two-dimensional subspace.
Case \(m=4\), \(\ell\ge2\)
The restriction of the Klein quadratic form to \(K\) is a quadratic form on a vector space of dimension at least two.

Over an algebraically closed field, every homogeneous quadratic form in at least two variables has a nonzero isotropic vector.

Therefore there exists
\[
0\ne w\in K
\]

such that
\[
q(w)=0.
\]

By the Klein-quadric criterion, \(w\) is decomposable.

No nondegeneracy assumption is necessary.

This is worth emphasizing: a degenerate quadratic form is also isotropic in dimension at least two over \(\mathbb C\).

For \(\ell=1\), the condition reduces to evaluating the quadratic form at the unique projective point represented by \(p_0\):
\[
q(p_0)=0.
\]

The statement is correct.

The proof should, however, explicitly state the Plücker/Klein-quadric equivalence being used. The quadratic-form isotropy lemma alone does not establish decomposability without that bridge.


IV. Consolidated verdict
The following table collects all 24 judgments.
Tier	Proposition	Verdict
I	A.1	成立
I	D.1	需要额外假设
I	G.1	成立
I	F.1	成立
I	H.1	成立
II	B.1	成立
II	B.2	成立
II	B.3	成立
II	B.4	有缺口
II	B.6	成立
II	B.8	成立
II	B.9	成立
II	B.10	成立
II	B.11	成立
III	C.1	成立
III	B.13	有缺口
III	B.14	成立
III	B.15	成立
III	B.16	成立
III	B.17	成立
III	B.21	成立
III	B.23	成立
III	B.24	成立
III	K.1	成立

Overall assessment
21
成立

2
有缺口

1
需额外假设



The main mathematical structure survives this review. The three items requiring revision are D.1, B.4 and B.13.

V. Recommended order of revision
I would not revise all the propositions simultaneously. The most efficient approach is to settle the foundational defects first.
Priority 1: B.4 — Correct the eigenvector formulation
This is the simplest correction.

Replace the \(A^{\mathsf T}\)-eigenvector formulation with the right-eigenvector condition for \(A\), unless the original proof explicitly uses a different dual-space convention.

Then check that the Lean statement agrees with the corrected mathematical statement.

This should be a relatively inexpensive correction.
Priority 2: D.1 — Make the recursion rigorous
This is more important mathematically.

I recommend producing a completely self-contained proof containing:
1. The precise definition of \(P(A,B,S)\).
2. The feasible family over which the minimum is taken.
3. The empty-family convention.
4. The definition of \(\Phi'\).
5. The proof that \(\Phi'\) is well-defined.
6. The proof of the one-step recursive identity.
7. The deduction of the lower bound.
In particular, I would not accept a proof that silently assumes the relevant quotient is invariant under \(A\).

The November 1 report itself records the distinction between the Lean-checked recursive core and the still-paper-level range-inclusion argument. 
REPORT_2026-11-01_EN.md

Priority 3: B.13 — Repair the incidence construction
This is the most technically interesting of the three.

The correct projective construction should use
\[
[\alpha:\beta]\in\mathbb P^1
\]

and the homogeneous pencil
\[
\alpha I-\beta A.
\]

Then establish the dimension of the incidence variety and its projection carefully.

I would separate the proof into three lemmas:
- Incidence lemma: The homogeneous incidence set is a constructible algebraic set with the claimed dimension bound.
- Fiber lemma: The dimension of the fibers of the projection is bounded as required.
- Coverage lemma: The projected bad set covers the desired Grassmannian under the stated dimension hypotheses.
This decomposition will make the argument substantially easier to audit.
Priority 4: Clarify the remaining propositions
These are not reasons to reject the propositions, but the paper should make the qualifications explicit.
Proposition	Revision
A.1	Separate quotient equivalence from lower-bound attainability.
G.1	Explicitly justify the polynomial left-inverse degree bound and realification.
F.1	Emphasize necessity, not sufficiency.
H.1	Retain \(A(S)\subseteq Z\) as an explicit hypothesis.
B.3	Remove unnecessary dependence on \(L_0\ne0\).
B.8	Specify that the determinantal divisor is \(\Delta_h\), with \(h\) the normal rank.
B.9	Use \(q\ge1\) as the actual essential assumption.
B.11	Distinguish the binary Type I classification from finer geometric configurations.
B.16	Emphasize that intermediate strata remain genuine spectral feasibility problems.
B.21	Do not impose \(q\ge1\) unnecessarily.
B.23	State explicitly that no diagonalizability of \(K_1\) is required.
B.24	Emphasize that full row rank is unnecessary for well-definedness of \(\Phi\).


VI. Broader mathematical observations
There are three aspects of the current project that I consider particularly valuable.
1. The quotient-pencil formulation is becoming a coherent theory
The progression
\[
(5a)
\Longrightarrow
A(S)\subseteq Z
\Longrightarrow
S\subseteq\ker N_Z(\lambda)
\]

and then
\[
(5b)
\iff
\ker N_Z(\lambda)=S
\quad\forall\lambda
\]

is mathematically clean.

It explains why the naive full-column-rank condition fails on intermediate strata and identifies the correct object:
\[
\overline N_Z(\lambda):V/S\longrightarrow X/Z.
\]

This is more than a computational reformulation. It identifies the precise geometric obstruction.
2. The Kronecker structure has a useful simplification
The combination of B.6, B.8, B.9 and B.21 gives a strong structural picture:
- (5a) forces the right minimal indices to vanish.
- The remaining polynomial freedom is concentrated on the left side and the elementary divisors.
- The finite elementary divisors characterize the spectral rank-drop obstruction.
- The number of nonzero left minimal indices is controlled by \(q+r_1-h\).
This substantially reduces the structural complexity of the observer pencil.

The important point is that the simplification is specific to observer pencils satisfying (5a). It should not be generalized to arbitrary matrix pencils.
3. The complexity problem remains genuinely open
Even after all the structural reductions, the central problem is still
\[
\exists Z\subseteq K,\qquad
\dim Z=d,
\]

subject to
\[
A(Z\cap V)\subseteq Z
\]

and the pointwise spectral condition.

The structural results make this problem much more explicit, but they do not yet eliminate the existential choice of \(Z\).

I would therefore avoid presenting the current results as a polynomial-time solution of the original problem.

The \(\exists\mathbb R\) upper bound is a meaningful complexity result, but membership and hardness are different questions.

VII. My recommendation for the next research round
I recommend the following order:
1. Correct B.4.
2. Complete the D.1 recursion proof.
3. Repair B.13's projective incidence construction.
4. Consolidate B.16, B.17 and B.21 into one unified quotient-pencil theorem.
5. Use B.23 and B.24 to develop a more intrinsic spectral characterization.
6. Return to the complexity question only after these structural statements have been stabilized.
In particular, I would prioritize the combination
\[
\boxed{\text{B.17}+\text{B.21}+\text{B.23}+\text{B.24}.}
\]

These results appear to provide the most promising foundation for a unified description of the spectral obstruction.

Final judgment: I would retain 21 propositions in the current mathematical inventory, revise B.4 and B.13, and withhold unconditional acceptance of D.1 until its quotient recursion and empty-feasibility convention are settled. There is no reason to discard the overall research direction on the basis of this review.

For the next round, the most productive step would be to send me the complete D.1 and B.13 proof dossiers. I can then examine the individual algebraic and geometric steps, rather than merely the summarized statements in the checklist.