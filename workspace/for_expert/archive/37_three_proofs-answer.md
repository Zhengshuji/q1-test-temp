# Review of `37_three_proofs.md`

The three proofs are a substantial improvement over the earlier versions. My overall assessment is:

- Theorem 1 is correct, including the square factorisation \\(H_A=ZH\\). There is one point in its interpretation that should be stated more carefully: \\(Z|\_{\operatorname{im}H}\\) is generally a map into \\(\mathbb C^q\\), not an endomorphism of \\(\operatorname{im}H\\).
- Theorem 2 is correct under its stated algebraic hypotheses. The projective compactification argument is rigorous. Its elimination corollary is also correct, provided the coordinate-ring hypotheses are made explicit.
- Theorem 3's central Bézout equivalence and rank-stratified corollary are correct. The coefficient count \\(2\omega\\) is now correct. However, there is a significant ambiguity or error in the stated number \\(N=\binom q\omega\\): for the original \\(q\times k\\) pencil, the number of all \\(\omega\times\omega\\) minors is\
  \\[\
  \binom q\omega\binom k\omega,\
  \\]\
  not \\(\binom q\omega\\). The shorter count is correct only after explicitly passing to a \\(q\times\omega\\) reduced pencil.
- The degree bounds are correct under the intended affine dependence on \\(R\\), but that dependence should be stated in Theorem 3 rather than left implicit.

The most likely remaining error is therefore not the rank-stratified corollary itself. It is the precise formulation of Theorem 3's minor family and its coefficient-degree hypotheses. I would correct that before the next round.

I will check each theorem independently, then give proposed replacement statements.

## 1. Theorem 1: reduced criterion

### 1.1 The factorisation \\(H_A=ZH\\) is valid

The hypothesis is

\\[ \ker H\subseteq\ker H_A, \qquad H,H_A\in\mathbb C^{q\times k}. \\]

Define a linear map

\\[ T:\operatorname{im}H\longrightarrow\mathbb C^q \\]

by

\\[ T(Hx)=H_Ax. \\]

The first point to verify is that \\(T\\) is well-defined. If \\(Hx=Hy\\), then

\\[ H(x-y)=0. \\]

Thus \\(x-y\in\ker H\\), and the hypothesis gives \\(x-y\in\ker H_A\\). Therefore

\\[ H_Ax=H_Ay. \\]

So \\(T\\) is well-defined.

It is linear because, for \\(a,b\in\mathbb C\\),

\\[ \begin{aligned} T(aHx_1+bHx_2) &=T(H(ax_1+bx_2))\\\ &=H_A(ax_1+bx_2)\\\ &=aH_Ax_1+bH_Ax_2. \end{aligned} \\]

Now choose a complementary subspace \\(W'\\) such that

\\[ \mathbb C^q=\operatorname{im}H\oplus W'. \\]

Extend \\(T\\) to a linear map

\\[ Z:\mathbb C^q\longrightarrow\mathbb C^q \\]

by choosing any linear map on \\(W'\\), for example zero. Then

\\[ ZH=H_A. \\]

Relative to the standard basis, \\(Z\\) is a square matrix in \\(\mathbb C^{q\times q}\\). Hence

\\[ \boxed{\ker H\subseteq\ker H_A \iff \exists Z\in\mathbb C^{q\times q}:H_A=ZH.} \\]

The reverse implication is immediate: if \\(Hx=0\\), then \\(H_Ax=ZHx=0\\).

Thus the factorisation asserted in Theorem 1 is exactly correct. It does not require \\(H\\) to have full column rank, nor does it require \\(H_A\\) to have the same image as \\(H\\).&#x20;

37_three_proofs.md



### 1.2 The normal-rank argument is correct

Once

\\[ H_A=ZH, \\]

we have

\\[ P(\lambda)=\lambda H-H_A=(\lambda I_q-Z)H. \\]

For any \\(\lambda_0\in\mathbb C\\),

\\[ \operatorname{im}P(\lambda_0) =(\lambda_0 I_q-Z)(\operatorname{im}H). \\]

Therefore

\\[ \operatorname{rank}P(\lambda_0) = \dim\operatorname{im}H -\dim\bigl(\operatorname{im}H\cap\ker(\lambda_0I_q-Z)\bigr). \\]

Since \\(\dim\operatorname{im}H=\omega\\),

\\[ \boxed{ \operatorname{rank}P(\lambda_0)=\omega \iff \operatorname{im}H\cap\ker(\lambda_0I_q-Z)=\\{0\\}. } \\]

This is the cleanest formulation of the rank criterion.

Because \\(Z\\) is a square complex matrix, it has only finitely many eigenvalues. Choose \\(\lambda_0\\) outside its spectrum. Then \\(\lambda_0 I_q-Z\\) is invertible, and

\\[ \operatorname{rank}P(\lambda_0)=\operatorname{rank}H=\omega. \\]

It follows that the normal rank of \\(P\\) is at least \\(\omega\\). On the other hand, \\(P(\lambda)\\) is obtained by multiplying \\(H\\) on the left, so

\\[ \operatorname{rank}P(\lambda)\le\operatorname{rank}H=\omega \\]

for every \\(\lambda\\). Thus

\\[ \boxed{\operatorname{nrank}P=\omega.} \\]

This proves the normal-rank assertion without any appeal to Kronecker canonical form.

### 1.3 The gcd criterion is correct

For every fixed \\(\lambda_0\\),

\\[ \operatorname{rank}P(\lambda_0)=\omega \\]

if and only if at least one \\(\omega\times\omega\\) minor of \\(P(\lambda_0)\\) is nonzero.

Consequently,

\\[ \operatorname{rank}P(\lambda_0)<\omega \\]

if and only if all its \\(\omega\times\omega\\) minors vanish at \\(\lambda_0\\).

Let those minors be \\(p_1(\lambda),\ldots,p_N(\lambda)\\). Over \\(\mathbb C\\), they have a common finite root if and only if their gcd is nonconstant. This follows from the fundamental theorem of algebra, together with the usual gcd property in the PID \\(\mathbb C[\lambda]\\).

Therefore

\\[ \boxed{ \operatorname{rank}P(\lambda)=\omega \quad\forall\lambda\in\mathbb C \iff \gcd(p_1,\ldots,p_N)\in\mathbb C^\times. } \\]

The fact that the normal rank is \\(\omega\\) is important: it ensures that the minors are not all identically zero.

### 1.4 The zero-rank case is correct, with one convention to state

If \\(\omega=0\\), then \\(H=0\\). The kernel hypothesis gives

\\[ \ker H=\mathbb C^k\subseteq\ker H_A, \\]

so \\(H_A=0\\). Thus

\\[ P(\lambda)=0 \\]

for all \\(\lambda\\), and

\\[ \operatorname{rank}P(\lambda)=0=\omega. \\]

Hence the reduced spectral condition is automatic.

I agree with separating this case rather than forcing it into the gcd formulation. One could adopt the convention that the unique \\(0\times0\\) minor is \\(1\\), but there is no need to introduce that convention into the main theorem.

### 1.5 One interpretative correction: \\(Z|\_{\operatorname{im}H}\\) need not be an endomorphism

The report's remark says

\\[ \Phi_K=Z|\_{\operatorname{im}H}. \\]

This is correct if the restriction is understood as

\\[ Z|\_{\operatorname{im}H}: \operatorname{im}H\longrightarrow\mathbb C^q. \\]

It is not generally an endomorphism of \\(\operatorname{im}H\\), because

\\[ Z(\operatorname{im}H)=\operatorname{im}H_A \\]

need not be contained in \\(\operatorname{im}H\\).

The correct obstruction is

\\[ \exists\\,0\ne w\in\operatorname{im}H,\quad Zw=\lambda w \\]

for some \\(\lambda\in\mathbb C\\). In other words, the restriction map \\(Z|\_{\operatorname{im}H}\\), considered as a map into the ambient \\(\mathbb C^q\\), has an eigenvector in its domain when its value happens to lie on the same line.

This is exactly the earlier invariant-line criterion:

\\[ \exists\\,0\ne w\in W_K,\quad \Phi_K(w)\in\mathbb Cw. \\]

It is not necessary that \\(Z\\) preserve all of \\(W_K\\). The eigenvector obstruction only concerns individual lines in \\(W_K\\).

There is also no dependence on the arbitrary extension of \\(T\\). Any two extensions \\(Z_1,Z_2\\) agree on \\(\operatorname{im}H\\), so

\\[ Z_1w=Z_2w\qquad(w\in\operatorname{im}H). \\]

Thus the obstruction is intrinsic, even though the square matrix \\(Z\\) is not unique.

Theorem 1: correct

I would retain the proof and make only the interpretative clarification above.

## 2. Theorem 2: closedness of the bad locus

The projective compactification proof is correct. In fact, it is one of the strongest parts of the report because it avoids a common error in elimination arguments: confusing the image of an affine projection with its Zariski closure.

### 2.1 The incidence set is closed

Let \\(U\\) be an algebraic set on which

\\[ \operatorname{rank}H(R)=\omega \\]

is constant, with \\(\omega\ge1\\).

Define

\\[ P^{\mathrm h}(R;\alpha,\beta) =\alpha H(R)-\beta H_A(R). \\]

For every choice of row and column index sets \\(I,J\\) of size \\(\omega\\), the corresponding minor

\\[ \det P^{\mathrm h}(R;\alpha,\beta)\_{I,J} \\]

is polynomial in \\(R\\) and homogeneous of degree \\(\omega\\) in \\((\alpha,\beta)\\), provided \\(H,H_A\\) are polynomially parameterised in \\(R\\).

The simultaneous vanishing of these minors defines a closed subset

\\[ \mathcal X\subseteq U\times\mathbb P^1. \\]

This step is exact. There is no issue caused by the use of a projective spectral parameter: the minors are homogeneous in \\((\alpha,\beta)\\), so their vanishing is well-defined on projective points.

### 2.2 The leading coefficient excludes the point at infinity

The point at infinity in the affine \\(\lambda=\alpha/\beta\\) chart is

\\[ [1:0]. \\]

At this point,

\\[ P^{\mathrm h}(R;1,0)=H(R). \\]

Since \\(\operatorname{rank}H(R)=\omega\\), at least one \\(\omega\times\omega\\) minor of \\(H(R)\\) is nonzero.

Therefore

\\[ (R,[1:0])\notin\mathcal X \\]

for every \\(R\in U\\).

Every point of \\(\mathcal X\\) consequently has \\(\beta\ne0\\), and so has a unique representative of the form

\\[ [\lambda:1]. \\]

At that representative,

\\[ P^{\mathrm h}(R;\lambda,1) =\lambda H(R)-H_A(R)=P(R,\lambda). \\]

It follows that

\\[ R\in\operatorname{pr}\_1(\mathcal X) \iff \exists\lambda\in\mathbb C: \operatorname{rank}P(R,\lambda)<\omega. \\]

This proves the exact set identity

\\[ \boxed{\mathcal B=\operatorname{pr}\_1(\mathcal X).} \\]

### 2.3 The projection is closed

The projection

\\[ \operatorname{pr}\_1:U\times\mathbb P^1\longrightarrow U \\]

is a projective morphism. Projective morphisms are proper, and proper morphisms are universally closed. In particular, they map Zariski-closed sets to Zariski-closed sets.

Hence

\\[ \mathcal B=\operatorname{pr}\_1(\mathcal X) \\]

is Zariski closed in \\(U\\).

This is precisely the point where projective compactification matters. If one worked directly with the affine \\(\lambda\\)-line, the projection need not be closed: a sequence of spectral roots can escape to infinity. The full-column-rank leading coefficient prevents that phenomenon because the homogenised incidence has no point over infinity.

Important: the kernel compatibility condition

\\[ \ker H\subseteq\ker H_A \\]

is not needed for Theorem 2 itself. Theorem 2 only needs the constant-rank leading coefficient. The compatibility condition is needed for the reduced-pencil interpretation and for the normal-rank statement in Theorem 1. This separation is mathematically useful and should be preserved.

37_three_proofs.md

### 2.4 Corollary 1: the open-or-empty dichotomy

If \\(U\\) is irreducible, every proper closed subset has a nonempty open dense complement. Therefore either

\\[ \mathcal B=U, \\]

in which case no point of \\(U\\) is spectrally feasible, or

\\[ \mathcal B\subsetneq U, \\]

in which case

\\[ U\setminus\mathcal B \\]

is nonempty, Zariski open, and dense in \\(U\\).

This corollary is immediate and correct.

One small wording point: if \\(U\\) is irreducible but not necessarily affine, this statement still holds. The affine hypothesis is only needed for the coordinate-ring formulation in Corollary 2.

### 2.5 Corollary 2: the elimination ideal

This corollary is correct, but its hypotheses should be made more explicit.

Assume \\(U\\) is an affine irreducible algebraic variety over \\(\mathbb C\\), with coordinate ring

\\[ A=\mathbb C[U], \\]

which is a finitely generated integral domain over \\(\mathbb C\\).

Let

\\[ J=\langle p_1,\ldots,p_N\rangle\subseteq A[\lambda] \\]

be the ideal generated by the \\(\omega\\)-minors of \\(\lambda H-H_A\\), and let

\\[ E=J\cap A. \\]

The affine elimination theorem says that

\\[ V_U(E) \\]

is the Zariski closure in \\(U\\) of the projection of the affine zero set \\(V(J)\subseteq U\times\mathbb A^1\\).

But Theorem 2 has already shown that this projection is closed in \\(U\\): it is precisely \\(\mathcal B\\). Therefore

\\[ \boxed{\mathcal B=V_U(E).} \\]

Now use that \\(A\\) is a finitely generated domain over the algebraically closed field \\(\mathbb C\\).

- \\(E=(0)\\) gives \\(V_U(E)=U\\).
- \\(E=A\\) gives \\(V_U(E)=\varnothing\\).
- If \\(0\ne E\ne A\\), then \\(V_U(E)\\) is a nonempty proper closed subset of \\(U\\).

The last assertion uses both the domain property and the Nullstellensatz. Since \\(A\\) is a domain, a nonzero element of \\(E\\) does not vanish identically on \\(U\\), so \\(V_U(E)\ne U\\). Since \\(E\\) is proper and \\(A\\) is a finitely generated \\(\mathbb C\\)-algebra, the weak Nullstellensatz ensures that \\(V_U(E)\ne\varnothing\\).

Thus the three cases in the report are correct:

\\[ \boxed{ \begin{array}{c|c|c} E & \mathcal B & \text{Feasible locus}\\\ \hline (0)&U&\varnothing\\\ 0\ne E\ne A&\text{proper nonempty closed}&\text{nonempty open dense}\\\ A&\varnothing&U \end{array} } \\]

And the feasibility test is indeed

\\[ \boxed{E\ne(0),} \\]

not merely \\(E\ne A\\).

That distinction is essential. A zero elimination ideal means the projection is dense; here, because the projection is closed, it means the projection is all of \\(U\\). So the zero ideal corresponds to universal badness, not feasibility.

### 2.6 One qualification for a locally closed chart

In the broader project, \\(U\\) is often a rank chart defined by

\\[ g(R)\ne0 \\]

inside an affine algebraic set. Such a chart is locally closed rather than closed in the ambient affine space.

Theorem 2 still holds relative to \\(U\\), because

\\[ U\times\mathbb P^1\longrightarrow U \\]

is still projective and hence closed. But for the elimination-ideal statement, one should work in the coordinate ring of the chart, typically by localising at \\(g\\):

\\[ A_g=A[g^{-1}]. \\]

Equivalently, one can use a saturation formulation in the ambient coordinate ring, with the precise saturation ideal stated.

One must not compute \\(J\cap A\\) in the unlocalised ambient ring and silently identify its variety with the projection restricted to \\(g\ne0\\). The chart condition is part of the geometry.

Theorem 2: correct

The projective proof is sound. Corollary 2 should be amended only to state the affine irreducibility and coordinate-ring hypotheses explicitly, and to explain localisation when the base is a principal-open chart.

## 3. Theorem 3: corrected Bézout system

The central mathematical argument is correct. The report has fixed the earlier coefficient-count error. There is, however, an important issue in the definition of \\(N\\).

### 3.1 The bounded-degree Bézout lemma

The theorem uses the statement

\\[ \gcd(p_1,\ldots,p_N)=1 \iff \exists u_1,\ldots,u_N,\quad \sum\_{i=1}^N u_i p_i=1,\quad \deg u_i\le\omega-1, \\]

where

\\[ \deg p_i\le\omega. \\]

This bounded-degree version is valid over an infinite field, in particular over \\(\mathbb C\\).

For completeness, here is a proof with the exceptional cases included.

If some \\(p_i\\) is a nonzero constant, take \\(u_i=p_i^{-1}\\) and all other \\(u_j=0\\).

Otherwise, assuming the gcd is one, choose a nonzero nonconstant polynomial among the \\(p_i\\), and relabel it as \\(p_1\\). For each root \\(\alpha\\) of \\(p_1\\), at least one of the other \\(p_i\\) satisfies

\\[ p_i(\alpha)\ne0; \\]

otherwise \\(\alpha\\) would be a common root and \\(\lambda-\alpha\\) would divide every \\(p_i\\).

Choose constants \\(c_2,\ldots,c_N\in\mathbb C\\) such that

\\[ g=\sum\_{i=2}^N c_i p_i \\]

does not vanish at any root of \\(p_1\\). Such a choice exists: each root of \\(p_1\\) excludes a proper linear hyperplane in the coefficient space \\(\mathbb C^{N-1}\\), and finitely many proper hyperplanes cannot cover this space over an infinite field.

Then

\\[ \gcd(p_1,g)=1. \\]

The ordinary two-polynomial Euclidean algorithm gives

\\[ a p_1+b g=1 \\]

with

\\[ \deg a<\deg g\le\omega,\qquad \deg b<\deg p_1\le\omega. \\]

Substituting the definition of \\(g\\) gives the required Bézout representation, with all multiplier degrees at most \\(\omega-1\\).

If \\(N=1\\), gcd one means \\(p_1\\) is a nonzero constant, which is already covered. If all \\(p_i=0\\), their gcd is not one. This completes the proof.

Thus the degree bound in Theorem 3 is valid.

### 3.2 The coefficient count is exactly \\(2\omega\\)

Write

\\[ u_i(\lambda)=\sum\_{j=0}^{\omega-1}u\_{ij}\lambda^j. \\]

Since

\\[ \deg p_i\le\omega, \\]

we have

\\[ \deg(u_ip_i)\le2\omega-1. \\]

Therefore

\\[ \deg\left(\sum_i u_ip_i-1\right)\le2\omega-1. \\]

A polynomial of degree at most \\(2\omega-1\\) vanishes identically if and only if its \\(2\omega\\) coefficients vanish:

\\[ [\lambda^0], [\lambda^1],\ldots,[\lambda^{2\omega-1}]. \\]

The identity

\\[ \sum_i u_ip_i=1 \\]

therefore yields exactly \\(2\omega\\) linear equations in the \\(N\omega\\) unknown coefficients \\(u\_{ij}\\).

Hence

\\[ \boxed{ M\_\omega(R)\in\mathbb C^{2\omega\times N\omega}, \qquad b\_\omega=(1,0,\ldots,0)^{\mathsf T}. } \\]

This is correct. The \\(\omega=1\\) check is a useful sanity test: constant multipliers applied to affine-linear polynomials require two equations, one for the coefficient of \\(\lambda\\) and one for the constant term.

### 3.3 Important correction: the stated number of minors

The report says

\\[ N=\binom q\omega. \\]

That is correct for a reduced \\(q\times\omega\\) pencil, but not for the original \\(q\times k\\) pencil when \\(k\\) may exceed \\(\omega\\).

For a \\(q\times k\\) matrix, an \\(\omega\times\omega\\) minor is determined by:

- a choice of \\(\omega\\) rows from \\(q\\);
- a choice of \\(\omega\\) columns from \\(k\\).

Therefore the number of such minors is

\\[ \boxed{N=\binom q\omega\binom k\omega.} \\]

This matters for the dimension and size claims of the coefficient system.

There are two correct formulations, and the report should choose one explicitly.

Formulation A: original pencil. Keep

\\[ P(\lambda)=\lambda H-H_A\in\mathbb C[\lambda]^{q\times k} \\]

and take all \\(\omega\times\omega\\) minors. Then

\\[ N=\binom q\omega\binom k\omega. \\]

Formulation B: reduced pencil. Choose a set of \\(\omega\\) columns \\(S\\) such that

\\[ H_S\in\mathbb C^{q\times\omega} \\]

has full column rank. Under

\\[ \ker H\subseteq\ker H_A, \\]

the columns of \\(H_A\\) satisfy the same linear dependencies as the columns of \\(H\\). Thus, after choosing the basis columns \\(S\\), there is a constant matrix \\(V\in\mathbb C^{\omega\times k}\\) of full row rank such that

\\[ H=H_SV,\qquad H_A=(H_A)\_SV. \\]

Consequently,

\\[ P(\lambda)=P_S(\lambda)V,\qquad P_S(\lambda)=\lambda H_S-(H_A)\_S. \\]

The rank of \\(P(\lambda)\\) equals the rank of \\(P_S(\lambda)\\), because \\(V:\mathbb C^k\to\mathbb C^\omega\\) is surjective. Hence it suffices to use the \\(\omega\times\omega\\) maximal minors of the reduced \\(q\times\omega\\) pencil \\(P_S\\). Their number is

\\[ \boxed{N=\binom q\omega.} \\]

This is likely the formulation intended by the report, but it must say explicitly that \\(P\\) has been reduced to \\(P_S\\). Otherwise the displayed value of \\(N\\) is incorrect.

There is an additional useful observation: the nonzero maximal minors of the original pencil and the maximal minors of \\(P_S\\) differ only by nonzero constant factors determined by the selected columns of \\(V\\). Thus their gcds agree up to a nonzero scalar. The reduced-pencil formulation does not change the spectral criterion.

37_three_proofs.md

### 3.4 The rank-comparison corollary is correct

The Bézout identity is solvable if and only if

\\[ M\_\omega(R)u=b\_\omega \\]

is consistent. The elementary rank criterion gives

\\[ M\_\omega(R)u=b\_\omega\text{ is inconsistent} \iff \operatorname{rank}[M\_\omega(R)\mid b\_\omega]> \operatorname{rank}M\_\omega(R). \\]

Since inconsistency is equivalent to the gcd being nonconstant, the bad spectral locus is exactly

\\[ \boxed{ \mathcal B\_\omega = \\{R: \operatorname{rank}[M\_\omega(R)\mid b\_\omega]> \operatorname{rank}M\_\omega(R)\\}. } \\]

This is an exact equality of sets.

The report's rank-stratified description is also correct:

\\[ \mathcal B\_\omega = \bigcup\_{s=0}^{2\omega-1} \left\\{ R: \operatorname{rank}M\_\omega(R)=s,\  \operatorname{rank}[M\_\omega(R)\mid b\_\omega]\ge s+1 \right\\}. \\]

To check the index range: if the system is inconsistent, the rank of \\(M\_\omega\\) must be strictly less than its number of rows \\(2\omega\\). Thus

\\[ s\le2\omega-1. \\]

Conversely, every point in one of the displayed strata is inconsistent. No rank possibilities are omitted.

Each rank condition is constructible. In detail:

\\[ \operatorname{rank}M=s \\]

is the conjunction of

- vanishing of all \\((s+1)\times(s+1)\\) minors;
- nonvanishing of at least one \\(s\times s\\) minor,

with the usual conventions at \\(s=0\\). And

\\[ \operatorname{rank}[M\mid b]\ge s+1 \\]

is the nonvanishing of at least one \\((s+1)\times(s+1)\\) minor.

Thus the bad locus has a finite constructible description.

The report is also right to reject the proposed shortcut involving vanishing of all maximal minors of the augmented matrix. Inconsistency means that augmentation increases the rank; it does not mean that the augmented matrix has deficient row rank.

This is exactly the distinction that was missing in the earlier attempt.&#x20;

37_three_proofs.md



### 3.5 The degree bounds

The degree calculation in the report is correct once the parameter dependence is stated.

Suppose every entry of \\(H(R)\\) and \\(H_A(R)\\) is affine-linear in \\(R\\). Then every entry of

\\[ P(R,\lambda)=\lambda H(R)-H_A(R) \\]

is affine-linear in \\(R\\), with coefficients polynomial of degree at most one in \\(R\\).

Each \\(\omega\times\omega\\) minor has coefficients in \\(\lambda\\) of degree at most \\(\omega\\), and each such coefficient has degree at most \\(\omega\\) in \\(R\\). Therefore every entry of \\(M\_\omega(R)\\) has degree at most \\(\omega\\) in \\(R\\).

A minor of \\(M\_\omega(R)\\) of size \\(s\\) has degree at most

\\[ s\omega. \\]

Since \\(M\_\omega\\) has \\(2\omega\\) rows, the largest relevant minor size is \\(2\omega\\). Hence

\\[ \boxed{\deg_R\le2\omega^2.} \\]

This is the correct bound for the rank-stratified equations in the original \\(R\\)-coordinates.

Now consider the factorisation

\\[ H=UV^{\mathsf T},\qquad H_A=ZV^{\mathsf T}, \\]

where

\\[ U,Z\in\mathbb C^{q\times\omega}, \qquad V\in\mathbb C^{k\times\omega}. \\]

Then

\\[ P(\lambda)=(\lambda U-Z)V^{\mathsf T}. \\]

For row set \\(I\\) and column set \\(J\\), both of cardinality \\(\omega\\),

\\[ \det P(\lambda)\_{I,J} = \det(\lambda U-Z)\_{I,:}\\, \det(V\_{J,:}^{\mathsf T}). \\]

The first factor has degree at most \\(\omega\\) in \\((U,Z)\\), and the second factor has degree \\(\omega\\) in \\(V\\). Therefore each coefficient of the minor has total degree at most \\(2\omega\\) in the factor variables.

The entries of the Bézout coefficient matrix have degree at most \\(2\omega\\) in \\((U,V,Z)\\), and a minor of size at most \\(2\omega\\) has degree at most

\\[ \boxed{4\omega^2.} \\]

Thus both displayed degree bounds are correct under the affine-entry hypothesis in the first calculation, and under the stated bilinear factorisation in the second.

One caveat: if \\(H,H_A\\) are polynomial of degree \\(\delta>1\\) in \\(R\\), the first bound becomes

\\[ 2\omega^2\delta, \\]

not \\(2\omega^2\\). The theorem should explicitly say that the entries are affine-linear in \\(R\\), as they are in the observer model.

Theorem 3: core proof correct; minor-count and hypotheses need correction

## 4. Question 2: is square \\(Z\\) or rectangular \\(Z\\) the right factorisation?

Both are correct, but they serve different purposes. For the observer problem and the factor-space parameterisation, the rectangular representation is more natural. The square representation is a convenient extension used in the proof of Theorem 1.

### 4.1 The intrinsic rectangular factorisation

Let

\\[ \omega=\operatorname{rank}H>0. \\]

Choose a full-column-rank matrix

\\[ U\in\mathbb C^{q\times\omega} \\]

whose columns form a basis of \\(\operatorname{im}H\\).

There is a unique full-row-rank matrix

\\[ V^{\mathsf T}\in\mathbb C^{\omega\times k} \\]

such that

\\[ H=UV^{\mathsf T}. \\]

Indeed, since the columns of \\(H\\) belong to \\(\operatorname{im}U\\), each column of \\(H\\) has unique coordinates in the chosen basis \\(U\\). Those coordinate columns form \\(V^{\mathsf T}\\). Since \\(\operatorname{rank}H=\omega\\) and \\(U\\) has rank \\(\omega\\), \\(V^{\mathsf T}\\) has rank \\(\omega\\).

Now assume

\\[ \ker H\subseteq\ker H_A. \\]

Because \\(U\\) has full column rank,

\\[ \ker H=\ker V^{\mathsf T}. \\]

The kernel inclusion is therefore

\\[ \ker V^{\mathsf T}\subseteq\ker H_A. \\]

It follows that \\(H_A\\) factors through \\(V^{\mathsf T}\\): there exists

\\[ G\in\mathbb C^{q\times\omega} \\]

such that

\\[ H_A=GV^{\mathsf T}. \\]

Thus the intrinsic rank-\\(\omega\\) representation is

\\[ \boxed{ H=UV^{\mathsf T},\qquad H_A=GV^{\mathsf T}, } \\]

where

\\[ U,G\in\mathbb C^{q\times\omega}, \qquad V\in\mathbb C^{k\times\omega}, \\]

and \\(U,V\\) have full column rank.

Conversely, every pair of this form satisfies

\\[ \ker H=\ker V^{\mathsf T}\subseteq\ker H_A. \\]

So this rectangular factorisation is equivalent to the compatibility condition, once \\(U,V\\) have the indicated ranks.

### 4.2 The reduced pencil becomes particularly simple

We have

\\[ P(\lambda) =\lambda H-H_A =(\lambda U-G)V^{\mathsf T}. \\]

Since \\(V^{\mathsf T}:\mathbb C^k\to\mathbb C^\omega\\) is surjective,

\\[ \operatorname{im}P(\lambda) = \operatorname{im}(\lambda U-G). \\]

Consequently,

\\[ \boxed{ \operatorname{rank}P(\lambda) = \operatorname{rank}(\lambda U-G). } \\]

The original \\(q\times k\\) pencil has therefore been reduced to the \\(q\times\omega\\) pencil

\\[ P\_{\mathrm{red}}(\lambda)=\lambda U-G, \\]

whose leading coefficient \\(U\\) has full column rank.

This is exactly the pencil to use in the Bézout system. Its maximal minors are the \\(\omega\times\omega\\) minors indexed only by row subsets, so their number is

\\[ \binom q\omega. \\]

This also resolves the minor-count ambiguity in Theorem 3 if the authors intend the reduced-pencil formulation.

### 4.3 How the square factorisation relates to the rectangular one

Because \\(U\\) has full column rank, it admits a left inverse

\\[ L\in\mathbb C^{\omega\times q}, \qquad LU=I\_\omega. \\]

Define

\\[ Z=GL+Z_0(I_q-UL), \\]

where \\(Z_0\in\mathbb C^{q\times q}\\) is arbitrary. Then

\\[ ZU =GLU+Z_0(I_q-UL)U =G. \\]

It follows that

\\[ ZH=ZUV^{\mathsf T}=GV^{\mathsf T}=H_A. \\]

Thus the square extension always exists. Conversely, if \\(H_A=ZH\\), then

\\[ H_A=ZUV^{\mathsf T}=(ZU)V^{\mathsf T}, \\]

so the rectangular factor is simply

\\[ G=ZU. \\]

Therefore:

\\[ \boxed{ H_A=ZH,\quad Z\in\mathbb C^{q\times q} \quad\Longleftrightarrow\quad H_A=GV^{\mathsf T},\quad G\in\mathbb C^{q\times\omega}, } \\]

when \\(H=UV^{\mathsf T}\\) with \\(U,V\\) full column rank.

### 4.4 What should be used in the observer problem?

The observer's intrinsic map is

\\[ \Phi_K:W_K\longrightarrow\mathbb C^q, \qquad W_K=\operatorname{im}H. \\]

It is naturally represented by a \\(q\times\omega\\) matrix \\(G\\) after choosing a basis of \\(W_K\\). It is not intrinsically an endomorphism of \\(\mathbb C^q\\).

For this reason, I recommend the following notation:

- Use \\(Z\_{\mathrm{ext}}\in\mathbb C^{q\times q}\\) only for the arbitrary square extension in Theorem 1.
- Use \\(G\in\mathbb C^{q\times\omega}\\) for the intrinsic rectangular factor in the rank-\\(\omega\\) parameterisation.
- Write\
  \\[\
  H=UV^{\mathsf T},\qquad H_A=GV^{\mathsf T}.\
  \\]

This avoids using the same letter \\(Z\\) for two matrices of different dimensions and clarifies which object is intrinsic.

Conclusion for Question 2: the square factorisation is correct and useful for proving Theorem 1. The rectangular factorisation is the better formulation for the observer problem, the reduced pencil, and the factor-space sampling programme.

## 5. Question 3: which proof is most likely to hide an error?

My ranking is:

1. Theorem 3's formulation and its degree/size bookkeeping — most likely to hide an error.
2. Corollary 2 of Theorem 2 — correct, but has hypotheses and localisation details that are easy to omit.
3. Theorem 1 — least likely; its factorisation and rank argument are sound.

The reason is worth explaining.

### 5.1 Theorem 3: the central algebra is right, but its interfaces need auditing

The Bézout coefficient argument itself is now correct:

\\[ \deg u_i\le\omega-1,\qquad \deg p_i\le\omega \\]

gives \\(2\omega\\) coefficient equations.

The rank comparison is also correct:

\\[ \operatorname{rank}[M\_\omega\mid b\_\omega]> \operatorname{rank}M\_\omega. \\]

The rank-stratified constructible description follows exactly from that comparison. I do not see a mathematical error in that corollary.

But there are two interface issues:

- Is the pencil the original \\(q\times k\\) pencil or the reduced \\(q\times\omega\\) pencil?
- Are the coefficients of \\(H,H_A\\) affine-linear in \\(R\\), as required for the stated \\(R\\)-degree bound?

These choices determine the number of minors, the coefficient-matrix dimensions, and the complexity estimate. They are not cosmetic details.

### 5.2 Theorem 2: the projective proof is strong, but elimination requires care

Theorem 2 itself is particularly robust. The only likely errors are in applying Corollary 2 beyond its hypotheses:

- Is the base an affine irreducible variety?
- Is its coordinate ring really a domain?
- Is the rank chart a principal-open set requiring localisation?
- Has the projection been shown closed before identifying it with the elimination variety?

The report's current argument handles these points in substance, but the paper should state them explicitly.

### 5.3 Theorem 1: the square extension is not a real weakness

The potential concern about a square \\(Z\\) is resolved by the extension argument. The only adjustment needed is terminological: do not call \\(Z|\_{\operatorname{im}H}\\) an endomorphism unless \\(Z\\) preserves \\(\operatorname{im}H\\). It is a map

\\[ \operatorname{im}H\longrightarrow\mathbb C^q. \\]

The eigenvector criterion remains valid without invariance of the whole subspace.

Theorem 1 has the strongest proof as written

## 6. Proposed corrected statements for the paper

I would make the following edits before treating the three results as final.

### 6.1 Replace the factorisation notation in Theorem 1

Retain the square extension proof, but add:

> The extension \\(Z\\) is not unique. Only its restriction as a map from \\(\operatorname{im}H\\) into \\(\mathbb C^q\\) is determined. In general, \\(\operatorname{im}H\\) need not be \\(Z\\)-invariant. The obstruction is the existence of a nonzero \\(w\in\operatorname{im}H\\) such that \\(Zw=\lambda w\\), not the existence of an eigenvalue of an endomorphism \\(Z|\_{\operatorname{im}H}\\).

### 6.2 Strengthen the hypotheses of Theorem 2

State that \\(H,H_A\\) depend algebraically (polynomially or regularly) on \\(R\\). This makes the incidence equations well-defined as algebraic equations.

For Corollary 2, state:

> Suppose \\(U\\) is an affine irreducible variety over \\(\mathbb C\\), with coordinate ring \\(A=\mathbb C[U]\\). Then, with \\(J\\) and \\(E\\) as defined above, \\(\mathcal B=V_U(E)\\).

Then add a separate sentence for locally closed rank charts: use the localised coordinate ring or an equivalent saturation.

### 6.3 Replace the first sentence of Theorem 3 with one of two alternatives

Preferred version: reduced pencil.

> Fix a rank-\\(\omega\\) column chart, and let \\(P\_{\mathrm{red}}(\lambda)=\lambda U-G\in\mathbb C[\lambda]^{q\times\omega}\\) be the reduced pencil with \\(U\\) of full column rank. Let \\(p_1,\ldots,p_N\\) be its maximal minors, where \\(N=\binom q\omega\\).

Then the current \\(2\omega\times N\omega\\) coefficient system is correct.

Alternative version: original pencil.

> Let \\(P(\lambda)=\lambda H-H_A\in\mathbb C[\lambda]^{q\times k}\\) have normal rank \\(\omega\\), and let \\(p_1,\ldots,p_N\\) be all its \\(\omega\times\omega\\) minors, where \\(N=\binom q\omega\binom k\omega\\).

Then the same Bézout coefficient argument applies, but the coefficient system has \\(N\omega\\) unknowns.

I favour the first version. It removes redundant minors and aligns directly with the intrinsic \\(W_K\\)-based reduction.

### 6.4 State the affine-dependence assumption

Add:

> Assume that the entries of \\(H(R)\\) and \\(H_A(R)\\) are affine-linear functions of the observer variables \\(R\\).

Then the \\(2\omega^2\\) degree bound in \\(R\\) follows as stated.

For the factor parameterisation, use

\\[ H=UV^{\mathsf T},\qquad H_A=GV^{\mathsf T}, \\]

and write the degree bound in \\((U,V,G)\\) as \\(4\omega^2\\).

## 7. Final assessment and next-round recommendation

| Item                                | Verdict                               | Required revision                                                               |
| ----------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------- |
| Square factorisation \\(H_A=ZH\\)   | Correct                               | Clarify that \\(Z\\) is an extension, not necessarily an invariant-subspace map |
| Theorem 1 normal rank               | Correct                               | None                                                                            |
| Theorem 1 gcd criterion             | Correct                               | None                                                                            |
| Theorem 2 projective incidence      | Correct                               | State algebraic dependence explicitly                                           |
| Theorem 2 projection closedness     | Correct                               | None                                                                            |
| Corollary 1                         | Correct                               | None                                                                            |
| Corollary 2 elimination ideal       | Correct with hypotheses               | State affine irreducibility and localise on open charts                         |
| Bézout degree bound                 | Correct                               | Include proof or cite bounded-degree lemma                                      |
| Bézout coefficient count            | Correct: \\(2\omega\\)                | None                                                                            |
| Rank-consistency identity           | Correct                               | None                                                                            |
| Rank-stratified constructibility    | Correct                               | None                                                                            |
| \\(N=\binom q\omega\\)              | Correct only for reduced pencil       | Otherwise use \\(\binom q\omega\binom k\omega\\)                                |
| Degree bound \\(2\omega^2\\)        | Correct for affine \\(R\\)-dependence | State the hypothesis                                                            |
| Factor degree bound \\(4\omega^2\\) | Correct                               | Prefer rectangular factor \\(G\\)                                               |

My recommendation for the next round is to focus exclusively on Theorem 3's reduced-pencil formulation and its consequences. Theorem 1 and Theorem 2 are sufficiently solid for the paper, subject to the clarifications above. The next useful deliverable is a fully explicit reduced-pencil Bézout theorem in which:

1. the selected independent columns are specified;
2. the factorisation \\(P=P\_{\mathrm{red}}V^{\mathsf T}\\) is proved;
3. the number of maximal minors is exactly \\(\binom q\omega\\);
4. the \\(2\omega\\)-equation coefficient matrix is displayed;
5. the rank-stratified constructibility statement is derived;
6. the degree bound is stated under the affine-entry hypothesis.

That will leave a clean algebraic foundation for the later sampling argument. It will not, by itself, prove \\(\mathrm{DEC}(q)\in\mathrm{RP}\\): the fixed-row constraints and the coverage of all observer rank strata remain separate issues. But it will remove the present ambiguity in the algebraic encoding, which is the right prerequisite for addressing those algorithmic questions.