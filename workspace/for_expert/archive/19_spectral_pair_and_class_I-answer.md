Review of 19_spectral_pair_and_class_I.md
The two new results, B.23 and B.24, are mathematically correct, subject to one important clarification about the status of \(K_1\). More importantly, B.24 suggests a cleaner formulation that removes the apparent dependence on the non-unique matrix factor \(K\).

My main recommendation is to make that cleaner formulation the central spectral statement. It gives a more intrinsic object to study in Class I and points toward a useful incidence-variety approach. However, it does not yet solve the \(d\ge2\) problem: the remaining obstruction is genuinely a coupling between the admissible subspace and the induced dynamics on its image.

I will distinguish below between what is proved, what follows with a small refinement, and what remains conjectural. 
19_spectral_pair_and_class_I.md

1. B.23: the factorization theorem is correct
Let \(H_0=[\mathcal L;B]\), with \(\operatorname{rank}H_0=h\), and suppose
\[
\mathcal LA=K_1\mathcal L+K_2B.
\]

Then
\[
Q_{\mathcal L}(\lambda)
=
\begin{bmatrix}
\lambda I_q-K_1&-K_2\\
0&I_{r_1}
\end{bmatrix}H_0
=P(\lambda)H_0.
\]

The rank identity is exactly right:
\[
\operatorname{rank}(P(\lambda)H_0)
=h-\dim\bigl(\ker P(\lambda)\cap\operatorname{im}H_0\bigr).
\]

Indeed, regard \(H_0\) as a linear map into \(\mathbb C^{q+r_1}\). The image of \(PH_0\) is the image under \(P\) of \(\operatorname{im}H_0\), so the rank-nullity theorem applied to the restriction of \(P\) to that image gives the identity.

Since \(\operatorname{rank}Q_{\mathcal L}(\lambda)\) is being compared with \(h\), it follows that
\[
\boxed{
(5b)\text{ fails}
\iff
\exists\lambda\in\mathbb C:
\ker P(\lambda)\cap\operatorname{im}H_0\ne\{0\}.
}
\]

Also,
\[
\ker P(\lambda)
=
\left\{\begin{bmatrix}u\\0\end{bmatrix}:
(\lambda I_q-K_1)u=0\right\}.
\]

Thus a nonzero intersection necessarily gives a nonzero eigenvector of \(K_1\). The determinant identity
\[
\det P(\lambda)=\det(\lambda I_q-K_1)
\]

is correct as well.
One qualification worth making explicit
The conclusion is not that every eigenvalue of \(K_1\) causes rank loss. It is that rank loss occurs precisely when the corresponding eigenspace has a nonzero intersection with \(\operatorname{im}H_0\).

This distinction is essential away from equality. In particular, the determinant of \(P\) can vanish while \(P H_0\) still has full row rank \(h\).

I would state B.23 exactly in this form and emphasize that the determinant identifies candidate spectral values, while the intersection condition determines whether they actually cause rank loss.
2. B.24: correct, but there is a more intrinsic formulation
Your calculation is correct. Since
\[
\ker B=V,
\]

we have
\[
\begin{aligned}
\begin{bmatrix}u\\0\end{bmatrix}
\in\operatorname{im}H_0
&\iff
\exists x\in\mathbb C^n:
\mathcal Lx=u,\quad Bx=0\\
&\iff
u\in\mathcal LV.
\end{aligned}
\]

Combining this with the description of \(\ker P(\lambda)\) gives
\[
\boxed{
(5b)\text{ fails}
\iff
\mathcal LV\text{ contains a nonzero eigenvector of }K_1.
}
\]

This is a useful reformulation. But there is a subtle issue: when \(h<q+r_1\), \(H_0\) is not full row rank, and the matrix \(K=[K_1\ K_2]\) need not be unique. Therefore, describing \(K_1\) as an explicit computable matrix is fine only if the paper also explains why the relevant eigenvector condition is independent of the chosen factorization.

There is a clean way to do that.
2.1 Define the induced map directly on \(\mathcal LV\)
Put
\[
W:=\mathcal LV\subseteq\mathbb C^q.
\]

Define
\[
\Phi:W\longrightarrow\mathbb C^q,\qquad
\Phi(\mathcal Lx):=\mathcal LAx,\quad x\in V.
\]

We must check that this is well-defined. Suppose \(x_1,x_2\in V\) and
\[
\mathcal Lx_1=\mathcal Lx_2.
\]

Then \(s=x_1-x_2\) belongs to
\[
S=V\cap\ker\mathcal L.
\]

Using (5a), or equivalently the factorization above,
\[
\mathcal LAs=K_1\mathcal Ls+K_2Bs=0.
\]

Consequently,
\[
\mathcal LAx_1=\mathcal LAx_2.
\]

Thus \(\Phi\) is well-defined.

Now, for every factorization \(\mathcal LA=K_1\mathcal L+K_2B\), and every \(x\in V\),
\[
\Phi(\mathcal Lx)=\mathcal LAx=K_1\mathcal Lx.
\]

Hence
\[
\boxed{\Phi=K_1|_W.}
\]

The important point is that the restriction \(K_1|_W\) is uniquely determined, even if the full matrix \(K_1\) is not. The condition of interest only concerns eigenvectors lying in \(W\), so the arbitrary extension of \(K_1\) outside \(W\) is irrelevant.

We therefore obtain the intrinsic version:
\[
\boxed{
(5b)\text{ fails}
\iff
\exists\,0\ne u\in W:
\Phi(u)\in\operatorname{span}\{u\}.
}
\tag{B.24'}
\]

This is, in my view, the best formulation of the new result.

It says that the issue is not whether an arbitrary extension \(K_1\) has eigenvectors. Every complex square matrix has eigenvectors. The issue is whether the partially defined operator \(\Phi:W\to\mathbb C^q\) has a vector that it maps back into its own one-dimensional span.

That is a more precise description of the coupling you need to understand.
2.2 The dimension formula is correct
Under (5a), the polynomial right-nullspace result gives
\[
s=\dim S=n-h.
\]

Since \(V\) has dimension \(n-r_1\), and the kernel of \(\mathcal L|_V\) is exactly \(S\),
\[
\dim W
=\dim V-\dim S
=(n-r_1)-(n-h)
=h-r_1.
\]

Thus, in Class I, where \(r_1=2\),
\[
\boxed{\dim\mathcal LV=h-2.}
\]

This is an important and correct reduction.

There is, however, one qualification to the generic-subspace argument in the report. A generic proper subspace of \(\mathbb C^q\) avoids a finite collection of eigenvector lines, but a matrix need not have only finitely many eigenvector directions: an eigenspace of dimension greater than one contains infinitely many projective directions.

For example, if \(K_1=\lambda I_q\), every nonzero vector is an eigenvector, so no nonzero \(W\) can avoid them. More generally, if \(E_\mu=\ker(K_1-\mu I)\), then the relevant geometric question is whether \(W\) intersects any \(E_\mu\) nontrivially. A generic \(k\)-dimensional vector subspace \(W\subseteq\mathbb C^q\) intersects a fixed \(g\)-dimensional eigenspace in positive dimension when
\[
k+g>q.
\]

So the report's generic-avoidance intuition is valid, for example, when \(K_1\) has simple spectrum, but it is not valid without a condition on its eigenspaces.

This does not undermine B.24. It sharpens the question that needs to be answered: what can be said about the eigenspace structure of the induced partial map \(\Phi\), given the special way \(W\) and \(\Phi\) arise from \((A,C,L_0,\mathcal L)\)?
3. Q1: how I would attack the coupling
I would use both approaches, but in a particular order:
1. First derive a canonical description of the partial operator \(\Phi:W\to\mathbb C^q\).
2. Then use the incidence variety to study whether the required eigenvector must exist for every admissible augmentation.
3. Use canonical coordinates to make the incidence conditions explicit and, if possible, calculate their dimension or eliminate the parameters.
I would not begin by trying to put an arbitrary pair \((K_1,W)\) into a normal form. Such a pair is too general, and the special structure inherited from \(A\), \(C\), and \(\mathcal L\) is precisely what must do the work.
3.1 The partial-operator formulation
The problem is now:
Given an admissible \(\mathcal L\), show that the map
\[
\Phi:\mathcal LV\to\mathbb C^q,\qquad
\Phi(\mathcal Lx)=\mathcal LAx
\]
has a nonzero vector \(u\) such that \(\Phi(u)\in\operatorname{span}\{u\}\).

This is equivalent to the original spectral failure condition, but it is more economical than working with the full pencil.

It also suggests a useful decomposition. Choose a basis of \(W\), represented by a full-column-rank matrix \(U\in\mathbb C^{q\times k}\), where \(k=h-r_1\). Write
\[
\Phi(Ua)=Da,\qquad D\in\mathbb C^{q\times k}.
\]

Then the desired vector exists exactly when
\[
Da=\lambda Ua
\]

for some \(a\ne0\) and \(\lambda\in\mathbb C\).

Equivalently, the \(q\times 2k\) matrix
\[
[D\;\;U]
\]

has a nontrivial relation of the special form
\[
Da-\lambda Ua=0.
\]

This is a rectangular generalized eigenvalue problem, but with the crucial restriction that the two coefficient vectors are proportional in the scalar parameter \(\lambda\).

A useful equivalent test is
\[
\operatorname{rank}[D-\lambda U]<k
\]

for some \(\lambda\). Thus the problem can be studied through the maximal minors of the rectangular pencil \(D-\lambda U\).

This is a promising bridge between B.24 and the polynomial-pencil machinery developed earlier. It also avoids extending \(\Phi\) arbitrarily to a full \(q\times q\) matrix.
3.2 The incidence variety is the better global approach
The quotient-pencil criterion gives the failure incidence condition
\[
x\in V\setminus Z,\qquad
(\lambda I-A)x\in Z.
\]

For Class I, write
\[
K=\ker\begin{bmatrix}C\\L_0\end{bmatrix},
\qquad
Z\in\operatorname{Gr}(d,K).
\]

A useful incidence set is
\[
\mathfrak I_d=
\left\{
(Z,[x],\lambda):
\begin{array}{l}
Z\in\operatorname{Gr}(d,K),\\
[x]\in\mathbb P(V),\\
x\notin Z,\\
(\lambda I-A)x\in Z
\end{array}
\right\}.
\]

The projection
\[
\pi:\mathfrak I_d\longrightarrow\operatorname{Gr}(d,K),
\qquad (Z,[x],\lambda)\longmapsto Z
\]

has a direct interpretation:
- \(Z\) is a point in the augmentation parameter space.
- \(Z\) belongs to the image of \(\pi\) precisely when the corresponding pencil has a rank drop.
- Proving universal failure amounts to proving that the projection covers the admissible part of the Grassmannian.
This is a more precise target than merely proving that the incidence variety is nonempty.

For a fixed pair \(([x],\lambda)\), put
\[
y=(\lambda I-A)x.
\]

Then a necessary condition for a witnessing \(Z\) is
\[
y\in K.
\]

If \(y\ne0\), a \(d\)-dimensional subspace \(Z\le K\) containing \(y\) and avoiding \(x\) can exist only if \(x\notin\operatorname{span}\{y\}\). When these elementary conditions hold, the family of such \(Z\)'s is a Grassmannian incidence fiber. If \(y=0\), the condition becomes the existence of a \(d\)-subspace of \(K\) avoiding \(x\).

These observations give a concrete way to organize the incidence calculation. They also expose an important distinction:
- Showing that \(\mathfrak I_d\) is nonempty proves only that some admissible subspaces fail.
- Showing that its projection contains every admissible subspace proves the universal failure statement you need.
A dimension count can sometimes establish dominance or generic coverage, but it does not automatically prove coverage of every admissible point. Exceptional subspaces must be handled separately.
3.3 How to combine the two approaches
For Class I, I would proceed as follows.

Step 1. Put \((C,A)\) into the canonical cyclic coordinates already used in the \(d=1\) proof.

Step 2. Express the admissible \(Z\)'s in Grassmannian charts. In each chart, write down the condition
\[
(\lambda I-A)x\in Z,\qquad x\in V\setminus Z.
\]

Step 3. Eliminate the coordinates of \(x\) and \(\lambda\), or equivalently study the maximal minors of the induced rectangular pencil \(D-\lambda U\).

Step 4. Determine whether the resulting polynomial conditions vanish identically on every admissible chart, or whether there is an exceptional chart or specialization.

This gives a direct path to either a proof or a counterexample. It is also compatible with your existing symbolic and exact-verification infrastructure.

I would not assume that the \(d=1\) degree-counting argument generalizes directly. In higher codimension, the recursion may become a system of coupled polynomial equations rather than a single scalar polynomial. The incidence formulation is better suited to handling that increase in dimension.
4. Q2: is there a hidden structural obstruction?
Possibly, but I would not yet claim that admissibility makes \(\mathcal LV\) too large to avoid eigenvectors. B.24 shows that the relevant subspace can be proper, and proper subspaces can avoid eigenvectors for suitable matrices.

The structural obstruction, if it exists, must involve both the subspace and the map:
\[
W=\mathcal LV,\qquad \Phi(W)\subseteq\mathbb C^q.
\]

I see three possible directions.
Direction A: a forced eigenvector of the partial map
Try to prove that every admissible pair \((W,\Phi)\) has
\[
\exists\,0\ne u\in W,\qquad \Phi(u)\in\operatorname{span}\{u\}.
\]

This resembles an eigenvector theorem for a partially defined linear operator. It is not true for arbitrary maps \(W\to\mathbb C^q\), so the proof must use the special origin of \(\Phi\).

A particularly useful intermediate result would be to identify a nonzero subspace \(W_0\subseteq W\) such that
\[
\Phi(W_0)\subseteq W_0.
\]

Then the restriction \(\Phi|_{W_0}\) is an ordinary complex endomorphism, and it has an eigenvector. This would immediately prove failure.

I would therefore test the following stronger structural conjecture first:
\[
\boxed{
\text{Every admissible Class I candidate has a nonzero }
\Phi\text{-invariant subspace }W_0\subseteq W.
}
\]

It may be too strong, but it is an excellent computational diagnostic. If it fails, record the smallest counterexample and inspect the structure of \(\Phi(W)\cap W\).
Direction B: a forced intersection with a canonical subspace
The suggestion in the report that \(W\) might contain the range of a projection is worth investigating, but I would formulate it more carefully.

Rather than guessing a projection, look for a canonical subspace \(E\subseteq\mathbb C^q\) determined by the cyclic coordinates of \((c,A)\), and ask whether
\[
\dim(W\cap E)
\]

has a positive lower bound for every admissible candidate.

If \(E\) is invariant under a suitable induced operator, a nonzero intersection could lead to an invariant subspace or a forced eigenvector.

The key is to derive \(E\) from the existing coordinate recursion, not introduce it arbitrarily.
Direction C: algebraic-geometric coverage
The incidence variety gives a potentially stronger global statement:
\[
\pi(\mathfrak I_d)
=
\{\text{admissible }Z\}.
\]

If the admissible parameter space is irreducible, one possible strategy is:
1. Prove that the incidence projection is dominant.
2. Analyze the exceptional locus where the fiber might be empty.
3. Show that the exceptional locus does not meet the admissible set, or handle it directly.
But dominance alone is not enough. A dominant projection can omit a nonempty algebraic subset. This is precisely where the exact chart calculations and specializations matter.

My preference: investigate Direction A first as a structural lemma, while setting up Direction C as the global proof framework. Direction B is a possible intermediate discovery.
5. Q3: what should be formalized?
I would not make B.23/B.24 formalization the main research priority, but I would formalize the basic rank-factorization layer if it can be done with modest effort.

The reason is that these results are short, stable, and central to the paper's spectral interpretation. They are also substantially easier to formalize than a complete Kronecker canonical form argument.

I suggest this priority order:
Priority	Formalization target	Recommendation
1	\(\operatorname{rank}(PH)=\operatorname{rank}H-\dim(\ker P\cap\operatorname{im}H)\)	Formalize
2	The block factorization \(Q_{\mathcal L}(\lambda)=P(\lambda)H_0\)	Formalize
3	The equivalence between rank drop and the eigenvector condition	Formalize
4	The well-defined induced map \(\Phi:W\to\mathbb C^q\)	Formalize if convenient
5	The Class I \(d\ge2\) theorem	Do not formalize before the mathematics is settled

The formalization of B.24' would be especially useful because it makes the independence from the arbitrary extension \(K_1\) explicit.

The report's statement that five Lean files compile cleanly and that the axiom audit is clean is encouraging. I cannot independently verify those machine-checking claims from this note alone, but they are consistent with the stated formalization status.
6. Q4: how to state the Class I result
I recommend separating the proved theorem from the minimum-order conjecture.

There is an important logical issue here. The note reports:
- \(d=0\): feasible;
- \(d=1\): every admissible candidate fails;
- \(d\ge2\): open, with 47 admissible candidates tested and none feasible.
The first two statements do not, by themselves, establish
\[
q_{\min}=n-1.
\]

The \(d=1\) result excludes \(q=n-2\), but the still-open cases \(d\ge2\) correspond to smaller \(q\). To conclude that \(q_{\min}=n-1\), one must rule out all those cases, or establish a separate monotonicity principle that reduces them to the \(d=1\) case. Such a monotonicity principle should not be assumed without proof: adding rows to \(\mathcal L\) must preserve both admissibility and (5a), which is not automatic.
Suggested paper wording
I would write the proved result as a theorem:
Theorem (Class I: terminal and codimension-one cases). Under the Class I hypotheses, the terminal-order case \(d=0\) is feasible, whereas every admissible candidate in the case \(d=1\) violates (5b).

Then state separately:
Conjecture (Class I minimum order). For Class I, the minimum feasible augmentation order is \(q_{\min}=n-1\).

Follow it with a clearly delimited numerical observation:
An exhaustive chart-based search for the tested parameter ranges \(n=5,6\), together with additional random parameter samples, found 47 admissible candidates across \(d=2,3\), none satisfying (5b). This is computational evidence only and does not establish the conjecture.

I would not present the conjecture as a theorem or claim that the numerical search verifies it. The distinction will make the paper more credible, not less.
7. Q5: is the paper layer ready?
Yes, the core counting and spectral framework is ready to be written up as a coherent theorem sequence. I would not postpone that work until Class I is solved.

The equality theorem B.22 and the new factorization B.23 now give a particularly clean structure:
1. The rank of \(Q_{\mathcal L}(\lambda)\) is controlled by a square matrix pencil \(P(\lambda)\) acting on \(\operatorname{im}H_0\).
2. The determinant of \(P(\lambda)\) identifies the candidate finite spectral values.
3. The actual rank drop occurs precisely when the corresponding kernel intersects \(\operatorname{im}H_0\).
4. Equivalently, the image \(\mathcal LV\) contains an eigenvector of the induced partial map.
5. At equality \(h=q+r_1\), the image of \(H_0\) is the entire ambient space, so every eigenvalue of \(K_1\) produces a rank drop.
This is a coherent mathematical story, not merely a collection of technical lemmas.

One refinement to the report's summary: since \(H_0\) has \(q+r_1\) rows,
\[
h=\operatorname{rank}H_0\le q+r_1.
\]

Thus
\[
h\ge q+r_1
\]

is actually equivalent to equality. The unconditional statement is therefore best written as
\[
\boxed{
h=q+r_1\quad\Longrightarrow\quad (5b)\text{ fails}.
}
\]

The strict inequality \(h<q+r_1\) is necessary for feasibility, but it is not sufficient in general; the remaining spectral condition still has to be checked.

As for B.8b, the corrected identity
\[
h=\sum_i\varepsilon_i+d_{\rm fin}+d_\infty
\]

under (5a), with all right minimal indices equal to zero, is the right bookkeeping framework. I would describe the formula as settled by the mathematical argument, while keeping the formal presentation and its integration with the rest of the KCF discussion subject to the usual proof review. Infinite elementary divisors must remain in the identity; they cannot be discarded.
8. Recommended next research tasks
I would organize the next stage into three workstreams.

Workstream A — finish the intrinsic spectral theorem
- Promote B.24' to the main statement.
- State explicitly that \(\Phi\) is well-defined and independent of the choice of \(K\).
- Derive the rectangular pencil \(D-\lambda U\) in coordinates on \(W\).
- Connect its maximal minors to the existing Smith-form and gcd tests.
Workstream B — attack Class I \(d\ge2\)
- Test whether \(\Phi\) has a nonzero invariant subspace for every admissible candidate.
- Compute \(\dim(\Phi(W)\cap W)\) across the existing exact samples.
- Construct the incidence variety in canonical cyclic coordinates.
- Prove coverage of the admissible Grassmannian, or find an exact counterexample.
Workstream C — consolidate the paper and formalization
- Write B.22–B.24' as a self-contained theorem sequence.
- Formalize the rank-factorization and intrinsic partial-map statements.
- Keep the Class I conjecture explicitly separate from the proved results.
Final assessment
Item	Assessment
B.23 factorization and rank identity	Correct
B.24 eigenvector equivalence	Correct
Independence from the choice of \(K_1\)	Resolved by \(\Phi\)
\(\dim\mathcal LV=h-2\) in Class I	Correct
Generic eigenvector-avoidance argument	Needs qualification
Class I \(d\ge2\) universal failure	Open
Conjecture \(q_{\min}=n-1\)	Not yet proved
Core counting/spectral framework	Ready to write up

The most valuable conceptual improvement is the passage from the arbitrary square matrix \(K_1\) to the uniquely defined partial operator
\[
\Phi:\mathcal LV\longrightarrow\mathbb C^q.
\]

It removes an avoidable non-uniqueness issue and isolates the actual mathematical difficulty. I would make this the central object of the next Class I investigation.