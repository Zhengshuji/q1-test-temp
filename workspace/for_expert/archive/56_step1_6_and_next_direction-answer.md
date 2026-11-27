# Overall assessment

The project has made a meaningful transition from an experimental and exploratory study to a collection of exact structural results. The most important development is not yet the type-control conjecture itself. It is the emergence of a coherent sequence of reductions:

1. the original rank conditions are reduced to a problem on the unobservable subspace \\(K\\);
2. the spectral condition is expressed as the absence of a certain eigenvector obstruction;
3. the polynomial-pencil condition is given a finite algebraic certificate;
4. the lifting problem is described through an exact Grassmannian fibre;
5. the remaining geometric difficulty is isolated in the structure of the base incidence varieties.

I regard this as a substantial improvement in the mathematical organisation of the project.

There is, however, one important correction to II.1 that I would make before treating the report as settled: the quotient in the rank condition should generally be the ambient state space modulo \\(V\\), not \\(K_0/V\\). Unless \\(A(K_0)\subseteq K_0\\), the latter quotient does not receive the map induced by \\(A\\). This is not a cosmetic notation issue; it is necessary for the exact fibre theorem to be correctly stated under the general hypotheses.

Subject to that correction, my recommendations are:

- Accept the \\(c=2\\) and \\(c=3\\) classifications as useful structural decompositions, but not yet as complete paper proofs. Their exactness conditions are now substantially improved. The parameterisations and nonemptiness statements still need explicit verification.
- Accept the polynomial certificate strategy, with a short but explicit Bézout-degree lemma. The degree bound \\(2\omega-2\\) is sound under the stated hypotheses.
- Use the robust rank identity in II.8. It is cleaner and avoids an unnecessary side condition.
- Prioritise the exact spectral reduction, the polynomial certificate, the corrected fibre theorem, and a rigorous \\(c=2\\) result. Do not make the general type-control conjecture the immediate centre of the project.
- Treat real-point feasibility as a separate, potentially essential issue if the intended application is over \\(\mathbb R\\).
- Do not invest heavily in formalising the general component-count conjecture at this stage. The unresolved issue is primarily geometric, not a deficiency in Lean.

I discuss each question below.

# 1. Question 1: Are the corrected \\(c=2\\) and \\(c=3\\) classifications acceptable as paper proofs?

## 1.1 First, correct the exact fibre theorem's quotient

Let \\(\mathcal X\\) denote the ambient state space, so that

\\[ K_0\subseteq \mathcal X,\qquad V\subseteq K_0. \\]

For a fixed \\(V\\), define

\\[ \Phi_V:V\longrightarrow \mathcal X/V,\qquad v\longmapsto Av+V. \\]

This map is always well-defined. Its kernel is

\\[ \begin{aligned} \ker\Phi_V &=\\{v\in V:Av\in V\\}\\\ &=V\cap A^{-1}V\\\ &=W. \end{aligned} \\]

Consequently,

\\[ \boxed{\operatorname{rank}\Phi_V=c-\dim W.} \\]

This is the general statement. In particular, the quotient should be written as \\(\mathcal X/V\\), not \\(K_0/V\\), unless the additional hypothesis

\\[ A(K_0)\subseteq K_0 \\]

has been established.

This distinction matters because the setup does not generally imply that \\(K_0\\) is \\(A\\)-invariant. Indeed, the definition

\\[ D=K_0\cap A^{-1}K_0 \\]

is precisely what is needed to restrict \\(A\\) to a map from \\(D\\) into \\(K_0\\). It would be unnecessary if \\(A(K_0)\subseteq K_0\\) were automatic.

The corrected fibre theorem is therefore as follows.

Corrected exact fibre theorem. Fix \\(W\subseteq D\\), with \\(\dim W=t\\), and put

\\[ U=W+A(W). \\]

Then the fibre over \\(W\\), in the incidence description where \\(W=V\cap A^{-1}V\\), is

\\[ \boxed{ \mathcal F_W= \left\\{ V\in\operatorname{Gr}(c,K_0): U\subseteq V,\  \operatorname{rank}\Phi_V=c-t \right\\}, } \\]

where

\\[ \Phi_V:V\to\mathcal X/V,\qquad v\mapsto Av+V. \\]

It is an open subset of

\\[ \operatorname{Gr}(c-\dim U,K_0/U). \\]

Proof. The conditions \\(W\subseteq V\\) and \\(A(W)\subseteq V\\) are equivalent to \\(U\subseteq V\\). Under these conditions,

\\[ W\subseteq\ker\Phi_V. \\]

Thus

\\[ \operatorname{rank}\Phi_V\le c-t. \\]

The condition that equality holds is a maximal-rank condition and hence is Zariski open on the Grassmannian of \\(V\\)'s containing \\(U\\). Finally, equality is equivalent to

\\[ \dim\ker\Phi_V=t, \\]

and since \\(W\subseteq\ker\Phi_V\\) and both spaces have dimension \\(t\\), it is equivalent to

\\[ \ker\Phi_V=W. \\]

This is exactly

\\[ V\cap A^{-1}V=W. \\]

\\(\square\\)

This version is rigorous and general. It should replace II.1 as currently written.

There is also a useful conceptual point: the fibre is not necessarily the entire Grassmannian. It is an open subset of the Grassmannian determined by a rank condition. It may be empty. Any statement about its irreducibility must therefore include nonemptiness.

## 1.2 The \\(c=2\\) classification

The revised classification is structurally sound. The three possibilities

\\[ t=\dim(V\cap A^{-1}V)\in\\{0,1,2\\} \\]

are exhaustive, and the distinction between invariant and non-invariant lines is the right one.

I would nevertheless require several details before treating the classification as a complete theorem.

### Case \\(t=2\\): invariant two-planes

Here

\\[ W=V,\qquad AV\subseteq V. \\]

The restriction \\(A|\_V\\) is a genuine endomorphism of the two-dimensional space \\(V\\), even though \\(A\\) need not preserve all of \\(K_0\\).

Over \\(\mathbb C\\), the possible Jordan types are:

1. two distinct eigenvalues;
2. one eigenvalue with a scalar restriction;
3. one eigenvalue with a nontrivial Jordan block of size two.

The report's descriptions are correct at the level of Jordan type, but the paper should make the ambient constraints explicit.

For distinct eigenvalues \\(\lambda\ne\mu\\), one has

\\[ V=\ell\_\lambda\oplus\ell\_\mu, \\]

where

\\[ \ell\_\lambda\subseteq E\_\lambda\cap K_0,\qquad \ell\_\mu\subseteq E\_\mu\cap K_0. \\]

Thus the corresponding parameter space is

\\[ \mathbb P(E\_\lambda\cap K_0) \times \mathbb P(E\_\mu\cap K_0), \\]

provided the two eigenspaces are nonzero. Here \\(E\_\lambda=\ker(A-\lambda I)\\) is taken in the ambient space.

For a scalar restriction,

\\[ A|\_V=\lambda I_V, \\]

one has

\\[ V\subseteq E\_\lambda\cap K_0, \\]

so the parameter space is

\\[ \operatorname{Gr}(2,E\_\lambda\cap K_0). \\]

For a nontrivial Jordan block, write

\\[ (A-\lambda I)u=v,\qquad (A-\lambda I)v=0, \\]

with \\(u,v\in K_0\\) and \\(v\ne0\\). Then

\\[ V=\operatorname{span}\\{u,v\\}. \\]

The important point is that the eigenline \\(\ell=\mathbb Cv\\) must satisfy the chain-lifting condition

\\[ \ell\subseteq (A-\lambda I)(K_0). \\]

It is not enough that \\(\ell\subseteq E\_\lambda\cap K_0\\).

For a fixed admissible eigenline \\(\ell\\), the set of \\(u\in K_0\\) satisfying

\\[ (A-\lambda I)u\in\ell\setminus\\{0\\} \\]

is, when nonempty, an affine family whose direction is

\\[ E\_\lambda\cap K_0. \\]

After quotienting by the freedom \\(u\mapsto u+\alpha v\\), the fibre dimension is

\\[ \dim(E\_\lambda\cap K_0)-1. \\]

Thus the report's fibre-dimension statement is correct under the chain-lifting hypothesis. The paper should state that hypothesis explicitly and distinguish the parameter space of admissible eigenlines from the fibre over a fixed eigenline.

My judgement: the \\(t=2\\) classification is acceptable as a theorem once these parameter-space qualifications are included. It should not be presented as a classification solely by ambient Jordan blocks of \\(A\\): the intersection with \\(K_0\\) and the chain-lifting constraints are essential.

### Case \\(t=1\\): one-dimensional exact kernel

Write

\\[ W=L=\mathbb Cv,\qquad v\ne0. \\]

There are two genuinely different cases.

#### Subtype A: \\(AL\subseteq L\\)

This includes \\(Av=0\\). One chooses an additional direction \\(x\\) and sets

\\[ V=\operatorname{span}\\{v,x\\}. \\]

The condition \\(Av\in V\\) is automatic because \\(AL\subseteq L\\). The remaining condition is

\\[ Ax\notin V. \\]

Equivalently, the induced map

\\[ V/L\longrightarrow\mathcal X/V \\]

must be injective. Both formulations are correct.

The paper should explicitly note that an eigenline with eigenvalue zero is included. Excluding zero-image lines would incorrectly remove invariant lines.

#### Subtype B: \\(AL\not\subseteq L\\)

Here \\(Av\notin L\\), and the condition \\(A(L)\subseteq V\\) forces

\\[ V=L+AL=\operatorname{span}\\{v,Av\\}. \\]

The exactness condition becomes

\\[ A^2v\notin\operatorname{span}\\{v,Av\\}, \\]

or

\\[ \boxed{\operatorname{rank}[v,Av,A^2v]=3.} \\]

This is the correct criterion. It is substantially stronger than merely requiring \\(A|\_D\\) to be non-scalar.

The nilpotent \\(2\times2\\) Jordan-block counterexample correctly invalidates the old condition. It should be retained in the paper because it demonstrates why a rank-three condition, rather than a non-scalarity condition, is needed.

One additional point: the rank-three condition itself implies that the ambient dimension is at least three. That is obvious mathematically, but an algorithm should handle the lower-dimensional case explicitly.

### Case \\(t=0\\)

Here

\\[ V\cap A^{-1}V=0, \\]

or equivalently

\\[ \operatorname{rank}\Phi_V=2. \\]

This is an open condition on \\(\operatorname{Gr}(2,K_0)\\). The statement is complete.

### Overall assessment of \\(c=2\\)

I would accept the \\(c=2\\) classification as a paper-ready structural theorem after the parameterisation details above are supplied.

The most important remaining work is not another conceptual classification. It is to make the parameter spaces exact:

- specify the base of admissible eigenlines;
- specify the chain-lifting conditions;
- state the affine or projective fibres;
- prove that the listed cases are disjoint and exhaustive;
- distinguish nonempty strata from formal descriptions of potentially empty strata.

## 1.3 The \\(c=3\\) classification

The \\(c=3\\) decomposition is also structurally plausible, but I would be more cautious about calling it a complete classification. The four values

\\[ t=0,1,2,3 \\]

are exhaustive, and the exact rank conditions are appropriate. The remaining issue is that some of the cases still describe admissibility conditions rather than explicit parameter spaces.

### Case \\(t=3\\): invariant three-planes

Here

\\[ AV\subseteq V. \\]

The restriction \\(A|\_V\\) has dimension three. Its possible Jordan structures include:

- three distinct eigenvalues;
- one eigenvalue with partition \\(1+1+1\\);
- one eigenvalue with partition \\(2+1\\);
- one eigenvalue with partition \\(3\\);
- mixtures of eigenvalues with the corresponding dimensions adding to three.

The report's insistence on including distinct eigenvalues is correct. A classification only by the partitions \\(1+1+1,2+1,3\\) would be incomplete.

However, “indexed by elementary divisors” should be understood as a description of the possible restriction types, not yet as a parameterisation of all invariant three-planes. To obtain the latter, one must describe how the relevant eigenvectors and generalized eigenvectors lie in \\(K_0\\), including the compatibility conditions for chains.

This is analogous to the \\(c=2\\) case, but with more possible combinations of elementary divisors.

### Case \\(t=2\\)

Now

\\[ \dim W=2,\qquad U=W+A(W)\subseteq V,\qquad \dim V=3. \\]

Since \\(W\\) has dimension two, there are two cases.

#### Subcase \\(\dim U=3\\)

Then

\\[ V=U. \\]

The exact condition is

\\[ \operatorname{rank}\Phi_V=1. \\]

This is the right condition. It is important not to omit it merely because \\(V\\) is already determined by \\(W\\). The construction \\(V=W+A(W)\\) guarantees \\(W\subseteq V\\) and \\(A(W)\subseteq V\\), but does not by itself guarantee that no additional vector of \\(V\\) maps back into \\(V\\).

If \\(b\\) is a suitable generator of \\(A(W)\\) modulo \\(W\\), then the condition can be written as

\\[ Ab\notin V. \\]

That formulation should be accompanied by a statement that the result is independent of the choice of representative \\(b\\) modulo \\(W\\).

#### Subcase \\(\dim U=2\\)

Then

\\[ A(W)\subseteq W. \\]

The space \\(V\\) is obtained by adding one line:

\\[ V=W+\mathbb Cw. \\]

The exact condition is

\\[ Aw\notin V. \\]

Equivalently, the induced map

\\[ V/W\longrightarrow\mathcal X/V \\]

has rank one.

This is correct, including the singular case \\(A(W)\subsetneq W\\). The distinction should be based on whether \\(A(W)\subseteq W\\), not whether \\(A(W)=W\\).

### Case \\(t=1\\)

Write

\\[ W=L=\mathbb Cv. \\]

Again, the split according to \\(AL\subseteq L\\) is the correct one.

#### Subtype A: \\(AL\subseteq L\\)

Because \\(L\\) is \\(A\\)-invariant, the quotient operator

\\[ \bar A:\mathcal X/L\to\mathcal X/L \\]

is well-defined.

Set

\\[ U'=V/L. \\]

Then \\(\dim U'=2\\), and exactness requires

\\[ \boxed{U'\cap\bar A^{-1}U'=0,} \\]

where the preimage is taken in the appropriate quotient domain, namely \\(K_0/L\\).

This is the correct condition. It is stronger than the absence of an invariant line. A two-dimensional subspace can contain no invariant line and nevertheless have a nonzero vector mapped back into itself modulo the quotient subspace. The rank-two condition rules out all such vectors at once.

#### Subtype B: \\(AL\not\subseteq L\\)

Here \\(L+A(L)\\) is two-dimensional. A three-dimensional \\(V\\) must have the form

\\[ V=L+A(L)+\mathbb Cw. \\]

The quotient \\(\mathcal X/V\\) receives two relevant images:

\\[ A^2v+V,\qquad Aw+V. \\]

The exact condition is that these two images be linearly independent. This is the correct rank-two condition on the quotient map.

It is not sufficient to require only

\\[ A^2v\notin V. \\]

That would ensure one nonzero image but would not ensure that the second independent direction is present.

The paper should write this as a rank condition, for example

\\[ \operatorname{rank} \begin{bmatrix} A^2v+V & Aw+V \end{bmatrix}=2, \\]

with the quotient-space interpretation made explicit.

### Case \\(t=0\\)

The condition is

\\[ \operatorname{rank}\Phi_V=3. \\]

This is again an open condition.

### Overall assessment of \\(c=3\\)

I would accept II.3 as a correct case decomposition and exact admissibility framework, subject to the ambient-quotient correction.

I would not yet call it a complete parameter classification. In particular, the \\(t=1\\) and \\(t=2\\) cases still require:

1. an explicit description of the base parameters \\(W\\);
2. an explicit description of the extension choices for \\(V\\);
3. a proof that the displayed rank conditions are equivalent to exactness;
4. a proof that all parameterisations are algebraic and that the stated nonempty loci are actually nonempty when claimed.

The distinction is important for the paper. A theorem saying “the solutions are exactly those satisfying this rank condition” is useful and rigorous, but it is not the same as a theorem describing all irreducible components or giving an algorithm for enumerating them.

# 2. Question 2: Is the polynomial certificate proof sound?

My assessment is positive. The proposed certificate and the degree bound

\\[ \boxed{\deg Y\le 2\omega-2} \\]

are sound, provided the proof includes the Bézout-degree lemma and handles the zero-rank case separately.

Let

\\[ P(\lambda)\in\mathbb C[\lambda]^{q\times k} \\]

have normal rank \\(\omega\\), and suppose

\\[ \operatorname{rank}P(\lambda)=\omega \qquad\forall\lambda\in\mathbb C. \\]

## 2.1 Maximal minors and the gcd condition

Let \\(p\_\alpha(\lambda)\\) denote the collection of all \\(\omega\times\omega\\) minors of \\(P(\lambda)\\), including identically zero minors if convenient.

Since \\(P\\) has normal rank \\(\omega\\), at least one such minor is nonzero.

The rank drops below \\(\omega\\) at a finite \\(\lambda_0\\) exactly when every maximal minor vanishes at \\(\lambda_0\\). Over \\(\mathbb C\\), this is equivalent to the maximal minors having a nonconstant common factor.

Therefore,

\\[ \operatorname{rank}P(\lambda)=\omega \quad\forall\lambda\in\mathbb C \\]

if and only if

\\[ \gcd\_\alpha p\_\alpha(\lambda)\in\mathbb C^\times. \\]

The algebraic closedness of \\(\mathbb C\\) is being used here: every nonconstant complex polynomial has a root.

This equivalence is exact.

## 2.2 The Bézout coefficient degree bound

Each maximal minor has degree at most \\(\omega\\), because each entry of \\(P\\) has degree at most one in the pencil case, and more generally the stated \\(2\omega-2\\) estimate presupposes that the entries have degree at most one.

More precisely, for a linear pencil,

\\[ \deg p\_\alpha\le\omega. \\]

Suppose the nonzero maximal minors have gcd \\(1\\). Choose one nonzero minor \\(p_1\\) of degree \\(d\le\omega\\).

Because

\\[ \gcd(p_1,p_2,\ldots,p_s)=1, \\]

the images of \\(p_2,\ldots,p_s\\) generate the unit ideal in the quotient ring

\\[ \mathbb C[\lambda]/(p_1). \\]

Thus there exist polynomials \\(b_2,\ldots,b_s\\), each represented by a polynomial of degree less than \\(d\\), such that

\\[ \sum\_{j=2}^s b_jp_j\equiv1\pmod{p_1}. \\]

Consequently,

\\[ b_1=\frac{1-\sum\_{j=2}^s b_jp_j}{p_1} \\]

is a polynomial.

The numerator has degree at most

\\[ (d-1)+d=2d-1, \\]

so

\\[ \deg b_1\le d-1. \\]

Therefore all coefficients can be chosen with

\\[ \boxed{\deg b_j\<d\le\omega.} \\]

This is the key elementary lemma. It is worth writing explicitly rather than saying only that the extended Euclidean algorithm gives a degree bound. With many generators, a reader may reasonably ask why the degrees remain bounded.

## 2.3 The adjugate construction

For each maximal minor indexed by a row set \\(I\\) and column set \\(J\\), let

\\[ M\_{I,J}=P\_{I,J} \\]

be the corresponding \\(\omega\times\omega\\) submatrix.

Let \\(S_I\\) and \\(T_J\\) be the row and column selection matrices, so

\\[ M\_{I,J}=S_IPT_J. \\]

Define the embedded adjugate

\\[ Y\_{I,J}=T_J\operatorname{adj}(M\_{I,J})S_I. \\]

This is a \\(k\times q\\) polynomial matrix.

The crucial identity is

\\[ \boxed{ P\\,Y\_{I,J}\\,P = \det(M\_{I,J})P. } \\]

For a minor that is generically invertible, this follows over the rational function field from the rank-\\(\omega\\) factorisation of \\(P\\). Namely, since \\(P\\) has rank \\(\omega\\) and \\(M\_{I,J}\\) is invertible generically,

\\[ P = PT_JM\_{I,J}^{-1}S_IP. \\]

Multiplying by \\(\det(M\_{I,J})\\) gives

\\[ P\\,T_J\operatorname{adj}(M\_{I,J})S_I\\,P = \det(M\_{I,J})P. \\]

Both sides are polynomial matrices, so the identity extends as a polynomial identity.

Now set

\\[ Y=\sum\_{I,J}b\_{I,J}Y\_{I,J}, \\]

where

\\[ \sum\_{I,J}b\_{I,J}\det(M\_{I,J})=1. \\]

Then

\\[ \begin{aligned} PYP &=\sum\_{I,J}b\_{I,J}P Y\_{I,J}P\\\ &=\sum\_{I,J}b\_{I,J}\det(M\_{I,J})P\\\ &=P. \end{aligned} \\]

This is exactly the required polynomial generalised-inverse identity.

## 2.4 Degree estimate

For a linear pencil:

- \\(\deg b\_{I,J}\le\omega-1\\);
- \\(\deg\operatorname{adj}(M\_{I,J})\le\omega-1\\).

Hence

\\[ \deg Y\_{I,J}\le\omega-1, \\]

and therefore

\\[ \boxed{\deg Y\le2\omega-2.} \\]

This estimate is correct.

The same argument gives a useful generalisation. If the entries of \\(P\\) have degree at most \\(d\\), then maximal minors have degree at most \\(d\omega\\), and the same construction gives the bound

\\[ \deg Y\le 2d\omega-2d. \\]

The linear-pencil result is the special case \\(d=1\\).

## 2.5 The Smith-form argument

The Smith-form observation is correct as an existence argument, but it is not by itself the cleanest route to the degree estimate.

Over the PID \\(\mathbb C[\lambda]\\), there are unimodular matrices \\(U,V\\) such that

\\[ UPV= \begin{bmatrix} d_1\\\ &\ddots\\\ &&d\_\omega\\\ &&&0 \end{bmatrix}, \\]

with the nonzero invariant factors satisfying the usual divisibility conditions.

If \\(P(\lambda)\\) has rank \\(\omega\\) for every finite \\(\lambda\in\mathbb C\\), none of the nonzero invariant factors can have a complex root. Therefore each \\(d_i\\) is a nonzero constant.

After rescaling, the Smith form becomes

\\[ UPV= \begin{bmatrix} I\_\omega&0\\\ 0&0 \end{bmatrix}. \\]

This gives a polynomial generalised inverse. But the unimodular matrices \\(U,V\\) obtained from Smith reduction may have degrees that are not controlled by the desired bound. Thus:

- use Smith form to establish the structural equivalence;
- use the maximal-minor Bézout construction to establish the explicit degree bound.

That separation is mathematically clean.

### Two qualifications

First, the statement should explicitly cover \\(\omega=0\\). In that case \\(P\\) is the zero matrix, and \\(Y=0\\) works. The expression \\(2\omega-2\\) is not meaningful as a nonnegative degree bound in that case. State the theorem for \\(\omega\ge1\\), with the rank-zero case handled separately.

Second, distinguish normal rank from pointwise rank. The theorem assumes normal rank \\(\omega\\), and the pointwise hypothesis says that this rank is attained at every finite complex \\(\lambda\\). Neither condition should be silently omitted.

Conclusion on II.7: I would accept the polynomial certificate proof. The only gap I would flag is an omitted proof of the Bézout coefficient degree bound, together with the need to write the embedded-adjugate identity with dimensions and selection matrices made explicit. These are short paper-proof tasks, not reasons to delay the result.

# 3. Question 3: Is the robust rank identity the right statement?

Yes. I would use the robust identity as the primary statement:

\\[ \boxed{ \operatorname{rank} \begin{bmatrix}P\\\Q\end{bmatrix} + \bigl(2-\operatorname{rank}[v,Av]\bigr) =\delta. } \\]

It is preferable to

\\[ \operatorname{rank} \begin{bmatrix}P\\\Q\end{bmatrix} = \delta-2+\operatorname{rank}[v,Av] \\]

because the latter uses natural-number subtraction and requires an explicit nonnegativity hypothesis.

The robust form has several advantages:

1. It is meaningful for every \\(\delta\\), including \\(\delta=0,1\\).
2. It makes the nonnegativity transparent.
3. It avoids the possibility that an implementation or formalisation silently interprets truncated natural subtraction as ordinary integer subtraction.
4. It is the natural dimension identity arising from the kernel correspondence.

The equivalent paper form can be stated as a corollary:

If \\(\delta\ge2\\), then

\\[ \operatorname{rank} \begin{bmatrix}P\\\Q\end{bmatrix} = \delta-2+\operatorname{rank}[v,Av]. \\]

I would state both, but identify the robust identity as the fundamental lemma.

There is one further improvement worth considering. Since

\\[ \operatorname{rank}[v,Av]\in\\{1,2\\} \\]

for nonzero \\(v\\), the identity gives the two cases immediately:

\\[ \operatorname{rank} \begin{bmatrix}P\\\Q\end{bmatrix} = \begin{cases} \delta-1,&v\text{ is an eigenvector of }A,\\\\[2mm] \delta,&v\text{ is not an eigenvector of }A, \end{cases} \\]

when \\(\delta\ge2\\).

This makes the geometric meaning of the rank identity more visible. The robust equation should remain the formalised theorem; the case split is the paper-facing interpretation.

# 4. Question 4: Which open items should be prioritised?

I would not prioritise the five listed directions equally. They differ substantially in mathematical risk, likely payoff, and dependence on unresolved results.

My recommended order is:

Priority 1 — Consolidate the exact core theorems

Immediate

Correct and finalise the exact fibre theorem, polynomial certificate, spectral block criterion, and the reduction from (5a)–(5b).

Priority 2 — Complete the \\(c=2\\) classification and algorithm

High

Turn the classification into an exact finite procedure with explicit parameter spaces and exact algebraic verification.

Priority 3 — Establish a rigorous \\(c=3\\) structural theorem

High

Complete the case decomposition and identify which strata admit effective parameterisations.

Priority 4 — Resolve real-point feasibility

Conditional, but important

Essential if the intended problem is over \\(\mathbb R\\); less urgent if the project is explicitly complex-algebraic.

Priority 5 — Investigate type-control and component bounds

Research direction

Pursue a restricted theorem first. Do not make a general \\(k\\)-independent component bound a prerequisite for progress.

## 4.1 Why the \\(c=2\\) algorithm should come before general type-control

The \\(c=2\\) classification has a particularly manageable structure:

- \\(t=2\\): invariant two-planes, controlled by eigenvectors and length-two Jordan chains;
- \\(t=1\\): invariant-line and non-invariant-line cases;
- \\(t=0\\): an open maximal-rank condition.

The nontrivial part is not the number of possible values of \\(t\\), but the exact parameterisation and the feasibility of the open conditions.

This makes \\(c=2\\) a natural test case for a complete algorithmic result.

I would aim for an algorithm that:

1. computes \\(D=K_0\cap A^{-1}K_0\\);
2. enumerates the admissible eigenlines and chain data for the invariant cases;
3. handles the non-invariant case through the rank-three condition;
4. tests the open rank conditions exactly;
5. checks the remaining lifting and spectral conditions using polynomial certificates.

The algorithm should not rely on the phrase “choose a generic point.” It should specify the representation of the parameter spaces, the field of computation, and the exact test used to determine whether the required open subset is nonempty.

This would be a genuine mathematical contribution even if no general component-count theorem is obtained.

## 4.2 Why \\(c=3\\) should be a structural result first

For \\(c=3\\), the classification is already useful, but a complete algorithm will require more work.

The \\(t=1\\) non-invariant case is particularly instructive: it requires two independent quotient images, not merely one nonzero image. This indicates that the difficulty increases with the dimension of the quotient \\(V/W\\).

I would first establish a clean theorem stating the exhaustive cases and exact rank conditions. Only then should you attempt to turn all strata into a finite algorithm.

## 4.3 Real-point feasibility

This deserves separate treatment if the intended application is real.

A nonempty complex algebraic variety need not have a real point. Likewise, a nonempty complex Zariski-open subset of a complex component does not automatically give a real admissible point on that component.

For example, a variety defined over \\(\mathbb R\\) can have complex points but no real points. Therefore a complex component decomposition is not, by itself, a real feasibility algorithm.

There are two distinct questions:

1. Does the complex incidence variety have an admissible point?
2. Does the real locus contain an admissible point?

The second requires real algebraic geometry, not merely complex algebraic geometry.

If the original synthesis problem is intended over \\(\mathbb R\\), I would not postpone this question indefinitely. At minimum, the paper should state clearly whether its theorems concern complex feasibility, real feasibility, or both.

A sensible initial step is to identify sufficient conditions guaranteeing real points—for example, explicit real parameterisations of the relevant strata—before attempting a full real-algebraic decision procedure.

## 4.4 Component decomposition complexity

This should be investigated after the \\(c=2\\) and \\(c=3\\) parameterisations are stable.

There is a danger of conflating three different computational tasks:

- deciding whether a good point exists;
- enumerating the irreducible components of the admissible variety;
- bounding the number of irreducible components.

The first can be substantially easier than the second or third. An exact feasibility algorithm need not enumerate every component.

The input model also matters. A complexity statement over rational input matrices is different from one over arbitrary complex coefficients, where exact equality and arithmetic are not algorithmically specified without an encoding model.

I recommend that the project explicitly separate these three tasks and define the coefficient-field model before making a complexity claim.

# 5. Question 5: Is there a route to a genuine theorem for general \\(c\\)?

Yes, but I would approach it through a sequence of restricted geometric theorems rather than directly attempting a global component bound.

The Kronecker/quiver formulation is the right language for organising the problem. It does not, by itself, prove a component bound.

## 5.1 The correct ambient representation

Recall

\\[ D=K_0\cap A^{-1}K_0, \qquad \iota:D\hookrightarrow K_0, \qquad A_0=A|\_D:D\to K_0. \\]

The pair

\\[ (\iota,A_0):D\rightrightarrows K_0 \\]

is a representation of the Kronecker quiver.

Every admissible \\(W\\) lies in \\(D\\), and the associated subspace

\\[ U=W+A_0(W) \\]

is the smallest subspace of \\(K_0\\) containing both images of \\(W\\).

The base incidence problem is therefore described by

\\[ W\in\operatorname{Gr}(t,D), \qquad U=W+A_0(W). \\]

For each fixed \\(t\\), the dimension

\\[ u=\dim U \\]

satisfies

\\[ t\le u\le 2t. \\]

This simple inequality is useful: when \\(c\\) is fixed, both \\(t\\) and \\(u\\) are bounded independently of \\(k\\).

The remaining extension space is

\\[ \operatorname{Gr}(c-u,K_0/U), \\]

restricted to the open rank condition

\\[ \operatorname{rank}\Phi_V=c-t. \\]

Thus the general geometry has two layers:

1. the base incidence geometry of \\(W\mapsto W+A_0(W)\\);
2. an open Grassmannian fibre over each base point.

This is the correct starting point for a general theorem.

## 5.2 A first genuine theorem: finite rank stratification

For fixed \\(t\\), consider the universal subbundle

\\[ \mathcal S\to\operatorname{Gr}(t,D). \\]

The two maps \\(\iota\\) and \\(A_0\\) induce a bundle map

\\[ \mathcal S\oplus\mathcal S \longrightarrow K_0\otimes\mathcal O, \qquad (w_1,w_2)\longmapsto \iota(w_1)+A_0(w_2). \\]

Its image at \\(W\\) is

\\[ W+A_0(W). \\]

Therefore the condition

\\[ \dim(W+A_0(W))=u \\]

is a determinantal rank condition. It defines a locally closed algebraic stratum in \\(\operatorname{Gr}(t,D)\\).

Since

\\[ t\le u\le2t, \\]

there are only finitely many possible pairs \\((t,u)\\) for fixed \\(c\\).

This yields a genuine finite locally closed stratification by the dimensions \\(t\\) and \\(u\\), without invoking Jordan type or Kronecker canonical form.

That is a useful theorem, but it is not yet a component bound. A determinantal stratum can itself be reducible.

## 5.3 A second theorem: the fibre construction is algebraic

Over a fixed rank stratum where \\(\dim U=u\\) is constant, the spaces \\(U\\) form an algebraic subbundle of the trivial \\(K_0\\)-bundle.

Consequently, the Grassmannians

\\[ \operatorname{Gr}(c-u,K_0/U) \\]

assemble into a relative Grassmannian over that stratum.

The exactness condition

\\[ \operatorname{rank}\Phi_V=c-t \\]

is open. Therefore the total incidence space over that stratum is an open subvariety of a relative Grassmannian.

This gives a genuine algebraic-geometric statement:

> Over every fixed-\\((t,u)\\) base stratum, the incidence space is an open subvariety of a relative Grassmannian.

This is stronger and more precise than saying informally that the fibres are open Grassmannians.

It also gives a component statement under an additional hypothesis:

> If a base stratum is irreducible and the open fibre is nonempty over every point, then the corresponding total space is irreducible.

The nonemptiness condition is important. An open subset of a relative Grassmannian can have empty fibres over some base points. One should either restrict to the locus where the fibre is nonempty or prove uniform nonemptiness.

## 5.4 What is still missing for a component bound?

The missing step is a bound on the number of irreducible components of the base rank strata.

The fact that there are only finitely many possible \\((t,u)\\) does not imply that each rank stratum has only a bounded number of components.

The Kronecker canonical form classifies the ambient pair of maps under strict equivalence, but the subspace incidence problem depends on how \\(W\\) is embedded in \\(D\\) and how the two images sit in \\(K_0\\). The canonical form organises the linear data; it does not automatically classify the geometry of all relevant subspace varieties.

This is exactly why the report's revised type-control conjecture is appropriately cautious.

## 5.5 A more promising restricted theorem

I would pursue a theorem in one of the following settings before attempting the general conjecture.

Setting A: \\(A(K_0)\subseteq K_0\\).

Then \\(K_0\\) is \\(A\\)-invariant, and the problem becomes one about invariant and almost-invariant subspaces of an endomorphism. Jordan decomposition can be used directly. This is a substantially simpler situation.

Setting B: The Kronecker pencil is regular on the relevant summand.

If the relevant part of the pencil has a particularly simple Kronecker decomposition, the subrepresentation problem may reduce to a controlled collection of invariant-subspace problems.

Setting C: \\(c\\) is fixed and small.

For fixed \\(c\\), only subspaces of dimension at most \\(c\\) are involved. One may be able to classify all possible restricted pairs

\\[ (\iota|\_W,A_0|\_W) \\]

by finitely many small-dimensional types, with the eigenvalue parameters and embedding data handled separately.

I favour Setting C as the immediate continuation because it directly extends the \\(c=2\\) and \\(c=3\\) work.

## 5.6 Can one prove a \\(k\\)-independent component bound?

It remains plausible, but it is not a consequence of the current arguments.

The fact that \\(t\le c\\) and \\(u\le2c\\) is encouraging. It means the dimensions of the subspaces being selected are bounded. However, the ambient Kronecker representation can have increasingly complicated multiplicities and embedding data as \\(k\\) grows.

A proof would need to show that this growing ambient data cannot generate arbitrarily many irreducible components in the fixed-\\(c\\) incidence problem.

I would not claim such a result until either:

- a uniform geometric argument is found; or
- a systematic search for counterexamples has been conducted for increasing ambient dimensions and fixed \\(c\\).

The latter should be treated as a falsification programme, not as proof.

My recommendation: replace the broad type-control conjecture by a hierarchy:

1. finite \\((t,u)\\)-rank stratification — theorem;
2. relative-Grassmannian fibre theorem — theorem;
3. component behaviour over irreducible base strata — conditional theorem;
4. uniform component bound for fixed \\(c\\) — conjecture.

This gives the project a sequence of defensible mathematical results even if the last step remains open.

# 6. Question 6: Which paper proofs should I review, and which should not be formalised?

I would separate the work into three categories.

## 6.1 Paper proofs I would specifically review

These are the proofs where a small gap could affect the correctness of a central theorem.

| Result                       | Review priority | Main issue to verify                                                         |
| ---------------------------- | --------------- | ---------------------------------------------------------------------------- |
| Exact fibre theorem          | Very high       | Correct ambient quotient and equivalence of rank condition with exact kernel |
| Polynomial certificate       | Very high       | Bézout degree bound and embedded-adjugate identity                           |
| Spectral block criterion     | Very high       | Equivalence between pencil rank drop and the eigenvector obstruction         |
| Reduction from (5a)–(5b)     | Very high       | Kernel correspondence, surjectivity, and treatment of the kernel \\(D\\)     |
| \\(c=2\\) classification     | High            | Exhaustiveness, chain-lifting conditions, and exactness                      |
| \\(c=3\\) classification     | High            | Quotient maps and the independence condition in the non-invariant case       |
| Hyperplane theorem           | High            | Irreducible strata, bundle construction, and component count                 |
| Generic-feasibility argument | Medium-high     | Closedness of the bad locus and the projection argument                      |

### A. Exact fibre theorem

This deserves a complete written proof, because it is the bridge between the subspace classification and the geometric incidence construction.

The proof is short, but it must use

\\[ \Phi_V:V\to\mathcal X/V, \\]

not \\(V\to K_0/V\\) without an invariance hypothesis.

### B. Polynomial certificate

I would review the Bézout-degree argument and the identity

\\[ P\\,T_J\operatorname{adj}(S_IPT_J)S_I\\,P = \det(S_IPT_J)P. \\]

These are the two technical points that turn a qualitative existence theorem into an explicit bounded-degree certificate.

### C. Spectral block criterion

The equivalence

\\[ \operatorname{rank} \begin{bmatrix} \lambda I-A\\\ B \end{bmatrix}<\omega \iff \exists y\ne0:\ Ay=\lambda y,\ By=0 \\]

is elementary, but its use in the compressed-pencil setting requires the factorisation and splitting arguments to be written without changing the domain or codomain inadvertently.

I would verify the dimensions and the exact role of the full-column-rank factorisation.

### D. Hyperplane theorem

This is a more delicate algebraic-geometric argument. The claimed component count depends on:

- the decomposition of the base into eigenvector projective subspaces and their complement;
- constant-rank descriptions of the lift constraints;
- vector-bundle structure over the resulting strata;
- the effect of imposing full-row-rank and spectral open conditions.

The proof should not merely say that the strata are “obviously” irreducible. It should identify each base stratum and prove the relevant total space is irreducible when nonempty.

## 6.2 Results that need a paper proof but not necessarily Lean

I would not insist on formalising:

- the general polynomial degree argument;
- the relative-Grassmannian construction;
- the hyperplane component argument;
- the general type-control conjecture;
- the full \\(c=2\\) and \\(c=3\\) component decompositions.

These are better developed first as carefully written mathematical proofs. Formalisation should follow once the statements are stable and the relevant algebraic-geometric library support is available.

## 6.3 Lean priorities

The current formalisation programme is sensible. The following results have a particularly good ratio of formalisation value to effort:

1. rank inequality;
2. lifting rank formula;
3. block spectral criterion;
4. hyperplane rank identities;
5. constant-matrix generalised-inverse identity;
6. explicit counterexamples.

I would also add the following small but useful formalisation target:

\\[ \ker\Phi_V=V\cap A^{-1}V \\]

and

\\[ \operatorname{rank}\Phi_V+\dim(V\cap A^{-1}V)=\dim V. \\]

This is the linear-algebraic core of the exact fibre theorem. It is a natural, stable formalisation target.

The polynomial degree estimate is less attractive for Lean at this stage. It involves polynomial gcds, Bézout identities, adjugates, and degree bookkeeping. The paper proof is short enough to be more efficient and more readable.

Likewise, I would not formalise the type-control conjecture until the geometric statement has been proved or reduced to a stable finite collection of lemmas.

### A caution on the Lean verification claims

The reported axiom list

\\[ [\texttt{propext},\texttt{Classical.choice},\texttt{Quot.sound}] \\]

is reassuring, and the absence of `sorry` is important. But the statement “compiled without `sorry`” should be understood at the level of the actual theorem and its dependency closure.

For a paper-facing formalisation claim, I would also check:

- whether the theorem is stated over the intended field and dimensions;
- whether all nondegeneracy assumptions are explicit;
- whether helper lemmas imported from the project contain additional axioms or placeholders;
- whether the formal statement matches the mathematical statement, especially regarding natural-number subtraction and quotient-space types.

The formalisation is valuable evidence that the algebraic identities have been translated correctly. It does not replace checking that the formal theorem is the theorem the paper intends to claim.

# 7. Question 7: What is the strongest contribution, and what should happen next?

## 7.1 The strongest contribution

I would identify the strongest contribution as the exact structural reduction of the original augmentation problem to a compressed spectral-pencil problem, together with a finite polynomial certificate for the spectral condition.

The type-control conjecture is potentially more ambitious, but it is not yet the strongest established result because its component-count claims remain open.

The exact spectral reduction has several advantages:

1. It explains what the universal rank condition (5b) is actually testing.
2. It replaces an infinite family of rank tests indexed by \\(\lambda\\) with a finite algebraic condition.
3. It identifies the obstruction as an eigenvector lying in a specified kernel.
4. It connects the original augmentation variables to a smaller compressed pencil.
5. It supports exact verification and a complexity upper bound.

The polynomial certificate then makes this reduction algorithmically meaningful.

In particular, the implication

\\[ \operatorname{rank}P(\lambda)=\omega\quad\forall\lambda\in\mathbb C \\]

if and only if

\\[ \exists Y(\lambda)\quad PYP=P \\]

with an explicit degree bound is a strong result. It turns a universal spectral rank condition into a finite polynomial identity with bounded-degree unknowns.

This is more than a computational convenience: it is a mathematically exact certificate theorem.

## 7.2 The second strongest contribution

The exact fibre theorem is the next strongest result.

It provides the correct geometry of the lifting problem:

\\[ W=V\cap A^{-1}V,\qquad U=W+A(W), \\]

followed by an open Grassmannian extension problem.

This is an important correction to the earlier, weaker condition involving \\(A(V)\cap V\\). The exact kernel condition is what makes the incidence geometry faithful to the original problem.

I would regard the combination of the spectral reduction, polynomial certificate, and exact fibre theorem as the current mathematical core.

## 7.3 What I would do next

I recommend the following concrete sequence.

### Step 1: Freeze the exact statements

Prepare a short internal theorem sheet containing the exact hypotheses and conclusions of:

- the reduction of (5a);
- the spectral kernel correspondence;
- the block eigenvector criterion;
- the polynomial certificate;
- the exact fibre theorem;
- the hyperplane theorem.

Resolve the ambient quotient issue in II.1 before proceeding.

This will prevent later reports from using subtly different versions of the same theorem.

### Step 2: Complete the \\(c=2\\) theorem

Do not start with component-count complexity. Start with a theorem that gives:

- the exhaustive \\(t=0,1,2\\) cases;
- exact parameter spaces;
- exact nonemptiness conditions;
- exact rank tests;
- the connection to the original lifting variables.

Then determine whether each stratum has an effective exact parameterisation.

This is the most realistic route to a complete low-codimension result.

### Step 3: Build a \\(c=2\\) exact algorithm

Specify:

- the coefficient field and input representation;
- how eigenvalues and eigenspaces are computed;
- how Jordan-chain conditions are checked;
- how the open rank conditions are tested;
- how polynomial certificates verify the spectral condition.

Avoid probabilistic language unless the algorithm includes a precise sampling distribution and a proven error bound.

An exact deterministic algorithm would be preferable. If that is not feasible, a Las Vegas or one-sided Monte Carlo formulation may be considered, but the probability statement must be derived from an explicit parameterisation and degree bound.

### Step 4: Finish the \\(c=3\\) structural theorem

The objective should be a complete and correct case decomposition, not yet a universal algorithm.

In particular, verify the \\(t=1\\) non-invariant case carefully. The independence of

\\[ A^2v+V,\qquad Aw+V \\]

is the key condition.

### Step 5: Prove the first general incidence theorem

Prove the finite \\((t,u)\\)-rank stratification and the relative-Grassmannian fibre theorem from Section 5.

These are attainable general-\\(c\\) results and would strengthen the project even if the component-bound conjecture remains open.

### Step 6: Revisit real feasibility

If the application is real, identify which complex components have real points and whether the admissible open subsets meet those real loci.

This should be done before making a claim that complex generic feasibility implies real feasibility.

### Step 7: Return to type-control

Only after the preceding steps should the project attempt to prove a general component bound.

At that point, the \\(c=2\\) and \\(c=3\\) cases may reveal the correct invariant and the right induction mechanism. The Kronecker representation should be used as an organising structure, not treated as a ready-made component theorem.

# 8. A more precise formulation of the type-control programme

I suggest revising II.5 into three separate statements.

Theorem A — finite rank stratification.

For fixed \\(c\\), the incidence base

\\[ W\in\operatorname{Gr}(t,D),\qquad U=W+A_0(W) \\]

admits a finite locally closed stratification by

\\[ 0\le t\le c,\qquad t\le u=\dim U\le2t. \\]

This follows from determinantal rank conditions on the universal bundle map.

Theorem B — relative Grassmannian fibre theorem.

Over a fixed-\\((t,u)\\) stratum, the choices of \\(V\\) containing \\(U\\) form a relative Grassmannian, and the exactness condition is an open rank condition. Hence the incidence space is an open subvariety of that relative Grassmannian.

Conjecture C — uniform component control.

For fixed \\(c\\), the number of irreducible components of the resulting incidence variety is bounded by a function of \\(c\\) and suitable finite-dimensional type data, with a possible stronger version asserting independence from \\(k\\).

This formulation has two advantages.

First, it separates what can already be proved from what remains conjectural.

Second, it makes the open problem much sharper: the unresolved issue is the number and geometry of components of the base rank strata, not the existence of the Grassmannian fibres.

# 9. Final verdict

| Question                                | Assessment                                                                                                                                                                                                         |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1. \\(c=2,c=3\\) classifications        | Structurally correct after the ambient-quotient correction; \\(c=2\\) is close to paper-ready, while \\(c=3\\) still needs more explicit parameter-space and nonemptiness proofs.                                  |
| 2. Polynomial certificate               | Sound. The \\(2\omega-2\\) bound is correct for a linear pencil. Add the explicit Bézout-degree lemma and embedded-adjugate identity; handle \\(\omega=0\\) separately.                                            |
| 3. Robust rank identity                 | Use the robust additive identity as the primary theorem. Give the subtraction formula only under \\(\delta\ge2\\).                                                                                                 |
| 4. Priorities                           | Exact core theorems first; then \\(c=2\\) algorithm; then \\(c=3\\) structure; real feasibility if relevant; general component bounds last.                                                                        |
| 5. General-\\(c\\) theorem              | Yes: finite rank stratification and relative-Grassmannian fibre theorem are realistic. A uniform component bound remains conjectural.                                                                              |
| 6. Proof review and formalisation       | Review the fibre theorem, polynomial certificate, spectral reduction, hyperplane theorem, and \\(c=2/c=3\\) exactness arguments. Formalise stable linear-algebraic identities, not the broad geometric conjecture. |
| 7. Strongest contribution and next step | The exact spectral reduction plus bounded-degree polynomial certificate is strongest. The immediate next step is a complete \\(c=2\\) theorem and exact algorithm.                                                 |

My central recommendation is to move from conjectural global geometry to a completed low-codimension theorem and algorithm, while proving the first two general incidence theorems in parallel.

The project does not need a solution of the full type-control conjecture before it can make a substantial mathematical contribution. The exact spectral reduction, the bounded-degree certificate, the corrected lifting geometry, and a rigorous \\(c=2\\) result already form a coherent and defensible body of work.

The one correction I would insist on immediately is the replacement of \\(K_0/V\\) by the ambient quotient \\(\mathcal X/V\\) in the exact fibre theorem, unless \\(A\\)-invariance of \\(K_0\\) has been separately proved. Once that is fixed, I would regard the current programme as mathematically well-directed and ready to move into theorem consolidation and low-codimension algorithm development.