# Research audit of `106_layer_table.md`

## 1. Overall assessment

The report makes a useful attempt to consolidate the compressed-observer analysis into a layer-by-layer classification. Its strongest contributions are the clean formulation of the layer decomposition, the compatibility-Grassmannian description, and the recognition that the middle-layer problem must be analysed through the admissible compressed pairs rather than through unconstrained random rows.

However, **the central conclusion of the report is not currently valid**:

> Every layer is either polynomial-time decidable or infeasible.

There is a concrete rational counterexample to the claim that all non-characteristic middle layers are infeasible. It also exposes an error in the top-layer discussion: the report treats rank completion as automatic when there is at least one free row, but one free row cannot generally complete a row space of dimension \\(k>1\\).

These are not merely missing proof details. They affect the proposed layer table and the conclusion that the original decision problem is polynomial-time decidable. In fact, the counterexample below gives a feasible non-characteristic middle layer.

My recommendation is therefore to **revise the layer table before pursuing the five questions in Part III**. The immediate priority should be to replace the claimed universal middle-layer obstruction with a correct characterization of the restricted pencil.

---

## 2. A concrete counterexample to the middle-layer impossibility claim

The most important claim to check is Part II.1(c), which says that if

\\[ K_0\cap\ker(\lambda I-A)=\\{0\\} \qquad\text{for every }\lambda\in\mathbb C, \\]

then every middle layer is infeasible. The report attributes this to a quadratic determinant obstruction.

That statement is false under the setup in Part I.

### 2.1 Construct a rational instance

Take \\(n=6\\), \\(p=2\\), and define

\\[ A= \begin{pmatrix} 0&0&0&0&0&0\\\ 0&0&0&0&0&0\\\ 1&0&0&0&0&0\\\ 0&1&0&0&0&0\\\ 0&0&1&0&0&0\\\ 0&0&0&1&0&0 \end{pmatrix}, \qquad C= \begin{pmatrix} 0&0&0&0&1&0\\\ 0&0&0&0&0&1 \end{pmatrix}. \\]

Let

\\[ N= \begin{pmatrix} 1&0\\\ 0&1\\\ 0&0\\\ 0&0\\\ 0&0\\\ 0&0 \end{pmatrix} =[e_1\ e_2]. \\]

We have

\\[ AN=[e_3\ e_4]. \\]

Moreover,

\\[ C= \begin{pmatrix}e_5^\top\\\e_6^\top\end{pmatrix}, \qquad CA= \begin{pmatrix}e_3^\top\\\e_4^\top\end{pmatrix}. \\]

Consequently,

\\[ K_0=\ker\begin{bmatrix}C\\\CA\end{bmatrix} =\operatorname{span}\\{e_1,e_2\\}, \\]

and \\(N\\) is indeed a basis matrix of \\(K_0\\). Thus \\(k=2\\).

### 2.2 The instance is non-characteristic

For \\(x=x_1e_1+x_2e_2\in K_0\\),

\\[ Ax=x_1e_3+x_2e_4. \\]

If

\\[ (\lambda I-A)x=0, \\]

then

\\[ \lambda x_1e_1+\lambda x_2e_2-x_1e_3-x_2e_4=0. \\]

Since \\(e_1,e_2,e_3,e_4\\) are linearly independent, this forces

\\[ x_1=x_2=0. \\]

Therefore

\\[ \boxed{ K_0\cap\ker(\lambda I-A)=\\{0\\} \quad\text{for every }\lambda\in\mathbb C. } \\]

The instance satisfies exactly the non-characteristic hypothesis used in Part II.1(c).

### 2.3 Construct a feasible middle-layer witness

Set

\\[ L_0=0,\qquad m=2, \\]

and choose

\\[ R= \begin{pmatrix} e_1^\top\\\ e_3^\top \end{pmatrix}. \\]

Then

\\[ H=RN = \begin{pmatrix} 1&0\\\ 0&0 \end{pmatrix}, \\]

while

\\[ H_A=RAN = \begin{pmatrix} 0&0\\\ 1&0 \end{pmatrix}. \\]

Hence

\\[ \operatorname{rank}H=1, \qquad \operatorname{row}H =\operatorname{row}H_A =\operatorname{span}\\{(1,0)\\}. \\]

In particular,

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H. \\]

The pencil is

\\[ \lambda H-H_A = \begin{pmatrix} \lambda&0\\\ -1&0 \end{pmatrix}. \\]

For every \\(\lambda\in\mathbb C\\), this matrix has rank exactly one:

\\[ \operatorname{rank}(\lambda H-H_A)=1=\omega. \\]

Thus both conditions (5a) and (5b) hold.

(Counterexample) **The layer \\(\omega=1\\), with \\(0<\omega\<k=2\\), is feasible even though the instance is non-characteristic.**

All matrices and the witness are rational.

### 2.4 Why this counterexample matters

This directly contradicts the report's claim that all non-characteristic middle layers are infeasible. It also shows why the proposed quadratic-determinant argument needs to be revisited.

The essential point is that the compressed pencil need not be a square pencil on all of \\(K_0\\). It acts on the selected row space \\(W\\), and its admissible rows are constrained by

\\[ \mathcal T_W=\mathcal S\cap(W\oplus W). \\]

In this example,

\\[ \mathcal S=\operatorname{row}[N\ AN] =\mathbb Q^{1\times 4}, \\]

so for every \\(W\leq\mathbb Q^{1\times 2}\\),

\\[ \mathcal T_W=W\oplus W. \\]

The admissible pairs can therefore include both

\\[ (w,0)\quad\text{and}\quad(0,w), \\]

where \\(w\\) spans \\(W\\). These two pairs produce the pencil rows

\\[ \lambda w,\qquad -w, \\]

which cannot vanish simultaneously at any complex \\(\lambda\\).

This is precisely the structure that defeats the claimed obstruction.

**Project implication:** the assertion that non-characteristic middle layers are always infeasible must be withdrawn. It cannot be used as the foundation of a polynomial-time classification.

---

## 3. The top-layer analysis has a rank-completion error

Part II.1(b) states that for \\(\omega=k\\), compatibility and rank completion are automatic as soon as \\(m\geq1\\).

The compatibility statement is correct, but the rank-completion statement is not.

### 3.1 What is actually automatic

When \\(\omega=k\\), the only possible row space is

\\[ W=V=\mathbb F^{1\times k}. \\]

Consequently,

\\[ \mathcal T_V=\mathcal S. \\]

Because \\(N\\) has full column rank,

\\[ \pi_1(\mathcal S) =\operatorname{row}N =\mathbb F^{1\times k}. \\]

This means that **the set of possible first compressed components spans all of \\(V\\)**.

It does not mean that one free row can generate all of \\(V\\).

The actual rank-completion condition is

\\[ \operatorname{span}\left( \\{h_i^0\\}\_{i=1}^{r_0} \cup \\{x_1,\ldots,x_m\\} \right)=V, \\]

where each \\(x_j\\) is the first component of an admissible free-row pair.

Let

\\[ \rho_0=\operatorname{rank}(L_0N). \\]

Since each free row adds at most one dimension, a necessary condition is

\\[ \boxed{m\geq k-\rho_0.} \\]

In the top layer, this is also sufficient for rank completion alone, because \\(\pi_1(\mathcal S)=V\\) allows the free rows to supply any desired additional independent first components.

Thus the correct rank-completion statement is

\\[ \boxed{ \text{Top-layer rank completion is possible} \iff m\geq k-\operatorname{rank}(L_0N). } \\]

This is a much more precise statement than \\(m\geq1\\).

### 3.2 Consequence for the claimed top-layer criterion

The report claims that, for \\(r\geq k+1\\),

\\[ \text{top layer feasible} \iff K_0\cap\ker(\lambda I-A)=\\{0\\} \quad\forall\lambda\in\mathbb C. \\]

It then concludes that the criterion is independent of \\(L_0\\).

But \\(r\geq k+1\\) only gives

\\[ r_0+m\geq k+1. \\]

It does not guarantee that the fixed rows and free rows can generate a \\(k\\)-dimensional row space.

For example, use the rational instance constructed in Section 2, but now set

\\[ r_0=2,\qquad L_0=0,\qquad m=1. \\]

Then

\\[ r=r_0+m=3=k+1. \\]

The non-characteristic condition still holds. Nevertheless,

\\[ \operatorname{rank}\begin{bmatrix}L_0N\\\RN\end{bmatrix} =\operatorname{rank}(RN)\leq1<2 \\]

for every single free row \\(R\\).

The top layer \\(\omega=2\\) is therefore impossible, despite satisfying the proposed right-hand-side criterion and the stated row-count bound.

This is a direct counterexample to the boxed equivalence as stated.

### 3.3 How to repair the top-layer theorem

I recommend separating the result into two propositions.

**Proposition A — rank completion.**

For \\(W=V\\), rank completion is possible if and only if

\\[ m\geq k-\operatorname{rank}(L_0N). \\]

**Proposition B — spectral regularity conditional on rank completion.**

Assume rank completion is possible. Determine whether the non-characteristic condition

\\[ K_0\cap\ker(\lambda I-A)=\\{0\\} \quad\forall\lambda\in\mathbb C \\]

is sufficient for the existence of a choice of free rows making the pencil full column rank at every \\(\lambda\\).

The second proposition is a separate question. Its proof must account for the number of free rows, the fixed pencil rows, and the fact that the same free rows must work for all \\(\lambda\\).

In particular, the current argument should not silently replace the fixed-row-plus-free-row problem by a generic selection from the entire space \\(\mathcal S\\).

---

## 4. The \\(\omega=0\\) criterion needs clarification

The report says that the zero layer is feasible exactly when

\\[ L_0[N\ AN]=0 \quad\text{and}\quad n>\dim\mathcal S. \\]

The first condition is correct. The second condition does not follow from the witness definition stated in Part I.

If the only requirements on \\(R\\) are those in (5a) and (5b), then choosing

\\[ R=0 \\]

gives

\\[ H=H_A=0. \\]

Both conditions hold automatically whenever the fixed rows also annihilate \\(N\\) and \\(AN\\).

There is no need for

\\[ n>\dim\mathcal S \\]

under this interpretation.

That dimension condition might be relevant if the original problem additionally requires one or more of the following:

- \\(R\\) must contain a nonzero row;
- the rows of \\(\mathcal L=[L_0;R]\\) must be linearly independent;
- the complete matrix \\(\mathcal L\\) must have prescribed row rank;
- the free rows must be selected from a specified complement of a subspace.

But none of these requirements appears in the witness definition quoted in this report.

**Recommendation:** explicitly state the admissible-witness constraints before presenting the zero-layer criterion. If there is a full-row-rank requirement on \\(\mathcal L\\), derive the exact dimension condition, including the interaction with the row space of \\(L_0\\). If there is no such requirement, remove \\(n>\dim\mathcal S\\).

This matters because the zero layer can make the entire decision problem trivially feasible in instances where \\(L_0\\) annihilates \\([N\ AN]\\).

---

## 5. The characteristic middle-layer experiments do not yet support a general theorem

Part II.1(d) studies the special family

\\[ K_0=\operatorname{span}\\{e_1,\ldots,e_k\\}, \qquad C=[0\mid I_k], \qquad A=\operatorname{blockdiag}(B,D), \\]

and reports three infeasible examples for \\(\omega=k-1\\).

These computations are useful evidence about that particular family, but they do not establish universal middle-layer infeasibility.

There are two separate issues.

### 5.1 The restriction \\(K_0\\) invariant under \\(A\\) is substantial

In this family, \\(K_0\\) is \\(A\\)-invariant, and \\(A|\_{K_0}=B\\) is well-defined.

For a general instance, however,

\\[ K_0=\ker[C;CA] \\]

need not be \\(A\\)-invariant. Therefore \\(A|\_{K_0}\\) is not generally an operator from \\(K_0\\) to itself, and

\\[ \operatorname{spec}(A|\_{K_0}) \\]

is not generally defined.

The expression

\\[ K_0\cap\ker(\lambda I-A) \\]

is always meaningful, but it records only eigenvectors of \\(A\\) that lie in \\(K_0\\). It is not the spectrum of a generally defined restriction.

This distinction is important for Q1. A proposed common factor arising from the spectrum of \\(A|\_{K_0}\\) can only be stated under an invariance assumption or replaced by a more general construction.

### 5.2 The drop condition is not a complete description of the pencil

The rank bound

\\[ \operatorname{rank}P(\lambda) \leq \operatorname{rank}((\lambda I-A)N) \\]

is a valid necessary condition. But the counterexample in Section 2 shows that when the right-hand side is full column rank, a middle-layer pencil can nevertheless be regular.

More generally, the relevant question is not merely whether \\((\lambda I-A)N\\) loses rank. It is whether the restricted pair space

\\[ \mathcal T_W=\mathcal S\cap(W\oplus W) \\]

contains enough pairs to produce a pencil whose maximal minors have gcd one.

The characteristic examples should therefore be studied through \\(\mathcal T_W\\), not just through the eigenvalue multiplicities of \\(B\\).

### 5.3 A better interpretation of the three computations

The three computations support the following limited conclusion:

> In the tested block-diagonal invariant-subspace family, for the tested dimensions and row configurations, the generic admissible pencil has a nonconstant common factor.

They do not establish that:

- every characteristic middle layer is infeasible;
- every middle layer has a factor from the eigenvalues of \\(B\\);
- the fixed rows are unable to repair the rank defect;
- increasing \\(r_0\\) cannot change the outcome.

The report is appropriately cautious in its reliability table, but the main text should preserve that caution more consistently.

---

## 6. Reassessment of the five questions

### Q1. Does every middle-layer gcd contain a factor from the spectrum of \\(A|\_{K_0}\\)?

**No general theorem of this form can hold under the stated assumptions.**

The non-characteristic counterexample already shows why a universal spectral-factor obstruction is implausible: the pencil has a \\(1\times1\\) nonzero maximal minor equal to \\(\lambda\\) and another equal to \\(-1\\), so

\\[ \gcd(\lambda,-1)=1. \\]

There is no nonconstant common factor.

For characteristic instances, a factor may indeed arise from a particular invariant-subspace structure. But the factor must be derived from the geometry of the admissible pair space.

A more promising formulation is:

Let \\(W\\) be a compatible \\(\omega\\)-dimensional subspace and let

\\[ \mathcal T_W=\mathcal S\cap(W\oplus W). \\]

Define the evaluation map

\\[ E\_\lambda:\mathcal T_W\longrightarrow W, \qquad (x,y)\longmapsto\lambda x-y. \\]

Then ask:

1. For which \\(\lambda\\) is \\(E\_\lambda\\) surjective?
2. If \\(E\_\lambda\\) is not surjective, is that failure forced by an eigenvector in \\(K_0\\)?
3. If \\(E\_\lambda\\) is surjective for every \\(\lambda\\), can sufficiently many admissible rows be chosen so that the resulting pencil is regular?

This formulation is more directly connected to the gcd condition.

It also avoids treating \\(A|\_{K_0}\\) as an operator when \\(K_0\\) is not invariant.

### Q2. Is the top-layer criterion independent of \\(L_0\\)?

**Not as currently stated.**

The top layer has automatic compatibility, but not automatic rank completion. The rank-completion threshold depends explicitly on

\\[ \operatorname{rank}(L_0N). \\]

Even after correcting that threshold, the spectral part needs a separate theorem. It is possible that a sufficiently large free-row budget makes the spectral-existence criterion independent of the particular fixed rows, because additional rows can only increase the row rank of the pencil. But that would require a proof under a precise bound on \\(m\\), not the present argument.

A suitable research question is:

> For fixed \\(A,C,N\\), what is the smallest \\(m\\) such that, for every compatible fixed matrix \\(L_0\\) of a specified rank, a regular top-layer pencil can be completed by \\(m\\) free rows whenever the non-characteristic condition holds?

This would give a meaningful quantitative version of the proposed top-layer result.

### Q3. Does the full decision problem depend on \\(L_0\\) only through the zero layer?

The current report does not establish this, and the top-layer rank-completion issue shows that the claim needs more care.

For a middle layer, the fixed pairs

\\[ (h_i^0,g_i^0) \\]

must lie in \\(W\oplus W\\), and they also contribute to the rank and spectral properties of the pencil. Thus \\(L_0\\) enters through more than just the zero layer at the level of the layer-feasibility tests.

It remains possible that some global existential theorem makes the final disjunction independent of \\(L_0\\) under additional assumptions. But that would need to be proved across all layers.

I recommend not making this a project-level conjecture yet. First establish the corrected individual-layer conditions.

### Q4. Can additional fixed rows repair the characteristic middle-layer examples?

This is a good question, but it should be formulated as a rank-completion and spectral-completion problem rather than simply as “adding more fixed rows.”

For a given \\(W\\), let the fixed compressed pencil be

\\[ P_0(\lambda)=\lambda H_0-H\_{A,0}. \\]

Let the admissible free-row pairs be

\\[ (x_j,y_j)\in\mathcal T_W, \\]

giving

\\[ P(\lambda)= \begin{bmatrix} P_0(\lambda)\\\ \lambda x_1-y_1\\\ \vdots\\\ \lambda x_m-y_m \end{bmatrix}. \\]

The question is whether there exist admissible pairs such that

\\[ \operatorname{rank}P(\lambda)=\omega \quad\forall\lambda\in\mathbb C. \\]

There are two possible mechanisms for failure:

- At some \\(\lambda_0\\), even the full evaluation space generated by fixed and admissible rows has rank less than \\(\omega\\). Then no completion is possible.
- The evaluation space has full rank at every individual \\(\lambda\\), but no finite selection of admissible pairs produces one pencil that has full rank simultaneously at all \\(\lambda\\).

These mechanisms should be distinguished. The second is a genuinely global pencil problem and cannot be settled by checking only pointwise ranks.

A useful first experiment is to hold the block-diagonal \\(B,D\\) family fixed, vary \\(r_0\\), and calculate the generic gcd over the exact parameter field. This will show whether the observed common factors are caused by the pair-space restriction or by the particular fixed rows.

### Q5. What would a hardness witness need to look like?

The report's earlier corrections are valuable: failure of a particular witness-filtering strategy does not establish the impossibility of a many-one reduction.

However, the current layer table does not yet justify the claim that hardness must come from making \\(N\\) part of the input in a special way.

There are at least three possible sources of complexity:

1. **Choice of \\(W\\):** the search over compatible subspaces in a Grassmannian.
2. **Restricted pair-space geometry:** the way \\(\mathcal T_W\\) changes with \\(W\\).
3. **Generic-pencil regularity:** the algebraic condition that the maximal minors have gcd one.

The counterexample demonstrates that even the non-characteristic middle-layer regime can support regular pencils. Thus the middle layers cannot be discarded as a source of complexity.

For a reduction, the source instance might be encoded in the geometry of \\(\mathcal T_W\\), or in the way the maximal-minor gcd varies with \\(W\\). It need not be encoded by forcing individual free-row coordinates to take discrete values.

I would therefore keep the hardness programme open, but suspend any reduction design that depends on the current layer table.

---

## 7. A corrected layer table

The report should not currently present its existing table as a classification theorem. A more accurate version is:

| Layer                                 | What is established                                                                               | What remains                                                                                   |
| ------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| \\(\omega=0\\)                        | The fixed rows must annihilate \\(N\\) and \\(AN\\); with unrestricted \\(R\\), choose \\(R=0\\). | Clarify any additional row-rank or nonzero-row requirement.                                    |
| \\(0<\omega\<k\\), non-characteristic | The report's universal infeasibility claim is false; a rational feasible example exists.          | Characterize feasibility using \\(\mathcal T_W\\) and its evaluation maps.                     |
| \\(0<\omega\<k\\), characteristic     | Three programmed examples are infeasible.                                                         | No general theorem; investigate fixed-row and pair-space effects.                              |
| \\(\omega=k\\)                        | \\(W=V\\), compatibility is automatic, and \\(\pi_1(\mathcal S)=V\\).                             | Rank completion depends on \\(L_0N\\) and \\(m\\); spectral completion needs a separate proof. |

The corrected top-layer rank-completion criterion is

\\[ m\geq k-\operatorname{rank}(L_0N). \\]

The corrected middle-layer conclusion is simply that the existing examples do not establish universal infeasibility.

---

## 8. Recommended next steps for the project

I would reorganize the next phase of work around four concrete tasks.

### Task 1 — Correct the foundational statements

Before any new experiments, revise the report to:

- remove the universal non-characteristic middle-layer obstruction;
- correct the top-layer rank-completion condition;
- clarify the zero-layer witness requirements;
- distinguish the spectrum of \\(A\\) restricted to an invariant \\(K_0\\) from eigenvalues whose eigenvectors happen to lie in \\(K_0\\).

These are necessary corrections, not optional refinements.

### Task 2 — Establish an exact evaluation-map criterion

For each compatible \\(W\\), define

\\[ E\_\lambda:\mathcal T_W\to W, \qquad E\_\lambda(x,y)=\lambda x-y. \\]

A necessary condition for a regular pencil is

\\[ \operatorname{span}\left( \\{\lambda h_i^0-g_i^0\\}\_{i=1}^{r_0} \cup E\_\lambda(\mathcal T_W) \right)=W \quad\forall\lambda\in\mathbb C. \\]

This is the pointwise obstruction test. It is not, by itself, sufficient for a single finite collection of free rows to work for every \\(\lambda\\). The next theorem should identify conditions under which it becomes sufficient when enough free rows are available.

This is likely the most productive mathematical formulation for the middle-layer problem.

### Task 3 — Build a small exact-computation suite

Use the counterexample above as a mandatory regression test. Then study:

- \\(k=2,\omega=1\\), where the maximal minors are linear in \\(\lambda\\);
- \\(k=3,\omega=1\\) and \\(k=3,\omega=2\\);
- invariant and non-invariant \\(K_0\\);
- several values of \\(r_0\\) and \\(m\\);
- fixed rows equal to zero, rank-deficient, and rank-completing.

For every instance, record:

1. \\(K_0\\), \\(N\\), and \\(\mathcal S\\);
2. compatible \\(W\\);
3. \\(\mathcal T_W\\);
4. the dimension of the evaluation image \\(E\_\lambda(\mathcal T_W)\\);
5. the generic maximal-minor gcd;
6. whether an explicit rational witness exists.

Do not use random sampling alone to establish generic gcd statements. Use exact rational parameterization and symbolic subresultants or elimination.

### Task 4 — Reassess complexity only after the corrected geometry is understood

Once the middle-layer feasibility problem is characterized, revisit the complexity question.

The most promising potential source of hardness is no longer simply “a choice of active subspace” or “a Boolean gadget.” It is the interaction between:

\\[ W,\qquad \mathcal T_W,\qquad E\_\lambda,\qquad \gcd(\text{maximal minors}). \\]

The key question is whether the existential choice of \\(W\\) can encode a difficult combinatorial selection problem through these objects.

There is no basis yet for claiming polynomial-time decidability, but there is also no established hardness reduction. The correct position is that the complexity of the general problem remains open.

---

## 9. A useful theorem to target next

I recommend making the following the next formal target.

**Proposed theorem — Pointwise evaluation obstruction and generic completion.**

Fix a compatible \\(W\\) and let

\\[ \mathcal P_W=\mathcal T_W^m \\]

be the space of admissible free-row choices. Define

\\[ \mathcal E\_\lambda = \operatorname{span}\left( \\{\lambda h_i^0-g_i^0\\}\_{i=1}^{r_0} \cup E\_\lambda(\mathcal T_W) \right) \leq W. \\]

Then:

1. If \\(\mathcal E\_{\lambda_0}\ne W\\) for some \\(\lambda_0\in\mathbb C\\), no admissible free-row choice can give a regular pencil.
2. If \\(\mathcal E\_\lambda=W\\) for every \\(\lambda\in\mathbb C\\), determine an explicit bound on \\(m\\) that guarantees the existence of a regular pencil.
3. Determine whether the bound can be improved when the fixed rows already contribute a subspace of positive dimension.
4. Determine whether the resulting regular choices form a nonempty Zariski-open subset of \\(\mathcal P_W\\).

Part 1 is immediate. Parts 2–4 are the substantial research questions.

The distinction between pointwise surjectivity and simultaneous regularity is especially important: a different choice of admissible rows at every \\(\lambda\\) is not the same thing as one fixed choice of rows that works for all \\(\lambda\\).

---

## 10. Final recommendation

(Major revision required)

The report is a useful research note, but its headline conclusion should be withdrawn. The non-characteristic middle-layer claim has an explicit rational counterexample, and the top-layer argument overlooks the number of free rows required for rank completion.

The good news is that the counterexample gives the project a much clearer direction. It shows that the middle-layer geometry is not vacuous and that the correct object is the evaluation map

\\[ E\_\lambda:\mathcal T_W\to W. \\]

**My strongest recommendation is to make the next report about the exact evaluation-map criterion and simultaneous generic completion, using the \\(n=6,k=2,\omega=1\\) counterexample above as the first test case.** This is a more productive next step than trying to rescue the current universal-infeasibility theorem or immediately constructing another hardness gadget.

The complexity question should remain open until that structural analysis is complete.