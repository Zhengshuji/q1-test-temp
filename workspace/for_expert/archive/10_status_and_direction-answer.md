# Review of `10_status_and_direction.md`

This is a significant improvement. The unconditional identity in II.2 removes the earlier ambiguity around \\(V'\\), the B.7 correction addresses the genuine flaw in the previous proof, and the report is much clearer about which conclusions are universal and which are empirical.

My main recommendation is to make the spectral structure the next mathematical target, but not to start with a hardness reduction. There is a particularly useful reduction hiding in B.10: the spectral condition can be expressed as an ordinary observability test for a \\(q\\)-dimensional pair. If the derivation below checks out against your exact definitions, it gives a much more direct route to Q4 and Q5 than subresultant enumeration.

## 1. II.2 — the unconditional counting identity

Correct

The identity

\\[ \boxed{h=s_0+q-\dim(R\cap S)} \\]

is correct under the stated assumptions.

Indeed, since

\\[ \mathcal Z^\perp=C\oplus R,\qquad \operatorname{row}L_0\subseteq R, \\]

we have

\\[ \mathcal Z^\perp+S=\mathcal Z^\perp+W. \\]

Therefore

\\[ h=\dim(\mathcal Z^\perp+S) =(p+q)+s_0-\dim(\mathcal Z^\perp\cap S). \\]

Since \\(C\subseteq S\\) and \\(C\cap R=0\\),

\\[ (C\oplus R)\cap S=C\oplus(R\cap S), \\]

so

\\[ \dim(\mathcal Z^\perp\cap S)=p+\dim(R\cap S). \\]

Substitution proves the formula.

The listed consequences also follow:

- \\(\dim(R\cap S)\ge r\\), hence \\(h\le s_0+q-r\\).
- \\(s_0\le r_1+r\\), because \\(S\\) is the sum of a \\((p+r)\\)-dimensional space and an \\(r_1\\)-dimensional space whose intersection contains \\(C\\), of dimension \\(p\\).
- Type I requires \\(s_0=r_1+r\\) and \\(\dim(R\cap S)=r\\).
- Since \\(L_0\subseteq R\cap S\\), the last equality is equivalent to \\(R\cap S=\operatorname{row}L_0\\).

The geometric equivalence

\\[ \text{Type I}\iff R\cap W=\\{0\\} \\]

is also correct: \\(C\subseteq W\\), \\(R\cap C=0\\), and quotienting by \\(C\\) identifies the relevant intersection with \\(\pi R\cap\pi W\\).

Paper-writing suggestion: make the distinction between these two conclusions explicit:

1. \\(s_0\<r_1+r\\) rules out Type I for every augmentation at that order.
2. \\(s_0=r_1+r\\) does not guarantee Type I; it says Type I is possible only if the chosen \\(R\\) also satisfies \\(R\cap S=\operatorname{row}L_0\\).

That distinction will prevent the arithmetic condition from being overstated.

## 2. II.3 — the revised Kronecker chain

The revisions are directionally right.

- B.6: the coefficient induction is sound, as discussed in the previous review.
- B.7: the reversed-pencil determinantal-divisor argument is the right repair. Its essential point is that every \\(h\\)-minor has valuation at least \\(h-q\\), and one such minor has exactly that valuation.
- B.8: the block-by-block derivation of the rectangular-pencil index identity is appropriate. Ensure the cited Kronecker-form references use the same convention for the degrees of finite and infinite elementary divisors.
- B.9: the reduced-minimal-basis bridge resolves the earlier missing justification.
- B.10: the factorization and spectral confinement are correct.

I have one technical qualification about B.10b. The properness argument is promising, but the claim that \\(\Lambda\\) can be chosen rationally on the entire stated stratum needs a little more precision. Cramer's rule gives a rational solution wherever a particular pivot minor is nonzero. A single pivot need not remain nonzero on the entire stratum. The safe formulation is:

> Refine the chart/stratum into finitely many pivot subcharts on each of which a specified nonzero minor is used to choose \\(\Lambda\\) rationally.

Then homogenize the characteristic polynomial and the rank-drop equations. The characteristic equation excludes the point at infinity, and the rank-drop conditions are closed. Projection from the product with \\(\mathbb P^1\\) is closed. This proves that the failure locus is closed on each refined subchart.

Thus I agree with the intended conclusion, but I would state it on pivot subcharts, unless you have a global regular choice of \\(\Lambda\\).

## 3. A useful reduction for Q5: the spectral test is an observability test

This is the most important additional direction I see in the report.

Assume (5a), and choose matrices \\(\Lambda,G_0,G_1\\) such that

\\[ \mathcal LA=\Lambda\mathcal L+G_0C+G_1CA. \\]

Put

\\[ H=\begin{pmatrix}\mathcal L\\\CA\\\C\end{pmatrix},\qquad D(\lambda)= \begin{pmatrix} \lambda I-\Lambda&-G_1&-G_0\\\ 0&I&0\\\ 0&0&I \end{pmatrix}. \\]

Then \\(Q\_{\mathcal L}(\lambda)=D(\lambda)H\\).

For any two linear maps \\(D,H\\), with \\(D\\) square on the codomain of \\(H\\),

\\[ \operatorname{rank}(DH)=\operatorname{rank}H \iff \ker D\cap\operatorname{im}H=\\{0\\}. \\]

Here

\\[ \ker D(\lambda) =\left\\{\begin{pmatrix}u\\\0\\\0\end{pmatrix}: (\lambda I-\Lambda)u=0\right\\}. \\]

On the other hand,

\\[ \operatorname{im}H =\left\\{\begin{pmatrix}\mathcal Lx\\\CAx\\\Cx\end{pmatrix}:x\in\mathbb C^n\right\\}. \\]

Consequently,

\\[ \operatorname{rank}Q\_{\mathcal L}(\lambda)\<h \\]

if and only if there is an \\(x\in\ker[C;CA]\\) such that

\\[ \mathcal Lx\ne0,\qquad \Lambda\mathcal Lx=\lambda\mathcal Lx. \\]

Define

\\[ V:=\ker[C;CA],\qquad U:=\mathcal L(V)\subseteq\mathbb C^q. \\]

We obtain the exact equivalence

\\[ \boxed{ (5b)\iff U\text{ contains no nonzero eigenvector of }\Lambda. } \\]

Now choose a matrix \\(P\\) with

\\[ \ker P=U. \\]

The Popov–Belevitch–Hautus observability criterion says that \\((P,\Lambda)\\) is observable precisely when

\\[ \operatorname{rank} \begin{pmatrix} \lambda I-\Lambda\\\P \end{pmatrix}=q \quad\text{for every }\lambda\in\mathbb C. \\]

That is exactly the condition that \\(\ker P=U\\) contain no eigenvector of \\(\Lambda\\). Hence

\\[ \boxed{ (5b)\iff (P,\Lambda)\text{ is observable} \iff \operatorname{rank} \begin{pmatrix} P\\\P\Lambda\\\\\vdots\\\P\Lambda^{q-1} \end{pmatrix}=q. } \\]

This is a finite-dimensional rank test. It replaces a condition quantified over every complex \\(\lambda\\) by one ordinary observability-matrix calculation.

Why this matters for your project

1. For a fixed candidate \\(\mathcal L\\), the spectral test can be performed without computing all maximal minors of the nullspace pencil.
2. It uses a \\(q\\)-dimensional matrix \\(\Lambda\\), which is often much smaller than the original \\(n\\)-dimensional pencil.
3. It gives a direct route to an algebraic certificate: full column rank of the observability matrix can be certified by a left inverse.
4. It may give a more compact global \\(\exists\mathbb R\\) encoding than a Bézout identity involving every maximal minor.

There are two implementation details to settle before claiming a polynomial-size global encoding. First, construct \\(P\\) with \\(\ker P=\mathcal L(V)\\) uniformly across the parameter family; this will generally require stratifying by \\(s=\dim\mathcal L(V)\\), or equivalently by \\(\dim(\ker\mathcal L\cap V)\\). Second, make sure the \\(\Lambda\\) variables are included together with the linear equations expressing the factorization. The choice of a factorization is existential, but any valid choice gives the same truth value for (5b), by the equivalence just proved.

This reduction is worth testing immediately against your existing Toeplitz, gcd, and nullspace-pencil implementations. It should agree on every fixed candidate, including the rank-drop cases.

## 4. Q1 — which direction should be attacked first?

My choice is (b), with a structural investigation from (c) running alongside it. I would defer (a).

I would slightly revise the objective, though:

> First obtain a complete, compact algebraic characterization and decision certificate for the spectral condition. Then investigate whether that characterization admits a polynomial-time algorithm.

The distinction matters. A polynomial-size existential formula proves membership in \\(\exists\mathbb R\\), not a polynomial-time algorithm.

The reason to prioritize this direction is the observability reduction above. It suggests that the spectral condition is not intrinsically an exponentially large maximal-minor problem. It may be a much smaller finite-rank condition with a natural certificate.

The structural question in Q2 is also worth investigating, but I would not make the entire project depend on proving the boundary phenomenon. It could turn out to be a useful special-case theorem rather than a complete classification.

## 5. Q2 — is \\(r_1=p+r\\) the only possible surjective boundary?

The four observed cases are interesting evidence, but they do not establish the proposed theorem. There is a basic dimension issue to resolve first.

Suppose the incidence construction really gives a map

\\[ \Phi:\mathbb P(V)\dashrightarrow\mathbb P(K), \qquad V=\ker[C;CA],\quad K=\ker[C;L_0]. \\]

The dimensions are

\\[ \dim\mathbb P(V)=n-r_1-1,\qquad \dim\mathbb P(K)=n-p-r-1. \\]

If this map is dominant, and hence can be surjective after the appropriate extension, a necessary dimension condition is

\\[ n-r_1-1\ge n-p-r-1, \\]

or

\\[ \boxed{r_1\le p+r.} \\]

This condition does not force equality. If \\(r_1\<p+r\\), the source has larger dimension than the target, and a surjective map is perfectly possible in general. Equality is the equal-dimension, potentially generically finite case; it is not the only dimensionally possible surjective case.

There is another complication: for \\(r>1\\), the scalar \\(\lambda(x)\\) used in the construction is not generally defined for every \\(x\in V\\). The proportionality condition

\\[ L_0Ax\in\operatorname{span}\\{L_0x\\} \\]

imposes additional equations on \\(x\\). The actual incidence domain can therefore have smaller dimension than \\(\mathbb P(V)\\).

I would formulate the general problem using the incidence variety

\\[ \mathscr I= \left\\{ ([x],[z],\lambda): x\in V,\ z\in K,\  (\lambda I-A)x\in\operatorname{span}(z) \right\\}, \\]

with the appropriate nonzero conditions. Then study the projection

\\[ \mathscr I\longrightarrow\mathbb P(K). \\]

Surjectivity is a dominance/projection question for this incidence variety, not merely a comparison of the dimensions of \\(\mathbb P(V)\\) and \\(\mathbb P(K)\\).

My recommendation: investigate \\(r_1=p+r\\) as a candidate equal-dimension boundary, not as an established necessary condition for Type III. The first theorem to seek is a dimension bound on the actual incidence domain. If its dimension is at most \\(\dim\mathbb P(K)\\), equality becomes a necessary condition for dominance. That missing bound is the real mathematical question.

## 6. Q3 — \\(\exists\mathbb R\\)-hardness or NP-hardness?

If you pursue hardness, \\(\exists\mathbb R\\)-hardness is the more informative target.

The report claims a polynomial-size \\(\exists\mathbb R\\) encoding. If that encoding is correct, then \\(\exists\mathbb R\\)-completeness would give a natural classification. NP-hardness would be a weaker result. Recall that \\(\mathrm{NP}\subseteq\exists\mathbb R\\). The \\(\exists\mathbb R\\) class is specifically designed for existential polynomial feasibility over the reals.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

ScienceDirect+1



Two candidate source problems are worth considering:

1. Quadratic feasibility / ETR-AMI. This is the most direct way to encode arithmetic variables and multiplication constraints. It is a good choice if the augmentation parameters and the factorization equations can simulate a small arithmetic circuit.
2. Minimum matrix rank or affine rank minimization. These are closer to your algebraic formulation. The \\(\exists\mathbb R\\) compendium records minimum/maximum matrix rank as \\(\exists\mathbb R\\)-complete.&#x20;

   [image](https://www.google.com/s2/favicons?domain=https://www.researchgate.net\&sz=32)

   ResearchGate+1



I would begin with quadratic feasibility, not because it is necessarily easier, but because it makes the reduction's logical requirements transparent. You need to encode variables, addition, and multiplication while preserving all the structural restrictions:

- fixed \\(A,C,L_0\\) or an allowed construction of them;
- the prescribed row-space containment;
- full row rank of \\([C;\mathcal L]\\);
- (5a);
- the spectral condition.

A reduction that only encodes arbitrary matrix rank constraints is not enough. The hard part will be making those constraints arise from this particular observer structure.

One further point: your problem is formulated over \\(\mathbb C\\), whereas \\(\exists\mathbb R\\)-completeness is normally defined using real variables. This is not an automatic obstacle: split each complex variable into real and imaginary parts and replace complex polynomial equalities by their real and imaginary equations. But the reduction must preserve the intended field and all nonzero/rank constraints.

## 7. Q4 — should you invest in subresultants?

Not as the first priority. The observability reduction offers a more direct way to handle rank-drop cases.

Let \\(V_0\\) be a fixed basis matrix for \\(V=\ker[C;CA]\\), and put

\\[ M=\mathcal L V_0,\qquad U=\operatorname{im}M. \\]

For a candidate of fixed order \\(q\\), let \\(s=\operatorname{rank}M\\). Choose

\\[ E\in\mathbb C^{(q-s)\times q} \\]

such that

\\[ \ker E=U. \\]

Then the spectral condition is equivalent to

\\[ \operatorname{rank} \begin{pmatrix} E\\\E\Lambda\\\ \vdots\\\E\Lambda^{q-1} \end{pmatrix}=q. \\]

This gives a direct finite certificate. For example, the condition can be encoded algebraically by existentially requiring:

\\[ EM=0,\qquad \operatorname{rank}M=s,\qquad \operatorname{rank}E=q-s, \\]

and

\\[ \exists Y:\quad Y \begin{pmatrix} E\\\E\Lambda\\\ \vdots\\\E\Lambda^{q-1} \end{pmatrix}=I_q. \\]

The first three conditions ensure \\(\ker E=\operatorname{im}M\\); the final condition certifies full column rank of the observability matrix.

The exact rank conditions can themselves be encoded using factorization witnesses and left/right inverses. For instance, rank \\(M=s\\) can be certified by a factorization \\(M=AB\\), with \\(A\\) full column rank and \\(B\\) full row rank. Full row rank of \\(E\\) can be certified by a right inverse.

There are only \\(q+1\\) possible values of \\(s\\), so a disjunction over these strata is polynomial in \\(q\\). This seems to be a particularly promising way to make the rank-drop cases complete without enumerating the maximal minors of the original pencil.

What I would do next:

1. Implement this test for individual rational candidates.
2. Compare it against all existing exact gcd, Toeplitz, and nullspace-pencil tests.
3. Test the exceptional rank-drop examples explicitly.
4. Only then formulate the global \\(\exists\mathbb R\\) encoding using the \\(s\\)-stratification.

Subresultants remain useful for the existing gcd-based implementation and as an independent certificate. They are not necessarily the best foundation for the complete method.

## 8. Q5 — can the special pencil shape lead to a polynomial algorithm?

I think this is now the most promising technical question, and the observability reduction gives a stronger answer than merely restricting \\(\lambda\\) to the roots of a degree-\\(q\\) polynomial.

For a fixed candidate, you do not need to compute the eigenvalues of \\(\Lambda\\) at all. You can test observability using

\\[ \mathcal O(P,\Lambda)= \begin{pmatrix} P\\\P\Lambda\\\\\vdots\\\P\Lambda^{q-1} \end{pmatrix}. \\]

This is an ordinary matrix rank computation.

Thus, for a fixed candidate, the spectral test is polynomial-time in the arithmetic-operation model: form the factorization coefficients, compute a basis for \\(U=\mathcal L(V)\\), construct an annihilator \\(P\\), and test the rank of \\(\mathcal O(P,\Lambda)\\).

This also provides an independent check of the Noferini–Van Dooren route in II.7. Their Lemma 5.2 states that a matrix pencil with \\(m\\) rows is right-invertible over \\(\mathbb C[\lambda]\\) precisely when it has no finite eigenvalues and no left minimal indices, and that a polynomial right inverse can be chosen with degree at most \\(m-1\\).&#x20;

[image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

ScienceDirect+1



That supports the stated degree bound provided the matrix to which you apply the lemma has exactly \\(t\\) rows and normal row rank \\(t\\). The dimensions and the absence of left minimal indices should be made explicit in the paper.

My preferred order is:

- First implement the observability-matrix test.
- Then compare it with the polynomial right-inverse certificate.
- Finally see whether the latter gives a more convenient global algebraic encoding.

The fixed-candidate polynomial-time result does not automatically imply a polynomial-time algorithm for choosing \\(\mathcal L\\). The latter is still a parameter-dependent feasibility problem. But it removes the need to treat the spectral condition as an infinite-\\(\lambda\\) test.

## 9. Q6 — write the paper now or continue pursuing Type III?

My recommendation is write the two established results now, while keeping a focused Type III workstream active.

The paper's central narrative can be:

1. The counting obstruction has an exact geometric and arithmetic characterization.
2. The apparent three-way classification reduces to two cases.
3. The spectral obstruction is genuinely different from the counting obstruction.
4. A whole-family counterexample demonstrates that the spectral obstruction can persist for every algebraically admissible augmentation at the minimum algebraic order.

This is a coherent mathematical contribution. It does not need a completed complexity classification to be worthwhile.

There is one important detail to settle before claiming \\(q\_{\min}=4\\) in the counterexample: the report establishes that every admissible augmentation at \\(q_0=3\\) fails (5b), but it does not display the order-four witness. Include either:

- an explicit \\(q=4\\) augmentation and its exact seven checks; or
- a clearly stated theorem giving the upper bound \\(q\_{\min}\le4\\), with its hypotheses verified for this instance.

Without one of these, the reported whole-family infeasibility at \\(q_0\\) proves \\(q\_{\min}>3\\), not by itself \\(q\_{\min}=4\\).

I would put the certificate-based decision procedure in an appendix or supplementary material. Its coverage figures and `UNKNOWN` outcomes are valuable, but they should not distract from the mathematical theorems.

## 10. Concrete next steps

Suggested next work package

1. Prove and implement the observability reduction.

   Test it against every existing exact spectral certificate, especially rank-drop cases.
2. Build the compact rank-stratified encoding.

   Use \\(s=\operatorname{rank}(\mathcal L V_0)\\), an annihilator \\(E\\), and an observability-matrix left inverse.
3. Finish the counterexample paper.

   Include the order-four feasibility certificate and keep the geometric surjectivity argument explicitly conditional.
4. Investigate the \\(r_1=p+r\\) phenomenon.

   Formulate the actual incidence variety and derive a dimension bound before proposing a boundary theorem.
5. Defer hardness reductions.

   Revisit \\(\exists\mathbb R\\)-hardness after the structural spectral characterization and compact encoding are settled.

Overall judgment: the project has reached a point where a focused paper is justified. More importantly, the observability reduction suggests that the spectral part may have a simpler algebraic structure than the maximal-minor computations have so far revealed. I would make that the next central mathematical result, rather than immediately expanding the computational machinery or beginning a hardness reduction.