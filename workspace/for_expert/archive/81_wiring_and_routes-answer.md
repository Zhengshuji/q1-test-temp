# Audit and route recommendation

The report identifies the right obstruction—unrestricted free rows can enlarge the row space and bypass the intended incidences—but its proposed fixed-subspace no-go is narrower than it may appear. There are two important refinements:

1. A fixed port line really is frozen when two fixed local subspaces already share that line. But fixed local subspaces can have zero intersection, and in a larger ambient space a variable row space can then have a moving one-dimensional intersection with a fixed subspace.
2. There is a concrete way to close the old fixed-\\(q\\) algorithmic sketch: factor \\(H=XB\\), normalize a set of pivot columns of \\(B\\), and eliminate the remaining \\(B\\)-variables by a rank-consistency certificate. This gives a plausible polynomial-time algorithm for every fixed \\(q\\). It is an XP-type result in \\(q\\), not automatically FPT in \\(q\\).

My overall recommendation is to prioritize the algorithmic results while keeping the hardness programme alive as a more focused structural project. I would not yet claim a no-go theorem for multiplication.

## 1. What the fixed-subspace obstruction really proves

Let \\(E_1,E_2\\) be fixed subspaces, and suppose every candidate row space \\(W\\) contains \\(E_1\\). Put

\\[ D=E_1\cap E_2. \\]

Then, for every such \\(W\\),

\\[ D\subseteq W\cap E_2. \tag{1} \\]

This elementary inclusion is the core of port rigidity.

Exact no-go statement. Suppose \\(D\\) is a fixed one-dimensional subspace and the proposed port is the entire intersection \\(W\cap E_2\\). If that intersection is required to be one-dimensional, then

\\[ W\cap E_2=D \\]

for every admissible \\(W\\). The port cannot move.

More generally:

- If \\(\dim D\ge2\\), the intersection cannot be a line at all.
- If \\(\dim D=1\\), any one-dimensional intersection is the fixed line \\(D\\).
- If \\(D=\\{0\\}\\), this argument gives no obstruction.

Thus the report's III.1 conclusion is correct for its particular subspaces. In fact, it follows immediately from (1), without needing the representation \\(W=\operatorname{span}(e_1,e_2,v)\\).

### The missing case: disjoint fixed local subspaces

It is not true that a fixed \\(E_2\\) can never have a moving one-dimensional intersection with a variable \\(W\\) containing fixed \\(E_1\\).

For example, in \\(\mathbb R^5\\), let

\\[ E_1=\operatorname{span}(e_1,e_2),\qquad E_2=\operatorname{span}(e_4,e_5), \\]

and define

\\[ W_t=\operatorname{span}(e_1,e_2,e_3,e_4+t e_5). \\]

Then

\\[ E_1\subseteq W_t,\qquad E_1\cap E_2=\\{0\\}, \\]

but

\\[ \boxed{W_t\cap E_2=\operatorname{span}(e_4+t e_5),} \\]

which is a moving line.

So the correct conclusion is not “fixed local subspaces cannot have moving ports.” It is:

> A fixed port defined as \\(W\cap E_2\\) cannot move as a line if \\(E_1\subseteq W\\) and \\(E_1\cap E_2\\) is already a fixed line. If the fixed local subspaces are disjoint, additional dimensions of \\(W\\) may support a moving intersection.

This distinction matters for the next construction attempt. The three-dimensional port-rigidity example is a minimal-dimensional obstruction, not a general theorem about all subspace arrangements.

### Refining the \\(v_x\\) argument

The report uses

\\[ E_1=\operatorname{span}(e_1,e_2),\qquad v_x=e_2+xe_3\in W. \\]

For \\(x\ne0\\),

\\[ e_3=x^{-1}(v_x-e_2)\in W, \\]

so

\\[ S:=\operatorname{span}(e_1,e_2,e_3)\subseteq W. \\]

If the rank stratum forces \\(\dim W=3\\), then \\(W=S\\) for every \\(x\ne0\\). Every fixed \\(E_2\\) consequently has the same intersection \\(S\cap E_2\\) throughout \\(x\ne0\\). In this minimal-rank regime, the moving-port obstruction is valid.

But if \\(\dim W>3\\), extra directions can create moving intersections, as the \\(\mathbb R^5\\) example illustrates. The additional directions would themselves need to be controlled in a sound q1 construction.

There is also a small wording correction in III.2: to get \\(W\cap E_2=\operatorname{span}(e_1)\\) using an outside direction \\(e_4\\), one should take \\(E_2=\operatorname{span}(e_1,e_4)\\), not \\(E_2=\operatorname{span}(e_4)\\).

Verdict on Question 1: port rigidity is a valid conditional no-go theorem, but the general fixed-subspace route is not closed. The decisive parameters are the intersection \\(E_1\cap E_2\\) and the amount of rank available beyond the directions already forced into \\(W\\).

## 2. Witness-defined local subspaces and the free-row problem

Making \\(E_j\\) witness-defined removes the fixed-port lemma, but it does not automatically solve soundness. It can make the problem worse: the same free rows used to define a local subspace may also enlarge the global row space against which the local incidence is tested.

There is a useful exact reformulation that should be the starting point.

Put

\\[ \mathcal T=\operatorname{row}[N\ AN]\subseteq\mathbb R^{2k}. \\]

For each free row \\(r_i\\), its compressed pair satisfies

\\[ \boxed{(H_i,(H_A)\_i)\in\mathcal T.} \tag{2} \\]

Conversely, every pair in \\(\mathcal T\\) is realizable by some free row \\(r_i\\). The free rows are independent, so the compressed problem is exactly:

- fixed rows have their prescribed pairs;
- each free row pair can be chosen arbitrarily from the same fixed linear space \\(\mathcal T\\);
- the whole matrices must satisfy (5a) and (5b).

This describes all the freedom in \\(R\\) without referring to the original state dimension.

### A symmetry that the gate programme should account for

All free rows have the same allowable pair space \\(\mathcal T\\). Therefore they are exchangeable.

If \\(S\\) is a permutation matrix that fixes the first \\(r_0\\) rows and permutes the free rows, then

\\[ H\longmapsto SH,\qquad H_A\longmapsto SH_A \\]

preserves both rank conditions:

\\[ \operatorname{rank}(SH)=\operatorname{rank}H,\qquad \operatorname{rank}(\lambda SH-SH_A) =\operatorname{rank}(\lambda H-H_A). \\]

It also preserves (2), since every free row pair belongs to the same \\(\mathcal T\\).

Hence no free row has an intrinsic gate identity merely because it occupies a particular row index. A sound construction may still identify roles by the geometry of the row values, but its decoding must be invariant under permutations of the free rows, or explicitly account for them.

This rules out a common shortcut: “row 3 is the first gate's output, and row 4 is the second gate's input” is not a sound specification unless the construction makes those roles algebraically distinguishable.

### Can the conditions control all free rows at once?

Potentially, but there is no general mechanism established in the report.

The most important identity is

\\[ \boxed{\operatorname{row}H_A=\operatorname{row}H} \tag{3} \\]

for every feasible solution. Indeed, (5a) gives inclusion, and (5b) at \\(\lambda=0\\) gives

\\[ \operatorname{rank}H_A=\operatorname{rank}H. \\]

Thus the two row spaces must be equal.

This is a genuinely global constraint. It couples the free row choices through a common row space. But it does not identify a particular free row or force it to be zero. Extra free rows can enlarge \\(\operatorname{row}H\\); their \\(H_A\\)-partners can enlarge the other row space at the same time.

One useful necessary condition on a sound construction is therefore:

> For invalid source assignments, every possible choice of free row pairs from \\(\mathcal T\\) must either violate row-space equality in (3) or cause the pencil to lose rank at some complex \\(\lambda\\).

That is much stronger than checking that one intended choice of free rows satisfies the multiplication equations.

A practical design principle is to make \\(\mathcal T\\) restrictive rather than use the universal lift \\(\mathcal T=\mathbb R^{2k}\\). The universal lift is excellent for realizing a desired compressed witness, but it provides no row-level restrictions at all. A nontrivial \\(\mathcal T\\) can impose a shared linear rule on every free row. The difficulty is then to combine this shared rule with the global rank and spectral conditions so that extra rows cannot bypass the gate.

## 3. Alternative encodings: work with the global row space, not local ports

I think the next direction should be a global constrained-matrix-pencil encoding. It avoids making the local intersections \\(W\cap E_j\\) carry the entire burden of wiring.

There are three exact structural facts to exploit.

### 3.1 The free-row constraint is one fixed linear space

As above, every free row pair belongs to

\\[ \mathcal T=\operatorname{row}[N\ AN]\subseteq\mathbb R^{2k}. \\]

Choose a matrix \\(D\\) with

\\[ \ker D=\mathcal T. \\]

Then the entire free-row condition is just

\\[ D\begin{bmatrix}H_i^{\mathsf T}\\\\(H_A)\_i^{\mathsf T}\end{bmatrix}=0 \quad\text{for each free row }i. \tag{4} \\]

Thus q1 can be viewed as a matrix-completion problem in which every free row of \\([H\ H_A]\\) lies in the same prescribed linear subspace, while the fixed rows are prescribed.

This is a more faithful global formulation than thinking of the free rows as individually named gate ports.

### 3.2 Feasibility forces equal row spaces

As noted,

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H \\]

comes from (5a), and (5b) at \\(\lambda=0\\) gives

\\[ \operatorname{rank}H_A=\operatorname{rank}H. \\]

Therefore

\\[ \operatorname{row}H_A=\operatorname{row}H=:W. \\]

So a feasible solution consists of two matrices whose rows generate the same subspace \\(W\\), with each free row pair constrained by \\(\mathcal T\\).

This suggests encoding wires by global linear dependencies between the two row systems, rather than by requiring a chosen row of \\(H_A\\) to equal a chosen row of \\(H\\).

### 3.3 The spectral condition has a global polynomial-matrix formulation

From (5a), choose \\(F\in\mathbb R^{q\times q}\\) such that

\\[ H_A=FH. \\]

Let

\\[ U=\operatorname{im}H\subseteq\mathbb R^q. \\]

Then (5b) is equivalent to

\\[ \operatorname{rank}((\lambda I-F)H)=\dim U \quad\forall\lambda\in\mathbb C, \\]

or

\\[ U\cap\ker(\lambda I-F)=\\{0\\} \quad\forall\lambda\in\mathbb C. \tag{5} \\]

There is another useful equivalent statement. Factor \\(H=XB\\), where \\(X\in\mathbb R^{q\times\omega}\\) has full column rank and \\(B\in\mathbb R^{\omega\times k}\\) has full row rank. Then

\\[ P(\lambda)=(\lambda I-F)XB. \\]

Since \\(B\\) has full row rank,

\\[ \operatorname{rank}P(\lambda) =\operatorname{rank}((\lambda I-F)X). \\]

Thus (5b) is equivalent to the rectangular polynomial matrix

\\[ Q(\lambda)=(\lambda I-F)X \\]

having full column rank \\(\omega\\) at every complex \\(\lambda\\).

This means \\(Q\\) has a polynomial left inverse:

\\[ G(\lambda)Q(\lambda)=I\_\omega \tag{6} \\]

for some polynomial matrix \\(G\\).

To see why, take all \\(\omega\times\omega\\) minors \\(m_I(\lambda)\\) of \\(Q\\). Full column rank for every complex \\(\lambda\\) is equivalent to their having no common complex root, hence to

\\[ \gcd_I m_I=1. \\]

There are therefore real polynomials \\(u_I\\) such that

\\[ \sum_I u_I(\lambda)m_I(\lambda)=1. \\]

For a row set \\(I\\), let \\(Q_I\\) be the corresponding square submatrix. The adjugate identity gives

\\[ \operatorname{adj}(Q_I)E_IQ =m_I I\_\omega, \\]

where \\(E_I\\) selects the rows in \\(I\\). Summing with coefficients \\(u_I\\) constructs the left inverse (6).

Moreover, since \\(\deg m_I\le\omega\\), the Bezout coefficients can be taken to have degree less than \\(\omega\\). This gives a left inverse with degree at most \\(2\omega-2\\).

This global polynomial-matrix identity is a useful alternative to individual spectral ports. It also gives a polynomial-size existential-real certificate for the spectral condition when the dimensions are unrestricted: quantify the coefficients of \\(G\\) and impose the polynomial identity (6).

What remains open: neither (4), equal row spaces, nor (6) yet encodes multiplication. They identify the global algebraic object in which a sound construction should live. A reduction would have to make arithmetic follow from the interaction of the shared row space, the per-row subspace \\(\mathcal T\\), and the polynomial left-inverse condition.

My answer to Question 3: yes, there is a promising global encoding route that avoids local-subspace intersections as the primary wiring mechanism. But it is a framework, not yet a circuit reduction.

## 4. Is sound multiplication possible at all?

There is currently no general no-go theorem in the report's arguments.

The fixed-port lemma rules out a particular type of local construction. It does not rule out a multiplication gadget based on:

- a moving subspace intersection with disjoint fixed local subspaces;
- a global row-space identity;
- a nontrivial per-row space \\(\mathcal T\\);
- the spectral condition as a polynomial-matrix left-invertibility condition.

Nor does the fact that free rows are exchangeable rule out a gadget. It means that the decoding must not depend on arbitrary row labels. A sound gadget could conceivably encode its variables through the unordered collection of free row pairs and the row space they jointly generate.

### 4.1 An exact restricted no-go result

There is one simple but important no-go condition.

Suppose, for a particular fixed instance, that choosing \\(R=0\\) already satisfies (5a) and (5b). Then q1 is feasible regardless of any intended values represented by the free rows. Therefore that instance cannot enforce a nontrivial relation among those values.

This is exactly what happened with the earlier universal-lift multiplication construction. The fixed rows alone supplied a feasible pencil.

Thus any sound multiplication construction must avoid this situation. More generally, for an invalid multiplication assignment, every allowable completion by free rows must fail—not just the intended completion.

### 4.2 A correction to the input-controlled nonzero claim

There is one quantifier distinction in II.2 that should be fixed in the report.

For the input-controlled construction,

\\[ H=\begin{bmatrix}1\\\u\end{bmatrix}, \qquad H_A=\begin{bmatrix}0\\\xv\end{bmatrix}, \qquad P(\lambda)= \begin{bmatrix} \lambda\\\ \lambda u-xv \end{bmatrix}. \\]

For a particular free row \\(R=(u,v,w)\\),

\\[ \boxed{(5b)\iff xv\ne0,} \\]

not \\(x\ne0\\) for every \\(R\\). For example, \\(v=0\\) makes (5b) fail even when \\(x\ne0\\).

The actual q1 feasibility statement is

\\[ \boxed{ \exists R:\ (5a)\wedge(5b) \iff x\ne0. } \\]

This is sound: if \\(x=0\\), no \\(R\\) works; if \\(x\ne0\\), choose any \\(v\ne0\\).

The distinction is between a property of every candidate \\(R\\) and a property of the existential feasibility problem. The report's construction remains a valid input-controlled nonzero gadget when stated with the correct quantifiers.

### 4.3 What would a genuine multiplication no-go need to say?

A meaningful no-go theorem must quantify over the entire allowed architecture. For example, it might prove that for a certain class of row-pair spaces \\(\mathcal T\\), fixed-row patterns, and rank strata, the feasible set of witness values cannot contain the graph

\\[ \\{(x,y,z):z=xy\\}. \\]

But no such theorem follows from the supplied port-rigidity argument.

I would not currently write “sound multiplication is impossible.” The accurate statement is:

> The existing multiplication construction is unsound under unrestricted \\(R\\). The fixed-port argument rules out a restricted family of wiring schemes. General sound multiplication remains open.

## 5. Is the fixed-\\(\kappa\_{\rm obs}\\) Gram certificate a publishable FPT route?

Strongest algorithmic route

Yes. Subject to writing out the exact bit-complexity proof, the Gram certificate appears sufficient for a genuine FPT theorem. Here is the full argument I would aim to put in the paper.

Let

\\[ d_0=\operatorname{rank}[N\ AN],\qquad \kappa\_{\rm obs}=r d_0. \\]

### 5.1 Compress the free variables

The map from one free row to its compressed pair is

\\[ r_i\longmapsto(r_iN,r_iAN)=r_i[N\ AN]. \\]

Its image is precisely \\(\mathcal T\\), of dimension \\(d_0\\).

Choose a rational basis of \\(\mathcal T\\). Each free row pair can then be represented by \\(d_0\\) real coordinates. These choices are independent from row to row. Hence the complete compressed instance depends on at most

\\[ r d_0=\kappa\_{\rm obs} \\]

effective real variables.

For \\(r\ge1\\), the full-column-rank property of \\(N\\) gives

\\[ k\le d_0\le\kappa\_{\rm obs}. \\]

The number \\(q\\) may be arbitrarily large; its dependence will enter only through polynomial-time sums and matrix operations.

The cases \\(r=0\\) and \\(k=0\\) should be handled directly. When \\(r=0\\), there is no free variable and the candidate can be tested directly. When \\(k=0\\), the compressed conditions are vacuous.

### 5.2 Encode (5a) with Gram matrices

For a fixed rank stratum \\(\omega\\), define

\\[ G_H=H^{\mathsf T}H,\qquad G_S=H^{\mathsf T}H+H_A^{\mathsf T}H_A. \\]

These are positive-semidefinite matrices, with

\\[ \operatorname{rank}G_H=\operatorname{rank}H,\qquad \operatorname{rank}G_S =\operatorname{rank}\begin{bmatrix}H\\\H_A\end{bmatrix}. \\]

For a positive-semidefinite matrix \\(G\\), its \\(j\\)-th elementary symmetric polynomial \\(e_j(G)\\) is positive exactly when \\(\operatorname{rank}G\ge j\\).

Therefore

\\[ \boxed{ (5a)\iff e\_\omega(G_H)>0,\qquad e\_{\omega+1}(G_S)=0 } \tag{7} \\]

on the rank-\\(\omega\\) stratum. The first condition gives rank at least \\(\omega\\); the second gives stacked rank at most \\(\omega\\). Since stacking cannot decrease rank, both ranks equal \\(\omega\\).

For \\(\omega=0\\), \\(e_0=1\\), and \\(e_1(G_S)=0\\) forces \\(H=H_A=0\\). That stratum can also be tested directly.

### 5.3 Encode (5b) by a bounded-degree Bezout certificate

Assume \\(\omega>0\\). Let \\(f_1,\ldots,f_s\\) be the \\(\omega\times\omega\\) minors of

\\[ P(\lambda)=\lambda H-H_A. \\]

They are real polynomials of degree at most \\(\omega\\).

Condition (5b) is equivalent to these polynomials having no common complex root, or equivalently

\\[ \gcd\_{\mathbb C[\lambda]}(f_1,\ldots,f_s)=1. \\]

The useful degree-bound lemma is:

> If real univariate polynomials \\(f_i\\) of degree at most \\(\omega\\) have no common complex root, then there exist real polynomials \\(g_i\\) of degree less than \\(\omega\\) such that\
> \\[\
> \sum_i g_i f_i=1.\
> \\]

To prove it, choose a nonzero real linear combination \\(g\\) of the \\(f_i\\). It has finitely many complex roots. At each root, the real coefficient vectors defining a linear combination \\(h\\) that vanishes there form a proper real linear subspace. Avoiding the finite union of these subspaces gives \\(h\\) with no common root with \\(g\\). Two-polynomial Bezout then produces multipliers of degree less than \\(\omega\\), and expanding the linear combinations gives the claim.

Now make a matrix \\(B\\) with \\(2\omega\\) columns. For every minor \\(f_i\\) and every \\(j=0,\ldots,\omega-1\\), include the coefficient vector of \\(\lambda^j f_i\\), in the basis

\\[ 1,\lambda,\ldots,\lambda^{2\omega-1}. \\]

Then

\\[ (5b)\iff e_0\in\operatorname{row}B. \\]

For real \\(B\\),

\\[ \operatorname{row}B =\operatorname{im}(B^{\mathsf T}B). \\]

Thus

\\[ \boxed{ (5b)\iff \exists x\in\mathbb R^{2\omega}: B^{\mathsf T}Bx=e_0. } \tag{8} \\]

This replaces the potentially enormous family of Bezout multiplier coefficients with only \\(2\omega\\) auxiliary variables.

### 5.4 Compute \\(B^{\mathsf T}B\\) without enumerating row minors

This is the crucial compression.

Write

\\[ f_i(\lambda)=\sum\_{a=0}^{\omega}c\_{i,a}\lambda^a, \\]

taking out-of-range coefficients as zero. The row of \\(B\\) indexed by \\((i,j)\\) has entry

\\[ B\_{(i,j),t}=c\_{i,t-j}. \\]

Therefore the correctly indexed Gram entries are

\\[ \boxed{ (B^{\mathsf T}B)\_{t,t'} = \sum\_{j=0}^{\omega-1}\sum_i c\_{i,t-j}c\_{i,t'-j}. } \tag{9} \\]

The shift-index sum is essential.

Define

\\[ K(\lambda,\mu) =\sum_i f_i(\lambda)f_i(\mu). \\]

If

\\[ K(\lambda,\mu)=\sum\_{a,b} s\_{a,b}\lambda^a\mu^b, \qquad s\_{a,b}=\sum_i c\_{i,a}c\_{i,b}, \\]

then (9) is

\\[ (B^{\mathsf T}B)\_{t,t'} =\sum\_{j=0}^{\omega-1}s\_{t-j,t'-j}. \\]

The minors are indexed by row subsets \\(I\\) and column subsets \\(J\\). Grouping by \\(J\\) and applying Cauchy–Binet gives

\\[ \boxed{ K(\lambda,\mu)= \sum\_{\substack{J\subseteq[k]\\\\|J|=\omega}} \det\\!\left( P(\lambda)\_{:,J}^{\mathsf T} P(\mu)\_{:,J} \right). } \tag{10} \\]

There are at most

\\[ \binom{k}{\omega}\le 2^k\le2^{\kappa\_{\rm obs}} \\]

terms. Each determinant has size \\(\omega\times\omega\\), and its matrix entries are sums over the \\(q\\) rows.

Thus (10) avoids enumerating \\(\binom q\omega\\) row subsets. It computes exactly the information needed for \\(B^{\mathsf T}B\\), with a parameter-dependent number of terms and polynomial dependence on \\(q\\).

### 5.5 FPT and bit complexity

For each rank stratum \\(\omega\\), the existential formula has at most

\\[ \kappa\_{\rm obs}+2\omega \le3\kappa\_{\rm obs} \\]

real variables.

Its number of polynomial constraints and their degrees are bounded by functions of \\(\kappa\_{\rm obs}\\):

- (7) contributes two polynomial conditions;
- (8) contributes \\(2\omega\\) polynomial equations;
- the degrees are at most \\(2\omega+2\\) for the rank condition and \\(2\omega+1\\) for the Gram-certificate equations.

For rational input, compute a rational nullspace basis \\(N\\) and a rational basis of \\(\mathcal T\\) by exact linear algebra. These operations have polynomial bit complexity. The coefficient calculations in (7) and (10) use a parameter-bounded number of determinants, each of size at most \\(\kappa\_{\rm obs}\\), together with polynomial-time sums over the \\(q\\) rows. The resulting coefficient bit lengths are bounded by \\(f(\kappa\_{\rm obs})\operatorname{poly}(\mathcal L)\\), where \\(\mathcal L\\) is the original input bit length.

An existential real feasibility algorithm with \\(m\\) variables, \\(s\\) polynomials of degree at most \\(D\\), and coefficient bit size \\(\tau\\) has singly-exponential dependence on \\(m\\), of the standard form \\((sD)^{O(m)}\operatorname{poly}(\tau)\\). This is the setting developed in the real-algebraic complexity literature, including Renegar's work and the Basu–Pollack–Roy treatment of existential real feasibility.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车+3



Here \\(m,s,D\\) are functions only of \\(\kappa\_{\rm obs}\\). Consequently the target bound is

\\[ \boxed{ q1\in f(\kappa\_{\rm obs})\\,\mathcal L^{O(1)}. } \\]

My assessment: this is a credible FPT theorem, not merely a heuristic. The proof still needs to be written as a formal algorithm with coefficient-growth bounds, but the Gram identity does close the earlier \\(q\\)-dependence problem. I would make this the main algorithmic result.

## 6. Fixed \\(q\\): a concrete way to close the parametric-elimination gap

I think the fixed-\\(q\\) route can also be made rigorous. The missing lemma need not be a deep new theorem about parametric linear systems. There is a direct rank-consistency encoding.

The idea is to factor \\(H\\) through its rank-\\(\omega\\) column space and eliminate the large factor by testing linear-system consistency.

### 6.1 Factor \\(H\\) and normalize pivot columns

Fix \\(\omega>0\\). For any matrix \\(H\\) of rank \\(\omega\\), there is a set of \\(\omega\\) columns \\(J\subseteq[k]\\) such that

\\[ X:=H\_{:,J}\in\mathbb R^{q\times\omega} \\]

has full column rank. Then there is a matrix \\(B\in\mathbb R^{\omega\times k}\\) such that

\\[ H=XB,\qquad B\_{:,J}=I\_\omega. \tag{11} \\]

Conversely, if \\(X\\) has full column rank and \\(B\_{:,J}=I\_\omega\\), then \\(H=XB\\) has rank exactly \\(\omega\\).

There are

\\[ \binom{k}{\omega} \\]

choices for \\(J\\). For fixed \\(q\\), \\(\omega\le q\\), so enumerating them is polynomial in \\(k\\).

By (5a), choose \\(F\in\mathbb R^{q\times q}\\) with

\\[ H_A=FH=FXB. \tag{12} \\]

The key is that \\(F\\) and \\(X\\) have only

\\[ q^2+q\omega\le2q^2 \\]

entries. These are a constant number of real parameters when \\(q\\) is fixed.

### 6.2 The remaining \\(B\\)-constraints form a parametric linear system

Recall the fixed per-row space

\\[ \mathcal T=\operatorname{row}[N\ AN]. \\]

Choose a rational matrix \\(D\\) with kernel \\(\mathcal T\\).

For each fixed row \\(i\le r_0\\), the prescribed compressed pair is

\\[ h_i^0=(L_0N)\_i,\qquad g_i^0=(L_0AN)\_i. \\]

Using (11)–(12), it must satisfy

\\[ X\_{i,:}B=h_i^0,\qquad (FX)\_{i,:}B=g_i^0. \tag{13} \\]

For every free row \\(i>r_0\\), its compressed pair must belong to \\(\mathcal T\\), so

\\[ D\begin{bmatrix} (X\_{i,:}B)^{\mathsf T}\\\ ((FX)\_{i,:}B)^{\mathsf T} \end{bmatrix}=0. \tag{14} \\]

After substituting the normalized columns \\(B\_{:,J}=I\_\omega\\), all equations (13)–(14) are linear in the remaining entries of \\(B\\). Their coefficients are polynomials of degree at most two in the entries of \\(F,X\\).

We therefore get a parametric linear system

\\[ \boxed{M(F,X)b=c(F,X),} \tag{15} \\]

where \\(b\\) contains the remaining entries of \\(B\\), and the number of rows and columns of \\(M\\) is polynomial in \\(k\\). Importantly, \\(b\\) is not needed as a quantified variable in the final formula: only consistency of (15) needs to be tested.

### 6.3 A rank-consistency lemma eliminates \\(b\\)

Here is the missing lemma in a convenient form.

> Lemma (parametric linear consistency). Let \\(M(z)\\) and \\(c(z)\\) be polynomial matrices and vectors in a fixed number \\(d\\) of real parameters \\(z\\), with dimensions growing as part of the input. Then\
> \\[\
> \exists b:\ M(z)b=c(z)\
> \\]\
> can be expressed by a polynomial-size semialgebraic formula in \\(z\\). If \\(d\\) is fixed and the entries of \\(M,c\\) have bounded degree, this formula can be constructed in polynomial bit complexity in the matrix dimensions and coefficient bit length, with the resulting polynomial degrees allowed to grow with the matrix dimensions.

Proof. Put

\\[ \Gamma=MM^{\mathsf T},\qquad \Gamma' = MM^{\mathsf T}+cc^{\mathsf T}. \\]

Both matrices are positive semidefinite, and

\\[ \operatorname{rank}\Gamma=\operatorname{rank}M,\qquad \operatorname{rank}\Gamma'=\operatorname{rank}[M\ c]. \\]

The system is consistent exactly when these ranks are equal.

Let \\(e_j\\) denote elementary symmetric polynomials, and let

\\[ d_1=\min\\{\text{number of rows of }M,\text{ number of columns of }M\\}. \\]

Rank equality can be written as the finite disjunction

\\[ \boxed{ \bigvee\_{t=0}^{d_1} \left[ e_t(\Gamma)>0 \ \wedge\ e\_{t+1}(\Gamma)=0 \ \wedge\ e\_{t+1}(\Gamma')=0 \right]. } \tag{16} \\]

Here \\(e_0=1\\), and elementary symmetric polynomials beyond the matrix size are zero by convention.

The first two conditions say \\(\operatorname{rank}\Gamma=t\\); the last says \\(\operatorname{rank}\Gamma'\le t\\). Since \\(\Gamma'\succeq\Gamma\succeq0\\), its rank cannot be smaller than \\(t\\), so equality follows.

The polynomials \\(e_j(\Gamma)\\) and \\(e_j(\Gamma')\\) are coefficients of characteristic polynomials such as

\\[ \det(sI+\Gamma). \\]

They can be computed by exact polynomial determinant algorithms. Since the number \\(d\\) of parameters is fixed, their degrees and the number of their monomials grow polynomially with the matrix dimensions. This gives a polynomial-size formula in the fixed parameters. \\(\square\\)

This is the precise elimination mechanism missing from the earlier fixed-\\(q\\) sketch.

### 6.4 The spectral condition depends only on \\(F,X\\)

From (11)–(12),

\\[ P(\lambda) =(\lambda I-F)XB. \\]

Since \\(B\\) has full row rank,

\\[ \operatorname{rank}P(\lambda) =\operatorname{rank}((\lambda I-F)X). \\]

Thus (5b) is equivalent to

\\[ \operatorname{rank}((\lambda I-F)X)=\omega \quad\forall\lambda\in\mathbb C. \tag{17} \\]

This condition is independent of \\(B\\).

For fixed \\(q\\), there are only \\(\binom q\omega\\) maximal minors of \\((\lambda I-F)X\\), and their degrees are at most \\(\omega\\). Encode (17) by the \\(2\omega\\)-variable Gram–Bezout certificate from Section 5. This adds only \\(2\omega\le2q\\) auxiliary variables.

Also impose

\\[ e\_\omega(X^{\mathsf T}X)>0 \\]

to ensure that \\(X\\) has full column rank.

### 6.5 Resulting complexity bound

For each \\(\omega\\), and each pivot set \\(J\\), the construction has:

- \\(q^2+q\omega\\) variables for \\(F,X\\);
- \\(2\omega\\) spectral-certificate variables;
- a polynomial-size consistency formula (16);
- a polynomial number of coefficients and constraints, with degrees polynomial in \\(k\\).

The total number of quantified variables is at most

\\[ q^2+q\omega+2\omega=O(q^2). \\]

The number of pivot sets is at most \\(k^q\\). A fixed-variable existential real decision algorithm therefore yields a coarse bound of the form

\\[ \boxed{\mathcal L^{O(q^2)}} \\]

for fixed \\(q\\), where \\(\mathcal L\\) is the rational input bit length. The exponent depends on \\(q\\), as expected for an XP-type result.

For \\(\omega=0\\), handle the stratum separately: it is feasible exactly when the fixed rows have \\(H_0=H\_{A,0}=0\\), since the free rows can be set to zero.

Answer to Question 6: the parametric rank-attainment issue is not an obstruction to a fixed-\\(q\\) polynomial algorithm. Equations (15)–(16) provide a concrete route to eliminate the high-dimensional linear variables. This is a proposed proof route that should be checked and formalized carefully, but it is materially stronger than the previous sketch.

There is related literature on parametric linear systems. For example, Corless, Giesbrecht, Rafiee Sevyeri, and Saunders study regime decompositions for parametric linear systems, with polynomial-time results in the number of matrix dimensions and parameter degrees for up to three parameters. The rank-consistency construction above is tailored to q1 and does not require importing their result.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



## 7. Overall route guidance

I would choose a combination of (b) and (c) as the main programme, while retaining (a) as a focused secondary project.

### Main line: fixed-\\(\kappa\_{\rm obs}\\) FPT

This has the clearest route to a rigorous theorem:

- The effective number of free variables is exactly \\(\kappa\_{\rm obs}=r\operatorname{rank}[N\ AN]\\).
- The Gram formulation for (5a) is straightforward.
- The bounded-degree Bezout certificate reduces (5b) to \\(2\omega\\) variables.
- Cauchy–Binet removes the dependence on the potentially large number of row minors.
- The remaining work is exact coefficient construction and bit-complexity accounting.

This is the route I would develop into the principal algorithmic paper.

### Second line: fixed-\\(q\\) polynomial time

The factorization \\(H=XB\\) and the rank-consistency lemma give a plausible second theorem:

\\[ \text{for every fixed }q,\quad q1\in\mathrm P. \\]

The likely complexity dependence is \\(\mathcal L^{O(q^2)}\\), so this does not replace the fixed-\\(\kappa\_{\rm obs}\\) FPT theorem. It is nevertheless a useful complement, because it shows that small observer order is algorithmically tractable even when the state dimension is large.

The distinction must be explicit:

- Fixed \\(q\\) polynomial time is an XP-style parameterized statement.
- Fixed-\\(\kappa\_{\rm obs}\\) FPT has a parameter-dependent factor times a polynomial whose exponent is independent of the parameter.

### Secondary line: continue hardness, but change the object of study

I would not abandon the hardness programme, but I would stop investing heavily in literal row-copy or formatter gadgets. The fixed-subspace obstruction shows why the minimal local-port idea is brittle.

The next hardness attempt should start from the global formulation

\\[ \mathcal T,\qquad \operatorname{row}H_A=\operatorname{row}H,\qquad H_A=FH,\qquad \operatorname{rank}((\lambda I-F)X)=\omega\quad\forall\lambda. \\]

A potentially better source is a global subspace-realization or matroid-representability problem, rather than a direct sum of independent multiplication blocks. But no reduction from such a source has been established; the per-row common-space condition and the spectral condition still have to be handled.

### What would change my recommendation?

I would promote the gate programme back to the main line only after one of the following:

1. A sound multiplication gadget is found, with a proof that every feasible unrestricted \\(R\\) decodes to \\(z=xy\\), including all other rank strata.
2. A genuine no-go theorem is proved for a well-defined broad class of possible gate constructions.

At present, neither exists. The existing port obstruction is too narrow to establish impossibility, while the current multiplication construction has an explicit \\(R=0\\) soundness failure.

## 8. Revised status table

| Claim                                                                      | Assessment                                                                                       |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Fixed \\(E_1,E_2\\) sharing a port line force that port to be fixed        | Proved, when the port is exactly their one-dimensional intersection with \\(W\\)                 |
| Fixed local subspaces never permit moving ports                            | False in general; disjoint fixed subspaces and extra dimensions can support moving intersections |
| \\(v_x=e_2+xe_3\\) freezes the port                                        | True in the minimal rank-three regime; not enough when extra dimensions are available            |
| Witness-defined local subspaces solve soundness                            | Not established; they can be enlarged by the same free rows used to define them                  |
| Free rows are exchangeable                                                 | Proved; decoding must respect this symmetry                                                      |
| Feasible solutions satisfy \\(\operatorname{row}H_A=\operatorname{row}H\\) | Proved                                                                                           |
| Sound multiplication is impossible                                         | Not proved                                                                                       |
| The earlier universal-lift multiplication gate is sound                    | False; \\(R=0\\) is a feasible bypass                                                            |
| Input-controlled nonzero gate                                              | Sound as an existential q1 test; for a fixed \\(R\\), the condition is \\(xv\ne0\\)              |
| Fixed-\\(\kappa\_{\rm obs}\\) FPT via Gram certificate                     | Strong, near-complete proof route; coefficient and bit bounds need formal write-up               |
| Fixed-\\(q\\) polynomial route                                             | A concrete new proof route via factorization and rank-consistency elimination                    |
| Unrestricted q1 \\(\exists\mathbb R\\)-hardness                            | Open in this programme                                                                           |

## 9. Final recommendation

The strongest research strategy is:

1. Finish the fixed-\\(\kappa\_{\rm obs}\\) FPT theorem first.
2. Formalize the fixed-\\(q\\) polynomial algorithm using the parametric rank-consistency lemma.
3. Keep the hardness question open, but replace local row-copy engineering with a global \\(\mathcal T\\)-constrained matrix-pencil formulation.
4. Pursue a different hardness source only if it naturally respects the exchangeability of free rows and the global spectral condition.

The most valuable conceptual shift is this: the wiring problem is not fundamentally about copying coordinates between rows. It is about controlling the entire feasible row space generated by an unordered collection of free row pairs. The fixed-port obstruction diagnoses one failed way to control that space; it does not show that the space cannot encode arithmetic.

The algorithmic route, by contrast, has a much clearer proof architecture and should now be the project's primary result.