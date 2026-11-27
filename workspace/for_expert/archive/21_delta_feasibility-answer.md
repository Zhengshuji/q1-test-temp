# Referee report on `21_delta_feasibility.md`

The report contains an important generalization of the previous results. The central theorem, B.31, is correct, and its consequences are stronger than the report currently emphasizes. In particular, it identifies a structural threshold that is more informative than the distinction \\(p=1\\) versus \\(p\ge2\\).

My overall assessment is:

1. B.29 is correct, including the claim that the target dimension \\(r\\) does not affect the minimum order when \\(p=1\\). It can be derived more directly from B.31.
2. B.30 is a useful stratification, but the phrase “almost always feasible” needs to remain an empirical description. The finite sample counts do not establish a genericity theorem.
3. B.31 is correct and important. It gives a necessary condition for every subterminal feasible augmentation:\
   \\[\
   1\le\delta\<r_1-p.\
   \\]
4. The explicit \\(n=6,p=r=2,q=3\\) example establishes that the intermediate stratum can genuinely contain feasible candidates. I also checked its principal rank and pencil claims by exact rational computation.
5. The proposed reformulation of \\(q\_{\min}\\) in Q3 is not sufficient as stated. The existence of an admissible intermediate-\\(\delta\\) subspace is necessary, but not sufficient; the spectral condition must remain in the optimization problem.
6. The strongest new deduction is:\
   \\[\
   \boxed{r_1\le p+1\quad\Longrightarrow\quad q\_{\min}=n-p,}\
   \\]\
   under the standing observability and target-independence assumptions that ensure terminal-order feasibility. Thus \\(p=1\\) is one instance of a broader terminal-only regime.

The main conceptual achievement is that the feasibility question has now been divided into two stages: a geometric exclusion stage, which determines where feasibility is even possible, and a spectral selection stage, which decides which candidates in the remaining stratum actually work.&#x20;

21_delta_feasibility.md



## 1. Preliminary notation and the geometry behind \\(\delta\\)

I recommend fixing the following notation throughout the paper, since the report currently uses several closely related row and state-space subspaces.

Let

\\[ R:=\operatorname{row}C,\qquad D:=\operatorname{row}(CA),\qquad W_0:=\operatorname{row}\begin{bmatrix}CA\\\C\end{bmatrix}=D+R. \\]

Let

\\[ \mathcal Z:=\ker\begin{bmatrix}C\\\\\mathcal L\end{bmatrix}, \qquad \mathcal V:=\mathcal Z^\perp. \\]

For an admissible augmentation,

\\[ \operatorname{rank}\begin{bmatrix}C\\\\\mathcal L\end{bmatrix}=p+q. \\]

Consequently,

\\[ \mathcal V =\operatorname{row}\begin{bmatrix}\mathcal L\\\C\end{bmatrix} =\operatorname{row}\mathcal L+R, \\]

and the sum is direct:

\\[ \boxed{\mathcal V=\operatorname{row}\mathcal L\oplus R,\qquad \dim\mathcal V=q+p.} \tag{1.1} \\]

The dimension parameter in the report is

\\[ \delta =\dim\bigl(D/(D\cap\mathcal V)\bigr). \\]

It is useful to introduce one more parameter:

\\[ \boxed{\rho:=r_1-p,} \qquad r_1=\dim(D+R). \tag{1.2} \\]

Because \\(R\subseteq\mathcal V\\), we have

\\[ \begin{aligned} r_1 &=\dim(D+R),\\\ \dim(D\cap\mathcal V) &\ge \dim(D\cap R), \end{aligned} \\]

but the most transparent calculation is

\\[ \begin{aligned} h &=\dim(\mathcal V+D)\\\ &=\dim\mathcal V+\dim D-\dim(D\cap\mathcal V)\\\ &=q+p+\delta. \end{aligned} \\]

Thus

\\[ \boxed{h=q+p+\delta.} \tag{1.3} \\]

Also,

\\[ \delta\le r_1-p=\rho. \\]

Indeed, since \\(R\subseteq\mathcal V\\),

\\[ D\cap\mathcal V\supseteq D\cap R, \\]

and

\\[ \dim D-\dim(D\cap R) =\dim(D+R)-\dim R =r_1-p. \\]

Therefore the possible strata satisfy

\\[ \boxed{0\le\delta\le\rho.} \tag{1.4} \\]

This notation reveals the central geometry:

- \\(\rho\\) is the number of independent directions contributed by \\(CA\\) modulo the original observation row space \\(R\\).
- \\(\delta\\) is the number of those directions that remain outside the augmented row space \\(\mathcal V\\).
- \\(\rho-\delta\\) is the number of new \\(CA\\)-directions absorbed into \\(\mathcal V\\).

In particular,

\\[ \boxed{ \dim(D\cap\mathcal V) =\dim D-\delta. } \\]

The parameter \\(\delta\\) measures the failure of \\(\mathcal V\\) to contain the \\(CA\\)-row space.

This is a good parameter for the paper because it measures exactly the geometric quantity that controls the rank \\(h\\).

## 2. B.31: detailed verification

### 2.1 The \\(\delta=\rho\\) boundary

From (1.3), if

\\[ \delta=\rho=r_1-p, \\]

then

\\[ h=q+p+\rho=q+r_1. \\]

The equality obstruction B.22 therefore gives

\\[ (5b)\text{ fails}. \\]

This argument is immediate once the dimension formula is established. It does not require \\(q+p\<n\\), except insofar as that condition is part of the setting in which the candidate is being considered.

Thus:

\\[ \boxed{ \delta=\rho\quad\Longrightarrow\quad (5b)\text{ fails}. } \tag{2.1} \\]

### 2.2 The \\(\delta=0\\) boundary

If \\(\delta=0\\), then

\\[ D\subseteq\mathcal V. \\]

Since \\(R\subseteq\mathcal V\\), it follows that

\\[ W_0=D+R\subseteq\mathcal V. \\]

Condition (5a) is equivalent to

\\[ \mathcal VA\subseteq\mathcal V+W_0. \\]

Since \\(W_0\subseteq\mathcal V\\), this becomes

\\[ \boxed{\mathcal VA\subseteq\mathcal V.} \tag{2.2} \\]

This is exactly the invariance conclusion needed.

Now \\(R\subseteq\mathcal V\\), and right multiplication by \\(A\\) preserves \\(\mathcal V\\). Therefore

\\[ \operatorname{row}(CA^k)\subseteq\mathcal V \qquad(k=0,1,2,\ldots). \\]

If \\((C,A)\\) is observable, then

\\[ \operatorname{span}\_{k\ge0}\operatorname{row}(CA^k) =\mathbb C^{1\times n}. \\]

Hence

\\[ \mathcal V=\mathbb C^{1\times n}. \\]

But

\\[ \dim\mathcal V=q+p, \\]

so

\\[ q+p=n. \\]

Consequently, when \\(q+p\<n\\), the case \\(\delta=0\\) is impossible:

\\[ \boxed{ q+p\<n,\quad\delta=0 \quad\Longrightarrow\quad \text{contradiction}. } \tag{2.3} \\]

This proves the second boundary exclusion.

### 2.3 The resulting necessary condition

Combining (2.1) and (2.3), every feasible candidate with \\(q+p\<n\\) must satisfy

\\[ \boxed{ 1\le\delta\<r_1-p. } \tag{2.4} \\]

This is precisely B.31.

Verdict: B.31 is correct. Both boundary arguments are valid, and neither uses observability of \\((L_0,A)\\). The only observability assumption needed is observability of \\((C,A)\\).

### 2.4 The hypothesis \\(q+p\<n\\) must remain explicit

Your concern in Q1(a) is well-founded.

At terminal order,

\\[ q+p=n, \\]

we have

\\[ \dim\mathcal V=n, \\]

so necessarily

\\[ \mathcal V=\mathbb C^{1\times n} \quad\text{and}\quad \delta=0. \\]

This is entirely compatible with feasibility.

Thus the correct statement is not that \\(\delta=0\\) is universally infeasible. It is that \\(\delta=0\\) is incompatible with feasibility below terminal order.

Also, \\(q+p>n\\) is not a possible admissible case, because the rank condition

\\[ \operatorname{rank}[C;\mathcal L]=p+q \\]

cannot exceed \\(n\\).

I recommend stating the range explicitly:

\\[ 1\le q\le n-p-1 \\]

for B.31's subterminal conclusion.

### 2.5 No hypothesis on \\(L_0\\) enters B.31

Your concern in Q1(b) is also resolved.

The \\(\delta=0\\) argument uses only

\\[ R=\operatorname{row}C\subseteq\mathcal V. \\]

This inclusion follows directly from

\\[ \mathcal V=\operatorname{row}[\mathcal L;C]. \\]

The target row space \\(L_0\\) enters only through the admissibility restriction on which \\(\mathcal Z\\)'s or \\(\mathcal V\\)'s are allowed.

The proof does not require \\((L_0,A)\\) to be observable.

This is worth emphasizing in the paper: the necessary condition is a property of the observation dynamics and the admissible augmented row space, not of target observability.

## 3. A stronger deduction: the width of the intermediate stratum controls whether subterminal feasibility is possible

The report's most important unexploited consequence is obtained by combining

\\[ 0\le\delta\le\rho \\]

with

\\[ 1\le\delta<\rho. \\]

Since \\(\delta\\) is an integer, the intermediate set

\\[ \\{1,2,\ldots,\rho-1\\} \\]

is nonempty if and only if

\\[ \rho\ge2. \\]

Therefore:

\\[ \boxed{ \text{Subterminal feasibility requires }r_1-p\ge2. } \tag{3.1} \\]

Equivalently,

\\[ \boxed{r_1\ge p+2.} \tag{3.2} \\]

But

\\[ r_1=\operatorname{rank}\begin{bmatrix}CA\\\C\end{bmatrix} \le2p, \\]

because the stacked matrix has \\(2p\\) rows. Hence

\\[ r_1-p\le p. \\]

Combining this with (3.1) gives

\\[ \boxed{p\ge2.} \tag{3.3} \\]

This recovers the fact that \\(p=1\\) is special, but it gives a more precise statement.

### 3.1 The terminal-only theorem

Suppose

\\[ r_1\le p+1. \\]

Then

\\[ \rho=r_1-p\le1. \\]

There is no integer satisfying

\\[ 1\le\delta<\rho. \\]

By B.31, no subterminal feasible augmentation can exist.

Thus, provided the terminal-order construction is available,

\\[ \boxed{ r_1\le p+1 \quad\Longrightarrow\quad q\_{\min}=n-p. } \tag{3.4} \\]

This is a useful theorem to add to the paper.

The terminal-order construction can be justified directly under the standing assumptions. Since

\\[ \operatorname{rank}[C;L_0]=p+r, \\]

the target row space is disjoint from \\(R=\operatorname{row}C\\). We can extend \\(\operatorname{row}L_0\\) to an \\((n-p)\\)-dimensional subspace \\(U\\) such that

\\[ U\cap R=\\{0\\}. \\]

Choose \\(\mathcal L\\) to be a basis matrix for \\(U\\). Then

\\[ \operatorname{rank}[C;\mathcal L]=n, \\]

so \\(q=n-p\\).

Condition (5a) is automatic because the rows of \\([C;\mathcal L]\\) span the entire state row space.

For completeness, condition (5b) follows from observability of \\((C,A)\\). In the coordinates determined by

\\[ T=\begin{bmatrix}C\\\\\mathcal L\end{bmatrix}, \qquad TAT^{-1} = \begin{bmatrix} A\_{11}&A\_{12}\\\ A\_{21}&A\_{22} \end{bmatrix}, \\]

where \\(A\_{22}\\) is \\(q\times q\\), elementary row operations reduce the rank test for \\(Q\_{\mathcal L}(\lambda)\\) to

\\[ \operatorname{rank} \begin{bmatrix} \lambda I_q-A\_{22}\\\ A\_{12} \end{bmatrix}=q. \\]

By the PBH observability criterion, this is equivalent to observability of \\((C,A)\\). Thus terminal feasibility does not require observability of \\((L_0,A)\\).

This establishes (3.4) under the stated target-independence and observation-observability assumptions.

### 3.2 B.29 becomes a corollary

For \\(p=1\\),

\\[ r_1\le2p=2. \\]

Observability and \\(n>1\\) imply that \\(c^{\mathsf T}\\) and \\(c^{\mathsf T}A\\) are independent, so

\\[ r_1=2=p+1. \\]

Consequently,

\\[ \rho=1. \\]

The intermediate interval

\\[ 1\le\delta<1 \\]

is empty.

B.31 therefore excludes every subterminal feasible order. Terminal feasibility gives

\\[ \boxed{q\_{\min}=n-1.} \\]

This is a particularly clean way to present B.29: it is a direct corollary of the general necessary condition and the fact that a single observation row can contribute at most one new \\(CA\\)-direction beyond \\(C\\).

The original two-case proof remains valuable because it gives an intuitive explanation of the two boundary mechanisms. But for the theorem sequence, I would state B.31 first and then present B.29 as its immediate specialization.

## 4. Q2: Does one feasible point imply that the failure set is a proper algebraic subset?

Not by itself. This question needs a distinction between three statements:

1. Not every candidate in the intermediate stratum fails.
2. The failure set is a proper subset of the intermediate stratum.
3. The failure set is contained in a proper algebraic subset, so feasibility holds generically.

Your exact feasible example establishes the first statement for the corresponding fixed data. If the feasible point and the failing points belong to the same fixed parameter space and the same \\(\delta\\)-stratum, it also establishes the second statement. It does not automatically establish the third.

The distinction is important if you want to use the phrase “almost always feasible” as a mathematical genericity claim.

### 4.1 What is the relevant parameter space?

Fix \\(A,C,L_0\\), and an order \\(q\\). Let

\\[ d=n-p-q. \\]

The augmentation subspaces can be represented by

\\[ \mathcal Z\in\operatorname{Gr}(d,K), \qquad K=\ker\begin{bmatrix}C\\\L_0\end{bmatrix}, \\]

subject to the condition corresponding to (5a).

Equivalently, work with

\\[ \mathcal V=\mathcal Z^\perp \\]

inside the appropriate Grassmannian, imposing

\\[ \operatorname{row}C+\operatorname{row}L_0 \subseteq\mathcal V \\]

and

\\[ \mathcal VA\subseteq\mathcal V+\operatorname{row}(CA). \\]

For fixed \\(q\\), the condition

\\[ \delta(\mathcal V)=\delta \\]

is a rank condition. It defines a locally closed rank stratum in the relevant Grassmannian parameter space.

Thus, after fixing the problem data and \\(q\\), one can define

\\[ \mathfrak S\_{q,\delta} = \\{\text{admissible }\mathcal V:\delta(\mathcal V)=\delta\\}. \\]

This is the correct space on which to formulate a genericity statement.

A caution: the counts in B.30 should not be interpreted as a sample from one algebraic variety unless the underlying \\(A,C,L_0\\) are fixed. If the samples vary the system data as well as the augmentation, they provide evidence about a family of problems, not the geometry of a single fixed stratum.

### 4.2 The spectral failure locus is naturally an incidence projection

On a stratum where the relevant dimensions are constant, consider the reduced pencil

\\[ \overline N\_{\mathcal Z}(\lambda): V/S\longrightarrow X/\mathcal Z, \\]

where

\\[ V=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \qquad S=V\cap\mathcal Z. \\]

The spectral failure locus is

\\[ \mathfrak F\_{q,\delta} = \left\\{ \mathcal Z\in\mathfrak S\_{q,\delta}: \exists\lambda\in\mathbb C,\  \ker\overline N\_{\mathcal Z}(\lambda)\ne\\{0\\} \right\\}. \\]

Introduce the incidence set

\\[ \mathfrak I\_{q,\delta} = \left\\{ (\mathcal Z,\lambda,[x]): \begin{array}{l} \mathcal Z\in\mathfrak S\_{q,\delta},\\\ \lambda\in\mathbb C,\\\ [x]\in\mathbb P(V/S),\\\ \overline N\_{\mathcal Z}(\lambda)[x]=0 \end{array} \right\\}. \\]

Then

\\[ \mathfrak F\_{q,\delta} =\pi(\mathfrak I\_{q,\delta}), \\]

where \\(\pi\\) projects onto the \\(\mathcal Z\\)-coordinate.

This is the appropriate incidence formulation. The equation defining the incidence set is polynomial in local Grassmannian coordinates, \\(\lambda\\), and homogeneous coordinates for \\([x]\\).

By the constructibility theorem for projections of algebraic sets, the failure locus is constructible (after working in the appropriate locally closed parameter space).

But the projection involves the affine parameter \\(\lambda\in\mathbb A^1\\), not a projective parameter. Consequently, the failure locus need not be Zariski closed.

### 4.3 Why a feasible point is not enough for generic feasibility

A simple algebraic example illustrates the issue.

Consider the polynomial family

\\[ f_t(\lambda)=t\lambda-1. \\]

For every \\(t\ne0\\), there is a finite root \\(\lambda=1/t\\). At \\(t=0\\), there is no finite root.

Thus the set of parameters admitting a finite root is

\\[ \\{t\ne0\\}, \\]

which is Zariski open, not Zariski closed.

The root escapes to infinity as \\(t\to0\\). This is exactly the kind of phenomenon that can occur when studying a pencil with a parameter-dependent finite spectrum.

Therefore, even if you exhibit a feasible point, you cannot conclude that the failure locus is a proper algebraic subset. Its Zariski closure might still be the entire stratum.

The rigorous hierarchy is:

| Claim                                        | What must be shown                                                                                      |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Some intermediate candidates are feasible    | Exhibit one exact feasible candidate                                                                    |
| Not all intermediate candidates are feasible | Exhibit one feasible candidate in the fixed stratum                                                     |
| The failure locus is a proper subset         | Prove that it is not the whole stratum                                                                  |
| Feasibility is generic                       | Prove that the feasible set contains a nonempty Zariski-open subset, or an equivalent density statement |

### 4.4 What does your exact example establish?

The example in B.31 has

\\[ n=6,\quad p=r=2,\quad q=3,\quad r_1=4, \\]

and therefore

\\[ \rho=r_1-p=2. \\]

It has

\\[ \delta=1, \\]

which is the only intermediate value.

The reported matrices satisfy the required ranks, the target inclusion, and (5a). I independently checked the principal numerical assertions using exact rational arithmetic:

\\[ \operatorname{rank}[C;L_0]=4,\qquad \operatorname{rank}[C;\mathcal L]=5, \\]

\\[ r_1=4,\qquad h=6,\qquad\delta=1. \\]

The nullspace of \\([C;\mathcal L]\\) is generated by

\\[ \begin{bmatrix} -6&1&-\frac92&\frac32&1&0 \end{bmatrix}^{\mathsf T}, \\]

as reported.

I also checked observability:

\\[ \operatorname{rank}\mathcal O_C=6,\qquad \operatorname{rank}\mathcal O\_{L_0}=6. \\]

Finally, the gcd of all nonzero \\(6\times6\\) minors of \\(Q\_{\mathcal L}(\lambda)\\) is

\\[ \boxed{1.} \\]

Thus there is no common finite complex root of the maximal minors, and (5b) holds.

This is a valid exact witness of feasibility in the intermediate stratum.

The example is particularly useful because it shows that the necessary condition B.31 is nonvacuous and sharp in the sense that the intermediate region really can contain feasible candidates.

### 4.5 What about the one failing intermediate candidate?

The single failing candidate reported for \\((p,r,r_1)=(2,1,4)\\) is also important. It shows that the intermediate condition is not sufficient candidate-by-candidate.

The correct conclusion is therefore:

\\[ \boxed{ \text{The intermediate stratum is the only possible location of subterminal feasibility,} } \\]

but

\\[ \boxed{ \text{not every candidate in that stratum is feasible.} } \\]

This is the right interpretation of B.30.

I would avoid the phrase “the failure set is apparently a proper algebraic subset” unless you have established the relevant algebraic-geometric statement. A more accurate description is:

> In the tested instances, feasibility was observed for nearly all sampled intermediate-stratum candidates. The exact examples establish that the intermediate stratum can contain feasible candidates, while the exceptional failing sample shows that the stratum is not uniformly feasible. Whether the failure locus is algebraically proper, and whether feasibility is generic, remain open.

That wording is rigorous and does not overstate the evidence.

## 5. Q3: Is \\(q\_{\min}\\) now a purely geometric optimization problem?

Not yet. The report's proposed reformulation is close, but it removes one condition that cannot be removed.

You write that \\(q\_{\min}\\) becomes the smallest order at which an admissible \\(\mathcal V\\) with

\\[ 1\le\delta\<r_1-p \\]

exists. This is a necessary geometric filter, not an exact characterization of minimum order.

The reason is already visible in B.30: an intermediate-stratum candidate can still fail (5b).

### 5.1 The exact optimization problem

For a fixed system \\((A,C,L_0)\\), define

\\[ \mathfrak S\_{q,\delta} \\]

to be the admissible subspaces at order \\(q\\) satisfying:

1. the target-space inclusion;
2. the subspace form of (5a),\
   \\[\
   \mathcal VA\subseteq\mathcal V+\operatorname{row}(CA);\
   \\]
3. the rank stratum,\
   \\[\
   \delta(\mathcal V)=\delta.\
   \\]

Let

\\[ \mathfrak S\_{q,\delta}^{\mathrm{sp}} \subseteq\mathfrak S\_{q,\delta} \\]

denote those subspaces satisfying the spectral condition (5b).

Then the exact characterization is

\\[ \boxed{ q\_{\min} = \min\left\\{ q: \bigcup\_{\delta=1}^{\rho-1} \mathfrak S\_{q,\delta}^{\mathrm{sp}} \ne\varnothing \right\\}, } \tag{5.1} \\]

provided the terminal feasible order is included as the upper endpoint.

This formula separates the two tasks:

- Geometry determines which \\(\delta\\)-strata are available.
- Spectral analysis determines which points in those strata satisfy (5b).

B.31 says

\\[ \mathfrak S\_{q,\delta}^{\mathrm{sp}}=\varnothing \quad\text{unless}\quad 1\le\delta<\rho \\]

for \\(q+p\<n\\).

It does not say that every \\(\mathfrak S\_{q,\delta}\\) in that range has a nonempty spectral-feasible subset.

### 5.2 A useful dimension refinement from the quotient-pencil theorem

There is a further formula worth adding to the report.

Recall

\\[ S=V\cap\mathcal Z, \qquad V=\ker\begin{bmatrix}C\\\CA\end{bmatrix}. \\]

We have

\\[ \dim V=n-r_1. \\]

Also, since

\\[ h=\operatorname{rank}\begin{bmatrix}\mathcal L\\\CA\\\C\end{bmatrix}, \\]

the polynomial right-nullspace result gives

\\[ \dim S=n-h. \\]

Therefore

\\[ \begin{aligned} \dim(V/S) &=\dim V-\dim S\\\ &=(n-r_1)-(n-h)\\\ &=h-r_1. \end{aligned} \\]

Using

\\[ h=q+p+\delta,\qquad r_1=p+\rho, \\]

we obtain

\\[ \boxed{ \dim(V/S)=q+\delta-\rho. } \tag{5.2} \\]

The codomain \\(X/\mathcal Z\\) has dimension

\\[ \dim(X/\mathcal Z)=p+q. \\]

Thus, on the \\(\delta\\)-stratum, the reduced pencil has size

\\[ \boxed{ (p+q)\times(q+\delta-\rho). } \tag{5.3} \\]

This is useful for two reasons.

First, it gives a direct matrix-size interpretation of the stratification. The intermediate parameter \\(\delta\\) controls the number of columns of the reduced pencil.

Second, it gives a natural computational representation of the exact spectral condition:

\\[ \operatorname{rank}\overline N\_{\mathcal Z}(\lambda) =q+\delta-\rho \qquad\text{for every finite }\lambda\in\mathbb C. \\]

Equivalently, the maximal minors of this rectangular pencil must have no common finite root.

This is the correct way to combine the geometric \\(\delta\\)-stratification with the spectral test.

### 5.3 What can be optimized geometrically before doing spectral analysis?

Although geometry alone does not determine \\(q\_{\min}\\), it can produce strong lower bounds.

For each order \\(q\\), ask whether

\\[ \mathfrak S\_{q,\delta}\ne\varnothing \\]

for any

\\[ 1\le\delta\le\rho-1. \\]

If all these strata are empty, then order \\(q\\) is impossible without any spectral calculation.

Thus the geometric search can be used as a first-stage pruning procedure:

\\[ \begin{array}{c} \text{Find admissible subspaces}\\\ \downarrow\\\ \text{Discard }\delta=0\\\ \downarrow\\\ \text{Discard }\delta=\rho\\\ \downarrow\\\ \text{Retain }1\le\delta<\rho\\\ \downarrow\\\ \text{Apply the quotient-pencil spectral test.} \end{array} \\]

I strongly recommend implementing this separation in the computational project. It will prevent expensive spectral computations on candidates that B.31 already excludes.

### 5.4 Should the next theorem target be geometric?

Yes, but with a carefully defined objective.

The next geometric question should not be “compute \\(q\_{\min}\\) without spectral analysis.” It should be:

> For fixed \\((A,C,L_0)\\), characterize the orders \\(q\\) and intermediate values \\(\delta\\) for which the admissible Grassmannian stratum \\(\mathfrak S\_{q,\delta}\\) is nonempty.

That is a well-defined geometric problem. It can be studied independently of the spectral condition and will give useful necessary lower bounds.

Then the second problem is:

> Within a nonempty intermediate stratum, characterize the subspaces for which the reduced pencil has full column rank at every finite spectral parameter.

That is the exact remaining feasibility problem.

The separation is conceptually clean and should make the next phase of the project much more manageable.

## 6. Q4: Is there a structural dichotomy between \\(p=1\\) and \\(p\ge2\\)?

There is a genuine structural distinction, but I would formulate it in terms of

\\[ \rho=r_1-p \\]

rather than simply separating \\(p=1\\) from \\(p\ge2\\).

The reason is that \\(p\\) only gives an upper bound on the possible width of the intermediate region:

\\[ \rho\le p. \\]

The actual width is determined by \\(r_1\\), which depends on the position of \\(\operatorname{row}(CA)\\) relative to \\(\operatorname{row}C\\).

### 6.1 The precise structural classification

The possible subterminal feasibility regimes are:

| Condition              | Intermediate values of \\(\delta\\) | Consequence                                     |
| ---------------------- | ----------------------------------- | ----------------------------------------------- |
| \\(\rho=0\\)           | None                                | No subterminal feasible candidate               |
| \\(\rho=1\\)           | None                                | No subterminal feasible candidate               |
| \\(\rho=2\\)           | \\(\delta=1\\)                      | One possible stratum                            |
| \\(\rho=3\\)           | \\(\delta=1,2\\)                    | Two possible strata                             |
| General \\(\rho\ge2\\) | \\(1\le\delta\le\rho-1\\)           | Subterminal feasibility is not excluded by B.31 |

The case \\(\rho=0\\) is generally incompatible with observability when \\(n>p\\): if \\(r_1=p\\), then \\(\operatorname{row}(CA)\subseteq\operatorname{row}C\\), so \\(\operatorname{row}C\\) is \\(A\\)-invariant, and observability forces \\(n=p\\).

Thus, in the nontrivial observable setting \\(n>p\\), the most relevant cases are \\(\rho=1\\) and \\(\rho\ge2\\).

The key theorem is therefore:

> Terminal-only regime. If \\(r_1=p+1\\), then no subterminal order is feasible, and the minimum order is \\(n-p\\), assuming the terminal construction is admissible.

This theorem includes every \\(p=1\\) observable system with \\(n>1\\), but it also applies to systems with \\(p\ge2\\).

### 6.2 Why \\(p\ge2\\) is necessary but not sufficient

Since

\\[ r_1\le2p, \\]

we have

\\[ \rho=r_1-p\le p. \\]

For \\(\rho\ge2\\), necessarily \\(p\ge2\\).

But \\(p\ge2\\) does not guarantee \\(\rho\ge2\\). For example, a system with \\(p=2\\) may have

\\[ r_1=3, \\]

in which case

\\[ \rho=1, \\]

and the intermediate region is still empty.

Thus the correct structural statement is:

\\[ \boxed{ \text{Subterminal feasibility requires }r_1\ge p+2, } \\]

not merely \\(p\ge2\\).

This is a stronger and more precise classification than the proposed “small \\(p\\) versus large \\(p\\)” dichotomy.

### 6.3 Interpreting the reported \\((2,2)\\) experiments

Your \\((p,r)=(2,2)\\) experiments show

\\[ q\_{\min}-q_0\in\\{0,1\\} \\]

for 600 tested random instances.

This is interesting because the gap is much smaller than the Class I gap. However, it is not yet enough to establish a theorem about all systems with \\(p=2,r=2\\).

I would formulate the observation as a conjecture only after fixing the precise parameter class and specifying the range of \\(n\\), the observability assumptions, and the definition of \\(q_0\\).

A plausible research conjecture is:

> Conjecture (small-gap behavior for low target dimension and multiple outputs). For certain fixed pairs \\((p,r)\\) with \\(p\ge2\\), the minimum feasible order may lie within a uniformly bounded distance of the dimension lower bound \\(q_0\\).

This is deliberately weaker than claiming that all \\(p\ge2\\) cases have small gaps.

The data currently support investigating this possibility, not asserting it.

## 7. Q5: Recommended theorem order for the paper

Your proposed order is essentially correct. I would make one slight adjustment: introduce the two boundary exclusions before stating B.31, so the reader sees why the intermediate stratum is the only possible location for feasibility.

Here is the sequence I recommend.

### Section 1. Problem formulation

Define:

- the system and target;
- admissible augmentations;
- conditions (5a) and (5b);
- the minimum-order problem;
- the rank parameter \\(r_1\\).

Clearly state the standing assumptions, particularly observability of \\((C,A)\\) and the target-independence condition.

### Section 2. Subspace reduction

Introduce

\\[ \mathcal Z=\ker[C;\mathcal L], \qquad \mathcal V=\mathcal Z^\perp. \\]

Prove

\\[ \mathcal V=\operatorname{row}[\mathcal L;C], \qquad \dim\mathcal V=q+p, \\]

and establish the general characterization

\\[ \boxed{ (5a)\iff \mathcal VA\subseteq\mathcal V+\operatorname{row}(CA). } \\]

This is the fundamental geometric reduction.

### Section 3. The \\(\delta\\)-stratification and counting identity

Define

\\[ \delta = \dim\left( \operatorname{row}(CA)/ (\operatorname{row}(CA)\cap\mathcal V) \right), \\]

and

\\[ \rho=r_1-p. \\]

Prove

\\[ 0\le\delta\le\rho, \qquad h=q+p+\delta. \\]

This section should explain the geometric meaning of the parameter and how it partitions the admissible Grassmannian.

### Section 4. Quotient-pencil spectral condition

Introduce the quotient pencil and its pointwise full-column-rank condition.

Then present the intrinsic partial-map formulation:

\\[ \Phi:\mathcal LV\to\mathbb C^q, \qquad \Phi(\mathcal Lx)=\mathcal LAx. \\]

The spectral condition becomes the absence of a nonzero \\(u\in\mathcal LV\\) satisfying

\\[ \Phi(u)\in\operatorname{span}\\{u\\}. \\]

Also include

\\[ \dim(V/S)=q+\delta-\rho. \\]

This makes the connection between the geometric strata and the sizes of the reduced pencils explicit.

### Section 5. The two boundary obstructions

Prove the two results:

Boundary I:

\\[ \delta=\rho \quad\Longrightarrow\quad h=q+r_1 \quad\Longrightarrow\quad (5b)\text{ fails}. \\]

Boundary II:

\\[ \delta=0,\quad q+p\<n \quad\Longrightarrow\quad \mathcal V\text{ is }A\text{-invariant} \quad\Longrightarrow\quad \text{contradiction with observability}. \\]

The first uses B.22; the second uses the general subspace characterization.

### Section 6. General necessary feasibility theorem

Now state B.31:

\\[ \boxed{ q+p\<n,\quad (5b) \quad\Longrightarrow\quad 1\le\delta\<r_1-p. } \\]

This is the natural synthesis of the previous sections.

I would title it:

Theorem (Necessary intermediate-stratum condition for feasibility).

Do not call it a complete feasibility criterion, because the intermediate condition is not sufficient.

### Section 7. Terminal-only classification and Class I

First state the more general corollary:

\\[ r_1\le p+1 \quad\Longrightarrow\quad q\_{\min}=n-p. \\]

Then specialize to \\(p=1\\):

\\[ \boxed{q\_{\min}=n-1.} \\]

This makes B.29 an application of the general theorem rather than an isolated coincidence.

### Section 8. Intermediate-stratum examples

Include:

- the exact feasible \\(n=6,p=r=2,q=3,\delta=1\\) example;
- the exact failing intermediate candidate;
- the other examples and sampling results.

The feasible and failing examples should be discussed together. Their combination illustrates the precise role of B.31: it identifies where feasibility can occur, but does not decide feasibility within that region.

### Section 9. Complexity and open problems

Separate:

1. geometric nonemptiness of intermediate strata;
2. spectral feasibility within those strata;
3. complexity of the combined synthesis problem.

This separation is important. It prevents the paper from prematurely claiming that the problem has become purely geometric.

## 8. Further deductions and concrete research directions

I see three particularly promising directions arising from this report.

### 8.1 Study the minimum possible \\(\rho\\) for a fixed system

The parameter

\\[ \rho=\operatorname{rank}\begin{bmatrix}CA\\\C\end{bmatrix}-p \\]

is independent of the augmentation \\(\mathcal L\\).

It measures the number of new directions generated by one step of the observation dynamics.

For an observable system with \\(n>p\\),

\\[ 1\le\rho\le p. \\]

If \\(\rho=1\\), the terminal-only theorem applies. If \\(\rho\ge2\\), subterminal feasibility becomes possible but is not guaranteed.

This suggests a first classification of systems by their one-step observation rank growth:

- \\(\rho=1\\): terminal-only feasibility;
- \\(\rho\ge2\\): potentially subterminal feasibility.

It would be valuable to investigate whether \\(\rho\\) predicts the minimum gap, or whether higher Krylov ranks are also necessary.

### 8.2 Introduce higher-step rank-growth parameters

The current parameter only uses \\(C\\) and \\(CA\\). But observability is a statement about the full sequence

\\[ C,\ CA,\ CA^2,\ldots. \\]

Define

\\[ r_k:=\operatorname{rank} \begin{bmatrix} C\\\CA\\\\\vdots\\\CA^k \end{bmatrix}, \qquad \Delta_k:=r_k-r\_{k-1}. \\]

Then

\\[ \Delta_1=r_1-p=\rho. \\]

The sequence \\(\Delta_k\\) measures the incremental number of new observable directions at each step. It is closely related to the observability indices of the pair \\((C,A)\\).

A natural question is whether the minimum feasible augmentation order can be bounded in terms of several increments

\\[ \Delta_1,\Delta_2,\ldots \\]

rather than \\(\Delta_1\\) alone.

This may help explain why two systems with the same \\((p,r,r_1)\\) can have different minimum-order behavior.

For example, if the first-step rank growth is large but the subsequent increments are concentrated in a small number of Krylov chains, the admissible intermediate subspaces may have a very different geometry from a system with evenly distributed observability indices.

I would treat this as a research direction, not a theorem at this stage.

### 8.3 Study the exceptional spectral-failure locus in the intermediate stratum

Your exact feasible and failing examples suggest that the intermediate stratum contains a nontrivial spectral selection problem.

For each fixed system and fixed \\((q,\delta)\\), I recommend computing:

1. the dimension of the admissible Grassmannian stratum;
2. the dimension of the spectral-failure incidence variety;
3. the dimension of the image of that incidence variety;
4. whether the failure image is dense;
5. whether the feasible set contains a nonempty Zariski-open subset.

This is more informative than simply counting feasible candidates.

If the failure incidence has smaller dimension than the parameter stratum, then its closure is proper, and generic feasibility follows. But this dimension comparison must be done carefully: the projection may have positive-dimensional fibers, and the dimension of the incidence variety alone does not determine the dimension of its image.

The correct calculation is

\\[ \dim\overline{\pi(\mathfrak I\_{q,\delta})} \\]

compared with

\\[ \dim\mathfrak S\_{q,\delta}. \\]

If the former is strictly smaller, generic feasibility follows. If they are equal, the dimension count is inconclusive.

This is a promising application of algebraic geometry to the spectral part of the problem.

## 9. Final assessment

## Mathematical status of the new results

B.29: \\(p=1\\), arbitrary \\(r\\)

Correct

A consequence of B.31 and terminal-order feasibility. The target dimension does not affect the lower-bound mechanism.

B.30: \\(\delta\\)-trichotomy

Correct with qualification

The boundary exclusions are rigorous. “Almost always feasible” remains empirical, not a proved genericity statement.

B.31: necessary feasibility condition

Proved

The proof is valid, with \\(q+p\<n\\) essential in the \\(\delta=0\\) branch.

Exact \\(n=6\\) feasible example

Exact checks confirmed

The reported ranks, nullspace, observability and maximal-minor gcd are consistent with exact rational verification.

Purely geometric characterization of \\(q\_{\min}\\)

Not established

The intermediate-stratum condition is necessary, not sufficient. The quotient-pencil spectral test remains essential.

Generic feasibility of intermediate strata

Open

The exact examples establish existence, but genericity requires an incidence-projection or algebraic argument.

### My principal recommendation

The next major theorem should be the terminal-only classification

\\[ \boxed{ r_1\le p+1 \quad\Longrightarrow\quad q\_{\min}=n-p. } \\]

It is a clean generalization of Class I, follows directly from B.31, and identifies the actual structural threshold.

After that, I would concentrate on the first genuinely nontrivial case:

\\[ \boxed{ r_1=p+2,\qquad \rho=2,\qquad\delta=1. } \\]

This is the narrowest possible intermediate regime. There is exactly one candidate value of \\(\delta\\), so the geometric ambiguity is minimized. The remaining question is purely spectral: does the admissible stratum contain a subspace for which the reduced pencil is injective at every finite \\(\lambda\\)?

Your \\(n=6,p=r=2,q=3\\) example already shows that the answer can be yes. The next objective should be to understand whether this happens generically, what structural conditions can force failure, and how the answer depends on the observability indices of \\((C,A)\\).

In short: B.31 has converted the original feasibility problem into a much more structured one. The boundary strata are completely understood; the intermediate strata are now the only place where the real problem remains. That is a substantial simplification, and it gives the project a precise next theorem target.