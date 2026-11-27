# Structural analysis of the new results and answers to Q1–Q6

The new results reveal an important development: the project now has a much more precise understanding of the difference between the minimum augmentation required by (5a) and the minimum augmentation required by both (5a) and (5b).

In particular, three findings deserve special attention:

1. The minimum augmentation for (5a) is unique at the level of row spaces.
2. The necessary condition\
   \\[\
   h\<q+r_1\
   \\]\
   gives a simple obstruction to satisfying (5b).
3. At larger orders, the existence of a nonzero left minimal index is not enough: its magnitude must also be sufficiently large.

The third point is especially important. It explains why the new obstruction is useful but cannot, by itself, determine the minimum order.

I will address all six questions, distinguish established mathematical conclusions from conjectures, and suggest specific results and experiments that could move the project forward.

02_structural_results_and_questions.md

# 1. First: what the new results establish

Let

\\[ V\_{\min} \\]

be the minimum-dimensional row space containing \\(\operatorname{row}L_0\\) and satisfying

\\[ V\_{\min}A\subseteq V\_{\min}+\operatorname{row}[C;CA]. \\]

Write

\\[ c=\mathrm{cl}(A,C,L_0)=\dim V\_{\min}. \\]

At order \\(q=c\\), the row space of every augmentation satisfying (5a) must equal \\(V\_{\min}\\).

Thus the minimal-order problem has a particularly simple structure:

\\[ \boxed{ q\_{\min}=c \iff \text{the unique minimal (5a)-augmentation satisfies (5b)}. } \\]

If it fails, the minimum order is strictly larger than \\(c\\).

This is a useful separation of the two constraints:

- (5a) determines a unique minimum-dimensional invariant-type row space.
- (5b) tests whether that particular space has the required spectral property.

At higher orders, additional row-space freedom appears, and the problem becomes existential.

## 1.1 The new obstruction in its strongest form

Recall

\\[ m=q+2p-h, \\]

and the number of zero left minimal indices is

\\[ z=2p-r_1. \\]

Hence the number of positive left minimal indices is

\\[ k=m-z=q+r_1-h. \\]

Since all positive indices are integers at least one,

\\[ \sum\_{j=1}^{m}\varepsilon_j \ge q+r_1-h. \\]

But (5b) requires

\\[ \sum_j\varepsilon_j=s. \\]

Therefore, a necessary condition is

\\[ \boxed{ s\ge q+r_1-h. } \tag{9} \\]

This is equivalent to

\\[ h\ge q+r_1-s. \\]

Together with B.9, we obtain two necessary inequalities:

\\[ \boxed{ q+r_1-s\le h\<q+r_1. } \tag{10} \\]

This is stronger than B.9 alone.

The derivation uses only:

- the number of positive left minimal indices;
- their integrality;
- the total-index identity.

It does not require any additional assumptions about the descriptor system.

Important qualification: these inequalities are necessary, not sufficient.

Your minimal counterexample in II.4 illustrates why the first inequality is useful: the number of positive indices can be correct while their sum is too small.

For example,

\\[ \varepsilon=[3],\qquad s=4 \\]

gives one positive index but fails the required equality.

There is also a useful consequence:

\\[ \boxed{ d\_{\mathrm{fin}} \le s-(q+r_1-h). } \tag{11} \\]

Indeed,

\\[ d\_{\mathrm{fin}} =s-\sum_j\varepsilon_j \\]

and the sum is at least the number of positive indices.

This provides an upper bound on the total degree of the finite elementary divisors for every pencil satisfying (5a).

I recommend adding (9)–(11) to the list of established structural obstructions.

# 2. Q1 — Is there a criterion for the minimal augmentation other than Kronecker data?

Yes. There is a particularly useful alternative in the functional-observer literature: a nullspace-based matrix criterion.

This is more than a different computational implementation. It provides a direct description of the geometric obstruction.

## 2.1 The nullspace characterisation

Let

\\[ r_1=\operatorname{rank}\begin{bmatrix}C\\\CA\end{bmatrix}, \\]

and choose a full-column-rank matrix \\(V\\) such that

\\[ \operatorname{im}V = \ker\begin{bmatrix}C\\\CA\end{bmatrix}. \\]

For an admissible augmentation \\(\mathcal L\\), let \\(Z\\) be a basis matrix of

\\[ \ker\begin{bmatrix}C\\\\\mathcal L\end{bmatrix}. \\]

Thus

\\[ CZ=0,\qquad \mathcal LZ=0. \\]

Let \\(R_Z\\) be a basis matrix of

\\[ \ker(CAZ). \\]

Under (5a), the spectral condition can be expressed as

\\[ \boxed{ \operatorname{rank} \begin{bmatrix} (\lambda I-A)V & Z \end{bmatrix} = \operatorname{rank} \begin{bmatrix} V&Z \end{bmatrix} \quad\forall\lambda\in\mathbb C. } \tag{12} \\]

This is the nullspace-pencil characterisation in Fernando's 2026 paper.

The algebraic condition is separately expressed as

\\[ \boxed{ \operatorname{rank} \begin{bmatrix} Z& AZR_Z \end{bmatrix} = \operatorname{rank}Z. } \tag{13} \\]

The two conditions together give an alternative characterisation of the admissible augmentation.

Source: Fernando, Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger, Sections IV–V, Theorems 3–5.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



## 2.2 Interpretation of the spectral obstruction

Define

\\[ \mathcal U=\operatorname{im}V = \ker C\cap\ker CA, \\]

and

\\[ \mathcal Z=\operatorname{im}Z. \\]

The spectral condition becomes

\\[ (\lambda I-A)v\in\mathcal Z \iff v\in\mathcal Z, \qquad v\in\mathcal U. \tag{14} \\]

The meaning is particularly transparent.

A vector in \\(\mathcal U\\) is invisible to the first two observation levels \\(C\\) and \\(CA\\).

The subspace \\(\mathcal Z\\) represents the directions invisible to both \\(C\\) and the augmented functional matrix.

Condition (5b) requires that, on \\(\mathcal U\\), applying \\(\lambda I-A\\) must not create additional invisible directions.

In other words, the augmentation must eliminate all nontrivial finite spectral obstructions in the quotient geometry determined by \\(\mathcal U\\) and \\(\mathcal Z\\).

This interpretation suggests investigating the induced action of \\(A\\) on the relevant quotient spaces rather than only studying the Kronecker form.

## 2.3 What makes the minimal augmentation fail?

I would distinguish three types of failure.

Type I: Zero positive-index count.

If

\\[ h\ge q+r_1, \\]

then there are no positive left minimal indices.

Since \\(s>0\\), (5b) necessarily fails.

This is exactly B.9.

Type II: Insufficient total positive-index degree.

If

\\[ 0\<q+r_1-h\<s, \\]

then there are positive left indices, but even the maximum possible contribution from the count alone does not establish the required sum.

More precisely, (5b) requires their actual sum to be \\(s\\). The number of positive indices is only a lower bound on that sum.

Type III: Geometric spectral degeneracy.

Even when the index-count inequalities are satisfied, the augmentation may still have finite elementary divisors.

The nullspace criterion (12) identifies this as a rank-drop phenomenon.

The distinction between Type II and Type III is important: Type II can be detected by integer invariants, whereas Type III requires more detailed information about the subspaces.

### My recommendation for Q1

For the minimum-order candidate, compute the following quantities:

\\[ \begin{aligned} s&=\operatorname{rank}\mathcal L,\\\ h&=\operatorname{rank}[\mathcal L;CA;C],\\\ k&=q+r_1-h,\\\ d\_{\mathrm{fin}}&=s-\sum_j\varepsilon_j. \end{aligned} \\]

Then classify every failure according to:

- \\(k=0\\);
- \\(0\<k\<s\\);
- \\(k\ge s\\), but \\(d\_{\mathrm{fin}}>0\\).

The third category is the genuinely interesting one because it cannot be eliminated using B.9 and the elementary sum bound.

I would also compare the nullspace-pencil test (12) with the Toeplitz criterion. The former may reveal the geometry of the failure, while the latter provides a compact exact certificate.

# 3. Q2 — Is \\(\mathrm{cl}\\) equal to the sum of functional observability indices?

This question needs a careful distinction between the definition of the augmentation and the definition of observer order in the literature.

My conclusion is:

\\[ \boxed{ \mathrm{cl}(A,C,L_0)=\sum\_{j=1}^{r}\eta_j } \\]

under the standing functional-observability assumptions and the identification of the two algebraic feasibility problems.

In particular, the reported discrepancy between closure dimension \\(4\\) or \\(5\\) and a functional-index sum of \\(3\\) should be investigated as a potential implementation or definition mismatch.

It should not be accepted as evidence that the two mathematical quantities are different.

## 3.1 Why the definitions appear different

Your closure problem is

\\[ \mathrm{cl} = \min\left\\{ \dim V: \operatorname{row}L_0\subseteq V,\quad VA\subseteq V+\operatorname{row}[C;CA] \right\\}. \tag{15} \\]

In Fernando's formulation, the augmented functional matrix \\(\mathcal L\\) is required to satisfy

\\[ \operatorname{row}L_0 \subseteq \operatorname{row}[C;\mathcal L], \\]

and

\\[ \operatorname{rank}[C;\mathcal L]=p+q. \\]

The important difference is that the prescribed functional \\(L_0\\) is required to lie in the combined row space of \\(C\\) and \\(\mathcal L\\), not necessarily in the row space of \\(\mathcal L\\) alone.

At first sight, these appear to define different minimisation problems.

However, the two problems are equivalent at the level of minimum dimension.

## 3.2 Proof of equivalence

Write

\\[ W_C=\operatorname{row}C. \\]

First, suppose \\(V\\) is feasible for (15).

Choose a complement \\(U\\) of \\(W_C\cap V\\) in \\(V\\):

\\[ V=(V\cap W_C)\oplus U. \\]

Then

\\[ \dim U = \dim V-\dim(V\cap W_C) \le\dim V, \\]

and

\\[ V+W_C=U+W_C. \\]

Because

\\[ VA\subseteq V+W_C+\operatorname{row}CA, \\]

we also have

\\[ UA\subseteq U+W_C+\operatorname{row}CA. \\]

Moreover, \\(L_0\subseteq V\\) and

\\[ \operatorname{row}L_0\cap W_C=\\{0\\}, \\]

so

\\[ \operatorname{row}L_0 \subseteq U+W_C. \\]

Thus \\(U\\) defines an algebraically admissible augmented functional matrix of order \\(\dim U\\).

Consequently,

\\[ q_0\le\dim V. \\]

Taking the minimum gives

\\[ q_0\le\mathrm{cl}. \tag{16} \\]

Conversely, suppose an algebraically admissible augmented functional matrix has order \\(q_0\\).

Let

\\[ S=\operatorname{row}[C;\mathcal L]. \\]

Then

\\[ \dim S=p+q_0, \qquad \operatorname{row}L_0\subseteq S. \\]

Since \\(\operatorname{row}L_0\\) is disjoint from \\(W_C\\), we can choose a complement \\(U\\) of \\(W_C\\) in \\(S\\) that contains \\(\operatorname{row}L_0\\).

Thus

\\[ S=U\oplus W_C, \qquad \dim U=q_0. \\]

The algebraic condition gives

\\[ \mathcal L A \subseteq \operatorname{row}\mathcal L+W_C+\operatorname{row}CA. \\]

Since \\(U+W_C=S\\), this implies

\\[ UA\subseteq U+W_C+\operatorname{row}CA. \\]

Therefore \\(U\\) is feasible for (15), and

\\[ \mathrm{cl}\le q_0. \tag{17} \\]

Combining (16) and (17),

\\[ \boxed{\mathrm{cl}=q_0=\sum\_{j=1}^{r}\eta_j.} \tag{18} \\]

This equivalence uses the assumption that the prescribed functional rows are independent modulo the measured-output rows.

It is important that the augmentation is understood as a row-space object: redundant rows must not be counted as additional observer states.

## 3.3 What does this imply for your implementation?

The functional-observability-index algorithm in Fernando's paper processes

\\[ C_1,\ldots,C_p,L\_{0,1},\ldots,L\_{0,r} \\]

and their successive \\(A\\)-iterates, retaining a candidate precisely when it increases the rank.

The functional observability indices are obtained from the last retained powers associated with the prescribed functional rows:

\\[ \eta_j=1+k\_{p+j}. \\]

Then

\\[ q_0=\sum_j\eta_j. \\]

This construction is given explicitly in the 2026 paper, Section III.A.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



If the index calculation returns \\(3\\), but your closure calculation returns \\(4\\) or \\(5\\), I would investigate the closure implementation first.

There are several possible sources of disagreement:

1. The closure routine may be adding too many rows because it uses a particular basis-dependent selection rather than a rank-minimal selection.
2. The functional-index implementation may be processing the generators in a different order from the prescribed convention.
3. The closure calculation may be using \\(CA\\) incorrectly or omitting the \\(C\\) component of the allowed correction space.
4. The implementation may be comparing row counts with ranks after adjoining \\(C\\), rather than comparing the same quotient dimensions.

In particular, verify that the closure condition is exactly

\\[ VA\subseteq V+\operatorname{row}C+\operatorname{row}CA. \\]

A test using only \\(V+\operatorname{row}CA\\) is not equivalent.

Recommended action: take one of the discrepant examples and compute the two quantities independently using exact rational arithmetic. The proof above predicts that they must agree.

If they do not, the discrepancy is evidence of a computational or modelling inconsistency that should be resolved before proceeding.

# 4. Q3 — Can the gap \\(q\_{\min}-\mathrm{cl}\\) exceed one?

Yes — an explicit published counterexample exists

This question has a decisive answer.

The 2026 paper by Fernando contains an example in which

\\[ q_0=3, \\]

the spectral condition fails at both

\\[ q=3 \quad\text{and}\quad q=4, \\]

but holds at

\\[ q=5. \\]

The actual minimum observer order is therefore

\\[ \boxed{q\_{\min}=q_0+2.} \\]

Since \\(q_0=\mathrm{cl}\\) under the equivalence above, this is precisely a counterexample to

\\[ q\_{\min}\in\\{\mathrm{cl},\mathrm{cl}+1\\}. \\]

## 4.1 Details of the published example

The example has

\\[ n=8,\qquad p=2,\qquad r=2. \\]

Its functional observability indices are

\\[ \eta_1=2,\qquad \eta_2=1. \\]

Therefore,

\\[ q_0=2+1=3. \\]

The system is completely observable, so

\\[ n_0-p=8-2=6. \\]

The algebraically admissible orders are

\\[ \\{3,4,5,6\\}. \\]

The paper proves:

| Order | Algebraic condition | Spectral condition |
| ----- | ------------------- | ------------------ |
| 3     | Feasible            | Infeasible         |
| 4     | Feasible            | Infeasible         |
| 5     | Feasible            | Feasible           |
| 6     | Feasible            | Feasible           |

Thus

\\[ \Sigma\_{\mathrm{FO}}=\\{5,6\\}, \\]

and

\\[ \boxed{\nu\_{\min}=5=q_0+2.} \\]

The failure at orders 3 and 4 is established by examining all relevant Grassmann charts, not merely by testing selected augmentations.

The feasible order-5 candidate is also given explicitly in the paper.

Source: Fernando, 2026, Section VII, especially the discussion of the order-3, order-4 and order-5 cases.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



## 4.2 Why this example is particularly important

It does more than disprove a conjecture.

It establishes that the spectral obstruction can persist after one additional algebraic degree of freedom has been introduced.

Therefore, no general argument of the form

\\[ \text{failure at }q_0 \Longrightarrow \text{success at }q_0+1 \\]

can be correct.

The published example also demonstrates that the minimum order can be strictly inside the algebraically admissible interval:

\\[ q_0\<q\_{\min}\<n_0-p. \\]

This is an important phenomenon in functional-observer theory.

### Consequence for your project

I recommend replacing the empirical conjecture in II.5 with the following statement:

\\[ \boxed{ q\_{\min}\ge\mathrm{cl}, \qquad q\_{\min}\le n_0-p } \\]

under functional observability, with equality at the upper endpoint guaranteed to be feasible.

There is no general upper bound of \\(\mathrm{cl}+1\\).

Your 56-instance experiment remains valuable, but it describes the distribution of gaps in your chosen random instance family, not a universal theorem.

# 5. Q4 — What structural mechanism can force \\(q\_{\min}\ge\mathrm{cl}+2\\)?

The published example gives a concrete answer, and I think it suggests a useful mechanism for your own investigation.

The key is that adding one row can enlarge the algebraically admissible family without removing the spectral obstruction.

The obstruction is not necessarily caused by insufficient dimension. It can be caused by the fact that every admissible subspace at a particular order has an undesirable intersection with the spectral directions of \\(A\\).

## 5.1 A geometric mechanism

Use the nullspace representation

\\[ \mathcal Z=\ker\begin{bmatrix}C\\\\\mathcal L\end{bmatrix}, \qquad \mathcal U=\ker\begin{bmatrix}C\\\CA\end{bmatrix}. \\]

At order \\(q\\), the dimension of \\(\mathcal Z\\) is

\\[ \dim\mathcal Z=n-p-q \\]

when the augmentation is reduced.

The algebraic condition restricts which subspaces \\(\mathcal Z\\) can occur.

The spectral condition then requires

\\[ \operatorname{rank} \begin{bmatrix} (\lambda I-A)V&Z \end{bmatrix} = \operatorname{rank} \begin{bmatrix} V&Z \end{bmatrix} \quad\forall\lambda. \\]

Suppose that, for every algebraically admissible \\(\mathcal Z\\), there is an eigenvalue \\(\lambda\\) and a vector \\(v\in\mathcal U\\) such that

\\[ v\notin\mathcal Z, \qquad (\lambda I-A)v\in\mathcal Z. \\]

Then the spectral condition necessarily fails.

Thus a possible mechanism for a two-order gap is:

- At \\(q=c\\), every algebraically admissible subspace has the same unavoidable spectral degeneracy.
- At \\(q=c+1\\), the extra degree of freedom is still insufficient to avoid that degeneracy.
- At \\(q=c+2\\), a new admissible subspace becomes available that avoids it.

This is a precise geometric formulation of the obstruction.

## 5.2 The published example provides an even more specific mechanism

In Fernando's example:

\\[ q_0=3,\qquad n=8,\qquad p=2. \\]

At \\(q=3\\), the candidate nullspaces are three-dimensional subspaces of a fixed four-dimensional space.

The complete family is covered by

\\[ \operatorname{Gr}(3,4), \\]

which has four standard Grassmann charts.

On every chart, the algebraic condition reduces the candidate family, but the spectral condition fails on every resulting branch.

At \\(q=4\\), the candidate nullspaces are two-dimensional subspaces of the same four-dimensional space:

\\[ \operatorname{Gr}(2,4). \\]

There are six standard charts. Again, the complete algebraically admissible family fails the spectral condition.

At \\(q=5\\), the candidate nullspace is one-dimensional, and a feasible vector is explicitly constructed.

The paper attributes the simultaneous failures at orders 3 and 4 to the same underlying rank mechanism: the algebraic family is confined to a locus on which the relevant spectral pencil matrix has the obstructing full-rank structure.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



This is exactly the sort of phenomenon you should try to identify in your own examples.

## 5.3 A practical way to search for a second extra row

I suggest introducing the following quantities for each admissible augmentation:

\\[ k_q=q+r_1-h_q, \\]

and

\\[ s_q=\operatorname{rank}\mathcal L_q. \\]

Then calculate

\\[ \delta_q = s_q-k_q. \\]

The necessary condition derived earlier gives

\\[ \delta_q\le0. \\]

There are three cases:

| Situation         | Interpretation                                                       |
| ----------------- | -------------------------------------------------------------------- |
| \\(k_q=0\\)       | Automatic spectral failure if \\(s_q>0\\)                            |
| \\(0\<k_q\<s_q\\) | Insufficient positive-index count; failure                           |
| \\(k_q\ge s_q\\)  | The counting obstruction disappears, but spectral failure may remain |

The third case is where you should concentrate your search.

For a candidate instance, examine every admissible augmentation at \\(c\\) and \\(c+1\\), and determine whether:

\\[ k_q\ge s_q \\]

but

\\[ \sum_j\varepsilon_j\<s_q. \\]

If this happens uniformly across the complete family at both orders, you have found a genuine higher-order spectral obstruction rather than merely an elementary counting obstruction.

### Suggested experimental search

I would modify the random-instance generator to deliberately favour the following properties:

1. Small functional-observability lower bound \\(c\\).
2. A relatively large unobservable or weakly observable subspace.
3. Repeated or highly structured eigenvalues of \\(A\\).
4. Small values of \\(r_1=\operatorname{rank}[C;CA]\\).
5. Algebraic augmentation families with low-dimensional Grassmann charts.

The motivation for conditions 3 and 4 is that they can make it easier for every admissible subspace to intersect the same spectral obstruction.

These are search heuristics, not proven sufficient conditions.

My strongest recommendation: reproduce Fernando's \\(8\\)-dimensional example inside your own code and calculate its complete left minimal-index sequences. This will tell you how the published two-order obstruction manifests itself in B.9 and the descriptor-pencil representation.

That is more informative than generating another hundred unrestricted random instances.

# 6. Q5 — Is the zero-index count standard in matrix-pencil theory?

Yes. It is a standard consequence of minimal polynomial basis theory.

However, your particular formula is useful enough that I recommend stating it explicitly as a lemma.

## 6.1 General result

Let

\\[ P(\lambda)\in\mathbb C[\lambda]^{a\times b} \\]

have normal rank \\(h\\), and suppose its left minimal indices are

\\[ \varepsilon_1,\ldots,\varepsilon\_{a-h}. \\]

Then

\\[ \boxed{ \dim\\{\phi\in\mathbb C^{1\times a}: \phi P(\lambda)\equiv0,\  \phi\text{ constant}\\} = \\#\\{j:\varepsilon_j=0\\}. } \tag{19} \\]

This follows from the predictable-degree property of a reduced minimal basis.

To see why, take a row-minimal basis

\\[ N(\lambda) \\]

of the left nullspace.

Its row degrees are precisely the left minimal indices.

Every polynomial left-null vector has a unique representation

\\[ y(\lambda)=f(\lambda)N(\lambda), \\]

where \\(f(\lambda)\\) is a polynomial row vector.

For a row-reduced minimal basis, the predictable-degree property says that the degree of a nonzero polynomial combination is determined by the degrees of its coefficients and the corresponding minimal indices.

In particular, a nonzero constant left-null vector can only involve basis rows of degree zero, with constant coefficients.

Conversely, every degree-zero row of \\(N(\lambda)\\) is a constant left-null vector.

Therefore, the dimension of the constant left-nullspace equals the number of zero minimal indices.

## 6.2 Application to your pencil

For

\\[ Q\_{\mathcal L}(\lambda) = \begin{bmatrix} \lambda\mathcal L-\mathcal LA\\\ CA\\\ C \end{bmatrix}, \\]

write a constant left vector as

\\[ \phi=(\phi_1,\phi_2,\phi_3). \\]

The identity

\\[ \phi Q\_{\mathcal L}(\lambda)\equiv0 \\]

gives

\\[ \phi_1\mathcal L=0 \\]

from the coefficient of \\(\lambda\\).

Assuming \\(\mathcal L\\) has full row rank,

\\[ \phi_1=0. \\]

The remaining condition is

\\[ \begin{bmatrix}\phi_2&\phi_3\end{bmatrix} \begin{bmatrix}CA\\\C\end{bmatrix} =0. \\]

Consequently,

\\[ \dim\ker\_{\mathrm{left,const}}Q\_{\mathcal L} = 2p-r_1. \\]

Applying (19),

\\[ \boxed{ \\#\\{j:\varepsilon_j=0\\}=2p-r_1. } \\]

Since the total number of left minimal indices is

\\[ m=q+2p-h, \\]

we obtain

\\[ \boxed{ \\#\\{j:\varepsilon_j>0\\} =q+r_1-h. } \\]

Thus B.9 follows directly.

## 6.3 Literature and presentation

The standard theory of minimal bases, minimal indices and their degree properties is discussed in the matrix-polynomial literature.

A useful reference is the work on computing root polynomials and minimal bases of matrix pencils, which explicitly relates polynomial nullspace dimensions to minimal-index multiplicities through block Toeplitz matrices.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

ScienceDirect+1



I would present your result as:

Lemma (Zero left minimal-index multiplicity).

For the pencil \\(Q\_{\mathcal L}(\lambda)\\), assuming \\(\mathcal L\\) has full row rank,

\\[ m_0(Q\_{\mathcal L}) = \dim\ker\_{\mathrm{left,const}}Q\_{\mathcal L} = 2p-\operatorname{rank}[C;CA]. \\]

Here \\(m_0\\) denotes the multiplicity of zero among the left minimal indices.

This formulation is self-contained and makes the subsequent counting argument immediate.

It is not necessary to claim that the underlying principle is new. The value of your contribution is its explicit specialisation to the functional-observer pencil and the resulting obstruction B.9.

# 7. Q6 — Gröbner bases, resultants, or algebraic geometry?

I recommend a combination, but with a clear division of labour:

- Use elimination theory for small-dimensional examples.
- Use algebraic geometry to understand the structure of the entire augmentation family.
- Use exact rank and Toeplitz computations for discovering the relevant strata.

There is one important issue concerning your observation that the spectrally feasible set appears to have measure zero.

We need to understand this observation before selecting the computational method.

## 7.1 First, distinguish the feasible and infeasible sets

For a fixed augmentation, let

\\[ f_1(\lambda;\Theta),\ldots, f_N(\lambda;\Theta) \\]

be the maximal minors of the relevant pencil, where \\(\Theta\\) denotes the augmentation parameters.

The spectral condition is

\\[ \gcd\_{\lambda} \bigl(f_1,\ldots,f_N\bigr)=1. \\]

The failure condition is

\\[ \exists\lambda\in\mathbb C: \quad f_1(\lambda;\Theta)=\cdots= f_N(\lambda;\Theta)=0. \\]

Introduce an additional variable \\(\lambda\\). Then the failure set is the projection onto the parameter coordinates of the algebraic incidence set

\\[ \mathcal X= \left\\{ (\Theta,\lambda): f_1(\lambda;\Theta)=\cdots=f_N(\lambda;\Theta)=0 \right\\}. \\]

By the constructibility theorem, this projection is a constructible set.

It need not be closed in the original parameter space.

This is an important technical point: simply taking an elimination ideal may describe the Zariski closure of the projection rather than the exact set of parameters with a finite common root.

## 7.2 Why resultants need care

For two polynomials \\(f\\) and \\(g\\), the resultant gives a convenient common-root test when their degrees are fixed and their leading coefficients are controlled.

However, in your problem:

- there are many maximal minors;
- their degrees may vary with the augmentation parameters;
- their leading coefficients may vanish on special parameter strata;
- a common root at infinity must not be confused with a common finite root.

Consequently, a naive resultant calculation can produce false obstructions or miss exceptional degree-drop cases.

I recommend the following approach.

Step 1. Stratify by degree profile.

Separate the parameter space according to the degrees of the maximal minors.

Step 2. Use subresultants or Bézout identities.

On each fixed-degree stratum, determine whether the minors have a nonconstant gcd.

Step 3. Treat exceptional leading-coefficient loci separately.

Use saturation and constructible elimination to avoid confusing finite roots with roots at infinity.

Step 4. Compare with the Toeplitz rank condition.

This provides an independent exact verification of the result.

## 7.3 A better formulation using the Toeplitz matrix

There is an additional advantage to your new Toeplitz criterion.

For a fixed augmentation, (5b) is equivalent to

\\[ \operatorname{rank}T_s = (q+2p)(s+1)-(s+1)m+s. \\]

When the entries of \\(T_s\\) are polynomial in the augmentation parameters, this is a determinantal condition.

Thus the problem can be represented without explicitly computing all maximal minors of the original pencil.

One can impose an exact rank condition using:

- vanishing of all minors of order \\(t+1\\);
- nonvanishing of at least one minor of order \\(t\\).

The nonvanishing condition can be represented over the real numbers by an auxiliary variable and a sum-of-squares construction, or by a suitable finite chart decomposition.

This gives a direct route to Gröbner-basis experiments.

It also provides a useful consistency check against the Smith-form implementation.

## 7.4 What does the zero-measure observation mean?

Suppose a chart of the augmentation family is described by an algebraic variety \\(X\\).

If the spectral-feasibility condition defines a nonempty Zariski-open subset of an irreducible component of \\(X\\), then it is Zariski dense in that component.

In that case, it cannot have zero measure relative to the smooth real part of that component.

Therefore, if your experiments genuinely indicate that the feasible set has zero relative measure, at least one of the following possibilities should be investigated:

1. The feasible set lies in a lower-dimensional algebraic stratum.
2. The augmentation family has several irreducible components, and only some components contain feasible points.
3. The parameterisation has redundant variables or non-generic singularities.
4. The observed zero-measure phenomenon is caused by the sampling procedure.
5. The spectral condition is constructible but not open on the parameter space being sampled, because of degree drops or exceptional leading-coefficient behaviour.

The fourth possibility should not be overlooked.

Random sampling in an ambient parameter space can completely miss a lower-dimensional component, even when that component contains all feasible augmentations.

## 7.5 My recommendation: a hybrid algebraic-geometric method

I would not choose between Gröbner bases and geometry. They should be used together.

Proposed workflow

1. Construct the exact algebraic augmentation family.

   Obtain the polynomial equations for (5a) in each complete chart.
2. Decompose the family.

   Use Gröbner bases, primary decomposition or numerical algebraic geometry to identify irreducible components.
3. Construct the spectral-degeneracy locus.

   Use the Toeplitz rank condition or the maximal-minor incidence equations.
4. Determine component-wise feasibility.

   Decide whether the spectral-good subset is empty, dense, or confined to a proper subvariety of each component.
5. Extract exact certificates.

   Use ideal membership, saturation, elimination or explicit rational witnesses.

For small \\(n\\), this is entirely reasonable.

For larger \\(n\\), full primary decomposition may become expensive, so I would first use the rank-counting obstruction B.9 to eliminate entire cases before invoking symbolic algebra.

# 8. An important issue: the claimed uniqueness of the minimum augmentation

There is one point in II.2 that I would investigate before accepting the computational architecture.

Your document states:

> At \\(q=\mathrm{cl}\\), there is exactly one (5a)-satisfying row space, namely \\(V\_{\min}\\).

This assertion is stronger than the equality

\\[ \mathrm{cl}=q_0. \\]

The equality of minimum dimensions does not imply uniqueness of the minimising subspace.

Moreover, the 2026 functional-observer paper describes the complete family of minimum-order algebraically admissible augmentations. Its nullspace parametrisation should be compared directly with your claimed unique row space.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



I see two separate mathematical questions:

1. Is the minimum dimension unique?
2. Is the subspace attaining that dimension unique?

The first is established by the functional-observability-index characterisation, subject to the equivalence proved in Section 3.

The second needs an independent proof.

## 8.1 A potential issue with the closure algorithm

Your proposed iteration is:

\\[ V_0=\operatorname{row}L_0, \\]

followed by adding \\(xA\\) whenever

\\[ xA\notin V+W, \qquad W=\operatorname{row}[C;CA]. \\]

There is a subtlety.

Suppose \\(U\\) is another feasible subspace. From

\\[ xA\in U+W \\]

one cannot conclude that

\\[ xA\in U. \\]

Thus, adding the unmodified vector \\(xA\\) does not automatically preserve the property that the current space is contained in every feasible subspace.

The choice of representatives modulo \\(W\\) may matter.

This is not a proof that your algorithm is incorrect. It is a proof that the claimed minimality does not follow merely from the stated iteration.

I recommend requiring the implementation to produce a certificate of both properties:

\\[ L_0\subseteq V, \qquad VA\subseteq V+W, \\]

and

\\[ \dim V=q_0, \\]

where \\(q_0\\) is independently computed from the functional observability indices.

If these three conditions hold, the dimension is certified to be minimal.

To establish uniqueness, one must additionally prove that every other feasible subspace of dimension \\(q_0\\) equals \\(V\\).

That last step should not be inferred from the dimension calculation.

This is an important verification task because it affects the statement in II.2 that the minimal-order decision is a single structural test.

Even if several minimal-order row spaces exist, the minimum-order problem remains a single existential feasibility problem, but it is no longer a test of one unique augmentation.

# 9. Consolidated answers to the six questions

| Question | Conclusion                                                                                                               |
| -------- | ------------------------------------------------------------------------------------------------------------------------ |
| Q1       | Yes. The nullspace-pencil criterion provides an alternative to Kronecker computation.                                    |
| Q2       | \\(\mathrm{cl}=\sum_j\eta_j\\), under the stated identification and functional-observability assumptions.                |
| Q3       | The gap can exceed one. A published example has gap exactly two.                                                         |
| Q4       | A persistent spectral obstruction across consecutive algebraic augmentation families can force a two-order gap.          |
| Q5       | The zero-index count is a standard consequence of minimal-basis theory; its specialisation is worth stating explicitly.  |
| Q6       | Use a hybrid of exact algebraic geometry, elimination and Toeplitz rank computations. Do not assume generic feasibility. |

The most important new conclusion is Q3: your empirical conjecture has a known counterexample.

The most important methodological issue is the uniqueness claim in II.2.

# 10. What I would change in the project immediately

I recommend making the following changes to the mathematical and computational programme.

## 10.1 Replace the empirical order-gap conjecture

Remove the conjecture

\\[ q\_{\min}\in\\{\mathrm{cl},\mathrm{cl}+1\\}. \\]

Replace it with the established bounds

\\[ \boxed{ \mathrm{cl}\le q\_{\min}\le n_0-p. } \\]

The lower bound is the algebraic feasibility threshold; the upper bound is guaranteed by functional observability.

The spectral order spectrum may have gaps, and the published example demonstrates a gap of two.

## 10.2 Add the stronger B.9 obstruction

Record

\\[ \boxed{ q+r_1-s\le h\<q+r_1. } \\]

This should be used as an inexpensive preprocessing test before constructing Toeplitz matrices.

If either inequality fails, the augmentation cannot satisfy (5b).

## 10.3 Replace the closure implementation as the authority on minimum dimension

Use the functional-observability-index calculation as an independent minimum-dimension certificate.

Then compare the closure algorithm against it.

If they disagree, do not modify the functional-index result to fit the closure output. First investigate the closure construction and its minimality proof.

## 10.4 Reproduce the published two-order-gap example

This should become a permanent regression test.

Verify:

- the functional indices \\((2,1)\\);
- the algebraic minimum \\(q_0=3\\);
- failure at orders 3 and 4 over all charts;
- existence at order 5;
- feasibility at the upper endpoint 6.

Then calculate your own invariants:

\\[ h,\quad r_1,\quad s,\quad (\varepsilon_1,\ldots,\varepsilon_m),\quad d\_{\mathrm{fin}}. \\]

This will connect the functional-observer nullspace representation with your Kronecker-index theory.

## 10.5 Investigate the geometry before attempting general hardness

For each irreducible component of the algebraic augmentation family, investigate the spectral-degeneracy locus.

I would particularly like to know whether the published two-order-gap example has the following property:

\\[ \text{The spectral-degeneracy locus contains the entire algebraic augmentation family at }q_0,q_0+1. \\]

If so, identify the algebraic relations responsible for this containment.

That could lead to a useful structural theorem explaining when additional augmentation rows are necessary.

# 11. My proposed next research target

Rather than pursuing all six questions simultaneously, I would formulate one central problem that combines the most promising findings.

Proposed research problem

Spectral obstruction and augmentation-order gap

Let \\(q_0=\sum_j\eta_j\\) be the minimum algebraically admissible order.

Characterise the smallest integer \\(k\ge0\\) such that there exists an order-\\((q_0+k)\\) augmentation satisfying (5b).

In particular, determine structural conditions on \\((A,C,L_0)\\) that force

\\[ k=0,\quad k=1,\quad\text{or}\quad k\ge2. \\]

Express these conditions in terms of:

- the invariant subspaces of \\(A\\);
- the dimensions of the observation-related subspaces;
- the positive left minimal indices;
- the rank structure of the descriptor pencil;
- the algebraic geometry of the complete augmentation family.

I would begin with a more restricted theorem.

Conjecture to investigate: If every algebraically admissible augmentation at orders \\(q_0,\ldots,q_0+k-1\\) has a positive finite-divisor degree, but an admissible augmentation at order \\(q_0+k\\) has zero finite-divisor degree, then the minimum order is exactly \\(q_0+k\\).

This is essentially a reformulation of the problem, not yet a structural theorem. The research objective is to replace the universal spectral tests by computable conditions on the original matrices \\(A,C,L_0\\).

The most promising intermediate step is to derive bounds on the finite-divisor degree:

\\[ d\_{\mathrm{fin}} = s-\sum_j\varepsilon_j. \\]

Your new counting result gives

\\[ 0\le d\_{\mathrm{fin}} \le s-(q+r_1-h). \\]

If this upper bound can be strengthened using invariant-subspace information, it may become possible to prove feasibility or impossibility without computing the complete Kronecker structure.

## 12. Final assessment

The new report contains several genuine advances.

Most importantly:

- You now have a simple necessary obstruction that can eliminate entire classes of augmentations.
- You have experimentally confirmed that the number of positive minimal indices and their total degree carry different information.
- You have an efficient Toeplitz-based method for recovering the complete index sequence.
- You have identified the distinction between algebraic feasibility and spectral feasibility as the central source of the minimum-order gap.

The literature comparison also resolves two questions decisively:

1. The functional-observability-index sum is the appropriate algebraic minimum.
2. A gap of two is not merely theoretically possible; it has already been demonstrated by an explicit example with complete chart-based verification.

I would now prioritise three tasks:

First: resolve the closure algorithm's claimed uniqueness and verify \\(\mathrm{cl}=q_0\\) on the discrepant instances.

Second: reproduce and analyse the published two-order-gap example using your left-minimal-index and Toeplitz framework.

Third: investigate whether the B.9 counting obstruction can be strengthened into a structural criterion involving the invariant subspaces of \\(A\\).

These tasks have a much higher immediate mathematical value than expanding the random-instance experiments or beginning an unrestricted NP-hardness reduction.

The project is now in a position to investigate a more fundamental question: not simply whether a spectrally admissible augmentation exists, but which structural properties of the original system determine the number of additional augmentation dimensions needed to remove the finite spectral obstruction.

That is the direction I would pursue.

### Principal external reference

Fernando, T. (2026), Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger, arXiv:2609.37992.

[Read the 2026 paper on arXiv](https://arxiv.org/abs/2609.37992?utm_source=chatgpt.com).

The results discussed above are from the September 2026 preprint; they should be cited as preprint results unless a later peer-reviewed publication is verified.