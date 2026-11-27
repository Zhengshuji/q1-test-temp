# Mathematical review of Report 64: rigidity, the non-invariant regime, and the next research direction

## 1. Overall assessment

Report 64 makes an important advance: it identifies a structural obstruction that substantially narrows the possible location of a hardness reduction.

The central theorem in Section II.6 is correct after one necessary qualification:

\\[ \boxed{ A(K_0)\subseteq K_0,\quad 0<\omega\<k \quad\Longrightarrow\quad \text{no feasible observer exists}. } \\]

The proof is sound in this range. However, the report states the conclusion for \\(c>0\\), which includes the boundary case

\\[ c=k,\qquad \omega=0. \\]

In that case the argument breaks down, and in fact feasible observers can exist—even under the stronger convention \\(\mathsf P\_{\mathrm{ind}}\\). I give an explicit counterexample below.

This correction does not undermine the main strategic conclusion. For positive compressed rank, the theorem establishes something stronger than the report's current wording:

> Every feasible observer with \\(A(K_0)\subseteq K_0\\) is impossible. More generally, whenever \\(A(V)\subseteq K_0\\), a feasible observer with \\(\omega>0\\) is impossible.

Consequently, the invariant-subspace multiplication gadget from Report 63 cannot be rescued simply by adding a nonzero \\(K_0\\)-to-complement block while still forcing the candidate subspace to be invariant inside \\(K_0\\).

The hardness workstream should therefore move away from invariant-subspace equations as the direct source of multiplication. The most promising remaining mechanism is the interaction between nonzero leakage out of \\(K_0\\) and the simultaneous lift constraints on \\((LN,LAN)\\).

My recommended order is:

1. Correct and formalize the rigidity theorem, including the zero-rank boundary.
2. Establish a precise fibre theorem for row-pair lifts at a fixed \\(V\\).
3. Characterize the non-invariant \\(c=1\\) branch more carefully, particularly its pencil obstructions.
4. Attempt a small nonzero-leakage gadget, probably with \\(c\ge2\\).
5. In parallel, consolidate the already established structural and membership results into a paper draft.

I would not abandon hardness, but I would stop treating the invariant-subspace multiplication gadget as a viable direct route.

## 2. Question 1: Line-by-line verification of the rigidity theorem

Let

\\[ K_0=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \qquad \dim K_0=k, \\]

and let \\(N\in\mathbb C^{n\times k}\\) have full column rank and image \\(K_0\\).

Set

\\[ H=LN,\qquad H_A=LAN, \\]

and suppose

\\[ \operatorname{rank}H=\omega,\qquad \dim\ker H=c=k-\omega. \\]

Write

\\[ V=\ker H. \\]

The exact compression gives

\\[ (5a)\iff \ker H\subseteq\ker H_A. \\]

Equivalently, every row of \\(H\\) and every row of \\(H_A\\) annihilates \\(V\\).

### 2.1 The first step: rows of \\(H\\) annihilate \\(V+AV\\)

Assume

\\[ A(K_0)\subseteq K_0. \\]

Then there exists a matrix \\(T\in\mathbb C^{k\times k}\\) such that

\\[ AN=NT. \\]

This \\(T\\) is the matrix representing \\(A|\_{K_0}\\) in the basis \\(N\\).

Consequently,

\\[ H_A=LAN=L T. \\]

More precisely, since \\(H=LN\\),

\\[ \boxed{H_A=HT.} \\]

Now let \\(v\in V\\). Since \\(Hv=0\\), condition (5a) also gives

\\[ H_Av=0. \\]

Using \\(H_A=HT\\),

\\[ HTv=0. \\]

Thus

\\[ Tv\in\ker H=V. \\]

We have therefore already proved

\\[ \boxed{T(V)\subseteq V.} \\]

There is an equivalent row-space argument. Every row \\(h\\) of \\(H\\) annihilates \\(V\\), and every row \\(hT\\) of \\(HT=H_A\\) also annihilates \\(V\\). Therefore

\\[ h(Tv)=0\qquad(v\in V). \\]

Hence every row of \\(H\\) annihilates \\(V+T(V)\\).

Since the rank of \\(H\\) is \\(\omega=k-c\\), this implies

\\[ \dim(V+T(V)) \le k-\omega=c. \\]

But \\(V\\) itself has dimension \\(c\\), so

\\[ \dim(V+T(V))\ge c. \\]

Consequently,

\\[ \dim(V+T(V))=c \\]

and

\\[ \boxed{T(V)\subseteq V.} \\]

This part of the argument is correct.

In fact, once \\(A(K_0)\subseteq K_0\\) is assumed, the inclusion \\(T(V)\subseteq V\\) follows directly from \\(H_A=HT\\) and the kernel inclusion. The dimension argument is useful because it also shows why the row-space equality below holds.

### 2.2 The second step: \\(\operatorname{row}H=V^\perp\\)

The row space of \\(H\\) is contained in the annihilator of its kernel:

\\[ \operatorname{row}H\subseteq V^\perp. \\]

The dimensions are

\\[ \dim\operatorname{row}H=\omega=k-c, \\]

and

\\[ \dim V^\perp=k-\dim V=k-c. \\]

Therefore

\\[ \boxed{\operatorname{row}H=V^\perp.} \\]

This equality is fully justified. It is simply the standard rank-nullity identity for a matrix with \\(k\\) columns.

Here \\(V^\perp\\) means the algebraic annihilator in the dual space \\(K_0^\*\\), not an orthogonal complement requiring a Hermitian inner product. That distinction is worth making explicit in the paper.

### 2.3 The third step: invariance of \\(V^\perp\\)

Since

\\[ T(V)\subseteq V, \\]

take any \\(\ell\in V^\perp\\). For every \\(v\in V\\),

\\[ (\ell T)v=\ell(Tv)=0. \\]

Thus

\\[ \ell T\in V^\perp. \\]

Therefore

\\[ \boxed{V^\perp T\subseteq V^\perp.} \\]

Equivalently, viewing covectors as columns, \\(V^\perp\\) is invariant under \\(T^{\mathsf T}\\).

This step is correct. There is no need for \\(T\\) to be diagonalizable or for the invariant subspace to have any special Jordan structure.

### 2.4 The fourth step: existence of a left eigenvector

If \\(\omega>0\\), then \\(V^\perp\\) is a nonzero finite-dimensional complex vector space.

It is invariant under the linear operator

\\[ \ell\longmapsto \ell T. \\]

Every linear operator on a nonzero finite-dimensional complex vector space has an eigenvector. Hence there exist

\\[ 0\ne\ell\in V^\perp,\qquad \lambda\in\mathbb C \\]

such that

\\[ \ell T=\lambda\ell. \\]

Equivalently, \\(\ell\\) is a left eigenvector of \\(T\\).

This step is correct precisely because the field is algebraically closed. Over \\(\mathbb R\\), the corresponding assertion would require a real eigenvalue and would not hold for every nonzero invariant subspace.

### 2.5 The fifth step: the left eigenvector gives a pencil rank drop

By the equality

\\[ \operatorname{row}H=V^\perp, \\]

there is a row vector \\(y\in\mathbb C^{1\times q}\\) such that

\\[ yH=\ell. \\]

Since \\(\ell\ne0\\), necessarily \\(y\ne0\\).

Now

\\[ P(\lambda)=\lambda H-H_A =\lambda H-HT. \\]

Therefore

\\[ \begin{aligned} yP(\lambda) &=y(\lambda H-HT)\\\ &=\lambda(yH)-(yH)T\\\ &=\lambda\ell-\ell T\\\ &=0. \end{aligned} \\]

Thus \\(P(\lambda)\\) has a nonzero left null vector, so

\\[ \operatorname{rank}P(\lambda)<\omega. \\]

This contradicts (5b), which requires

\\[ \operatorname{rank}P(\lambda)=\omega \qquad\forall\lambda\in\mathbb C. \\]

The contradiction is valid whenever \\(\omega>0\\).

### 2.6 The missing boundary case: \\(\omega=0\\)

The report states the theorem for \\(c>0\\). But

\\[ c>0 \\]

does not imply

\\[ \omega>0. \\]

Since \\(\omega=k-c\\), the omitted case is

\\[ c=k,\qquad \omega=0. \\]

When \\(\omega=0\\),

\\[ H=0,\qquad H_A=0 \\]

under the kernel inclusion, and the compressed pencil is identically zero:

\\[ P(\lambda)=0. \\]

Its rank is zero for every \\(\lambda\\), so (5b) is satisfied at the compressed level.

The eigenvector argument cannot start: \\(V^\perp=\\{0\\}\\) has no nonzero eigenvector.

More importantly, this is not just a technical gap. There are genuinely feasible examples.

## 3. An explicit counterexample to the theorem as currently stated

Take

\\[ n=3,\qquad p=1,\qquad q=1, \\]

and let

\\[ C=\begin{bmatrix}1&0&0\end{bmatrix}, \qquad A= \begin{bmatrix} 0&1&0\\\ 1&0&0\\\ 0&0&0 \end{bmatrix}. \\]

Then

\\[ CA=\begin{bmatrix}0&1&0\end{bmatrix}. \\]

Thus

\\[ K_0=\ker\begin{bmatrix} 1&0&0\\\ 0&1&0 \end{bmatrix} =\operatorname{span}\\{e_3\\}. \\]

Clearly,

\\[ A(K_0)=\\{0\\}\subseteq K_0. \\]

Hence the hypothesis \\(A(K_0)\subseteq K_0\\) holds, and \\(k=1\\).

Now choose

\\[ L_0=L=\begin{bmatrix}0&1&0\end{bmatrix}. \\]

The matrices are

\\[ LA=\begin{bmatrix}1&0&0\end{bmatrix}=C, \\]

and

\\[ CA=\begin{bmatrix}0&1&0\end{bmatrix}=L. \\]

Therefore

\\[ \operatorname{rank}[LA;L;CA;C] = \operatorname{rank} \begin{bmatrix} 1&0&0\\\ 0&1&0\\\ 0&1&0\\\ 1&0&0 \end{bmatrix} =2, \\]

while

\\[ \operatorname{rank}[L;CA;C] = \operatorname{rank} \begin{bmatrix} 0&1&0\\\ 0&1&0\\\ 1&0&0 \end{bmatrix} =2. \\]

Thus (5a) holds.

For every \\(\lambda\\),

\\[ \lambda L-LA = \begin{bmatrix} -1&\lambda&0 \end{bmatrix}. \\]

Since the rows \\(CA\\) and \\(C\\) already span the first two coordinate directions,

\\[ \operatorname{rank}[\lambda L-LA;CA;C]=2 =\operatorname{rank}[L;CA;C]. \\]

Thus (5b) also holds for every \\(\lambda\\).

Finally,

\\[ \operatorname{rank}[C;L]=2=p+q, \\]

so the example satisfies the stronger convention \\(\mathsf P\_{\mathrm{ind}}\\). Also, \\(L\\) has full row rank, so it satisfies \\(\mathsf P\_{\mathrm{full}}\\).

But

\\[ N=e_3,\qquad H=LN=0,\qquad H_A=LAN=0. \\]

Therefore

\\[ k=1,\qquad \omega=0,\qquad c=1>0. \\]

This is a feasible observer with \\(c>0\\) and \\(A(K_0)\subseteq K_0\\).

Correction required

The theorem in II.6 is false as stated. Its proof establishes the following corrected result:

\\[ \boxed{ \begin{gathered} A(K_0)\subseteq K_0,\quad 0<\omega\<k\\\ \Longrightarrow\quad \text{no feasible observer exists}. \end{gathered} } \\]

Equivalently,

\\[ \boxed{ A(K_0)\subseteq K_0,\quad 0\<c\<k \quad\Longrightarrow\quad \text{infeasible}. } \\]

The case \\(c=k\\) must be separated.

### 3.1 What happens in the zero-compressed-rank case?

If \\(H=0\\), then every row of \\(L\\) annihilates \\(K_0\\). Hence

\\[ \operatorname{row}L\subseteq K_0^\perp =\operatorname{row}[C;CA]. \\]

If \\(A(K_0)\subseteq K_0\\), then \\(K_0^\perp\\) is invariant under right multiplication by \\(A\\). Thus

\\[ \operatorname{row}LA\subseteq K_0^\perp. \\]

Consequently, if \\(L\\) has rows in \\(K_0^\perp\\), both \\(L\\) and \\(LA\\) lie in the row space of \\([C;CA]\\). This makes (5a) and (5b) automatic, subject to the required row-rank convention and the prescribed \\(L_0\\).

Under \\(\mathsf P\_{\mathrm{ind}}\\), the available dimension for independent rows modulo \\(\operatorname{row}C\\) is

\\[ d_C=\operatorname{rank}[C;CA]-\operatorname{rank}C. \\]

Thus the zero-compressed-rank branch can be feasible if the prescribed rows and the augmentation can be chosen with the required independence.

This boundary case should be explicitly included in the decision tree and in any theorem stated in the paper.

## 4. A stronger consequence: local rigidity for any feasible \\(V\\)

There is a useful strengthening of Section II.6 that directly answers Question 2.

The proof does not actually require all of \\(K_0\\) to be \\(A\\)-invariant. It only requires that the particular feasible subspace \\(V\\) satisfy

\\[ A(V)\subseteq K_0. \\]

### Proposition: local leakage rigidity

Suppose \\(V\subseteq K_0\\), \\(\dim V=c\\), and

\\[ A(V)\subseteq K_0. \\]

If an observer satisfies (5a) and has compressed rank

\\[ \omega=k-c>0, \\]

then

\\[ \boxed{A(V)\subseteq V.} \\]

Proof. Let \\(N\\) be a basis matrix of \\(K_0\\). Since \\(A(V)\subseteq K_0\\), the restriction of \\(A\\) to \\(V\\) can be represented in \\(K_0\\)-coordinates.

For every row \\(l_i\\) of \\(L\\), let

\\[ h_i=l_iN. \\]

Condition (5a) says that

\\[ l_iAv=0\qquad(v\in V). \\]

Because \\(Av\in K_0\\), this is precisely the statement that the compressed row \\(h_i\\) annihilates \\(A(V)\\). Also \\(h_i\\) annihilates \\(V\\).

Hence

\\[ \operatorname{row}H\subseteq(V+A(V))^\perp. \\]

It follows that

\\[ \omega\le k-\dim(V+A(V)). \\]

Since \\(\omega=k-c\\),

\\[ k-c\le k-\dim(V+A(V)), \\]

so

\\[ \dim(V+A(V))\le c. \\]

But \\(V\subseteq V+A(V)\\) and \\(\dim V=c\\). Thus

\\[ V+A(V)=V. \\]

Therefore \\(A(V)\subseteq V\\). \\(\square\\)

Now apply the original pencil argument to \\(V\\). Since \\(V\\) is invariant and \\(\omega>0\\), \\(V^\perp\\) is a nonzero invariant subspace of the dual action. It contains a left eigenvector, which gives a pencil rank drop.

We obtain the stronger conclusion:

\\[ \boxed{ \begin{gathered} \omega>0,\quad V=\ker H,\quad (5a),(5b)\\\ \Longrightarrow\quad A(V)\not\subseteq K_0. \end{gathered} } \\]

This is particularly important for the hardness programme.

It says that every feasible observer with positive compressed rank must have genuine leakage of \\(A(V)\\) out of \\(K_0\\). It is not merely necessary that \\(A(K_0)\not\subseteq K_0\\); the particular candidate kernel \\(V\\) must itself leak outside \\(K_0\\).

This is a sharper and more useful rigidity statement than II.6.

## 5. Question 2: Can \\(A\_{31},A\_{32}\\) break the rigidity and preserve the multiplication gadget?

The local rigidity proposition gives a fairly definitive answer for the original gadget.

### 5.1 Why the original invariant-subspace gadget cannot work

Recall the graph representation

\\[ V=\operatorname{graph}(X)\subseteq K_0, \\]

with a decomposition

\\[ \mathbb C^n=E\oplus F\oplus G, \qquad K_0=E\oplus F. \\]

The full invariance equation is

\\[ A\_{21}+A\_{22}X-XA\_{11}-XA\_{12}X=0, \\]

together with

\\[ A\_{31}+A\_{32}X=0. \\]

The second equation says exactly that

\\[ A(V)\subseteq K_0. \\]

The first then says that the component of \\(A(V)\\) outside \\(V\\), but inside \\(K_0\\), vanishes. Together they enforce

\\[ A(V)\subseteq V. \\]

But the local rigidity proposition says that any feasible \\(V\\) with \\(\omega>0\\) and \\(A(V)\subseteq K_0\\) must be invariant, and the pencil condition then rules it out.

Therefore:

\\[ \boxed{ \text{A feasible observer with }\omega>0 \text{ cannot satisfy }A\_{31}+A\_{32}X=0. } \\]

This means the multiplication gadget from Report 63 cannot be embedded by enforcing the full invariant-subspace equation, even if the ambient space \\(K_0\\) itself is not invariant under \\(A\\).

The obstacle is stronger than the global rigidity theorem: it applies to the individual candidate \\(V\\).

### 5.2 What role can the leakage blocks play?

The only viable regime is

\\[ A\_{31}+A\_{32}X\ne0. \\]

In other words, the candidate graph subspace must have a nonzero component of its image outside \\(K_0\\).

This changes the algebraic mechanism completely.

When \\(A(V)\subseteq K_0\\), the condition

\\[ l_iAv=0 \\]

can be interpreted as a condition on the compressed row \\(h_i=l_iN\\), because \\(Av\\) has coordinates in \\(K_0\\).

When \\(A(V)\not\subseteq K_0\\), that interpretation fails. The value \\(l_iAv\\) depends on the part of the ambient row \\(l_i\\) acting on the complement \\(G\\). This is the additional freedom that the invariant-subspace formulation suppresses.

Write

\\[ \mathbb C^n=K_0\oplus G \\]

and represent an ambient row as

\\[ l=(h,g), \\]

where \\(h\in K_0^\*\\) and \\(g\in G^\*\\). For \\(v\in K_0\\), write

\\[ Av=A\_{K}v+A_Gv, \\]

where

\\[ A_Kv\in K_0,\qquad A_Gv\in G. \\]

Then

\\[ l(Av)=h(A_Kv)+g(A_Gv). \\]

The condition (5a) becomes

\\[ \boxed{ h|\_V=0,\qquad h(A_KV)+g(A_GV)=0. } \\]

The second equation is now a coupled relation between \\(h\\), \\(g\\), and \\(V\\). This is where non-invariant geometry enters.

If \\(A_G|\_V\\) is sufficiently large, the \\(g\\)-variables may absorb the second constraint. That is why admissibility can become vacuous for bottom rows in some \\(c=1\\) cases. But this same freedom can also make it difficult to encode arithmetic: an existentially free \\(g\\) may remove the very equation one hoped to impose.

### 5.3 A more precise formulation of the leakage condition

Let

\\[ \pi_G:\mathbb C^n\to G \\]

be the projection along \\(K_0\\), and define the leakage map

\\[ J_V:V\to G,\qquad J_V(v)=\pi_G(Av). \\]

Then:

- \\(J_V=0\\) implies \\(A(V)\subseteq K_0\\), which is impossible for a feasible positive-rank observer.
- \\(J_V\ne0\\) is necessary, but not sufficient, for feasibility.
- The dimension and image of \\(J_V\\) determine how much freedom the complementary row component \\(g\\) has in satisfying \\(l(AV)=0\\).

For a fixed compressed row \\(h\\), the admissible complementary component \\(g\\) must solve

\\[ g\circ J_V=-h\circ A_K|\_V. \\]

Thus the exact solvability condition is

\\[ h\circ A_K|\_V\in\operatorname{im}J_V^\*, \\]

where

\\[ J_V^\*:G^\*\to V^\*,\qquad g\mapsto g\circ J_V. \\]

This is a useful linear-algebraic characterization. It makes the effect of leakage explicit.

In particular, if \\(J_V\\) is surjective onto its image, the dimension of the space of possible corrections \\(g\\) is

\\[ \dim G-\operatorname{rank}J_V, \\]

provided the right-hand side belongs to \\(\operatorname{im}J_V^\*\\).

### 5.4 My recommendation for the next gadget

Do not try to perturb the old multiplication gadget slightly. Its defining equation is the very condition that rigidity prohibits.

Instead, try to construct a gadget whose nonlinear relation arises from the compatibility of several row-lift equations:

\\[ g_i\circ J_V=-h_i\circ A_K|\_V, \\]

together with

\\[ \operatorname{rank}H=\omega \\]

and the pencil condition.

The first experiment should be a one-gate construction with:

- \\(J_V\ne0\\);
- at least two independent compressed rows;
- a nontrivial simultaneous lift condition;
- an explicit proof that the pencil is good.

I would use \\(c=2\\) as the initial target rather than \\(c=1\\). For \\(c=1\\), the lift equations are often too easily absorbed by a single complementary correction, as the report itself observes. With \\(c=2\\), the compatibility of the restrictions to a two-dimensional subspace may impose nontrivial relations.

This is a research proposal, not a construction already proved. I do not currently see a valid explicit nonzero-leakage multiplication gadget from the information in Report 64 alone.

## 6. Question 3: Is there a structural criterion for emptiness of the \\(c=1\\) non-invariant branch?

The report's decomposition is sensible:

\\[ \mathbb P(W_L) = \mathbb P(U)\ \dot\cup\ \bigl(\mathbb P(W_L)\setminus\mathbb P(U)\bigr), \\]

where

\\[ U=\\{v\in W_L:Av\in K_0\\}. \\]

The first branch is governed by the hyperplane lemma and eigenline analysis. The second branch is the genuine leakage branch.

I would distinguish three kinds of obstruction.

### 6.1 Obstruction A: a fixed eigenvector in the pencil kernel

For any candidate \\(V\\) and any lift \\(L\\), write

\\[ H_A=ZH \\]

on \\(\operatorname{im}H\\), and choose a splitting

\\[ Z=\begin{bmatrix}A\_\*\\\B\_\*\end{bmatrix}. \\]

As established in Report 62, the pencil condition is equivalent to

\\[ \ker(A\_\*-\lambda I)\cap\ker B\_\*=\\{0\\} \\]

for every eigenvalue \\(\lambda\\) of \\(A\_\*\\).

Thus a direct structural obstruction is:

\\[ \boxed{ \exists\\,0\ne y\in\ker(A\_\*-\lambda I)\cap\ker B\_\* \quad\Longrightarrow\quad \text{pencil failure}. } \\]

The important point is that this test is independent of diagonalizability. It only involves ordinary eigenspaces, not generalized eigenvectors.

For the \\(c=1\\) branch, this gives an exact test once a candidate lift is fixed.

### 6.2 Obstruction B: a common invariant subspace invisible to every attainable \\(B\_\*\\)

A more structural version would be to identify a nonzero subspace

\\[ E\subseteq\mathbb C^\omega \\]

such that, for every attainable lift over the relevant \\(V\\),

1. \\(E\\) is invariant under the corresponding \\(A\_\*\\);
2. \\(B\_\*|\_E=0\\).

Then every attainable pencil is bad.

This is a common-subspace obstruction. It is stronger than merely proving \\(B\_\*=0\\) for one lift, and it could potentially eliminate an entire family of candidates at once.

A particularly simple special case is

\\[ B\_\*=0 \\]

for every attainable lift. Then

\\[ P(\lambda)= \begin{bmatrix} (\lambda I-A\_\*)H\\\ 0 \end{bmatrix}, \\]

and the characteristic polynomial of \\(A\_\*\\) guarantees a rank drop.

The challenge is to derive such a common obstruction from the fixed data \\((A,C,L_0)\\), rather than checking it separately for every choice of bottom rows.

### 6.3 Obstruction C: a forced rank defect in the attainable row space

For fixed \\(V\\), define the admissible row-pair space

\\[ \mathscr P_V = \left\\{ (h,g)\in\mathscr P\_{A,C}: h|\_V=0,\ g|\_V=0 \right\\}, \\]

where

\\[ \mathscr P\_{A,C} = \\{(lN,lAN):l\in\mathcal X^\*\\}. \\]

The fixed rows \\(L_0\\) prescribe some of the row pairs. The remaining rows must be chosen from \\(\mathscr P_V\\).

One can then ask whether the attainable first components \\(h\\) span a sufficiently large subspace of \\(\operatorname{Ann}(V)\\). If their span has dimension below \\(\omega\\), then

\\[ \operatorname{rank}H<\omega \\]

for every lift, and the candidate is infeasible before the pencil is considered.

This is the natural generalization of the row-space certificates used in the \\(c=1\\) and \\(c=2\\) analyses.

### 6.4 Is full elimination unavoidable?

No, not always. The three obstructions above can produce exact structural certificates.

But if none applies, the remaining question is genuinely existential:

\\[ \exists V,\ \exists H,\ \exists H_A: \quad \text{lift constraints, rank constraints, and pencil conditions}. \\]

In that situation, algebraic elimination or real/complex quantifier elimination is the principled exact method.

I would therefore use the following order for the non-invariant branch:

1. Compute the attainable row-pair space for \\(V\\).
2. Test whether the first components can attain rank \\(\omega\\).
3. Test whether a common pencil obstruction forces an eigenvector in \\(\ker B\_\*\\).
4. If neither test eliminates the branch, perform exact elimination.

This is better than treating the whole complement as a generic open set. An open feasible locus may be nonempty, but openness alone does not decide whether it is empty.

## 7. Question 4: Which observer convention should the project adopt?

The report distinguishes

\\[ \mathsf P\_{\mathrm{ind}}: \operatorname{rank}[C;L]=p+q \\]

from

\\[ \mathsf P\_{\mathrm{full}}: \operatorname{rank}L=q. \\]

These are not equivalent.

Indeed,

\\[ \operatorname{rank}[C;L]=p+q \\]

implies that \\(L\\) has full row rank, but the converse need not hold. The difference is whether the rows of \\(L\\) are independent modulo the row space of \\(C\\).

### 7.1 What follows from the displayed rank conditions?

The rank conditions (5a) and (5b), as written in Report 64, do not themselves impose

\\[ \operatorname{rank}[C;L]=p+q. \\]

They also do not impose full row rank of \\(L\\) unless that is included as a separate observer requirement.

Therefore, from the algebraic problem stated in the report alone, one cannot decide which convention is intended.

The distinction must come from the precise definition in the original observer formulation or paper.

### 7.2 My recommendation

Do not select \\(\mathsf P\_{\mathrm{ind}}\\) merely because it gives a cleaner lift-completion theorem, and do not select \\(\mathsf P\_{\mathrm{full}}\\) merely because it is weaker.

Instead:

1. Identify the exact definition of a functional observer in the source that motivates the project.
2. Check whether it requires \\(L\\) to have full row rank, or requires \\([C;L]\\) to have full row rank.
3. Check whether rows of \\(L\\) are regarded as independent observer coordinates modulo the measured output \\(C x\\).
4. State the chosen convention explicitly in the problem definition.

Until this is settled, keep both problems separate:

\\[ \mathrm{DEC}\_{\mathrm{ind}}(q), \qquad \mathrm{DEC}\_{\mathrm{full}}(q). \\]

The rigidity theorem and its counterexample apply to both conventions, as the explicit example demonstrates. The pair-lift completion criterion, however, can differ.

The report's statement that the two test instances are infeasible under \\(\mathsf P\_{\mathrm{ind}}\\) is not automatically a proof of infeasibility under \\(\mathsf P\_{\mathrm{full}}\\). The compressed row-space arguments may transfer, but the simultaneous lift and independence steps must be rechecked.

## 8. Question 5: Which hardness source and which gadget should come next?

### 8.1 ETR remains the better source problem

I agree with the report's shift toward an arithmetic-circuit formulation of ETR.

Affine rank minimisation is not mathematically ruled out, but the natural direct encoding is poorly matched to the observer structure. By contrast, the observer geometry contains:

- bilinear and quadratic expressions in chart variables;
- linear constraints on row-pair lifts;
- rank conditions;
- an all-eigenvalues spectral condition.

This is a plausible environment for an arithmetic-circuit reduction, provided the construction uses the leakage variables and the row-pair coupling rather than simply identifying the source variables with \\(H\\) or \\(X\\).

### 8.2 The smallest gadget is now a leakage gadget, not an invariant multiplication gadget

The old order was:

1. multiplication;
2. variable sharing;
3. addition;
4. rank forcing.

The rigidity result changes this order.

I would now use:

1. A leakage feasibility gadget: exhibit a non-invariant \\(V\\) with \\(A(V)\not\subseteq K_0\\), and calculate all admissible row pairs.
2. A nontrivial compatibility gadget: force a relation among at least two row pairs through the same \\(V\\) and the same lift data.
3. A multiplication gate: show that the compatibility relation encodes \\(z=xy\\), or another nontrivial quadratic equation.
4. A spectral gadget: guarantee the eigenspace-injectivity criterion for every intended source assignment.
5. Variable sharing and addition.

The reason for putting leakage first is simple: without it, the rigidity theorem eliminates the candidate before any arithmetic construction matters.

### 8.3 What should be the first concrete experiment?

I recommend a deliberately small problem:

- Take \\(c=2\\).
- Choose \\(K_0\\) of dimension at least \\(4\\).
- Choose a candidate plane \\(V\\) for which\
  \\[\
  \dim\pi_G(A(V))=1.\
  \\]
- Compute the exact space of row pairs \\((h,g)\\) satisfying\
  \\[\
  h|\_V=0,\qquad h(A_KV)+g(A_GV)=0.\
  \\]
- Impose the fixed top-row conditions.
- Determine whether the requirement\
  \\[\
  \operatorname{rank}H=\omega\
  \\]\
  produces a nontrivial polynomial relation among the coordinates describing \\(V\\).

The choice of one-dimensional leakage is intentional. It is the smallest case in which the complementary lift has a nontrivial but not completely unconstrained role.

If the resulting rank condition only says that certain vectors are independent, then the construction may be too weak. If it produces a determinant or a bilinear relation involving the chart variables, it may be a useful gate.

I would not begin by attempting a large circuit. A one-gate construction with a fully proved equivalence is the appropriate first milestone.

## 9. Question 6(a): Further audit of the \\(c=1\\) and \\(c=2\\) arguments

The rigidity theorem is the main new result, but the report also asks for a check of the low-\\(c\\) classifications. I can verify the underlying logic of the \\(c=1\\) hyperplane argument from the stated assumptions. The \\(c=2\\) certificate cannot be fully verified without the actual matrices defining \\(\mathrm{Des}\\).

### 9.1 The \\(c=1\\) hyperplane lemma

Suppose

\\[ V=\mathbb Cv,\qquad \omega=k-1, \\]

and assume

\\[ W_L\subseteq D=K_0\cap A^{-1}K_0. \\]

For a feasible observer, the fixed top rows imply

\\[ L_0Nv=0,\qquad L_0ANv=0. \\]

For each bottom row \\(l_i\\), write

\\[ h_i=l_iN. \\]

Then

\\[ h_iv=0,\qquad l_iAv=0. \\]

Because \\(v\in D\\), we have \\(Av\in K_0\\). Write

\\[ Av=Nw. \\]

It follows that

\\[ h_iw=l_iNw=l_iAv=0. \\]

Thus every row of \\(H\\) annihilates both \\(v\\) and \\(w\\).

If \\(w\notin\mathbb Cv\\), then \\(v,w\\) are linearly independent. The space

\\[ \operatorname{Ann}(V) \\]

has dimension \\(k-1=\omega\\), and imposing the additional condition \\(h(w)=0\\) cuts it down to dimension \\(k-2\\). Consequently,

\\[ \operatorname{rank}H\le k-2<\omega, \\]

a contradiction.

Therefore any feasible \\(V\\) in this branch must be an eigenline:

\\[ Av=\lambda v. \\]

This is a correct argument. It does not depend on \\(\mathsf P\_{\mathrm{ind}}\\); it uses the compressed rank condition and the common-lift relation for each row.

There are two qualifications worth retaining in the formal statement:

1. The condition \\(W_L\subseteq D\\) is essential. Without \\(Av\in K_0\\), the expression \\(h_iw\\) is not defined as a restriction to \\(K_0\\) in the required way.
2. The eigenline case is not automatically feasible. It must still satisfy the fixed-row conditions, the lift conditions, the rank condition, and the pencil condition.

The report's use of the functional \\(\varphi\\) to eliminate tested eigenlines is therefore appropriate, provided the explicit computation of \\(\varphi\\) is included in the certificate.

### 9.2 The \\(c=1\\) leakage branch

The report states that when

\\[ W_L\not\subseteq D, \\]

admissibility is vacuous because every compressed row \\(h\\) has an admissible lift through a \\(g_0\\) adjustment.

That conclusion is plausible, but it is not independently verifiable from the summary. The exact formula for \\(g_0\\), its domain, and the relevant rank assumptions are needed.

More importantly, even if every individual compressed row has an admissible lift, one must distinguish:

- individual row-lift existence;
- simultaneous choice of all bottom rows;
- independence of the resulting rows under \\(\mathsf P\_{\mathrm{ind}}\\);
- full row rank under \\(\mathsf P\_{\mathrm{full}}\\).

These are different assertions.

The report should state the vacuity result at the individual-row level first, and then state the separate simultaneous-completion theorem.

### 9.3 The \\(c=2\\) forced-plane certificate

The report claims that, for a forced plane, the admissibility system either forces a coefficient \\(b_i=0\\) or permits it, and that when all bottom rows are forced,

\\[ \operatorname{rank}H=1<\omega. \\]

It then gives

\\[ \alpha=(-1,0),\qquad \alpha^{\mathsf T}\mathrm{Des}=e_b. \\]

This is potentially a very useful exact certificate: it shows that the relevant coefficient direction is forced to vanish by a linear combination of the admissibility equations.

However, I cannot verify the identity without the actual matrix \\(\mathrm{Des}\\), the definition and ordering of its columns, and the equation system it represents.

For a paper-quality proof, include:

1. the full matrix \\(\mathrm{Des}\\);
2. the coefficient vector \\(e_b\\);
3. the exact multiplication\
   \\[\
   (-1,0)\mathrm{Des}=e_b;\
   \\]
4. the derivation that the corresponding right-hand side must vanish;
5. the resulting rank bound on \\(H\\).

The conclusion should also be stated with the precise hypotheses under which the plane is forced. A certificate for one fixed plane is not automatically a certificate for every possible \\(V\\).

## 10. Question 6(d): Assessment of the component-bound programme

The component-bound programme is mathematically distinct from the hardness reduction. I recommend preserving it as a separate workstream. It may lead to useful algorithmic results even if the complexity question remains unresolved.

There are two aspects to assess.

### 10.1 The invariant part

The report claims that for a fixed eigenvalue-labelled Jordan type, the corresponding invariant-subspace stratum is irreducible or empty.

The proposed parameterisation uses cyclic generators for the Jordan blocks. This is a reasonable approach, but the proof must be formulated carefully.

For an eigenvalue \\(\lambda\\), let

\\[ T\_\lambda=A-\lambda I. \\]

Suppose the restriction of \\(T\_\lambda\\) to the candidate invariant subspace has Jordan type

\\[ \mu=(\mu_1,\ldots,\mu_b). \\]

One can attempt to parameterise the stratum by vectors

\\[ x_i\in\ker T\_\lambda^{\mu_i}, \qquad T\_\lambda^{\mu_i-1}x_i\ne0, \\]

such that all the chain vectors

\\[ x_i,\ T\_\lambda x_i,\ \ldots,\ T\_\lambda^{\mu_i-1}x_i \\]

are linearly independent across all \\(i\\).

The relevant parameter space is a subset of

\\[ \prod\_{i=1}^b\ker T\_\lambda^{\mu_i}. \\]

The nonvanishing and independence conditions are open conditions. Hence, if the parameter space is nonempty, it is an open subset of a product of vector spaces and is irreducible.

Its image under the map taking the generators to the span of their Jordan chains is the desired invariant-subspace stratum.

This is a promising proof architecture. There are, however, details to make explicit:

- For multiple eigenvalues, the Jordan blocks must be labelled by their eigenvalues.
- The generators for different eigenvalues must be combined into a single parameter space.
- The chain-independence condition must ensure that the total dimension is exactly \\(c\\).
- The map to the Grassmannian must be shown to be a morphism on the open set where the required minors are nonzero.

If these points are supplied, the irreducibility claim is credible.

The bound

\\[ N\_{\mathrm{inv}}(c) \le \sum\_{\lambda\vdash c}s^{b(\lambda)} \\]

then follows by counting the possible eigenvalue-labelled Jordan types, where \\(s\\) is the number of distinct eigenvalues of the relevant operator.

I would nevertheless avoid presenting this as established until the parameterisation is written out for general partitions, rather than only for a single cyclic block. A single cyclic vector proves the case \\(\mu=(c)\\); it does not alone prove the general partition case.

### 10.2 The non-invariant part and the \\(B\_{u,v}\\) strata

The report correctly warns that the sets

\\[ B\_{u,v} = \\{U:\dim(U\cap A^{-1}U)=v\\} \\]

need not be irreducible.

The example

\\[ A=\operatorname{diag}(0,1),\qquad u=v=1 \\]

is illustrative. An invariant line must be one of the two eigenspaces, so this stratum consists of two points.

This matters because an argument that counts only one irreducible component per pair \\((u,v)\\) would be invalid.

The quadratic chart

\\[ F_A(X)= \begin{bmatrix} A\_{21}+A\_{22}X-XA\_{11}-XA\_{12}X\\\ A\_{31}+A\_{32}X \end{bmatrix} \\]

is the right local representation of the relevant incidence condition.

The proposed uniform Bézout bound

\\[ b\_{u,v} \le \binom{k}{u} \bigl(2(u-v+1)\bigr)^{u(k-u)} \\]

is a possible route to an explicit component bound. But I would want to check three technical points before accepting it as a theorem:

1. Degree control. Are all equations used to define the relevant rank stratum of degree at most \\(2(u-v+1)\\), including the minors or auxiliary variables used to impose the rank?
2. Dimension control. Is \\(u(k-u)\\) a valid upper bound for the dimension of every chart component under consideration?
3. Component counting. Does the Bézout estimate bound the number of irreducible components of the locally closed stratum, or only the number of isolated solutions after a generic slicing?

The third point is particularly important. A standard Bézout bound on isolated solutions does not automatically give the same bound on components of a positive-dimensional algebraic set without a suitable slicing argument and degree control.

I would not discard the stated bound, but it needs a precise algebraic-geometric justification.

### 10.3 The \\(c=3,\ k=4\\) bound

The report gives

\\[ N_3\le s+s^2+s^3+1921. \\]

This is potentially useful as a finite component bound, but it is not independently auditable from the summary alone. The report should include the exact summation over the \\((u,v)\\) strata that yields \\(1921\\), together with the treatment of overlaps and the distinction between locally closed strata and irreducible components of their union.

In particular, the components of a union of locally closed strata need not be counted simply by summing the number of components of the strata unless the stratification and closure relationships are handled correctly.

Recommendation: keep the component-bound programme, but treat the \\(1921\\) estimate as provisional until the decomposition and Bézout argument are fully written out.

## 11. Question 7: What should the project prioritize?

I recommend a combination of (i) and (iii), followed by a carefully scoped continuation of (ii).

The rigidity result changes the hardness strategy, but it does not make the existing structural results less valuable. On the contrary, the project now has a coherent set of results that can be consolidated into a strong mathematical paper, subject to verification of the component-bound and low-\\(c\\) claims.

### Recommended order

Phase 1 — Correct and consolidate the structural theorems

Immediate

- Replace the stated rigidity theorem with the corrected \\(0<\omega\<k\\) theorem.
- Add the local leakage-rigidity proposition.
- Separate the zero-compressed-rank case.
- State the two observer conventions explicitly.
- Complete the \\(c=1\\) and \\(c=2\\) certificates.

Phase 2 — Finish the algorithmic framework

Parallel

- Complete the fixed-\\(V\\) pair-lift theorem.
- State the exact scope of the simultaneous completion condition.
- Preserve the four-layer solver, but distinguish a witness, a certified infeasibility result, and “not found.”
- Finish the component-bound proof or state the current bound as conditional.

Phase 3 — Test one nonzero-leakage gadget

Research experiment

- Begin with \\(c=2\\).
- Compute the leakage map \\(J_V\\).
- Derive the exact row-pair compatibility equations.
- Check whether rank constraints yield a nontrivial polynomial relation.
- Prove pencil goodness for the entire intended family.

Phase 4 — Decide whether to pursue hardness

After Phase 3

- If a nontrivial gate survives the lift and pencil conditions, build an arithmetic-circuit reduction.
- If all such gates collapse to free lifts or rank obstructions, investigate a rigidity theorem for the leakage regime.
- Do not commit to a full ETR reduction before the one-gate test succeeds.

### Why I would not pivot entirely to fixed-\\(c\\) algorithms

The current component-bound programme is valuable, but a fixed-\\(c\\) algorithm does not settle the unbounded-\\(c\\) complexity question.

It is possible that:

- fixed \\(c\\) admits a finite algebraic stratification with a manageable component bound;
- unbounded \\(c\\) remains \\(\exists\mathbb R\\)-hard;
- or a stronger structural theorem ultimately places the whole problem in a lower complexity class.

None of these possibilities follows from the current report.

Therefore, I would not treat fixed-\\(c\\) algorithms as a substitute for hardness research. They should be developed in parallel, especially because the low-\\(c\\) classifications already contain useful exact certificates.

## 12. Suggested theorem statements for the next report

I recommend replacing the current Section II.6 with two separate propositions.

### Theorem A — Global invariant-kernel obstruction

Let

\\[ K_0=\ker[C;CA],\qquad \dim K_0=k, \\]

and let \\(H=LN\\), \\(H_A=LAN\\), with

\\[ \operatorname{rank}H=\omega,\qquad \dim\ker H=k-\omega. \\]

If

\\[ A(K_0)\subseteq K_0 \\]

and

\\[ 0<\omega\<k, \\]

then no \\(L\\) can satisfy both (5a) and (5b).

Proof: The argument in Report 64, with the explicit assumption \\(\omega>0\\).

### Theorem B — Local leakage necessity

Suppose \\(L\\) satisfies (5a) and (5b), and

\\[ \operatorname{rank}H=\omega>0. \\]

Then its kernel

\\[ V=\ker H \\]

must satisfy

\\[ \boxed{A(V)\not\subseteq K_0.} \\]

Proof: If \\(A(V)\subseteq K_0\\), condition (5a) makes every row of \\(H\\) annihilate \\(V+A(V)\\). Since \\(\operatorname{rank}H=k-\dim V\\), dimension comparison forces \\(A(V)\subseteq V\\). The invariant-annihilator eigenvector argument then contradicts (5b).

The second theorem is especially valuable because it tells us exactly what a feasible positive-rank solution must look like, independently of whether the entire \\(K_0\\) is invariant.

## 13. Final research judgement

The most important new insight in Report 64 is not merely that invariant \\(K_0\\) is an infeasible regime. It is that a feasible positive-rank observer must use leakage on its own kernel subspace.

This is a strong geometric restriction:

\\[ \boxed{ \operatorname{rank}H>0 \quad\Longrightarrow\quad A(\ker H)\not\subseteq K_0. } \\]

It rules out the previous invariant-subspace multiplication gadget at its foundation. It also identifies the only plausible place where the extra degrees of freedom of the observer problem can matter: the part of \\(A(V)\\) lying outside \\(K_0\\), together with the ambient row components needed to annihilate it.

The resulting research question is now more precise:

\boxed{\
\begin{minipage}{0.88\linewidth}\
Can the compatibility of the leakage map \\(J_V:V\to\mathbb C^n/K_0\\), the simultaneous compressed row-pair lifts, and the rank and pencil conditions encode a nontrivial arithmetic relation?\
\end{minipage}\
}

I would not yet claim that this mechanism is expressive enough for ETR-hardness. But it is the right remaining mechanism to test.

The immediate deliverables should be:

1. a corrected rigidity theorem and its local strengthening;
2. a fully explicit fixed-\\(V\\) row-pair lift theorem;
3. a complete exact certificate for the \\(c=1\\) leakage branch in the existing test instances;
4. one carefully designed \\(c=2\\) nonzero-leakage gadget experiment.

If the fourth task succeeds, the arithmetic-circuit route becomes credible. If it fails for structural reasons, that failure may point toward a stronger rigidity theorem and a useful algorithmic classification.

My overall recommendation is to consolidate the structural results while continuing one narrowly targeted hardness experiment. The project is not yet at the point where a full hardness reduction is justified, but it is also not at the point where hardness should be abandoned. The local leakage-rigidity theorem is the key result that should guide the next phase.