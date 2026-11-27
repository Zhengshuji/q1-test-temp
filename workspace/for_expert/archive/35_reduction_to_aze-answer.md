Review of 35_reduction_to_aze.md
The report contains a worthwhile structural idea: under \(K\cap AK=\{0\}\), the two restrictions \(M|_K\) and \(M|_{AK}\) can be prescribed independently. This does give a precise surjectivity result for the map
\[
M\longmapsto (MN_K,\;MAN_K).
\]

However, the proposed implication from AZE hardness to hardness of the original \(\mathrm{DEC}(q)\) is not established as written. There are two distinct issues:
1. the fixed first \(r\) rows restrict the AZE instances that can be represented; and
2. more importantly, the AZE formulation appears to focus on full-column-rank \(H\), whereas the observer decision problem can admit feasible candidates with \(\operatorname{rank}H<k\).
The second issue is a genuine gap in a many-one hardness reduction: a rank-deficient observer candidate could make \(\mathrm{DEC}(q)\) a yes-instance even when the corresponding full-column-rank AZE instance is a no-instance. I will make the distinction precise below, then discuss the complexity of AZE and what can safely be concluded from the current reduction. 
35_reduction_to_aze(1).md

1. The realizability lemma: correct, with a precise formulation
Let \(K\) have dimension \(k\), let \(N_K\in\mathbb C^{n\times k}\) have columns forming a basis of \(K\), and suppose
\[
K\cap AK=\{0\}.
\]

Then \(AN_K\) also has full column rank: if \(AN_Kx=0\), then \(N_Kx\in K\cap\ker A\subseteq K\cap AK\), so \(N_Kx=0\), and hence \(x=0\).

Now take arbitrary matrices
\[
H,H_A\in\mathbb C^{q\times k}.
\]

The prescriptions
\[
M N_K=H,\qquad M A N_K=H_A
\]

define a linear map on \(K\oplus AK\): for \(v=N_Kx\in K\) and \(w=AN_Ky\in AK\), set
\[
M(v+w)=Hx+H_Ay.
\]

This is well-defined because the decomposition \(v+w\) is unique when \(K\cap AK=0\). Extend this map linearly to a complement of \(K\oplus AK\) in \(\mathbb C^n\). Thus the lemma is correct.

There is also a useful converse description: the linear map
\[
\Psi:\operatorname{Hom}(\mathbb C^n,\mathbb C^q)
\longrightarrow
\mathbb C^{q\times k}\times\mathbb C^{q\times k},
\qquad
M\longmapsto(MN_K,MAN_K)
\]

is surjective precisely when the map
\[
K\oplus K\longrightarrow\mathbb C^n,\qquad (v,w)\longmapsto v+Aw
\]

is injective, which is equivalent to \(K\cap AK=0\).

The dimension condition in the report is also correct:
\[
K,AK\subseteq\ker C,\quad K\cap AK=0
\quad\Longrightarrow\quad
2k\leq\dim\ker C.
\]

Since \(\dim\ker C\geq n-\operatorname{rank}C\geq n-p\), this gives
\[
n-p\geq 2k.
\]

The displayed construction at equality is consistent with the stated action of \(A\): \(CAe_1=CAe_2=0\), while \(CAe_5=e_3\) and \(CAe_6=e_4\) in the indicated coordinate convention, so \(\operatorname{rank}[C;CA]=4\) and \(K=\operatorname{span}\{e_1,e_2\}\). 
35_reduction_to_aze(1).md

2. What the fixed first \(r\) rows actually mean
The phrase “all pencil pairs with the first \(r\) rows fixed” needs a more exact statement.

Write
\[
M=\begin{bmatrix}L_0\\R\end{bmatrix},\qquad
H=MN_K,\qquad H_A=MAN_K.
\]

Then necessarily
\[
H=
\begin{bmatrix}
L_0N_K\\
RN_K
\end{bmatrix},
\qquad
H_A=
\begin{bmatrix}
L_0AN_K\\
RAN_K
\end{bmatrix}.
\]

Consequently, the realizable pairs are exactly
\[
\boxed{
H_{1:r,:}=L_0N_K,\qquad
(H_A)_{1:r,:}=L_0AN_K,
}
\]

with the remaining \(q-r\) rows of both matrices independently arbitrary, provided \(K\cap AK=0\).

The important point is that there are two prescribed blocks, not just the first \(r\) rows of \(H\). The first \(r\) rows of \(H_A\) are prescribed as well, and are linked to the same \(L_0\) and \(A\).

Thus the lemma proves surjectivity onto this restricted affine subspace of pencil pairs. It does not prove that every arbitrary affine AZE family can be represented with a prescribed \(L_0\).

This does not automatically invalidate a hardness strategy. In a reduction, one is allowed to construct \(L_0\) and the other observer data as part of the output instance. But one must actually give a polynomial-time construction mapping an arbitrary AZE input to observer data such that:
- the two fixed blocks have the required values;
- the variable rows reproduce the AZE parameters;
- the observer dimensions and the \(K,AK\) construction are valid; and
- the equivalence of yes- and no-instances is preserved.
It is not enough to say that the fixed block “can be absorbed” into AZE. That would require proving hardness for the AZE subclass with those prescribed blocks, or giving an explicit transformation from unrestricted AZE to that subclass.

There is a further modelling point: the report allows \(A,C,L_0\) to be part of the input, but if the intended \(q_{\min}\) problem fixes some of them in advance, a reduction that chooses them freely proves hardness only for the corresponding variable-data version. The precise input model must be stated before a hardness conclusion is drawn.
3. The key compatibility identity: condition (5a) is a rank-stratum condition on \(H,H_A\)
This is the most important missing bridge in the reduction. It can be stated exactly using the notation of the report.

Recall
\[
K=\ker\begin{bmatrix}C\\CA\end{bmatrix},
\qquad H=MN_K,\qquad H_A=MAN_K.
\]

Then
\[
\boxed{\quad (5a)\iff \ker H\subseteq\ker H_A.\quad}
\]

Proof. Condition (5a) is equivalent to the row-space inclusion
\[
\operatorname{row}(MA)
\subseteq
\operatorname{row}\begin{bmatrix}M\\CA\\C\end{bmatrix}.
\]

By taking annihilators, this is equivalent to
\[
\ker\begin{bmatrix}M\\CA\\C\end{bmatrix}
\subseteq\ker(MA).
\]

The kernel on the left is \(K\cap\ker M\). Every vector in it has the form \(N_Kx\) with \(Hx=0\), and
\[
MAN_Kx=H_Ax.
\]

Thus the inclusion is exactly \(\ker H\subseteq\ker H_A\). \(\square\)

This identity has two consequences.
1. If \(H\) has full column rank \(k\), then (5a) holds automatically.
2. If \(H\) is rank-deficient, (5a) is not automatic: it imposes the additional compatibility condition \(\ker H\subseteq\ker H_A\).
The report's AZE problem is formulated using \(H\) of full column rank. If that means every candidate under consideration has \(\operatorname{rank}H=k\), then the AZE candidates automatically satisfy (5a). That is useful. But it does not show that all candidates relevant to \(\mathrm{DEC}(q)\) have full column rank.

Indeed, the observer problem allows
\[
\omega=\operatorname{rank}H<k.
\]

On such a stratum, (5a) merely says that \(H_A\) factors through \(H\). The resulting reduced pencil has \(\omega\) columns, not \(k\). Its spectral feasibility is governed by the \(\omega\times\omega\) minors of a \(q\times\omega\) reduced pencil, as in the earlier criterion.

There are even degenerate examples: if \(H=0\) and \(H_A=0\), then \(\ker H\subseteq\ker H_A\), and the induced map on \(W_K=\operatorname{im}H=\{0\}\) has no nonzero eigenvector. Thus the spectral condition is automatic. This illustrates why one cannot simply discard lower-rank candidates from the observer problem.
Consequence for Question 2
Yes: as currently formulated, the reduction must control all rank strata that can contain feasible observer candidates. The issue is not that a single observer instance needs to be decomposed into charts before it can be a reduction. The issue is that the target decision problem itself existentially quantifies over all \(R\), and those \(R\)'s can have different values of \(\operatorname{rank}H(R)\).

Suppose the AZE instance is a no-instance in the full-column-rank sense:
\[
\text{there is no parameter value with }\operatorname{rank}H=k
\text{ and no finite rank drop.}
\]

This does not rule out an observer candidate with
\[
\operatorname{rank}H=\omega<k,\qquad
\ker H\subseteq\ker H_A,
\]

whose \(\omega\)-column reduced pencil has no finite rank drop. Such a candidate would make \(\mathrm{DEC}(q)\) a yes-instance.

That is a false-positive route for the proposed reduction. It must be closed before a hardness implication can be claimed.

The minimal ways to repair this are:
- Force full column rank: prove that every observer candidate satisfying (5a) has \(\operatorname{rank}H=k\). A sufficient condition is
  \[
  \operatorname{rank}(L_0N_K)=k,
  \]
  because the first \(r\) rows of \(H\) are fixed as \(L_0N_K\). This requires \(r\ge k\). It is a strong condition and changes the AZE subclass to one with a prescribed full-rank block.
- Use a rank-stratified AZE target: include all possible values \(\omega=0,\ldots,k\), with the compatibility condition \(\ker H\subseteq\ker H_A\) on each stratum, and use the corresponding reduced pencil. Then the observer problem and the target problem quantify over the same candidate types.
- Build a rank-exclusion gadget: construct additional observer data that make every rank-deficient \(H\) candidate infeasible. This could preserve a more general source AZE problem, but the report does not currently provide such a gadget.
The first is the cleanest immediate repair if it can be made compatible with the desired hardness source. The second is the most faithful mathematical reformulation of \(\mathrm{DEC}(q)\). The third is potentially the most useful for a reduction from a general AZE problem, but would require a new construction.
35_reduction_to_aze(1).md
4. Question 1 revisited: what exactly is the reduction proving?
The lemma plus \(K\cap AK=0\) proves that the observer map can realize every pair in the affine subspace
\[
\mathscr A_{L_0,A,K}
=
\left\{(H,H_A):
\begin{array}{l}
H_{1:r,:}=L_0N_K,\\
(H_A)_{1:r,:}=L_0AN_K
\end{array}
\right\}.
\]

This is a genuine and useful result. It also shows that the remaining rows of \(H\) and \(H_A\) can be varied independently.

But the statement
\[
\text{“AZE is hard”}\Longrightarrow\text{“DEC}(q)\text{ is hard”}
\]

needs a reduction between decision problems, not just a surjectivity lemma. There are three separate requirements:
1. Source-family requirement. The AZE hardness result must hold for affine families with the two prescribed blocks above, or the reduction must transform arbitrary AZE instances into such families.
2. Observer admissibility requirement. The map from source parameters to \(R\) must give the intended \((H,H_A)\), with all dimensions and data encoded with polynomial overhead.
3. No-extra-solutions requirement. Every observer candidate \(R\) that could make \(\mathrm{DEC}(q)\) true must correspond to a source AZE solution. This is where the lower-rank strata currently cause a gap.
The third requirement is logically independent of the first two. Even if the fixed-block AZE subclass is hard and the realizability lemma is perfectly implemented, lower-rank observer candidates can still destroy the no-instance direction.
A useful distinction about the fixed block
If \(L_0\) is part of the input to the observer problem, there is no objection in principle to choosing it during the reduction. One may choose \(L_0\) to produce whatever fixed blocks the construction requires, provided those choices are explicit and polynomially computable.

If \(L_0\) is fixed in advance as part of the problem definition, the reduction must respect that fixed \(L_0\); it cannot choose the block to suit the source instance.

In either model, it is not enough to say that the fixed rows can be “absorbed.” The reduction must demonstrate the absorption and preserve yes/no equivalence.

My assessment: the realizability lemma is correct; the fixed-row issue is a restriction on the hardness source and may be repairable; the rank-stratum issue is the more serious obstruction to the stated implication.
5. Question 3: what is AZE mathematically?
Let the affine family be parameterised by \(t=(t_1,\ldots,t_s)\in\mathbb C^s\):
\[
H(t)=H_0+\sum_{\ell=1}^s t_\ell H_\ell,\qquad
G(t)=G_0+\sum_{\ell=1}^s t_\ell G_\ell,
\]

and consider
\[
P(t,\lambda)=\lambda H(t)-G(t),
\qquad P(t,\lambda)\in\mathbb C^{q\times k}[\lambda].
\]

Here I use \(G\) for the report's \(H_A\), just to make the two coefficient matrices visually distinct.

The natural AZE decision question is:
Does there exist \(t\in\mathbb C^s\) such that \(H(t)\) has full column rank \(k\) and \(P(t,\lambda)\) has full column rank \(k\) for every finite \(\lambda\in\mathbb C\)?

Assume \(q\ge k\), and assume there is at least one \(t\) for which \(H(t)\) has full column rank. Let
\[
U=\{t\in\mathbb C^s:\operatorname{rank}H(t)=k\}.
\]

This is a nonempty Zariski-open subset of affine space, hence irreducible.

For \(t\in U\), the pencil has full column normal rank because its leading coefficient \(H(t)\) has full column rank. Its finite rank-drop condition is equivalent to
\[
\gcd\{\text{all }k\times k\text{ minors of }P(t,\lambda)\}
\ne 1.
\]

Thus AZE asks whether the gcd can be a unit for at least one \(t\in U\).
5.1 A significant genericity consequence
The earlier projective-incidence argument gives a useful fact here. The bad set
\[
B=\{t\in U:\exists\lambda\in\mathbb C,\ 
\operatorname{rank}P(t,\lambda)<k\}
\]

is Zariski closed relative to \(U\).

One way to see the closedness is to homogenise the spectral parameter:
\[
P^h(t;\alpha,\beta)=\alpha H(t)-\beta G(t),
\qquad [\alpha:\beta]\in\mathbb P^1.
\]

The simultaneous vanishing of all \(k\times k\) minors defines a closed incidence set in \(U\times\mathbb P^1\). At the point at infinity \([1:0]\), the matrix is \(H(t)\), which has full column rank for every \(t\in U\). Therefore the incidence set has no point over infinity. Its projection to \(U\) is closed because \(\mathbb P^1\) is projective, and that projection is exactly \(B\).

Now use irreducibility of \(U\). There are only two possibilities:
- \(B=U\): every full-column-rank member has a finite rank drop;
- \(B\subsetneq U\): the complement \(U\setminus B\) is nonempty Zariski open and dense.
In particular,
\[
\boxed{
\text{AZE has a yes-answer}
\iff
\text{a generic member of the affine family has no finite rank drop}.
}
\]

This is an important simplification. For an unrestricted complex affine parameter space, AZE is not a typical existential search problem in which one must find an exceptional parameter value. If a good member exists, then a Zariski-open dense set of parameters is good.
5.2 The function-field gcd criterion
Let
\[
F=\mathbb C(t_1,\ldots,t_s)
\]

be the rational function field of the parameter space, and regard
\[
P(t,\lambda)=\lambda H(t)-G(t)
\]

as a polynomial matrix over \(F[\lambda]\).

The genericity statement gives the following exact criterion:
\[
\boxed{
\mathrm{AZE}=\mathrm{YES}
\iff
\gcd_{F[\lambda]}
\{\text{all }k\times k\text{ minors of }P(t,\lambda)\}=1.
}
\]

Equivalently, the maximal determinantal divisor of the generic polynomial matrix is a unit in \(F[\lambda]\).

The logic is:
- A positive-degree common gcd means the generic pencil has a finite rank-drop value over the algebraic closure \(\overline F\). The projective bad locus therefore contains the generic point of \(U\). Since it is closed in \(U\), it must be all of \(U\). No full-column-rank member is feasible.
- A unit gcd means the generic point is not bad. Hence the bad locus is a proper closed subset, and its complement contains complex parameter values. AZE is feasible.
This is stronger than merely saying that a generic member is likely to work. It is an exact algebraic decision criterion.

Important qualification: this criterion concerns complex parameter values \(t\). If the observer augmentation is required to be real, the complex generic criterion alone does not establish the existence of a real feasible parameter. A nonempty complex Zariski-open set need not contain a real point of a particular real parameter locus. The real and complex versions must be kept separate.
6. Does the genericity criterion give a polynomial-time algorithm?
It gives a promising algorithmic route, but the complexity model matters.
6.1 Arithmetic-operation model
The generic gcd can be computed by treating \(F=\mathbb C(t_1,\ldots,t_s)\) as the coefficient field and computing a Smith form, or an equivalent polynomial-matrix normal form, of
\[
P(t,\lambda)\in F[\lambda]^{q\times k}.
\]

For a full-column-normal-rank polynomial matrix, the product of its Smith invariant factors is, up to a nonzero constant, the gcd of its maximal minors. Thus the AZE test is equivalent to asking whether that product is a unit.

This approach avoids explicitly expanding all
\[
\binom qk
\]

maximal minors. That matters: an algorithm which constructs every maximal minor may be exponentially large when \(k\) is in the middle range.

There is substantial algorithmic literature on Smith forms of univariate polynomial matrices over a coefficient field:
- Kaltofen, Krishnamoorthy and Saunders give parallel algorithms for Hermite and Smith forms, including polynomial-size circuits and efficient sequential algorithms over standard coefficient fields. 
  
  工业与应用数学学会+1
- Storjohann and Labahn give a fast Las Vegas algorithm for the Smith form of a polynomial matrix over \(\mathbb Q[x]\), with explicit bit-complexity estimates. 
  
  科学直通车
- Villard develops a deterministic polynomial-time Smith-form algorithm based on generalized subresultants. 
  
  科学直通车
These results are relevant because the spectral variable \(\lambda\) is univariate. They provide algorithmic tools for the generic polynomial-matrix calculation.

However, the coefficient field in AZE is not simply \(\mathbb Q\) or \(\mathbb C\). It is the rational function field
\[
\mathbb Q(t_1,\ldots,t_s)
\quad\text{or}\quad
\mathbb C(t_1,\ldots,t_s),
\]

depending on the input model. A polynomial-time algorithm measured in arithmetic operations over an abstract coefficient field does not automatically yield a polynomial-time bit algorithm for rational functions in a growing number of variables. Numerators, denominators, and intermediate expressions may grow.

So the careful conclusion is:
- Arithmetic model: the generic Smith-form/gcd route is a natural algorithmic solution, and standard univariate polynomial-matrix algorithms are directly relevant.
- Bit-complexity model: a polynomial bound must account for the representation and growth of multivariate rational functions. The cited Smith-form algorithms do not, by themselves, establish a polynomial bit-complexity bound for arbitrary AZE input.
- Fixed number of parameters: this is a particularly promising regime. If \(s\) is fixed, multivariate polynomial representations of bounded degree have polynomially many coefficients in the degree bound. This makes a bit-complexity result more plausible, but one still needs explicit bounds for the degrees and coefficient heights arising in the generic Smith-form computation.
6.2 A randomized-specialisation route
There is another useful consequence of the open-or-empty dichotomy.

Suppose the AZE input has rational coefficients and the parameter domain is the full complex affine space. If AZE is a yes-instance, then the feasible set contains a nonempty Zariski-open subset. If it is a no-instance, no full-column-rank parameter value is feasible.

Therefore, a randomly selected parameter value has the following one-sided property:
- if the sampled pencil has full column rank \(H(t)\) and has no finite rank drop, then AZE is certainly a yes-instance;
- if AZE is a no-instance, no valid sample can pass this test;
- if AZE is a yes-instance, a sufficiently generic sample will pass with high probability.
Testing one sampled pencil is an exact univariate polynomial-matrix computation over the sampled coefficient field. This suggests a one-sided randomized algorithm, provided one supplies an effective degree bound controlling the probability of hitting the proper bad locus and accounts for the bit complexity of the sample and the Smith-form calculation.

I would present this as a promising algorithmic consequence, not yet as a fully established complexity theorem for AZE. The remaining work is to state the input encoding, give an explicit degree bound for the exceptional parameter set, and combine it with a bit-complexity bound for the sampled polynomial-matrix test.
6.3 The square case is completely settled
If \(q=k>0\) and \(H\) has full column rank, then \(H\) is invertible and
\[
\det(\lambda H-G)
\]

is a polynomial of degree \(k\), with leading coefficient \(\det H\ne0\). By the fundamental theorem of algebra, it has a finite complex root. At that root the square pencil loses rank.

Consequently,
\[
\boxed{q=k>0\quad\Longrightarrow\quad\text{AZE is always a NO-instance}.}
\]

If \(q<k\), full column rank of \(H\) is impossible, so the full-column-rank AZE problem is again automatically a no-instance.

The nontrivial regime is therefore
\[
\boxed{q>k.}
\]

For an unrestricted family of pairs \((H,G)\), the situation is quite different from the square case: full-column-rank pencils with no finite rank drop do exist. For example,
\[
P(\lambda)=
\begin{bmatrix}
\lambda I_k\\
-I_k
\end{bmatrix}
\]

has full column rank \(k\) for every \(\lambda\in\mathbb C\). The challenge is whether the prescribed affine constraints on the pair permit such a pencil.
6.4 What the structured Smith-form literature does and does not establish
Murota studies structured polynomial matrices whose entries contain algebraically independent parameters and whose fixed part satisfies particular minor conditions. For that special class, the Smith form can be computed using a polynomial-time matroid-theoretic algorithm. 

工业与应用数学学会+1

This is relevant conceptually: it demonstrates that generic parameter dependence in Smith forms can sometimes be analysed combinatorially and efficiently. But the hypotheses are specialised. It is not a general complexity result for arbitrary affine families
\[
\lambda H(t)-G(t).
\]

Similarly, work on nearby nontrivial Smith forms studies the geometry and numerical optimisation of perturbations that produce a nontrivial Smith form. It is useful background for the geometry of rank-drop loci, but it does not establish NP-hardness or polynomial-time solvability of AZE as stated. 

科学直通车+1

A further distinction: the two-parameter matrix-pencil problem in the literature asks for spectral parameters at which a fixed pencil loses rank. That is not the same as AZE, which asks whether a member of an affine family of pencils avoids all finite rank drops. The two problems should not be conflated. 

工业与应用数学学会

6.5 NP-hardness and \(\exists\mathbb R\)-hardness: what can be claimed?
I did not locate a direct NP-hardness or \(\exists\mathbb R\)-hardness theorem for the precise AZE problem in the form given in the report. The literature found in this search is principally about canonical forms, symbolic computation, and structured polynomial matrices, rather than a complexity classification of this existential affine-family problem.

That is not a proof that no such result exists. It does mean that the report should not cite general NP-hardness statements about polynomial optimisation, matrix completion, or eigenvalue problems as if they automatically applied to AZE. A reduction must preserve the special dependence
\[
P(t,\lambda)=\lambda H(t)-G(t)
\]

and the full-column-rank leading coefficient condition.

There is also a reason to be cautious about expecting NP-hardness for the complex affine-space version of AZE. The genericity theorem says that a single good member implies a Zariski-open dense set of good members. Thus the decision problem is a generic algebraic property, not an arbitrary existential search over an affine space. This is precisely the setting in which generic polynomial-matrix algorithms and random specialisation can be effective.

In particular, a proof that AZE is NP-hard would have to be reconciled with the generic gcd criterion and the apparent one-sided randomised algorithmic route. It is not impossible for a problem with a randomised algorithm to be NP-hard, but such a result would have strong complexity-theoretic consequences (for example, it would imply \(\mathrm{NP}\subseteq\mathrm{RP}\) if the algorithm were indeed in RP).

For a complexity investigation, I recommend separating three problems:
Problem	Parameter domain	Natural complexity question
Complex affine AZE	\(t\in\mathbb C^s\)	Generic gcd / polynomial-matrix computation
Real affine AZE	\(t\in\mathbb R^s\)	Does the complex feasible open set contain a real point?
Observer DEC	\(R\in\mathbb R^{(q-r)\times n}\), or \(\mathbb C^{(q-r)\times n}\)	Rank-stratified existence with (5a)

The second and third problems do not inherit the first problem's genericity conclusion without additional hypotheses. In particular, a complex nonempty open feasible set need not meet the real parameter locus if that real locus is not Zariski dense in the complex parameter space.

7. What this means for \(q_{\min}\)
The report's stated question is whether computing \(q_{\min}\) is NP-hard. I would keep that question separate from AZE until the reduction is repaired.

For a fixed observer data set, define
\[
\mathrm{DEC}(q)=
\begin{cases}
\text{YES},&\exists R\text{ satisfying (5a) and (5b)},\\
\text{NO},&\text{otherwise}.
\end{cases}
\]

Appending a zero row to \(\mathcal L\) preserves both rank conditions. Hence
\[
\mathrm{DEC}(q)=\mathrm{YES}
\quad\Longrightarrow\quad
\mathrm{DEC}(q+1)=\mathrm{YES}.
\]

So the decision version is monotone in \(q\), and
\[
q_{\min}\le q
\iff
\mathrm{DEC}(q)=\mathrm{YES},
\]

assuming the same underlying fixed data and admissible augmentation convention.

Thus a valid many-one hardness reduction to \(\mathrm{DEC}(q)\) would be a natural route to hardness of the threshold version of \(q_{\min}\). But the current AZE reduction does not yet provide that reduction, because of the lower-rank candidate issue.

Also, complexity claims require an explicit encoding model. For example, a standard formulation would take \(A,C,L_0\) over \(\mathbb Q\) (or a specified algebraic number field), with rational entries encoded in binary, and ask whether a real \(R\) exists. If the input is arbitrary complex data with no finite representation, conventional bit-complexity classes such as NP and \(\exists\mathbb R\) are not directly applicable.

8. Recommended next steps
I would not spend the next round trying to prove NP-hardness of unrestricted complex AZE. The genericity result suggests a more productive order.
Priority 1 — Formalise the generic AZE theorem

Prove, with all hypotheses explicit, that for a complex affine family with nonempty full-column-rank domain \(U\),
\[
\mathrm{AZE}=\mathrm{YES}
\iff
\gcd_{\,\mathbb C(t)[\lambda]}
\{\text{maximal minors of }\lambda H(t)-G(t)\}=1.
\]

This should be a standalone theorem, with the projective no-infinity argument included.

Priority 2 — Establish the computational complexity of that test

Compare:
- generic Smith/Popov form over \(\mathbb Q(t)[\lambda]\);
- a generic determinantal-divisor algorithm;
- random rational specialisation followed by an exact univariate Smith-form computation.
Separate arithmetic-operation complexity, bit complexity, and randomised complexity. Avoid expanding all maximal minors explicitly.

Priority 3 — Repair the observer reduction

Prove the identity
\[
(5a)\iff\ker H\subseteq\ker H_A
\]

as a formal lemma, and decide whether the intended observer problem can force \(\operatorname{rank}H=k\). If not, formulate the rank-stratified AZE target.

Priority 4 — Only then pursue hardness

If the intended problem is the real observer problem, investigate real-point existence on the rank strata. That is where genuinely existential real-algebraic complexity may enter, rather than in the unrestricted complex affine AZE problem.

Suggested theorem to add to the next report
A useful next result would be the following.

Theorem (generic affine-pencil zero-exclusion criterion). Let
\[
H(t),G(t)\in\mathbb C[t_1,\ldots,t_s]^{q\times k}
\]

be affine-linear matrix functions, and assume \(H(t)\) has full column rank for at least one \(t\in\mathbb C^s\). Put \(F=\mathbb C(t_1,\ldots,t_s)\). Then the following are equivalent:
1. There exists \(t\in\mathbb C^s\) such that \(H(t)\) has full column rank and \(\lambda H(t)-G(t)\) has full column rank for every \(\lambda\in\mathbb C\).
2. The generic pencil \(\lambda H(t)-G(t)\) has full column rank at every finite \(\lambda\) over \(\overline F\).
3. The gcd in \(F[\lambda]\) of all \(k\times k\) minors of \(\lambda H(t)-G(t)\) is a unit.
The proof uses the projective incidence construction and irreducibility of the full-column-rank parameter domain.

This theorem would turn AZE from a seemingly existential search problem into a generic polynomial-matrix computation problem. It is the most important mathematical consequence of the current line of work.
9. Overall verdict on 35_reduction_to_aze.md
Part of the report	Assessment
\(K\cap AK=0\) realizability lemma	Correct
Dimension restriction \(n-p\ge2k\)	Correct
Explicit borderline construction	Consistent
Fixed-row absorption	Needs an explicit reduction
AZE hardness \(\Rightarrow\) observer DEC hardness	Not established
Need to account for rank strata	Essential gap
AZE complexity question	Promising generic algorithmic route; no direct hardness result identified

My main recommendation: preserve the realizability lemma. It is a sound and useful structural result. But revise the claimed consequence to a conditional statement:
The observer family realises the affine AZE family with the prescribed top blocks whenever \(K\cap AK=0\). A hardness transfer to the original observer decision problem additionally requires either a proof that every feasible observer candidate has full-column-rank \(H\), or a reduction that also controls all rank-deficient strata.

Then make the generic function-field gcd criterion the next main result for AZE. It is likely to be more useful than an immediate attempt at an NP-hardness reduction, and it may show that the unrestricted complex affine version is algorithmically much more tractable than the observer problem.
References worth adding to the report
1. E. Kaltofen, M. S. Krishnamoorthy and B. D. Saunders, “Fast Parallel Computation of Hermite and Smith Forms of Polynomial Matrices,” SIAM Journal on Algebraic and Discrete Methods. Article and DOI.
2. A. Storjohann and G. Labahn, “A fast Las Vegas algorithm for computing the Smith normal form of a polynomial matrix,” Linear Algebra and its Applications 253 (1997), 155–173. Article and DOI.
3. G. Villard, “Generalized Subresultants for Computing the Smith Normal Form of Polynomial Matrices,” Journal of Symbolic Computation 20 (1995), 269–286. Article and DOI.
4. K. Murota, “On the Smith Normal Form of Structured Polynomial Matrices.” Article and DOI.
5. M. Giesbrecht, J. Haraldson and G. Labahn, “Computing nearby non-trivial Smith forms,” Journal of Symbolic Computation 102 (2021), 304–327. Article and DOI.
These references support the polynomial-matrix algorithmic background. They should not be cited as direct NP-hardness or polynomial-time classifications of AZE.