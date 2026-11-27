# Mathematical audit of `39_fixed_rows_and_raze(1).md`

The report makes two useful advances: it isolates the effect of the fixed rows \\(L_0\\), and it gives a clean formulation of the decision problem as a finite union of rank-stratified reduced-pencil conditions.

My conclusions are:

1. Lemma 1 is false as stated. The condition \\(K\cap AK=0\\) is not sufficient: it does not imply that \\(A|\_K\\) is injective. The correct condition for the claimed surjectivity is\
   \\[\
   \ker(A|\_K)={0}\
   \quad\text{and}\quad\
   K\cap AK={0}.\
   \\]\
   There is, however, a simple exact description of the image for arbitrary \\(A\\), by linear compatibility conditions. This answers the sampler question more generally.
2. Theorem 2 is correct, including the \\(\omega=0\\) branch, provided that condition 3 is interpreted as the maximal-minor gcd condition for the reduced \\(q\times\omega\\) pencil. Its proof can be made shorter and cleaner by using the factorisation through the selected columns.
3. The proposed complexity statements need more careful wording. The \\(\omega=0\\) target in \\((H,H_A)\\)-space is a single point, but its preimage in \\(R\\)-space need not be a single point. The \\(\omega=1\\) badness condition is indeed quadratic in the observer variables, but that alone does not establish a polynomial-time algorithm for the corresponding existential decision problem. A polynomial-time claim requires a precise input model and a precise description of what is being decided.

I recommend correcting Lemma 1 first. It is the only outright mathematical error I have identified in the main results.

# Part I. Question 1 — the fixed-row image

## 1. The precise linear map underlying the problem

Let

\\[ m=q-r, \\]

and regard \\(K\\) as an abstract \\(k\\)-dimensional vector space. Write

\\[ \iota:K\hookrightarrow\mathbb C^n \\]

for the inclusion and

\\[ A_K:K\longrightarrow\mathbb C^n,\qquad A_K(v)=Av. \\]

The free rows \\(R\in\mathbb C^{m\times n}\\) define a linear map

\\[ \Theta:\mathbb C^{m\times n} \longrightarrow \operatorname{Hom}(K,\mathbb C^m) \times\operatorname{Hom}(K,\mathbb C^m) \\]

by

\\[ \Theta(R)=(R|\_K,\ R\circ A_K). \\]

In the chosen basis \\(N_K\\), this is exactly

\\[ \Theta(R)=(RN_K,\ RAN_K). \\]

The key point is that the two restrictions are not arbitrary independent maps unless the two copies of \\(K\\), one embedded as \\(K\\) and the other embedded as \\(AK\\), have the required independence.

To understand all compatibility relations, define

\\[ T:K\oplus K\longrightarrow\mathbb C^n, \qquad T(v,w)=v+Aw. \\]

For a prescribed pair

\\[ (B_1,B_2)\in \operatorname{Hom}(K,\mathbb C^m)^2, \\]

define

\\[ B:K\oplus K\longrightarrow\mathbb C^m, \qquad B(v,w)=B_1v+B_2w. \\]

Then

\\[ RN_K=B_1,\qquad RAN_K=B_2 \\]

is equivalent to

\\[ B=R\circ T. \\]

This gives the exact general result.

## 2. Exact image theorem

Proposition. For arbitrary \\(A\\) and \\(K\\),

\\[ \boxed{ (B_1,B_2)\in\operatorname{im}\Theta \iff B_1v+B_2w=0 \quad\forall(v,w)\in\ker T. } \\]

Equivalently,

\\[ \boxed{ \operatorname{im}\Theta = \left\\{ (B_1,B_2): B_1v+B_2w=0 \text{ whenever }v+Aw=0 \right\\}. } \\]

Proof.

If \\((B_1,B_2)=\Theta(R)\\), then

\\[ B_1v+B_2w =Rv+RAw =R(v+Aw). \\]

Thus, whenever \\(v+Aw=0\\),

\\[ B_1v+B_2w=0. \\]

Conversely, suppose \\(B_1v+B_2w=0\\) whenever \\(T(v,w)=0\\). Then

\\[ \ker T\subseteq\ker B. \\]

Consequently, the rule

\\[ \widetilde R(T(v,w))=B_1v+B_2w \\]

defines a well-defined linear map

\\[ \widetilde R:\operatorname{im}T=K+AK\longrightarrow\mathbb C^m. \\]

Extend \\(\widetilde R\\) linearly to all of \\(\mathbb C^n\\). The resulting matrix \\(R\\) satisfies

\\[ R|\_K=B_1,\qquad R\circ A_K=B_2. \\]

This proves the equivalence. \\(\square\\)

This proposition is stronger than Lemma 1: it describes the image for every \\(A,K\\), not merely in the surjective case.

39_fixed_rows_and_raze(1).md

## 3. What is the kernel of \\(T\\)?

We have

\\[ \ker T = \\{(v,w)\in K\oplus K:v=-Aw\\}. \\]

For such a pair, \\(Aw\in K\cap AK\\), and conversely every \\(w\in K\\) with \\(Aw\in K\\) gives an element

\\[ (-Aw,w)\in\ker T. \\]

Therefore

\\[ \boxed{ \ker T \cong \\{w\in K:Aw\in K\\}. } \\]

In particular,

\\[ \dim\ker T = \dim\bigl(K\cap A^{-1}K\bigr), \\]

where \\(A^{-1}K\\) denotes the preimage of \\(K\\) under \\(A\\), not an inverse matrix.

This dimension is not generally equal to \\(\dim(K\cap AK)\\). The difference is precisely the possibility of nonzero vectors in \\(\ker A\cap K\\).

The rank of \\(T\\) is

\\[ \operatorname{rank}T =2k-\dim(K\cap A^{-1}K). \\]

Thus the dimension of the attainable pair space is

\\[ \boxed{ \dim\operatorname{im}\Theta = m\bigl(2k-\dim(K\cap A^{-1}K)\bigr). } \\]

Here we have used the fact that restriction of an arbitrary linear map \\(\mathbb C^n\to\mathbb C^m\\) to \\(\operatorname{im}T\\) can be prescribed arbitrarily.

This is a useful exact dimension formula for the sampling problem.

## 4. The error in the proposed sufficient condition

The report claims that

\\[ K\cap AK=\\{0\\} \\]

implies both \\(N_K\\) and \\(AN_K\\) have full column rank.

The second implication is false.

Indeed,

\\[ AN_K\text{ has full column rank} \iff \ker(A|\_K)=\\{0\\}. \\]

But

\\[ K\cap AK=\\{0\\} \\]

does not imply this.

### Counterexample

Take

\\[ A=0,\qquad K\ne\\{0\\}. \\]

Then

\\[ AK=\\{0\\}, \qquad K\cap AK=\\{0\\}, \\]

but

\\[ AN_K=0 \\]

has rank zero.

In this example,

\\[ B_2=RAN_K=0 \\]

for every \\(R\\). Hence the image cannot contain every pair \\((B_1,B_2)\\).

So the claimed equivalence in Lemma 1 fails in its stated form.

### Corrected surjectivity criterion

The map \\(T\\) is injective if and only if

\\[ T(v,w)=0 \implies v=w=0. \\]

Since \\(v=-Aw\\), this is equivalent to

\\[ Aw\in K,\quad w\in K \implies w=0. \\]

This condition can be split into two requirements:

\\[ \boxed{ \ker(A|\_K)=\\{0\\}, \qquad K\cap AK=\\{0\\}. } \\]

To see this, suppose \\(T(v,w)=0\\). Then \\(Aw=-v\in K\\). If \\(A|\_K\\) is injective and \\(K\cap AK=0\\), then \\(Aw\in K\cap AK\\) forces \\(Aw=0\\), and injectivity gives \\(w=0\\), hence \\(v=0\\).

Conversely, if \\(T\\) is injective, then \\(Aw=0\\) for \\(w\in K\\) implies \\(T(0,w)=0\\), so \\(w=0\\). Thus \\(A|\_K\\) is injective. Also, if \\(v\in K\cap AK\\), write \\(v=Aw\\) for \\(w\in K\\); then \\(T(-v,w)=0\\), so \\(v=w=0\\).

Therefore the corrected lemma is:

\\[ \boxed{ \operatorname{im}\Theta = \operatorname{Hom}(K,\mathbb C^m)^2 \iff \ker(A|\_K)=0\text{ and }K\cap AK=0. } \\]

This is the exact necessary and sufficient condition.

A useful dimension consequence is

\\[ 2k\le n \\]

whenever \\(\Theta\\) is surjective, because injectivity of \\(T:K\oplus K\to\mathbb C^n\\) requires \\(2k\le n\\). The dimension count in the report is therefore consistent with the corrected criterion, but it is not a substitute for checking injectivity.

## 5. Are there exactly as many independent relations as \\(\dim(K\cap AK)\\)?

Not in general.

The number of independent compatibility conditions is

\\[ m\dim\ker T = m\dim(K\cap A^{-1}K). \\]

It is therefore governed by

\\[ \dim(K\cap A^{-1}K), \\]

not simply by \\(\dim(K\cap AK)\\).

If \\(A|\_K\\) is injective, then the restriction

\\[ A|\_{A^{-1}K\cap K}:A^{-1}K\cap K \longrightarrow K\cap AK \\]

is an isomorphism. In that special case,

\\[ \dim(K\cap A^{-1}K)=\dim(K\cap AK). \\]

So the report's intuition of one relation per independent overlap direction is correct provided \\(A|\_K\\) is injective.

Without that hypothesis, there can be additional relations arising from \\(\ker A\cap K\\).

### Explicit form of the relations when \\(A|\_K\\) is injective

Let

\\[ J=K\cap AK. \\]

For every \\(v\in J\\), there is a unique \\(w\in K\\) with

\\[ Aw=v. \\]

The compatibility relation is

\\[ \boxed{B_1v=B_2w.} \\]

A basis of \\(J\\) gives \\(\dim J\\) independent vector relations, each with \\(m\\) scalar coordinate equations. These relations completely describe the image.

Without injectivity, a vector \\(v\in J\\) may have multiple preimages \\(w\in K\\), and the correct statement is that \\(B_2\\) must take the same value on all such preimages, while vanishing on \\(\ker(A|\_K)\\). The kernel-of-\\(T\\) formulation handles all of these simultaneously.

## 6. Consequences for the sampler

The sampler proposed in the report is valid in the corrected surjective case, but the word “uniformly” needs qualification.

Over \\(\mathbb C\\), there is no translation-invariant probability distribution that is uniform over the whole vector space. What one can say is:

- If \\(\Theta\\) is surjective, every target pair \\((B_1,B_2)\\) is attainable.
- Given a target pair, one can construct a solution \\(R\\) by extending a linear map from \\(K+AK\\) to \\(\mathbb C^n\\).
- If a probability distribution on the target space is specified, it can be sampled first and then lifted to an \\(R\\).
- If the target distribution is Gaussian, a suitable linear right inverse can be used to produce a Gaussian or otherwise controlled distribution on the solution space, but the resulting distribution on \\(R\\) depends on the chosen right inverse and any additional randomness in the kernel of \\(\Theta\\).

When \\(\Theta\\) is not surjective, the exact compatibility conditions above should be imposed before sampling.

Recommendation: replace the original Lemma 1 by the exact image proposition, and state the corrected surjectivity criterion as a corollary. This gives you a general sampler framework rather than a special-case result.

# Part II. Question 2 — equivalence of DEC(q) and RAZE

## 7. The selected-column reduction

Theorem 2 is correct. The key point is that the selected columns of \\(H\\) form a basis of its column space.

Suppose

\\[ \operatorname{rank}H=\omega>0 \\]

and select \\(S\subseteq\\{1,\ldots,k\\}\\), \\(|S|=\omega\\), such that

\\[ U=H\_{[:,S]} \\]

has full column rank.

There is a unique matrix

\\[ V\in\mathbb C^{\omega\times k} \\]

such that

\\[ H=UV. \\]

The selected columns of \\(V\\) form the identity matrix:

\\[ V\_{[:,S]}=I\_\omega. \\]

In particular, \\(V\\) has full row rank.

Now suppose

\\[ \ker H\subseteq\ker H_A. \\]

Since \\(U\\) is injective,

\\[ \ker H=\ker V. \\]

Thus

\\[ \ker V\subseteq\ker H_A. \\]

Consequently \\(H_A\\) factors through \\(V\\): there is a matrix

\\[ G\in\mathbb C^{q\times\omega} \\]

such that

\\[ H_A=GV. \\]

Restricting to the selected columns gives

\\[ G=H\_{A,[:,S]}. \\]

Therefore

\\[ \boxed{ \lambda H-H_A=(\lambda U-G)V. } \\]

Since \\(V:\mathbb C^k\to\mathbb C^\omega\\) is surjective,

\\[ \operatorname{im}\bigl((\lambda U-G)V\bigr) =\operatorname{im}(\lambda U-G). \\]

Hence

\\[ \boxed{ \operatorname{rank}(\lambda H-H_A) = \operatorname{rank}(\lambda U-G) \quad\forall\lambda\in\mathbb C. } \\]

This establishes exactly the rank equality used in the report.

## 8. The reduced gcd criterion

The leading coefficient \\(U\\) has full column rank \\(\omega\\). Therefore the \\(q\times\omega\\) pencil

\\[ P_S(\lambda)=\lambda U-G \\]

has normal rank \\(\omega\\).

Its rank is \\(\omega\\) for every finite \\(\lambda\\) if and only if its \\(\omega\times\omega\\) minors have no common finite root. Over \\(\mathbb C\\), this is equivalent to

\\[ \boxed{ \gcd\\{\text{all }\omega\times\omega\text{ minors of }\lambda U-G\\} \in\mathbb C^\times. } \\]

Thus condition 3 is precisely the reduced-pencil spectral condition.

One minor terminology correction: these are the maximal minors of the \\(q\times\omega\\) pencil. There are

\\[ \binom q\omega \\]

of them, one for each choice of \\(\omega\\) rows.

## 9. The kernel identity and the \\(\omega=0\\) case

The report uses

\\[ \dim\ker Q\_{\mathcal L}(\lambda) = \dim D+\dim\ker P_K(\lambda). \\]

This is legitimate for every \\(\omega\\), including zero, provided \\(P_K\\) is interpreted as the induced pencil

\\[ P_K(\lambda)=\lambda\iota_K-\Phi_K: W_K\longrightarrow\mathbb C^q. \\]

Here

\\[ W_K=\mathcal LK,\qquad D=K\cap\ker\mathcal L. \\]

The identity comes from the linear map

\\[ \ker Q\_{\mathcal L}(\lambda)\longrightarrow\ker P_K(\lambda), \qquad v\longmapsto\mathcal Lv, \\]

which is surjective and has kernel \\(D\\). Rank–nullity gives the identity.

When \\(\omega=0\\),

\\[ W_K=\\{0\\},\qquad D=K. \\]

The induced pencil has domain the zero vector space, so

\\[ \dim\ker P_K(\lambda)=0. \\]

The identity becomes

\\[ \dim\ker Q\_{\mathcal L}(\lambda)=\dim K=k. \\]

Thus the kernel dimension of \\(Q\_{\mathcal L}(\lambda)\\) is constant. Consequently its rank is constant, and (5b) holds.

This agrees with the direct argument: \\(H=0\\) means

\\[ \mathcal L|\_K=0. \\]

Under (5a), the compatibility condition gives

\\[ \mathcal LA|\_K=0. \\]

Thus, for \\(v\in K\\),

\\[ (\lambda\mathcal L-\mathcal LA)v=0, \\]

and the kernel of \\(Q\_{\mathcal L}(\lambda)\\) is exactly \\(K\\), independent of \\(\lambda\\).

So the \\(\omega=0\\) branch is not a problematic vacuous use of a gcd. It is a genuine, separately verified branch of the reduced criterion.

## 10. A cleaner proof of Theorem 2

I would shorten the proof by structuring it as follows.

Theorem. The DEC\\((q)\\) instance is YES if and only if RAZE is YES.

Proof.

Suppose first that \\(R\\) satisfies (5a) and (5b). Set

\\[ H=\mathcal L N_K,\qquad H_A=\mathcal LA N_K,\qquad \omega=\operatorname{rank}H. \\]

By the established equivalence,

\\[ (5a)\iff\ker H\subseteq\ker H_A. \\]

If \\(\omega=0\\), condition 3 is vacuous. Otherwise choose \\(\omega\\) independent columns of \\(H\\), indexed by \\(S\\). The selected-column factorisation

\\[ H=UV,\qquad H_A=GV \\]

gives

\\[ \lambda H-H_A=(\lambda U-G)V, \\]

with \\(V\\) full row rank. Thus the full pencil and reduced pencil have equal rank for every \\(\lambda\\). Condition (5b) implies that the reduced pencil has full column rank for every finite \\(\lambda\\), and hence its maximal minors have gcd a nonzero constant. This gives RAZE.

Conversely, suppose RAZE holds. Condition 2 gives (5a). If \\(\omega>0\\), condition 3 gives

\\[ \operatorname{rank}(\lambda U-G)=\omega \quad\forall\lambda\in\mathbb C. \\]

The selected-column factorisation shows

\\[ \operatorname{rank}(\lambda H-H_A)=\omega \quad\forall\lambda. \\]

By the kernel identity, this is equivalent to constant rank of \\(Q\_{\mathcal L}(\lambda)\\), giving (5b). If \\(\omega=0\\), condition 2 implies \\(H_A=0\\), and the zero-rank branch gives (5b) automatically. \\(\square\\)

This version makes the proof's dependencies transparent and avoids an unnecessary detour through the invariant-line language.

Theorem 2: correct

39_fixed_rows_and_raze(1).md

# Part III. Question 3 — per-layer complexity

This part needs the most caution. The report's proposed restraint about \\(\omega\ge2\\) is sensible, but I would also revise the wording of the \\(\omega=0\\) and \\(\omega=1\\) statements.

## 11. The \\(\omega=0\\) stratum: a point in image space, not generally in \\(R\\)-space

If

\\[ \operatorname{rank}H(R)=0, \\]

then

\\[ H(R)=0. \\]

If the compatibility condition holds, then

\\[ H_A(R)=0. \\]

Thus, in the pair space

\\[ (H,H_A)\in (\mathbb C^{q\times k})^2, \\]

the rank-zero compatible target is indeed the single point

\\[ \boxed{(H,H_A)=(0,0).} \\]

But the set of \\(R\\) mapping to this pair is

\\[ \left\\{ R: RN_K=-(L_0N_K)\_{\text{lower-block convention}}, \quad RAN_K=-(L_0AN_K)\_{\text{lower-block convention}} \right\\}, \\]

with the exact right-hand sides determined by the fixed top blocks.

More simply, the full conditions are

\\[ L_0N_K=0,\quad RN_K=0, \\]

and

\\[ L_0AN_K=0,\quad RAN_K=0. \\]

The set of free matrices \\(R\\) satisfying these equations is generally an affine linear space, not a single point.

For example, if \\(K=\\{0\\}\\), then \\(N_K\\) has zero columns and both equations are vacuous. Every \\(R\\) gives \\(\omega=0\\). The feasible \\(R\\)-set is the entire parameter space, not a single point.

Therefore the defensible statement is:

> On the \\(\omega=0\\) stratum, the compatible image pair is uniquely determined as \\((H,H_A)=(0,0)\\). Whether this stratum is nonempty is determined by the fixed top-block conditions and the solvability of a system of linear equations in \\(R\\). Once it is nonempty, spectral feasibility is automatic.

This is stronger and more precise than saying the feasible set is a single point.

### Complexity consequence

For rational or algebraic input data, membership of a specified \\(R\\) in the rank-zero compatible stratum is decidable by exact matrix arithmetic. Existence of some \\(R\\) is also decidable by linear-system consistency.

For rational input, Gaussian elimination is polynomial-time in the standard bit model, subject to the usual coefficient-growth and bit-complexity accounting. This is a legitimate polynomial-time claim.

## 12. The \\(\omega=1\\) stratum: the exact quadratic criterion

Let

\\[ H\in\mathbb C^{q\times k},\qquad H_A\in\mathbb C^{q\times k} \\]

satisfy

\\[ \operatorname{rank}H=1,\qquad \ker H\subseteq\ker H_A. \\]

Choose a nonzero column \\(u\\) of \\(H\\), and write

\\[ H=u v^{\mathsf T} \\]

for some nonzero \\(v\in\mathbb C^k\\). Compatibility implies

\\[ H_A=g v^{\mathsf T} \\]

for some \\(g\in\mathbb C^q\\).

The reduced pencil is simply

\\[ P\_{\mathrm{red}}(\lambda)=\lambda u-g, \\]

a \\(q\times1\\) pencil.

It has rank zero at a finite \\(\lambda\\) precisely when

\\[ g=\lambda u. \\]

Equivalently, \\(u\\) and \\(g\\) are linearly dependent.

This is equivalent to the vanishing of all \\(2\times2\\) minors of

\\[ [u\ \ g]. \\]

Thus

\\[ \boxed{ \text{spectral badness} \iff u_i g_j-u_j g_i=0 \quad\forall\\,1\le i\<j\le q. } \\]

These are quadratic equations in the entries of \\(u,g\\).

For \\(q=1\\), there are no such minors, and every \\(g\\) is a scalar multiple of every nonzero \\(u\\). Thus the \\(\omega=1\\) stratum is always spectrally bad when \\(q=1\\). This is an important edge case to state explicitly.

For \\(q\ge2\\), the spectral feasible locus is the complement of the common zero set of those quadratic polynomials, relative to the rank-one compatible stratum.

## 13. What does “tested by linear algebra” mean here?

There are several different computational tasks, and they should not be conflated.

### Task A: test a given candidate \\(R\\)

Given \\(R\\), calculate \\(H,H_A\\), verify rank one and compatibility, and evaluate the \\(2\times2\\) minors of \\([u\ g]\\).

This is ordinary exact linear algebra and polynomial evaluation. For rational input, it is polynomial-time in the bit model.

### Task B: determine whether every point in a specified affine family is bad

Suppose the relevant candidate family is parameterised by free coordinates \\(x\\), and the entries of \\(u,g\\) are affine-linear in \\(x\\). Then the badness equations are quadratic polynomials

\\[ f\_{ij}(x)=u_i(x)g_j(x)-u_j(x)g_i(x). \\]

To decide whether every point of the family is bad, one must decide whether every \\(f\_{ij}\\) vanishes identically on that family.

If the family is an affine space with explicit coordinates, this can be done by expanding each polynomial and checking whether all coefficients vanish. That is a linear-algebraic coefficient test once the monomial basis is fixed.

But if the family is a rank stratum defined by additional equations, the correct question is whether the polynomials vanish identically on that stratum. This may require computing its vanishing ideal or working in its coordinate ring. It is not automatically the same as checking coefficients in the ambient \\(R\\)-coordinates.

### Task C: decide whether there exists a spectrally feasible \\(R\\) on the stratum

This asks whether

\\[ \exists R: \quad \operatorname{rank}H(R)=1,\quad \ker H(R)\subseteq\ker H_A(R), \quad \bigvee\_{i\<j} f\_{ij}(R)\ne0. \\]

The last condition is a disjunction of polynomial inequations, and the rank-one and compatibility conditions must also be imposed.

A quadratic description does not, by itself, imply a polynomial-time algorithm for this existential problem. One needs to exploit additional structure of the observer-induced parameterisation.

This is the critical distinction in the report's Question 3.

## 14. The input-encoding qualification

A complexity statement must specify at least:

1. Are \\(A,C,L_0\\) rational, algebraic, or arbitrary complex numbers?
2. If algebraic, how are algebraic numbers represented?
3. Is \\(q\\) part of the input or fixed?
4. Is the question candidate membership, nonemptiness of a stratum, or nonemptiness of the spectral feasible subset?
5. Is the algorithm expected to output a witness \\(R\\), or only answer YES/NO?

For a conventional bit-complexity statement, I recommend assuming

\\[ A,C,L_0\in\mathbb Q^{\text{appropriate dimensions}}, \\]

with rational entries encoded in binary.

Under this model:

- candidate verification on the \\(\omega=0\\) and \\(\omega=1\\) strata is polynomial-time;
- linear-system feasibility for the rank-zero stratum is polynomial-time;
- polynomial identity testing by explicit coefficient expansion is polynomial-time when the relevant affine parameterisation has polynomial-size dimension and the expanded polynomial representation remains polynomial in the input size;
- existential feasibility of a system of quadratic equations or inequations is not automatically polynomial-time.

One should not claim that the whole \\(\omega=1\\) existential decision problem is polynomial-time solely because the badness equations have degree two.

## 15. A useful refinement: \\(\omega=1\\) has a particularly simple geometric interpretation

The reduced pencil is

\\[ \lambda u-g. \\]

The bad locus is the condition

\\[ g\in\mathbb Cu. \\]

In projective terms, it is the incidence condition that the two vectors \\(u,g\\) span a subspace of dimension at most one:

\\[ \operatorname{rank}[u\ \ g]\le1. \\]

This is a determinantal variety, defined by quadratic equations. The spectral feasible set is its complement.

Therefore, on a fixed irreducible parameter component, the same open-or-empty principle from the previous report applies:

- If the bad determinantal condition holds identically on the component, no point of that component is spectrally feasible.
- If it does not hold identically, its complement is a nonempty Zariski-open dense subset of that component.

This is a useful structural theorem, but it still does not settle real feasibility or polynomial-time complexity.

For real observer variables, a nonempty complex Zariski-open subset need not contain a real point unless the real points of the relevant component are sufficiently rich—for example, Zariski dense in that component. That qualification should be retained from the earlier geometric analysis.

# Part IV. Recommended replacement statements

I would revise the report as follows.

## 16. Replacement for Lemma 1

Lemma 1 (exact fixed-row image). Let

\\[ \Psi\_{L_0}(R)=(RN_K,RAN_K), \\]

where \\(R\in\mathbb C^{(q-r)\times n}\\). Define

\\[ T:K\oplus K\to\mathbb C^n,\qquad T(v,w)=v+Aw. \\]

Then

\\[ \operatorname{im}\Psi\_{L_0} = \left\\{ (B_1,B_2): B_1v+B_2w=0 \quad\forall(v,w)\in\ker T \right\\}. \\]

In particular, \\(\Psi\_{L_0}\\) is surjective if and only if

\\[ \ker(A|\_K)=0,\qquad K\cap AK=0. \\]

The fixed top blocks impose the additional requirements

\\[ H\_{1:r,:}=L_0N_K,\qquad (H_A)\_{1:r,:}=L_0AN_K. \\]

This formulation is exact and includes the degenerate cases.

## 17. Replacement for the sampling consequence

> When \\(A|\_K\\) is injective and \\(K\cap AK=0\\), the map \\(R\mapsto(RN_K,RAN_K)\\) is surjective. Thus arbitrary lower-block target pairs can be realised, and a linear right inverse gives an explicit construction of \\(R\\). In the general case, the attainable pairs are precisely those satisfying the linear compatibility conditions determined by \\(\ker T\\). These conditions provide the correct target space for sampling.

This avoids the misleading claim of a uniform distribution on a complex vector space.

## 18. Replacement for the complexity paragraph

I would state only the following three claims at present.

Claim A — \\(\omega=0\\). The compatible image pair is necessarily \\((0,0)\\), and spectral feasibility is automatic. Nonemptiness of the corresponding \\(R\\)-fibre reduces to a linear-system consistency problem.

Claim B — \\(\omega=1\\). On a rank-one compatible candidate, spectral badness is equivalent to

\\[ \operatorname{rank}[u\ \ g]\le1, \\]

or, equivalently, the vanishing of all \\(2\times2\\) minors. These are quadratic equations in the candidate parameters. Candidate verification is polynomial-time over rational input.

Claim C — \\(\omega\ge2\\). The reduced-pencil Bézout construction gives a finite determinantal description of the bad locus, but no polynomial-time bound for the corresponding existential decision problem is asserted.

These are defensible and do not overstate what has been proved.

# Part V. Final verdict and priorities

| Item                                             | Verdict             | Action                                                                               |
| ------------------------------------------------ | ------------------- | ------------------------------------------------------------------------------------ |
| Fixed-row image formula in Lemma 1               | Incorrect as stated | Replace by kernel-of-\\(T\\) compatibility proposition                               |
| Sufficiency of \\(K\cap AK=0\\)                  | False               | Add injectivity of \\(A\|\_K\\)                                                      |
| Necessity of \\(K\cap AK=0\\) for surjectivity   | Correct             | Retain                                                                               |
| Number of independent compatibility relations    | Needs correction    | Use \\(\dim(K\cap A^{-1}K)\\); reduce to overlap dimension if \\(A\|\_K\\) injective |
| General image description                        | Available           | Use the exact linear compatibility conditions                                        |
| Sampling consequence                             | Needs qualification | Replace “uniformly” by surjective parametrisation/right-inverse language             |
| DEC\\((q)\\)\\(\iff\\) RAZE                      | Correct             | Retain                                                                               |
| Selected-column factorisation                    | Correct             | Make it the central proof device                                                     |
| \\(\omega=0\\) branch                            | Correct             | Emphasise that the image pair is one point, not necessarily its \\(R\\)-preimage     |
| \\(\omega=1\\) quadratic badness criterion       | Correct             | State explicitly using \\([u\ g]\\)                                                  |
| \\(\omega=1\\) polynomial-time existential claim | Not established     | Restrict the claim to candidate verification or a specified identity test            |
| \\(\omega\ge2\\) complexity                      | Open                | Do not claim polynomial-time without a new argument                                  |

## My recommendation

The next round should focus on two tasks.

First, repair the fixed-row lemma and build the general sampler from its exact image description. This is mathematically straightforward and gives a useful result even when \\(K\cap AK\ne0\\). In particular, the correct compatibility space is controlled by

\\[ \ker\bigl[(v,w)\mapsto v+Aw\bigr], \\]

which is the natural object to use in the sampler.

Second, separate the three levels of complexity claims: candidate verification, polynomial identity testing, and existential feasibility. The \\(\omega=0\\) and \\(\omega=1\\) algebraic descriptions are valid, but only the first two computational tasks have immediate elementary polynomial-time implementations under a rational bit model. The existential \\(\omega=1\\) problem needs a separate proof.

The main positive conclusion is that Theorem 2 survives the audit unchanged. The DEC–RAZE equivalence is sound, and the zero-rank branch is handled correctly. The fixed-row issue is independent of that equivalence: it affects how one parameterises or samples the attainable \\((H,H_A)\\)-pairs, not the correctness of the reduced-pencil characterisation itself.