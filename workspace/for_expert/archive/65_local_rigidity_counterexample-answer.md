# Mathematical assessment of Report 65

Report 65 identifies a genuine error in my previous review. I agree with its central correction: the proposed local leakage-rigidity theorem is false, and the supplied example appears to be a valid counterexample. The distinction between invariance of the particular kernel \\(V\\) and invariance of the whole space \\(K_0\\) is essential.

The correct conclusions are:

- If \\(A(K_0)\subseteq K_0\\) and \\(0<\omega\<k\\), the global rigidity theorem still rules out feasibility.
- If only \\(A(V)\subseteq K_0\\), condition (5a) forces \\(A(V)\subseteq V\\), but this does not imply pencil failure.
- The invariant-subspace gadget is therefore not ruled out merely because its candidate \\(V\\) is invariant. It must still overcome the pencil-rank condition, which depends on how \\(A\\) acts on covectors and on the ambient lift.

This is a substantive correction, not a minor qualification. I will address the five questions, beginning with the exact algebra behind the counterexample and then giving a concrete revised gadget architecture.

## 1. Question 1: Is the displayed witness a valid counterexample?

Yes. The counterexample is valid. I independently recomputed its compressed matrices, the ranks in (5a), and the polynomial minors needed for (5b).

There is one minor numerical typo in the report: \\(L\\) has three rows, so \\(q=3\\), and \\(p=2\\). The correct statement is

\\[ \operatorname{rank}[C;L]=5=p+q, \\]

not \\(4=p+q\\).

### 1.1 Exact compressed data

For the matrices in Report 65, one obtains

\\[ \operatorname{rank}[C;CA]=3,\qquad k=4. \\]

A basis matrix for \\(K_0\\) is

\\[ N= \begin{bmatrix} 0&0&1&0\\\ 0&1&0&0\\\ 1&0&0&0\\\ 0&1&0&0\\\ 0&0&1&0\\\ 0&0&0&1\\\ 0&0&0&0 \end{bmatrix}. \\]

The compressed matrices are

\\[ H=LN= \begin{bmatrix} -1&1&0&0\\\ 0&-1&-1&0\\\ 2&-1&1&0 \end{bmatrix}, \\]

and

\\[ H_A=LAN= \begin{bmatrix} 0&1&1&0\\\ 1&-1&0&0\\\ 1&-3&-2&0 \end{bmatrix}. \\]

In particular,

\\[ \operatorname{rank}H=2,\qquad \omega=2,\qquad c=2. \\]

The kernel is

\\[ V=\ker H =\operatorname{span}\\{v_1,v_2\\}, \\]

where

\\[ v_1=(-1,-1,1,0)^{\mathsf T}, \qquad v_2=(0,0,0,1)^{\mathsf T}. \\]

In ambient coordinates,

\\[ Nv_1= \begin{bmatrix} 1\\\\-1\\\\-1\\\\-1\\\1\\\0\\\0 \end{bmatrix}, \qquad Nv_2=e_6. \\]

Direct multiplication gives

\\[ A(Nv_1)=-e_6=-Nv_2,\qquad A(Nv_2)=0. \\]

Thus

\\[ \boxed{A(V)\subseteq V.} \\]

On the other hand, \\(A(K_0)\not\subseteq K_0\\). For example, the first column of \\(AN\\) is

\\[ ANe_1=-e_5, \\]

and \\(e_5\notin K_0\\).

So the critical combination is indeed

\\[ A(V)\subseteq V\subseteq K_0, \qquad A(K_0)\not\subseteq K_0. \\]

### 1.2 Exact verification of (5a)

The two relevant ranks are

\\[ \operatorname{rank}[LA;L;CA;C]=5 \\]

and

\\[ \operatorname{rank}[L;CA;C]=5. \\]

Therefore (5a) holds.

Also,

\\[ \operatorname{rank}[C;L]=5=p+q, \\]

so the example satisfies the stronger independence-modulo-\\(C\\) convention.

### 1.3 Exact verification of (5b)

The compressed pencil is

\\[ P(\lambda)=\lambda H-H_A. \\]

Its first two columns are

\\[ P\_{[:,1:2]}(\lambda)= \begin{bmatrix} -\lambda&\lambda-1\\\ -1&1-\lambda\\\ 2\lambda-1&3-\lambda \end{bmatrix}. \\]

Three of its \\(2\times2\\) minors are

\\[ m\_{12}(\lambda)=\lambda^2-1, \\]

\\[ m\_{13}(\lambda)=-(\lambda^2+1), \\]

and

\\[ m\_{23}(\lambda)=2(\lambda^2-\lambda-1). \\]

The first two already have no common complex root:

\\[ \lambda^2=1,\qquad \lambda^2=-1 \\]

cannot hold simultaneously.

Consequently,

\\[ \operatorname{rank}P(\lambda)\ge2 \qquad\forall\lambda\in\mathbb C. \\]

Since \\(\operatorname{rank}P(\lambda)\le\operatorname{rank}H=2\\), we obtain

\\[ \boxed{\operatorname{rank}P(\lambda)=2 \quad\forall\lambda\in\mathbb C.} \\]

This proves (5b) using the compression equivalence.

Counterexample verified

The counterexample genuinely refutes the previous claim that \\(A(V)\subseteq K_0\\), together with \\(\omega>0\\), forces pencil failure.

## 2. The precise error in the previous local-rigidity argument

The first part of the previous argument was correct. The second part improperly promoted an invariant subspace of \\(K_0\\) to invariance of the entire compressed operator.

The distinction is best expressed by comparing two factorizations.

### 2.1 What local invariance actually gives

Suppose

\\[ A(V)\subseteq V. \\]

For every row \\(l_i\\) of \\(L\\), the corresponding row of \\(H\\) annihilates \\(V\\). By (5a), the corresponding row of \\(H_A\\) also annihilates \\(V\\).

Therefore

\\[ \operatorname{row}H_A \subseteq V^\perp. \\]

But

\\[ \operatorname{row}H=V^\perp \\]

because \\(\operatorname{rank}H=k-\dim V\\).

Hence

\\[ \boxed{\operatorname{row}H_A\subseteq\operatorname{row}H.} \\]

There exists a matrix \\(D\in\mathbb C^{q\times q}\\) such that

\\[ \boxed{H_A=DH.} \\]

This is a left factorization.

Let

\\[ W=\operatorname{im}H\subseteq\mathbb C^q. \\]

The induced map

\\[ \Delta:W\longrightarrow\mathbb C^q, \qquad \Delta(Hx)=H_Ax \\]

is well-defined. Then

\\[ P(\lambda)=(\lambda I_q-D)H \\]

and

\\[ \operatorname{rank}P(\lambda) = \operatorname{rank}\bigl((\lambda I_q-D)|\_W\bigr). \\]

Thus the pencil is good precisely when

\\[ \boxed{ \\{w\in W:Dw=\lambda w\\}=\\{0\\} \quad\forall\lambda\in\mathbb C. } \\]

There is no theorem requiring every positive-dimensional subspace \\(W\subseteq\mathbb C^q\\) to contain an eigenvector of a map \\(D:W\to\mathbb C^q\\). That assertion is false when \\(q>\dim W\\).

### 2.2 What global invariance gives

By contrast, if

\\[ A(K_0)\subseteq K_0, \\]

then there is a square matrix \\(T\in\mathbb C^{k\times k}\\) such that

\\[ AN=NT. \\]

It follows that

\\[ \boxed{H_A=HT.} \\]

This is a right factorization.

Now, since \\(\ker H=V\\), condition (5a) implies

\\[ T(V)\subseteq V. \\]

Therefore \\(V^\perp\\) is invariant under the dual action of \\(T\\). If \\(\omega>0\\), this is a nonzero complex invariant subspace, so it contains a left eigenvector. That eigenvector gives a nonzero left null vector of \\(P(\lambda)\\) for some \\(\lambda\\).

The distinction is therefore:

| Hypothesis                | Factorization | Consequence                                     |
| ------------------------- | ------------- | ----------------------------------------------- |
| \\(A(V)\subseteq V\\)     | \\(H_A=DH\\)  | \\(D\\) may send \\(W\\) outside \\(W\\)        |
| \\(A(K_0)\subseteq K_0\\) | \\(H_A=HT\\)  | The induced dual action preserves \\(V^\perp\\) |

This is the precise reason the global theorem survives while the local theorem fails.

### 2.3 Corrected rigidity statements

I recommend retaining the following two results.

Local kernel-invariance lemma. If (5a) holds, \\(\omega>0\\), and

\\[ A(V)\subseteq K_0, \\]

then

\\[ \boxed{A(V)\subseteq V.} \\]

This follows from the dimension argument:

\\[ \operatorname{row}H\subseteq(V+AV)^\perp, \\]

so

\\[ k-\dim V=\omega \le k-\dim(V+AV). \\]

Since \\(V\subseteq V+AV\\), equality of dimensions follows.

Global invariant-kernel obstruction. If

\\[ A(K_0)\subseteq K_0,\qquad \omega>0, \\]

then no observer can satisfy both (5a) and (5b).

I would actually state this second theorem for all \\(\omega>0\\), not merely \\(0<\omega\<k\\). The proof also works when \\(c=0\\), because \\(V=\\{0\\}\\) is invariant and \\(V^\perp=K_0^\*\\) is nonzero.

The only excluded boundary is \\(\omega=0\\).

## 3. Question 2: A concrete corrected leakage placement

I agree with the diagnosis of the failed attempt. The problem was not simply that leakage was placed on a coordinate involved in \\(V\\). It was that the resulting induced map on the compressed row space had a rank defect at \\(\lambda=0\\).

The remedy is to use a shift chain ending in a leakage direction, rather than a single isolated leakage arrow.

Here is an explicit construction. It is smaller than the seven-dimensional counterexample in Report 65 and is designed precisely to address the obstruction described in II.3.

### 3.1 A six-dimensional template

Take

\\[ K_0=\operatorname{span}\\{e_1,e_2,e_3,e_4\\} \subset\mathbb C^6, \\]

and define

\\[ C=e_6^\*. \\]

Let \\(A\\) act on the standard basis by

\\[ \begin{aligned} Ae_1&=e_5,\\\ Ae_2&=e_1,\\\ Ae_3&=0,\\\ Ae_4&=0,\\\ Ae_5&=e_6,\\\ Ae_6&=0. \end{aligned} \\]

Then

\\[ CA=e_5^\*, \\]

so

\\[ K_0=\ker\begin{bmatrix}C\\\CA\end{bmatrix} =\operatorname{span}\\{e_1,e_2,e_3,e_4\\}. \\]

Notice that

\\[ A(K_0)\not\subseteq K_0 \\]

because \\(Ae_1=e_5\\), while

\\[ V=\operatorname{span}\\{e_3,e_4\\} \\]

satisfies

\\[ A(V)=\\{0\\}\subseteq V. \\]

Now choose

\\[ L_0=e_1^\* \\]

and

\\[ L= \begin{bmatrix} e_1^\*\\\ e_2^\*\\\ e_1^\*+e_2^\*+e_5^\* \end{bmatrix}. \\]

Thus \\(q=3\\), \\(p=1\\), and

\\[ \operatorname{rank}[C;L]=4=p+q. \\]

With \\(N=[e_1,e_2,e_3,e_4]\\), we obtain

\\[ H=LN= \begin{bmatrix} 1&0&0&0\\\ 0&1&0&0\\\ 1&1&0&0 \end{bmatrix} \\]

and

\\[ H_A=LAN= \begin{bmatrix} 0&1&0&0\\\ 0&0&0&0\\\ 1&1&0&0 \end{bmatrix}. \\]

Consequently,

\\[ \ker H=\operatorname{span}\\{e_3,e_4\\}=V, \qquad \operatorname{rank}H=2. \\]

### 3.2 Exact pencil verification

The compressed pencil is

\\[ P(\lambda)= \begin{bmatrix} \lambda&-1&0&0\\\ 0&\lambda&0&0\\\ \lambda-1&\lambda-1&0&0 \end{bmatrix}. \\]

Its first two columns have minors

\\[ \lambda^2,\qquad \lambda^2-1,\qquad -\lambda(\lambda-1). \\]

The first two have no common complex root. Therefore

\\[ \boxed{\operatorname{rank}P(\lambda)=2 \quad\forall\lambda\in\mathbb C.} \\]

The full rank checks are

\\[ \operatorname{rank}[LA;L;CA;C] = \operatorname{rank}[L;CA;C] =4. \\]

Thus this is an explicit feasible observer with

\\[ A(V)\subseteq V,\qquad A(K_0)\not\subseteq K_0,\qquad \omega=2>0. \\]

It also satisfies \\(\mathsf P\_{\mathrm{ind}}\\).

Explicit feasible template

### 3.3 Why this construction works

The key is the chain

\\[ \boxed{e_2\longmapsto e_1\longmapsto e_5.} \\]

- \\(e_2\mapsto e_1\\) supplies a nontrivial compressed transition.
- \\(e_1\mapsto e_5\\) supplies leakage out of \\(K_0\\).
- The row \\(e_1^\*+e_2^\*+e_5^\*\\) detects the leakage coordinate.
- The resulting induced map on \\(W=\operatorname{im}H\\) is a shift that has no eigenvector in \\(W\\).

In the attempted construction from Report 65, the leakage direction did not create a full-rank transition on the entire quotient \\(K_0/V\\). Here, the second quotient direction feeds into the first, and the first feeds into the leakage coordinate.

My concrete recommendation is therefore to retain the original chart variables but replace the isolated leakage arrow by a shift chain on the quotient coordinates.

For a graph chart, this means:

1. Keep the graph subspace \\(V=\operatorname{graph}(X)\\) in the arithmetic block.
2. Reserve at least two quotient directions outside \\(V\\).
3. Send the first quotient direction into a leakage coordinate.
4. Send the second quotient direction into the first.
5. Include the leakage coordinate in an appropriate lift row.

This gives a starting point for a construction in which the graph invariance equations encode the desired arithmetic relation while the shift chain handles the pencil condition.

It is not yet an arithmetic multiplication gadget, but it is a verified feasible spectral template.

## 4. Question 3: Is there a further rigidity theorem?

There is a useful further restriction, but it does not prohibit the invariant-subspace gadget.

### 4.1 A necessary condition: \\(q>\omega\\)

Suppose

\\[ A(V)\subseteq V \\]

and (5a) holds. As shown above, there is a map

\\[ \Delta:W\to\mathbb C^q,\qquad W=\operatorname{im}H, \\]

such that

\\[ H_A=\Delta H. \\]

The pencil is good exactly when

\\[ \Delta w\ne\lambda w \qquad \text{for every }0\ne w\in W,\ \lambda\in\mathbb C. \\]

If \\(q=\omega\\), then

\\[ W=\mathbb C^q. \\]

The map \\(\Delta\\) is then an endomorphism of a nonzero finite-dimensional complex vector space. It necessarily has an eigenvector. Thus the pencil must fail.

Therefore

\\[ \boxed{ A(V)\subseteq V,\quad (5a),(5b),\quad\omega>0 \quad\Longrightarrow\quad q>\omega. } \\]

This is a genuine additional rigidity theorem.

It is also consistent with the counterexample: \\(q=3\\), \\(\omega=2\\).

### 4.2 Exact spectral criterion

For invariant \\(V\\), the entire pencil issue is captured by

\\[ \boxed{ \ker(\Delta-\lambda I\_{\\!W})=\\{0\\} \quad\forall\lambda\in\mathbb C, } \\]

where the notation means

\\[ \\{w\in W:\Delta w=\lambda w\\}=\\{0\\}. \\]

Equivalently, \\(W\\) must contain no eigenvector of the ambient extension of \\(\Delta\\).

This is a useful way to think about the pencil:

- The map \\(\Delta\\) is not necessarily an endomorphism of \\(W\\).
- It can send \\(W\\) outside itself.
- The pencil is good if it never sends a nonzero \\(w\in W\\) to a scalar multiple of itself.

The shift construction in Section 3 is a particularly simple way to guarantee this.

### 4.3 A general spectral-padding construction

The six-dimensional example generalises.

Let

\\[ k=c+\omega,\qquad q=\omega+1. \\]

Choose a basis of \\(K_0\\) consisting of

\\[ v_1,\ldots,v_c,\ x_0,\ldots,x\_{\omega-1}. \\]

Extend the ambient space by two further vectors \\(g,z\\).

Define

\\[ C=z^\* \\]

and let \\(A\\) act as

\\[ Av_j=0,\qquad Ax_i=x\_{i+1}\quad(0\le i<\omega-1), \\]

\\[ Ax\_{\omega-1}=g,\qquad Ag=z,\qquad Az=0. \\]

Then

\\[ CA=g^\*, \\]

and therefore

\\[ K_0=\operatorname{span}\\{v_1,\ldots,v_c,x_0,\ldots,x\_{\omega-1}\\}. \\]

Set

\\[ V=\operatorname{span}\\{v_1,\ldots,v_c\\}. \\]

Then

\\[ A(V)=0,\qquad A(K_0)\not\subseteq K_0. \\]

Choose \\(L\\) with rows

\\[ x_0^\*,x_1^\*,\ldots,x\_{\omega-1}^\*,g^\*. \\]

The first row can be prescribed as \\(L_0=x_0^\*\\).

The compressed matrix \\(H\\) maps

\\[ x_i\longmapsto e_i\in\mathbb C^{\omega+1} \\]

and annihilates \\(V\\). Hence

\\[ \operatorname{rank}H=\omega,\qquad\ker H=V. \\]

The induced map on \\(W=\operatorname{span}\\{e_0,\ldots,e\_{\omega-1}\\}\\) is the shift

\\[ e_0\mapsto e_1\mapsto\cdots\mapsto e\_{\omega-1}\mapsto e\_\omega. \\]

Its only eigenvectors in the ambient space lie in the direction \\(e\_\omega\\), which is outside \\(W\\). Therefore the compressed pencil has full column rank for every \\(\lambda\\).

This gives a systematic spectral-padding family, not just an isolated numerical example.

### 4.4 What this says about the arithmetic gadget

The invariant-subspace gadget is feasible in principle. The remaining difficulty is to make the same matrix \\(A\\) perform two jobs:

1. encode the desired nonlinear incidence relation on the graph variables;
2. produce a pencil-good induced map on the compressed row space.

The general shift construction solves the second job for a prescribed invariant \\(V\\). It does not automatically solve it uniformly over all candidate graph subspaces \\(V(X)\\).

That distinction matters for a reduction. A valid reduction must guarantee pencil goodness for every source assignment that is supposed to be accepted, and must not introduce unintended feasible assignments.

I would therefore describe the shift chain as a spectral padding gadget. The next task is to couple it to the multiplication gadget without changing the intended graph-invariance equations.

## 5. Question 4: Is there an additional simultaneous-lift obstruction?

The proposed fibre description is correct, but the solver should distinguish two parameterisations:

1. prescribe only the first compressed row \\(h=lN\\);
2. prescribe the entire compressed pair \\((lN,lAN)\\).

The corresponding lift freedoms are different.

### 5.1 The admissible row space

Write

\\[ \widehat V=NV\subseteq K_0. \\]

For an ambient row \\(l\in(\mathbb C^n)^\*\\), the rowwise form of (5a) is

\\[ l|\_{\widehat V}=0,\qquad l|\_{A\widehat V}=0. \\]

Therefore the admissible ambient rows form

\\[ \boxed{ \mathcal L_V=(\widehat V+A\widehat V)^\perp. } \\]

Since \\(\widehat V\subseteq K_0\\),

\\[ K_0^\perp=\operatorname{row}[C;CA]. \\]

Let

\\[ \mathcal R=K_0^\perp,\qquad \mathcal C=\operatorname{row}C. \\]

For a prescribed compressed first row \\(h\\), choose a representative \\(l_h^0\\) satisfying

\\[ l_h^0N=h. \\]

All lifts with the same \\(h\\) have the form

\\[ l_h^0+g,\qquad g\in\mathcal R. \\]

Imposing the additional admissibility condition gives

\\[ g|\_{A\widehat V}=-l_h^0|\_{A\widehat V}. \\]

Thus the fibre is

\\[ \boxed{ l_h^0+ \\{g\in\mathcal R: g|\_{A\widehat V}=-l_h^0|\_{A\widehat V}\\}. } \\]

The direction of this affine fibre is

\\[ \boxed{ \mathcal G_V=\mathcal R\cap(A\widehat V)^\perp. } \\]

This is the correct fixed-\\(h\\) fibre description.

### 5.2 The simultaneous independence criterion for fixed \\(h_i\\)

Suppose the first compressed rows \\(h_1,\ldots,h_m\\) are prescribed and each has at least one admissible lift \\(l_i^0\\).

For each bottom row, its admissible lifts are

\\[ l_i^0+\mathcal G_V. \\]

Now quotient by the row space of \\(C\\):

\\[ Q=(\mathbb C^n)^\*/\mathcal C. \\]

Let \\(F\subseteq Q\\) be the span of the fixed top-row classes, and write

\\[ \bar{\mathcal G}\_V=(\mathcal G_V+\mathcal C)/\mathcal C. \\]

Let \\(\bar l_i^0\\) denote the class of \\(l_i^0\\) in \\(Q\\).

Assuming the fixed top rows are independent modulo \\(\mathcal C\\), there exist choices of the \\(m\\) bottom lifts that are jointly independent modulo \\(\mathcal C\\) if and only if

\\[ \boxed{ \dim\left( \frac{F+\bar{\mathcal G}\_V+ \operatorname{span}\\{\bar l_1^0,\ldots,\bar l_m^0\\}} {F} \right)\ge m. } \\]

This is an affine independent-representative criterion.

It is more informative than merely checking the dimension of the homogeneous lift space: the affine base classes matter too.

The criterion is exact because all bottom rows have the same direction space \\(\bar{\mathcal G}\_V\\). If the affine span generated by the available directions and base representatives has dimension at least \\(m\\), the representatives can be chosen independently; if not, they cannot.

For the full-row-rank convention \\(\mathsf P\_{\mathrm{full}}\\), the same argument applies without quotienting by \\(\mathcal C\\). One simply tests independence in the full ambient dual space.

### 5.3 What if the entire pair \\((h,h_A)\\) is prescribed?

Now consider

\\[ \Psi: (\mathbb C^n)^\*/\mathcal C \longrightarrow K_0^\*\oplus K_0^\*, \qquad \bar l\mapsto(lN,lAN). \\]

If the pair \\((h,h_A)\\) is prescribed, all lifts differ by

\\[ \ker\Psi. \\]

Every element of \\(\ker\Psi\\) annihilates both \\(K_0\\) and \\(A(K_0)\\), and therefore also annihilates \\(\widehat V+A\widehat V\\). Thus

\\[ \ker\Psi\subseteq\mathcal L_V \\]

at the level of lift directions.

Consequently, if the full compressed pair matrix \\(Z\_{\mathrm{pair}}\\) is prescribed, the earlier criterion

\\[ \boxed{ \dim\ker\Psi \ge \dim\ker Z\_{\mathrm{pair}} } \\]

remains the relevant simultaneous-completion criterion, under the assumption that the fixed top rows are independent modulo \\(\mathcal C\\).

So there is no additional independent admissibility obstruction once the entire pair is fixed and belongs to the image of \\(\Psi\\).

### 5.4 What should be added to the solver?

I recommend including both branches explicitly:

| Solver parameterisation                    | Lift direction                                       | Simultaneous test                           |
| ------------------------------------------ | ---------------------------------------------------- | ------------------------------------------- |
| First compressed rows \\(h_i\\) prescribed | \\(\mathcal G_V=\mathcal R\cap(A\widehat V)^\perp\\) | Affine independent-representative criterion |
| Full pairs \\((h_i,h\_{A,i})\\) prescribed | \\(\ker\Psi\\)                                       | \\(d'\_C\ge\dim\ker Z\_{\mathrm{pair}}\\)   |

Do not apply the two tests cumulatively to the same parameterisation. They describe different levels of what has already been fixed.

My preference is to use the full-pair parameterisation in the exact algebraic solver, because it makes the spectral pencil constraints explicit and retains a clean linear lift theorem. Use the fixed-\\(h\\) fibre description for structural analysis and for identifying when admissibility is automatically solvable.

## 6. Question 5: Should the project prioritise (i), (ii), or (iii)?

My recommendation is (i) and (iii) in parallel, with (ii) treated as a short separate classification task rather than as the main hardness direction.

### 6.1 Why the \\(\omega=0\\) branch is unlikely to yield hardness

When

\\[ \omega=0, \\]

we have

\\[ H=0. \\]

Condition (5a) then gives

\\[ H_A=0. \\]

In ambient terms, every row of \\(L\\) must annihilate both \\(K_0\\) and \\(A(K_0)\\). Thus

\\[ \boxed{ \operatorname{row}L \subseteq (K_0+A(K_0))^\perp. } \\]

Conversely, if every row of \\(L\\) lies in this annihilator, then \\(H=H_A=0\\), and both (5a) and (5b) hold.

Therefore the zero-compressed-rank feasibility problem reduces to extending the fixed rows \\(L_0\\) inside a linear subspace, subject to the selected row-independence convention.

That is a linear-algebraic dimension and rank test. It is not an attractive ETR-hardness source by itself.

It should be classified completely, but I would not devote the main hardness effort to it.

### 6.2 The corrected invariant-subspace route is now viable

The explicit construction in Section 3 gives a useful starting point. The next experiment should combine:

- a graph chart that encodes a polynomial relation;
- an invariant candidate \\(V(X)\\);
- a shift chain on the quotient directions;
- a leakage endpoint outside \\(K_0\\);
- lift rows that detect that endpoint;
- an automatic pencil-goodness proof.

The key challenge is uniformity: the pencil must remain good over the entire intended solution family, not just at one hand-picked \\(V\\).

### 6.3 A concrete next experiment

I suggest the following controlled programme.

Experiment A: chart rotation.

Start from the six-dimensional template and apply invertible changes of basis separately on:

- the candidate invariant subspace \\(V\\);
- its complement in \\(K_0\\);
- the leakage direction;
- the measured direction.

Track the transformed \\(A,C,L_0\\), rather than just rotating the chart coordinates. The goal is to identify which features of the shift construction are basis-invariant and which depend on the chosen coordinate placement.

Experiment B: one multiplication gate.

Add a minimal graph block whose invariance equation contains

\\[ z=xy. \\]

Keep the shift chain in a separate quotient block initially. Do not yet attempt variable sharing or a complete arithmetic circuit.

Experiment C: pencil certification.

For the resulting family, derive a fixed basis of the compressed image \\(W\\) and prove that the induced map has no eigenvector in \\(W\\), independently of the values of \\(x,y,z\\) satisfying the intended gate.

If the pencil proof depends on a genericity assumption or excludes some legitimate source solutions, the gadget is not yet valid.

Experiment D: full lift certification.

Verify that all prescribed compressed row pairs have ambient lifts and that the bottom rows can be completed independently modulo \\(C\\).

This order isolates the main difficulties and avoids confusing a failed lift with a failed arithmetic encoding.

### 6.4 Consolidation should proceed at the same time

Report 65 should be incorporated into the structural paper immediately. The revised results should be:

1. the global invariant-\\(K_0\\) obstruction;
2. the local kernel-invariance lemma;
3. the exact induced rectangular-pencil criterion;
4. the necessary condition \\(q>\omega\\) for invariant \\(V\\);
5. the explicit feasible invariant-\\(V\\), non-invariant-\\(K_0\\) construction;
6. the corrected lift-fibre and simultaneous-completion criteria;
7. the linear-algebraic classification of \\(\omega=0\\).

This is a coherent set of mathematical results, even before hardness is settled.

## 7. Revised research decision tree

The earlier decision tree should now be replaced by the following.

Start with a candidate \\(V=\ker H\\).

Case 1: \\(\omega=0\\)

Reduce to the linear subspace

\\[ (K_0+AK_0)^\perp \\]

and test row completion.

Case 2: \\(\omega>0\\) and \\(A(K_0)\subseteq K_0\\)

Infeasible

Global invariant-kernel obstruction.

Case 3: \\(\omega>0\\) and \\(A(V)\subseteq K_0\\)

Condition (5a) forces

\\[ A(V)\subseteq V. \\]

Then write

\\[ H_A=DH. \\]

- If \\(q=\omega\\), infeasible.
- If \\(q>\omega\\), test whether \\(\operatorname{im}H\\) contains an eigenvector of the induced map.

The shift-chain construction shows this branch can be feasible.

Case 4: \\(\omega>0\\) and \\(A(V)\not\subseteq K_0\\)

Use the full ambient row-lift constraints and test the pencil directly through the eigenspace-injectivity criterion.

Final step in Cases 3 and 4

Verify:

- simultaneous row lifts;
- the selected row-independence convention;
- exact original rank equalities (5a) and (5b).

## 8. Final judgement and next deliverable

Report 65 is correct to reject the local leakage-rigidity conclusion. The supplied counterexample is valid, and the previous review should be corrected accordingly.

More importantly, the report has opened a concrete route forward. The six-dimensional shift-chain construction demonstrates that:

\\[ \boxed{ A(V)\subseteq V,\quad A(K_0)\not\subseteq K_0,\quad \omega>0 } \\]

is compatible with both observer rank conditions, even under \\(\mathsf P\_{\mathrm{ind}}\\).

The strongest new general statement is the necessary condition

\\[ \boxed{ A(V)\subseteq V,\quad (5a),(5b),\quad\omega>0 \quad\Longrightarrow\quad q>\omega. } \\]

The most promising gadget architecture is therefore:

- encode arithmetic through invariance of a graph subspace;
- make \\(K_0\\) globally non-invariant by a controlled leakage chain;
- use the chain to keep the compressed image \\(W\\) free of eigenvectors;
- handle simultaneous row completion through the exact affine-fibre criterion.

I would make the six-dimensional template the starting point for the next systematic search, not return to the previous isolated-leakage construction. It is small, exact, rational, satisfies the stronger independence convention, and has an easily verifiable pencil certificate.

The immediate next milestone should be a one-gate construction that combines the graph equation with this shift-chain spectral padding. Only after that succeeds should the project move to variable sharing and a full ETR reduction.