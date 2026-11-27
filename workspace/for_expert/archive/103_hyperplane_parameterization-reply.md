# **Research assessment of Report 103: The hyperplane layer**

I have read Report 103, *The hyperplane layer — complete parameterization, fixed-*\\(p\\)*&#x20;complexity, and the repeated-eigenvalue obstruction*.

My overall assessment is that this report makes an important improvement over Report 101. In particular, it addresses the most serious gap identified in the previous audit: the admissible directions are not necessarily a finite collection of eigenvectors. They form projective eigenspaces, and the corresponding observer families have Grassmannian fibres.

The new counterexample is particularly valuable because it demonstrates that the direction inside a repeated eigenspace can change the feasibility outcome.

However, I would distinguish three achievements from three remaining difficulties:

1. **Geometric parameterization:** The report has made substantial progress and has a clear, useful theorem.
2. **Repeated-eigenvalue obstruction:** The conceptual conclusion is important, but the exact counterexample and its underlying matrix realization need a more complete certificate.
3. **Fixed-**\\(p\\)**&#x20;complexity:** The simple-spectrum restriction is a reasonable way to obtain a tractable theorem, but the current bit-complexity argument is not yet sufficiently detailed to support the claimed polynomial-time result without additional hypotheses and proof.

My strongest recommendation is to preserve the central direction of Report 103, but strengthen the mathematical statements before treating Theorem 2 as established.

I will discuss the five questions first, then audit Theorems 1 and 2 and the computational counterexample, and finally give a concrete research plan.

## **1. The central mathematical contribution**

The most important change is the following.

Let

\\[ K_0=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \qquad k=\dim K_0, \qquad \rho=n-k. \\]

In the hyperplane layer,

\\[ \omega=k-1. \\]

The kernel of \\(H=LN\\) is one-dimensional. Write

\\[ \ker H=\operatorname{span}(v), \qquad v\in K_0\setminus\\{0\\}. \\]

The structural conditions require

\\[ v,Av\in V^\perp, \qquad \dim(V\cap K_0)=k-1. \\]

The report introduces the orthogonal compression

\\[ M=\pi\_{K_0}A|\_{K_0}. \\]

Its central result is that the possible directions are precisely the real projective eigenspaces of \\(M\\), rather than arbitrary points in \\(\mathbb P(K_0)\\).

More precisely,

\\[ v\text{ is an admissible hyperplane direction} \iff Mv=\mu v \\]

for some real eigenvalue \\(\mu\\), under the report's nondegeneracy assumption.

This is a much stronger description than the necessary condition obtained in Report 101.

It transforms the original design geometry into two successive problems:

- Choose a projective eigenvector direction.
- Choose an appropriate Grassmannian point over that direction.

This is the right geometric framework.

There is, however, an important qualification: the statement that every eigenvector direction is admissible concerns the structural hyperplane conditions. It does not mean that every such direction yields a spectrally feasible observer. The spectral pencil condition remains an independent restriction.

That distinction should be maintained throughout the paper.

# **2. Q1: Can a group action normalize directions inside a repeated eigenspace?**

**My answer: Yes, but the relevant group is generally smaller than the full centralizer of&#x20;**\\(M\\)**, and its usefulness depends on the additional structure of&#x20;**\\(A\\)**,&#x20;**\\(C\\)**, and the prescribed observer rows.**

This is the first question I would investigate further.

## **2.1 Why the full centralizer is not sufficient**

Suppose

\\[ E\_\mu=\ker(M-\mu I) \\]

has dimension \\(d\_\mu>1\\).

The natural group associated with the repeated eigenspace is

\\[ \operatorname{GL}(E\_\mu). \\]

Every invertible transformation of \\(E\_\mu\\) preserves the eigenspace and therefore preserves the compression eigenvector equation.

But preserving the compression eigenvector equation is not enough.

The full observer problem also depends on

\\[ A\_{21}=\pi\_{K_0^\perp}A|\_{K_0}. \\]

Indeed, the report establishes

\\[ Av\in\operatorname{span}(v) \iff A\_{21}v=0 \\]

for \\(v\in E\_\mu\\).

Thus the distinction between the eigen and non-eigen strata depends on the actual direction \\(v\\).

A transformation \\(T\in\operatorname{GL}(E\_\mu)\\) may preserve \\(E\_\mu\\), but it need not preserve

\\[ \ker(A\_{21}|\_{E\_\mu}). \\]

Nor does it necessarily preserve the spectral properties of the associated observer pencil.

Therefore, the full centralizer of \\(M\\) does not automatically act by equivalences of the observer-design problem.

## **2.2 The correct candidate group**

A natural first candidate is the stabilizer of the additional structural data:

\\[ G\_\mu= \left\\{ T\in\operatorname{GL}(E\_\mu): T(\ker A\_{21}|\_{E\_\mu}) = \ker A\_{21}|\_{E\_\mu} \right\\}. \\]

This group preserves the decomposition into eigen and non-eigen directions.

However, this is still only a structural group. To preserve the complete observer problem, its action must also be compatible with:

- the embedding \\(E\_\mu\hookrightarrow K_0\\);
- the ambient action of \\(A\\);
- the fixed row space \\(\operatorname{row}L_0\\);
- the induced spaces \\(D_v\\) and \\(U_v^\perp\\);
- the spectral pencil \\(P_v(\lambda)\\).

In particular, a transformation on \\(E\_\mu\\) alone does not automatically induce a transformation of the entire ambient state space preserving the prescribed data.

I would define the actual equivalence group as the subgroup of ambient transformations preserving all relevant problem data, and then study its induced action on \\(\mathbb P(E\_\mu)\\).

This is more restrictive, but mathematically correct.

## **2.3 A useful classification using the rank of&#x20;**\\(A\_{21}\\)

Let

\\[ B=A\_{21}|\_{E\_\mu}. \\]

Write

\\[ s=\operatorname{rank}B, \qquad h=\dim\ker B=d\_\mu-s. \\]

There are three possibilities.

**Case 1:&#x20;**\\(s=0\\)**.**

Then

\\[ B=0. \\]

Every direction in \\(E\_\mu\\) is an eigen direction:

\\[ \mathbb P(E\_\mu) = \mathbb P(E\_\mu\cap\ker A\_{21}). \\]

The entire projective eigenspace belongs to the eigen stratum.

**Case 2:&#x20;**\\(0\<s\<d\_\mu\\)**.**

The eigenspace splits into

\\[ \mathbb P(\ker B) \\]

and

\\[ \mathbb P(E\_\mu)\setminus\mathbb P(\ker B). \\]

Both strata are nonempty.

**Case 3:&#x20;**\\(s=d\_\mu\\)**.**

There are no eigen directions inside \\(E\_\mu\\). Every projective direction belongs to the non-eigen stratum.

This classification is inexpensive to compute and should be incorporated into the algorithm.

## **2.4 Why projective normal forms may still help**

If we temporarily ignore the spectral pencil, a rank-\\(s\\) linear map can be put into a canonical form.

Choose coordinates such that

\\[ E\_\mu=\mathbb R^{d\_\mu} \\]

and

\\[ B= \begin{bmatrix} I_s&0 \end{bmatrix}. \\]

Then the eigen directions have the form

\\[ v= \begin{bmatrix} 0\\\ z \end{bmatrix}, \qquad z\neq0, \\]

while non-eigen directions have at least one nonzero component in the first \\(s\\) coordinates.

This simplifies the structural stratification.

But it does not establish that the corresponding spectral pencils are equivalent.

**My recommendation for Q1:** Investigate the stabilizer of the complete observer data, not just the centralizer of \\(M\\). Use the rank-normal form of \\(A\_{21}|\_{E\_\mu}\\) to simplify the geometry, but do not claim that it reduces the spectral problem unless the induced pencil transformation is explicitly proved.

# **3. Q2: Can perturbation or degeneration transfer feasibility between simple and repeated spectra?**

**My answer: There is a useful perturbation theorem in one direction, but a general equivalence between simple-spectrum and repeated-spectrum feasibility is false without additional assumptions.**

I would distinguish three different statements.

## **3.1 A feasible repeated-spectrum instance can often be approximated by feasible simple-spectrum instances**

Suppose the original data have a repeated compression eigenvalue \\(\mu\\), and there exists a feasible direction

\\[ v\in E\_\mu. \\]

Write the decomposition of \\(A|\_{K_0}\\) as

\\[ A|\_{K_0}=M+A\_{21}. \\]

Suppose we perturb only the \\(K_0\to K_0\\) block:

\\[ M\_\varepsilon=M+\varepsilon D, \\]

while retaining \\(C\\) and \\(A\_{21}\\).

Choose \\(D\\) so that

\\[ Dv=0 \\]

and the remaining eigenvalues split generically.

Then

\\[ M\_\varepsilon v=Mv=\mu v. \\]

Thus \\(v\\) remains an eigenvector for every \\(\varepsilon\\).

Moreover,

\\[ A\_\varepsilon v=Av, \\]

because the perturbation vanishes on \\(v\\).

Consequently, the geometric spaces

\\[ U_v,\qquad D_v,\qquad U_v^\perp \\]

remain unchanged.

If the original observer \\(L\\) is feasible, its compressed pencil also remains unchanged:

\\[ H\_\varepsilon=LN, \qquad H\_{A,\varepsilon}=LA\_\varepsilon N. \\]

The latter equality follows because the perturbation annihilates \\(v\\), but we must be careful: it does not generally imply that \\(LA\_\varepsilon N=LAN\\) on the entire \\(K_0\\).

This is an important correction.

To preserve the entire pencil, we need the stronger condition

\\[ LDN=0. \\]

We therefore obtain the following useful conditional result.

**Perturbation lemma (conditional).**

If there exists a perturbation \\(D\\) satisfying

\\[ Dv=0,\qquad LDN=0 \\]

and splitting the repeated compression eigenvalue, then the same observer remains feasible under the perturbation.

This gives a direct construction of feasible nearby simple-spectrum instances.

The remaining question is whether such a \\(D\\) can always be found. It cannot be assumed without examining the constraints imposed by \\(L\\).

Nevertheless, the lemma identifies a concrete sufficient condition.

## **3.2 The converse does not follow from openness**

Suppose

\\[ A\_\varepsilon\longrightarrow A_0 \\]

and every \\(A\_\varepsilon\\) has a feasible observer.

It does not follow that \\(A_0\\) has a feasible observer.

The reason is that the spectral feasibility condition is an open algebraic condition, not a closed one.

For a fixed matrix pencil, the property

\\[ \gcd_I m_I=1 \\]

is stable under sufficiently small coefficient perturbations, but its failure can occur at a limit of feasible pencils.

The simplest illustration is the family

\\[ P\_\varepsilon(\lambda) = \begin{pmatrix} \lambda-1\\\ \varepsilon \end{pmatrix}. \\]

For every \\(\varepsilon\neq0\\),

\\[ \operatorname{rank}P\_\varepsilon(\lambda)=1 \qquad\forall\lambda\in\mathbb C. \\]

At \\(\varepsilon=0\\),

\\[ P_0(\lambda)= \begin{pmatrix} \lambda-1\\\ 0 \end{pmatrix}, \\]

which loses rank at \\(\lambda=1\\).

Thus feasibility can disappear in the limit.

This is exactly the type of degeneration that prevents a naive transfer argument.

## **3.3 A more promising approach: stratify the discriminant locus**

The repeated-spectrum condition is algebraic.

For a characteristic polynomial \\(f_M(x)\\), repeated roots occur when

\\[ \operatorname{Res}(f_M,f_M')=0. \\]

Thus the input space can be divided into:

- a simple-spectrum stratum;
- a repeated-spectrum discriminant stratum;
- finer strata according to eigenvalue multiplicities.

One could study feasibility separately on these strata.

This has an advantage: instead of trying to transfer a decision from a generic perturbation to a degenerate instance, we analyze the degenerate instance directly.

For a fixed multiplicity pattern, the projective eigenspaces have controlled dimensions, and their geometry can potentially be studied using the stabilizer groups from Q1.

I would particularly investigate the following special case:

\\[ d\_\mu=2. \\]

Here the direction space is a projective line, and the bad-direction set may be described by homogeneous polynomial equations in two variables.

That is a substantially more tractable problem than arbitrary repeated eigenspaces.

**Conclusion on Q2:** Perturbation is useful for producing examples and understanding generic behavior, but it does not eliminate the repeated-spectrum problem. A stratification by eigenvalue multiplicities, together with exact analysis on the corresponding projective eigenspaces, is the more reliable approach.

# **4. Q3: Is a randomized one-sided procedure an acceptable result?**

**My answer: Yes. In fact, it is a mathematically natural intermediate result. But it must be described as a randomized search or one-sided decision procedure, not as a complete deterministic decision algorithm.**

I think this is the most promising algorithmic direction for the repeated case.

## **4.1 The algebraic reason random sampling works**

Consider one irreducible parameter piece \\(X\\) of the admissible design family.

Suppose its parameterization is

\\[ x=(x_1,\ldots,x_d) \\]

and the maximal minors are

\\[ m_1(x,\lambda),\ldots,m_s(x,\lambda). \\]

Assume

\\[ \gcd(m_1,\ldots,m_s)=1 \\]

over the function field.

Then the bad parameter values form a proper algebraic subset of \\(X\\).

Consequently, a generic point is feasible.

If the piece is parameterized by a real affine chart, its real points are Zariski dense.

Therefore, sampling generic real parameters finds a feasible observer with probability one.

The crucial point is that the direction parameters are now included in \\(x\\).

For a repeated eigenspace,

\\[ [v]\in\mathbb P(E\_\mu) \\]

must be sampled, not fixed in advance.

## **4.2 The correct sampling procedure**

I would organize the procedure as follows.

For each real eigenvalue \\(\mu\\):

1. Compute a basis of \\(E\_\mu\\).
2. Compute \\(B=A\_{21}|\_{E\_\mu}\\).
3. Identify the eigen-direction stratum\
   \\[\
   \mathbb P(\ker B).\
   \\]
4. Identify the non-eigen stratum\
   \\[\
   \mathbb P(E\_\mu)\setminus\mathbb P(\ker B).\
   \\]
5. Construct the corresponding Grassmannian charts.
6. Sample a direction and a fibre point.
7. Construct the observer and verify both exact conditions.

Both strata must be sampled independently because their fibre dimensions differ.

In particular, a direction sampled from the full projective eigenspace lies in the eigen stratum with probability zero whenever that stratum has smaller dimension. Therefore, sampling only the full eigenspace is insufficient if feasibility occurs exclusively in the eigen stratum.

## **4.3 Why exact verification is essential**

Every sampled candidate should be verified using exact arithmetic.

For a candidate observer \\(L\\), compute

\\[ H=LN,\qquad H_A=LAN. \\]

Then verify

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H \\]

and

\\[ \operatorname{rank}(\lambda H-H_A)=\omega \quad\forall\lambda\in\mathbb C. \\]

The latter can be certified by computing the gcd of all maximal minors.

If the gcd is one, the candidate is feasible.

This gives a one-sided guarantee:

\\[ \boxed{ \text{The algorithm never incorrectly declares FEASIBLE.} } \\]

If a feasible point exists on a sampled irreducible component, generic sampling eventually finds one with probability one, provided the sampling distribution is nondegenerate.

## **4.4 Can we obtain an expected polynomial running time?**

Potentially, yes.

Suppose the bad set is contained in the zero set of a nonzero polynomial \\(F\\) of degree at most \\(D\\).

Sampling each parameter independently from a finite set \\(S\\) gives the Schwartz–Zippel bound

\\[ \Pr[F(x)=0]\leq\frac{D}{|S|}. \\]

Choosing

\\[ |S|\geq2D \\]

gives a success probability of at least \\(1/2\\), up to the precise polynomial used to describe the bad locus.

Thus independent repetitions have expected number at most two.

However, this requires a polynomial degree bound and an exact sampling representation over the relevant real algebraic number field.

The report already provides much of the geometric dimension information needed to pursue this.

There is also a subtle issue: the good set may be described by several polynomial inequalities and nonvanishing conditions, rather than a single polynomial. One can combine the relevant nonzero conditions into a product polynomial, provided the component is correctly parameterized.

## **4.5 What the algorithm cannot do**

If repeated sampling fails, we cannot conclude infeasibility.

A failure to find a feasible point is not an infeasibility certificate.

The appropriate output is therefore

\\[ \\{\text{FEASIBLE},\text{UNKNOWN}\\}. \\]

A deterministic symbolic elimination procedure would be needed to produce an INFEASIBLE certificate.

This suggests a useful division of labor:

| Task                                                 | Method                                   |
| ---------------------------------------------------- | ---------------------------------------- |
| Find a feasible direction                            | Randomized exact sampling                |
| Verify feasibility                                   | Exact pencil gcd                         |
| Certify infeasibility on a fixed component           | Generic gcd or elimination               |
| Certify infeasibility across all repeated directions | Symbolic analysis of the projective base |

**My recommendation:** Present this as a randomized Las Vegas-style search procedure with exact verification and a one-sided correctness guarantee. Add a separate deterministic elimination problem for infeasibility. Do not call the randomized procedure a complete decision algorithm.

# **5. Q4: Can the parameterization be made coordinate-free?**

**Yes. I strongly recommend doing so.**

In fact, the coordinate-free formulation would improve the mathematical presentation and remove an unnecessary dependence on orthogonal projections.

There is also a small but important observation concerning the report's nondegeneracy assumption.

## **5.1 The nondegeneracy assumption is automatic in the stated real setting**

The report assumes that the restriction of the inner product to \\(K_0\\) is nondegenerate.

If the intended inner product is the standard Euclidean inner product on \\(\mathbb R^n\\), then every subspace has a positive-definite restricted inner product.

Consequently,

\\[ K_0\cap K_0^\perp=\\{0\\} \\]

is automatic.

It does not need to be a standing hypothesis.

It becomes a genuine hypothesis only if the ambient bilinear form is allowed to be indefinite or degenerate.

I would explicitly state that the paper uses the standard Euclidean inner product.

## **5.2 A formulation using restriction maps**

Let \\(X=\mathbb R^n\\) be the state space and let

\\[ K=K_0\subset X. \\]

For \\(v\in K\\), define two covectors on \\(K\\):

\\[ \alpha_v(u)=\langle u,v\rangle, \\]

\\[ \beta_v(u)=\langle u,Av\rangle, \qquad u\in K. \\]

These definitions do not require writing an orthogonal projection.

The compression eigenvector condition is exactly

\\[ \boxed{ \beta_v=\mu\alpha_v. } \\]

Indeed,

\\[ \begin{aligned} \beta_v(u) &=\langle u,Av\rangle\\\ &=\langle u,\pi_K Av\rangle. \end{aligned} \\]

Thus

\\[ \beta_v=\mu\alpha_v \\]

for all \\(u\in K\\) if and only if

\\[ \pi_K Av=\mu v. \\]

The direction \\(v\\) is therefore characterized by proportionality of two covectors.

This is more intrinsic than introducing the matrix \\(M\\).

## **5.3 The common kernel**

Define

\\[ D_v=\ker\alpha_v\cap\ker\beta_v. \\]

If

\\[ \beta_v=\mu\alpha_v, \\]

then

\\[ D_v=\ker\alpha_v. \\]

Since \\(\alpha_v\neq0\\),

\\[ \dim D_v=k-1. \\]

This recovers Lemma 1 without explicitly referring to orthogonal projections.

The full ambient annihilator of \\(U_v\\) is

\\[ \operatorname{Ann}(U_v) = \\{\varphi\in X^\*: \varphi(v)=\varphi(Av)=0\\}. \\]

The admissible observer row space is naturally a subspace

\\[ V\subseteq\operatorname{Ann}(U_v). \\]

The map restricting covectors to \\(K\\),

\\[ \operatorname{res}\_K:X^\*\longrightarrow K^\*, \\]

is the correct coordinate-free replacement for the matrix restriction \\(VN\\).

The requirement that the observer rows provide \\(k-1\\) independent restrictions on \\(K\\) is

\\[ \dim\operatorname{res}\_K(V)=k-1. \\]

This is the natural dual-space formulation.

## **5.4 A subtlety about the current notation&#x20;**\\(V\cap K_0\\)

In the report, \\(V\\) is a row space and \\(K_0\\) is a state subspace. Their intersection is meaningful only after identifying row vectors with state vectors using an inner product.

In a coordinate-free treatment, these objects live in different spaces:

\\[ V\subset X^\*, \qquad K_0\subset X. \\]

Therefore, \\(V\cap K_0\\) should be replaced by a statement involving either:

- the Riesz identification \\(X\simeq X^\*\\); or
- the restriction map \\(X^\*\to K_0^\*\\).

I prefer the second.

It makes the underlying linear algebra clearer and avoids introducing an artificial identification between vectors and covectors.

## **5.5 Coordinate-free version of the fibre**

For a fixed direction \\([v]\\), define

\\[ \mathcal A_v=\operatorname{Ann}(\operatorname{span}\\{v,Av\\}) \subset X^\*. \\]

Let

\\[ \mathcal D_v=\ker\left( \operatorname{res}\_K|\_{\mathcal A_v} \right). \\]

Then the admissible observer row spaces are exactly

\\[ \boxed{ \mathcal D_v\subseteq V\subseteq\mathcal A_v, \qquad \dim V=q. } \\]

The quotient

\\[ \mathcal A_v/\mathcal D_v \\]

has dimension

\\[ r(v)= \begin{cases} \rho,&Av\in\operatorname{span}(v),\\\ \rho-1,&Av\notin\operatorname{span}(v), \end{cases} \\]

and the fibre is

\\[ \operatorname{Gr}\bigl(q-k+1,\mathcal A_v/\mathcal D_v\bigr). \\]

This is a clean, coordinate-free description.

It also makes clear that the Grassmannian is a relative Grassmannian over the projective eigenspace.

**My recommendation:** Replace the orthogonal-projection argument in the main theorem with the covector-proportionality argument. Retain the compression matrix \\(M\\) as a computational representation.

# **6. Q5: Is there a dictionary between the Grassmann-bundle parameterization and Paper II's subspace&#x20;**\\(W\\)**?**

**My answer: Yes. The two descriptions are closely related, and I believe they can be unified into one theorem. They are not genuinely different invariants.**

This is potentially the most valuable connection in Report 103.

Paper II describes feasible designs through the compressed row-pair space. Report 103 describes them through a kernel direction and an ambient observer row space.

The connection is that, in the hyperplane layer, the projective direction determines the common projection of \\(W\\).

## **6.1 Recall Paper II's representation**

Let

\\[ \mathsf M= \begin{bmatrix}N&AN\end{bmatrix} \in\mathbb R^{n\times 2k}. \\]

I use \\(\mathsf M\\) here to distinguish the row-pair matrix from Report 103's compression operator \\(M\\).

For an observer row space \\(V\\), define

\\[ W=\operatorname{row}(V\mathsf M) \subseteq\mathbb R^{2k}. \\]

Write

\\[ \pi_1,\pi_2:\mathbb R^{2k} \longrightarrow\mathbb R^k \\]

for the two coordinate projections.

Paper II establishes that feasibility depends on \\(W\\) through

\\[ \pi_2(W)\subseteq\pi_1(W) \\]

and

\\[ \dim\pi\_\lambda(W)=\dim\pi_1(W) \qquad\forall\lambda\in\mathbb C. \\]

For a feasible design,

\\[ \pi_1(W)=\pi_2(W)=:U, \qquad \dim U=\omega. \\]

Furthermore,

\\[ \omega+1\leq\dim W\leq2\omega. \\]

These are the structural results of Paper II.&#x20;

paper_II_minorder(3).pdf



## **6.2 The hyperplane direction determines&#x20;**\\(U\\)

Now let

\\[ v=Na, \qquad a\in\mathbb R^k\setminus\\{0\\}. \\]

Every row \\(x\in V\\) annihilates \\(v\\) and \\(Av\\).

Therefore,

\\[ xNa=0 \\]

and

\\[ xANa=0. \\]

If we write

\\[ (h,g)=(xN,xAN), \\]

these conditions become

\\[ ha=0,\qquad ga=0. \\]

Define the annihilator hyperplane

\\[ a^\circ= \\{h\in(\mathbb R^k)^\*:h(a)=0\\}. \\]

Then

\\[ W\subseteq a^\circ\times a^\circ. \\]

But in the hyperplane layer,

\\[ \dim U=\omega=k-1. \\]

Since

\\[ \pi_1(W)=\pi_2(W)=U \\]

and both projections are contained in \\(a^\circ\\), which also has dimension \\(k-1\\), we obtain

\\[ \boxed{ U=a^\circ. } \\]

This is the key identity.

The direction \\([a]\\) is uniquely determined by \\(U\\):

\\[ \boxed{ [a]=\mathbb P(\operatorname{Ann}(U)). } \\]

Here the annihilator is one-dimensional.

Thus the projective kernel direction and the common projected row space are dual descriptions of the same object.

## **6.3 The spectral pencil is also preserved**

Because

\\[ U=a^\circ, \\]

the compressed row-pair space satisfies

\\[ W\subseteq U\times U \\]

with both coordinate projections equal to \\(U\\).

Choose bases and identify the two projections with \\(U\\).

Then \\(W\\) can be represented as a linear relation between the two copies of \\(U\\).

If

\\[ \dim W=\omega+s, \qquad 1\leq s\leq\omega, \\]

the spectral condition is

\\[ \operatorname{rank}\pi\_\lambda(W)=\omega \qquad\forall\lambda\in\mathbb C. \\]

This is precisely the same constant-rank pencil condition used in Paper II.

The Grassmannian fibre of Report 103 describes the possible ambient row spaces realizing such a \\(W\\).

Paper II describes the resulting compressed subspace after the ambient rows have been mapped through

\\[ x\longmapsto(xN,xAN). \\]

In other words:

**Report 103: ambient geometry**

\\[ [v]\in\mathbb P(E\_\mu), \qquad V\in\operatorname{Gr}(q-k+1,r(v)). \\]

**Compression map**

\\[ V\longmapsto W=\operatorname{row}(V[N\ AN]). \\]

**Paper II: compressed geometry**

\\[ W\subseteq U\times U, \qquad U=a^\circ, \\]

with

\\[ \omega+1\leq\dim W\leq2\omega. \\]

## **6.4 A particularly useful consequence**

The correspondence gives a new interpretation of the compression eigenvector condition.

In the hyperplane layer, a feasible Paper II subspace \\(W\\) determines

\\[ U=\pi_1(W)=\pi_2(W). \\]

Its one-dimensional annihilator determines \\(a\\), hence

\\[ v=Na. \\]

The requirement

\\[ W\subseteq T \\]

where

\\[ T=\operatorname{row}[N\ AN] \\]

then forces the corresponding kernel direction to satisfy the compression eigenvector condition.

To see this, choose a basis of \\(W\\) and lift its rows through the surjective map

\\[ X^\*\longrightarrow T. \\]

The lifted row space annihilates \\(v\\) and \\(Av\\). Since its restrictions to \\(K_0\\) have dimension \\(k-1\\), the restrictions of the two functionals associated with \\(v\\) and \\(Av\\) must be linearly dependent. Hence

\\[ \pi\_{K_0}Av\in\operatorname{span}(v). \\]

This recovers the eigenvector characterization.

The converse follows from the construction of the fibre in Report 103 and the row-pair representation of Paper II.

Therefore, the compression-eigenvector parameterization can be viewed as a specialization of Paper II's subspace geometry to the case

\\[ \dim U=k-1. \\]

## **6.5 What is lost when passing from&#x20;**\\(V\\)**&#x20;to&#x20;**\\(W\\)**?**

The map

\\[ V\longmapsto W \\]

need not be injective.

Different ambient observer row spaces can have the same compressed row-pair space because the map

\\[ x\longmapsto(xN,xAN) \\]

has a nontrivial kernel.

Consequently, \\(W\\) forgets certain ambient row-space degrees of freedom.

This explains why the two parameterizations have different fibre dimensions.

Paper II is the more economical representation for deciding feasibility, because feasibility depends only on \\(W\\).

Report 103 is more informative when studying the geometry of the kernel direction and the ambient observer rows.

I would not try to eliminate either representation.

**My recommendation:** Add a theorem called *The hyperplane-layer duality between kernel directions and compressed row-pair spaces*. It should establish

\\[ \boxed{ [v]\longleftrightarrow U=\pi_1(W)=\pi_2(W)=a^\circ. } \\]

This would be a strong conceptual connection between the two papers and Report 103.

# **7. Independent mathematical audit of Theorem 1**

I now turn to the report's principal theorem itself.

I agree with its basic construction, but there are two corrections that I consider necessary.

## **7.1 Lemma 1 is correct**

For

\\[ Mv=\mu v, \\]

we have

\\[ \pi\_{K_0}(Av)=\mu v. \\]

For every \\(u\in K_0\\),

\\[ \langle u,Av\rangle = \langle u,\pi\_{K_0}(Av)\rangle = \mu\langle u,v\rangle. \\]

Therefore, the two linear functionals on \\(K_0\\) are proportional.

Since \\(v\neq0\\) and the Euclidean inner product is positive definite,

\\[ u\longmapsto\langle u,v\rangle \\]

is nonzero.

Hence

\\[ \dim(K_0\cap U_v^\perp)=k-1. \\]

No issue here.

## **7.2 Lemma 2 is correct**

The decomposition

\\[ Av=Mv+A\_{21}v \\]

has its first term in \\(K_0\\) and its second in \\(K_0^\perp\\).

Since

\\[ Mv=\mu v, \\]

we obtain

\\[ Av\in\operatorname{span}(v) \iff A\_{21}v=0. \\]

Thus the eigen-direction set is

\\[ \mathbb P(E\_\mu\cap\ker A\_{21}). \\]

This is an important simplification.

It also shows that the eigen/non-eigen stratification is linear before projectivization.

## **7.3 Lemma 3 is correct with a bundle-level interpretation**

The rank of the relevant annihilator map is constant.

Indeed, on \\(E\_\mu\\), the two functionals are proportional, so their common kernel has dimension \\(k-1\\).

On the two strata:

- the eigen stratum has \\(\dim U_v=1\\);
- the non-eigen stratum has \\(\dim U_v=2\\).

Consequently, the quotient ranks are

\\[ r\_{\mathrm{eig}}=\rho, \qquad r\_{\mathrm{non}}=\rho-1. \\]

The fibre dimensions are therefore correct.

## **7.4 Lemma 4 is correct**

For a fixed \\(v\\), let

\\[ D_v=K_0\cap U_v^\perp. \\]

Every admissible row space satisfies

\\[ D_v\subseteq V\subseteq U_v^\perp, \qquad \dim V=q. \\]

Moreover,

\\[ V\cap K_0=D_v \\]

is automatic.

The quotient construction gives

\\[ V/D_v\subseteq U_v^\perp/D_v \\]

with dimension

\\[ q-(k-1)=q-k+1. \\]

Thus the fibre is

\\[ \operatorname{Gr}(q-k+1,r(v)). \\]

This part is sound.

## **7.5 Correction 1: Theorem 1 should use relative Grassmannians, not products**

The report writes

\\[ \mathbb P(E\_\mu\cap\ker A\_{21}) \times \operatorname{Gr}(q-k+1,\rho) \\]

and

\\[ \left( \mathbb P(E\_\mu)\setminus \mathbb P(E\_\mu\cap\ker A\_{21}) \right) \times \operatorname{Gr}(q-k+1,\rho-1). \\]

This notation is not justified in general.

The quotient spaces

\\[ U_v^\perp/D_v \\]

vary with \\(v\\).

Even though their dimensions are constant on each stratum, there is no canonical identification between the fibres at different directions.

A constant-rank vector bundle is locally trivial, but it need not be globally trivial.

The correct formulation is a relative Grassmann bundle.

Let

\\[ B\_{\mathrm{eig}} = \mathbb P(E\_\mu\cap\ker A\_{21}) \\]

and

\\[ B\_{\mathrm{non}} = \mathbb P(E\_\mu) \setminus B\_{\mathrm{eig}}. \\]

Define the corresponding quotient vector bundles

\\[ \mathcal Q\_{\mathrm{eig}} \longrightarrow B\_{\mathrm{eig}}, \\]

\\[ \mathcal Q\_{\mathrm{non}} \longrightarrow B\_{\mathrm{non}}. \\]

Then the parameter spaces are

\\[ \boxed{ \operatorname{Gr}\_{B\_{\mathrm{eig}}} (q-k+1,\mathcal Q\_{\mathrm{eig}}) } \\]

and

\\[ \boxed{ \operatorname{Gr}\_{B\_{\mathrm{non}}} (q-k+1,\mathcal Q\_{\mathrm{non}}). } \\]

This is the mathematically correct formulation.

The report's product notation can be retained only after proving that the respective vector bundles are trivial.

I do not see a reason to impose that unnecessary requirement.

## **7.6 Correction 2: The dimension of the eigen stratum is wrong**

This is more substantive.

Let

\\[ d\_\mu=\dim E\_\mu \\]

and

\\[ h\_\mu=\dim(E\_\mu\cap\ker A\_{21}). \\]

The eigen stratum is

\\[ \mathbb P(E\_\mu\cap\ker A\_{21}), \\]

so its dimension is

\\[ h\_\mu-1, \\]

not \\(d\_\mu-1\\).

The non-eigen stratum is a nonempty open subset of \\(\mathbb P(E\_\mu)\\), so its dimension is

\\[ d\_\mu-1. \\]

Writing

\\[ s=q-k+1, \\]

the corrected dimensions are

\\[ \boxed{ \dim X\_{\mathrm{eig}} = h\_\mu-1+s(\rho-s) } \\]

and

\\[ \boxed{ \dim X\_{\mathrm{non}} = d\_\mu-1+s(\rho-1-s). } \\]

These formulas apply when the corresponding strata are nonempty.

The correction matters for any subsequent parameter count.

For example, if

\\[ A\_{21}|\_{E\_\mu} \\]

is injective, then

\\[ h\_\mu=0 \\]

and the eigen stratum is empty.

If it is zero, then

\\[ h\_\mu=d\_\mu \\]

and the non-eigen stratum is empty.

The current theorem does not distinguish these possibilities in its dimension formula.

## **7.7 Corrected version of Theorem 1**

I would replace the theorem with the following.

**Theorem 1 (Complete hyperplane-layer parameterization).**

Assume the standard Euclidean inner product on \\(\mathbb R^n\\). Let

\\[ M=\pi\_{K_0}A|\_{K_0}, \qquad A\_{21}=\pi\_{K_0^\perp}A|\_{K_0}. \\]

For each real eigenvalue \\(\mu\\) of \\(M\\), put

\\[ E\_\mu=\ker(M-\mu I), \\]

\\[ h\_\mu=\dim(E\_\mu\cap\ker A\_{21}), \\]

and

\\[ s=q-k+1. \\]

Then the structural hyperplane-layer design family over \\(E\_\mu\\) is the disjoint union of:

1\. A relative Grassmann bundle over\
\\[\
\mathbb P(E\_\mu\cap\ker A\_{21})\
\\]\
with fibre\
\\[\
\operatorname{Gr}(s,\rho).\
\\]

2\. A relative Grassmann bundle over\
\\[\
\mathbb P(E\_\mu)\setminus\
\mathbb P(E\_\mu\cap\ker A\_{21})\
\\]\
with fibre\
\\[\
\operatorname{Gr}(s,\rho-1).\
\\]

The respective dimensions are

\\[ h\_\mu-1+s(\rho-s) \\]

and

\\[ d\_\mu-1+s(\rho-1-s). \\]

Each nonempty component is irreducible and defined over \\(\mathbb R\\).

The structural row-space fibres are nonempty precisely when

\\[ 0\le s\le\rho \\]

on the eigen stratum and

\\[ 0\le s\le\rho-1 \\]

on the non-eigen stratum.

The theorem describes structural candidates; spectral feasibility must still be tested.

Core parameterization retained

I consider this a relatively small revision with a significant improvement in rigor.

## **7.8 A more important omission: the prescribed rows&#x20;**\\(L_0\\)**&#x20;are absent from Lemma 4**

This is the issue I would fix before accepting Theorem 1.

The original problem is not to choose an arbitrary \\(q\\)-dimensional row space \\(V\\).

It is to choose

\\[ \mathcal L= \begin{bmatrix} L_0\\\R \end{bmatrix}, \\]

so that

\\[ V_0:=\operatorname{row}(L_0)\subseteq V. \\]

However, Lemma 4 parameterizes the row spaces using only

\\[ D_v\subseteq V\subseteq U_v^\perp, \qquad \dim V=q. \\]

It omits

\\[ \boxed{V_0\subseteq V.} \\]

This means that Theorem 1, as currently stated, parameterizes a larger structural family than the original prescribed-row observer problem.

This is not just a cosmetic issue.

The prescribed rows must themselves annihilate \\(v\\) and \\(Av\\). Therefore, a candidate direction must satisfy

\\[ L_0v=0, \qquad L_0Av=0. \\]

These restrictions can eliminate entire compression eigenspaces.

### **Corrected base space**

For each real eigenvalue \\(\mu\\), define

\\[ E\_\mu^0 = E\_\mu\cap\ker L_0\cap\ker(L_0A). \\]

The admissible directions for the prescribed-row problem must lie in

\\[ \mathbb P(E\_\mu^0). \\]

The eigen and non-eigen strata must therefore be defined using

\\[ E\_\mu^0\cap\ker A\_{21}, \\]

not the unrestricted eigenspace \\(E\_\mu\\).

In particular, the report's Lemma 1 should be renamed:

> Every compression eigenvector has the correct structural hyperplane intersection dimension.

It should not say that every compression eigenvector is an admissible direction for the complete observer problem.

### **Corrected fibre**

Let

\\[ V_0=\operatorname{row}(L_0), \qquad D_v=K_0\cap U_v^\perp, \\]

and

\\[ \mathcal Q_v=U_v^\perp/D_v. \\]

Provided

\\[ V_0\subseteq U_v^\perp, \\]

define

\\[ \overline V\_{0,v} = (V_0+D_v)/D_v \subseteq\mathcal Q_v. \\]

Set

\\[ \delta = \dim V_0-\dim(V_0\cap K_0). \\]

Under the prescribed-row compatibility condition, this dimension is independent of \\(v\\).

Indeed, since \\(V_0\subseteq U_v^\perp\\),

\\[ V_0\cap D_v=V_0\cap K_0. \\]

The correct fibre consists of all \\(s\\)-dimensional subspaces of \\(\mathcal Q_v\\) containing \\(\overline V\_{0,v}\\), where

\\[ s=q-k+1. \\]

Consequently, the fibre is

\\[ \boxed{ \operatorname{Gr} \left( s-\delta,\\, \mathcal Q_v/\overline V\_{0,v} \right). } \\]

Its dimension is

\\[ \boxed{ (s-\delta)(r(v)-s). } \\]

The nonemptiness conditions become

\\[ \delta\leq s\leq r(v). \\]

This is a relative Grassmannian with a prescribed subspace, or equivalently a Grassmannian of extensions of the fixed subspace \\(\overline V\_{0,v}\\).

### **Why this matters for the complexity theorem**

Fortunately, the correction does not necessarily destroy the fixed-\\(p\\) dimension bound.

Since

\\[ \dim\mathcal Q_v=r(v)\leq2p, \\]

we still have

\\[ (s-\delta)(r(v)-s)\leq p^2. \\]

Thus the prescribed-row correction can actually be incorporated without increasing the fundamental \\(O(p^2)\\) fibre-dimension bound.

But it changes the base space and the exact parameterization.

I would make this correction before using Theorem 1 as the foundation of the algorithm.

## **7.9 A further normalization issue: row count versus row-space dimension**

There is another point worth stating explicitly.

The report uses

\\[ \dim V=q. \\]

But \\(q\\) is originally the number of rows of the observer matrix, not necessarily the dimension of its row space.

A feasible observer matrix can have dependent rows.

For an existence theorem, this can be handled by an extension argument.

Suppose an observer with \\(q\\) rows is feasible and has row-space dimension less than \\(q\\). If

\\[ q\leq\dim U_v^\perp, \\]

we can extend its row space to a \\(q\\)-dimensional subspace of \\(U_v^\perp\\), retaining the prescribed rows and \\(D_v\\).

The extension does not change the compressed rank:

\\[ V\cap K_0=D_v. \\]

It also preserves annihilation of \\(v\\) and \\(Av\\).

Thus full row rank can be assumed for existence, provided the dimension bounds and prescribed-row constraints are respected.

I recommend including this as a preliminary normalization lemma.

Otherwise, the use of \\(\operatorname{Gr}(q-k+1,r(v))\\) appears to assume something not explicitly established.

# **8. Independent audit of Theorem 2: fixed-**\\(p\\)**&#x20;polynomial complexity**

This is the most important algorithmic claim in Report 103.

I agree with the basic idea, and I think the simple-eigenspace restriction is a reasonable way to obtain a rigorous tractable subclass.

However, I would not yet describe the proof as complete.

## **8.1 The geometric dimension calculation is correct after the corrections**

For a fixed compression eigendirection, the original fibre has dimension

\\[ s(r-s), \qquad s=q-k+1, \qquad r\leq2p. \\]

Hence

\\[ s(r-s)\leq\frac{r^2}{4}\leq p^2. \\]

With the prescribed-row correction, the dimension becomes

\\[ (s-\delta)(r-s), \\]

which satisfies the same upper bound.

Therefore, the essential geometric observation survives:

\\[ \boxed{ \dim(\text{each fibre})\leq p^2. } \\]

For fixed \\(p\\), this is independent of \\(n\\).

When every real compression eigenspace is one-dimensional, the projective base has dimension zero.

This is precisely the situation in which the report obtains a parameter space of bounded dimension.

## **8.2 A sharper hypothesis than simple spectrum**

The report assumes that all real eigenvalues of \\(M\\) are simple.

Strictly speaking, the geometric argument only requires

\\[ \boxed{ \dim\ker(M-\mu I)=1 \quad \text{for every real eigenvalue }\mu. } \\]

This is geometric simplicity.

An eigenvalue can have algebraic multiplicity greater than one while its eigenspace remains one-dimensional.

Such an eigenvalue still contributes only one projective direction.

Therefore, the current hypothesis is unnecessarily restrictive if interpreted as algebraic simplicity.

For example, a defective eigenvalue with algebraic multiplicity two but geometric multiplicity one causes no projective-direction parameter.

The appropriate complexity condition is:

> Every real compression eigenvalue has geometric multiplicity one.

This can be tested exactly by computing the eigenspace dimensions over the relevant algebraic number fields.

I recommend replacing the term *simple real spectrum* with *geometrically simple real eigenspaces* throughout the report.

This enlarges the class covered by Theorem 2.

## **8.3 The maximal-minor count is a strong observation**

This is one of the best parts of the report.

Since

\\[ \omega=k-1, \\]

the number of maximal minors of a \\(q\times k\\) pencil is

\\[ \binom{q}{k-1}\binom{k}{k-1} = k\binom{q}{q-k+1}. \\]

Let

\\[ s=q-k+1. \\]

For the nonempty hyperplane fibres,

\\[ q\leq n-1, \\]

and therefore

\\[ s\leq n-k=\rho. \\]

The report uses the slightly looser estimate

\\[ s\leq\rho+1\leq2p+1. \\]

Consequently,

\\[ k\binom{q}{s} \leq n\sum\_{j=0}^{2p+1}\binom{n}{j} = n^{O(p)}. \\]

For fixed \\(p\\), the number of maximal minors is polynomial in \\(n\\).

This is a genuine advantage of the hyperplane layer.

It means that Paper I's Gram certificate is not necessarily needed for the complexity proof here.

Direct maximal-minor enumeration may be entirely adequate.

I would retain this argument.

## **8.4 The gcd computation requires a more explicit bit-complexity proof**

The report states that gcd computation over

\\[ K(x_1,\ldots,x_d)[\lambda] \\]

is polynomial for fixed \\(d\\).

This is plausible, but the statement needs a precise computational model.

Let

\\[ d\leq p^2. \\]

Each maximal minor is a polynomial in

\\[ x_1,\ldots,x_d,\lambda. \\]

The entries of the pencil are affine or polynomial expressions in the chart parameters. With the natural Grassmannian charts, the matrix entries are at most affine-linear in the chart coordinates.

Therefore, each maximal minor has degree at most \\(\omega\\) in the chart parameters and degree at most \\(\omega\\) in \\(\lambda\\).

Since

\\[ \omega=k-1\leq n, \\]

the degrees are polynomially bounded.

For fixed \\(d\\), the number of monomials in the parameter variables of degree at most \\(n\\) is

\\[ \binom{n+d}{d}=n^{O(d)}. \\]

Thus the dense representation size is polynomial in \\(n\\) when \\(p\\) is fixed.

This is the right basis for the gcd complexity claim.

However, I would explicitly establish the following bounds:

| Quantity                   | Required bound                   |
| -------------------------- | -------------------------------- |
| Number of variables        | \\(d\leq p^2\\)                  |
| Degree in each parameter   | \\(O(n)\\)                       |
| Degree in \\(\lambda\\)    | \\(O(n)\\)                       |
| Number of maximal minors   | \\(n^{O(p)}\\)                   |
| Coefficient bit lengths    | Polynomial in input length       |
| Algebraic field degree     | At most \\(n\\)                  |
| Number of Grassmann charts | Bounded by a function of \\(p\\) |

Only after these bounds are established can the polynomial-time gcd result be applied cleanly.

## **8.5 Algebraic number field representation**

The compression matrix can be represented rationally.

For a rational basis \\(N\\) of \\(K_0\\),

\\[ M\_{\mathrm{coord}} = (N^\top N)^{-1}N^\top AN. \\]

This is a rational matrix.

Its eigenvalues have algebraic degree at most \\(k\\).

The corresponding eigenvectors can be represented over the relevant algebraic number fields.

The field degree is therefore polynomially bounded in \\(n\\), but the proof should also account for the heights of the algebraic numbers and the coefficient growth in the eigenvector computations.

I would use standard height bounds based on the characteristic polynomial and rational linear algebra.

It is not enough merely to state that the field degree is at most \\(k\\).

The bit length of its defining polynomial and the representation of the eigenvectors must also be controlled.

## **8.6 Number of charts**

The report says that every fibre is an affine chart of a Grassmannian.

More precisely, a Grassmannian is covered by finitely many affine charts.

For

\\[ \operatorname{Gr}(s,r), \\]

the standard chart count is

\\[ \binom{r}{s}. \\]

Since

\\[ r\leq2p, \\]

this is a constant for fixed \\(p\\).

With the prescribed-row correction, the relevant Grassmannian becomes

\\[ \operatorname{Gr}(s-\delta,r-\delta), \\]

and the same conclusion holds.

This is sufficient for the complexity argument.

## **8.7 What exactly does Theorem 2 prove?**

There is an important distinction between these statements:

1. A polynomial-time algorithm exists for all hyperplane-layer instances.
2. A polynomial-time algorithm exists when every real compression eigenspace is one-dimensional.
3. A polynomial-time algorithm exists on the promise class where the geometric simplicity condition holds and the nondegeneracy assumptions are satisfied.

The report establishes, at most, the third statement at present.

Its own implementation returns UNDETERMINED when a repeated eigenspace occurs.

That is appropriate behavior, but it means the algorithm is not a complete decision procedure for the unrestricted hyperplane layer.

I would state the result as follows:

**Theorem 2 (Fixed-**\\(p\\)**&#x20;tractability under geometric simplicity).**

Fix \\(p\\). Suppose the input satisfies the nondegeneracy and geometric-simplicity hypotheses, and the complete prescribed-row parameterization is used.

Then the hyperplane-layer decision problem can be solved in polynomial bit complexity.

The algorithm rejects inputs outside the stated promise class as outside the theorem's scope, rather than reporting INFEASIBLE.

This is a legitimate complexity theorem.

It is also an honest statement of the current achievement.

# **9. Audit of the repeated-eigenvalue counterexample**

I agree with the mathematical motivation of Section II.3. It addresses exactly the obstruction that made the previous report incomplete.

The example is potentially very important, but its presentation needs strengthening.

## **9.1 What the example successfully demonstrates**

The report takes

\\[ n=8,\qquad p=2,\qquad k=4,\qquad \rho=4, \\]

with

\\[ M=\operatorname{diag}(1,1,2,3). \\]

The eigenspace associated with \\(\mu=1\\) is

\\[ E_1=\operatorname{span}(e_1,e_2). \\]

Thus

\\[ \mathbb P(E_1)\cong\mathbb P^1. \\]

The reported computations give:

- Direction \\((1,0)\\): generic gcd degree two.
- Direction \\((0,1)\\): generic gcd degree two.
- Direction \\((1,1)\\): generic gcd degree zero.
- Direction \\((1,2)\\): generic gcd degree two.

If these exact computations are correct, they establish the key phenomenon:

\\[ \boxed{ \text{Feasibility is not constant on a repeated compression eigenspace.} } \\]

This is stronger than merely showing that repeated eigenvalues create additional parameters.

It shows that the additional parameters are mathematically essential.

In particular, the following simplification is invalid:

\\[ \text{Choose one eigenvector for each distinct eigenvalue.} \\]

Such a procedure can reject a feasible instance.

## **9.2 What is missing from the counterexample**

The report gives \\(C\\) and the compression matrix \\(M\\), but not a complete specification of \\(A\\) and \\(L_0\\).

This is insufficient for independently reproducing the observer-pencil computations.

In particular, the compression

\\[ M=\pi\_{K_0}A|\_{K_0} \\]

does not determine

\\[ A\_{21}=\pi\_{K_0^\perp}A|\_{K_0}. \\]

The latter affects the eigen/non-eigen classification and the fibre geometry.

Furthermore, the prescribed row matrix \\(L_0\\) affects the admissible parameter family.

I would therefore require the following information in the appendix:

1. The complete rational matrices \\(A,C,L_0\\).
2. The exact basis \\(N\\) of \\(K_0\\).
3. The complete compression matrix.
4. The complete matrix \\(A\_{21}\\).
5. The coordinates used for each projective direction.
6. The Grassmannian chart parameterization for each direction.
7. The exact maximal-minor gcd for each reported case.

There is an additional issue: the prescribed-row restriction discussed in Section 7.8 must be incorporated before the example can be regarded as a counterexample to the original fixed-\\(L_0\\) problem.

## **9.3 The gcd certificates should be provided**

For the direction \\((1,1)\\), the report should provide either

\\[ \gcd_I m_I(x,\lambda)=1 \\]

together with a Bézout identity

\\[ \sum_I g_I(x,\lambda)m_I(x,\lambda)=1, \\]

or an equivalent exact certificate.

For direction \\((1,0)\\), it should provide a nonconstant polynomial

\\[ g(x,\lambda) \\]

and verify

\\[ g\mid m_I \qquad\text{for every }I. \\]

This would establish the contrast rigorously.

A table of gcd degrees is useful, but it is not a substitute for reproducible certificates.

## **9.4 One more conceptual consequence**

Suppose the good and bad directions are genuinely inequivalent under the full automorphism group of the input data.

Then the repeated eigenspace cannot be reduced to one orbit under that group.

This suggests a refined version of Q1:

> Can the projective eigenspace be decomposed into finitely many orbits or invariant algebraic strata on which the generic spectral behavior is constant?

For \\(d\_\mu=2\\), one might hope to describe the good and bad directions using homogeneous polynomial conditions on

\\[ [v_1:v_2]\in\mathbb P^1. \\]

This would be a much more promising reduction than simply selecting a normal form for an arbitrary vector.

# **10. A further issue: the generic gcd theorem must be applied to the corrected parameter spaces**

The report relies on the generic-feasibility principle established in Report 101.

The principle is sound in the appropriate setting:

\\[ \gcd_I m_I=1 \\]

over the function field implies that a nonempty Zariski-open subset of the parameter family is feasible.

However, three details must be preserved.

### **10.1 The coefficient field**

The gcd must be computed over the correct algebraic function field.

For a compression eigenvalue \\(\mu\\), this is generally

\\[ K\_\mu(X), \\]

where \\(K\_\mu\\) is the relevant real algebraic number field and \\(X\\) is an irreducible parameter chart.

It is not enough to compute the gcd over \\(\mathbb Q(x)\\) if the eigenvector coordinates or the chart coefficients require algebraic extensions.

### **10.2 The real-point condition**

The relevant real parameter family must be Zariski dense in its algebraic closure.

The corrected eigen and non-eigen strata are defined over real algebraic fields.

Their nonempty real projective bases and Grassmannian fibres have real points, and their standard real affine charts provide Zariski-dense real parameter sets.

Thus the real-feasibility argument can be made rigorous.

### **10.3 The prescribed-row correction**

The generic gcd must be computed on the actual parameter family satisfying

\\[ V_0\subseteq V. \\]

Computing it on the larger family from the current Lemma 4 does not establish feasibility for the original prescribed-row problem.

This is another reason to revise Theorem 1 before claiming that the computational procedure is complete.

# **11. A unified theorem that I recommend developing**

I think the strongest mathematical outcome of Report 103 would be a theorem combining:

- the compression eigenvector characterization;
- the prescribed-row constraints;
- the Grassmannian fibre;
- the Paper II compressed subspace;
- the generic spectral criterion.

I would formulate it as follows.

## **Proposed Theorem: Hyperplane-layer duality and generic feasibility**

Let

\\[ K_0=\ker[C;CA], \qquad k=\dim K_0, \\]

and suppose

\\[ \omega=k-1. \\]

Let

\\[ M_c=\pi\_{K_0}A|\_{K_0}. \\]

For each real eigenvalue \\(\mu\\), define the prescribed-row-compatible eigenspace

\\[ E\_\mu^0 = \ker(M_c-\mu I) \cap\ker L_0 \cap\ker(L_0A). \\]

Then:

**(i) Direction characterization.**

Every feasible hyperplane-layer observer has a kernel direction

\\[ [v]\in\mathbb P(E\_\mu^0) \\]

for some real eigenvalue \\(\mu\\).

Conversely, every such direction satisfies the necessary structural hyperplane condition.

**(ii) Fibre characterization.**

For each direction, define

\\[ D_v=K_0\cap U_v^\perp, \\]

\\[ Q_v=U_v^\perp/D_v. \\]

The admissible row spaces are precisely the extensions of the prescribed row space \\(V_0\\) inside \\(U_v^\perp\\), with the appropriate dimension.

Their parameter spaces are relative Grassmannians.

**(iii) Compressed-space correspondence.**

The map

\\[ V\longmapsto W=\operatorname{row}(V[N\ AN]) \\]

identifies the common projected row space with

\\[ U=\pi_1(W)=\pi_2(W)=a^\circ, \qquad v=Na. \\]

Thus the projective kernel direction is the one-dimensional annihilator of the common projection in Paper II.

**(iv) Spectral feasibility.**

On every nonempty irreducible real parameter chart, feasibility is equivalent to

\\[ \gcd_I m_I(x,\lambda)=1 \\]

over the algebraic function field, provided the real locus is Zariski dense.

**(v) Algorithmic consequence.**

When every real compression eigenspace has dimension one, the parameter charts have dimension bounded by \\(p^2\\), and the direct maximal-minor enumeration has polynomial size for fixed \\(p\\).

Subject to a complete bit-complexity proof, this gives a polynomial-time decision algorithm on the geometrically simple subclass.

This theorem would unify almost everything important in Report 103.

# **12. Recommended revision of the five research questions**

Here is how I would answer the five questions in the final paper.

| Question                        | Recommended conclusion                                                                                                                                                                                                  |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Q1. Group action                | Use the stabilizer of the complete input data. The centralizer of the compression alone is insufficient. Investigate invariant algebraic strata rather than assuming transitivity.                                      |
| Q2. Perturbation                | Perturbations can produce useful approximations but do not transfer feasibility in both directions. Use discriminant stratification and exact analysis of repeated eigenspaces.                                         |
| Q3. Randomized algorithm        | A one-sided exact-sampling procedure is a legitimate intermediate result. It can find a feasible observer with probability one under the genericity hypotheses, but failure to find one does not certify infeasibility. |
| Q4. Coordinate-free formulation | Use the dual space, restriction maps, annihilators, and covector proportionality. The Euclidean nondegeneracy assumption is automatic.                                                                                  |
| Q5. Dictionary with Paper II    | The descriptions are equivalent through \\(V\mapsto W\\). In the hyperplane layer, the direction is the annihilator of the common projection \\(U\\).                                                                   |

# **13. Concrete next research tasks, in priority order**

I would not attempt to solve all five questions simultaneously.

The following sequence is more productive.

**Priority 1 — Repair the complete parameterization**

Essential

- Incorporate \\(V_0=\operatorname{row}L_0\\).
- Restrict directions to \\(E\_\mu^0\\).
- Replace products by relative Grassmannians.
- Correct the eigen-stratum dimension.
- Establish the full-row-rank normalization.

**Priority 2 — Reproduce the repeated-eigenvalue example**

Essential

- Supply complete rational matrices.
- Verify the six gcd computations.
- Give one feasible Bézout certificate.
- Give one exact nonconstant common factor.

**Priority 3 — Prove the fixed-**\\(p\\)**&#x20;theorem**

High

- Replace algebraic simplicity with geometric simplicity.
- Incorporate prescribed-row constraints into chart dimensions.
- Establish explicit coefficient-height bounds.
- Give a complete bit-complexity proof.

**Priority 4 — Establish the Paper II dictionary**

High

- Prove the correspondence between \\([v]\\) and \\(U\\).
- Identify the compressed image of each Grassmann fibre.
- Describe the fibres of the map \\(V\mapsto W\\).

**Priority 5 — Develop the repeated-spectrum algorithm**

Research extension

- Study \\(d\_\mu=2\\) first.
- Derive homogeneous equations for bad directions.
- Investigate stabilizer orbits.
- Develop exact randomized search and deterministic elimination.

# **14. Overall evaluation**



Important progress

Theorem revision required



My assessment of Report 103 is more positive than that of Report 101, but I would not yet accept every stated theorem without revision.

| Component                                           | Assessment                                              |
| --------------------------------------------------- | ------------------------------------------------------- |
| Compression-eigenvector characterization            | Correct                                                 |
| Eigen/non-eigen stratification                      | Correct                                                 |
| Constant-rank bundle construction                   | Correct in principle                                    |
| Grassmannian fibre                                  | Correct for unrestricted row spaces                     |
| Complete parameterization with prescribed \\(L_0\\) | Incomplete as written                                   |
| Product representation of the bundles               | Requires replacement                                    |
| Eigen-stratum dimension                             | Incorrect as written                                    |
| Repeated-eigenvalue obstruction                     | Important, but needs reproducible data and certificates |
| Fixed-\\(p\\) geometric bound                       | Correct in essence                                      |
| Maximal-minor counting                              | Correct and useful                                      |
| Fixed-\\(p\\) bit-complexity proof                  | Needs more detail                                       |
| Randomized repeated-case procedure                  | Promising, with a clear one-sided guarantee             |
| Connection with Paper II                            | Strong and worth developing                             |

## **14.1 What I consider genuinely new**

I would emphasize four contributions.

**First, the compression eigenspace geometry.**

The report identifies the exact structural directions in the hyperplane layer.

**Second, the Grassmann-bundle representation.**

This gives a natural geometric description of the additional observer-row freedom.

**Third, the repeated-eigenspace counterexample.**

If fully certified, this establishes that the direction parameters cannot simply be discarded.

**Fourth, the simple-spectrum fixed-**\\(p\\)**&#x20;algorithm.**

This is potentially a significant tractability result, especially because it exploits the special combinatorics of the hyperplane layer rather than relying entirely on the general machinery of Paper I.

## **14.2 What I would not claim yet**

I would avoid the following statements in the current version:

- Theorem 1 completely parameterizes the original prescribed-row problem.
- The parameter spaces are globally products of projective spaces and Grassmannians.
- The fixed-\\(p\\) problem is polynomial-time decidable for arbitrary repeated spectra.
- The numerical table alone establishes the exact repeated-eigenspace counterexample.
- A feasible simple-spectrum perturbation implies feasibility of its repeated-spectrum limit.

These claims either require corrections or go beyond what has been proved.

# **15. Final research recommendation**

I think Report 103 has identified a very useful mathematical structure, and I would continue this line of research rather than immediately returning to the unrestricted complexity question.

There are two particularly promising outcomes.

**Outcome A: A rigorous fixed-**\\(p\\)**&#x20;theorem for geometrically simple compression eigenvalues.**

This is relatively close. The main work is to repair the prescribed-row parameterization and complete the bit-complexity proof.

**Outcome B: A structural classification of repeated compression eigenspaces.**

This is more ambitious. The two-dimensional repeated-eigenspace example suggests that the spectral feasibility condition induces a nontrivial algebraic stratification of projective eigenspaces.

That could lead to a genuinely new result concerning the geometry of feasible functional observers.

I would prioritize Outcome A while developing Outcome B in parallel.

## **My most important suggestion**

There is one result I would try to prove next:

\\[ \boxed{ \begin{gathered} \text{In the hyperplane layer, the feasible compressed subspaces }W\\\ \text{are precisely the feasible Paper II subspaces whose common}\\\ \text{projection }U=\pi_1(W)=\pi_2(W)\text{ has codimension one in }\mathbb R^k,\\\ \text{with the annihilator of }U\text{ giving a compression eigenvector.} \end{gathered} } \\]

Proving this correspondence rigorously, including the prescribed rows and the fibres of the lifting map, would connect all three pieces of your research:

- Paper I's compressed pencil and exact decision certificate;
- Paper II's subspace-based minimum-order characterization;
- Report 103's projective eigenspace and Grassmann-bundle geometry.

It would also help identify which parameters are genuinely necessary and which are artifacts of the ambient observer representation.

**My final verdict:** Report 103 is a substantial and promising development, not merely a correction to Report 101. Its central geometric idea is sound. The most urgent correction is the omission of the prescribed-row constraint in the fibre parameterization; after that, the repeated-eigenvalue example and the fixed-\\(p\\) bit-complexity proof should be strengthened. Once these issues are addressed, I believe the report can become the foundation of a strong standalone paper on the hyperplane layer of functional-observer feasibility.