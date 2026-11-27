# Mathematical assessment of Report 61: solver, \\(c=1\\) infeasibility, and the two all-\\(q\\) obstructions

The report contains several substantial structural results. In particular, it identifies a potentially decisive distinction between full row rank of \\(L\\) and row independence of \\(L\\) modulo \\(C\\). It also gives a promising \\(c=1\\) obstruction and a clean determinant argument for \\(c=0\\).

My overall assessment is:

1. The \\(c=0\\) determinant obstruction is correct, under the stated square full-rank hypotheses.
2. The \\(c=1\\) hyperplane argument is correct in its essential linear-algebraic step, but the report should make the row-space and coordinate identifications explicit. The eigenline calculations establish only the stated cases; the identically-zero eigenline equation is a separate case and cannot be dismissed by the same argument.
3. The \\(c=2\\) all-\\(q\\) obstruction is valid under the convention \\(\operatorname{rank}[C;L]=p+q\\), provided the reported row-wise certificates are exact and the dimensions and hypotheses are verified.
4. The conclusion that the two instances are infeasible for every \\(q\\) is not yet a conclusion about the original observer problem until the convention is checked. This is the most important issue in the report.
5. The solver is a useful exact stratified search and witness-verification framework, but it is not yet a complete decision procedure as written. The lift conditions, exact rank constraints, and treatment of all strata need to be incorporated explicitly.

I will examine the points in that order, then give a recommended sequence of work.

## 1. The convention is the first issue to resolve

The report imposes both

\\[ \operatorname{rank}L=q \\]

and

\\[ \operatorname{rank}\begin{bmatrix}C\\\L\end{bmatrix}=p+q. \tag{1.1} \\]

The second condition says that the rows of \\(L\\) are linearly independent modulo \\(\operatorname{row}C\\). It is strictly stronger than requiring \\(L\\) itself to have full row rank.

Indeed, if

\\[ \operatorname{rank}C=p_0\<p, \\]

then even the equality on the right of (1.1) is impossible, because

\\[ \operatorname{rank}\begin{bmatrix}C\\\L\end{bmatrix} \le p_0+q\<p+q. \\]

Thus the convention implicitly requires \\(C\\) to have full row rank \\(p\\), unless the project has already assumed that.

More importantly, the second condition is not a harmless normalization. It can change feasibility and minimum order. A row of \\(L\\) that lies in \\(\operatorname{row}C\\) may be redundant as an independent output row, but it can still affect the prescribed form \\(L=[L_0;R]\\), the dimension \\(q\\), and the relation between \\(L\\) and the output map. Whether such rows should be excluded is a matter of the original observer definition, not something that can be settled by the compressed rank equations alone.

### 1.1 What changes if only \\(\operatorname{rank}L=q\\) is required?

The key implication in the report is

\\[ V=\ker H\subseteq W_L, \qquad W_L=\ker[L_0N;L_0AN]. \tag{1.2} \\]

This implication follows from (5a) and the fact that the first \\(r\\) rows of \\(H\\) and \\(H_A\\) are fixed. It does not follow from the independence condition (1.1).

To see the distinction, write

\\[ H=\begin{bmatrix}H_0\\\H_R\end{bmatrix}, \qquad H_A=\begin{bmatrix}H\_{A,0}\\\H\_{A,R}\end{bmatrix}, \\]

where

\\[ H_0=L_0N,\qquad H\_{A,0}=L_0AN. \\]

The condition (5a) implies

\\[ \ker H\subseteq\ker H_A. \\]

Consequently, if \\(v\in V=\ker H\\), then

\\[ H_0v=0,\qquad H\_{A,0}v=0, \\]

so \\(v\in W_L\\). Therefore (1.2) is forced by (5a), independently of whether \\([C;L]\\) has full row rank.

This is an important point: removing the independence-modulo-\\(C\\) condition does not, by itself, invalidate \\(V\subseteq W_L\\).

However, the dimension argument

\\[ \dim W_L=c\quad\Longrightarrow\quad V=W_L \tag{1.3} \\]

also does not require independence modulo \\(C\\). It follows simply because \\(V\subseteq W_L\\) and both have dimension \\(c\\).

What does change is the lifting problem. Under the stronger convention, the actual rows of \\(L\\) must be independent modulo \\(\operatorname{row}C\\). Without that convention, a compressed row-pair may be liftable using rows that are dependent modulo \\(C\\), and the pair-preserving lift-completion inequality from the earlier work is no longer the appropriate necessary-and-sufficient condition.

Thus I would separate the issues as follows:

- The geometric constraints on \\(V\\), \\(W\\), and \\(U\\), derived from (5a), remain in force.
- The rank requirement \\(\operatorname{rank}H=\omega\\) remains in force by definition of the stratum.
- The existence of actual rows of \\(L\\) lifting the compressed data changes.
- The final all-\\(q\\) infeasibility conclusion must be checked under the original lifting convention.

### 1.2 A useful distinction to put into the report

I recommend explicitly defining two problems:

\\[ \mathsf{P}\_{\mathrm{ind}}: \quad \operatorname{rank}L=q,\quad \operatorname{rank}[C;L]=p+q,\quad (5a),(5b), \\]

and

\\[ \mathsf{P}\_{\mathrm{full}}: \quad \operatorname{rank}L=q,\quad (5a),(5b). \\]

Then state every infeasibility result with its scope. The two instances may be infeasible for \\(\mathsf{P}\_{\mathrm{ind}}\\) while feasible for \\(\mathsf{P}\_{\mathrm{full}}\\). There is no contradiction in that possibility.

Recommendation: before spending further effort on the two-instance all-\\(q\\) theorem, recover the original observer definition and settle which of these two problems is actually intended. This is the highest-priority item in Report 61.

## 2. The \\(c=1\\) hyperplane lemma

This is the most interesting new structural result in the report. Its central idea is sound, and it is stronger than a calculation for a particular \\(\omega\\): it applies to arbitrary positive \\(\omega\\), provided the stated hypotheses hold.

Let

\\[ V=\mathbb Cv\subseteq W_L,\qquad W_L\subseteq D:=K_0\cap A^{-1}K_0. \\]

Since \\(v\in W_L\\), we have

\\[ L_0Nv=0,\qquad L_0ANv=0. \\]

Since \\(W_L\subseteq D\\), we also have \\(Av\in K_0\\). Write

\\[ Av=Nw,\qquad w\in\mathbb C^k. \\]

The key observation is that the admissibility condition for each actual row \\(l_i\\) of \\(L\\) becomes

\\[ (l_iAN)v=l_i(ANv)=l_i(Av)=l_iNw=h_iw=0, \\]

where \\(h_i=l_iN\\) is the corresponding row of \\(H\\).

Here the notation \\(h_iw\\) denotes the natural row-column pairing. The argument then becomes entirely a statement about the row space of \\(H\\).

### 2.1 The hyperplane argument is correct

Suppose

\\[ w\notin\operatorname{span}\\{v\\}. \\]

Since \\(V=\mathbb Cv\\), the space of row vectors on \\(\mathbb C^k\\) annihilating \\(V\\) is

\\[ \operatorname{Ann}(V) =\\{h\in(\mathbb C^k)^\*:hv=0\\}, \\]

and has dimension

\\[ k-1=\omega, \\]

because \\(c=1\\) and \\(\omega=k-c\\).

Consider the linear functional

\\[ \epsilon_w:\operatorname{Ann}(V)\longrightarrow\mathbb C, \qquad h\longmapsto hw. \\]

It is nonzero precisely because \\(w\notin V\\). To verify this, if it were zero, every covector annihilating \\(v\\) would also annihilate \\(w\\), which forces \\(w\in\operatorname{span}\\{v\\}\\) by finite-dimensional duality.

Therefore

\\[ \ker\epsilon_w =\\{h\in\operatorname{Ann}(V):hw=0\\} \\]

is a hyperplane of \\(\operatorname{Ann}(V)\\), of dimension \\(\omega-1\\).

Every row \\(h_i\\) of \\(H\\) belongs to this hyperplane:

- \\(h_iv=0\\), because \\(v\in\ker H\\);
- \\(h_iw=0\\), by the admissibility equation above.

Consequently,

\\[ \operatorname{rank}H\le\omega-1, \\]

contradicting the definition of the \\(\omega\\)-stratum.

Thus the following lemma is justified.

Valid under stated hypotheses

\\(c=1\\) hyperplane obstruction. If \\(W_L\subseteq K_0\cap A^{-1}K_0\\), and \\(V=\mathbb Cv\subseteq W_L\\) is admissible, then necessarily

\\[ Av\in\mathbb Cv. \\]

In other words, every admissible one-dimensional kernel \\(V\\) must be an \\(A\\)-invariant line.

This is a useful reduction: under the hypotheses, the \\(c=1\\) stratum has no admissible points except eigenlines of \\(A\\) lying in \\(W_L\\).

One small improvement to the proof is to state explicitly that the \\(h_i\\) all lie in \\(\operatorname{Ann}(V)\\), and that \\(\operatorname{Ann}(V)\\) is being taken in the dual of the \\(k\\)-dimensional compressed coordinate space. That removes a possible ambiguity between covectors on the original state space and covectors on \\(K_0\\).

### 2.2 The eigenline calculations must be treated as a separate finite test

Once the hyperplane lemma has reduced the problem to eigenlines, the remaining task is not to check arbitrary lines in \\(W_L\\). It is to determine

\\[ \mathcal E(W_L) = \\{[v]\in\mathbb P(W_L): Av\in\mathbb Cv\\}. \\]

For each such line, one must then test whether the corresponding admissibility constraints still force the compressed rows into a proper subspace of \\(\operatorname{Ann}(V)\\).

For a two-dimensional \\(W_L\\), this is a projective algebraic calculation. The report gives two examples:

- \\(a(a-b)=0\\), yielding the two lines \\(\mathbb Cw_1\\) and \\(\mathbb C(w_0+w_1)\\);
- \\(2a^2-2ab+b^2=0\\), yielding \\(b/a=1\pm i\\).

The second calculation is correctly treated over \\(\mathbb Q(i)\\), rather than only over \\(\mathbb Q\\). This matters: an eigenline over \\(\mathbb C\\) need not be rational, and a search over rational points would miss it.

For every eigenline, the report then claims that the associated constraint functional

\\[ \varphi=(\varphi_1,\varphi_2) \\]

is nonzero, with \\(\varphi=(1,0)\\) in the complex case. If this is indeed the coordinate representation of the functional

\\[ h\longmapsto hw \\]

on the relevant row-parameter space, then it proves that the admissible rows lie in a proper hyperplane, again contradicting \\(\operatorname{rank}H=\omega\\).

I would nevertheless strengthen the computational certificate. For each eigenline, output:

1. an exact representative \\(v\\);
2. an exact eigenvalue \\(\lambda\\) satisfying \\(Av=\lambda v\\);
3. the exact compressed coordinate \\(w\\) satisfying \\(Av=Nw\\);
4. a basis of \\(\operatorname{Ann}(V)\\);
5. the coordinate vector of \\(h\mapsto hw\\) in that basis;
6. an explicit nonzero coordinate, or an exact row-space identity proving that the functional is nonzero.

This would make the eigenline obstruction independently auditable and would avoid relying on the informal statement that \\(\varphi\ne0\\).

### 2.3 The identically-zero eigenline equation is a genuine exceptional case

The report correctly raises this issue. If the eigenline equation vanishes identically on \\(W_L\\), the preceding eigenline enumeration does not produce a finite list of candidate lines.

There are two cases worth distinguishing.

Case A: \\(\dim W_L\ge2\\). If every nonzero \\(v\in W_L\\) satisfies

\\[ Av\in\mathbb Cv, \\]

then linearity forces a single common eigenvalue:

\\[ A|\_{W_L}=\lambda I\_{W_L}. \\]

Indeed, for independent \\(v_1,v_2\\), write

\\[ Av_1=\lambda_1v_1,\qquad Av_2=\lambda_2v_2. \\]

The fact that \\(v_1+v_2\\) is also an eigenvector forces\
\\(\lambda_1=\lambda_2\\). The same argument applies to every vector in \\(W_L\\).

In this situation the hyperplane lemma gives no contradiction. For every \\(v\in W_L\\),

\\[ w=\lambda v, \\]

so every \\(h\in\operatorname{Ann}(V)\\) automatically satisfies \\(hw=0\\). The second annihilation condition adds no restriction to the row space of \\(H\\).

This does not establish feasibility. It only says that this particular rank-drop argument is silent. One must still check the pencil condition

\\[ \operatorname{rank}(\mu H-H_A)=\omega \quad\text{for every }\mu\in\mathbb C, \\]

the actual row-lift conditions, and the original observer constraints.

Case B: \\(\dim W_L=1\\). There is only one projective line to check. It is automatically the only candidate, and the identically-zero formulation is not a meaningful additional degeneracy: the question is simply whether its generator is an eigenvector and whether the remaining conditions hold.

For the two instances in the report, \\(\dim W_L=2\\) and the displayed eigenline polynomials are nonzero. Thus the exceptional scalar-restriction case does not appear to affect those two calculations. It should nevertheless be recorded as a separate branch in the solver.

### 2.4 Generalisation beyond \\(W_L\subseteq D\\)

The lemma already generalises to arbitrary \\(\omega\\). The more serious restriction is

\\[ W_L\subseteq D=K_0\cap A^{-1}K_0. \\]

This condition ensures that \\(Av\\) can be written as \\(Nw\\), allowing the admissibility equation to be expressed using only the compressed row \\(h_i=l_iN\\).

If \\(Av\notin K_0\\), this step fails. In general,

\\[ l_i(Av) \\]

is not determined by \\(l_iN\\) alone. Two actual row lifts can have the same compressed row \\(l_iN\\) but different values on \\(Av\\). Therefore the argument cannot simply be reused with a projected or truncated \\(w\\).

A sensible generalisation is to split the one-dimensional kernel candidates into two classes:

\\[ \mathcal V\_{\mathrm{in}} = \\{[v]\in\mathbb P(W_L):Av\in K_0\\}, \\]

and

\\[ \mathcal V\_{\mathrm{out}} = \\{[v]\in\mathbb P(W_L):Av\notin K_0\\}. \\]

- On \\(\mathcal V\_{\mathrm{in}}\\), the hyperplane lemma applies.
- On \\(\mathcal V\_{\mathrm{out}}\\), one should retain the full row-lift variables and derive a rank obstruction from the combined constraints on \\(l_iN\\) and \\(l_iAv\\).

This suggests a more general linear-algebraic approach: for each fixed \\(v\\), consider the linear map from the admissible space of actual row lifts to the pair of evaluations

\\[ l\longmapsto (lNv,\ lAv). \\]

The rank of the image of this map, and its relation to the required rank of \\(H\\), may yield a generalized obstruction. But the report does not yet establish such a theorem.

Recommendation: keep the current \\(c=1\\) lemma as a proved conditional result. Do not state a general \\(W_L\not\subseteq D\\) version until the actual row-lift variables have been incorporated.

## 3. The \\(c=0\\) determinant obstruction

This argument is correct and particularly clean.

When

\\[ c=0,\qquad \omega=k=q, \\]

the matrix

\\[ H=LN \\]

is square and has full rank. Thus

\\[ P(\lambda)=\lambda H-H_A =L(\lambda I-A)N \\]

is a \\(k\times k\\) matrix pencil with

\\[ \det P(\lambda) =\lambda^k\det H+\text{terms of lower degree}. \\]

Since \\(\det H\ne0\\), the determinant is a polynomial of degree exactly \\(k\\). For \\(k\ge1\\), the fundamental theorem of algebra gives some \\(\lambda_0\in\mathbb C\\) such that

\\[ \det P(\lambda_0)=0. \\]

Therefore

\\[ \operatorname{rank}P(\lambda_0)\<k=\omega, \\]

contradicting (5b).

Correct

The concern about the determinant being the zero polynomial is resolved by the nonzero leading coefficient. Under the hypotheses \\(H\\) is invertible, so

\\[ \det P(\lambda)\not\equiv0. \\]

Indeed, it is not merely nonzero: it has degree \\(k\\).

There are only two minor qualifications to record:

- The argument uses the field \\(\mathbb C\\), or more generally an algebraically closed field. Over \\(\mathbb R\\), a nonconstant polynomial need not have a real root, so this proof would not establish the same conclusion for real \\(\lambda\\).
- The case \\(k=0\\) is outside the intended positive-order setting. If it is allowed, it must be treated separately rather than invoking a degree-zero determinant polynomial as having a root.

The report's \\(c=0\\) result is therefore ready to be stated as a theorem.

## 4. The two-instance all-\\(q\\) infeasibility theorem

The classification in Part II.5 is logically well organised. It uses the identity

\\[ c=k-\omega \\]

to cover all possible compressed ranks, rather than relying on a search over selected values of \\(q\\).

For the two instances, the reported data are

\\[ k=4,\qquad \dim W_L=2,\qquad W_L\subseteq D. \\]

The four cases are:

| Case        | Geometric consequence                                      | Obstruction                                                                               |
| ----------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| \\(c\ge3\\) | \\(V\subseteq W_L\\), but \\(\dim V>\dim W_L\\)            | No possible \\(V\\)                                                                       |
| \\(c=2\\)   | \\(V=W_L\\)                                                | Every bottom compressed row is proportional to \\(h_0\\), so \\(\operatorname{rank}H<2\\) |
| \\(c=1\\)   | Every admissible \\(V\\) must be an eigenline in \\(W_L\\) | Each eigenline is separately ruled out by a nonzero constraint functional                 |
| \\(c=0\\)   | \\(H\\) is square and invertible                           | \\(\det(\lambda H-H_A)\\) has a complex root                                              |

This is a valid all-strata strategy. In particular, it avoids a common logical mistake: proving that one rank layer is infeasible and then concluding that the original problem is infeasible. Here the report attempts to exclude every possible value of \\(c\\).

### 4.1 The \\(c=2\\) argument is independent of the number of bottom rows

This is an important strength of the report.

When

\\[ \dim W_L=c=2, \\]

the kernel is forced:

\\[ V=W_L. \\]

For each bottom row, the admissibility equations are linear and are claimed to force

\\[ b_i=0. \\]

If this is true row by row, then increasing \\(q\\) cannot help. Every added bottom row is subject to the same constraint. All rows of \\(H\\) remain proportional to \\(h_0\\), so

\\[ \operatorname{rank}H\le1<2=\omega. \\]

This is much stronger than a computational statement such as “no solution was found for \\(q=3,4,5\\).” It proves that the entire \\(c=2\\) layer is impossible for every \\(q\\) to which the same row equations apply.

The certificate

\\[ e_b=\alpha^{\mathsf T}\mathrm{Des}, \qquad \alpha=(-1,0), \\]

is precisely the right kind of certificate. It establishes that \\(b\\) vanishes on the kernel of the admissibility matrix.

For a publication-quality proof, include the actual matrices \\(\mathrm{Des}\_i\\), the vector \\(\alpha\\), and the multiplication

\\[ \alpha^{\mathsf T}\mathrm{Des}\_i=e_b^{\mathsf T} \\]

for each instance and each relevant row type. This makes the obstruction transparent and machine-checkable.

### 4.2 The all-\\(q\\) conclusion is conditional, not yet unconditional

The report's conclusion should be phrased as:

> Under the convention \\(\operatorname{rank}[C;L]=p+q\\), the two specified instances are infeasible for every admissible \\(q\\), provided the stated exact certificates and the \\(c=1\\) eigenline computations are correct.

It should not yet be phrased as an unconditional theorem about the original observer problem. That depends on Question 1.

There is also a useful way to strengthen the computational record: produce a single certificate package for each instance containing

- the exact \\(K_0\\) and \\(N\\);
- the exact matrix defining \\(W_L\\);
- an exact basis of \\(W_L\\);
- a certificate that \\(W_L\subseteq D\\);
- the \\(c=2\\) row-space identities;
- the \\(c=1\\) eigenline polynomial and its complete factorisation over \\(\mathbb C\\);
- the nonzero constraint functional for each eigenline;
- the \\(c=0\\) leading determinant coefficient.

The first five items certify the structural setup; the last three certify the remaining rank layers. This would turn the all-\\(q\\) result into a compact, reproducible exact proof.

## 5. Is the uniform stratum solver a decision procedure?

The pipeline in Part II.1 is a good framework for constructing candidates and certifying positive answers. But the report itself correctly says that a negative answer may be only a failed search. I would make that distinction even sharper.

### 5.1 What the pipeline correctly captures

For a fixed candidate \\(V\\), the compressed construction has the following logic:

1. \\(V=\ker H\\) has dimension \\(c\\).
2. The fixed rows impose \\(V\subseteq W_L\\).
3. The condition \\(H_A|\_V=0\\) is the compressed form of the kernel inclusion required by (5a).
4. The row parameters must make \\(\operatorname{rank}H=\omega\\).
5. The pencil condition is tested by the maximal minors of\
   \\[\
   P(\lambda)=\lambda H-H_A.\
   \\]
6. Any actual lift must satisfy the original rank conditions and the convention on row independence.

The gcd test is mathematically appropriate once the rank of \\(H\\) is exactly \\(\omega\\). Under the kernel inclusion

\\[ \ker H\subseteq\ker H_A, \\]

we have

\\[ \operatorname{rank}(\lambda H-H_A)\le\omega \\]

for every \\(\lambda\\). Since the leading coefficient \\(H\\) has rank \\(\omega\\), the normal rank of the pencil is \\(\omega\\). Thus

\\[ \operatorname{rank}P(\lambda)=\omega \quad\forall\lambda\in\mathbb C \\]

is equivalent to saying that the \\(\omega\times\omega\\) minors have no common finite complex root, or equivalently that their gcd is a nonzero constant.

This is an exact algebraic test for a fixed candidate.

### 5.2 A point in the solver's rank parameterisation needs clarification

The report writes

\\[ \operatorname{Ann}(V) =\langle h_0,u_1,\ldots,u\_{\omega-1}\rangle \\]

and parameterises each bottom row as

\\[ h_i=a_i h_0+\sum_j b\_{ij}u_j. \\]

It then asserts

\\[ \operatorname{rank}H=\omega \iff \operatorname{rank}(b\_{ij})=\omega-1. \tag{5.1} \\]

This equivalence is correct under the implicit assumptions that:

- there is exactly one fixed compressed row \\(h_0\\);
- \\(h_0\ne0\\);
- \\(h_0,u_1,\ldots,u\_{\omega-1}\\) form a basis of the relevant \\(\omega\\)-dimensional row space.

But the report's general setup writes

\\[ L_0\in\mathbb C^{r\times n}, \\]

where \\(r\\) need not be one. If \\(r>1\\), the top compressed matrix

\\[ H_0=L_0N \\]

may have rank \\(\rho_0\\), and the relevant quotient dimension is \\(\omega-\rho_0\\), not necessarily \\(\omega-1\\).

The correct general formulation is:

Let \\(S_0=\operatorname{row}(H_0)\\), with \\(\dim S_0=\rho_0\\). Since \\(V\subseteq W_L\\), we have \\(S_0\subseteq\operatorname{Ann}(V)\\). Then

\\[ \operatorname{rank}H=\omega \\]

if and only if the projections of the bottom rows span

\\[ \operatorname{Ann}(V)/S_0. \\]

In a chosen basis of this quotient, the bottom-row coefficient matrix must have rank

\\[ \omega-\rho_0. \\]

Thus (5.1) is the special case \\(\rho_0=1\\). The report should either state that it is working throughout with \\(r=1\\) and \\(h_0\ne0\\), or replace this step by the quotient-space formulation.

This is not merely a notational issue: the dimension of the coefficient matrix and the rank constraints in the solver depend on it.

### 5.3 Enumerating \\(V\\) is not, by itself, an algorithmic decision method

The instruction “enumerate \\(V\in\operatorname{Gr}(c,W_L)\\)” is geometrically clear, but a Grassmannian over \\(\mathbb C\\) has infinitely many points. A numerical or finite candidate enumeration cannot certify that no \\(V\\) exists unless additional structure reduces the possibilities to a finite list.

A genuine exact decision procedure would need to do one of the following:

- formulate the existence of \\(V\\), the row parameters, and the pencil certificate as a finite system of polynomial equations and inequations, and decide it by an exact real-algebraic or complex-algebraic method;
- stratify the Grassmannian into finitely many algebraic pieces and prove that every piece has been decided;
- or provide a theorem reducing the candidate \\(V\\)'s to a finite collection of explicitly computable invariant subspaces or other special subspaces.

The solver described in the report is therefore best called an exact stratified search with exact positive-witness verification and selected structural negative certificates. It becomes a decision procedure only after the negative branches are made exhaustive and the algebraic feasibility of each remaining branch is decided.

The report is commendably careful about this distinction in its discussion of negative answers. I recommend carrying that terminology into the project documentation.

### 5.4 The lift is a separate necessary stage, not a final implementation detail

The compressed data \\(H,H_A\\) do not automatically give actual rows of \\(L\\). Under the independence-modulo-\\(C\\) convention, the pair-preserving lift criterion from the earlier analysis is the relevant condition.

In the notation developed there, let

\\[ \Psi:\mathcal X^\*/\operatorname{row}C \longrightarrow K_0^\*\oplus K_0^\*, \qquad \bar g\longmapsto(gN,gAN). \\]

The prescribed compressed row-pairs must lie in \\(\operatorname{im}\Psi\\). Under the stated assumptions on the fixed rows, the additional dimension condition is

\\[ \dim\ker\Psi\ge\dim\ker Z\_{\mathrm{pair}}, \\]

or equivalently

\\[ d'\_C\ge q-\omega \\]

when (5a) ensures \\(\operatorname{rank}Z\_{\mathrm{pair}}=\omega\\).

This should be built into the solver before it reports a compressed solution as a solution to the original observer problem.

If the original problem does not require independence modulo \\(C\\), this particular lift criterion must be reconsidered: it was derived for the stronger convention. Pair compatibility remains relevant, but the dimension condition for lifting independent actual rows is a different question. It is not safe simply to delete the inequality and assume that all compressed solutions lift.

### 5.5 A recommended architecture for the solver

I would split the implementation into four independently tested layers:

| Layer           | Input                               | Output                                                       |
| --------------- | ----------------------------------- | ------------------------------------------------------------ |
| Geometry        | \\(A,C,L_0,\omega\\)                | Candidate \\(V\\)'s or a certificate that a stratum is empty |
| Compressed rows | \\(V\\) and admissibility equations | \\(H,H_A\\), with exact ranks                                |
| Spectral test   | \\(H,H_A\\)                         | Exact gcd certificate or a bad \\(\lambda\\)                 |
| Actual lift     | Compressed row-pairs and convention | Actual \\(L\\), or a lift-obstruction certificate            |

A positive result should include an actual \\(L\\), not merely a compressed pair. A negative result should identify which layer excludes the entire stratum. This architecture also makes it easier to determine whether a failure is geometric, spectral, or caused by the row-independence convention.

## 6. Complexity position

The report's complexity discussion is appropriately cautious. There are three separate claims, and they should remain separate.

### 6.1 The solver does not establish membership in RP or BPP

The proposed solver enumerates geometric strata and performs exact algebraic calculations, including gcd computations. It has no established polynomial running-time bound. Therefore it does not show that the problem belongs to RP or BPP.

Even if the solver finds a witness quickly on the two test instances, that is empirical performance, not a randomized polynomial-time complexity result.

### 6.2 The \\(\exists\mathbb R\\) membership claim is a promising independent result

The report uses the original pencil

\\[ Q(\lambda)= \begin{bmatrix} \lambda L-LA\\\ CA\\\ C \end{bmatrix} \\]

and a polynomial generalized-inverse certificate

\\[ Q(\lambda)Y(\lambda)Q(\lambda)=Q(\lambda), \qquad \deg Y\le 2s-2, \\]

where

\\[ s=\operatorname{rank}[L;CA;C]. \\]

The key point is that the certificate must be accompanied by the normal-rank condition

\\[ \operatorname{nrank}Q=s. \\]

Without it, the identity alone does not establish the required rank. With it, the local Smith-form argument shows that the invariant factors have no finite roots, so the rank remains \\(s\\) at every finite \\(\lambda\\).

This is a reasonable route to an \\(\exists\mathbb R\\) upper bound, provided the polynomial degree bound and the encoding of the remaining rank conditions are stated fully. The finite disjunction over possible \\(q\\) values then gives the corresponding MIN formulation.

One point should be made explicit in the report: the real-algebraic encoding of complex coefficients must represent each coefficient by its real and imaginary parts, and every nonzero condition must be expressed as a real polynomial inequation, for example

\\[ (\operatorname{Re}z)^2+(\operatorname{Im}z)^2>0. \\]

### 6.3 Neither NP membership nor hardness follows

The report correctly observes that algebraic witnesses need not be rational. A certificate consisting only of rational entries is therefore not automatically available, so NP membership has not been established.

Likewise, \\(\exists\mathbb R\\)-membership is an upper bound, not a hardness result. The project should not yet claim:

- NP-hardness;
- \\(\exists\mathbb R\\)-hardness;
- polynomial-time solvability;
- or NP membership.

The appropriate current statement is that the decision problem has a proposed \\(\exists\mathbb R\\) formulation, while its lower-bound complexity remains open.

## 7. Answers to the six questions

Here are my direct answers to the report's questions.

| Question                                                           | Assessment                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Q1. Does the original problem require independence modulo \\(C\\)? | Not determined by the report. It must be checked against the original observer definition. The implication \\(V\subseteq W_L\\), and hence \\(V=W_L\\) when their dimensions agree, follows from (5a), not from independence modulo \\(C\\). The lifting criterion does depend on the convention.                                             |
| Q2. Is the \\(c=1\\) hyperplane lemma correct?                     | Yes, under \\(W_L\subseteq K_0\cap A^{-1}K_0\\). It forces every admissible \\(V\\) to be an eigenline. The reported eigenline calculations need exact certificates. An identically-zero eigenline equation is a separate case; if \\(\dim W_L\ge2\\), it means \\(A\|\_{W_L}=\lambda I\\), and the hyperplane argument gives no obstruction. |
| Q3. Is the \\(c=0\\) determinant obstruction correct?              | Yes, over \\(\mathbb C\\), for \\(k=q=\omega\ge1\\) and invertible \\(H\\). The determinant has degree exactly \\(k\\), so it has a root. The zero-polynomial loophole is excluded by the nonzero leading coefficient.                                                                                                                        |
| Q4. Is the solver a valid decision procedure?                      | It is a valid framework for exact candidate construction and witness verification, but not yet a complete decision procedure. Continuous Grassmannian enumeration, exhaustive negative certification, the general \\(r\\)-row rank parameterisation, and actual row lifting need to be addressed.                                             |
| Q5. Should the \\(c=1\\) lemma be generalised?                     | Yes, but in two stages. First, retain the proven arbitrary-\\(\omega\\) result under \\(W_L\subseteq D\\). Second, study \\(W_L\not\subseteq D\\) using the full row-lift variables. The compressed hyperplane argument alone is insufficient there.                                                                                          |
| Q6. What should be done next?                                      | First settle the original convention. Then validate the all-\\(q\\) certificates and test the solver on a genuinely feasible instance. The general component-bound project can continue in parallel, but it should not take priority over resolving the definition on which the current infeasibility conclusion depends.                     |

## 8. Recommended next steps, in priority order

I would not proceed directly to the general component bound as the main next task. Report 61 has exposed a more immediate issue: the project may have proved an all-\\(q\\) impossibility theorem for a stronger problem than the original observer problem.

### Priority 1 — Resolve the original definition

Recover the original statement defining admissible observers and answer precisely:

1. Is \\(\operatorname{rank}L=q\\) required?
2. Is \\(\operatorname{rank}[C;L]=p+q\\) explicitly required?
3. Is \\(C\\) assumed to have full row rank?
4. Is the order \\(q\\) the number of rows of \\(L\\), or the dimension of a quotient/output space?
5. Are redundant rows modulo \\(\operatorname{row}C\\) permitted?

This should be settled by quoting the original definition, not by inferring it from the compressed formulation.

If independence modulo \\(C\\) is required, the two-instance theorem is potentially a strong result. If it is not required, the solver and lift analysis must be revised before the theorem is used to draw conclusions about the original problem.

### Priority 2 — Finalise the two-instance proof

Assuming the convention is correct, make the all-\\(q\\) theorem fully auditable.

For each instance, provide:

- exact \\(K_0\\), \\(N\\), and \\(W_L\\);
- an exact proof that \\(\dim W_L=2\\);
- an exact proof that \\(W_L\subseteq D\\);
- the \\(c=2\\) row-space certificates;
- the complete \\(c=1\\) eigenline polynomial over \\(\mathbb C\\);
- the nonzero functional certificate for every eigenline;
- the \\(c=0\\) determinant argument.

I would also include a short theorem that combines the four cases. This makes the proof much easier to review than a collection of solver outputs.

### Priority 3 — Test the solver on a feasible instance

This is the most important computational next step.

The two instances in Report 61 are both infeasible under the stated convention. They are therefore excellent tests of negative certificates, but they cannot demonstrate that the solver can successfully construct a solution.

Construct or search for an instance with

\\[ \dim W_L>c \\]

and with a nonempty feasible stratum. Ideally, choose an instance for which:

- the admissible \\(V\\)'s form a positive-dimensional family;
- the compressed pencil has constant rank;
- the pair-preserving lift condition is satisfied;
- an actual full-row-rank \\(L\\) can be constructed.

Then test the entire pipeline, including reconstruction of \\(L\\) and independent verification of (5a) and (5b).

A solver that only returns negative results on infeasible examples has not yet been adequately validated.

### Priority 4 — Formalise the \\(c=1\\) theorem and exceptional case

The formal theorem should read approximately as follows:

> Let \\(V=\mathbb Cv\subseteq W_L\subseteq K_0\cap A^{-1}K_0\\). Suppose the compressed rows satisfy the admissibility conditions and \\(\operatorname{rank}H=\omega\\). Then \\(Av\in V\\).

The proof is short and well suited to Lean:

1. Show \\(Av\in K_0\\).
2. Express \\(Av=Nw\\).
3. Show every row \\(h_i\\) annihilates \\(v\\).
4. Show every row \\(h_i\\) annihilates \\(w\\).
5. If \\(w\notin V\\), construct a nonzero functional on \\(\operatorname{Ann}(V)\\).
6. Deduce that all rows of \\(H\\) lie in a proper subspace.
7. Contradict \\(\operatorname{rank}H=\omega\\).

Separately, handle

\\[ A|\_{W_L}=\lambda I. \\]

Do not fold this case into the generic eigenline computation.

### Priority 5 — Generalise the solver's row parameterisation

Clarify whether the project assumes \\(r=1\\). If so, state it prominently. Otherwise, replace the \\(h_0\\)-based parameterisation by the quotient

\\[ \operatorname{Ann}(V)/\operatorname{row}(L_0N). \\]

This is the correct formulation for general \\(r\\).

Then incorporate the appropriate lift test for the chosen observer convention.

### Priority 6 — Continue the general component-bound programme

The component-bound work remains mathematically worthwhile and is largely independent of whether the two current test instances are feasible. However, it answers a different question: how complicated the admissible geometric strata can be.

I would continue it as a separate workstream, with the following distinction maintained:

- the \\(c=1\\) lemma is a structural infeasibility result;
- the two-instance theorem is a problem-specific all-\\(q\\) result;
- the general component bound is a geometric complexity result;
- the lift theorem connects compressed geometric solutions to actual observers.

These results should not be merged into a single claim about algorithmic complexity.

## 9. Overall conclusion

Report 61 makes genuine progress. The \\(c=0\\) obstruction is rigorous, the \\(c=1\\) hyperplane lemma is mathematically sound under its stated assumptions, and the \\(c=2\\) row-wise forcing argument has the right structure to prove infeasibility independently of \\(q\\). Together they give a coherent all-strata argument for the two examples under the report's convention.

The most important qualification is that the convention itself remains unverified. The condition

\\[ \operatorname{rank}[C;L]=p+q \\]

is a substantive restriction, not a technical convenience. The all-\\(q\\) conclusion should therefore remain explicitly conditional until the original observer definition is checked.

My recommendation is to resolve the convention first, then complete the two-instance exact proof, and then validate the solver on a feasible example. In parallel, the general component-bound work can continue, but it should not distract from this immediate foundational issue.

The next most useful material to examine is the original problem statement or paper definition of admissible \\(L\\). With that in hand, we can decide whether Report 61 has proved infeasibility for the intended observer problem or for a stricter variant.&#x20;

61_solver_c1_infeasibility.md
