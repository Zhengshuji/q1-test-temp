# Reliability audit of the report

The report contains a promising algorithmic idea, but one central structural theorem is not proved as written. There is also a useful correction to the proposed spectral gadget: a very small pencil realizes \\((5b)\iff f\ne0\\), but its maximal-minor gcd is not the scalar \\(f\\). The Gram-certificate route is substantially sound, subject to a coefficient-indexing correction, a separate \\(\omega=0\\) case, and a careful bit-complexity statement.

Here is my assessment, separating what follows from the stated hypotheses from what needs an additional assumption.

## 1. Structural bound \\(\omega\le r\\)

Not established as stated

There are two distinct problems in the proof.

### 1.1 The step \\(H\_{A,0}=MH_0\\) does not follow from (5a)

From (5a), we know

\\[ \operatorname{row}(LA)\subseteq \operatorname{row}[L;CA;C]. \\]

In particular, the fixed rows satisfy

\\[ \operatorname{row}(L_0A)\subseteq \operatorname{row}[L_0;R;CA;C]. \\]

But the report uses the stronger inclusion

\\[ \operatorname{row}(L_0A)\subseteq \operatorname{row}[L_0;CA;C]. \\]

The free rows \\(R\\) cannot simply be removed from the right-hand side.

Indeed, multiplying a representation of \\(L_0A\\) by \\(N\\) gives, in general,

\\[ H\_{A,0}=M_0H_0+M_1Y, \\]

for suitable coefficient matrices \\(M_0,M_1\\), not necessarily \\(H\_{A,0}=MH_0\\).

The distinction matters: the term \\(M_1Y\\) can contribute directions outside \\(\operatorname{row}H_0\\), and the eigenvalue argument in the report relies on having the fixed block equal to \\(MH_0\\).

What would make this step valid? An additional hypothesis such as

\\[ L_0A\in\operatorname{row}[L_0;CA;C]. \tag{A} \\]

Under (A), multiplying by \\(N\\) does give

\\[ H\_{A,0}=MH_0. \\]

But (A) is not a consequence of the stated feasibility conditions for \\(L=[L_0;R]\\).

### 1.2 The intersection case has a separate rank error

Even granting \\(H\_{A,0}=MH_0\\), the second case in the proof is invalid.

Write

\\[ U=\operatorname{row}H_0,\qquad V=\operatorname{row}Y,\qquad a=\dim U,\quad b=\dim V,\quad d=\dim(U\cap V). \\]

Then

\\[ \omega=\dim(U+V)=a+b-d. \\]

The report claims that \\(d>0\\) implies

\\[ \operatorname{rank}H\le \operatorname{rank}Y=b. \\]

That does not follow. The correct general bound is

\\[ \operatorname{rank}H =a+b-d \le a+b-1. \\]

A nonzero intersection reduces the sum of dimensions by at least one; it does not imply \\(U\subseteq V\\).

For example, take

\\[ U=\operatorname{span}(e_1,e_2),\qquad V=\operatorname{span}(e_1,e_3). \\]

Their intersection is nonzero, but

\\[ \dim(U+V)=3>\dim V=2. \\]

### 1.3 What the eigenvalue argument actually proves

Under the additional hypothesis (A), the first case of the report is correct.

If \\(U\cap V=0\\), then

\\[ \omega=a+b. \\]

Choose a complex eigenvalue \\(\lambda\\) of \\(M\\). Since \\(H\_{A,0}=MH_0\\), the fixed block of \\(P(\lambda)\\) is

\\[ \lambda H_0-H\_{A,0}=(\lambda I-M)H_0. \\]

Its rank is at most \\(a-1\\), because \\(\lambda I-M\\) is singular. The free block has rank at most \\(b\\). Therefore

\\[ \operatorname{rank}P(\lambda) \le a-1+b=\omega-1, \\]

contradicting (5b).

So the valid conditional statement is:

> If \\(L_0A\in\operatorname{row}[L_0;CA;C]\\), and if \\(U\cap V=0\\), then (5a) and (5b) cannot both hold when \\(H_0\\) has positive rank.

For \\(d>0\\), the same argument only gives

\\[ \operatorname{rank}P(\lambda)\le a-1+b. \\]

To contradict (5b), we need

\\[ a-1+b< a+b-d, \\]

which is equivalent to \\(d<1\\). Thus it does not settle the nonzero-intersection case.

There is a possible refinement: if the chosen eigenvalue has geometric multiplicity \\(g\\), then

\\[ \operatorname{rank}((\lambda I-M)H_0)\le a-g, \\]

so the same proof gives

\\[ \operatorname{rank}P(\lambda)\le a-g+b. \\]

This contradicts (5b) if \\(g>d\\). But there is no general reason in the report that guarantees such an eigenvalue.

### 1.4 The absorption conclusion does not follow

The claimed conclusion

\\[ \operatorname{row}H_0\subseteq\operatorname{row}Y \\]

is stronger still. It does not follow from the supplied proof. Even under (A), the proof only rules out \\(U\cap V=0\\); it does not rule out a proper nonzero intersection.

Verdict: the theorem \\(\omega\le r\\), its corollaries, and the claimed absorption property should be downgraded from P. The proof currently establishes only the conditional disjoint-row-space obstruction above. The \\(q=4\\) impossibility conclusion therefore cannot be retained on the basis of this theorem alone.

## 2. Liftability bound and per-row criterion

Correct, with a notation clarification

Let \\(p=\operatorname{rank}C\\). Since

\\[ CN=0,\qquad CAN=0, \\]

every column of both \\(N\\) and \\(AN\\) belongs to \\(\ker C\\). Consequently,

\\[ \operatorname{rank}[N\ AN]\le \dim\ker C=n-p. \\]

This is the right obstruction to surjectivity of the compressed row map.

For a candidate free row \\(r_i\in\mathbb R^{1\times n}\\),

\\[ (r_iN,\ r_iAN)=r_i[N\ AN]. \\]

Thus

\\[ \boxed{ (H_i,H\_{A,i})\text{ is liftable} \iff (H_i,H\_{A,i})\in\operatorname{row}[N\ AN]. } \\]

This is an exact criterion, not merely a necessary condition:

- Necessity follows by multiplying the actual row \\(r_i\\) by \\([N\ AN]\\).
- Sufficiency follows because membership in the row space means there exists some row \\(r_i\\) producing exactly that pair.

The criterion applies independently to each free row. It does not say that arbitrary compressed rows can be chosen independently of one another subject to additional constraints elsewhere in the construction; it says that each specified pair has a row preimage.

A useful implementation detail: compute a basis for \\(\operatorname{row}[N\ AN]\\) once. Every proposed compressed gadget can then be checked row by row before attempting a full realization.

## 3. Is the \\(q=5\\) rank gate closed?

Search boundary, not a no-go theorem

The report does not establish a structural impossibility theorem for the \\(q=5\\) construction.

There are three logically different claims here:

1. \\(Y_1\ne e_1\\) makes \\(\operatorname{row}Y\\) a fixed plane.
2. \\(Y_1=e_1\\) creates a potential rank drop at \\(\lambda=1\\).
3. Adding \\(e_3,e_4\\) components to the corresponding offset might avoid that rank drop.

The first two can be useful reductions within the specific proposed parametrization. But the report does not give enough algebra to establish that they cover every liftable construction, nor that every possible offset with \\(e_3,e_4\\) components necessarily fails.

The 2,000 random trials are evidence about the search space and parametrization tested. They do not prove nonexistence.

### What can be stated rigorously?

For the particular proposed family, if its derivation proves that \\(Y_1\ne e_1\\) forces the remaining rows into a fixed plane, then the determinant condition in that family reduces to linear constraints. That rules out a quadratic gate within that family and under those hypotheses.

Likewise, if \\(Y_1=e_1\\) and the first corresponding pencil row is exactly

\\[ (\lambda-1)e_1, \\]

then that row vanishes at \\(\lambda=1\\). But a vanishing row alone does not imply that the whole pencil loses rank: the other rows may still span the required \\(\omega\\)-dimensional row space. One must calculate the rank of the entire pencil at \\(\lambda=1\\).

That last distinction is important. A row vanishing at a particular \\(\lambda\\) is a warning sign, not by itself a proof of failure of (5b).

### A better next step than more random trials

I would turn the proposed \\(q=5\\) family into a symbolic elimination problem:

- Write each free row as an independent vector \\(r_i\\).
- Express its pair \\((r_iN,r_iAN)\\) using the row-space liftability constraint.
- Impose the proposed rank-gate equation and the exact-rank chart condition.
- Substitute into \\(P(1)\\), and impose that all its \\(\omega\times\omega\\) minors are nonzero collectively (at least one must be nonzero).
- Eliminate the row variables and determine whether the resulting parameter set is empty.

This would produce either a genuine no-go result for the specified family or an explicit surviving parameter locus. It would not automatically prove a no-go theorem for all \\(q=5\\) observer constructions.

Recommended report wording: “No symbolic liftable gate has been found in the tested \\(q=5\\) families. The proposed cases narrow the search, but a general structural obstruction remains unproved.”

## 4. A simple spectral gadget for \\((5b)\iff f\ne0\\)

A compressed gadget exists

There is a particularly small construction. It also exposes a problem with the proposed “gcd exactly \\(f\\)” requirement.

Take

\\[ H=\begin{bmatrix}1\\\0\end{bmatrix}, \qquad H_A=\begin{bmatrix}0\\\f\end{bmatrix}. \\]

Here \\(H\\) is a \\(2\times1\\) matrix of constant rank

\\[ \operatorname{rank}H=1 \\]

for every \\(f\\), including \\(f=0\\). The pencil is

\\[ P(\lambda)=\lambda H-H_A =\begin{bmatrix}\lambda\\\\-f\end{bmatrix}. \\]

Its maximal minors are just its entries. Therefore

\\[ \operatorname{rank}P(\lambda)=1\quad\forall\lambda\in\mathbb C \\]

if and only if \\(\lambda\\) and \\(f\\) do not vanish simultaneously for any \\(\lambda\\). Equivalently,

\\[ \boxed{(5b)\iff f\ne0.} \\]

Indeed:

- If \\(f\ne0\\), the second entry is nonzero for every \\(\lambda\\).
- If \\(f=0\\), then \\(P(0)=0\\), so its rank drops to zero.

This meets the key operational requirements:

1. \\(H\\) is independent of \\(f\\) and has constant full column rank.
2. For \\(f=0\\), the pencil loses rank at \\(\lambda=0\\).
3. For \\(f\ne0\\), the pencil has full column rank for every complex \\(\lambda\\).

It also satisfies (5a), since \\(H_A=FH\\) with, for example,

\\[ F=\begin{bmatrix}0&0\\\f&0\end{bmatrix}. \\]

### Why the gcd is not \\(f\\)

The gcd of the two maximal minors, viewed as polynomials in \\(\lambda\\) over \\(\mathbb C[f]\\), is

\\[ \gcd(\lambda,f)=1. \\]

At \\(f=0\\), the specialized minors are \\(\lambda\\) and \\(0\\), whose gcd in \\(\mathbb C[\lambda]\\) is \\(\lambda\\). At \\(f\ne0\\), the specialized gcd is a nonzero constant.

So the scalar \\(f\\) does not appear as a common factor of the maximal minors. Instead, it controls whether those minors have a common complex root after specializing the parameter.

This is the right algebraic distinction:

- A common factor \\(f\\) in the coefficient ring would mean every maximal minor vanishes identically as a polynomial in \\(\lambda\\) when \\(f=0\\).
- A failure of (5b) at \\(f=0\\) only requires all maximal minors to vanish at some common value \\(\lambda=\lambda_0\\).

The latter is what the gadget needs.

In fact, if \\(H\\) is independent of \\(f\\), has rank \\(\omega\\), and \\(H_A(f)=F(f)H\\), then for every fixed \\(f\\), the matrix

\\[ P(\lambda,f)=(\lambda I-F(f))H \\]

has rank \\(\omega\\) for all but finitely many \\(\lambda\\), because \\(\lambda I-F(f)\\) is invertible away from the spectrum of \\(F(f)\\). Thus, at \\(f=0\\), it cannot have rank below \\(\omega\\) identically in \\(\lambda\\). This rules out the proposed interpretation in which all maximal minors become identically zero as polynomials in \\(\lambda\\).

### Important limitation: this is not yet an observer realization

The \\(2\times1\\) pencil is a compressed spectral gadget. It does not by itself show that there exist fixed \\(A,C,L_0\\) and a free row \\(R\\) producing the pair \\((H,H_A)\\).

For a genuine observer construction, the free row must satisfy

\\[ (H_i,H\_{A,i})\in\operatorname{row}[N\ AN]. \\]

In this example, the two compressed rows are \\((1,0)\\) and \\((0,f)\\). A realization must make the varying second component available while keeping the first component fixed. That is a specific liftability requirement to check, not something implied by the pencil calculation.

Recommendation: replace the “common scalar factor \\(f\\)” target with the more natural target “the maximal minors have a common root in \\(\lambda\\) exactly when \\(f=0\\).” The two-entry pencil above is the simplest model for that polarity.

## 5. Fixed-\\(\kappa\_{\rm obs}\\) FPT via the Gram certificate

The core certificate is sound

The Gram construction is the strongest part of the report. With the corrections below, it gives a credible route to an FPT theorem.

I would separate the proof into four lemmas.

### 5.1 The rank condition (5a)

Let

\\[ G_H=H^{\mathsf T}H,\qquad G_S=H^{\mathsf T}H+H_A^{\mathsf T}H_A. \\]

Then

\\[ \operatorname{rank}G_H=\operatorname{rank}H, \\]

and

\\[ \operatorname{rank}G_S =\operatorname{rank}\begin{bmatrix}H\\\H_A\end{bmatrix}. \\]

For a positive-semidefinite matrix \\(G\\), its eigenvalues are nonnegative, so

\\[ e_j(G)>0\iff \operatorname{rank}G\ge j, \\]

where \\(e_j\\) is the \\(j\\)-th elementary symmetric polynomial of the eigenvalues, equivalently the sum of the \\(j\times j\\) principal minors.

Fix a rank stratum \\(\omega\\). Then

\\[ \boxed{ (5a)\iff e\_\omega(G_H)>0 \quad\text{and}\quad e\_{\omega+1}(G_S)=0. } \\]

The first condition says \\(\operatorname{rank}H\ge\omega\\); the second says the stacked matrix has rank at most \\(\omega\\). Since stacking cannot reduce rank, both ranks must equal \\(\omega\\).

This part is correct.

The case \\(\omega=0\\) is also covered by this rank encoding if one uses \\(e_0(G_H)=1\\): the second condition forces \\(G_S=0\\), hence \\(H=H_A=0\\). But the spectral certificate below needs to treat \\(\omega=0\\) separately.

### 5.2 The bounded-degree Bezout certificate

Assume \\(\omega>0\\), and let \\(f_1,\ldots,f_s\\) be all \\(\omega\times\omega\\) minors of \\(P(\lambda)\\). Each has degree at most \\(\omega\\).

Condition (5b) is equivalent to the polynomials \\(f_i\\) having no common complex root. Equivalently,

\\[ \gcd\_{\mathbb C[\lambda]}(f_1,\ldots,f_s)=1. \\]

The key bounded-degree fact is:

> If real polynomials \\(f_1,\ldots,f_s\\), all of degree at most \\(\omega\\), have no common complex root, then there are real polynomials \\(g_i\\) of degree less than \\(\omega\\) such that\
> \\[\
> \sum\_^s g_i(\lambda)f_i(\lambda)=1.\
> \\]

One way to justify the degree bound is to choose two real linear combinations \\(g,h\\) of the \\(f_i\\) that are coprime. First choose a nonzero combination \\(g\\). It has finitely many complex roots. At each root, the combinations \\(h=\sum b_i f_i\\) that vanish there form a proper real linear subspace of coefficient vectors \\(b\\), since the original family has no common root. Avoiding the finite union of these subspaces gives \\(h\\) with no common root with \\(g\\). The ordinary two-polynomial Bezout identity then gives multipliers of degree less than \\(\omega\\); expanding the combinations gives the claimed \\(g_i\\).

Now form \\(B\\) as follows. For every \\(i\\) and every \\(j=0,\ldots,\omega-1\\), include one row equal to the coefficient vector of

\\[ \lambda^j f_i(\lambda) \\]

in the monomial basis

\\[ 1,\lambda,\ldots,\lambda^{2\omega-1}. \\]

Thus \\(B\\) has \\(2\omega\\) columns.

The Bezout identity exists exactly when the constant coefficient vector

\\[ e_0=(1,0,\ldots,0)^{\mathsf T} \\]

belongs to the row space of \\(B\\). Since \\(B\\) is real,

\\[ \operatorname{row}B=\operatorname{im}(B^{\mathsf T}B). \\]

Consequently,

\\[ \boxed{ (5b)\iff \exists x\in\mathbb R^{2\omega}: B^{\mathsf T}Bx=e_0. } \\]

This is a valid compact certificate: it introduces only \\(2\omega\\) real variables, rather than one multiplier polynomial for every maximal minor.

### 5.3 The coefficient computation needs a small correction

The Cauchy–Binet compression is correct, but the displayed indexing formula in the report should be corrected.

Let \\(c\_{i,a}\\) denote the coefficient of \\(\lambda^a\\) in \\(f_i\\), taking out-of-range coefficients to be zero. The rows of \\(B\\) are indexed by \\((i,j)\\), with \\(0\le j<\omega\\), and

\\[ B\_{(i,j),t}=c\_{i,t-j}. \\]

Therefore

\\[ \boxed{ (B^{\mathsf T}B)\_{t,t'} = \sum\_{j=0}^{\omega-1}\sum\_{i=1}^s c\_{i,t-j}c\_{i,t'-j}. } \tag{1} \\]

The sum over the shift index \\(j\\) is essential.

Define

\\[ K(\lambda,\mu) =\sum\_{i=1}^s f_i(\lambda)f_i(\mu) =\sum\_{a,b}S\_{a,b}\lambda^a\mu^b, \qquad S\_{a,b}=\sum_i c\_{i,a}c\_{i,b}. \\]

Then (1) becomes

\\[ (B^{\mathsf T}B)\_{t,t'} = \sum\_{j=0}^{\omega-1}S\_{t-j,t'-j}. \\]

So the coefficients of \\(K\\) determine \\(B^{\mathsf T}B\\) by a bounded sum.

To compute \\(K\\) without enumerating all row subsets \\(I\\), group the minors by their column set \\(J\\). If \\(P_J(\lambda)\\) denotes the \\(q\times\omega\\) submatrix of \\(P(\lambda)\\) formed by columns \\(J\\), then Cauchy–Binet gives

\\[ \boxed{ K(\lambda,\mu) = \sum\_{\substack{J\subseteq[k]\\\\|J|=\omega}} \det\\!\left( P_J(\lambda)^{\mathsf T}P_J(\mu) \right). } \\]

This identity is correct.

There are only

\\[ \binom{k}{\omega}\le 2^k \\]

terms. Each determinant is only \\(\omega\times\omega\\), and its entries are sums over the \\(q\\) rows. Since \\(k,\omega\le\kappa\_{\rm obs}\\), the number and size of these determinant computations are bounded by a function of \\(\kappa\_{\rm obs}\\), apart from polynomial dependence on \\(q\\).

The important distinction is that one must not explicitly enumerate all \\(\binom q\omega\\) row subsets. The Cauchy–Binet formula is precisely what avoids that dependence.

### 5.4 Why the number of variables is bounded by \\(\kappa\_{\rm obs}\\)

Let

\\[ d_0=\operatorname{rank}[N\ AN]. \\]

Each free row \\(r_i\\) contributes a compressed pair

\\[ (r_iN,r_iAN) \\]

in a vector space of dimension \\(d_0\\). There are \\(r\\) free rows, so the total number of effective free coordinates is

\\[ r d_0=\kappa\_{\rm obs}. \\]

Also,

\\[ k\le d_0\le\kappa\_{\rm obs}, \qquad r\le\kappa\_{\rm obs} \\]

when \\(r\ge1\\). In particular, the compressed matrices \\(H,H_A\\) are affine-linear functions of at most \\(\kappa\_{\rm obs}\\) variables. The number of fixed rows \\(r_0\\), and hence \\(q\\), need not be bounded.

For each rank stratum \\(\omega\\), the resulting existential formula has:

- at most \\(\kappa\_{\rm obs}\\) effective free variables;
- \\(2\omega\le2\kappa\_{\rm obs}\\) Gram-certificate variables;
- a number of polynomial constraints bounded by a function of \\(\kappa\_{\rm obs}\\);
- polynomial degrees bounded by a function of \\(\kappa\_{\rm obs}\\).

The coefficients can be computed by polynomially many arithmetic operations in the input dimensions, multiplied by a parameter-dependent factor. Enumerating \\(\omega=0,\ldots,\min(q,k)\\) adds only a parameter-bounded number of cases, since \\(k\le\kappa\_{\rm obs}\\).

For \\(\omega=0\\), handle the case directly: (5a) forces \\(H_A=0\\), and then (5b) holds automatically. No Bezout certificate is needed.

## 6. What bit-complexity statement is justified?

The report's phrase “modulo standard real quantifier elimination” is directionally right, but I would state the algorithmic conclusion more carefully.

Assume:

1. The input matrices \\(A,C,L_0\\) have rational entries encoded in binary.
2. The parameter is \\(\kappa\_{\rm obs}=r\operatorname{rank}[N\ AN]\\).
3. The nullspace basis \\(N\\), a basis for the row space of \\([N\ AN]\\), and the compressed affine parametrization are computed using exact rational linear algebra.

These computations have polynomial bit complexity in the input length, with the usual polynomial bit-growth bounds for rational Gaussian elimination.

The Gram entries are obtained from sums and determinants of matrices of size at most \\(\kappa\_{\rm obs}\\), with sums over at most polynomially many input rows. Thus the number of arithmetic operations is

\\[ f(\kappa\_{\rm obs})\operatorname{poly}(\mathcal L), \\]

where \\(\mathcal L\\) is the input bit length. The coefficient bit lengths remain polynomially bounded in \\(\mathcal L\\), up to parameter-dependent factors.

The final decision problem is an existential real-algebraic feasibility problem with a parameter-bounded number of variables, polynomials, and degrees. Using a singly-exponential algorithm for existential real feasibility, rather than invoking unrestricted quantifier elimination, gives a bound of the form

\\[ \boxed{ f(\kappa\_{\rm obs})\\,\mathcal L^{O(1)} } \\]

for a computable function \\(f\\).

The precise form of \\(f\\) depends on the chosen real-algebraic decision algorithm and on how the polynomial coefficients are represented. A standard schematic bound for an existential formula with \\(m\\) variables, \\(s\\) polynomials of degree at most \\(D\\), and coefficient bit length at most \\(\tau\\), is

\\[ (sD)^{O(m)}\tau^{O(1)} \\]

for suitable singly-exponential existential-feasibility algorithms. Here

\\[ m\le \kappa\_{\rm obs}+2\omega \le 3\kappa\_{\rm obs}, \\]

and \\(s,D\\) are functions of \\(\kappa\_{\rm obs}\\). This yields the desired FPT form.

I would avoid giving a more explicit exponent for \\(f\\) until the exact real-algebraic algorithm and coefficient representation have been fixed.

Verdict: the Gram-certificate idea is sufficient in principle for the fixed-\\(\kappa\_{\rm obs}\\) FPT proof. The displayed coefficient formula needs the shift-index correction, and the \\(\omega=0\\) case must be separated. The remaining proof obligation is to write out the compressed affine parametrization and bit-growth analysis carefully. I do not see a fundamental obstruction in the stated route.

## 7. Revised status table

| Claim                                          | Revised assessment                | Reason                                                                          |
| ---------------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------- |
| \\(H\_{A,0}=MH_0\\)                            | Not established                   | (5a) allows the free rows \\(Y\\) in the representation of \\(L_0A\\).          |
| Eigenvalue rank drop                           | Correct conditionally             | Valid if \\(H\_{A,0}=MH_0\\).                                                   |
| Nonzero intersection implies \\(\omega\le r\\) | Incorrect inference               | A nonzero intersection does not imply \\(U\subseteq V\\).                       |
| Structural theorem \\(\omega\le r\\)           | Unproved                          | Both the initial inclusion and the intersection case need repair.               |
| \\(\operatorname{rank}[N\ AN]\le n-p\\)        | Correct                           | Both \\(N\\) and \\(AN\\) have columns in \\(\ker C\\).                         |
| Per-row liftability test                       | Exact                             | It is precisely membership in the image of \\(r_i\mapsto r_i[N\ AN]\\).         |
| \\(q=5\\) gate closed                          | Not proved                        | The supplied cases and random trials do not establish exhaustive impossibility. |
| Four-condition scalar-gcd gadget               | Wrong target                      | A scalar common factor is stronger than a parameter-controlled common root.     |
| \\(2\times1\\) spectral gadget                 | Correct as a compressed gadget    | \\(P(\lambda)=(\lambda,-f)^{\mathsf T}\\) gives (5b) exactly when \\(f\ne0\\).  |
| Gram certificate for (5b)                      | Correct, with indexing correction | The \\(2\omega\\)-dimensional certificate is valid.                             |
| Cauchy–Binet compression                       | Correct                           | It avoids enumerating the \\(\binom q\omega\\) row subsets.                     |
| Fixed-\\(\kappa\_{\rm obs}\\) FPT              | Strong proof route                | Needs the complete rational bit-complexity write-up, not a new conceptual idea. |
| Fixed-\\(q\\) polynomial algorithm             | Still a sketch                    | The parametric linear-elimination issue remains.                                |

## 8. Recommended research priorities

I would change the order of work slightly.

First: complete the fixed-\\(\kappa\_{\rm obs}\\) FPT proof. It is now the most mature route. Write it as a sequence of explicit lemmas:

1. Exact compressed parametrization of all free rows using \\(d_0=\operatorname{rank}[N\ AN]\\).
2. Gram characterization of (5a).
3. Bounded-degree Bezout lemma for the maximal minors.
4. Gram certificate \\(B^{\mathsf T}Bx=e_0\\).
5. Cauchy–Binet computation of the certificate without enumerating row minors.
6. Rational bit-complexity and existential-real feasibility bound.

This is a potentially publishable algorithmic result if the details hold up.

Second: repair or replace the structural theorem. The first thing to investigate is whether the original problem has an additional assumption on \\(L_0\\) that implies

\\[ L_0A\in\operatorname{row}[L_0;CA;C]. \\]

If it does, state it explicitly and investigate the remaining intersection case. If it does not, the current proof cannot be used to eliminate \\(q=4\\) or constrain the rank window.

Third: use the small spectral gadget as a target, not as a completed reduction. The pair

\\[ H=\begin{bmatrix}1\\\0\end{bmatrix},\qquad H_A=\begin{bmatrix}0\\\f\end{bmatrix} \\]

is an excellent minimal model of the desired spectral polarity. The next question is whether its parameter dependence can be implemented through a free row \\(r\\) under the exact liftability constraint.

Fourth: put the \\(q=5\\) random search on hold until the symbolic family is specified completely. The current search boundary is useful, but it should not be described as a closed construction route in a theorem or abstract.

### Overall conclusion

The most important correction is that the report's structural theorem is not currently reliable: the fixed-row representation does not follow from (5a), and the nonzero-intersection rank estimate is false. That correction also means the claimed \\(q=4\\) impossibility needs to be revisited.

By contrast, the liftability criterion is exact, the compressed \\(2\times1\\) spectral gadget works, and the Gram-certificate FPT route survives a detailed mathematical audit with manageable corrections. I would make the FPT theorem the main line of the project, while treating rank-gate hardness as exploratory until a genuinely liftable symbolic construction or a rigorous no-go theorem is obtained.