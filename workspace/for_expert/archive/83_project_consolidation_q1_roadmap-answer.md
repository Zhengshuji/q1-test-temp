# Strategic assessment of q1: what is established, what remains open, and the best route forward

My recommendation is to make the fixed-\\(\kappa\_{\rm obs}\\) FPT result the principal theorem, develop fixed-\\(q\\) polynomial time as a second theorem, and keep unrestricted hardness as a parallel research question.

I would not yet predict that q1 is in P, nor that it is \\(\exists\mathbb R\\)-complete. Both remain compatible with the results in the report.

There is, however, a useful additional conclusion: the two upper bounds can be combined with an explicit existential-real formulation, and the hardness programme now has a much better candidate source than isolated multiplication gates—affine rank minimization with a fixed global rank bound.

I will address the seven questions, but first I want to make one distinction precise: Fernando's characterization and the complexity of the prescribed-row completion problem are related, but they are not the same theorem.

# 1. The current mathematical picture

The starting reduction is sound:

\\[ K_0=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \qquad H=LN,\qquad H_A=LAN. \\]

With \\(N\\) a basis of \\(K_0\\),

\\[ (5a)\iff\operatorname{row}H_A\subseteq\operatorname{row}H \\]

and

\\[ (5b)\iff \operatorname{rank}(\lambda H-H_A)=\operatorname{rank}H \quad\forall\lambda\in\mathbb C. \\]

An additional identity is worth putting at the centre of the paper. Since (5b) holds at \\(\lambda=0\\),

\\[ \operatorname{rank}H_A=\operatorname{rank}H. \\]

Combining this with (5a) gives

\\[ \boxed{\operatorname{row}H_A=\operatorname{row}H.} \tag{1} \\]

Thus q1 is not merely a rank-completion problem. It asks for two matrices with the same row space, subject to a shared row-wise linear constraint on their free row pairs, and a full-rank condition on their pencil.

Set

\\[ \mathcal T=\operatorname{row}[N\ AN], \qquad d_0=\dim\mathcal T, \qquad r=q-r_0, \\]

and

\\[ \boxed{\kappa\_{\rm obs}=r d_0.} \\]

Every free row pair belongs to \\(\mathcal T\\), and conversely every element of \\(\mathcal T\\) is realizable by a state-space row. So \\(\kappa\_{\rm obs}\\) is exactly the dimension of the total compressed free-row space.

This gives three algorithmic facts that should be stated separately:

\\[ \boxed{ \begin{aligned} q1&\in\exists\mathbb R,\\\ \text{for every fixed }q:\quad q1&\in\mathrm P,\\\ q1&\in\mathrm{FPT}(\kappa\_{\rm obs}). \end{aligned}} \tag{2} \\]

The first is an unrestricted membership statement; the second is an XP-style parameterized upper bound; the third is a genuine FPT result.

The last two do not imply that unrestricted q1 is in P.

## 1.1 A direct existential-real membership certificate

The report assumes q1 belongs to \\(\exists\mathbb R\\). This can be justified explicitly, without enumerating all maximal minors.

Fix a rank stratum \\(\omega>0\\), and parameterize each free row pair by coordinates in \\(\mathcal T\\). This uses at most \\(r d_0\\) real variables.

Factor

\\[ H=XB,\qquad H_A=GB, \\]

where

\\[ X\in\mathbb R^{q\times\omega},\qquad G\in\mathbb R^{q\times\omega},\qquad B\in\mathbb R^{\omega\times k}. \\]

Impose

\\[ e\_\omega(X^{\mathsf T}X)>0,\qquad e\_\omega(BB^{\mathsf T})>0. \\]

These ensure that \\(X\\) has full column rank, \\(B\\) has full row rank, and hence \\(H=XB\\) has rank exactly \\(\omega\\).

The equality \\(H_A=GB\\) is equivalent to (5a): because \\(B\\) has full row rank and \\(X\\) has full column rank,

\\[ \operatorname{row}(XB)=\operatorname{row}B, \\]

so \\(GB\\) has its rows in \\(\operatorname{row}H\\).

Now

\\[ P(\lambda)=(\lambda X-G)B. \\]

Since \\(B\\) has full row rank,

\\[ (5b)\iff Q(\lambda):=\lambda X-G \text{ has full column rank for every }\lambda\in\mathbb C. \\]

This condition is equivalent to the existence of a polynomial left inverse

\\[ S(\lambda)Q(\lambda)=I\_\omega. \tag{3} \\]

We can bound its degree by \\(2\omega-2\\). Indeed, the maximal minors \\(m_I(\lambda)\\) of \\(Q(\lambda)\\) have degree at most \\(\omega\\). If they have no common complex root, they have a real polynomial Bezout identity

\\[ \sum_I u_I(\lambda)m_I(\lambda)=1, \qquad \deg u_I<\omega. \\]

Writing \\(Q_I\\) for the square submatrix on rows \\(I\\), and \\(E_I\\) for the corresponding row-selection matrix, the adjugate identity gives

\\[ \operatorname{adj}(Q_I)E_IQ=m_I I\_\omega. \\]

Therefore

\\[ S(\lambda)= \sum_Iu_I(\lambda)\operatorname{adj}(Q_I(\lambda))E_I \\]

satisfies (3), and has degree at most \\(2\omega-2\\).

Quantifying the coefficients of \\(S\\) introduces only polynomially many variables and equations. Finally, take a finite disjunction over \\(\omega=0,\ldots,\min(q,k)\\).

For \\(\omega=0\\), the condition is simply \\(H=H_A=0\\), which can be tested directly.

This supplies a polynomial-size existential-real certificate for q1. It also gives a clean conceptual interpretation of (5b): the compressed pencil must be left-unimodular over \\(\mathbb R[\lambda]\\).

That formulation will be useful in both the algorithmic paper and any future hardness reduction.

# 2. Question 1: what is the likely unrestricted complexity?

There is no defensible way to infer the unrestricted complexity from the two parameterized algorithms alone.

All three possibilities remain open:

- \\(q1\in\mathrm P\\);
- q1 is \\(\exists\mathbb R\\)-complete;
- q1 has an intermediate classification, such as an XP upper bound in \\(q\\), FPT in \\(\kappa\_{\rm obs}\\), and parameterized hardness for \\(q\\).

There is a particularly important logical point:

\\[ \boxed{ \text{\\(\exists\mathbb R\\)-completeness is compatible with FPT in }\kappa\_{\rm obs}. } \\]

An \\(\exists\mathbb R\\)-complete problem can be easy on instances with a small structural parameter. Its hard instances may simply have \\(\kappa\_{\rm obs}\\) growing with the source instance.

Likewise, fixed-\\(q\\) polynomial time does not rule out \\(\exists\mathbb R\\)-hardness. A hardness reduction would have to make \\(q\\) grow.

## 2.1 What would support each outcome?

| Possible outcome                | Evidence needed                                                                                                                       |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Unrestricted P                  | An algorithm whose polynomial exponent is independent of both \\(q\\) and \\(\kappa\_{\rm obs}\\), exploiting global pencil structure |
| \\(\exists\mathbb R\\)-complete | A polynomial-time reduction with soundness under unrestricted \\(R\\), preferably through one global row-space or rank constraint     |
| Parameterized classification    | For example, FPT in \\(\kappa\_{\rm obs}\\) and W[1]-hardness in \\(q\\), together with the existing fixed-\\(q\\) XP algorithm       |

My research judgment is that \\(\exists\mathbb R\\)-hardness deserves continued investigation, but there is not yet enough evidence to call it the most likely outcome.

Why? Because the pencil condition has substantial algebraic structure. In particular, it is not arbitrary polynomial feasibility: it is a degree-one polynomial matrix with a global left-invertibility condition. This may permit algorithms that do not appear in generic \\(\exists\mathbb R\\) problems.

Conversely, the row-space and rank constraints are expressive enough that one should not assume a polynomial algorithm merely because the individual spectral test is tractable.

The right present description is therefore: q1 is in \\(\exists\mathbb R\\), has two meaningful parameterized upper bounds, and its unrestricted complexity is open.

# 3. Question 2: the best route to hardness

Among the candidates in the report, I would investigate affine rank minimization first, matroid realization second, and polynomial-matrix unimodularity as a way to express the target constraints rather than as the initial source problem.

There is a particularly relevant recent result.

## 3.1 Affine rank minimization: the strongest blueprint

Majumdar's 2026 preprint, Affine Rank Minimization is ER-Complete, studies the problem

\\[ \exists X\in\mathbb R^{m\times n}: \quad \langle A_i,X\rangle=b_i\ (i=1,\ldots,s), \quad \operatorname{rank}X\le k. \\]

It claims \\(\exists\mathbb R\\)-completeness even for fixed \\(k=3\\). Its reduction uses a single global matrix, affine equations on its entries, rank-forcing multiplication gadgets, a fixed-rank gauge submatrix, and a composition lemma to prevent unintended interactions.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



This is relevant to q1 for a specific reason: the earlier q1 hardness attempt failed because it tried to make independent local gates communicate through individual rows. ARM instead puts all gate quantities into one global rank-constrained object, and uses a gauge block to make the represented values unambiguous.

That is conceptually close to what q1 needs.

I would study the ARM reduction in detail, particularly its:

- gauge fixing;
- treatment of repeated circuit variables;
- proof that arbitrary completions cannot invalidate gate equations;
- global composition lemma.

Those are exactly the ingredients missing from the q1 multiplication construction.

### What prevents an immediate reduction?

ARM has arbitrary affine constraints coupling entries of \\(X\\). In q1, the free compressed rows satisfy

\\[ (H_i,(H_A)\_i)\in\mathcal T \\]

for one common linear space \\(\mathcal T\\). These constraints are row-local and identical across the free rows.

Furthermore, q1 has the additional identity

\\[ \operatorname{row}H_A=\operatorname{row}H \\]

and the pencil condition

\\[ \operatorname{rank}(\lambda H-H_A)=\operatorname{rank}H \quad\forall\lambda. \\]

Thus the missing reduction has to transform ARM's affine constraints and rank bound into this much more structured completion architecture. The ARM theorem does not automatically imply q1-hardness.

My recommendation: attempt an ARM-to-q1 reduction before building more local multiplication gadgets. Start with ARM(3), and ask whether its gauge block can be represented by fixed rows of \\(H,H_A\\), while its affine constraints can be encoded through the common row-pair space \\(\mathcal T\\). The main obstruction will be the per-row separability of \\(\mathcal T\\), not the general idea of rank-based multiplication.

## 3.2 Matroid realization: the strongest incidence-oriented source

A second candidate is real matroid representability. Kim, de Mesmay, and Miltzow prove that deciding whether a matroid is representable over \\(\mathbb R\\) is \\(\exists\mathbb R\\)-complete, already for matroids of rank three. This result is published in Discrete Mathematics & Theoretical Computer Science (2024).&#x20;

[image](https://www.google.com/s2/favicons?domain=https://dmtcs.episciences.org\&sz=32)

dmtcs.episciences.org



This source has a different advantage from ARM. A matroid representation is a global collection of vectors whose dependence relations encode the instance. It is therefore naturally related to

\\[ W=\operatorname{row}H =\operatorname{row}H_A. \\]

However, a matroid instance specifies the independence of many different subsets. q1 does not directly let us prescribe an arbitrary rank function on subsets of free rows. It gives one global row-space equality, together with the restriction \\(\mathcal T\\) and the pencil condition.

So a matroid reduction would need to show how the desired subset-dependence pattern is exposed through the particular pair \\((H,H_A)\\). Without that, “matroid realization is incidence-like” is only an analogy, not a reduction.

### My ranking of the sources

| Source                                 | Compatibility with q1                                                  | Main missing bridge                                                                                  |
| -------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Affine rank minimization, fixed rank 3 | Strong conceptual match: global rank, affine constraints, gauge fixing | Encode arbitrary affine coupling through row-wise \\(\mathcal T\\) and preserve the pencil condition |
| Real matroid realization, rank 3       | Strong geometric match: global vector dependencies and incidence       | Encode many prescribed subset ranks using q1's much more limited global conditions                   |
| Polynomial-matrix unimodularity        | Strong match to (5b)                                                   | Find a hard input class with the special pencil form \\(\lambda X-G\\), tied to \\(\mathcal T\\)     |
| General structured matrix completion   | Potentially broad                                                      | Identify a source problem with exactly the same row-pair restrictions                                |

The most promising first experiment is ARM(3). Matroid realization is the best alternative if the intended reduction is based on subspace arrangements rather than affine rank constraints.

## 3.3 Direct global reduction may be better than a sound multiplication gadget

I would not insist that q1 first needs a standalone multiplication gate.

There is an important difference between:

\\[ \text{local gate reduction} \quad\text{and}\quad \text{global matrix reduction}. \\]

A local gate reduction tries to prove that every feasible \\(R\\) enforces a particular product equation. It is vulnerable to extra free rows, cross-block components, and alternative rank strata.

A global reduction could instead encode the source instance into a single prescribed row system and prove:

\\[ \text{source instance feasible} \iff \text{there exists a global }W,F \text{ satisfying the q1 constraints}. \\]

The variables may be decoded from a canonical submatrix or a gauge-fixed basis for \\(W\\), rather than from designated free-row indices.

This is the route I would explore. It is closer to ARM's proof strategy and respects the exchangeability of free rows.

# 4. Question 3: can sound multiplication be ruled out?

No general no-go theorem is currently justified.

The report has identified a real obstruction for a restricted class of constructions, but not a general impossibility.

There are three levels of statements.

### 4.1 A valid no-go for the universal-lift bypass architecture

Suppose the allowed free-row pair space is all of \\(\mathbb R^{2k}\\), as in the universal lift. If the fixed rows alone give a feasible pair when all free rows are set to zero, then the q1 instance is feasible independently of the intended multiplication variables.

Formally, if

\\[ (H_0,H\_{A,0}) \\]

satisfies both rank conditions after appending zero free rows, then

\\[ \exists R\ (5a)\wedge(5b) \\]

is automatically true for that instance.

This is a valid restricted obstruction. It explains exactly why the previous multiplication construction fails.

### 4.2 A valid no-go for fixed shared-port constructions

If

\\[ E_1\subseteq W,\qquad E_1\cap E_2=D \\]

with \\(D\\) a fixed line, then

\\[ D\subseteq W\cap E_2. \\]

If the intended port is required to be one-dimensional, it must equal \\(D\\). It cannot carry a variable line.

That rules out the fixed-intersection construction in the report, not global incidence or matrix-pencil constructions.

### 4.3 What a general no-go theorem would need to prove

A genuinely general no-go theorem would have to cover all choices of:

- dimensions \\(n,p,q,r_0\\);
- fixed matrices \\(A,C,L_0\\);
- per-row spaces \\(\mathcal T=\operatorname{row}[N\ AN]\\);
- feasible rank strata \\(\omega\\);
- possible global row-space decodings.

For example, a theorem might prove that every feasible set of decoded coordinates has a geometric property incompatible with the graph

\\[ \\{(x,y,z):z=xy\\}. \\]

But none of the present arguments establishes such a property.

The fact that q1 is a polynomially describable real-feasibility problem does not itself rule out multiplication. The conditions are nonlinear in the free coordinates through rank and determinant constraints.

### 4.4 The most promising construction principle

If I were to attempt sound multiplication again, I would use a gauge-fixed global rank representation, inspired by ARM, rather than a row-labelled gate.

The design should have:

1. A fixed anchor submatrix that forces the intended rank stratum.
2. A canonical basis for \\(W\\), obtained through this anchor.
3. A decoded scalar assigned to an invariant entry of the global factorization, rather than to a particular free row.
4. A global proof that every admissible completion obeys the arithmetic equations.
5. A pencil scaffold that guarantees the spectral condition exactly when the source constraints hold.

The key change is that the gauge fixes the coordinate system of the global row space. It does not attempt to fix the individual free rows.

This is only a proposed construction programme. I would not yet assign it a P label.

# 5. Question 4: parameterized hardness

The two algorithmic results have an important consequence for parameterized lower bounds.

## 5.1 Parameter \\(\kappa\_{\rm obs}\\)

Since the report proposes

\\[ q1\in\mathrm{FPT}(\kappa\_{\rm obs}), \\]

a proof that q1 is W[1]-hard when parameterized by \\(\kappa\_{\rm obs}\\) would imply

\\[ \mathrm{FPT}=\mathrm{W[1]} \\]

under standard fixed-parameter reductions.

Therefore I would not pursue W[1]-hardness for \\(\kappa\_{\rm obs}\\) unless there is a reason to suspect the FPT proof is wrong.

A more relevant lower-bound question is whether there is a kernelization or a stronger parameterized algorithm for \\(\kappa\_{\rm obs}\\). But one should not infer such improvements merely from the Gram construction.

## 5.2 Parameter \\(q\\)

For \\(q\\), the present result is

\\[ T(\mathcal I)=\mathcal L^{O(q^2)}. \\]

This is XP, not FPT.

W[1]-hardness with respect to \\(q\\) is compatible with an XP algorithm. It would suggest that the dependence of the polynomial exponent on \\(q\\) may be inherent, unless standard parameterized complexity classes collapse.

This is a legitimate lower-bound direction.

A plausible target would be a parameterized reduction from Multicolored Clique with

\\[ q=O(t), \\]

where \\(t\\) is the clique parameter. The reduction would have to arrange that the effective dimension

\\[ \kappa\_{\rm obs}=r\\,\operatorname{rank}[N\ AN] \\]

is allowed to grow with the graph size. This is essential: if the reduction also kept \\(\kappa\_{\rm obs}\\) bounded by a function of \\(t\\), it would contradict the FPT theorem unless FPT=W[1].

In other words, a q-parameterized hardness reduction must exploit growing per-row compressed freedom even though the number of observer rows stays small relative to the clique parameter.

Whether that can be achieved is open.

## 5.3 Parameterized lower-bound priority

| Parameter                                  | Current upper bound | Lower-bound assessment                                                                     |
| ------------------------------------------ | ------------------- | ------------------------------------------------------------------------------------------ |
| \\(q\\)                                    | XP                  | W[1]-hardness is worth investigating                                                       |
| \\(\kappa\_{\rm obs}\\)                    | FPT                 | W[1]-hardness would contradict the claimed FPT result unless FPT=W[1]                      |
| \\(d_0=\operatorname{rank}[N\ AN]\\) alone | No FPT bound stated | Potentially interesting, but \\(\kappa\_{\rm obs}\\) also contains the number of free rows |
| \\(r=q-r_0\\) alone                        | No FPT bound stated | Not enough, since \\(d_0\\) may be unbounded                                               |

A parameterized hardness theorem in \\(q\\) would complement the fixed-\\(q\\) result. It would not resolve unrestricted \\(\exists\mathbb R\\)-hardness by itself.

# 6. Question 5: novelty and positioning relative to Fernando and parametric linear systems

The algorithmic results have a plausible novelty claim, but the paper must be precise about what is new.

## 6.1 What Fernando's 2026 work already establishes

Fernando's Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger, arXiv:2609.37992, is a very close antecedent. It provides:

- an order-by-order characterization of algebraic and spectral observer feasibility;
- necessary and sufficient matrix-rank and matrix-pencil conditions;
- a nullspace parameterization of fixed-order realizations;
- a finite Grassmannian-chart parameterization covering all candidate nullspaces;
- a finite polynomial spectral test based on maximal-minor gcds.

These are explicit contributions of the paper, not merely background observations.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+3



Consequently, I would not claim novelty for:

\\[ (5a)\iff\operatorname{row}H_A\subseteq\operatorname{row}H, \\]

the matrix-pencil form of (5b), the use of nullspace coordinates, or the fact that fixed-order observer feasibility has a finite algebraic characterization.

Those belong to the existing observer-characterization framework.

### The important difference

Fernando's formulation starts with a prescribed functional \\(L\\), and considers an augmented functional matrix \\(\mathcal L\\) from which \\(L\\) must be recoverable, together with the reduced-realization requirement. The conditions (A) and (S) are imposed on \\(\mathcal L\\).&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



Your q1 formulation instead fixes a literal block:

\\[ \mathcal L=[L_0;R]. \\]

It asks whether the remaining rows can be completed while the rank conditions hold.

These formulations are closely related, but the exact equivalence depends on whether q1 includes the target-functional recoverability condition and the reducedness condition used by Fernando. It is important to write down this correspondence explicitly.

There is another complexity distinction. Fernando parameterizes fixed-order candidate nullspaces using Grassmannian charts. In the notation of his chart construction, the chart matrices have

\\[ d(m_L-d) \\]

parameters. In a reduced fixed-order setting with \\(r\\) independent target rows, \\(d=n-p-q\\) and \\(m_L=n-p-r\\), so the number of chart parameters becomes

\\[ (n-p-q)(q-r). \\]

This can grow linearly with \\(n\\), even when \\(q\\) is fixed. The number of charts can be polynomial for fixed \\(q-r\\), but the existence problem within a chart is still not automatically a fixed-variable real-feasibility problem.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



Your approach takes a different route:

- factor \\(H=XB\\);
- replace \\(F\\) by \\(G=FX\\);
- eliminate the large factor \\(B\\) through linear consistency;
- encode the spectral condition with \\(2\omega\\) auxiliary variables;
- use Cauchy–Binet to avoid the row-minor explosion.

That is a genuine complexity-oriented compression.

My positioning recommendation: describe Fernando as providing the observer-theoretic characterization and geometric parameterization; describe your contribution as a bit-complexity analysis of a prescribed-row completion problem, with parameterized algorithms that compress the feasibility test beyond the dimension of the original chart coordinates.

Do not claim that Fernando's paper proves the same fixed-\\(q\\) or fixed-\\(\kappa\_{\rm obs}\\) bounds unless the exact model equivalence and algorithmic implication have been established.

## 6.2 What the parametric-linear-system literature already covers

Corless, Giesbrecht, Rafiee Sevyeri, and Saunders, On Parametric Linear System Solving (2025), study systems linear in unknowns with polynomially parameter-dependent coefficients. Their paper gives polynomial-time methods for computing solution regimes when there are up to three symbolic parameters.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



This is related to your fixed-\\(q\\) system

\\[ M(X,G)b=c(X,G). \\]

But it is not a direct implication of their result:

1. Your number of parameters is \\(2q\omega\\), which may exceed three.
2. You need only decide whether the system is consistent at some parameter value, not compute a complete decomposition into solution regimes.
3. Your positive-semidefinite rank-consistency formula provides a direct semialgebraic description of consistency without constructing all those regimes.

The distinction is important for novelty. Your method does not need to solve the entire parametric linear-system problem. It eliminates the linear variables using the special rank identity

\\[ \operatorname{rank}(MM^{\mathsf T}) = \operatorname{rank}(MM^{\mathsf T}+cc^{\mathsf T}). \\]

That is the natural tailored tool for q1.

## 6.3 The real-algebraic complexity references

For the final decision step, cite Renegar's three-part work on the computational complexity and geometry of the first-order theory of the reals, particularly the existential decision bounds. These are standard sources for singly-exponential real-algebraic decision procedures.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车+2



The precise statement you need is that a rational existential-real formula with \\(m\\) variables, \\(s\\) polynomials, maximum degree \\(D\\), and coefficient bit length \\(\tau\\) has a deterministic decision algorithm with a bound of schematic form

\\[ (sD)^{O(m)}\tau^{O(1)}, \\]

up to the convention used for dense versus sparse polynomial encoding.

For fixed \\(q\\), \\(m=O(q^2)\\), while \\(s,D\\) are polynomial in the input dimensions. This gives a polynomial algorithm for every fixed \\(q\\).

For fixed \\(\kappa\_{\rm obs}\\), \\(m,s,D\\) are all functions of \\(\kappa\_{\rm obs}\\), giving the FPT bound.

This is the right place to invoke real algebraic geometry—not as a substitute for proving that the polynomial formula has bounded size, but after that size analysis has been completed.

# 7. Question 6: the concrete research roadmap

I would divide the project into three phases, with one primary deliverable and two secondary investigations.

## Phase A — finish and secure the algorithmic paper

Highest priority

The most important task is to turn the FPT skeleton into a fully formal theorem.

I would organize the proof around six lemmas:

| Lemma                  | Required conclusion                                                                                                                 |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Compression lemma      | Every free row pair is parametrized by \\(d_0\\) coordinates, with exactly \\(\kappa\_{\rm obs}=rd_0\\) total variables             |
| Gram-rank lemma        | Equivalence of (5a) and the two elementary-symmetric-polynomial conditions                                                          |
| Bezout lemma           | No common complex root gives real multipliers of degree \\(<\omega\\)                                                               |
| Gram-certificate lemma | (5b) is equivalent to \\(B^{\mathsf T}Bx=e_0\\)                                                                                     |
| Cauchy–Binet lemma     | The Gram certificate can be constructed without enumerating row subsets                                                             |
| Bit-complexity lemma   | All rational preprocessing and polynomial construction fit \\(f(\kappa\_{\rm obs})\operatorname{poly}(\mathcal L)\\) bit operations |

After that, formalize the \\(r=0\\), \\(k=0\\), and \\(\omega=0\\) cases.

The fixed-\\(q\\) algorithm should be included as a second theorem. Use

\\[ G=FX,\qquad H_A=GB, \\]

and the rank-consistency elimination to avoid quantifying over the \\(O(qk)\\) entries of \\(B\\).

I would also make the q1 membership-in-\\(\exists\mathbb R\\) proof explicit using the polynomial left-inverse identity. That puts all three results in one framework.

## Phase B — one controlled hardness experiment

Secondary priority

Do not restart the old local multiplication search. Instead:

1. Read and verify the ARM(3) composition and gauge arguments.
2. Identify exactly which affine constraints in ARM couple different matrix rows.
3. Ask whether these can be implemented by the q1 row-pair space \\(\mathcal T\\).
4. Try to use fixed rows as a gauge block.
5. Determine whether (5b) can be made automatic using a shift scaffold without giving extra free rows a bypass.

The first milestone should not be a complete reduction. It should be a small, explicit translation lemma:

> Can a fixed-rank global affine matrix-completion instance be represented by a q1 compressed row-pair system, with all affine constraints preserved and no extra feasible completions?

If this fails for the obvious embedding, record which affine interactions cannot be represented through a common \\(\mathcal T\\). That information may suggest a different source problem.

## Phase C — parameterized lower bounds

This should be a later project, after the main FPT theorem is stable.

The natural question is W[1]-hardness in \\(q\\), not in \\(\kappa\_{\rm obs}\\).

A possible reduction source is Multicolored Clique. The goal would be a mapping in which the observer order depends on the clique parameter, but the row-pair dimension grows with the graph input. Such a reduction would be compatible with FPT in \\(\kappa\_{\rm obs}\\).

If successful, the result would provide a meaningful parameterized classification:

\\[ \boxed{ q1\in\mathrm{XP}(q),\quad q1\text{ is W[1]-hard parameterized by }q,\quad q1\in\mathrm{FPT}(\kappa\_{\rm obs}). } \\]

This is a worthwhile possible destination, but I would not make it a requirement for the first algorithmic paper.

# 8. Final recommendation: which outcome should the project target?

I would distinguish the result that is most likely to be publishable soon from the result that would settle unrestricted q1.

## Recommended priorities

(a) Finish the algorithmic paper

First

This has the strongest proof architecture. The fixed-\\(\kappa\_{\rm obs}\\) FPT theorem should be the main result, with fixed-\\(q\\) polynomial time as a complementary theorem.

(b) Attempt global hardness

Second

Use ARM(3) as the first source to investigate. The gauge and global-composition strategy addresses the exact soundness weakness of the previous gate programme.

(c) Parameterized hardness

Third

Investigate W[1]-hardness in \\(q\\), not in \\(\kappa\_{\rm obs}\\). This could give a meaningful parameterized classification.

(d) General no-go for multiplication

Deprioritize

The existing obstructions apply to specific architectures. A general no-go would be difficult, and even a no-go for multiplication gadgets would not rule out hardness through a different global encoding.

## 8.1 What I would claim in the first paper

I would aim for the following theorem package:

Theorem 1 — Existential-real membership.

\\[ q1\in\exists\mathbb R. \\]

Theorem 2 — Fixed observer order. For each fixed \\(q\\), q1 is decidable in polynomial time, with the proposed bound

\\[ T_A(\mathcal I)=\mathcal L^{O(q^2)}. \\]

Theorem 3 — Fixed effective free-row dimension.

\\[ T_B(\mathcal I) =f(\kappa\_{\rm obs})\mathcal L^{O(1)}. \\]

Theorem 4 — Combined parameterized upper bound.

\\[ \boxed{ T(\mathcal I)\le \min\left\\{ \mathcal L^{O(q^2)}, f(\kappa\_{\rm obs})\mathcal L^{O(1)} \right\\}. } \\]

The first theorem supplies the unrestricted real-algebraic classification upper bound. The other two reveal two distinct sources of tractability.

I would not put an unrestricted hardness claim in this paper unless a sound reduction is actually completed.

## 8.2 What would count as a real breakthrough on unrestricted q1?

There are two especially valuable possibilities.

Breakthrough A: an ARM-to-q1 reduction. This would potentially establish \\(\exists\mathbb R\\)-hardness, and together with membership prove completeness. It would require a full global soundness argument, not just local gate realizations.

Breakthrough B: a uniform algorithm. If the Gram certificates can be combined with additional polynomial-matrix structure to remove the \\(q\\)-dependent exponent and the parameter dependence on \\(\kappa\_{\rm obs}\\), then unrestricted polynomial time might become possible. There is currently no such argument.

I would set one intermediate milestone before either: prove a sharper structural theorem about the feasible global row-space pairs

\\[ (W,\mathcal T) \\]

and their associated pencils. Such a theorem could guide both the algorithmic and hardness routes.

# 9. Final reliability summary

| Part of the project                                  | Current conclusion                                                                         |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Functional-observer rank and pencil characterization | Established in the observer-theory literature; cite Fernando                               |
| q1 existential-real membership                       | Has a direct polynomial-size left-inverse certificate                                      |
| Fixed-\\(q\\) polynomial algorithm                   | Strong, credible proof route; requires formal coefficient-construction and bit analysis    |
| Fixed-\\(\kappa\_{\rm obs}\\) FPT algorithm          | Strongest algorithmic result; Gram–Bezout–Cauchy–Binet argument is mathematically coherent |
| Exact script checks                                  | Useful finite verification; not independent general proofs                                 |
| Sound multiplication                                 | Not established                                                                            |
| General multiplication no-go                         | Not established                                                                            |
| ARM-based hardness                                   | Promising research direction; no q1 reduction yet                                          |
| W[1]-hardness in \\(q\\)                             | Plausible lower-bound project                                                              |
| W[1]-hardness in \\(\kappa\_{\rm obs}\\)             | Incompatible with the FPT claim unless FPT=W[1]                                            |
| Unrestricted q1 complexity                           | Open                                                                                       |

One qualification is important for publication: the two algorithmic results should be described as proof candidates supported by the supplied identities and verification record, until the rational coefficient-height estimates and the complete formal reductions have been written and independently checked. The previous exact scripts are not available here for reproduction, so I would retain their E labels rather than describe them as independently rerun.

## 10. My bottom line

The project has reached a point where the algorithmic contribution no longer depends on solving the multiplication-wiring problem.

That is the strategic advantage. You have a potentially strong result even if q1's unrestricted complexity remains unresolved.

I would proceed in this order:

1. Finish and formalize the FPT theorem.
2. Complete the fixed-\\(q\\) algorithm using the \\(G=FX\\) simplification.
3. Write the precise comparison with Fernando's 2026 fixed-order characterization.
4. Investigate one global ARM(3)-to-q1 reduction.
5. Only then decide whether to pursue W[1]-hardness in \\(q\\) or further structural algorithms.

The most plausible immediate research outcome is a two-parameter algorithmic classification, not a resolution of unrestricted q1. But that classification is meaningful in its own right. It is also compatible with either eventual \\(\exists\mathbb R\\)-completeness or a stronger polynomial-time algorithm.

The central mathematical insight worth building the paper around is:

\\[ \boxed{ \text{q1's effective nonlinear freedom is concentrated in } \kappa\_{\rm obs}=r\\,\operatorname{rank}[N\ AN], } \\]

while the observer order \\(q\\) controls a separate low-dimensional factorization in the fixed-order algorithm.

That separation—not the individual rank identities—is the strongest organizing principle for the project.

### Key references

1. T. Fernando, [Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger](https://arxiv.org/abs/2609.37992?utm_source=chatgpt.com), 2026.&#x20;

   [image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

   arXiv

2. R. M. Corless, M. Giesbrecht, L. Rafiee Sevyeri, B. D. Saunders, [On Parametric Linear System Solving](https://arxiv.org/abs/2508.21629?utm_source=chatgpt.com), 2025.&#x20;

   [image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

   arXiv

3. J. Renegar, On the Computational Complexity and Geometry of the First-Order Theory of the Reals, Parts I–III, Journal of Symbolic Computation 13 (1992).&#x20;

   [image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

   科学直通车+2

4. A. Majumdar, [Affine Rank Minimization is ER-Complete](https://arxiv.org/abs/2602.14037?utm_source=chatgpt.com), 2026 preprint.&#x20;

   [image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

   arXiv

5. E. J. Kim, A. de Mesmay, T. Miltzow, [Representing Matroids over the Reals is \\(\exists\mathbb R\\)-complete](https://dmtcs.episciences.org/en/articles/13924?utm_source=chatgpt.com), DMTCS 26 (2024).&#x20;

   [image](https://www.google.com/s2/favicons?domain=https://dmtcs.episciences.org\&sz=32)

   dmtcs.episciences.org
