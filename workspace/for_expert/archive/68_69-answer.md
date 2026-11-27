# Research assessment of Reports 68 and 69: the single-gate barriers and the free-witness obstruction

The two reports identify a more fundamental difficulty than the spectral-uniformity problem addressed in Report 67. The spectral mechanism now has a satisfactory solution: a fixed unit minor can protect the pencil uniformly over a parameter family. The unresolved issue is whether the observer feasibility conditions can force an arithmetic relation on variables that are themselves chosen as part of the witness \\(L\\).

My central assessment is:

1. The free-witness obstruction is a genuine warning, but it is not yet a general impossibility theorem. Constructibility does not imply that parameter fibres are open or finite, and rank equalities can impose arbitrary polynomial equations on suitable parameterizations.
2. The fixed-\\(L_0\\), \\(\omega=2,q=3\\) obstruction is plausible and can be made rigorous under the hypotheses stated in Report 68. It should be recorded as a low-dimensional no-go lemma, not generalized prematurely.
3. The proposed \\(\omega\ge4\\) two-step architecture is a reasonable next construction to test, but the report has not established that \\(\omega=4\\) is sufficient or minimal. The argument must account for all columns of the pencil and for realization by a fixed \\(A,C\\).
4. The fixed-kernel lift family is useful for spectral and row-independence engineering, but it does not encode multiplication in its present form. Its feasible parameter set \\(s\ne0\\) is an open condition, so it cannot force \\(s=xy\\).
5. The most promising change of direction is to stop treating the arithmetic variables as freely chosen coordinates of \\(L\\). They should instead be represented by quantities determined by the input data or by a rigid, uniquely recoverable substructure of the witness. The rank conditions can then test relations among those quantities.

The distinction between a free witness coordinate and an input-determined invariant is central. It is not enough to produce a polynomial equation involving variables that occur in \\(L\\); one must prevent the remaining witness freedom from satisfying that equation independently of the intended arithmetic assignment.

I will separate what is proved by the reports, what follows mathematically, and what remains conjectural.

## 1. Report 68: audit of the structural claims

### 1.1 The uniform spectral lemma is correct

The unit-minor argument in Part II.1 is sound.

Suppose

\\[ H_A(X)=D(X)H(X),\qquad \operatorname{im}H(X)=W, \\]

where \\(\dim W=\omega\\), independently of \\(X\\). Then

\\[ P_X(\lambda) =(\lambda I-D(X))H(X). \\]

Choose a basis

\\[ w_0,\ldots,w\_{\omega-1} \\]

of \\(W\\), and a vector \\(g\notin W\\). Assume

\\[ D(X)w_j=w\_{j+1}+\sum\_{i=0}^{j}a\_{ij}(X)w_i, \quad 0\le j<\omega-1, \\]

and

\\[ D(X)w\_{\omega-1} =g+\sum\_{i=0}^{\omega-1}a\_{i,\omega-1}(X)w_i. \\]

Consider the matrix of \\((\lambda I-D(X))|\_W\\), restricted to the output coordinates

\\[ w_1,\ldots,w\_{\omega-1},g \\]

and the input basis

\\[ w_0,\ldots,w\_{\omega-1}. \\]

It is triangular, with diagonal entries all equal to \\(-1\\). Thus the selected minor is

\\[ (-1)^\omega. \\]

Consequently,

\\[ \boxed{ \operatorname{rank}P_X(\lambda)=\omega \quad\forall X,\ \forall\lambda\in\mathbb C. } \\]

This is stronger and more useful than a generic gcd argument: the certificate is an identity, not a statement about generic parameter values. It remains valid under arbitrary changes to the coefficients \\(a\_{ij}(X)\\), provided the filtration and its pivot coefficients are preserved.

One minor clarification: the fixed image \\(W\\) and the map \\(D(X)\\) need only be defined on \\(W\\). Extending \\(D(X)\\) to all of \\(\mathbb C^q\\) is unnecessary.

Verdict: retain this lemma as a proved structural result. It is not the obstruction to the hardness programme.&#x20;

68_single_gate_barriers.md



### 1.2 A fixed \\(L_0\\) restricts the graph chart, but does not prevent a variable kernel

The report is right that the naive chart

\\[ H(X)=[I\ -X] \\]

cannot be used without modification if its first row is supposed to equal the fixed row

\\[ h_0=L_0N. \\]

But the conclusion should be more precise.

Since

\\[ V(X)=\ker H(X), \\]

and the first row of \\(H(X)\\) is fixed, every admissible kernel must satisfy

\\[ \boxed{V(X)\subseteq\ker h_0.} \\]

Thus the variable kernels are restricted to a Schubert-type subvariety of the relevant Grassmannian. This is a genuine geometric restriction, but it is not a prohibition on variation.

A useful chart is

\\[ H(X)= C_0 \begin{bmatrix} h_0\\\ g_1(X)\\\ \vdots\\\ g\_{\omega-1}(X) \end{bmatrix}, \\]

where \\(C_0\\) is fixed and the \\(g_i(X)\\) vary.

In this representation, the first row remains fixed, while the row space of \\(H(X)\\), and hence its kernel, can vary.

In fact, the construction below gives an explicit observer realization with precisely this structure.

Verdict: Part II.2 is correct as a warning against the naive chart, but it should not be read as a structural obstruction to variable kernels.&#x20;

68_single_gate_barriers.md



### 1.3 The claimed \\(\omega=2,q=3\\) impossibility is false

This is the most important correction to Report 68.

The argument in Part II.3 correctly observes that, under its row representation,

\\[ h\_{A,0}\in\operatorname{span}\\{h_0,g(X)\\}. \\]

If \\(h_0\\) is fixed and the directions \\(g(X)\\) vary sufficiently, then it may follow that

\\[ h\_{A,0}=\lambda_0h_0. \\]

But the next inference is invalid:

> The first row of \\(P(\lambda_0)\\) is zero, so the rank of \\(P(\lambda_0)\\) drops.

A zero row does not imply that a \\(3\times k\\) matrix of rank two has rank less than two. The other two rows can still be independent.

Here is an explicit counterexample at the compressed-pencil level.

Let

\\[ H(t)= \begin{bmatrix} 1&0&0\\\ 0&1&t\\\ 1&1&t \end{bmatrix}, \qquad D= \begin{bmatrix} 0&0&0\\\ 1&0&0\\\ 1&1&0 \end{bmatrix}. \\]

Then

\\[ H_A(t)=DH(t) = \begin{bmatrix} 0&0&0\\\ 1&0&0\\\ 1&1&t \end{bmatrix}. \\]

The first row of \\(H(t)\\) is fixed:

\\[ h_0=(1,0,0), \\]

and the first row of \\(H_A(t)\\) is also fixed:

\\[ h\_{A,0}=0. \\]

The kernel is

\\[ \boxed{ \ker H(t)=\operatorname{span}\\{(0,-t,1)\\}. } \\]

It varies with \\(t\\).

Yet the pencil is

\\[ P_t(\lambda)= \begin{bmatrix} \lambda&0&0\\\ -1&\lambda&\lambda t\\\ \lambda-1&\lambda-1&t(\lambda-1) \end{bmatrix}. \\]

Its \\(2\times2\\) minors using the first two columns include

\\[ \lambda^2,\qquad \lambda(\lambda-1),\qquad 1-\lambda^2. \\]

Since

\\[ \gcd(\lambda^2,1-\lambda^2)=1, \\]

the pencil has rank two for every finite complex \\(\lambda\\).

In particular, at \\(\lambda=0\\), its first row is zero, but the remaining two rows are independent.

This already disproves the claimed compressed-pencil obstruction. More importantly, the example can be realized by fixed observer data.

### 1.4 An explicit fixed-\\(L_0\\) observer family with \\(\omega=2,q=3,c=2\\)

The following construction is a stronger counterexample: it satisfies the original observer conditions, has a fixed \\(A,C,L_0\\), and has a variable two-dimensional kernel.

Take \\(n=10\\), with standard basis \\(e_1,\ldots,e\_{10}\\). Define \\(A\\) by

\\[ \begin{aligned} Ae_1&=e_8,& Ae_2&=e_9,& Ae_3&=e\_{10},\\\ Ae_4&=0,& Ae_5&=0,& Ae_6&=0,& Ae_7&=0,\\\ Ae_8&=e_5,& Ae_9&=e_6,& Ae\_{10}&=e_7. \end{aligned} \\]

Take

\\[ C= \begin{bmatrix} e_5^\*\\\e_6^\*\\\e_7^\* \end{bmatrix}, \qquad L_0=e_1^\*. \\]

Then

\\[ CA= \begin{bmatrix} e_8^\*\\\e_9^\*\\\e\_{10}^\* \end{bmatrix}, \\]

so

\\[ K_0=\ker[C;CA] =\operatorname{span}\\{e_1,e_2,e_3,e_4\\}. \\]

Use

\\[ N=[e_1,e_2,e_3,e_4]. \\]

For every \\(t\in\mathbb C\\), define

\\[ L(t)= \begin{bmatrix} e_1^\*\\\ e_2^\*+t e_3^\*+e_8^\*\\\ e_1^\*+e_2^\*+t e_3^\*+e_8^\*+e_9^\*+t e\_{10}^\* \end{bmatrix}. \\]

The first row is exactly the prescribed, fixed \\(L_0\\).

Direct multiplication gives

\\[ \boxed{ H(t)=L(t)N= \begin{bmatrix} 1&0&0&0\\\ 0&1&t&0\\\ 1&1&t&0 \end{bmatrix}, } \\]

and

\\[ \boxed{ H_A(t)=L(t)AN= \begin{bmatrix} 0&0&0&0\\\ 1&0&0&0\\\ 1&1&t&0 \end{bmatrix}. } \\]

Let

\\[ D= \begin{bmatrix} 0&0&0\\\ 1&0&0\\\ 1&1&0 \end{bmatrix}. \\]

Then

\\[ H_A(t)=DH(t) \\]

for every \\(t\\).

The kernel is

\\[ \boxed{ V_t=\ker H(t) =\operatorname{span}\\{-t e_2+e_3,\ e_4\\}. } \\]

Thus \\(V_t\\) is a genuinely variable two-plane in \\(K_0\\). In particular,

\\[ k=4,\qquad \omega=2,\qquad c=2,\qquad q=3. \\]

The pencil is

\\[ P_t(\lambda)= \begin{bmatrix} \lambda&0&0&0\\\ -1&\lambda&\lambda t&0\\\ \lambda-1&\lambda-1&t(\lambda-1)&0 \end{bmatrix}. \\]

For completeness, all potentially nonzero \\(2\times2\\) minors are as follows:

| Row pair    | Column pair | Minor                     |
| ----------- | ----------- | ------------------------- |
| \\((1,2)\\) | \\((1,2)\\) | \\(\lambda^2\\)           |
| \\((1,2)\\) | \\((1,3)\\) | \\(t\lambda^2\\)          |
| \\((1,3)\\) | \\((1,2)\\) | \\(\lambda(\lambda-1)\\)  |
| \\((1,3)\\) | \\((1,3)\\) | \\(t\lambda(\lambda-1)\\) |
| \\((2,3)\\) | \\((1,2)\\) | \\(1-\lambda^2\\)         |
| \\((2,3)\\) | \\((1,3)\\) | \\(t(1-\lambda^2)\\)      |

All other \\(2\times2\\) minors vanish because the fourth column is zero or the selected columns are dependent.

Since

\\[ \gcd(\lambda^2,1-\lambda^2)=1, \\]

we obtain

\\[ \operatorname{rank}P_t(\lambda)=2 \qquad\forall t,\lambda\in\mathbb C. \\]

The full observer conditions also hold:

- \\(\operatorname{rank}[C;CA]=6\\);
- \\(\operatorname{rank}[C;L(t)]=6=p+q\\);
- \\(\operatorname{rank}[L(t);CA;C]=8\\);
- \\(\operatorname{rank}[LA;L;CA;C]=8\\);
- \\(\operatorname{rank}[\lambda L-LA;CA;C]=8\\) for every \\(\lambda\\).

The last two follow directly from the compressed rank calculations and the fact that \\(H_A=DH\\).

Thus this is a valid family under the stronger independence convention \\(\mathsf P\_{\mathrm{ind}}\\).

Explicit counterexample

The fixed-\\(L_0\\) variable-kernel route is possible already for \\(\omega=2,q=3,c=2\\).

This answers Report 68 Question 1 affirmatively and refutes the proposed \\(\omega\ge4\\) necessity in Question 2.

It also shows that the shift-chain idea can be implemented with a fixed first row. The chain is

\\[ w_0\longmapsto w_1\longmapsto g\_{\mathrm{out}}, \\]

where

\\[ w_0=(1,0,1)^T,\quad w_1=(0,1,1)^T,\quad g\_{\mathrm{out}}=(0,0,1)^T. \\]

The map \\(D\\) sends \\(w_0\\) to \\(w_1\\) and \\(w_1\\) to \\(g\_{\mathrm{out}}\\). In the output basis \\((w_0,w_1,g\_{\mathrm{out}})\\), the selected minor of \\((\lambda I-D)|\_W\\) is

\\[ \begin{bmatrix} -1&\lambda\\\ 0&-1 \end{bmatrix}, \\]

with determinant \\(1\\).

The arithmetic parameter \\(t\\) enters the domain map \\(H(t)\\), not the spectral shift. This gives a clean separation between variable kernel and uniform spectral control.

The construction does not yet encode an arithmetic equation: every \\(t\in\mathbb C\\) is feasible. But it decisively removes the proposed fixed-\\(L_0\\), low-dimensional impossibility barrier.

### 1.5 The two obstructions in Part II.4 are architecture-specific

The report identifies two failures:

- a particular shift-\\(A\\) architecture;
- an architecture with \\(A(W)\subseteq S\\), leading to a zero-column/eigenvalue dilemma.

These observations may be correct for the specific structural assumptions used in those attempts. They do not establish a general obstruction.

The new \\(10\\)-dimensional construction illustrates why. It uses

\\[ A(K_0)=\operatorname{span}\\{e_8,e_9,e\_{10}\\}, \\]

which is disjoint from \\(K_0\\), and the row-pair map can realize the shift-compatible compressed pairs.

The important point is that the variable direction is not required to map into a fixed subspace of the compressed image in the manner assumed by the failed architectures.

The correct conclusion is:

- retain the zero-column/eigenvector analysis as a diagnostic for restricted designs;
- do not promote it to a general lower bound on \\(\omega\\);
- test proposed constructions at the level of the full pair map \\(\Psi\\), not only at the level of an abstract \\(D\\).

68_single_gate_barriers.md

## 2. Report 68 Part II.5: the isolated-kernel phenomenon can be proved exactly

The report's experiments concern the feasible instance with \\(\dim W_L=3\\). The earlier report defining that instance gives

\\[ \begin{aligned} Ae_1&=e_2,& Ae_2&=e_1,& Ae_3&=e_3+e_2,\\\ Ae_4&=e_4,& Ae_5&=e_5,& Ae_6&=3e_6+e_2, \end{aligned} \\]

with

\\[ C=e_1^\*,\qquad L_0=e_3^\*. \\]

It also supplies the feasible witness

\\[ L= \begin{bmatrix} e_3^\*\\\ e_3^\*+e_6^\*\\\ e_2^\*+e_3^\*+e_6^\* \end{bmatrix}. \\]

60_deliverables_and_rank_strata.md

I can strengthen the report's finite search substantially: for this instance, one can classify all candidate planes in \\(\operatorname{Gr}(2,W_L)\\), not just the sampled planes.

### 2.1 Compute \\(K_0\\) and \\(W_L\\)

We have

\\[ CA=e_2^\*, \\]

so

\\[ K_0=\operatorname{span}\\{e_3,e_4,e_5,e_6\\}. \\]

Take

\\[ N=[e_3,e_4,e_5,e_6]. \\]

Moreover,

\\[ L_0N=(1,0,0,0), \qquad L_0AN=(1,0,0,0). \\]

Hence

\\[ W_L=\ker[L_0N;L_0AN] =\operatorname{span}\\{e_4,e_5,e_6\\}. \\]

Every feasible two-dimensional kernel \\(V\\) must be contained in \\(W_L\\), so the search space is indeed

\\[ \operatorname{Gr}(2,W_L)\cong\mathbb P^2. \\]

### 2.2 Parameterize an arbitrary plane

Every two-plane in \\(W_L\\) is the kernel of a nonzero covector

\\[ u=a e_4^\*+b e_5^\*+c e_6^\*, \\]

where \\((a,b,c)\ne(0,0,0)\\), with scalar multiples defining the same plane.

Since \\(L_0N=e_3^\*\\), the annihilator of \\(V\\) in \\(K_0^\*\\) is

\\[ \operatorname{Ann}(V) =\operatorname{span}\\{h_0,u\\}, \qquad h_0=e_3^\*. \\]

Every bottom row \\(\ell_i\\) of a feasible \\(L\\) must therefore have compressed row

\\[ h_i=\ell_iN=\alpha_i h_0+\beta_i u. \\]

Write

\\[ \eta_i=\ell_i(e_2). \\]

Using the actions of \\(A\\), we get

\\[ \boxed{ h\_{A,i}=\ell_iAN = (\alpha_i+\eta_i,\ \beta_i a,\ \beta_i b,\ 3\beta_i c+\eta_i). } \\]

Condition (5a) requires \\(h\_{A,i}\in\operatorname{span}\\{h_0,u\\}\\).

### 2.3 Every plane other than \\(V\_{45}\\) fails (5b)

Suppose

\\[ (a,b)\ne(0,0). \\]

Comparing the \\(e_4^\*\\) and \\(e_5^\*\\) coordinates in

\\[ h\_{A,i}\in\operatorname{span}\\{h_0,u\\} \\]

forces the coefficient of \\(u\\) to be \\(\beta_i\\). The \\(e_6^\*\\) coordinate then gives

\\[ 3\beta_i c+\eta_i=\beta_i c, \\]

so

\\[ \eta_i=-2\beta_i c. \\]

Consequently,

\\[ h\_{A,i} =(\alpha_i-2\beta_i c)h_0+\beta_i u. \\]

The top row is fixed:

\\[ h\_{A,0}=h_0. \\]

At \\(\lambda=1\\), the first row of \\(P(1)\\) is zero. Every bottom row is

\\[ h_i-h\_{A,i}=2\beta_i c\\,h_0. \\]

Thus

\\[ \boxed{ \operatorname{rank}P(1)\le1<2. } \\]

This argument applies to every possible choice of bottom-row lifts. It is not a calculation for one particular \\(L\\).

Therefore no plane with \\((a,b)\ne(0,0)\\) can be feasible.

The remaining case is

\\[ a=b=0,\qquad c\ne0. \\]

Then \\(u\\) is proportional to \\(e_6^\*\\), and

\\[ \boxed{ V=\operatorname{span}\\{e_4,e_5\\}=V\_{45}. } \\]

This is the only candidate plane not ruled out by the spectral condition.

### 2.4 The remaining plane is feasible

Use the witness from the earlier report:

\\[ L= \begin{bmatrix} e_3^\*\\\ e_3^\*+e_6^\*\\\ e_2^\*+e_3^\*+e_6^\* \end{bmatrix}. \\]

Its compressed matrices, using coordinates \\((e_3,e_6)\\) on the row space, are

\\[ H= \begin{bmatrix} 1&0\\\ 1&1\\\ 1&1 \end{bmatrix}, \qquad H_A= \begin{bmatrix} 1&0\\\ 1&3\\\ 2&4 \end{bmatrix}. \\]

The pencil is

\\[ P(\lambda)= \begin{bmatrix} \lambda-1&0\\\ \lambda-1&\lambda-3\\\ \lambda-2&\lambda-4 \end{bmatrix}. \\]

Its three maximal minors are

\\[ \begin{aligned} \Delta\_{12}(\lambda)&=(\lambda-1)(\lambda-3),\\\ \Delta\_{13}(\lambda)&=(\lambda-1)(\lambda-4),\\\ \Delta\_{23}(\lambda)&=-2. \end{aligned} \\]

The constant minor \\(-2\\) proves

\\[ \operatorname{rank}P(\lambda)=2 \quad\forall\lambda\in\mathbb C. \\]

The full row-independence condition also holds, as recorded in the earlier report.

We have therefore proved the exact classification:

\\[ \boxed{ \\{V\in\operatorname{Gr}(2,W_L): V\text{ admits a feasible lift}\\} = \\{V\_{45}\\}. } \\]

This is stronger than the finite search in Report 68. It proves that the feasible-kernel locus is a singleton in the full complex Grassmannian for this particular observer instance.

The finite search over 18 candidates does not, by itself, establish this: \\(\operatorname{Gr}(2,3)\\) over \\(\mathbb C\\) has infinitely many points. The argument above supplies the missing global classification.

Interpretation: the isolated-kernel phenomenon is real for this instance, but it is instance-specific. It is not a universal consequence of fixed \\(L_0\\), \\(q=3\\), or \\(\omega=2\\). The explicit \\(10\\)-dimensional family in Section 1.4 gives the contrasting positive-dimensional case.

68_single_gate_barriers.md

## 3. Report 68 Part II.6: the fixed-kernel lift family works, but one claim is incorrect

The report gives

\\[ H= \begin{bmatrix} 1&0\\\ 1&1\\\ 1&1 \end{bmatrix}, \qquad H_A(s)= \begin{bmatrix} 1&0\\\ 1&3\\\ 1+s&3+s \end{bmatrix}. \\]

These are the compressed matrices in the coordinates \\((e_3,e_6)\\).

The pencil is

\\[ P_s(\lambda)= \begin{bmatrix} \lambda-1&0\\\ \lambda-1&\lambda-3\\\ \lambda-1-s&\lambda-3-s \end{bmatrix}. \\]

Its three \\(2\times2\\) minors are

\\[ \begin{aligned} \Delta\_{12}(\lambda,s) &=(\lambda-1)(\lambda-3),\\\ \Delta\_{13}(\lambda,s) &=(\lambda-1)(\lambda-3-s),\\\ \Delta\_{23}(\lambda,s) &=-2s. \end{aligned} \\]

Therefore

\\[ \boxed{ s\ne0 \quad\Longrightarrow\quad \operatorname{rank}P_s(\lambda)=2 \quad\forall\lambda. } \\]

At \\(s=0\\), however,

\\[ \Delta\_{23}=0, \\]

and the first two minors share the factor \\(\lambda-1\\). In fact,

\\[ \operatorname{rank}P_0(1)=1. \\]

Thus the statement in Report 68 that the pencil is still good at \\(s=0\\) is incorrect. At \\(s=0\\), the pencil fails (5b), in addition to the reported failure of

\\[ \operatorname{rank}[C;L]=p+q. \\]

The corrected conclusion is:

- for \\(s\ne0\\), the pencil is spectrally good and the independence condition holds;
- for \\(s=0\\), the pencil is spectrally bad and the independence condition fails.

So the feasible set along this family is indeed

\\[ \mathbb C^\times. \\]

The report's main interpretation remains correct: this lift parameter is free on an open set. It does not impose a relation such as \\(s=xy\\). But the exact reason for exclusion at zero must be corrected.&#x20;

68_single_gate_barriers.md



# Part XII. Report 69: adjudication of the free-witness obstruction

## 4. There is no general open-or-finite theorem

The proposed general theorem in Report 69 is false.

The report correctly observes that rank conditions define constructible sets and that their projections remain constructible. But it then asks whether the fibres of the projection must be either open or finite.

There is no such general dichotomy.

Let

\\[ F=\\{(x,y,z)\in\mathbb C^3:z=xy\\}. \\]

This is a closed algebraic set. Its projection onto the \\(z\\)-coordinate is all of \\(\mathbb C\\), because for every \\(z\\) we may choose \\(x=1,y=z\\).

But the fibres are

\\[ F_z=\\{(x,y):xy=z\\}. \\]

For \\(z\ne0\\), each fibre is a one-dimensional hyperbola. For \\(z=0\\), it is the union of the two coordinate axes. These fibres are neither finite nor open subsets of \\(\mathbb C^2\\).

More generally, constructible subsets of affine varieties can have fibres of many different dimensions and shapes. Chevalley's theorem says that projections of constructible sets are constructible; it does not say that fibres are open or finite.

The correct general statement is only:

\\[ \boxed{ \text{Observer feasibility is constructible, and its projections are constructible.} } \\]

No stronger open-or-finite conclusion follows from constructibility alone.

### 4.1 Rank equalities can force multiplication directly

A particularly simple counterexample to the suggested obstruction is

\\[ G(x,y,z)= \begin{bmatrix} 1&x\\\ y&z \end{bmatrix}. \\]

Because the upper-left entry is fixed and nonzero,

\\[ \operatorname{rank}G(x,y,z)=1 \\]

is equivalent to

\\[ \det G(x,y,z)=0. \\]

Hence

\\[ \boxed{ \operatorname{rank} \begin{bmatrix} 1&x\\\ y&z \end{bmatrix} =1 \iff z=xy. } \\]

This is a single rank equality that forces an exact multiplication relation. There is no auxiliary parameter that can absorb the equation once \\(x,y,z\\) are the entries of the specified matrix.

Thus the difficulty is not that rank equalities cannot encode multiplication. They plainly can.

The difficulty is to realize such a determinantal gate inside the particular observer conditions, with fixed \\(A,C,L_0\\), while controlling every other witness degree of freedom.

## 5. What the free-witness obstruction really says

The report's central concern is nevertheless important.

Suppose a proposed construction has a parameter \\(s\\) appearing in a lift direction, and feasibility only requires

\\[ s\ne0. \\]

Then \\(s\\) is not constrained to equal the output of a multiplication gate. It can be chosen independently, and the construction does not encode the intended relation.

That is a genuine failure of that particular gadget.

But it does not establish a general impossibility theorem.

The distinction is:

- free nuisance parameter: a variable that can be changed without affecting the intended arithmetic relation;
- constrained witness variable: a variable that is extracted from \\(L\\) and whose value is tied to other extracted variables by a rank equality;
- gauge freedom: different choices of \\(L\\) that represent the same intended arithmetic assignment.

A valid reduction may have free nuisance parameters and gauge freedom. What matters is that every feasible \\(L\\) must yield a valid source assignment.

The formal requirement is

\\[ \begin{aligned} &\text{source instance has a solution}\\\ &\qquad\Longleftrightarrow\\\ &\exists L\text{ satisfying (5a), (5b), and the prescribed rank convention}. \end{aligned} \\]

For soundness, one must define an extraction map

\\[ \pi:L\longmapsto(x_1,\ldots,x_m) \\]

such that every feasible \\(L\\) gives a source solution. The extraction must be well-defined on all feasible witnesses, not just on one convenient parameterization.

This is the real missing ingredient.

## 6. The lift directions cannot encode the gate if they are completely invisible

The earlier pair-map framework makes this point precise.

If

\\[ g\in\ker\Psi, \\]

then

\\[ gN=0,\qquad gAN=0. \\]

Replacing a row \\(l_i\\) by \\(l_i+g\\) leaves both compressed rows unchanged:

\\[ (l_i+g)N=l_iN,\qquad (l_i+g)AN=l_iAN. \\]

Therefore it leaves \\(H,H_A\\), the kernel \\(V\\), and the compressed pencil unchanged.

Such directions can help satisfy row-independence requirements, but they cannot impose a polynomial equation through (5a) or (5b).

The Report 68 family uses a slightly larger lift direction: \\(gN=0\\) but \\(gAN\ne0\\). That direction changes \\(H_A\\), so it is not invisible to the pencil. Nevertheless, in the tested family it only creates the open condition \\(s\ne0\\).

The correct lesson is:

- use \\(\ker\Psi\\) for independent row completion;
- use \\(gN=0,\ gAN\ne0\\) directions only when their effect on \\(H_A\\) is part of a genuine determinantal constraint;
- do not treat row-completion freedom as an arithmetic encoding mechanism.

69_free_witness_obstruction.md

# Part XIII. A more promising architecture for the hardness programme

## 7. Separate the arithmetic gate from the spectral guard

The explicit \\(10\\)-dimensional construction above suggests a better architecture.

Use two logically separate mechanisms:

1. A spectral guard whose shift-chain minor is a fixed nonzero constant.
2. An arithmetic gate encoded by a rank equality in the observer feasibility conditions.

The spectral guard should not be responsible for distinguishing satisfying from nonsatisfying arithmetic assignments. It should guarantee that the pencil condition is automatically satisfied throughout the intended arithmetic parameter space.

The arithmetic gate should impose the polynomial relation.

This avoids the mistake of asking the arithmetic block itself to have a favorable spectral structure.

### 7.1 The natural arithmetic gate

For a multiplication equation

\\[ z=xy, \\]

use the anchored matrix

\\[ G(x,y,z)= \begin{bmatrix} 1&x\\\ y&z \end{bmatrix}. \\]

The rank-one constraint

\\[ \operatorname{rank}G=1 \\]

is exactly the desired equation.

The challenge is to make this matrix, or its Schur complement, appear as a forced submatrix of one of the observer rank constraints.

For example, if a suitable pivot block \\(I_s\\) is fixed, then a matrix of the form

\\[ \begin{bmatrix} I_s&U\\\ V&G \end{bmatrix} \\]

has rank

\\[ s+\operatorname{rank}(G-VU) \\]

when the pivot block is invertible. Thus a rank threshold can impose a rank condition on the Schur complement.

The observer problem already has a natural rank-inclusion condition:

\\[ \operatorname{rank}[LA;L;CA;C] = \operatorname{rank}[L;CA;C]. \\]

It is therefore reasonable to seek a block arrangement in which the residual of a selected row of \\(LA\\), after elimination against a fixed pivot block in \\([L;CA;C]\\), contains the entries

\\[ 1,\quad x,\quad y,\quad z \\]

in the required pattern.

This is a concrete target for the next gadget.

It is not yet a construction: the difficult part is ensuring that the pivot block is forced, the residual entries are canonically determined by \\(L\\), and no other rows of \\(L\\) can compensate for a failed gate.

## 8. The spectral guard can be the construction from Section 1.4

The \\(10\\)-dimensional family gives a useful base block with:

- fixed \\(A,C,L_0\\);
- fixed output image \\(W\\);
- a variable kernel;
- a uniform unit-minor spectral certificate;
- the stronger row-independence condition.

This means the next gate need not solve the spectral problem from scratch.

The remaining task is to couple the arithmetic variables to the pair-map realization constraints without changing the fixed shift pivots.

One possibility is to enlarge the compressed domain with additional coordinates carrying the gate variables, while keeping the two shift-chain columns as the spectral guard. The extra coordinates must not introduce new independent columns in \\(P(\lambda)\\) that can lose rank.

A second possibility is to put the arithmetic gate in the row-space inclusion (5a), leaving the pencil block untouched.

I would test the second possibility first. It separates the two tasks most cleanly.

## 9. What should be fixed, and what should remain variable?

The reduction should have the following organization.

| Object                       | Role                                               | Status                |
| ---------------------------- | -------------------------------------------------- | --------------------- |
| \\(A,C,L_0,q\\)              | Encodes the source instance and the gate structure | Fixed input           |
| \\(H\\)'s first row          | Provides a fixed anchor                            | Fixed                 |
| Graph coordinates of \\(V\\) | Represent arithmetic variables                     | Witness-extracted     |
| Shift-chain block            | Guarantees spectral admissibility                  | Fixed pivots          |
| Multiplication block         | Enforces \\(z=xy\\)                                | Determinantal         |
| \\(\ker\Psi\\) directions    | Complete row independence                          | Nuisance freedom only |

The phrase input-determined parameter should be used carefully. The source variables in an \\(\exists\mathbb R\\) reduction are not numerically fixed by the input; they are existentially quantified. What is required is that they be canonically recoverable from every feasible witness.

That is enough for soundness.

## 10. Is varying the input rather than \\(L\\) a solution?

Not for the same decision problem.

In a many-one reduction to the observer feasibility problem, \\(A,C,L_0,q\\) are constructed from the source instance and then fixed. The unknown source assignment must be represented by the existential witness \\(L\\), or by other quantified variables that are legitimately part of the target problem.

Allowing \\(A\\) itself to vary existentially would define a different target problem unless that variation can be encoded in \\(L\\) while preserving the required fixed-input structure.

It is entirely appropriate for the reduction to make \\(A,C,L_0\\) depend on the coefficients of the source polynomial system. It is not appropriate to make them depend on the unknown solution of that system.

# Part XIV. Revised answers to the questions in the reports

## Report 68

Question 1: Is a variable-kernel family with fixed \\(L_0\\) possible?

Yes. The explicit \\(n=10,p=3,q=3\\) construction in Section 1.4 proves it, even with

\\[ \omega=2,\qquad c=2, \\]

and \\(\mathsf P\_{\mathrm{ind}}\\).

Question 2: Is \\(\omega\ge4\\) necessary? What is the minimum architecture?

No. The proposed lower bound is false. The example uses

\\[ \omega=2,\qquad q=3=\omega+1. \\]

The architecture is a two-dimensional shift chain with one leakage coordinate. This is already enough.

Question 3: Can a rank equality force \\(s=xy\\), rather than merely \\(s\ne0\\)?

Yes in principle: the anchored rank-one gate

\\[ \operatorname{rank} \begin{bmatrix} 1&x\\\y&z \end{bmatrix}=1 \\]

is exactly \\(z=xy\\).

The unresolved problem is embedding this gate into (5a) or another forced observer rank equality, with soundness against all other lifts.

Question 4: Is there a different hardness mechanism?

The strongest next candidate is to encode the arithmetic gate in (5a), while using the fixed shift-chain construction to make (5b) automatic.

Varying \\(A\\) existentially would change the target problem. Completely invisible lift directions cannot encode the gate.

Question 5: Can the symbolic family in II.5 be checked using all minors?

Yes. For the \\(\dim W_L=3\\) instance from the earlier report, the exact calculation in Section 2 proves that every plane except \\(V\_{45}\\) fails. In particular, every plane in the family

\\[ V_t=\operatorname{span}\\{e_4,e_5+t e_6\\} \\]

with \\(t\ne0\\) fails at \\(\lambda=1\\). This is a complete symbolic proof, not just a sample of minors or a finite search.

## Report 69

Is the free-witness obstruction a theorem?

No, not in the proposed constructibility/open-or-finite form. Constructibility permits arbitrary algebraic relations and positive-dimensional fibres.

Can rank equalities force arithmetic relations?

Yes. The \\(2\times2\\) rank-one gate proves this immediately.

What remains genuinely difficult?

The observer-specific realization problem:

- fixed \\(A,C,L_0\\);
- canonical extraction of arithmetic variables from \\(L\\);
- exact enforcement of multiplication by (5a) or a related rank equality;
- no spurious solutions from alternative lifts;
- uniform spectral feasibility for every intended arithmetic assignment.

# Part XV. Recommended next research steps

I would revise the work programme in the following order.

### Priority 1: Correct the record

Make four corrections:

1. Replace the \\(\omega=2,q=3\\) impossibility claim in Report 68 by the explicit fixed-\\(L_0\\) counterexample above.
2. Replace the suggested lower bound \\(\omega\ge4\\) by the observation that \\(\omega=2,q=3\\) already suffices.
3. Correct the \\(s=0\\) statement in Part II.6: the pencil itself fails (5b) at \\(\lambda=1\\).
4. Replace the finite-search-only claim about the unique good plane in the \\(\dim W_L=3\\) instance by the exact all-plane classification in Section 2.

### Priority 2: Formalize the fixed-\\(L_0\\) spectral architecture

The \\(10\\)-dimensional example is a useful lemma:

> There exist fixed \\(A,C,L_0\\) and a one-parameter family \\(L(t)\\) with fixed \\(\operatorname{im}H(t)\\), variable \\(\ker H(t)\\), and a constant unit minor certifying (5b) for all \\(t\\).

It is worth recording the construction and its exact calculations as a reusable spectral base.

### Priority 3: Build a multiplication gate into (5a)

Do not spend the next round trying to make the free lift parameter \\(s\\) equal \\(xy\\) by an open rank condition.

Instead, construct an anchored \\(2\times2\\) gate and attempt to make its determinant a forced residual minor in the row-space inclusion

\\[ \operatorname{row}(LA) \subseteq \operatorname{row}[L;CA;C]. \\]

The key proof obligation is that the gate entries are canonically recovered from \\(L\\), and that the row-space equality forces the determinant to vanish.

### Priority 4: Prove soundness before scaling up

For one multiplication gate, establish:

\\[ \text{observer feasibility} \Longrightarrow z=xy \\]

for every feasible \\(L\\), not merely for a selected normal-form witness.

Then prove the reverse direction by constructing \\(L\\) from any solution of \\(z=xy\\).

Only after this should variable sharing and circuit composition begin.

## Final research judgement

Reports 68 and 69 contain important progress, but their strongest negative conclusions are too broad.

The central correction is that fixed \\(L_0\\) does not prevent a variable kernel, even in the smallest nontrivial spectral dimensions. The explicit \\(10\\)-dimensional construction establishes a variable two-plane kernel, fixed first row, fixed observer data, uniform spectral admissibility, and the stronger row-independence condition.

The \\(\dim W_L=3\\) example exhibits the opposite phenomenon: its feasible kernel is exactly one plane. Both behaviours occur, so neither should be elevated to a universal rigidity principle.

Likewise, the free-witness concern is not a general algebraic obstruction. Rank equalities can encode multiplication exactly. The real difficulty is embedding the determinantal gate into the observer structure and proving that every feasible witness decodes to a valid arithmetic assignment.

Recommended direction

Continue the hardness programme, but change its immediate target. The next milestone should be a one-gate realization through (5a), with the shift-chain construction supplying a uniform spectral guard. This is more promising than further attempts to force arithmetic through the open lift condition \\(s\ne0\\), and it addresses the actual obstruction identified by the two reports.