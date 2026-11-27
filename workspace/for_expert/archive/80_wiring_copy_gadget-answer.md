# Audit of the wiring report

The row-wise nature of column overlap is not the fundamental obstruction. Cross-row transfer is possible through the global row-space condition, and there is a compact projective representation of multiplication that gives a useful alternative to the proposed formatter.

However, there is a more basic issue that must be resolved before the gate library can support a hardness reduction:

> The displayed multiplication gate is a full-observer realization of a particular compressed witness, but it has not yet been shown to be a sound q1 gadget under arbitrary \\(R\\).

This is not a minor technicality. The universal lift permits every free row-pair to vary independently, including rows that the proposed gate writes as zero. I will demonstrate the issue explicitly, then give a compressed two-gate construction that shows how the wiring could work geometrically.

## 0. A necessary correction: the multiplication gate is not yet sound as a q1 gadget

The universal lift in II.1 is correct. But it has a consequence that is easy to overlook: for every free row \\(r_i\\), the pair

\\[ (H_i,H\_{A,i})=(r_iN,r_iAN) \\]

can be chosen arbitrarily in \\(\mathbb R^k\times\mathbb R^k\\).

In particular, the zero entries in the proposed multiplication gate are not automatically constraints. They are merely values chosen for one particular witness.

Consider II.2. Its fixed data have

\\[ H_0=\begin{bmatrix}e\\\e\end{bmatrix}, \qquad H\_{A,0}=\begin{bmatrix}0\\\e\end{bmatrix}, \\]

where \\(e=(1,0,0)\\). Choose the entirely legitimate free-row assignment

\\[ R=0. \\]

Then

\\[ H=\begin{bmatrix}e\\\e\\\0\\\0\end{bmatrix}, \qquad H_A=\begin{bmatrix}0\\\e\\\0\\\0\end{bmatrix}, \\]

and

\\[ P(\lambda)= \begin{bmatrix} \lambda e\\\ (\lambda-1)e\\\ 0\\\ 0 \end{bmatrix}. \\]

For every complex \\(\lambda\\), at least one of \\(\lambda\\) and \\(\lambda-1\\) is nonzero. Therefore

\\[ \operatorname{rank}P(\lambda)=1=\operatorname{rank}H \quad\forall\lambda. \\]

Condition (5a) also holds. Thus the q1 instance described by this \\(A,C,L_0\\) is feasible without imposing any condition whatsoever on \\(x,y,z\\).

The issue is that the displayed calculation for II.2 fixes the free rows to have the forms

\\[ H_3=(0,1,x),\quad (H_A)\_3=(0,y,z),\quad H_4=0,\quad (H_A)\_4=(0,\beta,\beta x). \\]

Under those restrictions, the calculation is correct. But q1 does not impose those restrictions on \\(R\\). In q1, \\(x,y,z,\beta\\), and the other entries of the free rows are all witness coordinates. A solution is allowed to choose a different rank stratum, or to choose the rows intended to be zero to be nonzero.

This distinction should be reflected in the report:

- Full-observer realization: a specified compressed pair has been realized by actual \\(A,C,L_0,R\\).
- Sound q1 gadget: every feasible \\(R\\) for the fixed \\(A,C,L_0\\) obeys the intended decoded relation.

II.2 establishes the first, but not the second. The same distinction applies to any composition based on zero free rows.

The input-controlled nonzero construction in II.3 is different. There, the fixed row makes the pencil lose rank at \\(\lambda=0\\) when \\(x=0\\), and arbitrary choices of \\(R\\) cannot repair that loss. That is why its equivalence

\\[ \exists R:\ (5a)\wedge(5b)\iff x\ne0 \\]

is a genuine q1 feasibility statement.

This soundness distinction will matter in all five questions below.

## 1. Copy/format: is \\((0,y,z)\mapsto(0,1,z)\\) possible?

There is no general impossibility theorem for a multi-row observer gadget, but the literal formatter is not achievable by simple row proportionality or a single column-overlap copy.

### 1.1 Why simple proportionality does not perform the requested format

Suppose the source and target are required to represent the same row direction:

\\[ (0,y,z)\sim(0,1,z). \\]

In the last two coordinates, this requires

\\[ (y,z)=\alpha(1,z). \\]

Consequently,

\\[ z(y-1)=0. \\]

It does not hold for arbitrary \\(y,z\\). When \\(z\ne0\\), it forces \\(y=1\\).

This is exactly the degeneracy encountered when one identifies the whole output row of the first gate with the normalized input row of the next gate.

Column overlap does not fix this. If \\(AN_j=N_l\\), then

\\[ (H_A)\_{i,j}=H\_{i,l}; \\]

this copies a coordinate between \\(H_A\\) and \\(H\\) within row \\(i\\). It does not perform the nonlinear normalization needed to turn \\(y\\) into \\(1\\) while retaining \\(z\\).

A larger incidence construction might implement an affine chart change, but the report does not yet contain such a construction. In particular, there is no justified claim about the smallest \\(k\\) for a general copy/format gadget.

### 1.2 A better solution: redesign the multiplication output as a projective wire

I would avoid trying to format \\((0,y,z)\\) after the first gate. Instead, change the local multiplication representation so that its output is already in a format suitable for another gate.

In \\(\mathbb R^3\\), define

\\[ a=(1,x,0),\qquad b=(0,1,y),\qquad c=(1,0,-z). \\]

Then

\\[ \det\begin{bmatrix} 1&x&0\\\ 0&1&y\\\ 1&0&-z \end{bmatrix} =xy-z. \\]

Since \\(a,b\\) are always linearly independent,

\\[ \boxed{ c\in\operatorname{span}\\{a,b\\} \iff z=xy. } \tag{7} \\]

This is a useful local multiplication incidence. Its output is \\(c=(1,0,-z)\\). Apply the fixed signed coordinate permutation

\\[ T(u,v,w)=(v,u,-w). \\]

Then

\\[ T(c)=(0,1,z). \\]

So the output of this multiplication relation can be made into the input format required by the next gate merely by changing the coordinate frame. No data-dependent normalization is needed.

Useful compressed primitive

The local determinant construction uses \\(k=3\\), and \\(k=3\\) is minimal for this particular three-vector, codimension-one incidence construction: in dimension two, two independent carrier vectors already span the entire ambient space, so membership of a third vector would impose no condition.

This is not a proof that \\(k=3\\) is the minimum for every possible observer copy/format gadget. Nor, by itself, is (7) a sound q1 multiplication gadget. It is a better compressed representation of the arithmetic relation, and it suggests the correct wiring abstraction: pass a projective vector or line, rather than trying to copy one selected scalar entry and normalize another.

## 2. Is the row-wise limitation of column overlap fundamental?

No. Column overlap is row-wise, but (5a) is a global row-space condition and permits cross-row mixing.

There is a simple exact example.

Take

\\[ H=\begin{bmatrix} 1&0\\\ 0&1\\\ 0&0 \end{bmatrix}, \qquad H_A=\begin{bmatrix} 0&0\\\ 1&0\\\ 0&1 \end{bmatrix}. \\]

Both matrices have row space \\(\mathbb R^2\\), so (5a) holds. The pencil is

\\[ P(\lambda)= \begin{bmatrix} \lambda&0\\\ -1&\lambda\\\ 0&-1 \end{bmatrix}. \\]

The minor formed by rows 2 and 3 is

\\[ \det\begin{bmatrix} -1&\lambda\\\ 0&-1 \end{bmatrix}=1. \\]

Therefore

\\[ \operatorname{rank}P(\lambda)=2 \quad\forall\lambda\in\mathbb C. \\]

Here

\\[ H_1=(1,0),\quad H_2=(0,1),\quad H_3=0, \\]

while

\\[ (H_A)\_2=H_1,\qquad (H_A)\_3=H_2. \\]

The third row transfers a direction despite having zero \\(H\\)-row.

In fact, this is a shift:

\\[ H_A=FH,\qquad F=\begin{bmatrix} 0&0&0\\\ 1&0&0\\\ 0&1&0 \end{bmatrix}. \\]

The off-diagonal entries of \\(F\\) express cross-row mixing.

There is a general identity behind this example. From (5a),

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H. \\]

From (5b) at \\(\lambda=0\\),

\\[ \operatorname{rank}H_A=\operatorname{rank}H. \\]

Consequently,

\\[ \boxed{\operatorname{row}H_A=\operatorname{row}H.} \tag{8} \\]

Thus the two matrices generate the same subspace, even though their rows need not match one by one. A row of \\(H_A\\) can be a linear combination of several different rows of \\(H\\).

What this establishes: cross-row transfer is compatible with both (5a) and (5b). So column overlap is not the only conceivable wiring mechanism.

What it does not establish: that q1 forces a particular row of \\(H_A\\) to equal a particular row of \\(H\\). The shift above is a feasible compressed pair. It is not automatically a sound gadget, because arbitrary free rows might produce other feasible pairs.

A good distinction is:

- Column overlap gives a structural, row-wise identity.
- Row-space containment gives a global, potentially cross-row linear dependence.
- A wiring gadget must make the desired dependence unavoidable in every feasible solution, not merely possible in one selected witness.

## 3. Can the two-gate series be realized?

At the compressed incidence level, yes. There is a clean global construction that avoids the literal formatter and shows how two multiplication relations can share a wire through a common row space.

It is not yet a sound full q1 reduction, for reasons I explain below.

### 3.1 A global subspace construction

Work in \\(\mathbb R^4\\), with standard basis \\(e_1,e_2,e_3,e_4\\). Define

\\[ \begin{aligned} a_1&=e_1+x_1e_2,\\\ b_1&=e_2+y_1e_3,\\\ a_2&=e_4+x_2e_1,\\\ c_1&=e_1-z_1e_3,\\\ c_2&=e_4+z_2e_3. \end{aligned} \\]

Let

\\[ W=\operatorname{span}\\{a_1,b_1,a_2\\}. \\]

The three generators are linearly independent for every \\(x_1,y_1,x_2\\).

First consider \\(c_1\\). If

\\[ c_1=\alpha a_1+\beta b_1+\gamma a_2, \\]

comparison of the \\(e_4\\) coordinate gives \\(\gamma=0\\). The \\(e_1\\) coordinate gives \\(\alpha=1\\), and the \\(e_2\\) coordinate gives \\(\beta=-x_1\\). The \\(e_3\\) coordinate then gives

\\[ -z_1=-x_1y_1. \\]

Hence

\\[ \boxed{c_1\in W\iff z_1=x_1y_1.} \tag{9} \\]

Now consider \\(c_2\\). If

\\[ c_2=\alpha a_1+\beta b_1+\gamma a_2, \\]

the \\(e_4\\) coordinate gives \\(\gamma=1\\). The \\(e_1\\) coordinate gives \\(\alpha=-x_2\\), and the \\(e_2\\) coordinate gives \\(\beta=x_1x_2\\). Finally, the \\(e_3\\) coordinate gives

\\[ z_2=x_1x_2y_1. \\]

Combining this with (9),

\\[ \boxed{c_2\in W\iff z_2=x_2z_1,} \tag{10} \\]

provided the first relation is also imposed.

This is a genuine global wiring pattern. The second gate does not need a separately copied scalar \\(z_1\\): the line representing the first output is already the relevant direction in the common row space.

Geometrically, the first gate uses

\\[ E_1=\operatorname{span}\\{e_1,e_2,e_3\\}, \\]

and the second uses

\\[ E_2=\operatorname{span}\\{e_1,e_3,e_4\\}. \\]

Their common coordinate plane is

\\[ S=E_1\cap E_2=\operatorname{span}\\{e_1,e_3\\}. \\]

The first gate's carrier plane intersects \\(S\\) in the wire direction

\\[ e_1-z_1e_3. \\]

The second gate uses precisely that direction as its second input. This is the subspace-gluing version of the projective format change.

### 3.2 A compressed pencil that also satisfies (5b)

The spectral condition can be satisfied very simply in this compressed construction.

Set

\\[ H= \begin{bmatrix} a_1\\\ b_1\\\ a_2\\\ 0\\\ 0\\\ 0 \end{bmatrix}, \qquad H_A= \begin{bmatrix} 0\\\ a_1\\\ b_1\\\ a_2\\\ c_1\\\ c_2 \end{bmatrix}. \tag{11} \\]

Then

\\[ \operatorname{rank}H=3. \\]

Condition (5a) is equivalent to \\(c_1,c_2\in W\\), which by (9)–(10) gives the two desired multiplication relations.

On that locus, the pencil rows are

\\[ \begin{aligned} &\lambda a_1,\\\ &\lambda b_1-a_1,\\\ &\lambda a_2-b_1,\\\ &-a_2,\\\ &-c_1,\\\ &-c_2. \end{aligned} \\]

Relative to the basis \\((a_1,b_1,a_2)\\), the coefficient matrix of rows 2, 3, and 4 is

\\[ \begin{bmatrix} -1&\lambda&0\\\ 0&-1&\lambda\\\ 0&0&-1 \end{bmatrix}, \\]

whose determinant is \\(-1\\). All pencil rows lie in \\(W\\), and these three rows span \\(W\\), so

\\[ \boxed{\operatorname{rank}P(\lambda)=3 \quad\forall\lambda\in\mathbb C.} \\]

Thus (11) is an exact compressed two-gate series construction.

### 3.3 Why this is still not a sound q1 series gadget

The zero rows in (11) are part of the displayed compressed witness. In a q1 instance, unless the corresponding rows are fixed or otherwise constrained, they are free rows of \\(R\\).

That creates an immediate way to bypass the intended multiplication equations: promote the proposed output rows \\(c_1,c_2\\) into additional generators of \\(\operatorname{row}H\\).

For example, take the false assignment

\\[ x_1=0,\quad y_1=0,\quad z_1=1,\qquad x_2=0,\quad z_2=2. \\]

The intended equations both fail. But set

\\[ a_1=e_1,\quad b_1=e_2,\quad a_2=e_4,\quad c_1=e_1-e_3,\quad c_2=e_4+2e_3 \\]

and choose the six \\(H\\)-rows and \\(H_A\\)-rows as

\\[ H= \begin{bmatrix} a_1\\\b_1\\\a_2\\\c_1\\\c_2\\\0 \end{bmatrix}, \qquad H_A= \begin{bmatrix} 0\\\a_1\\\b_1\\\a_2\\\c_1\\\c_2 \end{bmatrix}. \tag{12} \\]

Now \\(H\\) has rank 4, and (5a) holds automatically because its row space is all of \\(\mathbb R^4\\).

Furthermore, the submatrix of \\(P(\lambda)\\) formed by rows 3 through 6 is

\\[ \begin{bmatrix} 0&-1&0&\lambda\\\ \lambda&0&-\lambda&-1\\\ -1&0&2\lambda+1&\lambda\\\ 0&0&-2&-1 \end{bmatrix}. \\]

Its determinant is the constant \\(-2\\). Therefore

\\[ \operatorname{rank}P(\lambda)=4=\operatorname{rank}H \quad\forall\lambda\in\mathbb C. \\]

So (12) is feasible even though both intended product equations are false.

This is an exact soundness counterexample to the unrestricted compressed construction (11): allowing the rows written as zero to become free generators can make both output incidences automatic, while preserving (5b).

Answer to Question 3: two-gate series composition is possible at the compressed subspace level, as (11) shows. The report does not yet establish a sound full q1 series gadget. There is no general no-go theorem here; the explicit failure is a soundness failure of the current implementation, not a mathematical impossibility of wiring.

## 4. What composition primitive should replace row copy?

I recommend projective subspace ports with shared intersections, not scalar copy and not whole-row equality.

There are three levels of representation to distinguish.

### 4.1 Scalar representation

The original approach represents a wire by a selected coordinate \\(z\\). This creates a formatting problem: a later gate wants \\((0,1,z)\\), while the previous gate produces \\((0,y,z)\\).

A literal scalar copy asks for equality of particular entries across different rows. Column overlap cannot do that.

### 4.2 Projective representation

Instead, represent a scalar \\(z\\) by a one-dimensional subspace, for example

\\[ \ell_z=\operatorname{span}\\{(1,0,-z)\\}. \\]

A nonzero scalar multiple is the same wire. This removes unnecessary normalization constraints.

The signed coordinate permutation

\\[ (1,0,-z)\longmapsto(0,1,z) \\]

shows that the same projective wire can be used in a different local coordinate frame.

### 4.3 Subspace-gluing representation

For a circuit, make each gate occupy a local coordinate subspace \\(E_j\\). Adjacent gates share a port subspace. The actual wire is represented by a line in that shared port, and the two local gate subspaces meet precisely along that line.

The two-gate construction in Section 3 is an example:

\\[ E_1\cap E_2=\operatorname{span}\\{e_1,e_3\\}, \\]

and the shared direction is

\\[ \operatorname{span}\\{e_1-z_1e_3\\}. \\]

This is a better abstraction than copying a scalar between rows. It also suggests how to handle fan-out: a single projective line can belong to several local gate subspaces.

However, the crucial requirement is that the intended intersections must be forced by the whole row-space configuration. It is not enough to draw the local subspaces and assume other free rows respect them.

## 5. Soundness: how should a genuine circuit semantics be enforced?

The answer is not to restrict \\(R\\) externally. In q1, \\(R\\) is unrestricted. A reduction must make the desired structure follow from the fixed data and the two rank conditions for every feasible \\(R\\).

I would use a global linear-algebra encoding, with the following proof obligations.

### 5.1 Never treat a free zero row as a fixed zero row

This is the immediate lesson from (11)–(12).

If a free row is displayed as

\\[ H_i=0,\qquad (H_A)\_i=g, \\]

then one must explain why every feasible solution has \\(H_i=0\\), or prove that allowing \\(H_i\ne0\\) cannot invalidate the decoded constraints.

The universal lift does not force this. It makes the pair \\((H_i,(H_A)\_i)\\) arbitrary.

A useful general warning is:

> If an output row \\(g\\) is required to lie in \\(\operatorname{row}H\\), but another free row can simply be chosen equal to \\(g\\), then the intended incidence may become automatic.

This is precisely how the false products in (12) bypass the compressed constraints.

### 5.2 Force the intended rank stratum

The rank

\\[ \omega=\operatorname{rank}H \\]

is not an input to q1. A construction that has been checked only on the stratum \\(\omega=2\\) or \\(\omega=3\\) is incomplete unless the fixed instance forces that stratum, or unless all other strata have been analyzed and excluded.

In particular, (5b) does not mean “use the intended rank.” It only requires the pencil to have the same rank as whatever rank \\(H\\) happens to have.

The identity

\\[ \operatorname{row}H_A=\operatorname{row}H \\]

is useful, but it does not determine \\(\omega\\). A feasible solution may occupy a smaller or larger rank stratum than the intended compressed witness.

I would not rely on the earlier general claim \\(\omega\le r\\) as a substitute for this analysis; the previously supplied proof of that claim had gaps. Any rank bound used in a reduction needs its own valid proof under the exact hypotheses of that construction.

### 5.3 Do not assume block-diagonal \\(R\\)

If \\(A,C\\) are block diagonal, a free row of \\(R\\) can still have components in every block. Those components can combine to produce a larger global row space.

The global condition is

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H, \\]

not a separate containment condition for each diagonal block. Cross-block components can therefore provide directions that a blockwise analysis would miss.

A direct-sum argument is sound only if it proves that every feasible unrestricted \\(R\\) decodes into feasible block witnesses. Showing that block-diagonal \\(R\\) gives a desired witness proves completeness, not soundness.

### 5.4 Use one global row-space invariant

The strongest design direction is:

1. Specify a global row space \\(W\\) generated by the carrier rows.
2. Assign each gate a local coordinate subspace \\(E_j\\).
3. Design the local geometry so that \\(W\cap E_j\\) is exactly the intended carrier subspace for that gate.
4. Require each output vector to lie in \\(W\\); because it is supported in \\(E_j\\), this tests membership in \\(W\cap E_j\\).
5. Make adjacent local subspaces intersect along the projective wire line.
6. Prove that every additional free row either lies in \\(W\\), or would force a violation of (5b).

The two-gate construction in Section 3 is a prototype for steps 1–5. The unresolved part is step 6: obtaining the required local intersections despite unrestricted free-row entries.

### 5.5 Treat the spectral condition as part of the design, not as an afterthought

The shift example suggests a useful spectral scaffold:

\\[ H= \begin{bmatrix} v_1\\\ v_2\\\ \vdots\\\ v\_\omega\\\ 0 \end{bmatrix}, \qquad H_A= \begin{bmatrix} 0\\\ v_1\\\ \vdots\\\ v\_\omega \end{bmatrix}. \\]

Then the pencil rows are

\\[ \lambda v_1,\quad \lambda v_2-v_1,\quad\dots,\quad \lambda v\_\omega-v\_{\omega-1},\quad -v\_\omega. \\]

The last \\(\omega\\) rows have a triangular coefficient matrix with determinant \\((-1)^\omega\\), so the pencil has rank \\(\omega\\) for every \\(\lambda\\).

This is a very simple way to obtain the spectral condition for a specified compressed pair. But it must not be used to smuggle in unforced zero rows or unforced cross-row equalities. If the shift rows are free, their values are part of the soundness problem.

The right approach is to design the shift or another spectral certificate together with the local incidence system, rather than first designing arithmetic blocks and then appending rows that are merely assumed to be zero or copied.

## 6. Answers to the five questions

| Question                 | Answer                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Copy/format gadget    | No sound full q1 formatter is currently established. Simple proportionality cannot implement \\((0,y,z)\mapsto(0,1,z)\\) for arbitrary \\(y,z\\). A better compressed alternative is to output the projective vector \\((1,0,-z)\\), which becomes \\((0,1,z)\\) under a fixed signed coordinate permutation. \\(k=3\\) suffices for this local determinant construction; a general minimum \\(k\\) for an observer formatter is not known. |
| 2. Row-wise limitation   | Not fundamental. The shift pencil gives exact cross-row transfer, including a row with \\(H_i=0\\) and \\((H_A)\_i\ne0\\). But a feasible cross-row pattern is not automatically a gadget enforcing that pattern.                                                                                                                                                                                                                           |
| 3. Two-gate series       | There is an exact compressed global construction, equations (9)–(11), that enforces \\(z_1=x_1y_1\\) and \\(z_2=x_2z_1\\), with (5b) guaranteed by a constant minor. It is not yet a sound full q1 reduction: free rows can enlarge the row space, as the explicit false assignment (12) demonstrates. No general no-go theorem is established.                                                                                             |
| 4. Composition primitive | Use projective wire lines and local subspaces glued along shared intersections. This is preferable to literal scalar copying or whole-row equality. The global row-space geometry must isolate each gate's local incidence.                                                                                                                                                                                                                 |
| 5. Soundness             | Do not restrict \\(R\\), and do not assume block-diagonal \\(R\\). Use one global linear-algebra encoding. Force or robustly control the rank stratum, include all free-row directions in the analysis, and prove that cross-block or extra-row components cannot satisfy the pencil conditions while violating a source gate.                                                                                                              |

## 7. Revised research status

I would revise the report's bottom line as follows.

| Component                     | Status after audit                                                                                                                 |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Universal lift                | Established as a realization map for arbitrary prescribed compressed row pairs. It does not constrain free rows.                   |
| Input-controlled nonzero gate | Sound full q1 feasibility gadget for \\(x\ne0\\).                                                                                  |
| II.2 multiplication pattern   | Exact on its prescribed compressed family, but not yet a sound q1 multiplication gadget under unrestricted \\(R\\).                |
| Column-overlap copy           | Exact row-wise identity; insufficient by itself for cross-row wiring.                                                              |
| Cross-row transfer            | Established at the compressed-pencil level by the shift example.                                                                   |
| Projective multiplication     | Exact local incidence construction using a \\(3\times3\\) determinant.                                                             |
| Two-gate series               | Exact compressed global construction with a constant spectral minor; sound q1 realization remains open.                            |
| Circuit reduction             | Not established. The central missing issue is controlling all unrestricted free rows and rank strata, not merely copying a scalar. |

### Recommended next target

I would pause work on a standalone \\((0,y,z)\mapsto(0,1,z)\\) formatter. The projective multiplication output already gives a better representation: a line can be carried between local coordinate frames without normalizing a scalar.

Instead, formulate and prove the following intermediate theorem:

> Global incidence realization problem. Construct fixed rational \\(A,C,L_0\\) such that every feasible \\(R\\) induces a global row space \\(W\\) whose intersections with designated local coordinate subspaces are exactly the intended gate carrier spaces, and whose feasible projective port lines satisfy the circuit's wire equalities.

The theorem needs both directions: every source circuit solution must yield a feasible \\(R\\), and every feasible unrestricted \\(R\\)—including those with additional nonzero rows and cross-block components—must decode to a source circuit solution.

That is the real wiring problem. The compressed projective construction gives a promising geometric model for it, but the unrestricted-\\(R\\) soundness gap must be closed before describing the gate library as complete or claiming an \\(\exists\mathbb R\\)-hardness reduction.