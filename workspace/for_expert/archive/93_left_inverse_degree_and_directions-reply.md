# **Strategic assessment of the minimum-order functional-observer project**

I have reviewed the entire report, including the established theorems, computational observations, conjectures, unresolved geometric questions, and the six requests in Part III.

My overall assessment is that **the project has reached a significant theoretical stage, but its main obstacle has shifted from obtaining upper bounds to understanding the geometry and complexity of the unrestricted feasibility problem.**

You already have several substantial results:

- A bit-complexity XP algorithm parameterized by \\(q\\).
- A bit-complexity FPT algorithm parameterized by \\(\ell=\operatorname{rank}(AN)\\).
- An \\(\exists\mathbb R\\) membership result.
- An exact polynomial-time solution for \\(r=0\\).
- A partial geometric theory for the hyperplane and \\(c=2\\) cases.

However, none of these resolves unrestricted \\(q1\\), and there is currently no hardness reduction.

I would change the immediate research strategy. Rather than continuing to develop all six directions simultaneously, I recommend organizing the project around three central questions:

1. Can the geometric approach produce an exact algorithm?
2. Can the algebraic formulation produce a sound hardness reduction?
3. Is there a sharper structural theorem for polynomial left inverses that simplifies the existing algorithms?

Below are my detailed recommendations.

# **1. First, clarify what the project is actually trying to establish**

There are three different research objectives.

| Objective | Mathematical question                                     | Current status                                             |
| --------- | --------------------------------------------------------- | ---------------------------------------------------------- |
| DEC       | Is there a feasible observer of prescribed order \\(q\\)? | XP in \\(q\\), FPT in \\(\ell\\)                           |
| OPT       | What is the minimum feasible order?                       | Decidable through order enumeration                        |
| FIND      | Construct a minimum-order observer and certify minimality | Constructive results, with remaining bit-model obligations |

These distinctions should remain explicit throughout the project.

In particular, do not assume that feasibility is monotone in \\(q\\), or that binary search can be used to find the minimum order. The current report does not establish that property.

I would also distinguish two notions of progress:

- **Structural progress:** understanding the admissible subspaces and their components.
- **Complexity progress:** obtaining a deterministic algorithm or a hardness reduction.

The former does not automatically imply the latter.

This distinction is important because the geometric program currently has several promising structural results but not yet a complete decision algorithm.

# **2. My assessment of the four main research directions**

## **Direction A. Deterministic hyperplane case (Q1)**

Highest priority for the geometric programme

This is probably the best immediate mathematical problem.

You already have:

- At most \\(\delta+1\\) irreducible components.
- A vector-bundle description of the components.
- An exact rank identity.
- A randomized one-sided feasibility test.
- An identified exceptional-locus obstruction.

This is a fairly well-defined research problem.

The key remaining issue is not random sampling itself. It is understanding how the gcd of the maximal minors changes under specialization.

### **My recommendation: use the function-field approach, but strengthen it**

I would choose option (i):

1. Compute the generic gcd over the function field of each irreducible component.
2. Determine the locus where its degree increases.
3. Decompose that exceptional locus into irreducible components.
4. Repeat the generic-gcd computation on those components.
5. Continue until the resulting stratification is exhausted.

However, there is an important technical refinement.

You should work with the homogeneous maximal minors of the pencil, rather than relying exclusively on their ordinary affine polynomial degrees.

For example, consider the homogeneous pencil

\\[ Q(s,t)=sX-tG. \\]

Its maximal minors are homogeneous forms of degree \\(\omega\\).

This representation naturally includes the projective point at infinity. Consequently, degree drops in the affine parameter cannot silently disappear from the analysis.

For a family of homogeneous forms, gcd-degree conditions can be expressed using subresultant or appropriate coefficient-matrix rank conditions.

This suggests a more precise formulation:

**Proposed lemma to investigate**

Let \\(Y\\) be an algebraic variety and let

\\[ f_1(y;s,t),\ldots,f_m(y;s,t) \\]

be homogeneous binary forms of fixed degree, depending algebraically on \\(y\in Y\\).

Study the loci

\\[ Y_d= \left\\{ y\in Y: \deg\gcd(f_1(y),\ldots,f_m(y))\ge d \right\\}. \\]

Determine:

- Whether these loci are closed under the relevant nondegeneracy assumptions.
- Their defining determinantal equations.
- Effective degree bounds for their defining equations.
- Whether their irreducible components admit recursive generic-gcd testing.

The advantage is that this becomes an algebraic-geometric problem independent of the observer terminology.

### **Important warning**

A degree bound for the exceptional locus does not, by itself, provide a polynomial-time deterministic algorithm.

You still need to control:

- The number of components.
- Their representation complexity.
- The bit complexity of decomposition.
- The recursion depth.

I would therefore avoid claiming a deterministic algorithm until these issues are addressed.

**My verdict:** This is a strong, manageable next theorem. It can close the first genuinely nontrivial geometric layer.

## **Direction B. Type control (Q2)**

Potentially the most important structural theorem

This direction has greater long-term significance than Q1.

Your conjecture is that, for fixed \\(c\\), the restricted pair

\\[ (\iota|\_W,A|\_W): W\rightrightarrows W+A(W) \\]

admits a finite stratification whose complexity is bounded independently of \\(k\\).

I think the idea is promising, but the formulation needs refinement.

### **The relevant mathematical framework**

The natural language is the representation theory of the Kronecker quiver.

The pair consists of two linear maps with a common domain and codomain:

\\[ W \overset{\iota}{\longrightarrow} W+A(W), \\]

\\[ W \overset{A}{\longrightarrow} W+A(W). \\]

This is a representation of the two-arrow Kronecker quiver.

There is an important subtlety, however.

The Kronecker quiver is tame, not representation-finite. Even for small dimension vectors, its representations can depend on continuous parameters.

For example, when both maps are invertible, one can normalize the first map to the identity, leaving a matrix classified up to similarity. Its eigenvalues vary continuously.

Therefore, you should not formulate type control as a finite classification of isomorphism classes.

Instead, distinguish:

1. Discrete Kronecker data: minimal-index patterns and invariant-factor degree patterns.
2. Continuous moduli: the actual polynomial coefficients or eigenvalue parameters.
3. Geometric incidence data: how the representation is embedded into the ambient space.

For fixed \\(c\\),

\\[ \dim W=c,\qquad \dim(W+A(W))\le 2c. \\]

This is an important observation: the dimensions of the restricted representations are bounded entirely in terms of \\(c\\), regardless of \\(k\\).

It suggests that the number of possible discrete Kronecker profiles may indeed admit a bound depending only on \\(c\\).

But that alone does not establish the desired component bound. The geometry of the embedding into the ambient space must also be controlled.

### **What I would try to prove**

Break the conjecture into three separate statements.

**Statement 1: Finite discrete profiles**

For fixed \\(c\\), there are finitely many possible discrete Kronecker profiles for the restricted pair.

**Statement 2: Algebraic stratification**

The locus corresponding to each profile is constructible, preferably locally closed after a suitable finite refinement.

**Statement 3: Uniform geometric complexity**

The number of relevant irreducible components, or another suitable complexity measure, is bounded by a function of \\(c\\), independently of \\(k\\).

The third statement is the real objective.

I would not assume it follows automatically from the first two.

### **Why this matters**

If you can prove a uniform component bound, the entire layer programme changes.

Instead of treating every \\(c\\) independently, you could obtain a systematic algorithm:

\\[ \text{enumerate discrete types} \longrightarrow \text{construct strata} \longrightarrow \text{test generic feasibility} \longrightarrow \text{handle exceptional loci}. \\]

That is a much more convincing route toward a general algorithm.

**My verdict:** This is the most valuable structural direction, but it is more ambitious than Q1. I would begin with small \\(c\\), especially \\(c=2\\), and seek a theorem that genuinely explains the existing component bound.

## **Direction C. Hardness reduction (Q3 and Q4)**

Highest strategic uncertainty

This is where I would be most careful.

Your report correctly identifies the central problem:

The existing multiplication construction is not sound because \\(R=0\\) can produce a feasible instance that ignores the intended variables.

This is not a minor technical defect.

It means that the construction does not encode the source problem.

I would stop developing local multiplication gates for now.

### **Why the global encoding is more promising**

The desired reduction should encode an entire algebraic object through one global row-space constraint.

The source problem should have a feasible object \\(X\\) satisfying something like

\\[ \operatorname{rank}X\le r, \\]

together with polynomial constraints.

The observer construction would then need to enforce:

1. The existence of the intended object.
2. The correct rank bound.
3. A unique or globally decodable interpretation of its variables.
4. The pencil condition.
5. The absence of degenerate solutions that ignore the encoded object.

The critical requirement is the fourth-to-fifth transition: every feasible observer must decode to a valid source witness.

It is not sufficient that every source witness produces a feasible observer.

You need both directions.

### **My recommendation: prove the translation lemma first**

Before constructing a large reduction, isolate the following theorem.

**Proposed translation lemma**

Construct a polynomial-time mapping from a suitable affine rank-constrained feasibility problem to an observer instance such that

\\[ \text{source instance feasible} \iff \text{observer instance feasible}. \\]

The lemma should explicitly establish:

- Soundness.
- Completeness.
- Rank preservation.
- Polynomial encoding size.
- Compatibility with the common compressed row space \\(\mathcal T\\).
- The identity

\\[ \operatorname{row}H_A=\operatorname{row}H. \\]

I would regard this lemma as the most important milestone in the hardness programme.

If it cannot be proved for a simplified source problem, a more complicated gadget construction will not fix the underlying problem.

### **Which source problem?**

I would investigate affine rank minimization and rank-constrained affine feasibility first.

They are structurally closer to your problem than arbitrary arithmetic-circuit satisfiability.

However, do not assume that fixed-rank-3 hardness automatically transfers.

The translation must preserve the very particular row-wise restriction

\\[ (H_i,(H_A)\_i)\in\mathcal T \\]

with a common \\(\mathcal T\\).

That restriction may be the decisive obstruction.

### **Should you prove a no-go theorem for local gates?**

I would write it as an internal technical result, not yet as a separate paper.

A useful no-go theorem would establish that a specified class of local gate architectures cannot enforce the required global row-space decoding.

That would prevent repeated investment in an approach already known to be structurally inadequate.

**My verdict:** Pursue the global translation lemma. Do not invest heavily in W[1]-hardness until a sound reduction architecture exists.

## **Direction D. Sharper polynomial left-inverse degree bound (Q5)**

Best isolated algebraic problem

This is an especially interesting new observation.

You currently have

\\[ \deg S\le 2\omega-2, \\]

while the computational evidence suggests

\\[ \boxed{\deg S\le\omega-1.} \\]

The evidence is meaningful:

- Exhaustive testing for \\((q,\omega)=(3,2)\\).
- Random exact rational tests up to \\(\omega=5\\).
- No observed instance attaining the elementary upper bound.
- The conjectured upper bound is attained in the tested minimal-height cases.

I would elevate this from a side observation to an independent algebraic problem.

### **A useful normalization**

Since \\(X\\) has full column rank, constant invertible row transformations allow you to write

\\[ X= \begin{bmatrix} I\_\omega\\\ 0 \end{bmatrix}. \\]

Partition

\\[ G= \begin{bmatrix} G_1\\\ G_2 \end{bmatrix}. \\]

Then

\\[ Q(\lambda)= \begin{bmatrix} \lambda I\_\omega-G_1\\\ -G_2 \end{bmatrix}. \\]

The condition that \\(Q(\lambda)\\) have full column rank for every complex \\(\lambda\\) becomes

\\[ \operatorname{rank} \begin{bmatrix} \lambda I\_\omega-G_1\\\ G_2 \end{bmatrix} =\omega \qquad\forall\lambda\in\mathbb C. \\]

This is precisely the Hautus observability condition for the pair \\((G_1,G_2)\\).

That connection is worth exploiting.

It suggests investigating whether the minimum polynomial left-inverse degree can be characterized using:

- Observability indices.
- Controllability indices of the dual pair.
- Polynomial matrix minimal indices.
- Minimal polynomial bases.
- State-space realizations.

In particular, the conjectured bound may be related to the fact that the observability index of an observable \\(\omega\\)-dimensional system is at most \\(\omega\\).

This is a promising route, although it does not by itself prove the polynomial left-inverse degree bound.

### **One important refinement**

Do not only search for an upper bound.

Try to characterize

\\[ d\_{\min}(Q) \\]

in terms of intrinsic invariants of the pair \\((G_1,G_2)\\).

A characterization would be much more valuable than a slightly sharper degree estimate.

For example, it could explain why the minimal-height case \\(q=\omega+1\\) consistently produces degree \\(\omega-1\\).

### **Recommended theorem sequence**

1. Prove invariance under constant equivalence.
2. Establish the observability interpretation.
3. Derive an upper bound using observability indices, if possible.
4. Investigate sharpness.
5. If the conjecture fails, identify the smallest counterexample and determine the correct bound.

**My verdict:** This is a relatively isolated problem with potentially substantial consequences for both the \\(r=0\\) algorithm and the \\(\exists\mathbb R\\) certificate.

I would prioritize it over a general W[1]-hardness investigation.

# **3. Is FPT in&#x20;**\\(q\\)**&#x20;plausible?**

This is Q3, and I think the report draws a conclusion that should be weakened.

You establish that your current encoding has

\\[ \Theta(q^2) \\]

variables when \\(\omega=\Theta(q)\\).

That is a genuine limitation of the current quantifier-elimination approach.

But it is not a lower bound on all possible algorithms.

There are important distinctions:

| Claim                                                                       | Assessment                           |
| --------------------------------------------------------------------------- | ------------------------------------ |
| Current encoding has \\(\Theta(q^2)\\) variables                            | Established                          |
| Current QE approach cannot give the desired FPT bound by simple bookkeeping | Established                          |
| No FPT algorithm in \\(q\\) exists                                          | Not established                      |
| XP is the natural complexity ceiling                                        | Not established                      |
| W[1]-hardness in \\(q\\)                                                    | Interesting target, but no reduction |

I would not yet invest in proving W[1]-hardness.

There are two reasons.

First, your problem already has an FPT algorithm in \\(\ell\\). The relationship between \\(\ell\\), \\(q\\), and the compressed row-space dimensions may offer alternative parameterized approaches.

Second, a W[1]-hardness reduction must respect the observer's special algebraic structure. The same soundness difficulty encountered in the \\(\exists\mathbb R\\)-hardness programme will reappear.

### **A better intermediate question**

Can the unrestricted problem be reduced to a bounded-dimensional algebraic problem whose dimension depends on \\(q\\), but whose coefficient representation has polynomial bit complexity?

Possible approaches include:

- Bounded-rank matrix representations.
- Grassmannian parameterizations.
- Determinantal variety intersections.
- Polynomial-matrix minimal bases.
- Structured low-rank completion.

I would investigate these before committing to a parameterized hardness reduction.

# **4. What is the correct overarching mathematical framework?**

Your Q6 asks whether you should continue developing the layer programme or identify an existing classified problem.

My recommendation is to investigate the following framework:

**Rank-constrained feasibility over a Grassmannian with a polynomial-matrix nondegeneracy condition.**

This captures the essential structure better than treating the problem as an ordinary existential polynomial system.

At a high level, you are selecting nested spaces

\\[ W_0\subseteq W\subseteq\mathcal T \\]

subject to compatibility conditions and

\\[ \dim\pi\_\lambda(W)=\dim\pi_1(W) \qquad \forall\lambda\in\mathbb C. \\]

The first constraints are determinantal and incidence-geometric.

The final constraint is a polynomial-matrix nondegeneracy condition.

These two ingredients are individually well studied, but their intersection is where the difficulty lies.

I would investigate connections to:

1. Quiver Grassmannians and representation varieties.
2. Determinantal varieties and their intersections with Grassmannians.
3. Polynomial matrix completion and polynomial left inverses.
4. Rank-constrained affine feasibility.
5. Parametric linear systems and determinantal divisors.

There is one particularly important distinction.

For a fixed candidate subspace, the spectral condition can be checked using polynomial-matrix algebra.

The difficult part is selecting the subspace.

Thus, I would formulate the central research problem as:

\\[ \boxed{ \text{Existential selection of a structured subspace} + \text{polynomial-matrix nondegeneracy}. } \\]

That formulation may help identify existing complexity results or appropriate hardness sources.

# **5. My recommended priority ordering**

I would not simply follow the order in which the six questions appear in the report.

Here is the ordering I recommend.

## **Recommended research priorities**

**1. Q5 — Left-inverse degree**

Immediate

Establish or refute \\(d\_{\min}\le\omega-1\\). Investigate the observability-index connection and seek an intrinsic characterization.

**2. Q1 — Hyperplane determinism**

Immediate

Develop the homogeneous gcd and subresultant formulation. Aim for a complete deterministic algorithm for \\(c=1\\).

**3. Q4 — Global hardness translation**

Parallel track

Prove a small, explicit sound-and-complete translation lemma before building a full reduction.

**4. Q2 — General type control**

Long-term

First establish finite discrete Kronecker profiles, then investigate the uniform component bound.

**5. Q3 — W[1]-hardness**

Defer

Revisit only after the global encoding architecture is understood.

There is a reason for this ordering.

Q5 and Q1 are concrete mathematical problems with relatively precise success criteria.

Q4 is strategically important because it could settle the complexity direction.

Q2 could eventually provide the strongest algorithmic breakthrough, but it is currently too broad to serve as the immediate main task.

Q3 depends heavily on progress in Q4.

# **6. A concrete research programme**

I would divide the next phase into three work packages.

## **Work package I: Algebraic simplification**

**Objective:** Improve the existing upper-bound machinery.

| Task                      | Deliverable                   |
| ------------------------- | ----------------------------- |
| Normalize the pencil      | Canonical form \\(X=[I;0]\\)  |
| Connect to observability  | Exact equivalence theorem     |
| Study left-inverse degree | Sharp bound or counterexample |
| Improve the certificate   | Reduced polynomial degree     |
| Re-audit \\(r=0\\)        | Updated exact linear system   |

The success criterion is a theorem that improves the existing \\(2\omega-2\\) bound or explains precisely why it cannot be improved.

## **Work package II: Geometric algorithm**

**Objective:** Turn the partial layer programme into a deterministic algorithm.

| Task                        | Deliverable                              |
| --------------------------- | ---------------------------------------- |
| Homogeneous gcd formulation | Exact exceptional-locus equations        |
| Generic-gcd recursion       | Complete hyperplane decision procedure   |
| \\(c=2\\) refinement        | Exact component and fibre classification |
| Kronecker profiles          | Finite discrete stratification           |
| Uniformity analysis         | Component bound depending on \\(c\\)     |

The success criterion is a deterministic exact algorithm for a nontrivial family of unrestricted instances.

## **Work package III: Complexity classification**

**Objective:** Determine whether unrestricted \\(q1\\) is tractable or hard.

| Task                    | Deliverable                                    |
| ----------------------- | ---------------------------------------------- |
| Select source problem   | Rank-constrained affine feasibility            |
| Fix global gauge        | Eliminate degeneracy                           |
| Establish decoding      | Every feasible observer gives a source witness |
| Prove translation lemma | Soundness and completeness                     |
| Complete reduction      | A genuine hardness theorem                     |

The success criterion is a valid complexity classification, not merely a collection of gadgets.

# **7. Important issues I would audit before claiming further results**

There are several points in the report that deserve additional scrutiny.

### **7.1 The bit complexity of the FPT algorithm**

The report states

\\[ \exp(O(\ell^2\log(\ell+2))) \operatorname{poly}(\mathcal L). \\]

This is a strong result.

But the polynomial dependence on input bit length must include:

- Coefficient growth in the Gram–Bézout construction.
- Rational normalization.
- Intermediate matrix dimensions.
- Rank computations.
- Certificate verification.

I would specifically audit whether the polynomial factor has an exponent independent of \\(\ell\\).

Otherwise, the claimed bit-level FPT result could accidentally become XP.

You already identify a remaining FIND bit-model obligation. I would close that before treating the entire algorithmic result as final.

### **7.2 The&#x20;**\\(\exists\mathbb R\\)**&#x20;upper bound**

The report gives

\\[ q1\in\exists\mathbb R. \\]

This is valuable, but the distinction between an upper bound and completeness must be emphasized.

Do not use language suggesting that the problem is \\(\exists\mathbb R\\)-complete until a hardness reduction exists.

### **7.3 The minimum-order construction**

Keep the following separate:

\\[ \mathrm{DEC}(q),\qquad \mathrm{OPT},\qquad \mathrm{FIND}. \\]

In particular, a decision algorithm does not automatically provide a polynomial-time construction of a minimum-order observer.

This is especially important if you eventually present the work as two papers.

### **7.4 Computational evidence**

Your exact rational computations are useful, especially for Q5.

But I recommend maintaining three explicit categories in every research report:

- Proven theorem.
- Exact finite computational verification.
- Conjecture.

Do not let the repeated success of numerical experiments gradually turn into an implicit theorem assumption.

The current report does this well; preserve that discipline.

# **8. How I would position the two papers**

Given the existing division of your project into Paper I and Paper II, I would preserve that separation.

Paper I

**Decision complexity and algebraic certificates**

Main contribution:

- Compression and equivalence.
- Fixed-order XP algorithm.
- Fixed-\\(\ell\\) FPT algorithm.
- \\(\exists\mathbb R\\) membership.
- Exact zero-free-row algorithm.

The paper should focus on decision complexity and certified algorithms.

Paper II

**Minimum order and construction**

Main contribution:

- Minimum-order characterization.
- Order spectrum.
- Lower bounds.
- Constructive observer synthesis.
- Minimality certificates.

The paper should focus on the optimization and construction problem.

I would not put the incomplete hyperplane algorithm, speculative type-control conjecture, and unsound hardness construction into either paper as established results.

Q5 could eventually strengthen Paper I substantially.

The geometric programme could become a separate third contribution if it yields a general deterministic algorithm or a sufficiently strong structural theorem.

I would not create a third paper merely to publish intermediate conjectures.

# **9. My six direct answers**

| Question                   | My recommendation                                                                                                 |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Q1: Hyperplane determinism | Use function-field generic gcd, homogeneous minors, subresultants, and recursive exceptional-locus decomposition. |
| Q2: Type control           | Use Kronecker-quiver representations, but distinguish discrete profiles from continuous moduli.                   |
| Q3: FPT in \\(q\\)         | Still plausible. The current variable count is not a general impossibility result.                                |
| Q4: Hardness               | Prioritize a global rank-decoding translation lemma. Abandon local multiplication gates as the main approach.     |
| Q5: Degree bound           | Investigate the observability-index connection and seek a structural characterization of \\(d\_{\min}\\).         |
| Q6: Task planning          | Prioritize Q5 and Q1, pursue Q4 in parallel, and develop Q2 as the long-term geometric programme.                 |

# **10. My most important strategic suggestion**

I think there is a risk that the project becomes too fragmented.

You currently have several interesting mathematical directions:

- Polynomial matrix theory.
- Algebraic geometry.
- Representation theory.
- Parameterized complexity.
- Algebraic complexity and hardness reductions.

All are relevant, but they should not become five independent research projects.

I would organize the entire effort around one central question:

# **The central research question**

Can the minimum-order functional-observer problem be solved by exploiting the low-dimensional structure of its compressed polynomial pencil, or is the existential selection of its row space inherently computationally hard?

**Algorithmic route**

Establish sharper polynomial-matrix certificates and bounded geometric complexity.

**Hardness route**

Establish a sound global encoding of rank-constrained feasibility.

Everything else should support one of these two routes.

My strongest recommendation is to pursue the two routes in parallel, but with different levels of investment:

- Spend approximately 60% of the mathematical effort on the algebraic and geometric algorithmic programme.
- Spend approximately 40% on the global hardness translation.
- Do not invest substantial time in W[1]-hardness until the reduction architecture has been validated.

The reason is straightforward: you already possess meaningful upper bounds. Another incremental upper-bound improvement is useful, but a deterministic solution of the hyperplane case or a sound hardness reduction would change the overall understanding of the problem much more substantially.

**My assessment:** This is a promising research project with several genuinely substantial results already established. The next breakthrough is unlikely to come from adding another general-purpose certificate. It is more likely to come from either a structural theorem explaining the geometry of the compressed pencil or a global encoding that finally establishes hardness.

I would make those the two defining objectives of the next research phase.

I can also help turn this into a concrete weekly research programme, with individual lemmas, proof obligations, computational experiments, and explicit stopping criteria for each direction.

🔬Weekly research progress review轻点设置