# Mathematical review of `46_experiments_review.md`: experimental validity, an exact emptiness criterion, and the next research direction

The new report is valuable because it moves the project beyond abstract algebraic geometry and tests the structural claims against actual observer instances. More importantly, it identifies three distinct causes of failed computations:

1. sampling a positive-codimension admissible set;
2. attempting a construction in a dimensionally impossible regime;
3. choosing fixed top blocks that are incompatible with the required row-space inclusion.

These are mathematically different phenomena and should not be grouped together as generic computational failures.

My overall assessment is:

- Experiment 1: the computations are useful evidence about pointwise behaviour, but the sampled “all bad” instances do not establish the existence of bad irreducible components.
- Experiment 2: the negative sampling results are inconclusive for exactly the reason identified in the report.
- Experiment 3: the dimension obstruction is correct, subject to a small clarification about injectivity of \\(A|\_K\\).
- Experiment 4: this is a valid one-sided feasibility experiment. An exact good witness proves nonemptiness; an exact bad witness proves that the bad locus is nonempty. Together they show that the bad locus is a nonempty proper closed subset of the admissible locus, but not that every irreducible component has a good point.
- Experiment 5: the \\(L_0=e_2^{\mathsf T}\\) emptiness argument is structurally meaningful. It can be generalized into a necessary-and-sufficient criterion involving a subspace \\(S\\) of the kernel-coordinate space.
- Experiment 6: the unresolved software failure should be replaced by an independent exact linear-algebra implementation. The report already contains enough structure to do this without relying on a symbolic rank routine.

My main recommendation is to introduce an exact Grassmannian criterion for nonemptiness of the rank-\\(\omega\\) admissible stratum. This directly answers Question 2 and gives a systematic preliminary step for Question 3. It should also substantially reduce wasted computation in the constrained region.

I will develop that criterion first, because it is the most useful new result.

# 1. The mathematical structure of the experiments

Let

\\[ K=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \qquad \dim K=k, \\]

and let \\(N_K\in\mathbb F^{n\times k}\\) have columns forming a basis of \\(K\\).

Write the augmentation as

\\[ \mathcal L= \begin{bmatrix} L_0\\\R \end{bmatrix}, \qquad m=q-r, \\]

where \\(L_0\\) is fixed and \\(R\\) has \\(m\\) rows.

The two restricted matrices are

\\[ H(R)=\mathcal L N_K, \qquad H_A(R)=\mathcal LA N_K. \\]

Separate their fixed and variable rows:

\\[ H(R)= \begin{bmatrix} U_0\\\B_1 \end{bmatrix}, \qquad H_A(R)= \begin{bmatrix} V_0\\\B_2 \end{bmatrix}, \\]

where

\\[ U_0=L_0N_K,\qquad V_0=L_0AN_K, \\]

and

\\[ B_1=RN_K,\qquad B_2=RAN_K. \\]

The admissibility conditions on the rank-\\(\omega\\) stratum are

\\[ \operatorname{rank}H(R)=\omega, \qquad \operatorname{rank} \begin{bmatrix} H(R)\\\H_A(R) \end{bmatrix} =\omega. \\]

The second equality is equivalent to

\\[ \operatorname{row}H_A(R)\subseteq\operatorname{row}H(R). \\]

This row-space formulation is the right one for the experiments. It makes the role of the fixed top blocks explicit.

The report also uses the reachable-pair characterization

\\[ B_1Z_1+B_2Z_2=0, \qquad Z= \begin{bmatrix}Z_1\\\Z_2\end{bmatrix} \text{ a basis of }\ker T, \\]

where

\\[ T:K\oplus K\longrightarrow\mathbb F^n, \qquad T(v,w)=v+Aw. \\]

This is the exact linear compatibility relation for the variable bottom blocks.&#x20;

46_experiments_review\.md



The crucial observation is that each row of the bottom blocks satisfies the same compatibility equation independently. This permits an exact reduction to a subspace problem.

# 2. Question 1: Are Experiments 1 and 4 methodologically sound?

## 2.1 Experiment 1: what the sampling actually proves

The report describes the following setup:

\\[ n=4,\quad p=1,\quad q=2,\quad r=1, \\]

with

\\[ C=e_1^{\mathsf T}, \qquad K=\operatorname{span}\\{e_2,e_3\\}, \\]

and the remaining rows of \\(A\\) selected randomly. For each instance, \\(R\\) was enumerated over

\\[ \\{-1,0,1\\}^4. \\]

The reported counts are:

| Observed category                           | Number of instances |
| ------------------------------------------- | ------------------- |
| No sampled admissible point                 | 16                  |
| Sampled admissible points, all bad          | 12                  |
| Sampled admissible points, all good         | 2                   |
| Both good and bad sampled admissible points | 2                   |

These counts are useful as a diagnostic record. They show that the small finite grid contains examples of different pointwise behaviours, including examples in which good and bad admissible points coexist.&#x20;

46_experiments_review\.md



However, the interpretation must remain strictly one-sided.

### A. The twelve “all bad” instances do not establish a bad component

For a fixed instance, let

\\[ \mathcal X_1 = \left\\{ R: \operatorname{rank}H(R)=1,\quad \operatorname{rank} \begin{bmatrix}H(R)\\\H_A(R)\end{bmatrix}=1 \right\\}. \\]

The bad locus is

\\[ \mathcal B_1 = \left\\{ R\in\mathcal X_1: \text{the reduced pencil loses column rank at some finite }\lambda \right\\}. \\]

At \\(\omega=1\\), the pointwise spectral criterion reduces to

\\[ \operatorname{rank}[H(R)\ H_A(R)]=2 \\]

for a good point. Hence the bad condition is

\\[ \operatorname{rank}[H(R)\ H_A(R)]<2. \\]

This is a closed rank condition relative to the admissible locus.

But suppose every admissible point encountered on the finite grid is bad. That only establishes

\\[ \mathcal X_1\cap\\{-1,0,1\\}^4 \subseteq\mathcal B_1. \\]

It does not establish

\\[ \mathcal X_1\subseteq\mathcal B_1. \\]

Nor does it establish that any irreducible component of \\(\mathcal X_1\\) is contained in \\(\mathcal B_1\\).

A finite grid is not generally Zariski dense in the admissible locus. The fact that all sampled points satisfy a polynomial equation does not imply that the equation vanishes identically on an irreducible component.

This distinction is essential.

### B. The two mixed instances establish more, but still not a bad component

For either mixed instance, suppose the reported good and bad points are exactly verified admissible points:

\\[ R\_{\mathrm{good}}\in\mathcal X_1\setminus\mathcal B_1, \qquad R\_{\mathrm{bad}}\in\mathcal B_1. \\]

Then we have proved

\\[ \mathcal X_1\setminus\mathcal B_1\ne\varnothing, \qquad \mathcal B_1\ne\varnothing. \\]

Since \\(\mathcal B_1\\) is closed relative to \\(\mathcal X_1\\), this establishes that the bad locus is a nonempty proper closed subset of the admissible locus.

That is a valid and useful conclusion.

It does not establish that the bad point belongs to an irreducible component entirely contained in the bad locus. The bad point may lie in a component that also contains good points.

To prove the existence of a bad irreducible component, one must establish that for some irreducible component \\(X_i\\) of \\(\mathcal X_1\\),

\\[ X_i\subseteq\mathcal B_1. \\]

A single bad point is insufficient. A finite collection of bad points is also insufficient, unless supplemented by an argument proving that those points are Zariski dense in the component under consideration.

### C. What would establish a bad component?

There are several valid approaches.

Method 1: Exact component equations.

Compute an irreducible decomposition

\\[ \mathcal X_1=X_1\cup\cdots\cup X_s. \\]

Then test whether the defining equations of \\(\mathcal B_1\\) vanish identically on any \\(X_i\\).

Method 2: Generic-point test.

For each component \\(X_i\\), compute its function field

\\[ F_i=\mathbb F(X_i). \\]

Evaluate the generic spectral gcd over \\(F_i[\lambda]\\). If the gcd is nonconstant, the generic point is bad, and the entire component is bad because the bad locus is closed.

If the gcd is constant, the good set is nonempty open dense in that component.

Method 3: A direct algebraic identity.

Sometimes the structure of \\(A,C,L_0\\) gives a relation forcing

\\[ \operatorname{rank}[H(R)\ H_A(R)]<2 \\]

for every admissible \\(R\\). This is exactly what the report successfully did for one choice of \\(L_0\\) in Experiment 5.

This third method is often the cheapest and most informative.

### Verdict on Experiment 1

Valid as finite-grid evidence

The experiment is methodologically sound as an exploratory enumeration, provided its conclusions are restricted to the grid.

The two mixed instances are particularly useful: they give exact examples in which the admissible set contains both good and bad points, assuming the points were checked exactly.

But the twelve “all bad” instances should be recorded as:

> No good admissible point was found in the enumerated grid.

They should not be recorded as:

> The admissible locus is all bad.

And they certainly do not yet prove the existence of bad irreducible components.

## 2.2 Experiment 4: a valid one-sided feasibility experiment

The report's successful construction uses

\\[ n=9,\qquad p=3,\qquad C=[I_3\ 0], \\]

and an \\(A\\) for which

\\[ \operatorname{rank} \begin{bmatrix}C\\\CA\end{bmatrix}=6, \qquad k=3, \\]

with

\\[ K=\operatorname{span}\\{e_7,e_8,e_9\\}. \\]

The construction gives

\\[ K\cap AK=\\{0\\}, \\]

and the chosen \\(A\\) is injective on \\(K\\). The report then constructs factorizations

\\[ H=UV,\qquad H_A=GV, \\]

with \\(U\\) full column rank and \\(V\\) full row rank, and solves for \\(R\\). It reports 125 good and 75 bad constructions.&#x20;

46_experiments_review\.md



There are two distinct conclusions here.

### A. One exact good construction proves feasibility

If even one constructed \\(R\_\*\\) is exactly verified to satisfy

\\[ \operatorname{rank}H(R\_\*)=\omega, \\]

\\[ \operatorname{rank} \begin{bmatrix}H(R\_\*)\\\H_A(R\_\*)\end{bmatrix} =\omega, \\]

and

\\[ \operatorname{rank}P\_{R\_\*}(\lambda)=\omega \quad\text{for every finite }\lambda, \\]

then

\\[ \boxed{\mathcal X\_\omega\setminus\mathcal B\_\omega\ne\varnothing.} \\]

This is a rigorous existence certificate.

No sampling-density argument is needed. The point itself proves nonemptiness.

For the spectral check, I would require an exact gcd certificate, not a floating-point root calculation. For example, if \\(m_I(\lambda)\\) are the maximal minors of the reduced pencil, exhibit polynomials \\(u_I(\lambda)\\) such that

\\[ \sum_I u_I(\lambda)m_I(\lambda)=1. \\]

This is an explicit Bézout certificate of spectral feasibility.

### B. One good and one bad construction prove the bad locus is nonempty and proper

If the 125 good and 75 bad constructions are all exact and admissible, then

\\[ \mathcal B\_\omega\ne\varnothing \\]

and

\\[ \mathcal B\_\omega\ne\mathcal X\_\omega. \\]

Since the bad locus is closed relative to the admissible locus, it is a nonempty proper closed subset of \\(\mathcal X\_\omega\\).

That is a stronger statement than mere feasibility.

However, it does not imply that every irreducible component of \\(\mathcal X\_\omega\\) has a good point. The admissible locus may be reducible. It is possible that one component is entirely bad while another component contains good points.

Thus the correct conclusion is:

> The admissible locus contains both good and bad points, and the global bad locus is a nonempty proper closed subset of it.

Do not strengthen this to:

> The bad locus is proper on every irreducible component.

That stronger claim requires componentwise analysis.

### C. One structural clarification about the surjectivity condition

The report describes the free regime using

\\[ K\cap AK=\\{0\\}. \\]

This condition alone is not sufficient to guarantee that the reachable-pair map is surjective.

Recall

\\[ T(v,w)=v+Aw,\qquad v,w\in K. \\]

Then

\\[ \ker T = \\{(-Aw,w):w\in K,\ Aw\in K\\}. \\]

Consequently,

\\[ \ker T=0 \iff K\cap A^{-1}K=\\{0\\}. \\]

Equivalently, one needs both

\\[ \ker(A|\_K)=\\{0\\} \\]

and

\\[ AK\cap K=\\{0\\}. \\]

The distinction matters: \\(AK\cap K=\\{0\\}\\) does not rule out a nonzero vector \\(w\in K\\) with \\(Aw=0\\).

In the explicit Experiment 4 construction, however, \\(A|\_K\\) is injective, because

\\[ Ae_7=e_4,\quad Ae_8=e_5,\quad Ae_9=e_6. \\]

Thus the stronger condition is satisfied, and the surjectivity argument is valid.

### Verdict on Experiment 4

Valid one-sided feasibility evidence

The experiment is mathematically sound provided that the generated points and gcd checks are exact. It establishes nonemptiness of the good and bad sets, but it does not settle the irreducible-component structure.

I would retain the construction as a benchmark instance for testing future algorithms.

# 3. Question 2: An exact criterion for emptiness in terms of \\(L_0N_K\\), \\(L_0AN_K\\), and compatibility

This is the central new result I recommend adding to the project.

The report's \\(L_0=e_2^{\mathsf T}\\) example is not an isolated accident. It is an instance of a general criterion that characterizes the nonemptiness of the rank-\\(\omega\\) admissible stratum.

## 3.1 Set up the row-space problem

Let

\\[ E=\operatorname{row}(U_0) =\operatorname{row}(L_0N_K), \\]

and

\\[ F_0=\operatorname{row}(V_0) =\operatorname{row}(L_0AN_K). \\]

Let

\\[ Z= \begin{bmatrix}Z_1\\\Z_2\end{bmatrix} \\]

be a basis matrix for \\(\ker T\\).

For a candidate \\(\omega\\)-dimensional subspace

\\[ S\subseteq\mathbb F^k, \\]

define

\\[ \mathcal C_S = \left\\{ (x,y)\in S\times S: xZ_1+yZ_2=0 \right\\}. \\]

Here \\(x,y\\) are row vectors in \\(\mathbb F^{1\times k}\\).

Now define the first projection

\\[ X_S = \operatorname{pr}\_1(\mathcal C_S) = \left\\{ x\in S: \exists y\in S,\ xZ_1+yZ_2=0 \right\\}. \\]

Equivalently,

\\[ \boxed{ X_S=\\{x\in S:xZ_1\in S Z_2\\}. } \\]

The sign is immaterial because \\(SZ_2\\) is a linear subspace.

The interpretation is:

- \\(S\\) is the row space that we want \\(H\\) to have;
- \\(E\\) is the row space already forced by the fixed top block of \\(H\\);
- \\(F_0\\) is the row space forced by the fixed top block of \\(H_A\\);
- \\(X_S\\) consists of precisely those bottom rows of \\(H\\) that can be completed by a compatible bottom row of \\(H_A\\), while keeping both rows inside \\(S\\).

This is exactly the interaction that the \\(L_0=e_2^{\mathsf T}\\) example exposes.

## 3.2 The nonemptiness theorem

Theorem (Grassmannian criterion for rank-\\(\omega\\) admissibility).

Let \\(m=q-r\\), and fix the observer data \\(A,C,L_0\\), the basis \\(N_K\\), and the compatibility basis \\(Z=[Z_1^{\mathsf T},Z_2^{\mathsf T}]^{\mathsf T}\\).

There exists an augmentation \\(R\\) satisfying

\\[ \operatorname{rank}H(R)=\omega, \qquad \operatorname{rank} \begin{bmatrix} H(R)\\\H_A(R) \end{bmatrix} =\omega \\]

if and only if there exists an \\(\omega\\)-dimensional subspace

\\[ S\in\operatorname{Gr}(\omega,k) \\]

such that

\\[ \boxed{ \begin{aligned} & E+F_0\subseteq S,\\\ & E+X_S=S,\\\ & \omega-\dim E\le m. \end{aligned} } \tag{G} \\]

All dimensions and subspaces may be taken over \\(\mathbb R\\) when the desired augmentation \\(R\\) is real.

### Proof: necessity

Suppose an admissible \\(R\\) exists.

Let

\\[ S=\operatorname{row}H(R). \\]

By the rank condition,

\\[ \dim S=\omega. \\]

Since

\\[ H(R)=\begin{bmatrix}U_0\\\B_1\end{bmatrix}, \\]

we have

\\[ E\subseteq S. \\]

Similarly, admissibility gives

\\[ \operatorname{row}H_A(R)\subseteq S. \\]

Since the top rows of \\(H_A\\) are \\(V_0\\), this implies

\\[ F_0\subseteq S. \\]

Thus

\\[ E+F_0\subseteq S. \\]

Write the rows of \\(B_1,B_2\\) as

\\[ (x_1,\ldots,x_m), \qquad (y_1,\ldots,y_m). \\]

Because both bottom blocks have their rows in \\(S\\),

\\[ x_i,y_i\in S. \\]

The reachable-pair compatibility equation

\\[ B_1Z_1+B_2Z_2=0 \\]

holds row by row, so

\\[ x_iZ_1+y_iZ_2=0. \\]

Therefore

\\[ x_i\in X_S. \\]

Since the rows of \\(H\\) span \\(S\\),

\\[ S=E+\operatorname{span}\\{x_1,\ldots,x_m\\}. \\]

In particular,

\\[ E+X_S=S. \\]

Finally, adding \\(m\\) rows to a row space of dimension \\(\dim E\\) can increase its dimension by at most \\(m\\). Therefore

\\[ \omega-\dim E\le m. \\]

All three conditions in (G) are necessary.

### Proof: sufficiency

Conversely, suppose there exists an \\(\omega\\)-dimensional subspace \\(S\\) satisfying (G).

Since

\\[ E+X_S=S, \\]

we can choose

\\[ d=\omega-\dim E \\]

vectors

\\[ x_1,\ldots,x_d\in X_S \\]

whose images form a basis of \\(S/E\\).

By the definition of \\(X_S\\), for each \\(i\\) there exists \\(y_i\in S\\) satisfying

\\[ x_iZ_1+y_iZ_2=0. \\]

Because \\(d\le m\\), append \\(m-d\\) zero pairs:

\\[ x_i=0,\qquad y_i=0,\qquad i=d+1,\ldots,m. \\]

Construct \\(B_1,B_2\\) from these rows. Then

\\[ B_1Z_1+B_2Z_2=0. \\]

By the exact reachable-pair characterization, there exists an \\(R\\) such that

\\[ B_1=RN_K,\qquad B_2=RAN_K. \\]

The rows of \\(H\\) span

\\[ E+\operatorname{span}\\{x_1,\ldots,x_d\\}=S, \\]

so

\\[ \operatorname{rank}H=\dim S=\omega. \\]

Also, \\(F_0\subseteq S\\) and every \\(y_i\in S\\). Hence every row of \\(H_A\\) belongs to \\(S=\operatorname{row}H\\). Therefore

\\[ \operatorname{rank} \begin{bmatrix}H\\\H_A\end{bmatrix} =\omega. \\]

This proves sufficiency. \\(\square\\)

## 3.3 Immediate consequences

The criterion gives several inexpensive necessary conditions.

First,

\\[ \boxed{ \dim(E+F_0)\le\omega. } \tag{N1} \\]

If the fixed top blocks already span more than \\(\omega\\) dimensions, the stratum is empty.

Second,

\\[ \boxed{ \omega-\dim E\le m. } \tag{N2} \\]

If the bottom block has too few rows to raise the row rank of \\(H\\) from \\(\dim E\\) to \\(\omega\\), the stratum is empty.

These are simple tests that should be performed before any rank factorization or random construction.

But (N1) and (N2) are not sufficient in general. The compatibility constraint can prevent the bottom rows of \\(H\\) from supplying the missing directions.

That obstruction is captured exactly by

\\[ E+X_S=S. \\]

## 3.4 A particularly useful simplification in the surjective regime

Suppose

\\[ \ker T=\\{0\\}. \\]

Then there are no compatibility equations:

\\[ Z_1,Z_2\text{ have zero columns}. \\]

Consequently,

\\[ X_S=S \\]

for every \\(S\\).

The Grassmannian criterion reduces to the existence of an \\(\omega\\)-dimensional subspace \\(S\\) satisfying

\\[ E+F_0\subseteq S, \qquad \omega-\dim E\le m. \\]

Such a subspace exists if and only if

\\[ \boxed{ \dim(E+F_0)\le\omega\le\dim E+m. } \tag{S} \\]

This is a very simple exact test.

It is also a useful audit of Experiment 4. Under the actual surjectivity hypothesis, nonemptiness of the admissible rank-\\(\omega\\) stratum can be checked directly from the two fixed top-block row spaces and the number of available bottom rows.

There is no need to randomly search for an admissible point merely to discover whether the stratum is empty.

## 3.5 Applying the theorem to the \\(L_0=e_2^{\mathsf T}\\) example

The report considers

\\[ n=5,\quad p=1,\quad q=3,\quad r=1,\quad m=2,\quad k=3, \\]

with \\(L_0=e_2^{\mathsf T}\\) and \\(\omega=2\\).

The fixed top blocks are

\\[ U_0=(1,0,0), \qquad V_0=(0,1,0). \\]

Therefore

\\[ E=\operatorname{span}\\{e_1^{\mathsf T}\\}, \qquad F_0=\operatorname{span}\\{e_2^{\mathsf T}\\}. \\]

Since \\(\omega=2\\), any candidate \\(S\\) must contain both \\(E\\) and \\(F_0\\). Thus it is forced:

\\[ S=\operatorname{span}\\{e_1^{\mathsf T},e_2^{\mathsf T}\\}. \\]

The report states that the compatibility relation reduces to

\\[ B_2e_3=B_1e_2. \\]

For a compatible row pair \\((x,y)\in S\times S\\), we have

\\[ ye_3=0, \\]

because every \\(y\in S\\) has zero third coordinate.

The compatibility equation therefore forces

\\[ xe_2=0. \\]

Hence

\\[ X_S\subseteq\operatorname{span}\\{e_1^{\mathsf T}\\}=E. \\]

It follows that

\\[ E+X_S=E\ne S. \\]

The Grassmannian criterion fails. Thus

\\[ \boxed{\mathcal X_2=\varnothing} \\]

for this choice of \\(L_0\\).

This reproduces the report's structural argument and places it inside a general necessary-and-sufficient theorem. The original calculation is recorded in the report.&#x20;

46_experiments_review\.md



This is a genuine mathematical result, not merely a failure to find a point.

## 3.6 What this criterion does and does not solve

The criterion is exact, but it is not automatically a linear-algebra-only algorithm for arbitrary \\(\omega\\).

The unknown \\(S\\) ranges over the Grassmannian

\\[ \operatorname{Gr}(\omega,k). \\]

The condition

\\[ X_S=\\{x\in S:xZ_1\in SZ_2\\} \\]

depends on \\(S\\) in a nonlinear way.

Nevertheless, it provides a much better formulation than searching directly over \\(R\\):

- it separates the fixed top-block obstruction from the variable bottom rows;
- it isolates the compatibility obstruction;
- it gives immediate dimension-based emptiness tests;
- it reduces the problem to an \\(\omega\\)-dimensional subspace search;
- it gives a simple closed-form criterion when \\(\Theta\\) is surjective.

This should become part of the project's main structural theory.

# 4. The dimension obstruction in Experiments 3 and 4

The report correctly identifies a structural restriction arising from the choice of \\(C\\) and \\(A\\). I would make the proof explicit and slightly sharpen the statement.

Suppose \\(C\\) has full row rank \\(p\\), so

\\[ \dim\ker C=n-p. \\]

Since

\\[ K=\ker C\cap\ker CA, \\]

we have

\\[ K\subseteq\ker C. \\]

For \\(v\in K\\), we also have \\(CAv=0\\). Thus

\\[ Av\in\ker C. \\]

Consequently,

\\[ K+AK\subseteq\ker C. \\]

Now suppose

\\[ K\cap AK=\\{0\\}. \\]

This implies

\\[ \dim(K+AK)=\dim K+\dim AK. \\]

However, to conclude that \\(\dim AK=k\\), we also need \\(A|\_K\\) to be injective.

In the situation where

\\[ K\cap AK=\\{0\\} \quad\text{and}\quad A|\_K\text{ is injective}, \\]

we obtain

\\[ \dim AK=k, \\]

and therefore

\\[ 2k=\dim(K+AK)\le n-p. \\]

Hence

\\[ \boxed{n-p\ge 2k.} \\]

This is a necessary condition for the stronger free regime in which

\\[ \ker T=0. \\]

For \\(k=3\\), it requires

\\[ n-p\ge6. \\]

Also, because

\\[ \operatorname{rank}\begin{bmatrix}C\\\CA\end{bmatrix} =n-k, \\]

and the stacked matrix has at most \\(2p\\) rows,

\\[ n-k\le2p. \\]

Combining this with \\(n-p\ge2k\\) gives

\\[ p\ge k. \\]

Thus, for \\(k=3\\),

\\[ \boxed{n\ge9,\qquad p\ge3} \\]

are necessary in this free regime.

This explains why the \\(n=6,p=2,k=3\\) construction was structurally impossible. The report's diagnosis is correct.&#x20;

46_experiments_review\.md



### Recommendation

Before constructing a free-regime example, check:

\\[ \begin{aligned} &\dim K=k,\\\ &A|\_K\text{ is injective},\\\ &K\cap AK=\\{0\\},\\\ &n-p\ge2k,\\\ &\operatorname{rank}\begin{bmatrix}C\\\CA\end{bmatrix}=n-k. \end{aligned} \\]

The first three conditions characterize \\(\ker T=0\\); the last two provide immediate dimension checks.

Do not use \\(K\cap AK=\\{0\\}\\) alone as the surjectivity test.

# 5. Question 3: Is the proposed constrained-region protocol sound?

The proposed protocol is directionally correct:

1. test top-block compatibility;
2. parameterize the compatibility space;
3. construct rank-\\(\omega\\) points by factorization;
4. test spectral feasibility by exact gcd.

I agree with its basic structure. I would add several steps and change the order slightly.

## 5.1 Recommended exact protocol

### Step 0. Fix the arithmetic field

If the data are rational, work over \\(\mathbb Q\\) throughout.

If the data are algebraic, use an exact representation of the relevant number field.

Do not use floating-point rank tests to certify an exact rank stratum. Numerical rank can be useful for exploratory screening, but the final conclusion must be exact.

### Step 1. Compute \\(K\\) and its basis exactly

Compute

\\[ K=\ker\begin{bmatrix}C\\\CA\end{bmatrix} \\]

using exact Gaussian elimination.

Choose a basis matrix \\(N_K\\).

Verify

\\[ \begin{bmatrix}C\\\CA\end{bmatrix}N_K=0 \\]

and

\\[ \operatorname{rank}N_K=k. \\]

This avoids errors from inconsistent basis conventions later.

### Step 2. Compute the reachable-pair compatibility space

Construct

\\[ T(v,w)=v+Aw,\qquad v,w\in K. \\]

In coordinates relative to \\(N_K\\), this is the matrix

\\[ \begin{bmatrix}N_K&AN_K\end{bmatrix}. \\]

Compute an exact basis

\\[ Z=\begin{bmatrix}Z_1\\\Z_2\end{bmatrix} \\]

for its kernel.

Verify

\\[ N_KZ_1+AN_KZ_2=0. \\]

Then the bottom blocks must satisfy

\\[ B_1Z_1+B_2Z_2=0. \\]

This is the correct compatibility equation. It should be tested directly before attempting any construction.

### Step 3. Compute and test the fixed top-block spaces

Compute

\\[ U_0=L_0N_K,\qquad V_0=L_0AN_K, \\]

and

\\[ E=\operatorname{row}(U_0),\qquad F_0=\operatorname{row}(V_0). \\]

Apply the immediate necessary conditions

\\[ \dim(E+F_0)\le\omega, \\]

and

\\[ \omega-\dim E\le m. \\]

If either fails, the stratum is empty.

This should be done before factorization or random sampling.

### Step 4. Determine whether the reachable-pair map is surjective

Check

\\[ \ker T=\\{0\\}. \\]

Equivalently,

\\[ K\cap A^{-1}K=\\{0\\}. \\]

If this holds, the compatibility constraints disappear, and the exact nonemptiness criterion reduces to

\\[ \boxed{ \dim(E+F_0)\le\omega\le\dim E+m. } \\]

This is the cheapest possible outcome.

If \\(\ker T\ne0\\), retain the compatibility equations and use the Grassmannian criterion (G).

### Step 5. Search for a candidate row space \\(S\\)

For the constrained case, search for

\\[ S\in\operatorname{Gr}(\omega,k) \\]

with

\\[ E+F_0\subseteq S, \qquad E+X_S=S. \\]

A practical implementation should use pivot charts on the Grassmannian.

For example, choose a pivot index set \\(J\\) of size \\(\omega\\) and represent \\(S\\) as the row space of

\\[ \begin{bmatrix}I\_\omega&W\end{bmatrix} \\]

after a suitable coordinate permutation.

Then the condition

\\[ xZ_1\in SZ_2 \\]

can be written as a finite system of linear equations in the coordinates of \\(x\\) and the auxiliary vector \\(y\\), with coefficients polynomial in the chart variables \\(W\\).

The condition

\\[ E+X_S=S \\]

can be expressed by a rank condition.

This converts the abstract Grassmannian criterion into finitely many algebraic chart problems.

### Step 6. Construct the bottom blocks

Once a suitable \\(S\\) is found, choose vectors

\\[ x_1,\ldots,x_d\in X_S, \qquad d=\omega-\dim E, \\]

whose images form a basis of \\(S/E\\).

For each \\(x_i\\), solve the exact linear equation

\\[ x_iZ_1+y_iZ_2=0, \qquad y_i\in S. \\]

Append zero pairs if \\(d\<m\\).

This constructs \\(B_1,B_2\\) with the desired row-space and compatibility properties.

### Step 7. Recover \\(R\\) by exact linear algebra

Solve

\\[ RN_K=B_1,\qquad RAN_K=B_2. \\]

This is a linear system in the entries of \\(R\\).

If it is inconsistent, either the compatibility calculation or the implementation is wrong, because the exact reachable-pair characterization says that the compatibility condition is necessary and sufficient.

In practice, I would retain the residual

\\[ \begin{bmatrix} RN_K-B_1 & RAN_K-B_2 \end{bmatrix} \\]

as part of the verification output.

### Step 8. Verify admissibility independently

For the recovered \\(R\\), recompute

\\[ H(R),\qquad H_A(R) \\]

directly from the original definitions.

Then verify exactly:

\\[ \operatorname{rank}H(R)=\omega, \\]

and

\\[ \operatorname{rank} \begin{bmatrix}H(R)\\\H_A(R)\end{bmatrix} =\omega. \\]

Do not rely solely on the intermediate factorization.

### Step 9. Test the spectral condition by exact gcd

Choose a rank factorization

\\[ H=UV,\qquad H_A=GV, \\]

where

\\[ U\in\mathbb F^{q\times\omega} \\]

has full column rank and

\\[ V\in\mathbb F^{\omega\times k} \\]

has full row rank.

Then

\\[ \lambda H-H_A=(\lambda U-G)V. \\]

Since \\(V\\) has full row rank,

\\[ \operatorname{rank}(\lambda H-H_A)=\omega \iff \operatorname{rank}(\lambda U-G)=\omega. \\]

Compute the \\(\omega\times\omega\\) maximal minors of

\\[ P(\lambda)=\lambda U-G \\]

and their gcd exactly.

- Gcd equal to a nonzero constant: good.
- Gcd nonconstant: bad.
- All maximal minors identically zero: inconsistent with the assumed full-column-rank \\(U\\), and indicates an implementation error.

For a good point, save a Bézout identity:

\\[ \sum_I u_I(\lambda)\det P_I(\lambda)=1. \\]

For a bad point, save the exact nonconstant gcd.

These are reproducible certificates.

### Step 10. Separate pointwise feasibility from componentwise genericity

A single good point proves that the stratum is nonempty and feasible.

It does not determine the generic behaviour of every component.

If componentwise information is needed, proceed only after obtaining a valid parameterization of the admissible set, and compute the generic gcd over the function field of each component.

## 5.2 Is factorization \\(H=UV,\ H_A=GV\\) sound?

Yes. It is exact on the admissible rank-\\(\omega\\) stratum.

If

\\[ \operatorname{rank}H=\omega, \qquad \operatorname{row}H_A\subseteq\operatorname{row}H, \\]

then there exists a full-column-rank \\(U\\) and full-row-rank \\(V\\) such that

\\[ H=UV,\qquad H_A=GV. \\]

Conversely, any such factorization with the stated ranks implies

\\[ \operatorname{rank}H=\omega, \qquad \operatorname{row}H_A\subseteq\operatorname{row}H. \\]

So the factorization is not an approximation or a heuristic. It is an exact parameterization of the admissible pairs.

However, there are two important implementation cautions.

First: the fixed top blocks impose

\\[ U\_{\mathrm{top}}V=U_0, \qquad G\_{\mathrm{top}}V=V_0. \\]

These equations must be enforced exactly.

Second: in the constrained regime, the bottom blocks must also satisfy

\\[ B_1Z_1+B_2Z_2=0. \\]

Choosing arbitrary \\(U,G,V\\) and then assuming that the resulting pair is reachable is not valid.

The factorization should be combined with the compatibility equations, not substituted for them.

# 6. Question 4: What should be prioritized now?

The report asks whether to:

(a) push the constrained-region experiment;

(b) move to componentwise symbolic computation of the generic gcd;

(c) do something else.

My recommendation is (c), followed by a targeted version of (a), and then (b).

The next step should be to implement the Grassmannian emptiness criterion. This is likely to be more informative than either more blind random constructions or immediate full component decomposition.

## 6.1 Why not immediately pursue componentwise symbolic gcd?

Componentwise generic-gcd computation is mathematically well motivated. But it requires a usable description of the irreducible components of the admissible locus.

At present, the report shows that the team has not yet reliably established nonemptiness for one constrained instance with \\(L_0=e_4^{\mathsf T}\\). Performing a full componentwise symbolic analysis before resolving this basic question may be unnecessarily expensive.

The right order is:

1. decide whether the stratum is empty;
2. if nonempty, construct an exact point;
3. determine the relevant component or components;
4. compute generic gcds on those components.

This is not a rejection of Stage 2. It is a more efficient way of preparing for it.

## 6.2 Why not simply continue the constrained experiment by random sampling?

The report has already identified that random sampling is ineffective on positive-codimension loci.&#x20;

46_experiments_review\.md



The constrained admissible locus is precisely such a locus. Randomly sampling \\(R\\) in a small integer box is unlikely to find points satisfying all the required rank and row-space constraints.

The next constrained-region computation should therefore be constructive:

- use the fixed top-block spaces;
- use the compatibility basis;
- search for \\(S\\);
- construct compatible bottom rows;
- recover \\(R\\) exactly.

This makes the search target the actual admissible geometry rather than hoping to hit it accidentally.

# 7. A focused plan for the unresolved \\(L_0=e_4^{\mathsf T}\\) experiment

I would make this the immediate computational target.

The report says that the \\(L_0=e_4^{\mathsf T}\\) top blocks are compatible, but the symbolic routine crashed twice, with a non-square-matrix error. Replacing the rank routine with exact Gaussian elimination did not remove the crash, and the cause remains unidentified.&#x20;

46_experiments_review\.md



I would not spend more time debugging the existing symbolic pipeline before obtaining an independent structural test.

For that instance, compute the following quantities manually or with a short exact-rational script:

1. \\(N_K\\).
2. \\(U_0=L_0N_K\\).
3. \\(V_0=L_0AN_K\\).
4. A basis \\(Z=[Z_1^{\mathsf T},Z_2^{\mathsf T}]^{\mathsf T}\\) for \\(\ker T\\).
5. The dimensions of \\(E\\), \\(F_0\\), and \\(E+F_0\\).
6. The Grassmannian chart equations for \\(S\in\operatorname{Gr}(2,3)\\).
7. The subspace \\(X_S\\) on each chart.
8. Whether \\(E+X_S=S\\) can hold.

Since

\\[ k=3,\qquad\omega=2, \\]

the Grassmannian

\\[ \operatorname{Gr}(2,3) \\]

has dimension only \\(2\\). This is an especially manageable test case.

In fact, every two-dimensional subspace of \\(\mathbb F^3\\) is the kernel of a nonzero covector, so one can parameterize \\(S\\) by a projective point

\\[ [\sigma_1:\sigma_2:\sigma_3]\in\mathbb P^2 \\]

through

\\[ S=\\{x\in\mathbb F^{1\times3}:x\sigma=0\\}. \\]

The inclusion

\\[ E+F_0\subseteq S \\]

becomes a set of linear equations in \\(\sigma\\). This may determine \\(S\\) uniquely or leave a simple projective family.

For each candidate \\(S\\), compute

\\[ X_S=\\{x\in S:xZ_1\in SZ_2\\} \\]

by exact linear algebra, then test

\\[ E+X_S=S. \\]

This is substantially simpler than searching directly over all entries of \\(R\\).

### Possible outcomes

There are three useful outcomes.

Outcome 1: No \\(S\\) satisfies the criterion.

Then the rank-two admissible stratum is empty. This is a structural proof, analogous to the \\(L_0=e_2^{\mathsf T}\\) case.

Outcome 2: Some \\(S\\) satisfies the criterion, but the current script cannot recover \\(R\\).

Then the mathematical stratum is nonempty, and the problem is purely computational. The proof of the theorem guarantees a compatible pair and hence an \\(R\\). One should implement the recovery step independently.

Outcome 3: Some \\(S\\) satisfies the criterion and an exact \\(R\\) is recovered.

Then compute the generic gcd on the component containing that point, or first construct a local parameterization of the admissible family around the point.

This gives a clear progression from structural feasibility to spectral classification.

# 8. What the experiments say about tractability and hardness

The new report does not yet provide evidence that the general problem is hard. It does, however, make the source of possible complexity more precise.

I would distinguish four layers.

| Layer | Mathematical problem                                            | Current status                 |
| ----- | --------------------------------------------------------------- | ------------------------------ |
| 1     | Fixed \\(R\\): test spectral feasibility                        | Solved by exact univariate gcd |
| 2     | \\(\omega=1\\): pointwise spectral condition                    | Rank criterion                 |
| 3     | \\(k=\omega\\): affine-family spectral existence                | Generic algebraic test         |
| 4     | \\(k>\omega\\): existence inside the nonlinear admissible locus | Main unresolved layer          |

The new Grassmannian criterion helps with Layer 4 by characterizing nonemptiness of the admissible stratum before the spectral condition is considered.

It does not by itself solve the spectral existence problem on that stratum.

This distinction is important. The project should not conflate:

\\[ \mathcal X\_\omega\ne\varnothing \\]

with

\\[ \mathcal X\_\omega\setminus\mathcal B\_\omega\ne\varnothing. \\]

The first is admissibility. The second is admissibility plus spectral feasibility.

The proposed criterion (G) solves the first question exactly. The generic-gcd analysis is still needed for the second.

### A potentially important consequence

Suppose the Grassmannian criterion yields a parameterization of the admissible stratum over an irreducible parameter space. Then the genericity theorem can be applied to the spectral bad locus on that parameter space, provided the parameterization is genuinely affine or the corresponding closedness argument is established on the parameter space.

This suggests a two-stage approach:

\\[ \boxed{ \begin{array}{c} \text{Grassmannian admissibility analysis}\\\ \Downarrow\\\ \text{parameterize the admissible family}\\\ \Downarrow\\\ \text{generic gcd on each irreducible component}\\\ \Downarrow\\\ \text{decide whether some component is generically good} \end{array} } \\]

The key technical issue is whether the chosen parameterization preserves the correct irreducible components and whether the real locus has real points. These must be checked, not assumed.

# 9. A few further methodological recommendations

## 9.1 Record exact witnesses, not only aggregate counts

For each successful instance, save:

- the exact matrices \\(A,C,L_0,R\\);
- the basis \\(N_K\\);
- the compatibility basis \\(Z\\);
- the matrices \\(H,H_A\\);
- the exact ranks;
- the maximal minors of the reduced pencil;
- the gcd;
- a Bézout identity for good points.

This will turn the experiments into reproducible mathematical certificates.

Aggregate counts such as “125 good and 75 bad” are useful summaries, but they are not substitutes for the underlying witnesses.

## 9.2 Distinguish four types of negative results

Every failed experiment should be classified as one of:

1. Proven empty: a structural argument or exact algebraic certificate proves \\(\mathcal X\_\omega=\varnothing\\).
2. No point found: a search failed to find a point.
3. Numerical failure: the computational routine failed or returned an unreliable result.
4. Wrong target regime: the chosen dimensions or fixed blocks made the intended construction impossible.

Experiment 2 is type 2. Experiment 3 is type 4. The \\(L_0=e_2^{\mathsf T}\\) part of Experiment 5 is type 1. The \\(L_0=e_4^{\mathsf T}\\) attempt is type 3.

This classification should be included in the project's experimental log.

## 9.3 Avoid using random integer samples to estimate component structure

Random samples can show that a set is nonempty, but they are unreliable for identifying its irreducible components or determining whether a polynomial vanishes identically on a component.

For componentwise questions, use:

- exact elimination;
- ideal decomposition;
- rational function fields;
- generic-point computations;
- or a proved algebraic parameterization.

Random sampling is best used after a component or parameterization has been identified, as a consistency check.

# 10. Direct answers to the four questions

## Question 1

Are Experiments 1 and 4 methodologically sound as evidence?

Yes, with carefully limited conclusions.

- Experiment 1 is sound as finite-grid evidence. Its twelve sampled “all bad” instances do not establish a bad irreducible component. The two mixed instances prove the existence of both good and bad admissible points, assuming exact verification, but still do not prove a bad component.
- Experiment 4 is a valid one-sided feasibility experiment. One exact good point proves nonemptiness of the feasible set. One exact bad point additionally proves the bad locus is nonempty. Together they show the bad locus is a nonempty proper closed subset of the admissible locus, but do not prove that every component contains good points.

## Question 2

Is there a general criterion for emptiness in terms of the top blocks and compatibility space?

Yes. The Grassmannian criterion (G) above is necessary and sufficient:

\\[ \boxed{ \exists S\in\operatorname{Gr}(\omega,k): \quad E+F_0\subseteq S,\quad E+X_S=S,\quad \omega-\dim E\le m, } \\]

where

\\[ E=\operatorname{row}(L_0N_K), \qquad F_0=\operatorname{row}(L_0AN_K), \\]

and

\\[ X_S=\\{x\in S:xZ_1\in SZ_2\\}. \\]

In the surjective reachable-pair regime, this simplifies to

\\[ \boxed{ \dim(E+F_0)\le\omega\le\dim E+m. } \\]

This gives an exact systematic test for choosing \\(L_0\\), and it explains the \\(L_0=e_2^{\mathsf T}\\) obstruction.

## Question 3

Is the proposed protocol sound, and should anything be added?

Yes, but it should be expanded to:

1. compute \\(K,N_K\\) exactly;
2. compute \\(Z_1,Z_2\\) exactly;
3. test the top-block dimension obstructions;
4. test whether the reachable-pair map is surjective;
5. apply the Grassmannian criterion;
6. construct compatible bottom rows;
7. recover \\(R\\) by exact linear solving;
8. verify the original rank conditions independently;
9. compute the spectral gcd exactly;
10. only then perform componentwise generic analysis.

The main addition is Step 5, which should precede random factorization.

## Question 4

What should be prioritized?

My recommendation is:

\\[ \boxed{\text{(c) first: implement the exact emptiness criterion; then pursue a targeted (a); then (b).}} \\]

Specifically:

- implement the Grassmannian criterion for \\(k=3,\omega=2\\);
- use it to resolve the \\(L_0=e_4^{\mathsf T}\\) case;
- construct an exact admissible point if one exists;
- then compute the generic gcd on the relevant component.

I would not yet launch a general hardness reduction. The current experiments have not identified a genuine complexity barrier, and the new structural criterion may substantially simplify the admissibility layer.

# 11. Final recommendation: the next deliverable should be a structural emptiness report

I suggest making the next research milestone very concrete.

Proposed deliverable: “Exact admissibility criterion and constrained \\(k=3,\omega=2\\) classification.”

It should contain:

1. the theorem (G) and its proof;
2. the surjective special case (S);
3. the complete derivation of the \\(L_0=e_2^{\mathsf T}\\) obstruction;
4. an exact analysis of \\(L_0=e_4^{\mathsf T}\\);
5. at least one exact admissible witness if the latter stratum is nonempty;
6. the reduced pencil and exact gcd for that witness;
7. a clear distinction between pointwise feasibility and componentwise generic feasibility.

The immediate mathematical objective is not yet to prove hardness or tractability of the full REAL-AUG problem. It is to understand the admissible geometry well enough that the spectral question can be posed on the correct components.

The central new criterion gives you a systematic way to do precisely that.

In short: the experiments are useful, but their strongest contribution is not the numerical counts. It is the identification of the top-block/compatibility obstruction. The Grassmannian criterion turns that observation into an exact theorem and should be the next foundation of the project.