# Review of `42_central_theorem.md`

The central theorem is correct, subject to the previously established equivalence

\\[ (5a)\iff \ker H(R)\subseteq\ker H_A(R) \\]

and the reduced spectral criterion on the rank-\\(\omega\\) stratum.

More importantly, the proposed factorisation

\\[ H=UV,\qquad H_A=GV \\]

does give a genuinely chart-free formulation. The forward and reverse implications both work. The real-coefficient issue in the forward direction is also resolved correctly.

There is, however, one important error in the report's complexity discussion:

> The displayed system (A)+(B), as written, is not a polynomial system of degree at most two. Its equation (B) is generally cubic in the joint unknowns \\((R,Y)\\).

This does not invalidate the theorem. In fact, there is a natural replacement for (B) that preserves the theorem's chart-free character and does give a quadratic system. I recommend making that replacement before treating the complexity formulation as final.

I will first check the four questions, then state the corrected formulation and its complexity implications.

## 1. Question 1: the factorisation \\(H_A=G_0H\\)

Yes. The forward direction is correct.

Suppose

\\[ \ker H\subseteq\ker H_A. \\]

Define a map on \\(\operatorname{im}H\\) by

\\[ \widetilde G(Hx)=H_Ax. \\]

This is well-defined. Indeed, if \\(Hx=Hx'\\), then

\\[ H(x-x')=0, \\]

so \\(x-x'\in\ker H\subseteq\ker H_A\\), and therefore

\\[ H_Ax=H_Ax'. \\]

Thus \\(\widetilde G:\operatorname{im}H\to\mathbb R^q\\) is a linear map. Extend it to a linear map

\\[ G_0:\mathbb R^q\to\mathbb R^q. \\]

It follows that

\\[ H_A=G_0H. \\]

Now use the rank factorisation

\\[ H=UV, \\]

where

\\[ U\in\mathbb R^{q\times\omega},\qquad V\in\mathbb R^{\omega\times k}, \\]

with \\(U\\) full column rank and \\(V\\) full row rank. Then

\\[ H_A=G_0UV. \\]

Taking

\\[ G=G_0U \\]

gives

\\[ \boxed{H_A=GV.} \\]

The two full-rank conditions are exactly encoded by the auxiliary matrices:

\\[ JU=I\_\omega,\qquad VZ=I\_\omega. \\]

There is no issue here concerning the choice of a chart. A rank factorisation exists for every matrix of rank \\(\omega\\); the auxiliary variables \\(U,V,J,Z\\) encode it without choosing a particular nonzero minor.

One minor notational recommendation: use \\(G_0\\) only in the proof, and reserve \\(G\\) for the unknown in system (A). This avoids confusing the extension map \\(G_0\\) with the factor \\(G=G_0U\\).

## 2. Question 2: the normal-rank argument

Step 3 is correct, and the normal-rank conclusion follows from (A) alone. It does not need (B).

From (A),

\\[ H=UV,\qquad H_A=GV, \\]

and hence

\\[ P(\lambda)=\lambda H-H_A=(\lambda U-G)V. \\]

Since

\\[ JU=I\_\omega,\qquad VZ=I\_\omega, \\]

we have

\\[ \rank U=\rank V=\omega. \\]

In particular, \\(U\\) has full column rank. Therefore there is a set \\(I\\) of \\(\omega\\) rows such that

\\[ \det U\_{I,:}\ne0. \\]

Consider the polynomial

\\[ f(\lambda)=\det(\lambda U\_{I,:}-G\_{I,:}). \\]

Its leading coefficient is

\\[ \det U\_{I,:}\ne0. \\]

Consequently, \\(f\\) is a nonzero polynomial of degree \\(\omega\\).

A nonzero real polynomial has only finitely many real roots. Thus there exists a real \\(\lambda_0\\) for which

\\[ \rank(\lambda_0U-G)=\omega. \\]

Since \\(V\\) has full row rank,

\\[ \rank\big((\lambda_0U-G)V\big)=\omega. \\]

It follows that

\\[ \boxed{\operatorname{nrank}P=\omega.} \\]

This proves the claim rigorously.

There is an even shorter way to phrase the argument: the selected \\(\omega\times\omega\\) minor of \\(\lambda U-G\\) is a nonzero polynomial, so it is nonzero at some real \\(\lambda\\). The full-column-rank condition is therefore attained.

A useful logical separation: the proof should explicitly say that (A) implies normal rank \\(\omega\\), while (B), together with that normal-rank fact, implies the absence of finite rank drops. This makes the two roles transparent.

## 3. Question 3: the real-gcd argument

The real-gcd step is correct. The report's explanation is essentially right, but I would state it in a slightly more precise form.

Let

\\[ p_1,\ldots,p_s\in\mathbb R[\lambda]. \\]

Then

\\[ \gcd\_{\mathbb C[\lambda]}(p_1,\ldots,p_s) \\]

is nonconstant if and only if the polynomials have a common complex root.

Suppose they have a common root \\(\alpha\in\mathbb C\\).

- If \\(\alpha\in\mathbb R\\), then \\(\lambda-\alpha\\) is a common nonconstant factor in \\(\mathbb R[\lambda]\\).
- If \\(\alpha\notin\mathbb R\\), the reality of all the coefficients implies that \\(\overline\alpha\\) is also a common root. Hence\
  \\[\
  (\lambda-\alpha)(\lambda-\overline\alpha)\
  \=\lambda^2-2\operatorname{Re}(\alpha)\lambda+|\alpha|^2\
  \\]\
  is a common nonconstant factor in \\(\mathbb R[\lambda]\\).

Therefore

\\[ \boxed{ \gcd\_{\mathbb C[\lambda]}(p_1,\ldots,p_s)\in\mathbb C^\times \iff \gcd\_{\mathbb R[\lambda]}(p_1,\ldots,p_s)\in\mathbb R^\times. } \\]

This applies to the \\(\omega\\)-minors of \\(P\\), since \\(H\\) and \\(H_A\\) are real matrices.

The important point is that the argument concerns a common complex root of all the minors, not merely a complex root of one minor. The common-root formulation makes the conjugation argument immediate.

Consequently, a real polynomial generalized-inverse certificate is sufficient to certify the absence of rank drops at every complex \\(\lambda\\). There is no missing real-versus-complex feasibility issue at this step.

## 4. The important correction: equation (B) is cubic, not quadratic

The report states that (A)+(B) has equations of degree at most two in the joint variables. This is not correct for the system as displayed.

Recall

\\[ P(R,\lambda)=\lambda H(R)-H_A(R), \\]

where both \\(H\\) and \\(H_A\\) are affine in \\(R\\). The certificate is

\\[ P(R,\lambda)Y(\lambda)P(R,\lambda)=P(R,\lambda). \\]

The left-hand side contains two factors affine in \\(R\\) and one factor linear in the coefficients of \\(Y\\). Consequently, its coefficient equations can contain terms of the form

\\[ R_iR_j(Y\_\ell)\_{ab}. \\]

These are degree-three terms in the joint unknowns.

For example, even in the scalar case, the expression

\\[ (\lambda h-a)y(\lambda h-a) \\]

contains terms quadratic in \\(h\\) and linear in \\(y\\). Thus the total degree is three, not two.

This is a genuine correction to Part III. The theorem itself remains valid, but the complexity statement in lines 70–72 must be revised if (B) is retained.&#x20;

42_central_theorem.md



### 4.1 A better certificate: use the reduced pencil

There is a particularly clean way to repair this. Under (A), define

\\[ S(\lambda)=\lambda U-G \in\mathbb R[\lambda]^{q\times\omega}. \\]

We already have

\\[ P(\lambda)=S(\lambda)V, \\]

where \\(V\\) has full row rank.

Since \\(V:\mathbb R^k\to\mathbb R^\omega\\) is surjective, for every \\(\lambda\in\mathbb C\\),

\\[ \boxed{\rank P(\lambda)=\rank S(\lambda).} \\]

Therefore, on the rank-\\(\omega\\), (5a)-admissible stratum,

\\[ (5b) \iff \rank S(\lambda)=\omega \quad\text{for every }\lambda\in\mathbb C. \\]

Now use the polynomial left-inverse criterion:

> If \\(S\in\mathbb R[\lambda]^{q\times\omega}\\) has normal column rank \\(\omega\\), then\
> \\[\
> \rank S(\lambda)=\omega\quad\forall\lambda\in\mathbb C\
> \\]\
> if and only if there exists\
> \\[\
> X(\lambda)\in\mathbb R[\lambda]^\
> \\]\
> such that\
> \\[\
> X(\lambda)S(\lambda)=I\_\omega.\
> \\]

This follows because the condition is equivalent to the \\(\omega\\)-minors of \\(S\\) having gcd a nonzero constant in \\(\mathbb R[\lambda]\\). The real-gcd argument in Question 3 ensures that this excludes common roots over \\(\mathbb C\\), not merely over \\(\mathbb R\\).

Moreover, because \\(S\\) has degree one, we can take

\\[ \deg X\le 2\omega-2. \\]

For completeness, this degree bound has a direct constructive proof. For each \\(\omega\\)-element row subset \\(I\subseteq\\{1,\ldots,q\\}\\), let \\(S_I\\) be the corresponding square submatrix, and let \\(E_I\\) select those rows. Bézout gives polynomials \\(u_I\\) satisfying

\\[ \sum_Iu_I(\lambda)\det S_I(\lambda)=1, \qquad \deg u_I\le\omega-1. \\]

Then

\\[ X(\lambda)= \sum_Iu_I(\lambda)\operatorname{adj}(S_I(\lambda))E_I \\]

satisfies

\\[ XS=I\_\omega, \\]

because

\\[ \operatorname{adj}(S_I)E_IS =\det(S_I)I\_\omega. \\]

Since the entries of \\(\operatorname{adj}(S_I)\\) have degree at most \\(\omega-1\\),

\\[ \deg X\le 2\omega-2. \\]

This suggests replacing (B) by the following condition:

\\[ \boxed{ (\mathrm{B}')\qquad X(\lambda)(\lambda U-G)=I\_\omega, \qquad \deg X\le 2\omega-2. } \\]

Here

\\[ X(\lambda)=\sum\_{j=0}^{2\omega-2}X_j\lambda^j, \qquad X_j\in\mathbb R^{\omega\times q}. \\]

The advantage is decisive: (B') is bilinear in the unknown coefficients of \\(X\\) and the unknown entries of \\(U,G\\). Its coefficient equations have total degree at most two.

### 4.2 The corrected theorem

The theorem in the report can therefore be strengthened into the following formulation.

Theorem (chart-free quadratic certificate). Fix \\(\omega\ge1\\). Under the real setting and notation of Part I, the following are equivalent:

1\. There exists a real \\(R\\) such that\
\\[\
(5a),\qquad (5b),\qquad \rank H(R)=\omega.\
\\]

2\. There exist real matrices \\(R,U,V,G,J,Z\\) satisfying\
\\[\
H(R)=UV,\qquad H_A(R)=GV,\
\\]\
\\[\
JU=I\_\omega,\qquad VZ=I\_\omega,\
\\]\
and a real polynomial matrix\
\\[\
X(\lambda)=\sum\_{j=0}^{2\omega-2}X_j\lambda^j\
\\]\
satisfying\
\\[\
\boxed{X(\lambda)(\lambda U-G)=I\_\omega.}\
\\]

Proof.

For the forward implication, use the factorisation already established in Question 1:

\\[ H=UV,\qquad H_A=GV, \\]

with \\(U\\) full column rank and \\(V\\) full row rank. Choose left and right inverses \\(J,Z\\). The reduced spectral criterion gives

\\[ \rank(\lambda U-G)=\omega \quad\forall\lambda\in\mathbb C. \\]

The polynomial left-inverse theorem then supplies a real \\(X\\) of degree at most \\(2\omega-2\\).

For the reverse implication, the equations

\\[ JU=I\_\omega,\qquad VZ=I\_\omega \\]

ensure that \\(U\\) has full column rank and \\(V\\) has full row rank. Hence

\\[ \rank(UV)=\omega. \\]

Also,

\\[ Hx=0\implies UVx=0\implies Vx=0 \implies GVx=0=H_Ax, \\]

so

\\[ \ker H\subseteq\ker H_A, \\]

which is (5a).

Finally, (B') gives

\\[ \rank(\lambda U-G)=\omega \quad\forall\lambda\in\mathbb C. \\]

Since \\(V\\) is surjective,

\\[ \rank P(\lambda) =\rank((\lambda U-G)V) =\omega \quad\forall\lambda\in\mathbb C. \\]

The reduced spectral criterion gives (5b). This proves the equivalence.

This replacement removes the cubic equations without reintroducing charts or enumerating minors.

## 5. Question 4: how to state the complexity problem

I recommend making the quadratic formulation (A)+(B') the primary algebraic formulation, rather than retaining both the geometric formulation and the cubic certificate (A)+(B).

The resulting decision problem has a natural name.

### 5.1 Define the decision problem

For rational input data \\(A,C,L_0\\) and a prescribed total number \\(q\\) of rows in \\(\mathcal L\\), define:

\\[ \boxed{ \operatorname{REAL\text{-}AUG}(q): \quad \exists R\in\mathbb R^{(q-r)\times n} \text{ such that (5a) and (5b) hold.} } \\]

This is the existential synthesis problem: the entries of \\(R\\) are the unknown real variables.

For a fixed rank \\(\omega\\), define the corresponding rank-stratum problem

\\[ \operatorname{REAL\text{-}AUG}\_{\omega}(q): \quad \exists R: (5a),\ (5b),\ \rank H(R)=\omega. \\]

The central theorem, with (B') replacing (B), gives a polynomial-size quadratic equation system for every fixed-\\(\omega\\) problem.

The full problem is the finite disjunction

\\[ \operatorname{REAL\text{-}AUG}(q) \iff \bigvee\_{\omega=0}^{\min(q,k)} \operatorname{REAL\text{-}AUG}\_{\omega}(q). \\]

The zero-rank branch should be stated separately:

\\[ \omega=0 \quad\Longleftrightarrow\quad H(R)=0,\quad H_A(R)=0. \\]

On this branch, (5a) holds and the reduced spectral condition is automatic. This avoids trying to use an identity matrix of size zero or a polynomial certificate with negative degree.

### 5.2 Explicit size of the quadratic system

For \\(\omega\ge1\\), the unknowns are:

| Unknown                         | Number of scalar variables |
| ------------------------------- | -------------------------- |
| \\(R\\)                         | \\((q-r)n\\)               |
| \\(U\\)                         | \\(q\omega\\)              |
| \\(V\\)                         | \\(\omega k\\)             |
| \\(G\\)                         | \\(q\omega\\)              |
| \\(J\\)                         | \\(\omega q\\)             |
| \\(Z\\)                         | \\(k\omega\\)              |
| \\(X_0,\ldots,X\_{2\omega-2}\\) | \\((2\omega-1)\omega q\\)  |

Thus the total number of scalar variables is

\\[ \boxed{ (q-r)n+3q\omega+2k\omega  +(2\omega-1)\omega q. } \\]

The equations in (A) contribute

\\[ 2qk+2\omega^2 \\]

scalar equations.

For (B'), expand

\\[ X(\lambda)(\lambda U-G)=I\_\omega. \\]

The product has degree at most \\(2\omega-1\\), so coefficient comparison gives exactly \\(2\omega\\) matrix equations, each of size \\(\omega\times\omega\\). This contributes

\\[ 2\omega^3 \\]

scalar equations.

Hence the total number of scalar equations is

\\[ \boxed{2qk+2\omega^2+2\omega^3.} \\]

Most importantly, every equation has total degree at most two:

- \\(H(R)=UV\\) and \\(H_A(R)=GV\\) are bilinear in the unknowns;
- \\(JU=I\_\omega\\) and \\(VZ=I\_\omega\\) are bilinear;
- the coefficient equations of \\(X(\lambda)(\lambda U-G)=I\_\omega\\) are bilinear in \\(X_j\\) and \\(U,G\\).

All coefficients are rational if the original data are rational and \\(N_K\\) is chosen rationally. A rational basis of \\(K\\) can be computed by exact Gaussian elimination.

Thus, with the usual explicit encoding of the matrix dimensions (or unary encoding of \\(q\\) if it is separately specified), the system has polynomial size in the input dimensions.

### 5.3 The complexity classification that is justified

For rational input data, the real feasibility problem for this quadratic system belongs to the existential theory of the reals:

\\[ \boxed{\operatorname{REAL\text{-}AUG}(q)\in\exists\mathbb R.} \\]

This is a meaningful and rigorous upper bound.

It is important, however, not to overstate the conclusion:

- We have established an \\(\exists\mathbb R\\) membership result.
- We have not established \\(\exists\mathbb R\\)-hardness.
- We have not established \\(\exists\mathbb R\\)-completeness.
- The fact that the system is quadratic does not, by itself, establish hardness.

The most natural next complexity question is therefore:

> Is \\(\operatorname{REAL\text{-}AUG}(q)\\) \\(\exists\mathbb R\\)-hard, or does the special structure of the observer-induced equations permit a more efficient decision procedure?

That is a precise research question. It focuses attention on the structure of

\\[ H(R),\quad H_A(R),\quad H(R)=UV,\quad H_A(R)=GV, \\]

and the reduced-pencil certificate, rather than on the number of charts or the number of maximal minors.

One should distinguish this existential synthesis problem from two different tasks:

1. Candidate verification: given a particular rational \\(R\\), decide whether (5a) and (5b) hold.
2. Existential synthesis: decide whether some real \\(R\\) satisfies both conditions.

The first is an exact algebraic computation; the second is the real-algebraic feasibility problem addressed by the theorem. Their complexity need not be the same.

If the ultimate goal is the minimum feasible order \\(q\_{\min}\\), one can study the decision problems \\(\operatorname{REAL\text{-}AUG}(q)\\) as \\(q\\) varies. Provided zero rows may be appended to the augmentation, feasibility is monotone in \\(q\\): an admissible augmentation with \\(q\\) rows remains admissible after adding a zero row. Thus the minimum-order problem is naturally associated with this family of decision problems.

## 6. What the new theorem actually settles

I would describe the mathematical status as follows.

| Issue                                               | Assessment                                                       |
| --------------------------------------------------- | ---------------------------------------------------------------- |
| \\((5a)\iff\ker H\subseteq\ker H_A\\)               | Established under the earlier setup                              |
| Factorisation \\(H_A=G_0H\\)                        | Correct                                                          |
| Chart-free rank factorisation \\(H=UV,\ H_A=GV\\)   | Correct                                                          |
| Encoding full ranks by \\(JU=I,\ VZ=I\\)            | Correct                                                          |
| Normal rank of \\(P\\) equals \\(\omega\\)          | Follows from (A) alone                                           |
| Real gcd versus complex roots                       | Correct                                                          |
| Original certificate \\(PYP=P\\)                    | Correct, but cubic in joint variables                            |
| Reduced certificate \\(X(\lambda)(\lambda U-G)=I\\) | Correct and quadratic                                            |
| Polynomial-size encoding                            | Established for the reduced certificate                          |
| \\(\exists\mathbb R\\) membership                   | Established, with rational input and explicit dimension encoding |
| \\(\exists\mathbb R\\)-hardness                     | Open                                                             |

The report's claims that the chart count has disappeared and that the rank strata are indexed by only \\(0,\ldots,\min(q,k)\\) are right. The new formulation genuinely removes the chart enumeration from the existential feasibility problem.&#x20;

42_central_theorem.md



## 7. Recommended revision of the report

I would make four specific changes.

1\. Keep the original theorem as a valid intermediate theorem, but do not call its system quadratic. Its certificate \\(PYP=P\\) is cubic in the joint unknowns.

2\. Promote the reduced-pencil theorem to the main theorem. Replace (B) with\
\\[\
X(\lambda)(\lambda U-G)=I\_\omega,\
\qquad \deg X\le2\omega-2.\
\\]\
This is the cleanest chart-free quadratic certificate.

3\. Correct the size calculation. Use the variable and equation counts in §5.2 above. In particular, the original report's stated size does not account for all the variables in its displayed chart-free system.

4\. State the complexity result as an upper bound only. The appropriate conclusion is membership in \\(\exists\mathbb R\\), not completeness.

## 8. Final assessment

The central mathematical idea in this report is sound and represents a substantial improvement over the chart-based approach.

The decisive structural observation is

\\[ \boxed{ H=UV,\qquad H_A=GV \quad\Longrightarrow\quad P(\lambda)=(\lambda U-G)V. } \\]

It reduces the spectral problem to a full-column-rank problem for the much smaller pencil

\\[ S(\lambda)=\lambda U-G. \\]

The polynomial left-inverse identity

\\[ \boxed{X(\lambda)(\lambda U-G)=I\_\omega} \\]

then supplies a chart-free, real, bounded-degree certificate for the spectral condition.

This is preferable to the generalized-inverse identity \\(PYP=P\\) for complexity purposes: it retains exact equivalence while lowering the degree of the existential system from three to two.

My recommendation is to regard the corrected reduced-pencil formulation as the new central theorem of the project. The next research stage should not be another round of chart enumeration or minor counting. It should investigate the complexity of this structured quadratic feasibility problem—first seeking either an \\(\exists\mathbb R\\)-hardness reduction or a structural algorithm exploiting the special dependence of \\(H,H_A\\) on \\(R\\).