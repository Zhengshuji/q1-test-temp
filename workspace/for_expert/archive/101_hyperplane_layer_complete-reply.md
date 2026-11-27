# **Comprehensive research review of Report 101: The Hyperplane Layer**

The central contribution of Report 101 is a proposed structural and algorithmic treatment of the **first nontrivial layer of the functional-observer feasibility problem**, namely the hyperplane layer \\(c=1\\), where

\\[ \omega=k-1,\qquad k=\dim\ker[C;CA]. \\]

The report goes beyond the two papers in an important direction. Paper I establishes finite algebraic certificates and parameterized complexity bounds for prescribed-order feasibility, while Paper II develops minimum-order characterization, lower bounds, monotonicity, and construction. Report 101 attempts to exploit the additional geometry of the \\(c=1\\) layer to obtain a more explicit decision procedure and a new fixed-\\(p\\) polynomial-time result.

My overall assessment is that this is a promising and mathematically interesting extension. In particular, the compression-eigenvector reduction in Proposition E, the projective closedness argument in Theorem A, and the left-factor interpretation in Proposition F provide a useful framework for understanding the layer.

However, **the report should not yet be regarded as a fully established complexity result without several additional mathematical audits**. There are important distinctions between:

1. proving that admissible directions must be eigenvectors of a compression;
2. proving that the resulting parameter space is a finite union of algebraic fibres;
3. deciding feasibility on each fibre by a generic gcd calculation;
4. establishing a polynomial bit-complexity bound for the entire procedure.

These are related but logically separate steps. I will distinguish results that follow from the stated hypotheses, results that need additional qualifications, and claims that require further proof.

## **1. Relationship between the three documents**

Before addressing the five questions, it is important to distinguish the mathematical roles of the three documents.

### **1.1 Paper I: the decision-theoretic foundation**

*Deciding functional observer feasibility: compression, certificates, and parameterized algorithms* establishes the following framework.

Let

\\[ K_0=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \qquad N\text{ a basis matrix of }K_0, \\]

and define

\\[ H=LN,\qquad H_A=LAN,\qquad P(\lambda)=\lambda H-H_A. \\]

The observer conditions reduce to

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H \tag{1} \\]

and

\\[ \operatorname{rank}P(\lambda)=\operatorname{rank}H \quad\forall\lambda\in\mathbb C. \tag{2} \\]

The key achievement is that the second condition can be tested by a finite algebraic certificate, rather than by explicitly checking infinitely many spectral values.

More specifically, Paper I develops:

- A pivot factorization of the compressed matrix \\(H\\).
- A bounded-degree Bézout representation of the maximal minors.
- A Gram-matrix representation using Cauchy–Binet.
- A fixed-order decision algorithm with \\(O(L^{O(q^2)})\\) bit operations for fixed \\(q\\).
- A fixed-parameter algorithm with complexity

\\[ \exp\big(O(\ell^2\log(\ell+2))\big)\operatorname{poly}(L), \qquad \ell=\operatorname{rank}(AN). \\]

The important distinction is that the fixed-parameter result is parameterized by \\(\ell\\), not by the number of free rows or by the number of coordinates used to describe them.

Paper I also establishes membership in the existential theory of the reals, while leaving unrestricted complexity unresolved.&#x20;

paper_I_dec(2).pdf



### **1.2 Paper II: the optimization and construction framework**

*Minimum order and minimum-order construction for functional observers* starts from the same compressed representation but develops a different consequence.

It introduces

\\[ T=\operatorname{row}[N\ AN], \\]

\\[ W=\operatorname{row}[H\ H_A], \qquad W_0=\operatorname{row}(L_0[N\ AN]). \\]

A feasible design corresponds to a subspace satisfying

\\[ W_0\subseteq W\subseteq T, \qquad \dim(W/W_0)\le r, \\]

together with the two compressed observer conditions.

The central structural theorem gives

\\[ \boxed{\omega+1\leq \dim W\leq 2\omega} \\]

for a feasible design with \\(\omega>0\\), and consequently

\\[ \omega\leq\ell, \qquad t=\dim(W/W_0)\leq 2\ell. \\]

This leads to the minimum-order formula

\\[ q\_{\min}=r_0+t\_{\min}, \\]

where

\\[ t\_{\min}=\min\\{\dim(W/W_0):W\text{ feasible}\\}. \\]

Paper II also proves monotonicity of feasible orders and derives an independent spectral lower bound. It uses the decision procedure of Paper I as an interface rather than reproving its complexity results.&#x20;

paper_II_minorder(3).pdf



### **1.3 Report 101: a new geometric specialization**

Report 101 introduces

\\[ c=k-\omega. \\]

The hyperplane layer is

\\[ \boxed{c=1,\qquad \omega=k-1.} \\]

The report's objective is to exploit this special codimension to reduce the original feasibility problem to a much smaller geometric problem.

Its proposed chain is

\\[ \boxed{ \text{hyperplane geometry} \longrightarrow \text{compression eigenvectors} \longrightarrow \text{algebraic fibres} \longrightarrow \text{generic pencil certificates} \longrightarrow \text{fixed-}p\text{ complexity}. } \\]

This is a natural research direction. However, the transition from compression eigenvectors to a finite collection of low-dimensional fibres requires more care than the report currently provides.

# **2. Detailed mathematical audit of the main results**

## **2.1 The hyperplane-layer reduction**

The report begins with

\\[ \omega=k-1. \\]

Since

\\[ H=LN \\]

has rank \\(k-1\\), its kernel is one-dimensional:

\\[ \ker H=\operatorname{span}(v). \\]

Because \\(N\\) is a basis of \\(K_0\\), we can regard \\(v\\) as a vector in \\(K_0\\).

The report then observes that

\\[ Hv=0 \\]

implies

\\[ LNv=0. \\]

Thus every row of \\(L\\) annihilates the corresponding state-space vector \\(Nv\\). With the report's convention that \\(v\\) itself denotes this state-space vector, this gives

\\[ V\subseteq v^\perp, \\]

where \\(V=\operatorname{row}L\\).

Furthermore, the condition

\\[ H_A=LAN \\]

and the row-space inclusion

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H \\]

imply that every row of \\(L\\) annihilates \\(Av\\) as well.

Therefore,

\\[ \boxed{ V\subseteq \operatorname{span}(v,Av)^\perp. } \\]

Writing

\\[ U_v=\operatorname{span}(v,Av), \\]

the geometric restriction becomes

\\[ V\subseteq U_v^\perp, \qquad \dim(V\cap K_0)=k-1. \\]

This is the correct starting point for the hyperplane analysis.

There are two cases:

- Eigen direction: \\(Av\in\operatorname{span}(v)\\).
- Non-eigen direction: \\(Av\notin\operatorname{span}(v)\\).

The distinction is important because

\\[ \dim U_v= \begin{cases} 1,&v\text{ is an eigenvector of }A,\\\ 2,&v\text{ is not an eigenvector of }A. \end{cases} \\]

**Assessment:** This reduction is mathematically sound, provided that the identification between the compressed kernel vector and its state-space representative is maintained consistently.

One notation improvement is necessary: use separate symbols for the vector in compressed coordinates and its image under \\(N\\). Otherwise, expressions such as \\(v\in K_0\\) and \\(Nv\\) can become ambiguous.

## **2.2 Theorem A: projective closedness and the generic-point criterion**

This is one of the strongest parts of the report.

Suppose \\(X\\) is an irreducible algebraic parameter space, and the matrices \\(H(x)\\) and \\(H_A(x)\\) depend polynomially on \\(x\\), with

\\[ \operatorname{rank}H(x)=\omega \\]

throughout \\(X\\).

Let \\(m_I(x,\lambda)\\) denote the \\(\omega\times\omega\\) maximal minors of

\\[ P_x(\lambda)=\lambda H(x)-H_A(x). \\]

Define the bad locus

\\[ \mathcal B= \left\\{ x\in X: \exists\lambda\in\mathbb C,\  m_I(x,\lambda)=0\ \forall I \right\\}. \\]

The report homogenizes the spectral variable:

\\[ P_x(s,t)=sH(x)-tH_A(x). \\]

The corresponding homogeneous maximal minors define a closed incidence variety

\\[ \mathcal D = \left\\{ (x,[s:t]): m_I(x,s,t)=0\ \forall I \right\\} \subseteq X\times\mathbb P^1. \\]

At infinity, \\(t=0\\), we have

\\[ P_x(1,0)=H(x). \\]

Since \\(H(x)\\) has rank \\(\omega\\), at least one maximal minor is nonzero. Thus

\\[ \mathcal D\cap(X\times\\{[1:0]\\})=\varnothing. \\]

Consequently, the projective incidence does not acquire an additional component at infinity.

Since

\\[ X\times\mathbb P^1\longrightarrow X \\]

is a proper morphism, the projection of the closed incidence set is closed. Therefore \\(\mathcal B\\) is closed.

Now use irreducibility of \\(X\\). There are only two possibilities:

1. \\(\mathcal B=X\\).
2. \\(\mathcal B\subsetneq X\\).

In the second case, every point in the nonempty Zariski-open set \\(X\setminus\mathcal B\\) is feasible.

Let \\(\mathbb Q(X)\\) be the function field of \\(X\\). Then the generic point is good precisely when the maximal minors have no common root over the algebraic closure of \\(\mathbb Q(X)\\). Equivalently,

\\[ \boxed{ \gcd_I m_I=1 \quad\text{in}\quad \overline{\mathbb Q(X)}[\lambda]. } \\]

Thus

\\[ \boxed{ X\text{ contains a feasible point} \iff \gcd_I m_I=1. } \\]

This is an important result because it changes the nature of the existence question.

Instead of searching for a special feasible point, one asks whether the generic point of an irreducible family is feasible.

### **An important qualification**

The irreducibility hypothesis is essential.

For a reducible parameter space, the generic point of one component may be bad while another component contains feasible points.

Therefore, the correct algorithmic principle is:

\\[ \boxed{ \text{Cover the parameter space by finitely many irreducible pieces,} } \\]

and test each piece separately.

The report correctly recognizes that a cover is sufficient and that a maximal irreducible-component decomposition is unnecessary.

However, there is a technical issue in the proposed implementation.

The assertion that a determinantal subset of an affine Grassmann chart is automatically irreducible is not true for arbitrary structured determinantal varieties. Determinantal varieties defined by generic matrix entries have familiar irreducibility properties, but imposing special linear relations among the entries can produce reducible varieties.

Consequently, the report must establish irreducibility of its particular chart pieces, rather than relying on the word *determinantal* alone.

A safe alternative is to parameterize the relevant fibre directly by an affine space or a projective space, or explicitly decompose any reducible chart locus into irreducible pieces.

**Verdict:** Theorem A is correct under the stated algebraic hypotheses. Its proposed use in the algorithm is also correct once the irreducibility of the actual parameter pieces is established.

101_hyperplane_layer_complete.md

## **2.3 Theorem B: the&#x20;**\\(p=1,\ q=n-2\\)**&#x20;non-eigen obstruction**

Theorem B is particularly useful because it gives a genuine impossibility result.

The hypotheses are

\\[ p=1,\qquad q=n-2,\qquad r_0=0. \\]

For a non-eigen direction,

\\[ \dim U_v=2. \\]

The report uses

\\[ \rho=\operatorname{rank}[C;CA]\leq 2 \\]

and

\\[ k=n-\rho. \\]

Since

\\[ \omega=k-1=n-\rho-1, \\]

we compare the available ambient dimension with the required compressed rank.

The proof separates into two cases.

**Case 1:**

\\[ n-2-p\<k-1. \\]

The compressed pencil has insufficient rank, and condition (5b) fails identically.

**Case 2:**

\\[ n-2-p=k-1. \\]

Here the prescribed row count forces the observer row space to occupy the entire admissible ambient space:

\\[ V=U_v^\perp. \\]

After choosing suitable bases, the compressed pencil reduces to a square pencil

\\[ \lambda X'-G', \\]

where \\(X'\\) is nonsingular.

Therefore,

\\[ \det(\lambda X'-G') \\]

is a polynomial of degree exactly \\(k-1\\).

For \\(k-1\geq1\\), the fundamental theorem of algebra guarantees a complex root. At that root, the rank drops.

Hence condition (5b) fails.

### **Why the restriction&#x20;**\\(q=n-2\\)**&#x20;matters**

This is not a cosmetic assumption.

The argument needs the dimension equality that forces

\\[ V=U_v^\perp. \\]

Without it, the observer row space can be a proper subspace of the admissible ambient space, and the square-pencil argument no longer follows.

The report explicitly corrects this point, which is important.

**Verdict:** Theorem B is a useful special-case obstruction. It should be presented as a theorem for the full-row-space pattern, not as a general statement about \\(p=1\\).

## **2.4 Proposition C: the zero-frequency rank identity**

Proposition C states

\\[ \boxed{ \operatorname{rank}H_A = \dim(AK_0) - \dim(AK_0\cap V^\perp). } \\]

This identity is correct and particularly valuable.

To see this, note that

\\[ \operatorname{im}(AN)=AK_0. \\]

Thus

\\[ \operatorname{rank}(LAN) = \operatorname{rank}(L|\_{AK_0}). \\]

The kernel of the restriction \\(L|\_{AK_0}\\) is

\\[ AK_0\cap\ker L. \\]

Since

\\[ \ker L=V^\perp, \\]

rank-nullity gives the result.

Now condition (5b) at \\(\lambda=0\\) requires

\\[ \operatorname{rank}(-H_A)=\omega. \\]

Consequently,

\\[ \boxed{\operatorname{rank}H_A=\omega.} \\]

This is a necessary condition for feasibility.

An especially important consequence is that if

\\[ v\in AK_0, \\]

then \\(v\in V^\perp\\) as well, so

\\[ \dim(AK_0\cap V^\perp)\geq1. \\]

Hence

\\[ \operatorname{rank}H_A\leq\ell-1. \\]

Feasibility therefore requires

\\[ \boxed{\ell\geq\omega+1=k.} \\]

This is a very inexpensive necessary test.

### **Connection with Paper II**

Paper II already uses the consequence of condition (5b) at zero frequency:

\\[ \pi_1(W)=\pi_2(W). \\]

Proposition C gives a more geometric interpretation of the same phenomenon: the restriction of \\(L\\) to \\(AK_0\\) must retain full rank \\(\omega\\).

This is a useful strengthening of the geometric language of Paper II.

**Recommendation:** Proposition C should be moved earlier in the report, perhaps immediately after the hyperplane-layer reduction. It gives a fast algebraic pruning test before any fibre construction or gcd calculation.

## **2.5 Proposition D: the eigenvector criterion is not sufficient**

The report gives an explicit counterexample with

\\[ n=5,\qquad p=1,\qquad C=e_5^{\mathsf T}. \\]

It establishes that

\\[ e_1\in K_0 \\]

is an eigenvector, yet the entire corresponding fibre fails condition (5b) at zero frequency.

The key computation is

\\[ \ell=\dim(AK_0)=2=\omega. \\]

Since

\\[ e_1\in AK_0 \\]

and every admissible row space annihilates \\(e_1\\), Proposition C gives

\\[ \operatorname{rank}H_A\leq1<2=\omega. \\]

Therefore no admissible observer in that fibre can satisfy the spectral condition.

This is a rigorous counterexample to the naive conjecture

\\[ K_0\text{ contains an eigenvector} \Longrightarrow \text{the hyperplane layer is feasible}. \\]

It also demonstrates why the zero-frequency condition cannot be omitted.

**Verdict:** Proposition D is conceptually important. It prevents the compression-eigenvector condition from being mistaken for a complete feasibility criterion.

# **3. The most important issue: Proposition E and the geometry of the admissible directions**

This is where I would make the most substantial revision to Report 101.

## **3.1 What Proposition E actually proves**

Let

\\[ \pi\_{K_0}:\mathbb R^n\longrightarrow K_0 \\]

be the orthogonal projection, and define the compressed operator

\\[ M=\pi\_{K_0}A|\_{K_0}. \\]

For a non-eigen direction \\(v\\), the report proves that admissibility implies

\\[ \boxed{Mv\in\operatorname{span}(v).} \\]

In other words,

\\[ Mv=\mu v \\]

for some scalar \\(\mu\\).

The proof uses the two functionals on \\(K_0\\):

\\[ \varphi_v(u)=u^{\mathsf T}v, \qquad \varphi\_{Av}(u)=u^{\mathsf T}Av. \\]

Since

\\[ V\cap K_0 \subseteq \\{u\in K_0: u^{\mathsf T}v=0,\  u^{\mathsf T}Av=0\\}, \\]

and

\\[ \dim(V\cap K_0)=k-1, \\]

the common kernel of the two functionals must have dimension at least \\(k-1\\).

Therefore, the functionals must be linearly dependent.

Because the inner product restricted to \\(K_0\\) is nondegenerate, this is equivalent to

\\[ \pi\_{K_0}(Av)\in\operatorname{span}(v). \\]

The proof is correct.

## **3.2 The terminology and known mathematical structures**

The most natural name is:

**Eigenvector of an orthogonal compression of an operator to a subspace.**

There are several closely related mathematical concepts.

| Area                     | Related concept                  | Relevance                                                            |
| ------------------------ | -------------------------------- | -------------------------------------------------------------------- |
| Operator theory          | Compression of a linear operator | The operator \\(M=\pi\_{K_0}A\|\_{K_0}\\)                            |
| Numerical linear algebra | Ritz vectors and Ritz values     | Eigenvectors of projected operators                                  |
| Spectral theory          | Invariant subspaces              | The line \\(\operatorname{span}(v)\\) is invariant under \\(M\\)     |
| Control theory           | Projected dynamics               | The action of \\(A\\) after projection onto an unobservable subspace |
| Algebraic geometry       | Projective eigenvarieties        | The set of eigenvector directions                                    |

The terminology *Ritz vector* is especially relevant when one studies an operator through a projection onto a lower-dimensional subspace.

However, there is an important distinction: the report is not merely studying an approximation to an eigenvalue of \\(A\\). It is studying exact eigenvectors of the compressed operator \\(M\\).

The eigenvalue \\(\mu\\) satisfies

\\[ \pi\_{K_0}(Av)=\mu v, \\]

but this does not imply

\\[ Av=\mu v. \\]

The component of \\(Av\\) outside \\(K_0\\) is precisely what distinguishes the non-eigen case.

I would therefore use the terminology:

> Admissible hyperplane directions are eigenvector directions of the orthogonal compression of \\(A\\) to \\(K_0\\).

This is precise and avoids introducing a new name for a familiar linear-algebraic object.

## **3.3 A necessary correction: eigenvalues are finite, but eigenvector directions need not be**

The report says that the hyperplane layer is a finite union of fibres, one for each eigenvalue of the compression.

This requires an important qualification.

The set of eigenvalues is finite, but the set of eigenvector directions need not be finite.

For an eigenvalue \\(\mu\\), define

\\[ E\_\mu=\ker(M-\mu I). \\]

The corresponding projective eigenvector set is

\\[ \mathbb P(E\_\mu). \\]

If

\\[ \dim E\_\mu=1, \\]

then \\(\mathbb P(E\_\mu)\\) consists of one point.

But if

\\[ \dim E\_\mu=d>1, \\]

then

\\[ \mathbb P(E\_\mu)\cong\mathbb P^{d-1} \\]

contains infinitely many directions.

For example, if

\\[ M=I_k, \\]

then every nonzero vector of \\(K_0\\) is an eigenvector.

Thus the compression-eigenvector condition does not generally reduce the parameter space to finitely many individual directions.

It reduces it to a finite union of projective eigenspaces:

\\[ \boxed{ \bigcup\_{\mu\in\operatorname{Spec}(M)} \mathbb P(\ker(M-\mu I)). } \\]

This distinction is fundamental.

### **Why this matters algorithmically**

Suppose an eigenvalue has geometric multiplicity \\(d\\).

Then the eigenvector direction itself contributes \\(d-1\\) projective parameters.

These parameters must be included in the generic feasibility test.

One cannot simply select one eigenvector for each eigenvalue and test the corresponding fibre. Doing so may miss feasible designs associated with other directions in the same eigenspace.

A correct algorithm must therefore:

1. Factor the characteristic polynomial of \\(M\\).
2. Construct the number field associated with each irreducible factor.
3. Compute the full eigenspace over that number field.
4. Parameterize its projectivization.
5. Incorporate the row-space parameters into the same algebraic family.
6. Apply the generic gcd criterion to each irreducible parameter piece.

This is a more accurate description of the proposed algorithm.

## **3.4 The eigen case must be included explicitly**

Proposition E is stated only for non-eigen directions.

However, if

\\[ Av=\lambda_0v, \\]

then

\\[ Mv=\pi\_{K_0}(Av)=\lambda_0v. \\]

Therefore, every eigenvector of \\(A\\) belonging to \\(K_0\\) is automatically an eigenvector of the compression.

The compression-eigenvector condition is consequently necessary for both types of admissible directions.

I suggest strengthening Proposition E to the following statement.

**Proposed Proposition E'.**

Let \\(v\in K_0\setminus\\{0\\}\\) be an admissible hyperplane direction. Then

\\[ \boxed{ \pi\_{K_0}(Av)\in\operatorname{span}(v). } \\]

In particular, every admissible direction belongs to the projective eigenvariety of \\(M\\).

The proof should treat the two cases separately:

- If \\(Av\notin\operatorname{span}(v)\\), use the two-functional argument.
- If \\(Av\in\operatorname{span}(v)\\), the result is immediate.

This formulation is cleaner and avoids leaving the eigen case outside the principal structural theorem.

## **3.5 A further geometric qualification: the fibre is not automatically a projective space**

There is another issue that should be addressed before using the fibre description in the complexity proof.

For a fixed direction \\(v\\), put

\\[ D_v=K_0\cap U_v^\perp. \\]

In the admissible case,

\\[ \dim D_v=k-1. \\]

Since

\\[ V\subseteq U_v^\perp \\]

and

\\[ V\cap K_0=D_v, \\]

we have

\\[ D_v\subseteq V\subseteq U_v^\perp. \\]

Thus \\(V\\) is determined by a subspace

\\[ V/D_v\subseteq U_v^\perp/D_v. \\]

The quotient has dimension

\\[ \dim(U_v^\perp/D_v) = \begin{cases} \rho-1,&v\text{ non-eigen},\\\ \rho,&v\text{ eigen}, \end{cases} \\]

where

\\[ \rho=\operatorname{rank}[C;CA]. \\]

This verifies the dimension calculation in the report.

However, the space of all possible \\(V\\)'s is not automatically a projective space.

If the observer row space has prescribed dimension \\(d_V\\), then the fibre is a Grassmannian:

\\[ \boxed{ \operatorname{Gr} \left( d_V-(k-1), \dim(U_v^\perp/D_v) \right). } \\]

If the row-space dimension is not prescribed, one obtains a union of Grassmannians, subject to the row-count restriction.

A projective-space description is valid only in the special case where the quotient subspace has dimension one.

This matters because the report repeatedly identifies the fibres with \\(\mathbb P^r\\). That identification needs an explicit dimensional hypothesis or a corrected parameterization.

**My recommendation:** Reformulate the layer as a finite union of families indexed by projective eigenspaces, with Grassmannian fibres over the admissible directions. Then use standard affine Grassmann charts to obtain irreducible parameter pieces.

This gives a mathematically correct geometric framework without losing the intended algorithmic structure.

# **4. Q2: When can a fixed common factor of the maximal minors occur?**

This is probably the most interesting structural question in Report 101 after Proposition E.

The third computational instance shows that excess dimension does not guarantee feasibility. The report finds that both compression eigenspace families are entirely bad, with a common factor of degree three in the maximal minors.

The natural question is whether this phenomenon can be characterized by a resonance between \\(A\\) and the compression.

I believe there is a useful way to formulate this problem.

## **4.1 The algebraic meaning of a common factor**

Let \\(X\\) be one irreducible parameter piece, with function field

\\[ K=\mathbb Q(X). \\]

Write the maximal minors as

\\[ m_1(x,\lambda),\ldots,m_s(x,\lambda) \in K[\lambda]. \\]

Suppose

\\[ g(x,\lambda) = \gcd(m_1,\ldots,m_s) \\]

has positive degree.

Then there exists an algebraic spectral value \\(\alpha\\), possibly depending on the parameters \\(x\\), such that

\\[ m_i(x,\alpha)=0 \qquad\text{for every }i. \\]

Equivalently,

\\[ \boxed{ \operatorname{rank}P_x(\alpha)<\omega } \\]

at the generic point of the parameter family.

This is stronger than saying that a particular point is bad.

It says that the entire irreducible family is bad at a generic spectral value.

An important distinction is that the common factor need not be a polynomial with constant coefficients. Its coefficients may belong to \\(K\\), so the bad spectral value can vary rationally or algebraically with the fibre parameters.

Therefore, I would distinguish:

- **Fixed resonance:** a common factor in \\(\overline{\mathbb Q}[\lambda]\\), independent of the fibre parameters.
- **Generic resonance:** a common factor in \\(\overline{\mathbb Q(X)}[\lambda]\\), possibly depending on the fibre parameters.

The second is the actual obstruction detected by Theorem A.

## **4.2 A useful formulation using the left-factor representation**

Under condition (5a),

\\[ H_A=SH \\]

for some matrix \\(S\\), and therefore

\\[ P(\lambda)=(\lambda I-S)H. \\]

The rank drops exactly when

\\[ \operatorname{im}H\cap\ker(\lambda I-S)\neq\\{0\\}. \\]

Thus badness is equivalent to the existence of an eigenvector of \\(S\\) lying in \\(\operatorname{im}H\\).

This gives a direct geometric interpretation of the common factor:

\\[ \boxed{ \text{A generic pencil is bad if its image subspace intersects an eigenspace of }S. } \\]

However, this is not yet a structural characterization of when the intersection must occur for every parameter value.

The difficulty is that both objects can vary:

\\[ H=H(x),\qquad S=S(x). \\]

We need to understand when

\\[ \operatorname{im}H(x) \cap E\_\lambda(S(x)) \neq\\{0\\} \\]

holds generically in \\(x\\) for some algebraic spectral branch \\(\lambda=\alpha(x)\\).

## **4.3 A proposed resonance criterion**

A useful intermediate object is the induced map

\\[ \overline S(x): \mathbb C^k/\ker H(x) \longrightarrow \mathbb C^q, \\]

but this formulation is not quite the most convenient because \\(S(x)\\) acts on the observer-row coordinates.

A cleaner approach is to use the pivot factorization from Paper I.

Choose a pivot block

\\[ H=XB, \\]

where

\\[ X\in K^{q\times\omega} \\]

has full column rank and \\(B\\) has full row rank.

Since

\\[ H_A=SH, \\]

we have

\\[ H_A=SX B. \\]

Writing

\\[ G=SX, \\]

we obtain

\\[ P(\lambda)=(\lambda X-G)B. \\]

Because \\(B\\) has full row rank,

\\[ \operatorname{rank}P(\lambda) = \operatorname{rank}(\lambda X-G). \\]

Thus the obstruction becomes

\\[ \operatorname{rank}(\lambda X-G)<\omega. \\]

Equivalently,

\\[ \exists z\neq0: \quad Gz=\lambda Xz. \\]

Therefore, the bad spectral values are generalized eigenvalues of the rectangular pair \\((G,X)\\).

The generic resonance question becomes:

> Under what conditions does a parameterized rectangular matrix pair \\((G(x),X(x))\\) possess a generalized eigenvalue over the function field of the parameter space?

This is a much more concrete formulation.

### **A possible theorem to investigate**

Let

\\[ \mathcal P(x,\lambda)=\lambda X(x)-G(x), \\]

where \\(X(x)\\) has full column rank.

Then generic badness is equivalent to the existence of a nonzero vector

\\[ z(x,\lambda) \\]

over an algebraic extension of \\(K(\lambda)\\) satisfying

\\[ G(x)z=\lambda X(x)z. \\]

A stronger sufficient condition is the existence of a nonzero rational-function vector \\(z(x)\\) and a scalar \\(\alpha(x)\\) such that

\\[ G(x)z(x)=\alpha(x)X(x)z(x). \\]

This gives a rational eigenvector section of the parameterized generalized eigenvalue problem.

It is not necessary in general, because the generic eigenvector may exist only over an algebraic extension of \\(K\\).

Nevertheless, it suggests a route through polynomial eigenvector equations and determinantal ideals.

## **4.4 The role of the compression**

The compression

\\[ M=\pi\_{K_0}A|\_{K_0} \\]

determines which kernel directions are admissible.

The left-factor operator \\(S\\), on the other hand, determines the spectral rank obstruction for a particular observer row space.

These are different operators acting in different spaces:

\\[ M:K_0\to K_0, \qquad S:\mathbb C^q\to\mathbb C^q. \\]

A resonance theory should connect them through the construction of \\(H\\), not simply identify their eigenvalues.

I would investigate whether the admissibility condition produces a structural relationship between:

1. the eigenspaces of \\(M\\);
2. the induced row-pair subspaces \\(W\\);
3. the generalized eigenstructure of \\((G,X)\\).

This is likely where a genuinely new theorem can emerge.

## **4.5 What should be computed next?**

For each irreducible fibre, record the following:

| Quantity                                       | Purpose                                                                              |
| ---------------------------------------------- | ------------------------------------------------------------------------------------ |
| \\(\gcd_I m_I\\)                               | Detects generic spectral failure                                                     |
| Degree of the gcd                              | Measures the number of generic bad spectral roots, counted with multiplicity         |
| Factorization of the gcd                       | Identifies possible spectral branches                                                |
| Resultant with \\(\det(\lambda I-M)\\)         | Tests whether a spectral branch is algebraically related to the compression spectrum |
| Rank of the corresponding coefficient matrices | Detects structural dependencies                                                      |
| Generic kernel dimension of \\(\lambda X-G\\)  | Measures the dimension of the spectral rank drop                                     |

One important caution: the spectral parameter \\(\lambda\\) in the observer pencil and the eigenvalue \\(\mu\\) of the compression need not coincide.

A resultant between the corresponding polynomials is a useful diagnostic, but a vanishing resultant alone does not establish the desired resonance.

**My conclusion on Q2:** The right starting point is a theory of generic generalized eigenvalues of parameterized rectangular matrix pairs, combined with the eigenspace geometry of the compression. I would not yet claim a complete resonance characterization.

# **5. Q3: Is fixed&#x20;**\\(p\\)**&#x20;the correct complexity boundary?**

This question requires the most careful distinction between the report and the two papers.

## **5.1 Why the report obtains&#x20;**\\(r\leq 2p\\)

The report defines

\\[ \rho=\operatorname{rank}[C;CA]. \\]

Since

\\[ K_0=\ker[C;CA], \\]

we have

\\[ k=n-\rho. \\]

In the hyperplane layer,

\\[ \omega=k-1=n-\rho-1. \\]

For a non-eigen direction,

\\[ \dim U_v=2, \\]

and, by the admissibility condition,

\\[ \dim(K_0\cap U_v^\perp)=k-1. \\]

Therefore,

\\[ \begin{aligned} \dim(U_v^\perp/(K_0\cap U_v^\perp)) &=(n-2)-(k-1)\\\ &=n-k-1\\\ &=\rho-1. \end{aligned} \\]

For an eigen direction,

\\[ \dim U_v=1, \\]

and the quotient dimension becomes

\\[ (n-1)-(k-1)=\rho. \\]

Hence

\\[ \boxed{ d\_{\mathrm{fib}}= \begin{cases} \rho-1,&\text{non-eigen},\\\ \rho,&\text{eigen}. \end{cases} } \\]

Since

\\[ \rho\leq 2p, \\]

we obtain

\\[ d\_{\mathrm{fib}}\leq2p. \\]

This calculation is correct.

It shows that the ambient quotient space used to describe the additional row-space choices has dimension bounded independently of \\(n\\) when \\(p\\) is fixed.

That is a meaningful structural observation.

## **5.2 Why this does not immediately prove Proposition G**

The report's complexity argument needs to bound all the parameters of the algorithm, not just the quotient dimension.

There are at least four different sources of complexity:

1. The number of compression eigenspaces.
2. The dimensions of those eigenspaces.
3. The number of parameters needed to describe each family of admissible row spaces.
4. The cost of the generic gcd computations, including the number and size of the maximal minors.

The first quantity is at most \\(k\\), which is polynomial in \\(n\\).

The second quantity can also be large.

This is exactly why the repeated-eigenvalue issue in Section 3.3 matters.

A large eigenspace contributes additional parameters that are not included in the report's original fibre count.

Consequently, the estimate

\\[ d\_{\mathrm{fib}}\leq2p \\]

alone is not sufficient to justify a fixed-\\(p\\) polynomial-time result.

The parameter count must include the projective eigenspace dimensions and the Grassmannian parameters.

## **5.3 A useful observation that may rescue the fixed-**\\(p\\)**&#x20;result**

There is nevertheless an important fact specific to the hyperplane layer.

Since

\\[ \omega=k-1 \\]

and

\\[ k=n-\rho, \\]

we have

\\[ \omega=n-\rho-1. \\]

Because the observer has at most \\(n\\) rows,

\\[ \omega\leq q\leq n. \\]

Therefore,

\\[ q-\omega\leq \rho+1\leq2p+1. \\]

This has a useful consequence for the number of maximal minors.

The number of \\(\omega\times\omega\\) maximal minors of a \\(q\times k\\) pencil is

\\[ \binom{q}{\omega}\binom{k}{\omega}. \\]

But here

\\[ \binom{k}{\omega}=\binom{k}{k-1}=k \\]

and

\\[ \binom{q}{\omega} = \binom{q}{q-\omega} \leq \sum\_{j=0}^{2p+1}\binom{n}{j}. \\]

For fixed \\(p\\), this is polynomial in \\(n\\).

Thus, unlike the general situation in Paper I, explicitly enumerating the maximal minors may actually be polynomial in the hyperplane layer when \\(p\\) is fixed.

This is a significant observation.

It suggests that the hyperplane specialization may genuinely permit a simpler complexity argument than the general fixed-parameter algorithm.

However, it still does not settle the repeated-eigenspace and fibre-parameter issues.

## **5.4 The connection with Paper I's Gram certificate**

Paper I avoids enumerating all maximal minors by compressing their coefficients through a Gram matrix.

The important formula is based on Cauchy–Binet:

\\[ \sum\_{I,J} f\_{I,J}(\lambda)f\_{I,J}(\mu), \\]

where \\(f\_{I,J}\\) are maximal minors.

This produces a certificate of size controlled by \\(\ell\\), rather than by the total number of minors.

In the hyperplane layer, however,

\\[ \omega=k-1. \\]

Consequently, the number of minors has a special combinatorial structure, as just shown.

For fixed \\(p\\), direct enumeration may already be polynomial.

I therefore recommend the following comparison.

| Approach                 | Advantages                                                               | Limitations                                                      |
| ------------------------ | ------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| Direct maximal-minor gcd | Conceptually simple; follows Theorem A directly                          | Requires coefficient-size and gcd-complexity analysis            |
| Paper I Gram certificate | Avoids maximal-minor enumeration; established certificate machinery      | Its natural parameter is \\(\ell\\), which may grow with \\(n\\) |
| Hybrid approach          | Exploits hyperplane combinatorics and uses Gram compression where useful | Requires a separate complexity proof                             |

The hybrid approach is particularly attractive.

## **5.5 The bit-complexity issue**

The report says that arithmetic in a number field of degree at most \\(k\\) is polynomial.

This statement needs more precision.

A number field

\\[ K=\mathbb Q[\mu]/(f) \\]

with \\(\deg f\leq k\\) can be represented using a polynomial basis.

Field operations are polynomial in \\(k\\) and the coefficient bit sizes, under standard representations.

Likewise, factorization of a univariate rational polynomial is polynomial-time in the standard bit model.

However, the complete algorithm also performs polynomial operations over

\\[ K(x_1,\ldots,x_d), \\]

where \\(d\\) is the number of fibre parameters.

To claim polynomial bit complexity for fixed \\(p\\), one must bound:

- \\(d\\);
- the number of polynomials;
- their degrees in the \\(x_i\\);
- their degrees in \\(\lambda\\);
- their coefficient bit lengths;
- the coefficient growth during the gcd computation.

The degree of the characteristic polynomial is \\(k\\), so the algebraic extension itself is not a problem if the necessary size bounds are established.

The more delicate issue is whether the full parameterization has dimension bounded solely by \\(p\\).

Repeated compression eigenvalues must be included in that calculation.

## **5.6 My recommendation for the complexity claim**

I would not abandon fixed \\(p\\) as the intended boundary.

It is a natural and potentially correct boundary for the hyperplane layer.

But I would revise Proposition G into two stages.

**Stage 1: establish a corrected geometric parameter bound.**

Prove that the entire family of admissible designs, including compression eigenspaces and Grassmannian fibres, admits a finite irreducible cover with uniformly bounded chart dimension for fixed \\(p\\).

**Stage 2: establish a bit-complexity bound on each chart.**

Use either the direct minor enumeration, exploiting

\\[ q-\omega\leq2p+1, \\]

or the Gram certificate from Paper I.

Then prove that each chart's generic gcd computation has polynomial bit complexity for fixed \\(p\\).

Only after these steps should the report state:

\\[ \boxed{ \text{The hyperplane-layer decision problem belongs to P for every fixed }p. } \\]

### **Can the boundary be expressed using&#x20;**\\(\ell\\)**&#x20;or&#x20;**\\(q_0\\)**?**

I do not think \\(q_0\\) is the right parameter for this question.

Paper II's \\(q_0\\) controls the algebraic lower bound on the observer order. It does not control the dimension of the compression eigenspaces or the number of parameters in the hyperplane geometry.

The quantity

\\[ \ell=\operatorname{rank}(AN) \\]

is more closely related to Paper I's complexity theory, but it is not necessarily bounded when \\(p\\) is fixed.

Indeed, it can be as large as \\(k\\), which is approximately \\(n\\).

Thus the two approaches have different strengths:

- Paper I: fixed-parameter tractability in \\(\ell\\).
- Report 101: a proposed fixed-\\(p\\) specialization based on the small codimension of \\(K_0\\).

I would preserve this distinction rather than trying to force the hyperplane result into the \\(\ell\\)-parameter framework.

**My conclusion on Q3:** Fixed \\(p\\) is a reasonable and potentially stronger specialization, but Proposition G needs a corrected geometric parameter count and a complete bit-complexity analysis. It is not yet justified by the quotient-dimension calculation alone.

# **6. Q4: Is Proposition F the same as the observability formulation in Paper I?**

The answer is: they describe the same spectral rank condition, but from different mathematical viewpoints.

This distinction is worth developing because it could produce a much cleaner exposition.

## **6.1 Proposition F: the eigenvector-incidence formulation**

Under

\\[ H_A=SH, \\]

we have

\\[ P(\lambda)=(\lambda I-S)H. \\]

Let

\\[ \mathcal R=\operatorname{im}H. \\]

Since \\(H:\mathbb C^k\to\mathbb C^q\\) has rank \\(\omega\\), the rank of \\(P(\lambda)\\) is

\\[ \operatorname{rank}P(\lambda) = \omega- \dim\left( \mathcal R\cap\ker(\lambda I-S) \right). \\]

Therefore,

\\[ \boxed{ \operatorname{rank}P(\lambda)<\omega \iff \mathcal R\cap E\_\lambda(S)\neq\\{0\\}. } \\]

This is a geometric statement.

The spectral condition fails precisely when the image subspace of \\(H\\) contains a nonzero eigenvector of \\(S\\).

Notice that \\(S\\) need not leave \\(\mathcal R\\) invariant. The relevant object is the intersection of \\(\mathcal R\\) with the eigenspaces of the ambient operator \\(S\\).

That distinction is important.

## **6.2 Paper I: the pivot-pencil formulation**

Paper I chooses a set of \\(\omega\\) pivot columns and writes

\\[ H=XB, \\]

where

\\[ X\in\mathbb R^{q\times\omega} \\]

has full column rank and

\\[ B\in\mathbb R^{\omega\times k} \\]

has full row rank.

Since

\\[ H_A=SH, \\]

we obtain

\\[ H_A=SX B. \\]

Set

\\[ G=SX. \\]

Then

\\[ P(\lambda) = (\lambda X-G)B. \\]

Because \\(B\\) has full row rank,

\\[ \boxed{ \operatorname{rank}P(\lambda) = \operatorname{rank}(\lambda X-G). } \\]

Thus condition (5b) becomes

\\[ \operatorname{rank}(\lambda X-G)=\omega \quad\forall\lambda\in\mathbb C. \\]

This is precisely the formulation used in Paper I to construct its finite spectral certificate.

The important point is that the matrix pair \\((X,G)\\) is rectangular:

\\[ X,G\in\mathbb R^{q\times\omega}. \\]

The condition is that

\\[ \lambda X-G \\]

have full column rank for every complex \\(\lambda\\).

## **6.3 The equivalence of the two pictures**

Since \\(H=XB\\) and \\(B\\) has full row rank,

\\[ \operatorname{im}H=\operatorname{im}X. \\]

Furthermore,

\\[ G=SX. \\]

Therefore,

\\[ (\lambda I-S)X=\lambda X-G. \\]

The incidence condition

\\[ \operatorname{im}X\cap E\_\lambda(S)\neq\\{0\\} \\]

is exactly equivalent to the existence of a nonzero vector \\(z\\) satisfying

\\[ (\lambda X-G)z=0. \\]

Thus Proposition F and the pivot-pencil formulation of Paper I are mathematically equivalent.

They are not competing characterizations.

They are two descriptions of the same obstruction:

**Geometric representation — Report 101**

\\[ \operatorname{im}H\cap E\_\lambda(S)\neq\\{0\\}. \\]

**Algebraic representation — Paper I**

\\[ \operatorname{rank}(\lambda X-G)<\omega. \\]

**Equivalent generalized eigenvector equation**

\\[ Gz=\lambda Xz,\qquad z\neq0. \\]

## **6.4 What is new in Proposition F?**

The algebraic certificate in Paper I answers:

> Does the rectangular pencil \\(\lambda X-G\\) lose column rank at some complex value?

Proposition F adds a geometric interpretation:

> Does the image of the pivot block contain an eigenvector of the ambient matrix \\(S\\)?

This is useful because it turns the spectral condition into an incidence problem between a subspace and an eigenspace.

For the hyperplane layer, this might be particularly valuable.

The observer family varies, but the incidence condition can sometimes be analyzed by studying how the admissible image subspaces intersect the eigenspaces of \\(S\\).

That could lead to a more direct structural proof of infeasibility than a full gcd computation.

### **A terminology correction**

I would avoid calling Proposition F an observability formulation without qualification.

The classical observability matrix is built from repeated products such as

\\[ C,\ CA,\ CA^2,\ldots. \\]

Proposition F instead describes the spectral rank condition through an eigenvector-incidence relation.

Paper I's Gram certificate is also not itself the classical observability matrix.

The most accurate description is:

> Proposition F gives an eigenspace-incidence interpretation of the same compressed pencil condition that Paper I tests using a pivot factorization and a Gram certificate.

**Verdict:** This is a genuinely useful complementary formulation, but not a different feasibility criterion. It should be presented as the geometric interpretation of Paper I's pencil factorization.

# **7. Q5: Can the eigenvector criterion be repaired by adding the zero-frequency rank condition?**

This question deserves a direct answer.

The proposed criterion is:

1. \\(K_0\\) contains an eigenvector of the compression.
2. The corresponding admissible family satisfies

\\[ \operatorname{rank}H_A=\omega. \\]

Would these conditions guarantee feasibility?

**No, not in general.**

The zero-frequency condition only excludes rank loss at \\(\lambda=0\\).

It does not exclude rank loss at nonzero spectral values.

## **7.1 Why the zero-frequency condition is insufficient**

Suppose

\\[ H_A=SH. \\]

Then

\\[ P(\lambda)=(\lambda I-S)H. \\]

The condition

\\[ \operatorname{rank}H_A=\omega \\]

means

\\[ \operatorname{rank}(SH)=\omega. \\]

Equivalently,

\\[ \operatorname{im}H\cap\ker S=\\{0\\}. \\]

Thus the image subspace avoids the zero eigenspace of \\(S\\).

But feasibility requires

\\[ \operatorname{im}H\cap E\_\lambda(S)=\\{0\\} \\]

for every complex \\(\lambda\\).

Avoiding the zero eigenspace does not imply avoiding the other eigenspaces.

A simple compressed-pencil example illustrates the distinction.

Take

\\[ H= \begin{pmatrix} 1\\\0 \end{pmatrix}, \qquad S= \begin{pmatrix} 2&0\\\ 0&3 \end{pmatrix}. \\]

Then

\\[ H_A=SH= \begin{pmatrix} 2\\\0 \end{pmatrix}. \\]

We have

\\[ \operatorname{rank}H=1, \qquad \operatorname{rank}H_A=1. \\]

Thus the zero-frequency condition is satisfied.

However,

\\[ P(\lambda) = \begin{pmatrix} \lambda-2\\\ 0 \end{pmatrix}, \\]

and therefore

\\[ \operatorname{rank}P(2)=0<1. \\]

The pencil fails at a nonzero spectral value.

This example illustrates the missing logical implication. A system-level counterexample would additionally have to realize the particular \\(H,H_A\\) through the prescribed \\(A,C,L_0\\), but the algebraic reason for insufficiency is already clear.

## **7.2 The correct repaired criterion**

The right repair is not to add another single rank condition.

Instead, one must combine the structural compression condition with the complete spectral certificate.

For a candidate direction \\(v\\), the following are necessary:

\\[ Mv\in\operatorname{span}(v), \\]

and

\\[ \operatorname{rank}H_A=\omega. \\]

But the sufficient condition is still

\\[ \gcd_I m_I(\lambda)=1 \\]

for at least one point of the corresponding admissible family.

On an irreducible family, this can be replaced by the generic gcd criterion of Theorem A.

Thus the correct logical structure is

\\[ \boxed{ \begin{aligned} &\text{Compression eigenvector condition}\\\ &+\text{zero-frequency rank condition}\\\ &+\text{generic spectral gcd condition}\\\ &\qquad\Longleftrightarrow \text{existence of a feasible point in the family}. \end{aligned} } \\]

The first two conditions are useful pruning rules.

The third is the actual spectral decision criterion.

## **7.3 A stronger possibility: characterize all bad spectral values**

There may be a more elegant route.

Since

\\[ P(\lambda)=(\lambda I-S)H, \\]

the bad spectral values are exactly those \\(\lambda\\) for which

\\[ \operatorname{im}H\cap E\_\lambda(S)\neq\\{0\\}. \\]

Suppose the spectrum of \\(S\\) is partitioned into distinct eigenvalues

\\[ \lambda_1,\ldots,\lambda_m. \\]

Then feasibility is equivalent to

\\[ \boxed{ \operatorname{im}H\cap E\_{\lambda_j}(S)=\\{0\\} \quad\text{for every }j. } \\]

This is a finite collection of subspace-intersection conditions.

It is equivalent to the pencil condition, but it may be easier to exploit when \\(S\\) has a particularly simple structure.

The difficulty is that \\(S\\) depends on the representation of the row inclusion and may not be uniquely determined outside the relevant quotient structure. The pencil itself is canonical, whereas a particular factor \\(S\\) need not be.

I would therefore use this as a structural analysis tool rather than immediately replacing the gcd algorithm.

**Verdict:** The proposed two-condition repair is not sufficient. The correct repair must retain the full spectral obstruction, either through the gcd criterion or through an equivalent eigenspace-intersection test.

# **8. A further issue: real feasibility versus algebraic feasibility**

There is an important logical distinction that should be made explicit in the report.

The original functional-observer problem asks for a real observer:

\\[ L\in\mathbb R^{q\times n}. \\]

However, the proposed algebraic procedure works with:

\\[ \overline{\mathbb Q(X)}[\lambda] \\]

and number fields associated with irreducible factors of the compression characteristic polynomial.

These are algebraically natural objects, but complex algebraic feasibility and real feasibility are not automatically equivalent.

## **8.1 Compression eigenvalues must be real**

The compression \\(M\\) is a real matrix.

A real admissible direction \\(v\\) must satisfy

\\[ Mv=\mu v \\]

with \\(v\in\mathbb R^k\setminus\\{0\\}\\).

Consequently, \\(\mu\\) must be real.

For example, if \\(M\\) has a characteristic polynomial with an irreducible quadratic factor

\\[ f(x)=x^2+1, \\]

that factor contributes no real eigenvector direction.

The algorithm should therefore distinguish:

- irreducible factors with real roots;
- irreducible factors without real roots.

Only the former can contribute real compression eigenvectors.

The appropriate exact procedure is to use real-root isolation for the characteristic polynomial, and then compute the eigenspace over the corresponding real algebraic number field or real algebraic extension.

## **8.2 Why Theorem A can still be used for real designs**

Suppose a fibre has a real algebraic parameterization by an affine space:

\\[ x=(x_1,\ldots,x_d)\in\mathbb R^d. \\]

If the generic gcd is one, the bad locus is a proper algebraic subset.

A proper algebraic subset cannot contain all of \\(\mathbb R^d\\).

Therefore, a real feasible point exists.

More generally, the same conclusion holds if the real points of the irreducible parameter piece are Zariski dense.

But this density property should be stated explicitly.

Irreducibility over an algebraically closed field alone does not imply that the real locus is nonempty or Zariski dense.

For example, an algebraic variety may have complex points but no real points.

### **Recommended correction**

Replace the unqualified statement

\\[ X\text{ contains a feasible point} \iff \gcd_I m_I=1 \\]

with a version that explicitly identifies the field and real-point hypothesis:

**Real generic-feasibility criterion.**

Let \\(X\\) be an irreducible algebraic parameter space defined over a real algebraic number field \\(K\\), and assume \\(X(K\_{\mathrm{real}})\\) is Zariski dense in \\(X\\). Suppose the matrices \\(H,H_A\\) are polynomial on \\(X\\), with constant rank \\(\omega\\).

Then

\\[ \boxed{ \begin{aligned} &\text{There exists a real feasible point of }X\\\ &\iff \gcd_I m_I=1 \quad\text{in }\overline{K(X)}[\lambda]. \end{aligned} } \\]

Here the real parameter space is understood through a fixed real embedding of the algebraic coefficient field.

This is the version needed for the original observer-design problem.

It is a relatively modest addition, but it is important for mathematical precision.

# **9. The two-way decision procedure: how I would revise the algorithm**

The proposed five-step algorithm has the right basic structure, but I would modify its first four stages to account for the geometry discussed above.

## **9.1 Revised algorithm**

```

Input:
    Rational matrices A, C, L0 and prescribed order q.

Step 1: Compression
    Compute K0 = ker[C; CA].
    Compute a rational basis N of K0.
    Compute k = dim K0 and rho = rank[C; CA].
    Set omega = k - 1.
    Compute the compression M = pi_K0 A|K0.

Step 2: Necessary-condition screening
    Check the structural dimension constraints.
    Apply the zero-frequency identity:
        rank(H_A) = omega.
    Use ell = rank(AN) to reject impossible cases.

Step 3: Compression eigenspaces
    Factor the characteristic polynomial of M over Q.
    Isolate its real roots.
    For every real algebraic eigenvalue mu:
        Compute the full eigenspace ker(M - mu I).
        Parameterize its projectivization.

Step 4: Admissible row-space families
    For every compression eigenspace:
        Construct the corresponding U_v and D_v.
        Parameterize the possible row spaces V/D_v
        using Grassmann charts.
        Retain the real parameter pieces.
        Verify irreducibility of each piece.

Step 5: Generic spectral test
    On every irreducible piece:
        Construct H(x), H_A(x).
        Compute the maximal minors of P_x(lambda).
        Compute their gcd over the function field.
        Degree zero: the piece contains real feasible points.
        Positive degree: the entire piece is bad.

Step 6: Decision
    Return FEASIBLE if at least one piece is generically good.
    Otherwise return INFEASIBLE.

```

The crucial correction is that Step 3 must retain the entire eigenspace, not a single eigenvector.

## **9.2 Why the algorithm is a two-way decision procedure**

The logic is:

- Proposition E' says every admissible direction belongs to a compression eigenspace.
- The fibre construction covers all admissible row spaces over those directions.
- Theorem A decides whether each irreducible piece contains a feasible point.
- The finite union is feasible exactly when at least one piece is feasible.

Thus the algorithm has both directions:

\\[ \text{FEASIBLE} \Longrightarrow \text{some piece has gcd }1, \\]

and

\\[ \text{some piece has gcd }1 \Longrightarrow \text{FEASIBLE}. \\]

This is substantially stronger than a numerical search over candidate observers.

## **9.3 What the implementation should report**

I recommend that each computational instance produce a certificate containing:

1. The exact characteristic polynomial of \\(M\\).
2. The real algebraic eigenvalues considered.
3. A basis for each full eigenspace.
4. The dimensions of the associated Grassmannian fibres.
5. The parameterization of each irreducible chart.
6. The exact maximal minors or an equivalent compressed certificate.
7. The gcd over the corresponding function field.
8. A Bézout identity when the gcd is one.
9. A nonconstant common factor when the gcd has positive degree.

For a feasible instance, a generic gcd equal to one establishes the existence of a real feasible point under the real-density condition. Nevertheless, for reproducibility, I would additionally extract an explicit real algebraic parameter value and verify the corresponding observer conditions.

For an infeasible instance, the proof must cover every irreducible piece. A positive-degree gcd on each piece gives a particularly useful exact certificate.

# **10. The computational experiments: what they establish and what they do not**

The three examples in Section II.7 are valuable because they demonstrate that the hyperplane layer is not governed by a simple dimension-counting principle.

The examples are:

| Instance | Compression characteristic polynomial | Reported outcome |
| -------- | ------------------------------------- | ---------------- |
| 1        | \\((x-1)(x^3+2x^2+4x+6)\\)            | Feasible         |
| 2        | \\(x(x-1)(x^2-8)\\)                   | Feasible         |
| 3        | \\((x-1)(x^3+4x^2+2x-5)\\)            | Infeasible       |

I particularly appreciate the use of algebraic eigenvalues in Instance 2.

The factor

\\[ x^2-8 \\]

has eigenvalues

\\[ \mu=\pm2\sqrt2. \\]

This illustrates why rational sampling of the compression eigenvectors is inadequate.

A search restricted to rational eigenvectors would miss these directions entirely.

## **10.1 Instance 1**

The report states that both fibres are good and provides an independent Bézout identity:

\\[ \sum_i g_i f_i=1. \\]

This is a strong form of verification.

It directly certifies that the maximal minors have no common complex root.

The identity is analogous to the certificate underlying Paper I, although the parameterized setting requires care about the coefficient field.

I recommend including the actual identity or a compact machine-readable representation in the computational appendix.

## **10.2 Instance 2**

This example demonstrates that an algebraic extension can reveal feasible directions unavailable over \\(\mathbb Q\\).

The computation in

\\[ \mathbb Q(\sqrt2) \\]

is particularly appropriate.

The report should specify whether the positive and negative roots are treated as separate real embeddings and whether the corresponding eigenspaces are both checked.

## **10.3 Instance 3**

This is arguably the most interesting example.

The report finds that both relevant families are entirely bad.

The implication is important:

\\[ n-2-p>\omega \\]

does not guarantee feasibility.

A sufficiently large ambient space does not prevent a structured family of pencils from having a common spectral root throughout the family.

This is a meaningful counterexample to a tempting geometric heuristic.

However, I would be careful with the phrase *first instance in the excess regime*.

That is a historical priority claim. Unless a systematic literature search has been conducted, the safer wording is:

> This example provides an exact infeasible instance in the excess-dimension regime and demonstrates that excess dimension alone is insufficient for feasibility.

The mathematical contribution does not depend on the priority claim.

## **10.4 A necessary computational audit**

The report honestly records two previous implementation bugs:

- zero coefficients remaining in polynomial dictionaries;
- an incorrect conversion of a rational number \\(p/q\\) into \\(p+q\mu\\), instead of \\(p/q\\).

I strongly recommend adding automated consistency checks.

For every polynomial computation:

\\[ \operatorname{normalize}(0)=0 \\]

must be enforced after arithmetic operations.

For every number-field conversion, verify the defining algebraic relation and compare exact evaluations against independently computed rational specializations whenever possible.

For each proposed gcd:

- verify that the gcd divides every maximal minor;
- verify that every maximal minor is divisible by the gcd;
- if the gcd is one, verify the corresponding Bézout identity;
- if the gcd is nonconstant, verify that its degree is positive and that it is a common divisor of every minor.

These checks are especially important because the conclusion of the entire decision procedure depends on the distinction between a zero and a nonzero polynomial.

# **11. How Report 101 should connect to the main results of Papers I and II**

I would strengthen the report by explicitly identifying which parts are inherited from the papers and which are genuinely new.

| Result                                               | Source                    | Role in the hyperplane analysis            |
| ---------------------------------------------------- | ------------------------- | ------------------------------------------ |
| Compression to \\(H,H_A\\)                           | Paper I                   | Reduces observer conditions                |
| Constant-rank pencil criterion                       | Paper I                   | Spectral feasibility test                  |
| Finite Gram certificate                              | Paper I                   | Alternative exact spectral test            |
| Subspace representation \\(W\\)                      | Papers I and II           | Removes dependence on individual free rows |
| Structural bound \\(\omega+1\leq\dim W\leq2\omega\\) | Paper I, used in Paper II | Bounds feasible design dimensions          |
| Minimum-order characterization                       | Paper II                  | Connects feasibility to optimization       |
| Hyperplane kernel direction \\(v\\)                  | Report 101                | New specialization                         |
| Compression eigenvector condition                    | Report 101                | New geometric reduction                    |
| Projective closedness argument                       | Report 101                | Generic feasibility criterion              |
| Zero-frequency identity in terms of \\(AK_0\\)       | Report 101                | New necessary screening condition          |
| Left-factor eigenspace incidence                     | Report 101                | New geometric interpretation               |
| Fixed-\\(p\\) hyperplane complexity                  | Report 101                | Proposed new complexity result             |

This separation is important for academic writing.

Report 101 should not suggest that the two papers themselves establish the compression-eigenvector classification or the proposed hyperplane algorithm.

Those are new results.

Conversely, it should not repeat the full proof of Paper I's Gram certificate or Paper II's minimum-order theorem unless a specific part is needed for the hyperplane argument.

## **11.1 A useful connection with Paper II's structural bound**

Paper II proves

\\[ \omega+1\leq\dim W\leq2\omega. \\]

For the hyperplane layer,

\\[ \omega=k-1. \\]

Therefore,

\\[ k\leq\dim W\leq2k-2. \\]

This means the feasible compressed row-pair space must have dimension at least \\(k\\).

The lower bound has a direct interpretation: a feasible row-pair space cannot simply be the graph of a linear map on a \\(\omega\\)-dimensional space, because such a graph would produce a square pencil with a complex spectral root.

The additional dimension is essential.

This is closely related to the argument in Paper II proving that

\\[ \dim W\geq\omega+1. \\]

In Report 101, I would make this connection explicit.

It helps explain why the hyperplane layer is nontrivial: even though the kernel of \\(H\\) is only one-dimensional, the row-pair space must have at least one extra dimension beyond the compressed observer rank.

## **11.2 The zero-frequency condition as an independent lower-bound mechanism**

Paper II's spectral lower bound is based on

\\[ \operatorname{rank}[U_0;V_0] \leq\omega \leq s_0+t-1. \\]

Proposition C provides a different expression of the zero-frequency restriction:

\\[ \ell-\dim(AK_0\cap V^\perp)=\omega. \\]

These formulations should be compared.

The Paper II bound measures the additional dimension required to reconcile the prescribed row-space projections.

Proposition C measures how much of \\(AK_0\\) is lost under the restriction of the observer map.

They are related through the same zero-frequency equality, but they are not identical invariants.

A useful future result would be a unified necessary-condition theorem combining both:

\\[ \begin{aligned} \omega&\geq\operatorname{rank}[U_0;V_0],\\\ \omega&=\ell-\dim(AK_0\cap V^\perp),\\\ \omega&=k-1. \end{aligned} \\]

This could yield inexpensive rejection rules before any spectral gcd calculation.

# **12. Formal verification: what the Lean results establish**

The report includes several Lean 4 formalizations.

I consider this a positive aspect, but the scope of the formal verification needs to be described accurately.

The verified results include:

- The abstract rank identity underlying Proposition C.
- The implication from a nonzero intersection to rank loss.
- The existence of a common vector in the relevant kernel and image spaces.
- Two elementary algebraic facts concerning roots over algebraically closed fields.

These are useful mathematical building blocks.

However, the most important structural claims of Report 101 are not yet formally verified:

1. The complete compression-eigenvector reduction.
2. The construction of the admissible parameter families.
3. The projective closedness argument in the actual parameter spaces.
4. The equivalence between generic gcd computations and real feasibility.
5. The concrete computational instances.
6. The complete fixed-\\(p\\) complexity theorem.

The report acknowledges that the matrix bookkeeping in Theorem B and the concrete instances are not formalized.

I would recommend extending the Lean development in the following order:

| Priority | Formalization target                                | Reason                                      |
| -------- | --------------------------------------------------- | ------------------------------------------- |
| 1        | Proposition E'                                      | Establishes the central geometric reduction |
| 2        | Fibre characterization                              | Ensures no admissible observer is omitted   |
| 3        | Zero-frequency criterion                            | Already has a verified abstract foundation  |
| 4        | Projective incidence and closedness                 | Establishes the generic decision principle  |
| 5        | Equivalence of the pivot and incidence formulations | Connects Report 101 with Paper I            |
| 6        | Finite algebraic decision procedure                 | Establishes algorithmic completeness        |

I would not prioritize formalizing every computational detail immediately. The first priority should be formalizing the mathematical completeness of the parameterization.

# **13. My proposed research direction: three theorems that would substantially strengthen Report 101**

Rather than adding many independent observations, I recommend organizing the next stage around three central theorems.

## **Theorem 1: Complete characterization of admissible hyperplane directions**

This should be the first main theorem.

**Proposed statement.**

Let

\\[ K_0=\ker[C;CA] \\]

and let

\\[ M=\pi\_{K_0}A|\_{K_0}. \\]

If a real admissible observer exists in the hyperplane layer, then its kernel direction \\(v\\) satisfies

\\[ Mv=\mu v \\]

for some real eigenvalue \\(\mu\\).

Therefore, the admissible directions belong to

\\[ \bigcup\_{\mu\in\operatorname{Spec}\_{\mathbb R}(M)} \mathbb P(\ker(M-\mu I)). \\]

The next part should characterize exactly which directions and which Grassmannian fibre points satisfy the row-space constraints.

The first assertion is already essentially established by Proposition E and its immediate eigen-case extension.

The second assertion is what needs to be developed.

**Why this matters:** It provides a complete geometric reduction, rather than merely a necessary condition.

## **Theorem 2: Generic spectral feasibility on the admissible families**

For each irreducible real parameter piece \\(X_j\\), define the maximal minors

\\[ m\_{j,I}(x,\lambda). \\]

Assume the real points of \\(X_j\\) are Zariski dense.

Then

\\[ \boxed{ X_j\text{ contains a feasible observer} \iff \gcd_I m\_{j,I}=1 \text{ in }\overline{K_j(X_j)}[\lambda]. } \\]

Consequently,

\\[ \boxed{ \text{Hyperplane layer feasible} \iff \exists j: \gcd_I m\_{j,I}=1. } \\]

This theorem should include:

- the real-point hypothesis;
- the finite irreducible cover;
- repeated compression eigenvalues;
- all admissible Grassmannian fibre dimensions;
- the treatment of eigen and non-eigen directions.

This would turn Theorem A and Proposition E into a complete decision theorem.

## **Theorem 3: Fixed-**\\(p\\)**&#x20;polynomial-time complexity**

This should be the final theorem, not the starting assumption.

The desired result is

\\[ \boxed{ \operatorname{DEC}\_{c=1} \in\mathrm P \qquad\text{for every fixed }p. } \\]

Its proof should establish:

1. A finite cover of the admissible parameter space.
2. A bound on the total number of chart parameters.
3. A polynomial bound on the number of charts.
4. Polynomial bounds on the degrees and coefficient sizes of the maximal minors.
5. Polynomial bit complexity of the generic gcd tests.
6. Polynomial bit complexity of real algebraic eigenvalue and eigenspace computations.

The combinatorial identity

\\[ \binom{q}{k-1}\binom{k}{k-1} = k\binom{q}{q-k+1} \\]

and the bound

\\[ q-k+1\leq\rho+1\leq2p+1 \\]

are particularly useful ingredients.

They show that the hyperplane-layer minor count has a favorable dependence on fixed \\(p\\).

This may allow a direct polynomial-time proof without reproducing all of Paper I's more elaborate fixed-parameter machinery.

# **14. Recommended structure for a revised Report 101**

I would reorganize the report to make the mathematical progression more convincing.

**Part I. Hyperplane-layer reduction**

1. Notation and connection with Papers I and II.
2. The \\(c=1\\) condition.
3. The kernel-direction geometry.
4. Eigen and non-eigen cases.

**Part II. Structural theorems**

5. Projective closedness and generic feasibility.
6. Zero-frequency rank identity.
7. Compression-eigenvector characterization.
8. Complete fibre and Grassmannian parameterization.
9. Special obstruction for \\(p=1,\ q=n-2\\).

**Part III. Spectral geometry**

10. Left-factor representation.
11. Eigenspace-incidence interpretation.
12. Generic spectral resonance.
13. Relation with Paper I's pivot-pencil certificate.

**Part IV. Decision algorithm**

14. Algebraic compression eigenspaces.
15. Real algebraic parameterization.
16. Generic gcd algorithm.
17. Correctness theorem.

**Part V. Complexity**

18. Parameter counting.
19. Number of algebraic charts.
20. Polynomial bit-complexity proof for fixed \\(p\\).

**Part VI. Computational evidence**

21. Feasible examples.
22. Infeasible example.
23. Exact certificates.
24. Lean formalization and limitations.

I would move the current Section II.9 (Corrections) into a short methodological discussion or appendix. Its contents are important, but the main theorem sequence should not be interrupted by implementation history.

# **15. Final assessment of the five research questions**

Here are my direct answers.

| Question                                      | My assessment                                                                                          | Recommended direction                                                                                   |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| Q1. Compression eigenvectors                  | Yes, this is a standard projected-operator eigenvector condition.                                      | Use compression eigenvectors, Ritz vectors, and projective eigenvarieties as the relevant terminology.  |
| Q2. Common-factor resonance                   | A precise algebraic formulation is available, but a complete structural characterization remains open. | Study generic generalized eigenvalues of the parameterized pair \\((G,X)\\).                            |
| Q3. Fixed-\\(p\\) complexity                  | A promising and potentially correct complexity boundary, but the proof is incomplete.                  | Account for repeated eigenspaces, Grassmann charts, real algebraic computations, and coefficient sizes. |
| Q4. Left-factor formulation                   | Equivalent to Paper I's pivot-pencil formulation, but geometrically different.                         | Use it as the eigenspace-incidence interpretation of the same spectral condition.                       |
| Q5. Eigenvector plus zero-frequency condition | Not sufficient in general.                                                                             | Retain the full spectral gcd or equivalent all-eigenvalue incidence condition.                          |

# **16. Final research verdict**



Strong mathematical direction

Further proof required



I regard Report 101 as a meaningful extension of the two papers, with one particularly promising idea: the hyperplane condition reduces the admissible kernel directions to eigenvectors of a compressed operator.

That observation is not merely a computational convenience. It identifies an algebraic-geometric structure underlying a special case of the functional-observer problem.

However, I would distinguish the report's results as follows.

| Result                        | Assessment                                                             |
| ----------------------------- | ---------------------------------------------------------------------- |
| Theorem A                     | Mathematically sound under its algebraic hypotheses                    |
| Theorem B                     | Sound under its stated restrictive hypotheses                          |
| Proposition C                 | Correct and useful                                                     |
| Proposition D                 | Important and valid counterexample                                     |
| Proposition E                 | Correct for non-eigen directions; should be extended to the eigen case |
| Finite-fibre conclusion       | Requires correction for repeated eigenvalues and fibre geometry        |
| Proposition F                 | Correct and valuable geometric interpretation                          |
| Two-way algorithm             | Promising, but requires a complete real parameterization               |
| Proposition G                 | Plausible, but not yet proved as stated                                |
| Three computational instances | Useful exact evidence, subject to complete reproducible certificates   |

## **16.1 The three issues I would prioritize**

If I were continuing this research, I would concentrate on the following.

**First: resolve the geometry of the compression eigenspaces.**

This is the most fundamental issue.

The compression-eigenvector condition is a strong reduction, but the complete admissible set is a union of projective eigenspaces, not necessarily a finite set of directions.

The correct Grassmannian fibre parameterization must be established.

**Second: prove the fixed-**\\(p\\)**&#x20;complexity theorem.**

This is potentially the most important algorithmic contribution.

The combination

\\[ \rho\leq2p, \qquad \omega=k-1, \qquad q-\omega\leq2p+1 \\]

gives a particularly favorable combinatorial structure.

I would investigate whether it is possible to establish the entire polynomial-time result directly, rather than relying on the general fixed-parameter machinery of Paper I.

**Third: understand the generic spectral obstruction.**

The third computational instance suggests that infeasibility can be structural rather than accidental.

The generalized eigenvalue formulation

\\[ G(x)z=\lambda X(x)z \\]

is a promising way to investigate this.

A theorem identifying structural conditions that force a generic common factor would make the report substantially more than a specialized algorithmic result.

## **16.2 Overall publication potential**

My assessment is that the report contains the ingredients of a potentially publishable mathematical contribution, but I would not submit the current version as a completed theorem-driven paper.

The strongest potential contribution is not simply that a special layer can be decided by a gcd computation.

It is the combination of:

1. A compression-eigenvector characterization of admissible hyperplane directions.
2. An algebraic-geometric generic-feasibility criterion.
3. A finite, exact decision procedure.
4. A possible polynomial-time result for fixed output dimension \\(p\\).
5. Explicit examples showing that dimension excess does not guarantee feasibility.

The fixed-\\(p\\) theorem would be particularly valuable because it would provide a complexity result that is structurally different from Paper I's parameterization by \\(\ell\\).

I would therefore preserve the main direction of Report 101, but revise the geometric parameterization before investing heavily in the final complexity proof.

## **17. The most valuable next mathematical task**

I recommend making the following statement the immediate target of the next research iteration:

**Complete hyperplane-layer parameterization theorem.**

Let

\\[ M=\pi\_{K_0}A|\_{K_0}. \\]

For every real eigenvalue \\(\mu\\) of \\(M\\), define

\\[ E\_\mu=\ker(M-\mu I). \\]

Characterize the complete set of admissible observer row spaces associated with

\\[ [v]\in\mathbb P(E\_\mu), \\]

including both

\\[ Av\in\operatorname{span}(v) \\]

and

\\[ Av\notin\operatorname{span}(v). \\]

Then prove that the resulting design family has a finite cover by explicitly parameterized irreducible real algebraic varieties.

This single theorem would resolve the main logical gap between Proposition E and the proposed decision algorithm.

It would also provide the correct foundation for proving Proposition G.

**My final recommendation:** Do not move immediately to NP-hardness or unrestricted complexity. First settle the hyperplane layer completely. A rigorous fixed-\\(p\\) polynomial-time theorem would be a substantial result in its own right, and the compression-eigenvector geometry may provide a useful template for studying the higher-codimension layers \\(c\geq2\\).

The next step I would take is to work out the complete eigenspace-plus-Grassmannian parameterization and prove its dimension and irreducibility properties. That is the point on which the rest of Report 101 most strongly depends.