Mathematical audit of 36_rp_argument.md
The report makes a serious attempt to turn the geometric results into a randomized complexity statement. Its central intuition is promising: on a fixed full-rank chart, the bad spectral locus is closed, and a bounded-degree description could make random sampling effective.

However, the claimed proof of \(\mathrm{DEC}(q)\in\mathrm{RP}\) is not valid as written. There are several independent gaps, including one concrete coefficient-count error in the Bézout system, an incorrect determinantal description of its inconsistency locus, and a sampling construction that does not yet respect the observer's fixed rows or cover all rank strata.

I would not state \(\mathrm{DEC}(q)\in\mathrm{RP}\), nor infer a conclusion about NP-hardness, on the basis of this report. There is still useful progress here: the bounded-degree Bézout lemma is applicable, the inconsistency condition is exactly expressible by a rank comparison, and the projective closedness theorem remains a sound route to a one-sided sampling algorithm provided an appropriate sampler for each relevant parameter space can be constructed.

I will distinguish the algebraic issues from the complexity issues, since repairing the former does not automatically repair the latter. 
36_rp_argument.md

1. Question 1: the Bézout solvability identity is correct; the asserted minor equation is not
Fix a candidate with
\[
\omega=\operatorname{rank}H>0,
\]

and let \(p_1,\ldots,p_N\) be all \(\omega\times\omega\) minors of
\[
P(\lambda)=\lambda H-H_A.
\]

Each \(p_i\) has degree at most \(\omega\). The bounded-degree Bézout lemma says
\[
\gcd(p_1,\ldots,p_N)=1
\iff
\exists u_1,\ldots,u_N,\quad
\sum_{i=1}^N u_i(\lambda)p_i(\lambda)=1,
\quad \deg u_i\leq\omega-1.
\]

This is the correct starting point.
1.1 The coefficient system has \(2\omega\), not \(2\omega-1\), rows
Write
\[
u_i(\lambda)=\sum_{j=0}^{\omega-1}u_{ij}\lambda^j.
\]

Then
\[
\deg\left(\sum_i u_ip_i\right)\leq
(\omega-1)+\omega=2\omega-1.
\]

To impose the polynomial identity
\[
\sum_i u_i p_i=1,
\]

one must match the coefficients of
\[
\lambda^0,\lambda^1,\ldots,\lambda^{2\omega-1}.
\]

There are \(2\omega\) coefficient equations. Thus the coefficient system should be written
\[
\boxed{M_\omega(R)u=b_\omega,\qquad
M_\omega(R)\in
\mathbb C^{\,2\omega\times N\omega},\quad
b_\omega=(1,0,\ldots,0)^{\mathsf T}.}
\]

The report matches only the coefficients through \(\lambda^{2\omega-2}\). It omits the top-degree coefficient equation. That omission is not harmless: the top-degree coefficient of \(\sum_i u_ip_i\) is generally not identically zero for arbitrary multipliers \(u_i\).

The simplest check is \(\omega=1\). Then the \(p_i\) are affine-linear polynomials and the \(u_i\) are constants. The identity
\[
\sum_i u_i(a_i\lambda+b_i)=1
\]

requires both
\[
\sum_i u_i a_i=0,\qquad
\sum_i u_i b_i=1.
\]

There are two equations, not one. Omitting the first would incorrectly declare many systems solvable.

So the correct unknown and equation counts are
\[
\boxed{\#\text{unknowns}=N\omega,\qquad
\#\text{equations}=2\omega.}
\]

1.2 The rank comparison is an exact identity
With the corrected coefficient matrix, Bézout solvability is exactly
\[
M_\omega(R)u=b_\omega
\quad\Longleftrightarrow\quad
\operatorname{rank}M_\omega(R)
=
\operatorname{rank}[M_\omega(R)\mid b_\omega].
\]

Consequently, on the fixed rank-\(\omega\) domain,
\[
\boxed{
\mathcal B_\omega
=
\left\{R:
\operatorname{rank}[M_\omega(R)\mid b_\omega]
>
\operatorname{rank}M_\omega(R)
\right\},
}
\]

where \(\mathcal B_\omega\) denotes the bad spectral locus, namely the candidates for which the maximal minors have a nonconstant common factor.

This is an equality of sets, not merely an equality after taking Zariski closure. It follows directly from the elementary consistency criterion for a linear system. The fact that the bad locus is also known to be closed is a separate geometric result; it is not needed to establish this rank identity.
1.3 But the “all \((2\omega-1)\)-minors vanish” formula is false
The report claims
\[
\mathcal B_\omega
=
\{R:\text{all }(2\omega-1)\text{-minors of }[M(R)\mid b]\text{ vanish}\}.
\]

There are two errors here:
1. the coefficient system has \(2\omega\) rows, not \(2\omega-1\);
2. even with the corrected number of rows, inconsistency is not equivalent to the vanishing of all maximal minors of the augmented matrix.
The second point is important. Let \(M\) have \(m\) rows. Inconsistency means
\[
\operatorname{rank}[M\mid b]>\operatorname{rank}M.
\]

It does not mean \(\operatorname{rank}[M\mid b]<m\). For example, if
\[
\operatorname{rank}M=m-1,\qquad
\operatorname{rank}[M\mid b]=m,
\]

the system is inconsistent, but the augmented matrix has a nonzero \(m\times m\) minor.

Conversely, if
\[
\operatorname{rank}M=m-2,\qquad
\operatorname{rank}[M\mid b]=m-1,
\]

the system is still inconsistent, although all \(m\times m\) minors of the augmented matrix vanish.

Thus maximal-minor vanishing does not characterize inconsistency.

The correct algebraic description is a rank-stratified constructible description. For each \(s\),
\[
\begin{aligned}
\mathcal B_{\omega,s}
=\{R:\;&\operatorname{rank}M_\omega(R)=s,\\
&\operatorname{rank}[M_\omega(R)\mid b_\omega]\ge s+1\}.
\end{aligned}
\]

Then
\[
\boxed{\mathcal B_\omega
=\bigcup_{s=0}^{2\omega-1}\mathcal B_{\omega,s}.}
\]

Each rank condition is expressible by minors: rank exactly \(s\) is the conjunction that all \((s+1)\)-minors vanish and at least one \(s\)-minor is nonzero; rank at least \(s+1\) is the condition that at least one \((s+1)\)-minor is nonzero. Hence each \(\mathcal B_{\omega,s}\) is constructible.

There is no contradiction with the previously established closedness of \(\mathcal B_\omega\). A set can have a constructible description by a union of rank strata and also be closed for a separate structural reason. What fails is the report's proposed single family of maximal-minor equations.
1.4 Correct degree bound from the coefficient system
Each maximal minor \(p_i\) is a determinant of an \(\omega\times\omega\) matrix whose entries are affine-linear in \(R\). Therefore each coefficient of \(p_i(\lambda)\), as a polynomial in \(R\), has degree at most \(\omega\).

The entries of the corrected matrix \(M_\omega(R)\) consequently have degree at most \(\omega\) in \(R\), while \(b_\omega\) is constant.

A minor of size \(s\) of \(M_\omega(R)\), or of its augmentation, has degree at most
\[
s\omega.
\]

Since \(M_\omega\) has \(2\omega\) rows, the largest relevant minor size is \(2\omega\). Thus a uniform bound for the rank-stratified equations is
\[
\boxed{\deg_R\le 2\omega^2.}
\]

This is the corrected counterpart of the report's \(2\omega(2\omega-1)\). It is not the same formula, because the number of coefficient equations was undercounted.

This degree bound is valid for the rank conditions of the corrected coefficient system. It does not by itself prove an RP algorithm; sampling and representation issues remain.
36_rp_argument.md
2. The degree bound after rank factorisation
The report next parameterises a rank-\(\omega\) matrix as
\[
H=UV^{\mathsf T},
\qquad
U\in\mathbb C^{q\times\omega},\quad
V\in\mathbb C^{k\times\omega},
\]

with both \(U\) and \(V\) of full column rank.

This is a valid parameterisation of the rank-\(\omega\) matrices \(H\). But the corresponding \(H_A\) must also be parameterised compatibly with (5a). The exact form is
\[
\boxed{H_A=ZV^{\mathsf T},\qquad Z\in\mathbb C^{q\times\omega}.}
\]

Indeed,
\[
\ker H=\ker V^{\mathsf T},
\]

and
\[
\ker H\subseteq\ker H_A
\iff
H_A=ZV^{\mathsf T}
\]

for some \(Z\). Thus the appropriate rank-\(\omega\) parameterisation is a triple \((U,V,Z)\), not just \((U,V)\).

The pencil becomes
\[
\lambda H-H_A=(\lambda U-Z)V^{\mathsf T}.
\]

For row set \(I\) and column set \(J\), both of cardinality \(\omega\), its maximal minor factors as
\[
\det\big((\lambda U-Z)V^{\mathsf T}\big)_{I,J}
=
\det\big((\lambda U-Z)_{I,:}\big)
\det\big(V_{J,:}^{\mathsf T}\big).
\]

This factorisation is useful: the dependence on the spectral variable lies entirely in the first determinant.
2.1 Corrected total-degree bound
Each maximal minor has degree at most \(\omega\) in the entries of \(U,Z\), and at most \(\omega\) in the entries of \(V\). Its total degree in all factor variables is therefore at most \(2\omega\).

The corrected Bézout coefficient matrix has \(2\omega\) rows. A rank condition involves minors of size at most \(2\omega\). Thus the pullback of any such minor to the \((U,V,Z)\)-parameter space has total degree at most
\[
\boxed{2\omega\cdot 2\omega=4\omega^2.}
\]

More precisely, its degree in the \(U,Z\) variables is at most \(2\omega^2\), and its degree in the \(V\) variables is at most \(2\omega^2\).

Accordingly, if one obtains a nonzero polynomial of this degree whose zero set contains the bad pullback, Schwartz–Zippel gives the familiar bound
\[
\Pr[\text{sample lies in that zero set}]
\leq \frac{4\omega^2}{|S|},
\]

for independent uniform choices of the factor variables from a finite subset \(S\) of a field, provided the polynomial is not identically zero on the parameter space being sampled.

The report's \(2\omega(2\omega-1)\) follows from its incorrect \(2\omega-1\)-row coefficient system. It should be replaced by \(4\omega^2\) under this direct total-degree accounting. 
36_rp_argument.md

2.2 A subtle but important distinction: degree of equations versus degree of a single witness polynomial
There is one further issue to make explicit. The bad locus is described by the rank comparison
\[
\operatorname{rank}[M_\omega\mid b_\omega]>
\operatorname{rank}M_\omega.
\]

This is a union of rank strata, not generally the zero set of one specified maximal minor polynomial. To apply Schwartz–Zippel in the stated way, one needs the following argument:
- the parameter domain being sampled is irreducible;
- the bad locus is a proper closed subset of that domain;
- a nonzero polynomial \(f\) of controlled degree can be chosen whose zero set contains the bad locus.
For an affine irreducible parameter space, a proper closed set has at least one nonzero defining polynomial. If the equations defining it are known and their degrees are bounded, one can choose one such nonzero equation. But the rank-stratified description alone does not identify a single nonzero polynomial that works uniformly across all components.

This is not an obstacle in principle. It means the proof must explicitly combine the degree-bounded rank equations with irreducibility and properness. The closedness theorem from the earlier report supplies the geometric part; the corrected coefficient-system construction supplies candidate equations. The connection between them still needs to be written carefully.
3. Question 2: the sampling argument does not yet sample the observer chart
This is the largest obstacle after the coefficient-system correction.

The report proposes:
1. draw \(U,V\) randomly;
2. form a target pair \((H,H_A)\);
3. solve
   \[
   H(R)=UV^{\mathsf T},\qquad
   H_A(R)=\text{target}
   \]
   for \(R\);
4. invoke the realizability lemma to guarantee solvability.
The problem is that the realizability lemma in the previous report was for an unrestricted \(q\times n\) matrix \(M\). In the observer problem,
\[
M=\begin{bmatrix}L_0\\R\end{bmatrix},
\]

and the first \(r\) rows are fixed. Consequently, the lemma does not guarantee that an arbitrary target pair \((H,H_A)\) is realisable.
3.1 The fixed-block constraints
Every realisable pair must satisfy
\[
H_{1:r,:}=L_0N_K,\qquad
(H_A)_{1:r,:}=L_0AN_K.
\]

A randomly generated pair \(UV^{\mathsf T},ZV^{\mathsf T}\) will not, in general, satisfy these equations.

Thus the proposed sampling procedure is valid in the unrestricted case \(r=0\), under \(K\cap AK=0\), but it is not justified for the stated observer problem with general fixed \(L_0\).

To repair it, one needs a sampler whose image is dense in the appropriate rank-\(\omega\) part of the affine slice
\[
\mathscr A_{L_0}
=
\left\{(H,H_A):
H_{1:r,:}=L_0N_K,\ 
(H_A)_{1:r,:}=L_0AN_K
\right\},
\]

subject to
\[
\operatorname{rank}H=\omega,\qquad
\ker H\subseteq\ker H_A.
\]

One cannot simply sample arbitrary \(U,V,Z\) and then solve for \(R\).
3.2 The unrestricted case is a useful special case, not a proof of the general case
If \(r=0\) and \(K\cap AK=0\), the realizability map is surjective. Then every triple \((U,V,Z)\) with \(U,V\) full column rank gives a realisable pair
\[
H=UV^{\mathsf T},\qquad H_A=ZV^{\mathsf T}.
\]

In this special setting, the factorisation gives a plausible route to sampling the rank-\(\omega\) compatible-pair space.

But even here, the proof must establish that the pullback of the bad locus is proper whenever the bad locus is proper. The factorisation map is surjective onto the rank-\(\omega\) compatible-pair space, so this follows if the sampled parameter domain is the full factor space with the full-rank restrictions. Those restrictions are nonempty Zariski-open conditions, and hence do not destroy irreducibility.

For \(r>0\), the same argument requires a parameterisation of the intersection with the prescribed-block constraints. It may be empty, reducible, or have components of different dimensions. The report has not supplied such a parameterisation.
3.3 The chart and component problem remains
There are two kinds of decomposition here:
- a rank decomposition, according to \(\omega=\operatorname{rank}H\);
- a pivot/chart decomposition, according to which \(\omega\times\omega\) minor of \(H\) is nonzero.
For a fixed \(\omega\), the number of possible column subsets is \(\binom{k}{\omega}\), and if row pivots are also used, there can be up to
\[
\binom{k}{\omega}\binom{q}{\omega}
\]

principal pivot charts.

For fixed \(\omega\), this number is polynomial in \(q,k\). If \(\omega\) is allowed to grow with the input, it can be exponential.

More fundamentally, the intersection of an affine observer parameter space with the rank-\(\omega\) determinantal variety need not be irreducible. A random parameterisation of one component will not find a feasible point confined to another component.

The report mentions component decomposition, but does not give an algorithm or a polynomial bound for it. Irreducible decomposition of an algebraic set is not a free operation in a bit-complexity argument.

Conclusion on Question 2: the Schwartz–Zippel estimate is a valid conditional estimate for a nonzero polynomial on a suitable irreducible parameter space. The report has not yet constructed that parameter space or a polynomial-time sampler covering all feasible observer components. It therefore does not establish the required sampling claim for \(\mathrm{DEC}(q)\).
4. Question 3: what is the weakest correct complexity statement?
There are several levels of conclusion, and it is important not to conflate them.
4.1 What is justified now
The following conditional statement is supported by the mathematics:

Conditional one-sided sampling proposition. Let \(X\) be an explicitly parameterised irreducible algebraic set over an effectively represented infinite field, and suppose:
1. the bad spectral locus \(B\subseteq X\) is closed;
2. membership of a sampled point in \(X\setminus B\) can be checked exactly in polynomial time;
3. there is a polynomial-time sampler whose distribution is supported on \(X\), and whose pullback to the parameter space is Zariski dense;
4. the bad locus, when proper, is contained in the zero set of a nonzero polynomial of explicitly bounded degree \(D\).
Then sampling the parameters from a sufficiently large finite subset \(S\) gives
\[
\Pr[\text{sample is bad}]\leq D/|S|.
\]

If \(B=X\), every sample is bad. If \(B\subsetneq X\), a sufficiently large \(S\) gives a constant probability of sampling a good point. Exact verification therefore yields a one-sided randomized test for feasibility on \(X\).

This is a genuine and useful result. It is a per-irreducible-parameter-space statement. It is not yet an RP result for the full observer decision problem.
4.2 Why the number of rank strata is not the only issue
The report correctly observes that
\[
\sum_{\omega=0}^k\binom{k}{\omega}=2^k
\]

is exponential. But it is worth separating three possible sources of complexity:
Source	What is known from the current argument?
Number of possible ranks \(\omega\)	Only \(k+1\), which is polynomial
Number of pivot charts for a fixed \(\omega\)	Can be \(\binom{k}{\omega}\binom{q}{\omega}\)
Number and representation of irreducible components	No polynomial bound or efficient decomposition has been established

The number of ranks alone does not imply an exponential number of cases. The potential exponential cost comes from pivot charts, component decomposition, and the construction of samplers on the relevant intersections.

A more global approach might avoid enumerating all pivot charts by using a parameterisation of the rank-\(\omega\) determinantal variety. That is precisely what \(H=UV^{\mathsf T}\) attempts. But for the observer problem, this parameterisation must be intersected with the affine constraints imposed by \(L_0\), and the report does not yet solve that problem.
4.3 A legitimate restricted result
There is a meaningful result available if the problem is restricted to a regime in which:
- \(\omega\) is fixed or bounded by a constant;
- the observer pair space is the unrestricted one (for example, \(r=0\)) or an explicitly parametrised irreducible affine slice;
- \(K\cap AK=0\), so the required pair realisation is available;
- the sampler, candidate reconstruction, and exact verification all have polynomial bit complexity.
In that setting, the corrected Bézout system has
\[
N\omega
=\binom{q}{\omega}\binom{k}{\omega}\omega
\]

unknowns and \(2\omega\) equations. For fixed \(\omega\), the number of minors and the coefficient-system size are polynomial in \(q,k\). The corrected degree bound is \(O(\omega^2)\), and hence is constant when \(\omega\) is fixed.

Under those additional hypotheses, the per-stratum test can be placed in RP. This is a restricted theorem, not a theorem for unrestricted \(\mathrm{DEC}(q)\).

I would state it in the paper only after specifying the input encoding and giving the actual sampler. In particular, the phrase “provided the chart sampling and component decomposition are as described” should be replaced by a precise algorithm and a proved polynomial bound. 
36_rp_argument.md

4.4 Finite-field sampling versus rational sampling
The report says that over \(\mathbb Q\) one should work over a large prime field and verify candidates exactly. There is a subtle issue here.

A point found modulo a prime \(p\) is not automatically a rational point of the original problem. A modular solution to
\[
M(R)u=b
\]

does not, by itself, lift to a rational solution \(R\) of the observer constraints. Nor does a good modular pencil certify a good rational pencil.

There are two ways to formulate a valid argument:

Option A: sample rational/integer parameters directly. If the parameterisation is defined over \(\mathbb Q\), sample its free parameters from a finite set \(S\subset\mathbb Z\), reconstruct \(R\) over \(\mathbb Q\), and verify the resulting candidate exactly. Schwartz–Zippel applies to a nonzero polynomial over \(\mathbb Q\) evaluated on \(S\). This avoids a lifting step.

Option B: use modular computations only as a computational aid. If sampling and verification are performed modulo \(p\), one needs a separate lifting or certificate argument to establish a valid solution over the original field. Modular success alone is insufficient.

Option A is the cleaner route for an RP proof, but only if the parameterisation and reconstruction are rational and polynomially bounded. For arbitrary complex input data, the ordinary binary-input complexity classes RP, NP and \(\exists\mathbb R\) are not even defined without a finite representation of those data.

There is also a coefficient-height issue: exact verification of a reconstructed rational candidate must run in polynomial time in the input length and the random bits used. A proof based solely on algebraic degree does not control numerator and denominator growth.

5. Question 4: what does this say about \(q_{\min}\) and NP-hardness?
The implication the report has in mind is essentially correct if the RP result is first proved for the same decision language used in the hardness reduction.

Suppose a binary-input decision language \(L\) is in RP and is NP-hard under deterministic polynomial-time many-one reductions. Then every language in NP reduces to \(L\), so running the RP algorithm after the reduction gives an RP algorithm for every NP language. Therefore
\[
\mathrm{NP}\subseteq\mathrm{RP}.
\]

Since
\[
\mathrm{RP}\subseteq\mathrm{NP},
\]

this would imply
\[
\boxed{\mathrm{NP}=\mathrm{RP}.}
\]

So the usual formulation is not “NP-hardness is impossible”; it is:
If the claimed RP algorithm is valid, NP-hardness of the corresponding decision language under deterministic polynomial-time many-one reductions would imply \(\mathrm{NP}=\mathrm{RP}\).

That is a conditional complexity-theoretic consequence, not a proof that the problem is not NP-hard.
5.1 Threshold decision versus optimisation
The report correctly distinguishes the threshold problem from the optimisation problem, but the relationship should be stated carefully.

For a fixed underlying instance, define
\[
\mathrm{DEC}(q)=
\bigl[\exists R\text{ satisfying (5a),(5b) with augmentation dimension }q\bigr].
\]

If zero rows may be appended to the augmentation without changing admissibility, then
\[
\mathrm{DEC}(q)=\mathrm{YES}
\implies
\mathrm{DEC}(q+1)=\mathrm{YES}.
\]

Consequently, whenever \(q_{\min}\) is finite,
\[
q_{\min}\le q
\iff
\mathrm{DEC}(q)=\mathrm{YES}.
\]

This establishes the monotonic threshold relationship. It does not by itself establish that an RP algorithm for one fixed \(q\) computes \(q_{\min}\) in RP. For that, one also needs:
- a known finite upper bound on \(q_{\min}\);
- an RP algorithm uniformly applicable to all thresholds in the binary search;
- a polynomial-time bound on the number and cost of calls.
Likewise, if \(q_{\min}\) is called NP-hard under an optimisation reduction, one must specify the reduction notion. The clean statement is about the threshold language \(\mathrm{DEC}\): if that language is NP-hard and is in RP, then NP \(=\) RP. A claim about the optimisation function needs a reduction that connects its output to the threshold decision problem.
5.2 The current report does not establish the premise
Because the sampling construction is not yet valid for general observer data, the implication
\[
\mathrm{DEC}(q)\in\mathrm{RP}
\]

has not been proved. Hence the report cannot yet conclude that NP-hardness of \(\mathrm{DEC}(q)\) would imply NP \(=\) RP as a theorem about this particular problem. It can state this as a conditional observation:
If a polynomial-time one-sided randomized algorithm for the full binary-encoded \(\mathrm{DEC}(q)\) problem is established, then NP-hardness of \(\mathrm{DEC}(q)\) under deterministic polynomial-time many-one reductions would imply NP \(=\) RP.

That is accurate and worth recording.
6. Question 5: which paper-only results should be checked or formalised first?
I would not formalise the RP argument first. The most effective order is to settle the mathematical statements on which it depends, particularly the ones that can be checked independently of the algorithmic questions.

Here is my recommended priority order.
Priority 1 — Formalise the reduced spectral criterion (L7)
This is the central bridge between the original observer pencil and the smaller polynomial matrix:
\[
(5b)\iff
\gcd\{\text{all }\omega\times\omega\text{ minors of }
\lambda H-H_A\}\in\mathbb C^\times.
\]

It is used by almost every subsequent argument:
- the closedness of the bad locus;
- the Bézout coefficient system;
- the generic-gcd criterion;
- the rank-stratified formulation;
- the proposed randomized algorithm.
The proof should explicitly handle:
- \(\omega=0\), where spectral feasibility is automatic;
- \(\omega>0\), where full column rank of \(H\) gives full column normal rank of the reduced pencil;
- the relationship between the original kernel and the reduced pencil kernel;
- the field over which the gcd is computed.
This is the highest-value formalisation because a defect here would affect nearly the entire subsequent programme.
Priority 2 — Formalise the closedness of the bad locus
The projective proof is conceptually clean:
\[
P^h(R;\alpha,\beta)=\alpha H(R)-\beta H_A(R).
\]

On a full-column-rank chart, there is no common maximal-minor zero at infinity, because
\[
P^h(R;1,0)=H(R)
\]

has full column rank. Thus the common-zero incidence is closed in the product with \(\mathbb P^1\), and its projection is closed.

The main formalisation difficulty is not the linear algebra. It is representing the projective parameter space and using the closedness of projection from a projective variety. This may be more convenient to prove in a paper-level algebraic-geometric argument than in Lean, depending on the project's Mathlib infrastructure.

Still, I would regard this as the most important paper-only geometric theorem to check independently. The closedness statement is what turns a genericity argument into an all-or-nothing statement on an irreducible chart.
Priority 3 — Correct and formalise the Bézout coefficient system
This report has identified a concrete correction. The coefficient system must have \(2\omega\) equations, not \(2\omega-1\). The correct statement is
\[
\gcd(p_1,\ldots,p_N)=1
\iff
\exists u,\quad M_\omega(R)u=b_\omega,
\]

where
\[
M_\omega(R)\in\mathbb C^{2\omega\times N\omega}.
\]

I would formalise this as two separate lemmas:
1. the bounded-degree Bézout lemma;
2. the equivalence between the Bézout identity and solvability of the coefficient-matching linear system.
Then state the inconsistency condition exactly as
\[
\operatorname{rank}[M_\omega(R)\mid b_\omega]>
\operatorname{rank}M_\omega(R).
\]

Do not formalise the incorrect all-maximal-minors equation from the current report. Use the rank-stratified constructible description instead.
Priority 4 — Verify the realizability lemma with fixed rows included
The unrestricted lemma is correct, but the observer application needs a more precise version.

I recommend formalising the following two statements separately:
- unrestricted surjectivity when \(K\cap AK=0\);
- the exact image when the first \(r\) rows are fixed:
  \[
  \operatorname{im}\Psi_{L_0}
  {(H,H_A):H_{1:r,:}=L_0N_K,\
  (H_A)_{1:r,:}=L_0AN_K}.
  \]
The second identity is what the reduction and sampling arguments actually need.

Also, the explicit borderline construction should be checked by exact symbolic computation, not just a numerical rank calculation. Its validity is straightforward to establish using the displayed basis vectors, so this should be a relatively inexpensive verification.
Priority 5 — Verify the rank-stratified target and the equivalence with DEC
This is the most important conceptual issue for the hardness and RP programme.

The key identity
\[
(5a)\iff\ker H\subseteq\ker H_A
\]

is already reported as Lean-checked. The next step is to build the complete rank-stratified target using that identity.

For each \(\omega\), define the candidate set by
\[
\operatorname{rank}H=\omega,\qquad
\ker H\subseteq\ker H_A,
\]

and impose the reduced spectral condition on the induced \(\omega\)-column pencil. Then prove that the union over \(\omega\) is exactly the original observer decision problem.

This should be a standalone theorem:
\[
\boxed{\mathrm{DEC}(q)\iff\mathrm{RAZE}(q),}
\]

with the definition of RAZE fully specified.

It is essential that \(\omega=0\) be included. Excluding that stratum without a proof that it is impossible under the fixed data would be incorrect.
Priority 6 — Revisit the per-layer complexity claims
The report says that \(\omega=0\) and \(\omega=1\) are polynomial-time, while \(\omega\ge2\) reduces to a non-emptiness/identity test.

I would check these claims after the preceding results. In particular:
- \(\omega=0\): the reduced spectral condition is automatic, but feasibility of the fixed-row observer constraints still needs to be checked.
- \(\omega=1\): the reduced pencil is a \(q\times1\) column. The condition is that its entries have no common finite zero. This is a univariate gcd computation, but the observer feasibility constraints and coefficient encoding must be included.
- \(\omega\ge2\): a generic gcd or determinantal-divisor test is natural, but calling it an “identity test” is not enough to establish polynomial bit complexity.
I would not claim a complexity boundary at \(\omega=2\) without a careful input-size analysis.

7. The machine-checked audit: what it establishes and what it does not
The report lists the following Lean declarations as compiling successfully:
- the factorisation characterisation of (5a);
- well-definedness and uniqueness of \(\Phi_K\);
- the dimension identity for \(\mathcal LK\);
- the kernel-fibre identity;
- the equivalence \((5a)\iff\ker H\subseteq\ker H_A\);
- full-column-rank \(H\) implying (5a).
These are important formal results. I would preserve the declaration names in the paper's proof-status appendix, as the report does. 
36_rp_argument.md

There is one qualification: from the report alone, I can audit the mathematical statements and their role, but I cannot independently verify that the declarations compile or that their Lean definitions exactly match the intended matrices. That would require the Lean source files and the relevant definitions. So I would describe these as “reported machine-checked results” until the source is available for independent review.

The paper-only dimension addition in the kernel identity is relatively low risk: once the set-level kernel-fibre identity is correct, it follows from rank–nullity for the map \(v\mapsto Lv\), with kernel \(D\).

The generic-gcd and closedness statements are more important mathematically and deserve a written proof independent of the formalisation status.

8. A corrected version of the report's main RP claim
I suggest replacing the current Section III.2 with a more conservative theorem.

Proposition (conditional RP test on an irreducible rank chart). Fix \(\omega>0\), and let \(X\) be an irreducible, explicitly parameterised observer candidate space on which
\[
\operatorname{rank}H=\omega,\qquad
\ker H\subseteq\ker H_A.
\]

Assume:
1. the bad spectral locus \(B\subseteq X\) is closed;
2. \(B\) is described by the corrected \(2\omega\)-equation Bézout coefficient system;
3. the rank-stratified equations have degree at most \(2\omega^2\) in the observer coordinates, or at most \(4\omega^2\) after the factor parameterisation \((U,V,Z)\);
4. a polynomial-time sampler for \(X\) is available, with Zariski-dense image;
5. exact candidate verification has polynomial bit complexity.
Then feasibility on \(X\) has a one-sided randomized test. If \(B=X\), no sample is accepted. If \(B\subsetneq X\), a sample is accepted with probability at least
\[
1-\frac{D}{|S|},
\]

where \(D\) is the applicable degree bound and \(S\) is the sampling set.

For example, choosing \(|S|\ge 2D\) gives acceptance probability at least \(1/2\) in the feasible case, provided the nonzero witness polynomial and sampler are as specified.

This proposition is not yet \(\mathrm{DEC}(q)\in\mathrm{RP}\). To obtain that conclusion, one must prove that all possible observer candidates can be covered by a polynomial number of such parameter spaces, with polynomial-time samplers and reconstruction procedures. The present report does not do so.

I would explicitly label this as a conditional per-chart result rather than an RP classification of the full decision problem.

9. Revised status of the project
The new report contains one good mathematical direction, one correct linear-algebraic identity, and several claims that need revision before they can support a complexity conclusion.
Claim	Current status	Required action
Bounded-degree Bézout representation	Valid	Retain; state hypotheses and proof
\(2\omega-1\) coefficient equations	Incorrect	Replace by \(2\omega\)
Rank comparison characterises inconsistency	Valid	Retain exactly
All maximal minors of augmented matrix vanish characterises badness	Incorrect	Replace by rank-stratified conditions
Degree bound \(2\omega(2\omega-1)\)	Incorrect as derived	Use \(2\omega^2\) in \(R\), or \(4\omega^2\) in \((U,V,Z)\)
Factorisation \(H=UV^{\mathsf T}\)	Valid	Add \(H_A=ZV^{\mathsf T}\)
Random factor sampling for unrestricted pairs	Conditional	State \(r=0\) or prove a fixed-block sampler
Random factor sampling for general observer data	Not established	Respect fixed rows and component structure
Per-chart one-sided sampling	Conditional	Specify sampler, degree witness, and bit model
\(\mathrm{DEC}(q)\in\mathrm{RP}\)	Not proved	Do not claim yet
NP-hardness implies \(\mathrm{NP}=\mathrm{RP}\)	Correct conditionally	Apply only after RP membership is established

10. My recommended next research task
I would make the next report narrowly focused on the following four items, in this order:
1. Correct the Bézout system: write the \(2\omega\)-row coefficient matrix explicitly, prove the exact rank-consistency identity, and derive the corrected degree bounds.
2. Establish the factor-space sampler: first in the unrestricted \(r=0\) case, using
   \[
   H=UV^{\mathsf T},\qquad H_A=ZV^{\mathsf T}.
   \]
   Prove that the factor parameterisation is dominant and that the pullback of a proper bad locus remains proper.
3. Analyse the fixed-row case: determine whether the affine constraints from \(L_0\) admit a similarly efficient parameterisation. Do not assume that the unrestricted realizability lemma solves this.
4. Decide whether the full observer problem admits a polynomial cover: only after this should the RP claim be reconsidered.
The unrestricted \(r=0\) case is a particularly good test bed. It isolates the algebraic sampling idea from the fixed-row obstruction and can show whether the degree-based argument is sound in its most favourable setting. But be aware that it may also be degenerate for the original observer problem: if \(L_0\) is absent and \(R=0\) is allowed, the zero augmentation can itself make the spectral condition automatic. A useful nontrivial special case should therefore preserve whatever nonzero or fixed-output constraints are essential to the intended problem.

Bottom line: the report has not proved \(\mathrm{DEC}(q)\in\mathrm{RP}\), but it has identified a promising route to a conditional one-sided algorithm on irreducible rank strata. The immediate mathematical correction is the \(2\omega\)-equation Bézout system. The immediate structural obstacle is constructing a sampler that respects the fixed observer rows and covers all feasible rank strata. I would resolve those two issues before drawing any conclusion about NP-hardness or \(q_{\min}\).