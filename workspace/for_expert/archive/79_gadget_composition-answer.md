# Audit: the multiplication gate can be lifted

The report is right that witness-variable multiplication is the relevant target for an \\(\exists\mathbb R\\)-reduction. More importantly, I found an explicit construction that lifts a modified version of II.3 to a full observer with one fixed \\(A,C,L_0\\). There is also a simple full-observer construction for the input-controlled nonzero gate in Question 3.

The main remaining difficulty is not making \\(A\\) serve several gates. It is composing the gates so that repeated occurrences of a circuit variable really denote the same witness value, while preventing unintended cross-block solutions.

## 1. Witness-variable multiplication is enough—but only locally

An \\(\exists\mathbb R\\) reduction starts with existentially quantified real variables. The inputs to a multiplication gate and its output are therefore all witness variables:

\\[ x,\ y,\ z\in\mathbb R,\qquad z=xy. \\]

They do not need to be fixed by the target instance. The fixed rational data of the source instance are constants; the unknown values of its variables are what the target witness must encode.

This matches the usual arithmetic formulation of ETR: terms are built from variables and constants using \\(+,-,\cdot\\), and the variables are existentially quantified. Polynomial feasibility remains \\(\exists\mathbb R\\)-complete even when the polynomials have degree at most two. 【turn150226view0†L85-L102】【turn150226view0†L104-L110】

So the right local correctness condition for a multiplication gadget is:

\\[ \exists\text{ auxiliary witnesses}: \quad (5a),(5b) \quad\Longleftrightarrow\quad z=xy. \\]

It is not necessary that \\(x,y,z\\) be entries of the fixed input matrices.

There is, however, an important distinction:

- Local gate correctness: the gadget enforces \\(z=xy\\) on its witness coordinates.
- Circuit correctness: all occurrences of the same source variable are represented by the same value, and the outputs of gates are consistently wired into later gates.

II.3/II.4 address the first issue. They do not yet solve the second. In particular, stacking separate copies with independent variables does not encode a circuit whose gates share wires.

## 2. A general full-observer lifting construction

The report's liftability concern can be resolved much more generally than by testing individual rows.

For any \\(k\ge1\\), split the state space as

\\[ \mathbb R^{3k}=U\oplus V\oplus W, \qquad \dim U=\dim V=\dim W=k, \\]

and choose

\\[ C=\begin{bmatrix}I_k&0&0\end{bmatrix}, \qquad A=\begin{bmatrix} 0&0&I_k\\\ 0&0&0\\\ 0&I_k&0 \end{bmatrix}. \\]

Then

\\[ CA=\begin{bmatrix}0&0&I_k\end{bmatrix}, \qquad K_0=\ker\begin{bmatrix}C\\\CA\end{bmatrix}=V. \\]

Taking

\\[ N=\begin{bmatrix}0\\\I_k\\\0\end{bmatrix} \\]

gives

\\[ AN=\begin{bmatrix}0\\\0\\\I_k\end{bmatrix}, \qquad [N\ AN]= \begin{bmatrix} 0&0\\\ I_k&0\\\ 0&I_k \end{bmatrix}. \\]

Consequently,

\\[ \operatorname{rank}[N\ AN]=2k, \qquad \operatorname{row}[N\ AN]=\mathbb R^{2k}. \\]

This is the key point: the map

\\[ r\longmapsto (rN,rAN) \\]

is surjective onto \\(\mathbb R^{2k}\\). The bound

\\[ \operatorname{rank}[N\ AN]\le n-p \\]

does not preclude that. Here \\(n=3k,\ p=k\\), so the rank is \\(2k=n-p< n\\), but the target of the row map has dimension \\(2k\\), not \\(n\\).

Thus the earlier claim that the row map can never be surjective because its rank is less than \\(n\\) is incorrect. Surjectivity requires rank \\(2k\\), not rank \\(n\\).

In fact, this gives a universal lift. Given any desired fixed compressed rows \\(H_0,H\_{A,0}\\), and any free compressed rows \\(Y,Z\\), set

\\[ L_0=\begin{bmatrix}0&H_0&H\_{A,0}\end{bmatrix}, \qquad R=\begin{bmatrix}0&Y&Z\end{bmatrix}. \\]

Then, with the same fixed \\(A,C\\) above,

\\[ LN=\begin{bmatrix}H_0\\\Y\end{bmatrix}, \qquad LAN=\begin{bmatrix}H\_{A,0}\\\Z\end{bmatrix}. \\]

Conclusion: every compressed pair \\((H,H_A)\\) with prescribed fixed rows and freely chosen remaining row pairs can be lifted using this one fixed \\(A,C\\). The per-row test is exact, but it is not an inherent obstruction: this construction makes every pair pass it.

### A lifted multiplication gadget

The universal lift gives a particularly clean replacement for II.3 that avoids its spectral nondegeneracy problem.

Set \\(k=3\\), \\(n=9\\), \\(p=3\\), and use the fixed \\(A,C\\) above. Let

\\[ e=(1,0,0),\qquad v_x=(0,1,x). \\]

Choose the compressed matrices

\\[ H= \begin{bmatrix} e\\\e\\\v_x\\\0 \end{bmatrix}, \qquad H_A= \begin{bmatrix} 0\\\e\\\\(0,y,z)\\\\(0,\beta,w) \end{bmatrix}. \tag{2} \\]

They are realized by fixed \\(L_0\\) and variable \\(R\\):

\\[ L_0=[\\,0\mid H_0\mid H\_{A,0}\\,], \quad R=[\\,0\mid Y\mid Z\\,], \\]

where

\\[ H_0=\begin{bmatrix}e\\\e\end{bmatrix},\quad H\_{A,0}=\begin{bmatrix}0\\\e\end{bmatrix},\quad Y=\begin{bmatrix}v_x\\\0\end{bmatrix},\quad Z=\begin{bmatrix}(0,y,z)\\\\(0,\beta,w)\end{bmatrix}. \\]

The row space of \\(H\\) is

\\[ \operatorname{row}H=\operatorname{span}\\{e,v_x\\}, \\]

and \\(e,v_x\\) are independent for every real \\(x\\). Therefore

\\[ (5a)\iff z=xy,\quad w=\beta x. \tag{3} \\]

On this locus, the rows of \\(P(\lambda)=\lambda H-H_A\\) are

\\[ \lambda e,\quad(\lambda-1)e,\quad (\lambda-y)v_x,\quad-\beta v_x. \\]

The first two rows always supply the \\(e\\)-direction: \\(\lambda\\) and \\(\lambda-1\\) cannot both vanish. The last two supply the \\(v_x\\)-direction for every \\(\lambda\\) exactly when \\(\beta\ne0\\). If \\(\beta=0\\), they both vanish at \\(\lambda=y\\). Hence

\\[ (5b)\iff\beta\ne0 \quad\text{on the locus (3).} \\]

Consequently, after existentially eliminating \\(\beta,w\\),

\\[ \boxed{ \exists\beta,w:\ (5a)\wedge(5b) \iff z=xy. } \tag{4} \\]

For the reverse direction, simply choose \\(\beta=1,w=x\\).

This is a full observer realization of a multiplication gate, not just a compressed pencil. Its fixed \\(A,C,L_0\\) are explicitly given above; all of \\(x,y,z,\beta,w\\) occur in the free rows \\(R\\).

It also clarifies the status of the original II.3 claim. In II.3 itself, after imposing \\(z=xy,w=\beta x\\), the three maximal minors, up to signs, are

\\[ (\lambda-a)(\lambda-y),\quad \beta(\lambda-a),\quad \alpha(\lambda-y). \\]

Their gcd is \\(1\\) when

\\[ \alpha\beta\ne0,\qquad a\ne y. \\]

Thus the report's spectral statement needs these nondegeneracy conditions; it is not valid for all values of its displayed variables. Construction (2) replaces the potentially problematic condition \\(a\ne y\\) by two fixed anchor rows with distinct constants.

## 3. Input-controlled nonzero: yes, with \\(x\\) in \\(A\\)

There is a very small full-observer construction that answers Question 3 affirmatively.

Take

\\[ C=\begin{bmatrix}0&0&1\end{bmatrix},\qquad A(x)= \begin{bmatrix} 0&0&0\\\ x&0&0\\\ 0&1&0 \end{bmatrix}, \qquad L_0=\begin{bmatrix}1&0&0\end{bmatrix}. \tag{5} \\]

Let the free row be

\\[ R=\begin{bmatrix}u&v&w\end{bmatrix}. \\]

Since

\\[ CA(x)=\begin{bmatrix}0&1&0\end{bmatrix}, \\]

we have, for every \\(x\\),

\\[ K_0=\ker\begin{bmatrix}C\\\CA(x)\end{bmatrix} =\operatorname{span}(e_1),\qquad N=e_1. \\]

In particular, the nullspace basis does not vary with \\(x\\). The compressed matrices are

\\[ H=\begin{bmatrix}1\\\u\end{bmatrix}, \qquad H_A=\begin{bmatrix}0\\\xv\end{bmatrix}. \\]

Thus \\(\operatorname{rank}H=1\\), and (5a) holds automatically. The pencil is

\\[ P(\lambda)= \begin{bmatrix} \lambda\\\ \lambda u-xv \end{bmatrix}. \\]

For \\(\lambda\ne0\\), its rank is automatically one. At \\(\lambda=0\\), its rank is one precisely when \\(xv\ne0\\). Therefore

\\[ \exists R:\ (5a)\wedge(5b) \iff \exists v\in\mathbb R:\ xv\ne0 \iff \boxed{x\ne0.} \tag{6} \\]

This also gives the eigenspace-avoidance interpretation requested in Question 3. A valid choice of \\(F\\) satisfying \\(H_A=FH\\) is

\\[ F= \begin{bmatrix} 0&0\\\ xv&0 \end{bmatrix}. \\]

When \\(xv\ne0\\), its only eigenvalue is \\(0\\), with eigenspace

\\[ E_0(F)=\operatorname{span}\\!\begin{bmatrix}0\\\1\end{bmatrix}. \\]

But

\\[ \operatorname{im}H =\operatorname{span}\\!\begin{bmatrix}1\\\u\end{bmatrix}, \\]

so the two subspaces intersect only at zero. When \\(xv=0\\), \\(F=0\\) and the eigenspace is all of \\(\mathbb R^2\\), which intersects \\(\operatorname{im}H\\) nontrivially.

The important design choice is that \\(N\\) stays fixed while \\(AN=xe_2\\) carries the input parameter. The rank of \\([N\ AN]\\) drops at \\(x=0\\), but the rank of \\(H\\) does not. That is exactly what the two failed attempts in the report did not achieve.

Scope: (6) tests whether a fixed input coefficient \\(x\\) is nonzero. It does not, by itself, test whether a polynomial in unknown witness variables is nonzero. That latter use requires the polynomial value to be represented and wired into a witness-dependent gadget.

## 4. Composition: common \\(A\\) is manageable; naive block sums are not

There are two different issues here.

### 4.1 One global \\(F\\) is not an independent obstruction

Once (5a) holds,

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H. \\]

For each row of \\(H_A\\), choose coefficients expressing it as a linear combination of the rows of \\(H\\). Put those coefficient vectors into the corresponding rows of \\(F\\). This constructs one global matrix satisfying

\\[ H_A=FH. \\]

There is no additional compatibility condition between different rows or different gadgets. If the intended compressed matrices are exactly block diagonal and each block has \\(H_A^{(j)}=F_jH^{(j)}\\), then

\\[ F=\operatorname{diag}(F_1,\ldots,F_s) \\]

works. So global \\(F\\)-consistency is not the central obstruction.

The universal lift in Section 2 makes the point even more directly: the same fixed \\(A,C\\) works for an arbitrary global compressed pair. There is no need to construct one \\(A\\) separately for each multiplication block.

### 4.2 But block-diagonal \\(A,C\\) do not force block-diagonal \\(R\\)

This is a genuine soundness issue.

Consider the two-copy compressed construction, with

\\[ H=\begin{bmatrix}I_2\\\0\_{2\times2}\end{bmatrix}, \qquad H_A=\begin{bmatrix}0\_{2\times2}\\\J\end{bmatrix}, \qquad J=\begin{bmatrix}0&1\\\1&0\end{bmatrix}. \\]

Then

\\[ \operatorname{row}H=\mathbb R^2, \\]

so (5a) holds automatically, and

\\[ P(\lambda)= \begin{bmatrix} \lambda I_2\\\\-J \end{bmatrix} \\]

has rank two for every complex \\(\lambda\\), because \\(J\\) is invertible.

Yet the two diagonal scalar blocks, considered separately, would have zero support parameters and would each fail their own nonzero-pencil test.

This is not just a formal matrix concern. In the direct sum of two copies of II.1, a free row of \\(R\\) has coordinates in both state blocks. Block-diagonal \\(A,C\\) do not prohibit those cross-block components. They can generate the off-diagonal matrix \\(J\\) above.

So the direct-sum identity in II.2 is correct for the displayed block-diagonal compressed matrices. But it does not establish that the unrestricted q1 instance formed by taking block-diagonal \\(A,C\\) is the conjunction of the two individual instances. For that, soundness must cover every unrestricted \\(R\\), including cross-block choices.

### 4.3 A safer composition direction

The lifted gate (2) already gives a genuine shared-\\(A\\) construction. It can also be extended to several products sharing the same factor \\(x\\).

Use two fixed anchor rows \\(e,e\\), one free carrier row

\\[ H_i=v_x,\qquad (H_A)\_i=(0,y_1,z_1), \\]

additional free rows

\\[ H_j=0,\qquad (H_A)\_j=(0,y_j,z_j), \\]

and a final support row

\\[ H_s=0,\qquad (H_A)\_s=(0,\beta,w). \\]

The row-space condition forces

\\[ z_j=xy_j\quad\text{for every }j,\qquad w=\beta x. \\]

Choosing \\(\beta=1,w=x\\) makes the pencil full rank for every \\(\lambda\\), with the two anchors supplying \\(e\\) and the support row supplying \\(v_x\\).

Thus a common factor can be broadcast to multiple product rows without stacking independent q1 instances. This is a promising composition primitive and is compatible with the universal lift.

What it does not yet provide is a general circuit wiring theorem. In an arbitrary circuit, an output of one gate may be an input to many other gates, and those repeated occurrences must be represented by the same scalar. Separate rows or separate diagonal blocks do not automatically identify them. A complete reduction still needs an explicit mechanism for:

- sharing a variable across different gate roles;
- enforcing equality/copy constraints without allowing unintended cross-block solutions;
- encoding the source equations and proving both directions of the reduction.

## 5. Revised status of the four questions

| Question                                             | Assessment                                                                                                                                                                                                        |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Are witness-variable multiplication gates enough? | Yes. They are the correct local target. The missing step is global wire/equality consistency and the reduction's soundness/completeness proof.                                                                    |
| 2. How to lift II.3/II.4?                            | There is a general recipe. The \\(3k\\)-dimensional construction makes the row map onto all compressed row pairs surjective. II.3 can be replaced by the explicit full-observer gate (2).                         |
| 3. Input-controlled nonzero?                         | Yes. Construction (5) gives a full observer with feasibility exactly \\(x\ne0\\), while \\(K_0\\) remains fixed.                                                                                                  |
| 4. Composition with one \\(A\\)?                     | One \\(A\\) is not the main problem. A common \\(A,C\\) can lift the whole compressed system. Naive block-diagonal composition is unsound unless cross-block \\(R\\) is controlled. Variable wiring remains open. |

## Bottom line

There are two substantive upgrades to the report:

1\. The liftability concern is much less restrictive than stated. The rank bound \\(\operatorname{rank}[N\ AN]\le n-p\\) does not prevent surjectivity onto the \\(2k\\)-dimensional compressed row-pair space. The explicit \\(3k\\)-state construction realizes arbitrary compressed pairs and lifts the multiplication gadget to a full observer.

2\. The input-controlled nonzero gate exists. Keeping \\(K_0\\) fixed and putting \\(x\\) in \\(AN\\) gives a full observer feasible exactly when \\(x\ne0\\).

The strongest next research target is now a global wiring/equality gadget, not another isolated multiplication or nonzero gadget. Until that is proved, the constructions establish a useful gate library and full-observer realizations, but not yet \\(\exists\mathbb R\\)-hardness of q1.