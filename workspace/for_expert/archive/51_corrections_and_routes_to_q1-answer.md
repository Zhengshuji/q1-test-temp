# Research assessment of Report 51: corrections, constrained geometry, and routes toward \\(q=1\\)

The report marks a useful change in the project’s centre of gravity. The earlier question—whether a particular spectral stratum is good or bad—has now been separated from the more difficult question of whether any admissible stratum exists at a given order. The correction \\(q\_{\min}=2\\), together with the exact all-bad result for the \\(q=3,\omega=2\\) stratum, is a particularly clear illustration of why that separation matters.

My overall recommendation is:

1. Prioritise route (a): a general constrained-fibre criterion for \\(q=\omega+1\\), beginning with \\(k-\omega=1\\).
2. In parallel, establish the algebraic-geometric framework needed for route (b), but do not initially attempt a complete classification of all irreducible components.
3. Do not begin with a hardness reduction from the free case. The free case has substantial structure, and the existing genericity results suggest that it may be algorithmically easier than the full constrained problem.
4. Treat route (d) as a literature and equivalence investigation, not as a substitute for a reduction. An equivalence with a known problem is valuable only if the equivalence preserves the actual shared-\\(R\\) structure and the relevant feasibility quantifiers.

The strongest next theorem would be an exact description of the admissible fibre over a Grassmannian point \\(S\\), followed by a spectral criterion on that fibre. This is more likely to yield a genuinely new structural result than a premature complexity claim.

51_corrections_and_routes_to_q1.md

## 1. What is now established, and what still needs proof

### 1.1 The \\(q\_{\min}=2\\) correction is decisive

The report correctly distinguishes three logically different statements:

- a particular rank stratum is empty;
- a particular rank stratum is nonempty but entirely bad;
- no feasible augmentation exists at the specified order.

Only the third implies an order lower bound. The \\(q=3,\omega=2\\) all-bad theorem does not rule out a feasible point with \\(\omega=1\\), and the explicit \\(q=2\\) construction shows that such a point exists in the example. The observability argument also correctly identifies why the terminal-region result was inapplicable.&#x20;

51_corrections_and_routes_to_q1.md



This is not a minor correction. It gives the project a methodological rule worth stating explicitly in the paper:

> Order infeasibility must be proved after taking the union over all admissible ranks \\(\omega\\), not by excluding one rank stratum.

For each \\(q\\), the feasible set is a union of rank strata. A lower bound on \\(q\\) requires excluding every one of them, including strata with different values of \\(\omega\\).

### 1.2 The constrained all-bad theorem is meaningful, but its Lean status must be described precisely

The two Grassmannian points and their compatible-pair parametrisations give a transparent route to the all-bad conclusion. On each of the two points, a common value of \\(\lambda\\) makes the relevant pencil rows lie in a one-dimensional subspace. This proves rank loss for every compatible choice of the bottom rows in that fibre.&#x20;

51_corrections_and_routes_to_q1.md



The Lean result is useful, but the report is right to call it a kernel rather than a machine-checked proof of the complete theorem. The formalised proposition is the terminal linear-algebra implication:

\\[ \text{all rows lie in }\operatorname{span}\\{E_3\\} \quad\Longrightarrow\quad \operatorname{rank}\leq 1. \\]

The derivation of the row form from the compatibility equations, the exhaustion of the Grassmannian points, and the parametrisation of the fibres remain outside the Lean kernel.

For a paper, I would present this as:

- a formalised linear-algebra lemma;
- a human-readable proof of the compatibility parametrisation;
- an exact symbolic verification of the Grassmannian-point exhaustion;
- a statement that the formalisation checks the final rank implication, not the entire theorem.

That is a defensible and useful formal-methods contribution. It should not be described as “the all-bad theorem is Lean-verified” unless the formal file actually includes the preceding derivation.

### 1.3 The RP argument is promising, but one point needs a sharper complexity statement

The sequential two-combination argument is now logically sound: choose a nonzero \\(f\\) in the rational span of the minors, then avoid the finitely many proper subspaces associated with the irreducible factors of \\(f\\). This yields \\(g\\) with \\(\gcd(f,g)=1\\).&#x20;

51_corrections_and_routes_to_q1.md



The remaining issue is not the algebraic idea but the precise bit-complexity lemma for the rectangular polynomial matrix. It should be stated with:

- the coefficient field and representation (here \\(\mathbb Q\\), with rational coefficients encoded in binary);
- dimensions \\(q,k\\);
- degree bound (at most one);
- coefficient bit-size;
- output representation and bit-size;
- deterministic versus randomized complexity.

The report’s intended lemma is plausible, but “follows from rectangular Smith/Hermite form” is not yet a complete proof. In particular, one must verify that the determinantal divisor—the gcd of the maximal minors—is obtained with polynomial bit complexity for the rectangular input in the exact form used. A square-only Smith-form theorem is not enough unless the reduction to the rectangular case is proved and its bit complexity tracked.

I would keep the RP result as a theorem conditional on this explicit lemma until that lemma is written and sourced precisely. The fixed-\\((q,\omega)\\) result and the probabilistic analysis should be kept separate from this remaining computational algebra step.

## 2. Question 1: which route should be prioritised?

### 2.1 Route (a): the constrained criterion for \\(q=\omega+1\\)

First priority

This is the best immediate target for three reasons.

First, the Grassmannian becomes especially manageable. When \\(k=\omega+1\\),

\\[ \operatorname{Gr}(\omega,\omega+1)\cong\mathbb P^\omega. \\]

Every candidate row space \\(S\\) is a hyperplane in the \\(k\\)-dimensional ambient row-coordinate space. It can be represented as

\\[ S=\ker \sigma,\qquad [\sigma]\in\mathbb P((\mathbb C^k)^\*). \\]

The fixed-row condition \\(E+F_0\subseteq S\\) becomes

\\[ \sigma|\_{E+F_0}=0. \\]

Thus the first reduction is not a complicated Grassmannian search: it is a projective linear subspace of \\(\mathbb P^\omega\\), possibly empty.

Second, the compatibility condition has a particularly simple interpretation. Recall

\\[ \mathcal C_S =\\{(x,y)\in S\times S:xZ_1+yZ_2=0\\}, \qquad X_S=\operatorname{pr}\_1\mathcal C_S. \\]

The admissibility condition

\\[ E+X_S=S \\]

is equivalent, once \\(E\subseteq S\\), to

\\[ \dim(E+X_S)=\omega. \\]

Equivalently, the projection \\(X_S\\) must contain enough directions outside \\(E\\) to span \\(S/E\\). In the special case \\(\omega-\dim E=1\\), this reduces to the existence of just one compatible pair \\((x,y)\\) with \\(x\notin E\\). This is an attractive first subcase because the spanning requirement becomes a single nonvanishing condition.

Third, the spectral obstruction is unusually explicit when \\(q=\omega+1\\). In the block representation

\\[ Z=\begin{pmatrix}A\\\B\end{pmatrix}, \qquad B\in\mathbb C^{1\times\omega}, \\]

the bad condition is

\\[ \exists\\,0\ne y\in\ker B,\qquad Ay\in\mathbb Cy. \\]

Equivalently, for every eigenspace \\(E\_\mu=\ker(A-\mu I)\\),

\\[ E\_\mu\cap\ker B=\\{0\\}. \\]

Since \\(B\\) is a scalar-valued linear functional, this gives the useful necessary condition

\\[ \dim E\_\mu\le1 \quad\text{for every eigenvalue }\mu. \\]

If every eigenspace is one-dimensional, goodness is equivalent to \\(B\\) being nonzero on every eigenline.

This is more than a convenient reformulation. It turns the spectral part into a finite collection of geometric nonincidence conditions, indexed by the eigenlines of \\(A\\). The eigenvalues themselves need not be distinct algebraically: what matters here is geometric eigenspace dimension.

Recommended theorem sequence for route (a).

I would not attempt the full general theorem in one step. Prove the following progressively:

1. Projective admissibility theorem. Parameterise all \\(S\\) by \\([\sigma]\in\mathbb P^\omega\\), impose \\(\sigma(E+F_0)=0\\), and express \\(E+X_S=S\\) as a rank condition on an explicitly defined compatibility matrix.
2. Constant-rank compatibility theorem. On each locus where the relevant compatibility-map ranks are constant, describe \\(X_S\\) as the image of a vector bundle map. This will identify where \\(X_S\\) changes dimension.
3. Spectral-line theorem. For each admissible \\(S\\), formulate the condition that the induced quotient functional \\(B_S\\) does not vanish on any eigenline of \\(A_S\\), and prove the eigenspace-dimension obstruction.
4. Generic-fibre theorem. On each irreducible component of the admissible projective locus, decide whether the spectral-good points form a nonempty Zariski-open subset or whether the entire component is bad.

The main technical difficulty will be that \\(A_S\\) and \\(B_S\\) depend on choices of complements and bases. The final theorem should be expressed invariantly, or should explicitly prove that its conditions are independent of those choices.

### 2.2 Route (b): irreducible components for general \\(k>\omega\\)

Second priority

This is the right long-term framework, but a complete component classification is likely too ambitious as the immediate deliverable.

The admissible set is defined by

\\[ \rank H(R)=\omega,\qquad \ker H(R)\subseteq\ker H_A(R). \\]

The first condition is locally closed: it is the intersection of a rank-at-least-\\(\omega\\) open condition with a rank-at-most-\\(\omega\\) closed condition. The second condition is also algebraic on the rank-\\(\omega\\) locus; it can be expressed by

\\[ \rank\begin{bmatrix}H\\\H_A\end{bmatrix}=\omega. \\]

Thus the admissible locus is a locally closed determinantal set.

There is a natural incidence description over the Grassmannian:

\\[ \mathfrak I\_\omega = \\{(S,R): S\in\operatorname{Gr}(\omega,k),\ \operatorname{row}H(R)=S,\ \operatorname{row}H_A(R)\subseteq S\\}. \\]

Its projection to the \\(R\\)-space is the admissible locus. In the constrained case, the fibre over \\(S\\) is controlled by the compatible-pair equations

\\[ xZ_1+yZ_2=0,\qquad x,y\in S. \\]

This suggests a more tractable intermediate objective:

> Do not initially classify the irreducible components of the projected admissible locus in \\(R\\)-space. Classify the incidence space over the Grassmannian, stratified by the ranks of the compatibility maps.

Why? Because the Grassmannian records the row space \\(S\\), while the compatibility equations record exactly which pairs of rows can be realised by a common \\(R\\). Projection to \\(R\\)-space can merge components or create singularities that obscure this structure.

A workable programme is:

- stratify the Grassmannian by \\(\dim X_S\\) and the rank of the full compatibility map;
- on each constant-rank stratum, identify the compatible-pair spaces as vector bundles or kernels of bundle maps;
- impose the spanning condition \\(E+X_S=S\\);
- then analyse the spectral-good locus on the resulting incidence components.

This would produce a structural theorem even if the final component decomposition is not explicit.

### 2.3 Route (c): hardness reduction

Defer

I would not prioritise a reduction yet.

The project has not exhausted the positive structure available in the free case, and the constrained case already has a useful Grassmannian parametrisation. A reduction attempted before those structures are understood risks encoding a problem into variables that can be eliminated by a genericity argument.

The most natural candidate source problems are:

- affine existential singularity;
- affine rank minimisation or low-rank completion;
- existential feasibility of bilinear or quadratic systems.

But none is an immediate match. The first asks for a singular matrix in an affine space; the observer problem asks for a candidate \\(R\\) whose entire pencil avoids rank loss. The second minimises rank, whereas the present problem fixes a rank stratum and imposes a universal spectral condition. The third has the right algebraic flavour but requires a reduction that preserves the shared dependence of \\(H\\) and \\(H_A\\) on the same \\(R\\).

The central obstruction is exactly the one identified in the report: the same \\(R\\) controls both blocks. It is not legitimate to choose \\(H\\) and \\(H_A\\) independently, even if their separate affine images appear flexible.

### 2.4 Route (d): equivalence or barrier result

This is worth pursuing as a parallel literature investigation, but not as the main mathematical route.

The useful question is not simply whether the problem resembles AZE, matrix completion, or a regular-subpencil problem. It is whether there is a polynomial-time many-one reduction preserving:

1. the shared-\\(R\\) dependence;
2. the full-row-rank condition on \\(L\\);
3. the rank-\\(\omega\\) admissibility condition;
4. the universal quantifier over \\(\lambda\in\mathbb C\\);
5. the distinction between real and complex feasibility, if the input data are real.

Without all five, the equivalence may be only heuristic.

A particularly useful barrier result would show that a proposed source problem cannot be encoded in the free regime because the free regime admits a randomized polynomial-time algorithm. That would redirect any future hardness attempt toward the constrained compatibility geometry.

## 3. Question 2(i): is induction on \\(k-\omega\\) plausible?

Yes, but the proposed “\\(\mathbb P^1\\)-bundle peeling” is not automatically valid. I would retain the induction idea but change its geometric formulation.

### 3.1 The first step \\(k-\omega=1\\) is genuinely special

For \\(k=\omega+1\\), the choice of \\(S\\) is a hyperplane, so the Grassmannian is projective space. This is a genuine simplification, not just a dimension reduction.

The condition \\(E+F_0\subseteq S\\) cuts out a projective linear subspace. The remaining compatibility and spanning conditions then define algebraic rank loci inside that projective space. This makes the first case suitable for explicit equations and exact elimination.

### 3.2 Why naive peeling does not produce a \\(\mathbb P^1\\)-bundle

For \\(k-\omega=d>1\\), one might try to choose a chain

\\[ S\_\omega\subset S\_{\omega+1}\subset\cdots\subset S_k \\]

and add one ambient dimension at a time. But the space of intermediate subspaces is a flag variety, and the fibres of the natural projections are generally Grassmannians, not necessarily projective lines.

More importantly, the compatibility condition is not preserved in a simple way under such a chain. The map

\\[ S\longmapsto \mathcal C_S =\\{(x,y)\in S^2:xZ_1+yZ_2=0\\} \\]

is a kernel construction whose dimension can jump as \\(S\\) changes. Its projection \\(X_S\\) can jump as well. Thus a one-dimensional extension of \\(S\\) may change both the dimension and the geometry of the compatible-pair space.

The spectral condition can jump at the same time: the induced operator \\(A_S\\) and quotient map \\(B_S\\) depend on the chosen \\(S\\).

### 3.3 A better induction: stratified flag incidence

I would formulate an induction through the incidence space of flags, rather than claim a bundle structure that may fail.

At each stage:

1. Fix a subspace \\(S_j\\) of dimension \\(\omega+j\\).
2. Record the ranks of the restrictions of the compatibility maps to \\(S_j\times S_j\\).
3. Extend \\(S_j\\) by one dimension, and derive the conditions under which the compatibility ranks change by \\(0\\), \\(1\\), or more.
4. Track the corresponding change in \\(X\_{S_j}\\) and in the dimension of \\(E+X\_{S_j}\\).
5. Only after these rank conditions are fixed, analyse the spectral incidence.

This is a stratified induction, not a uniform projective-bundle induction. It may still be effective, but its success depends on whether the number and complexity of the rank strata remain controlled.

My assessment: \\(k-\omega=1\\) is the right first theorem. A general induction is plausible as a research programme, but there is no reason yet to expect a simple one-polynomial recurrence or a \\(\mathbb P^1\\)-bundle at each step.

## 4. Question 2(ii): is the free case a plausible source of hardness?

There is an important distinction between two problems:

- choosing one member of an affine family of matrices to have full rank;
- choosing one member of an affine family of pencils to have full rank for every \\(\lambda\\).

The first is much closer to symbolic matrix rank and determinant identity testing. The second is the actual spectral condition.

### 4.1 Fixed-\\(\lambda\\) affine full-rank existence is not the right hardness target

For an affine matrix family \\(M(t)\\), existence of a parameter \\(t\\) for which \\(M(t)\\) has full column rank is equivalent, over an infinite field, to at least one maximal minor being a nonzero polynomial in \\(t\\). This is a polynomial identity testing question.

For square linear matrix spaces, the closely related symbolic determinant identity testing problem asks whether a matrix space contains a nonsingular matrix. There are deterministic polynomial-time results for special classes, but not a general deterministic solution in the standard model. Ivanyos, Karpinski, Qiao, and Santha study symbolic matrix rank and symbolic determinant identity testing, including deterministic algorithms for special classes such as spaces spanned by rank-one matrices or triangularizable matrices.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://eccc.weizmann.ac.il\&sz=32)

eccc.weizmann.ac.il



Thus, a reduction from generic affine full-rank existence alone would not automatically give the desired hardness. It would need to exploit the additional universal-\\(\lambda\\) requirement.

### 4.2 A potentially important positive result: the free affine-pencil problem has a generic resultant test

Suppose the relevant family is genuinely affine in a parameter vector \\(t\\):

\\[ P_t(\lambda)=\lambda H(t)-H_A(t), \\]

where \\(H(t)\\) and \\(H_A(t)\\) are affine in \\(t\\), and \\(\rank H(t)=\omega\\) on a nonempty open domain \\(D\\).

The genericity theorem already established for such families says that the bad locus is closed in \\(D\\). Consequently,

\\[ \exists t\in D:\ P_t(\lambda)\text{ has full column rank for all }\lambda \\]

is equivalent to generic goodness on \\(D\\). Equivalently, over the rational function field \\(\mathbb C(t)\\),

\\[ \gcd\\{\text{all }\omega\times\omega\text{ minors of }P_t(\lambda)\\}=1 \quad\text{in }\mathbb C(t)[\lambda]. \\]

This observation suggests a concrete randomized algorithm for the fixed affine-pencil family, even when \\(q,\omega\\) vary.

Let \\(M_1,M_2\\) be two independently sampled \\(\omega\times q\\) constant matrices, and form

\\[ f_i(t,\lambda)=\det(M_iP_t(\lambda)),\qquad i=1,2. \\]

By Cauchy–Binet, each \\(f_i\\) is a linear combination of the maximal minors of \\(P_t(\lambda)\\). For generic choices of \\(M_1,M_2\\), the gcd of these two combinations equals the gcd of the full collection of maximal minors over \\(\mathbb C(t)[\lambda]\\). Thus the generic pencil is good precisely when the resultant

\\[ \operatorname{Res}\_\lambda(f_1,f_2) \\]

is not identically zero as a polynomial in \\(t\\), subject to the usual handling of zero polynomials and degree drops.

The crucial computational point is that \\(f_i\\) can be computed as the determinant of an \\(\omega\times\omega\\) matrix. One need not enumerate all \\(\binom q\omega\\) maximal minors.

This is a promising route to a randomized polynomial-time test for the fixed affine-pencil family, with a bit-complexity proof still to be supplied. The relevant bounds are controlled by the pencil size and the degree of the resultant, rather than by explicitly listing all maximal minors.

There are, however, two important qualifications:

- This is a test for a fixed affine family of pencil coefficients. It is not yet an algorithm for the full constrained observer problem.
- In the observer problem with \\(k>\omega\\), admissibility itself involves the nonlinear condition \\(\ker H\subseteq\ker H_A\\). Even if the underlying row map is surjective, the global admissible set is not automatically one affine space.

This is why I would not try to prove hardness in the free case first. The fixed-\\(S\\) free fibre is likely to admit a generic resultant method. The difficult question is whether the union over admissible \\(S\\) can be handled with comparably controlled geometry.

### 4.3 What would make a free-case hardness reduction credible?

A successful reduction would have to encode the source problem in the choice of the admissible row space \\(S\\), not merely in a fixed affine pencil with freely chosen bottom rows.

It would also need to avoid the genericity collapse above. If the good set is nonempty on an irreducible affine domain, it is open dense, so a reduction that encodes a discrete choice only through exceptional parameter values may be destroyed by generic perturbation.

This gives a useful obstruction to keep in mind:

> A reduction that relies on isolated good parameter values inside an irreducible affine family is incompatible with the open-dense genericity theorem unless the admissible domain itself is restricted or decomposed in a way that prevents the perturbation.

That is a concrete reason to investigate constrained geometry before investing in free-case hardness.

## 5. Question 2(iii): is stratification by normal rank \\(\rho\\) the right algorithmic template?

Yes, but stratification by \\(\rho\\) alone is too coarse. I would use it as one layer in a more complete stratification.

### 5.1 What \\(\rho\\) captures

For a fixed top block, define

\\[ P_0(\lambda)=\lambda U_0-V_0, \qquad \rho=\operatorname{nrank}P_0(\lambda). \\]

The normal rank determines how much rank is already supplied by the fixed rows, generically in \\(\lambda\\). The free-fibre classification shows why this is useful: different values of \\(\rho\\) lead to different mechanisms for repairing rank loss.

The proportionality case

\\[ V_0=\lambda_0U_0 \\]

must be separated from the generic \\(\rho=2\\) case because the fixed pencil vanishes at a finite spectral point and requires more free directions to repair it.

So the report is right that \\(\rho\\), together with proportionality type, is more informative than \\(\dim(E+F_0)\\) alone.

### 5.2 Why \\(\rho\\) is not sufficient in the constrained case

The constrained case has additional data:

\\[ xZ_1+yZ_2=0,\qquad x,y\in S. \\]

Two subspaces \\(S\\) may have the same dimension and the same normal rank of their induced fixed pencil, yet different compatibility spaces. One may have enough compatible first coordinates to span \\(S/E\\); the other may not.

Even when both are admissible, their spectral pencils may have different determinantal divisors. The bad root can also vary with the parameter, so it is not enough to check whether a single common \\(\lambda_0\\) causes rank loss throughout the fibre.

The report's own all-bad example illustrates this last distinction: each of the two admissible Grassmannian points has a common bad value, but the value differs between the two points.&#x20;

51_corrections_and_routes_to_q1.md



### 5.3 The stratification I would actually use

For each candidate \\(S\\), or more generally on the Grassmannian incidence space, record the following data:

1. Fixed-pencil normal rank\
   \\[\
   \rho(S)=\operatorname{nrank}(\lambda U_S-V_S).\
   \\]
2. Proportionality and common-factor data for the maximal minors of the fixed pencil.
3. Compatibility-map rank, including the rank of\
   \\[\
   (S\times S)\longrightarrow \operatorname{Hom}(\ker T,\mathbb C),\
   \qquad (x,y)\longmapsto xZ_1+yZ_2.\
   \\]
4. Projection rank determining \\(\dim X_S\\).
5. Spanning rank determining \\(\dim(E+X_S)\\).
6. Rank of the full observer matrix \\(L\\), since the full-row-rank requirement is a separate open condition.

On each locally closed constant-rank stratum, one can then study the generic pencil over the function field of each irreducible component. The generic determinantal divisor answers whether the bad spectral locus fills that component or is a proper closed subset.

This is a sound algorithmic template:

\\[ \boxed{ \text{rank stratification} \ \longrightarrow\ \text{irreducible components} \ \longrightarrow\ \text{generic determinantal divisor} \ \longrightarrow\ \text{real-point feasibility}. } \\]

The final arrow is important. A complex Zariski-open subset of a complex component need not automatically contain a real point on the relevant real locus. For real-input synthesis, the existence of real points must be treated separately.

### 5.4 A key simplification: generic gcd, not explicit bad-root tracking

I would avoid trying to parameterise every bad eigenvalue \\(\lambda\\) as a function of \\(S\\). The generic gcd criterion is more robust:

\\[ \Delta_S(\lambda) = \gcd\\{\omega\text{-minors of }P_S(\lambda)\\}. \\]

On an irreducible component \\(X\\), compute this over the function field \\(\mathbb C(X)\\).

- If \\(\Delta_X\\) is nonconstant, the generic point is bad, and the bad locus fills the component.
- If \\(\Delta_X\\) is a unit, the bad locus is proper closed, and the good locus is nonempty open dense over the complex component.

This directly handles moving bad roots. It is a better invariant than selecting a candidate \\(\lambda_0\\) and attempting to make it common across a whole fibre.

Verdict: adopt the stratification idea, but make compatibility ranks and irreducible components part of the stratification. Normal rank \\(\rho\\) is a useful first invariant, not a complete classifier.

## 6. Question 2(iv): can the block criterion encode quadratic feasibility directly?

It can produce bilinear equations, but that fact alone is not enough for an \\(\exists\mathbb R\\)-hardness reduction.

The block criterion

\\[ \text{bad}\iff \exists\\,0\ne y\in\ker B,\quad Ay\in\mathbb Cy \\]

can be written as

\\[ By=0,\qquad Ay=\mu y,\qquad y\ne0, \\]

for some scalar \\(\mu\\). These equations are bilinear in the matrix entries and the vector \\(y\\), and polynomial after introducing \\(\mu\\).

But the observer synthesis problem does not permit arbitrary independent choices of \\(A\\), \\(B\\), and \\(y\\). The matrices \\(A\\) and \\(B\\) are derived from the same pair \\((H,H_A)\\), and that pair is constrained by the common parameter \\(R\\).

There are therefore three main obstacles.

### 6.1 Shared-variable structure

A naive reduction might encode each quadratic equation using a product of two independent variables, then place the two factors into separate matrix blocks. But in the observer problem those blocks must arise from one \\(R\\). A reduction must demonstrate that every encoded variable is represented consistently across all appearances.

### 6.2 The direction of the spectral condition

The block criterion gives a characterization of badness. The synthesis problem asks for goodness:

\\[ \exists R\quad\forall\lambda\quad \rank Q_R(\lambda)=h. \\]

A direct encoding of quadratic feasibility through an eigenvector condition naturally produces an existential witness for badness, not good synthesis. One must reverse the logic without introducing unwanted solutions.

### 6.3 Genericity can erase isolated algebraic solutions

In a free irreducible affine family, a single good point implies a Zariski-open dense set of good points. Thus a reduction that depends on the existence of one isolated exceptional parameter value is unlikely to work in that regime.

A more credible strategy is to encode the quadratic system into the admissibility locus—the simultaneous conditions on \\(H\\) and \\(H_A\\)—so that the source equations determine whether an appropriate admissible component exists. Then the spectral condition can potentially be made generic on the components that encode solutions.

This reinforces the earlier recommendation: study the constrained admissible geometry before trying to encode arbitrary quadratic systems in the spectral block.

## 7. Question 3: what should the next deliverable be?

My recommendation is (i) first, then (ii). I would not make (iii) the next deliverable.

### 7.1 Why not begin with the paper package alone?

The corrected RP theorem, free-fibre theorem, and constrained collapse lemma form a coherent package. But the free-fibre theorem currently concerns a special geometry, and the collapse lemma is a sufficient condition for an entire fibre to be bad, not a general characterisation of constrained feasibility.

A paper containing only those results may look like a collection of technically correct special cases unless the general constrained-fibre framework provides a unifying theorem.

### 7.2 Why not begin with hardness?

There is no verified hardness reduction yet, and the fixed affine-pencil analysis suggests a potentially efficient generic resultant test. Starting with hardness now would risk spending substantial effort on a regime where a positive algorithmic theorem may be available.

### 7.3 Recommended deliverable sequence

Deliverable A: constrained \\(q=\omega+1\\) theorem

Next

Establish the projective parametrisation, compatibility-rank stratification, and spectral eigenline criterion. Start with \\(k=\omega+1\\), then extend to \\(k-\omega=1\\) with the full observer rank conditions.

Deliverable B: unified paper package

Assemble the corrected RP theorem, the free-fibre classification, the constrained all-bad example, and the new projective criterion. Include the Lean kernel with a precise account of its scope.

Deliverable C: complexity direction

Only after A and B, decide whether the remaining constrained component problem admits a deterministic or randomized algorithm, or whether it is a plausible location for a hardness reduction.

### 7.4 What would make the paper package publishable?

I would aim for a paper with one central theorem and several supporting results:

1. A general structural reduction of (5a)–(5b) to the induced map on \\(W=\mathcal LK\\) and its projective eigenvector locus.
2. An exact constrained-fibre criterion for \\(q=\omega+1\\), with a clear description of its compatibility strata.
3. The free-fibre classification as a complete theorem in its stated regime, with the incidence-dimension proof for the \\(\rho=1\\) case.
4. A rigorous genericity theorem for affine pencil families and its generic determinantal-divisor criterion.
5. A corrected randomized complexity theorem, with the determinantal-divisor algorithmic lemma stated and proved at the required bit-complexity level.
6. A constrained example demonstrating an entire admissible stratum that is bad, while explicitly showing why this does not imply order infeasibility.
7. A formal verification appendix explaining exactly which algebraic kernel is Lean-checked.

I would not claim \\(\exists\mathbb R\\)-hardness, NP-hardness of the full observer synthesis problem, or a complete complexity classification without an actual reduction. A rigorous structural paper with a precise randomized upper bound and a nontrivial constrained theorem is already a substantial result.

## 8. Question 4: references and what they actually establish

There are useful references in all three areas, but the distinctions between the problems matter. I would organise the bibliography into three groups.

### 8.1 Affine matrix spaces, existential singularity, and AZE-type problems

(1) Buss, Frandsen, and Shallit (1999).

Jonathan F. Buss, Gudmund S. Frandsen, and Jeffrey O. Shallit, “The Computational Complexity of Some Problems of Linear Algebra,” Journal of Computer and System Sciences 58(3), 572–596 (1999).

This is the relevant source behind the affine existential-singularity result. A later paper by Bei, Chen, Guan, Qiao, and Sun explicitly summarises the result: deciding whether an affine matrix space contains a non-full-rank matrix is NP-hard over finite fields, \\(\mathbb Q\\), and \\(\mathbb R\\).&#x20;

[image](https://www.google.com/s2/favicons?domain=https://drops.dagstuhl.de\&sz=32)

drops.dagstuhl.de+1



The terminology needs care. There are two different questions:

- Affine existential singularity: does an affine matrix space contain at least one singular matrix?
- Linear-space singularity: are all matrices in a given linear matrix space singular?

These are not interchangeable. The later paper explicitly warns about the terminology and notes that the affine and linear versions can behave quite differently.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://drops.dagstuhl.de\&sz=32)

drops.dagstuhl.de+1



For your project, affine existential singularity is a plausible source problem, but the reduction direction is not automatic. Your desired condition is closer to finding a pencil with no finite rank-drop parameter, whereas affine existential singularity asks for the existence of a rank-deficient member.

(2) Ivanyos, Karpinski, Qiao, and Santha (2015).

Gábor Ivanyos, Marek Karpinski, Youming Qiao, and Miklos Santha, “Generalized Wong Sequences and Their Applications to Edmonds’ Problems,” Journal of Computer and System Sciences 81(7), 1373–1386 (2015).

This is an important reference for symbolic matrix rank and symbolic determinant identity testing. It gives deterministic polynomial-time algorithms for special classes of matrix spaces, including spaces spanned by rank-one matrices and triangularizable spaces.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://eccc.weizmann.ac.il\&sz=32)

eccc.weizmann.ac.il+1



It is useful for understanding the boundary between tractable structured matrix-space problems and the general Edmonds problem. It does not solve the observer-pencil synthesis problem.

(3) Recht, Fazel, and Parrilo (2010).

Benjamin Recht, Maryam Fazel, and Pablo A. Parrilo, “Guaranteed Minimum-Rank Solutions of Linear Matrix Equations via Nuclear Norm Minimization,” SIAM Review 52(3), 471–501 (2010).

This establishes the general NP-hardness of affine rank minimisation, which includes finding low-rank matrices satisfying affine linear constraints.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://epubs.siam.org\&sz=32)

应用数学学会+1



It is relevant background, but I would not use it as a direct hardness source unless you can show that the observer problem actually encodes a minimum-rank objective or an equivalent rank threshold. The observer problem fixes a rank stratum and asks for a universal spectral property; that is a different quantifier structure.

### 8.2 Matrix completion and rank-metric problems

The affine rank-minimisation literature is relevant, but there are at least three different problem types:

| Problem                  | Typical question                                               | Relation to your problem                                                                               |
| ------------------------ | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Low-rank completion      | Can missing entries be filled to achieve rank at most \\(r\\)? | Similar algebraic rank constraints, but usually no spectral universal quantifier                       |
| Affine rank minimisation | Does an affine space contain a matrix of rank at most \\(r\\)? | A possible source problem if the rank threshold can be encoded                                         |
| Rank-metric completion   | Can a matrix be completed within a prescribed rank distance?   | Potentially useful for structured constraints, but the distance objective is not your pencil condition |

The 2025 paper “New Hardness Results for Low-Rank Matrix Completion” gives additional NP-hardness results for structured low-rank completion, including positive-semidefinite completion variants.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

数字对象标识符



I would treat these as possible sources only after identifying a reduction that preserves the observer-specific coupling. In particular, an arbitrary missing-entry pattern does not automatically correspond to the map

\\[ R\longmapsto (RN_K,RAN_K). \\]

That map has a very particular shared-variable structure. Any reduction must realise its constraints using that structure, rather than assuming independently selectable matrix entries.

### 8.3 Polynomial matrix normal forms and the determinantal-divisor lemma

This is the part of the bibliography that needs the most care.

(1) Kaltofen, Krishnamoorthy, and Saunders (1987).

Erich Kaltofen, M. S. Krishnamoorthy, and B. David Saunders, “Fast Parallel Computation of Hermite and Smith Forms of Polynomial Matrices,” SIAM Journal on Algebraic and Discrete Methods 8(4), 683–690 (1987), DOI: 10.1137/0608057.

The paper proves that the Smith form of a square nonsingular polynomial matrix over \\(\mathbb Q[x]\\) can be computed in deterministic polynomial time. It also discusses rectangular generalisations of its approach.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://epubs.siam.org\&sz=32)

应用数学学会+1



However, there is a crucial qualification: the paper's explicit deterministic sequential theorem is formulated for square nonsingular input. Its introduction says that the approach can be generalised to rectangular inputs, but that statement alone is not a complete, independently stated deterministic bit-complexity theorem for the exact rectangular determinantal-divisor problem in your report.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://kaltofen.math.ncsu.edu\&sz=32)

kaltofen.math.ncsu.edu+1



Therefore, I would not cite KKS 1987 alone as if it directly proved the report's rectangular lemma.

(2) Storjohann and Labahn (1997).

Arne Storjohann and George Labahn, “A Fast Las Vegas Algorithm for Computing the Smith Normal Form of a Polynomial Matrix,” Linear Algebra and its Applications 253 (1997), 155–173, DOI: 10.1016/0024-3795(95)00743-1.

The published abstract gives an expected bit-complexity bound for the Smith form of a square nonsingular matrix over \\(\mathbb Z[x]\\), using a Las Vegas algorithm.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://uwspace.uwaterloo.ca\&sz=32)

UWSpace+1



This is useful for a faster alternative, but it is not the deterministic result required by the proposed RP proof, and its stated input is square and nonsingular.

(3) Storjohann and Labahn on rectangular polynomial matrices.

Arne Storjohann and George Labahn, “Preconditioning of Rectangular Polynomial Matrices for Efficient Hermite Normal Form Computation.”

This work explicitly addresses rectangular full-column-rank polynomial matrices and gives a Las Vegas reduction of rectangular Hermite-form computation to smaller rectangular Hermite-form computation.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://cs.uwaterloo.ca\&sz=32)

cs.uwaterloo.ca



It is a useful reference for the rectangular input issue. But Hermite form computation and the precise deterministic computation of the gcd of all maximal minors are not identical claims. The paper's result should not be cited as if it immediately supplied the exact deterministic Smith-form lemma either.

(4) Beckermann, Labahn, and Villard (2006).

Bernhard Beckermann, George Labahn, and Gilles Villard, “Normal Forms for General Polynomial Matrices,” Journal of Symbolic Computation 41(6), 708–737 (2006).

This paper treats rectangular polynomial matrices and shifted Popov/Hermite normal forms, including fraction-free computations over integral domains. It is a relevant source for a rigorous rectangular normal-form treatment.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

科学直通车



### 8.4 What I recommend stating in the paper

I would separate the mathematical identity from the computational lemma.

First, state the algebraic identity:

\\[ \Delta_k(P) = \gcd\\{\det P\_{I,J}: |I|=|J|=k\\} = \prod\_{i=1}^k s_i, \\]

where \\(s_1\mid s_2\mid\cdots\mid s_k\\) are the nonzero invariant factors in the rectangular Smith form of a full-column-normal-rank \\(q\times k\\) polynomial matrix \\(P\\).

Then state the algorithmic result you actually need:

> Rectangular determinantal-divisor lemma. Given a full-column-normal-rank matrix \\(P\in\mathbb Q[\lambda]^{q\times k}\\), with entry degrees at most one and rational coefficients encoded in binary, its \\(k\\)-th determinantal divisor can be computed in deterministic polynomial bit complexity in \\(q,k\\) and the input coefficient bit size.

The proof should cite a rectangular polynomial-matrix normal-form algorithm and explicitly show how its output yields \\(\prod\_{i=1}^k s_i\\). If the chosen source gives a Las Vegas algorithm rather than a deterministic one, the theorem must be labelled accordingly.

This is a small but important distinction: the fact that a rectangular Smith form exists and that its invariant factors multiply to the determinantal divisor is algebraic; the polynomial bit-complexity claim is algorithmic. The paper needs both.

## 9. One concrete computation or small theorem to discriminate between the two scenarios

I recommend one focused experiment, followed by a theorem attempt.

### Proposed experiment: exact component analysis for \\(k=\omega+1\\)

Start with the smallest genuinely constrained case beyond the already studied example:

\\[ k=3,\qquad \omega=2,\qquad q=3. \\]

Use exact rational or symbolic data for \\(Z_1,Z_2,E,F_0\\). Parameterise

\\[ S=\ker(\sigma_1,\sigma_2,\sigma_3), \qquad [\sigma_1:\sigma_2:\sigma_3]\in\mathbb P^2. \\]

Then compute, exactly:

1. the projective locus satisfying \\(E+F_0\subseteq S\\);
2. the compatibility matrix for \\(S\times S\\);
3. the rank strata of that matrix;
4. the locus satisfying \\(E+X_S=S\\);
5. the generic determinantal divisor of the induced pencil on every irreducible component.

The goal is to determine whether the resulting projective admissible locus is typically:

- empty;
- irreducible with a generic-good or generic-bad outcome;
- reducible with different spectral behaviour on different components;
- or structurally more complicated than the proposed rank stratification predicts.

This is not a hardness proof. Its value is that it tests the central structural hypothesis behind route (a) and route (b).

### The small theorem I would attempt immediately after the computation

The most valuable first theorem is:

> Projective constrained-fibre theorem for \\(k=\omega+1\\). On each constant-rank stratum of the compatibility map over the projective space of hyperplanes \\(S\\), the admissible hyperplanes form a locally closed algebraic set. On each irreducible component of that set, the spectral-good locus is either empty or a nonempty Zariski-open subset, and generic goodness is decided by the generic determinantal divisor of the induced pencil over the component's function field.

The first half is a rank-stratification statement. The second half uses the already established projective incidence/genericity argument. The genuinely new work is to express the compatibility map and its rank strata explicitly in hyperplane coordinates, and to prove that the induced pencil is algebraically well-defined on each stratum.

If this theorem works cleanly, it supports the algorithmic scenario. If the component decomposition becomes complicated even in this first projective case, that is evidence that the constrained geometry—not the spectral test—is where a hardness reduction might eventually reside.

## 10. Final prioritisation

| Research direction                           | Assessment                       | Immediate action                                             |
| -------------------------------------------- | -------------------------------- | ------------------------------------------------------------ |
| Constrained \\(q=\omega+1\\) theorem         | Highest value                    | Derive hyperplane-coordinate equations                       |
| General admissible-locus components          | Important, but broad             | Work through incidence-space rank strata                     |
| Free affine-pencil complexity                | Promising algorithmic direction  | Develop the two-compression resultant test rigorously        |
| Hardness from affine singularity             | Premature                        | First establish the precise reduction obstruction            |
| Min-rank or completion hardness              | Secondary                        | Use only if shared-\\(R\\) structure can be preserved        |
| Rectangular determinantal-divisor complexity | Necessary technical closure      | Prove or source the exact rectangular bit-complexity lemma   |
| Lean formalisation                           | Valuable supporting contribution | Extend only after the full mathematical statement stabilises |

My strongest recommendation: make the next research milestone the \\(k=\omega+1\\) constrained projective theorem, not a hardness reduction. In parallel, close the rectangular determinantal-divisor complexity lemma, since it is the remaining technical dependency in the RP package.

The project now has enough structural results to support a serious paper. The next advance should unify them through the geometry of the admissible locus, rather than add another isolated example or an early complexity conjecture.

I would be glad to review a draft of the projective constrained-fibre theorem, especially its hyperplane-coordinate compatibility equations and the generic-gcd argument on each irreducible component.