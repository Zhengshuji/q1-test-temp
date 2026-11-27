# Independent mathematical review of the MIN-ROWS / q1 project

Research assessment · 8 November 2026

## 1. Overall assessment

My assessment is that the project has developed into a substantial and mathematically coherent research programme. Its most important achievement is not yet a complexity classification, but the discovery of a useful geometric structure connecting:

1. the original observer-order problem;
2. compressed matrix pencils and their constant-rank condition;
3. the geometry of Grassmannians and invariant-subspace incidence varieties;
4. the lifting of compressed solutions to genuinely independent rows;
5. polynomial certificates for spectral feasibility.

The reduction chain

\\[ R\longmapsto(H,H_A)\longmapsto Z \longmapsto\text{incidence space} \\]

is a sensible organising framework. It separates several mathematical difficulties that would otherwise be mixed together.

However, I would distinguish three levels of achievement.

| Level                                    | Assessment                                                                                               |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Linear-algebraic reductions              | Substantially developed; several identities have strong formal verification                              |
| Geometric structure and component bounds | Strong for the hyperplane case; promising for \\(c=2\\); incomplete for \\(c=3\\) and general \\(c\\)    |
| Algorithmic complexity                   | An existential-real upper-bound route is available; hardness and a polynomial-time algorithm remain open |

There are also two issues that deserve more attention than they receive in the report.

First, the compressed geometric problem and the original MIN-ROWS problem are not interchangeable without a precise lifting theorem. This is the most important technical issue in the current project.

Second, component counting is not the same as algorithmic complexity. Even a small number of irreducible components does not automatically yield an efficient decision procedure. The geometry of the spectral-good locus inside each component must also be understood.

I recommend continuing the project, but changing the immediate objective. Rather than trying to establish a general component bound or prove hardness immediately, I would first establish a completely correct equivalence between the original feasibility problem and a finite, explicit system of algebraic constraints, including the lift-completion conditions.

That would provide a reliable foundation for both the geometric and computational parts.

# Part I. Audit of the mathematical framework

## 2. The original problem and its algebraic meaning

You seek the minimum number of rows of \\(L\\), subject to

\\[ \operatorname{rank}[LA;L;CA;C] = \operatorname{rank}[L;CA;C], \tag{5a} \\]

and

\\[ \operatorname{rank}[\lambda L-LA;CA;C] = \operatorname{rank}[L;CA;C] \qquad \forall\lambda\in\mathbb C. \tag{5b} \\]

The first condition says

\\[ \operatorname{row}(LA) \subseteq \operatorname{row}[L;CA;C]. \\]

The second says that the pencil has constant rank equal to the rank of the matrix at infinity.

These are fundamentally different types of restrictions:

- (5a) is an algebraic compatibility condition on the row spaces.
- (5b) is a global spectral condition on a matrix pencil.

This distinction is important throughout the project.

### 2.1 A preliminary issue: the full-row-rank convention

The report uses several rank conventions that should be unified in the paper.

In particular, distinguish:

\\[ \operatorname{rank}L=q \\]

from

\\[ \operatorname{rank}[C;L]=p+q. \\]

The latter is stronger and is essential to the lifting and row-completion arguments.

If the intended original problem requires only \\(L\\) to have full row rank, then the completion theorem must explain why independence modulo \\(\operatorname{row}C\\) is required or how it is incorporated into the original formulation.

If the intended problem requires independence of the rows of \\(C\\) and \\(L\\) together, state that explicitly.

There is also a basic feasibility condition:

\\[ q\ge r,\qquad q\le n \\]

when \\(L_0\\) has \\(r\\) independent prescribed rows and \\(L\\) must have full row rank.

If \\([C;L]\\) must have full row rank, one additionally needs

\\[ p+q\le n. \\]

These should be stated at the outset rather than introduced implicitly in the lifting argument.

### 2.2 The coefficient field

The project works over \\(\mathbb C\\), and the condition in (5b) quantifies over all complex \\(\lambda\\).

This is mathematically convenient because:

- every nonconstant complex polynomial has a root;
- the spectral condition is equivalent to a gcd condition;
- the relevant Grassmannians and algebraic varieties are naturally complex varieties.

However, the complexity question requires a separate input model.

I recommend adopting:

- rational input matrices \\(A,C,L_0\\);
- rational encoding of their entries;
- complex unknown matrix entries represented by pairs of real variables;
- existential-real feasibility as the decision framework.

The distinction between arbitrary complex input and rational input should not be left implicit.

## 3. First compression: \\(R\mapsto(H,H_A)\\)

Let

\\[ K_0=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \qquad N_K\in\mathbb C^{n\times k} \\]

be a basis matrix of \\(K_0\\).

Set

\\[ H=LN_K,\qquad H_A=LAN_K. \\]

The first compression is mathematically well motivated.

### 3.1 Verification of the equivalence for (5a)

Because

\\[ K_0=\ker C\cap\ker(CA), \\]

restriction to \\(K_0\\) annihilates both \\(C\\) and \\(CA\\).

Consequently,

\\[ \operatorname{row}(LA) \subseteq \operatorname{row}[L;CA;C] \\]

is equivalent to

\\[ \operatorname{row}(H_A) \subseteq \operatorname{row}(H). \\]

Equivalently,

\\[ \boxed{\ker H\subseteq\ker H_A.} \\]

This is a correct and important reduction.

It is worth including the short annihilator argument explicitly in the paper. The equivalence depends on the identity

\\[ K_0^\perp=\operatorname{row}[C;CA]. \\]

It does not require \\(A(K_0)\subseteq K_0\\).

### 3.2 Verification of the spectral reduction

Let

\\[ \omega=\operatorname{rank}H. \\]

Under (5a), the inclusion of kernels gives a well-defined linear map

\\[ Z:\operatorname{im}H\longrightarrow\mathbb C^q, \qquad Z(Hx)=H_Ax. \\]

Then

\\[ H_A=ZH \\]

and

\\[ P(\lambda)=\lambda H-H_A =(\lambda I-Z)H. \\]

Since \\(H\\) induces an isomorphism

\\[ K_0/\ker H\cong\operatorname{im}H, \\]

we obtain

\\[ \operatorname{rank}P(\lambda) = \operatorname{rank}(\lambda I-Z). \\]

More precisely, the right-hand side means the rank of the map from \\(\operatorname{im}H\\) to \\(\mathbb C^q\\).

Now choose a decomposition

\\[ \mathbb C^q=\operatorname{im}H\oplus W'. \\]

Writing

\\[ Z= \begin{bmatrix} A\_\*\\\B\_\* \end{bmatrix}, \\]

we get

\\[ P(\lambda)\sim \begin{bmatrix} \lambda I\_\omega-A\_\*\\\ -B\_\* \end{bmatrix}. \\]

Therefore

\\[ \boxed{ \operatorname{rank}P(\lambda)<\omega \iff \exists y\ne0: \quad A\_\*y=\lambda y,\quad B\_\*y=0. } \\]

This is the right structural interpretation of the spectral condition.

### 3.3 An important conceptual consequence

The spectral condition is not simply an eigenvalue-avoidance condition for \\(A\_\*\\).

It says that no eigenvector of \\(A\_\*\\) is simultaneously annihilated by \\(B\_\*\\).

Equivalently,

\\[ \ker B\_\* \\]

must contain no nonzero eigenvector of \\(A\_\*\\).

This is closely related to observability and invariant-zero questions.

In particular, the pair \\((A\_\*,B\_\*)\\) should be studied using the theory of unobservable eigenvectors, invariant zeros, and matrix-pencil structure.

This connection may ultimately be more useful for the algorithmic problem than the raw gcd formulation.

## 4. Second compression: the pencil and its gcd

The equivalence

\\[ \operatorname{rank}P(\lambda)=\omega \quad\forall\lambda\in\mathbb C \\]

if and only if the gcd of the \\(\omega\times\omega\\) minors is a nonzero constant is correct, provided

\\[ \operatorname{normalrank}P=\omega. \\]

This last qualification should always appear.

The distinction between normal rank and pointwise rank is essential.

For a polynomial matrix \\(P(\lambda)\\), normal rank is the rank over the rational-function field \\(\mathbb C(\lambda)\\). The maximal minors vanish simultaneously at a finite point precisely when their gcd has a finite complex root.

Since the entries of \\(P\\) are affine polynomials, the condition is particularly tractable.

### 4.1 Projective closedness argument

The homogenisation argument is also sound in principle.

Consider

\\[ P_h(\lambda,\mu)=\lambda H-\mu H_A. \\]

At infinity, \\([\lambda:\mu]=[1:0]\\), and

\\[ P_h(1,0)=H. \\]

On the fixed layer \\(\operatorname{rank}H=\omega\\), the matrix at infinity has rank exactly \\(\omega\\).

The bad incidence set

\\[ \mathcal B= \left\\{ (x,[\lambda:\mu]): \operatorname{rank}P_h(x;\lambda,\mu)<\omega \right\\} \\]

is closed.

Its projection onto the parameter variety is closed because \\(\mathbb P^1\\) is proper.

Thus the bad locus is Zariski closed.

The consequence is useful:

On an irreducible parameter variety, either every point is bad or the good points form a nonempty Zariski-open dense subset.

This is a correct and powerful reduction.

However, it must be applied to the actual lifted parameter space, not merely to a compressed parameter space, unless a surjectivity and compatibility result has already been established.

That distinction is particularly important in the next section.

# Part II. The central difficulty: lifting compressed solutions

## 5. The exact sequence is the right framework

The report correctly identifies the missing information in the compressed pair.

The sequence

\\[ 0\longrightarrow E_C \longrightarrow \mathcal X^\*/\operatorname{row}C \overset{\rho}{\longrightarrow} K_0^\* \longrightarrow0 \\]

is the natural algebraic framework.

Here

\\[ E_C= \frac{\operatorname{row}[C;CA]}{\operatorname{row}C} \\]

and

\\[ d_C=\dim E_C = \operatorname{rank}[C;CA]-\operatorname{rank}C. \\]

The map \\(\rho\\) is restriction to \\(K_0\\).

This is an exact sequence because

\\[ \ker\rho = K_0^\perp/\operatorname{row}C = \operatorname{row}[C;CA]/\operatorname{row}C. \\]

Thus every compressed row on \\(K_0\\) has a lift, and the ambiguity in that lift is exactly \\(E_C\\).

This is the correct starting point for a completion theorem.

## 6. The correction involving \\(gAN\\) is essential and correct

Suppose

\\[ g=aC+bCA. \\]

Since

\\[ CAN=0, \\]

we have

\\[ gN=0 \\]

and

\\[ gAN = aCAN+bCA^2N = bCA^2N. \\]

Therefore, adding an invisible row \\(g\\) preserves \\(H=LN\\), but it need not preserve

\\[ H_A=LAN. \\]

This is a genuine issue, not a technicality.

The correct space of invisible directions preserving both compressed matrices is

\\[ E'\_C= \frac{ \\{g\in\operatorname{row}[C;CA]:gAN=0\\} }{ \operatorname{row}C }. \\]

The condition \\(gN=0\\) is redundant because every row in \\(\operatorname{row}[C;CA]\\) already annihilates \\(N\\).

Define

\\[ \Gamma:E_C\longrightarrow \mathbb C^{1\times k}, \qquad [g]\longmapsto gAN. \\]

This is well defined: if \\(g\\) is changed by a row in \\(\operatorname{row}C\\), then \\(gAN\\) is unchanged because \\(CAN=0\\).

Hence

\\[ E'\_C=\ker\Gamma \\]

and

\\[ \boxed{ d'\_C=d_C-\operatorname{rank}\Gamma. } \\]

This formula is correct.

It should replace the unqualified use of \\(d_C\\) whenever the purpose of completion is to preserve the entire compressed pair.

### 6.1 A further refinement

I recommend not treating \\(d'\_C\\) as a mysterious new numerical invariant.

Define the induced map explicitly:

\\[ \overline\Gamma: \frac{\operatorname{row}[C;CA]}{\operatorname{row}C} \longrightarrow \operatorname{rowspace}(CA^2N), \\]

where

\\[ \overline\Gamma([aC+bCA])=bCA^2N. \\]

Strictly speaking, the coefficient \\(b\\) is not unique if the rows of \\(C\\) and \\(CA\\) are dependent. The definition should therefore be made through \\(g\mapsto gAN\\), not through a chosen representation \\((a,b)\\).

This gives a basis-independent description.

In particular,

\\[ d'\_C = \dim\ker\overline\Gamma. \\]

It may be computable using only ranks of explicitly constructed matrices.

That should be investigated before the geometric algorithm is implemented.

## 7. The completion criterion: what is established and what needs qualification

The report gives two criteria:

\\[ q-\omega\le d_C \\]

for completion modulo \\(C\\), and

\\[ q-\omega\le d'\_C \\]

for completion preserving the compressed pair.

The second is the relevant criterion for the current spectral problem.

However, it is important to state the hypotheses precisely.

Assume:

1. the prescribed compressed pair \\((H,H_A)\\) is compatible with (5a);
2. the prescribed rows \\(L_0\\) are retained;
3. \\(\operatorname{rank}[C;L_0]=p+r\\);
4. the compressed row space has dimension \\(\omega\\);
5. the additional rows may be chosen freely.

Then the kernel of restriction to \\(K_0\\), on the final row space modulo \\(\operatorname{row}C\\), must have dimension

\\[ q-\omega. \\]

If the compressed pair is to remain unchanged, that kernel must lie in \\(E'\_C\\).

Consequently,

\\[ \boxed{q-\omega\le d'\_C} \\]

is necessary.

Under the stated freedom to choose the additional lifts, it is also sufficient for the row-independence completion.

The reason is straightforward: choose a basis of the required kernel subspace inside \\(E'\_C\\), then choose lifts of a basis of the prescribed compressed row space. These two sets of rows are independent modulo \\(\operatorname{row}C\\).

But this is a completion theorem for a prescribed compatible compressed pair. It is not a theorem that an arbitrary \\(V\\) in an admissible Grassmannian stratum gives a feasible original solution.

That distinction should be made explicit.

### 7.1 The fixed-row issue

The prescribed rows \\(L_0\\) cannot be altered.

Their compressed restrictions and their contributions to the kernel of restriction must be included in the completion construction.

A clean theorem should use the following notation:

\\[ \overline{\mathcal L}\_0 = \operatorname{span}\\{[l]:l\text{ is a row of }L_0\\} \subseteq \mathcal X^\*/\operatorname{row}C. \\]

Then one must extend this subspace to a \\(q\\)-dimensional subspace whose restriction to \\(K_0\\) has the prescribed image.

This formulation avoids accidentally counting the already available invisible directions twice.

The dimension inequality above is valid under the compatible extension hypotheses, but the paper should prove the extension statement with \\(L_0\\) fixed rather than only prove an abstract dimension count.

## 8. The most important remaining issue: compatibility of \\(V\\) with the lift

The report correctly identifies that for

\\[ V=\ker H\subseteq K_0, \\]

the compatibility condition is

\\[ \ker H\subseteq\ker H_A. \\]

But this condition needs to be incorporated into the construction of the lift, not merely checked after choosing \\(V\\).

Suppose we start with a compressed row map

\\[ H:K_0\longrightarrow\mathbb C^q \\]

having kernel \\(V\\).

An arbitrary lift of \\(H\\) determines \\(L\\), but its second compressed matrix \\(LAN_K\\) need not satisfy

\\[ \ker H\subseteq\ker(LAN_K). \\]

The appropriate procedure is therefore:

1. Choose the desired compressed map \\(H\\).
2. Choose a lift \\(L^{(0)}\\) of \\(H\\).
3. Write all possible lifts as\
   \\[\
   L=L^{(0)}+G,\
   \\]\
   where the rows of \\(G\\) belong to \\(\operatorname{row}[C;CA]\\).
4. Impose\
   \\[\
   (L^{(0)}+G)AN_K\big|\_V=0.\
   \\]
5. Impose the row-independence condition.
6. Impose the spectral condition on the resulting pencil.

The crucial observation is that step 4 is a linear condition on \\(G\\).

If the rows of \\(G\\) are chosen in \\(E'\_C\\), then \\(GAN_K=0\\), so the entire compressed pair is preserved. But if the chosen reference lift does not already satisfy the kernel inclusion, adding elements of \\(E'\_C\\) cannot repair that failure.

This gives a particularly important distinction:

\\[ \boxed{ \text{Preserving an admissible compressed pair} \neq \text{making an arbitrary compressed pair admissible}. } \\]

The report's diagnosis of the failed numerical pipeline is therefore correct.

### 8.1 My proposed replacement: an affine lift-feasibility theorem

Instead of trying to choose a basis of \\(E'\_C\\) first and then construct \\(L\\), formulate the lift problem as an affine linear system.

Let

\\[ \mathcal G=\operatorname{row}[C;CA] \\]

and let \\(\mathcal G_0\\) denote the corresponding space of allowed row corrections, taking account of the fixed rows \\(L_0\\).

For a prescribed compressed map \\(H\\), choose one particular lift \\(L^{(0)}\\).

The general lift has the form

\\[ L=L^{(0)}+G. \\]

The compatibility requirement is

\\[ G A N_K\big|\_V = -L^{(0)}A N_K\big|\_V. \tag{8.1} \\]

This is an affine linear equation in the coefficients of \\(G\\).

The solution set, if nonempty, is an affine space

\\[ G_0+\ker\mathcal T_V, \\]

where

\\[ \mathcal T_V:G\longmapsto GAN_K\big|\_V. \\]

The preserving subspace \\(E'\_C\\) is the kernel of the unrestricted map \\(G\mapsto GAN_K\\), but the relevant kernel in (8.1) is potentially larger because only the restriction to \\(V\\) must vanish.

This leads to an improvement over the current formulation.

The most general lift-feasibility test should use the restricted map \\(\mathcal T_V\\), not only the global invariant \\(d'\_C\\).

In particular, define

\\[ d'\_C(V)=\dim\ker\mathcal T_V. \\]

Then

\\[ d'\_C(V)\ge d'\_C. \\]

The quantity \\(d'\_C\\) measures freedom preserving the entire compressed pair. The larger \\(d'\_C(V)\\) measures freedom preserving only the required compatibility on \\(V\\).

This distinction could be useful for the \\(c=2\\) algorithm.

It also suggests that the lift problem may be easier than the current report assumes: one need not preserve the whole compressed pair if one can construct a compatible lift and subsequently test the resulting spectral pencil.

# Part III. The Grassmannian and incidence geometry

## 9. The exact fibre theorem

The fibre theorem is one of the strongest mathematical statements in the report.

Let

\\[ V\in\operatorname{Gr}(c,K_0), \\]

and define

\\[ W=V\cap A^{-1}V, \qquad t=\dim W, \qquad U=W+A(W). \\]

Consider

\\[ \Phi_V:V\longrightarrow\mathcal X/V, \qquad v\longmapsto Av+V. \\]

Then

\\[ \ker\Phi_V=W \\]

and

\\[ \operatorname{rank}\Phi_V=c-t. \\]

Now fix \\(W\\) and write

\\[ U=W+A(W). \\]

The condition

\\[ W\subseteq V\cap A^{-1}V \\]

is equivalent to

\\[ U\subseteq V. \\]

Furthermore, the equality

\\[ V\cap A^{-1}V=W \\]

is equivalent to

\\[ \operatorname{rank}\Phi_V=c-t. \\]

Therefore the fibre is

\\[ \mathcal F_W= \left\\{ V\in\operatorname{Gr}(c,K_0): U\subseteq V,\  \operatorname{rank}\Phi_V=c-t \right\\}. \\]

The subspaces containing \\(U\\) form

\\[ \operatorname{Gr}(c-\dim U,K_0/U). \\]

The rank condition is open, so

\\[ \boxed{ \mathcal F_W \text{ is an open subset of } \operatorname{Gr}(c-\dim U,K_0/U). } \\]

This is correct.

### 9.1 An important qualification

The quotient is

\\[ K_0/U, \\]

but the rank test takes values in

\\[ \mathcal X/V. \\]

One must not replace this with \\(K_0/V\\).

The reason is that \\(A(K_0)\\) need not be contained in \\(K_0\\).

This distinction is not cosmetic. It changes the geometry and can invalidate an otherwise plausible dimension calculation.

I recommend emphasizing this point in the statement and proof of the theorem.

### 9.2 What the theorem does not establish

The theorem describes the fibres over a fixed \\(W\\).

It does not establish that the base variety of admissible \\(W\\)'s is irreducible.

Nor does it establish that the total incidence space has a bounded number of irreducible components.

The implication

\\[ \text{irreducible base} + \text{nonempty open Grassmannian fibres} \Longrightarrow \text{irreducible total space} \\]

is valid under the usual local triviality and irreducibility hypotheses.

But it is not available when the base is merely a determinantal stratum whose irreducibility has not been proved.

This is precisely the gap that appears in the \\(c=3\\) problem.

## 10. The \\(c=2\\) classification

The six-layer classification is a substantial result.

The important achievement is that it replaces an unrestricted search over

\\[ \operatorname{Gr}(2,K_0) \\]

with a finite collection of geometrically meaningful cases.

The cases are:

1. Two distinct eigenlines.
2. A two-dimensional scalar eigenspace.
3. A length-two Jordan-chain configuration.
4. A one-dimensional invariant intersection with an invariant line.
5. A one-dimensional intersection with a non-invariant line.
6. The open stratum \\(t=0\\).

This classification is plausible and structurally well motivated.

However, I would not yet regard the component bound as completely paper-ready.

### 10.1 Three points requiring independent checking

A. The Jordan-chain lifting condition

The condition

\\[ \ell\subseteq(A-\lambda I)(K_0) \\]

must be interpreted carefully.

The eigenline must belong to the appropriate intersection of the eigenspace with the image of the restricted map.

It is not enough to know that \\(\ell\\) is an eigenline of \\(A\\).

The affine fibre dimension

\\[ \dim(E\_\lambda\cap K_0)-1 \\]

also needs verification in every degenerate case, including the possibility of an empty base.

B. The \\(t=1\\), non-invariant case

The condition

\\[ V=L+AL \\]

with

\\[ \operatorname{rank}[v,Av,A^2v]=3 \\]

is a good way to encode the non-invariant configuration.

The paper should explicitly prove both directions:

- every admissible \\(V\\) of this type arises from such a line \\(L\\);
- every line satisfying the stated rank condition produces exactly one such \\(V\\).

Otherwise, there is a risk of overcounting or omitting exceptional configurations.

C. The \\(t=0\\) stratum

This is an open subset of the Grassmannian, hence irreducible if nonempty.

But nonemptiness must be checked.

An empty stratum contributes no component.

A nonempty stratum contributes at most one.

This distinction should be reflected in the counting statement.

### 10.2 The component bound

The proposed estimate is

\\[ \boxed{ N_2\le \binom{s}{2}+3s+2. } \\]

I find this a reasonable theorem to pursue.

The counting is consistent with the six families:

\\[ \binom{s}{2} + s+s+s+1+1. \\]

The three \\(s\\)-dependent terms arise from the scalar, Jordan, and invariant-line cases.

The remaining two terms arise from the non-invariant and open cases.

But the theorem needs a formal component argument.

In particular:

- each eigenvalue-indexed family must be irreducible;
- the parameter map to the incidence space must not create additional components;
- the finite quotient by swapping two distinct eigenvalues must be treated correctly;
- the good spectral locus must be shown to be open in the relevant lifted parameter space.

I would present the bound initially as a theorem about the number of irreducible parameter-space components, and only then establish the corresponding statement for the actual lifted feasibility space.

This avoids conflating the compressed and lifted geometries.

Recommended result to consolidate

The \\(c=2\\) classification and its component bound are the strongest candidates for a standalone mathematical paper section, once the lift compatibility is incorporated.

## 11. The \\(c=3\\) problem

The report is right to suspend the proposed bound

\\[ \binom{s}{3}+3s^2+6s+1. \\]

The existence of eleven rank-type strata does not establish that there are eleven irreducible components.

These are different assertions.

A locally closed determinantal variety can be reducible, even when it is defined by only a small number of rank conditions.

### 11.1 Which strata need separate proofs?

I would divide the eleven strata into four groups.

| Stratum type         | Main issue                                       | Required proof                                            |
| -------------------- | ------------------------------------------------ | --------------------------------------------------------- |
| Six invariant types  | Eigenvalue coincidences and Jordan-chain lifting | Irreducibility of each eigenvalue-indexed parameter space |
| \\(t=2,\dim U=3\\)   | Exact-rank locus                                 | Independent determinantal irreducibility argument         |
| \\(t=2,\dim U=2\\)   | Open rank condition over a base                  | Base irreducibility and nonemptiness                      |
| \\(t=1\\), two types | Invariant versus non-invariant line geometry     | Irreducibility of each base and open fibres               |
| \\(t=0\\)            | Open Grassmannian stratum                        | Nonemptiness                                              |

The most suspicious stratum is

\\[ S\_{2,3} = \left\\{ W\in\operatorname{Gr}(2,D): \dim(W+A_0(W))=3 \right\\}. \\]

Here

\\[ D=K_0\cap A^{-1}K_0 \\]

and \\(A_0=A|\_D\\), with the understanding that \\(A(D)\subseteq K_0\\).

The condition is

\\[ \operatorname{rank} \left( A_0|\_W\bmod W \right)=1. \\]

This is an exact-rank condition, not simply a rank-at-most-one condition.

The distinction matters because

\\[ \\{\operatorname{rank}T\le1\\} \\]

is closed, whereas

\\[ \\{\operatorname{rank}T=1\\} \\]

is locally closed and can have several irreducible pieces.

### 11.2 A better approach to \\(S\_{2,3}\\)

I would study the incidence variety

\\[ \mathcal I= \left\\{ (W,\ell): W\in\operatorname{Gr}(2,D),\ \ell\in\mathbb P(D/W),\ A_0(W)\subseteq W+\ell \right\\}. \\]

The projection

\\[ \pi:\mathcal I\longrightarrow\operatorname{Gr}(2,D) \\]

has a unique \\(\ell\\) precisely when

\\[ \dim(W+A_0(W))=3. \\]

Thus the desired stratum is closely related to an open subset of an incidence variety.

The advantage is that the incidence description separates the rank condition into:

- a choice of a line in a quotient;
- a linear containment condition;
- an open condition guaranteeing exact dimension.

This may make irreducibility easier to establish.

But the incidence variety itself must be checked. It is not automatically irreducible.

### 11.3 Known reducibility phenomena

The warning about Springer fibres is appropriate.

Invariant-subspace varieties and quiver Grassmannians can have multiple irreducible components.

For example, the literature on Springer fibres and quiver Grassmannians contains explicit reducible varieties and component descriptions. See:

- Gerstenhaber’s work on varieties of commuting matrices;
- Ringel and Schmidmeier, Invariant subspaces of nilpotent linear operators;
- Kosakowska and Schmidmeier, The boundary of the irreducible components for invariant subspace varieties.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

  DOI



There is also relevant work on Springer fibres via quiver varieties.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车+1



These references do not prove that your particular \\(c=3\\) strata are reducible. They establish why irreducibility cannot be inferred merely from a Jordan-type classification.

My recommendation is to complete the \\(c=2\\) theorem first, then audit the eleven \\(c=3\\) strata individually.

Do not try to prove the \\(c=3\\) bound by analogy with \\(c=2\\).

## 12. General \\(c\\): what can honestly be claimed?

The general incidence theorem is a useful result.

For fixed

\\[ (t,u),\qquad t\le u\le2t, \\]

the locus

\\[ S\_{t,u} = \left\\{ W\in\operatorname{Gr}(t,D): \dim(W+A_0(W))=u \right\\} \\]

is locally closed and determinantal.

Over this base, the \\(V\\)'s form an open subset of a relative Grassmannian.

This is a genuine finite stratification.

It is not a general component bound.

### 12.1 Why the partition count is insufficient

The number

\\[ p(c)n^c \\]

counts possible combinatorial labels associated with partitions and eigenvalue assignments.

It does not count irreducible components.

One Jordan type can produce several geometrically distinct families.

Conversely, different parameter descriptions can map into the same component.

Thus the statement

\\[ N\_{\mathrm{components}}\le p(c)n^c \\]

is not established by the current argument.

I recommend removing this as a claimed bound and retaining it only as a count of possible invariant-type labels.

### 12.2 Is quiver-Grassmannian language useful?

Yes, but with an important qualification.

For invariant subspaces, the equation

\\[ A(W)\subseteq W \\]

is naturally a representation-theoretic condition.

One can view \\(A\\) as a representation of the one-loop quiver and invariant subspaces as subrepresentations.

The more general condition

\\[ \dim(W+A(W))=u \\]

can be expressed through an incidence construction involving the image of \\(W\\) under \\(A\\).

This suggests a quiver-Grassmannian or representation-variety formulation.

The benefit would be access to:

- decomposition by representation type;
- degeneration orders;
- orbit closures;
- tangent-space calculations;
- component descriptions through extension data.

However, the general exact-rank incidence strata are not automatically quiver Grassmannians of a single fixed representation.

I would therefore use quiver language as an auxiliary structural tool, not as the primary theorem.

# Part IV. The polynomial certificate and computational complexity

## 13. Audit of the polynomial generalized-inverse certificate

This is another particularly strong part of the project.

Suppose

\\[ P(\lambda)\in\mathbb C[\lambda]^{q\times k} \\]

has normal rank \\(\omega\\), and

\\[ \operatorname{rank}P(\lambda)=\omega \qquad\forall\lambda\in\mathbb C. \\]

The proposed conclusion is that there exists a polynomial matrix

\\[ Y(\lambda)\in\mathbb C[\lambda]^{k\times q} \\]

such that

\\[ PYP=P \\]

and

\\[ \boxed{\deg Y\le2\omega-2.} \\]

I believe the argument is correct, subject to the precise indexing of the maximal minors and embedded adjugates.

### 13.1 The Bézout step

Let \\(p_I(\lambda)\\) denote the nonzero \\(\omega\times\omega\\) minors of \\(P\\).

Constant rank at every finite complex point gives

\\[ \gcd_I p_I=1. \\]

Choose one nonzero minor \\(p_1\\), of degree \\(d\\).

Because the gcd of all the minors is one, their residue classes generate the unit ideal in

\\[ \mathbb C[\lambda]/(p_1). \\]

Thus there exist polynomials \\(b_I\\) such that

\\[ \sum\_{I\ne1}b_Ip_I\equiv1\pmod{p_1}. \\]

The representatives can be chosen with

\\[ \deg b_I\<d. \\]

After incorporating the multiple of \\(p_1\\), we obtain

\\[ 1=\sum_I b_Ip_I \\]

with

\\[ \deg b_I\le\omega-1. \\]

The degree estimate for the coefficient of \\(p_1\\) also needs to be included, but it follows from the degree bound on the other terms.

### 13.2 The adjugate identity

For each selected invertible minor \\(P\_{I,J}\\), embed

\\[ \operatorname{adj}(P\_{I,J}) \\]

into a \\(k\times q\\) matrix \\(E\_{I,J}\\), using the corresponding column and row index sets.

Then, over the rational-function field,

\\[ P E\_{I,J}P = \det(P\_{I,J})P. \\]

Since this is a polynomial identity, it holds in the polynomial ring.

Define

\\[ Y=\sum\_{I,J}b\_{I,J}E\_{I,J}. \\]

Then

\\[ PYP = \left(\sum\_{I,J}b\_{I,J}p\_{I,J}\right)P =P. \\]

Each embedded adjugate has degree at most \\(\omega-1\\), and the Bézout coefficients have degree at most \\(\omega-1\\).

Therefore

\\[ \deg Y\le2\omega-2. \\]

This establishes the claimed degree bound.

### 13.3 An important convention for \\(\omega=0\\)

The formula

\\[ 2\omega-2 \\]

is meaningful only for \\(\omega\ge1\\).

For \\(\omega=0\\), the pencil is identically zero, and the certificate is simply \\(Y=0\\).

The paper should treat this case separately.

### 13.4 A useful independent proof through Smith normal form

There is a second way to understand the result.

Over the PID \\(\mathbb C[\lambda]\\), a polynomial matrix admits a Smith form:

\\[ UPV= \begin{bmatrix} d_1&&&0\\\ &d_2&&0\\\ &&\ddots&0\\\ &&&d\_\omega\\\ 0&\cdots&0&0 \end{bmatrix}, \\]

where \\(U,V\\) are unimodular.

The pointwise constant-rank condition is equivalent to all invariant factors being units:

\\[ d_1=\cdots=d\_\omega=1 \\]

up to nonzero constants.

Consequently, the matrix is polynomially equivalent to a constant rank-\\(\omega\\) matrix.

This gives another proof of the existence of a polynomial generalized inverse.

The adjugate/Bézout proof is better for the complexity question because it gives an explicit degree bound.

The Smith-form proof is better for conceptual understanding.

Relevant background on Smith forms and polynomial matrices can be found in the standard linear-systems literature; see, for example, Kailath's Linear Systems and the polynomial-matrix treatment in the literature on linear systems theory.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.mathematik.uni-kassel.de\&sz=32)

mathematik.uni-kassel.de+1



## 14. Does the certificate establish membership in \\(\exists\mathbb R\\)?

My answer is yes, with a precise rational-input formulation and a few additional details in the proof.

Consider the decision problem:

\\[ \mathrm{DEC}(q): \quad \exists R\text{ such that }L=[L_0;R] \text{ satisfies (5a), (5b), and the required rank conditions}. \\]

For rational input matrices, we can encode this as an existential formula over the reals.

### 14.1 Encoding the unknown matrices

Write each complex unknown as

\\[ z=x+iy, \qquad x,y\in\mathbb R. \\]

All matrix equalities become polynomial equalities in real variables.

Rank constraints can be encoded through minors.

For example,

\\[ \operatorname{rank}M\le r \\]

is equivalent to the vanishing of all \\((r+1)\times(r+1)\\) minors.

The condition

\\[ \operatorname{rank}M=r \\]

additionally requires at least one \\(r\times r\\) minor to be nonzero.

This is existentially expressible using a finite disjunction.

### 14.2 Encoding the spectral condition

Introduce a polynomial matrix

\\[ Y(\lambda)=Y_0+Y_1\lambda+\cdots+Y_D\lambda^D, \\]

where

\\[ D=2\omega-2. \\]

Impose the polynomial identity

\\[ P(\lambda)Y(\lambda)P(\lambda)=P(\lambda). \\]

Equating coefficients of powers of \\(\lambda\\) produces finitely many polynomial equations.

Since the entries of \\(P\\) have degree at most one, the identity has degree at most

\\[ 2D+2=4\omega-2. \\]

The number of coefficient equations is therefore polynomial in the input dimensions.

### 14.3 Why this is equivalent to the original spectral condition

One direction is immediate:

If \\(P(\lambda)\\) has constant rank \\(\omega\\), the certificate theorem supplies \\(Y\\).

For the converse, suppose

\\[ PYP=P. \\]

Over the local ring at a point \\(\lambda_0\\), the Smith form of \\(P\\) has invariant factors \\(d_i\\).

The identity forces each nonzero invariant factor to divide a unit in the local ring.

Hence no invariant factor can vanish at \\(\lambda_0\\).

Thus the rank cannot drop at any finite point.

This proves the equivalence.

It is worth including this converse explicitly. Without it, the existential certificate would only establish sufficiency.

### 14.4 The complexity conclusion

Consequently,

\\[ \boxed{\mathrm{DEC}(q)\in\exists\mathbb R.} \\]

For a bound \\(k\\), define

\\[ \mathrm{MIN}(k) = \bigvee\_{q=r}^{k}\mathrm{DEC}(q). \\]

Then

\\[ \boxed{\mathrm{MIN}(k)\in\exists\mathbb R.} \\]

This remains valid even though feasibility need not be monotone in \\(q\\).

One must not assume that feasibility at \\(q\\) implies feasibility at \\(q+1\\).

That is an important point for the formal complexity statement.

### 14.5 What remains to be checked in the complexity proof?

I would require the following before publishing the \\(\exists\mathbb R\\) result:

1. An explicit rational encoding of all input data.
2. A proof that the number of unknown polynomial coefficients is polynomial in the input size.
3. A proof that all coefficient equations have polynomial bit complexity.
4. An explicit treatment of the different possible values of \\(\omega\\).
5. A separate treatment of \\(\omega=0\\).
6. A proof that the rank-equality disjunctions have polynomial total size.
7. A proof that the fixed rows \\(L_0\\) are correctly incorporated.
8. A proof that the full-row-rank requirements are exactly those of the original problem.

The degree bound is the central mathematical ingredient, but these encoding details are what turn it into a complete complexity theorem.

Strong potential theorem

I would prioritise publishing the \\(\exists\mathbb R\\)-membership result independently of the eventual hardness classification.

## 15. Is the fixed-\\(c=2\\) problem likely to be hard?

There is currently insufficient evidence to claim either hardness or polynomial-time solvability.

I would not infer hardness from the general complexity of rank-constrained matrix problems.

For example, affine rank minimisation and positive-semidefinite matrix completion have strong hardness results, including fixed-rank hardness in certain formulations.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv-troller.com\&sz=32)

arXiv+1



But these results do not automatically transfer to MIN-ROWS.

The reason is that your problem has substantial additional structure:

- the unknown rows enter through a particular linear map;
- the pencil is generated by the same matrix \\(A\\);
- the compatibility condition is a structured kernel inclusion;
- the spectral condition is a constant-rank condition on an affine pencil;
- the candidate subspaces are constrained by the dynamics of \\(A\\).

A reduction must preserve all of these restrictions.

### 15.1 Why \\(c=2\\) is especially interesting

For \\(c=2\\), the Grassmannian geometry is relatively simple.

The admissible \\(V\\)'s are controlled by a finite classification of:

- pairs of eigenlines;
- scalar eigenspaces;
- Jordan-chain configurations;
- one-dimensional intersections;
- generic transverse configurations.

This may make the problem polynomial-time solvable for fixed \\(c=2\\), provided the lift and spectral tests can be performed without an exponential search over the parameter spaces.

The key issue is not the number of components alone.

It is the complexity of deciding whether the spectral-good open subset of each component is nonempty after imposing the affine lift constraints.

That is the real algorithmic problem.

### 15.2 A possible algorithmic direction

On each irreducible stratum:

1. Parameterise the compressed subspace \\(V\\).
2. Express the affine lift constraints linearly.
3. Eliminate the lift variables where possible.
4. Construct the resulting pencil over the function field of the stratum.
5. Compute the gcd of its maximal minors.
6. Determine whether the resulting good locus is nonempty.

If the bad locus is not the entire irreducible component, the good locus is dense.

Thus one generic point is sufficient to establish existence over an algebraically closed field.

However, this argument only works if the actual lifted family is irreducible and the projection to the base is properly understood.

A generic point of the compressed base need not admit a compatible lift.

This is another reason to make the affine lift-feasibility theorem the immediate priority.

# Part V. Additional structural results worth incorporating

## 16. Do not overlook the polynomial-matrix minimal-index approach

There is a second structural route in the broader project that deserves to be integrated into the current report.

It uses the Kronecker structure of the polynomial pencil rather than Grassmannian strata.

Under (5a), the polynomial matrix can be factored in the form

\\[ Q\_{\mathcal L}(\lambda)=D(\lambda)H, \\]

with the relevant right minimal indices equal to zero.

The resulting relations connect:

- the rank of the constant coefficient matrix;
- the degree of the pencil at infinity;
- the finite elementary divisors;
- the left minimal indices.

In particular, the corrected identity is

\\[ \sum_j\varepsilon_j = \operatorname{rank}\mathcal L-d\_{\mathrm{fin}}, \\]

where \\(d\_{\mathrm{fin}}\\) denotes the total contribution of the finite elementary divisors in the relevant normal-rank setting.

Thus the spectral condition can also be expressed as the vanishing of the finite elementary-divisor contribution:

\\[ \boxed{ (5b) \iff d\_{\mathrm{fin}}=0 \iff \sum_j\varepsilon_j=\operatorname{rank}\mathcal L. } \\]

This is potentially useful because it gives an independent way to test a fixed candidate.

There is also a Toeplitz nullity characterization that can recover the minimal-index multiplicities.

I would incorporate this into the project as a parallel computational route, rather than treating the gcd certificate as the only way to test (5b).

The two approaches have different advantages:

| Method                                     | Main advantage                               |
| ------------------------------------------ | -------------------------------------------- |
| Gcd of maximal minors                      | Direct algebraic-geometric formulation       |
| Polynomial generalized-inverse certificate | Explicit bounded-degree existential encoding |
| Kronecker/minimal-index analysis           | Structural interpretation of the pencil      |
| Toeplitz nullity test                      | Finite exact test for a fixed candidate      |

The fixed-candidate spectral problem is therefore considerably more developed than the general feasibility problem.

This is important for the paper's presentation: the difficult problem is not how to test a given \\(L\\), but how to decide whether a suitable \\(L\\) exists.

# Part VI. Answers to the nine questions

## 17. Question 1: Is the three-compression framework sound?

Answer: Yes, with an important refinement concerning lifting.

The chain

\\[ R\longrightarrow(H,H_A)\longrightarrow Z \longrightarrow\text{incidence space} \\]

is mathematically sound as an organising framework.

Each compression removes a different kind of redundancy:

- \\(R\mapsto(H,H_A)\\) removes information invisible on \\(K_0\\).
- \\((H,H_A)\mapsto Z\\) converts the pencil into a structured operator problem.
- \\(Z\mapsto\\) incidence geometry identifies the possible kernels and compatible subspaces.

However, the first compression is not an equivalence of feasibility problems unless the lift is retained as part of the data.

I recommend replacing the schematic chain with

\\[ \boxed{ \begin{aligned} &\text{Original row variables}\\\ &\quad\downarrow\\\ &\text{Compressed pair and affine lift fibre}\\\ &\quad\downarrow\\\ &\text{Compatible operator }Z\\\ &\quad\downarrow\\\ &\text{Lifted incidence variety with spectral condition}. \end{aligned} } \\]

This makes the missing lift information explicit.

The assumptions that should be stated are:

1. Whether \\(C\\) has full row rank.
2. Whether \\(L_0\\) has full row rank.
3. Whether \\([C;L_0]\\) has full row rank.
4. Whether the final requirement is \\(\operatorname{rank}L=q\\) or \\(\operatorname{rank}[C;L]=p+q\\).
5. Whether \\(L_0\\) is fixed exactly.
6. Whether the coefficient field is \\(\mathbb C\\) or a rational subfield for complexity purposes.
7. Whether \\(q\\) is restricted to \\(r\le q\le n\\), or to \\(r\le q\le n-p\\) under the stronger independence condition.

The first five affect the mathematical equivalence. The sixth and seventh affect the complexity statement.

## 18. Question 2: Is the exact-sequence completion criterion correct?

Answer: Yes, after replacing \\(E_C\\) by \\(E'\_C\\) for pair-preserving completion.

The exact sequence is correct.

The calculation

\\[ gAN=bCA^2N \\]

is correct.

The dimension

\\[ d'\_C=d_C-\operatorname{rank}\Gamma \\]

is correct.

The criterion

\\[ q-\omega\le d'\_C \\]

is the appropriate dimension condition for extending a compatible compressed pair while preserving both \\(H\\) and \\(H_A\\).

However, the theorem should be formulated with the fixed rows \\(L_0\\) explicitly included.

Furthermore, for general compatibility rather than full-pair preservation, the more precise quantity is

\\[ d'\_C(V)=\dim\ker\mathcal T_V. \\]

I recommend developing both versions:

- a global pair-preserving completion theorem using \\(E'\_C\\);
- a restricted compatibility-completion theorem using \\(\mathcal T_V\\).

The latter is more general and may be algorithmically superior.

As for references, the natural literature is on:

- exact sequences of finite-dimensional vector spaces;
- linear matrix completion;
- affine determinantal varieties;
- polynomial-matrix completion and generalized inverses.

The exact-sequence argument itself is elementary finite-dimensional linear algebra. It does not require a specialised theorem.

The more relevant literature for the pencil side is the theory of polynomial matrices and Kronecker canonical forms.

## 19. Question 3: Is the \\(c=2\\) algorithm correct?

Answer: The proposed pipeline is structurally correct, but its completeness has not yet been established.

The six-layer classification is the right starting point.

The completion criterion is necessary for pair-preserving lifts.

The gcd test is an exact spectral test.

But the pipeline

\\[ \text{enumerate six layers} \longrightarrow \text{complete the lift} \longrightarrow \text{test gcd} \\]

needs one additional step:

\\[ \boxed{ \text{Solve the affine compatibility problem on each layer.} } \\]

The correct sequence should be

\\[ \begin{aligned} &\text{Enumerate admissible }V\text{-strata};\\\ &\text{construct the affine space of lifts};\\\ &\text{impose }\ker H\subseteq\ker H_A;\\\ &\text{impose row independence};\\\ &\text{construct the resulting pencil};\\\ &\text{test the constant-rank condition}. \end{aligned} \\]

The condition \\(d'\_C\ge1\\) is sufficient for one additional pair-preserving invisible direction, but it does not guarantee that the spectral-good locus is nonempty.

That is a separate question.

### Could one avoid enumerating \\(V\\)?

Possibly.

I would investigate an elimination-based formulation in which \\(V\\) is represented by a full-column-rank matrix \\(X\\), and the compatibility condition is written directly as

\\[ HX=0,\qquad H_AX=0. \\]

The Grassmannian is then handled through a rank constraint and a change-of-basis invariance.

This may lead to a smaller algebraic system than explicitly classifying the six geometric strata.

However, it will not automatically improve complexity: eliminating \\(X\\) may produce high-degree polynomial equations.

My recommendation is to implement both approaches on small instances and compare:

- number of variables;
- polynomial degree;
- number of components;
- Gröbner-basis or quantifier-elimination performance;
- numerical conditioning.

The geometric approach should be used for structural understanding; the direct algebraic approach should be used as a computational baseline.

## 20. Question 4: Are all eleven \\(c=3\\) strata irreducible?

Answer: Not established, and there is no reason to assume so.

The six invariant types need separate irreducibility proofs.

The two \\(t=2\\) strata require separate analysis of their bases.

The two \\(t=1\\) strata need independent proofs for their respective invariant and non-invariant cases.

The \\(t=0\\) stratum is an open Grassmannian subset and is irreducible if nonempty.

The highest-priority case is

\\[ S\_{2,3}. \\]

I would not publish the \\(c=3\\) component bound until this and the remaining ten cases have been audited.

A useful strategy is to construct explicit low-dimensional examples and calculate the irreducible decomposition of the relevant determinantal ideals.

For instance, test:

\\[ \dim K_0=4,5,6, \\]

with several Jordan types for \\(A_0\\).

If a reducible example appears, it immediately disproves the proposed component argument and identifies the geometric source of the failure.

If no reducible example appears, that is useful evidence but not a proof.

## 21. Question 5: Is there a general component bound?

Answer: Not from the current results.

The honest general theorem is:

- a finite locally closed stratification by \\((t,u)\\);
- a relative Grassmannian description of the fibres;
- irreducibility of the total space whenever the corresponding base and fibre hypotheses hold.

The label count

\\[ p(c)n^c \\]

should not be advertised as a component bound.

I would investigate quiver-Grassmannian techniques, particularly degenerations of invariant subspaces and orbit closures.

But I would not make a general component-bound theorem the immediate objective.

The likely difficulty grows rapidly with \\(c\\), and the invariant-subspace geometry can become quite complicated.

A better goal is a conditional theorem:

> If every relevant base stratum \\(S\_{t,u}\\) has at most \\(B\_{t,u}\\) irreducible components and the associated open Grassmannian fibres are nonempty, then the lifted incidence space has at most the sum of these component bounds.

This is mathematically precise and leaves the difficult representation-theoretic question clearly identified.

## 22. Question 6: Does the certificate give \\(\exists\mathbb R\\) membership?

Answer: Yes, subject to the encoding details in Section 14.

I would treat this as a positive result.

The degree bound

\\[ \deg Y\le2\omega-2 \\]

is exactly the type of uniform certificate needed.

It is not necessary to express the original universal quantifier over \\(\lambda\\) directly.

The polynomial identity

\\[ PYP=P \\]

replaces it with finitely many coefficient equations.

This establishes a strong upper bound.

There is currently no basis for claiming \\(\exists\mathbb R\\)-hardness or NP-hardness from this argument.

For \\(c=2\\), I would first investigate a polynomial-time exact algorithm.

For general \\(c\\), the complexity may be substantially harder.

## 23. Question 7: What references should be consulted?

Here is the literature I would prioritise.

### A. Polynomial matrices and generalized inverses

1\. Thomas Kailath, Linear Systems.

Useful for polynomial matrices, Smith forms, matrix pencils, and system-theoretic rank structure.

2\. Gohberg, Lancaster and Rodman, Matrix Polynomials.

Particularly relevant to matrix polynomials, elementary divisors, canonical forms, and polynomial matrix identities.

3\. The Smith-form literature for polynomial matrices, including the treatment of invariant factors and determinantal divisors.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.mathematik.uni-kassel.de\&sz=32)

mathematik.uni-kassel.de+2



### B. Invariant-subspace varieties and incidence geometry

1. Gerstenhaber (1961), On Dominance and Varieties of Commuting Matrices.
2. Ringel and Schmidmeier (2008), Invariant Subspaces of Nilpotent Linear Operators.
3. Kosakowska and Schmidmeier (2018), The Boundary of the Irreducible Components for Invariant Subspace Varieties.
4. Im, Lai and Wilbert (2022), A Study of Irreducible Components of Springer Fibers Using Quiver Varieties.&#x20;

   [image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

   DOI+1



These are particularly useful for understanding why invariant-subspace varieties can have multiple components.

### C. Functional observers

The two recent preprints by Tyrone Fernando are important to the problem's current formulation:

- [A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions (arXiv:2609.33615)](https://papers.cool/arxiv/2609.33615?utm_source=chatgpt.com).
- [Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger (arXiv:2609.37992)](https://papers.cool/arxiv/2609.37992?utm_source=chatgpt.com).

The first develops the minimum-order framework and functional observability indices; the second gives an order-by-order characterization and spectral feasibility conditions.

The project should cite these as recent preprints, not as established peer-reviewed results unless their publication status is independently confirmed.

### D. Existential-real complexity

For the complexity part, I recommend studying:

- the standard existential theory of the reals and its reductions;
- affine rank minimisation;
- rank-constrained matrix completion;
- polynomial feasibility over real closed fields.

A recent example is Affine Rank Minimization is ER Complete (2026), which illustrates how powerful rank constraints can be when combined with affine equations.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv-troller.com\&sz=32)

arXiv



But remember that this is a source of reduction techniques, not a direct hardness result for MIN-ROWS.

## 24. Question 8: What should be the next step?

My recommendation is a carefully ordered combination of options (i), (ii), and (iv), with the complexity result developed in parallel.

Here is the priority ranking.

Priority 1 — Complete the lift theorem

Essential

Establish the exact affine compatibility and row-completion criterion, with \\(L_0\\) fixed. This is the prerequisite for every algorithm based on compressed geometry.

Priority 2 — Finish the \\(c=2\\) theorem

High value

Prove the six-layer classification, establish irreducibility, incorporate the lift, and derive an exact feasibility procedure.

Priority 3 — Consolidate \\(c=1\\) and \\(c=2\\)

Publication-ready direction

Present the two cases as a unified theorem about low-codimension kernels, with precise component bounds and spectral criteria.

Priority 4 — Complete the \\(\exists\mathbb R\\) proof

Independent result

Formalise the bounded-degree certificate and provide the rational-input encoding.

Priority 5 — Audit \\(c=3\\)

Exploratory

Test and prove irreducibility of the eleven strata separately.

Priority 6 — General hardness

Long-term

Search for a structured reduction, but do not let the absence of one delay the established results.

### Why this order?

The lift theorem is the logical bottleneck.

Without it, the geometric classification may describe compressed objects that do not correspond to actual feasible matrices \\(L\\).

Once the lift is settled, the \\(c=2\\) case becomes a well-defined finite geometric decision problem.

The complexity certificate can then be presented independently, because it does not require the component classification.

The \\(c=3\\) and general-\\(c\\) questions can be treated as extensions rather than prerequisites.

## 25. Question 9: Which statements need independent verification?

I would divide the statements into three groups.

### 25.1 Statements that are relatively secure

These have direct linear-algebraic proofs and are appropriate for formalisation.

| Statement                                | Assessment                                                          |
| ---------------------------------------- | ------------------------------------------------------------------- |
| Equivalence of (5a) and kernel inclusion | Sound                                                               |
| Factorisation \\(H_A=ZH\\)               | Sound                                                               |
| Universal block criterion                | Sound                                                               |
| Pencil rank and kernel identities        | Sound                                                               |
| Exact-sequence description of \\(E_C\\)  | Sound                                                               |
| Formula for \\(d'\_C\\)                  | Sound                                                               |
| Exact fibre theorem                      | Sound, with the ambient quotient distinction                        |
| Bézout/adjugate certificate              | Sound, subject to the stated indexing and \\(\omega=0\\) convention |

I would retain these as the algebraic foundation.

### 25.2 Statements requiring additional mathematical proofs

These should not yet be treated as established general theorems.

1. The complete equivalence between the compressed feasibility problem and the original problem, with fixed \\(L_0\\).
2. The pair-preserving lift-completion theorem with all hypotheses explicit.
3. The six \\(c=2\\) strata as a complete and mutually exclusive classification.
4. Irreducibility of every \\(c=2\\) parameter space.
5. The \\(c=2\\) component bound for the actual lifted incidence space.
6. The affine compatibility and spectral-good-locus nonemptiness conditions.
7. Any extension of the component count to \\(c=3\\).

### 25.3 Statements I would not formalise yet

I would postpone:

- the general \\(p(c)n^c\\) component-bound conjecture;
- the irreducibility of all eleven \\(c=3\\) strata;
- a general polynomial-time algorithm;
- any NP-hardness reduction;
- the assertion that \\(d'\_C\ge1\\) guarantees spectral feasibility;
- any argument that a generic compressed point necessarily has a compatible lift.

These are research conjectures or incomplete constructions, not yet suitable formal targets.

# Part VII. Formal verification and computational experiments

## 26. How I assess the Lean development

The Lean results are valuable, but their significance should be stated precisely.

A proof kernel compiled without `sorry` and with axioms restricted to

\\[ [\text{propext},\text{Classical.choice},\text{Quot.sound}] \\]

provides strong evidence that the formalised propositions follow from the stated definitions.

This is particularly useful for:

- the block criterion;
- the rank formulas;
- the exact kernel identities;
- the lifting identities;
- the polynomial certificate.

Nevertheless, formal verification has two separate levels.

Level 1: Formal correctness.

Does the proof establish the proposition stated in Lean?

Level 2: Mathematical modelling correctness.

Does the proposition stated in Lean faithfully represent the intended mathematical claim?

The second level is especially important for this project.

I recommend that every Lean theorem be accompanied by:

1. A mathematical statement in the paper.
2. A precise translation of every matrix dimension.
3. The hypotheses used.
4. A short explanation of the intended mathematical interpretation.
5. A reference to the corresponding Lean theorem.

The formalisation should not be presented as verification of the whole research argument.

It verifies the encoded algebraic claims, not the irreducibility of geometric strata or the completeness of an algorithm unless those statements themselves have been formalised.

## 27. How to improve the computational experiments

The report refers to numerical tests in which

\\[ d_C=3,\qquad \operatorname{rank}\Gamma=1, \qquad d'\_C=2. \\]

This is useful diagnostic information.

But I recommend upgrading the experiments from random numerical testing to exact symbolic testing.

### 27.1 Use rational matrices

Generate matrices over \\(\mathbb Q\\), not floating-point approximations.

This permits exact calculation of:

- ranks;
- nullspaces;
- intersections;
- Jordan structures;
- polynomial gcds;
- determinantal ideals.

### 27.2 Separate the stages

Every experiment should record:

| Stage                | Test                                                 |
| -------------------- | ---------------------------------------------------- |
| Original input       | Verify dimensions and prescribed rank assumptions    |
| Compression          | Compute \\(K_0,N_K,H,H_A\\)                          |
| Kernel compatibility | Test \\(\ker H\subseteq\ker H_A\\)                   |
| Lift                 | Solve the affine equations for \\(G\\)               |
| Independence         | Test \\(\operatorname{rank}[C;L]=p+q\\), if required |
| Spectrum             | Compute gcd of maximal minors                        |
| Verification         | Substitute the final \\(L\\) into (5a) and (5b)      |

The last step is essential.

A candidate produced by the compressed algorithm should always be checked against the original conditions.

### 27.3 Use adversarial examples

Random matrices are useful for finding generic behaviour, but they are poor at detecting exceptional geometry.

For the next phase, systematically generate:

- diagonal \\(A\\) with repeated eigenvalues;
- Jordan blocks of sizes two and three;
- multiple Jordan blocks with the same eigenvalue;
- matrices preserving \\(K_0\\);
- matrices for which \\(A(K_0)\not\subseteq K_0\\);
- cases with \\(d'\_C=0\\);
- cases with \\(d'\_C>0\\) but an empty compatible lift fibre;
- cases with compatible lifts but no spectral-good point.

These examples directly test the logical distinctions that the project has identified.

### 27.4 Maintain a counterexample registry

Every rejected formula or false conjecture should remain in a permanent test suite.

I would organise the registry into:

- closed-form counterexamples;
- non-monotonicity examples;
- reducible-stratum examples;
- lift-completion failures;
- spectral obstruction examples;
- quotient-space errors.

This is important because the project has already undergone several conceptual corrections.

The registry will prevent a previously refuted argument from being inadvertently reintroduced.

# Part VIII. The strongest possible research contribution

## 28. What would constitute a strong paper?

I see three possible paper directions.

### Paper A: Geometry and low-codimension classification

Possible title:

Low-Codimension Incidence Geometry in Minimal-Order Functional Observer Problems

Main results:

1. The exact compressed-pencil reduction.
2. The universal block criterion.
3. The exact fibre theorem.
4. The hyperplane classification.
5. The complete \\(c=2\\) classification.
6. The \\(c=2\\) component bound.
7. The lift-completion theorem.

This would be the most natural first paper if the \\(c=2\\) results can be completed rigorously.

### Paper B: Algebraic complexity

Possible title:

Polynomial Certificates and Existential-Real Formulations of Minimal-Order Functional Observer Feasibility

Main results:

1. Constant-rank characterization through determinantal divisors.
2. Explicit bounded-degree polynomial generalized inverse.
3. Existential-real encoding.
4. Complexity upper bound.
5. Exact fixed-candidate spectral testing.

This paper has a clear independent mathematical contribution even without hardness.

### Paper C: Representation-theoretic geometry

Possible title:

Invariant-Subspace Incidence Varieties and Component Bounds in Functional Observer Design

Main results:

1. General \\((t,u)\\)-stratification.
2. Quiver representation formulation.
3. Irreducibility and reducibility criteria.
4. Component bounds for selected values of \\(c\\).
5. General degeneration-theoretic results.

This is potentially the most ambitious paper, but it is also the least mature.

### My preference

I would aim first for a combined version of Papers A and B, provided the proofs are sufficiently independent and the paper does not become too long.

The geometry explains the structure of the feasible family.

The polynomial certificate explains its algebraic complexity.

The two contributions complement each other.

# Part IX. Final research recommendations

## 29. The five questions I would investigate immediately

Rather than continuing with nine broad questions simultaneously, I would reduce the next phase to five concrete mathematical problems.

### Problem 1. Exact lift-completion theorem

Given a compressed pair \\((H,H_A)\\), determine necessary and sufficient conditions for the existence of \\(L\\) such that

\\[ LN_K=H,\qquad LAN_K=H_A, \\]

with \\(L_0\\) fixed and the required independence conditions satisfied.

This theorem should explicitly identify:

- the affine space of all lifts;
- the compatibility equations;
- the dimension of the homogeneous solution space;
- the independence condition;
- the exact role of \\(E'\_C\\).

This is the most important unresolved mathematical issue.

### Problem 2. Nonemptiness of the spectral-good locus

On each irreducible lifted component, determine whether the constant-rank pencil condition holds identically or fails identically.

The projective closedness theorem gives a strong starting point.

The remaining issue is to calculate the gcd of maximal minors over the function field of the component.

This may lead to an effective generic-feasibility algorithm.

### Problem 3. A complete \\(c=2\\) feasibility algorithm

Prove that the six strata cover every admissible configuration.

For each stratum, solve the affine lift problem and test the pencil.

Establish both directions:

\\[ \text{algorithm outputs feasible} \Longrightarrow \text{original problem feasible}, \\]

and

\\[ \text{original problem feasible} \Longrightarrow \text{algorithm finds a feasible stratum}. \\]

Without the second implication, the algorithm is only a witness-generation procedure.

### Problem 4. An independent \\(\exists\mathbb R\\) theorem

Complete the rational-input encoding and prove polynomial size.

This should be pursued independently of the \\(c=2\\) algorithm.

### Problem 5. The first reducibility audit for \\(c=3\\)

Focus on

\\[ S\_{2,3}. \\]

Determine whether it is always irreducible under the special linear-operator structure of this problem.

If not, find the smallest counterexample.

This will determine whether the proposed \\(c=3\\) component bound needs to be revised or replaced.

## 30. My final assessment of the nine questions

| Question                        | Conclusion                                                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Q1. Three-compression framework | Yes, sound, but retain the affine lift fibre                                                                    |
| Q2. Lift completion             | Exact sequence correct; \\(E'\_C\\) correct for pair preservation; restricted compatibility map is more general |
| Q3. \\(c=2\\) algorithm         | Correct direction, but not yet a complete algorithm                                                             |
| Q4. \\(c=3\\) irreducibility    | Open; eleven strata need individual verification                                                                |
| Q5. General component bound     | Not established; retain finite stratification and label count only                                              |
| Q6. Complexity                  | \\(\exists\mathbb R\\) membership is available; hardness is open                                                |
| Q7. References                  | Polynomial matrices, invariant-subspace varieties, quiver Grassmannians, and ETR                                |
| Q8. Next step                   | Lift theorem, then \\(c=2\\), with complexity in parallel                                                       |
| Q9. Verification                | Formalise algebraic identities; postpone general irreducibility and hardness claims                             |

## 31. Final verdict

## Research status

Linear-algebraic foundation

Strong

Pencil and spectral theory

Strong

Exact incidence geometry

Substantial

\\(c=2\\) component theorem

Needs final proof

Lift-completion algorithm

Unresolved

\\(c=3\\) component bound

Unproved

General component bound

Open

\\(\exists\mathbb R\\) membership

Mathematically supported

NP-hardness / ETR-hardness

Open

My strongest recommendation is:

Do not make NP-hardness the immediate measure of success for this project.

The project has already produced several results that are mathematically valuable independently of the final complexity classification.

In particular, the combination of:

- the universal block criterion;
- the exact Grassmannian fibre theorem;
- the low-codimension stratification;
- the lift-completion problem;
- the polynomial generalized-inverse certificate;

is a meaningful body of work.

The remaining difficulty is to connect these results into a single correct theorem about the original observer feasibility problem.

I would formulate the central research objective as follows:

> Determine the algebraic and geometric structure of the feasible set of minimal-order functional observers, including its lifted incidence components and the spectral-good locus, and establish the computational complexity of deciding whether that locus is nonempty.

This formulation is stronger and more precise than simply asking whether MIN-ROWS is NP-hard.

It also leaves room for several substantial outcomes:

1. A polynomial-time algorithm for \\(c=2\\).
2. Explicit component bounds for low-codimension cases.
3. An existential-real upper bound for arbitrary input dimensions.
4. A general geometric description through determinantal incidence varieties.
5. Eventually, a hardness result or a structural reason why the problem is easier than general rank-constrained feasibility.

The next decisive milestone should be a rigorous lift-completion theorem followed by a complete \\(c=2\\) feasibility theorem. If those are achieved, the project will have a much stronger foundation for publication and for the subsequent complexity investigation.

I would next concentrate on turning the affine lift-feasibility formulation into a necessary-and-sufficient theorem, including the fixed \\(L_0\\) constraints and a constructive procedure.