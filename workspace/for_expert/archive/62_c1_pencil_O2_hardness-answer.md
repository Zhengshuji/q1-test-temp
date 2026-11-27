# Assessment of Report 62: the \\(c=1\\) pencil criterion, the \\(O_2\\) reduction, and unbounded-\\(c\\) hardness

Report 62 makes an important advance: it isolates the spectral obstruction in the \\(c=1\\) case as an eigenvector-intersection problem, rather than a generalized-eigenvector or polynomial-gcd problem. That reduction is useful, but one of the report's stated consequences is incorrect: \\(B\_\*\ne0\\) and diagonalizability of \\(A\_\*\\) do not imply that the pencil is good.

The correct criterion is simple and complete:

\\[ \boxed{ \operatorname{rank}P(\lambda)=\omega\quad\forall\lambda\in\mathbb C \iff \ker(A\_\*-\lambda I)\cap\ker B\_\*=\\{0\\} \quad\forall\lambda\in\mathbb C. } \\]

This holds whether or not \\(A\_\*\\) is diagonalizable. Generalized eigenvector chains cannot create a rank drop that is not already witnessed by an ordinary eigenvector.

The \\(O_2\\) split is a promising way to organise the continuous \\(c=1\\) family, but its open-set argument needs a sharper distinction between openness of the good locus in the joint parameter space and existence of a feasible lift over a given \\(v\\). Finally, for \\(q1\\), I recommend treating unbounded-\\(c\\) hardness as a separate workstream, while finishing the fixed-\\(c\\) theory as a structural and algorithmic foundation. I address each issue below.

## 1. O1: the pencil criterion is complete, but the diagonalizable consequence must be corrected

The report writes, after identifying

\\[ \mathbb C^q=W\oplus W',\qquad W=\operatorname{im}H, \\]

that

\\[ Z:W\to\mathbb C^q,\qquad Z=\begin{bmatrix}A\_\*\\\B\_\*\end{bmatrix}, \\]

and

\\[ P(\lambda) = \begin{bmatrix} (\lambda I-A\_\*)H\\\ -B\_\*H \end{bmatrix}. \\]

Here \\(A\_\*:W\to W\\), while \\(B\_\*:W\to W'\\). Since \\(H\\) is surjective onto \\(W\\), we have

\\[ \operatorname{rank}P(\lambda) = \operatorname{rank} \begin{bmatrix} \lambda I-A\_\*\\\ -B\_\* \end{bmatrix}. \\]

The right-hand matrix has domain \\(W\\). It has rank less than \\(\omega=\dim W\\) exactly when its kernel is nonzero. Hence

\\[ \begin{aligned} \operatorname{rank}P(\lambda)<\omega &\iff \exists\\,0\ne y\in W: (\lambda I-A\_\*)y=0,\ B\_\*y=0\\\ &\iff \ker(A\_\*-\lambda I)\cap\ker B\_\*\ne\\{0\\}. \end{aligned} \\]

This proves the boxed criterion above. It is an exact equivalence, not merely a necessary condition.

### 1.1 What follows when \\(B\_\*=0\\)?

If \\(B\_\*=0\\), then \\(Z(W)\subseteq W\\), and \\(A\_\*\\) is an endomorphism of the \\(\omega\\)-dimensional space \\(W\\). Thus

\\[ P(\lambda)=(\lambda I-A\_\*)H. \\]

Because \\(H\\) is onto \\(W\\),

\\[ \operatorname{rank}P(\lambda) =\operatorname{rank}(\lambda I-A\_\*). \\]

The characteristic polynomial of \\(A\_\*\\) has a complex root, so \\(\lambda I-A\_\*\\) is singular for some \\(\lambda\in\mathbb C\\). Therefore the pencil is bad.

So the report's \\(B\_\*=0\\) obstruction is correct.

The equivalence

\\[ B\_\*=0 \iff Z(W)\subseteq W \iff H_A\text{ has all its rows in }\operatorname{row}H \\]

is also correct, provided \\(Z\\) is defined by \\(H_A=ZH\\) on \\(W=\operatorname{im}H\\).

### 1.2 The diagonalizable claim is false

The report says:

> If \\(B\_\*\ne0\\) and \\(A\_\*\\) is diagonalizable, the eigenvectors span \\(W\\), so not all can lie in the proper subspace \\(\ker B\_\*\\); hence the pencil is good.

The conclusion does not follow. The bad-pencil criterion requires at least one eigenvector to lie in \\(\ker B\_\*\\), not all eigenvectors. The fact that \\(B\_\*\\) is nonzero only proves that not every vector in an eigenbasis is killed.

A two-dimensional counterexample is enough. Take

\\[ A\_\*= \begin{bmatrix} 0&0\\\ 0&1 \end{bmatrix}, \qquad B\_\*= \begin{bmatrix} 1&0 \end{bmatrix}. \\]

Then \\(A\_\*\\) is diagonalizable and \\(B\_\*\ne0\\), but

\\[ e_2\in\ker(A\_\*-I)\cap\ker B\_\*. \\]

Consequently, the pencil loses rank at \\(\lambda=1\\).

In fact,

\\[ \begin{bmatrix} \lambda I-A\_\*\\\B\_\* \end{bmatrix} = \begin{bmatrix} \lambda&0\\\ 0&\lambda-1\\\ 1&0 \end{bmatrix}, \\]

which has rank one at \\(\lambda=1\\).

Correction required

The correct diagonalizable statement is:

If \\(A\_\*\\) is diagonalizable, the pencil is good if and only if

\\[ \ker(A\_\*-\lambda I)\cap\ker B\_\*=\\{0\\} \\]

for every eigenvalue \\(\lambda\\) of \\(A\_\*\\).

Equivalently, for every eigenspace \\(E\_\lambda\\),

\\[ B\_\*|\_{E\_\lambda}:E\_\lambda\to W' \\]

must be injective.

It is not enough that \\(B\_\*\\) be nonzero on \\(W\\). It must be nonzero on every nonzero vector in every eigenspace, in the stronger sense of injectivity on each eigenspace.

### 1.3 Generalized eigenvector chains do not create additional bad cases

This answers Question 1 directly.

The rank-drop condition at a fixed \\(\lambda\\) is

\\[ \ker(\lambda I-A\_\*)\cap\ker B\_\*\ne\\{0\\}. \\]

The first kernel consists of ordinary eigenvectors, not generalized eigenvectors. A generalized eigenvector \\(y\\) satisfying

\\[ (A\_\*-\lambda I)^2y=0,\qquad (A\_\*-\lambda I)y\ne0 \\]

does not lie in \\(\ker(A\_\*-\lambda I)\\), so it cannot by itself witness a rank drop.

Therefore, for any \\(A\_\*\\), diagonalizable or not, it is sufficient to check the ordinary eigenspaces:

\\[ \boxed{ \text{Pencil good} \iff B\_\*|\_{\ker(A\_\*-\lambda I)} \text{ is injective for every eigenvalue }\lambda. } \\]

There are only finitely many eigenvalues. This makes the O1 test substantially simpler than the report suggests. The generalized-eigenvector branch can be removed from the decision tree.

The polynomial gcd test remains a valid independent check, and is useful as a verification routine. But once the block decomposition is available, the eigenspace-injectivity criterion gives a more direct exact test.

## 2. O2: the continuous family reduction is useful, but its finite-eigenline claim needs a hypothesis

The report defines

\\[ U=\\{v\in W_L:Av\in K_0\\}. \\]

This is indeed a linear subspace: it is the kernel of the linear map

\\[ W_L\longrightarrow \mathbb C^n/K_0,\qquad v\longmapsto Av+K_0. \\]

Therefore the decomposition

\\[ \mathbb P(W_L) = \mathbb P(U)\ \dot\cup\ \bigl(\mathbb P(W_L)\setminus\mathbb P(U)\bigr) \\]

is valid, with the understanding that \\(\mathbb P(\\{0\\})\\) is empty.

The split is mathematically natural because the two pieces have different lifting behaviour:

- On \\(\mathbb P(U)\\), \\(v\in K_0\\) and \\(Av\in K_0\\), so \\(V=\mathbb Cv\subseteq D\\). The earlier \\(c=1\\) hyperplane obstruction applies.
- Outside \\(\mathbb P(U)\\), \\(Av\notin K_0\\), so the earlier compressed argument that uses \\(Av=Nw\\) cannot be applied directly. The full row-lift variables matter.

That is a good decomposition. There are, however, three qualifications.

### 2.1 The eigenline locus need not be finite

The report says that on \\(\mathbb P(U)\\), eigenlines are finite because

\\[ \det[v,Av]=0 \\]

is a quadratic equation.

This is valid in a two-dimensional setting when the eigenline condition is represented by one nonzero homogeneous quadratic on \\(\mathbb P^1\\). But it is not a general statement for arbitrary \\(d=\dim W_L\\).

The correct eigenline set is

\\[ \mathcal E(U) = \\{[v]\in\mathbb P(U):Av\in\mathbb Cv\\} = \bigcup\_{\lambda\in\sigma(A)} \mathbb P\bigl(U\cap\ker(A-\lambda I)\bigr). \\]

There are finitely many eigenvalues, but an eigenspace can have dimension greater than one. Hence \\(\mathcal E(U)\\) can contain positive-dimensional projective subspaces.

For example, if \\(A|\_U=\lambda I_U\\) and \\(\dim U\ge2\\), then every point of \\(\mathbb P(U)\\) is an eigenline. This is precisely the exceptional scalar-restriction case already identified in Report 61.

The correct procedure is therefore:

1. Compute the distinct eigenvalues of \\(A\\) over the working field.
2. Compute \\(U\cap\ker(A-\lambda I)\\) for each eigenvalue.
3. Determine the dimensions of these intersections.
4. Apply the row-lift or pencil obstruction to the entire projective eigenspace when its dimension is positive.

For the two-dimensional examples in which the eigenline equation is a nonzero quadratic on \\(\mathbb P^1\\), the finite-eigenline calculation is appropriate. But the report's general \\(d>1\\) statement needs this qualification.

### 2.2 The outside-\\(U\\) lifting statement must be tied to the precise content of Lemma 188

The report asserts that, outside \\(\mathbb P(U)\\), every

\\[ h\in\operatorname{Ann}(L) \\]

has an admissible lift. If Lemma 188 proves exactly that, then it is a substantial simplification: the compressed admissibility equations no longer impose an additional linear restriction on the chosen \\(h\\).

But three things must be distinguished:

- existence of an actual row \\(l\\) lifting a prescribed compressed row \\(h=lN\\);
- existence of such a row satisfying the required \\(lAN\\) condition;
- existence of enough such rows to assemble a matrix \\(L\\) with all required ranks and the chosen row-independence convention.

The first two do not automatically imply the third. In particular, under the convention

\\[ \operatorname{rank}[C;L]=p+q, \\]

the pair-preserving lift-completion condition from the previous work must still be checked. The report should state explicitly whether Lemma 188 proves an individual-row lifting assertion or a simultaneous independent-row completion theorem.

If it proves only individual-row existence, the solver still needs the global completion step.

### 2.3 Openness is useful, but does not decide emptiness

For a fixed parameter space of \\((v,H,\text{lifts})\\), with the algebraic constraints imposed, the conditions

\\[ \operatorname{rank}H=\omega \\]

and

\\[ \operatorname{rank}P(\lambda)=\omega \quad\forall\lambda\in\mathbb C \\]

are open conditions relative to the appropriate fixed-rank algebraic stratum.

For the pencil condition, this follows because the bad locus is the projection of the projective incidence set

\\[ \\{(H,H_A,[x],\lambda): (\lambda H-H_A)x=0\\} \\]

with the appropriate rank and nonzero-vector conditions; after homogenising the spectral parameter, the projection is closed. Equivalently, on the fixed-rank stratum, the common-root condition for the maximal minors is algebraically closed.

So the report is right that a feasible witness is decisive: one exact point satisfying all the conditions proves feasibility.

But openness does not establish that the projection of the feasible joint parameter set onto \\(\mathbb P(W_L)\setminus\mathbb P(U)\\) is open, nor does it decide that this projection is empty. Projection of an open subset under a general algebraic map need not be open. It is generally safer to regard the projected feasible set as constructible.

This matters for the proposed resultant method.

### 2.4 What is the right emptiness method?

I would use a hierarchy of methods rather than begin with a large resultant calculation.

First: derive structural restrictions on \\(B\_\*\\).

The O1 criterion identifies the spectral condition as

\\[ \ker(A\_\*-\lambda I)\cap\ker B\_\*=\\{0\\} \quad\text{for every eigenvalue }\lambda. \\]

Thus a structural proof that \\(B\_\*=0\\) immediately rules out the entire candidate family. More generally, a proof that \\(B\_\*\\) kills a nonzero eigenvector rules it out. This is likely to be much cheaper than eliminating all variables.

Second: formulate the joint incidence problem exactly.

Use projective coordinates for \\(v\\), coordinates for the compressed rows, and coordinates for the actual lifts. Include:

- \\(v\notin U\\);
- the linear admissibility equations;
- exact rank \\(\omega\\) of \\(H\\);
- the pair-preserving lift constraints, if applicable;
- the spectral certificate.

The spectral condition can be encoded using a bounded-degree polynomial generalized-inverse certificate, or by maximal-minor Bézout identities. This turns the universal condition in \\(\lambda\\) into finitely many polynomial equations and inequations.

Third: use elimination or real-algebraic decision methods.

For a fixed low-dimensional parameter space, resultants, Gröbner bases, and saturation may be effective. But the resultant must be constructed from the complete system, not merely from the eigenline equation. Nonvanishing conditions require saturation or an equivalent auxiliary-variable encoding; otherwise the elimination may retain components lying in forbidden loci.

For a general instance, the most robust route is quantifier elimination over the reals, or an exact algebraic-geometric computation over the appropriate coefficient field. This is not expected to be polynomial-time in general, but it can certify emptiness.

My recommendation for O2: retain the \\(U\\)-split, but first prove the exact scope of Lemma 188 and the simultaneous lift condition. Then try to derive a structural obstruction to the outside-\\(U\\) family using the \\(B\_\*\\) criterion. Use elimination only if the structural route fails.

## 3. O1 and O2 together: a cleaner \\(c=1\\) decision framework

There is a useful simplification that Report 62 does not quite make explicit.

The block criterion

\\[ \ker(A\_\*-\lambda I)\cap\ker B\_\*=\\{0\\} \\]

is exactly the Hautus observability test for the pair \\((B\_\*,A\_\*)\\). In standard notation, the pair is observable if

\\[ \operatorname{rank} \begin{bmatrix} \lambda I-A\_\*\\\B\_\* \end{bmatrix} =\omega \quad\text{for all }\lambda\in\mathbb C. \\]

Thus the pencil branch is not a separate mysterious algebraic condition. It is an ordinary observability test for the compressed pair \\((B\_\*,A\_\*)\\).

This gives the following revised decision tree.

Step 1 — Split the candidate lines

\\[ \mathbb P(W_L)=\mathbb P(U)\ \dot\cup\ \bigl(\mathbb P(W_L)\setminus\mathbb P(U)\bigr). \\]

Step 2 — On \\(\mathbb P(U)\\)

Use the \\(c=1\\) hyperplane lemma: non-eigenlines are excluded. For eigenlines, retain the full eigenspaces \\(U\cap\ker(A-\lambda I)\\), not merely a finite list of representatives when these spaces have dimension greater than one. Then test the remaining row-lift and pencil conditions.

Step 3 — Outside \\(\mathbb P(U)\\)

Use the full lift variables. If Lemma 188 applies, generate admissible lifts and impose exact rank and pair-completion conditions.

Step 4 — Test the pencil

Form \\(A\_\*,B\_\*\\) and test

\\[ B\_\*|\_{\ker(A\_\*-\lambda I)}\text{ injective} \\]

for every distinct eigenvalue \\(\lambda\\) of \\(A\_\*\\).

Step 5 — Certify the result

A positive answer requires an actual \\(L\\). A negative answer requires a structural obstruction or an exact algebraic certificate that every branch is empty.

This is more efficient than dividing the pencil branch into diagonalizable and non-diagonalizable cases. The eigenvector test works in both cases.

A practical implementation should compute the distinct eigenvalues and their eigenspaces over an exact algebraic extension. For rational input, algebraic-number arithmetic is appropriate; floating-point eigenvectors are not sufficient for a proof of injectivity.

## 4. Unbounded-\\(c\\) hardness: which target should the project pursue?

This is the strategic question in Report 62. My recommendation is to investigate ETR directly, with affine rank minimisation as the first algebraic source problem and static output feedback as a second, control-theoretic comparison problem.

I would not choose one of these targets without first comparing the structure of its constraints with the observer formulation.

### 4.1 Candidate A: affine rank minimisation

Consider the problem

\\[ \begin{cases} \langle A_i,X\rangle=b_i,\quad i=1,\ldots,m,\\\ \operatorname{rank}X\le r, \end{cases} \\]

where the \\(A_i,b_i\\) are rational and \\(X\\) is the unknown real matrix.

A 2026 preprint by Angshul Majumdar, Affine Rank Minimization is ER Complete, claims that this problem is \\(\exists\mathbb R\\)-complete even when the rank bound is fixed at \\(r=3\\). Its reduction encodes arithmetic-circuit multiplication constraints using rank-forcing gadgets, while all explicit constraints on the matrix entries are affine.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



This is an attractive source for your problem for two reasons.

First, it has a close geometric connection to your compressed matrix \\(H\\).

Your framework has

\\[ H=LN,\qquad \operatorname{rank}H=\omega. \\]

The unknown compressed matrix is constrained by a rank condition, and the remaining constraints arise from its coupling with

\\[ H_A=LAN. \\]

That resembles rank-constrained affine feasibility.

Second, the fixed-rank hardness result is particularly interesting for your unbounded-\\(c\\) question.

In the observer notation,

\\[ c=k-\omega. \\]

A reduction with \\(\omega=3\\) and \\(k\\) growing with the source instance would produce unbounded \\(c\\), even though the compressed rank is fixed. Thus the fixed-rank source result is not an obstacle; it may actually be a useful way to isolate the difficulty in the kernel dimension.

There is, however, a serious reduction obstacle.

In affine rank minimisation, the arbitrary affine equations

\\[ \langle A_i,X\rangle=b_i \\]

are part of the input. In the observer problem, \\(H\\) is not an arbitrary matrix subject to arbitrary affine equations. It must arise as \\(LN\\), and its companion \\(H_A\\) must arise from the same \\(L\\):

\\[ H_A=LAN. \\]

Moreover, the kernel inclusion and the spectral pencil condition must hold.

You therefore cannot simply identify \\(X\\) with \\(H\\) and claim a reduction. You must explain how the affine constraints of the source instance are implemented through the fixed data \\(A,C,L_0\\), and how the spectral condition is maintained.

My assessment: affine rank minimisation is the best first algebraic target, but the main research problem is constructing the embedding into the coupled pair \\((LN,LAN)\\).

### 4.2 Candidate B: static output feedback

A second, particularly relevant development is the recent preprint by Zhaobo Liu, Computational complexity of static output feedback stabilization, arXiv:2610.00390.

It claims that static output feedback stabilization is \\(\exists\mathbb R\\)-complete for rational plant data, even for controllable and observable integer plants with two inputs. It also establishes strong NP-hardness for a family of minimal single-input plants.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.paperpeel.com\&sz=32)

PaperPeel



The standard problem is

\\[ \exists K\quad A+BKC\text{ is Hurwitz}. \\]

This is attractive because it is already a control-synthesis problem with an existential matrix variable and a spectral constraint. There is also a conceptual relationship between output feedback, output injection, and observer synthesis.

But I would be cautious about treating it as a direct reduction source.

Your condition (5b) is

\\[ \operatorname{rank}(\lambda H-H_A)=\omega \quad\forall\lambda\in\mathbb C. \\]

As established in Section 1, this is equivalent to an observability condition on the compressed pair \\((B\_\*,A\_\*)\\). It is not a Hurwitz condition. The distinction matters:

- static output feedback stabilization asks for all closed-loop eigenvalues to lie in the open left half-plane;
- your all-\\(\lambda\\) condition asks for a pencil to have full column rank at every finite complex parameter.

These are different spectral properties. The fact that both are expressed through matrices depending on unknown parameters does not provide a reduction.

There may still be a route through a transformation that encodes the static-feedback characteristic polynomial into the algebraic constraints on \\(V\\) or the compressed pair. But that would require a construction, not merely a duality observation.

My assessment: static output feedback is a very useful control-theoretic source to investigate, especially because of the recent \\(\exists\mathbb R\\)-completeness result. However, affine rank minimisation appears closer to the rank-geometric structure of the observer problem.

### 4.3 Candidate C: general quadratic feasibility

The most direct source is simply ETR in arithmetic-circuit form:

\\[ \exists x_1,\ldots,x_m\in\mathbb R: \quad f_i(x)=0,\quad g_j(x)>0. \\]

After standard transformations, one can assume that the source system consists of elementary arithmetic-gate constraints, particularly

\\[ z=xy,\qquad z=x+y,\qquad z=c. \\]

The observer problem has potentially useful quadratic structure. For example, in a Grassmannian chart, the matrix describing the induced map

\\[ U\longrightarrow \mathbb C^n/U,\qquad x\longmapsto Ax+U \\]

has the form

\\[ F_A(X)= \begin{bmatrix} A\_{21}+A\_{22}X-XA\_{11}-XA\_{12}X\\\ A\_{31}+A\_{32}X \end{bmatrix}. \\]

The term

\\[ XA\_{12}X \\]

is quadratic in the chart variables.

This offers a possible route to encode multiplication gates using incidence or rank constraints. It also links the hardness question to the determinantal geometry already being developed in the project.

However, there is a gap between having quadratic expressions and being able to encode arbitrary arithmetic circuits. A valid reduction must show:

1. each source variable is represented by an identifiable coordinate;
2. each multiplication gate is enforced by a rank or incidence condition;
3. different gates can be composed without unwanted interactions;
4. all auxiliary variables are polynomially bounded in number and encoding size;
5. the resulting instance satisfies the observer's fixed-data requirements;
6. the spectral condition is satisfied exactly when the source system is feasible.

The last two points are likely to be the hardest.

### 4.4 My ranking of the targets

| Candidate                | Structural proximity to your problem        | Main obstacle                                                          | Recommendation              |
| ------------------------ | ------------------------------------------- | ---------------------------------------------------------------------- | --------------------------- |
| ETR arithmetic circuits  | Direct source of polynomial feasibility     | Must encode multiplication and inequalities through observer structure | Essential reference problem |
| Affine rank minimisation | Strong connection to compressed matrix rank | \\(H\\) and \\(H_A\\) must come from the same \\(L\\)                  | First reduction target      |
| Static output feedback   | Strong connection to control synthesis      | Hurwitz stability differs from the all-\\(\lambda\\) pencil condition  | Second reduction target     |

I would also investigate whether the reduction can be organised in two stages:

\\[ \text{ETR} \longrightarrow \text{a structured rank/incidence problem} \longrightarrow \mathrm{DEC}(q). \\]

The intermediate problem should preserve the essential coupling imposed by \\(A\\), rather than treating the compressed matrix as unconstrained.

## 5. A concrete possible hardness programme

Here is the route I would investigate first. It is a research proposal, not a claimed reduction.

### Stage 1: Isolate the algebraic source of nonlinearity

Use an ETR arithmetic circuit or the rank-three affine rank minimisation problem.

The desired intermediate object would be a matrix \\(X\\) satisfying affine constraints and

\\[ \operatorname{rank}X\le3. \\]

Use a fixed \\(3\times3\\) gauge block to convert the rank-at-most-three condition into a rank-exactly-three condition without changing feasibility. This is analogous to the gauge-fixing strategy in the affine-rank-minimisation preprint.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



### Stage 2: Encode the source matrix in the observer kernel geometry

Try to arrange

\\[ \omega=3,\qquad k\text{ variable},\qquad c=k-3. \\]

Then the unknown kernel

\\[ V\in\operatorname{Gr}(k-3,K_0) \\]

has dimension growing with the source instance.

This is attractive because the source's rank-three structure can potentially be represented by the codimension-three quotient

\\[ K_0/V. \\]

The central task is to arrange the fixed map \\(A\\) so that the conditions on \\(V\\), including

\\[ \dim(V\cap A^{-1}V), \\]

encode the desired arithmetic relations.

The earlier Grassmannian chart formula is worth revisiting here: its quadratic term is a possible multiplication gadget.

### Stage 3: Make the spectral condition automatic

This is an important design principle.

You do not want the hardness reduction to be derailed by an unrelated pencil obstruction. Ideally, arrange the construction so that

\\[ B\_\*|\_{\ker(A\_\*-\lambda I)} \\]

is injective for every eigenvalue \\(\lambda\\), regardless of whether the source arithmetic instance is feasible.

For example, a construction with \\(B\_\*\\) injective on all of \\(W\\) would make the pencil condition automatic. Whether this can be achieved simultaneously with the desired kernel geometry and the fixed-data constraints is a central technical question.

This would isolate the hardness in the algebraic feasibility of the kernel and rank conditions.

### Stage 4: Verify actual observer lifting

The construction must produce actual \\(L\\), not just an abstract \\(V\\) or compressed pair.

Under the independence-modulo-\\(C\\) convention, it must satisfy the pair-preserving lift condition. The reduction must preserve the original observer definition, not merely a relaxed compressed problem.

### Stage 5: Prove polynomial size and both directions

A complete reduction needs explicit polynomial-time constructions

\\[ \mathcal I\longmapsto(A\_{\mathcal I},C\_{\mathcal I},L\_{0,\mathcal I},q\_{\mathcal I}) \\]

and proofs of

\\[ \mathcal I\text{ feasible} \iff \mathrm{DEC}(q\_{\mathcal I})\text{ is YES}. \\]

In particular, the reverse implication must recover a satisfying assignment from every feasible observer. This is where gauge fixing, anchor variables, and exact rank constraints become important.

If you can establish this, the existing \\(\exists\mathbb R\\) upper bound would yield \\(\exists\mathbb R\\)-completeness.

## 6. What does the literature say about functional-observer complexity?

I checked the literature relevant to the report's Question 5. The distinction between observer theory and its computational complexity is important.

### 6.1 Minimum-order functional observers

Fernando's 2010 paper, Functional Observability and the Design of Minimum Order Linear Functional Observers, establishes a minimum-order functional-observer design framework. Its contribution is primarily mathematical characterization and construction, not an \\(\exists\mathbb R\\)-hardness result.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

DOI



The 2025 paper by Darouach and Fernando, On functional observability and functional observer design, develops further functional-observability and observer-design conditions. Again, this is not a complexity classification of the existential augmentation condition.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

sciencedirect.com



The two recent 2026 Fernando preprints are particularly relevant to your formulation:

- A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions;
- Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger.

They provide a general minimum-order framework, including the algebraic and spectral characterisations and the family of minimum-dimensional augmentations.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



These papers are important for identifying the exact \\(\exists\Theta\\) condition that your reduction must target. But the available material does not establish that this existential condition is NP-hard or \\(\exists\mathbb R\\)-hard.

### 6.2 Related NP-hardness in functional observability

There is relevant adjacent work. A 2025 paper on functional observability, structural functional observability, and optimal sensor placement proves NP-hardness for certain sensor-selection problems.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://ieeexplore.ieee.org\&sz=32)

IEEE Xplore



This is worth studying because it demonstrates that combinatorial optimisation problems associated with functional observability can be computationally hard.

But it does not establish hardness of your problem. Sensor selection changes the measurement structure; your problem asks for an algebraic augmentation and a spectral pencil condition. A reduction would have to connect these two formulations.

### 6.3 What I did not find

In the literature I checked, I did not find a direct complexity classification of the precise existential augmentation condition in your minimum-order characterisation, nor a direct \\(\exists\mathbb R\\)-hardness proof for the minimum-order functional-observer problem in the form considered here.

That is not proof that no such result exists. It is a statement about the material located in this search, and a systematic review of the references and citations in the recent characterisation papers is still warranted.

The most useful literature leads are therefore:

1. Fernando (2010), for the classical minimum-order functional-observer framework.
2. Darouach and Fernando (2025), for recent functional-observability conditions.
3. Fernando (2026), for the exact minimum-order augmentation characterisation.
4. Liu (2026), for the new \\(\exists\mathbb R\\)-completeness result for static output feedback.
5. Majumdar (2026), for \\(\exists\mathbb R\\)-completeness of affine rank minimisation.

The last two are especially relevant to a new hardness reduction. The first three help ensure that the target problem is formulated correctly.

## 7. Should fixed-\\(c\\) analysis or hardness take priority?

The report asks whether to finish \\(c=1\\), then \\(c=2\\), or move directly to hardness.

My recommendation is parallel workstreams, with a clear division of purpose.

### Workstream A — Finish the fixed-\\(c\\) theory

This should include:

- Correct the O1 diagonalizable claim.
- Replace the diagonalizable/non-diagonalizable split by the general eigenspace-injectivity criterion.
- Complete the O2 analysis, including positive-dimensional eigenspaces and the exact scope of Lemma 188.
- Complete the \\(c=2\\) stratification and solver.
- Validate the solver on both feasible and infeasible instances.

This workstream has immediate mathematical value. It produces exact structural theorems, tests the implementation, and may expose the right incidence structure for a hardness reduction.

### Workstream B — Begin unbounded-\\(c\\) hardness now

Do not wait for every fixed-\\(c\\) case to be solved.

The hardness question is inherently unbounded in \\(c\\), so finishing \\(c=1\\) and \\(c=2\\) cannot by itself resolve it. Start by trying to construct a reduction from affine rank minimisation or an arithmetic-circuit problem.

The first goal should not be a complete reduction. It should be a small expressiveness lemma:

> Can the observer data \\((A,C,L_0)\\) realise a sufficiently general affine or quadratic incidence condition on a Grassmannian chart, while keeping the spectral pencil condition automatically satisfied?

If the answer is yes, that could be the central technical lemma for an \\(\exists\mathbb R\\)-hardness proof.

If the answer is no, understanding the obstruction may reveal a tractable structural restriction in the observer problem.

### Why this division is preferable

The fixed-\\(c\\) work and the hardness work answer different questions:

- Fixed \\(c\\): how much structure can be exploited when the kernel dimension is bounded?
- Unbounded \\(c\\): can the geometry encode arbitrary real algebraic feasibility?

A fixed-\\(c\\) algorithm might be polynomial in the ambient dimensions for each fixed \\(c\\), yet the unrestricted problem could still be \\(\exists\mathbb R\\)-complete. Conversely, proving good component bounds for fixed \\(c\\) does not imply any useful upper bound when \\(c\\) grows.

So I would not let the component-bound project delay the first hardness experiments.

## 8. Revised conclusions and action list for Report 62

Here is the precise status I would assign to the report.

| Result or claim                                             | Assessment                                                 | Required action                                               |
| ----------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------- |
| Block factorisation of \\(P(\lambda)\\)                     | Correct                                                    | Retain                                                        |
| Eigenvector-intersection criterion                          | Correct and complete                                       | Promote to theorem                                            |
| \\(B\_\*=0\\) implies pencil bad                            | Correct                                                    | Retain                                                        |
| \\(B\_\*\ne0\\) and \\(A\_\*\\) diagonalizable implies good | Incorrect                                                  | Replace by injectivity on every eigenspace                    |
| Generalized eigenvectors may create an additional bad case  | No                                                         | Remove this branch                                            |
| \\(O_2\\) decomposition using \\(U\\)                       | Correct                                                    | Retain                                                        |
| Eigenlines in \\(\mathbb P(U)\\) are always finite          | Not in general                                             | Replace by eigenspace-intersection analysis                   |
| Outside-\\(U\\) admissible lifts                            | Depends on Lemma 188                                       | State exact lifting theorem and check simultaneous completion |
| Pencil and rank conditions are open                         | Correct on the relevant fixed-rank parameter space         | Do not infer emptiness from openness                          |
| Resultants decide outside-\\(U\\) emptiness                 | Sometimes useful, not universally sufficient by themselves | Use full elimination/QE formulation                           |
| Affine rank minimisation as a hardness source               | Promising                                                  | First reduction target                                        |
| Static output feedback as a hardness source                 | Promising but structurally less direct                     | Investigate separately                                        |
| Existing functional-observer complexity result              | No direct result located in this review                    | Check references of the recent characterisation papers        |

### Recommended immediate sequence

1. Correct O1 in the mathematical report and solver. This is a definite correction, not a speculative suggestion.
2. Re-run all existing pencil tests using eigenspace injectivity. In particular, check whether any previously classified diagonalizable cases were incorrectly labelled good.
3. Complete O2 with the full eigenspace formulation. Do not assume a finite eigenline set when eigenspaces can have dimension greater than one.
4. Audit Lemma 188 and the simultaneous row-lift condition.
5. Begin a reduction prototype from ARM(3) or ETR arithmetic circuits. Start with a small multiplication gadget in the Grassmannian chart.
6. Keep static output feedback as a second route, but do not assume the all-\\(\lambda\\) pencil condition is interchangeable with Hurwitz stability.
7. Continue \\(c=2\\) in parallel, particularly because it can test whether the general incidence constructions are expressive enough to support a reduction.

## 9. Final assessment

The most important mathematical correction in Report 62 is the O1 criterion. Once the factorisation is written down, the pencil problem becomes exactly

\\[ \ker(A\_\*-\lambda I)\cap\ker B\_\*=\\{0\\} \\]

for every eigenvalue of \\(A\_\*\\). This is a complete eigenvector test. It applies equally to diagonalizable and non-diagonalizable matrices. The generalized-eigenvector distinction is unnecessary, while the report's claim that \\(B\_\*\ne0\\) suffices in the diagonalizable case is false.

The O2 split is a good structural reduction, but it does not yet settle the continuous outside-\\(U\\) family. Its main unresolved issue is the interaction between individual admissible lifts, simultaneous row completion, and the spectral condition. A structural \\(B\_\*\\)-based obstruction should be attempted before general-purpose elimination.

For the complexity question, affine rank minimisation is my preferred first target. Its \\(\exists\mathbb R\\)-completeness even at fixed rank three makes it especially interesting for a construction with \\(\omega=3\\) and unbounded \\(c\\). Static output feedback is also an excellent comparison problem, given the recent \\(\exists\mathbb R\\)-completeness result, but its Hurwitz condition is not the same as your pencil condition.

The central research question I would now pursue is this:

> Can arbitrary real arithmetic be encoded into the incidence geometry of \\(V\subseteq K_0\\) and the coupled compressed pair \\((LN,LAN)\\), while the spectral pencil condition is made automatic?

A positive answer would provide a direct route to \\(\exists\mathbb R\\)-hardness. A negative answer, if supported by a structural theorem, could be equally important: it might identify the hidden rigidity that distinguishes minimum-order functional observers from general rank-constrained algebraic feasibility.

That is the most promising direction opened by Report 62.